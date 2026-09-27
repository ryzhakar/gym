# Blind fill input, batch 1, file 05 of 13

For each Claim below, name the one Position of its Question that the Claim supports (a Position id from the list), or `none` if it supports none of them. The Claims are in random order.

## Question `fast-path-complexity`

When a hand-tuned "fast path" optimization gives a large relative speedup on constrained/older hardware but a negligible absolute one on modern hardware, should a library keep the extra code complexity for the fast path, or drop it and favor the simpler code?

Positions:
- `fast-path-complexity--p1`: Absolute magnitude decides
- `fast-path-complexity--p2`: Relative impact on constrained hw matters

Claims:
- `b-sb04-f001392-c2` · Voice: EdJoPaTo · Source: https://github.com/ratatui/ratatui/pull/1089 (`f001392`) · Date: 2024-05-11 · Locator: PR #1089, comment 2024-05-11T09:13:41Z
  - Quote: "Relatively small improvements will impact a lot of code depending on it."
  - Paraphrase: argues the fast path is worth keeping because `Line` is one of the most-used core constructs and `Alignment::Left` is the common default, so a "relatively small" per-call regression compounds across hundreds of rendered cells per frame on low-power devices (own benchmarks on Raspberry Pi 1/2/4 showed 12-38% regressions without it)
- `b-sb04-f001392-c1` · Voice: joshka · Source: https://github.com/ratatui/ratatui/pull/1089 (`f001392`) · Date: 2024-05-11 · Locator: PR #1089, comment 2024-05-11T01:36:36Z
  - Quote: "It's important to look the absolute magnitude of a perf gain, and not just the relative amount."
  - Paraphrase: argues the fast path for left-aligned lines should be removed because, while the relative regression on a Raspberry Pi looks large, the absolute per-frame cost (~30ns on an M2 Mac) is not worth the added code complexity

## Question `feature-flag-trunk-vs-long-branch`

Should incomplete or breaking Rust work be merged to main behind a Cargo feature flag (trunk-based development), or kept on a long-lived branch?

Positions:
- `feature-flag-trunk-vs-long-branch--p1`: Feature flag gate on trunk
- `feature-flag-trunk-vs-long-branch--alt1`: Keep the work on a long-lived branch

Claims:
- `b-bk03-f000267-c11` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Zebra versioning and releases § Feature Flags
  - Quote: "To keep the main branch in a releasable state, experimental features must be gated behind a Rust feature flag."
  - Paraphrase: to keep main always releasable, experimental features and (unless urgent) breaking changes must be gated behind a Rust/Cargo feature flag rather than developed on a long-lived branch

## Question `feature-flags-vs-generic-wiring`

Should optional/alternate implementations in a Rust library be selected via Cargo feature flags, or via generic type-level component wiring (traits/generics, e.g. CGP-style)?

Positions:
- `feature-flags-vs-generic-wiring--p1`: Generic wiring over feature flags
- `feature-flags-vs-generic-wiring--alt1`: Select implementations with Cargo feature flags

Claims:
- `a-sa16-f007175-c1` · Voice: Soares Chen · Source: https://contextgeneric.dev/blog/hypershell-release (`f007175`) · Date: 2025-06-14 · Locator: § Modularity of HandleSimpleExec
  - Quote: "This generic approach is also less error-prone than feature flags, as all alternative implementations can coexist and be tested simultaneously"
  - Paraphrase: CGP-style generic component wiring lets alternative implementations coexist and be tested together, avoiding the combinatorial-testing burden of Cargo feature flags.

## Question `feature-flags-vs-separate-crates`

Should functionality live in one crate (feature flags, in-tree, a monolithic binary) or in separate, independently usable crates?

Positions:
- `feature-flags-vs-separate-crates--split-into-crates`: Split into separate crates or modular crates joined by traits
- `feature-flags-vs-separate-crates--p1`: Modular library first

Claims:
- `a-sR13-f004685-c2` · Voice: iroh/n0 (Friedel Ziegelmayer & Rüdiger Klaehn, post authors) · Source: https://iroh.computer/blog/iroh-1-0-0-rc-0 (`f004685`) · Date: 2026-05-11 · Locator: § "Sometimes things have to move out"
  - Quote: "This allows us to have a different versioning and release schedule for these components. It is also helpful to reduce the number of optional features in iroh."
  - Paraphrase: `DhtAddressLookup`, `MdnsAddressLookup` and `AccessLimit` were moved out of the `iroh` crate into their own crates/repos to allow independent versioning and release schedules and to reduce the number of optional features in the main crate
- `b-sR05-f002151-c1` · Voice: benwis (Leptos maintainer) · Source: https://github.com/leptos-rs/leptos/pull/3063 (`f002151`) · Date: 2024-10-06 · Locator: leptos-rs/leptos#3063, comment 2024-10-06T02:05:17Z. · L1097-L1100.
  - Quote: "We're keeping most new integrations out of the main crates to reduce the time needed to release a new feature."
  - Paraphrase: keep new integrations out of the main crates.
- `a-sa18-f008651-c1` · Voice: Michael de Silva · Source: https://crustyengineer.com/blog/axum-multi-tenancy-abstract-repository-layer (`f008651`) · Date: 2025-10-19 · Locator: "Another 'abstraction' to the repository layer" section
  - Quote: "the sub-crates only care about primitive types... types used by the repository interface can change (as much as they need to), without impacting the sub-crate API."
  - Paraphrase: splits Postgres access into per-domain sub-crates (e.g. `accounts`, `payments`) behind an `interfaces` crate, arguing this keeps sub-crate public APIs stable (they only deal in primitive types) while the repository-facing types can change freely, and lets the Postgres stack be shared with another engineer decoupled from the host Axum app; explicitly flags this against a critique ("daymare was just commenting on the need for constant abstractions") without fully rebutting it, and closes by asking readers whether this is extreme
- `b-sb25-f011435-c1` · Voice: Nico (Blitz/Dioxus Labs; maintains Servo-adjacent Blitz, Taffy, blessed.rs) · Source: https://youtube.com/watch?v=J1KcRkV_fvk (`f011435`) · Date: 2026-06-11 · Locator: ~10:14-11:16
  - Quote: "I was getting a lot of more like do we have to do this?"
  - Paraphrase: after contributing modularity work to Servo and getting "do we have to do this?" rather than buy-in, he concluded a separate project was needed; Blitz is built around a small core (BlitzDom: DOM tree, layout, styling) with everything else — rendering, HTML parsing, networking, windowing — behind traits as swappable/reusable pieces
