# First training protocol — provisional, expires on evidence-map.md

> Basis: 20 claims verified, 14 sources, 14 full texts. Saturation: none. Stage A only.

Inclusion rule: `ledger/claims-status.csv` row says VERIFIED, S≥2, O≥1. Where `claims.csv` and `claims-status.csv` differ, `claims-status.csv` governs. Excluded from this set: 6 UNVERIFIABLE rows (N1-r1-12, N2-r1-09, N3-r1-03, N3-r1-04, N3-r1-10, N7-r1-05); 2 VERIFIED rows at O=0 (N1-r1-10, N2-r1-03). Every claim below cites its `verify/claims/` file; caveats come from that file.

Population key, used throughout: K-12 = school pupils; UG = undergraduates; ADULT-LAB = adults on lab tasks, no professional skill; ADULT-CS = adults acquiring a CS-adjacent skill; SURG = surgical trainees.

Reading rule: O=1 means unaided performance measured in the same session; O=2 means ≥7 days later or a transfer task. 13 of 20 included claims sit at O=1. Only 3 of 20 sit at R=3 (adults, CS-adjacent skill).

## Measure (N1): the unaided delayed probe — instrument, delay, cost per session; proxies to ignore

### What the evidence supports

- Instrument: held-out items, solved with the AI removed. N1-r1-01 (`verify/claims/N1-r1-01.md`): 3 RCTs, AI sidebar removed without warning before 3 held-out test items, learners told to use no AI or outside source; AI-condition solve rate below control in all three (d = −0.42, −0.19, −0.42). Population: US crowdworker adults on fraction and reading items (R=2). Delay: none, same ~13–15 min session (O=1). Not preregistered. No independent replication; two concurrent studies point the same way.
- Assisted performance overstates later unaided skill. N7-r1-09 (`verify/claims/N7-r1-09.md`): before/during/after design, n=124 US adults, ≥UG degree, logic puzzles; AI users' assisted performance overestimated their post-AI unaided performance; non-users' was underestimated by 0.15 reward-rate units. Same session (O=1). Preprint, HCOMP 2026 accepted, 0 citations. Also N3-r1-11 (`verify/claims/N3-r1-11.md`): K-12, practice scores up 48–127%, unaided exam down 17% in the ungated arm, same 90-min session (O=1).
- Delay is part of the instrument, not a free parameter. N1-r1-09 (`verify/claims/N1-r1-09.md`): meta-analysis, 317 experiments, ~85% young adults, lab verbal recall (R=1); the spacing that maximizes retention rises with the retention interval used to test it. "Schedule-independent instrument" wording is the surveyor's inference from the paper's finding, not the paper's phrase. Retention intervals synthesized: seconds to ~8 years (O=2).
- Averaged practice curves mislead on rate. N1-r1-02 (`verify/claims/N1-r1-02.md`): reanalysis of 7,910 individual learning series, 475 adult lab subjects, simple RT tasks (R=1, O=1 by judgment call; claim is about method, not an assisted/unaided contrast); exponential fits beat power fits in every unaveraged set; averaging biases toward the power law. One 2021 boundary finding: individual exponential pattern held for only 13.3% of young adults on a complex motor task.
- Cost per session: no included claim measures it. Only datum: N1-r1-01's whole session, learning phase plus 3 test items, ran ~13–15 minutes.
- Proxies with verified evidence against them: assisted-task success (N1-r1-01, N3-r1-11, N7-r1-09), practice-problem scores (N3-r1-11, N7-r1-01). Self-report, felt learning, confidence, tutor impression: surveyed evidence was S=1/O=0 (N1-r1-03, -04, -08), UNVERIFIABLE (N1-r1-12), or not verified this round (N1-r1-05, -06, -07). No included claim covers them. Treat as unknown, not as cleared.

### Early-measurement probe (PLAN §8 open point 8)

Default stands: unaided delayed probes, capped at 10 minutes per session. What N1's included claims support and do not:

