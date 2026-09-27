# AI access during practice — resolution

Tier 4 resolver, 2026-09-27. Scope: does LLM access during practice help or hurt unaided, lasting skill. Inputs: ROOT/verify/claims/{N3-r1-11, N7-r1-01, N7-r1-02, N1-r1-01, N7-r1-08, N7-r1-09} (side A), {N7-r1-07, N7-r1-03, N3-r1-12, N7-r1-04} (side B). Every source below re-fetched and re-read this run; verification files used only as pointers.

Full texts read: 7. Abstract only: 1. Unread leads: 4. Web searches: 2 attempted, 0 returned (session search budget exhausted). API calls: Crossref 6, Unpaywall 2, Semantic Scholar 2, DOAJ 1, Elsevier 1, PMC efetch 1, arXiv 5.

## The Contradiction

- Side A: LLM access during practice lowers unaided performance versus no-AI control. Four independent RCTs, all same direction: Bastani et al. 2025 (high school, math), Liu et al. 2026 (online adults, fractions, reading), Shen & Tamkin 2026 (working programmers, new library), Wu et al. 2026 (online adults, logic puzzles).
- Side B: LLM access raises unaided performance, and the gain holds at one week. Contractor & Reyes 2026 (undergraduates, 1-week retention). Also cited on B: Kestin et al. 2025 (AI tutor vs active-learning class), Wang et al. Tutor CoPilot (LLM helps the human tutor).

What looks like the dispute: same-session harm vs one-week help. What the texts show: timing does not split the studies cleanly. Timing is confounded with three other things: what the AI did, what the task was, and what counted as practice. No study in the set finds harm same-session and help at one week in the same arm. The only study measuring both timings (Contractor & Reyes) finds help at both.

## Primary Source Checks

### A1. Bastani et al. 2025, PNAS — DOI 10.1073/pnas.2422633122

URL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=12232635 (PMC full-text XML, ~7,500 words read). Crossref: no update-to.

- AI configuration, two arms. GPT Base: "a standard chat interface based on GPT-4, designed to mimic the widely used ChatGPT tool" (Introduction). GPT Tutor: its prompt includes "one or more (correct) solutions to the practice problem, as well as common student mistakes" and "instructions to avoid giving away the entire solution" (Methods; footnote †).
- Timing: "Each session has three contiguous parts … The third part is an unassisted evaluation, where students take a closed-book, closed-laptop exam" (Methods). Four sessions. Every exam is same-session.
- Result, Table 1: exam GPT Base −0.054* (SE 0.022), GPT Tutor −0.004 (SE 0.013), control SD 0.277. Practice: +0.137**, +0.361**.
- Mechanism: "students often use GPT Base as a 'crutch' by asking for and copying solutions" (Introduction). GPT Base gave "a correct answer only 51% of the time" (Mechanism), but its logical errors had no significant effect on the matching exam problems. The authors conclude copying, not wrong answers, is "the main mechanism".
- Population moderator: "limited to no statistically significant support for heterogeneous treatment effects … particularly with respect to unassisted exam performance" (Heterogeneity).
- Self-limit: "we focus on short-term outcomes due to limitations imposed by our partner school" (Discussion). Also: "our finding of a 'crutch' mechanism suggests that both types of learning would be negatively impacted" (footnote ‡). That is an inference. It was not measured.
- Deployment was Fall 2023: "modes of interaction may have changed now that users are more familiar" (Discussion).
- Supports: A for answer-giving AI, same session. Neither for guarded AI: harm gone, no gain. Says nothing about ≥7 days.

### A2. Liu, Christian, Dumbalska, Bakker, Dubey 2026, COLM — arXiv 2604.04721v4

URL: https://arxiv.org/pdf/2604.04721v4 (full text).

- AI configuration: "The AI assistant was pre-prompted with each problem and its solution, allowing participants to receive immediate, accurate answers with minimal effort … they could simply type 'answer?'" (§2.1). The AI's answers were accurate, so harm here does not depend on wrong answers.
- Timing: AI "removed without warning", then 3 test problems in the same ~13–15 min session (§2.1, §3.1).
- Result: Exp 1 d = −0.42; Exp 2 (fixes confounds) d = −0.19, P = 0.020; Exp 3 (reading) d = −0.42 (pp. 4, 5, 8).
- Moderator within the AI arm, Exp 2, self-reported and cross-sectional ("not necessarily causal", §3.3). Direct-solution users (61%) scored 0.65 vs control 0.77 (d = −0.36). Hint/clarification users (27%) scored 0.76, the same as control. Pretest was balanced across these groups (F = 1.21, P = 0.306).
- Self-limit: "participants were tested immediately after AI removal, and whether the impairments persist hours (or days) later is unknown … our AI was maximally helpful, providing complete answers on demand" (§Limitations).
- Supports: A for answer-on-demand AI, immediate. The hint subgroup is neither: no harm.

