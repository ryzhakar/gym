Framing: For each source, where do competent Rust practitioners disagree?

## f000258 — Hello wasm-pack! (unknown (living document), en)
### Questions
- Q: For a WebAssembly binary where size is often critical, should a Rust/wasm project use a size-optimized global allocator (e.g. wee_alloc) instead of Rust's default allocator, accepting slower allocation for a smaller compiled footprint?
  concepts: WebAssembly, global allocator, binary size, wasm-bindgen; domains_live: wasm; positions_seen: rustwasm project (wasm-pack-template) — offers wee_alloc as an optional allocator replacement for size-sensitive wasm binaries, trading allocation speed for code size
### Claims
- voice: rustwasm project (wasm-pack-template docs) | connection: official rustwasm/wasm-pack project documentation and template, the canonical wasm-pack tutorial | position: prefer-size-optimized-allocator-for-wasm | date: unknown (no page date; internal evidence — rustc 1.30-1.33 references, wasm-pack pre-1.0 usage — places the tutorial text circa 2018-2019, on a page still served as a living document) | locator: wasm-pack docs, "Template Deep Dive" -> "wee_alloc" | paraphrase: The tutorial presents wee_alloc, a ~1KB WebAssembly-targeted allocator, as an optional feature the official project template ships, framing it explicitly as a size/speed tradeoff against Rust's default global allocator: smaller code size, worse allocation performance. | quote: "wee_alloc trades off size for speed. It has a tiny code-size footprint, but it is not competitive in terms of performance with the default global allocator, for example." | practiced_evidence: https://github.com/rustwasm/wasm-pack-template | flag: voice-unverified

## f000491 — Asset loading on the Web produces many 404 errors for `.meta` files (2023-10-17, en)
### Nothing new
reason-code: no-decision
reason: A long Bevy GitHub issue thread about WASM/web asset loading spamming 404s for `.meta` files; contributors (including maintainer @cart) discuss possible fixes, but every substantive proposal is phrased as a tentative plan ("I think", "probably", "haven't thought of one yet") or as a workaround tied to the commenter's own project situation, so none clears the declared-Position bar.

## f000725 — embedded-hal v1.0 now released! (2024-01-09, en)
### Questions
- Q: When a hardware-abstraction-layer (HAL) crate's trait design serves two audiences — end users wanting ergonomic direct APIs and generic-driver authors wanting portable abstractions — and the two goals conflict, which should the crate prioritize?
  concepts: HAL trait design, generic drivers, API ergonomics; domains_live: embedded; positions_seen: Rust Embedded Working Group (embedded-hal 1.0) — prioritize generic-driver-writing over direct end-user API ergonomics when the two conflict
- Q: For async trait methods in embedded/no_std Rust, should code rely on native async-fn-in-trait support (stable since Rust 1.75) or on macro-based polyfills like the async-trait crate?
  concepts: async traits, no_std, dynamic dispatch, heap allocation; domains_live: embedded; positions_seen: Rust Embedded Working Group (embedded-hal-async) — prefer native async traits over macro-based polyfills for bare-metal/no_std, since native support avoids heap allocation and dynamic dispatch
### Claims
- voice: Rust Embedded Working Group (embedded-hal project) | connection: official embedded-hal 1.0 release announcement on the Rust Embedded WG blog; embedded-hal is the central HAL trait crate of the embedded Rust ecosystem | position: prioritize-generic-driver-goal-over-end-user-api-goal | date: 2024-01-09 | locator: Rust Embedded Working Group blog, "embedded-hal v1.0 now released!" -> "Focus on drivers" | paraphrase: The post states that previous embedded-hal versions tried to serve both standardizing end-user HAL APIs and enabling generic drivers, that these goals sometimes conflict, and that 1.0 deliberately picks the generic-driver goal because it brings much more value, simplifying/merging some traits and removing others (e.g. timers) that didn't serve generic drivers well. | quote: "Experience has shown that these goals sometimes conflict with each other. As the latter brings much more value, 1.0 focuses on that." | practiced_evidence: https://github.com/rust-embedded/embedded-hal | flag: voice-unverified
- voice: Rust Embedded Working Group (embedded-hal project) | connection: same | position: prefer-native-async-traits-over-macro-polyfill-for-embedded | date: 2024-01-09 | locator: Rust Embedded Working Group blog, "embedded-hal v1.0 now released!" -> "Async" | paraphrase: The post introduces embedded-hal-async and states its async traits can be used without heap allocation or dynamic dispatch, explicitly contrasting this with "previous macro-based polyfills like the async-trait crate," and frames native async traits (stable since Rust 1.75) as a good fit for bare-metal embedded use precisely because they avoid that overhead. | quote: "They can be used without heap allocations or dynamic dispatch (unlike previous macro-based polyfills like the async-trait crate), so they are a great fit for bare-metal embedded usage." | practiced_evidence: https://github.com/rust-embedded/embedded-hal | flag: voice-unverified

