"""`gym --version` prints the installed package version and exits 0."""

from __future__ import annotations

from importlib.metadata import version

from typer.testing import CliRunner

from gym.cli import app

runner = CliRunner()


def test_version_prints_package_version_and_exits_zero() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert result.stdout.strip() == f"gym {version('gym')}"


def test_root_still_refuses_with_no_command() -> None:
    """--version must not change the existing no-args behaviour."""
    result = runner.invoke(app, [])
    assert result.exit_code == 2
