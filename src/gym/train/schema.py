r"""Schema for gym train's per-session event lines.

Line shape: `YYYY-MM-DDTHH:MM | actor | kind | key=value key="value with spaces" ...`. `actor` is
one of `ACTORS`; `kind` is one of `KINDS`, each mapping its required field names to a validator of
the raw string value. A value holding a space (or a quote, or a backslash) is written
double-quoted, its own `"` and `\` escaped (`quote_value`); reading a line back
(`parse_fields`) tokenizes with `shlex.split`, which understands that quoting, so a field's shape
is recovered exactly, with no need to know which fields a given kind admits before parsing — kind
awareness is purely `validate_fields`'s job, not the parser's (team lead ruling, 2026-09-30, one
correction after an earlier version of this parser resolved the same ambiguity by continuation
instead of quoting). Team lead ruling (2026-09-30): any kind may also carry an optional `request`
field (same `hint|answer|explain|none` values as the dedicated `request` kind), so a hint or answer
can be logged as one line instead of two; `probe-item` may also carry an optional `fraction` field,
a number from 0 to 1.

A line is refused, with the reason, on an unknown kind or actor, a missing required field, or a bad
value. A backward-clock refusal is the caller's job (`gym.train.events.append_event`), since it
needs the file's last line, not just the line itself.
"""
from __future__ import annotations

import re
import shlex
from datetime import date
from typing import Callable

# The clock stamp every event *line* carries (the first `|`-delimited column), e.g.
# `2026-09-30T16:36 | trainer | ...`. Colon, matching the rest of gym's own trace-line convention
# (`gym.records.event`) — this is text inside a file, never a path component, so a colon is fine.
TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M"

# The shape of a *session id* — used to name `sessions/<session_id>/` and, via
# `gym.train.probe.session_path_segment`, the probe's staging directory under `work/`. Hyphen, not
# colon: a colon in a path breaks `cargo test` on macOS, which puts the crate's manifest path in
# `$DYLD_FALLBACK_LIBRARY_PATH`, itself colon-separated — a real dry run hit exactly this. Team
# lead ruling (2026-09-30): `gym train open` refuses any id not shaped this way, defaulting to it
# from the clock.
SESSION_ID_FORMAT = "%Y-%m-%dT%H-%M"

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


def float_in(low: float, high: float) -> Validator:
    def check(value: str) -> "str | None":
        try:
            parsed = float(value)
        except ValueError:
            return "not a number"
        return None if low <= parsed <= high else f"outside [{low}, {high}]"

    return check


def iso_date(value: str) -> "str | None":
    try:
        date.fromisoformat(value)
    except ValueError:
        return "not YYYY-MM-DD"
    return None


