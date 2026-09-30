"""Schema for gym train's per-session event lines.

Line shape: `YYYY-MM-DDTHH:MM | actor | kind | key=value key=value ...`. `actor` is one of `ACTORS`;
`kind` is one of `KINDS`, each mapping its required field names to a validator of the raw string
value. `note` is the one field allowed to carry free text (including spaces): when present it must
be the last `key=value` token on the line and swallows everything after its own `=` to the end.

A line is refused, with the reason, on an unknown kind or actor, a missing required field, or a bad
value. A backward-clock refusal is the caller's job (`gym.train.events.append_event`), since it
needs the file's last line, not just the line itself.
"""
from __future__ import annotations

from datetime import date
from typing import Callable

TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M"

ACTORS = ("manager", "trainer", "learner", "tool:probe")

Validator = Callable[[str], "str | None"]


def enum(*values: str) -> Validator:
    def check(value: str) -> "str | None":
        return None if value in values else f"not one of {values}"

    return check


def nonempty(value: str) -> "str | None":
    return None if value.strip() else "empty"


def int_at_least(minimum: int) -> Validator:
    def check(value: str) -> "str | None":
        try:
            parsed = int(value)
        except ValueError:
            return "not an integer"
        return None if parsed >= minimum else f"below {minimum}"

    return check


def float_at_least(minimum: float) -> Validator:
    def check(value: str) -> "str | None":
        try:
            parsed = float(value)
        except ValueError:
            return "not a number"
        return None if parsed >= minimum else f"below {minimum}"

    return check


def iso_date(value: str) -> "str | None":
    try:
        date.fromisoformat(value)
    except ValueError:
        return "not YYYY-MM-DD"
    return None


# Every kind's required fields, in the order the task prompt gives them. A kind not listed here is
# unknown. `note` never appears as a required field except for `ladder-gap`, the one kind the
# trainer's own procedure (gym-trainer.md's <respond-to-a-request>) requires a note on.
#
# `start`, `question` and `answer` are additions past the task's original 13, added on the team
# lead's own ruling to match gym-trainer.md's turn kinds: `start` for a unit's opening turn
# (<open-the-session>: "Log the unit's opening as a `start` turn"), `question` for a trainer
# question with no dedicated kind before this, and `answer` for a logged breach of the solution
# ban (<log-every-turn>: "Log a handed-over solution as `answer`; never hide a breach under
# another kind"). A baseline item (no real unit of its own) logs `unit=baseline` — a plain string
# satisfying `nonempty` like any other unit id, needing no schema change of its own.
KINDS: dict[str, dict[str, Validator]] = {
    "open": {
        "learner": nonempty,
        "trainer_model": nonempty,
    },
    "start": {
        "unit": nonempty,
    },
    "present": {
        "unit": nonempty,
        "item": nonempty,
    },
    "question": {
        "unit": nonempty,
        "item": nonempty,
    },
    "answer": {
        "unit": nonempty,
        "item": nonempty,
    },
    "request": {
        "unit": nonempty,
        "item": nonempty,
        "request": enum("hint", "answer", "explain", "none"),
    },
    "hint": {
        "unit": nonempty,
        "item": nonempty,
        "level": enum("1", "2", "3"),
        "source": enum("supplied", "authored"),
    },
    "attempt": {
        "unit": nonempty,
        "item": nonempty,
        "result": enum("pass", "fail", "skip"),
        "minutes": float_at_least(0),
    },
    "build": {
        "unit": nonempty,
        "item": nonempty,
        "result": nonempty,
    },
    "feedback": {
        "unit": nonempty,
        "item": nonempty,
    },
    "instruction": {
        "unit": nonempty,
        "item": nonempty,
        "principle": nonempty,
    },
    "ladder-gap": {
        "unit": nonempty,
        "item": nonempty,
        "note": nonempty,
    },
    "confidence": {
        "unit": nonempty,
        "item": nonempty,
        "value": enum("0", "1", "2", "3", "4"),
    },
    "probe-item": {
        "unit": nonempty,
        "which": enum("immediate", "delayed"),
        "problem": nonempty,
        "result": enum("pass", "fail"),
        "minutes": float_at_least(0),
    },
    "queue": {
        "unit": nonempty,
        "kind": enum("delayed_probe", "revisit", "next_unit"),
        "due": iso_date,
    },
    "close": {
        "minutes": int_at_least(0),
        "units": nonempty,
        "interruptions": int_at_least(0),
        "assistant_closed": enum("yes", "no"),
    },
}


def parse_fields(rest: str) -> dict[str, str]:
    """`"unit=u1 item=x note=free text here"` → `{"unit": "u1", "item": "x", "note": "free text here"}`.
    Every token but the last must be a single `key=value` word; `note`, wherever it starts, absorbs
    every token after it (including embedded `=` signs) as one free-text value — the schema's one
    escape hatch for a value containing spaces.
    """
    tokens = rest.split(" ")
    fields: dict[str, str] = {}
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if "=" not in token:
            raise ValueError(f"not 'field=value': {token!r}")
        key, _, value = token.partition("=")
        if not key:
            raise ValueError(f"empty field name: {token!r}")
        if key in fields:
            raise ValueError(f"'{key}' given twice")
        if key == "note":
            fields[key] = " ".join([value, *tokens[index + 1 :]])
            return fields
        fields[key] = value
        index += 1
    return fields


def validate_fields(kind: str, fields: dict[str, str]) -> "str | None":
    """The reason `fields` fails `kind`'s required set, or `None`. Extra fields beyond a kind's
    required set (an optional `note`, or anything else) are never refused here — only a missing
    required field or a bad value on one that's present."""
    required = KINDS[kind]
    missing = [name for name in required if name not in fields]
    if missing:
        return f"missing field(s) for {kind}: {', '.join(missing)}"
    for name, check in required.items():
        error = check(fields[name])
        if error:
            return f"{kind}.{name} {error}: {fields[name]!r}"
    return None
