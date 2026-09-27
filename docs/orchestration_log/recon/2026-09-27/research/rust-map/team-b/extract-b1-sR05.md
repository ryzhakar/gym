For each source: what must a Rust practitioner decide, and where do the sources conflict on it?

## f001890 — iroh blog, "0.23.0 — Welcoming Node.js to the family" (2024-08-21, domain: decentralized-iroh)

Nothing new. Reason: a release-notes post (ramfox, n0-computer). It documents an API rename (`connection`/`ConnectionInfo` -> `remote`/`RemoteInfo`) motivated by the old name over-promising ("it turns out we were lying to you a bit"), but this is the maintainer correcting their own naming mistake, not a Position on a Question where practitioners in general disagree.

## f001953 — zed-industries/zed issue #17100, "Compare (diff) two files" (2024-08-29 → 2026-05-04, domain: desktop-cli-ui)

Nothing new. Reason: a long user feature-request/duplicate-triage thread about a missing editor feature; no Rust-specific design Position is stated by any maintainer, only user requests and a maintainer (SomeoneToIgnore) pointing at an existing feature.

## f001983 — WebAssembly/component-model PR #393, "Unlocked deps" (2024-09-05 → 2024-10-01, domain: wasm)

Question and Claim.

- Question: should WIT syntax name a dependency-on-implementation with dedicated keywords (`locked-dep`/`unlocked-dep`), or with one generic keyword (`dependency`) whose lock state is inferred from the version syntax that follows it?
  - Claim — Voice: Luke Wagner (Fastly; W3C/Bytecode Alliance component-model co-designer). Position: favors the single `dependency` keyword with locked/unlocked inferred from the trailing syntax, for regularity and to keep vocabulary aligned with how package managers already use the word "dependency."
    Quote: "What if we used just the word 'dependency' and inferred 'locked' vs. 'unlocked'/'range' from the syntax after the `@`." And: "the word 'dependency' is used by package managers and their associated build-config files (e.g., `npm`/`package.json`, `cargo`/`Cargo.toml`, etc) to exclusively refer to *implementations*."
    Values: approachability/consistency vs. explicitness. Source: WebAssembly/component-model#393, comments 2024-09-10T20:00:17Z and 2024-09-11T19:36:18Z. Locator: L406-L465.
  - Note, no Claim: James-Mart (a component-model *user*, not established as a Voice with a Rust track record under this source) separately argued for `specified-dep`; his objection shaped the discussion but doesn't itself qualify as evidence.

## f001990 — Neon blog, "Easy Embeddings Indexing Pipelines with Redpanda and Neon" (2024-09-06, domain: distributed)

Nothing new. Reason: a no-code data-pipeline tutorial (Redpanda Connect + Ollama + Neon/pgvector); no Rust-specific content or Voice.

## f002048 — tracel-ai/burn PR #2287, "Introduce autotuning to conv2d/conv_transpose2d with im2col/GEMM" (2024-09-17 → 2024-09-23, domain: ml)

Questions and Claims.

- Question: should a numerics/kernel library ship one fixed algorithm per operation, or ship several algorithm implementations and autotune between them at runtime?
  - Claim — Voice: wingertge (PR author, tracel-ai/burn contributor). Position: ship multiple algorithms (existing "direct" plus a new `im2col`/GEMM path) and autotune, even though the new path trades memory for speed.
    Quote: "Adds the required infrastructure to autotune `conv2d` and `conv_transpose2d`, as well as adding a second algorithm based on `im2col` which provides significant speedups at the cost of memory usage."
    Values: performance vs. memory footprint. Source: tracel-ai/burn#2287, PR description, 2024-09-17T15:20:57Z. Locator: L853-L865.

- Question: should hardware/backend-specific magic numbers used in a GPU kernel be hardcoded inline, or threaded through as a comptime-configurable parameter?
  - Claim — Voice: louisfd (tracel-ai/burn maintainer). Position: hardcode for now but pass the values through a comptime struct so a future backend-specific change (e.g. a different warp/wavefront size on AMD) doesn't require touching the kernel body.
    Quote: "I think it's fine to hardcode these values for now, but they should be passed to the cube kernel via a comptime struct, because the day they will change (for amd it's 64 for instance) we won't have to change the kernels, just the launch."
    Values: portability/maintainability vs. immediate simplicity. Source: tracel-ai/burn#2287, comment 2024-09-23T14:26:38Z. Locator: L977-L979.

