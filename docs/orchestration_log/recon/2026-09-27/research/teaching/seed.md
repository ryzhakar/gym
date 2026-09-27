# Research seed: an elite personal trainer for CS-adjacent hard skills

## Object of inquiry

An AI-run personal trainer, available at any hour, serving one adult learner across CS-adjacent hard skills. Its sole objective is the learner's durable, unaided capability. Three strands came up:

1. What an elite trainer does that a merely good tutor does not.
2. A mechanic in which the trainer watches a shared working file (the "paper") and engages on file writes or checker verdicts (e.g. bacon). The aim is to let the learner struggle the efficient and effective amount, and no more.
3. A split between a subject-agnostic learning core and subject-specific packs. The packs are the learner's to define.

Learner context: an experienced backend developer (Python, PostgreSQL/ClickHouse, LLM applications) who is a beginner in Rust, the first target domain. Later domains range widely: distributed systems, WebAssembly, ML frameworks, embedded, desktop and frontend.

## Provenance

Everything below comes from a single conversational pass: roughly forty web searches and a handful of page fetches. Most findings were read at the level of abstracts, author summaries, or secondary coverage; very few full papers were read. Each item carries a tag:

- **[F]** full text or primary page read
- **[A]** abstract or author-written summary seen
- **[S]** secondary coverage only (press, blogs, summaries by others)
- **[R]** recalled from background knowledge, not retrieved in this pass

---

## 1. The target and its proxies

### Findings

- **Bastani et al., "Generative AI without guardrails can harm learning," PNAS 2025** [A]. Field experiment with nearly 1,000 Turkish high-school math students.
  - Two GPT-4 tutors: an unguarded ChatGPT-like interface ("GPT Base") and a prompt-safeguarded "GPT Tutor."
  - Practice-session grades rose 48% (Base) and 127% (Tutor).
  - Once access was removed, the Base group scored 17% below students who never had access.
  - Per secondary coverage, the Tutor group scored about the same as control on the exam: harm removed, no gain [S].
  - https://papers.ssrn.com/abstract=4895486 · https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education
- **Deslauriers et al., PNAS 2019** [A]. Randomized comparison in large intro physics courses.
  - Students in active-learning sections learned more but perceived they learned less than peers in lectures by highly rated instructors.
  - The authors attribute this partly to cognitive effort being read as poor learning.
  - https://openlab.citytech.cuny.edu/gamelab/files/2023/01/Deslauriersa-et-al-2019.pdf
- **Shen & Tamkin (Anthropic), "How AI assistance impacts the formation of coding skills," Jan 2026** [F].
  - Setup: RCT, n=52 mostly junior engineers learning the Trio async library.
  - Main result: quiz scores of 50% (AI) vs 67% (hand-coding), Cohen's d=0.738, p=0.01. The time saving (about 2 minutes) was not significant, and the largest gap was on debugging questions.
  - Qualitative interaction clusters, low-scoring (<40%): full delegation (n=4), progressive reliance (n=4), iterative AI debugging (n=4).
  - Qualitative interaction clusters, high-scoring (≥65%): generation-then-comprehension (n=2), hybrid code+explanation (n=3), conceptual inquiry only (n=7). Conceptual inquiry was second fastest overall.
  - Generation-then-comprehension looked nearly identical to delegation. It differed only in follow-up questions used to check understanding.
  - The control group's errors fell on the Trio concepts the quiz tested. Pilot studies were used to remove irrelevant struggles such as Python syntax.
  - Stated limits: small sample, a quiz taken right after the task, and no measure of agentic tools.
  - https://www.anthropic.com/research/AI-assistance-coding-skills · https://arxiv.org/abs/2601.20245
- **Chi, Siler & Jeong 2004, "Can tutors monitor students' understanding accurately?"**, seen through Wittwer, Nückles & Renkl's replication [A].
  - Tutors overestimated tutees' correct understanding and underestimated their incorrect understanding.
  - Assessment accuracy correlated with tutee learning and depended on the tutor's content knowledge.
  - https://repositories.cdlib.org/content/qt1c169462/qt1c169462.pdf
