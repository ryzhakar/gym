"""Append one row to a named learner-record file, timestamped by the clock.

Usage: `uv run python scripts/train/log.py <sessions|items|turns|confidence|queue> field=value ...`.
Refuses a `timestamp=...` argument — the clock stamps it, never hand-typed (event-lines convention) —
and any row the schema in `record_schema.py` does not admit: an unknown field, a missing field, or a
value the column's shape rejects. Refuses a timestamp older than the file's last row.

`turn --session <id> --n <n> --kind <k> --item <i> --request <hint|answer|explain|none>
[--note "<text>"]` is an alias for `turns` in the trainer's own flag form (rust-trainer.md v0.2
rule 38's literal invocation, `allowlist.md`'s Bash allow pattern) — `kind` accepts `start` and
`present` (v0.2) alongside the v0.1 set, and `ladder-gap` in place of a `feedback` turn whose note
reads `ladder gap: <item> after level <n>` (v0.1 rule 23, promoted in v0.2). `--note` is required
for `--kind ladder-gap` and otherwise omitted entirely — rule 38's own words, "required for
ladder-gap, otherwise absent" — defaulting to blank when left out (`record_schema.ROW_CHECKS`
refuses a non-blank note on any other kind). Any flag value of exactly `none` also maps to the
column's blank string, for a trainer that passes one explicitly instead of omitting it.
`minute` is never a flag: the trainer has no clock (rule 11); this script computes it as the minutes
elapsed since `--session`'s own timestamp.
"""
from __future__ import annotations

import csv
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from record_schema import FILES, ROW_CHECKS, TIMESTAMP_FIELD, TIMESTAMP_FORMAT, file_path  # noqa: E402

TURN_FLAG_COLUMNS = {
    "session": "session",
    "n": "n",
    "kind": "kind",
    "item": "item",
    "request": "request_kind",
    "note": "note",
}


def parse_fields(argv: list[str]) -> dict[str, str]:
    fields: dict[str, str] = {}
    for token in argv:
        if "=" not in token:
            sys.exit(f"refused, not 'field=value': {token}")
        name, _, value = token.partition("=")
        if name in fields:
            sys.exit(f"refused, '{name}' given twice")
        fields[name] = value
    return fields


def parse_turn_flags(argv: list[str]) -> dict[str, str]:
    """`--session id --n 1 --kind hint-1 --item x --request hint --note none` → `turns` columns —
    any value of exactly `none` maps to that column's blank string. Never a `--minute`: `turn_fields`
    computes it."""
    fields: dict[str, str] = {}
    tokens = list(argv)
    while tokens:
        token = tokens.pop(0)
        if not token.startswith("--") or token[2:] not in TURN_FLAG_COLUMNS:
            sys.exit(f"refused, not one of --{'/--'.join(TURN_FLAG_COLUMNS)}: {token}")
        if not tokens:
            sys.exit(f"refused, '{token}' has no value")
        column = TURN_FLAG_COLUMNS[token[2:]]
        value = tokens.pop(0)
        if column in fields:
            sys.exit(f"refused, '{column}' given twice")
        fields[column] = "" if value == "none" else value
    return fields


def turn_fields(argv: list[str]) -> dict[str, str]:
    """`parse_turn_flags` plus `minute`: elapsed minutes since `--session`'s own timestamp, this
    script's clock, never the trainer's (rule 11 — the trainer has no clock). `--note` defaults to
    blank when the trainer omits it entirely (rule 38: "required for ladder-gap, otherwise absent")
    — only `ladder-gap` needs to pass it."""
    fields = parse_turn_flags(argv)
    fields.setdefault("note", "")
    session_id = fields.get("session", "")
    try:
        session_start = datetime.strptime(session_id, TIMESTAMP_FORMAT)
    except ValueError:
        sys.exit(f"refused, --session is not {TIMESTAMP_FORMAT}: {session_id!r}")
    elapsed_minutes = (datetime.now() - session_start).total_seconds() / 60
    if elapsed_minutes < 0:
        sys.exit(f"refused, --session {session_id} is in the future")
    fields["minute"] = f"{elapsed_minutes:.2f}"
    return fields


def build_row(name: str, fields: dict[str, str]) -> dict[str, str]:
    """Fields plus the auto-stamped timestamp, refused if the row does not match `record_schema.FILES[name]`."""
    columns = FILES[name]
    data_columns = [column for column in columns if column != TIMESTAMP_FIELD]
    if TIMESTAMP_FIELD in fields:
        sys.exit(f"refused, '{TIMESTAMP_FIELD}' is hand-typed here; the clock stamps it")
    unknown = set(fields) - set(data_columns)
    if unknown:
        sys.exit(f"refused, unknown field(s) for {name}: {', '.join(sorted(unknown))}")
    missing = set(data_columns) - set(fields)
    if missing:
        sys.exit(f"refused, missing field(s) for {name}: {', '.join(sorted(missing))}")
    row = {TIMESTAMP_FIELD: datetime.now().strftime(TIMESTAMP_FORMAT), **fields}
    for column, check in columns.items():
        error = check(row[column])
        if error:
            sys.exit(f"refused, {name}.{column} {error}: {row[column]!r}")
    for row_check in ROW_CHECKS.get(name, []):
        error = row_check(row)
        if error:
            sys.exit(f"refused, {name} row {error}: {row}")
    return row


def last_row_timestamp(path: Path) -> "str | None":
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    return rows[-1][0] if len(rows) > 1 else None


def append_row(name: str, row: dict[str, str]) -> Path:
    path = file_path(name)
    header = list(FILES[name])
    if not path.is_file():
        sys.exit(f"refused, no such record file: {path}")
    with path.open(encoding="utf-8", newline="") as handle:
        existing_header = next(csv.reader(handle), None)
    if existing_header != header:
        sys.exit(f"refused, {path} header {existing_header} is not the schema's {header}")
    last_timestamp = last_row_timestamp(path)
    if last_timestamp and row[TIMESTAMP_FIELD] < last_timestamp:
        sys.exit(f"refused, the clock reads {row[TIMESTAMP_FIELD]}, before {path}'s last row at {last_timestamp}")
    with path.open("a", encoding="utf-8", newline="") as handle:
        csv.writer(handle).writerow([row[column] for column in header])
    return path


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        sys.exit(__doc__)
    if argv[1] == "turn":
        name, fields = "turns", turn_fields(argv[2:])
    elif argv[1] in FILES:
        name, fields = argv[1], parse_fields(argv[2:])
    else:
        sys.exit(__doc__)
    row = build_row(name, fields)
    path = append_row(name, row)
    print(f"{path}: {row}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