- Supported: unaided, held-out items, AI closed before the probe starts (N1-r1-01); a fixed, recorded delay, since retention depends on it (N1-r1-09); per-item, per-trial logging rather than a fitted average curve (N1-r1-02).
- Not supported by any included claim: the 10-minute figure; any specific delay length. The ≥7-day bar comes from the grading rubric (O=2), not from a measured cost. The cap stays a plan default until N1 sets a figure.

### Checklist for the first sessions

- [ ] Each session ends with a probe: 3 held-out items on material practiced in an earlier session, not this one.
- [ ] Close the LLM session before the probe starts. Record that it was closed. No documented substrate mechanism enforces removal; the probe rests on the learner closing it (`context/substrate-audit.md` lists no lock-out).
- [ ] Record the delay in days between the practice session that covered the item and the probe. Never compare two probes with different delays as if equal.
- [ ] First probe on any item: ≥7 days after its practice. Earlier probes count as O=1 and are labeled so.
- [ ] Log per item: solved / skipped / wrong, time, delay, date. Keep raw rows. Do not fit or average a curve across sessions.
- [ ] Never log assisted-practice success or practice-problem scores as evidence the skill is learned.
- [ ] Never log confidence or "felt it click" as evidence either way; record it, if at all, in a separate column marked unverified.
- [ ] Probe cost: stop at 10 minutes; record actual minutes so N1 can set a figure.

## Practice unit and order (N2)

### What the evidence supports

- Subgoal-labeled worked examples, then problem solving. N2-r1-05 (`verify/claims/N2-r1-05.md`): n=40 UG novices learning a block-based app-building tool, random assignment, two 1-hour sessions one week apart; subgoal group completed 36% more problem-solving tasks correctly across two immediate and one 1-week-delayed assessment (F(1,38)=11.16, p=.002). R=3, O=2. Single small experiment, no replication found. N2-r1-06 (`verify/claims/N2-r1-06.md`): same experiment; component transfer f=.58 (p=.001), procedural transfer f=.37 (p=.025) on tasks needing components not shown in instruction. Caveat from `needs/n2-r1.md`: the same idea scaled to a semester course (N2-r1-07, not verified this round) held on quizzes, not on exams.
- Attempt before instruction. N2-r1-10 (`verify/claims/N2-r1-10.md`) and N3-r1-02 (`verify/claims/N3-r1-02.md`), one meta-analysis: 53 studies, 166 comparisons; problem-solving-then-instruction beats instruction-then-problem-solving, g=0.36 [0.20, 0.51]; transfer alone g=0.40; procedural knowledge unharmed (g=−0.03); high-fidelity productive-failure designs g=0.37–0.58. Reverses for grades 2–5 (−0.09) and for domain-general skills (−0.17). Population mixed: 15% grades 2–5, 45% grades 6–10, 37% UG, 3% postgraduate/professional (R=2). "12,000+ participants" not found in the primary text by the N2-r1-10 verifier; treat that number as unconfirmed. Delay-to-test not coded. Standing dispute with the cognitive-load line (worked examples first) is reported in `needs/n2-r1.md` and `needs/n3-r1.md`, not adjudicated.
- Interleave problem types. N2-r1-02 (`verify/claims/N2-r1-02.md`): preregistered cluster RCT, 787 7th-graders, 15 teachers; interleaved beat blocked 61% vs 38%, d=0.83 [0.68, 0.97], on an unannounced test one month later; positive for all 15 teachers. K-12 (R=1), O=2. No independent replication yet.
- Space practice to the retention target. N2-r1-01 (`verify/claims/N2-r1-01.md`): same meta-analysis as N1-r1-09; optimal inter-study interval rises with retention interval — under 1 minute for sub-minute retention, ≥1 month for ≥6-month retention. Lab verbal recall (R=1), O=2. A 2008 companion study and a 2025 conceptual replication of it exist under different DOIs; noted, not conflated.
- Whole-task vs part-task order: N2-r1-09 UNVERIFIABLE. No included claim. Practitioner "kata before project" belief (`needs/breadth-r1.md`): five sources, zero outcome data.

### Checklist for the first sessions

