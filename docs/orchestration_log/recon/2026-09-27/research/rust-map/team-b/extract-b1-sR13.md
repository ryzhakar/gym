## f007973 — Build with Naz : Comprehensive guide to nom parsing (2023-02-20, en)
### Questions
- Q: Should Rust developers write parsers with a combinator library (nom) rather than a grammar-based generator (pest, lalrpop) or a hand-rolled recursive-descent parser?
  concepts: parser combinators, zero-copy parsing, error reporting; domains_live: core;desktop-cli-ui; positions_seen: combinators (nom) as the idiomatic, efficient choice
### Claims
- voice: Nazmul Idris (r3bl_tui maintainer) | position: nom-style parser combinators are the effective way to build parsers in Rust: small composable functions, no unnecessary allocation, and richer error reporting via VerboseError/context than a naive hand-rolled parser would give you | date: 2023-02-20 | locator: "Getting to know nom using lots of examples" section | paraphrase: "nom is very efficient and fast, it does not allocate memory when parsing if it doesn't have to, and it makes it very easy for you to do the same"; the article goes on to show context/convert_error as the way to get human-readable error messages out of a combinator chain | quote: "nom is very efficient and fast, it does not allocate memory when parsing if it doesn't have to" | practiced_evidence: https://github.com/r3bl-org/r3bl-open-core (production Markdown parser built this way, in r3bl_tui)

## f008692 — The Embedded Rustacean Issue #58 (2025-11-07, en)
### Nothing new
This is a link-curation newsletter (news roundup, job board, event calendar); per the map's own finding, curated lists record conclusions, not disagreements, and no item here is the curator's own declared Position on a contested Rust question.

## f008801 — Visualizing persistent vectors with Rust and WebAssembly (2026-02-12, en)
### Questions
- Q: Should Rust's collections behave like true persistent (structural-sharing) values with cheap clone, rather than accepting the current model where clone is a full deep copy?
  concepts: ownership, persistent data structures, RRB trees; domains_live: core; positions_seen: persistent/structural-sharing collections are worth building for Rust
### Claims
- voice: Araz Abishov | position: Rust would benefit from persistent, structural-sharing vector types (RRB trees) that make clone cheap (O(log n) path-copying) instead of the O(n) deep copy that ordinary owned collections force today | date: 2026-02-12 | locator: opening paragraphs, before "A quick intro to persistent vectors" | paraphrase: "Ownership means you must clone a vector if you want to keep using it after passing it somewhere else. As Niko Matsakis pointed out, Rust collections already behave like values; they just have an expensive clone. What if that clone could be nearly free?" — this framing motivates building pvec-rs | quote: "Rust collections already behave like values; they just have an expensive clone." | practiced_evidence: pvec-rs (author's own crate, plus a WebAssembly visualizer built on it)

## f009654 — crates.io security incident: improperly stored session cookies (2025-04-11, en)
### Nothing new
A factual incident disclosure and remediation notice (cookie values leaking into Sentry, sessions invalidated); no Position is argued on any contested Question, only what happened and what was fixed.

## f009740 — Announcing Google Summer of Code 2026 selected projects (2026-04-30, en)
### Questions
- Q: How should a Rust project respond to AI-generated contributions/proposals in its community processes?
  concepts: AI-assisted Rust, contribution norms; domains_live: core; positions_seen: treat it as a real but manageable quality-control problem, rather than grounds for an outright ban
### Claims
- voice: Jakub Beránek, on behalf of the Rust Project mentorship team | position: AI-generated proposals are a genuine nuisance for a mentored-contribution program, but one that can be managed through normal review rather than requiring a blanket policy against them | date: 2026-04-30 | locator: paragraph on the 96 submitted proposals | paraphrase: "Like many other GSoC organizations this year, we somewhat struggled with some AI-generated proposals and low-quality contributions generated using AI agents, but it stayed manageable." | quote: "we somewhat struggled with some AI-generated proposals ... but it stayed manageable" | practiced_evidence: none stated beyond this year's GSoC selection round

## f009755 — Announcing a Maintainer in Residence: Scott Schafer for the Cargo team (2026-09-22, en)
### Questions
- Q: Should critical Rust infrastructure (e.g. Cargo) rely on volunteer maintainer bandwidth, or be sustained by dedicated, foundation/corporate-funded paid maintainers?
  concepts: OSS sustainability, maintainer funding, governance; domains_live: core; positions_seen: fund a full-time paid Maintainer in Residence via the Rust Foundation Maintainers Fund plus corporate donations (AWS)
### Claims
- voice: Jakub Beránek, on behalf of the Rust Funding team | position: when a critical team's volunteer maintenance capacity breaks down (members leaving or losing funding), the right fix is a dedicated, foundation-and-sponsor-funded full-time maintainer, not relying on remaining volunteers to absorb the gap | date: 2026-09-22 | locator: "Why Cargo?" section | paraphrase: the Cargo team "struggled with meeting its maintenance demands" after members left or lost funding, so the Funding team used Leadership Council and AWS money to open a new full-time Maintainer in Residence position; explicitly framed as partial relief, not a full fix | quote: "Even though we know that a single full-time maintainer will not completely solve the maintenance struggles of the Cargo team, we hope that it will improve the situation" | practiced_evidence: https://blog.rust-lang.org (Maintainers in Residence program, already running for a prior cohort before this Cargo-specific hire)

## f011688 — Writing Cronjobs in Rust (2024-01-23, en)
### Nothing new
A step-by-step API tutorial (apalis, sqlx, shuttle-shared-db) with no argued position of its own; the only editorial language ("Zero config. No Dockerfiles. Just write Rust and ship.") is site-wide Shuttle marketing chrome repeated on every blog post's footer, not a claim earned by this article's content.

## f011716 — Asynchronous Programming in Rust (Packt store listing) (2024-02-14, en)
### Nothing new
This is a retail product page (price tiers, shipping options, anonymous Amazon/Feefo reviews, publisher-written blurb and author bio), not the book's own text; no identified Voice's own words argue a Position on a contested Rust question here — only third-party marketing copy and anonymous customer praise.

## f012568 — This Week in Rust #605 (Reddit) (2025-06-25, en)
### Unreachable
Page renders only a cross-posting bot's meta-comments ("publishing in progress...", a link to the bot's own repo) plus Reddit's unrelated recommended-post sidebar; the actual r/rust discussion thread for the linked TWIR articles never loads. Logged unreachable rather than read, per the bot-page carve-out.

## f012788 — Netstack.FM, episode 15 (2025-11-26, en)
### Unreachable
The URL's #episode-15 fragment targets a specific episode, but both the bundled scrape and a direct re-fetch of the same URL return only the client-rendered default view (Season 1 episodes 33-38); episode 15's content never renders. Logged unreachable rather than read.
