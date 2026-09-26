# Rust Opinion Map — Spec

As of 2026-09-25.

## Purpose

The map lets Arthur choose his Rust positions on evidence rather than affinity, then place anything he reads, then anticipate who thinks what.

**Jobs, ranked**

1. **Deliberation: choose positions.** The Question is the primary unit. Each carries steelmanned Positions, their Arguments, the Values those appeal to, and the evidence.
2. **Orientation: place what I read.** Each Position carries tells: recognizable signatures in code, Cargo.toml and prose. Any artifact can be traced to the Questions it touches.
3. **Prediction: who thinks what.** Voice views are derived from dated Claims, never written as standalone profiles.

**Readers**

- **Data layer:** the single source of truth, structured, written for Claude and for tooling. It expresses every entity and relation in Language, and new kinds can be added later without rewriting existing data.
- **Presentation layer:** a web interface for Arthur to explore and study. It depends entirely on the data layer and keeps no state of its own; every view can be rebuilt from the data alone. Transient interaction, such as which names are revealed, is never stored.

**Judgment**

- Every Position is tagged fact, tradeoff or taste.
- Every Convention carries practice data: evidence of how widespread it is.
- No verdicts and no recommendations on tradeoffs or taste.

## Language

Eleven entities, one name each (default). The skeleton is IBIS (issue, position, argument), first described by Rittel and Kunz in 1970 ([source](https://eight2late.com/2014/11)), extended with people, dates, values, domains and concepts.

| Entity | Meaning | Retired aliases |
| --- | --- | --- |
| Question | A point where competent Rustaceans disagree. Example: should a library ever panic? | axis, debate, fork |
| Position | One answer to a Question | opinion, stance |
| Argument | A reason offered for or against a Position | — |
| Value | What an Argument ultimately appeals to: correctness, simplicity, iteration speed, performance, stability, approachability | principle |
| Voice | A person or institution that takes Positions | personality, figure |
| Claim | One Voice holding one Position, with its Source and date. The atom of evidence | — |
| Source | A dated primary artifact: post, talk, script, RFC, code, crate | — |
| School | Positions that repeatedly travel together across Voices. Derived from Claims, never declared | worldview, camp |
| Convention | A Position practice has settled on, with prevalence evidence and recorded dissent | idiom, best practice |
| Domain | An area of use where a Question is live: CLI, web, embedded, Wasm | — |
| Concept | A Rust idea or mechanism that Questions are about: ownership, lifetimes, async runtimes, macros, unsafe | topic |

"Philosophy" is retired: it meant Value in some uses and School in others.

**Relations**

- A Question has two or more Positions, is live in one or more Domains, and is about one or more Concepts.
- A Concept connects to other Concepts.
- An Argument supports or objects to one Position and appeals to one or more Values.
- A Claim links exactly one Voice, one Position and one Source, with a date.
- A Voice's view is the set of its Claims; it can hold different Positions at different dates.
- A School is a cluster of Positions co-held by several Voices.
- A Convention is a Position plus prevalence evidence.

## Constraints

Six findings from preliminary research bind the design.

| Finding | Consequence for the map | Source |
| --- | --- | --- |
| Voices change Positions. No Boilerplate's older scripts (up to video 43) recommend tokio; video 48 argues for synchronous Rust, threads and rayon | Every Claim is dated; a Voice renders as a timeline, not a label | [async script](https://www.namtao.com/async-isn-t-real-and-can-t-hurt-you/), [script index](https://www.namtao.com/nb/) |
| Loud is not common. No Boilerplate runs nightly by default; the 2025 State of Rust survey found most people on stable, with nightly use declining | Conventions need prevalence evidence independent of any Voice | [toolkit](https://www.namtao.com/rust-toolkit-2026/), [survey](https://blog.rust-lang.org/2026/03/02/2025-State-Of-Rust-Survey-results) |
| Questions are domain-local. Async is optional in a CLI but native to iroh 1.0 and to WASI 0.3 components, both released June 2026 | Each Question lists the Domains where it is live | [iroh 1.0](https://iroh.computer/blog/the-road-to-iroh-1-0), [WASI 0.3](https://wasi.dev/releases/wasi-p3) |
| Values conflict inside one person. Correct By Construction and the Simplicity Manifesto disagree on what type checkers buy you | Values are their own layer; every Argument names the Values it appeals to | [LLM_MANIFESTOS](https://github.com/ryzhakar/LLM_MANIFESTOS) |
| Existing curation records conclusions, not disagreements: crate lists and idiom lists state answers without the debate | Such lists are Sources for Conventions, not substitutes for the map | [idiomatic-rust](https://github.com/mre/idiomatic-rust) |
| Norms about machine-written work are contested. The Rust project retracted an LLM-drafted blog post in March 2026 | AI-assisted Rust is a candidate Question in its own right | [retraction note](https://blog.rust-lang.org/2026/03/20/rust-challenges) |

## Out of scope

- **The trainer program (default).** Curriculum, drills and measurement are a later artifact. The map only guarantees its data layer is readable by it.
- **Placing Arthur on the map (default).** Self-location is a separate artifact that reads the map, so current preferences cannot shape how the map is drawn.
- **Verdicts and recommendations** on tradeoffs or taste (see Purpose).
- **A crate catalog (default).** Crates appear only as Sources or as tells of a Position.

## Scope

**Questions: all of Rust, culture included.** Governance and community disputes count as Questions alongside technical ones, for example norms about AI-written contributions.

**Time window: current Claims, plus the history that explains today.** An older episode enters only when a live Position or Convention traces back to it.

**Who gets onto the map: a balance of argument strength and influence.**

- Each Position shows two advocates in full: whoever argues it best, and whoever is most heard holding it. When one Voice is both, it appears once.
- Other known holders are listed by name only, so Prediction still works.
- Influence is shown with the evidence behind it: crates maintained and how many projects depend on them, reach of books, courses or channels, roles in the Rust project or at major adopters. No single influence score.
- "Argues it best" is settled by the fairness test in Done and upkeep.

Every Voice is tagged by type: builder, educator, language designer, institution, critic or leaver.

## Evidence rules

- **What establishes a Claim:** the Voice's own declaration, something they said or wrote. Code alone never establishes a Claim: employers, deadlines, compatibility and history shape code as much as belief does.
- **What strengthens a Claim:** visible practice of the declared view in code the Voice maintains. Such a Claim is marked as practiced.
- **Code that contradicts a declaration (default):** recorded as a gap beside the Claim; it does not overturn it.
- **Minimum per Question:** at least two Positions, each backed by at least two independent Sources. Independent means from different Voices, and neither merely restates the other.
- **Practice data (default):** how widespread a Convention is comes from the annual State of Rust survey plus crates.io usage numbers, meaning downloads and how many crates depend on a given crate. Scanning public code is left out as noisy and expensive.
- **Storage:** a Claim stores a paraphrase, a link and a locator, with at most one short quote. Superseded Claims stay, marked by date.

## Bias controls

- **Names:** every argument renders anonymously; each Voice is revealed only when Arthur clicks that item.
- **No per-person rules:** the map governs itself by its generic rules alone. Amos, Tris and Greg appear wherever they hold a Position, at minimum by name. Because every Question carries at least two Positions with their best advocates, anything they claim already sits beside its strongest opposition.
- **Check on Claude's lean:** four established methods, adapted.
  1. Duplicate extraction, after systematic-review practice: on every Question, two independent runs fill the subjective fields (which Position a Claim supports, each Position's summary, the fact/tradeoff/taste tag) without seeing each other's work. Disagreements resolve by a rule fixed in advance. Cochrane requires this for subjective and critical data ([source](https://training-noproxy.cochrane.org/handbook/archive/v5.1/chapter_7/7_6_2_who_should_extract_data.htm)).
  2. Paired cases, after Anthropic's open-source even-handedness evaluation: each Position's case is written under identical instructions, then graded for equal depth, engagement and evidence ([source](https://github.com/anthropics/political-neutrality-eval)).
  3. Ideological Turing test, after Caplan (2011): each Position's summary must match how its own advocates state it ([source](https://en.wikipedia.org/wiki/Bryan_Caplan)).
  4. A judge that is not the writer: LLM graders favor their own outputs ([source](https://arxiv.org/abs/2404.13076v1)), so grading uses fresh Claude instances that wrote none of the text, with the order of compared texts swapped. Another company's model may replace them later; each check records which model judged it, so a switch means re-running checks, not redesigning.

A fifth control sits in Evidence rules: every Claim comes from a retrieved primary Source. Model recall is weakest on rarely documented facts and retrieval reduces that dependence ([source](https://arxiv.org/abs/2211.08411v2)), which is the mechanism behind a drift toward popular answers.

## Navigation and form

Interface details are settled later, in design iteration on real data.

- **Presentation:** a web interface.
- **Home:** a git repository of plain-text entity files; the site is generated from it.
- **Graphics first:** every view is a graphic; prose appears only when a mark is opened.
- **Matrix:** the front door. One row per Question, Voices as columns, each cell showing the Position held; rows and columns reorder until blocks appear, and the blocks are Schools. This is Bertin's reorderable matrix ([source](https://www.r-bloggers.com/2013/06/the-reorderable-data-matrix-and-the-promise-of-pattern-discovery/)). Columns stay anonymous until clicked.
- **Graph:** a second view showing how Concepts connect to each other and to the Questions, Values and Domains around them.
- **Deferred to design iteration:** controls, what each click opens, and phone behavior.

## Done and upkeep

**Done means complete.** The map counts as finished only when every Question passes every check in Bias controls; a pilot or partial pass is not done. Every step must run with Claude alone, so optional upgrades never block completion.

**Change is data.** The map changes only through its data layer. Every published state of the data must pass the tests below.

Acceptance tests, one per job plus one for fairness (default):

- [ ] **Deliberation:** for any Question, Arthur can state the strongest case for the Position he rejects.
- [ ] **Orientation:** a random tutorial, README or code sample can be placed on the Questions it touches.
- [ ] **Prediction:** a Voice's Position on a Question can be predicted from their other Claims, then checked against a Claim held back from the prediction.
- [ ] **Fairness:** each Position's summary passes the ideological Turing test in Bias controls.
