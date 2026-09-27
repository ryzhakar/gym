# Blind fill summaries, batch 1, file 08 (run a)

## middleware-hook-vs-typestate--p1
Typestate gives a straightforward guarantee: a handler can only obtain `Authorization` by calling through the authorization subsystem, which itself only comes from a `User` obtained via authentication. No worrying about the order handlers run in, no Rails-style before/after/around ordering bugs.
tag: tradeoff
Claims: a-saL1-f005454-c4

## middleware-hook-vs-typestate--p2
Dropshot's own FAQ anticipates the question of why there's no way to add a handler that runs on every request — framed as the design most users expect from a web framework, with lessons-learned invited after a few years living without it.
tag: tradeoff
Claims: a-saL1-f005454-c5

## minimal-vs-batteries-std--p1
Rust never set out to be minimal; the target was always "medium sized," a middle point between a bare core and a fully batteries-included system.
tag: fact
Claims: a-sa28-f012469-c3

## minimal-vs-batteries-std--p2
"Buy Your Own Damn Batteries" — the stdlib's posture is the deliberate opposite of Python's "batteries included."
tag: fact
Claims: a-sa28-f012469-c4

## missing-asset-build-fail-vs-runtime-degrade--p1
An `allow_missing = true` option that lets the build succeed and then 404 at request time turns a build-time problem into a silent runtime one — a bad default.
tag: tradeoff
Claims: b-sR10-f004706-c1

## missing-context-default-vs-surface--p1
Patch leptos-axum so a missing `ResponseOptions` context resolves via `unwrap_or_default()` instead of panicking — a workaround for callers who don't touch `ResponseOptions` anyway.
tag: tradeoff
Claims: b-sb03-f000669-c1

## missing-context-default-vs-surface--p2
`unwrap_or_default()` mostly hides the problem rather than fixing it: a server function that actually sets `ResponseOptions` would silently fail to have its header/status applied. Find and fix the real cause — a disposed Runtime.
tag: tradeoff
Claims: b-sb03-f000669-c2

## ml-dataset-eager-vs-lazy--p1
`new_segmentation_with_items` builds an `InMemoryDataset` under the hood, already flagged as problematic for large images or large datasets, with no known fix yet.
tag: fact
Claims: a-sa03-f002243-c1

## modulo-vs-branch-wraparound--p1
Modulo-based wraparound costs a div instruction on the common non-edge case; replacing it with if-branches and a manually unrolled loop lets the branch predictor do the work, measured at 7.61x.
tag: fact
Claims: a-sB02-f000256-c5

## multiple-algorithms-autotune--p1
Add the infrastructure to autotune `conv2d`/`conv_transpose2d`, plus a second `im2col`-based algorithm alongside the existing "direct" one, trading memory for significant speedups.
tag: tradeoff
Claims: b-sR05-f002048-c1

## multitenant-resource-allocation--p1
Measure utilization across the whole system rather than per tenant; throttle a single heavy tenant before throttling everyone else, accepting that a compute-intensive tenant sometimes gets lower throughput than dedicated hardware would give.
tag: tradeoff
Claims: a-saL2-f011092-c4

