"""Root Typer app. Registers one sub-app per group: map, train, research, records."""

from importlib.metadata import version
from typing import Optional

import typer

from gym.map.cli import app as map_app
from gym.records.cli import app as records_app
from gym.research.cli import app as research_app
from gym.train.cli import app as train_app

app = typer.Typer(help="gym: administrative concerns for the language-learning project.")

app.add_typer(map_app, name="map")
app.add_typer(train_app, name="train")
app.add_typer(research_app, name="research")
app.add_typer(records_app, name="records")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"gym {version('gym')}")
        raise typer.Exit()


@app.callback()
def main(
    version_: Optional[bool] = typer.Option(
        None, "--version", callback=_version_callback, is_eager=True, help="Print gym's version and exit."
    ),
) -> None:
    pass


if __name__ == "__main__":
    app()
