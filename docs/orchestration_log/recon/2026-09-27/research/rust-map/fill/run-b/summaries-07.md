# Blind fill summaries, batch 1, file 07 (run b)

## lambda-vs-containers--serverless-first: Default to serverless once measured, or build on edge primitives
tag: tradeoff
Advocates hold that, once measured, serverless should be the default: routing each data need to the matching edge primitive (queryable durable storage, KV, object storage, atomic durable objects) lets operations vanish and cost scale to zero, and a real migration from an always-on container showed steady latency, a fraction of the memory use, and cold starts as a small minority of invocations — leading to the conclusion that serverless, not containers/Kubernetes, is what should be reached for by default, including for teams that later "graduate" to Kubernetes once they understand their workload.
Claims: b-sT07-f004166-c1, a-sa24-f011220-c1

## lambda-vs-containers--split-by-workload: Serverless for infrequent or test traffic, containers for always-on
tag: tradeoff
Advocates hold that an app that is costly to run 24/7 on Lambda but cheap on ECS/Fargate should split by workload: infrequent or test environments run on serverless, always-on production traffic runs on containers — accepting a meaningful infrastructure mismatch between test and production as a tradeoff that's worth the cost savings in some scenarios.
Claims: b-sb20-f007797-c1, a-sa17-f007797-c1

## land-hal-separate-now-vs-unified-later--p1: Land it as a side crate now; unify later once the shared metapac/combined HAL is ready
tag: taste
Advocates hold previously-private work should be upstreamed as its own crate as soon as possible to unblock users, with a path to fold it into the unified HAL once that becomes possible from being in the same repo.
Claims: b-sR09-f003955-c1

## land-hal-separate-now-vs-unified-later--p2: Same — merge as-is now, deprecate in favor of the unified HAL once ready
tag: taste
Advocates hold the same design as p1 in different words: get it merged as-is now, switch to the shared metapac once ready, then deprecate this crate once the combined HAL exists.
Claims: b-sR09-f003955-c2

## language-safety-vs-hw-isolation--p1: Language safety insufficient for untrusted code
tag: fact
Advocates hold Rust does not provide language-level safety sufficient for running mutually adversarial code in one address space: it protects against accidental misuse, not deliberate misuse, and language-level capabilities/effect systems can't solve multi-tenant isolation unless literally all code sharing the address space is trusted, unsafe-forbidden Rust — viable for a single-application unikernel, not for many mutually distrusting applications together.
Claims: a-saL1-f005360-c4, a-saL1-f005360-c6

## language-safety-vs-hw-isolation--p2: Language safety a major step toward safe libos
tag: tradeoff
Advocates hold Rust "might not be there yet" for full language-level security, but has already solved the hardest combined problem — safety plus performance — needed to make a high-performance library-OS design viable, with missing pieces like capabilities/effects systems expected to emerge next.
Claims: a-saL1-f005360-c5

## large-pr-split--split-into-small-prs: Split before merging
tag: taste
Advocates hold that reviewing one huge combined branch is hard and risky; it's better to treat it as a development hub and extract small, isolated PRs for merging.
Claims: b-sb08-f002518-c3

## leaky-signal-abstraction-electrical-config--p1: The peripheral-signal abstraction is a leaky one that ideally wouldn't exist, but is kept for convenience
tag: tradeoff
Advocates hold that peripheral I/O ideally shouldn't need to know about drive strength, pull resistors or input/output mode, naming the current design a leaky abstraction that visibly shows up in the null methods `DummyPin`/`Level` are forced to carry.
Claims: a-sR06-f002005-c1

## library-auth-opinionated-vs-unopinionated--authenticated-managed-default: The managed service authenticates relays by default
tag: tradeoff
Advocates hold that an open relay's URL is a credential that ships in every client and leaks, so anyone who learns it can spend its finite bandwidth — which is why managed relays deployed from a given date onward require a signed, expiring, endpoint-bound token issued from the project's API key.
Claims: a-sT11-f004960-c1a, a-sT11-f004960-c1b

## library-auth-opinionated-vs-unopinionated--unopinionated-library: The library stays unopinionated; operators choose the scheme for self-hosted relays
tag: taste
Advocates hold the library itself takes no position on authentication for self-run relays — operators are free to build their own authentication scheme.
Claims: b-sR11-f004960-c1

## library-error-type-opaque-vs-typed--concrete-typed-errors: Concrete, enumerable error types over `anyhow`
tag: taste
Advocates hold public APIs should return concrete, enumerable error types rather than `anyhow::Error`, even where this is a large change touching most of the codebase.
Claims: b-sb10-f003188-c2

## library-error-type-opaque-vs-typed--hybrid-snafu: A hybrid with automatic backtraces (snafu)
tag: tradeoff
Advocates hold `snafu` is "essentially thiserror on steroids": it gives enum-based precision like `thiserror` plus automatic backtrace and span-trace capture per variant, working around the `Into`-trait conflict that otherwise forces a choice between ergonomic `?` and backtraces, and adopting it vastly reduces prior `anyhow` usage.
Claims: b-sb10-f003222-c1, a-sa14-f005149-c1

