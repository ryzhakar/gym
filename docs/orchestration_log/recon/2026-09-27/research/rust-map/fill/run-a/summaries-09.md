# Blind fill summaries, batch 1, file 09 (run a)

## pac-crate-per-chip-vs-shared--single-crate-with-features
One shared PAC crate (`stm32-metapac` style) covering related chips, feature-gated, was easier to build than expected and made Cargo features "clean up" — much less annoying to release and manage than a separate crate per chip.
tag: tradeoff
Claims: a-sa01-f001838-c1, b-sb06-f001838-c1

## paid-maintainers-for-infrastructure--fund-maintainers
Funding removes the tradeoff between maintenance work someone loves and a better-paid job elsewhere, meets financial needs, and boosts productivity; the Cargo team opened a funded Maintainer in Residence position after volunteer capacity struggled, framed explicitly as improving — not fully solving — the situation.
tag: tradeoff
Claims: a-sR15-f009751-c2, a-sR15-f009751-c1, b-sR13-f009755-c1

## parser-combinator-vs-generator--p1
nom is efficient and fast, doesn't allocate memory when parsing if it doesn't have to, and makes that easy for the user to replicate; `context`/`convert_error` give human-readable error messages out of a combinator chain.
tag: fact
Claims: b-sR13-f007973-c1

## persistent-collections-cheap-clone--p1
Rust collections already behave like values, they just have an expensive clone — what if that clone could be nearly free, via structural sharing?
tag: tradeoff
Claims: b-sR13-f008801-c1

## pin-for-non-relocatable-cpp-types--p1
Unsafe Rust has long assumed all types are memcopy-relocatable, but most C++ types run a move constructor (e.g. small-string-optimized `std::string`); there's growing support for representing such values with `Pin`.
tag: fact
Claims: b-sb24-f011312-c5

## pin-project-vs-pin-project-lite--p1
pin-project-lite is recommended when a project wants to avoid procedural-macro dependencies, at the cost of being less expressive and giving no custom error messages; pin-project is recommended otherwise.
tag: tradeoff
Claims: b-bk01-f000233-c9

## pin-vs-move-constructors--p1
A `Move` marker trait was rejected because pinning is a phased, per-place concept while traits apply to a value's whole lifetime — a Move trait would be widely "infectious" and break backward compatibility. C++-style move constructors were rejected because they'd break Rust's invariant that objects can always be bitwise-moved, silently breaking unsafe code and leaving no way to fix up references held from outside the moved object.
tag: tradeoff
Claims: b-bk01-f000233-c10

## platform-gating-feature-vs-target-cfg--p1
Once `wasm32-wasip2` becomes a stable Rust target, the use of feature flags for that platform code can be simplified by using the target directive instead.
tag: tradeoff
Claims: b-sR05-f002151-c2

## platform-logic-module-vs-inline--p1
Prefer keeping all `serve.rs`-related code in `serve.rs`, marking a helper `unsafe` with a `// SAFETY` comment at the call site, over introducing a separate module that adds more `#[cfg]`s to validate.
tag: taste
Claims: a-sa14-f005079-c5

## plugin-system-mechanism--p1
Native dynamic libraries have no stable ABI, offer no sandboxing (a buggy or malicious plugin can crash or compromise the host), and compiled-code distribution hides backdoors and is harder for users to audit than scripts.
tag: tradeoff
Claims: a-sa16-f007483-c1

## plugin-system-mechanism--p2
Embed QuickJS as the default plugin approach: small binary size, no JIT, faster cold starts, easier integration than V8/deno_core or Lua.
tag: tradeoff
Claims: a-sa16-f007483-c2

## plugin-system-mechanism--p3
WebAssembly is currently too immature to be used for a plugin system and will make plugin developers' lives hard, despite its sandboxing strength — uneven cross-language support, churning toolchains and targets (WASI p1, p2).
tag: fact
Claims: a-sa16-f007483-c3

