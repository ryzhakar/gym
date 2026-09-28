# Summaries, batch 1 file 12 (fill b)

## Question `sound-lifetime-erasure-in-callbacks`

### sound-lifetime-erasure-in-callbacks--p1
Summary: Casting away a reference's lifetime to store it for a later callback isn't really allowed — at any point there might be an aliased mutable reference, and a comment claiming the lifetime outlives the callback doesn't hold since the external API is free to do what it wants. The sound fix is a thread-local holding the pointer only for the duration it's actually needed — still `unsafe`, but far easier to reason about than a bare raw-pointer cast.
Tag: fact
Claims: b-sR04-f001749-c1

## Question `spawn-vs-compose-futures`

### spawn-vs-compose-futures--p1
Summary: If parallelism is wanted, or not explicitly excluded, spawning separate tasks is usually simpler than `join!`/`select!` — less error-prone, more general, and each spawned task gets a fair scheduling share, giving more predictable performance than composing futures inside one task. The tradeoff is less structure and harder-to-reason-about lifecycle and resource management.
Tag: tradeoff
Claims: b-bk01-f000233-c5

## Question `speculative-from-impls`

### speculative-from-impls--p1
Summary: Remove a speculative conversion now — adding another `From` impl later would produce a compile error on existing code, so it's better not to add related conversions ahead of actually needing them.
Tag: fact
Claims: a-sa11-f004265-c2

## Question `spi-hardware-cs-in-spibus`

### spi-hardware-cs-in-spibus--p1
Summary: Chip select should just be an ordinary GPIO `Output` pin — that way one bus can address as many targets as there are available GPIOs. Hardware chip-select complicates the embedded-hal `SpiBus`/`SpiDevice` split, which is why most HALs tend not to use it.
Tag: tradeoff
Claims: a-sa09-f004055-c4, a-sa09-f004055-c3

### spi-hardware-cs-in-spibus--p2
Summary: Use marker types (`HardwareCs`, `NoCs`) so `SpiBus` is implemented only for the no-hardware-CS variant, following embedded-hal semantics where `SpiBus` means exclusive bus access without CS management — while a separate constructor still exposes hardware CS for callers who specifically want it.
Tag: tradeoff
Claims: a-sa09-f004055-c5

## Question `stable-contract-api-vs-cli`

### stable-contract-api-vs-cli--p1
Summary: The Rust APIs of the crates are currently unstable and unsupported; the versioned, supported surface for interacting with the application is the CLI commands and JSON-RPCs, not the Rust library API.
Tag: fact
Claims: b-bk03-f000267-c10

## Question `state-accessor-and-stream-split`

### state-accessor-and-stream-split--p1
Summary: A single primitive that tries to serve both "what's the state right now" and "tell me when it changes" ends up serving neither well — splitting it into a lifetime-bound borrowed-snapshot accessor and a separate `'static` event stream lets each answer just one question.
Tag: tradeoff
Claims: a-sR13-f004685-c1

## Question `static-allocation-in-real-time`

### static-allocation-in-real-time--p1
Summary: Dynamic allocation is problematic for resource-constrained real-time systems on both performance and reliability grounds — Rust panics on out-of-memory — so static allocation is the preferable approach.
Tag: tradeoff
Claims: a-sB01-f000227-c4

## Question `static-model-security-guarantees`

### static-model-security-guarantees--p1
Summary: Even a formally verified RTOS kernel like seL4 only claims integrity, confidentiality and availability for the kernel itself, not the whole system, especially once dynamic allocation enters the picture. A declarative, static, system-wide task/resource model, combined with Rust's compile-time aliasing, mutability and lifetime guarantees, propagates integrity properties across the whole system instead of stopping at the kernel boundary.
Tag: fact
Claims: a-sB04-f000227-c4

## Question `static-verification-no-panic-mechanism`

