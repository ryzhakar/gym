"""Tests for gym.train.close: gym train close."""
from __future__ import annotations

from pathlib import Path

import pytest

from gym.train.close import close_session, summarize_state
from gym.train.events import append_event, events_path, session_md_path


@pytest.fixture
def opened_session(tmp_path: Path) -> tuple[Path, str]:
    subject_dir = tmp_path / "rust"
    session_id = "2026-09-30T10-00"
    (subject_dir / "sessions" / session_id).mkdir(parents=True)
    (subject_dir / "sessions" / session_id / "events.md").touch()
    session_md_path(subject_dir, session_id).write_text(f"# {session_id}\n", encoding="utf-8")
    return subject_dir, session_id


def test_summarize_state_counts_probe_items() -> None:
    rows = [
        {"event_kind": "probe-item", "result": "pass"},
        {"event_kind": "probe-item", "result": "fail"},
    ]
    assert summarize_state(rows) == "1/2 probe item(s) passed"


def test_summarize_state_lists_queue_rows_by_their_own_kind_field() -> None:
    rows = [{"event_kind": "queue", "kind": "delayed_probe", "unit": "u1", "due": "2026-10-07"}]
    assert summarize_state(rows) == "queued delayed_probe:u1@2026-10-07"


def test_summarize_state_with_no_probe_or_queue_events() -> None:
    assert summarize_state([{"event_kind": "present", "unit": "u1"}]) == "no probe or queue events this session"


def test_close_session_appends_close_block_and_close_event(opened_session: tuple[Path, str]) -> None:
    subject_dir, session_id = opened_session
    line = close_session(subject_dir, session_id, minutes=45, units="u1", interruptions=0, assistant_closed="yes", next_step="u2 next")
    assert " | manager | close | " in line
    assert "minutes=45 units=u1 interruptions=0 assistant_closed=yes" in line

    events_text = events_path(subject_dir, session_id).read_text(encoding="utf-8")
    assert events_text.strip() == line

    session_text = session_md_path(subject_dir, session_id).read_text(encoding="utf-8")
    assert "## Close — " in session_text
    assert "state   no probe or queue events this session" in session_text
    assert "open    none" in session_text
    assert "next    u2 next" in session_text


def test_close_session_summarizes_probe_and_queue_events(opened_session: tuple[Path, str]) -> None:
    subject_dir, session_id = opened_session
    append_event(subject_dir, session_id, "tool:probe", "probe-item", {"unit": "u1", "which": "probe-a", "problem": "p1", "result": "pass", "minutes": "5"})
    append_event(subject_dir, session_id, "manager", "queue", {"unit": "u1", "kind": "delayed_probe", "due": "2026-10-07"})

    close_session(subject_dir, session_id, minutes=30, units="u1", interruptions=1, assistant_closed="no", next_step="revisit u1")

    session_text = session_md_path(subject_dir, session_id).read_text(encoding="utf-8")
    assert "1/1 probe item(s) passed" in session_text
    assert "queued delayed_probe:u1@2026-10-07" in session_text
    assert "open    interruptions=1 assistant_closed=no" in session_text


def test_close_session_accepts_the_optional_probe_minutes_field(opened_session: tuple[Path, str]) -> None:
    """Team lead ruling (2026-09-30): `close` may optionally carry `probe_minutes`, a
    non-negative number — the old `sessions.csv` column this schema had no home for until now."""
    subject_dir, session_id = opened_session
    line = close_session(
        subject_dir, session_id, minutes=30, units="u1", interruptions=0, assistant_closed="yes",
        next_step="u2", probe_minutes=8.5,
    )
    assert "probe_minutes=8.5" in line


def test_close_session_omits_probe_minutes_when_not_given(opened_session: tuple[Path, str]) -> None:
    subject_dir, session_id = opened_session
    line = close_session(subject_dir, session_id, minutes=30, units="u1", interruptions=0, assistant_closed="yes", next_step="u2")
    assert "probe_minutes" not in line


def test_close_session_refuses_a_negative_probe_minutes(opened_session: tuple[Path, str]) -> None:
    subject_dir, session_id = opened_session
    with pytest.raises(SystemExit, match="below 0"):
        close_session(
            subject_dir, session_id, minutes=30, units="u1", interruptions=0, assistant_closed="yes",
            next_step="u2", probe_minutes=-1.0,
        )
