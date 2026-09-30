"""Draw one batch's stratified samples for the Rust map's wide pass (fable-plan.md § 2, Tier 2).

Usage: `uv run gym map sample --frame frame.csv --out samples/ --batch n --seed s (--per-team k | --cells cells.csv) [--by-class]`,
or `... --frame frame.csv --out samples/ --batch n --seed s --replace ids.csv` to replace drawn rows.

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
and batch 1 re-draws from its logged seed. With the flag, the cell that drew
each row is written to `batch-n-team-T-cells.csv` (id, language, hint, class).

`--replace` (columns team, frame_id) swaps each listed row of `batch-n-team-T.csv`
for one row drawn from the same (language, hint, class) cell, excluding every
row the team has drawn in any batch or had replaced; the RNG is
`Random(f"{seed}-{team}")`. An empty cell leaves the row out with no
replacement. Every swap is appended to `batch-n-team-T-replaced.csv`.
With `--other-class`, the replacement comes from the same (language, hint) cell's other
classes: for a class dropped whole from the frame, whose own cell is empty.
"""

from __future__ import annotations

import csv
import random
from pathlib import Path

FRAME_FIELDS = ["id", "url", "title", "author", "date", "language", "class", "domain_hints"]
CELL_FIELDS = ["id", "language", "hint", "class"]
REPLACED_FIELDS = ["replaced_id", "replacement_id", "language", "hint", "class", "pool", "seed"]
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
            selected.setdefault(row["id"], {**row, "cell": key})
    return [selected[row_id] for row_id in sorted(selected)]


def in_cell(row: dict, cell: tuple[str, str]) -> bool:
    language, hint = cell
    return row["language"] == language and (hint == "*" or hint in row["domain_hints"].split(";"))


def replace_rows(frame_rows: list[dict], current: list[dict], cell_of: dict[str, tuple[str, str]], replace_ids: list[str],
                 excluded: set[str], rng: random.Random, other_class: bool = False) -> tuple[list[dict], list[dict]]:
    by_id = {row["id"]: row for row in current}
    excluded = excluded | set(by_id) | set(replace_ids)
    log: list[dict] = []
    for row_id in sorted(replace_ids):
        old = by_id.pop(row_id)
        cell, row_class = cell_of[row_id], sampling_class(old)
        pool = sorted((row for row in frame_rows if row["id"] not in excluded and in_cell(row, cell)
                       and (sampling_class(row) != row_class if other_class else sampling_class(row) == row_class)),
                      key=lambda row: row["id"])
        new = rng.choice(pool) if pool else None
        if new:
            excluded.add(new["id"])
            by_id[new["id"]] = new
            cell_of[new["id"]] = cell
        log.append({"replaced_id": row_id, "replacement_id": new["id"] if new else "", "language": cell[0],
                    "hint": cell[1], "class": row_class, "pool": len(pool)})
    return [by_id[row_id] for row_id in sorted(by_id)], log


def write_rows(path: Path, fields: list[str], rows: list[dict], append: bool = False) -> None:
    new_file = not (append and path.exists())
    with path.open("a" if append else "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        if new_file:
            writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def write_sample(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FRAME_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in FRAME_FIELDS})


def main(frame: Path, out: Path, batch: int, seed: int, per_team: int | None, cells: Path | None, by_class: bool) -> int:
    rows = read_frame(frame)
    if cells:
        team_quota = read_cells(cells)
        cell_rows = {**strata_of(rows), **whole_language_cells(rows)}
        missing = sorted(key for key in team_quota if key not in cell_rows)
        if missing:
            raise SystemExit(f"cells not in the frame: {missing}")
        strata = {key: cell_rows[key] for key in team_quota}
        quota: int | dict[tuple[str, str], int] = team_quota
    else:
        quota = per_team
        strata = strata_of(rows)
    out.mkdir(parents=True, exist_ok=True)

    for offset, team in enumerate(TEAMS):
        rng = random.Random(seed + offset)
        used = already_used(out, team, batch)
        drawn = draw_for_team(strata, used, quota, rng, by_class)
        write_sample(out / f"batch-{batch}-team-{team}.csv", drawn)
        if by_class:
            write_rows(out / f"batch-{batch}-team-{team}-cells.csv", CELL_FIELDS,
                       [{"id": row["id"], "language": row["cell"][0], "hint": row["cell"][1], "class": sampling_class(row)} for row in drawn])
        print(f"seed: {seed + offset}  batch: {batch}  team: {team}  rows: {len(drawn)}")

    return 0


def replace_main(frame: Path, out: Path, batch: int, seed: int, replace: Path, other_class: bool) -> int:
    rows = read_frame(frame)
    requests = read_frame(replace)
    for team in TEAMS:
        replace_ids = [row["frame_id"] for row in requests if row["team"] == team]
        if not replace_ids:
            continue
        sample_path = out / f"batch-{batch}-team-{team}.csv"
        cells_path = out / f"batch-{batch}-team-{team}-cells.csv"
        log_path = out / f"batch-{batch}-team-{team}-replaced.csv"
        current = read_frame(sample_path)
        cell_of = {row["id"]: (row["language"], row["hint"]) for row in read_frame(cells_path)}
        missing = sorted(set(replace_ids) - {row["id"] for row in current})
        if missing:
            raise SystemExit(f"team {team}: not in {sample_path.name}: {missing}")
        replaced_before = {row["replaced_id"] for row in read_frame(log_path)} if log_path.exists() else set()
        excluded = already_used(out, team, batch) | replaced_before
        rng = random.Random(f"{seed}-{team}")
        updated, log = replace_rows(rows, current, cell_of, replace_ids, excluded, rng, other_class)
        write_sample(sample_path, updated)
        write_rows(cells_path, CELL_FIELDS, [{"id": row["id"], "language": cell_of[row["id"]][0], "hint": cell_of[row["id"]][1],
                                             "class": sampling_class(row)} for row in updated])
        write_rows(log_path, REPLACED_FIELDS, [{**entry, "seed": seed} for entry in log], append=True)
        for entry in log:
            print(f"team {team}: {entry['replaced_id']} -> {entry['replacement_id'] or '(cell empty)'}  "
                  f"cell {entry['language']}/{entry['hint']}/{entry['class']}  pool {entry['pool']}")
    return 0
