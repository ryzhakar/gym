## ecs-relationship-type-level-exclusivity
### ecs-relationship-type-level-exclusivity--p1
- for | The edge type should have a different interface based on its exclusivity — one-to-many derefs to `Entity`, many-to-one to `[Entity]` — because it makes incorrect usage fail to compile, improves error messages, and keeps the model close to what `Parent`/`Children` already are for users, for reflection, and for scene-serialization formats (BSN/`ron`). | values: correctness, approachability | sources: f002142@PR #15635, comment 2024-10-20T08:31:44Z
- against | Type-level exclusivity is not even correct in practice, since an entity can still hold both a `OneToOne<R>` and a `OneToMany<R>` edge of the same relationship, and it forces every query site to know and restate the edge shape; "being at a type level is not a benefit it is the option," and consistency of one query API matters more than having that option. | values: correctness, simplicity | sources: f002142@PR #15635, comment 2024-10-20T10:57:04Z

### ecs-relationship-type-level-exclusivity--p2
- for | "Consistency is more important here than options... Being at a type level is not a benefit it is the option": type-level exclusivity isn't even correct (an entity can hold both `OneToOne<R>` and `OneToMany<R>`) and forces every query site to restate the edge shape, so one consistent query API regardless of exclusivity is preferred. | values: simplicity, correctness | sources: f002142@PR #15635, comment 2024-10-20T10:57:04Z

## encode-invariant-in-representation
### encode-invariant-in-representation--encode-in-types
- for | "In general, we store the log2(page_size) rather than the page size directly. This helps cut down on invalid states and properties we need to assert." | values: correctness, simplicity | sources: f001582@PR description, 2024-06-10T20:15:41Z

### encode-invariant-in-representation--p1
- for | zebra-chain's data structures are deliberately defined so invalid states are unrepresentable — the `Transaction` enum has one variant per transaction version, so it is impossible to construct a transaction with spend/output descriptions but no binding signature, or a version-2 (Sprout) transaction carrying Sapling proofs. | values: correctness | sources: f000267@Design Overview § zebra-chain

## enum-vs-dyn-trait-closed-set
### enum-vs-dyn-trait-closed-set--open-trait-for-extensibility
- for | "The relay's access control has been redesigned. The AccessConfig enum is gone, replaced by an AccessControl trait with on_connect and on_disconnect hooks," so embedders can implement arbitrary policy rather than choosing among enum variants. | values: value-candidate: extensibility | sources: f004741@section "🔐 Pluggable relay access control"

### enum-vs-dyn-trait-closed-set--static-by-default
- for | After offline discussion, agreed to redo the Graph representation as node enums rather than trait objects, dropping heap allocation and vtable indirection while staying entirely safe: "We will redo as a graph of node enums." | values: performance, simplicity | sources: f003704@PR #3872, comment 2025-11-07T15:47:01Z

### enum-vs-dyn-trait-closed-set--unsafe-unions-for-memory
- no argument in sources

## ergonomics-vs-explicitness
### ergonomics-vs-explicitness--p1
- for | "Explicitness is the fourth core value of Rust. Ironically, I don't see that 'Explicitness' is ever explicitly stated as a goal of Rust" — explicitness functions as one of Rust's de facto core values even though it was never written down as one. | values: value-candidate: explicitness | sources: f012469@post by @nayru25 dated 2016-04-03T00:20:55Z; re-cited by @cg-cnu dated 2018-04-25T09:01:38Z

### ergonomics-vs-explicitness--p2
- for | "Anywhere your code is hard to write, we'll be there, writing controversial RFCs then scaling them back! Resistance is futile!" — the 2017 ergonomics-initiative RFCs, pushing implicit sugar into places code was hard to write, are acknowledged by their own author as knowingly controversial and likely to need scaling back. | values: value-candidate: explicitness | sources: f012469@post by @MaloJaffre dated 2017-08-31T19:26:05Z, sourced "Aturon about ergonomics initiative RFCs"

## esp32-psram-display-dma-strategy
### esp32-psram-display-dma-strategy--p1
- against | Cyclic DMA descriptors — feeding the display from an infinite, cyclic buffer that never restarts — "failed after the very first frame" in practice; switching to acyclic descriptors that restart the transmission after each frame works instead. | values: correctness, stability | sources: f002499@comment 2026-02-16T23:59:16Z

### esp32-psram-display-dma-strategy--p2
- for | Two PSRAM framebuffers feeding two 1/16 SRAM bounce buffers via looping DMA, with descriptors locating the emitted slice through a `DMA_OUT_CHx` interrupt and canceling late refills, achieved "double-buffered glitch-free output without relying on XiP from PSRAM" at 31.1 FPS; a CPU-copy alternative was rejected as "glacial." | values: performance, correctness | sources: f002499@comment 2026-09-06T10:36:52Z

### esp32-psram-display-dma-strategy--p3
- for | Cyclic descriptors failed after the first frame in practice; "using acyclic descriptors and restarting the transmission after each frame seems to be fine, although not as nice" as a true infinite loop, with an offer to upstream a generic version of the fix. | values: correctness, stability | sources: f002499@comment 2026-02-16T23:59:16Z

### esp32-psram-display-dma-strategy--p4
- for | After getting a bounce-buffer renderer working, flash contention and PSRAM bandwidth slowed the application down, so the practical choice was to not switch device and instead keep a smaller, lower-resolution I8080 display: "didn't switch device and still use an I8080 display at lower size and resolution." | values: performance | sources: f002499@comment 2026-09-06T19:24:30Z