- **Person et al. 1994 (tutoring dialogue analysis)** [A].
  - Tutors tend to follow pre-planned curriculum scripts (citing Putnam 1987), so misconceptions are rarely diagnosed and repaired.
  - Tutors often accept a student's self-report of understanding.
  - https://talkbank.org/class/access/0docs/person1994.pdf
- Feynman's account of Brazilian physics students who could recite the rule for polarized reflection but did not recognize the phenomenon in real light (*Surely You're Joking*) [R].

### Counter-evidence

- **Kazemitabaar et al., CHI 2023** [A]. 69 novices aged 10–17 worked through 45 Python authoring tasks; half had Codex.
  - Every authoring task was followed by an unaided modification task.
  - Codex raised authoring performance (1.15× completion, 1.8× scores) without lowering performance on the unaided modification tasks.
  - A week later, the Codex group did slightly better on retention tests (not significant). Learners with higher Scratch pre-test scores did significantly better if they had had Codex access.
  - https://arxiv.org/abs/2302.07427
  - Follow-up log analysis of the coding approaches used (Koli Calling 2023) [A]: https://ar5iv.labs.arxiv.org/html/2309.14049

### Hypotheses from this pass

- Four signals are weak proxies for durable unaided capability: assisted task success, the learner's feeling of learning, self-report, and the tutor's impression.
- The divergence between Kazemitabaar and Bastani/Anthropic may come from design: an unaided task after every assisted task, a younger learner population, and different outcome measures. This is untested.
- How the learner uses AI (delegation vs conceptual inquiry) may matter more than whether AI is present at all. The Anthropic cluster analysis is observational, not causal.

### Unknowns

- Retention beyond one week under AI assistance.
- Effects on experienced adult developers learning a new domain, as opposed to K-12 or junior learners.
- Effects of agentic coding tools, as opposed to chat sidebars.

---

## 2. How large tutoring effects are, human and AI

### Findings

- **VanLehn 2011, meta-review** [A]. Effect sizes against no tutoring: human tutoring d=0.79; step-based ITS 0.76; substep-based 0.40; answer-based 0.31.
  - The commonly assumed values (human 2.0, ITS 1.0) were not confirmed.
  - VanLehn's proposed mechanism: short inference chains between interactions make errors easy to locate, and hints launch just enough inference to reach the next step.
  - https://quality.mit.edu/files/2012/01/Quality-Symposium-Kurt-VanLehn.pdf · https://www.nectec.or.th/icce2011/speakers/ICCE2011_kurt_20111117.pdf
- **Bloom 1984, "two sigma problem"** [S]. Tutoring combined with mastery learning, about 2 SD. Widely cited as optimistic.
- **Guryan et al. (Saga Education), NBER w28531** [A]. High-dosage in-school tutoring RCTs in Chicago: +0.16 SD, then +0.37 SD in a replication, with effects persisting into later years. https://ideas.repec.org/p/nbr/nberwo/28531.html
- **Kestin et al., "AI tutoring outperforms in-class active learning," Scientific Reports 2025** [A].
  - Setup: 194 Harvard intro-physics students in a crossover design. The custom GPT-4 tutor was built on the same pedagogical practices as the in-class lesson.
  - Result: students learned significantly more in less time, reported more than twice the learning gain, and took a median 49 vs 75 minutes [S].
  - Scope: a two-week study; retention and transfer not measured.
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/
- **De Simone et al. (World Bank), "From Chalkboards to Chatbots," 2025** [A].
  - Setup: six-week after-school program in Nigeria using Microsoft Copilot (GPT-4) with teacher guidance.
  - Result: +0.31 SD overall and +0.23 SD in English, with larger effects for female and higher-performing students.
  - https://reproducibility.worldbank.org/catalog/419
- **Wang et al., "Tutor CoPilot," 2024** [A].
  - Setup: an LLM gave live guidance to human tutors; 900 tutors and 1,800 K-12 students.
  - Result: students were 4 pp more likely to master topics, and 9 pp more for students of lower-rated tutors.
  - Tutors with access asked more guiding questions and gave away fewer answers.
  - https://arxiv.org/abs/2410.03017