## plugin-system-mechanism--p4
For his own project, forked CEL down to a boolean-only expression subset because non-Turing expression languages give bounded, predictable-runtime evaluation of untrusted user input; recommends QuickJS instead for most other projects.
tag: tradeoff
Claims: a-sa16-f007483-c4

## pointer-addr-vs-as-usize--p1
Casting a pointer to `usize` has implicit behavior around provenance; `.addr()` has more explicitly defined behavior and should be used when provenance isn't needed.
tag: fact
Claims: a-sa11-f004512-c1

## polonius-scope-cut--p1
The current datalog-based Polonius approximation handles all UI tests except a loop/region case the older, slower approach used to accept correctly; the team is discussing whether to cut scope and accept this narrower formulation in exchange for an easier path to production, while still evaluating what expressiveness limits it would impose.
tag: tradeoff
Claims: a-sa20-f009698-c3

## portable-async-vs-sync-io--p1
If a portable library must perform I/O, it cannot be synchronous — there is only asynchronous I/O on the Web — so architect it as a function generic over `F: Future`, or as a trait implemented once per target behind `#[cfg(target_arch = "wasm32")]`.
tag: fact
Claims: b-bk02-f000256-c6

## portable-kernels-performance-cost--p1
The industry consensus is that abstracting GPU and CPU programming without sacrificing performance is impossible; through intentional design — `comptime` specialization per plane size and line size, including plane size 1 for the CPU runtime rather than simulating GPU execution — this was proven otherwise.
tag: fact
Claims: a-sa09-f004016-c2

## porting-to-rust-safety--naive-port-not-safe
Pure Rust can't create mutably-aliasing references; if a ported function relies on C++'s permissive aliasing, naively translating it and letting the optimizer assume exclusivity can silently introduce new undefined behavior that wasn't present in the original C++. Separately, existing C-style code's organization can make it too hard to refactor into a genuinely safe version, so a straight port doesn't by itself deliver Rust's safety benefits.
tag: fact
Claims: b-sb24-f011312-c4, a-sa21-f011069-c4

## postfix-await--p1
Postfix `.await` reads more naturally in chains of method calls and field accesses — `fetch().await?.status_code` against the prefix-syntax equivalent `(await fetch())?.status_code`.
tag: taste
Claims: b-bk01-f000233-c1

## pre-1-0-api-default-stability--p1
Without a known blocking issue, there's no problem exposing the interrupt API as stable for now.
tag: tradeoff
Claims: b-sb08-f002517-c1

## pre-1-0-api-default-stability--p2
Prior PRs targeting interrupts assumed they wouldn't be stabilized, and some interrupt enum variants don't make sense for the CPU-driven driver — after pushback, agreement that the API isn't ready and should stay unstable.
tag: tradeoff
Claims: b-sb08-f002517-c2, b-sb08-f002517-c3

## pre-1-0-canary-releases--p1
Waiting until everything was fully finished before releasing was not actually the best way to get a stable release into users' hands; three-week cycles and fast canary releases before 1.0 get feedback quickly and let the team move with confidence.
tag: tradeoff
Claims: b-sb10-f003188-c1

## predicate-rules-vs-first-match--p1
After a predicate-function design produced a real bug (two mutually exclusive conditions both false), redesign the conditional rules as a match-style, ordered "first condition wins" list.
tag: fact
Claims: b-sb09-f003030-c8

## proc-macro-derives-vs-reflection-shape--proc-macros-costly
A pure AST transform gets shaped as Rust source that the compiler must compile, optimize, run, and grant full disk/network access to "just in case" — every new behavior (Debug, Display, Deserialize, ...) tends to spawn its own trait and derive macro that must independently win ecosystem-wide adoption, and many attempts to fix this haven't stuck.
tag: tradeoff
Claims: a-sa25-f011413-c1

