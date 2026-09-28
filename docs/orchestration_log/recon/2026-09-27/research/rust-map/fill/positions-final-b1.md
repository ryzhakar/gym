# Positions, final, batch 1

Resolved from blind fills A and B plus a third blind fill (t4-fill-resolve-b1, 2026-09-28). Claim lists come from `resolved-b1.csv` (status agree or majority); an `unresolved` row is in no Position. Tag votes read A / B / third; third is blank where A and B agreed.

## Question `absolute-instant-periodic-timing`

### absolute-instant-periodic-timing--p1 — Accumulate absolute instant to avoid drift

Summary: A periodic wait computed from a delayed loop iteration accumulates extra delay from the work done each cycle; accumulating a stored absolute instant and delaying until `previous + period` instead of `now + period` keeps the loop on schedule instead of drifting later with every iteration.

Summary source: run-b, tie on share of the Claims' quoted words (0.29), shorter summary.

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: a-sB04-f000227-c2

## Question `actor-vs-shared-locks`

### actor-vs-shared-locks--p1 — Remove the actor; use lock-based data structures

Summary: An actor around connection management is an unnecessary indirection layer; removing it in favor of higher-order shared data structures with locks cuts that layer, at the cost of a follow-up fix for a deadlock the change introduced.

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sT05-f002550-c2

## Question `ad-hoc-special-case-vs-general-mechanism`

### ad-hoc-special-case-vs-general-mechanism--p1 — Resist ad hoc design general solution first

Summary: Adding another special-cased mechanism on top of an already-unfortunate special case ("can of worms") should be resisted; the right move is to think through a better long-term, general solution before merging.

Summary source: run-a, higher share of the Claims' quoted words (0.60 vs 0.47).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb09-f003052-c1

### ad-hoc-special-case-vs-general-mechanism--p2 — Merge as is and refactor later

Summary: The special case can land now and the redesign can follow, sequenced behind a related refactor already in flight (an external "custom" printing mechanism); rebasing on that later is preferred to blocking the current PR on an inline redesign.

Summary source: run-b, higher share of the Claims' quoted words (0.24 vs 0.12).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb09-f003052-c2, b-sb09-f003052-c3

## Question `additive-features`

### additive-features--p1 — Features must stay additive

Summary: A feature flag like `std` should never be required just to build the crate on ordinary targets (e.g. Linux/Windows); if disabling a feature breaks the build, that defeats the purpose of feature gating and the accompanying CI changes shouldn't have been necessary in the first place.

Summary source: run-a, higher share of the Claims' quoted words (0.82 vs 0.27).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb10-f003186-c1

### additive-features--p2 — Disabling a feature can change buildability

Summary: A fix can intentionally disable standard-library-dependent features for dependents that build with `default-features = false`, accepting that this changes what builds successfully under that configuration.

Summary source: run-a, higher share of the Claims' quoted words (0.88 vs 0.62).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb10-f003186-c2

## Question `affine-types-vs-formal-verification`

### affine-types-vs-formal-verification--p1 — Needs stronger formal guarantees

Summary: Rust's affine types do not offer the same guarantees as linear types combined with dependent types; the type system alone is weaker than what those stronger formal systems would provide.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.86).

Tag: tradeoff (majority; votes fact / tradeoff / tradeoff)

Claims: b-sb19-f005743-c4

### affine-types-vs-formal-verification--p2 — Combine rust with formal tools

Summary: Integrated model checkers (e.g. Frama-C, including a Rust port such as TrustInSoft's) sit alongside Rust's affine-type checking rather than replacing it; using such tools is "not mutually exclusive with the use of Rust."

Summary source: run-b, tie on share of the Claims' quoted words (0.69), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb19-f005743-c5, b-sb19-f005743-c6

## Question `ai-agents-and-explicit-syntax`

### ai-agents-and-explicit-syntax--p1 — Agents shift calculus toward explicit named syntax

Summary: Coding agents change the calculus that previously judged explicit named-argument syntax not worth its typing cost: once "I'm not typing myself anymore," the verbosity cost drops out and the call-site clarity benefit remains, arguably larger for an agent reading the call than for a human — though no real evals have been run on this yet.

Summary source: run-b, tie on share of the Claims' quoted words (0.20), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa18-f009104-c3

## Question `ai-authored-community-contributions`

### ai-authored-community-contributions--acceptable-if-marked — Assistance is fine; unmarked AI content is the problem

Summary: Assistance from AI tools is not itself a problem; clearly marked AI-generated content generally isn't going to cause trouble under forum rules aimed at unmarked, low-effort AI spam.

Summary source: run-a, tie on share of the Claims' quoted words (0.78), shorter summary.

Tag: taste (majority; votes taste / tradeoff / taste)

Claims: a-sa29-f013224-c6

### ai-authored-community-contributions--acceptable-if-substance-is-own — Acceptable when the substance is the contributor's own and the model only composes

Summary: Using an LLM to write up a contribution is fine when the contributor supplied the substance — the points, the thinking — and the model only composed the prose; writing this kind of communication isn't everyone's strength, and that division of labor is not itself a problem.

Summary source: run-b, only run whose summary covers the final Claims.

Tag: taste (majority; votes taste / tradeoff / taste)

Claims: a-sa29-f013224-c5

### ai-authored-community-contributions--human-must-stay-accountable — Acceptable only with the human author in the loop and accountable, per project policy

Summary: A contribution that reads as a large wall of AI-generated text is flagged directly to its author, who is told to consult the project's AI-tool-use policy and, regardless of that policy's details, to stay personally in the loop on all communication because they own the change and are responsible for it.

Summary source: run-b, higher share of the Claims' quoted words (0.57 vs 0.36).

Tag: taste (majority; votes taste / tradeoff / taste)

Claims: b-sb15-f004721-c1

### ai-authored-community-contributions--manage-through-review-not-ban — A real problem, but managed through review and policy, not a ban

Summary: A strict no-AI ban solves some problems but creates others — toxic witch hunts over suspected AI use, incentives to lie to maintainers, and an enforcement burden that's close to impossible — so projects are moving toward managing AI-generated proposals through review and policy instead of a blanket ban, treating the volume of low-quality AI submissions as a manageable, ongoing cost rather than a reason to prohibit them outright.

Summary source: run-a, higher share of the Claims' quoted words (0.48 vs 0.35).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR11-f004993-c1, b-sR13-f009740-c1

### ai-authored-community-contributions--p1 — Welcome with disclosure and accountability

Summary: AI-assisted contributions are welcome; what decides acceptance is the quality of the result and the contributor's own understanding of it, not whether AI was involved, provided the AI usage is disclosed in the PR description and the human contributor remains the sole responsible author, able to explain the logic and trade-offs of every change.

Summary source: run-b, only run with a summary.

Tag: unresolved (one run tradeoff, third taste, other run had no summary; votes - / tradeoff / taste)

Claims: b-bk03-f000267-c6

### ai-authored-community-contributions--reject-ai-authored-content — Undesirable: it erases the author's voice, or readers do not want it

Summary: AI-authored material in community venues is unwanted on its own terms: an obviously LLM-styled proposal reads as prompted toward a predetermined conclusion, and a newsletter's own readers, surveyed directly, say plainly they do not want anything in it generated by AI.

Summary source: run-b, tie on share of the Claims' quoted words (0.24), shorter summary.

Tag: taste (majority; votes taste / tradeoff / taste)

Claims: a-sa29-f013224-c4, b-sb20-f007942-c1

## Question `ai-review-suggestions`

### ai-review-suggestions--p1 — Critically evaluate not blindly follow

Summary: An AI code-review tool's suggestions are noise as often as signal: a Copilot comment telling an author to avoid a harmless pattern is dismissed outright, while attention is redirected to a real, unsupported-configuration bug the AI reviewer missed entirely — the suggestions are evaluated on their merits, not followed by default.

Summary source: run-b, higher share of the Claims' quoted words (0.12 vs 0.00).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR08-f003550-c1

## Question `all-rust-vs-platform-native-tooling`

### all-rust-vs-platform-native-tooling--all-rust — Write it in Rust (the `jni` crate, `objc2`, `wasm-bindgen-test`)

Summary: The glue and test code at the platform boundary can be written entirely in Rust — JNI functions following the `Java_<package>_<class>_<method>` convention with no C++ intermediary, native Objective-C calls via `objc2` instead of writing objc, and pure-Rust `wasm-bindgen-test` E2E harnesses — specifically to avoid adding non-Rust dependencies like C++, Playwright, Cypress or Selenium to the pipeline.

Summary source: run-a, higher share of the Claims' quoted words (0.54 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sT12-f008455-c1, b-sb13-f004367-c1, b-sb22-f008914-c1

### all-rust-vs-platform-native-tooling--all-rust-workable-not-production — All-Rust is workable but brittle, not production-ready (iOS XCTest)

Summary: An all-Rust XCTest harness — bundling both the app and a `#![no_main]` XCTest bundle built from `objc2` bindings — genuinely works, driving UI automation and coverage without ever opening Xcode, but exit-status detection is unreliable, on-device behavior is unclear, and the whole setup is "pretty brittle," not something its author is sure he'd suggest for production.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.67).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb21-f008793-c1

### all-rust-vs-platform-native-tooling--platform-native-glue — Write the glue in the platform's language for its tooling (C++ JNI in Android Studio)

Summary: Even where many guides write both the FFI and JNI layers in Rust, writing the JNI side in the platform's own language (C++) instead lets the platform's native tooling — code generation, build automation, code analysis, jump-to-declaration in Android Studio — keep working across the boundary, at the cost of one extra language in the project.

Summary source: run-b, higher share of the Claims' quoted words (0.88 vs 0.12).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb20-f007678-c1

## Question `api-handler-as-async-trait`

### api-handler-as-async-trait--p1 — Define API endpoints via async traits decoupled from implementation

Summary: Defining an HTTP API's handlers via an async trait decoupled from any concrete implementation lets tooling extract API/schema information without needing a real implementation to be compiled, or even present at all; the hope is that more Rust projects adopt this pattern generally.

Summary source: run-a, higher share of the Claims' quoted words (0.76 vs 0.65).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sa14-f005454-c3

## Question `api-schema-spec-first-vs-code-first`

### api-schema-spec-first-vs-code-first--p1 — Generate the OpenAPI spec from code, not code from the spec

Summary: Don't hand-write the OpenAPI spec and rely on a programmer to keep it current; have the API server generate the spec from its own code instead, so code is the source of truth and the generated spec provably cannot diverge from the implementation that produced it.

Summary source: run-a, higher share of the Claims' quoted words (0.60 vs 0.44).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sa14-f005454-c1, a-sa23-f011186-c1

## Question `async-by-default-host-interfaces`

### async-by-default-host-interfaces--p1 — Async by default

Summary: WASIp3's async I/O model, previously experimental and opt-in, is now the default platform for new applications, and a framework's own host interfaces (KV, SQLite, Postgres, Redis, outbound HTTP) get rewritten to be async so that I/O-heavy handlers get real concurrency instead of blocking the instance.

Summary source: run-a, higher share of the Claims' quoted words (0.80 vs 0.73).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR10-f004809-c1

## Question `async-drop-raii-vs-close`

### async-drop-raii-vs-close--explicit-close-required — Require an explicit async close; `Drop` is best effort only

Summary: Without reliable async `Drop`, an async resource should require an explicit async close — an endpoint no longer attempts to gracefully close connections when merely dropped; callers must `await` `close()` themselves before dropping the last instance, and that explicit close path is made cheap (near-instant when the peer already closed, about one RTT otherwise) so it functions as the primary, first-class shutdown mechanism.

Summary source: run-a, higher share of the Claims' quoted words (0.59 vs 0.47).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR10-f004423-c1, b-sR10-f004741-c1

### async-drop-raii-vs-close--preserve-raii-with-workarounds — Keep RAII, working around the missing async Drop

Summary: RAII shouldn't be given up on for async resources; an async shutdown function can offer a gentle, explicit path, but every entity should still attempt cleanup on `Drop` as well, so cleanup isn't solely dependent on callers remembering to call close.

Summary source: run-a, tie on share of the Claims' quoted words (0.60), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb17-f005159-c2

## Question `async-fn-in-traits-cost`

### async-fn-in-traits-cost--p1 — Acceptable for most applications; avoid in hot low-level public APIs

Summary: Using `async fn` in traits (via the `async-trait` crate or async-fn-in-trait) costs a heap allocation per call, but that cost is not significant for the vast majority of applications; it should only be weighed carefully when exposing the pattern in the public API of a low-level function expected to be called millions of times a second.

Summary source: run-a, tie on share of the Claims' quoted words (0.67), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-bk01-f000233-c14

## Question `async-for-cpu-bound-work`

### async-for-cpu-bound-work--p1 — Qualified yes, against the "never use async for CPU work" meme

Summary: The common claim that async Rust (Tokio) should simply never be used for CPU-intensive work is an over-simplification; the real constraint is that mixing IO-bound/latency-sensitive tasks with CPU-bound/long-running tasks on the same runtime needs special handling, not blanket avoidance of async.

Summary source: run-a, tie on share of the Claims' quoted words (0.86), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-bk01-f000233-c6

## Question `async-hook-cancellation-upfront`

### async-hook-cancellation-upfront--p1 — Ship minimal now

Summary: A young, not-yet-stable API can ship without committing to cancellation semantics up front when the design already covers the large majority of use cases; the cancellation decision is better postponed until real usage demonstrates an actual need, at which point it can be added as a variant.

Summary source: run-b, higher share of the Claims' quoted words (0.36 vs 0.29).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-02-f000957-c1

## Question `async-io-with-sync-storage`

### async-io-with-sync-storage--p1 — Incompatible deps should be avoided

Summary: Pairing an async I/O library (e.g. quinn for QUIC) with a storage layer that only offers a synchronous API is an avoidable, foreseeable architecture mismatch; the right response is to have looked for a different, more compatible dependency rather than accepting the pairing.

Summary source: run-a, tie on share of the Claims' quoted words (0.44), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb18-f005307-c1

### async-io-with-sync-storage--p2 — Sync storage is unavoidable given available options

Summary: Sync-only storage isn't a foreseeable design error to avoid — every in-process embedded database evaluated (rocksdb, redb, sled, sqlite) exposes a synchronous API, so there is no viable async-native alternative to switch to, and non-`Send` futures are often unavoidable once a future has to capture a non-`Send` database or transaction handle.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb18-f005307-c2

## Question `async-rust-production-ready`

### async-rust-production-ready--p1 — Reliable despite rough edges

Summary: Stable async Rust is reliable and performant and is used in production in some of the most demanding situations at the largest tech companies; the rough edges that remain sit in ergonomics — async iterators and streams, async in traits, async destruction — not in reliability.

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: b-sR01-f000233-c2

## Question `async-transport-asyncread-vs-sink-stream`

### async-transport-asyncread-vs-sink-stream--p1 — Build the transport abstraction against `AsyncRead`/`AsyncWrite`, not `Sink`/`Stream`

Summary: Available open-source WebSocket-over-async libraries built on `Sink`/`Stream` do not jointly satisfy `Send`, `Sync` and `Unpin` the way a multi-threaded async runtime needs; rather than adopt one of them, a custom translation layer is written so the whole handler stays generic over `AsyncRead`/`AsyncWrite` streams instead.

Summary source: run-b, tie on share of the Claims' quoted words (0.23), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sa03-f002236-c1

## Question `async-vs-threads`

### async-vs-threads--async-for-io-wait-and-no-os — Async where work waits on I/O or there is no OS

Summary: Async programming is a good fit for systems that need to handle very many concurrent tasks where those tasks spend a lot of their time waiting (e.g. on client responses or other IO), and it also fits microcontrollers with very limited memory that have no OS-provided threads to fall back on.

Summary source: run-a, higher share of the Claims' quoted words (0.92 vs 0.85).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sR01-f000233-c1

### async-vs-threads--async-tasks-on-embedded — Async tasks compiled to static executors beat manual task splitting on embedded

Summary: On embedded targets, async/await's ergonomics gain is compatible with strict resource requirements too: the compiler forbids awaiting while holding a resource (preserving priority-ceiling-style guarantees), and compile-time-generated static executors avoid dynamic allocation altogether, so there's no risk of an out-of-memory panic the way a heap-allocating task model would have.

Summary source: run-a, tie on share of the Claims' quoted words (0.33), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sR01-f000227-c2

### async-vs-threads--p1 — Async/await preferred for ergonomics over manual state-machine sub-tasking

Summary: Without async/await, a programmer has to manually split a task into sub-tasks and track its state by hand; async/await brings "improved ergonomics" by having the compiler build that state-progression mechanism automatically via Futures instead.

Summary source: run-a, tie on share of the Claims' quoted words (0.67), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB01-f000227-c3

### async-vs-threads--p2 — Async for large numbers of (esp. IO-bound) tasks and constrained environments; plain threads otherwise

Summary: Asynchronous programming is "not better than threads, but different": OS threads need no new programming model, let existing synchronous code run unchanged, and support OS-level thread-priority tuning, but carry real per-thread CPU/memory overhead; async supports orders of magnitude more concurrent tasks for the same overhead, especially for IO-bound work like servers and databases, and — being zero-cost with no required heap allocation or dynamic dispatch — can run in constrained environments like embedded systems, at the cost of larger compiled binaries and a bundled runtime; use threads if you don't need async's performance benefits.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.80).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-bk01-f000233-c11

## Question `aya-vs-libbpf-rs`

### aya-vs-libbpf-rs--p1 — No strong preference used libbpf rs for familiarity

Summary: Between a pure-Rust eBPF toolchain (Aya) and a Rust wrapper around the native C `libbpf` library with the eBPF program itself in C (libbpf-rs), the choice made here is libbpf-rs "for no specific reason," explicitly declining to take a side or judge either project's maintainers.

Summary source: run-b, higher share of the Claims' quoted words (0.21 vs 0.11).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb24-f011306-c2

## Question `batch-crypto-verification`

### batch-crypto-verification--p1 — Batch verify for throughput

Summary: Contemporaneous cryptographic verification requests are batched automatically and transparently rather than verified one at a time, because serial, one-block-at-a-time verification is too slow during initial chain sync; data dependencies are deferred so signature, proof and script verification can be parallelized.

Summary source: run-b, tie on share of the Claims' quoted words (0.38), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-bk03-f000267-c5

## Question `batteries-included-web-framework`

### batteries-included-web-framework--batteries-included — Use or build a convention-over-configuration, batteries-included framework

Summary: Rust's existing minimalist web/backend frameworks and SPA frameworks each still require substantial manual wiring — routing, templates, auth, database access, admin — across separate libraries; the ecosystem instead needs a single, integrated, batteries-included framework that handles it all with clean upgrade paths between versions, in the spirit of Rails/Django/Spring.

Summary source: run-a, higher share of the Claims' quoted words (0.70 vs 0.60).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb19-f005872-c1

## Question `become-tail-call-codegen`

### become-tail-call-codegen--alt1 — Poor or inconsistent codegen on other targets (x86-64, Wasm)

Summary: The nightly `become` tail-call feature's codegen quality is target-dependent: on ARM64 (M1) the tail-call interpreter beats both the plain VM and hand-written ARM64 assembly, but on x86-64 it beats the VM while still losing to hand-written assembly, and compiled to WASM it runs 1.2–4.6x slower than the plain VM across Firefox, Chrome and wasmtime, attributed to codegen (register spills to the stack) not translating well to the WASM stack machine.

Summary source: run-a, only run with a summary.

Tag: fact (agree (one run + third; other run summarised no claim here); votes fact / - / fact)

Claims: a-sa15-f005821-c1

## Question `behavioral-equivalence-testing-method`

### behavioral-equivalence-testing-method--p1 — Unit and integration tests insufficient

Summary: Unit tests and integration tests are rejected as sufficient for verifying that a rewritten system preserves an emergent, hard-to-specify effect: the divergence only shows up late in long play sessions, no single fixed tolerance holds everywhere, and one integration test's pass or fail cannot be extrapolated to the whole game.

Summary source: run-b, tie on share of the Claims' quoted words (0.00), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa21-f011069-c1

### behavioral-equivalence-testing-method--p2 — Naive property based testing insufficient

Summary: Naive property-based (fuzz) testing is rejected as inadequate on its own: the relevant input space (keyboard holds, frame counts, continuous mouse movement) grows exponentially, and pure random search produces inputs "a human would not even be capable of producing," yielding many false negatives against the goal of preserving a human-discoverable exploit.

Summary source: run-b, tie on share of the Claims' quoted words (0.29), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa21-f011069-c2

### behavioral-equivalence-testing-method--p3 — Heuristic guided rl search preferred

Summary: The right approach is a heuristic-constrained, Markov-process-style reinforcement-learning search biased toward human-plausible inputs, treating "the exploit stays reachable within human-plausible effort" as the correctness criterion instead of exact input/output matching.

Summary source: run-a, tie on share of the Claims' quoted words (0.57), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa21-f011069-c3

## Question `benchmark-colocation-with-crate`

### benchmark-colocation-with-crate--p1 — Colocate benchmark with owning crate

Summary: When a function moves to a different crate in a multi-crate workspace, its benchmark should move with it into the crate that now defines the function; use `git mv` on the move to preserve the file's history.

Summary source: run-a, higher share of the Claims' quoted words (0.43 vs 0.29).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sR04-f001096-c2

## Question `bitflags-vs-generated-variants`

### bitflags-vs-generated-variants--p1 — Bitflags preferred

Summary: Combinatorial pipeline state is better represented as bitflags than as an explicit bool-per-combination approach: bit flags take a lot less space and are arguably clearer when using named constants, such as those the bitflag crate offers.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.82).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb01-f000493-c1

### bitflags-vs-generated-variants--p2 — Explicit array generation

Summary: The two approaches are mostly equivalent in principle, but at a larger combination count (32 versus a prior case of 6) hand-enumerating every combination becomes too daunting, which is the specific reason to generate the array of variants in code instead.

Summary source: run-a, higher share of the Claims' quoted words (0.33 vs 0.25).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb01-f000493-c2

## Question `blocking-work-in-async`

### blocking-work-in-async--p1 — Match mechanism to work shape

Summary: The mechanism should match the shape of the work: use `spawn_blocking` for blocking I/O, use `std::thread::spawn` rather than a thread-pool slot for a thread that will run forever, and reach for a dedicated thread pool (e.g. Rayon) or a second async runtime for sustained CPU-bound work — accepting a plain dedicated thread or `spawn_blocking` as an easy, if suboptimal, choice when performance needs are modest.

Summary source: run-b, tie on share of the Claims' quoted words (0.70), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-bk01-f000233-c7

### blocking-work-in-async--p2 — single-threaded-runtime-fine-for-n1-scheduling

Summary: A warning against ever using Tokio's single-threaded runtime except when no OS threads are available is simply wrong: if the goal is N:1 scheduling of async tasks (rather than M:N), the single-threaded runtime is the right tool for that job, though pairing it with blocking syscalls on that same thread is unusual.

Summary source: run-a, higher share of the Claims' quoted words (0.67 vs 0.58).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb18-f005307-c3

## Question `borrowck-self-referential-structs`

### borrowck-self-referential-structs--p1 — Extend borrow checker

Summary: A subset of self-referential structs — ones that borrow only from a heap allocation owned by a sibling field, without mutating it — could be proven safe by a smarter borrow checker without needing `Pin`; this is wanted more than fields-in-traits because the need for it comes up regularly, to the point of expecting to "wonder how we ever lived without it."

Summary source: run-b, higher share of the Claims' quoted words (0.64 vs 0.36).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb19-f007207-c3

## Question `borrowed-build-state-vs-builder`

### borrowed-build-state-vs-builder--p1 — Builder consume to immutable

Summary: The current reliance on a lifetime-bound reference into shared build state is a "lifetime hack"; the fix is a builder that consumes the mutable build state into an immutable owned structure, so downstream code can reference the resulting store directly instead of threading a borrow through construction.

Summary source: run-b, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa07-f003704-c4

## Question `bounded-grid-universe`

### bounded-grid-universe--p2 — Fixed-size, periodic (toroidal) universe, over unbounded-growable or fixed-non-wrapping

Summary: Of the three ways to bound an in-principle-infinite simulation grid in finite memory — unbounded expansion (risks unbounded slowdown or running out of memory), fixed non-periodic edges (kills patterns that reach the boundary, like gliders), and a fixed-size periodic (toroidal, wraparound) universe — the periodic option is chosen because it lets patterns keep running forever without either problem.

Summary source: run-a, only run whose summary covers the final Claims.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sB02-f000256-c2, b-bk02-f000256-c1

## Question `boxed-closure-tuple-vs-named-field`

### boxed-closure-tuple-vs-named-field--p1 — Tuple struct with constructor

Summary: The predicate should be stored as `Box<dyn Fn(&S) -> bool>` in a public tuple-struct field so stateful closures that capture values (e.g. a level number) can be used, not just hard-coded literals; `Box` won't allocate for non-capturing closures anyway.

Summary source: run-a, higher share of the Claims' quoted words (0.55 vs 0.18).

Tag: taste (majority; votes tradeoff / taste / taste)

Claims: b-sb14-f004398-c1

### boxed-closure-tuple-vs-named-field--p2 — Avoid trait objects in public field

Summary: The original design deliberately stayed away from exposing the trait object in the public field so that users would never need to write `Box::new` at a call site themselves.

Summary source: run-b, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb14-f004398-c2

### boxed-closure-tuple-vs-named-field--p3 — Constructor function mitigates boxing friction

Summary: A `new` constructor that performs the boxing internally keeps the `Box<dyn Fn>` representation while letting a call site read as plain `DespawnOnExitWith::new(|state| ...)`, mitigating the friction of boxing without changing the field's shape.

Summary source: run-b, higher share of the Claims' quoted words (0.50 vs 0.33).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb14-f004398-c3

### boxed-closure-tuple-vs-named-field--p4 — Named field for clarity

Summary: Once a constructor already does the boxing, the tuple struct's main ergonomic benefit is gone, and "stores a boxed function" is tricky for newcomers to read off a bare tuple field, so the field should be named for clarity.

Summary source: run-b, higher share of the Claims' quoted words (0.58 vs 0.42).

Tag: taste (majority; votes taste / tradeoff / taste)

Claims: b-sb14-f004398-c4

## Question `boxed-vs-hand-written-future`

### boxed-vs-hand-written-future--p1 — Prefer `Box::pin(async move {...})` (one heap allocation per request) over a hand-rolled `poll`-based future struct for middleware that needs post-response work, given Lambda's cost profile

Summary: `Box::pin(async move {...})` is the idiomatic default for middleware that must do work after the inner future resolves; on Lambda the one heap allocation per request is irrelevant, so hand-rolling a `poll`-based struct with `pin-project` to save it is reserved for a tight loop on a busy server, not the general case.

Summary source: run-b, tie on share of the Claims' quoted words (0.67), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb22-f008906-c2

## Question `breaking-rename-for-vocabulary`

### breaking-rename-for-vocabulary--p1 — Rename for vocabulary consistency pre 1.0

Summary: A term left over from an earlier, broader project scope ("node") is dropped from the vocabulary everywhere it appears in the public API, because the moment right before 1.0 is the moment to align naming with the current mental model, even though it breaks every caller using the old names.

Summary source: run-b, higher share of the Claims' quoted words (0.25 vs 0.12).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sR08-f003731-c2

## Question `breaking-wire-change-in-minor`

### breaking-wire-change-in-minor--p1 — Break compat with transition window

Summary: A pre-1.0 networking library can ship a breaking wire-protocol change in a routine minor release for a real protocol improvement (here, dropping a full round-trip from every new connection), accepting that new and old nodes can no longer talk to each other, and softening the break with a transition window (here, keeping the old infrastructure running for several more weeks).

Summary source: run-a, higher share of the Claims' quoted words (0.40 vs 0.20).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sT04-f001319-c1

## Question `build-tool-cargo-subcommand-vs-standalone`

### build-tool-cargo-subcommand-vs-standalone--p1 — Cargo subcommand

Summary: A subcommand is functionally identical to a standalone binary plus a few injected environment variables, so an ecosystem tool aiming for wide reuse should register as a `cargo` subcommand; a standalone "cargo plus plus" replacement fragments and, in the strong form of this view, is how you kill an ecosystem.

Summary source: run-b, higher share of the Claims' quoted words (0.36 vs 0.29).

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: a-sa05-f003025-c1, a-sa05-f003025-c2

### build-tool-cargo-subcommand-vs-standalone--p2 — Standalone or replacement

Summary: Cargo cannot run, test or bench wasm/iOS/Android projects and its development cycle is slow, so high-usage ecosystem tools (wasm-bindgen and similar) end up standalone by necessity, and a project's own CLI (e.g. Bevy's) can reasonably be designed as a cargo wrapper/replacement rather than a subcommand, with narrow project-specific needs better served outside a general-purpose stable tool like Cargo.

Summary source: run-a, higher share of the Claims' quoted words (0.48 vs 0.32).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa05-f003025-c3, a-sa05-f003025-c4, a-sa05-f003025-c5

## Question `built-in-async-runtime`

### built-in-async-runtime--p1 — No built-in runtime, ecosystem choice

Summary: Rust is a low-level language that strives for minimal runtime overhead, so unlike languages whose runtime bundles memory management and exception handling, it leaves the async runtime's scope limited and lets you choose one depending on your requirements rather than providing one — at the cost of an extra step to get started.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.29).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-bk01-f000233-c2

## Question `builtin-package-manager-effect`

### builtin-package-manager-effect--p1 — Builtin package manager changes practice

Summary: Not even thinking to look for a C/C++ library, because any that existed would have had to be vendored by copying source into the project, versus a single `cargo add` for the Rust equivalent, is read as evidence that having a good, builtin package manager changes what a developer will even attempt.

Summary source: run-b, higher share of the Claims' quoted words (0.50 vs 0.44).

Tag: fact (majority; votes fact / tradeoff / fact)

Claims: a-sR15-f008241-c2

## Question `byte-vs-bit-packed-cells`

### byte-vs-bit-packed-cells--p1 — Bit-packed FixedBitSet over one-byte-per-cell Vec<Cell>

Summary: Representing each cell with a full byte makes iterating over cells easy but wastes seven of every eight bits per cell; a `FixedBitSet`-based, bit-packed rewrite is the resolution to that waste.

Summary source: run-a, higher share of the Claims' quoted words (0.64 vs 0.27).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-bk02-f000256-c4

## Question `c-maintainers-rust-bindings-duty`

### c-maintainers-rust-bindings-duty--p1 — C maintainers not obligated to rust

Summary: A C maintainer will fix their own C code but is not going to be forced to learn Rust or take responsibility for fixing Rust bindings that break as a result of a C-side change.

Summary source: run-b, higher share of the Claims' quoted words (0.50 vs 0.33).

Tag: taste (majority; votes taste / tradeoff / taste)

Claims: b-sb18-f005332-c1

### c-maintainers-rust-bindings-duty--p2 — Rust needs c maintainer cooperation

Summary: Rust adoption in a C codebase depends on C maintainers' cooperation: being blocked from pushing small, Rust-motivated robustness and lifetime fixes into the C code causes real harm — kernel panics that trace back to bugs in that C code rather than to the Rust side — and the resulting friction and exhaustion is itself a reason people leave the effort.

Summary source: run-a, tie on share of the Claims' quoted words (0.17), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb18-f005332-c2, b-sb18-f005332-c3

### c-maintainers-rust-bindings-duty--p3 — Adoption slow for practical reasons

Summary: The pushback against Rust in the kernel is attributed to old-time C kernel developers being unfamiliar with and unenthusiastic about learning a new, quite different language, plus instability in the Rust kernel infrastructure itself — not to bad faith — framing slow adoption as a practical, expected friction rather than a moral failing on either side.

Summary source: run-b, higher share of the Claims' quoted words (0.39 vs 0.33).

Tag: fact (majority; votes fact / tradeoff / fact)

Claims: b-sb18-f005332-c4

## Question `cancel-safety-requirement`

### cancel-safety-requirement--cancel-safety-required — Cancel safety is required; its absence is a bug or rules a crate out

Summary: Cancel safety on `recv` is a hard requirement for async RPC/mpmc channels used internally, not a nice-to-have: a library whose `recv` occasionally lost notifications under cancellation caused stuck tasks in practice, and a non-cancel-safe RPC channel found in production was treated as a critical bug serious enough to break a fixed release cadence and ship an out-of-cycle fix.

Summary source: run-a, higher share of the Claims' quoted words (0.56 vs 0.44).

Tag: tradeoff (majority; votes fact / tradeoff / tradeoff)

Claims: a-sT04-f001650-c1, b-sb17-f005159-c4

## Question `cfg-wasm-as-reduced-platform-proxy`

### cfg-wasm-as-reduced-platform-proxy--p1 — Deliberately misreport target metadata (`target_family` without "wasm", `arch: "wasm64"`) to defeat crates' `cfg`-based assumptions that "wasm32" implies a reduced-functionality standalone web build

Summary: Crates that special-case behavior whenever they see the "wasm" target family or `wasm32` architecture get it wrong for a target with full Linux syscall access, so metadata is deliberately misreported to defeat those assumptions — called "hacks" that the team would rather not need, pending the ecosystem recognizing that fully-featured Wasm targets exist.

Summary source: run-b, higher share of the Claims' quoted words (0.58 vs 0.50).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sb22-f009062-c2

## Question `cli-flag-convenience-vs-consistency`

### cli-flag-convenience-vs-consistency--p1 — Consistency across commands

Summary: Every other command in the tool already uses `--no-dry-run`, so the new command should match that pattern for consistency rather than introduce a differently-shaped flag.

Summary source: run-b, tie on share of the Claims' quoted words (0.00), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb09-f003036-c1

### cli-flag-convenience-vs-consistency--p2 — Convenience over consistency

Summary: Getting this particular flag wrong isn't actually dangerous, and `--no-dry-run` is annoying enough to type that a shorter, less consistent default might be worth the deviation.

Summary source: run-a, tie on share of the Claims' quoted words (0.56), shorter summary.

Tag: taste (majority; votes tradeoff / taste / taste)

Claims: b-sb09-f003036-c2

## Question `cli-flags-mirror-familiar-tool`

### cli-flags-mirror-familiar-tool--p1 — Mirror an established CLI's conventions rather than design fresh

Summary: A niche protocol tool's flags are designed around curl's argument conventions on purpose, under a stated "principle of least surprise," rather than inventing fresh names for its own domain.

Summary source: run-b, higher share of the Claims' quoted words (0.56 vs 0.44).

Tag: taste (majority; votes taste / tradeoff / taste)

Claims: a-sa14-f004947-c1

## Question `cli-output-overwrite-default`

### cli-output-overwrite-default--p1 — Default overwrite latest output

Summary: A CLI tool that repeatedly writes an output file should overwrite the same filename by default, so past shell commands can be reused unedited to view the latest result; this also matches a peer tool's (samply's) behavior, which nobody has been heard complaining about.

Summary source: run-a, higher share of the Claims' quoted words (0.24 vs 0.18).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb13-f004160-c3

### cli-output-overwrite-default--p2 — Default timestamp to avoid silent overwrite

Summary: The output filename should include a timestamp by default, or at least from the second run onward, so that a new result never silently replaces an old one.

Summary source: run-a, tie on share of the Claims' quoted words (0.33), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb13-f004160-c4

## Question `cli-tool-single-vs-multi-protocol`

### cli-tool-single-vs-multi-protocol--p1 — One CLI should cover every privacy protocol a team operates (OHTTP, CONNECT proxying, MASQUE, Privacy Pass), rather than a narrow tool per protocol

Summary: Existing single-protocol tools for OHTTP were useful but narrow; the differentiator for a new tool is combining OHTTP, CONNECT proxying, MASQUE and (soon) Privacy Pass in one place, since nothing else does.

Summary source: run-b, tie on share of the Claims' quoted words (0.82), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sR11-f004947-c1

## Question `close-future-result-vs-infallible`

