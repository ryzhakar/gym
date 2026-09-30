"""Tests for gym.train.schema: field parsing and the four line-refusal cases the task names."""
from __future__ import annotations

import pytest

from gym.train.schema import KINDS, quote_value, parse_fields, validate_fields


def test_parse_fields_splits_simple_tokens() -> None:
    assert parse_fields("unit=u1 item=x result=pass") == {"unit": "u1", "item": "x", "result": "pass"}


def test_quote_value_leaves_a_plain_value_bare() -> None:
    assert quote_value("u1") == "u1"
    assert quote_value("") == ""


def test_quote_value_quotes_and_escapes_a_value_with_spaces() -> None:
    assert quote_value("move semantics") == '"move semantics"'


def test_quote_value_escapes_an_embedded_double_quote_and_backslash() -> None:
    assert quote_value('has "quotes" inside') == '"has \\"quotes\\" inside"'
    assert quote_value("back\\slash") == '"back\\\\slash"'


def test_quote_value_quotes_a_lone_single_quote_even_without_a_space() -> None:
    """A bare, unquoted `'` breaks `shlex.split` outright (an unterminated quote), regardless of
    whether it's next to a space — `quote_value` must catch it too, not just whitespace."""
    assert quote_value("don't") == '"don\'t"'


def test_parse_fields_reads_a_quoted_value_holding_spaces_back_out() -> None:
    """`gym.train.events.build_line` writes `principle=quote_value(...)`; `parse_fields` (via
    `shlex.split`) is what reads that back — round-trip, not just the writer's own escaping."""
    fields = parse_fields('unit=u1 item=x principle="move, don\'t copy" request=none')
    assert fields == {"unit": "u1", "item": "x", "principle": "move, don't copy", "request": "none"}


def test_parse_fields_reads_a_quoted_value_with_an_embedded_equals_sign() -> None:
    fields = parse_fields('unit=u1 note="a=b c=d"')
    assert fields == {"unit": "u1", "note": "a=b c=d"}


def test_parse_fields_refuses_a_token_with_no_equals_sign() -> None:
    with pytest.raises(ValueError, match="not 'field=value'"):
        parse_fields("unit=u1 bogus")


def test_parse_fields_refuses_a_field_given_twice() -> None:
    """Quoting removes the ambiguity a continuation-based parser had here (an earlier version of
    this function could only absorb a repeat as more free text instead of refusing it) —
    `shlex.split` draws token boundaries exactly, so a real duplicate is always caught now."""
    with pytest.raises(ValueError, match="given twice"):
        parse_fields("unit=u1 unit=u2")


def test_parse_fields_refuses_an_unterminated_quote() -> None:
    with pytest.raises(ValueError, match="not shlex-parseable"):
        parse_fields('unit=u1 note="unterminated')


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


def test_validate_fields_refuses_an_unknown_extra_field() -> None:
    """Team lead ruling (2026-09-30): an unrecognized field name is refused, `note` excepted — the
    old behaviour (silently tolerating it) let a real bug through: `gym train log ... probe-item
    ... continuous=0.5` used to write and round-trip a field this schema never declared."""
    error = validate_fields("attempt", {"unit": "u1", "item": "x", "result": "pass", "minutes": "5", "extra": "z"})
    assert error is not None and "unknown field(s)" in error and "extra" in error


def test_validate_fields_still_allows_note_on_any_kind() -> None:
    """`note` is the one exception to the unknown-field refusal: legal free text on any kind,
    required only by `ladder-gap`."""
    assert validate_fields("present", {"unit": "u1", "item": "x", "note": "an aside"}) is None


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


def test_any_kind_accepts_an_optional_request_field() -> None:
    """Team lead ruling (2026-09-30): a hint or answer turn can carry the learner's own ask on the
    same line, so `request` is legal (and validated) on any kind, not only the dedicated `request`
    kind itself."""
    assert validate_fields(
        "hint", {"unit": "u1", "item": "x", "level": "1", "source": "supplied", "request": "hint"}
    ) is None
    assert validate_fields(
        "answer", {"unit": "u1", "item": "x", "request": "answer"}
    ) is None


