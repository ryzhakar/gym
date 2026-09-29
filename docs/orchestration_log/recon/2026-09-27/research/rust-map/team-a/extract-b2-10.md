## f009331 — Change error message of a failing `assert_eq!` (2026-03-30, en)

### Questions
- Q: What argument order (if any) should `assert_eq!`'s failure message impose: a canonical "actual, expected" order, the status-quo unordered left/right, or opt-in named labels?
  concepts: testing, macros, error-messages; domains_live: core; positions_seen: adopt actual-expected order; keep unordered (no consensus to codify); opt-in named disambiguators instead of a forced order

### Claims
- voice: nik-rev | connection: self-reported Rust use ("I frequently come across Rust codebases that have a different order"), posting a detailed macro-design proposal on internals.rust-lang.org | position: standardize the failure message on "actual, expected" order | date: 2026-03-30 | locator: @nik-rev · 2026-03-30T07:37:31.862Z | paraphrase: proposes changing `assert_eq!`'s panic message to "actual VS expected" because that reading is more natural and, per a GitHub search, the more common convention (32,800 vs 17,600 uses) | quote: "I think there's a lot of value to gain in eliminating this inconsistency from the ecosystem" | practiced_evidence: none | flag: voice-unverified
- voice: epage | connection: self-reported maintainer of the snapbox/assert_cmd/assert_fs crates | position: adopt "(actual, expected)" ordering | date: 2026-04-07 | locator: @epage · 2026-04-07T13:45:08.155Z | paraphrase: describes migrating his own snapbox crate's assertion APIs from an (expected, actual) convention to (actual, expected), after user confusion with the old order, with no confusion reported since | quote: "Since that change, snapbox has replaced cargo's bespoke assertions. I've not had any confusion" | practiced_evidence: https://crates.io/crates/snapbox | flag: voice-unverified
- voice: tcsc | connection: posting a Rust macro-design argument on internals.rust-lang.org | position: don't codify an order; the current unordered left/right is preferable given the split is not real consensus | date: 2026-03-30 | locator: @tcsc · 2026-03-30T11:10:59.693Z | paraphrase: argues a ~1/3 vs ~2/3 usage split is not enough consensus to codify, and that codifying an order would be wrong a large fraction of the time | quote: "I think rust's approach of not choosing a canonical ordering for this is better" | practiced_evidence: none | flag: voice-unverified
- voice: tornewuff | connection: posting a Rust macro-design argument on internals.rust-lang.org | position: don't codify an order (independent second voice) | date: 2026-04-01 | locator: @tornewuff · 2026-04-01T16:25:57.254Z | paraphrase: argues there is no real consensus in Rust or other languages/libraries about which order is correct, and explicitly defining one now will not fix the ambiguity, just relabel it | quote: "explicitly defining the order now is not going to fix that - it's just going to end up with a bunch of code where the labels are backwards" | practiced_evidence: none | flag: voice-unverified
- voice: Manishearth | connection: posting a Rust macro-design argument on internals.rust-lang.org | position: don't just reorder the default message; instead add opt-in named disambiguators (`expected=`/`actual=`) | date: 2026-03-31 | locator: @Manishearth · 2026-03-31T02:38:14.020Z | paraphrase: argues changing the default message ordering won't fix ecosystem inconsistency since most people won't notice; proposes `assert_eq!(expected = foo, actual = bar)` as an opt-in instead | quote: "you cannot just force consensus through a behavior change" | practiced_evidence: none | flag: voice-unverified

## f009358 — AI skills based on official guidelines (2026-08-31, en)

### Questions
- Q: Should the Rust Project officially adopt/publish AI(LLM)-oriented guidance ("skills"), leave this to unofficial third parties, or actively work to hinder LLM interoperability with Rust tooling?
  concepts: governance, AI-assisted-development, documentation; domains_live: core; positions_seen: official first-party adoption; unofficial-only, high bar for org adoption; actively hinder/sabotage LLM tooling; skeptical middle ground, no sabotage

