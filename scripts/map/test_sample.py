"""Tests for the wide-pass sampler: batch 1 re-draws from its logged seed; the by-class draw keeps its quotas.

Run: `uv run --with pytest pytest scripts/map/test_sample.py`.
"""

from __future__ import annotations

import random
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prepare_frame import prepare  # noqa: E402
from sample import draw_for_team, sampling_class, strata_of  # noqa: E402

GYM = Path(__file__).resolve().parents[2]
RECON = GYM / "docs/orchestration_log/recon/2026-09-27/research/rust-map"
SAMPLES = RECON / "samples"
BATCH_1_SEED = 1786744536  # samples/batch-1.md line 5


def test_prepare_reproduces_batch_1_input(tmp_path: Path) -> None:
    out = tmp_path / "frame-b1-input.csv"
    subprocess.run([sys.executable, str(GYM / "scripts/map/prepare_frame.py"), "--frame", str(RECON / "frame/frame.csv"),
                    "--out", str(out)], check=True, capture_output=True)
    assert out.read_bytes() == (SAMPLES / "frame-b1-input.csv").read_bytes()


def test_batch_1_redraws_from_logged_seed(tmp_path: Path) -> None:
    subprocess.run([sys.executable, str(GYM / "scripts/map/sample.py"), "--frame", str(SAMPLES / "frame-b1-input.csv"),
                    "--out", str(tmp_path), "--batch", "1", "--per-team", "18", "--seed", str(BATCH_1_SEED)],
                   check=True, capture_output=True)
    for team in "ab":
        assert (tmp_path / f"batch-1-team-{team}.csv").read_bytes() == (SAMPLES / f"batch-1-team-{team}.csv").read_bytes()


def frame(rows: list[tuple[str, str, str]]) -> list[dict]:
    return [{"id": row_id, "url": row_id, "title": "", "author": "", "date": "", "language": "en",
             "class": row_class, "domain_hints": hints} for row_id, row_class, hints in rows]


def test_by_class_splits_quota_evenly_and_passes_shortfall_on() -> None:
    rows = frame([(f"big{i:03d}", "domain-subframes", "core") for i in range(100)]
                 + [(f"tlk{i:03d}", "talks;twir-links", "core") for i in range(100)]
                 + [(f"bk{i}", "books-courses", "core") for i in range(2)])
    drawn = draw_for_team(strata_of(rows), set(), 18, random.Random(1), by_class=True)
    counts = Counter(sampling_class(row) for row in drawn)
    assert len(drawn) == 18
    assert counts["books-courses"] == 2
    assert {counts["domain-subframes"], counts["talks"]} == {8}


def test_by_class_fills_every_cell_without_reusing_rows() -> None:
    rows = frame([(f"r{i:02d}", "talks", "core;ml") for i in range(30)])
    drawn = draw_for_team(strata_of(rows), {"r00", "r01"}, 12, random.Random(7), by_class=True)
    ids = [row["id"] for row in drawn]
    assert len(ids) == 24 == len(set(ids))
    assert not {"r00", "r01"} & set(ids)


def test_by_class_takes_every_row_of_a_short_cell() -> None:
    rows = frame([("a1", "blogs", "core"), ("a2", "books", "core"), ("a3", "books", "core")])
    drawn = draw_for_team(strata_of(rows), set(), 20, random.Random(3), by_class=True)
    assert sorted(row["id"] for row in drawn) == ["a1", "a2", "a3"]


def test_prepare_drops_listed_rows_and_older_window() -> None:
    base = {"url": "", "title": "", "author_handle": "", "date": "", "language": "en", "class": "talks",
            "transcript_available": "no"}
    rows = [{**base, "frame_id": "f1", "domain_hints": "", "window": "in"},
            {**base, "frame_id": "f2", "domain_hints": "swift-interop", "window": "in"},
            {**base, "frame_id": "f3", "domain_hints": "web", "window": "older"},
            {**base, "frame_id": "f4", "domain_hints": "other", "window": "in"},
            {**base, "frame_id": "f5", "domain_hints": "other;governance", "window": "in"}]
    out = prepare(rows, {"f2"})
    assert [(row["id"], row["domain_hints"]) for row in out] == [("f1", "core"), ("f5", "core")]

