# Blind fill summaries, batch 1, file 03 of 13 (run b)

## cpp-binding-tool-choice--p1
Summary: Across bindgen/cbindgen (C-ABI-only, forcing manual unsafe conversion for anything richer), CXX (safer types but manual redeclaration and boxing since it can't see existing layouts), a hand-written IDL like Zengar (explicit layout control but a separate file that doesn't scale), and Crubit (maximum coverage via native clang+rustc integration but a clang-toolchain requirement) — no two C++-interop projects want exactly the same tradeoffs, so there may not be one interop solution to rule them all.
Tag: tradeoff
Claims: b-sb24-f011312-c1

## cpp-bindings-default-unsafe--p1
Summary: Marking every bound C++ function `unsafe` by default makes the annotation stop meaning anything — one project forked its own tooling just to turn blanket `unsafe` off entirely — so a better binding combines optional C++-side safety annotations with type-based heuristics, leaving `unsafe` visible only on genuinely dangerous APIs.
Tag: tradeoff
Claims: b-sb24-f011312-c2

## cpp-mutable-reference-representation--p1
Summary: Raw pointers force every reference-taking method, including plain method calls through `self`, to be unsafe, and `Cell` assumes invariants (safe projection through `Option`/`Vec`, `Sync`-safety) that C++ references simply don't guarantee; none of the existing approaches are good enough, so the preferred fix is a new, native C++-style reference type in Rust — one where only mutation that could invalidate the reference is unsafe — which needs compiler features (generalized field projection, custom auto-referencing) that don't exist yet.
Tag: tradeoff
Claims: b-sb24-f011312-c3

## crate-maintenance-signaling--new-deprecate-mechanism
Summary: Yank is too alarmist and breaking for signaling a crate or version shouldn't be used; what's wanted is a dedicated command like `cargo deprecate <pkg>[@range] -m <reason>` that marks specific version ranges with a reason, without forcing a break — something the existing whole-crate maintenance badge cannot do since it can't target individual problematic versions.
Tag: tradeoff
Claims: b-sb23-f009334-c1, b-sb23-f009334-c4

## crate-maintenance-signaling--existing-tools-suffice
Summary: The `badges.maintenance.status` field in Cargo.toml, already rendered by lib.rs, already solves whole-crate deprecation signaling, and for the genuinely serious case — a version with a real security vulnerability — outright yanking is proportionate, not "too alarmist" as its critics claim.
Tag: tradeoff
Claims: b-sb23-f009334-c3, b-sb23-f009334-c5

## crate-maintenance-signaling--status-auto-decays
Summary: A status marked once and never revisited stops reflecting reality; the system doesn't work if the maintenance information isn't kept up to date, which argues for a status that decays automatically rather than staying wherever an author last set it.
Tag: fact
Claims: b-sb23-f009334-c6

## crate-maintenance-signaling--status-opt-in-only
Summary: Modeled on opt-in "last seen online" indicators, a crate's maintenance status should be something an author affirmatively opts into setting and can change later, never forced or auto-decayed, and any reminder emails should likewise be a separate, one-time opt-in per person — with an author's affirmative "this is fine" mark seen as useful precisely because most old, untouched crates on crates.io are abandonware and users need a way to tell the rare exceptions apart.
Tag: tradeoff
Claims: b-sb23-f009334-c7, b-sb23-f009334-c2

## crdt-vs-coordination--p1
Summary: "Convergence without coordination" — CRDTs, formalized in 2011, have been the center of this collaborative-editor's work for a decade, letting the same shared document be edited by people and agents on different continents at once with no locking, operational-transform, or authoritative-server step required.
Tag: tradeoff
Claims: b-sR11-f005071-c1

## current-thread-runtime-for-blocking--p1
Summary: A warning against ever using Tokio's single-threaded runtime except when no OS threads are available is disputed directly: if the goal is N:1 scheduling of async tasks rather than M:N, the single-threaded runtime is the right tool for that job, even though combining it with a blocking syscall on that same thread is unusual.
Tag: tradeoff
Claims: b-sb18-f005307-c3