### close-future-result-vs-infallible--p1 — Infallible close future

Summary: A close/shutdown future should be infallible rather than return a `Result`; an endpoint's `close()` future was changed from `Result`-returning to infallible.

Summary source: run-a, tie on share of the Claims' quoted words (0.75), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sT05-f002550-c3

## Question `cloud-lock-in-source`

### cloud-lock-in-source--p1 — Compute-platform choice is a smaller lock-in risk than adopting a cloud's proprietary managed-data SDK; ports-and-adapters (hexagonal) architecture removes the compute-level lock-in concern

Summary: Adopting a proprietary managed-data service (a specific SDK and data model) locks a project in more than the choice of compute platform does; structuring the codebase around a core business-logic crate with entry-point adapters lets the same application run on Fargate/ECS or Lambda interchangeably, which is offered as the actual fix for lock-in fears about serverless compute.

Summary source: run-b, tie on share of the Claims' quoted words (0.29), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa24-f011220-c2

## Question `codegen-macro-vs-generated-source`

### codegen-macro-vs-generated-source--p1 — Plain-generated-source over macro-based codegen (for client generation specifically)

Summary: A code generator emits a normal, on-disk Rust crate — source directory, `Cargo.toml`, `.rs` files — rather than expanding inline as a procedural macro, because macro-generated output is hard to debug and macros can produce confusing compile errors.

Summary source: run-b, tie on share of the Claims' quoted words (0.40), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa23-f011186-c2

## Question `compile-time-cost-of-generated-crates`

### compile-time-cost-of-generated-crates--p1 — Accept long compile times for generated-crate quality

Summary: Large autogenerated API crates can dominate a project's slowest-compiling dependencies, especially in release mode, but after looking for ways to shrink them, it's better to accept the long compile time than to give users a lower-quality API.

Summary source: run-a, tie on share of the Claims' quoted words (0.46), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa23-f011186-c5

## Question `compile-time-typed-dsl`

### compile-time-typed-dsl--p1 — Compile time typed dsl

Summary: Hosting a DSL's programs as compile-time types buys zero runtime cost and no dynamic loading, at the cost of not being able to easily run DSL programs that are loaded into a host application at runtime (config files, plugins, game mods).

Summary source: run-a, tie on share of the Claims' quoted words (0.62), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa16-f007175-c2

## Question `compile-time-vs-runtime-switches`

### compile-time-vs-runtime-switches--runtime-switch — Switch at runtime, dropping cfg or compile-time env vars

Summary: A compile-time environment variable used to pick test-only behavior is dropped entirely — described as "more programmatically sound" — and a related infrastructure-selection bug (production code silently pointed at staging relays) is fixed by moving off the `test-utils` feature and `#[cfg(test)]` entirely, relying only on a runtime-checked environment variable behind a dedicated function.

Summary source: run-b, tie on share of the Claims' quoted words (0.57), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sT04-f002233-c1, b-sT05-f002550-c1

## Question `compiler-triage-automation`

### compiler-triage-automation--p1 — Keep PR-nudging/triage bookkeeping partly manual rather than fully automating it

Summary: Routine compiler-team triage bookkeeping shouldn't be fully automated: contributors have only a finite amount of time and are a precious asset, so a human judgment call on when to nudge a reviewer avoids over-pressuring them, even while external contributors also expect a timely response.

Summary source: run-a, tie on share of the Claims' quoted words (0.30), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb23-f011235-c1

## Question `component-abi-special-case-lowerings`

### component-abi-special-case-lowerings--p1 — Ad hoc optimize common shapes

Summary: Ad hoc special-cased lowerings for common shapes — `ref.null` for `none`/no-error, a boolean `i32` for a no-payload `result` — are licensed at the CABI level when they're a significant win, and `option` is common enough that this qualifies.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.80).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa05-f003074-c1

### component-abi-special-case-lowerings--p2 — Regular lowering only

Summary: The claim that a null-for-none optimization would cover close to 95% of cases in practice is disputed, since languages with parametric polymorphism (such as Java's `Optional`) typically cannot perform that specialization without costly runtime type dispatch, undercutting the case for the ad hoc shortcut.

Summary source: run-b, higher share of the Claims' quoted words (0.50 vs 0.40).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa05-f003074-c2

### component-abi-special-case-lowerings--p3 — Cautious of shape proliferation

Summary: Allowing extra matched shapes for special-cased lowerings risks a slippery slope — "how many shapes is enough" — so any widening of matchable shapes needs an explicit design principle rather than case-by-case allowances.

Summary source: run-a, tie on share of the Claims' quoted words (0.71), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa05-f003074-c3

## Question `component-map-duplicate-keys`

### component-map-duplicate-keys--p1 — Generators must normalize last wins

Summary: Bindings generators should be required — strengthened from merely expected to a spec-level MUST — to normalize a map with duplicate keys so that generated map interfaces behave as if duplicates were filtered out with last-value-wins semantics.

Summary source: run-b, tie on share of the Claims' quoted words (0.48), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sb11-f003384-c1, b-sb11-f003384-c2

### component-map-duplicate-keys--p2 — Mandate uniqueness enforced at boundary

Summary: Uniqueness of map keys should be mandated by the spec and enforced at the component boundary rather than silently tolerated, though there's room to differ on the enforcement mechanism — whether a violation should trap or the lowering side should just silently keep the final value.

Summary source: run-a, higher share of the Claims' quoted words (0.73 vs 0.55).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb11-f003384-c3, b-sb11-f003384-c4

### component-map-duplicate-keys--p3 — Host may not must dedupe

Summary: A host should be allowed, but not required, to deduplicate a `map` with duplicate keys, with well-defined last-value-overwrites semantics only when such merging happens — drawing an analogy to how NaN payload canonicalization is optional, not mandatory, at component boundaries.

Summary source: run-b, higher share of the Claims' quoted words (0.60 vs 0.53).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb11-f003384-c5

## Question `component-map-ordering`

### component-map-ordering--p1 — Preserve order rename type

Summary: Bindings are expected to preserve a `map`'s entry order, since most host languages' own Map types do, and the component-model type should be renamed to something like `dict` or `ordered-map` to avoid confusion with types that don't preserve order.

Summary source: run-b, higher share of the Claims' quoted words (0.58 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb11-f003384-c6

### component-map-ordering--p2 — Unordered by default

Summary: The basic `map` type should not guarantee any order, since most languages' basic map types don't either — nine times out of ten you don't need ordering — with an explicitly ordered variant available separately as `list<tuple<key,value>>`, matching the precedent of Rust's HashMap, .NET's Dictionary, Java's HashMap and Go's map.

Summary source: run-b, higher share of the Claims' quoted words (0.68 vs 0.63).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sb11-f003384-c7, b-sb11-f003384-c8

### component-map-ordering--p3 — Deterministic profile may need canonical order

Summary: If a deterministic execution profile can't randomly permute and doesn't normalize map order, then order becomes an observable part of `map`'s semantics whether intended or not — a consequence worth discussing on its own rather than a settled question.

Summary source: run-a, tie on share of the Claims' quoted words (0.69), shorter summary.

Tag: fact (majority; votes fact / tradeoff / fact)

Claims: b-sb11-f003384-c9

## Question `compress-debug-sections-default`

### compress-debug-sections-default--p1 — Make `--compress-debug-sections=zstd` the Linux default

Summary: Setting `--compress-debug-sections=zstd` as the default linker flag for Linux targets is worth doing, based on a measured shrink of a hello-world project's `target/` from 4.7M to 1.5M plus a modest build-time improvement.

Summary source: run-a, higher share of the Claims' quoted words (0.64 vs 0.55).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sb22-f009132-c1

### compress-debug-sections-default--p2 — The stated motivation (shrinking `target/`) doesn't yet justify this specific fix, and if it ships at all it should apply to release builds only

Summary: The motivation itself is called lacking: before reaching for compression as a default fix, the discussion should first pin down why `target/` is actually big — duplication across projects, stale files, or genuinely unused debug info — since compression alone would also not obviously help, and would slow down, every debug build.

Summary source: run-b, higher share of the Claims' quoted words (0.75 vs 0.25).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sb22-f009132-c2

### compress-debug-sections-default--p3 — This cannot become the Linux default until mainstream distro debugging/profiling tools support zstd-compressed debug sections

Summary: Many developers are required to use Ubuntu LTS or another enterprise distro at work, whose gdb and binutils lack zstd support; shipping this by default would silently break their debugging experience, called a "showstopper" that leaves the proposal going nowhere until mainstream distro tooling catches up.

Summary source: run-b, higher share of the Claims' quoted words (0.50 vs 0.33).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sb22-f009132-c3

## Question `consolidate-internal-network-frameworks`

### consolidate-internal-network-frameworks--p1 — Reuse and consolidate on ecosystem crates

Summary: A new internal framework is deliberately built to stand on the shoulders of existing, battle-tested open-source crates (hyper, tokio) rather than reinvent them, prioritizing faster iteration and contributing fixes back upstream — to the point that team members become core maintainers of the upstream crates.

Summary source: run-b, higher share of the Claims' quoted words (0.22 vs 0.00).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa15-f005604-c1

## Question `const-generics-unify-specializations`

### const-generics-unify-specializations--p1 — Unify via const generics

Summary: Two hand-specialized types differing only by stride count have already drifted apart from each other inside the very PR meant to add the second one, and a single type parameterized by a const generic would cover both with identical codegen once monomorphized, so the drift is treated as real rather than hypothetical.

Summary source: run-b, higher share of the Claims' quoted words (0.45 vs 0.24).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sR12-f005085-c2

## Question `coupled-debug-accessor-vs-primitive`

### coupled-debug-accessor-vs-primitive--p1 — Narrow purpose built debug accessor

Summary: A host-only, linear-search accessor deliberately scoped to guest-debugging mode is added, and when its linear-search cost is challenged it is rewritten to be O(1) via a lazily-built, module-level cached reverse table rather than abandoning the narrow, purpose-built design.

Summary source: run-b, higher share of the Claims' quoted words (0.09 vs 0.05).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb16-f005000-c1, b-sb16-f005000-c4

### coupled-debug-accessor-vs-primitive--p2 — Skeptical of narrow internals coupled api

Summary: A powerful but inherently inefficient (linear-search) debugging capability that couples to internal layout details is worth questioning even once made asymptotically efficient, since the cost of maintaining that coupling — and its fragility to future refactoring — may not be justified for what is a niche use case.

Summary source: run-a, higher share of the Claims' quoted words (0.42 vs 0.38).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb16-f005000-c2, b-sb16-f005000-c5

### coupled-debug-accessor-vs-primitive--p3 — Prefer generic decoupled primitive

Summary: A smaller, general primitive — `Func::eq`/`Func::hash` as pointer-identity equality — is preferred because it is independently useful and lets the caller build their own index in a single linear pass, asymptotically better than the coupled accessor; the accessor's own author ultimately agrees the internal-layout coupling isn't worth it and drops it in favor of this primitive.

Summary source: run-b, higher share of the Claims' quoted words (0.42 vs 0.35).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb16-f005000-c3, b-sb16-f005000-c6

## Question `cow-for-allocation-visibility`

### cow-for-allocation-visibility--p1 — Prefer cow for allocation visibility even at negligible gain

Summary: Even when an allocation-avoiding type like `Cow<str>` would only save a negligible amount of work, it's still worth preferring over a plain `String`, because Rust makes allocations visible in the code in a way that makes you want to avoid them regardless of how small the performance impact actually is.

Summary source: run-a, higher share of the Claims' quoted words (0.64 vs 0.55).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sR15-f008241-c1

## Question `cpp-binding-tool-choice`

### cpp-binding-tool-choice--p1 — No single tool fits everyone

Summary: Across bindgen/cbindgen (C-ABI-only, forcing manual unsafe conversion for anything richer), CXX (safer types but manual redeclaration and boxing since it can't see existing layouts), a hand-written IDL like Zengar (explicit layout control but a separate file that doesn't scale), and Crubit (maximum coverage via native clang+rustc integration but a clang-toolchain requirement) — no two C++-interop projects want exactly the same tradeoffs, so there may not be one interop solution to rule them all.

Summary source: run-b, higher share of the Claims' quoted words (0.55 vs 0.45).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb24-f011312-c1

## Question `cpp-bindings-default-unsafe`

### cpp-bindings-default-unsafe--p1 — Reject blanket unsafe use annotations and heuristics

Summary: Marking every bound C++ function `unsafe` by default makes the annotation stop meaning anything — one project forked its own tooling just to turn blanket `unsafe` off entirely — so a better binding combines optional C++-side safety annotations with type-based heuristics, leaving `unsafe` visible only on genuinely dangerous APIs.

Summary source: run-b, higher share of the Claims' quoted words (0.50 vs 0.17).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb24-f011312-c2

## Question `cpp-mutable-reference-representation`

### cpp-mutable-reference-representation--p1 — None satisfying yet add native cpp reference type

Summary: Raw pointers force every reference-taking method, including plain method calls through `self`, to be unsafe, and `Cell` assumes invariants (safe projection through `Option`/`Vec`, `Sync`-safety) that C++ references simply don't guarantee; none of the existing approaches are good enough, so the preferred fix is a new, native C++-style reference type in Rust — one where only mutation that could invalidate the reference is unsafe — which needs compiler features (generalized field projection, custom auto-referencing) that don't exist yet.

Summary source: run-b, higher share of the Claims' quoted words (0.36 vs 0.27).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb24-f011312-c3

## Question `crate-maintenance-signaling`

### crate-maintenance-signaling--existing-tools-suffice — Existing tools suffice (maintenance badges, yank for serious cases)

Summary: The `badges.maintenance.status` field in Cargo.toml, already rendered by lib.rs, already solves whole-crate deprecation signaling, and for the genuinely serious case — a version with a real security vulnerability — outright yanking is proportionate, not "too alarmist" as its critics claim.

Summary source: run-b, higher share of the Claims' quoted words (0.79 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb23-f009334-c3, b-sb23-f009334-c5

### crate-maintenance-signaling--new-deprecate-mechanism — A dedicated per-version deprecation mechanism

Summary: Yank is too alarmist and breaking for signaling a crate or version shouldn't be used; what's wanted is a dedicated command like `cargo deprecate <pkg>[@range] -m <reason>` that marks specific version ranges with a reason, without forcing a break — something the existing whole-crate maintenance badge cannot do since it can't target individual problematic versions.

Summary source: run-b, only run whose summary covers the final Claims.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb23-f009334-c1, b-sb23-f009334-c4

### crate-maintenance-signaling--status-auto-decays — Maintenance status should decay automatically

Summary: A status marked once and never revisited stops reflecting reality; the system doesn't work if the maintenance information isn't kept up to date, which argues for a status that decays automatically rather than staying wherever an author last set it.

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sb23-f009334-c6

### crate-maintenance-signaling--status-opt-in-only — Status opt-in only, no forced decay

Summary: Maintenance status should be opt-in per crate and changeable later by the author, modeled on "last seen online" indicators, rather than forced on everyone; any reminder emails nudging authors to update status should likewise be a separate, one-time opt-in per person, not automatic.

Summary source: run-a, only run whose summary covers the final Claims.

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: b-sb23-f009334-c7

## Question `crdt-vs-coordination`

### crdt-vs-coordination--p1 — Convergence for a multi-actor, human-and-agent live document should come from CRDTs rather than a coordinating or locking mechanism

Summary: "Convergence without coordination" — CRDTs, formalized in 2011, have been the center of this collaborative-editor's work for a decade, letting the same shared document be edited by people and agents on different continents at once with no locking, operational-transform, or authoritative-server step required.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.67).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR11-f005071-c1

## Question `custom-allocator-restart-persistence`

### custom-allocator-restart-persistence--p1 — Custom allocator for restart persistence

Summary: Rust objects can be made to survive a process restart by stitching together systemd's FD store, `memfd_create`, and a custom raw-memory `Allocator`, as an alternative to the more familiar practice of serializing state out to Redis or a temp file before shutdown and reloading it on startup.

Summary source: run-a, higher share of the Claims' quoted words (0.50 vs 0.40).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sb19-f005836-c1

## Question `custom-bytes-type-vs-vec-u8`

### custom-bytes-type-vs-vec-u8--p1 — Custom bytes type over vec u8 at boundaries

Summary: Owned byte buffers at an API boundary where allocation strategy matters should be typed as a custom wrapper (e.g. `burn_common::Bytes`) rather than `Vec<u8>`, so that a future backend-managed allocation strategy (like pinned GPU memory) can be substituted later, while borrowed `&[u8]`/`&mut [u8]` stay as-is.

Summary source: run-a, higher share of the Claims' quoted words (0.50 vs 0.25).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR08-f003587-c3

## Question `custom-wasm-target-vs-wasi`

### custom-wasm-target-vs-wasi--p1 — Define a custom Rust compilation target (`wasm32-browserpod-linux-musl`) rather than port to a WASI target, for running unmodified existing Rust programs in-browser

Summary: Porting an existing program to WASI would mean touching every `std::os::unix` call site, dropping thread usage entirely since wasip3's cooperative threading isn't yet supported by std or tokio, and losing the ability to shell out to other tools; since the sandbox's own kernel already solves filesystem, networking, subprocesses and real per-thread parallelism, writing a custom Rust compilation target skips that porting work entirely rather than accepting those losses.

Summary source: run-b, tie on share of the Claims' quoted words (0.40), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sb22-f009062-c1

## Question `debug-assert-vs-infallible`

### debug-assert-vs-infallible--p1 — Keep debug asserts

Summary: `debug_assert!` is valuable in a library because it actually documents and tests an assumption in the code; giving it up is only acceptable when the replacement code comes with enough tests to cover the same ground.

Summary source: run-a, tie on share of the Claims' quoted words (0.25), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb04-f001392-c3

### debug-assert-vs-infallible--p2 — Prefer infallible code

Summary: `debug_assert!` in a library is disliked outright because when the assumption turns out wrong, it surfaces as a panic in the library's users' users — reportable and fixable only through a coordinated release across projects — so the code should instead be rewritten so the assumption can never be violated at all.

Summary source: run-b, tie on share of the Claims' quoted words (0.33), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb04-f001392-c4

## Question `dedicated-design-vs-duplicate-now`

### dedicated-design-vs-duplicate-now--p1 — Dedicated decoupled recorder from the start

Summary: A new but closely related serialization format should get its own dedicated, decoupled implementation (e.g. a `SafeTensorFileRecorder` independent of the PyTorch recorder, with a configurable adapter) from the start, rather than starting from a copy of the existing similar format's code.

Summary source: run-a, higher share of the Claims' quoted words (0.33 vs 0.11).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb09-f002567-c1

### dedicated-design-vs-duplicate-now--p2 — Duplicate now refactor later

Summary: Copying the existing, similar format's implementation wholesale as a starting base, with cleanup planned for later, is how the new format's support actually got built.

Summary source: run-b, tie on share of the Claims' quoted words (0.00), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb09-f002567-c2

### dedicated-design-vs-duplicate-now--p3 — Reduce duplication before merge

Summary: A large amount of introduced duplication — whether in code or in near-identical documentation sections — should be reduced before merge rather than merged with the intent to fix it later, since "later" risks never happening or happening even worse given the size of the change.

Summary source: run-a, higher share of the Claims' quoted words (0.25 vs 0.20).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb09-f002567-c3, b-sb09-f002567-c4

### dedicated-design-vs-duplicate-now--p4 — Keep separate for pragmatic reasons

Summary: After discussing it directly, the two near-identical documentation sections are kept separate — same format and language, but two sections rather than one merged one — because for now that is simply the easier path.

Summary source: run-b, higher share of the Claims' quoted words (0.55 vs 0.45).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb09-f002567-c5

## Question `dedicated-methods-vs-manual-composition`

### dedicated-methods-vs-manual-composition--p1 — Omit methods with no perf benefit, compose manually

Summary: An API shouldn't add a dedicated method for a composed operation like append/prepend rotation when a specific method gives no performance benefit over building the transformation and multiplying it in manually.

Summary source: run-a, tie on share of the Claims' quoted words (0.80), shorter summary.

Tag: unresolved (three-way split; votes tradeoff / fact / taste)

Claims: a-sB01-f000217-c5

## Question `dedicated-test-for-overlapping-case`

### dedicated-test-for-overlapping-case--p1 — A new prop-label feature should get its own dedicated test even where the new code path overlaps generic behavior

Summary: Even where a new feature's code path largely overlaps existing, more general behavior, a reviewer still asks the author to add a test making sure the new case specifically works.

Summary source: run-b, higher share of the Claims' quoted words (0.80 vs 0.60).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sR01-f000538-c2

### dedicated-test-for-overlapping-case--p2 — A dedicated test for behavior already covered by more general, feature-independent tests is unnecessary

Summary: A dedicated test for behavior already exercised by more general, feature-independent tests is unnecessary, since the case in question (optional prop values) isn't inherent to the new feature at all.

Summary source: run-a, higher share of the Claims' quoted words (0.55 vs 0.36).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sR01-f000538-c3

## Question `dedupe-transitive-dependency-versions`

### dedupe-transitive-dependency-versions--p1 — Actively reduce duplicated transitive dependencies by upgrading

Summary: Upgrading a core dependency was valued specifically because it let the project drop duplicated copies of shared transitive dependencies, shrinking its overall dependency footprint as a direct, named benefit of the upgrade.

Summary source: run-b, tie on share of the Claims' quoted words (0.40), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sR05-f001981-c2

## Question `default-features-minimal-vs-inclusive`

### default-features-minimal-vs-inclusive--inclusive-defaults — Enable by default for minimal friction

Summary: Weighing pushback that niche formats shouldn't be defaults, the path of least friction now — shipping them enabled — is preferable to pre-curating defaults by popularity, with the option to change the defaults later.

Summary source: run-a, higher share of the Claims' quoted words (0.75 vs 0.62).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa02-f002127-c1

### default-features-minimal-vs-inclusive--minimal-defaults — Compile in only what is used

Summary: You should be able to compile in only what you're actually using — demonstrated by shipping with roughly a third of a comparable project's dependency count, achieved by enabling only 4 of 20 available image codecs by default and making SVG and networking support opt-in per deployment rather than bundled by default.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.67).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb25-f011435-c2

### default-features-minimal-vs-inclusive--unresolved-reported — Reported as an open debate, no side taken (heap profiling)

Summary: Whether a heap-profiling feature should ship on by default is left as an open, ongoing discussion in the project's own issue tracker, with the current default being off and readers pointed to the discussion rather than told an answer.

Summary source: run-b, tie on share of the Claims' quoted words (0.45), shorter summary.

Tag: fact (majority; votes fact / taste / fact)

Claims: a-sa26-f011684-c1

## Question `defensive-guards-for-unlikely-failures`

### defensive-guards-for-unlikely-failures--p1 — Guard even theoretical leaks

Summary: Even a failure mode judged unlikely to ever occur in practice is worth guarding against with good old-fashioned RAII (a `Drop`-based guard), because correctness is worth the modest extra engineering even for a merely theoretical problem.

Summary source: run-a, higher share of the Claims' quoted words (0.73 vs 0.55).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sR14-f007341-c1

## Question `defer-multithreaded-encoding`

### defer-multithreaded-encoding--p1 — Defer multithreading decision

Summary: Whether to wait on a shared lock with a timeout under multithreaded access is a real decision with a real failure mode (deadlocks), and it's fine to delay making that decision until the current single-threaded implementation has proven its worth, since multithreaded encoding doesn't yet show much benefit.

Summary source: run-b, higher share of the Claims' quoted words (0.67 vs 0.56).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb03-f000569-c1

## Question `depend-vs-hand-roll`

### depend-vs-hand-roll--hand-roll-or-vendor — Keep a hand-rolled or vendored implementation, or a lean internal wrapper over a weak vendor SDK

Summary: The Rust vendor-SDK ecosystem is weak enough across several major cloud providers that a team builds and maintains its own small internal SDKs instead; the same instinct shows up as resisting a new dependency for something as foundational as an executor's core data structures, preferring them self-contained and in-tree so they can change without cross-repo coordination, and as asking whether a thin crate implementing a stable external protocol could simply be vendored directly.

Summary source: run-b, higher share of the Claims' quoted words (0.31 vs 0.29).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa04-f002865-c2, a-sa14-f005079-c3, a-saL2-f011092-c3

### depend-vs-hand-roll--minimize-footprint — Minimize the dependency footprint even at the cost of uglier code or release cycles; audit burden too high

Summary: Minimizing a library's dependency footprint is worth uglier code, slower release cycles, or breaking changes: a new dependency tree's `cargo vet` audit burden was called excessive; a maintainer accepted uglier code specifically because reducing dependencies matters more for a widely-used library; and a project spent whole release cycles cutting dependencies ahead of its 1.0, accepting breaking changes as the cost.

Summary source: run-a, higher share of the Claims' quoted words (0.21 vs 0.18).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR06-f002016-c1, b-sR03-f001160-c1, b-sR05-f002453-c1

### depend-vs-hand-roll--take-the-dependency — Take the existing, tested crate (persistent data structures, an intrusive-list crate, `rustix` over raw libc)

Summary: An existing, tested crate is often the better call than hand-rolling: a persistent-data-structure crate (`rpds`) beat a hand-rolled segment tree on API cleanliness, correctness and good-enough performance; a `rustix` safe wrapper is repeatedly proposed over raw, manual syscall handling; and an executor's internal data structure crate is defended for keeping the dependency specifically because of its miri+loom test coverage and shared maintenance with another executor.

Summary source: run-a, higher share of the Claims' quoted words (0.35 vs 0.29).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-02-f001053-c1, a-sa04-f002865-c1, a-sa14-f005079-c4

## Question `dependency-upgrade-regression-handling`

### dependency-upgrade-regression-handling--p1 — Never ship a known crash prefer soft guardrails

Summary: A version that always crashes on exit is not an option to ship, so between shipping with that always-crash regression, pinning to the older broken version, or holding the release, the workable path is a narrower crash confined to one feature path with a guardrail steering users away from it — never a known, unconditional crash.

Summary source: run-a, higher share of the Claims' quoted words (0.57 vs 0.29).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR04-f001749-c2

## Question `dependency-version-requirement-width`

### dependency-version-requirement-width--p1 — Loosen serde requirement to `^1`

Summary: A crate's `serde` requirement blocking an otherwise-portable example is grounds to loosen that requirement to `^1`, favoring compatibility with older `serde` versions already in a downstream project's tree.

Summary source: run-b, higher share of the Claims' quoted words (0.67 vs 0.33).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sT05-f003044-c2

## Question `deprecate-gradually-vs-break`

### deprecate-gradually-vs-break--p1 — A deprecated compatibility shim (WAGI) should be phased out with warnings and migration time, not removed outright

Summary: A legacy compatibility shim starts printing deprecation warnings and gets dropped from new examples in the docs, but existing components built on it keep running unbroken — explicitly framed as the start of a gradual, managed deprecation rather than a break.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.40).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR11-f005050-c2

## Question `deref-delegation-vs-accessors`

### deref-delegation-vs-accessors--p1 — Drop Deref delegation for explicit accessors

Summary: Delegating one type's methods to another through `Deref` should be dropped in favor of explicit accessor methods — removing a `Deref` link so a subsystem's client can "stand on its own" and callers write an explicit accessor call rather than relying on an implicit deref chain.

Summary source: run-a, higher share of the Claims' quoted words (0.50 vs 0.25).

Tag: taste (majority; votes tradeoff / taste / taste)

Claims: b-sT04-f001890-c1

## Question `derive-arithmetic-ops`

### derive-arithmetic-ops--ecosystem-crates-suffice — Leave it to ecosystem crates

Summary: There's no need to put arithmetic-trait derives in the core language: `derive_more` already covers this well, and it's the point of having a package manager that the core language and std stay minimal while most conveniences are left to libraries.

Summary source: run-a, higher share of the Claims' quoted words (0.54 vs 0.46).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa19-f009292-c6

### derive-arithmetic-ops--oppose-semantics-ambiguous — Reject: field-wise arithmetic is wrong or rarely useful

Summary: Unconstrained field-wise arithmetic derive is rejected as semantically wrong or too narrow to be a sane default: it's unclear how often naive field-wise addition is actually correct (most wrapper structs needing arithmetic — complex numbers, quaternions, matrices — have their own non-field-wise rules), there's no single right answer even for simple newtypes (e.g. whether angle arithmetic should wrap modulo 2π), and affine-space math shows addition of points (two geographic coordinates, two `Instant`s) is often meaningless even where point-minus-point or point-plus-translation is meaningful.

Summary source: run-a, higher share of the Claims' quoted words (0.42 vs 0.35).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa19-f009292-c2, a-sa19-f009292-c3, a-sa19-f009292-c4, b-sb22-f009292-c2, b-sb22-f009292-c3

### derive-arithmetic-ops--prefer-delegation-mechanism — Reject in favor of a delegation mechanism

Summary: A basic field-wise arithmetic derive can only encode one relationship between fields, so it doesn't generalize to matrices, quaternions or complex numbers; a delegation syntax or a generalized macro for constructing derives would serve the need better than a single fixed derive.

Summary source: run-a, higher share of the Claims' quoted words (0.62 vs 0.38).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa19-f009292-c5

### derive-arithmetic-ops--support-fieldwise-derive — Add it, like Clone/Debug

Summary: Hand-writing (or reaching for `derive_more` for) trivial field-wise `Add`/`Sub`/`Mul`/`Div` on structs where field-wise operation is obviously the only sensible behavior is needless busywork; std should support deriving these the same way it already does `Clone`, `Debug` and `Copy`, and the existence of `derive_more`'s own arithmetic derives is offered as evidence of real, existing demand for exactly this.

Summary source: run-b, higher share of the Claims' quoted words (0.47 vs 0.33).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa19-f009292-c1, b-sb22-f009292-c1, b-sb22-f009292-c4

## Question `desktop-webview-ipc-vs-single-context`

### desktop-webview-ipc-vs-single-context--p1 — Reject split brain untyped ipc

Summary: Half the point of Rust is the bugs it catches at compile time, and an IPC boundary that just tosses untyped strings and values around at runtime — where a host-side field rename fails only at runtime instead of at compile time — throws that benefit away, to the point of "genuinely hating" an architecture built that way.

Summary source: run-b, higher share of the Claims' quoted words (0.50 vs 0.28).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb21-f008390-c1

## Question `divergent-signature-for-forever-tasks`

### divergent-signature-for-forever-tasks--p1 — Prefer divergent signature for run forever tasks

Summary: A task meant to run forever should use a divergent (`-> !`) function signature rather than an ordinary returning one, because it grants a `'static` context and `'static`-lifetime local resources, making the run-forever intent explicit in the type signature itself.

Summary source: run-a, higher share of the Claims' quoted words (0.67 vs 0.44).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sB04-f000227-c3

## Question `docs-as-rust-vs-markdown`

### docs-as-rust-vs-markdown--p1 — Docs as rust source for compile time checks and dedup

Summary: Rewriting the documentation site's content as Rust source instead of an MDX-like format buys compile-time-validated doc links that go through the site's own router, plus data-as-code deduplication across documentation versions, offered as the concrete payoff for leaving Markdown-adjacent authoring.

Summary source: run-b, higher share of the Claims' quoted words (0.73 vs 0.64).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb14-f004399-c1

### docs-as-rust-vs-markdown--p2 — Keep markdown for authoring ergonomics

Summary: Ordinary editor and language tooling understands Markdown but not a custom Rust DSL for docs; writing a blog post should stay in the format it actually came from, and it's worth researching whether Markdown-based authoring can be preserved without losing the concerns that motivated moving away from it.

Summary source: run-a, tie on share of the Claims' quoted words (0.36), shorter summary.

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: b-sb14-f004399-c2, b-sb14-f004399-c3

### docs-as-rust-vs-markdown--p3 — Downgrade to plain markdown plus custom component delimiters

Summary: After weighing the ergonomics concern, the resolution is to downgrade the docs content from MDX/Rust-source back to plain Markdown files, inventing a custom convention (comment delimiters) for embedding interactive components instead of relying on a macro-based DSL.

Summary source: run-a, higher share of the Claims' quoted words (0.67 vs 0.44).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb14-f004399-c4

## Question `doctests-must-compile`

### doctests-must-compile--p1 — Require all blocks to compile

Summary: Every code block embedded in a doc comment is required to be valid, compiling Rust, because the project treats doc-comment examples as unit tests in their own right, not merely illustrative prose.

Summary source: run-b, higher share of the Claims' quoted words (0.50 vs 0.40).

Tag: unresolved (three-way split; votes taste / fact / tradeoff)

Claims: a-sR07-f002347-c1

## Question `downstream-vendor-removed-api-vs-rework`

### downstream-vendor-removed-api-vs-rework--rework-downstream — Rework downstream; the cost falls on downstream's own misuse

Summary: A downstream project hit by the same removal attributes the resulting pain to its own prior "horrifying" workarounds — dynamically generated columns that depended on the removed piece — rather than treating the removal itself as the fault, and offers to work through the fallout.

Summary source: run-b, tie on share of the Claims' quoted words (0.17), shorter summary.

Tag: tradeoff (majority; votes fact / tradeoff / tradeoff)

Claims: b-sT07-f003809-c4

### downstream-vendor-removed-api-vs-rework--vendor-removed-trait — Replicate the dropped trait downstream as a fallback

Summary: When a removed piece is needed and reworking the integration is too costly right now, the fallback is to replicate the dropped functionality directly inside the downstream project's own codebase.

Summary source: run-b, tie on share of the Claims' quoted words (0.40), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sT07-f003809-c3

## Question `durable-job-queue-vs-in-process`

### durable-job-queue-vs-in-process--p1 — Durable Postgres-backed job queue

Summary: A background job queue is deliberately backed by durable Postgres storage rather than kept in memory, because an in-memory queue's jobs would simply disappear the moment the service has any outage.

Summary source: run-b, tie on share of the Claims' quoted words (0.57), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sT09-f011688-c1

## Question `dyn-compatibility-rules-relaxation`

### dyn-compatibility-rules-relaxation--p1 — Dyn trait relaxation for this case is far off or never

Summary: Even a carefully sketched, higher-ranked-bound version of a `dyn`-compatible trait that would satisfy a real use case is judged not close to landing — "years and years, if ever" — with the plain `dyn` equivalent probably not even plausible.

Summary source: run-b, only run whose summary covers the final Claims.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa30-f013276-c1

### dyn-compatibility-rules-relaxation--p2 — Dyn trait object safety rules are overly constraining

Summary: `dyn Trait`'s object-safety rules are judged too constraining, with real doubt about whether many of them can be lifted at all — voiced alongside the fact that the next-generation trait-resolver rewrite meant to eventually address this has been underway since 2015.

Summary source: run-b, only run with a summary.

Tag: unresolved (one run fact, third tradeoff, other run had no summary; votes - / fact / tradeoff)

Claims: a-sa30-f013276-c5

## Question `dynamic-ecs-component-typed-id`

### dynamic-ecs-component-typed-id--p1 — Typed wrapper for safety

Summary: Runtime-registered ECS components should carry a compile-time type witness — a typed wrapper around the component ID parameterized by `T` — so that dynamic component access can be done safely, in place of manual pointer work and unsafe code, while still allowing multiple components with the same underlying type to be registered and accessed separately.

Summary source: run-a, higher share of the Claims' quoted words (0.63 vs 0.53).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-02-f001231-c1

## Question `easy-mode-rust`

### easy-mode-rust--p1 — Tasteful combination favoring easy mode

Summary: When onboarding a team new to Rust on a security-critical project, deliberately favor owned types over borrowed references and `Arc<RwLock<T>>` over lock-free structures, to minimize borrow-checker headaches for engineers new to the language, while keeping the option to refactor toward more advanced, performant idioms later.

Summary source: run-a, tie on share of the Claims' quoted words (0.40), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb24-f011295-c1

## Question `ecs-events-first-architecture`