### static-verification-no-panic-mechanism--p1
Summary: Clippy lints don't recurse into dependencies and only cover hard-coded library types; an effect-type system would require a new language; a link-time hack is optimization-dependent, has no async support, and breaks under `panic = "abort"`/no_std; cfg-forking the standard library affects every consumer and breaks tooling. The most accurate approach, now shipped and certified against, is a custom rustc driver using a post-monomorphization pass to detect every resolved function call.
Tag: fact
Claims: b-sR12-f005169-c1

## Question `std-mutex-vs-async-mutex`

### std-mutex-vs-async-mutex--p1
Summary: Use `std::Mutex` if you can; reserve the async `Mutex` for cases where the lock must be held across an `.await` point or protects an IO resource, since the async version is more expensive precisely because it supports being held across awaits.
Tag: tradeoff
Claims: b-bk01-f000233-c8

## Question `std-naming-convention-imperfect-fit`

### std-naming-convention-imperfect-fit--p1
Summary: `raw_parts` works even though there's no matching `into_raw_parts` here, only `from_raw_parts` — but this isn't the standard library, so it's fine if the pattern doesn't apply exactly.
Tag: taste
Claims: b-sR05-f002326-c1

## Question `std-naming-conventions-strictness`

### std-naming-conventions-strictness--strict
Summary: `into_` should only be used where the method actually consumes `self` — a name that doesn't match its ownership signature should be renamed. `to_owned` in particular is not a bad name: the receiver is neither doing the owning nor being owned, it's being copied into a different form, so `own()` would misdescribe the operation — the Rust API Guidelines document is the standing rationale for the `to_` prefix here, and naming here, while inherently imperfect, isn't wrong.
Tag: taste
Claims: b-sR08-f003587-c2, b-sb22-f009236-c3, b-sb22-f009236-c2

### std-naming-conventions-strictness--loose
Summary: `Clone`/`Borrow` aren't named `ToCloned`/`AsBorrowed`, so the `to_`/`as_`/`into_` prefix is unneeded morphology when converting between representations of the *same* type — it should just be `Own`, and `"whatever".own()` reads better than `"whatever".to_owned()` — even while granting the prefix convention makes sense for genuine cross-type conversions like `IntoIterator`.
Tag: taste
Claims: b-sb22-f009236-c1

## Question `synthetic-canary-vs-tracing`

### synthetic-canary-vs-tracing--p1
Summary: No information about the timing of real source messages can leave the on-premises cover node, so tracing real messages through the system is out. Instead, run a "message canary" that sends a real encrypted message through the live system once an hour and measures delivery time, alarming if delivery exceeds three hours.
Tag: tradeoff
Claims: b-sb24-f011295-c3

## Question `tail-expression-vs-explicit-return`

### tail-expression-vs-explicit-return--p1
Summary: Coming from a lot of Rust work, the last-expression rule seriously hurts readability for both function returns and `if` expressions — worst of all when the block is long and the last expression sits far from the assignment it feeds.
Tag: taste
Claims: b-sT02-f000576-c1

### tail-expression-vs-explicit-return--p2
Summary: In direct personal experience it runs the other way: Rust's implicit return of the last expression is much easier to read than having `return` statements scattered everywhere.
Tag: taste
Claims: b-sT02-f000576-c2

## Question `target-tier-without-ci`

### target-tier-without-ci--p1
Summary: With Apple ending x86_64 support and GitHub ending free macOS x86_64 runners for public repositories, the tier policy's requirement that Tier 1 platforms run CI tests forces the target to Tier 2 with host tools from 1.90.0 — builds are still distributed, but the target will likely accumulate bugs faster and could be demoted further if it causes problems.
Tag: fact
Claims: a-sT12-f009704-c1

## Question `teach-rust-in-curricula`

### teach-rust-in-curricula--p1
Summary: Modern software education over-focuses on frameworks and abstractions and under-teaches how systems actually work — memory, concurrency, performance, tradeoffs. It's not bad to use frameworks, but it's valuable to understand what's going on behind the wood, and Rust forces students to confront ownership, memory and error handling directly, concepts other languages abstract away.
Tag: taste
Claims: a-sa26-f011443-c1

