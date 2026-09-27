# Blind fill input, batch 1, file 12 of 13

For each Claim below, name the one Position of its Question that the Claim supports (a Position id from the list), or `none` if it supports none of them. The Claims are in random order.

## Question `sound-lifetime-erasure-in-callbacks`

When an external callback API erases a reference's lifetime so it can be stored for later, how should the resulting unsafe surface be structured to stay sound?

Positions:
- `sound-lifetime-erasure-in-callbacks--p1`: Thread local scoped storage over raw pointer cast
- `sound-lifetime-erasure-in-callbacks--alt1`: Cast the lifetime away with a raw pointer

Claims:
- `b-sR04-f001749-c1` · Voice: ArthurBrussee · Source: https://github.com/emilk/egui/pull/4849 (`f001749`) · Date: 2024-07-26 · Locator: PR #4849, comment 2024-07-26T01:00:25Z
  - Quote: "That's really not allowed! At any point there might be an aliased mutable reference, and the comment about how the lifetime outlives the callback doesnt really make sense to me - winit is free to do what it wants!"
  - Paraphrase: the prior integration cast away an `&ActiveEventLoop`'s lifetime to store it for a later callback, which he judged unsound (possible aliased mutable reference, no real outlives guarantee from winit); replaced it with a thread-local holding the pointer only for the paint call's duration — still `unsafe`, but easier to reason about.

## Question `spawn-vs-compose-futures`

When running multiple futures concurrently, should you spawn separate tasks or compose them in place with `join!`/`select!`?

Positions:
- `spawn-vs-compose-futures--p1`: Prefer spawn+JoinHandles for parallelism
- `spawn-vs-compose-futures--alt1`: Compose in place with `join!`/`select!`

Claims:
- `b-bk01-f000233-c5` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "Composing futures concurrently" § Alternatives / Final words
  - Quote: "Spawning tasks is usually less error-prone, more general, and performance is more predictable."
  - Paraphrase: if parallelism is wanted (or not explicitly excluded), spawning tasks is usually a simpler alternative to join!/select!, being less error-prone, more general, and giving more predictable/fairer performance (each spawned task gets a fair scheduling share, unlike futures joined inside one task); spawning is traded off against being less structured, harder to reason about lifecycle and resource management.

## Question `speculative-from-impls`

When you can foresee wanting another blanket `From` impl for a type later, should you add related conversions now speculatively, or hold off to avoid a breaking compile error for downstream users when you do add it?

Positions:
- `speculative-from-impls--p1`: Avoid speculative trait impls that would break under a later addition
- `speculative-from-impls--alt1`: Add related conversions now

Claims:
- `a-sa11-f004265-c2` · Voice: MabezDev · Source: https://github.com/esp-rs/esp-hal/pull/5002 (`f004265`) · Date: 2026-02-19 · Locator: comment 2026-02-19T14:04:18Z; 2026-02-19T14:04:25Z
  - Quote: "Remove this, if we add another from impl later, we'll get a compile error on existing code."
  - Paraphrase: asks to remove a conversion because adding another `From` impl later would produce a compile error on existing code

## Question `spi-hardware-cs-in-spibus`

Should an SPI driver expose hardware chip-select (CS) control as part of the embedded-hal `SpiBus` trait, or restrict `SpiBus` to software/GPIO-controlled CS and handle hardware CS separately?

Positions:
- `spi-hardware-cs-in-spibus--p1`: Software cs via spidevice
- `spi-hardware-cs-in-spibus--p2`: Support both type level distinction

Claims:
- `a-sa09-f004055-c4` · Voice: felipebalbi · Source: https://github.com/embassy-rs/embassy/pull/5175 (`f004055`) · Date: 2026-01-07 · Locator: comment @felipebalbi 2026-01-07T19:47:44Z
  - Quote: "I would rather use CS as regular Output GPIOs. This means we can talk to as many targets as we have available GPIOs for."
  - Paraphrase: prefers CS as ordinary GPIO `Output` pins so one bus can address as many targets as there are available GPIOs
- `a-sa09-f004055-c5` · Voice: bogdan-petru · Source: https://github.com/embassy-rs/embassy/pull/5175 (`f004055`) · Date: 2026-02-05 · Locator: comment @bogdan-petru 2026-02-05T04:50:38Z
  - Quote: "The SpiBus trait is now only implemented for Spi<..., NoCs>, following embedded-hal semantics where SpiBus represents exclusive bus access without CS management."
  - Paraphrase: converges on marker types (`HardwareCs`, `NoCs`) so `SpiBus` is implemented only for the no-hardware-CS variant, while a separate constructor still exposes hardware CS for callers who want it
- `a-sa09-f004055-c3` · Voice: jamesmunns · Source: https://github.com/embassy-rs/embassy/pull/5175 (`f004055`) · Date: 2026-01-05 · Locator: comment @jamesmunns 2026-01-05T14:30:11Z
  - Quote: "In many other HALs, we tend to not utilize hardware chip selects, as this complicates the embedded-hal SpiBus vs SpiDevice implementations."
  - Paraphrase: hardware chip-select complicates the embedded-hal `SpiBus`/`SpiDevice` split, so most HALs avoid it

## Question `stable-contract-api-vs-cli`

For a Rust binary application distributed as a set of crates, which surface should be the versioned, stable contract — the published Rust library API, or the CLI/RPC surface?

Positions:
- `stable-contract-api-vs-cli--p1`: Rpc cli stable rust api unstable
- `stable-contract-api-vs-cli--alt1`: The published Rust library API is the stable contract

Claims:
- `b-bk03-f000267-c10` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Zebra versioning and releases § Deprecation practices, "Rust APIs"
  - Quote: "The Rust APIs of the Zebra crates are currently unstable and unsupported. Use the zebrad commands or JSON-RPCs to interact with Zebra."
  - Paraphrase: the deprecation policy states that the Rust APIs of the Zebra crates are currently unstable and unsupported; the stable, versioned surface for interacting with Zebra is the zebrad commands and JSON-RPCs, not the Rust library API

## Question `state-accessor-and-stream-split`

Should a Rust crate's live-state accessor and its change-notification stream be one overloaded API or two separate primitives?

Positions:
- `state-accessor-and-stream-split--p1`: Split into two primitives
- `state-accessor-and-stream-split--alt1`: One overloaded API serving both

