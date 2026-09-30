# Opinion map

Owner rulings of 2026-09-25 (doc/SPEC.md, archived at docs/orchestration_log/archive/SPEC.md), generalized from Rust to any subject on the owner's ruling of 2026-09-26 to separate the map's architecture from its subjects; entered 2026-09-26. Later rulings are marked where they stand.

## Purpose

The map's focus is to inform the user and expose them to things they don't necessarily like, solving unknowns, known and unknown, as far as reasonable ROI allows (owner ruling 2026-09-26).

**Jobs, ranked**

1. **Deliberation: choose positions.** The Question is the primary unit. Each carries steelmanned Positions, their Arguments, the Values those appeal to, and the evidence.
2. **Orientation: place what the user reads.** Each Position carries tells: recognizable signatures in code, package manifests and prose. Any artifact can be traced to the Questions it touches.
3. **Prediction: who thinks what.** Voice views are derived from dated Claims, never written as standalone profiles.

**Readers**

- **Data layer:** the single source of truth, structured, written for Claude and for tooling. It expresses every entity and relation in the Language, and new kinds can be added later without rewriting existing data.
- **Presentation layer:** a web interface for the user to explore and study. It depends entirely on the data layer and keeps no state of its own; every view can be rebuilt from the data alone. Transient interaction, such as which names are revealed, is never stored.

**Judgment**

- Every Position is tagged fact, tradeoff or taste.
- Every Convention carries practice data: evidence of how widespread it is.
- No verdicts and no recommendations on tradeoffs or taste.

## Language

