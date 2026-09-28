# Summaries, batch 1 file 11 (fill b)

## Question `rust-vs-c-inherent-performance`

### rust-vs-c-inherent-performance--no-inherent-advantage
Summary: There's no inherent reason either language is faster; it's all project-specific. Where C codebases outperform Rust ones today, that's usually because they're older and have had far more engineer-hours of optimization poured into them, not a property of C itself.
Tag: fact
Claims: a-saL1-f005516-c1

### rust-vs-c-inherent-performance--types-enable-optimizations
Summary: A language with more semantic granularity gives the compiler more true invariants to exploit — Rust code built on iteration rather than raw array access can drop bounds checks entirely, and Rust puts the equivalent of C's `restrict` on every reference without an `UnsafeCell`, encoded in the type system rather than left as a convention. That's a real, structural edge over C, on top of being ahead on pointer provenance semantics.
Tag: fact
Claims: a-saL1-f005516-c2, a-saL1-f005516-c3

### rust-vs-c-inherent-performance--real-overheads
Summary: Safe Rust has real, measurable costs: it requires a value at construction time rather than allowing dataflow-based init-before-use, so a large array or small-object allocator ends up eagerly zero-initializing memory it may never read first, sometimes bloating codegen enough to block inlining. Trivial new features can force large refactors because they necessitate new borrowing schemes, and clones or `Rc` get added defensively just to satisfy the borrow checker where they aren't algorithmically necessary. Looking at actual disassembly on nontrivial examples shows the recurring costs plainly: bounds checks on array/division/shift access, unsafe-gated SIMD intrinsics, iterators that don't optimize as well as hoped, `RefCell` overhead, and un-collapsible `Result` wrapping — which is why Rust solutions don't top competitive-programming leaderboards.
Tag: fact
Claims: a-saL1-f005516-c9, a-saL1-f005516-c12, a-saL1-f005516-c4

### rust-vs-c-inherent-performance--init-cost-narrow
Summary: Rust doesn't require init for all variables broadly — it merely requires init-before-use based on dataflow analysis, the same as any ordinary variable. The zero-init cost being described should only bite in narrow cases like large arrays or read buffers, not as a blanket tax, and it's fair to ask whether the allocator scenario generalizes at all.
Tag: fact
Claims: a-saL1-f005516-c10

### rust-vs-c-inherent-performance--composability-wins
Summary: The reason a B-Tree is usable in Rust where an AVL tree is the safer bet in C isn't raw speed, it's composability: an intrusive C B-Tree is too risky to trust with your hands in everything's underwear, so engineers default to the worse-performing structure. In Rust it's trivial to write code abstract over a data structure, so a wrong pick found in profiling can be swapped easily, whereas in C the implementation details leak through unless you wrap them in painful macros — replacing a hand-rolled generic concurrent hash table with an off-the-shelf container plus a lock came out both more maintainable and faster. What matters is what engineers are actually willing to ship, not who wins a benchmark race.
Tag: tradeoff
Claims: a-sa15-f005516-c1, a-saL1-f005516-c13, a-saL1-f005516-c11

### rust-vs-c-inherent-performance--safety-cost-acceptable
Summary: A real safety cost is worth paying: given a choice, a 10% perf hit (40 FPS instead of 45) for a memory-safe implementation that doesn't crash beats an unsafe/unmanaged-heavy one that tops out barely higher and still crashes.
Tag: tradeoff
Claims: b-sb26-f013214-c4

### rust-vs-c-inherent-performance--p1
Summary: The practical gap is partly ecosystem-driven: C's lack of an easily-reached-for hashmap pushes real code toward slow linear searches until it becomes a forced problem, while Rust's easy hashmaps and parallel iterators make fast-by-default collections and code the norm in practice — so the live discussion is just which language makes it easier to write fast programs.
Tag: fact
Claims: a-saL1-f005516-c5

## Question `rust-vs-gc-for-multitenant-runtime`

### rust-vs-gc-for-multitenant-runtime--p1
Summary: A garbage-collected language like Go doesn't have the reliability, strictness, customizability or performance needed to safely run untrusted code for many tenants — no exhaustive Result/Option error handling, hidden allocation costs, and a host GC that would conflict with an embedded engine's own GC in the same process. Rust (with some C++ for the embedded engine) was chosen instead, and Rust's cost model is transparent enough that nothing allocates without an explicit `.clone()`.
Tag: tradeoff
Claims: a-sa22-f011092-c1

