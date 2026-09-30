"""Tests for gym.train.status: gym train status derivations."""
from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from gym.train.events import append_event
from gym.train.status import build_status, due_queue_rows, format_status, other_probes_by_unit


@pytest.fixture
def subject_dir(tmp_path: Path) -> Path:
    directory = tmp_path / "rust"
    session_id = "2026-09-30T10-00"
    (directory / "sessions" / session_id).mkdir(parents=True)
    (directory / "sessions" / session_id / "events.md").touch()
    return directory


SESSION = "2026-09-30T10-00"


def test_due_queue_delayed_probe_needs_seven_days_past_its_own_due_date() -> None:
    rows = [{"event_kind": "queue", "unit": "u1", "kind": "delayed_probe", "due": "2026-09-20"}]
    assert due_queue_rows(rows, today=date(2026, 9, 26)) == []  # 6 days past due: not yet
    assert due_queue_rows(rows, today=date(2026, 9, 27)) == rows  # 7 days past due: due


def test_due_queue_revisit_and_next_unit_are_due_once_their_date_has_passed() -> None:
    revisit = [{"event_kind": "queue", "unit": "u1", "kind": "revisit", "due": "2026-09-26"}]
    assert due_queue_rows(revisit, today=date(2026, 9, 25)) == []
    assert due_queue_rows(revisit, today=date(2026, 9, 26)) == revisit


def test_due_queue_keeps_only_the_latest_row_per_unit_and_kind() -> None:
    rows = [
        {"event_kind": "queue", "unit": "u1", "kind": "revisit", "due": "2026-09-01"},
        {"event_kind": "queue", "unit": "u1", "kind": "revisit", "due": "2026-09-26"},
    ]
    due = due_queue_rows(rows, today=date(2026, 9, 26))
    assert len(due) == 1 and due[0]["due"] == "2026-09-26"


def test_build_status_reads_last_attempt_probe_and_confidence(subject_dir: Path) -> None:
    append_event(subject_dir, SESSION, "trainer", "attempt", {"unit": "u1", "item": "u1-attempt", "result": "fail", "minutes": "3"})
    append_event(subject_dir, SESSION, "trainer", "attempt", {"unit": "u1", "item": "u1-attempt", "result": "pass", "minutes": "2"})
    append_event(
        subject_dir, SESSION, "tool:probe", "probe-item",
        {"unit": "u1", "which": "probe-a", "problem": "p1", "result": "pass", "minutes": "4"},
    )
    append_event(subject_dir, SESSION, "trainer", "confidence", {"unit": "u1", "item": "u1-probe-a-p1", "value": "3"})

    status = build_status(subject_dir)

    assert status["last_attempt"]["u1"]["result"] == "pass"
    assert status["last_probe_immediate"]["u1"]["result"] == "pass"
    assert status["last_probe_delayed"] == {}
    assert status["last_confidence"]["u1"]["value"] == "3"


def test_build_status_tail_is_the_last_20_raw_lines(subject_dir: Path) -> None:
    for n in range(25):
        append_event(subject_dir, SESSION, "trainer", "present", {"unit": "u1", "item": f"item-{n}"})
    status = build_status(subject_dir)
    assert len(status["tail"]) == 20
    assert status["tail"][-1].endswith("item=item-24")
    assert all(line.startswith(SESSION + ": ") for line in status["tail"])


def test_format_status_prints_units_due_queue_and_tail(subject_dir: Path) -> None:
    append_event(subject_dir, SESSION, "trainer", "attempt", {"unit": "u1", "item": "u1-attempt", "result": "pass", "minutes": "2"})
    append_event(subject_dir, SESSION, "manager", "queue", {"unit": "u1", "kind": "next_unit", "due": "2020-01-01"})
    text = format_status(build_status(subject_dir))
    assert "## Units" in text and "- u1" in text
    assert "## Due queue" in text and "next_unit unit=u1 due=2020-01-01" in text
    assert "## Tail (last 20 events)" in text


def test_other_probes_by_unit_ignores_probe_a_and_probe_b_keeping_only_further_sides() -> None:
    rows = [
        {"event_kind": "probe-item", "unit": "u1", "which": "probe-a", "result": "pass"},
        {"event_kind": "probe-item", "unit": "u1", "which": "probe-b", "result": "fail"},
        {"event_kind": "probe-item", "unit": "u1", "which": "probe-c", "result": "pass"},
    ]
    other = other_probes_by_unit(rows)
    assert set(other["u1"]) == {"probe-c"}
    assert other["u1"]["probe-c"]["result"] == "pass"


def test_other_probes_by_unit_keeps_only_the_latest_row_per_side() -> None:
    rows = [
        {"event_kind": "probe-item", "unit": "u1", "which": "probe-c", "result": "fail"},
        {"event_kind": "probe-item", "unit": "u1", "which": "probe-c", "result": "pass"},
    ]
    assert other_probes_by_unit(rows)["u1"]["probe-c"]["result"] == "pass"


def test_build_status_and_format_status_surface_a_third_probe_side(subject_dir: Path) -> None:
    append_event(
        subject_dir, SESSION, "tool:probe", "probe-item",
        {"unit": "u1", "which": "probe-c", "problem": "p1", "result": "pass", "minutes": "4"},
    )

    status = build_status(subject_dir)
    text = format_status(status)

    assert status["other_probes"]["u1"]["probe-c"]["result"] == "pass"
    assert "other probe probe-c: pass" in text