Claims:
- `a-sR13-f004685-c1` · Voice: iroh/n0 (Friedel Ziegelmayer & Rüdiger Klaehn, post authors) · Source: https://iroh.computer/blog/iroh-1-0-0-rc-0 (`f004685`) · Date: 2026-05-11 · Locator: § "Path observation API redesign"
  - Quote: "went through PathWatcher, a single primitive that tried to serve two very different consumers: code that wants \"what are the paths right now?\" and code that wants \"tell me when paths change\""
  - Paraphrase: the single `PathWatcher` primitive tried to serve both "what are the paths right now" and "tell me when paths change," so it was replaced by `Connection::paths()` (a lifetime-bound borrowed snapshot) and `Connection::path_events()` (a `'static` event stream), each answering one question

## Question `static-allocation-in-real-time`

In resource-constrained real-time systems, should allocation be static rather than dynamic?

Positions:
- `static-allocation-in-real-time--p1`: Static allocation preferred over dynamic in real-time systems
- `static-allocation-in-real-time--alt1`: Dynamic allocation

Claims:
- `a-sB01-f000227-c4` · Voice: RTIC developers · Source: https://rtic.rs/ (`f000227`) · Date: undated (living doc) · Locator: Preface, "RTIC into the Future"
  - Quote: "Thus, static allocation is the preferable approach!"
  - Paraphrase: States dynamic allocation is problematic for resource-constrained real-time systems on both performance and reliability grounds (Rust panics on out-of-memory), so static allocation is the preferable approach

## Question `static-model-security-guarantees`

Can a Rust-based real-time framework's compile-time static model provide stronger system-wide security guarantees (particularly integrity) than a traditional RTOS kernel, even a formally verified one?

Positions:
- `static-model-security-guarantees--p1`: RTIC+Rust's static model extends integrity guarantees system-wide; traditional RTOS kernel security covers only the kernel
- `static-model-security-guarantees--alt1`: A traditional RTOS kernel's guarantees suffice (e.g. seL4)

Claims:
- `a-sB04-f000227-c4` · Voice: RTIC developers · Source: https://rtic.rs/ (`f000227`) · Date: undated (living doc, v2.x) · Locator: "4. RTIC vs. the world", "Comparison regarding safety and security"
  - Quote: "RTIC on the other hand holds your back. The declarative system wide model gives you a static set of tasks and resources, with precise control over what data is shared and between which parties."
  - Paraphrase: Argues that even a formally verified RTOS kernel like seL4 only claims integrity/confidentiality/availability for the kernel itself, not the whole system, especially once dynamic allocation is involved; RTIC's declarative static task/resource model plus Rust's compile-time aliasing, mutability and lifetime guarantees propagate integrity properties across the whole system instead

## Question `static-verification-no-panic-mechanism`

How should a Rust project statically verify a property like "this function never panics" or "this function never calls unvalidated code" across a codebase: clippy lints, a new effect-type system, a link-time hack, a cfg-forked standard library, or a custom compiler driver?

Positions:
- `static-verification-no-panic-mechanism--p1`: Custom compiler driver post mono
- `static-verification-no-panic-mechanism--alt1`: Clippy lints
- `static-verification-no-panic-mechanism--alt2`: a new effect-type system
- `static-verification-no-panic-mechanism--alt3`: a link-time hack
- `static-verification-no-panic-mechanism--alt4`: a cfg-forked standard library

Claims:
- `b-sR12-f005169-c1` · Voice: Jynn (Ferrous Systems, Ferrocene team) · Source: https://ferrous-systems.com/blog/callgraph-analysis (`f005169`) · Date: 2026-04-08 · Locator: section "What have we learned?" (whole post walks the alternatives it rejects: clippy lints, effect-type systems, link-time no_panic hack, cfg-forked std)
  - Quote: "For Ferrocene, the most accurate approach was to write a custom rustc driver which uses a post-monomorphization pass to detect all resolved function calls."
  - Paraphrase: for certifying that validated `core` functions only call other validated functions (generalizable to "never panics"), clippy lints don't recurse into dependencies and only cover hard-coded library types; an effect-type system would require a new language; a link-time hack is optimization-dependent, has no async support, breaks under `panic = "abort"`/no_std, and is unsafe to use in library crates; cfg-forking the standard library affects every consumer and breaks tooling. A custom rustc driver with a post-monomorphization MIR pass was the most accurate approach and is what Ferrocene now ships and certifies against

## Question `std-mutex-vs-async-mutex`

In async code, should locking default to a std (sync) `Mutex` or an async `Mutex`?

Positions:
- `std-mutex-vs-async-mutex--p1`: Prefer std Mutex where possible
- `std-mutex-vs-async-mutex--alt1`: Default to an async `Mutex`

Claims:
- `b-bk01-f000233-c8` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "Channels, locking, and synchronization" § Locks
  - Quote: "use std::Mutex if you can"
  - Paraphrase: recommends using `std::Mutex` if you can, reserving the async `Mutex` for cases where the lock must be held across an `.await` point or protects an IO resource, because the async version is more expensive precisely because it supports being held across awaits.

## Question `std-naming-convention-imperfect-fit`

should a crate's naming for a raw-pointer-plus-length accessor follow std's `raw_parts`/`from_raw_parts` convention even where the analogy is imperfect (no matching `into_raw_parts` exists here), or invent its own name when the fit is inexact?

Positions:
- `std-naming-convention-imperfect-fit--p1`: Reuse the `raw_parts`-style name anyway; std's convention doesn't have to apply exactly to a non-std crate
- `std-naming-convention-imperfect-fit--alt1`: Invent a name when the analogy with std is inexact

Claims:
- `b-sR05-f002326-c1` · Voice: bugadani (esp-hal maintainer) · Source: https://github.com/esp-rs/esp-hal/pull/2546 (`f002326`) · Date: 2024-11-23 · Locator: esp-rs/esp-hal#2546, comment 2024-11-23T13:48:41Z. · L1903-L1905.
  - Quote: "`raw_parts` works, I decided against it because there is no 'into_raw_parts', just 'from_raw_parts'. But we are also not the standard library, so I guess it's okay if the pattern doesn't apply to us."
  - Paraphrase: reuse the `raw_parts`-style name anyway; std's convention doesn't have to apply exactly to a non-std crate.

## Question `std-naming-conventions-strictness`

How strictly to follow std's `as_`/`to_`/`into_` naming convention?

Positions:
- `std-naming-conventions-strictness--strict`: Follow the convention strictly (`into_` consumes, `to_owned` is correct)
- `std-naming-conventions-strictness--loose`: Reuse the convention loosely, or rename to a bare verb

