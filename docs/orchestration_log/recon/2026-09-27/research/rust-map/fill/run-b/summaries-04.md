# Blind fill summaries, batch 1, file 04 of 13 (run b)

## doctests-must-compile--p1
Summary: Every code block embedded in a doc comment is required to be valid, compiling Rust, because the project treats doc-comment examples as unit tests in their own right, not merely illustrative prose.
Tag: fact
Claims: a-sR07-f002347-c1

## downstream-vendor-removed-api-vs-rework--vendor-removed-trait
Summary: When a removed piece is needed and reworking the integration is too costly right now, the fallback is to replicate the dropped functionality directly inside the downstream project's own codebase.
Tag: tradeoff
Claims: b-sT07-f003809-c3

## downstream-vendor-removed-api-vs-rework--rework-downstream
Summary: A downstream project hit by the same removal attributes the resulting pain to its own prior "horrifying" workarounds — dynamically generated columns that depended on the removed piece — rather than treating the removal itself as the fault, and offers to work through the fallout.
Tag: tradeoff
Claims: b-sT07-f003809-c4

## durable-job-queue-vs-in-process--p1
Summary: A background job queue is deliberately backed by durable Postgres storage rather than kept in memory, because an in-memory queue's jobs would simply disappear the moment the service has any outage.
Tag: fact
Claims: b-sT09-f011688-c1

## dyn-compatibility-rules-relaxation--p1
Summary: Even a carefully sketched, higher-ranked-bound version of a `dyn`-compatible trait that would satisfy a real use case is judged not close to landing — "years and years, if ever" — with the plain `dyn` equivalent probably not even plausible.
Tag: fact
Claims: a-sa30-f013276-c1

## dyn-compatibility-rules-relaxation--p2
Summary: `dyn Trait`'s object-safety rules are judged too constraining, with real doubt about whether many of them can be lifted at all — voiced alongside the fact that the next-generation trait-resolver rewrite meant to eventually address this has been underway since 2015.
Tag: fact
Claims: a-sa30-f013276-c5

## dynamic-ecs-component-typed-id--p1
Summary: Wrapping a runtime-registered `ComponentId` in a typed witness (`TypedComponentId<T>`) lets dynamic queries register and access multiple components sharing the same underlying type safely, replacing manual pointer work and unsafe code with a compile-time guarantee.
Tag: fact
Claims: a-02-f001231-c1

## easy-mode-rust--p1
Summary: As a team new to Rust on a security-critical project, the deliberate choice was owned types instead of borrowed references and `Arc<RwLock<T>>` instead of lock-free structures, specifically to minimize borrow-checker friction for engineers new to the language — while keeping the door open to refactor toward more advanced, performant idioms later.
Tag: tradeoff
Claims: b-sb24-f011295-c1

## ecs-events-first-architecture--p1
Summary: Modeling every cross-system state change (granting XP, playing a sound, updating a tile) as a cascade of events made each system easy to reason about and reuse in isolation, at the real cost that a failure partway through a cascade cannot be rolled back — so every handler has to defensively stop propagation itself to keep the game in a stable state.
Tag: tradeoff
Claims: b-sb25-f012561-c1

## ecs-relationship-fragmenting--p1
Summary: Several concrete query operations — wildcard queries, named wildcard queries, nested joins, efficient up-traversal, efficient sibling queries — are only possible at all when relationship edge information is exposed at the archetype level, which a non-fragmenting, component-based approach cannot provide.
Tag: fact
Claims: b-sb07-f002142-c3

## ecs-relationship-fragmenting--p2
Summary: Fragmenting relationships would be useless for a real use case and would just produce one archetype per entity; the non-fragmenting, relationship-type-keyed approach is what's actually needed, a judgment independently echoed by an ECS subject-matter expert.
Tag: tradeoff
Claims: b-sb07-f002142-c4

