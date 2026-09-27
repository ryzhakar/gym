# Blind grouping — Rust batch 1 (merge-check2)

Written before opening merge*/ or audit/.

- Population: 494 team-local Questions parsed from team-a/extract-b1-*.md and team-b/extract-b1-*.md (`- Q:`, `- Question:`, `### Question —`); parser `merge-check2/pop.py`. Id `<a|b>-<slice>-<frame_id>-q<k>`, k counted within the frame's `## fNNNNNN` section of that file.
- Sample: seed 20260927, `random.Random(20260927).sample(range(494), 99)` over the parser's order (team-a files sorted, then team-b files sorted, file order within); 99 = ceil(0.2 × 494). Team split 53 a / 46 b.
- Method: each sampled item's co-members were sought over the whole population (all 494), not the sample only. Test: same decision a practitioner faces, context variants merged, different decisions apart. Group definitions: `merge-check2/groups.py`.
- Result: 33 sampled items in multi-member groups, 66 singletons.

| sampled id | group | co-members (population) | question (truncated) |
|---|---|---|---|
| a-02-f000957-q1 | singleton | — | When designing an async-computation hook API, should cancellation semantics be committed to upfront even at the cost of a larger initial API |
| a-02-f000993-q2 | singleton | — | Should a generic tensor-container abstraction enforce a single uniform tensor type across backends, or allow different backends/precisions t |
| a-sR01-f000227-q2 | singleton | — | Should real-time/embedded Rust frameworks model concurrency with async/await tasks rather than classical run-to-completion/interrupt-only ta |
| a-sR04-f001096-q1 | singleton | — | Should numeric reductions in a Rust ML kernel (e.g. softmax) accumulate in a higher-precision type than the input/output dtype? |
| a-sR05-f001981-q1 | contain-or-crash-on-unit-failure | a-sa14-f004985-q3 | Should an async QUIC accept loop treat an individual incoming-connection failure as fatal, or log it and keep serving? |
| a-sR05-f001981-q2 | singleton | — | Should a Rust library actively chase down and eliminate duplicate transitive dependency versions (e.g., two copies of `rustls`) in its depen |
| a-sR06-f001989-q1 | singleton | — | Should a HAL crate that needs allocator callback functions (e.g. `esp-wifi` needing `free_internal_heap`/`allocate_from_internal_ram`) take  |
| a-sR06-f002005-q1 | singleton | — | Should an embedded HAL's peripheral-signal abstraction expose electrical-configuration details (drive strength, pull resistors, input/output |
| a-sR07-f002155-q1 | interior-mutability-vs-restructure-ownership | b-sT09-f005440-q1, b-sb04-f001022-q1, a-sa06-f003414-q2 | When a Rust trait method receives only `&self` (because the implementing type is shared behind an `Arc`), should new mutable state be added  |
| a-sR07-f002271-q2 | singleton | — | What naming convention should Rust reactive-frontend-framework hooks use, given no established convention exists across the ecosystem? |
| a-sR08-f003033-q1 | singleton | — | When defining a Wasm component's WIT world, should a function be exported directly from the world, or wrapped inside a named interface that  |
| a-sR13-f004586-q1 | singleton | — | Should a Rust networking crate hard-depend on one crypto/TLS backend, or expose the backend as a pluggable provider? |
| a-sR13-f004586-q2 | non-exhaustive-before-1.0 | a-sT08-f004169-q2 | Should public enums/structs in an API heading toward 1.0 default to `#[non_exhaustive]`, accepting the forced wildcard match arm it imposes  |
| a-sR13-f004685-q2 | features-in-one-crate-vs-separate-crates | b-sR12-f005120-q1, b-sR05-f002151-q1 | Should optional library functionality live behind feature flags in the main crate, or be split out into separate crates/repos? |
| a-sR14-f005702-q1 | singleton | — | should a Rust web UI framework use fine-grained (signal-based) reactivity or virtual-DOM diffing |
| a-sT08-f003375-q1 | singleton | — | On a QUIC stream, should a protocol send several length-prefixed messages over one stream, or one message per stream written with `write_all |
| a-sT08-f004169-q3 | where-cross-cutting-auth-lives | b-sb22-f008906-q1, a-sa14-f005454-q2, a-saL1-f005454-q2 | Should authentication and similar concerns for iroh protocols live in connection-layer hooks (middleware), or inside each protocol implement |
| a-sT11-f007659-q1 | singleton | — | Should a Rust AWS Lambda be built with a size-optimized release profile (`opt-level = "z"`, `lto = true`, `codegen-units = 1`, `panic = "abo |
| a-sT11-f007659-q2 | singleton | — | Should a Rust Lambda ship as a zipped `provided.al2` bootstrap built by cargo-lambda, or as a container image? |
| a-sT12-f008455-q1 | objc2-vs-native-swift-glue | b-sb21-f008793-q1 | For iOS platform hooks such as AppDelegate calls in a Rust app, should the Rust side call Apple's Objective-C APIs directly through Rust bin |
| a-sT12-f009632-q1 | singleton | — | How should the Rust trademark policy govern use of the Rust name and marks? Should it follow the Rust Foundation's 2023 draft, which drew wi |
| a-sT12-f009704-q1 | singleton | — | When free CI for a platform disappears, should the Rust project keep the target at Tier 1 by other means, or demote it (here x86_64-apple-da |
| a-sa01-f001838-q1 | pac-per-chip-vs-shared | b-sb06-f001838-q1 | When an embedded Rust project adds support for a new, closely related microcontroller variant (here, rp2350 alongside the existing rp2040) v |
| a-sa02-f002127-q1 | feature-default-on-or-opt-in | b-sb25-f011435-q2, a-sa26-f011684-q1, b-sb25-f011684-q1 | When gating a new optional capability (e.g. an image format) behind a feature flag, should the default favor minimal friction (enable it, na |
| a-sa03-f002243-q1 | singleton | — | Should a machine-learning dataset abstraction that loads segmentation masks/images eagerly materialize every item into memory (e.g. building |
| a-sa05-f003074-q1 | singleton | — | In the Component Model's GC canonical ABI, should common shapes (e.g. `null` for `none`/`error`, a boolean `i32` for a no-payload `result`)  |
| a-sa07-f003704-q1 | static-vs-dynamic-typing-of-abstraction | a-sa30-f013276-q1 | Should a processing pipeline use runtime type erasure with up/down-casting, or a compile-time associated type on the processing trait? |
| a-sa07-f003704-q2 | singleton | — | Should a bounded, safety-first multi-pass graph algorithm favor a simple iterative fixed-point loop, or a more complex event-driven re-trigg |
| a-sa07-f003922-q1 | singleton | — | Should agent tool implementations couple to a specific language's SDK and calling runtime, or be built as portable WebAssembly components co |
| a-sa09-f004016-q1 | singleton | — | Should a Rust OSS framework monetize by gating features behind a paywall, or by building a complementary paid layer (e.g. a hosted cloud/tra |
| a-sa09-f004055-q1 | type-enforced-vs-convention-register-safety | a-sa05-f002466-q1, b-sR05-f002466-q1 | When a temporary/scratch register must cross a function boundary, should its safe use be enforced by the type system (dedicated types, exclu |
| a-sa09-f004055-q3 | validate-and-Result-vs-panic-or-caller | b-sb05-f001512-q1, b-sR10-f004573-q1, b-sR12-f005421-q1, a-sa21-f011069-q3 | For an operation whose safety depends on a runtime-checkable condition (e.g. whether a DMA buffer sits in DMA-accessible memory), should the |
| a-sa11-f004512-q2 | singleton | — | Should a low-level allocator-hook API pass the raw pointer type (`*mut u8`) through to callbacks, or reduce it to an address (`usize`) since |
| a-sa14-f004985-q1 | singleton | — | When compiling C/C++/Rust code to WebAssembly for a serverless runtime, should you go through an emulation layer like Emscripten, or compile |
| a-sa14-f004985-q2 | singleton | — | When a needed capability (like `eval`) isn't natively supported by the host platform, is it acceptable to run a full interpreter for that ca |
| a-sa14-f005149-q2 | singleton | — | Should error enums be scoped per-module (one large enum for everything a module can fail at), or per-function/operation (smaller, descriptiv |
| a-sa14-f005162-q1 | singleton | — | In embedded/no_std logging, should you format and print human-readable strings at the point of use, or defer formatting to the host by sendi |
| a-sa14-f005454-q3 | singleton | — | Should an HTTP API's handler signature be defined using an async trait decoupled from any concrete implementation, so tooling can extract AP |
| a-sa15-f005821-q1 | singleton | — | Does Rust's nightly `become` tail-call feature produce reliably good codegen across targets, or is it currently good on some architectures a |
| a-sa16-f007175-q1 | singleton | — | Should optional/alternate implementations in a Rust library be selected via Cargo feature flags, or via generic type-level component wiring  |
| a-sa17-f008217-q2 | singleton | — | In safety/crash-sensitive embedded Rust, should panics be eliminated for a given task at compile time, or tolerated and handled via runtime  |
| a-sa18-f008583-q1 | thiserror-display-chain-gap | b-sb21-f008583-q1 | When logging or wrapping errors in Rust, does `thiserror`'s default `{}` `Display` (which drops the source-error chain) create a real diagno |
| a-sa18-f008651-q1 | singleton | — | In a layered Rust service architecture, does splitting the repository layer into per-tenant/per-domain sub-crates (a crate boundary as an ad |
| a-sa18-f008787-q1 | singleton | — | For offline/edge ML inference (no cloud connectivity, consumer hardware), is a Rust-based stack (Burn) a viable or superior alternative to t |
| a-sa21-f011069-q2 | porting-to-rust-gives-safety | b-sb24-f011312-q4 | Does porting/rewriting existing C-style code into Rust automatically yield memory safety and eliminate undefined behavior, or does it requir |
| a-sa23-f011186-q4 | singleton | — | should generated crates be fully automatic, or must they leave handwritten escape hatches for what a schema can't express (e.g. trait impls) |
| a-sa26-f011684-q1 | feature-default-on-or-opt-in | a-sa02-f002127-q1, b-sb25-f011435-q2, b-sb25-f011684-q1 | should a Rust database's heap-profiling instrumentation (e.g. jemalloc mem-prof) be compiled in and enabled by default, or opt-in via a buil |
| a-sa28-f012469-q6 | singleton | — | What is `unsafe`'s proper mental model — a manual-invariant-maintenance discipline still bound by the same rules, or a permissive escape hat |
| a-sa29-f012940-q1 | tracing-vs-otel-api | b-sb24-f011306-q1 | For a new Rust application adopting OpenTelemetry, should the logging facade be the span-native `tracing` crate, or a conventional logging c |
| a-saL1-f005360-q1 | in-process-vs-process-isolation-http | a-sa14-f005360-q1 | Does using Rust to embed a full HTTP server as an in-process library (rather than nginx-style multi-process isolation) represent a genuinely |
| a-saL1-f005454-q1 | http-error-as-Err-or-Ok-response | b-sb22-f008906-q3, b-sb22-f008906-q4 | When modeling HTTP handler responses whose shape varies by status code, should a framework use a single unified enum spanning all status cod |
| a-saL1-f005516-q4 | singleton | — | Does Rust's composability (safe abstraction over data structures) let engineers actually ship better-optimized designs in practice than they |
| a-saL2-f011092-q2 | singleton | — | in a multi-tenant sandboxed runtime, should tenants share read-only memory pages (e.g. a JS engine's read-only heap) for efficiency, or shou |
| b-sR01-f000256-q1 | rust-wasm-vs-js-for-web-code | a-sa26-f011460-q1, a-sa26-f011460-q2, b-sb19-f005699-q1, b-sb20-f007290-q1 | Why (if at all) should Rust be chosen over JavaScript as a WebAssembly compile target? |
| b-sR01-f000464-q1 | singleton | — | Does quantization reliably speed up inference in candle, or only for some model architectures? |
| b-sR03-f000763-q2 | singleton | — | should derived per-column values be computed in a single iterator pass or via several simpler passes/collects? |
| b-sR03-f001160-q1 | depend-or-build-it-yourself | b-sR05-f002453-q1, a-sa14-f005079-q2, a-sa04-f002865-q1, a-02-f001053-q1, a-sR06-f002016-q1, a-saL2-f011092-q3 | should a library accept an uglier, more special-cased implementation to avoid growing its dependency footprint (here, avoiding the `syn` "ex |
| b-sR03-f001160-q2 | singleton | — | should a codegen tool trade a larger generated-output size for better runtime performance? |
| b-sR04-f001749-q1 | singleton | — | When an external callback API erases a reference's lifetime so it can be stored for later, how should the resulting unsafe surface be struct |
| b-sR05-f002048-q2 | singleton | — | should hardware/backend-specific magic numbers used in a GPU kernel be hardcoded inline, or threaded through as a comptime-configurable para |
| b-sR05-f002326-q1 | strictness-of-std-naming-conventions | b-sR08-f003587-q2, b-sb22-f009236-q1 | should a crate's naming for a raw-pointer-plus-length accessor follow std's `raw_parts`/`from_raw_parts` convention even where the analogy i |
| b-sR05-f002453-q2 | singleton | — | should a public trait's methods require callers to wrap `self` in `Arc` (shared ownership baked into the API), or accept a plain reference/g |
| b-sR08-f003531-q1 | singleton | — | Should a piece of state with more than two meaningful outcomes be represented as a bool (with special-cased checks layered around it) or as  |
| b-sR08-f003587-q1 | which-serialization-format | a-sa03-f002300-q1, a-sa06-f003590-q2, b-sb09-f003030-q1 | Which serialization format should a Rust library pick for a data format that needs no-std support? |
| b-sR10-f004741-q3 | enum-vs-trait-objects-for-variants | a-sa07-f003704-q3, a-sa17-f007884-q1 | Should an extensible policy/configuration surface (e.g. connection access control) be expressed as a closed enum, or as an open trait? |
| b-sR11-f005050-q1 | singleton | — | Should a Wasm component sandbox grant capabilities by default (ambient authority), or require every capability — including for middleware an |
| b-sR12-f005120-q2 | singleton | — | In a hot loop, should working memory be a caller-owned scratch buffer reused across calls, or freshly allocated per call for simplicity? |
| b-sR12-f005668-q1 | singleton | — | Should a language's memory-model default favor explicitness/performance (opt into convenience, as Rust's move/borrow-by-default with Cow/Rc  |
| b-sR13-f008801-q1 | singleton | — | Should Rust's collections behave like true persistent (structural-sharing) values with cheap clone, rather than accepting the current model  |
| b-sR13-f009740-q1 | ai-generated-contributions-policy | b-sR11-f004993-q1, b-sb15-f004721-q1, a-sa29-f013224-q2 | How should a Rust project respond to AI-generated contributions/proposals in its community processes? |
| b-sT02-f000576-q1 | singleton | — | Should a Rust block or function yield its value through an implicit tail expression (semicolon-less last line), or does that rule hurt reada |
| b-sT05-f002499-q2 | singleton | — | Can bare-metal Rust (esp-hal) match Arduino/esp-idf C for demanding display work on ESP32-S3? |
| b-sT05-f002499-q4 | singleton | — | When a HAL keeps a needed low-level facility private (cache writeback, DMA interrupts for a driver-owned channel), should users drop to the  |
| b-sT05-f002550-q1 | test-switch-compile-time-vs-runtime | b-sT04-f002233-q1 | Should test-only behaviour switches be compile-time environment variables or runtime API options gated behind a cargo feature? |
| b-sT05-f003044-q3 | adopt-binary-hot-patching | b-sb20-f007290-q3 | Is binary hot-patching (subsecond / `dx serve --hotpatch`) worth adopting over plain cargo rebuilds for iteration speed? |
| b-sT09-f011688-q1 | singleton | — | Should scheduled or background jobs in a Rust service run on a durable, database-backed job queue (e.g. apalis with Postgres storage) or on  |
| b-sb04-f001392-q1 | singleton | — | When a hand-tuned "fast path" optimization gives a large relative speedup on constrained/older hardware but a negligible absolute one on mod |
| b-sb05-f001512-q3 | options-struct-vs-many-methods | b-sb10-f003222-q2 | Should peripheral configuration be exposed through one `Config` struct set at construction, or through many individual constructors/`with_x` |
| b-sb05-f001582-q2 | singleton | — | When a compiler backend (LLVM/Cranelift) could optimize an eager computation away, should code still be written in the more efficient/lazy f |
| b-sb07-f002142-q1 | singleton | — | Should an ECS's relationship "edge" components be public types with the exclusivity (one-to-one, one-to-many, many-to-many, ...) encoded at  |
| b-sb08-f002518-q1 | singleton | — | Should a GPU-targeting Rust crate's build script compile device code (PTX) only for the build host's own compute capability, or build/distri |
| b-sb13-f004160-q2 | singleton | — | Should a CLI tool that repeatedly writes an output file overwrite the same filename by default (simpler, faster iteration, matches a peer to |
| b-sb14-f004398-q1 | singleton | — | When a public API wraps a `Box<dyn Fn>` behind a required constructor function, should the wrapped closure live in an unnamed tuple-struct f |
| b-sb16-f004997-q1 | singleton | — | When using an LLM to bring doc-comment prose in a codebase to a consistent style, should the project make the process reproducible by pinnin |
| b-sb17-f005113-q1 | singleton | — | When a struct's fields need a smaller in-memory footprint than natural alignment would otherwise give, should Rust code use `#[repr(packed)] |
| b-sb18-f005307-q1 | singleton | — | When your chosen async I/O library (e.g. quinn for QUIC) is paired with a storage/database layer that only offers a synchronous API (as with |
| b-sb19-f005964-q1 | replace-mature-c-lib-with-rust | a-sa15-f006797-q1 | Should legacy C-based TLS stacks (OpenSSL) be replaced by memory-safe Rust implementations (Rustls), now that Rustls claims server-side perf |
| b-sb20-f007290-q1 | rust-wasm-vs-js-for-web-code | b-sR01-f000256-q1, a-sa26-f011460-q1, a-sa26-f011460-q2, b-sb19-f005699-q1 | is Rust (via a fullstack WASM framework like Dioxus) ready to replace JavaScript/TypeScript frameworks for frontend and fullstack web develo |
| b-sb20-f007678-q1 | jni-layer-rust-vs-cpp | b-sb22-f008914-q1 | for an Android app calling into a shared Rust library, should the JNI-facing binding layer be hand-written in Rust (alongside the Rust↔C FFI |
| b-sb22-f008906-q5 | singleton | — | for a rate limiter, should you use a fixed-window counter, a token bucket, or a sliding window? |
| b-sb22-f008906-q6 | singleton | — | should per-IP/per-user rate limiting on a Lambda-fronted API be built as custom middleware, or left to API Gateway usage plans? |
| b-sb22-f009062-q1 | singleton | — | when the goal is running an existing, unmodified Rust/Linux program (with threads, filesystem, subprocesses) inside a sandbox, should you ta |
| b-sb22-f009292-q1 | derive-arithmetic-in-std | a-sa19-f009292-q1 | should the standard library provide a `#[derive]` for arithmetic operator traits (`Add`, `Sub`, `Mul`, `Div`) that performs naive field-wise |
| b-sb23-f009334-q2 | singleton | — | Should crate "maintenance status" metadata be author-declared and decayed/expired automatically over time, or purely opt-in with no forced e |
| b-sb23-f011233-q2 | singleton | — | For performance-sensitive numeric code, should Rust developers prefer the ergonomic, nightly-only `std::simd` portable-SIMD API over stable  |
| b-sb24-f011413-q4 | reflection-type-model | a-sa25-f011413-q4 | Should a compiler-level Rust reflection mechanism describe a type's shape the way the compiler internally represents it, or the way it's erg |
| b-sb25-f011435-q2 | feature-default-on-or-opt-in | a-sa02-f002127-q1, a-sa26-f011684-q1, b-sb25-f011684-q1 | When building a modular engine, should each optional capability (JS engine, specific image/video codecs, networking, SVG) be its own compile |
| b-sb25-f012561-q2 | singleton | — | When a Bevy codebase grows past tens of thousands of lines and single-crate compile times become disruptive, should shared types be pulled i |
| b-sb26-f012849-q1 | adopt-rust-over-c-cpp-framing | b-sb19-f005743-q1 | does adopting a language with compiler-enforced ownership/borrow-checked safety (Rust) constitute a broad, unambiguous quality improvement o |

## Group reasons

- **rust-wasm-vs-js-for-web-code** (5): one decision: write browser-side code in Rust/Wasm or in JS/TS; heavy-compute vs whole-frontend is context under which the answer flips.
- **depend-or-build-it-yourself** (7): one decision: take a dependency (crate, feature, SDK, bindings) or write/vendor the code; footprint, audit burden, control are the context/values.
- **options-struct-vs-many-methods** (2): one decision: expose optional configuration through one options/Config struct or through many constructors/builder methods.
- **pac-per-chip-vs-shared** (2): same source, same decision.
- **contain-or-crash-on-unit-failure** (2): one decision: a failure in one unit (connection, component) crashes the process or is contained and serving continues.
- **feature-default-on-or-opt-in** (4): one decision: an optional capability ships enabled by default or stays opt-in behind a feature.
- **interior-mutability-vs-restructure-ownership** (4): one decision: reach for shared ownership / interior mutability (Rc/Arc + RefCell/Mutex) or restructure so ownership/&mut is threaded explicitly.
- **strictness-of-std-naming-conventions** (3): one decision: follow std's naming conventions (as_/to_/into_, from_raw_parts) strictly or loosely where the fit is inexact.
- **test-switch-compile-time-vs-runtime** (2): one decision: test-only/staging switches via compile-time (cfg/features/env) or runtime mechanism.
- **adopt-binary-hot-patching** (2): one decision for the practitioner: enable hot-patching during development; DWARF loss is context. Tool-builder direction questions (f002719-q1, a-sa26-f011305-q5) kept apart: different actor, different decision.
- **which-serialization-format** (4): one decision: which serialization format; no-std, wire compatibility, human readability, i128 support are contexts that flip the answer.
- **static-vs-dynamic-typing-of-abstraction** (2): one decision: compile-time generics/associated types or runtime type erasure/dyn.
- **enum-vs-trait-objects-for-variants** (3): one decision: model a set of variants as an enum or as trait objects/open trait; closed vs extensible set is context.
- **type-enforced-vs-convention-register-safety** (3): the extractor marked f004055-q1 as a recurrence of f002466; both f002466 extracts are the same source debate.
- **validate-and-Result-vs-panic-or-caller** (5): one decision: on invalid/unsafe input an API checks and returns Result, or panics/marks unsafe and leaves validation to the caller.
- **where-cross-cutting-auth-lives** (4): one decision: cross-cutting concerns (auth) enforced in a middleware/hook layer, per handler/protocol, or through types.
- **non-exhaustive-before-1.0** (2): same decision, same library family.
- **features-in-one-crate-vs-separate-crates** (3): one decision: optional/young functionality lives in the main crate (behind features) or in separate crates.
- **in-process-vs-process-isolation-http** (2): same source, same decision.
- **http-error-as-Err-or-Ok-response** (3): one decision: HTTP error statuses are carried as Err or as part of the Ok response value.
- **replace-mature-c-lib-with-rust** (2): one decision: replace a battle-tested C library (OpenSSL, image codecs) with a Rust implementation.
- **jni-layer-rust-vs-cpp** (2): identical text.
- **objc2-vs-native-swift-glue** (2): one decision: reach Apple APIs from Rust via objc2 bindings or write native Swift/ObjC; AppDelegate hooks vs XCTest are contexts.
- **thiserror-display-chain-gap** (2): same source, same decision.
- **derive-arithmetic-in-std** (2): same source, same decision.
- **ai-generated-contributions-policy** (4): one decision: whether AI-authored contributions/proposals/posts are acceptable in Rust project and community processes. Newsletter content (f007942-q1) kept apart: publication, not contribution.
- **porting-to-rust-gives-safety** (2): one decision: treat a port to Rust as memory-safe because it compiles, or restructure first.
- **reflection-type-model** (2): same source, same decision.
- **adopt-rust-over-c-cpp-framing** (2): one decision: adopting Rust over C/C++ is a broad/moral imperative or a narrower engineering trade-off.
- **tracing-vs-otel-api** (2): one decision: which instrumentation API (tracing crate vs OTel-native / conventional log) to standardize on.
