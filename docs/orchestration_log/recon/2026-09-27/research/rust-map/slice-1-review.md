# Slice 1 review — Rust map, batch 1 (English)

Reviewer: t5-slice-review (fable), 2026-09-28. Read-only. Figures from the files named per row; counts over `MAP` by script (`check_map.py`, plus two throwaway scripts over `maps/rust/**` and `merge-v3/crosswalk-b1.csv`). No verdicts on content.

Binding crosswalk: `merge-v3/` (the README cites it; `merge-final/` and `merge-v2/` are superseded, `merge-v3/merged-questions-b1.md` line 3). Where an earlier crosswalk's figure is quoted, it is named.

## 1. Coverage per stratum

Sample: 198 rows per team, 18 per cell × 11 cells, 17 rows drawn by both teams (`samples/batch-1.md`). Read logs: team A 358 rows over 188 distinct frame ids, 10 unreachable, 2,950 minutes self-reported; team B 342 rows over 189 ids, 3 unreachable, 2,864 minutes (`team-{a,b}/readlog-b1-*.csv`; re-passes sR, sT, sB, bk re-log rows, so rows exceed ids).

| stratum | A only | B only | both | seen | Chapman N̂ | unseen | 95% CI on N̂ | Chao1 N̂ | unseen | 95% CI on N̂ | Q per sampled row |
|---|---|---|---|---|---|---|---|---|---|---|---|
| core | 86 | 87 | 36 | 209 | 411.2 | 49.2% | [319, 503] | 537.9 | 61.1% | [386, 690] | 3.80 |
| wasm | 26 | 28 | 17 | 71 | 111.4 | 36.3% | [81, 142] | 151.0 | 53.0% | [88, 214] | 1.77 |
| embedded | 33 | 21 | 16 | 70 | 110.8 | 36.8% | [80, 142] | 188.2 | 62.8% | [91, 286] | 1.79 |
| distributed | 19 | 24 | 15 | 58 | 86.5 | 32.9% | [63, 110] | 115.0 | 49.6% | [64, 166] | 1.29 |
| web | 28 | 15 | 13 | 56 | 86.0 | 34.9% | [60, 112] | 136.2 | 58.9% | [61, 211] | 1.02 |
| desktop-cli-ui | 19 | 15 | 10 | 44 | 69.9 | 37.1% | [46, 94] | 129.3 | 66.0% | [37, 222] | 1.02 |
| ml | 13 | 21 | 8 | 42 | 72.3 | 41.9% | [43, 102] | 117.0 | 64.1% | [35, 199] | 1.08 |
| decentralized-iroh | 13 | 18 | 10 | 41 | 62.3 | 34.2% | [42, 83] | 59.4 | 30.9% | [39, 80] | 1.14 |
| cloud-workers | 21 | 8 | 9 | 38 | 54.8 | 30.7% | [37, 73] | 94.3 | 59.7% | [30, 159] | 1.03 |
| frontend | 9 | 9 | 7 | 25 | 35.1 | 28.8% | [23, 48] | 106.0 | 76.4% | [−30, 242] | 0.69 |
| other | 5 | 11 | 6 | 22 | 29.9 | 26.3% | [19, 41] | 59.5 | 63.0% | [1, 118] | — (0 rows sampled) |
| swift-interop | 4 | 2 | 2 | 8 | 10.7 | 25.0% | [5, 16] | 20.5 | 61.0% | [−13, 54] | 0.21 |
| all canonical | 168 | 180 | 51 | 399 | | | | | | | |

Sources: A/B/both from `merge-v3/crosswalk-b1.csv` (matches n1, n2, m in `merge-v3/estimate/closure-b1.md`); estimates and CIs from that closure file; Q per sampled row = seen ÷ sampled rows carrying the hint (`samples/batch-1-team-{a,b}.csv`). 401 Questions in `MAP`: 399 with captures plus 2 carried only by re-homed Claims, `domains: []` (`compile/compile-b1.md` § 2 Questions with no Domain). Captures per canonical Question, (team, source) pairs: 323 seen once, 54 twice, 22 three or more — f1 dominates, which is what keeps Chao1 above Chapman.

Thin: swift-interop (8 seen, rule 4 FAIL; 27 of 38 sampled rows and 169 of 262 in-window frame rows under that hint are forums.swift.org threads, which all three audits pass as Swift-internal — `audit/audit-b1.md` f001837, f003923; `audit-b1-sendback.md` f002042; `audit-b1-third.md` f001677, f002042, f004174, f004371); other (22 seen, 0 rows sampled — the tag is assigned by the merger after the fact, so its estimate is not a sampling estimate); frontend (25 seen, Chao1 CI crosses zero). Empty: none. Non-English: zero rows read (`fable-plan.md` OP7).

