"""Tests for the map data-layer validator (fable-plan.md § 5, rules 1-8). Every
map fixture is built under `tmp_path` from a minimal schema and a handful of
entity files; each violation fixture is checked to isolate exactly one rule
before its assertion is trusted. Run: `uv run pytest tests/map/test_check_map.py`.
"""

from __future__ import annotations

import copy
import datetime
from pathlib import Path

import yaml

from gym.map.check_map import load_schema, main, report, run_checks
from gym.paths import ROOT

# --- minimal schema: same kinds/fields/relations as maps/rust/schema.yaml, trimmed ---

SCHEMA: dict = {
    "kinds": {
        "question": {
            "home": "questions",
            "required": ["text", "concepts", "domains", "status"],
            "fields": {
                "text": {"type": "string"},
                "concepts": {"type": "list", "relation": "concept"},
                "domains": {"type": "list", "relation": "domain"},
                "status": {"type": "enum", "values": ["open", "closed"]},
            },
        },
        "position": {
            "home": "positions",
            "required": ["question", "summary", "tag"],
            "fields": {
                "question": {"type": "string", "relation": "question"},
                "summary": {"type": "string"},
                "tag": {"type": "enum", "values": ["fact", "tradeoff", "taste"]},
            },
        },
        "argument": {
            "home": "arguments",
            "required": ["position", "side", "text", "values"],
            "fields": {
                "position": {"type": "string", "relation": "position"},
                "side": {"type": "enum", "values": ["for", "against"]},
                "text": {"type": "string"},
                "values": {"type": "list", "relation": "value"},
            },
        },
        "value": {
            "home": "values",
            "required": ["text"],
            "fields": {"text": {"type": "string"}},
        },
        "voice": {
            "home": "voices",
            "required": ["name", "type", "track_record"],
            "fields": {
                "name": {"type": "string"},
                "type": {"type": "enum", "values": ["builder", "educator", "language-designer", "institution", "critic", "leaver"]},
                "track_record": {"type": "list"},
            },
        },
        "claim": {
            "home": "claims",
            "required": ["voice", "position", "source", "date", "locator", "paraphrase"],
            "fields": {
                "voice": {"type": "string", "relation": "voice"},
                "position": {"type": "string", "relation": "position", "allow": ["unresolved"]},
                "source": {"type": "string", "relation": "source"},
                "date": {"type": "date"},
                "locator": {"type": "string"},
                "paraphrase": {"type": "string"},
                "quote": {"type": "string"},
                "superseded_by": {"type": "string", "relation": "claim"},
            },
        },
        "source": {
            "home": "sources",
            "required": ["url", "title", "kind", "date", "language"],
            "fields": {
                "url": {"type": "string"},
                "title": {"type": "string"},
                "kind": {"type": "enum", "values": ["post", "talk", "script", "rfc", "thread", "code", "package", "book", "survey"]},
                "date": {"type": "date"},
                "language": {"type": "enum", "values": ["en", "zh", "de", "fr", "uk"]},
            },
        },
        "convention": {
            "home": "conventions",
            "required": ["position", "prevalence"],
            "fields": {
                "position": {"type": "string", "relation": "position"},
                "prevalence": {"type": "list"},
                "dissent": {"type": "list", "relation": "claim"},
            },
        },
        "domain": {
            "home": "domains",
            "required": ["text"],
            "fields": {"text": {"type": "string"}},
        },
        "concept": {
            "home": "concepts",
            "required": ["text"],
            "fields": {"text": {"type": "string"}, "related": {"type": "list", "relation": "concept"}},
        },
        "check": {
            "home": "checks",
            "list": True,
            "required": ["check", "run_a", "run_b", "agree"],
            "fields": {
                "check": {"type": "enum", "values": ["fill-position", "fill-tag", "paired-cases", "itt", "merge", "judge"]},
                "run_a": {"type": "map"},
                "run_b": {"type": "map"},
                "agree": {"type": "bool"},
                "grader": {"type": "map"},
            },
        },
    }
}

