"""Open and close a training session: due delayed probes, the trainer hand-off, the closing rows.

Usage:
  `uv run python scripts/train/session.py open [--items-root DIR]`
  `uv run python scripts/train/session.py close --minutes M --units "u1;u2" --trainer-model opus
      --probe-minutes P --assistant-closed true|false --interruptions N --next-unit u3`

`open` runs every due delayed probe first (queue.csv, kind `delayed_probe`, due today or earlier,
skipping units already probed at that due date — fable-plan.md § 3 "Session n ≥ 1"), then prints the
record tail and the command that starts the trainer on the queued next unit, under a tool allowlist
scoped to that unit (`trainer_launch_command`). `close` writes the session row and the queue rows:
one delayed probe due in 7 days per unit practiced (§ 6 O3, a first-protocol default, unmeasured)
and one `next_unit` row.

`--items-root` (`training/rust/items`, decided: team lead, 2026-09-28) holds `<unit>/` directories
in P3's layout (attempt.md, example.md, reuse-1..2/, unshown/, probe-a/, probe-b/, hints.yaml, key/)
plus `baseline/<item>/` for the unaided baseline set.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import shlex
import subprocess
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).parent))
import record_schema  # noqa: E402
from log import append_row, build_row  # noqa: E402
from probe import run_probe  # noqa: E402
from record_schema import ROOT, TIMESTAMP_FORMAT, file_path  # noqa: E402

TRAINING_ROOT = ROOT / "training/rust"
DEFAULT_ITEMS_ROOT = ROOT / "training/rust/items"  # decided: team lead, 2026-09-28
TRAINER_GUARD = ROOT / "scripts/train/hooks/trainer_guard.py"

# The trainer's own session's permission rules (team lead, 2026-09-28), read from
# docs/orchestration_log/recon/2026-09-28/trainer/agent/allowlist.md — this is that spec's
# "Claude Code permission form" turned into the settings this launch actually applies, with UNIT,
# CRATE and RECORD substituted per unit. Not parsed from the file at run time: the file is P1's
# prose account of the same team-lead ruling this reads directly, so the two can't format-drift but
# also aren't mechanically coupled — flagged, not silently assumed reconciled.
KEY_DENY_PATTERN = "Read(**/key/**)"


def unit_paths(unit: str) -> tuple[str, str, str]:
    """UNIT, CRATE, RECORD — absolute, as `allowlist.md` names them."""
    unit_dir = str(ROOT / "training/rust/items" / unit)
    crate = str(TRAINING_ROOT / unit)
    record = str(record_schema.RECORD_DIR)
    return unit_dir, crate, record


def permission_settings(unit: str) -> dict:
    """`allowlist.md` § Allow/Deny, substituted for `unit`: a `--settings` payload, `permissions` plus
    the `trainer_guard.py` `PreToolUse` hook for what a permission pattern alone cannot pin (chaining
    after a `cargo check*`/`cargo test*` prefix; a command's cwd — allowlist.md § Open points 1, 3),
    matched against `Bash|Read|Glob` as a second, hook-level check on top of the Read/Glob deny
    patterns below (P1 eval v0.1, "Remaining findings" — belt-and-suspenders, not a replacement)."""
    unit_dir, crate, record = unit_paths(unit)
    allow = [
        f"Read({unit_dir}/attempt.md)",
        f"Read({unit_dir}/example.md)",
        f"Read({unit_dir}/hints.yaml)",
        f"Read({unit_dir}/reuse-1/**)",
        f"Read({unit_dir}/reuse-2/**)",
        f"Read({unit_dir}/unshown/**)",
        f"Read({crate}/**)",
        f"Read({record}/**)",
        f"Glob({crate}/**)",
        f"Bash(uv run python {ROOT}/scripts/train/log.py turn *)",
        "Bash(cargo check*)",
        "Bash(cargo test*)",
    ]
    deny = [
        KEY_DENY_PATTERN,
        "Glob(**/key/**)",
        "Read(**/probe-*/**)",
        "Glob(**/probe-*/**)",
        "Bash(cargo run*)",
        "Bash(cargo build*)",
        "Bash(cargo add*)",
        "Bash(cargo install*)",
        "Bash(git *)",
    ]
    return {
        "permissions": {"allow": allow, "deny": deny},
        "hooks": {
            "PreToolUse": [
                {
                    "matcher": "Bash|Read|Glob",
                    "hooks": [
                        {
                            "type": "command",
                            "command": f"uv run python {TRAINER_GUARD} --crate {shlex.quote(crate)}",
                            "timeout": 5,
                        }
                    ],
                }
            ]
        },
    }


def new_session_id() -> str:
    return datetime.now().strftime(TIMESTAMP_FORMAT)


def write_settings_file(unit: str) -> Path:
    """The unit's permission settings, generated fresh on every launch (never committed, same as the
    crate tree it sits beside): `--settings` takes a path or inline JSON (`claude --help`) — a file
    keeps the printed launch command short and lets the settings be inspected before the trainer runs."""
    _unit_dir, crate, _record = unit_paths(unit)
    path = Path(crate) / ".trainer-settings.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(permission_settings(unit), indent=2), encoding="utf-8")
    return path


def trainer_launch_command(unit: str) -> str:
    """The trainer hand-off command: the unit's permission settings in a generated file (`--settings
    <path>`), plus `dontAsk` so a call outside them is refused outright, never put to the learner (no
    lock-out exists otherwise — fable-plan.md § 5 sessions.assistant_closed). The trailing prompt
    carries the session id, unit id, item directory and record tail the trainer's own definition
    expects."""
    unit_dir, _crate, record = unit_paths(unit)
    session_id = new_session_id()
    settings_path = write_settings_file(unit)
    prompt = (
        f"session {session_id}; unit {unit}; items {unit_dir}; record {record}\n"
        "sessions tail:\n" + "\n".join(record_tail("sessions")) + "\n"
        "items tail:\n" + "\n".join(record_tail("items"))
    )
    parts = [
        "claude",
        "--agent",
        "rust-trainer",
        "--permission-mode",
        "dontAsk",
        "--settings",
        str(settings_path),
        prompt,
    ]
    return " ".join(shlex.quote(part) for part in parts)


def workspace_path() -> Path:
    return TRAINING_ROOT / "Cargo.toml"


def read_members(path: Path) -> list[str]:
    if not path.is_file():
        return []
    match = re.search(r"members\s*=\s*\[(.*?)\]", path.read_text(encoding="utf-8"), re.DOTALL)
    if not match:
        return []
    return [item.strip().strip('"') for item in match.group(1).split(",") if item.strip()]


def write_workspace(path: Path, members: list[str]) -> None:
    body = "".join(f'    "{member}",\n' for member in sorted(members))
    path.write_text(f"[workspace]\nmembers = [\n{body}]\n", encoding="utf-8")


def ensure_unit_crate(unit: str) -> Path:
    """The unit's member crate, created on demand and registered in the workspace, idempotently."""
    TRAINING_ROOT.mkdir(parents=True, exist_ok=True)
    workspace = workspace_path()
    if not workspace.is_file():
        write_workspace(workspace, [])
    crate_dir = TRAINING_ROOT / unit
    if not crate_dir.is_dir():
        subprocess.run(
            ["cargo", "new", "--lib", "--name", unit, str(crate_dir)],
            check=True,
            capture_output=True,
        )
    members = read_members(workspace)
    if unit not in members:
        write_workspace(workspace, [*members, unit])
    return crate_dir


def completed_delayed_probe_units() -> set[str]:
    path = file_path("items")
    if not path.is_file():
        return set()
    with path.open(encoding="utf-8", newline="") as handle:
        return {row["unit"] for row in csv.DictReader(handle) if row["kind"] == "probe-delayed"}


def due_delayed_probes() -> list[dict[str, str]]:
    path = file_path("queue")
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    today = date.today().isoformat()
    done = completed_delayed_probe_units()
    return [row for row in rows if row["kind"] == "delayed_probe" and row["due_date"] <= today and row["unit"] not in done]


def next_unit() -> "str | None":
    path = file_path("queue")
    if not path.is_file():
        return None
    with path.open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["kind"] == "next_unit"]
    return rows[-1]["unit"] if rows else None


def record_tail(name: str, lines: int = 5) -> list[str]:
    path = file_path(name)
    if not path.is_file():
        return []
    return path.read_text(encoding="utf-8").splitlines()[-lines:]


def open_session(
    items_root: Path = DEFAULT_ITEMS_ROOT,
    wait: Callable[[], None] = lambda: input(),
    clock: Callable[[], float] = time.monotonic,
) -> None:
    due = due_delayed_probes()
    for row in due:
        unit_dir = items_root / row["unit"]
        run_probe(unit_dir, "delayed", wait=wait, clock=clock)
    unit = next_unit()
    if unit:
        ensure_unit_crate(unit)
    print(f"due delayed probes run: {[row['unit'] for row in due] or 'none'}")
    print(f"next unit: {unit or 'none — run session.py close --next-unit <id> first'}")
    print("sessions tail:")
    for line in record_tail("sessions"):
        print(f"  {line}")
    print("items tail:")
    for line in record_tail("items"):
        print(f"  {line}")
    if unit:
        print(f"\nstart the trainer:\n  {trainer_launch_command(unit)}")


def gap_days_since_last_session() -> float:
    path = file_path("sessions")
    if not path.is_file():
        return 0.0
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return 0.0
    last = datetime.strptime(rows[-1]["timestamp"], TIMESTAMP_FORMAT)
    return round((datetime.now() - last).total_seconds() / 86400, 2)


def close_session(
    minutes: float,
    units: list[str],
    trainer_model: str,
    probe_minutes: float,
    assistant_closed: bool,
    interruptions: int,
    next_unit_id: str,
) -> None:
    session_row = build_row(
        "sessions",
        {
            "minutes": str(minutes),
            "gap_days": str(gap_days_since_last_session()),
            "units": ";".join(units),
            "trainer_model": trainer_model,
            "probe_minutes": str(probe_minutes),
            "assistant_closed": "true" if assistant_closed else "false",
            "interruptions": str(interruptions),
        },
    )
    append_row("sessions", session_row)
    due_date = (date.today() + timedelta(days=7)).isoformat()  # O3: first probe >= 7 days, unmeasured default
    for unit in units:
        append_row("queue", build_row("queue", {"kind": "delayed_probe", "unit": unit, "due_date": due_date}))
    append_row(
        "queue",
        build_row("queue", {"kind": "next_unit", "unit": next_unit_id, "due_date": date.today().isoformat()}),
    )


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_open = sub.add_parser("open")
    p_open.add_argument("--items-root", type=Path, default=DEFAULT_ITEMS_ROOT)

    p_close = sub.add_parser("close")
    p_close.add_argument("--minutes", type=float, required=True)
    p_close.add_argument("--units", required=True, help="';'-separated unit ids practiced this session")
    p_close.add_argument("--trainer-model", required=True)
    p_close.add_argument("--probe-minutes", type=float, required=True)
    p_close.add_argument("--assistant-closed", choices=["true", "false"], required=True)
    p_close.add_argument("--interruptions", type=int, required=True)
    p_close.add_argument("--next-unit", required=True, dest="next_unit_id")

    args = parser.parse_args(argv[1:])
    if args.command == "open":
        open_session(args.items_root)
    else:
        close_session(
            args.minutes,
            args.units.split(";"),
            args.trainer_model,
            args.probe_minutes,
            args.assistant_closed == "true",
            args.interruptions,
            args.next_unit_id,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
