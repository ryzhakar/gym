"""gym train probe: present a unit's probe items, time the attempt against the shared cap, grade
each item against its key, log one `probe-item` event per problem.

Moved whole from `scripts/train/probe.py` (untouched, still live), keeping every rule that script
enforced: `immediate` reads `probe-a/`, `delayed` reads `probe-b/`; one cap shared across every
problem crate in the probe; a `key/` path is never opened or printed for display, only read at
grading time, by copying its held-out test files in, running `cargo test`, and always removing
exactly what was copied; a build failure grades as a full miss, never a script abort; the session's
colon-bearing id is sanitized before it becomes a path component (`cargo test`'s
`$DYLD_FALLBACK_LIBRARY_PATH` breaks on a literal `:` on macOS). The one change: the write target
is a `probe-item` event under the session's own `events.md`, not an `items` CSV row.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Callable

from gym.train.events import append_event

CAP_MINUTES_DEFAULT = 10.0
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


def run_probe(
    subject_dir: Path,
    unit_dir: Path,
    which: str,
    session_id: str,
    cap_minutes: float = CAP_MINUTES_DEFAULT,
    wait: Callable[[], None] = lambda: input(),
    clock: Callable[[], float] = time.monotonic,
) -> list[dict[str, str]]:
    unit = unit_dir.name
    work_root = subject_dir / "work"
    directory = probe_dir(unit_dir, which)
    problems = list_problem_dirs(directory)
    staged = [stage_item(problem, work_root, session_id, unit) for problem in problems]
    for work_dir in staged:
        print(item_text(work_dir))
        print()
    print(f"cap: {cap_minutes:g} min total for {len(problems)} item(s). Press Enter once your answers are in place.")
    start = clock()
    wait()
    elapsed_minutes = (clock() - start) / 60
    if elapsed_minutes > cap_minutes:
        print(f"over the {cap_minutes:g}-minute cap: {elapsed_minutes:.1f} min")
    rows: list[dict[str, str]] = []
    for problem, work_dir in zip(problems, staged):
        passed, fraction = grade_item(work_dir, key_dir_for(unit_dir, which, problem.name))
        fields = {
            "unit": unit,
            "which": which,
            "problem": problem.name,
            "result": "pass" if passed else "fail",
            "minutes": f"{elapsed_minutes:.2f}",
            "fraction": f"{fraction:.4f}",
        }
        line = append_event(subject_dir, session_id, "tool:probe", "probe-item", fields)
        rows.append({"line": line, **fields})
    return rows
