# Blind grouping — Rust batch 1, merge-check3

Written before opening merge*/ or audit/. Grouping rule: dispatch of 2026-09-28 (Question = concrete alternatives at one point of work; Value trade-offs are not Questions; "Choose Rust for X" one per X; context variants of one concrete choice are one Question).

## Population

- Parsed `- Q:`, `- Question:`, `### Question —` in team-a/extract-b1-*.md and team-b/extract-b1-*.md; frame from the preceding `## f<id>` heading; id `<team>-<slice>-<frame>-q<k>`, k counted per slice file per frame in file order.
- Raw 565. saL1 re-log replacements (my mapping, judged by content): sa14-f005360-q1,q2,q3 → saL1-f005360-q1,q2,q3; sa14-f005454-q2 → saL1-f005454-q2; sa15-f005516-q1,q2 → saL1-f005516-q1 (saL1 q1 fuses both); sa15-f005516-q3 → saL1-f005516-q3 (+q4). Kept: sa14-f005360-q4, sa14-f005454-q1, sa14-f005454-q3. Population 558.
- Sample: `random.Random(20260928).sample(sorted(ids), ceil(0.2*558))` → 112. Seed 20260928.

## Method

Read all 558 Question lines. For every sampled item, listed its co-members across the whole population (not only the sample). In-sample co-member set = those co-members that are also sampled. `*` = sampled.

## Groups (every group containing ≥1 sampled item)

