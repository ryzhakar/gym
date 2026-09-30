"""Tests for gym.train.baseline: `gym train baseline stage`/`grade`, paralleling `probe
stage`/`grade` for the six items under `<subject_dir>/items/baseline/` — `spec.md` + `stub/` +
`key/`, no `probe-a`/`probe-b` sides (`training/rust/items/README.md` §Layout;
`recon/2026-09-30/train/baseline-procedure.md` confirms `probe.py` itself refuses this shape).

Run: `uv run pytest tests/train/test_baseline.py`. Needs `cargo` on PATH for the grading tests.
"""
from __future__ import annotations

import os
import shutil
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from gym.train import baseline
from gym.train.events import read_events

CARGO_MISSING = shutil.which("cargo") is None

CARGO_TOML = '[package]\nname = "crate_under_test"\nversion = "0.1.0"\nedition = "2021"\n\n[workspace]\n'
LIB_RS_BROKEN = "pub fn keep_long(words: Vec<String>, min: usize) -> (usize, Vec<String>) {\n    todo!()\n}\n"
LIB_RS_PASSING = (
    "pub fn keep_long(words: Vec<String>, min: usize) -> (usize, Vec<String>) {\n"
    "    let total = words.len();\n"
    "    let kept = words.into_iter().filter(|w| w.len() > min).collect();\n"
    "    (total, kept)\n"
    "}\n"
)
VISIBLE_RS = (
    "use crate_under_test::keep_long;\n\n#[test]\nfn visible_case() {\n"
    "    let (total, kept) = keep_long(vec![\"a\".into(), \"bbbb\".into()], 2);\n"
    "    assert_eq!(total, 2);\n"
    "    assert_eq!(kept, vec![\"bbbb\".to_string()]);\n"
    "}\n"
)
HELDOUT_RS = (
    "use crate_under_test::keep_long;\n\n#[test]\nfn heldout_case() {\n"
    "    let (total, kept) = keep_long(vec![\"x\".into()], 0);\n"
    "    assert_eq!(total, 1);\n"
    "    assert_eq!(kept, vec![\"x\".to_string()]);\n"
    "}\n"
)


def make_crate(root: Path, lib_rs: str, visible_rs: str = VISIBLE_RS) -> None:
    (root / "src").mkdir(parents=True)
    (root / "tests").mkdir(parents=True)
    (root / "Cargo.toml").write_text(CARGO_TOML, encoding="utf-8")
    (root / "src" / "lib.rs").write_text(lib_rs, encoding="utf-8")
    (root / "tests" / "visible.rs").write_text(visible_rs, encoding="utf-8")


def make_baseline_item(subject_dir: Path, item: str) -> Path:
    """`<subject_dir>/items/baseline/<item>/` with `spec.md`, a broken `stub/`, and a passing
    `key/` carrying the extra held-out test — the real bank's own shape for `b1-own`."""
    one_item_dir = subject_dir / "items" / "baseline" / item
    (one_item_dir).mkdir(parents=True)
    (one_item_dir / "spec.md").write_text(f"# {item}\n\nEdit: src/lib.rs\n", encoding="utf-8")
    make_crate(one_item_dir / "stub", LIB_RS_BROKEN)
    make_crate(one_item_dir / "key", LIB_RS_PASSING)
    (one_item_dir / "key" / "tests" / "heldout.rs").write_text(HELDOUT_RS, encoding="utf-8")
    return one_item_dir


@pytest.fixture
def subject_dir(tmp_path: Path) -> Path:
    directory = tmp_path / "rust"
    (directory / "sessions" / "sess-1").mkdir(parents=True)
    (directory / "sessions" / "sess-1" / "events.md").touch()
    return directory


def test_all_baseline_items_sorted(subject_dir: Path) -> None:
    for item in ("b3-result", "b1-own", "b2-life"):
        make_baseline_item(subject_dir, item)
    assert baseline.all_baseline_items(subject_dir) == ["b1-own", "b2-life", "b3-result"]