- [ ] Unit: one worked example whose steps are grouped and named by the subgoal each group achieves, then problem-solving tasks that reuse those subgoals, then tasks needing a component the example did not show.
- [ ] Order within a new topic: attempt first, instruction second. Skip this order for domain-general skills (the meta-analysis reverses there).
- [ ] Order across topics: once two or more problem types exist, mix them; no two consecutive problems of the same type.
- [ ] Return to a topic at a gap sized to the retention wanted; for multi-month retention, revisit at month-scale gaps, not day-scale. Log the gap.
- [ ] Log which unit form each session used, so a probe failure can later be tied to a unit form.
- [ ] Do not claim whole-task or part-task ordering as evidence-backed; neither is verified.

## Session shape (N3): intervene when / with what / feedback content and timing

### What the evidence supports

- When to intervene: after an attempt, not before. Same meta-analysis as above (N3-r1-02, `verify/claims/N3-r1-02.md`; N2-r1-10). Caveats as listed under N2.
- What to hand over: hints, not answers. N7-r1-02 (`verify/claims/N7-r1-02.md`): same K-12 cluster RCT as N3-r1-11; the arm prompted to give teacher-designed hints instead of answers scored −0.004 (n.s., ≈−0.01 SD) on the unaided exam versus −0.054 (p<.05, ≈−0.19 SD) for the ungated arm (N7-r1-01, `verify/claims/N7-r1-01.md`). Turkish high school (R=1), same 90-minute session (O=1). "839 students" is arithmetic inference, not a quoted count. One correction on record: affiliation only.
- Assisted gains do not carry to unaided performance. N3-r1-11 (`verify/claims/N3-r1-11.md`): as above; O re-graded 2→1 because the exam followed practice in the same session.
- When the learner bypasses material, target exactly what was bypassed. N3-r1-07 (`verify/claims/N3-r1-07.md`): middle-school (R=1), quasi-experiment, control always first, half the planned design dropped; gaming 33% → 18%, p=0.07, marginal; students receiving the most supplemental exercises gained 46 vs 20 points (p=0.04). S re-graded 3→2. The paper's own decomposition: negative-affect messages alone had no effect; more exercises correlated with more, not less, gaming. Weak evidence; the one actionable part is "exercises on the bypassed material".
- Human tutor with an LLM copilot. N3-r1-12 / N7-r1-04 (`verify/claims/N3-r1-12.md`, `verify/claims/N7-r1-04.md`): preregistered RCT, 900 tutors, 1,800 K-12 pupils; +4 p.p. topic mastery (p<.01), +9 p.p. for lower-rated tutors. Exit ticket at session end (O=1). Preprint. Applies where a human tutor is in the loop; gym has none.
- Feedback content and timing: no included claim. N3-r1-04 (immediate vs delayed, meta-analysis, 1988) UNVERIFIABLE, paywalled. N3-r1-03 (contingent support) UNVERIFIABLE. N3-r1-10 (help-seeking feedback) UNVERIFIABLE. N3-r1-05 S=1/O=0. Timing has no verified value in this protocol.

### Checklist for the first sessions

- [ ] Task first. Instruction after the attempt, whatever the attempt produced.
- [ ] During practice: hints, never the solution. Log every direct answer given as a protocol breach.
- [ ] Log every hint: what was asked, what was given, at what point in the attempt.
- [ ] If the learner skips or fast-forwards a step, next unit targets that step; log the skip.
- [ ] Feedback timing: pick one (immediate or end-of-attempt), keep it fixed across the first sessions, and record it, so a later round can compare. No evidence backs either choice.
- [ ] Do not count "mastered in session" as mastered. Only the delayed probe counts.

## What holds on an LLM substrate (N7): holds / fails / untested — one table

Substrate facts from `context/substrate-audit.md`: file-change hooks and Monitor watching (Monitor 30 min max); scheduled runs at ≥1-hour intervals; persistent per-project memory files; 200k-token context; no documented lock-out of the LLM for a probe.