DATE = datetime.date(2026, 1, 1)


def write_entity(map_dir: Path, kind: str, entity_id: str, data: dict) -> None:
    home = SCHEMA["kinds"][kind]["home"]
    directory = map_dir / home
    directory.mkdir(parents=True, exist_ok=True)
    (directory / f"{entity_id}.yaml").write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def write_check(map_dir: Path, entity_id: str, records: list[dict]) -> None:
    directory = map_dir / "checks"
    directory.mkdir(parents=True, exist_ok=True)
    (directory / f"{entity_id}.yaml").write_text(yaml.safe_dump(records, sort_keys=False), encoding="utf-8")


def build_map(map_dir: Path, entities: dict[str, list[tuple[str, dict]]], checks: dict[str, list[dict]] | None = None) -> None:
    map_dir.mkdir(parents=True, exist_ok=True)
    (map_dir / "schema.yaml").write_text(yaml.safe_dump(SCHEMA, sort_keys=False), encoding="utf-8")
    for kind, items in entities.items():
        for entity_id, data in items:
            write_entity(map_dir, kind, entity_id, data)
    for entity_id, records in (checks or {}).items():
        write_check(map_dir, entity_id, records)


# --- a minimal, fully valid map: one entity of every kind, an open Question ---


def minimal_open_entities() -> dict[str, list[tuple[str, dict]]]:
    return {
        "domain": [("dom1", {"id": "dom1", "text": "core"})],
        "concept": [("con1", {"id": "con1", "text": "ownership"})],
        "question": [("q1", {"id": "q1", "text": "x?", "concepts": ["con1"], "domains": ["dom1"], "status": "open"})],
        "position": [("p1", {"id": "p1", "question": "q1", "summary": "s", "tag": "fact"})],
        "value": [("v1", {"id": "v1", "text": "safety"})],
        "argument": [("arg1", {"id": "arg1", "position": "p1", "side": "for", "text": "t", "values": ["v1"]})],
        "voice": [("voice1", {"id": "voice1", "name": "V", "type": "builder", "track_record": [{"url": "https://example.com/v1"}]})],
        "source": [("src1", {"id": "src1", "url": "https://example.com/s1", "title": "T", "kind": "post", "date": DATE, "language": "en"})],
        "claim": [("claim1", {"id": "claim1", "voice": "voice1", "position": "p1", "source": "src1", "date": DATE, "locator": "p.1", "paraphrase": "p"})],
        "convention": [("conv1", {"id": "conv1", "position": "p1", "prevalence": [{"url": "https://example.com/c1", "date": DATE}]})],
    }


def test_clean_minimal_map_yields_zero_fail(tmp_path: Path) -> None:
    build_map(tmp_path, minimal_open_entities())
    findings = run_checks(tmp_path)
    assert findings == []


def test_rule8_report_matches_hand_count(tmp_path: Path) -> None:
    build_map(tmp_path, minimal_open_entities())
    from gym.map.check_map import load_entities

    entities, parse_findings = load_entities(tmp_path, load_schema(tmp_path))
    assert parse_findings == []
    text = report(entities)
    # one entity of every kind but question/position/argument/value/voice/source/claim/convention/domain/concept = 1 each
    for kind in ["question", "position", "argument", "value", "voice", "claim", "source", "convention", "domain", "concept"]:
        assert f"{kind}: 1" in text
    assert "dom1: questions open=1 closed=0" in text
    assert "claims confirmed (resolved to a Position): 1 / 1" in text
    assert "voices: 1" in text


# --- Rule 1: shape (parse, id, uniqueness, known fields, required, enums) ---


def test_rule1_missing_required_field(tmp_path: Path) -> None:
    entities = minimal_open_entities()
    q_id, q_data = entities["question"][0]
    q_data = dict(q_data)
    del q_data["text"]
    entities["question"] = [(q_id, q_data)]
    build_map(tmp_path, entities)
    findings = run_checks(tmp_path)
    assert len(findings) == 1
    assert findings[0].level == "FAIL"
    assert "q1.yaml" in findings[0].where
    assert "missing required field 'text'" in findings[0].message


