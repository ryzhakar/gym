"""Draw one batch's stratified samples for the Rust map's wide pass (fable-plan.md § 2, Tier 2).

Usage: `uv run python scripts/map/sample.py --frame frame.csv --out samples/ --batch n --seed s (--per-team k | --cells cells.csv) [--by-class]`.

Strata are (language, domain-hint) cells; a row with several domain hints falls
into several cells and is de-duplicated once selected. Per cell, per team, draws
up to `k` rows: independent draws across teams (team B reads seed+1, so the two
teams' draws differ but both stay reproducible from one `--seed`; overlap
between them is the capture-recapture signal, not something to avoid), without
replacement within a team across batches already written to `--out`.

`--cells` names the cells to draw and each cell's `k` (columns language, hint,
per_team; hint `*` is one cell holding every row of the language). Without it,
every cell in the frame is drawn at `--per-team`.

`--by-class` (batch 2 on; slice-1-review.md § 4 (2)) splits each cell's `k`
evenly across the source classes in it, a class being the first `;`-token of the
row's class string; a class with fewer rows than its share passes the rest to
the others, and which classes take the remainder is drawn by the same RNG. Rows
this team already drew in the batch leave the later cells' pools, so every cell
gets its full `k` when it has the rows. Without the flag the draw is batch 1's,
and batch 1 re-draws from its logged seed.
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


def whole_language_cells(rows: list[dict]) -> dict[tuple[str, str], list[dict]]:
    cells: dict[tuple[str, str], list[dict]] = {}
    for row in rows:
        cells.setdefault((row["language"], "*"), []).append(row)
    return cells


def read_cells(path: Path) -> dict[tuple[str, str], int]:
    return {(row["language"], row["hint"]): int(row["per_team"]) for row in read_frame(path)}


def sampling_class(row: dict) -> str:
    return row["class"].split(";")[0]


def class_quotas(sizes: dict[str, int], k: int, rng: random.Random) -> dict[str, int]:
    """Deal `k` draws one at a time over the classes, in an RNG-drawn order, skipping full classes."""
    order = rng.sample(sorted(sizes), len(sizes))
    quotas = dict.fromkeys(order, 0)
    remaining = min(k, sum(sizes.values()))
    while remaining:
        for name in order:
            if remaining and quotas[name] < sizes[name]:
                quotas[name] += 1
                remaining -= 1
    return quotas


def draw_cell_by_class(pool: list[dict], k: int, rng: random.Random) -> list[dict]:
    by_class: dict[str, list[dict]] = {}
    for row in pool:
        by_class.setdefault(sampling_class(row), []).append(row)
    quotas = class_quotas({name: len(rows) for name, rows in by_class.items()}, k, rng)
    drawn: list[dict] = []
    for name in sorted(by_class):
        drawn += rng.sample(by_class[name], quotas[name])
    return drawn


def draw_for_team(strata: dict[tuple[str, str], list[dict]], used: set[str], per_team: int | dict[tuple[str, str], int],
                  rng: random.Random, by_class: bool = False) -> list[dict]:
    selected: dict[str, dict] = {}
    for key in sorted(strata):
        k = per_team[key] if isinstance(per_team, dict) else per_team
        taken = used | selected.keys() if by_class else used
        pool = sorted((row for row in strata[key] if row["id"] not in taken), key=lambda row: row["id"])
        if by_class:
            drawn = draw_cell_by_class(pool, k, rng)
        else:
            drawn = pool if len(pool) <= k else rng.sample(pool, k)
        print(f"  cell {key[0]}/{key[1]}: pool {len(pool)}  drawn {len(drawn)}")
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
    quota = parser.add_mutually_exclusive_group(required=True)
    quota.add_argument("--per-team", type=int, dest="per_team")
    quota.add_argument("--cells", type=Path, help="CSV: language,hint,per_team; hint * is the whole language")
    parser.add_argument("--by-class", action="store_true", dest="by_class")
    parser.add_argument("--seed", required=True, type=int)
    args = parser.parse_args()

    rows = read_frame(args.frame)
    if args.cells:
        per_team = read_cells(args.cells)
        cells = {**strata_of(rows), **whole_language_cells(rows)}
        missing = sorted(key for key in per_team if key not in cells)
        if missing:
            parser.error(f"cells not in the frame: {missing}")
        strata = {key: cells[key] for key in per_team}
    else:
        per_team = args.per_team
        strata = strata_of(rows)
    args.out.mkdir(parents=True, exist_ok=True)

    for offset, team in enumerate(TEAMS):
        rng = random.Random(args.seed + offset)
        used = already_used(args.out, team, args.batch)
        drawn = draw_for_team(strata, used, per_team, rng, args.by_class)
        write_sample(args.out / f"batch-{args.batch}-team-{team}.csv", drawn)
        print(f"seed: {args.seed + offset}  batch: {args.batch}  team: {team}  rows: {len(drawn)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
