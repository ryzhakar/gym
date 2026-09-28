# Blind fill B, batch 1, file 08 — Position summaries

## middleware-hook-vs-typestate--p1 — Typestate explicit preferred over middleware
Advocates hold that a web framework should omit a generic per-request middleware hook and instead force handlers to obtain capabilities like authorization only by calling through the relevant subsystem (e.g. an `Authorization` value obtainable only via a `User` from authentication). They value this because it removes the class of subtle ordering/dependency bugs associated with Rails-style before/after/around middleware — there is no way to call a handler without having gone through the required steps in the required order.
Tag: tradeoff
Claims: a-saL1-f005454-c4

## minimal-vs-batteries-std--p1 — Rust targets medium not minimal
Advocates state plainly that Rust's stdlib was never meant to be minimal; the design target was explicitly "medium sized," not the smallest possible core.
Tag: fact
Claims: a-sa28-f012469-c3

## minimal-vs-batteries-std--p2 — Stdlib is not batteries included
Advocates frame Rust's stdlib philosophy as the direct opposite of Python's "batteries included" approach — summarized as "buy your own damn batteries."
Tag: fact
Claims: a-sa28-f012469-c4

## missing-asset-build-fail-vs-runtime-degrade--p1 — Fail the build
Advocates hold that an option letting the build succeed and then serve a 404 at request time is a bad default, because it converts what should be a build-time problem into a silent runtime one.
Tag: tradeoff
Claims: b-sR10-f004706-c1

## missing-context-default-vs-surface--p1 — Silent default workaround
Advocates propose patching the framework so a missing context falls back to a default value (`unwrap_or_default()`), as a practical workaround for callers not using that context, avoiding an outright panic.
Tag: tradeoff
Claims: b-sb03-f000669-c1

## missing-context-default-vs-surface--p2 — Surface and fix root cause
Advocates worry that defaulting silently "mostly hides the problem rather than fixing it," since a server function that actually needs to set the context would silently fail to have its effect applied; they prefer finding and fixing the real cause (here, a disposed Runtime).
Tag: tradeoff
Claims: b-sb03-f000669-c2

## ml-dataset-eager-vs-lazy--p1 — Current eager in-memory materialization is inadequate for large datasets, unresolved
Advocates note that the existing dataset constructor path ultimately builds an in-memory dataset, which maintainers themselves flag as potentially problematic for large images or datasets — without yet having identified a fix.
Tag: fact
Claims: a-sa03-f002243-c1

## modulo-vs-branch-wraparound--p1 — Branch unrolled (chosen)
Advocates hold that in the hot loop's common (non-edge) case, modulo-based wraparound costs a `div` instruction; replacing it with if-branches for edge cases and a manually unrolled loop lets the CPU's branch predictor handle it instead, measured at a 7.61x speedup.
Tag: tradeoff
Claims: a-sB02-f000256-c5

## multiple-algorithms-autotune--p1 — Ship multiple algorithms and autotune
Advocates add autotuning infrastructure plus a second, faster `im2col`-based algorithm alongside the existing "direct" one, explicitly accepting that the new path costs more memory in exchange for significant speedups.
Tag: tradeoff
Claims: b-sR05-f002048-c1

## multitenant-resource-allocation--p1 — Dynamic system-wide throttling over static per-tenant reservation
Advocates measure utilization across the entire system rather than reserving resources per tenant, and throttle an individual heavy tenant before throttling everyone else, accepting that a compute-intensive tenant may sometimes get lower throughput than dedicated hardware would give it.
Tag: tradeoff
Claims: a-saL2-f011092-c4