def test_rule1_id_mismatch_with_filename(tmp_path: Path) -> None:
    entities = minimal_open_entities()
    q_id, q_data = entities["question"][0]
    q_data = dict(q_data)
    q_data["id"] = "not-q1"
    entities["question"] = [(q_id, q_data)]  # filename stays q1.yaml, id field says otherwise
    build_map(tmp_path, entities)
    findings = run_checks(tmp_path)
    assert len(findings) == 1
    assert "does not equal the filename 'q1'" in findings[0].message


def test_rule1_illegal_enum_value(tmp_path: Path) -> None:
    entities = minimal_open_entities()
    q_id, q_data = entities["question"][0]
    q_data = dict(q_data)
    q_data["status"] = "half-open"
    entities["question"] = [(q_id, q_data)]
    build_map(tmp_path, entities)
    findings = run_checks(tmp_path)
    assert len(findings) == 1
    assert "status value 'half-open' is not one of" in findings[0].message


def test_rule1_passes_on_baseline(tmp_path: Path) -> None:
    build_map(tmp_path, minimal_open_entities())
    findings = run_checks(tmp_path)
    assert findings == []


# --- Rule 2: relations resolve to an existing file of the right kind ---


def test_rule2_dangling_relation(tmp_path: Path) -> None:
    entities = minimal_open_entities()
    p_id, p_data = entities["position"][0]
    p_data = dict(p_data)
    p_data["question"] = "no-such-question"
    entities["position"] = [(p_id, p_data)]
    build_map(tmp_path, entities)
    findings = run_checks(tmp_path)
    assert len(findings) == 1
    assert "p1.yaml" in findings[0].where
    assert "question 'no-such-question' does not resolve to a question" in findings[0].message


def test_rule2_passes_on_baseline(tmp_path: Path) -> None:
    build_map(tmp_path, minimal_open_entities())
    assert run_checks(tmp_path) == []


# --- Rule 3: Claim shape (ISO date, quote cap, non-empty locator, superseded_by) ---


def test_rule3_date_not_iso(tmp_path: Path) -> None:
    entities = minimal_open_entities()
    c_id, c_data = entities["claim"][0]
    c_data = dict(c_data)
    c_data["date"] = "not-a-date"
    entities["claim"] = [(c_id, c_data)]
    build_map(tmp_path, entities)
    findings = run_checks(tmp_path)
    assert len(findings) == 1
    assert "claim1.yaml" in findings[0].where
    assert "date 'not-a-date' is not ISO" in findings[0].message


def test_rule3_quote_over_cap(tmp_path: Path) -> None:
    entities = minimal_open_entities()
    c_id, c_data = entities["claim"][0]
    c_data = dict(c_data)
    c_data["quote"] = "x" * 301
    entities["claim"] = [(c_id, c_data)]
    build_map(tmp_path, entities)
    findings = run_checks(tmp_path)
    assert len(findings) == 1
    assert "quote is 301 characters, over the 300-character cap" in findings[0].message


def test_rule3_empty_locator(tmp_path: Path) -> None:
    entities = minimal_open_entities()
    c_id, c_data = entities["claim"][0]
    c_data = dict(c_data)
    c_data["locator"] = "   "
    entities["claim"] = [(c_id, c_data)]
    build_map(tmp_path, entities)
    findings = run_checks(tmp_path)
    assert len(findings) == 1
    assert "locator is empty" in findings[0].message


def test_rule3_passes_on_baseline(tmp_path: Path) -> None:
    build_map(tmp_path, minimal_open_entities())
    assert run_checks(tmp_path) == []


# --- Rules 4 and 5: a closed Question's evidence minimum ---


