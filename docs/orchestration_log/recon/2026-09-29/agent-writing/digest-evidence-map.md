# Digest — evidence map v3 (teaching toward lasting unaided skill)

Source: `docs/orchestration_log/recon/2026-09-27/research/teaching/synthesis/evidence-map-v3.md`, 1,123 lines, read in full; grades S R O. Ledger (last row per id) matches the map on every cited id: 135 VERIFIED, 89 UNVERIFIABLE, 6 REFUTED; 103 at O≥1; 13 at R=3.

Key (line 9):
S = source strength 1–4. R = relevance; 3 = adults on a CS-adjacent skill. O: 2 = unaided at ≥7 days or a transfer task (so not necessarily delayed); 1 = unaided, immediate; 0 = assisted, self-report, time.

## 1. Structure

1–9 basis, status rule, key · 11–13 Answer · 15–62 changes from v2 · 64–690 per need (tables, disputes, gaps): N1 68, N2 161, N3 249, N4 343, N5 428, N6 514, N7 595 · 692–742 disagreements D1–D41 · 744–753 refuted · 755–806 Pareto set · 808–865 LLM transfer · 867–873 owner calibration · 875–889 coverage gaps · 891–1062 confidence (saturation, round-8 capture) · 1064–1072 not verified · 1074–1123 first-protocol changes.

Status: final on sources (the owner closed collection 2026-09-27), open on reading. Only claims VERIFIED at O≥1 enter the Pareto set.

## 2. Pareto set

Rule (line 800): a verified non-negative O=2 cell or ≥2 non-negative cells; that O=2 result uncontradicted, interval not crossing zero; undominated. No method dominates across the four axes (skill per hour, durability, transfer, sustainability); no member has a sustainability cell.

- **Spacing to target.** Revisit gap sized to the retention wanted.
  - Skill: N2-r7-04 (4 1 2), gain at equal total study time.
  - Durability: N2-r1-01 (4 1 2), re-found N2-r7-03.
  - Conditions: lab verbal recall, young adults, intervals up to ~8 years.
- **Interleaving.** Mix problem types.
  - Skill and durability: N2-r1-02 (3 1 2), d=0.83 at 1 month, re-found N2-r7-01.
  - Transfer: N2-r5-01 (4 2 2), SMD 0.55. Durability: N2-r5-05 (4 2 1).
  - Conditions: field evidence is one K-12 RCT; motor effects n.s. in applied settings (N2-r5-03: 0.11 after outliers; N2-r5-06: −0.01).
- **Subgoal-labeled worked examples, novices.**
  - N2-r1-05 (3 3 2), +36% tasks correct.
  - N2-r1-06 (3 3 2), component and procedural transfer.
  - Conditions: n=40 UG, one lab; 1-week test pooled with immediate ones; no attempt-first arm.
- **Attempt before instruction, instruction building on the attempts.**
  - N3-r1-02 (4 2 2): transfer g=0.40, procedural g=−0.03.
  - N2-r1-10 (4 2 1): g=0.36 overall.
  - Conditions: grade 6+, domain-specific; reverses for grades 2–5 and domain-general skills; fidelity 0.56 vs 0.20; experimental g 0.25; adults undetermined; delay not coded.
- **Problem-based practice.**
  - Durability: N2-r3-01 (4 2 2), 12 weeks to 2 years.
  - Negative on immediate exams: N2-r3-02 (4 2 1).
  - Conditions: medical education, 1970–2000.
- **Socratic guidance from an LLM tutor**, against prompt refinement.
  - N7-r3-04c (3 3 2): weeks later, 13/29 vs 4/23 students prompted for understanding.
  - Conditions: graduate robotics, 52 traced; outcome measured with LLM access (transfer of LLM use, not unaided skill).
