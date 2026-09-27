# Fill A — position summaries, file 05

## fast-path-complexity

### fast-path-complexity--p1 (Absolute magnitude decides)
Advocates say the right lens is the absolute per-call cost, not the relative one: a regression that looks huge in percentage terms on old or constrained hardware (a Raspberry Pi) can still be tens of nanoseconds on current hardware, and that absolute number, not the ratio, is what should decide whether the extra code complexity of a fast path is worth keeping.
Tag: tradeoff.
Claims: b-sb04-f001392-c1.

### fast-path-complexity--p2 (Relative impact on constrained hw matters)
Advocates say relative regressions matter because the affected code sits on a hot path used constantly (a core construct like `Line`, hit hundreds of times per rendered frame), so even a "small" per-call regression compounds into a real, measured slowdown on low-power devices, and that compounding effect justifies keeping the fast path.
Tag: tradeoff.
Claims: b-sb04-f001392-c2.

## feature-flag-trunk-vs-long-branch

### feature-flag-trunk-vs-long-branch--p1 (Feature flag gate on trunk)
Advocates say experimental or breaking work belongs on main behind a Cargo feature flag, not on a long-lived branch, because that's what keeps main continuously releasable.
Tag: tradeoff.
Claims: b-bk03-f000267-c11.

## feature-flags-vs-generic-wiring

### feature-flags-vs-generic-wiring--p1 (Generic wiring over feature flags)
Advocates say generic, trait/type-level component wiring beats Cargo feature flags for selecting alternate implementations because every alternative implementation can coexist and be tested simultaneously, avoiding the combinatorial feature-flag testing burden.
Tag: tradeoff.
Claims: a-sa16-f007175-c1.

## feature-flags-vs-separate-crates

### feature-flags-vs-separate-crates--split-into-crates (Split into separate crates or modular crates joined by traits)
Advocates say functionality should be factored out of one crate into separate, independently versioned and releasable crates — moving optional components to their own repos, keeping new integrations out of a main crate to shorten release cycles, splitting a monolithic domain into per-domain sub-crates behind a stable interface crate, building a small core with everything else swappable behind traits, or splitting a single crate into a workspace where only the required piece is a mandatory dependency.
Tag: tradeoff.
Claims: a-sR13-f004685-c2, b-sR05-f002151-c1, a-sa18-f008651-c1, b-sb25-f011435-c1, b-sR12-f005120-c1.

### feature-flags-vs-separate-crates--p1 (Modular library first)
Advocates frame the choice as a library-first design commitment: build the project as independently reusable library crates from the start, with a contributing guide naming this as a scope boundary against a monolithic, feature-flagged binary.
Tag: tradeoff.
Claims: b-bk03-f000267-c3.

## feature-misuse-responsibility

### feature-misuse-responsibility--p1 (Structure feature placement to discourage misuse)
Advocates say where a feature lives changes how safely it gets used: placing a feature on a crate whose accidental activation has visible, non-wasm-target effects makes wrongful unconditional enabling by a downstream crate a more visible, more punished mistake than placing it somewhere a wrong enable silently does nothing.
Tag: tradeoff.
Claims: a-sa06-f003558-c3.

### feature-misuse-responsibility--p2 (Misuse is the misusing crate's bug, not the exposing crate's design problem)
Advocates reject "protect against misuse" as a design goal outright: a crate cannot be forced to behave properly by restructuring the exposing API, misbehaving crates should get issues or PRs filed against them directly, and relocating the feature only moves the same possible mistake elsewhere rather than solving it.
Tag: tradeoff.
Claims: a-sa06-f003558-c4.

## feature-naming-mechanism-vs-capability

### feature-naming-mechanism-vs-capability--p1 (Name a feature for its literal mechanism, not the capability it implies)
Advocates object when a feature name like "tracking" implies the library itself takes care of a capability with little user setup, when the feature actually just wires up a low-level mechanism (hooking) and nothing more; the name should say what it mechanically does, not what it enables.
Tag: taste.
Claims: a-sa11-f004512-c5.

## ffi-bindings-lag-pause-or-ship

