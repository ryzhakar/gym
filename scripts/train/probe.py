"""Present a unit's probe items, time the attempt against the shared cap, grade each item, log one row per item.

Usage: `uv run python scripts/train/probe.py <unit_dir> immediate|delayed --session-id <id> [--cap-minutes 10]`.

`immediate` presents the unit's `probe-a/`, `delayed` its `probe-b/` — the isomorph the delayed
check reads against (fable-plan.md § 1 T3, § 7 "isomorph illusion"). Layout is P3's (`items/README.md`):
`probe-a/`/`probe-b/` hold several standalone problem crates (`p1-*`, `p2-*`, `p3-*`), one cap shared
across all of them (each problem's own `spec.md` says so: "10 minutes for p1, p2 and p3 together"),
one `items` row logged per problem. `key/<which>/<problem>/` mirrors every problem path and holds the
held-out tests; presentation (`item_text`) never opens or prints anything under a `key/` path
component, anywhere. Grading is the one place that does read `key/` — P3-selfcheck "Found during the
check" #3, decided by the team lead 2026-09-28: the no-key rule binds the trainer session
(`allowlist.md`), not this script's own grading step. Grading only ever *copies* the held-out test
files into the learner's problem directory, runs the tests, and removes exactly what it copied in —
it never prints a key file's content, on any path, at any point.

`training/rust/items/` stays read-only in use (team lead ruling, 2026-09-28): the learner never
edits a committed stub directly. Before presenting or grading, every problem crate is copied to
`training/rust/work/<session_id>/<unit>/<problem>/` (gitignored); that copy is what gets presented,
edited, and graded — `items/` itself is only ever read from.
"""
from __future__ import annotations

import argparse
import csv
import re
import shutil
import subprocess
import sys
import time
from datetime import date, datetime
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).parent))
from log import append_row, build_row  # noqa: E402
from record_schema import ROOT, TIMESTAMP_FORMAT, file_path  # noqa: E402

CAP_MINUTES_DEFAULT = 10.0  # O2, first-protocol default, unmeasured (fable-plan.md § 6 O2)
KIND_OF = {"immediate": "probe-immediate", "delayed": "probe-delayed"}
ISOMORPH_OF = {"immediate": "probe-a", "delayed": "probe-b"}
WORK_ROOT = ROOT / "training/rust/work"


def assert_no_key(path: Path) -> None:
    """The presentation-side guard: never used by grading, which reads `key/` by design (see module docstring)."""
    if "key" in path.parts:
        sys.exit(f"refused, probe.py never opens or prints a 'key/' path for display: {path}")


def probe_dir(unit_dir: Path, which: str) -> Path:
    target = unit_dir / ISOMORPH_OF[which]
    assert_no_key(target)
    if not target.is_dir():
        sys.exit(f"refused, no such probe directory: {target}")
    return target


def list_problem_dirs(directory: Path) -> list[Path]:
    """Every problem crate directly under `directory` (its own `Cargo.toml`), sorted by name — P3's
    "a probe is three crates, not one workspace" (items/README.md § Layout)."""
    problems = sorted(path for path in directory.iterdir() if path.is_dir() and (path / "Cargo.toml").is_file())
    if not problems:
        sys.exit(f"refused, no problem crates under {directory}")
    return problems


PRESENTATION_EXCLUDED_SEGMENTS = ("key", "target")  # target/: cargo's own build directory, left in
# place by a real grading run since each item declares its own `[workspace]` (items/README.md § Layout)
# — binary artifacts under it are never presented, and re-presenting an already-graded item must not
# choke trying to read them as text.


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
    """`(all passed, fraction passed)`. A build failure (a "fix the compile error" stub that doesn't
    yet compile is the ordinary case for a probe item, not a broken setup — P3-selfcheck's own table
    of stub `cargo test` results is mostly build errors) grades as a full miss, `(False, 0.0)`, never
    a script abort: every item still gets its row."""
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
    """`session_id` (`YYYY-MM-DDTHH:MM`) made safe as a filesystem path component. A colon in a
    crate's absolute path breaks `cargo test` on macOS: `cargo` puts that path in
    `$DYLD_FALLBACK_LIBRARY_PATH`, which uses `:` as its own list separator, and a real dry run
    (2026-09-29, P6) hit exactly this — `error: failed to join paths from
    '$DYLD_FALLBACK_LIBRARY_PATH' together` — the first time a real, colon-bearing session id
    reached a real `cargo test` rather than a test's own harmless `"sess-1"`-style stand-in. Every
    `:` becomes `-`; never parsed back into a timestamp, only ever compared for equality by whoever
    builds the same path again (`session.unit_paths` does, via this same function)."""
    return session_id.replace(":", "-")


