"""records sub-app: the record checks memento lacks. Writes go through the memento CLI."""

from __future__ import annotations

import typer

from gym.records import check_records as _check_records

app = typer.Typer(help="Records: the checks `memento check` lacks.")


@app.callback()
def records() -> None:
    """Keeps `check` a named subcommand while it is the group's only command."""


@app.command("check")
def check() -> None:
    """Check the map's audit line, retired entries, opinion-map and subject pointers and wraps, and untracked record files."""
    raise typer.Exit(code=_check_records.main())
