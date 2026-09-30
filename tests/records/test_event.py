"""gym records event: the line-shape refusal on a malformed kind, against a tmp copy of the trace tree."""

from __future__ import annotations

import shutil

import pytest

from gym.paths import ROOT
from gym.records import event as event_module


def test_malformed_kind_is_refused_before_any_write(tmp_path, monkeypatch) -> None:
    history_copy = tmp_path / "orchestration_log" / "history"
    shutil.copytree(ROOT / "docs/orchestration_log/history", history_copy)
    monkeypatch.setattr(event_module, "ORCHESTRATION", tmp_path / "orchestration_log")

    with pytest.raises(SystemExit) as excinfo:
        event_module.append_event("owner", "not-a-real-kind", "should never be written")

    assert "refused" in str(excinfo.value)
    for trace in history_copy.glob("*/events.md"):
        assert "should never be written" not in trace.read_text(encoding="utf-8")
