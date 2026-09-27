# Fill A — summaries, file 11

## Question `rust-vs-c-inherent-performance`

### rust-vs-c-inherent-performance--no-inherent-advantage
Neither language has an inherent speed edge; where C code is faster today it's because those codebases are older and have absorbed more optimization effort, not a property of C itself.
tag: tradeoff
claims: a-saL1-f005516-c1

### rust-vs-c-inherent-performance--types-enable-optimizations
Rust's type system carries real, checkable guarantees — a `restrict`-equivalent no-aliasing rule on every non-`UnsafeCell` reference, and enough semantic granularity that iteration-based code can drop bounds checks entirely — which the compiler can exploit for optimizations C's weaker type system can't offer.
tag: fact
claims: a-saL1-f005516-c2, a-saL1-f005516-c3

### rust-vs-c-inherent-performance--real-overheads
Safe Rust has concrete, disassembly-visible costs: eager zero-init on large arrays/allocators the dataflow analysis can't reach, bounds checks, unsafe-gated SIMD, RefCell overhead, un-collapsible `Result` wrapping, and clones/`Rc` added defensively just to satisfy the borrow checker — plus trivial features forcing large refactors when they need new borrowing schemes.
tag: fact
claims: a-saL1-f005516-c9, a-saL1-f005516-c12, a-saL1-f005516-c4

### rust-vs-c-inherent-performance--init-cost-narrow
Rust only requires init-before-use by dataflow analysis, not blanket default initialization, so the zero-init cost described elsewhere should bite only in narrow cases like large arrays or read buffers, not "all variables" broadly.
tag: fact
claims: a-saL1-f005516-c10

### rust-vs-c-inherent-performance--composability-wins
Composability lets engineers actually ship the better data structure: Cantrill reaches for a B-Tree in Rust where he'd default to an AVL tree in C because a hand-rolled intrusive C B-Tree is too risky to trust; Chisnall swapped a hand-rolled generic hash table for an off-the-shelf container plus a lock, both more maintainable and faster; the win is measured in what engineers are willing to ship, not benchmark racing.
tag: tradeoff
claims: a-sa15-f005516-c1, a-saL1-f005516-c13, a-saL1-f005516-c11

### rust-vs-c-inherent-performance--safe-rust-matches
Safe Rust, with zero `unsafe` in the author's own code, handles several coordinated CPU-bound threads (refresh, per-frame update, event processing, asset decoding) acceptably where the same coordination would be "really hard" to get right safely in C++.
tag: tradeoff
claims: b-sb26-f013214-c3

### rust-vs-c-inherent-performance--safety-cost-acceptable
Given a session where an unsafe/unmanaged-heavy game crashed three times and struggled near 45 FPS, the stated preference is a 10% perf hit (40 FPS) for a memory-safe implementation that doesn't crash — relaxed safety isn't free performance either.
tag: taste
claims: b-sb26-f013214-c4

### rust-vs-c-inherent-performance--p1
C's lack of an easily-reached-for hashmap pushes real C code toward slow linear searches until forced to fix; Rust's easy hashmaps and parallel iterators make fast-by-default code more common in practice, making the comparison about which language makes it easier to write fast programs.
tag: fact
claims: a-saL1-f005516-c5

## Question `rust-vs-gc-for-multitenant-runtime`

### rust-vs-gc-for-multitenant-runtime--p1
Deno tried Go first for its multi-tenant sandboxed runtime and rejected it for lacking the reliability, strictness, customizability and performance needed to safely run untrusted code; chose Rust (plus some C++ for embedded V8) instead, citing exhaustive Result/Option error handling, explicit allocation cost, no GC conflict with V8's own GC, and easy C++ interop.
tag: fact
claims: a-sa22-f011092-c1

## Question `rust-worth-it-for-failure-heavy-infra`