- **Eedi / LearnLM study, 2025** [S]. 165 students aged 13–15.
  - Supervising tutors approved 76.4% of LearnLM's responses with little or no editing.
  - Success on subsequent harder topics: 66% (LearnLM) vs 61% (human tutor) vs 56% (static hints).
  - https://nssa.stanford.edu/studies/tutor-copilot-human-ai-approach-scaling-real-time-expertise
- **Jurenka et al., LearnLM-Tutor, 2024** [A].
  - Argues the main obstacles are turning pedagogical intuitions into prompts and the lack of good evaluation practice.
  - Introduces seven pedagogical benchmarks. https://arxiv.org/abs/2407.12687
- Productized learning modes exist: Claude Code's Learning and Explanatory output styles, and ChatGPT Study Mode (referenced in the Anthropic study page) [F].

### Hypotheses from this pass

- Being patient, always available, and able to answer anything gets a tutor to "good" (about 0.8 SD). The headroom above that lies in precise diagnosis, designed practice, and honest verification, the things ordinary tutors rarely do.
- Tutor design, not the underlying model, separates harm from gain. Bastani (GPT-4, harm or neutral) and Kestin (GPT-4, large gain) point this way, but the populations, subjects, and baselines differ too much for a clean comparison.

### Unknowns

- Head-to-head comparisons of AI tutor designs with the model held constant.
- Evidence from adult, self-directed learners in CS.
- Long-horizon effects of AI tutors, measured in months rather than weeks.

---

## 3. Diagnosis and misconceptions

### Findings

- The tutor-accuracy findings in §1 (Chi et al.; Person et al.).
- **Crichton, Gray & Krishnamurthi, OOPSLA 2023** [A]. A grounded conceptual model for Rust ownership.
  - Built the "Ownership Inventory." Rust learners could not connect static and dynamic semantics, for example saying whether a rejected program would actually cause undefined behavior.
  - A permissions-based conceptual model with a compiler-plugin visualizer raised inventory scores by about 9% (N=342, d=0.56).
  - https://cs.brown.edu/~sk/Publications/Papers/Published/cgk-grounded-model-rust-ownership/
  - The companion "Profiling Programming Language Learning" (OOPSLA 2024) instrumented the Rust Book with quizzes (title and venue only) [A]. https://rust-book.cs.brown.edu/
  - This is an example of domain-level concept-inventory work of the kind a subject pack could draw on.
- **Hypercorrection effect** (Butterfield & Metcalfe 2001) [A].
  - High-confidence errors are more likely to be corrected after feedback than low-confidence ones; a surprise/attention account is favored.
  - Replicated with delayed tests and with conceptual and classroom materials [A]. https://pmc.ncbi.nlm.nih.gov/articles/PMC4036076 · https://par.nsf.gov/servlets/purl/10309371
  - Reported weaker in older adults [A]. https://pmc.ncbi.nlm.nih.gov/articles/PMC3604148
- LLM-based misconception diagnosis is an active research area.
  - Mitton et al. 2026 diagnose misconceptions from student–tutor dialogue with a generate–retrieve–rerank pipeline [A]. https://arxiv.org/pdf/2602.02414
  - A 2024 knowledge-tracing paper notes prior work finding LLMs ineffective at anticipating and following flawed student reasoning [A]. https://arxiv.org/pdf/2409.16490

### Hypotheses from this pass

- A trainer can treat diagnosis as hypothesis testing: keep named misconception hypotheses per skill and design probes whose answers discriminate between them.
  - Example raised for Rust: one probe asks for the concrete execution that would go wrong without the borrow check. A second asks whether removing the last use of a borrow makes the program compile. The first probe separates "rule as slogan" from a real memory model; the second separates "borrow lasts to end of scope" from liveness.
- Predictions with confidence ratings, made before each run, both harvest hypercorrection and build a calibration record.

### Unknowns

- How accurately current LLMs diagnose misconceptions from code, process data, or short probes.
- Whether concept inventories exist for other CS domains (e.g. concurrency, distributed systems, databases) and how good they are. Not searched.

---

## 4. Practice design

### Findings

