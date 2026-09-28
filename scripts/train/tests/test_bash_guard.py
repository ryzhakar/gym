"""Tests for bash_guard.py: the PreToolUse hook that closes what a permission pattern can't pin —
shell chaining after an allowed `cargo` prefix, and a `cargo` command's cwd.

Run: `uv run pytest scripts/train/tests/test_bash_guard.py`.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import bash_guard  # noqa: E402

CRATE = "/Users/ryzhakar/pp/gym/training/rust/unit-1"


@pytest.mark.parametrize("token", [";", "&&", "||", "|", ">", "`"])
def test_chaining_token_is_denied(token: str) -> None:
    result = bash_guard.check(f"cargo test {token} cat key/x", CRATE, CRATE)
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert token in result["hookSpecificOutput"]["permissionDecisionReason"]


def test_cargo_with_the_right_cwd_is_allowed() -> None:
    result = bash_guard.check("cargo test", CRATE, CRATE)
    assert result["hookSpecificOutput"]["permissionDecision"] == "allow"


def test_cargo_with_the_wrong_cwd_is_denied() -> None:
    result = bash_guard.check("cargo test", "/tmp/somewhere-else", CRATE)
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert "cwd" in result["hookSpecificOutput"]["permissionDecisionReason"]


def test_the_logger_call_is_allowed() -> None:
    result = bash_guard.check(
        "uv run python /Users/ryzhakar/pp/gym/scripts/train/log.py turn --session s --n 1 --kind hint-1 --item x --request hint",
        "/anywhere",
        CRATE,
    )
    assert result["hookSpecificOutput"]["permissionDecision"] == "allow"


def test_main_reads_stdin_and_prints_a_decision(tmp_path: Path) -> None:
    payload = json.dumps({"tool_input": {"command": "cargo test; cat key/x"}, "cwd": CRATE})
    result = subprocess.run(
        [sys.executable, str(Path(__file__).resolve().parents[1] / "bash_guard.py"), "--crate", CRATE],
        input=payload,
        capture_output=True,
        text=True,
        check=True,
    )
    decision = json.loads(result.stdout)
    assert decision["hookSpecificOutput"]["permissionDecision"] == "deny"
