## f003266 — Is this a bug in automatic reference counting? (2025-07-17, en)

### Nothing new
Swift forum thread among Swift compiler engineers (jrose, John_McCall) about `consume`/ARC lifetime semantics; no Voice shows a public Rust track record, and the one Rust mention ("If Swift always consumed in these situations, as Rust does") is a passing contrast, not a Rust practitioner Position.

## f003375 — Tutorial: Message Framing with iroh (2025-08-12, en)

### Nothing new
Single-author (n0 team) tutorial demonstrating one length-prefix framing technique; the aside on varints is advice, not an argued alternative, and no Voice disputes the approach.

## f003389 — Neon's Microsoft Azure Native Integration is Generally Available (2025-08-14, en)

### Nothing new
Product-announcement marketing post; no Rust design content and no contested point.

## f003414 — Add support for encodings other than UTF-8 (2025-08-19, en)

### Questions
- Q: When two crates cover the same need, how much should an unmaintained/flagged dependency (per RustSec) count against it versus its narrower scope fit?
  concepts: dependency selection, crate maintenance signals; domains_live: desktop-cli-ui; positions_seen: prefer the actively maintained, broader-scope crate even if built for a narrower original use case (`encoding_rs` over `encoding`)
- Q: Should an API expose shared mutable state (e.g. `Arc<Mutex<>>`) that callers can mutate implicitly, or should ownership changes be threaded explicitly through return values?
  concepts: interior mutability, API design, ownership; domains_live: desktop-cli-ui; core; positions_seen: no implicit shared mutable state, make changes explicit in the type signature
- Q: Is `unwrap()` acceptable in production code, or should it be reserved for tests and provably-infallible cases?
  concepts: error handling, panics; domains_live: core; positions_seen: early-return instead of `unwrap()` except in tests or when the current function makes non-panic provable by inspection
- Q: When a function's required inputs grow, is it better to add a separate specialized function or grow one function's argument list?
  concepts: API surface design, function signatures; domains_live: desktop-cli-ui; positions_seen: keep a separate `load_with_encoding` function to avoid a 4-argument `load`; vs. accept a single simpler function by dropping a feature (automatic UTF-16 detection) to keep arguments to two

### Claims
- voice: CrazyboyQCD | position: prefer actively-maintained broad-scope crate over flagged narrow one | date: 2025-08-30 | locator: comment 2025-08-30T08:19:58Z | paraphrase: argues `encoding` is unmaintained, buggy and legacy per a linked RustSec advisory, so a more modern crate (`encoding_rs`, or possibly ICU) is preferable even though `encoding_rs`'s stated focus is the Web | quote: "it is unmaintained, buggy and legacy, so I think a more mordern crate would be better" | practiced_evidence: none
- voice: ConradIrwin | position: no implicit shared mutable state in API | date: 2025-10-28 | locator: comment 2025-10-28T01:59:12Z | paraphrase: objects to a `Buffer` containing an `Arc<Mutex<>>` that lets callers change encoding without the buffer knowing; wants the encoding passed/returned explicitly instead | quote: "I don't like that the Buffer contains an Arc<Mutex<>> that allows callers to change the encoding without the buffer knowing" | practiced_evidence: none
- voice: ConradIrwin | position: unwrap only in tests or provably-safe spots | date: 2025-10-28 | locator: comment 2025-10-28T01:59:12Z | paraphrase: flags new `unwrap()`s as needing early returns instead, with unwrap acceptable only in tests or where the current function makes panics provably impossible | quote: "unwrap is OK in tests and also when you can tell by reading the current function that it can't ever unwrap" | practiced_evidence: none
- voice: EuclidDivisionLemma | position: keep a separate function over widening one function's argument list | date: 2025-09-13 | locator: comment 2025-09-13T06:20:43Z | paraphrase: weighs three options (keep `load_with_encoding` separate; one `load` with UTF-16 auto-detection at the cost of 4 args; drop auto-detection for a 2-arg `load`) and flags readability cost of merging | quote: "having a single function will require us to pass four arguments in all those places, making the code significantly less readable" | practiced_evidence: none
- voice: ConradIrwin | position: drop the feature to keep the function simple | date: 2025-09-12 | locator: comment 2025-09-12T19:43:46Z | paraphrase: is willing to merge without automatic BOM/UTF-16 detection to keep the `load` call simple, i.e. picks fewer arguments over the extra feature | quote: "I'd also be OK to merge a v1 of this work without the BOM detection" | practiced_evidence: none

## f003558 — Add feature-gated `getrandom` support (2025-09-19, en)

### Questions
- Q: Facing the absence of a proper Web-WASM Rust target, should the ecosystem work around it now with crate-feature plumbing, or push to get the target itself built first?
  concepts: WASM compilation targets, ecosystem workarounds; domains_live: wasm; positions_seen: push for a real `wasm32-web`/`wasm32-bindgen` target before adding more workarounds; vs. ship a workaround now because the target has seen no progress and must work on current stable/MSRV
