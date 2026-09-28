# Blind fill A — summaries, batch 1, file 03

### cpp-binding-tool-choice--p1
Summary: No single tool fits everyone binding a large C++ API surface to Rust — bindgen/cbindgen only handle C-ABI-compatible functions, forcing manual unsafe conversion for RAII/generic/user-defined types; CXX adds safer higher-level types but needs items manually redeclared and boxed since it can't see existing memory layout; a hand-written IDL ("Zengar") allows passing by value with explicit layout but requires a separate file that doesn't scale to huge surfaces; and native compiler integration (Crubit) gets maximum coverage but requires a clang toolchain not every project can use — because no two C++-interop projects want exactly the same thing.
Tag: tradeoff
Claims: b-sb24-f011312-c1

### cpp-bindings-default-unsafe--p1
Summary: Marking every bound C++ function `unsafe` by default makes the annotation meaningless — one project forked its own tool just to turn `unsafe` off entirely — so the better approach combines optional C++-side safety annotations with type-based heuristics, leaving `unsafe` visible only on genuinely dangerous APIs.
Tag: tradeoff
Claims: b-sb24-f011312-c2

### cpp-mutable-reference-representation--p1
Summary: None of the existing options for representing non-exclusive C++ mutable references in Rust are satisfying: raw pointers force every reference-taking method call to be unsafe, and `Cell` assumes invariants C++ references don't actually provide (safe projection through `Option`/`Vec`, `Sync`-safety for thread-safe C++ types); the better answer is a new C++-style reference type native to Rust, where only mutation that could invalidate a reference is unsafe — but this needs compiler features (generalized field projection, auto-referencing for custom reference types) that don't exist yet.
Tag: tradeoff
Claims: b-sb24-f011312-c3

### crate-maintenance-signaling--existing-tools-suffice
Summary: The tools crates.io already has are enough: the `badges.maintenance.status` field (already rendered by lib.rs) solves whole-crate deprecation signaling, and yanking remains the proportionate response when a version carries a serious vulnerability.
Tag: tradeoff
Claims: b-sb23-f009334-c3, b-sb23-f009334-c5

### crate-maintenance-signaling--new-deprecate-mechanism
Summary: A dedicated per-version deprecation mechanism is needed — yank is too alarmist and breaking for routine cases, the existing maintenance badge only covers the whole crate rather than specific problematic version ranges, and against a backdrop where the overwhelming majority of old crates turn out to be abandonware, users need a lighter, more granular way (like a `cargo deprecate <pkg>[@range] -m <reason>` command) to be warned off specific versions without a hard break.
Tag: tradeoff
Claims: b-sb23-f009334-c1, b-sb23-f009334-c2, b-sb23-f009334-c4

### crate-maintenance-signaling--status-opt-in-only
Summary: Maintenance status should be opt-in per crate and changeable later by the author, modeled on "last seen online" indicators, rather than forced on everyone; any reminder emails nudging authors to update status should likewise be a separate, one-time opt-in per person, not automatic.
Tag: taste
Claims: b-sb23-f009334-c7

### crate-maintenance-signaling--status-auto-decays
Summary: A maintenance-status signal has to decay automatically over time, because without decay a crate could be marked "maintained" once and then never revisited for years while still showing as maintained — the system doesn't work if the information isn't kept up to date.
Tag: tradeoff
Claims: b-sb23-f009334-c6

### crdt-vs-coordination--p1
Summary: Convergence for a multi-actor, human-and-agent live document should come from CRDTs rather than any coordinating or locking mechanism — CRDTs, "formalized in 2011," have been the center of this project's work for a decade and let a shared document be edited by several people and agents on different continents at once with no coordination step at all.
Tag: tradeoff
Claims: b-sR11-f005071-c1

### current-thread-runtime-for-blocking--p1
Summary: A warning against ever using Tokio's single-threaded runtime except when no OS threads are available is simply wrong: if the goal is N:1 scheduling of async tasks (rather than M:N), the single-threaded runtime is the right tool for that job, though pairing it with blocking syscalls on that same thread is unusual.
Tag: tradeoff
Claims: b-sb18-f005307-c3

### custom-allocator-restart-persistence--p1
Summary: Rust objects can be made to survive a process restart by stitching together systemd's FD store, `memfd_create`, and a custom raw-memory `Allocator`, as an alternative to the more familiar practice of serializing state out to Redis or a temp file before shutdown and reloading it on startup.
Tag: tradeoff
Claims: b-sb19-f005836-c1