## expose-fixed-array-vs-wrapper-type
### expose-fixed-array-vs-wrapper-type--p1
- for | "I think we should wrap `[u8; 6]` into a `Mac` type where we can derive some stuff, implement `Display`" — wrapping the fixed-size array in a dedicated semantic type keeps the door open for a same-shaped but larger variant (an 8-byte IEEE MAC), which the raw array's current shape could never return. | values: stability, correctness | sources: f004265@comment 2026-02-18T14:11:20Z
- against | The same author reverses a day later: "Return a slice, not [u8; 6]" — pushing back on returning the fixed-size array at all (wrapped or not), preferring a slice-typed return to keep the door open for a larger variant. | values: stability, simplicity | sources: f004265@comment 2026-02-19T14:04:25Z

### expose-fixed-array-vs-wrapper-type--p2
- for | "Return a slice, not [u8; 6]" — the same author reverses a day later, pushing back on returning the fixed-size array at all and preferring a slice-typed return as the way to keep the door open for a larger variant. | values: stability, simplicity | sources: f004265@comment 2026-02-19T14:04:25Z

## extend-foreign-trait-type
### extend-foreign-trait-type--p1
- against | "It is something the user should neither know, nor care about" — the crate effectively already has "its own" version of the foreign type in practice (currently just a lazy type alias), so making it a real, independently extensible type of its own is fine even though it's a breaking change, rather than bolting on another parallel type. | values: simplicity | sources: f002027@PR #479, comment 2024-09-23T16:21:54Z

### extend-foreign-trait-type--p2
- for | The crate effectively already has "its own `Operation`... if you squint a little" (currently just a type-alias out of laziness); users should not need to know or care whether they're going through `embedded_hal`'s `Operation` or the crate's own, so making it a real, independently extensible type is fine even as a breaking change: "it is something the user should neither know, nor care about." | values: simplicity | sources: f002027@PR #479, comment 2024-09-23T16:21:54Z

## externref-in-rust
### externref-in-rust--keep-out-of-language-core
- against | JavaScript interop "is not a complex or niche topic and this is a major quality of life improvement to that story," and Rust has tackled harder, more niche problems before — countering the view that WebAssembly's design oddities are too niche to justify changing the language core. | values: approachability | sources: f013113@RFC #3987, comment 2026-07-30T15:48:27Z

### externref-in-rust--must-fit-abstract-machine
- for | "This RFC is proposing to introduce a fundamentally new kind of thing to Rust only to then make that thing a complete nightmare to use for anything" — the RFC's semantics can't be expressed in the Abstract Machine that MIR-transform and MIR-to-LLVM-IR correctness proofs rely on, an unprecedented kind of break worse than prior type-system-assumption-breaking RFCs, and without integration into `Result`, async, `==`, or newtypes the feature will feel bolted on. | values: correctness | sources: f013113@RFC #3987, comments 2026-07-29T12:21:27Z / 12:34:52Z
- against | JavaScript interop is a major quality-of-life story worth solving at the language level, and Rust has tackled harder, more niche problems before, while conceding the proposal must be justified for Rust on its own merits. | values: approachability | sources: f013113@RFC #3987, comment 2026-07-30T15:48:27Z

### externref-in-rust--new-restricted-lang-type
- for | Proposes `core::arch::wasm32::externref`, "an opaque, unforgeable reference to a WebAssembly host value," legal only as a bare top-level type of function parameters/returns/locals, lowering to Wasm's `externref` reference type, so host references (e.g. JS values) can marshal directly across foreign calls for interoperability and performance. | values: approachability, performance | sources: f013113@RFC #3987, opening post, 2026-07-29T00:09:07Z
- for | Responding directly to an objection that the idea is too niche, argues "JavaScript interop is not a complex or niche topic and this is a major quality of life improvement to that story," and that Rust has tackled harder, more niche problems before, while conceding the proposal must be justified for Rust on its own merits rather than by Clang precedent. | values: approachability | sources: f013113@RFC #3987, comment 2026-07-30T15:48:27Z
- against | The RFC's semantics can't be expressed in the Abstract Machine that MIR-transform and MIR-to-LLVM-IR correctness proofs rely on, an unprecedented kind of break, and without integration into `Result`, async, `==`, or newtypes the feature will feel "bolted on." | values: correctness | sources: f013113@RFC #3987, comments 2026-07-29T12:21:27Z / 12:34:52Z
- against | "A non-zero cost wrapper could work better": `externref` could act as a table index everywhere in Rust-only code, with the real WebAssembly `externref` crossing only at FFI boundaries, and an optimization pass eliding the table insert/extract round-trip whenever a value is merely passed straight through — rather than adding a new first-class restricted language type. | values: performance, simplicity | sources: f013113@RFC #3987, comment 2026-07-29T13:09:09Z

### externref-in-rust--table-index-in-rust-code
- for | "A non-zero cost wrapper could work better": `externref` acting as a table index everywhere in Rust-only code, with the actual WASM `externref` only crossing at FFI boundaries, and an optimization pass eliding the table insert/extract round-trip when a value is merely passed through. | values: performance, simplicity | sources: f013113@RFC #3987, comment 2026-07-29T13:09:09Z

