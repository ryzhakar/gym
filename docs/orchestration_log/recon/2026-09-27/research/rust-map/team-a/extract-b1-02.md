Your job: for each source, where do competent Rust practitioners disagree?

## f000801 — semantic search (2024-01-24, en)
### Nothing new
A TypeScript/Next.js tutorial on OpenAI embeddings and Postgres vector search (pg_embedding); no Rust content at all.

## f000957 — Introduce a new use_async hook, that allows for setting dependencies (2024-02-20, en)
### Questions
- Q: When designing an async-computation hook API, should cancellation semantics be committed to upfront even at the cost of a larger initial API surface, or postponed until real usage demonstrates the need?
  concepts: async hooks, API stability, premature generality; domains_live: frontend; positions_seen: ship-minimal-now (author), commit-upfront (implicit alternative the author argues against)
### Claims
- voice: Ekleog | position: ship-minimal-now | date: 2024-02-20 | locator: PR description | paraphrase: argues the initial `use_async` hook should ship without baking in cancellation semantics, since Yew isn't stable yet and the design likely covers ~90% of use cases; cancellation can be added later as a variant if real need emerges | quote: "Yew is not stable yet, and probably at least 90% of the use cases are covered by this API, so I think it makes sense to postpone the decision after verifying that there is an actual need." | practiced_evidence: https://github.com/Ekleog/crdb/commit/2ed2777a607b894c3aa1e93e6584c33be27b6679

## f000977 — Add support for `Option<*const T>`, `Option<*mut T>` and `NonNull<T>` (2024-02-23, en)
### Questions
- Q: In FFI/wasm-bindgen-style APIs, should a safety-encoding wrapper type like `NonNull<T>` be accepted as a parameter even when it forces a runtime null check, or should the API stick to raw pointer types to avoid the check?
  concepts: FFI, NonNull, runtime checks, API surface; domains_live: wasm; positions_seen: avoid-runtime-check (author), accept-runtime-check-for-safety (implicit alternative)
### Claims
- voice: daxpedda | position: avoid-runtime-null-check | date: 2024-02-23 | locator: PR body (top comment) | paraphrase: deliberately did not implement taking `NonNull<T>` as a parameter in the new atomic-pointer API, specifically to avoid adding a runtime check | quote: "I specifically didn't implement taking `NonNull<T>` as a parameter to avoid having to add a runtime check somewhere." | practiced_evidence: https://github.com/wasm-bindgen/wasm-bindgen/pull/3852

## f000993 — Dynamic tensors; `TensorContainer` refactor (2024-02-25, en)
### Questions
- Q: When a large refactor PR introducing new foundational abstractions grows invasive and disruptive, should it land as one big PR, or be broken into smaller, incrementally mergeable chunks?
  concepts: refactor scope, code review process, engineering culture; domains_live: ml; positions_seen: ship-as-one-large-PR (PR author, opened "mainly to instigate discussion"), break-into-smaller-chunks (reviewer, unattributed)
- Q: Should a generic tensor-container abstraction enforce a single uniform tensor type across backends, or allow different backends/precisions to coexist within the same container to support mixed-precision training and multi-backend graphs?
  concepts: generics, tensor containers, mixed precision, backend abstraction; domains_live: ml; positions_seen: enforce-uniform-type (implied by author's redesign attempts), allow-backend-flexibility (reviewer's stated goal, unattributed)
### Claims
- voice: miestrode | position: refactor-now-for-serialization | date: 2024-02-25 | locator: PR description ("Changes" section) | paraphrase: argues `TensorContainer`'s current design is a mess that blocks serialization needed for applications like sending `GradientsParams` over the wire, and opened the PR mainly to instigate discussion on a foundational redesign even though its API is still unstable | quote: "TensorContainer is a bit of a mess. It's code needs a refactor, and it's current design prevents some important things, such as deserializing and serializing it, which is needed for many applications, such as passing GradientsParams over the wire." | practiced_evidence: https://github.com/tracel-ai/burn/pull/1362

