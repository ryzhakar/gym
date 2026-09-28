# Fill A — position summaries, file 07

## lambda-vs-containers

### lambda-vs-containers--serverless-first (Default to serverless once measured, or build on edge primitives)
Advocates argue that matching each data need to the right storage primitive (queryable durable store, KV, blob storage, atomic coordination) lets serverless operations largely vanish and cost scale to zero; after porting a real web API and background service off an always-on container, latency held steady, memory use dropped to a fraction of the container's, cold starts were a small minority of invocations, and they conclude serverless — not the container/Kubernetes path — is what should be reached for by default, even for teams that later graduate to Kubernetes once they understand their workload.
Tag: tradeoff.
Claims: b-sT07-f004166-c1, a-sa24-f011220-c1.

### lambda-vs-containers--split-by-workload (Serverless for infrequent or test traffic, containers for always-on)
Advocates say an app that's costly to run 24/7 on Lambda can be cheap on ECS, so the right split is infrequent or test environments on Lambda and always-on production on containers — explicitly naming this "a tradeoff" since test and production then run on meaningfully different infrastructure, judged worth it for the cost savings in some scenarios.
Tag: tradeoff.
Claims: b-sb20-f007797-c1, a-sa17-f007797-c1.

## land-hal-separate-now-vs-unified-later

### land-hal-separate-now-vs-unified-later--p1 (Land it as a side crate now; unify later)
Advocates want previously private work upstreamed as soon as possible so an old, siloed fork can be deprecated and archived, with a path to unifying the new crate into the shared HAL once that becomes possible, now that the code lives in the same repo.
Tag: tradeoff.
Claims: b-sR09-f003955-c1.

### land-hal-separate-now-vs-unified-later--p2 (Same — merge as-is now, deprecate once the unified HAL is ready)
Advocates describe the same plan from the other side: get it merged as-is now, switch it onto the shared metapac once that's ready, and deprecate it in favor of the combined HAL once that arrives, without it being "a big deal" for users to switch.
Tag: tradeoff.
Claims: b-sR09-f003955-c2.

## language-safety-vs-hw-isolation

### language-safety-vs-hw-isolation--p1 (Language safety insufficient for untrusted code)
Advocates say Rust protects against a user "holding it wrong" — accidental misuse — but not against intentional, deliberate misuse, which is what real fine-grained security between mutually adversarial code would require; language-level capabilities and effect systems can't solve multi-tenant isolation unless literally every piece of code sharing the address space is trusted, unsafe-forbidden Rust compiled by a trusted compiler, which is viable for a single-application unikernel but not for many mutually distrusting applications together.
Tag: fact.
Claims: a-saL1-f005360-c4, a-saL1-f005360-c6.

### language-safety-vs-hw-isolation--p2 (Language safety a major step toward safe libOS)
Advocates concede Rust "might not be there yet" for full language-level security, but argue it already solved the hardest combined problem — safety plus performance — needed to make a high-performance library-OS design viable, with missing pieces like capability and effect systems expected to emerge next.
Tag: fact.
Claims: a-saL1-f005360-c5.

## large-pr-split

### large-pr-split--split-into-small-prs (Split before merging)
Advocates say reviewing one huge combined branch is hard and risky, so it's better to treat that branch as a development hub and extract small, isolated PRs from it for actual merging.
Tag: tradeoff.
Claims: b-sb08-f002518-c3.

## leaky-signal-abstraction-electrical-config

### leaky-signal-abstraction-electrical-config--p1 (A leaky abstraction, kept for convenience)
Advocates say peripheral I/O ideally shouldn't need to know about drive strength, pull resistors, or input/output mode, and name the current design a leaky abstraction, pointing to the random null methods `DummyPin`/`Level` must carry as the visible symptom.
Tag: tradeoff.
Claims: a-sR06-f002005-c1.

## library-auth-opinionated-vs-unopinionated

### library-auth-opinionated-vs-unopinionated--authenticated-managed-default (The managed service authenticates relays by default)
Advocates argue an open relay's URL ships in every client and leaks, so anyone who learns it can spend its finite bandwidth; managed relays deployed from a given date onward require a signed, expiring, endpoint-bound token issued from the project's API key, while relays deployed earlier stay open unless switched over.
Tag: tradeoff.
Claims: a-sT11-f004960-c1a, a-sT11-f004960-c1b.

