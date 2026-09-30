"""Tests for capture-recapture closure math (Chapman, Chao1) and the five-part
closure rule. Every expected number below is derived from the formula's own
definition (Seber 1982 for Chapman, Chao 1987 for Chao1) or a hand count over
the fixture rows, independently of `gym.map.estimate` — never by running the
module and copying its answer. Run: `uv run pytest tests/map/test_estimate.py`.
"""

from __future__ import annotations

import math

import pytest

from gym.map.estimate import StratumResult, chao1, chapman


def rows(stratum: str, batch: int, team_a: list[str], team_b: list[str]) -> list[dict]:
    out = []
    for q in team_a:
        out.append({"stratum": stratum, "team": "a", "question_id": q, "batch": str(batch)})
    for q in team_b:
        out.append({"stratum": stratum, "team": "b", "question_id": q, "batch": str(batch)})
    return out


# --- Chapman: closed-form check against Seber 1982's own definition ---


def test_chapman_matches_closed_form_with_overlap() -> None:
    # n1=10, n2=10, m=5: (11*11)/6 - 1, variance (11*11*5*5)/(6^2*7)
    n1, n2, m = 10, 10, 5
    expected_estimate = (n1 + 1) * (n2 + 1) / (m + 1) - 1
    expected_variance = (n1 + 1) * (n2 + 1) * (n1 - m) * (n2 - m) / ((m + 1) ** 2 * (m + 2))
    expected_se = math.sqrt(expected_variance)
    estimate, se = chapman(n1, n2, m)
    assert estimate == pytest.approx(19.166666666666668)
    assert se == pytest.approx(3.464674335917916)
    assert estimate == pytest.approx(expected_estimate)
    assert se == pytest.approx(expected_se)


def test_chapman_matches_closed_form_with_no_overlap() -> None:
    # n1=3, n2=4, m=0: (4*5)/1 - 1, variance (4*5*3*4)/(1^2*2)
    n1, n2, m = 3, 4, 0
    expected_estimate = (n1 + 1) * (n2 + 1) / (m + 1) - 1
    expected_variance = (n1 + 1) * (n2 + 1) * (n1 - m) * (n2 - m) / ((m + 1) ** 2 * (m + 2))
    estimate, se = chapman(n1, n2, m)
    assert estimate == pytest.approx(19.0)
    assert estimate == pytest.approx(expected_estimate)
    assert se == pytest.approx(math.sqrt(expected_variance))
    assert se == pytest.approx(10.954451150103322)


def test_chapman_empty_stratum_is_zero() -> None:
    # n1=n2=m=0: (1*1)/1 - 1 = 0, variance 0/(1*2) = 0
    estimate, se = chapman(0, 0, 0)
    assert estimate == pytest.approx(0.0)
    assert se == pytest.approx(0.0)


# --- Chao1: closed-form check against Chao 1987's own definition ---


def test_chao1_matches_closed_form() -> None:
    # seen=15, f1=10, f2=5: 15 + 10^2/(2*5) = 25; ratio=2, var=5*(0.5*4+8+0.25*16)=70
    seen, f1, f2 = 15, 10, 5
    expected_estimate = seen + f1**2 / (2 * f2)
    ratio = f1 / f2
    expected_variance = f2 * (0.5 * ratio**2 + ratio**3 + 0.25 * ratio**4)
    result = chao1(seen, f1, f2)
    assert result is not None
    estimate, se = result
    assert estimate == pytest.approx(25.0)
    assert estimate == pytest.approx(expected_estimate)
    assert se == pytest.approx(math.sqrt(expected_variance))
    assert se == pytest.approx(8.366600265340756)


def test_chao1_undefined_when_f2_is_zero() -> None:
    # f2=0 (no doubletons): estimate is undefined by the formula's own definition
    assert chao1(seen=7, f1=7, f2=0) is None


# --- StratumResult: hand-computable capture-recapture inputs, from rows ---


def test_stratum_result_with_known_overlap() -> None:
    # team a: q1..q10 (n1=10); team b: q6..q15 (n2=10); overlap q6..q10 (m=5)
    team_a = [f"q{i}" for i in range(1, 11)]
    team_b = [f"q{i}" for i in range(6, 16)]
    result = StratumResult("core", rows("core", 1, team_a, team_b))
    assert (result.n1, result.n2, result.m) == (10, 10, 5)
    assert result.seen == 15  # |a union b| = 15 distinct questions, by hand count
    assert result.f1 == 10  # seen by exactly one team: q1-5 (a only) + q11-15 (b only)
    assert result.f2 == 5  # seen by exactly two mentions: q6-10 (both teams)
    assert result.chapman_n == pytest.approx(19.166666666666668)
    assert result.chao1_n == pytest.approx(25.0)


