# Blind fill summaries, batch 1, file 05 (run b)

## fast-path-complexity--p1: Absolute magnitude decides
tag: tradeoff
Advocates hold that a fast path's worth is judged by its absolute per-call cost, not the relative percentage regression on old hardware; if removing a code path costs only tens of nanoseconds on current hardware, that absolute cost doesn't justify keeping the extra complexity, even when the relative slowdown looks dramatic on constrained devices like a Raspberry Pi.
Claims: b-sb04-f001392-c1

## fast-path-complexity--p2: Relative impact on constrained hw matters
tag: tradeoff
Advocates hold the opposite framing matters more: because a construct sits on a hot path used across huge volumes of rendered output, even a "relatively small" per-call regression compounds significantly on constrained/older hardware; their own benchmarks on low-power devices showed double-digit percentage regressions without the fast path, so relative impact on the hardware that most needs it is the number that should decide.
Claims: b-sb04-f001392-c2

## feature-flag-trunk-vs-long-branch--p1: Feature flag gate on trunk
tag: tradeoff
Advocates hold that keeping main always releasable requires gating experimental or breaking work behind a Cargo feature flag on trunk, rather than developing it on a long-lived branch.
Claims: b-bk03-f000267-c11

## feature-flags-vs-generic-wiring--p1: Generic wiring over feature flags
tag: tradeoff
Advocates hold that generic, type-level component wiring is less error-prone than Cargo feature flags because it lets every alternative implementation coexist and be tested simultaneously, instead of requiring combinatorial feature-flag test coverage.
Claims: a-sa16-f007175-c1

## feature-flags-vs-separate-crates--split-into-crates: Split into separate crates or modular crates joined by traits
tag: tradeoff
Advocates hold that functionality belongs in separate, independently-versioned crates rather than piling into one crate behind feature flags: components get moved into their own crates/repos to decouple release schedules and shrink the main crate's optional-feature surface; new integrations are kept out of main crates to keep releases fast; per-domain logic is split into sub-crates behind a stable, primitives-only interface crate so repository-facing types can change freely without breaking consumers; validation logic is factored into independently reusable library crates as an explicit scope boundary against a monolithic full node; and a single crate can turn itself into a workspace so only the required runtime piece need be linked, with the rest pulled in only on demand.
Claims: a-sR13-f004685-c2, b-sR05-f002151-c1, a-sa18-f008651-c1, b-bk03-f000267-c3, b-sR12-f005120-c1

## feature-flags-vs-separate-crates--p1: Modular library first
tag: taste
Advocates hold that a modular library comes first: build a small, general core and put everything else — rendering, parsing, networking, windowing — behind swappable trait-based pieces, arrived at after finding that pushing that same modularity into an existing large project met resistance ("do we have to do this?") rather than buy-in.
Claims: b-sb25-f011435-c1

## feature-misuse-responsibility--p1: Structure feature placement to discourage misuse
tag: taste
Advocates hold that where a feature lives affects who gets blamed for misusing it: putting a capability in a crate whose accidental inclusion has zero effect on the target platform lets misuse go unpunished, so relocating the feature to a crate whose unconditional inclusion is a more visible mistake is the better structural placement.
Claims: a-sa06-f003558-c3

## feature-misuse-responsibility--p2: Misuse is the misusing crate's bug, not the exposing crate's design problem
tag: taste
Advocates hold this is "a solution in search of a problem": crates cannot be engineered into behaving correctly by restructuring an API, misbehaving crates should have issues or PRs filed against them directly, and moving the feature elsewhere just relocates the same possible mistake rather than removing it.
Claims: a-sa06-f003558-c4

## feature-naming-mechanism-vs-capability--p1: Name a feature for its literal mechanism, not the capability it implies
tag: taste
Advocates hold a feature name should describe only the mechanism it literally provides; naming a hooking-only feature "tracking" wrongly implies the library itself does allocation tracking with little setup, so the name should be more explicit that it adds hooking and nothing more.
Claims: a-sa11-f004512-c5

## ffi-bindings-lag-pause-or-ship--p1: Pause and fix ffi first
tag: tradeoff
Advocates hold that shipping degraded non-Rust bindings every release, when the FFI story doesn't meet the "just works" bar the project holds Rust to, does more ecosystem harm than pausing bindings updates to fix the FFI/bridging story first, accepting the fragmentation risk of a pause as the lesser cost.
Claims: a-sa04-f002665-c1

## ffi-copy-vs-share--p2: Minimize copying/serializing across the JS↔wasm boundary; expose long-lived Rust data as opaque handles, return small copyable results
tag: tradeoff
Advocates hold that a good JS↔wasm interface minimizes copying and serialization by keeping large, long-lived data as Rust types living in wasm linear memory, exposed to JS only as opaque handles, with JS calling functions that do the heavy work and return small, copyable results; a delta/diff-based alternative is acknowledged as viable but not adopted because it is harder to implement.
Claims: a-sB02-f000256-c3, b-bk02-f000256-c2

