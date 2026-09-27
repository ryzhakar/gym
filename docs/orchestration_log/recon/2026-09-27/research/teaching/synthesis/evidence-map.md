# Teaching toward lasting unaided skill — Evidence map v1

> Basis: 367 sources in `ledger/sources.csv` (47 marked full-text read at survey; 26 primary sources read in full at verification, 30 more inside the three resolutions), 117 claims (40 VERIFIED / 2 REFUTED / 22 UNVERIFIABLE / 53 SURVEYED, never verified), 3 resolutions (`resolve/`), saturation table: none — `ROOT/audit/` does not exist; no saturation round was computed. Stage B, first map. Replaces `synthesis/first-protocol.md`.

Status rule applied: last row per claim_id in `ledger/claims-status.csv` governs status; grades from that row, falling back to the claim's latest non-blank grades; the `verify/claims/*.md` file is authoritative where a label disagrees. Claims enter the Pareto table only as VERIFIED with O≥1. Scope corrections from `resolve/*.md` and the verify files are carried in the claim text and the note column.

Population key: K-12 = school pupils; UG = undergraduates; ADULT-LAB = adults on lab tasks; ADULT = adults in another skill domain or a course; ADULT-CS = adults acquiring a CS-adjacent skill; MED = medical trainees or clinicians; SURG = surgical trainees. O=1 same session; O=2 ≥7 days or a transfer task; O=0 assisted, self-report, satisfaction, behaviour only.

## Answer

The methods with a verified unaided outcome are: testing on held-out items with the assistant removed (the one instrument that separates learning from assisted performance), spacing revisits to the retention target, interleaving problem types, subgoal-labeled worked examples for novices, a generation attempt before instruction where the instruction then builds on the attempt (domain-specific material, grade 6 and up), and problem-based practice for month-scale retention at a short-term exam cost. On an LLM substrate the one replicated result is negative: an assistant that hands over solutions during practice lowers unaided performance in the same session in four independent RCTs (d −0.19 to −0.74) across high-schoolers, online adults and experienced programmers, and the mechanism is answer-copying, not wrong answers. Withholding the solution removes the harm and adds no measured gain. Whether any LLM regime beats no-LLM on unaided skill at ≥7 days is unknown: one working paper says yes for knowledge intake from text, one abstract says no at 45 days, and nothing tests procedural practice. On the four axes, skill per hour and transfer carry most of the evidence, durability rests on K-12 and lab sources, sustainability has no verified claim. Of 117 claims, 40 are verified, 33 with an unaided outcome, 3 at R=3, one at R=3 and O=2 (n=40). Generated practice, continuous file watching and always-on availability, the substrate's own advantages, have no outcome study. Human-authored hints beat LLM-generated hints on learning gain in the one RCT that compared them. Seed coverage is 18%, so the map rests on an evidence base largely disjoint from the owner's own reading.

## Per need

### N1 — Measure

| claim_id | claim | S R O | population | axes | status | file |
|---|---|---|---|---|---|---|
| N1-r1-01 | Unaided held-out items after the assistant is removed: AI arm below control in 3 RCTs, d −0.42, −0.19, −0.42. Scope (resolution): the assistant was pre-prompted with each solution and gave complete answers on demand; 10–15 min exposure; hint/clarification users (27%, cross-sectional) ≈ control, 0.76 vs 0.77 | 3 2 1 | ADULT (US crowdworkers), fractions and reading; same session; not preregistered | skill per hour | VERIFIED | `verify/claims/N1-r1-01.md` |
| N1-r1-02 | Power-law practice curves are an averaging artifact; individual series fit exponential in every unaveraged set (7,910 series, 475 subjects). Boundary: exponential pattern held for 13.3% of young adults on a complex motor task (2021) | 3 1 1 | ADULT-LAB, simple RT tasks | skill per hour | VERIFIED | `verify/claims/N1-r1-02.md` |
| N1-r1-09 | Spacing that maximizes retention rises with the retention interval used to test it (317 experiments). "Schedule-independent instrument" is the surveyor's inference | 4 1 2 | ~85% young adults, lab verbal recall; intervals seconds to ~8 years | durability | VERIFIED | `verify/claims/N1-r1-09.md` |
| N1-r1-10 | 17 studies, 484 surgical trainees: no study measured transfer to operative behaviour or patient outcome | 4 2 0 | SURG; R re-graded 3→2 | transfer | VERIFIED, O=0 | `verify/claims/N1-r1-10.md` |
| N1-r1-12 | Self-regulation constructs explain 17% of learning variance (k=430). Outcome is learning, not sustained practice | 4 2 1 | adults in training | sustainability | UNVERIFIABLE (paywalled; abstract matches) | `verify/claims/N1-r1-12.md` |
| N1-r3-01 | Instrument choice changes the apparent retention curve: continuous compression depth n.s. at 2–8 months, pass/fail correct-depth 86.9%→12.81%; the swing itself n.s. (heterogeneity) | 4 1 2 | K-12 CPR, ages 6–18 | durability | VERIFIED | `verify/claims/N1-r3-01.md` |
| N1-r3-02 | Immediate post-training correct-CPR rates 74–90%: the baseline decay is read against | 4 1 1 | K-12 CPR | skill per hour | VERIFIED | `verify/claims/N1-r3-02.md` |
| N1-r3-03 | Performance and detection bias, not selection bias, dominate retention studies | 4 1 2 | K-12 CPR | durability | VERIFIED | `verify/claims/N1-r3-03.md` |
| N1-r3-05 | Half of procedural gains lost after ~6.5 months (accuracy), ~13 months (speed), 1,344 effect sizes | 4 2 2 | mixed adult procedural | durability | UNVERIFIABLE (abstract only) | `verify/claims/N1-r3-05.md` |
| N1-r3-06 | A delayed test lets learners relearn during the probe; retention and relearning must be separated | 4 2 2 | as above | durability | UNVERIFIABLE (abstract only) | `verify/claims/N1-r3-06.md` |
| N1-r3-07 | Self-reported gains track perceived environment more than cognitive indicators (n=1,713) | 3 1 0 | UG, Colombia | durability | UNVERIFIABLE (abstract only) | `verify/claims/N1-r3-07.md` |
| N1-r3-11 | Facilitator-free calibration-feedback training (Practical scoring rule) did not improve confidence calibration, N=610 and N=871 | 3 1 1 | ADULT-LAB, online panels | skill per hour | VERIFIED | `verify/claims/N1-r3-11.md` |
| N1-r3-12 | CFA-validated self-directed-learning instrument has good factor fit but no tested link to study behaviour. Refuted on n: CFA ran on 478, not 1,960 | 3 2 0 | adult distance learners | sustainability | REFUTED (n figure) | `verify/claims/N1-r3-12.md` |
| N1-r1-03 | Performance during acquisition is an unreliable index of learning | 1 2 0 | review | durability | SURVEYED | — |
| N1-r1-04 | Real-time judgments of learning are miscalibrated | 1 2 0 | review | durability | SURVEYED | — |
| N1-r1-05 | Ultrasound skill declined over 6 months; confidence declined only partly | 2 3 2 | MED n=141 | durability | SURVEYED | — |
| N1-r1-06 | Tourniquet skill: one variant decayed at 2 months, one held | 2 3 2 | MED n=32 | durability | SURVEYED | — |
| N1-r1-07 | LLM-assisted writers could not quote their own essays as well as controls at ~4 months | 2 2 2 | adults n=54; disputed (index) | durability | SURVEYED | — |
| N1-r1-08 | AI-supported performance becomes the learner's cue for own competence | 1 2 0 | conceptual | durability | SURVEYED | — |
| N1-r1-11 | Far transfer needs multi-dimensional classification, not one effect size | 1 2 0 | theory | transfer | SURVEYED | — |
| N1-r1-13 | Learners' study choices are confident, not always optimal | 2 2 1 | adults, lab | sustainability | SURVEYED | — |
| N1-r3-04 | 6-month knowledge decay measured; hands-on skill never assessed | 2 3 2 | MED n=37 | durability | SURVEYED | — |
| N1-r3-08 | Proposal: three AI-collaboration competencies instead of one prompting score | 1 1 0 | preprint | transfer | SURVEYED | — |
| N1-r3-09 | Unaided test scores extrapolate less well to AI-saturated real use | 1 2 0 | argument | transfer | SURVEYED | — |
| N1-r3-10 | Matrix sampling makes performance assessment affordable at population level | 1 1 0 | policy essay | skill per hour | SURVEYED | — |

