# Rust map research — state, 2026-09-29

## Published: maps/rust/ v0.1, provisional (commits fae7df5 … Arguments compile)

| layer | count | checked |
|---|---|---|
| Questions | 401 | merge blind check 78.0% agreement (merge-v3) |
| Positions | 607 | blind double fill: Position 98.7%, tag 67.6%; 1 Position and 9 tags unresolved |
| Claims | 771 | 664 checked at source: 648 CONFIRMED, 8 DATE-WRONG fixed, 8 UNFAITHFUL fixed; 107 below the Voice bar unchecked |
| Voices | 374 (399 ids, 25 merged) | 300 MEETS, 77 FAILS, 22 UNKNOWN; calibration audit applied |
| Arguments | 429 over 259 Positions, 114 Questions | 58 held out: candidate Values only (args/value-candidates.md) |
| Validator | 417 FAIL | all declared gaps (Voice fields, undated Claims, 9 untagged Positions, 2 Questions without domains) |

Evidence minimum met: 4 Questions. Single-Position Questions: 275. Coverage: Chapman unseen 25–49%, Chao1 31–76% per stratum (merge-v3/estimate/closure-b1.md). English only. No fairness grading (paired cases, ITT) yet: waits for a stable Question set (slice-1-review.md § 5).

## Batch 2: prepared, extraction stopped at the weekly limit (2026-09-28 16:18)

Prep (batch-2-prep.md): frozen prompts; class-balanced sampler; swift-interop off-subject rows dropped; zh conference-talk anchor rows redrawn; all rows cached. Draw: 285 rows per team (en 90, zh 158, uk 20, de 17), 132 shared; bundled into 28 slices (team a, 273 readable rows) and 33 slices (team b, 275).

Extraction on disk, complete per manifest:
- team a: slices 01 02 03 04 07 08 10 11 (8 of 28)
- team b: slices 01 02 03 04 05 06 10 11 13 (9 of 33)

Resumable agents and their unfinished assigned slices:

| agent | done | left |
|---|---|---|
| r2-xa-1 | 01–03 | 13–15 |
| r2-xa-2 | 04 | 05–06 |
| r2-xa-3 | 07–08 | 09 |
| r2-xa-4 | 10–11 | 12 |
| r2-xb-2 | 04–06, 13 | 14–15 |
| r2-xb-3 | — | 07–09 |
| r2-xb-4 | 10–11 | 12 |

Unassigned, not launched this span (owner ruling 2026-09-29): team a 16–28, team b 16–33.

After extraction: census gate, audit, merge (merge-b2/), merge check, estimate.py, blind fill and resolve, Claim and Voice checks, Arguments, compile to v0.2 (prompts/t5-compile.md).
