"""train sub-app: gym train open/log/probe/close/status/check on the per-session record layout
under `<subject_dir>/sessions/<session_id>/`. `scripts/train/` (log.py, probe.py, record_schema.py,
check_record.py, hooks/trainer_guard.py) stays untouched and live: a session in progress writes
through it right now."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from gym.train import baseline as baseline_module
from gym.train import check as check_module
from gym.train import close as close_module
from gym.train import probe as probe_module
from gym.train import session as session_module
from gym.train import status as status_module
from gym.train.log import log_event

app = typer.Typer(help="Training sessions: per-session events, logging, probing, status, checks.")
probe_app = typer.Typer(help="Stage a unit's probe problems, then grade them once ready — no interactive wait.")
app.add_typer(probe_app, name="probe")
baseline_app = typer.Typer(help="Stage a baseline item's stub, then grade it once ready — mirrors probe stage/grade.")
app.add_typer(baseline_app, name="baseline")


def _validate_which(which: str) -> None:
    if which in ("immediate", "delayed") or probe_module.SIDE_PATTERN.fullmatch(which):
        return
    raise typer.BadParameter(
        "must be 'immediate', 'delayed', or a literal 'probe-[a-z]' side name", param_hint="which"
    )


@app.command("open")
def open_command(
    subject_dir: Path = typer.Argument(..., help="Subject directory, e.g. training/rust; created if new"),
    learner: str = typer.Option(..., "--learner", help="The learner's name, recorded in session.md"),
    trainer_model: str = typer.Option(..., "--trainer-model", help="The trainer model's name, recorded in session.md"),
    session_id: Optional[str] = typer.Option(
        None, "--id", help="Session id, YYYY-MM-DDTHH-MM; default: now"
    ),
) -> None:
    """Create the session directory, write session.md's heading, log the open event; print the session id."""
    typer.echo(session_module.open_session(subject_dir, learner, trainer_model, session_id))


@app.command("log")
def log_command(
    subject_dir: Path = typer.Argument(..., help="Subject directory, e.g. training/rust"),
    session_id: str = typer.Argument(..., help="Session id this event belongs to, as printed by `gym train open`"),
    actor: str = typer.Argument(..., help="Who logged this event: manager, trainer, tool:probe, ..."),
    kind: str = typer.Argument(..., help="Event kind the session schema admits, e.g. attempt, feedback, queue"),
    fields: Optional[list[str]] = typer.Argument(None, help="field=value pairs carried by this event kind"),
) -> None:
    """Append one event line after validation."""
    typer.echo(log_event(subject_dir, session_id, actor, kind, fields or []))


@probe_app.command("stage")
def probe_stage_command(
    unit_dir: Path = typer.Argument(..., help="Unit directory holding the probe's problem files"),
    which: str = typer.Argument(..., help="immediate|delayed|probe-<letter>"),
    session: str = typer.Option(..., "--session", help="Session id this stage belongs to"),
) -> None:
    """Copy the unit's probe problems to the work path and log a probe-start event; prints the staged paths."""
    _validate_which(which)
    subject_dir = unit_dir.resolve().parent.parent
    probe_module.run_stage(subject_dir, unit_dir, which, session)


@probe_app.command("go")
def probe_go_command(
    unit_dir: Path = typer.Argument(..., help="Unit directory holding the probe's problem files"),
    which: str = typer.Argument(..., help="immediate|delayed|probe-<letter>"),
    session: str = typer.Option(..., "--session", help="Session id this go belongs to"),
) -> None:
    """Log the learner's start mark for the staged probe; grade then measures minutes from it.
    Refuses if nothing was staged for this unit and side in this session."""
    _validate_which(which)
    subject_dir = unit_dir.resolve().parent.parent
    probe_module.run_go(subject_dir, unit_dir, which, session)


