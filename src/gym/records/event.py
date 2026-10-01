"""Append one event to a span's trace, stamped by the clock and checked against the schema.

Usage: `gym records event [--span <suffix>] <actor> <kind> <what>`.
`self span-event "open; ..."` starts a trace file dated today; every other event goes to the newest trace.
Without `--span` the trace is the shared `events.md`; with it, the span's own `events-<suffix>.md`.
"""

from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path

from gym.records.check_records import ORCHESTRATION, load_schema, trace_line_shape

SPAN_SHAPE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")


def is_span_opening(kind: str, what: str) -> bool:
    return kind == "span-event" and what.startswith("open")


def trace_name(span: str | None) -> str:
    """The trace's file name: the shared `events.md`, or `events-<span>.md` for a span keeping its own records."""
    if span is None:
        return "events.md"
    if not SPAN_SHAPE.fullmatch(span):
        sys.exit(f"refused, span {span!r} does not match {SPAN_SHAPE.pattern}: lowercase letters and digits, joined by single hyphens")
    return f"events-{span}.md"


def current_trace(opening: bool, span: str | None = None) -> Path:
    """The trace a span writes to: named by the date the span opened."""
    name = trace_name(span)
    if opening:
        today = ORCHESTRATION / "history" / datetime.now().strftime("%Y-%m-%d")
        today.mkdir(parents=True, exist_ok=True)
        return today / name
    traces = sorted(ORCHESTRATION.glob(f"history/*/{name}"))
    if not traces:
        if span is None:
            sys.exit("no trace exists; open a span first: event.py self span-event 'open; ...'")
        sys.exit(f"no trace {name} exists; open the span first: gym records event --span {span} self span-event 'open; ...'")
    return traces[-1]


def append_event(actor: str, kind: str, what: str, span: str | None = None) -> tuple[Path, str]:
    line = f"{datetime.now().strftime('%Y-%m-%dT%H:%M')} | {actor} | {kind} | {what}"
    if not trace_line_shape(load_schema()).match(line):
        sys.exit(f"refused, not a trace line the schema admits: {line}")
    trace = current_trace(is_span_opening(kind, what), span)
    lines = trace.read_text(encoding="utf-8").splitlines() if trace.exists() else []
    if lines and lines[-1][:16] > line[:16]:
        sys.exit(f"refused: the clock reads {line[:16]}, before the trace's last line at {lines[-1][:16]}")
    with trace.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return trace, line


def main(argv: list[str]) -> int:
    if len(argv) < 4:
        sys.exit(__doc__)
    trace, line = append_event(argv[1], argv[2], " ".join(argv[3:]))
    print(f"{trace}: {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
