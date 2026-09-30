"""gym train open: create the session directory, write session.md's heading, log the open event."""
from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

from gym.train.events import all_session_ids, append_event, session_dir, session_md_path
from gym.train.schema import TIMESTAMP_FORMAT


def gap_days(subject_dir: Path, session_id: str) -> "float | None":
    """Days between `session_id` and the previous session's id (lexicographic order equals
    chronological order for this fixed-width timestamp), or `None` when none precedes it."""
    earlier = [sid for sid in all_session_ids(subject_dir) if sid < session_id]
    if not earlier:
        return None
    previous = datetime.strptime(earlier[-1], TIMESTAMP_FORMAT)
    current = datetime.strptime(session_id, TIMESTAMP_FORMAT)
    return (current - previous).total_seconds() / 86400


def open_session(
    subject_dir: Path,
    learner: str,
    trainer_model: str,
    session_id: "str | None" = None,
) -> str:
    session_id = session_id or datetime.now().strftime(TIMESTAMP_FORMAT)
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
