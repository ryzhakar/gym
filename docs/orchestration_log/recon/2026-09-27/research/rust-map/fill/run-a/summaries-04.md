# Blind fill A — summaries, batch 1, file 04

### doctests-must-compile--p1
Summary: Every code block embedded in a doc comment should be required to compile, because the project treats doc-comment code blocks as unit tests too, not merely as illustrative prose.
Tag: taste
Claims: a-sR07-f002347-c1

### downstream-vendor-removed-api-vs-rework--vendor-removed-trait
Summary: When an upstream library removes a public API a downstream project relied on, and reworking the integration is slow, the fallback is to replicate the removed piece directly into the downstream codebase rather than wait on or redesign around the removal.
Tag: tradeoff
Claims: b-sT07-f003809-c3

### downstream-vendor-removed-api-vs-rework--rework-downstream
Summary: When downstream migration pain follows a removal, the cost can fall on downstream's own prior misuse — building on internals in ways the maintainers call "horrifying" — rather than on the removal itself, and the response is to work through the resulting issues rather than treat the removal as the problem.
Tag: fact
Claims: b-sT07-f003809-c4

### durable-job-queue-vs-in-process--p1
Summary: Scheduled or background jobs in a Rust service should run on a durable, database-backed job queue (e.g. Postgres-backed storage), because without that durability, jobs are lost outright whenever the service has an outage.
Tag: tradeoff
Claims: b-sT09-f011688-c1

### dyn-compatibility-rules-relaxation--p1
Summary: `dyn Trait`'s object-safety constraints are too restrictive, and there's real pessimism about whether many of them can ever be lifted — even a carefully sketched hypothetical fix using higher-ranked bounds is judged years away, if it's plausible at all.
Tag: fact
Claims: a-sa30-f013276-c5, a-sa30-f013276-c1

### dynamic-ecs-component-typed-id--p1
Summary: Runtime-registered ECS components should carry a compile-time type witness — a typed wrapper around the component ID parameterized by `T` — so that dynamic component access can be done safely, in place of manual pointer work and unsafe code, while still allowing multiple components with the same underlying type to be registered and accessed separately.
Tag: tradeoff
Claims: a-02-f001231-c1

### easy-mode-rust--p1
Summary: When onboarding a team new to Rust on a security-critical project, deliberately favor owned types over borrowed references and `Arc<RwLock<T>>` over lock-free structures, to minimize borrow-checker headaches for engineers new to the language, while keeping the option to refactor toward more advanced, performant idioms later.
Tag: tradeoff
Claims: b-sb24-f011295-c1

### ecs-events-first-architecture--p1
Summary: Cross-system state changes in a growing ECS game should flow through an events/observers cascade rather than direct system-to-system mutation — modeling every change (granting XP, playing a sound, updating a tile) this way keeps each system easy to reason about and reuse in isolation, at the explicit cost that a failure partway through a cascade can't be rolled back, so every handler must defensively stop propagation to keep the game stable.
Tag: tradeoff
Claims: b-sb25-f012561-c1

### ecs-relationship-fragmenting--p1
Summary: Archetype-fragmenting relationship edges are necessary because several concrete query operations — wildcard queries, named wildcard queries, nested joins, efficient up-traversal, efficient sibling queries — simply aren't possible unless edge information is exposed at the archetype level.
Tag: tradeoff
Claims: b-sb07-f002142-c3

### ecs-relationship-fragmenting--p2
Summary: Fragmenting relationships are useless for hierarchical use cases and would just produce one archetype per entity; the non-fragmenting, relationship-type-keyed approach is what's actually needed, a conclusion independently reached by both this commenter and a Bevy ECS subject-matter expert.
Tag: tradeoff
Claims: b-sb07-f002142-c4

### ecs-relationship-source-of-truth--p1
Summary: An ECS relationship system should treat the `Relationship` component as the sole source of truth, making `RelationshipTarget` a pure reflection that can't be populated directly, so component lifecycles alone (rather than runtime scanning) protect against duplicates — trading away the ability to spawn a populated target collection directly for O(1) inserts and no quadratic-runtime duplicate scanning.
Tag: tradeoff
Claims: a-sa04-f002554-c1