## f001053 — persistent structures in neons wal indexing (2024-03-01, en)
### Questions
- Q: For performance-critical, correctness-sensitive infrastructure code, should teams reach for an existing (if less popular) persistent-data-structure crate, or hand-roll a bespoke specialized data structure for maximum control and performance?
  concepts: persistent/immutable data structures, library adoption, build-vs-buy; domains_live: distributed; core; positions_seen: adopt-existing-crate (author/Neon), hand-roll-bespoke-structure (same source's own rejected "failed attempt" path)
### Claims
- voice: Bojan Serafimov | position: reach-for-existing-persistent-data-structure-crate | date: 2024-03-01 | locator: "Rust Persistent Data Structures (RPDS) to the rescue" / "Conclusion" sections | paraphrase: rather than hand-roll a balanced 2D segment tree with lazy propagation, the team reached for the `rpds` crate to build a copy-on-write layer map, crediting it over more popular alternatives | quote: "There are more popular persistent data structure libraries in Rust, but this one deserves a lot more credit for its clean API, correct results (!!!), and more than good enough performance." | practiced_evidence: https://github.com/neondatabase/neon

## f001071 — Icon extensions (2024-03-04, en)
### Nothing new
A general open-source roadmap/aesthetic-vs-community-demand dispute over Zed's icon UX; not specific to Rust language or practice, and no comment in the thread is attributable to a named Voice.

## f001094 — SE-0427: Noncopyable Generics (2024-03-08, en)
### Nothing new
A Swift Evolution proposal review of Swift's own Copyable/generics syntax; Rust appears only as passing analogy by Swift community members (var/let history, macro constraints, `?Copyable` aping Rust syntax), never as a Rust practitioner's own declared Position.

## f001096 — Metal: Improved reduce and softmax (2024-03-08, en)
### Nothing new
A numerical-correctness bug hunt and benchmarking collaboration on a Metal backend kernel; no contested design point is argued.

## f001181 — Cranelift: implement "precise store traps" in presence of store-tearing hardware. (2024-03-22, en)
### Questions
- Q: On hardware with "store-tearing" behavior, where a partial store can have observable side effects before trapping, should a WebAssembly runtime pay a load-before-store performance cost to guarantee precise, spec-compliant trap semantics, or accept imprecise traps as an acceptable, mostly theoretical risk on rare/low-power hardware?
  concepts: Cranelift, trap semantics, memory safety, WebAssembly spec compliance, store tearing; domains_live: wasm; embedded; positions_seen: pay-for-precise-traps-opt-in (PR author), accept-imprecision-as-practically-irrelevant-on-tier1 (discussion converges toward this for production hardware, unattributed)
### Claims
- voice: cfallin | position: load-before-store-opt-in | date: 2024-03-22 | locator: PR description | paraphrase: implements precise store-trap semantics (prepending a same-size load before every store) on architectures with store tearing (ARMv8, RISC-V), shipped off by default, accepting a measured ~2% cost on Apple M2 Pro, pending Wasm spec clarification | quote: "This PR implements the idea first proposed [...] namely to prepend a load of the same size to every store. The idea is that if the store will trap, the load will as well." | practiced_evidence: https://github.com/bytecodealliance/wasmtime/pull/8221

## f001231 — Dynamic Component Id type (2024-03-30, en)
### Questions
- Q: Should runtime-registered ("dynamic") ECS components carry a compile-time type witness (a typed ID wrapper constrained to `T: Component`) for safe access, or stay untyped so that scripting/runtime-defined component variants aren't forced into newtyping?
  concepts: ECS, dynamic typing, phantom types, unsafe code; domains_live: desktop-cli-ui; positions_seen: typed-witness-wrapper (PR author), untyped-for-flexibility (reviewer, unattributed)
### Claims
- voice: ecoskey | position: typed-wrapper-for-safety | date: 2024-03-30 | locator: PR description ("Objective"/"Solution") | paraphrase: proposes wrapping dynamic `ComponentId`s in a typed `TypedComponentId<T>` witness so dynamic component access can be done safely, instead of manual pointer work and unsafe code | quote: "Add a wrapper around ComponentId with a type parameter T to act as a witness that that id corresponds to a component with type T. This allows registering multiple components with the same underlying type, that dynamic queries can access separately in a safe way." | practiced_evidence: https://github.com/bevyengine/bevy/pull/12794; later published independently as https://crates.io/bevy_dyn_component

## f001244 — nextjs authentication using clerk drizzle orm and neon (2024-04-02, en)
### Nothing new
A TypeScript/Next.js tutorial on Clerk auth and Drizzle ORM; no Rust content at all.

## f001271 — Qdrant Hybrid Cloud and Haystack for Enterprise RAG (2024-04-10, en)
### Nothing new
A partnership/product announcement (Qdrant Hybrid Cloud plus Haystack); no contested point, no Rust content beyond Qdrant being written in Rust.

## f001319 — Iroh 0.14.0 - Dial the world (2024-04-18, en)
### Nothing new
A release-announcement blog post (changelog: DNS node discovery, faster relay handshakes, Basic Author API, redb upgrade); no contested design point is argued.

## f001531 — how to create previews with anonymized production-like data in seconds (2024-05-28, en)
### Nothing new
A product-integration announcement (Neon plus Neosync anonymization); no Rust content.

## f001578 — add an interface to your neon database via outerbase (2024-06-07, en)
### Nothing new
A product-integration announcement (Neon plus Outerbase); no Rust content.
