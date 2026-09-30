"""Tests for gym.train.log: gym train log."""
from __future__ import annotations

from pathlib import Path

import pytest

from gym.train.events import events_path, read_events
from gym.train.log import log_event


@pytest.fixture
def opened_session(tmp_path: Path) -> tuple[Path, str]:
    subject_dir = tmp_path / "rust"
    session_id = "2026-09-30T10-00"
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


def test_log_event_treats_each_argv_token_as_one_field_never_splitting_on_spaces(opened_session: tuple[Path, str]) -> None:
    """Team lead ruling (2026-09-30): a shell-quoted value survives as one argv item, verbatim,
    space and all — `gym train log ... note="ladder gap: u1 after level 3"` (the shell already
    stripped the quotes down to one list item by the time Python sees it). The stored line quotes
    it in turn (`note="ladder gap: u1 after level 3"`, double-quoted per `quote_value`), and reads
    back to the exact same value via `shlex.split`."""
    subject_dir, session_id = opened_session
    line = log_event(
        subject_dir, session_id, "trainer", "ladder-gap",
        ["unit=u1", "item=x", "note=ladder gap: u1 after level 3"],
    )
    assert 'note="ladder gap: u1 after level 3"' in line
    rows = read_events(events_path(subject_dir, session_id))
    assert rows[-1]["note"] == "ladder gap: u1 after level 3"


def test_log_event_no_longer_joins_unquoted_tokens_into_one_field(opened_session: tuple[Path, str]) -> None:
    """The old behaviour (an unquoted, multi-token note stitched back together) is gone: each argv
    token must now be its own complete `key=value` pair."""
    subject_dir, session_id = opened_session
    with pytest.raises(SystemExit, match="not 'field=value'"):
        log_event(
            subject_dir, session_id, "trainer", "ladder-gap",
            ["unit=u1", "item=x", "note=ladder", "gap:", "u1", "after", "level", "3"],
        )


def test_log_event_a_value_may_hold_an_embedded_equals_sign(opened_session: tuple[Path, str]) -> None:
    subject_dir, session_id = opened_session
    line = log_event(subject_dir, session_id, "trainer", "instruction", ["unit=u1", "item=x", "principle=a=b, not c"])
    assert 'principle="a=b, not c"' in line
    rows = read_events(events_path(subject_dir, session_id))
    assert rows[-1]["principle"] == "a=b, not c"


def test_log_event_refuses_a_field_given_twice(opened_session: tuple[Path, str]) -> None:
    subject_dir, session_id = opened_session
    with pytest.raises(SystemExit, match="given twice"):
        log_event(subject_dir, session_id, "trainer", "present", ["unit=u1", "unit=u2"])


def test_log_event_a_value_with_an_apostrophe_and_a_comma_round_trips(opened_session: tuple[Path, str]) -> None:
    """The exact live example from the report: `principle="move, don't copy"`."""
    subject_dir, session_id = opened_session
    log_event(subject_dir, session_id, "trainer", "instruction", ["unit=u1", "item=x", "principle=move, don't copy"])
    rows = read_events(events_path(subject_dir, session_id))
    assert rows[-1]["principle"] == "move, don't copy"


def test_log_event_writes_the_optional_request_field_on_a_hint_turn(opened_session: tuple[Path, str]) -> None:
    """Team lead ruling (2026-09-30): a hint or answer turn can carry the learner's own ask on one
    line instead of a separate `request` event first."""
    subject_dir, session_id = opened_session
    line = log_event(
        subject_dir, session_id, "trainer", "hint",
        ["unit=u1", "item=x", "level=1", "source=supplied", "request=hint"],
    )
    assert "request=hint" in line