### ffi-bindings-lag-pause-or-ship--p1 (Pause and fix ffi first)
Advocates say when non-Rust bindings can't meet the "just works" bar the project holds native Rust usage to, ship no more degraded releases of them — stop and fix the FFI/bridging story itself first, accepting the ecosystem-fragmentation risk of a pause rather than keep shipping a substandard experience.
Tag: tradeoff.
Claims: a-sa04-f002665-c1.

## ffi-copy-vs-share

### ffi-copy-vs-share--p2 (Minimize copying/serializing across the JS↔wasm boundary; expose long-lived Rust data as opaque handles, return small copyable results)
Advocates give this as a general rule of thumb: large, long-lived data structures should live as Rust types inside wasm linear memory and be exposed to JS only as opaque handles, with JS calling functions that do the heavy work and hand back small, cheap results, minimizing copy and serialize overhead at the boundary; a delta/diff-based alternative is acknowledged as viable but harder to implement.
Tag: tradeoff.
Claims: a-sB02-f000256-c3, b-bk02-f000256-c2.

### ffi-copy-vs-share--p3 (Replace a Display-generated JS String with a raw pointer + Uint8Array overlay onto wasm linear memory)
Advocates point to a concrete before/after: generating and allocating a Rust String and letting wasm-bindgen convert it to a JS string makes unnecessary copies, so the fix returns a raw pointer and lets JS read the cell buffer directly out of wasm memory via a typed-array overlay instead.
Tag: tradeoff.
Claims: b-bk02-f000256-c3.

### ffi-copy-vs-share--share-or-borrow (Pass borrowed references to avoid conversion overhead)
Advocates mark passing `&str` as the efficient choice against `String`, contrasted directly as one of a short list of performance practices at an FFI boundary — use references where possible instead of owned, converted values.
Tag: tradeoff.
Claims: b-sb22-f008914-c2.

### ffi-copy-vs-share--convert-or-copy (Convert or copy into idiomatic types)
Advocates say copying immutable data across the boundary, rather than sharing a pointer into it, is generally safer and easier: it costs a small performance penalty but guarantees that memory management on one side of a binding can't affect the other side, which is judged worth it more often than not.
Tag: tradeoff.
Claims: b-sb20-f007678-c2.

## ffi-tag-unwind-vs-abort

### ffi-tag-unwind-vs-abort--p1 (Tag unwinds explicitly)
Advocates say between two workable options — marking all definitely-abort errors, or marking all definitely-unwind errors — they chose to tag the recoverable (unwind) case explicitly, because it fit more easily on top of their existing raw WAT-level exception-handling implementation.
Tag: tradeoff.
Claims: a-sa12-f004598-c2.

## ffi-ui-state-snapshots-vs-diffs

### ffi-ui-state-snapshots-vs-diffs--p1 (Whole snapshot, chosen)
Advocates expose the whole state (the entire universe, as a pointer into linear memory) to the UI side each tick, naming a delta-based design — returning only the cells that changed — as a viable alternative they explicitly did not adopt because it is harder to implement.
Tag: tradeoff.
Claims: a-sB02-f000256-c4.

### ffi-ui-state-snapshots-vs-diffs--p2 (Rust side tracks and emits diffs)
Advocates settled on this after iterating through worse designs (manual return-value wiring, per-field event handlers, an all-optional model needing manual checks): a derive macro generates a companion struct plus a diff enum, so Rust tracks uncommitted field changes and the UI side applies an exhaustive diff that the compiler refuses to build if a new field goes unhandled.
Tag: tradeoff.
Claims: a-sa18-f008389-c1.

## fields-in-traits

### fields-in-traits--p1 (Mildly supportive, uncertain use case)
Advocates land on a shrug: the feature is limited and distinct enough that it doesn't seem to harm Rust's design in any way, but they personally don't have a compelling use case that would make them push for it.
Tag: taste.
Claims: b-sb19-f007207-c1.

## final-trait-methods

