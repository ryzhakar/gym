# Saturation audit — round 5

Scope: N1–N7, rounds 1–5. Rules: PLAN §5 lines 242–260 plus the r5 changes (prompts/audit-r5.md): rules 1–2 on rounds 4 and 5; rule 2 from `## Found DOIs`, S≥2 per sources.csv; rule 4 with S≤2 claims closed; no Stage C cap (owner ruling "done at saturation", history/2026-09-26/events.md line 116, confirmed).

Inputs: ledger/sources.csv (599 rows), ledger/claims.csv (308), ledger/claims-status.csv (159; last row per claim_id), the search logs and Found DOIs sections of all 29 need-round files, verify/seed-probe.md, context/seed-citations.csv. Arithmetic ran as throwaway `uv run --no-project python -` over the CSVs. No script is kept.

Data defect: sources.csv lines 565, 569 and 576 (agent t2-n4-r5) carry 18 fields, because an unquoted comma splits one field. They were parsed right-anchored (the last 9 fields are fixed). After that parse, every row's round resolves to 0–5.

## Headline

1. **No need is SATURATED. All seven are VOID-ROUND.** Rounds 4 and 5 each skipped OpenAlex, and every field list in PLAN §2 T1 names it: zero OpenAlex queries in 14 of 14 logs. Each file records the skip as a budget set in the dispatch. Waive that void and every need is still OPEN, because rules 1, 2 and 3 fail for all seven.
2. **Rule 2: the Found DOIs fix removed the ledger artifact, but overlap is still m=0.** The six computable needs show zero overlap between r4 and r5 at S≥2. Across every identifier listed, graded or not, the overlap is one: an S1 source for N6. The records show two causes besides field size. First, the rounds deliberately avoided earlier angles, which N3-r4, N3-r5, N5-r4, N6-r4, N6-r5 and N7-r4 state outright and N7-r4 attributes to an "avoid the obvious" instruction. That breaks the independence Lincoln–Petersen assumes. Second, discovery ran through Crossref alone, examining 3–8 hits per query. Under this design, m=0 cannot tell a saturated need from an open one.
3. **Rule 1 fails for all seven even under the harshest count.** Count only sources whose full text was read, and every need except N4 still found a new S≥3 source in r4 or r5; N4 fails on new S=2 sources (5 and 8). N1 comes closest: r5 found 0 new S≥3 but 4 new S=2.
4. **Rule 4 passes for all seven under the r5 exemption.** All 153 claims graded S≥3 have a status row. Read the PLAN literally ("none SURVEYED") and 155 SURVEYED claims remain, all S≤2.
5. **seed-probe.md undercounts.** It marks 7 citations "not found" that sit in sources.csv from rounds 0–2. Recomputed coverage still fails the 80% bar for every need. Rounds 4–5 added no new seed citation to the ledger.

## Rule 1 — two consecutive rounds, zero new S≥3, ≤1 new S=2

"new" means the DOI/URL is not tagged to the need in an earlier round or earlier in the same round (normalized: lowercase, `https://doi.org/` stripped, arXiv forms unified). Rounds 1–3 are shown for context; the verdict uses r4 and r5.