## library-error-type-opaque-vs-typed--typed-over-time: Move toward typed errors as the codebase matures; keep `anyhow` for some things
tag: taste
Advocates hold that, having started out happily using `anyhow` for many things, structured typed error handling proved far more valuable as the project matured — while still keeping `anyhow` for some things.
Claims: a-saL2-f011092-c6

## library-error-type-opaque-vs-typed--wrap-in-anyhow-for-context: For logged context, wrap typed errors in `anyhow`/`eyre`
tag: fact
Advocates hold that `thiserror` currently only supports the default `{}` Display format, which loses the full source-error chain, so the workaround for logging is to wrap typed errors in `anyhow` or `eyre`, which support the alternate `{:#}` display that preserves context.
Claims: a-sa18-f008583-c1, b-sb21-f008583-c1

## library-io-factored-out--p2: Bring your own threads
tag: tradeoff
Advocates hold that since spawning threads panics on `wasm32-unknown-unknown`, a portable library should factor thread spawning out to the caller — similar to factoring out I/O — which also plays nicer with apps that own a custom thread pool.
Claims: a-sB02-f000256-c14

## library-io-factored-out--p3: Factor I/O out of a portable library; accept in-memory slices, let the caller perform I/O
tag: fact
Advocates hold that since the Web has no filesystem and only async I/O, a portable library should factor I/O out of itself entirely, taking input slices from callers rather than reading files or performing I/O directly.
Claims: a-sB02-f000256-c13, b-bk02-f000256-c5

## library-panic--never-panic-return-result: Return `Result`; constructors and runtime-checkable conditions return errors
tag: taste
Advocates hold that constructors and runtime-checkable operations should return `Result` rather than `unwrap`/`assert`/panic internally, converging in one case on a safe function returning `Result<Transfer<'_>, Error>` in place of asserts, and in another on a library-wide guarantee that any panic reaching the host is treated as a bug.
Claims: a-sa09-f004055-c6, b-sR12-f005421-c1, b-sb05-f001512-c1, a-sa09-f004055-c7

## library-panic--no-ad-hoc-panics: No ad hoc panics; only control-flow-contingent ones
tag: taste
Advocates hold ad hoc panics used as a short-circuit bail-out are bad practice, preferring panics reserved for cases genuinely tied to control flow, while allowing that other Rust practitioners may disagree.
Claims: a-sa21-f011069-c5

## library-panic--unwrap-only-in-tests: `unwrap` only in tests or provably safe spots
tag: taste
Advocates hold `unwrap` is acceptable only in tests, or in spots where reading the current function shows a panic can never actually occur.
Claims: a-sa06-f003414-c3

## library-panic--prevent-via-explicit-check: Prevent the invalid case with an explicit check
tag: tradeoff
Advocates hold that rather than letting an invalid input fail deep inside an algorithm, an explicit up-front check should reject it early with a clear error message.
Claims: b-sR10-f004573-c2

## library-panic--panic-fine-if-documented: Panicking is fine if documented
tag: taste
Advocates hold a panic path can be acceptable as long as it is listed in the function's `# Panics` documentation, so a user isn't surprised by hitting it.
Claims: b-sR10-f004573-c1

## lifetimes-on-structs--borrow-for-measured-performance: Add lifetime parameters where a measured bottleneck justifies them
tag: fact
Advocates hold that converting an owned type to one carrying borrowed/owned variants (`Value<'a>` with `Cow`-like semantics) was the key change that closed a measured performance gap, getting within ~10ns of native code versus 147ns for the original owned implementation.
Claims: b-sb20-f007364-c1

## lifetimes-on-structs--owned-by-default: Avoid lifetimes on structs as a rule; favor easy-mode owned types, especially for teams new to Rust
tag: taste
Advocates hold that, while experimenting with borrow-checker fights builds useful intuition, the actionable rule of thumb when stuck is to keep lifetime parameters off struct definitions.
Claims: b-sb20-f007608-c2

## lightweight-clones-in-language--p1: Add lightweight/automatic clone ergonomics to Rust itself
tag: taste
Advocates hold that adding lightweight, automatic-clone ergonomics (a "generational box" style mechanism) for callback-heavy UI code is critical to the success of high-level Rust, while acknowledging the proposal is contested and opinions are divided.
Claims: a-sa26-f011305-c3

## lint-allow-broad-vs-narrow--p1: Broad allow when linter blind to trait indirection
tag: fact
Advocates hold a blanket `#![allow(unused)]` should stay because the compiler's lint cannot see that trait operations are being consumed indirectly through a macro like `#[tracing::instrument]`, so a narrower, item-level allow would misfire.
Claims: a-sR11-f003983-c1

## lld-default-linker--p1: Make rust-lld the default linker on x86_64-unknown-linux-gnu for stable releases
tag: fact
Advocates hold that after internal testing on CI, crater and nightly with no major issues, a measured ~7x incremental-link and 40% end-to-end speedup is worth the small risk that `lld` isn't bug-for-bug compatible with GNU `ld`, switching the default while keeping an escape hatch.
Claims: b-sb23-f009657-c1