@probe_app.command("grade")
def probe_grade_command(
    unit_dir: Path = typer.Argument(..., help="Unit directory holding the probe's problem files"),
    which: str = typer.Argument(..., help="immediate|delayed|probe-<letter>"),
    session: str = typer.Option(..., "--session", help="Session id this grade belongs to"),
    cap_minutes: float = typer.Option(
        probe_module.CAP_MINUTES_DEFAULT, "--cap-minutes", help="Minutes per problem recorded as the cap, never enforced"
    ),
) -> None:
    """Grade every staged problem against its key and log one probe-item event each (each carrying
    whether it ran over --cap-minutes, recorded only, never enforced); refuses if nothing was
    staged for this unit and side in this session. Minutes run from the latest probe go when one
    was logged since staging, else from the stage time."""
    _validate_which(which)
    subject_dir = unit_dir.resolve().parent.parent
    probe_module.run_grade(subject_dir, unit_dir, which, session, cap_minutes)


@baseline_app.command("stage")
def baseline_stage_command(
    subject_dir: Path = typer.Argument(..., help="Subject directory, e.g. training/rust"),
    item: Optional[str] = typer.Option(None, "--item", help="Baseline item id, e.g. b1-own; required unless --all"),
    session: str = typer.Option(..., "--session", help="Session id this stage belongs to"),
    all_items: bool = typer.Option(False, "--all", help="Stage all six baseline items, in order, ignoring --item"),
) -> None:
    """Copy the item's stub/ to its own work path (absolute, from this command's own arguments,
    never the caller's cwd) and log a present event; prints the staged path. --all stages every
    baseline item in order."""
    subject_dir = subject_dir.resolve()
    if all_items:
        baseline_module.run_stage_all(subject_dir, session)
        return
    if not item:
        raise typer.BadParameter("required unless --all is given", param_hint="--item")
    baseline_module.run_stage(subject_dir, item, session)


@baseline_app.command("grade")
def baseline_grade_command(
    subject_dir: Path = typer.Argument(..., help="Subject directory, e.g. training/rust"),
    item: str = typer.Option(..., "--item", help="Baseline item id, e.g. b1-own"),
    session: str = typer.Option(..., "--session", help="Session id this grade belongs to"),
    cap_minutes: float = typer.Option(
        baseline_module.CAP_MINUTES_DEFAULT, "--cap-minutes", help="Minutes recorded as the cap, never enforced"
    ),
) -> None:
    """Grade the staged item against its key and log one probe-item event (which=baseline);
    refuses if nothing was staged for this item in this session. Never opens or prints key/."""
    subject_dir = subject_dir.resolve()
    baseline_module.run_grade(subject_dir, item, session, cap_minutes)


@app.command("close")
def close_command(
    subject_dir: Path = typer.Argument(..., help="Subject directory, e.g. training/rust"),
    session_id: str = typer.Argument(..., help="Session id to close, as printed by `gym train open`"),
    minutes: int = typer.Option(..., "--minutes", help="Total minutes the session ran"),
    units: str = typer.Option(..., "--units", help="Unit id(s) worked this session, comma-separated"),
    interruptions: int = typer.Option(..., "--interruptions", help="Count of interruptions during the session"),
    assistant_closed: str = typer.Option(..., "--assistant-closed", help="yes/no: did the trainer close the session"),
    next_step: str = typer.Option(..., "--next", help="First step for the next session"),
    probe_minutes: Optional[float] = typer.Option(
        None, "--probe-minutes", help="Total minutes spent on probes this session, if any ran"
    ),
) -> None:
    """Append a close block to session.md and log the close event."""
    typer.echo(
        close_module.close_session(
            subject_dir, session_id, minutes, units, interruptions, assistant_closed, next_step, probe_minutes
        )
    )


@app.command("status")
def status_command(
    subject_dir: Path = typer.Argument(..., help="Subject directory, e.g. training/rust"),
) -> None:
    """Per-unit attempt/probe/confidence history, due queue rows, and the last 20 event lines."""
    raise typer.Exit(code=status_module.main(subject_dir))


@app.command("check")
def check_command(
    subject_dir: Path = typer.Argument(..., help="Subject directory, e.g. training/rust"),
) -> None:
    """Lint every session's events.md and session.md; exit 1 on any FAIL."""
    raise typer.Exit(code=check_module.main(subject_dir))
