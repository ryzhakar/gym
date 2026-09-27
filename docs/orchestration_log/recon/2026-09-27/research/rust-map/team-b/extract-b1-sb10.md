## f003080 — Redesigned Swift.org is now live (2025-06-04, en)
### Nothing new
`nothing new` — Swift.org website-redesign feedback thread (visual design, marketing copy); no Voice holds a public Rust track record and no Rust practitioner decision is at stake, only passing outside-references to Rust's learning curve.

## f003186 — fix(no_std)!: respect `std` feature when target is windows/unix (2025-06-27, en)
### Questions
- Q: Should a crate's Cargo feature flags always be strictly additive (the crate builds with any subset of features, including none), or is it acceptable for disabling a feature (like `std`) to change what builds successfully on certain targets?
  concepts: Cargo feature flags, additive features, no_std support; domains_live: core, embedded; positions_seen: features-must-stay-additive (alexcrichton), disabling-a-feature-can-change-buildability (salmans, initial PR)
### Claims
- voice: alexcrichton | position: features-must-stay-additive | date: 2025-06-30 | locator: comment 2025-06-30T18:19:37Z | paraphrase: the `std` feature should not be required just to build the crate on Linux/Windows targets; requiring it defeats the point of feature gating | quote: "the `std` feature should not be necessary to just build the crate, even on Linux/Windows targets. In essence these CI changes shouldn't be necessary." | practiced_evidence: https://github.com/salmans/wasmtime/pull/1
- voice: salmans | position: disabling-a-feature-can-change-buildability | date: 2025-06-27 | locator: PR description, 2025-06-27T21:18:19Z | paraphrase: the fix intentionally disables standard-library-dependent features for dependents using `default-features = false`, changing what builds under that configuration | quote: "This fix will disable standard library features for dependents that use wasmtime with `default-features = false`." | practiced_evidence: https://github.com/bytecodealliance/wasmtime/pull/11152

## f003188 — iroh v0.90 - The Canary Series (2025-06-27, en)
### Questions
- Q: Before a crate's 1.0 release, should breaking changes ship frequently in a fast pre-release ("canary") channel to get user feedback quickly, or should a team hold changes until they are fully finished before cutting each release?
  concepts: pre-1.0 semver policy, release cadence, breaking changes; domains_live: distributed, decentralized-iroh; positions_seen: frequent-canary-releases-for-fast-feedback (ramfox)
- Q: Should library-facing errors be concrete, enumerable types (e.g. via `thiserror`/`snafu`) rather than a single opaque/type-erased error (`anyhow::Error`)?
  concepts: error handling, `anyhow` vs `thiserror`/`snafu`, concrete vs opaque error types; domains_live: distributed, decentralized-iroh; positions_seen: concrete-errors-over-anyhow (ramfox)
### Claims
- voice: ramfox | position: frequent-canary-releases-for-fast-feedback | date: 2025-06-27 | locator: blog body, paragraph beginning "Last time we published a release blog" | paraphrase: waiting until everything was fully finished before releasing was not the best way to get a stable release into users' hands; three-week cycles and fast canary releases before 1.0 get feedback quickly and let the team move with confidence | quote: "we realized that waiting until we had everything worked through and finished before releasing was not actually the best way for us to get a stable release into the hands of our users." | practiced_evidence: https://iroh.computer/blog/iroh-0-90-the-canary-series (shipped as this very release)
- voice: ramfox | position: concrete-errors-over-anyhow | date: 2025-06-27 | locator: "💥 Concrete Errors 💥" section / Breaking Changes list | paraphrase: all iroh public APIs now return concrete error types instead of anyhow::Error, a large change touching most of the codebase | quote: "all public APIs return concrete error types, rather than anyhow::Error" | practiced_evidence: https://iroh.computer/blog/iroh-0-90-the-canary-series (shipped in this release)

## f003222 — iroh-blobs v0.90 - The Upgrade Guide (2025-07-04, en)
### Questions
- Q: Should library-facing errors be concrete, enumerable types (e.g. via `thiserror`/`snafu`) rather than a single opaque/type-erased error (`anyhow::Error`)?
  concepts: error handling, `anyhow` vs `thiserror`/`snafu`, concrete vs opaque error types; domains_live: distributed, decentralized-iroh; positions_seen: concrete-errors-over-anyhow (rklaehn)
- Q: Given Rust has neither function overloading nor default parameter values, should optional/configurable operations expose a single `_with_opts(Options)` method (with convenience wrappers delegating to it), or another mechanism for common cases?
  concepts: optional parameters, builder pattern, `impl Into<T>`, API ergonomics; domains_live: distributed, decentralized-iroh; positions_seen: with-opts-plus-convenience-wrappers (rklaehn)
### Claims
- voice: rklaehn | position: concrete-errors-over-anyhow | date: 2025-07-04 | locator: "Errors" section | paraphrase: iroh-blobs has vastly reduced its use of anyhow, switching to the snafu crate for concrete errors with backtraces and span traces | quote: "Compared to the old blobs, we have vastly reduced the usage of anyhow for errors. Instead we use the snafu crate to provide concrete errors, with some additional features like backtraces and span traces." | practiced_evidence: https://iroh.computer/blog/iroh-blobs-0-90-changes (shipped in this release)
- voice: rklaehn | position: with-opts-plus-convenience-wrappers | date: 2025-07-04 | locator: "Options" section | paraphrase: Rust has neither overloading nor default parameters, so each operation exposes an `_with_opts` method taking an Options struct (the closest mapping to the underlying RPC message), plus convenience wrapper methods using `impl Into<T>` for common cases | quote: "in other languages, you might solve this issue with either overloading or with default parameters. But rust has neither, for very good reasons. So we have come up with the following pattern." | practiced_evidence: https://iroh.computer/blog/iroh-blobs-0-90-changes (shipped in iroh-blobs)

## f003272 — TiDB Cloud User Research: The Process Behind the Updates (2025-07-17, en)
### Nothing new
`nothing new` — TiDB Cloud console UX/navigation research write-up; a product-design case study, no Rust content or practitioner decision at all.

## f003275 — dont normalize twice for no reason in octahedral_decode (2025-07-18, en)
### Nothing new
`nothing new` — a trivial bevy shader fix; the thread is almost entirely in-joke banter, with only a minor variable-naming/doc-comment nit, not a contested Rust design decision.

## f003302 — Why Postgres needs better connection security defaults (2025-07-22, en)
### Nothing new
`nothing new` — a Postgres/libpq/OpenSSL connection-security explainer (sslmode, channel binding); about Postgres protocol security, not a Rust language or practice decision.
