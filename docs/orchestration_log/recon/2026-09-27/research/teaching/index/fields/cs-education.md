# Computing Education Research — Anchor Index

Fetched: 2026-09-27. Databases and queries:

| database | queries run | notes |
|---|---|---|
| OpenAlex (`api.openalex.org/works`, search + title.search) | 13 | free-text search noisy (cross-domain false hits); title.search precise. Hit shared-IP rate limit ("$0 remaining budget") after ~13 calls; retry window ~2h out, not waited for |
| Crossref (`api.crossref.org/works`, query.bibliographic + query.title + direct DOI lookups) | 26 bibliographic/title searches + 44 direct DOI verifications | primary tool for this pass once OpenAlex was exhausted |
| ERIC, arXiv, PMC | 0 | not queried — every anchor found is ACM/IEEE conference or journal literature already indexed by Crossref; no relevant preprint or K-12-education-agency hit surfaced in the searches run |

full_text_read: 0. This is the index pass (anchor-collection, metadata-level); one-liners below are drawn from title/venue/abstract-level knowledge of the works, not from fetched full text. Full-text reading is Tier 2's job (need surveys), not this field index's.

## Anchors

| # | DOI/URL | Authors, year | Title | Kind | One line |
|---|---|---|---|---|---|
| 1 | https://doi.org/10.1145/2483710.2483713 | Sorva, 2013 | Notional machines and introductory programming education | theory | Names the notional-machine construct as the thing programming instruction must make visible to learners. |
| 2 | https://doi.org/10.1080/08993401003612167 | Robins, 2010 | Learning edge momentum: a new account of outcomes in CS1 | theory | Proposes that early success/failure on connected concepts compounds, explaining bimodal CS1 outcome distributions. |
| 3 | https://doi.org/10.1145/1268784.1268845 | Caspersen, Larsen, Bennedsen, 2007 | Mental models and programming aptitude | obs | Tests a mental-model-consistency aptitude measure on a CS1 cohort; results diverge from the claim it strongly predicts success (see Disputes). |
| 4 | https://doi.org/10.1145/572133.572137 | McCracken, Almstrum, Diaz et al., 2001 | A multi-national, multi-institutional study of assessment of programming skills of first-year CS students | obs | Landmark cross-institution study finding first-year students perform far below instructor expectations on a common programming task. |
| 5 | https://doi.org/10.1145/3141880.3141895 | Ericson, Margulieux, Rick, 2017 | Solving parsons problems versus fixing and writing code | RCT | Quasi-experiment comparing Parsons-problem practice to code-writing/fixing at matched time budgets. |
| 6 | https://doi.org/10.1145/3077618 | Qian, Lehman, 2017 | Students' Misconceptions and Other Difficulties in Introductory Programming | meta | Systematic review of documented programming misconceptions and the difficulties distinct from them, across the CS-ed literature (TOCE). |
| 7 | https://doi.org/10.1145/3293881.3295779 | Luxton-Reilly, Simon, Albluwi et al., 2018 | Introductory programming: a systematic literature review | meta | ITiCSE working-group systematic review of introductory-programming research across pedagogy, tools and assessment. |
| 8 | https://doi.org/10.1109/te.2018.2864133 | Medeiros, Ramalho, Falcão, 2019 | A Systematic Literature Review on Teaching and Learning Introductory Programming in Higher Education | meta | Independent systematic review covering similar ground to #7 from an IEEE Transactions on Education angle. |
| 9 | https://doi.org/10.1145/1041624.1041673 | Lister, Adams, Fitzgerald et al., 2004 | A multi-national study of reading and tracing skills in novice programmers | obs | Multi-institution study: students who cannot trace code reliably also cannot write it; tracing precedes writing ability. |
| 10 | https://doi.org/10.1145/3341525.3387373 | Price, Hovemeyer, Rivers et al., 2020 | ProgSnap2: A Flexible Format for Programming Process Data | dataset | Defines the standard data format for fine-grained programming process/keystroke data, enabling cross-study process-data comparison. |
| 11 | https://doi.org/10.1145/2632320.2632349 | Vihavainen, Airaksinen, Watson, 2014 | A systematic review of approaches for teaching introductory programming and their influence on success | meta | ICER systematic review of pedagogical interventions and their measured effect on CS1 outcomes. |
| 12 | https://doi.org/10.1076/csed.13.2.137.14200 | Robins, Rountree, Rountree, 2003 | Learning and Teaching Programming: A Review and Discussion | meta | Widely cited early synthesis of what was then known about novice programmers' difficulties and pedagogy. |
| 13 | https://doi.org/10.1145/1404520.1404522 | Begel, Simon, 2008 | Novice software developers, all over again | obs | Follows CS graduates into their first industry jobs; documents that professional-context struggles echo CS1-level difficulties. |
| 14 | https://doi.org/10.1145/1937117.1937125 | LaToza, Myers, 2010 | Hard-to-answer questions about code | obs | Surveys professional developers on what they cannot answer from code alone, motivating tool and process design for developer learning. |
| 15 | https://doi.org/10.1017/9781108654555 | Fincher, Robins (eds.), 2019 | The Cambridge Handbook of Computing Education Research | meta | Field-defining handbook; each chapter is itself a synthesis of a CS-ed subarea (this index draws on its chapter structure, not its content). |
| 16 | https://doi.org/10.1145/2635868.2635892 | Meyer, Fritz, Murphy et al., 2014 | Software developers' perceptions of productivity | obs | Field study of what professional developers believe drives their own productivity, contrasted against logged activity. |
| 17 | https://doi.org/10.1145/1404520.1404532 | Denny, Luxton-Reilly, Simon, 2008 | Evaluating a new exam question: Parsons problems | RCT | Introduces Parsons problems as an assessment format and compares student performance against conventional exam questions. |
| 18 | https://doi.org/10.1145/2361276.2361300 | Helminen, Ihantola, Karavirta et al., 2012 | How do students solve parsons programming problems? | obs | Process-data study of the solution paths (not just outcomes) students take through Parsons problems. |
| 19 | https://doi.org/10.1145/3373165.3373187 | Du, Luxton-Reilly, Denny, 2020 | A Review of Research on Parsons Problems | meta | Systematic review of the Parsons-problem literature; reports inconsistent effect sizes across studies (see Disputes). |
| 20 | https://doi.org/10.1145/2538862.2538924 | Brown, Kölling, McCall et al., 2014 | Blackbox: A Large Scale Repository of Novice Programmers' Activity | dataset | The BlueJ Blackbox dataset: large-scale, fine-grained novice programming activity logs, an early process-data corpus predating ProgSnap2. |
| 21 | https://doi.org/10.1145/1953163.1953200 | Tew, Guzdial, 2011 | The FCS1: a language-independent assessment of CS1 knowledge | obs | Introduces and validates a CS1 knowledge assessment instrument independent of the language taught in, enabling cross-course comparison. |
| 22 | https://doi.org/10.1145/2960310.2960316 | Parker, Guzdial, Engleman, 2016 | Replication, Validation, and Use of a Language Independent CS1 Knowledge Assessment | obs | Independent replication of the FCS1 instrument (#21) across new institutions and populations. |
| 23 | https://doi.org/10.1145/3089799 | Weintrop, Wilensky, 2017 | Comparing Block-Based and Text-Based Programming in High School Computer Science Classrooms | RCT | Quasi-experimental comparison finding block-based and text-based introductions produce comparable learning outcomes, against the intuition that text is inherently harder/more "real." |
| 24 | https://doi.org/10.1145/2996201 | Umapathy, Ritzhaupt, 2017 | A Meta-Analysis of Pair-Programming in Computer Programming Courses | meta | Meta-analysis of pair-programming's effect on programming-course outcomes across the collected primary studies. |
| 25 | https://doi.org/10.1145/1089733.1089734 | Kelleher, Pausch, 2005 | Lowering the barriers to programming: a taxonomy of programming environments and languages for novice programmers | theory | Landmark ACM Computing Surveys taxonomy of novice-programming environments/languages and the barriers each targets. |
| 26 | https://doi.org/10.1145/2591708.2591749 | Watson, Li, 2014 | Failure rates in introductory programming revisited | obs | Updates the multi-institution CS1 failure-rate estimate (#28) with a larger, more recent sample; rate is stable across the intervening years. |
| 27 | https://doi.org/10.1145/1272848.1272879 | Bennedsen, Caspersen, 2007 | Failure rates in introductory programming | obs | Original multi-institution survey establishing the oft-cited ~1/3 average CS1 failure rate. |
| 28 | https://doi.org/10.1145/3231711 | Keuning, Jeuring, Heeren, 2018 | A Systematic Literature Review of Automated Feedback Generation for Programming Exercises | meta | Systematic review of automated-feedback techniques for programming exercises, directly relevant to LLM-generated feedback (N7). |
| 29 | https://doi.org/10.1109/icpc.2015.35 | Jbara, Feitelson, 2015 | How Programmers Read Regular Code: A Controlled Experiment Using Eye Tracking | RCT | Controlled eye-tracking experiment on how code regularity/structure shapes reading behavior and comprehension speed. |
| 30 | https://doi.org/10.1109/tse.1984.5010283 | Soloway, Ehrlich, 1984 | Empirical Studies of Programming Knowledge | theory | Foundational IEEE TSE paper introducing "programming plans" and "rules of discourse" as the unit of programming knowledge and expertise. |
| 31 | https://doi.org/10.2190/689t-1r2a-x4w4-29j2 | Pea, 1986 | Language-Independent Conceptual "Bugs" in Novice Programming | theory | Argues many novice programming errors reflect misconceptions about the notional machine, not syntax, and recur across languages. |
| 32 | https://doi.org/10.2190/3lfx-9rrf-67t8-uvk9 | du Boulay, 1986 | Some Difficulties of Learning to Program | theory | Foundational taxonomy of what makes learning to program hard: notional machine, notation, structures, pragmatics, schemas. |
| 33 | https://doi.org/10.1145/1140123.1140157 | Lister, Simon, Thompson et al., 2006 | Not seeing the forest for the trees | obs | Applies the SOLO taxonomy to novice code-reading/abstraction responses across multiple institutions. |
| 34 | https://doi.org/10.1145/2999541.2999554 | Ahadi, Hellas, Ihantola et al., 2016 | Replication in computing education research | theory | Methodology paper surveying how rarely CS-ed findings are independently replicated and what that means for the field's evidence base. |
| 35 | https://doi.org/10.1145/3639475.3640107 | Liebel, Langlois, Gama, 2024 | Challenges, Strengths, and Strategies of Software Engineers with ADHD: A Case Study | obs | Interview-based case study of professional software engineers with ADHD: reported task-switching costs, hyperfocus as an asset, and coping strategies. |
| 36 | https://doi.org/10.1109/ase63991.2025.00342 | Shah, Magalhães, Gama et al., 2025 | Tether: A Personalized Support Assistant for Software Engineers with ADHD | obs | Designs and evaluates a support tool for ADHD software engineers targeting the attention/task-switching problems documented in #35. |
| 37 | https://doi.org/10.5220/0014584600004021 | Jiang, Düdder, 2026 | A Trait-Based Prioritization Framework: Teaching Practices to Support Neurodivergent Learners in Computer Science Education | theory | Proposes a framework for prioritizing which teaching-practice adaptations to make for neurodivergent CS learners, including attention differences. |

