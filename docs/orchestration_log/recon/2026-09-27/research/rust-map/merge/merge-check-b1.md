# Merge check — batch 1 (t4-merge-check-b1)

## 1. Population and sample

- Population: every `- Q:` entry in `team-a/extract-b1-*.md` and `team-b/extract-b1-*.md`, sR* send-back files excluded (lead instruction). 337 entries parsed (team A 185, team B 152); 10 team-A entries in sa14 (f005360 ×4, f005454 ×3) and sa15 (f005516 ×3) dropped as superseded by the saL1 re-extraction of those rows (t4-merge.md step 1). saL2 rows kept: they continue a cut read, not re-extract it. Population: 327 (team A 175, team B 152).
- Team-local id used here: `<team>:<slice>:<frame_id>:<ordinal of the Q within that frame section>`. Extract files carry no ids of their own.
- Sample: `random.Random(20260927).sample(sorted(ids), ceil(0.2*327)=66)`, drawn with `uv run python -c`. Seed 20260927.

## 2. Blind merge of the sample

Groupings fixed 2026-09-27T19:24 (scratchpad blind.json), before any file under RECON/merge/ was read. Rule applied: two Questions are one when their Positions choose between the same alternatives at the same level of generality, so a Claim on one pins to the other without distortion; project context alone does not split them; shared keywords alone do not join them. Each sampled Question was searched against the full 327-entry population.