## Question `rust-worth-it-for-failure-heavy-infra`

### rust-worth-it-for-failure-heavy-infra--rust-for-failure-heavy-infra
Summary: HTTP has too many edge cases and possibly-malicious clients to leave to chance; Rust's ownership and pattern matching are what let a small team actually manage that casework in an ingress service handling client disconnects, malformed and out-of-order events, and spot preemption. Replacing an earlier Python-based ingress with this Rust service cut 502 errors by 99.7%.
Tag: tradeoff
Claims: b-sb19-f005948-c1, a-sa15-f005948-c1

## Question `safe-wrapper-soundness-scope`

### safe-wrapper-soundness-scope--p1
Summary: Calling this type "safely useable" is too vague and overpromises — a composition like boxing it with external-memory backing is not actually safe to use, so the label shouldn't claim more than the type can back up under every instantiation.
Tag: fact
Claims: b-sR10-f004804-c1

### safe-wrapper-soundness-scope--p2
Summary: Without a full formal proof, a cache writeback is, as far as can be told, generally a safe operation, and invalidate isn't called on these paths — so it's reasonable to call the current alignment guarantees fine for this type at this time, even if the phrasing is wishy-washy.
Tag: tradeoff
Claims: b-sR10-f004804-c2

## Question `same-state-transition-trigger`

### same-state-transition-trigger--p1
Summary: It's genuinely unclear whether a transition into the same state the entity is already in should be excluded from triggering — this check prevents despawning on same-state transitions, and whether that's actually wanted depends on use cases not yet known.
Tag: tradeoff
Claims: b-sb14-f004398-c5

### same-state-transition-trigger--p2
Summary: It doesn't really make sense to react to changing into a state you're already in — that's a no-op by nature and shouldn't trigger anything.
Tag: taste
Claims: b-sb14-f004398-c6

### same-state-transition-trigger--p3
Summary: Some users have specifically pushed for allowing same-state transitions to trigger, precisely to support a "reload" pattern, so the naive (non-special-cased) behavior is the right default here.
Tag: fact
Claims: b-sb14-f004398-c7

## Question `scoped-impls-nameable`

### scoped-impls-nameable--p1
Summary: Naming these implementations is strongly the wrong call — it's detrimental for clarity, awkward syntactically, and harder to use. Anonymity keeps coherence checking simple within one scope, lets the module double as the name in error messages, and avoids the breaking-change rules naming would force whenever an implementation is later broadened.
Tag: fact
Claims: a-sa19-f009123-c1

### scoped-impls-nameable--p2
Summary: Names are wanted here: an explicit mechanism to specify a type along with explicitly chosen impls would make the implicit scoped-impl behavior desugar from something writable, even if users rarely write the explicit form by hand. Names would also let two implementations of the same trait/type coexist in one module and let compiler errors point at a normal path instead of "the impl from this module."
Tag: tradeoff
Claims: a-sa19-f009123-c3, a-sa19-f009123-c2

## Question `scratch-buffer-vs-per-call-alloc`

### scratch-buffer-vs-per-call-alloc--p1
Summary: The merge working set should live in a caller-owned scratch buffer reused across calls, so the hot loop never touches the allocator at all — removing the repeated per-pre-token allocations and priority-queue construction the prior version paid for.
Tag: fact
Claims: b-sR12-f005120-c2

## Question `scratch-register-type-enforced`

### scratch-register-type-enforced--encode-in-types
Summary: Relying on the type system to identify or audit scratch-register usage — or giving exclusive access analogous to allocatable registers — is the right fix, because passing a scratch register around as a parameter extends its live range and raises the risk of unintentional clobbering.
Tag: tradeoff
Claims: a-sa05-f002466-c1

### scratch-register-type-enforced--p1
Summary: Scratch registers in this compiler aren't tracked by the register allocator, so unintentional clobbering is a serious risk; the live range of a scratch register should be as short as possible, and that means minimizing it and avoiding passing it around as a parameter, even if it means redefining signatures and accepting some duplication across ISA-specific paths.
Tag: tradeoff
Claims: b-sR05-f002466-c1

## Question `semver-break-signaling-in-ci`

### semver-break-signaling-in-ci--p1
Summary: A change that breaks a published crate's public API must be marked with `!` in both the PR title and the branch commit that introduces the break — the CI gate reads the PR title to skip semver-checks and require a breaking-change fragment, while the release tooling separately reads the landed commits to decide the major-version bump.
Tag: fact
Claims: b-bk03-f000267-c7

