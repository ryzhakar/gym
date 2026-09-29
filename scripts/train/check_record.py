"""Validate every file of the Rust trainer's learner record against `record_schema.py`.

Usage: `uv run python scripts/train/check_record.py`. One line per finding; exit 1 on any FAIL.
Checks: the header matches the schema; every cell passes its column's validator; every row passes
its file's whole-row rules, if any (`record_schema.ROW_CHECKS`); timestamps never go backward
within a file.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from record_schema import FILES, ROW_CHECKS, TIMESTAMP_FIELD, file_path  # noqa: E402


def check_file(name: str) -> list[str]:
    path = file_path(name)
    columns = FILES[name]
    header = list(columns)
    if not path.is_file():
        return [f"FAIL  {path}  file does not exist"]
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    if not rows or rows[0] != header:
        got = rows[0] if rows else []
        return [f"FAIL  {path}:1  header {got} is not the schema's {header}"]
    findings: list[str] = []
    previous_timestamp = ""
    for number, values in enumerate(rows[1:], start=2):
        where = f"{path}:{number}"
        if len(values) != len(header):
            findings.append(f"FAIL  {where}  {len(values)} value(s), header has {len(header)}")
            continue
        record = dict(zip(header, values))
        for column, check in columns.items():
            error = check(record[column])
            if error:
                findings.append(f"FAIL  {where}  {name}.{column} {error}: {record[column]!r}")
        for row_check in ROW_CHECKS.get(name, []):
            error = row_check(record)
            if error:
                findings.append(f"FAIL  {where}  {name} row {error}: {record}")
        timestamp = record[TIMESTAMP_FIELD]
        if timestamp < previous_timestamp:
            findings.append(f"FAIL  {where}  time {timestamp} goes back from {previous_timestamp}")
        previous_timestamp = max(previous_timestamp, timestamp)
    return findings


def main() -> int:
    findings = [line for name in FILES for line in check_file(name)]
    for line in findings:
        print(line)
    print(f"record: {len(findings)} FAIL")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
