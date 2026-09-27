# Blind fill A — summaries, batch 1, file 01

### absolute-instant-periodic-timing--p1
Summary: In a periodic async loop, each wait should be computed as a stored absolute instant advanced by a fixed period (e.g. `previous + 1000`), then awaited with `delay_until`, rather than recomputed as "now + period" each iteration; the loop's own work time doesn't get added back in, so timing doesn't drift over many iterations.
Tag: tradeoff
Claims: a-sB04-f000227-c2

### actor-vs-shared-locks--p1
Summary: An actor layer for connection management can be unnecessary overhead; removing it in favor of higher-order shared data structures simplifies the architecture, even if it later needs a follow-up fix for a deadlock introduced by the change.
Tag: tradeoff
Claims: b-sT05-f002550-c2

### ad-hoc-special-case-vs-general-mechanism--p1
Summary: Adding another special-cased mechanism on top of an already-unfortunate special case ("can of worms") should be resisted; the right move is to think through a better long-term, general solution before merging.
Tag: tradeoff
Claims: b-sb09-f003052-c1

### ad-hoc-special-case-vs-general-mechanism--p2
Summary: Given a separate, more general refactor is already in flight elsewhere, it's reasonable to merge the current special case as-is now and rebase/refactor onto the general mechanism once that other work lands, rather than blocking this PR on an inline redesign.
Tag: tradeoff
Claims: b-sb09-f003052-c2, b-sb09-f003052-c3

### additive-features--p1
Summary: A feature flag like `std` should never be required just to build the crate on ordinary targets (e.g. Linux/Windows); if disabling a feature breaks the build, that defeats the purpose of feature gating and the accompanying CI changes shouldn't have been necessary in the first place.
Tag: tradeoff
Claims: b-sb10-f003186-c1

### additive-features--p2
Summary: A fix can intentionally disable standard-library-dependent features for dependents that build with `default-features = false`, accepting that this changes what builds successfully under that configuration.
Tag: tradeoff
Claims: b-sb10-f003186-c2

### affine-types-vs-formal-verification--p1
Summary: Rust's affine types do not offer the same guarantees as linear types combined with dependent types; the type system alone is weaker than what those stronger formal systems would provide.
Tag: fact
Claims: b-sb19-f005743-c4

### affine-types-vs-formal-verification--p2
Summary: Formal-verification tooling — model checkers like Frama-C, including a Rust port from TrustInSoft — can be integrated alongside Rust's type system rather than treated as a replacement for it; the two are not mutually exclusive.
Tag: tradeoff
Claims: b-sb19-f005743-c5, b-sb19-f005743-c6

### ai-agents-and-explicit-syntax--p1
Summary: Coding agents change the calculus for verbose, explicit call-site syntax like named arguments: once a human isn't the one typing the call, the clarity benefit at the call site outweighs the typing cost, and the clarity gain may be larger for an agent reading the call than for a human — though no real evals have been run to confirm this.
Tag: tradeoff
Claims: a-sa18-f009104-c3

### ai-authored-community-contributions--reject-ai-authored-content
Summary: AI-generated content in community-facing material is unwanted on its own terms: a newsletter survey found readers explicitly do not want anything AI-generated in it, and separately, a proposal that reads as heavily LLM-composed and steered toward a predetermined conclusion draws direct criticism for how it comes across.
Tag: taste
Claims: b-sb20-f007942-c1, a-sa29-f013224-c4

### ai-authored-community-contributions--acceptable-if-substance-is-own
Summary: Using an LLM to compose a contribution is fine as long as the substance — the points, the logic, the trade-offs — is the contributor's own; what matters is the quality of the result and the contributor's understanding of it, not whether AI was involved in producing the prose.
Tag: taste
Claims: a-sa29-f013224-c5, b-bk03-f000267-c6

### ai-authored-community-contributions--acceptable-if-marked
Summary: Assistance from AI tools is not itself a problem; clearly marked AI-generated content generally isn't going to cause trouble under forum rules aimed at unmarked, low-effort AI spam.
Tag: taste
Claims: a-sa29-f013224-c6

### ai-authored-community-contributions--human-must-stay-accountable
Summary: A contribution that reads as AI-generated is acceptable only if the human author stays personally in the loop on all communication about it, since they own the change and are responsible for it.
Tag: taste
Claims: b-sb15-f004721-c1

### ai-authored-community-contributions--manage-through-review-not-ban
Summary: A strict no-AI ban solves some problems but creates others — toxic witch hunts over suspected AI use, incentives to lie to maintainers, and an enforcement burden that's close to impossible — so projects are moving toward managing AI-generated proposals through review and policy instead of a blanket ban, treating the volume of low-quality AI submissions as a manageable, ongoing cost rather than a reason to prohibit them outright.
Tag: tradeoff
Claims: b-sR11-f004993-c1, b-sR13-f009740-c1