## ecs-relationship-source-of-truth--p1
Summary: Making the relationship component the single, authoritative source of truth — so the reflected target collection can never be populated directly — lets the system rely on component lifecycles to prevent duplicates instead of scanning at runtime, buying O(1) inserts in exchange for that one constraint, versus a symmetric two-sided design that needs scanning and hashing to stay consistent.
Tag: tradeoff
Claims: a-sa04-f002554-c1

## ecs-relationship-type-level-exclusivity--p1
Summary: Encoding a relationship's exclusivity (one-to-one, one-to-many, etc.) at the type level is preferred because it makes incorrect usage fail to compile, improves error messages, and keeps the model close to how existing hierarchy types already read for users, for reflection, and for scene-serialization formats.
Tag: tradeoff
Claims: b-sb07-f002142-c1

## ecs-relationship-type-level-exclusivity--p2
Summary: Type-level exclusivity isn't even fully correct — nothing stops an entity from holding both a one-to-one and a one-to-many edge component of the same relationship type — and it forces every query call site to know and restate the edge's shape; one consistent query API regardless of exclusivity matters more than having that option.
Tag: tradeoff
Claims: b-sb07-f002142-c2

## ecs-ui-large-vs-small-systems--p1
Summary: Large "god" UI systems with dozens of queries are simple to write but constantly conflict with the borrow checker, and switching to a widget-per-system pattern helps isolate conflicts but forces repeated manual world/state access that itself risks new borrow errors — an acknowledged ongoing problem with no settled solution either way.
Tag: fact
Claims: b-sb25-f012561-c3

## embedded-crash-policy-kernel-vs-supervisor--p1
Summary: There is no right answer to whether a crashed task should restart immediately, back off, or give up, so the kernel deliberately does not hardcode that policy at all — it only records the fault and notifies a userspace supervisor task, leaving the actual recovery decision to the application programmer since it depends on context.
Tag: tradeoff
Claims: a-sa17-f008217-c1

## embedded-deferred-log-formatting--p1
Summary: The same log line costs 1675 instructions when formatted to a human-readable string on-device versus 1050 instructions when sent as a raw value plus a format-string ID for the host to decode later, and more efficient logging directly means being able to afford to log more for the same time-and-power budget.
Tag: fact
Claims: a-sa14-f005162-c1

## embedded-framework-bundles-hal-and-executor--p1
Summary: The framework aims to provide only the execution/concurrency layer, leaving the platform HAL and PAC to the user, and separately aims to give tasks exclusive access to hardware resources as low-level as possible — ideally hardware-guarded — specifically to avoid needing software-level locking at all.
Tag: tradeoff
Claims: a-sB04-f000227-c5

## embedded-interpreter-stopgap--p1
Summary: Running a full ECMAScript interpreter inside their own Wasm module to support `eval`, which the host platform doesn't natively support, is acknowledged plainly as "a runtime on top of a runtime, which doesn't seem optimal, and it isn't" — but it works well enough as a stopgap until native support exists.
Tag: tradeoff
Claims: a-sa14-f004985-c2

## embedded-panics-compile-time-vs-recovery--p1
Summary: Because nothing restarts the one task that supervises everything else if it crashes, that task specifically is compiled with a no-panic feature so any unoptimized-away panic becomes a link-time failure — catching that whole class of crash at compile time for the one task that has no runtime safety net above it.
Tag: fact
Claims: a-sa17-f008217-c2

## emscripten-vs-native-rust-wasm--p1
Summary: Emscripten's mocked-dependency emulation layers make compiled binaries bulky and slow, so the choice made is native Rust compiled directly to WebAssembly via `wasm-bindgen`, avoiding those unnecessary emulation layers entirely.
Tag: fact
Claims: a-sa14-f004985-c1

## emulate-specialization--p1
Summary: Instead of two separate constructors for a read-only and a read-write variant, one constructor is kept with a single `Option<SyncFn>` field that only trait-bound-gated impl blocks (those requiring `Read + Write + Seek`) can set to `Some`, which also fixed a real bug where the read-write variant's writes silently failed to sync.
Tag: fact
Claims: b-sb20-f007213-c1