Disputes and what moves them:
- Same-session harm vs one-week help under LLM access (`resolve/ai-access-resolution.md`): timing does not split the studies. What separates them is whether the assistant produced the thing practice was meant to make the learner produce (answer-giving harms; guarded hints neutral; knowledge intake from text gains at 1 week, one working paper, contradicted at 45 days by an abstract). In every study recording both, assisted performance overstated unaided performance (Bastani practice +48% vs exam −17%; Wu +0.22 reward-rate units).
- Threshold vs continuous instruments (N1-r3-01): same data, different curve. Neither is "the" retention.
- Self-report vs learning: weak predictor (N1-r1-12, 17%, unverifiable) and misleading proxy (N1-r1-03/04, S1); tutor-perceived learning went the wrong way in Bastani's GPT Tutor arm (perceived better, was not).

Gaps, with queries tried: cost per probe in session minutes — no claim; only datum is the ~13–15 min whole session of N1-r1-01 (`needs/n1-r3.md`: "cost effective skill assessment instrument administration time", "assessment burden time cost", both 0 relevant). Any probe on adults, CS-adjacent, ≥7 days — none. Confidence calibration on a skill task — one null RCT (N1-r3-11), no contrasting study. Transfer instrument outside simulators — N1-r1-10 finds none in its field; Aggarwal & Grantcharov's Transfer Effectiveness Ratio located, unread.

### N2 — Unit and order of practice

| claim_id | claim | S R O | population | axes | status | file |
|---|---|---|---|---|---|---|
| N2-r1-01 | Optimal inter-study interval rises with retention interval: <1 min for sub-minute retention, ≥1 month for ≥6-month retention | 4 1 2 | lab verbal recall | durability | VERIFIED | `verify/claims/N2-r1-01.md` |
| N2-r1-02 | Interleaved beat blocked practice 61% vs 38%, d=0.83 [0.68, 0.97], on an unannounced test one month later; positive for all 15 teachers | 3 1 2 | K-12, 787 7th-graders; preregistered cluster RCT | skill per hour; durability | VERIFIED | `verify/claims/N2-r1-02.md` |
| N2-r1-03 | Same trial: teachers ran interleaving without training and later endorsed it | 3 1 0 | 15 teachers | sustainability | VERIFIED, O=0 | `verify/claims/N2-r1-03.md` |
| N2-r1-05 | Subgoal-labeled worked examples: 36% more problem-solving tasks correct across two immediate and one 1-week assessment, F(1,38)=11.16, p=.002. Scope (resolution): both arms were worked examples; no attempt-first arm | 3 3 2 | ADULT-CS, n=40 UG novices, block-based app tool | skill per hour; transfer | VERIFIED | `verify/claims/N2-r1-05.md` |
| N2-r1-06 | Same experiment: component transfer f=.58 (p=.001), procedural transfer f=.37 (p=.025) | 3 3 2 | as above | transfer | VERIFIED | `verify/claims/N2-r1-06.md` |
| N2-r1-09 | Whole-task beat part-task on acquisition and transfer (4C/ID) | 3 2 1 | ADULT, n=51 pre-service teachers | skill per hour; transfer | UNVERIFIABLE (abstract; prior-knowledge clause unsupported) | `verify/claims/N2-r1-09.md` |
| N2-r1-10 | Attempt before instruction beats instruction first, g=0.36 [0.20, 0.51]; reverses for grades 2–5 and domain-general skills. Corrections: "12,000+ participants" not in the text; "g 0.37–0.58 high fidelity" is single-criterion subgroups, 4 of 7 significant, confounded with quasi-experimental design (experimental comparisons g 0.25 [0.04, 0.47]) | 4 2 1 | 15% grades 2–5, 45% grades 6–10, 37% UG, 3% postgraduate/professional; delay not coded | skill per hour; transfer | VERIFIED | `verify/claims/N2-r1-10.md` |
| N2-r3-01 | Problem-based practice beat conventional instruction on long-term retention (12 weeks to 2 years) and skill ratings; 2 of 8 source syntheses carry the retention split | 4 2 2 | MED, studies 1970–2000 | durability | VERIFIED | `verify/claims/N2-r3-01.md` |
| N2-r3-02 | Conventional instruction beat problem-based practice on immediate standardized board exams, "across all studies" | 4 2 1 | MED | skill per hour | VERIFIED | `verify/claims/N2-r3-02.md` |
| N2-r3-03 | Project-based learning d+=0.71 over traditional (30 studies). A 2026 math-only three-level re-synthesis: d=0.529, trim-and-fill 0.275 | 4 1 1 | mixed K-12 | skill per hour | UNVERIFIABLE (abstract only) | `verify/claims/N2-r3-03.md` |
| N2-r3-04 | Same meta-analysis: effect varies by subject, location, hours, IT support; not by stage or group size. IT-support finding contradicted in the 2026 math re-synthesis | 4 1 1 | mixed K-12 | skill per hour | UNVERIFIABLE (abstract only) | `verify/claims/N2-r3-04.md` |
| N2-r3-05 | Mastery learning (criterion-gated units) raised exam performance across 108 evaluations; stronger for weaker students; self-paced college versions reduce completion | 4 1 1 | K-12 and college | skill per hour | UNVERIFIABLE (abstract only) | `verify/claims/N2-r3-05.md` |
| N2-r3-06 | Simulation-based mastery learning produced downstream patient-care outcomes (23 studies) | 3 2 2 | MED | transfer; durability | UNVERIFIABLE (abstract elided; "23" unconfirmed) | `verify/claims/N2-r3-06.md` |
| N2-r3-07 | Expertise reversal for added explanations replicated on transfer, not on retention (2×2, n=93) | 3 2 2 | students | transfer | UNVERIFIABLE (abstract only; delay unknown) | `verify/claims/N2-r3-07.md` |
| N2-r3-08 | Pre-decomposed sub-parts helped novices, hurt knowledgeable learners, only on high-interactivity material (n=104) | 3 2 1 | ADULT, accounting students | skill per hour | UNVERIFIABLE (no text reached) | `verify/claims/N2-r3-08.md` |
| N2-r3-10 | Problem-based practice: higher student and staff satisfaction | 4 2 0 | MED | sustainability | VERIFIED, O=0 | `verify/claims/N2-r3-10.md` |
| N2-r1-04 | Coaches' drill-vs-play choice tracked their beliefs, not athlete age | 2 2 0 | 12 coaches | skill per hour | SURVEYED | — |
| N2-r1-07 | Subgoal labels at semester scale: quizzes up, exams not | 2 2 1 | CS1, n=265 | skill per hour; transfer | SURVEYED | — |
| N2-r1-08 | Same deployment: lower exam variance, fewer drops/fails | 2 2 1 | CS1, n=265 | sustainability | SURVEYED | — |
| N2-r1-11 | Tracing ability correlates with writing; "teach tracing first" is the authors' untested recommendation | 2 2 0 | CS1, 12 institutions | skill per hour | SURVEYED | — |
| N2-r3-09 | Naive knowledge-component discovery on 351 CS1 students' code fits poorly; purpose-built account fits better | 2 2 0 | CS1 | skill per hour | SURVEYED | — |