Claims:
- `b-sR08-f003587-c2` · Voice: nathanielsimard · Source: https://github.com/tracel-ai/burn/pull/3792 (`f003587`) · Date: 2025-10-09 · Locator: PR #3792, review comments 2025-10-09T12:33:22Z and 2025-10-09T13:27:11Z
  - Quote: "The naming isn't correct here, into should consume a self. Maybe `from_mapped_value`"
  - Paraphrase: objects to a method using `into_`-style naming that doesn't actually take ownership of `self`, insisting the name should match the ownership signature and proposing a rename.
- `b-sb22-f009236-c1` · Voice: jvcmarcenes · Source: https://internals.rust-lang.org/t/toowned-is-a-bad-name-for-the-trait/22129 (`f009236`) · Date: 2025-01-07 · Locator: opening post, and follow-up timestamped 2025-01-07T16:24:46
  - Quote: "It should just be Own... I'd much rather write \"whatever\".own() than \"whatever\".to_owned()."
  - Paraphrase: argues by analogy that `Clone`/`Borrow` aren't named `ToCloned`/`AsBorrowed`, so the `to_`/`as_`/`into_` prefix convention is unneeded "morphology" when converting between representations of the *same* type, even while granting the prefix convention makes sense for genuine cross-type conversions like `IntoIterator`
- `b-sb22-f009236-c3` · Voice: jrose · Source: https://internals.rust-lang.org/t/toowned-is-a-bad-name-for-the-trait/22129 (`f009236`) · Date: 2025-01-08 · Locator: reply timestamped 2025-01-08T01:57:00
  - Quote: "no, I don't actually think to_owned is a bad name."
  - Paraphrase: the receiver of `to_owned` is neither doing the owning nor being owned — it is being copied into a different form — so `own()` would misdescribe the operation; naming here is inherently imperfect, but that doesn't make the existing name bad
- `b-sb22-f009236-c2` · Voice: steffahn · Source: https://internals.rust-lang.org/t/toowned-is-a-bad-name-for-the-trait/22129 (`f009236`) · Date: 2025-01-07 · Locator: reply timestamped 2025-01-07T16:10:44
  - Quote: "In that framework, to_ is the correct naming choice."
  - Paraphrase: points directly to the Rust API Guidelines naming-conventions document as the standing rationale for the `to_` prefix here

## Question `synthetic-canary-vs-tracing`

When a system's design forbids observing real user traffic (privacy/anonymity by design), should you build synthetic "canary" traffic that exercises the real system on a schedule, rather than instrumenting/tracing real messages for observability?

Positions:
- `synthetic-canary-vs-tracing--p1`: Synthetic canary over tracing real traffic
- `synthetic-canary-vs-tracing--alt1`: Instrument and trace real traffic

Claims:
- `b-sb24-f011295-c3` · Voice: Zeke Hunter Green · Source: https://youtube.com/watch?v=8n13Oh8c0r4 (`f011295`) · Date: 2025-10-03 · Locator: [30:28]-[32:28]
  - Quote: "we don't want any information on the timing of real source messages to go to any third parties... that means we can't uh add any tracing of real messages going through the system."
  - Paraphrase: because the protocol requires that no timing information about real source messages ever leaves the on-premises cover node (to preserve anonymity), they cannot trace real messages; instead they run a "message canary" that sends real encrypted messages through the live system once an hour and measures delivery time, alarming if delivery exceeds 3 hours

## Question `tail-expression-vs-explicit-return`

Should a Rust block or function yield its value through an implicit tail expression (semicolon-less last line), or does that rule hurt readability enough to favour an explicit marker such as `return`?

Positions:
- `tail-expression-vs-explicit-return--p1`: Tail expression hurts readability
- `tail-expression-vs-explicit-return--p2`: Tail expression reads better

Claims:
- `b-sT02-f000576-c1` · Voice: andrews05 · Source: https://forums.swift.org/t/pitch-multi-statement-if-switch-do-expressions/68443 (`f000576`) · Date: 2023-11-17 · Locator: post @andrews05 2023-11-17T03:44:40Z (quotes their own earlier SE-0380 review comment, whose date is not given in this source)
  - Quote: "as someone who has been working with Rust a lot lately. I am really not a fan of the "last expression" rule"
  - Paraphrase: Says they are strongly opposed to any bare/last-expression rule on readability grounds. Draws on their Rust work: the rule "seriously hurts readability" for function returns and `if` expressions alike, most of all when the block is long and the last expression sits far from the assignment.
- `b-sT02-f000576-c2` · Voice: Nobody1707 · Source: https://forums.swift.org/t/pitch-multi-statement-if-switch-do-expressions/68443 (`f000576`) · Date: 2023-12-01 · Locator: post @Nobody1707 2023-12-01T17:02:06Z
  - Quote: "I find implicit return of the last expression in Rust much easier to read than if there were return statements everywhere."
  - Paraphrase: Answers a claim that languages with last-expression evaluation are worse for it. Says their own experience runs the other way: Rust's implicit return of the last expression is much easier to read than return statements everywhere.

## Question `target-tier-without-ci`

When free CI for a platform disappears, should the Rust project keep the target at Tier 1 by other means, or demote it (here x86_64-apple-darwin to Tier 2 with host tools) and accept less testing?

Positions:
- `target-tier-without-ci--p1`: Demote to Tier 2 with host tools
- `target-tier-without-ci--alt1`: Keep the target at Tier 1 by other means

Claims:
- `a-sT12-f009704-c1` · Voice: Jake Goulding, for the Rust Infrastructure team · Source: https://blog.rust-lang.org/2025/08/19/demoting-x86-64-apple-darwin-to-tier-2-with-host-tools (`f009704`) · Date: 2025-08-19 · Locator: § "Background", § "What changes?", § "Future"
  - Quote: "Since the target tier policy requires that Tier 1 platforms must run tests in CI, the x86_64-apple-darwin target must be demoted to Tier 2."
  - Paraphrase: Apple is ending x86_64 support, and GitHub is ending free macOS x86_64 runners for public repositories. The tier policy requires Tier 1 targets to run CI tests, so from 1.90.0 the target becomes Tier 2 with host tools; builds are still distributed, but the target will likely accumulate bugs faster and may be demoted further if it causes problems

## Question `teach-rust-in-curricula`