### A3. Shen & Tamkin 2026 — arXiv 2601.20245v2

URL: https://arxiv.org/pdf/2601.20245v2 (full text).

- AI configuration: "can produce the full, correct code for both tasks directly when prompted" (§4.1).
- Population: "more than one year of [language] experience, code in [language] at least once a week … never used the [library] library before" (§4.3). Programmers learning a new asynchronous library. Prior experience in the language is high; the library is new.
- Timing: quiz right after the task, same sitting (§4.3).
- Result: "reduction in the evaluation score by 17% or two grade points (Cohen's d = 0.738, p = 0.010)" (Introduction). Control scored higher "across all levels of prior coding experience" (Fig. 7).
- Moderator: six interaction patterns (Fig. 11). "Conceptual Inquiry" (n = 7) scored 65%; "Generation-Then-Comprehension" (n = 2) 86%; "AI Delegation" (n = 4) 39%; "Iterative AI Debugging" (n = 4) 24%. The clusters are exploratory, not randomized, and have 2–7 people each.
- Self-limit: "We measured skill formation … over a one-hour period" (§7.1).
- Supports: A, immediate, R3 population.

### A4. Wu, Belem, Fu, Steyvers, Smyth 2026, HCOMP — arXiv 2608.23543v1

URL: https://arxiv.org/pdf/2608.23543v1 (full text).

- AI configuration: each request "revealed the location of one randomly selected object". The simulated AI was fixed "to be perfectly correct (100%)" (§3.2). This is partial answer-giving.
- Randomized contrast, on request cost. Phase 1 → Phase 3 reward-rate gain was 1.95 (No-AI), 1.66 (High-cost), 1.32 (Low-cost). Low-cost vs No-AI: "one-sided t-test (t = 1.30, p < 0.10)". "In Phase 3, accuracy did not differ across conditions (ANOVA: F = 0.097, p = 0.91)" (§4.1).
- The headline finding compares AI users with non-users. That split is self-selected, not randomized: "for AI users, Phase 3 performance was overestimated by 0.22 reward-rate units" (§4.1).
- Timing: Phase 3 in the same session.
- Supports: A only weakly. The randomized effect is marginal and one-sided. The strong finding is observational. The assisted-overestimates-unaided finding is solid and relevant to measurement.

### B1. Contractor & Reyes 2026 — arXiv 2607.08849v1 (also IZA DP 18792)

URL: https://arxiv.org/pdf/2607.08849v1 (full text, 4,173 lines).

- AI configuration: off-the-shelf, unrestricted. "a dedicated ChatGPT (GPT-4o) account" alongside Wikipedia and the library site. Control got Google, Wikipedia and the library site (§2.1 Treatment).
- Task: learn an unfamiliar factual topic (blockchain, carbon capture, gene editing) from a 1,253–1,399-word reading in ≤35 min. Write a ~500-word essay during the same window (§2.1 Learning Phase). The practice is information intake and essay writing, not solving problems of the kind tested.
- Instrument: 5-item multiple-choice post-test in Session One, 10-item multiple-choice in Session Two, plus an unaided essay (§2.2).
- Population: Middlebury undergraduates, "mean GPA is 3.68 and the mean SAT score is 1386". "AI adoption at Middlebury exceeded 80 percent". Baseline 30.3% correct (§3).
- Result: immediate +6.7 pp = 0.27 SD (p = 0.034). One week: "ITT of β̂ = 5.1 pp (p = 0.027) … Standardized … 0.27 SD" (§5.1). Mean gap 6.99 days. Studying between sessions was <1%, balanced across arms (fn 22).
- Confound on the immediate test: "treated students are β̂ = 12.6 pp more likely to cheat (p = 0.005)". Cheating accounts for "roughly 2.2 pp, or about a third of the ITT" (§4.4 Academic Integrity).
- Moderator, from logs classified by an LLM, non-randomized, overlapping subgroups (Table 8). Automation users: essay-quality gain 0.54 SD in Session One fell to 0.02 SD at one week; test gain 0.19 SD, p = 0.330. Augmentation users: test 0.29 SD at one week, p = 0.061.
- Ability moderator: "gains tend to be larger in the upper ability quartiles (by GPA and SAT)" (Introduction).
- The authors' own sorting of 13 RCTs (§4.2): "The losses often come from settings where AI could do the practice in the learner's place … The gains often come from designs that cast AI as a coach."
- Supports: B for knowledge acquisition from text by high-ability undergraduates, at 1 week. Neither for procedural problem-solving, which was not tested. Flag: working paper, not peer reviewed.

