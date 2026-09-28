"""PreToolUse hook: the trainer session's second backstop against a solution-ban breach (T8; P1 eval v0.1, "Remaining findings").

Usage (wired by `session.py`'s launch command via a generated `--settings` file, not run by hand): a
Claude Code `PreToolUse` hook matching `Bash|Read|Glob`, `uv run python
scripts/train/hooks/trainer_guard.py --crate <CRATE>`. Reads the hook's JSON on stdin, writes one
`hookSpecificOutput` line on stdout when it denies; prints nothing and exits 0 when it doesn't,
leaving the permission list's own decision (`allowlist.md`) in force.

`allowlist.md`'s permission patterns already deny `Read`/`Glob` on `**/key/**` and `**/probe-*/**`,
and allow `Bash` only for the logger and `cargo check`/`cargo test` — solid for a straight call, but
two gaps a pattern alone can't close (P1 eval v0.1 "Remaining findings", allowlist.md § Open points):
a prefix pattern like `cargo test*` still admits shell chaining after it (`cargo test; cat key/x`,
`cargo test --manifest-path ... $(cat .../key/x)`, a second line), and a permission pattern can't
pin a command's cwd. This hook closes both: `;`, `&&`, `||`, `|`, `>`, `<`, a backtick, `$(`, and a
literal newline (a second line in one Bash call) are all denied outright, regardless of what
precedes them; a Bash command naming a `key`/`probe-*` path segment is denied even with none of
those present (belt-and-suspenders on top of the permission deny, for the same path a chained
command could still reach); and a `Read`/`Glob` call on such a path is denied directly (a second
check on top of the permission list, not a replacement).
"""
from __future__ import annotations

import argparse
import json
import re
import sys

CHAIN_TOKENS = [";", "&&", "||", "|", ">", "<", "`", "$(", "\n"]


def decision(verdict: str, reason: str) -> dict:
    return {"hookSpecificOutput": {"permissionDecision": verdict, "permissionDecisionReason": reason}}


def path_touches_denied_segment(path: str) -> "str | None":
    """The first `key` or `probe-*` path segment in `path`, split on `/` and `\\`, or None."""
    for segment in re.split(r"[/\\]", path):
        if segment == "key" or re.fullmatch(r"probe-.*", segment):
            return segment
    return None


def command_denied_segment(command: str) -> "str | None":
    """The first `key`/`probe-*` segment named by any whitespace-delimited token in `command`, or None."""
    for token in command.split():
        found = path_touches_denied_segment(token)
        if found:
            return found
    return None


def check_bash(command: str, cwd: str, crate: str) -> "dict | None":
    for token in CHAIN_TOKENS:
        if token in command:
            return decision("deny", f"chaining token {token!r} is not allowed in a trainer session Bash call")
    segment = command_denied_segment(command)
    if segment:
        return decision("deny", f"command names a {segment!r} path segment, denied regardless of chaining")
    if command.strip().startswith("cargo") and cwd.rstrip("/") != crate.rstrip("/"):
        return decision("deny", f"cargo must run with cwd {crate}, not {cwd!r}")
    return None


def check_path_tool(tool_input: dict) -> "dict | None":
    """Read/Glob: every string value in `tool_input`, since the exact argument key (`file_path`,
    `pattern`, `path`, ...) is not pinned down here — a superset check, never a narrower one."""
    for value in tool_input.values():
        if isinstance(value, str):
            segment = path_touches_denied_segment(value)
            if segment:
                return decision("deny", f"path names a {segment!r} segment: {value}")
    return None


def check(tool_name: str, tool_input: dict, cwd: str, crate: str) -> "dict | None":
    if tool_name == "Bash":
        return check_bash(tool_input.get("command", ""), cwd, crate)
    if tool_name in ("Read", "Glob"):
        return check_path_tool(tool_input)
    return None


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--crate", required=True)
    args = parser.parse_args(argv[1:])
    payload = json.load(sys.stdin)
    verdict = check(payload.get("tool_name", ""), payload.get("tool_input", {}), payload.get("cwd", ""), args.crate)
    if verdict is not None:
        print(json.dumps(verdict))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