### final-trait-methods--p1 (Support final methods)
Advocates point to concrete design work already done: a drafted RFC ("Trait method impl restrictions") using the reserved `final` keyword, and a proposed `#[non_overridable]` attribute, both meant to let a trait forbid overriding specific methods for correctness reasons and potentially shrink vtables by excluding such methods.
Tag: tradeoff.
Claims: a-sa19-f009316-c2, a-sa19-f009316-c1.

### final-trait-methods--p2 (Skeptical, limited value vs free functions)
Advocates doubt final methods offer real benefit beyond "minor sugar," arguing that any trait bound or call used inside a final method can just as well be replicated with an equivalent free function.
Tag: taste.
Claims: a-sa19-f009316-c3.

### final-trait-methods--p3 (Final methods need vtable for soundness)
Advocates demonstrate, with a concrete example, that a final method called through `dyn Trait` can observably differ from an equivalent generic free function (e.g. via `TypeId::of::<Self>` versus the erased type), so final methods cannot simply desugar away and must remain reachable via the vtable; a filed I-unsound bug shows nightly's experimental implementation currently gets this wrong, confirming the concern is live, not theoretical.
Tag: fact.
Claims: a-sa19-f009316-c4, a-sa19-f009316-c5.

## fine-grained-reactivity-vs-vdom

### fine-grained-reactivity-vs-vdom--p1 (Fine-grained reactivity)
Advocates say a fine-grained reactivity system, where only the specific parts of an app that need updating are updated, is the right model for a Rust web UI framework, contrasted implicitly with vdom-diffing frameworks.
Tag: tradeoff.
Claims: a-sR14-f005702-c1.

## fixed-point-loop-vs-event-retrigger

### fixed-point-loop-vs-event-retrigger--p1 (Simple, iterative, bounded)
Advocates kept a bounded iterative fixed-point loop over a more efficient graph-retrigger design because, in their own comparison, the iterative approach was the safer, bug-free option even though the alternative would have been more efficient.
Tag: tradeoff.
Claims: a-sa07-f003704-c2.

## fixed-vs-dynamic-matrix-sizing

### fixed-vs-dynamic-matrix-sizing--p1 (Prefer fixed/static sizing whenever possible)
Advocates say fixed, compile-time-known resizing should be preferred over dynamic resizing whenever possible, because dynamic resizing always produces heap-allocated results.
Tag: tradeoff.
Claims: a-sB01-f000217-c3.

## foreign-keys-vs-app-integrity

### foreign-keys-vs-app-integrity--app-enforced-integrity (Drop foreign keys; enforce integrity in application code)
Advocates report learning this the hard way: on an eventually consistent store, foreign-key checks broke across sequential writes, so all foreign keys were removed and referential integrity was moved into application code.
Tag: tradeoff.
Claims: b-sT07-f004166-c2.

## form-values-list-vs-scalar-deserialization

### form-values-list-vs-scalar-deserialization--p1 (Disambiguate scalar vs. list by observed value count, no schema change)
Advocates say for multi-valued elements like a multi-select, the deserializer should infer whether a field is a single value or a list from how many values were actually observed for it, rather than adding an explicit schema/cardinality marker to the wire data.
Tag: tradeoff.
Claims: a-01-f000543-c1.

## frontend-hook-naming

### frontend-hook-naming--p1 (use_ prefixed noun phrase)
Advocates, acknowledging no precise convention exists across the ecosystem, propose naming accessor-style hooks with a `use_<noun>` pattern (e.g. `use_search_query`, `use_location_hash`).
Tag: taste.
Claims: a-sR07-f002271-c2.

## fullstack-reactive-complexity-essential

### fullstack-reactive-complexity-essential--p1 (Essential, not accidental)
Advocates say the intimidating surface of a fullstack framework — many hooks, rules whose breakage produces silent misbehavior rather than a compiler or runtime error — reflects that fullstack apps are inherently complicated, not that the framework added complexity that wasn't needed.
Tag: tradeoff.
Claims: b-sb20-f007290-c2.

## futures-crate-vs-alternatives

### futures-crate-vs-alternatives--p1 (Avoid futures crate, use alternatives)
Advocates dropped the mainline `futures` crate entirely after finding bugs in its unsafe-heavy combinators (`FuturesUnordered`) that were impractical to fix upstream, replacing it with futures-lite for simple combinators, futures-buffered in place of `FuturesUnordered`, and futures-util only for what neither covers.
Tag: tradeoff.
Claims: b-sb17-f005159-c3.