Disputes and what moves them:
- Worked examples first vs attempt before instruction (`resolve/we-vs-pf-resolution.md`): the sides mostly test different contrasts (studying an example vs unaided solving during practice; the order of an attempt and full instruction). Six boundary conditions: fidelity of the failure phase (instruction building on the learner's attempts 0.56 vs 0.20; multiple attempts 0.47 vs 0.16; when generation is thin, watching a demonstrated attempt beat making one's own, Hartmann 2021, SURVEYED candidate), age (grades 2–5 reverse), domain-general skills (reverse, −0.17, 8 comparisons), prior knowledge (examples become redundant then harmful as topic knowledge grows; for the sequence question, direction unsettled in adult data: He 2025 Exp 1 low knowledge → attempt first, Exp 2 higher → instruction first, between-experiment contrast), outcome type (procedural: tie or instruction-first ahead, g −0.03; conceptual and transfer: attempt-first when fidelity holds), delay (effects on both sides at ≥7 days, no sign flip shown). Several Sinha & Kapur subgroup intervals exclude their own point estimates; magnitudes unusable, significance marks only. Sampling frame: articles citing the second author's own PF papers.
- Drill vs project (N2-r3-01 vs N2-r3-02): the same synthesis ranks them oppositely by outcome window: conventional wins immediate board exams, problem-based wins 12-week-to-2-year retention. Practitioner "kata before project" (`needs/breadth-r1.md`, five sources) carries zero outcome data, S1.
- Lab-to-field shrinkage in the same programme: N2-r1-05's 1-week transfer effect held on quizzes, not exams, at semester scale (N2-r1-07, SURVEYED).
- Deliberate practice (`resolve/deliberate-practice-resolution.md`): variance explained runs 14% (broad definition, uncorrected) to 61–87% (narrow, reliability-corrected); the number moves with definition and assumed reliability, not with new data. Both camps' data agree: practice amount matters more in non-elite samples; the teacher-design criterion adds nothing measurable (r .56 vs .51, p=.64; 23% vs 26%); recent practice predicts current performance better than lifetime totals; retrospective hours are biased upward and unreliable for irregular activity (r=.35). Whether the construct applies to programming: no study relates any practice type to an objective programming outcome; the one process study (n=24 professional designers) finds feedback processing, not tenure, separates high from mid-level performers. Six proposed claims (DP-R-01…06) are not in the ledger.

Gaps, with queries tried: adult, CS-adjacent order evidence at ≥7 days — none; whole-task vs part-task — N2-r1-09 unverifiable, Wightman & Lintern 1985 unreadable; knowledge-component granularity for programming — one SURVEYED source (N2-r3-09), Learning Factors Analysis unread; project-based vs drill outside medicine — N2-r3-03/04 abstract only; expertise-reversal meta-analysis (Tetzlaff 2025) publisher-blocked; Chen & Kalyuga 2020 review unread; LLM-generated subgoal-labeled examples — 0 relevant hits (`needs/n7-r2.md`).

### N3 — Session shape and intervention

| claim_id | claim | S R O | population | axes | status | file |
|---|---|---|---|---|---|---|
| N3-r1-02 | Same meta-analysis as N2-r1-10; transfer g=0.40, procedural g=−0.03. Scope added (resolution): sampling frame cites PF's originator; subgroup intervals exclude point estimates; undergraduates not significantly different; professionals 5 comparisons; do not cite the p-curve 0.87 | 4 2 2 | as N2-r1-10 | skill per hour; transfer | VERIFIED | `verify/claims/N3-r1-02.md` |
| N3-r1-03 | Fully contingent tutoring support beat fixed support at posttest, 1 week, 1 month | 3 2 2 | K-12 (grades 4–5), n=40 | durability | UNVERIFIABLE (no text reached) | `verify/claims/N3-r1-03.md` |
| N3-r1-04 | Immediate feedback beats delayed in applied classroom studies; the reverse in list-learning labs (53 studies, 1988) | 4 2 1 | mixed | durability; skill per hour | UNVERIFIABLE (paywalled) | `verify/claims/N3-r1-04.md` |
| N3-r1-07 | Supplemental exercises on bypassed material: highest-exercise third gained 46 vs 20 points (p=0.04); gaming 33%→18% (p=0.07); anger messages alone no effect; more exercises correlated with more gaming (p<0.001) | 2 1 1 | K-12, quasi-experiment, control always first; S re-graded 3→2 | skill per hour | VERIFIED | `verify/claims/N3-r1-07.md` |
| N3-r1-10 | Feedback on help-seeking changed hint use, persisted, did not raise domain learning | 2 1 1 | K-12 geometry, n=58/67; S 3→2, R 2→1 | transfer; skill per hour | UNVERIFIABLE (bot-gated) | `verify/claims/N3-r1-10.md` |
| N3-r1-11 | Unrestricted GPT-4 raised practice scores (+48%) and lowered the unaided exam in the same session (−17%). Correction: "retained" deleted; students mostly asked for and copied answers | 3 1 1 | K-12, Turkey, ~1,000 students; O re-graded 2→1 | durability | VERIFIED | `verify/claims/N3-r1-11.md` |
| N3-r1-12 | Tutor-facing LLM copilot: +4 p.p. topic mastery (p<.01), +9 p.p. for lower-rated tutors. Scope added: learners never used the LLM; exit ticket same session; end-of-year test null (math −0.35, SE 0.88) | 3 1 1 | K-12, 900 tutors, 1,800 pupils; preregistered; preprint | skill per hour | VERIFIED | `verify/claims/N3-r1-12.md` |
| N3-r3-02 | Hint-request rate responds to scoring penalties only where baseline rates are mid-range; depends on problem type and difficulty | 3 2 0 | ADULT, university CS lab course; R 3→2 | skill per hour | VERIFIED, O=0 | `verify/claims/N3-r3-02.md` |
| N3-r3-04 | Human-authored algebra hints produced significant learning gains (24.6%, 23.7%); ChatGPT hints did not (11.1%, 1.7%); differences p=0.038; 70% of ChatGPT hints passed quality checks | 3 2 1 | ADULT, MTurk n=77; immediate | skill per hour | VERIFIED | `verify/claims/N3-r3-04.md` |
| N3-r3-05 | Premature hint requests and superficial hint reading predict lower learning gains (n=999), strongest for low prior knowledge | 3 1 1 | K-12 math ITS | skill per hour | UNVERIFIABLE (ACM-gated) | `verify/claims/N3-r3-05.md` |
| N3-r3-06 | Hawthorne effect: most of 19 studies show some effect; size, conditions and mechanism unknown after 60 years | 4 2 0 | health-science adults | skill per hour | VERIFIED, O=0 | `verify/claims/N3-r3-06.md` |
| N3-r3-08 | Raising information-access cost improved resumption after interruption, slowed completion | 3 1 1 | ADULT-LAB, copying task | skill per hour; durability | UNVERIFIABLE (host dead) | `verify/claims/N3-r3-08.md` |
| N3-r3-09 | Interruption-recovery practice transfers only to the same task pair | 3 1 1 | UG, lab | skill per hour; transfer | UNVERIFIABLE (paywalled) | `verify/claims/N3-r3-09.md` |
| N3-r3-10 | Higher working-memory capacity cuts the resumption cost of longer interruptions (n=229) | 3 1 1 | students, lab | skill per hour | UNVERIFIABLE (paywalled) | `verify/claims/N3-r3-10.md` |
| N3-r1-01 | Learning in tutoring was uncommon without an impasse; at impasses explanations were sometimes followed by learning. Resolution: "requires" overstated; marked UNVERIFIABLE in the resolution, no status row | 2 2 1 | UG physics, ~125 h dialogue | skill per hour | SURVEYED (resolution: UNVERIFIABLE) | — |
| N3-r1-05 | Formative feedback: nonevaluative, specific, timing adjustable | 1 2 0 | review | durability | SURVEYED | — |
| N3-r1-06 | Gaming frequency predicts post-test as strongly as prior knowledge | 2 1 1 | K-12 ITS | skill per hour | SURVEYED | — |
| N3-r1-08 | Teachers wait <1 s before and after a response | 1 1 0 | K-12 | skill per hour | SURVEYED | — |
| N3-r1-09 | Guidance that helps novices loses effect and can harm as expertise grows. Resolution: ledger quote not in the article; replaced with the abstract sentence; narrative review, no effect sizes, no delayed tests; applies to example study vs solving during practice, not to the attempt-first sequence | 2 2 1 | trade apprentices, students | transfer; skill per hour | SURVEYED (resolution: verified on substance, no status row) | — |
| N3-r3-01 | Deployed ITSs define wheel-spinning as 3 consecutive correct within 10–15 opportunities | 1 1 0 | K-12 ITS | skill per hour | SURVEYED | — |
| N3-r3-03 | Whether hints help or hurt flips with co-occurring affect | 2 1 0 | K-12 ITS logs | skill per hour | SURVEYED | — |
| N3-r3-07 | Observer-present vs absent: no difference once performance feedback held constant (n=5 teachers) | 2 2 0 | adult professionals | skill per hour | SURVEYED | — |

