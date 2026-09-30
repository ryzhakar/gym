"""Tests for gym.train.session: gym train open."""
from __future__ import annotations

from pathlib import Path

import pytest

from gym.train.events import events_path, session_md_path
from gym.train.session import gap_days, open_session


@pytest.fixture
def subject_dir(tmp_path: Path) -> Path:
    return tmp_path / "rust"


def test_open_session_creates_the_directory_and_heading(subject_dir: Path) -> None:
    session_id = open_session(subject_dir, "arthur", "opus", "2026-09-30T10:00")
    assert session_id == "2026-09-30T10:00"
    heading = session_md_path(subject_dir, session_id).read_text(encoding="utf-8")
    assert heading.splitlines()[0] == "# 2026-09-30T10:00"
    assert "learner: arthur" in heading
    assert "trainer model: opus" in heading
    assert "gap_days: none" in heading


def test_open_session_logs_the_open_event(subject_dir: Path) -> None:
    session_id = open_session(subject_dir, "arthur", "opus", "2026-09-30T10:00")
    events = events_path(subject_dir, session_id).read_text(encoding="utf-8")
    assert " | manager | open | " in events
    assert "learner=arthur" in events
    assert "trainer_model=opus" in events


def test_open_session_defaults_the_id_to_now(subject_dir: Path) -> None:
    session_id = open_session(subject_dir, "arthur", "opus")
    assert session_md_path(subject_dir, session_id).is_file()


def test_open_session_refuses_an_existing_session(subject_dir: Path) -> None:
    open_session(subject_dir, "arthur", "opus", "2026-09-30T10:00")
    with pytest.raises(SystemExit, match="already exists"):
        open_session(subject_dir, "arthur", "opus", "2026-09-30T10:00")


def test_gap_days_is_none_for_the_first_session(subject_dir: Path) -> None:
    assert gap_days(subject_dir, "2026-09-30T10:00") is None


def test_gap_days_is_computed_from_the_previous_session(subject_dir: Path) -> None:
    open_session(subject_dir, "arthur", "opus", "2026-09-28T10:00")
    assert gap_days(subject_dir, "2026-09-30T10:00") == pytest.approx(2.0)


def test_second_open_session_writes_the_measured_gap(subject_dir: Path) -> None:
    open_session(subject_dir, "arthur", "opus", "2026-09-28T10:00")
    open_session(subject_dir, "arthur", "opus", "2026-09-30T10:00")
    heading = session_md_path(subject_dir, "2026-09-30T10:00").read_text(encoding="utf-8")
    assert "gap_days: 2.00" in heading