def full_evidence_position(position_id: str, question_id: str, voice_a: str, voice_b: str, source_a: str, source_b: str) -> dict:
    """A closed Question's Position that passes rule 5 in full: 2 resolved Claims
    from 2 distinct Voices, an Argument with >=1 Value, a passing fill-tag check
    and a passing itt check."""
    return {
        "position": {"id": position_id, "question": question_id, "summary": "s", "tag": "fact"},
        "arguments": [
            {"id": f"{position_id}-arg", "position": position_id, "side": "for", "text": "t", "values": ["v1"]},
        ],
        "claims": [
            {"id": f"{position_id}-c1", "voice": voice_a, "position": position_id, "source": source_a, "date": DATE, "locator": "p.1", "paraphrase": "p"},
            {"id": f"{position_id}-c2", "voice": voice_b, "position": position_id, "source": source_b, "date": DATE, "locator": "p.2", "paraphrase": "p"},
        ],
        "checks": {
            position_id: [
                {"check": "fill-tag", "run_a": {}, "run_b": {}, "agree": True},
                {"check": "itt", "run_a": {}, "run_b": {}, "agree": True, "grader": {"verdict": "pass"}},
            ],
            f"{position_id}-c1": [{"check": "fill-position", "run_a": {}, "run_b": {}, "agree": True}],
            f"{position_id}-c2": [{"check": "fill-position", "run_a": {}, "run_b": {}, "agree": True}],
        },
    }


def closed_question_map_entities() -> tuple[dict[str, list[tuple[str, dict]]], dict[str, list[dict]]]:
    entities: dict[str, list[tuple[str, dict]]] = {
        "domain": [("dom1", {"id": "dom1", "text": "core"})],
        "concept": [("con1", {"id": "con1", "text": "ownership"})],
        "question": [("q1", {"id": "q1", "text": "x?", "concepts": ["con1"], "domains": ["dom1"], "status": "closed"})],
        "value": [("v1", {"id": "v1", "text": "safety"})],
        "voice": [
            ("voiceA", {"id": "voiceA", "name": "A", "type": "builder", "track_record": [{"url": "https://example.com/a"}]}),
            ("voiceB", {"id": "voiceB", "name": "B", "type": "critic", "track_record": [{"url": "https://example.com/b"}]}),
        ],
        "source": [
            ("srcA", {"id": "srcA", "url": "https://example.com/sa", "title": "TA", "kind": "post", "date": DATE, "language": "en"}),
            ("srcB", {"id": "srcB", "url": "https://example.com/sb", "title": "TB", "kind": "post", "date": DATE, "language": "en"}),
        ],
        "position": [],
        "argument": [],
        "claim": [],
    }
    checks: dict[str, list[dict]] = {}

    p1 = full_evidence_position("p1", "q1", "voiceA", "voiceB", "srcA", "srcB")
    p2 = full_evidence_position("p2", "q1", "voiceA", "voiceB", "srcA", "srcB")
    for p in (p1, p2):
        entities["position"].append((p["position"]["id"], p["position"]))
        for arg in p["arguments"]:
            entities["argument"].append((arg["id"], arg))
        for claim in p["claims"]:
            entities["claim"].append((claim["id"], claim))
        checks.update(p["checks"])

    return entities, checks


def test_closed_question_with_full_evidence_passes(tmp_path: Path) -> None:
    entities, checks = closed_question_map_entities()
    build_map(tmp_path, entities, checks)
    findings = run_checks(tmp_path)
    assert findings == []


def test_rule4_closed_question_with_one_position(tmp_path: Path) -> None:
    entities, checks = closed_question_map_entities()
    entities = copy.deepcopy(entities)
    # drop p2 (and its argument/claims/checks) so q1 has only 1 Position, but p1 stays fully valid
    entities["position"] = [item for item in entities["position"] if item[0] == "p1"]
    entities["argument"] = [item for item in entities["argument"] if item[0].startswith("p1-")]
    entities["claim"] = [item for item in entities["claim"] if item[0].startswith("p1-")]
    checks = {k: v for k, v in checks.items() if k.startswith("p1")}
    build_map(tmp_path, entities, checks)
    findings = run_checks(tmp_path)
    assert len(findings) == 1
    assert "closed with 1 Position(s), needs >=2" in findings[0].message