## llm-doc-edits-reproducibility--p1: Pre review guidelines for llms
tag: taste
Advocates hold the doc-consistency effort should result in additions to the project's developer guidelines that, among other things, help LLMs pre-review changes.
Claims: b-sb16-f004997-c1

## llm-doc-edits-reproducibility--p2: Adopt-controlled-language-standard-ASD-STE100
tag: taste
Advocates hold mandating a controlled-language standard like ASD-STE100 Simplified Technical English constrains vocabulary and grammar enough to remove model "taste" from the equation, keeping the prose consistent and free of "flowery nonsense."
Claims: b-sb16-f004997-c4, b-sb16-f004997-c2

## llm-doc-edits-reproducibility--p3: Declare model prompt and clean env
tag: taste
Advocates hold that merging an LLM-driven doc pass requires declaring which model was used (since each model has its own "taste"), declaring the exact prompt (wording changes results), and running the update in a clean environment to avoid picking up incidental local agent rules.
Claims: b-sb16-f004997-c3

## lts-release-channel--support-old-lines: Keep older lines supported (LTS train, backport the fix)
tag: tradeoff
Advocates hold that a too-fast release cadence should be answered with designated LTS releases carrying guaranteed multi-year API-compatible security patches, letting users upgrade on a slower cadence while still receiving fixes.
Claims: b-sR06-f002937-c1

## lts-release-channel--upgrade-instead: No backport; upgrade
tag: taste
Advocates hold a reported fix should not be backported to an older line; users should follow the upgrade guide instead.
Claims: b-sT05-f002501-c1

## macro-hides-construction-requirements--p1: Macros may hide complexity
tag: tradeoff
Advocates hold that a less-friendly, more verbose way of constructing something is an acceptable cost because existing macros hide that friction from end users.
Claims: b-sR10-f004804-c3

## macro-ide-tooling--p1: Build new tooling rather than accept macro IDE opacity
tag: tradeoff
Advocates hold that since Rust macros lack autocomplete and partial expansion, new libraries should be built to give macro-based DSLs real IDE support rather than accepting the opacity.
Claims: a-sa26-f011305-c4

## macro-vs-boilerplate--macros-sparingly: Use macros sparingly; prefer functions, derives or macro-free APIs; boilerplate is an acceptable price
tag: taste
Advocates hold macros are like salt — powerful but to be used sparingly — and that for most real applications, boilerplate is tolerable or main() needs custom per-case initialization a fully-generated main forecloses; a macro is reserved for a case repeated in several places (better a function first), or for many simple, uniform call sites (e.g. many simple Lambdas) with low tolerance for boilerplate.
Claims: a-sa23-f011186-c3, b-sb20-f007736-c1, b-sb20-f007760-c1, a-sR08-f003082-c1, a-sa17-f007736-c1

## memory-safety-and-resource-leaks--safety-does-not-prevent-leaks: It does not prevent resource leaks
tag: fact
Advocates hold plainly that Rust's memory-safety guarantees do not mitigate memory leaks: a production team leaked tokio tasks and threads and only found the bugs through load simulation and profiling, not through the safety guarantees themselves.
Claims: b-sR05-f002341-c1, a-sR07-f002341-c1

## memory-safety-design-priority--p1: Rust over invested in safety at cost of metaprogramming
tag: taste
Advocates hold that Rust spent so much of its design budget on memory safety alone that it became a lopsided, "disharmonic" language with little else developed.
Claims: a-sa28-f012469-c5

## memory-safety-design-priority--p2: Safety first was the right call, metaprogramming will follow
tag: taste
Advocates hold that solving the hard part — memory management without a GC — first was the right foundation for a young language, and expect the missing "muscle" (easier, more powerful metaprogramming) to come in time.
Claims: a-sa28-f012469-c6

## memory-safety-vs-correctness-frame--p1: Correctness is the real target
tag: taste
Advocates hold that every blog post that over-fits on memory safety is a missed opportunity to talk about correctness, which is a strict superset of memory safety and what actually matters.
Claims: b-sb19-f005743-c7

## merge-expensive-feature-with-limits--p1: Ship with documented limits
tag: tradeoff
Advocates hold the feature should ship now: a fixed, small-width enum (Px1/Px2/Px3) makes the performance ceiling explicit to users while still allowing the common case, and the exponential cost can simply be documented in the public API doc comment rather than blocking the feature outright.
Claims: a-sa05-f003126-c1, a-sa05-f003126-c2

## merge-expensive-feature-with-limits--p2: Hold for proper solution
tag: tradeoff
Advocates hold reluctance to merge something this slow and rough, wanting a proper SDF-based solution instead, and — even after batching improvements — remain negative because most users won't read the docs closely enough to avoid the performance cliff and visible artifact bugs.
Claims: a-sa05-f003126-c4, a-sa05-f003126-c3

## metal-vs-cpu-priority-candle--p1: Prioritize metal next
tag: taste
Advocates hold Metal/GPU support is the top engineering priority for the next major push, ahead of further quantized-CPU work.
Claims: b-sR01-f000464-c2
