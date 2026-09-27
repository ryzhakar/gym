# Blind fill input, batch 1, file 04 of 13

For each Claim below, name the one Position of its Question that the Claim supports (a Position id from the list), or `none` if it supports none of them. The Claims are in random order.

## Question `doctests-must-compile`

Should code blocks embedded in Rust doc comments be required to compile as doctests, or is it acceptable to leave illustrative snippets non-compiling?

Positions:
- `doctests-must-compile--p1`: Require all blocks to compile
- `doctests-must-compile--alt1`: Allow illustrative, non-compiling snippets

Claims:
- `a-sR07-f002347-c1` · Voice: BD103 · Source: https://github.com/bevyengine/bevy/pull/16455 (`f002347`) · Date: 2024-12-17 · Locator: comment on CI failures (2024-12-17T17:43:35Z)
  - Quote: "We require all code blocks to be valid Rust, since we treat them as unit tests as well."
  - Paraphrase: Bevy's convention requires every doc-comment code block to be valid, compiling Rust because the project treats them as unit tests too

## Question `downstream-vendor-removed-api-vs-rework`

When a library removes a public API in a major release, should downstream vendor the removed piece or rework its integration, and does the migration cost count against the removal?

Positions:
- `downstream-vendor-removed-api-vs-rework--vendor-removed-trait`: Replicate the dropped trait downstream as a fallback
- `downstream-vendor-removed-api-vs-rework--rework-downstream`: Rework downstream; the cost falls on downstream's own misuse

Claims:
- `b-sT07-f003809-c3` · Voice: comphead · Source: https://github.com/apache/datafusion/issues/18566 (`f003809`) · Date: 2026-01-06 · Locator: comments 2026-01-06T17:13:01Z, 2026-01-06T17:30:28Z
  - Quote: "plan B is to replicate SchemaAdapter in Comet codebase"
  - Paraphrase: the SchemaAdapter removal lengthens Comet's upgrade; plan B is to copy SchemaAdapter into the Comet codebase
- `b-sT07-f003809-c4` · Voice: adriangb · Source: https://github.com/apache/datafusion/issues/18566 (`f003809`) · Date: 2026-01-06 · Locator: comment 2026-01-06T17:17:48Z
  - Quote: "that's mostly on us for doing *horrifying* things in the first place"
  - Paraphrase: Pydantic was hit by the same removal, but because of its own hacky dynamically generated columns filled by SchemaAdapter; offers to work through issues

## Question `durable-job-queue-vs-in-process`

Should scheduled or background jobs in a Rust service run on a durable, database-backed job queue (e.g. apalis with Postgres storage) or on an in-process scheduler whose jobs live only in memory?

Positions:
- `durable-job-queue-vs-in-process--p1`: Durable Postgres-backed job queue
- `durable-job-queue-vs-in-process--alt1`: An in-process scheduler with jobs in memory

Claims:
- `b-sT09-f011688-c1` · Voice: Joshua Mo (Shuttle) · Source: https://shuttle.rs/blog/2024/01/24/writing-cronjobs-rust (`f011688`) · Date: 2024-01-23 · Locator: § Hooking it all up, paragraph 1
  - Quote: "Without durable job queues, our jobs would disappear if our web service has any outages!"
  - Paraphrase: PostgresStorage is set up so the job queue is durable, with the reason that jobs would otherwise be lost when the service has an outage

## Question `dyn-compatibility-rules-relaxation`

How constrained are `dyn Trait`'s object-safety rules, and how likely/soon could they be relaxed (e.g., via higher-ranked generic bounds or a next-generation trait solver)?

Positions:
- `dyn-compatibility-rules-relaxation--p1`: Dyn trait relaxation for this case is far off or never
- `dyn-compatibility-rules-relaxation--p2`: Dyn trait object safety rules are overly constraining

Claims:
- `a-sa30-f013276-c5` · Voice: parasyte — track record not established from this source · Source: https://users.rust-lang.org/t/abstract-factory-trait-with-generic-method/122066 (`f013276`) · Date: 2024-12-06 · Locator: post 2024-12-06T05:54:27.164Z
  - Quote: "I am pessimistic on the outlook of dyn Trait, though. The rules are too constraining and I don't know if it's possible to lift many of them."
  - Paraphrase: expresses pessimism that `dyn Trait`'s object-safety constraints can be substantially relaxed, noting the trait-resolver rewrite ("next-gen trait solver") has been underway since 2015
- `a-sa30-f013276-c1` · Voice: quinedot — track record not established from this source · Source: https://users.rust-lang.org/t/abstract-factory-trait-with-generic-method/122066 (`f013276`) · Date: 2024-12-06 · Locator: post 2024-12-06T01:21:37.914Z
  - Quote: "But we're talking years and years, if ever; probably the dyn equivalent isn't plausible."
  - Paraphrase: sketches a hypothetical higher-ranked-bound `dyn EventStore` that would satisfy the OP's use case, then predicts it is not close, if it ever lands

## Question `dynamic-ecs-component-typed-id`

Should runtime-registered ("dynamic") ECS components carry a compile-time type witness (a typed ID wrapper constrained to `T: Component`) for safe access, or stay untyped so that scripting/runtime-defined component variants aren't forced into newtyping?

Positions:
- `dynamic-ecs-component-typed-id--p1`: Typed wrapper for safety
- `dynamic-ecs-component-typed-id--alt1`: Keep dynamic component ids untyped for flexibility

Claims:
- `a-02-f001231-c1` · Voice: ecoskey · Source: https://github.com/bevyengine/bevy/pull/12794 (`f001231`) · Date: 2024-03-30 · Locator: PR description ("Objective"/"Solution")
  - Quote: "Add a wrapper around ComponentId with a type parameter T to act as a witness that that id corresponds to a component with type T. This allows registering multiple components with the same underlying type, that dynamic queries can access separately in a safe way."
  - Paraphrase: proposes wrapping dynamic `ComponentId`s in a typed `TypedComponentId<T>` witness so dynamic component access can be done safely, instead of manual pointer work and unsafe code

## Question `easy-mode-rust`

When onboarding a team new to Rust on a security-critical project, should you write "easy mode Rust" (owned types instead of borrowed references, `Arc<RwLock<T>>` instead of lock-free structures) to keep the team approachable, or go straight for the most advanced/performant Rust idioms?

Positions:
- `easy-mode-rust--p1`: Tasteful combination favoring easy mode
- `easy-mode-rust--alt1`: Use the most advanced idioms (borrowed references, lock-free structures) from the start