### ecs-relationship-type-level-exclusivity--p1
Summary: Relationship edge components should be public types whose type encodes the exclusivity (one-to-one, one-to-many, etc.), because that makes incorrect usage fail to compile, improves error messages, and stays close to what existing types like `Parent`/`Children` already are for users and for reflection/scene formats.
Tag: tradeoff
Claims: b-sb07-f002142-c1

### ecs-relationship-type-level-exclusivity--p2
Summary: Type-level exclusivity isn't even correct in practice — an entity can still hold both a one-to-one and a one-to-many edge component of the same relationship — and it forces every query site to know and restate the edge shape; a single, consistent query API regardless of exclusivity matters more than having that option.
Tag: tradeoff
Claims: b-sb07-f002142-c2

### ecs-ui-large-vs-small-systems--p1
Summary: Large "god" UI systems with dozens of queries are simple to write but constantly conflict with the borrow checker, and a widget-per-system split helps isolate systems but forces repeated manual world/state access that itself risks borrow-checker errors — an ongoing problem, not a solved one, even after trying both shapes.
Tag: fact
Claims: b-sb25-f012561-c3

### embedded-crash-policy-kernel-vs-supervisor--p1
Summary: There's no single right answer to what crash-recovery policy (restart, backoff, giving up) a kernel should enforce, so the kernel deliberately doesn't hardcode one — it only records the fault and notifies a userspace supervisor task, leaving the actual recovery policy to the application programmer, since the correct choice depends on context.
Tag: tradeoff
Claims: a-sa17-f008217-c1

### embedded-deferred-log-formatting--p1
Summary: Deferred, binary-token logging that sends the raw value plus a format-string ID for off-device decoding measurably beats formatting human-readable strings on the device — the same log line took 1050 instructions deferred versus 1675 instructions formatted on-device — and more efficient logging lets you log more for the same time/power budget.
Tag: fact
Claims: a-sa14-f005162-c1

### embedded-framework-bundles-hal-and-executor--p1
Summary: A framework can aim to be execution-layer-only, leaving HAL/PAC to the user, and additionally aim to give tasks exclusive resource access as low-level as possible — ideally hardware-guarded — specifically to avoid needing software-level locking, unlike a bundled-HAL-and-executor alternative.
Tag: tradeoff
Claims: a-sB04-f000227-c5

### embedded-interpreter-stopgap--p1
Summary: Running a full interpreter for a missing platform capability inside your own compiled Wasm module — "a runtime on top of a runtime" — isn't optimal, but it's an acceptable stopgap that works well enough until native platform support for that capability lands.
Tag: tradeoff
Claims: a-sa14-f004985-c2

### embedded-panics-compile-time-vs-recovery--p1
Summary: For a task nothing else can restart if it crashes, compile it with a no-panic feature so that any unoptimized-away panic becomes a link failure — catching that whole class of crashes at compile time rather than relying on runtime recovery, which has no one above it to fall back on.
Tag: tradeoff
Claims: a-sa17-f008217-c2

### emscripten-vs-native-rust-wasm--p1
Summary: Compile natively from Rust straight to WebAssembly (via `wasm-bindgen`) rather than going through an Emscripten emulation layer, because Emscripten's mocked-dependency layers make compiled binaries bulky and slow.
Tag: tradeoff
Claims: a-sa14-f004985-c1

### emulate-specialization--p1
Summary: Instead of two separate constructors for read-only versus read-write capability, keep one constructor with a single field (e.g. an `Option<SyncFn>`) that only trait-bound-gated impl blocks (`Read + Write + Seek`) can set to `Some`, which fixed a real bug where the read-write variant's writes silently failed to sync.
Tag: tradeoff
Claims: b-sb20-f007213-c1

### encode-invariant-in-representation--p1
Summary: A data model's structures should be defined so invalid states are literally unrepresentable — for example, an enum with one variant per format version makes it impossible to construct a value combining fields that version can't have.
Tag: tradeoff
Claims: b-bk03-f000267-c2

