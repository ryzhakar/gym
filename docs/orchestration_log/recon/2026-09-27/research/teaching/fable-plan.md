# Teaching research — plan under research-tree

Planner: agent:teaching-fable (Fable 5.1), 2026-09-27. Plan only; nothing here has run. Bound: stop-yapping, first-principles, cargo-cult-science, simple-made-easy.

Inputs read in full: research-tree SKILL.md (4.3.1); events.md 2026-09-26 lines 98–123 and 129–130 (the owner's rulings for this research; 118 is intake calibration; 100–101 record the rejected Rust framing); user_deferred_items.md lines 5–9; seed.md. Nothing else under recon/ read. The owner takes no further questions: the research launches from this plan; §8 holds defaults, not questions.

Root for every output path below: `/Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27/research/teaching/` — written `ROOT/` from here on.

---

## 0. What binds this plan

Owner rulings, by events line (history/2026-09-26/events.md):

| line | ruling | consequence for the plan |
|---|---|---|
| 103 | scope: anyone learning CS-adjacent skills | population, not one learner; not one subject |
| 104 | learned = done unaided, lasting | outcome measure is fixed; assisted success, self-report, felt learning are proxies |
| 105 | LLM strengths: always there, endless tailored practice, watching the work, answering anything; teaching-specific edge is for research to discover | N7 exists; edge is a research output, not an assumption |
| 106 | seed strands 1, 2 owner's ideas; strand 3 peer claim | strands 1, 2 are questions (N5, N3); strand 3 is a claim to test, not a frame |
| 108 | deliverable: evidence map + how it transfers onto an LLM substrate; not a design | synthesis writes claims with grades, never a trainer design |
| 109 | single best = Pareto set loosely calibrated to owner | no single winner; a set positioned on four axes |
| 110 | every evidence kind counts, weighed by strength and by relevance to its subdomain | two-dimensional grading, §4 |
| 111 | fields: education research, elite coaching, expertise research, AI tutoring, anything else except snake-oil | six index fields, §2 T1; exclusion register, §4 |
| 113 | Pareto axes: skill per hour, how long it lasts, transfer, sustainability | every claim tagged with the axes it speaks to |
| 114 | calibration: intake interview before research (done, lines 117–119) + early measurement in training; records not a source | N1 supplies the early measurement; agents never read history/ for learner traits |
| 115 | toward daily; irregular bursts now | N6 |
| 116 | done at saturation | §5 |
| 118 | intake (calibration, not a ruling): senior engineer; skills built by building real things and through people; stalls from interruptions and being stuck too long; hyperfocus-and-breadth attention | calibration data only, quarantined to the map's calibration section; never an input to T1–T4 |
| 120 | trainer for most everyone, adapts; owner traits must not shape the product much; CS-specific ways to channel hyperfocus-and-breadth attention: research asks | generalizability gate; one sub-question in N6 |
| 121 | feedback to owner: blunt, terse, clear | style is calibration, out of research; feedback content and timing are in (N3) |
| 122 | watching: continuous + learner calls attention to a spot | N3 intervention policy under continuous observation |
| 123 | generalizability required | population tag on every claim |
| 129–130 | time to first training first-class | §7 staging: Stage A ships before saturation |

Lines 100–101: the owner rejected a Rust-framed interview ("your framing is rust-primed, again. start again."). Every prompt below carries a subject-neutrality rule; no subject file is an input anywhere.

---

## 1. Setup

### Research surface

No single index exists. Surface = five literatures plus practitioner sources, entered through bibliographic APIs and built into an index by Tier 1:

| class | entry point | checked 2026-09-27 |
|---|---|---|
| bibliographic metadata, citations | `https://api.openalex.org/works` | reachable, JSON |
| bibliographic, influential-citation counts | `https://api.semanticscholar.org/graph/v1/paper/{DOI}` | reachable per-DOI; search endpoint 429 — use OpenAlex for search |
| education literature | `https://api.ies.ed.gov/eric/?search=…&format=json` | reachable |
| DOI resolution, retraction records | `https://api.crossref.org/works` (`filter=update-type:retraction`, `update-to` field) | reachable |
| open-access full text by DOI | `https://api.unpaywall.org/v2/{DOI}?email=…` | reachable, returns PDF URL |
| preprints | `https://export.arxiv.org/api/query`; `https://api.osf.io/v2/preprints/?filter[provider]=edarxiv` | reachable |
| biomedical/psychology full text | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/` (db=pmc) | reachable |
| curated evidence syntheses | What Works Clearinghouse `https://ies.ed.gov/ncee/wwc/` | reachable; EEF toolkit 403 to fetch tool — use WebSearch snippets or skip |
| practitioner accounts | HN Algolia `https://hn.algolia.com/api/v1/search`; blogs; coach memoirs via WebSearch | reachable |
| deployed tutor systems (source code, prompts) | GitHub, e.g. `https://github.com/liffiton/Gen-Ed` (CodeHelp) | reachable |
| paywalled | ACM DL 403 to fetch tool | route via Unpaywall / arXiv / author PDFs; else mark UNREACHABLE |

### Research question, in the owner's terms

Deferred item, verbatim: "the single best way of teaching in general and on a specific subject that plays to the projects strengths (LLMs) and users strengths (curiosity) to supercharge the project beyond what any amount of human-teachers schooling could ever achieve."

Bound by rulings 104, 109, 113:

> Across everything known about teaching, coaching, expertise and AI tutoring, which methods produce skill that is done unaided and lasts — positioned on skill per hour, durability, transfer, sustainability — and which of them hold, fail, or gain when the trainer is an LLM that is always there, watches the work continuously, and can generate endless tailored practice?

Sub-questions, one per need-category (§3).

### Project context files agents receive

- `ROOT/context/rulings-brief.md` — Tier 0 output: rulings as facts, no learner traits beyond ruling 120's attention question
- `ROOT/context/substrate-audit.md` — Tier 0 output: what a trainer agent on this substrate can actually do
- Never: `docs/orchestration_log/history/**` (ruling 114), `ROOT/seed.md` (anchoring, §2 T3), `docs/subjects/**` (subject priming, failure 101), any other plan under recon/

---

## 2. Tiers

All six tiers run. Reason: findings become load-bearing for every trainer gym builds (Truth 2: consequence high); the seed shows abstract-level reading yields contested numbers (Tier 3 required); fields disagree by design — worked examples vs productive failure, deliberate practice's share (Tier 4 required); saturation is ruled (Tier 2 iterates).

Directory:

```
ROOT/
├── context/          T0
├── index/            T1  fields/*.md, index.md, exclusion-register.md
├── ledger/           sources.csv, claims.csv (data, appended by agents, audited by script)
├── needs/            T2  n1…n7 per round: n{k}-r{round}.md; breadth-r{round}.md
├── verify/           T3  claims/{claim-id}.md; seed-probe.md; calibration-set.md
├── resolve/          T4  {topic}-resolution.md
├── audit/            saturation-r{round}.md
└── synthesis/        T5  first-protocol.md (Stage A), evidence-map.md (Stage B), evidence-map-v{n}.md (Stage C)
```

Ledger schemas (CSV, one row per source / claim; agents append, never edit):

- `sources.csv`: `doi_or_url | title | year | venue | design | n | population | delay_to_test | fields | needs | S | R | O | flags | found_by_agent | round | full_text_read (Y/N)`
- `claims.csv`: `claim_id | need | claim_text | source_doi | quote_location | S | R | O | axes | status (SURVEYED/VERIFIED/REFUTED/UNVERIFIABLE) | verified_by`

### Tier 0 — Ground truth (3 agents, parallel with T1)

| id | job (one artifact) | model | inputs | output | depends on |
|---|---|---|---|---|---|
| t0-rulings | rulings lines 98–123 and 129–130 (skip 118, 124–128) + deferred item lines 5–9 → facts brief: population, outcome definition, axes, fields, exclusions, watching, schedule reality, attention sub-question. No learner traits except as line 120 phrases them. | haiku | `/Users/ryzhakar/pp/gym/docs/orchestration_log/history/2026-09-26/events.md` (lines 98–123, 129–130 only), `/Users/ryzhakar/pp/gym/docs/user_deferred_items.md` (lines 5–9) | `ROOT/context/rulings-brief.md` | — |
| t0-substrate | what a trainer subagent on this substrate can do, from docs not memory: file-change hooks, cron, subagent spawning, tool access, session persistence, context limits. Each capability: source URL, quote. | claude-code-guide agent (its own model) | Claude Code docs; `/Users/ryzhakar/pp/gym/CLAUDE.md` for the orchestrator/trainer split | `ROOT/context/substrate-audit.md` | — |
| t0-seed-facts | seed.md → citation list only: author, year, title, DOI/URL, seed's read-level tag ([F]/[A]/[S]/[R]), which strand/section. Strip every hypothesis, number and interpretation. | haiku | `ROOT/seed.md` | `ROOT/context/seed-citations.csv` | — |

Gate: three files exist; rulings-brief cites a line number per fact; substrate-audit has ≥1 URL per capability; seed-citations has one row per citation in seed.md (count stated).

### Tier 1 — Index (7 agents, parallel)

Builds the map research-tree assumes exists. One agent per field; each writes anchor works: systematic reviews, meta-analyses, handbooks, landmark studies, active labs, key datasets, venues. Fields from ruling 111 plus two the population forces (adult professional skill acquisition; CS education):

| id | field | model | inputs | output | depends on |
|---|---|---|---|---|---|
| t1-edu | education research + cognitive psychology of learning (retrieval, spacing, feedback, worked examples, cognitive load, self-regulation) | haiku | OpenAlex, ERIC, WWC, Crossref | `ROOT/index/fields/education.md` | — |
| t1-cs-ed | computing education research (SIGCSE/ICER/ITiCSE/Koli, notional machines, tracing, Parsons, misconceptions, process data, attention/ADHD in CS learners) | haiku | OpenAlex, arXiv, ERIC | `ROOT/index/fields/cs-education.md` | — |
| t1-expertise | expertise research (deliberate practice and its critics, skill acquisition theory, transfer, retention curves) | haiku | OpenAlex, PMC, Crossref | `ROOT/index/fields/expertise.md` | — |
| t1-coaching | elite coaching: coded observations of coaches, coach-behaviour literature (sport science), music pedagogy, surgical coaching, expert-tutor studies | haiku | OpenAlex, PMC, WebSearch | `ROOT/index/fields/coaching.md` | — |
| t1-ai-tutor | AI tutoring: ITS effect sizes, LLM tutors (RCTs, field deployments), guardrailed CS assistants with source, tutor benchmarks, harm studies | haiku | OpenAlex, arXiv, GitHub, WebSearch | `ROOT/index/fields/ai-tutoring.md` | — |
| t1-adult | adult professional skill acquisition: medical education, simulation training, aviation, workplace learning, self-directed adult learning | haiku | OpenAlex, PMC, ERIC | `ROOT/index/fields/adult-skill.md` | — |
| t1-exclusion | exclusion register: retracted works in these fields (Crossref retraction filter × field keywords), refuted claims per ≥2 systematic reviews (neuromyths etc.), commercial claims without third-party evaluation | haiku | Crossref, OpenAlex | `ROOT/index/exclusion-register.md` | — |

Then one merge:

| id | job | model | inputs | output | depends on |
|---|---|---|---|---|---|
| t1-merge | dedupe by DOI, assign fields, write `index.md` with statistics; seed each anchor into `ledger/sources.csv` with S/R/O blank | haiku | `ROOT/index/fields/*.md` | `ROOT/index/index.md`, `ROOT/ledger/sources.csv` | t1-* |

Gate: every entry has DOI-or-URL resolved (Crossref/OpenAlex hit pasted), year, one line, field; statistics section; ≥25 anchors per field or a stated reason; exclusion register has ≥1 checkable criterion per entry. Orchestrator reads statistics only.

### Tier 2 — Survey by need (7 need surveyors + 2 breadth expanders per round)

Round 1 = Stage A needs N1, N2, N3, N7 (4 surveyors + 1 breadth). Round 2 = N4, N5, N6 (3 + 1). Rounds ≥3 = saturation rounds, all needs, fresh agents, §5.

| id | need | model | inputs | output | depends on |
|---|---|---|---|---|---|
| t2-n{k}-r{r} | one need, §3 | sonnet | `ROOT/index/index.md` (its field sections named), `ROOT/context/rulings-brief.md`, `ROOT/context/substrate-audit.md` (N3, N7 only), `ROOT/index/exclusion-register.md`, `ROOT/verify/calibration-set.md` (rounds ≥2) | `ROOT/needs/n{k}-r{r}.md` + rows appended to both ledgers | t1-merge, t0-* |
| t2-breadth-r{r} | sources not in the index: practitioner accounts (HN, blogs, coach memoirs, course post-mortems), deployed-tutor repos, grey literature | haiku | `ROOT/index/index.md`, query list per need | `ROOT/needs/breadth-r{r}.md` + ledger rows | t1-merge |

Gate: per need, ≥10 claims in claims.csv each with source DOI, quote location, S/R/O, axes; every source touched has a sources.csv row with `full_text_read` filled honestly; search log with queries, database, hit counts, new-vs-seen; per-axis section (skill/hour, durability, transfer, sustainability) each holding claims or "no evidence found, queries: …".

Calibration set (grading drift control): t2 round 1 also grades 5 shared sources named by the orchestrator (one per S band, chosen from index.md by t1-merge as `ROOT/verify/calibration-set.md` stub); disagreements >1 band go to Tier 4.

### Tier 3 — Verify (per load-bearing claim; plus seed probe)

Triggers: every claim the Stage A brief or Stage B map will rest on (synthesizer names them before writing — see §7 order); any claim with S≥3 whose survey row says `full_text_read=N`; any claim contradicting another ledger row; any effect > 1.0 SD from one study; every extraordinary claim in completion summaries.

| id | job | model | inputs | output | depends on |
|---|---|---|---|---|---|
| t3-claim-{id} | fetch full text (Unpaywall → PDF; arXiv; PMC); quote the sentence/table carrying the number; confirm design, n, population, outcome instrument, delay-to-test; Crossref retraction check; replication search (OpenAlex citing works + "replication"); set status VERIFIED/REFUTED/UNVERIFIABLE with quote | sonnet | claim row from `ROOT/ledger/claims.csv`, the source; nothing from needs/*.md beyond that row | `ROOT/verify/claims/{claim-id}.md` + claims.csv status update | t2 |
| t3-seed-probe | for each seed citation: (a) found independently by t2 (DOI in sources.csv)? (b) primary-source check of the number seed reports; (c) seed strand-3 claims (KC modeling) checked as claims. Output = coverage fraction + per-citation verdict. Reads seed.md only after t2 round 2 closes. | sonnet | `ROOT/context/seed-citations.csv`, `ROOT/seed.md`, `ROOT/ledger/sources.csv` | `ROOT/verify/seed-probe.md` | t2 round 2 |
| t3-substrate-{cap} | for N7 claims that depend on a substrate capability (file watching, cron, context limits): test it — a hook that fires on write, a cron that fires — and record the transcript | sonnet | `ROOT/context/substrate-audit.md` | `ROOT/verify/substrate-{cap}.md` | t0-substrate |

Gate: each report quotes primary text with page/section; status set; `full_text_read=Y` or UNVERIFIABLE with the reason (paywall URL, 404).

### Tier 4 — Resolve (0–n)

Detection by script over claims.csv: same source with differing S/R/O by >1 band; opposite-direction claims under one need; calibration-set disagreements; seed-probe REFUTED where a survey said VERIFIED.

| id | job | model | output | depends on |
|---|---|---|---|---|
| t4-{topic} | research-tree contradiction resolver, adapted: primary text of both sources, moderators named (population, prior knowledge, outcome delay, fidelity), verdict; known standing disputes (worked examples vs productive failure; deliberate practice variance; learning-rate regularity) get one resolver each, framed as "what moderates" not "who wins" | opus | `ROOT/resolve/{topic}-resolution.md` | t3 |

### Tier 5 — Synthesize (three deliverables across stages)

| id | job | model | inputs | output | depends on |
|---|---|---|---|---|---|
| t5-first-protocol | Stage A brief: for N1, N2, N3, N7, the VERIFIED claims (S≥2, O≥1), what the first sessions do because of each, the unaided delayed probe N1 supplies, expiry line | fable | `ROOT/context/*`, `ROOT/needs/n{1,2,3,7}-r1.md`, `ROOT/verify/claims/*.md` (Stage A set), `ROOT/ledger/*.csv` | `ROOT/synthesis/first-protocol.md` | t3 Stage A set |
| t5-evidence-map | Stage B map: all needs; every claim with S/R/O, axes, population, status; Pareto positioning; transfer-to-LLM section per need; gaps; confidence; owner calibration section reading rulings 118–121 only here | fable | every file under ROOT except seed.md | `ROOT/synthesis/evidence-map.md` | t4 |
| t5-map-v{n} | Stage C: re-synthesis after each saturation round that changed any VERIFIED claim | fable | as above + `ROOT/audit/*` | `ROOT/synthesis/evidence-map-v{n}.md` | audit round n |

Gate (from research-tree, adapted): executive answer to the question; per-need claim tables citing `verify/claims/*.md`; four-axis Pareto table; LLM-transfer section; coverage gaps; confidence table; forbidden: any section that designs the trainer (ruling 108) — reviewer greps for "the trainer should" and rejects.

---

## 3. Need-categories

Derived from the rulings (§0), not from any field's taxonomy. Each is one decision the trainer's builder must make; each names the rulings that force it and the axes it serves.

| id | need (the decision) | forced by | axes | Stage |
|---|---|---|---|---|
| N1 | **Measure.** How to tell that a skill is done unaided and lasts; what instrument, at what delay, at what cost in session time; what proxies mislead (assisted success, felt learning, self-report, tutor impression) | 104, 113, 114 (early measurement) | all four — the axes are unmeasurable without it | A |
| N2 | **Unit and order of practice.** What the practiceable unit of a CS-adjacent skill is; how units are sequenced; where building real things sits relative to drills; how much prior knowledge each method presumes | 103, 113 (skill/hour, transfer), 118 (building real things, quarantined as a hypothesis) | skill/hour, transfer | A |
| N3 | **Session shape and intervention.** Under continuous watching plus a learner's call: when to intervene, with what (hint, worked case, question, silence), how much struggle, feedback content and timing | 122, 106 (strand 2), 121 (content only) | skill/hour, durability | A |
| N4 | **Diagnosis.** How the trainer learns what the learner actually holds: misconception elicitation, probes, process signals from the work, calibration of the learner's confidence; accuracy limits of human and LLM tutors at this | 105 (watching the work), 104 | skill/hour, transfer | B |
| N5 | **Elite margin.** What observed elite coaches and expert tutors do that good ones do not; which of it is documented with data; which is portable to text-mediated adult skill training | 106 (strand 1), 105 (edge to discover), deferred item ("beyond human-teachers schooling") | all four | B |
| N6 | **Sustain.** Scheduling under irregular bursts toward daily; re-entry after interruption; curiosity/interest as a driver; whether established CS-specific ways channel hyperfocus-and-breadth attention — for a population, not one learner | 115, 118 (stalls), 120, deferred item ("curiosity") | sustainability, durability | B |
| N7 | **LLM transfer.** Which findings from N1–N6 hold, fail, or gain when the trainer is an LLM: harm evidence, guardrail designs with outcomes, always-on availability, generated practice, watching files; what the substrate can actually do | 105, 108 | all four | A (initial), re-run after B |

N7 in Stage A reads only its own field (AI tutoring) plus substrate-audit; after Stage B it re-runs as a lens over N1–N6 claims (t2-n7-r2).

Not a need: trainer architecture, core/pack splits, modes, hint ladders. Seed strand 3 and seed §6 hypotheses are design; they enter only where they make checkable empirical claims (KC modeling → N2; struggle metrics → N4).

---

## 4. Evidence grading

Ruling 110: every kind counts, weighed by strength and by relevance. Three dimensions, never collapsed to one number (collapsing complects them; synthesis reads the triple).

**S — strength of the evidence as evidence**

| S | criterion |
|---|---|
| 4 | meta-analysis or systematic review reporting heterogeneity and moderators; or preregistered RCT with an independent replication |
| 3 | single RCT or quasi-experiment with a control; or large-N observational dataset with stated model |
| 2 | systematic observation with coding (coded coaching sessions, tutoring-dialogue analyses), case series with data, learning-analytics on one system |
| 1 | practitioner account, expert opinion, theory paper, product white paper, memoir |
| 0 | excluded (register below) |

**R — relevance to the subdomain (ruling 103's population)**

| R | criterion |
|---|---|
| 3 | adults acquiring CS-adjacent or comparable professional hard skills, self-directed or coached one-to-one |
| 2 | adults in other skill domains (music, surgery, sport, language), or CS learners in courses |
| 1 | K-12, or lab tasks with no skill outcome |
| 0 | not applicable to skill acquisition |

**O — outcome match (ruling 104)**

| O | criterion |
|---|---|
| 2 | unaided performance measured ≥7 days after practice, or transfer task |
| 1 | unaided performance immediately after |
| 0 | assisted performance, self-report, satisfaction, time-on-task only |

Rules: a claim carries the triple of its best source and lists the rest; every survey row records all three; a claim with O=0 never enters a recommendation set, whatever S; practitioner accounts (S1) enter the map as S1 and are reported, never silently dropped — ruling 110. The synthesizer states, per claim, which sources it rested on.

**Snake-oil exclusion (S0), operational.** A source is S0 when any holds; the register lists the check and its evidence:

1. Retracted or under expression of concern — Crossref `update-to` / `update-type:retraction` hit.
2. Efficacy claimed with a commercial interest and no third-party evaluation locatable by OpenAlex citing-works search.
3. No primary data and no citation to any — nothing to verify.
4. Central mechanism refuted by ≥2 independent S4 reviews (learning-styles matching, left/right brain, brain training for transfer); the register names the reviews.

Flags, not exclusion (recorded in `flags`): effect >1.0 SD from one study; preprint only; venue not indexed by OpenAlex/Crossref; author sells the intervention; sample n<30; abstract-only read.

---

## 5. Saturation

Ruling 116: done at saturation. A rule agents cannot meet by laziness: it is computed from ledger data by a script, never asserted.

**Per-need stopping rule.** Need N is saturated when all hold:

1. **Two independent rounds, zero new strong sources.** Two consecutive rounds by different agents, each with a distinct query set (≥12 queries, ≥3 databases, listed in the search log) find zero sources with S≥3 not already in `sources.csv` for N, and ≤1 with S=2.
2. **Capture–recapture bound.** Across the two most recent rounds, Lincoln–Petersen on DOIs: n1 = round r sources for N, n2 = round r+1, m = overlap; N̂ = n1·n2/m; unseen fraction = 1 − |seen|/N̂ ≤ 10% for S≥2 sources. (Threshold: §8 point 1.)
3. **Seed coverage.** ≥80% of seed citations tagged to N with S≥2 were found independently (seed-probe.md). Below that, coverage failed regardless of 1–2.
4. **Ledger closure.** Every claim for N is VERIFIED, REFUTED or UNVERIFIABLE-with-reason; none SURVEYED.
5. **Axis closure.** Each of the four axes has ≥1 VERIFIED claim or a "no evidence" entry with its queries.

**Void rounds.** A round is void — does not count toward rule 1 — if its search log lacks queries, databases or hit counts; if it reused >30% of a prior round's queries; if it skipped a database the need's field list names; if any source row lacks S/R/O. Void rounds are re-run by a fresh agent.

**Audit.** `audit/saturation-r{round}.md` produced by a uv Python script (conventions: python-via-uv) over `ledger/*.csv` and the search logs — orchestrator writes it before Stage B; haiku agent as fallback that must show its arithmetic. Report per need: rounds, new-vs-seen counts, N̂, unseen %, seed coverage, claim statuses, axis closure, verdict SATURATED / OPEN / VOID-ROUND. The owner can recompute every number from the CSV.

**Time cap.** Saturation gates Stage C only. At the cap (§8 point 2: three rounds) the map ships with the audit table as its confidence section — gaps visible, not hidden.

---

## 6. Prompt skeletons

Common blocks, pasted into every prompt:

```
PRINCIPLES
1. Primary sources only count. Fetch the paper (Unpaywall → PDF, arXiv, PMC). An abstract, a press
   release, a blog summary of a study, a citation in another paper: hypotheses until the text is read.
   Record full_text_read honestly.
2. Search beyond the index. OpenAlex, ERIC, Crossref, arXiv, PMC, OSF, HN Algolia, WebSearch. Log every query,
   database and hit count.
3. Evidence, not conclusions. Quote the sentence or table with page/section. Design, n, population, outcome
   instrument, delay-to-test. No recommendations. No trainer design.
4. Every citation is resolved before it enters the ledger: paste the Crossref/OpenAlex response line.
   An unresolvable citation is not a citation.
5. Subject-neutral. No programming language, framework or tool names as the frame. A study about
   language X is evidence about "learning X"; write it so. (Failure 101.)
6. Population-tagged. Every claim names who it was measured on. K-12 ≠ adults ≠ professionals.

DO NOT: trust an abstract's number; conflate similarly named studies (check DOI); read seed.md or
history/; write "the trainer should"; grade by the venue's prestige; stop at the index.

GRADING (paste §4 tables S, R, O verbatim)

LEDGER APPEND FORMAT (paste the two CSV headers verbatim)
```

### t0-rulings (haiku; Read, Write)

```
Read {events.md} lines 98–123 and 129–130, and {user_deferred_items.md} lines 5–9 only. Skip line 118 (intake
calibration) and 124–128 (plan logistics). Write ROOT/context/rulings-brief.md: one fact per line,
`line N: <fact>`. Sections: population; outcome definition; Pareto axes; fields and exclusions; deliverable;
watching; schedule reality; calibration rule; attention sub-question (line 120's wording only). Add one line:
"Subject-neutral: lines 100–101 — a Rust-framed round was rejected." No interpretation. No other file.
```

### t1-field (haiku; WebFetch, WebSearch, Write)

```
You are indexing the field "{FIELD}" for a research project on teaching toward lasting unaided skill.
{PRINCIPLES}
TASK: via OpenAlex (search + cited_by_count sort), ERIC, Crossref, arXiv, PMC, find anchor works: systematic
reviews, meta-analyses, handbooks, landmark studies, replications and their critics, key datasets, active labs,
venues. Minimum 25 or state why fewer. Write ROOT/index/fields/{field}.md:

# {FIELD} — Anchor Index
Fetched: {date}. Databases and queries: (table)
## Anchors
| # | DOI/URL | Authors, year | Title | Kind (meta/RCT/obs/theory/dataset/venue) | One line |
## Disputes (pairs of anchors that disagree, one line each)
## Statistics: total; by kind; queries run
```

### t2-need surveyor (sonnet; Read, WebFetch, WebSearch, Write)

```
You are surveying need {Nk}: "{NEED_DECISION}" — the sub-question: {SUB_QUESTION}.
CONTEXT: ROOT/context/rulings-brief.md (read first), ROOT/context/substrate-audit.md {if N3/N7}.
{PRINCIPLES} {GRADING} {LEDGER FORMAT}
INPUTS: ROOT/index/index.md sections {FIELD SECTIONS}; ROOT/index/exclusion-register.md;
ROOT/verify/calibration-set.md (grade its 5 sources first, record grades in your report).
TASK: (1) read index entries for this need; (2) search beyond it, ≥12 queries, ≥3 databases, log all;
(3) for each source: fetch full text, extract design/n/population/instrument/delay, grade S/R/O, tag axes,
append sources.csv; (4) write ≥10 claims as claims.csv rows with quote locations, status SURVEYED;
(5) write ROOT/needs/n{k}-r{r}.md:

# {Nk} — Survey round {r}
## Search log (query | database | hits | new | seen)
## Calibration grades (5 rows)
## Claims by axis
### Skill per hour / ### Durability / ### Transfer / ### Sustainability
| claim_id | claim | best source DOI | design, n, population, delay | S | R | O | quote (≤25 words, location) | status |
(each axis: rows, or "No evidence found. Queries: …")
## Disagreements between sources (pairs, one line)
## Excluded (source | S0 criterion | evidence)
## What I did not read (source | reason: paywall URL / 404 / time)
Scope: only {Nk}. A finding for another need: one line under "## Out of scope, seen", nothing more.
```

### t2-breadth (haiku; WebFetch, WebSearch, Write)

```
Find sources NOT in ROOT/index/index.md: practitioner accounts (HN Algolia, blogs, memoirs of coaches/teachers,
course post-mortems), deployed tutor repositories with prompts, grey literature. Queries: {LIST per need}.
{PRINCIPLES} {LEDGER FORMAT} Grade every find S=1 or S=2 per §4; R and O as measured.
Write ROOT/needs/breadth-r{r}.md: methodology; high-signal finds (2+ independent mentions OR a claim with data);
table of the rest; patterns. Append sources.csv.
```

### t3-claim verifier (sonnet; Read, WebFetch, Write)

```
VERIFY claim {claim_id}: "{CLAIM_TEXT}" attributed to {DOI}. Do NOT read ROOT/needs/. Do NOT trust the claim.
{PRINCIPLES}
1. Resolve DOI (Crossref). Retraction check: api.crossref.org/works/{DOI} → update-to / relation.
2. Full text: Unpaywall → PDF; else arXiv/PMC/author page. UNREACHABLE if none, with URLs tried.
3. Quote the exact sentence/table carrying the number. Confirm design, n, population, instrument, delay.
4. Replications and critics: OpenAlex cited_by with "replication"/"reanalysis"/"comment"; list DOIs.
5. Re-grade S/R/O from the text.
Write ROOT/verify/claims/{claim_id}.md:
# {claim_id} — Verification
## Claim as surveyed / ## Primary text (quote, location) / ## Design facts (table) / ## Retraction check
## Replications & critics / ## Grade (S R O, changed from survey? why) / ## Status: VERIFIED | REFUTED | UNVERIFIABLE
Then update the claims.csv row status and verified_by.
```

### t3-seed-probe (sonnet; Read, WebFetch, Write) — launches after t2 round 2 closes

```
ROOT/context/seed-citations.csv lists citations from a peer-written seed. For each: (a) in ROOT/ledger/sources.csv
by DOI? (b) fetch primary text; does the seed's number/claim (read it now from ROOT/seed.md at the cited line)
match? (c) grade S/R/O. Seed hypotheses are not claims; skip them unless they cite data.
Write ROOT/verify/seed-probe.md: coverage per need (found/total S≥2); per-citation table
(seed line | DOI | found independently Y/N | seed claim | primary text says | verdict); list of seed claims
the surveys never touched.
```

### t4-resolver (opus; Read, WebFetch, Write)

Research-tree template, with: "Frame the verdict as moderators (population, prior knowledge, outcome delay, fidelity of implementation) when both sources are S≥3. 'Both right under different conditions' is a verdict; state the conditions with quotes." Output `ROOT/resolve/{topic}-resolution.md` in the template's format plus `## Impact on claims` naming claim_ids and their new status.

### t5-first-protocol (fable; Read, Write)

```
Write ROOT/synthesis/first-protocol.md from files only: ROOT/context/*, ROOT/needs/n{1,2,3,7}-r1.md,
ROOT/verify/claims/*.md, ROOT/ledger/*.csv. Nothing from your own knowledge.
Include only claims with status VERIFIED, S≥2, O≥1. Not a design (ruling 108): each section says what the
evidence supports and what the first sessions therefore do, as a checklist the owner can act on and check.

# First training protocol — provisional, expires on evidence-map.md
> Basis: N claims verified, N sources, N full texts. Saturation: none. Stage A only.
## Measure (N1): the unaided delayed probe — instrument, delay, cost per session; proxies to ignore
## Practice unit and order (N2)
## Session shape (N3): intervene when / with what / feedback content and timing
## What holds on an LLM substrate (N7): holds / fails / untested — one table
## Claims table: claim_id | claim | S R O | population | axes | verify file
## Not covered yet (N4, N5, N6) and what that means for the first sessions
## Threats (from §9 of the plan, those live now)
Cite a verify/claims file per claim. Forbidden strings: "the trainer should", "architecture", "mode", "ladder".
```

### t5-evidence-map (fable; Read, Write)

Research-tree synthesizer template with this format:

```
# Teaching toward lasting unaided skill — Evidence map v{n}
> Basis: N sources (N full texts), N claims (N VERIFIED / N REFUTED / N UNVERIFIABLE), N resolutions,
  saturation table from ROOT/audit/.
## Answer (≤10 sentences, the question from the plan §1)
## Per need N1…N7: claims table (claim_id | claim | S R O | population | axes | status | file); disputes and
   their moderators; gaps with queries tried
## Pareto set: methods × axes table, each cell a claim_id or "—"; the set, and what trades against what
## LLM transfer: per method — holds / fails / gains / untested, with the harm evidence and the substrate facts
## Calibration to the owner (reads rulings 118–121 here only): which Pareto members the intake favors,
   and the early measurements from N1 that would confirm or overturn that
## Coverage gaps / ## Confidence per need (from audit) / ## What was not verified
Forbidden: trainer design. Cite a file per claim.
```

---

## 7. Staging and cost

Time to first training is first-class (line 130). Stage A ships a usable, honest, expiring answer before any saturation work.

| stage | waves (each wave = one parallel launch) | agents | models | lands |
|---|---|---|---|---|
| **A — first usable answer** | W1: t0 ×3 ∥ t1 ×7 → W2: t1-merge → W3: t2 N1,N2,N3,N7 + breadth-r1 → W4: t3 for the ≤8 claims the brief needs (synthesizer names them first from claims.csv, then verifiers run) → W5: t5-first-protocol | 3 + 8 + 5 + ~8 + 1 ≈ 25 | haiku 12, sonnet 12, fable 1 (+ claude-code-guide 1) | end of one orchestrator session; five sequential waves. Output: `synthesis/first-protocol.md` — training can start on it |
| **B — full map v1** | W6: t2 N4,N5,N6 + breadth-r2 ∥ t3 remaining Stage A claims → W7: t3-seed-probe ∥ t3 for Stage B load-bearing claims ∥ t3-substrate ×2–3 → W8: t2-n7-r2 (transfer lens over N1–N6) → W9: t4 ×3–6 → W10: audit r1 → W11: t5-evidence-map | 4 + ~14 + 3 + 1 + ~5 + 1 + 1 ≈ 29 | haiku 6, sonnet 17, opus 5, fable 1 | second session. Output: `synthesis/evidence-map.md` — replaces the brief; training adjusts |
| **C — saturation** | per round: fresh t2 for every OPEN need (different agents, new queries) + breadth + t3 for new S≥3 sources + audit; t5-map-v{n} when a VERIFIED claim changed | per round ≈ 7 + 1 + ~6 + 1 (+1) ≈ 16; expect 2–3 rounds | haiku 4, sonnet 11, fable ≤1 per round | rounds until all needs SATURATED or round 3 closes (§8 point 2). Output: `evidence-map-v{n}.md` |

Totals: ≈ 55 agents to v1, ≈ 100 to saturation at 3 rounds. Fable calls: 1 + 1 + ≤3.

Why Stage A already changes training: N1 gives the measurement the first sessions must collect (ruling 114's early measurement); N3 sets intervention under continuous watching; N2 sets what a session practises; N7 says which of that survives on the substrate. All four are verified claims with file citations the owner can open.

Orchestrator rules per research-tree: never relay content (AP-1); block each synthesis on all its inputs (AP-2); every wave one message (AP-5); verifier per extraordinary claim (AP-6); template pasted (AP-8); breadth finds get verifiers (AP-9).

---

## 8. Open points

The owner takes no more questions; the research launches from these defaults. Each: default, ground, what would overturn it.

| # | point | default | ground | overturned by |
|---|---|---|---|---|
| 1 | Saturation threshold | capture–recapture unseen ≤10% of S≥2 sources per need, plus two zero-new rounds (§5) | line 129: time to first training first-class; Rust's 2% was flagged "may be dropped if unrealistic" for a bounded surface — teaching literature is unbounded, so 2% would never close; 10% is reachable in 2–3 rounds and the audit reports the actual figure | audit round 2 shows every need under 5% — then lower to 5% at no cost |
| 2 | Stage C cap | three saturation rounds, then ship `evidence-map-v3.md` with OPEN needs declared in the confidence table | line 129 (start training soon, not build forever); line 116 (saturation) is honoured per need where reached, and the audit makes every unreached need visible rather than hidden | all needs SATURATED earlier (stop earlier); a VERIFIED claim still flipping in round 3 (one more round for that need only) |
| 3 | Training starts on Stage A | yes — the first sessions run on `first-protocol.md` | lines 129–130; line 114 requires early measurement *in training*, which cannot start before training does; the brief carries an expiry and only VERIFIED claims | Stage A verifies fewer than 5 claims — then Stage B's N1 and N3 precede training |
| 4 | K-12 evidence | kept at R=1, never excluded | line 110: every kind counts, weighed by relevance — exclusion would violate the ruling; R=1 makes the weighting explicit | none; a population dimension is the ruling made operational |
| 5 | Vendor-authored studies | S=1 with a commercial flag; excluded (S0) only under criterion 2 — efficacy claimed with no third-party evaluation at all | line 110; line 111 excludes snake-oil, not commerce; a vendor study with an independent evaluation is evidence about a deployed system, which N7 needs | a vendor study found retracted or data-free — criteria 1, 3 |
| 6 | Source languages | English, plus whatever the APIs return in other languages; no translated query rounds | no ruling for this research; the Rust ruling (line 90) is subject-specific and does not transfer; OpenAlex/ERIC/Crossref index English predominantly; a translated round costs a full round under point 2 | a seed-probe or breadth find showing a strong non-English literature for one need — one translated round for that need |
| 7 | Feedback style vs content | style ("blunt, terse, clear") is calibration, out of research; content and timing are researched under N3 | line 121 says feedback *to the owner*; line 120 says owner traits must not shape the product much; N3's content and timing findings are population-level | none |
| 8 | Early-measurement probes in the first sessions | yes: unaided delayed probes as N1 specifies, capped at 10 minutes per session until N1's cost evidence sets another figure | line 114 names early measurement in training as the calibration source; line 104 makes unaided-and-lasting the only outcome that counts, which nothing but a delayed unaided probe measures | N1 finds a cheaper instrument with O=2 evidence — use it |

---

## 9. Validity threats

Report of what could make the result wrong, uncompressed.

| threat | mechanism | control in the plan | residual |
|---|---|---|---|
| Subject priming | lines 100–101; agents given a language name frame everything by it | principle 5 in every prompt; no `docs/subjects/` input; reviewer greps synthesis for language names | agents still know Rust is the first subject if they read CLAUDE.md — they are not given it; t0-substrate reads CLAUDE.md for the orchestrator/trainer split only |
| Seed anchoring | peer claims steer search and grading toward the seed's picks | seed withheld from T1–T2; used only as a coverage probe and claim check after round 2 | strands 1–2 shape N3, N5 by ruling — intended |
| Abstract-level reading | seed shows most items [A]/[S]; numbers drift from abstracts | `full_text_read` column; T3 requires quotes; Unpaywall/arXiv/PMC routes; S≥3 with full_text_read=N triggers verification | paywalled works (ACM 403) may stay UNVERIFIABLE — count reported |
| Hallucinated citations | LLM agents invent plausible DOIs | principle 4: Crossref/OpenAlex response pasted per citation; script rejects rows whose DOI does not resolve | a real DOI attached to a wrong claim — caught only by T3 |
| Proxy outcomes | assisted success, satisfaction, felt learning read as learning | O dimension; O=0 never enters recommendations | O=1 (immediate) dominates the literature; durability claims will be thin — reported as gap |
| Population mismatch | K-12 and undergraduate evidence generalised to adult professionals | R dimension; population column on every claim | adult self-directed CS evidence may be near-empty — reported, not filled by analogy |
| Publication bias, one-study headlines | AI-tutoring results are recent, single, small | flag effect >1.0 SD single study; replication search in T3; T4 for disputes | recency: no replications exist yet for 2025–26 studies |
| Grading drift across agents | S/R/O bands applied differently | calibration set of 5 shared sources; >1-band disagreement → T4 | bands are still judgment; triple reported, not hidden in a score |
| Lazy saturation | agent asserts "nothing new" after few queries | void-round rules; script computes new-vs-seen from DOIs; capture–recapture; seed coverage floor | two lazy rounds with correlated queries can still overlap heavily → reuse cap 30% |
| Owner traits leaking into the general product | intake data shaping claims (ruling 120) | line 118 excluded from rulings-brief; calibration section only in synthesis, reading rulings 118–121 there | N6's attention sub-question is owner-motivated by ruling; it is framed for a population |
| Synthesis writes a design | strong models drift to "the trainer should" (ruling 108) | forbidden strings; format has no design section | reviewer must actually grep |
| Time pressure makes Stage A final | first-protocol treated as the answer | expiry line; Stage B blocked on nothing but launch; map replaces brief | owner attention may end at Stage A — §8 point 3 assumes it does not |
| Rate limits / blocks | Semantic Scholar 429; ACM, EEF 403 | OpenAlex primary; per-DOI S2 only; Unpaywall for full text; UNREACHABLE recorded | some evidence syntheses (EEF) reachable only via snippets |
| Measuring what is easy | skill/hour has evidence; transfer and sustainability far less | axis closure rule: each axis holds claims or a "no evidence" entry with queries | the Pareto set may be one-sided; that is the finding |
| Snake-oil register built from literature | exclusion criterion 4 uses S4 reviews — a literature judgment | criteria 1–3 are mechanical; 4 requires two independent reviews named | contested cases go to T4, not silently excluded |

---

## Summary

The research runs all six research-tree tiers over seven need-categories derived from the owner's rulings, graded on three separate dimensions (strength, population relevance, outcome match) with a mechanical snake-oil exclusion and a script-computed saturation rule. Stage A lands a verified, expiring first-training protocol (measurement, practice unit, session shape, LLM transfer) in one session of about 25 mostly cheap agents, before any saturation work; Stage B delivers the full evidence map; Stage C saturates to 10% unseen or three rounds. Eight open points carry defaults with grounds — training starts on Stage A's brief, K-12 and vendor evidence stay in at reduced weight, English sources, probes capped at 10 minutes — so the research launches without further questions.