## proc-macro-derives-vs-reflection-shape--ship-shape-data
Instead of turning types into more code, ship data about types: a single associated `SHAPE` constant per type (name, offset, alignment, type id, variants, attributes, doc comments) that many downstream behaviors can consume from one derive, and that a reflection-based serializer can use to pick the right encoding for a concrete element type at runtime — something Serde needs an explicit annotation for, since Rust has no stable or nightly-safe specialization to detect it automatically.
tag: tradeoff
Claims: b-sb24-f011413-c1, b-sb24-f011413-c2

## proc-macro-derives-vs-reflection-shape--reflection-doesnt-clearly-win
Reflection was expected to trade only build time for runtime speed; measured build times came out "a wash" and runtime performance unconditionally worse "by design... a fact of life, you can do nothing to change that" — a negative result. A Cranelift JIT built on the reflected data can beat Serde in a microbenchmark, but shipping a JIT isn't viable broadly: rejected outright on Apple platforms, disliked for unexplained binary size and warm-up cost.
tag: fact
Claims: a-sa25-f011413-c4, b-sb24-f011413-c3, a-sa25-f011413-c5

## proc-macro-emitted-paths-hidden-deps--p1
Trace the root cause to `leptos_macro`'s `view!` macro unconditionally emitting `tracing::instrument` under `debug_assertions`/`ssr`; fix it by having the `ssr` feature also enable `tracing`, or by reworking the macro's `cfg_attr` gating, rather than requiring every downstream crate to add `tracing` itself.
tag: tradeoff
Claims: a-01-f000701-c1

## profile-before-optimizing--p2
Time may be spent in places you don't expect: the fillStyle canvas setter, not tick(), ate 40% of frame time; vector allocation, the stated hypothesis for the bottleneck, turned out to have negligible cost — always let profiling guide your focus and override your hypothesis.
tag: fact
Claims: b-bk02-f000256-c7, a-sB02-f000256-c6

## project-decision-speed-vs-inclusion--alt1
We must learn to recognize when having a consensus is more important than having the right consensus, and in these cases, pick progress over stagnation.
tag: taste
Claims: b-sb19-f005743-c9

## project-discussions-area--p1
Design talk and explanations that used to live in the project's discussion area — including one contributor's writeup on bus arbitration — got deleted along with it, and there's now no alternative location for that kind of discussion.
tag: fact
Claims: b-sT05-f002499-c10, b-sT05-f002499-c9

## project-priorities-communication--p1
This is notably not a "roadmap" and also not authoritative — an initial staffed/unstaffed framing that read as active/inactive felt dictatorial, so it was loosened: any approved Goal can get a Working Group even unstaffed, while staffing still signals leadership focus.
tag: tradeoff
Claims: b-sR11-f004993-c2

## properties-syntax--p1
Field access should be visibly cheap and side-effect-free; hiding a method call — which could do anything including crash or block on a network request — behind `foo.x` syntax is undesirable, especially in a systems language.
tag: taste
Claims: b-sb19-f007207-c2

## ptx-build-host-vs-multi-arch--p1
The PTX is compiled for your machine via `build.rs` at compile time — it is not one binary distributed to everyone.
tag: fact
Claims: b-sb08-f002518-c1

## ptx-build-host-vs-multi-arch--p2
Compiling only for the build host's active compute capability may break portability across heterogeneous multi-GPU systems.
tag: tradeoff
Claims: b-sb08-f002518-c2

## public-naming-brevity-vs-clarity--clarity-over-brevity
It makes sense to spell out "snippets" explicitly in a name rather than abbreviate it to "scls," to make it a bit easier on users to infer what the name means.
tag: taste
Claims: b-sR04-f001617-c1

## public-naming-brevity-vs-clarity--alt1
Fun names are great, but sometimes they get in the way — the team loved `MagicEndpoint` as a name, but it just became too long, so it was renamed to plain `Endpoint`.
tag: taste
Claims: b-sR04-f001515-c1

## pump-events-timeout-poll--p1
Any duration, as long as it's `Some`, should make the control flow `Poll`.
tag: tradeoff
Claims: a-sR08-f002685-c1

