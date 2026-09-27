# Breadth round 2 — practitioner and grey literature, N4/N5/N6

Scope: sources absent from `index/index.md`'s 256 anchors. Searched HN Algolia API (primary), lobste.rs (via HN cross-reference), GitHub repository search via `gh api` (secondary, low yield). WebSearch was unavailable — session budget exhausted before this task started (shared across the team on this IP); no ERIC/Crossref/arXiv grey-lit pass was run since the practitioner-account brief pointed at HN/blogs/repos, not papers.

## Methodology

- N4 (diagnosis): 28 HN Algolia queries logged, `hn/n4_hn*.log`.
- N5 (elite margin): 17 HN Algolia queries logged, `hn/n5_hn*.log`.
- N6 (sustain): 20 HN Algolia queries logged, `hn/n6_hn*.log`.
- GitHub: 5 `gh api search/repositories` queries for deployed-tutor / mentoring-playbook / spaced-repetition repos — near-zero yield (one 0-star playbook repo, one hobby spaced-repetition tool; no outcome data attached to any).
- For each promising HN thread, fetched full item JSON (`hn/item_<id>.json`) via Algolia's items endpoint and read top-level comments directly (curl, not WebFetch) to extract the actual claims rather than title text alone.
- For external blog posts, used WebFetch against the specific URL surfaced by HN (4 fetches; 1 failed — DNS no longer resolves).
- 1s sleep between HN Algolia calls throughout, per instructions.
- 13 ledger rows appended, `ledger/sources.csv`, all graded S=1 (practitioner/opinion, no coded data or outcome measurement), O=0 (no unaided or delayed outcome measured anywhere in this batch — these are opinion and coping threads, not intervention studies). R varies 2–3.

Full texts read: 1 blog post read to completion (daedtech), 2 blog posts read via WebFetch summary (swarmia, atomicobject), 1 blog unreachable (melchua, DNS dead), 10 HN threads read via full comment JSON.

## High-signal finds

**Rise of the Expert Beginner** (daedtech.com, 2012) — the single highest-resonance find (three separate HN submissions, 672+238+157 points, 432+85+51 comments; sustained practitioner attention over at least three re-submission cycles = 2+ independent mentions). Core mechanism, stated as opinion not data: software's feedback loop is too slow and too socially thin for self-diagnosis — a developer isolated from peer review and the wider community plateaus and then reasons circularly ("I do it right because I'm the expert"). Directly names the mechanism N4 asks about: what breaks diagnosis is not lack of intelligence but lack of external calibration signal. No data; theory + anecdote (Dreyfus model, Dunning-Kruger, bowling analogy).

**Ask HN: Strategies for mentoring junior developers?** (2018, 215 pts, 71 comments) + **Atomic Object: Effective Mentoring Dialogue** (2015, single-case anecdote) converge on the same diagnostic move from two independent sources: don't state the misconception, ask a question the junior must answer from their own model ("why would the display update?"), and let the wrong answer surface the flaw. This is a concrete, repeatable technique, reported twice independently, but with zero measurement of whether it works better than telling.

**Ask HN: What is deliberate practice for programmers?** — asked independently on HN (2019, 6 pts) and lobste.rs (2019, 26 pts, cross-posted same year) — two independent venues converging on the same skepticism: repliers argue programming structurally resists deliberate-practice-style repetition because code is reused/abstracted rather than replayed like a piano piece or a chess opening. This is a portability objection to N5's elite-margin question that the indexed academic literature (Ericsson vs. Macnamara dispute) does not raise in these terms — practitioners are disputing whether the construct even applies to this domain, not just its effect size.

**Busting the 10x software engineer myth** (Swarmia, 2023; HN thread 155 pts/344 comments) — practitioner-blog counter-claim to the "elite individual" framing N5 was seeking evidence for: describes a specific case where a nominally indispensable, long-tenured engineer was later diagnosed as a knowledge-silo liability, not a multiplier — cited as a caution against reading "elite margin" purely off perceived individual output.

## Table of the rest

| find | venue | one line | fit |
|---|---|---|---|
| How did you go from being an adequate to exceptional programmer? | HN Ask (2014) | Recurring advice: learn the "why," deliberately rewrite the same function multiple ways and compare | N5, thin |
| How to improve as a struggling junior software engineer? | HN Ask (2022, 249 pts/170 comments) | Senior-side reframing: junior struggle often diagnoses a broken mentorship structure, not fixed ability | N4/N5 |
| How to find time to learn after full-time job? | HN Ask (2024, 61 pts/65 comments) | Recurring pattern: learning is scheduled opportunistically into low-workload weeks, not as a fixed daily habit — matches the project's own "irregular bursts toward daily" reality | N6 |
| After 4 years of self-funded coding marathons I feel "finished" | HN Ask (2010, 379 pts/184 comments) | Burnout narrative after sustained solo effort; only loosely about skill-practice sustain (it's product/marketing burnout) | N6, weak fit |
| ADHD developer coping threads (×3) | HN Ask (2019/2023/2024) | No established CS-specific hyperfocus-channeling method surfaced in any of the three; advice is individual (medication, scheduling around personal hyperfocus windows) | N6 — see Patterns |
| I am the dumbest person in the room | HN Ask (2015, 196 pts/183 comments) | Mostly imposter-syndrome coping, not a diagnostic technique; weaker fit than it looked from the title | N4, weak fit |
| Cognitive apprenticeship case studies in software engineering | melchua.com blog (2012) | Unreadable — domain no longer resolves (DNS failure). Found via HN Algolia snippet only, never verified | N4, unreachable |

## Patterns

1. **The strongest practitioner consensus is a negative result for N5's framing.** Every thread asking "what makes an elite/10x/exceptional programmer" (five separate threads, two independent venues) either fails to converge on a mechanism or actively argues the construct doesn't transfer cleanly from other skill domains to programming. This mirrors, from grey literature independently, the same Ericsson-vs-Macnamara tension already in the indexed academic literature — practitioners without access to that literature reach a structurally similar doubt.
2. **N4's best practitioner-level technique is question-driven elicitation, converging from two unconnected sources** (a 2018 Ask HN thread and a 2015 company blog, five years apart, no evidence either cites the other): ask a question whose wrong answer reveals the misconception, rather than stating the misconception. This is a specific, actionable, but entirely unmeasured claim.
3. **N6 has the weakest grey-literature yield of the three needs.** Twenty queries surfaced schedule-fitting anecdotes (learning gets slotted into light workweeks) but nothing resembling a documented, named method for "channeling hyperfocus-and-breadth attention" as ruling 120 asks about — the closest hits are three thin ADHD-coping threads offering only individual, non-CS-specific advice (medication, quiet hours). That absence, checked across 20 queries and 3 read-through threads, is itself the finding for this need: no CS-specific grey-literature answer exists at the depth this search reached.
4. **GitHub yielded almost nothing.** Deployed tutor repos with outcome data are apparently concentrated in the peer-reviewed literature already indexed (CodeHelp, CodeAid, OATutor, CTAT) rather than in unindexed public repos — five targeted searches found one 0-star playbook and one hobby spaced-repetition tool, neither carrying outcome data.