Eleven entities, one name each. The skeleton is IBIS (issue, position, argument), first described by Rittel and Kunz in 1970 ([source](https://eight2late.com/2014/11)), extended with people, dates, values, domains and concepts. Each subject's instances of these entities live in its file under `docs/subjects/`.

| Entity | Meaning | Retired aliases |
| --- | --- | --- |
| Question | A point where competent practitioners of the subject disagree | axis, debate, fork |
| Position | One answer to a Question | opinion, stance |
| Argument | A reason offered for or against a Position | — |
| Value | What an Argument ultimately appeals to: correctness, simplicity, iteration speed, performance, stability, approachability | principle |
| Voice | A person or institution that takes Positions | personality, figure |
| Claim | One Voice holding one Position, with its Source and date. The atom of evidence | — |
| Source | A dated primary artifact: post, talk, script, design proposal, code, package | — |
| School | Positions that repeatedly travel together across Voices. Derived from Claims, never declared | worldview, camp |
| Convention | A Position practice has settled on, with prevalence evidence and recorded dissent | idiom, best practice |
| Domain | An area of use where a Question is live | — |
| Concept | An idea or mechanism of the subject that Questions are about | topic |

"Philosophy" is retired: it meant Value in some uses and School in others.

**Relations**

- A Question has two or more Positions, is live in one or more Domains, and is about one or more Concepts.
- A Concept connects to other Concepts.
- An Argument supports or objects to one Position and appeals to one or more Values.
- A Claim links exactly one Voice, one Position and one Source, with a date.
- A Voice's view is the set of its Claims; it can hold different Positions at different dates.
- A School is a cluster of Positions co-held by several Voices.
- A Convention is a Position plus prevalence evidence.

## Design rules and where they come from

Each rule answers a finding; the finding's evidence stays with the subject or person it was found in.

| Rule | Finding | Evidence |
| --- | --- | --- |
| Every Claim is dated; a Voice renders as a timeline, not a label | Voices change Positions | `docs/subjects/rust.md` § Findings |
| Conventions need prevalence evidence independent of any Voice | Loud is not common | `docs/subjects/rust.md` § Findings |
| Each Question lists the Domains where it is live | Questions are domain-local | `docs/subjects/rust.md` § Findings |
| Values are their own layer; every Argument names the Values it appeals to | Values conflict inside one person | `docs/ground-truth.md` § Arthur at the start |
| Curated lists are Sources for Conventions, not substitutes for the map | Existing curation records conclusions, not disagreements | `docs/subjects/rust.md` § Findings |

## Scope rules

- The owner sets each subject's depth, how deep the rabbit holes go, and breadth, how wide the net is cast (owner ruling 2026-09-26). Inside that scope the user's current preferences never shape how the map is drawn.
- Governance and community disputes count as Questions alongside technical ones.
- Time window: current Claims, plus the history that explains today. An older episode enters only when a live Position or Convention traces back to it.
- How a subject's Question set closes is settled in that subject's research (owner ruling 2026-09-26).

**Who gets onto the map:** a balance of argument strength and influence.

- Each Position shows two advocates in full: whoever argues it best, and whoever is most heard holding it. When one Voice is both, it appears once.
- Other known holders are listed by name only, so Prediction still works.
- Influence is shown with the evidence behind it, of the kinds the subject's file names. No single influence score.
- "Argues it best" is settled by the fairness test in Done and upkeep.
- Every Voice is tagged by type: builder, educator, language designer, institution, critic or leaver.

## Evidence rules

- **What establishes a Claim:** the Voice's own declaration, something they said or wrote. Code alone never establishes a Claim: employers, deadlines, compatibility and history shape code as much as belief does.
- **What strengthens a Claim:** visible practice of the declared view in code the Voice maintains. Such a Claim is marked as practiced.
- **Code that contradicts a declaration:** recorded as a gap beside the Claim; it does not overturn it.
- **Minimum per Question:** at least two Positions, each backed by at least two independent Sources. Independent means from different Voices, and neither merely restates the other.
- **Practice data:** how widespread a Convention is comes from the subject's community survey plus its package registry's usage numbers, meaning downloads and how many packages depend on a given package. Scanning public code is left out as noisy and expensive. The subject's file names its survey and registry.
- **Storage:** a Claim stores a paraphrase, a link and a locator, with at most one short quote. Superseded Claims stay, marked by date.

## Bias controls

- **Names:** every argument renders anonymously; each Voice is revealed only when the user clicks that item.
- **No per-person rules:** the map governs itself by its generic rules alone. The user's current affinities (`docs/ground-truth.md` § Arthur at the start) appear wherever they hold a Position, at minimum by name. Because every Question carries at least two Positions with their best advocates, anything they claim already sits beside its strongest opposition.
- **Check on Claude's lean:** four established methods, adapted.
  1. Duplicate extraction, after systematic-review practice: on every Question, two independent runs fill the subjective fields (which Position a Claim supports, each Position's summary, the fact/tradeoff/taste tag) without seeing each other's work. Disagreements resolve by a rule fixed in advance. Cochrane requires this for subjective and critical data ([source](https://training-noproxy.cochrane.org/handbook/archive/v5.1/chapter_7/7_6_2_who_should_extract_data.htm)).
  2. Paired cases, after Anthropic's open-source even-handedness evaluation: each Position's case is written under identical instructions, then graded for equal depth, engagement and evidence ([source](https://github.com/anthropics/political-neutrality-eval)).
  3. Ideological Turing test, after Caplan (2011): each Position's summary must match how its own advocates state it ([source](https://en.wikipedia.org/wiki/Bryan_Caplan)).
  4. A judge that is not the writer: LLM graders favor their own outputs ([source](https://arxiv.org/abs/2404.13076v1)), so grading uses fresh Claude instances that wrote none of the text, with the order of compared texts swapped. Another company's model may replace them later; each check records which model judged it, so a switch means re-running checks, not redesigning.

A fifth control sits in Evidence rules: every Claim comes from a retrieved primary Source. Model recall is weakest on rarely documented facts and retrieval reduces that dependence ([source](https://arxiv.org/abs/2211.08411v2)), which is the mechanism behind a drift toward popular answers.

## Form

Interface details are settled later, in design iteration on real data (`docs/user_deferred_items.md`).

- **Presentation:** a web interface.
- **Home:** a git repository of plain-text entity files; the site is generated from it.
- **Graphics first:** every view is a graphic; prose appears only when a mark is opened.
- **Matrix:** One row per Question, Voices as columns, each cell showing the Position held; rows and columns reorder until blocks appear, and the blocks are Schools. This is Bertin's reorderable matrix ([source](https://www.r-bloggers.com/2013/06/the-reorderable-data-matrix-and-the-promise-of-pattern-discovery/)). Columns stay anonymous until clicked.
- **Graph, the map itself (owner ruling 2026-09-30):** the front door. Concepts are the nodes; an edge between two Concepts holds every Question that touches both, and the more Questions the stronger it draws. Read at a glance and walked through Concepts, in the manner of Obsidian's graph: a Concept opens to its neighbourhood and its Questions; no prose on the canvas. Concepts are deduplicated in the data layer before drawing.
- **Matrix, clustered two ways (owner ruling 2026-09-30):** Voices are similar by their stances on Questions, Questions are similar by the Voices taking stances on them; rows and columns are clustered on both, and the lumps that appear are the Schools.

## Boundaries

- **No trainer program.** Curriculum, drills and measurement are a separate artifact; the map only guarantees its data layer is readable by it.
- **No verdicts or recommendations** on tradeoffs or taste (see Judgment).
- **No package catalog.** Packages appear only as Sources or as tells of a Position.
- **Self-location**, placing the user on a map, is a possible application of a map, not a planned stage (owner ruling 2026-09-26).

## Interface to the rest of gym

- **Vocabulary.** The Language is the shared vocabulary for every gym artifact.
- **A readable data layer.** The only guarantee the map makes to the rest of gym is that its data layer is readable.
- **Domain scope.** Every Question lists the Domains where it is live, so other work can narrow to the target domains in `docs/ground-truth.md`.

## Done and upkeep

**Work in progress by default.** A subject's map is work in progress unless explicitly declared finished, and it is live while research keeps iterating on it; every entry shows whether it is provisional or checked (owner ruling 2026-09-27).

**Finished.** A map may be declared finished only when every Question in its scope passes every check in Bias controls; a pilot or partial pass is not finished.

**Change is data.** The map changes only through its data layer. A map declared finished must pass the tests below in every state it is published in; a work-in-progress map runs them as they become available and shows the results (owner ruling 2026-09-27).

Acceptance tests (the Deliberation test dropped, owner ruling 2026-09-26; how to set the tests up is open, `docs/user_deferred_items.md`):

- **Orientation:** a random tutorial, README or code sample can be placed on the Questions it touches.
- **Prediction:** a Voice's Position on a Question can be predicted from their other Claims, then checked against a Claim held back from the prediction.
- **Fairness:** each Position's summary passes the ideological Turing test in Bias controls.
