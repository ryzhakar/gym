# Worked examples first vs attempt before instruction — resolution

Tier 4 resolver, 2026-09-27. Scope: the standing dispute, index/fields/education.md line 43 (worked examples and the minimal-guidance critique vs productive failure), the expertise-reversal effect, and impasse-driven learning. Inputs: ROOT/verify/claims/{N3-r1-02, N2-r1-10, N2-r1-05, N2-r1-06}; ROOT/ledger/claims.csv rows N3-r1-01, N3-r1-09; index education anchors #4–#9, #17, #26, #30. Sources re-fetched this run; verification files used as pointers only.

Reads:
- Full text, PDF: 9. Sinha & Kapur 2021; Kalyuga et al. 2003; Kirschner et al. 2006; Chen 2016 thesis; Schwartz et al. 2011; Chowrira et al. 2019; Mazziotti et al. 2019; Kapur et al. 2023; Margulieux et al. 2016.
- Full text, publisher HTML through WebFetch: 3. He et al. 2025; Hartmann et al. 2021; Baumgartner et al. 2025. WebFetch passes the page through an extraction model, so quotes from these three are marked (WF). Numbers were cross-checked across two fetches for He et al.
- Abstract only: 9. Ashman et al. 2020; Loibl et al. 2017; Steenhof et al. 2019; Kalyuga et al. 2001; VanLehn et al. 2003; Likourezos & Kalyuga 2017; Chen & Kalyuga 2020; Darabi et al. 2018; Kapur 2014.
- Unreachable in full: Springer challenge (curl), T&F and Wiley 403, figshare WAF, UNSW records with no files, ETH search 403. No web searches: the budget was spent.
- API calls: Unpaywall 41, Semantic Scholar 21, Crossref 42, ERIC 4, figshare 2, DSpace 6.

## The Contradiction

