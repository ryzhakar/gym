## f002499 — Implement `wait_for_done` for `DpiTransfer` (2025-01-03, en)

### Questions

(none)

### Claims

(none)

### Nothing new

`nothing new`: this is collaborative hardware/driver debugging (esp-hal DPI/DMA + PSRAM timing, bounce buffers, cache flushing) between contributors converging on a shared diagnosis, not a decision Rust practitioners are shown taking opposing Positions on.

## f002501 — allow_headers config allways falls back to * (2025-01-03, en)

### Questions

(none)

### Claims

(none)

### Nothing new

`nothing new`: a bug report and fix in loco-rs's CORS middleware config handling; the thread converges on a single diagnosis and a merged patch, with no contested design choice.

## f002542 — Bytecode Alliance Election Results (2025-01-14, en)

### Questions

(none)

### Claims

(none)

### Nothing new

`nothing new`: a governance-results announcement (TSC delegates, At-Large Director) with no argued position or disagreement in the text.

## f002550 — iroh 0.31.0 - Back At Fighting Fit (2025-01-15, en)

### Questions

(none)

### Claims

(none)

### Nothing new

`nothing new`: a release-notes post (features, bug fixes, breaking changes); it reports what was built and fixed, not a live disagreement.

## f002584 — Vim Roadmap 2025 (2025-01-22, en)

### Questions

(none)

### Claims

(none)

### Nothing new

`nothing new`: Conrad Irwin's roadmap for Zed's Vim emulation (conformance vs. multi-cursor UX) is an editor product roadmap, not a Question about Rust the language or ecosystem practice — no Rust practitioner is shown disagreeing with this Position, and the decision at hand (how faithfully to emulate Vim) isn't a Rust-practitioner decision.

## f002755 — Introducing Qdrant Cloud's New Enterprise-Ready Vector Search (2025-03-04, en)

### Questions

(none)

### Claims

(none)

### Nothing new

`nothing new`: a product-marketing announcement for Qdrant Cloud's enterprise features (RBAC, SSO, monitoring); contains no Rust-language or ecosystem content at all.

## f002775 — Rust on Cortex-R52 (2025-03-10, en)

### Questions

(none)

### Claims

(none)

### Nothing new

`nothing new`: an announcement that Ferrous Systems ported and open-sourced Rust support libraries for Arm Cortex-R52; Jonathan Pallant's quote is promotional framing, not a Position argued against a stated alternative.

## f002827 — Vibe Coding RAG with our MCP server (2025-03-21, en)

### Questions

(none)

### Claims

(none)

### Nothing new

`nothing new`: a webinar recap about AI coding assistants (Cursor, Copilot, Aider, Claude Code) and Qdrant's MCP server; no Rust-language or ecosystem content.

## f002937 — Wasmtime LTS Releases (2025-04-22, en)

### Questions

- Q: Should a fast-moving Rust ecosystem project (monthly feature releases) also commit to a formal long-term-support channel with a guaranteed multi-year security-fix window, or leave downstream stability entirely to users tracking upstream closely?
  concepts: release cadence, semver/API compatibility, security-fix support windows, ecosystem maintenance burden; domains_live: wasm; core; positions_seen: "adopt a formal LTS release train, decoupled from the fast release cadence" (Alex Crichton / Wasmtime)

### Claims

- voice: Alex Crichton | position: adopt a formal LTS release train, decoupled from the fast release cadence | date: 2025-04-22 | locator: "Wasmtime LTS Releases" article, paragraphs 2-4 (bytecodealliance.org/articles/wasmtime-lts) | paraphrase: Wasmtime previously supported each monthly release for only 2 months, forcing embedders to track upstream closely for security fixes; Wasmtime now designates every 12th release an LTS release, guaranteed 24 months of API-compatible security patches (no backported features), so users can upgrade yearly instead of monthly while still receiving guaranteed security fixes | quote: "This rate of change can be too fast for users so Wasmtime now supports LTS releases." | practiced_evidence: https://bytecodealliance.org/articles/wasmtime-lts (policy documented and live; 24.0.0 retroactively classified LTS, 36.0.0 scheduled as the next LTS)

### Nothing new

(n/a — Question and Claim logged above)

## f003044 — Trying `subsecond` and: `Ignoring hotpatch since there is no ASLR reference` (2025-05-25, en)

### Questions

(none)

### Claims

(none)

### Nothing new

`nothing new`: a support/bug-triage thread on Dioxus's experimental `subsecond` hot-patching feature (closures, async functions, multi-crate projects); contributors converge on workarounds and bug reports, no contested design Position.