### encode-invariant-in-representation--encode-in-types
Summary: Storing a derived, invariant-preserving value in the type (e.g. log2 of a page size rather than the raw page size) cuts down on the invalid states a data model can represent and the assertions needed elsewhere to guard against them.
Tag: tradeoff
Claims: b-sb05-f001582-c1

### enum-glob-import-in-match--p1
Summary: Match arms on an enum should use a local glob import (`use Enum::*;`) inside the method to drop the type-qualified path from each arm, for terser match arms.
Tag: taste
Claims: b-sR03-f000763-c3

### enum-vs-dyn-trait-closed-set--static-by-default
Summary: For a fixed, known set of kinds, enums (or an enum-dispatch-style approach) should be the default over `Box<dyn Trait>`, since dynamic dispatch is the slowest and least idiomatic option and enums drop heap allocation and vtable indirection while staying entirely safe — including deciding, after discussion, to redo a graph representation as node enums rather than trait objects.
Tag: tradeoff
Claims: a-sa17-f007884-c2, a-sa07-f003704-c3, a-sa17-f007884-c1

### enum-vs-dyn-trait-closed-set--open-trait-for-extensibility
Summary: A closed enum enumerating policy variants was replaced by an open trait with hook methods, specifically so embedders can implement arbitrary policy rather than being limited to choosing among a fixed set of enum variants.
Tag: tradeoff
Claims: b-sR10-f004741-c3

### enum-vs-dyn-trait-closed-set--unsafe-unions-for-memory
Summary: Beyond the safe enum-dispatch default, unsafe unions with hand-rolled tagged pointers (`ManuallyDrop`, pointer aliasing via `transmute_copy`) are a legitimate, deliberate escalation past safe Rust when shrinking a value's memory layout below what the default enum representation would give is worth the added unsafety.
Tag: tradeoff
Claims: a-sa17-f007884-c3

### enum-vs-flags-and-optionals--enum
Summary: Multi-outcome or growing state should be modeled as a (often non-exhaustive) enum rather than a bool or a struct of optional fields — replacing two independent fields with enum variants lets future kinds be added without another breaking change, and replacing a boolean flag with a named enum was judged more readable, safer and clearer once implemented.
Tag: tradeoff
Claims: b-sR08-f003731-c1, b-sR08-f003531-c1, b-sR08-f003531-c2

### epoll-vs-io-uring--p1
Summary: For a hand-built async I/O reactor on Linux, build the readiness-notification layer on `epoll` for now, since it hits the "standard" tradeoff of being neither too slow nor too experimental, while `io_uring` might take over that role in a few years.
Tag: tradeoff
Claims: b-sb21-f008396-c1

### ergonomic-sugar-now-or-later--p1
Summary: Ship the minimal raw mechanism now — a PR thrown together quickly — and only add a macro or trait wrapper for ergonomic sugar later, since there's little reason to add that syntactic dressing before it's shown to carry its weight.
Tag: tradeoff
Claims: a-sa11-f004512-c4

### ergonomics-vs-explicitness--p1
Summary: Explicitness functions as one of Rust's de facto core values even though, ironically, it's never explicitly stated as a goal of the language.
Tag: fact
Claims: a-sa28-f012469-c9

### ergonomics-vs-explicitness--p2
Summary: The 2017 ergonomics-initiative RFCs, which push implicit sugar into places code was hard to write, are self-consciously acknowledged by their own author as controversial and as likely needing to be scaled back over time.
Tag: fact
Claims: a-sa28-f012469-c10

### error-enum-scope-module-vs-function--p1
Summary: Error enums are better scoped per-function/operation than per-module: starting with one large per-module enum proved unwieldy, so the design moved to a nested, scoped hierarchy (e.g. a `DialError` nested inside a `ConnectError`) with names descriptive of the specific failure surface.
Tag: tradeoff
Claims: a-sa14-f005149-c2

