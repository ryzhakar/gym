For each source: where do competent Rust practitioners disagree?

## f004173 — SP-001: Platform Support Levels (2026-01-28, en)

### Nothing new
nothing new — the thread's contested points (Linux as one Tier 1 platform vs per-distribution/triple tiers; Foundation/Dispatch/Swift Testing/DocC as hard vs soft Tier 1 requirements; PR testing blocking merges) are Swift-project governance decisions no Rust practitioner makes, and its three Rust mentions are descriptions of Rust, not declared Positions: @bclee 2026-02-03T23:22:11Z ("Rust, in contrast, largely relies on libc and otherwise ships a mostly self-contained toolchain"), @FranzBusch 2026-02-03T23:40:54Z (Rust specifies a minimum kernel and glibc version), @FranzBusch 2026-02-21T12:05:18Z (cites Rustup package availability as a model for Swift).

Read note: 72/72 visible posts match Discourse posts_count 72. One post is deleted (highest_post_number 73). A 3405691582 post quoted by @al45tair at 2026-02-10T15:00:52Z ("Should we explicitly say what happens when a change breaks a Tier 2 platform?") is not in the thread text.

## f004174 — What is ~Copyable for? (2026-01-28, en)

### Nothing new
nothing new — every contested point (destructor versus consuming close for fallible or async release, reference-counting cost versus unique ownership, typestate through consuming methods versus runtime checks, movable locks) is argued by Swift Voices about Swift's `~Copyable`, `deinit` and ARC, which rule 9 bars mapping onto Rust Questions. The two posts that name Rust come from Voices whose Rust connection does not show in the source. @Nobody1707 2026-01-29T22:01:36Z is an opinion on Rust's design with no Rust use stated: "I'm honestly not convinced that Rust was wrong in making Copy a refinement of Clone". @jrose 2026-02-14T20:56:00Z states a fact, not a side: "Rust atomics and std::sync::Mutex both allow moving". @ben-cohen 2026-01-29T17:05:23Z names Rust's RefCell only as a model for a Swift library type.

Read note: 54/54 visible posts match Discourse posts_count 54. One post is deleted (highest_post_number 55). @jrose 2026-01-29T04:54:34Z ("How so? (genuine!)") answers a post not in the thread text. Superseded: an earlier version of this section logged 5 Questions and 24 Claims by mapping Swift arguments onto Rust. The lead's clarifications and rules 8–9 of 2026-09-27 withdrew them.
