# Blind fill input, batch 1, file 07 of 13

For each Claim below, name the one Position of its Question that the Claim supports (a Position id from the list), or `none` if it supports none of them. The Claims are in random order.

## Question `lambda-vs-containers`

Should a Rust service run serverless (Lambda, edge Workers) or on long-running containers or VPSes?

Positions:
- `lambda-vs-containers--serverless-first`: Default to serverless once measured, or build on edge primitives
- `lambda-vs-containers--split-by-workload`: Serverless for infrequent or test traffic, containers for always-on

Claims:
- `b-sT07-f004166-c1` · Voice: Nick Kuntz · Source: https://blog.cloudflare.com/serverless-matrix-homeserver-workers (`f004166`) · Date: 2026-01-27 · Locator: § storage primitives ("The key insight from porting Tuwunel…"); § conclusion
  - Quote: "different data needs different consistency guarantees"
  - Paraphrase: D1 for queryable durable data, KV for OAuth tokens, R2 for media, Durable Objects where atomicity is required (one-time key claims); argues operations vanish and cost scales to zero
- `b-sb20-f007797-c1` · Voice: Sam Van Overmeire · Source: https://medium.com/@sam.van.overmeire/deploying-axum-to-lambda-and-ecs-using-lambda-web-adapter-2273bd56bb81 (`f007797`) · Date: 2024-02-21 · Locator: closing paragraph, beginning "Lambda Web Adapter not only makes it easier"
  - Quote: "It's a tradeoff because there is now a meaningful difference between the infrastructure your code runs on in test versus production. But in some scenarios, the cost savings might be worth it."
  - Paraphrase: because Lambda Web Adapter decouples the Axum app from any one runtime, an app that is costly to run 24/7 on Lambda but cheap on ECS could run infrequent test environments on Lambda and production on ECS; the author calls this "a tradeoff" since test and production would then run on meaningfully different infrastructure, but says the cost savings can be worth it in some scenarios
- `a-sa24-f011220-c1` · Voice: James Eastham · Source: https://youtube.com/watch?v=x4yUfs0GrI4 (`f011220`) · Date: 2024-12-13 · Locator: ~38:52-39:58
  - Quote: "next time you're looking to deploy a rust application into production just consider serverless see how that might help you"
  - Paraphrase: after porting the same Rust web API and Kafka-consuming background service from Fargate (512 MB, always-on) to Lambda, latency and p50/p99 held steady, memory use dropped to a fraction of the container's, cold starts were a small minority of invocations (3/850 for the background service, 4/1,350 for the web API), and the idle 24/7 container cost/sustainability problem went away; he concludes serverless, not the container/Kubernetes path, is what should be reached for by default, including for teams that later "graduate" to Kubernetes once they understand their workload
- `a-sa17-f007797-c1` · Voice: Sam Van Overmeire · Source: https://medium.com/@sam.van.overmeire/deploying-axum-to-lambda-and-ecs-using-lambda-web-adapter-2273bd56bb81 (`f007797`) · Date: 2024-02-16 · Locator: paragraph beginning "Lambda Web Adapter not only makes it easier..."
  - Quote: "An application that runs 24/7 on prod can be costly on Lambda, but cheap on ECS. On the other hand, if you have one or more infrequently used test environments, Lambda is the better choice."
  - Paraphrase: Using Lambda Web Adapter to keep one Axum app deployable to either target, argues Lambda suits infrequently-used or test environments while ECS/Fargate is cheaper for always-on production traffic — accepting a test/prod infrastructure mismatch for the cost savings.

## Question `land-hal-separate-now-vs-unified-later`

should a new chip-family HAL be merged into the monorepo immediately as its own separate crate to unblock waiting users, or held back until it can be integrated into the unified/combined HAL from the start?

Positions:
- `land-hal-separate-now-vs-unified-later--p1`: Land it as a side crate now; unify later once the shared metapac/combined HAL is ready
- `land-hal-separate-now-vs-unified-later--p2`: Same — merge as-is now, deprecate in favor of the unified HAL once ready

Claims:
- `b-sR09-f003955-c2` · Voice: felipebalbi (NXP embedded engineer, embassy-nxp contributor) · Source: https://github.com/embassy-rs/embassy/pull/4989 (`f003955`) · Date: 2025-12-04 · Locator: embassy-rs/embassy#4989, comment 2025-12-04T18:35:15Z. · L824-L827.
  - Quote: "The idea is that we can get this merged as is, once the metapac is ready, we can switch to it. Then once the combined HAL is ready, it shouldn't be a big deal to deprecate this and have users switch."
  - Paraphrase: same — merge as-is now, deprecate in favor of the unified HAL once ready.
- `b-sR09-f003955-c1` · Voice: jamesmunns (embassy maintainer) · Source: https://github.com/embassy-rs/embassy/pull/4989 (`f003955`) · Date: 2025-12-04 · Locator: embassy-rs/embassy#4989, comment 2025-12-04T18:32:46Z. · L817-L820.
  - Quote: "I wanted to get our previously private work upstreamed ASAP (so we can basically deprecate/archive odp/embassy-mcxa). If there's a path to moving mcxa into embassy-nxp, we can do it now that the code is in the same repo."
  - Paraphrase: land it as a side crate now; unify later once the shared metapac/combined HAL is ready.

## Question `language-safety-vs-hw-isolation`

Does Rust's memory safety meaningfully substitute for hardware/OS-level address-space isolation when running untrusted or mutually adversarial code in one process (single-address-space "libOS" designs)?

Positions:
- `language-safety-vs-hw-isolation--p1`: Language safety insufficient for untrusted code
- `language-safety-vs-hw-isolation--p2`: Language safety a major step toward safe libos

