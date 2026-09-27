## f001398 — SE-0430 (second review): `sendable` parameter and result values (2024-05-07, en)
### Nothing new
`nothing new` — Swift Evolution keyword-naming review; no Voice holds a public Rust track record, and the Rust references are outside-analogies by Swift authors, not a Rust practitioner decision.

## f001401 — Small difference makes suspicion performance decreasing (2024-05-07, en)
### Nothing new
`nothing new` — collaborative Wasmtime/Cranelift bug diagnosis (instruction-fetch alignment); the exchange converges on a shared explanation, no declared, contested design Position.

## f001512 — Rework Uart constructors, add UartTx and UartRx constuctors. (2024-05-24, en)
### Questions
- Q: Should embedded HAL constructors return `Result` instead of panicking (`unwrap`) on invalid configuration?
  concepts: error handling, embedded HAL API design; domains_live: embedded; positions_seen: fallible-constructors (MabezDev)
- Q: Should embedded HAL peripheral construction use the type-state pattern to enforce valid configuration at compile time, given the complexity it adds?
  concepts: type-state pattern, embedded HAL API design; domains_live: embedded; positions_seen: type-state-suggested-but-costly (bjoernQ)
- Q: Should peripheral configuration be exposed through one `Config` struct set at construction, or through many individual constructors/`with_x` builder methods?
  concepts: config struct, builder pattern, API surface; domains_live: embedded; positions_seen: config-struct-consolidation (MabezDev), many-constructors-status-quo-criticized (jessebraham)
- Q: Should blocking and async variants of a peripheral driver share one generic implementation, or stay duplicated?
  concepts: generics over mode, async/sync duplication; domains_live: embedded, async; positions_seen: generic-over-mode (MabezDev)
### Claims
- voice: MabezDev | position: fallible-constructors-over-panic | date: 2024-06-11 | locator: comment 2024-06-11T10:24:37Z | paraphrase: constructors should return Result rather than unwrap/panic internally | quote: "We shouldn't unwrap here, let's make new and friends fallible I think" | practiced_evidence: none
- voice: bjoernQ | position: type-state-suggested-but-costly | date: 2024-05-24 | locator: comment 2024-05-24T15:15:23Z | paraphrase: type-state could resolve the TX/RX default-pin ambiguity but adds ongoing complexity | quote: "Maybe adding type-state but that gets annoying later" | practiced_evidence: none
- voice: MabezDev | position: config-struct-consolidation | date: 2024-06-11 | locator: comment 2024-06-11T10:22:55Z | paraphrase: once a setting is part of the config, it should not be public as a separate method — everything should go through the config struct | quote: "If this is part of the config now, then I don't think this should be public anymore, we should do everything through the config struct" | practiced_evidence: none
- voice: jessebraham | position: many-constructors-status-quo-criticized | date: 2024-05-30 | locator: comment 2024-05-30T12:38:44Z | paraphrase: the proliferation of constructors without documentation makes the API hard to understand | quote: "there are way too many constructors and not enough documentation" | practiced_evidence: none
- voice: MabezDev | position: generic-over-mode | date: 2024-05-29 | locator: comment 2024-05-29T09:59:47Z | paraphrase: blocking and async constructors should share one generic implementation instead of duplicating methods | quote: "I think we should be able to have one impl that is generic over the mode." | practiced_evidence: none

## f001515 — iroh 0.17.0 - Everything Is A Little Better (2024-05-24, en)
### Nothing new
`nothing new` — release-notes blog post (API renames, changelog, a self-reported perf regression vs. raw quinn); no contested decision, only one Voice reporting without argued alternatives.

## f001582 — Wasmtime: Implement the custom-page-sizes proposal (2024-06-10, en)
### Questions
- Q: Should a type's representation encode an invariant directly (e.g. storing `log2(page_size)` instead of the raw value) to make invalid states unrepresentable, rather than validating separately at each use site?
  concepts: invalid-states-unrepresentable, type design, invariants; domains_live: core, wasm; positions_seen: encode-invariant-in-representation (fitzgen)
- Q: When a compiler backend (LLVM/Cranelift) could optimize an eager computation away, should code still be written in the more efficient/lazy form?
  concepts: compiler-trust, readability vs. micro-optimization; domains_live: core; positions_seen: readability-over-manual-optimization-when-backend-cleans-up (fitzgen)
### Claims
- voice: fitzgen | position: encode-invariant-in-representation | date: 2024-06-10 | locator: PR description, 2024-06-10T20:15:41Z | paraphrase: storing log2(page_size) instead of the raw page size cuts down on invalid states and the assertions needed elsewhere | quote: "In general, we store the log2(page_size) rather than the page size directly. This helps cut down on invalid states and properties we need to assert." | practiced_evidence: https://github.com/bytecodealliance/wasmtime/pull/8763
- voice: fitzgen | position: readability-over-manual-optimization-when-backend-cleans-up | date: 2024-06-11 | locator: comment 2024-06-11T16:35:49Z | paraphrase: eager vs. lazy default computation doesn't matter much here since LLVM can likely optimize it away, but the change is worth making for reader clarity | quote: "I think it probably doesn't matter much either way in this case, since there isn't anything here that could prevent LLVM from cleaning this up itself" | practiced_evidence: none

## f001609 — Healing Connections After Network Migration (2024-06-17, en)
### Nothing new
`nothing new` — descriptive networking-design explainer (hole-punching, NAT healing); one Voice describing a shipped mechanism, no contested Rust-practitioner decision.

## f001617 — Add language-agnostic snippets (2024-06-19, en)
### Nothing new
`nothing new` — Zed editor feature PR about snippet naming/config, not a Rust language or practice decision.