## extract-single-use-function
### extract-single-use-function--extract-for-communication
- for | "Functions are not just a tool for reuse, they're a tool for communicating blocks of code like this" — pulls span-visibility logic into its own method even though it has one caller, because a well-named function with a defined input/output lets the reader trust what it does without re-deriving it. | values: approachability | sources: f001392@PR #1089, comment 2024-05-11T11:12:04Z
- for | The same dense/non-broadcast check is duplicated verbatim at two call sites gating `storage_mut()`, so drift between them would silently produce a bad write instead of a compile error; it should be a single method on `Layout` that documents the actual contract: "reads better as a single method on `Layout` carrying the actual contract." | values: correctness | sources: f005085@PR review comment, 2026-09-08T21:11:40Z

### extract-single-use-function--keep-inline
- for | "I don't think moving this into its own method is very useful. Its very specific to the render_span method" — the logic is too specific to one caller, and extracting and naming it (`visible`) risks being misleading about what it actually guarantees. | values: approachability | sources: f001392@PR #1089, comment 2024-05-11T09:24:22Z
- against | "Functions are not just a tool for reuse, they're a tool for communicating blocks of code like this" — a well-named function with a defined input/output lets the reader trust what it does without re-deriving it, even for a single caller. | values: approachability | sources: f001392@PR #1089, comment 2024-05-11T11:12:04Z

## fast-path-complexity
### fast-path-complexity--p1
- for | "It's important to look at the absolute magnitude of a perf gain, and not just the relative amount" — the fast path for left-aligned lines should be removed because, while the relative regression on a Raspberry Pi looks large, the absolute per-frame cost (~30ns on an M2 Mac) is not worth the added code complexity. | values: performance, simplicity | sources: f001392@PR #1089, comment 2024-05-11T01:36:36Z

### fast-path-complexity--p2
- for | "Relatively small improvements will impact a lot of code depending on it" — `Line` is one of the most-used core constructs and `Alignment::Left` is the common default, so a "relatively small" per-call regression compounds across hundreds of rendered cells per frame on low-power devices (own benchmarks on Raspberry Pi 1/2/4 showed 12-38% regressions without the fast path). | values: performance | sources: f001392@PR #1089, comment 2024-05-11T09:13:41Z
- against | The absolute per-frame cost of the fast path (~30ns on an M2 Mac) is not worth the added code complexity, even though the relative regression on constrained hardware looks large: "It's important to look at the absolute magnitude of a perf gain, and not just the relative amount." | values: performance, simplicity | sources: f001392@PR #1089, comment 2024-05-11T01:36:36Z

## feature-flags-vs-separate-crates
### feature-flags-vs-separate-crates--p1
- for | "Zebra has a modular, library-first design, with the intent that each component can be independently reused outside of the zebrad full node" — in contrast to zcashd's monolithic architecture, Zebra is factored into independently reusable library crates (zebra-chain, zebra-network, zebra-state), and the contributing guide names this as a scope boundary against a monolithic, feature-flagged binary. | values: simplicity | sources: f000267@Design Overview § Architecture; Contributing § Pull Requests

### feature-flags-vs-separate-crates--split-into-crates
- for | Splits Postgres access into per-domain sub-crates (`accounts`, `payments`) behind an `interfaces` crate, since "the sub-crates only care about primitive types... types used by the repository interface can change... without impacting the sub-crate API," keeping sub-crate public APIs stable while letting the Postgres stack be shared with another engineer decoupled from the host Axum app. | values: stability, simplicity | sources: f008651@"Another 'abstraction' to the repository layer" section
- for | "One crate became a workspace: tk-encode is the required runtime, and tk-serialize, tk-convert and tk-train are linked only when an application needs them," so `tk-encode` is the only required runtime piece. | values: performance | sources: f005120@table row "workspace split" / "Progress Towards V1"
- for | "We're keeping most new integrations out of the main crates to reduce the time needed to release a new feature." | values: iteration-speed | sources: f002151@leptos-rs/leptos#3063, comment 2024-10-06T02:05:17Z
- for | `DhtAddressLookup`, `MdnsAddressLookup` and `AccessLimit` were moved out of the `iroh` crate into their own crates/repos "to have a different versioning and release schedule for these components... also helpful to reduce the number of optional features in iroh." | values: iteration-speed, simplicity | sources: f004685@§ "Sometimes things have to move out"
- for | After contributing modularity work to Servo and getting "do we have to do this?" rather than buy-in, concluded a separate project was needed; Blitz is built around a small core (BlitzDom: DOM tree, layout, styling) with rendering, HTML parsing, networking, and windowing behind traits as swappable/reusable pieces. | values: simplicity | sources: f011435@~10:14-11:16

## feature-misuse-responsibility
### feature-misuse-responsibility--p1
- for | Prefers the feature live in `js-sys` rather than `getrandom` directly, since "such incorrect behavior does not get punished, while users would be more careful with js-sys" — a crate wrongly adding `js-sys` unconditionally is a more visible mistake than wrongly enabling a `getrandom` feature, which has no effect on non-WASM targets and so goes unpunished. | values: correctness | sources: f003558@comment 2025-09-19T16:28:13Z
- against | "This seems to me like a solution in search of a problem" — crates cannot be engineered into behaving correctly by restructuring an API; misbehaving crates should have issues or PRs filed against them directly, and moving the feature elsewhere just relocates the same possible mistake. | values: simplicity | sources: f003558@comment 2025-09-21T22:11:14Z; 2025-09-21T22:31:20Z

