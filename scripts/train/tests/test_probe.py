"""Tests for probe.py: several problem crates per probe, graded one at a time with `cargo test
--no-fail-fast`, held-out tests copied in from `key/` at grading time and removed after — `key/`
itself never opened or printed for display.

Run: `uv run pytest scripts/train/tests/test_probe.py`. Needs `cargo` on PATH.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import probe  # noqa: E402
import record_schema  # noqa: E402

CARGO_MISSING = shutil.which("cargo") is None

LIB_RS_PASSING = "pub fn double(n: i32) -> i32 {\n    n * 2\n}\n"
# passes the visible case (n=2) by hard-coding it, fails the held-out one (n=5) — a fake that only
# a held-out test, not the locked visible one, can catch
LIB_RS_PARTIAL = "pub fn double(n: i32) -> i32 {\n    if n == 2 { 4 } else { n }\n}\n"
VISIBLE_RS = "use crate_under_test::double;\n\n#[test]\nfn visible_case() {\n    assert_eq!(double(2), 4);\n}\n"
HELDOUT_RS = "use crate_under_test::double;\n\n#[test]\nfn heldout_case() {\n    assert_eq!(double(5), 10);\n}\n"
CARGO_TOML = '[package]\nname = "crate_under_test"\nversion = "0.1.0"\nedition = "2021"\n\n[workspace]\n'


@pytest.fixture(autouse=True)
def isolated_record_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    record_dir = tmp_path / "record"
    record_dir.mkdir()
    (record_dir / "items.csv").write_text(",".join(record_schema.FILES["items"]) + "\n", encoding="utf-8")
    monkeypatch.setattr(record_schema, "RECORD_DIR", record_dir)
    monkeypatch.setattr(probe, "WORK_ROOT", tmp_path / "work")


def make_problem_crate(root: Path, lib_rs: str = LIB_RS_PASSING) -> Path:
    (root / "src").mkdir(parents=True)
    (root / "tests").mkdir(parents=True)
    (root / "Cargo.toml").write_text(CARGO_TOML, encoding="utf-8")
    (root / "src" / "lib.rs").write_text(lib_rs, encoding="utf-8")
    (root / "tests" / "visible.rs").write_text(VISIBLE_RS, encoding="utf-8")
    return root


def make_key_problem(root: Path) -> Path:
    """A mirror of the learner's problem, plus the held-out test — never a spec.md, never presented."""
    make_problem_crate(root, LIB_RS_PASSING)
    (root / "tests" / "heldout.rs").write_text(HELDOUT_RS, encoding="utf-8")
    return root


def make_unit_dir(root: Path, unit: str, which_dirs: tuple[str, ...] = ("probe-a", "probe-b")) -> Path:
    unit_dir = root / unit
    for which_dir in which_dirs:
        for problem in ("p1", "p2"):
            problem_dir = unit_dir / which_dir / problem
            (problem_dir).mkdir(parents=True)
            make_problem_crate(problem_dir)
            (problem_dir / "spec.md").write_text(f"# {which_dir} {problem}\n\nEdit: src/lib.rs\n", encoding="utf-8")
            make_key_problem(unit_dir / "key" / which_dir / problem)
    return unit_dir


def test_assert_no_key_refuses_any_key_path() -> None:
    with pytest.raises(SystemExit, match="never opens or prints a 'key/' path"):
        probe.assert_no_key(Path("units/unit-1/probe-a/p1/key/heldout.rs"))


