"""Tests for gym.train.events: appending and reading one session's events.md."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pytest

from gym.train.events import all_events, all_session_ids, append_event, build_line, parse_line, read_events


@pytest.fixture
def subject_dir(tmp_path: Path) -> Path:
    return tmp_path / "rust"


@pytest.fixture
def opened_session(subject_dir: Path) -> str:
    session_id = "2026-09-30T10-00"
    (subject_dir / "sessions" / session_id).mkdir(parents=True)
    (subject_dir / "sessions" / session_id / "events.md").touch()
    return session_id


def test_append_event_stamps_with_the_clock_and_appends(subject_dir: Path, opened_session: str) -> None:
    line = append_event(subject_dir, opened_session, "manager", "open", {"learner": "arthur", "trainer_model": "opus"})
    assert line.startswith(datetime.now().strftime("%Y-%m-%d"))
    text = (subject_dir / "sessions" / opened_session / "events.md").read_text(encoding="utf-8")
    assert text.strip() == line


def test_append_event_refuses_an_unknown_kind(subject_dir: Path, opened_session: str) -> None:
    with pytest.raises(SystemExit, match="unknown kind"):
        append_event(subject_dir, opened_session, "manager", "bogus-kind", {"unit": "u1"})


def test_append_event_refuses_an_unknown_actor(subject_dir: Path, opened_session: str) -> None:
    with pytest.raises(SystemExit, match="unknown actor"):
        append_event(subject_dir, opened_session, "ghost", "present", {"unit": "u1", "item": "x"})


def test_append_event_refuses_a_missing_required_field(subject_dir: Path, opened_session: str) -> None:
    with pytest.raises(SystemExit, match="missing field"):
        append_event(subject_dir, opened_session, "trainer", "present", {"unit": "u1"})


def test_append_event_refuses_a_bad_value(subject_dir: Path, opened_session: str) -> None:
    with pytest.raises(SystemExit, match="not one of"):
        append_event(subject_dir, opened_session, "learner", "request", {"unit": "u1", "item": "x", "request": "solution"})


def test_append_event_refuses_a_missing_session(subject_dir: Path) -> None:
    with pytest.raises(SystemExit, match="no such session"):
        append_event(subject_dir, "2026-09-30T09-00", "manager", "open", {"learner": "arthur", "trainer_model": "opus"})


def test_append_event_refuses_a_time_before_the_last_line(subject_dir: Path, opened_session: str) -> None:
    append_event(subject_dir, opened_session, "trainer", "present", {"unit": "u1", "item": "x"}, now=datetime(2026, 9, 30, 10, 5))
    with pytest.raises(SystemExit, match="before"):
        append_event(
            subject_dir, opened_session, "trainer", "present", {"unit": "u1", "item": "y"}, now=datetime(2026, 9, 30, 10, 0)
        )


def test_read_events_round_trips_every_field(subject_dir: Path, opened_session: str) -> None:
    append_event(subject_dir, opened_session, "trainer", "attempt", {"unit": "u1", "item": "x", "result": "pass", "minutes": "4.5"})
    rows = read_events(subject_dir / "sessions" / opened_session / "events.md")
    assert len(rows) == 1
    row = rows[0]
    assert row["actor"] == "trainer" and row["event_kind"] == "attempt"
    assert row["unit"] == "u1" and row["item"] == "x" and row["result"] == "pass" and row["minutes"] == "4.5"
    assert "raw" in row


def test_all_events_spans_every_session_oldest_first(subject_dir: Path) -> None:
    for session_id in ("2026-09-28T10-00", "2026-09-30T10-00"):
        (subject_dir / "sessions" / session_id).mkdir(parents=True)
        (subject_dir / "sessions" / session_id / "events.md").touch()
        append_event(subject_dir, session_id, "manager", "open", {"learner": "arthur", "trainer_model": "opus"})
    rows = all_events(subject_dir)
    assert [row["session"] for row in rows] == ["2026-09-28T10-00", "2026-09-30T10-00"]


def test_all_session_ids_sorted(subject_dir: Path) -> None:
    for session_id in ("2026-09-30T10-00", "2026-09-28T10-00"):
        (subject_dir / "sessions" / session_id).mkdir(parents=True)
    assert all_session_ids(subject_dir) == ["2026-09-28T10-00", "2026-09-30T10-00"]


def test_all_session_ids_empty_when_no_sessions_dir(subject_dir: Path) -> None:
    assert all_session_ids(subject_dir) == []


def test_build_line_and_parse_line_round_trip() -> None:
    line = build_line("2026-09-30T10:00", "trainer", "present", {"unit": "u1", "item": "x"})
    timestamp, actor, kind, fields = parse_line(line)
    assert (timestamp, actor, kind, fields) == ("2026-09-30T10:00", "trainer", "present", {"unit": "u1", "item": "x"})


def test_parse_line_refuses_a_malformed_line() -> None:
    with pytest.raises(ValueError, match="not 'timestamp"):
        parse_line("not a valid line at all")