## Question `test-via-real-entry-point`

### test-via-real-entry-point--p1
Summary: Even after a fix, nothing tests the actual gesture — toggle/switch tests still drive the methods directly rather than the deferred mouse-event path itself. At least one test should dispatch the real action via a keystroke against the real strip, not a bespoke harness, so a broken keybinding wiring would actually be caught.
Tag: tradeoff
Claims: a-sa13-f004772-c4, a-sa13-f004772-c3

### test-via-real-entry-point--p2
Summary: The dangerous bugs aren't in new code, they're in what old code used to do that nothing does anymore — a refactor can silently stop enforcing a check with no test failing and no diff showing a deleted check. The guide requires inventorying every rejection the old code could produce and naming its new home, testing every parse-time rejection through the actual production entry point rather than only the check's own unit tests, and individually auditing fallible conversions (`.ok()`, `unwrap_or`, defaulted `try_from`) that could silently turn an invalid value into one a check treats as benign — two real incidents slipped through this exact gap with green CI.
Tag: tradeoff
Claims: b-bk03-f000267-c15

## Question `threads-vs-simd-for-batch-work`

### threads-vs-simd-for-batch-work--p1
Summary: Instruction-level parallelism alone is a good choice for a small batch of blobs — decent speedup, stays on one CPU, doesn't affect the rest of the program — but for peak performance, combining instruction-level and thread-level parallelism wins, measured at 17x over sequential and 2.1x over thread-level parallelism alone.
Tag: fact
Claims: b-sR08-f003702-c1

## Question `tiered-checked-unchecked-apis`

### tiered-checked-unchecked-apis--p1
Summary: Deliberately expose three ways to build the same row: a positional "Fast API" for best performance, a "Safe API" that validates field names, and an "Indexed API" balancing the two — so callers pick their own safety/performance tradeoff rather than the crate picking one for them.
Tag: tradeoff
Claims: a-sR16-f012642-c1

## Question `timer-instant-overflow-panic`

### timer-instant-overflow-panic--p2
Summary: The correct behavior is to never register a future as ready again once its wake time would overflow, rather than firing based on a MAX-derived time that undershoots — Tokio's `far_future()` hack is unnecessary. One version of this position keeps a sleeping future alive but never fires it early, reserving a panic only for the extremely unlikely case that `Instant::now` itself reaches `Instant::MAX`, since no reasonable behavior exists past that point.
Tag: tradeoff
Claims: a-sa19-f009196-c6, a-sa19-f009196-c5

## Question `tokio-as-default-runtime`

### tokio-as-default-runtime--tokio-default
Summary: Despite criticisms of Tokio, the alternatives are limited — async-std stale, smol inactive, glommio Linux-only — so Tokio remains the best option, reinforced by being quinn's default. It's often regarded as the one true async runtime and powers much of Rust's networking ecosystem.
Tag: taste
Claims: b-sb17-f005159-c1, a-sa29-f012940-c2

### tokio-as-default-runtime--p1
Summary: Tokio is a general-purpose runtime and the most popular in the ecosystem, good for both getting started and production — recommended as the runtime for most of this guide, while noting other runtimes may give better performance or simpler code in some circumstances.
Tag: tradeoff
Claims: b-bk01-f000233-c3

