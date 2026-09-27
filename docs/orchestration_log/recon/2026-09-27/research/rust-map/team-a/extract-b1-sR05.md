## f001837 — Why do not actor-isolated properties support 'await' setter? (2024-08-09, English)

### Questions

None.

### Claims

None.

### Nothing new

`nothing new` — all 45 posts are Swift community/compiler-team voices (vns, ktoso, Andropov, taylorswift, tclementdev, nkbelov, et al.) debating Swift actor isolation, async setters, and locks vs. actors; Rust is invoked twice, both as a passing analogy by a non-Rust voice (vns, on the borrow-checker's learning curve and "fighting the compiler"), never a declared Position by a Voice with a Rust track record.

## f001903 — Can we make Swift 6 easier? (2024-08-22, English)

### Questions

None.

### Claims

None.

### Nothing new

`nothing new` — the thread is entirely about Swift 6's concurrency-checking ergonomics (embedded mode, RemObjects' Silver compiler, adoption friction); the one Rust mention (vns, comparing the borrow checker's steep-then-flat learning curve to Swift's progressive disclosure) is again a non-Rust voice's passing analogy, not a declared Position by a Rust-track-record Voice.

## f001981 — iroh 0.24.0 - Upgrading to Quinn 11 (2024-09-04, English)

### Questions

- Q: Should an async QUIC accept loop treat an individual incoming-connection failure as fatal, or log it and keep serving?
  concepts: error handling, accept loops, async I/O; domains_live: distributed; decentralized-iroh; positions_seen: non-fatal, log-and-continue

- Q: Should a Rust library actively chase down and eliminate duplicate transitive dependency versions (e.g., two copies of `rustls`) in its dependency tree?
  concepts: dependency management, crate ecosystem bloat, semver; domains_live: decentralized-iroh; core; positions_seen: actively reduce duplication via upgrades

### Claims

- voice: matheus23 (iroh maintainer, n0) | position: non-fatal, log-and-continue on accept errors | date: 2024-09-04 | locator: "API Changes" section | paraphrase: `Incoming::accept` can fail for benign network reasons; such failures should be logged and passed over, not treated as fatal | quote: "don't treat errors there as fatal" | practiced_evidence: https://github.com/n0-computer/iroh (repo the changelog documents)

- voice: matheus23 (iroh maintainer, n0) | position: actively reduce duplicated transitive dependencies by upgrading | date: 2024-09-04 | locator: "🤝 Transitive dependencies" section | paraphrase: upgrading iroh's `quinn` dependency was valued because it let iroh drop duplicated copies of shared dependencies, shrinking its overall dependency footprint | quote: "we were generally able to reduce duplicated dependencies" | practiced_evidence: https://github.com/n0-computer/iroh/releases/tag/v0.24.0
