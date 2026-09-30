"""Tests for gym.train.check: gym train check."""
from __future__ import annotations

from pathlib import Path

import pytest

from gym.train.check import check
from gym.train.events import append_event
from gym.train.session import open_session


@pytest.fixture
def subject_dir(tmp_path: Path) -> Path:
    return tmp_path / "rust"


def test_clean_open_session_has_no_findings(subject_dir: Path) -> None:
    open_session(subject_dir, "arthur", "opus", "2026-09-30T10-00")
    assert check(subject_dir) == []


def test_malformed_line_is_a_fail(subject_dir: Path) -> None:
    open_session(subject_dir, "arthur", "opus", "2026-09-30T10-00")
    events = subject_dir / "sessions" / "2026-09-30T10-00" / "events.md"
    with events.open("a", encoding="utf-8") as handle:
        handle.write("not a valid line\n")
    findings = check(subject_dir)
    assert any("not 'timestamp" in finding for finding in findings)


def test_unknown_kind_is_a_fail(subject_dir: Path) -> None:
    open_session(subject_dir, "arthur", "opus", "2026-09-30T10-00")
    events = subject_dir / "sessions" / "2026-09-30T10-00" / "events.md"
    with events.open("a", encoding="utf-8") as handle:
        handle.write("2026-09-30T10:05 | trainer | bogus-kind | unit=u1\n")
    findings = check(subject_dir)
    assert any("unknown kind" in finding for finding in findings)


def test_start_kind_is_now_known_and_clean(subject_dir: Path) -> None:
    """`start` (a unit's opening turn) was added past the task's original 13 kinds; confirm it no
    longer trips 'unknown kind'."""
    open_session(subject_dir, "arthur", "opus", "2026-09-30T10-00")
    events = subject_dir / "sessions" / "2026-09-30T10-00" / "events.md"
    with events.open("a", encoding="utf-8") as handle:
        handle.write("2099-01-01T00:00 | trainer | start | unit=u1\n")
    assert check(subject_dir) == []


def test_missing_required_field_is_a_fail(subject_dir: Path) -> None:
    open_session(subject_dir, "arthur", "opus", "2026-09-30T10-00")
    events = subject_dir / "sessions" / "2026-09-30T10-00" / "events.md"
    with events.open("a", encoding="utf-8") as handle:
        handle.write("2026-09-30T10:05 | trainer | present | unit=u1\n")
    findings = check(subject_dir)
    assert any("missing field" in finding for finding in findings)


def test_time_going_backward_is_a_fail(subject_dir: Path) -> None:
    open_session(subject_dir, "arthur", "opus", "2026-09-30T10-00")
    events = subject_dir / "sessions" / "2026-09-30T10-00" / "events.md"
    with events.open("a", encoding="utf-8") as handle:
        handle.write("2026-09-30T09:00 | trainer | present | unit=u1 item=x\n")
    findings = check(subject_dir)
    assert any("goes back" in finding for finding in findings)


def test_session_md_missing_heading_is_a_fail(subject_dir: Path) -> None:
    open_session(subject_dir, "arthur", "opus", "2026-09-30T10-00")
    (subject_dir / "sessions" / "2026-09-30T10-00" / "session.md").write_text("no heading here\n", encoding="utf-8")
    findings = check(subject_dir)
    assert any("no heading" in finding for finding in findings)


def test_closed_session_without_a_close_block_is_a_fail(subject_dir: Path) -> None:
    open_session(subject_dir, "arthur", "opus", "2026-09-30T10-00")
    append_event(
        subject_dir, "2026-09-30T10-00", "manager", "close",
        {"minutes": "10", "units": "u1", "interruptions": "0", "assistant_closed": "yes"},
    )
    findings = check(subject_dir)
    assert any("no close block" in finding for finding in findings)


def test_closed_session_with_a_close_block_is_clean(subject_dir: Path) -> None:
    from gym.train.close import close_session

    open_session(subject_dir, "arthur", "opus", "2026-09-30T10-00")
    close_session(subject_dir, "2026-09-30T10-00", minutes=10, units="u1", interruptions=0, assistant_closed="yes", next_step="u2")
    assert check(subject_dir) == []