### Claims
- voice: MusicalNinjaDad | connection: self-reported author of the proposed AI skills, built from official Rust guideline docs | position: the Rust Project should officially provide AI-targeted ("skill") versions of its human guidelines (API Guidelines, rustdoc book) | date: 2026-08-31 | locator: @MusicalNinjaDad · 2026-08-31T14:02:18.517Z | paraphrase: reports large quality improvements giving an LLM AI-friendly versions of the Rust API Guidelines and documentation guide, and proposes officializing this | quote: "I'd like to open up the idea of officially providing AI-targeted versions of the guidance we give to humans" | practiced_evidence: none | flag: voice-unverified
- voice: jyn | connection: posting on internals.rust-lang.org with detailed Rust-org process/policy knowledge (crates.io-dependency bar) | position: don't formally adopt this in the Rust org; keep it unofficial/third-party, with a high bar for anything the Rust org adopts | date: 2026-08-31 | locator: @jyn · 2026-08-31T15:06:39.141Z | paraphrase: argues formal adoption would be read as Rust encouraging LLM use, and suggests an unofficial plugin/site instead, applying the same high bar used for adding crates.io dependencies to std | quote: "i do not think this should be formally adopted by the Rust org" | practiced_evidence: none | flag: voice-unverified
- voice: Noratrieb | connection: posting on internals.rust-lang.org with Rust-project context | position: the Rust Project would not publish such AI skills (independent second voice for the unofficial-only position) | date: 2026-09-01 | locator: @Noratrieb · 2026-09-01T07:11:39.767Z | paraphrase: agrees people can write and share their own Rust AI skills, but the Rust Project itself would not publish them because too many people would oppose the endorsement | quote: "Too many people would be opposed to these kinds of endorsements (including me)" | practiced_evidence: none | flag: voice-unverified
- voice: zackw | connection: posting a detailed Rust-tooling argument on internals.rust-lang.org | position: Rust-the-project should actively hinder/sabotage LLM interoperability with Rust tooling entirely | date: 2026-08-31 | locator: @zackw · 2026-08-31T22:53:18.207Z | paraphrase: argues for putting anti-scraper measures in front of official Rust sites/crates.io/docs.rs and adding compiler/Cargo code that refuses to interoperate with agents | quote: "Rust-the-project should go out of its way to make it difficult to use LLMs to write programs in, or contribute to, Rust-the-language" | practiced_evidence: none | flag: voice-unverified
- voice: mhaeuser | connection: posting a detailed Rust-tooling argument on internals.rust-lang.org, describing own rustc-search use of LLMs | position: skeptical middle ground — avoid official endorsement or de-facto standardization, but reject sabotage; personally avoids LLM code generation while allowing narrow uses like semantic search | date: 2026-09-01 | locator: @mhaeuser · 2026-09-01T08:48:26.844Z | paraphrase: argues one can provide newcomers resources to prototype/upskill without making LLM-generated code look polished, and doesn't think AI writing guideline-compliant docs is needed to upskill and learn | quote: "You can provide newcomers with resources to prototype and upskill without making LLM code generation superficially look like polished work" | practiced_evidence: none | flag: voice-unverified

## f009604 — Clippy: Deprecating `feature = "cargo-clippy"` (2024-02-28, en)

### Questions
- Q: How should code detect that Clippy is linting it: an implicit Cargo feature flag (`feature = "cargo-clippy"`), or the built-in `cfg(clippy)`?
  concepts: conditional-compilation, clippy, linting; domains_live: core; positions_seen: deprecate the implicit feature flag, use `cfg(clippy)` instead

### Claims
- voice: The Clippy Team | connection: official Rust Clippy team blog post | position: deprecate the implicit `feature = "cargo-clippy"` config in favor of `cfg(clippy)` | date: 2024-02-28 | locator: byline "Feb. 28, 2024 · The Clippy Team" | paraphrase: states the implicit feature was only kept for backwards compatibility and will be deprecated ahead of `check-cfg` stabilization, replaced by an explicit `cfg(clippy)` alternative | quote: "The implicit feature = \"cargo-clippy\" has only been kept for backwards compatibility" | practiced_evidence: none | flag: voice-unverified

## f009612 — Changes to Rust's WASI targets (2024-04-09, en)

### Questions
- Q: How should an evolving WASI spec version be named as a Rust target triple: reuse a name that will later need renaming (`wasm32-wasi`), or version-suffix it from the start (`wasm32-wasip1`/`wasm32-wasip2`)?
  concepts: wasi, target-triples, wasm; domains_live: wasm; positions_seen: rename to version-suffixed target names going forward