should introductory CS/software-engineering curricula teach a systems language like Rust directly (to force understanding of memory, concurrency, ownership), or is teaching via high-level frameworks and abstractions sufficient?

Positions:
- `teach-rust-in-curricula--p1`: Teach Rust directly to force systems understanding
- `teach-rust-in-curricula--alt1`: Teaching through high-level frameworks and abstractions is sufficient

Claims:
- `a-sa26-f011443-c1` · Voice: Mordecai Emmanuel Etukudo · Source: https://youtube.com/watch?v=RROFUwKZbCA (`f011443`) · Date: 2026-06-11 · Locator: ~01:10-02:10
  - Quote: "The modern software education... focus more on teaching people about framework and a lot of abstractions... it's not bad to use frameworks... but it's nice to understand what is going on behind the wood"
  - Paraphrase: modern software education over-focuses on frameworks and abstractions and under-teaches how systems actually work (memory, concurrency, performance, tradeoffs); learning Rust forces students to confront ownership, memory, and error handling directly, concepts other languages abstract away

## Question `test-via-real-entry-point`

Should tests go through the production entry point, or through internal methods?

Positions:
- `test-via-real-entry-point--p1`: Test via real entry point
- `test-via-real-entry-point--p2`: Entry point testing plus fallible conversion audit

Claims:
- `a-sa13-f004772-c4` · Voice: SomeoneToIgnore · Source: https://github.com/zed-industries/zed/pull/58618 (`f004772`) · Date: 2026-08-07 · Locator: comment @SomeoneToIgnore 2026-08-07T22:48:19Z
  - Quote: "nothing tests the actual gesture: the toggle/switch tests drive the methods directly, the deferred up-out path itself has zero coverage."
  - Paraphrase: notes that even after a gesture-handling fix, "nothing tests the actual gesture" — the toggle/switch tests still drive the methods directly rather than the deferred mouse-event path itself
- `a-sa13-f004772-c3` · Voice: SomeoneToIgnore · Source: https://github.com/zed-industries/zed/pull/58618 (`f004772`) · Date: 2026-08-06 · Locator: comment @SomeoneToIgnore 2026-08-06T16:39:43Z
  - Quote: "At least one test should dispatch editor::OpenBreadcrumbs via a keystroke against the real strip."
  - Paraphrase: objects that tests drive the navigation/re-anchoring functions as plain method calls against a bespoke harness, so they would keep passing even if the real keybinding wiring broke; wants at least one test to dispatch the actual action via a keystroke against the real strip
- `b-bk03-f000267-c15` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Refactoring Consensus-Critical Code (full page)
  - Quote: "The dangerous bugs are not in the new code: they are in what the old code used to do that nothing does anymore."
  - Paraphrase: when a refactor moves or replaces code that enforces consensus rules, a check can silently stop being enforced without any test failing and without a diff showing a deleted check, because the danger is in what the old code used to do that nothing does anymore; the guide requires inventorying every rejection the old code could produce and naming its new home, testing every parse-time rejection through the actual production entry point rather than only through the check's own unit tests, and individually auditing fallible conversions (.ok(), unwrap_or, defaulted try_from) that could silently turn an invalid wire value into one a check treats as benign — citing two real incidents (#10461, #11386) where this exact failure mode slipped through with green CI

## Question `threads-vs-simd-for-batch-work`

When batch-hashing many small blobs (or a similar compute-bound batch workload), should you use thread-level parallelism (rayon), instruction-level parallelism (SIMD), or both, and when does each apply?

Positions:
- `threads-vs-simd-for-batch-work--p1`: Simd for small batches combine with threads for large batches
- `threads-vs-simd-for-batch-work--alt1`: Thread-level parallelism (rayon) only
- `threads-vs-simd-for-batch-work--alt2`: SIMD only

Claims:
- `b-sR08-f003702-c1` · Voice: Rüdiger Klaehn · Source: https://iroh.computer/blog/hashing-multiple-blobs-with-BLAKE3 (`f003702`) · Date: 2025-10-15 · Locator: § "Combining instruction level parallelism and thread level parallelism"
  - Quote: "Instruction level parallelism alone is frequently a good choice if you have a small batch of blobs to hash. You get a decent speed up but only use one CPU, and don't affect other parts of your program... For peak performance we can combine instruction level parallelism and thread level parallelism."
  - Paraphrase: SIMD alone is a good choice for a small batch — decent speedup, stays on one core, doesn't disturb the rest of the program — but for a large batch where the whole machine is available, combining SIMD with rayon's thread-level parallelism gives peak throughput (measured 17x over sequential, 2.1x over rayon alone).

## Question `tiered-checked-unchecked-apis`

Should a high-performance Rust client API expose multiple tiers of the same builder operation — an unchecked/positional fast path alongside a checked/named-field safe path — rather than one safe-by-default interface?

Positions:
- `tiered-checked-unchecked-apis--p1`: Offer tiered apis
- `tiered-checked-unchecked-apis--alt1`: One safe-by-default interface

Claims:
- `a-sR16-f012642-c1` · Voice: Jiachun Feng (Co-Founder, Greptime) · Source: https://greptime.com/blogs/2025-07-30-greptimedb-rust-guide-bulk-stream-insert (`f012642`) · Date: 2025-07-30 · Locator: § "Three Insert Approaches"
  - Quote: "Fast API: Best performance, positional values / Safe API: Validates field names / Indexed API: Uses index for balance of safety and speed"
  - Paraphrase: the bulk-stream row builder deliberately exposes three ways to build the same row — a positional "Fast API" for best performance, a "Safe API" that validates field names, and an "Indexed API" balancing the two — so callers pick their own safety/performance tradeoff rather than the crate picking one for them

## Question `timer-instant-overflow-panic`

When a scheduled timer/interval's next wake time would overflow the maximum representable `Instant`, should the runtime panic or silently never become ready again?

Positions:
- `timer-instant-overflow-panic--p1`: Panic on overflow
- `timer-instant-overflow-panic--p2`: Never ready without panic

Claims:
- `a-sa19-f009196-c5` · Voice: kevincox · Source: https://internals.rust-lang.org/t/instant-systemtime-min-max/21375 (`f009196`) · Date: 2024-08-17 · Locator: reply, 2024-08-17T19:19:10.352Z
  - Quote: "Panic if Instant::now reaches Instant::MAX... you never run a timer too early but you also don't panic upfront."
  - Paraphrase: Argues the best behaviour is to keep a sleeping future alive but never fire it early, panicking only in the extremely unlikely case that Instant::now itself reaches Instant::MAX, since no reasonable behaviour exists past that point.