Claims:
- `a-saL1-f005360-c4` · Voice: matklad · Source: https://lobste.rs/s/r1wrt6 (`f005360`) · Date: 2024-10-15 · Locator: reply, 2024-10-15T10:57:36-05:00
  - Quote: "We don't have language-level safety. Rust protects a user from 'holding it wrong,' but it doesn't protect from intentional misuse."
  - Paraphrase: Rejects that Rust provides "language-level safety" sufficient for running mutually adversarial code in one address space; Rust protects against accidental misuse ("holding it wrong"), not deliberate misuse, which is what true fine-grained security would require.
- `a-saL1-f005360-c5` · Voice: dist1ll · Source: https://lobste.rs/s/r1wrt6 (`f005360`) · Date: 2024-10-15 · Locator: reply, 2024-10-15T13:13:15-05:00
  - Quote: "Rust might not be there yet, but it solved some of the hardest problems (safety + performance) that make a high-performance libOS not a total nightmare."
  - Paraphrase: Concedes Rust "might not be there yet" for full language-level security, but argues it already solved the hardest combined problem (safety plus performance) needed to make a high-performance library-OS design viable, with missing pieces like capabilities/effects systems emerging next.
- `a-saL1-f005360-c6` · Voice: lonjil · Source: https://lobste.rs/s/r1wrt6 (`f005360`) · Date: 2024-10-15 · Locator: reply, 2024-10-15T13:39:05-05:00
  - Quote: "Rust and (language-level) capabilities and effect systems are incapable of solving the problem unless absolutely all the code is such Rust code and unsafe is forbidden... Very viable for single application unikernel stuff, but not viable for many applications in the same address space."
  - Paraphrase: Argues language-level capabilities/effect systems can't solve multi-tenant isolation unless literally all code sharing the address space is such trusted, unsafe-forbidden code compiled by a trusted compiler; viable for a single-application unikernel, not for many mutually distrusting applications together.

## Question `large-pr-split`

One large PR, or split into small PRs?

Positions:
- `large-pr-split--split-into-small-prs`: Split before merging
- `large-pr-split--alt1`: Land the large contribution as one PR

Claims:
- `b-sb08-f002518-c3` · Voice: ivarflakstad · Source: https://github.com/huggingface/candle/pull/2704 (`f002518`) · Date: 2026-06-21 · Locator: comment 2026-06-21T09:32:07Z
  - Quote: "I think having this branch as the hub where backwards cuda compatibility is developed - and then extract only the required code into isolated PRs is a good way to get the improvements merged."
  - Paraphrase: reviewing one huge combined branch is hard and risky; better to treat it as a development hub and extract small isolated PRs for merging

## Question `leaky-signal-abstraction-electrical-config`

Should an embedded HAL's peripheral-signal abstraction expose electrical-configuration details (drive strength, pull resistors, input/output mode) on the signal type itself, even though this leaks device-specific configuration into what is meant to be a clean peripheral-routing abstraction?

Positions:
- `leaky-signal-abstraction-electrical-config--p1`: The peripheral-signal abstraction is a leaky one that ideally wouldn't exist, but is kept for convenience
- `leaky-signal-abstraction-electrical-config--alt1`: Keep electrical configuration off the peripheral-signal abstraction

Claims:
- `a-sR06-f002005-c1` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/2128 (`f002005`) · Date: 2024-09-10 · Locator: PR #2128, comment 2024-09-10T08:14:33Z
  - Quote: "Peripheral I/O shouldn't, in an ideal world, care about GPIO drive strength, pull resistors, input/output mode, and this leaky abstraction really shows in the random null methods we must have on DummyPin/Level now."
  - Paraphrase: says peripheral I/O ideally shouldn't need to know about drive strength, pull resistors or input/output mode, and calls the current design a leaky abstraction visible in the null methods `DummyPin`/`Level` must carry.

## Question `library-auth-opinionated-vs-unopinionated`

Should a networking library impose an authentication scheme for its relays, or stay unopinionated?

Positions:
- `library-auth-opinionated-vs-unopinionated--authenticated-managed-default`: The managed service authenticates relays by default
- `library-auth-opinionated-vs-unopinionated--unopinionated-library`: The library stays unopinionated; operators choose the scheme for self-hosted relays

Claims:
- `a-sT11-f004960-c1a` · Voice: n0, inc. (Iroh Services), post by Rae McKelvey · Source: https://iroh.computer/blog/authenticated-relays (`f004960`) · Date: 2026-07-30 · Locator: intro ("we've decided that managed relays on Iroh Services are now authenticated by default") and "The problem: a relay URL is a credential you can't revoke"
  - Quote: "If the relay accepts anyone, then anyone who learns its URL can push traffic through it."
  - Paraphrase: an open relay's URL ships in every client and leaks, so anyone can spend its finite bandwidth. Managed relays deployed from June 2026 onward require a signed, expiring, endpoint-bound token issued from the project's API key, while earlier relays stay open unless switched. For self-run relays, iroh leaves authentication to the operator
- `b-sR11-f004960-c1` · Voice: Rae McKelvey (iroh / n0) · Source: https://iroh.computer/blog/authenticated-relays (`f004960`) · Date: 2026-07-30 · Locator: "The problem: a relay URL is a credential you can't revoke" section
  - Quote: "iroh is unopinionated about that"
  - Paraphrase: self-run relays are untouched — "you can build your own authentication scheme" — while managed relays now default to API-key-scoped tokens
