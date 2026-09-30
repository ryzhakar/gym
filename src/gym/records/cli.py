"""records sub-app: will absorb scripts/check_records.py, event.py, close_span.py."""

import typer

app = typer.Typer(help="Records: schema checks, event lines, span closes.")