## Question `serde-centralization`

### serde-centralization--p1
Summary: Rust's orphan rules have created a real ecosystem composition problem: crates that want to interoperate with a popular derive macro like serde have to piggyback on it rather than add independent support, which functionally corners the ecosystem around one crate.
Tag: fact
Claims: a-sa25-f011413-c2

### serde-centralization--p2
Summary: Rather than generating a new derive for every new trait or behavior, the sound path forward is for crates to ship structural data about their types once, and let behaviors be built generically over that data — the strategy just needs adjusting, not abandoning the idea that many crates build on one shared foundation.
Tag: tradeoff
Claims: a-sa25-f011413-c3

## Question `serialization-format-choice`

### serialization-format-choice--established-binary-format
Summary: An established, well-defined binary format like postcard is preferable to a bespoke one — it's simpler to target than JSON and close to what's already being generated, and it doesn't need extra const-time logic to format strings and numbers. It is non-self-describing, so the enum-case order has to be preserved for the protocol to stay stable long-term, but that's a requirement to design around, not a reason to avoid it.
Tag: tradeoff
Claims: a-sa03-f002300-c1, a-sa06-f003590-c2

### serialization-format-choice--cbor-for-no-std
Summary: MessagePack (via `rmp-serde`) was dropped for CBOR (via `ciborium`) because `rmp-serde` isn't no-std compatible and its upstream has been inactive for over a year; CBOR is IETF-standardized, Serde-recommended, no-std-capable, and still preserves enum variant information.
Tag: fact
Claims: b-sR08-f003587-c1

### serialization-format-choice--toml-for-consistency
Summary: Why not TOML, to stay consistent with the rest of the Rust ecosystem?
Tag: taste
Claims: b-sb09-f003030-c1

### serialization-format-choice--yaml-for-convenience
Summary: TOML's representation is inconvenient for this use case; YAML is the nicest representation available, and the spec doesn't forbid wider integers even if it doesn't mandate them, so the missing i128 support is a library gap worth patching (or trying an alternative crate like facet-yaml) rather than a reason to abandon YAML — especially since `serde_yml` itself looks unmaintained.
Tag: taste
Claims: b-sb09-f003030-c2, b-sb09-f003030-c4, b-sb09-f003030-c6, b-sb09-f003030-c3

### serialization-format-choice--no-custom-format
Summary: After evaluating `serde_yml`, `serde_yaml` and `facet-yaml`, YAML tooling in the Rust ecosystem is a dead end for i128 support; defining a custom config language is an alternative, but probably too much effort to "just try it."
Tag: tradeoff
Claims: b-sb09-f003030-c5

### serialization-format-choice--ship-now-switch-later
Summary: This format is strictly internal right now, so proceed with YAML plus workarounds, and switch library or format later if something better shows up.
Tag: tradeoff
Claims: b-sb09-f003030-c7

### serialization-format-choice--p1
Summary: Bincode is a risky format to reach for because it depends on the exact order and type of struct fields — fine for the legacy column families that already use it via serde, but don't use it for new ones.
Tag: fact
Claims: b-bk03-f000267-c9

## Question `service-fault-isolation-degrade`

### service-fault-isolation-degrade--contain-and-continue
Summary: `Incoming::accept` can fail for benign network reasons, and such failures should be logged and passed over, not treated as fatal. More broadly, commit as a design rule before writing any code that any failure degrades to a blank frame or a missing element, never a dead session — the service has to keep rendering hostile, unreliable input without ever dropping the session it's holding.
Tag: tradeoff
Claims: a-sR05-f001981-c1, a-sa14-f004985-c3

## Question `share-via-combinator-vs-separate-impls`

### share-via-combinator-vs-separate-impls--p1
Summary: `reduce_sum` and `all_reduce_sum` are different operations, but the duplication between them is real and worth solving with a local op-combinator library — even if that library never gets exposed to end users.
Tag: tradeoff
Claims: a-sR11-f003983-c2

## Question `shared-hw-resource-refcount-vs-raii`

### shared-hw-resource-refcount-vs-raii--p1
Summary: Unless references are counted per modem clock controller, repeatedly calling the function to disable the PHY clock on one controller would eventually disable it even while a different modem still relies on it — so a `RadioClockController` needs its own per-modem reference count.
Tag: tradeoff
Claims: a-sa05-f003169-c1