### custom-bytes-type-vs-vec-u8--p1
Summary: Owned byte buffers at an API boundary where allocation strategy matters should be typed as a custom wrapper (e.g. `burn_common::Bytes`) rather than `Vec<u8>`, so that a future backend-managed allocation strategy (like pinned GPU memory) can be substituted later, while borrowed `&[u8]`/`&mut [u8]` stay as-is.
Tag: tradeoff
Claims: b-sR08-f003587-c3

### custom-wasm-target-vs-wasi--p1
Summary: To run an existing, unmodified Rust/Linux program inside a browser sandbox, define a custom, non-standard Rust compilation target tailored to the sandbox's own syscall/threading model rather than port to WASI — porting would mean touching every `std::os::unix` call site, dropping thread usage entirely (since wasip3's cooperative threading is new and unsupported by std or tokio), and losing the ability to shell out to `git`/`node`, whereas the sandbox's own kernel already solves filesystem, networking, subprocesses and real per-thread parallelism.
Tag: tradeoff
Claims: b-sb22-f009062-c1

### debug-assert-vs-infallible--p1
Summary: `debug_assert!` is valuable in a library because it actually documents and tests an assumption in the code; giving it up is only acceptable when the replacement code comes with enough tests to cover the same ground.
Tag: tradeoff
Claims: b-sb04-f001392-c3

### debug-assert-vs-infallible--p2
Summary: `debug_assert!` shouldn't be relied on in a library at all, because when the assumption turns out wrong it surfaces as a hard-to-report panic in the library's users' users, fixable only by a coordinated release across projects; the code should instead be rewritten so the assumption can never be violated even conceptually.
Tag: tradeoff
Claims: b-sb04-f001392-c4

### dedicated-design-vs-duplicate-now--p1
Summary: A new but closely related serialization format should get its own dedicated, decoupled implementation (e.g. a `SafeTensorFileRecorder` independent of the PyTorch recorder, with a configurable adapter) from the start, rather than starting from a copy of the existing similar format's code.
Tag: tradeoff
Claims: b-sb09-f002567-c1

### dedicated-design-vs-duplicate-now--p2
Summary: It's acceptable to copy an existing similar format's implementation wholesale as the starting point for the new format's support, with cleanup planned as a later step rather than done up front.
Tag: tradeoff
Claims: b-sb09-f002567-c2

### dedicated-design-vs-duplicate-now--p3
Summary: A large amount of introduced duplication — whether in code or in near-identical documentation sections — should be reduced before merge rather than merged with the intent to fix it later, since "later" risks never happening or happening even worse given the size of the change.
Tag: tradeoff
Claims: b-sb09-f002567-c4, b-sb09-f002567-c3

### dedicated-design-vs-duplicate-now--p4
Summary: After weighing it, keeping two near-duplicate doc sections (same format and language, different file recorder) separate rather than merging them is the pragmatic choice for now, even without a strong case for two sections on the merits.
Tag: tradeoff
Claims: b-sb09-f002567-c5

### dedicated-methods-vs-manual-composition--p1
Summary: An API shouldn't add a dedicated method for a composed operation like append/prepend rotation when a specific method gives no performance benefit over building the transformation and multiplying it in manually.
Tag: tradeoff
Claims: a-sB01-f000217-c5

### dedicated-test-for-overlapping-case--p1
Summary: A new macro feature's code path should get its own dedicated test even where its behavior largely overlaps existing generic tests, to make sure that specific case is confirmed working.
Tag: taste
Claims: a-sR01-f000538-c2

### dedicated-test-for-overlapping-case--p2
Summary: A dedicated test for behavior already exercised by more general, feature-independent tests is unnecessary, since the case in question (optional prop values) isn't inherent to the new feature at all.
Tag: taste
Claims: a-sR01-f000538-c3

### dedupe-transitive-dependency-versions--p1
Summary: A library should actively chase down and eliminate duplicate transitive dependency versions in its tree — upgrading a core dependency was valued specifically because it let duplicated copies of shared dependencies be dropped, shrinking the overall dependency footprint.
Tag: tradeoff
Claims: a-sR05-f001981-c2

### default-features-minimal-vs-inclusive--minimal-defaults
Summary: A crate should compile in only what's actually being used — one project's roughly 300 dependencies versus a comparable project's roughly 1,000 came in part from enabling only 4 of 20 available image codecs by default and making SVG/networking support opt-in per deployment.
Tag: tradeoff
Claims: b-sb25-f011435-c2