## pump-events-timeout-poll--p2
It doesn't make sense to return `Wait` when a nonzero duration like `Some(2s)` was explicitly requested — narrow the workaround to only the zero-duration case and leave the rest to winit's own handling.
tag: tradeoff
Claims: a-sR08-f002685-c2

## pure-rust-crypto-stopgap--p1
Both `ring` and `aws-lc-rs` fail on the target because they wrap C code with platform-specific assembly; since rustls providers are pluggable, fork a pure-Rust backend down to only the needed primitives to fit the binary-size budget — a hardware-accelerated backend "would be the right thing to do for a production system," but for now, pure Rust.
tag: tradeoff
Claims: a-sa11-f004471-c1

## quantization-speedup-candle--p1
T5's cross-attention involves much larger matmuls than llama/mistral, making it compute- rather than memory-bound on M1/M2; quantization's usual speedup comes from being memory-bound, so it's hard to beat Apple Accelerate here even after tuning parameters.
tag: fact
Claims: b-sR01-f000464-c1

## query-engine-batching-parallelism--p1
Contrasted a fully-sequential "tight loop" (cache-friendly, low interpretation overhead) against fully-parallel per-row processing (better core utilization); DataFusion's partition-based architecture achieves a balance, reaping benefits from both ends.
tag: tradeoff
Claims: a-sR08-f003580-c1

## quic-framing-one-stream-vs-per-message--p1
Writing one chunk with `write_all`, reading it all, then closing the stream is fine while getting familiar, but real protocols want something more sophisticated: multiple logical messages per stream, each prefixed by its length, so the protocol is designed as messages rather than bytes and variable-length messages are handled.
tag: tradeoff
Claims: a-sT08-f003375-c1

## rate-limiter-algorithm--p1
A motivated client can double its effective rate by firing requests at the edges of two adjacent fixed windows — the textbook reason people move to token bucket or sliding window — but those cost an extra DynamoDB round trip versus one atomic `ADD`; stick with the fixed window mostly because it keeps the schema minimal and easy to follow, leaving the algorithm swap as a follow-up.
tag: tradeoff
Claims: b-sb22-f008906-c5

## reactive-keyed-child-notification--p1
"False negatives" (broken reactivity) are worse than "false positives" (technically-unnecessary notifications) — track the parent path by default and notify all keyed children on a parent write, leaving precise-but-manual patch/update as an opt-in path.
tag: tradeoff
Claims: b-sb13-f003963-c1, b-sb13-f003963-c2

## readability-vs-manual-optimization--p1
It probably doesn't matter much either way in this case, since there isn't anything preventing LLVM from cleaning the eager computation up itself — but the change to the more efficient form is worth making anyway, for reader clarity.
tag: tradeoff
Claims: b-sb05-f001582-c2

## reduction-accumulation-precision--p1
Should probably accumulate with float in softmax to preserve precision — shouldn't affect performance at all.
tag: fact
Claims: a-sR04-f001096-c1

## reflection-security-risk--p1
The auto-implemented `Reflect` trait reads as inherently ominous — "like tapping the Marauder's Map with your wand and saying 'I solemnly swear I am up to no good.'"
tag: taste
Claims: a-sa28-f012469-c7

## reflection-security-risk--p2
Rust doesn't have dynamic class loading and reflection, but someone could still build a serde-serializable type to do custom remote command/process execution — the difference from a Java/Struts-style deserialization RCE is that it would be deliberate and not some oversight, though still possible given enough will.
tag: tradeoff
Claims: a-sa28-f012469-c8

---
Filled batch 1 file 09 (30 Questions, 58 Claims) for run a: every Claim got a Position id with a stated reason. One low-confidence case — polonius-scope-cut's claim describes an active team discussion leaning toward cutting scope, not a settled position. 48 Positions got a one-paragraph summary and a fact/tradeoff/taste tag, no verdicts.
