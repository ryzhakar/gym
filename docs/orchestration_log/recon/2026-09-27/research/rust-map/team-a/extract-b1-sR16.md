## f012428 — Rust Polymorphism live-coding video (developerlife.com / "Nas") (2025-03-26, en)
### Questions
- Q: Is Rust's trait-based supertrait/subtrait polymorphism (no class inheritance) an adequate, ergonomic substitute for OOP-style inheritance, or does the required generic/trait-bound plumbing make it more verbose and confusing than an inheritance-based language?
  concepts: traits, generics, subtyping/variance, static vs. dynamic dispatch; domains_live: core, desktop-cli-ui; positions_seen: adequate-but-more-verbose (Nas)
### Claims
- voice: Nas (CEO/founder Rebel, author developerlife.com, maintainer of Rebel's Dewey crates) | position: adequate-but-more-verbose | date: 2025-03-26 | locator: video ~[34:17]-[35:17] | paraphrase: modeling an OOP-style view/component hierarchy in Rust via supertrait/subtrait relationships (rather than inheritance) works, but doing it generically over the inner-storage type is a lot more work and, in his words, more verbose and confusing than the equivalent in Kotlin, Java or TypeScript | quote: "arguably it's more verbose and somewhat confusing especially if you're coming from something like cotlin or java or typescript" | practiced_evidence: none (points to his "Rebel Open Core repo" generally, no URL given for this specific pattern)

## f012642 — GreptimeDB Rust Client - A Comprehensive Guide to High-Throughput Bulk Stream Inserts (2025-07-30, en)
### Questions
- Q: Should a high-performance Rust client API expose multiple tiers of the same builder operation — an unchecked/positional fast path alongside a checked/named-field safe path — rather than one safe-by-default interface?
  concepts: API design, ergonomics vs. performance, unchecked/checked accessors; domains_live: distributed, core; positions_seen: offer-tiered-apis (Greptime)
### Claims
- voice: Jiachun Feng (Co-Founder, Greptime) | position: offer-tiered-apis | date: 2025-07-30 | locator: § "Three Insert Approaches" | paraphrase: the bulk-stream row builder deliberately exposes three ways to build the same row — a positional "Fast API" for best performance, a "Safe API" that validates field names, and an "Indexed API" balancing the two — so callers pick their own safety/performance tradeoff rather than the crate picking one for them | quote: "Fast API: Best performance, positional values / Safe API: Validates field names / Indexed API: Uses index for balance of safety and speed" | practiced_evidence: none (names the crate greptimedb-ingester-rust for its benchmark tool but gives no URL)

## f012963 — GitHub search: open unsafe-code-guidelines issues labeled final-comment-period
### Nothing new
UNREACHABLE: the URL is a GitHub search query for open issues tagged `final-comment-period`; the fetched text is only the repository's static README (purpose, links to the UCG book/glossary/Rustonomicon, code-of-conduct notice), not the search results the URL requests — no actual FCP issue content was retrieved, so nothing can be extracted from this fetch.