Disputes and what moves them:
- What to hand over: unrestricted answers (harm, N3-r1-11/N7-r1-01) vs teacher-hint guardrail (harm gone, no gain, N7-r1-02) vs copilot to a human tutor (immediate gain, delayed null, N3-r1-12). The variable is who produces the solution.
- Hint quality: human-authored hints beat LLM-generated hints on learning gain (N3-r3-04, immediate, adults, n=77) — one RCT, no replication.
- Feedback timing: N3-r1-04 unverifiable; Shute (S1) treats timing as tunable; no verified value.
- Being watched (ruling 122): N3-r3-06 says the effect's size and conditions are unknown; N3-r3-07 (SURVEYED) found feedback, not observation, drove change. Continuous watching has no learning-outcome study.
- Impasse-driven learning (N3-r1-01): consistent with attempt-first at single-step scale; observational; full text closed.

Gaps, with queries tried: hint granularity — `needs/n3-r3.md` found candidates (arXiv 2603.07311) unpursued; session length and breaks — Walker 2002, Baddeley & Longman 1978, Elion 2008 all unreadable, no claim; interruption and resumption — three claims, all unverifiable, all lab; CS-specific resumption (Parnin & Rugaber) unread; observation effects on skill performance specifically — audience-effect classics found, unpursued; feedback content beyond Kluger & DeNisi and Hattie & Timperley one-liners — never surveyed under N3.

### N4 — Diagnosis

| claim_id | claim | S R O | population | axes | status | file |
|---|---|---|---|---|---|---|
| N4-r2-05 | Middle-quartile CS1 students showed conceptual grasp of loops and arrays but failed the long chain of reasoning tracing requires "and/or" abstract-level reasoning; authors: "not possible to draw any firm conclusions as to the exact cause" | 3 2 1 | CS1, 7 countries, N=556; R 3→2 | transfer | VERIFIED | `verify/claims/N4-r2-05.md` |
| N4-r2-06 | The 12-item tracing/completion set: Cronbach's α=0.75, below the 0.80 convention. The reasoning-chain reading is post hoc, not the instrument's design goal | 3 2 0 | as above | skill per hour | VERIFIED, O=0 | `verify/claims/N4-r2-06.md` |
| N4-r2-10 | Self-assessment accuracy after worked examples: performance-based cues beat explanation-based cues (both experiments); telling learners the cue in advance helped in Experiment 1 only | 3 1 1 | UG, lab stochastics, N=135 and 252; immediate | skill per hour | VERIFIED | `verify/claims/N4-r2-10.md` |
| N4-r2-01 | LLM-generated misconceptions from quiz data rated "Excellent" by one expert for 93.8% of 48 items | 2 2 0 | MED courses | skill per hour | SURVEYED | — |
| N4-r2-02 | Faculty confirmed quiz-data difficult topics matched classroom experience | 2 2 0 | MED courses | skill per hour | SURVEYED | — |
| N4-r2-03 | Zero-shot GPT classification of help-request type F1=.81; GPT-4 edge on debugging sub-categories (κ .52 vs .36) | 2 3 0 | CS1, 2,082 queries | skill per hour | SURVEYED | — |
| N4-r2-04 | Fine-tuned classifier reached κ=.75, equal to human–human agreement | 2 3 0 | CS1 | skill per hour | SURVEYED | — |
| N4-r2-07 | Students who annotated while tracing got items right far more often; non-annotators 50% | 2 3 1 | CS1, 56 pages | skill per hour | SURVEYED | — |
| N4-r2-08 | Frontier LLMs 92–98% on English misconception identification (K-12 math MC) | 2 1 0 | benchmark | skill per hour | SURVEYED | — |
| N4-r2-09 | Same benchmark: accuracy drops >10 points in several non-English languages | 2 1 0 | benchmark | transfer | SURVEYED | — |
| N4-r2-11 | In a guardrailed LLM deployment, 14 of 45 students said the tool fails when they cannot yet articulate the problem | 2 3 0 | CS1, 52 students | skill per hour | SURVEYED | — |

Disputes and what moves them: none inside the claim set. Structured items (N4-r2-05/06) distinguish concept from chain execution with the authors' own hedge; open conversational diagnosis depends on the learner's ability to state the problem (N4-r2-11, SURVEYED). Selecting corrective feedback is far harder for an LLM than naming the misconception (53.4% vs 97.6%, same source as N4-r2-08, out-of-scope note).

Gaps, with queries tried: whether a diagnosis predicts a delayed outcome — 0 sources (`needs/n4-r2.md` queries 19, 21); diagnostic burden or sustainability — 0; Kruger & Dunning, Davis 2006 physician self-assessment, Qian & Lehman misconception review, Meyer 2004 teacher diagnosis — all unreadable; CodeAid, OATutor — unread; ChatGPT + code-tracing (Adeeb & Muldner 2025) — paywalled.

### N5 — Elite margin

| claim_id | claim | S R O | population | axes | status | file |
|---|---|---|---|---|---|---|
| N5-r2-01 | Probability of finding the shorter, less familiar solution rose with rating: .01 (Candidate Master) to .64 (Grandmaster). Correction: the regression covers Candidate Master to Grandmaster (n=34), not down to Class C | 3 2 1 | adult tournament chess players | transfer | VERIFIED | `verify/claims/N5-r2-01.md` |
| N5-r2-02 | Primed Candidate Masters 0% "indistinguishable" from Class C 0%, both high on the unprimed version | 1 2 1 | as above | transfer | REFUTED (Class C never saw the primed problem; their unprimed score was 0%) | `verify/claims/N5-r2-02.md` |
| N5-r2-03 | "The more expert they were, the less prone they were to the effect": partial, not full, resistance | 3 2 1 | as above | transfer | VERIFIED | `verify/claims/N5-r2-03.md` |
| N5-r2-04 | Elite coaches withhold feedback to build self-direction | 2 2 0 | 16 elite UK coaches, interviews | sustainability | SURVEYED | — |
| N5-r2-05 | Elite coaches individualize every programme | 2 2 0 | as above | skill per hour | SURVEYED | — |
| N5-r2-06 | Elite coaches favour long-term coherence over junior wins | 2 2 0 | as above | durability | SURVEYED | — |
| N5-r2-07 | Talent spotted by rapid holistic pattern recognition | 1 2 0 | 8 elite coaches | skill per hour | SURVEYED | — |
| N5-r2-08 | Coaches lack a shared vocabulary for their judgment | 1 2 0 | as above | skill per hour | SURVEYED | — |
| N5-r2-09 | Expert vs novice teachers differed on 1 of 3 coded dimensions | 2 1 0 | K-12, 10+10 | skill per hour | SURVEYED | — |
| N5-r2-10 | The null dimension had the weakest reliability | 2 1 0 | as above | skill per hour | SURVEYED | — |

Disputes and what moves them: expertise both protects against fixation and is erased by it in the same dataset (N5-r2-01/03 vs the refuted N5-r2-02 reading); explicit statable principles (Martindale) vs tacit unarticulable judgment (Christensen), both self-report. Deliberate-practice resolution: the teacher-design criterion adds nothing measurable in either camp's data; hours to chess master vary ~8-fold; elite samples 1%. Practitioner threads argue the construct does not apply to programming; the objections restate DP's own preconditions (measurable target, repetition, immediate valid feedback).

Gaps, with queries tried: expert-tutor process studies (Lepper & Woolverton, Chi 2001, VanLehn 2003) all closed; master-therapist and pedagogical-content-knowledge instruments closed; nothing verified separates an elite coach's behaviour from an adequate one's on a learner outcome; no N5 claim has O=2.

### N6 — Sustain

