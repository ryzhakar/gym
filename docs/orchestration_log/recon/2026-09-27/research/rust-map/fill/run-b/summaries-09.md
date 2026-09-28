# Blind fill B, batch 1, file 09 — Position summaries

## pac-crate-per-chip-vs-shared--single-crate-with-features — One shared crate
Advocates prefer adding new chip support to an existing shared PAC crate (the `stm32-metapac` pattern) rather than a new per-chip crate (the `nrfxxx-pac` pattern used elsewhere in the same org), reporting after trying it that it was easier than expected and that Cargo features are much less annoying to release and manage this way.
Tag: tradeoff
Claims: a-sa01-f001838-c1, b-sb06-f001838-c1

## paid-maintainers-for-infrastructure--fund-maintainers — Fund dedicated maintainers
Advocates describe funding as removing the tradeoff between doing maintenance work they love and taking a better-paid job elsewhere, letting them pour full effort into the project without financial anxiety; at the team level, a funding body opens a new full-time maintainer position after a team "struggled with meeting its maintenance demands" once volunteer members left or lost funding, framed as partial relief rather than a full fix.
Tag: fact
Claims: a-sR15-f009751-c2, a-sR15-f009751-c1, b-sR13-f009755-c1

## parser-combinator-vs-generator--p1 — Nom-style parser combinators
Advocates hold that nom is efficient and fast, avoiding allocation when it doesn't need it, and that combinator chains can still get human-readable error messages via `context`/`convert_error`.
Tag: fact
Claims: b-sR13-f007973-c1

## persistent-collections-cheap-clone--p1 — Persistent, structural-sharing vector types
Advocates argue Rust collections already behave like values but pay for it with an expensive (deep-copy) clone, and ask what if that clone could be nearly free — motivating a persistent-vector library built around cheap, path-copying clone.
Tag: tradeoff
Claims: b-sR13-f008801-c1

## pin-for-non-relocatable-cpp-types--p1 — Yes, Pin is the emerging convention
Advocates note there is growing support for using `Pin` to represent C++ values that cannot be relocated via bitwise memcopy (e.g. small-string-optimized `std::string`), even though the same aliasing/projection/auto-ref ergonomics gaps that affect `Pin` elsewhere still apply here.
Tag: fact
Claims: b-sb24-f011312-c5

## pin-project-vs-pin-project-lite--p1 — pin-project-lite to avoid proc-macro deps, pin-project otherwise
Advocates (the async-book itself) recommend `pin-project-lite` when a project wants to avoid adding procedural-macro dependencies, at the cost of being less expressive and giving no custom error messages, and recommend `pin-project` otherwise.
Tag: tradeoff
Claims: b-bk01-f000233-c9

