"""records sub-app: absorbs scripts/check_records.py, event.py, close_span.py."""

from __future__ import annotations

import typer

from gym.records import check_records as _check_records
from gym.records import close_span as _close_span
from gym.records.event import append_event

app = typer.Typer(help="Records: schema checks, event lines, span closes.")


@app.command("check")
def check() -> None:
    """Check gym's records against the shapes and rules `.claude/memento.yaml` declares."""
    raise typer.Exit(code=_check_records.main())


@app.command("event")
def event(
    actor: str = typer.Argument(...),
    kind: str = typer.Argument(...),
    what: list[str] = typer.Argument(...),
) -> None:
    """Append one event to the current span's trace, stamped by the clock and checked against the schema."""
    trace, line = append_event(actor, kind, " ".join(what))
    typer.echo(f"{trace}: {line}")


@app.command("close")
def close(
    state: str = typer.Option(..., "--state"),
    open_items: str = typer.Option(..., "--open"),
    next_step: str = typer.Option(..., "--next"),
) -> None:
    """Close the current span: append its close block to the session record and a span-event to the trace."""
    raise typer.Exit(code=_close_span.run(state, open_items, next_step))