def test_item_text_excludes_key(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    text = probe.item_text(unit_dir / "probe-a" / "p1")
    assert "Edit: src/lib.rs" in text
    assert "heldout_case" not in text
    assert "key" not in text


def test_item_text_skips_a_build_directory_without_choking_on_binary_files(tmp_path: Path) -> None:
    """A real grading run's `cargo test` leaves `target/` inside the item's own directory (each item
    is its own `[workspace]`); re-presenting the item afterward must not crash reading it as text."""
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    problem_dir = unit_dir / "probe-a" / "p1"
    build_dir = problem_dir / "target" / "debug"
    build_dir.mkdir(parents=True)
    (build_dir / "some_binary").write_bytes(b"\xff\xfe\x00\x01not utf-8")

    text = probe.item_text(problem_dir)

    assert "Edit: src/lib.rs" in text
    assert "target" not in text


def test_probe_dir_refuses_a_key_target(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    monkeypatch.setitem(probe.ISOMORPH_OF, "immediate", "probe-a/key")
    with pytest.raises(SystemExit, match="never opens or prints a 'key/' path"):
        probe.probe_dir(unit_dir, "immediate")


def test_list_problem_dirs_finds_every_crate_sorted(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    problems = probe.list_problem_dirs(unit_dir / "probe-a")
    assert [p.name for p in problems] == ["p1", "p2"]


def test_list_problem_dirs_refuses_an_empty_directory(tmp_path: Path) -> None:
    empty = tmp_path / "probe-a"
    empty.mkdir()
    with pytest.raises(SystemExit, match="no problem crates"):
        probe.list_problem_dirs(empty)


def test_heldout_test_files_excludes_what_the_learner_already_has(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    problem_dir = unit_dir / "probe-a" / "p1"
    key_dir = unit_dir / "key" / "probe-a" / "p1"
    found = probe.heldout_test_files(key_dir, problem_dir)
    assert [f.name for f in found] == ["heldout.rs"]


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_grade_item_copies_heldout_runs_and_cleans_up(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    problem_dir = unit_dir / "probe-a" / "p1"
    key_dir = unit_dir / "key" / "probe-a" / "p1"

    passed, continuous = probe.grade_item(problem_dir, key_dir)

    assert passed is True
    assert continuous == pytest.approx(1.0)
    assert not (problem_dir / "tests" / "heldout.rs").exists()  # removed after grading
    assert (problem_dir / "tests" / "visible.rs").exists()  # the learner's own file, untouched


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_grade_item_fails_a_wrong_implementation_and_still_cleans_up(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    problem_dir = unit_dir / "probe-a" / "p2"
    (problem_dir / "src" / "lib.rs").write_text(LIB_RS_PARTIAL, encoding="utf-8")
    key_dir = unit_dir / "key" / "probe-a" / "p2"

    passed, continuous = probe.grade_item(problem_dir, key_dir)

    assert passed is False
    assert continuous == pytest.approx(0.5)  # visible passes, heldout fails
    assert not (problem_dir / "tests" / "heldout.rs").exists()


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_grade_item_grades_a_build_failure_as_a_full_miss_and_still_cleans_up(tmp_path: Path) -> None:
    """A stub that doesn't compile is the ordinary "fix the compile error" starting state (P3
    items), not a broken setup — it grades as a fail, it doesn't abort the probe."""
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    problem_dir = unit_dir / "probe-a" / "p1"
    (problem_dir / "src" / "lib.rs").write_text("this does not compile(", encoding="utf-8")
    key_dir = unit_dir / "key" / "probe-a" / "p1"

    passed, continuous = probe.grade_item(problem_dir, key_dir)

    assert passed is False
    assert continuous == pytest.approx(0.0)
    assert not (problem_dir / "tests" / "heldout.rs").exists()  # cleaned up all the same


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_probe_logs_every_item_even_when_one_fails_to_compile(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    (unit_dir / "probe-a" / "p1" / "src" / "lib.rs").write_text("this does not compile(", encoding="utf-8")

    rows = probe.run_probe(unit_dir, "immediate", "sess-1", wait=lambda: None, clock=lambda: 0.0)

    assert len(rows) == 2  # p1's compile failure didn't abort grading p2
    by_item = {row["item_id"]: row for row in rows}
    assert by_item["unit-1-probe-a-p1"]["pass"] == "false"
    assert by_item["unit-1-probe-a-p1"]["continuous"] == "0.0000"
    assert by_item["unit-1-probe-a-p2"]["pass"] == "true"


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_probe_grades_every_item_and_logs_one_row_each(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    (unit_dir / "probe-a" / "p2" / "src" / "lib.rs").write_text(LIB_RS_PARTIAL, encoding="utf-8")

    clock_values = iter([0.0, 42.0])
    rows = probe.run_probe(unit_dir, "immediate", "sess-1", wait=lambda: None, clock=lambda: next(clock_values))

    assert len(rows) == 2
    by_item = {row["item_id"]: row for row in rows}
    assert by_item["unit-1-probe-a-p1"]["pass"] == "true"
    assert by_item["unit-1-probe-a-p2"]["pass"] == "false"
    for row in rows:
        assert row["kind"] == "probe-immediate"
        assert row["delay_days"] == "0.0"
        assert float(row["minutes"]) == pytest.approx(42.0 / 60, abs=0.01)

    items_csv = (record_schema.RECORD_DIR / "items.csv").read_text(encoding="utf-8")
    assert "unit-1-probe-a-p1" in items_csv
    assert "unit-1-probe-a-p2" in items_csv


def snapshot(root: Path) -> dict[str, bytes]:
    return {str(path.relative_to(root)): path.read_bytes() for path in sorted(root.rglob("*")) if path.is_file()}


def test_stage_item_copies_to_work_root_leaving_the_source_untouched(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    source = unit_dir / "probe-a" / "p1"
    before = snapshot(source)

    work_dir = probe.stage_item(source, "sess-1", "unit-1", kind="probe")

    assert work_dir == probe.WORK_ROOT / "sess-1" / "unit-1" / "probe" / "p1"
    assert snapshot(work_dir) == before
    assert snapshot(source) == before  # copying never touches the source


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_probe_leaves_items_byte_identical(tmp_path: Path) -> None:
    """The learner edits the staged copy, never `items/` itself (team lead ruling, 2026-09-28)."""
    items_root = tmp_path / "items"
    unit_dir = make_unit_dir(items_root, "unit-1")
    before = snapshot(items_root)

    def learner_edits_the_staged_copy() -> None:
        staged = probe.WORK_ROOT / "sess-1" / "unit-1" / "probe" / "p1" / "src" / "lib.rs"
        assert staged.read_text(encoding="utf-8") == LIB_RS_PASSING  # the copy started from the stub
        staged.write_text(LIB_RS_PARTIAL, encoding="utf-8")  # a real edit, distinct from the original

    probe.run_probe(unit_dir, "immediate", "sess-1", wait=learner_edits_the_staged_copy, clock=lambda: 0.0)

    assert snapshot(items_root) == before


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_probe_warns_over_cap(tmp_path: Path, capsys: pytest.CaptureFixture) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    clock_values = iter([0.0, 900.0])
    probe.run_probe(unit_dir, "immediate", "sess-1", cap_minutes=10.0, wait=lambda: None, clock=lambda: next(clock_values))
    assert "over the 10-minute cap" in capsys.readouterr().out


def test_run_cargo_test_uses_no_fail_fast(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    crate_dir = make_problem_crate(tmp_path / "crate")
    captured: dict = {}

    def fake_run(cmd, **kwargs):
        captured["cmd"] = cmd
        return subprocess.CompletedProcess(cmd, 0, stdout="test result: ok. 1 passed; 0 failed\n", stderr="")

    monkeypatch.setattr(probe.subprocess, "run", fake_run)
    probe.run_cargo_test(crate_dir)
    assert "--no-fail-fast" in captured["cmd"]