### feature-misuse-responsibility--p2
- for | "This seems to me like a solution in search of a problem" — rejects the "protect against misuse" framing outright, arguing crates cannot be forced to behave properly by restructuring the API, that misbehaving crates should have issues/PRs filed against them directly, and that shifting the feature to `js-sys` only relocates the same possible mistake. | values: simplicity | sources: f003558@comment 2025-09-21T22:11:14Z; 2025-09-21T22:31:20Z

## ffi-copy-vs-share
### ffi-copy-vs-share--convert-or-copy
- for | "Copying immutable data is generally safer and easier than trying to share it" — creating an FFI struct that copies out of the Rust result object, rather than sharing a pointer into it, costs a small performance penalty but guarantees memory management on one side of a binding can't affect the other side, which is judged worth it "more often than not." | values: correctness, performance | sources: f007678@section "Rust for Android," paragraph beginning "On the Rust side, you'll need to encapsulate"

### ffi-copy-vs-share--p2
- for | "We want to optimize for the following properties: Minimizing copying... Minimizing serializing and deserializing" — a good JS↔wasm interface keeps large, long-lived data as Rust types living in wasm linear memory, exposed to JS only as opaque handles, with JS calling functions that do the heavy work and return small, copyable results; a delta/diff-based alternative is named as viable but not adopted, citing implementation difficulty. | values: performance | sources: f000256@§ "Interfacing Rust and JavaScript"

### ffi-copy-vs-share--p3
- for | "Generating (and allocating) a String in Rust and then having wasm-bindgen convert it to a valid JavaScript string makes unnecessary copies of the universe's cells" — the tutorial's initial `render()` returning a Rust-formatted `String` is a source of unnecessary copies, fixed by returning a raw pointer so JS reads the cell buffer directly out of wasm memory via a typed-array overlay. | values: performance | sources: f000256@§ "Rendering to Canvas Directly from Memory"

### ffi-copy-vs-share--share-or-borrow
- no argument in sources

## ffi-ui-state-snapshots-vs-diffs
### ffi-ui-state-snapshots-vs-diffs--p1
- for | "Another viable design alternative would be for Rust to return a list of every cell that changed states after each tick... The trade off is that this delta-based design is slightly more difficult to implement" — the tutorial exposes the whole state as a pointer into linear memory each tick instead, naming the delta approach as viable but harder to implement. | values: simplicity | sources: f000256@§ "Interfacing Rust and JavaScript in our Game of Life"

### ffi-ui-state-snapshots-vs-diffs--p2
- for | After iterating through three worse designs (manual return-value wiring, one-function-per-field event handlers, an all-optional model needing manual `Some`-checking), settled on a derive proc macro generating a diff enum, so "if a state field is added or removed on the Rust side, this Swift function will fail compilers' enum exhaustiveness checks until it is added." | values: correctness | sources: f008389@"How procedural macros made it better" section

## final-trait-methods
### final-trait-methods--p1
- for | "I think something like #[non_overridable] could be a useful addition to the language" — proposes a `#[non_overridable]` attribute for trait extension methods whose override could cause correctness bugs, potentially excluding such methods from vtables to shrink them. | values: correctness | sources: f009316@OP, 2026-01-07T21:26:16.248Z
- for | Points to an already-drafted RFC ("Trait method impl restrictions," using the reserved `final` keyword) to "support restricting implementation of individual methods within traits," letting any trait forbid overriding specific methods or associated functions. | values: correctness | sources: f009316@linked RFC (joshtriplett/rfcs "final"), cited 2026-01-07T21:42:35.707Z

### final-trait-methods--p2
- no argument in sources

### final-trait-methods--p3
- no argument in sources

## gamedev-ecosystem-maturity
### gamedev-ecosystem-maturity--p1
- for | "The trouble is, the graphics crate ecosystem still isn't ready for prime time... Over half my time goes into dealing with ecosystem bugs" — describes the graphics crates as tightly coupled, advancing in version lockstep with frequent breaking upgrades and rustdoc-only documentation; by March 2024 some things had measurably improved but core stability problems remained unresolved. | values: stability | sources: f013214@opening post, and reply timestamped 2024-03-25T21:11
- against | "So we are firmly in the Trough of Disillusionment stage? That's fine and kinda expected" — draws an analogy to games staying on MS-DOS for years after Windows existed (moving only once 3D accelerator cards forced it), arguing Rust gamedev lacks an equivalent forcing function yet, so any transition will simply take years or decades. | values: value-candidate: adoption-timeline | sources: f013214@reply timestamped 2024-01-07T00:24:43

### gamedev-ecosystem-maturity--p2
- for | "So we are firmly in the Trough of Disillusionment stage? That's fine and kinda expected" — frames the situation with the Gartner hype-cycle label, drawing an analogy to games staying on MS-DOS for years after Windows existed, arguing Rust lacks an equivalent forcing function yet, so any transition will take years or decades. | values: value-candidate: adoption-timeline | sources: f013214@reply timestamped 2024-01-07T00:24:43

