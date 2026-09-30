"""train sub-app: gym train open/log/probe/close/status/check on the per-session record layout
under `<subject_dir>/sessions/<session_id>/`. `scripts/train/` (log.py, probe.py, record_schema.py,
check_record.py, hooks/trainer_guard.py) stays untouched and live: a session in progress writes
through it right now."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from gym.train import check as check_module
from gym.train import close as close_module
from gym.train import probe as probe_module
from gym.train import session as session_module
from gym.train import status as status_module
from gym.train.log import log_event

app = typer.Typer(help="Training sessions: per-session events, logging, probing, status, checks.")
probe_app = typer.Typer(help="Stage a unit's probe problems, then grade them once ready — no interactive wait.")
app.add_typer(probe_app, name="probe")


def _validate_which(which: str) -> None:
    if which not in ("immediate", "delayed"):
        raise typer.BadParameter("must be 'immediate' or 'delayed'", param_hint="which")


@app.command("open")
def open_command(
    subject_dir: Path = typer.Argument(...),
    learner: str = typer.Option(..., "--learner"),
    trainer_model: str = typer.Option(..., "--trainer-model"),
    session_id: Optional[str] = typer.Option(None, "--id"),
) -> None:
    """Create the session directory, write session.md's heading, log the open event; print the session id."""
    typer.echo(session_module.open_session(subject_dir, learner, trainer_model, session_id))


@app.command("log")
def log_command(
    subject_dir: Path = typer.Argument(...),
    session_id: str = typer.Argument(...),
    actor: str = typer.Argument(...),
    kind: str = typer.Argument(...),
    fields: Optional[list[str]] = typer.Argument(None),
) -> None:
    """Append one event line after validation."""
    typer.echo(log_event(subject_dir, session_id, actor, kind, fields or []))


@probe_app.command("stage")
def probe_stage_command(
    unit_dir: Path = typer.Argument(...),
    which: str = typer.Argument(..., help="immediate|delayed"),
    session: str = typer.Option(..., "--session"),
) -> None:
    """Copy the unit's probe problems to the work path and log a probe-start event; prints the staged paths."""
    _validate_which(which)
    subject_dir = unit_dir.resolve().parent.parent
    probe_module.run_stage(subject_dir, unit_dir, which, session)


@probe_app.command("grade")
def probe_grade_command(
    unit_dir: Path = typer.Argument(...),
    which: str = typer.Argument(..., help="immediate|delayed"),
    session: str = typer.Option(..., "--session"),
    cap_minutes: float = typer.Option(probe_module.CAP_MINUTES_DEFAULT, "--cap-minutes"),
) -> None:
    """Grade every staged problem against its key and log one probe-item event each (each carrying
    whether it ran over --cap-minutes, recorded only, never enforced); refuses if nothing was
    staged for this unit and side in this session."""
    _validate_which(which)
    subject_dir = unit_dir.resolve().parent.parent
    probe_module.run_grade(subject_dir, unit_dir, which, session, cap_minutes)


@app.command("close")
def close_command(
    subject_dir: Path = typer.Argument(...),
    session_id: str = typer.Argument(...),
    minutes: int = typer.Option(..., "--minutes"),
    units: str = typer.Option(..., "--units"),
    interruptions: int = typer.Option(..., "--interruptions"),
    assistant_closed: str = typer.Option(..., "--assistant-closed"),
    next_step: str = typer.Option(..., "--next"),
    probe_minutes: Optional[float] = typer.Option(None, "--probe-minutes"),
) -> None:
    """Append a close block to session.md and log the close event."""
    typer.echo(
        close_module.close_session(
            subject_dir, session_id, minutes, units, interruptions, assistant_closed, next_step, probe_minutes
        )
    )


@app.command("status")
def status_command(subject_dir: Path = typer.Argument(...)) -> None:
    """Per-unit attempt/probe/confidence history, due queue rows, and the last 20 event lines."""
    raise typer.Exit(code=status_module.main(subject_dir))


@app.command("check")
def check_command(subject_dir: Path = typer.Argument(...)) -> None:
    """Lint every session's events.md and session.md; exit 1 on any FAIL."""
    raise typer.Exit(code=check_module.main(subject_dir))
