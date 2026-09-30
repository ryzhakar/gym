"""train sub-app: will absorb scripts/train/ (record_schema, check_record, log, probe, hooks)."""

import typer

app = typer.Typer(help="Training sessions: records, logging, probing, guardrails.")
