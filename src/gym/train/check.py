"""gym train check: lint every session's events.md against the schema, and every session.md for
its heading and, once the session logged a close event, a close block.

Usage: `gym train check <subject_dir>`. One line per finding; exits 1 on any FAIL.
"""
from __future__ import annotations

from pathlib import Path

from gym.train.events import LINE_SHAPE, all_session_ids, events_path, session_md_path
from gym.train.schema import ACTORS, KINDS, parse_fields, validate_fields


def check_events_file(path: Path) -> list[str]:
    findings: list[str] = []
    if not path.is_file():
        findings.append(f"FAIL  {path}  file does not exist")
        return findings
    previous = ""
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        where = f"{path}:{number}"
        match = LINE_SHAPE.match(line)
        if not match:
            findings.append(f"FAIL  {where}  not 'timestamp | actor | kind | key=value ...': {line!r}")
            continue
        timestamp, actor, kind = match["timestamp"], match["actor"], match["kind"]
        if actor not in ACTORS:
            findings.append(f"FAIL  {where}  unknown actor: {actor!r}")
        if kind not in KINDS:
            findings.append(f"FAIL  {where}  unknown kind: {kind!r}")
        else:
            try:
                fields = parse_fields(match["rest"])
            except ValueError as error:
                findings.append(f"FAIL  {where}  {error}")
            else:
                error = validate_fields(kind, fields)
                if error:
                    findings.append(f"FAIL  {where}  {error}")
        if timestamp < previous:
            findings.append(f"FAIL  {where}  time {timestamp} goes back from {previous}")
        previous = max(previous, timestamp)
    return findings


def check_session_md(subject_dir: Path, session_id: str, closed: bool) -> list[str]:
    findings: list[str] = []
    path = session_md_path(subject_dir, session_id)
    if not path.is_file():
        findings.append(f"FAIL  {path}  no session.md")
        return findings
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != f"# {session_id}":
        findings.append(f"FAIL  {path}:1  no heading '# {session_id}'")
    if closed and "## Close" not in path.read_text(encoding="utf-8"):
        findings.append(f"FAIL  {path}  session logged a close event but session.md has no close block")
    return findings


def check(subject_dir: Path) -> list[str]:
    findings: list[str] = []
    for session_id in all_session_ids(subject_dir):
        path = events_path(subject_dir, session_id)
        findings.extend(check_events_file(path))
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        closed = any(" | close | " in line for line in text.splitlines())
        findings.extend(check_session_md(subject_dir, session_id, closed))
    return findings


def main(subject_dir: Path) -> int:
    findings = check(subject_dir)
    print(f"train: {len(findings)} FAIL")
    for line in findings:
        print(line)
    return 1 if findings else 0
