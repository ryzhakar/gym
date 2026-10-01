"""Tests for gym.train.probe, ported from scripts/train/tests/test_probe.py onto the events layout:
several problem crates per probe, graded one at a time with `cargo test --no-fail-fast`, held-out
tests copied in from `key/` at grading time and removed after — `key/` itself never opened or
printed for display. The write target is a `probe-item` event, not an `items` CSV row.
`stage`/`grade` (team lead ruling, 2026-09-30) replace a single interactive command that waited on
stdin between presenting the items and grading them.

Run: `uv run pytest tests/train/test_probe.py`. Needs `cargo` on PATH for the grading tests.
"""
from __future__ import annotations

import os
import shutil
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from gym.train import probe
from gym.train.events import read_events
from gym.train.schema import TIMESTAMP_FORMAT

CARGO_MISSING = shutil.which("cargo") is None

LIB_RS_PASSING = "pub fn double(n: i32) -> i32 {\n    n * 2\n}\n"
# passes the visible case (n=2) by hard-coding it, fails the held-out one (n=5)
LIB_RS_PARTIAL = "pub fn double(n: i32) -> i32 {\n    if n == 2 { 4 } else { n }\n}\n"
VISIBLE_RS = "use crate_under_test::double;\n\n#[test]\nfn visible_case() {\n    assert_eq!(double(2), 4);\n}\n"
HELDOUT_RS = "use crate_under_test::double;\n\n#[test]\nfn heldout_case() {\n    assert_eq!(double(5), 10);\n}\n"
CARGO_TOML = '[package]\nname = "crate_under_test"\nversion = "0.1.0"\nedition = "2021"\n\n[workspace]\n'


@pytest.fixture
def subject_dir(tmp_path: Path) -> Path:
    directory = tmp_path / "rust"
    (directory / "sessions" / "sess-1").mkdir(parents=True)
    (directory / "sessions" / "sess-1" / "events.md").touch()
    return directory


def make_problem_crate(root: Path, lib_rs: str = LIB_RS_PASSING) -> Path:
    (root / "src").mkdir(parents=True)
    (root / "tests").mkdir(parents=True)
    (root / "Cargo.toml").write_text(CARGO_TOML, encoding="utf-8")
    (root / "src" / "lib.rs").write_text(lib_rs, encoding="utf-8")
    (root / "tests" / "visible.rs").write_text(VISIBLE_RS, encoding="utf-8")
    return root


def make_key_problem(root: Path) -> Path:
    make_problem_crate(root, LIB_RS_PASSING)
    (root / "tests" / "heldout.rs").write_text(HELDOUT_RS, encoding="utf-8")
    return root


def make_unit_dir(root: Path, unit: str, which_dirs: tuple[str, ...] = ("probe-a", "probe-b")) -> Path:
    unit_dir = root / unit
    for which_dir in which_dirs:
        for problem in ("p1", "p2"):
            problem_dir = unit_dir / which_dir / problem
            problem_dir.mkdir(parents=True)
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


def test_resolve_side_maps_immediate_and_delayed_to_probe_a_and_probe_b() -> None:
    assert probe.resolve_side("immediate") == "probe-a"
    assert probe.resolve_side("delayed") == "probe-b"


def test_resolve_side_passes_a_literal_probe_side_name_through() -> None:
    assert probe.resolve_side("probe-c") == "probe-c"


def test_resolve_side_refuses_anything_else() -> None:
    with pytest.raises(SystemExit, match="not 'immediate', 'delayed', or a literal"):
        probe.resolve_side("tomorrow")