## ffi-copy-vs-share--p3: Replace a Display-generated JS String with a raw pointer + Uint8Array overlay onto wasm linear memory
tag: tradeoff
Advocates hold that generating a Rust `String` and letting wasm-bindgen convert it into a JS string makes "unnecessary copies," and replace that with a render function returning a raw pointer so JS reads the buffer directly out of wasm linear memory via a `Uint8Array` overlay.
Claims: b-bk02-f000256-c3

## ffi-copy-vs-share--share-or-borrow: Pass borrowed references to avoid conversion overhead
tag: tradeoff
Advocates hold that passing `&str` rather than `String` across the boundary is the efficient choice, using references where possible instead of converting/copying, alongside minimizing call count and profile tuning.
Claims: b-sb22-f008914-c2

## ffi-copy-vs-share--convert-or-copy: Convert or copy into idiomatic types (copy across FFI, Rust collections, lean on generated glue)
tag: tradeoff
Advocates hold that copying immutable data out of a Rust result into an FFI struct, rather than sharing a pointer into it, is generally safer and easier: it costs a small performance penalty but guarantees that memory management on one side of the binding can't affect the other, which is judged worth it more often than not.
Claims: b-sb20-f007678-c2

## ffi-tag-unwind-vs-abort--p1: Tag unwinds explicitly
tag: tradeoff
Advocates hold that, given a choice between tagging all definitely-abort errors or all definitely-unwind errors to distinguish recoverable foreign exceptions from unrecoverable aborts, tagging the unwind case was the easier fit for their existing raw WAT-level exception-handling implementation.
Claims: a-sa12-f004598-c2

## ffi-ui-state-snapshots-vs-diffs--p1: Whole snapshot(chosen)
tag: tradeoff
Advocates hold that exposing the whole state as a pointer into linear memory each tick is the right call, naming a delta/diff-based design as a viable alternative that is not adopted because it is more difficult to implement.
Claims: a-sB02-f000256-c4

## ffi-ui-state-snapshots-vs-diffs--p2: Rust side tracks and emits diffs
tag: tradeoff
Advocates hold that, after iterating through worse designs (manual return-value wiring, per-field event handlers, an all-optional model needing manual checks), the Rust side should track field changes and emit a diff enum via a derive macro, so the receiving side applies it through an exhaustive switch that fails to compile if a new field goes unhandled.
Claims: a-sa18-f008389-c1

## fields-in-traits--p1: Mildly supportive uncertain use case
tag: taste
Advocates hold fields-in-traits is a limited, distinct-enough feature that "doesn't seem bad in any way," while conceding they personally don't have a compelling use case for it — support without conviction.
Claims: b-sb19-f007207-c1

## final-trait-methods--p1: Support final methods
tag: taste
Advocates hold Rust should add final/non-overridable trait methods: one points to an already-drafted RFC using the reserved `final` keyword to let any trait forbid overriding specific methods, and another proposes a `#[non_overridable]` attribute for extension methods whose override could cause correctness bugs, potentially shrinking vtables by excluding such methods.
Claims: a-sa19-f009316-c2, a-sa19-f009316-c1

## final-trait-methods--p2: Skeptical limited value vs free functions
tag: taste
Advocates hold final trait methods offer little beyond "minor sugar," since any trait bound or call used inside such a method could just as well be replicated with a corresponding free function.
Claims: a-sa19-f009316-c3

## final-trait-methods--p3: Final methods need vtable for soundness
tag: fact
Advocates hold that final trait methods cannot simply desugar to free functions and must remain reachable through the vtable for soundness: a concrete example shows a final method called through `dyn Trait` observably differing from an equivalent free function, and a filed I-unsound bug shows nightly's experimental final associated functions already misbehave inconsistently under `dyn Trait` dispatch.
Claims: a-sa19-f009316-c4, a-sa19-f009316-c5

## fine-grained-reactivity-vs-vdom--p1: Fine grained reactivity
tag: tradeoff
Advocates hold that fine-grained reactivity is the right model because only the parts of the app that need to update actually do, contrasted implicitly with virtual-DOM diffing frameworks.
Claims: a-sR14-f005702-c1

## fixed-point-loop-vs-event-retrigger--p1: Simple iterative bounded
tag: tradeoff
Advocates hold that a simple, bounded iterative fixed-point loop (reduced from 100 passes to 10) is the safer, bug-free choice over a more efficient but more complex graph-retrigger design.
Claims: a-sa07-f003704-c2