### tokio-as-default-runtime--p2
Summary: There is no asynchronous runtime in the standard library, and none are officially recommended — Tokio, async-std, smol and fuchsia-async are listed as options without ranking, and cross-runtime incompatibility (Tokio's mio-based reactor vs. the async-executor/futures-I/O-trait world of async-std and smol) is a reason to research fit before committing to one.
Tag: fact
Claims: b-bk01-f000233-c4

## Question `tokio-axum-vs-nginx-performance`

### tokio-axum-vs-nginx-performance--p1
Summary: It's difficult to see how an untuned "out of the box" async Rust server could be competitive, since nginx is highly-tuned async C++ and the comparison isn't apples to apples.
Tag: fact
Claims: a-sa14-f005360-c5

### tokio-axum-vs-nginx-performance--p2
Summary: Cloudflare replaced nginx in production with the Tokio-based Pingora proxy — Tokio is pretty fast out of the box, and Rust's async was designed from the ground up to be very low overhead.
Tag: fact
Claims: a-saL1-f005360-c7

### tokio-axum-vs-nginx-performance--p3
Summary: Tokio and Hyper are both very fast on their own, but Axum adds its own routing/extractor overhead on top — surprising, since Actix-Web previously topped benchmarks while also providing routing and extractors, so Axum wasn't expected to differ much. Where complex path routing and extractors aren't needed, it's probably better to use Hyper and Tower directly.
Tag: fact
Claims: a-saL1-f005360-c8, a-saL1-f005360-c9

## Question `totokens-intermediate-tokenstream`

### totokens-intermediate-tokenstream--p1
Summary: Rewrite the `ToTokens` impl so each match arm calls `to_tokens` on its inner value directly, rather than building a temporary `TokenStream` from one variant just to feed it into another.
Tag: tradeoff
Claims: a-sR01-f000538-c1

## Question `tower-middleware-vs-handler-helpers`

### tower-middleware-vs-handler-helpers--middleware-layer
Summary: An `EndpointHooks` trait intercepts connections before connect and after handshake, so authentication, authorization, rate limiting and observability sit at the connection layer and individual protocols don't need to handle authentication themselves. Looking across almost every Rust Lambda codebase reviewed recently, logging/auth/validation gets bolted directly into the handler via helpers, macros or trait extensions — none of which quite match the convenience and composability of the middleware engine already built into the runtime via tower.
Tag: tradeoff
Claims: a-sT08-f004169-c3, b-sb22-f008906-c1

## Question `trace-context-propagation-mechanism`

### trace-context-propagation-mechanism--p1
Summary: There is no one all-good solution as of now for context propagation in distributed scenarios: the eBPF kernel function that could write into user-space memory was locked down in 2021 over security concerns, and its replacement zero-initializes on load and can crash the program if headers were already allocated there; the non-eBPF alternative, library interposition via `LD_PRELOAD` on libcurl/libssl, works well but gets messy when those libraries are statically linked.
Tag: fact
Claims: b-sb24-f011306-c3

## Question `tracing-crate-vs-otel-api`

### tracing-crate-vs-otel-api--p1
Summary: The Tokio `tracing` crate is widely adopted but not fully suited to distributed tracing, while the OpenTelemetry API is spec-compliant but far less adopted; the community has debated dropping one, but the current practical (still unstable) path is to keep both active and improve interoperability between them.
Tag: tradeoff
Claims: b-sb24-f011306-c1

## Question `tracing-vs-log-for-otel`

### tracing-vs-log-for-otel--p1
Summary: OpenTelemetry Rust bridges existing loggers rather than mandating its own API, but recommends `tracing` for new applications because its Span concept aligns with OTel spans.
Tag: tradeoff
Claims: a-sa29-f012940-c1

## Question `trait-api-forced-arc-self`

### trait-api-forced-arc-self--p1
Summary: The trait previously required using explicit `Arc`s, but this is no longer required, allowing a more flexible structure in defining protocols.
Tag: tradeoff
Claims: b-sR05-f002453-c2

## Question `trait-default-methods-vs-major-bump`

### trait-default-methods-vs-major-bump--p1
Summary: Provide default implementations for the new trait methods for now so they don't trigger a backward-incompatible change, and ship them in a minor release — planning to make them required only in the next major version.
Tag: tradeoff
Claims: b-sR08-f003540-c1, b-sR08-f003540-c2

## Question `trait-error-open-custom-variant`

### trait-error-open-custom-variant--p1
Summary: For traits that users can implement themselves, the associated error type needs a `User`/Custom variant plus `from_err`/`from_err_box` helpers, so implementors can propagate their own errors instead of being boxed into the crate's own failure modes.
Tag: tradeoff
Claims: a-sa14-f005149-c3

## Question `trait-impl-boilerplate-mechanism`

### trait-impl-boilerplate-mechanism--p1
Summary: For traits with exactly one required method, syntactic sugar like `impl Display (self, f) for Type { ... }` would remove an indentation level and the need to look up the method's exact signature, beyond what derive alone offers — worth generalizing into official sugar.
Tag: tradeoff
Claims: a-sa19-f009292-c7

### trait-impl-boilerplate-mechanism--p2
Summary: There's really no need to write out `type Item = i32;` when it's the only possible thing given the method body — the compiler should infer associated types like `Iterator::Item` from context, simplifying `Add`, `Sub`, `IntoIterator` and `Deref` impls without new surface syntax.
Tag: tradeoff
Claims: a-sa19-f009292-c8

## Question `traits-as-inheritance-substitute`

### traits-as-inheritance-substitute--p1
Summary: Modeling an OOP-style view/component hierarchy in Rust via supertrait/subtrait relationships works, but doing it generically over the inner-storage type takes a lot more work and is, in his words, more verbose and somewhat confusing especially coming from Kotlin, Java or TypeScript.
Tag: taste
Claims: a-sR16-f012428-c1

## Question `trust-microbenchmarks`

### trust-microbenchmarks--distrust-by-default
Summary: Benchmarks are, always, generally, dangerous to quote because they're a special type of lie; microbenchmarks especially — his own "Canada" benchmark against serde_json isn't apples-to-apples because it skips a precise floating-point rounding mode, and conference benchmarks given without a right of reply should be treated as suspect by default. Blanket moral opposition: they should all be consumed by gaping fissures in the earth's crust.
Tag: fact
Claims: a-sa28-f012469-c2, a-sa25-f011413-c6, a-sa28-f012469-c1

## Question `typed-response-struct-vs-untyped-value`

### typed-response-struct-vs-untyped-value--p1
Summary: Leverage Rust's strong typing to do the work: replace untyped JSON output with a `Serialize` struct so the compiler validates the response shape.
Tag: tradeoff
Claims: a-sT11-f007659-c3

## Question `typed-wrapper-vs-raw-access`

### typed-wrapper-vs-raw-access--p1
Summary: A raw `Matrix4` can't guarantee it represents a pure rotation, isometry, or even an invertible transform — that's why dedicated transformation types are recommended instead of raw matrices.
Tag: tradeoff
Claims: a-sB01-f000217-c2

### typed-wrapper-vs-raw-access--p2
Summary: Typing a column family's name out every time is error-prone — a typo causes a panic since the column family doesn't exist — so define the name and type of each column family once and route every read/write through a typed method. Likewise, raw volatile register operations should be questioned in favor of PAC-generated typed accessors, and if the PAC is missing an accessor, that's a bug to fix in the PAC, not a reason to fall back to manual bit operations.
Tag: tradeoff
Claims: b-bk03-f000267-c8, a-sa09-f004055-c1, a-sa09-f004055-c2

## Question `typestate-crypto-keys`

### typestate-crypto-keys--p1
Summary: Types give superpowers: they let the rules of a system be encoded in a way checked at compile time, helping prevent mistakes. Cryptographic keys get a `Role` marker type and a verified/unverified type-state, so passing a cover-node key where a journalist-provisioning key is required fails to compile, and an unverified key can't be used cryptographically until explicitly checked.
Tag: tradeoff
Claims: b-sb24-f011295-c2

## Question `typestate-generic-vs-separate-types`

### typestate-generic-vs-separate-types--p1
Summary: Separate structs per connection variety duplicated the whole connection API and stopped 0-RTT connections from sharing code paths; a single `Connection<T>` with a state parameter restores that flexibility and de-duplicates the code, with state-specific signatures only where authentication actually differs.
Tag: tradeoff
Claims: a-sT08-f004169-c1