### rust-worth-it-for-failure-heavy-infra--rust-for-failure-heavy-infra
HTTP ingress has many concurrent edge cases (malformed/out-of-order events, disconnects, spot preemption, possibly-malicious clients); Rust's ownership and pattern matching were chosen specifically to manage that casework, and replacing an earlier Python-based ingress with the Rust service (`modal-http`, on hyper/tokio) cut 502 errors by 99.7%.
tag: fact
claims: b-sb19-f005948-c1, a-sa15-f005948-c1

## Question `safe-wrapper-soundness-scope`

### safe-wrapper-soundness-scope--p1
Calling a wrapper type "safely useable" overpromises when a composition of it — such as boxing it with external-memory backing — is not actually safe to use; the label should not claim more soundness than every instantiation actually delivers.
tag: tradeoff
claims: b-sR10-f004804-c1

### safe-wrapper-soundness-scope--p2
Without a full proof, a cache writeback is judged safe enough in practice for this type's current alignment guarantees, given invalidate isn't called on these paths — a pragmatic, "wishy-washy" call rather than a proven guarantee.
tag: taste
claims: b-sR10-f004804-c2

## Question `same-state-transition-trigger`

### same-state-transition-trigger--p1
It's unclear without more use-case knowledge whether a same-state transition should be excluded from triggering the predicate — the check as written prevents an action (e.g. despawning) on same-state transitions, and whether that's wanted is an open question.
tag: fact
claims: b-sb14-f004398-c5

### same-state-transition-trigger--p2
Reacting to a transition into a state the entity is already in doesn't make sense, so same-state transitions should be suppressed as a no-op.
tag: taste
claims: b-sb14-f004398-c6

### same-state-transition-trigger--p3
Some users specifically want same-state transitions to trigger, for a "reload" pattern, so the naive (non-special-cased) behavior — allowing the trigger — should be used instead of suppressing it.
tag: taste
claims: b-sb14-f004398-c7

## Question `scoped-impls-nameable`

### scoped-impls-nameable--p1
Strongly opposed to naming scoped impls: anonymity keeps coherence checking simple within one scope, lets the module double as an error-message name, and avoids new breaking-change rules that naming would introduce if an impl is later broadened.
tag: tradeoff
claims: a-sa19-f009123-c1

### scoped-impls-nameable--p2
Wants an explicit mechanism to name a type alongside explicitly chosen impls, so two implementations of the same trait/type can coexist in one module and compiler errors can reference a normal path instead of "the impl from this module".
tag: taste
claims: a-sa19-f009123-c3, a-sa19-f009123-c2

## Question `scratch-buffer-vs-per-call-alloc`

### scratch-buffer-vs-per-call-alloc--p1
The prior implementation allocated fresh memory and a new priority queue per pre-token; v1 instead reuses a scratch buffer owned by the caller, so the merge loop never touches the allocator.
tag: fact
claims: b-sR12-f005120-c2

## Question `scratch-register-type-enforced`

### scratch-register-type-enforced--encode-in-types
Proposes relying on the type system to identify or audit scratch-register usage, or exclusive access analogous to allocatable registers, because passing a scratch register as a parameter extends its live range and raises unintentional-clobbering risk.
tag: tradeoff
claims: a-sa05-f002466-c1

### scratch-register-type-enforced--p1
Since scratch registers aren't tracked by the regalloc and must be used sparingly and with extreme caution, the live range should be minimized and passing them as parameters avoided, even if that means redefining signatures and accepting duplication across ISA-specific paths.
tag: tradeoff
claims: b-sR05-f002466-c1

## Question `semver-break-signaling-in-ci`

### semver-break-signaling-in-ci--p1
A change that breaks a published crate's API must carry a `!` marker in both the PR title and the branch commit that introduces the break, because the CI gate reads the PR title to skip semver-checks and require a breaking-change fragment, while release tooling reads the landed commits to decide the major-version bump.
tag: fact
claims: b-bk03-f000267-c7

## Question `serde-centralization`

