# Architecture log

## 2026-09-30 — Scripts become the gym app

KIND:          runnable
FROM → TO:     a dismembered collection of scripts under scripts/ (map, research, train, and the three memento scripts at the root), each run as `uv run python scripts/…` → one Typer application, `uv run gym <group> <command>`, package src/gym/, groups map, research, records, with the train group built beside the still-live train scripts
WHY:           owner ruling 2026-09-30: one typer-enabled app manages gym concerns, not a dismembered collection of scripts
INVALIDATES:   every command of the form `uv run python scripts/<name>.py` outside scripts/train/; docs/conventions.md record-check and event-lines now name `gym records`
EVIDENCE:      commits 3a6ba15, 8798572, 0ef8f54, 5ed454e, 7f22d78; 104 tests pass

## 2026-09-30 — The map gains a generated site

KIND:          runnable
FROM → TO:     no presentation layer; the map readable only as entity files → `gym map site <map-path>` generates a self-contained page with the Matrix and Graph views from the data layer alone
WHY:           owner ruling 2026-09-30: the frontend is a command operating on a path; the deferral's pickup condition, real Questions in the data layer, is met
INVALIDATES:   nothing computed; the prototype under recon/2026-09-30/frontend/proto/ is superseded by src/gym/map/site.py
EVIDENCE:      commits 5ed454e, 8386204, 621694a; 15 tests under tests/map

## 2026-09-30 — Claims carry a checked field

KIND:          computed
FROM → TO:     verification of a Claim's quote and date recorded only in maps/rust/README.md prose → each verified Claim carries `checked: {date, method, verdict}` in its file, 648 confirmed and 16 corrected; 107 below the Voice bar carry none
WHY:           the map's rule that every entry shows whether it is provisional or checked (docs/opinion-map.md § Done and upkeep); the site reads the field
INVALIDATES:   any count that reads verification status from README prose; `practiced` never meant checked
EVIDENCE:      commit 7bb354e; `gym map check --map maps/rust` 417 FAIL before and after

## 2026-09-30 — Training sessions keep their own records

KIND:          runnable
FROM → TO:     five CSV tables under training/rust/record/ written by scripts/train/ (log.py, probe.py), the sessions row written by nobody, an interactive probe run by the learner → one directory per session under training/<subject>/sessions/<id>/ holding events.md and session.md, written through `gym train open`, `log`, `probe stage`, `probe grade`, `close`; `status` derives the queue, unit history and confidence; `check` lints; ids colon-free
WHY:           owner ruling 2026-09-30: a training session has its own record and events, the tables dropped; the learner does no administration
INVALIDATES:   every reader of training/rust/record/*.csv; every summons naming scripts/train/; probe minutes as one shared elapsed time
EVIDENCE:      commits 7f22d78, 5692800, 3067135, d7f00ba, fa8cab9, d788cd2, 35b3f23; 192 tests pass; session 2026-09-30T15:40 converted, `gym train check training/rust` 0 FAIL

## 2026-09-30 — The Concept graph becomes the map's front door

KIND:          computed
FROM → TO:     Concepts drawn as an undifferentiated hairball from Question-Concept links, 1447 Concepts with duplicates, Concept-Concept edges 0 of 1447 → canonical Concepts (1372 after 75 merges marked `merged_into`) as nodes, an edge between two Concepts holding every Question touching both, weight the count, Louvain communities named by hubs, hover isolation, pinned panels, local views; the Matrix co-clustered two ways by a spectral module
WHY:           owner rulings 2026-09-30: the Concept graph is the map itself, Obsidian-style, readable at a glance; edges hold co-touching Questions; Concepts deduplicated; the Matrix clusters Voices by stances and Questions by Voices
INVALIDATES:   every Concept count before the dedup; the Graph v0 and v01 renders under recon/2026-09-30/frontend/; any reading of the Matrix that treated its order as arbitrary
EVIDENCE:      commits 9602197, bb0d915, 44cc092, 090a2d4, 635d6f5, a8bf2dc, e745638, b1f974a, 2be2270, 42d79f8, b12e416; 280 tests pass; cold review passed all four tests, recon/2026-09-30/frontend/map-review-2.md

## 2026-09-30 — Baseline items run by command

KIND:          runnable
FROM → TO:     baseline items attempted from a hand-copied stub and graded by a shell loop the learner ran, which silently weakened grading on 5 of 6 items → `gym train baseline stage` and `gym train baseline grade`, run by the trainer from absolute paths, key tests brought in by the command, one probe-item event per item with which=baseline; the trainer definition v4 calls them
WHY:           the first-session audit (recon/2026-09-30/train/trainer-quality-report.md) ranked the copy loop and the colon path as the costliest faults
INVALIDATES:   the by-hand baseline procedure in recon/2026-09-30/train/baseline-procedure.md; any session id holding a colon
EVIDENCE:      commits 2c8e3a3, ed3b481; 280 tests pass

