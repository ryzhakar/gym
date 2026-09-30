# Capabilities

What gym's built parts are and do. Measured 2026-09-30 unless dated otherwise.

## The gym app

One Typer application, package `src/gym/`, entry point `uv run gym`. Groups: `gym map` (check, census, sample, frame, estimate, site), `gym train` (open, log, probe, close, status, check), `gym research` (books, bundle, cache, search, sendback), `gym records` (event, close, check). Tests under `tests/`: 172 pass (measured 2026-09-30 17:21). Decided 2026-09-30, see docs/architecture_log.md.

## The map site

`uv run gym map site <map-path> --out <html>` generates one self-contained HTML page from a map's data layer: no server, framework, CDN or stored state. Views: the Matrix (rows Questions, columns Voices anonymous until clicked, cells the Position held, Reorder by greedy nearest neighbour, drag) and the Graph (Questions, Concepts, Domains, Values on the edges the data holds; Concept-Concept edges 0 of 1447 on 2026-09-30). Default Matrix subset iterates to a fixed point: 41 Questions by 43 Voices, 115 of 698 cells (measured 2026-09-30). A Claim renders checked when it carries `checked`, provisional otherwise; 664 of 771 Rust Claims carry it (measured 2026-09-30).

## Training records

`gym train` keeps one directory per session, `training/<subject>/sessions/<id>/`, holding `events.md` (one line per event, `time | actor | kind | key=value …`, kinds and required fields in `src/gym/train/schema.py`) and `session.md` (heading, then a close block). `status` derives the queue, unit history and confidence from all sessions' events; `check` lints them. Session ids are colon-free, `YYYY-MM-DDTHH-MM`, since a colon in a path breaks cargo on macOS (found 2026-09-30). The session of 2026-09-30 ran on the earlier CSV tables and was converted into this layout on 2026-09-30; the tables and the old scripts are gone. `probe stage` copies a unit's probe problems and records the start; `probe grade` grades them against the key tests and writes per-problem minutes, total minutes and the cap verdict.
