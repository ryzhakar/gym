"""Tests for the Concept dedup command (src/gym/map/concepts.py).

Run: `uv run pytest tests/map/test_concepts.py -q`.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from gym.map import check_map
from gym.map.concepts import (
    SHORT_NAME_CHARS,
    ConceptFile,
    canonical,
    load_concepts,
    load_question_links,
    main,
    normalise,
    plan_merges,
    similarity,
)

# --- normalisation ---


def test_normalise_lowercases_and_strips_punctuation() -> None:
    assert normalise("ABI Stability!") == "abi stability"


def test_normalise_strips_accents_to_ascii() -> None:
    assert normalise("Café Über") == "cafe uber"


def test_normalise_treats_hyphens_as_word_breaks() -> None:
    assert normalise("async-await-syntax") == normalise("async await syntax")


def test_normalise_drops_stop_words() -> None:
    assert normalise("actor vs shared locks") == normalise("actor shared locks")


def test_normalise_singularises() -> None:
    assert normalise("traits") == normalise("trait")
    assert normalise("dependencies") == normalise("dependency")
    assert normalise("processes") == normalise("process")


def test_normalise_folds_synonym_pairs() -> None:
    assert normalise("async runtime") == normalise("asynchronous runtime")
    assert normalise("config file") == normalise("configuration file")


def test_normalise_short_word_not_over_singularised() -> None:
    # "gas" (<=3 chars after strip) must not become "ga"
    assert normalise("gas") == "gas"


# --- tier fixtures ---


def _concept(cid: str, text: str) -> ConceptFile:
    return ConceptFile(id=cid, path=Path(f"/fake/{cid}.yaml"), data={"id": cid, "text": text})


def test_tier1_merges_identical_normalised_names_into_the_one_with_more_questions() -> None:
    concepts = {
        "wasm": _concept("wasm", "WASM"),
        "wasm-2": _concept("wasm-2", "Wasm"),
    }
    by_question = {"wasm": {"q1", "q2"}, "wasm-2": {"q3"}}
    plan = plan_merges(concepts, by_question, {})
    assert plan.counts()["tier1"] == 1
    merge = plan.merges[0]
    assert merge.loser == "wasm-2"
    assert merge.canonical == "wasm"


def test_tier1_tie_breaks_on_lexicographically_smaller_id() -> None:
    concepts = {
        "futures": _concept("futures", "Futures"),
        "futures-2": _concept("futures-2", "futures"),
    }
    by_question: dict[str, set[str]] = {}
    plan = plan_merges(concepts, by_question, {})
    assert plan.merges[0].canonical == "futures"
    assert plan.merges[0].loser == "futures-2"


#  similarity('async runtime scheduler', 'async runtime scheduling') = 0.918
#  after normalisation, verified with concepts.similarity() directly — a
#  real tier-2 pair, not a guessed one.


def test_tier2_merges_near_duplicates_sharing_a_question() -> None:
    concepts = {
        "async-runtime-scheduler": _concept("async-runtime-scheduler", "async runtime scheduler"),
        "async-runtime-scheduling": _concept("async-runtime-scheduling", "async runtime scheduling"),
    }
    by_question = {
        "async-runtime-scheduler": {"q1"},
        "async-runtime-scheduling": {"q1", "q2"},
    }
    plan = plan_merges(concepts, by_question, {})
    assert plan.counts()["tier2"] == 1
    merge = plan.merges[0]
    # more Questions wins
    assert merge.canonical == "async-runtime-scheduling"
    assert merge.loser == "async-runtime-scheduler"


def test_tier2_requires_shared_question_or_domain_even_above_threshold() -> None:
    concepts = {
        "async-runtime-scheduler": _concept("async-runtime-scheduler", "async runtime scheduler"),
        "async-runtime-scheduling": _concept("async-runtime-scheduling", "async runtime scheduling"),
    }
    plan = plan_merges(concepts, {}, {})  # no shared Question, no shared Domain
    assert plan.counts()["tier1"] == 0
    assert plan.counts()["tier2"] == 0


def test_tier2_gate_satisfied_by_shared_domain_alone() -> None:
    # both normalised names are >= SHORT_NAME_CHARS, so Domain alone suffices
    concepts = {
        "async-runtime-scheduler": _concept("async-runtime-scheduler", "async runtime scheduler"),
        "async-runtime-scheduling": _concept("async-runtime-scheduling", "async runtime scheduling"),
    }
    by_domain = {"async-runtime-scheduler": {"embedded"}, "async-runtime-scheduling": {"embedded", "web"}}
    plan = plan_merges(concepts, {}, by_domain)
    assert plan.counts()["tier2"] == 1


def test_tier2_short_names_require_a_shared_question_not_domain_alone() -> None:
    # 'locking'/'blocking': similarity 0.93, normalised names 7/8 chars, both
    # under SHORT_NAME_CHARS — the real false merge this rule exists to stop.
    concepts = {
        "locking": _concept("locking", "locking"),
        "blocking": _concept("blocking", "blocking"),
    }
    by_domain = {"locking": {"async"}, "blocking": {"async", "web"}}
    plan = plan_merges(concepts, {}, by_domain)  # shared Domain only, no shared Question
    assert plan.counts()["tier2"] == 0
    assert plan.counts()["tier1"] == 0


def test_tier2_short_names_still_merge_on_a_shared_question() -> None:
    concepts = {
        "locking": _concept("locking", "locking"),
        "blocking": _concept("blocking", "blocking"),
    }
    by_question = {"locking": {"q1"}, "blocking": {"q1", "q2"}}
    plan = plan_merges(concepts, by_question, {"locking": {"async"}, "blocking": {"async"}})
    assert plan.counts()["tier2"] == 1
    assert plan.merges[0].loser == "locking"
    assert plan.merges[0].canonical == "blocking"


def test_tier2_short_name_rule_checked_against_the_real_map_finds_no_mixed_pair() -> None:
    # difflib/rapidfuzz ratio caps at 2*min_len/(len_a+len_b): a short and a
    # long normalised name structurally cannot reach 0.88 together, so a
    # "one side short, one side long, still >= 0.88" fixture can't be built
    # from real words — confirmed empirically over every canonical Concept
    # in maps/rust/concepts/*.yaml (checked before writing this test, not
    # assumed): zero such pairs exist. The short<->short case above
    # ('locking'/'blocking') is the one that occurs in practice.
    import glob

    import yaml as _yaml

    texts = {}
    for path in glob.glob("maps/rust/concepts/*.yaml"):
        data = _yaml.safe_load(open(path))
        if data.get("merged_into"):
            continue
        texts[data["id"]] = normalise(data.get("text") or data["id"])
    short = {cid: n for cid, n in texts.items() if len(n) < SHORT_NAME_CHARS}
    long_ = {cid: n for cid, n in texts.items() if len(n) >= SHORT_NAME_CHARS}
    mixed_hits = [
        (a, b)
        for a, na in short.items()
        for b, nb in long_.items()
        if similarity(na, nb) >= 0.88
    ]
    assert mixed_hits == []


def test_tier3_lists_but_does_not_merge() -> None:
    # similarity('rust trait object', 'rust trait object usage') = 0.85,
    # verified with concepts.similarity() directly — inside [0.75, 0.88).
    concepts = {
        "rust-trait-object": _concept("rust-trait-object", "rust trait object"),
        "rust-trait-objects-usage": _concept("rust-trait-objects-usage", "rust trait objects usage"),
    }
    plan = plan_merges(
        concepts,
        {"rust-trait-object": {"q1"}, "rust-trait-objects-usage": {"q1"}},
        {},
    )
    assert plan.counts()["tier1"] == 0
    assert plan.counts()["tier2"] == 0
    assert len(plan.tier3_pairs) == 1
    a, b, sim = plan.tier3_pairs[0]
    assert {a, b} == {"rust-trait-object", "rust-trait-objects-usage"}
    assert 0.75 <= sim < 0.88


def test_tier1_winner_further_merged_in_tier2_is_flattened() -> None:
    # "async-runtime-scheduler" and "-scheduler-2" are identical post-
    # normalisation (tier 1; scheduler has more Questions so it wins that
    # round). "async-runtime-scheduler" then near-duplicates
    # "async-runtime-scheduling" (0.918 similarity) sharing q1 (tier 2), and
    # scheduling has more Questions, so the tier-1 WINNER itself gets
    # merged. "-scheduler-2" must end up pointing directly at the final
    # canonical "async-runtime-scheduling", never at "async-runtime-scheduler".
    concepts = {
        "async-runtime-scheduler": _concept("async-runtime-scheduler", "async runtime scheduler"),
        "async-runtime-scheduler-2": _concept("async-runtime-scheduler-2", "async runtime scheduler"),
        "async-runtime-scheduling": _concept("async-runtime-scheduling", "async runtime scheduling"),
    }
    by_question = {
        "async-runtime-scheduler": {"q1"},
        "async-runtime-scheduler-2": set(),
        "async-runtime-scheduling": {"q1", "q2", "q3"},
    }
    plan = plan_merges(concepts, by_question, {})
    by_loser = {m.loser: m.canonical for m in plan.merges}
    assert by_loser["async-runtime-scheduler"] == "async-runtime-scheduling"
    assert by_loser["async-runtime-scheduler-2"] == "async-runtime-scheduling"
    # no merge may point at a Concept that is itself a loser
    losers = set(by_loser)
    for target in by_loser.values():
        assert target not in losers


# --- canonical() helper ---


def test_canonical_resolves_through_a_chain_defensively() -> None:
    concepts = {
        "a": {"id": "a", "text": "a", "merged_into": "b"},
        "b": {"id": "b", "text": "b", "merged_into": "c"},
        "c": {"id": "c", "text": "c"},
    }
    assert canonical("a", concepts) == "c"


def test_canonical_returns_self_when_not_merged() -> None:
    concepts = {"a": {"id": "a", "text": "a"}}
    assert canonical("a", concepts) == "a"


def test_canonical_returns_self_for_unknown_id() -> None:
    assert canonical("missing", {}) == "missing"


# --- full command: fixture on disk ---


def _write_concept(map_dir: Path, cid: str, text: str) -> None:
    (map_dir / "concepts" / f"{cid}.yaml").write_text(
        yaml.safe_dump({"id": cid, "text": text}, sort_keys=False), encoding="utf-8"
    )


def _write_question(map_dir: Path, qid: str, concept_ids: list[str], domains: list[str]) -> None:
    (map_dir / "questions" / f"{qid}.yaml").write_text(
        yaml.safe_dump(
            {"id": qid, "text": qid, "concepts": concept_ids, "domains": domains, "status": "open"},
            sort_keys=False,
        ),
        encoding="utf-8",
    )


def _build_fixture(tmp_path: Path) -> Path:
    map_dir = tmp_path / "map"
    (map_dir / "concepts").mkdir(parents=True)
    (map_dir / "questions").mkdir(parents=True)
    _write_concept(map_dir, "wasm", "WASM")
    _write_concept(map_dir, "wasm-2", "Wasm")
    _write_concept(map_dir, "rust-traits", "Rust traits")
    _write_question(map_dir, "q1", ["wasm", "rust-traits"], ["web"])
    _write_question(map_dir, "q2", ["wasm-2"], ["web"])
    return map_dir


def test_load_concepts_and_question_links_roundtrip(tmp_path: Path) -> None:
    map_dir = _build_fixture(tmp_path)
    concepts = load_concepts(map_dir)
    assert set(concepts) == {"wasm", "wasm-2", "rust-traits"}
    by_question, by_domain = load_question_links(map_dir)
    assert by_question["wasm"] == {"q1"}
    assert by_domain["wasm-2"] == {"web"}


def test_main_apply_writes_merged_into_and_is_idempotent(tmp_path: Path, capsys) -> None:
    map_dir = _build_fixture(tmp_path)

    main(map_dir, apply=False, report_path=None)
    before = yaml.safe_load((map_dir / "concepts" / "wasm-2.yaml").read_text())
    assert "merged_into" not in before

    main(map_dir, apply=True, report_path=None)
    after = yaml.safe_load((map_dir / "concepts" / "wasm-2.yaml").read_text())
    assert after["merged_into"] == "wasm"
    # nothing else on the file changed
    assert after["id"] == "wasm-2"
    assert after["text"] == "Wasm"

    canonical_file = yaml.safe_load((map_dir / "concepts" / "wasm.yaml").read_text())
    assert "merged_into" not in canonical_file

    # idempotent: a second apply writes nothing further
    capsys.readouterr()
    main(map_dir, apply=True, report_path=None)
    out = capsys.readouterr().out
    assert "wrote merged_into to 0 Concept file(s)" in out


def test_main_writes_report_with_merges_and_tier3(tmp_path: Path) -> None:
    map_dir = _build_fixture(tmp_path)
    report_path = tmp_path / "report.md"
    main(map_dir, apply=False, report_path=report_path)
    text = report_path.read_text()
    assert "wasm-2" in text
    assert "tier1 merges: 1" in text


# --- check_map rule: merged_into must point at a canonical Concept ---
#
# Reuses test_check_map.SCHEMA (the same kinds/fields/relations as
# maps/rust/schema.yaml, trimmed) with `merged_into` added to `concept`,
# exactly as this task adds it to the real schema.yaml.


def _write_schema(map_dir: Path) -> None:
    import copy

    from test_check_map import SCHEMA as _base_schema

    schema = copy.deepcopy(_base_schema)
    schema["kinds"]["concept"]["fields"]["merged_into"] = {"type": "string", "relation": "concept"}
    (map_dir / "concepts").mkdir(parents=True, exist_ok=True)
    (map_dir / "questions").mkdir(parents=True, exist_ok=True)
    (map_dir / "schema.yaml").write_text(yaml.safe_dump(schema, sort_keys=False), encoding="utf-8")


def test_check_rule_passes_when_merged_into_points_at_a_canonical_concept(tmp_path: Path) -> None:
    map_dir = tmp_path / "map"
    _write_schema(map_dir)
    _write_concept(map_dir, "wasm", "WASM")
    _write_concept(map_dir, "wasm-2", "Wasm")
    (map_dir / "concepts" / "wasm-2.yaml").write_text(
        yaml.safe_dump({"id": "wasm-2", "text": "Wasm", "merged_into": "wasm"}, sort_keys=False),
        encoding="utf-8",
    )
    findings = check_map.run_checks(map_dir)
    assert not any("merged_into" in f.message for f in findings)


def test_check_rule_fails_when_merged_into_points_at_a_merged_concept(tmp_path: Path) -> None:
    map_dir = tmp_path / "map"
    _write_schema(map_dir)
    (map_dir / "concepts").mkdir(parents=True, exist_ok=True)
    (map_dir / "concepts" / "a.yaml").write_text(
        yaml.safe_dump({"id": "a", "text": "a", "merged_into": "b"}, sort_keys=False), encoding="utf-8"
    )
    (map_dir / "concepts" / "b.yaml").write_text(
        yaml.safe_dump({"id": "b", "text": "b", "merged_into": "c"}, sort_keys=False), encoding="utf-8"
    )
    (map_dir / "concepts" / "c.yaml").write_text(
        yaml.safe_dump({"id": "c", "text": "c"}, sort_keys=False), encoding="utf-8"
    )
    findings = check_map.run_checks(map_dir)
    messages = [f.message for f in findings if "merged_into" in f.message]
    assert any("'b' is itself merged, not canonical" in m for m in messages)
