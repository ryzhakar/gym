"""Tests for gym.train.practice: `gym train practice grade`, grading a practice item's learner
folder against the held-out tests its unit's `key/<item>/tests/` keeps, in a scratch copy.

Layout under test (training/rust/items/README.md): `<subject>/items/<unit>/<item>/` the item's crate,
`<subject>/items/<unit>/key/<item>/tests/` its held-out tests, and
`<subject>/work/<session>/<unit>/<item>/` the learner's folder.

Run: `uv run pytest tests/train/test_practice.py`. Needs `cargo` on PATH.
"""
from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

import pytest
from typer.testing import CliRunner

from gym.train import practice
from gym.train.cli import app
from gym.train.events import read_events

CARGO_MISSING = shutil.which("cargo") is None
pytestmark = pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")

LIB_RS_PASSING = "pub fn double(n: i32) -> i32 {\n    n * 2\n}\n"
# passes the visible case (n=2) by hard-coding it, fails the held-out one (n=5)
LIB_RS_PARTIAL = "pub fn double(n: i32) -> i32 {\n    if n == 2 { 4 } else { n }\n}\n"
LIB_RS_BROKEN = "this does not compile("
VISIBLE_RS = "use crate_under_test::double;\n\n#[test]\nfn visible_case() {\n    assert_eq!(double(2), 4);\n}\n"
HELDOUT_RS = "use crate_under_test::double;\n\n#[test]\nfn heldout_secret_case() {\n    assert_eq!(double(5), 10);\n}\n"
CARGO_TOML = '[package]\nname = "crate_under_test"\nversion = "0.1.0"\nedition = "2021"\n\n[workspace]\n'

SESSION = "sess-1"
UNIT = "u-enums"


@pytest.fixture
def subject_dir(tmp_path: Path) -> Path:
    directory = tmp_path / "rust"
    (directory / "sessions" / SESSION).mkdir(parents=True)
    (directory / "sessions" / SESSION / "events.md").touch()
    return directory


def make_crate(root: Path, lib_rs: str, *tests: tuple[str, str]) -> Path:
    (root / "src").mkdir(parents=True)
    (root / "tests").mkdir(parents=True)
    (root / "Cargo.toml").write_text(CARGO_TOML, encoding="utf-8")
    (root / "src" / "lib.rs").write_text(lib_rs, encoding="utf-8")
    for name, text in tests:
        (root / "tests" / name).write_text(text, encoding="utf-8")
    return root


def make_unit(subject_dir: Path, item: str = "reuse-1") -> Path:
    """A unit directory with one practice item and its key: visible plus held-out tests."""
    unit_dir = subject_dir / "items" / UNIT
    make_crate(unit_dir / item, LIB_RS_BROKEN, ("visible.rs", VISIBLE_RS))
    make_crate(unit_dir / "key" / item, LIB_RS_PASSING, ("visible.rs", VISIBLE_RS), ("heldout.rs", HELDOUT_RS))
    return unit_dir


def learner_folder(subject_dir: Path, item: str = "reuse-1", lib_rs: str = LIB_RS_PASSING) -> Path:
    """The learner's work folder as the trainer leaves it: the item's crate copied in, then edited."""
    folder = subject_dir / "work" / SESSION / UNIT / item
    make_crate(folder, lib_rs, ("visible.rs", VISIBLE_RS))
    return folder


