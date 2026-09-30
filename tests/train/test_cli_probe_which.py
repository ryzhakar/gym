"""Tests for gym.train.cli's `_validate_which`: `gym train probe stage|grade` accepts `immediate`,
`delayed`, or a literal side name matching `probe-[a-z]` (owner ruling, 2026-09-30: a unit may
carry a third probe side, `probe-c`, for a repeat of the unit)."""
from __future__ import annotations

import pytest
import typer

from gym.train.cli import _validate_which


@pytest.mark.parametrize("which", ["immediate", "delayed", "probe-a", "probe-b", "probe-c", "probe-z"])
def test_validate_which_accepts_aliases_and_any_literal_side(which: str) -> None:
    _validate_which(which)  # raises on refusal; no return value to assert


@pytest.mark.parametrize("which", ["tomorrow", "probe-ab", "probe-1", "probe", ""])
def test_validate_which_refuses_anything_else(which: str) -> None:
    with pytest.raises(typer.BadParameter):
        _validate_which(which)
