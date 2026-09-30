"""gym train log: append one event line to a session after validation.

Usage: `gym train log <subject_dir> <session_id> <actor> <kind> key=value ...`. Thin: parses the
`key=value` arguments and hands them straight to `gym.train.events.append_event`, which does every
refusal check.

Team lead ruling (2026-09-30): each argv token is one `key=value` pair, verbatim, never split on
spaces. A value may itself hold spaces when the shell quotes it — `principle="move semantics"`
arrives as one already-atomic argv item, and this parser never rejoins-then-resplits it (the bug
an earlier version of this module had). Unlike `gym.train.schema.parse_fields`, which reads an
already-stored line back and must resolve a genuine ambiguity there (a continuation token can look
like another `key=value` pair), a CLI argument is never ambiguous this way — the shell already drew
its boundary — so this parser needs none of that machinery.
"""
from __future__ import annotations

import sys
from pathlib import Path

from gym.train.events import append_event


def parse_cli_fields(tokens: list[str]) -> dict[str, str]:
    fields: dict[str, str] = {}
    for token in tokens:
        key, has_equals, value = token.partition("=")
        if not has_equals:
            sys.exit(f"refused, not 'field=value': {token!r}")
        if not key:
            sys.exit(f"refused, empty field name: {token!r}")
        if key in fields:
            sys.exit(f"refused, '{key}' given twice")
        fields[key] = value
    return fields


def log_event(subject_dir: Path, session_id: str, actor: str, kind: str, tokens: list[str]) -> str:
    fields = parse_cli_fields(tokens)
    return append_event(subject_dir, session_id, actor, kind, fields)
