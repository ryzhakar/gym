"""Event-file I/O for gym train: one `events.md` per session directory, one line per event.

Layout: `<subject_dir>/sessions/<session_id>/events.md` and `session.md`, `session_id` the
session's own `YYYY-MM-DDTHH:MM` stamp (`gym train open`'s own output). A line is refused, with
the reason and exit 1, on an unknown kind or actor, a missing required field, a bad value, or a
time before the file's last line — the same four cases the task names.
"""
from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path

from gym.train.schema import ACTORS, KINDS, TIMESTAMP_FORMAT, parse_fields, quote_value, validate_fields

LINE_SHAPE = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}) \| (?P<actor>[\w:.-]+) \| (?P<kind>[\w-]+) \| (?P<rest>\S.*)$"
)


def session_dir(subject_dir: Path, session_id: str) -> Path:
    return subject_dir / "sessions" / session_id


def events_path(subject_dir: Path, session_id: str) -> Path:
    return session_dir(subject_dir, session_id) / "events.md"


def session_md_path(subject_dir: Path, session_id: str) -> Path:
    return session_dir(subject_dir, session_id) / "session.md"


def parse_line(line: str) -> tuple[str, str, str, dict[str, str]]:
    """One raw line to `(timestamp, actor, kind, fields)`. Raises `ValueError` with the reason on
    any of the four refusal cases except the clock check, which needs file context. Field parsing
    (`gym.train.schema.parse_fields`) uses `shlex.split`, so a free-text field's quoted value
    (`note`, `principle`, ...) survives holding spaces regardless of where it falls on the line."""
    match = LINE_SHAPE.match(line)
    if not match:
        raise ValueError(f"not 'timestamp | actor | kind | key=value ...': {line!r}")
    actor, kind = match["actor"], match["kind"]
    if actor not in ACTORS:
        raise ValueError(f"unknown actor: {actor!r}")
    if kind not in KINDS:
        raise ValueError(f"unknown kind: {kind!r}")
    fields = parse_fields(match["rest"])
    error = validate_fields(kind, fields)
    if error:
        raise ValueError(error)
    return match["timestamp"], actor, kind, fields


def build_line(timestamp: str, actor: str, kind: str, fields: dict[str, str]) -> str:
    if actor not in ACTORS:
        raise ValueError(f"unknown actor: {actor!r}")
    if kind not in KINDS:
        raise ValueError(f"unknown kind: {kind!r}")
    error = validate_fields(kind, fields)
    if error:
        raise ValueError(error)
    rest = " ".join(f"{key}={quote_value(value)}" for key, value in fields.items())
    return f"{timestamp} | {actor} | {kind} | {rest}"


def last_timestamp(path: Path) -> "str | None":
    if not path.is_file():
        return None
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return lines[-1][:16] if lines else None


def append_event(
    subject_dir: Path,
    session_id: str,
    actor: str,
    kind: str,
    fields: dict[str, str],
    now: "datetime | None" = None,
) -> str:
    """Validate, stamp with the clock (or `now`, for tests), and append one line to the session's
    `events.md`. Refuses, with exit 1, on a missing session directory or any of the four schema
    refusal cases; returns the line actually written."""
    path = events_path(subject_dir, session_id)
    if not path.parent.is_dir():
        sys.exit(f"refused, no such session: {path.parent}")
    timestamp = (now or datetime.now()).strftime(TIMESTAMP_FORMAT)
    try:
        line = build_line(timestamp, actor, kind, fields)
    except ValueError as error:
        sys.exit(f"refused, {error}")
    previous = last_timestamp(path)
    if previous is not None and timestamp < previous:
        sys.exit(f"refused, the clock reads {timestamp}, before {path}'s last line at {previous}")
    with path.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return line


def read_events(path: Path) -> list[dict[str, str]]:
    """Every line in one session's `events.md`, each as
    `{'timestamp','actor','event_kind','raw',**fields}`. The event's own kind is keyed
    `event_kind`, not `kind` — the `queue` kind's own required field is itself named `kind`
    (`delayed_probe|revisit|next_unit`), and merging `**fields` after a plain `kind` key would let
    that field silently overwrite the event kind. A line the schema would refuse is skipped here —
    `gym train check` is what reports it."""
    rows: list[dict[str, str]] = []
    if not path.is_file():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            timestamp, actor, kind, fields = parse_line(line)
        except ValueError:
            continue
        rows.append({"timestamp": timestamp, "actor": actor, "event_kind": kind, "raw": line, **fields})
    return rows


def all_session_ids(subject_dir: Path) -> list[str]:
    sessions = subject_dir / "sessions"
    if not sessions.is_dir():
        return []
    return sorted(path.name for path in sessions.iterdir() if path.is_dir())


def all_events(subject_dir: Path) -> list[dict[str, str]]:
    """Every parsed event across every session, sessions oldest first, each row tagged with its
    own `session` id."""
    rows: list[dict[str, str]] = []
    for session_id in all_session_ids(subject_dir):
        for row in read_events(events_path(subject_dir, session_id)):
            rows.append({"session": session_id, **row})
    return rows