- **Gaze training (new).** Train the learner in the expert performer's measured gaze.
  - N5-r6-02 (3 2 1): 55% vs 32–39% faster.
  - N5-r6-03 (3 2 1).
  - N5-r6-06 (3 2 2): 1.9 fewer putts over 10 competitive rounds.
  - N5-r6-09/10 (3 2 1): held under dual task and anxiety.
  - Conditions: three RCTs, n=20–30, golfers and medical/surgical novices, up to 3 months.
- **Simulation-based mastery learning over video (new).**
  - Negative immediately: N1-r6-05 (3 2 1).
  - Ahead at 2 weeks: N1-r6-06 (3 2 2), retention index 114% vs 91%.
  - Conditions: one RCT, 30 medical students.
- **Tutor built from 10 expert tutors' dialogue moves (new, non-LLM).**
  - N5-r6-05 (3 1 2): d=.71 immediate.
  - N5-r6-07 (3 1 2): d=.36 at 1–2 weeks.
  - Conditions: K-12, n=34, quasi-experiment vs class only; comparison humans were not the source tutors.

Candidates (line 804):
- LLM for knowledge intake: N7-r1-07 (3 2 2), contradicted by an abstract at 45 days.
- Expert-supervised LLM drafts: N7-r6-05 (3 1 2), interval crossing zero.
- Project-based mathematics: N2-r6-01 (4 1 1).
- Hint timing from hint history: N3-r4-08/09 (3 2 1).
- Human tutoring: N3-r5-02 (3 1 1).
- LLM tutoring added to instruction: N7-r3-07, -11 (3 1 1).
- Cost-of-offloading feedback: N7-r3-02 (3 1 1).
- GRE tutor equivalence: N7-r3-05c (3 2 1).
- Pedagogical agents: N7-r7-06 (4 2 1).
- Four sustainability cells: N6-r3-04, N6-r5-07, N6-r4-06, N6-r5-03.

Classed as constraints, not methods: human-authored hints, withheld solutions, cost-of-offloading feedback, contingent support, asynchronous delivery.

Trade-offs (line 806): immediate vs delayed (N2-r3-02/01, N1-r6-05/06); lab vs field (N2-r5-03/06); procedural vs transfer; speed vs learning under answer-giving; assisted product vs learner gain (N7-r7-04); AI's own metric vs independent (N5-r6-04).

## 3. Per need

**N1 Measure**
- With the assistant removed, AI arm below control on held-out items: d −0.42/−0.19/−0.42 — N1-r1-01 (3 2 1).
- The delay is part of the instrument; optimal spacing moves with the test interval — N1-r1-09 (4 1 2).
- Assisted-exam format moved the assisted score, not a 2-week closed-book quiz — N1-r4-10 (3 2 2).
- Immediate and 2-week rankings reverse — N1-r6-05/06.
- A knowledge test missed a procedural difference — N1-r6-07 (3 2 0).
- Practice sharpens resolution and worsens calibration of judgments of learning — N1-r7-04 (3 1 1).
- Self-perceived learning ran opposite to measured learning in both AI arms — N1-r7-08 (3 1 1).
- Felt AI speed-up did not show in measured time — N1-r6-09 (3 1 0).
- Null: calibration feedback — N1-r3-11 (3 1 1), N1-r4-01 (3 2 1). Harm: more underconfident on correct cases — N1-r4-02 (3 2 1).
- Threshold and continuous measures give different curves from the same data — N1-r3-01 (4 1 2).
- A delayed test is a relearning event — N1-r3-06 (UNVERIFIABLE).
- A knowledge-tracing "mastered" estimate has no forgetting term — N4-r3-02 (1 1 0).