- `a-sa19-f009196-c6` · Voice: bjorn3 · Source: https://internals.rust-lang.org/t/instant-systemtime-min-max/21375 (`f009196`) · Date: 2024-08-17 · Locator: reply, 2024-08-17T18:40:14.074Z
  - Quote: "The only options are to panic or have the future never be ready ever again."
  - Paraphrase: Criticizes Tokio's existing `far_future()` hack (used in `Interval::poll_tick`) as unnecessary; when a period is too large or the clock is nearly exhausted, the correct behaviour is to never register the future as ready again, not to wait based on a MAX-derived time that undershoots.

## Question `tokio-as-default-runtime`

Tokio as the default async runtime, or alternatives?

Positions:
- `tokio-as-default-runtime--tokio-default`: Tokio
- `tokio-as-default-runtime--p1`: Tokio as default runtime
- `tokio-as-default-runtime--p2`: No official recommendation, list options neutrally

Claims:
- `b-sb17-f005159-c1` · Voice: Rüdiger Klaehn · Source: https://iroh.computer/blog/async-rust-challenges-in-iroh (`f005159`) · Date: 2024-07-31 · Locator: article body, "Choosing a Runtime" section
  - Quote: "Although there are criticisms of Tokio, the alternatives are limited... Consequently, Tokio remains the best option for iroh."
  - Paraphrase: despite criticisms of Tokio, judges the alternatives (async-std stale, smol inactive, glommio Linux-only) too limited, and picks Tokio as iroh's runtime, reinforced by it being quinn's default
- `b-bk01-f000233-c3` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "Async and Await" § The runtime
  - Quote: "It's a general purpose runtime and is the most popular runtime in the ecosystem."
  - Paraphrase: recommends Tokio as the runtime for most of the guide because it is general purpose, the most popular in the ecosystem, and good for both getting started and production; notes other runtimes may give better performance or simpler code in some circumstances.
