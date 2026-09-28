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



def test_replace_draws_from_the_same_cell_and_class_and_logs(tmp_path: Path) -> None:
    import csv
    header = "id,url,title,author,date,language,class,domain_hints\n"
    lines = [f"b{i},u,t,x,d,en,books-courses,ml\n" for i in range(4)] + [f"t{i},u,t,x,d,en,talks,ml\n" for i in range(4)] \
        + ["c0,u,t,x,d,en,books-courses,core\n"]
    frame_path = tmp_path / "frame.csv"
    frame_path.write_text(header + "".join(lines), encoding="utf-8")
    (tmp_path / "cells.csv").write_text("language,hint,per_team\nen,ml,4\n", encoding="utf-8")
    run = [sys.executable, str(GYM / "scripts/map/sample.py"), "--frame", str(frame_path), "--out", str(tmp_path), "--batch", "1"]
    subprocess.run(run + ["--cells", str(tmp_path / "cells.csv"), "--by-class", "--seed", "5"], check=True, capture_output=True)
    drawn = [row["id"] for row in csv.DictReader((tmp_path / "batch-1-team-a.csv").open())]
    books = [row_id for row_id in drawn if row_id.startswith("b")]
    assert len(books) == 2
    (tmp_path / "replace.csv").write_text(f"team,frame_id\na,{books[0]}\na,{books[1]}\n", encoding="utf-8")
    subprocess.run(run + ["--replace", str(tmp_path / "replace.csv"), "--seed", "9"], check=True, capture_output=True)
    after = [row["id"] for row in csv.DictReader((tmp_path / "batch-1-team-a.csv").open())]
    new_books = sorted(set(after) - set(drawn))
    assert len(after) == 4 and not set(books) & set(after)
    assert new_books == sorted({"b0", "b1", "b2", "b3"} - set(books))
    log = list(csv.DictReader((tmp_path / "batch-1-team-a-replaced.csv").open()))
    assert [row["seed"] for row in log] == ["9", "9"] and {row["class"] for row in log} == {"books-courses"}
    assert subprocess.run(run + ["--replace", str(tmp_path / "replace.csv"), "--seed", "9"], capture_output=True).returncode != 0
    (tmp_path / "replace.csv").write_text(f"team,frame_id\na,{new_books[0]}\n", encoding="utf-8")
    subprocess.run(run + ["--replace", str(tmp_path / "replace.csv"), "--seed", "10"], check=True, capture_output=True)
    log = list(csv.DictReader((tmp_path / "batch-1-team-a-replaced.csv").open()))
    assert log[-1]["replacement_id"] == "" and log[-1]["pool"] == "0"


def test_replace_other_class_draws_from_the_rest_of_the_cell() -> None:
    from sample import replace_rows
    frame_rows = frame([("t1", "talks", "ml"), ("t2", "talks", "ml"), ("f1", "forum", "ml"), ("f2", "forum", "ml"),
                        ("x1", "forum", "web")])
    current = [frame_rows[0]]
    updated, log = replace_rows(frame_rows, current, {"t1": ("en", "ml")}, ["t1"], set(), random.Random(2), other_class=True)
    assert [row["id"] for row in updated][0] in {"f1", "f2"} and log[0]["pool"] == 2