- `a-sT11-f004960-c1b` · Voice: n0, inc. (Iroh Services), post by Rae McKelvey · Source: https://iroh.computer/blog/authenticated-relays (`f004960`) · Date: 2026-07-30 · Locator: intro ("we've decided that managed relays on Iroh Services are now authenticated by default") and "The problem: a relay URL is a credential you can't revoke"
  - Quote: "If the relay accepts anyone, then anyone who learns its URL can push traffic through it."
  - Paraphrase: an open relay's URL ships in every client and leaks, so anyone can spend its finite bandwidth. Managed relays deployed from June 2026 onward require a signed, expiring, endpoint-bound token issued from the project's API key, while earlier relays stay open unless switched. For self-run relays, iroh leaves authentication to the operator

## Question `library-error-type-opaque-vs-typed`

Opaque (`anyhow`) or concrete typed (`thiserror`/`snafu`) error types, and do typed errors need an opaque wrapper for logged context?

Positions:
- `library-error-type-opaque-vs-typed--concrete-typed-errors`: Concrete, enumerable error types over `anyhow`
- `library-error-type-opaque-vs-typed--hybrid-snafu`: A hybrid with automatic backtraces (snafu)
- `library-error-type-opaque-vs-typed--typed-over-time`: Move toward typed errors as the codebase matures; keep `anyhow` for some things
- `library-error-type-opaque-vs-typed--wrap-in-anyhow-for-context`: For logged context, wrap typed errors in `anyhow`/`eyre`