- **Koedinger, Carvalho, Liu & McLaughlin, "An astonishing regularity in student learning rate," PNAS 2023**, across 27 datasets [A/S].
  - A typical student needed about 7 practice opportunities to reach 80% accuracy on a typical knowledge component (KC).
  - Students differed widely in starting point (about 4 vs 13 opportunities between quartiles) but little in rate (about 7 vs 8).
  - https://hechingerreport.org/proof-points-the-myth-of-the-quick-learner/
  - Replication on MATHia (15,000+ students) supported the finding [A]. https://educationaldatamining.org/edm2024/proceedings/2024.EDM-short-papers.40/index.html
  - Lee et al. 2026 challenge it [A]: truncating practice sequences inflates the estimated spread in learning rates (by 75% when capped at ten opportunities), so the regularity is sensitive to how observations are included. https://arxiv.org/pdf/2605.01690
- **Deliberate practice dispute** [A].
  - Macnamara, Hambrick & Oswald 2014: deliberate practice explained 26% of performance variance in games, 21% in music, 18% in sports, 4% in education, and under 1% in professions. https://stafforini.com/works/macnamara-2014-deliberate-practice-and/
  - Macnamara et al. 2016: practice explained 18% of variance in sports overall and 1% among elite performers.
  - Ericsson's reply: Macnamara used a much broader definition ("structured practice"). The original concept involved master teachers who give individualized instruction and set goals for solitary practice. https://frontiersin.org/article/10.3389/fpsyg.2019.02396/full
- **Xie et al., "A theory of instruction for introductory programming skills," 2019** [A].
  - Four skills learned incrementally: tracing, writing syntax, comprehending templates, and writing with templates. Read before write; semantics before templates.
  - https://faculty.washington.edu/ajko/papers/Xie2019IntroCSTheoryOfInstruction.pdf
  - Related: Nelson et al. 2017, PLTutor, a comprehension-first pedagogy [A]. https://faculty.washington.edu/ajko/papers/Nelson2017PLTutor.pdf
- **Expertise reversal effect** (Kalyuga et al. 2003) [A/S].
  - Worked examples are efficient early and become redundant or harmful as expertise grows.
  - Faded examples and completion tasks smooth the transition. https://www.springerpflege.de/chapter/10.1007/978-1-4419-8126-4_14
- **McLaren et al. (worked examples vs high-assistance software)** [A].
  - Worked examples, tutored problems, and erroneous examples produced equal learning outcomes, with worked examples much more efficient.
  - The result held when feedback was curtailed. https://repub.eur.nl/pub/86388
- **Sinha & Kapur 2021, meta-analysis of productive failure** (53 studies, 166 comparisons) [A/S].
  - Problem-solving before instruction beat the reverse, with additive gains when implemented with high fidelity to productive-failure principles.
  - Scaffolding the preparatory problem-solving toward success added no learning benefit.
  - Proposed mechanisms: activation, awareness, affect, and assembly. The approach requires some prior knowledge, and an expert must explain the canonical solution and why attempts missed.
  - https://www.research-collection.ethz.ch/entities/person/b29f1844-44e9-4b5f-b2f8-d3de80b033c4 · https://edutopia.org/article/if-youre-not-failing-youre-not-learning
- **Dunlosky et al. 2013** [A/S].
  - High utility: practice testing and distributed practice.
  - Moderate: self-explanation, interleaving, elaborative interrogation.
  - Low: rereading, highlighting, summarization.
  - https://www.sciencedaily.com/releases/2013/01/130110111734.htm

### Tensions

- **Worked examples vs productive failure.** Both have meta-analytic or multi-study support and point in opposite directions for the start of learning. Candidate moderators raised: prior knowledge, conceptual vs procedural targets, and the fidelity of the consolidation phase. Unresolved here.
- **"Only struggle teaches" vs worked-example efficiency.** Effort appears necessary; failure appears to be one tool among several.

### Hypotheses from this pass

- Projects are performance, not practice. Practice consists of isolated, feedback-rich repetitions on a specific weakness.
- A trainer's main output is a stream of well-aimed practice opportunities with feedback at the level of individual steps; explanations come second.
- Guidance fades as a function of evidence, not time.

---

## 5. Feedback style and coaching

### Findings

