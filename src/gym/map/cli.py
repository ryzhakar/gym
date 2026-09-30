"""map sub-app: census, check, estimate, frame, sample, site for the Rust opinion map."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from gym.map import census as census_module
from gym.map import check_map as check_map_module
from gym.map import concepts as concepts_module
from gym.map import estimate as estimate_module
from gym.map import prepare_frame as prepare_frame_module
from gym.map import sample as sample_module
from gym.map import site as site_module

app = typer.Typer(help="Opinion map: census, sampling, estimation, frame prep, site.")
concepts_app = typer.Typer(help="Concept-set maintenance.")
app.add_typer(concepts_app, name="concepts")


def _existing_map_dir(map_dir: Path) -> Path:
    """Refuse a map path that isn't a real directory, instead of letting a downstream
    `open()`/`read_text()` surface as a traceback."""
    if not map_dir.is_dir():
        raise typer.BadParameter(f"no such map directory: {map_dir}")
    return map_dir


@app.command()
def check(
    map_dir: Path = typer.Option(
        ..., "--map", help="Map directory to check, e.g. maps/rust", callback=_existing_map_dir
    ),
) -> None:
    """Check a map instance against its schema.yaml. One line per finding; exits 1 on any FAIL."""
    raise typer.Exit(code=check_map_module.main(map_dir))


@concepts_app.command()
def dedup(
    map_path: Path = typer.Argument(
        ..., help="Map directory, e.g. maps/rust", callback=_existing_map_dir
    ),
    apply: bool = typer.Option(False, "--apply", help="Write merged_into to each merged Concept's file"),
    report: Optional[Path] = typer.Option(None, "--report", help="Path to write the merge report"),
) -> None:
    """Merge duplicate/near-duplicate Concepts; prints tier counts, writes the report."""
    raise typer.Exit(code=concepts_module.main(map_path, apply, report))


@app.command()
def census(
    recon: Path = typer.Option(..., "--recon", help="Recon root holding team-a/ and team-b/"),
    batch: int = typer.Option(..., "--batch", help="Batch number this census covers"),
    out: Path = typer.Option(..., "--out", help="Path to write census-b<n>.md and its population CSV"),
) -> None:
    """Nothing-new census gate: writes census-b<n>.md and its population CSV. Exits 1 while anything is flagged."""
    raise typer.Exit(code=census_module.main(recon, batch, out))


@app.command()
def estimate(
    crosswalk_dir: Path = typer.Option(..., "--crosswalk-dir", help="Directory holding the batch's crosswalk CSVs"),
    batch: int = typer.Option(..., "--batch", help="Batch number to estimate closure for"),
    out: Path = typer.Option(..., "--out", help="Path to write the estimate report"),
    threshold: float = typer.Option(0.10, "--threshold", help="Max acceptable unseen fraction before a stratum fails"),
    audit_pass: list[str] = typer.Option(
        [], "--audit-pass",
        help="team(s) whose audit verdict for this batch is PASS; repeat the flag per team (a, b)",
    ),
    merge_check_agreement: float = typer.Option(
        0.0, "--merge-check-agreement", help="Minimum cross-team merge agreement required for closure"
    ),
) -> None:
    """Chapman/Chao1 capture-recapture closure estimate per stratum."""
    bad = sorted(set(audit_pass) - {"a", "b"})
    if bad:
        raise typer.BadParameter(f"--audit-pass: {bad} not one of ['a', 'b']")
    raise typer.Exit(code=estimate_module.main(crosswalk_dir, batch, out, threshold, set(audit_pass), merge_check_agreement))


@app.command()
def frame(
    frame: list[Path] = typer.Option(..., "--frame", help="repeatable; rows are concatenated in the order given"),
    drop: Optional[Path] = typer.Option(None, "--drop", help="CSV with a frame_id column; those rows are excluded"),
    out: Path = typer.Option(..., "--out", help="Path to write the combined sampler input CSV"),
) -> None:
    """Turn frame CSVs into one sampler input CSV for the wide pass."""
    raise typer.Exit(code=prepare_frame_module.main(frame, drop, out))


@app.command(name="sample")
def sample_command(
    frame: Path = typer.Option(..., "--frame", help="Sampler input CSV, as written by `gym map frame`"),
    out: Path = typer.Option(..., "--out", help="directory holding batch-*-team-*.csv"),
    batch: int = typer.Option(..., "--batch", help="Batch number to draw"),
    seed: int = typer.Option(..., "--seed", help="Random seed for the draw, for a reproducible batch"),
    per_team: Optional[int] = typer.Option(None, "--per-team", help="Flat row count per team, ignoring cells"),
    cells: Optional[Path] = typer.Option(None, "--cells", help="CSV: language,hint,per_team; hint * is the whole language"),
    replace: Optional[Path] = typer.Option(None, "--replace", help="CSV: team,frame_id; rows of this batch to replace"),
    by_class: bool = typer.Option(False, "--by-class", help="With --cells: draw per class, not per language"),
    other_class: bool = typer.Option(False, "--other-class", help="with --replace: draw from the cell's other classes"),
) -> None:
    """Draw one batch's stratified samples, or replace listed rows with --replace."""
    given = [name for name, value in (("--per-team", per_team), ("--cells", cells), ("--replace", replace)) if value is not None]
    if len(given) != 1:
        raise typer.BadParameter("exactly one of --per-team, --cells, --replace is required")
    if replace is not None:
        raise typer.Exit(code=sample_module.replace_main(frame, out, batch, seed, replace, other_class))
    if cells is not None:
        raise typer.Exit(code=sample_module.main(frame, out, batch, seed, None, cells, by_class))
    raise typer.Exit(code=sample_module.main(frame, out, batch, seed, per_team, None, by_class))


@app.command()
def site(
    map_path: Path = typer.Argument(
        ..., help="Map directory, e.g. maps/rust", callback=_existing_map_dir
    ),
    out: Optional[Path] = typer.Option(None, "--out", help="default: <map-path>/site/index.html"),
) -> None:
    """Generate the reorderable-matrix site for a map."""
    output = out if out is not None else map_path / "site" / "index.html"
    site_module.main(map_path, output)
    typer.echo(f"file://{output.resolve()}")
