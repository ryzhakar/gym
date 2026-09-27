# Saturation audit — rounds 6–7

Scope: N1–N7, rounds 1–7. Rules: PLAN §5 lines 242–260, with the changes in prompts/audit-r5.md and prompts/audit-r7.md:
- Rules 1 and 2 use rounds 6 and 7 as the pair.
- Rule 2 reads the `## Found DOIs` sections and keeps S≥2 per sources.csv.
- Rule 4 counts S≤2 claims as closed.
- A database that was attempted and blocked with logged retries counts as searched.
- Axis strings are normalized.
- Rule 3 is recomputed from the ledger.

Inputs: ledger/sources.csv (826 rows, all 17 fields, so the repair holds), ledger/claims.csv (464), ledger/claims-status.csv (234; last row per claim_id), the 14 r6/r7 need files plus earlier rounds' logs for query reuse, verify/seed-probe.md, context/seed-citations.csv, prompts/round-6-7.md. Arithmetic ran as throwaway `uv run --no-project python -` over the CSVs in scratch. No script is kept.

"Before the pair" means ledger rows with round 0–5. That includes the 63 t3-grade-found rows, which verify/found-dois-graded.md labels with their source round (4 or 5).

## Headline

1. **No need is SATURATED.** N1, N2, N3, N5 and N7 are OPEN. N4 and N6 are VOID-ROUND because n4-r7.md and n6-r7.md have no `## Found DOIs` section, so rule 2 cannot be computed for them. Rule 1 fails for all seven: every round in the pair found new S≥3 sources.
2. **Rule 2 now registers recaptures.** Dropping the avoid-lists worked: overlap m is 1 for N2 and N7, and 5 for N3. N3 comes closest to saturation, with N̂=53 and 47% unseen. All six sources both N3 captures listed (graded or not) predate the pair, which is the signal a thinning field gives. Every computable need still fails the 10% bar.
3. **Rule 4 fails for N7.** Claims N7-r7-05 and N7-r7-06 are S4 and have no status row. The dispatch said all S≥3 claims from r6/r7 were verified; the ledger does not bear that out. The other six needs pass.
4. **Capture is still thin.**
   - OpenAlex returned results for 34 of 98 logged queries; the rest hit HTTP 429/503 or an exhausted budget, with retries logged. Every round attempted all five required databases, so none is void on that clause.
   - 85 of 269 Found ids have no grade in the ledger, against round-6-7 rule 4 ("grade every source"). Ungraded ids drop out of rule 2's n and m.
   - Most new S≥3 sources were read at abstract level only: 11 of 11 in N2-r7 and 4 of 4 in N4-r6.

## Rule 1 — pair r6/r7: zero new S≥3, ≤1 new S=2

"new" means the id is not tagged to the need in rounds 0–5. Each capture is measured against the ledger as it stood before the pair, because the two ran concurrently.

```
need r  | rows | new | seen | new-to-ledger | new S≥3 | S=2 | S≤1 | ungraded | S/R/O blank | new S≥3 not full-text
N1 r6   |  9 |  9 | 0 |  9 |  3 | 3 | 3 | 0 | 0 | 1
N1 r7   |  8 |  8 | 0 |  5 |  5 | 2 | 1 | 0 | 0 | 4
N2 r6   |  7 |  7 | 0 |  6 |  4 | 0 | 3 | 0 | 0 | 3
N2 r7   | 27 | 21 | 6 | 19 | 11 | 7 | 3 | 0 | 0 | 11
N3 r6   |  9 |  9 | 0 |  9 |  3 | 4 | 2 | 0 | 0 | 3
N3 r7   | 17 | 13 | 4 |  5 |  5 | 3 | 5 | 0 | 0 | 2
N4 r6   | 15 | 15 | 0 | 13 |  4 | 7 | 4 | 0 | 0 | 4
N4 r7   | 11 |  9 | 2 |  9 |  2 | 4 | 3 | 0 | 0 | 2
N5 r6   |  7 |  7 | 0 |  7 |  5 | 1 | 1 | 0 | 0 | 0
N5 r7   | 10 | 10 | 0 | 10 |  1 | 4 | 5 | 0 | 0 | 1
N6 r6   | 10 | 10 | 0 | 10 |  2 | 3 | 5 | 0 | 0 | 2
N6 r7   |  9 |  9 | 0 |  6 |  3 | 3 | 3 | 0 | 0 | 2
N7 r6   | 16 |  9 | 7 |  6 |  2 | 1 | 6 | 0 | 0 | 1
N7 r7   |  9 |  9 | 0 |  9 |  4 | 3 | 2 | 0 | 0 | 3
ledger-row overlap of new ids, r6∩r7: N4 1, all others 0
```