What the figures cannot show. Every stratum FAILs all of rule parts 1–3; parts 2 and 3 fail by construction (one batch; `estimate.py` was run without `--audit-pass` or `--merge-check-agreement`). The unseen fraction measures the merge grain as much as coverage: the same extracts under three grain rules give core unseen 61.6% (`merge-final/estimate/closure-b1.md`, 387 Questions), 30.7% (`merge-v2/estimate/closure-b1.md`, 271) and 49.2% (`merge-v3`, 401); m in wasm and frontend rests largely on one book both teams drew (f000256, 11 of the 51 two-team Questions, `merge-v3/merged-questions-b1.md` § Counts). Correlated misses between two Claude teams are invisible to both estimators (plan § 9 T1). Team B's third-pass Claims were struck at 13/36 (`audit/strike-b1-third.md`), so "seen" counts Questions whose Claims later failed the bar; the crosswalk removed 14 Claim-less captures but not Questions whose only Claims are `voice-below-bar`.

## 2. Quality per stage

| stage | figure | file |
|---|---|---|
| Audit, pass 1 | A FAIL: 10 nothing-new + 1 drop sampled, 3 misses (f012428, f000227 record, f011125 wording). B FAIL: 11 + 1, 1 miss (f002937). Census of nothing-new reasons citing "no opposing voice": A 11/97, B 30/101 | `audit/audit-b1.md` |
| Audit, send-back | A FAIL: 6 + 1, 3 misses (f004169, f000149 drop, f011484 record). B FAIL: 5, 2 misses (f002233, f005312). Rule 6 re-worded after pass 1 | `audit/audit-b1-sendback.md` |
| Audit, third pass | A FAIL: 5 of 46 + 1 drop, miss f000217 (fetch fault: Wayback lookup missed www host). B PASS: 5 of 33. Rules 8 and 9 added before this pass | `audit/audit-b1-third.md` |
| Strike check | 54 third-pass Claims: 38 KEEP (9 weak), 16 STRIKE; A 3/18, B 13/36. Three earlier audit passes (f003375, f001890, f011688) reverse under the later rules | `audit/strike-b1-third.md` |
| Merge check 1 (vs `merge/`) | 58/66 = 87.9% [77.9, 93.7]; FAIL → adjudication (`merge-final/`) | `merge/merge-check-b1.md`, `merge-final/adjudication-b1.md` |
| Adjudication M1 vs M2 | co-member sets identical 369/420 = 87.9%; pair Jaccard 55.9%; M1 missed 20 team-b items by parser | `merge-final/adjudication-b1.md` § 2 |
| Merge check 2 (vs `merge-v2/`) | 51/94 = 54.3% [44.2, 64.0]; 20 MISS (checker), 16 GRAIN, 7 HOLD | `merge-check2/merge-check-b1.md` |
| Merge check 3 (vs `merge-v3/`) | population 85/109 = 78.0% [69.3, 84.7]; in-sample 104/109 = 95.4%, inflated (90 of 109 items have no in-sample co-member); after reason v3 right on 19 of 24, 5 held, 3 of those rejoined by lead ruling | `merge-check3/merge-check-b1.md`; `merge-v3/merged-questions-b1.md` § Corrections |
| Fill, Claim→Position | 762/772 = 98.7% agree; 9 by third fill, 1 `unresolved`; resolver's blinding lapsed on the 10 third fills, a fresh instance matched 9/10; the mismatch (`a-sa30-f013276-c5`) set `unresolved` by lead | `fill/resolve-b1.md`; `compile/compile-b1.md` § Disposition |
| Fill, tag | 410/607 = 67.6% agree; 192 by majority; 9 unresolved (untagged in MAP). Tag definitions written by the resolver; `opinion-map.md` names the tags without defining them | `fill/resolve-b1.md` § Tags |
| Fill, summaries | picked by quoted-word overlap: 388 by share, 207 tie → shorter; no semantic read | `fill/resolve-b1.md` § Summaries |
| Fill vs merger key | 23 of 772 differ; 7 Questions with duplicate Positions declared, not merged | `fill/resolve-b1.md` § Key comparison; `compile-b1.md` § 7 declared duplicate Positions |
| Voice verification | 399 ids: MEETS 300, FAILS 77, UNKNOWN 22; 25 ids merged into 18 (same person) → 374 files | `MAP/README.md`; `compile-b1.md` § Voice-verification pass |
| Voice calibration | 118 re-checked; 24 first-pass MEETS→FAILS flips, 21 reverted on a four-kind check, final 2 flips (chescock, skifire13); 5 FAILS stay | `verify/voices-calibration.md` § Totals |
| Claims gapped by Voice | 107 `voice-below-bar`, 58 `voice-unverified`, 0 overlap (substring over `gap`, matches README) | `MAP/claims/*.yaml`; `MAP/README.md` |
| Claim verification | 664 checked (all but the 107 below-bar): 648 CONFIRMED, 8 DATE-WRONG, 8 UNFAITHFUL; 384 rows rechecked by adjudicator, 280 taken from chunk files; random 31/311 clean rows: 0 disagreements; `practiced: unknown` on all 664 | `verify/claims-adjudication.md`; `verify/claims-final.csv` |
| Validator (run 2026-09-28) | 417 FAIL: voices missing `type` 88, missing `track_record` 86, no url 86; claims missing `date` 70 (×2 rules); positions missing `tag` 9; sources missing `date` 6; questions missing `domains` 2 | `check_map.py --map maps/rust`; `compile-b1.md` § Validator run |
| Check records | `MAP/checks/`: 0 files; `arguments/`: 0; `conventions/`: 0 | `check_map.py` counts per kind |

