"""records sub-app: absorbs scripts/check_records.py, event.py, close_span.py."""

from __future__ import annotations

import typer

from gym.records import check_records as _check_records
from gym.records import close_span as _close_span
from gym.records.event import append_event

app = typer.Typer(help="Records: schema checks, event lines, span closes.")

SPAN_HELP = "Suffix of this span's own files: events-<span>.md, session-<span>.md; omitted means the shared pair"


@app.command("check")
def check() -> None:
    """Check gym's records against the shapes and rules `.claude/memento.yaml` declares."""
    raise typer.Exit(code=_check_records.main())


@app.command("event")
def event(
    actor: str = typer.Argument(..., help="Who this event happened to: owner, self, agent:<name>, or tool:<name>"),
    kind: str = typer.Argument(..., help="Event kind the schema admits, e.g. decision, discovery, commitment"),
    what: list[str] = typer.Argument(..., help="The event's text; joined with spaces into one line"),
    span: str | None = typer.Option(None, "--span", help=SPAN_HELP),
) -> None:
    """Append one event to the current span's trace, stamped by the clock and checked against the schema."""
    trace, line = append_event(actor, kind, " ".join(what), span=span)
    typer.echo(f"{trace}: {line}")


@app.command("close")
def close(
    state: str = typer.Option(..., "--state", help="At most 3 lines: the state the span leaves behind"),
    open_items: str = typer.Option(..., "--open", help="Waits, tripwires, or delegations still open; or 'none'"),
    next_step: str = typer.Option(..., "--next", help="The first step for whoever picks this up next"),
    span: str | None = typer.Option(None, "--span", help=SPAN_HELP),
) -> None:
    """Close the current span: append its close block to the session record and a span-event to the trace."""
    raise typer.Exit(code=_close_span.run(state, open_items, next_step, span=span))
