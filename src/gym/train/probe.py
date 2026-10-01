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

`gym train probe go` (session 2026-10-01T15-56 narrative): a probe may be staged before the learner
starts, so the learner's start is its own event, `probe-go`, logged by this command after `stage`.
`grade` measures from the latest `probe-go` of that unit and side since its latest staging when one
exists — each problem's `minutes` and the probe's `total_minutes` are the last save minus the go,
floored at 0 — and from the `probe-start` stage time, as before, when none does.

Team lead ruling (2026-09-30): a unit may carry a third probe side, `probe-c`, for a repeat of the
unit — and any further side of the same shape. `which` still accepts `immediate`/`delayed` as
aliases for `probe-a`/`probe-b`, or a literal side name matching `probe-[a-z]` (`resolve_side`);
every event this module logs carries that resolved, literal side name in its own `which` field, so
a stored event's `which` is always one spelling, never an alias (schema widened to match).
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Callable

from gym.train.events import append_event, events_path, read_events
from gym.train.schema import TIMESTAMP_FORMAT

ISOMORPH_OF = {"immediate": "probe-a", "delayed": "probe-b"}

# A literal probe-side directory name: `probe-a`, `probe-b`, `probe-c`, ... — matches the schema's
# own `which` pattern for `probe-start`/`probe-item` (`gym.train.schema.KINDS`).
SIDE_PATTERN = re.compile(r"probe-[a-z]")


def resolve_side(which: str) -> str:
    """The canonical, literal probe-side name for `which`: `immediate` and `delayed` still mean
    `probe-a` and `probe-b`; anything else must already be a literal `probe-[a-z]` name (a unit's
    repeat side, `probe-c`, or any later one of the same shape). Refuses otherwise."""
    if which in ISOMORPH_OF:
        return ISOMORPH_OF[which]
    if SIDE_PATTERN.fullmatch(which):
        return which
    sys.exit(f"refused, not 'immediate', 'delayed', or a literal 'probe-[a-z]' side name: {which!r}")


def assert_no_key(path: Path) -> None:
    """The presentation-side guard: never used by grading, which reads `key/` by design."""
    if "key" in path.parts:
        sys.exit(f"refused, probe never opens or prints a 'key/' path for display: {path}")