## pin-vs-move-constructors--p1 — Pin's phased/place-based design over the alternatives
Advocates defend why Rust didn't solve self-referential futures with a `Move` marker trait (rejected: pinning is a phased, per-place concept while traits apply to a value's whole lifetime, and a `Move` trait would create widely "infectious" bounds plus backward-compatibility breakage) or C++-style move constructors (rejected: breaks Rust's bitwise-move invariant, silently breaking unsafe code, and cannot fix up references held from outside the moved object).
Tag: fact
Claims: b-bk01-f000233-c10

## platform-gating-feature-vs-target-cfg--p1 — Prefer target-based gating once stabilized
Advocates hold that once a target (e.g. `wasm32-wasip2`) becomes a stable Rust target, platform-specific code gating can be simplified by switching from Cargo feature flags to a target directive.
Tag: tradeoff
Claims: b-sR05-f002151-c2

## platform-logic-module-vs-inline--p1 — Keep platform-specific logic inline
Advocates prefer keeping all logic for one file in that file, marking a small unsafe helper with a `// SAFETY` comment at the call site, rather than introducing a separate module or abstraction that would add more `#[cfg]`s to validate.
Tag: taste
Claims: a-sa14-f005079-c5

## plugin-system-mechanism--p1 — Native dylib rejected
Advocates reject native dynamic libraries as a Rust plugin mechanism because there is no stable ABI, no sandboxing (a buggy or malicious plugin can crash or compromise the host), and compiled-code distribution hides backdoors and is harder to audit than scripts.
Tag: tradeoff
Claims: a-sa16-f007483-c1

## plugin-system-mechanism--p2 — Scripting language preferred
Advocates recommend embedding QuickJS as the default approach for a Rust plugin system — over V8/deno_core and over Lua — citing small binary size, no JIT, faster cold starts, and easier integration, evaluating other methods only when QuickJS has too many drawbacks for the specific use case.
Tag: taste
Claims: a-sa16-f007483-c2

## plugin-system-mechanism--p3 — Wasm too immature
Advocates judge WebAssembly currently too immature for a Rust plugin system despite its sandboxing strength, citing uneven cross-language WASM support and churning toolchains/targets (WASI p1, p2).
Tag: fact
Claims: a-sa16-f007483-c3

## plugin-system-mechanism--p4 — Expression engine for bounded untrusted eval
Advocates, for their own project, fork CEL down to a boolean-only subset, reasoning that a non-Turing-complete expression language gives bounded, predictable-runtime evaluation of untrusted user input; they recommend QuickJS instead for most other projects.
Tag: tradeoff
Claims: a-sa16-f007483-c4

## pointer-addr-vs-as-usize--p1 — Prefer `.addr()` over `as usize`
Advocates flag that casting a pointer to `usize` has implicit behavior around provenance and recommend `.addr()` instead, since provenance isn't needed in this case and it has more explicitly defined behavior.
Tag: fact
Claims: a-sa11-f004512-c1

## polonius-scope-cut--p1 — Cut scope for shippability
Advocates report the team actively discussing whether to accept a narrower Polonius formulation — one with a known false positive on a loop/region case their older, slower approach used to accept correctly — in exchange for an easier path to production readiness, while still evaluating what expressiveness limits that would impose elsewhere.
Tag: tradeoff
Claims: a-sa20-f009698-c3

## portable-async-vs-sync-io--p1 — Go async, or split by target — never synchronous
Advocates state that synchronous I/O is not an option on the Web, and name two alternative architectures for a portable library — a function generic over a Future type, or a trait implemented once per target behind `#[cfg(target_arch = "wasm32")]` — without picking one as universally superior.
Tag: fact
Claims: b-bk02-f000256-c6

## portable-kernels-performance-cost--p1 — Comptime specialization avoids the tradeoff
Advocates claim their framework disproves the industry-consensus GPU/CPU portability-performance tradeoff, using `comptime` to specialize kernels per plane size and line size, including setting plane size to 1 for the CPU runtime rather than simulating GPU execution.
Tag: fact
Claims: a-sa09-f004016-c2

## porting-to-rust-safety--naive-port-not-safe — No; restructure or risk new UB
Advocates hold that pure Rust cannot create mutably-aliasing references, so if a ported function relies on C++'s permissive aliasing, naively translating it and letting the optimizer assume exclusivity can silently introduce new undefined behavior absent from the original C++; separately, an advocate found that eliminating memory leaks and UB was harder than expected because the existing C-style code's organization did not allow refactoring into a safe version — implying a straight port preserving the original architecture does not by itself deliver Rust's safety benefits.
Tag: fact
Claims: b-sb24-f011312-c4, a-sa21-f011069-c4

## postfix-await--p1 — Postfix `.await`
Advocates hold postfix `.await` is more ergonomic than a prefix operator in chains of method calls and field accesses, contrasting `fetch().await?.status_code` against the prefix-syntax equivalent `(await fetch())?.status_code` as more natural to read in longer chains.
Tag: taste
Claims: b-bk01-f000233-c1

## pre-1-0-api-default-stability--p1 — Stable unless flagged
Advocates, absent a known blocking issue, see no problem exposing an unreviewed API surface as stable for now, having assumed the team was already aligned on that.
Tag: taste
Claims: b-sb08-f002517-c1

## pre-1-0-api-default-stability--p2 — Unstable until agreed ready
Advocates object that prior work on the API assumed it would stay unstable, and that some enum variants don't make sense for the current driver; after pushback, even the API's own author reverses course and agrees the general consensus that it isn't ready, marking it unstable for now.
Tag: taste
Claims: b-sb08-f002517-c2, b-sb08-f002517-c3

## pre-1-0-canary-releases--p1 — Frequent canary releases for fast feedback
Advocates conclude that waiting until everything was fully finished before releasing was not the best way to get a stable release into users' hands, and instead ship three-week cycles and fast canary releases before 1.0 to get feedback quickly and move with confidence.
Tag: taste
Claims: b-sb10-f003188-c1

## predicate-rules-vs-first-match--p1 — Ordered first match wins
Advocates propose redesigning independent boolean-predicate configuration rules as a match-style ordered list evaluated first-match-wins, after the predicate-function design produced a real bug (two mutually exclusive conditions both evaluating false).
Tag: tradeoff
Claims: b-sb09-f003030-c8

## proc-macro-derives-vs-reflection-shape--proc-macros-costly — Proc macros are costly and unsolved
Advocates describe procedural macros as a pure AST transform shaped as Rust source that the compiler must compile, optimize, run, and grant disk/network access to "just in case," noting many people have tried to fix this and nothing has stuck.
Tag: fact
Claims: a-sa25-f011413-c1

## proc-macro-derives-vs-reflection-shape--ship-shape-data — Ship shape data; reflection avoids annotation gaps
Advocates argue that instead of every new behavior (Debug, Display, Deserialize, ...) spawning its own trait and costly proc-macro derive that must independently win ecosystem-wide adoption, a type should derive one associated `SHAPE` constant (name, offset, alignment, type id, variants, attributes, doc comments) that many downstream behaviors can consume from a single derive; they also note a reflection-based serializer can inspect a concrete element type at runtime and pick the right encoding without the explicit annotation Serde needs because Rust has no stable (or nightly-safe) specialization.
Tag: tradeoff
Claims: b-sb24-f011413-c1, b-sb24-f011413-c2

## proc-macro-derives-vs-reflection-shape--reflection-doesnt-clearly-win — Reflection's runtime cost is real and a JIT is no general answer
Advocates report measuring, contrary to their own expectation, that reflection's build times come out roughly a wash against Serde's generated code while its runtime performance is unconditionally worse "by design" and "a fact of life"; a Cranelift JIT built on the reflected data can close or beat the gap in a microbenchmark, but shipping a JIT isn't viable broadly — rejected outright on Apple platforms and disliked by users for unexplained binary size and warm-up cost.
Tag: fact
Claims: a-sa25-f011413-c4, b-sb24-f011413-c3, a-sa25-f011413-c5

## proc-macro-emitted-paths-hidden-deps--p1 — Fix via feature-gating, not via requiring every downstream crate to declare the dependency
Advocates trace a hidden transitive-dependency compile error to a macro unconditionally emitting a call gated on `debug_assertions`/`ssr`, and propose fixing it by having the `ssr` feature also enable the needed dependency's feature, or by reworking the macro's `cfg_attr` gating, rather than requiring every downstream crate to declare the dependency itself.
Tag: tradeoff
Claims: a-01-f000701-c1

## profile-before-optimizing--p2 — Let profiling data override the developer's hypothesis, every time
Advocates narrate cases from their own tutorial where the expected bottleneck was wrong — a canvas setter, not the expected hot function, ate 40% of frame time; a suspected allocation cost turned out negligible — using these as reminders to always let profiling, not intuition or a stated hypothesis, guide where optimization effort goes.
Tag: fact
Claims: b-bk02-f000256-c7, a-sB02-f000256-c6

## project-decision-speed-vs-inclusion--alt1 — Pick progress and faster consensus over inclusive process
Advocates argue the community must learn to recognize when having a consensus matters more than having the right consensus, and in those cases pick progress over stagnation, contrasting this with frustration over long-stalled nightly-only APIs and floating a BDFL model.
Tag: taste
Claims: b-sb19-f005743-c9

## project-discussions-area--p1 — Removing the discussion area lost knowledge
Advocates report that design talk is now forced into an ill-fitting issue thread, with no alternative location, after the discussion area's removal, and that explanations that used to live in discussions (including a detailed one on bus arbitration) have all been deleted.
Tag: fact
Claims: b-sT05-f002499-c10, b-sT05-f002499-c9

## project-priorities-communication--p1 — A lightweight, non-authoritative "Goals" system rather than a fixed roadmap or ad hoc culture
Advocates explicitly frame their project's Goals system as "not a roadmap" and "not authoritative," having loosened an initial rollout that felt "dictatorial" (staffed/unstaffed read as active/inactive) so any approved Goal can get a Working Group even unstaffed, while staffing still signals leadership focus.
Tag: taste
Claims: b-sR11-f004993-c2

## properties-syntax--p1 — Reject properties
Advocates hold that field access should stay visibly cheap and free of unseen consequences, and that hiding a method call — which could do anything, including crash or block on a network request — behind ordinary field-access syntax is undesirable, especially in a systems language.
Tag: taste
Claims: b-sb19-f007207-c2

## ptx-build-host-vs-multi-arch--p1 — Compile for build host only
Advocates clarify that PTX is compiled for the user's own machine via `build.rs` at build time, not distributed as one binary to everyone, framing this as already addressing the portability concern.
Tag: fact
Claims: b-sb08-f002518-c1

## ptx-build-host-vs-multi-arch--p2 — Needs portable multi-arch support
Advocates flag that compiling only for the compute capability active on the build host may break portability across systems with multiple different GPUs.
Tag: tradeoff
Claims: b-sb08-f002518-c2

## public-naming-brevity-vs-clarity--clarity-over-brevity — Name for clarity and the literal mechanism
Advocates decline abbreviating a public name, preferring to spell it out in full so users can infer what it means from the name alone.
Tag: taste
Claims: b-sR04-f001617-c1

## public-naming-brevity-vs-clarity--alt1 — Favor brevity or memorability
Advocates rename a public type to a shorter, plainer name, reasoning that a fun/evocative name became a liability once it got too long, even though the team liked the original.
Tag: taste
Claims: b-sR04-f001515-c1

## pump-events-timeout-poll--p1 — Any `Some(duration)` timeout should force `ControlFlow::Poll`
Advocates propose that every non-nil duration passed to `pump_events`, not just zero, should force `Poll`.
Tag: taste
Claims: a-sR08-f002685-c1

## pump-events-timeout-poll--p2 — Special-case only `Duration::ZERO`
Advocates narrow their workaround to the zero-duration case only, reasoning it doesn't make sense to return `Wait` when a nonzero duration was explicitly requested, and leave handling that case correctly to winit itself.
Tag: taste
Claims: a-sR08-f002685-c2

## pure-rust-crypto-stopgap--p1 — Pure-Rust crypto backend as an acceptable stopgap, not the end state
Advocates, finding both `ring` and `aws-lc-rs` fail on an unusual target because they wrap C code with platform-specific assembly, fork a pure-Rust backend down to only the primitives they need, explicitly stating a hardware-accelerated backend "would be the right thing to do for a production system" while treating the pure-Rust version as good enough for now.
Tag: tradeoff
Claims: a-sa11-f004471-c1

## quantization-speedup-candle--p1 — Quantization helps memory-bound cases only
Advocates note that some architectures (e.g. T5's cross-attention) involve much larger matmuls that make them compute- rather than memory-bound, so quantization's usual speedup — which comes from being memory-bound — is hard to realize there, even after tuning.
Tag: fact
Claims: b-sR01-f000464-c1

## query-engine-batching-parallelism--p1 — Partition-based batch execution captures the benefits of both
Advocates contrast a fully-sequential tight loop (cache-friendly, low interpretation overhead) against fully-parallel per-row processing (better core utilization), and endorse a partition-based architecture — vectorized batches within a partition, parallelized across partitions — as achieving a balance that reaps benefits from both ends.
Tag: tradeoff
Claims: a-sR08-f003580-c1

## quic-framing-one-stream-vs-per-message--p1 — Length-prefixed framing on one stream
Advocates hold that writing one chunk with `write_all` and reading it all before closing is fine while learning, but real protocols should send multiple logical messages per stream, each prefixed by its length, so the protocol is designed as messages rather than bytes and variable-length messages are handled.
Tag: tradeoff
Claims: a-sT08-f003375-c1

## rate-limiter-algorithm--p1 — Fixed-window counter, accepting its boundary-burst weakness
Advocates acknowledge a motivated client can double its effective rate by firing requests at the edges of two adjacent fixed windows — the textbook reason production-grade rate limiters move on from fixed windows — but keep the fixed window anyway because it keeps the storage schema minimal and easy to follow, an atomic `ADD` versus the extra round trip token bucket or sliding window would cost, leaving the algorithm swap as a follow-up.
Tag: tradeoff
Claims: b-sb22-f008906-c5

## reactive-keyed-child-notification--p1 — Default notify all children, favor no false negatives
Advocates conclude that broken reactivity (a write that silently misses a keyed child) is worse than unnecessary notifications, so a parent write should notify all keyed-child subscriptions by default, with precise per-field updates left as an opt-in path rather than the default.
Tag: tradeoff
Claims: b-sb13-f003963-c1, b-sb13-f003963-c2

## readability-vs-manual-optimization--p1 — Readability over manual optimization when the backend cleans up
Advocates hold that an eager-vs-lazy choice here doesn't matter much performance-wise since LLVM can likely optimize it away regardless, so the change is worth making for the sake of reader clarity.
Tag: tradeoff
Claims: b-sb05-f001582-c2

## reduction-accumulation-precision--p1 — Accumulate in float for precision
Advocates hold that a numeric reduction like softmax should accumulate in float32 even when the surrounding tensors are lower precision, to avoid precision loss, at negligible performance cost.
Tag: tradeoff
Claims: a-sR04-f001096-c1

## reflection-security-risk--p1 — Universally implemented reflection is suspicious
Advocates react to a marker trait auto-implemented for all types as inherently ominous, likening it to admitting "I am up to no good."
Tag: taste
Claims: a-sa28-f012469-c7 (voice track record uncertain in this source)

## reflection-security-risk--p2 — Rust lacks reflection and that closes off a footgun class
Advocates distinguish Rust from a Java/Struts-style deserialization RCE footgun (enabled by reflection plus dynamic class loading): in Rust, the same outcome would require someone to deliberately build a serde-serializable type to do it — a possible but deliberate act, not an accidental byproduct of a language feature.
Tag: fact
Claims: a-sa28-f012469-c8 (voice track record uncertain in this source)
