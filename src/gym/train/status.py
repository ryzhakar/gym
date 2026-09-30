"""gym train status: derive per-unit history, due queue rows, and confidence from every session's
events — nothing is stored separately; this command is the one place that reads across sessions.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from gym.train.events import all_events

TAIL_LINES = 20


def last_attempt_by_unit(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    last: dict[str, dict[str, str]] = {}
    for row in rows:
        if row["event_kind"] == "attempt":
            last[row["unit"]] = row
    return last


def last_probe_by_unit(rows: list[dict[str, str]], which: str) -> dict[str, dict[str, str]]:
    last: dict[str, dict[str, str]] = {}
    for row in rows:
        if row["event_kind"] == "probe-item" and row.get("which") == which:
            last[row["unit"]] = row
    return last


def last_confidence_by_unit(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    last: dict[str, dict[str, str]] = {}
    for row in rows:
        if row["event_kind"] == "confidence":
            last[row["unit"]] = row
    return last


def due_queue_rows(rows: list[dict[str, str]], today: "date | None" = None) -> list[dict[str, str]]:
    """The latest `queue` row per (unit, its own `kind` field), still due today. Per the task: a
    `delayed_probe` row is due once 7 or more days have passed since its own `due` date; a
    `revisit` or `next_unit` row is due once its `due` date has simply passed."""
    today = today or date.today()
    latest: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows:
        if row["event_kind"] == "queue":
            latest[(row["unit"], row["kind"])] = row
    due = []
    for (_unit, kind), row in latest.items():
        days_passed = (today - date.fromisoformat(row["due"])).days
        threshold = 7 if kind == "delayed_probe" else 0
        if days_passed >= threshold:
            due.append(row)
    return due


def build_status(subject_dir: Path, today: "date | None" = None) -> dict:
    rows = all_events(subject_dir)
    return {
        "last_attempt": last_attempt_by_unit(rows),
        "last_probe_immediate": last_probe_by_unit(rows, "immediate"),
        "last_probe_delayed": last_probe_by_unit(rows, "delayed"),
        "last_confidence": last_confidence_by_unit(rows),
        "due_queue": due_queue_rows(rows, today),
        "tail": [f"{row['session']}: {row['raw']}" for row in rows][-TAIL_LINES:],
    }


def format_status(status: dict) -> str:
    lines: list[str] = []
    units = sorted(
        set(status["last_attempt"]) | set(status["last_probe_immediate"]) | set(status["last_probe_delayed"]) | set(status["last_confidence"])
    )
    lines.append("## Units")
    if not units:
        lines.append("(no unit events logged yet)")
    for unit in units:
        attempt = status["last_attempt"].get(unit)
        immediate = status["last_probe_immediate"].get(unit)
        delayed = status["last_probe_delayed"].get(unit)
        confidence = status["last_confidence"].get(unit)
        lines.append(f"- {unit}")
        lines.append(f"  last attempt: {attempt['result'] if attempt else 'none'}")
        lines.append(
            "  last immediate probe: "
            + (f"{immediate['result']} ({immediate['timestamp'][:10]})" if immediate else "none")
        )
        lines.append(
            "  last delayed probe: " + (f"{delayed['result']} ({delayed['timestamp'][:10]})" if delayed else "none")
        )
        lines.append(f"  last confidence: {confidence['value'] if confidence else 'none'}")
    lines.append("")
    lines.append("## Due queue")
    if not status["due_queue"]:
        lines.append("(none due)")
    for row in status["due_queue"]:
        lines.append(f"- {row['kind']} unit={row['unit']} due={row['due']}")
    lines.append("")
    lines.append(f"## Tail (last {TAIL_LINES} events)")
    if not status["tail"]:
        lines.append("(no events logged yet)")
    lines.extend(status["tail"])
    return "\n".join(lines)


def main(subject_dir: Path) -> int:
    print(format_status(build_status(subject_dir)))
    return 0