def test_optional_request_field_is_still_validated_against_its_enum() -> None:
    error = validate_fields("hint", {"unit": "u1", "item": "x", "level": "1", "source": "supplied", "request": "solution"})
    assert error is not None and "not one of" in error


def test_request_kind_itself_still_requires_its_own_request_field() -> None:
    """'keep the request kind too': the dedicated `request` kind is unaffected by `request`
    becoming a globally optional field on every other kind."""
    error = validate_fields("request", {"unit": "u1", "item": "x"})
    assert error is not None and "missing field(s)" in error and "request" in error


def test_probe_item_accepts_an_optional_fraction_field_in_0_to_1() -> None:
    required = {"unit": "u1", "which": "probe-a", "problem": "p1", "result": "pass", "minutes": "5"}
    assert validate_fields("probe-item", {**required, "fraction": "0.6667"}) is None
    assert validate_fields("probe-item", {**required, "fraction": "0"}) is None
    assert validate_fields("probe-item", {**required, "fraction": "1"}) is None


def test_probe_item_fraction_outside_0_to_1_is_refused() -> None:
    required = {"unit": "u1", "which": "probe-a", "problem": "p1", "result": "pass", "minutes": "5"}
    error = validate_fields("probe-item", {**required, "fraction": "1.5"})
    assert error is not None and "outside [0.0, 1.0]" in error
    error = validate_fields("probe-item", {**required, "fraction": "-0.1"})
    assert error is not None and "outside [0.0, 1.0]" in error


def test_probe_item_accepts_an_optional_over_cap_field() -> None:
    """Team lead ruling (2026-09-30): the per-probe cap `gym train probe grade` dropped along with
    the interactive wait is restored as data on `probe-item` — recorded, never enforced."""
    required = {"unit": "u1", "which": "probe-a", "problem": "p1", "result": "pass", "minutes": "5"}
    assert validate_fields("probe-item", {**required, "over_cap": "yes"}) is None
    assert validate_fields("probe-item", {**required, "over_cap": "no"}) is None


def test_probe_item_over_cap_must_be_yes_or_no() -> None:
    required = {"unit": "u1", "which": "probe-a", "problem": "p1", "result": "pass", "minutes": "5"}
    error = validate_fields("probe-item", {**required, "over_cap": "maybe"})
    assert error is not None and "not one of" in error


def test_over_cap_is_not_recognized_on_a_kind_other_than_probe_item() -> None:
    error = validate_fields("attempt", {"unit": "u1", "item": "x", "result": "pass", "minutes": "5", "over_cap": "yes"})
    assert error is not None and "unknown field(s)" in error and "over_cap" in error


def test_probe_item_accepts_an_optional_total_minutes_field() -> None:
    """Team lead ruling (2026-09-30): once `minutes` became per-problem (mtime-based), `over_cap`
    needed a separate shared quantity to judge against — `total_minutes`, grade time minus
    `probe-start` time, the same on every problem in one `grade` call."""
    required = {"unit": "u1", "which": "probe-a", "problem": "p1", "result": "pass", "minutes": "5"}
    assert validate_fields("probe-item", {**required, "total_minutes": "5.32"}) is None
    assert validate_fields("probe-item", {**required, "total_minutes": "0"}) is None


def test_probe_item_total_minutes_below_0_is_refused() -> None:
    required = {"unit": "u1", "which": "probe-a", "problem": "p1", "result": "pass", "minutes": "5"}
    error = validate_fields("probe-item", {**required, "total_minutes": "-1"})
    assert error is not None and "below 0" in error


def test_total_minutes_is_not_recognized_on_a_kind_other_than_probe_item() -> None:
    error = validate_fields("attempt", {"unit": "u1", "item": "x", "result": "pass", "minutes": "5", "total_minutes": "5"})
    assert error is not None and "unknown field(s)" in error and "total_minutes" in error


def test_fraction_is_not_recognized_on_a_kind_other_than_probe_item() -> None:
    """`fraction` is `probe-item`'s own optional field, not global like `request` — an unrelated
    kind carrying it is refused as an unknown field for that kind."""
    error = validate_fields("attempt", {"unit": "u1", "item": "x", "result": "pass", "minutes": "5", "fraction": "9"})
    assert error is not None and "unknown field(s)" in error and "fraction" in error