```
need r  | rows | new | seen | new S≥3 | new S=2 | new S≤1 | ungraded | S/R/O blank
N1 r1   | 17 | 17 | 0 |  6 | 4 |  7 |  0 |  0
N1 r3   | 16 | 16 | 0 |  5 | 1 |  3 |  7 |  7
N1 r4   |  6 |  6 | 0 |  5 | 1 |  0 |  0 |  0
N1 r5   |  4 |  4 | 0 |  0 | 4 |  0 |  0 |  0
N2 r1   | 14 | 14 | 0 |  5 | 3 |  6 |  0 |  0
N2 r3   | 10 | 10 | 0 |  6 | 1 |  0 |  3 |  3
N2 r4   |  8 |  8 | 0 |  3 | 1 |  4 |  0 |  0
N2 r5   |  5 |  5 | 0 |  4 | 1 |  0 |  0 |  0
N3 r1   | 19 | 19 | 0 |  7 | 5 |  7 |  0 |  0
N3 r3   | 10 | 10 | 0 |  7 | 2 |  1 |  0 |  0
N3 r4   | 11 | 11 | 0 |  8 | 2 |  1 |  0 |  0
N3 r5   |  6 |  6 | 0 |  5 | 0 |  1 |  0 |  0
N4 r2   | 17 | 17 | 0 |  4 | 5 |  8 |  0 |  1
N4 r3   | 14 | 14 | 0 |  2 | 9 |  3 |  0 |  0
N4 r4   | 12 | 12 | 0 |  6 | 5 |  1 |  0 |  0
N4 r5   | 14 | 14 | 0 |  1 | 8 |  5 |  0 |  0
N5 r2   | 24 | 24 | 0 |  1 | 2 |  6 | 15 | 15
N5 r3   | 13 | 13 | 0 |  1 | 7 |  0 |  5 |  5
N5 r4   |  8 |  8 | 0 |  2 | 0 |  6 |  0 |  0
N5 r5   | 16 | 16 | 0 |  4 | 8 |  4 |  0 |  0
N6 r2   | 19 | 19 | 0 |  6 | 3 | 10 |  0 |  0
N6 r3   |  8 |  8 | 0 |  4 | 3 |  1 |  0 |  0
N6 r4   |  8 |  8 | 0 |  2 | 1 |  5 |  0 |  0
N6 r5   |  8 |  7 | 1 |  5 | 2 |  0 |  0 |  0
N7 r1   | 27 | 27 | 0 | 11 | 5 | 11 |  0 |  0
N7 r2   |  3 |  3 | 0 |  0 | 2 |  1 |  0 |  0
N7 r3   | 12 | 12 | 0 |  9 | 1 |  2 |  0 |  0
N7 r4   |  8 |  8 | 0 |  2 | 2 |  4 |  0 |  0
N7 r5   |  8 |  8 | 0 |  4 | 1 |  3 |  0 |  0
```

The r1–r3 rows reproduce the r3 audit's counts.

New S≥3 sources in r4 and r5 whose full text was not read (`full_text_read=N`):

```
N1 r4 2/5  r5 0/0 | N2 r4 2/3 r5 2/4 | N3 r4 5/8 r5 3/5 | N4 r4 6/6 r5 1/1
N5 r4 0/2  r5 4/4 | N6 r4 0/2 r5 3/5 | N7 r4 1/2 r5 4/4
```

| need | new S≥3 (r4, r5) | new S=2 (r4, r5) | different agents | ≥12 queries, ≥3 DBs | Rule 1 |
|---|---|---|---|---|---|
| N1 | 5, 0 | 1, 4 | yes | yes | FAIL |
| N2 | 3, 4 | 1, 1 | yes | yes | FAIL |
| N3 | 8, 5 | 2, 0 | yes | yes | FAIL |
| N4 | 6, 1 | 5, 8 | yes | yes | FAIL |
| N5 | 2, 4 | 0, 8 | yes | yes | FAIL |
| N6 | 2, 5 | 1, 2 | yes | yes | FAIL |
| N7 | 2, 4 | 2, 1 | yes | yes | FAIL |

Round 5 found more new S≥3 than round 4 for N2, N5, N6 and N7. On this count the fields are not running dry.

## Rule 2 — Lincoln–Petersen on Found DOIs, r4 vs r5, S≥2

Input: every `- <id>` line of the `## Found DOIs` sections, normalized, `new` and `seen` both counted, kept only where the id's highest S in sources.csv is ≥2. An id with no grade drops out, either because it is absent from the ledger or because its row is blank.

```
need r  | listed | absent from ledger | in ledger, S blank | S≤1 | S≥2
N1 r4   | 15 |  5 | 1 | 2 |  7
N1 r5   | 14 | 10 | 0 | 0 |  4
N2 r4   |  8 |  0 | 0 | 4 |  4
N2 r5   | 14 |  5 | 2 | 0 |  7
N3 r4   | 14 |  3 | 0 | 1 | 10
N3 r5   | 11 |  5 | 0 | 1 |  5
N4 r4   | 17 |  5 | 0 | 1 | 11
N4 r5   | 19 |  4 | 0 | 5 | 10
N5 r4   | section absent
N5 r5   | 17 |  0 | 0 | 4 | 13
N6 r4   |  8 |  0 | 0 | 5 |  3
N6 r5   | 16 |  8 | 0 | 1 |  7
N7 r4   | 56 | 46 | 0 | 4 |  6
N7 r5   | 14 |  4 | 0 | 4 |  6
raw overlap r4∩r5 over all listed ids: N6 {10.1037/0003-066x.55.1.68 (S1)}; all others ∅
```

