"""map sub-app: will absorb scripts/map/ (census, check_map, estimate, prepare_frame, sample)."""

import typer

app = typer.Typer(help="Opinion map: census, sampling, estimation, frame prep.")