- **Tharp & Gallimore 1976; Gallimore & Tharp 2004 reanalysis** of John Wooden's 1974–75 practices [A/S].
  - 2,326 coded acts: instructions 50.3%, "hustles" 12.7%, the scold-then-reinstruct move 8%, praise 6.9%, reproofs 6.6%. About 75% of acts carried information.
  - Signature move: model the correct action, the incorrect one, then the correct one again, with demonstrations rarely longer than three seconds.
  - The 2004 reanalysis concluded that meticulous planning underlay the information density.
  - Reported planning practice: about two hours each morning, drills on 3×5 cards, notes on individual players.
  - https://www.thefivecoatconsultinggroup.com/the-coronavirus-crisis/great-coach · https://bakadesuyo.com/2012/06/what-does-it-take-to-coach-the-best-performan/ · https://www.theartofcoachingvolleyball.com/what-a-coach-can-teach-a-teacher/ · https://choralnet.org/archives/428909
- Recalled but not retrieved [R]:
  - Lepper & Woolverton's INSPIRE model of expert tutors.
  - Gawande, "Personal Best" (New Yorker, 2011), on coaching in surgery.
  - Chi et al. 2001, "Learning from human tutoring" (prompting-only tutoring as effective as explaining).
  - Chi & Wylie 2014, the ICAP framework.
  - Koedinger & Aleven 2007, "assistance dilemma".
  - Bjork, "desirable difficulties".

### Unknowns

- The Wooden evidence is observational data on one coach in one sport. Whether information density and minimal praise transfer to text-mediated adult technical learning is untested here.

---

## 6. Struggle, confusion, and detecting when to intervene

### Findings

- **Impasses:** VanLehn et al. 2003, reported in D'Mello's work: in over 100 hours of human tutoring dialogue, comprehension of physics concepts was rare when learners did not reach an impasse [S]. https://cdn2.psychologytoday.com/assets/2024-02/EJ1190004.pdf
- **Productive confusion:** D'Mello, Lehman, Pekrun & Graesser 2014, "Confusion can be beneficial for learning" [A].
  - Confusion helps when appropriately induced, regulated, and resolved.
  - Productive conditions: the source is linked to the content, the learner attempts resolution, and help arrives when they struggle [S].
  - Unresolved confusion tends toward frustration, then boredom and disengagement. This is the "zone of optimal confusion" [S].
  - https://acuresearchbank.acu.edu.au/item/8v7v6/confusion-can-be-beneficial-for-learning · https://sciencedaily.com/releases/2012/06/120620103233.htm · https://publications.ascilite.org/index.php/APUB/article/download/1905/1731/8955
- **Compiler-error struggle metrics** [A].
  - Jadud's Error Quotient (EQ) scores consecutive failed compiles, with a penalty for repeated error types.
  - Becker's Repeated Error Density (RED) is less context-dependent and usable on short sessions.
  - Both are imperfect proxies, and EQ is context-sensitive.
  - https://arxiv.org/pdf/2404.05988 · https://researchrepository.ucd.ie/entities/publication/4a56127f-90db-4d9f-8b9e-9c6aa0d6d400
  - The ProgSnap2 paper (ITiCSE 2020) compared EQ, RED, and Watwin across five datasets and several languages: each was only mildly predictive of performance. https://dx.doi.org/10.1145/3341525.3387373
- **Wheel-spinning:** Beck & Gong 2013 [S].
  - After about 10 practice attempts, roughly two-thirds of students had mastered a skill, and more attempts barely raised the share. The rest needed different interventions.
  - https://new.igi-global.com/article/understanding-wheel-spinning-in-the-context-of-affective-factors/133177
  - A decision-tree study [A] linked wheel-spinning to heavy bottom-out hint use and short delays between problems on the same skill, favoring spacing and sparing use of bottom-out hints. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/210
  - Wheel-spinning is also associated with help avoidance [S].
  - Early detection models for wheel-spinning exist (Gong & Beck 2015; Botelho et al., RNN-based) [S]. https://arxiv.org/pdf/2009.13371