Claims:
- `b-sb24-f011295-c1` · Voice: Sam Cutter · Source: https://youtube.com/watch?v=8n13Oh8c0r4 (`f011295`) · Date: 2025-10-03 · Locator: [12:09]-[13:10]
  - Quote: "In practice, this means instead of strrus containing references to other objects, we prefer our strs to be have owned types. This minimizes borrow checker headaches."
  - Paraphrase: as the first Rust team at the Guardian, they deliberately avoided the most advanced/fastest Rust (lifetimes-heavy, lock-free structures) in favor of owned types and `Arc<RwLock<T>>`, to minimize borrow-checker friction for engineers new to Rust, while keeping the option to refactor toward performance later

## Question `ecs-events-first-architecture`

In a growing Bevy/ECS game, should cross-system state changes flow through an events/observers-first architecture (systems never mutate each other's state directly) rather than direct shared mutable access, accepting the loss of transactional rollback and added boilerplate in exchange for decoupling?

Positions:
- `ecs-events-first-architecture--p1`: Build state changes as an events/observers cascade rather than direct system-to-system mutation, despite losing atomicity
- `ecs-events-first-architecture--alt1`: Direct shared mutable access between systems

Claims:
- `b-sb25-f012561-c1` · Voice: Tristan (solo Rust/Bevy game developer, "Green Fit Heaven") · Source: https://youtube.com/watch?v=_FIDuLV0ZsA (`f012561`) · Date: 2025-06-18 · Locator: ~06:10-09:13
  - Quote: "it breaks atomicity ... if something fails ... you can't roll back the previous event"
  - Paraphrase: modeling every state change (granting XP, playing a sound, updating a tile) as a hierarchy of events made each system easy to reason about in isolation and easy to reuse, at the cost that a failure partway through a cascade can't be rolled back, so every handler has to defensively stop propagation and keep the game in a stable state

## Question `ecs-relationship-fragmenting`

Should ECS relationships be stored as archetype-fragmenting edges (entities with different relationship targets end up in different archetypes, enabling wildcard/nested-join/traversal query operations), or as non-fragmenting components (all related entities can share the same archetype/table, favoring dense cache-friendly iteration for common hierarchical cases)?

Positions:
- `ecs-relationship-fragmenting--p1`: Fragmenting enables more queries
- `ecs-relationship-fragmenting--p2`: Non fragmenting preferred for hierarchies

Claims:
- `b-sb07-f002142-c4` · Voice: nakedible · Source: https://github.com/bevyengine/bevy/pull/15635 (`f002142`) · Date: 2024-10-20 · Locator: PR #15635, comment 2024-10-20T08:31:44Z
  - Quote: "Fragmenting relationships are totally useless for my use cases, and will just lead to one archetype per entity."
  - Paraphrase: states that fragmenting relationships would be useless for their use case and would just produce one archetype per entity, whereas the non-fragmenting, relationship-type-keyed approach in this PR is what they actually need (and reports that a Bevy ECS SME independently suggested the same to them)
- `b-sb07-f002142-c3` · Voice: iiYese · Source: https://github.com/bevyengine/bevy/pull/15635 (`f002142`) · Date: 2024-10-20 · Locator: PR #15635, comment 2024-10-20T11:38:42Z
  - Quote: "You cannot do many query operations when edge information is not exposed at an archetype level."
  - Paraphrase: lists concrete query operations (wildcard queries, named wildcard queries, nested joins, efficient up-traversal, efficient sibling queries) that are only possible when relationship edges are exposed at the archetype level, which this PR's component-based (non-fragmenting) approach does not provide

## Question `ecs-relationship-source-of-truth`

For an ECS relationship system, should the design enforce a single source of truth (only the `Relationship` component is authoritative, the reflected `RelationshipTarget` collection can't be populated directly), accepting that constraint in exchange for O(1) inserts and no runtime duplicate-scanning, or should both sides carry equal, symmetric authority for more flexibility at the cost of scanning/hashing to prevent duplicates?

Positions:
- `ecs-relationship-source-of-truth--p1`: Single source of truth relationship
- `ecs-relationship-source-of-truth--alt1`: Both sides of the relationship carry equal authority

Claims:
- `a-sa04-f002554-c1` · Voice: cart · Source: https://github.com/bevyengine/bevy/pull/17398 (`f002554`) · Date: 2025-01-16 · Locator: PR description, "Relationships are the source of truth" section
  - Quote: "We can rely on component lifecycles to protect us against duplicates, rather than needing to scan at runtime to ensure entities don't already exist (which results in quadratic runtime)."
  - Paraphrase: argues `Relationship` should be the sole source of truth so `RelationshipTarget` is a pure reflection, accepting that populated target collections can't be spawned directly, in exchange for O(1) inserts and no runtime duplicate-scanning; contrasts this with a symmetric two-sided design (`evergreen_relations`) that needs scanning/hashing to prevent duplicates

## Question `ecs-relationship-type-level-exclusivity`

Should an ECS's relationship "edge" components be public types with the exclusivity (one-to-one, one-to-many, many-to-many, ...) encoded at the type level for compile-time correctness and ergonomics, or should the edge-storing components be private (mutable only via commands/hooks) with a single consistent query API regardless of exclusivity?

Positions:
- `ecs-relationship-type-level-exclusivity--p1`: Type level exclusivity public
- `ecs-relationship-type-level-exclusivity--p2`: Private edges runtime consistency

Claims:
- `b-sb07-f002142-c2` · Voice: iiYese · Source: https://github.com/bevyengine/bevy/pull/15635 (`f002142`) · Date: 2024-10-20 · Locator: PR #15635, comment 2024-10-20T10:57:04Z
  - Quote: "Consistency is more important here than options... Being at a type level is not a benefit it is the option."
  - Paraphrase: argues type-level exclusivity is not even correct (an entity can still hold both `OneToOne<R>` and `OneToMany<R>`) and forces every query site to know and restate the edge shape; consistency of one query API matters more than having the option
- `b-sb07-f002142-c1` · Voice: bushrat011899 · Source: https://github.com/bevyengine/bevy/pull/15635 (`f002142`) · Date: 2024-10-20 · Locator: PR #15635, comment 2024-10-20T08:31:44Z
  - Quote: "I believe it is nicer that the type has a different interface based on the exclusivity - it makes the difference explicit in code, and incorrect usage not compile"
  - Paraphrase: prefers public edge components whose type encodes the relationship's exclusivity (one-to-many derefs to `Entity`, many-to-one to `[Entity]`), because it makes incorrect usage fail to compile, improves error messages, and keeps the model close to what `Parent`/`Children` already are for users and for reflection/scene formats (BSN/`ron`)

## Question `ecs-ui-large-vs-small-systems`

For complex UI built on an ECS with an immediate-mode UI library (egui), should you write large systems with many queries in one place (simpler control flow, but they frequently deadlock against the borrow checker), or split into many small per-widget systems (fewer conflicts per system, but requires repeated manual world/state access that itself risks borrow-checker errors)?

Positions:
- `ecs-ui-large-vs-small-systems--p1`: Still actively fighting the borrow checker over how to split large UI systems, with no settled solution
- `ecs-ui-large-vs-small-systems--alt1`: Large systems with many queries in one place
- `ecs-ui-large-vs-small-systems--alt2`: many small per-widget systems

Claims:
- `b-sb25-f012561-c3` · Voice: Tristan · Source: https://youtube.com/watch?v=_FIDuLV0ZsA (`f012561`) · Date: 2025-06-18 · Locator: ~19:24-20:26
  - Quote: "it's an ongoing problem for me, it's not ... deadly ... but it's an ongoing problem"
  - Paraphrase: his large "god" UI systems with dozens of queries are simple to write but constantly conflict with the borrow checker; he tried a widget-per-system pattern proposed by another user in a GitHub discussion, which helps isolate systems but forces repeated manual `get_mut::<State>`/`get_mut::<World>` calls that themselves risk borrow errors — he calls it "an ongoing problem," not resolved

## Question `embedded-crash-policy-kernel-vs-supervisor`

In an embedded OS kernel, should crash-recovery policy (restart strategy, backoff, giving up) be hardcoded into the kernel, or left to an application-defined supervisor task?

Positions:
- `embedded-crash-policy-kernel-vs-supervisor--p1`: Policy in userspace supervisor not kernel
- `embedded-crash-policy-kernel-vs-supervisor--alt1`: Hardcode the crash-recovery policy in the kernel

Claims:
- `a-sa17-f008217-c1` · Voice: Cliff L. Biffle · Source: https://cliffle.com/blog/exhubris-super (`f008217`) · Date: 2024-12-14 · Locator: § "The role of the supervisor in Hubris"
  - Quote: "My conclusion is that there is no right answer to this question... So, Hubris leaves it up to you, the programmer."
  - Paraphrase: Hubris's kernel deliberately does not hardcode a crash-restart policy (immediate restart, backoff, giving up); it only records the fault and notifies a userspace supervisor task, leaving the recovery policy to the application programmer because the correct policy depends on context.

## Question `embedded-deferred-log-formatting`

In embedded/no_std logging, should you format and print human-readable strings at the point of use, or defer formatting to the host by sending compact binary tokens and decoding off-device?

Positions:
- `embedded-deferred-log-formatting--p1`: Deferred/binary logging over on-device string formatting
- `embedded-deferred-log-formatting--alt1`: Format human-readable strings on the device

Claims:
- `a-sa14-f005162-c1` · Voice: Ferrous Systems (Jonathan) · Source: https://ferrous-systems.com/blog/embedded-world-2025-demos (`f005162`) · Date: 2025-03-11 · Locator: § Rust for Microcontrollers
  - Quote: "the more efficient your logging, the more you can log for a given cost in terms of time and power, so this kind of saving soon adds up!"
  - Paraphrase: measures the same log line implemented via `rprintln!` (1675 instructions, converts f32 to string on-device) against `defmt::info!` (1050 instructions, sends the raw value plus a format-string ID) and generalizes that more efficient logging lets you log more for the same time/power cost

## Question `embedded-framework-bundles-hal-and-executor`

Should an embedded Rust concurrency solution bundle its own HAL and executor (batteries-included), or stay a framework-only layer that leaves HAL/PAC to the user and favors hardware-level resource exclusivity over software locking?

Positions:
- `embedded-framework-bundles-hal-and-executor--p1`: RTIC: framework-only, hardware-level exclusivity where possible; named alternative: Embassy bundles HAL + executor
- `embedded-framework-bundles-hal-and-executor--alt1`: Bundle a HAL and an executor with the framework (Embassy-style)

Claims:
- `a-sB04-f000227-c5` · Voice: RTIC developers · Source: https://rtic.rs/ (`f000227`) · Date: undated (living doc, v2.x) · Locator: "5. RTIC and Embassy", "Differences"
  - Quote: "RTIC aims to provide exclusive access to resources at as low a level as possible, ideally guarded by some form of hardware protection."
  - Paraphrase: States Embassy provides both a HAL and an executor/runtime (e.g. embassy-stm32, embassy-executor) while RTIC aims to provide only the execution framework, leaving PAC/HAL to the user (typically stm32-rs); RTIC additionally aims to give exclusive resource access as low-level as possible, ideally hardware-guarded, to avoid needing software-level locking

## Question `embedded-interpreter-stopgap`

When a needed capability (like `eval`) isn't natively supported by the host platform, is it acceptable to run a full interpreter for that capability inside your own Rust-compiled Wasm module as a stopgap, even though it means "a runtime on top of a runtime"?

Positions:
- `embedded-interpreter-stopgap--p1`: Embedded Rust interpreter as an acceptable stopgap for a missing platform capability
- `embedded-interpreter-stopgap--alt1`: Do not embed an interpreter; wait for native platform support

Claims:
- `a-sa14-f004985-c2` · Voice: Celso Martinho, Ruskin Constant, Rui Figueira, and Luís Duarte · Source: https://blog.cloudflare.com/kitesurf (`f004985`) · Date: 2026-08-06 · Locator: § How we built it / Yes, but evals
  - Quote: "We are basically executing a runtime on top of a runtime, which doesn't seem optimal, and it isn't, but it works well enough"
  - Paraphrase: explain they use Boa (a Rust-implemented ECMAScript engine) to handle `eval` since Workers doesn't support it natively and a second isolate wouldn't share `globalThis`, calling the approach non-optimal but workable until native support lands

## Question `embedded-panics-compile-time-vs-recovery`

In safety/crash-sensitive embedded Rust, should panics be eliminated for a given task at compile time, or tolerated and handled via runtime crash recovery?

Positions:
- `embedded-panics-compile-time-vs-recovery--p1`: Compile time no panic for the one critical task
- `embedded-panics-compile-time-vs-recovery--alt1`: Tolerate panics and rely on runtime crash recovery

Claims:
- `a-sa17-f008217-c2` · Voice: Cliff L. Biffle · Source: https://cliffle.com/blog/exhubris-super (`f008217`) · Date: 2024-12-14 · Locator: § "Who supervises the supervisor?"
  - Quote: "This provides a way to ensure, at compile time, that a task cannot panic."
  - Paraphrase: Because nothing restarts the supervisor task itself if it crashes, recommends compiling it with userlib's no-panic feature so any unoptimized-away panic becomes a link failure, catching a whole class of crashes at compile time for that one task rather than relying on runtime recovery (which has no one above it).

## Question `emscripten-vs-native-rust-wasm`

When compiling C/C++/Rust code to WebAssembly for a serverless runtime, should you go through an emulation layer like Emscripten, or compile natively from Rust straight to Wasm?

Positions:
- `emscripten-vs-native-rust-wasm--p1`: Native Rust-to-Wasm over an Emscripten emulation layer
- `emscripten-vs-native-rust-wasm--alt1`: Compile through an emulation layer such as Emscripten

Claims:
- `a-sa14-f004985-c1` · Voice: Celso Martinho, Ruskin Constant, Rui Figueira, and Luís Duarte · Source: https://blog.cloudflare.com/kitesurf (`f004985`) · Date: 2026-08-06 · Locator: § Design decisions / Use Rust when possible
  - Quote: "Instead, we opted for native Rust whenever possible and to compile directly to WebAssembly using wasm-bindgen, thus avoiding unnecessary emulation layers"
  - Paraphrase: explain that Emscripten's mocked-dependency layers make compiled binaries bulky and slow, so they chose native Rust compiled directly to Wasm via wasm-bindgen instead

## Question `emulate-specialization`

when a type needs specialization-like behavior (methods gated on stronger trait bounds, e.g. `Read+Write+Seek` vs `Read+Seek`) but Rust's real specialization is unstable, do you fake it with a runtime-checked field set from trait-bound-gated impl blocks, or reach for a different pattern entirely?

Positions:
- `emulate-specialization--p1`: Single-constructor design with an `Option<SyncFn>` field toggled from trait-bound-gated impl blocks, replacing separate RO/RW constructors
- `emulate-specialization--alt1`: Separate constructors per capability
- `emulate-specialization--alt2`: wait for real specialization

Claims:
- `b-sb20-f007213-c1` · Voice: Oakchris1955 · Source: https://oakchris1955.eu/posts/bypassing_specialization_followup (`f007213`) · Date: 2025-07-26 · Locator: section "The solution"
  - Quote: "Instead of using 2 constructors, one for a RO filesystem and another for a R/W filesystem, we use one for both cases."
  - Paraphrase: instead of two constructors (one for read-only, one for read-write), keep one constructor and one `sync_fn` field defaulted to `None`; only impls bound on `Read + Write + Seek` can set it to `Some`, which fixes a bug where RWFile writes silently failed to sync

## Question `encode-invariant-in-representation`

Should a Rust data model encode its invariants in the representation (exhaustive enums, log2-stored sizes) so invalid states are unrepresentable, or validate at use?

Positions:
- `encode-invariant-in-representation--encode-in-types`: Encode it in types
- `encode-invariant-in-representation--p1`: Make invalid states unrepresentable

Claims:
- `b-bk03-f000267-c2` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Design Overview § zebra-chain
  - Quote: "making invalid states unrepresentable"
  - Paraphrase: zebra-chain's data structures are deliberately defined to enforce structural validity by making invalid states unrepresentable — e.g. the Transaction enum has one variant per transaction version, so it is impossible to construct a transaction with spend/output descriptions but no binding signature, or a version-2 (Sprout) transaction carrying Sapling proofs
- `b-sb05-f001582-c1` · Voice: fitzgen · Source: https://github.com/bytecodealliance/wasmtime/pull/8763 (`f001582`) · Date: 2024-06-10 · Locator: PR description, 2024-06-10T20:15:41Z
  - Quote: "In general, we store the log2(page_size) rather than the page size directly. This helps cut down on invalid states and properties we need to assert."
  - Paraphrase: storing log2(page_size) instead of the raw page size cuts down on invalid states and the assertions needed elsewhere

## Question `enum-glob-import-in-match`

should match arms on an enum use a local glob import (`use Enum::*;`) to drop the type-qualified path, or keep variants fully qualified?

Positions:
- `enum-glob-import-in-match--p1`: Favors the local glob import for terser match arms
- `enum-glob-import-in-match--alt1`: Keep variants fully qualified

Claims:
- `b-sR03-f000763-c3` · Voice: joshka · Source: https://github.com/ratatui/ratatui/pull/840 (`f000763`) · Date: 2024-01-18 · Locator: ratatui/ratatui#840, comment 2024-01-18T01:32:39Z. · L125-L136.
  - Quote: "And add a `use KeyCode::*;` above this (inside the method) to drop the `Keycode::` from each."
  - Paraphrase: favors the local glob import for terser match arms.

## Question `enum-vs-dyn-trait-closed-set`

Should a set of kinds be modelled as an enum or as trait objects (`dyn Trait`, an open trait)?

Positions:
- `enum-vs-dyn-trait-closed-set--static-by-default`: Enums or generics; avoid `dyn` when possible
- `enum-vs-dyn-trait-closed-set--open-trait-for-extensibility`: An open trait for extensible policy
- `enum-vs-dyn-trait-closed-set--unsafe-unions-for-memory`: Unsafe unions when memory must be squeezed

Claims:
- `a-sa17-f007884-c2` · Voice: alonely0 · Source: https://alonely0.github.io/blog/unions (`f007884`) · Date: 2024-04-28 · Locator: § "A first attempt: dynamic dispatch", closing paragraph
  - Quote: "it's the slowest and least idiomatic"
  - Paraphrase: Treats Box<dyn Trait> as the slowest and least idiomatic option, worth using mainly as a guaranteed-two-word size bound or as a fallback for one oversized enum variant, to be avoided otherwise.
- `a-sa07-f003704-c3` · Voice: antimora · Source: https://github.com/tracel-ai/burn/pull/3872 (`f003704`) · Date: 2025-11-07 · Locator: PR #3872, comment 2025-11-07T15:47:01Z
  - Quote: "We will redo as a graph of node enums"
  - Paraphrase: agreed, after offline discussion, to redo the Graph representation as node enums
- `a-sa17-f007884-c1` · Voice: alonely0 · Source: https://alonely0.github.io/blog/unions (`f007884`) · Date: 2024-04-28 · Locator: § "Enum dispatch", opening
  - Quote: "The naive approach, which is the one I'd recommend myself, would be to use enums."
  - Paraphrase: Recommends enums (enum_dispatch-style) as the default over dynamic dispatch for a fixed set of known types, since it drops heap allocation and vtable indirection while staying entirely safe.
- `b-sR10-f004741-c3` · Voice: Friedel Ziegelmayer & Rüdiger Klaehn (iroh/n0 computer) · Source: https://iroh.computer/blog/iroh-1-0-0-rc-1 (`f004741`) · Date: 2026-05-27 · Locator: section "🔐 Pluggable relay access control"
  - Quote: "The relay's access control has been redesigned. The AccessConfig enum is gone, replaced by an AccessControl trait with on_connect and on_disconnect hooks."
  - Paraphrase: the closed `AccessConfig` enum was replaced by an open `AccessControl` trait with `on_connect`/`on_disconnect` hooks, so embedders can implement arbitrary policy rather than choosing among enum variants
- `a-sa17-f007884-c3` · Voice: alonely0 · Source: https://alonely0.github.io/blog/unions (`f007884`) · Date: 2024-04-28 · Locator: § "Now with unions, also known as C's untagged enums..."
  - Quote: "Unions are not just an archaic tool from the long forgotten era of Dennis Ritchie, they are still a very useful tool which can yield amazing results in the right han[ds]"
  - Paraphrase: Goes beyond the enum-dispatch default into unsafe unions with hand-rolled tagged pointers (ManuallyDrop, ptr aliasing via transmute_copy) to shrink the value below the default enum's size, treating it as a deliberate, specialized escalation past safe Rust when memory layout is worth the unsafety.

## Question `enum-vs-flags-and-optionals`

Should multi-outcome or growing state be an enum, or a bool or a struct of optional fields?

Positions:
- `enum-vs-flags-and-optionals--enum`: Use a (non-exhaustive) enum
- `enum-vs-flags-and-optionals--alt1`: A bool or a struct of optional fields

Claims:
- `b-sR08-f003731-c1` · Voice: ramfox · Source: https://iroh.computer/blog/iroh-0-94-0-the-endpoint-takeover (`f003731`) · Date: 2025-10-22 · Locator: § "Future proofing: Introducing TransportAddr"
  - Quote: "To combine them, and to allow for additions in the future, they are now represented as variants on a TransportAddr"
  - Paraphrase: replaced two independent fields (an optional relay URL and a set of socket addresses) with a single `#[non_exhaustive] enum TransportAddr { Relay(RelayUrl), Ip(SocketAddr) }`, so future transport kinds (e.g. WebRTC) can be added as new variants without another breaking change.
- `b-sR08-f003531-c1` · Voice: MrSubidubi · Source: https://github.com/zed-industries/zed/pull/38102 (`f003531`) · Date: 2025-10-10 · Locator: PR #38102, review comment 2025-10-10T21:34:30Z
  - Quote: "Could we perhaps fix the logic above instead or change `self.serialize_dirty_buffers` to be an enum instead ... With that, this might be more readable and understandable, what do you think?"
  - Paraphrase: instead of adding another special-cased check around the existing `serialize_dirty_buffers` boolean, suggests changing it to a named enum (`Always`/`Dirty`/`Never`) for readability.
- `b-sR08-f003531-c2` · Voice: im-lunex · Source: https://github.com/zed-industries/zed/pull/38102 (`f003531`) · Date: 2025-10-16 · Locator: PR #38102, comment 2025-10-16T09:45:09Z
  - Quote: "The use of enum was the right decision - so neater and more secure."
  - Paraphrase: implemented the suggested `SerializationMode` enum in place of the boolean flag and judges it the safer, clearer choice.

## Question `epoll-vs-io-uring`

For a hand-built async I/O reactor on Linux, should you build the readiness-notification layer on `epoll` (mature, stable) or on `io_uring` (newer, potentially faster but more experimental)?

Positions:
- `epoll-vs-io-uring--p1`: Epoll for now as the standard tradeoff
- `epoll-vs-io-uring--alt1`: Build on `io_uring`

Claims:
- `b-sb21-f008396-c1` · Voice: Natalie Klestrup Röijezon (natkr) · Source: https://natkr.com/2025-04-15-async-from-scratch-2 (`f008396`) · Date: 2025-04-16 · Locator: footnote 9 (§ "Sleepy I/O")
  - Quote: "Not the only API, there are others. But it's the one that hits the 'standard' tradeoff between not being too slow or too experimental."
  - Paraphrase: chooses epoll for the tutorial's reactor because it hits the "standard" balance of being neither too slow nor too experimental, while noting io_uring might take over that role "in a few years"

## Question `ergonomic-sugar-now-or-later`

When shipping a small utility feature quickly, is it worth adding ergonomic sugar (a macro/trait wrapper) around the raw mechanism, or should that wait until it's shown to carry its weight?

Positions:
- `ergonomic-sugar-now-or-later--p1`: Ship the minimal raw mechanism now, add sugar only once it earns it
- `ergonomic-sugar-now-or-later--alt1`: Add the macro or trait sugar now

Claims:
- `a-sa11-f004512-c4` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/5296 (`f004512`) · Date: 2026-04-01 · Locator: comment 2026-04-01T20:16:11Z
  - Quote: "This PR was thrown together in 15 minutes. Whether this will be good enough or not, time will tell. We can add a macro and a trait to dress this up as a plugin, but there's very little reason to do that except for some syntactic sugar."
  - Paraphrase: acknowledges the PR was assembled quickly and says a macro/trait wrapper could be added for syntactic sugar later, but sees little reason to do it now

## Question `ergonomics-vs-explicitness`

Should Rust favor implicit ergonomic sugar (the 2017 "ergonomics initiative", e.g. match ergonomics) even where it costs the language's own stated core value of explicitness, or hold the line on explicitness?

Positions:
- `ergonomics-vs-explicitness--p1`: Explicitness is an unstated core value
- `ergonomics-vs-explicitness--p2`: Ergonomics-initiative-RFCs-are-knowingly-controversial

Claims:
- `a-sa28-f012469-c10` · Voice: aturon (Aaron Turon, Rust language-design team) · Source: https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (`f012469`) · Date: 2017-08-31 · Locator: post by @MaloJaffre dated 2017-08-31T19:26:05Z, sourced "Aturon about ergonomics initiative RFCs"
  - Quote: "Anywhere your code is hard to write, we'll be there, writing controversial RFCs then scaling them back! Resistance is futile!"
  - Paraphrase: self-aware acknowledgment that the 2017 ergonomics-initiative RFCs (pushing implicit sugar into hard-to-write corners) are controversial and will need walking back
- `a-sa28-f012469-c9` · Voice: Ian Whitney (blog post "Rust via its Core Values," cited independently twice, two years apart, by different posters — circumstantial evidence of being a genuinely referenced source) · Source: https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (`f012469`) · Date: blog post undated in source; cited 2016-04-03 and again 2018-04-25 · Locator: post by @nayru25 dated 2016-04-03T00:20:55Z; re-cited by @cg-cnu dated 2018-04-25T09:01:38Z
  - Quote: "Explicitness is the fourth core value of Rust. Ironically, I don't see that 'Explicitness' is ever explicitly stated as a goal of Rust."
  - Paraphrase: identifies explicitness as one of Rust's de facto core values despite it never being explicitly written down as a goal

## Question `error-enum-scope-module-vs-function`

Should error enums be scoped per-module (one large enum for everything a module can fail at), or per-function/operation (smaller, descriptively-named enums scoped to what one call can fail at)?

Positions:
- `error-enum-scope-module-vs-function--p1`: Scope error enums per-function, not per-module
- `error-enum-scope-module-vs-function--alt1`: One large error enum per module

Claims:
- `a-sa14-f005149-c2` · Voice: dig, b5, and ramfox (iroh team) · Source: https://iroh.computer/blog/error-handling-in-iroh (`f005149`) · Date: 2025-08-22 · Locator: § Concrete-error writing guidelines / Error enums are scoped to functions not modules
  - Quote: "Lean toward error enum names that are descriptive of the error, when logical"
  - Paraphrase: describe starting with one big per-module enum, finding it unwieldy, and moving to a nested/scoped hierarchy (e.g. `DialError` inside `ConnectError`) with names descriptive of the failure surface

## Question `esp32-psram-display-dma-strategy`

How should an ESP32-S3 Rust firmware feed a large RGB (DPI) display from PSRAM framebuffers: cyclic DMA straight from PSRAM, restarted transfers, SRAM bounce buffers refilled from PSRAM, XIP from PSRAM, or abandon RGB for an I8080 panel?

Positions:
- `esp32-psram-display-dma-strategy--p1`: Infinite cyclic DMA buffer, never restart transfers
- `esp32-psram-display-dma-strategy--p2`: SRAM bounce buffers refilled from PSRAM by Mem2Mem DMA, no XIP
- `esp32-psram-display-dma-strategy--p3`: Bounce buffers with acyclic descriptors, restart per frame
- `esp32-psram-display-dma-strategy--p4`: Stay on an I8080 display for a PSRAM-heavy app

Claims:
- `b-sT05-f002499-c3` · Voice: Limeth · Source: https://github.com/esp-rs/esp-hal/issues/2884 (`f002499`) · Date: 2026-02-16 · Locator: comment 2026-02-16T23:59:16Z
  - Quote: "using acyclic descriptors and restarting the transmission after each frame seems to be fine, although not as nice"
  - Paraphrase: cyclic descriptors failed after the first frame; acyclic descriptors restarted each frame work; open to upstreaming a generic solution to esp-hal
- `b-sT05-f002499-c1` · Voice: Dominaezzz · Source: https://github.com/esp-rs/esp-hal/issues/2884 (`f002499`) · Date: 2026-01-29 · Locator: comment 2026-01-29T04:49:37Z
  - Quote: "I avoid restarting transfers and I always use an infinite DMA buffer"
  - Paraphrase: in own projects every framebuffer's last DMA descriptor points to its first; switching buffers = relinking descriptors; breaks down once PSRAM bandwidth enters
- `b-sT05-f002499-c4` · Voice: yanshay · Source: https://github.com/esp-rs/esp-hal/issues/2884 (`f002499`) · Date: 2026-09-06 · Locator: comment 2026-09-06T19:24:30Z
  - Quote: "didn't switch device and still use an I8080 display at lower size and resolution"
  - Paraphrase: had a bounce-buffer Slint renderer working, but flash contention and PSRAM bandwidth slowed the application; kept a smaller I8080 display
- `b-sT05-f002499-c2` · Voice: EliteTK · Source: https://github.com/esp-rs/esp-hal/issues/2884 (`f002499`) · Date: 2026-09-06 · Locator: comment 2026-09-06T10:36:52Z
  - Quote: "double-buffered glitch-free output without relying on XiP from PSRAM"
  - Paraphrase: two PSRAM framebuffers, two 1/16 bounce buffers in RAM, looping DMA to LCD, 8x descriptors to locate the emitted slice via DMA_OUT_CHx interrupt; cancels late refills; 31.1 FPS glitch-free; CPU copy rejected as "glacial"

## Question `example-data-domain-struct-vs-generic`

in example/demo code, should tabular data be modeled with a dedicated domain struct or with generic collections (`Vec<Vec<String>>`)?

Positions:
- `example-data-domain-struct-vs-generic--p1`: Prefer a small dedicated struct even at the cost of extra ceremony, to show real-world data mapping
- `example-data-domain-struct-vs-generic--alt1`: Generic collections (`Vec<Vec<String>>`)

Claims:
- `b-sR03-f000763-c1` · Voice: joshka (ratatui maintainer) · Source: https://github.com/ratatui/ratatui/pull/840 (`f000763`) · Date: 2024-01-18 · Locator: ratatui/ratatui#840, comment 2024-01-18T22:51:17Z. · L424-L442.
  - Quote: "What about adding a small struct that has name, address, email and which gets generated in the app constructor instead of Vec<Vec<String>>? ... Obviously this is just gold plating things at this point. But it does give a nice way of showing how to map real world data into table columns."
  - Paraphrase: prefer a small dedicated struct even at the cost of extra ceremony, to show real-world data mapping.

## Question `exclusive-access-default-in-task-api`

For a Rust task/resource API, should exclusive (&mut) access to shared state be the default, with shared (&-) read-only access only available opt-in?

Positions:
- `exclusive-access-default-in-task-api--p1`: Default-exclusive, opt-in-shared-for-lock-elision
- `exclusive-access-default-in-task-api--alt1`: Shared access by default

Claims:
- `a-sB04-f000227-c1` · Voice: RTIC developers (rtic.rs maintainers) · Source: https://rtic.rs/ (`f000227`) · Date: undated (living doc, v2.x) · Locator: "2.4. Resources", "Only shared (&-) access"
  - Quote: "The advantage of specifying shared access (&-) to a resource is that no locks are required to access the resource even if the resource is contended by more than one task running at different priorities."
  - Paraphrase: States the framework assumes exclusive mutable access by default; a task can opt into shared (&-) access instead, trading the ability to mutate for skipping the lock API even when the resource is contended across priorities

## Question `executor-agnostic-libraries`

Should a library that exposes an async API depend on a specific async executor or reactor?

Positions:
- `executor-agnostic-libraries--p1`: Libraries should stay executor/reactor-agnostic
- `executor-agnostic-libraries--alt1`: Depend on a specific executor or reactor

Claims:
- `b-bk01-f000233-c12` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "The Async Ecosystem" § Determining Ecosystem Compatibility
  - Quote: "Libraries exposing async APIs should not depend on a specific executor or reactor, unless they need to spawn tasks or define their own async I/O or timer futures."
  - Paraphrase: libraries exposing async APIs should not depend on a specific executor or reactor unless they must spawn tasks or define their own async I/O or timer futures; ideally only binaries own scheduling/running of tasks. Reasons from the ecosystem's actual fragmentation: Tokio's mio-based reactor and its own AsyncRead/AsyncWrite traits are not directly compatible with async-std or smol (which use the async-executor crate and futures' I/O traits), though compatibility layers like async_compat exist as a workaround.

## Question `explicit-vs-convenience-memory-defaults`

Should a language's memory-model default favor explicitness/performance (opt into convenience, as Rust's move/borrow-by-default with Cow/Rc as opt-in) or convenience (opt into performance, as Swift's copy-on-write-by-default with ownership as opt-in)?

Positions:
- `explicit-vs-convenience-memory-defaults--p1`: Domain dependent tradeoff
- `explicit-vs-convenience-memory-defaults--alt1`: Explicitness and performance by default (Rust-style)
- `explicit-vs-convenience-memory-defaults--alt2`: convenience by default (Swift-style copy-on-write)

Claims:
- `b-sR12-f005668-c1` · Voice: nmn (nmn.sh blog author) · Source: https://nmn.sh/blog/2023-10-02-swift-is-the-more-convenient-rust (`f005668`) · Date: 2026-01-31 · Locator: section "Convenience has its costs"
  - Quote: "I would say both languages have their uses. Rust is better for systems and embedded programming... Swift is better for writing UI and servers and some parts of compilers and operating systems. Over time I expect to see the overlap get bigger."
  - Paraphrase: neither default is simply better; Rust's performance-first default suits systems, embedded, compilers and browser engines, Swift's convenience-first default suits UI, servers and parts of compilers/operating systems, and the author expects the overlap between the two to grow over time

## Question `explicit-vs-implicit-indirection`

Should indirection for a recursive data type be explicit (the programmer writes `Box<T>`) or implicit (a compiler-inferred/annotated indirection, as Swift's `indirect` keyword)?

Positions:
- `explicit-vs-implicit-indirection--p1`: Explicit favorably framed
- `explicit-vs-implicit-indirection--alt1`: Implicit, compiler-handled indirection (Swift's `indirect`)

Claims:
- `b-sR12-f005668-c2` · Voice: nmn (nmn.sh blog author) · Source: https://nmn.sh/blog/2023-10-02-swift-is-the-more-convenient-rust (`f005668`) · Date: 2026-01-31 · Locator: section "Rust's compiler catches problems. Swift's compiler solves some of them"
  - Quote: "This makes the problem explicit and forces you to deal with it directly, Swift is a little more, automatic."
  - Paraphrase: contrasting Rust's `Box<TreeNode<T>>` for a recursive enum with Swift's `indirect` keyword, the author frames Rust's requirement to write the indirection explicitly as forcing the programmer to confront the problem directly, versus Swift handling it more automatically

## Question `expose-fixed-array-vs-wrapper-type`

When a fixed-size array (e.g. `[u8; 6]`) might later need to hold a same-shaped but larger variant (e.g. an 8-byte IEEE MAC), should the API expose the array type directly, or return a slice / wrap it in a dedicated type to keep the door open?

Positions:
- `expose-fixed-array-vs-wrapper-type--p1`: Wrap raw array in a semantic type rather than exposing it directly
- `expose-fixed-array-vs-wrapper-type--p2`: Return a slice instead of a fixed-size array

Claims:
- `a-sa11-f004265-c1` · Voice: MabezDev · Source: https://github.com/esp-rs/esp-hal/pull/5002 (`f004265`) · Date: 2026-02-18 · Locator: comment 2026-02-18T14:11:20Z
  - Quote: "I think we should wrap `[u8; 6]` into a `Mac` type where we can derive some stuff, implement `Display`"
  - Paraphrase: argues for wrapping `[u8; 6]` in a `Mac` type with derives and a `Display` impl, noting IEEE MACs are 8 bytes so the current shape could never return one
- `a-sa11-f004265-c3` · Voice: MabezDev · Source: https://github.com/esp-rs/esp-hal/pull/5002 (`f004265`) · Date: 2026-02-19 · Locator: comment 2026-02-19T14:04:25Z
  - Quote: "Return a slice, not [u8; 6]"
  - Paraphrase: pushes back on returning `[u8; 6]`, preferring a slice-typed return

## Question `expose-rustc-internals-rustdoc-json`

When rustc has internal capability to correctly deduce information (implied trait bounds) that an external tool (cargo-semver-checks) cannot feasibly re-derive on its own, should that capability be exposed through a structured interface (rustdoc JSON) rather than left for external tools to approximate?

Positions:
- `expose-rustc-internals-rustdoc-json--p1`: Expose rustc internals via rustdoc json
- `expose-rustc-internals-rustdoc-json--alt1`: Leave external tools to approximate the information

Claims:
- `a-sa20-f009698-c4` · Voice: @obi1kenobi · Source: https://blog.rust-lang.org/2025/05/26/april-project-goals-update (`f009698`) · Date: 2025-05-03 · Locator: "Continue resolving `cargo-semver-checks` blockers for merging into cargo" section, comment posted 2025-05-03
  - Quote: "While technical limitations make it infeasible for cargo-semver-checks to correctly deduce implied bounds, rustc has this capability internally. We have asked the rustdoc team to expose implied bounds in rustdoc JSON by using those rustc internal APIs."
  - Paraphrase: discovered that Rust's implied bounds (not stated explicitly at a definition site) are load-bearing for SemVer — missing them produces both false positives and false negatives — and that while it's technically infeasible for cargo-semver-checks to correctly deduce implied bounds itself, rustc already has this capability internally, so the team asked the rustdoc team to expose implied bounds in rustdoc JSON via those internal APIs

## Question `extend-foreign-trait-type`

When a foreign trait's shared type (e.g. `embedded_hal::spi::Operation`) can't expose the hardware-specific capability a HAL needs, should the HAL define its own parallel type (accepting API duplication and a breaking change) to extend, or add narrowly scoped extension methods that leave the foreign type untouched?

Positions:
- `extend-foreign-trait-type--p1`: Narrow extension methods
- `extend-foreign-trait-type--p2`: Own parallel type with conversion

Claims:
- `b-sb06-f002027-c1` · Voice: elipsitz · Source: https://github.com/esp-rs/esp-idf/pull/479 (`f002027`) · Date: 2024-09-17 · Locator: PR #479, comment 2024-09-17T20:43:31Z and 2024-09-23T15:36:19Z
  - Quote: "I'd be wary of bolting on another `Operation` enum without re-evaluating the complexity of the API."
  - Paraphrase: initially wary of "bolting on another `Operation` enum without re-evaluating the complexity of the API," since the existing SPI API is already fairly unintuitive; leans toward a narrowly scoped `transaction_with_width` method or new enum variants instead of a second type
- `b-sb06-f002027-c2` · Voice: ivmarkov · Source: https://github.com/esp-rs/esp-idf/pull/479 (`f002027`) · Date: 2024-09-23 · Locator: PR #479, comment 2024-09-23T16:21:54Z
  - Quote: "yet - it is something the user should neither know, nor care about"
  - Paraphrase: argues the crate effectively already has "its own `Operation`... if you squint a little" (currently just a type-alias out of laziness); users should not need to know or care whether they're going through embedded_hal's `Operation` or the crate's own, so making it a real, independently extensible type is fine even as a breaking change

## Question `externref-in-rust`

Should Rust add WebAssembly's `externref` as a new restricted language type, or keep it outside the core language?

Positions:
- `externref-in-rust--new-restricted-lang-type`: Add a restricted lang-item type; JS interop justifies a language change
- `externref-in-rust--must-fit-abstract-machine`: Reject types outside the Abstract Machine
- `externref-in-rust--table-index-in-rust-code`: Table-index wrapper, real `externref` only at FFI
- `externref-in-rust--keep-out-of-language-core`: Leave it to the compiler or runtime

Claims:
- `a-sa29-f013113-c3` · Voice: juntyr · Source: https://github.com/rust-lang/rfcs/pull/3987 (`f013113`) · Date: 2026-07-29T13:09:09Z · Locator: RFC #3987, comment 2026-07-29T13:09:09Z
  - Quote: "a non-zero cost wrapper could work better"
  - Paraphrase: proposes that `externref` act as a table index everywhere in Rust-only code, with the actual WASM `externref` only crossing at FFI boundaries, and an optimization pass eliding the table insert/extract round-trip when a value is merely passed through
- `a-sa29-f013113-c4` · Voice: ds84182 · Source: https://github.com/rust-lang/rfcs/pull/3987 (`f013113`) · Date: 2026-07-30T02:36:47Z · Locator: RFC #3987, comment 2026-07-30T02:36:47Z
  - Quote: "I do not think languages should change at such a core level to support something extremely niche like this"
  - Paraphrase: notes `__externref_t` is Clang's own non-standard extension, unmatched by GCC or MSVC, and argues WebAssembly's design oddities should be papered over by the compiler/runtime rather than by changing the language core for something this niche
- `a-sa29-f013113-c5` · Voice: guybedford · Source: https://github.com/rust-lang/rfcs/pull/3987 (`f013113`) · Date: 2026-07-30T15:48:27Z · Locator: RFC #3987, comment 2026-07-30T15:48:27Z
  - Quote: "JavaScript interop is not a complex or niche topic and this is a major quality of life improvement to that story"
  - Paraphrase: responding directly to ds84182, argues JavaScript interop is a major quality-of-life story worth solving at the language level and that Rust has tackled harder, more niche problems before, while conceding the proposal must be justified for Rust on its own merits rather than by Clang precedent
- `a-sa29-f013113-c1` · Voice: guybedford · Source: https://github.com/rust-lang/rfcs/pull/3987 (`f013113`) · Date: 2026-07-29 · Locator: RFC #3987, opening post, 2026-07-29T00:09:07Z
  - Quote: "an opaque, unforgeable reference to a WebAssembly host value, lowering to the Wasm externref reference type in function signatures"
  - Paraphrase: proposes `core::arch::wasm32::externref`, legal only as a bare top-level type of function parameters/returns/locals, to let host references (e.g. JS values) marshal directly across foreign calls for interoperability and performance
- `a-sa29-f013113-c2` · Voice: RalfJung · Source: https://github.com/rust-lang/rfcs/pull/3987 (`f013113`) · Date: 2026-07-29T12:21:27Z and 2026-07-29T12:34:52Z · Locator: RFC #3987, comments 2026-07-29T12:21:27Z / 12:34:52Z
  - Quote: "this RFC is proposing to introduce a fundamentally new kind of thing to Rust only to then make that thing a complete nightmare to use for anything"
  - Paraphrase: argues the RFC's semantics can't be expressed in the Abstract Machine used to justify MIR-transform and MIR-to-LLVM-IR correctness, calling this an unprecedented kind of break (worse than prior type-system-assumption-breaking RFCs), and that without integration into `Result`, async, `==`, or newtypes the feature will feel "bolted on"

## Question `extract-single-use-function`

Should single-use or repeated inline logic be extracted into a named function or method, or kept inline?

Positions:
- `extract-single-use-function--extract-for-communication`: Extract into a named function or method
- `extract-single-use-function--keep-inline`: Keep it inline where used

Claims:
- `b-sb04-f001392-c5` · Voice: joshka · Source: https://github.com/ratatui/ratatui/pull/1089 (`f001392`) · Date: 2024-05-11 · Locator: PR #1089, comment 2024-05-11T11:12:04Z
  - Quote: "Functions are not just a tool for reuse, they're a tool for communicating blocks of code like this."
  - Paraphrase: pulls span-visibility logic into its own method even though it has one caller, because a well-named function with a defined input/output lets the reader trust what it does without re-deriving it; functions are "a tool for communicating blocks of code", not just for reuse
- `b-sR12-f005085-c1` · Voice: antimora (Tracel AI / burn maintainer) · Source: https://github.com/tracel-ai/burn/pull/5617 (`f005085`) · Date: 2026-09-08 · Locator: PR review comment, 2026-09-08T21:11:40Z
  - Quote: "This is duplicated verbatim at `ops/gather_scatter.rs:18`. Both copies gate `storage_mut()`, so a drift between them is a bad write rather than a compile error... Reads better as a single method on `Layout` carrying the actual contract."
  - Paraphrase: the same dense/non-broadcast check is duplicated verbatim at two call sites gating `storage_mut()`, so drift between them would silently produce a bad write instead of a compile error; it should be a single method on `Layout` that documents the actual contract
- `b-sb04-f001392-c6` · Voice: EdJoPaTo · Source: https://github.com/ratatui/ratatui/pull/1089 (`f001392`) · Date: 2024-05-11 · Locator: PR #1089, comment 2024-05-11T09:24:22Z
  - Quote: "I don't think moving this into its own method is very useful. Its very specific to the render_span method."
  - Paraphrase: argues against extracting the same logic into its own method, since it is very specific to one caller (`render_spans`) and pulling it out (and naming it `visible`) risks being misleading about what it actually guarantees
