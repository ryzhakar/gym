"""gym train open: create the session directory, write session.md's heading, log the open event."""
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

from gym.train.events import all_session_ids, append_event, session_dir, session_md_path
from gym.train.schema import SESSION_ID_FORMAT


def validate_session_id(session_id: str) -> None:
    """Team lead ruling (2026-09-30): a session id is shaped `YYYY-MM-DDTHH-MM` — hyphen, not
    colon, since a colon in a path breaks `cargo test` on macOS (`$DYLD_FALLBACK_LIBRARY_PATH`
    uses `:` as its own separator) and a session id names both the session directory and, via
    `gym.train.probe.session_path_segment`, the probe's staging directory. `--id` is refused
    outright on any other shape, rather than let a malformed id become a directory name and only
    surface as a `datetime.strptime` crash later, inside `gap_days` or a subsequent `gym train log`
    call."""
    try:
        datetime.strptime(session_id, SESSION_ID_FORMAT)
    except ValueError:
        sys.exit(f"refused, --id is not {SESSION_ID_FORMAT}: {session_id!r}")


def gap_days(subject_dir: Path, session_id: str) -> "float | None":
    """Days between `session_id` and the previous session's id (lexicographic order equals
    chronological order for this fixed-width timestamp — true regardless of `-` vs `:` as the
    separator, as long as every id uses the same one), or `None` when none precedes it."""
    earlier = [sid for sid in all_session_ids(subject_dir) if sid < session_id]
    if not earlier:
        return None
    previous = datetime.strptime(earlier[-1], SESSION_ID_FORMAT)
    current = datetime.strptime(session_id, SESSION_ID_FORMAT)
    return (current - previous).total_seconds() / 86400


def open_session(
    subject_dir: Path,
    learner: str,
    trainer_model: str,
    session_id: "str | None" = None,
) -> str:
    session_id = session_id or datetime.now().strftime(SESSION_ID_FORMAT)
    validate_session_id(session_id)
    directory = session_dir(subject_dir, session_id)
    if directory.exists():
        sys.exit(f"refused, session already exists: {directory}")
    gap = gap_days(subject_dir, session_id)
    directory.mkdir(parents=True)
    (directory / "events.md").touch()
    gap_text = "none" if gap is None else f"{gap:.2f}"
    heading = "\n".join(
        [
            f"# {session_id}",
            f"subject: {subject_dir.name}",
            f"learner: {learner}",
            f"trainer model: {trainer_model}",
            f"gap_days: {gap_text}",
            "",
        ]
    )
    session_md_path(subject_dir, session_id).write_text(heading, encoding="utf-8")
    append_event(subject_dir, session_id, "manager", "open", {"learner": learner, "trainer_model": trainer_model})
    return session_id