def csv_list(value: str) -> "str | None":
    """A comma-joined list of nonempty names, e.g. `p1-board,p2-summary,p3-shift` — `probe-start`'s
    own `problems` field."""
    parts = value.split(",")
    if not value or any(not part.strip() for part in parts):
        return "not a comma-separated list of names"
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
    # Team lead ruling (2026-09-30): `gym train probe` split into `stage`/`grade`, no interactive
    # wait; `stage` logs this event instead of presenting item text — the time it stamps is what
    # `grade` measures elapsed minutes from, and `problems` is the ordered list `grade` re-grades.
    "probe-start": {
        "unit": nonempty,
        "which": enum("immediate", "delayed"),
        "problems": csv_list,
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

# A field any kind may optionally carry beyond its own required set, validated when present. Team
# lead ruling (2026-09-30): a hint or answer turn can carry the learner's own ask on the same
# line, instead of a separate `request` event first.
GLOBAL_OPTIONAL_FIELDS: dict[str, Validator] = {
    "request": enum("hint", "answer", "explain", "none"),
}

# An optional field recognized for one specific kind only.
KIND_OPTIONAL_FIELDS: dict[str, dict[str, Validator]] = {
    "probe-item": {"fraction": float_in(0.0, 1.0)},
    # Team lead ruling (2026-09-30): `close` may optionally carry `probe_minutes`, a non-negative
    # number — the one old `sessions.csv` column (`record_schema.py`'s `probe_minutes`,
    # `float_at_least(0)` there too) this schema gives a home to.
    "close": {"probe_minutes": float_at_least(0)},
}


# Characters that are unsafe for `shlex.split` to see unquoted in a value: whitespace (splits the
# token), a quote character (either one opens an unterminated quoted region on its own — verified:
# an unquoted `'` or `"` anywhere in a token makes `shlex.split` raise "No closing quotation" even
# with no matching space), and a backslash (an escape character even outside quotes in POSIX mode —
# verified: an unquoted `\` silently vanishes, along with whatever followed it).
NEEDS_QUOTING = re.compile(r'[\s"\'\\]')


def quote_value(value: str) -> str:
    r"""`value` as a stored line's own token: bare when safe, `"escaped"` when it holds any of
    `NEEDS_QUOTING`'s characters — only `"` and `\` need escaping inside the quotes; a `'` or a
    space is inert there. Team lead ruling (2026-09-30): a value that holds spaces is written
    `key="value"`, double-quoted, its own quotes escaped."""
    if not NEEDS_QUOTING.search(value):
        return value
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def parse_fields(rest: str) -> dict[str, str]:
    """Parse one stored line's `rest` (everything after `kind |`) back into a fields dict.
    `shlex.split` does the tokenizing — it already understands the quoting `quote_value` writes, so
    `"unit=u1 item=x principle=\\"move semantics\\""` → `{"unit": "u1", "item": "x", "principle":
    "move semantics"}` with no need to know which fields `kind` admits first; `validate_fields` is
    where kind-specific knowledge belongs, not here. A duplicate field, or a token with no `=`, is
    refused outright — quoting resolves the ambiguity an earlier version of this parser had to
    paper over with continuation, so both cases are reliable now.
    """
    try:
        tokens = shlex.split(rest)
    except ValueError as error:
        raise ValueError(f"not shlex-parseable ({error}): {rest!r}") from error
    fields: dict[str, str] = {}
    for token in tokens:
        key, has_equals, value = token.partition("=")
        if not has_equals:
            raise ValueError(f"not 'field=value': {token!r}")
        if not key:
            raise ValueError(f"empty field name: {token!r}")
        if key in fields:
            raise ValueError(f"'{key}' given twice")
        fields[key] = value
    return fields


def validate_fields(kind: str, fields: dict[str, str]) -> "str | None":
    """The reason `fields` fails `kind`'s required set, an optional field's own value check, or an
    unknown field, or `None`. Team lead ruling (2026-09-30): a field name that is neither one of
    `kind`'s required fields nor a recognized optional field (`GLOBAL_OPTIONAL_FIELDS`,
    `KIND_OPTIONAL_FIELDS`) is refused outright — `note` is the one exception, legal free text on
    any kind whether or not that kind requires it. Before this ruling an unrecognized extra field
    was silently tolerated (a real instance: `gym train log ... probe-item ... continuous=0.5`
    wrote a line that round-tripped, `continuous` never having been a field this schema ever
    declared — only `fraction` is `probe-item`'s own optional field)."""
    required = KINDS[kind]
    missing = [name for name in required if name not in fields]
    if missing:
        return f"missing field(s) for {kind}: {', '.join(missing)}"
    for name, check in required.items():
        error = check(fields[name])
        if error:
            return f"{kind}.{name} {error}: {fields[name]!r}"
    optional = {**GLOBAL_OPTIONAL_FIELDS, **KIND_OPTIONAL_FIELDS.get(kind, {})}
    for name, check in optional.items():
        if name in fields and name not in required:
            error = check(fields[name])
            if error:
                return f"{kind}.{name} {error}: {fields[name]!r}"
    known = set(required) | set(optional) | {"note"}
    unknown = sorted(name for name in fields if name not in known)
    if unknown:
        return f"unknown field(s) for {kind}: {', '.join(unknown)}"
    return None
