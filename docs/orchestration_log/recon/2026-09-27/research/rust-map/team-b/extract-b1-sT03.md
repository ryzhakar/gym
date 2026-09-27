For each source: what must a Rust practitioner decide, and where do the sources conflict on it?

## f000896 — [Pitch] Synchronous Mutual Exclusion Lock (2024-02-06, en)

### Nothing new
A Swift Evolution thread about Swift's `Mutex` API: closure-based `withLock` versus exposing `lock()`/`unlock()` or a guard type, `Lock` versus `Mutex` naming, and Sendable constraints. Rust appears only as a reference design, for example Rust's `MutexGuard` and lifetimes (@Alejandro proposal § Mutex Guard API; @gwendal.roue 2024-02-09T16:31:08Z; @Joe_Groff 2024-02-09T16:32:15Z) and "in Rust we have Mutex" (proposal § Rename to Lock). No participant shows a public Rust track record in the source, and no one declares a Position on a decision Rust practitioners make.

## f000981 — Data Freshness: Why It Matters and How to Deliver It (2024-02-23, en)

### Nothing new
A Materialize marketing post (Kevin Bartley, Marketing Team) on operational data warehouses, CDC and incrementally maintained views. It never mentions Rust or any Rust decision.

## f001085 — Add right-click menu to dock (zed-industries/zed PR #8952) (2024-03-06, en)

### Nothing new
A PR review thread about wiring a macOS dock menu through gpui's `Platform` trait. It covers the feature's plumbing and questions about the local bundling script. @SomeoneToIgnore's architecture advice, to add a setter on `Platform` rather than calling the DB from `platform.rs` (2024-03-07T15:55:06Z), is a project-specific design call with no stated alternative that Rust practitioners hold. The contributor calls it "my first time using Rust" (2024-03-14T17:49:51Z).

## f001206 — uniffi-rs 0.27 throw error with Constructor return type must be Arc<Self> (mozilla/uniffi-rs #2051) (2024-03-27, en)

### Nothing new
A bug report that turned out to be a compatibility problem in cargo-swift (fix commit linked 2024-03-30T14:39:46Z). The maintainers (@mhammond, @bendk) state what UniFFI supports: a constructor may return `Self` or `Arc<Self>`. They take no Position on a contested decision.

## f001246 — Neon Developer Days 1: 6-8 December 2022 (post dated 2022-11-18; frame date 2024-04-03; en)

### Nothing new
A short event announcement for Neon's Serverless Postgres developer days. The body is complete at its natural length, so it is not a stub. It says nothing about Rust.