N̂: Lincoln–Petersen n1·n2/m is undefined when m=0, so the Chapman form (n1+1)(n2+1)/(m+1)−1 is used. seen = |r4 ∪ r5|, and unseen = 1 − seen/N̂.

| need | n1 (r4) | n2 (r5) | m | N̂ Chapman | seen | unseen | Rule 2 |
|---|---|---|---|---|---|---|---|
| N1 | 7 | 4 | 0 | 39 | 11 | 72% | FAIL (m=0) |
| N2 | 4 | 7 | 0 | 39 | 11 | 72% | FAIL (m=0) |
| N3 | 10 | 5 | 0 | 65 | 15 | 77% | FAIL (m=0) |
| N4 | 11 | 10 | 0 | 131 | 21 | 84% | FAIL (m=0) |
| N5 | — | 13 | — | — | — | — | VOID-ROUND (r4 has no Found DOIs) |
| N6 | 3 | 7 | 0 | 31 | 10 | 68% | FAIL (m=0) |
| N7 | 6 | 6 | 0 | 48 | 12 | 75% | FAIL (m=0) |

Chapman's N̂ at m=0 is an upper-biased estimate. It is reported as an order of magnitude, not as a measurement.

What m=0 does and does not show:
- The r3 artifact is gone: an append-only ledger no longer hides recaptures, since `seen` ids now appear in the Found DOIs lists. Recaptures still do not happen.
- Independence is broken by design. Six r4/r5 files state that they avoided angles earlier rounds had mined. N3-r5 builds its avoid-list from r1, r3 and r4, and N6-r5 from r2–r4. An avoid-list pushes m toward 0 whatever the population size.
- Capture effort per round is small. Discovery ran on Crossref bibliographic search, which returns 10⁶–10⁷ total hits per query, of which agents examined 3–8.
- Found-but-unledgered ids never reach the S≥2 filter: 98 of the 223 listed ids have no grade. N7-r4 alone lists 45 DOIs absent from the ledger, plus a line of 8 PMCIDs counted here as one id; N1-r5 lists 10.

Under this search design, rule 2 cannot pass even for a need that is in fact saturated.

## Rule 3 — seed coverage, recomputed against the current ledger

Unit: the per-citation rows of seed-probe.md's table. It has 51 rows, although its summary says 45, so the file is inconsistent with itself. "Found" means the paper appears in sources.csv, matched by DOI, arXiv id or title. Section-to-need mapping is the r3 audit's, which is inferred and not authored by the plan.

seed-probe.md marks 7 citations "N" that are in the ledger, all from rounds 0–2, before the probe:

| seed line | paper as ledgered | ledger lines (round) |
|---|---|---|
| 28 | 10.1073/pnas.2422633122, the published version under the same title | 180 (r0), 286 and 293 (r1) |
| 84 | 10.1080/00461520.2011.611369 | 143 (r0) |
| 90 | 10.1038/s41598-025-97652-6 | 179 (r0), 294 (r1) |
| 169 | 10.1177/0956797614535810 | 76 (r0), 364 (r2) |
| 170 | 10.1177/1745691616635591 | 78 (r0), 365 (r2) |
| 187 | 10.1177/1529100612453266 | 4 (r0) |
| 234 | 10.1207/s1532690xci2103_01 | 146 (r0), 276 (r1), 353 (r2) |

Found after the probe:
- Seed line 95 (10.1596/1813-9450-11125), found in r3.
- Seed line 142 (10.1145/3774398.3811609, published version), found in r3.

Rounds 4–5 added none:
- Bloom's r5 row re-tags a round-0 row.
- D'Mello et al. 2014 (10.1016/j.learninstruc.2012.05.003) appears in N3-r5's Found DOIs but has no ledger row, so it does not count.

| need | seed section(s) | checkable | found | coverage | Rule 3 |
|---|---|---|---|---|---|
| N1 | §1 | 7 | 2 | 29% | FAIL |
| N2 | §4 + §7 | 12 + 5 | 6 + 0 | 35% | FAIL |
| N3 | §6 | 12 | 2 | 17% | FAIL |
| N4 | §3 | 6 | 1 | 17% | FAIL |
| N5 | §5 | 1 | 0 | 0% | FAIL |
| N6 | proxy: §6 lines 254–256 | 3 | 0 | 0% | FAIL |
| N7 | §2 | 8 | 6 | 75% | FAIL |