## game-logic-in-scripting-layer

### game-logic-in-scripting-layer--p1 (Keep the native layer thin; put game logic in the hosted scripting language)
Advocates point to long-standing precedent — browser JavaScript games, and older engines like SCUMM and Another World — for putting effectively all game logic in the hosted language, keeping the unmanaged native layer a general-purpose platform with "nothing to do with the game," and treating serialized data files as the real source of truth rather than either language's live objects.
Tag: tradeoff.
Claims: b-sb26-f013214-c6.

## gamedev-ecosystem-maturity

### gamedev-ecosystem-maturity--p1 (Not yet ready for prime time)
Advocates describe the graphics crate ecosystem as tightly coupled, advancing in version lockstep with frequent breaking upgrades and documentation limited to rustdoc; across a multi-year production project, over half their time went to filing and chasing ecosystem bugs rather than the application itself, with only partial, incremental improvement over time.
Tag: fact.
Claims: b-sb26-f013214-c1.

### gamedev-ecosystem-maturity--p2 (Not a flop, just early)
Advocates frame the situation with the Gartner "Trough of Disillusionment" label as expected and fine, drawing an analogy to games staying on MS-DOS for years after Windows existed — the switch happened only once 3D accelerator cards forced it, not because Windows was inherently better — and argue Rust gamedev lacks an equivalent forcing function yet, so any transition will simply take years or decades.
Tag: taste.
Claims: b-sb26-f013214-c2.

## gating-pre-1-0-dependency-integrations

### gating-pre-1-0-dependency-integrations--p1 (Cfg-gate hidden impls, not unstable attribute)
Advocates say private structs and functions don't need to be documented as unstable at all; hidden impls can simply be `#[cfg(feature = "unstable")]`-gated instead.
Tag: tradeoff.
Claims: b-sb09-f002615-c1.

### gating-pre-1-0-dependency-integrations--p2 (Per function, not per block, annotation)
Advocates say the `#[unstable]` attribute belongs on each individual function, not on whole inherent impl blocks.
Tag: tradeoff.
Claims: b-sb09-f002615-c2.

### gating-pre-1-0-dependency-integrations--p3 (Blanket unstable flag)
Advocates defend the existing approach on the grounds that the impl is marked unstable specifically because the underlying dependency (ufmt) is itself still pre-1.0.
Tag: tradeoff.
Claims: b-sb09-f002615-c3.

### gating-pre-1-0-dependency-integrations--p4 (Need an explicit policy)
Advocates say ad hoc fixes — removing one dependency's integration, or debating one attribute's placement — don't resolve the underlying question; there are several such pre-1.0 optional dependencies (ufmt, rand-core, embassy-embedded-hal, log), and the project needs to work out a general policy for what to do with all of them, since neither a blanket-unstable flag nor per-dependency-version features feel fully right.
Tag: tradeoff.
Claims: b-sb09-f002615-c8, b-sb09-f002615-c5, b-sb09-f002615-c4.

### gating-pre-1-0-dependency-integrations--p5 (Per-dependency subfeature)
Advocates propose expanding the single "unstable" feature into named per-dependency sub-features, like `unstable-ufmt`.
Tag: tradeoff.
Claims: b-sb09-f002615-c6.

### gating-pre-1-0-dependency-integrations--p6 (Just remove and re-add on demand)
Advocates say it's simpler to remove an optional integration outright — as was already done for embedded-hal-nb — and re-add it later only if users complain, rather than spend more time designing feature-flag machinery than the removal itself would take.
Tag: tradeoff.
Claims: b-sb09-f002615-c7.

## generated-crates-escape-hatches

### generated-crates-escape-hatches--p1 (Generated crates need handwritten escape hatches)
Advocates report that even at ~95% codegen, a dedicated handwritten file holds trait impls and helpers that can't be inferred from the schema alone, and the generator is written to never overwrite that file.
Tag: tradeoff.
Claims: a-sa23-f011186-c4.