def test_rule5_closed_position_missing_itt_pass(tmp_path: Path) -> None:
    entities, checks = closed_question_map_entities()
    # p2 keeps its fill-tag check but loses its itt-pass check; p1 stays fully valid, so q1 still has 2 Positions
    checks = dict(checks)
    checks["p2"] = [record for record in checks["p2"] if record["check"] != "itt"]
    build_map(tmp_path, entities, checks)
    findings = run_checks(tmp_path)
    assert len(findings) == 1
    assert "p2.yaml" in findings[0].where
    assert "summary has no passing itt check" in findings[0].message


def test_rule5_closed_position_no_argument_with_value(tmp_path: Path) -> None:
    entities, checks = closed_question_map_entities()
    entities = copy.deepcopy(entities)
    # p2 loses its Argument entirely (an empty `values: []` would itself fail rule 1's
    # required-field check, since values is required and `[]` is falsy) — everything
    # else about p2 stays valid, so this isolates rule 5's "no Argument with >=1 Value"
    entities["argument"] = [item for item in entities["argument"] if item[0] != "p2-arg"]
    build_map(tmp_path, entities, checks)
    findings = run_checks(tmp_path)
    assert len(findings) == 1
    assert "p2.yaml" in findings[0].where
    assert "no Argument with >=1 Value" in findings[0].message


# --- Rule 6: Voice track_record ---


def test_rule6_voice_track_record_without_url(tmp_path: Path) -> None:
    entities = minimal_open_entities()
    v_id, v_data = entities["voice"][0]
    v_data = dict(v_data)
    v_data["track_record"] = [{"note": "no url here"}]
    entities["voice"] = [(v_id, v_data)]
    build_map(tmp_path, entities)
    findings = run_checks(tmp_path)
    assert len(findings) == 1
    assert "voice1.yaml" in findings[0].where
    assert "no track_record line with a url" in findings[0].message


def test_rule6_passes_on_baseline(tmp_path: Path) -> None:
    build_map(tmp_path, minimal_open_entities())
    assert run_checks(tmp_path) == []


# --- Rule 7: Convention prevalence ---


def test_rule7_convention_prevalence_without_date(tmp_path: Path) -> None:
    entities = minimal_open_entities()
    c_id, c_data = entities["convention"][0]
    c_data = dict(c_data)
    c_data["prevalence"] = [{"url": "https://example.com/c1"}]  # no date
    entities["convention"] = [(c_id, c_data)]
    build_map(tmp_path, entities)
    findings = run_checks(tmp_path)
    assert len(findings) == 1
    assert "conv1.yaml" in findings[0].where
    assert "no prevalence line with a url and a date" in findings[0].message


def test_rule7_passes_on_baseline(tmp_path: Path) -> None:
    build_map(tmp_path, minimal_open_entities())
    assert run_checks(tmp_path) == []


# --- Rule 8: report is descriptive counts, not a FAIL rule; no violation fixture applies ---
# (see test_rule8_report_matches_hand_count above, and Open Problems in the report)


# --- Live maps/rust: a regression guard on today's declared gap count ---


def test_live_rust_map_declared_gap_count() -> None:
    # measured 2026-09-30 via `uv run gym map check --map maps/rust`: 417 FAIL.
    # A change to this number should be a deliberate map edit, not a silent regression.
    findings = run_checks(ROOT / "maps" / "rust")
    assert len(findings) == 417


def test_main_exit_code_matches_findings(tmp_path: Path) -> None:
    build_map(tmp_path, minimal_open_entities())
    assert main(tmp_path) == 0
    entities = minimal_open_entities()
    q_id, q_data = entities["question"][0]
    q_data = dict(q_data)
    del q_data["text"]
    entities["question"] = [(q_id, q_data)]
    build_map(tmp_path, entities)
    assert main(tmp_path) == 1
