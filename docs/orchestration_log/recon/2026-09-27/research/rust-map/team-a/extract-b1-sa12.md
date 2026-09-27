## f004555 — Introducing Zed's Agent Metrics (2026-04-09, en)
### Nothing new
`nothing new`: Zed's public dashboard post on AI-agent adoption/latency metrics; no Rust language or practice disagreement, just usage analytics.

## f004562 — Git repo not recognized in a project (2026-04-11, en)
### Nothing new
`nothing new`: Zed bug-report thread about intermittent git-panel/git-binary detection failures; a tooling bug report, no Rust-practitioner disagreement.

## f004581 — Agents Week: network performance update (2026-04-17, en)
### Nothing new
`nothing new`: Cloudflare network-performance blog post (connection-time rankings across global networks); tagged "Rust" but the body never discusses Rust language or practice, only network measurement methodology.

## f004586 — iroh 0.98.0 - Getting back to traversing NATs (2026-04-17, en)
### Nothing new
`nothing new`: solo-authored (dignifiedquire) iroh release-notes changelog covering NAT-traversal fixes and a new pluggable-crypto-backend feature; describes options offered, not a contested point with an opposing voice.

## f004596 — Unable to connect to local network after prolonged use (no route to host) (2026-04-21, en)
### Nothing new
`nothing new`: Zed bug-report thread that resolves to a macOS Info.plist/TCC entitlement gap (missing NSLocalNetworkUsageDescription); an app-packaging/OS-permissions bug, not a Rust language or practice disagreement.

## f004598 — Making Rust Workers reliable: panic and abort recovery in wasm‑bindgen (2026-04-22, en)
### Questions
- Q: For Rust compiled to WebAssembly (wasm32-unknown-unknown), should panics use the platform default of panic=abort, or panic=unwind (running destructors and preserving instance state across a single failed request)?
  concepts: panic-handling, unwind-safety, wasm-compilation-targets; domains_live: wasm, cloud-workers; positions_seen: panic-unwind-for-reliability (Cloudflare Workers/wasm-bindgen team, adopted and planned as future default)
- Q: When an FFI/Wasm boundary must distinguish recoverable foreign exceptions from unrecoverable aborts, should the recoverable (unwind) case be explicitly tagged, or the unrecoverable (abort) case?
  concepts: error-classification, ffi-boundary-safety, exception-handling; domains_live: wasm, cloud-workers; positions_seen: tag-unwinds-explicitly (Cloudflare/wasm-bindgen team, chosen for ease of implementation)
### Claims
- voice: Guy Bedford, Hood Chatham, and Logan Gatlin (Cloudflare Workers/wasm-bindgen team) | position: panic-unwind-for-reliability | date: 2026-04-22 | locator: blog post, § "Implementing panic=unwind with WebAssembly Exception Handling" | paraphrase: added panic=unwind support to wasm-bindgen/Rust Workers via the WebAssembly Exception Handling proposal because panic=abort's default full-reinitialization recovery wipes in-memory state for stateful workloads like Durable Objects; shipped behind a flag in Rust Workers 0.8.0 with plans to make it the default | quote: "To recover from panics without discarding instance state, we needed panic=unwind support for wasm32-unknown-unknown in wasm-bindgen" | practiced_evidence: https://blog.cloudflare.com/making-rust-workers-reliable
- voice: Guy Bedford, Hood Chatham, and Logan Gatlin | position: tag-unwinds-explicitly | date: 2026-04-22 | locator: blog post, § "Abort recovery" | paraphrase: chose to mark all definitely-unwind errors with exception tags, rather than marking all definitely-abort errors, to distinguish recoverable foreign exceptions from unrecoverable aborts at the Wasm boundary, because their existing raw WAT-level Exception Handling implementation made that direction easier | quote: "We had two options to solve this technically: either mark all errors which are definitely aborts, or mark all errors which are definitely unwinds. Either could have worked but we chose the latter." | practiced_evidence: https://blog.cloudflare.com/making-rust-workers-reliable

## f004637 — Handling of HEAD requests violates RFC 9110 (2026-05-01, en)
### Questions
- Q: When a response body's size cannot be determined without expensive computation, should an HTTP framework represent that as a distinct "unknown size" state, or default to treating it the same as a known-empty body?
  concepts: api-design, option-semantics, http-body-trait; domains_live: web, core; positions_seen: distinguish-unknown-from-zero (lorenzleutgeb, proposed Body::unknown()), collapse-to-known-zero (status quo, http_body_util::Empty)
### Claims
- voice: lorenzleutgeb | position: distinguish-unknown-from-zero | date: 2026-05-02 | locator: axum issue #3741, comment 2026-05-02T11:59:01Z | paraphrase: proposes changing `impl IntoResponse for ()` to use `Body::unknown()` instead of `Body::empty()`, so a handler that can't cheaply determine its length on a HEAD request doesn't get a spurious `content-length: 0`, arguing the current special-casing is conceptually wrong | quote: "Special casing responses with `content-length: 0` is conceptually problematic." | practiced_evidence: https://github.com/lorenzleutgeb/axum/commit/378f9d4d9ede5050c22c8da8f7f1f77bbd65ce58
- voice: davidpdrsn (axum maintainer) | position: cautious-narrow-fix | date: 2026-05-02 | locator: axum issue #3741, comment 2026-05-02T12:49:09Z | paraphrase: resists making `()` default to an unknown body size because it could silently change behavior for unrelated responses; wants a fix that works for users unfamiliar with axum's APIs rather than one requiring them to opt in explicitly | quote: "Changing `()` to have an unknown body size feels too broad to me. I worry that might impact other responses using `()` that don't care about HEAD requests." | practiced_evidence: none

## f004685 — iroh 1.0.0-rc.0 - The first release candidate (2026-05-11, en)
### Nothing new
`nothing new`: iroh 1.0 release-candidate changelog (Friedel Ziegelmayer & Rüdiger Klaehn); describes their own API redesign (splitting PathWatcher into a snapshot API and an event-stream API) as a completed improvement, not a live contested point with an opposing voice.