def test_all_baseline_items_refuses_an_empty_bank(subject_dir: Path) -> None:
    (subject_dir / "items" / "baseline").mkdir(parents=True)
    with pytest.raises(SystemExit, match="no baseline items"):
        baseline.all_baseline_items(subject_dir)


def test_item_dir_refuses_an_unknown_item(subject_dir: Path) -> None:
    with pytest.raises(SystemExit, match="no such baseline item"):
        baseline.item_dir(subject_dir, "b9-nope")


def test_run_stage_copies_stub_leaving_the_bank_untouched_and_logs_present(subject_dir: Path) -> None:
    make_baseline_item(subject_dir, "b1-own")

    result = baseline.run_stage(subject_dir, "b1-own", "sess-1")

    assert result["work_dir"] == subject_dir / "work" / "sess-1" / "baseline" / "b1-own"
    assert (result["work_dir"] / "src" / "lib.rs").read_text(encoding="utf-8") == LIB_RS_BROKEN
    assert (subject_dir / "items" / "baseline" / "b1-own" / "stub" / "src" / "lib.rs").read_text(
        encoding="utf-8"
    ) == LIB_RS_BROKEN

    logged = read_events(subject_dir / "sessions" / "sess-1" / "events.md")
    presents = [row for row in logged if row["event_kind"] == "present"]
    assert len(presents) == 1
    assert presents[0]["unit"] == "baseline" and presents[0]["item"] == "b1-own"


def test_run_stage_prints_the_staged_path(subject_dir: Path, capsys: pytest.CaptureFixture) -> None:
    make_baseline_item(subject_dir, "b1-own")
    baseline.run_stage(subject_dir, "b1-own", "sess-1")
    out = capsys.readouterr().out
    assert str(subject_dir / "work" / "sess-1" / "baseline" / "b1-own") in out


def test_run_stage_all_stages_every_item_in_order(subject_dir: Path) -> None:
    for item in ("b2-life", "b1-own"):
        make_baseline_item(subject_dir, item)

    results = baseline.run_stage_all(subject_dir, "sess-1")

    assert [r["work_dir"].name for r in results] == ["b1-own", "b2-life"]
    logged = read_events(subject_dir / "sessions" / "sess-1" / "events.md")
    presents = [row for row in logged if row["event_kind"] == "present"]
    assert [row["item"] for row in presents] == ["b1-own", "b2-life"]


def test_run_grade_refuses_without_a_matching_present_event(subject_dir: Path) -> None:
    make_baseline_item(subject_dir, "b1-own")
    with pytest.raises(SystemExit, match="no present event"):
        baseline.run_grade(subject_dir, "b1-own", "sess-1")