| need | new S≥3 (r6, r7) | new S=2 (r6, r7) | new S≥3, full text read only | Rule 1 |
|---|---|---|---|---|
| N1 | 3, 5 | 3, 2 | 2, 1 | FAIL |
| N2 | 4, 11 | 0, 7 | 1, 0 | FAIL |
| N3 | 3, 5 | 4, 3 | 0, 3 | FAIL |
| N4 | 4, 2 | 7, 4 | 0, 0 (S=2 still 7, 4) | FAIL |
| N5 | 5, 1 | 1, 4 | 5, 0 | FAIL |
| N6 | 2, 3 | 3, 3 | 0, 1 | FAIL |
| N7 | 2, 4 | 1, 3 | 1, 1 | FAIL |

Different agents ran each capture, and each ran ≥12 queries on ≥3 databases. Rule 1 fails for all seven even when only full-text-read S≥3 sources count.

## Rule 2 — Lincoln–Petersen on Found DOIs, r6 vs r7, S≥2

```
need r  | listed | absent from ledger | in ledger, S blank | S≤1 | S≥2
N1 r6   | 13 |  2 | 0 | 3 |  8
N1 r7   | 15 |  0 | 4 | 3 |  8
N2 r6   | 14 |  4 | 1 | 4 |  5
N2 r7   | 25 |  0 | 3 | 4 | 18
N3 r6   | 42 | 19 | 0 | 4 | 19
N3 r7   | 23 |  0 | 3 | 6 | 14
N4 r6   | 19 |  0 | 0 | 4 | 15
N4 r7   | section absent
N5 r6   | 13 |  3 | 1 | 3 |  6
N5 r7   | 36 | 21 | 3 | 6 |  6
N6 r6   | 18 |  1 | 0 | 7 | 10
N6 r7   | section absent
N7 r6   | 36 | 14 | 4 | 7 | 11
N7 r7   | 15 |  1 | 1 | 3 | 10
total listed 269, ungraded 85
```

| need | n1 (r6) | n2 (r7) | m | overlap (S≥2) | N̂ LP | seen | unseen (LP) | N̂ Chapman, unseen | Rule 2 |
|---|---|---|---|---|---|---|---|---|---|
| N1 | 8 | 8 | 0 | — | undefined | 16 | — | 80, 80% | FAIL (m=0) |
| N2 | 5 | 18 | 1 | 10.1016/0167-9457(90)90005-x | 90.0 | 22 | 76% | 56, 61% | FAIL |
| N3 | 19 | 14 | 5 | 10.1007/s40593-015-0089-1, 10.1037/0033-2909.119.2.254, 10.1073/pnas.2422633122, 10.1207/s1532690xci2103_01, 10.3102/00346543058001079 | 53.2 | 28 | 47% | 49, 43% | FAIL |
| N4 | 15 | — | — | — | — | — | — | — | VOID-ROUND (r7 has no Found DOIs) |
| N5 | 6 | 6 | 0 | — | undefined | 12 | — | 48, 75% | FAIL (m=0) |
| N6 | 10 | — | — | — | — | — | — | — | VOID-ROUND (r7 has no Found DOIs) |
| N7 | 11 | 10 | 1 | 10.32664/icobits.v1.130 | 110.0 | 20 | 82% | 65, 69% | FAIL |

Sensitivity, counting every listed id regardless of grade:

```
N1 n1=13 n2=15 m=0            Chapman 223, unseen 87%
N2 n1=14 n2=25 m=1  LP 350    unseen 89%
N3 n1=42 n2=23 m=6  LP 161    unseen 63%
N5 n1=13 n2=36 m=2  LP 234    unseen 80%
N7 n1=36 n2=15 m=2  LP 270    unseen 82%
```