Claims:
- `a-sa18-f008583-c1` · Voice: Tomas Tauber · Source: https://forgestream.idverse.com/blog/20250902-cloudwatch-rust-logging (`f008583`) · Date: 2025-09-02 · Locator: "Error logging" section
  - Quote: "The thiserror crate currently only supports the default {} display format, which loses the error context. One workaround for this is to wrap the errors in anyhow or eyre that support the alternate display format."
  - Paraphrase: recommends logging errors with the alternate `{:#}` display because it preserves the full source-error chain (e.g. AWS SDK's `Unhandled` variants), and flags that `thiserror` currently only supports the default `{}` format, losing that context, so the workaround is to wrap errors in `anyhow` or `eyre` which support the alternate display
- `a-saL2-f011092-c6` · Voice: Luca Casonato · Source: https://youtube.com/watch?v=YcujtU0LA9Y (`f011092`) · Date: 2024-02-13 · Locator: ~00:48:46 (Q&A)
  - Quote: "I gained... an appreciation for very robust error handling... in the beginning I was very happy to use... anyhow for many things and we still do use anyhow for things but... as time went on I realized... having really structured errors is something that's super super valuable"
  - Paraphrase: reflecting on lessons learned building Deno, says he started out happily using anyhow for error handling broadly, but over time came to see well-structured, typed error handling as far more valuable, while noting they still use anyhow for some things
- `b-sb10-f003188-c2` · Voice: ramfox · Source: https://iroh.computer/blog/iroh-0-90-the-canary-series (`f003188`) · Date: 2025-06-27 · Locator: "💥 Concrete Errors 💥" section / Breaking Changes list
  - Quote: "all public APIs return concrete error types, rather than anyhow::Error"
  - Paraphrase: all iroh public APIs now return concrete error types instead of anyhow::Error, a large change touching most of the codebase
- `b-sb10-f003222-c1` · Voice: rklaehn · Source: https://iroh.computer/blog/iroh-blobs-0-90-changes (`f003222`) · Date: 2025-07-04 · Locator: "Errors" section
  - Quote: "Compared to the old blobs, we have vastly reduced the usage of anyhow for errors. Instead we use the snafu crate to provide concrete errors, with some additional features like backtraces and span traces."
  - Paraphrase: iroh-blobs has vastly reduced its use of anyhow, switching to the snafu crate for concrete errors with backtraces and span traces
- `a-sa14-f005149-c1` · Voice: dig, b5, and ramfox (iroh team) · Source: https://iroh.computer/blog/error-handling-in-iroh (`f005149`) · Date: 2025-08-22 · Locator: § Enter Snafu: The Hybrid Approach
  - Quote: "Snafu is essentially thiserror on steroids... Automatic backtrace capture when constructing error variants"
  - Paraphrase: after experimenting with both dominant approaches, settle on snafu because it gives enum-based precision like thiserror plus automatic backtrace capture per variant, working around the `Into`-trait conflict that otherwise forces a choice between ergonomic `?` and backtraces
- `b-sb21-f008583-c1` · Voice: Tomas Tauber · Source: https://forgestream.idverse.com/blog/20250902-cloudwatch-rust-logging (`f008583`) · Date: 2025-09-03 · Locator: § "Error logging"
  - Quote: "The thiserror crate currently only supports the default {} display format, which loses the error context. One workaround for this is to wrap the errors in anyhow or eyre that support the alternate display format."
  - Paraphrase: `thiserror` currently only supports the default `{}` Display format and loses error context (e.g. AWS SDK's `Unhandled` variant losing the underlying resource info); wrapping errors in `anyhow` or `eyre` recovers the alternate `{:#}` display that carries full context

## Question `library-io-factored-out`

Should a portable library perform its own I/O and threads, or take in-memory data and leave I/O to the caller?

Positions:
- `library-io-factored-out--p1`: Factor-out-I/O
- `library-io-factored-out--p2`: Bring your own threads
- `library-io-factored-out--p3`: Factor I/O out of a portable library; accept in-memory slices, let the caller perform I/O

Claims:
- `a-sB02-f000256-c13` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "How to Add WebAssembly Support to a General-Purpose Crate" — "Avoid Performing I/O Directly"
  - Quote: "Factor I/O out of your library, let users perform the I/O and then pass the input slices to your library instead."
  - Paraphrase: since the Web has no filesystem and only async I/O, a portable library should factor I/O out of itself, taking input slices from callers rather than reading files or performing I/O itself.
- `a-sB02-f000256-c14` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "How to Add WebAssembly Support to a General-Purpose Crate" — "Avoid Spawning Threads"
  - Quote: "Another option is to factor out thread spawning from your library and allow users to \"bring their own threads\"."
  - Paraphrase: since spawning threads panics on wasm32-unknown-unknown, a portable library should factor thread spawning out to the caller, similar to factoring out I/O, which also plays nicer with apps that own a custom thread pool.
- `b-bk02-f000256-c5` · Voice: rustwasm working group (Rust and WebAssembly book) [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: unknown (living doc) · Locator: § "How to Add WebAssembly Support to a General-Purpose Crate" → Avoid Performing I/O Directly
  - Quote: "Factor I/O out of your library, let users perform the I/O and then pass the input slices to your library instead."
  - Paraphrase: gives a before/after refactor turning a `fs::read`-based function into one taking `&[u8]`, reasoning that the Web has no filesystem and I/O there is always asynchronous.

## Question `library-panic`

On invalid input or a violated precondition, panic (`unwrap`, documented panics) or return `Result`?

Positions:
- `library-panic--never-panic-return-result`: Return `Result`; constructors and runtime-checkable conditions return errors
- `library-panic--no-ad-hoc-panics`: No ad hoc panics; only control-flow-contingent ones
- `library-panic--unwrap-only-in-tests`: `unwrap` only in tests or provably safe spots
- `library-panic--prevent-via-explicit-check`: Prevent the invalid case with an explicit check
- `library-panic--panic-fine-if-documented`: Panicking is fine if documented

Claims:
- `a-sa09-f004055-c6` · Voice: jamesmunns · Source: https://github.com/embassy-rs/embassy/pull/5175 (`f004055`) · Date: 2026-01-05 · Locator: comment @jamesmunns 2026-01-05T14:16:51Z
  - Quote: "why did you remove the Result and switch it back to an assert? If we're going to do that, I'd prefer to have a try_transfer_mem_to_mem that returns a Result and have the main transfer_mem_to_mem just call that with an unwrap."
  - Paraphrase: questions why a memory-transfer function is `unsafe` and an `assert` was reintroduced in place of a `Result`; proposes a fallible `try_` variant with a panicking convenience wrapper on top
- `b-sR12-f005421-c1` · Voice: Rhai project (rhaiscript maintainers) · Source: https://github.com/rhaiscript/rhai (`f005421`) · Date: 2025-01-17 · Locator: README section "Protected against attacks", sub-item "_Don't Panic_ guarantee"
  - Quote: "_Don't Panic_ guarantee - Any panic is a bug. Rhai subscribes to the motto that a library should never panic the host system, and is coded with this in mind."
  - Paraphrase: Rhai treats any panic reaching the host application as a bug in Rhai itself, not an acceptable outcome, and is coded under that guarantee
- `b-sR10-f004573-c1` · Voice: antimora (Tracel AI / burn maintainer) · Source: https://github.com/tracel-ai/burn/pull/4813 (`f004573`) · Date: 2026-04-21 · Locator: PR review comment, 2026-04-21T14:39:58Z
  - Quote: "The `# Panics` list should include the QFloat case (added in the new `TensorCheck::det` at check.rs:1403-1409). Right now a user hitting it gets a panic with no heads-up from the docs."
  - Paraphrase: the QFloat panic path is acceptable but must be listed in the function's `# Panics` docs so a user isn't surprised by it
- `b-sb05-f001512-c1` · Voice: MabezDev · Source: https://github.com/esp-rs/esp-hal/pull/1592 (`f001512`) · Date: 2024-06-11 · Locator: comment 2024-06-11T10:24:37Z
  - Quote: "We shouldn't unwrap here, let's make new and friends fallible I think"
  - Paraphrase: constructors should return Result rather than unwrap/panic internally
- `a-sa06-f003414-c3` · Voice: ConradIrwin · Source: https://github.com/zed-industries/zed/pull/36497 (`f003414`) · Date: 2025-10-28 · Locator: comment 2025-10-28T01:59:12Z
  - Quote: "unwrap is OK in tests and also when you can tell by reading the current function that it can't ever unwrap"
  - Paraphrase: flags new `unwrap()`s as needing early returns instead, with unwrap acceptable only in tests or where the current function makes panics provably impossible
- `a-sa21-f011069-c5` · Voice: Aleksandr Petrosyan · Source: https://youtube.com/watch?v=LO7tvIed-YQ (`f011069`) · Date: 2023-11-15 · Locator: ~00:32:20-00:32:40
  - Quote: "I don't think that having ad hoc panics in your code is a good idea... maybe experts of about Rust will tell me otherwise, but I don't like panics in my code which are ad hoc."
  - Paraphrase: Used a panic as an ad hoc short-circuit to bail out of a search after too long, but states he considers ad hoc panics bad practice, preferring panics reserved for specific cases tied to control flow — while explicitly flagging that other Rust practitioners may disagree with him.
- `b-sR10-f004573-c2` · Voice: softmaximalist (PR author, burn contributor) · Source: https://github.com/tracel-ai/burn/pull/4813 (`f004573`) · Date: 2026-04-19 · Locator: PR review comment, 2026-04-19T18:47:03Z
  - Quote: "Hence, I have added a tensor check to reject a quantized input tensor."
  - Paraphrase: rather than let a quantized input fail deep inside LU decomposition, add an explicit TensorCheck that rejects it up front with a clear message
- `a-sa09-f004055-c7` · Voice: bogdan-petru · Source: https://github.com/embassy-rs/embassy/pull/5175 (`f004055`) · Date: 2026-02-05 · Locator: comment @bogdan-petru 2026-02-05T01:10:05Z
  - Quote: "Safe function: mem_to_mem() is now a safe function (not unsafe)... Returns Result: It returns Result<Transfer<'_>, Error> instead of using asserts... Returns Error::BufferNotAccessible if validation fails."
  - Paraphrase: converges by making the memory-transfer function safe, returning `Result<Transfer<'_>, Error>` with runtime validation that the source/destination buffers are DMA-accessible

## Question `lifetimes-on-structs`

Should structs carry lifetime parameters (borrowed data) or keep data owned?

Positions:
- `lifetimes-on-structs--borrow-for-measured-performance`: Add lifetime parameters where a measured bottleneck justifies them
- `lifetimes-on-structs--owned-by-default`: Avoid lifetimes on structs as a rule; favor easy-mode owned types, especially for teams new to Rust

Claims:
- `b-sb20-f007608-c2` · Voice: jacko.io · Source: https://jacko.io/object_soup.html (`f007608`) · Date: 2023-10-25 · Locator: footnote to the paragraph beginning "Playing with these examples is educational" in section "Part Two: Borrowing"
  - Quote: "a good rule of thumb is to avoid putting lifetime parameters on structs"
  - Paraphrase: while experimenting with borrow-checker fights builds useful intuition, the actionable takeaway when you get stuck is to keep lifetime parameters off your struct definitions
- `b-sb20-f007364-c1` · Voice: howardjohn · Source: https://blog.howardjohn.info/posts/cel-fast (`f007364`) · Date: 2026-03-04 · Locator: section "References#" preceded by "Native types in CEL#" and "References#" (value type redefinition under heading "References#" appears just after "Ultimate solution"); exact quote is from the paragraph beginning "First, we need references!"
  - Quote: "First, we need references! We change Value to not be owned"
  - Paraphrase: converting `Value` from an owned enum to `Value<'a>` with `Cow`-like `Borrowed`/`Owned` variants (and a `Dynamic`/`DynamicType` trait for native Rust types) was the key change that let a CEL evaluation get within ~10ns of native code, versus 147ns for the original owned/hashmap-based implementation

## Question `lightweight-clones-in-language`

should Rust adopt a lightweight/automatic-clone mechanism (e.g. reference-counted "generational box" ergonomics) for callback-heavy UI code, trading some compile-time guarantees for runtime checks?

Positions:
- `lightweight-clones-in-language--p1`: Add lightweight/automatic clone ergonomics to Rust itself
- `lightweight-clones-in-language--alt1`: Keep cloning explicit; do not add automatic clones to the language

Claims:
- `a-sa26-f011305-c3` · Voice: Jonathan Kelly · Source: https://youtube.com/watch?v=Kl90J5RmPxY (`f011305`) · Date: 2025-10-03 · Locator: ~15:06-16:09
  - Quote: "this is a controversial change in the Rust language. Not everyone may agree, but in my opinion, this is critical to the success of high-level Rust" / "Opinions were divided"
  - Paraphrase: proposed a Rust project goal adding lightweight clones for types like reference-counted smart pointers, prototyped as "generational box"; acknowledges it is contested

## Question `lint-allow-broad-vs-narrow`

When a macro-generated code path (e.g. `#[tracing::instrument]` reaching a value only through a trait method) triggers a false-positive unused/dead-code lint, should the fix be a broad `#![allow(unused)]` or a narrowly scoped allow on the specific item?

Positions:
- `lint-allow-broad-vs-narrow--p1`: Broad allow when linter blind to trait indirection
- `lint-allow-broad-vs-narrow--alt1`: A narrowly scoped allow on the specific item

Claims:
- `a-sR11-f003983-c1` · Voice: crutcher · Source: https://github.com/tracel-ai/burn/pull/4157 (`f003983`) · Date: 2025-12-15 · Locator: comment 2025-12-15T20:40:52Z
  - Quote: "Because the rust linter isn't smart enough to understand that `TensorMetadata` trait operations are being used by `#[tracing::instrument]`"
  - Paraphrase: the blanket `#[allow(unused)]` stays because the compiler's lint can't see that `TensorMetadata` trait operations are being consumed via `#[tracing::instrument]`, so item-level allows would misfire

## Question `lld-default-linker`

Should Rust switch its default linker on the most popular target (x86_64-unknown-linux-gnu) from the system linker to a faster non-GNU linker (lld), accepting a small risk of incompatibility?

Positions:
- `lld-default-linker--p1`: Make rust-lld the default linker on x86_64-unknown-linux-gnu for stable releases
- `lld-default-linker--alt1`: Keep the system linker as the default

Claims:
- `b-sb23-f009657-c1` · Voice: Rémy Rakic (on behalf of the compiler performance working group) · Source: https://blog.rust-lang.org/2025/09/01/rust-lld-on-1.90.0-stable (`f009657`) · Date: 2025-09-01 · Locator: "Summary, and call for testing" section
  - Quote: "it's a drop-in replacement for the vast majority of cases, but lld is not bug-for-bug compatible with GNU ld"
  - Paraphrase: after internal testing on CI, crater and nightly since May 2024 with no major issues, the team judges the ~7x incremental-link / 40% end-to-end speedup on the ripgrep benchmark worth the small risk that lld isn't bug-for-bug compatible with GNU ld, keeping an escape hatch (`-C linker-features=-lld`)

## Question `llm-doc-edits-reproducibility`

When using an LLM to bring doc-comment prose in a codebase to a consistent style, should the project make the process reproducible by pinning down and declaring exactly which model, prompt, and environment produced the edits, or should it instead adopt a formal controlled-language writing standard that constrains vocabulary/grammar enough to make the model's "taste" mostly irrelevant?

Positions:
- `llm-doc-edits-reproducibility--p1`: Pre review guidelines for llms
- `llm-doc-edits-reproducibility--p2`: Adopt-controlled-language-standard-ASD-STE100
- `llm-doc-edits-reproducibility--p3`: Declare model prompt and clean env

Claims:
- `b-sb16-f004997-c3` · Voice: MabezDev · Source: https://github.com/esp-rs/esp-hal/pull/6096 (`f004997`) · Date: 2026-08-12 · Locator: comment @MabezDev 2026-08-12T13:34:07Z
  - Quote: "We must declare what model we run this with. Each model has its own interpretation of the rules and its own \"taste\"... We need to declare the prompt we run with this... we should run these updates in a clean env."
  - Paraphrase: argues that to merge this kind of LLM-driven doc pass, the project must declare which model was used (since each model has its own "taste"), declare the exact prompt (wording changes the results), and run the update in a clean environment to avoid picking up incidental local agent rules.
- `b-sb16-f004997-c1` · Voice: bjoernQ · Source: https://github.com/esp-rs/esp-hal/pull/6096 (`f004997`) · Date: 2026-08-11 · Locator: PR description @bjoernQ 2026-08-11T12:34:57Z
  - Quote: "I assume this will end up in a lot of bike-shedding which ideally should result in additions to the DEVELOPER-GUIDELINES.md to (not only) help LLMs in pre-reviewing changes."
  - Paraphrase: expects the doc-consistency effort to trigger bikeshedding, and hopes it results in additions to DEVELOPER-GUIDELINES.md that also help LLMs pre-review changes.
- `b-sb16-f004997-c4` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/6096 (`f004997`) · Date: 2026-08-12 · Locator: comment @bugadani 2026-08-12T13:36:48Z
  - Quote: "Simplified Technical English pretty much removes taste from the equation, it limits vocabulary and grammar, too."
  - Paraphrase: responds that a controlled-language standard largely removes model "taste" from the equation by constraining vocabulary and grammar, offering this as an alternative to MabezDev's process-heavy approach.
- `b-sb16-f004997-c2` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/6096 (`f004997`) · Date: 2026-08-11 · Locator: comment @bugadani 2026-08-11T12:39:59Z
  - Quote: "I would also propose mandating some standard we should follow, like ASD-STE100 Simplified Technical English, so that the _style_ of the prose is also consistent, and free of any flowery nonsense."
  - Paraphrase: proposes mandating a standard like ASD-STE100 Simplified Technical English so the prose style is consistent and free of "flowery nonsense."

## Question `lts-release-channel`

Should a project support older release lines (an LTS train, backports) or require upgrading?

Positions:
- `lts-release-channel--support-old-lines`: Keep older lines supported (LTS train, backport the fix)
- `lts-release-channel--upgrade-instead`: No backport; upgrade

Claims:
- `b-sR06-f002937-c1` · Voice: Alex Crichton · Source: https://bytecodealliance.org/articles/wasmtime-lts (`f002937`) · Date: 2025-04-22 · Locator: "Wasmtime LTS Releases" article, paragraphs 2-4 (bytecodealliance.org/articles/wasmtime-lts)
  - Quote: "This rate of change can be too fast for users so Wasmtime now supports LTS releases."
  - Paraphrase: Wasmtime previously supported each monthly release for only 2 months, forcing embedders to track upstream closely for security fixes; Wasmtime now designates every 12th release an LTS release, guaranteed 24 months of API-compatible security patches (no backported features), so users can upgrade yearly instead of monthly while still receiving guaranteed security fixes
- `b-sT05-f002501-c1` · Voice: kaplanelad · Source: https://github.com/loco-rs/loco/issues/1133 (`f002501`) · Date: 2025-01-10 · Locator: comment 2025-01-10T16:08:08Z
  - Quote: "Unfortunately, I can't apply this fix to version 0.13.x. It's recommended to upgrade"
  - Paraphrase: points to loco upgrade guide for axum breaking changes; declines applying the CORS fix to 0.13.x

## Question `macro-hides-construction-requirements`

Should a macro hide an API's less-friendly construction requirements from the user, or should the API stay explicit even if less ergonomic?

Positions:
- `macro-hides-construction-requirements--p1`: Macros may hide complexity
- `macro-hides-construction-requirements--alt1`: Keep the API explicit even if less ergonomic

Claims:
- `b-sR10-f004804-c3` · Voice: bugadani (esp-hal maintainer, PR author) · Source: https://github.com/esp-rs/esp-hal/pull/5744 (`f004804`) · Date: 2026-06-15 · Locator: PR description, 2026-06-15T17:07:50Z
  - Quote: "It makes constructing buffers a bit less friendly, but that's hidden from us by the macros currently."
  - Paraphrase: the new reference type makes constructing DMA buffers less friendly directly, but that friction is absorbed by the existing macros so end users don't see it

## Question `macro-ide-tooling`

should Rust macros get first-class IDE tooling (autocomplete, hover, partial expansion) via new mechanisms, or is today's macro opacity accepted as a tradeoff for macro power?

Positions:
- `macro-ide-tooling--p1`: Build new tooling rather than accept macro IDE opacity
- `macro-ide-tooling--alt1`: Accept macro opacity in IDEs as the price of macro power

Claims:
- `a-sa26-f011305-c4` · Voice: Jonathan Kelly · Source: https://youtube.com/watch?v=Kl90J5RmPxY (`f011305`) · Date: 2025-10-03 · Locator: ~13:06
  - Quote: "Rust macros do not support things like autocomplete and partial expansion. So we developed new libraries, such as partial expressions, to make it easier to write high-quality Rust DSLs"
  - Paraphrase: since Rust macros don't support autocomplete or partial expansion, they built a separate library ("partial expressions") to give macro-based DSLs IDE support

## Question `macro-vs-boilerplate`

Should a repeated pattern be written with a macro, or as plain code (functions, derives, explicit boilerplate)?

Positions:
- `macro-vs-boilerplate--macros-sparingly`: Use macros sparingly; prefer functions, derives or macro-free APIs; boilerplate is an acceptable price
- `macro-vs-boilerplate--alt1`: Reach for a macro to remove repetition

Claims:
- `a-sa23-f011186-c3` · Voice: Adam · Source: https://youtube.com/watch?v=bjgGboWCTDw (`f011186`) · Date: 2024-11-20 · Locator: ~00:11:27
  - Quote: "I think macros are kind of like salt you want to use a little"
  - Paraphrase: Rust's macro system is both one of its best and one of its worst features; very powerful but should be used carefully and in small amounts
- `b-sb20-f007736-c1` · Voice: Sam Van Overmeire · Source: https://medium.com/@sam.van.overmeire/rust-macros-taking-care-of-some-lambda-boilerplate-96244d9e1924 (`f007736`) · Date: 2024-01-17 · Locator: paragraph beginning "Before continuing: would you ever want to use a macro like this?"
  - Quote: "For real applications: default to no."
  - Paraphrase: for most real applications either the boilerplate is tolerable or you'll want custom initialization code in `main` that a fully-generated `main` forecloses; the macro pays off mainly if you have many simple Lambdas, a very low tolerance for boilerplate, or want to experiment with macros and serverless
- `b-sb20-f007760-c1` · Voice: Sam Van Overmeire · Source: https://medium.com/@sam.van.overmeire/rust-macros-taking-care-of-even-more-lambda-boilerplate-0c5cb6c4b63c (`f007760`) · Date: 2024-01-31 · Locator: paragraph beginning "As a reminder: in the previous blog post"
  - Quote: "A bit of boilerplate is acceptable when this helps you retain the flexibility to customize your main function, adding any (initialization) code you require."
  - Paraphrase: reiterating the prior post's stance while extending the macro to auto-initialize AWS SDK clients found among the handler's parameters — still frames the macro as useful only for callers with many simple, client-only Lambdas
- `a-sR08-f003082-c1` · Voice: fitzgen (Bytecode Alliance / Wasmtime core, `arbitrary` crate author) · Source: https://github.com/bytecodealliance/wasmtime/pull/10924 (`f003082`) · Date: 2025-06-12 · Locator: PR #10924 review comments
  - Quote: "if we did want to create this particular sequence in a bunch of places we should just use a function rather than a macro"
  - Paraphrase: reviewing a macro used to produce a fixed empty-value sequence, argued it should just be `TableOps::default()` derived on the type, and that if the sequence were needed in several places it should be a function rather than a macro
- `a-sa17-f007736-c1` · Voice: Sam Van Overmeire · Source: https://medium.com/@sam.van.overmeire/rust-macros-taking-care-of-some-lambda-boilerplate-96244d9e1924 (`f007736`) · Date: 2024-01-10 · Locator: paragraph beginning "Before continuing: would you ever want to use a macro like this?"
  - Quote: "Before continuing: would you ever want to use a macro like this? For real applications: default to no."
  - Paraphrase: Defaults against using an attribute macro to strip Lambda-handler boilerplate in real applications, since the boilerplate is usually minor or main() needs custom per-Lambda initialization anyway; reserves the macro for many simple Lambdas, low tolerance for boilerplate, or macro experimentation.

## Question `memory-safety-and-resource-leaks`

Do Rust's safety guarantees prevent resource leaks?

Positions:
- `memory-safety-and-resource-leaks--safety-does-not-prevent-leaks`: It does not prevent resource leaks
- `memory-safety-and-resource-leaks--alt1`: Rust's safety guarantees do prevent resource leaks

Claims:
- `b-sR05-f002341-c1` · Voice: Arqu (n0-computer/iroh engineer, production post-mortem author) · Source: https://iroh.computer/blog/relay-down-a-post-mortem (`f002341`) · Date: 2024-11-19 · Locator: iroh.computer/blog/relay-down-a-post-mortem, "The Nitty Gritty" section, 2024-11-19. · L1958-L1971.
  - Quote: "Rust's memory safety guarantees do not mitigate memory leaks."
  - Paraphrase: safety guarantees are not sufficient; the team had to add load simulation, profiling and explicit fixes for two separate leaked-task/thread bugs, and states the gap outright.
- `a-sR07-f002341-c1` · Voice: Arqu · Source: https://iroh.computer/blog/relay-down-a-post-mortem (`f002341`) · Date: 2024-11-19 · Locator: "The Nitty Gritty" section, memory-issues paragraph
  - Quote: "Rust's memory safety guarantees do not mitigate memory leaks"
  - Paraphrase: Rust's memory-safety guarantees address memory corruption, not leaks; the team leaked tokio tasks and threads in production and only found them through load testing and profiling

## Question `memory-safety-design-priority`

Did Rust's design correctly prioritize memory safety as its one "hard problem," and is that tradeoff fair against other capabilities (e.g., metaprogramming/expressiveness) that consequently matured more slowly?

Positions:
- `memory-safety-design-priority--p1`: Rust over invested in safety at cost of metaprogramming
- `memory-safety-design-priority--p2`: Safety first was the right call metaprogramming will follow

Claims:
- `a-sa28-f012469-c6` · Voice: llogiq (Rust clippy maintainer) · Source: https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (`f012469`) · Date: 2015-09-01 · Locator: same post as above, llogiq's own reply
  - Quote: "I for one think of this as high praise for Rust – it's a young language, and having solved the hard part makes for a great foundation. I trust the other missing 'muscle' (mostly easier/more powerful metaprogramming) will come in time."
  - Paraphrase: reframes Alexandrescu's critique as high praise — solving the hard part (memory management without GC) first is the right foundation, expects metaprogramming/expressiveness to mature later
- `a-sa28-f012469-c5` · Voice: Andrei Alexandrescu (creator of D) — Voice-eligibility caveat: no confirmed Rust track record per subject scope rules (maintains no Rust crate, no Rust role found in this source); logged per rule 5 (exact names, don't invent), eligibility left for merge/audit to rule on · Source: https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (`f012469`) · Date: reddit comment undated in source, reposted 2015-09-01 · Locator: post by @llogiq dated 2015-09-01T01:17:54Z, sourced "on reddit"
  - Quote: "the language had to dedicate so much real estate to this (difficult) problem alone, it became a disharmonic creature with one bulging muscle and little of anything else"
  - Paraphrase: argues Rust spent so much of its design budget on memory-safety that it became lopsided, with little else developed

## Question `memory-safety-vs-correctness-frame`

Is "memory safety" the right frame for language-correctness discourse, or is "correctness" (of which memory safety is one part) the property that actually matters?

Positions:
- `memory-safety-vs-correctness-frame--p1`: Correctness is the real target
- `memory-safety-vs-correctness-frame--alt1`: Memory safety is the right frame

Claims:
- `b-sb19-f005743-c7` · Voice: kristoff · Source: https://lobste.rs/s/67tqpz (`f005743`) · Date: 2026-06-02 · Locator: comment at 2026-06-02T13:32:19-05:00
  - Quote: "Every time a blog post over-fits on memory safety, it's a missed opportunity to talk about correctness, which is a strict superset and what actually matters."
  - Paraphrase: memory-safety-centric arguments miss that correctness is the broader property that matters

## Question `merge-expensive-feature-with-limits`

When a feature is useful but the only available implementation is algorithmically expensive (here, exponential batch count with glyph/outline count), should a game engine merge it now with documented limits, or hold it out of core until an efficient approach exists?

Positions:
- `merge-expensive-feature-with-limits--p1`: Ship with documented limits
- `merge-expensive-feature-with-limits--p2`: Hold for proper solution

Claims:
- `a-sa05-f003126-c4` · Voice: alice-i-cecile · Source: https://github.com/bevyengine/bevy/pull/19639 (`f003126`) · Date: 2025-06-19 · Locator: comment @alice-i-cecile 2025-06-19T00:58:08Z
  - Quote: "I'm really reluctant to merge something this slow and jank, even though I appreciate that it's better than it could have been."
  - Paraphrase: reluctant to merge something this inefficient and rough; asks whether an offline font-preprocessing/baking approach could substitute, and ultimately wants a proper SDF-based text rendering solution instead
- `a-sa05-f003126-c1` · Voice: TotalKrill · Source: https://github.com/bevyengine/bevy/pull/19639 (`f003126`) · Date: 2025-06-16 · Locator: comment @TotalKrill 2025-06-16T16:10:03Z
  - Quote: "I would argue that we could go with a clearer enum of Px1, Px2, Px3... It would also quite clearly communicate the limitations of this implementation, while still allowing us to have it."
  - Paraphrase: an enum of fixed, small widths (Px1/Px2/Px3) makes the performance ceiling explicit to users while still shipping the feature for the common case
- `a-sa05-f003126-c2` · Voice: UkoeHB · Source: https://github.com/bevyengine/bevy/pull/19639 (`f003126`) · Date: 2025-06-16 · Locator: comment @UkoeHB 2025-06-16T20:45:49Z
  - Quote: "The computation cost of the outline increases exponentially with width in the current implementation, so it is not recommended to use a width greater than 3."
  - Paraphrase: documents the cost in the public API doc comment (exponential growth with width) rather than blocking the feature
- `a-sa05-f003126-c3` · Voice: ickshonpe · Source: https://github.com/bevyengine/bevy/pull/19639 (`f003126`) · Date: 2025-06-19 · Locator: comment @ickshonpe 2025-06-19T09:25:27Z
  - Quote: "I'm feeling very negative about it now, even with all the improvements that have been made... most users aren't going to carefully read the docs for text outlines."
  - Paraphrase: even with the batching fixes, most users will not read the docs closely enough to avoid the performance cliff, and the implementation still has visible artifact bugs under transform/rotation

## Question `metal-vs-cpu-priority-candle`

Should GPU (Metal) backend work be prioritized ahead of further CPU/quantization optimization in candle?

Positions:
- `metal-vs-cpu-priority-candle--p1`: Prioritize metal next
- `metal-vs-cpu-priority-candle--alt1`: Prioritize further CPU and quantization work

Claims:
- `b-sR01-f000464-c2` · Voice: LaurentMazare · Source: https://github.com/huggingface/candle/issues/1043 (`f000464`) · Date: 2023-10-06 · Locator: issue comment, 2023-10-06T09:20:02Z
  - Quote: "Metal support is at the top of the priority list for the next large thing"
  - Paraphrase: Metal/GPU support is the top engineering priority for candle's next major push, ahead of further quantized-CPU work.