### ecs-events-first-architecture--p1 — Build state changes as an events/observers cascade rather than direct system-to-system mutation, despite losing atomicity

Summary: Modeling every cross-system state change (granting XP, playing a sound, updating a tile) as a cascade of events made each system easy to reason about and reuse in isolation, at the real cost that a failure partway through a cascade cannot be rolled back — so every handler has to defensively stop propagation itself to keep the game in a stable state.

Summary source: run-b, tie on share of the Claims' quoted words (0.12), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb25-f012561-c1

## Question `ecs-relationship-fragmenting`

### ecs-relationship-fragmenting--p1 — Fragmenting enables more queries

Summary: Several concrete query operations — wildcard queries, named wildcard queries, nested joins, efficient up-traversal, efficient sibling queries — are only possible at all when relationship edge information is exposed at the archetype level, which a non-fragmenting, component-based approach cannot provide.

Summary source: run-b, higher share of the Claims' quoted words (0.89 vs 0.78).

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: b-sb07-f002142-c3

### ecs-relationship-fragmenting--p2 — Non fragmenting preferred for hierarchies

Summary: Fragmenting relationships are useless for hierarchical use cases and would just produce one archetype per entity; the non-fragmenting, relationship-type-keyed approach is what's actually needed, a conclusion independently reached by both this commenter and a Bevy ECS subject-matter expert.

Summary source: run-a, higher share of the Claims' quoted words (0.75 vs 0.62).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb07-f002142-c4

## Question `ecs-relationship-source-of-truth`

### ecs-relationship-source-of-truth--p1 — Single source of truth relationship

Summary: An ECS relationship system should treat the `Relationship` component as the sole source of truth, making `RelationshipTarget` a pure reflection that can't be populated directly, so component lifecycles alone (rather than runtime scanning) protect against duplicates — trading away the ability to spawn a populated target collection directly for O(1) inserts and no quadratic-runtime duplicate scanning.

Summary source: run-a, higher share of the Claims' quoted words (0.50 vs 0.31).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa04-f002554-c1

## Question `ecs-relationship-type-level-exclusivity`

### ecs-relationship-type-level-exclusivity--p1 — Type level exclusivity public

Summary: Encoding a relationship's exclusivity (one-to-one, one-to-many, etc.) at the type level is preferred because it makes incorrect usage fail to compile, improves error messages, and keeps the model close to how existing hierarchy types already read for users, for reflection, and for scene-serialization formats.

Summary source: run-b, tie on share of the Claims' quoted words (0.43), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb07-f002142-c1

### ecs-relationship-type-level-exclusivity--p2 — Private edges runtime consistency

Summary: Type-level exclusivity isn't even correct in practice — an entity can still hold both a one-to-one and a one-to-many edge component of the same relationship — and it forces every query site to know and restate the edge shape; a single, consistent query API regardless of exclusivity matters more than having that option.

Summary source: run-a, tie on share of the Claims' quoted words (0.38), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb07-f002142-c2

## Question `ecs-ui-large-vs-small-systems`

### ecs-ui-large-vs-small-systems--p1 — Still actively fighting the borrow checker over how to split large UI systems, with no settled solution

Summary: Large "god" UI systems with dozens of queries are simple to write but constantly conflict with the borrow checker, and a widget-per-system split helps isolate systems but forces repeated manual world/state access that itself risks borrow-checker errors — an ongoing problem, not a solved one, even after trying both shapes.

Summary source: run-a, tie on share of the Claims' quoted words (0.67), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: b-sb25-f012561-c3

## Question `embedded-crash-policy-kernel-vs-supervisor`

### embedded-crash-policy-kernel-vs-supervisor--p1 — Policy in userspace supervisor not kernel

Summary: There is no right answer to whether a crashed task should restart immediately, back off, or give up, so the kernel deliberately does not hardcode that policy at all — it only records the fault and notifies a userspace supervisor task, leaving the actual recovery decision to the application programmer since it depends on context.

Summary source: run-b, tie on share of the Claims' quoted words (0.43), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa17-f008217-c1

## Question `embedded-deferred-log-formatting`

### embedded-deferred-log-formatting--p1 — Deferred/binary logging over on-device string formatting

Summary: The same log line costs 1675 instructions when formatted to a human-readable string on-device versus 1050 instructions when sent as a raw value plus a format-string ID for the host to decode later, and more efficient logging directly means being able to afford to log more for the same time-and-power budget.

Summary source: run-b, tie on share of the Claims' quoted words (0.36), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa14-f005162-c1

## Question `embedded-framework-bundles-hal-and-executor`

### embedded-framework-bundles-hal-and-executor--p1 — RTIC: framework-only, hardware-level exclusivity where possible; named alternative: Embassy bundles HAL + executor

Summary: The framework aims to provide only the execution/concurrency layer, leaving the platform HAL and PAC to the user, and separately aims to give tasks exclusive access to hardware resources as low-level as possible — ideally hardware-guarded — specifically to avoid needing software-level locking at all.

Summary source: run-b, higher share of the Claims' quoted words (0.77 vs 0.54).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB04-f000227-c5

## Question `embedded-interpreter-stopgap`

### embedded-interpreter-stopgap--p1 — Embedded Rust interpreter as an acceptable stopgap for a missing platform capability

Summary: Running a full ECMAScript interpreter inside their own Wasm module to support `eval`, which the host platform doesn't natively support, is acknowledged plainly as "a runtime on top of a runtime, which doesn't seem optimal, and it isn't" — but it works well enough as a stopgap until native support exists.

Summary source: run-b, higher share of the Claims' quoted words (0.78 vs 0.56).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa14-f004985-c2

## Question `embedded-panics-compile-time-vs-recovery`

### embedded-panics-compile-time-vs-recovery--p1 — Compile time no panic for the one critical task

Summary: For a task nothing else can restart if it crashes, compile it with a no-panic feature so that any unoptimized-away panic becomes a link failure — catching that whole class of crashes at compile time rather than relying on runtime recovery, which has no one above it to fall back on.

Summary source: run-a, tie on share of the Claims' quoted words (0.57), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sa17-f008217-c2

## Question `emscripten-vs-native-rust-wasm`

### emscripten-vs-native-rust-wasm--p1 — Native Rust-to-Wasm over an Emscripten emulation layer

Summary: Emscripten's mocked-dependency emulation layers make compiled binaries bulky and slow, so the choice made is native Rust compiled directly to WebAssembly via `wasm-bindgen`, avoiding those unnecessary emulation layers entirely.

Summary source: run-b, higher share of the Claims' quoted words (0.62 vs 0.44).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sa14-f004985-c1

## Question `emulate-specialization`

### emulate-specialization--p1 — Single-constructor design with an `Option<SyncFn>` field toggled from trait-bound-gated impl blocks, replacing separate RO/RW constructors

Summary: Instead of two separate constructors for read-only versus read-write capability, keep one constructor with a single field (e.g. an `Option<SyncFn>`) that only trait-bound-gated impl blocks (`Read + Write + Seek`) can set to `Some`, which fixed a real bug where the read-write variant's writes silently failed to sync.

Summary source: run-a, tie on share of the Claims' quoted words (0.33), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sb20-f007213-c1

## Question `encode-invariant-in-representation`

### encode-invariant-in-representation--encode-in-types — Encode it in types

Summary: Storing a derived, invariant-preserving value in the type (e.g. log2 of a page size rather than the raw page size) cuts down on the invalid states a data model can represent and the assertions needed elsewhere to guard against them.

Summary source: run-a, tie on share of the Claims' quoted words (0.47), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sb05-f001582-c1

### encode-invariant-in-representation--p1 — Make invalid states unrepresentable

Summary: A data model's structures should be defined so invalid states are literally unrepresentable — for example, an enum with one variant per format version makes it impossible to construct a value combining fields that version can't have.

Summary source: run-a, tie on share of the Claims' quoted words (0.75), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-bk03-f000267-c2

## Question `enum-glob-import-in-match`

### enum-glob-import-in-match--p1 — Favors the local glob import for terser match arms

Summary: Match arms on an enum should use a local glob import (`use Enum::*;`) inside the method to drop the type-qualified path from each arm, for terser match arms.

Summary source: run-a, higher share of the Claims' quoted words (0.60 vs 0.40).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sR03-f000763-c3

## Question `enum-vs-dyn-trait-closed-set`

### enum-vs-dyn-trait-closed-set--open-trait-for-extensibility — An open trait for extensible policy

Summary: A closed enum enumerating access-control configurations is replaced by an open trait with connect/disconnect hooks, so embedders can implement arbitrary policy logic instead of being limited to choosing among a fixed set of enum variants.

Summary source: run-b, higher share of the Claims' quoted words (0.46 vs 0.23).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR10-f004741-c3

### enum-vs-dyn-trait-closed-set--static-by-default — Enums or generics; avoid `dyn` when possible

Summary: For a fixed, known set of kinds, enums (or an enum-dispatch-style approach) should be the default over `Box<dyn Trait>`, since dynamic dispatch is the slowest and least idiomatic option and enums drop heap allocation and vtable indirection while staying entirely safe — including deciding, after discussion, to redo a graph representation as node enums rather than trait objects.

Summary source: run-a, higher share of the Claims' quoted words (0.73 vs 0.55).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa07-f003704-c3, a-sa17-f007884-c1, a-sa17-f007884-c2

### enum-vs-dyn-trait-closed-set--unsafe-unions-for-memory — Unsafe unions when memory must be squeezed

Summary: Beyond the safe enum-dispatch default, unsafe unions with hand-rolled tagged pointers (`ManuallyDrop`, pointer aliasing via `transmute_copy`) are a legitimate, deliberate escalation past safe Rust when shrinking a value's memory layout below what the default enum representation would give is worth the added unsafety.

Summary source: run-a, tie on share of the Claims' quoted words (0.08), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa17-f007884-c3

## Question `enum-vs-flags-and-optionals`

### enum-vs-flags-and-optionals--enum — Use a (non-exhaustive) enum

Summary: Multi-outcome or growing state should be modeled as a (often non-exhaustive) enum rather than a bool or a struct of optional fields — replacing two independent fields with enum variants lets future kinds be added without another breaking change, and replacing a boolean flag with a named enum was judged more readable, safer and clearer once implemented.

Summary source: run-a, tie on share of the Claims' quoted words (0.22), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR08-f003531-c1, b-sR08-f003531-c2, b-sR08-f003731-c1

## Question `epoll-vs-io-uring`

### epoll-vs-io-uring--p1 — Epoll for now as the standard tradeoff

Summary: `epoll` is chosen for a hand-built async reactor specifically because it hits the "standard" tradeoff between being too slow and too experimental, with an explicit note that `io_uring` might take over that role in a few years.

Summary source: run-b, higher share of the Claims' quoted words (0.86 vs 0.71).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb21-f008396-c1

## Question `ergonomic-sugar-now-or-later`

### ergonomic-sugar-now-or-later--p1 — Ship the minimal raw mechanism now, add sugar only once it earns it

Summary: Ship the minimal raw mechanism now — a PR thrown together quickly — and only add a macro or trait wrapper for ergonomic sugar later, since there's little reason to add that syntactic dressing before it's shown to carry its weight.

Summary source: run-a, higher share of the Claims' quoted words (0.47 vs 0.41).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa11-f004512-c4

## Question `ergonomics-vs-explicitness`

### ergonomics-vs-explicitness--p1 — Explicitness is an unstated core value

Summary: Explicitness functions as one of Rust's de facto core values even though, ironically, it's never explicitly stated as a goal of the language.

Summary source: run-a, higher share of the Claims' quoted words (0.70 vs 0.60).

Tag: fact (majority; votes fact / tradeoff / fact)

Claims: a-sa28-f012469-c9

### ergonomics-vs-explicitness--p2 — Ergonomics-initiative-RFCs-are-knowingly-controversial

Summary: The 2017 ergonomics-initiative RFCs, pushing implicit sugar into places code was hard to write, are acknowledged by their own author as knowingly controversial and likely to need scaling back — self-aware about trading away some of the language's explicitness for ergonomic convenience.

Summary source: run-b, higher share of the Claims' quoted words (0.64 vs 0.55).

Tag: fact (majority; votes fact / tradeoff / fact)

Claims: a-sa28-f012469-c10

## Question `error-enum-scope-module-vs-function`

### error-enum-scope-module-vs-function--p1 — Scope error enums per-function, not per-module

Summary: Error enums are better scoped per-function/operation than per-module: starting with one large per-module enum proved unwieldy, so the design moved to a nested, scoped hierarchy (e.g. a `DialError` nested inside a `ConnectError`) with names descriptive of the specific failure surface.

Summary source: run-a, higher share of the Claims' quoted words (0.57 vs 0.29).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa14-f005149-c2

## Question `esp32-psram-display-dma-strategy`

### esp32-psram-display-dma-strategy--p1 — Infinite cyclic DMA buffer, never restart transfers

Summary: Feed the display from an infinite, cyclic DMA buffer and never restart transfers — every framebuffer's last DMA descriptor points back to its first, and switching buffers means relinking descriptors rather than restarting anything — though this approach breaks down once PSRAM bandwidth becomes the bottleneck.

Summary source: run-a, higher share of the Claims' quoted words (0.67 vs 0.33).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sT05-f002499-c1

### esp32-psram-display-dma-strategy--p2 — SRAM bounce buffers refilled from PSRAM by Mem2Mem DMA, no XIP

Summary: Use small SRAM bounce buffers refilled from PSRAM framebuffers via Mem2Mem DMA and looping DMA to the LCD, with descriptors to locate the emitted slice via an interrupt and canceling late refills, avoiding XIP from PSRAM entirely — achieving glitch-free output at over 31 FPS, since a CPU-copy alternative was rejected as too slow.

Summary source: run-a, higher share of the Claims' quoted words (0.50 vs 0.38).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sT05-f002499-c2

### esp32-psram-display-dma-strategy--p3 — Bounce buffers with acyclic descriptors, restart per frame

Summary: Cyclic DMA descriptors failed after the very first frame in practice, while switching to acyclic descriptors that restart the transmission after each frame works — described as fine, if "not as nice" as a true infinite loop — with an offer to upstream a generic version of the fix.

Summary source: run-b, higher share of the Claims' quoted words (0.70 vs 0.60).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sT05-f002499-c3

### esp32-psram-display-dma-strategy--p4 — Stay on an I8080 display for a PSRAM-heavy app

Summary: After getting a bounce-buffer renderer working but running into flash contention and PSRAM bandwidth slowing the application down, the practical choice was to not switch device and keep a smaller, lower-resolution I8080 display instead.

Summary source: run-a, tie on share of the Claims' quoted words (0.67), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: b-sT05-f002499-c4

## Question `example-data-domain-struct-vs-generic`

### example-data-domain-struct-vs-generic--p1 — Prefer a small dedicated struct even at the cost of extra ceremony, to show real-world data mapping

Summary: In example/demo code, a small dedicated struct (name, address, email, generated in the app constructor) is preferable to `Vec<Vec<String>>`, even at the cost of extra ceremony that could be called "gold plating," because it demonstrates how to map real-world data into table columns.

Summary source: run-a, higher share of the Claims' quoted words (0.62 vs 0.58).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sR03-f000763-c1

## Question `exclusive-access-default-in-task-api`

### exclusive-access-default-in-task-api--p1 — Default-exclusive, opt-in-shared-for-lock-elision

Summary: A task/resource API should default to exclusive (`&mut`) access to shared state, with shared (`&-`) read-only access available as an opt-in specifically because it lets a task skip the lock API entirely, even when the resource is contended by tasks running at different priorities.

Summary source: run-a, tie on share of the Claims' quoted words (0.69), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sB04-f000227-c1

## Question `executor-agnostic-libraries`

### executor-agnostic-libraries--p1 — Libraries should stay executor/reactor-agnostic

Summary: Libraries exposing async APIs should not depend on a specific executor or reactor unless they genuinely need to spawn tasks or define their own async I/O or timer futures, reasoned directly from the ecosystem's real fragmentation — Tokio's reactor and I/O traits are not directly compatible with async-std or smol's — where only binaries should really own scheduling.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.80).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-bk01-f000233-c12

## Question `explicit-vs-convenience-memory-defaults`

### explicit-vs-convenience-memory-defaults--p1 — Domain dependent tradeoff

Summary: Neither a performance-first nor a convenience-first memory-model default is simply better: one suits systems, embedded programming, and compilers/browser engines, the other suits UI, servers, and other parts of compilers and operating systems, and the overlap between where each is the right choice is expected to keep growing over time.

Summary source: run-b, higher share of the Claims' quoted words (0.56 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR12-f005668-c1

## Question `explicit-vs-implicit-indirection`

### explicit-vs-implicit-indirection--p1 — Explicit favorably framed

Summary: Requiring the programmer to write `Box<T>` for a recursive type's indirection, as Rust does, makes the underlying problem explicit and forces the programmer to deal with it directly, in contrast with a more automatic, compiler-handled approach like Swift's `indirect` keyword.

Summary source: run-a, higher share of the Claims' quoted words (0.89 vs 0.33).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sR12-f005668-c2

## Question `expose-fixed-array-vs-wrapper-type`

### expose-fixed-array-vs-wrapper-type--p1 — Wrap raw array in a semantic type rather than exposing it directly

Summary: A fixed-size array like `[u8; 6]` should be wrapped in a dedicated semantic type with derives and a `Display` implementation, motivated directly by noting that a same-shaped but larger variant (an 8-byte IEEE MAC) could never be returned from the array's current shape.

Summary source: run-b, tie on share of the Claims' quoted words (0.29), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa11-f004265-c1

### expose-fixed-array-vs-wrapper-type--p2 — Return a slice instead of a fixed-size array

Summary: The same author reverses a day later, pushing back on returning the fixed-size array at all and preferring a slice-typed return instead, as the way to keep the door open for a larger variant.

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa11-f004265-c3

## Question `expose-rustc-internals-rustdoc-json`

### expose-rustc-internals-rustdoc-json--p1 — Expose rustc internals via rustdoc json

Summary: Implied trait bounds turn out to be load-bearing for detecting SemVer breaks — missing them produces both false positives and false negatives — and since it's technically infeasible for an external tool to re-derive them while the compiler already has that capability internally, the request made is for the compiler team to expose implied bounds through a structured interface (rustdoc JSON) using those existing internal APIs.

Summary source: run-b, higher share of the Claims' quoted words (0.60 vs 0.55).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sa20-f009698-c4

## Question `extend-foreign-trait-type`

### extend-foreign-trait-type--p1 — Narrow extension methods

Summary: Bolting on another parallel enum type without re-evaluating the complexity of an already fairly unintuitive API is treated with real wariness; a narrowly scoped method or a small set of new enum variants is the preferred fix over adding a whole second type.

Summary source: run-b, higher share of the Claims' quoted words (0.75 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb06-f002027-c1

### extend-foreign-trait-type--p2 — Own parallel type with conversion

Summary: The crate effectively already has "its own" version of the foreign type in practice — currently just a lazy type alias — and users shouldn't need to know or care which one they're going through, so making it a real, independently extensible type of its own is fine even though it's a breaking change.

Summary source: run-b, tie on share of the Claims' quoted words (0.40), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb06-f002027-c2

## Question `externref-in-rust`

### externref-in-rust--keep-out-of-language-core — Leave it to the compiler or runtime

Summary: WebAssembly's design oddities — even ones with prior art like Clang's own non-standard `__externref_t` extension, unmatched by GCC or MSVC — shouldn't be papered over by changing the language core; languages shouldn't change at such a fundamental level to support something this niche.

Summary source: run-a, higher share of the Claims' quoted words (0.78 vs 0.56).

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: a-sa29-f013113-c4

### externref-in-rust--must-fit-abstract-machine — Reject types outside the Abstract Machine

Summary: The proposal introduces a fundamentally new kind of thing to Rust whose semantics can't be expressed in the Abstract Machine that MIR-transform and MIR-to-LLVM-IR correctness proofs rely on — an unprecedented kind of break, worse than prior type-system-assumption-breaking RFCs — and without integration into `Result`, async, `==`, or newtypes the feature will feel bolted on.

Summary source: run-a, higher share of the Claims' quoted words (0.44 vs 0.33).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa29-f013113-c2

### externref-in-rust--new-restricted-lang-type — Add a restricted lang-item type; JS interop justifies a language change

Summary: JavaScript interop is a major quality-of-life story, not a niche one, and is worth solving at the language level: a new restricted lang-item type — an opaque, unforgeable reference to a WebAssembly host value, legal only as a bare top-level type of function parameters/returns/locals, lowering to Wasm's `externref` — lets host references marshal directly across foreign calls for interoperability and performance, though the proposal still needs to be justified for Rust on its own merits.

Summary source: run-a, higher share of the Claims' quoted words (0.82 vs 0.77).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa29-f013113-c1, a-sa29-f013113-c5

### externref-in-rust--table-index-in-rust-code — Table-index wrapper, real `externref` only at FFI

Summary: A non-zero-cost wrapper could work better than a first-class language type: `externref` would act as a table index everywhere in Rust-only code, with the real WebAssembly `externref` crossing only at FFI boundaries, and an optimization pass could elide the table insert/extract round-trip whenever a value is merely passed straight through.

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa29-f013113-c3

## Question `extract-single-use-function`

### extract-single-use-function--extract-for-communication — Extract into a named function or method

Summary: Pulling logic into its own named method is valued even for a single caller, because a well-named function with a defined input and output lets a reader trust what it does without re-deriving the logic themselves — functions are "a tool for communicating blocks of code," not just for reuse — and the same reasoning applies to a check duplicated verbatim at two call sites, which should be one method on the owning type documenting the real contract so drift becomes a compile error rather than a silent bad write.

Summary source: run-b, higher share of the Claims' quoted words (0.59 vs 0.52).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR12-f005085-c1, b-sb04-f001392-c5

### extract-single-use-function--keep-inline — Keep it inline where used

Summary: Moving logic this specific to one caller into its own method isn't seen as useful, and naming it risks being actively misleading about what the extracted function actually guarantees versus what it merely happens to do at its one call site.

Summary source: run-b, tie on share of the Claims' quoted words (0.67), shorter summary.

Tag: taste (majority; votes taste / tradeoff / taste)

Claims: b-sb04-f001392-c6

## Question `fast-path-complexity`

### fast-path-complexity--p1 — Absolute magnitude decides

Summary: Advocates say the right lens is the absolute per-call cost, not the relative one: a regression that looks huge in percentage terms on old or constrained hardware (a Raspberry Pi) can still be tens of nanoseconds on current hardware, and that absolute number, not the ratio, is what should decide whether the extra code complexity of a fast path is worth keeping.

Summary source: run-a, tie on share of the Claims' quoted words (0.25), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb04-f001392-c1

### fast-path-complexity--p2 — Relative impact on constrained hw matters

Summary: Advocates hold the opposite framing matters more: because a construct sits on a hot path used across huge volumes of rendered output, even a "relatively small" per-call regression compounds significantly on constrained/older hardware; their own benchmarks on low-power devices showed double-digit percentage regressions without the fast path, so relative impact on the hardware that most needs it is the number that should decide.

Summary source: run-b, higher share of the Claims' quoted words (0.50 vs 0.33).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb04-f001392-c2

## Question `feature-flag-trunk-vs-long-branch`

### feature-flag-trunk-vs-long-branch--p1 — Feature flag gate on trunk

Summary: Advocates say experimental or breaking work belongs on main behind a Cargo feature flag, not on a long-lived branch, because that's what keeps main continuously releasable.

Summary source: run-a, tie on share of the Claims' quoted words (0.54), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-bk03-f000267-c11

## Question `feature-flags-vs-generic-wiring`

### feature-flags-vs-generic-wiring--p1 — Generic wiring over feature flags

Summary: Advocates hold that generic, type-level component wiring is less error-prone than Cargo feature flags because it lets every alternative implementation coexist and be tested simultaneously, instead of requiring combinatorial feature-flag test coverage.

Summary source: run-b, higher share of the Claims' quoted words (0.83 vs 0.67).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa16-f007175-c1

## Question `feature-flags-vs-separate-crates`

### feature-flags-vs-separate-crates--p1 — Modular library first

Summary: Advocates frame the choice as a library-first design commitment: build the project as independently reusable library crates from the start, with a contributing guide naming this as a scope boundary against a monolithic, feature-flagged binary.

Summary source: run-a, only run whose summary covers the final Claims.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-bk03-f000267-c3

### feature-flags-vs-separate-crates--split-into-crates — Split into separate crates or modular crates joined by traits

Summary: Advocates say functionality should be factored out of one crate into separate, independently versioned and releasable crates — moving optional components to their own repos, keeping new integrations out of a main crate to shorten release cycles, splitting a monolithic domain into per-domain sub-crates behind a stable interface crate, building a small core with everything else swappable behind traits, or splitting a single crate into a workspace where only the required piece is a mandatory dependency.

Summary source: run-a, only run whose summary covers the final Claims.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR13-f004685-c2, a-sa18-f008651-c1, b-sR05-f002151-c1, b-sR12-f005120-c1, b-sb25-f011435-c1

## Question `feature-misuse-responsibility`

### feature-misuse-responsibility--p1 — Structure feature placement to discourage misuse

Summary: Advocates say where a feature lives changes how safely it gets used: placing a feature on a crate whose accidental activation has visible, non-wasm-target effects makes wrongful unconditional enabling by a downstream crate a more visible, more punished mistake than placing it somewhere a wrong enable silently does nothing.

Summary source: run-a, higher share of the Claims' quoted words (0.20 vs 0.00).

Tag: taste (majority; votes tradeoff / taste / taste)

Claims: a-sa06-f003558-c3

### feature-misuse-responsibility--p2 — Misuse is the misusing crate's bug, not the exposing crate's design problem

Summary: Advocates hold this is "a solution in search of a problem": crates cannot be engineered into behaving correctly by restructuring an API, misbehaving crates should have issues or PRs filed against them directly, and moving the feature elsewhere just relocates the same possible mistake rather than removing it.

Summary source: run-b, higher share of the Claims' quoted words (0.75 vs 0.00).

Tag: taste (majority; votes tradeoff / taste / taste)

Claims: a-sa06-f003558-c4

## Question `feature-naming-mechanism-vs-capability`

### feature-naming-mechanism-vs-capability--p1 — Name a feature for its literal mechanism, not the capability it implies

Summary: Advocates hold a feature name should describe only the mechanism it literally provides; naming a hooking-only feature "tracking" wrongly implies the library itself does allocation tracking with little setup, so the name should be more explicit that it adds hooking and nothing more.

Summary source: run-b, tie on share of the Claims' quoted words (0.53), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa11-f004512-c5

## Question `ffi-bindings-lag-pause-or-ship`

### ffi-bindings-lag-pause-or-ship--p1 — Pause and fix ffi first

Summary: Advocates say when non-Rust bindings can't meet the "just works" bar the project holds native Rust usage to, ship no more degraded releases of them — stop and fix the FFI/bridging story itself first, accepting the ecosystem-fragmentation risk of a pause rather than keep shipping a substandard experience.

Summary source: run-a, higher share of the Claims' quoted words (0.38 vs 0.23).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa04-f002665-c1

## Question `ffi-copy-vs-share`

### ffi-copy-vs-share--convert-or-copy — Convert or copy into idiomatic types (copy across FFI, Rust collections, lean on generated glue)

Summary: Advocates say copying immutable data across the boundary, rather than sharing a pointer into it, is generally safer and easier: it costs a small performance penalty but guarantees that memory management on one side of a binding can't affect the other side, which is judged worth it more often than not.

Summary source: run-a, tie on share of the Claims' quoted words (0.75), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb20-f007678-c2

### ffi-copy-vs-share--p2 — Minimize copying/serializing across the JS↔wasm boundary; expose long-lived Rust data as opaque handles, return small copyable results

Summary: Advocates hold that a good JS↔wasm interface minimizes copying and serialization by keeping large, long-lived data as Rust types living in wasm linear memory, exposed to JS only as opaque handles, with JS calling functions that do the heavy work and return small, copyable results; a delta/diff-based alternative is acknowledged as viable but not adopted because it is harder to implement.

Summary source: run-b, tie on share of the Claims' quoted words (0.52), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB02-f000256-c3, b-bk02-f000256-c2

### ffi-copy-vs-share--p3 — Replace a Display-generated JS String with a raw pointer + Uint8Array overlay onto wasm linear memory

Summary: Advocates point to a concrete before/after: generating and allocating a Rust String and letting wasm-bindgen convert it to a JS string makes unnecessary copies, so the fix returns a raw pointer and lets JS read the cell buffer directly out of wasm memory via a typed-array overlay instead.

Summary source: run-a, higher share of the Claims' quoted words (0.67 vs 0.60).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-bk02-f000256-c3

### ffi-copy-vs-share--share-or-borrow — Pass borrowed references to avoid conversion overhead

Summary: Advocates hold that passing `&str` rather than `String` across the boundary is the efficient choice, using references where possible instead of converting/copying, alongside minimizing call count and profile tuning.

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb22-f008914-c2

## Question `ffi-tag-unwind-vs-abort`

### ffi-tag-unwind-vs-abort--p1 — Tag unwinds explicitly

Summary: Advocates say between two workable options — marking all definitely-abort errors, or marking all definitely-unwind errors — they chose to tag the recoverable (unwind) case explicitly, because it fit more easily on top of their existing raw WAT-level exception-handling implementation.

Summary source: run-a, higher share of the Claims' quoted words (0.33 vs 0.25).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa12-f004598-c2

## Question `ffi-ui-state-snapshots-vs-diffs`

### ffi-ui-state-snapshots-vs-diffs--p1 — Whole snapshot(chosen)

Summary: Advocates hold that exposing the whole state as a pointer into linear memory each tick is the right call, naming a delta/diff-based design as a viable alternative that is not adopted because it is more difficult to implement.

Summary source: run-b, tie on share of the Claims' quoted words (0.42), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB02-f000256-c4

### ffi-ui-state-snapshots-vs-diffs--p2 — Rust side tracks and emits diffs

Summary: Advocates hold that, after iterating through worse designs (manual return-value wiring, per-field event handlers, an all-optional model needing manual checks), the Rust side should track field changes and emit a diff enum via a derive macro, so the receiving side applies it through an exhaustive switch that fails to compile if a new field goes unhandled.

Summary source: run-b, tie on share of the Claims' quoted words (0.36), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa18-f008389-c1

## Question `fields-in-traits`

### fields-in-traits--p1 — Mildly supportive uncertain use case

Summary: Advocates land on a shrug: the feature is limited and distinct enough that it doesn't seem to harm Rust's design in any way, but they personally don't have a compelling use case that would make them push for it.

Summary source: run-a, higher share of the Claims' quoted words (0.67 vs 0.56).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb19-f007207-c1

## Question `final-trait-methods`

### final-trait-methods--p1 — Support final methods

Summary: Advocates point to concrete design work already done: a drafted RFC ("Trait method impl restrictions") using the reserved `final` keyword, and a proposed `#[non_overridable]` attribute, both meant to let a trait forbid overriding specific methods for correctness reasons and potentially shrink vtables by excluding such methods.

Summary source: run-a, tie on share of the Claims' quoted words (0.35), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa19-f009316-c1, a-sa19-f009316-c2

### final-trait-methods--p2 — Skeptical limited value vs free functions

Summary: Advocates hold final trait methods offer little beyond "minor sugar," since any trait bound or call used inside such a method could just as well be replicated with a corresponding free function.

Summary source: run-b, tie on share of the Claims' quoted words (0.25), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa19-f009316-c3

### final-trait-methods--p3 — Final methods need vtable for soundness

Summary: Advocates hold that final trait methods cannot simply desugar to free functions and must remain reachable through the vtable for soundness: a concrete example shows a final method called through `dyn Trait` observably differing from an equivalent free function, and a filed I-unsound bug shows nightly's experimental final associated functions already misbehave inconsistently under `dyn Trait` dispatch.

Summary source: run-b, tie on share of the Claims' quoted words (0.36), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa19-f009316-c4, a-sa19-f009316-c5

## Question `fine-grained-reactivity-vs-vdom`

### fine-grained-reactivity-vs-vdom--p1 — Fine grained reactivity

Summary: Advocates say a fine-grained reactivity system, where only the specific parts of an app that need updating are updated, is the right model for a Rust web UI framework, contrasted implicitly with vdom-diffing frameworks.

Summary source: run-a, higher share of the Claims' quoted words (0.78 vs 0.56).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR14-f005702-c1

## Question `fixed-point-loop-vs-event-retrigger`

### fixed-point-loop-vs-event-retrigger--p1 — Simple iterative bounded

Summary: Advocates hold that a simple, bounded iterative fixed-point loop (reduced from 100 passes to 10) is the safer, bug-free choice over a more efficient but more complex graph-retrigger design.

Summary source: run-b, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa07-f003704-c2

## Question `fixed-vs-dynamic-matrix-sizing`

### fixed-vs-dynamic-matrix-sizing--p1 — Prefer fixed/static sizing whenever possible

Summary: Advocates hold that fixed, compile-time-known matrix sizing should be preferred whenever possible, because dynamic resizing always produces heap-allocated results when the output size can't be deduced at compile time.

Summary source: run-b, higher share of the Claims' quoted words (0.79 vs 0.50).

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: a-sB01-f000217-c3

## Question `foreign-keys-vs-app-integrity`

### foreign-keys-vs-app-integrity--app-enforced-integrity — Drop foreign keys; enforce integrity in application code

Summary: Advocates report learning this the hard way: on an eventually consistent store, foreign-key checks broke across sequential writes, so all foreign keys were removed and referential integrity was moved into application code.

Summary source: run-a, higher share of the Claims' quoted words (0.88 vs 0.75).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sT07-f004166-c2

## Question `form-values-list-vs-scalar-deserialization`

### form-values-list-vs-scalar-deserialization--p1 — Disambiguate scalar vs. list by observed value count (no schema change)

Summary: Advocates hold that for multi-valued form elements like a `<select multiple>`, a deserializer should infer scalar-vs-list per field from how many values were actually observed, rather than adding an explicit schema/cardinality marker to the wire format.

Summary source: run-b, tie on share of the Claims' quoted words (0.36), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-01-f000543-c1

## Question `frontend-hook-naming`

### frontend-hook-naming--p1 — Use_ prefixed noun phrase

Summary: Advocates hold that, absent any established convention, hooks should be named with a `use_<noun>` pattern (e.g. `use_search_query`, `use_location_hash`).

Summary source: run-b, tie on share of the Claims' quoted words (0.27), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: a-sR07-f002271-c2

## Question `fullstack-reactive-complexity-essential`

### fullstack-reactive-complexity-essential--p1 — The hooks/reactivity complexity in a fullstack framework is essential, not accidental

Summary: Advocates hold that the complexity practitioners feel around a fullstack framework's hooks and reactivity — including that breaking hook rules silently misbehaves rather than erroring — reflects that "full stack stuff is complicated," not that the framework added complexity that wasn't needed.

Summary source: run-b, higher share of the Claims' quoted words (0.60 vs 0.30).

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: b-sb20-f007290-c2

## Question `futures-crate-vs-alternatives`

### futures-crate-vs-alternatives--p1 — Avoid futures crate use alternatives

Summary: Advocates dropped the mainline `futures` crate entirely after finding bugs in its unsafe-heavy combinators (`FuturesUnordered`) that were impractical to fix upstream, replacing it with futures-lite for simple combinators, futures-buffered in place of `FuturesUnordered`, and futures-util only for what neither covers.

Summary source: run-a, higher share of the Claims' quoted words (0.33 vs 0.29).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb17-f005159-c3

## Question `game-logic-in-scripting-layer`

### game-logic-in-scripting-layer--p1 — Keep the native (Rust) layer a thin, general-purpose platform and put effectively all game logic in the hosted scripting/VM language, rather than building a bridge for native code to touch mutable game state directly

Summary: Advocates hold that, per long-standing precedent (browser JS games, SCUMM, Another World), essentially all game logic should live in the hosted scripting language, with the unmanaged native layer staying a general-purpose platform that has "nothing to do with the game," and the real state of record living in serialized data files rather than in either language's live objects.

