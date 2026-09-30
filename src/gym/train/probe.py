"""gym train probe: stage a unit's probe problems, then grade them against their keys, one
`probe-item` event per problem.

Split in two, on the team lead's ruling (2026-09-30), replacing an earlier single interactive
command that waited on stdin: `gym train probe stage` copies every problem crate to its work path
and logs a `probe-start` event (the time, and the list of problems staged); `gym train probe grade`
re-reads that event — refusing outright if none exists for this unit and probe side in this
session — grades each staged problem against its key, computes elapsed minutes from the
`probe-start` event's own timestamp to now, and logs one `probe-item` event per problem. No
interactive wait anywhere; the two commands are two separate, ordinary invocations, run whenever
the caller is ready for each.

Every other rule from the original, single-command version (itself moved whole from
`scripts/train/probe.py`, untouched, still live) is kept: `immediate` reads `probe-a/`, `delayed`
reads `probe-b/`; a `key/` path is never opened or printed for display, only read at grading time,
by copying its held-out test files in, running `cargo test`, and always removing exactly what was
copied; a build failure grades as a full miss, never a script abort; the session's id is sanitized
before it becomes a path component (`cargo test`'s `$DYLD_FALLBACK_LIBRARY_PATH` breaks on a
literal `:` on macOS — moot in practice now that `gym train open` only ever produces a hyphen-shaped
id, but kept as a defensive second layer).
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from gym.train.events import append_event, events_path, read_events
from gym.train.schema import TIMESTAMP_FORMAT

ISOMORPH_OF = {"immediate": "probe-a", "delayed": "probe-b"}


def assert_no_key(path: Path) -> None:
    """The presentation-side guard: never used by grading, which reads `key/` by design."""
    if "key" in path.parts:
        sys.exit(f"refused, probe never opens or prints a 'key/' path for display: {path}")


def probe_dir(unit_dir: Path, which: str) -> Path:
    target = unit_dir / ISOMORPH_OF[which]
    assert_no_key(target)
    if not target.is_dir():
        sys.exit(f"refused, no such probe directory: {target}")
    return target


def list_problem_dirs(directory: Path) -> list[Path]:
    """Every problem crate directly under `directory` (its own `Cargo.toml`), sorted by name."""
    problems = sorted(path for path in directory.iterdir() if path.is_dir() and (path / "Cargo.toml").is_file())
    if not problems:
        sys.exit(f"refused, no problem crates under {directory}")
    return problems


PRESENTATION_EXCLUDED_SEGMENTS = ("key", "target")


def item_text(directory: Path) -> str:
    """Every file's text under `directory`, sorted by path, excluding `key/` and a build's `target/`."""
    parts = []
    for path in sorted(directory.rglob("*")):
        if any(part in PRESENTATION_EXCLUDED_SEGMENTS for part in path.relative_to(directory).parts):
            continue
        if path.is_file():
            assert_no_key(path)
            parts.append(f"--- {path.relative_to(directory)} ---\n{path.read_text(encoding='utf-8')}")
    return "\n\n".join(parts)


def run_cargo_test(crate_dir: Path) -> tuple[bool, float]:
    """`(all passed, fraction passed)`. A build failure grades as a full miss, `(False, 0.0)`,
    never a script abort — every item still gets logged."""
    manifest = crate_dir / "Cargo.toml"
    if not manifest.is_file():
        sys.exit(f"refused, no crate at {crate_dir}")
    result = subprocess.run(
        ["cargo", "test", "--no-fail-fast", "--manifest-path", str(manifest)],
        capture_output=True,
        text=True,
        check=False,
    )
    passed = failed = 0
    for match in re.finditer(r"test result: \w+\. (\d+) passed; (\d+) failed", result.stdout):
        passed += int(match.group(1))
        failed += int(match.group(2))
    if passed + failed == 0:
        return False, 0.0
    return failed == 0, passed / (passed + failed)


def session_path_segment(session_id: str) -> str:
    """`session_id` made safe as a filesystem path component: a colon breaks `cargo test` on macOS
    (`$DYLD_FALLBACK_LIBRARY_PATH` uses `:` as its own separator). `gym train open` now refuses any
    session id not already shaped `YYYY-MM-DDTHH-MM` (hyphen — team lead ruling, 2026-09-30), so
    this is normally a no-op; kept as a defensive second layer for any id that reaches here some
    other way."""
    return session_id.replace(":", "-")


def stage_item(source_dir: Path, work_root: Path, session_id: str, unit: str) -> Path:
    """Copy `source_dir`'s stub crate into `<work_root>/<session_id, path-safe>/<unit>/<name>/` —
    the learner edits and is graded there, never in `source_dir` itself."""
    work_dir = work_root / session_path_segment(session_id) / unit / source_dir.name
    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_dir, work_dir)
    return work_dir


def key_dir_for(unit_dir: Path, which: str, problem_name: str) -> Path:
    return unit_dir / "key" / ISOMORPH_OF[which] / problem_name


def heldout_test_files(key_problem_dir: Path, problem_dir: Path) -> list[Path]:
    """Files under `key_problem_dir/tests/` the learner's `problem_dir/tests/` doesn't already have."""
    key_tests = key_problem_dir / "tests"
    if not key_tests.is_dir():
        return []
    learner_tests = {path.name for path in (problem_dir / "tests").glob("*")} if (problem_dir / "tests").is_dir() else set()
    return sorted(path for path in key_tests.iterdir() if path.name not in learner_tests)


def grade_item(problem_dir: Path, key_problem_dir: Path) -> tuple[bool, float]:
    """Copy the held-out test files in, run `cargo test --no-fail-fast`, then remove exactly the
    files this copied in — never printed at any point, never left behind, whatever the tests do."""
    copied: list[Path] = []
    try:
        for source in heldout_test_files(key_problem_dir, problem_dir):
            target = problem_dir / "tests" / source.name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            copied.append(target)
        return run_cargo_test(problem_dir)
    finally:
        for path in copied:
            path.unlink(missing_ok=True)


def run_stage(subject_dir: Path, unit_dir: Path, which: str, session_id: str) -> dict:
    """Copy every problem crate for `which` into its work path and log one `probe-start` event
    naming them, in staged order. Returns `{'line', 'problem_names', 'staged'}`; prints each
    staged path (never the item text — presentation is no longer this command's job)."""
    unit = unit_dir.name
    work_root = subject_dir / "work"
    directory = probe_dir(unit_dir, which)
    problems = list_problem_dirs(directory)
    staged = [stage_item(problem, work_root, session_id, unit) for problem in problems]
    problem_names = [problem.name for problem in problems]
    line = append_event(
        subject_dir, session_id, "tool:probe", "probe-start",
        {"unit": unit, "which": which, "problems": ",".join(problem_names)},
    )
    for work_dir in staged:
        print(work_dir)
    return {"line": line, "problem_names": problem_names, "staged": staged}


def latest_probe_start(subject_dir: Path, session_id: str, unit: str, which: str) -> "dict[str, str] | None":
    """The most recent `probe-start` event for `unit`/`which` in this session, or `None`."""
    rows = read_events(events_path(subject_dir, session_id))
    matches = [row for row in rows if row["event_kind"] == "probe-start" and row["unit"] == unit and row["which"] == which]
    return matches[-1] if matches else None


def run_grade(
    subject_dir: Path,
    unit_dir: Path,
    which: str,
    session_id: str,
    now: "datetime | None" = None,
) -> list[dict[str, str]]:
    """Grade every problem `gym train probe stage` staged for `unit_dir`/`which` in this session,
    against its key, and log one `probe-item` event each. Refuses outright if no `probe-start`
    event exists for this unit and probe side in this session. `minutes` is elapsed time from that
    `probe-start` event's own clock stamp to `now` (or `datetime.now()`), shared across every
    problem — the same "one cap for the whole probe" semantics the original single command had,
    now measured across two separate invocations instead of one wait."""
    unit = unit_dir.name
    start_row = latest_probe_start(subject_dir, session_id, unit, which)
    if start_row is None:
        sys.exit(f"refused, no probe-start event for unit {unit!r}, which {which!r}, in session {session_id}")
    started = datetime.strptime(start_row["timestamp"], TIMESTAMP_FORMAT)
    elapsed_minutes = ((now or datetime.now()) - started).total_seconds() / 60
    work_root = subject_dir / "work"
    rows: list[dict[str, str]] = []
    for problem_name in start_row["problems"].split(","):
        work_dir = work_root / session_path_segment(session_id) / unit / problem_name
        passed, fraction = grade_item(work_dir, key_dir_for(unit_dir, which, problem_name))
        fields = {
            "unit": unit,
            "which": which,
            "problem": problem_name,
            "result": "pass" if passed else "fail",
            "minutes": f"{elapsed_minutes:.2f}",
            "fraction": f"{fraction:.4f}",
        }
        line = append_event(subject_dir, session_id, "tool:probe", "probe-item", fields)
        rows.append({"line": line, **fields})
        print(f"{problem_name}: {fields['result']} ({fraction:.2f})")
    return rows
