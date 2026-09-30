# Capabilities

What gym's built parts are and do. Measured 2026-09-30 unless dated otherwise.

## The gym app

One Typer application, package `src/gym/`, entry point `uv run gym`. Every command carries one-sentence help; `gym --version`; checks print their summary first; a bad path fails in one line with exit 2 (measured 2026-09-30). Groups: `gym map` (check, census, sample, frame, estimate, site, concepts dedup), `gym train` (open, log, probe, close, status, check), `gym research` (books, bundle, cache, search, sendback), `gym records` (event, close, check). Tests under `tests/`: 261 pass (measured 2026-09-30 23:33). Decided 2026-09-30, see docs/architecture_log.md.

## The map site

`uv run gym map site <map-path> --out <html>` generates one self-contained HTML page from a map's data layer: no server, framework, CDN or stored state. Front door: the Concept graph, canonical Concepts (1372 on 2026-09-30, `merged_into` marking 75 merged) as nodes sized by the Questions touching them, an edge between two Concepts holding every Question touching both (4837 edges, 4793 of weight 1, measured 2026-09-30), Louvain communities laid out as separate islands, a backbone of 1880 of 4837 edges at the opening frame, hubs above the 99th degree percentile capped, the 490 detached Concepts in 125 clusters behind a legend toggle, labels acting as their Concept, hover isolation, pinned panel with the Concept's Questions, local views at depth 1 and 2, search; settles in 236 ms headless (measured 2026-09-30). Second view: the Matrix, rows Questions and columns Voices anonymous until clicked, co-clustered by `src/gym/map/cluster.py` (spectral, Dhillon 2001; on Rust k=5 blocks over 62 Questions and 51 Voices, measured 2026-09-30). A Claim renders checked when it carries `checked`, provisional otherwise; 664 of 771 Rust Claims carry it (measured 2026-09-30). Decided 2026-09-30, see docs/architecture_log.md.

## Training records

`gym train` keeps one directory per session, `training/<subject>/sessions/<id>/`, holding `events.md` (one line per event, `time | actor | kind | key=value …`, kinds and required fields in `src/gym/train/schema.py`) and `session.md` (heading, then a close block). `status` derives the queue, unit history and confidence from all sessions' events; `check` lints them. Session ids are colon-free, `YYYY-MM-DDTHH-MM`, since a colon in a path breaks cargo on macOS (found 2026-09-30). The session of 2026-09-30 ran on the earlier CSV tables and was converted into this layout on 2026-09-30; the tables and the old scripts are gone. `probe stage` copies a unit's probe problems and records the start; `probe grade` grades them against the key tests and writes per-problem minutes, total minutes and the cap verdict.

## The trainer

`.claude/agents/gym-trainer.md`, version of 2026-09-30: summoned by the manager with the summons at `training/summons-template.md` filled in; holds every tool, with the key/ and workspace bans as rules in its text; may summon agents of its own for anything but the conversation with the learner; logs every turn through `gym train log`, runs probes through `gym train probe stage` and `grade`, and writes the session narrative into the session record before it returns. The learner's tool allowance per item kind stands in `training/rust/items/README.md`.
