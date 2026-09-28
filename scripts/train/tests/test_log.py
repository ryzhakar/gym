"""Tests for log.py: a malformed row is refused, and the timestamp is always the clock's, never hand-typed.

Run: `uv run pytest scripts/train/tests/test_log.py`.
"""
from __future__ import annotations

import csv
import sys
from datetime import datetime, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import log  # noqa: E402
import record_schema  # noqa: E402


@pytest.fixture
def sessions_csv(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(record_schema, "RECORD_DIR", tmp_path)
    path = tmp_path / "sessions.csv"
    path.write_text(",".join(record_schema.FILES["sessions"]) + "\n", encoding="utf-8")
    return path


VALID_SESSION_FIELDS = {
    "minutes": "60",
    "gap_days": "0",
    "units": "unit-1",
    "trainer_model": "opus",
    "probe_minutes": "8",
    "assistant_closed": "true",
    "interruptions": "0",
}


def test_valid_row_is_stamped_and_appended(sessions_csv: Path) -> None:
    before = datetime.now()
    row = log.build_row("sessions", dict(VALID_SESSION_FIELDS))
    after = datetime.now()
    stamped = datetime.strptime(row["timestamp"], record_schema.TIMESTAMP_FORMAT)
    assert before - timedelta(minutes=1) <= stamped <= after + timedelta(minutes=1)
    log.append_row("sessions", row)
    with sessions_csv.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    assert rows[1][0] == row["timestamp"]


def test_hand_typed_timestamp_is_refused(sessions_csv: Path) -> None:
    fields = {**VALID_SESSION_FIELDS, "timestamp": "2020-01-01T00:00"}
    with pytest.raises(SystemExit, match="hand-typed"):
        log.build_row("sessions", fields)


@pytest.mark.parametrize(
    ("mutation", "match"),
    [
        (lambda f: f.pop("minutes"), "missing"),
        (lambda f: f.update(unknown_field="x"), "unknown"),
        (lambda f: f.update(assistant_closed="maybe"), "not 'true' or 'false'"),
        (lambda f: f.update(minutes="-1"), "below 0"),
        (lambda f: f.update(minutes="soon"), "not an integer"),
        (lambda f: f.update(units=""), "empty"),
    ],
)
def test_malformed_row_is_refused(sessions_csv: Path, mutation, match: str) -> None:
    fields = dict(VALID_SESSION_FIELDS)
    mutation(fields)
    with pytest.raises(SystemExit, match=match):
        log.build_row("sessions", fields)


def test_append_refuses_a_timestamp_before_the_last_row(sessions_csv: Path) -> None:
    row = log.build_row("sessions", dict(VALID_SESSION_FIELDS))
    log.append_row("sessions", row)
    earlier = {**row, "timestamp": "2000-01-01T00:00"}
    with pytest.raises(SystemExit, match="before"):
        log.append_row("sessions", earlier)


def test_append_refuses_a_mismatched_header(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(record_schema, "RECORD_DIR", tmp_path)
    (tmp_path / "sessions.csv").write_text("wrong,header\n", encoding="utf-8")
    row = log.build_row("sessions", dict(VALID_SESSION_FIELDS))
    with pytest.raises(SystemExit, match="is not the schema's"):
        log.append_row("sessions", row)


def test_append_refuses_a_missing_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(record_schema, "RECORD_DIR", tmp_path)
    row = log.build_row("sessions", dict(VALID_SESSION_FIELDS))
    with pytest.raises(SystemExit, match="no such record file"):
        log.append_row("sessions", row)


@pytest.fixture
def turns_csv(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(record_schema, "RECORD_DIR", tmp_path)
    path = tmp_path / "turns.csv"
    path.write_text(",".join(record_schema.FILES["turns"]) + "\n", encoding="utf-8")
    return path


def test_parse_turn_flags_matches_the_trainer_definitions_literal_invocation() -> None:
    fields = log.parse_turn_flags(
        ["--session", "2026-09-28T10:00", "--n", "1", "--kind", "hint-1", "--item", "unit-1-attempt", "--request", "hint"]
    )
    assert fields == {"session": "2026-09-28T10:00", "n": "1", "kind": "hint-1", "item": "unit-1-attempt", "request_kind": "hint"}


def test_parse_turn_flags_maps_request_none_to_blank() -> None:
    fields = log.parse_turn_flags(
        ["--session", "s", "--n", "1", "--kind", "instruction", "--item", "unit-1-example", "--request", "none"]
    )
    assert fields["request_kind"] == ""


def test_turn_fields_computes_minute_from_the_session_id_never_a_hand_typed_one() -> None:
    session_id = (datetime.now() - timedelta(minutes=5)).strftime(record_schema.TIMESTAMP_FORMAT)
    fields = log.turn_fields(
        ["--session", session_id, "--n", "1", "--kind", "hint-1", "--item", "unit-1-attempt", "--request", "hint"]
    )
    assert float(fields["minute"]) == pytest.approx(5.0, abs=1.0)  # --session truncates to the minute


def test_turn_fields_refuses_a_malformed_session_id() -> None:
    with pytest.raises(SystemExit, match="--session is not"):
        log.turn_fields(["--session", "not-a-timestamp", "--n", "1", "--kind", "hint-1", "--item", "x", "--request", "hint"])


def test_turn_alias_round_trips_through_build_and_append(turns_csv: Path) -> None:
    session_id = datetime.now().strftime(record_schema.TIMESTAMP_FORMAT)
    fields = log.turn_fields(
        ["--session", session_id, "--n", "1", "--kind", "hint-1", "--item", "unit-1-attempt", "--request", "hint"]
    )
    row = log.build_row("turns", fields)
    log.append_row("turns", row)
    assert "hint-1" in turns_csv.read_text(encoding="utf-8")


def test_main_turn_alias_appends_to_turns_csv(turns_csv: Path) -> None:
    session_id = (datetime.now() - timedelta(minutes=1)).strftime(record_schema.TIMESTAMP_FORMAT)
    log.main(
        [
            "log.py",
            "turn",
            "--session",
            session_id,
            "--n",
            "1",
            "--kind",
            "feedback",
            "--item",
            "unit-1-reuse-1",
            "--request",
            "none",
        ]
    )
    with turns_csv.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 1
    assert rows[0]["session"] == session_id
    assert rows[0]["kind"] == "feedback"
    assert rows[0]["item"] == "unit-1-reuse-1"
    assert rows[0]["request_kind"] == ""
    assert float(rows[0]["minute"]) == pytest.approx(1.0, abs=1.0)  # --session truncates to the minute
