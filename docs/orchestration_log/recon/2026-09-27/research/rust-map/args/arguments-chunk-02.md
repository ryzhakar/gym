## kernel-constants-hardcode-vs-comptime
### kernel-constants-hardcode-vs-comptime--hardcode-for-this-use
- for | For this particular pivot-replacement site, machine epsilon (`finfo().epsilon`) is the wrong semantic quantity regardless of dtype — it's still much larger than the small-scale pivot values that would get silently corrupted, so the exact-zero check should stay hardcoded rather than switch to a dtype-derived value. | values: correctness | sources: f004573@PR review comment, 2026-04-21T14:45:23Z
- against | Elsewhere in the same review, a generic accessor on the dtype's own precision metadata (`FloatDType::finfo()`) is called a strict improvement over hardcoded per-dtype constants — self-documenting, dtype-correct, and handling all float dtypes uniformly. | values: correctness, simplicity | sources: f004573@PR review comment, 2026-04-21T14:45:21Z

### kernel-constants-hardcode-vs-comptime--parameterize-constants
- for | Hardcode the values for now, but pass them to the kernel via a comptime struct, so a future backend-specific change (e.g. AMD's different warp/wavefront size) won't require touching the kernel body, only the launch. | values: iteration-speed | sources: f002048@tracel-ai/burn#2287, comment 2024-09-23T14:26:38Z. · L977-L979.
- for | A generic accessor on the dtype's own precision metadata (`FloatDType::finfo()`) is a strict improvement over hardcoded per-dtype epsilon constants — self-documenting, dtype-correct, and it handles Flex32 uniformly for free. | values: correctness, simplicity | sources: f004573@PR review comment, 2026-04-21T14:45:21Z
- against | For at least one specific pivot-replacement site, `finfo().epsilon` is the wrong semantic quantity regardless of dtype, so a generic dtype-derived constant isn't always the right replacement for a hardcoded one. | values: correctness | sources: f004573@PR review comment, 2026-04-21T14:45:23Z

## keyed-access-copy-vs-clone-keys
### keyed-access-copy-vs-clone-keys--p1
- for | Deliberately requiring `Copy` on keys stops users reaching for costlier `Clone` keys when a cheaper option exists. | values: performance | sources: f003963@PR description 2025-12-05T21:04:20Z
- against | Cheaply-clonable types like `Arc<str>` are reasonable to use as keys, so constraining to `Copy` alone excludes a legitimate, cheap case. | values: approachability | sources: f003963@comment @gbj 2025-12-12T20:04:23Z

### keyed-access-copy-vs-clone-keys--p2
- for | The trait should also accept `Clone` key types, since types like `Arc<str>` are cheap to clone and reasonable keys, even though cloning large objects generally is not. | values: approachability | sources: f003963@comment @gbj 2025-12-12T20:04:23Z
- against | Requiring `Copy` on keys is good practice because it stops users from reaching for `Clone` keys rather than a cheaper option when one is available. | values: performance | sources: f003963@PR description 2025-12-05T21:04:20Z

## lambda-vs-containers
### lambda-vs-containers--serverless-first
- for | After porting the same Rust web API and a Kafka-consuming background service from Fargate to Lambda, latency (p50/p99) held steady, memory usage dropped, cold starts were a rare minority of invocations, and the 24/7 idle container cost disappeared — concludes serverless should be reached for by default. | values: performance, value-candidate: cost-efficiency | sources: f011220@~38:52-39:58
- against | An app that runs 24/7 in production can be costly on Lambda but cheap on ECS/Fargate, so always-on production traffic is better run on containers even where serverless suits other environments. | values: value-candidate: cost-efficiency | sources: f007797@paragraph beginning "Lambda Web Adapter not only makes it easier..."

### lambda-vs-containers--split-by-workload
- for | An app that's costly to run 24/7 on Lambda but cheap on ECS/Fargate should split by workload: infrequent or test environments on serverless, always-on production traffic on containers — accepting a meaningful test/production infrastructure mismatch as a tradeoff worth the cost savings in some scenarios. | values: value-candidate: cost-efficiency | sources: f007797@paragraph beginning "Lambda Web Adapter not only makes it easier..."; f007797@closing paragraph, beginning "Lambda Web Adapter not only makes it easier"
- against | A real migration from an always-on container to Lambda showed steady latency, a fraction of the memory use, and cold starts as a small minority of invocations — serverless, not a split by workload, should be the default reach. | values: performance, value-candidate: cost-efficiency | sources: f011220@~38:52-39:58

## land-hal-separate-now-vs-unified-later
### land-hal-separate-now-vs-unified-later--p1
- for | Land previously private work upstreamed as a side crate as soon as possible, so an old siloed fork can be deprecated/archived, with a path to unifying into the shared HAL once that becomes possible now that the code lives in the same repo. | values: iteration-speed | sources: f003955@embassy-rs/embassy#4989, comment 2025-12-04T18:32:46Z. · L817-L820.
- against | no argument in sources

### land-hal-separate-now-vs-unified-later--p2
- for | Get the crate merged as-is now; once the shared metapac is ready, switch to it, and once the combined HAL is ready, deprecate this crate — a switch users won't find a big deal. | values: iteration-speed | sources: f003955@embassy-rs/embassy#4989, comment 2025-12-04T18:35:15Z. · L824-L827.
- against | no argument in sources

## language-safety-vs-hw-isolation
### language-safety-vs-hw-isolation--p1
- for | Rust protects a user from "holding it wrong" (accidental misuse), not from intentional, deliberate misuse — which is what real fine-grained security between mutually adversarial code would require. | values: correctness | sources: f005360@reply, 2024-10-15T10:57:36-05:00
- for | Language-level capabilities and effect systems can't solve multi-tenant isolation unless literally every piece of code sharing the address space is trusted, unsafe-forbidden Rust compiled by a trusted compiler — viable for a single-application unikernel, not for many mutually distrusting applications together. | values: correctness | sources: f005360@reply, 2024-10-15T13:39:05-05:00
- against | no argument in sources

### language-safety-vs-hw-isolation--p2
- no argument in sources

## library-auth-opinionated-vs-unopinionated
### library-auth-opinionated-vs-unopinionated--authenticated-managed-default
- for | An open relay's URL is a credential that ships in every client and leaks (visible to anyone watching a connection get established), so anyone who learns it can spend its finite bandwidth — which is why managed relays deployed from a given date onward require a signed, expiring, endpoint-bound token issued from the project's API key. | values: correctness, value-candidate: security | sources: f004960@intro ("we've decided that managed relays on Iroh Services are now authenticated by default") and "The problem: a relay URL is a credential you can't revoke"
- against | For self-run relays, the library itself stays unopinionated about authentication — operators can build their own scheme rather than being forced into the managed default. | values: approachability | sources: f004960@"The problem: a relay URL is a credential you can't revoke" section

### library-auth-opinionated-vs-unopinionated--unopinionated-library
- for | Self-run relays are untouched by the new policy — "iroh is unopinionated about that" — operators can build their own authentication scheme. | values: approachability | sources: f004960@"The problem: a relay URL is a credential you can't revoke" section
- against | A relay's URL is an unrevocable, leaking credential, and anyone who learns it can spend its finite bandwidth, which is why the managed service now defaults to authenticated, API-key-scoped tokens rather than leaving the choice fully open. | values: correctness, value-candidate: security | sources: f004960@intro ("we've decided that managed relays on Iroh Services are now authenticated by default") and "The problem: a relay URL is a credential you can't revoke"

## library-error-type-opaque-vs-typed
### library-error-type-opaque-vs-typed--concrete-typed-errors
- for | All public APIs should return concrete error types rather than `anyhow::Error`, even where this is a large change touching most of the codebase. | values: correctness | sources: f003188@"💥 Concrete Errors 💥" section / Breaking Changes list
- against | `thiserror`-style concrete errors currently only support the default `{}` Display format, which loses the full source-error chain, so a concrete type alone can lose logged context that an opaque wrapper (`anyhow`/`eyre`) would preserve. | values: correctness | sources: f008583@"Error logging" section

### library-error-type-opaque-vs-typed--hybrid-snafu
- for | After experimenting with both dominant approaches, settle on `snafu` because it gives enum-based precision like `thiserror` plus automatic backtrace and span-trace capture per variant, working around the `Into`-trait conflict that otherwise forces a choice between ergonomic `?` and backtraces. | values: correctness, approachability | sources: f005149@"Enter Snafu: The Hybrid Approach"; f003222@"Errors" section
- against | `thiserror`-based concrete errors currently only support the default `{}` Display format, losing the full source-error chain, so the workaround many reach for is wrapping in an opaque `anyhow`/`eyre` type instead of a hybrid concrete+backtrace crate. | values: correctness | sources: f008583@"Error logging" section

### library-error-type-opaque-vs-typed--typed-over-time
- for | Having started out happily using `anyhow` for many things, structured typed error handling proved far more valuable as the project matured, while `anyhow` is still kept for some things. | values: correctness | sources: f011092@~00:48:46 (Q&A)
- against | `thiserror`-style typed errors currently only support the default `{}` Display format, which loses the full source-error chain for logging, so an opaque wrapper (`anyhow`/`eyre`) is still needed to preserve context even after typed errors mature. | values: correctness | sources: f008583@"Error logging" section

### library-error-type-opaque-vs-typed--wrap-in-anyhow-for-context
- for | `thiserror` currently only supports the default `{}` Display format, which loses the full source-error chain (e.g. an AWS SDK `Unhandled` variant losing the underlying resource info); the workaround is to wrap typed errors in `anyhow` or `eyre`, which support the alternate `{:#}` display that preserves context. | values: correctness | sources: f008583@"Error logging" section
- against | All public APIs should return concrete, enumerable error types rather than being wrapped in an opaque `anyhow::Error`. | values: correctness | sources: f003188@"💥 Concrete Errors 💥" section / Breaking Changes list

## library-io-factored-out
### library-io-factored-out--p2
- for | Since spawning threads panics on `wasm32-unknown-unknown`, a portable library should factor thread spawning out to the caller — "bring their own threads" — the same way it factors out I/O, which also plays nicer with apps that own a custom thread pool. | values: approachability | sources: f000256@§ "How to Add WebAssembly Support to a General-Purpose Crate" — "Avoid Spawning Threads"
- against | no argument in sources

### library-io-factored-out--p3
- for | Since the Web has no filesystem and I/O there is always asynchronous, a portable library should factor I/O out of itself entirely, taking input slices from callers rather than reading files or performing I/O directly. | values: approachability | sources: f000256@§ "How to Add WebAssembly Support to a General-Purpose Crate" — "Avoid Performing I/O Directly"
- against | no argument in sources

## library-panic
### library-panic--never-panic-return-result
- for | Questions why a memory-transfer function was made `unsafe` with an `assert` reintroduced in place of a `Result`; proposes a fallible `try_` variant with a panicking convenience wrapper on top instead. | values: correctness | sources: f004055@comment @jamesmunns 2026-01-05T14:16:51Z
- for | Rhai treats any panic reaching the host application as a bug in Rhai itself, not an acceptable outcome, and is coded under that "Don't Panic" guarantee. | values: correctness, stability | sources: f005421@README section "Protected against attacks", sub-item "_Don't Panic_ guarantee"
- for | Constructors should return `Result` rather than `unwrap`/panic internally. | values: correctness | sources: f001512@comment 2024-06-11T10:24:37Z
- against | A panic path can be acceptable as long as it's listed in the function's `# Panics` documentation, so a user isn't surprised by hitting it. | values: approachability | sources: f004573@PR review comment, 2026-04-21T14:39:58Z

### library-panic--no-ad-hoc-panics
- for | Ad hoc panics used as a short-circuit bail-out are bad practice; panics should be reserved for cases genuinely tied to control flow — while allowing that other Rust practitioners may disagree. | values: correctness | sources: f011069@~00:32:20-00:32:40
- against | no argument in sources

### library-panic--panic-fine-if-documented
- for | A panic path can be acceptable as long as it is listed in the function's `# Panics` documentation, so a user isn't surprised by hitting it. | values: approachability | sources: f004573@PR review comment, 2026-04-21T14:39:58Z
- against | Any panic reaching the host application should be treated as a bug, not something merely to document and accept. | values: correctness, stability | sources: f005421@README section "Protected against attacks", sub-item "_Don't Panic_ guarantee"

### library-panic--prevent-via-explicit-check
- no argument in sources

### library-panic--unwrap-only-in-tests
- for | New `unwrap()`s should be early returns instead; `unwrap` is acceptable only in tests, or where reading the current function shows a panic can never actually occur. | values: correctness | sources: f003414@comment 2025-10-28T01:59:12Z
- against | no argument in sources

## lifetimes-on-structs
### lifetimes-on-structs--borrow-for-measured-performance
- for | Converting a value type from owned (hashmap-based) to borrowed, with `Cow`-like borrowed/owned variants, was the key change that brought an evaluation within ~10ns of native code, down from 147ns for the original owned implementation. | values: performance | sources: f007364@section "References#" preceded by "Native types in CEL#" and "References#"
- against | A good rule of thumb, once you get stuck fighting the borrow checker, is to avoid putting lifetime parameters on structs at all. | values: simplicity | sources: f007608@footnote to the paragraph beginning "Playing with these examples is educational" in section "Part Two: Borrowing"

### lifetimes-on-structs--owned-by-default
- for | While experimenting with borrow-checker fights builds useful intuition, the actionable rule of thumb when stuck is to keep lifetime parameters off struct definitions. | values: simplicity | sources: f007608@footnote to the paragraph beginning "Playing with these examples is educational" in section "Part Two: Borrowing"
- against | Converting an owned struct to a borrowed one (lifetime parameters, `Cow`-like variants) was the key change that brought performance within ~10ns of native code, versus 147ns owned. | values: performance | sources: f007364@section "References#" preceded by "Native types in CEL#" and "References#"

## llm-doc-edits-reproducibility
### llm-doc-edits-reproducibility--p1
- for | Expects the doc-consistency effort to trigger bikeshedding, and hopes it results in additions to the project's developer guidelines that, among other things, help LLMs pre-review changes. | values: value-candidate: process-consistency | sources: f004997@PR description @bjoernQ 2026-08-11T12:34:57Z
- against | no argument in sources

### llm-doc-edits-reproducibility--p2
- for | Proposes mandating a standard like ASD-STE100 Simplified Technical English so the prose style stays consistent and free of "flowery nonsense." | values: value-candidate: process-consistency | sources: f004997@comment @bugadani 2026-08-11T12:39:59Z
- for | A controlled-language standard largely removes a model's "taste" from the equation on its own, by limiting vocabulary and grammar. | values: value-candidate: process-consistency | sources: f004997@comment @bugadani 2026-08-12T13:36:48Z
- against | Merging an LLM-driven doc pass requires declaring which model was used, since each model has its own "taste" regardless of a controlled-language standard, plus declaring the exact prompt and running in a clean environment. | values: value-candidate: reproducibility | sources: f004997@comment @MabezDev 2026-08-12T13:34:07Z

### llm-doc-edits-reproducibility--p3
- for | To merge this kind of LLM-driven doc pass, the project must declare which model was used (each model has its own "taste"), declare the exact prompt (wording changes results), and run the update in a clean environment to avoid picking up incidental local agent rules. | values: value-candidate: reproducibility | sources: f004997@comment @MabezDev 2026-08-12T13:34:07Z
- against | A controlled-vocabulary writing standard (ASD-STE100) removes a model's "taste" from the equation on its own, without needing to pin down model/prompt/environment. | values: value-candidate: process-consistency | sources: f004997@comment @bugadani 2026-08-12T13:36:48Z

## lts-release-channel
### lts-release-channel--support-old-lines
- for | A too-fast monthly release cadence forced users to track upstream closely for security fixes, so designated LTS releases now guarantee 24 months of API-compatible security patches (no backported features), letting users upgrade yearly instead of monthly while still receiving fixes. | values: stability | sources: f002937@"Wasmtime LTS Releases" article, paragraphs 2-4
- against | Rather than support an older version line, point users to the project's upgrade guide and decline applying the fix to it. | values: iteration-speed | sources: f002501@comment 2025-01-10T16:08:08Z

### lts-release-channel--upgrade-instead
- for | Declines applying a fix to an older version line, pointing instead to the project's upgrade guide. | values: iteration-speed | sources: f002501@comment 2025-01-10T16:08:08Z
- against | A too-fast release cadence should be answered with designated LTS releases carrying guaranteed multi-year API-compatible security patches, rather than requiring every user to upgrade. | values: stability | sources: f002937@"Wasmtime LTS Releases" article, paragraphs 2-4

## memory-safety-design-priority
### memory-safety-design-priority--p1
- no argument in sources

### memory-safety-design-priority--p2
- for | Reframes the "lopsided" critique as high praise: solving the hard part — memory management without a garbage collector — first gives a young language a great foundation, and the remaining capabilities (mainly easier/more powerful metaprogramming) are trusted to come in time. | values: correctness, performance | sources: f012469@same post as above, llogiq's own reply
- against | no argument in sources

## merge-expensive-feature-with-limits
### merge-expensive-feature-with-limits--p1
- for | Document the cost in the public API doc comment (exponential growth with width) rather than blocking the feature outright. | values: approachability | sources: f003126@comment @UkoeHB 2025-06-16T20:45:49Z
- against | Even with the batching fixes, most users won't read the docs closely enough to avoid the performance cliff, and the implementation still has visible artifact bugs under transform/rotation. | values: performance, correctness | sources: f003126@comment @ickshonpe 2025-06-19T09:25:27Z

### merge-expensive-feature-with-limits--p2
- for | Reluctant to merge something this slow and rough; even after batching improvements, remains negative because most users won't read the docs closely enough to avoid the performance cliff and visible artifact bugs, wanting a proper SDF-based solution instead. | values: performance, correctness | sources: f003126@comment @ickshonpe 2025-06-19T09:25:27Z; f003126@comment @alice-i-cecile 2025-06-19T00:58:08Z
- against | The cost can simply be documented in the public API doc comment rather than blocking the feature, so it can ship for the common case now. | values: approachability | sources: f003126@comment @UkoeHB 2025-06-16T20:45:49Z

## minimal-vs-batteries-std
### minimal-vs-batteries-std--p1
- for | Rust never aimed to be a "minimal" language, but a "medium sized" one — a middle point between a bare core and a fully batteries-included system. | values: simplicity | sources: f012469@post by @johansigfrids dated 2015-06-29T17:33:32Z, sourced "graydon2 on reddit"
- against | The stdlib's posture is "Buy Your Own Damn Batteries" — the deliberate opposite of Python's "batteries included." | values: simplicity | sources: f012469@post by @DanielKeep dated 2015-06-12T13:06:31Z

### minimal-vs-batteries-std--p2
- for | "Buy Your Own Damn Batteries" — frames Rust's stdlib philosophy as the deliberate opposite of Python's "batteries included." | values: simplicity | sources: f012469@post by @DanielKeep dated 2015-06-12T13:06:31Z
- against | Rust never set out to be minimal in the first place; the target was always "medium sized," not a bare core deferring everything to crates.io. | values: simplicity | sources: f012469@post by @johansigfrids dated 2015-06-29T17:33:32Z, sourced "graydon2 on reddit"

## mutex-vs-atomics
### mutex-vs-atomics--atomics-carry-own-bugs
- for | Pushes back that framing atomics/CAS as the safe alternative glosses over the fact that races (stale or inconsistent reads) are themselves a real bug class, not a lesser evil. | values: correctness | sources: f005600@lobste.rs/s/fzro7f, comment 2025-11-01T02:14:18-05:00
- against | Locks are "always a disaster waiting to happen" because something will eventually die holding one and the whole system grinds to a halt, whereas the worst case with atomics/CAS is livelock, which is rare and usually recovers. | values: stability, performance | sources: f005600@lobste.rs/s/fzro7f, comment 2025-11-01T01:54:49-05:00

### mutex-vs-atomics--atomics-over-locks
- for | Rejected a Mutex-guarded shared iterator for concurrent ID generation because it forces threads to wait on the lock; replaced it with a lock-free design (`RoaringBitmap::select` plus atomics) that lets threads proceed without synchronization. | values: performance | sources: f007846@§ "Sharing an Iterator Over the Available IDs" → § "The Final Solution"
- for | Atomics and compare-and-swap are fine — worst case is livelock, which is rare and usually recovers — while a lock is "always a disaster waiting to happen" because something will eventually die holding it; goes as far as calling the mere existence of a lock, even inside a library, always a programming bug. | values: stability, performance | sources: f005600@lobste.rs/s/fzro7f, comment 2025-11-01T01:54:49-05:00
- against | Framing atomics/CAS as the safe alternative glosses over the fact that races (stale or inconsistent reads) are themselves a real bug class, not a lesser evil. | values: correctness | sources: f005600@lobste.rs/s/fzro7f, comment 2025-11-01T02:14:18-05:00
- against | If there are many threads and heavy lock contention, move to lock-free structures; but if a lock is rarely contended, a normal mutex is simpler and just as good, since lock-free brings its own hazards like the ABA problem. | values: simplicity | sources: f011233@~29:29-30:32

### mutex-vs-atomics--mutex-unless-contended
- for | If there are many threads and heavy lock contention, move to lock-free data structures (crossbeam, parking_lot); if a lock is rarely contended, a normal mutex-based structure is simpler and just as good, because lock-free implementations bring their own hazards (e.g. the ABA problem). | values: simplicity, performance | sources: f011233@~29:29-30:32
- against | The existence of a lock is "always a programming bug even inside a library" — the worst case with atomics/CAS is a rare, recoverable livelock, versus a lock's potential to be held by something that dies, grinding the whole system to a halt. | values: stability, performance | sources: f005600@lobste.rs/s/fzro7f, comment 2025-11-01T01:54:49-05:00

## named-default-args-overloading
### named-default-args-overloading--named-parameters-only
- for | Named parameters could work for Rust — unlike optional/default arguments — but unresolved design problems remain: parameters are patterns not names, function-values erase parameter names, and reordering call-site arguments conflicts with left-to-right evaluation order. | values: correctness, approachability | sources: f009104@"I'm okay with named parameters now" section
- against | Rust should support built-in overloading today, especially for interop with existing languages, since it already fakes overloading inconsistently via trait dispatch. | values: approachability | sources: f011312@[28:38]-[30:39]

### named-default-args-overloading--overloading-for-interop
- for | Rust should support built-in overloading today, especially for interop with existing languages: C++ API maintainers rely on adding overloads without breaking existing callers, Rust already fakes overloading inconsistently via trait dispatch (multiple `From` impls, `Into`'s return-type-directed dispatch), and built-in overloading could also resolve an aliasing problem by letting the compiler pick a safe vs. unsafe overload based on the caller's reference. | values: approachability, correctness | sources: f011312@[28:38]-[30:39]
- against | Rust has for years opposed named parameters, optional/default arguments and overloading altogether, because the features are numerous and mutually entangled, and the current one-function-one-signature rule keeps the language simple at an acceptable cost. | values: simplicity | sources: f009104@"These features make me uneasy" section

### named-default-args-overloading--reject-all-for-simplicity
- for | Has for years opposed Rust adding named parameters, optional/default arguments and function overloading — all requested since at least a twelve-year-old GitHub issue — arguing the features are numerous and mutually entangled, and that Rust's current rule (one function, one signature; write a differently-named function or a builder for variants) keeps the language simple at an acceptable cost. | values: simplicity | sources: f009104@"These features make me uneasy" section
- against | Rust should support built-in overloading today, especially for interop with existing languages, since it already fakes overloading inconsistently via trait dispatch. | values: approachability | sources: f011312@[28:38]-[30:39]

## nightly-feature-autodetection
### nightly-feature-autodetection--p1
- for | Nightly features should be opt-in, not opt-out — that's how the entire Rust nightly feature system is designed; libraries auto-enabling features run counter to the Rust Project's own general principle that unstable features should only impact those who opted in. | values: correctness, stability | sources: f009343@reply, 2026-06-30T12:20:20.661Z; f009343@reply, 2026-06-29T17:46:02.300Z
- for | Wants to use nightly for unrelated ergonomic toolchain features while explicitly not consenting to dependencies silently using other unstable library or compiler features just because a nightly compiler was detected. | values: stability | sources: f009343@reply, 2026-06-29T15:30:35.384Z
- for | When switching to nightly for unrelated reasons, doesn't want dependencies to implicitly change behavior by using unstable features; any such blanket opt-in should be a separate, explicit flag, never implied by nightly usage alone. | values: stability | sources: f009343@reply, 2026-06-29T15:39:25.162Z
- against | Prefers a crate that documents clearly when it auto-detects and uses nightly features over one that requires going through manual opt-in flags, while acknowledging safety-critical users need a documented way to fully opt out. | values: approachability | sources: f009343@reply, 2026-06-29T17:48:03.889Z

### nightly-feature-autodetection--p2
- for | As an ergonomics-motivated developer, prefers a crate that documents clearly if it auto-detects and uses nightly features to one that requires going through manual opt-in flags, while acknowledging safety-critical users need a documented way to fully opt out. | values: approachability | sources: f009343@reply, 2026-06-29T17:48:03.889Z
- against | Nightly features should be opt-in, not opt-out; libraries auto-enabling features run counter to the Rust Project's own principle that unstable features only impact those who opted in, and harm nightly users who didn't consent to other unstable behavior silently changing. | values: correctness, stability | sources: f009343@reply, 2026-06-30T12:20:20.661Z; f009343@reply, 2026-06-29T17:46:02.300Z

## nightly-in-production
### nightly-in-production--nightly-when-it-pays
- for | Raw target-feature-gated intrinsics are unsafe, verbose, and need manual wrapping and runtime feature detection; `std::simd`'s portable_simd lets you write safe, ordinary iterator code the compiler lowers per architecture — "the choice," even though it currently requires nightly. | values: correctness, approachability | sources: f011233@~36:39-39:43
- against | The team does not, has not, and does not plan to rely on unstable Rust features; every foundational crate is published to crates.io with no unpublished dependencies. | values: stability | sources: f011092@~00:46:45-00:47:45 (Q&A)

### nightly-in-production--stable-only
- for | States plainly that the team does not, has not, and does not plan to rely on unstable Rust features, and that all their foundational crates are published to crates.io with no unpublished dependencies. | values: stability | sources: f011092@~00:46:45-00:47:45 (Q&A)
- against | Portable SIMD lets you write safe, ordinary-looking code the compiler lowers per architecture instead of unsafe, verbose, manually-wrapped target-feature intrinsics — recommended as "the choice" even though it currently requires nightly. | values: correctness, approachability | sources: f011233@~36:39-39:43

## optional-parameters-api-shape
### optional-parameters-api-shape--drop-feature-keep-signature-small
- for | Willing to merge a first version of the work without an extra feature (automatic BOM/encoding detection), choosing fewer arguments over including it. | values: simplicity | sources: f003414@comment 2025-09-12T19:43:46Z
- against | There are way too many constructors and not enough documentation, so trimming a feature to keep one signature small can still leave the overall API surface hard to understand. | values: approachability | sources: f001512@comment 2024-05-30T12:38:44Z

### optional-parameters-api-shape--many-constructors-criticized
- for | There are way too many constructors and not enough documentation. | values: approachability | sources: f001512@comment 2024-05-30T12:38:44Z
- against | Rather than multiplying constructors, route optional configuration through one entry point — e.g. everything through a config struct once a setting belongs to it. | values: simplicity | sources: f001512@comment 2024-06-11T10:22:55Z

### optional-parameters-api-shape--one-configurable-entry
- for | Rust has neither overloading nor default parameters, so each operation should expose one `_with_opts` method taking an Options struct (the closest mapping to the underlying protocol), plus convenience wrapper methods using `impl Into<T>` for common cases. | values: simplicity, approachability | sources: f003222@"Options" section
- for | Once a setting is part of the config, it should not be public as a separate method — everything should go through the config struct. | values: simplicity | sources: f001512@comment 2024-06-11T10:22:55Z
- for | A `ColorSpace` enum passed as a second constructor argument avoids multiplying method names for every source-type/color-space combination. | values: simplicity | sources: f000530@PR comment, mid-thread
- against | There are way too many constructors and not enough documentation, so a single option-bearing entry point doesn't by itself fix an unclear API. | values: approachability | sources: f001512@comment 2024-05-30T12:38:44Z

### optional-parameters-api-shape--separate-specialized-entries
- no argument in sources

## oss-reuse-attribution-norms
### oss-reuse-attribution-norms--coordination-and-credit-matter
- for | Taking a project's work wholesale and redistributing it without discussing it first is "bad form" even where the license permits it, because banners/brands carry the social and financial capital that sustains maintainers. | values: value-candidate: attribution-norms | sources: f003025@comment @cart 2025-06-01T22:35:03Z
- for | Copying, stripping, and renaming another team's code, then shopping it around for maintainers, without reaching out first, is disrespectful of the original authors' investment even where the license allows it. | values: value-candidate: attribution-norms | sources: f003025@comment @jkelleyrtp 2025-06-02T07:00:30Z
- for | Points out a function copy-pasted almost verbatim, bugs included, from a different open PR, and asks that a co-authored-by credit be added if code was really copied from it. | values: value-candidate: attribution-norms | sources: f004772@comment @SomeoneToIgnore 2026-08-02T15:31:14Z
- against | Producers of open source aren't entitled to anything, the same way consumers aren't either — forking and improving others' code is the real beauty of open source, a gift with no expectations. | values: value-candidate: attribution-norms | sources: f003025@comment @hecrj 2025-06-02T02:49:06Z

### oss-reuse-attribution-norms--no-entitlement
- for | Producers of open source are not entitled to control over branding or how their code is reused; forking and improving others' code is the essence of open source, not a breach of it. | values: value-candidate: attribution-norms | sources: f003025@comment @hecrj 2025-06-02T02:49:06Z
- against | Taking a project's work wholesale and redistributing it without discussing it first, or copying code without credit, is disrespectful of the original authors' investment and "bad form," even where the license allows it. | values: value-candidate: attribution-norms | sources: f003025@comment @cart 2025-06-01T22:35:03Z; f003025@comment @jkelleyrtp 2025-06-02T07:00:30Z

## plugin-system-mechanism
### plugin-system-mechanism--p1
- for | Native dynamic libraries have no stable ABI, offer no sandboxing (a buggy or malicious plugin can crash or compromise the host), and compiled-code distribution hides backdoors and is harder for users to audit than scripts. | values: correctness, stability, value-candidate: security | sources: f007483@§ Native Libraries
- against | Embedding a scripting language (QuickJS) is recommended over native dynamic libraries as the default plugin approach, for its small binary size, no JIT, faster cold starts, and easier integration. | values: performance, approachability | sources: f007483@§ Scripting language, closing paragraph

### plugin-system-mechanism--p2
- for | Recommends embedding QuickJS as the default approach for a Rust plugin system — over V8/deno_core and over Lua — citing small binary size, no JIT, faster cold starts, and easier integration; evaluate other methods only when QuickJS has too many drawbacks for the specific use case. | values: performance, approachability | sources: f007483@§ Scripting language, closing paragraph
- against | WebAssembly is currently too immature to be used for a plugin system despite its sandboxing strength, and an expression engine can give bounded, predictable-runtime evaluation of untrusted input for narrower cases. | values: value-candidate: security, correctness | sources: f007483@§ WASM, closing paragraph; f007483@§ Expression engine, closing paragraph

### plugin-system-mechanism--p3
- for | WebAssembly is currently too immature to be used for a plugin system and will make plugin developers' lives hard, despite its sandboxing strength — citing uneven cross-language support and churning toolchains and targets (WASI p1, p2). | values: value-candidate: security, stability | sources: f007483@§ WASM, closing paragraph
- against | Embedding QuickJS is recommended as the default, easier-to-integrate plugin approach over WASM. | values: approachability, performance | sources: f007483@§ Scripting language, closing paragraph

### plugin-system-mechanism--p4
- for | For his own project, forks CEL down to a boolean-only subset, reasoning that a non-Turing-complete expression language gives bounded, predictable-runtime evaluation of untrusted user input; recommends QuickJS instead for most other projects. | values: correctness, value-candidate: security | sources: f007483@§ Expression engine, closing paragraph
- against | For most projects, embedding QuickJS is recommended as the default plugin approach rather than a narrower expression engine. | values: approachability, performance | sources: f007483@§ Scripting language, closing paragraph

## pre-1-0-api-default-stability
### pre-1-0-api-default-stability--p1
- for | Without a known blocking issue, sees no problem exposing the interrupt API as stable for now. | values: iteration-speed | sources: f002517@comment 2025-01-10T12:44:33Z
- against | After push back, the same voice reverses course and agrees the interrupt API isn't ready, since prior PRs assumed interrupts wouldn't be stabilized and some interrupt enum variants don't make sense for the CPU-driven driver. | values: correctness, stability | sources: f002517@comment 2025-01-10T13:08:42Z

### pre-1-0-api-default-stability--p2
- for | After push back, reverses course and agrees the interrupt API isn't ready, marking it unstable for now. | values: correctness, stability | sources: f002517@comment 2025-01-10T13:08:42Z
- against | Without a known blocking issue, there's no problem exposing the interrupt API as stable for now. | values: iteration-speed | sources: f002517@comment 2025-01-10T12:44:33Z

## proc-macro-derives-vs-reflection-shape
### proc-macro-derives-vs-reflection-shape--proc-macros-costly
- for | A pure AST transform gets shaped as Rust source that the compiler must compile, optimize, run, and grant full disk/network access to "just in case" — every new behavior (Debug, Display, Deserialize, ...) tends to spawn its own trait and derive macro that must independently win ecosystem-wide adoption, and many attempts to fix this haven't stuck. | values: value-candidate: security, simplicity | sources: f011413@~00:02:04–00:02:37
- against | A single associated `SHAPE` constant per type, derived once, lets many downstream behaviors consume from one derive instead of spawning a new trait and macro per behavior. | values: simplicity | sources: f011413@[02:09]-[04:09]

### proc-macro-derives-vs-reflection-shape--reflection-doesnt-clearly-win
- for | Reflection was expected to trade only build time for runtime speed; measured build times came out "a wash," and runtime performance was unconditionally worse "by design... a fact of life, you can do nothing to change that" — a negative result. | values: performance | sources: f011413@~00:06:23–00:07:00; f011413@[05:09]-[09:12]
- for | A Cranelift JIT built on the reflected data can beat Serde in a microbenchmark, but shipping a JIT isn't viable broadly: rejected outright on Apple platforms, disliked for unexplained binary size and warm-up cost. | values: performance, value-candidate: distribution-constraints | sources: f011413@~00:10:31–00:11:03
- against | Ship data about types instead of more code: a single associated `SHAPE` constant per type lets many downstream behaviors consume from one derive, and a reflection-based serializer can pick the right encoding for a concrete element type at runtime without Serde's explicit annotation. | values: simplicity, correctness | sources: f011413@[02:09]-[04:09]; f011413@[08:11]-[10:12]

### proc-macro-derives-vs-reflection-shape--ship-shape-data
- for | Instead of turning types into more code, ship data about types: a single associated `SHAPE` constant per type (name, offset, alignment, type id, variants, attributes, doc comments) that many downstream behaviors can consume from one derive, avoiding the ecosystem-adoption cost of a new trait/derive per behavior. | values: simplicity | sources: f011413@[02:09]-[04:09]
- for | A reflection-based serializer can inspect the concrete element type at runtime and pick the right encoding (e.g. `Vec<u8>` as raw bytes) without any annotation, something Serde needs an explicit `#[serde(with = ...)]` for since Rust has no stable or nightly-safe specialization. | values: correctness | sources: f011413@[08:11]-[10:12]
- against | Reflection's own measured tradeoffs are a negative result: build times came out "a wash" rather than clearly better, and runtime performance is unconditionally worse by design; a JIT can close the gap but isn't viable to ship broadly. | values: performance | sources: f011413@~00:06:23–00:07:00; f011413@~00:10:31–00:11:03

## ptx-build-host-vs-multi-arch
### ptx-build-host-vs-multi-arch--p1
- for | The PTX is compiled for your machine via `build.rs` at compile time — it is not one binary distributed to everyone. | values: correctness | sources: f002518@comment 2025-10-25T10:12:19Z
- against | no argument in sources

### ptx-build-host-vs-multi-arch--p2
- no argument in sources

## public-naming-brevity-vs-clarity
### public-naming-brevity-vs-clarity--alt1
- for | Fun names are great, but sometimes they get in the way — the team loved `MagicEndpoint` as a name, but it just became too long, so it was renamed to plain `Endpoint`. | values: approachability | sources: f001515@§ "The MagicEndpoint is dead, long live the Endpoint"
- against | It makes sense to spell a name out explicitly rather than abbreviate it, to make it a bit easier on users to infer what the name means. | values: approachability | sources: f001617@PR #13253, comment 2024-06-19T11:34:20Z

### public-naming-brevity-vs-clarity--clarity-over-brevity
- for | It makes sense to spell out "snippets" explicitly in a name rather than abbreviate it to "scls," to make it a bit easier on users to infer what the name means. | values: approachability | sources: f001617@PR #13253, comment 2024-06-19T11:34:20Z
- against | Fun/evocative names are great, but brevity can be the deciding factor even against a well-liked name once it gets too long. | values: approachability | sources: f001515@§ "The MagicEndpoint is dead, long live the Endpoint"

## pump-events-timeout-poll
### pump-events-timeout-poll--p1
- for | Proposed broadening the workaround so that every non-nil duration, not just zero, forces `Poll`. | values: correctness | sources: f002685@GitHub issue comment, 2025-02-20T10:24
- against | Reconsidered and narrowed the workaround to only the zero-duration case, reasoning it doesn't make sense to return `Wait` when a nonzero duration was explicitly requested — that should be winit's own responsibility to handle correctly. | values: correctness | sources: f002685@GitHub issue comment, 2025-02-20T13:08

### pump-events-timeout-poll--p2
- for | Narrows the workaround to the zero-duration case only, reasoning it doesn't make sense to return `Wait` when a nonzero duration was explicitly requested, and leaves handling that case correctly to winit itself. | values: correctness | sources: f002685@GitHub issue comment, 2025-02-20T13:08
- against | Any duration, as long as it's `Some`, should make the control flow `Poll`. | values: correctness | sources: f002685@GitHub issue comment, 2025-02-20T10:24

## reflection-security-risk
### reflection-security-risk--p1
- for | The auto-implemented `Reflect` trait reads as inherently ominous — "like tapping the Marauder's Map with your wand and saying 'I solemnly swear I am up to no good.'" | values: value-candidate: security | sources: f012469@post by @XMPPwocky dated 2015-12-01T00:17:43Z
- against | no argument in sources

### reflection-security-risk--p2
- no argument in sources

## replace-battle-tested-c-with-rust
### replace-battle-tested-c-with-rust--age-means-battle-tested
- for | Cites a Google security-blog study on Android finding most memory-safety vulnerabilities live in recently changed code, taking this as support for older code tending to have fewer bugs. | values: value-candidate: empirical-evidence | sources: f005516@reply, 2025-06-10T07:41:05-05:00
- against | The takeaway from that same Google study should be that code gets less buggy from active use and maintenance, not from the simple passage of time; the "old codebases are more optimized/battle-tested" meme is false in general. | values: value-candidate: empirical-evidence | sources: f005516@reply, 2025-06-10T00:43:48-05:00 and 2025-06-10T10:38:09-05:00; f005516@reply, 2025-06-10T07:57:08-05:00

### replace-battle-tested-c-with-rust--bootstrap-undermines-case
- for | All the language-level memory safety in the world can't help if the compiler's own bootstrap chain could be compromised — by the same "moral imperative" logic, avoiding Rust until bootstrapping is fixed (e.g. keeping mrustc close to mainline) would be the imperative instead. | values: value-candidate: supply-chain-trust | sources: f005743@comment at 2026-06-02T17:16:20-05:00
- against | There are genuine moral imperatives in the industry, but language choice isn't one of them. | values: value-candidate: supply-chain-trust | sources: f005743@comment at 2026-06-02T14:37:20-05:00

### replace-battle-tested-c-with-rust--broad-quality-improvement
- no argument in sources

### replace-battle-tested-c-with-rust--narrow-niche
- for | Contrasts "Rust evangelists coming from Python or JS" with a C/C++ background, framing Rust's proper role as displacing C specifically in very-low-level/constrained work, while judging its contribution to OS kernel development as minor ("almost nothing... but still some progress"). | values: value-candidate: scope-of-applicability | sources: f012849@comment, "1mo"
- against | no argument in sources

### replace-battle-tested-c-with-rust--only-maintenance-improves-code
- for | Rejects the "old codebases are more optimized/battle-tested" meme as false in general — it depends on whether someone actually spent time optimizing or fuzzing; a Rust crate (encoding_rs) beat glibc's iconv because of iconv's fundamentally slow architecture, and unfuzzed "battle-tested" old code can still hide bugs the first real fuzzer finds. | values: performance, correctness | sources: f005516@reply, 2025-06-10T00:43:48-05:00 and 2025-06-10T10:38:09-05:00
- for | Reframes the cited Google study's takeaway as being about active use and maintenance reducing bugs over time, not the simple passage of time. | values: correctness | sources: f005516@reply, 2025-06-10T07:57:08-05:00
- against | A Google security-blog study on Android found most memory-safety vulnerabilities live in recently changed code, which supports older code tending to have fewer bugs — i.e. age itself correlates with fewer bugs. | values: value-candidate: empirical-evidence | sources: f005516@reply, 2025-06-10T07:41:05-05:00

### replace-battle-tested-c-with-rust--p1
- for | Implement as much of the project in Rust as reasonably possible, but keep pragmatic exceptions — it doesn't make sense to rewrite something like libsecp256k1 in Rust when the same upstream library other projects already trust is available. | values: value-candidate: pragmatism | sources: f000267@Design Overview § Desiderata
- against | no argument in sources

### replace-battle-tested-c-with-rust--reject-moral-framing
- for | There are genuine moral imperatives in the industry, but language choice isn't one of them. | values: value-candidate: economics | sources: f005743@comment at 2026-06-02T14:37:20-05:00
- against | All the language-level memory safety in the world can't help if the compiler's own bootstrap chain could be compromised, so by the same "moral imperative" logic used to argue for Rust, avoiding Rust until bootstrapping is fixed would be the imperative instead. | values: value-candidate: supply-chain-trust | sources: f005743@comment at 2026-06-02T17:16:20-05:00

### replace-battle-tested-c-with-rust--replace-with-rust
- for | OpenSSL and its derivatives carry a long history of memory-safety vulnerabilities, and Rustls now shows roughly 2x lower handshake latency in benchmarks — time for the Internet to move off C-based TLS. | values: correctness, performance | sources: f005964@§ "What is Rustls?" / "Conclusion"
- for | librsvg is dropping gdk-pixbuf's C image decoders for the Rust `image-rs` crate, explicitly acknowledging the incumbent C libraries are heavily tested and continuously fuzzed and that the Rust decoder crates are comparatively less developed on performance and exotic-format support, but framing the move as an opportunity to find and fix exactly the gaps that remain rather than a claim of already-equal maturity. | values: correctness | sources: f006797@"Se buscan probadores" section
- against | Implement as much as reasonably possible in Rust, but keep pragmatic exceptions — it doesn't make sense to rewrite a battle-tested library like libsecp256k1 in Rust when the same upstream library other projects already trust is available. | values: value-candidate: pragmatism | sources: f000267@Design Overview § Desiderata

### replace-battle-tested-c-with-rust--safety-not-enough
- no argument in sources

## reuse-vs-purpose-built-unwind
### reuse-vs-purpose-built-unwind--p1
- for | Fine with two separate collection methods coexisting, but doesn't want a second, parallel implementation of debuginfo-less unwinding built alongside one that is already implemented and battle-tested in the codebase. | values: stability, simplicity | sources: f004160@comment 2026-01-26T19:58:25Z
- against | no argument in sources

### reuse-vs-purpose-built-unwind--p2
- no argument in sources

## roadmap-performance-vs-features
### roadmap-performance-vs-features--p1
- for | The project is already in good shape on extensibility and customizability, so it would be great to have one or two quarters where the focus is specifically performance. | values: performance | sources: f001724@issue comment, 2024-07-13T09:20:20Z
- against | A logical-types proposal isn't purely a feature detour from the perf-quarter push — it would itself improve performance, particularly late materialization for REE arrays and string views. | values: performance | sources: f001724@issue comment, 2024-07-14T17:55:14Z

### roadmap-performance-vs-features--p2
- for | A logical-types proposal isn't purely a feature detour from the perf-quarter push — it would itself improve performance, particularly late materialization for REE arrays and string views — while still agreeing to rescope it to be easier to manage. | values: performance | sources: f001724@issue comment, 2024-07-14T17:55:14Z
- against | The project is already in good shape on extensibility/customizability, so the roadmap should dedicate one or two quarters specifically to performance rather than new features. | values: performance | sources: f001724@issue comment, 2024-07-13T09:20:20Z

## rust-for-high-level-apps
### rust-for-high-level-apps--less-productive-for-prototyping
- for | Long compile times and language rigidity made their own users simply more productive with existing high-level tools like React and FastAPI than with early high-level Rust. | values: iteration-speed, approachability | sources: f011305@~02:01
- against | Rust's mission shouldn't be exclusive to so-called core/systems software — high-level application development deserves the same investment. | values: approachability | sources: f011305@~03:01

### rust-for-high-level-apps--push-rust-into-high-level-apps
- for | Rust's mission shouldn't be exclusive to so-called core/systems software — high-level application development deserves the same investment. | values: approachability | sources: f011305@~03:01
- against | Long compile times and language rigidity made their own users simply more productive with existing high-level tools like React and FastAPI than with early high-level Rust. | values: iteration-speed, approachability | sources: f011305@~02:01
