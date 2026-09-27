# Rust map — batch 1 sample

Input sha256 (frame.csv, verified before use): `99ea45bb67b8c64238c7cff0286ca74cd4c27db06aa96c20b9b6f6823dab80e7` — matches.

Seed: `1786744536` (team a); team b reads `seed+1` = `1786744537` per sampler contract.

## sample.py could not express the batch rules directly

`sample.py` has no flag for "no-hint rows sample as core", "other-only rows excluded", or restricting strata to the eleven fixed cells; it also expects columns `id`/`author`, not the frame's `frame_id`/`author_handle`. Wrote a filtered, renamed copy of the frame first.

Filter script (`uv run python -c "..."`, full logic):

```python
import csv

FRAME = "docs/orchestration_log/recon/2026-09-27/research/rust-map/frame/frame.csv"
OUT = "docs/orchestration_log/recon/2026-09-27/research/rust-map/samples/frame-b1-input.csv"
KNOWN_DOMAINS = {"web","distributed","decentralized-iroh","ml","desktop-cli-ui",
                 "swift-interop","frontend","cloud-workers","wasm","embedded","core"}
OUT_FIELDS = ["id","url","title","author","date","language","class","domain_hints",
              "transcript_available","window"]

with open(FRAME, newline="") as f:
    rows = list(csv.DictReader(f))

kept = []
for row in rows:
    tokens = [t for t in row["domain_hints"].strip().split(";") if t]
    if not tokens:
        dh = "core"                                    # hint-less -> core
    else:
        if set(tokens) == {"other"}:
            continue                                    # other-only -> excluded
        filtered = [t for t in tokens if t in KNOWN_DOMAINS]  # drop other/unknown tags
        dh = ";".join(filtered) if filtered else "core"
    kept.append({"id": row["frame_id"], "url": row["url"], "title": row["title"],
                 "author": row["author_handle"], "date": row["date"],
                 "language": row["language"], "class": row["class"], "domain_hints": dh,
                 "transcript_available": row["transcript_available"], "window": row["window"]})

with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=OUT_FIELDS)
    w.writeheader()
    w.writerows(kept)
```

Input: 11083 rows, all `language=en` (batch 1 is English-only by construction, no rows dropped for language). Effect: 4618 hint-less rows set to `core`; 0 other-only rows dropped (none exist — the 13 rows carrying `other` all also carry a real domain, e.g. `core;other`, `distributed;other`); 24 rows had `other` and/or an unknown tag (`community`, `governance`, `tools`, `compiler` — not in the fixed strata set) stripped while keeping their real domain hint(s). Output: 11083 rows, `frame-b1-input.csv`.

## Sampler run

```
uv run python scripts/map/sample.py --frame docs/orchestration_log/recon/2026-09-27/research/rust-map/samples/frame-b1-input.csv --out docs/orchestration_log/recon/2026-09-27/research/rust-map/samples --batch 1 --per-team 18 --seed 1786744536
```

Output:
```
seed: 1786744536  batch: 1  team: a  rows: 198
seed: 1786744537  batch: 1  team: b  rows: 198
```

`--per-team 18` chosen because 18 × 11 cells = 198, closest whole-k multiple of 11 to the ~200/team target. Every one of the 11 cells has far more source rows than 18 (smallest cell, `cloud-workers`, has 76 in the filtered frame), so both teams drew a full 18 in every cell — no cell short of quota.

## Rows per team per cell

Counted from each team's output file; a count includes rows drawn under another cell that also happen to carry this cell as a secondary hint (e.g. a `web;core` row drawn via the `web` cell's own draw still counts toward `core` here), so per-cell totals exceed the 18 draws made specifically against that cell.

| cell | team a | team b |
|---|---|---|
| core | 27 | 28 |
| web | 28 | 27 |
| distributed | 23 | 22 |
| decentralized-iroh | 18 | 18 |
| ml | 19 | 20 |
| desktop-cli-ui | 23 | 20 |
| swift-interop | 19 | 19 |
| frontend | 18 | 18 |
| cloud-workers | 19 | 18 |
| wasm | 19 | 21 |
| embedded | 20 | 19 |

Distinct rows: team a 198, team b 198.

## Overlap

17 frame ids drawn by both team a and team b (of 198 each) — the capture-recapture signal, not a defect.

## Cells short of quota

None. All 11 cells' pool sizes (76–5329 rows) exceed `--per-team 18`.