Summary source: run-b, tie on share of the Claims' quoted words (0.56), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb26-f013214-c6

## Question `gamedev-ecosystem-maturity`

### gamedev-ecosystem-maturity--p1 — After three years building a demanding 3D metaverse client, the Rust graphics crate ecosystem (WGPU, Rend3, winit, egui) is not yet "ready for prime time"

Summary: Advocates hold that Rust's 3D/graphics crate ecosystem "isn't ready for prime time": the crates are tightly coupled with frequent breaking upgrades and rustdoc-only documentation, and over half of three years on a demanding project went to filing and chasing ecosystem bugs rather than the actual application, with only partial, incremental improvement over time.

Summary source: run-b, higher share of the Claims' quoted words (0.67 vs 0.50).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sb26-f013214-c1

### gamedev-ecosystem-maturity--p2 — Rust game dev is not a flop, just early — game-industry technology adoption is inherently slow regardless of a technology's merits

Summary: Advocates frame the situation with the Gartner "Trough of Disillusionment" label as expected and fine, drawing an analogy to games staying on MS-DOS for years after Windows existed — the switch happened only once 3D accelerator cards forced it, not because Windows was inherently better — and argue Rust gamedev lacks an equivalent forcing function yet, so any transition will simply take years or decades.

Summary source: run-a, higher share of the Claims' quoted words (0.57 vs 0.43).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb26-f013214-c2

## Question `gating-pre-1-0-dependency-integrations`

### gating-pre-1-0-dependency-integrations--p1 — Cfg gate hidden impls not unstable attribute

Summary: Advocates hold private structs/functions don't need to be documented as `#[unstable]`; hidden impls can simply be `#[cfg(feature = "unstable")]`-gated instead.

Summary source: run-b, tie on share of the Claims' quoted words (0.33), shorter summary.

Tag: taste (majority; votes tradeoff / taste / taste)

Claims: b-sb09-f002615-c1

### gating-pre-1-0-dependency-integrations--p2 — Per function not per block annotation

Summary: Advocates say the `#[unstable]` attribute belongs on each individual function, not on whole inherent impl blocks.

Summary source: run-a, higher share of the Claims' quoted words (0.75 vs 0.62).

Tag: taste (majority; votes tradeoff / taste / taste)

Claims: b-sb09-f002615-c2

### gating-pre-1-0-dependency-integrations--p3 — Blanket unstable flag

Summary: Advocates hold gating behind one coarse "unstable" flag is justified because the underlying dependency (`ufmt`) is itself still pre-1.0.

Summary source: run-b, tie on share of the Claims' quoted words (0.40), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb09-f002615-c3

### gating-pre-1-0-dependency-integrations--p4 — Need an explicit policy

Summary: Advocates hold that ad hoc fixes — removing one dependency's integration, or picking blanket-vs-per-dependency gating case by case — don't resolve the underlying question, since other pre-1.0 dependencies (rand-core, embassy-embedded-hal, log) raise the same issue; neither extreme (one coarse flag, or per-dependency-version features) feels right, and the project needs a general policy for handling pre-1.0 optional trait dependencies.

Summary source: run-b, higher share of the Claims' quoted words (0.15 vs 0.13).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb09-f002615-c4, b-sb09-f002615-c5, b-sb09-f002615-c8

### gating-pre-1-0-dependency-integrations--p5 — Per dependency subfeature

Summary: Advocates propose expanding the single "unstable" feature into named per-dependency sub-features, like `unstable-ufmt`.

Summary source: run-a, tie on share of the Claims' quoted words (0.33), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb09-f002615-c6

### gating-pre-1-0-dependency-integrations--p6 — Just remove and readd on demand

Summary: Advocates say it's simpler to remove an optional integration outright — as was already done for embedded-hal-nb — and re-add it later only if users complain, rather than spend more time designing feature-flag machinery than the removal itself would take.

Summary source: run-a, higher share of the Claims' quoted words (0.67 vs 0.50).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb09-f002615-c7

## Question `generated-crates-escape-hatches`

### generated-crates-escape-hatches--p1 — Generated crates need handwritten escape hatches

Summary: Advocates hold that even a ~95%-generated crate needs a dedicated handwritten file for what the schema can't express (e.g. arithmetic trait impls on a generated type), with the generator written to never overwrite that file.

Summary source: run-b, higher share of the Claims' quoted words (0.60 vs 0.20).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa23-f011186-c4

## Question `generated-size-vs-runtime-performance`

### generated-size-vs-runtime-performance--p1 — Favors performance over output size for this change

Summary: Advocates hold that generating JS bindings for WebIDL dictionary setters instead of using `Reflect` is worth the larger binding size because it's more performant.

Summary source: run-b, tie on share of the Claims' quoted words (0.80), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR03-f001160-c2

## Question `generic-over-blocking-async`

### generic-over-blocking-async--p1 — Generic over mode

Summary: Advocates hold blocking and async variants of a peripheral driver should share one implementation generic over the mode, rather than duplicating methods for each.

Summary source: run-b, tie on share of the Claims' quoted words (0.40), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb05-f001512-c5

## Question `generics-vs-dyn-for-abstraction`

### generics-vs-dyn-for-abstraction--p2 — Use trait objects instead of generic type parameters to cut code size, accepting slower indirect calls and lost per-type inlining

Summary: Advocates hold that using trait objects instead of generic type parameters is worth it to shrink `.wasm` code size, since monomorphized generics emit one function copy per concrete type: the explicit cost is losing compiler optimization opportunities and per-type inlining, paid for indirect, dynamically dispatched calls.

Summary source: run-b, higher share of the Claims' quoted words (0.71 vs 0.52).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB02-f000256-c10, b-bk02-f000256-c9

### generics-vs-dyn-for-abstraction--static-by-default — Enums or generics; avoid `dyn` when possible

Summary: Advocates hold that generics/enums should be favored over `dyn Trait` by default: `dyn Trait` is a valid dependency-injection mechanism but its benefits are "extremely narrow" relative to its downsides, type erasure "often hurts more than it helps" without a motivation beyond looking "more abstract," trait objects are "not nearly as capable as generics" for some abstractions, and one maintainer proposed replacing a trait's runtime type erasure and up/down-casting with an associated type instead.

Summary source: run-b, tie on share of the Claims' quoted words (0.44), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa07-f003704-c1, a-sa30-f013276-c3, a-sa30-f013276-c4, a-sa30-f013276-c7

## Question `git-storage-database-decentralized`

### git-storage-database-decentralized--p1 — Rebuild Git's storage engine on a database and decentralize hosting rather than depend on a centralized host

Summary: Advocates hold that because centralized hosts like GitHub can unilaterally access all data or use it for AI training or deletion, Git object storage should move into a distributed database (mirroring Google Piper and Meta Sapling) with a P2P network layered on top, so repositories can be cloned and pushed without depending on any single central node.

Summary source: run-b, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb23-f011178-c1

## Question `global-statics-vs-per-request-state`

### global-statics-vs-per-request-state--p1 — Prefer per request scoped state

Summary: Advocates hold that once one instance can serve concurrent in-flight requests, any static, module-level, or `OnceCell` "global" state must be audited and moved to per-request state or explicit synchronization.

Summary source: run-b, tie on share of the Claims' quoted words (0.73), shorter summary.

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: b-sR10-f004809-c2

## Question `gpu-async-await-vs-dsl`

### gpu-async-await-vs-dsl--p1 — Reuse existing async model over new dsl

Summary: Advocates hold that Rust's `Future` trait and async/await already provide the right abstraction for structured, composable GPU concurrency — encoded in an existing language without committing to a specific execution model, letting an existing executor (Embassy) be ported with very few changes — over building a new purpose-built DSL/compiler stack like JAX, Triton or CUDA Tile, while acknowledging it still carries async/await's function-coloring problem.

Summary source: run-b, higher share of the Claims' quoted words (0.84 vs 0.74).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb21-f008808-c1

## Question `greptimedb-write-api-choice`

### greptimedb-write-api-choice--p1 — Pick the write API by workload shape (Regular for low-latency/small-batch, Bulk for high-throughput/delay-tolerant), and tune parallelism/compression to the actual bottleneck rather than using one default configuration

Summary: Advocates hold the choice between GreptimeDB's Regular and Bulk Stream Insert write APIs should be made by workload shape — Regular for real-time alerting/IoT/dashboards, Bulk for ETL/log collection/historical import — backed by a benchmark showing Bulk ~49% faster under compression (155,099 vs 104,237 rows/s on 2M rows), with parallelism and compression (Zstd vs LZ4) tuned to whichever resource is actually the bottleneck.

Summary source: run-b, tie on share of the Claims' quoted words (0.12), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sb25-f012642-c1

## Question `grouped-vs-field-optionality`

### grouped-vs-field-optionality--p1 — Grouped optionality

Summary: Advocates hold that when several query parameters only make sense together, semantically you want to know whether all of them were specified as a group, not check a mess of several individual `Option` values.

Summary source: run-b, higher share of the Claims' quoted words (0.60 vs 0.53).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb08-f002538-c1

### grouped-vs-field-optionality--p2 — Field level optionality

Summary: Advocates recommend wrapping every query field in `Option` individually, arguing this best reflects the reality of how query parameters actually arrive, and report never having seen a real case where a set of parameters is optional as a whole group rather than one by one.

Summary source: run-a, tie on share of the Claims' quoted words (0.67), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb08-f002538-c2, b-sb08-f002538-c3

## Question `gui-accessibility-first-class`

### gui-accessibility-first-class--p1 — First class requirement

Summary: Advocates hold that Windows support, screen-reader accessibility and IME input are core seriousness criteria for evaluating a Rust GUI framework, not afterthoughts — if these rank below chasing trends, "you are not serious."

Summary source: run-b, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb21-f008390-c4

## Question `gui-custom-renderer-vs-native`

### gui-custom-renderer-vs-native--p1 — Build a custom modular GPU-based renderer rather than reuse an existing engine

Summary: Advocates position their renderer (Blitz) against unnamed "existing solutions" as free, open-source, and extremely modular — a hybrid that alternates native system widgets with a custom GPU-based drawing layer rather than fully wrapping native widgets or an existing browser engine.

Summary source: run-a, higher share of the Claims' quoted words (0.89 vs 0.78).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa26-f011305-c6

## Question `hal-driver-typestate`

### hal-driver-typestate--encode-in-types — Encode it in types

Summary: Advocates hold a driver's mode should be a typestate generic parameter (e.g. `Uart<T, M>` with `M` = `Blocking`/`Async`), determined by how the driver is constructed rather than by a cargo feature flag.

Summary source: run-b, tie on share of the Claims' quoted words (0.62), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb03-f000715-c1

### hal-driver-typestate--runtime-or-raw — A simpler runtime mechanism or raw form

Summary: Advocates had a similar runtime-binding idea independently, arrived at without introducing a typestate at all.

Summary source: run-a, higher share of the Claims' quoted words (0.14 vs 0.00).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb03-f000715-c2

### hal-driver-typestate--typestate-costly — Typestate is possible but costly

Summary: Advocates concede type-state could resolve an ambiguity (default TX/RX pins) but flag that it adds ongoing complexity that becomes annoying later.

Summary source: run-a, higher share of the Claims' quoted words (0.57 vs 0.43).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb05-f001512-c2

## Question `hal-expose-private-facilities`

### hal-expose-private-facilities--p1 — HAL should expose a public version of the private cache-flush function

Summary: Advocates, after having to copy out a private cache-flush function definition to get their code working, say it's worth making a public version of that facility available since it's required.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.67).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sT05-f002499-c8

## Question `handle-identity-traits-vs-store-methods`

### handle-identity-traits-vs-store-methods--p1 — Store scoped explicit methods

Summary: Advocates say pointer-identity equality on a bare handle is surprising because it doesn't hold across import/export boundaries even for the same underlying function, so correct identity needs a store borrow and must be separate methods (`is_same(&store, ...)`, `identity_key(&store)`) rather than literal `Eq`/`Hash` impls.

Summary source: run-a, higher share of the Claims' quoted words (0.48 vs 0.43).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sb16-f005000-c7, b-sb16-f005000-c8

### handle-identity-traits-vs-store-methods--p2 — Exclude lazily populated field from identity key

Summary: Advocates report discovering a candidate identity-key field starts as `None` and gets filled in later, so using it alone as a hash/identity key would collide two never-imported functions and change a function's own key mid-lifetime, breaking `HashMap` use — so that field is excluded and `(vmctx, array_call)` plus `type_index` is used instead.

Summary source: run-a, higher share of the Claims' quoted words (0.42 vs 0.26).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sb16-f005000-c9

## Question `hard-dependency-vs-pluggable-interface`

### hard-dependency-vs-pluggable-interface--hard-dependency-behind-feature — A hard dependency behind a feature flag is fine

Summary: Advocates hold a hard dependency is fine as long as it sits behind a feature flag, rather than requiring a fully pluggable interface.

Summary source: run-b, higher share of the Claims' quoted words (0.83 vs 0.67).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR06-f001989-c2

### hard-dependency-vs-pluggable-interface--pluggable-interface — Keep a pluggable interface

Summary: Advocates want to avoid a hard dependency that would force a new release whenever an unrelated crate releases, and make a swappable interface (e.g. TLS crypto provider via feature flags) so platforms where the default backend can't build, or orgs that mandate a different certified backend, aren't stuck.

Summary source: run-a, higher share of the Claims' quoted words (0.42 vs 0.32).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR06-f001989-c1, a-sR13-f004586-c1

## Question `hardware-interrupt-scheduling`

### hardware-interrupt-scheduling--p1 — Hardware-interrupt-driven (SRP-based) scheduling preferred over software-kernel scheduling

Summary: Advocates argue the Cortex-M hardware interrupt/priority model maps directly onto Stack Resource Policy scheduling, giving zero-cost, compile-time-computed ceilings that a thread-based RTOS's software kernel can't reach.

Summary source: run-a, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sB01-f000227-c2

## Question `hook-api-pointer-vs-address`

### hook-api-pointer-vs-address--p1 — Keep the raw pointer type in the hook API rather than reducing to an address

Summary: Advocates hold the pointer should be passed as-is to hooks to avoid loss of information, trusting the caller not to alter it.

Summary source: run-b, higher share of the Claims' quoted words (0.62 vs 0.50).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa11-f004512-c2

### hook-api-pointer-vs-address--p2 — An address is sufficient information for the hook

Summary: Advocates respond that they aren't sure what information a hook would need beyond the pointer's address.

Summary source: run-a, tie on share of the Claims' quoted words (0.83), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa11-f004512-c3

## Question `host-and-embedded-cargo-layout`

### host-and-embedded-cargo-layout--p1 — Separate projects

Summary: Advocates keep host and embedded/cross-compiled code as fully separate, non-workspace Cargo projects when the toolchains differ and one side needs a patched dependency the other doesn't.

Summary source: run-a, higher share of the Claims' quoted words (0.31 vs 0.25).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR14-f004865-c1

## Question `hot-patching-for-iteration`

### hot-patching-for-iteration--faster-codegen-backend — Faster full rebuilds via an alternate codegen backend

Summary: Advocates propose adding the Cranelift codegen backend as an optional flag for hot-reload builds, reporting it roughly halved measured build times on their own machine.

Summary source: run-a, tie on share of the Claims' quoted words (0.17), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb09-f002719-c2

### hot-patching-for-iteration--hot-patch — Hot-patch for iteration speed

Summary: Advocates hold that hot-patching a running binary (Subsecond: recompiling only changed crates and linking them to hardcoded addresses at runtime, skipping the normal link step) is the way to get near-instant iteration, accepting "a huge number of quirks, edge cases, incomprehensible behavior" to make it work, and treat remaining rustc-level costs (like incremental-artifact disk copying) as further ground to close toward "blink and miss it" hotpatch speed.

Summary source: run-b, only run whose summary covers the final Claims.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa26-f011305-c5, b-sb09-f002719-c1, b-sb09-f002719-c3

## Question `http-body-unknown-size`

### http-body-unknown-size--p1 — Distinguish unknown from zero

Summary: Advocates want `impl IntoResponse for ()` to use an explicit "unknown size" body instead of an empty one, arguing that special-casing `content-length: 0` when the true size can't be cheaply known is conceptually wrong.

Summary source: run-a, tie on share of the Claims' quoted words (0.71), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa12-f004637-c1

### http-body-unknown-size--p2 — Cautious narrow fix

Summary: Advocates hold that changing the default to "unknown size" is too broad a change, risking silent behavior changes for unrelated responses that don't care about HEAD requests; the fix should work without requiring unfamiliar users to opt in explicitly.

Summary source: run-b, higher share of the Claims' quoted words (0.62 vs 0.46).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa12-f004637-c2

## Question `http-error-status-in-result`

### http-error-status-in-result--errors-in-err-channel — Split success and error types so `?` works

Summary: Advocates grant that splitting response variants into a Result-like type — 2xx/3xx on one side, 4xx/5xx on the other — would make the `?` operator usable again, at the cost of extra library-side complexity (e.g. a parallel `SuccessStatusCode` type).

Summary source: run-a, higher share of the Claims' quoted words (0.50 vs 0.44).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-saL1-f005454-c2, a-saL1-f005454-c3

### http-error-status-in-result--unified-response-type — Errors are ordinary responses (`Ok(response)`, one enum)

Summary: Advocates put every HTTP response — success and error alike — into one enum or return type returned directly by the handler, since there aren't really "successful" or "unsuccessful" responses, just responses; one advocate frames a drop-in `Ok(response)` middleware that "just works" the moment it's added, worth the cost of a baked-in response shape, as the reason an escaping `Err` gets mistranslated by upstream infrastructure (e.g. API Gateway) into a generic 502 instead of the deliberately designed 401/403/429/500.

Summary source: run-a, higher share of the Claims' quoted words (0.48 vs 0.22).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-saL1-f005454-c1, b-sb22-f008906-c3, b-sb22-f008906-c4

## Question `human-written-code-standard`

### human-written-code-standard--human-written-for-critical-code — Hold critical work to human-written-only

Summary: Advocates state, as a personal standard rather than an argued position, that all of a project's core code — and even the blog post describing it — is human-written, after an earlier LLM-assisted attempt "proved controversial."

Summary source: run-a, higher share of the Claims' quoted words (0.50 vs 0.42).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa15-f005821-c2

### human-written-code-standard--light-review-for-peripheral-code — A brief check is enough for peripheral code

Summary: Advocates find it acceptable to let an LLM write an entire peripheral component outside their own expertise (a JS/WASM GUI) and ship it after only a brief check rather than deep review.

Summary source: run-a, higher share of the Claims' quoted words (0.14 vs 0.00).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sR14-f004865-c2

## Question `immediate-vs-retained-gui`

### immediate-vs-retained-gui--doesnt-matter-at-small-scale — The choice does not matter for small-to-medium UIs

Summary: Advocates note immediate mode avoids widget-lifetime bookkeeping and integrates easily into a game engine's GPU loop, while retained mode can perform better by not rebuilding the whole UI every frame — but at the scale of a small task the difference is untestable, so they aren't sure they love immediate mode "on principle" even though it doesn't matter here.

Summary source: run-a, higher share of the Claims' quoted words (0.80 vs 0.30).

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: b-sb21-f008390-c3

### immediate-vs-retained-gui--message-passing-for-realtime — Elm-style message passing fits real-time, stateful apps

Summary: Advocates hold that a real-time, stateful app needs a genuinely event-based library that can synchronize external state changes (e.g. audio playback ticks) with UI redraws while supporting custom canvas drawing, choosing a message-passing framework specifically for that reason.

Summary source: run-b, higher share of the Claims' quoted words (0.29 vs 0.24).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa15-f005857-c1

## Question `impl-trait-syntax-reuse`

### impl-trait-syntax-reuse--p1 — Apit syntax reuse was a mistake

Summary: Advocates state, as a personal view, that argument-position impl Trait sharing the exact same `impl Trait` syntax as return-position impl Trait was a design mistake, at minimum in terms of sharing the syntax.

Summary source: run-a, higher share of the Claims' quoted words (0.55 vs 0.36).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa30-f013276-c2

## Question `in-app-vs-infrastructure-concern`

### in-app-vs-infrastructure-concern--delegate-tls-to-proxy — Terminate TLS in a reverse proxy

Summary: Advocates recommend setting up a reverse proxy for TLS even though their own web framework has built-in TLS support, and require HTTPS for a sensitive component (the web vault).

Summary source: run-a, higher share of the Claims' quoted words (0.45 vs 0.36).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sT09-f005312-c1

### in-app-vs-infrastructure-concern--p1 — A self-written in-process server removes nginx's role rather than replacing it

Summary: Advocates argue that nginx's actual value in front of an HTTP service is providing decoupled operational concerns — flood protection, bandwidth throttling, load balancing, TLS termination — that a new in-process server doesn't reproduce, so dropping nginx removes that role rather than replacing it.

Summary source: run-a, tie on share of the Claims' quoted words (0.29), shorter summary.

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: a-sa14-f005360-c7

### in-app-vs-infrastructure-concern--rate-limit-in-app — Build rate limiting in the app; gateway usage plans fall short

Summary: Advocates detail why an API gateway's usage plans don't substitute for in-app rate limiting: on HTTP API v2 they don't exist at all, even on REST they're invisible to clients (no rate-limit headers, just a bare 429), require pre-provisioned API keys up to a hard per-account cap, and only offer day/week/month windows rather than the fine-grained window the use case needs.

Summary source: run-a, higher share of the Claims' quoted words (0.64 vs 0.45).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb22-f008906-c6

## Question `incremental-invalidation-redesign`

### incremental-invalidation-redesign--p1 — Redesign around atomic levels and data dependencies

Summary: Advocates pitch representing what stage a compilation needs (AST/HIR/MIR/codegen) as an explicit "atomic level," plus tracking fine-grained data dependencies like LTO flags separately, so that `cargo check`, `clippy`, and `build` stop redoing each other's work and unrelated flag changes stop invalidating unrelated tools.

Summary source: run-a, tie on share of the Claims' quoted words (0.20), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa18-f008694-c1

## Question `incremental-port-vs-rewrite-to-rust`

### incremental-port-vs-rewrite-to-rust--p1 — Incremental port only hot paths

Summary: Advocates hold existing JS code bases don't need to be thrown away: port the most performance-sensitive functions to Rust for immediate benefit, and you can stop there.

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB02-f000256-c1

## Question `infrastructure-from-code-vs-iac`

### infrastructure-from-code-vs-iac--p1 — Provision infrastructure from code annotations over Docker or Terraform

Summary: Advocates present an in-code annotation for provisioning a database as "pretty simple" next to running Docker locally or hand-managing Postgres with an IaC tool like Terraform in production.

Summary source: run-a, tie on share of the Claims' quoted words (0.42), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sT09-f011688-c2

## Question `instant-min-max`

### instant-min-max--p1 — Oppose instant extrema fraught

Summary: Advocates say `Instant`'s API contract does not guarantee a fixed reference time — a conforming implementation could start or stop its reference timer dynamically — so a `MIN` value wouldn't reliably denote a stable point, and separately that `Instant` values aren't portable or stable across reboots, making its extrema more hazardous than `SystemTime`'s.

Summary source: run-a, tie on share of the Claims' quoted words (0.56), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa19-f009196-c1, a-sa19-f009196-c2

### instant-min-max--p2 — Instant extrema fraught prefer saturating ops

Summary: Advocates hold SystemTime::MIN/MAX seem reasonable but Instant::MIN/MAX seem fraught for the reasons already raised, proposing saturating arithmetic methods directly on Instant instead of exposing its extrema.

Summary source: run-b, tie on share of the Claims' quoted words (0.88), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa19-f009196-c3

### instant-min-max--p3 — Support instant bound for saturating arithmetic

Summary: Advocates want an `Instant` minimum or maximum specifically to support saturating arithmetic in a real use case (a token-bucket rate limiter), where moving a timestamp below the representable minimum should saturate rather than panic.

Summary source: run-a, higher share of the Claims' quoted words (0.67 vs 0.33).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa19-f009196-c4

## Question `internal-hazmat-api-for-performance`

### internal-hazmat-api-for-performance--p1 — It is worth bypassing BLAKE3's public API and using its internal `Platform::hash_many` SIMD entry point to batch-hash many small blobs, even though the internal function has unchecked preconditions that silently produce wrong results (rather than panicking) on real SIMD platforms

Summary: Advocates, finding the public API has no support for hashing multiple independent blobs at once, repurpose an internal, precondition-checked-only-outside SIMD entry point to get a 17x combined speedup over sequential hashing, explicitly accepting that violating its unchecked preconditions on a real SIMD platform silently produces wrong results rather than panicking.

Summary source: run-a, higher share of the Claims' quoted words (0.57 vs 0.29).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR09-f003702-c1

## Question `internal-service-abstraction-trait`

### internal-service-abstraction-trait--p1 — Service abstraction internally

Summary: Advocates route all communication between a project's stateful internal components through an internal asynchronous request/response abstraction built on a buffered service trait — described as "microservices in one process" — so that internal storage-engine behaviors stay from leaking into the external API and the backing store stays replaceable.

Summary source: run-a, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-bk03-f000267-c4

## Question `intra-doc-links`

### intra-doc-links--p1 — Use rustdoc intra doc links

Summary: Advocates say doc comments should reference types and functions via rustdoc intra-doc links rather than plain text, both because it makes documentation easier to navigate and because the rustdoc lint will then catch a typo'd or renamed reference that plain text would silently leave stale.

Summary source: run-a, higher share of the Claims' quoted words (0.60 vs 0.20).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-bk03-f000267-c16

## Question `io-safety-op-placement-in-main`

### io-safety-op-placement-in-main--p1 — An I/O-safety-critical operation must run at the very start of `main`

Summary: Advocates argue an fd-inheritance setup should be called at the start of `main` specifically to ensure no other fd takes the place of a missing one, framing any later placement as an I/O-safety violation.

Summary source: run-a, tie on share of the Claims' quoted words (0.80), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa14-f005079-c1

### io-safety-op-placement-in-main--p2 — Exact placement doesn't need to be enforced as long as nothing intervenes

Summary: Advocates hold it isn't worth contorting a CLI's structure to guarantee the operation happens literally at the start of `fn main`, since controlling all entrypoints and the current placement during startup/CLI processing is already fine.

Summary source: run-b, tie on share of the Claims' quoted words (0.25), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa14-f005079-c2

## Question `jit-code-alignment`

### jit-code-alignment--p1 — 32 byte default reasonable

Summary: Advocates note the CPU frontend fetches aligned 32B/64B chunks, so a function starting mid-chunk wastes fetch bandwidth, and suspect 32-byte function alignment would be a more reasonable default than the current 16-byte one.

Summary source: run-a, higher share of the Claims' quoted words (0.71 vs 0.57).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sR04-f001401-c1

## Question `js-tooling-in-rust`

### js-tooling-in-rust--p1 — Rust is the standout choice specifically for building JavaScript/TypeScript tooling and infrastructure

Summary: Advocates call Rust "the big star" in JavaScript and TypeScript tooling and infrastructure, framing it as addressing the most significant unsolved issue in the current tooling ecosystem: performance.

Summary source: run-a, higher share of the Claims' quoted words (0.85 vs 0.77).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb26-f012866-c1

### js-tooling-in-rust--p2 — Replace established JavaScript-based tooling (Prettier, ESLint) with a Rust-implemented toolchain for better performance and a more consistent developer experience

Summary: Advocates hold a Rust-implemented toolchain should explicitly aim to replace established JS tools like Prettier and ESLint, framing the payoff as both raw performance and a more consistent developer experience than the tools it replaces.

Summary source: run-b, tie on share of the Claims' quoted words (0.59), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb26-f012866-c2

## Question `kernel-constants-hardcode-vs-comptime`

### kernel-constants-hardcode-vs-comptime--hardcode-for-this-use — Hardcode for this specific use

Summary: Advocates argue that for a particular pivot-replacement site, machine epsilon is the wrong semantic quantity regardless of dtype, so an exact-zero check should stay hardcoded rather than switch to a dtype-derived value.

Summary source: run-a, tie on share of the Claims' quoted words (0.40), shorter summary.

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: b-sR10-f004573-c4

### kernel-constants-hardcode-vs-comptime--parameterize-constants — Pass through a comptime struct or derive from metadata

Summary: Advocates say it's fine to hardcode values for now as long as they're passed to the kernel via a comptime struct, so a future backend-specific change doesn't require touching the kernel body; separately, a generic accessor on the dtype's own precision metadata is called a strict improvement over hardcoded per-dtype constants, self-documenting and handling all float dtypes uniformly.

Summary source: run-a, higher share of the Claims' quoted words (0.54 vs 0.25).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR05-f002048-c2, b-sR10-f004573-c3

## Question `keyed-access-copy-vs-clone-keys`

### keyed-access-copy-vs-clone-keys--p1 — Copy only keys

Summary: Advocates hold key types should be deliberately constrained to `Copy`, to stop users reaching for costlier `Clone` keys when a cheaper option exists.

Summary source: run-b, tie on share of the Claims' quoted words (0.42), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb13-f003963-c3

### keyed-access-copy-vs-clone-keys--p2 — Allow clone keys

Summary: Advocates argue the trait should also accept `Clone` key types, since types like `Arc<str>` are cheap to clone and reasonable as keys even though cloning large objects generally is not.

Summary source: run-a, higher share of the Claims' quoted words (0.40 vs 0.33).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb13-f003963-c4

## Question `lambda-build-tooling`

### lambda-build-tooling--cargo-lambda-by-default — Cargo Lambda by default; Docker only when needed

Summary: Advocates hold Cargo Lambda is the best way to interact with the Rust Lambda runtime for local runs, hot reload and arm64 zip builds, reaching for a container image only "if, for some reason" it's required.

Summary source: run-b, higher share of the Claims' quoted words (0.83 vs 0.33).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sT11-f007659-c2

## Question `lambda-release-profile-size`

### lambda-release-profile-size--p1 — Size-optimized release profile

Summary: Advocates adopted a size-optimized release profile on outside feedback, accepting longer compiles and no unwinding, and measured a binary shrinking from 3.6 MB to 1.8 MB with cold start improving from 20 ms to 17 ms, expecting larger gains on bigger programs.

Summary source: run-a, tie on share of the Claims' quoted words (0.38), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sT11-f007659-c1

## Question `lambda-vs-containers`

### lambda-vs-containers--serverless-first — Default to serverless once measured, or build on edge primitives

Summary: Advocates hold that, once measured, serverless should be the default: routing each data need to the matching edge primitive (queryable durable storage, KV, object storage, atomic durable objects) lets operations vanish and cost scale to zero, and a real migration from an always-on container showed steady latency, a fraction of the memory use, and cold starts as a small minority of invocations — leading to the conclusion that serverless, not containers/Kubernetes, is what should be reached for by default, including for teams that later "graduate" to Kubernetes once they understand their workload.

Summary source: run-b, tie on share of the Claims' quoted words (0.12), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa24-f011220-c1, b-sT07-f004166-c1

### lambda-vs-containers--split-by-workload — Serverless for infrequent or test traffic, containers for always-on

Summary: Advocates hold that an app that is costly to run 24/7 on Lambda but cheap on ECS/Fargate should split by workload: infrequent or test environments run on serverless, always-on production traffic runs on containers — accepting a meaningful infrastructure mismatch between test and production as a tradeoff that's worth the cost savings in some scenarios.

Summary source: run-b, higher share of the Claims' quoted words (0.60 vs 0.48).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa17-f007797-c1, b-sb20-f007797-c1

## Question `land-hal-separate-now-vs-unified-later`

### land-hal-separate-now-vs-unified-later--p1 — Land it as a side crate now; unify later once the shared metapac/combined HAL is ready

Summary: Advocates want previously private work upstreamed as soon as possible so an old, siloed fork can be deprecated and archived, with a path to unifying the new crate into the shared HAL once that becomes possible, now that the code lives in the same repo.

Summary source: run-a, higher share of the Claims' quoted words (0.50 vs 0.44).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sR09-f003955-c1

### land-hal-separate-now-vs-unified-later--p2 — Same — merge as-is now, deprecate in favor of the unified HAL once ready

Summary: Advocates describe the same plan from the other side: get it merged as-is now, switch it onto the shared metapac once that's ready, and deprecate it in favor of the combined HAL once that arrives, without it being "a big deal" for users to switch.

Summary source: run-a, higher share of the Claims' quoted words (0.82 vs 0.64).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sR09-f003955-c2

## Question `language-safety-vs-hw-isolation`

### language-safety-vs-hw-isolation--p1 — Language safety insufficient for untrusted code

Summary: Advocates say Rust protects against a user "holding it wrong" — accidental misuse — but not against intentional, deliberate misuse, which is what real fine-grained security between mutually adversarial code would require; language-level capabilities and effect systems can't solve multi-tenant isolation unless literally every piece of code sharing the address space is trusted, unsafe-forbidden Rust compiled by a trusted compiler, which is viable for a single-application unikernel but not for many mutually distrusting applications together.

Summary source: run-a, higher share of the Claims' quoted words (0.73 vs 0.64).

Tag: fact (agree; votes fact / fact / -)

Claims: a-saL1-f005360-c4, a-saL1-f005360-c6

### language-safety-vs-hw-isolation--p2 — Language safety a major step toward safe libos

Summary: Advocates hold Rust "might not be there yet" for full language-level security, but has already solved the hardest combined problem — safety plus performance — needed to make a high-performance library-OS design viable, with missing pieces like capabilities/effects systems expected to emerge next.

Summary source: run-b, tie on share of the Claims' quoted words (0.64), shorter summary.

Tag: fact (majority; votes fact / tradeoff / fact)

Claims: a-saL1-f005360-c5

## Question `large-pr-split`

### large-pr-split--split-into-small-prs — Split before merging

Summary: Advocates hold that reviewing one huge combined branch is hard and risky; it's better to treat it as a development hub and extract small, isolated PRs for merging.

Summary source: run-b, tie on share of the Claims' quoted words (0.21), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb08-f002518-c3

## Question `leaky-signal-abstraction-electrical-config`

### leaky-signal-abstraction-electrical-config--p1 — The peripheral-signal abstraction is a leaky one that ideally wouldn't exist, but is kept for convenience

Summary: Advocates say peripheral I/O ideally shouldn't need to know about drive strength, pull resistors, or input/output mode, and name the current design a leaky abstraction, pointing to the random null methods `DummyPin`/`Level` must carry as the visible symptom.

Summary source: run-a, higher share of the Claims' quoted words (0.74 vs 0.70).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR06-f002005-c1

## Question `library-auth-opinionated-vs-unopinionated`

### library-auth-opinionated-vs-unopinionated--authenticated-managed-default — The managed service authenticates relays by default

Summary: Advocates hold that an open relay's URL is a credential that ships in every client and leaks, so anyone who learns it can spend its finite bandwidth — which is why managed relays deployed from a given date onward require a signed, expiring, endpoint-bound token issued from the project's API key.

Summary source: run-b, tie on share of the Claims' quoted words (0.43), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sT11-f004960-c1a, a-sT11-f004960-c1b

### library-auth-opinionated-vs-unopinionated--unopinionated-library — The library stays unopinionated; operators choose the scheme for self-hosted relays

Summary: Advocates say the library itself is unopinionated about authentication for self-run relays — operators can build their own authentication scheme — leaving that choice untouched even as the managed service defaults to authenticated tokens.

Summary source: run-a, higher share of the Claims' quoted words (0.50 vs 0.00).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sR11-f004960-c1

## Question `library-error-type-opaque-vs-typed`

### library-error-type-opaque-vs-typed--concrete-typed-errors — Concrete, enumerable error types over `anyhow`

Summary: Advocates hold public APIs should return concrete, enumerable error types rather than `anyhow::Error`, even where this is a large change touching most of the codebase.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.88).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb10-f003188-c2