**N2 Unit and order**
- Interleaving: age and setting confounded — N2-r5-07 (4 2 1); the paper's own p-values are inconsistent — N2-r5-02 (3 2 2).
- Subgoal labels at semester scale: quizzes up, exams not — N2-r1-07 (SURVEYED).
- Project-based mathematics d=0.529, 0.275 bias-corrected — N2-r6-01/02 (4 1 1).
- Part-task ahead at 1 month (N2-r4-02) vs whole-task ahead (N2-r1-09): both UNVERIFIABLE.
- Fading plus self-explanation positives (N2-r5-10, N2-r6-03…-06, N3-r7-09/12): all UNVERIFIABLE.
- Deliberate practice: variance explained 14% to 61–87% by definition; the teacher-design criterion adds nothing (resolution, not ledgered).

**N3 Session shape**
- Harm: unrestricted GPT-4, practice +48%, unaided exam −17%, answers copied — N3-r1-11 (3 1 1).
- Human-authored hints beat ChatGPT hints — N3-r3-04 (3 2 1).
- Expert debugging explanations beat GPT-4's on 5/5 tasks — N3-r5-04 (3 2 1).
- Hints timed from hint history: ~20% less training time, accuracy d=.45 — N3-r4-08/09 (3 2 1).
- Asynchronous feedback ≈ face-to-face at 2 days — N3-r5-06 (3 2 1).
- Tutor copilot: +4 p.p. in the session, end-of-year null — N3-r1-12 (3 1 1).
- Exercises on bypassed material helped; more exercises came with more gaming — N3-r1-07 (2 1 1).
- Hint rate responds to penalties only at mid-range baselines — N3-r3-02 (3 2 0).
- Hawthorne effect: size unknown — N3-r3-06 (4 2 0).
- Unverified: a third of feedback interventions lower performance (N3-r7-05); praise-type replication null (N3-r4-04).
- Feedback timing: no verified value.

**N4 Diagnosis**
- Tracing items separate concept from chain execution, cause uncertain — N4-r2-05 (3 2 1); α=0.75 — N4-r2-06.
- Performance-based cues beat explanation-based cues for self-assessment — N4-r2-10 (3 1 1).
- DKT predicts correctness, AUC 0.85 vs 0.68 — N4-r3-01 (3 1 0).
- Null: calibration feedback — N4-r6-05 (3 3 1).
- Non-diagnostic cues degrade judgment, and warning about them does not restore it — N4-r7-04 (3 1 0).
- SURVEYED: concept diagnosis 2–17% Macro-F1 — N4-r3-03; zero-shot below keywords — N4-r3-04; expert tutors barely diagnose — N4-r4-04/05; GPT-4 explains 96% of errors, fixes less than novices — N4-r5-03; conversational diagnosis fails when the learner cannot state the problem — N4-r2-11.
- No diagnosis predicts a delayed outcome.

**N5 Elite margin**
- AI feedback beat a live expert on its own metric; the expert ≈ no feedback; blinded OSATS tied — N5-r6-04 (3 2 1).
- Chess: partial resistance to fixation grows with expertise — N5-r2-01/03 (3 2 1).
- Code review: general coding experience predicts usefulness; repeated pairings lower it — N5-r4-01…-04 (3 3 0).
- Null: expert- and novice-taught students recalled equally at 2 weeks — N5-r6-08 (SURVEYED).
- No verified finding shows an elite coach's own behaviour beating an adequate one's.

**N6 Sustain**
- Starts cluster after temporal landmarks — N6-r3-04 (3 1 1).
- Gamified work portal, 1 year, 50 software professionals; non-randomized, monitored — N6-r5-07 (3 3 2).
- ADHD group time-management training: OR 5.41 on symptoms — N6-r4-06 (3 2 1).
- A warning before an interruption cut first-action errors — N6-r5-03 (3 1 1); the resumption cost had faded by the 3rd–4th action — N6-r5-04.
- Notification-driven adherence collapsed after the notifications stopped — N7-r3-08 (3 2 0).
- Grit explained ~4% of variance — N6-r2-03 (3 2 0).
- Curiosity came with interest 86–89% of the time; interest with curiosity 55–72% — N6-r7-04 (4 2 0).
- Unverified: a missed day costs nothing (N6-r3-02); procedural half-life ~6.5 months (N6-r2-01); weekly practice lost less than daily by 3 months (N6-r6-01).
- Implementation intentions: SURVEYED only (N6-r4-01…-04).
- Re-entry after weeks unverified; no CS-specific attention method.