### Claims
- voice: Yosh Wuyts | connection: self-reported author writing on behalf of the Rust project's WASI target work | position: rename `wasm32-wasi` to `wasm32-wasip1` and introduce `wasm32-wasip2`, rather than keep reusing the bare name across spec versions | date: 2024-04-09 | locator: byline "Apr. 9, 2024 · Yosh Wuyts" | paraphrase: states that with hindsight the project would not have named the WASI 0.1 target plain `wasm32-wasi`, and is now correcting this by rolling out version-suffixed target names ahead of an eventual WASI 1.0 | quote: "we would not have chosen to introduce the \"WASI, snapshot 1\" target as wasm32-wasi" | practiced_evidence: none | flag: voice-unverified

## f009635 — The wasm32-wasip2 Target Has Reached Tier 2 Support (2024-11-26, en)

### Nothing new
reason-code: no-decision
reason: The post is a status announcement that wasm32-wasip2 reached tier-2 platform support and how to enable it; it states no decision against a named alternative or contested tradeoff, only a milestone update.

## f009652 — C ABI Changes for `wasm32-unknown-unknown` (2025-04-04, en)

### Questions
- Q: Should Rust's C ABI for `wasm32-unknown-unknown` match the WebAssembly tool-conventions standard, or keep its historical non-standard ("legacy") definition that some tooling like wasm-bindgen relies on?
  concepts: wasm, C-ABI, wasm-bindgen, FFI; domains_live: wasm; positions_seen: switch to the standard tool-conventions ABI, breaking the legacy behavior

### Claims
- voice: Alex Crichton | connection: self-reported author describing the Rust compiler's own wasm ABI implementation and history | position: replace the long-kept non-standard "legacy" C ABI for wasm32-unknown-unknown with the standard tool-conventions ABI, despite breaking wasm-bindgen-era assumptions | date: 2025-04-04 | locator: byline "Apr. 4, 2025 · Alex Crichton" | paraphrase: explains the target has used a non-standard ABI since 2017 largely for wasm-bindgen compatibility, and that the compiler will now switch to the standard definition now that wasm-bindgen has been fixed to not rely on the old behavior | quote: "The time has now come to correct this historical mistake" | practiced_evidence: none | flag: voice-unverified

## f009664 — Security Advisory for Cargo (CVE-2026-5223) (2026-05-25, en)

### Nothing new
reason-code: no-decision
reason: The post is a security advisory describing a symlink-handling vulnerability in Cargo's tarball extraction and its fix; it states a bug patch, not a decision weighed against a named alternative approach.

## f009733 — Call for Testing: Build Dir Layout v2 (2026-03-13, en)

### Questions
- Q: How should Cargo organize intermediate build artifacts inside the build directory: by content type (current layout), or scoped by package name plus a build-unit hash (proposed v2 layout)?
  concepts: cargo-internals, build-cache, caching; domains_live: core; positions_seen: adopt package/hash-scoped layout to enable cross-workspace caching, cleanup, and finer locking

### Claims
- voice: Ed Page | connection: self-reported Cargo team member describing the change and its motivation | position: reorganize the build directory from an organize-by-content-type layout to one scoped by package name and a hash of the build unit and its inputs | date: 2026-03-13 | locator: byline "Mar. 13, 2026 · Ed Page" | paraphrase: proposes the new layout as a stepping stone toward cross-workspace caching, automatic cleanup of stale build units, and more granular locking, while flagging the Cargo team does not officially endorse sharing a build-dir across workspaces | quote: "this helps with: Build performance as the intermediate artifacts accumulate in deps/" | practiced_evidence: none | flag: voice-unverified

## f009735 — Security advisory for Cargo (CVE-2026-33056) (2026-03-21, en)

### Nothing new
reason-code: no-decision
reason: The post is a security advisory about a `tar`-crate permission-handling vulnerability used by Cargo during extraction, describing a patch shipped in Rust 1.94.1, not a contested design decision.

## f009743 — The many journeys of learning Rust (2026-06-25, en)

### Nothing new
reason-code: no-decision
reason: The post reports anonymized Vision Doc interview and survey quotes about learning Rust, attributed only to roles (e.g. "Fractional CTO", "Founder of a startup") rather than any name or handle, and closes with the author group's own suggestions framed as things "worth trying," not firm decisions weighed against rejected alternatives.