### library-error-type-opaque-vs-typed--hybrid-snafu — A hybrid with automatic backtraces (snafu)

Summary: Advocates vastly reduced their use of `anyhow` in favor of the `snafu` crate, which gives concrete, enum-based errors like `thiserror` plus automatic backtrace and span-trace capture per variant, working around the `Into`-trait conflict that otherwise forces a choice between ergonomic `?` and backtraces.

Summary source: run-a, higher share of the Claims' quoted words (0.50 vs 0.46).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa14-f005149-c1, b-sb10-f003222-c1

### library-error-type-opaque-vs-typed--typed-over-time — Move toward typed errors as the codebase matures; keep `anyhow` for some things

Summary: Advocates hold that, having started out happily using `anyhow` for many things, structured typed error handling proved far more valuable as the project matured — while still keeping `anyhow` for some things.

Summary source: run-b, higher share of the Claims' quoted words (0.43 vs 0.38).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-saL2-f011092-c6

### library-error-type-opaque-vs-typed--wrap-in-anyhow-for-context — For logged context, wrap typed errors in `anyhow`/`eyre`

Summary: Advocates hold that `thiserror` currently only supports the default `{}` Display format, which loses the full source-error chain, so the workaround for logging is to wrap typed errors in `anyhow` or `eyre`, which support the alternate `{:#}` display that preserves context.

Summary source: run-b, tie on share of the Claims' quoted words (0.94), shorter summary.

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: a-sa18-f008583-c1, b-sb21-f008583-c1

## Question `library-io-factored-out`

### library-io-factored-out--p2 — Bring your own threads

Summary: Advocates say since spawning threads panics on `wasm32-unknown-unknown`, a portable library should factor thread spawning out to the caller — "bring their own threads" — the same way it factors out I/O, which also plays nicer with apps that own a custom thread pool.

Summary source: run-a, higher share of the Claims' quoted words (0.60 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB02-f000256-c14

### library-io-factored-out--p3 — Factor I/O out of a portable library; accept in-memory slices, let the caller perform I/O

Summary: Advocates hold that since the Web has no filesystem and only async I/O, a portable library should factor I/O out of itself entirely, taking input slices from callers rather than reading files or performing I/O directly.

Summary source: run-b, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sB02-f000256-c13, b-bk02-f000256-c5

## Question `library-panic`

### library-panic--never-panic-return-result — Return `Result`; constructors and runtime-checkable conditions return errors

Summary: Advocates push back whenever a `Result`-returning path is reverted to an `assert` or `unwrap`, proposing instead a fallible `try_` variant with a panicking convenience wrapper on top, or making the whole function safe and returning `Result` with explicit runtime validation; one project states outright that any panic reaching the host application is a bug, not an acceptable outcome, and is coded under that guarantee.

Summary source: run-a, higher share of the Claims' quoted words (0.32 vs 0.29).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa09-f004055-c6, a-sa09-f004055-c7, b-sR12-f005421-c1, b-sb05-f001512-c1

### library-panic--no-ad-hoc-panics — No ad hoc panics; only control-flow-contingent ones

Summary: Advocates hold ad hoc panics used as a short-circuit bail-out are bad practice, preferring panics reserved for cases genuinely tied to control flow, while allowing that other Rust practitioners may disagree.

Summary source: run-b, tie on share of the Claims' quoted words (0.18), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa21-f011069-c5

### library-panic--panic-fine-if-documented — Panicking is fine if documented

Summary: Advocates hold a panic path can be acceptable as long as it is listed in the function's `# Panics` documentation, so a user isn't surprised by hitting it.

Summary source: run-b, higher share of the Claims' quoted words (0.27 vs 0.20).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sR10-f004573-c1

### library-panic--prevent-via-explicit-check — Prevent the invalid case with an explicit check

Summary: Advocates hold that rather than letting an invalid input fail deep inside an algorithm, an explicit up-front check should reject it early with a clear error message.

Summary source: run-b, higher share of the Claims' quoted words (0.43 vs 0.29).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR10-f004573-c2

### library-panic--unwrap-only-in-tests — `unwrap` only in tests or provably safe spots

Summary: Advocates hold `unwrap` is acceptable only in tests, or in spots where reading the current function shows a panic can never actually occur.

Summary source: run-b, higher share of the Claims' quoted words (0.71 vs 0.57).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa06-f003414-c3

## Question `lifetimes-on-structs`

### lifetimes-on-structs--borrow-for-measured-performance — Add lifetime parameters where a measured bottleneck justifies them

Summary: Advocates converted an owned, hashmap-based value type to a borrowed one with `Cow`-like borrowed/owned variants, naming this the key change that brought an evaluation within ~10ns of native code, down from 147ns for the original owned implementation.

Summary source: run-a, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: b-sb20-f007364-c1

### lifetimes-on-structs--owned-by-default — Avoid lifetimes on structs as a rule; favor easy-mode owned types, especially for teams new to Rust

Summary: Advocates hold that, while experimenting with borrow-checker fights builds useful intuition, the actionable rule of thumb when stuck is to keep lifetime parameters off struct definitions.

Summary source: run-b, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb20-f007608-c2

## Question `lightweight-clones-in-language`

### lightweight-clones-in-language--p1 — Add lightweight/automatic clone ergonomics to Rust itself

Summary: Advocates propose a Rust project goal adding lightweight clones for reference-counted smart pointers, prototyped as a "generational box," describing it as a controversial but — in their opinion — critical change for the success of high-level Rust, while acknowledging opinions on it are divided.

Summary source: run-a, higher share of the Claims' quoted words (0.77 vs 0.54).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa26-f011305-c3

## Question `lint-allow-broad-vs-narrow`

### lint-allow-broad-vs-narrow--p1 — Broad allow when linter blind to trait indirection

Summary: Advocates keep a blanket `#[allow(unused)]` because the compiler's lint can't see that certain trait operations are actually consumed indirectly through a macro like `#[tracing::instrument]`, so item-level allows would misfire.

Summary source: run-a, tie on share of the Claims' quoted words (0.40), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sR11-f003983-c1

## Question `lld-default-linker`

### lld-default-linker--p1 — Make rust-lld the default linker on x86_64-unknown-linux-gnu for stable releases

Summary: Advocates hold that after internal testing on CI, crater and nightly with no major issues, a measured ~7x incremental-link and 40% end-to-end speedup is worth the small risk that `lld` isn't bug-for-bug compatible with GNU `ld`, switching the default while keeping an escape hatch.

Summary source: run-b, tie on share of the Claims' quoted words (0.17), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sb23-f009657-c1

## Question `llm-doc-edits-reproducibility`

### llm-doc-edits-reproducibility--p1 — Pre review guidelines for llms

Summary: Advocates hold the doc-consistency effort should result in additions to the project's developer guidelines that, among other things, help LLMs pre-review changes.

Summary source: run-b, higher share of the Claims' quoted words (0.58 vs 0.50).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb16-f004997-c1

### llm-doc-edits-reproducibility--p2 — Adopt-controlled-language-standard-ASD-STE100

Summary: Advocates propose mandating a standard like ASD-STE100 Simplified Technical English so the prose style stays consistent and free of "flowery nonsense," arguing a controlled vocabulary and grammar largely remove a model's "taste" from the equation on their own.

Summary source: run-a, higher share of the Claims' quoted words (0.73 vs 0.68).

Tag: taste (majority; votes tradeoff / taste / taste)

Claims: b-sb16-f004997-c2, b-sb16-f004997-c4

### llm-doc-edits-reproducibility--p3 — Declare model prompt and clean env

Summary: Advocates hold that merging an LLM-driven doc pass requires declaring which model was used (since each model has its own "taste"), declaring the exact prompt (wording changes results), and running the update in a clean environment to avoid picking up incidental local agent rules.

Summary source: run-b, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb16-f004997-c3

## Question `lts-release-channel`

### lts-release-channel--support-old-lines — Keep older lines supported (LTS train, backport the fix)

Summary: Advocates hold that a too-fast release cadence should be answered with designated LTS releases carrying guaranteed multi-year API-compatible security patches, letting users upgrade on a slower cadence while still receiving fixes.

Summary source: run-b, higher share of the Claims' quoted words (0.43 vs 0.14).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR06-f002937-c1

### lts-release-channel--upgrade-instead — No backport; upgrade

Summary: Advocates decline to apply a fix to an older version line, pointing instead to the project's upgrade guide.

Summary source: run-a, higher share of the Claims' quoted words (0.60 vs 0.20).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sT05-f002501-c1

## Question `macro-hides-construction-requirements`

### macro-hides-construction-requirements--p1 — Macros may hide complexity

Summary: Advocates note a new reference type makes constructing buffers directly less friendly, but that friction is absorbed by the project's existing macros so end users never see it.

Summary source: run-a, higher share of the Claims' quoted words (0.75 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR10-f004804-c3

## Question `macro-ide-tooling`

### macro-ide-tooling--p1 — Build new tooling rather than accept macro IDE opacity

Summary: Advocates hold that since Rust macros lack autocomplete and partial expansion, new libraries should be built to give macro-based DSLs real IDE support rather than accepting the opacity.

Summary source: run-b, higher share of the Claims' quoted words (0.53 vs 0.47).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa26-f011305-c4

## Question `macro-vs-boilerplate`

### macro-vs-boilerplate--macros-sparingly — Use macros sparingly; prefer functions, derives or macro-free APIs; boilerplate is an acceptable price

Summary: Advocates compare macros to salt — powerful, but meant to be used in small amounts — and, across several concrete cases, default against reaching for a macro: for most real applications the boilerplate is tolerable or custom per-case initialization code forecloses a fully-generated alternative, a repeated sequence should become a plain function rather than a macro if it appears in several places, and a bit of boilerplate is worth keeping the flexibility to customize initialization.

Summary source: run-a, higher share of the Claims' quoted words (0.50 vs 0.33).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sR08-f003082-c1, a-sa17-f007736-c1, a-sa23-f011186-c3, b-sb20-f007736-c1, b-sb20-f007760-c1

## Question `memory-safety-and-resource-leaks`

### memory-safety-and-resource-leaks--safety-does-not-prevent-leaks — It does not prevent resource leaks

Summary: Advocates hold plainly that Rust's memory-safety guarantees do not mitigate memory leaks: a production team leaked tokio tasks and threads and only found the bugs through load simulation and profiling, not through the safety guarantees themselves.

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sR07-f002341-c1, b-sR05-f002341-c1

## Question `memory-safety-design-priority`

### memory-safety-design-priority--p1 — Rust over invested in safety at cost of metaprogramming

Summary: Advocates hold that Rust spent so much of its design budget on memory safety alone that it became a lopsided, "disharmonic" language with little else developed.

Summary source: run-b, tie on share of the Claims' quoted words (0.44), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa28-f012469-c5

### memory-safety-design-priority--p2 — Safety first was the right call metaprogramming will follow

Summary: Advocates reframe the "lopsided" critique as high praise: solving the hard part — memory management without a garbage collector — first gives a young language a great foundation, and they trust the remaining capabilities, mainly easier and more powerful metaprogramming, will come in time.

Summary source: run-a, higher share of the Claims' quoted words (0.64 vs 0.55).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa28-f012469-c6

## Question `memory-safety-vs-correctness-frame`

### memory-safety-vs-correctness-frame--p1 — Correctness is the real target

Summary: Advocates hold that every blog post that over-fits on memory safety is a missed opportunity to talk about correctness, which is a strict superset of memory safety and what actually matters.

Summary source: run-b, higher share of the Claims' quoted words (0.93 vs 0.87).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb19-f005743-c7

## Question `merge-expensive-feature-with-limits`

### merge-expensive-feature-with-limits--p1 — Ship with documented limits

Summary: Advocates hold the feature should ship now: a fixed, small-width enum (Px1/Px2/Px3) makes the performance ceiling explicit to users while still allowing the common case, and the exponential cost can simply be documented in the public API doc comment rather than blocking the feature outright.

Summary source: run-b, tie on share of the Claims' quoted words (0.26), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa05-f003126-c1, a-sa05-f003126-c2

### merge-expensive-feature-with-limits--p2 — Hold for proper solution

Summary: Advocates hold reluctance to merge something this slow and rough, wanting a proper SDF-based solution instead, and — even after batching improvements — remain negative because most users won't read the docs closely enough to avoid the performance cliff and visible artifact bugs.

Summary source: run-b, tie on share of the Claims' quoted words (0.43), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa05-f003126-c3, a-sa05-f003126-c4

## Question `metal-vs-cpu-priority-candle`

### metal-vs-cpu-priority-candle--p1 — Prioritize metal next

Summary: Advocates hold Metal/GPU support is the top engineering priority for the next major push, ahead of further quantized-CPU work.

Summary source: run-b, tie on share of the Claims' quoted words (0.57), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sR01-f000464-c2

## Question `middleware-hook-vs-typestate`

### middleware-hook-vs-typestate--p1 — Typestate explicit preferred over middleware

Summary: Typestate gives a straightforward guarantee: a handler can only obtain `Authorization` by calling through the authorization subsystem, which itself only comes from a `User` obtained via authentication. No worrying about the order handlers run in, no Rails-style before/after/around ordering bugs.

Summary source: run-a, higher share of the Claims' quoted words (0.71 vs 0.29).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-saL1-f005454-c4

## Question `minimal-vs-batteries-std`

### minimal-vs-batteries-std--p1 — Rust targets medium not minimal

Summary: Rust never set out to be minimal; the target was always "medium sized," a middle point between a bare core and a fully batteries-included system.

Summary source: run-a, tie on share of the Claims' quoted words (0.71), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa28-f012469-c3

### minimal-vs-batteries-std--p2 — Stdlib is not batteries included

Summary: "Buy Your Own Damn Batteries" — the stdlib's posture is the deliberate opposite of Python's "batteries included."

Summary source: run-a, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa28-f012469-c4

## Question `ml-dataset-eager-vs-lazy`

### ml-dataset-eager-vs-lazy--p1 — Current eager in-memory materialization is inadequate for large datasets, unresolved

Summary: `new_segmentation_with_items` builds an `InMemoryDataset` under the hood, already flagged as problematic for large images or large datasets, with no known fix yet.

Summary source: run-a, tie on share of the Claims' quoted words (0.44), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa03-f002243-c1

## Question `modulo-vs-branch-wraparound`

### modulo-vs-branch-wraparound--p1 — Branch unrolled(chosen)

Summary: Advocates hold that in the hot loop's common (non-edge) case, modulo-based wraparound costs a `div` instruction; replacing it with if-branches for edge cases and a manually unrolled loop lets the CPU's branch predictor handle it instead, measured at a 7.61x speedup.

Summary source: run-b, higher share of the Claims' quoted words (0.67 vs 0.56).

Tag: fact (majority; votes fact / tradeoff / fact)

Claims: a-sB02-f000256-c5

## Question `multiple-algorithms-autotune`

### multiple-algorithms-autotune--p1 — Ship multiple algorithms (existing "direct" plus a new `im2col`/GEMM path) and autotune, even though the new path trades memory for speed

Summary: Add the infrastructure to autotune `conv2d`/`conv_transpose2d`, plus a second `im2col`-based algorithm alongside the existing "direct" one, trading memory for significant speedups.

Summary source: run-a, higher share of the Claims' quoted words (0.61 vs 0.44).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR05-f002048-c1

## Question `multitenant-resource-allocation`

### multitenant-resource-allocation--p1 — Dynamic system-wide throttling over static per-tenant resource reservation

Summary: Advocates measure utilization across the entire system rather than reserving resources per tenant, and throttle an individual heavy tenant before throttling everyone else, accepting that a compute-intensive tenant may sometimes get lower throughput than dedicated hardware would give it.

Summary source: run-b, higher share of the Claims' quoted words (0.50 vs 0.44).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-saL2-f011092-c4

## Question `multitenant-shared-readonly-pages`

### multitenant-shared-readonly-pages--p1 — Share read-only memory pages across tenants, mitigate side-channels via defense-in-depth

Summary: Advocates share memory pages across tenants only when they are entirely read-only and unmodifiable (e.g. a JS engine's read-only heap), and explicitly do not rely on a single security layer — they avoid exposing high-resolution timers specifically to block timing/Spectre-style side-channel attacks, layering this on top of other sandbox measures.

Summary source: run-b, higher share of the Claims' quoted words (0.73 vs 0.62).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-saL2-f011092-c2

## Question `mutex-vs-atomics`

### mutex-vs-atomics--atomics-carry-own-bugs — Atomics carry their own bug class

Summary: Framing atomics/CAS as the safe alternative glosses over the fact that races — stale or inconsistent reads — are themselves a real bug class, not a lesser evil.

Summary source: run-a, tie on share of the Claims' quoted words (0.25), shorter summary.

Tag: unresolved (three-way split; votes tradeoff / taste / fact)

Claims: b-sb18-f005600-c2

### mutex-vs-atomics--atomics-over-locks — Avoid locks; prefer atomics

Summary: Advocates argue atomics and compare-and-swap are fine — worst case is livelock, which is rare and usually recovers — while a lock is "always a disaster waiting to happen" because something will eventually die holding it and the whole system grinds to a halt; one advocate goes as far as calling the mere existence of a lock, even inside a library, always a programming bug. In practice, advocates reject mutex-guarded shared state (e.g. a shared iterator for ID generation) in favor of lock-free constructs (atomics, `RoaringBitmap::select`) that let threads proceed without synchronization.

Summary source: run-b, higher share of the Claims' quoted words (0.53 vs 0.41).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa17-f007846-c1, b-sb18-f005600-c1

### mutex-vs-atomics--mutex-unless-contended — Plain mutexes unless contention is high

Summary: If there are many threads and heavy lock contention, move to lock-free data structures; if a lock is rarely contended, a normal mutex is simpler and just as good — lock-free brings its own hazards like the ABA problem.

Summary source: run-a, tie on share of the Claims' quoted words (0.58), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb23-f011233-c2

## Question `nalgebra-typed-api-vs-glm`

### nalgebra-typed-api-vs-glm--p1 — Nalgebra for rigor and dynamically-sized cases; nalgebra-glm for simplicity

Summary: Advocates (the library's own maintainers) frame the choice as depending on taste and background: nalgebra for those who prefer rigorous, type-level-restricted treatments of transformations and for dynamically-sized matrices, nalgebra-glm for those coming from C++ GLM or wanting more straightforward functions.

Summary source: run-b, higher share of the Claims' quoted words (0.88 vs 0.62).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sB01-f000217-c1

## Question `named-default-args-overloading`

### named-default-args-overloading--named-parameters-only — Named parameters only

Summary: Named parameters could work for Rust; optional or default arguments still shouldn't, and unresolved design problems remain — parameters are patterns not names, function-values erase parameter names, and reordering call-site arguments conflicts with left-to-right evaluation order.

Summary source: run-a, higher share of the Claims' quoted words (0.62 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa18-f009104-c2

### named-default-args-overloading--overloading-for-interop — Overloading, at least for interop

Summary: Advocates hold that Rust should support built-in overloading today, especially for interop with existing languages, noting C++ API maintainers rely on adding overloads without breaking existing callers, that Rust already fakes overloading inconsistently via trait dispatch (multiple `From` impls, `Into`'s return-type-directed dispatch), and that built-in overloading could also resolve an aliasing problem by letting the compiler pick a safe vs. unsafe overload based on the caller's reference.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.89).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb24-f011312-c6

### named-default-args-overloading--reject-all-for-simplicity — Reject all

Summary: Advocates have for years opposed Rust adding named parameters, optional/default arguments, and function overloading — all requested since at least a twelve-year-old GitHub issue — arguing the features are numerous and mutually entangled, and that Rust's current rule (one function, one signature; write a differently-named function or a builder for variants) keeps the language simple at an acceptable cost.

Summary source: run-b, higher share of the Claims' quoted words (0.17 vs 0.08).

Tag: taste (majority; votes tradeoff / taste / taste)

Claims: a-sa18-f009104-c1

## Question `narrating-comments`

### narrating-comments--p1 — No narrating comments

Summary: Doc comments narrating one-line private helpers repeat the same pattern across a file; removing them all is better than keeping or improving them, so strip the narrating comments.

Summary source: run-a, higher share of the Claims' quoted words (0.61 vs 0.50).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa13-f004772-c5, a-sa13-f004772-c6

## Question `networking-lib-core-scope`

### networking-lib-core-scope--minimal-core-pluggable — Minimal core, pluggable trait extensions

Summary: The networking stack is "what iroh is"; everything else is a custom protocol layered on top. Adding every candidate transport into the core would make the code a maze of feature flags and drag in dependencies most users don't need, so `CustomTransport`/`CustomEndpoint`/`CustomSender` traits let users plug in only what they need.

Summary source: run-a, higher share of the Claims' quoted words (0.62 vs 0.29).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR11-f004170-c1, a-sa02-f002124-c1

## Question `new-features-on-old-editions`

### new-features-on-old-editions--p1 — Extend back until first interaction

Summary: Advocates argue the reason Rust uses editions rather than fine-grained feature flags is to avoid a combinatoric explosion of untested feature/rule interactions — not a default rule that all new features are edition-gated. A feature should therefore be made available on older editions up until the point it actually interacts with something that changed in a later edition; needing to go back and modify an edition migration to work differently would signal the feature was pushed too far back.

Summary source: run-b, higher share of the Claims' quoted words (0.70 vs 0.40).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sa20-f009698-c1

## Question `new-type-vs-option-for-variant`

### new-type-vs-option-for-variant--p1 — Extend via option

Summary: No new recorder type needed for byte-based loading — an argument/option on the existing recorder does the job.

Summary source: run-a, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb09-f002567-c6

## Question `nextest-vs-custom-runner`

### nextest-vs-custom-runner--p1 — Custom test-runner wrapper over cargo-nextest

Summary: Advocates built a custom wrapper around `cargo test` — building test binaries on one machine, shipping them to others as a zip, sharding execution, and converting cargo's unstable JSON test output into JUnit XML — after trying cargo-nextest first and rejecting it, because nextest's different (parallel-process) execution model broke an existing test-suite assumption (a global mutex handing out network ports one at a time), and fixing that assumption would have cost more time than they had.

Summary source: run-b, higher share of the Claims' quoted words (0.19 vs 0.12).

Tag: tradeoff (majority; votes fact / tradeoff / tradeoff)

Claims: a-saL2-f011092-c1

## Question `nightly-feature-autodetection`

### nightly-feature-autodetection--p1 — Nightly features must be explicit opt in

Summary: Unstable features should only impact those who opted in — that's how the entire nightly system is designed. Wanting nightly for one ergonomic reason doesn't mean consenting to dependencies silently using other unstable features, or having them implicitly change behavior; libraries auto-enabling features runs counter to the Rust Project's own principle.

Summary source: run-a, higher share of the Claims' quoted words (0.69 vs 0.42).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sa19-f009343-c3, a-sa19-f009343-c4, a-sa19-f009343-c5, a-sa19-f009343-c6

### nightly-feature-autodetection--p2 — Build probes should default to detecting and using nightly features

Summary: Advocates, as ergonomics-motivated developers, prefer a crate that documents clearly when it auto-detects and uses nightly features over one that requires going through manual opt-in flags, while acknowledging that safety-critical users need a documented way to fully opt out.

Summary source: run-b, higher share of the Claims' quoted words (0.57 vs 0.36).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa19-f009343-c7

## Question `nightly-gate-feature-vs-cfg`

### nightly-gate-feature-vs-cfg--p1 — Rustflags cfg gate

Summary: Gate the tail-call code with `#[cfg(pulley_tail_call)]` set via `RUSTFLAGS` rather than a Cargo feature, because a Cargo feature gets force-enabled by the "test with all features enabled" CI job even on a stable compiler — and this lets the PR land, checked only by a dedicated nightly `cargo check` job, ahead of upstream rustc codegen support.

Summary source: run-a, tie on share of the Claims' quoted words (0.54), shorter summary.

Tag: tradeoff (majority; votes fact / tradeoff / tradeoff)

Claims: b-sb06-f002033-c1

## Question `nightly-in-production`

### nightly-in-production--nightly-when-it-pays — Nightly when its safety and ergonomics pay (portable SIMD)

Summary: Raw target-feature-gated intrinsics are unsafe, verbose, and need manual wrapping and runtime feature detection. `std::simd`'s portable_simd lets you write safe, ordinary iterator code the compiler lowers per architecture — "the choice," even though it currently requires nightly.

Summary source: run-a, higher share of the Claims' quoted words (0.75 vs 0.62).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb23-f011233-c3

### nightly-in-production--stable-only — Stable only

Summary: The team does not, has not, and does not plan to rely on unstable Rust features; every foundational crate is published to crates.io with no unpublished dependencies.

Summary source: run-a, tie on share of the Claims' quoted words (0.60), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-saL2-f011092-c5

## Question `no-std-for-wasm`

### no-std-for-wasm--p1 — No_std is embedded-only, not needed for wasm

Summary: "You do not need to disable libstd when compiling to wasm!" — that step is necessary only for embedded, not for browser/wasm targets.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.40).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sB01-f000217-c4

## Question `non-exhaustive-by-default`

### non-exhaustive-by-default--non-exhaustive-by-default — Yes

Summary: Because custom transports (bluetooth, WebRTC) and new address kinds are a planned direction, types like `TransportAddr`, `PathEvent` and `IncomingLocalAddr` are marked `#[non_exhaustive]` so future variants can be added without breaking the public API — callers must add a wildcard match arm.

Summary source: run-a, tie on share of the Claims' quoted words (0.24), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR13-f004586-c2, a-sR13-f004685-c3, a-sT08-f004169-c2

## Question `nonnull-in-ffi-params`

### nonnull-in-ffi-params--p1 — Avoid runtime null check

Summary: Deliberately did not implement taking `NonNull<T>` as a parameter in the atomic-pointer API, specifically to avoid adding a runtime check.

Summary source: run-a, higher share of the Claims' quoted words (0.73 vs 0.64).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-02-f000977-c1

## Question `object-graph-representation`

### object-graph-representation--indices-or-handles — Indices into an arena, or a separate handle domain, for object graphs

Summary: Rc<RefCell<T>> compiles for "object soup" but leaks memory on reference cycles and panics on self-referential mutable borrows; raw/unsafe pointers hit the same aliasing problems with undefined-behavior risk. Keeping objects in a `Vec` and referring to each other by `usize` index turns aliasing bugs into compiler errors and serializes/parallelizes cleanly with serde/rayon — the same shape an ECS-ish API paired with handles would take for a scripting-language boundary, though that pairing has never actually been built out to prove it works.

Summary source: run-a, higher share of the Claims' quoted words (0.19 vs 0.06).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb20-f007608-c1, b-sb26-f013214-c5

## Question `one-enum-vs-two-types`

### one-enum-vs-two-types--p1 — Split into two structs

Summary: The enum-based accessor is confusing when traversing relations dynamically; better to split it into two separate structs plus friendlier wrapper methods.

Summary source: run-a, higher share of the Claims' quoted words (0.67 vs 0.33).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa07-f003716-c3

## Question `oop-patterns-in-rust`

### oop-patterns-in-rust--p1 — Factories are rarely idiomatic in rust

Summary: Try generic types like `Rc<E>` instead of Abstract Factory — factories are rarely used in Rust.

Summary source: run-a, higher share of the Claims' quoted words (0.56 vs 0.33).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa30-f013276-c6

## Question `opt-level-z-vs-s`

### opt-level-z-vs-s--p2 — Never assume opt-level="z" beats opt-level="s" for binary size — measure both

Summary: Surprisingly, opt-level="s" can sometimes result in smaller binaries than opt-level="z" — always measure, never assume the more aggressive flag wins.

Summary source: run-a, tie on share of the Claims' quoted words (0.80), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sB02-f000256-c7, b-bk02-f000256-c10

## Question `optional-parameters-api-shape`

### optional-parameters-api-shape--drop-feature-keep-signature-small — Drop the feature to keep the signature small

Summary: Advocates are willing to merge a first version of the work without an extra feature (automatic BOM/encoding detection), choosing fewer arguments over including it.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.75).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa06-f003414-c5

### optional-parameters-api-shape--many-constructors-criticized — Many constructors (status quo, criticized)

Summary: There are way too many constructors and not enough documentation.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.75).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb05-f001512-c4

### optional-parameters-api-shape--one-configurable-entry — One entry point: a `Config` struct, `_with_opts`, an enum discriminant, an option on the existing type

Summary: Rust has neither overloading nor default parameters, so route optional configuration through one entry point: a `ColorSpace` enum as a second constructor argument instead of a method per color space, everything through the config struct once a setting belongs to it, or an `_with_opts` method taking an Options struct plus `impl Into<T>` convenience wrappers.

Summary source: run-a, tie on share of the Claims' quoted words (0.39), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-01-f000530-c2, b-sb05-f001512-c3, b-sb10-f003222-c2

### optional-parameters-api-shape--separate-specialized-entries — Separate specialized functions or primitives

Summary: One explicitly-named method per source type and color space keeps the target color space visible at the call site rather than inferred from context; a single merged function would force passing four arguments everywhere, making the code significantly less readable.

Summary source: run-a, higher share of the Claims' quoted words (0.65 vs 0.35).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-01-f000530-c1, a-sa06-f003414-c4

## Question `oss-framework-monetization`

### oss-framework-monetization--fully-open — Fully open, paid layer alongside or donate permissively

Summary: Advocates donate libraries and examples to a project's community working group under an open-source license, framing this as consistent with being long-time open-source advocates; separately, advocates build a paid cloud layer alongside a fully-capable free/local plan, envisioning a business model based on adding complementary value rather than restricting core features behind a paywall.

Summary source: run-b, higher share of the Claims' quoted words (0.72 vs 0.52).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa09-f004016-c1, b-sT05-f002775-c1

## Question `oss-reuse-attribution-norms`

### oss-reuse-attribution-norms--coordination-and-credit-matter — Coordination and credit matter

Summary: Copy-pasting, stripping and renaming another team's code, then shopping it around for maintainers, without reaching out first, is disrespectful of the original authors' investment even where the license allows it — publishing a "debranded" version without discussing it first is "bad form... legal... but bad form nonetheless." A near-verbatim uncredited copy, bugs included, should carry a co-authored-by credit; once pointed out, that credit gets added along with a PR-body acknowledgment of the prior work.

Summary source: run-a, higher share of the Claims' quoted words (0.33 vs 0.19).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa05-f003025-c6, a-sa05-f003025-c8, a-sa13-f004772-c7, a-sa13-f004772-c8

### oss-reuse-attribution-norms--no-entitlement — No entitlement to control reuse

Summary: Producers of open source aren't entitled to anything, the same way consumers aren't either — forking and improving others' code is the real beauty of open source, a gift with no expectations.

Summary source: run-a, higher share of the Claims' quoted words (0.93 vs 0.79).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa05-f003025-c7

## Question `pac-crate-per-chip-vs-shared`

### pac-crate-per-chip-vs-shared--single-crate-with-features — One shared crate

Summary: One shared PAC crate (`stm32-metapac` style) covering related chips, feature-gated, was easier to build than expected and made Cargo features "clean up" — much less annoying to release and manage than a separate crate per chip.

Summary source: run-a, higher share of the Claims' quoted words (0.43 vs 0.37).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa01-f001838-c1, b-sb06-f001838-c1

## Question `paid-maintainers-for-infrastructure`

### paid-maintainers-for-infrastructure--fund-maintainers — Fund dedicated maintainers

Summary: Advocates describe funding as removing the tradeoff between doing maintenance work they love and taking a better-paid job elsewhere, letting them pour full effort into the project without financial anxiety; at the team level, a funding body opens a new full-time maintainer position after a team "struggled with meeting its maintenance demands" once volunteer members left or lost funding, framed as partial relief rather than a full fix.

Summary source: run-b, higher share of the Claims' quoted words (0.24 vs 0.18).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sR15-f009751-c1, a-sR15-f009751-c2, b-sR13-f009755-c1

## Question `parser-combinator-vs-generator`

### parser-combinator-vs-generator--p1 — Nom-style parser combinators are the effective way to build parsers in Rust: small composable functions, no unnecessary allocation, and richer error reporting via VerboseError/context than a naive hand-rolled parser would give you

Summary: nom is efficient and fast, doesn't allocate memory when parsing if it doesn't have to, and makes that easy for the user to replicate; `context`/`convert_error` give human-readable error messages out of a combinator chain.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.50).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sR13-f007973-c1

## Question `persistent-collections-cheap-clone`

### persistent-collections-cheap-clone--p1 — Rust would benefit from persistent, structural-sharing vector types (RRB trees) that make clone cheap (O(log n) path-copying) instead of the O(n) deep copy that ordinary owned collections force today

Summary: Rust collections already behave like values, they just have an expensive clone — what if that clone could be nearly free, via structural sharing?

Summary source: run-a, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR13-f008801-c1

## Question `pin-for-non-relocatable-cpp-types`

### pin-for-non-relocatable-cpp-types--p1 — Yes pin is the emerging convention

Summary: Advocates note there is growing support for using `Pin` to represent C++ values that cannot be relocated via bitwise memcopy (e.g. small-string-optimized `std::string`), even though the same aliasing/projection/auto-ref ergonomics gaps that affect `Pin` elsewhere still apply here.

Summary source: run-b, higher share of the Claims' quoted words (0.67 vs 0.44).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sb24-f011312-c5

## Question `pin-project-vs-pin-project-lite`

### pin-project-vs-pin-project-lite--p1 — Pin-project-lite to avoid proc-macro deps, pin-project otherwise

Summary: pin-project-lite is recommended when a project wants to avoid procedural-macro dependencies, at the cost of being less expressive and giving no custom error messages; pin-project is recommended otherwise.

Summary source: run-a, tie on share of the Claims' quoted words (0.89), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-bk01-f000233-c9

## Question `pin-vs-move-constructors`

### pin-vs-move-constructors--p1 — Pin's phased/place-based design over Move-trait or move-constructor alternatives

Summary: A `Move` marker trait was rejected because pinning is a phased, per-place concept while traits apply to a value's whole lifetime — a Move trait would be widely "infectious" and break backward compatibility. C++-style move constructors were rejected because they'd break Rust's invariant that objects can always be bitwise-moved, silently breaking unsafe code and leaving no way to fix up references held from outside the moved object.

Summary source: run-a, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-bk01-f000233-c10

## Question `platform-gating-feature-vs-target-cfg`

### platform-gating-feature-vs-target-cfg--p1 — Prefer target-based gating over feature flags once the target is stabilized

Summary: Once `wasm32-wasip2` becomes a stable Rust target, the use of feature flags for that platform code can be simplified by using the target directive instead.

Summary source: run-a, higher share of the Claims' quoted words (0.85 vs 0.77).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR05-f002151-c2

## Question `platform-logic-module-vs-inline`

### platform-logic-module-vs-inline--p1 — Keep platform-specific logic inline rather than a separate abstraction

Summary: Prefer keeping all `serve.rs`-related code in `serve.rs`, marking a helper `unsafe` with a `// SAFETY` comment at the call site, over introducing a separate module that adds more `#[cfg]`s to validate.

Summary source: run-a, higher share of the Claims' quoted words (0.45 vs 0.18).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa14-f005079-c5

## Question `plugin-system-mechanism`

### plugin-system-mechanism--p1 — Native dylib rejected

Summary: Native dynamic libraries have no stable ABI, offer no sandboxing (a buggy or malicious plugin can crash or compromise the host), and compiled-code distribution hides backdoors and is harder for users to audit than scripts.

Summary source: run-a, tie on share of the Claims' quoted words (0.40), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa16-f007483-c1

### plugin-system-mechanism--p2 — Scripting language preferred

Summary: Advocates recommend embedding QuickJS as the default approach for a Rust plugin system — over V8/deno_core and over Lua — citing small binary size, no JIT, faster cold starts, and easier integration, evaluating other methods only when QuickJS has too many drawbacks for the specific use case.