## multitenant-shared-readonly-pages--p1 — Share read-only memory pages across tenants, mitigate side-channels via defense-in-depth
Advocates share memory pages across tenants only when they are entirely read-only and unmodifiable (e.g. a JS engine's read-only heap), and explicitly do not rely on a single security layer — they avoid exposing high-resolution timers specifically to block timing/Spectre-style side-channel attacks, layering this on top of other sandbox measures.
Tag: tradeoff
Claims: a-saL2-f011092-c2

## mutex-vs-atomics--atomics-over-locks — Avoid locks; prefer atomics
Advocates argue atomics and compare-and-swap are fine — worst case is livelock, which is rare and usually recovers — while a lock is "always a disaster waiting to happen" because something will eventually die holding it and the whole system grinds to a halt; one advocate goes as far as calling the mere existence of a lock, even inside a library, always a programming bug. In practice, advocates reject mutex-guarded shared state (e.g. a shared iterator for ID generation) in favor of lock-free constructs (atomics, `RoaringBitmap::select`) that let threads proceed without synchronization.
Tag: taste
Claims: b-sb18-f005600-c1, a-sa17-f007846-c1

## mutex-vs-atomics--atomics-carry-own-bugs — Atomics carry their own bug class
Advocates push back on framing atomics/CAS as the safe alternative, pointing out that races — stale or inconsistent reads — are themselves a real bug class, not a lesser evil than locking.
Tag: taste
Claims: b-sb18-f005600-c2

## mutex-vs-atomics--mutex-unless-contended — Plain mutexes unless contention is high
Advocates offer an explicit decision rule: with many threads and heavy lock contention, move to lock-free data structures (e.g. crossbeam, parking_lot); if a lock is rarely contended, a normal mutex-based structure is simpler and just as good, since lock-free implementations bring their own hazards (e.g. the ABA problem).
Tag: tradeoff
Claims: b-sb23-f011233-c2

## nalgebra-typed-api-vs-glm--p1 — Nalgebra for rigor and dynamically-sized cases; nalgebra-glm for simplicity
Advocates (the library's own maintainers) frame the choice as depending on taste and background: nalgebra for those who prefer rigorous, type-level-restricted treatments of transformations and for dynamically-sized matrices, nalgebra-glm for those coming from C++ GLM or wanting more straightforward functions.
Tag: taste
Claims: a-sB01-f000217-c1

## named-default-args-overloading--reject-all-for-simplicity — Reject all
Advocates have for years opposed Rust adding named parameters, optional/default arguments, and function overloading — all requested since at least a twelve-year-old GitHub issue — arguing the features are numerous and mutually entangled, and that Rust's current rule (one function, one signature; write a differently-named function or a builder for variants) keeps the language simple at an acceptable cost.
Tag: taste
Claims: a-sa18-f009104-c1

## named-default-args-overloading--named-parameters-only — Named parameters only
Advocates have become open specifically to named parameters, while still opposing optional/default arguments and overloading, and while flagging unresolved language-design problems the proposal would need to solve: parameters are patterns not names, function values erase parameter names, left-to-right evaluation order conflicts with letting call sites reorder named arguments, and renaming a parameter becomes a breaking change.
Tag: tradeoff
Claims: a-sa18-f009104-c2

## named-default-args-overloading--overloading-for-interop — Overloading, at least for interop
Advocates hold that Rust should support built-in overloading today, especially for interop with existing languages, noting C++ API maintainers rely on adding overloads without breaking existing callers, that Rust already fakes overloading inconsistently via trait dispatch (multiple `From` impls, `Into`'s return-type-directed dispatch), and that built-in overloading could also resolve an aliasing problem by letting the compiler pick a safe vs. unsafe overload based on the caller's reference.
Tag: tradeoff
Claims: b-sb24-f011312-c6

## narrating-comments--p1 — No narrating comments
Advocates flag comments and doc comments that merely narrate what a simple, self-evident line or private helper does — a repeating pattern across a file — and hold that removing them all is better than keeping or improving them; when asked, they comply by stripping such comments across the touched files.
Tag: taste
Claims: a-sa13-f004772-c5, a-sa13-f004772-c6

## networking-lib-core-scope--minimal-core-pluggable — Minimal core, pluggable trait extensions
Advocates deliberately shrink the library's default scope — disabling higher-level sync features by default and reframing them as separate protocols layered on the core networking primitive — and decline to build every candidate transport (WebTransport, Bluetooth, Tor, InfiniBand, ...) into the core, since doing so would create a maze of feature flags and drag in dependencies most users don't need; instead they expose extension traits (`CustomTransport`/`CustomEndpoint`/`CustomSender`) for users to plug in only what they need.
Tag: tradeoff
Claims: a-sa02-f002124-c1, a-sR11-f004170-c1

## new-features-on-old-editions--p1 — Extend back until first interaction
Advocates argue the reason Rust uses editions rather than fine-grained feature flags is to avoid a combinatoric explosion of untested feature/rule interactions — not a default rule that all new features are edition-gated. A feature should therefore be made available on older editions up until the point it actually interacts with something that changed in a later edition; needing to go back and modify an edition migration to work differently would signal the feature was pushed too far back.
Tag: fact
Claims: a-sa20-f009698-c1

## new-type-vs-option-for-variant--p1 — Extend via option
Advocates reject adding a new dedicated type for the requested capability variant and instead propose an argument/option on the existing type.
Tag: taste
Claims: b-sb09-f002567-c6

## nextest-vs-custom-runner--p1 — Custom test-runner wrapper over cargo-nextest
Advocates built a custom wrapper around `cargo test` — building test binaries on one machine, shipping them to others as a zip, sharding execution, and converting cargo's unstable JSON test output into JUnit XML — after trying cargo-nextest first and rejecting it, because nextest's different (parallel-process) execution model broke an existing test-suite assumption (a global mutex handing out network ports one at a time), and fixing that assumption would have cost more time than they had.
Tag: tradeoff
Claims: a-saL2-f011092-c1

## nightly-feature-autodetection--p1 — Nightly features must be explicit opt in
Advocates hold that unstable features should only affect those who opted in, and that libraries or build probes auto-detecting and using nightly features by default runs counter to that principle; they want to use a nightly compiler for unrelated reasons (debug flags, toolchain ergonomics) without their dependencies implicitly gaining access to other unstable features they never consented to.
Tag: fact
Claims: a-sa19-f009343-c3, a-sa19-f009343-c4, a-sa19-f009343-c5, a-sa19-f009343-c6

## nightly-feature-autodetection--p2 — Build probes should default to detecting and using nightly features
Advocates, as ergonomics-motivated developers, prefer a crate that documents clearly when it auto-detects and uses nightly features over one that requires going through manual opt-in flags, while acknowledging that safety-critical users need a documented way to fully opt out.
Tag: taste
Claims: a-sa19-f009343-c7

## nightly-gate-feature-vs-cfg--p1 — Rustflags cfg gate
Advocates gate unstable-feature code with a `--cfg` flag set through `RUSTFLAGS` rather than a Cargo feature, because a Cargo feature gets force-enabled by a "test with all features enabled" CI job even when the compiler in use is stable; this also lets a PR land — checked only by a dedicated nightly `cargo check` job — ahead of the corresponding upstream compiler support existing.
Tag: tradeoff
Claims: b-sb06-f002033-c1

## nightly-in-production--stable-only — Stable only
Advocates state plainly that their project does not, has not, and does not plan to rely on unstable Rust features, and that all their foundational crates are published to crates.io with no unpublished dependencies.
Tag: taste
Claims: a-saL2-f011092-c5

## nightly-in-production--nightly-when-it-pays — Nightly when its safety and ergonomics pay (portable SIMD)
Advocates contrast writing raw, target-feature-gated intrinsics — unsafe, verbose, requiring manual wrapping and runtime feature detection — with `portable_simd`, which lets you write safe, ordinary-looking iterator code that the compiler lowers to the right instructions per architecture; they recommend it as "the choice" even though it currently requires nightly.
Tag: tradeoff
Claims: b-sb23-f011233-c3

## no-std-for-wasm--p1 — No_std is embedded-only, not needed for wasm
Advocates explicitly correct the assumption that compiling to WebAssembly requires disabling the standard library — that step, they state, is necessary only for embedded targets, not for browser/wasm targets.
Tag: fact
Claims: a-sB01-f000217-c4

## non-exhaustive-by-default--non-exhaustive-by-default — Yes
Advocates mark newly public or changed enums and structs `#[non_exhaustive]` — including a `TransportAddr` replacing a prior type, and types like `PathEvent` and `IncomingLocalAddr` — specifically so that future variants (e.g. from planned custom transports such as Bluetooth or WebRTC) can be added later without a breaking API change, requiring callers to add a wildcard match arm.
Tag: tradeoff
Claims: a-sT08-f004169-c2, a-sR13-f004685-c3, a-sR13-f004586-c2

## nonnull-in-ffi-params--p1 — Avoid runtime null check
Advocates deliberately avoid taking `NonNull<T>` as a parameter in an FFI/atomic-pointer API specifically to avoid adding a runtime null check.
Tag: tradeoff
Claims: a-02-f000977-c1

## object-graph-representation--indices-or-handles — Indices into an arena, or a separate handle domain, for object graphs
Advocates hold that keeping objects in a `Vec` and referring to each other by `usize` index avoids both `Rc<RefCell<T>>`'s reference-cycle leaks and runtime borrow panics, and raw/unsafe pointers' aliasing and undefined-behavior risk — turning aliasing bugs into compiler errors and serializing/parallelizing cleanly with `serde`/`rayon`. For embedding a scripting language into a game, one advocate similarly pictures pairing an ECS-ish API on the Rust side with an OO-ish API on the guest side, joined through handles, though without having built this out to prove it works.
Tag: tradeoff
Claims: b-sb26-f013214-c5, b-sb20-f007608-c1

## one-enum-vs-two-types--p1 — Split into two structs
Advocates find an enum-based accessor confusing when traversing relations dynamically and suggest splitting it into two separate structs plus friendlier wrapper methods.
Tag: taste
Claims: a-sa07-f003716-c3

## oop-patterns-in-rust--p1 — Factories are rarely idiomatic in rust
Advocates redirect away from the Abstract Factory pattern toward generics (e.g. `Rc<E>`), framing factories as a pattern rarely used in Rust.
Tag: taste
Claims: a-sa30-f013276-c6

## opt-level-z-vs-s--p2 — Never assume opt-level="z" beats opt-level="s" for binary size, measure both
Advocates note that, surprisingly, `opt-level = "s"` can sometimes produce smaller binaries than the more aggressive `opt-level = "z"`, so the choice should always be measured rather than assumed.
Tag: fact
Claims: b-bk02-f000256-c10, a-sB02-f000256-c7
Note: p1 ("Measure both, recommended") and p2 read as the same position stated twice; both Claims here are the identical quote from the same source. Flagging for merge rather than resolving myself.

## optional-parameters-api-shape--one-configurable-entry — One entry point (Config struct, _with_opts, enum discriminant, option on existing type)
Advocates route optional/variant behavior through one configurable entry point rather than multiplying methods: an enum discriminant passed as a second constructor argument instead of one method per variant; everything that is part of a config struct routed through that struct rather than also exposed as a separate public method; and an `_with_opts` method taking an Options struct (plus `impl Into<T>` convenience wrappers), reasoned as the closest available mapping given Rust has neither overloading nor default parameters.
Tag: tradeoff
Claims: a-01-f000530-c2, b-sb05-f001512-c3, b-sb10-f003222-c2

## optional-parameters-api-shape--separate-specialized-entries — Separate specialized functions or primitives
Advocates propose one explicitly-named method per source type and color space so the target is always visible at the call site rather than inferred from context, and separately flag that merging into a single function would force passing four arguments at every call site, at a cost to readability.
Tag: tradeoff
Claims: a-01-f000530-c1, a-sa06-f003414-c4

## optional-parameters-api-shape--drop-feature-keep-signature-small — Drop the feature to keep the signature small
Advocates are willing to merge a first version of the work without an extra feature (automatic BOM/encoding detection), choosing fewer arguments over including it.
Tag: taste
Claims: a-sa06-f003414-c5

## optional-parameters-api-shape--many-constructors-criticized — Many constructors (status quo, criticized)
Advocates flag that the proliferation of constructors, without enough documentation, makes the API hard to understand.
Tag: tradeoff
Claims: b-sb05-f001512-c4

## oss-framework-monetization--fully-open — Fully open, paid layer alongside or donate permissively
Advocates donate libraries and examples to a project's community working group under an open-source license, framing this as consistent with being long-time open-source advocates; separately, advocates build a paid cloud layer alongside a fully-capable free/local plan, envisioning a business model based on adding complementary value rather than restricting core features behind a paywall.
Tag: taste
Claims: b-sT05-f002775-c1, a-sa09-f004016-c1

## oss-reuse-attribution-norms--coordination-and-credit-matter — Coordination and credit matter
Advocates hold that copying, stripping, and renaming another project's code, or "debranding" it, without reaching out or discussing it first, is disrespectful of the original authors' investment and "bad form," even where the license permits it, because a project's name and brand carry the social and financial capital that sustains its maintainers; when copying is found without credit, advocates ask for it to be added, and the copier concedes and adds attribution (including a co-authored-by line) after the fact.
Tag: taste
Claims: a-sa05-f003025-c8, a-sa05-f003025-c6, a-sa13-f004772-c7, a-sa13-f004772-c8

## oss-reuse-attribution-norms--no-entitlement — No entitlement to control reuse
Advocates hold that producers of open source are not entitled to anything regarding how their code is reused or rebranded, just as consumers aren't entitled to anything from producers — framing forking and reuse without prior coordination as "the real beauty of open source: a gift with no expectations."
Tag: taste
Claims: a-sa05-f003025-c7
