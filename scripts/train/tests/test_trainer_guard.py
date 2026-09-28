"""Tests for scripts/train/hooks/trainer_guard.py: the trainer session's second backstop, on top of
the permission list, against chaining, key/probe-* path references, and a wrong cargo cwd.

Run: `uv run pytest scripts/train/tests/test_trainer_guard.py`.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "hooks"))

import trainer_guard  # noqa: E402

CRATE = "/Users/ryzhakar/pp/gym/training/rust/u01"
HOOK_PATH = Path(__file__).resolve().parents[1] / "hooks" / "trainer_guard.py"


def verdict(tool_name: str, tool_input: dict, cwd: str = CRATE, crate: str = CRATE) -> "dict | None":
    return trainer_guard.check(tool_name, tool_input, cwd, crate)


@pytest.mark.parametrize("token", [";", "&&", "||", "|", ">", "<", "`", "$(", "\n"])
def test_chained_bash_command_is_denied(token: str) -> None:
    command = f"cargo test --manifest-path {CRATE}/Cargo.toml {token} cat {CRATE}/../items/u01/key/x"
    result = verdict("Bash", {"command": command})
    assert result is not None
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_bash_naming_a_key_path_is_denied_even_without_chaining() -> None:
    result = verdict("Bash", {"command": "cat training/rust/items/u01/key/solution.rs"})
    assert result is not None
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert "key" in result["hookSpecificOutput"]["permissionDecisionReason"]


def test_the_exact_reported_command_substitution_gap_is_denied() -> None:
    """team lead, 2026-09-28: `cargo test --manifest-path training/rust/u01/Cargo.toml
    $(cat training/rust/items/u01/key/x)` — a command substitution smuggling a key/ read."""
    command = "cargo test --manifest-path training/rust/u01/Cargo.toml $(cat training/rust/items/u01/key/x)"
    result = verdict("Bash", {"command": command})
    assert result is not None
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_a_second_line_with_no_key_reference_is_still_denied() -> None:
    """A bare newline (two Bash statements in one call) is denied on its own — not only when the
    second line happens to reference key/, which would let a key-free second command through."""
    command = "cargo test --manifest-path training/rust/u01/Cargo.toml\nrm -rf /tmp/whatever"
    result = verdict("Bash", {"command": command})
    assert result is not None
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert "chaining" in result["hookSpecificOutput"]["permissionDecisionReason"]


def test_bash_naming_a_probe_path_is_denied() -> None:
    result = verdict("Bash", {"command": "cat training/rust/items/u01/probe-a/prompt.md"})
    assert result is not None
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_cargo_with_the_wrong_cwd_is_denied() -> None:
    result = verdict("Bash", {"command": "cargo test"}, cwd="/tmp/elsewhere", crate=CRATE)
    assert result is not None
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_plain_cargo_test_with_manifest_path_is_allowed() -> None:
    result = verdict("Bash", {"command": f"cargo test --manifest-path {CRATE}/Cargo.toml"})
    assert result is None


def test_the_logger_call_is_allowed() -> None:
    command = (
        "uv run python /Users/ryzhakar/pp/gym/scripts/train/log.py turn "
        "--session s --n 1 --kind hint-1 --item x --request hint"
    )
    result = verdict("Bash", {"command": command}, cwd="/anywhere")
    assert result is None


def test_read_of_a_key_path_is_denied() -> None:
    result = verdict("Read", {"file_path": f"{CRATE}/../items/u01/probe-a/key/solution.rs"})
    assert result is not None
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_read_of_a_probe_path_is_denied() -> None:
    result = verdict("Read", {"file_path": "/Users/ryzhakar/pp/gym/training/rust/items/u01/probe-b/key/tests.rs"})
    assert result is not None
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_glob_touching_key_is_denied() -> None:
    result = verdict("Glob", {"pattern": "**/key/**"})
    assert result is not None
    assert result["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_read_of_an_allowed_path_is_untouched() -> None:
    result = verdict("Read", {"file_path": "/Users/ryzhakar/pp/gym/training/rust/items/u01/attempt.md"})
    assert result is None


def test_main_denies_a_chained_bash_command_over_stdin() -> None:
    payload = json.dumps({"tool_name": "Bash", "tool_input": {"command": "cargo test; cat key/x"}, "cwd": CRATE})
    result = subprocess.run(
        [sys.executable, str(HOOK_PATH), "--crate", CRATE], input=payload, capture_output=True, text=True, check=True
    )
    decision = json.loads(result.stdout)
    assert decision["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_main_denies_a_read_of_a_key_path_over_stdin() -> None:
    payload = json.dumps({"tool_name": "Read", "tool_input": {"file_path": "training/rust/items/u01/key/x"}, "cwd": CRATE})
    result = subprocess.run(
        [sys.executable, str(HOOK_PATH), "--crate", CRATE], input=payload, capture_output=True, text=True, check=True
    )
    decision = json.loads(result.stdout)
    assert decision["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_main_prints_nothing_for_a_clean_call() -> None:
    payload = json.dumps({"tool_name": "Bash", "tool_input": {"command": f"cargo check --manifest-path {CRATE}/Cargo.toml"}, "cwd": CRATE})
    result = subprocess.run(
        [sys.executable, str(HOOK_PATH), "--crate", CRATE], input=payload, capture_output=True, text=True, check=True
    )
    assert result.stdout.strip() == ""
