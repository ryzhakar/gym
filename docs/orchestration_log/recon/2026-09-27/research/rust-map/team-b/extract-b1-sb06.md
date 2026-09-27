## f001724 — 2024 Q3-Q4 Roadmap? (2024-07-12, en)
### Nothing new
`nothing new` — a collaborative roadmap-planning thread; every reply builds consensus on priorities (performance, logical types, community growth) with no contested Position surfacing.

## f001749 — Upgrade winit to 0.30.2 (2024-07-18, en)
### Nothing new
`nothing new` — ArthurBrussee narrates his own reasoning for a pragmatic `unsafe` workaround (casting away a lifetime, stored in a thread-local) and for a winit-version-pinning tradeoff, self-critically, but no second Voice contests either judgment; emilk only approves.

## f001838 — Initial rp235x support (2024-08-09, en)
### Questions
- Q: Should a multi-chip-variant HAL use a single PAC crate that selects the chip via Cargo features, or a separate PAC crate per chip family?
  concepts: crate organization, cargo features, PAC (peripheral access crate) generation
  domains_live: embedded
  positions_seen: single-crate-with-features, separate-crate-per-chip
### Claims
- voice: Dirbaio | position: single-crate-with-features | date: 2024-08-09 | locator: PR #3243, comment 2024-08-09T07:14:06Z | paraphrase: prefers adding rp235x support to the existing `rp-pac` crate (the `stm32-metapac` pattern) rather than a new per-chip crate (the `nrfxxx-pac` pattern already used elsewhere in the embassy org), since it's much less annoying to release and manage Cargo features | quote: "I think we should add rp235x to `rp-pac` (`stm32-metapac` style) instead of making separate crates per chip (`nrfxxx-pac` style). It's much less annoying to release and manage Cargo features." | practiced_evidence: https://github.com/embassy-rs/rp-pac/pull/5 (merged; single-pac approach adopted, "features did indeed clean up")

## f001890 — iroh 0.23.0 - Welcoming Node.js to the family! (2024-08-21, en)
### Nothing new
`nothing new` — a release-notes blog explaining already-made API renames (`connection`→`remote`); it announces a decision with its rationale but shows no contested Position from another Voice.

## f001953 — Compare (diff) two files (2024-08-29, en)
### Nothing new
`nothing new` — an end-user product feature request thread about Zed's UI (side-by-side diff view); no Rust language, design or implementation content at all.

## f001983 — Unlocked deps (2024-09-05, en)
### Nothing new
`nothing new` — a WIT/component-model keyword-naming bikeshed (`unlocked-dep` vs. `specified-dep` vs. `dependency` vs. `instance`) among many contributors floating alternatives with no settled two-sided split; the one Rust-affiliated participant (alexcrichton) only asks clarifying questions, taking no declared Position.

## f001990 — Easy Embeddings Indexing Pipelines with Redpanda and Neon (2024-09-06, en)
### Nothing new
`nothing new` — a no-code YAML pipeline tutorial; contains no Rust content and no declared technical position.

## f002027 — Add dual and quad SPI support (2024-09-14, en)
### Questions
- Q: When a foreign trait's shared type (e.g. `embedded_hal::spi::Operation`) can't expose the hardware-specific capability a HAL needs, should the HAL define its own parallel type (accepting API duplication and a breaking change) to extend, or add narrowly scoped extension methods that leave the foreign type untouched?
  concepts: embedded_hal, trait/type extension, orphan rule, API surface, breaking changes
  domains_live: embedded
  positions_seen: own-parallel-type-with-conversion, narrow-extension-methods
### Claims
- voice: elipsitz | position: narrow-extension-methods | date: 2024-09-17 | locator: PR #479, comment 2024-09-17T20:43:31Z and 2024-09-23T15:36:19Z | paraphrase: initially wary of "bolting on another `Operation` enum without re-evaluating the complexity of the API," since the existing SPI API is already fairly unintuitive; leans toward a narrowly scoped `transaction_with_width` method or new enum variants instead of a second type | quote: "I'd be wary of bolting on another `Operation` enum without re-evaluating the complexity of the API." | practiced_evidence: none
- voice: ivmarkov | position: own-parallel-type-with-conversion | date: 2024-09-23 | locator: PR #479, comment 2024-09-23T16:21:54Z | paraphrase: argues the crate effectively already has "its own `Operation`... if you squint a little" (currently just a type-alias out of laziness); users should not need to know or care whether they're going through embedded_hal's `Operation` or the crate's own, so making it a real, independently extensible type is fine even as a breaking change | quote: "yet - it is something the user should neither know, nor care about" | practiced_evidence: https://github.com/esp-rs/esp-idf-hal (maintainer; the plan to copy embedded_hal's `Operation` into the crate was adopted)

## f002033 — Pulley: tail calls (2024-09-15, en)
### Questions
- Q: How should an unstable/nightly-only compiler feature be gated in library code — via a Cargo feature flag, or via a `--cfg` set through RUSTFLAGS?
  concepts: cargo features, RUSTFLAGS, cfg, unstable/nightly features, CI
  domains_live: core
  positions_seen: rustflags-cfg-gate
### Claims
- voice: alexcrichton | position: rustflags-cfg-gate | date: 2024-09-16 | locator: PR #9251, comment 2024-09-16T15:40:18Z | paraphrase: recommends gating the tail-call code with `#[cfg(pulley_tail_call)]` set via `RUSTFLAGS`, rather than a Cargo feature, because a Cargo feature gets force-enabled by the "test with all features enabled" CI job even when the compiler in use is stable; this also lets the PR land, checked only by a dedicated nightly `cargo check` job, before upstream rustc codegen support for `become` exists | quote: "with a Cargo feature controlling this it unfortunately doesn't play well with our \"test with all features enabled\" in CI well because it enables the feature when a stable compiler is in use." | practiced_evidence: https://github.com/bytecodealliance/wasmtime/pull/9251 (merged; adopted, per fitzgen's follow-up commit)

## f002048 — Introduce autotuning to conv2d and conv_transpose2d with a new im2col/GEMM algorithm (2024-09-17, en)
### Nothing new
`nothing new` — GPU-kernel code review (hardcoded tile-size constants, `comptime` bounds checks); louisfd's questions and wingertge's answers converge into agreed refinements (e.g. moving constants into a `comptime` struct) with no opposing Position left standing.
