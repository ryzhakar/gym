"""Tests for gym.train.schema: field parsing and the four line-refusal cases the task names."""
from __future__ import annotations

import pytest

from gym.train.schema import KINDS, parse_fields, validate_fields


def test_parse_fields_splits_simple_tokens() -> None:
    assert parse_fields("unit=u1 item=x result=pass") == {"unit": "u1", "item": "x", "result": "pass"}


def test_parse_fields_note_absorbs_the_rest_of_the_line() -> None:
    fields = parse_fields("unit=u1 item=x note=ladder gap: u1 after level 2")
    assert fields == {"unit": "u1", "item": "x", "note": "ladder gap: u1 after level 2"}


def test_parse_fields_note_is_absorbed_even_with_embedded_equals_signs() -> None:
    fields = parse_fields("unit=u1 note=a=b c=d")
    assert fields == {"unit": "u1", "note": "a=b c=d"}


def test_parse_fields_refuses_a_token_with_no_equals_sign() -> None:
    with pytest.raises(ValueError, match="not 'field=value'"):
        parse_fields("unit=u1 bogus")


def test_parse_fields_refuses_a_field_given_twice() -> None:
    with pytest.raises(ValueError, match="given twice"):
        parse_fields("unit=u1 unit=u2")


def test_every_kind_declares_at_least_one_field() -> None:
    assert all(KINDS[kind] for kind in KINDS)


def test_validate_fields_passes_a_complete_valid_row() -> None:
    assert validate_fields("attempt", {"unit": "u1", "item": "x", "result": "pass", "minutes": "5"}) is None


def test_validate_fields_reports_a_missing_required_field() -> None:
    error = validate_fields("attempt", {"unit": "u1", "item": "x", "result": "pass"})
    assert error is not None and "missing field(s)" in error and "minutes" in error


def test_validate_fields_reports_a_bad_enum_value() -> None:
    error = validate_fields("attempt", {"unit": "u1", "item": "x", "result": "maybe", "minutes": "5"})
    assert error is not None and "not one of" in error


def test_validate_fields_reports_a_bad_number() -> None:
    error = validate_fields("attempt", {"unit": "u1", "item": "x", "result": "pass", "minutes": "soon"})
    assert error is not None and "not a number" in error


def test_validate_fields_tolerates_an_unknown_extra_field() -> None:
    """Only a missing required field or a bad value on one present is refused; an extra field
    (a probe's own `continuous`, or any other) is never rejected here."""
    error = validate_fields("attempt", {"unit": "u1", "item": "x", "result": "pass", "minutes": "5", "extra": "z"})
    assert error is None


def test_ladder_gap_requires_a_nonempty_note() -> None:
    error = validate_fields("ladder-gap", {"unit": "u1", "item": "x", "note": ""})
    assert error is not None and "empty" in error


def test_confidence_value_must_be_0_to_4() -> None:
    assert validate_fields("confidence", {"unit": "u1", "item": "x", "value": "4"}) is None
    error = validate_fields("confidence", {"unit": "u1", "item": "x", "value": "5"})
    assert error is not None and "not one of" in error


def test_start_kind_matches_gym_trainer_mds_unit_opening_turn() -> None:
    assert validate_fields("start", {"unit": "u1"}) is None
    error = validate_fields("start", {})
    assert error is not None and "unit" in error


def test_question_kind_matches_gym_trainer_mds_question_turn() -> None:
    assert validate_fields("question", {"unit": "u1", "item": "x"}) is None


def test_answer_kind_matches_gym_trainer_mds_logged_breach_turn() -> None:
    assert validate_fields("answer", {"unit": "u1", "item": "x"}) is None


def test_baseline_item_logs_unit_baseline_needing_no_schema_change() -> None:
    """A baseline item has no unit of its own; `unit=baseline` satisfies every kind's plain
    `nonempty` check on `unit` like any other unit id — no new schema entry required."""
    assert validate_fields("present", {"unit": "baseline", "item": "b1-own"}) is None
    assert validate_fields("attempt", {"unit": "baseline", "item": "b1-own", "result": "pass", "minutes": "3"}) is None