| sampled id | blind group | members (full population) |
| --- | --- | --- |
| a:02:f000957:1 | G-defer-until-need | a:02:f000957:1, b:sb03:f000569:1, a:sa11:f004512:3 |
| a:02:f000993:2 | singleton | a:02:f000993:2 |
| a:sa03:f002243:1 | singleton | a:sa03:f002243:1 |
| a:sa03:f002356:1 | singleton | a:sa03:f002356:1 |
| a:sa04:f002554:1 | singleton | a:sa04:f002554:1 |
| a:sa04:f002665:1 | singleton | a:sa04:f002665:1 |
| a:sa04:f002865:1 | G-depend-vs-own | a:sa14:f005079:2, a:sa04:f002865:1, a:02:f001053:1 |
| a:sa05:f003025:2 | G-reuse-norms | a:sa05:f003025:2, a:sa13:f004772:4 |
| a:sa05:f003074:2 | singleton | a:sa05:f003074:2 |
| a:sa06:f003414:2 | G-shared-mut-vs-explicit | a:sa06:f003414:2, b:sb04:f001022:1 |
| a:sa07:f003704:1 | singleton | a:sa07:f003704:1 |
| a:sa07:f003704:2 | singleton | a:sa07:f003704:2 |
| a:sa07:f003716:1 | singleton | a:sa07:f003716:1 |
| a:sa09:f004016:2 | singleton | a:sa09:f004016:2 |
| a:sa11:f004512:4 | singleton | a:sa11:f004512:4 |
| a:sa12:f004637:1 | singleton | a:sa12:f004637:1 |
| a:sa13:f004772:3 | singleton | a:sa13:f004772:3 |
| a:sa13:f004772:4 | G-reuse-norms | a:sa05:f003025:2, a:sa13:f004772:4 |
| a:sa14:f004985:3 | G-fail-loud-vs-default | a:sa14:f004985:3, a:sa14:f005079:5, b:sb03:f000669:1 |
| a:sa14:f005079:1 | singleton | a:sa14:f005079:1 |
| a:sa14:f005079:2 | G-depend-vs-own | a:sa14:f005079:2, a:sa04:f002865:1, a:02:f001053:1 |
| a:sa14:f005079:3 | singleton | a:sa14:f005079:3 |
| a:sa14:f005079:5 | G-fail-loud-vs-default | a:sa14:f004985:3, a:sa14:f005079:5, b:sb03:f000669:1 |
| a:sa14:f005149:2 | singleton | a:sa14:f005149:2 |
| a:sa16:f007175:1 | singleton | a:sa16:f007175:1 |
| a:sa18:f008694:1 | singleton | a:sa18:f008694:1 |
| a:sa18:f008787:1 | singleton | a:sa18:f008787:1 |
| a:sa19:f009196:1 | singleton | a:sa19:f009196:1 |
| a:sa19:f009196:2 | singleton | a:sa19:f009196:2 |
| a:sa19:f009343:1 | singleton | a:sa19:f009343:1 |
| a:sa21:f011069:1 | singleton | a:sa21:f011069:1 |
| a:sa25:f011413:2 | singleton | a:sa25:f011413:2 |
| a:sa26:f011305:5 | G-hotpatch-bypass | a:sa26:f011305:5, b:sb09:f002719:1 |
| a:sa26:f011443:1 | singleton | a:sa26:f011443:1 |
| a:sa28:f012469:1 | G-microbench-trust | a:sa28:f012469:1, a:sa25:f011413:5 |
| a:sa28:f012469:6 | singleton | a:sa28:f012469:6 |
| a:sa30:f013276:2 | singleton | a:sa30:f013276:2 |
| a:sa30:f013276:4 | singleton | a:sa30:f013276:4 |
| a:saL1:f005360:1 | singleton | a:saL1:f005360:1 |
| a:saL1:f005360:3 | singleton | a:saL1:f005360:3 |
| b:sb04:f001022:1 | G-shared-mut-vs-explicit | a:sa06:f003414:2, b:sb04:f001022:1 |
| b:sb05:f001512:2 | G-typestate-vs-runtime | b:sb05:f001512:2, b:sb03:f000715:1, b:sb24:f011295:2 |
| b:sb09:f003036:1 | singleton | b:sb09:f003036:1 |
| b:sb13:f003963:2 | singleton | b:sb13:f003963:2 |
| b:sb13:f004160:1 | singleton | b:sb13:f004160:1 |
| b:sb17:f005113:1 | singleton | b:sb17:f005113:1 |
| b:sb17:f005159:2 | singleton | b:sb17:f005159:2 |
| b:sb18:f005307:2 | singleton | b:sb18:f005307:2 |
| b:sb18:f005600:1 | G-mutex-vs-lockfree | b:sb18:f005600:1, a:sa17:f007846:1 |
| b:sb19:f005948:1 | G-rust-failure-handling-worth | b:sb19:f005948:1, a:sa15:f005948:1 |
| b:sb19:f007207:1 | singleton | b:sb19:f007207:1 |
| b:sb19:f007207:2 | singleton | b:sb19:f007207:2 |
| b:sb20:f007290:3 | singleton | b:sb20:f007290:3 |
| b:sb20:f007797:1 | singleton | b:sb20:f007797:1 |
| b:sb21:f008390:2 | singleton | b:sb21:f008390:2 |
| b:sb21:f008808:1 | singleton | b:sb21:f008808:1 |
| b:sb23:f009657:1 | singleton | b:sb23:f009657:1 |
| b:sb24:f011295:3 | singleton | b:sb24:f011295:3 |
| b:sb24:f011312:4 | G-port-yields-safety | b:sb24:f011312:4, a:sa21:f011069:2 |
| b:sb24:f011413:1 | G-derive-vs-reflection | b:sb24:f011413:1, b:sb24:f011413:3, a:sa25:f011413:1, a:sa25:f011413:3 |
| b:sb24:f011413:4 | G-reflection-model | b:sb24:f011413:4, a:sa25:f011413:4 |
| b:sb25:f011435:1 | singleton | b:sb25:f011435:1 |
| b:sb25:f012561:1 | singleton | b:sb25:f012561:1 |
| b:sb26:f012849:1 | G-rust-unambiguous-vs-tradeoff | b:sb26:f012849:1, b:sb19:f005743:1 |
| b:sb26:f013214:1 | singleton | b:sb26:f013214:1 |
| b:sb26:f013214:4 | singleton | b:sb26:f013214:4 |

## 3. Comparison with t4-merge

Crosswalk read after section 2 was fixed: `merge/crosswalk-b1.csv` (541 rows, 276 canonical ids) and the rules and doubt notes in `merge/merged-questions-b1.md`.

- Population match: the crosswalk's team-local ids (`<team>-<slice>-<frame>-q<k>`) equal this check's 327 ids one to one. No id missing either side; each maps to exactly one canonical id. The merger applied the same supersession (saL1 over sa14/sa15) and the same sR exclusion.
- Agreement measure: a sampled Question agrees when the set of population members sharing its canonical id is identical in both merges. One member more or fewer anywhere fails the item.
- **Result: 58 of 66 agree = 87.9%** (Wilson 95% interval 77.9%–93.7%). Below the 90% gate.
- Member links from sampled Questions (self excluded): both merges 18, this check only 8, t4-merge only 4.

## 4. Disagreements

Eight sampled items, six grouping decisions. Merger's reason quoted or paraphrased from `merged-questions-b1.md`; "after reading" is this checker's view once the merger's reasons were seen. It does not change the blind rate.