- **Bottom-out hints as worked examples:** Shih, Koedinger & Scheines 2008 [A]. Learners who spend time processing a bottom-out hint learn from it. A response-time model separates productive from abusive use and captures self-explanation. https://www.cmu.edu/dietrich/philosophy/docs/scheines/Shih_Koedinger_Scheines_2008_EDM.pdf
- **Interruption timing** [A].
  - Iqbal & Bailey 2005: interruptions at predicted low-workload task boundaries caused less resumption lag and annoyance. https://www.interruptions.net/literature/Iqbal-CHI05-p1489-iqbal.pdf
  - Parnin & Rugaber 2011 (10,000 sessions, 85 programmers): only 10% of sessions resumed coding within a minute. https://sites.cc.gatech.edu/reverse/repository/resumptionstrategies.pdf
  - Counterpoint: a field study found *longer* resumption lags at interruptions during application switching (a breakpoint type) in real office conditions. https://www.ai.rug.nl/~niels/publications/p1801-tanaka.pdf
- **Tooling** [F].
  - bacon (background checker) ships analyzers for Rust (cargo, clippy, nextest, miri, JSON diagnostics), C++, Go, Python (pytest, ruff, unittest), JS/TS (biome, eslint, tsc), and Swift. Its cargo_json analyzer enables export of detailed diagnostics to other tools (e.g. bacon-ls). https://dystroy.org/bacon/analyzers/
  - ProgSnap2 is a standardized format for programming process data (events, code snapshots, metadata) [A]. https://dx.doi.org/10.1145/3341525.3387373

### Hypotheses from this pass (design ideas, unvalidated)

- **Information-rate rule.** Struggle is worth its cost while it produces new information: for the learner (new ideas being generated and tested about the target) or for the trainer (attempts revealing which misconception is held).
  - Repeated identical errors, returns to earlier file states, and friction off the target skill produce none.
- **Event roles.**
  - File saves serve as the process record, snapshotted into a separate shadow git repository.
  - Checker verdicts serve as the decision points. Every verdict source is normalized to one event shape: timestamp, source, status, and items with signature, location, and knowledge component.
  - Deterministic code decides *whether* to engage; the language model decides only *what* to say.
- **Channels.**
  - The trainer writes a task header once and otherwise never edits the paper. It speaks in a separate "margin" (a file or pane), one line per engagement, tagged with a reason code.
  - It speaks at verdict-time breakpoints only.
- **Paper markers** (comment lines): predictions with confidence, hypotheses, questions, and an "I'm spinning" signal.
  - Predictions are auto-scored against the next verdict.
  - Fresh hypothesis and prediction lines count as information and extend the struggle budget.
  - Idle time alone never triggers help.
- **Four modes, each with its own help policy.**
  - Explore: silent on the target; ends when distinct attempts stop, followed by consolidation.
  - Practice: a hint ladder on stall.
  - Probe: no help; asking ends the probe and scores a miss.
  - Perform: log only, review afterward.
- **Errors classified on-target vs off-target** against the task's declared target skills. Off-target friction is cleared immediately with no pedagogy.
- **Hint ladder:** orient, then locate, then name the principle, then a contrasting worked case, then bottom-out.
  - A bottom-out hint creates a debt: a self-explanation line now and a scheduled unaided redo later.
- **Circuit breaker.** When a skill fails repeatedly across episodes, the trainer stops hinting and switches method (worked example, prerequisite probe, different representation), then defers the skill.
- **Stall thresholds (invented defaults, not evidence-based):** the same error signature on three consecutive verdicts; a return to a previously seen file state; or several minutes idle with a failing verdict and no new hypothesis lines.
- **Per-learner tuning.** An episode log (skill, mode, duration, highest hint rung reached, later unaided probe result) adjusts thresholds slowly. With a single learner, the data is thin.

### Unknowns

