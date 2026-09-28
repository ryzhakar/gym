"""Tests for probe.py: `key/` is never opened, the item text excludes it, and a real `cargo test` gets logged.

Run: `uv run pytest scripts/train/tests/test_probe.py`. Needs `cargo` on PATH (a `--lib` crate's
default test needs no network).
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import probe  # noqa: E402
import record_schema  # noqa: E402

CARGO_MISSING = shutil.which("cargo") is None


@pytest.fixture(autouse=True)
def isolated_record_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    record_dir = tmp_path / "record"
    record_dir.mkdir()
    (record_dir / "items.csv").write_text(",".join(record_schema.FILES["items"]) + "\n", encoding="utf-8")
    monkeypatch.setattr(record_schema, "RECORD_DIR", record_dir)


def make_unit_dir(root: Path, unit: str) -> Path:
    unit_dir = root / unit
    for probe_name in ("probe-a", "probe-b"):
        probe_dir = unit_dir / probe_name
        probe_dir.mkdir(parents=True)
        (probe_dir / "prompt.md").write_text(f"solve it ({probe_name})", encoding="utf-8")
        key_dir = probe_dir / "key"
        key_dir.mkdir()
        (key_dir / "solution.rs").write_text("the answer, never shown", encoding="utf-8")
    return unit_dir


def test_assert_no_key_refuses_any_key_path() -> None:
    with pytest.raises(SystemExit, match="never opens a 'key/' path"):
        probe.assert_no_key(Path("units/unit-1/probe-a/key/solution.rs"))


def test_item_text_excludes_key(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    text = probe.item_text(unit_dir / "probe-a")
    assert "solve it" in text
    assert "the answer" not in text
    assert "key" not in text


def test_probe_dir_refuses_a_key_target(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    monkeypatch.setitem(probe.ISOMORPH_OF, "immediate", "probe-a/key")
    with pytest.raises(SystemExit, match="never opens a 'key/' path"):
        probe.probe_dir(unit_dir, "immediate")


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_probe_grades_with_cargo_test_and_logs_a_row(tmp_path: Path) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    crate_dir = tmp_path / "crate"
    subprocess.run(["cargo", "new", "--lib", "--name", "unit-1", str(crate_dir)], check=True, capture_output=True)

    clock_values = iter([0.0, 42.0])  # 42 seconds elapsed, well under the cap
    row = probe.run_probe(unit_dir, crate_dir, "immediate", wait=lambda: None, clock=lambda: next(clock_values))

    assert row["unit"] == "unit-1"
    assert row["kind"] == "probe-immediate"
    assert row["item_id"] == "unit-1-probe-a"
    assert row["pass"] == "true"
    assert row["delay_days"] == "0.0"
    assert float(row["minutes"]) == pytest.approx(42.0 / 60, abs=0.01)

    items_csv = (record_schema.RECORD_DIR / "items.csv").read_text(encoding="utf-8")
    assert "unit-1-probe-a" in items_csv


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_run_probe_warns_over_cap(tmp_path: Path, capsys: pytest.CaptureFixture) -> None:
    unit_dir = make_unit_dir(tmp_path, "unit-1")
    crate_dir = tmp_path / "crate"
    subprocess.run(["cargo", "new", "--lib", "--name", "unit-1", str(crate_dir)], check=True, capture_output=True)

    clock_values = iter([0.0, 900.0])  # 15 minutes, over a 10-minute cap
    probe.run_probe(unit_dir, crate_dir, "immediate", cap_minutes=10.0, wait=lambda: None, clock=lambda: next(clock_values))

    assert "over the 10-minute cap" in capsys.readouterr().out
