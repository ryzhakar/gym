"""gym train close: append a close block to session.md, in the memento digest shape, and log the
close event.

`## Close — <time>`, then `state`, `open`, `next`, each label padded to 8 columns — the same shape
`gym.records.close_span` writes for memento's own session records, minus the `HEAD` line (train has
no git state to report; the task names only `state`, `open`, `next`).
"""
from __future__ import annotations

from pathlib import Path

from gym.train.events import append_event, events_path, read_events, session_md_path

LABEL_WIDTH = 8


def summarize_state(rows: list[dict[str, str]]) -> str:
    """`state` per the task: a summary of this session's own `probe-item` and `queue` events.
    A row's `event_kind` is the event line's own kind (`probe-item`, `queue`, ...); a `queue`
    row's `kind` field (`delayed_probe`/`revisit`/`next_unit`) is a different thing, read here as
    `row['kind']` only after `event_kind` has already picked out the queue rows."""
    probes = [row for row in rows if row["event_kind"] == "probe-item"]
    queues = [row for row in rows if row["event_kind"] == "queue"]
    parts = []
    if probes:
        passed = sum(1 for row in probes if row["result"] == "pass")
        parts.append(f"{passed}/{len(probes)} probe item(s) passed")
    if queues:
        parts.append("queued " + ", ".join(f"{row['kind']}:{row['unit']}@{row['due']}" for row in queues))
    return "; ".join(parts) if parts else "no probe or queue events this session"


def close_block(state: str, open_items: str, next_step: str, timestamp: str) -> str:
    def field(label: str, value: str) -> str:
        return label.ljust(LABEL_WIDTH) + value

    lines = [f"## Close — {timestamp}", "", field("state", state), field("open", open_items), field("next", next_step)]
    return "\n" + "\n".join(lines) + "\n"


def close_session(
    subject_dir: Path,
    session_id: str,
    minutes: int,
    units: str,
    interruptions: int,
    assistant_closed: str,
    next_step: str,
    probe_minutes: "float | None" = None,
) -> str:
    rows = read_events(events_path(subject_dir, session_id))
    state = summarize_state(rows)
    open_items = "none" if assistant_closed == "yes" and interruptions == 0 else f"interruptions={interruptions} assistant_closed={assistant_closed}"
    fields = {
        "minutes": str(minutes),
        "units": units,
        "interruptions": str(interruptions),
        "assistant_closed": assistant_closed,
    }
    if probe_minutes is not None:
        fields["probe_minutes"] = str(probe_minutes)
    line = append_event(subject_dir, session_id, "manager", "close", fields)
    timestamp = line.split(" | ", 1)[0]
    block = close_block(state, open_items, next_step, timestamp)
    path = session_md_path(subject_dir, session_id)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(block)
    return line