### default-features-minimal-vs-inclusive--inclusive-defaults
Summary: Weighing pushback that niche formats shouldn't be defaults, the path of least friction now — shipping them enabled — is preferable to pre-curating defaults by popularity, with the option to change the defaults later.
Tag: tradeoff
Claims: a-sa02-f002127-c1

### default-features-minimal-vs-inclusive--unresolved-reported
Summary: Whether an optional capability like heap profiling should be on by default is an active, ongoing discussion in the project's issue tracker, currently shipping off by default behind a feature flag, with the question left open rather than settled.
Tag: fact
Claims: a-sa26-f011684-c1

### defensive-guards-for-unlikely-failures--p1
Summary: Even a failure mode judged unlikely to ever occur in practice is worth guarding against with good old-fashioned RAII (a `Drop`-based guard), because correctness is worth the modest extra engineering even for a merely theoretical problem.
Tag: tradeoff
Claims: a-sR14-f007341-c1

### defer-multithreaded-encoding--p1
Summary: When a resource like a Metal command buffer needs coordinated access from multiple threads, it's fine to delay the decision of whether to wait on the lock with a timeout until the single-threaded implementation has proven its worth, since multithreaded encoding doesn't yet show much benefit anyway.
Tag: tradeoff
Claims: b-sb03-f000569-c1

### depend-vs-hand-roll--take-the-dependency
Summary: An existing, tested crate is often the better call than hand-rolling: a persistent-data-structure crate (`rpds`) beat a hand-rolled segment tree on API cleanliness, correctness and good-enough performance; a `rustix` safe wrapper is repeatedly proposed over raw, manual syscall handling; and an executor's internal data structure crate is defended for keeping the dependency specifically because of its miri+loom test coverage and shared maintenance with another executor.
Tag: tradeoff
Claims: a-sa14-f005079-c4, a-sa04-f002865-c1, a-02-f001053-c1

### depend-vs-hand-roll--hand-roll-or-vendor
Summary: Sometimes hand-rolling or vendoring is the better call: a weak Rust vendor-SDK ecosystem (broken S3 retry behavior, missing or dormant GCP/Azure/Stripe SDKs) pushed a team to build and maintain its own small internal "mini SDKs"; a foundational executor's data structures are kept self-contained and in-tree rather than pulled in as a dependency, so they can be changed without cross-repo coordination; and a thin crate implementing an external, rarely-changing protocol is a candidate for vendoring directly rather than depending on.
Tag: tradeoff
Claims: a-saL2-f011092-c3, a-sa04-f002865-c2, a-sa14-f005079-c3

### depend-vs-hand-roll--minimize-footprint
Summary: Minimizing a library's dependency footprint is worth uglier code, slower release cycles, or breaking changes: a new dependency tree's `cargo vet` audit burden was called excessive; a maintainer accepted uglier code specifically because reducing dependencies matters more for a widely-used library; and a project spent whole release cycles cutting dependencies ahead of its 1.0, accepting breaking changes as the cost.
Tag: tradeoff
Claims: a-sR06-f002016-c1, b-sR03-f001160-c1, b-sR05-f002453-c1

### dependency-upgrade-regression-handling--p1
Summary: A version that always crashes on exit is not an option to ship, so between shipping with that always-crash regression, pinning to the older broken version, or holding the release, the workable path is a narrower crash confined to one feature path with a guardrail steering users away from it — never a known, unconditional crash.
Tag: tradeoff
Claims: b-sR04-f001749-c2

### dependency-version-requirement-width--p1
Summary: A library's dependency version requirement (here, serde) should be loosened to `^1` for portability, since a tighter minimum blocked adding an otherwise-independent example.
Tag: tradeoff
Claims: b-sT05-f003044-c2

### deprecate-gradually-vs-break--p1
Summary: A deprecated compatibility shim should be phased out gradually with warnings and migration time rather than removed outright — a release can start printing deprecation warnings and drop the shim from examples/documentation while existing components built against it keep running.
Tag: tradeoff
Claims: b-sR11-f005050-c2

### deref-delegation-vs-accessors--p1
Summary: Delegating one type's methods to another through `Deref` should be dropped in favor of explicit accessor methods — removing a `Deref` link so a subsystem's client can "stand on its own" and callers write an explicit accessor call rather than relying on an implicit deref chain.
Tag: tradeoff
Claims: b-sT04-f001890-c1

