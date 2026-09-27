# Fill A — summaries, file 12

## Question `sound-lifetime-erasure-in-callbacks`

### sound-lifetime-erasure-in-callbacks--p1
Casting away a reference's lifetime to store it for a later callback is unsound — there might be an aliased mutable reference, and the API providing the reference gives no real outlives guarantee; the fix is a thread-local holding a raw pointer only for the duration of the call that needs it, still `unsafe` but much easier to reason about.
tag: tradeoff
claims: b-sR04-f001749-c1

## Question `spawn-vs-compose-futures`

### spawn-vs-compose-futures--p1
When parallelism is wanted, spawning tasks is usually the simpler alternative to `join!`/`select!`: less error-prone, more general, and gives more predictable, fairer scheduling, at the cost of being less structured and harder to reason about for lifecycle and resource management.
tag: tradeoff
claims: b-bk01-f000233-c5

## Question `speculative-from-impls`

### speculative-from-impls--p1
Remove a speculative conversion now, because adding another `From` impl for the same type later would produce a compile error on existing code.
tag: tradeoff
claims: a-sa11-f004265-c2

## Question `spi-hardware-cs-in-spibus`

### spi-hardware-cs-in-spibus--p1
Prefers keeping CS as ordinary GPIO `Output` pins, addressing as many targets as there are available GPIOs, since hardware chip-select complicates the embedded-hal `SpiBus`/`SpiDevice` split and most HALs avoid it for that reason.
tag: taste
claims: a-sa09-f004055-c4, a-sa09-f004055-c3

### spi-hardware-cs-in-spibus--p2
Converges on marker types (`HardwareCs`, `NoCs`) so `SpiBus` is implemented only for the no-hardware-CS variant, following embedded-hal semantics of exclusive bus access, while a separate constructor still exposes hardware CS to callers who want it.
tag: tradeoff
claims: a-sa09-f004055-c5

## Question `stable-contract-api-vs-cli`

### stable-contract-api-vs-cli--p1
The deprecation policy states the Rust APIs of the crates are currently unstable and unsupported; the versioned, stable surface for interacting with the application is the CLI commands and JSON-RPCs, not the Rust library API.
tag: fact
claims: b-bk03-f000267-c10

## Question `state-accessor-and-stream-split`

### state-accessor-and-stream-split--p1
A single primitive tried to serve two very different consumers — "what's the state right now" and "tell me when it changes" — and was replaced by two dedicated primitives, a lifetime-bound borrowed snapshot and a `'static` event stream, each answering one question.
tag: tradeoff
claims: a-sR13-f004685-c1

## Question `static-allocation-in-real-time`

### static-allocation-in-real-time--p1
Dynamic allocation is problematic for resource-constrained real-time systems on both performance and reliability grounds (the runtime panics on out-of-memory), so static allocation is the preferable approach.
tag: tradeoff
claims: a-sB01-f000227-c4

## Question `static-model-security-guarantees`

### static-model-security-guarantees--p1
Even a formally verified RTOS kernel like seL4 only claims integrity/confidentiality/availability for the kernel itself, not the whole system, especially once dynamic allocation enters the picture; a declarative static task/resource model combined with compile-time aliasing, mutability and lifetime guarantees propagates integrity properties across the whole system instead.
tag: tradeoff
claims: a-sB04-f000227-c4

## Question `static-verification-no-panic-mechanism`

### static-verification-no-panic-mechanism--p1
Clippy lints don't recurse into dependencies and only cover hard-coded library types; an effect-type system would require a new language; a link-time hack is optimization-dependent, lacks async support, breaks under `panic = "abort"`/no_std, and is unsafe in library crates; cfg-forking the standard library affects every consumer and breaks tooling. A custom rustc driver running a post-monomorphization pass over resolved function calls was the most accurate approach found, and is what now ships and is certified against.
tag: tradeoff
claims: b-sR12-f005169-c1

## Question `std-mutex-vs-async-mutex`

### std-mutex-vs-async-mutex--p1
Recommends using `std::Mutex` where possible, reserving the async `Mutex` for cases where the lock must be held across an `.await` point or protects an IO resource, since the async version costs more precisely because it supports that.
tag: taste
claims: b-bk01-f000233-c8

## Question `std-naming-convention-imperfect-fit`

### std-naming-convention-imperfect-fit--p1
`raw_parts` works even though there's no matching `into_raw_parts`, and since the crate isn't the standard library, it's fine if the pattern doesn't apply exactly.
tag: taste
claims: b-sR05-f002326-c1