### ai-review-suggestions--p1
Summary: An AI code-review tool's suggestions shouldn't be followed by default; a suggestion can be noise (e.g. flagging a harmless reference as a problem) while missing the actual bug that needs fixing, so a practitioner's own judgment stays the deciding factor.
Tag: tradeoff
Claims: b-sR08-f003550-c1

### all-rust-vs-platform-native-tooling--all-rust
Summary: The glue and test code at the platform boundary can be written entirely in Rust — JNI functions following the `Java_<package>_<class>_<method>` convention with no C++ intermediary, native Objective-C calls via `objc2` instead of writing objc, and pure-Rust `wasm-bindgen-test` E2E harnesses — specifically to avoid adding non-Rust dependencies like C++, Playwright, Cypress or Selenium to the pipeline.
Tag: tradeoff
Claims: b-sb22-f008914-c1, b-sb13-f004367-c1, a-sT12-f008455-c1

### all-rust-vs-platform-native-tooling--all-rust-workable-not-production
Summary: An all-Rust setup for a platform-native test harness (bundling the app and a `#![no_main]` XCTest bundle built from objc2 bindings) works and lets you drive UI automation and coverage without opening Xcode, but exit-status detection is unreliable, on-device behavior is unclear, and the whole thing is brittle enough that the author wouldn't suggest it in production, preferring a Makefile/CLI workflow over `xcodebuild` day to day regardless.
Tag: tradeoff
Claims: b-sb21-f008793-c1

### all-rust-vs-platform-native-tooling--platform-native-glue
Summary: Writing the platform-boundary layer (e.g. the JNI side) in the platform's own language, like C++ on Android, lets that platform's native tooling — code generation, build automation, code analysis, jump-to-declaration in Android Studio — work across the boundary, at the cost of introducing one extra language into the project.
Tag: tradeoff
Claims: b-sb20-f007678-c1

### api-handler-as-async-trait--p1
Summary: Defining an HTTP API's handlers via an async trait decoupled from any concrete implementation lets tooling extract API/schema information without needing a real implementation to be compiled, or even present at all; the hope is that more Rust projects adopt this pattern generally.
Tag: tradeoff
Claims: a-sa14-f005454-c3

### api-schema-spec-first-vs-code-first--p1
Summary: Don't hand-write the OpenAPI spec and rely on a programmer to keep it current; have the API server generate the spec from its own code instead, so code is the source of truth and the generated spec provably cannot diverge from the implementation that produced it.
Tag: tradeoff
Claims: a-sa23-f011186-c1, a-sa14-f005454-c1

### async-by-default-host-interfaces--p1
Summary: WASIp3's async I/O model, previously experimental and opt-in, is now the default platform for new applications, and a framework's own host interfaces (KV, SQLite, Postgres, Redis, outbound HTTP) get rewritten to be async so that I/O-heavy handlers get real concurrency instead of blocking the instance.
Tag: tradeoff
Claims: b-sR10-f004809-c1

### async-drop-raii-vs-close--explicit-close-required
Summary: Without reliable async `Drop`, an async resource should require an explicit async close — an endpoint no longer attempts to gracefully close connections when merely dropped; callers must `await` `close()` themselves before dropping the last instance, and that explicit close path is made cheap (near-instant when the peer already closed, about one RTT otherwise) so it functions as the primary, first-class shutdown mechanism.
Tag: tradeoff
Claims: b-sR10-f004423-c1, b-sR10-f004741-c1

### async-drop-raii-vs-close--preserve-raii-with-workarounds
Summary: RAII shouldn't be given up on for async resources; an async shutdown function can offer a gentle, explicit path, but every entity should still attempt cleanup on `Drop` as well, so cleanup isn't solely dependent on callers remembering to call close.
Tag: tradeoff
Claims: b-sb17-f005159-c2

### async-fn-in-traits-cost--p1
Summary: Using `async fn` in traits (via the `async-trait` crate or async-fn-in-trait) costs a heap allocation per call, but that cost is not significant for the vast majority of applications; it should only be weighed carefully when exposing the pattern in the public API of a low-level function expected to be called millions of times a second.
Tag: tradeoff
Claims: b-bk01-f000233-c14

### async-for-cpu-bound-work--p1
Summary: The common claim that async Rust (Tokio) should simply never be used for CPU-intensive work is an over-simplification; the real constraint is that mixing IO-bound/latency-sensitive tasks with CPU-bound/long-running tasks on the same runtime needs special handling, not blanket avoidance of async.
Tag: tradeoff
Claims: b-bk01-f000233-c6