## multitenant-shared-readonly-pages--p1
Share memory pages across tenants only when entirely read-only and unmodifiable (e.g. V8's read-only heap); don't rely on a single security layer — specifically avoid exposing high-resolution timers to block timing/Spectre-style side channels, on top of other sandbox layers.
tag: tradeoff
Claims: a-saL2-f011092-c2

## mutex-vs-atomics--mutex-unless-contended
If there are many threads and heavy lock contention, move to lock-free data structures; if a lock is rarely contended, a normal mutex is simpler and just as good — lock-free brings its own hazards like the ABA problem.
tag: tradeoff
Claims: b-sb23-f011233-c2

## mutex-vs-atomics--atomics-carry-own-bugs
Framing atomics/CAS as the safe alternative glosses over the fact that races — stale or inconsistent reads — are themselves a real bug class, not a lesser evil.
tag: tradeoff
Claims: b-sb18-f005600-c2

## mutex-vs-atomics--atomics-over-locks
Atomics and compare-and-swap are fine — worst case a rare, recoverable livelock. A lock is a disaster waiting to happen: something dies holding it and the whole system grinds to a halt. The existence of a lock, even inside a library, is always a programming bug.
tag: taste
Claims: b-sb18-f005600-c1, a-sa17-f007846-c1

## nalgebra-typed-api-vs-glm--p1
Prefer nalgebra's rigorous, type-level-restricted transforms; reach for nalgebra-glm if coming from C++ GLM or wanting more straightforward functions.
tag: taste
Claims: a-sB01-f000217-c1

## named-default-args-overloading--overloading-for-interop
Rust should support built-in overloading, especially for interop with existing languages; it already fakes overloading via trait dispatch inconsistently, and real overloading would also let the compiler pick a safe vs. unsafe overload based on the caller's reference.
tag: tradeoff
Claims: b-sb24-f011312-c6

## named-default-args-overloading--reject-all-for-simplicity
Named parameters, optional/default arguments and overloading are numerous and mutually entangled; the current rule — one function, one signature, write a differently-named function or a builder for variants — keeps Rust simple at an acceptable cost.
tag: tradeoff
Claims: a-sa18-f009104-c1

## named-default-args-overloading--named-parameters-only
Named parameters could work for Rust; optional or default arguments still shouldn't, and unresolved design problems remain — parameters are patterns not names, function-values erase parameter names, and reordering call-site arguments conflicts with left-to-right evaluation order.
tag: tradeoff
Claims: a-sa18-f009104-c2

## narrating-comments--p1
Doc comments narrating one-line private helpers repeat the same pattern across a file; removing them all is better than keeping or improving them, so strip the narrating comments.
tag: taste
Claims: a-sa13-f004772-c6, a-sa13-f004772-c5

## networking-lib-core-scope--minimal-core-pluggable
The networking stack is "what iroh is"; everything else is a custom protocol layered on top. Adding every candidate transport into the core would make the code a maze of feature flags and drag in dependencies most users don't need, so `CustomTransport`/`CustomEndpoint`/`CustomSender` traits let users plug in only what they need.
tag: tradeoff
Claims: a-sa02-f002124-c1, a-sR11-f004170-c1

## new-features-on-old-editions--p1
Editions exist to avoid a combinatoric explosion of untested feature/rule interactions, not to gate every new capability by default. A feature should be available on older editions until the point it interacts with something that changed later; needing to modify an edition migration afterward signals the feature was pushed too far back.
tag: tradeoff
Claims: a-sa20-f009698-c1

## new-type-vs-option-for-variant--p1
No new recorder type needed for byte-based loading — an argument/option on the existing recorder does the job.
tag: taste
Claims: b-sb09-f002567-c6

## nextest-vs-custom-runner--p1
cargo-nextest's different test-execution model (parallel processes) broke an existing assumption — a global mutex handing out network ports one at a time — and fixing that would have cost more time than was available, so a custom `cargo test` wrapper (sharded execution, JUnit XML conversion) was built instead.
tag: fact
Claims: a-saL2-f011092-c1

## nightly-feature-autodetection--p1
Unstable features should only impact those who opted in — that's how the entire nightly system is designed. Wanting nightly for one ergonomic reason doesn't mean consenting to dependencies silently using other unstable features, or having them implicitly change behavior; libraries auto-enabling features runs counter to the Rust Project's own principle.
tag: tradeoff
Claims: a-sa19-f009343-c5, a-sa19-f009343-c4, a-sa19-f009343-c3, a-sa19-f009343-c6

## nightly-feature-autodetection--p2
As a "Group B" ergonomics-motivated developer, a crate that documents and auto-detects nightly features is preferable to one that forces manual opt-in flags — while "Group A" safety-critical users still need a documented full opt-out.
tag: tradeoff
Claims: a-sa19-f009343-c7

## nightly-gate-feature-vs-cfg--p1
Gate the tail-call code with `#[cfg(pulley_tail_call)]` set via `RUSTFLAGS` rather than a Cargo feature, because a Cargo feature gets force-enabled by the "test with all features enabled" CI job even on a stable compiler — and this lets the PR land, checked only by a dedicated nightly `cargo check` job, ahead of upstream rustc codegen support.
tag: fact
Claims: b-sb06-f002033-c1

## nightly-in-production--stable-only
The team does not, has not, and does not plan to rely on unstable Rust features; every foundational crate is published to crates.io with no unpublished dependencies.
tag: tradeoff
Claims: a-saL2-f011092-c5

## nightly-in-production--nightly-when-it-pays
Raw target-feature-gated intrinsics are unsafe, verbose, and need manual wrapping and runtime feature detection. `std::simd`'s portable_simd lets you write safe, ordinary iterator code the compiler lowers per architecture — "the choice," even though it currently requires nightly.
tag: tradeoff
Claims: b-sb23-f011233-c3

## no-std-for-wasm--p1
"You do not need to disable libstd when compiling to wasm!" — that step is necessary only for embedded, not for browser/wasm targets.
tag: fact
Claims: a-sB01-f000217-c4

## non-exhaustive-by-default--non-exhaustive-by-default
Because custom transports (bluetooth, WebRTC) and new address kinds are a planned direction, types like `TransportAddr`, `PathEvent` and `IncomingLocalAddr` are marked `#[non_exhaustive]` so future variants can be added without breaking the public API — callers must add a wildcard match arm.
tag: tradeoff
Claims: a-sT08-f004169-c2, a-sR13-f004685-c3, a-sR13-f004586-c2

## nonnull-in-ffi-params--p1
Deliberately did not implement taking `NonNull<T>` as a parameter in the atomic-pointer API, specifically to avoid adding a runtime check.
tag: tradeoff
Claims: a-02-f000977-c1

## object-graph-representation--indices-or-handles
Rc<RefCell<T>> compiles for "object soup" but leaks memory on reference cycles and panics on self-referential mutable borrows; raw/unsafe pointers hit the same aliasing problems with undefined-behavior risk. Keeping objects in a `Vec` and referring to each other by `usize` index turns aliasing bugs into compiler errors and serializes/parallelizes cleanly with serde/rayon — the same shape an ECS-ish API paired with handles would take for a scripting-language boundary, though that pairing has never actually been built out to prove it works.
tag: tradeoff
Claims: b-sb20-f007608-c1, b-sb26-f013214-c5

## one-enum-vs-two-types--p1
The enum-based accessor is confusing when traversing relations dynamically; better to split it into two separate structs plus friendlier wrapper methods.
tag: taste
Claims: a-sa07-f003716-c3

## oop-patterns-in-rust--p1
Try generic types like `Rc<E>` instead of Abstract Factory — factories are rarely used in Rust.
tag: taste
Claims: a-sa30-f013276-c6

## opt-level-z-vs-s--p2
Surprisingly, opt-level="s" can sometimes result in smaller binaries than opt-level="z" — always measure, never assume the more aggressive flag wins.
tag: fact
Claims: b-bk02-f000256-c10, a-sB02-f000256-c7

## optional-parameters-api-shape--one-configurable-entry
Rust has neither overloading nor default parameters, so route optional configuration through one entry point: a `ColorSpace` enum as a second constructor argument instead of a method per color space, everything through the config struct once a setting belongs to it, or an `_with_opts` method taking an Options struct plus `impl Into<T>` convenience wrappers.
tag: tradeoff
Claims: a-01-f000530-c2, b-sb05-f001512-c3, b-sb10-f003222-c2

## optional-parameters-api-shape--drop-feature-keep-signature-small
Willing to merge without automatic BOM/UTF-16 detection, to keep the `load` call simple — fewer arguments over the extra feature.
tag: tradeoff
Claims: a-sa06-f003414-c5

## optional-parameters-api-shape--separate-specialized-entries
One explicitly-named method per source type and color space keeps the target color space visible at the call site rather than inferred from context; a single merged function would force passing four arguments everywhere, making the code significantly less readable.
tag: tradeoff
Claims: a-01-f000530-c1, a-sa06-f003414-c4

## optional-parameters-api-shape--many-constructors-criticized
There are way too many constructors and not enough documentation.
tag: tradeoff
Claims: b-sb05-f001512-c4

## oss-framework-monetization--fully-open
Donate the project to the community under an open-source license; or build a paid layer that adds value through complementarity — a fully-capable free/local plan alongside a paid cloud layer — rather than restricting features behind a paywall.
tag: taste
Claims: b-sT05-f002775-c1, a-sa09-f004016-c1

## oss-reuse-attribution-norms--coordination-and-credit-matter
Copy-pasting, stripping and renaming another team's code, then shopping it around for maintainers, without reaching out first, is disrespectful of the original authors' investment even where the license allows it — publishing a "debranded" version without discussing it first is "bad form... legal... but bad form nonetheless." A near-verbatim uncredited copy, bugs included, should carry a co-authored-by credit; once pointed out, that credit gets added along with a PR-body acknowledgment of the prior work.
tag: taste
Claims: a-sa05-f003025-c8, a-sa05-f003025-c6, a-sa13-f004772-c7, a-sa13-f004772-c8

## oss-reuse-attribution-norms--no-entitlement
Producers of open source aren't entitled to anything, the same way consumers aren't either — forking and improving others' code is the real beauty of open source, a gift with no expectations.
tag: taste
Claims: a-sa05-f003025-c7

---
Filled batch 1 file 08 (13 Questions, 60 Claims) for run a: every Claim got a Position id, `none`, or flagged ambiguous with low confidence and a stated reason. Two low-confidence cases stand out — the middleware-hook Voice quoting Dropshot's own FAQ rather than asserting a view, and opt-level-z-vs-s's two Positions being near-textual-duplicates, forcing an arbitrary split on c10/c7. 43 Positions got a one-paragraph summary and a fact/tradeoff/taste tag; none carry a verdict.
