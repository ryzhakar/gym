"""Root Typer app. Registers one sub-app per group: map, train, research, records."""

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


if __name__ == "__main__":
    app()
