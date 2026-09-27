## f003587 — BurnpackStore (2025-09-26, en)
### Nothing new
`nothing new` — a code-review PR (serialization format choice rmp-serde→CBOR/ciborium, `Vec<u8>`-vs-`burn_common::Bytes`, naming, extension choice); every reviewer suggestion from nathanielsimard is accepted by antimora without pushback, so no persisting disagreement surfaces.

## f003634 — The Invisible Database: Running Postgres at Runtime (2025-10-02, en)
### Nothing new
`nothing new` — a Neon product/marketing post on Postgres infrastructure for AI agents; no Rust content and no practitioner voice or contested point.

## f003685 — Neon Developer Days: Mark Your Calendars for March 29th, 2023 (2025-10-14, en)
### Nothing new
`nothing new` — a short conference-announcement post with no technical or Rust content.

## f003702 — Hashing multiple blobs with BLAKE3 (2025-10-15, en)
### Nothing new
`nothing new` — a single-author (Rüdiger Klaehn) technical exploration of BLAKE3's internal/hazmat SIMD API combined with rayon; no second voice or contested design point.

## f003719 — Handling Time-Variant DAGs with Constraints in Postgres (2025-10-20, en)
### Nothing new
`nothing new` — a single-author (traconiq) Postgres/SQL schema-design write-up with no Rust content and no second voice.

## f003731 — iroh 0.94.0 - The Endpoint Takeover (2025-10-22, en)
### Nothing new
`nothing new` — a single-author (ramfox) release-notes post announcing the Node→Endpoint rename, `TransportAddr` enum, and the split of tickets into their own crate; no second voice or contested point.

## f003756 — Keeping the Internet fast and secure: introducing Merkle Tree Certificates (2025-10-28, en)
### Nothing new
`nothing new` — a multi-author Cloudflare post on post-quantum WebPKI/TLS certificate design; no Rust-specific practitioner decision or disagreement is stated, despite the Rust tag.

## f003809 — Release DataFusion 52.0.0 (Dec 2025 / Jan 2026) (2025-11-09, en)
### Nothing new
`nothing new` — a release-coordination checklist; its one technical exchange (tschwarzinger's `Arc<dyn Any>` downcast/Clone surprise in `DynamicFilterPhysicalExpr`, confirmed by adriangb as "probably a bug") is a confirmed defect under investigation, not two practitioners holding opposing design positions.

## f003815 — fix: revert deno wasm loading template (2025-11-10, en)
### Nothing new
`nothing new` — a debugging/revert PR; RReverser's instantiateStreaming-vs-plain-instantiate reasoning is accepted without a second voice defending the opposite choice, and kallebysantos's later "perhaps we don't need to revert" aside is never taken up by anyone.

## f003938 — Yew 0.22 - For Real This Time (2025-11-29, en)
### Nothing new
`nothing new` — a single-author (Mattuwu) release-notes post (component rename, for-loops in `html!`, MSRV bump, vendoring gloo-workers); no second voice or contested point.

## f003955 — Upstream `embassy-mcxa` (2025-12-04, en)
### Nothing new
`nothing new` — a code-import PR; i509VCB's regret that the HAL ships as a side crate is answered and accepted via felipebalbi/jamesmunns's incremental-then-unify rationale, and the license/scaffolding cleanup items converge without pushback.