| claim_id | claim | S R O | population | axes | status | file |
|---|---|---|---|---|---|---|
| N6-r2-01 | Half of procedural gains lost after ~6.5 months (accuracy), ~13 months (speed); 0.06–0.08 SD per month | 4 2 2 | mixed adult | durability | UNVERIFIABLE (last status row; abstract only) | `verify/claims/N6-r2-01.md` |
| N6-r2-03 | Grit explained ~4% of variance across six samples; did not relate positively to IQ (two small negative correlations) | 3 2 0 | adults, cadets, spelling-bee children | sustainability | VERIFIED, O=0 | `verify/claims/N6-r2-03.md` |
| N6-r2-04 | Grit's higher-order structure not confirmed; perseverance of effort carries "significantly stronger" validity than consistency of interest ("essentially all" overstates) | 4 2 0 | 66,807 individuals | sustainability | UNVERIFIABLE (last row; abstract only) | `verify/claims/N6-r2-04.md` |
| N6-r2-09 | Hyperfocus more prevalent with higher ADHD symptomology (n=251, 372, preregistered); prevalence only | 3 2 0 | adults | sustainability | UNVERIFIABLE (last row; abstract only) | `verify/claims/N6-r2-09.md` |
| N6-r2-12 | Same trial as N2-r1-02, re-tagged for N6 | 3 1 2 | K-12 | durability | VERIFIED | `verify/claims/N6-r2-12.md` |
| N6-r2-13 | Same source as N2-r1-01, re-tagged for N6; "irregular bursts" phrasing is the surveyor's | 4 1 2 | lab verbal recall | durability; sustainability | VERIFIED | `verify/claims/N6-r2-13.md` |
| N6-r2-02 | Older expert pianists' maintenance predicted by later-adulthood practice, not age | 2 2 2 | pianists | durability; sustainability | SURVEYED (DP resolution: consistent, primary unread) | — |
| N6-r2-05 | ADHD engineers report body-doubling, pair programming, externalized todo systems, flexible work as attention supports | 2 3 0 | 19 professional SEs | sustainability | SURVEYED | — |
| N6-r2-06 | Same study: hyperfocus both asset and liability; no channeling method | 2 3 0 | as above | sustainability | SURVEYED | — |
| N6-r2-07 | Framework naming attention regulation among five neurodivergent-learner traits; unvalidated | 1 2 0 | CS-ed synthesis | sustainability | SURVEYED | — |
| N6-r2-08 | LLM-powered ADHD support tool: self-use prototype, unevaluated | 1 2 0 | n=1 | sustainability | SURVEYED | — |
| N6-r2-10 | Curiosity-driven attention self-organizes toward intermediate novelty; retention claim rests on an unread citation | 1 1 2 | review | durability; sustainability | SURVEYED | — |
| N6-r2-11 | Self-directed learning (what/when) encompasses self-regulated learning (how) | 1 2 0 | theory | sustainability | SURVEYED | — |

Disputes and what moves them: trait-level curiosity/grit (weak predictors, consistency-of-interest weakest) vs environmental supports (body-doubling, externalization) as the meaning of "channeling"; neither has O≥1. Hyperfocus is measurable and replicated; no source measures an intervention that changes its outcome relation. Deliberate-practice resolution: solitary practice was rated effortful and middling on enjoyment, not low, in both violin samples.

Gaps, with queries tried (`needs/n6-r2.md`, 19 queries; `needs/breadth-r2.md`, 20 HN queries): no source on scheduling under irregular bursts; no source on re-entry after a gap of weeks; no CS-specific named method for hyperfocus-and-breadth attention in academic or grey literature; Hidi & Renninger interest development, Kang 2009 curiosity-retention, Parnin & Rugaber resumption, Arthur 1998 decay — all unread. Sustainability axis: zero VERIFIED O≥1 claims in the whole ledger.

### N7 — LLM transfer

