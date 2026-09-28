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
import re
import shlex
import subprocess
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).parent))
from log import append_row, build_row  # noqa: E402
from probe import run_probe  # noqa: E402
from record_schema import ROOT, TIMESTAMP_FORMAT, file_path  # noqa: E402

TRAINING_ROOT = ROOT / "training/rust"
DEFAULT_ITEMS_ROOT = ROOT / "training/rust/items"  # decided: team lead, 2026-09-28

# Deny/allow rules for the trainer's own session (team lead, 2026-09-28): no read of any item's
# key/, and Bash confined to the append-only logger and to cargo check/test in the unit's own crate.
# The trainer's agent definition (P1) writes the same rules, in prose, to
# docs/orchestration_log/recon/2026-09-28/trainer/agent/allowlist.md; this is the enforced form.
KEY_DENY_PATTERN = "Read(training/rust/items/**/key/**)"


def allowed_bash_patterns(unit: str) -> list[str]:
    manifest = f"training/rust/{unit}/Cargo.toml"
    return [
        "Bash(uv run python scripts/train/log.py*)",
        f"Bash(cargo check --manifest-path {manifest}*)",
        f"Bash(cargo test --manifest-path {manifest}*)",
    ]


def trainer_launch_command(unit: str) -> str:
    """The trainer hand-off command, permission flags included: `dontAsk` so a call outside the
    allowlist is refused outright rather than put to the learner (no lock-out exists otherwise —
    fable-plan.md § 5 sessions.assistant_closed)."""
    parts = [
        "claude",
        "--agent",
        "rust-trainer",
        "--permission-mode",
        "dontAsk",
        "--allowedTools",
        " ".join(allowed_bash_patterns(unit)),
        "--disallowedTools",
        KEY_DENY_PATTERN,
        "--",
        "--unit",
        unit,
        "--record",
        "training/rust/record/",
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
        crate_dir = ensure_unit_crate(row["unit"])
        run_probe(unit_dir, crate_dir, "delayed", wait=wait, clock=clock)
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