The rule's literal denominator is "seed citations with S≥2". Dropping ungraded, unfound citations from it would score N4 at 1/1 = 100%, with 5 of 6 citations missing, and N7 at 4/5 = 80%. That reading rewards leaving unfound citations ungraded, so it is not used. Counting only S≥2 while keeping the ungraded unfound citations, N7 scores 4/6 = 67%.

Independence caveats:
- The round-3 N2/N3 prompt leak stands, as recorded in the r3 audit.
- The r4/r5 dispatch prompts are not on disk, so their independence from seed.md, seed-probe.md and saturation-r3.md cannot be checked from the records.
- N3-r5 ran bibliographic lookups for Bloom 1984 and for D'Mello et al.'s confusion study. seed-probe.md and saturation-r3.md both name these two as gaps.

## Rule 4 — ledger closure (S≤2 claims closed)

```
need | total | VERIFIED | REFUTED | UNVERIFIABLE | SURVEYED S≤2 (closed) | SURVEYED S≥3 (open)
N1   | 47 | 13 | 1 |  8 | 25 | 0
N2   | 41 | 17 | 1 | 13 | 10 | 0
N3   | 44 | 15 | 1 | 17 | 11 | 0
N4   | 42 |  5 | 0 |  4 | 33 | 0
N5   | 44 |  7 | 1 |  1 | 35 | 0
N6   | 41 | 11 | 0 |  9 | 21 | 0
N7   | 49 | 23 | 2 |  4 | 20 | 0
S≥3 claims with a status row: N1 22/22, N2 31/31, N3 33/33, N4 9/9, N5 9/9, N6 20/20, N7 29/29
```