- **Side WE (worked examples first).**
  - Novices learn more from studying worked examples than from solving the equivalent problems. The advantage shrinks, then reverses, as expertise grows: the expertise-reversal effect. Sweller & Cooper 1985 (index #8), Kalyuga et al. 2003 (#9, N3-r1-09).
  - Minimally guided instruction fails for novices. Kirschner, Sweller & Clark 2006 (#7).
  - In the claim set, WE-design evidence on adults: Margulieux et al. 2016 (N2-r1-05, N2-r1-06).
- **Side PF (attempt before instruction).**
  - Solving problems before instruction beats instruction first on conceptual knowledge and transfer, and does not harm procedural knowledge. Pooled over 53 studies: Sinha & Kapur 2021 (N3-r1-02, N2-r1-10); Kapur 2008 (#17).
  - Learning in tutoring happens at impasses. VanLehn et al. 2003 (N3-r1-01).
- **What looks like the dispute:** the same cognitive-load facts lead to opposite orders.
- **What the texts show:** the two sides mostly test different contrasts.
  - WE studies compare, during practice, studying a worked example against solving the same problem unaided. Instruction on the principle is typically held constant.
  - PS-I studies compare the order of a generation phase and a full instruction phase. The PS-I arm always receives the full instruction afterwards.
  - Sinha & Kapur describe the I-PS comparator as "practice-oriented (rather than being generative in nature)" (p. 773). They also say the PF generation phase provides "no new canonical information … via cognitive scaffolds, worked examples" (p. 785).
  - Kirschner et al. target instruction where learners "must discover or construct essential information for themselves" (opening section). PF does not claim that the generation phase alone teaches.
  - The contrasts meet in three places, where the conflict is real:
    - (a) PS-I vs I-PS on high-element-interactivity material, in the same population;
    - (b) generating before instruction vs studying an example before instruction;
    - (c) the direction of the prior-knowledge moderator.

## Primary Source Checks

### PF1. Sinha & Kapur 2021, Rev. Educ. Res. 91(5) — DOI 10.3102/00346543211019105

URL: https://www.research-collection.ethz.ch/server/api/core/bitstreams/f6c98c41-ec4b-4996-b677-97fa3c997cf9/content (publisher PDF, read in full). Crossref: update-to none.

- **Pooled effect:** conceptual knowledge and transfer "moderate (Hedge's g = 0.36, p < .0001, 95% CI [0.20, 0.51])". Procedural knowledge: "g = −0.03, p = .7384, 95% CI [−0.20, 0.15]" (pp. 775–776).
- **Sampling frame:** articles that "cited either of the two seminal PF articles (Kapur, 2008; Kapur & Bielaczyc, 2012) and/or other key follow-up PF articles" (p. 767). Only literature that cites PF enters. The second author originated PF.
- **Population, Table 1:** 2nd–5th graders 25 comparisons (15.1%), 6th–10th 75 (45.2%), undergraduates 61 (36.7%), "Others (postgraduates, professionals)" 5 (3%).
- **Fidelity, Table 3.** Among PS-I arms that met a criterion:
  - evidence of multiple-solution generation 0.47 [0.00, 0.61] vs 0.16;
  - group work 0.49 vs 0.19;
  - "Instruction building on student solutions" 0.56 [0.07, 0.64] vs 0.20;
  - dialogue-dominant instruction 0.55 vs 0.24.
  - "Only four of these seven subgroup differences were significant (or marginally significant)". Overall fidelity score β = 0.0065, p < .001 (p. 777).
- **Fidelity is confounded with design** (pp. 777–780).
  - Experimental comparisons had mean fidelity 32.36%; quasi-experimental ones 76.78%.
  - Experimental g = 0.25 [0.04, 0.47]; quasi-experimental g = 0.46.
  - Short interventions: "cramming too many design features within a short amount of time may not be optimal".
- **Age, Table 4 and p. 779:** "The pooled effect size estimate for younger students (2nd to 5th graders) was negative, and these estimates increased … with the age range". Subgroup differences were significant "for all student subcategories (except for undergraduates)". Others (postgraduates, professionals): 1.03 [0.05, 1.39], from 5 comparisons.
- **Domain-general skills, Table 5:** −0.17 [−1.11, −0.02], from 8 comparisons: "control of variables strategy, water jug problems, Rubik's cube".
  - Explanation offered: "the problem-solving phase in and of itself is less likely to provide implicit feedback about what goals to adopt … In the absence of explicit feedback regarding what problem-solving actions are actually failures, PS-I can therefore be expected to perform worse" (p. 786).
- **Outcome type, Table 5:** transfer 0.40 [−0.19, 0.32], conceptual 0.33 [−0.30, 0.22]. "There were, however, no significant subgroup differences" (p. 780).
- **Reporting anomaly.** This check found it; the verification files did not.
  - In Tables 4–5, several intervals exclude their own point estimate: 2nd–5th −0.09 [−0.92, −0.16]; undergraduates 0.28 [−0.46, 0.24]; conceptual 0.33 [−0.30, 0.22]; transfer 0.40 [−0.19, 0.32]; Europe 0.19 [−0.59, 0.15]; North America 0.24 [−0.54, 0.09].
  - The paper does not explain this. Subgroup magnitudes cannot be read as estimate ± interval. Only the significance marks and the text statements are usable.
- **Publication bias.**
  - Egger's test "not significant (intercept = 0.63, p = .219)".
  - From the p-curve, the authors report a "true effect size (in absence of publication bias)" of g = 0.87 (p. 782).
  - A p-curve estimates the effect behind significant results only. Do not use 0.87.
- **Delay:** not coded as a moderator anywhere in the paper.
- **Self-limits:** "More studies with postgraduates and professionals need to be conducted before we can begin talking about whether PS-I treatments might positively impact such populations". "multiple RSM generation is a rather weak proxy for failure" (pp. 787–788). They cite Ashman et al. 2020: "advantages of PS-I over I-PS may diminish with increasing complexity" (p. 787).
- **Supports:** PF for conceptual outcomes in grade 6+, domain-specific material, under high fidelity. Neither side on procedural knowledge. WE for grades 2–5 and for domain-general skills. Adults: undetermined (undergraduates n.s.; professionals n = 5).

### WE1. Kalyuga, Ayres, Chandler & Sweller 2003, Educ. Psychol. 38(1) — DOI 10.1207/s15326985ep3801_4

URL: University of Wollongong Research Online copy, fetched via https://mrbartonmaths.com/resourcesnew/8.%20Research/Explicit%20Instruction/The%20Expertise%20Reversal%20Effect.pdf (full text). Crossref: update-to none.

- **Design:** narrative review of the authors' own programme of controlled experiments. No pooled estimate, no effect sizes, no test delays stated.
- **Core statement:** "Instructional techniques that are highly effective with inexperienced learners can lose their effectiveness and even have negative consequences when used with more experienced learners" (abstract).
- **Worked-example reversal:** Kalyuga, Chandler, Tuovinen & Sweller 2001, "Inexperienced mechanical trade apprentices … inexperienced trainees benefitted most from the worked examples condition … With more experience … problem solving proved superior" (section "Interactions between levels of expertise and the worked example effect").
  - Tuovinen & Sweller 1999, database use: "Students with no previous familiarity … benefitted more from worked examples. For students who had previous familiarity … there were no differences".
- **Fading:** Renkl and colleagues found "a fading out procedure was superior to an abrupt switch from worked examples to problems" (same section).
- **Element interactivity is relative to the learner:** "an assessment of element interactivity is always relative to the level of expertise of an intended learner" (section on element interactivity).
- **Measurement used:** "Subjective mental load ratings collected immediately after each stage".
- **Not in the text:** the quote in N3-r1-09's ledger row, "for higher-knowledge learners…, reduced guidance often results in better performance than well-guided instruction". Searched for "reduced guidance", "higher-knowledge", "well-guided": no match. It came from a secondary synthesis.
- **Supports:** WE during practice for novices, with reversal as expertise grows. Silent on the PS-I sequence.

### WE2. Kirschner, Sweller & Clark 2006, Educ. Psychol. 41(2) — DOI 10.1207/s15326985ep4102_1

URL: https://www.sfu.ca/~jcnesbit/EDUC220/ThinkPaper/KirschnerSweller2006.pdf (full text). Crossref: update-to none.

- **Target:** minimal guidance, where learners "must discover or construct essential information for themselves" (opening section). "The advantage of guidance begins to recede only when learners have sufficiently high prior knowledge to provide 'internal' guidance" (abstract).
- **Worked-example effect:** "occurs when learners required to solve problems perform worse on subsequent test problems than learners who study the equivalent worked examples" (section "Worked examples").
  - Two boundary conditions are stated in the text. It fails when examples "impose a heavy cognitive load". It "first disappears and then reverses as the learners' expertise increases".
- **Key cited contrast:** Klahr & Nigam 2004, control of variables. "Direct instruction involving considerable guidance, including examples, resulted in vastly more learning than discovery" (pp. 79–80). This is a domain-general skill in young children. It matches both of Sinha's reversal cells (grades 2–5, domain-general skills).
- **Grade:** S1, an argument paper. It does not test PS-I followed by full instruction.
- **Supports:** WE against unguided discovery. Not a test of PF.

### WE3. Chen 2016, PhD thesis, UNSW — DOI 10.26190/unsworks/18917

(Published as Chen, Kalyuga & Sweller 2015, DOI 10.1037/edu0000018.) URL: https://unsworks.unsw.edu.au/bitstreams/4835a79e-b19a-4e55-bb40-168112a51706/download (full text, 300 pp.).

- **Design:** five experiments, 2 (guidance) × 2 (element interactivity), Grades 4, 6, 7, 10, 11. Contrast: worked examples vs problem solving, and presented vs generated formulae.
- **Grades 4 → 6 → 7:** "the worked example group was superior to the problem solving group … reduced when using more knowledgeable students in Experiment 2 and totally reversed in Experiment 3" (§13.1).
- **Grade 10 novices, N = 34:** at 1 week, "students who studied worked example-problem solving pairs were better at solving the delayed test problems" (d = 0.65, high element interactivity). Generation won on low-interactivity material (d = 0.83). Neither effect appeared on the immediate test (§11, §13.2).
- **Grade 11:** "the generation effect was obtained on both immediate and delayed tests for both sets of material with no sign of the worked example effect" (§13.2).
- **Self-limit:** "the worked example effect has rarely been tested using delayed tests" (§13.2).
- **Supports:** WE for novices on high-interactivity material, which holds at 1 week. Generation for low-interactivity material or more knowledgeable learners. Population: K-12.

### PF2. Schwartz, Chase, Oppezzo & Chin 2011, J. Educ. Psychol. 103(4) — DOI 10.1037/a0025140

URL: http://aaalab.stanford.edu/papers/DBChin_PracticingvsInventing_JEP5_FINAL_20110720.pdf (author manuscript). Crossref: update-to none.

- **Design:** eighth graders, Exp 1 N = 128, Exp 2 N = 120. Stratified random assignment within class. Invent-with-contrasting-cases, then lecture, vs tell-and-practice on the same cases.
- **Procedural result:** "Both groups exhibited equal proficiency at using the formulas on word problems" (abstract).
- **Transfer result:** "the ICC students performed significantly better than the T&P students on the delayed transfer" problem, 21 days later (Results).
- **Design critique, quoted by the authors:** Sweller 2009, "If multiple factors are varied simultaneously … it [is] impossible to determine exactly what caused the effects" (introduction). This study holds the cases constant across arms.
- **Prior achievement:** "ICC benefitted both low- and high-achieving students" (abstract). The authors add: "students were working in pairs, so it is still possible that working individually would lead to a prior achievement by treatment interaction".
- **Supports:** PF for transfer at 21 days in adolescents. No difference on procedural outcomes.

### PF3. He, Fiorella & Lemons 2025, Educ. Psychol. Rev. — DOI 10.1007/s10648-025-09993-3

URL: https://link.springer.com/article/10.1007/s10648-025-09993-3 (WF, full text). Crossref: update-to none.

- **Design (WF):** undergraduates in two classroom experiments, randomized. Exp 1: introductory biology, n = 367, low prior knowledge. Exp 2: biochemistry, n = 138, higher prior knowledge.
  - Instruction was a video that "compared these canonical solutions to ideas commonly expressed by students". It did not build on each student's own solutions.
  - Post-test on Day 6.
- **Near transfer (WF):**
  - Exp 1: PS-I 6.34 vs I-PS 5.07, F(1,365) = 7.18, p = .008, ηp² = .019.
  - Exp 2: I-PS 10.72 vs PS-I 9.47, F(1,136) = 4.51, p = .036, ηp² = .033.
  - "Neither experiment showed significant effects of instructional sequences on the far-transfer test."
- **Practice phase (WF):** I-PS solved more during problem solving (2.72 vs 0.93). Assisted-phase performance points the opposite way from the outcome.
- **Authors' explanation (WF):** high-knowledge students may have "approached the problem-solving phase in a somewhat superficial manner".
  - Self-limit: the prior-knowledge grouping relied on "course level and test scores with overlapping distributions". The prior-knowledge contrast is between experiments, not randomized.
- **Supports:** PF for low topic knowledge and WE (I-PS) for higher topic knowledge, both small. This is the reverse of the naive expertise-reversal prediction for sequencing. One paper.

### PF4. Hartmann, van Gog & Rummel 2021, Instr. Sci. — DOI 10.1007/s11251-020-09528-z

URL: https://link.springer.com/article/10.1007/s11251-020-09528-z (WF, full text). Crossref: update-to none.

- **Design (WF):** N = 173 analyzed, mean age 16.1, mathematics (mean absolute deviation). Three arms before identical 45-min instruction "contrasted typical student solutions to the canonical solution":
  - PF: generate own solutions;
  - VF-process: watch a model generate solutions;
  - VF-outcome: see only the model's final solutions.
- **Results (WF):**
  - Conceptual: "VF-process was actually more effective for conceptual knowledge acquisition than PF, F(1, 166) = 6.91, p = 0.009, ηp2 = 0.04".
  - Procedural: "no significant differences … F(2, 168) = 0.15".
  - Prior knowledge: "students in the VF-process condition gained more from observing the process when they had higher prior knowledge, r(56) = 0.53", whereas in PF "r(55) = 0.13, p = 0.345".
- **Fidelity self-limit (WF):** "PF students in our sample generated less solution attempts … compared to a study by Loibl and Rummel". Test was immediate.
- **Contradicted by:** Kapur 2014, abstract only (Crossref), which found PF beat vicarious failure. Three explanations fit both results: generation volume, population (Singapore vs Germany), or instruction design. No evidence here separates them.
- **Supports:** WE-like (observed failure) over own failure at immediate test, when own generation is thin.

### Other primary checks

- **Chowrira, Smith, Dubois & Roll 2019**, npj Sci. Learn. — DOI 10.1038/s41539-019-0040-6 (full text).
  - Design: undergraduate biology, quasi-experiment, PF section 295 vs active-learning section 279.
  - Result: "PF students scored nearly five percentage-points higher on the relevant topics in the subsequent midterm exam", "with several weeks between manipulation and testing". "Improvement on the final exam was only visible for low-performing students."
  - Self-limit: "both sections were taught by different instructors, and students self-selected into sections".
  - Grade: S3 R2 O2, flag quasi-experimental. The comparator is active learning, not worked examples.
- **Mazziotti, Rummel, Deiglmayr & Loibl 2019**, npj Sci. Learn. — DOI 10.1038/s41539-019-0041-5 (full text).
  - 228 fifth graders. The contrasting activity was implemented. "We found no empirical support for either of our hypotheses".
  - Supports the age boundary.
- **Kapur, Saba & Roll 2023**, npj Sci. Learn. — DOI 10.1038/s41539-023-00165-y (full text).
  - PF arms only, two Singapore schools, no I-PS arm.
  - "it was inventive production that had a stronger association with learning from PF than pre-existing differences in math achievement".
  - Grade: S2 for the moderator question.
- **Baumgartner, Daguati & Trninic 2025**, Instr. Sci. — DOI 10.1007/s11251-025-09709-8 (WF, full text).
  - Population: ETH first-year engineering linear algebra, voluntary preparatory PS-I sheets.
  - Result: exam d = 0.28–0.59 vs pre-intervention cohorts.
  - Self-limit (WF): "Our design did not include a control group … It is likely that more motivated students participated more often". Grade: S2, flag selection.
- **Margulieux, Catrambone & Guzdial 2016**, Comput. Sci. Educ. 26(1) — DOI 10.1080/08993408.2016.1144429 (full text, author PDF).
  - Both arms are worked examples: "compared the effectiveness of subgoal labeled worked examples to that of conventional worked examples". No problem-solving-first arm.
  - The 36% and transfer f values match N2-r1-05/06.
- **Ashman, Kalyuga & Sweller 2020**, Educ. Psychol. Rev. — DOI 10.1007/s10648-019-09500-5 (abstract only, Springer page).
  - Year 5, two randomized experiments. Exp 1 (N = 64): I-PS superior on similar problems, "no difference on transfer". Exp 2, higher element interactivity (N = 71): I-PS superior "on both similar and transfer problems".
  - Whether the instruction built on student solutions is not visible in the abstract. Supports WE in the age cell where Sinha also finds I-PS ahead.
- **Steenhof, Woods, Van Gerven et al. 2019**, Adv. Health Sci. Educ. — DOI 10.1007/s10459-019-09895-4 (abstract only, ERIC EJ1230253).
  - 40 first-year PharmD students, randomized. "no difference … on the acquisition and application tests. However, participants in the productive failure condition outperformed … on the preparation for future learning test."
  - Test timing not stated in the abstract. S3 R2, flag n = 40, abstract-only.
- **Kalyuga, Chandler, Tuovinen & Sweller 2001**, J. Educ. Psychol. 93(3) — DOI 10.1037/0022-0663.93.3.579 (abstract only, ERIC EJ640537).
  - Adult trade apprentices: "worked examples became redundant and problem solving proved superior". R2 adults.
- **Likourezos & Kalyuga 2017**, Instr. Sci. — DOI 10.1007/s11251-016-9399-4 (abstract only, ERIC EJ1135438).
  - A worked example, partial guidance or no guidance before instruction: "no differences between the three groups on the transfer post-test", a delayed test.
  - The worked example lowered load; delayed transfer was unchanged.
- **Loibl, Roll & Rummel 2017**, Educ. Psychol. Rev. — DOI 10.1007/s10648-016-9379-x (abstract only).
  - "PS-I fosters learning only if specific design features (namely contrasting cases or building instruction on student solutions) are implemented."
- **Chen & Kalyuga 2020**, Eur. J. Psychol. Educ. — DOI 10.1007/s10212-019-00445-5 (abstract only, ERIC EJ1261949).
  - A systematic review with effect sizes by element interactivity, knowledge type and expertise. The figshare full text was blocked by its firewall. It is an S4 candidate from the WE side, still unread; the verdict below lacks its numbers.
- **Darabi, Arrington & Sayilir 2018**, ETR&D — DOI 10.1007/s11423-018-9579-9 (abstract only).
  - 12 experimental studies, "moderately positive result for the effect of learning from failure"; grade level, domain and duration not significant as moderators.
- **VanLehn, Siler, Murray et al. 2003**, Cogn. Instr. 21(3) — DOI 10.1207/s1532690xci2103_01 (abstract only, ERIC EJ675271; T&F 403, OpenAlex "closed").
  - "university physics students … when students were not at an impasse, learning was uncommon regardless of the tutorial explanations employed. When students were at an impasse, tutorial explanations were sometimes associated with learning."
- **Not reached, leads only:**
  - Glogger-Frey et al. 2015, DOI 10.1016/j.learninstruc.2015.05.001 (inventing vs studying a worked solution before instruction);
  - Kapur 2008;
  - Sweller & Cooper 1985;
  - Tuovinen & Sweller 1999;
  - Newman & DeCaro 2019;
  - Brand, Loibl & Rummel 2025, DOI 10.1007/s10648-025-10074-8;
  - Campbell review protocol, DOI 10.1002/cl2.1337 (a systematic review of PS-I in children, in progress).

## Verdict

Both sides are right under different conditions. Most of the apparent contradiction is a mismatch between contrasts.

- WE evidence says: during practice, a novice facing high-interactivity material learns more from studying a solution than from searching for one, and this reverses with expertise.
- PF evidence says: a generation attempt placed before a full instruction phase that builds on the attempt improves conceptual and transfer outcomes, without costing procedural skill.
- The two claims can both hold for the same learner. Where the two approaches do collide, six moderators decide:

1. **Fidelity of the failure phase** (strongest within-PF moderator; correlational across studies).
   - PS-I helps when the learner actually generates several solution attempts and the instruction then works from those attempts:
     - Sinha Table 3: building on student solutions 0.56 vs 0.20; evidence of multiple solutions 0.47 vs 0.16;
     - Loibl et al. 2017: "only if";
     - Kapur 2023: inventive production predicts learning better than prior achievement.
   - When generation is thin, observing a modeled attempt does better (Hartmann: VF-process > PF, η² .04).
   - Randomized experiments had lower fidelity and a smaller effect (g 0.25 [0.04, 0.47]). Fidelity is confounded with duration and with quasi-experimental design.
2. **Age.**
   - Grades 2–5 reverse toward instruction first: Sinha (significant subgroup difference); Ashman Year 5; Mazziotti fifth graders null; Klahr & Nigam in Kirschner.
   - Sinha's grade trend rises with age.
   - Adult evidence is thin: the undergraduate subgroup is not significantly different; professionals n = 5 comparisons; two adult RCTs (Steenhof n = 40, abstract only; He, small ηp²).
3. **Domain-general vs domain-specific.**
   - Domain-general strategies (control of variables, puzzle strategies) favor instruction first: Sinha −0.17 [−1.11, −0.02], 8 comparisons.
   - The stated mechanism: the attempt gives no signal about which actions are failures.
   - Domain-specific concepts favor PS-I.
4. **Prior knowledge.** It works in two directions, depending on the contrast.
   - WE vs problem solving during practice: more topic knowledge → examples become redundant, then harmful (Kalyuga 2001 apprentices; Chen Grades 4→11; Tuovinen & Sweller). No conflict with PF.
   - PS-I vs I-PS sequence: the direction is not settled.
     - Low topic knowledge did better with PS-I in He Exp 1, and the benefit was larger for low performers in Chowrira.
     - Higher topic knowledge did better with I-PS in He Exp 2, a between-experiment contrast. It did not moderate PF itself in Hartmann.
     - The expertise-reversal logic ("novices need guidance first") does not carry over to the sequence question in the adult data.
   - What PS-I needs is relevant intuitive resources to generate attempts, while the target concept is still unknown. Age proxies the first; a topic pretest measures the second.
5. **Outcome type.** Every study that separated the outcomes agrees.
   - Procedural or near-identical problems: no difference, or instruction first ahead. Sinha −0.03; Schwartz equal; Steenhof equal on acquisition and application; Hartmann equal; Ashman I-PS ahead in Year 5.
   - Conceptual, transfer and preparation-for-future-learning: PS-I ahead when fidelity holds. Sinha 0.36; Schwartz transfer; Steenhof future learning.
   - Far transfer: null in He, both experiments.
   - The WE effect is measured mainly on similar test problems.
6. **Delay** (weakest evidence; no synthesis coded it).
   - Effects at ≥7 days exist on both sides: Schwartz, PF transfer at 21 days; Chowrira, PF weeks later (quasi-experimental); Chen Exp 4, WE at 1 week but not immediately; Likourezos, a tie at delay.
   - No study shows the sign flipping with delay. "PF pays off later, WE only now" is not established.

**Impasse (VanLehn 2003).** Consistent with PF at the scale of a single tutoring step: explanations produced learning mainly after an impasse. The full text is unread and the claim is observational. It does not bear on worked examples, because worked-example study has no explanation-without-impasse condition to compare.

**Unresolved by this evidence:**
- (a) Own generation vs a studied or modeled attempt before instruction, with generation volume controlled: Hartmann and Kapur 2014 disagree, Likourezos ties, Glogger-Frey is unread.
- (b) PS-I vs I-PS for adults on high-element-interactivity, domain-specific material at ≥7 days.
- (c) Chen & Kalyuga 2020's effect sizes, unread.

## Impact on claims

| claim_id | status | change |
|---|---|---|
| N3-r1-02 | VERIFIED, scope added | Add: sampling frame is articles citing Kapur's PF papers, and the second author originated PF (flag). Delay not coded. Procedural g −0.03 ns. The grades 2–5 and domain-general reversals are significant subgroup differences, but several table intervals exclude their own point estimates (2nd–5th, undergraduates, transfer, conceptual), so the subgroup magnitudes are not usable. Undergraduates not significantly different; professionals n = 5 comparisons. Do not cite the p-curve "true effect" 0.87. Keep S4 R2 O2. |
| N2-r1-10 | VERIFIED, text corrected | Delete "(12,000+ participants)": not in the text. "g=0.37-0.58 under high fidelity" = single-criterion subgroup estimates, 4 of 7 differences significant, and confounded with quasi-experimental design and duration (experimental comparisons g 0.25 [0.04, 0.47]). O: harmonize with N3-r1-02. The pooled g covers conceptual and transfer outcomes, so O=2 by the rubric's transfer branch, flagged "transfer-only subgroup not separable". |
| N2-r1-05 | VERIFIED, scope added | Both arms were worked examples (subgoal-labeled vs conventional); no problem-solving-first arm. Evidence on worked-example design for adult novices, not on WE-vs-PF order. S3 R3 O2 unchanged. |
| N2-r1-06 | VERIFIED, scope added | Same as N2-r1-05. |
| N3-r1-09 | VERIFIED on substance, quote replaced, S2 R2 O1 | Full text read. The ledger quote is not in the article; replace it with "Instructional techniques that are highly effective with inexperienced learners can lose their effectiveness and even have negative consequences when used with more experienced learners" (abstract). Scope: narrative review of the authors' own lab experiments (trade apprentices, students); no effect sizes; no delayed tests reported. It applies to worked-example study vs problem solving during practice, not to the PS-I sequence. |
| N3-r1-01 | UNVERIFIABLE (full text closed), text corrected | T&F 403, OpenAlex "closed", no repository copy. The ERIC abstract supports "learning was uncommon" without an impasse, and says explanations were "sometimes associated with learning" at an impasse. "requires" overstates the finding. Corrected text: "In university physics tutoring, learning was uncommon when the student was not at an impasse, whatever explanation was given; at impasses, explanations were sometimes followed by learning." Observational, S2 R2 O1. |
| (new) He et al. 2025 | SURVEYED, candidate | DOI 10.1007/s10648-025-09993-3. S3 R2 O2 (near-transfer task; far transfer null). Flag: WF extraction; prior knowledge compared across experiments. |
| (new) Hartmann et al. 2021 | SURVEYED, candidate | DOI 10.1007/s11251-020-09528-z. S3 R1 O1. Modeled attempt > own attempt, conceptual. |
| (new) Schwartz et al. 2011 | SURVEYED, candidate | DOI 10.1037/a0025140. S3 R1 O2 (21-day transfer). |
| (new) Chen 2016 thesis / Chen, Kalyuga & Sweller 2015 | SURVEYED, candidate | DOI 10.1037/edu0000018. S3 R1 O2 (1-week delay), flag n = 34 in Exp 4. |
| (new) Chowrira et al. 2019 | SURVEYED, candidate | DOI 10.1038/s41539-019-0040-6. S3 R2 O2, flag quasi-experimental, comparator is active learning. |
| (new) Steenhof et al. 2019; Ashman et al. 2020; Kalyuga et al. 2001; Likourezos & Kalyuga 2017 | leads, abstract only | Full text needed before any recommendation. Steenhof and Kalyuga 2001 are adult (R2). |
| (new) Chen & Kalyuga 2020; Glogger-Frey et al. 2015 | leads, unread | The strongest missing sources on the WE side. |

No claim moves to REFUTED. Every quoted number in N3-r1-02, N2-r1-05, N2-r1-06 and N2-r1-10 matched its primary text. One ledger quote (N3-r1-09) and one parenthetical (N2-r1-10) did not.

## What an adult learner's first sessions measure, to place themselves on the moderators

Per unit (a concept or exercise family, with matched isomorphic probe items):

- **Unit type, decided before practice:** domain-specific concept vs domain-general strategy (Sinha Table 5). Only domain-specific units enter the PS-I vs WE comparison. Domain-general units have one direction of evidence (instruction first) and serve as a check on it.
- **Topic prior knowledge:** a 5–10 minute unaided pretest on the target concept, not only its prerequisites.
  - Sinha reports targeted pretests descriptively raise the PS-I effect.
  - If the learner already solves the pretest, both sides agree worked examples are redundant (Kalyuga 2003; Chen Grade 11). Log it and skip the comparison.
- **Inventive production:** in a timed generation attempt (e.g. 15–20 min), count the distinct solution approaches (Kapur 2014, 2023; Sinha criterion b).
  - This is the fidelity check the learner can observe.
  - Near-zero counts are the condition in which the modeled attempt beat own generation (Hartmann).
- **Instruction fidelity, yes/no per unit:** did the post-attempt instruction contrast the learner's own attempts with the canonical solution (Sinha's top predictor; Loibl "only if")?
- **Load:** one 1–9 mental-effort rating after each phase, the subjective load rating that Kalyuga 2003 uses as its evidence.
- **Outcomes, kept separate:**
  - procedural items (same form as practice);
  - conceptual items (explain why);
  - transfer items (same structure, new surface).
  - Collapsing them hides the split that every study shows.
- **Timing:** each probe unaided, at the end of the session and at ≥7 days (Chen Exp 4 found the WE effect only at 1 week; Schwartz found transfer at 21 days).
- **Assisted-phase score, record only:** He's I-PS arm solved more during practice (2.72 vs 0.93) and lost on near transfer. Practice-phase success does not decide the question.
- **Design:** within-person alternating treatments.
  - Each matched unit is randomized to (a) attempt, then instruction built on the attempt, or (b) worked example / instruction, then practice.
  - Order units so that shared prerequisites fall in the same condition.
  - Pre-register the rule: (a) stays for domain-specific units if its ≥7-day conceptual/transfer mean is not below (b), and its procedural mean is not below (b) by more than the spread across (b) units.
- **Power:**
  - Two-sample, α .05, power .8 (computed): 8 units per condition detect d ≥ 1.51; 12 units d ≥ 1.20; 16 units d ≥ 1.03.
  - The literature's effects are g 0.2–0.6, so one learner can detect only a large difference.
  - The placement measures (topic pretest, inventive production, unit type) inform the choice for each unit even while the outcome comparison cannot yet decide it.

## Notification summary

Wrote ROOT/resolve/we-vs-pf-resolution.md from 9 full-text PDFs, 3 publisher full texts via WebFetch and 9 abstracts (no web searches; about 115 API calls). Verdict: the sides mostly test different contrasts (worked example vs unaided solving during practice, against the order of an attempt and full instruction). They collide only where six moderators decide: fidelity of the failure phase, age (grades 2–5 reverse), domain-general skills (reverse), prior knowledge (direction depends on the contrast), outcome type (procedural tie; conceptual and transfer favor attempt-first) and delay (effects on both sides, no sign flip shown). Six claims updated with none refuted: N3-r1-09's quote is not in its source, N2-r1-10's "12,000+" is removed, N3-r1-01 is marked UNVERIFIABLE with "requires" corrected, N2-r1-05/06 are scoped out of the order question, and N3-r1-02 gains a flag on its subgroup intervals, several of which exclude their own point estimates.
