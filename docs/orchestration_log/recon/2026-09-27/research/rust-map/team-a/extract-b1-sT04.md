For each source: where do competent Rust practitioners disagree?

Team a · batch 1 · third pass · slice T04 · bundle samples/bundles/b1-team-a-T04.txt · no fetches made.

## f001244 — Next.js authentication using Clerk, Drizzle ORM, and Neon (2024-04-02, en)

### Nothing new
It is a TypeScript/Next.js tutorial with no Rust connection. Its one declared stance ("never 'roll your own' regarding authentication") is language-agnostic, and the rest is install and setup practice.

## f001271 — Qdrant Hybrid Cloud and Haystack for Enterprise RAG (2024-04-10, en)

### Nothing new
It is a partnership announcement listing product benefits. It has no Rust content and states no decision against an alternative.

## f001319 — Iroh 0.14.0 - Dial the world (2024-04-18, en)

### Questions
- Q: Should a pre-1.0 Rust networking library ship breaking wire-protocol changes in a routine minor release for a protocol improvement, or keep compatibility with the previous release?
  concepts: semver; pre-1.0 stability; wire-protocol compatibility; relays; domains_live: decentralized-iroh; distributed; core; positions_seen: break-compat-with-transition-window

### Claims
- voice: dignifiedquire (byline, iroh blog; Rust connection in source: iroh release post with Rust API code) | position: break-compat-with-transition-window | date: 2024-04-18 | locator: section "Faster relay handshakes" | paraphrase: The relay handshake was refactored to drop a full roundtrip on every new connection. The team accepted that new relays cannot talk to 0.13.0 nodes, and softened it by keeping the old relays running for at least 4 more weeks. | quote: "Unfortunately, this means the new relays can not talk to 0.13.0 nodes." | practiced_evidence: https://github.com/n0-computer/iroh/releases/tag/v0.14.0 | flag: voice-unverified

Not logged, as practice with no reason (rule 8): "Iroh relies on redb", the redb v2 upgrade (a performance gain, but no alternative named), and DNS discovery based on pkarr.

## f001531 — How to create previews with anonymized production-like data in seconds (2024-05-28, en)

### Nothing new
It is a Neon and Neosync product-integration post. It has no Rust content and no decision against an alternative.

## f001578 — Add an interface to your Neon database via Outerbase (2024-06-07, en)

### Nothing new
It is an integration announcement for Outerbase Data Studio. It has no Rust content and no declared decision.

## f001650 — iroh 0.19.0 - Make it your own (2024-06-27, en)

### Questions
- Q: Must async Rust APIs such as RPC channels be cancel-safe, with a missing guarantee treated as a bug, or is cancel-safety a caller responsibility to be documented?
  concepts: async; cancellation safety; futures; RPC; channels; domains_live: core; decentralized-iroh; distributed; positions_seen: cancel-safety-required-in-library

### Claims
- voice: ramfox (byline, iroh blog; Rust connection in source: iroh release post, Rust code, and "the quic-rpc crate, which is a crate that we've written") | position: cancel-safety-required-in-library | date: 2024-06-27 | locator: section "Better late than never" | paraphrase: The team broke its two-week release cadence because it found a rare, high-load critical bug: its RPC channels were not cancel-safe. They fixed it in quic-rpc and upgraded iroh before releasing. The documented-caller-responsibility alternative is not named in the source; the Position rests on the stated reason (critical bug, fix immediately). | quote: "Turns out, our RPC channels were not cancel-safe." | practiced_evidence: https://github.com/n0-computer/iroh/releases/tag/v0.19.0 | flag: voice-unverified

Not logged, as practice with no reason (rule 8): the ProtocolBuilder, `Builder::disable_docs()`, the RPC connection APIs, the relay config changes, and the Breaking Changes list (for example "Builder loses the E type parameter").

## f001677 — [Proposal] Set literals (2024-07-04, en)

### Nothing new
It is a Swift Evolution pitch thread on Swift literal syntax, and no Voice shows a Rust connection in the source. Under rule 9 its Positions are neither Claims nor mapped onto Rust Questions; the only Rust mention is @vns 2024-07-07T11:07:12Z citing Rust as an example language.