## generated-size-vs-runtime-performance

### generated-size-vs-runtime-performance--p1 (Favors performance over output size)
Advocates chose to generate JS bindings for WebIDL dictionary setters instead of using `Reflect`, explicitly accepting a larger Web API bindings size in exchange for better performance.
Tag: tradeoff.
Claims: b-sR03-f001160-c2.

## generic-over-blocking-async

### generic-over-blocking-async--p1 (Generic over mode)
Advocates say blocking and async constructors for a peripheral driver should share one implementation generic over the mode, rather than duplicating methods for each.
Tag: tradeoff.
Claims: b-sb05-f001512-c5.

## generics-vs-dyn-for-abstraction

### generics-vs-dyn-for-abstraction--static-by-default (Enums or generics; avoid dyn when possible)
Advocates rank `dyn Trait` as a valid but disproportionately costly dependency-injection mechanism next to generics and enums, arguing type erasure "often hurts more than it helps" and typically needs some motivation beyond making code look "more abstract"; in a case where a desired abstraction was pushed onto trait objects, advocates say trait objects are much less capable than generics for it and the abstraction is better supported with generics; elsewhere, a proposal replaces a trait's runtime type erasure and up/down-casting with a plain associated type instead.
Tag: tradeoff.
Claims: a-sa30-f013276-c4, a-sa30-f013276-c3, a-sa30-f013276-c7, a-sa07-f003704-c1.

### generics-vs-dyn-for-abstraction--p2 (Use trait objects instead of generic type parameters to cut code size, accepting slower indirect calls and lost per-type inlining)
Advocates say generic functions get monomorphized into one machine-code copy per concrete type, growing binary size, while trait objects emit a single dynamically-dispatched copy shared across types; the named trade is explicit — smaller code size against lost compiler optimization opportunities and added indirect-call overhead.
Tag: tradeoff.
Claims: a-sB02-f000256-c10, b-bk02-f000256-c9.

## git-storage-database-decentralized

### git-storage-database-decentralized--p1 (Rebuild Git's storage engine on a database and decentralize hosting)
Advocates argue centralized hosts can unilaterally access all repository data — for AI training, or deletion — so Git object storage should move into a distributed database, mirroring how Google's Piper and Meta's Sapling scale monorepos, layered with a peer-to-peer network so repositories can be cloned and pushed without depending on one central host.
Tag: tradeoff.
Claims: b-sb23-f011178-c1.

## global-statics-vs-per-request-state

### global-statics-vs-per-request-state--p1 (Prefer per-request scoped state)
Advocates say that once one instance can serve concurrent in-flight requests, any code relying on static, module-level, or `OnceCell` "global" state must be audited and moved to per-request state or given explicit synchronization.
Tag: tradeoff.
Claims: b-sR10-f004809-c2.

## gpu-async-await-vs-dsl

### gpu-async-await-vs-dsl--p1 (Reuse existing async model over a new DSL)
Advocates say Rust's `Future` trait and async/await already encode structured, composable concurrency inside an existing general-purpose language without committing to one execution model, so it can run unchanged on the GPU and reuse the existing async ecosystem (an embedded executor was ported with very few changes) — unlike JAX, Triton or CUDA Tile, which each require a new DSL/compiler stack and a break from existing CPU libraries — while acknowledging it still carries async/await's function-coloring problem.
Tag: tradeoff.
Claims: b-sb21-f008808-c1.

## greptimedb-write-api-choice

### greptimedb-write-api-choice--p1 (Pick the write API by workload shape, tune to the actual bottleneck)
Advocates present a benchmark (2M rows, 22-field schema) showing the Bulk API around 49% faster than the Regular API under compression, but frame the choice as workload-dependent rather than universal: a decision table routes real-time alerting/IoT/dashboards to the Regular API and ETL/log-collection/historical import to Bulk, with separate tuning guidance to match parallelism to whether the workload is network- or CPU-bound, and to prefer Zstd over LZ4 only when bandwidth rather than CPU is the constraint.
Tag: tradeoff.
Claims: b-sb25-f012642-c1.