## gating-pre-1-0-dependency-integrations
### gating-pre-1-0-dependency-integrations--p1
- for | "We don't need to document a hidden impl, whether it's stable or not" — private structs/functions don't need to be documented as `#[unstable]`; hidden impls can simply be `#[cfg(feature = "unstable")]`-gated instead. | values: simplicity | sources: f002615@comment @bugadani 2025-01-29T12:14:24Z

### gating-pre-1-0-dependency-integrations--p2
- for | "We shouldn't use `#[unstable]` on inherent impl blocks, the attribute should be placed on each function" — the `#[unstable]` attribute belongs on each individual function, not on whole inherent impl blocks. | values: simplicity | sources: f002615@comment @bugadani 2025-01-29T12:13:30Z

### gating-pre-1-0-dependency-integrations--p3
- for | "I think the intention of having this unstable is that `ufmt` is 0.2.0" — gating behind one coarse "unstable" flag is justified because the underlying dependency (`ufmt`) is itself still pre-1.0. | values: stability | sources: f002615@comment @bjoernQ 2025-01-29T13:13:58Z

### gating-pre-1-0-dependency-integrations--p4
- for | "Hiding every one of these behind 'unstable' seems a bit off to me... but also a dependency+version feature... may be a bit too granular... I think we might want to come up with a policy regarding them" — neither blanket-unstable nor per-dependency-version features feel right; the project needs a general policy for pre-1.0 optional trait dependencies. | values: simplicity | sources: f002615@comment @bugadani 2025-01-29T12:33:55Z
- for | "My point is, we need to figure out these dependencies, and what we do with them. We can remove a specific example, but the issue doesn't go away just from that" — pushes back that `ufmt` is not the only such dependency (rand-core, embassy-embedded-hal, log), so ad hoc removal doesn't resolve the underlying question. | values: correctness | sources: f002615@comment @bugadani 2025-01-30T10:24:54Z
- for | "I agree that gating this all behind the `unstable` feature is probably a bit of a ham-fisted approach, however I'm also not super excited about the prospect of potentially accumulating a bunch of different versions of various dependencies" — agrees the blanket approach is ham-fisted but is wary of accumulating many per-dependency-version features. | values: simplicity | sources: f002615@comment @jessebraham 2025-01-29T13:02:37Z

### gating-pre-1-0-dependency-integrations--p5
- for | "One option is to expand the `unstable` feature to have `unstable-ufmt` etc... maybe for dependencies it makes sense?" — proposes expanding the single "unstable" feature into named per-dependency sub-features. | values: stability | sources: f002615@comment @MabezDev 2025-01-29T15:44:45Z

### gating-pre-1-0-dependency-integrations--p6
- for | "We spend more time talking/thinking about it than it would take to remove and re-add it" — it's simpler to remove an optional integration outright, as was already done for embedded-hal-nb, and re-add it later only if users complain. | values: iteration-speed, simplicity | sources: f002615@comment @bjoernQ 2025-01-30T10:14:28Z
- against | `ufmt` is not the only pre-1.0 dependency raising the same issue (rand-core, embassy-embedded-hal, log); ad hoc removal doesn't resolve the underlying question of what to do with unstable optional dependencies generally: "the issue doesn't go away just from that." | values: correctness | sources: f002615@comment @bugadani 2025-01-30T10:24:54Z

## generics-vs-dyn-for-abstraction
### generics-vs-dyn-for-abstraction--p2
- for | Generic functions get monomorphized into one copy per concrete type, growing `.wasm` code size; using trait objects instead of type parameters emits a single dynamically-dispatched copy — "the downside is the loss of the compiler optimization opportunities and the added cost of indirect, dynamically dispatched function calls." | values: performance | sources: f000256@§ "Shrinking .wasm Code Size" — "Use Trait Objects Instead of Generic Type Parameters"

### generics-vs-dyn-for-abstraction--static-by-default
- for | "This abstraction doesn't seem possible with trait objects, as they're not nearly as capable as generics and you're pushing them over their limits. Abstraction in Rust is better supported with generics." | values: value-candidate: capability | sources: f013276@post 2024-12-05T22:41:05.581Z
- for | "dyn Trait can also be used for dependency injection... But the benefits for its use are extremely narrow, and it comes with more downsides than the one thing it has going for it" — ranks generics, enums, and `dyn Trait` as valid dependency-injection mechanisms but singles out `dyn Trait` as having disproportionately narrow benefit for its cost. | values: simplicity, performance | sources: f013276@post 2024-12-06T04:21:54.051Z
- for | Proposes replacing the `NodeConfig` trait's runtime type erasure and up/down-casting with an associated config type on `NodeProcessor`: "this would remove the need for `NodeConfig` trait entirely." | values: simplicity | sources: f003704@PR #3872, comment 2025-11-03T20:43:16Z
- for | "Type erasure often hurts more than it helps, but there must be some other motivation for it than making the code 'more abstract'" — challenges the motivation for reaching for type erasure, stating it more often costs than it buys. | values: simplicity | sources: f013276@post 2024-12-05T23:20:50.930Z

## grouped-vs-field-optionality
### grouped-vs-field-optionality--p1
- for | "Semantically 99% of the time when I even want several query parameters stored in the same value I want to know if all of them have been specified though, not a mess of several `Option` values" — when several query params only make sense together, wants to know if all were specified as a group rather than checking several individual `Option` fields. | values: simplicity | sources: f002538@comment 2025-01-14T14:21:43Z
- against | "I would recommend to wrap all your query fields with Option instead, since that best reflects reality of how query parameters work." | values: correctness | sources: f002538@comment 2025-01-14T14:17:35Z
- against | "I have never seen a set of query parameters that are optional _as a group_, rather than individually." | values: correctness | sources: f002538@comment 2025-01-14T18:44:03Z