### G01 api: many named entry points vs one parameterized entry point (no overloading/defaults)
- * `team-a-01-f000530-q1` — When Rust's lack of method overloading forces a choice for a type-conversion API surface (e.g. building a `Color` from `Vec4`, `[f32; 4]`, `Vec3`, `[f32; 3]` ac
-   `team-a-sa06-f003414-q4` — When a function's required inputs grow, is it better to add a separate specialized function or grow one function's argument list?
- * `team-b-sb05-f001512-q3` — Should peripheral configuration be exposed through one `Config` struct set at construction, or through many individual constructors/`with_x` builder methods?
-   `team-b-sb10-f003222-q2` — Given Rust has neither function overloading nor default parameter values, should optional/configurable operations expose a single `_with_opts(Options)` method (

### G02 form data list-vs-scalar cardinality
- * `team-a-01-f000543-q1` — When a UI framework's form-submission API hands back untyped, string-keyed values (e.g. a `HashMap<String, Vec<String>>`) for deserialization into a caller-defi

### G03 wasm store-tearing precise traps
- * `team-a-02-f001181-q1` — On hardware with "store-tearing" behavior, where a partial store can have observable side effects before trapping, should a WebAssembly runtime pay a load-befor

### G04 dynamic ECS components typed id vs untyped
- * `team-a-02-f001231-q1` — Should runtime-registered ("dynamic") ECS components carry a compile-time type witness (a typed ID wrapper constrained to `T: Component`) for safe access, or st

### G05 wasm requires no_std?
- * `team-a-sB01-f000217-q4` — Does compiling to WebAssembly require disabling the standard library (no_std), the way embedded targets do?

### G06 wasm allocator choice
- * `team-a-sB02-f000256-q10` — Should a size-sensitive wasm crate keep the default allocator, switch to a size-optimized allocator, or eliminate heap allocation entirely?
-   `team-b-bk02-f000256-q10` — Should a wasm target keep the default (dlmalloc-derived) global allocator or switch to a smaller, slower one?

### G07 debug wasm as native test vs in wasm
- * `team-a-sB02-f000256-q12` — When debugging Rust-generated WebAssembly, reproduce the bug as a native Rust #[test]/#[bench] first, or debug inside the wasm/browser environment directly?
- * `team-b-bk02-f000256-q7` — When debugging or benchmarking Rust destined for wasm, should the issue be reproduced as a native #[test]/#[bench] under OS-native tooling, or debugged directly

### G08 FFI/wasm boundary: copy/serialize vs opaque handle/shared ref
- * `team-a-sB02-f000256-q3` — At a Rust/JS boundary, expose large long-lived data by copying/serializing it across, or as an opaque handle into wasm linear memory?
-   `team-b-bk02-f000256-q2` — How should Rust expose computed state to JS across the wasm boundary — copy/serialize it, or share memory via pointer/opaque handle?
-   `team-b-sb20-f007678-q2` — across a Rust FFI boundary (to Kotlin/Java, Swift, or JavaScript), should complex data be copied across, or shared by reference/pointer?
-   `team-b-sb22-f008914-q2` — across a Rust FFI boundary (to Kotlin/Java, Swift, or JavaScript), should complex data be copied across, or shared by reference/pointer?
-   `team-a-sa26-f011460-q3` — at the Rust/Wasm↔JavaScript FFI boundary, should code favor ergonomic serialization (serde-wasm-bindgen) or manual/structural field access (wasm-bindgen getters

### G09 profiling vs hypothesis
- * `team-a-sB02-f000256-q6` — Should optimization work be guided by profiling measurements or by a developer's hypothesis about where cost lives?
-   `team-b-bk02-f000256-q6` — Should optimization effort be guided by profiling data or by the developer's hypothesis about where time/space goes?

### G10 benchmark moves with fn via git mv
- * `team-a-sR04-f001096-q2` — When a function moves to a different crate in a multi-crate Rust workspace, should its benchmark move with it, using `git mv` to preserve file history?

### G11 eliminate duplicate transitive dep versions
- * `team-a-sR05-f001981-q2` — Should a Rust library actively chase down and eliminate duplicate transitive dependency versions (e.g., two copies of `rustls`) in its dependency tree?

### G12 HAL hard dep on allocator crate vs fn interface
- * `team-a-sR06-f001989-q1` — Should a HAL crate that needs allocator callback functions (e.g. `esp-wifi` needing `free_internal_heap`/`allocate_from_internal_ram`) take a hard Cargo depende

### G13 signal type exposes electrical config
- * `team-a-sR06-f002005-q1` — Should an embedded HAL's peripheral-signal abstraction expose electrical-configuration details (drive strength, pull resistors, input/output mode) on the signal

### G14 Option<PIN> vs required placeholder
- * `team-a-sR06-f002005-q2` — When a driver constructor takes a set of GPIO/peripheral signals, should each signal be a required explicit value (even a placeholder like `Level::Low`), or sho

### G15 expose foreign/dependency type vs own type
- * `team-a-sR07-f002271-q1` — When wrapping a browser Web API (e.g. `UrlSearchParams`) inside a Rust frontend-framework hook, should the API surface the raw web-sys type or convert it to an 
-   `team-b-bk03-f000267-q15` — Should a crate depend on a third-party type directly in its public API, or wrap it behind a local newtype/abstraction?

### G16 WIT: export fn from world vs via interface
- * `team-a-sR08-f003033-q1` — When defining a Wasm component's WIT world, should a function be exported directly from the world, or wrapped inside a named interface that the world then expor

### G17 networking lib core: built-in bundle vs minimal core + plug-in layers
- * `team-a-sR11-f004170-q1` — Should a networking library ship built-in support for many use-case-specific transports/backends, or keep its core minimal and expose a pluggable trait-based ex
- * `team-a-sa02-f002124-q1` — Should a foundational networking/infra library keep expanding its default surface area to bundle more built-in functionality as part of "core", or aggressively 

### G18 reject unauthenticated conn before vs after handshake
- * `team-a-sR13-f004586-q3` — Should an async network server reject invalid/unauthenticated incoming connections before or after the handshake completes?

### G19 tiered builder (unchecked fast path + safe) vs one safe API
- * `team-a-sR16-f012642-q1` — Should a high-performance Rust client API expose multiple tiers of the same builder operation — an unchecked/positional fast path alongside a checked/named-fiel

### G20 pre-1.0 breaking wire change in minor vs compat
- * `team-a-sT04-f001319-q1` — Should a pre-1.0 Rust networking library ship breaking wire-protocol changes in a routine minor release for a protocol improvement, or keep compatibility with t

### G21 typestate generic Connection<T> vs separate types
- * `team-a-sT08-f004169-q1` — Should a Rust API express protocol states as one generic type with a typestate parameter (`Connection<T>`), or as separate concrete types per state?

### G22 Lambda zip bootstrap vs container image
- * `team-a-sT11-f007659-q2` — Should a Rust Lambda ship as a zipped `provided.al2` bootstrap built by cargo-lambda, or as a container image?

### G23 WASI P2 components vs C-ABI FFI
- * `team-a-sT12-f008237-q1` — For cross-language interop, should Rust code expose and consume WASI Preview 2 components (WIT interfaces, composition) or C-ABI FFI?

### G24 Apple platform glue: objc2 in Rust vs Swift/ObjC
- * `team-a-sT12-f008455-q1` — For iOS platform hooks such as AppDelegate calls in a Rust app, should the Rust side call Apple's Objective-C APIs directly through Rust bindings (`objc2`), or 
- * `team-b-sb21-f008793-q1` — For iOS UI testing, should a Rust practitioner write the test harness directly in Rust via `objc2`/`objc2-xc-test`/`objc2-xc-ui-automation` bindings (bypassing 

### G25 ML dataset eager vs lazy
- * `team-a-sa03-f002243-q1` — Should a machine-learning dataset abstraction that loads segmentation masks/images eagerly materialize every item into memory (e.g. building an `InMemoryDataset

### G26 ECS relationship single source of truth vs symmetric
- * `team-a-sa04-f002554-q1` — For an ECS relationship system, should the design enforce a single source of truth (only the `Relationship` component is authoritative, the reflected `Relations

### G27 ergonomic sugar now vs later
- * `team-a-sa11-f004512-q3` — When shipping a small utility feature quickly, is it worth adding ergonomic sugar (a macro/trait wrapper) around the raw mechanism, or should that wait until it

### G28 OpenAPI code-first vs spec-first
- * `team-a-sa14-f005454-q1` — For an HTTP API framework, should the OpenAPI spec be generated from the Rust code (code as source of truth), or should the code be generated from a hand-writte
-   `team-a-sa23-f011186-q1` — should an API's schema be hand-authored or generated from the server's own code (spec-first vs code-first)?

### G29 Rust for failure-heavy HTTP/WS ingress
- * `team-a-sa15-f005948-q1` — For a high-throughput, failure-heavy network service (translating HTTP/WebSocket traffic into distributed function calls), does Rust's pattern matching and owne
-   `team-b-sb19-f005948-q1` — For a high-throughput HTTP/WebSocket ingress layer with heavy edge-case and failure-mode handling, does Rust's ownership model and pattern matching justify its 

### G30 DSL programs as compile-time types vs runtime
- * `team-a-sa16-f007175-q2` — Is hosting a Rust DSL's programs as compile-time types (zero runtime cost, no dynamic loading) worth trading away runtime-loaded/dynamic DSL programs?

### G31 AWS compute: Lambda/FaaS vs containers
- * `team-a-sa17-f007797-q1` — Should a Rust web service targeting AWS be deployed to Lambda or to a long-running container platform (ECS/Fargate)?
-   `team-a-sa24-f011220-q1` — For a latency- and cost-sensitive Rust service, should compute default to serverless functions (Lambda-style FaaS) or to long-running containers (Fargate/ECS, K

### G32 closed set of kinds: enum vs trait objects
- * `team-a-sa17-f007884-q1` — For a value that can be one of several known types, should Rust code use dynamic dispatch (Box<dyn Trait>), a tagged enum, or unsafe unions/tagged-pointer packi
-   `team-a-sa07-f003704-q3` — Should a fixed, closed set of graph node kinds be represented as an enum, or via trait objects/dynamic dispatch?
-   `team-b-sR10-f004741-q3` — Should an extensible policy/configuration surface (e.g. connection access control) be expressed as a closed enum, or as an open trait?

### G33 cross-boundary state: full snapshot vs delta
-   `team-a-sB02-f000256-q4` — Expose the whole simulation state to JS each frame, or only the delta of what changed?
- * `team-a-sa18-f008389-q1` — When a Rust core pushes state changes across an FFI boundary to a declarative native UI (e.g. SwiftUI), should the boundary API return full/partial state snapsh

### G34 thiserror Display drops chain: need anyhow/eyre?
- * `team-a-sa18-f008583-q1` — When logging or wrapping errors in Rust, does `thiserror`'s default `{}` `Display` (which drops the source-error chain) create a real diagnostic gap that needs 
-   `team-b-sb21-f008583-q1` — When you need full error context in structured logs (e.g. the alternate `{:#}` display), does declaring error types with `thiserror` alone suffice, or do you ne

### G35 incremental invalidation redesign
- * `team-a-sa18-f008694-q1` — Should the Rust compiler's/Cargo's incremental-rebuild invalidation be redesigned around explicit "atomic level" targets (AST/HIR/MIR/codegen) plus separately-t

### G36 AI agents change verbose call-site syntax calculus
- * `team-a-sa18-f009104-q2` — Does the rise of AI coding agents change the cost/benefit calculus for verbose, explicit call-site syntax (like named arguments) that was previously judged not 

### G37 scoped trait impls nameable
- * `team-a-sa19-f009123-q1` — Should scoped trait implementations be nameable, or must they stay anonymous?

### G38 timer Instant overflow: panic vs never ready
- * `team-a-sa19-f009196-q2` — When a scheduled timer/interval's next wake time would overflow the maximum representable `Instant`, should the runtime panic or silently never become ready aga

### G39 Polonius narrower formulation vs full parity
- * `team-a-sa20-f009698-q3` — When a new borrow-checker algorithm (Polonius) trades full expressiveness parity with the old implementation for an easier path to production-readiness, should 

### G40 per-trait behavior: proc-macro derives vs runtime reflection
- * `team-a-sa25-f011413-q1` — Should Rust rely on procedural macros as the primary way to generate per-trait behavior, given their compile-time cost, binary bloat, and the build-time capabil
-   `team-a-sa25-f011413-q3` — Should Rust adopt runtime type reflection (shipping structural "shape" data about types at runtime) as an alternative to compile-time code generation, accepting
-   `team-b-sb24-f011413-q1` — For adding new behaviors to Rust types (serialization, debug formatting, diffing, etc.), should each behavior get its own trait plus a dedicated proc-macro deri
-   `team-b-sb24-f011413-q3` — Is trading build-time code generation for runtime reflection actually a good trade for a Rust library, and is JIT-compiling reflection data (via Cranelift) a re

### G41 Rust for high-level rapid prototyping
-   `team-a-sa26-f011305-q1` — should Rust be pushed into high-level, rapid-prototyping application development, or kept to systems/"core" software?
- * `team-a-sa26-f011305-q2` — do Rust's compile times and language rigidity make it less productive than high-level frameworks (React, FastAPI) for rapid prototyping?
- * `team-a-sa26-f012146-q1` — should Rust be pushed into high-level, rapid-prototyping application development, or kept to systems/"core" software? [reusing wording from f011305]

### G42 Rust for AI-written-code future
- * `team-a-sa26-f011443-q2` — is Rust the best-suited language for an AI-driven future where machines write code and humans architect systems (because the compiler independently checks AI-ge

### G43 memory safety as the one hard problem (retrospective)
- * `team-a-sa28-f012469-q3` — Did Rust's design correctly prioritize memory safety as its one "hard problem," and is that tradeoff fair against other capabilities (e.g., metaprogramming/expr

### G44 default async runtime: Tokio vs alternatives
- * `team-a-sa29-f012940-q2` — Is Tokio the async runtime Rust networking/observability applications should standardize on, or is that still contested given the ecosystem's multiple async run
- * `team-b-bk01-f000233-q3` — Which async runtime should a Rust project default to when starting out — or is there an official recommendation at all?
-   `team-b-sb17-f005159-q1` — For an async Rust project needing broad platform support, should Tokio be adopted as the default runtime despite acknowledged criticisms (mature ecosystem, quin

### G45 rust-lang.org AI assistant
- * `team-a-sa29-f013224-q1` — Should rust-lang.org (or official Rust community properties) integrate an AI assistant/LLM feature — semantic search, chat assistant, or interactive tutorials?

### G46 static (generics) vs dynamic (dyn) dispatch
-   `team-a-sB02-f000256-q9` — For code-size-sensitive Rust, prefer generic functions (static dispatch, monomorphized) or trait objects (dynamic dispatch)?
-   `team-b-bk02-f000256-q8` — For code-size-sensitive wasm builds, should generic type-parameterized functions or trait objects be used?
- * `team-a-sa30-f013276-q1` — Should Rust abstraction and dependency injection favor static dispatch (generics) over dynamic dispatch (`dyn Trait`/type erasure), and how narrow are `dyn Trai
-   `team-a-sa07-f003704-q1` — Should a processing pipeline use runtime type erasure with up/down-casting, or a compile-time associated type on the processing trait?

### G47 Rust vs C inherent speed
- * `team-a-saL1-f005516-q1` — Is there an inherent language-level reason for Rust or C to be faster than the other, or does performance mainly reflect non-language factors (codebase age, eng

### G48 replace battle-tested C library with Rust reimplementation
-   `team-b-bk03-f000267-q1` — When should a Rust project reimplement a C/C++ dependency in Rust versus reuse the existing upstream library?
-   `team-a-sa15-f006797-q1` — When a safety-critical C library (image codecs) has decades of fuzzing and battle-testing, does the memory-safety case for migrating it to a less mature Rust cr
-   `team-b-sb19-f005964-q1` — Should legacy C-based TLS stacks (OpenSSL) be replaced by memory-safe Rust implementations (Rustls), now that Rustls claims server-side performance parity or be
- * `team-a-saL1-f005516-q2` — Does old, long-maintained C code tend to be more optimized and reliable ("battle-tested") than newer Rust code simply because of its age?

### G49 depend on existing crate/SDK vs build own
-   `team-a-02-f001053-q1` — For performance-critical, correctness-sensitive infrastructure code, should teams reach for an existing (if less popular) persistent-data-structure crate, or ha
-   `team-a-sa04-f002865-q1` — For a foundational, safety-critical embedded component like an async executor's run queue, should the project depend on an external, well-tested intrusive-data-
-   `team-a-sa14-f005079-q2` — For a small, stable, externally-specified protocol (like systemd's socket-activation environment-variable protocol), should a project vendor its own minimal imp
-   `team-a-sa14-f005079-q3` — For low-level syscall-adjacent operations (fcntl, fstat, getsockname, socket options), should code call into libc directly with manual unsafe blocks, or use a s
- * `team-a-saL2-f011092-q3` — for third-party cloud/vendor integrations in Rust, should a team rely on official vendor SDKs (where they exist), or build lean internal wrapper SDKs given how 
-   `team-b-sR03-f001160-q1` — should a library accept an uglier, more special-cased implementation to avoid growing its dependency footprint (here, avoiding the `syn` "extra-traits" feature)
-   `team-b-sR05-f002453-q1` — should a library accept extra implementation cost/breaking changes to minimize its dependency footprint, or accept more dependencies for convenience/cleanliness

### G50 errors: opaque (anyhow) vs typed enums
- * `team-a-saL2-f011092-q6` — should Rust error handling favor dynamic/opaque error types (anyhow) or structured, typed errors, as a codebase and team mature?
-   `team-b-sb10-f003188-q2` — Should library-facing errors be concrete, enumerable types (e.g. via `thiserror`/`snafu`) rather than a single opaque/type-erased error (`anyhow::Error`)?
-   `team-b-sb10-f003222-q1` — Should library-facing errors be concrete, enumerable types (e.g. via `thiserror`/`snafu`) rather than a single opaque/type-erased error (`anyhow::Error`)?
-   `team-a-sa14-f005149-q1` — For a Rust library, should errors be a single generic catch-all type, or precise per-case enums, given that Rust hasn't stabilized backtrace propagation on erro

### G51 built-in async runtime vs ecosystem
- * `team-b-bk01-f000233-q2` — Should the language provide a built-in async runtime, or leave runtime choice to the crate ecosystem?

### G52 spawn tasks vs join!/select!
- * `team-b-bk01-f000233-q4` — When running multiple futures concurrently, should you spawn separate tasks or compose them in place with `join!`/`select!`?

### G53 CPU-bound/blocking work in async
-   `team-b-bk01-f000233-q5` — Is async Rust (e.g. Tokio) an appropriate choice for CPU-intensive work?
- * `team-b-bk01-f000233-q6` — How should CPU-bound or blocking work be integrated into an async program?
-   `team-b-sb18-f005307-q1` — When your chosen async I/O library (e.g. quinn for QUIC) is paired with a storage/database layer that only offers a synchronous API (as with embedded databases 
-   `team-b-sb18-f005307-q2` — Is it acceptable practice to run blocking synchronous I/O (e.g. database calls) inside a dedicated single-threaded ("current_thread") Tokio runtime on its own O

### G54 abort helper vs unsafe unchecked unwrap
-   `team-a-sB02-f000256-q8` — When avoiding panic-driven code bloat, should Option/Result unwrapping fail safely via process::abort(), or use unsafe unchecked assumption?
- * `team-b-bk02-f000256-q11` — When a value is statically safe to unwrap but the compiler can't prove it, should code use a safe abort-based helper or an unsafe unchecked unwrap?

### G55 portable lib does own I/O vs caller
-   `team-a-sB02-f000256-q11` — Should a portable library crate perform its own I/O and thread spawning, or factor those out to the caller?
- * `team-b-bk02-f000256-q4` — Should a portable library perform its own I/O, or leave I/O to the caller and accept only in-memory data?

### G56 portable crate sync vs async I/O
- * `team-b-bk02-f000256-q5` — Should a portable crate needing I/O expose synchronous or async I/O, and how should it abstract wasm vs native?

### G57 what counts as semver-breaking
- * `team-b-bk03-f000267-q12` — What counts as a semver-breaking change for a published Rust crate's public API?

### G58 intra-doc links vs plain text
- * `team-b-bk03-f000267-q14` — Should Rust doc comments reference types and functions via intra-doc links, or as plain text?

### G59 batch CPU-bound crypto verification
- * `team-b-bk03-f000267-q5` — Should CPU-bound cryptographic verification in an async Rust service be batched for throughput?

### G60 JIT function alignment
- * `team-b-sR04-f001401-q1` — What function/code alignment should a JIT-style code generator use to avoid wasting instruction-fetch bandwidth?

### G61 GPU magic numbers inline vs comptime param
- * `team-b-sR05-f002048-q2` — should hardware/backend-specific magic numbers used in a GPU kernel be hardcoded inline, or threaded through as a comptime-configurable parameter?

### G62 scratch register: explicit param/convention vs encapsulated/type-enforced
-   `team-a-sa05-f002466-q1` — When a temporary/scratch register must cross a function boundary, should its safe use be enforced by the type system (dedicated types, exclusive access), or lef
- * `team-b-sR05-f002466-q1` — should a scratch/temporary resource that the register allocator doesn't track be exposed as an explicit function parameter (composable, flexible), or kept encap

### G63 future variants: non_exhaustive enum vs struct of options
- * `team-b-sR08-f003731-q1` — When a type may need to represent additional variants in the future (e.g. new transport kinds), should it be modeled as a `#[non_exhaustive]` enum of variants, 

### G64 html! imperative control flow
- * `team-b-sR09-f003938-q1` — should a component-templating macro (like Yew's `html!`) support native imperative control flow (`for`, `if`) written inline, or require iterator-adapter/functi

### G65 missing/ambiguous input: fail loudly vs silent default
- * `team-b-sR10-f004706-q1` — When an expected embedded resource (e.g. a static asset) is missing, should the framework fail the build, or degrade silently at runtime (e.g. serve a 404)?
-   `team-a-sa14-f005079-q5` — When a caller's input is ambiguous or partially satisfiable (multiple matching sockets, or a requested feature with no usable input at all), should the code sil
-   `team-b-sb03-f000669-q1` — When a context a handler expects (e.g. `ResponseOptions`) is legitimately missing under load, should the code fall back to a silent safe default, or should the 
-   `team-a-sa14-f004985-q3` — In a long-running service that must never crash on hostile/untrusted input, should a component let a failure propagate and crash the process, or should every bo

### G66 'safe' wrapper sound under all generic instantiations
- * `team-b-sR10-f004804-q1` — When a type wraps an unsafe operation and is labeled "safe," must that safety guarantee hold under every generic instantiation/composition, or is a narrower gua

### G67 debugging CLI one per protocol vs bundle
- * `team-b-sR11-f004947-q1` — Should a debugging CLI for a protocol specialize narrowly, one tool per protocol, or bundle several related protocols into one tool?

### G68 wasm sandbox ambient vs explicit capabilities
- * `team-b-sR11-f005050-q1` — Should a Wasm component sandbox grant capabilities by default (ambient authority), or require every capability — including for middleware and dependencies — to 

### G69 ESP32 RGB display from PSRAM
- * `team-b-sT05-f002499-q1` — How should an ESP32-S3 Rust firmware feed a large RGB (DPI) display from PSRAM framebuffers: cyclic DMA straight from PSRAM, restarted transfers, SRAM bounce bu

### G70 GitHub Discussions keep vs remove
- * `team-b-sT05-f002499-q5` — Should a Rust project keep a GitHub Discussions area for support and design talk, or remove it?

### G71 practitioner adopts binary hot-patching vs plain rebuilds
- * `team-b-sT05-f003044-q3` — Is binary hot-patching (subsecond / `dx serve --hotpatch`) worth adopting over plain cargo rebuilds for iteration speed?
- * `team-b-sb20-f007290-q3` — when a WASM framework offers hot-patching (fast, stateful code reload) that is incompatible with DWARF-based native debugging, should a practitioner enable hot-

### G72 referential integrity: DB FKs vs app code
- * `team-b-sT07-f004166-q2` — On eventually consistent storage, should referential integrity be enforced by database foreign keys or in application code?

### G73 lock wait now vs defer multithreading
- * `team-b-sb03-f000569-q1` — When a resource (a Metal command buffer/lock) needs coordinated access from multiple threads, should the implementation wait on the lock (with a timeout) now, o

### G74 session store client cookie vs server-side
- * `team-b-sb04-f001365-q1` — Should a Rust web framework default new apps to a client-side (encrypted + signed cookie) session store for low-friction onboarding, or push toward a server-sid

### G75 invalid input: panic vs Result
- * `team-b-sb05-f001512-q1` — Should embedded HAL constructors return `Result` instead of panicking (`unwrap`) on invalid configuration?
-   `team-b-sR12-f005421-q1` — Should a library ever panic on invalid input, or should it always signal failure through Result/Option instead? (same disagreement first logged in extract-b1-sR
-   `team-b-sR10-f004573-q1` — Should a numeric operation panic on invalid/unsupported input (e.g. a quantized dtype), and if so, must the panic condition be spelled out in the function's own
-   `team-a-sa21-f011069-q3` — Should a library ever panic ad hoc as a quick bailout, or should panics be reserved for specific cases contingent on control flow?
-   `team-a-sa09-f004055-q3` — For an operation whose safety depends on a runtime-checkable condition (e.g. whether a DMA buffer sits in DMA-accessible memory), should the API perform the che
-   `team-a-sa06-f003414-q3` — Is `unwrap()` acceptable in production code, or should it be reserved for tests and provably-infallible cases?

### G76 typestate vs runtime checks
-   `team-b-sb03-f000715-q1` — Should a driver's mode (blocking vs. async) be encoded in the type system via a typestate generic, so the compiler prevents implementing async traits in blockin
- * `team-b-sb05-f001512-q2` — Should embedded HAL peripheral construction use the type-state pattern to enforce valid configuration at compile time, given the complexity it adds?
-   `team-b-sb24-f011295-q2` — For security-critical code handling cryptographic keys, should key roles and verification status be encoded as distinct types checked at compile time (the types

### G77 write lazy form despite optimizer
- * `team-b-sb05-f001582-q2` — When a compiler backend (LLVM/Cranelift) could optimize an eager computation away, should code still be written in the more efficient/lazy form?

### G78 new similar format: dedicated design vs duplicate-then-refactor
- * `team-b-sb09-f002567-q1` — When adding support for a new but closely related serialization format, should the implementation start as a decoupled, dedicated design or as pragmatic duplica

### G79 tooling: hot-patching vs faster full rebuilds
- * `team-b-sb09-f002719-q1` — To shorten the Rust edit-compile-run loop, should tooling pursue binary/process-level hot-patching (skip rebuilding and relinking) or faster full-rebuild codege
-   `team-a-sa26-f011305-q5` — should a hot-reload/hot-patch mechanism bypass the normal cargo build/linking pipeline to get near-instant iteration, even at the cost of many platform-specific

### G80 merge ad hoc special case now vs general mechanism first
- * `team-b-sb09-f003052-q1` — When migrating a compiler backend to a new, more systematic instruction-assembler abstraction, and an instruction needs special-cased handling (e.g. custom flag

### G81 strictly additive features
- * `team-b-sb10-f003186-q1` — Should a crate's Cargo feature flags always be strictly additive (the crate builds with any subset of features, including none), or is it acceptable for disabli

### G82 pre-1.0 canary breaking releases vs hold
- * `team-b-sb10-f003188-q1` — Before a crate's 1.0 release, should breaking changes ship frequently in a fast pre-release ("canary") channel to get user feedback quickly, or should a team ho

### G83 same-state transition no-op vs trigger
- * `team-b-sb14-f004398-q2` — For a component that triggers on a state-machine transition matching a predicate, should a transition into the same state the entity is already in be treated as

### G84 project policy on AI-assisted contributions
- * `team-b-sb15-f004721-q1` — When a contributor's PR description and review replies read as substantially AI-drafted, should maintainers require the human author to demonstrably stay person
-   `team-b-bk03-f000267-q6` — What should a Rust project's policy be on AI-assisted contributions?
-   `team-b-sR11-f004993-q1` — Should a Rust open-source project accept AI-assisted contributions, and how should that be policed?
-   `team-b-sR13-f009740-q1` — How should a Rust project respond to AI-generated contributions/proposals in its community processes?
-   `team-a-sa29-f013224-q2` — Is it acceptable to compose a community forum post or proposal using an LLM rather than in the poster's own words?

### G85 cancel-safety required vs caller's problem
- * `team-b-sb17-f005159-q4` — For an async mpmc channel crossing the sync/async boundary, should cancel-safety on `recv` be treated as a non-negotiable requirement (ruling out otherwise-attr
-   `team-a-sT04-f001650-q1` — Must async Rust APIs such as RPC channels be cancel-safe, with a missing guarantee treated as a bug, or is cancel-safety a caller responsibility to be documente

### G86 C maintainers' duty to Rust bindings
- * `team-b-sb18-f005332-q1` — When a C-subsystem maintainer changes their C code in a way that breaks the corresponding Rust abstraction/bindings, should the C maintainer be expected to help

### G87 Mutex vs lock-free atomics
- * `team-b-sb18-f005600-q1` — In concurrent Rust systems, should hand-written locks (`Mutex`) be avoided in favor of atomics/compare-and-swap-based (lock-free) data structures — on the reaso
-   `team-a-sa17-f007846-q1` — For shared mutable state on a hot parallel path in Rust, should code use a Mutex or a lock-free approach (atomics)?

### G88 Rust+wasm vs JS for browser compute
- * `team-b-sb19-f005699-q1` — For a given workload, does compiling Rust to WASM for browser execution actually beat a pure JS/TypeScript implementation, once the JS↔WASM boundary cost is cou
-   `team-a-sa26-f011460-q1` — is JavaScript "fast enough" for typical web workloads, making Rust+Wasm unnecessary outside of the heaviest-compute applications?
-   `team-a-sa26-f011460-q2` — should WebAssembly be reserved for heavy-compute workloads only, or is it competitive even for small, string-heavy, low-computation functions?
-   `team-b-sR01-f000256-q1` — Why (if at all) should Rust be chosen over JavaScript as a WebAssembly compile target?

### G89 affine types sufficient vs formal verification
- * `team-b-sb19-f005743-q2` — Does Rust's affine-type system provide sufficient correctness guarantees, or is further formal verification (linear/dependent types, model checkers) needed on t

### G90 'memory safety' vs 'correctness' frame
- * `team-b-sb19-f005743-q3` — Is "memory safety" the right frame for language-correctness discourse, or is "correctness" (of which memory safety is one part) the property that actually matte

### G91 lifetime params on structs vs owned
- * `team-b-sb20-f007364-q1` — should structs/enums carry lifetime parameters (borrowed data) to avoid heap allocation and copying, or should you avoid putting lifetime parameters on structs,
- * `team-b-sb20-f007608-q2` — should structs/enums carry lifetime parameters (borrowed data), or should you avoid putting lifetime parameters on structs, as a rule of thumb?

### G92 object soup representation
- * `team-b-sb20-f007608-q1` — how do you represent a mutable, cyclic, many-to-many object graph ("object soup") in Rust: `Rc<RefCell<T>>`/`Arc<Mutex<T>>`, raw/unsafe pointers, or an index-in
- * `team-b-sb26-f013214-q3` — how do you represent a mutable, cyclic, many-to-many object graph ("object soup") in Rust: `Rc<RefCell<T>>`/`Arc<Mutex<T>>`, raw/unsafe pointers, or an index-in

### G93 GUI bespoke DSL vs plain Rust
- * `team-b-sb21-f008390-q2` — Should a Rust GUI framework define UI structure through a bespoke DSL with dedicated tooling (Slint's own language, Makepad's `live_design!` macro), or should i

### G94 immediate vs retained/Elm GUI
- * `team-b-sb21-f008390-q3` — For typical small-to-medium desktop UIs, does the immediate-mode vs. retained-mode GUI architecture choice actually matter, or is it a difference that only show
-   `team-a-sa15-f005857-q1` — For a real-time, stateful interactive Rust desktop app (synchronized audio playback + canvas redraw + UI), is a message-passing/subscription (Elm-style) GUI arc

### G95 follow std naming convention (as_/to_/into_, raw_parts) when fit inexact
- * `team-b-sb22-f009236-q1` — for a trait whose one method converts a value into a different representation of the same underlying type (e.g. `ToOwned::to_owned`), should the trait/method fo
-   `team-b-sR08-f003587-q2` — Should a method be named `into_foo` only when it actually consumes `self` (Rust's `into_`/`as_`/`to_` naming convention), or can `into_` be used more loosely?
-   `team-b-sR05-f002326-q1` — should a crate's naming for a raw-pointer-plus-length accessor follow std's `raw_parts`/`from_raw_parts` convention even where the analogy is imperfect (no matc

### G96 wasm undefined symbols hard error
- * `team-b-sb23-f009737-q1` — Should Rust's WebAssembly targets treat undefined symbols as a hard link error by default (matching native platforms), even though some code intentionally relie

### G97 std::simd nightly vs stable intrinsics
- * `team-b-sb23-f011233-q2` — For performance-sensitive numeric code, should Rust developers prefer the ergonomic, nightly-only `std::simd` portable-SIMD API over stable but manual target-fe

### G98 trace context: LD_PRELOAD vs eBPF
- * `team-b-sb24-f011306-q3` — For propagating distributed-trace context (W3C trace-context HTTP headers) across a network boundary without modifying application code, should you use library 

### G99 C++ binding tool
- * `team-b-sb24-f011312-q1` — For binding a large existing C++ API surface to Rust, should you use a low-level C-ABI-only generator (bindgen/cbindgen), a manually-declared bridge macro with 

### G100 function overloading in Rust
- * `team-b-sb24-f011312-q6` — Should Rust add built-in function overloading (at least for FFI/interop purposes), given it has historically avoided overloading in favor of traits, generics, a
-   `team-a-sa18-f009104-q1` — Should Rust adopt call-site ergonomics features common in other languages — named parameters, optional/default arguments, function overloading — or does the sim

### G101 ECS events/observers-first vs direct mutation
- * `team-b-sb25-f012561-q1` — In a growing Bevy/ECS game, should cross-system state changes flow through an events/observers-first architecture (systems never mutate each other's state direc

### G102 ECS: big vs many small systems
- * `team-b-sb25-f012561-q3` — For complex UI built on an ECS with an immediate-mode UI library (egui), should you write large systems with many queries in one place (simpler control flow, bu

### G103 scripting owns logic vs Rust owns state
- * `team-b-sb26-f013214-q4` — when a Rust game engine embeds a scripting/modding language, should most game logic live in the hosted scripting language itself, or should Rust own the state w

## Would remove (not a Question under the rule)

- `team-a-sa11-f004512-q3` — stopgap-vs-proper / YAGNI Value trade-off
- `team-b-sb09-f003052-q1` — stopgap vs proper fix (named Value trade-off)
- `team-a-sa28-f012469-q3` — retrospective on language design, no practitioner choice
- `team-b-sb19-f005743-q3` — discourse framing, no practitioner choice
- `team-b-bk03-f000267-q12` — knowledge question, no alternatives

Borderline, kept:
- `team-a-sa18-f009104-q2` — belief about AI changing a calculus
- `team-a-saL1-f005516-q1` — empirical belief, no alternatives
- `team-a-saL1-f005516-q2` — empirical belief; grouped with G48 as its underlying dispute

## Sample list

S1 `team-a-01-f000530-q1`
S2 `team-a-01-f000543-q1`
S3 `team-a-02-f001181-q1`
S4 `team-a-02-f001231-q1`
S5 `team-a-sB01-f000217-q4`
S6 `team-a-sB02-f000256-q10`
S7 `team-a-sB02-f000256-q12`
S8 `team-a-sB02-f000256-q3`
S9 `team-a-sB02-f000256-q6`
S10 `team-a-sR04-f001096-q2`
S11 `team-a-sR05-f001981-q2`
S12 `team-a-sR06-f001989-q1`
S13 `team-a-sR06-f002005-q1`
S14 `team-a-sR06-f002005-q2`
S15 `team-a-sR07-f002271-q1`
S16 `team-a-sR08-f003033-q1`
S17 `team-a-sR11-f004170-q1`
S18 `team-a-sR13-f004586-q3`
S19 `team-a-sR16-f012642-q1`
S20 `team-a-sT04-f001319-q1`
S21 `team-a-sT08-f004169-q1`
S22 `team-a-sT11-f007659-q2`
S23 `team-a-sT12-f008237-q1`
S24 `team-a-sT12-f008455-q1`
S25 `team-a-sa02-f002124-q1`
S26 `team-a-sa03-f002243-q1`
S27 `team-a-sa04-f002554-q1`
S28 `team-a-sa11-f004512-q3`
S29 `team-a-sa14-f005454-q1`
S30 `team-a-sa15-f005948-q1`
S31 `team-a-sa16-f007175-q2`
S32 `team-a-sa17-f007797-q1`
S33 `team-a-sa17-f007884-q1`
S34 `team-a-sa18-f008389-q1`
S35 `team-a-sa18-f008583-q1`
S36 `team-a-sa18-f008694-q1`
S37 `team-a-sa18-f009104-q2`
S38 `team-a-sa19-f009123-q1`
S39 `team-a-sa19-f009196-q2`
S40 `team-a-sa20-f009698-q3`
S41 `team-a-sa25-f011413-q1`
S42 `team-a-sa26-f011305-q2`
S43 `team-a-sa26-f011443-q2`
S44 `team-a-sa26-f012146-q1`
S45 `team-a-sa28-f012469-q3`
S46 `team-a-sa29-f012940-q2`
S47 `team-a-sa29-f013224-q1`
S48 `team-a-sa30-f013276-q1`
S49 `team-a-saL1-f005516-q1`
S50 `team-a-saL1-f005516-q2`
S51 `team-a-saL2-f011092-q3`
S52 `team-a-saL2-f011092-q6`
S53 `team-b-bk01-f000233-q2`
S54 `team-b-bk01-f000233-q3`
S55 `team-b-bk01-f000233-q4`
S56 `team-b-bk01-f000233-q6`
S57 `team-b-bk02-f000256-q11`
S58 `team-b-bk02-f000256-q4`
S59 `team-b-bk02-f000256-q5`
S60 `team-b-bk02-f000256-q7`
S61 `team-b-bk03-f000267-q12`
S62 `team-b-bk03-f000267-q14`
S63 `team-b-bk03-f000267-q5`
S64 `team-b-sR04-f001401-q1`
S65 `team-b-sR05-f002048-q2`
S66 `team-b-sR05-f002466-q1`
S67 `team-b-sR08-f003731-q1`
S68 `team-b-sR09-f003938-q1`
S69 `team-b-sR10-f004706-q1`
S70 `team-b-sR10-f004804-q1`
S71 `team-b-sR11-f004947-q1`
S72 `team-b-sR11-f005050-q1`
S73 `team-b-sT05-f002499-q1`
S74 `team-b-sT05-f002499-q5`
S75 `team-b-sT05-f003044-q3`
S76 `team-b-sT07-f004166-q2`
S77 `team-b-sb03-f000569-q1`
S78 `team-b-sb04-f001365-q1`
S79 `team-b-sb05-f001512-q1`
S80 `team-b-sb05-f001512-q2`
S81 `team-b-sb05-f001512-q3`
S82 `team-b-sb05-f001582-q2`
S83 `team-b-sb09-f002567-q1`
S84 `team-b-sb09-f002719-q1`
S85 `team-b-sb09-f003052-q1`
S86 `team-b-sb10-f003186-q1`
S87 `team-b-sb10-f003188-q1`
S88 `team-b-sb14-f004398-q2`
S89 `team-b-sb15-f004721-q1`
S90 `team-b-sb17-f005159-q4`
S91 `team-b-sb18-f005332-q1`
S92 `team-b-sb18-f005600-q1`
S93 `team-b-sb19-f005699-q1`
S94 `team-b-sb19-f005743-q2`
S95 `team-b-sb19-f005743-q3`
S96 `team-b-sb20-f007290-q3`
S97 `team-b-sb20-f007364-q1`
S98 `team-b-sb20-f007608-q1`
S99 `team-b-sb20-f007608-q2`
S100 `team-b-sb21-f008390-q2`
S101 `team-b-sb21-f008390-q3`
S102 `team-b-sb21-f008793-q1`
S103 `team-b-sb22-f009236-q1`
S104 `team-b-sb23-f009737-q1`
S105 `team-b-sb23-f011233-q2`
S106 `team-b-sb24-f011306-q3`
S107 `team-b-sb24-f011312-q1`
S108 `team-b-sb24-f011312-q6`
S109 `team-b-sb25-f012561-q1`
S110 `team-b-sb25-f012561-q3`
S111 `team-b-sb26-f013214-q3`
S112 `team-b-sb26-f013214-q4`