| Practice | Verdict | Evidence | Population, delay, caveats |
|---|---|---|---|
| Unaided probe with the AI removed | holds | N1-r1-01 (`verify/claims/N1-r1-01.md`) | ADULT crowdworkers, R=2, O=1; not preregistered |
| Hints in place of answers during practice | holds, K-12, same session | N7-r1-02 (`verify/claims/N7-r1-02.md`) | K-12, R=1, O=1; preregistered; ≈−0.01 SD n.s. |
| Ungated answers during practice | fails | N7-r1-01 (`verify/claims/N7-r1-01.md`); N3-r1-11; N1-r1-01 | K-12 and ADULT-LAB, O=1; ≈−0.19 SD, d −0.19 to −0.42 |
| Full delegation of the task to the AI while learning | fails for learning | N7-r1-08 (`verify/claims/N7-r1-08.md`) | ADULT-CS, n=52, R=3, O=1; impaired concepts, code reading, debugging; no significant average speed gain; delegators (~20% of treatment) faster (19.5 vs 23 min) |
| Interaction patterns with cognitive engagement, low AI reliance | holds for learning, same study | N7-r1-08 | 3 of 6 patterns scored 65–86% vs 24–39%; descriptive typology, not randomized per pattern |
| On-demand AI in a reasoning task, then AI removed | fails | N7-r1-09 (`verify/claims/N7-r1-09.md`) | ADULT-LAB, n=124, O=1; lower request cost → more use; preprint, 0 citations |
| AI access while learning an unfamiliar topic, tested unaided a week later | holds, disputed | N7-r1-07 (`verify/claims/N7-r1-07.md`) | 211 UG, R=2, O=2 (mean 6.99 days); +0.27 SD immediate, +5.1 p.p. at one week (p=.027); preprint only, no peer review |
| Structured AI tutor vs in-class active learning | holds, immediate only | N7-r1-03 (`verify/claims/N7-r1-03.md`) | 194 UG physics, crossover, O=1; effect 0.63–1.3 SD, flagged >1.0 SD; authors name retention as unstudied |
| AI tutor vs expert human instructor, surgical skills | roughly equal, small low-certainty edge, higher extraneous load | N7-r1-06 (`verify/claims/N7-r1-06.md`) | SURG, R=2, O=1; OSATS MD 0.20 [0.01, 0.39], pooled n=159 of 268, 79.9% weight on one high-risk-of-bias study; authors recommend hybrid |
| LLM copilot to a human tutor | holds, not applicable without a human tutor | N7-r1-04 (`verify/claims/N7-r1-04.md`) | K-12, R=1, O=1; preprint |
| Continuous watching of the learner's files | untested | none | substrate supports it; no included claim measures its effect on learning |
| Endless tailored practice generation | untested | none | no included claim |
| Retention past 7 days under any LLM practice regime | untested except N7-r1-07 | N7-r1-07 only | one preprint, UG, favorable direction |
| Adults, CS-adjacent, delayed unaided outcome | untested | none | zero claims at R=3 and O=2 among N7 |

Dispute carried, not resolved (`needs/n7-r1.md`): N7-r1-07 (gains persist) vs N7-r1-08/-09 (unaided skill worse after help withdrawn). The surveyors' candidate explanation: delegation (AI does the task) vs tutoring (AI helps the learner do it). No verified claim tests that split directly; N7-r1-08's typology is consistent with it.

### Checklist for the first sessions

- [ ] The LLM does not write the learner's solution. Any generated solution is logged as a breach.
- [ ] Every AI turn during practice is a hint or a question, per the N3 checklist.
- [ ] Log interaction pattern per task: who wrote the code, how many AI turns, whether the learner read AI output before running it.
- [ ] Log time to completion per task alongside the probe result, so speed and learning are never read off one number.
- [ ] Treat the one-week persistence result as a hypothesis to test with the probe, not as a license for freer AI use.

## Claims table: claim_id | claim | S R O | population | axes | verify file