## f001795 — Bounded lists and strings (2024-08-01, en)
### Nothing new
reason-code: off-subject
reason: A WebAssembly Component Model / WASI Interface Types (WIT) design thread about adding bounded-length lists and strings to the language-neutral component type system; participants occasionally cite Rust types (heapless::String, arrayvec::ArrayVec) only as illustrative bindings for a cross-language spec decision, not as a Rust practitioner's own declared Position.

## f002563 — async/stream/future plumbing for wasmtime-environ (2025-01-18, en)
### Nothing new
reason-code: no-decision
reason: A Wasmtime PR review thread about how to lay out internal VM tables for resources, futures, streams and error-contexts; the participants (including maintainer alexcrichton) weigh implementation options but every choice is left as an open, deferred question ("could this be deferred to a future PR", "we can always come back in the future"), with no settled declared Position reached in the thread.

## f002722 — examples: add mnist-no-std (2025-02-25, en)
### Nothing new
reason-code: no-decision
reason: A Burn PR adding a bare-metal/TrustZone no_std training example; most of the thread is code-review nits and CI troubleshooting, and the one substantive design discussion (host-driven, interrupt-free control flow for OP-TEE) is presented as following necessarily from that specific hardware's constraints, and the PR is ultimately withdrawn as too niche for the core examples repo — no declared Position defended against a viable alternative.

## f002835 — Make the critical-section impl optional (2025-03-24, en)
### Questions
- Q: For an internal implementation detail that a crate does not consider part of its public API contract, should the crate expose configuring it via a Cargo feature flag, or via a build-time config option (outside Cargo's global feature-unification)?
  concepts: Cargo features, feature unification, semver, crate configuration, critical-section; domains_live: embedded; positions_seen: esp-hal maintainers (bugadani, bjoernQ, Dominaezzz) — prefer a config option over a Cargo feature when the choice is not part of the public API, partly to avoid a Cargo feature being accidentally enabled elsewhere in the dependency graph
### Claims
- voice: bugadani | connection: esp-hal maintainer/reviewer, author of the PR changing esp-hal's critical-section handling (esp-rs/esp-hal) | position: prefer-config-option-over-cargo-feature-for-non-public-api-choice | date: 2025-03-25 | locator: github.com/esp-rs/esp-hal PR #3293, review comment thread, 2025-03-25T14:55:40Z | paraphrase: Discussing whether esp-hal's critical-section implementation choice should be a Cargo feature or a config value, bugadani frames the criterion as whether the choice counts as public API; since an existing issue (#2509) said to keep such choices as Cargo features only when they are public API, and the team judges the critical-section implementation to be an internal detail (the `critical-section` crate itself is the public API), they favor a config option over a feature, partly because a config option can't be "accidentally enabled" by another crate the way a globally-unified Cargo feature can. | quote: "I guess the question is, do we consider the CS implementation a public API? If yes, #2509 indicates we should stick with the cargo feature." | practiced_evidence: https://github.com/esp-rs/esp-hal/pull/3293 | flag: voice-unverified

## f003114 — fp8 support (2025-06-11, en)
### Nothing new
reason-code: no-decision
reason: A Candle PR adding fp8 tensor support; the thread is CUDA-compatibility debugging (PTX JIT failures, compute-capability testing on specific GPUs) and benchmark reporting, with no declared Position on a Rust-practitioner design question.

## f003232 — allow `EntityCloner` to move components without `Clone` or `Reflect` (2025-07-09, en)
### Nothing new
reason-code: no-decision
reason: A Bevy ECS PR review thread on component-cloning/moving semantics and hook interactions; the author repeatedly frames the design direction as tentative ("I think", "I believe the best course of action... for now", open questions about whether a use case even exists), so no settled declared Position emerges from the thread.

## f005231 — Tesla Cybertrucks Are Rusting Despite Being Made Of Stainless Steel (2024-02-15, en)
### Nothing new
reason-code: off-subject
reason: A car-news article about corrosion on Tesla Cybertruck stainless-steel body panels; "rust" here is the metallurgical phenomenon, unrelated to the Rust programming language.