## encode-invariant-in-representation--p1
Summary: A data model's types are deliberately defined so invalid states are unrepresentable at all — an enum with one variant per transaction version, for instance, makes it impossible to even construct a transaction carrying signature data or proof types that don't belong to its own version.
Tag: fact
Claims: b-bk03-f000267-c2

## encode-invariant-in-representation--encode-in-types
Summary: Storing the log2 of a size rather than the raw size directly is offered as a concrete instance of encoding a constraint in the representation itself, which cuts down on the invalid states and the assertions that would otherwise be needed to guard against them elsewhere in the code.
Tag: fact
Claims: b-sb05-f001582-c1

## enum-glob-import-in-match--p1
Summary: Adding a local `use Enum::*;` glob import just above a block of match arms is suggested specifically to drop the repeated type-qualified prefix from each arm, favoring terser match arms over fully qualified variant paths.
Tag: taste
Claims: b-sR03-f000763-c3

## enum-vs-dyn-trait-closed-set--static-by-default
Summary: `Box<dyn Trait>` is treated as the slowest and least idiomatic option, worth reaching for mainly as a guaranteed-size bound or an escape hatch for one oversized enum variant; enums (`enum_dispatch`-style) are the recommended default for a fixed, known set of types since they drop heap allocation and vtable indirection while staying entirely safe — a stance also reflected in redoing a graph representation as node enums after review.
Tag: tradeoff
Claims: a-sa17-f007884-c2, a-sa17-f007884-c1, a-sa07-f003704-c3

## enum-vs-dyn-trait-closed-set--open-trait-for-extensibility
Summary: A closed enum enumerating access-control configurations is replaced by an open trait with connect/disconnect hooks, so embedders can implement arbitrary policy logic instead of being limited to choosing among a fixed set of enum variants.
Tag: tradeoff
Claims: b-sR10-f004741-c3

## enum-vs-dyn-trait-closed-set--unsafe-unions-for-memory
Summary: Going beyond the safe enum default into hand-rolled unsafe unions — `ManuallyDrop`, pointer aliasing via `transmute_copy` — is treated as a deliberate, specialized escalation past safe Rust, worth it specifically to shrink a value's size below what even a tightly packed enum could achieve, when memory layout is worth the added unsafety.
Tag: tradeoff
Claims: a-sa17-f007884-c3

## enum-vs-flags-and-optionals--enum
Summary: Two independent fields (an optional value and a set of alternatives) are collapsed into a single, non-exhaustive enum specifically so future variants can be added without another breaking change; separately, a plain boolean flag governing a whole subsystem's behavior is replaced by a named, multi-state enum on the judgment that it reads more clearly and is "more secure" than the boolean it replaced.
Tag: tradeoff
Claims: b-sR08-f003731-c1, b-sR08-f003531-c1, b-sR08-f003531-c2

## epoll-vs-io-uring--p1
Summary: `epoll` is chosen for a hand-built async reactor specifically because it hits the "standard" tradeoff between being too slow and too experimental, with an explicit note that `io_uring` might take over that role in a few years.
Tag: tradeoff
Claims: b-sb21-f008396-c1

## ergonomic-sugar-now-or-later--p1
Summary: A small utility PR assembled quickly ships with the raw mechanism only; a macro or trait wrapper to dress it up as reusable sugar could be added later, but there is very little reason to do that now beyond pure syntactic convenience.
Tag: taste
Claims: a-sa11-f004512-c4

## ergonomics-vs-explicitness--p1
Summary: Explicitness functions as one of Rust's real, de facto core values in practice, even though — pointedly, ironically — it is never actually written down anywhere as a stated goal of the language the way other values are.
Tag: tradeoff
Claims: a-sa28-f012469-c9

## ergonomics-vs-explicitness--p2
Summary: The 2017 ergonomics-initiative RFCs, pushing implicit sugar into places code was hard to write, are acknowledged by their own author as knowingly controversial and likely to need scaling back — self-aware about trading away some of the language's explicitness for ergonomic convenience.
Tag: tradeoff
Claims: a-sa28-f012469-c10

