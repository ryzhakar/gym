"""Tests for the Matrix's two-way co-clustering. Run: `uv run pytest tests/map/test_cluster.py`."""

from __future__ import annotations

import random
from pathlib import Path

import yaml

from gym.map.cluster import cocluster
from gym.paths import ROOT

# `gym.map.site` is mid-refactor by a concurrent agent as this is written
# (its __init__ imports a page.py that does not exist yet) and is out of
# this task's scope to touch, so this test reads the map's YAML directly
# rather than importing the in-flux site package.


def _load_kind(map_dir: Path, name: str) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for f in sorted((map_dir / name).glob("*.yaml")):
        out[f.stem] = yaml.safe_load(f.read_text()) or {}
    return out


def _planted_schools(seed: int, n_schools: int = 3, qs_per_school: int = 10, vs_per_school: int = 8):
    """Three planted Schools: each owns its own Questions and Voices; each
    Voice agrees with its School's single stance on each of its School's
    Questions with probability 0.9 (else a random off-School position,
    modelling a dissenting Claim); a few cross-School cells are added so the
    graph is not perfectly block-diagonal by construction alone.
    """
    rng = random.Random(seed)
    cells: dict[tuple[str, str], str] = {}
    school_questions: dict[int, list[str]] = {}
    school_voices: dict[int, list[str]] = {}
    house_position: dict[str, str] = {}

    for s in range(n_schools):
        qs = [f"s{s}-q{i}" for i in range(qs_per_school)]
        vs = [f"s{s}-v{i}" for i in range(vs_per_school)]
        school_questions[s] = qs
        school_voices[s] = vs
        for q in qs:
            house_position[q] = f"{q}--house"
        for q in qs:
            for v in vs:
                if rng.random() < 0.9:
                    cells[(q, v)] = house_position[q]
                else:
                    cells[(q, v)] = f"{q}--dissent-{rng.randint(0, 3)}"

    # cross-school noise, added once every school's questions/voices exist
    for s in range(n_schools):
        for _ in range(5):
            q = rng.choice(school_questions[s])
            other = rng.choice([o for o in range(n_schools) if o != s])
            v = rng.choice(school_voices[other])
            cells[(q, v)] = f"{q}--cross-{rng.randint(0, 3)}"

    return cells, school_questions, school_voices


def _best_overlap_fraction(planted_groups: list[list[str]], found_groups: list[list[str]]) -> float:
    """Match each planted group to the found group with the largest
    intersection (greedy, each found group used at most once), and return
    total matched elements / total planted elements.
    """
    found = [set(g) for g in found_groups]
    used: set[int] = set()
    matched = 0
    total = sum(len(g) for g in planted_groups)
    for planted in planted_groups:
        planted_set = set(planted)
        best_i, best_overlap = None, -1
        for i, f in enumerate(found):
            if i in used:
                continue
            overlap = len(planted_set & f)
            if overlap > best_overlap:
                best_i, best_overlap = i, overlap
        if best_i is not None:
            used.add(best_i)
            matched += best_overlap
    return matched / total if total else 0.0


def test_recovers_three_planted_schools() -> None:
    cells, school_questions, school_voices = _planted_schools(seed=42)
    result = cocluster(cells)

    assert result.k == 3, f"expected 3 recovered clusters, got {result.k}"

    planted_rows = list(school_questions.values())
    planted_cols = list(school_voices.values())
    row_fraction = _best_overlap_fraction(planted_rows, result.row_groups)
    col_fraction = _best_overlap_fraction(planted_cols, result.col_groups)

    assert row_fraction >= 0.9, f"row (question) membership recovery {row_fraction:.2%} < 90%"
    assert col_fraction >= 0.9, f"col (voice) membership recovery {col_fraction:.2%} < 90%"

    # every block should show near-total fill (schools are fully populated)
    # and high within-question stance agreement (house position dominates)
    for block in result.blocks:
        if block.row_group and block.col_group:
            assert block.fill_ratio > 0.9
            assert block.dominant_position_agreement > 0.7


def test_thin_rows_and_cols_are_set_aside() -> None:
    cells, school_questions, school_voices = _planted_schools(seed=11)
    # a question with exactly one voice, and a voice with exactly one question
    cells[("lonely-question", "s0-v0")] = "lonely-question--only-stance"
    cells[("s0-q0", "lonely-voice")] = "s0-q0--house"

    result = cocluster(cells)

    assert "lonely-question" in result.thin_rows
    assert "lonely-voice" in result.thin_cols
    assert not any("lonely-question" in g for g in result.row_groups)
    assert not any("lonely-voice" in g for g in result.col_groups)
    # thin ids are never silently dropped -- they land at the tail of the order
    assert result.row_order[-len(result.thin_rows):] == sorted(result.thin_rows)
    assert result.col_order[-len(result.thin_cols):] == sorted(result.thin_cols)


def test_deterministic_across_two_runs() -> None:
    cells, _, _ = _planted_schools(seed=99)
    first = cocluster(cells)
    second = cocluster(cells)

    assert first.row_order == second.row_order
    assert first.col_order == second.col_order
    assert [tuple(g) for g in first.row_groups] == [tuple(g) for g in second.row_groups]
    assert [tuple(g) for g in first.col_groups] == [tuple(g) for g in second.col_groups]
    assert [
        (b.fill_ratio, b.dominant_position_agreement) for b in first.blocks
    ] == [(b.fill_ratio, b.dominant_position_agreement) for b in second.blocks]


def _rust_map_cells() -> dict[tuple[str, str], str]:
    map_dir = ROOT / "maps" / "rust"
    positions = _load_kind(map_dir, "positions")
    claims = _load_kind(map_dir, "claims")
    voices = _load_kind(map_dir, "voices")
    questions = _load_kind(map_dir, "questions")

    groups: dict[tuple[str, str], list[str]] = {}
    for cid, c in claims.items():
        pid = c.get("position")
        pos = positions.get(pid)
        if pos is None or pid == "unresolved":
            continue
        vid = c.get("voice")
        if vid not in voices:
            continue
        qid = pos.get("question")
        if qid not in questions:
            continue
        groups.setdefault((qid, vid), []).append(cid)

    cells: dict[tuple[str, str], str] = {}
    for (qid, vid), cids in groups.items():
        dated = [c for c in cids if claims[c].get("date")]
        chosen = sorted(dated, key=lambda c: (claims[c]["date"], c))[-1] if dated else sorted(cids)[0]
        cells[(qid, vid)] = claims[chosen]["position"]
    return cells


def test_live_rust_map_co_clustering_runs_and_reports() -> None:
    cells = _rust_map_cells()
    result = cocluster(cells)

    assert result.k >= 1
    total_row_members = sum(len(g) for g in result.row_groups)
    total_col_members = sum(len(g) for g in result.col_groups)
    assert total_row_members + len(result.thin_rows) == len({q for q, _ in cells})
    assert total_col_members + len(result.thin_cols) == len({v for _, v in cells})

    print(f"\nlive maps/rust: k={result.k}, thin_rows={len(result.thin_rows)}, thin_cols={len(result.thin_cols)}")
    for i, block in enumerate(result.blocks):
        print(
            f"  block {i}: rows={len(block.row_group)} cols={len(block.col_group)} "
            f"fill={block.fill_ratio:.2f} agreement={block.dominant_position_agreement:.2f} "
            f"cells_present={block.cells_present}"
        )