def test_stratum_result_empty() -> None:
    result = StratumResult("core", [])
    assert (result.n1, result.n2, result.m, result.seen) == (0, 0, 0, 0)
    assert result.f1 == 0 and result.f2 == 0
    assert result.chapman_n == pytest.approx(0.0)
    assert result.chao1_n is None  # f2=0: undefined by Chao1's own definition
    assert result.batches == []


def test_stratum_result_with_no_overlap() -> None:
    # team a: q1,q2,q3 (n1=3); team b: q4,q5,q6,q7 (n2=4); no shared question (m=0)
    team_a = ["q1", "q2", "q3"]
    team_b = ["q4", "q5", "q6", "q7"]
    result = StratumResult("core", rows("core", 1, team_a, team_b))
    assert (result.n1, result.n2, result.m) == (3, 4, 0)
    assert result.seen == 7
    assert result.f1 == 7  # every question mentioned exactly once: no doubletons
    assert result.f2 == 0
    assert result.chapman_n == pytest.approx(19.0)
    assert result.chao1_n is None  # f2=0: Chao1 is undefined with no overlap at all


# --- unseen_fraction: (estimate - seen) / estimate, by definition ---


def test_unseen_fraction_by_hand() -> None:
    result = StratumResult("core", [])
    result.seen = 98
    assert result.unseen_fraction(100.0) == pytest.approx((100.0 - 98) / 100.0)
    assert result.unseen_fraction(100.0) == pytest.approx(0.02)


def test_unseen_fraction_none_when_estimate_not_positive() -> None:
    result = StratumResult("core", [])
    assert result.unseen_fraction(None) is None
    assert result.unseen_fraction(0.0) is None
    assert result.unseen_fraction(-1.0) is None


# --- Five-part closure rule: threshold boundary at exactly 2% and just above ---


def make_result_for_rule(seen: int, estimate: float, batches: list[int]) -> StratumResult:
    result = StratumResult("core", [])
    result.seen = seen
    result.chapman_n = estimate
    result.chao1_n = estimate
    result.batches = batches
    return result


def test_rule_part1_passes_at_exactly_threshold() -> None:
    # unseen fraction (1000-980)/1000 = 0.02, threshold 0.02: <= admits the boundary
    result = make_result_for_rule(seen=980, estimate=1000.0, batches=[1, 2])
    verdict = result.rule(threshold=0.02, audit_pass={"a", "b"}, merge_check_agreement=0.95)
    assert verdict["part1_unseen_fraction"] == "PASS"
    assert verdict["verdict"] == "PASS"


def test_rule_part1_fails_just_above_threshold() -> None:
    # unseen fraction (1000-979)/1000 = 0.021, threshold 0.02: strictly over the line
    result = make_result_for_rule(seen=979, estimate=1000.0, batches=[1, 2])
    verdict = result.rule(threshold=0.02, audit_pass={"a", "b"}, merge_check_agreement=0.95)
    assert verdict["part1_unseen_fraction"] == "FAIL"
    assert verdict["verdict"] == "FAIL"


# --- Determinism: pure functions return identical output across repeated calls ---


def test_chapman_is_deterministic() -> None:
    first = chapman(10, 10, 5)
    second = chapman(10, 10, 5)
    assert first == second


def test_chao1_is_deterministic() -> None:
    first = chao1(15, 10, 5)
    second = chao1(15, 10, 5)
    assert first == second


def test_stratum_result_is_deterministic_across_construction() -> None:
    team_a = [f"q{i}" for i in range(1, 11)]
    team_b = [f"q{i}" for i in range(6, 16)]
    fixture_rows = rows("core", 1, team_a, team_b)
    first = StratumResult("core", fixture_rows)
    second = StratumResult("core", fixture_rows)
    assert (first.n1, first.n2, first.m, first.seen, first.f1, first.f2) == (
        second.n1, second.n2, second.m, second.seen, second.f1, second.f2,
    )
    assert first.chapman_n == second.chapman_n
    assert first.chao1_n == second.chao1_n