## fixed-vs-dynamic-matrix-sizing--p1: Prefer fixed/static sizing whenever possible
tag: fact
Advocates hold that fixed, compile-time-known matrix sizing should be preferred whenever possible, because dynamic resizing always produces heap-allocated results when the output size can't be deduced at compile time.
Claims: a-sB01-f000217-c3

## foreign-keys-vs-app-integrity--app-enforced-integrity: Drop foreign keys; enforce integrity in application code
tag: tradeoff
Advocates hold that on eventually consistent storage, database foreign keys should be dropped and referential integrity enforced in application code instead, after finding that FK checks broke across sequential writes under eventual consistency.
Claims: b-sT07-f004166-c2

## form-values-list-vs-scalar-deserialization--p1: Disambiguate scalar vs. list by observed value count (no schema change)
tag: taste
Advocates hold that for multi-valued form elements like a `<select multiple>`, a deserializer should infer scalar-vs-list per field from how many values were actually observed, rather than adding an explicit schema/cardinality marker to the wire format.
Claims: a-01-f000543-c1

## frontend-hook-naming--p1: Use_ prefixed noun phrase
tag: taste
Advocates hold that, absent any established convention, hooks should be named with a `use_<noun>` pattern (e.g. `use_search_query`, `use_location_hash`).
Claims: a-sR07-f002271-c2

## fullstack-reactive-complexity-essential--p1: The hooks/reactivity complexity in a fullstack framework is essential, not accidental
tag: fact
Advocates hold that the complexity practitioners feel around a fullstack framework's hooks and reactivity — including that breaking hook rules silently misbehaves rather than erroring — reflects that "full stack stuff is complicated," not that the framework added complexity that wasn't needed.
Claims: b-sb20-f007290-c2

## futures-crate-vs-alternatives--p1: Avoid futures crate use alternatives
tag: tradeoff
Advocates hold that, after finding bugs in the `futures` crate's unsafe-heavy combinators (e.g. `FuturesUnordered`) that were impractical to fix upstream, it's better to drop the `futures` dependency entirely and assemble the needed functionality from futures-lite, futures-buffered and futures-util instead.
Claims: b-sb17-f005159-c3

## game-logic-in-scripting-layer--p1: Keep the native (Rust) layer a thin, general-purpose platform and put effectively all game logic in the hosted scripting/VM language
tag: taste
Advocates hold that, per long-standing precedent (browser JS games, SCUMM, Another World), essentially all game logic should live in the hosted scripting language, with the unmanaged native layer staying a general-purpose platform that has "nothing to do with the game," and the real state of record living in serialized data files rather than in either language's live objects.
Claims: b-sb26-f013214-c6

## gamedev-ecosystem-maturity--p1: not yet "ready for prime time"
tag: fact
Advocates hold that Rust's 3D/graphics crate ecosystem "isn't ready for prime time": the crates are tightly coupled with frequent breaking upgrades and rustdoc-only documentation, and over half of three years on a demanding project went to filing and chasing ecosystem bugs rather than the actual application, with only partial, incremental improvement over time.
Claims: b-sb26-f013214-c1

## gamedev-ecosystem-maturity--p2: not a flop, just early
tag: taste
Advocates hold this is simply the expected "Trough of Disillusionment," not a flop: game-industry technology adoption is inherently slow regardless of a technology's merits (as with the MS-DOS-to-Windows transition, which needed 3D accelerator cards as a forcing function), and Rust gamedev lacks an equivalent forcing function yet, so any transition will take years or decades.
Claims: b-sb26-f013214-c2

## gating-pre-1-0-dependency-integrations--p1: Cfg gate hidden impls not unstable attribute
tag: taste
Advocates hold private structs/functions don't need to be documented as `#[unstable]`; hidden impls can simply be `#[cfg(feature = "unstable")]`-gated instead.
Claims: b-sb09-f002615-c1

## gating-pre-1-0-dependency-integrations--p2: Per function not per block annotation
tag: taste
Advocates hold the `#[unstable]` attribute should sit on each individual function rather than on a whole inherent impl block.
Claims: b-sb09-f002615-c2

## gating-pre-1-0-dependency-integrations--p3: Blanket unstable flag
tag: tradeoff
Advocates hold gating behind one coarse "unstable" flag is justified because the underlying dependency (`ufmt`) is itself still pre-1.0.
Claims: b-sb09-f002615-c3

## gating-pre-1-0-dependency-integrations--p4: Need an explicit policy
tag: taste
Advocates hold that ad hoc fixes — removing one dependency's integration, or picking blanket-vs-per-dependency gating case by case — don't resolve the underlying question, since other pre-1.0 dependencies (rand-core, embassy-embedded-hal, log) raise the same issue; neither extreme (one coarse flag, or per-dependency-version features) feels right, and the project needs a general policy for handling pre-1.0 optional trait dependencies.
Claims: b-sb09-f002615-c8, b-sb09-f002615-c5, b-sb09-f002615-c4