### B2. Kestin et al. 2025, Sci Rep — DOI 10.1038/s41598-025-97652-6

URL: https://www.nature.com/articles/s41598-025-97652-6.pdf (full text).

- AI configuration: structured and guarded. "we enriched our prompts with comprehensive, step-by-step answers". The platform was "designed to guide students sequentially through each part of each problem" (Designing successful student-AI interactions).
- Comparator: "in-class active learning", not a no-AI practice condition (Study design).
- Timing and conditions: post-test at the end of each lesson. The AI group worked "at home, on their own". The main text does not say whether the at-home post-test was proctored or whether AI was withheld during it.
- Self-limit: follow-ups "would also allow for systematic integration of well-established retention enhancing strategies (e.g., spacing)" (Context, limitations).
- Supports: neither side of this dispute. It tests a structured AI tutor against an active human class, immediately, with unaided status unstated. It does not test LLM access against no LLM.

### B3. Wang, Ribeiro, Robinson, Loeb, Demszky — Tutor CoPilot, arXiv 2410.03017v2

URL: https://arxiv.org/pdf/2410.03017v2 (full text).

- AI configuration: the AI advises the human tutor. Students never use it. Treatment tutors used "Give Away Answer/Explanation" less often than control tutors (Fig. 3).
- Outcome: exit ticket, where "the tutor cannot help the student here" (Appendix, strategy table). It is unaided and same-session: 62% → 66% passing, p < 0.01.
- Delayed outcome, which the verification files omit: "we did not find statistically significant improvements in end-of-year math test scores" (§7). Appendix K Table 12: math MAP −0.35 (SE 0.88), reading +1.44 (SE 1.45). The authors attribute this to "limited variation in treatment exposure".
- Supports: neither. Learners had no LLM access. At the delayed outcome, the result is null.

### Outside the claim set, found in the texts above

- Barcaui 2025, Social Sciences & Humanities Open 12:102287, DOI 10.1016/j.ssaho.2025.102287. Crossref resolves; update-to none. Abstract only, via DOAJ API. The ScienceDirect and SSRN full texts returned 403. Abstract: "randomized controlled trial (n = 120) … undergraduates learning AI … use ChatGPT as a study aid … surprise test 45 days after learning … 57.5 % correct … vs 68.5 % … t (83) = −3.19, p = .002, Cohen's d = 0.68." Harm at 45 days, in undergraduates, with unrestricted chatbot access. This directly contradicts B1's timing argument. Flags: abstract-only; 85 analyzed of 120 (t(83)), attrition unexplained in the abstract. Supports A at ≥7 days, pending full text.
- Unread leads, to be surveyed and not used here:
  - Poulidis, Bastani & Bastani, "Self-Regulated AI Use Hinders Long-Term Learning", DOI 10.2139/ssrn.5604932 (Crossref resolves). B1 describes it as comparing system-regulated with on-demand AI "in a 12-week chess training program".
  - Kazemitabaar et al. 2023, DOI 10.1145/3544548.3580919. Per B1's appendix: novice K-12 programmers, immediate −0.05 SD, one-week code-modification +0.41 SD.
  - Bassner et al. 2026. Per B1's appendix: scaffolded tutor −0.07 SD and unrestricted chatbot −0.01 SD vs no-AI, on an unassisted test for introductory programming students.
  - Strömberg et al. 2026. Cited by B1: "AI raises homework scores but lowers exam performance".
  These come secondhand from B1's text only.

## Verdict

Both sides are right, under different conditions. Timing does not separate them. What separates them is whether the AI produced the thing the practice was supposed to make the learner produce. Five moderators, in order of evidential weight:

