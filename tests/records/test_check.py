"""gym records check, run against the repo's own committed records."""

from __future__ import annotations

from typer.testing import CliRunner

from gym.records.cli import app

runner = CliRunner()


def test_check_reports_zero_fail_on_the_repo() -> None:
    result = runner.invoke(app, ["check"])
    assert result.exit_code == 0
    assert "records: 0 FAIL" in result.stdout
