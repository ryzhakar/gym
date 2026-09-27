## f004378 — TiDB Community Quarterly Roundup: The Most Popular Discussion Topics in Q4 2025 (2026-03-06, en)
### Nothing new
No Rust content: the source covers TiDB/MariaDB/MySQL migration, TiDB Cloud pricing and RU billing, and TiDB feature-gap Q&A — no mention of Rust as a language and no engineering decision a Rust practitioner would face.

## f004414 — Building a Voice-First AI Journal: What I Learned About AI Memory, Vector Search, and TiDB (2026-03-13, en)
### Nothing new
No Rust content: the post is about an app's memory architecture (Mem0, embeddings, TiDB schema, Claude model choice) with no mention of Rust or a Rust-specific decision.

## f004555 — Introducing Zed's Agent Metrics (2026-04-09, en)
### Nothing new
Zed is Rust-built but this post is product analytics (session/turn/latency metrics across AI agents) with no claim about Rust language or engineering practice.

## f004562 — Git repo not recognized in a project (GitHub issue, zed-industries/zed#53694) (2026-04-11, en)
### Nothing new
A user bug report and troubleshooting thread about Zed picking up the wrong `git` binary / a broken `settings.json`; no Voice makes a declared engineering decision about Rust practice, only end-user diagnosis of one installation's behavior.

## f004581 — Agents Week: network performance update (Cloudflare Blog) (2026-04-17, en)
### Nothing new
Tagged "Rust" but the content is entirely about RUM-based network-latency measurement methodology and results; no Rust language or engineering claim appears.

## f004586 — iroh 0.98.0 - Getting back to traversing NATs (2026-04-17, en)
### Questions
- Q: Should a Rust networking crate hard-depend on one crypto/TLS backend, or expose the backend as a pluggable provider?
  concepts: dependency injection, feature flags, TLS backend selection; domains_live: decentralized-iroh, core; positions_seen: pluggable-by-default (iroh)
- Q: Should public enums/structs in an API heading toward 1.0 default to `#[non_exhaustive]`, accepting the forced wildcard match arm it imposes on callers?
  concepts: API stability, semver, non_exhaustive; domains_live: decentralized-iroh, core; positions_seen: non_exhaustive-by-default (iroh)
- Q: Should an async network server reject invalid/unauthenticated incoming connections before or after the handshake completes?
  concepts: async runtimes, QUIC, connection handling; domains_live: decentralized-iroh, distributed; positions_seen: reject-early (iroh)
### Claims
- voice: iroh/n0 (dignifiedquire, post author) | position: pluggable-by-default | date: 2026-04-17 | locator: § "Pluggable Crypto Backends" | paraphrase: iroh 0.98 makes the TLS crypto provider swappable via feature flags (`ring` default, `aws-lc-rs` alternative, or a fully custom provider), because a hard-pinned `ring` dependency breaks on platforms where it can't build or where an org mandates a FIPS-certified backend | quote: "It's a problem if you're on a platform where ring doesn't build, if your org mandates a FIPS-certified backend like aws-lc-rs" | practiced_evidence: https://github.com/n0-computer/iroh (PR #3992, cited in post)
- voice: iroh/n0 (dignifiedquire, post author) | position: non_exhaustive-by-default | date: 2026-04-17 | locator: § "Breaking Changes", multiple types marked `#[non_exhaustive]` (`iroh::DirectAddrType`, `iroh::address_lookup::mdns::DiscoveryEvent`) | paraphrase: newly public/changed types are marked non-exhaustive so future variants can be added without a breaking change | quote: none (structural, not prose declaration) | practiced_evidence: https://github.com/n0-computer/iroh
- voice: iroh/n0 (dignifiedquire, post author) | position: reject-early | date: 2026-04-17 | locator: § "Rate Limiting in the Router" | paraphrase: the router gained an `incoming_filter` hook so a public endpoint can accept/reject/retry an incoming connection by address, endpoint ID, or ALPN before the handshake finishes, because rejecting early is far cheaper than accepting then closing | quote: "Rejecting early is much cheaper than closing the connection after it's established... Benchmarks on the PR show ~30x throughput for address-based rejection vs. accepting and closing." | practiced_evidence: https://github.com/n0-computer/iroh (PR #3951, cited in post)

## f004596 — Unable to connect to local network after prolonged use (no route to host) (GitHub issue, zed-industries/zed#54414) (2026-04-21, en)
### Nothing new
The thread diagnoses a macOS entitlement/TCC bug (missing `NSLocalNetworkUsageDescription` in Zed.app's Info.plist) causing silent LAN-access denial; this is a platform packaging bug shared with other macOS apps (Cursor cited as precedent), not a Rust-specific engineering decision under dispute.

## f004685 — iroh 1.0.0-rc.0 - The first release candidate (2026-05-11, en)
### Questions
- Q: Should a Rust crate's live-state accessor and its change-notification stream be one overloaded API or two separate primitives?
  concepts: API design, async streams, ownership/lifetimes; domains_live: decentralized-iroh, core; positions_seen: split-into-two-primitives (iroh)
- Q: Should optional library functionality live behind feature flags in the main crate, or be split out into separate crates/repos?
  concepts: crate structure, modularity, release cadence; domains_live: decentralized-iroh, core; positions_seen: split-into-separate-crates (iroh)
### Claims
- voice: iroh/n0 (Friedel Ziegelmayer & Rüdiger Klaehn, post authors) | position: split-into-two-primitives | date: 2026-05-11 | locator: § "Path observation API redesign" | paraphrase: the single `PathWatcher` primitive tried to serve both "what are the paths right now" and "tell me when paths change," so it was replaced by `Connection::paths()` (a lifetime-bound borrowed snapshot) and `Connection::path_events()` (a `'static` event stream), each answering one question | quote: "went through PathWatcher, a single primitive that tried to serve two very different consumers: code that wants \"what are the paths right now?\" and code that wants \"tell me when paths change\"" | practiced_evidence: https://github.com/n0-computer/iroh (#4188, cited in post)
- voice: iroh/n0 (Friedel Ziegelmayer & Rüdiger Klaehn, post authors) | position: split-into-separate-crates | date: 2026-05-11 | locator: § "Sometimes things have to move out" | paraphrase: `DhtAddressLookup`, `MdnsAddressLookup` and `AccessLimit` were moved out of the `iroh` crate into their own crates/repos to allow independent versioning and release schedules and to reduce the number of optional features in the main crate | quote: "This allows us to have a different versioning and release schedule for these components. It is also helpful to reduce the number of optional features in iroh." | practiced_evidence: https://github.com/n0-computer/iroh-address-lookups, https://github.com/n0-computer/iroh-util
- voice: iroh/n0 (Friedel Ziegelmayer & Rüdiger Klaehn, post authors) | position: non_exhaustive-by-default | date: 2026-05-11 | locator: § "Non-exhaustive structs and enums" | paraphrase: restates and extends the 0.98 non_exhaustive Position — `PathEvent` and `IncomingLocalAddr` are marked non-exhaustive specifically to allow future variants without breaking the public API, requiring callers to add a wildcard match arm | quote: "PathEvent and IncomingLocalAddr are both #[non_exhaustive], so the compiler requires you to handle the case of variants we may add later." | practiced_evidence: https://github.com/n0-computer/iroh