1. **What the AI did** (the strongest moderator; varied at random only in Bastani).
   - Gave answers or complete solutions on demand: same-session unaided harm. Bastani GPT Base −0.19 SD; Liu d −0.42 and −0.19; Shen d 0.74.
   - Accurate answers still harmed (Liu's AI held the solution; Bastani found errors did not carry over). So the harm comes from answer-giving, not from wrong answers.
   - Guarded (withholds the solution, gives teacher hints, checks answers): harm removed, no unaided gain. Bastani GPT Tutor −0.004 ns.
   - Structured tutor compared with an active class: gain, immediate (Kestin). Not a no-AI comparison.
   - Tutor-facing AI: +4 pp immediate unaided; end-of-year null (Tutor CoPilot).
2. **How the learner used unrestricted access** (associational in every study).
   - Hint or explanation use ≈ control or better: Liu hint users 0.76 vs control 0.77; C&R augmentation 0.29 SD at 1 week; Shen "Conceptual Inquiry" 65%.
   - Answer use falls below control: Liu d −0.36; Shen delegation 39%; C&R automation essay gain gone at 1 week.
   - Three studies agree on this split. None randomized it.
3. **Task type.**
   - Harm appears where practice means producing solutions of the tested kind (math problems, code, puzzles). The AI can do that practice itself.
   - Help appears where practice means taking in information, and the test checks recall and concepts by multiple choice (C&R). The AI works there as an explainer set against Google and Wikipedia.
   - C&R's own essay outcome, where the AI could write the product, shows the harm pattern for automation users.
4. **Outcome timing.**
   - All side-A harms are same-session (O=1). No side-A study measured ≥7 days.
   - At ≥7 days there is evidence in both directions: C&R +0.27 SD at 1 week (full text); Barcaui d −0.68 at 45 days (abstract only).
   - So "helps at one week" is not established as a general claim. One working paper supports it, and one peer-reviewed abstract contradicts it under similar conditions (undergraduates, unrestricted chatbot).
5. **Population and prior knowledge.**
   - Harm holds across high schoolers, online adults and experienced programmers new to a library (Shen: at every experience level).
   - C&R's gain comes from a selective college, larger in upper ability quartiles.
   - Bastani found no heterogeneity by ability.
   - Prior knowledge does not remove the answer-giving harm in the one R3 sample (Shen).

Measurement: in every study that recorded both, assisted performance overstates unaided performance. Bastani practice +48% vs exam −17%; Wu, AI users overestimated by 0.22 reward-rate units. Bastani also reports that perceived learning goes the wrong way: GPT Tutor students "perceived that they performed significantly better", and did not. Assisted scores and self-report cannot decide this question. Only an unaided probe can.

Unresolved by this evidence: whether guarded, hint-only AI beats no AI on unaided skill at ≥7 days. No study in the set measures that.

## Impact on claims

| claim_id | status | change |
|---|---|---|
| N3-r1-11 | VERIFIED, text corrected | Delete "retained". Correct text: "...scored lower on an unaided exam in the same session...". Scope: unrestricted chatbot; students mostly asked for and copied answers. O=1 (already re-graded). |
| N7-r1-01 | VERIFIED, scope added | Add: same-session exam; mechanism is copying, since GPT Base's errors did not carry over to the exam; Fall 2023 deployment. |
| N7-r1-02 | VERIFIED, scope and axes | Add: the guardrail prompt held the correct solution plus teacher hints; harm removed, no unaided gain. Drop `durability` from axes: there is no delayed measure. |
| N1-r1-01 | VERIFIED, scope added | Add: the AI was pre-prompted with solutions and gave complete answers on demand; 10–15 min exposure; immediate test. Hint-using subgroup ≈ control (cross-sectional). |
| N7-r1-08 | VERIFIED, text corrected | The randomized contrast is AI access vs none (d 0.74), not "full delegation". The six-pattern result is exploratory, 2–7 people per cluster. Correct text: "Access to an AI assistant able to write the full solution ... lowered an immediate unaided quiz by 17% (d 0.74); in exploratory clusters, conceptual-question patterns scored ≥65%, delegation patterns ≤39%." |
| N7-r1-09 | VERIFIED as worded, S 3→2 for its causal reading | The "AI users worse" contrast is self-selected. The randomized cost effect is one-sided p < 0.10, and Phase 3 accuracy did not differ (p = 0.91). Keep the assisted-overestimates-unaided finding as a measurement claim. |
| N7-r1-07 | VERIFIED, scope narrowed | Add: single 35-min session learning factual content from a text; multiple-choice knowledge tests of 5 and 10 items; elite-college sample; cheating explains up to ~1/3 of the immediate ITT; working paper. Not evidence for procedural problem-solving practice. Contradicted at ≥7 days by Barcaui (abstract only). |
| N7-r1-03 | VERIFIED, scope narrowed, O flagged | Comparator is an active-learning class, not no-AI. The tutor was structured, with solutions in the prompt and fixed sequencing. The at-home post-test's unaided status is not stated in the main text, so O=1 is conditional. Remove from the "LLM access vs none" set. |
| N3-r1-12 | VERIFIED, scope added | Tutor-facing: learners never used the LLM. Exit ticket unaided, same-session. Add: end-of-year test null (math −0.35, SE 0.88), with limited exposure. |
| N7-r1-04 | VERIFIED, scope added | Same as N3-r1-12. Not evidence on learner LLM access. |
| (new) Barcaui 2025 | SURVEYED, candidate | DOI 10.1016/j.ssaho.2025.102287; S3 R2 O2; flag abstract-only, attrition 120 → 85. Needs full-text verification before any recommendation. |
| (new) Poulidis et al.; Kazemitabaar et al. 2023; Bassner et al. 2026; Strömberg et al. 2026 | leads | Secondhand via B1. Survey and verify; Poulidis and Kazemitabaar carry delayed outcomes. |

No claim moves to REFUTED. Every quoted number matched its primary text.

## Deciding measurement for one adult learner, first sessions

Question to decide: for this learner and this material, does LLM access of a given type during practice change unaided skill at ≥7 days?

- **Design: within-person, alternating treatments.**
  - Split the first weeks' material into matched units: pairs or triples of comparable concepts or exercise families with isomorphic probe items.
  - Randomize each unit to one condition:
    - (a) no LLM during practice;
    - (b) guarded LLM: hints and concept explanation only, no solution until the learner has submitted an attempt;
    - optionally (c) unrestricted.
  - Randomizing per unit follows Bastani's and Liu's arms. Within-person comparison removes the population moderators.
- **Primary outcome: unaided, on new isomorphic items, at ≥7 days.** No LLM or references during the probe. Use items not seen in practice, as Bastani paired each exam problem to a practice problem.
- **Secondary outcomes, same session:**
  - unaided probe at the end of the session (O=1, comparable to side A);
  - skip or give-up rate on the probe (Liu's persistence measure);
  - minutes per unit (the skill-per-hour axis);
  - the learner's predicted probe score before the probe. Assisted performance and self-report are known to overestimate (Bastani, Wu), so the prediction error is itself a measurement.
- **Log every LLM turn** as answer-request vs hint or concept question. This is the moderator in Liu, Shen and C&R; logging it turns the associational finding into a within-learner check.
- **Record but do not decide on** assisted practice scores and "felt learned".
- **Power, stated honestly.**
  - With 8 units per condition, a two-sample comparison at α 0.05 and power 0.8 detects only about d ≥ 1.4 in unit-score SD. The literature's effects are d 0.2–0.7.
  - One learner over the first sessions can therefore catch a large harm or gain, not a typical one.
  - Pre-register the decision rule: condition (b) stays if its 7-day unaided mean is not below (a) by more than the spread of the (a) units.
  - Carryover between units, since concepts share parts, biases toward no difference. Order units so shared prerequisites fall in the same condition.

## Notification summary

Wrote ROOT/resolve/ai-access-resolution.md, resolving 10 claims from 7 primary full texts (1 more abstract-only; 2 web searches attempted, none returned): both sides hold under different conditions, and what separates them is whether the AI produced the learner's practice output (answer-giving harms same-session unaided skill; guarded hints are neutral; knowledge intake from text gains at 1 week), not outcome timing. No claim is refuted. Six claims get scope or text corrections (N3-r1-11 wrongly says "retained"; N7-r1-08 calls the randomized contrast "full delegation"; N7-r1-09's causal reading is self-selected, S 3→2), and Tutor CoPilot and Kestin are removed from the "LLM access vs none" set. Newly surfaced: Tutor CoPilot's end-of-year null, and Barcaui 2025 (abstract only, d −0.68 at 45 days), which contradicts the one-week gain. The first-session test is a within-person alternating-treatments design with an unaided probe at ≥7 days on isomorphic items and a logged answer-vs-hint count, which can detect only large (d ≥ 1.4) effects for one learner.