### derive-arithmetic-ops--support-fieldwise-derive
Summary: For struct types where field-wise arithmetic is the obviously sensible behavior, hand-writing (or reaching for `derive_more` to get) `Add`/`Sub`/`Mul`/`Div` is needless busywork; std should let you `#[derive]` these traits the same way it already does `Clone`/`Debug`/`Copy`, with `derive_more`'s existing arithmetic derives cited as evidence of real, ongoing demand for exactly this.
Tag: tradeoff
Claims: a-sa19-f009292-c1, b-sb22-f009292-c1, b-sb22-f009292-c4

### derive-arithmetic-ops--oppose-semantics-ambiguous
Summary: Unconstrained field-wise arithmetic derive is rejected as semantically wrong or too narrow to be a sane default: it's unclear how often naive field-wise addition is actually correct (most wrapper structs needing arithmetic — complex numbers, quaternions, matrices — have their own non-field-wise rules), there's no single right answer even for simple newtypes (e.g. whether angle arithmetic should wrap modulo 2π), and affine-space math shows addition of points (two geographic coordinates, two `Instant`s) is often meaningless even where point-minus-point or point-plus-translation is meaningful.
Tag: fact
Claims: b-sb22-f009292-c2, a-sa19-f009292-c2, a-sa19-f009292-c4, a-sa19-f009292-c3, b-sb22-f009292-c3

### derive-arithmetic-ops--prefer-delegation-mechanism
Summary: A basic field-wise arithmetic derive can only encode one relationship between fields, so it doesn't generalize to matrices, quaternions or complex numbers; a delegation syntax or a generalized macro for constructing derives would serve the need better than a single fixed derive.
Tag: tradeoff
Claims: a-sa19-f009292-c5

### derive-arithmetic-ops--ecosystem-crates-suffice
Summary: There's no need to put arithmetic-trait derives in the core language: `derive_more` already covers this well, and it's the point of having a package manager that the core language and std stay minimal while most conveniences are left to libraries.
Tag: taste
Claims: a-sa19-f009292-c6

### desktop-webview-ipc-vs-single-context--p1
Summary: An independent frontend runtime talking to a host process over a serialized, untyped IPC boundary (command names as bare strings, arguments as `JsValue`) throws away much of Rust's compile-time-checking value — a field rename on the host side fails only at runtime instead of compile time — and combined with the architectural split, this is bad enough to make the whole design something to actively reject.
Tag: tradeoff
Claims: b-sb21-f008390-c1

### divergent-signature-for-forever-tasks--p1
Summary: A task meant to run forever should use a divergent (`-> !`) function signature rather than an ordinary returning one, because it grants a `'static` context and `'static`-lifetime local resources, making the run-forever intent explicit in the type signature itself.
Tag: tradeoff
Claims: a-sB04-f000227-c3

### docs-as-rust-vs-markdown--p1
Summary: Authoring documentation content directly as Rust source (rather than a Markdown-derivative like MDX) pays off through compile-time-validated internal and external doc links and data-as-code deduplication across doc versions.
Tag: tradeoff
Claims: b-sb14-f004399-c1

### docs-as-rust-vs-markdown--p2
Summary: Ordinary editor and language tooling understands Markdown but not a custom Rust DSL for docs; writing a blog post should stay in the format it actually came from, and it's worth researching whether Markdown-based authoring can be preserved without losing the concerns that motivated moving away from it.
Tag: taste
Claims: b-sb14-f004399-c3, b-sb14-f004399-c2

### docs-as-rust-vs-markdown--p3
Summary: After weighing the ergonomics concern, the resolution is to downgrade the docs content from MDX/Rust-source back to plain Markdown files, inventing a custom convention (comment delimiters) for embedding interactive components instead of relying on a macro-based DSL.
Tag: tradeoff
Claims: b-sb14-f004399-c4

---
Notification: Filled positions-03.csv (60 claim rows) and summaries-03.md (44 positions) for input-b1-03.md, covering questions from `cpp-binding-tool-choice` through `docs-as-rust-vs-markdown`. One low-confidence call is flagged: a `crate-maintenance-signaling` claim about abandonware base rates argues generally for a marking mechanism without specifying decay vs. opt-in, so it was mapped to the broader "new mechanism" position. All other 59 claim-to-position assignments are high confidence, judged from quote and paraphrase alone, no sources opened.