- `b-bk03-f000267-c3` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Design Overview § Architecture; Contributing § Pull Requests
  - Quote: "Zebra has a modular, library-first design, with the intent that each component can be independently reused outside of the zebrad full node"
  - Paraphrase: in contrast to zcashd's monolithic architecture inherited from its Bitcoin Core fork origins, Zebra is factored into independently reusable library crates (zebra-chain, zebra-network, zebra-state, etc.) so each can be reused outside the zebrad full node; the contributing guide names this as a scope boundary — Zebra stays a minimal validator node and pushes wallets, explorers, and mining pools to separate projects (Zaino, Zallet, librustzcash)
- `b-sR12-f005120-c1` · Voice: Arthur Zucker / Hugging Face tokenizers team · Source: https://huggingface.co/blog/tokenizers-v1 (`f005120`) · Date: 2026-09-21 · Locator: table row "workspace split" / "Progress Towards V1"
  - Quote: "one crate became a workspace: tk-encode is the required runtime, and tk-serialize, tk-convert and tk-train are linked only when an application needs them."
  - Paraphrase: the single tokenizers crate became a workspace so `tk-encode` is the only required runtime piece and `tk-serialize`, `tk-convert`, `tk-train` are linked only when an application actually needs them

## Question `feature-misuse-responsibility`

When an opt-in crate feature can be misused by downstream crates (enabled unconditionally "for convenience"), is it the exposing crate's job to structure the API/placement to make misuse harder, or the misusing crate's bug to fix?

Positions:
- `feature-misuse-responsibility--p1`: Structure feature placement to discourage misuse
- `feature-misuse-responsibility--p2`: Misuse is the misusing crate's bug, not the exposing crate's design problem

Claims:
- `a-sa06-f003558-c4` · Voice: Pauan · Source: https://github.com/wasm-bindgen/wasm-bindgen/issues/4667 (`f003558`) · Date: 2025-09-21 · Locator: comment 2025-09-21T22:11:14Z; 2025-09-21T22:31:20Z
  - Quote: "This seems to me like a solution in search of a problem"
  - Paraphrase: rejects the "protect against misuse" framing outright, arguing crates cannot be forced to behave properly by restructuring the API, that misbehaving crates should have issues/PRs filed against them directly, and that shifting the feature to `js-sys` only relocates the same possible mistake
- `a-sa06-f003558-c3` · Voice: newpavlov · Source: https://github.com/wasm-bindgen/wasm-bindgen/issues/4667 (`f003558`) · Date: 2025-09-19 · Locator: comment 2025-09-19T16:28:13Z
  - Quote: "such incorrect behavior does not get punished, while users would be more careful with js-sys"
  - Paraphrase: prefers the feature live in `js-sys` rather than `getrandom` directly, reasoning that a crate wrongly adding `js-sys` unconditionally is a more visible/unlikely mistake than wrongly enabling a `getrandom` feature, since the latter has no effect on non-WASM targets and so goes unpunished

## Question `feature-naming-mechanism-vs-capability`

Should a feature's name describe only the literal mechanism it provides, or the higher-level capability that mechanism enables, when the feature itself is just the low-level primitive?

Positions:
- `feature-naming-mechanism-vs-capability--p1`: Name a feature for its literal mechanism, not the capability it implies
- `feature-naming-mechanism-vs-capability--alt1`: Name the feature for the capability it enables

Claims:
- `a-sa11-f004512-c5` · Voice: AnthonyGrondin · Source: https://github.com/esp-rs/esp-hal/pull/5296 (`f004512`) · Date: 2026-04-01 · Locator: comment 2026-04-01T17:33:09Z
  - Quote: "to me, `tracking` implies that the library itself is taking care of allocation tracking, without requiring much setup from the user. I think it should be more explicit, that this feature is simply adding hooking, and nothing more."
  - Paraphrase: objects that "tracking" implies the library itself tracks allocations with little setup, when the feature really just adds hooking and nothing more, and argues the name should be more explicit about that

## Question `ffi-bindings-lag-pause-or-ship`

When a Rust library's non-Rust-language FFI bindings lag behind the quality of its native Rust API, should maintainers keep shipping degraded bindings on every release, or pause bindings updates until the FFI/bridging story itself is fixed, accepting ecosystem-fragmentation risk in the meantime?

Positions:
- `ffi-bindings-lag-pause-or-ship--p1`: Pause and fix ffi first
- `ffi-bindings-lag-pause-or-ship--alt1`: Keep shipping the bindings every release

Claims:
- `a-sa04-f002665-c1` · Voice: b5 · Source: https://iroh.computer/blog/ffi-updates (`f002665`) · Date: 2025-02-12 · Locator: opening section ("Why?")
  - Quote: "Because we don't think our FFI story is good enough right now. Our promise is to ship \"P2P that works\", and we're not hitting that \"just works\" experience in languages that aren't rust."
  - Paraphrase: announces iroh will stop updating its Kotlin/Python/Swift/JavaScript FFI bindings on every release because the FFI experience doesn't yet match the "just works" bar the project holds Rust usage to, and because degraded bindings risk fragmenting the protocol ecosystem across languages

## Question `ffi-copy-vs-share`

At a Rust FFI or JS boundary, should data be copied or serialized across, or shared by reference or opaque handle?

Positions:
- `ffi-copy-vs-share--convert-or-copy`: Convert or copy into idiomatic types (copy across FFI, Rust collections, lean on generated glue)
- `ffi-copy-vs-share--share-or-borrow`: Pass borrowed references to avoid conversion overhead
- `ffi-copy-vs-share--p1`: Opaque handles(recommended)
- `ffi-copy-vs-share--p2`: Minimize copying/serializing across the JS↔wasm boundary; expose long-lived Rust data as opaque handles, return small copyable results
- `ffi-copy-vs-share--p3`: Replace a Display-generated JS String with a raw pointer + Uint8Array overlay onto wasm linear memory