### grouped-vs-field-optionality--p2
- for | "I would recommend to wrap all your query fields with Option instead, since that best reflects reality of how query parameters work." | values: correctness | sources: f002538@comment 2025-01-14T14:17:35Z
- for | "I have never seen a set of query parameters that are optional _as a group_, rather than individually." | values: correctness | sources: f002538@comment 2025-01-14T18:44:03Z

## hal-driver-typestate
### hal-driver-typestate--encode-in-types
- for | "A feature should not determine a driver whether a driver is async or blocking, it should be determined by how its initialized" — proposes a typestate `Uart<T: Instance, M>` where `M` is `Blocking` or `Async`, with per-mode constructors, moving interrupt handlers from link-time binding to a runtime-installed `__INTERRUPTS` array. | values: correctness | sources: f000715@issue #1063, comment 2024-01-05T16:28:34Z
- against | Type-state could resolve the same kind of ambiguity but adds ongoing complexity that "gets annoying later." | values: simplicity | sources: f001512@comment 2024-05-24T15:15:23Z

### hal-driver-typestate--runtime-or-raw
- for | "Basically, had a similar thing in mind (minus the type-state)" — had a similar runtime-binding idea independently, arrived at without introducing a typestate at all. | values: simplicity | sources: f000715@issue #1063, comment 2024-01-05T16:38:20Z

### hal-driver-typestate--typestate-costly
- for | "Maybe adding type-state but that gets annoying later" — concedes type-state could resolve an ambiguity (default TX/RX pins) but flags that it adds ongoing complexity. | values: simplicity | sources: f001512@comment 2024-05-24T15:15:23Z

## handle-identity-traits-vs-store-methods
### handle-identity-traits-vs-store-methods--p1
- for | "Equality (and hashing) *should* hold when a `Func` refers to the same function within a store, regardless how it's reached... we need to provide separate methods on the `Func` for this" — pointer-identity equality on the bare handle is surprising because it doesn't hold across import/export boundaries even for the same underlying function, so correct identity needs a store borrow and must be separate methods rather than literal `Eq`/`Hash` impls. | values: correctness | sources: f005000@comment @cfallin 2026-08-13T17:28:44Z

### handle-identity-traits-vs-store-methods--p2
- no argument in sources

## hard-dependency-vs-pluggable-interface
### hard-dependency-vs-pluggable-interface--hard-dependency-behind-feature
- for | "Imo, the hard dependency is fine as we can add it behind a feature in esp-wifi" — pushes back on avoiding the dependency outright, proposing instead that the allocator-callback functions move into `esp-wifi` behind an `esp-alloc` feature. | values: simplicity | sources: f001989@PR #2099, comment 2024-09-06T11:10:19Z
- against | "I wanted to avoid a hard dependency in `esp-wifi` to not require a new release whenever `esp-alloc` gets a release" — wants to avoid a hard dependency that forces a new release whenever an unrelated crate releases. | values: iteration-speed | sources: f001989@PR #2099, comment 2024-09-06T09:38:15Z

### hard-dependency-vs-pluggable-interface--pluggable-interface
- for | Iroh 0.98 makes the TLS crypto provider swappable via feature flags (`ring` default, `aws-lc-rs` alternative, or a fully custom provider), because "it's a problem if you're on a platform where ring doesn't build, if your org mandates a FIPS-certified backend like aws-lc-rs." | values: stability | sources: f004586@§ "Pluggable Crypto Backends"
- for | "I wanted to avoid a hard dependency in `esp-wifi` to not require a new release whenever `esp-alloc` gets a release" — the design choice was driven by wanting to avoid forcing a release of `esp-wifi` on every `esp-alloc` release. | values: iteration-speed | sources: f001989@PR #2099, comment 2024-09-06T09:38:15Z
- against | "Imo, the hard dependency is fine as we can add it behind a feature in esp-wifi" — pushes back on avoiding the dependency outright, proposing instead that the allocator-callback functions move into `esp-wifi` behind a feature. | values: simplicity | sources: f001989@PR #2099, comment 2024-09-06T11:10:19Z

## hook-api-pointer-vs-address
### hook-api-pointer-vs-address--p1
- against | "I'm not entirely sure what information you need other than the pointer's address" — responds to the pointer-preservation objection by questioning what more information a hook would actually need beyond the address. | values: simplicity | sources: f004512@comment 2026-04-01T20:06:56Z

### hook-api-pointer-vs-address--p2
- for | "I'm not entirely sure what information you need other than the pointer's address" — responds to a pointer-type objection by saying they aren't sure what more information the hook would need beyond the address. | values: simplicity | sources: f004512@comment 2026-04-01T20:06:56Z

## hot-patching-for-iteration
### hot-patching-for-iteration--faster-codegen-backend
- no argument in sources