## Question `std-naming-conventions-strictness`

### std-naming-conventions-strictness--strict
The name must match the ownership signature — an `into_`-named method that doesn't consume `self` is wrong and should be renamed; conversely `to_owned` is defended as not a bad name despite an imperfect fit, since the operation is neither pure owning nor pure borrowing, with the Rust API Guidelines cited as the standing rationale for the `to_` prefix.
tag: taste
claims: b-sR08-f003587-c2, b-sb22-f009236-c3, b-sb22-f009236-c2

### std-naming-conventions-strictness--loose
By analogy with `Clone`/`Borrow` (not named `ToCloned`/`AsBorrowed`), the `to_`/`as_`/`into_` prefix convention is unneeded morphology for converting between representations of the same type — preferring a bare verb like `own()` — even while granting the prefix makes sense for genuine cross-type conversions like `IntoIterator`.
tag: taste
claims: b-sb22-f009236-c1

## Question `synthetic-canary-vs-tracing`

### synthetic-canary-vs-tracing--p1
Because no timing information about real source messages may leave the on-premises node, tracing real messages is off the table; instead a "message canary" sends real encrypted messages through the live system once an hour, measuring delivery time and alarming past a threshold.
tag: tradeoff
claims: b-sb24-f011295-c3

## Question `tail-expression-vs-explicit-return`

### tail-expression-vs-explicit-return--p1
Strongly opposed to any bare/last-expression rule on readability grounds, drawing on Rust experience: it seriously hurts readability for both function returns and `if` expressions, most of all when the block is long and the last expression sits far from the assignment.
tag: taste
claims: b-sT02-f000576-c1

### tail-expression-vs-explicit-return--p2
Experience runs the other way: Rust's implicit return of the last expression is much easier to read than `return` statements everywhere.
tag: taste
claims: b-sT02-f000576-c2

## Question `target-tier-without-ci`

### target-tier-without-ci--p1
The tier policy requires Tier 1 platforms to run CI tests; with free macOS x86_64 CI runners ending, the target is demoted to Tier 2 with host tools from the named release — builds still ship, but the target will likely accumulate bugs faster and could be demoted further.
tag: fact
claims: a-sT12-f009704-c1

## Question `teach-rust-in-curricula`

### teach-rust-in-curricula--p1
Modern software education over-focuses on frameworks and abstractions and under-teaches how systems actually work; learning Rust forces students to confront ownership, memory and error handling directly rather than letting a framework abstract them away.
tag: taste
claims: a-sa26-f011443-c1

## Question `test-via-real-entry-point`

### test-via-real-entry-point--p1
Even after a fix, nothing tests the actual gesture: existing tests drive the toggle/switch methods directly rather than the deferred mouse-event path itself, so they'd keep passing even if the real keybinding wiring broke; wants at least one test to dispatch the real action via a keystroke against the real strip.
tag: tradeoff
claims: a-sa13-f004772-c4, a-sa13-f004772-c3