| claim_id | claim | S R O | population | axes | verify file |
|---|---|---|---|---|---|
| N1-r1-01 | Unaided test after AI removal shows AI-assisted learners below control, 3 RCTs, d −0.19 to −0.42 | 3 2 1 | US crowdworker adults; same session; not preregistered | skill per hour | `verify/claims/N1-r1-01.md` |
| N1-r1-02 | Averaged power-law practice curves are an averaging artifact; individual curves exponential | 3 1 1 | adult lab subjects, simple RT tasks; boundary finding for complex motor tasks | skill per hour | `verify/claims/N1-r1-02.md` |
| N1-r1-09 | Retention-maximizing spacing depends on the delay used to test it | 4 1 2 | ~85% young adults, lab verbal recall; "instrument" wording is inference | durability | `verify/claims/N1-r1-09.md` |
| N2-r1-01 | Optimal inter-study interval rises with retention interval | 4 1 2 | same source as N1-r1-09 | durability | `verify/claims/N2-r1-01.md` |
| N2-r1-02 | Interleaved beat blocked practice 61% vs 38%, d=0.83, one month later | 3 1 2 | 787 7th-graders; preregistered cluster RCT | skill per hour; durability | `verify/claims/N2-r1-02.md` |
| N2-r1-05 | Subgoal-labeled worked examples: 36% more problem-solving tasks correct across immediate and 1-week tests | 3 3 2 | n=40 UG novices, app-building tool; no replication | skill per hour; transfer | `verify/claims/N2-r1-05.md` |
| N2-r1-06 | Same group higher on component (f=.58) and procedural (f=.37) transfer | 3 3 2 | same experiment | transfer | `verify/claims/N2-r1-06.md` |
| N2-r1-10 | Problem-solving before instruction g=0.36; reverses for grades 2–5 and domain-general skills | 4 2 1 | mixed grade 2 to professional; "12,000+" unconfirmed; delay not coded | skill per hour; transfer | `verify/claims/N2-r1-10.md` |
| N3-r1-02 | Same meta-analysis; transfer g=0.40; procedural unharmed g=−0.03 | 4 2 2 | as N2-r1-10 | skill per hour; transfer | `verify/claims/N3-r1-02.md` |
| N3-r1-07 | Supplemental exercises on bypassed material; high-exercise group gained 46 vs 20 points | 2 1 1 | middle school; quasi-experiment, order not randomized; gaming reduction p=0.07 | skill per hour | `verify/claims/N3-r1-07.md` |
| N3-r1-11 | Ungated GPT-4 raised practice scores, lowered unaided exam 17% | 3 1 1 | Turkish high school; same 90-min session; O re-graded 2→1 | durability | `verify/claims/N3-r1-11.md` |
| N3-r1-12 | LLM copilot for human tutors: +4 p.p. mastery, +9 p.p. for lower-rated tutors | 3 1 1 | 900 tutors, 1,800 K-12; exit ticket; preprint | skill per hour | `verify/claims/N3-r1-12.md` |
| N7-r1-01 | Ungated arm ≈ −0.19 SD on unaided exam | 3 1 1 | same trial as N3-r1-11; 839 inferred | skill per hour; transfer | `verify/claims/N7-r1-01.md` |
| N7-r1-02 | Hint-only arm ≈ −0.01 SD, n.s.; harm eliminated | 3 1 1 | same trial | skill per hour; transfer; durability | `verify/claims/N7-r1-02.md` |
| N7-r1-03 | Structured AI tutor beat in-class active learning, immediate | 3 2 1 | 194 UG physics; crossover; effect flagged >1.0 SD | skill per hour | `verify/claims/N7-r1-03.md` |
| N7-r1-04 | Same as N3-r1-12, re-verified | 3 1 1 | as N3-r1-12 | skill per hour | `verify/claims/N7-r1-04.md` |
| N7-r1-06 | AI vs expert surgical tutoring: OSATS MD 0.20, low certainty, higher extraneous load, hybrid recommended | 4 2 1 | surgical trainees; OSATS n=159 of 268; one high-RoB study 79.9% weight | skill per hour; transfer | `verify/claims/N7-r1-06.md` |
| N7-r1-07 | AI access +0.27 SD immediate; +5.1 p.p. unaided at one week | 3 2 2 | 211 UG; mean 6.99 days; preprint only | skill per hour; durability | `verify/claims/N7-r1-07.md` |
| N7-r1-08 | Full delegation impaired concepts, code reading, debugging; no significant speed gain; 3 of 6 patterns preserved learning | 3 3 1 | n=52 crowd workers with prior experience; immediate quiz | skill per hour; durability | `verify/claims/N7-r1-08.md` |
| N7-r1-09 | AI users worse after removal; assisted performance overestimates unaided | 3 2 1 | 124 US adults, logic puzzles; same session; preprint | durability; transfer | `verify/claims/N7-r1-09.md` |

