"""Column shapes for the Rust trainer's learner record: five append-only CSVs under `training/rust/record/`.

Files and fields are fable-plan.md § 5. Every row starts with `timestamp` (the clock's stamp,
`YYYY-MM-DDTHH:MM` — never hand-typed, matching the trace-line convention `scripts/event.py` sets).
Two named fields collapse into that one column: sessions' `date` and `start` are one instant, so a
second column would carry the same fact twice (Simplicity Manifesto: don't split what isn't
interleaved with anything else) — a default, unmeasured simplification, not one of the plan's
evidence-grounded rules.

A validator is a function of the raw string cell to an error message, or `None` when the cell is
good. `FILES[name]` is that file's columns in header order.
"""
from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from typing import Callable

Validator = Callable[[str], "str | None"]

ROOT = Path(__file__).resolve().parents[2]
RECORD_DIR = ROOT / "training/rust/record"

TIMESTAMP_FIELD = "timestamp"
TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M"


def file_path(name: str) -> Path:
    return RECORD_DIR / f"{name}.csv"


def timestamp_token(value: str) -> "str | None":
    try:
        datetime.strptime(value, TIMESTAMP_FORMAT)
    except ValueError:
        return f"not {TIMESTAMP_FORMAT}"
    return None


def iso_date(value: str) -> "str | None":
    try:
        date.fromisoformat(value)
    except ValueError:
        return "not YYYY-MM-DD"
    return None


def nonempty(value: str) -> "str | None":
    return None if value.strip() else "empty"


def bool_token(value: str) -> "str | None":
    return None if value in ("true", "false") else "not 'true' or 'false'"


def enum(*values: str) -> Validator:
    def check(value: str) -> "str | None":
        return None if value in values else f"not one of {values}"

    return check


def maybe(check: Validator) -> Validator:
    def wrapped(value: str) -> "str | None":
        return None if value == "" else check(value)

    return wrapped


def int_at_least(minimum: int) -> Validator:
    def check(value: str) -> "str | None":
        try:
            parsed = int(value)
        except ValueError:
            return "not an integer"
        return None if parsed >= minimum else f"below {minimum}"

    return check


def int_in(low: int, high: int) -> Validator:
    def check(value: str) -> "str | None":
        try:
            parsed = int(value)
        except ValueError:
            return "not an integer"
        return None if low <= parsed <= high else f"outside [{low}, {high}]"

    return check


def float_at_least(minimum: float) -> Validator:
    def check(value: str) -> "str | None":
        try:
            parsed = float(value)
        except ValueError:
            return "not a number"
        return None if parsed >= minimum else f"below {minimum}"

    return check


def float_in(low: float, high: float) -> Validator:
    def check(value: str) -> "str | None":
        try:
            parsed = float(value)
        except ValueError:
            return "not a number"
        return None if low <= parsed <= high else f"outside [{low}, {high}]"

    return check


# items.kind, turns.kind: probe-immediate reads isomorph a, probe-delayed reads isomorph b
# (fable-plan.md § 1 T3, § 5 "durability"); turns.kind "answer" is the breach case (§ 6 O13).
FILES: dict[str, dict[str, Validator]] = {
    "sessions": {
        TIMESTAMP_FIELD: timestamp_token,
        "minutes": int_at_least(0),
        "gap_days": float_at_least(0),
        "units": nonempty,  # ';'-joined unit ids covered this session
        "trainer_model": nonempty,  # O6: opus by default; no fixed enum, the owner may raise it
        "probe_minutes": float_at_least(0),
        "assistant_closed": bool_token,  # learner attests; no lock-out exists (§ 5 sessions row)
        "interruptions": int_at_least(0),
    },
    "items": {
        TIMESTAMP_FIELD: timestamp_token,
        "item_id": nonempty,
        "unit": nonempty,
        "kind": enum("baseline", "practice", "probe-immediate", "probe-delayed"),
        "delay_days": float_at_least(0),
        "pass": bool_token,
        "continuous": float_in(0.0, 1.0),
        "minutes": float_at_least(0),
        "attempts": int_at_least(1),
    },
    "turns": {
        TIMESTAMP_FIELD: timestamp_token,
        "session": nonempty,  # the session row's own timestamp
        "n": int_at_least(1),
        "kind": enum("hint-1", "hint-2", "hint-3", "question", "feedback", "instruction", "answer"),
        "item": nonempty,
        "minute": float_at_least(0),
        "request_kind": maybe(enum("hint", "answer", "explain")),  # blank when the trainer initiated
    },
    "confidence": {
        TIMESTAMP_FIELD: timestamp_token,
        "item_id": nonempty,
        "session": nonempty,
        "confidence": int_in(0, 4),  # quarantined; never joined to an axis (N1-r7-04, N1-r7-08, N4-r6-05)
    },
    "queue": {
        TIMESTAMP_FIELD: timestamp_token,
        "kind": enum("delayed_probe", "revisit", "next_unit"),
        "unit": nonempty,
        "due_date": iso_date,
    },
}