Integrity checks: no duplicate claim_ids, no status rows for unknown ids, and all 159 status rows point to an existing verify/claims/*.md file.

| need | open | Rule 4 (r5) | PLAN literal |
|---|---|---|---|
| N1 | 0 | PASS | FAIL (25 SURVEYED) |
| N2 | 0 | PASS | FAIL (10) |
| N3 | 0 | PASS | FAIL (11) |
| N4 | 0 | PASS | FAIL (33) |
| N5 | 0 | PASS | FAIL (35) |
| N6 | 0 | PASS | FAIL (21) |
| N7 | 0 | PASS | FAIL (20) |

N4 and N5 rest mostly on S≤2 evidence, with 5 and 7 VERIFIED claims out of 42 and 44.

## Rule 5 — axis closure

The axes column of claims.csv was normalized: `skill per hour`, `skill/hour` → `skill_per_hour`. Status per claim is the last status row, or SURVEYED where no row exists.

```
need | skill_per_hour            | durability              | transfer                      | sustainability
N1   | V6 S4                     | V6 S11 U7               | V1 S6                         | V0 S4 U1 R1
N2   | V7 S4 U6                  | V6 U3                   | V8 S6 U7 R1                   | V2 S1
N3   | V14 S10 U15 R1            | V1 S1 U5                | V1 S1 U2                      | none
N4   | V3 S28 U3                 | V1                      | V1 S9 U1                      | none
N5   | V2 S23                    | V0 S3                   | V2 S4 U1 R1                   | V3 S5
N6   | none                      | V4 S8 U3                | V0 U1                         | V9 S18 U7
N7   | V17 S6 U3 R1              | V6 S10                  | V6 S7 U1 R1                   | V2 S5 U1
(V VERIFIED, S SURVEYED, U UNVERIFIABLE, R REFUTED)
```

For each axis with 0 VERIFIED, the "No evidence found" entries under that axis heading:

| need · axis | entries naming queries | entries stating no query targeted the axis |
|---|---|---|
| N1 · sustainability | n1-r4:87 (2 queries) | — |
| N3 · sustainability | n3-r1:94, n3-r3:107 | n3-r4:81, n3-r5:93 |
| N4 · sustainability | n4-r2:89 (#20, #21) | n4-r3:98, n4-r4:85 |
| N5 · durability | n5-r2:65, n5-r3:74, n5-r5:65 | — |
| N6 · skill_per_hour | n6-r3:56 (queries listed, none aimed at the axis) | n6-r2:52, n6-r4:67, n6-r5:71 |
| N6 · transfer | n6-r2:66 (points to the search log) | n6-r4:81, n6-r5:82 |

| need | skill/hour | durability | transfer | sustainability | Rule 5 (letter) | r3-audit reading (an open claim blocks the escape) |
|---|---|---|---|---|---|---|
| N1 | PASS | PASS | PASS | escape | PASS | FAIL (4 SURVEYED on sustainability) |
| N2 | PASS | PASS | PASS | PASS | PASS | PASS |
| N3 | PASS | PASS | PASS | escape | PASS | PASS |
| N4 | PASS | PASS | PASS | escape | PASS | PASS |
| N5 | PASS | escape | PASS | PASS | PASS | FAIL (3 SURVEYED on durability) |
| N6 | escape, untargeted | PASS | escape, untargeted | PASS | PASS | PASS on letter; no N6 round in r2–r5 ran a query aimed at skill/hour or transfer |
| N7 | PASS | PASS | PASS | PASS | PASS | PASS |

## Void rounds

Clauses checked for r4 and r5: search log lacks queries, databases or hit counts; reuse of a prior round's queries >30%; a database named by the field list was skipped; any source row lacks S/R/O.

Query reuse compares against every earlier round of the same need. Tokens are lowercased, with stopwords and query operators stripped. The table shows the worst pair for each round.

```
round  | queries | DBs (log)                              | exact reuse max | near-dup (Jaccard≥0.6) max
n1-r4  | 27 | arxiv crossref eric pmc                         | 4% (vs r3)  | 4%
n1-r5  | 24 | arxiv crossref osf s2 unpaywall                 | 0%          | 4%
n2-r4  | 22 | arxiv crossref eric pmc                         | 0%          | 9% (vs r3)
n2-r5  | 36 | arxiv crossref eric pmc                         | 3% (vs r1)  | 17% (vs r1)
n3-r4  | 17 | arxiv crossref eric pmc                         | 0%          | 0%
n3-r5  | 16 | arxiv crossref eric (+pmc, s2 per header)       | 0%          | 0%
n4-r4  | 20 | arxiv crossref eric s2                          | 5% (vs r2)  | 15% (vs r2)
n4-r5  | 15 | arxiv crossref eric pmc                         | 0%          | 7%
n5-r4  | 13 | arxiv crossref eric                             | 8% (vs r2)  | 8%
n5-r5  | 23 | arxiv crossref eric pmc                         | 0%          | 4%
n6-r4  | 25 | arxiv crossref eric s2 unpaywall                | 8% (vs r2)  | 8%
n6-r5  | 39 | crossref eric pmc s2 unpaywall                  | 0%          | 3%
n7-r4  | 20 | arxiv crossref eric pmc                         | 0%          | 5%
n7-r5  | 20 | arxiv crossref eric pmc                         | 5% (vs r1)  | 10%
```

| clause | r4, r5 result |
|---|---|
| queries, databases, hit counts present | pass, all 14 |
| reuse >30% | pass, all 14 (maximum 17%, near-duplicate) |
| S/R/O blank on any source row | pass, all 14 (0 blank; the round-4 fix held) |
| field-list database skipped | **void, all 14**: OpenAlex, which all six T1 field rows name, has 0 query rows in every r4/r5 log. WebSearch, named by the coaching and AI-tutoring fields, also has 0. Each file cites the dispatch budget. |

Rounds 1–3 under the same database clause: OpenAlex appears as a database only in n1-r1, n2-r1 and n3-r1. The r3 audit did not apply this clause, and every other r1–r3 round is void under it. No verdict changes, because the verdict rests on r4 and r5.

As with the r3 void for ungraded rows, the mechanism here is the orchestrator's budget and not surveyor negligence. The rule is applied as written.

## Verdict

| need | Rule 1 | Rule 2 | Rule 3 | Rule 4 | Rule 5 | void (r4, r5) | **Verdict** | with the void waived |
|---|---|---|---|---|---|---|---|---|
| N1 | FAIL | FAIL | FAIL 29% | PASS | PASS | both | **VOID-ROUND** | OPEN |
| N2 | FAIL | FAIL | FAIL 35% | PASS | PASS | both | **VOID-ROUND** | OPEN |
| N3 | FAIL | FAIL | FAIL 17% | PASS | PASS | both | **VOID-ROUND** | OPEN |
| N4 | FAIL | FAIL | FAIL 17% | PASS | PASS | both | **VOID-ROUND** | OPEN |
| N5 | FAIL | VOID | FAIL 0% | PASS | PASS | both, plus no Found DOIs in r4 | **VOID-ROUND** | OPEN |
| N6 | FAIL | FAIL | FAIL 0% | PASS | PASS | both | **VOID-ROUND** | OPEN |
| N7 | FAIL | FAIL | FAIL 75% | PASS | PASS | both | **VOID-ROUND** | OPEN |

Zero needs are SATURATED under every reading tested here.

## Round 6 — what to look for

Common to all seven:
- Use OpenAlex, and WebSearch where the field list names it; otherwise the round is void again.
- Drop avoid-lists. Two independent full-population rounds are what rule 2 needs, and a truly saturated field will then show recaptures.
- Grade and ledger every Found DOI, since ungraded ids are invisible to rule 2.
- Do not give surveyors this audit, seed-probe.md or saturation-r3.md, because all three name seed citations.

- **N1.** r5 came closest to rule 1: 0 new S≥3, 4 new S=2. Grade the 16 ungraded Found ids: 10 from r5, 6 from r4. The sustainability axis holds 0 VERIFIED claims against 4 SURVEYED, 1 UNVERIFIABLE and 1 REFUTED, and its escape rests on two r4 queries. Transfer holds 1 VERIFIED claim out of 7. Look for S≥3 evidence that measures sustainability and transfer.
- **N2.** Not thinning: r5 found 4 new S≥3, 2 of them S4. Grade the 7 ungraded r5 Found ids, 2 of which are still-blank r3 rows (10.1102/2051-7726.2021.a019, 10.1177/001872088502700304). The transfer axis carries 7 UNVERIFIABLE and 6 SURVEYED claims against 8 VERIFIED, and sustainability has 2 VERIFIED. Look for reachable full texts on transfer.
- **N3.** Highest new-strong yield in r4–r5 (8, 5). 17 of 44 claims are UNVERIFIABLE, the largest share of any need. Durability and transfer have 1 VERIFIED each. Grade the 8 ungraded Found ids. Look for delayed-test (O2) evidence on intervention timing and content.
- **N4.** Largest Chapman N̂ (131). All 6 new S≥3 sources in r4 are abstract-only. 33 of 42 claims are SURVEYED S≤2, with 5 VERIFIED. Durability and transfer have 1 VERIFIED each, and sustainability was never targeted after r2. Read full texts of r4's six strong sources and look for S≥3 designs with delayed or transfer outcomes.
- **N5.** Write a Found DOIs section, which r4 lacked. All 4 new S≥3 sources in r5 are abstract-only. 35 of 44 claims are SURVEYED S≤2. Durability has 0 VERIFIED, and skill/hour has 2 VERIFIED out of 25. Look for full-text S≥3 evidence on elite versus good practitioners with a delayed outcome.
- **N6.** r5 found 5 new S≥3, 3 of them abstract-only. Grade the 8 ungraded r5 Found ids. Skill/hour has no claims and transfer has 1 UNVERIFIABLE, and both escapes were never targeted. Run at least one query aimed at each of those axes so the escape reflects an actual search.
- **N7.** The largest unmined pool: N7-r4 surfaced 55 DOIs, 45 of them absent from the ledger, plus 8 PMCIDs. Grade those first, since rule 2 cannot count them otherwise. All 4 new S≥3 sources in r5 are abstract-only. Durability holds 6 VERIFIED against 10 SURVEYED.

---

Notification summary: All seven needs (N1–N7) are VOID-ROUND and none is SATURATED, because rounds 4–5 skipped OpenAlex, which every field list names; with that waived, all seven are still OPEN, failing rule 1 (new S≥3 in r4 or r5), rule 2 (m=0) and rule 3 (seed coverage 0–75%), while rules 4 and 5 pass. All seven need round 6: with OpenAlex, without avoid-lists, and grading every Found DOI, starting with N7-r4's 45 DOIs absent from the ledger and N1/N6's ungraded r5 ids. The biggest gap is method, not literature: m=0 is guaranteed by avoid-lists plus Crossref-only discovery, so rule 2 cannot tell saturated from open until two independent full-population rounds run.