### async-hook-cancellation-upfront--p1
Summary: An initial async-computation hook API should ship without committing to cancellation semantics upfront, since the library isn't stable yet and the minimal API likely covers most use cases already; cancellation support can be added later, as a variant, once real usage demonstrates an actual need.
Tag: tradeoff
Claims: a-02-f000957-c1

### async-io-with-sync-storage--p1
Summary: Pairing an async I/O library (e.g. quinn for QUIC) with a storage layer that only offers a synchronous API is an avoidable, foreseeable architecture mismatch; the right response is to have looked for a different, more compatible dependency rather than accepting the pairing.
Tag: tradeoff
Claims: b-sb18-f005307-c1

### async-io-with-sync-storage--p2
Summary: Sync-only storage isn't a foreseeable design error to avoid — every in-process embedded database evaluated (rocksdb, redb, sled, sqlite) exposes a synchronous API, so there is no viable async-native alternative to switch to, and non-`Send` futures are often unavoidable once a future has to capture a non-`Send` database or transaction handle.
Tag: tradeoff
Claims: b-sb18-f005307-c2

### async-rust-production-ready--p1
Summary: Stable async Rust is reliable and performant, and is used in production in some of the most demanding situations at the largest tech companies; the rough edges that remain are in ergonomics — async iterators/streams, async in traits, async destruction — not in reliability itself.
Tag: fact
Claims: b-sR01-f000233-c2

### async-transport-asyncread-vs-sink-stream--p1
Summary: A custom async transport abstraction that must work across several carriers should be built against `AsyncRead`/`AsyncWrite`, not `Sink`/`Stream`, because available OSS WebSocket-over-async libraries built on `Sink`/`Stream` didn't jointly satisfy `Send`, `Sync` and `Unpin` together; writing a translation layer to keep the handler generic over `AsyncRead`/`AsyncWrite` avoided that combinatorial trait problem entirely.
Tag: tradeoff
Claims: a-sa03-f002236-c1

### async-vs-threads--p1
Summary: Without async/await, a programmer has to manually split a task into sub-tasks and track its state by hand; async/await brings "improved ergonomics" by having the compiler build that state-progression mechanism automatically via Futures instead.
Tag: tradeoff
Claims: a-sB01-f000227-c3

### async-vs-threads--async-tasks-on-embedded
Summary: On embedded targets, async/await's ergonomics gain is compatible with strict resource requirements too: the compiler forbids awaiting while holding a resource (preserving priority-ceiling-style guarantees), and compile-time-generated static executors avoid dynamic allocation altogether, so there's no risk of an out-of-memory panic the way a heap-allocating task model would have.
Tag: tradeoff
Claims: a-sR01-f000227-c2

### async-vs-threads--p2
Summary: Asynchronous programming is "not better than threads, but different": OS threads need no new programming model, let existing synchronous code run unchanged, and support OS-level thread-priority tuning, but carry real per-thread CPU/memory overhead; async supports orders of magnitude more concurrent tasks for the same overhead, especially for IO-bound work like servers and databases, and — being zero-cost with no required heap allocation or dynamic dispatch — can run in constrained environments like embedded systems, at the cost of larger compiled binaries and a bundled runtime; use threads if you don't need async's performance benefits.
Tag: tradeoff
Claims: b-bk01-f000233-c11

### async-vs-threads--async-for-io-wait-and-no-os
Summary: Async programming is a good fit for systems that need to handle very many concurrent tasks where those tasks spend a lot of their time waiting (e.g. on client responses or other IO), and it also fits microcontrollers with very limited memory that have no OS-provided threads to fall back on.
Tag: tradeoff
Claims: b-sR01-f000233-c1

### aya-vs-libbpf-rs--p1
Summary: Between a pure-Rust eBPF toolchain (Aya, no libbpf/BCC/kernel-header dependency, experimental CO-RE) and a Rust wrapper around the native C `libbpf` library with the eBPF program itself written in C and CO-RE support by default (libbpf-rs), the choice for a given set of examples came down to familiarity rather than any specific technical reason to prefer one over the other.
Tag: taste
Claims: b-sb24-f011306-c2

### batch-crypto-verification--p1
Summary: CPU-bound cryptographic verification (signatures, proofs, scripts) should be automatically and transparently batched across contemporaneous requests rather than verified one at a time, because serial, one-at-a-time verification is too slow during an operation like initial chain sync; batching lets data dependencies be deferred and the work parallelized.
Tag: tradeoff
Claims: b-bk03-f000267-c5

### batteries-included-web-framework--batteries-included
Summary: Rust's existing minimalist web/backend frameworks and SPA frameworks each still require substantial manual wiring — routing, templates, auth, database access, admin — across separate libraries; the ecosystem instead needs a single, integrated, batteries-included framework that handles it all with clean upgrade paths between versions, in the spirit of Rails/Django/Spring.
Tag: taste
Claims: b-sb19-f005872-c1