## custom-allocator-restart-persistence--p1
Summary: Stitching together systemd's file-descriptor store, `memfd_create`, and a custom Rust `Allocator` lets an object's backing memory survive a `systemctl restart` directly, offered as an alternative to the more conventional practice of serializing state out to Redis or a temp file on shutdown and reloading it on startup.
Tag: fact
Claims: b-sb19-f005836-c1

## custom-bytes-type-vs-vec-u8--p1
Summary: Owned buffer types at a storage API boundary should use a custom `Bytes` wrapper rather than `Vec<u8>`, while borrowed `&[u8]`/`&mut [u8]` stay as they are, specifically so a future backend-managed allocation strategy (such as pinned GPU memory) can be substituted underneath without changing the API.
Tag: tradeoff
Claims: b-sR08-f003587-c3

## custom-wasm-target-vs-wasi--p1
Summary: Porting an existing program to WASI would mean touching every `std::os::unix` call site, dropping thread usage entirely since wasip3's cooperative threading isn't yet supported by std or tokio, and losing the ability to shell out to other tools; since the sandbox's own kernel already solves filesystem, networking, subprocesses and real per-thread parallelism, writing a custom Rust compilation target skips that porting work entirely rather than accepting those losses.
Tag: fact
Claims: b-sb22-f009062-c1

## debug-assert-vs-infallible--p1
Summary: A `debug_assert!` documents and actually tests an assumption in the code, which is valued directly; agreeing to see it removed in favor of infallible code is conditioned specifically on the replacement bringing enough test coverage to keep testing the same ground, not on debug_assert being wrong in principle.
Tag: tradeoff
Claims: b-sb04-f001392-c3

## debug-assert-vs-infallible--p2
Summary: `debug_assert!` in a library is disliked outright because when the assumption turns out wrong, it surfaces as a panic in the library's users' users — reportable and fixable only through a coordinated release across projects — so the code should instead be rewritten so the assumption can never be violated at all.
Tag: tradeoff
Claims: b-sb04-f001392-c4

## dedicated-design-vs-duplicate-now--p1
Summary: A new but closely related format should get its own dedicated, decoupled implementation from the start — a separate recorder type with its own configurable adapter — rather than being bolted onto the existing format's code.
Tag: tradeoff
Claims: b-sb09-f002567-c1

## dedicated-design-vs-duplicate-now--p2
Summary: Copying the existing, similar format's implementation wholesale as a starting base, with cleanup planned for later, is how the new format's support actually got built.
Tag: tradeoff
Claims: b-sb09-f002567-c2

## dedicated-design-vs-duplicate-now--p3
Summary: Merging a large amount of duplicated test and example code with only an intention to fix it eventually is objected to given the size of the change, and once the two formats' documentation sections turn out to be nearly identical, whether keeping them as two separate sections adds any real value at all is questioned.
Tag: tradeoff
Claims: b-sb09-f002567-c4, b-sb09-f002567-c3

## dedicated-design-vs-duplicate-now--p4
Summary: After discussing it directly, the two near-identical documentation sections are kept separate — same format and language, but two sections rather than one merged one — because for now that is simply the easier path.
Tag: taste
Claims: b-sb09-f002567-c5

## dedicated-methods-vs-manual-composition--p1
Summary: There is no dedicated method for a composed operation like append-or-prepend-rotation, because a specific method for it would give no performance benefit over building the transformation and composing it manually.
Tag: fact
Claims: a-sB01-f000217-c5

## dedicated-test-for-overlapping-case--p1
Summary: Even where a new feature's code path largely overlaps existing, more general behavior, a reviewer still asks the author to add a test making sure the new case specifically works.
Tag: taste
Claims: a-sR01-f000538-c2

## dedicated-test-for-overlapping-case--p2
Summary: A dedicated test for the new feature's overlap case is questioned as redundant, since the behavior in question is supposed to already be exercised by more general tests that aren't specific to the new feature at all.
Tag: taste
Claims: a-sR01-f000538-c3

## dedupe-transitive-dependency-versions--p1
Summary: Upgrading a core dependency was valued specifically because it let the project drop duplicated copies of shared transitive dependencies, shrinking its overall dependency footprint as a direct, named benefit of the upgrade.
Tag: fact
Claims: a-sR05-f001981-c2

