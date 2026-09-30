"""CLI ergonomics: `gym map site`'s --out default and file:// print, and the bad-path refusals
for `gym map check`, `gym map site`, and `gym map concepts dedup`. Site generation itself
(`gym.map.site.main`) is monkeypatched out here -- it is exercised for real in test_site.py --
so these tests stay fast and independent of map data.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from gym.map import cli as map_cli
from gym.map.cli import app

runner = CliRunner()


@pytest.fixture
def map_dir(tmp_path: Path) -> Path:
    directory = tmp_path / "amap"
    directory.mkdir()
    return directory


def test_site_out_defaults_to_map_path_site_index_html(monkeypatch: pytest.MonkeyPatch, map_dir: Path) -> None:
    captured = {}

    def fake_main(map_path: Path, out: Path) -> None:
        captured["map_path"] = map_path
        captured["out"] = out

    monkeypatch.setattr(map_cli, "site_module", type("M", (), {"main": staticmethod(fake_main)}))
    result = runner.invoke(app, ["site", str(map_dir)])
    assert result.exit_code == 0, result.output
    assert captured["out"] == map_dir / "site" / "index.html"


def test_site_prints_file_url_on_success(monkeypatch: pytest.MonkeyPatch, map_dir: Path) -> None:
    monkeypatch.setattr(map_cli, "site_module", type("M", (), {"main": staticmethod(lambda *a: None)}))
    result = runner.invoke(app, ["site", str(map_dir)])
    assert result.exit_code == 0, result.output
    expected = f"file://{(map_dir / 'site' / 'index.html').resolve()}"
    assert expected in result.output


def test_site_out_override_is_respected(monkeypatch: pytest.MonkeyPatch, map_dir: Path, tmp_path: Path) -> None:
    captured = {}
    monkeypatch.setattr(
        map_cli, "site_module", type("M", (), {"main": staticmethod(lambda mp, out: captured.update(out=out))})
    )
    custom_out = tmp_path / "elsewhere.html"
    result = runner.invoke(app, ["site", str(map_dir), "--out", str(custom_out)])
    assert result.exit_code == 0, result.output
    assert captured["out"] == custom_out
    assert f"file://{custom_out.resolve()}" in result.output


@pytest.mark.parametrize(
    "args",
    [
        ["check", "--map", "{bad}"],
        ["site", "{bad}"],
        ["concepts", "dedup", "{bad}"],
    ],
)
def test_bad_map_path_is_one_line_exit_2_no_traceback(args: list[str], tmp_path: Path) -> None:
    bad = tmp_path / "does-not-exist"
    resolved = [a.format(bad=bad) for a in args]
    result = runner.invoke(app, resolved)
    assert result.exit_code == 2
    assert "Traceback" not in result.output
    # Rich's error box wraps a long path across lines, so check the (whitespace-
    # collapsed) box body names the bad path, rather than a single contiguous line.
    assert bad.name in " ".join(result.output.split())