Axis coverage: skill per hour 16 claims; durability 7; transfer 7; sustainability 0. The sustainability axis has no included claim.

## Not covered yet (N4, N5, N6) and what that means for the first sessions

- N4, diagnosis: no round run. No verified way to tell why a probe failed (missing concept, missing procedure, misread task). First sessions: log the failed item and the learner's attempt verbatim; do not classify the cause; do not adapt the next unit on a diagnosis nobody verified.
- N5, elite margin: no round run. Nothing verified separates an elite coach from an adequate one. First sessions carry no claim of being better than a textbook plus the probe. N7-r1-06's surgical result (AI ≈ expert, low certainty) is the only verified human-vs-AI comparison, and it is not CS.
- N6, sustain: no round run. Sustainability axis: zero included claims (N1-r1-12 UNVERIFIABLE; N2-r1-03 O=0). Ruling 115: irregular bursts are the current reality. First sessions: log date, duration, gap since last session as raw rows; attach no verified expectation to any cadence. Spacing evidence (N2-r1-01) says a gap of weeks is compatible with month-scale retention targets; it says nothing about whether the learner returns.
- Attention sub-question (ruling 120, hyperfocus and breadth): no verified claim. Nothing in this protocol adapts to it.

## Threats (from §9 of the plan, those live now)

| threat | how it shows in this protocol | residual |
|---|---|---|
| Proxy outcomes | 13 of 20 claims O=1; durability evidence for LLM practice is one preprint (N7-r1-07) | the probe checklist exists because the literature mostly does not measure what ruling 104 counts |
| Population mismatch | 10 claims R=1 (K-12 or lab), 7 R=2, 3 R=3; the hint-not-answer result is K-12 only | every checklist item drawn from K-12 or lab evidence is an untested transfer to an adult self-directed learner |
| Publication bias, one-study headlines | N1-r1-01, N7-r1-03, -07, -08, -09, N3-r1-11 family, N3-r1-12 family, N7-r1-06: 2025–26, no replications found; four are preprints; N7-r1-03 flagged >1.0 SD | direction of the AI-access effect is disputed within this set |
| Rate limits / blocks | OpenAlex citing-works search failed on every verification; replication checks rest on Semantic Scholar and Crossref | a critique indexed only in OpenAlex would be missed |
| Abstract-level reading | 6 claims dropped as UNVERIFIABLE, including both feedback-timing sources; all 20 included claims are full-text reads | feedback timing enters with no evidence at all |
| Grading drift | re-grades applied: N1-r1-09 R 2→1, N3-r1-07 S 3→2, N3-r1-11 O 2→1, N1-r1-10 R 3→2 | bands remain judgment; triple shown per claim |
| Measuring what is easy | skill per hour 16 claims; sustainability 0 | first sessions have no sustainability guidance |
| Time pressure makes Stage A final | this file expires on evidence-map.md; 20 claims, one round, no saturation | if Stage B never runs, K-12 and same-session evidence stays the basis |
| Synthesis writes a design | checklists state actions the owner checks; forbidden strings absent | reviewer grep still required |
| Subject priming | tool and library names in sources replaced by neutral descriptions | none known in this file |
| Seed anchoring | not checked here; seed withheld from this synthesis | unknown |

---

Notification summary: 20 VERIFIED claims at S≥2, O≥1 from 14 full-text sources feed this protocol; 6 UNVERIFIABLE and 2 O=0 rows are excluded and named. The first sessions end in a 3-item unaided probe with the LLM closed and a recorded ≥7-day delay, practice subgoal-labeled worked examples then interleaved problems with attempt-before-instruction, and permit hints but never solutions during practice, logging every breach. Biggest open risk: 13 of 20 claims measure same-session performance and 10 come from K-12 or lab populations, while the one ≥7-day study of LLM-assisted learning (undergraduates, preprint) points the opposite way from the four same-session harm studies, so whether AI access during practice helps or hurts this learner's retention is unknown until the probes say.