### Venues (no DOI; the field's recurring publication and community anchors)

| # | URL | Venue | Kind | One line |
|---|---|---|---|---|
| V1 | https://sigcse.org/ | SIGCSE Technical Symposium (ACM) | venue | The largest annual CS-ed conference; most anchors above (#4, #9, #13, #17, #20, #21, #26–27, #33) appear here or its Bulletin. |
| V2 | https://icer.acm.org/ | ICER — International Computing Education Research conference (ACM) | venue | The field's flagship research-first (vs. teaching-practice-first) conference; anchors #11, #18, #22 appear here. |
| V3 | https://iticse.acm.org/ | ITiCSE — Innovation and Technology in Computer Science Education (ACM) | venue | European-rooted sister conference to SIGCSE; source of the ITiCSE working-group reports (#4, #7, #9). |
| V4 | https://www.kolicalling.fi/ | Koli Calling International Conference on Computing Education Research | venue | Smaller, methodologically rigorous Nordic-rooted conference; source of #5, #34. |
| V5 | https://dl.acm.org/journal/toce | ACM Transactions on Computing Education (TOCE) | venue | The field's dedicated archival journal; source of #1, #6, #23, #24, #28. |

## Disputes

- **Aptitude-by-mental-model-consistency, unsettled.** Bornat's PPIG 2006/2008 claim that a pre-course "mental model consistency" test bimodally predicts CS1 success (the informally circulated "camel has two humps" line of work) has no resolvable DOI — it exists as an ACM DL identifier (`10.5555/1379249.1379253`) that Crossref does not carry, so it does not enter this index as a citation (rule 4). The nearest resolvable, closely related study, #3 (Caspersen, Larsen, Bennedsen 2007), tested a similar mental-model-consistency measure independently and reports results that do not confirm a strong, clean predictive split — an unresolved and only partly citable dispute.
- **Parsons problems: effective, but not uniformly.** #5 and #17 report measurable learning/assessment benefits from Parsons problems in their specific study designs; #19, the field's own systematic review of the same literature, reports the effect sizes across studies are inconsistent and moderated by problem design (e.g., "faded" vs. full Parsons problems) — the practice is well-evidenced in aggregate but not as a uniform effect.
- **Block-based vs. text-based programming, contested intuition.** The common assumption that block-based environments are a lesser stepping-stone and text-based is the "real" skill being deferred is not supported by #23's quasi-experimental comparison, which found comparable learning outcomes — a case where a course-design intuition and the measured evidence diverge.

## Statistics

- Total anchors: 37 papers + 5 venues = 42 rows.
- By kind: theory 8, obs 13, RCT 5, meta 9, dataset 2, venue 5.
- By decade: 1980s 3, 2000s 8, 2010s 20, 2020s 6.
- Databases queried: OpenAlex (13 calls, then rate-limited off a shared-IP daily budget — not this account's own key), Crossref (26 search queries + 44 direct DOI verifications). ERIC, arXiv, PMC: 0 calls — no anchor in this field required them.
- DOI resolution: 37/37 anchor papers resolved via Crossref (each fetched and its authors/year/title/container verified individually, not trusted from search-snippet text). 1 known landmark work (Bornat's "camel has two humps") explicitly excluded as unresolvable per rule 4, noted above rather than silently dropped.
- full_text_read: 0/37 — this is the anchor-index pass; full-text engagement is Tier 2's job.