### become-tail-call-codegen--alt1
Summary: The nightly `become` tail-call feature's codegen quality is target-dependent: on ARM64 (M1) the tail-call interpreter beats both the plain VM and hand-written ARM64 assembly, but on x86-64 it beats the VM while still losing to hand-written assembly, and compiled to WASM it runs 1.2–4.6x slower than the plain VM across Firefox, Chrome and wasmtime, attributed to codegen (register spills to the stack) not translating well to the WASM stack machine.
Tag: fact
Claims: a-sa15-f005821-c1

### behavioral-equivalence-testing-method--p1
Summary: Unit tests and integration tests are insufficient for verifying that a rewritten system preserves an emergent, hard-to-specify behavior like a physics-engine exploit, because the divergence only shows up late in long play sessions, no single fixed tolerance works everywhere, and one integration test's passing result can't be extrapolated to the whole game.
Tag: fact
Claims: a-sa21-f011069-c1

### behavioral-equivalence-testing-method--p2
Summary: Naive property-based (fuzzing) testing is also insufficient on its own for this kind of verification: the relevant input space (key holds, frame counts, continuous mouse movement) grows exponentially, and pure random search generates inputs "a human would not even be capable of producing," producing many false negatives against the goal of preserving a human-discoverable exploit.
Tag: fact
Claims: a-sa21-f011069-c2

### behavioral-equivalence-testing-method--p3
Summary: The right approach is a heuristic-constrained, Markov-process-style reinforcement-learning search biased toward human-plausible inputs, treating "the exploit stays reachable within human-plausible effort" as the correctness criterion instead of exact input/output matching.
Tag: fact
Claims: a-sa21-f011069-c3

### benchmark-colocation-with-crate--p1
Summary: When a function moves to a different crate in a multi-crate workspace, its benchmark should move with it into the crate that now defines the function; use `git mv` on the move to preserve the file's history.
Tag: taste
Claims: a-sR04-f001096-c2

### bitflags-vs-generated-variants--p1
Summary: Combinatorial pipeline state is better represented as bitflags than as an explicit bool-per-combination approach: bit flags take a lot less space and are arguably clearer when using named constants, such as those the bitflag crate offers.
Tag: tradeoff
Claims: b-sb01-f000493-c1

### bitflags-vs-generated-variants--p2
Summary: The two approaches are mostly equivalent in principle, but at a larger combination count (32 versus a prior case of 6) hand-enumerating every combination becomes too daunting, which is the specific reason to generate the array of variants in code instead.
Tag: tradeoff
Claims: b-sb01-f000493-c2

### blocking-work-in-async--p1
Summary: CPU-bound or blocking work should be matched to the right mechanism rather than handled uniformly: use `spawn_blocking` for blocking IO, use `std::thread::spawn` (not a thread-pool slot) for a thread that will run forever, and use a dedicated thread pool (e.g. Rayon) or a second async runtime for sustained CPU-bound work — accepting a dedicated thread or `spawn_blocking` as an easy-but-suboptimal choice when performance needs are modest.
Tag: tradeoff
Claims: b-bk01-f000233-c7

### borrowck-self-referential-structs--p1
Summary: A subset of self-referential structs — ones that only borrow from a heap allocation owned by a sibling field, without mutating it — could be proven safe by a smarter borrow checker, without needing `Pin`; this is wanted because the need for it comes up regularly.
Tag: tradeoff
Claims: b-sb19-f007207-c3

### borrowed-build-state-vs-builder--p1
Summary: Relying on a lifetime-bound reference into shared build state (e.g. via a field like `_graph_data`) is a lifetime hack; the better design is a builder that consumes the build state into an immutable, owned structure so downstream code can reference the tensor store directly without lifetime entanglement.
Tag: tradeoff
Claims: a-sa07-f003704-c4

### bounded-grid-universe--p2
Summary: Of the three ways to bound an in-principle-infinite simulation grid in finite memory — unbounded expansion (risks unbounded slowdown or running out of memory), fixed non-periodic edges (kills patterns that reach the boundary, like gliders), and a fixed-size periodic (toroidal, wraparound) universe — the periodic option is chosen because it lets patterns keep running forever without either problem.
Tag: tradeoff
Claims: b-bk02-f000256-c1, a-sB02-f000256-c2

---
Notification: Filled positions-01.csv (58 claim rows) and summaries-01.md (48 positions) for input-b1-01.md, covering questions from `absolute-instant-periodic-timing` through `bounded-grid-universe`. Three low-confidence calls are flagged: `api-schema-spec-first-vs-code-first` and `bounded-grid-universe` each list two positions that read as near-duplicates of each other, and `become-tail-call-codegen`'s single claim evidences both listed positions depending on target architecture. All other claim-to-position assignments are high confidence, judged from quote and paraphrase alone without opening any source.
