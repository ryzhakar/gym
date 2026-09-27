## f002155 — [STM32ARMv7] Restore DBGMCU_CR register contents when stopping debug (2024-10-06, en)

### Questions
- Q: When a Rust trait method receives only `&self` (because the implementing type is shared behind an `Arc`), should new mutable state be added via interior mutability (`Mutex`), or should ownership be redesigned so the caller can pass `&mut` access instead?
  concepts: interior mutability, Arc, Sync bounds, ownership design; domains_live: embedded, core; positions_seen: prefer-redesign-over-mutex-or-arc (Yatekii)

### Claims
- voice: Yatekii | position: prefer-redesign-over-mutex | date: 2024-12-03 | locator: comment "I dont think the Mutex is necessary as the sequences are held on the session which should then go into the mutex. Not internally." | paraphrase: rather than adding a `Mutex` inside the type to satisfy a `Sync` bound, move the mutable state to the owning `Session` and access it there | quote: "I dont think the Mutex is necessary as the sequences are held on the session which should then go into the mutex." | practiced_evidence: none
- voice: Yatekii | position: prefer-no-arc | date: 2024-12-19 | locator: comment "Ah, I disregarded that fact. I would prefer no Arc 🤔 Maybe we can reevaluate in the future." | paraphrase: prefers avoiding Arc-based shared ownership for this type even after conceding the immediate `Sync` constraint requires it, wanting to revisit the design later | quote: "I would prefer no Arc 🤔 Maybe we can reevaluate in the future." | practiced_evidence: none

## f002226 — SE-0451: Raw identifiers (2024-10-24, en)

### Nothing new
nothing new — a Swift Evolution review thread on identifier syntax; Rust is named once only, by a Swift community member quoting rustc's confusable-identifier warnings as a point of comparison, not as a Rust Voice declaring a Position.

## f002271 — Support query parameters in routes (2024-11-03, en)

### Questions
- Q: When wrapping a browser Web API (e.g. `UrlSearchParams`) inside a Rust frontend-framework hook, should the API surface the raw web-sys type or convert it to an idiomatic Rust collection?
  concepts: web-sys/wasm-bindgen API wrapping, idiomatic API surface; domains_live: frontend, wasm; positions_seen: convert-to-rust-collection (lukechu10)
- Q: What naming convention should Rust reactive-frontend-framework hooks use, given no established convention exists across the ecosystem?
  concepts: hook naming conventions, API naming; domains_live: frontend; positions_seen: use_-prefixed-noun-phrase (lukechu10)

### Claims
- voice: lukechu10 | position: convert-to-rust-collection | date: 2024-11-03 | locator: comment on router.rs (2024-11-03T22:58:52Z) | paraphrase: a hook exposing browser search params should return a `HashMap<String, String>` rather than the raw `UrlSearchParams` handle | quote: "we should return a `HashMap<String, String>` from search params to values" | practiced_evidence: https://github.com/sycamore-rs/sycamore/pull/752
- voice: lukechu10 | position: use_-prefixed-noun-phrase | date: 2024-11-03 | locator: comment on router.rs (2024-11-03T22:54:24Z) | paraphrase: acknowledging no precise convention exists, proposes naming query/hash accessor hooks with a `use_<noun>` pattern (`use_search_query`, `use_location_hash`) | quote: "Although there isn't really a precise convention here, I think the hook would be better named `use_search_query` instead." | practiced_evidence: https://github.com/sycamore-rs/sycamore/pull/752

## f002341 — Relay outage: A post-mortem (2024-11-19, en)

### Questions
- Q: Do Rust's compile-time memory-safety guarantees protect a program against resource leaks, such as leaked async tasks and threads?
  concepts: memory safety guarantees, resource leaks, async task lifecycle; domains_live: distributed, core; positions_seen: safety-does-not-prevent-leaks (Arqu)

### Claims
- voice: Arqu | position: safety-does-not-prevent-leaks | date: 2024-11-19 | locator: "The Nitty Gritty" section, memory-issues paragraph | paraphrase: Rust's memory-safety guarantees address memory corruption, not leaks; the team leaked tokio tasks and threads in production and only found them through load testing and profiling | quote: "Rust's memory safety guarantees do not mitigate memory leaks" | practiced_evidence: https://github.com/n0-computer/iroh/pull/2915, https://github.com/n0-computer/iroh/pull/2924 (merged fixes)

## f002347 — Basic filtering examples for users of the bevy_log (2024-11-21, en)

### Questions
- Q: Should code blocks embedded in Rust doc comments be required to compile as doctests, or is it acceptable to leave illustrative snippets non-compiling?
  concepts: doctests, documentation conventions; domains_live: core; positions_seen: require-all-blocks-to-compile (BD103)

### Claims
- voice: BD103 | position: require-all-blocks-to-compile | date: 2024-12-17 | locator: comment on CI failures (2024-12-17T17:43:35Z) | paraphrase: Bevy's convention requires every doc-comment code block to be valid, compiling Rust because the project treats them as unit tests too | quote: "We require all code blocks to be valid Rust, since we treat them as unit tests as well." | practiced_evidence: https://github.com/bevyengine/bevy/pull/16455 (CI enforcement shown in thread)

## f002488 — [Pitch] Explicit Specialization (2025-01-02, en)

### Nothing new
nothing new — a Swift Evolution pitch thread on generic monomorphization/specialization; Rust is named once only, in a factual aside about ABI-stable monomorphized generics, not as part of any Rust practitioner's declared Position.