## f002151 — leptos-rs/leptos PR #3063, "wasm32-wasip1/2 first-class citizen for SSR" (2024-10-05 → 2024-11-02, domain: wasm)

Questions and Claims.

- Question: should a young, platform-specific integration (e.g. a new deploy target) live in-tree in a project's core crates, or ship as a separate out-of-tree crate?
  - Claim — Voice: benwis (Leptos maintainer). Position: keep new integrations out of the main crates.
    Quote: "We're keeping most new integrations out of the main crates to reduce the time needed to release a new feature."
    Values: iteration speed/release velocity vs. cohesion/discoverability. Source: leptos-rs/leptos#3063, comment 2024-10-06T02:05:17Z. Locator: L1097-L1100.

- Question: should platform-specific code be gated behind a Cargo feature flag, or behind a `#[cfg(target...)]`/target-triple check once the platform is a proper Rust target?
  - Claim — Voice: brooksmtownsend (wasmCloud engineer; contributor to mio/tokio-rs WASI socket support). Position: prefer target-based gating over feature flags once the target is stabilized.
    Quote: "Once `wasm32-wasip2` is a stable target in Rust (coming in 1.82 afaik) the use of feature flags could be simplified, using the target directive instead."
    Values: simplicity/correctness vs. the flexibility of feature flags. Source: leptos-rs/leptos#3063, comment 2024-10-11T13:37:26Z. Locator: L1290-L1291.

## f002177 — n0-computer/iroh issue #2799, "Tracking: WebAssembly support for iroh" (2024-10-10 → 2026-04-27, domain: decentralized-iroh)

Question and Claim.

- Question: when compiling an async networking stack to a non-native target, should you swap the async runtime/networking primitives for target-specific shims, or keep the existing runtime (tokio) and target a platform that can host it directly?
  - Claim — Voice: matheus23 (n0-computer/iroh maintainer). Position: the two Wasm targets warrant different answers — swap out tokio for a browser shim when targeting `wasm32-unknown-unknown`, but for `wasm32-wasip2/3` compile most of the stack unchanged and depend on tokio gaining support for that platform instead.
    Quote: "Instead of swapping out tokio with another runtime (wasm-bindgen-futures/'the browser' in that case)... we'd instead try to compile most of the stack to wasm32-wasip2/3... So this means we'd be dependent on tokio to work under that platform and for it to support UDP/TCP sockets."
    Values: portability/code-reuse vs. adapting to each platform's constraints. Source: n0-computer/iroh#2799, comment 2026-04-27T08:40:49Z. Locator: L1518-L1524.

## f002233 — iroh blog, "0.27.0 — Squashing Bugs and Taking Names" (2024-10-24, domain: decentralized-iroh)

Nothing new. Reason: a bug-fix/changelog release post (ramfox); config and API cleanups are described but none is framed as a Position against a competing view.

## f002301 — bevyengine/bevy PR #16340, "Add unregister_system command" (2024-11-11 → 2024-11-12, domain: core)

Nothing new. Reason: a naming-consistency fix scoped to one crate's internal API (`remove_system` renamed to `unregister_system` to pair with `register_system`/`add_systems`); this is project-local API bikeshedding, not a Question where Rust practitioners at large disagree.

## f002326 — esp-rs/esp-hal PR #2546, "Auto-initialize PSRAM" (2024-11-15 → 2025-01-26, domain: embedded)

Question and Claim.

- Question: should a crate's naming for a raw-pointer-plus-length accessor follow std's `raw_parts`/`from_raw_parts` convention even where the analogy is imperfect (no matching `into_raw_parts` exists here), or invent its own name when the fit is inexact?
  - Claim — Voice: bugadani (esp-hal maintainer). Position: reuse the `raw_parts`-style name anyway; std's convention doesn't have to apply exactly to a non-std crate.
    Quote: "`raw_parts` works, I decided against it because there is no 'into_raw_parts', just 'from_raw_parts'. But we are also not the standard library, so I guess it's okay if the pattern doesn't apply to us."
    Values: consistency-with-std vs. precise fit to the local case. Source: esp-rs/esp-hal#2546, comment 2024-11-23T13:48:41Z. Locator: L1903-L1905.