## gating-pre-1-0-dependency-integrations--p5: Per dependency subfeature
tag: tradeoff
Advocates hold the "unstable" feature should be expanded into named per-dependency sub-features (e.g. `unstable-ufmt`).
Claims: b-sb09-f002615-c6

## gating-pre-1-0-dependency-integrations--p6: Just remove and readd on demand
tag: taste
Advocates hold it's simpler to just remove an optional integration (as was done for embedded-hal-nb) and re-add it later if users complain, rather than spend time designing feature-flag machinery for it.
Claims: b-sb09-f002615-c7

## generated-crates-escape-hatches--p1: Generated crates need handwritten escape hatches
tag: tradeoff
Advocates hold that even a ~95%-generated crate needs a dedicated handwritten file for what the schema can't express (e.g. arithmetic trait impls on a generated type), with the generator written to never overwrite that file.
Claims: a-sa23-f011186-c4

## generated-size-vs-runtime-performance--p1: Favors performance over output size for this change
tag: tradeoff
Advocates hold that generating JS bindings for WebIDL dictionary setters instead of using `Reflect` is worth the larger binding size because it's more performant.
Claims: b-sR03-f001160-c2

## generic-over-blocking-async--p1: Generic over mode
tag: tradeoff
Advocates hold blocking and async variants of a peripheral driver should share one implementation generic over the mode, rather than duplicating methods for each.
Claims: b-sb05-f001512-c5

## generics-vs-dyn-for-abstraction--static-by-default: Enums or generics; avoid `dyn` when possible
tag: taste
Advocates hold that generics/enums should be favored over `dyn Trait` by default: `dyn Trait` is a valid dependency-injection mechanism but its benefits are "extremely narrow" relative to its downsides, type erasure "often hurts more than it helps" without a motivation beyond looking "more abstract," trait objects are "not nearly as capable as generics" for some abstractions, and one maintainer proposed replacing a trait's runtime type erasure and up/down-casting with an associated type instead.
Claims: a-sa30-f013276-c4, a-sa30-f013276-c3, a-sa30-f013276-c7, a-sa07-f003704-c1

## generics-vs-dyn-for-abstraction--p2: Use trait objects instead of generic type parameters to cut code size, accepting slower indirect calls and lost per-type inlining
tag: tradeoff
Advocates hold that using trait objects instead of generic type parameters is worth it to shrink `.wasm` code size, since monomorphized generics emit one function copy per concrete type: the explicit cost is losing compiler optimization opportunities and per-type inlining, paid for indirect, dynamically dispatched calls.
Claims: a-sB02-f000256-c10, b-bk02-f000256-c9

## git-storage-database-decentralized--p1: Rebuild Git's storage engine on a database and decentralize hosting rather than depend on a centralized host
tag: taste
Advocates hold that because centralized hosts like GitHub can unilaterally access all data or use it for AI training or deletion, Git object storage should move into a distributed database (mirroring Google Piper and Meta Sapling) with a P2P network layered on top, so repositories can be cloned and pushed without depending on any single central node.
Claims: b-sb23-f011178-c1

## global-statics-vs-per-request-state--p1: Prefer per request scoped state
tag: fact
Advocates hold that once one instance can serve concurrent in-flight requests, any static, module-level, or `OnceCell` "global" state must be audited and moved to per-request state or explicit synchronization.
Claims: b-sR10-f004809-c2

## gpu-async-await-vs-dsl--p1: Reuse existing async model over new dsl
tag: tradeoff
Advocates hold that Rust's `Future` trait and async/await already provide the right abstraction for structured, composable GPU concurrency — encoded in an existing language without committing to a specific execution model, letting an existing executor (Embassy) be ported with very few changes — over building a new purpose-built DSL/compiler stack like JAX, Triton or CUDA Tile, while acknowledging it still carries async/await's function-coloring problem.
Claims: b-sb21-f008808-c1

## greptimedb-write-api-choice--p1: Pick the write API by workload shape
tag: fact
Advocates hold the choice between GreptimeDB's Regular and Bulk Stream Insert write APIs should be made by workload shape — Regular for real-time alerting/IoT/dashboards, Bulk for ETL/log collection/historical import — backed by a benchmark showing Bulk ~49% faster under compression (155,099 vs 104,237 rows/s on 2M rows), with parallelism and compression (Zstd vs LZ4) tuned to whichever resource is actually the bottleneck.
Claims: b-sb25-f012642-c1