- Matching titles through the ledger found no pair of ids that name one paper under two identifiers, so m is not understated by identifier form.
- For N4 and N6 the ledger rows by round are informational only. At S≥2, N4 has r6=11, r7=7, m=0, and N6 has r6=5, r7=6, m=0.

## Rule 3 — seed coverage, recomputed from the ledger

Method as in saturation-r5.md: seed-probe's 51 per-citation rows, matched by DOI, arXiv id or title in sources.csv, over the r3 section-to-need mapping.

New matches since r5:
- Seed line 47, Chi, Siler & Jeong 2004 (10.1207/s1532690xci2203_4). t2-n4-r6 ledgered it at S1 (metadata only) and t2-n4-r7 at S0/R0/O0, flagged "not graded".
- Seed line 143, arXiv 2409.16490. t2-n4-r6 ledgered it at S2 (abstract-only).

| need | seed section(s) | checkable | found | coverage | Rule 3 |
|---|---|---|---|---|---|
| N1 | §1 | 7 | 3 (+Chi et al.) | 43% | FAIL |
| N2 | §4 + §7 | 12 + 5 | 6 + 0 | 35% | FAIL |
| N3 | §6 | 12 | 2 | 17% | FAIL |
| N4 | §3 | 6 | 2 (+2409.16490) | 33% | FAIL |
| N5 | §5 | 1 | 0 | 0% | FAIL |
| N6 | proxy: §6 lines 254–256 | 3 | 0 | 0% | FAIL |
| N7 | §2 | 8 | 6 | 75% | FAIL |

Independence:
- prompts/round-6-7.md carries no seed content.
- The header of n7-r7.md cites "audit/saturation-r5.md", and that file names seed citations. N7-r7 ledgered no seed citation that was missing before, so §2 coverage is unaffected.
- No other r6/r7 file mentions the audits or the seed.

## Rule 4 — ledger closure (S≤2 claims closed)

```
need | total | VERIFIED | REFUTED | UNVERIFIABLE | SURVEYED S≤2 (closed) | SURVEYED S≥3 (open) | S≥3 claims with a status row
N1   | 68 | 21 | 1 | 13 | 33 | 0 | 35/35
N2   | 61 | 23 | 1 | 17 | 20 | 0 | 41/41
N3   | 67 | 17 | 1 | 28 | 21 | 0 | 46/46
N4   | 65 |  7 | 0 |  9 | 49 | 0 | 16/16
N5   | 65 | 16 | 1 |  2 | 46 | 0 | 19/19
N6   | 61 | 15 | 0 | 14 | 32 | 0 | 29/29
N7   | 77 | 34 | 2 |  6 | 33 | 2 | 42/44
open: N7-r7-05 (S4 R2 O1, transfer), N7-r7-06 (S4 R2 O1, skill_per_hour); both rest on 10.3390/bs16091583; neither has a verify/claims file
```

Integrity checks: no duplicate claim_ids, no orphan status rows, and every status row's file exists.

| need | Rule 4 | PLAN literal ("none SURVEYED") |
|---|---|---|
| N1 | PASS | FAIL (33) |
| N2 | PASS | FAIL (20) |
| N3 | PASS | FAIL (21) |
| N4 | PASS | FAIL (49) |
| N5 | PASS | FAIL (46) |
| N6 | PASS | FAIL (32) |
| N7 | **FAIL (2 open)** | FAIL (35) |

## Rule 5 — axis closure

Normalized tokens: `skill per hour` (35) and `skill/hour` (34) were folded into `skill_per_hour` (167).

```
need | skill_per_hour     | durability     | transfer        | sustainability
N1   | V9 S6 U1           | V10 S16 U9     | V1 S7 U1        | V1 S4 U2 R1
N2   | V10 S13 U9         | V8 U3          | V9 S7 U8 R1     | V2 S1
N3   | V16 S19 U20 R1     | V1 S2 U8       | V1 S1 U6        | none
N4   | V5 S43 U8          | V1             | V1 S12 U2       | none
N5   | V7 S27 U1          | V2 S4          | V5 S6 U1 R1     | V3 S9
N6   | U1                 | V5 S8 U4       | U2              | V12 S29 U9
N7   | V22 S13 U4 R1      | V8 S15 U1      | V10 S10 U1 R1   | V5 S8 U1
```

