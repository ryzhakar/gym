"""Draw one batch's stratified samples for the Rust map's wide pass (fable-plan.md § 2, Tier 2).

Usage: `uv run python scripts/map/sample.py --frame frame.csv --out samples/ --batch n --per-team k --seed s`.

Strata are (language, domain-hint) cells; a row with several domain hints falls
into several cells and is de-duplicated once selected. Per cell, per team, draws
up to `k` rows: independent draws across teams (team B reads seed+1, so the two
teams' draws differ but both stay reproducible from one `--seed`; overlap
between them is the capture-recapture signal, not something to avoid), without
replacement within a team across batches already written to `--out`.
"""

from __future__ import annotations

import argparse
import csv
import random
import sys
from pathlib import Path

FRAME_FIELDS = ["id", "url", "title", "author", "date", "language", "class", "domain_hints"]
TEAMS = ["a", "b"]


def read_frame(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def strata_of(rows: list[dict]) -> dict[tuple[str, str], list[dict]]:
    strata: dict[tuple[str, str], list[dict]] = {}
    for row in rows:
        hints = [hint.strip() for hint in row["domain_hints"].split(";") if hint.strip()]
        for hint in hints:
            strata.setdefault((row["language"], hint), []).append(row)
    return strata


def already_used(out_dir: Path, team: str, before_batch: int) -> set[str]:
    used: set[str] = set()
    for path in out_dir.glob(f"batch-*-team-{team}.csv"):
        batch_number = int(path.stem.split("-")[1])
        if batch_number < before_batch:
            used |= {row["id"] for row in read_frame(path)}
    return used


def draw_for_team(strata: dict[tuple[str, str], list[dict]], used: set[str], per_team: int, rng: random.Random) -> list[dict]:
    selected: dict[str, dict] = {}
    for key in sorted(strata):
        pool = sorted((row for row in strata[key] if row["id"] not in used), key=lambda row: row["id"])
        drawn = pool if len(pool) <= per_team else rng.sample(pool, per_team)
        for row in drawn:
            selected.setdefault(row["id"], row)
    return [selected[row_id] for row_id in sorted(selected)]


def write_sample(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FRAME_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in FRAME_FIELDS})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frame", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path, help="directory holding batch-*-team-*.csv")
    parser.add_argument("--batch", required=True, type=int)
    parser.add_argument("--per-team", required=True, type=int, dest="per_team")
    parser.add_argument("--seed", required=True, type=int)
    args = parser.parse_args()

    rows = read_frame(args.frame)
    strata = strata_of(rows)
    args.out.mkdir(parents=True, exist_ok=True)

    for offset, team in enumerate(TEAMS):
        rng = random.Random(args.seed + offset)
        used = already_used(args.out, team, args.batch)
        drawn = draw_for_team(strata, used, args.per_team, rng)
        write_sample(args.out / f"batch-{args.batch}-team-{team}.csv", drawn)
        print(f"seed: {args.seed + offset}  batch: {args.batch}  team: {team}  rows: {len(drawn)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
