For each source: what must a Rust practitioner decide, and where do the sources conflict on it?

## f000763 — ratatui/ratatui PR #840 (2024-01-17, domain: desktop-cli-ui)

Questions and Claims.

- Question: in example/demo code, should tabular data be modeled with a dedicated domain struct or with generic collections (`Vec<Vec<String>>`)?
  - Claim — Voice: joshka (ratatui maintainer). Position: prefer a small dedicated struct even at the cost of extra ceremony, to show real-world data mapping.
    Quote: "What about adding a small struct that has name, address, email and which gets generated in the app constructor instead of Vec<Vec<String>>? ... Obviously this is just gold plating things at this point. But it does give a nice way of showing how to map real world data into table columns."
    Values: correctness/clarity vs. simplicity. Source: ratatui/ratatui#840, comment 2024-01-18T22:51:17Z. Locator: L424-L442.

- Question: should derived per-column values be computed in a single iterator pass or via several simpler passes/collects?
  - Claim — Voice: joshka. Position: prefer single-pass computation over iterating a collected result multiple times.
    Quote: "If you're iterating and collecting then iterating on the result 3 times or might be neater to iterate and collect the max for each column in a single iteration."
    Values: performance, simplicity. Source: ratatui/ratatui#840, comment 2024-01-18T22:33:34Z. Locator: L403-L406.

- Question: should match arms on an enum use a local glob import (`use Enum::*;`) to drop the type-qualified path, or keep variants fully qualified?
  - Claim — Voice: joshka. Position: favors the local glob import for terser match arms.
    Quote: "And add a `use KeyCode::*;` above this (inside the method) to drop the `Keycode::` from each."
    Values: simplicity/ergonomics vs. explicitness. Source: ratatui/ratatui#840, comment 2024-01-18T01:32:39Z. Locator: L125-L136.

Gap: the PR's actual merged code was not diffed against these suggestions; whether each Position was adopted in the shipped example is not established from this thread alone.

## f000889 — Bytecode Alliance, Plumber's Summit Day 2 (2024-02-05, domain: wasm)

Third-party recap of a conference, not a primary transcript; most content is paraphrase without the speakers' own words, so most of it fails the Claim bar (no direct declaration).

- Question: before a spec (WASI 0.3 async) is finalized, should the ecosystem ship stopgap/polyfill implementations to unblock development, or wait for the finished standard?
  - Claim — Voice: Joel Dice (Fermyon, component-model/wasmtime contributor). Position: favors shipping a polyfill ahead of the spec.
    Quote (his own words, quoted in the recap): a "'polyfill' that devs can play with today while they're waiting for WASI 0.3 and real async."
    Values: iteration speed vs. waiting for a stable, correct standard. Source: bytecodealliance.org/articles/plumbers-day-2, "Async and WASI 0.3" section, talk timestamp 1:11:00. Locator: L465-L472.

- Question noted, no Claim: "what is the single source of truth for WIT packages" (binary artifacts from WIT snapshots vs. other registry designs) — resolved to a "consensus" attributed to the group as a whole, not to a named Voice's own words; not loggable as a Claim under this source.

## f000896 — Swift forums, "[Pitch] Synchronous Mutual Exclusion Lock" (2024-02-06 → 2024-02-20, domain: swift-interop)

Nothing new. Reason: read in full (a long, active thread); it repeatedly invokes Rust's `Mutex`/`MutexGuard` as design precedent (e.g. gwendal.roue and Joe_Groff comparing lifetime-scoped guards to Rust's `LockGuard<'a, T>`), but every participant is a Swift-side voice (Apple/Swift-core engineers, forum regulars) with no established Rust track record per scope (no crate, no Rust production use, no Rust project role, no Rust book/talk/post cited). No Voice qualifies to anchor a Rust Claim, so the source yields no Rust map content despite being Rust-adjacent.

## f000981 — Materialize blog, "What is Data Freshness" (2024-02-23, domain: distributed)

Nothing new. Reason: marketing copy about an operational data warehouse; no Rust-specific content, no named Voice, no Position on any Rust practitioner decision (Materialize's Rust implementation is never discussed).

## f001085 — zed-industries/zed PR #8952 (2024-03-06 → 2024-03-28, domain: desktop-cli-ui)

Nothing new. Reason: a first-time contributor (xyzqm) is mentored end-to-end by a Zed maintainer (SomeoneToIgnore) through one codebase's internal plumbing (macOS dock-menu wiring, `Platform`/`AppContext`/`Workspace`/`Worktree` layering). The advice ("invert control," add a setter on a trait, wire it up where the workspace initializes) is generic software-architecture guidance applied to this one PR, not a Position on a Question where Rust practitioners generally disagree; nothing here rises above project-local implementation detail.

## f001160 — wasm-bindgen/wasm-bindgen PR #3898 (2024-03-19 → 2024-04-03, domain: wasm)

Questions and Claims.

- Question: should a library accept an uglier, more special-cased implementation to avoid growing its dependency footprint (here, avoiding the `syn` "extra-traits" feature)?
  - Claim — Voice: daxpedda (wasm-bindgen maintainer). Position: accept the uglier code; minimizing dependencies matters more.
    Quote: "This is pretty ugly indeed, but I think it's very important for a library like `wasm-bindgen` to reduce its dependency footprint."
    Values: minimalism/dependency footprint vs. code quality/maintainability. Source: wasm-bindgen/wasm-bindgen#3898, comment 2024-04-03T06:30:56Z. Locator: L2338-L2341.

- Question: should a codegen tool trade a larger generated-output size for better runtime performance?
  - Claim — Voice: daxpedda. Position: favors performance over output size for this change.
    Quote (his proposed changelog wording): "Generate JS bindings for WebIDL dictionary setters instead of using `Reflect`. This increases the size of the Web API bindings but should be more performant."
    Values: performance vs. footprint/size. Source: wasm-bindgen/wasm-bindgen#3898, comment 2024-04-03T06:33:18Z. Locator: L2343-L2347.

## f001206 — mozilla/uniffi-rs issue #2051 (2024-03-27 → 2024-03-30, domain: swift-interop)

Nothing new. Reason: a support/bug thread (constructor return-type check regression traced to a `cargo-swift` interop bug); no participant states a Position on a debated Question, only diagnosis of one specific defect.

## f001246 — Neon blog, "Neon Developer Days 1" (2024-04-03, domain: cloud-workers)

Nothing new. Reason: a short event-announcement post (Dec 2022 virtual meetup); no technical content and no Rust-specific claim of any kind.

Summary: 8 sources read, 0 unreachable. 7 Questions raised (3 ratatui #840, 2 Bytecode Alliance recap, 2 wasm-bindgen #3898), 6 Claims logged (3 ratatui, 1 Bytecode Alliance, 2 wasm-bindgen) across 3 sources; 5 sources verdicted Nothing new, each with its own stated reason rather than a bare "single voice" dismissal.