## error-enum-scope-module-vs-function--p1
Summary: Error handling started with one large enum covering everything a module could fail at, found that unwieldy in practice, and moved to a nested hierarchy of smaller, descriptively named enums scoped to what one specific function or operation can fail at.
Tag: taste
Claims: a-sa14-f005149-c2

## esp32-psram-display-dma-strategy--p1
Summary: Every framebuffer's last DMA descriptor is linked back to its own first descriptor to form an infinite loop, and switching buffers means relinking descriptors rather than ever restarting a transfer — an approach whose author reports breaks down once PSRAM's bandwidth limits enter the picture.
Tag: fact
Claims: b-sT05-f002499-c1

## esp32-psram-display-dma-strategy--p2
Summary: Two PSRAM-backed framebuffers feed two small SRAM bounce buffers refilled by looping Mem2Mem DMA, tracked through eight descriptors that locate the emitted slice via a DMA interrupt and cancel late refills, reaching 31.1 FPS glitch-free — explicitly rejecting both XIP from PSRAM and CPU-copy approaches (the latter called "glacial").
Tag: fact
Claims: b-sT05-f002499-c2

## esp32-psram-display-dma-strategy--p3
Summary: Cyclic DMA descriptors failed after the very first frame in practice, while switching to acyclic descriptors that restart the transmission after each frame works — described as fine, if "not as nice" as a true infinite loop — with an offer to upstream a generic version of the fix.
Tag: fact
Claims: b-sT05-f002499-c3

## esp32-psram-display-dma-strategy--p4
Summary: After getting a bounce-buffer renderer working, flash contention and PSRAM bandwidth still slowed the application enough that the practical resolution was staying on a smaller I8080 display at lower size and resolution rather than pushing the PSRAM-fed RGB approach further.
Tag: fact
Claims: b-sT05-f002499-c4

## example-data-domain-struct-vs-generic--p1
Summary: A small dedicated struct (name, address, email, generated in the app constructor) is preferred over generic nested collections, explicitly conceding it's "gold plating" for a demo, but valued because it gives a clean, concrete way to show how real-world data actually maps into table columns.
Tag: taste
Claims: b-sR03-f000763-c1

## exclusive-access-default-in-task-api--p1
Summary: The framework assumes exclusive (mutable) access to a resource by default; a task can instead opt into shared (read-only) access, which skips the lock API entirely even when the resource is contended by tasks running at different priorities, at the cost of losing the ability to mutate through that access.
Tag: fact
Claims: a-sB04-f000227-c1

## executor-agnostic-libraries--p1
Summary: Libraries exposing async APIs should not depend on a specific executor or reactor unless they genuinely need to spawn tasks or define their own async I/O or timer futures, reasoned directly from the ecosystem's real fragmentation — Tokio's reactor and I/O traits are not directly compatible with async-std or smol's — where only binaries should really own scheduling.
Tag: fact
Claims: b-bk01-f000233-c12

## explicit-vs-convenience-memory-defaults--p1
Summary: Neither a performance-first nor a convenience-first memory-model default is simply better: one suits systems, embedded programming, and compilers/browser engines, the other suits UI, servers, and other parts of compilers and operating systems, and the overlap between where each is the right choice is expected to keep growing over time.
Tag: tradeoff
Claims: b-sR12-f005668-c1

## explicit-vs-implicit-indirection--p1
Summary: Requiring the programmer to write the indirection explicitly (`Box<TreeNode<T>>`) for a recursive type is framed favorably as making the problem visible and forcing it to be dealt with directly, in contrast to a compiler-handled, more automatic indirection mechanism.
Tag: taste
Claims: b-sR12-f005668-c2

## expose-fixed-array-vs-wrapper-type--p1
Summary: A fixed-size array like `[u8; 6]` should be wrapped in a dedicated semantic type with derives and a `Display` implementation, motivated directly by noting that a same-shaped but larger variant (an 8-byte IEEE MAC) could never be returned from the array's current shape.
Tag: tradeoff
Claims: a-sa11-f004265-c1