def test_probe_item_refuses_the_old_ad_hoc_continuous_field() -> None:
    """The exact bug reported: `gym train log ... probe-item ... continuous=0.5` used to be
    accepted, `continuous` never having been declared anywhere in this schema (only `fraction`
    is `probe-item`'s own optional field, since the second-pass rename)."""
    required = {"unit": "u1", "which": "probe-a", "problem": "p1", "result": "pass", "minutes": "5"}
    error = validate_fields("probe-item", {**required, "continuous": "0.5"})
    assert error is not None and "unknown field(s)" in error and "continuous" in error


def test_close_accepts_an_optional_probe_minutes_field() -> None:
    """Team lead ruling (2026-09-30): `close` may optionally carry `probe_minutes`, a
    non-negative number — the one old `sessions.csv` column this schema gives a home to."""
    required = {"minutes": "30", "units": "u1", "interruptions": "0", "assistant_closed": "yes"}
    assert validate_fields("close", {**required, "probe_minutes": "8.5"}) is None
    assert validate_fields("close", {**required, "probe_minutes": "0"}) is None


def test_close_probe_minutes_below_0_is_refused() -> None:
    required = {"minutes": "30", "units": "u1", "interruptions": "0", "assistant_closed": "yes"}
    error = validate_fields("close", {**required, "probe_minutes": "-1"})
    assert error is not None and "below 0" in error


def test_close_probe_minutes_is_not_recognized_on_an_unrelated_kind() -> None:
    error = validate_fields("attempt", {"unit": "u1", "item": "x", "result": "pass", "minutes": "5", "probe_minutes": "8"})
    assert error is not None and "unknown field(s)" in error and "probe_minutes" in error


def test_probe_start_which_accepts_any_literal_probe_side_name() -> None:
    for side in ("probe-a", "probe-b", "probe-c", "probe-z"):
        fields = {"unit": "u1", "which": side, "problems": "p1,p2"}
        assert validate_fields("probe-start", fields) is None


def test_probe_item_which_accepts_any_literal_probe_side_name() -> None:
    for side in ("probe-a", "probe-b", "probe-c"):
        fields = {"unit": "u1", "which": side, "problem": "p1", "result": "pass", "minutes": "5"}
        assert validate_fields("probe-item", fields) is None


def test_probe_item_which_refuses_the_old_immediate_delayed_aliases() -> None:
    """Team lead ruling (2026-09-30): a stored event's `which` is always the literal, resolved
    side name (`gym.train.probe.resolve_side`) — `immediate`/`delayed` are CLI-facing aliases
    only, never a value an event line itself carries."""
    fields = {"unit": "u1", "which": "immediate", "problem": "p1", "result": "pass", "minutes": "5"}
    error = validate_fields("probe-item", fields)
    assert error is not None and "which" in error


def test_probe_item_which_refuses_a_shape_that_is_not_a_single_letter_side() -> None:
    for bad in ("probe-ab", "probe-1", "probe-", "probe"):
        fields = {"unit": "u1", "which": bad, "problem": "p1", "result": "pass", "minutes": "5"}
        error = validate_fields("probe-item", fields)
        assert error is not None and "which" in error


def test_probe_item_which_accepts_the_literal_baseline_value() -> None:
    """`gym train baseline grade` reuses `probe-item` for its own result, `which=baseline` — not a
    probe side, so `probe-start`'s own `which` stays unwidened (a baseline item is never staged
    through `probe-start`)."""
    fields = {"unit": "baseline", "which": "baseline", "problem": "b1-own", "result": "pass", "minutes": "5"}
    assert validate_fields("probe-item", fields) is None


def test_probe_start_which_still_refuses_the_literal_baseline_value() -> None:
    fields = {"unit": "baseline", "which": "baseline", "problems": "b1-own"}
    error = validate_fields("probe-start", fields)
    assert error is not None and "which" in error


def test_procedure_requires_note_and_allows_an_optional_unit() -> None:
    assert validate_fields("procedure", {"note": "explained cargo test flags"}) is None
    assert validate_fields("procedure", {"note": "explained the cap", "unit": "u1"}) is None


def test_procedure_refuses_a_missing_note() -> None:
    error = validate_fields("procedure", {"unit": "u1"})
    assert error is not None and "note" in error