| claim_id | claim | S R O | population | axes | status | file |
|---|---|---|---|---|---|---|
| N7-r1-01 | Ungated GPT-4 during practice: unaided exam −0.054 (SE 0.022) ≈ −0.19 SD vs control, same session. Scope added: mechanism is copying (GPT Base's errors did not carry to the exam); Fall 2023 deployment; "839" is inference | 3 1 1 | K-12, Turkey | skill per hour; transfer | VERIFIED | `verify/claims/N7-r1-01.md` |
| N7-r1-02 | GPT Tutor arm (prompt held the correct solution plus teacher hints, withheld answers): exam −0.004 (n.s.) ≈ −0.01 SD; harm removed, no unaided gain. Durability axis dropped (no delayed measure) | 3 1 1 | K-12, Turkey | skill per hour; transfer | VERIFIED | `verify/claims/N7-r1-02.md` |
| N7-r1-03 | Structured AI tutor beat in-class active learning, gains over double (z=−5.6), 0.63–1.3 SD. Scope narrowed: comparator is an active class, not no-AI; tutor prompt held step-by-step answers; at-home post-test's unaided status not stated (O=1 conditional); >1.0 SD flag | 3 2 1 | UG physics, n=194, crossover | skill per hour | VERIFIED | `verify/claims/N7-r1-03.md` |
| N7-r1-04 | Same trial as N3-r1-12, re-verified; not evidence on learner LLM access; end-of-year null | 3 1 1 | K-12 | skill per hour | VERIFIED | `verify/claims/N7-r1-04.md` |
| N7-r1-05 | AI video-analysis tutor ≈ expert instructor > self-directed for laparoscopic skill (n=124); lower extraneous load applies to both tutored arms vs control | 3 2 1 | MED | skill per hour; transfer | UNVERIFIABLE (paywalled) | `verify/claims/N7-r1-05.md` |
| N7-r1-06 | AI vs expert surgical tutoring: OSATS MD 0.20 [0.01, 0.39], 3 studies n=159, 79.9% weight on one high-risk-of-bias study, low certainty; AI arm higher extraneous load (MD 0.23, p=0.01); authors recommend hybrid | 4 2 1 | SURG | skill per hour; transfer | VERIFIED | `verify/claims/N7-r1-06.md` |
| N7-r1-07 | Unrestricted GPT-4o while learning a factual topic from a text: +0.27 SD immediate, +5.1 p.p. (0.27 SD, p=.027) unaided at ~7 days. Scope narrowed: 35-min knowledge intake and essay, MC tests of 5 and 10 items, elite college (mean SAT 1386), cheating explains ~1/3 of the immediate effect, working paper; contradicted at 45 days by Barcaui 2025 (abstract only, d −0.68). Not evidence for procedural practice | 3 2 2 | UG, n=211 | skill per hour; durability | VERIFIED | `verify/claims/N7-r1-07.md` |
| N7-r1-08 | Corrected text: access to an assistant able to write the full solution, while learning a new async library, lowered an immediate unaided quiz by 17% (d 0.74, p=0.010), no significant average speed gain; delegators (~20% of treatment) 19.5 vs 23 min; six interaction patterns are exploratory, 2–7 people each (conceptual-question patterns 65–86%, delegation 39%, iterative AI debugging 24%) | 3 3 1 | ADULT-CS, n=52 crowdworkers with ≥1 year in the language | skill per hour; durability | VERIFIED | `verify/claims/N7-r1-08.md` |
| N7-r1-09 | Assisted performance overestimated post-AI unaided performance (AI users +0.22; non-users −0.15). Resolution: the "AI users worse" contrast is self-selected; randomized cost effect one-sided p<0.10, Phase 3 accuracy no difference (p=0.91); S 3→2 for the causal reading; keep as a measurement claim | 3 2 1 | ADULT, n=124, logic puzzles, same session; preprint, 0 citations | durability; transfer | VERIFIED | `verify/claims/N7-r1-09.md` |
| N7-r1-10 | LLM-assisted essay writers: weaker EEG connectivity, worse self-quotation (n=54); EEG inference disputed | 2 2 1 | adults | durability; transfer | SURVEYED | — |
| N7-r1-11 | AI-tool use correlates with lower critical-thinking scores (n=666, self-report); corrected paper | 2 2 0 | adults | sustainability; transfer | SURVEYED | — |
| N7-r1-12 | UX practitioners self-report skill erosion | 1 2 0 | forum posts | sustainability; durability | SURVEYED | — |
| N7-r2-01 | An unsteered LLM running a productive-failure lesson reveals the solution early; steering (StratL) restored process fidelity in 17 students; learning gains not measured | 2 1 0 | K-12, no control | transfer | SURVEYED | — |
| N7-r2-02 | Five LLM tutor families vs simulated disengaged learners: rankings stable, absolute quality varies; automated scoring diverges from human judgment | 2 1 0 | simulation | skill per hour | SURVEYED | — |
| N7-r2-03 | LLM spaced-repetition scheduler: 90.2% vs 88.4% on 100 simulated learners | 1 0 0 | simulation | durability | SURVEYED | — |

Disputes and what moves them: `resolve/ai-access-resolution.md`, five conditions in order of weight: what the assistant did (answers on demand → harm; withholds → neutral; structured tutor vs active class → gain, not a no-AI comparison; tutor-facing → immediate gain, delayed null), how the learner used it (hint users ≈ control, answer users below; three studies agree, none randomized it), task type (harm where practice means producing the tested kind of solution; help where practice means taking in information tested by recall), timing (all harms O=1; at ≥7 days one working paper up, one abstract down), population (harm at every experience level in the R=3 sample; gain in a selective college, larger in upper ability quartiles). Unresolved: guarded hint-only LLM vs no LLM on unaided skill at ≥7 days — no study. Practitioner "vibe-coding erosion" cluster (`needs/breadth-r1.md`) is unanimous and entirely self-report.

Gaps, with queries tried (`needs/n7-r1.md`, `needs/n7-r2.md`): endless generated practice — "AI generated practice problems personalized effectiveness" 2 pilots, no outcome; continuous watching — "LLM watching student work continuous feedback programming" 0 relevant; always-on availability — 1 registry entry, no result; LLM-generated interleaving or subgoal examples — 0; Kazemitabaar 2023 (K-12 novices, one-week code-modification +0.41 SD per secondhand), Poulidis/Bastani/Bastani (12-week chess, system-regulated vs on-demand), Bassner 2026, Strömberg 2026, Barcaui 2025 — all unread leads with delayed outcomes; CodeHelp and CodeAid outcome studies — unread.

## Pareto set

Methods × axes. Each cell: claim_id (S R O) of the best VERIFIED, O≥1 claim; "—" where none; "neg" where the verified effect is negative. Instrument facts (N1) sit below the table; they bound every cell.

| method | skill per hour | durability | transfer | sustainability |
|---|---|---|---|---|
| Unaided probe on held-out items, assistant removed (the instrument) | N1-r1-01 (3 2 1) | — | — | — |
| Space revisits to the retention target | — | N2-r1-01 (4 1 2) | — | — |
| Interleave problem types | N2-r1-02 (3 1 2) | N2-r1-02 (3 1 2) | — | — |
| Subgoal-labeled worked examples, novices | N2-r1-05 (3 3 2) | N2-r1-05 (3 3 2), 1 week | N2-r1-06 (3 3 2) | — |
| Attempt before instruction, instruction built on the attempts; domain-specific; grade 6+ | N3-r1-02 (4 2 2) | — | N3-r1-02 (4 2 2), g 0.40 | — |
| Problem-based practice over conventional instruction | neg: N2-r3-02 (4 2 1) immediate exams | N2-r3-01 (4 2 2), 12 wk–2 yr | — | — |
| Exercises targeted at bypassed material | N3-r1-07 (2 1 1) | — | — | — |
| Prompt performance-based cues for self-assessment | N4-r2-10 (3 1 1) | — | — | — |
| Human-authored hints (vs LLM-generated) | N3-r3-04 (3 2 1) | — | — | — |
| LLM withholds solutions, gives hints | N7-r1-02 (3 1 1): harm removed, no gain | — | N7-r1-02 (3 1 1), same | — |
| LLM hands over solutions during practice | neg: N7-r1-01 (3 1 1), N1-r1-01 (3 2 1), N7-r1-08 (3 3 1) | neg: N3-r1-11 (3 1 1), same session | neg: N7-r1-09 (3 2 1), measurement only | — |
| Unrestricted LLM for knowledge intake from a text | N7-r1-07 (3 2 2) | N7-r1-07 (3 2 2), 1 week; contradicted by an abstract at 45 days | — | — |
| Structured AI tutor at home vs active class | N7-r1-03 (3 2 1), comparator not no-AI | — | — | — |
| AI tutor vs expert human, procedural motor skill | N7-r1-06 (4 2 1), MD 0.20 low certainty, higher load | — | — | — |
| LLM copilot to a human tutor | N7-r1-04 (3 1 1); delayed null; no human tutor in gym | — | — | — |
| Calibration-feedback training, facilitator-free | neg/null: N1-r3-11 (3 1 1) | — | — | — |

Instrument facts: assisted performance and self-report overstate unaided skill (N1-r1-01, N7-r1-09, Bastani's perceived-learning reversal); the delay is part of the instrument (N1-r1-09); threshold and continuous measures give different curves from the same data (N1-r3-01); averaged curves bias toward a power law (N1-r1-02); a delayed test is itself a relearning event (N1-r3-06, unverifiable); one immediate session already yields majority-correct performance on a procedural skill (N1-r3-02).

The set. No verified method dominates another across all four axes, because no method has a sustainability cell and only three have two or more non-negative cells. Non-dominated members: subgoal-labeled worked examples (the only R=3, O=2 cell, n=40, one lab); attempt before instruction under fidelity (S4, transfer and conceptual, adults undetermined, procedural tie); interleaving (one preregistered field RCT, K-12, month delay); spacing to target (S4, lab recall, the only durability claim spanning years); problem-based practice (durability at months to years, R=2, at an immediate-exam cost, studies 1970–2000). The unaided probe is not a member; it is the instrument every member is measured by. Human-authored hints and withheld solutions are constraints on the LLM's turn, not methods. What trades against what: short-term exam performance against long-term retention (N2-r3-02 vs N2-r3-01); procedural fluency against conceptual and transfer outcomes (attempt-first ties on procedural, wins on transfer; worked examples win on similar problems for novices, lose as expertise grows); speed against learning under an answer-giving assistant (delegators 19.5 vs 23 min, quiz 39% vs 65–86%); assisted-phase success against the unaided outcome (He 2025's instruction-first arm solved 2.72 vs 0.93 during practice and lost on near transfer; Bastani +48% vs −17%). Every cell in the durability column except N7-r1-07 comes from K-12 or lab recall; every R=3 cell is O≤1 except N2-r1-05/06.

## LLM transfer

Per method, from `needs/n7-r2.md` (lens over 22 VERIFIED N1–N6 claims) and `resolve/ai-access-resolution.md`, against `context/substrate-audit.md`: file-change hooks and Monitor (30 min max); scheduled runs at ≥1-hour intervals; persistent per-project memory; 200k-token context; no documented lock-out of the assistant for a probe.

| method | verdict | evidence | note |
|---|---|---|---|
| Unaided probe with the assistant removed | holds | N1-r1-01: the source's own arm is an LLM chatbot | The measurement survives; the substrate has no lock-out, so removal rests on the learner |
| Assisted performance as a proxy | fails | N1-r1-01, N7-r1-09, N3-r1-11 | Overstates unaided skill in every study that recorded both |
| Spacing to the retention target | untested | substrate can schedule at ≥1 h; N7-r2-03 is simulation only, R=0 | No real learner under an LLM-computed interval |
| Interleaving | untested | 0 relevant hits for LLM-generated interleaved sequencing | |
| Subgoal-labeled worked examples | untested | 0 relevant hits for LLM-generated subgoal examples | |
| Attempt before instruction | fails (mechanism), untested (outcome) | N7-r2-01: an unsteered LLM "quickly reveal[s] the solution"; steering restored fidelity in 17 students, no learning measure | The default failure is the one the g=0.36 effect depends on not happening |
| Problem-based practice | untested | none | |
| Exercises on bypassed material | untested | N7-r2-02 shows disengagement detection is instrumentable; automated scoring diverges from human judgment | Continuous watching would supply the detection; no outcome study |
| Hints, never solutions | holds as harm-avoidance | N7-r1-02 (K-12, same session); Liu hint subgroup ≈ control (adults, cross-sectional) | No unaided gain measured; ≥7-day unknown |
| LLM-generated hints | fails vs human-authored | N3-r3-04, adults, immediate | 70% of generated hints passed quality checks; learning gains lower and non-significant |
| Solutions on demand | fails, replicated | N7-r1-01, N1-r1-01, N7-r1-08, N7-r1-09 (weak); four independent RCTs | Harm from copying, not from wrong answers (Liu's assistant held the correct solution) |
| Knowledge intake from a text with unrestricted access | gains at 1 week, disputed | N7-r1-07 vs Barcaui abstract | Not procedural practice |
| Structured, sequenced AI tutor | gains vs an active class, immediate | N7-r1-03 | Unaided status of the post-test unstated |
| Copilot to a human tutor | gains immediate, fails delayed | N3-r1-12 / N7-r1-04 | No human tutor in gym |
| AI vs expert for a procedural motor skill | roughly equal, low certainty | N7-r1-06 | Higher extraneous load in the AI arm |
| Diagnosis by structured items | holds (trainer-neutral) | N4-r2-05/06 | α=0.75 is a property of the item set |
| Diagnosis by open conversation | fails partly | N4-r2-11 (SURVEYED) | Breaks when the learner cannot articulate the problem |
| Prompting the self-assessment cue | untested | 0 relevant hits (all hits concern the LLM's own calibration) | |
| Teacher-design criterion of deliberate practice | not load-bearing | DP resolution: r .56 vs .51, p=.64; 23% vs 26% | Who designs the practice shows no measurable difference in two datasets; no source tests an automated designer |
| Continuous watching of files | untested | substrate supports it; N3-r3-06 (Hawthorne size unknown) | No learning-outcome study |
| Endless tailored practice generation | untested | none | |
| Always-on availability | untested | none; sustainability axis empty | |
| Configuration instead of teacher retraining | gains, categorical | N2-r1-03 (O=0) plus persistent memory | Not an outcome measurement |

Substrate facts that bound the verdicts: no lock-out mechanism for a probe; Monitor ends at 30 min; scheduled runs no finer than hourly; cloud runs see only cloned repositories; the assistant's default is to reveal solutions (N7-r2-01), which is the one behaviour the replicated harm evidence names.

## Calibration to the owner

Read here only, from `context/rulings-brief.md`: line 120 (the trainer must be effective for most everyone and adapt to specific students; the owner's traits must not shape the end product much; whether established CS-specific ways channel hyperfocus-and-breadth attention); line 121 as referenced by line 144 (feedback style is calibration; feedback content and timing are researched in N3); line 122 (watching: continuous, plus the learner's ability to call attention to a specific spot). Lines 118 and 119 do not appear in the brief; line 121 appears only through 144. Line 114: calibration by an intake interview before the research plus early measurement in training; records are not a calibration source. The intake interview has not happened (`docs/user_deferred_items.md` line 9 per the brief).

Which Pareto members the intake favors: unknown until the interview. What is calibration-sensitive by ruling 121 is feedback style only; every Pareto member above is content or timing, so none is decided by the interview. Ruling 120's population clause is met by the set as it stands: no member rests on a trait of the owner, and the attention sub-question has no verified claim in either direction (N6). Ruling 122's continuous watching has no outcome evidence and one S4 finding that the size of being-observed effects is unknown (N3-r3-06).

Early measurements from N1 that would confirm or overturn a member, for this learner: an unaided probe on new isomorphic items at ≥7 days is the only instrument the evidence supports (N1-r1-01, N1-r1-09); logged per item as both pass/fail and a continuous measure, since the two curves differ (N1-r3-01); with the answer-vs-hint count of every assistant turn logged, since that split separates hint users (≈ control) from answer users (below control) in three studies and none randomized it. What one learner can detect, from the resolutions' arithmetic: 8 units per condition at α .05, power .8, detects d ≥ 1.4–1.5; 12 units d ≥ 1.2; 16 units d ≥ 1.03; the literature's effects run 0.2–0.7, so the first sessions catch only a large harm or gain. Signals that would overturn a member: a ≥7-day probe below the no-assistant condition under hint-only access overturns "hints hold"; procedural items below the worked-example condition under attempt-first overturns the procedural tie for this learner; a probe at month-scale gaps below one at day-scale gaps overturns spacing-to-target for this retention window.

## Coverage gaps

Seed coverage (`verify/seed-probe.md`): 8 of 45 checkable seed citations (18%) appear in `sources.csv`; only 4 graded S≥2. By seed section: §1 target and proxies 0/7; §2 tutoring effects 3/8; §3 diagnosis 0/5; §4 practice design 2/2 checkable (clears 80% by having two items); §5 coaching 0/1; §6 struggle/intervention 1/11 (ungraded); §7 subject-agnostic core 0/4. Two seed claims contradict their primary text (Lee 2026: 118% not 75%; Sinha & Kapur's mechanism list and scaffolding claim). Seed coverage for the knowledge-component (N2 round 3) and struggle/intervention (N3 round 3) blocks from round 3 on is not an independent measure: the round-3 query sets were built from sub-areas named in the dispatch that mirror seed §6–§7 (orchestrator prompt leak, recorded); round 3 found none of those seed citations anyway.

Population: 3 of 40 VERIFIED claims at R=3 (N2-r1-05, N2-r1-06, N7-r1-08); 1 at R=3 and O=2. 17 VERIFIED claims at R=1. Zero VERIFIED claims on adults, CS-adjacent, ≥7 days.

Axes: sustainability has zero VERIFIED O≥1 claims in any need; durability rests on K-12, lab recall, medical education and one working paper.

Blocked reads: OpenAlex citing-works search failed on every verification (daily budget); ACM DL, APA, Sage, Springer, Wiley, Taylor & Francis returned bot challenges or paywalls throughout; 22 UNVERIFIABLE claims are abstract-only for that reason, including both feedback-timing sources, the procedural-decay meta-analysis, the mastery-learning meta-analysis and the 4C/ID whole-task RCT.

Never surveyed: feedback content meta-syntheses (Kluger & DeNisi; Hattie & Timperley) under N3; CodeHelp/CodeAid outcome studies; Bloom 1984 and VanLehn 2011 tutoring effect sizes (in the index, never graded); Dunlosky 2013; ICAP; the assistance dilemma; desirable difficulties as a primary source; learning-curve and knowledge-component literature (DataShop, Difficulty Factors Assessment) beyond one SURVEYED claim.

Unread leads with delayed unaided outcomes on LLM practice: Kazemitabaar 2023, Poulidis/Bastani/Bastani, Bassner 2026, Strömberg 2026, Barcaui 2025. Unread on the WE-vs-PF side: Chen & Kalyuga 2020 review, Glogger-Frey 2015, Tetzlaff 2025.

Grading drift on record: N1-r1-09 R 2→1; N1-r1-10 R 3→2; N3-r1-07 S 3→2; N3-r1-10 S 3→2, R 2→1; N3-r1-11 O 2→1; N3-r3-02 R 3→2; N4-r2-05/06 R 3→2; N5-r2-02 S 3→1; N7-r1-09 S 3→2 proposed for the causal reading (ledger row still 3). Cepeda 2006 R graded 1 by one surveyor and 2 by four.

## Confidence per need

No `ROOT/audit/` exists; saturation rules 1–2 (two zero-new rounds; Lincoln–Petersen unseen ≤10%) were never computed. Rule 3 (seed ≥80%) fails everywhere except seed §4. Rule 4 (no SURVEYED claims) fails in every need. Rule 5 (every axis has a VERIFIED claim or a logged "no evidence") fails on sustainability in every need. Every need is OPEN.

| need | rounds | claims V / U / R / S | VERIFIED O≥1 | of which R=3 | of which O=2 | S≥2 sources in ledger | full texts at survey | seed coverage |
|---|---|---|---|---|---|---|---|---|
| N1 Measure | 2 (r1, r3) | 7 / 4 / 1 / 13 | 6 | 0 | 3 | 16 | 8 | §1: 0/7 |
| N2 Unit and order | 2 (r1, r3) | 8 / 7 / 0 / 6 | 7 | 2 | 5 | 15 | 3 | §4: 2/2 |
| N3 Session shape | 2 (r1, r3) | 8 / 6 / 0 / 8 | 5 | 0 | 1 | 21 | 10 | §5: 0/1; §6: 1/11 |
| N4 Diagnosis | 1 (r2) | 3 / 0 / 0 / 8 | 2 | 0 | 0 | 9 | 10 | §3: 0/5 |
| N5 Elite margin | 1 (r2) | 2 / 0 / 1 / 7 | 2 | 0 | 0 | 3 | 9 | §5: 0/1 |
| N6 Sustain | 1 (r2) | 3 / 3 / 0 / 7 | 2 | 0 | 2 | 9 | 5 | — |
| N7 LLM transfer | 2 (r1, r2 lens) | 9 / 1 / 0 / 5 | 8 | 1 | 1 | 18 | 6 | §2: 3/8 |

Source counts are unique DOI/URL rows tagged to the need in `sources.csv`; a source tagged to two needs counts in both. "Full texts at survey" is `full_text_read=Y` at survey time; verification read 26 sources in full across all needs.

## What was not verified

- 53 claims SURVEYED and never sent to verification, listed per need above; among them the entire N4 LLM-diagnosis block (N4-r2-01…04, -08, -09, -11), every N5 coach-interview claim, every N6 attention claim, N7-r1-10…12 and N7-r2-01…03.
- 22 UNVERIFIABLE claims, all abstract-only or unreachable, none contradicted: N1-r1-12, N1-r3-05, -06, -07, N2-r1-09, N2-r3-03, -04, -05, -06, -07, -08, N3-r1-03, -04, -10, N3-r3-05, -08, -09, -10, N6-r2-01, -04, -09, N7-r1-05.
- 2 REFUTED: N1-r3-12 (n=1,960 misattributed to a CFA run on 478; the substantive finding stands), N5-r2-02 (the study did not run the design the claim describes).
- Claims the resolutions changed without a ledger row: N3-r1-01 (to UNVERIFIABLE, text corrected), N3-r1-09 (verified on substance, ledger quote not in the article); index corrections to Macnamara 2014's figures (corrected 24/23/20/5/1, overall 14%) and three author or target attributions; six proposed DP-R claims and eleven SURVEYED candidates from the resolutions (He 2025, Hartmann 2021, Schwartz 2011, Chen 2015, Chowrira 2019, Barcaui 2025 and others) not appended.
- Full texts read at verification but with an unconfirmed sub-claim: N2-r1-10 ("12,000+"), N7-r1-01 ("839"), N7-r1-06 ("n=268" is the intake, OSATS n=159), N6-r2-03 ("did not correlate with IQ"), N4-r2-10 ("informing in advance", Exp 1 only), N5-r2-01 (range down to Class C).
- `sources.csv` was read by script for counts and grades, not row by row.

## Where `synthesis/first-protocol.md` changes

Items the later evidence alters; the rest of that file's checklist items stand as written.

- N7 table, "Full delegation … fails for learning": the randomized contrast is access vs none (d 0.74), not delegation; the six-pattern split is exploratory, 2–7 people per cluster (`resolve/ai-access-resolution.md`, N7-r1-08). "Interaction patterns … holds for learning" is likewise exploratory.
- N7 table, "On-demand AI … then removed: fails": the "AI users worse" contrast is self-selected; the randomized cost effect is one-sided p<0.10 and Phase 3 accuracy did not differ; N7-r1-09 stands only as a measurement claim (assisted overestimates unaided).
- N7 table, "AI access … tested unaided a week later: holds, disputed": scope narrows to knowledge intake from a text tested by multiple choice in an elite college with cheating explaining ~1/3 of the immediate effect; contradicted at 45 days by Barcaui (abstract). Not evidence for procedural practice.
- N7 table, "Structured AI tutor vs in-class active learning: holds, immediate only": the comparator is an active class, not no-AI, and the at-home post-test's unaided status is unstated; removed from the "LLM access vs none" set.
- N7 table, "LLM copilot to a human tutor": add the end-of-year null (math −0.35, SE 0.88).
- N7 table, "Hints in place of answers … holds": the guardrail prompt held the correct solution plus teacher hints; the result is harm removed, no gain; durability axis dropped. Adult support added: Liu's hint subgroup ≈ control (cross-sectional). New constraint: LLM-generated hints scored lower learning gains than human-authored hints (N3-r3-04, adults, immediate).
- N3 "Assisted gains do not carry to unaided performance" (N3-r1-11): "retained" deleted; same-session only; mechanism is copying.
- N2 "Attempt before instruction": add the fidelity conditions the effect depends on (instruction built on the learner's attempts; multiple attempts; thin generation favours a demonstrated attempt over one's own), the design confound (experimental g 0.25), the unusable subgroup magnitudes, and "adults undetermined" (undergraduates n.s., professionals 5 comparisons). On an LLM substrate the default behaviour violates the mechanism (N7-r2-01).
- N2 "Subgoal-labeled worked examples, then problem solving": both arms were worked examples; the source says nothing about order relative to an attempt.
- N2, whole-task vs part-task: still unverifiable. New: problem-based practice beats conventional instruction on 12-week-to-2-year retention and loses on immediate exams (N2-r3-01/02, medical education, S4 R2), the first verified evidence on the project-vs-drill question; the practitioner "kata before project" belief remains S1.
- N1 checklist "Log per item: solved / skipped / wrong": add a continuous measure beside the pass/fail, since the two instruments give different retention curves (N1-r3-01); note that a delayed probe is itself a relearning event (N1-r3-06, unverifiable). Baseline: one session already yields majority-correct performance on a procedural skill (N1-r3-02, K-12 CPR).
- N1 proxies: facilitator-free calibration-feedback training did not improve calibration (N1-r3-11); self-reported gains track environment (N1-r3-07, unverifiable); self-assessment accuracy is better with performance-based cues than explanation-based cues (N4-r2-10).
- "Not covered yet — N4": now three VERIFIED claims. A tracing/completion item set separates conceptual grasp from chain execution with the authors' own "and/or" and no firm cause; α=0.75; open conversational diagnosis breaks when the learner cannot state the problem (SURVEYED).
- "Not covered yet — N5": two VERIFIED chess claims and one REFUTED; nothing on coaches at O≥1. The teacher-design criterion of deliberate practice adds nothing measurable (resolution, not ledgered).
- "Not covered yet — N6": VERIFIED O≥1 claims are the same two sources as N2 (spacing, interleaving) re-tagged; the procedural-decay half-life and the grit meta-analysis fell to UNVERIFIABLE on the last status row; sustainability still has zero.
- Threats table, "Abstract-level reading": 22 UNVERIFIABLE now, not 6. "Grading drift": add N3-r1-10, N3-r3-02, N4-r2-05/06, N5-r2-02, N7-r1-09. "Seed anchoring": now measured, 18%, with a recorded prompt leak from round 3.
- Basis line: 20 claims → 40 VERIFIED, 33 at O≥1, 3 at R=3; 14 full texts → 26 at verification plus 30 in resolutions.

---

Notification summary: Wrote `ROOT/synthesis/evidence-map.md` from 117 claims (40 VERIFIED, 33 with an unaided outcome, 3 at R=3), 3 resolutions, the seed probe and every need file; the answer is that held-out unaided probing, spacing to the retention target, interleaving, subgoal-labeled worked examples, attempt-before-instruction under fidelity, and problem-based practice are the methods with verified unaided outcomes, while an assistant that hands over solutions during practice is the one LLM finding replicated four times, and it is negative. The Pareto set is those five methods plus the probe as instrument, with withheld solutions and human-authored hints as constraints on the assistant's turn, no member dominant, and sustainability empty for all. The biggest gap: no verified claim on adults acquiring a CS-adjacent skill measured unaided at ≥7 days under any regime, LLM or not, and no outcome study of the substrate's own advantages (generated practice, continuous watching, always-on availability); no saturation audit exists, seed coverage is 18%, and 22 claims are abstract-only.