## expose-fixed-array-vs-wrapper-type--p2
Summary: The same author reverses a day later, pushing back on returning the fixed-size array at all and preferring a slice-typed return instead, as the way to keep the door open for a larger variant.
Tag: tradeoff
Claims: a-sa11-f004265-c3

## expose-rustc-internals-rustdoc-json--p1
Summary: Implied trait bounds turn out to be load-bearing for detecting SemVer breaks — missing them produces both false positives and false negatives — and since it's technically infeasible for an external tool to re-derive them while the compiler already has that capability internally, the request made is for the compiler team to expose implied bounds through a structured interface (rustdoc JSON) using those existing internal APIs.
Tag: fact
Claims: a-sa20-f009698-c4

## extend-foreign-trait-type--p1
Summary: Bolting on another parallel enum type without re-evaluating the complexity of an already fairly unintuitive API is treated with real wariness; a narrowly scoped method or a small set of new enum variants is the preferred fix over adding a whole second type.
Tag: tradeoff
Claims: b-sb06-f002027-c1

## extend-foreign-trait-type--p2
Summary: The crate effectively already has "its own" version of the foreign type in practice — currently just a lazy type alias — and users shouldn't need to know or care which one they're going through, so making it a real, independently extensible type of its own is fine even though it's a breaking change.
Tag: tradeoff
Claims: b-sb06-f002027-c2

## externref-in-rust--new-restricted-lang-type
Summary: JavaScript interop is not a niche or complex topic but a major quality-of-life story worth solving at the language level, justifying a new opaque, unforgeable reference type — legal only as a bare top-level type in function parameters, returns and locals — that lowers directly to WebAssembly's own `externref` and lets host references marshal across foreign calls.
Tag: tradeoff
Claims: a-sa29-f013113-c5, a-sa29-f013113-c1

## externref-in-rust--must-fit-abstract-machine
Summary: Introducing a fundamentally new kind of thing whose semantics can't be expressed in the Abstract Machine that justifies the compiler's own MIR-transform and MIR-to-LLVM-IR correctness proofs is an unprecedented kind of break, worse than prior type-system-assumption-breaking proposals, and without integration into `Result`, async, equality, or newtypes the feature will feel permanently bolted on.
Tag: fact
Claims: a-sa29-f013113-c2

## externref-in-rust--table-index-in-rust-code
Summary: A non-zero-cost wrapper could work better than a first-class language type: `externref` would act as a table index everywhere in Rust-only code, with the real WebAssembly `externref` crossing only at FFI boundaries, and an optimization pass could elide the table insert/extract round-trip whenever a value is merely passed straight through.
Tag: tradeoff
Claims: a-sa29-f013113-c3

## externref-in-rust--keep-out-of-language-core
Summary: The underlying construct is Clang's own non-standard extension, matched by neither GCC nor MSVC, so WebAssembly's design oddities should be papered over by the compiler or runtime rather than justifying a change at the language's core level for something this niche.
Tag: tradeoff
Claims: a-sa29-f013113-c4

## extract-single-use-function--extract-for-communication
Summary: Pulling logic into its own named method is valued even for a single caller, because a well-named function with a defined input and output lets a reader trust what it does without re-deriving the logic themselves — functions are "a tool for communicating blocks of code," not just for reuse — and the same reasoning applies to a check duplicated verbatim at two call sites, which should be one method on the owning type documenting the real contract so drift becomes a compile error rather than a silent bad write.
Tag: tradeoff
Claims: b-sb04-f001392-c5, b-sR12-f005085-c1

## extract-single-use-function--keep-inline
Summary: Moving logic this specific to one caller into its own method isn't seen as useful, and naming it risks being actively misleading about what the extracted function actually guarantees versus what it merely happens to do at its one call site.
Tag: tradeoff
Claims: b-sb04-f001392-c6