The batch's own gates were not met as written: the audit failed team A on every pass and team B on two of three; no merge check reached 90% on the population reading; the slice gate's "validator 0 FAIL" stands at 417 (`fable-plan.md` line 147). The audit verdicts rest on samples of 5–11 rows where one miss fails a team, and the extraction rules changed twice inside the batch (rule 6 re-worded, rules 8–9 added), so the three passes measure three different bars. The fill checks that validator rules 4–5 need (`fill-position`, `fill-tag`) exist only as recon CSVs; nothing in `MAP/checks/` records them, so no Question can pass rule 4 whatever its evidence. The `gap` field carries four unrelated things (Voice bar, verification notes, date proxies, extractor caveats) because the claim schema has no verification field (`compile-b1.md` § Schema note).

## 3. Evidence minimum, from MAP by script

Rule applied: ≥2 Positions, each with Claims from ≥2 distinct Voices, a Claim not counting if `position: unresolved` or `gap` contains `voice-below-bar` or `voice-unverified`. "None restating the other" (plan § 3) is not script-checkable and is not applied. Countable Claims: 604 of 771.

| stratum | Questions | ≥2 Positions | meets, every Position at bar | meets on ≥2 Positions, another below | 1 Position only | Claims | countable |
|---|---|---|---|---|---|---|---|
| core | 209 | 77 | 2 | 5 | 132 | 460 | 355 |
| wasm | 71 | 28 | 1 | 2 | 43 | 162 | 110 |
| embedded | 70 | 37 | 1 | 3 | 33 | 197 | 149 |
| distributed | 58 | 18 | 2 | 2 | 40 | 124 | 108 |
| web | 56 | 25 | 1 | 2 | 31 | 129 | 96 |
| desktop-cli-ui | 44 | 19 | 0 | 1 | 25 | 112 | 85 |
| ml | 42 | 14 | 1 | 2 | 28 | 100 | 86 |
| decentralized-iroh | 41 | 13 | 1 | 2 | 28 | 101 | 94 |
| cloud-workers | 38 | 8 | 2 | 2 | 30 | 76 | 68 |
| frontend | 25 | 10 | 0 | 1 | 15 | 63 | 53 |
| other | 22 | 12 | 0 | 1 | 10 | 65 | 48 |
| swift-interop | 8 | 3 | 0 | 0 | 5 | 17 | 11 |
| (no domain) | 2 | 0 | 0 | 0 | 2 | 2 | 1 |
| distinct | 401 | 126 | 2 | 5 | 275 | 769 | 604 |

Two Questions meet the minimum on every Position: `depend-vs-hand-roll` (7 domains) and `http-error-status-in-result` (4); the stratum column counts each in every domain it carries. Three more meet it on two Positions with further Positions below bar: `ai-authored-community-contributions`, `replace-battle-tested-c-with-rust`, `serialization-format-choice`. 275 of 401 Questions hold one Position; of 607 Positions, 109 have no countable Voice, 435 have one, 63 have two or more. 14 Questions are one Voice short on one Position. No Question has an Argument (0 files), so none can reach `status: closed` regardless of Claims (validator rule 4).