def stage_item(source_dir: Path, session_id: str, unit: str, kind: str) -> Path:
    """Copy `source_dir`'s stub crate into
    `training/rust/work/<session_id, path-safe>/<unit>/<kind>/<source_dir.name>/` — the learner
    edits and is graded there, never in `source_dir` itself (team lead ruling, 2026-09-28).
    Re-staging the same problem in the same session starts from the stub again.

    `kind` (`"probe"` here, `"practice"` in `session.py`) keeps the two staging areas apart under
    one unit: the trainer's permission grant is scoped to `.../<unit>/practice/` alone (team lead
    ruling, 2026-09-28), and a probe item staged in the same session under `.../<unit>/probe/` must
    never fall inside that grant by a naming coincidence — rule 19, the trainer never sees a probe."""
    work_dir = WORK_ROOT / session_path_segment(session_id) / unit / kind / source_dir.name
    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_dir, work_dir)
    return work_dir


def key_dir_for(unit_dir: Path, which: str, problem_name: str) -> Path:
    return unit_dir / "key" / ISOMORPH_OF[which] / problem_name


def heldout_test_files(key_problem_dir: Path, problem_dir: Path) -> list[Path]:
    """Files under `key_problem_dir/tests/` the learner's `problem_dir/tests/` doesn't already have —
    the held-out tests (`items/README.md` § Grading); a file already there (`visible.rs`) is never
    touched or overwritten."""
    key_tests = key_problem_dir / "tests"
    if not key_tests.is_dir():
        return []
    learner_tests = {path.name for path in (problem_dir / "tests").glob("*")} if (problem_dir / "tests").is_dir() else set()
    return sorted(path for path in key_tests.iterdir() if path.name not in learner_tests)


def grade_item(problem_dir: Path, key_problem_dir: Path) -> tuple[bool, float]:
    """Copy the held-out test files from `key_problem_dir` into the learner's own `problem_dir`, run
    `cargo test --no-fail-fast` there against the learner's actual edited source, then remove exactly
    the files this copied in — never printed at any point, never left behind, whatever `cargo test`
    does (team lead ruling, 2026-09-28)."""
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


def delay_days_for(unit: str) -> float:
    """Days since the unit's most recent logged practice item; 0 when none is logged yet."""
    path = file_path("items")
    if not path.is_file():
        return 0.0
    with path.open(encoding="utf-8", newline="") as handle:
        practice = [row for row in csv.DictReader(handle) if row["unit"] == unit and row["kind"] == "practice"]
    if not practice:
        return 0.0
    latest = max(row["timestamp"] for row in practice)
    then = datetime.strptime(latest, TIMESTAMP_FORMAT).date()
    return float((date.today() - then).days)


def run_probe(
    unit_dir: Path,
    which: str,
    session_id: str,
    cap_minutes: float = CAP_MINUTES_DEFAULT,
    wait: Callable[[], None] = lambda: input(),
    clock: Callable[[], float] = time.monotonic,
) -> list[dict[str, str]]:
    unit = unit_dir.name
    directory = probe_dir(unit_dir, which)
    problems = list_problem_dirs(directory)
    staged = [stage_item(problem, session_id, unit, kind="probe") for problem in problems]
    for work_dir in staged:
        print(item_text(work_dir))
        print()
    print(f"cap: {cap_minutes:g} min total for {len(problems)} item(s). Press Enter once your answers are in place.")
    start = clock()
    wait()
    elapsed_minutes = (clock() - start) / 60
    if elapsed_minutes > cap_minutes:
        print(f"over the {cap_minutes:g}-minute cap: {elapsed_minutes:.1f} min")
    delay_days = 0.0 if which == "immediate" else delay_days_for(unit)
    rows = []
    for problem, work_dir in zip(problems, staged):
        passed, continuous = grade_item(work_dir, key_dir_for(unit_dir, which, problem.name))
        fields = {
            "item_id": f"{unit}-{ISOMORPH_OF[which]}-{problem.name}",
            "unit": unit,
            "kind": KIND_OF[which],
            "delay_days": str(delay_days),
            "pass": "true" if passed else "false",
            "continuous": f"{continuous:.4f}",
            "minutes": f"{elapsed_minutes:.2f}",
            "attempts": "1",
        }
        row = build_row("items", fields)
        append_row("items", row)
        rows.append(row)
    return rows


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("unit_dir", type=Path)
    parser.add_argument("which", choices=["immediate", "delayed"])
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--cap-minutes", type=float, default=CAP_MINUTES_DEFAULT)
    args = parser.parse_args(argv[1:])
    rows = run_probe(args.unit_dir, args.which, args.session_id, args.cap_minutes)
    for row in rows:
        print(f"logged: {row}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
