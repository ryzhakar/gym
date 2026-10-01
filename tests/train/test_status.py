"""Tests for gym.train.status: gym train status derivations."""
from __future__ import annotations

from datetime import date, datetime
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
    assert "## Units" in text and "u1" in text.splitlines()[2]
    assert "## Due queue" in text
    due_row = next(line for line in text.splitlines() if line.startswith("next_unit"))
    assert due_row.split() == ["next_unit", "u1", "2020-01-01"]
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
    assert "probe-c: pass" in text


def _stamp(day: str, hour_minute: str = "10:00") -> datetime:
    return datetime.fromisoformat(f"{day}T{hour_minute}")


def _queue(unit: str, kind: str, due: str, timestamp: str) -> dict[str, str]:
    return {"event_kind": "queue", "unit": unit, "kind": kind, "due": due, "timestamp": timestamp}


def _event(event_kind: str, unit: str, timestamp: str, **fields: str) -> dict[str, str]:
    return {"event_kind": event_kind, "unit": unit, "timestamp": timestamp, **fields}


def test_live_case_a_next_unit_with_a_later_attempt_in_another_session_is_not_due(tmp_path: Path) -> None:
    """The session 2026-10-01T15-56 defect: next_unit u02 queued 2026-09-30, attempts on u02 on 2026-10-01."""
    subject = tmp_path / "rust"
    first, second = "2026-09-30T15-40", "2026-10-01T15-56"
    for session_id in (first, second):
        (subject / "sessions" / session_id).mkdir(parents=True)
        (subject / "sessions" / session_id / "events.md").touch()
    append_event(
        subject, first, "manager", "queue", {"unit": "u02", "kind": "next_unit", "due": "2026-10-01"},
        now=_stamp("2026-09-30", "18:24"),
    )
    append_event(subject, second, "trainer", "start", {"unit": "u02"}, now=_stamp("2026-10-01", "15:57"))
    append_event(
        subject, second, "trainer", "attempt", {"unit": "u02", "item": "attempt", "result": "pass", "minutes": "15"},
        now=_stamp("2026-10-01", "17:53"),
    )

    assert build_status(subject, today=date(2026, 10, 1))["due_queue"] == []


def test_a_next_unit_row_with_no_later_event_of_its_unit_stays_due() -> None:
    rows = [_queue("u02", "next_unit", "2026-10-01", "2026-09-30T18:24")]
    assert due_queue_rows(rows, today=date(2026, 10, 1)) == rows


@pytest.mark.parametrize("consumer", ["start", "attempt"])
def test_next_unit_is_consumed_by_a_later_start_or_attempt_of_its_unit(consumer: str) -> None:
    rows = [_queue("u02", "next_unit", "2026-10-01", "2026-09-30T18:24"), _event(consumer, "u02", "2026-10-01T15:57")]
    assert due_queue_rows(rows, today=date(2026, 10, 1)) == []


def test_next_unit_is_consumed_by_a_later_probe_item_of_its_unit() -> None:
    rows = [
        _queue("u02", "next_unit", "2026-10-01", "2026-09-30T18:24"),
        _event("probe-item", "u02", "2026-10-01T18:13", which="probe-a"),
    ]
    assert due_queue_rows(rows, today=date(2026, 10, 1)) == []


@pytest.mark.parametrize("not_a_consumer", ["present", "feedback", "confidence", "question", "build"])
def test_next_unit_is_not_consumed_by_other_event_kinds_of_its_unit(not_a_consumer: str) -> None:
    rows = [_queue("u02", "next_unit", "2026-10-01", "2026-09-30T18:24"), _event(not_a_consumer, "u02", "2026-10-01T15:57")]
    assert due_queue_rows(rows, today=date(2026, 10, 1)) == rows[:1]


def test_next_unit_is_not_consumed_by_an_event_of_another_unit() -> None:
    rows = [_queue("u02", "next_unit", "2026-10-01", "2026-09-30T18:24"), _event("attempt", "u01", "2026-10-01T15:57")]
    assert due_queue_rows(rows, today=date(2026, 10, 1)) == rows[:1]


def test_an_event_timestamped_before_the_queue_row_does_not_consume_it() -> None:
    rows = [_event("attempt", "u02", "2026-09-30T17:00"), _queue("u02", "next_unit", "2026-10-01", "2026-09-30T18:24")]
    assert due_queue_rows(rows, today=date(2026, 10, 1)) == rows[1:]


def test_an_event_in_the_same_minute_as_the_queue_row_does_not_consume_it() -> None:
    rows = [_queue("u02", "next_unit", "2026-10-01", "2026-09-30T18:24"), _event("attempt", "u02", "2026-09-30T18:24")]
    assert due_queue_rows(rows, today=date(2026, 10, 1)) == rows[:1]


@pytest.mark.parametrize("consumer", ["start", "attempt"])
def test_revisit_is_consumed_by_a_later_start_or_attempt(consumer: str) -> None:
    rows = [_queue("u01", "revisit", "2026-10-02", "2026-10-01T18:14"), _event(consumer, "u01", "2026-10-03T09:00")]
    assert due_queue_rows(rows, today=date(2026, 10, 3)) == []


def test_revisit_is_not_consumed_by_a_probe_item() -> None:
    rows = [
        _queue("u01", "revisit", "2026-10-02", "2026-10-01T18:14"),
        _event("probe-item", "u01", "2026-10-03T09:00", which="probe-b"),
    ]
    assert due_queue_rows(rows, today=date(2026, 10, 3)) == rows[:1]


def test_delayed_probe_is_consumed_by_a_later_probe_item_of_the_delayed_side() -> None:
    rows = [
        _queue("u01", "delayed_probe", "2026-10-07", "2026-09-30T18:24"),
        _event("probe-item", "u01", "2026-10-14T09:00", which="probe-b"),
    ]
    assert due_queue_rows(rows, today=date(2026, 10, 14)) == []


@pytest.mark.parametrize(
    "other",
    [
        _event("probe-item", "u01", "2026-10-14T09:00", which="probe-a"),
        _event("probe-item", "u01", "2026-10-14T09:00", which="probe-c"),
        _event("attempt", "u01", "2026-10-14T09:00"),
        _event("start", "u01", "2026-10-14T09:00"),
    ],
)
def test_delayed_probe_is_not_consumed_by_anything_but_a_delayed_side_probe_item(other: dict[str, str]) -> None:
    rows = [_queue("u01", "delayed_probe", "2026-10-07", "2026-09-30T18:24"), other]
    assert due_queue_rows(rows, today=date(2026, 10, 14)) == rows[:1]


def test_a_queue_row_laid_after_the_consuming_event_is_due_again() -> None:
    rows = [
        _queue("u01", "revisit", "2026-10-02", "2026-10-01T18:14"),
        _event("attempt", "u01", "2026-10-03T09:00"),
        _queue("u01", "revisit", "2026-10-03", "2026-10-03T10:00"),
    ]
    assert due_queue_rows(rows, today=date(2026, 10, 3)) == rows[2:]


def test_each_queue_row_is_judged_on_its_own_unit_and_kind() -> None:
    rows = [
        _queue("u02", "next_unit", "2026-10-01", "2026-09-30T18:24"),
        _queue("u01", "revisit", "2026-10-01", "2026-09-30T18:24"),
        _event("attempt", "u02", "2026-10-01T15:57"),
    ]
    assert due_queue_rows(rows, today=date(2026, 10, 1)) == [rows[1]]