Summary source: run-b, higher share of the Claims' quoted words (0.80 vs 0.27).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa16-f007483-c2

### plugin-system-mechanism--p3 — Wasm too immature

Summary: WebAssembly is currently too immature to be used for a plugin system and will make plugin developers' lives hard, despite its sandboxing strength — uneven cross-language support, churning toolchains and targets (WASI p1, p2).

Summary source: run-a, higher share of the Claims' quoted words (0.58 vs 0.42).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa16-f007483-c3

### plugin-system-mechanism--p4 — Expression engine for bounded untrusted eval

Summary: Advocates, for their own project, fork CEL down to a boolean-only subset, reasoning that a non-Turing-complete expression language gives bounded, predictable-runtime evaluation of untrusted user input; they recommend QuickJS instead for most other projects.

Summary source: run-b, higher share of the Claims' quoted words (0.30 vs 0.20).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa16-f007483-c4

## Question `pointer-addr-vs-as-usize`

### pointer-addr-vs-as-usize--p1 — Prefer `.addr()` over `as usize` for pointer-to-integer conversion

Summary: Advocates flag that casting a pointer to `usize` has implicit behavior around provenance and recommend `.addr()` instead, since provenance isn't needed in this case and it has more explicitly defined behavior.

Summary source: run-b, higher share of the Claims' quoted words (0.90 vs 0.70).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa11-f004512-c1

## Question `polonius-scope-cut`

### polonius-scope-cut--p1 — Cut scope for shippability

Summary: The current datalog-based Polonius approximation handles all UI tests except a loop/region case the older, slower approach used to accept correctly; the team is discussing whether to cut scope and accept this narrower formulation in exchange for an easier path to production, while still evaluating what expressiveness limits it would impose.

Summary source: run-a, higher share of the Claims' quoted words (0.50 vs 0.45).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa20-f009698-c3

## Question `portable-async-vs-sync-io`

### portable-async-vs-sync-io--p1 — For I/O that a portable library must perform itself, go async (generic over a Future type), or split by target with a trait plus #[cfg]-gated impls — never synchronous

Summary: If a portable library must perform I/O, it cannot be synchronous — there is only asynchronous I/O on the Web — so architect it as a function generic over `F: Future`, or as a trait implemented once per target behind `#[cfg(target_arch = "wasm32")]`.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.33).

Tag: fact (agree; votes fact / fact / -)

Claims: b-bk02-f000256-c6

## Question `portable-kernels-performance-cost`

### portable-kernels-performance-cost--p1 — Comptime specialization avoids the tradeoff

Summary: The industry consensus is that abstracting GPU and CPU programming without sacrificing performance is impossible; through intentional design — `comptime` specialization per plane size and line size, including plane size 1 for the CPU runtime rather than simulating GPU execution — this was proven otherwise.

Summary source: run-a, higher share of the Claims' quoted words (0.69 vs 0.19).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa09-f004016-c2

## Question `porting-to-rust-safety`

### porting-to-rust-safety--naive-port-not-safe — No; restructure or risk new UB

Summary: Advocates hold that pure Rust cannot create mutably-aliasing references, so if a ported function relies on C++'s permissive aliasing, naively translating it and letting the optimizer assume exclusivity can silently introduce new undefined behavior absent from the original C++; separately, an advocate found that eliminating memory leaks and UB was harder than expected because the existing C-style code's organization did not allow refactoring into a safe version — implying a straight port preserving the original architecture does not by itself deliver Rust's safety benefits.

Summary source: run-b, higher share of the Claims' quoted words (0.42 vs 0.29).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa21-f011069-c4, b-sb24-f011312-c4

## Question `postfix-await`

### postfix-await--p1 — Postfix `.await`

Summary: Advocates hold postfix `.await` is more ergonomic than a prefix operator in chains of method calls and field accesses, contrasting `fetch().await?.status_code` against the prefix-syntax equivalent `(await fetch())?.status_code` as more natural to read in longer chains.

Summary source: run-b, higher share of the Claims' quoted words (0.43 vs 0.29).

Tag: taste (agree; votes taste / taste / -)

Claims: b-bk01-f000233-c1

## Question `pre-1-0-api-default-stability`

### pre-1-0-api-default-stability--p1 — Stable unless flagged

Summary: Without a known blocking issue, there's no problem exposing the interrupt API as stable for now.

Summary source: run-a, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb08-f002517-c1

### pre-1-0-api-default-stability--p2 — Unstable until agreed ready

Summary: Prior PRs targeting interrupts assumed they wouldn't be stabilized, and some interrupt enum variants don't make sense for the CPU-driven driver — after pushback, agreement that the API isn't ready and should stay unstable.

Summary source: run-a, higher share of the Claims' quoted words (0.40 vs 0.27).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb08-f002517-c2, b-sb08-f002517-c3

## Question `pre-1-0-canary-releases`

### pre-1-0-canary-releases--p1 — Frequent canary releases for fast feedback

Summary: Waiting until everything was fully finished before releasing was not actually the best way to get a stable release into users' hands; three-week cycles and fast canary releases before 1.0 get feedback quickly and let the team move with confidence.

Summary source: run-a, higher share of the Claims' quoted words (0.80 vs 0.73).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb10-f003188-c1

## Question `predicate-rules-vs-first-match`

### predicate-rules-vs-first-match--p1 — Ordered first match wins

Summary: After a predicate-function design produced a real bug (two mutually exclusive conditions both false), redesign the conditional rules as a match-style, ordered "first condition wins" list.

Summary source: run-a, higher share of the Claims' quoted words (0.71 vs 0.57).

Tag: tradeoff (majority; votes fact / tradeoff / tradeoff)

Claims: b-sb09-f003030-c8

## Question `proc-macro-derives-vs-reflection-shape`

### proc-macro-derives-vs-reflection-shape--proc-macros-costly — Proc macros are costly and unsolved

Summary: A pure AST transform gets shaped as Rust source that the compiler must compile, optimize, run, and grant full disk/network access to "just in case" — every new behavior (Debug, Display, Deserialize, ...) tends to spawn its own trait and derive macro that must independently win ecosystem-wide adoption, and many attempts to fix this haven't stuck.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.92).

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: a-sa25-f011413-c1

### proc-macro-derives-vs-reflection-shape--reflection-doesnt-clearly-win — Reflection's runtime cost is real and a JIT is no general answer

Summary: Reflection was expected to trade only build time for runtime speed; measured build times came out "a wash" and runtime performance unconditionally worse "by design... a fact of life, you can do nothing to change that" — a negative result. A Cranelift JIT built on the reflected data can beat Serde in a microbenchmark, but shipping a JIT isn't viable broadly: rejected outright on Apple platforms, disliked for unexplained binary size and warm-up cost.

Summary source: run-a, higher share of the Claims' quoted words (0.60 vs 0.48).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa25-f011413-c4, a-sa25-f011413-c5, b-sb24-f011413-c3

### proc-macro-derives-vs-reflection-shape--ship-shape-data — Ship shape data; reflection avoids annotation gaps

Summary: Instead of turning types into more code, ship data about types: a single associated `SHAPE` constant per type (name, offset, alignment, type id, variants, attributes, doc comments) that many downstream behaviors can consume from one derive, and that a reflection-based serializer can use to pick the right encoding for a concrete element type at runtime — something Serde needs an explicit annotation for, since Rust has no stable or nightly-safe specialization to detect it automatically.

Summary source: run-a, higher share of the Claims' quoted words (0.43 vs 0.35).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb24-f011413-c1, b-sb24-f011413-c2

## Question `proc-macro-emitted-paths-hidden-deps`

### proc-macro-emitted-paths-hidden-deps--p1 — Fix via feature-gating, not via requiring every downstream crate to declare the dependency

Summary: Trace the root cause to `leptos_macro`'s `view!` macro unconditionally emitting `tracing::instrument` under `debug_assertions`/`ssr`; fix it by having the `ssr` feature also enable `tracing`, or by reworking the macro's `cfg_attr` gating, rather than requiring every downstream crate to add `tracing` itself.

Summary source: run-a, higher share of the Claims' quoted words (0.29 vs 0.14).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-01-f000701-c1

## Question `profile-before-optimizing`

### profile-before-optimizing--p2 — Let profiling data override the developer's hypothesis about where time is spent, every time

Summary: Time may be spent in places you don't expect: the fillStyle canvas setter, not tick(), ate 40% of frame time; vector allocation, the stated hypothesis for the bottleneck, turned out to have negligible cost — always let profiling guide your focus and override your hypothesis.

Summary source: run-a, higher share of the Claims' quoted words (0.53 vs 0.29).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sB02-f000256-c6, b-bk02-f000256-c7

## Question `project-decision-speed-vs-inclusion`

### project-decision-speed-vs-inclusion--alt1 — Pick progress and faster consensus over inclusive process

Summary: We must learn to recognize when having a consensus is more important than having the right consensus, and in these cases, pick progress over stagnation.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.91).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb19-f005743-c9

## Question `project-discussions-area`

### project-discussions-area--p1 — Removing the discussion area lost knowledge

Summary: Advocates report that design talk is now forced into an ill-fitting issue thread, with no alternative location, after the discussion area's removal, and that explanations that used to live in discussions (including a detailed one on bus arbitration) have all been deleted.

Summary source: run-b, higher share of the Claims' quoted words (0.75 vs 0.62).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sT05-f002499-c10, b-sT05-f002499-c9

## Question `project-priorities-communication`

### project-priorities-communication--p1 — Project direction should be communicated through a lightweight, non-authoritative "Goals" system (staffed/unstaffed as a focus signal) rather than a fixed roadmap or the prior ad hoc culture

Summary: This is notably not a "roadmap" and also not authoritative — an initial staffed/unstaffed framing that read as active/inactive felt dictatorial, so it was loosened: any approved Goal can get a Working Group even unstaffed, while staffing still signals leadership focus.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.67).

Tag: taste (majority; votes tradeoff / taste / taste)

Claims: b-sR11-f004993-c2

## Question `properties-syntax`

### properties-syntax--p1 — Reject properties

Summary: Advocates hold that field access should stay visibly cheap and free of unseen consequences, and that hiding a method call — which could do anything, including crash or block on a network request — behind ordinary field-access syntax is undesirable, especially in a systems language.

Summary source: run-b, higher share of the Claims' quoted words (0.72 vs 0.61).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb19-f007207-c2

## Question `ptx-build-host-vs-multi-arch`

### ptx-build-host-vs-multi-arch--p1 — Compile for build host only

Summary: The PTX is compiled for your machine via `build.rs` at compile time — it is not one binary distributed to everyone.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.88).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sb08-f002518-c1

### ptx-build-host-vs-multi-arch--p2 — Needs portable multi arch support

Summary: Compiling only for the build host's active compute capability may break portability across heterogeneous multi-GPU systems.

Summary source: run-a, higher share of the Claims' quoted words (0.67 vs 0.53).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb08-f002518-c2

## Question `public-naming-brevity-vs-clarity`

### public-naming-brevity-vs-clarity--alt1 — Favor brevity or memorability

Summary: Fun names are great, but sometimes they get in the way — the team loved `MagicEndpoint` as a name, but it just became too long, so it was renamed to plain `Endpoint`.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.38).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sR04-f001515-c1

### public-naming-brevity-vs-clarity--clarity-over-brevity — Name for clarity and the literal mechanism

Summary: It makes sense to spell out "snippets" explicitly in a name rather than abbreviate it to "scls," to make it a bit easier on users to infer what the name means.

Summary source: run-a, higher share of the Claims' quoted words (0.89 vs 0.33).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sR04-f001617-c1

## Question `pump-events-timeout-poll`

### pump-events-timeout-poll--p1 — Any `Some(duration)` timeout passed to `pump_events` should force `ControlFlow::Poll`

Summary: Any duration, as long as it's `Some`, should make the control flow `Poll`.

Summary source: run-a, higher share of the Claims' quoted words (0.75 vs 0.50).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sR08-f002685-c1

### pump-events-timeout-poll--p2 — Special-case only `Duration::ZERO` to force `ControlFlow::Poll`; leave other durations to winit's own handling

Summary: Advocates narrow their workaround to the zero-duration case only, reasoning it doesn't make sense to return `Wait` when a nonzero duration was explicitly requested, and leave handling that case correctly to winit itself.

Summary source: run-b, higher share of the Claims' quoted words (0.71 vs 0.57).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sR08-f002685-c2

## Question `pure-rust-crypto-stopgap`

### pure-rust-crypto-stopgap--p1 — Pure-Rust crypto backend as an acceptable stopgap, not the end state

Summary: Advocates, finding both `ring` and `aws-lc-rs` fail on an unusual target because they wrap C code with platform-specific assembly, fork a pure-Rust backend down to only the primitives they need, explicitly stating a hardware-accelerated backend "would be the right thing to do for a production system" while treating the pure-Rust version as good enough for now.

Summary source: run-b, higher share of the Claims' quoted words (0.78 vs 0.67).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa11-f004471-c1

## Question `quantization-speedup-candle`

### quantization-speedup-candle--p1 — Quantization helps memory bound only

Summary: T5's cross-attention involves much larger matmuls than llama/mistral, making it compute- rather than memory-bound on M1/M2; quantization's usual speedup comes from being memory-bound, so it's hard to beat Apple Accelerate here even after tuning parameters.

Summary source: run-a, higher share of the Claims' quoted words (0.46 vs 0.31).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sR01-f000464-c1

## Question `query-engine-batching-parallelism`

### query-engine-batching-parallelism--p1 — Partition-based batch execution (vectorized batches within a partition, parallelized across partitions) captures the benefits of both fully-sequential and fully-parallel row processing

Summary: Contrasted a fully-sequential "tight loop" (cache-friendly, low interpretation overhead) against fully-parallel per-row processing (better core utilization); DataFusion's partition-based architecture achieves a balance, reaping benefits from both ends.

Summary source: run-a, higher share of the Claims' quoted words (0.70 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR08-f003580-c1

## Question `quic-framing-one-stream-vs-per-message`

### quic-framing-one-stream-vs-per-message--p1 — Length prefixed framing on one stream

Summary: Writing one chunk with `write_all`, reading it all, then closing the stream is fine while getting familiar, but real protocols want something more sophisticated: multiple logical messages per stream, each prefixed by its length, so the protocol is designed as messages rather than bytes and variable-length messages are handled.

Summary source: run-a, higher share of the Claims' quoted words (0.86 vs 0.29).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sT08-f003375-c1

## Question `rate-limiter-algorithm`

### rate-limiter-algorithm--p1 — Use a fixed-window counter for the rate limiter, accepting its known boundary-burst weakness, rather than a token bucket or sliding window

Summary: Advocates acknowledge a motivated client can double its effective rate by firing requests at the edges of two adjacent fixed windows — the textbook reason production-grade rate limiters move on from fixed windows — but keep the fixed window anyway because it keeps the storage schema minimal and easy to follow, an atomic `ADD` versus the extra round trip token bucket or sliding window would cost, leaving the algorithm swap as a follow-up.

Summary source: run-b, higher share of the Claims' quoted words (0.67 vs 0.53).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb22-f008906-c5

## Question `reactive-keyed-child-notification`

### reactive-keyed-child-notification--p1 — Default notify all children favor no false negatives

Summary: "False negatives" (broken reactivity) are worse than "false positives" (technically-unnecessary notifications) — track the parent path by default and notify all keyed children on a parent write, leaving precise-but-manual patch/update as an opt-in path.

Summary source: run-a, higher share of the Claims' quoted words (0.38 vs 0.16).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb13-f003963-c1, b-sb13-f003963-c2

## Question `readability-vs-manual-optimization`

### readability-vs-manual-optimization--p1 — Readability over manual optimization when backend cleans up

Summary: It probably doesn't matter much either way in this case, since there isn't anything preventing LLVM from cleaning the eager computation up itself — but the change to the more efficient form is worth making anyway, for reader clarity.

Summary source: run-a, higher share of the Claims' quoted words (0.79 vs 0.43).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb05-f001582-c2

## Question `reduction-accumulation-precision`

### reduction-accumulation-precision--p1 — Accumulate in float for precision

Summary: Should probably accumulate with float in softmax to preserve precision — shouldn't affect performance at all.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.50).

Tag: fact (majority; votes fact / tradeoff / fact)

Claims: a-sR04-f001096-c1

## Question `reflection-security-risk`

### reflection-security-risk--p1 — Universally implemented reflection is suspicious

Summary: The auto-implemented `Reflect` trait reads as inherently ominous — "like tapping the Marauder's Map with your wand and saying 'I solemnly swear I am up to no good.'"

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.14).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa28-f012469-c7

### reflection-security-risk--p2 — Rust lacks reflection and that closes off a footgun class

Summary: Rust doesn't have dynamic class loading and reflection, but someone could still build a serde-serializable type to do custom remote command/process execution — the difference from a Java/Struts-style deserialization RCE is that it would be deliberate and not some oversight, though still possible given enough will.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.52).

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: a-sa28-f012469-c8

## Question `reflection-type-model-and-mutation`

### reflection-type-model-and-mutation--open-design-space — Unresolved

Summary: The in-progress compiler/std reflection MVP is still an open, contested design space: whether to describe types from the compiler's internal model or from what's useful to a user (e.g. serialization), and whether mutation through reflection is sound at all, since it can violate invariants expressed nowhere but the code. There are more open questions than answers right now, and the MVP is reportedly being rewritten from scratch.

Summary source: run-a, higher share of the Claims' quoted words (0.53 vs 0.47).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa25-f011413-c7, b-sb24-f011413-c4

## Question `reject-connections-before-handshake`

### reject-connections-before-handshake--p1 — Reject early

Summary: Rejecting an invalid or unauthenticated incoming connection early, by address/endpoint ID/ALPN before the handshake finishes, is much cheaper than accepting and then closing it — benchmarks on the PR show roughly 30x throughput for address-based rejection.

Summary source: run-a, higher share of the Claims' quoted words (0.87 vs 0.67).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sR13-f004586-c3

## Question `release-lto`

### release-lto--p1 — Enable LTO in release builds despite longer compile times, for both smaller and faster wasm

Summary: LTO makes the .wasm both smaller and faster at runtime via more inlining and pruning; the downside is longer compilation — worth it anyway.

Summary source: run-a, higher share of the Claims' quoted words (0.88 vs 0.62).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-bk02-f000256-c13

## Question `release-on-request`

### release-on-request--p1 — Release on request

Summary: Making a release is relatively low cost, so favor cutting one as soon as a fix is requested — even a request buried in a closed PR counts, tracked with an issue so it isn't lost.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.71).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sT07-f002883-c1

## Question `release-sequencing-after-dependency-major`

### release-sequencing-after-dependency-major--p1 — Ship DataFusion 52 against the planned arrow minor (57.2.0)

Summary: The next arrow release is a minor version (57.2.0); being minor, it should be usable with DataFusion 52, so there's no need to sequence the release after arrow's major.

Summary source: run-a, tie on share of the Claims' quoted words (0.43), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: b-sT07-f003809-c2

## Question `replace-battle-tested-c-with-rust`

### replace-battle-tested-c-with-rust--age-means-battle-tested — Old C is more optimized and reliable for its age

Summary: Advocates cite a Google security study on Android to argue that older code tends to have fewer bugs.

Summary source: run-b, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-saL1-f005516-c6

### replace-battle-tested-c-with-rust--bootstrap-undermines-case — The bootstrap trust gap undermines the safety argument

Summary: All the language-level memory safety in the world can't help if the compiler's own bootstrap chain could be compromised — by the same "moral imperative" logic, avoiding Rust until bootstrapping is fixed (e.g. keeping mrustc close to mainline) would be the imperative instead.

Summary source: run-a, higher share of the Claims' quoted words (0.78 vs 0.56).

Tag: fact (majority; votes fact / taste / fact)

Claims: b-sb19-f005743-c8

### replace-battle-tested-c-with-rust--broad-quality-improvement — A broad quality improvement; pushback is mostly habit

Summary: After decades writing C/C++, Rust makes for a better programmer for anything low-level or high-performance — it keeps you from an entire class of mistakes that were too easy to make in any language without garbage collection; pushback against it reads as belly-aching from people too attached to what they've used for decades.

Summary source: run-a, higher share of the Claims' quoted words (0.94 vs 0.59).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb26-f012849-c1

### replace-battle-tested-c-with-rust--narrow-niche — Rust's legitimate niche is narrow

Summary: Rust finally finds its niche: replacing C specifically in very-low-level and constrained-environment programming — its contribution to OS kernel development, by contrast, is judged almost nothing, with only some progress.

Summary source: run-a, higher share of the Claims' quoted words (0.70 vs 0.30).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb26-f012849-c3

### replace-battle-tested-c-with-rust--only-maintenance-improves-code — Age alone does not improve code; maintenance does

Summary: The takeaway from the cited Google study should be that code gets less buggy from active use and maintenance, not from the simple passage of time; the "old codebases are more optimized/battle-tested" meme is false in general — it depends on whether someone actually spent time optimizing or fuzzing, and unfuzzed "battle-tested" code can still hide bugs the first real fuzzer finds.

Summary source: run-a, higher share of the Claims' quoted words (0.76 vs 0.56).

Tag: fact (agree; votes fact / fact / -)

Claims: a-saL1-f005516-c7, a-saL1-f005516-c8

### replace-battle-tested-c-with-rust--p1 — Rust by default with pragmatic c exceptions

Summary: Implement as much of the project in Rust as reasonably possible, but keep pragmatic exceptions — it doesn't make sense to rewrite something like libsecp256k1 in Rust when the same upstream library other projects already trust is available.

Summary source: run-a, higher share of the Claims' quoted words (0.73 vs 0.36).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-bk03-f000267-c1

### replace-battle-tested-c-with-rust--reject-moral-framing — Not a moral imperative; an economic choice

Summary: Escalating "moral imperative" logic could just as well demand replacing Rust itself with something formally stronger, which shows the framing proves too much; correctness and safety are really an economic choice — no one funds fixes to xz-utils even as people make millions off it; there are genuine moral imperatives in the industry, and language choice isn't one of them.

Summary source: run-a, higher share of the Claims' quoted words (0.61 vs 0.52).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb19-f005743-c1, b-sb19-f005743-c2, b-sb19-f005743-c3

### replace-battle-tested-c-with-rust--replace-with-rust — Replace it; memory safety outweighs the testing record

Summary: OpenSSL and its derivatives carry a long history of memory-safety vulnerabilities, and Rustls now shows roughly 2x lower handshake latency in benchmarks — time for the Internet to move off C-based TLS. Likewise, librsvg is dropping gdk-pixbuf's C image decoders for the Rust `image-rs` crate, explicitly acknowledging the incumbent C libraries are heavily tested and continuously fuzzed, framing the move as an opportunity to find and fix exactly the gaps that remain rather than a claim of already-equal maturity.

Summary source: run-a, higher share of the Claims' quoted words (0.15 vs 0.09).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa15-f006797-c1, b-sb19-f005964-c1

### replace-battle-tested-c-with-rust--safety-not-enough — Memory safety is far from enough; model checking needed

Summary: There's far more to writing safe software than memory safety — Rust isn't nearly enough on its own; any conversation about safer software should include model checking (CBMC for C, Kani for Rust, SPARK for Ada), regardless of which language is chosen.

Summary source: run-a, higher share of the Claims' quoted words (0.92 vs 0.69).

Tag: unresolved (three-way split; votes fact / taste / tradeoff)

Claims: b-sb26-f012849-c2

## Question `repr-c-for-persistent-memory`

### repr-c-for-persistent-memory--p1 — Repr c required

Summary: `#[repr(C)]` is needed to keep an object's in-memory layout stable across binary versions, since default Rust layout carries no such guarantee.

Summary source: run-a, tie on share of the Claims' quoted words (0.41), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: b-sb19-f005836-c2

## Question `repr-packed-vs-byte-array`

### repr-packed-vs-byte-array--p1 — Avoid repr packed use byte array getters

Summary: `#[repr(packed)]` is tempting to shrink a struct but "controversial for good reasons"; a safer, less readable alternative — storing fields as a raw byte array with getter methods — compiles to the same layout without exposing misaligned references.

Summary source: run-a, higher share of the Claims' quoted words (0.50 vs 0.42).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb17-f005113-c1

## Question `reproduce-wasm-bugs-natively`

### reproduce-wasm-bugs-natively--p2 — Reproduce non-JS bugs as native #[test]/#[bench] under OS-native tools rather than debugging on the wasm/Web target directly

Summary: WebAssembly's debugging story is still immature — no DWARF-equivalent, stepping through raw wasm instructions — so bugs not tied to JS/Web-API interaction should be isolated and reproduced as smaller native `#[test]`/`#[bench]` cases under mature OS-native tooling, though it's worth first confirming via a browser profiler that the bottleneck is actually in the wasm before investing in native profiling.

Summary source: run-a, higher share of the Claims' quoted words (0.53 vs 0.29).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB02-f000256-c15, b-bk02-f000256-c8

## Question `required-signals-vs-option-pins`

### required-signals-vs-option-pins--p1 — Driver constructors should require an explicit signal value for every input/output rather than accepting `Option<PIN>`

Summary: Once the PR lands, no driver should accept `Option<PIN>` — users should explicitly set each signal to something, even a placeholder like `Level::Low`, mainly to prevent a previous driver's settings from lingering.

Summary source: run-a, higher share of the Claims' quoted words (0.82 vs 0.64).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sR06-f002005-c2

## Question `restrict-external-construction`

### restrict-external-construction--p1 — Restrict external construction of the validated type

Summary: Leans toward not letting external callers construct the type at all, since agreement follows that it "doesn't make much sense" — every value is created internally anyway.

Summary source: run-a, higher share of the Claims' quoted words (0.38 vs 0.23).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa11-f004265-c4, a-sa11-f004265-c5

## Question `retain-joinhandles`

### retain-joinhandles--p1 — Always retain and poll joinhandles

Summary: Advocates warn that Tokio makes it easy — and even implicitly encourages, via its own examples — dropping a `JoinHandle` and letting a task run detached, silently swallowing any panic inside it; they recommend always polling handles (via `buffered_unordered`, `JoinSet`, or a custom aborting wrapper) so panics surface.

Summary source: run-b, higher share of the Claims' quoted words (0.19 vs 0.12).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sb17-f005159-c5

## Question `reuse-vs-purpose-built-unwind`

### reuse-vs-purpose-built-unwind--p1 — Prefer reuse existing unwind logic

Summary: Advocates do not want a second, parallel implementation of debuginfo-less unwinding built alongside one that is already implemented and battle-tested in the codebase, though they are fine with two separate collection methods coexisting.

Summary source: run-b, higher share of the Claims' quoted words (0.67 vs 0.58).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb13-f004160-c1

### reuse-vs-purpose-built-unwind--p2 — Prefer purpose built implementation for performance

Summary: Chose a simpler frame-pointer-only unwinder over the existing DWARF-based machinery, since the general implementation does more than needed and is roughly 100x slower for this purpose.

Summary source: run-a, higher share of the Claims' quoted words (0.60 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb13-f004160-c2

## Question `roadmap-performance-vs-features`

### roadmap-performance-vs-features--p1 — Perf first for a quarter

Summary: The project is already in good shape on extensibility and customizability, so it would be great to have one or two quarters where the focus is specifically performance.

Summary source: run-a, higher share of the Claims' quoted words (0.75 vs 0.25).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: b-sR04-f001724-c1

### roadmap-performance-vs-features--p2 — Feature work also serves perf

Summary: A logical-types proposal isn't purely a feature detour from the perf-quarter push — it would itself improve performance, particularly late materialization for REE arrays and string views — while still agreeing to rescope it to be easier to manage.

Summary source: run-a, higher share of the Claims' quoted words (0.57 vs 0.36).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR04-f001724-c2

## Question `rpc-error-detail-vs-flat-outcome`

### rpc-error-detail-vs-flat-outcome--p1 — Flat outcome enum over `Result<T, E>` for RPC responses

Summary: Advocates make an RPC response a plain enum rather than a `Result` carrying a detailed error, because serializing detailed errors is often a real pain and failure specifics like stack traces are "nobody's business" — the enum tells the caller only enough to decide whether retrying makes sense.

Summary source: run-b, higher share of the Claims' quoted words (0.67 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa06-f003590-c1

## Question `rtic-is-an-rtos`

### rtic-is-an-rtos--p1 — RTIC is a (hardware-accelerated) RTOS

Summary: From RTIC's developers' own point of view, RTIC is a hardware-accelerated RTOS that uses hardware such as the NVIC on Cortex-M or CLIC on RISC-V to perform scheduling, rather than a classical software kernel.

Summary source: run-a, tie on share of the Claims' quoted words (0.89), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sB01-f000227-c1, a-sR01-f000227-c1

## Question `rust-core-guidelines-document`

### rust-core-guidelines-document--p1 — Enforce via compiler and Clippy lints rather than write a guidelines document

Summary: Rust's preferred solution is to avoid needing a prescriptive guidelines document at all — the language is designed to be statically analyzable so the compiler enforces as much as possible, and whenever a gotcha is discovered, someone writes a Clippy lint for it instead of documenting a best practice, with popular crates serving as de-facto standards.

Summary source: run-a, higher share of the Claims' quoted words (0.84 vs 0.58).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sa26-f011993-c1

## Question `rust-cuda-vs-cpp-kernels`

### rust-cuda-vs-cpp-kernels--p1 — Rust-cuda is the right direction despite CUDA's vendor lock-in and the ecosystem's current gaps

Summary: Rust-CUDA — kernels and host code both in Rust, wrapping LLVM/NVVM/PTX — is presented as the exciting alternative to writing kernels in C++/CUDA, even while conceding, once pressed, that no non-NVIDIA equivalent is known and that almost all real GPU work today still goes through C++ kernels with a thin Rust host layer.

Summary source: run-a, tie on share of the Claims' quoted words (0.29), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb23-f011233-c1

## Question `rust-efficiency-for-cloud-workloads`

### rust-efficiency-for-cloud-workloads--p1 — Large quantified advantage

Summary: Rust uses at least 50% less energy than languages like Python, cutting CPU time up to 75% and memory up to 95% versus Python/Ruby/JS.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.71).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sB01-f000149-c3

## Question `rust-for-ai-generated-code`

### rust-for-ai-generated-code--p1 — Rust is the best language for an AI-coding future

Summary: As AI increasingly writes code and humans architect systems, Rust's compiler acts as an independent, automatic check on AI-generated code — vetting for things like memory leaks — in a way other languages' compilers don't provide.

Summary source: run-a, tie on share of the Claims' quoted words (0.38), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa26-f011443-c2

## Question `rust-for-backend-services-vs-jvm`

### rust-for-backend-services-vs-jvm--rust-over-jvm — Rust over the JVM or C/C++ for backend services

Summary: A Rust application framework emphasizes convention over configuration, inspired by Spring Boot, with an extensible plugin system, a concise API, and a `#[component]` macro that removes the need to implement the Plugin trait by hand.

Summary source: run-a, higher share of the Claims' quoted words (0.67 vs 0.44).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sT09-f005314-c1

## Question `rust-for-high-level-apps`

### rust-for-high-level-apps--less-productive-for-prototyping — Today Rust is less productive than high-level frameworks for prototyping

Summary: Long compile times and language rigidity made their own users simply more productive with existing high-level tools like React and FastAPI than with early high-level Rust.

Summary source: run-a, higher share of the Claims' quoted words (0.69 vs 0.62).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa26-f011305-c2

### rust-for-high-level-apps--push-rust-into-high-level-apps — Push Rust into high-level application development

Summary: Rust's mission shouldn't be exclusive to so-called core/systems software — high-level application development deserves the same investment.

Summary source: run-a, higher share of the Claims' quoted words (0.80 vs 0.60).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa26-f011305-c1

## Question `rust-for-lambda-vs-interpreted`

### rust-for-lambda-vs-interpreted--p1 — Worth it for lambda

Summary: Advocates argue Rust's compiled binaries lower both the memory and execution-time dimensions of Lambda's billing formula compared to JavaScript and Python, and that its explicit Option/Result handling catches edge cases earlier; they report cold starts of 10-60ms, roughly 10-20x faster than the interpreted alternatives.

Summary source: run-b, higher share of the Claims' quoted words (0.80 vs 0.70).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sb19-f007042-c1

## Question `rust-for-mlops-vs-python`

### rust-for-mlops-vs-python--p1 — Rust-first default

Summary: Rust if you can, Python if you must — Rust is the first-choice language for cloud/data/MLOps projects, with Python as the fallback only when necessary.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.67).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sB01-f000149-c1

## Question `rust-for-web-frontend`

### rust-for-web-frontend--isomorphic-rust-web — A unified isomorphic Rust client/server model over server MVC plus a JS frontend

Summary: Unlike a framework that replicates batteries-included scaffolding with a separate React frontend, Leptos lets a developer define server functions callable directly from client code, with the client/server interface auto-generated, so logic moves between browser and server almost effortlessly.

Summary source: run-a, higher share of the Claims' quoted words (0.24 vs 0.12).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa26-f012146-c1

### rust-for-web-frontend--not-yet-for-frontend — Not yet for frontends: Rust backend, TypeScript frontend

Summary: Advocates, after using a Rust frontend framework on a real project, conclude "not yet" — it remains unpleasant compared to their JavaScript-ecosystem gold standard, even while feeling optimistic about its trajectory, and choose Rust for the backend and TypeScript for the frontend in the meantime.

Summary source: run-b, higher share of the Claims' quoted words (0.83 vs 0.67).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb20-f007290-c1

### rust-for-web-frontend--rust-wasm-compute-bound-only — Rust/Wasm only for compute-bound work with minimal interop

Summary: The Rust parsing itself was never the slow part — the overhead was entirely in the boundary. WASM wins only for compute-bound work with rare boundary crossings (image/video, crypto, physics, porting existing C/C++ libraries); it loses for parsing structured text into JS objects and for frequently-called functions on small inputs, because the serialization/boundary tax dominates and V8's JIT closes the raw-compute gap.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.22).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sb19-f005699-c1

### rust-for-web-frontend--rust-wasm-over-js-broadly — Rust/Wasm beats JS broadly, even for small string-heavy functions; small size and incremental adoption

Summary: JS's dynamic typing and GC pauses make web performance unreliable; Rust gives low-level control without that non-determinism, ships no runtime so `.wasm` stays small, and lets teams port only hot-path JS functions incrementally rather than rewrite everything. The blanket advice to reserve WebAssembly for only heavy compute is too simple — a hand-optimized, string-heavy hex-color-parsing function, "very hostile" to Wasm on paper, still beat its JavaScript control by roughly 2x.

Summary source: run-a, higher share of the Claims' quoted words (0.46 vs 0.35).

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: a-sa26-f011460-c1, a-sa26-f011460-c2, b-sR01-f000256-c1

## Question `rust-in-process-server-new-capability`

### rust-in-process-server-new-capability--p1 — Rust enables safe in process libification

Summary: Embedding an HTTP server as a Rust library is a genuine "lib-ification" of the web-server concept that was never realistic to do safely in C/C++; making well-written C safe to *use* generally requires isolating it in a separate process, the way nginx does, whereas Rust lets an expert's high-performance code be reused safely as a library by less-expert programmers in the same language — that reuse is what's novel.

Summary source: run-a, higher share of the Claims' quoted words (0.48 vs 0.44).

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: a-saL1-f005360-c1, a-saL1-f005360-c2

### rust-in-process-server-new-capability--p2 — Safety framing is overstated

Summary: Framing a memory-safe language's libraries against C/C++'s dangers is "getting really old" — nginx and Apache, both written in C, already work fine as web servers.

Summary source: run-a, tie on share of the Claims' quoted words (0.56), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: a-saL1-f005360-c3

## Question `rust-lang-org-ai-assistant`

### rust-lang-org-ai-assistant--p1 — An AI assistant for rust-lang.org is acceptable if strictly opt-in