| # | sampled item(s) | this check (blind) | t4-merge | reason for the split | after reading |
| --- | --- | --- | --- | --- | --- |
| 1 | a:02:f000957:1 | one Question with b:sb03:f000569:1 and a:sa11:f004512:3 ("design for an anticipated need now, or defer until use proves it") | three singletons: `async-hook-cancellation-upfront`, `defer-multithreaded-encoding`, `ergonomic-sugar-now-or-later` | merger listed them under "ship-now-or-wait instances that share a shape but not the thing decided"; its test: could a practitioner hold opposite Positions on the two — yes (cancellation semantics break callers if added late; sugar does not) | merger holds; checker grouped by shape |
| 2 | a:sa04:f002865:1, a:sa14:f005079:2 | `depend-vs-own` with a:02:f001053:1 | same plus a:saL2:f011092:3 (official vendor SDK vs lean internal wrapper) | checker missed f011092:3 in the population scan; under the checker's own rule it belongs | merger holds; checker's miss |
| 3 | a:sa14:f004985:3, a:sa14:f005079:5 | one Question with b:sb03:f000669:1 ("fail loudly vs degrade to a default") | `service-fault-isolation-degrade` (f004985:3 alone) apart from `silent-fallback-vs-explicit-error` (f005079:5 + b:sb03:f000669:1) | merger: "never crashing on hostile input is a different decision from guessing on bad input" | merger holds; one can hold "fault-isolate the service" and "error on ambiguous input" at once |
| 4 | b:sb20:f007797:1 | singleton (uniform substrate vs Lambda-dev/containers-prod mismatch) | `lambda-vs-containers` with a:sa17:f007797:1, a:sa24:f011220:1; b's framing becomes Position `--split-by-workload` | checker read b's question as env-parity, a separate decision; merger read the split as one answer to where a Rust service runs | merger defensible; the only item where the checker split and the merger joined |
| 5 | b:sb24:f011413:1 | one Question with b:sb24:f011413:3, a:sa25:f011413:1, a:sa25:f011413:3 (derive codegen vs reflection) | two cross-team pairs: `proc-macro-derives-vs-reflection-shape` (q1s), `runtime-reflection-vs-codegen-tradeoff` (q3s) | merger flagged this itself (doubt note 12): "You could also argue a-q1, a-q3, b-q1 and b-q3 are one decision"; "proc macros are costly" and "reflection does not clearly win" can be held together, which favours two | open judgment split; the merger's split passes its own test |
| 6 | b:sb26:f012849:1 | one Question with b:sb19:f005743:1 (Rust over C/C++: unambiguous good vs tradeoff) | `rust-broad-quality-improvement-over-c` apart from `memory-safe-language-moral-imperative` | merger: "the first asks whether the choice is ethical or economic, the second whether the technical merit is broad or narrow" | merger holds; "not a moral duty" and "broadly better" are compatible |

Direction: 5 of 6 decisions are the checker lumping where the merger split (1, 3, 5, 6) or missing a member (2); 1 is the checker splitting where the merger joined (4). The disagreement is mostly calibration of the sameness test, not crosswalk error: the checker's blind test ("a Claim on one pins to the other without distortion") admits shared-shape lumps that the merger's test ("could a practitioner hold opposite Positions on the two") correctly refuses.

Effect on shared-count m in the sampled groups, had the checker's merge stood: +1 (item 1 becomes cross-team), −1 (item 4 leaves b alone), −1 (item 5, two cross-team canonicals become one); items 2, 3, 6 leave m unchanged. Net −1.

## 5. Threats to validity

- One checker, one sample of 66; the 95% interval (77.9%–93.7%) straddles 90%. The gate reads the point estimate.
- The checker's sameness rule was written before reading the merger's; the two rules differ in wording, and 4 of 6 disagreements trace to that difference. A checker bound to the merger's exact test would likely have agreed more; that is not measured here and cannot be, since the rule was seen.
- Agreement is judged per full group, so a single missed member (item 2) fails two sampled items.
- "After reading" judgments were formed after seeing the merger's reasons and are not blind. They are reported for adjudication, not counted.
- Only Question grouping was checked; Position merges and Claim placement were not.

## 6. Verdict

Blind agreement 87.9% (58/66) < 90%: FAIL for PLAN § 4 rule 3. Per PLAN line 131, <90% triggers a full second merge and adjudication. Input for adjudication: in 5 of the 6 disputed decisions the merger's grouping holds under its stated test on this checker's reading; decision 5 (f011413 reflection split) is an open judgment call the merger already flagged.
