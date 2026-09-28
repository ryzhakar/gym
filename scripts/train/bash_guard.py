"""PreToolUse hook: refuses shell chaining in a trainer-session Bash call, and pins `cargo`'s cwd to the unit's crate.

Usage (wired by `session.py`'s launch command, not run by hand): a Claude Code `PreToolUse` hook for
the `Bash` tool, `uv run python scripts/train/bash_guard.py --crate <CRATE>`. Reads the hook's JSON on
stdin, writes one `hookSpecificOutput.permissionDecision` line on stdout.

Two gaps the permission-pattern layer alone leaves open (`allowlist.md` § "Open points", both
`default, unmeasured`): a prefix pattern like `cargo test*` still admits shell chaining after it
(`cargo test; cat key/x`), and a permission pattern cannot pin a command's cwd. This hook closes
both: it denies any Bash command containing `;`, `&&`, `||`, `|`, `>`, or a backtick, and denies a
`cargo` command whose cwd is not the crate it was launched for.
"""
from __future__ import annotations

import argparse
import json
import sys

CHAIN_TOKENS = [";", "&&", "||", "|", ">", "`"]


def decision(verdict: str, reason: str) -> dict:
    return {"hookSpecificOutput": {"permissionDecision": verdict, "permissionDecisionReason": reason}}


def check(command: str, cwd: str, crate: str) -> dict:
    for token in CHAIN_TOKENS:
        if token in command:
            return decision("deny", f"chaining token {token!r} is not allowed in a trainer session Bash call")
    if command.strip().startswith("cargo") and cwd.rstrip("/") != crate.rstrip("/"):
        return decision("deny", f"cargo must run with cwd {crate}, not {cwd!r}")
    return decision("allow", "no chaining token, cwd matches the crate")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--crate", required=True)
    args = parser.parse_args(argv[1:])
    payload = json.load(sys.stdin)
    command = payload.get("tool_input", {}).get("command", "")
    cwd = payload.get("cwd", "")
    print(json.dumps(check(command, cwd, args.crate)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
