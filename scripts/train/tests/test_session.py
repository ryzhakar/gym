"""Round-trip test for session.py: close writes the session and queue rows; open runs a due probe
and hands off to the next unit; a unit's crate is created on demand and joins the workspace.

Run: `uv run pytest scripts/train/tests/test_session.py`. Needs `cargo` on PATH.
"""
from __future__ import annotations

import csv
import shutil
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import log  # noqa: E402
import record_schema  # noqa: E402
import session  # noqa: E402

CARGO_MISSING = shutil.which("cargo") is None


@pytest.fixture(autouse=True)
def isolated_paths(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    record_dir = tmp_path / "record"
    record_dir.mkdir()
    for name, columns in record_schema.FILES.items():
        (record_dir / f"{name}.csv").write_text(",".join(columns) + "\n", encoding="utf-8")
    monkeypatch.setattr(record_schema, "RECORD_DIR", record_dir)
    monkeypatch.setattr(session, "TRAINING_ROOT", tmp_path / "training")
    return tmp_path


def read_rows(name: str) -> list[dict[str, str]]:
    with record_schema.file_path(name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_close_writes_session_and_queue_rows() -> None:
    session.close_session(
        minutes=45,
        units=["unit-1"],
        trainer_model="opus",
        probe_minutes=8,
        assistant_closed=True,
        interruptions=0,
        next_unit_id="unit-2",
    )
    sessions = read_rows("sessions")
    assert len(sessions) == 1
    assert sessions[0]["units"] == "unit-1"
    assert sessions[0]["gap_days"] == "0.0"

    queue = read_rows("queue")
    kinds = {row["kind"]: row for row in queue}
    assert kinds["delayed_probe"]["unit"] == "unit-1"
    assert kinds["delayed_probe"]["due_date"] == (date.today() + timedelta(days=7)).isoformat()
    assert kinds["next_unit"]["unit"] == "unit-2"


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_open_with_no_due_probe_hands_off_to_the_next_unit(isolated_paths: Path, capsys: pytest.CaptureFixture) -> None:
    session.close_session(
        minutes=45,
        units=["unit-1"],
        trainer_model="opus",
        probe_minutes=8,
        assistant_closed=True,
        interruptions=0,
        next_unit_id="unit-2",
    )
    session.open_session(items_root=isolated_paths / "items")
    out = capsys.readouterr().out
    assert "due delayed probes run: none" in out
    assert "next unit: unit-2" in out
    assert "unit-2" in read_workspace_members(isolated_paths)
    assert (isolated_paths / "training/unit-2/Cargo.toml").is_file()


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_open_runs_a_due_delayed_probe_then_hands_off(isolated_paths: Path, capsys: pytest.CaptureFixture) -> None:
    items_root = isolated_paths / "items"
    probe_b = items_root / "unit-1" / "probe-b"
    probe_b.mkdir(parents=True)
    (probe_b / "prompt.md").write_text("isomorph b of unit-1's probe", encoding="utf-8")

    log.append_row(
        "queue",
        log.build_row("queue", {"kind": "delayed_probe", "unit": "unit-1", "due_date": "2020-01-01"}),
    )
    log.append_row(
        "queue",
        log.build_row("queue", {"kind": "next_unit", "unit": "unit-2", "due_date": date.today().isoformat()}),
    )

    session.open_session(items_root=items_root, wait=lambda: None, clock=lambda: 0.0)

    items = read_rows("items")
    assert len(items) == 1
    assert items[0]["unit"] == "unit-1"
    assert items[0]["kind"] == "probe-delayed"

    out = capsys.readouterr().out
    assert "due delayed probes run: ['unit-1']" in out
    assert "next unit: unit-2" in out


def read_workspace_members(root: Path) -> list[str]:
    return session.read_members(root / "training/Cargo.toml")


def test_launch_command_denies_key_reads_and_scopes_bash_to_the_unit_crate() -> None:
    command = session.trainer_launch_command("unit-1")

    assert "--permission-mode dontAsk" in command
    assert "--disallowedTools" in command
    assert session.KEY_DENY_PATTERN in command
    assert "training/rust/items/**/key/**" in command

    for pattern in session.allowed_bash_patterns("unit-1"):
        assert pattern in command
    assert "training/rust/unit-1/Cargo.toml" in command
    # not a blanket Bash allowance — every allowed Bash entry names a specific command
    assert "Bash(*)" not in command
    assert "'Bash'" not in command


def test_launch_command_scopes_cargo_to_the_named_unit_only() -> None:
    command_a = session.trainer_launch_command("unit-1")
    command_b = session.trainer_launch_command("unit-2")

    assert "training/rust/unit-2/Cargo.toml" not in command_a
    assert "training/rust/unit-1/Cargo.toml" not in command_b


@pytest.mark.skipif(CARGO_MISSING, reason="cargo not on PATH")
def test_open_session_prints_a_launch_command_with_the_deny_rule(
    isolated_paths: Path, capsys: pytest.CaptureFixture
) -> None:
    session.close_session(
        minutes=45,
        units=["unit-1"],
        trainer_model="opus",
        probe_minutes=8,
        assistant_closed=True,
        interruptions=0,
        next_unit_id="unit-2",
    )
    session.open_session(items_root=isolated_paths / "items")
    out = capsys.readouterr().out
    assert session.KEY_DENY_PATTERN in out
    assert "--permission-mode dontAsk" in out
