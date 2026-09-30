"""gym train log: append one event line to a session after validation.

Usage: `gym train log <subject_dir> <session_id> <actor> <kind> key=value ...`. Thin: parses the
`key=value` tokens and hands them straight to `gym.train.events.append_event`, which does every
refusal check.
"""
from __future__ import annotations

import sys
from pathlib import Path

from gym.train.events import append_event
from gym.train.schema import parse_fields


def log_event(subject_dir: Path, session_id: str, actor: str, kind: str, tokens: list[str]) -> str:
    try:
        fields = parse_fields(" ".join(tokens))
    except ValueError as error:
        sys.exit(f"refused, {error}")
    return append_event(subject_dir, session_id, actor, kind, fields)