- Whether struggle metrics designed for novice compile errors carry over to experienced adults, type-heavy languages (Rust's borrow checker), test failures, or non-code verdicts.
- Whether process signals (saves, verdicts, state cycling) can distinguish productive thinking from stalling without affect sensing.
- Appropriate time or struggle budgets for adult learners in any CS domain. No evidence-based numbers were found.
- How intervention timing research applies to a self-chosen training session, as opposed to office work.

---

## 7. Subject-agnostic core vs subject packs

### Findings

- **Knowledge-component modeling (CMU LearnLab / DataShop)** [A].
  - Human-designed student models are often wrong and should be discovered from data rather than designed.
  - A good KC decomposition produces smooth learning curves. Bumpy curves, no apparent learning, or unexpected error rates point to model problems.
  - https://learnlab.org/wp-content/uploads/2019/11/DataShopLearnSphere.pdf · https://learnlab.org/datashop/ResearchGoals
  - **Difficulty Factors Assessment:** when one task is much harder than a closely related one, the gap implies at least one extra KC.
    - Stamper & Koedinger 2011 refined models this way; Koedinger et al. 2013 report a redesigned tutor from an improved model producing faster, better learning [A/S].
    - https://jedm.educationaldatamining.org/index.php/JEDM/article/download/212/pdf_29
  - Retuning knowledge-tracing parameters to reduce over- and under-practice shortened instructional time (Cen, Koedinger et al.) [S]. https://datashop.phzh.ch/about/casestudies.html
  - Limitation: a JEDM paper finds learning-curve-based refinement of domain models is unreliable under some conditions, so historical refinements may need re-examination [A]. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/316

### Hypotheses from this pass

- **The core owns everything about learning:** the learner model, modes, struggle policy and ladder, scheduler, feedback style, prediction ledger, and self-audit against delayed unaided probes.
- **A pack supplies only:** a skill graph with prerequisites; verdict adapters with a map from error signatures to skills; tasks tagged with target skills and suitable modes; a register of which claims are facts and which are matters of taste; and marker syntax.
- **Leak test:** the core contains no subject vocabulary, and swapping packs changes nothing in it.
- **The pack's skill graph is a hypothesis.** The trainer proposes splits or merges with evidence (e.g. a "single" skill that is trivial in one form and impossible in another), and the learner approves.
- **Ground-truth ranking by trust:**
  1. Executable verdicts: compilers, tests, proof checkers, model checkers, query results.
  2. Comparison against a reference answer.
  3. The trainer's own judgment, weighted least in the learner model.
- Most CS-adjacent domains can reach the first rung. Design-heavy topics are the hardest case.

### Unknowns

- Student modeling and skill discovery with a single learner, where statistical learning curves are unavailable.
- How reliable LLM judgment is as an evaluator of learner work in domains without executable verdicts. Not searched.
- Whether general knowledge-tracing methods (Bayesian Knowledge Tracing, the Additive Factors Model) behave sensibly on sparse, heterogeneous, self-directed practice.

---

## 8. Cross-cutting limits of the evidence found

- Most experimental evidence comes from K-12 or undergraduate learners, math and physics, and short horizons (weeks). Adult, self-directed, CS-specific, long-horizon evidence was not found.
- Several headline AI-tutoring results are one study each, with small samples (Anthropic, n=52; Kestin, 2 weeks; Eedi, n=165) or populations far from an experienced adult developer.
- The coaching evidence (Wooden) is observational and centered on one person.
- Some regularities widely cited in this space are methodologically contested:
  - Koedinger's learning-rate regularity.
  - Deliberate practice's share of performance variance.
  - Learning-curve-based model refinement.

## 9. Adjacent areas not searched in this pass

Named from background knowledge only [R]:

- **Spaced-repetition scheduling algorithms** (SM-2, FSRS) and their fit for skills rather than facts.
- **Data-driven hint generation for programming:** Hint Factory (Barnes & Stamper), iSnap (Price).
- **Guardrailed LLM assistants deployed in CS courses:** CodeHelp (Liffiton et al.), CodeAid (Kazemitabaar et al.), CS50's AI tools (Liu et al.).
- **Programming CS-education techniques:**
  - Parsons problems and subgoal labeling (Margulieux).
  - Research on notional machines (du Boulay; Sorva).
  - The "tracing before writing" line of work (Lister; Lopez et al.).
- **Metacognitive and help-seeking tutoring:** Aleven, Roll et al.
- **Keystroke-level and IDE telemetry datasets:** e.g. Blackbox from BlueJ.
- **Cognitive task analysis** and the difficulty experts have articulating their own knowledge.
- **Transfer of learning** across programming languages and paradigms.
- **Evaluation frameworks and benchmarks for AI tutors** beyond LearnLM's.
