"""Skeleton smoke test: root app and every group resolve and print help."""

import pytest
from typer.testing import CliRunner

from gym.cli import app

runner = CliRunner()


@pytest.mark.parametrize("args", [[], ["map"], ["train"], ["research"], ["records"]])
def test_help_exits_zero(args: list[str]) -> None:
    result = runner.invoke(app, [*args, "--help"])
    assert result.exit_code == 0