**N7**: see §4; also a solution-writing assistant cut an immediate quiz 17%, d 0.74, no speed gain — N7-r1-08 (3 3 1); pre-LLM ed-tech positives 0.18–0.63 SD — N7-r6-11 (4 2 1).

## 4. LLM transfer (lines 808–865)

Holds: unaided probe, assistant removed — N1-r1-01, N7-r3-11 (no lock-out exists); hints not solutions, harm removed, no gain — N7-r1-02 (3 1 1); asynchronous feedback — N3-r5-06; structured diagnostic items — N4-r2-05/06; log correctness prediction — N4-r3-01 (O=0); recording metrics — N7-r7-12.

Fails: assisted performance as proxy — N1-r1-01, N7-r1-09, N1-r7-08, N7-r7-04, N1-r4-10; solutions on demand, four RCTs, harm from copying — N7-r1-01, N7-r3-03, N7-r1-08, N7-r1-09; LLM hints and explanations vs human-authored — N3-r3-04, N3-r5-04/05; attempt-first mechanism, unsteered LLM reveals the solution — N7-r2-01 (SURVEYED); self-explanation prompts null — N7-r4-07/08 (3 2 1, not randomized); calibration feedback — N4-r6-05; LLM concept diagnosis — N4-r3-03/04 (SURVEYED).

Gains: Socratic guidance — N7-r3-04c; cost-of-offloading feedback, OR 1.51 [0.98, 2.33] — N7-r3-02; tutoring added to instruction, 0.31 SD, g 0.33 — N7-r3-11, -07; GRE equivalence, 918× cheaper — N7-r3-05c; structured tutor vs active class — N7-r1-03; supervised drafts +5.5 p.p. [−1.4, +12.4] — N7-r6-05; knowledge intake, disputed — N7-r1-07.

Mixed: writing aid, product up, knowledge and transfer flat, fewer metacognitive processes — N7-r7-03/04; AI vs expert on motor skill, AI ahead only on its own metric, humans improve earlier — N7-r1-06, N5-r6-04, N7-r5-01/02; copilot, immediate gain, delayed null — N3-r1-12; reminders, adherence collapses after — N7-r3-08.

Untested on an LLM: spacing, interleaving, subgoal examples, problem- and project-based learning, mastery learning, gaze training (substrate sees text and files, not gaze), hint-history timing, interruption warning, contingent support (N7-r3-01), continuous watching, generated practice, always-on, withdrawal (N7-r3-10). Harm signal: unaided detection −6.0 p.p. at 3 months after AI introduction — N7-r7-01 (3 2 2, UNVERIFIABLE, observational).

Substrate facts (line 865): the default assistant reveals solutions; every positive unaided LLM result came from a study-built tutor; the null and essay results used a general chat assistant.

## 5. Refuted

- N7-r3-04: fabricated denominators; corrected as N7-r3-04c.
- N7-r3-05: figure misattributed; corrected as N7-r3-05c.
- N5-r2-02: design never run; rules out "fixation erases expertise" from it.
- N2-r4-07: 0.84 was recall, matched by two baselines; rules out a lead for automated prerequisite discovery.
- N3-r5-07: p=.197; no e-feedback needle-handling advantage.
- N1-r3-12: n misattributed; the finding stands.

## 6. Gaps and confidence

