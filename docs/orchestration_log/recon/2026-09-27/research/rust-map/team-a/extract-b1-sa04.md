Your job: for each source, where do competent Rust practitioners disagree?

## f002488 — [Pitch] Explicit Specialization (2025-01-02, en)
### Nothing new
A Swift Evolution pitch on explicit generic specialization (`@specialize`) and monomorphization; several commenters compare it at length to Rust's and C++'s ABI-for-monomorphized-generics tradeoffs, but always as commentary on Swift's own design, never as a Rust practitioner's declared Position.

## f002554 — Relationships (non-fragmenting, one-to-many) (2025-01-16, en)
### Questions
- Q: For an ECS relationship system, should the design enforce a single source of truth (only the `Relationship` component is authoritative, the reflected `RelationshipTarget` collection can't be populated directly), accepting that constraint in exchange for O(1) inserts and no runtime duplicate-scanning, or should both sides carry equal, symmetric authority for more flexibility at the cost of scanning/hashing to prevent duplicates?
  concepts: ECS, relationships, source of truth, API surface, performance; domains_live: desktop-cli-ui; positions_seen: single-source-of-truth (PR author), symmetric-source-of-truth (contrasted `evergreen_relations` approach, same source)
### Claims
- voice: cart | position: single-source-of-truth-relationship | date: 2025-01-16 | locator: PR description, "Relationships are the source of truth" section | paraphrase: argues `Relationship` should be the sole source of truth so `RelationshipTarget` is a pure reflection, accepting that populated target collections can't be spawned directly, in exchange for O(1) inserts and no runtime duplicate-scanning; contrasts this with a symmetric two-sided design (`evergreen_relations`) that needs scanning/hashing to prevent duplicates | quote: "We can rely on component lifecycles to protect us against duplicates, rather than needing to scan at runtime to ensure entities don't already exist (which results in quadratic runtime)." | practiced_evidence: https://github.com/bevyengine/bevy/pull/17398

## f002643 — How to Build GitHub Copilot Extensions (2025-02-06, en)
### Nothing new
A Python/FastAPI tutorial on building a GitHub Copilot extension server; no Rust content.

## f002665 — Update On FFI Bindings (2025-02-12, en)
### Questions
- Q: When a Rust library's non-Rust-language FFI bindings lag behind the quality of its native Rust API, should maintainers keep shipping degraded bindings on every release, or pause bindings updates until the FFI/bridging story itself is fixed, accepting ecosystem-fragmentation risk in the meantime?
  concepts: FFI, UniFFI, multi-language bindings, ecosystem fragmentation; domains_live: decentralized-iroh; swift-interop; positions_seen: pause-and-fix-ffi-first (author/iroh maintainers)
### Claims
- voice: b5 | position: pause-and-fix-ffi-first | date: 2025-02-12 | locator: opening section ("Why?") | paraphrase: announces iroh will stop updating its Kotlin/Python/Swift/JavaScript FFI bindings on every release because the FFI experience doesn't yet match the "just works" bar the project holds Rust usage to, and because degraded bindings risk fragmenting the protocol ecosystem across languages | quote: "Because we don't think our FFI story is good enough right now. Our promise is to ship \"P2P that works\", and we're not hitting that \"just works\" experience in languages that aren't rust." | practiced_evidence: https://github.com/n0-computer/iroh-ffi; https://github.com/n0-computer/iroh

## f002685 — javascript event loop becomes extremly slow in wayland (2025-02-18, en)
### Nothing new
A collaborative debugging thread (a `winit`/Wayland `ControlFlow`-vs-`pump_events` blocking bug affecting a Node.js embedding of Slint) that converges to an agreed narrow fix; no persisting contested Position between practitioners.

## f002865 — [embassy-executor]: Upstream "Earliest Deadline First" Scheduler (2025-04-01, en)
### Questions
- Q: For a foundational, safety-critical embedded component like an async executor's run queue, should the project depend on an external, well-tested intrusive-data-structure crate (with miri/loom coverage and cross-project shared maintenance), or keep a minimal, self-contained hand-rolled implementation to minimize dependency surface and cross-repo coordination?
  concepts: dependency management, intrusive data structures, unsafe code, embedded executors, miri, loom; domains_live: embedded; positions_seen: adopt-external-tested-dependency (PR author), keep-self-contained-hand-rolled (reviewer)
### Claims
- voice: jamesmunns | position: adopt-cordyceps-dependency | date: 2025-04-01 | locator: PR comment ("I'd like to try and make the case for keeping the cordyceps dependency!") | paraphrase: argues embassy-executor should keep the `cordyceps` dependency rather than hand-roll/vendor the data structures, citing its miri+loom test coverage, shared usage and maintenance with the `maitake` executor, and tested user APIs that reduce unsafe surface area | quote: "Cordyceps is fairly exhaustively tested, with both miri and loom, which helps to avoid regressions potentially caused by changes." | practiced_evidence: https://github.com/embassy-rs/embassy/pull/4035; https://crates.io/crates/cordyceps
- voice: Dirbaio | position: keep-self-contained-hand-rolled | date: 2025-04-01 | locator: PR comment ("Some concerns") | paraphrase: objects to adding `cordyceps` as a dependency for something as foundational as the executor, preferring the data structures stay self-contained and in-tree so the project can change them without cross-repo coordination, keeping the abstraction surface minimal | quote: "I don't think we should add `cordyceps` as a dep, I'd prefer to keep the data structures self-contained for something as foundational as the executor. Having it all in-tree means we can make changes as needed without having to coordinate across repos, and less abstraction means it's clearer what's going on in this case IMO." | practiced_evidence: https://github.com/embassy-rs/embassy/pull/4035

## f002883 — Workaround for a TextDecoder bug in Safari causing a RangeError to be thrown (2025-04-06, en)
### Nothing new
A bug-workaround PR (Safari `TextDecoder`'s 2GiB decode limit) with collaborative, converging refinement of an empirical safety margin; no contested design point between practitioners.