Summary: Advocates argue making the feature opt-in (hidden unless enabled by a preference) would defuse resistance, noting people already bring raw ChatGPT output to the forum for help, so a built-in, opt-in assistant could improve on that status quo.

Summary source: run-b, higher share of the Claims' quoted words (0.50 vs 0.25).

Tag: taste (majority; votes tradeoff / taste / taste)

Claims: a-sa29-f013224-c1

### rust-lang-org-ai-assistant--p2 — Rust-lang.org should not host an LLM feature; the cost/quality economics make it a net negative for an underfunded open-source project

Summary: There is nothing gained and multiple problems rising from providing an LLM at rust-lang.org: good models are expensive to run well and mostly viable only for VC-subsidized companies, and tuning response quality is a full-time job the community can't sustain — users are better served using existing third-party AI services themselves.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.00).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa29-f013224-c2

### rust-lang-org-ai-assistant--p3 — Rust-lang.org's real search problem is inadequate full-text documentation search, not the absence of an LLM

Summary: Current docs.rs search matches only type/item names, not documentation prose — a concrete miss cited (searching "replace" instead of the actual function name "interpolate" in regex-automata) — so proper full-text search would be a huge step forward on its own.

Summary source: run-a, higher share of the Claims' quoted words (0.78 vs 0.44).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa29-f013224-c3

## Question `rust-ml-edge-inference-vs-python`

### rust-ml-edge-inference-vs-python--p1 — Rust burn viable for edge inference

Summary: Rust + Burn is a legitimate ML stack for edge inference specifically, not for training transformers: a single ~24MB binary versus ~7.1GB of PyTorch dependencies (300x), under 100ms cold start versus PyTorch's ~3s, and one model/codebase compiling to native GPU (wgpu), CPU (ndarray), WASM and Tauri-mobile targets.

Summary source: run-a, higher share of the Claims' quoted words (0.80 vs 0.70).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa18-f008787-c1

## Question `rust-trademark-policy`

### rust-trademark-policy--p1 — Revised 2024 draft

Summary: After community concern about the 2023 draft, the Leadership Council, Project Directors and Foundation revised the policy; the Council calls the new draft legally sound, able to protect the language's integrity, and confident it has addressed the prevailing concerns.

Summary source: run-a, higher share of the Claims' quoted words (0.73 vs 0.55).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sT12-f009632-c1

## Question `rust-vs-c-inherent-performance`

### rust-vs-c-inherent-performance--composability-wins — Composability lets engineers ship better data structures

Summary: The reason a B-Tree is usable in Rust where an AVL tree is the safer bet in C isn't raw speed, it's composability: an intrusive C B-Tree is too risky to trust with your hands in everything's underwear, so engineers default to the worse-performing structure. In Rust it's trivial to write code abstract over a data structure, so a wrong pick found in profiling can be swapped easily, whereas in C the implementation details leak through unless you wrap them in painful macros — replacing a hand-rolled generic concurrent hash table with an off-the-shelf container plus a lock came out both more maintainable and faster. What matters is what engineers are actually willing to ship, not who wins a benchmark race.

Summary source: run-b, higher share of the Claims' quoted words (0.48 vs 0.21).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa15-f005516-c1, a-saL1-f005516-c11, a-saL1-f005516-c13

### rust-vs-c-inherent-performance--init-cost-narrow — Initialization cost is a narrow edge case

Summary: Rust doesn't require init for all variables broadly — it merely requires init-before-use based on dataflow analysis, the same as any ordinary variable. The zero-init cost being described should only bite in narrow cases like large arrays or read buffers, not as a blanket tax, and it's fair to ask whether the allocator scenario generalizes at all.

Summary source: run-b, higher share of the Claims' quoted words (0.65 vs 0.47).

Tag: fact (agree; votes fact / fact / -)

Claims: a-saL1-f005516-c10

### rust-vs-c-inherent-performance--no-inherent-advantage — No inherent advantage; social factors dominate

Summary: There's no inherent reason either language is faster; it's all project-specific. Where C codebases outperform Rust ones today, that's usually because they're older and have had far more engineer-hours of optimization poured into them, not a property of C itself.

Summary source: run-b, higher share of the Claims' quoted words (0.64 vs 0.36).

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: a-saL1-f005516-c1

### rust-vs-c-inherent-performance--p1 — Rust idioms default to faster collections

Summary: The practical gap is partly ecosystem-driven: C's lack of an easily-reached-for hashmap pushes real code toward slow linear searches until it becomes a forced problem, while Rust's easy hashmaps and parallel iterators make fast-by-default collections and code the norm in practice — so the live discussion is just which language makes it easier to write fast programs.

Summary source: run-b, higher share of the Claims' quoted words (0.75 vs 0.60).

Tag: fact (agree; votes fact / fact / -)

Claims: a-saL1-f005516-c5

### rust-vs-c-inherent-performance--real-overheads — Rust has real overheads: initialization, forced refactors and copies

Summary: Safe Rust has real, measurable costs: it requires a value at construction time rather than allowing dataflow-based init-before-use, so a large array or small-object allocator ends up eagerly zero-initializing memory it may never read first, sometimes bloating codegen enough to block inlining. Trivial new features can force large refactors because they necessitate new borrowing schemes, and clones or `Rc` get added defensively just to satisfy the borrow checker where they aren't algorithmically necessary. Looking at actual disassembly on nontrivial examples shows the recurring costs plainly: bounds checks on array/division/shift access, unsafe-gated SIMD intrinsics, iterators that don't optimize as well as hoped, `RefCell` overhead, and un-collapsible `Result` wrapping — which is why Rust solutions don't top competitive-programming leaderboards.

Summary source: run-b, higher share of the Claims' quoted words (0.55 vs 0.29).

Tag: fact (agree; votes fact / fact / -)

Claims: a-saL1-f005516-c12, a-saL1-f005516-c4, a-saL1-f005516-c9

### rust-vs-c-inherent-performance--safe-rust-matches — Safe Rust matches C for demanding work (embedded display, 3D)

Summary: Safe Rust, with zero `unsafe` in the author's own code, handles several coordinated CPU-bound threads (refresh, per-frame update, event processing, asset decoding) acceptably where the same coordination would be "really hard" to get right safely in C++.

Summary source: run-a, only run with a summary.

Tag: unresolved (one run tradeoff, third fact, other run had no summary; votes tradeoff / - / fact)

Claims: b-sb26-f013214-c3

### rust-vs-c-inherent-performance--safety-cost-acceptable — A real safety cost is an acceptable trade

Summary: A real safety cost is worth paying: given a choice, a 10% perf hit (40 FPS instead of 45) for a memory-safe implementation that doesn't crash beats an unsafe/unmanaged-heavy one that tops out barely higher and still crashes.

Summary source: run-b, tie on share of the Claims' quoted words (0.75), shorter summary.

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: b-sb26-f013214-c4

### rust-vs-c-inherent-performance--types-enable-optimizations — Rust's type system enables optimizations C lacks

Summary: A language with more semantic granularity gives the compiler more true invariants to exploit — Rust code built on iteration rather than raw array access can drop bounds checks entirely, and Rust puts the equivalent of C's `restrict` on every reference without an `UnsafeCell`, encoded in the type system rather than left as a convention. That's a real, structural edge over C, on top of being ahead on pointer provenance semantics.

Summary source: run-b, higher share of the Claims' quoted words (0.60 vs 0.47).

Tag: fact (agree; votes fact / fact / -)

Claims: a-saL1-f005516-c2, a-saL1-f005516-c3

## Question `rust-vs-gc-for-multitenant-runtime`

### rust-vs-gc-for-multitenant-runtime--p1 — Rust for reliability and explicit performance

Summary: A garbage-collected language like Go doesn't have the reliability, strictness, customizability or performance needed to safely run untrusted code for many tenants — no exhaustive Result/Option error handling, hidden allocation costs, and a host GC that would conflict with an embedded engine's own GC in the same process. Rust (with some C++ for the embedded engine) was chosen instead, and Rust's cost model is transparent enough that nothing allocates without an explicit `.clone()`.

Summary source: run-b, higher share of the Claims' quoted words (0.67 vs 0.56).

Tag: tradeoff (majority; votes fact / tradeoff / tradeoff)

Claims: a-sa22-f011092-c1

## Question `rust-worth-it-for-failure-heavy-infra`

### rust-worth-it-for-failure-heavy-infra--rust-for-failure-heavy-infra — Yes for failure-heavy, high-throughput infrastructure: ownership and pattern matching tame edge cases

Summary: HTTP ingress has many concurrent edge cases (malformed/out-of-order events, disconnects, spot preemption, possibly-malicious clients); Rust's ownership and pattern matching were chosen specifically to manage that casework, and replacing an earlier Python-based ingress with the Rust service (`modal-http`, on hyper/tokio) cut 502 errors by 99.7%.

Summary source: run-a, tie on share of the Claims' quoted words (0.60), shorter summary.

Tag: tradeoff (majority; votes fact / tradeoff / tradeoff)

Claims: a-sa15-f005948-c1, b-sb19-f005948-c1

## Question `safe-wrapper-soundness-scope`

### safe-wrapper-soundness-scope--p1 — Overpromising is unsound

Summary: Calling this type "safely useable" is too vague and overpromises — a composition like boxing it with external-memory backing is not actually safe to use, so the label shouldn't claim more than the type can back up under every instantiation.

Summary source: run-b, higher share of the Claims' quoted words (0.36 vs 0.27).

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: b-sR10-f004804-c1

### safe-wrapper-soundness-scope--p2 — Pragmatic judgment call acceptable

Summary: Without a full formal proof, a cache writeback is, as far as can be told, generally a safe operation, and invalidate isn't called on these paths — so it's reasonable to call the current alignment guarantees fine for this type at this time, even if the phrasing is wishy-washy.

Summary source: run-b, higher share of the Claims' quoted words (0.81 vs 0.56).

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: b-sR10-f004804-c2

## Question `same-state-transition-trigger`

### same-state-transition-trigger--p1 — Raises same state transition question

Summary: It's genuinely unclear whether a transition into the same state the entity is already in should be excluded from triggering — this check prevents despawning on same-state transitions, and whether that's actually wanted depends on use cases not yet known.

Summary source: run-b, tie on share of the Claims' quoted words (0.75), shorter summary.

Tag: tradeoff (majority; votes fact / tradeoff / tradeoff)

Claims: b-sb14-f004398-c5

### same-state-transition-trigger--p2 — Suppress same state transitions

Summary: It doesn't really make sense to react to changing into a state you're already in — that's a no-op by nature and shouldn't trigger anything.

Summary source: run-b, higher share of the Claims' quoted words (0.75 vs 0.38).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb14-f004398-c6

### same-state-transition-trigger--p3 — Allow naive no suppression

Summary: Some users have specifically pushed for allowing same-state transitions to trigger, precisely to support a "reload" pattern, so the naive (non-special-cased) behavior is the right default here.

Summary source: run-b, higher share of the Claims' quoted words (0.85 vs 0.62).

Tag: unresolved (three-way split; votes taste / fact / tradeoff)

Claims: b-sb14-f004398-c7

## Question `scoped-impls-nameable`

### scoped-impls-nameable--p1 — Anonymous impls required for coherence

Summary: Naming these implementations is strongly the wrong call — it's detrimental for clarity, awkward syntactically, and harder to use. Anonymity keeps coherence checking simple within one scope, lets the module double as the name in error messages, and avoids the breaking-change rules naming would force whenever an implementation is later broadened.

Summary source: run-b, higher share of the Claims' quoted words (0.38 vs 0.19).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: a-sa19-f009123-c1

### scoped-impls-nameable--p2 — Named impls for clarity

Summary: Names are wanted here: an explicit mechanism to specify a type along with explicitly chosen impls would make the implicit scoped-impl behavior desugar from something writable, even if users rarely write the explicit form by hand. Names would also let two implementations of the same trait/type coexist in one module and let compiler errors point at a normal path instead of "the impl from this module."

Summary source: run-b, higher share of the Claims' quoted words (0.57 vs 0.35).

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: a-sa19-f009123-c2, a-sa19-f009123-c3

## Question `scratch-buffer-vs-per-call-alloc`

### scratch-buffer-vs-per-call-alloc--p1 — Caller owned scratch buffer

Summary: The merge working set should live in a caller-owned scratch buffer reused across calls, so the hot loop never touches the allocator at all — removing the repeated per-pre-token allocations and priority-queue construction the prior version paid for.

Summary source: run-b, higher share of the Claims' quoted words (0.87 vs 0.67).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sR12-f005120-c2

## Question `scratch-register-type-enforced`

### scratch-register-type-enforced--encode-in-types — Encode it in types

Summary: Proposes relying on the type system to identify or audit scratch-register usage, or exclusive access analogous to allocatable registers, because passing a scratch register as a parameter extends its live range and raises unintentional-clobbering risk.

Summary source: run-a, tie on share of the Claims' quoted words (0.92), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa05-f002466-c1

### scratch-register-type-enforced--p1 — Minimize the live range and avoid passing scratch registers around as parameters, even if it means redefining signatures and accepting some duplication across ISA-specific paths

Summary: Since scratch registers aren't tracked by the regalloc and must be used sparingly and with extreme caution, the live range should be minimized and passing them as parameters avoided, even if that means redefining signatures and accepting duplication across ISA-specific paths.

Summary source: run-a, tie on share of the Claims' quoted words (0.39), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR05-f002466-c1

## Question `semver-break-signaling-in-ci`

### semver-break-signaling-in-ci--p1 — Title marker plus commit marker gates ci

Summary: A change that breaks a published crate's API must carry a `!` marker in both the PR title and the branch commit that introduces the break, because the CI gate reads the PR title to skip semver-checks and require a breaking-change fragment, while release tooling reads the landed commits to decide the major-version bump.

Summary source: run-a, tie on share of the Claims' quoted words (0.80), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: b-bk03-f000267-c7

## Question `serde-centralization`

### serde-centralization--p1 — Orphan rules force derive centralization

Summary: Rust's orphan rules have created a real ecosystem composition problem: crates that want to interoperate with a popular derive macro like serde have to piggyback on it rather than add independent support, which functionally corners the ecosystem around one crate.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.57).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa25-f011413-c2

### serde-centralization--p2 — Ship type data instead of more derives

Summary: Rather than generating a new derive for every new trait or behavior, crates should ship structural data about their types once and let behaviors build generically over that data — the many-crates-on-one-derive idea is sound, but the strategy needs adjusting.

Summary source: run-a, tie on share of the Claims' quoted words (0.47), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa25-f011413-c3

## Question `serialization-format-choice`

### serialization-format-choice--cbor-for-no-std — CBOR over MessagePack for no-std

Summary: Switched metadata serialization from MessagePack (`rmp-serde`) to CBOR (`ciborium`) because `rmp-serde` isn't no-std compatible and its upstream has been inactive over a year, while CBOR is IETF-standardized, serde-recommended, no-std-capable, and preserves enum variant information.

Summary source: run-a, higher share of the Claims' quoted words (0.86 vs 0.43).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sR08-f003587-c1

### serialization-format-choice--established-binary-format — An established binary format (postcard), with variant order as a stability contract

Summary: Postcard is preferred as a simpler, well-defined, already-similar-to-current-output format over a bespoke or JSON serialization; separately, since postcard is non-self-describing, enum case order must be preserved as a stability contract for the protocol to remain stable long-term — a requirement to design around, not a reason to avoid it.

Summary source: run-a, tie on share of the Claims' quoted words (0.55), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa03-f002300-c1, a-sa06-f003590-c2

### serialization-format-choice--no-custom-format — A custom config language is too costly

Summary: After evaluating `serde_yml`, `serde_yaml` and `facet-yaml`, YAML tooling in the Rust ecosystem is a dead end for i128 support; defining a custom config language is an alternative, but probably too much effort to "just try it."

Summary source: run-b, higher share of the Claims' quoted words (0.54 vs 0.38).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb09-f003030-c5

### serialization-format-choice--p1 — Avoid bincode for new persisted data

Summary: Bincode is called out as a risky format for anything new because it depends on the exact order and type of struct fields; legacy column families keep it, but new ones should not use it.

Summary source: run-a, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: b-bk03-f000267-c9

### serialization-format-choice--ship-now-switch-later — Ship now, switch format later

Summary: This format is strictly internal right now, so proceed with YAML plus workarounds, and switch library or format later if something better shows up.

Summary source: run-b, higher share of the Claims' quoted words (0.77 vs 0.38).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb09-f003030-c7

### serialization-format-choice--toml-for-consistency — TOML for ecosystem consistency

Summary: Why not TOML, to stay consistent with the rest of the Rust ecosystem?

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb09-f003030-c1

### serialization-format-choice--yaml-for-convenience — YAML for convenience, patching the library

Summary: TOML's representation is inconvenient for this use case; YAML is the nicest representation available, and the spec doesn't forbid wider integers even if it doesn't mandate them, so the missing i128 support is a library gap worth patching (or trying an alternative crate like facet-yaml) rather than a reason to abandon YAML — especially since `serde_yml` itself looks unmaintained.

Summary source: run-b, higher share of the Claims' quoted words (0.52 vs 0.36).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb09-f003030-c2, b-sb09-f003030-c3, b-sb09-f003030-c4, b-sb09-f003030-c6

## Question `service-fault-isolation-degrade`

### service-fault-isolation-degrade--contain-and-continue — Contain, log, keep serving

Summary: `Incoming::accept` can fail for benign network reasons, and such failures should be logged and passed over, not treated as fatal. More broadly, commit as a design rule before writing any code that any failure degrades to a blank frame or a missing element, never a dead session — the service has to keep rendering hostile, unreliable input without ever dropping the session it's holding.

Summary source: run-b, higher share of the Claims' quoted words (0.83 vs 0.75).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR05-f001981-c1, a-sa14-f004985-c3

## Question `share-via-combinator-vs-separate-impls`

### share-via-combinator-vs-separate-impls--p1 — Extract a shared combinator even if unexposed

Summary: `reduce_sum` and `all_reduce_sum` are different operations, but the duplication between them is real and worth solving with a local op-combinator library — even if that library never gets exposed to end users.

Summary source: run-b, tie on share of the Claims' quoted words (0.60), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR11-f003983-c2

## Question `shared-hw-resource-refcount-vs-raii`

### shared-hw-resource-refcount-vs-raii--p1 — Reference counted controller

Summary: Unless references are counted per modem clock controller, repeatedly calling the function to disable the PHY clock on one controller would eventually disable it even while a different modem still relies on it — so a `RadioClockController` needs its own per-modem reference count.

Summary source: run-b, higher share of the Claims' quoted words (0.82 vs 0.24).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa05-f003169-c1

### shared-hw-resource-refcount-vs-raii--p2 — Raii exclusive ownership

Summary: Questions why a separate controller and manual ref-count are needed at all when only the peripheral singletons — already unique and exclusive by construction — can touch the clock; the clock-control logic should live directly on the radio peripheral structs, and the author ultimately removed the separate ref-counted controller in favor of this.

Summary source: run-a, tie on share of the Claims' quoted words (0.30), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa05-f003169-c2, a-sa05-f003169-c3

## Question `shared-model-crate-vs-domain-split`

### shared-model-crate-vs-domain-split--p1 — Keep one shared low-level "model" crate rather than doing a full domain-driven crate split

Summary: A domain-driven crate split was something that could have been done, but by the time it came up the project was already too far along — there wasn't the time or energy left to do it, so `model` stayed the catch-all for whatever must be shared, kept as small as discipline allows.

Summary source: run-b, tie on share of the Claims' quoted words (0.44), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb25-f012561-c2

## Question `shared-mutable-state-vs-explicit-passing`

### shared-mutable-state-vs-explicit-passing--restructure-for-explicit-ownership — Avoid implicit shared state; pass context or `&mut`, drop forced `Arc`

Summary: Preference runs toward moving mutable state to its owning context rather than wrapping it for sharing: move state onto the owning `Session` rather than adding an internal `Mutex`; prefer no `Arc` even after conceding an immediate `Sync` bound currently requires it, wanting to revisit later; object to a `Buffer` holding an `Arc<Mutex<>>` that lets callers change encoding invisibly, wanting it passed/returned explicitly instead; and, after retracting an `Rc<RefCell<_>>` fix that still panicked on reentrant borrows, float passing a `cx` context down the stack instead, matching the rest of the codebase's existing pattern.

Summary source: run-a, higher share of the Claims' quoted words (0.42 vs 0.39).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR07-f002155-c1, a-sR07-f002155-c2, a-sa06-f003414-c2, b-sb04-f001022-c1, b-sb04-f001022-c2

### shared-mutable-state-vs-explicit-passing--shared-where-structure-demands — `Rc`/`Arc` where reader count is hard to know; `RefCell` narrowly

Summary: `Rc`/`Arc` are recommended when the program's structure makes it hard to tell how many readers a piece of data will have; `RefCell` moves borrow rules to runtime, works only single-threaded, and panics on violation, so it fits only a narrow range of problems.

Summary source: run-a, tie on share of the Claims' quoted words (0.82), shorter summary.

Tag: tradeoff (majority; votes fact / tradeoff / tradeoff)

Claims: b-sT09-f005440-c1

## Question `ship-polyfill-before-spec`

### ship-polyfill-before-spec--p1 — Favors shipping a polyfill ahead of the spec

Summary: Favors shipping a "polyfill" that developers can play with today while they wait for WASI 0.3 and real async, rather than waiting for the finished standard.

Summary source: run-a, tie on share of the Claims' quoted words (0.88), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR03-f000889-c1

## Question `silent-fallback-vs-explicit-error`

### silent-fallback-vs-explicit-error--fail-loudly — Fail loudly and fix the cause

Summary: An `allow_missing = true` option that lets the build succeed and then 404 at request time turns a build-time problem into a silent runtime one — a bad default. `unwrap_or_default()` mostly hides the problem rather than fixing it: a server function that actually sets `ResponseOptions` would silently fail to have its header/status applied. Find and fix the real cause — a disposed Runtime. Asks whether the code should return an error when multiple TCP sockets are listed, rather than silently using the first, since picking the first could cause odd behavior if it's the wrong one. Made both the multiple-socket case and the no-usable-socket case an error, reasoning it would be surprising for an explicit flag like `--systemd-listenfd` to silently fall back to the tool listening itself because of a mismatched environment variable.

Summary source: run-a, higher share of the Claims' quoted words (0.55 vs 0.53).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa14-f005079-c6, a-sa14-f005079-c7, b-sR10-f004706-c1, b-sb03-f000669-c2

### silent-fallback-vs-explicit-error--silent-fallback — Fall back silently

Summary: Patch leptos-axum so a missing `ResponseOptions` context resolves via `unwrap_or_default()` instead of panicking — a workaround for callers who don't touch `ResponseOptions` anyway.

Summary source: run-a, higher share of the Claims' quoted words (0.55 vs 0.18).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb03-f000669-c1

## Question `single-pass-vs-multi-pass-iteration`

### single-pass-vs-multi-pass-iteration--p1 — Prefer single-pass computation over iterating a collected result multiple times

Summary: If you're iterating and collecting, then iterating the result three more times, it's neater to iterate once and collect the max for each column in that single pass.

Summary source: run-b, tie on share of the Claims' quoted words (0.82), shorter summary.

Tag: taste (majority; votes taste / tradeoff / taste)

Claims: b-sR03-f000763-c2

## Question `single-vs-multi-threaded-executor`

### single-vs-multi-threaded-executor--p1 — Measure for the specific workload, no blanket rule

Summary: A multi-threaded executor can speed up workloads with many tasks by making progress on several at once, but synchronizing data between tasks gets more expensive; rather than defaulting to one or the other, measure performance for your application when choosing between a single- and multi-threaded runtime.

Summary source: run-b, higher share of the Claims' quoted words (0.90 vs 0.80).

Tag: fact (agree; votes fact / fact / -)

Claims: b-bk01-f000233-c13

## Question `slint-vs-qt`

### slint-vs-qt--p1 — Prefer Slint over QML/Qt for new Rust GUI work despite Slint's current feature gaps

Summary: Having reimplemented an existing QML demo app in Slint from scratch, Slint currently seems like the best toolkit for Rust — its build-time-checked, Rust-native, easily cross-compiled model is worth the tradeoff against QML's more mature multimedia/3D/testing tooling and Qt's licensing costs, especially for embedded targets.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.83).

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: b-sb23-f011133-c1

## Question `sound-lifetime-erasure-in-callbacks`

### sound-lifetime-erasure-in-callbacks--p1 — Thread local scoped storage over raw pointer cast

Summary: Casting away a reference's lifetime to store it for a later callback isn't really allowed — at any point there might be an aliased mutable reference, and a comment claiming the lifetime outlives the callback doesn't hold since the external API is free to do what it wants. The sound fix is a thread-local holding the pointer only for the duration it's actually needed — still `unsafe`, but far easier to reason about than a bare raw-pointer cast.

Summary source: run-b, higher share of the Claims' quoted words (0.81 vs 0.44).

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: b-sR04-f001749-c1

## Question `spawn-vs-compose-futures`

### spawn-vs-compose-futures--p1 — Prefer spawn+JoinHandles for parallelism

Summary: If parallelism is wanted, or not explicitly excluded, spawning separate tasks is usually simpler than `join!`/`select!` — less error-prone, more general, and each spawned task gets a fair scheduling share, giving more predictable performance than composing futures inside one task. The tradeoff is less structure and harder-to-reason-about lifecycle and resource management.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.89).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-bk01-f000233-c5

## Question `speculative-from-impls`

### speculative-from-impls--p1 — Avoid speculative trait impls that would break under a later addition

Summary: Remove a speculative conversion now, because adding another `From` impl for the same type later would produce a compile error on existing code.

Summary source: run-a, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: a-sa11-f004265-c2

## Question `spi-hardware-cs-in-spibus`

### spi-hardware-cs-in-spibus--p1 — Software cs via spidevice

Summary: Chip select should just be an ordinary GPIO `Output` pin — that way one bus can address as many targets as there are available GPIOs. Hardware chip-select complicates the embedded-hal `SpiBus`/`SpiDevice` split, which is why most HALs tend not to use it.

Summary source: run-b, higher share of the Claims' quoted words (0.65 vs 0.60).

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: a-sa09-f004055-c3, a-sa09-f004055-c4

### spi-hardware-cs-in-spibus--p2 — Support both type level distinction

Summary: Use marker types (`HardwareCs`, `NoCs`) so `SpiBus` is implemented only for the no-hardware-CS variant, following embedded-hal semantics where `SpiBus` means exclusive bus access without CS management — while a separate constructor still exposes hardware CS for callers who specifically want it.

Summary source: run-b, higher share of the Claims' quoted words (0.83 vs 0.67).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa09-f004055-c5

## Question `stable-contract-api-vs-cli`

### stable-contract-api-vs-cli--p1 — Rpc cli stable rust api unstable

Summary: The Rust APIs of the crates are currently unstable and unsupported; the versioned, supported surface for interacting with the application is the CLI commands and JSON-RPCs, not the Rust library API.

Summary source: run-b, tie on share of the Claims' quoted words (0.75), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: b-bk03-f000267-c10

## Question `state-accessor-and-stream-split`

### state-accessor-and-stream-split--p1 — Split into two primitives

Summary: A single primitive tried to serve two very different consumers — "what's the state right now" and "tell me when it changes" — and was replaced by two dedicated primitives, a lifetime-bound borrowed snapshot and a `'static` event stream, each answering one question.

Summary source: run-a, higher share of the Claims' quoted words (0.53 vs 0.33).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR13-f004685-c1

## Question `static-allocation-in-real-time`

### static-allocation-in-real-time--p1 — Static allocation preferred over dynamic in real-time systems

Summary: Dynamic allocation is problematic for resource-constrained real-time systems on both performance and reliability grounds — Rust panics on out-of-memory — so static allocation is the preferable approach.

Summary source: run-b, tie on share of the Claims' quoted words (0.80), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB01-f000227-c4

## Question `static-model-security-guarantees`

### static-model-security-guarantees--p1 — RTIC+Rust's static model extends integrity guarantees system-wide; traditional RTOS kernel security covers only the kernel

Summary: Even a formally verified RTOS kernel like seL4 only claims integrity, confidentiality and availability for the kernel itself, not the whole system, especially once dynamic allocation enters the picture. A declarative, static, system-wide task/resource model, combined with Rust's compile-time aliasing, mutability and lifetime guarantees, propagates integrity properties across the whole system instead of stopping at the kernel boundary.

Summary source: run-b, higher share of the Claims' quoted words (0.28 vs 0.22).

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: a-sB04-f000227-c4

## Question `static-verification-no-panic-mechanism`

### static-verification-no-panic-mechanism--p1 — Custom compiler driver post mono

Summary: Clippy lints don't recurse into dependencies and only cover hard-coded library types; an effect-type system would require a new language; a link-time hack is optimization-dependent, has no async support, and breaks under `panic = "abort"`/no_std; cfg-forking the standard library affects every consumer and breaks tooling. The most accurate approach, now shipped and certified against, is a custom rustc driver using a post-monomorphization pass to detect every resolved function call.

Summary source: run-b, tie on share of the Claims' quoted words (0.73), shorter summary.

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: b-sR12-f005169-c1

## Question `std-mutex-vs-async-mutex`

### std-mutex-vs-async-mutex--p1 — Prefer std Mutex where possible

Summary: Recommends using `std::Mutex` where possible, reserving the async `Mutex` for cases where the lock must be held across an `.await` point or protects an IO resource, since the async version costs more precisely because it supports that.

Summary source: run-a, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: b-bk01-f000233-c8

## Question `std-naming-convention-imperfect-fit`

### std-naming-convention-imperfect-fit--p1 — Reuse the `raw_parts`-style name anyway; std's convention doesn't have to apply exactly to a non-std crate

Summary: `raw_parts` works even though there's no matching `into_raw_parts` here, only `from_raw_parts` — but this isn't the standard library, so it's fine if the pattern doesn't apply exactly.

Summary source: run-b, higher share of the Claims' quoted words (0.69 vs 0.62).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sR05-f002326-c1

## Question `std-naming-conventions-strictness`

### std-naming-conventions-strictness--loose — Reuse the convention loosely, or rename to a bare verb

Summary: `Clone`/`Borrow` aren't named `ToCloned`/`AsBorrowed`, so the `to_`/`as_`/`into_` prefix is unneeded morphology when converting between representations of the *same* type — it should just be `Own`, and `"whatever".own()` reads better than `"whatever".to_owned()` — even while granting the prefix convention makes sense for genuine cross-type conversions like `IntoIterator`.

Summary source: run-b, higher share of the Claims' quoted words (0.40 vs 0.00).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sb22-f009236-c1

### std-naming-conventions-strictness--strict — Follow the convention strictly (`into_` consumes, `to_owned` is correct)

Summary: `into_` should only be used where the method actually consumes `self` — a name that doesn't match its ownership signature should be renamed. `to_owned` in particular is not a bad name: the receiver is neither doing the owning nor being owned, it's being copied into a different form, so `own()` would misdescribe the operation — the Rust API Guidelines document is the standing rationale for the `to_` prefix here, and naming here, while inherently imperfect, isn't wrong.

Summary source: run-b, higher share of the Claims' quoted words (0.46 vs 0.31).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sR08-f003587-c2, b-sb22-f009236-c2, b-sb22-f009236-c3

## Question `synthetic-canary-vs-tracing`

### synthetic-canary-vs-tracing--p1 — Synthetic canary over tracing real traffic

Summary: Because no timing information about real source messages may leave the on-premises node, tracing real messages is off the table; instead a "message canary" sends real encrypted messages through the live system once an hour, measuring delivery time and alarming past a threshold.

Summary source: run-a, tie on share of the Claims' quoted words (0.67), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb24-f011295-c3

## Question `tail-expression-vs-explicit-return`

### tail-expression-vs-explicit-return--p1 — Tail expression hurts readability

Summary: Coming from a lot of Rust work, the last-expression rule seriously hurts readability for both function returns and `if` expressions — worst of all when the block is long and the last expression sits far from the assignment it feeds.

Summary source: run-b, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: b-sT02-f000576-c1

### tail-expression-vs-explicit-return--p2 — Tail expression reads better

Summary: Experience runs the other way: Rust's implicit return of the last expression is much easier to read than `return` statements everywhere.

Summary source: run-a, tie on share of the Claims' quoted words (0.91), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: b-sT02-f000576-c2

## Question `target-tier-without-ci`

### target-tier-without-ci--p1 — Demote to Tier 2 with host tools

Summary: The tier policy requires Tier 1 platforms to run CI tests; with free macOS x86_64 CI runners ending, the target is demoted to Tier 2 with host tools from the named release — builds still ship, but the target will likely accumulate bugs faster and could be demoted further.

Summary source: run-a, tie on share of the Claims' quoted words (0.67), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: a-sT12-f009704-c1

## Question `teach-rust-in-curricula`

### teach-rust-in-curricula--p1 — Teach Rust directly to force systems understanding

Summary: Modern software education over-focuses on frameworks and abstractions and under-teaches how systems actually work — memory, concurrency, performance, tradeoffs. It's not bad to use frameworks, but it's valuable to understand what's going on behind the wood, and Rust forces students to confront ownership, memory and error handling directly, concepts other languages abstract away.

Summary source: run-b, higher share of the Claims' quoted words (0.64 vs 0.43).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa26-f011443-c1

## Question `test-via-real-entry-point`

### test-via-real-entry-point--p1 — Test via real entry point

Summary: Even after a fix, nothing tests the actual gesture: existing tests drive the toggle/switch methods directly rather than the deferred mouse-event path itself, so they'd keep passing even if the real keybinding wiring broke; wants at least one test to dispatch the real action via a keystroke against the real strip.

Summary source: run-a, tie on share of the Claims' quoted words (0.83), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa13-f004772-c3, a-sa13-f004772-c4

### test-via-real-entry-point--p2 — Entry point testing plus fallible conversion audit

Summary: The dangerous bugs aren't in new code, they're in what old code used to do that nothing does anymore — a refactor can silently stop enforcing a check with no test failing and no diff showing a deleted check. The guide requires inventorying every rejection the old code could produce and naming its new home, testing every parse-time rejection through the actual production entry point rather than only the check's own unit tests, and individually auditing fallible conversions (`.ok()`, `unwrap_or`, defaulted `try_from`) that could silently turn an invalid value into one a check treats as benign — two real incidents slipped through this exact gap with green CI.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.60).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-bk03-f000267-c15

## Question `threads-vs-simd-for-batch-work`

### threads-vs-simd-for-batch-work--p1 — Simd for small batches combine with threads for large batches

Summary: Instruction-level parallelism alone is a good choice for a small batch of blobs — decent speedup, stays on one CPU, doesn't affect the rest of the program — but for peak performance, combining instruction-level and thread-level parallelism wins, measured at 17x over sequential and 2.1x over thread-level parallelism alone.

Summary source: run-b, higher share of the Claims' quoted words (0.75 vs 0.60).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sR08-f003702-c1

## Question `tiered-checked-unchecked-apis`

### tiered-checked-unchecked-apis--p1 — Offer tiered apis

Summary: Deliberately exposes three ways to build the same row — a positional fast API for best performance, a safe API that validates field names, and an indexed API balancing the two — so callers pick their own safety/performance tradeoff rather than the crate picking one for them.

Summary source: run-a, tie on share of the Claims' quoted words (0.67), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sR16-f012642-c1

## Question `timer-instant-overflow-panic`

### timer-instant-overflow-panic--p2 — Never ready without panic

Summary: The correct behavior is to never register a future as ready again once its wake time would overflow, rather than firing based on a MAX-derived time that undershoots — Tokio's `far_future()` hack is unnecessary. One version of this position keeps a sleeping future alive but never fires it early, reserving a panic only for the extremely unlikely case that `Instant::now` itself reaches `Instant::MAX`, since no reasonable behavior exists past that point.

Summary source: run-b, higher share of the Claims' quoted words (0.67 vs 0.58).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa19-f009196-c5, a-sa19-f009196-c6