Escapes used where an axis holds 0 VERIFIED claims:

| need · axis | "No evidence" entries that name queries | Rule 5 |
|---|---|---|
| N3 · sustainability | n3-r1:94, n3-r3:107, n3-r7:78 | escape |
| N4 · sustainability | n4-r2:89. n4-r7:82 lists no query. | escape |
| N6 · skill_per_hour | n6-r3:56 (queries listed, none aimed at the axis). n6-r7:48 states none targeted. | escape, untargeted |
| N6 · transfer | n6-r2:66 (points to the search log). No round r2–r7 ran a transfer query. | escape, untargeted |

| need | Rule 5 (letter) | note |
|---|---|---|
| N1 | PASS | transfer and sustainability each rest on 1 VERIFIED claim |
| N2 | PASS | |
| N3 | PASS | |
| N4 | PASS | durability rests on a single claim, VERIFIED |
| N5 | PASS | durability now 2 VERIFIED (0 at r5) |
| N6 | PASS | two axes pass by untargeted escape only |
| N7 | PASS | |

## Void rounds (r6, r7)

```
round  | query rows | OpenAlex rows returning results | exact reuse max (vs) | near-dup J≥0.6 max (vs)
n1-r6  | 20 | 0/4   | 0% | 15% (r1)
n1-r7  | 16 | 0/2   | 0% | 12% (r6)
n2-r6  | 23 | 1/3   | 0% | 13% (r5)
n2-r7  | 46 | 0/15  | 7% (r6) | 15% (r4, r6)
n3-r6  | 33 | 6/10  | 9% (r1) | 18% (r1)
n3-r7  | 23 | 2/7   | 0% | 30% (r6)
n4-r6  | 30 | 6/13  | 0% | 13% (r2)
n4-r7  | 21 | 2/4   | 0% | 14% (r2)
n5-r6  | 14 | 4/7   | 0% | 14% (r3)
n5-r7  | 15 | 2/5   | 0% | 13% (r2)
n6-r6  | 19 | 0/2   | 0% | 11% (r2)
n6-r7  | 24 | 7/9   | 4% | 8%
n7-r6  | 21 | 1/9   | 5% (r1) | 33% (r1)
n7-r7  | 28 | 3/8   | 4% | 18% (r1)
```

The OpenAlex totals are 34 of 98. All 14 logs contain rows for OpenAlex, Crossref, ERIC, PMC and arXiv.

| clause | result |
|---|---|
| queries, databases, hit counts | pass. Rows without a hit count are blocked calls whose status is logged: n2-r7 explains 15 OpenAlex rows in prose (429 ×5, then 503 "search paused"), and n7-r6 logs "429/503 exhausted". |
| required database never attempted | pass, all 14: each blocked database was attempted with logged retries |
| query reuse >30% (exact) | pass, all 14 (maximum 9%). Near-duplicates reach 33% (n7-r6 vs n7-r1), which is expected when obvious queries are allowed. |
| S/R/O blank | pass by form, 0 blank. By function, **n4-r7 is void**: sources.csv line 687 carries S0/R0/O0 flagged "listed as not-read, not graded". S0 is the exclusion grade (PLAN §4), not a placeholder, so this row lacks a grade. |
| WebSearch | round-6-7.md does not require it, and the need-to-field mapping is not recorded. n2-r7 and n3-r6 log the session WebSearch budget exhausted at 200/200. |

## Verdict

| need | R1 | R2 | R3 | R4 | R5 | void | **Verdict** |
|---|---|---|---|---|---|---|---|
| N1 | FAIL | FAIL (m=0) | FAIL 43% | PASS | PASS | none | **OPEN** |
| N2 | FAIL | FAIL (76% unseen) | FAIL 35% | PASS | PASS | none | **OPEN** |
| N3 | FAIL | FAIL (47% unseen) | FAIL 17% | PASS | PASS | none | **OPEN** |
| N4 | FAIL | VOID | FAIL 33% | PASS | PASS | r7: no Found DOIs; line 687 S0 placeholder | **VOID-ROUND** |
| N5 | FAIL | FAIL (m=0) | FAIL 0% | PASS | PASS | none | **OPEN** |
| N6 | FAIL | VOID | FAIL 0% | PASS | PASS | r7: no Found DOIs | **VOID-ROUND** |
| N7 | FAIL | FAIL (82% unseen) | FAIL 75% | FAIL (2 open) | PASS | none | **OPEN** |