## 4. Batch 2 targets

Yield by source class, batch 1 (crosswalk joined to `frame/frame.csv` class; minutes are extractor self-reports):

| class | sampled rows (A+B) | unreachable | minutes | canonical Questions | sources yielding | Q per sampled row | Q per logged hour |
|---|---|---|---|---|---|---|---|
| books-courses | 14 | 5 | 462 | 62 | 6 | 4.43 | 8.1 |
| talks | 21 | 0 | 330 | 47 | 16 | 2.24 | 8.5 |
| users-forum | 3 | 0 | 62 | 10 | 3 | 3.33 | 9.7 |
| internals | 9 | 0 | 96 | 11 | 8 | 1.22 | 6.9 |
| hn-lobsters | 21 | 0 | 305 | 26 | 16 | 1.24 | 5.1 |
| twir-links | 24 | 6 | 205 | 26 | 14 | 1.08 | 7.6 |
| individual-blogs;twir-links | 41 | 1 | 550 | 40 | 29 | 0.98 | 4.4 |
| individual-blogs | 14 | 0 | 135 | 13 | 9 | 0.93 | 5.8 |
| project-blog (+twir) | 9 | 0 | 67 | 10 | 8 | 1.11 | 9.0 |
| domain-subframes | 227 | 1 | 3,464 | 195 | 146 | 0.86 | 3.4 |
| rfc | 1 | 0 | 0 | 0 | 0 | 0 | — |

Reads needed per stratum under the plan's own equal-catchability model (§ 4: unseen ≈ (1−p)², λ = −ln(1−p)); p̂A = m/n2, p̂B = m/n1 from `merge-v3/estimate/closure-b1.md`:

| stratum | p̂A | p̂B | λ̂ | reads × current for 10% | for 2% |
|---|---|---|---|---|---|
| core | 0.29 | 0.30 | 0.35 | 3.3 | 5.6 |
| ml | 0.28 | 0.38 | 0.40 | 2.9 | 4.9 |
| desktop-cli-ui | 0.40 | 0.34 | 0.47 | 2.5 | 4.2 |
| embedded | 0.43 | 0.33 | 0.48 | 2.4 | 4.1 |
| wasm | 0.38 | 0.40 | 0.49 | 2.4 | 4.0 |
| web | 0.46 | 0.32 | 0.50 | 2.3 | 3.9 |
| decentralized-iroh | 0.36 | 0.43 | 0.51 | 2.3 | 3.9 |
| distributed | 0.38 | 0.44 | 0.53 | 2.2 | 3.7 |
| cloud-workers | 0.53 | 0.30 | 0.56 | 2.1 | 3.5 |
| frontend | 0.44 | 0.44 | 0.58 | 2.0 | 3.4 |
| swift-interop | 0.50 | 0.33 | 0.55 | 2.1 | 3.6 |

Non-English frame entry (`frame/frame-v2-stats.md`; language × hint by script over `frame-v2-nonen.csv`, window=in):

| language | rows | hint-less | cells with ≥18 rows | classes |
|---|---|---|---|---|
| zh | 2,089 | 1,612 | core 101, ml 108, web 93, distributed 42, desktop-cli-ui 41, embedded 41, decentralized-iroh 32, wasm 28, frontend 19 | forum-threads 917, weekly-newsletter-links 919, qa-topics 149, conference-talks 104; video-channels 0 |
| uk | 107 | 0 | core 95 | github 87, dou 10, youtube 10; telegram 0 |
| de | 40 | 0 | none (core 15 largest) | blogs 26, podcasts 7, talks 4, books 3 |