def test_run_grade_refuses_when_nothing_was_staged(subject_dir: Path) -> None:
    make_baseline_item(subject_dir, "b1-own")
    baseline.append_event(subject_dir, "sess-1", "tool:probe", "present", {"unit": "baseline", "item": "b1-own"})
    with pytest.raises(SystemExit, match="nothing staged"):
        baseline.run_grade(subject_dir, "b1-own", "sess-1")


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_grade_fails_the_unmodified_stub(subject_dir: Path) -> None:
    make_baseline_item(subject_dir, "b1-own")
    baseline.run_stage(subject_dir, "b1-own", "sess-1")

    row = baseline.run_grade(subject_dir, "b1-own", "sess-1")

    assert row["result"] == "fail"
    assert row["which"] == "baseline"
    assert row["unit"] == "baseline"
    assert row["problem"] == "b1-own"
    logged = read_events(subject_dir / "sessions" / "sess-1" / "events.md")
    probe_items = [r for r in logged if r["event_kind"] == "probe-item"]
    assert len(probe_items) == 1
    assert probe_items[0]["which"] == "baseline"


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_grade_passes_a_pasted_solution(subject_dir: Path) -> None:
    make_baseline_item(subject_dir, "b1-own")
    result = baseline.run_stage(subject_dir, "b1-own", "sess-1")
    (result["work_dir"] / "src" / "lib.rs").write_text(LIB_RS_PASSING, encoding="utf-8")

    row = baseline.run_grade(subject_dir, "b1-own", "sess-1")

    assert row["result"] == "pass"
    assert row["fraction"] == "1.0000"


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_grade_leaves_no_heldout_file_behind_and_never_prints_key(
    subject_dir: Path, capsys: pytest.CaptureFixture
) -> None:
    make_baseline_item(subject_dir, "b1-own")
    result = baseline.run_stage(subject_dir, "b1-own", "sess-1")
    (result["work_dir"] / "src" / "lib.rs").write_text(LIB_RS_PASSING, encoding="utf-8")
    capsys.readouterr()  # drop stage's own output

    baseline.run_grade(subject_dir, "b1-own", "sess-1")

    assert not (result["work_dir"] / "tests" / "heldout.rs").exists()
    assert (result["work_dir"] / "tests" / "visible.rs").exists()
    out = capsys.readouterr().out
    assert "key" not in out
    assert str(subject_dir / "items" / "baseline" / "b1-own" / "key") not in out


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_stage_and_grade_are_cwd_independent(subject_dir: Path, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Finding 4: the by-hand copy loop silently used the wrong tree when the caller's shell
    wasn't at the repo root. `subject_dir` is absolute here (as the CLI layer resolves it before
    calling in), so staging and grading must work the same regardless of the process cwd."""
    make_baseline_item(subject_dir, "b1-own")
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    monkeypatch.chdir(elsewhere)

    result = baseline.run_stage(subject_dir.resolve(), "b1-own", "sess-1")
    (result["work_dir"] / "src" / "lib.rs").write_text(LIB_RS_PASSING, encoding="utf-8")
    row = baseline.run_grade(subject_dir.resolve(), "b1-own", "sess-1")

    assert row["result"] == "pass"


def test_latest_save_mtime_excludes_target_and_tests(subject_dir: Path) -> None:
    make_baseline_item(subject_dir, "b1-own")
    result = baseline.run_stage(subject_dir, "b1-own", "sess-1")
    work_dir = result["work_dir"]

    old = datetime(2026, 9, 30, 10, 0).timestamp()
    for path in work_dir.rglob("*"):
        if path.is_file():
            os.utime(path, (old, old))

    target_file = work_dir / "target" / "debug" / "fake"
    target_file.parent.mkdir(parents=True)
    target_file.write_text("build cache", encoding="utf-8")
    newer = datetime(2026, 9, 30, 12, 0).timestamp()
    os.utime(target_file, (newer, newer))

    assert baseline.latest_save_mtime(work_dir) == pytest.approx(old)


def test_run_grade_minutes_reflects_the_edit_not_a_cargo_run(subject_dir: Path) -> None:
    """A `cargo test`/`check` run the item bank's own tooling rules allow touches `target/`, which
    must not itself read as a fresh "save"."""
    make_baseline_item(subject_dir, "b1-own")
    result = baseline.run_stage(subject_dir, "b1-own", "sess-1")
    start_row = baseline.latest_present(subject_dir, "sess-1", "b1-own")
    started = datetime.strptime(start_row["timestamp"], "%Y-%m-%dT%H:%M")

    edited = started + timedelta(minutes=2)
    os.utime(result["work_dir"] / "src" / "lib.rs", (edited.timestamp(), edited.timestamp()))
    later_build = started + timedelta(minutes=9)
    build_file = result["work_dir"] / "target" / "debug" / "fake"
    build_file.parent.mkdir(parents=True)
    build_file.write_text("cache", encoding="utf-8")
    os.utime(build_file, (later_build.timestamp(), later_build.timestamp()))

    minutes = baseline.minutes_since(started, baseline.latest_save_mtime(result["work_dir"]))
    assert minutes == pytest.approx(2.0, abs=0.02)