- No need saturated. Round-8 unseen title-relevant fraction: N1 51%, N2 48%, N3 50%, N4 71% (least certain), N5 42%, N6 58%, N7 62%.
- Ledger holds 1.3–3.3% of round-8 relevant DOIs. Seed coverage 0–75%. Verdicts: N1–N3, N5, N7 OPEN; N4, N6 VOID-ROUND.
- Zero VERIFIED claims on adults acquiring a CS-adjacent skill, unaided, separately tested at ≥7 days; candidates (N4-r5-01/02, N2-r5-10, N3-r7-09/12) UNVERIFIABLE.
- 89 UNVERIFIABLE, including all fading/self-explanation positives, both part/whole RCTs, feedback meta-analyses, the "myth" meta-analysis, the colonoscopy study.
- 234 SURVEYED claims (all S≤2) never verified.
- Sustainability: 7 VERIFIED O≥1 claims, 4 method cells, each flagged.
- D5, D6 and D11 are blocked on reading. D30 needs a withdrawal arm no study has.

## 7. Calibration to the owner (lines 867–873)

Intake: senior engineer; best skills from building real things and through people; stalls from interruptions and being stuck too long; self-diagnosed ADHD, hyperfocus alternating with breadth. Rulings: 120 trainer works for most everyone, owner traits shape it little; 121 feedback blunt, terse, clear; 122 continuous watching plus learner pointing at a spot; 114 intake interview plus early measurement.

Mapped: real things → problem-based, N2-r6-01/02, D6 open; people → N3-r5-02, N5-r6-05/07, N7-r6-05; stuck → solution harm, N7-r1-02, N3-r4-08/09, N3-r5-04, N7-r3-02; interruptions → N6-r5-03/04 (seconds), N6-r3-04, weeks unverified; attention → no CS-specific method, N6-r4-06 symptom outcome; curiosity → N6-r7-04.

No member rests on an owner trait.

Early measurements named: ≥7-day unaided probe on new isomorphic items beside an immediate one; pass/fail plus continuous measure; answer-vs-hint count per turn; confidence recorded, never read as learning; raw return dates and gaps.

Power, one learner: 8/12/16 units per condition detect d ≥ 1.4–1.5 / 1.2 / 1.03; literature effects run 0.2–0.7, so early sessions catch only large harm or gain. Per-member overturning signals are listed.

## 8. Tensions inside the map

- **O=2 against own caveats:** N2-r1-05/06 (pooled delay), N7-r3-04c (LLM-assisted outcome), N6-r5-07 (counts, ratings) hold O=2, while the key makes assisted performance O=0 (applied in the N7-r3-06 re-grade) and the Answer says no adult CS-adjacent ≥7-day unaided claim exists.
- **N7-r3-01** is graded O=1, though the map calls its outcome assisted performance by the rubric's own text.
- **Cost-of-offloading feedback** is listed both as a candidate and as "not a method" (line 804).
- **Grading drift on one source:** N1-r4-01 R=2 vs N4-r6-05 R=3; N6-r3-10 vs N6-r6-03; N7-r6-11 S 3 vs 4.
- **N7 rule 4:** table prints FAIL, text says closed; audit not re-run after grading changed.
- **N5-r4-07:** a verifier marked it VERIFIED; a team-lead ruling made it UNVERIFIABLE.
- **Interleaving** stays a member on one K-12 RCT while its applied motor cells shrink to n.s. (D1).
- **Counter-evidence unverifiable:** D7, D12.
- **Transfer gaps:** gaze has no text-skill analogue; the dialogue-moves tutor is pre-LLM.

## Summary

Nine methods have verified unaided outcomes: spacing, interleaving, subgoal worked examples, attempt-first under fidelity, problem-based practice, Socratic tutor guidance, gaze training, mastery learning over video and an expert-dialogue tutor. They were shown mostly in K-12, lab or medical populations, none has a sustainability cell, and none is verified on adults learning a CS-adjacent skill at ≥7 days unaided. On an LLM, handed-over solutions harm, human-authored hints beat GPT-4's, self-explanation prompts add nothing, and assisted scores and self-perception overstate skill; withdrawal, continuous watching and generated practice are untested, and no need is saturated.
