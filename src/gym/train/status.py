"""gym train status: derive per-unit history, due queue rows, and confidence from every session's
events — nothing is stored separately; this command is the one place that reads across sessions.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from gym.train.events import all_events

TAIL_LINES = 20

IMMEDIATE_SIDE = "probe-a"
DELAYED_SIDE = "probe-b"

# The event kinds that consume a queue row, by the row's own `kind`: a later event of the row's unit
# that does the thing the row asked for. `delayed_probe` is consumed only by a `probe-item` of the
# delayed side, since a `probe-item` of the immediate side is not the delayed probe.
QUEUE_CONSUMER_KINDS = {
    "next_unit": ("start", "attempt", "probe-item"),
    "revisit": ("start", "attempt"),
    "delayed_probe": ("probe-item",),
}


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


def other_probes_by_unit(rows: list[dict[str, str]]) -> dict[str, dict[str, dict[str, str]]]:
    """Every unit's last `probe-item` row for each side beyond `probe-a`/`probe-b` — a unit
    carrying a third probe side (`probe-c`, a repeat of the unit; team lead ruling, 2026-09-30) or
    any later one of the same shape — keyed by that side's own literal name."""
    last: dict[str, dict[str, dict[str, str]]] = {}
    for row in rows:
        if row["event_kind"] != "probe-item":
            continue
        side = row.get("which")
        if side in ("probe-a", "probe-b"):
            continue
        last.setdefault(row["unit"], {})[side] = row
    return last


def last_confidence_by_unit(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    last: dict[str, dict[str, str]] = {}
    for row in rows:
        if row["event_kind"] == "confidence":
            last[row["unit"]] = row
    return last


def consumes(queue_row: dict[str, str], row: dict[str, str]) -> bool:
    """Whether `row` is an event of the queue row's own unit that does what the queue row asked for
    (`QUEUE_CONSUMER_KINDS`) and is timestamped strictly after the queue row — event stamps have
    minute precision, so an event in the queue row's own minute is not later."""
    if row["event_kind"] not in QUEUE_CONSUMER_KINDS[queue_row["kind"]]:
        return False
    if row.get("unit") != queue_row["unit"]:
        return False
    if queue_row["kind"] == "delayed_probe" and row.get("which") != DELAYED_SIDE:
        return False
    return row["timestamp"] > queue_row["timestamp"]


def due_queue_rows(rows: list[dict[str, str]], today: "date | None" = None) -> list[dict[str, str]]:
    """The latest `queue` row per (unit, its own `kind` field), still due today and not yet
    consumed. A row of any kind is due once its own `due` date has been reached: a `delayed_probe`
    row's `due` is already the date the probe falls due (the trainer sets it a week after the
    immediate probe), so no further wait is added. A row stops reading due once a later event, in
    any session, consumes it (`consumes`): a `start`, `attempt` or `probe-item` of its unit for
    `next_unit`, a `start` or `attempt` for `revisit`, a `probe-item` of the delayed side for
    `delayed_probe`."""
    today = today or date.today()
    latest: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows:
        if row["event_kind"] == "queue":
            latest[(row["unit"], row["kind"])] = row
    return [
        row
        for row in latest.values()
        if date.fromisoformat(row["due"]) <= today and not any(consumes(row, other) for other in rows)
    ]


def build_status(subject_dir: Path, today: "date | None" = None) -> dict:
    rows = all_events(subject_dir)
    return {
        "last_attempt": last_attempt_by_unit(rows),
        "last_probe_immediate": last_probe_by_unit(rows, IMMEDIATE_SIDE),
        "last_probe_delayed": last_probe_by_unit(rows, DELAYED_SIDE),
        "other_probes": other_probes_by_unit(rows),
        "last_confidence": last_confidence_by_unit(rows),
        "due_queue": due_queue_rows(rows, today),
        "tail": [f"{row['session']}: {row['raw']}" for row in rows][-TAIL_LINES:],
    }


def _table(headers: list[str], rows: list[list[str]]) -> list[str]:
    """Left-aligned columns, two spaces apart, each column sized to its widest cell."""
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    def fmt(cells: list[str]) -> str:
        return "  ".join(cell.ljust(widths[i]) for i, cell in enumerate(cells)).rstrip()

    return [fmt(headers), *(fmt(row) for row in rows)]


def format_status(status: dict) -> str:
    lines: list[str] = []
    units = sorted(
        set(status["last_attempt"])
        | set(status["last_probe_immediate"])
        | set(status["last_probe_delayed"])
        | set(status["other_probes"])
        | set(status["last_confidence"])
    )
    lines.append("## Units")
    if not units:
        lines.append("(no unit events logged yet)")
    else:
        headers = ["UNIT", "ATTEMPT", "IMMEDIATE PROBE", "DELAYED PROBE", "CONFIDENCE", "OTHER PROBES"]
        rows = []
        for unit in units:
            attempt = status["last_attempt"].get(unit)
            immediate = status["last_probe_immediate"].get(unit)
            delayed = status["last_probe_delayed"].get(unit)
            other = status["other_probes"].get(unit, {})
            confidence = status["last_confidence"].get(unit)
            other_cell = "; ".join(
                f"{side}: {other[side]['result']} ({other[side]['timestamp'][:10]})" for side in sorted(other)
            )
            rows.append([
                unit,
                attempt["result"] if attempt else "none",
                f"{immediate['result']} ({immediate['timestamp'][:10]})" if immediate else "none",
                f"{delayed['result']} ({delayed['timestamp'][:10]})" if delayed else "none",
                confidence["value"] if confidence else "none",
                other_cell or "none",
            ])
        lines.extend(_table(headers, rows))
    lines.append("")
    lines.append("## Due queue")
    if not status["due_queue"]:
        lines.append("(none due)")
    else:
        rows = [[row["kind"], row["unit"], row["due"]] for row in status["due_queue"]]
        lines.extend(_table(["KIND", "UNIT", "DUE"], rows))
    lines.append("")
    lines.append(f"## Tail (last {TAIL_LINES} events)")
    if not status["tail"]:
        lines.append("(no events logged yet)")
    lines.extend(status["tail"])
    return "\n".join(lines)


def main(subject_dir: Path) -> int:
    print(format_status(build_status(subject_dir)))
    return 0