Targets, in the order the figures rank them. (1) Strata: core, ml, desktop-cli-ui, embedded, wasm — highest read multipliers and, for core, the largest absolute gap (Chapman unseen ≈ 200 Questions). (2) Source classes: books-courses and talks return 8 Questions per logged hour against 3.4 for domain-subframes, which took 227 of 396 sampled rows (57%) and 3,464 of 5,814 logged minutes because `sample.py` draws uniformly within a hint cell and domain-subframes holds 4,871 of 11,083 in-window rows (2,189 of 2,496 desktop-cli-ui hint rows, `frame/frame-stats.md`). The plan draws by (language, hint) cell only (`fable-plan.md` line 102); drawing by (hint, class) cell, or capping domain-subframes per cell, is the change that moves reads toward the classes that yield, and it is a sampling-design change to record before batch 2 draws. What this cannot show: Questions per hour is not unseen-Questions per hour; books cluster many Questions in one source (62 from 6 sources), and a book both teams draw lifts m as one recapture event (f000256 carries 11 of 51 two-team Questions), so the book class raises the estimate's noise as fast as it raises seen. (3) swift-interop: no batch sizing helps while 169 of 262 hint rows are forums.swift.org threads that pass every audit as off-subject; a frame v2 row-class fix for that hint is a Tier 1 change, logged as such, before its cell is drawn again. Under rule 4 it merges into core after three batches if still under 10 seen. (4) other: not a sampling stratum in batch 1 (0 rows); it stays a merger tag until the target strata close (plan § 3). (5) Batch size: at 18 per cell per team, the multipliers say three cumulative batches for most target strata and four for core and ml before 10% is in reach under the plan's model, which Chao1 (f1 = 323 of 399) says is optimistic; a batch 2 of the same size, class-balanced, is the cheapest step that also satisfies rule 2 (two batches). (6) Non-English: only zh can be drawn per hint cell; its 1,612 hint-less rows become core under batch 1's rule (`samples/batch-1.md` line 30), which would put the newsletter-link class into every core draw; uk is 89% core with 87 of 107 rows being GitHub repos (code, which is never a Claim, rule 3); de has 40 rows total. The figures support zh cells at 18 per team where the cell has ≥18, and uk and de as whole-frame draws sized to the frame (uk ≤ 20, de ≤ 20) with language as the reporting dimension the plan makes it (OP2).

Process changes the recorded failures point at. Extraction rules 6, 8, 9 landed mid-batch (`audit-b1-sendback.md` header, `audit-b1-third.md` header): fix `prompts/t2-extract.md` before batch 2 and hold it for the batch, so one audit bar applies. Audit samples of 5–11 rows with one-miss send-back produced two full re-extractions; the auditor's full-population phrase census (A 11/97, B 30/101 forbidden grounds) is a script-sized check — run it over every nothing-new reason as a gate before the audit draws. Prefetch: books-courses front pages fetched as the whole book (f000149, f000217; `audit-b1-third.md` § Notes), 5 of 14 book rows paywalled, 5 talks lost to YouTube 429 (`samples/prefetch-b1.md`) — chapter enumeration for docs sites and a retry window for yt-dlp before the batch draws. Merge: three merges, three checks, none ≥ 90% on the population reading; the grain rule is now written (`merge-v3/merged-questions-b1.md` § The grain rule) — pass it to the batch 2 merger and checker verbatim, gate on the population reading, and feed `--merge-check-agreement` and `--audit-pass` to `estimate.py` so part 3 measures rather than fails by construction. Fill: Claim→Position agreed 98.7% and tags 67.6% — the tag disagreement traces to undefined terms, defined by the resolver after the fact; write the three definitions into the fill prompt. Checks: write `fill-position` and `fill-tag` records into `MAP/checks/` at compile, or validator rule 4 gates nothing. Voices: 25 ids for 18 people came from extractor naming (`voices-calibration.md` § Same-person id pairs) — normalize Voice ids at merge. Team B's third-pass strike rate (13/36) came from high-volume GitHub threads (`strike-b1-third.md` § Notes) — rule 8 now covers it; the batch 2 audit's Claim sample should be sized above 4.

## 5. When fairness grading pays off

Paired cases and ITT grade Position summaries against Arguments and Claims of one Question (`fable-plan.md` lines 143–144). Inputs today: 2 Questions at the evidence minimum, 0 Arguments, 126 Questions with ≥2 Positions, 7 Questions with declared duplicate Positions, 9 untagged Positions, every summary picked by lexical overlap. Question identity moved through five crosswalks in one batch (canonical 276 → 387 → 271 → 401) and the merge check never cleared 90% on the population reading; a graded summary whose Question is re-split or absorbed at the next merge is a wasted grader run.

Trigger condition, from these figures: grade a Question when (a) its canonical id and member set survive the next batch's merge unchanged — measurable from consecutive crosswalks as the fraction of batch-n canonical ids with identical member sets after batch n+1, and worth running once that fraction is ≥ 90% for the stratum, the plan's own merge-agreement floor; (b) it meets the evidence minimum with both fills resolved and Arguments written, since ITT grades summaries against Claims' quotes and paired cases need Arguments; (c) none of its Positions is on the duplicate list. Under (b) alone the set is 2 Questions and both lack Arguments, so plan § 7's "graders on slice 1 in S2" would grade nothing gradable; the figures put grading after the batch that first leaves a stratum's Question set stable, with the check records landing in `MAP/checks/` where the validator reads them.
