"""Present a unit's probe item, time the attempt against the cap, grade it with `cargo test`, log the row.

Usage: `uv run python scripts/train/probe.py <unit_dir> <crate_dir> immediate|delayed [--cap-minutes 10]`.

`immediate` presents the unit's `probe-a/`, `delayed` its `probe-b/` — the isomorph the delayed
check reads against (fable-plan.md § 1 T3, § 7 "isomorph illusion"). Layout is P3's, § 4: each unit
directory holds `probe-a/`, `probe-b/`, and a `key/` this script never opens or prints — anywhere
under the unit directory, under either probe directory, or under any path handed to it — even if a
future item bank nests `key/` somewhere unexpected.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from datetime import date, datetime
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).parent))
from log import append_row, build_row  # noqa: E402
from record_schema import TIMESTAMP_FORMAT, file_path  # noqa: E402

CAP_MINUTES_DEFAULT = 10.0  # O2, first-protocol default, unmeasured (fable-plan.md § 6 O2)
KIND_OF = {"immediate": "probe-immediate", "delayed": "probe-delayed"}
ISOMORPH_OF = {"immediate": "probe-a", "delayed": "probe-b"}


def assert_no_key(path: Path) -> None:
    if "key" in path.parts:
        sys.exit(f"refused, probe.py never opens a 'key/' path: {path}")


def probe_dir(unit_dir: Path, which: str) -> Path:
    target = unit_dir / ISOMORPH_OF[which]
    assert_no_key(target)
    if not target.is_dir():
        sys.exit(f"refused, no such probe directory: {target}")
    return target


def item_text(directory: Path) -> str:
    """Every file's text under `directory`, sorted by path, with any `key/` path component excluded."""
    parts = []
    for path in sorted(directory.rglob("*")):
        if "key" in path.relative_to(directory).parts:
            continue
        if path.is_file():
            assert_no_key(path)
            parts.append(f"--- {path.relative_to(directory)} ---\n{path.read_text(encoding='utf-8')}")
    return "\n\n".join(parts)


def run_cargo_test(crate_dir: Path) -> tuple[bool, float]:
    manifest = crate_dir / "Cargo.toml"
    if not manifest.is_file():
        sys.exit(f"refused, no crate at {crate_dir}")
    result = subprocess.run(
        ["cargo", "test", "--manifest-path", str(manifest)],
        capture_output=True,
        text=True,
        check=False,
    )
    passed = failed = 0
    for match in re.finditer(r"test result: \w+\. (\d+) passed; (\d+) failed", result.stdout):
        passed += int(match.group(1))
        failed += int(match.group(2))
    if passed + failed == 0:
        sys.exit(f"refused, no test result in cargo output for {crate_dir}:\n{result.stdout}\n{result.stderr}")
    return failed == 0, passed / (passed + failed)


def delay_days_for(unit: str) -> float:
    """Days since the unit's most recent logged practice item; 0 when none is logged yet."""
    path = file_path("items")
    if not path.is_file():
        return 0.0
    import csv

    with path.open(encoding="utf-8", newline="") as handle:
        practice = [row for row in csv.DictReader(handle) if row["unit"] == unit and row["kind"] == "practice"]
    if not practice:
        return 0.0
    latest = max(row["timestamp"] for row in practice)
    then = datetime.strptime(latest, TIMESTAMP_FORMAT).date()
    return float((date.today() - then).days)


def run_probe(
    unit_dir: Path,
    crate_dir: Path,
    which: str,
    cap_minutes: float = CAP_MINUTES_DEFAULT,
    wait: Callable[[], None] = lambda: input(),
    clock: Callable[[], float] = time.monotonic,
) -> dict[str, str]:
    unit = unit_dir.name
    directory = probe_dir(unit_dir, which)
    print(item_text(directory))
    print(f"\ncap: {cap_minutes:g} min. Press Enter once your answer is in {crate_dir}.")
    start = clock()
    wait()
    elapsed_minutes = (clock() - start) / 60
    if elapsed_minutes > cap_minutes:
        print(f"over the {cap_minutes:g}-minute cap: {elapsed_minutes:.1f} min")
    passed, continuous = run_cargo_test(crate_dir)
    delay_days = 0.0 if which == "immediate" else delay_days_for(unit)
    fields = {
        "item_id": f"{unit}-{ISOMORPH_OF[which]}",
        "unit": unit,
        "kind": KIND_OF[which],
        "delay_days": str(delay_days),
        "pass": "true" if passed else "false",
        "continuous": f"{continuous:.4f}",
        "minutes": f"{elapsed_minutes:.2f}",
        "attempts": "1",
    }
    row = build_row("items", fields)
    append_row("items", row)
    return row


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("unit_dir", type=Path)
    parser.add_argument("crate_dir", type=Path)
    parser.add_argument("which", choices=["immediate", "delayed"])
    parser.add_argument("--cap-minutes", type=float, default=CAP_MINUTES_DEFAULT)
    args = parser.parse_args(argv[1:])
    row = run_probe(args.unit_dir, args.crate_dir, args.which, args.cap_minutes)
    print(f"logged: {row}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