### hot-patching-for-iteration--hot-patch
- for | Describes "zerolink"/"thinlink," "our new approach for drastically speeding up rust compile times by automatically using dynamic linking," dynamically linking workspace crates against a cached dependencies dylib alongside the Subsecond hot-patching mechanism. | values: iteration-speed | sources: f002719@comment @jkelleyrtp 2025-03-18T21:13:39Z
- for | "Subsecond" hot-patches running Rust binaries by recompiling only changed crates and linking them to hardcoded addresses at runtime, "almost completely eliminating the expensive linking step that slows down incremental development," despite "a huge number of quirks, edge cases, incomprehensible behavior" needed to make it work. | values: iteration-speed | sources: f011305@~22:12-23:12
- for | Profiling showed 100-300ms of a ~500ms build spent copying incremental artifacts to disk, pointing to an upstream rustc PR aiming to remove that cost, wanting to reach "blink and you miss it" hotpatch speed. | values: iteration-speed, performance | sources: f002719@comment @jkelleyrtp 2025-03-19T20:56:59Z

## http-body-unknown-size
### http-body-unknown-size--p1
- for | "Special casing responses with `content-length: 0` is conceptually problematic" — proposes changing `impl IntoResponse for ()` to use `Body::unknown()` instead of `Body::empty()`, so a handler that can't cheaply determine its length on a HEAD request doesn't get a spurious `content-length: 0`. | values: correctness | sources: f004637@axum issue #3741, comment 2026-05-02T11:59:01Z
- against | "Changing `()` to have an unknown body size feels too broad to me. I worry that might impact other responses using `()` that don't care about HEAD requests" — resists the change because it could silently change behavior for unrelated responses, wanting a fix that works without requiring users to opt in explicitly. | values: stability | sources: f004637@axum issue #3741, comment 2026-05-02T12:49:09Z

### http-body-unknown-size--p2
- for | "Changing `()` to have an unknown body size feels too broad to me. I worry that might impact other responses using `()` that don't care about HEAD requests" — resists making `()` default to an unknown body size because it could silently change behavior for unrelated responses, wanting a fix that works for users unfamiliar with axum's APIs rather than one requiring explicit opt-in. | values: stability, approachability | sources: f004637@axum issue #3741, comment 2026-05-02T12:49:09Z

## http-error-status-in-result
### http-error-status-in-result--errors-in-err-channel
- for | "What do you think of separating out successful and unsuccessful variants into a result type? 2xx and 3xx on one side, 4xx and 5xx on the other." | values: approachability | sources: f005454@reply, 2025-02-24T19:22:07-06:00
- for | "That could work. I think doing it that way could be more convenient for users because `?` would be usable... but at the cost of some library-side complexity" — grants the split-type approach could work and would make `?` more usable, at the cost of a parallel `SuccessStatusCode` type, while noting he personally keeps HTTP-aware code out of his core business logic anyway. | values: approachability | sources: f005454@reply, 2025-02-24T21:22:14-06:00
- against | A descriptive `Err` requires every consumer to write a translation layer back into a response, whereas a pre-baked `Ok(response)` middleware "just works" the moment it's dropped into a `ServiceBuilder`: "we will go with option 2. A drop-in middleware that just works is worth a lot in practice." | values: approachability | sources: f008906@section "Back to the rate limiter"

### http-error-status-in-result--unified-response-type
- for | "There aren't really 'successful' or 'unsuccessful' responses, just responses" — describes a design where all HTTP responses live in one enum returned directly by the handler, which keeps status-code categorization simple but means `?` doesn't work directly and needs a separate inner function plus manual matching to bridge back into the enum. | values: simplicity | sources: f005454@reply, 2025-02-24T19:01:11-06:00
- for | "We will go with option 2. A drop-in middleware that just works is worth a lot in practice" — weighed both designs explicitly: a descriptive `Err` keeps callers in control of the response shape but requires every consumer to write a translation layer, while a pre-baked `Ok(response)` "just works" the moment it's added, at the cost of a baked-in response shape (mitigated later with override hooks). | values: approachability | sources: f008906@section "Back to the rate limiter"
- for | "Return Ok(response) for anything you want the client to see, even when the response is a 401, 403, 429, or 500" — an `Err` that escapes all the way to `lambda_http::run` is treated as an invocation error, so API Gateway answers the client with a generic 502 instead of the carefully designed status code; avoiding that confusion is the entire reason for the rule. | values: correctness | sources: f008906@section "The HTTP rule of thumb"

## human-written-code-standard
### human-written-code-standard--human-written-for-critical-code
- for | "I'm pleased to declare that all of the tail-call code is human-written... (This blog post is also entirely human-written, per my personal standards)" — states, as a personal standard, that all of a project's core code is human-written, after an earlier LLM-assisted attempt "proved controversial." | values: value-candidate: authorship-trust | sources: f005821@opening paragraphs, linking to his earlier post "Experimenting with LLMs"

### human-written-code-standard--light-review-for-peripheral-code
- for | "I am not a javascript developer, so the WASM GUI is vibe coded. I just briefly checked it" — finds it acceptable to let an LLM write an entire peripheral component outside their own expertise and ship it after only a brief check rather than deep review. | values: iteration-speed | sources: f004865@"A proper GUI" section

## immediate-vs-retained-gui
### immediate-vs-retained-gui--doesnt-matter-at-small-scale
- for | "I'm not sure I love immediate mode on principle, although at this scale it extremely doesn't matter" — immediate mode avoids widget-lifetime bookkeeping and is easier to integrate into a game engine's GPU loop; retained mode can perform better by not rebuilding the whole UI every frame, but at small scale the difference is untestable. | values: simplicity, performance | sources: f008390@last line of § "egui" (just before the "Digression" heading)