### test-via-real-entry-point--p2
When a refactor moves or replaces consensus-critical code, a check can silently stop being enforced with no test failing and no diff showing a deletion, because the danger is in what the old code used to do that nothing does anymore; the fix is to inventory every rejection the old code could produce, test every parse-time rejection through the actual production entry point (not just the check's own unit tests), and individually audit fallible conversions that could silently turn an invalid value into one treated as benign — citing two real incidents that slipped through with green CI.
tag: tradeoff
claims: b-bk03-f000267-c15

## Question `threads-vs-simd-for-batch-work`

### threads-vs-simd-for-batch-work--p1
SIMD alone is a good choice for a small batch of blobs — decent speedup, stays on one core, doesn't disturb the rest of the program — but for a large batch with the whole machine available, combining SIMD with thread-level parallelism gives peak throughput, measured at 17x over sequential and 2.1x over threads alone.
tag: fact
claims: b-sR08-f003702-c1

## Question `tiered-checked-unchecked-apis`

### tiered-checked-unchecked-apis--p1
Deliberately exposes three ways to build the same row — a positional fast API for best performance, a safe API that validates field names, and an indexed API balancing the two — so callers pick their own safety/performance tradeoff rather than the crate picking one for them.
tag: tradeoff
claims: a-sR16-f012642-c1

## Question `timer-instant-overflow-panic`

### timer-instant-overflow-panic--p2
The correct behavior when a computed wake time is too far out is to never register the future as ready again, not to wait based on a MAX-derived time that undershoots (rejecting Tokio's existing `far_future()` hack); one view keeps a sleeping future alive and never fires it early, reserving a panic only for the separate, far more extreme case of `Instant::now` itself reaching `Instant::MAX`.
tag: tradeoff
claims: a-sa19-f009196-c6, a-sa19-f009196-c5

## Question `tokio-as-default-runtime`

### tokio-as-default-runtime--tokio-default
Despite criticisms of Tokio, the alternatives (async-std stale, smol inactive, glommio Linux-only) are judged too limited, so Tokio remains the best option for this project, reinforced by it already being the default of a key dependency; separately, Tokio is commonly characterized as "the one true async runtime" powering much of Rust's networking ecosystem.
tag: tradeoff
claims: b-sb17-f005159-c1, a-sa29-f012940-c2

### tokio-as-default-runtime--p1
Recommends Tokio as the guide's runtime for most readers because it's general purpose, the most popular in the ecosystem, and good for both getting started and production, while noting other runtimes may perform better or simplify code in some circumstances.
tag: taste
claims: b-bk01-f000233-c3

### tokio-as-default-runtime--p2
States flatly that no asynchronous runtime is officially recommended and lists Tokio, async-std, smol and fuchsia-async as options without ranking them, discussing cross-runtime incompatibility as a reason to check fit before committing.
tag: fact
claims: b-bk01-f000233-c4

## Question `tokio-axum-vs-nginx-performance`

### tokio-axum-vs-nginx-performance--p1
Nginx is highly-tuned async C++, while the compared Rust server is untuned "out of the box," so the two aren't on equal footing in a benchmark.
tag: fact
claims: a-sa14-f005360-c5

### tokio-axum-vs-nginx-performance--p2
Cloudflare's production replacement of nginx with the Tokio-based Pingora proxy is pointed to as evidence Tokio is fast out of the box and that Rust's async was designed from the ground up for low overhead.
tag: fact
claims: a-saL1-f005360-c7

### tokio-axum-vs-nginx-performance--p3
Tokio and Hyper are both very fast, but Axum adds its own routing/extractor overhead on top, disappointingly so given Actix-Web previously topped benchmarks while also providing routing and extractors; recommends Hyper and Tower directly when complex path routing isn't needed.
tag: fact
claims: a-saL1-f005360-c8, a-saL1-f005360-c9

## Question `totokens-intermediate-tokenstream`

### totokens-intermediate-tokenstream--p1
Rewrite the `ToTokens` impl so each match arm calls `to_tokens` on its inner value directly, avoiding allocating a temporary `TokenStream` just to feed it into another.
tag: taste
claims: a-sR01-f000538-c1

## Question `tower-middleware-vs-handler-helpers`

### tower-middleware-vs-handler-helpers--middleware-layer
An `EndpointHooks`-style trait intercepts connections before connect and after handshake, so authentication, authorization, rate limiting and observability sit at the connection layer and individual protocols stay on their core logic instead of each handling auth themselves; surveying the wider ecosystem, most codebases instead bolt these concerns directly into handlers via ad-hoc helpers, macros or trait extensions, none of which quite match the convenience and composability of a real middleware stack.
tag: tradeoff
claims: a-sT08-f004169-c3, b-sb22-f008906-c1

## Question `trace-context-propagation-mechanism`

### trace-context-propagation-mechanism--p1
There is no one all-good solution today for context propagation in distributed scenarios: the eBPF kernel function that could write into user-space memory was locked down in 2021 over security concerns and its replacement can crash the user-space program, while the traditional library-interposition alternative works well but gets messy when the libraries are statically linked.
tag: fact
claims: b-sb24-f011306-c3

## Question `tracing-crate-vs-otel-api`

### tracing-crate-vs-otel-api--p1
The Tokio `tracing` crate is widely adopted but not fully suited to distributed tracing, while the OpenTelemetry API is spec-compliant but far less adopted; the community has debated dropping one, but the current practical (still unstable) path is to keep both active and improve interoperability between them.
tag: tradeoff
claims: b-sb24-f011306-c1

## Question `tracing-vs-log-for-otel`

### tracing-vs-log-for-otel--p1
The OpenTelemetry Rust project bridges existing loggers rather than mandating its own API, but recommends `tracing` for new applications because its Span concept aligns with OTel spans.
tag: taste
claims: a-sa29-f012940-c1

## Question `trait-api-forced-arc-self`

### trait-api-forced-arc-self--p1
The trait previously required callers to wrap `self` in explicit `Arc`s; this requirement was dropped, allowing a more flexible structure for defining protocols.
tag: tradeoff
claims: b-sR05-f002453-c2

## Question `trait-default-methods-vs-major-bump`

### trait-default-methods-vs-major-bump--p1
Added default implementations for two new trait methods so they wouldn't trigger a backward-incompatible change, shipping them in a minor release and planning to make them required only in the next major version; a reviewer endorses shipping the new methods this way rather than waiting for a major bump.
tag: tradeoff
claims: b-sR08-f003540-c1, b-sR08-f003540-c2

## Question `trait-error-open-custom-variant`

### trait-error-open-custom-variant--p1
For traits users can implement themselves, the associated error type includes a `User`/custom variant plus `from_err`/`from_err_box` helpers, so implementors can propagate their own errors rather than being boxed into the crate's own failure modes.
tag: tradeoff
claims: a-sa14-f005149-c3

## Question `trait-impl-boilerplate-mechanism`

### trait-impl-boilerplate-mechanism--p1
Proposes new dedicated impl shorthand syntax for traits with exactly one required method, generalized as official syntactic sugar, removing an indentation level and the need to look up the method's exact signature.
tag: taste
claims: a-sa19-f009292-c7

### trait-impl-boilerplate-mechanism--p2
Rather than new syntax, wants the compiler to infer associated types (e.g. `Iterator::Item`) from the method body, simplifying implementations of `Add`, `Sub`, `IntoIterator` and `Deref` without adding new surface syntax.
tag: taste
claims: a-sa19-f009292-c8

## Question `traits-as-inheritance-substitute`

### traits-as-inheritance-substitute--p1
Modeling an OOP-style hierarchy via supertrait/subtrait relationships works, but doing it generically over the inner-storage type is a lot more work and, in the speaker's words, more verbose and confusing than the equivalent in Kotlin, Java or TypeScript.
tag: taste
claims: a-sR16-f012428-c1

## Question `trust-microbenchmarks`

### trust-microbenchmarks--distrust-by-default
Benchmarks are always dangerous to quote — "a special type of lie" — with one speaker citing his own conference benchmark as non-apples-to-apples and arguing such benchmarks, especially given without a right of reply, should be treated as suspect by default; another declares blanket moral opposition to microbenchmarks outright.
tag: taste
claims: a-sa28-f012469-c2, a-sa25-f011413-c6, a-sa28-f012469-c1

## Question `typed-response-struct-vs-untyped-value`

### typed-response-struct-vs-untyped-value--p1
Replaces untyped JSON output with a `Serialize` struct so the compiler validates the response shape, leveraging Rust's strong typing to do that work.
tag: taste
claims: a-sT11-f007659-c3

## Question `typed-wrapper-vs-raw-access`

### typed-wrapper-vs-raw-access--p1
A raw matrix type cannot guarantee it represents a pure rotation, isometry, or even an invertible transform, so dedicated transformation types are recommended instead of raw matrices.
tag: tradeoff
claims: a-sB01-f000217-c2

### typed-wrapper-vs-raw-access--p2
A typo'd raw column-family-name string can cause a panic, so route every read/write through one typed method defined once per column family instead of low-level generic methods; similarly, raw volatile register operations should give way to PAC-generated typed accessors, and a missing PAC accessor is treated as a bug to fix in the PAC rather than worked around with manual bit ops.
tag: tradeoff
claims: b-bk03-f000267-c8, a-sa09-f004055-c1, a-sa09-f004055-c2

## Question `typestate-crypto-keys`

### typestate-crypto-keys--p1
Types give "superpowers": a `Role` marker type and a verified/unverified type-state on cryptographic keys make passing the wrong key role fail to compile, and an unverified key cannot be used for cryptographic operations until explicitly checked.
tag: tradeoff
claims: b-sb24-f011295-c2

## Question `typestate-generic-vs-separate-types`

### typestate-generic-vs-separate-types--p1
Separate structs per connection variant duplicated the whole connection API and stopped connections sharing code paths; a single generic type with a state parameter restores that flexibility and de-duplicates the code, with state-specific signatures only where behavior actually differs.
tag: tradeoff
claims: a-sT08-f004169-c1