Claims:
- `a-sB02-f000256-c3` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "Interfacing Rust and JavaScript"
  - Quote: "we want to optimize for the following properties: Minimizing copying... Minimizing serializing and deserializing."
  - Paraphrase: a good JS↔wasm interface keeps large, long-lived data as Rust types living in wasm linear memory, exposed to JS only as opaque handles, to minimize copying and serialization overhead across the boundary.
- `b-bk02-f000256-c3` · Voice: rustwasm working group (Rust and WebAssembly book) [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: unknown (living doc) · Locator: § "Rendering to Canvas Directly from Memory"
  - Quote: "Generating (and allocating) a String in Rust and then having wasm-bindgen convert it to a valid JavaScript string makes unnecessary copies of the universe's cells."
  - Paraphrase: the tutorial's initial render() returns a Rust-formatted String, which it then names as a source of "unnecessary copies," and replaces it with a pointer-returning render so JS reads the cell buffer directly out of wasm memory.
- `b-sb22-f008914-c2` · Voice: Chayan Mistry · Source: https://chayanmistry.medium.com/rust-in-android-development-complete-guide-5f3313f40e50 (`f008914`) · Date: 2026-05-12 · Locator: section "Performance Considerations," subsection "2. Use Appropriate Data Types"
  - Quote: "✅ Efficient: Use references when possible"
  - Paraphrase: contrasts `pub fn process_string(s: String) -> String` (marked inefficient, string-conversion overhead) with `pub fn process_string(s: &str) -> String` (marked efficient), as one of four listed performance practices alongside minimizing JNI call count and release-profile tuning
- `b-sb20-f007678-c2` · Voice: Emily Dixon · Source: https://mux.com/blog/practical-client-side-rust-for-android-ios-and-web (`f007678`) · Date: 2023-12-13 · Locator: section "Rust for Android," paragraph beginning "On the Rust side, you'll need to encapsulate"
  - Quote: "Copying immutable data is generally safer and easier than trying to share it."
  - Paraphrase: creating an FFI struct that copies out of the Rust result object (rather than sharing a pointer into it) costs a small performance penalty but guarantees memory management on one side of a binding can't affect the other side, which the author judges worth it "more often than not"
- `b-bk02-f000256-c2` · Voice: rustwasm working group (Rust and WebAssembly book) [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: unknown (living doc) · Locator: § "Interfacing Rust and JavaScript"
  - Quote: "a good JavaScript↔WebAssembly interface design is often one where large, long-lived data structures are implemented as Rust types that live in the WebAssembly linear memory, and are exposed to JavaScript as opaque handles."
  - Paraphrase: states a general interface-design rule of thumb for wasm_bindgen boundaries — large, long-lived structures should live in Rust/wasm linear memory and be exposed to JS only as opaque handles, with JS calling functions that do the heavy work and return small results, to avoid copy/serialize overhead; separately names "return only the cells that changed" (a delta-based design) as a viable alternative it does not adopt, citing implementation difficulty.

## Question `ffi-tag-unwind-vs-abort`

When an FFI/Wasm boundary must distinguish recoverable foreign exceptions from unrecoverable aborts, should the recoverable (unwind) case be explicitly tagged, or the unrecoverable (abort) case?

Positions:
- `ffi-tag-unwind-vs-abort--p1`: Tag unwinds explicitly
- `ffi-tag-unwind-vs-abort--alt1`: Tag the abort case explicitly

Claims:
- `a-sa12-f004598-c2` · Voice: Guy Bedford, Hood Chatham, and Logan Gatlin · Source: https://blog.cloudflare.com/making-rust-workers-reliable (`f004598`) · Date: 2026-04-22 · Locator: blog post, § "Abort recovery"
  - Quote: "We had two options to solve this technically: either mark all errors which are definitely aborts, or mark all errors which are definitely unwinds. Either could have worked but we chose the latter."
  - Paraphrase: chose to mark all definitely-unwind errors with exception tags, rather than marking all definitely-abort errors, to distinguish recoverable foreign exceptions from unrecoverable aborts at the Wasm boundary, because their existing raw WAT-level Exception Handling implementation made that direction easier

## Question `ffi-ui-state-snapshots-vs-diffs`

When Rust pushes state across a boundary to a UI, send whole snapshots or only deltas?

Positions:
- `ffi-ui-state-snapshots-vs-diffs--p1`: Whole snapshot(chosen)
- `ffi-ui-state-snapshots-vs-diffs--p2`: Rust side tracks and emits diffs

Claims:
- `a-sB02-f000256-c4` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "Interfacing Rust and JavaScript in our Game of Life"
  - Quote: "Another viable design alternative would be for Rust to return a list of every cell that changed states after each tick... The trade off is that this delta-based design is slightly more difficult to implement."
  - Paraphrase: the tutorial exposes the whole universe (as a pointer into linear memory) each tick rather than the delta-based design, naming the delta approach as a viable but harder-to-implement alternative.
- `a-sa18-f008389-c1` · Voice: TantalusPath (Serendipity Systems LLC) · Source: https://tantaluspath.com/tech/rust_to_swift_state_syncing (`f008389`) · Date: 2025-03-27 · Locator: "How procedural macros made it better" section
  - Quote: "If a state field is added or removed on the Rust side, this Swift function will fail compilers' enum exhaustiveness checks until it is added."
  - Paraphrase: after iterating through three worse designs (manual return-value wiring, one-function-per-field event handlers, an all-optional `StateUpdateModel` requiring manual `Some`-checking on the Swift side), settled on a derive proc macro that generates a companion struct plus a diff enum, so the Rust side tracks uncommitted field changes and the Swift side gets a `[FieldValue]` diff it applies via an exhaustive `switch`, which the Swift compiler will fail to build if a new field isn't handled

## Question `fields-in-traits`

Should Rust add "fields in traits" (a shared field, accessed through a vtable offset on `dyn Trait`, that every implementor must provide)?

Positions:
- `fields-in-traits--p1`: Mildly supportive uncertain use case
- `fields-in-traits--alt1`: Do not add fields in traits

Claims:
- `b-sb19-f007207-c1` · Voice: Jimmy Hartzell · Source: https://thecodedmessage.com/posts/rust-features-2 (`f007207`) · Date: 2025-07-21 · Locator: § "Merits of the Proposal"
  - Quote: "my conclusion comes out to a shrug. This feature doesn't seem bad in any way... But I personally don't engage with a use case for it."
  - Paraphrase: fields-in-traits is a limited, distinct-enough feature that wouldn't harm Rust's design, but he doesn't personally have a compelling use case for it

## Question `final-trait-methods`

Should Rust add `final`/non-overridable trait methods, and if so, must such methods still participate in dynamic dispatch (vtables) for soundness?

Positions:
- `final-trait-methods--p1`: Support final methods
- `final-trait-methods--p2`: Skeptical limited value vs free functions
- `final-trait-methods--p3`: Final methods need vtable for soundness

Claims:
- `a-sa19-f009316-c4` · Voice: SkiFire13 · Source: https://internals.rust-lang.org/t/idea-trait-methods-with-un-overridable-implementations/23906 (`f009316`) · Date: 2026-01-08 · Locator: reply, 2026-01-08T21:16:18.959Z
  - Quote: "The .baz() method prints () because it's being monomorphized for () and inserted into the vtable, while the baz function call prints dyn playground::Foo..."
  - Paraphrase: Constructs a concrete example where a final method called through `dyn Trait` observably differs from an equivalent generic free function (via `TypeId::of::<Self>` vs. the erased type), showing final methods cannot simply desugar to free functions and must remain reachable via the vtable.
- `a-sa19-f009316-c5` · Voice: eggyal · Source: https://internals.rust-lang.org/t/idea-trait-methods-with-un-overridable-implementations/23906 (`f009316`) · Date: 2026-03-12 · Locator: linked rust-lang/rust issue (opened 2026-03-10), cited 2026-03-12T06:00:48.747Z
  - Quote: "`final` methods should work the same as without it (if it works without it)"
  - Paraphrase: Filed an I-unsound bug showing nightly's experimental `final` associated functions behave inconsistently with `dyn Trait` dispatch (an `assert_ne!` on `TypeId::of` via `dyn Trait` fails), confirming the vtable/soundness concern is a live, unresolved implementation problem rather than a purely theoretical one.
- `a-sa19-f009316-c2` · Voice: josh · Source: https://internals.rust-lang.org/t/idea-trait-methods-with-un-overridable-implementations/23906 (`f009316`) · Date: 2024-08-13 · Locator: linked RFC (joshtriplett/rfcs "final"), cited 2026-01-07T21:42:35.707Z
  - Quote: "Support restricting implementation of individual methods within traits, using the already reserved `final` keyword."
  - Paraphrase: Points to an already-drafted RFC ("Trait method impl restrictions", using the reserved `final` keyword) letting any trait forbid overriding specific methods or associated functions.
- `a-sa19-f009316-c1` · Voice: newpavlov · Source: https://internals.rust-lang.org/t/idea-trait-methods-with-un-overridable-implementations/23906 (`f009316`) · Date: 2026-01-07 · Locator: OP, 2026-01-07T21:26:16.248Z
  - Quote: "I think something like #[non_overridable] could be a useful addition to the language."
  - Paraphrase: Proposes a `#[non_overridable]` attribute for trait extension methods whose override could cause correctness bugs, potentially excluding such methods from vtables to shrink them.
- `a-sa19-f009316-c3` · Voice: afetisov · Source: https://internals.rust-lang.org/t/idea-trait-methods-with-un-overridable-implementations/23906 (`f009316`) · Date: 2026-01-08 · Locator: reply, 2026-01-08T14:37:33.435Z
  - Quote: "Surely there are other benefits, besides minor sugar, for a new feature? Personally I can't think of any."
  - Paraphrase: Doubts final methods offer real benefit beyond "minor sugar", since any trait bound or call used inside a final method can just as well be replicated with a corresponding free function.

## Question `fine-grained-reactivity-vs-vdom`

should a Rust web UI framework use fine-grained (signal-based) reactivity or virtual-DOM diffing

Positions:
- `fine-grained-reactivity-vs-vdom--p1`: Fine grained reactivity
- `fine-grained-reactivity-vs-vdom--alt1`: Virtual-DOM diffing

Claims:
- `a-sR14-f005702-c1` · Voice: Sycamore · Source: https://sycamore.dev (`f005702`) · Date: 2026-04-01 · Locator: front page, "Fine-Grained Reactivity" feature blurb
  - Quote: "Sycamore's reactivity system is fine-grained, meaning that only the parts of your app that need to be updated will be."
  - Paraphrase: fine-grained reactivity is the right model, contrasted implicitly with vdom-diffing frameworks (e.g. Yew).

## Question `fixed-point-loop-vs-event-retrigger`

Should a bounded, safety-first multi-pass graph algorithm favor a simple iterative fixed-point loop, or a more complex event-driven re-trigger design?

Positions:
- `fixed-point-loop-vs-event-retrigger--p1`: Simple iterative bounded
- `fixed-point-loop-vs-event-retrigger--alt1`: Event-driven re-trigger design

Claims:
- `a-sa07-f003704-c2` · Voice: antimora · Source: https://github.com/tracel-ai/burn/pull/3872 (`f003704`) · Date: 2025-11-07 · Locator: PR #3872, comment 2025-11-07T17:03:28Z
  - Quote: "this iterative approached was the safest and bug free compared to graph re-trigger approach, which would have been more efficient but it was complex"
  - Paraphrase: kept the iterative type-inference loop (bounded to 10 passes, down from 100) over a more efficient graph-retrigger design because the iterative approach was safer and bug-free

## Question `fixed-vs-dynamic-matrix-sizing`

When a matrix's size is known at compile time, should code prefer fixed (stack-allocated) resizing/operations over dynamic (heap-allocated) ones?

Positions:
- `fixed-vs-dynamic-matrix-sizing--p1`: Prefer fixed/static sizing whenever possible
- `fixed-vs-dynamic-matrix-sizing--alt1`: Dynamic, heap-allocated sizing

Claims:
- `a-sB01-f000217-c3` · Voice: Dimforge (nalgebra maintainers) · Source: https://nalgebra.org/docs (`f000217`) · Date: capture 2025-01-15 (Wayback; underlying doc undated) · Locator: "Vectors and matrices" chapter, "Matrix resizing"
  - Quote: "Indeed, dynamic resizing will produce heap-allocated results because the size of the output matrix cannot be deduced at compile-time."
  - Paraphrase: States fixed (compile-time-known) resizing should be preferred over dynamic resizing whenever possible, because dynamic resizing always produces heap-allocated results

## Question `foreign-keys-vs-app-integrity`

On eventually consistent storage, should referential integrity be enforced by database foreign keys or in application code?

Positions:
- `foreign-keys-vs-app-integrity--app-enforced-integrity`: Drop foreign keys; enforce integrity in application code
- `foreign-keys-vs-app-integrity--alt1`: Keep database foreign keys

Claims:
- `b-sT07-f004166-c2` · Voice: Nick Kuntz · Source: https://blog.cloudflare.com/serverless-matrix-homeserver-workers (`f004166`) · Date: 2026-01-27 · Locator: § D1 ("We learned one hard lesson")
  - Quote: "We removed all foreign keys and enforce referential integrity in application code."
  - Paraphrase: D1's eventual consistency broke FK checks across sequential writes, so all FKs were removed

## Question `form-values-list-vs-scalar-deserialization`

When a UI framework's form-submission API hands back untyped, string-keyed values (e.g. a `HashMap<String, Vec<String>>`) for deserialization into a caller-defined struct via serde, should the ambiguity between a single value and a multi-value field (e.g. a multi-select) be resolved by an explicit schema/cardinality marker in the data, or by a permissive/heuristic deserializer that infers list-vs-scalar from the observed value count per field?

Positions:
- `form-values-list-vs-scalar-deserialization--p1`: Disambiguate scalar vs. list by observed value count (no schema change)
- `form-values-list-vs-scalar-deserialization--alt1`: Add an explicit list/scalar marker to the data

Claims:
- `a-01-f000543-c1` · Voice: bunnyBites · Source: https://github.com/DioxusLabs/dioxus/pull/1610 (`f000543`) · Date: 2023-11-04 · Locator: PR comment responding to review
  - Quote: "I think for multi-valued elements like select, we would expect the same result as the 'values' (vector/array of values), which we can get to know based on the length of values."
  - Paraphrase: For multi-valued elements like a `<select multiple>`, the deserializer should infer list-vs-scalar for a field from how many values were observed for it, rather than adding an explicit list/scalar marker to the wire format.

## Question `frontend-hook-naming`

What naming convention should Rust reactive-frontend-framework hooks use, given no established convention exists across the ecosystem?

Positions:
- `frontend-hook-naming--p1`: Use_ prefixed noun phrase
- `frontend-hook-naming--other`: Other / none of these

Claims:
- `a-sR07-f002271-c2` · Voice: lukechu10 · Source: https://github.com/sycamore-rs/sycamore/pull/752 (`f002271`) · Date: 2024-11-03 · Locator: comment on router.rs (2024-11-03T22:54:24Z)
  - Quote: "Although there isn't really a precise convention here, I think the hook would be better named `use_search_query` instead."
  - Paraphrase: acknowledging no precise convention exists, proposes naming query/hash accessor hooks with a `use_<noun>` pattern (`use_search_query`, `use_location_hash`)

## Question `fullstack-reactive-complexity-essential`

is the complexity practitioners feel in fullstack reactive frameworks (hooks, effects, suspense, hydration mismatches) accidental complexity added by the framework, or essential complexity inherent to the fullstack problem itself?

Positions:
- `fullstack-reactive-complexity-essential--p1`: The hooks/reactivity complexity in a fullstack framework is essential, not accidental
- `fullstack-reactive-complexity-essential--alt1`: The complexity is accidental, added by the framework

Claims:
- `b-sb20-f007290-c2` · Voice: fasterthanlime · Source: https://fasterthanli.me/articles/does-dioxus-spark-joy (`f007290`) · Date: 2025-11-22 · Locator: section "Love-hate"
  - Quote: "It's that full stack stuff is complicated. It truly is. It's not that Dioxus added complexity where we didn't need any."
  - Paraphrase: the long list of Dioxus hooks and the fact that breaking hook rules produces silent misbehavior rather than a compile or runtime error feels intimidating, but that is because fullstack apps are inherently complicated, not because Dioxus added needless complexity

## Question `futures-crate-vs-alternatives`

Should a Rust library depend on the mainline `futures` crate for complex combinators (e.g. `FuturesUnordered`) despite known bugs in that unsafe-heavy code, or should it avoid `futures` altogether and assemble the needed functionality from several smaller alternative crates (futures-lite, futures-buffered, futures-util) at the cost of ergonomics and discoverability?

Positions:
- `futures-crate-vs-alternatives--p1`: Avoid futures crate use alternatives
- `futures-crate-vs-alternatives--alt1`: Keep depending on the `futures` crate

Claims:
- `b-sb17-f005159-c3` · Voice: Rüdiger Klaehn · Source: https://iroh.computer/blog/async-rust-challenges-in-iroh (`f005159`) · Date: 2024-07-31 · Locator: article body, "Complex combinators in futures are buggy" section
  - Quote: "We have therefore decided to take the drastic step to stop using the futures crate altogether and use a set of crates to replace it: futures-lite for simple futures and streams combinators, futures-buffered to replace FuturesUnordered, and futures-util from the futures repo for the rare case where we want to use something from futures that is not covered by either."
  - Paraphrase: after finding bugs in `futures`'s unsafe-heavy combinators (e.g. `FuturesUnordered`) that were impractical to fix upstream, drops the `futures` crate dependency entirely in favor of futures-lite, futures-buffered and futures-util

## Question `game-logic-in-scripting-layer`

when a Rust game engine embeds a scripting/modding language, should most game logic live in the hosted scripting language itself, or should Rust own the state with the scripting language calling into it through getter/setter shims?

Positions:
- `game-logic-in-scripting-layer--p1`: Keep the native (Rust) layer a thin, general-purpose platform and put effectively all game logic in the hosted scripting/VM language, rather than building a bridge for native code to touch mutable game state directly
- `game-logic-in-scripting-layer--alt1`: Rust owns the state; scripts call in through getter/setter shims

Claims:
- `b-sb26-f013214-c6` · Voice: parasyte · Source: https://users.rust-lang.org/t/game-dev-in-rust-some-notes-on-the-mess/104939 (`f013214`) · Date: 2024-05-05 · Locator: reply timestamped 2024-05-05T02:19:47
  - Quote: "one of the most consistent designs I've seen is putting 100% of the game logic into the hosted scripting language."
  - Paraphrase: points to long-standing precedent — browser JavaScript games, and older engines like SCUMM and Another World — for putting ~100% of game logic in the hosted language, with the unmanaged layer having "nothing to do with the game" as a general-purpose platform, and the real source of truth for state living in serialized data files (JSON, glTF, VRM) rather than in either language's live objects

## Question `gamedev-ecosystem-maturity`

is Rust's 3D/graphics game-dev crate ecosystem (wgpu, Rend3, Bevy, egui, winit) mature enough for demanding, multi-year production projects, or does its ongoing API churn and thinness make such projects impractical today?

Positions:
- `gamedev-ecosystem-maturity--p1`: After three years building a demanding 3D metaverse client, the Rust graphics crate ecosystem (WGPU, Rend3, winit, egui) is not yet "ready for prime time"
- `gamedev-ecosystem-maturity--p2`: Rust game dev is not a flop, just early — game-industry technology adoption is inherently slow regardless of a technology's merits

Claims:
- `b-sb26-f013214-c1` · Voice: John_Nagle · Source: https://users.rust-lang.org/t/game-dev-in-rust-some-notes-on-the-mess/104939 (`f013214`) · Date: 2024-01-06 (opening post), reaffirmed 2024-03-25 · Locator: opening post, and reply timestamped 2024-03-25T21:11
  - Quote: "The trouble is, the graphics crate ecosystem still isn't ready for prime time... Over half my time goes into dealing with ecosystem bugs."
  - Paraphrase: describes the graphics crates as "tightly coupled," advancing in version lockstep with frequent breaking upgrades and documentation limited to rustdoc; over half his time across three years has gone to filing and chasing ecosystem bugs rather than his actual application; by March 2024 some things had measurably improved (Rend3 dropping a net-negative occlusion-culling optimization, a new `glam` release) but core stability problems (consistent frame rate under concurrent content updates) were still unresolved
- `b-sb26-f013214-c2` · Voice: khimru · Source: https://users.rust-lang.org/t/game-dev-in-rust-some-notes-on-the-mess/104939 (`f013214`) · Date: 2024-01-07 · Locator: reply timestamped 2024-01-07T00:24:43
  - Quote: "So we are firmly in the Trough of Disillusionment stage? That's fine and kinda expected."
  - Paraphrase: frames the situation with the Gartner hype-cycle "Trough of Disillusionment" label, and draws an analogy to games staying on MS-DOS for years after Windows existed — games moved only once 3D accelerator cards forced the issue, not because Windows was inherently better — arguing Rust lacks an equivalent forcing function, so any transition will take years or decades

## Question `gating-pre-1-0-dependency-integrations`

For optional, pre-1.0 dependencies whose traits a crate implements, should the crate gate the exposure behind one coarse "unstable" feature flag, behind per-dependency (or per-dependency-version) feature flags, or simply drop the integration and re-add it only if users ask?

Positions:
- `gating-pre-1-0-dependency-integrations--p1`: Cfg gate hidden impls not unstable attribute
- `gating-pre-1-0-dependency-integrations--p2`: Per function not per block annotation
- `gating-pre-1-0-dependency-integrations--p3`: Blanket unstable flag
- `gating-pre-1-0-dependency-integrations--p4`: Need an explicit policy
- `gating-pre-1-0-dependency-integrations--p5`: Per dependency subfeature
- `gating-pre-1-0-dependency-integrations--p6`: Just remove and readd on demand

Claims:
- `b-sb09-f002615-c8` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/3055 (`f002615`) · Date: 2025-01-30 · Locator: comment @bugadani 2025-01-30T10:24:54Z
  - Quote: "My point is, we need to figure out these dependencies, and what we do with them. We can remove a specific example, but the issue doesn't go away just from that."
  - Paraphrase: pushes back that ufmt is not the only such dependency (rand-core, embassy-embedded-hal, log, etc.), so ad hoc removal doesn't resolve the underlying question of what to do with unstable optional dependencies generally.
- `b-sb09-f002615-c2` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/3055 (`f002615`) · Date: 2025-01-29 · Locator: comment @bugadani 2025-01-29T12:13:30Z
  - Quote: "We shouldn't use `#[unstable]` on inherent impl blocks, the attribute should be placed on each function."
  - Paraphrase: the `#[unstable]` attribute should sit on each function rather than on whole inherent impl blocks.
- `b-sb09-f002615-c7` · Voice: bjoernQ · Source: https://github.com/esp-rs/esp-hal/pull/3055 (`f002615`) · Date: 2025-01-30 · Locator: comment @bjoernQ 2025-01-30T10:14:28Z
  - Quote: "we spend more time talking/thinking about it than it would take to remove and re-add it"
  - Paraphrase: argues it's simpler to just remove optional integrations (as was done for embedded-hal-nb) and re-add them later if users complain, rather than design feature-flag machinery.
- `b-sb09-f002615-c3` · Voice: bjoernQ · Source: https://github.com/esp-rs/esp-hal/pull/3055 (`f002615`) · Date: 2025-01-29 · Locator: comment @bjoernQ 2025-01-29T13:13:58Z
  - Quote: "I think the intention of having this unstable is that `ufmt` is 0.2.0"
  - Paraphrase: the impl is marked unstable because the underlying `ufmt` dependency is still pre-1.0 (0.2.0).
- `b-sb09-f002615-c5` · Voice: jessebraham · Source: https://github.com/esp-rs/esp-hal/pull/3055 (`f002615`) · Date: 2025-01-29 · Locator: comment @jessebraham 2025-01-29T13:02:37Z
  - Quote: "I agree that gating this all behind the `unstable` feature is probably a bit of a ham-fisted approach, however I'm also not super excited about the prospect of potentially accumulating a bunch of different versions of various dependencies..."
  - Paraphrase: agrees the blanket-unstable approach is ham-fisted but is wary of accumulating many per-dependency-version features.
- `b-sb09-f002615-c6` · Voice: MabezDev · Source: https://github.com/esp-rs/esp-hal/pull/3055 (`f002615`) · Date: 2025-01-29 · Locator: comment @MabezDev 2025-01-29T15:44:45Z
  - Quote: "One option is to expand the `unstable` feature to have `unstable-ufmt` etc... maybe for dependencies it makes sense?"
  - Paraphrase: proposes expanding the "unstable" feature into named sub-features like `unstable-ufmt` per dependency.
- `b-sb09-f002615-c1` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/3055 (`f002615`) · Date: 2025-01-29 · Locator: comment @bugadani 2025-01-29T12:14:24Z
  - Quote: "We don't need to document a hidden impl, whether it's stable or not."
  - Paraphrase: argues private structs/functions don't need `#[instability::unstable]`; hidden impls can just be `#[cfg(feature = "unstable")]`-gated instead of documented as unstable.
- `b-sb09-f002615-c4` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/3055 (`f002615`) · Date: 2025-01-29 · Locator: comment @bugadani 2025-01-29T12:33:55Z
  - Quote: "Hiding every one of these behind \"unstable\" seems a bit off to me... but also a dependency+version feature... may be a bit too granular... I think we might want to come up with a policy regarding them."
  - Paraphrase: neither blanket-unstable nor per-dependency-version features feel right; the project needs a general policy on how to handle pre-1.0 optional trait dependencies.

## Question `generated-crates-escape-hatches`

should generated crates be fully automatic, or must they leave handwritten escape hatches for what a schema can't express (e.g. trait impls)?

Positions:
- `generated-crates-escape-hatches--p1`: Generated crates need handwritten escape hatches
- `generated-crates-escape-hatches--alt1`: Fully automatic generated crates with no handwritten code

Claims:
- `a-sa23-f011186-c4` · Voice: Adam · Source: https://youtube.com/watch?v=bjgGboWCTDw (`f011186`) · Date: 2024-11-20 · Locator: ~00:25:33
  - Quote: "support handwritten code I'd say 95% of the crate is generated"
  - Paraphrase: ~95% of his generated crate is codegen'd, but a dedicated `methods.rs` file holds handwritten trait impls and helpers (e.g. arithmetic on a generated `Angle` type) that can't be inferred from the OpenAPI schema alone, and the generator is written to never overwrite that file

## Question `generated-size-vs-runtime-performance`

should a codegen tool trade a larger generated-output size for better runtime performance?

Positions:
- `generated-size-vs-runtime-performance--p1`: Favors performance over output size for this change
- `generated-size-vs-runtime-performance--alt1`: Favor smaller generated output

Claims:
- `b-sR03-f001160-c2` · Voice: daxpedda · Source: https://github.com/wasm-bindgen/wasm-bindgen/pull/3898 (`f001160`) · Date: 2024-04-03 · Locator: wasm-bindgen/wasm-bindgen#3898, comment 2024-04-03T06:33:18Z. · L2343-L2347.
  - Quote: "Generate JS bindings for WebIDL dictionary setters instead of using `Reflect`. This increases the size of the Web API bindings but should be more performant."
  - Paraphrase: favors performance over output size for this change.

## Question `generic-over-blocking-async`

Should blocking and async variants of a peripheral driver share one generic implementation, or stay duplicated?

Positions:
- `generic-over-blocking-async--p1`: Generic over mode
- `generic-over-blocking-async--alt1`: Keep blocking and async implementations duplicated

Claims:
- `b-sb05-f001512-c5` · Voice: MabezDev · Source: https://github.com/esp-rs/esp-hal/pull/1592 (`f001512`) · Date: 2024-05-29 · Locator: comment 2024-05-29T09:59:47Z
  - Quote: "I think we should be able to have one impl that is generic over the mode."
  - Paraphrase: blocking and async constructors should share one generic implementation instead of duplicating methods

## Question `generics-vs-dyn-for-abstraction`

Should Rust code abstract with generics (static dispatch, associated types) or with `dyn Trait` and type erasure?

Positions:
- `generics-vs-dyn-for-abstraction--static-by-default`: Enums or generics; avoid `dyn` when possible
- `generics-vs-dyn-for-abstraction--p1`: Trait objects for size
- `generics-vs-dyn-for-abstraction--p2`: Use trait objects instead of generic type parameters to cut code size, accepting slower indirect calls and lost per-type inlining

Claims:
- `a-sa30-f013276-c4` · Voice: parasyte — track record not established from this source · Source: https://users.rust-lang.org/t/abstract-factory-trait-with-generic-method/122066 (`f013276`) · Date: 2024-12-06 · Locator: post 2024-12-06T04:21:54.051Z
  - Quote: "dyn Trait can also be used for dependency injection. It's pure dynamic dispatch, of course. But the benefits for its use are extremely narrow, and it comes with more downsides than the one thing it has going for it."
  - Paraphrase: ranks generics, enums, and `dyn Trait` as all valid dependency-injection mechanisms but singles out `dyn Trait` as having disproportionately narrow benefit for its cost
- `a-sa30-f013276-c3` · Voice: parasyte — track record not established from this source · Source: https://users.rust-lang.org/t/abstract-factory-trait-with-generic-method/122066 (`f013276`) · Date: 2024-12-05 · Locator: post 2024-12-05T23:20:50.930Z
  - Quote: "Type erasure often hurts more than it helps, but there must be some other motivation for it than making the code 'more abstract'."
  - Paraphrase: challenges the OP's motivation for reaching for type erasure, stating it more often costs than it buys
- `a-sB02-f000256-c10` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "Shrinking .wasm Code Size" — "Use Trait Objects Instead of Generic Type Parameters"
  - Quote: "The downside is the loss of the compiler optimization opportunities and the added cost of indirect, dynamically dispatched function calls."
  - Paraphrase: generic functions get monomorphized into one copy per type, growing code size; trait objects emit a single function using dynamic dispatch instead, at the cost of lost compiler optimization opportunities and added indirect-call overhead.
- `a-sa30-f013276-c7` · Voice: jumpnbrownweasel — track record not established from this source · Source: https://users.rust-lang.org/t/abstract-factory-trait-with-generic-method/122066 (`f013276`) · Date: 2024-12-05 · Locator: post 2024-12-05T22:41:05.581Z
  - Quote: "This abstraction doesn't seem possible with trait objects, as they're not nearly as capable as generics and you're pushing them over their limits. Abstraction in Rust is better supported with generics."
  - Paraphrase: states the OP's desired abstraction isn't achievable with trait objects because they are much less capable than generics for this purpose
- `b-bk02-f000256-c9` · Voice: rustwasm working group (Rust and WebAssembly book) [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: unknown (living doc) · Locator: § "Shrinking .wasm Code Size" → Use Trait Objects Instead of Generic Type Parameters
  - Quote: "If you use trait objects instead of type parameters... only a single version of the function is emitted in the .wasm. The downside is the loss of the compiler optimization opportunities and the added cost of indirect, dynamically dispatched function calls."
  - Paraphrase: contrasts monomorphized generics, which emit one function copy per concrete type and enable per-type optimization, against trait objects, which emit a single dynamically-dispatched copy; names the size win and the speed/inlining loss explicitly as the trade.
- `a-sa07-f003704-c1` · Voice: laggui · Source: https://github.com/tracel-ai/burn/pull/3872 (`f003704`) · Date: 2025-11-03 · Locator: PR #3872, comment 2025-11-03T20:43:16Z
  - Quote: "This would remove the need for `NodeConfig` trait entirely."
  - Paraphrase: proposes replacing the NodeConfig trait's runtime type erasure and up/down-casting with an associated config type on NodeProcessor

## Question `git-storage-database-decentralized`

For hosting large monorepos, should Git object storage move off the traditional filesystem-based backend and into a distributed database (as Google Piper/Meta Sapling do), combined with decentralizing hosting itself rather than relying on a centralized host like GitHub?

Positions:
- `git-storage-database-decentralized--p1`: Rebuild Git's storage engine on a database and decentralize hosting rather than depend on a centralized host
- `git-storage-database-decentralized--alt1`: Keep filesystem-based Git storage on a centralized host

Claims:
- `b-sb23-f011178-c1` · Voice: Quanyi Ma · Source: https://youtube.com/watch?v=qHcfiCmcIf8 (`f011178`) · Date: 2024-11-18 · Locator: ~06:14-11:22
  - Quote: "being centralized ... can access all data and can take action like ... training AI or deleting projects"
  - Paraphrase: argues centralized hosts like GitHub can unilaterally access all data or use it for AI training/deletion, so his project (Mega, built in Rust) stores Git objects in a database (mirroring how Google's Piper and Meta's Sapling scale monorepos) and layers a GTM-based P2P network on top so repositories can be cloned/pushed without a single central node

## Question `global-statics-vs-per-request-state`

Under a concurrent-instance execution model, should shared state use global statics/OnceCell, or be scoped per-request with explicit synchronization?

Positions:
- `global-statics-vs-per-request-state--p1`: Prefer per request scoped state
- `global-statics-vs-per-request-state--alt1`: Global statics or `OnceCell`

Claims:
- `b-sR10-f004809-c2` · Voice: The Spin Project (Fermyon / CNCF Spin, institution) · Source: https://spinframework.dev/blog/announcing-spin-4-0 (`f004809`) · Date: 2026-06-15 · Locator: section "Heads up on global state"
  - Quote: "Audit any static, module-level, or OnceCell state and reach for per-request state or explicit synchronization where needed."
  - Paraphrase: since one instance can now serve concurrent in-flight requests, code that used static/module-level/OnceCell "global" state must be audited and moved to per-request state or explicit synchronization

## Question `gpu-async-await-vs-dsl`

For structured concurrent GPU programming, is it better to reuse an existing general-purpose language's async/await abstraction (Rust's `Future`/async-await) than to adopt a purpose-built DSL/compiler stack (JAX, Triton, NVIDIA CUDA Tile)?

Positions:
- `gpu-async-await-vs-dsl--p1`: Reuse existing async model over new dsl
- `gpu-async-await-vs-dsl--alt1`: A purpose-built DSL or compiler stack (JAX, Triton, CUDA Tile)

Claims:
- `b-sb21-f008808-c1` · Voice: VectorWare · Source: https://vectorware.com/blog/async-await-on-gpu (`f008808`) · Date: 2026-02-18 · Locator: § "Rust's Future trait and async/await"
  - Quote: "We believe Rust's Future trait and async/await provide such an abstraction. They encode structured concurrency directly in an existing language without committing to a specific execution model."
  - Paraphrase: JAX, Triton and CUDA Tile each require a new Python-based DSL/compiler and a break from existing CPU code/libraries; Rust's Future trait already encodes structured, composable concurrency without committing to an execution model, so it can be run unchanged on the GPU and reuse the existing async ecosystem (they ported the `Embassy` embedded executor with very few changes) — while acknowledging it still carries the same function-coloring problem async/await has on the CPU

## Question `greptimedb-write-api-choice`

When writing data to GreptimeDB from Rust, should an application use the low-latency Regular write API or the high-throughput Bulk Stream Insert API, and how should parallelism and compression be tuned for each?

Positions:
- `greptimedb-write-api-choice--p1`: Pick the write API by workload shape (Regular for low-latency/small-batch, Bulk for high-throughput/delay-tolerant), and tune parallelism/compression to the actual bottleneck rather than using one default configuration
- `greptimedb-write-api-choice--alt1`: Always the Regular write API
- `greptimedb-write-api-choice--alt2`: always the Bulk Stream Insert API

Claims:
- `b-sb25-f012642-c1` · Voice: Jiachun Feng (Co-Founder, Greptime) · Source: https://greptime.com/blogs/2025-07-30-greptimedb-rust-guide-bulk-stream-insert (`f012642`) · Date: 2025-07-30 · Locator: "Summary" and "When to Use Which API" sections
  - Quote: "Bulk API is more suitable for scenarios requiring higher throughput and can tolerate some latency"
  - Paraphrase: presents a benchmark (2M rows, 22-field log schema) showing Bulk API at 155,099 rows/s versus Regular API at 104,237 rows/s (about 49% faster) under compression, then gives a decision table by use case (real-time alerting/IoT/dashboards → Regular; ETL/log collection/historical import → Bulk) and separate tuning guidance: match `parallelism` to whether the workload is network- or CPU-bound, and choose Zstd over LZ4 only when bandwidth, not CPU, is the constraint
