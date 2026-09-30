"""Turn frame files into one sampler input for the Rust map's wide pass (fable-plan.md § 2, Tier 2).

Usage: `uv run gym map frame --frame frame.csv [--frame frame-v2-nonen.csv] [--drop drop.csv] --out input.csv`.

The batch-1 rules (`samples/batch-1.md` § sample.py could not express the batch
rules directly), unchanged: a hint-less row samples as `core`; a row whose only
hint is `other` is excluded; hints outside the eleven sampled strata are
stripped, and a row left with none samples as `core`. Columns are renamed to the
sampler's (`frame_id` → `id`, `author_handle` → `author`). Added for batch 2:
rows outside `window=in` are excluded (every batch-1 row was `in`), and the
frame ids listed in a `--drop` file (column `frame_id`) are excluded, the way a
Tier 1 frame fix is applied without editing the committed frame.
"""

from __future__ import annotations

import csv
from pathlib import Path

SAMPLED_STRATA = {"web", "distributed", "decentralized-iroh", "ml", "desktop-cli-ui",
                  "swift-interop", "frontend", "cloud-workers", "wasm", "embedded", "core"}
OUT_FIELDS = ["id", "url", "title", "author", "date", "language", "class", "domain_hints",
              "transcript_available", "window"]


def sampled_hints(domain_hints: str) -> str | None:
    tokens = [token for token in domain_hints.strip().split(";") if token]
    if not tokens:
        return "core"
    if set(tokens) == {"other"}:
        return None
    kept = [token for token in tokens if token in SAMPLED_STRATA]
    return ";".join(kept) if kept else "core"


def prepare(frame_rows: list[dict], dropped: set[str]) -> list[dict]:
    prepared = []
    for row in frame_rows:
        if row["window"] != "in" or row["frame_id"] in dropped:
            continue
        hints = sampled_hints(row["domain_hints"])
        if hints is None:
            continue
        prepared.append({"id": row["frame_id"], "url": row["url"], "title": row["title"],
                         "author": row["author_handle"], "date": row["date"],
                         "language": row["language"], "class": row["class"], "domain_hints": hints,
                         "transcript_available": row["transcript_available"], "window": row["window"]})
    return prepared


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main(frame: list[Path], drop: Path | None, out: Path) -> int:
    frame_rows = [row for path in frame for row in read_csv(path)]
    dropped = {row["frame_id"] for row in read_csv(drop)} if drop else set()
    prepared = prepare(frame_rows, dropped)

    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUT_FIELDS)
        writer.writeheader()
        writer.writerows(prepared)
    print(f"read: {len(frame_rows)}  dropped by list: {len(dropped & {row['frame_id'] for row in frame_rows})}  written: {len(prepared)}  -> {out}")
    return 0