### esp32-psram-display-dma-strategy--p1
Summary: Feed the display from an infinite, cyclic DMA buffer and never restart transfers — every framebuffer's last DMA descriptor points back to its first, and switching buffers means relinking descriptors rather than restarting anything — though this approach breaks down once PSRAM bandwidth becomes the bottleneck.
Tag: fact
Claims: b-sT05-f002499-c1

### esp32-psram-display-dma-strategy--p2
Summary: Use small SRAM bounce buffers refilled from PSRAM framebuffers via Mem2Mem DMA and looping DMA to the LCD, with descriptors to locate the emitted slice via an interrupt and canceling late refills, avoiding XIP from PSRAM entirely — achieving glitch-free output at over 31 FPS, since a CPU-copy alternative was rejected as too slow.
Tag: fact
Claims: b-sT05-f002499-c2

### esp32-psram-display-dma-strategy--p3
Summary: Cyclic descriptors failed after the first frame in this setup, but switching to acyclic descriptors that restart the transmission after each frame works, if "not as nice" as a cyclic approach would be — with the author open to upstreaming a generic version of the fix.
Tag: fact
Claims: b-sT05-f002499-c3

### esp32-psram-display-dma-strategy--p4
Summary: After getting a bounce-buffer renderer working but running into flash contention and PSRAM bandwidth slowing the application down, the practical choice was to not switch device and keep a smaller, lower-resolution I8080 display instead.
Tag: fact
Claims: b-sT05-f002499-c4

### example-data-domain-struct-vs-generic--p1
Summary: In example/demo code, a small dedicated struct (name, address, email, generated in the app constructor) is preferable to `Vec<Vec<String>>`, even at the cost of extra ceremony that could be called "gold plating," because it demonstrates how to map real-world data into table columns.
Tag: taste
Claims: b-sR03-f000763-c1

### exclusive-access-default-in-task-api--p1
Summary: A task/resource API should default to exclusive (`&mut`) access to shared state, with shared (`&-`) read-only access available as an opt-in specifically because it lets a task skip the lock API entirely, even when the resource is contended by tasks running at different priorities.
Tag: tradeoff
Claims: a-sB04-f000227-c1

### executor-agnostic-libraries--p1
Summary: A library exposing an async API should not depend on a specific executor or reactor, unless it needs to spawn tasks or define its own async I/O or timer futures — ideally only binaries own the actual scheduling and running of tasks, since executors like Tokio's mio-based reactor aren't directly compatible with async-std's or smol's async-executor-based approach, requiring compatibility shims like `async_compat` to bridge them.
Tag: tradeoff
Claims: b-bk01-f000233-c12

### explicit-vs-convenience-memory-defaults--p1
Summary: Neither a performance-first default (Rust's move/borrow-by-default) nor a convenience-first default (Swift's copy-on-write-by-default) is simply better; each suits different domains — Rust for systems, embedded, compilers and browser engines, Swift for UI, servers and some compiler/OS work — and the overlap between where each fits is expected to grow over time.
Tag: tradeoff
Claims: b-sR12-f005668-c1

### explicit-vs-implicit-indirection--p1
Summary: Requiring the programmer to write `Box<T>` for a recursive type's indirection, as Rust does, makes the underlying problem explicit and forces the programmer to deal with it directly, in contrast with a more automatic, compiler-handled approach like Swift's `indirect` keyword.
Tag: taste
Claims: b-sR12-f005668-c2

### expose-fixed-array-vs-wrapper-type--p1
Summary: A fixed-size array that might later need to hold a same-shaped but larger variant (an 8-byte IEEE MAC where the current type is `[u8; 6]`) should be wrapped in a dedicated semantic type with derived traits and a `Display` implementation, rather than exposed directly, since the current array shape could never actually hold the larger variant.
Tag: tradeoff
Claims: a-sa11-f004265-c1

### expose-fixed-array-vs-wrapper-type--p2
Summary: Rather than wrapping the array in a new type, the API should just return a slice instead of a fixed-size array, keeping the door open for a larger variant without introducing a dedicated wrapper.
Tag: tradeoff
Claims: a-sa11-f004265-c3