### serde-centralization--p1
Rust's orphan rules mean crates wanting to interoperate with a popular derive macro must piggyback on it rather than add independent support, which has functionally cornered the ecosystem around one crate (serde).
tag: fact
claims: a-sa25-f011413-c2

### serde-centralization--p2
Rather than generating a new derive for every new trait or behavior, crates should ship structural data about their types once and let behaviors build generically over that data — the many-crates-on-one-derive idea is sound, but the strategy needs adjusting.
tag: tradeoff
claims: a-sa25-f011413-c3

## Question `serialization-format-choice`

### serialization-format-choice--established-binary-format
Postcard is preferred as a simpler, well-defined, already-similar-to-current-output format over a bespoke or JSON serialization; separately, since postcard is non-self-describing, enum case order must be preserved as a stability contract for the protocol to remain stable long-term — a requirement to design around, not a reason to avoid it.
tag: tradeoff
claims: a-sa03-f002300-c1, a-sa06-f003590-c2

### serialization-format-choice--cbor-for-no-std
Switched metadata serialization from MessagePack (`rmp-serde`) to CBOR (`ciborium`) because `rmp-serde` isn't no-std compatible and its upstream has been inactive over a year, while CBOR is IETF-standardized, serde-recommended, no-std-capable, and preserves enum variant information.
tag: fact
claims: b-sR08-f003587-c1

### serialization-format-choice--toml-for-consistency
Questions why the PR uses YAML instead of TOML, given TOML would be more consistent with the rest of the Rust ecosystem.
tag: taste
claims: b-sb09-f003030-c1

### serialization-format-choice--yaml-for-convenience
YAML is judged the nicest available representation once TOML is found inconvenient for the use case; the preference holds even through defending the spec against negativity, suggesting a better-maintained library (facet-yaml) as an alternative, and preferring to patch whichever YAML library is chosen (adding i128 support) over changing the config's own type range.
tag: taste
claims: b-sb09-f003030-c2, b-sb09-f003030-c6, b-sb09-f003030-c4, b-sb09-f003030-c3

### serialization-format-choice--no-custom-format
After evaluating serde_yml, serde_yaml and facet-yaml and finding YAML tooling a dead end for i128 support, floats designing a custom config language but judges it too much effort to "just try it".
tag: tradeoff
claims: b-sb09-f003030-c5

### serialization-format-choice--ship-now-switch-later
Since the format is currently internal-only, proposes proceeding with YAML plus workarounds now, and switching library or format later if something better appears.
tag: tradeoff
claims: b-sb09-f003030-c7

### serialization-format-choice--p1
Bincode is called out as a risky format for anything new because it depends on the exact order and type of struct fields; legacy column families keep it, but new ones should not use it.
tag: fact
claims: b-bk03-f000267-c9

## Question `service-fault-isolation-degrade`

### service-fault-isolation-degrade--contain-and-continue
Failures should be contained rather than fatal: benign accept-time network errors should be logged and passed over rather than treated as fatal, and as a design rule set before writing code, any failure should degrade to a blank frame or missing element rather than a dead session, since the target must render hostile, unreliable input without ever dropping the session it's holding.
tag: tradeoff
claims: a-sR05-f001981-c1, a-sa14-f004985-c3

## Question `share-via-combinator-vs-separate-impls`

### share-via-combinator-vs-separate-impls--p1
Two operations (a local op and its collective counterpart) are legitimately different operations, but the duplication between them is real and worth solving with an internal op-combinator library, even if that library is never exposed to end users.
tag: tradeoff
claims: a-sR11-f003983-c2

## Question `shared-hw-resource-refcount-vs-raii`

### shared-hw-resource-refcount-vs-raii--p1
Proposes a `RadioClockController` that counts references per modem, so that disabling one modem's use of a shared PHY clock doesn't disable it out from under another modem still relying on it.
tag: tradeoff
claims: a-sa05-f003169-c1

