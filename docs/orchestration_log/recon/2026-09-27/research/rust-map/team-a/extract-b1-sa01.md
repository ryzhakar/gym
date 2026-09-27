Framing: For each source, where do competent Rust practitioners disagree?

Source: RECON/samples/bundles/b1-team-a-01.txt (already fetched; read from bundle, not re-fetched). Note on dates: the one gh-api-thread source (f001838) strips per-comment usernames/timestamps in its plain text, keeping only the PR's own date and explicit `@mentions`; where a Claim's voice is not self-signed or unambiguously named, no Claim is written — only a `positions_seen` label — and the Claim date used is the source's own date, not an individual comment timestamp.

## f001650 — iroh 0.19.0 - Make it your own (2024-06-27, en)
### Nothing new
`nothing new` — single-author release-notes blog post (by ramfox); announces features and breaking changes, no contested point or opposing position appears.

## f001677 — [Proposal] Set literals (2024-07-04, en)
### Nothing new
`nothing new` — full 817-line Swift forum thread read (plus a targeted re-scan for "rust"/"crate"/"cargo"/"borrow"); it is an extensive Swift community debate over Set-literal syntax, Set vs. Array performance and ergonomics, but every participant speaks as a Swift practitioner; the sole Rust reference is a one-line aside comparing semicolon-omission rules, not a claim by a Rust practitioner; out of subject for the Rust map.

## f001837 — Why do not actor-isolated properties support 'await' setter? (2024-08-09, en)
### Nothing new
`nothing new` — Swift Concurrency forum thread (actor property mutation, async setters, isolation vs. access control) read in full and re-scanned for "rust"/"crate"/"cargo"/"borrow"; the sole Rust reference is a one-line analogy ("the case with Rust borrow-checker... now that's the case with Swift Concurrency"), not a claim by a Rust practitioner; out of subject for the Rust map.

## f001838 — Initial rp235x support (2024-08-09, en)
### Questions
- Q: When an embedded Rust project adds support for a new, closely related microcontroller variant (here, rp2350 alongside the existing rp2040) via a peripheral-access crate (PAC), should each chip variant get its own separate PAC crate (the `nrfxxx-pac` pattern), or should variants share one PAC crate gated by Cargo features (the `stm32-metapac`/`rp-pac` pattern)?
  concepts: peripheral-access crates (PAC), Cargo features, code generation (chiptool), embedded HAL crate organization; domains_live: embedded; positions_seen: reviewer (unattributed) — one shared PAC crate per chip family, gated by features, is easier to release and maintain; CBJamo (PR author) — initially organizing per chip, then adopting the shared-crate approach once shown it was feasible
### Claims
- voice: CBJamo | position: adopts a single shared PAC crate covering both chip variants, gated by Cargo features, rather than a separate crate per chip | date: 2024-08-09 | locator: PR comment, mid-thread (rp-pac#5 follow-up) | paraphrase: After a reviewer argued for the `stm32-metapac` pattern (one PAC crate covering related chips, feature-gated) over separate per-chip crates, the PR author reports it was easier than expected and that Cargo features "cleaned up" once unified into a single `rp-pac`. | quote: "I had assumed it'd be hard to do, but it wasn't too bad. I just updated the update.sh to make both and hand wrote a tiny lib.rs. Features did indeed clean up with the single pac." | practiced_evidence: embassy-rs/rp-pac#5 (their own follow-up implementing it)

## f001903 — Can we make Swift 6 easier? (2024-08-22, en)
### Nothing new
`nothing new` — Swift community thread on Swift 6's learning curve, re-scanned for "rust"/"crate"/"cargo"/"borrow"; the sole Rust reference is a one-line comparison of Rust's borrow-checker learning curve to Swift Concurrency's, not a claim by a Rust practitioner; out of subject for the Rust map.

## f001981 — iroh 0.24.0 - Upgrading to Quinn 11 (2024-09-04, en)
### Nothing new
`nothing new` — single-author release-notes blog post (by matheus23); reports a dependency upgrade, API/breaking changes and benchmark numbers, no contested point or opposing position appears.