### expose-rustc-internals-rustdoc-json--p1
Summary: Where rustc already has the internal capability to correctly deduce information (like implied trait bounds) that an external tool cannot feasibly re-derive on its own — and where getting it wrong produces both false positives and false negatives for something load-bearing like SemVer checking — that capability should be exposed through a structured interface like rustdoc JSON using rustc's own internal APIs, rather than left for the external tool to approximate.
Tag: tradeoff
Claims: a-sa20-f009698-c4

### extend-foreign-trait-type--p1
Summary: Rather than bolting on a whole second, parallel type to extend a foreign trait's shared type, prefer narrowly scoped extension methods (or new enum variants) that leave the foreign type untouched, being wary of adding complexity to an API that's already fairly unintuitive.
Tag: tradeoff
Claims: b-sb06-f002027-c1

### extend-foreign-trait-type--p2
Summary: It's fine — even as a breaking change — to make what's effectively already a parallel type (currently just a lazy type alias) into a real, independently extensible one, since users shouldn't need to know or care whether they're going through the foreign trait's shared type or the crate's own equivalent.
Tag: tradeoff
Claims: b-sb06-f002027-c2

### externref-in-rust--new-restricted-lang-type
Summary: JavaScript interop is a major quality-of-life story, not a niche one, and is worth solving at the language level: a new restricted lang-item type — an opaque, unforgeable reference to a WebAssembly host value, legal only as a bare top-level type of function parameters/returns/locals, lowering to Wasm's `externref` — lets host references marshal directly across foreign calls for interoperability and performance, though the proposal still needs to be justified for Rust on its own merits.
Tag: tradeoff
Claims: a-sa29-f013113-c5, a-sa29-f013113-c1

### externref-in-rust--must-fit-abstract-machine
Summary: The proposal introduces a fundamentally new kind of thing to Rust whose semantics can't be expressed in the Abstract Machine that MIR-transform and MIR-to-LLVM-IR correctness proofs rely on — an unprecedented kind of break, worse than prior type-system-assumption-breaking RFCs — and without integration into `Result`, async, `==`, or newtypes the feature will feel bolted on.
Tag: fact
Claims: a-sa29-f013113-c2

### externref-in-rust--table-index-in-rust-code
Summary: `externref` should act only as a table index everywhere in ordinary Rust code, with the real WebAssembly `externref` crossing only at FFI boundaries, and an optimization pass could elide the table insert/extract round-trip when a value is merely passed through — a non-zero-cost wrapper that could work better than a first-class language type.
Tag: tradeoff
Claims: a-sa29-f013113-c3

### externref-in-rust--keep-out-of-language-core
Summary: WebAssembly's design oddities — even ones with prior art like Clang's own non-standard `__externref_t` extension, unmatched by GCC or MSVC — shouldn't be papered over by changing the language core; languages shouldn't change at such a fundamental level to support something this niche.
Tag: taste
Claims: a-sa29-f013113-c4

### extract-single-use-function--extract-for-communication
Summary: Pulling logic into its own named method is worth doing even for a single caller, because a well-named function with a defined input/output lets the reader trust what it does without re-deriving it — functions are a tool for communicating blocks of code, not just for reuse — and the same reasoning applies to eliminating verbatim-duplicated logic across two call sites: it should become one documented method rather than risk silent drift between copies.
Tag: tradeoff
Claims: b-sb04-f001392-c5, b-sR12-f005085-c1

### extract-single-use-function--keep-inline
Summary: Moving logic that is very specific to one caller into its own method isn't useful and risks being actively misleading, since a name given to the extracted method (like `visible`) can promise more generality or guarantee than the logic actually provides.
Tag: taste
Claims: b-sb04-f001392-c6

---
Notification: Filled positions-04.csv (60 claim rows) and summaries-04.md (49 positions) for input-b1-04.md, covering questions from `doctests-must-compile` through `extract-single-use-function`. One low-confidence call is flagged: a `dyn-compatibility-rules-relaxation` claim mixes language matching both listed positions in one quote, mapped to the timeline/possibility framing. All other 59 claim-to-position assignments are high confidence from quote and paraphrase alone, no sources opened.