### immediate-vs-retained-gui--message-passing-for-realtime
- for | "I needed a truly event-based library to handle the synchronization during playback while also being able to draw the tablature in a custom way with some kind of canvas abstraction... I am very happy with my choice so I did not try other libraries" — chose Iced specifically because the app needed an event-based library to synchronize audio playback state with UI redraws while also supporting custom canvas drawing. | values: correctness | sources: f005857@"Building a UI" and "Putting it all together" sections

## in-app-vs-infrastructure-concern
### in-app-vs-infrastructure-concern--delegate-tls-to-proxy
- for | "While Vaultwarden is based upon the Rocket web framework which has built-in support for TLS our recommendation would be that you setup a reverse proxy" — recommends a reverse proxy for TLS even though the framework has built-in TLS support, and requires HTTPS for the sensitive web-vault component. | values: correctness | sources: f005312@README § Usage, paragraph "While Vaultwarden is based upon the Rocket web framework…"

### in-app-vs-infrastructure-concern--p1
- for | "Nginx is often put in front of http services written in any language... People do it for performance reasons and to access solutions to problems that can be decoupled from the actual response logic" — nginx's actual value in front of an HTTP service is providing decoupled operational concerns (flood protection, bandwidth throttling, load balancing, TLS termination) that a new in-process server doesn't reproduce, so dropping nginx removes that role rather than replacing it. | values: simplicity, performance | sources: f005360@comment 2024-10-13T14:37:28

### in-app-vs-infrastructure-concern--rate-limit-in-app
- for | Usage plans don't exist at all on HTTP API v2, are invisible to clients even on REST ("there are no X-RateLimit-* response headers"), require API keys pre-provisioned up to a hard cap of 10,000 per account/region, and only offer DAY/WEEK/MONTH windows rather than the 15-minute window the use case needs. | values: correctness | sources: f008906@section "Why not just use API Gateway usage plans?"

## instant-min-max
### instant-min-max--p1
- for | "For SystemTime this might be reasonable to have, but the values wouldn't be portable. I think Instant would be more hazardous..." — `Instant`'s API contract doesn't guarantee a fixed reference time, so a `MIN` value wouldn't reliably denote a stable point, and `Instant` values aren't portable or stable across reboots, making its extrema more hazardous than `SystemTime`'s. | values: stability | sources: f009196@reply, 2024-08-15T23:11:10.007Z

### instant-min-max--p2
- for | "SystemTime::MIN and SystemTime::MAX seem reasonable to me... Instant::MIN and Instant::MAX seem fraught, for reasons already discussed" — proposes adding saturating arithmetic methods directly on `Instant` instead of exposing its extrema. | values: stability | sources: f009196@reply, 2024-08-16T13:04:57.183Z
- against | "For my use case it is preferable to saturate" — wants an `Instant` minimum/maximum specifically to support saturating arithmetic in a token-bucket rate limiter, where moving a timestamp below the representable minimum should saturate rather than panic. | values: correctness | sources: f009196@reply, 2024-08-16T13:23:59.223Z

### instant-min-max--p3
- for | "For my use case it is preferable to saturate" — wants an `Instant` minimum/maximum (or equivalent) to support saturating arithmetic in a token-bucket rate limiter, where moving a timestamp below the representable minimum should saturate rather than panic. | values: correctness | sources: f009196@reply, 2024-08-16T13:23:59.223Z

## io-safety-op-placement-in-main
### io-safety-op-placement-in-main--p1
- for | "This should probably be called at the start of main to ensure no other fd takes the place of a missing fd, violating I/O-safety" — argues the fd-inheritance setup should be called at the start of `main` specifically to ensure no other fd takes the place of a missing one. | values: correctness | sources: f005079@comment 2026-09-07T21:21:42Z
- against | Pushes back that it isn't worth contorting a CLI's structure to guarantee the operation happens literally at the start of `fn main`, since the tool controls all entrypoints and the current placement during startup/CLI processing is already fine. | values: simplicity | sources: f005079@comment 2026-09-08T18:52:06Z

### io-safety-op-placement-in-main--p2
- for | Pushes back that it isn't worth contorting a CLI's structure to guarantee the operation happens literally at the start of `fn main`, since Wasmtime controls all CLI entrypoints and the current placement during startup/CLI processing is already fine. | values: simplicity | sources: f005079@comment 2026-09-08T18:52:06Z

## js-tooling-in-rust
### js-tooling-in-rust--p1
- for | "Rust is undoubtedly the big star in JavaScript and TypeScript tooling and infrastructure. It addresses the most significant issue in the current tooling ecosystem: performance" — identifies performance as the most significant unsolved issue in JS/TS tooling, and states Rust's language- and compiler-level safeguards make it easier to build successful tools in the first place, not just faster ones. | values: performance | sources: f012866@pull-quote in section "JavaScript / TypeScript," attributed "Author of the TypeScript Cookbook and TypeScript in 50 Lessons"

### js-tooling-in-rust--p2
- for | "Biome aims to replace existing JavaScript tooling like Prettier and ESLint with a Rust-implemented toolchain that offers better performance and a more consistent developer experience." | values: performance, approachability | sources: f012866@pull-quote in section "Common Use Cases and Projects," attributed "Core Contributor in Biome"
