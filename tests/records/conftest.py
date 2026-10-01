"""Fixtures for the records tests: a tmp copy of the journal and a clock that reads the moment a test sets."""

from __future__ import annotations

import shutil
from collections.abc import Callable
from datetime import datetime
from pathlib import Path

import pytest

from gym.paths import ROOT
from gym.records import check_records, close_span
from gym.records import event as event_module


@pytest.fixture
def history(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """A copy of the live `history/` under a tmp tree that stands in for the repo root; the records modules read the copy.

    HEAD is pinned, so a close block never depends on the live repo's git state.
    """
    orchestration = tmp_path / "docs" / "orchestration_log"
    shutil.copytree(ROOT / "docs/orchestration_log/history", orchestration / "history")
    monkeypatch.setattr(event_module, "ORCHESTRATION", orchestration)
    monkeypatch.setattr(check_records, "ORCHESTRATION", orchestration)
    monkeypatch.setattr(check_records, "ROOT", tmp_path)
    monkeypatch.setattr(close_span, "head_line", lambda: "abc1234 (clean)")
    return orchestration / "history"


@pytest.fixture
def at(monkeypatch: pytest.MonkeyPatch) -> Callable[[str], None]:
    """`at("2099-01-02T09:00")` sets the moment the clock reads in event.py and close_span.py."""

    def freeze(moment: str) -> None:
        frozen = datetime.fromisoformat(moment)

        class Frozen(datetime):
            @classmethod
            def now(cls, tz=None):  # type: ignore[override]
                return frozen

        monkeypatch.setattr(event_module, "datetime", Frozen)
        monkeypatch.setattr(close_span, "datetime", Frozen)

    return freeze