## Question `tokio-as-default-runtime`

### tokio-as-default-runtime--p1 — Tokio as default runtime

Summary: Recommends Tokio as the guide's runtime for most readers because it's general purpose, the most popular in the ecosystem, and good for both getting started and production, while noting other runtimes may perform better or simplify code in some circumstances.

Summary source: run-a, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: b-bk01-f000233-c3

### tokio-as-default-runtime--p2 — No official recommendation, list options neutrally

Summary: There is no asynchronous runtime in the standard library, and none are officially recommended — Tokio, async-std, smol and fuchsia-async are listed as options without ranking, and cross-runtime incompatibility (Tokio's mio-based reactor vs. the async-executor/futures-I/O-trait world of async-std and smol) is a reason to research fit before committing to one.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.57).

Tag: fact (agree; votes fact / fact / -)

Claims: b-bk01-f000233-c4

### tokio-as-default-runtime--tokio-default — Tokio

Summary: Despite criticisms of Tokio, the alternatives are limited — async-std stale, smol inactive, glommio Linux-only — so Tokio remains the best option, reinforced by being quinn's default. It's often regarded as the one true async runtime and powers much of Rust's networking ecosystem.

Summary source: run-b, higher share of the Claims' quoted words (0.85 vs 0.70).

Tag: tradeoff (majority; votes tradeoff / taste / tradeoff)

Claims: a-sa29-f012940-c2, b-sb17-f005159-c1

## Question `tokio-axum-vs-nginx-performance`

### tokio-axum-vs-nginx-performance--p1 — Nginx's tuning advantage isn't matched by async Rust out of the box

Summary: It's difficult to see how an untuned "out of the box" async Rust server could be competitive, since nginx is highly-tuned async C++ and the comparison isn't apples to apples.

Summary source: run-b, higher share of the Claims' quoted words (0.88 vs 0.62).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa14-f005360-c5

### tokio-axum-vs-nginx-performance--p2 — Tokio competitive out of the box

Summary: Cloudflare replaced nginx in production with the Tokio-based Pingora proxy — Tokio is pretty fast out of the box, and Rust's async was designed from the ground up to be very low overhead.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.85).

Tag: fact (agree; votes fact / fact / -)

Claims: a-saL1-f005360-c7

### tokio-axum-vs-nginx-performance--p3 — Axum framework overhead hurts raw performance

Summary: Tokio and Hyper are both very fast on their own, but Axum adds its own routing/extractor overhead on top — surprising, since Actix-Web previously topped benchmarks while also providing routing and extractors, so Axum wasn't expected to differ much. Where complex path routing and extractors aren't needed, it's probably better to use Hyper and Tower directly.

Summary source: run-b, higher share of the Claims' quoted words (0.69 vs 0.54).

Tag: fact (agree; votes fact / fact / -)

Claims: a-saL1-f005360-c8, a-saL1-f005360-c9

## Question `totokens-intermediate-tokenstream`

### totokens-intermediate-tokenstream--p1 — Avoid building a temporary `TokenStream` in a `ToTokens` impl; match on the enum and call `to_tokens` on the matched arm directly

Summary: Rewrite the `ToTokens` impl so each match arm calls `to_tokens` on its inner value directly, avoiding allocating a temporary `TokenStream` just to feed it into another.

Summary source: run-a, higher share of the Claims' quoted words (0.83 vs 0.67).

Tag: taste (majority; votes taste / tradeoff / taste)

Claims: a-sR01-f000538-c1

## Question `tower-middleware-vs-handler-helpers`

### tower-middleware-vs-handler-helpers--middleware-layer — A middleware or connection-hook layer

Summary: An `EndpointHooks`-style trait intercepts connections before connect and after handshake, so authentication, authorization, rate limiting and observability sit at the connection layer and individual protocols stay on their core logic instead of each handling auth themselves; surveying the wider ecosystem, most codebases instead bolt these concerns directly into handlers via ad-hoc helpers, macros or trait extensions, none of which quite match the convenience and composability of a real middleware stack.

Summary source: run-a, tie on share of the Claims' quoted words (0.80), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sT08-f004169-c3, b-sb22-f008906-c1

## Question `trace-context-propagation-mechanism`

### trace-context-propagation-mechanism--p1 — No fully good solution yet

Summary: There is no one all-good solution today for context propagation in distributed scenarios: the eBPF kernel function that could write into user-space memory was locked down in 2021 over security concerns and its replacement can crash the user-space program, while the traditional library-interposition alternative works well but gets messy when the libraries are statically linked.

Summary source: run-a, tie on share of the Claims' quoted words (0.86), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: b-sb24-f011306-c3

## Question `tracing-crate-vs-otel-api`

### tracing-crate-vs-otel-api--p1 — Keep both with better interop for now

Summary: The Tokio `tracing` crate is widely adopted but not fully suited to distributed tracing, while the OpenTelemetry API is spec-compliant but far less adopted; the community has debated dropping one, but the current practical (still unstable) path is to keep both active and improve interoperability between them.

Summary source: run-a, tie on share of the Claims' quoted words (0.35), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb24-f011306-c1

## Question `tracing-vs-log-for-otel`

### tracing-vs-log-for-otel--p1 — Use the `tracing` crate, not a conventional logging crate, as the logging facade for a new Rust app that will adopt OpenTelemetry

Summary: The OpenTelemetry Rust project bridges existing loggers rather than mandating its own API, but recommends `tracing` for new applications because its Span concept aligns with OTel spans.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.80).

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: a-sa29-f012940-c1

## Question `trait-api-forced-arc-self`

### trait-api-forced-arc-self--p1 — Drop the forced `Arc` requirement from `ProtocolHandler` for a more flexible structure

Summary: The trait previously required using explicit `Arc`s, but this is no longer required, allowing a more flexible structure in defining protocols.

Summary source: run-b, higher share of the Claims' quoted words (0.83 vs 0.75).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR05-f002453-c2

## Question `trait-default-methods-vs-major-bump`

### trait-default-methods-vs-major-bump--p1 — Default impls to avoid breaking change

Summary: Provide default implementations for the new trait methods for now so they don't trigger a backward-incompatible change, and ship them in a minor release — planning to make them required only in the next major version.

Summary source: run-b, tie on share of the Claims' quoted words (0.41), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR08-f003540-c1, b-sR08-f003540-c2

## Question `trait-error-open-custom-variant`

### trait-error-open-custom-variant--p1 — Give public-trait errors an open Custom/User variant

Summary: For traits users can implement themselves, the associated error type includes a `User`/custom variant plus `from_err`/`from_err_box` helpers, so implementors can propagate their own errors rather than being boxed into the crate's own failure modes.

Summary source: run-a, tie on share of the Claims' quoted words (0.42), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa14-f005149-c3

## Question `trait-impl-boilerplate-mechanism`

### trait-impl-boilerplate-mechanism--p1 — New impl shorthand syntax

Summary: Proposes new dedicated impl shorthand syntax for traits with exactly one required method, generalized as official syntactic sugar, removing an indentation level and the need to look up the method's exact signature.

Summary source: run-a, tie on share of the Claims' quoted words (0.38), shorter summary.

Tag: taste (majority; votes taste / tradeoff / taste)

Claims: a-sa19-f009292-c7

### trait-impl-boilerplate-mechanism--p2 — Infer associated types

Summary: There's really no need to write out `type Item = i32;` when it's the only possible thing given the method body — the compiler should infer associated types like `Iterator::Item` from context, simplifying `Add`, `Sub`, `IntoIterator` and `Deref` impls without new surface syntax.

Summary source: run-b, higher share of the Claims' quoted words (0.89 vs 0.11).

Tag: taste (majority; votes taste / tradeoff / taste)

Claims: a-sa19-f009292-c8

## Question `traits-as-inheritance-substitute`

### traits-as-inheritance-substitute--p1 — Adequate but more verbose

Summary: Modeling an OOP-style view/component hierarchy in Rust via supertrait/subtrait relationships works, but doing it generically over the inner-storage type takes a lot more work and is, in his words, more verbose and somewhat confusing especially coming from Kotlin, Java or TypeScript.

Summary source: run-b, higher share of the Claims' quoted words (0.70 vs 0.40).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sR16-f012428-c1

## Question `trust-microbenchmarks`

### trust-microbenchmarks--distrust-by-default — Distrust by default

Summary: Benchmarks are, always, generally, dangerous to quote because they're a special type of lie; microbenchmarks especially — his own "Canada" benchmark against serde_json isn't apples-to-apples because it skips a precise floating-point rounding mode, and conference benchmarks given without a right of reply should be treated as suspect by default. Blanket moral opposition: they should all be consumed by gaping fissures in the earth's crust.

Summary source: run-b, higher share of the Claims' quoted words (0.71 vs 0.38).

Tag: fact (majority; votes taste / fact / fact)

Claims: a-sa25-f011413-c6, a-sa28-f012469-c1, a-sa28-f012469-c2

## Question `typed-response-struct-vs-untyped-value`

### typed-response-struct-vs-untyped-value--p1 — Typed response struct

Summary: Leverage Rust's strong typing to do the work: replace untyped JSON output with a `Serialize` struct so the compiler validates the response shape.

Summary source: run-b, higher share of the Claims' quoted words (0.83 vs 0.67).

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: a-sT11-f007659-c3

## Question `typed-wrapper-vs-raw-access`

### typed-wrapper-vs-raw-access--p1 — Dedicated types recommended over raw matrices

Summary: A raw matrix type cannot guarantee it represents a pure rotation, isometry, or even an invertible transform, so dedicated transformation types are recommended instead of raw matrices.

Summary source: run-a, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB01-f000217-c2

### typed-wrapper-vs-raw-access--p2 — Typed wrapper over raw api

Summary: Typing a column family's name out every time is error-prone — a typo causes a panic since the column family doesn't exist — so define the name and type of each column family once and route every read/write through a typed method. Likewise, raw volatile register operations should be questioned in favor of PAC-generated typed accessors, and if the PAC is missing an accessor, that's a bug to fix in the PAC, not a reason to fall back to manual bit operations.

Summary source: run-b, higher share of the Claims' quoted words (0.65 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa09-f004055-c1, a-sa09-f004055-c2, b-bk03-f000267-c8

## Question `typestate-crypto-keys`

### typestate-crypto-keys--p1 — Yes use typestate for keys

Summary: Types give superpowers: they let the rules of a system be encoded in a way checked at compile time, helping prevent mistakes. Cryptographic keys get a `Role` marker type and a verified/unverified type-state, so passing a cover-node key where a journalist-provisioning key is required fails to compile, and an unverified key can't be used cryptographically until explicitly checked.

Summary source: run-b, higher share of the Claims' quoted words (0.85 vs 0.38).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb24-f011295-c2

## Question `typestate-generic-vs-separate-types`

### typestate-generic-vs-separate-types--p1 — Unified generic typestate

Summary: Separate structs per connection variant duplicated the whole connection API and stopped connections sharing code paths; a single generic type with a state parameter restores that flexibility and de-duplicates the code, with state-specific signatures only where behavior actually differs.

Summary source: run-a, tie on share of the Claims' quoted words (0.38), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sT08-f004169-c1

## Question `ui-async-data-cache-vs-component`

### ui-async-data-cache-vs-component--p1 — Component owns async lifecycle

Summary: A hand-rolled cache, hover-triggered prefetch, and version-keyed invalidation are accidental complexity that exists only because a popover builder is synchronous; the fix is to let the menu entity spawn its own async fetch and render a loading state — "how every picker works" — which one reviewer's rework then delivered: one async menu entity fetching its own data per step, eliminating the cache, prefetch, and re-anchoring flag by construction.

Summary source: run-a, higher share of the Claims' quoted words (0.62 vs 0.57).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa13-f004772-c1, a-sa13-f004772-c2

## Question `ui-dsl-vs-plain-rust`

### ui-dsl-vs-plain-rust--p1 — Value depends on priorities

Summary: If you want to avoid DSLs and macros and write only regular Rust, egui offers that; if you like DSL-driven UIs with serious developer-tooling investment (a better error-message ceiling since it's a standalone language, not just macros), Slint might be for you — no overall winner between the two approaches.

Summary source: run-b, higher share of the Claims' quoted words (0.88 vs 0.38).

Tag: unresolved (three-way split; votes fact / taste / tradeoff)

Claims: b-sb21-f008390-c2

## Question `ui-state-scoped-lifetimes-vs-runtime-handles`

### ui-state-scoped-lifetimes-vs-runtime-handles--p1 — Copy runtime tracked state

Summary: The `'bump`-lifetime scope model doesn't work for `'static` futures and produces confusing lifetime errors — replace it with `Copy` signals backed by a generational-box allocator: essentially a light form of garbage collection bolted onto Rust, using component lifecycles as the trigger for dropping state.

Summary source: run-b, higher share of the Claims' quoted words (0.56 vs 0.48).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb17-f005144-c1

## Question `unchecked-unwrap-vs-safe-abort`

### unchecked-unwrap-vs-safe-abort--p1 — Safe-abort(default recommendation)

Summary: Panics translate into aborts on wasm32-unknown-unknown anyway, so a safe helper that calls `process::abort()` on None/Err gives the same behavior as unwrap without the formatted-panic code bloat.

Summary source: run-b, higher share of the Claims' quoted words (0.92 vs 0.50).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB02-f000256-c8

### unchecked-unwrap-vs-safe-abort--p2 — Unsafe unchecked(conditional)

Summary: The `unreachable` crate's unsafe `unchecked_unwrap` is a further, riskier alternative, restricted to cases where the programmer is "110% sure" the assumption holds — and only in release builds, keeping checked behavior in debug.

Summary source: run-b, tie on share of the Claims' quoted words (0.50), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB02-f000256-c9

### unchecked-unwrap-vs-safe-abort--p3 — Prefer a safe abort-on-None/Err wrapper over unsafe unchecked unwrapping; reserve the unsafe route for near-certainty, kept checked in debug builds

Summary: The safe `process::abort`-based `unwrap_abort` is the default way to drop panic-infrastructure bloat; the unsafe `unchecked_unwrap` is a further step, explicitly conditioned on near-total certainty plus a debug build that still checks.

Summary source: run-b, tie on share of the Claims' quoted words (0.11), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-bk02-f000256-c12

## Question `uniffi-packaging-xcode-vs-script`

### uniffi-packaging-xcode-vs-script--p1 — Run Rust-to-Swift FFI packaging as an external shell-script/CI pipeline, not as an Xcode build phase

Summary: It's possible to wire UniFFI's binding generation into an Xcode build phase, but given the relative difficulty of doing that and the overall flakiness of the Xcode build process, a simple, reliable shell script was chosen instead — at the cost of needing a manual rebuild after Rust changes.

Summary source: run-b, higher share of the Claims' quoted words (0.93 vs 0.71).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa27-f012237-c1

## Question `unmaintained-dependency-weight`

### unmaintained-dependency-weight--p1 — Prefer actively-maintained broad-scope crate over flagged narrow one

Summary: A crate flagged unmaintained, buggy and legacy per a RustSec advisory should give way to a more modern crate, even when that modern crate's stated focus (the Web) is narrower than the original's scope.

Summary source: run-a, tie on share of the Claims' quoted words (0.57), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa06-f003414-c1

## Question `unsafe-fields-design`

### unsafe-fields-design--p1 — Minimal field level rules

Summary: Field safety tooling reduces to two rules: a field should be marked unsafe if it carries a safety invariant of any kind, and a field marked unsafe is unsafe to use — settled after an observation that the additive/subtractive dichotomy and its Drop-related concerns could be sidestepped, since a field already can't be put into an unsound-to-drop state without unsafe code.

Summary source: run-b, higher share of the Claims' quoted words (0.90 vs 0.80).

Tag: tradeoff (majority; votes fact / tradeoff / tradeoff)

Claims: a-sa20-f009698-c2

## Question `unsafe-mental-model`

### unsafe-mental-model--p1 — Unsafe is manual invariant maintenance not permission to break rules

Summary: Unsafe code isn't for violating Rust's invariants, it's for maintaining them manually.

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: fact (majority; votes taste / fact / fact)

Claims: a-sa28-f012469-c11

### unsafe-mental-model--p2 — Unsafe is a last resort not a nuclear option

Summary: Using unsafe is less "nuclear option" and more "diplomacy has failed."

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa28-f012469-c12

## Question `unsafe-trait-vs-unsafe-method`

### unsafe-trait-vs-unsafe-method--p1 — Unsafe consuming fn

Summary: Correctness here must be enforced either by marking the trait itself unsafe, or by leaving the consuming accessor method unsafe, since the implementer can't otherwise be trusted; the design that shipped trusts the derive macro to build a valid accessor and puts the unsafe contract on the consuming method instead of the trait.

Summary source: run-b, higher share of the Claims' quoted words (0.38 vs 0.25).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa07-f003716-c1, a-sa07-f003716-c2

## Question `unstable-feature-gate-vs-wait`

### unstable-feature-gate-vs-wait--ship-gated-unstable — Ship it behind an unstable gate

Summary: New functionality (a `PathSelector` trait and its types; a custom-transport API) ships now, gated behind an unstable flag, explicitly excluded from the stability guarantees and expected to stay unstable for some time — even past a 1.0 release.

Summary source: run-b, higher share of the Claims' quoted words (0.42 vs 0.38).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR10-f004423-c2, b-sR10-f004741-c2

## Question `unstable-marking-of-required-macros`

### unstable-marking-of-required-macros--p1 — Needs to stay usable

Summary: `entry` quite obviously needs to be stable — if you can't write `main`, how would you use the crate at all?

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: fact (majority; votes tradeoff / fact / fact)

Claims: b-sb08-f002517-c4

## Question `verify-crates-io-against-source`

### verify-crates-io-against-source--p1 — Verify and publish raw

Summary: Built a comparator between crates.io tarballs and their git repositories across nearly all of crates.io, and released the raw dataset rather than holding it back, because there wasn't time to review it all first.

Summary source: run-b, tie on share of the Claims' quoted words (0.42), shorter summary.

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: a-sR14-f005287-c1

## Question `view-macro-native-control-flow`

### view-macro-native-control-flow--p1 — Add native `for`-loop syntax to `html!` alongside the existing iterator-adapter style, because it's "more natural."

Summary: You can now use for-loops directly in the `html!` macro, alongside the existing iterator-adapter form, making iteration more natural.

Summary source: run-b, higher share of the Claims' quoted words (0.50 vs 0.30).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sR09-f003938-c1

## Question `warn-missing-edition`

### warn-missing-edition--p1 — Support warn on missing edition

Summary: rustc ought to warn whenever it is invoked without an `--edition`, since almost nobody writing a rustc invocation today should be using the 2015 edition. Implemented as an undismissable "note" rather than a lint specifically so `forbid`/`deny(warnings)` setups used by build probes aren't broken by it; the only people affected are those explicitly comparing textual compiler output in scripts.

Summary source: run-b, higher share of the Claims' quoted words (0.92 vs 0.38).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa19-f009343-c1, a-sa19-f009343-c2

## Question `wasi-path-workaround-vs-breaking-fix`

### wasi-path-workaround-vs-breaking-fix--p1 — Pragmatic workaround preferred

Summary: A prior workaround wasn't an ideal fix, but perfect shouldn't be the enemy of functional — it's still worth shipping since it makes real-world extensions work now, packaged as a community Windows build.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.83).

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: b-sb07-f002307-c1

### wasi-path-workaround-vs-breaking-fix--p2 — Correct breaking fix preferred

Summary: The proper fix is the extension-API change, and even though it's a breaking change, compatibility should be handled by shipping a new extension-API version rather than settling permanently for the older workaround.

Summary source: run-b, tie on share of the Claims' quoted words (0.12), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb07-f002307-c2

## Question `wasip2-std-minimal-imports`

### wasip2-std-minimal-imports--p1 — Minimal imports

Summary: Using a simple std facility like `format!` makes the compiled component import the whole `wasi:cli` world, including interfaces that are useless in this case (such as `wasi:cli/env`) — filed as an issue that's still open.

Summary source: run-b, higher share of the Claims' quoted words (0.60 vs 0.50).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sT12-f008237-c2

## Question `wasm-allocator-choice`

### wasm-allocator-choice--p1 — Switch to wee_alloc

Summary: wee_alloc is designed for situations where you need some kind of allocator but not a particularly fast one, and happily trades allocation speed for smaller code size — the default allocator costs roughly 10KB, and wee_alloc saves most of that.

Summary source: run-b, higher share of the Claims' quoted words (0.93 vs 0.33).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB02-f000256-c11

### wasm-allocator-choice--p2 — Eliminate-allocation/no_std

Summary: For a single-instance program, exporting operations on a static mut global with double-buffering removes all dynamic allocation, allowing a `#![no_std]` crate with no allocator dependency at all, for maximum size reduction.

Summary source: run-a, tie on share of the Claims' quoted words (0.55), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sB02-f000256-c12

### wasm-allocator-choice--p3 — Swap the default dlmalloc-derived allocator for wee_alloc (or drop dynamic allocation) when code size outweighs allocation speed

Summary: The choice is explicitly a speed-for-size trade: the default allocator's ~10KB footprint is the cost of keeping it, and wee_alloc's slower allocation is the cost of switching.

Summary source: run-b, tie on share of the Claims' quoted words (0.40), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-bk02-f000256-c11

## Question `wasm-bindgen-manual-vs-generated-glue`

### wasm-bindgen-manual-vs-generated-glue--p1 — Lean into bindgen glue

Summary: A fair amount of code online prefers manual conversions with js_sys — a reasonable strategy, but found to be time-consuming and brittle in practice; leaning into bindgen's generated glue, and accepting its naming/wrapper conventions, buys better compile-time feedback.

Summary source: run-b, higher share of the Claims' quoted words (0.87 vs 0.47).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb19-f005691-c1

## Question `wasm-boundary-serde-vs-getters`

### wasm-boundary-serde-vs-getters--p1 — Choose serde-wasm-bindgen vs wasm-bindgen getters based on hot/cold path

Summary: After surveying GitHub crates, found people mostly doing the right thing already: using serde-wasm-bindgen (more ergonomic, more allocation) for cold paths like config initialization, and wasm-bindgen getters/reflection (faster, less ergonomic) for hot paths where needed.

Summary source: run-a, higher share of the Claims' quoted words (0.89 vs 0.84).

Tag: tradeoff (majority; votes fact / tradeoff / tradeoff)

Claims: a-sa26-f011460-c3

## Question `wasm-bundler-choice`

### wasm-bundler-choice--p1 — Webpack(chosen, "for convenience")

Summary: webpack is not required for working with Rust and WebAssembly — it's just the bundler and development server chosen for convenience here; Parcel and Rollup also support wasm as ES modules, and using Rust+wasm with no bundler at all is viable too.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.45).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sB02-f000256-c17

## Question `wasm-capabilities-explicit-vs-ambient`

### wasm-capabilities-explicit-vs-ambient--p1 — Middleware components get no ambient authority; every capability a middleware needs (e.g. an outbound host) must be explicitly listed in the trigger's inherit_configuration, exactly like any other component dependency

Summary: An auth middleware can reach an endpoint only because the underlying component grants that capability and the trigger explicitly inherits it; middleware gets no ambient authority otherwise.

Summary source: run-a, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR11-f005050-c1

## Question `wasm-components-for-interop`

### wasm-components-for-interop--wasm-components — Wasm components

Summary: SDK-based tool calling couples tool instances to the calling application's runtime and can't be reused externally — a layer of indirection between models and their tools is needed, and composing independently-built WebAssembly components, regardless of source language, solves discovery, portability and sandboxing better. The foundation of software interop is still legacy C ABIs, which are fragile and dangerous; composing through compatible WIT interfaces relieves that pain.

Summary source: run-b, higher share of the Claims' quoted words (0.86 vs 0.52).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sT12-f008237-c1, a-sa07-f003922-c1

## Question `wasm-core-sum-types`

### wasm-core-sum-types--p1 — Primitive sum types worthwhile

Summary: The most immediate benefit first-class sum types would give over shoe-horning sum types into struct subtypes is a `br_table`-like instruction for exhaustively matching on cases — easier to optimize than a chain of `br_on_cast` checks, and lets tools like binaryen reason over a closed case set.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.53).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa05-f003074-c4

### wasm-core-sum-types--p2 — Marginal benefit over encoding

Summary: A custom type descriptor can already store an integer tag for `br_table` dispatch without wasting per-variant space, so primitive sum types would mainly save the trailing cast check — which would require adding a case construct to Wasm, quite a bit of machinery for not a hell lot of relevant generic optimizations.

Summary source: run-b, higher share of the Claims' quoted words (0.75 vs 0.25).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa05-f003074-c5

## Question `wasm-instantiate-streaming-vs-bytes`

### wasm-instantiate-streaming-vs-bytes--p1 — Drop the streaming wrapper when the bytes are already in hand; it buys nothing there

Summary: There's no need for the complex wrapping into a `Response` — `instantiateStreaming` doesn't have any benefits when the whole file is already loaded as a blob; revert to the regular `instantiate`, which can take the bytes directly.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.89).

Tag: fact (agree; votes fact / fact / -)

Claims: b-sR09-f003815-c1

## Question `wasm-monolithic-vs-small-components`

### wasm-monolithic-vs-small-components--p1 — Self-contained pieces of application logic (e.g. a classifier) should be split into their own Wasm component, composed into the app via a WIT interface and a declared spin.toml dependency, rather than living inline in the HTTP-triggered component

Summary: Decoupling the core classification logic into its own Wasm component kept the HTTP control flow lean, standard, and easy to maintain, with the WIT files serving as the single source of truth for the boundary.

Summary source: run-a, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR11-f005053-c1

## Question `wasm-panic-hook`

### wasm-panic-hook--p1 — Install panic hook

Summary: Rather than getting cryptic, difficult-to-debug `RuntimeError: unreachable executed` messages, installing `console_error_panic_hook` gives Rust's actual formatted panic message in the console.

Summary source: run-b, higher share of the Claims' quoted words (0.93 vs 0.67).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sB02-f000256-c16

## Question `wasm-panic-unwind-vs-abort`

### wasm-panic-unwind-vs-abort--p1 — Panic unwind for reliability

Summary: To recover from panics without discarding instance state, panic=unwind support for wasm32-unknown-unknown was added to wasm-bindgen via the WebAssembly Exception Handling proposal, because panic=abort's default full-reinitialization recovery wipes in-memory state for stateful workloads like Durable Objects.

Summary source: run-b, higher share of the Claims' quoted words (0.93 vs 0.71).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-sa12-f004598-c1

## Question `wasm-precise-traps-store-tearing`

### wasm-precise-traps-store-tearing--p1 — Load before store opt in

Summary: Implements precise store-trap semantics by prepending a same-size load before every store on architectures with store tearing, so a trapping store traps via the load first; shipped on by default, accepting a measured ~2% cost on one benchmarked chip pending Wasm spec clarification.

Summary source: run-a, higher share of the Claims' quoted words (0.62 vs 0.54).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: a-02-f001181-c1

## Question `wasm-runtime-swap-vs-host-target`

### wasm-runtime-swap-vs-host-target--p1 — The two Wasm targets warrant different answers — swap out tokio for a browser shim when targeting `wasm32-unknown-unknown`, but for `wasm32-wasip2/3` compile most of the stack unchanged and depend on tokio gaining support for that platform instead

Summary: The two Wasm targets warrant different answers: swap out tokio for a browser shim (wasm-bindgen-futures) when targeting `wasm32-unknown-unknown`, but for `wasm32-wasip2/3` compile most of the stack unchanged and depend on tokio gaining support for that platform, including UDP/TCP sockets, instead.

Summary source: run-b, higher share of the Claims' quoted words (0.62 vs 0.52).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sR05-f002177-c1

## Question `wasm-undefined-symbols-error`

### wasm-undefined-symbols-error--p1 — Remove --allow-undefined as the wasm-target default; undefined symbols should error at build time like on native platforms

Summary: All native platforms consider undefined symbols an error by default, so passing `--allow-undefined` introduces surprising behavior specific to WebAssembly targets that kicks a mistake down the road to a confusing runtime failure; removing it as the default aligns wasm with how every other platform already behaves, and existing intentional users can opt back in per-symbol.

Summary source: run-b, higher share of the Claims' quoted words (0.81 vs 0.38).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb23-f009737-c1

## Question `web-framework-actor-vs-tower`

### web-framework-actor-vs-tower--p1 — Actix-default for web, Clap for CLI

Summary: Default students to Clap for CLI and Actix for web, unless they have a compelling reason to switch to a new framework.

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: a-sB01-f000149-c2

### web-framework-actor-vs-tower--p2 — Axum's Tower-based design is often preferred over Actix Web's actor model

Summary: Actix Web uses the actor model and has its own mature middleware system; both frameworks are fast and production-ready, but Axum's design philosophy is often preferred for its simplicity and tight integration with Tokio.

Summary source: run-b, higher share of the Claims' quoted words (1.00 vs 0.95).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa26-f011605-c2

## Question `web-framework-macro-free-api`

### web-framework-macro-free-api--p1 — Macro-free API design is a distinguishing strength

Summary: What makes Axum stand out in the Rust framework landscape is its macro-free API design, its predictable error-handling model, and its own middleware system built on Tower.

Summary source: run-b, higher share of the Claims' quoted words (0.94 vs 0.82).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa26-f011605-c1

## Question `web-session-store-default`

### web-session-store-default--p1 — Cookie store default with encryption

Summary: Following Rails' precedent, new apps should start by storing sessions inside the cookie, both encrypted and signed, switchable later via `tower-sessions` — Rails itself calls the choice "controversial," but it keeps initial friction low.

Summary source: run-b, higher share of the Claims' quoted words (0.56 vs 0.22).

Tag: tradeoff (agree; votes tradeoff / tradeoff / -)

Claims: b-sb04-f001365-c1

### web-session-store-default--p2 — Server side store preferred

Summary: There's no way to force-invalidate a session or change permissions on the fly when the data lives on the client, so whatever effort is saved by skipping a server-side store is negated by that inflexibility; encrypted cookies also aren't good practice in production since they can enable replay attacks and similar vulnerabilities — storing sensitive data server-side is always the better choice.

Summary source: run-b, higher share of the Claims' quoted words (0.75 vs 0.56).

Tag: tradeoff (majority; votes tradeoff / fact / tradeoff)

Claims: b-sb04-f001365-c2, b-sb04-f001365-c3

## Question `web-wasm-target-workaround-vs-target`

### web-wasm-target-workaround-vs-target--p1 — Pursue a real Web-WASM target instead of another workaround

Summary: The root cause is the lack of a way to signal wasm-bindgen usage to the compiler — shouldn't there finally be a discussion of a proper `wasm32-web`/`wasm32-bindgen` target instead, now that the project has active maintainers again, to fix this class of problem generally?

Summary source: run-b, higher share of the Claims' quoted words (0.88 vs 0.38).

Tag: tradeoff (majority; votes taste / tradeoff / tradeoff)

Claims: a-sa06-f003558-c1

### web-wasm-target-workaround-vs-target--p2 — Ship the workaround now, a new target isn't realistic soon

Summary: Says there has been zero progress on a proper Web-WASM target in about four years and holds no hope of getting one anytime soon, so the immediate need is a solution that works with current stable Rust and the declared MSRV.

Summary source: run-a, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: tradeoff (majority; votes fact / tradeoff / tradeoff)

Claims: a-sa06-f003558-c2

## Question `what-counts-as-semver-breaking`

### what-counts-as-semver-breaking--p1 — Enum variant addition breaks without non exhaustive

Summary: Adding a variant to a public enum that is not marked `#[non_exhaustive]` is breaking, because downstream match expressions that were previously exhaustive stop compiling.

Summary source: run-b, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: b-bk03-f000267-c12

### what-counts-as-semver-breaking--p2 — Dependency type leakage forces lockstep major bump

Summary: A dependency bump forces a major-version bump of the crate itself when the dependency's own semver-incompatible change exposes types that appear in the crate's public API, since two incompatible versions of the same crate can't unify for downstream consumers; a purely internal dependency needs no changelog entry at all.

Summary source: run-a, tie on share of the Claims' quoted words (0.25), shorter summary.

Tag: fact (agree; votes fact / fact / -)

Claims: b-bk03-f000267-c13

### what-counts-as-semver-breaking--p3 — Msrv bump is breaking

Summary: An MSRV bump is itself classified as a breaking change for the crate, not a minor or patch-level change.

Summary source: run-a, higher share of the Claims' quoted words (1.00 vs 0.60).

Tag: fact (agree; votes fact / fact / -)

Claims: b-bk03-f000267-c14

## Question `wit-dependency-keyword-design`

### wit-dependency-keyword-design--p1 — Favors the single `dependency` keyword with locked/unlocked inferred from the trailing syntax, for regularity and to keep vocabulary aligned with how package managers already use the word "dependency."

Summary: What if just the word "dependency" were used, and "locked" vs. "unlocked"/"range" were inferred from the syntax after the `@` — the word "dependency" is already used by package managers and their build-config files (npm/package.json, cargo/Cargo.toml) to exclusively refer to implementations, so this keeps vocabulary aligned and regular.

Summary source: run-b, higher share of the Claims' quoted words (0.95 vs 0.50).

Tag: taste (agree; votes taste / taste / -)

Claims: b-sR05-f001983-c1

## Question `wit-export-direct-vs-interface`

### wit-export-direct-vs-interface--p1 — Wrap related functions inside a named interface and export the interface, rather than exporting a raw function from the world

Summary: While a world can export a bare function directly, the recommended best practice is to wrap related functions inside a named interface which the world then exports, since this is more modular, extensible, and matches how WIT is used in real multi-function components.

Summary source: run-a, tie on share of the Claims' quoted words (1.00), shorter summary.

Tag: taste (agree; votes taste / taste / -)

Claims: a-sR08-f003033-c1

## Question `work-stealing-vs-thread-per-core`

### work-stealing-vs-thread-per-core--p1 — Choice is workload dependent not universally faster

Summary: Across 360 benchmarked configurations spanning balanced/unbalanced and low-to-high-scale, CPU- through IO-heavy HTTP/2 workloads, io_uring (Glommio) didn't strictly outperform epoll-based runtimes even under a "noisy neighbor" scenario designed to favor work-stealing, and tokio's work-stealing configuration showed unexplained throughput anomalies at 8/12 threads. The choice between executor-per-thread and work-stealing isn't a simple matter of "which is faster" but which architecture best aligns with the application's own logic.

Summary source: run-b, higher share of the Claims' quoted words (0.67 vs 0.33).

Tag: fact (agree; votes fact / fact / -)

Claims: a-sa18-f009026-c1

## Question `wrap-third-party-types-in-public-api`

### wrap-third-party-types-in-public-api--controlled-type — Expose a type the crate controls (a std collection, a local newtype)

Summary: A hook exposing browser search params should return a `HashMap<String, String>` rather than the raw `UrlSearchParams` handle. Because the language has no standard u256 type, one of several third-party crate implementations is chosen but not exposed directly — it's wrapped behind a local named type, so the underlying crate choice stays swappable.

Summary source: run-a, tie on share of the Claims' quoted words (0.62), shorter summary.

Tag: tradeoff (majority (merged position; each run's sources carry taste/tradeoff); votes taste/tradeoff / taste/tradeoff / tradeoff)

Claims: a-sR07-f002271-c1, b-bk03-f000267-c17

## Question `xcframework-tooling-vs-hand-built`

### xcframework-tooling-vs-hand-built--p1 — Use Apple's official `xcodebuild -create-xcframework` rather than hand-assembling the XCFramework directory

Summary: XCFramework's on-disk structure is simple enough that some teams build it by hand, but chose to stick to Apple's official `xcodebuild -create-xcframework` tooling to combine the per-target static libraries, headers and module map instead of replicating that structure manually.

Summary source: run-a, higher share of the Claims' quoted words (0.73 vs 0.64).

Tag: taste (agree; votes taste / taste / -)

Claims: a-sa27-f012237-c2
