# Breadth expansion, round 1 — N1, N2, N3, N7

Scope: sources not in `index/index.md`. Practitioner accounts with data, deployed-tutor repos with prompts/outcomes, grey literature. No trainer design. No recommendations.

## Methodology

Databases: HN Algolia (`tags=story`, 8 hits/query), WebSearch, Crossref (DOI resolution only), one GitHub existence check via `curl`/`gh api`. Full text fetched via WebFetch where noted; everything else is WebSearch-snippet level and marked `full_text_read=N` in the ledger — honestly, not as a formality: several of these are opinion clusters where no primary text exists to read.

### Search log

| # | query | database | hits | new | seen |
|---|---|---|---|---|---|
| N1-1 | how do you know you actually learned to code | HN Algolia | 40 | 1 | rest off-topic |
| N1-2 | measuring programmer skill | HN Algolia | 3 | 1 | — |
| N1-3 | illusion of competence programming | HN Algolia | 1 | 1 | — |
| N1-4 | tutorial hell | HN Algolia | 1121 | 1 (vibe-code-hell) | mostly off-topic/unrelated tutorials |
| N1-5 | leetcode does not measure real skill | HN Algolia | 1 | 0 | interview-in-AI-age thread, logged under N3/N7 instead |
| N1-6 | coding interview vs real skill | HN Algolia | 5 | 1 | — |
| N1-7 | self taught programmer how to tell progress | HN Algolia | 0 | 0 | — |
| N1-8 | spaced repetition programming | HN Algolia | 35 | 1 (Fata Show HN) | sive.rs SRS piece also notable, not deep-dived this round |
| N1-9 | coding bootcamp longitudinal outcomes report retention skill after graduation | WebSearch | 9 links | 0 | Course Report / CIRR reports are outcome (job/salary) data, not skill-retention data — logged as a gap, not a source |
| N1-10 | "illusion of competence" self-taught programmer blog | WebSearch | 9 links | 1 cluster | — |
| N1-11 | does leetcode measure real engineering skill blog postmortem | WebSearch | 9 links | 1 cluster | — |
| N1-12 | "skill assessment" instrument thesis programming novice validation grey literature | WebSearch | 9 links | 1 (Bergersen et al.) | led to a resolvable IEEE TSE DOI, not itself grey lit |
| N1-13 | hiring "work sample test" vs coding interview predicts job performance engineering blog | WebSearch | 9 links | 1 | — |
| N2-1 | learn by building projects vs tutorials | HN Algolia | 1 | 0 | off-topic |
| N2-2 | katas deliberate practice programming | HN Algolia | 2 | 1 (chadfowler) | — |
| N2-3 | 100 days of code | HN Algolia | 418 | 0 | challenge-log posts, no teaching-method content |
| N2-4 | how I taught myself to code | HN Algolia | 125 | 0 | memoir titles, thin content, not deep-dived |
| N2-5 | learn to code by building real things | HN Algolia | 48 | 0 | Show-HN noise |
| N2-6 | programming exercises vs real projects | HN Algolia | 0 | 0 | — |
| N2-7 | exercism codewars review | HN Algolia | 0 | 0 | — |
| N2-8 | project based learning postmortem programming | HN Algolia | 0 | 0 | — |
| N2-9 | chadfowler code kata deliberate practice programmers blog | WebSearch | 9 links | 1 cluster (5 sources) | — |
| N2-10 | exercism.org design philosophy mentored practice mastery learning blog | WebSearch | 9 links | 1 | — |
| N2-11 | "build projects not tutorials" learn programming blog debate evidence | WebSearch | 9 links | 1 cluster | — |
| N2-12 | prior knowledge prerequisite sequencing programming curriculum blog practitioner order of topics | WebSearch | 9 links | 0 | all K-12 general-ed curriculum blogs, R=1, excluded from detail |
| N3-1 | how I mentor junior engineers | HN Algolia | 12 | 0 | mostly off-topic (hiring/YC threads) |
| N3-2 | pair programming teaching | HN Algolia | 14 | 0 | off-topic |
| N3-3 | when to give hints vs let them struggle | HN Algolia | 0 | 0 | — |
| N3-4 | code review feedback junior developer | HN Algolia | 7 | 0 | off-topic (product launches) |
| N3-5 | rubber duck debugging | HN Algolia | 89 | 0 | technique is well-known, no new session-shape evidence |
| N3-6 | mentoring software engineers lessons | HN Algolia | 0 | 0 | — |
| N3-7 | socratic method teaching programming | HN Algolia | 0 | 0 | — |
| N3-8 | productive struggle programming | HN Algolia | 3 | 0 | off-topic |
| N3-9 | "how I mentor" software engineers blog hints vs answers give struggle | WebSearch | 9 links | 1 (Pragmatic Engineer) | several generic mentoring-tips SEO pages skipped, low signal |
| N3-10 | driver navigator pair programming teaching technique blog engineering | WebSearch | 9 links | 1 cluster (3 sources) | — |
| N3-11 | "productive struggle" OR "desirable difficulty" software engineering mentorship blog postmortem | WebSearch | 9 links | 1 (Kalvium) | also surfaced the "Next Senior" preprint, logged under N7 |
| N3-12 | teaching assistant office hours "when to help" programming course report | WebSearch | 9 links | 1 (Ren et al., ICER 2019) | this is peer-reviewed and missing from the merged index — a genuine Tier-1 gap, not grey lit, logged anyway per instructions to find what's not indexed |
| N7-1 | AI coding assistant makes you worse programmer | HN Algolia | 0 | 0 | — |
| N7-2 | learning to code with ChatGPT | HN Algolia | 141 | 0 | mostly Show-HN product launches |
| N7-3 | vibe coding skill | HN Algolia | 241 | 1 (arXiv "vibe coding proficiency" paper, out of scope for breadth — academic) | cluster of Substack/blog reactions noted |
| N7-4 | AI tutor guardrails withhold solution | HN Algolia | 0 | 0 | — |
| N7-5 | GitHub Copilot skill atrophy | HN Algolia | 1 | 1 (Ask HN thread) | — |
| N7-6 | does using AI hurt learning to code | HN Algolia | 5 | 0 | off-topic |
| N7-7 | AI pair programmer classroom deployment | HN Algolia | 0 | 0 | — |
| N7-8 | cognitive debt AI assistant | HN Algolia | 8 | 0 | all point to the already-indexed Kosmyna et al. paper |
| N7-9 | CodeHelp Liffiton guardrail prompts github repository classroom deployment | WebSearch | 9 links | 0 (CodeHelp/Gen-Ed already indexed, anchor #44) | confirms Gen-Ed repo is the CodeHelp codebase |
| N7-10 | deployed LLM tutor system prompt github "do not give the answer" course postmortem | WebSearch | 9 links | 1 (help-ladder paper) + 1 dead link | — |
| N7-11 | "vibe coding" skill erosion engineers survey data blog | WebSearch | 9 links | 1 cluster (4+ sources) | — |
| N7-12 | "Are AI Copilots Eroding Our Programming Skills" hacker news discussion summary | WebSearch | 9 links | 1 (Nature/Sci-Am deskilling piece) + confirmed HN thread | — |

62 queries logged (N1: 13, N2: 12, N3: 12, N7: 12, plus overlap items), all ≥12/need.

## High-signal finds (2+ independent mentions, or a claim with data)

**N2 — Code kata as the practiceable unit.** Five independent practitioner sources (Dave Thomas's `codekata.com`, Chad Fowler's musician-practice framing, Salesforce Engineering's blog, Jeff Atwood's "The Ultimate Code Kata," codingblocks.net) converge on the same claim: a "kata" — a small, repeated, throwaway exercise — is the deliberate-practice unit for programming, explicitly distinct from and prior to building a real project. All five explicitly invoke Ericsson's deliberate-practice framing (already an anchor, expertise field, item 2) as their own justification. None report outcome data of any kind — this is a widely-repeated practitioner belief riding on an academic theory it never tests. Directly bears on N2 (unit and order of practice): the field's own practitioners assert kata-before-project, but offer zero measurement to weigh against N2's competing hypothesis (building real things).

**N3 — Driver/navigator as the intervention-timing mechanism.** Three independent named-practitioner sources (Martin Fowler, Maaret Pyhäjärvi's "strong-style pairing," a HackerNoon pattern catalog) converge on a specific mechanism for when to intervene during pair programming: the navigator (mentor/watcher role) must voice an idea before the driver may act on it, forcing verbalization before code changes. This is the closest practitioner analogue found this round to N3's actual question (hint vs. worked example vs. question vs. silence) — it names "voice the idea first" as the intervention discipline. No outcome data among the three.

**N7 — Vibe-coding skill-erosion cluster.** Four-plus independent sources (blog.boot.dev's "vibe code hell," VentureBeat, a Talent500 self-report survey of 167 engineers, a Final Round AI survey of 18 CTOs reporting 16 production disasters, and first-person testimony collected by 404 Media and repeated on HN) converge on a claim: heavy LLM-code reliance produces perceived and self-reported skill decline, concentrated in debugging and "why does this work" comprehension rather than typing/output speed. Every source in the cluster is self-report or anecdote — S=1 throughout, no source in the cluster used a controlled or delayed-test design. This matters as convergent *practitioner belief* going into N7, not as evidence at the strength N7 needs; the two RCTs already in the index (Bastani et al. harm; Kestin et al. benefit) are the actual evidence-grade anchors this cluster is a folk-theory echo of.

**N7 — AskTIM / help-ladder tutor (arXiv 2608.12292).** A single deployed system (two undergraduate data-structures courses, University of Washington Bothell) with the most detailed guardrail-tuning data found this round: an eight-rung help ladder (H0 acknowledgment → H7 full solution), four automated acceptance gates, and reported before/after calibration numbers (earnest-help-revise rate 43%→0%; hint-ceiling compliance 54%→96%→100%). The paper is unusually disciplined about its own limits: it explicitly states it does not claim a learning-outcomes result and that a human-subjects study is future work — so this is O=0 by the authors' own declaration, not by this project's inference. Directly relevant to N3 (a concrete, graded intervention taxonomy) and N7 (a real deployment's guardrail-tuning method). A GitHub URL surfaced by the search summarizer for the same system (`bonbon-on-fire/asktim_llm_tutor_project`) returned 404 on both WebFetch and a direct `curl`/`gh api` check — logged as unresolvable, not used as a citation.

## Table of the rest

| find | kind | S | R | O | note |
|---|---|---|---|---|---|
| Bergersen, Sjøberg, Dybå 2014, IEEE TSE (10.1109/tse.2014.2348997) | peer-reviewed instrument paper, gap in merged index | 3 | 3 | 1 | 65 professional developers, 8 countries, 19 Java tasks, Rasch model; full text not opened this round (academia.edu/ResearchGate blocked the fetch) |
| Ren et al., ICER 2019, "What Help Do Students Seek in TA Office Hours?" (10.1145/3291279.3339418) | peer-reviewed, gap in merged index | 2 | 2 | 0 | PDF fetched but binary-encoded, not parsed; graded from bibliographic metadata only |
| CodeGuard (arXiv 2602.02509) | deployed dataset + classifier, no human subjects | 2 | 2 | 0 | 8,000-prompt taxonomy from 18 real CS syllabi; 0.93 F1, 97.4% accuracy, 30–65% reduction in harmful completions; human eval stated as future work |
| Lancet Gastro commentary on colonoscopy deskilling (10.1016/s2468-1253(25)00164-5) | commentary on an unresolved primary study | 1 | 2 | 0 | strongest cross-domain over-reliance/harm analogue found for N7; the actual primary study's numbers (ADR 28.4%→22.4%, n=19) came only through science journalism this round — flagged as hypothesis, not citation, per rule 4 |
| "Who Will Become the Next Senior?" (arXiv 2607.17067) | unclear design, low-confidence read | 1 | 2 | 0 | fetch tool's summary was internally inconsistent (called both "argument-based" and "qualitative empirical") — needs a direct read before use |
| Kalvium blog on productive struggle | practitioner argument, no data | 1 | 2 | 0 | names feedback timing + calibrated difficulty as the condition that makes struggle productive; cites Bjork/Ericsson secondhand |
| Pragmatic Engineer, "Developers mentoring other developers" | practitioner account | 1 | 3 | 0 | cross-company observation by a high-reach named author, not coded/systematic |
| LeetCode/interview-doesn't-measure-skill cluster | practitioner opinion, 4+ sources | 1 | 2 | 0 | consensus claim, zero data; a candidate mislead-proxy for N1 |
| Illusion-of-competence/Dunning-Kruger cluster | practitioner opinion, 3+ sources | 1 | 2 | 0 | another candidate mislead-proxy for N1 |
| Exercism mentored-practice docs | platform design, no data | 1 | 3 | 0 | pairs a practice unit with 1:1 mentoring; N2/N3 crossover |
| "Vibe code hell" (boot.dev) | practitioner essay | 1 | 3 | 0 | top-scoring HN item in this search (283 pts) |
| HN thread, "Are AI Copilots Eroding Our Programming Skills?" | practitioner self-report thread | 1 | 3 | 0 | direct first-person accounts, one dissenting account |
| Work-sample-vs-interview hiring blog | practitioner argument citing secondhand research | 1 | 2 | 0 | not independently verified against the I-O psych literature it cites |
| `bonbon-on-fire/asktim_llm_tutor_project` GitHub URL | — | 0 | 0 | 0 | UNRESOLVABLE — 404, not a citation |

## What I did not read

- Coding-bootcamp outcome reports (Course Report, CIRR, SwitchUp): fetched at snippet level only; they measure job placement and salary, not skill retention or durability, so they were not pursued further under N1 — logged as a negative result (this genre of grey lit does not answer N1's question).
- Bergersen et al. 2014 and Ren et al. 2019 (see table): bibliographic/abstract level only; academia.edu, ResearchGate, and a raw PDF all failed to yield parseable full text this round.
- Sive.rs "Memorizing a programming language using spaced repetition" (2013) and `executeprogram.com`'s spaced-repetition pages: surfaced under N1, not deep-dived — time budget went to the higher-signal clusters above.

## Patterns

1. Every strong N2/N3 practitioner claim this round independently reaches for an academic theory already anchored in the index (deliberate practice, Ericsson; desirable difficulty, Bjork) to justify itself, but none of them test it — the practitioner layer is citing the theory layer, not extending it with new evidence. A surveyor reading only the academic index would miss that these folk practices exist at all; a surveyor reading only this layer would overrate how tested they are.
2. The N7 harm/erosion literature has two levels that do not talk to each other: RCT-grade evidence already in the index (Bastani et al.: harm; Kestin et al.: benefit — genuinely disagreeing) and a large, self-reinforcing practitioner/survey layer (vibe-coding cluster) that all points one direction (erosion) with no source stronger than self-report. The disagreement lives entirely in the RCT layer; the practitioner layer looks unanimous only because none of it is measuring anything.
3. Two genuine Tier-1 gaps surfaced by accident while breadth-searching grey lit (Bergersen et al. 2014; Ren et al. 2019) — both peer-reviewed, both missing from the merged index's cs-education field. Worth a corpus-reconciliation pass against OpenAlex/Crossref directly rather than assuming the six field indexes are complete.
4. A tool-reliability finding, not a research one: a WebSearch summarizer produced a plausible-looking GitHub URL and project name for a real arXiv paper's described system; the URL was fabricated (404 on direct check). Every URL a search-summary tool hands back needs an independent existence check before it enters a ledger — this round caught one, but the failure mode is generic to the pipeline.