def snapshot(root: Path) -> dict[str, tuple[bytes, int]]:
    return {
        str(path.relative_to(root)): (path.read_bytes(), path.stat().st_mtime_ns)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def grade_events(subject_dir: Path) -> list[dict[str, str]]:
    return [row for row in read_events(subject_dir / "sessions" / SESSION / "events.md") if row["event_kind"] == "grade"]


def test_a_correct_solution_passes_every_test_including_the_heldout_one(subject_dir: Path) -> None:
    unit_dir = make_unit(subject_dir)
    learner_folder(subject_dir)

    row = practice.run_grade(subject_dir, unit_dir, "reuse-1", SESSION)

    assert (row["result"], row["fraction"]) == ("pass", "1.0000")
    logged = grade_events(subject_dir)
    assert len(logged) == 1
    assert (logged[0]["actor"], logged[0]["unit"], logged[0]["item"]) == ("tool:practice", UNIT, "reuse-1")
    assert (logged[0]["result"], logged[0]["fraction"]) == ("pass", "1.0000")


def test_a_solution_that_passes_only_the_visible_tests_fails_on_the_heldout_one(subject_dir: Path) -> None:
    """The visible tests are green in the learner's folder; the held-out test is what fails."""
    unit_dir = make_unit(subject_dir)
    learner_folder(subject_dir, lib_rs=LIB_RS_PARTIAL)

    row = practice.run_grade(subject_dir, unit_dir, "reuse-1", SESSION)

    assert (row["result"], row["fraction"]) == ("fail", "0.5000")
    assert grade_events(subject_dir)[0]["result"] == "fail"


def test_a_build_failure_grades_as_a_full_miss_and_still_logs(subject_dir: Path) -> None:
    unit_dir = make_unit(subject_dir)
    learner_folder(subject_dir, lib_rs=LIB_RS_BROKEN)

    row = practice.run_grade(subject_dir, unit_dir, "reuse-1", SESSION)

    assert (row["result"], row["fraction"]) == ("fail", "0.0000")
    assert len(grade_events(subject_dir)) == 1


def test_the_learners_folder_is_left_byte_and_mtime_identical(subject_dir: Path) -> None:
    unit_dir = make_unit(subject_dir)
    folder = learner_folder(subject_dir)
    before = snapshot(folder)

    practice.run_grade(subject_dir, unit_dir, "reuse-1", SESSION)

    assert snapshot(folder) == before  # no heldout.rs copied in, no target/, no Cargo.lock
    assert not (folder / "target").exists()
    assert not (folder / "Cargo.lock").exists()


def test_the_key_is_left_untouched(subject_dir: Path) -> None:
    unit_dir = make_unit(subject_dir)
    learner_folder(subject_dir)
    before = snapshot(unit_dir / "key")

    practice.run_grade(subject_dir, unit_dir, "reuse-1", SESSION)

    assert snapshot(unit_dir / "key") == before


def test_nothing_of_the_key_is_printed(subject_dir: Path, capsys: pytest.CaptureFixture) -> None:
    unit_dir = make_unit(subject_dir)
    learner_folder(subject_dir, lib_rs=LIB_RS_PARTIAL)  # a failing held-out test would print its name and values

    practice.run_grade(subject_dir, unit_dir, "reuse-1", SESSION)

    out = capsys.readouterr()
    shown = out.out + out.err
    assert shown.strip() == "reuse-1: fail (0.50)"
    for secret in ("heldout_secret_case", "double(5)", "assert_eq", str(unit_dir / "key")):
        assert secret not in shown


def test_the_scratch_copy_is_removed_after_grading(subject_dir: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    scratch_root = tmp_path / "scratch-root"
    scratch_root.mkdir()
    monkeypatch.setattr(tempfile, "tempdir", str(scratch_root))
    unit_dir = make_unit(subject_dir)
    learner_folder(subject_dir)

    practice.run_grade(subject_dir, unit_dir, "reuse-1", SESSION)

    assert list(scratch_root.iterdir()) == []


def test_the_scratch_path_holds_no_colon(subject_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A colon in the crate's path breaks `cargo test` on macOS (`DYLD_FALLBACK_LIBRARY_PATH`)."""
    seen: list[str] = []
    real = practice.run_cargo_test

    def spy(crate_dir: Path):
        seen.append(str(crate_dir))
        return real(crate_dir)

    monkeypatch.setattr(practice, "run_cargo_test", spy)
    unit_dir = make_unit(subject_dir)
    learner_folder(subject_dir)

    practice.run_grade(subject_dir, unit_dir, "reuse-1", SESSION)

    assert len(seen) == 1 and ":" not in seen[0]


def test_the_keys_tests_replace_a_learner_edit_to_the_visible_tests(subject_dir: Path) -> None:
    """Locked files are always the key's (items README, Grading): editing a test in the learner's
    folder cannot make a wrong solution pass."""
    unit_dir = make_unit(subject_dir)
    folder = learner_folder(subject_dir, lib_rs=LIB_RS_PARTIAL)
    (folder / "tests" / "visible.rs").write_text("#[test]\nfn visible_case() {}\n", encoding="utf-8")
    (folder / "tests" / "mine.rs").write_text("#[test]\nfn a_test_of_my_own() { panic!() }\n", encoding="utf-8")

    row = practice.run_grade(subject_dir, unit_dir, "reuse-1", SESSION)

    assert (row["result"], row["fraction"]) == ("fail", "0.5000")  # the key's two tests, one red


def test_an_item_whose_key_holds_only_visible_tests_grades_on_those(subject_dir: Path) -> None:
    """`attempt` keys hold `tests/visible.rs` alone: every test green is still the pass."""
    unit_dir = subject_dir / "items" / UNIT
    make_crate(unit_dir / "attempt", LIB_RS_BROKEN, ("visible.rs", VISIBLE_RS))
    make_crate(unit_dir / "key" / "attempt", LIB_RS_PASSING, ("visible.rs", VISIBLE_RS))
    learner_folder(subject_dir, item="attempt")

    row = practice.run_grade(subject_dir, unit_dir, "attempt", SESSION)

    assert (row["result"], row["fraction"]) == ("pass", "1.0000")


def test_it_is_independent_of_the_callers_cwd(subject_dir: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    unit_dir = make_unit(subject_dir)
    learner_folder(subject_dir)
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    monkeypatch.chdir(elsewhere)

    row = practice.run_grade(subject_dir.resolve(), unit_dir.resolve(), "reuse-1", SESSION)

    assert row["result"] == "pass"
    assert list(elsewhere.iterdir()) == []


def test_each_call_logs_one_grade_event(subject_dir: Path) -> None:
    unit_dir = make_unit(subject_dir)
    learner_folder(subject_dir)

    practice.run_grade(subject_dir, unit_dir, "reuse-1", SESSION)
    practice.run_grade(subject_dir, unit_dir, "reuse-1", SESSION)

    assert len(grade_events(subject_dir)) == 2


def test_refuses_an_item_with_no_directory_in_the_unit(subject_dir: Path) -> None:
    unit_dir = make_unit(subject_dir)
    with pytest.raises(SystemExit, match="no such practice item"):
        practice.run_grade(subject_dir, unit_dir, "reuse-9", SESSION)
    assert grade_events(subject_dir) == []


@pytest.mark.parametrize("item", ["", ".", "..", "key", "../reuse-1", "reuse-1/src", "/etc"])
def test_refuses_an_item_that_is_not_one_plain_directory_name(subject_dir: Path, item: str) -> None:
    unit_dir = make_unit(subject_dir)
    learner_folder(subject_dir)
    with pytest.raises(SystemExit, match="refused"):
        practice.run_grade(subject_dir, unit_dir, item, SESSION)
    assert grade_events(subject_dir) == []


def test_refuses_an_item_whose_key_holds_no_tests(subject_dir: Path) -> None:
    """A probe side is a directory of problems, not a practice item: its key has no `tests/`."""
    unit_dir = make_unit(subject_dir)
    (unit_dir / "probe-a" / "p1").mkdir(parents=True)
    (unit_dir / "key" / "probe-a" / "p1").mkdir(parents=True)
    with pytest.raises(SystemExit, match="no held-out tests"):
        practice.run_grade(subject_dir, unit_dir, "probe-a", SESSION)


def test_refuses_when_the_learners_folder_does_not_exist(subject_dir: Path) -> None:
    unit_dir = make_unit(subject_dir)
    with pytest.raises(SystemExit, match="nothing in the learner's folder"):
        practice.run_grade(subject_dir, unit_dir, "reuse-1", SESSION)
    assert grade_events(subject_dir) == []


def test_refuses_an_unopened_session_before_running_anything(subject_dir: Path) -> None:
    unit_dir = make_unit(subject_dir)
    learner_folder(subject_dir)
    with pytest.raises(SystemExit, match="no such session"):
        practice.run_grade(subject_dir, unit_dir, "reuse-1", "no-such-session")


def test_cli_grade_logs_a_grade_event_and_prints_one_line(tmp_path: Path) -> None:
    subject = tmp_path / "rust"
    (subject / "sessions" / SESSION).mkdir(parents=True)
    (subject / "sessions" / SESSION / "events.md").touch()
    unit_dir = make_unit(subject)
    learner_folder(subject)

    result = CliRunner().invoke(app, ["practice", "grade", str(unit_dir), "--item", "reuse-1", "--session", SESSION])

    assert result.exit_code == 0, result.output
    assert result.output.strip() == "reuse-1: pass (1.00)"
    assert [(row["actor"], row["result"]) for row in grade_events(subject)] == [("tool:practice", "pass")]


def test_cli_grade_requires_item_and_session(tmp_path: Path) -> None:
    unit_dir = make_unit(tmp_path / "rust")
    runner = CliRunner()
    assert runner.invoke(app, ["practice", "grade", str(unit_dir), "--session", SESSION]).exit_code == 2
    assert runner.invoke(app, ["practice", "grade", str(unit_dir), "--item", "reuse-1"]).exit_code == 2


def test_cli_grade_exits_nonzero_on_a_refusal(tmp_path: Path) -> None:
    subject = tmp_path / "rust"
    (subject / "sessions" / SESSION).mkdir(parents=True)
    (subject / "sessions" / SESSION / "events.md").touch()
    unit_dir = make_unit(subject)

    result = CliRunner().invoke(app, ["practice", "grade", str(unit_dir), "--item", "reuse-1", "--session", SESSION])

    assert result.exit_code == 1
    assert grade_events(subject) == []
