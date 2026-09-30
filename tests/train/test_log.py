"""Tests for gym.train.log: gym train log."""
from __future__ import annotations

from pathlib import Path

import pytest

from gym.train.events import events_path
from gym.train.log import log_event


@pytest.fixture
def opened_session(tmp_path: Path) -> tuple[Path, str]:
    subject_dir = tmp_path / "rust"
    session_id = "2026-09-30T10:00"
    (subject_dir / "sessions" / session_id).mkdir(parents=True)
    (subject_dir / "sessions" / session_id / "events.md").touch()
    return subject_dir, session_id


def test_log_event_appends_a_valid_line(opened_session: tuple[Path, str]) -> None:
    subject_dir, session_id = opened_session
    line = log_event(subject_dir, session_id, "trainer", "present", ["unit=u1", "item=x"])
    assert "trainer | present | unit=u1 item=x" in line
    assert events_path(subject_dir, session_id).read_text(encoding="utf-8").strip() == line


def test_log_event_refuses_a_malformed_token(opened_session: tuple[Path, str]) -> None:
    subject_dir, session_id = opened_session
    with pytest.raises(SystemExit, match="not 'field=value'"):
        log_event(subject_dir, session_id, "trainer", "present", ["unit=u1", "bogus"])


def test_log_event_note_absorbs_the_rest_of_the_tokens(opened_session: tuple[Path, str]) -> None:
    subject_dir, session_id = opened_session
    line = log_event(
        subject_dir, session_id, "trainer", "ladder-gap",
        ["unit=u1", "item=x", "note=ladder", "gap:", "u1", "after", "level", "3"],
    )
    assert "note=ladder gap: u1 after level 3" in line
