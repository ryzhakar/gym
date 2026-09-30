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