### shared-hw-resource-refcount-vs-raii--p2
Summary: If only the peripheral singletons — already unique and exclusive by construction — can touch the shared clock, a separate controller object and manual ref-count aren't needed at all; the clock-control logic should live directly on the radio peripheral structs. Converging on this, the separate `RadioClockController` was removed, reducing the design to a single shared PHY ref-count guarded by the peripheral-singleton pattern.
Tag: tradeoff
Claims: a-sa05-f003169-c2, a-sa05-f003169-c3

## Question `shared-model-crate-vs-domain-split`

### shared-model-crate-vs-domain-split--p1
Summary: A domain-driven crate split was something that could have been done, but by the time it came up the project was already too far along — there wasn't the time or energy left to do it, so `model` stayed the catch-all for whatever must be shared, kept as small as discipline allows.
Tag: tradeoff
Claims: b-sb25-f012561-c2

## Question `shared-mutable-state-vs-explicit-passing`

### shared-mutable-state-vs-explicit-passing--restructure-for-explicit-ownership
Summary: Rather than reach for a `Mutex` inside a type to satisfy a `Sync` bound, move the mutable state to the owning `Session` and access it there instead — a preference for no `Arc` at all persists even after conceding an immediate constraint requires it, with an eye to revisiting later. An `Arc<Mutex<>>` that lets callers change encoding without the containing type knowing is itself an objection: pass or return the encoding explicitly. Turning fields into `Rc<RefCell<_>>` doesn't actually solve the reentrant-borrow problem either — dispatching from inside an active borrow still panics — so the working answer is to clone whatever refs are needed before dropping the state, or better, pass a `cx` context down the stack the way the rest of the codebase already does.
Tag: tradeoff
Claims: a-sR07-f002155-c1, a-sR07-f002155-c2, a-sa06-f003414-c2, b-sb04-f001022-c1, b-sb04-f001022-c2

### shared-mutable-state-vs-explicit-passing--shared-where-structure-demands
Summary: `Rc`/`Arc` are the right tool when the structure of a program makes it genuinely hard to tell how many readers a piece of data will have; `RefCell` fits only a narrow range of problems since it moves borrow checking to runtime, works only single-threaded, and panics on violation.
Tag: tradeoff
Claims: b-sT09-f005440-c1

## Question `ship-polyfill-before-spec`

### ship-polyfill-before-spec--p1
Summary: Ship a "polyfill" that developers can play with today while they're waiting for WASI 0.3 and real async, rather than leaving them with nothing until the spec finalizes.
Tag: tradeoff
Claims: b-sR03-f000889-c1

## Question `silent-fallback-vs-explicit-error`

### silent-fallback-vs-explicit-error--p1
Summary: If multiple TCP sockets are listed, using the first one silently could lead to odd behavior if it's the wrong one — this should probably be an error instead.
Tag: tradeoff
Claims: a-sa14-f005079-c6

### silent-fallback-vs-explicit-error--p2
Summary: It would be surprising for `--systemd-listenfd` to silently fall back to the process listening itself just because of a mismatched environment variable that got ignored — so both the multiple-socket case and the no-usable-socket case were made errors instead of silent fallbacks.
Tag: tradeoff
Claims: a-sa14-f005079-c7

## Question `single-pass-vs-multi-pass-iteration`

### single-pass-vs-multi-pass-iteration--p1
Summary: If you're iterating and collecting, then iterating the result three more times, it's neater to iterate once and collect the max for each column in that single pass.
Tag: tradeoff
Claims: b-sR03-f000763-c2

## Question `single-vs-multi-threaded-executor`

### single-vs-multi-threaded-executor--p1
Summary: A multi-threaded executor can speed up workloads with many tasks by making progress on several at once, but synchronizing data between tasks gets more expensive; rather than defaulting to one or the other, measure performance for your application when choosing between a single- and multi-threaded runtime.
Tag: fact
Claims: b-bk01-f000233-c13

## Question `slint-vs-qt`

### slint-vs-qt--p1
Summary: Having reimplemented an existing QML demo app in Slint from scratch, Slint currently seems like the best toolkit for Rust — its build-time-checked, Rust-native, easily cross-compiled model is worth the tradeoff against QML's more mature multimedia/3D/testing tooling and Qt's licensing costs, especially for embedded targets.
Tag: tradeoff
Claims: b-sb23-f011133-c1