### library-auth-opinionated-vs-unopinionated--unopinionated-library (The library stays unopinionated for self-hosted relays)
Advocates say the library itself is unopinionated about authentication for self-run relays — operators can build their own authentication scheme — leaving that choice untouched even as the managed service defaults to authenticated tokens.
Tag: tradeoff.
Claims: b-sR11-f004960-c1.

## library-error-type-opaque-vs-typed

### library-error-type-opaque-vs-typed--concrete-typed-errors (Concrete, enumerable error types over anyhow)
Advocates made all public APIs return concrete error types instead of `anyhow::Error`, describing it as a large change touching most of the codebase.
Tag: tradeoff.
Claims: b-sb10-f003188-c2.

### library-error-type-opaque-vs-typed--hybrid-snafu (A hybrid with automatic backtraces)
Advocates vastly reduced their use of `anyhow` in favor of the `snafu` crate, which gives concrete, enum-based errors like `thiserror` plus automatic backtrace and span-trace capture per variant, working around the `Into`-trait conflict that otherwise forces a choice between ergonomic `?` and backtraces.
Tag: tradeoff.
Claims: b-sb10-f003222-c1, a-sa14-f005149-c1.

### library-error-type-opaque-vs-typed--typed-over-time (Move toward typed errors as the codebase matures)
Advocates recall starting out happily using `anyhow` broadly, but over time coming to see well-structured, typed error handling as far more valuable, while noting they still use `anyhow` for some things.
Tag: tradeoff.
Claims: a-saL2-f011092-c6.