## default-features-minimal-vs-inclusive--minimal-defaults
Summary: You should be able to compile in only what you're actually using — demonstrated by shipping with roughly a third of a comparable project's dependency count, achieved by enabling only 4 of 20 available image codecs by default and making SVG and networking support opt-in per deployment rather than bundled by default.
Tag: tradeoff
Claims: b-sb25-f011435-c2

## default-features-minimal-vs-inclusive--inclusive-defaults
Summary: Weighing pushback that a niche format shouldn't ship as a default, the path of least friction is preferred for now — leave it enabled — with the explicit understanding that defaults can be changed later rather than pre-curated by popularity up front.
Tag: taste
Claims: a-sa02-f002127-c1

## default-features-minimal-vs-inclusive--unresolved-reported
Summary: Whether a heap-profiling feature should ship on by default is left as an open, ongoing discussion in the project's own issue tracker, with the current default being off and readers pointed to the discussion rather than told an answer.
Tag: taste
Claims: a-sa26-f011684-c1

## defensive-guards-for-unlikely-failures--p1
Summary: A resource-leak path is judged as a problem only in theory, one that may never actually occur in practice, and an RAII (`Drop`-based) guard is added for it anyway rather than left unhandled, treating the theoretical correctness gap as worth closing.
Tag: taste
Claims: a-sR14-f007341-c1

## defer-multithreaded-encoding--p1
Summary: Whether to wait on a shared lock with a timeout under multithreaded access is a real decision with a real failure mode (deadlocks), and it's fine to delay making that decision until the current single-threaded implementation has proven its worth, since multithreaded encoding doesn't yet show much benefit.
Tag: tradeoff
Claims: b-sb03-f000569-c1

## depend-vs-hand-roll--take-the-dependency
Summary: An existing, tested crate is preferred over hand-rolling: a safe-wrapper crate replaces manual syscall handling piece by piece, a well-tested (miri- and loom-covered) intrusive-list crate is kept over vendoring the data structures in-tree, and a persistent-data-structures crate is reached for over hand-rolling a segment tree specifically for its clean API and correct results.
Tag: tradeoff
Claims: a-sa14-f005079-c4, a-sa04-f002865-c1, a-02-f001053-c1

## depend-vs-hand-roll--hand-roll-or-vendor
Summary: The Rust vendor-SDK ecosystem is weak enough across several major cloud providers that a team builds and maintains its own small internal SDKs instead; the same instinct shows up as resisting a new dependency for something as foundational as an executor's core data structures, preferring them self-contained and in-tree so they can change without cross-repo coordination, and as asking whether a thin crate implementing a stable external protocol could simply be vendored directly.
Tag: tradeoff
Claims: a-saL2-f011092-c3, a-sa04-f002865-c2, a-sa14-f005079-c3

## depend-vs-hand-roll--minimize-footprint
Summary: A large new dependency tree's `cargo vet` audit burden is called excessive on its own; separately, a widely-used library accepts uglier resulting code and a project spends whole release cycles cutting dependencies ahead of a 1.0 API, in both cases treating a smaller dependency footprint as worth the cost in code quality or breaking changes.
Tag: tradeoff
Claims: a-sR06-f002016-c1, b-sR03-f001160-c1, b-sR05-f002453-c1

## dependency-upgrade-regression-handling--p1
Summary: Among pinning the older broken version, shipping with the new regression, or holding the release, a version that always crashes on exit is treated as categorically off the table; the preferred path is a narrower, soft-guardrail fix that steers users away from the one path that still regresses.
Tag: tradeoff
Claims: b-sR04-f001749-c2

## dependency-version-requirement-width--p1
Summary: A crate's `serde` requirement blocking an otherwise-portable example is grounds to loosen that requirement to `^1`, favoring compatibility with older `serde` versions already in a downstream project's tree.
Tag: taste
Claims: b-sT05-f003044-c2

## deprecate-gradually-vs-break--p1
Summary: A legacy compatibility shim starts printing deprecation warnings and gets dropped from new examples in the docs, but existing components built on it keep running unbroken — explicitly framed as the start of a gradual, managed deprecation rather than a break.
Tag: tradeoff
Claims: b-sR11-f005050-c2

