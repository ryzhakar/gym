"""Close the current span: append its close block to the span's session record and a span-event to its trace.

Usage: `gym records close --state "..." --open "..." --next "..."`.
HEAD and the working-tree state come from git, the time from the clock; a multi-line state separates lines with `\\n`.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime

from gym.paths import ROOT
from gym.records.check_records import close_block_findings, load_schema
from gym.records.event import append_event, current_trace


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True).stdout.rstrip("\n")


def head_line() -> str:
    dirty = git("status", "--porcelain").splitlines()
    state = "clean" if not dirty else "dirty: " + ", ".join(entry[3:] for entry in dirty)
    return f"{git('rev-parse', '--short', 'HEAD')} ({state})"


def close_block(state: str, open_items: str, next_step: str, width: int) -> str:
    def field(label: str, value: str) -> str:
        first, *rest = value.split("\\n")
        return "\n".join([label.ljust(width) + first] + [" " * width + line for line in rest])

    fields = [field("HEAD", head_line()), field("state", state), field("open", open_items), field("next", next_step)]
    return f"\n## Close — {datetime.now().strftime('%Y-%m-%dT%H:%M')}\n\n" + "\n".join(fields) + "\n"


def run(state: str, open_items: str, next_step: str) -> int:
    schema = load_schema()
    session = current_trace(opening=False).parent / "session.md"
    before = session.read_bytes() if session.exists() else None
    prefix = "" if before else f"# {session.parent.name}\n"
    block = close_block(state, open_items, next_step, schema["kinds"]["digest"]["close_label_width"])
    with session.open("a", encoding="utf-8") as handle:
        handle.write(prefix + block)
    problems = list(close_block_findings(schema, session))
    if problems:
        if before is None:
            session.unlink()
        else:
            session.write_bytes(before)
        sys.exit("refused, close block malformed: " + "; ".join(problem.message for problem in problems))
    append_event("self", "span-event", f"close; HEAD {head_line()}; next: {next_step}")
    print(f"{session}: close block written")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", required=True)
    parser.add_argument("--open", required=True, dest="open_items")
    parser.add_argument("--next", required=True, dest="next_step")
    args = parser.parse_args()
    return run(args.state, args.open_items, args.next_step)


if __name__ == "__main__":
    sys.exit(main())