Zero SATURATED. N4 and N6 would be OPEN if rule 2 could be computed, because rule 1 fails for both.

## Round 8 — what to look for

Common to all seven:
- Write `## Found DOIs` (N4-r7 and N6-r7 lacked it).
- Ledger a real S/R/O for every Found id. Today 85 of 269 are ungraded and invisible to rule 2. S0 is not a placeholder.
- OpenAlex blocked 64 of 98 queries. n2-r7 logs the budget message "resets at midnight UTC". Schedule round 8 after the reset, or stagger the 14 agents, which share one IP budget.
- Keep full-population queries without avoid-lists, since that change produced the first recaptures.
- Do not give surveyors the audits or seed-probe.md.

- **N1.** m=0 at 8×8, from 28 listed ids. New S≥3: 3 and 5, with 5 of 8 abstract-only. Grade the 6 ungraded Found ids. Transfer holds 1 VERIFIED claim out of 9, and sustainability 1 out of 8. Look for S≥3 measurement studies with transfer or sustained-engagement outcomes.
- **N2.** r7 found 21 new sources, 11 of them S≥3 and all 11 abstract-only. Read those full texts first; a regrade may move rule 1. m=1. Grade the 8 ungraded Found ids. Sustainability holds 2 VERIFIED claims.
- **N3.** Closest to saturation: m=5, N̂=53, 47% unseen, and every recapture is a source that predates the pair. Grade the 22 ungraded Found ids, 19 of them in r6; that raises both n and m. New S≥3: 3 and 5. Durability holds 1 VERIFIED claim out of 11, and transfer 1 out of 8. Look for delayed-outcome (O2) intervention studies.
- **N4.** Re-run both captures with Found DOIs and real grades. All 6 new S≥3 sources in r6/r7 are abstract-only; new S=2 counts are 7 and 4. Skill/hour holds 5 VERIFIED claims against 43 SURVEYED. Durability has 1 claim in all, and transfer 1 VERIFIED out of 15. Look for S≥3 diagnosis-accuracy studies with delayed or transfer outcomes.
- **N5.** m=0 at 6×6. N5-r7 lists 36 ids, 24 of them ungraded: the largest ungraded pool of any round. Grade those first. r6's 5 new S≥3 sources were read in full, so the field is not thinning. Durability holds 2 VERIFIED claims out of 6.
- **N6.** Re-run r7 with Found DOIs. Skill/hour and transfer hold 0 VERIFIED claims (U1, U2), and in rounds r2–r7 no query was ever aimed at either axis. Run at least one query per axis. New S≥3: 2 and 3, with 4 of 5 abstract-only.
- **N7.** Verify N7-r7-05 and N7-r7-06 (S4, 10.3390/bs16091583) to close rule 4. m=1. Grade the 20 ungraded Found ids, 18 of them in r6. N7-r6 was the most blocked capture: OpenAlex returned results for 1 of 9 queries and arXiv for 0 of 3. Durability holds 8 VERIFIED claims against 15 SURVEYED.

---

Notification summary: No need is SATURATED: N1, N2, N3, N5 and N7 are OPEN, and N4 and N6 are VOID-ROUND because their round-7 files lack Found DOIs; rule 1 fails for all seven and rule 4 fails for N7 (N7-r7-05 and N7-r7-06, S4, have no status row). All seven need round 8, with Found DOIs written and every Found id graded (85 of 269 are ungraded), OpenAlex run after its budget resets, N4 and N6 captures re-run, and N7's two claims verified. The biggest gap is thin capture rather than literature: dropping the avoid-lists produced the first recaptures (N3 m=5, 47% unseen), but OpenAlex blocked 64 of 98 queries and a third of Found ids stayed ungraded, so no need is near the 10% bar yet.
