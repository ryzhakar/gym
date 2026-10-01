"""gym train practice: grade a practice item's learner folder against its held-out tests.

Layout (`training/rust/items/README.md` §Layout and §Grading), read from the bank itself:

- the item: `<subject_dir>/items/<unit>/<item>/`, `<item>` one of `attempt`, `reuse-N`, `unshown`;
- its held-out tests: `<subject_dir>/items/<unit>/key/<item>/tests/` — `visible.rs` unchanged, plus
  `heldout.rs` where the item has one, plus `structure.rs` where its spec names a structural rule;
- the learner's folder: `<subject_dir>/work/<session, path-safe>/<unit>/<item>/`, the same shape
  `gym train probe stage` uses for a probe's problems.

`grade` copies the learner's folder to a scratch directory, replaces that copy's `tests/` with the
key's (the README's rule: the locked files are always the key's, so editing a test in the learner's
folder changes nothing, and a test file the learner added is not graded), runs `cargo test` there,
and logs one `grade` event by `tool:practice`. The learner's folder is only read: no held-out file
is copied into it, and no `target/` or `Cargo.lock` appears in it. `key/` is only read, never
printed; the command prints one line, `<item>: pass|fail (<fraction>)`, and cargo's own output is
captured, never shown, since a failing held-out test names itself and its values there.

Not graded here: the learner's `Cargo.toml` and any file outside `tests/` come from the learner's
folder as they stand, as `gym train baseline grade` and `probe grade` take them.
"""
from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

from gym.train.events import append_event, events_path
from gym.train.probe import run_cargo_test, session_path_segment


def item_dir(unit_dir: Path, item: str) -> Path:
    """`unit_dir/<item>`, refusing anything but one plain directory name that exists and is not
    `key` — an `item` such as `../x` or `key` would otherwise reach outside the item or into the key."""
    if not item or Path(item).name != item or item in (".", "..", "key"):
        sys.exit(f"refused, not one practice item directory name: {item!r}")
    target = unit_dir / item
    if not target.is_dir():
        sys.exit(f"refused, no such practice item: {target}")
    return target


def key_tests_dir(unit_dir: Path, item: str) -> Path:
    """The item's held-out tests directory under `key/`, required to hold at least one file. Its
    files are copied into the scratch crate by `scratch_copy` and never read, listed or printed."""
    target = unit_dir / "key" / item / "tests"
    if not target.is_dir() or not any(path.is_file() for path in target.rglob("*")):
        sys.exit(f"refused, no held-out tests for {item!r} under this unit's key")
    return target


def learner_dir(subject_dir: Path, session_id: str, unit: str, item: str) -> Path:
    return subject_dir / "work" / session_path_segment(session_id) / unit / item


def scratch_copy(learner_folder: Path, key_tests: Path, scratch_root: Path) -> Path:
    """Copy `learner_folder` to `scratch_root/<its name>`, minus its `target/`, then make that copy's
    `tests/` the key's exactly. Returns the scratch crate directory."""
    crate = scratch_root / learner_folder.name
    shutil.copytree(learner_folder, crate, ignore=shutil.ignore_patterns("target"))
    shutil.rmtree(crate / "tests", ignore_errors=True)
    shutil.copytree(key_tests, crate / "tests")
    return crate


def run_grade(subject_dir: Path, unit_dir: Path, item: str, session_id: str) -> dict[str, str]:
    """Grade the learner's folder for `item` in `session_id` against the unit's key, log one `grade`
    event, print one result line. Refuses, logging nothing, on an item that is not a plain directory
    name of the unit, a key with no tests, an unopened session, or a missing learner folder."""
    unit = unit_dir.name
    item_dir(unit_dir, item)
    key_tests = key_tests_dir(unit_dir, item)
    if not events_path(subject_dir, session_id).parent.is_dir():
        sys.exit(f"refused, no such session: {events_path(subject_dir, session_id).parent}")
    folder = learner_dir(subject_dir, session_id, unit, item)
    if not folder.is_dir():
        sys.exit(f"refused, nothing in the learner's folder for {item!r} in session {session_id}: {folder}")
    with tempfile.TemporaryDirectory(prefix="gym-practice-") as scratch:
        passed, fraction = run_cargo_test(scratch_copy(folder, key_tests, Path(scratch)))
    fields = {"unit": unit, "item": item, "result": "pass" if passed else "fail", "fraction": f"{fraction:.4f}"}
    line = append_event(subject_dir, session_id, "tool:practice", "grade", fields)
    print(f"{item}: {fields['result']} ({fraction:.2f})")
    return {"line": line, **fields}
