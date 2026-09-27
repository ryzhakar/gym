For each source: what must a Rust practitioner decide, and where do the sources conflict on it?

## f000267 — The Zebra Book (undated living document; accessed 2026-09-27, text cites tag v6.0.0; en)

Scope note: the frame URL is the book's landing page (4,285 chars, cached a4726cb06af4, complete, not a stub). Linked chapters were not followed, per Tier 2. Voice is an institution: Zcash Foundation ("The Zcash Foundation maintains the following resources documenting Zebra"), maintainer of Zebra, a Zcash full node in Rust. No date on the page; the Claim carries the access date, not a publication date.

### Questions
- Q: Which license should a Rust crate carry: the ecosystem's dual MIT/Apache-2.0, or a single license?
  concepts: licensing; dual MIT OR Apache-2.0; code provenance; domains_live: core; positions_seen: dual MIT/Apache-2.0 by default, MIT-only where code came from MIT-licensed projects (Zcash Foundation)

### Claims
- voice: Zcash Foundation | flag: voice-unverified | position: dual MIT/Apache-2.0, MIT-only where code provenance requires | date: 2026-09-27 (accessed; page undated) | locator: § License | paraphrase: Zebra is dual-licensed MIT and Apache-2.0; some crates are MIT-only because part of their code came from MIT-licensed projects. | quote: "Some Zebra crates are distributed under the MIT license only, because some of their code was originally from MIT-licensed projects." | practiced_evidence: none

Not logged, declared practice with no reason and no rejected alternative: distribution through a Docker image, signed pre-built binaries via `cargo binstall` (Sigstore attestation, Cosign signature) and source builds, all offered side by side (§ Getting Started, § Manual Install); `cargo install --locked zebrad` (§ Manual Install); the rocksdb C++ dependency and its GCC 15 workaround (§ Manual Install); GitHub Actions CI; Kubernetes health endpoints; publishing internal-API docs. Only the landing page was read; the book's other chapters may hold declared Positions.