### shared-hw-resource-refcount-vs-raii--p2
Questions why a separate controller and manual ref-count are needed at all when only the peripheral singletons — already unique and exclusive by construction — can touch the clock; the clock-control logic should live directly on the radio peripheral structs, and the author ultimately removed the separate ref-counted controller in favor of this.
tag: tradeoff
claims: a-sa05-f003169-c2, a-sa05-f003169-c3

## Question `shared-model-crate-vs-domain-split`

### shared-model-crate-vs-domain-split--p1
Asked directly whether a domain-driven crate split was considered instead of "everything depends on model," the answer is that it could have been done but the split happened too late in the project's life to be worth the time and energy — so the shared model crate persisted as a catch-all, kept as small as discipline allows, more by circumstance than by chosen design.
tag: tradeoff
claims: b-sb25-f012561-c2

## Question `shared-mutable-state-vs-explicit-passing`

### shared-mutable-state-vs-explicit-passing--restructure-for-explicit-ownership
Preference runs toward moving mutable state to its owning context rather than wrapping it for sharing: move state onto the owning `Session` rather than adding an internal `Mutex`; prefer no `Arc` even after conceding an immediate `Sync` bound currently requires it, wanting to revisit later; object to a `Buffer` holding an `Arc<Mutex<>>` that lets callers change encoding invisibly, wanting it passed/returned explicitly instead; and, after retracting an `Rc<RefCell<_>>` fix that still panicked on reentrant borrows, float passing a `cx` context down the stack instead, matching the rest of the codebase's existing pattern.
tag: tradeoff
claims: a-sR07-f002155-c1, a-sR07-f002155-c2, a-sa06-f003414-c2, b-sb04-f001022-c1, b-sb04-f001022-c2

### shared-mutable-state-vs-explicit-passing--shared-where-structure-demands
`Rc`/`Arc` are recommended when the program's structure makes it hard to tell how many readers a piece of data will have; `RefCell` moves borrow rules to runtime, works only single-threaded, and panics on violation, so it fits only a narrow range of problems.
tag: fact
claims: b-sT09-f005440-c1

## Question `ship-polyfill-before-spec`

### ship-polyfill-before-spec--p1
Favors shipping a "polyfill" that developers can play with today while they wait for WASI 0.3 and real async, rather than waiting for the finished standard.
tag: tradeoff
claims: b-sR03-f000889-c1

## Question `silent-fallback-vs-explicit-error`

### silent-fallback-vs-explicit-error--p1
Asks whether the code should return an error when multiple TCP sockets are listed, rather than silently using the first, since picking the first could cause odd behavior if it's the wrong one.
tag: tradeoff
claims: a-sa14-f005079-c6

### silent-fallback-vs-explicit-error--p2
Made both the multiple-socket case and the no-usable-socket case an error, reasoning it would be surprising for an explicit flag like `--systemd-listenfd` to silently fall back to the tool listening itself because of a mismatched environment variable.
tag: tradeoff
claims: a-sa14-f005079-c7

## Question `single-pass-vs-multi-pass-iteration`

### single-pass-vs-multi-pass-iteration--p1
When iterating and collecting a result only to iterate over it several more times, it's neater to collect the derived value (e.g. a per-column max) in a single pass instead.
tag: taste
claims: b-sR03-f000763-c2

## Question `single-vs-multi-threaded-executor`

### single-vs-multi-threaded-executor--p1
A multi-threaded executor can speed up workloads with many tasks by progressing several at once, but synchronizing data between tasks becomes more expensive; rather than defaulting to either model, performance should be measured for the specific application when choosing between a single- and multi-threaded runtime.
tag: fact
claims: b-bk01-f000233-c13

## Question `slint-vs-qt`

### slint-vs-qt--p1
Having reimplemented an existing QML demo app in Slint from scratch, judges Slint the best toolkit currently available for Rust — its build-time-checked, Rust-native, easily cross-compiled model is worth the tradeoff against QML's more mature multimedia/3D/testing tooling and Qt's licensing costs, especially for embedded targets.
tag: taste
claims: b-sb23-f011133-c1