- `b-bk01-f000233-c4` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "The Async Ecosystem" § Popular Async Runtimes
  - Quote: "There is no asynchronous runtime in the standard library, and none are officially recommended."
  - Paraphrase: states flatly that no runtime is officially recommended and lists Tokio, async-std, smol and fuchsia-async as options without ranking them, then discusses cross-runtime incompatibility (Tokio's mio-based reactor and its own AsyncRead/AsyncWrite are not directly compatible with async-std/smol, which use the async-executor crate and futures' I/O traits) as a reason to research fit before committing. Flagged as an internal conflict: this contradicts this same source's earlier, newer chapter recommending Tokio by name as the default (see the Tokio-as-default Claim above) — the book's own top-of-page notice that it is "currently undergoing a rewrite" and that the `print.html` output concatenates old and new chapters is the likely mechanism (see this section's Coverage note).
- `a-sa29-f012940-c2` · Voice: Dhruv Ahuja · Source: https://signoz.io/blog/opentelemetry-rust (`f012940`) · Date: 2026-03-11 · Locator: section "Powered by Tokio"
  - Quote: "Tokio, which is often regarded as the one true async runtime, and powers much of Rust's networking ecosystem"
  - Paraphrase: describes the demo's web server and telemetry layer as built on Tokio, characterizing it as "often regarded as the one true async runtime" and the power behind much of Rust's networking ecosystem, without naming or engaging any specific alternative-runtime advocate

## Question `tokio-axum-vs-nginx-performance`

Is async Rust (Tokio-based web stacks) production-competitive with mature C-based servers like nginx "out of the box," or does the higher-level framework layer (e.g. Axum) add meaningful overhead that needs bypassing for performance?

Positions:
- `tokio-axum-vs-nginx-performance--p1`: Nginx's tuning advantage isn't matched by async Rust out of the box
- `tokio-axum-vs-nginx-performance--p2`: Tokio competitive out of the box
- `tokio-axum-vs-nginx-performance--p3`: Axum framework overhead hurts raw performance

Claims:
- `a-saL1-f005360-c7` · Voice: kornel · Source: https://lobste.rs/s/r1wrt6 (`f005360`) · Date: 2024-10-13 · Locator: reply, 2024-10-13T08:05:40-05:00
  - Quote: "Cloudflare has replaced nginx with tokio-based Pingora. Tokio is pretty fast out of the box, and Rust's async has been designed from the ground up to be very low overhead."
  - Paraphrase: Points to Cloudflare's production replacement of nginx with the Tokio-based Pingora proxy as evidence Tokio is fast out of the box and Rust's async was designed from the ground up for low overhead.
- `a-sa14-f005360-c5` · Voice: yawaramin · Source: https://lobste.rs/s/r1wrt6 (`f005360`) · Date: 2024-10-13 · Locator: comment 2024-10-13T05:36:31
  - Quote: "Difficult to see how that could be true since Nginx is highly-tuned async C++ and the async Rust is as is 'out of the box'."
  - Paraphrase: responds to a claim that async Rust should be competitive with nginx by pointing out nginx is highly-tuned async C++, while the compared Rust server is untuned "out of the box"
- `a-saL1-f005360-c8` · Voice: mattya · Source: https://lobste.rs/s/r1wrt6 (`f005360`) · Date: 2024-10-13 · Locator: reply, 2024-10-13T08:47:00-05:00
  - Quote: "Tokio and Hyper are both very fast, but this is using Axum which adds its own overhead... If you don't need complex path routing and 'extractors'... it's probably better to use Hyper and Tower directly."
  - Paraphrase: Distinguishes Tokio/Hyper (both very fast) from Axum, which adds its own routing/extractor overhead on top; recommends using Hyper and Tower directly when complex path routing isn't needed.
- `a-saL1-f005360-c9` · Voice: kornel · Source: https://lobste.rs/s/r1wrt6 (`f005360`) · Date: 2024-10-13 · Locator: reply, 2024-10-13T09:11:28-05:00
  - Quote: "Oh, that's disappointing. Actix-Web used to be a benchmark-topping framework while having routing and extractors, so I didn't expect Axum to differ much."
  - Paraphrase: Expresses surprise/disappointment at Axum's overhead, noting Actix-Web previously topped benchmarks while also providing routing and extractors, so he hadn't expected Axum to differ much.

## Question `totokens-intermediate-tokenstream`

In a `ToTokens` impl for a proc-macro AST enum, should each arm call `to_tokens` on the matched variant directly, or is it acceptable to build an intermediate `TokenStream` and feed it into the outer one?

Positions:
- `totokens-intermediate-tokenstream--p1`: Avoid building a temporary `TokenStream` in a `ToTokens` impl; match on the enum and call `to_tokens` on the matched arm directly
- `totokens-intermediate-tokenstream--alt1`: Build an intermediate `TokenStream`

Claims:
- `a-sR01-f000538-c1` · Voice: its-the-shrimp · Source: https://github.com/yewstack/yew/pull/3509 (`f000538`) · Date: 2025-05-04 · Locator: PR #3509, comment 2025-05-04T12:20:47Z
  - Quote: "to avoid allocating a temporary TokenStream just to feed it into another TokenStream"
  - Paraphrase: suggests rewriting the `impl ToTokens` so each match arm calls `to_tokens` on its inner value directly, rather than constructing a `TokenStream` from one variant and feeding it into another.

## Question `tower-middleware-vs-handler-helpers`

Cross-cutting concerns in a middleware or connection-hook layer, or per handler or protocol?

Positions:
- `tower-middleware-vs-handler-helpers--middleware-layer`: A middleware or connection-hook layer
- `tower-middleware-vs-handler-helpers--alt1`: Handle it per handler or per protocol (helpers, macros, per-protocol checks)

Claims:
- `a-sT08-f004169-c3` · Voice: ramfox · Source: https://iroh.computer/blog/iroh-0-96-0-the-quic-multipaths-to-1-0 (`f004169`) · Date: 2026-01-27 · Locator: § "Endpoint Hooks", `auth-hook` example paragraph and the paragraph after it
  - Quote: "individual protocols don't need to handle authentication themselves"
  - Paraphrase: an `EndpointHooks` trait intercepts connections before connect and after handshake, so authentication, authorization, rate limiting and observability sit at the connection layer and individual protocols stay on their core logic instead of each handling auth
- `b-sb22-f008906-c1` · Voice: Luciano Mammino · Source: https://loige.co/writing-middlewares-for-rust-lambda-functions (`f008906`) · Date: 2026-05-03 · Locator: section "Does this pattern make sense in Rust?"
  - Quote: "None of them quite match the convenience and composability of a real middleware stack, though."
  - Paraphrase: almost every Rust Lambda codebase reviewed in the last year bolts logging/auth/validation directly into the handler, sometimes via clever helpers, macros or trait extensions, none of which quite match the convenience and composability of the middleware engine already built into `aws-lambda-rust-runtime` via tower

## Question `trace-context-propagation-mechanism`

For propagating distributed-trace context (W3C trace-context HTTP headers) across a network boundary without modifying application code, should you use library interposition (`LD_PRELOAD` hijacking libcurl/libssl calls) or an eBPF-based mechanism (kernel-level header injection)?

Positions:
- `trace-context-propagation-mechanism--p1`: No fully good solution yet
- `trace-context-propagation-mechanism--alt1`: Library interposition (`LD_PRELOAD`)
- `trace-context-propagation-mechanism--alt2`: eBPF-based header injection

Claims:
- `b-sb24-f011306-c3` · Voice: Lalit Basin · Source: https://youtube.com/watch?v=OWCj8mDbAXc (`f011306`) · Date: 2025-10-03 · Locator: [32:45]-[36:51]
  - Quote: "there is no one all good solution uh as of now for context propagation in the dist distributed scenarios."
  - Paraphrase: injecting a new HTTP header for trace-context propagation from eBPF has no clean solution today — the kernel function that could write into user-space memory (`bpf_probe_write_user`) was locked down in August 2021 over security concerns, and its replacement (BPF arena, shared memory) zero-initializes on load and can crash the user-space program if headers were already allocated there; the traditional non-eBPF alternative, library interposition via `LD_PRELOAD` on libcurl/libssl, works well but becomes messy when those libraries are statically linked into the application

## Question `tracing-crate-vs-otel-api`

For distributed tracing in Rust, should the ecosystem standardize on the widely-adopted `tracing` crate (Tokio's tracing API), on the OpenTelemetry-spec-compliant tracing API, or keep maintaining both with improved interop?

Positions:
- `tracing-crate-vs-otel-api--p1`: Keep both with better interop for now
- `tracing-crate-vs-otel-api--alt1`: Standardize on the `tracing` crate
- `tracing-crate-vs-otel-api--alt2`: standardize on the OpenTelemetry API

Claims:
- `b-sb24-f011306-c1` · Voice: Lalit Basin · Source: https://youtube.com/watch?v=OWCj8mDbAXc (`f011306`) · Date: 2025-10-03 · Locator: [06:14]-[08:14]
  - Quote: "the community has been debating how how to really interrop with both these APIs whether we should drop one of them or whether we should continue using both of them... currently the state is that uh both practical path is to keep both of them active and running and provide an improved interoperability across both of them."
  - Paraphrase: the Tokio `tracing` crate is widely adopted but not fully suited to distributed tracing, while the OpenTelemetry tracing API is spec-compliant but far less adopted; the community has debated dropping one, but the current practical (and still unstable) path is to keep both and improve interop between them

## Question `tracing-vs-log-for-otel`

For a new Rust application adopting OpenTelemetry, should the logging facade be the span-native `tracing` crate, or a conventional logging crate bridged into OpenTelemetry later?

Positions:
- `tracing-vs-log-for-otel--p1`: Use the `tracing` crate, not a conventional logging crate, as the logging facade for a new Rust app that will adopt OpenTelemetry
- `tracing-vs-log-for-otel--alt1`: A conventional logging crate bridged into OpenTelemetry

Claims:
- `a-sa29-f012940-c1` · Voice: Dhruv Ahuja · Source: https://signoz.io/blog/opentelemetry-rust (`f012940`) · Date: 2026-03-11 · Locator: section "State of Logging and OpenTelemetry"
  - Quote: "the project recommends using tracing for new Rust applications"
  - Paraphrase: notes the OpenTelemetry Rust project bridges existing loggers (rather than mandating its own API) but recommends `tracing` for new applications because its Span concept aligns with OTel spans; the demo app follows this, using `tracing` throughout instead of a plain logging crate

## Question `trait-api-forced-arc-self`

should a public trait's methods require callers to wrap `self` in `Arc` (shared ownership baked into the API), or accept a plain reference/generic `Self` and leave ownership to the caller?

Positions:
- `trait-api-forced-arc-self--p1`: Drop the forced `Arc` requirement from `ProtocolHandler` for a more flexible structure
- `trait-api-forced-arc-self--alt1`: Require `Arc<Self>` in the trait's methods

Claims:
- `b-sR05-f002453-c2` · Voice: dignifiedquire · Source: https://iroh.computer/blog/iroh-0-30-0-slimming-down (`f002453`) · Date: 2024-12-17 · Locator: iroh.computer/blog/iroh-0-30-0-slimming-down, "Simpler ProtocolHandler API" section. · L2098-L2100.
  - Quote: "Previously the `ProtocolHandler` trait required using explicit Arcs, but this is no longer required, allowing for a more flexible structure in defining protocols."
  - Paraphrase: drop the forced `Arc` requirement from `ProtocolHandler` for a more flexible structure.

## Question `trait-default-methods-vs-major-bump`

When adding new methods to a public trait, should you give them default implementations to avoid a breaking change, or bump the major version?

Positions:
- `trait-default-methods-vs-major-bump--p1`: Default impls to avoid breaking change
- `trait-default-methods-vs-major-bump--alt1`: Bump the major version

Claims:
- `b-sR08-f003540-c1` · Voice: milenkovicm · Source: https://github.com/apache/datafusion/issues/17594 (`f003540`) · Date: 2025-09-19 · Locator: issue comment, 2025-09-19T15:47:59Z
  - Quote: "I have provided default implementation for those two methods for now, so they do not trigger backward incompatible change. will revert them back to unmplemented methods for df 51 release"
  - Paraphrase: added default implementations for two new `FunctionRegistry` trait methods so they would not trigger a backward-incompatible change in the 50.1.0 minor release, planning to make them required (unimplemented) only in the next major version.
- `b-sR08-f003540-c2` · Voice: alamb · Source: https://github.com/apache/datafusion/issues/17594 (`f003540`) · Date: 2025-09-18 · Locator: issue comment, 2025-09-18T18:04:21Z
  - Quote: "I think adding two new methods and releasing `50.1.0` sounds good to me"
  - Paraphrase: endorses adding the two new trait methods and shipping them in the 50.1.0 minor release rather than waiting for a major version bump.

## Question `trait-error-open-custom-variant`

Should a public trait's associated error type be a closed, fully-enumerated set of variants, or include an open "custom"/user-extension variant so third-party implementors can propagate their own errors?

Positions:
- `trait-error-open-custom-variant--p1`: Give public-trait errors an open Custom/User variant
- `trait-error-open-custom-variant--alt1`: A closed, fully enumerated error type

Claims:
- `a-sa14-f005149-c3` · Voice: dig, b5, and ramfox (iroh team) · Source: https://iroh.computer/blog/error-handling-in-iroh (`f005149`) · Date: 2025-08-22 · Locator: § Concrete-error writing guidelines / Errors for public traits should contain a Custom variant
  - Quote: "for traits that folks working with iroh can implement themselves, we needed to ensure that they could use the errors associated with that trait for their own purposes"
  - Paraphrase: for traits users can implement themselves (e.g. `Discovery`), the associated error type includes a `User` variant plus `from_err`/`from_err_box` helpers so implementors can propagate their own errors rather than being boxed into the crate's own failure modes

## Question `trait-impl-boilerplate-mechanism`

How should Rust reduce boilerplate for simple trait implementations — new dedicated impl syntax, compiler-inferred associated types, or ecosystem derive-macro crates?

Positions:
- `trait-impl-boilerplate-mechanism--p1`: New impl shorthand syntax
- `trait-impl-boilerplate-mechanism--p2`: Infer associated types

Claims:
- `a-sa19-f009292-c7` · Voice: zackw · Source: https://internals.rust-lang.org/t/pre-rfc-derive-support-for-arithmetic-traits-add-sub-mul-div-on-structs/23482 (`f009292`) · Date: 2025-09-08 · Locator: reply, 2025-09-08T15:59:48.016Z
  - Quote: "I wonder if we could come up with a generalization of this macro that would be suitable as official syntactic sugar."
  - Paraphrase: Proposes syntactic sugar such as `impl Display (self, f) for Type { ... }` for traits with exactly one required method, removing an indentation level and the need to look up the method's exact signature, beyond what derive alone offers.
- `a-sa19-f009292-c8` · Voice: scottmcm · Source: https://internals.rust-lang.org/t/pre-rfc-derive-support-for-arithmetic-traits-add-sub-mul-div-on-structs/23482 (`f009292`) · Date: 2025-09-08 · Locator: reply, 2025-09-08T23:27:35.279Z
  - Quote: "there's really no need... for me to have to write the type Item = i32; because it's the only possible thing given that next."
  - Paraphrase: Rather than new impl syntax, wants the compiler to infer associated types (e.g. `Iterator::Item`) from the method body, which would simplify implementing Add, Sub, IntoIterator and Deref without adding new surface syntax.

## Question `traits-as-inheritance-substitute`

Is Rust's trait-based supertrait/subtrait polymorphism (no class inheritance) an adequate, ergonomic substitute for OOP-style inheritance, or does the required generic/trait-bound plumbing make it more verbose and confusing than an inheritance-based language?

Positions:
- `traits-as-inheritance-substitute--p1`: Adequate but more verbose
- `traits-as-inheritance-substitute--alt1`: Traits are an inadequate substitute for inheritance

Claims:
- `a-sR16-f012428-c1` · Voice: Nas (CEO/founder Rebel, author developerlife.com, maintainer of Rebel's Dewey crates) · Source: https://youtube.com/watch?v=K5SY-lc8nTE (`f012428`) · Date: 2025-03-26 · Locator: video ~[34:17]-[35:17]
  - Quote: "arguably it's more verbose and somewhat confusing especially if you're coming from something like cotlin or java or typescript"
  - Paraphrase: modeling an OOP-style view/component hierarchy in Rust via supertrait/subtrait relationships (rather than inheritance) works, but doing it generically over the inner-storage type is a lot more work and, in his words, more verbose and confusing than the equivalent in Kotlin, Java or TypeScript

## Question `trust-microbenchmarks`

How far to trust microbenchmarks?

Positions:
- `trust-microbenchmarks--distrust-by-default`: Distrust by default
- `trust-microbenchmarks--alt1`: Microbenchmarks can be trusted at face value

Claims:
- `a-sa28-f012469-c2` · Voice: bstrie (attribution hedged by the poster themselves: "I'm pretty sure it's @bstrie") · Source: https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (`f012469`) · Date: 2015-07-17 · Locator: post by @carols10cents dated 2015-07-17T01:06:52Z, citing "33:52 of Rusty Radio Episode 2"
  - Quote: "I know that benchmarks are, always, generally, dangerous to quote because they're a special type of lie"
  - Paraphrase: benchmarks are a special category of lie, always risky to cite
- `a-sa25-f011413-c6` · Voice: Amos (fasterthanlime) · Source: https://youtube.com/watch?v=11m5HRMvPmU (`f011413`) · Date: 2026-06-11 · Locator: ~00:19:41–00:20:16
  - Quote: "microbenchmarks are always lies... Canada is a lie. Not the country, the benchmark."
  - Paraphrase: his own "Canada" benchmark against serde_json is not apples-to-apples because it skips serde's precise floating-point rounding mode; he states microbenchmarks, especially conference ones given without a right of reply, should be treated as suspect by default
- `a-sa28-f012469-c1` · Voice: kibwen · Source: https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (`f012469`) · Date: 2015-06-06 · Locator: post by @llogiq dated 2015-06-06T16:29:42Z, sourced "on /r/rust"
  - Quote: "I'm morally opposed to microbenchmarks and think they should all be consumed by gaping fissures in the earth's crust"
  - Paraphrase: declares blanket moral opposition to microbenchmarks

## Question `typed-response-struct-vs-untyped-value`

Should a Rust service handler return a typed, `serde::Serialize` response struct or an untyped `serde_json::Value`?

Positions:
- `typed-response-struct-vs-untyped-value--p1`: Typed response struct
- `typed-response-struct-vs-untyped-value--alt1`: An untyped `serde_json::Value`

Claims:
- `a-sT11-f007659-c3` · Voice: maahl (maahl.net) · Source: https://maahl.net/blog/rust-aws-lambda (`f007659`) · Date: 2023-11-05 · Locator: § "A more structured response"
  - Quote: "We can, however, leverage Rust's strong typing to do the work for us."
  - Paraphrase: replaces untyped JSON output with a `Serialize` struct so the compiler validates the response shape

## Question `typed-wrapper-vs-raw-access`

Should low-level data (registers, byte stores, raw matrices) be accessed through typed wrappers or accessors, or raw?

Positions:
- `typed-wrapper-vs-raw-access--encode-in-types`: Encode it in types
- `typed-wrapper-vs-raw-access--p1`: Dedicated types recommended over raw matrices
- `typed-wrapper-vs-raw-access--p2`: Typed wrapper over raw api

Claims:
- `b-bk03-f000267-c8` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Zebra Cached State Database Implementation § Adding a Column Family
  - Quote: "If we type the column family name out every time, a typo can lead to a panic, because the column family doesn't exist."
  - Paraphrase: most column families could be accessed with low-level methods taking any type, but that is error-prone (wrong types on read vs write, a typo'd column-family-name string causing a panic); instead, define the name and type of each column family once, add a typed method that returns that type, and route every read/write through it
- `a-sa09-f004055-c1` · Voice: jamesmunns · Source: https://github.com/embassy-rs/embassy/pull/5175 (`f004055`) · Date: 2026-01-05 · Locator: comment @jamesmunns 2026-01-05T14:14:27Z
  - Quote: "Why use raw volatile ops here instead of PAC operations?"
  - Paraphrase: repeatedly questions raw volatile register operations in favor of PAC-generated typed accessors
- `a-sB01-f000217-c2` · Voice: Dimforge (nalgebra maintainers) · Source: https://nalgebra.org/docs (`f000217`) · Date: capture 2025-01-21 (Wayback; underlying doc undated) · Locator: "Computer-graphics recipes" chapter, "Transformations using Matrix4"
  - Quote: "That's why all the transformation types are recommended instead of raw matrices."
  - Paraphrase: Argues a raw Matrix4 cannot guarantee it represents a pure rotation, isometry, or even an invertible transform, so dedicated transformation types are recommended instead
- `a-sa09-f004055-c2` · Voice: felipebalbi · Source: https://github.com/embassy-rs/embassy/pull/5175 (`f004055`) · Date: 2026-01-07 · Locator: comment @felipebalbi 2026-01-07T19:35:31Z
  - Quote: "PAC gives you accessors for these bits, if it doesn't, let me know so we can patch the PAC as that would be a bug."
  - Paraphrase: treats a missing PAC accessor as a bug to be fixed in the PAC itself rather than worked around with manual bit ops

## Question `typestate-crypto-keys`

For security-critical code handling cryptographic keys, should key roles and verification status be encoded as distinct types checked at compile time (the typestate pattern), rather than checked with runtime assertions?

Positions:
- `typestate-crypto-keys--p1`: Yes use typestate for keys
- `typestate-crypto-keys--alt1`: Runtime assertions

Claims:
- `b-sb24-f011295-c2` · Voice: Sam Cutter · Source: https://youtube.com/watch?v=8n13Oh8c0r4 (`f011295`) · Date: 2025-10-03 · Locator: [17:10]-[21:12]
  - Quote: "Types give us superpowers. They allow us to encode the rules of our system in a way that can be checked compile time, helping prevent mistakes."
  - Paraphrase: cryptographic keys are given a `Role` marker type and a verified/unverified type-state, so that e.g. passing a cover-node provisioning key where a journalist-provisioning key is required fails to compile, and an unverified key cannot be used for cryptographic operations until explicitly checked

## Question `typestate-generic-vs-separate-types`

Should a Rust API express protocol states as one generic type with a typestate parameter (`Connection<T>`), or as separate concrete types per state?

Positions:
- `typestate-generic-vs-separate-types--p1`: Unified generic typestate
- `typestate-generic-vs-separate-types--alt1`: Separate concrete types per state

Claims:
- `a-sT08-f004169-c1` · Voice: ramfox · Source: https://iroh.computer/blog/iroh-0-96-0-the-quic-multipaths-to-1-0 (`f004169`) · Date: 2026-01-27 · Locator: § "0-RTT and the Connection API changes"
  - Quote: "we've de-duplicated a bunch of code that was the same over the three different variaties of connections"
  - Paraphrase: separate `OutgoingZeroRttConnection` and `IncomingZeroRttConnection` structs duplicated the whole connection API and stopped 0-RTT connections sharing code paths; a single `Connection<T>` with a state parameter restores that flexibility and de-duplicates the code, with state-specific signatures only where authentication differs