def probe_dir(unit_dir: Path, which: str) -> Path:
    target = unit_dir / resolve_side(which)
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
    return unit_dir / "key" / resolve_side(which) / problem_name


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
    staged path (never the item text — presentation is no longer this command's job). The event's
    own `which` is always the resolved, literal side name (`resolve_side`), never `immediate` or
    `delayed`."""
    unit = unit_dir.name
    work_root = subject_dir / "work"
    side = resolve_side(which)
    directory = probe_dir(unit_dir, which)
    problems = list_problem_dirs(directory)
    staged = [stage_item(problem, work_root, session_id, unit) for problem in problems]
    problem_names = [problem.name for problem in problems]
    line = append_event(
        subject_dir, session_id, "tool:probe", "probe-start",
        {"unit": unit, "which": side, "problems": ",".join(problem_names)},
    )
    for work_dir in staged:
        print(work_dir)
    return {"line": line, "problem_names": problem_names, "staged": staged}


def latest_probe_start(subject_dir: Path, session_id: str, unit: str, which: str) -> "dict[str, str] | None":
    """The most recent `probe-start` event for `unit`/`which` (an alias or a literal side name,
    resolved the same way `run_stage` resolved it before logging) in this session, or `None`."""
    side = resolve_side(which)
    rows = read_events(events_path(subject_dir, session_id))
    matches = [row for row in rows if row["event_kind"] == "probe-start" and row["unit"] == unit and row["which"] == side]
    return matches[-1] if matches else None


def run_go(
    subject_dir: Path, unit_dir: Path, which: str, session_id: str, now: "datetime | None" = None
) -> dict:
    """Log one `probe-go` event: the learner's start mark for the probe `run_stage` staged for
    `unit_dir`/`which` in this session. Refuses outright if no `probe-start` event exists for that
    unit and side in this session, since a mark with nothing staged marks nothing. Returns
    `{'line'}` and prints the line. The event's own `which` is the resolved, literal side name."""
    unit = unit_dir.name
    side = resolve_side(which)
    if latest_probe_start(subject_dir, session_id, unit, which) is None:
        sys.exit(f"refused, no probe-start event for unit {unit!r}, which {side!r}, in session {session_id}; stage first")
    line = append_event(subject_dir, session_id, "tool:probe", "probe-go", {"unit": unit, "which": side}, now=now)
    print(line)
    return {"line": line}


def latest_probe_go(subject_dir: Path, session_id: str, unit: str, which: str) -> "dict[str, str] | None":
    """The most recent `probe-go` event for `unit`/`which` in this session that comes after the
    latest `probe-start` of that unit and side in the file, or `None`. A go before the latest
    staging marked work that staging wiped, so it does not count; file order, not the minute
    stamp, decides, since a go may share the stage's minute."""
    side = resolve_side(which)
    rows = read_events(events_path(subject_dir, session_id))
    starts = [
        index
        for index, row in enumerate(rows)
        if row["event_kind"] == "probe-start" and row["unit"] == unit and row["which"] == side
    ]
    if not starts:
        return None
    goes = [
        row
        for row in rows[starts[-1] + 1 :]
        if row["event_kind"] == "probe-go" and row["unit"] == unit and row["which"] == side
    ]
    return goes[-1] if goes else None


CAP_MINUTES_DEFAULT = 10.0


def latest_mtime_under(directory: Path, skip: "Callable[[Path], bool] | None" = None) -> "float | None":
    """The most recent modification time (epoch seconds) among every file under `directory` that
    `skip` (given the file's path relative to `directory`) does not name, or `None` when there is
    none (missing, empty, or all skipped)."""
    if not directory.is_dir():
        return None
    mtimes = [
        path.stat().st_mtime
        for path in directory.rglob("*")
        if path.is_file() and not (skip and skip(path.relative_to(directory)))
    ]
    return max(mtimes) if mtimes else None


# What is never the learner's own save, in a problem's folder: the bank's test files, cargo's build
# output, the manifest and lockfile cargo and the learner's own `cargo` runs write, the spec, and
# bacon's `.bacon-locations`, which bacon writes whenever it runs a check (live data: 4 to 346 seconds
# after the last `src/` edit).
# Directories at the folder's root only, files at the root only: a `tests` under `src/` is work.
NOT_A_SAVE_DIRS = ("tests", "target")
NOT_A_SAVE_FILES = ("Cargo.toml", "Cargo.lock", "spec.md", ".bacon-locations")


def _is_not_a_save(relative: Path) -> bool:
    if len(relative.parts) == 1:
        return relative.name in NOT_A_SAVE_FILES
    return relative.parts[0] in NOT_A_SAVE_DIRS


def latest_save_mtime(work_dir: Path) -> "float | None":
    """A problem's last-save time: the newest modification time over every file in `work_dir`
    except `tests/`, `target/`, `Cargo.toml`, `Cargo.lock`, `spec.md` and `.bacon-locations` (`NOT_A_SAVE_*`), or `None`
    when no other file exists. Any edit counts — `src/`, a predict-output item's `prediction.txt`,
    any file the learner adds — where an earlier version read only `src/` and gave a problem that
    edits `prediction.txt` 0.00 minutes (session 2026-10-01T15-56). Probe and baseline grading both
    read it."""
    return latest_mtime_under(work_dir, skip=_is_not_a_save)


def minutes_since(reference: datetime, mtime_epoch: "float | None") -> float:
    """Minutes from `reference` to the local time `mtime_epoch` names, floored at 0. `None` (no
    file at all) or an `mtime_epoch` at or before `reference` both read as `0.0` — team lead ruling
    (2026-09-30): "an untouched problem gets minutes=0".

    Known precision limit, not fixed here: `reference` is a `probe-start` event's own timestamp,
    truncated to the minute (`TIMESTAMP_FORMAT` has no seconds), while `mtime_epoch` is a real,
    second-precision filesystem timestamp. `gym train probe stage`'s own `shutil.copytree` runs at
    the *real* instant the event was logged, which is always at or after that truncated minute, by
    up to 59 seconds — so an untouched problem's true `minutes` can read as up to ~1 (never
    negative, thanks to the floor above) rather than exactly `0`, depending on where in the minute
    staging happened to land. This is a property of every event timestamp in this schema, not a bug
    specific to this function; narrowing it would mean giving `probe-start` sub-minute precision,
    which the task never asked for."""
    if mtime_epoch is None:
        return 0.0
    touched = datetime.fromtimestamp(mtime_epoch)
    return max(0.0, (touched - reference).total_seconds() / 60)


def run_grade(
    subject_dir: Path,
    unit_dir: Path,
    which: str,
    session_id: str,
    cap_minutes: float = CAP_MINUTES_DEFAULT,
    now: "datetime | None" = None,
) -> list[dict[str, str]]:
    """Grade every problem `gym train probe stage` staged for `unit_dir`/`which` in this session,
    against its key, and log one `probe-item` event each. Refuses outright if no `probe-start`
    event exists for this unit and probe side in this session.

    Team lead ruling (2026-09-30): each event's own `minutes` is per-problem, not shared — the
    last-save time of that problem's staged folder (`latest_save_mtime`) minus the reference time
    (`minutes_since`), so an untouched problem (never edited since staging) reads `minutes=0`, and
    a problem the learner actually worked on reads how long *that* work took. `total_minutes` is
    the probe's own time, the same on every problem in one call; `over_cap` (`yes`/`no`, recorded
    only, never enforced or refused) is judged against it.

    The reference time is the latest `probe-go` of this unit and side since its latest staging
    (`latest_probe_go`) when one exists: then `total_minutes` is the latest save over every problem
    minus the go, floored at 0 (0 when nothing was saved). With no go it is the `probe-start`
    event's own clock stamp, and `total_minutes` is `now` (or `datetime.now()`) minus that stamp."""
    unit = unit_dir.name
    side = resolve_side(which)
    start_row = latest_probe_start(subject_dir, session_id, unit, which)
    if start_row is None:
        sys.exit(f"refused, no probe-start event for unit {unit!r}, which {side!r}, in session {session_id}")
    started = datetime.strptime(start_row["timestamp"], TIMESTAMP_FORMAT)
    go_row = latest_probe_go(subject_dir, session_id, unit, which)
    reference = datetime.strptime(go_row["timestamp"], TIMESTAMP_FORMAT) if go_row else started
    work_root = subject_dir / "work"
    problem_names = start_row["problems"].split(",")
    work_dirs = {name: work_root / session_path_segment(session_id) / unit / name for name in problem_names}
    saves = {name: latest_save_mtime(work_dirs[name]) for name in problem_names}
    if go_row:
        total_minutes = minutes_since(reference, max((mtime for mtime in saves.values() if mtime is not None), default=None))
    else:
        total_minutes = max(0.0, ((now or datetime.now()) - started).total_seconds() / 60)
    over_cap = "yes" if total_minutes > cap_minutes else "no"
    rows: list[dict[str, str]] = []
    for problem_name in problem_names:
        item_minutes = minutes_since(reference, saves[problem_name])
        passed, fraction = grade_item(work_dirs[problem_name], key_dir_for(unit_dir, which, problem_name))
        fields = {
            "unit": unit,
            "which": side,
            "problem": problem_name,
            "result": "pass" if passed else "fail",
            "minutes": f"{item_minutes:.2f}",
            "total_minutes": f"{total_minutes:.2f}",
            "over_cap": over_cap,
            "fraction": f"{fraction:.4f}",
        }
        line = append_event(subject_dir, session_id, "tool:probe", "probe-item", fields)
        rows.append({"line": line, **fields})
        print(f"{problem_name}: {fields['result']} ({fraction:.2f})")
    return rows