## deref-delegation-vs-accessors--p1
Summary: A `Deref`-based grouping that let one type's methods be called directly on another is removed in favor of an explicit accessor method, stated as a breaking change made so the delegated-to module can "stand on its own."
Tag: taste
Claims: b-sT04-f001890-c1

## derive-arithmetic-ops--support-fieldwise-derive
Summary: Hand-writing (or reaching for `derive_more` for) trivial field-wise `Add`/`Sub`/`Mul`/`Div` on structs where field-wise operation is obviously the only sensible behavior is needless busywork; std should support deriving these the same way it already does `Clone`, `Debug` and `Copy`, and the existence of `derive_more`'s own arithmetic derives is offered as evidence of real, existing demand for exactly this.
Tag: tradeoff
Claims: a-sa19-f009292-c1, b-sb22-f009292-c1, b-sb22-f009292-c4

## derive-arithmetic-ops--oppose-semantics-ambiguous
Summary: Field-wise projection of arithmetic operators is disputed as broadly correct at all: languages with parametric polymorphism can't easily do it, most wrapper types that actually need arithmetic (complex numbers, quaternions, matrices) have their own non-field-wise rules, there is no single right answer even for simple newtypes, and affine-space math shows plainly that adding two points (two geographic coordinates, two `Instant`s) is meaningless even though point-minus-point or point-plus-translation is fine — so a naive derive would often just be wrong.
Tag: fact
Claims: b-sb22-f009292-c2, a-sa19-f009292-c2, a-sa19-f009292-c4, a-sa19-f009292-c3, b-sb22-f009292-c3

## derive-arithmetic-ops--prefer-delegation-mechanism
Summary: A basic field-wise arithmetic derive can only encode one relationship between fields, so it can never generalize to matrices, quaternions or complex numbers; a delegation syntax or a generalized derive-construction macro would solve the underlying need better than a narrow, fixed derive.
Tag: tradeoff
Claims: a-sa19-f009292-c5

## derive-arithmetic-ops--ecosystem-crates-suffice
Summary: `derive_more` already covers field-wise arithmetic derives well, and the core language and std should stay minimal, leaving conveniences like this to libraries — which is exactly the point of having a package manager in the first place.
Tag: taste
Claims: a-sa19-f009292-c6

## desktop-webview-ipc-vs-single-context--p1
Summary: Half the point of Rust is the bugs it catches at compile time, and an IPC boundary that just tosses untyped strings and values around at runtime — where a host-side field rename fails only at runtime instead of at compile time — throws that benefit away, to the point of "genuinely hating" an architecture built that way.
Tag: tradeoff
Claims: b-sb21-f008390-c1

## divergent-signature-for-forever-tasks--p1
Summary: A task meant to run forever should use the `-> !` divergent signature, because it grants the task a `'static` context and `'static` local-resource lifetimes and makes the "this never returns" intent explicit rather than implicit in an ordinary returning signature.
Tag: fact
Claims: a-sB04-f000227-c3

## docs-as-rust-vs-markdown--p1
Summary: Rewriting the documentation site's content as Rust source instead of an MDX-like format buys compile-time-validated doc links that go through the site's own router, plus data-as-code deduplication across documentation versions, offered as the concrete payoff for leaving Markdown-adjacent authoring.
Tag: tradeoff
Claims: b-sb14-f004399-c1

## docs-as-rust-vs-markdown--p2
Summary: Writing a blog post or doc page directly as this Rust DSL is not wanted; the author would rather write the Markdown it came from, since ordinary editor and language tooling understands Markdown and does not understand the DSL — a concern serious enough that the case for keeping the Rust-source approach is conceded and researching how to preserve Markdown-based authoring is agreed to.
Tag: tradeoff
Claims: b-sb14-f004399-c2, b-sb14-f004399-c3

## docs-as-rust-vs-markdown--p3
Summary: After researching MDX-capable crates, the resolution lands on downgrading all docs content to plain Markdown files and inventing a custom comment-delimiter convention of the project's own for embedding interactive components, rather than keeping content as Rust source or full MDX.
Tag: taste
Claims: b-sb14-f004399-c4