def test_probe_dir_accepts_a_literal_third_side(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1", which_dirs=("probe-a", "probe-b", "probe-c"))
    assert probe.probe_dir(unit_dir, "probe-c") == unit_dir / "probe-c"


def test_probe_dir_refuses_a_side_with_no_directory_under_the_unit(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")  # only probe-a/probe-b exist
    with pytest.raises(SystemExit, match=r"no such probe directory: .*probe-c"):
        probe.probe_dir(unit_dir, "probe-c")


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


def test_session_path_segment_strips_colons() -> None:
    assert probe.session_path_segment("2026-09-29T12:20") == "2026-09-29T12-20"
    assert ":" not in probe.session_path_segment("2026-09-29T12:20")


def test_stage_item_copies_to_work_root_leaving_the_source_untouched(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    source = unit_dir / "probe-a" / "p1"
    before = source.read_bytes() if source.is_file() else None
    work_root = tmp_path / "work"

    work_dir = probe.stage_item(source, work_root, "sess-1", "unit-1")

    assert work_dir == work_root / "sess-1" / "unit-1" / "p1"
    assert (work_dir / "src" / "lib.rs").read_text(encoding="utf-8") == LIB_RS_PASSING
    assert (source / "src" / "lib.rs").read_text(encoding="utf-8") == LIB_RS_PASSING
    assert before is None  # source is a directory, not a file; sanity check only


def test_run_cargo_test_uses_no_fail_fast(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    crate_dir = make_problem_crate(tmp_path / "crate")
    captured: dict = {}

    def fake_run(cmd, **kwargs):
        captured["cmd"] = cmd
        return subprocess.CompletedProcess(cmd, 0, stdout="test result: ok. 1 passed; 0 failed\n", stderr="")

    monkeypatch.setattr(probe.subprocess, "run", fake_run)
    probe.run_cargo_test(crate_dir)
    assert "--no-fail-fast" in captured["cmd"]


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_grade_item_copies_heldout_runs_and_cleans_up(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    problem_dir = unit_dir / "probe-a" / "p1"
    key_dir = unit_dir / "key" / "probe-a" / "p1"

    passed, continuous = probe.grade_item(problem_dir, key_dir)

    assert passed is True
    assert continuous == pytest.approx(1.0)
    assert not (problem_dir / "tests" / "heldout.rs").exists()
    assert (problem_dir / "tests" / "visible.rs").exists()


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_grade_item_fails_a_wrong_implementation_and_still_cleans_up(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    problem_dir = unit_dir / "probe-a" / "p2"
    (problem_dir / "src" / "lib.rs").write_text(LIB_RS_PARTIAL, encoding="utf-8")
    key_dir = unit_dir / "key" / "probe-a" / "p2"

    passed, continuous = probe.grade_item(problem_dir, key_dir)

    assert passed is False
    assert continuous == pytest.approx(0.5)
    assert not (problem_dir / "tests" / "heldout.rs").exists()


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_grade_item_grades_a_build_failure_as_a_full_miss_and_still_cleans_up(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    problem_dir = unit_dir / "probe-a" / "p1"
    (problem_dir / "src" / "lib.rs").write_text("this does not compile(", encoding="utf-8")
    key_dir = unit_dir / "key" / "probe-a" / "p1"

    passed, continuous = probe.grade_item(problem_dir, key_dir)

    assert passed is False
    assert continuous == pytest.approx(0.0)
    assert not (problem_dir / "tests" / "heldout.rs").exists()


def test_run_stage_logs_a_probe_start_event_and_stages_every_problem(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")

    result = probe.run_stage(subject_dir, unit_dir, "immediate", "sess-1")

    assert result["problem_names"] == ["p1", "p2"]
    assert all(work_dir.is_dir() for work_dir in result["staged"])
    assert "probe-start" in result["line"]

    logged = read_events(subject_dir / "sessions" / "sess-1" / "events.md")
    starts = [row for row in logged if row["event_kind"] == "probe-start"]
    assert len(starts) == 1
    assert starts[0]["unit"] == "unit-1" and starts[0]["which"] == "probe-a"
    assert starts[0]["problems"] == "p1,p2"


def test_run_stage_stages_a_literal_third_side_and_logs_its_own_literal_name(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1", which_dirs=("probe-a", "probe-b", "probe-c"))

    result = probe.run_stage(subject_dir, unit_dir, "probe-c", "sess-1")

    assert result["problem_names"] == ["p1", "p2"]
    logged = read_events(subject_dir / "sessions" / "sess-1" / "events.md")
    starts = [row for row in logged if row["event_kind"] == "probe-start"]
    assert starts[0]["which"] == "probe-c"


def test_run_stage_prints_the_staged_paths_not_the_item_text(tmp_path: Path, subject_dir: Path, capsys: pytest.CaptureFixture) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    probe.run_stage(subject_dir, unit_dir, "immediate", "sess-1")
    out = capsys.readouterr().out
    assert str(subject_dir / "work" / "sess-1" / "unit-1" / "p1") in out
    assert "Edit: src/lib.rs" not in out  # no item text, per the team lead's spec


def test_latest_probe_start_returns_none_when_nothing_staged(subject_dir: Path) -> None:
    assert probe.latest_probe_start(subject_dir, "sess-1", "unit-1", "immediate") is None


def test_latest_probe_start_returns_the_most_recent_matching_event(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    probe.run_stage(subject_dir, unit_dir, "immediate", "sess-1")
    probe.run_stage(subject_dir, unit_dir, "delayed", "sess-1")  # a different `which`, no match

    row = probe.latest_probe_start(subject_dir, "sess-1", "unit-1", "immediate")

    assert row is not None and row["which"] == "probe-a"


def test_run_grade_refuses_without_a_matching_probe_start_event(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    with pytest.raises(SystemExit, match="no probe-start event"):
        probe.run_grade(subject_dir, unit_dir, "immediate", "sess-1")


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_grade_logs_one_probe_item_event_per_problem_even_on_a_compile_failure(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    (unit_dir / "probe-a" / "p1" / "src" / "lib.rs").write_text("this does not compile(", encoding="utf-8")

    probe.run_stage(subject_dir, unit_dir, "immediate", "sess-1")
    rows = probe.run_grade(subject_dir, unit_dir, "immediate", "sess-1")

    assert len(rows) == 2
    by_problem = {row["problem"]: row for row in rows}
    assert by_problem["p1"]["result"] == "fail"
    assert by_problem["p1"]["fraction"] == "0.0000"
    assert by_problem["p2"]["result"] == "pass"

    logged = read_events(subject_dir / "sessions" / "sess-1" / "events.md")
    probe_events = [row for row in logged if row["event_kind"] == "probe-item"]
    assert len(probe_events) == 2
    assert all(row["unit"] == "unit-1" and row["which"] == "probe-a" for row in probe_events)


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_stage_then_grade_round_trips_on_a_literal_third_side(tmp_path: Path, subject_dir: Path) -> None:
    """A unit's repeat side, `probe-c` (owner ruling, 2026-09-30): stage and grade both take it as
    a literal side name, unrelated to `immediate`/`delayed`, and every event it logs carries
    `which=probe-c`, never an alias."""
    unit_dir = make_unit_dir(tmp_path, "unit-1", which_dirs=("probe-a", "probe-b", "probe-c"))

    probe.run_stage(subject_dir, unit_dir, "probe-c", "sess-1")
    rows = probe.run_grade(subject_dir, unit_dir, "probe-c", "sess-1")

    assert len(rows) == 2
    assert all(row["which"] == "probe-c" for row in rows)
    assert {row["result"] for row in rows} == {"pass"}


def test_run_grade_refuses_a_literal_side_with_no_matching_probe_start(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1", which_dirs=("probe-a", "probe-b", "probe-c"))
    with pytest.raises(SystemExit, match="no probe-start event for unit 'unit-1', which 'probe-c'"):
        probe.run_grade(subject_dir, unit_dir, "probe-c", "sess-1")


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_grade_total_minutes_is_computed_from_the_probe_start_events_own_timestamp(tmp_path: Path, subject_dir: Path) -> None:
    """Team lead ruling (2026-09-30): `total_minutes` is the shared quantity the old, single
    `minutes` field used to be — grade time minus the `probe-start` event's own clock stamp, the
    same on every problem in one `grade` call."""
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    probe.run_stage(subject_dir, unit_dir, "immediate", "sess-1")
    # the probe-start event was just stamped with the real clock; graded "now" is 5 minutes later
    started = probe.latest_probe_start(subject_dir, "sess-1", "unit-1", "immediate")
    real_start = datetime.strptime(started["timestamp"], TIMESTAMP_FORMAT)

    rows = probe.run_grade(subject_dir, unit_dir, "immediate", "sess-1", now=real_start + timedelta(minutes=5))

    assert all(float(row["total_minutes"]) == pytest.approx(5.0, abs=0.02) for row in rows)


def _set_mtime(path: Path, when: datetime) -> None:
    epoch = when.timestamp()
    os.utime(path, (epoch, epoch))


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_grade_minutes_is_0_for_an_untouched_problem(tmp_path: Path, subject_dir: Path) -> None:
    """Team lead ruling (2026-09-30): each event's own `minutes` is now per-problem — the latest
    mtime under that problem's staged `src/` minus the `probe-start` event's time. A problem never
    edited since staging reads `minutes=0`, whatever `total_minutes` (grade time elapsed) says.
    Both problems' `src/` mtimes are pinned explicitly, at-or-before `real_start`, so the test
    doesn't depend on how fast `shutil.copytree` happened to run relative to the minute boundary
    `probe-start`'s own timestamp truncated to (see `minutes_since`'s docstring)."""
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    probe.run_stage(subject_dir, unit_dir, "immediate", "sess-1")
    started = probe.latest_probe_start(subject_dir, "sess-1", "unit-1", "immediate")
    real_start = datetime.strptime(started["timestamp"], TIMESTAMP_FORMAT)
    for problem in ("p1", "p2"):
        _set_mtime(subject_dir / "work" / "sess-1" / "unit-1" / problem / "src" / "lib.rs", real_start)

    rows = probe.run_grade(subject_dir, unit_dir, "immediate", "sess-1", now=real_start + timedelta(minutes=5))

    assert all(row["minutes"] == "0.00" for row in rows)
    assert all(float(row["total_minutes"]) == pytest.approx(5.0, abs=0.02) for row in rows)


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_grade_minutes_reflects_the_edited_problems_own_mtime(tmp_path: Path, subject_dir: Path) -> None:
    """A problem the learner actually edited gets its own `minutes`, from its own `src/` mtime —
    not `total_minutes`'s shared, grade-time-elapsed figure. Both problems' mtimes are pinned
    explicitly (p2 to exactly `real_start`, p1 three minutes after) so the comparison is exact,
    not subject to real `shutil.copytree` timing noise within a minute boundary."""
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    probe.run_stage(subject_dir, unit_dir, "immediate", "sess-1")
    started = probe.latest_probe_start(subject_dir, "sess-1", "unit-1", "immediate")
    real_start = datetime.strptime(started["timestamp"], TIMESTAMP_FORMAT)

    p1_src = subject_dir / "work" / "sess-1" / "unit-1" / "p1" / "src" / "lib.rs"
    p1_src.write_text(LIB_RS_PASSING, encoding="utf-8")
    _set_mtime(p1_src, real_start + timedelta(minutes=3))
    _set_mtime(subject_dir / "work" / "sess-1" / "unit-1" / "p2" / "src" / "lib.rs", real_start)

    rows = probe.run_grade(subject_dir, unit_dir, "immediate", "sess-1", now=real_start + timedelta(minutes=5))
    by_problem = {row["problem"]: row for row in rows}

    assert float(by_problem["p1"]["minutes"]) == pytest.approx(3.0, abs=0.02)
    assert by_problem["p2"]["minutes"] == "0.00"  # p2 was never touched
    assert all(float(row["total_minutes"]) == pytest.approx(5.0, abs=0.02) for row in rows)


def test_latest_mtime_under_returns_none_for_a_missing_directory(tmp_path: Path) -> None:
    assert probe.latest_mtime_under(tmp_path / "nope") is None


def test_latest_mtime_under_returns_none_for_an_empty_directory(tmp_path: Path) -> None:
    empty = tmp_path / "empty"
    empty.mkdir()
    assert probe.latest_mtime_under(empty) is None


def test_minutes_since_floors_at_0_for_no_mtime_or_an_mtime_at_or_before_the_reference() -> None:
    reference = datetime(2026, 9, 30, 22, 0)
    assert probe.minutes_since(reference, None) == 0.0
    assert probe.minutes_since(reference, reference.timestamp()) == 0.0
    assert probe.minutes_since(reference, reference.timestamp() - 60) == 0.0  # a minute earlier: still 0


def test_minutes_since_computes_positive_elapsed_minutes() -> None:
    reference = datetime(2026, 9, 30, 22, 0)
    assert probe.minutes_since(reference, reference.timestamp() + 90) == pytest.approx(1.5, abs=0.001)


def test_run_grade_defaults_cap_minutes_to_10() -> None:
    assert probe.CAP_MINUTES_DEFAULT == 10.0


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_grade_records_over_cap_no_when_under_the_cap(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    probe.run_stage(subject_dir, unit_dir, "immediate", "sess-1")
    started = probe.latest_probe_start(subject_dir, "sess-1", "unit-1", "immediate")
    real_start = datetime.strptime(started["timestamp"], TIMESTAMP_FORMAT)

    rows = probe.run_grade(
        subject_dir, unit_dir, "immediate", "sess-1", cap_minutes=10.0, now=real_start + timedelta(minutes=5)
    )

    assert all(row["over_cap"] == "no" for row in rows)


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_grade_records_over_cap_yes_when_over_the_cap_never_refusing(tmp_path: Path, subject_dir: Path) -> None:
    """The cap is recorded as data, never enforced: grading still runs and logs normally past it."""
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    probe.run_stage(subject_dir, unit_dir, "immediate", "sess-1")
    started = probe.latest_probe_start(subject_dir, "sess-1", "unit-1", "immediate")
    real_start = datetime.strptime(started["timestamp"], TIMESTAMP_FORMAT)

    rows = probe.run_grade(
        subject_dir, unit_dir, "immediate", "sess-1", cap_minutes=10.0, now=real_start + timedelta(minutes=15)
    )

    assert len(rows) == 2
    assert all(row["over_cap"] == "yes" for row in rows)
    assert {row["result"] for row in rows} == {"pass"}  # grading itself is unaffected


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_stage_then_grade_leaves_items_byte_identical(tmp_path: Path, subject_dir: Path) -> None:
    """The learner edits the staged copy, between the two commands, never the items directory
    itself."""
    items_root = tmp_path / "items"
    unit_dir = make_unit_dir(items_root, "unit-1")
    before = (unit_dir / "probe-a" / "p1" / "src" / "lib.rs").read_bytes()

    probe.run_stage(subject_dir, unit_dir, "immediate", "sess-1")
    staged = subject_dir / "work" / "sess-1" / "unit-1" / "p1" / "src" / "lib.rs"
    assert staged.read_text(encoding="utf-8") == LIB_RS_PASSING
    staged.write_text(LIB_RS_PARTIAL, encoding="utf-8")  # the learner's own edit, in the work path

    probe.run_grade(subject_dir, unit_dir, "immediate", "sess-1")

    assert (unit_dir / "probe-a" / "p1" / "src" / "lib.rs").read_bytes() == before


# --- `gym train probe go`: the learner's start mark, from which grade measures minutes ---

CLOCK = datetime(2026, 10, 1, 10, 0)


def _log(subject_dir: Path, kind: str, fields: dict[str, str], when: datetime) -> None:
    from gym.train.events import append_event

    append_event(subject_dir, "sess-1", "tool:probe", kind, fields, now=when)


def _staged_by_hand(
    tmp_path: Path, subject_dir: Path, stage_at: datetime = CLOCK, which: str = "probe-a"
) -> tuple[Path, dict[str, Path]]:
    """A unit staged with an explicit clock: files copied, `probe-start` logged at `stage_at`, every
    source file's mtime pinned at `stage_at`, so each test sets only the saves and marks it means."""
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    work: dict[str, Path] = {}
    for problem in ("p1", "p2"):
        work[problem] = probe.stage_item(unit_dir / which / problem, subject_dir / "work", "sess-1", "unit-1")
        for path in work[problem].rglob("*"):
            if path.is_file():
                _set_mtime(path, stage_at)
    _log(subject_dir, "probe-start", {"unit": "unit-1", "which": which, "problems": "p1,p2"}, stage_at)
    return unit_dir, work


def _save(work_dir: Path, when: datetime) -> None:
    lib = work_dir / "src" / "lib.rs"
    lib.write_text(LIB_RS_PASSING, encoding="utf-8")
    _set_mtime(lib, when)


def test_run_go_logs_a_probe_go_event_for_the_staged_side(tmp_path: Path, subject_dir: Path, capsys: pytest.CaptureFixture) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    probe.run_stage(subject_dir, unit_dir, "immediate", "sess-1")

    result = probe.run_go(subject_dir, unit_dir, "immediate", "sess-1")

    goes = [row for row in read_events(subject_dir / "sessions" / "sess-1" / "events.md") if row["event_kind"] == "probe-go"]
    assert len(goes) == 1
    assert (goes[0]["actor"], goes[0]["unit"], goes[0]["which"]) == ("tool:probe", "unit-1", "probe-a")
    assert capsys.readouterr().out.strip().endswith(result["line"])


def test_run_go_logs_the_literal_side_for_a_literal_third_side(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1", which_dirs=("probe-a", "probe-b", "probe-c"))
    probe.run_stage(subject_dir, unit_dir, "probe-c", "sess-1")

    probe.run_go(subject_dir, unit_dir, "probe-c", "sess-1")

    goes = [row for row in read_events(subject_dir / "sessions" / "sess-1" / "events.md") if row["event_kind"] == "probe-go"]
    assert goes[0]["which"] == "probe-c"


def test_run_go_refuses_without_a_probe_start_for_that_unit_and_side(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    with pytest.raises(SystemExit, match="no probe-start event for unit 'unit-1', which 'probe-a'"):
        probe.run_go(subject_dir, unit_dir, "immediate", "sess-1")
    probe.run_stage(subject_dir, unit_dir, "immediate", "sess-1")
    with pytest.raises(SystemExit, match="no probe-start event for unit 'unit-1', which 'probe-b'"):
        probe.run_go(subject_dir, unit_dir, "delayed", "sess-1")


def test_latest_probe_go_is_none_without_a_go_and_the_latest_with_several(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir, _work = _staged_by_hand(tmp_path, subject_dir)
    assert probe.latest_probe_go(subject_dir, "sess-1", "unit-1", "immediate") is None
    _log(subject_dir, "probe-go", {"unit": "unit-1", "which": "probe-a"}, CLOCK + timedelta(minutes=2))
    _log(subject_dir, "probe-go", {"unit": "unit-1", "which": "probe-a"}, CLOCK + timedelta(minutes=4))
    row = probe.latest_probe_go(subject_dir, "sess-1", "unit-1", "immediate")
    assert row is not None and row["timestamp"] == "2026-10-01T10:04"


def test_latest_probe_go_ignores_another_side_and_a_go_before_the_latest_staging(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir, _work = _staged_by_hand(tmp_path, subject_dir)
    _log(subject_dir, "probe-go", {"unit": "unit-1", "which": "probe-a"}, CLOCK + timedelta(minutes=2))
    _log(subject_dir, "probe-start", {"unit": "unit-1", "which": "probe-b", "problems": "p1,p2"}, CLOCK + timedelta(minutes=3))
    _log(subject_dir, "probe-go", {"unit": "unit-1", "which": "probe-b"}, CLOCK + timedelta(minutes=4))
    assert probe.latest_probe_go(subject_dir, "sess-1", "unit-1", "delayed")["timestamp"] == "2026-10-01T10:04"
    assert probe.latest_probe_go(subject_dir, "sess-1", "unit-1", "immediate")["timestamp"] == "2026-10-01T10:02"
    # staged again after that go: the go marked work the restaging wiped
    _log(subject_dir, "probe-start", {"unit": "unit-1", "which": "probe-a", "problems": "p1,p2"}, CLOCK + timedelta(minutes=6))
    assert probe.latest_probe_go(subject_dir, "sess-1", "unit-1", "immediate") is None


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_grade_measures_minutes_and_total_from_the_go_mark_not_the_stage_time(tmp_path: Path, subject_dir: Path) -> None:
    """Staged 10:00, go 10:02, p1 last saved 10:05, p2 10:04, graded 10:30 with a 10 minute cap:
    from the stage time p1 would read 5.00 and the total 30.00, over the cap; from the go, p1 3.00,
    p2 2.00, total 3.00 (latest last save of the probe minus the go), under the cap."""
    unit_dir, work = _staged_by_hand(tmp_path, subject_dir)
    _log(subject_dir, "probe-go", {"unit": "unit-1", "which": "probe-a"}, CLOCK + timedelta(minutes=2))
    _save(work["p1"], CLOCK + timedelta(minutes=5))
    _save(work["p2"], CLOCK + timedelta(minutes=4))

    rows = probe.run_grade(subject_dir, unit_dir, "immediate", "sess-1", cap_minutes=10.0, now=CLOCK + timedelta(minutes=30))
    by_problem = {row["problem"]: row for row in rows}

    assert by_problem["p1"]["minutes"] == "3.00"
    assert by_problem["p2"]["minutes"] == "2.00"
    assert all(row["total_minutes"] == "3.00" for row in rows)
    assert all(row["over_cap"] == "no" for row in rows)
    assert {row["result"] for row in rows} == {"pass"}


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_grade_without_a_go_still_measures_from_the_stage_time(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir, work = _staged_by_hand(tmp_path, subject_dir)
    _save(work["p1"], CLOCK + timedelta(minutes=5))

    rows = probe.run_grade(subject_dir, unit_dir, "immediate", "sess-1", cap_minutes=10.0, now=CLOCK + timedelta(minutes=30))
    by_problem = {row["problem"]: row for row in rows}

    assert by_problem["p1"]["minutes"] == "5.00"
    assert by_problem["p2"]["minutes"] == "0.00"
    assert all(row["total_minutes"] == "30.00" and row["over_cap"] == "yes" for row in rows)


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_grade_floors_a_save_before_the_go_at_0_and_an_unsaved_probe_totals_0(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir, work = _staged_by_hand(tmp_path, subject_dir)
    _log(subject_dir, "probe-go", {"unit": "unit-1", "which": "probe-a"}, CLOCK + timedelta(minutes=7))
    _save(work["p1"], CLOCK + timedelta(minutes=5))  # saved before the go

    rows = probe.run_grade(subject_dir, unit_dir, "immediate", "sess-1", now=CLOCK + timedelta(minutes=30))

    assert all(row["minutes"] == "0.00" and row["total_minutes"] == "0.00" and row["over_cap"] == "no" for row in rows)


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_grade_uses_the_latest_go(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir, work = _staged_by_hand(tmp_path, subject_dir)
    _log(subject_dir, "probe-go", {"unit": "unit-1", "which": "probe-a"}, CLOCK + timedelta(minutes=1))
    _log(subject_dir, "probe-go", {"unit": "unit-1", "which": "probe-a"}, CLOCK + timedelta(minutes=4))
    _save(work["p1"], CLOCK + timedelta(minutes=6))

    rows = probe.run_grade(subject_dir, unit_dir, "immediate", "sess-1", now=CLOCK + timedelta(minutes=30))

    assert {row["problem"]: row["minutes"] for row in rows}["p1"] == "2.00"
    assert all(row["total_minutes"] == "2.00" for row in rows)


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_grade_ignores_a_go_logged_before_the_probe_was_staged_again(tmp_path: Path, subject_dir: Path) -> None:
    unit_dir, work = _staged_by_hand(tmp_path, subject_dir)
    _log(subject_dir, "probe-go", {"unit": "unit-1", "which": "probe-a"}, CLOCK + timedelta(minutes=2))
    _log(subject_dir, "probe-start", {"unit": "unit-1", "which": "probe-a", "problems": "p1,p2"}, CLOCK + timedelta(minutes=10))
    _save(work["p1"], CLOCK + timedelta(minutes=14))

    rows = probe.run_grade(subject_dir, unit_dir, "immediate", "sess-1", now=CLOCK + timedelta(minutes=30))

    assert {row["problem"]: row["minutes"] for row in rows}["p1"] == "4.00"
    assert all(row["total_minutes"] == "20.00" for row in rows)


def test_cli_probe_go_logs_a_probe_go_event(tmp_path: Path) -> None:
    from typer.testing import CliRunner

    from gym.train.cli import app

    subject = tmp_path / "rust"
    (subject / "sessions" / "sess-1").mkdir(parents=True)
    (subject / "sessions" / "sess-1" / "events.md").touch()
    unit_dir = make_unit_dir(subject / "items", "unit-1")
    runner = CliRunner()

    staged = runner.invoke(app, ["probe", "stage", str(unit_dir), "immediate", "--session", "sess-1"])
    went = runner.invoke(app, ["probe", "go", str(unit_dir), "immediate", "--session", "sess-1"])

    assert staged.exit_code == 0, staged.output
    assert went.exit_code == 0, went.output
    goes = [row for row in read_events(subject / "sessions" / "sess-1" / "events.md") if row["event_kind"] == "probe-go"]
    assert [(row["actor"], row["unit"], row["which"]) for row in goes] == [("tool:probe", "unit-1", "probe-a")]


def test_cli_probe_go_refuses_an_unknown_side(tmp_path: Path) -> None:
    from typer.testing import CliRunner

    from gym.train.cli import app

    result = CliRunner().invoke(app, ["probe", "go", str(tmp_path / "x" / "y" / "unit-1"), "tomorrow", "--session", "s"])
    assert result.exit_code == 2
    assert "Invalid value for which" in result.output