- Q: When an opt-in crate feature can be misused by downstream crates (enabled unconditionally "for convenience"), is it the exposing crate's job to structure the API/placement to make misuse harder, or the misusing crate's bug to fix?
  concepts: crate feature design, dependency graph hygiene, Cargo feature unification; domains_live: wasm; positions_seen: place/gate the feature so incorrect use is less likely (e.g. host it in `js-sys` rather than `getrandom` directly); vs. misuse is a bug in the misusing crate, not something the exposing crate should engineer around

### Claims
- voice: CryZe | position: pursue a real Web-WASM target instead of another workaround | date: 2025-09-19 | locator: comment 2025-09-19T12:38:24Z | paraphrase: argues the root cause is the lack of a way to signal wasm-bindgen usage, and that a proper `wasm32-web` target would fix this class of problem generally, now that the project has active maintainers again | quote: "Shouldn't we finally discuss a proper wasm32-web / wasm32-bindgen target instead" | practiced_evidence: none
- voice: newpavlov | position: ship the workaround now, a new target isn't realistic soon | date: 2025-09-19 | locator: comment 2025-09-19T12:53:59Z; 2025-09-19T13:06:16Z | paraphrase: says there has been zero progress on a Web WASM target in about 4 years, `getrandom` needs a solution that works with the current stable Rust and declared MSRV, and hypothetical language changes are out of scope for this issue | quote: "I don't have any hope for getting it anytime soon" | practiced_evidence: none (maintainer of `getrandom`, per issue context)
- voice: newpavlov | position: structure feature placement to discourage misuse | date: 2025-09-19 | locator: comment 2025-09-19T16:28:13Z | paraphrase: prefers the feature live in `js-sys` rather than `getrandom` directly, reasoning that a crate wrongly adding `js-sys` unconditionally is a more visible/unlikely mistake than wrongly enabling a `getrandom` feature, since the latter has no effect on non-WASM targets and so goes unpunished | quote: "such incorrect behavior does not get punished, while users would be more careful with js-sys" | practiced_evidence: none
- voice: Pauan | position: misuse is the misusing crate's bug, not the exposing crate's design problem | date: 2025-09-21 | locator: comment 2025-09-21T22:11:14Z; 2025-09-21T22:31:20Z | paraphrase: rejects the "protect against misuse" framing outright, arguing crates cannot be forced to behave properly by restructuring the API, that misbehaving crates should have issues/PRs filed against them directly, and that shifting the feature to `js-sys` only relocates the same possible mistake | quote: "This seems to me like a solution in search of a problem" | practiced_evidence: none

## f003580 — R2 SQL: a deep dive into our new distributed query engine (2025-09-25, en)

### Nothing new
First-person Cloudflare engineering write-up (Yevgen Safronov, Nikita Lapkov, Jérôme Schneider) describing R2 SQL's planner/executor architecture built on DataFusion/Arrow/Parquet; it narrates the authors' own design rationale, including a batch-vs-row-at-a-time tradeoff, but no other Voice contests any of it — no disagreement is argued, only explained.

## f003590 — A DHT for iroh - Part 1, The Protocol (2025-09-26, en)

### Questions
- Q: Should an RPC failure response be a `Result<T, E>` carrying a detailed error, or a flat enum exposing only coarse, intentionally limited outcomes?
  concepts: error handling, RPC protocol design, serialization; domains_live: decentralized-iroh; positions_seen: use a flat outcome enum (e.g. `ErrFull`, `ErrInvalid`) instead of `Result<(), SetError>`, deliberately omitting fine-grained error detail
- Q: For a protocol meant to stay wire-compatible long-term, is a compact non-self-describing ordinal format (postcard) an acceptable choice, and what does using it commit you to?
  concepts: serialization format, protocol stability, wire compatibility; domains_live: decentralized-iroh; positions_seen: use postcard for compactness, but treat enum-variant order as an append-only contract that must never be reordered

### Claims
- voice: Rüdiger Klaehn | position: flat outcome enum over `Result<T, E>` for RPC responses | date: 2025-09-26 | locator: § RPC protocol / KV store protocol | paraphrase: explains the DHT's `SetResponse` is a plain enum rather than `Result<(), SetError>` because serializing detailed errors is often painful and because failure specifics like stack traces are "nobody's business"; the enum only tells the caller enough to decide whether retrying makes sense | quote: "you have to be aware that serializing detailed errors is sometimes a big pain" | practiced_evidence: https://github.com/n0-computer (iroh-dht-experiment repo linked in post)
- voice: Rüdiger Klaehn | position: postcard is fine if variant order is treated as a stability contract | date: 2025-09-26 | locator: § RPC protocol | paraphrase: states postcard is non-self-describing, so enum case order must be preserved for the protocol to remain stable long-term; this is presented as a requirement to design around, not a reason to avoid postcard | quote: "Postcard is a non-self-describing format, so we need to make sure to keep the order of the enum cases if we want the protocol to be long-term stable" | practiced_evidence: https://github.com/n0-computer (iroh-dht-experiment repo linked in post)