## f002341 — iroh blog, "Relay outage: A post-mortem" (2024-11-19, domain: distributed)

Question and Claim.

- Question: can a service written in Rust rely on the language's memory-safety guarantees to prevent resource leaks in a long-running process, or must leak detection be engineered separately?
  - Claim — Voice: Arqu (n0-computer/iroh engineer, production post-mortem author). Position: safety guarantees are not sufficient; the team had to add load simulation, profiling and explicit fixes for two separate leaked-task/thread bugs, and states the gap outright.
    Quote: "Rust's memory safety guarantees do not mitigate memory leaks."
    Values: correctness/reliability vs. an unearned trust in language guarantees. Source: iroh.computer/blog/relay-down-a-post-mortem, "The Nitty Gritty" section, 2024-11-19. Locator: L1958-L1971.

## f002453 — iroh blog, "0.30.0 — Slimming Down" (2024-12-17, domain: decentralized-iroh)

Questions and Claims.

- Question: should a library accept extra implementation cost/breaking changes to minimize its dependency footprint, or accept more dependencies for convenience/cleanliness? (same Question as raised by daxpedda in wasm-bindgen#3898, batch b1-sR03)
  - Claim — Voice: dignifiedquire (n0-computer/iroh maintainer). Position: actively spend release cycles cutting dependencies ahead of a 1.0 API, even though it means a wave of breaking changes.
    Quote: "Less is more, simpler is better. This release we focused on cleaning up iroh APIs, streamlining the protocol APIs, and reducing our dependency load!" And: "Irohs dependency load is not the smallest, so while preparing the API for 1.0, we are also trying to reduce the number of required dependencies."
    Values: minimalism/dependency footprint vs. convenience. Source: iroh.computer/blog/iroh-0-30-0-slimming-down, 2024-12-17. Locator: L2007-L2097.

- Question: should a public trait's methods require callers to wrap `self` in `Arc` (shared ownership baked into the API), or accept a plain reference/generic `Self` and leave ownership to the caller?
  - Claim — Voice: dignifiedquire. Position: drop the forced `Arc` requirement from `ProtocolHandler` for a more flexible structure.
    Quote: "Previously the `ProtocolHandler` trait required using explicit Arcs, but this is no longer required, allowing for a more flexible structure in defining protocols."
    Values: flexibility/ergonomics vs. the up-front simplicity of a single fixed ownership shape. Source: iroh.computer/blog/iroh-0-30-0-slimming-down, "Simpler ProtocolHandler API" section. Locator: L2098-L2100.

## f002466 — bytecodealliance/wasmtime PR #9889, "Winch: implement fpu to int conversions for aarch64" (2024-12-21 → 2025-01-05, domain: wasm)

Question and Claim.

- Question: should a scratch/temporary resource that the register allocator doesn't track be exposed as an explicit function parameter (composable, flexible), or kept encapsulated with the shortest possible internal live range (safer, harder to misuse)?
  - Claim — Voice: saulecabrera (Bytecode Alliance, Wasmtime Winch baseline-compiler maintainer). Position: minimize the live range and avoid passing scratch registers around as parameters, even if it means redefining signatures and accepting some duplication across ISA-specific paths.
    Quote: "the unintentional clobbering risk is particularly important in the case of scratch registers in Winch: even though they can be used for any purpose, one important detail about them is that they are not tracked by Winch's regalloc therefore they must be used sparingly and with extreme caution... Ideally, the live range of the scratch registers should be as short as possible to avoid potential bugs."
    Values: correctness/safety vs. flexibility/composability. Source: bytecodealliance/wasmtime#9889, comment 2025-01-04T16:38:14Z. Locator: L2288-L2319.

Summary: 13 sources read, 0 unreachable. 11 Questions raised with 11 Claims logged, across 8 sources (component-model#393, burn#2287 ×2, leptos#3063 ×2, iroh#2799, esp-hal#2546, iroh relay post-mortem, iroh 0.30 blog ×2, wasmtime#9889); one dependency-footprint Question reuses the wording from batch b1-sR03's wasm-bindgen finding. 5 sources verdicted Nothing new (changelog/announcement posts with no contested Position, a user feature thread, and one narrow single-crate naming fix), each with its stated reason.
