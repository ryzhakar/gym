## f003983 — Reorganize and tracing::instrument collective operations (2025-12-11, en)

### Questions
- Q: When a macro-generated code path (e.g. `#[tracing::instrument]` reaching a value only through a trait method) triggers a false-positive unused/dead-code lint, should the fix be a broad `#![allow(unused)]` or a narrowly scoped allow on the specific item?
  concepts: macros, trait dispatch, lints; domains_live: ml, core; positions_seen: broad-allow-when-linter-blind-to-trait-indirection (crutcher)
- Q: When two operations are logically distinct (a local op returning a `Tensor` vs. a collective op returning a `{PeerId: Tensor}` map) but share underlying logic, should the crate share code via a combinator abstraction or keep them separately implemented?
  concepts: code duplication, abstraction boundaries, collective/distributed tensor ops; domains_live: ml, distributed; positions_seen: extract-a-shared-combinator-even-if-unexposed (crutcher)

### Claims
- voice: crutcher | position: broad-allow-when-linter-blind-to-trait-indirection | date: 2025-12-15 | locator: comment 2025-12-15T20:40:52Z | paraphrase: the blanket `#[allow(unused)]` stays because the compiler's lint can't see that `TensorMetadata` trait operations are being consumed via `#[tracing::instrument]`, so item-level allows would misfire | quote: "Because the rust linter isn't smart enough to understand that `TensorMetadata` trait operations are being used by `#[tracing::instrument]`" | practiced_evidence: https://github.com/tracel-ai/burn/pull/4157
- voice: crutcher | position: extract-a-shared-combinator-even-if-unexposed | date: 2025-12-12 | locator: comment 2025-12-12T20:24:57Z | paraphrase: `reduce_sum` (local) and `all_reduce_sum` (collective) are different operations, but the duplication between them is real and worth solving with an internal op-combinator library, even if that library never reaches end users | quote: "we probably want a local op-combinator library to avoid that duplication, even if those ops aren't shared to users" | practiced_evidence: none

### Nothing new
(none for this source — both threads above yielded a Question and Claim)

---

## f004065 — Delivering at Scale: How Ninja Van Powers Millions of Shipments with TiDB (2026-01-05, en)

### Nothing new
Customer-story marketing post about a MySQL-to-TiDB migration at Ninja Van; no Rust content and no practitioner disagreement of any kind appears anywhere in the piece.

---

## f004166 — Building a serverless, post-quantum Matrix homeserver (2026-01-27, en)

### Nothing new
The port (Synapse to Cloudflare Workers) is described as done in TypeScript with Hono; Rust appears only in one unexplained Durable Object code snippet (`#[durable_object]`), with no Voice declaration of why Rust was used there versus TypeScript elsewhere — code alone, per Evidence rules, is never a Claim.

---

## f004169 — iroh 0.96.0 - The QUIC Multipaths to 1.0 (2026-01-27, en)

### Nothing new
Release-notes changelog (API renames, breaking-change list, multipath/QNT mechanics); it narrates implementation and naming decisions already made but records no Voice arguing a contested position against another view.

---

## f004170 — Use iroh with Tor for anonymous connections (2026-01-27, en)

### Questions
- Q: Should a networking library ship built-in support for many use-case-specific transports/backends, or keep its core minimal and expose a pluggable trait-based extension API for users to add their own?
  concepts: custom transports, trait objects, feature flags, dependency weight; domains_live: distributed, decentralized-iroh; positions_seen: minimal-core-plus-pluggable-traits (Rüdiger Klaehn)

### Claims
- voice: Rüdiger Klaehn | position: minimal-core-plus-pluggable-traits | date: 2026-01-27 | locator: section "What are iroh custom transports anyway?" | paraphrase: iroh will not build every candidate transport (WebTransport, Bluetooth, Tor, InfiniBand, ...) into the core; adding them all would create a maze of feature flags and drag in dependencies most users don't need, so the library exposes `CustomTransport`/`CustomEndpoint`/`CustomSender` traits for users to plug in only what they need | quote: "we do not want to add additional transports to the iroh codebase. That would make the code very complex with a maze of feature flags, add a lot of dependencies that most of our customers don't need" | practiced_evidence: https://github.com/n0-computer/iroh-tor

---

## f004173 — SP-001: Platform Support Levels (2026-01-28, en)

### Nothing new
A Swift forum policy-review thread (platform support tiers for Swift toolchains); Rust is mentioned once as a comparison (@bclee, 2026-02-03: Rust "largely relies on libc and otherwise ships a mostly self-contained toolchain," so it need not break down support by Linux distribution the way Swift does), but bclee shows no Rust track record per the Voices bar in `docs/subjects/rust.md` § Scope, and no Rust practitioner disagreement appears anywhere in the thread.
