"""gym train baseline: stage a baseline item's stub, then grade it against its key — the same
`stage`/`grade` split as `gym train probe`, for the six items under `<subject_dir>/items/baseline/`
(`training/rust/items/README.md` §Layout: `spec.md` + `stub/` + `key/`, no `probe-a`/`probe-b`
sides — `probe_dir` refuses that shape outright, confirmed live in
`recon/2026-09-30/train/baseline-procedure.md`).

`stage` copies the item's `stub/` to `<subject_dir>/work/<session, path-safe>/baseline/<item>/`
and logs a `present` event (`unit=baseline item=<item>`) — the same event kind a unit's own item
presentation uses, and the one `grade` re-reads for its own elapsed-time reference, the way
`probe-item` re-reads `probe-start`. `grade` copies the key's held-out test files in
(`gym.train.probe.heldout_test_files`/`grade_item`, reused unchanged — `key/` is read, never
opened for display or printed), runs `cargo test --no-fail-fast`, and logs one `probe-item` event
(`which=baseline`, reusing the probe schema's own kind rather than adding a parallel one for a
single literal value — schema widened to admit it, `gym.train.schema.KINDS['probe-item']`).

Finding 4 (`recon/2026-09-30/train/trainer-quality-report.md`): the by-hand copy loop the first
session ran silently downgraded 5 of 6 baseline items to visible-tests-only, since it depended on
the caller's shell `cwd`. Every path here is built from `subject_dir` (already resolved absolute by
the CLI layer) and the command's own `--item`/`--session` arguments — never `Path.cwd()`.
"""
from __future__ import annotations

import shutil
import sys
from datetime import datetime
from pathlib import Path

from gym.train.events import append_event, events_path, read_events
from gym.train.probe import CAP_MINUTES_DEFAULT, grade_item, minutes_since, session_path_segment
from gym.train.schema import TIMESTAMP_FORMAT


def baseline_root(subject_dir: Path) -> Path:
    return subject_dir / "items" / "baseline"


def all_baseline_items(subject_dir: Path) -> list[str]:
    """Every baseline item's directory name under `baseline_root`, sorted — `b1-own` through
    `b6-enum` in order, since all six share the same `b<n>-<name>` width."""
    directory = baseline_root(subject_dir)
    if not directory.is_dir():
        sys.exit(f"refused, no such directory: {directory}")
    items = sorted(path.name for path in directory.iterdir() if path.is_dir())
    if not items:
        sys.exit(f"refused, no baseline items under {directory}")
    return items


def item_dir(subject_dir: Path, item: str) -> Path:
    target = baseline_root(subject_dir) / item
    if not target.is_dir():
        sys.exit(f"refused, no such baseline item: {target}")
    return target


def stub_dir(one_item_dir: Path) -> Path:
    target = one_item_dir / "stub"
    if not target.is_dir():
        sys.exit(f"refused, no stub for baseline item: {one_item_dir.name}")
    return target


def work_dir_for(subject_dir: Path, session_id: str, item: str) -> Path:
    return subject_dir / "work" / session_path_segment(session_id) / "baseline" / item


def stage_item(one_item_dir: Path, subject_dir: Path, session_id: str, item: str) -> Path:
    """Copy `one_item_dir`'s `stub/` into its work path, replacing whatever was staged there
    before — the learner edits and is graded there, `training/rust/items/` itself never touched."""
    stub = stub_dir(one_item_dir)
    target = work_dir_for(subject_dir, session_id, item)
    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(stub, target)
    return target


def run_stage(subject_dir: Path, item: str, session_id: str) -> dict:
    """Stage one baseline item and log its `present` event. Returns `{'line', 'work_dir'}`; prints
    the staged path."""
    one_item_dir = item_dir(subject_dir, item)
    work_dir = stage_item(one_item_dir, subject_dir, session_id, item)
    line = append_event(subject_dir, session_id, "tool:probe", "present", {"unit": "baseline", "item": item})
    print(work_dir)
    return {"line": line, "work_dir": work_dir}


def run_stage_all(subject_dir: Path, session_id: str) -> list[dict]:
    """Stage every baseline item, in order (`all_baseline_items`)."""
    return [run_stage(subject_dir, item, session_id) for item in all_baseline_items(subject_dir)]


def latest_present(subject_dir: Path, session_id: str, item: str) -> "dict[str, str] | None":
    """The most recent `present` event for `unit=baseline`, this `item`, in this session, or
    `None` — the reference `run_grade` measures elapsed minutes from, the way probe grading reads
    back its own `probe-start` event."""
    rows = read_events(events_path(subject_dir, session_id))
    matches = [
        row
        for row in rows
        if row["event_kind"] == "present" and row.get("unit") == "baseline" and row.get("item") == item
    ]
    return matches[-1] if matches else None


def latest_save_mtime(work_dir: Path) -> "float | None":
    """The latest modification time among `work_dir`'s own files, excluding `target/` (cargo's
    build cache — touched by every `cargo build`/`check`/`test` run the item bank's own tooling
    rules allow, which would otherwise read as a "save" the instant the learner merely re-ran a
    check) and `tests/` (the bank's own test files: unedited by the learner before grading, and
    `grade_item` copies a held-out one in only after this is read). Covers `src/lib.rs` items and
    `prediction.txt` items (top-level, not under `src/`) alike, unlike probe's own
    `latest_mtime_under`, which only ever looks under a problem's `src/`."""
    if not work_dir.is_dir():
        return None
    excluded = {"target", "tests"}
    mtimes = [
        path.stat().st_mtime
        for path in work_dir.rglob("*")
        if path.is_file() and excluded.isdisjoint(path.relative_to(work_dir).parts)
    ]
    return max(mtimes) if mtimes else None


def run_grade(
    subject_dir: Path,
    item: str,
    session_id: str,
    cap_minutes: float = CAP_MINUTES_DEFAULT,
    now: "datetime | None" = None,
) -> dict[str, str]:
    """Grade the baseline item `gym train baseline stage` staged for `item`/`session_id`, against
    its key, and log one `probe-item` event (`which=baseline`). Refuses outright if no matching
    `present` event exists, or if nothing was staged. Never opens or prints `key/`."""
    one_item_dir = item_dir(subject_dir, item)
    start_row = latest_present(subject_dir, session_id, item)
    if start_row is None:
        sys.exit(f"refused, no present event for baseline item {item!r} in session {session_id}")
    started = datetime.strptime(start_row["timestamp"], TIMESTAMP_FORMAT)
    total_minutes = max(0.0, ((now or datetime.now()) - started).total_seconds() / 60)
    over_cap = "yes" if total_minutes > cap_minutes else "no"
    work_dir = work_dir_for(subject_dir, session_id, item)
    if not work_dir.is_dir():
        sys.exit(f"refused, nothing staged for baseline item {item!r} in session {session_id}")
    item_minutes = minutes_since(started, latest_save_mtime(work_dir))
    passed, fraction = grade_item(work_dir, one_item_dir / "key")
    fields = {
        "unit": "baseline",
        "which": "baseline",
        "problem": item,
        "result": "pass" if passed else "fail",
        "minutes": f"{item_minutes:.2f}",
        "total_minutes": f"{total_minutes:.2f}",
        "over_cap": over_cap,
        "fraction": f"{fraction:.4f}",
    }
    line = append_event(subject_dir, session_id, "tool:probe", "probe-item", fields)
    print(f"{item}: {fields['result']} ({fraction:.2f})")
    return {"line": line, **fields}