### library-error-type-opaque-vs-typed--wrap-in-anyhow-for-context (Wrap typed errors in anyhow/eyre for logged context)
Advocates note `thiserror` currently only supports the default `{}` display format, which loses source-error context (e.g. an AWS SDK error's underlying resource info), so the workaround for logging is to wrap errors in `anyhow` or `eyre`, which support the alternate `{:#}` display that carries the full chain.
Tag: tradeoff.
Claims: a-sa18-f008583-c1, b-sb21-f008583-c1.

## library-io-factored-out

### library-io-factored-out--p2 (Bring your own threads)
Advocates say since spawning threads panics on `wasm32-unknown-unknown`, a portable library should factor thread spawning out to the caller — "bring their own threads" — the same way it factors out I/O, which also plays nicer with apps that own a custom thread pool.
Tag: tradeoff.
Claims: a-sB02-f000256-c14.

### library-io-factored-out--p3 (Factor I/O out; accept in-memory slices, let the caller perform I/O)
Advocates say since the Web has no filesystem and only async I/O, a portable library should factor I/O out of itself entirely, taking input slices from callers rather than reading files or performing I/O itself — illustrated with a before/after refactor turning an `fs::read`-based function into one that just takes `&[u8]`.
Tag: tradeoff.
Claims: a-sB02-f000256-c13, b-bk02-f000256-c5.

## library-panic

### library-panic--never-panic-return-result (Return Result; constructors and runtime-checkable conditions return errors)
Advocates push back whenever a `Result`-returning path is reverted to an `assert` or `unwrap`, proposing instead a fallible `try_` variant with a panicking convenience wrapper on top, or making the whole function safe and returning `Result` with explicit runtime validation; one project states outright that any panic reaching the host application is a bug, not an acceptable outcome, and is coded under that guarantee.
Tag: tradeoff.
Claims: a-sa09-f004055-c6, b-sR12-f005421-c1, b-sb05-f001512-c1, a-sa09-f004055-c7.

### library-panic--unwrap-only-in-tests (unwrap only in tests or provably safe spots)
Advocates flag new `unwrap()` calls as needing early returns instead, treating `unwrap` as acceptable only in tests or where the current function makes a panic provably impossible by inspection.
Tag: tradeoff.
Claims: a-sa06-f003414-c3.

### library-panic--no-ad-hoc-panics (No ad hoc panics; only control-flow-contingent ones)
Advocates, even while admitting to using a panic themselves as an ad hoc short-circuit, state they consider ad hoc panics bad practice and prefer panics reserved for cases specifically tied to control flow, while flagging that other Rust practitioners may disagree.
Tag: taste.
Claims: a-sa21-f011069-c5.

### library-panic--prevent-via-explicit-check (Prevent the invalid case with an explicit check)
Advocates add an explicit check that rejects an invalid input up front with a clear message, rather than letting it fail deep inside the algorithm.
Tag: tradeoff.
Claims: b-sR10-f004573-c2.

### library-panic--panic-fine-if-documented (Panicking is fine if documented)
Advocates accept a panic path as acceptable so long as it's listed in the function's `# Panics` documentation, so a user isn't surprised by it.
Tag: tradeoff.
Claims: b-sR10-f004573-c1.

## lifetimes-on-structs

### lifetimes-on-structs--owned-by-default (Avoid lifetimes on structs as a rule)
Advocates say that while experimenting with the borrow checker builds useful intuition, the actionable rule of thumb once you get stuck is to keep lifetime parameters off struct definitions.
Tag: tradeoff.
Claims: b-sb20-f007608-c2.

### lifetimes-on-structs--borrow-for-measured-performance (Add lifetimes where a measured bottleneck justifies them)
Advocates converted an owned, hashmap-based value type to a borrowed one with `Cow`-like borrowed/owned variants, naming this the key change that brought an evaluation within ~10ns of native code, down from 147ns for the original owned implementation.
Tag: fact.
Claims: b-sb20-f007364-c1.

## lightweight-clones-in-language

### lightweight-clones-in-language--p1 (Add lightweight/automatic clone ergonomics to Rust itself)
Advocates propose a Rust project goal adding lightweight clones for reference-counted smart pointers, prototyped as a "generational box," describing it as a controversial but — in their opinion — critical change for the success of high-level Rust, while acknowledging opinions on it are divided.
Tag: tradeoff.
Claims: a-sa26-f011305-c3.

## lint-allow-broad-vs-narrow

### lint-allow-broad-vs-narrow--p1 (Broad allow when the linter is blind to trait indirection)
Advocates keep a blanket `#[allow(unused)]` because the compiler's lint can't see that certain trait operations are actually consumed indirectly through a macro like `#[tracing::instrument]`, so item-level allows would misfire.
Tag: fact.
Claims: a-sR11-f003983-c1.

## lld-default-linker

### lld-default-linker--p1 (Make rust-lld the default linker on x86_64-unknown-linux-gnu)
Advocates, after internal testing across CI, crater, and nightly for over a year with no major issues, judge a roughly 7x incremental-link and 40% end-to-end build speedup worth the small risk that the new linker isn't bug-for-bug compatible with GNU ld, while keeping an explicit escape hatch to opt back out.
Tag: tradeoff.
Claims: b-sb23-f009657-c1.

## llm-doc-edits-reproducibility

### llm-doc-edits-reproducibility--p1 (Pre-review guidelines for LLMs)
Advocates expect the doc-consistency effort to trigger a lot of bikeshedding, and hope that debate results in additions to the project's developer guidelines that also help LLMs pre-review changes.
Tag: tradeoff.
Claims: b-sb16-f004997-c1.

### llm-doc-edits-reproducibility--p2 (Adopt a controlled-language standard, ASD-STE100)
Advocates propose mandating a standard like ASD-STE100 Simplified Technical English so the prose style stays consistent and free of "flowery nonsense," arguing a controlled vocabulary and grammar largely remove a model's "taste" from the equation on their own.
Tag: tradeoff.
Claims: b-sb16-f004997-c4, b-sb16-f004997-c2.

### llm-doc-edits-reproducibility--p3 (Declare model, prompt, and clean environment)
Advocates argue merging an LLM-driven doc pass requires declaring exactly which model was used (since each model has its own "taste"), declaring the exact prompt (wording changes the results), and running the update in a clean environment to avoid picking up incidental local agent rules.
Tag: tradeoff.
Claims: b-sb16-f004997-c3.

## lts-release-channel

### lts-release-channel--support-old-lines (Keep older lines supported)
Advocates moved from supporting each monthly release for only two months — which forced embedders to track upstream closely for security fixes — to designating every 12th release an LTS release, guaranteed 24 months of API-compatible security patches without backported features, so users can upgrade yearly while still getting fixes.
Tag: tradeoff.
Claims: b-sR06-f002937-c1.

### lts-release-channel--upgrade-instead (No backport; upgrade)
Advocates decline to apply a fix to an older version line, pointing instead to the project's upgrade guide.
Tag: tradeoff.
Claims: b-sT05-f002501-c1.

## macro-hides-construction-requirements

### macro-hides-construction-requirements--p1 (Macros may hide complexity)
Advocates note a new reference type makes constructing buffers directly less friendly, but that friction is absorbed by the project's existing macros so end users never see it.
Tag: tradeoff.
Claims: b-sR10-f004804-c3.

## macro-ide-tooling

### macro-ide-tooling--p1 (Build new tooling rather than accept macro IDE opacity)
Advocates, faced with Rust macros not supporting autocomplete or partial expansion, built a separate library to give macro-based DSLs IDE support rather than accepting the opacity.
Tag: tradeoff.
Claims: a-sa26-f011305-c4.

## macro-vs-boilerplate

### macro-vs-boilerplate--macros-sparingly (Use macros sparingly; boilerplate is an acceptable price)
Advocates compare macros to salt — powerful, but meant to be used in small amounts — and, across several concrete cases, default against reaching for a macro: for most real applications the boilerplate is tolerable or custom per-case initialization code forecloses a fully-generated alternative, a repeated sequence should become a plain function rather than a macro if it appears in several places, and a bit of boilerplate is worth keeping the flexibility to customize initialization.
Tag: tradeoff.
Claims: a-sa23-f011186-c3, b-sb20-f007736-c1, b-sb20-f007760-c1, a-sR08-f003082-c1, a-sa17-f007736-c1.

## memory-safety-and-resource-leaks

### memory-safety-and-resource-leaks--safety-does-not-prevent-leaks (It does not prevent resource leaks)
Advocates state outright that Rust's memory-safety guarantees do not mitigate memory leaks, recounting a production incident where leaked tokio tasks and threads were found only through load simulation and profiling, not through the language's safety guarantees.
Tag: fact.
Claims: b-sR05-f002341-c1, a-sR07-f002341-c1.

## memory-safety-design-priority

### memory-safety-design-priority--p1 (Rust over-invested in safety at the cost of metaprogramming)
Advocates argue Rust dedicated so much of its design budget to the difficult memory-safety problem that it became a lopsided, "disharmonic" language with one strong capability and comparatively little developed elsewhere.
Tag: taste.
Claims: a-sa28-f012469-c5.

### memory-safety-design-priority--p2 (Safety first was the right call; metaprogramming will follow)
Advocates reframe the "lopsided" critique as high praise: solving the hard part — memory management without a garbage collector — first gives a young language a great foundation, and they trust the remaining capabilities, mainly easier and more powerful metaprogramming, will come in time.
Tag: taste.
Claims: a-sa28-f012469-c6.

## memory-safety-vs-correctness-frame

### memory-safety-vs-correctness-frame--p1 (Correctness is the real target)
Advocates say every time a piece of writing over-fits on memory safety, it's a missed opportunity to talk about correctness instead, which is the strict superset of memory safety and the property that actually matters.
Tag: taste.
Claims: b-sb19-f005743-c7.

## merge-expensive-feature-with-limits

### merge-expensive-feature-with-limits--p1 (Ship with documented limits)
Advocates favor shipping the feature with its algorithmic cost made explicit rather than blocked: a fixed, small-width enum communicates the performance ceiling directly to users, or the exponential cost is simply named in the public API's doc comment, in both cases still allowing the common case to work today.
Tag: tradeoff.
Claims: a-sa05-f003126-c1, a-sa05-f003126-c2.

### merge-expensive-feature-with-limits--p2 (Hold for a proper solution)
Advocates remain reluctant to merge something this slow and rough even after improvements, wanting a proper efficient (SDF-based) approach instead, and note that most users won't carefully read documentation closely enough to avoid the performance cliff or the remaining visible artifact bugs.
Tag: tradeoff.
Claims: a-sa05-f003126-c4, a-sa05-f003126-c3.

## metal-vs-cpu-priority-candle

### metal-vs-cpu-priority-candle--p1 (Prioritize Metal next)
Advocates name Metal/GPU support as the top priority for the project's next major engineering push, ahead of further quantized-CPU work.
Tag: tradeoff.
Claims: b-sR01-f000464-c2.
