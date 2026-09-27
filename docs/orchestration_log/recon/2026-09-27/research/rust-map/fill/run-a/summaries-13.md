# Fill A — summaries, file 13

## Question `ui-async-data-cache-vs-component`

### ui-async-data-cache-vs-component--p1
A hand-rolled cache, hover-triggered prefetch, and version-keyed invalidation are accidental complexity that exists only because a popover builder is synchronous; the fix is to let the menu entity spawn its own async fetch and render a loading state — "how every picker works" — which one reviewer's rework then delivered: one async menu entity fetching its own data per step, eliminating the cache, prefetch, and re-anchoring flag by construction.
tag: tradeoff
claims: a-sa13-f004772-c1, a-sa13-f004772-c2

## Question `ui-dsl-vs-plain-rust`

### ui-dsl-vs-plain-rust--p1
Recommends egui to readers who want zero DSL/macros and plain Rust, and Slint to readers who want a DSL with serious dev-tooling investment (a better error-message ceiling since it's a standalone language), without picking an overall winner between the two approaches.
tag: fact
claims: b-sb21-f008390-c2

## Question `ui-state-scoped-lifetimes-vs-runtime-handles`

### ui-state-scoped-lifetimes-vs-runtime-handles--p1
Removed the `'bump`-lifetime scope model because it doesn't work with `'static` futures and produces confusing lifetime errors, replacing it with `Copy` signals backed by a generational-box allocator — described as bolting a light form of garbage collection onto Rust, using component lifecycles as the trigger for dropping state.
tag: tradeoff
claims: b-sb17-f005144-c1

## Question `unchecked-unwrap-vs-safe-abort`

### unchecked-unwrap-vs-safe-abort--p1
To cut panic-related code bloat from `unwrap`, prefer a safe helper that calls `process::abort()` on `None`/`Err` over letting the formatted panic machinery run, since panics compile down to aborts on `wasm32-unknown-unknown` anyway.
tag: tradeoff
claims: a-sB02-f000256-c8

### unchecked-unwrap-vs-safe-abort--p2
The `unreachable` crate's unsafe `unchecked_unwrap` is offered as a further, riskier alternative, but restricted to cases where the programmer is "110% sure" the assumption holds, and only in release builds, keeping checked behavior in debug.
tag: tradeoff
claims: a-sB02-f000256-c9

### unchecked-unwrap-vs-safe-abort--p3
Presents the safe `process::abort`-based wrapper as the default way to drop panic-infrastructure bloat, and the `unreachable` crate's unsafe `unchecked_unwrap` as a further, riskier step, explicitly conditioning its use on near-total certainty plus a debug build that still checks.
tag: tradeoff
claims: b-bk02-f000256-c12

## Question `uniffi-packaging-xcode-vs-script`

### uniffi-packaging-xcode-vs-script--p1
It's possible to wire UniFFI's binding generation into an Xcode build phase, but that was rejected given the relative difficulty and the overall flakiness of the Xcode build process, choosing a plain shell script invoked manually or by CI instead, at the cost of needing a manual rebuild after Rust changes.
tag: tradeoff
claims: a-sa27-f012237-c1

## Question `unmaintained-dependency-weight`

### unmaintained-dependency-weight--p1
A crate flagged unmaintained, buggy and legacy per a RustSec advisory should give way to a more modern crate, even when that modern crate's stated focus (the Web) is narrower than the original's scope.
tag: tradeoff
claims: a-sa06-f003414-c1

## Question `unsafe-fields-design`

### unsafe-fields-design--p1
After an observation that the additive/subtractive dichotomy and its Drop-related concerns could be sidestepped (a field already can't be put into an unsound-to-drop state without unsafe code), field safety tooling was reduced to two rules: a field is marked unsafe if it carries a safety invariant, and a field marked unsafe is unsafe to use — weighed against a proposed hybrid of syntactic markers and wrapper types.
tag: fact
claims: a-sa20-f009698-c2

## Question `unsafe-mental-model`

### unsafe-mental-model--p1
Unsafe code isn't for violating Rust's invariants — it's for maintaining them manually.
tag: taste
claims: a-sa28-f012469-c11

### unsafe-mental-model--p2
Using unsafe is "less 'nuclear option' and more 'diplomacy has failed'" — a last resort, not an extreme, rarely-justified tool.
tag: taste
claims: a-sa28-f012469-c12

## Question `unsafe-trait-vs-unsafe-method`

### unsafe-trait-vs-unsafe-method--p1
Correctness could be enforced either by marking the trait itself unsafe or by leaving the consuming accessor method unsafe since the implementer can't be trusted; the shipped design trusts the derive macro to build a valid accessor and puts the unsafe contract on the consuming method instead of the trait, which the other party agrees with.
tag: tradeoff
claims: a-sa07-f003716-c1, a-sa07-f003716-c2

## Question `unstable-feature-gate-vs-wait`

### unstable-feature-gate-vs-wait--ship-gated-unstable
New trait and type surface (a `PathSelector` trait; a custom-transport API) ships now, gated behind an unstable feature flag and explicitly excluded from the 1.0 stability guarantee, declared unstable and likely to remain so even well past the 1.0 release line.
tag: tradeoff
claims: b-sR10-f004741-c2, b-sR10-f004423-c2

## Question `unstable-marking-of-required-macros`

### unstable-marking-of-required-macros--p1
The `entry` macro quite obviously needs to stay stable, since without it users can't write `main` and therefore can't use the crate at all.
tag: tradeoff
claims: b-sb08-f002517-c4

## Question `verify-crates-io-against-source`

### verify-crates-io-against-source--p1
Built a comparator between crates.io tarballs and their git repositories across nearly all of crates.io, and released the raw dataset rather than holding it back for private review first, citing lack of time to review it all.
tag: taste
claims: a-sR14-f005287-c1

## Question `view-macro-native-control-flow`

### view-macro-native-control-flow--p1
Added native `for`-loop syntax directly usable inside the templating macro, alongside the existing iterator-adapter style, because it makes iteration "more natural."
tag: taste
claims: b-sR09-f003938-c1

## Question `warn-missing-edition`

### warn-missing-edition--p1
Given how significant edition differences have become, rustc should warn whenever invoked with no `--edition`, since almost no one today intends the 2015 default; implemented as an undismissable "note" rather than a lint specifically so `forbid`/`deny(warnings)` setups used by build probes aren't broken by it.
tag: tradeoff
claims: a-sa19-f009343-c1, a-sa19-f009343-c2

## Question `wasi-path-workaround-vs-breaking-fix`

### wasi-path-workaround-vs-breaking-fix--p1
After a workaround PR was closed for not being an ideal fix, argues it's still worth shipping since it makes real-world extensions work now, packaging it as a community build — "perfect shouldn't be the enemy of functional."
tag: taste
claims: b-sb07-f002307-c1

### wasi-path-workaround-vs-breaking-fix--p2
Argues the proper fix is the breaking extension-API change, and even though it's a breaking change, compatibility should be handled by shipping a new versioned extension-API rather than settling permanently for the older workaround.
tag: tradeoff
claims: b-sb07-f002307-c2

## Question `wasip2-std-minimal-imports`

### wasip2-std-minimal-imports--p1
Using a simple std facility makes the compiled component import the whole `wasi:cli` world, including useless interfaces such as `wasi:cli/env`; filed as a still-open issue.
tag: fact
claims: a-sT12-f008237-c2

## Question `wasm-allocator-choice`

### wasm-allocator-choice--p1
The default dlmalloc-based allocator costs roughly 10KB; replacing it with wee_alloc trades allocation speed for saving most of that size, recommended when allocation can't be avoided entirely.
tag: tradeoff
claims: a-sB02-f000256-c11

### wasm-allocator-choice--p2
For a single-instance program, exporting operations on a static mut global with double-buffering removes all dynamic allocation, allowing a `#![no_std]` crate with no allocator dependency at all, for maximum size reduction.
tag: tradeoff
claims: a-sB02-f000256-c12

### wasm-allocator-choice--p3
Names the default allocator's ~10KB footprint as the cost of keeping it and wee_alloc's slower allocation as the cost of switching, framing the choice explicitly as trading allocation speed for code size.
tag: tradeoff
claims: b-bk02-f000256-c11

## Question `wasm-bindgen-manual-vs-generated-glue`

### wasm-bindgen-manual-vs-generated-glue--p1
Manual conversion with `js_sys` is a reasonable but time-consuming, brittle strategy; leaning into bindgen's generated glue, accepting its naming and wrapper conventions, buys better compile-time feedback.
tag: tradeoff
claims: b-sb19-f005691-c1

## Question `wasm-boundary-serde-vs-getters`

### wasm-boundary-serde-vs-getters--p1
After surveying GitHub crates, found people mostly doing the right thing already: using serde-wasm-bindgen (more ergonomic, more allocation) for cold paths like config initialization, and wasm-bindgen getters/reflection (faster, less ergonomic) for hot paths where needed.
tag: fact
claims: a-sa26-f011460-c3

## Question `wasm-bundler-choice`

### wasm-bundler-choice--p1
The tutorial's template uses webpack as bundler/dev-server, stating this isn't required — Parcel and Rollup also support wasm as ES modules, and no bundler at all is viable — webpack is picked "for convenience."
tag: taste
claims: a-sB02-f000256-c17

## Question `wasm-capabilities-explicit-vs-ambient`

### wasm-capabilities-explicit-vs-ambient--p1
An auth middleware can reach an endpoint only because the underlying component grants that capability and the trigger explicitly inherits it; middleware gets no ambient authority otherwise.
tag: tradeoff
claims: b-sR11-f005050-c1

## Question `wasm-components-for-interop`

### wasm-components-for-interop--wasm-components
SDK-based tool calling couples tool instances to the calling application's runtime and can't be reused externally, whereas composing independently-built WebAssembly components (regardless of source language) solves discovery, portability and sandboxing better; separately, legacy C ABIs are called fragile and dangerous as a foundation for interop, a pain that composing through compatible WIT interfaces relieves.
tag: tradeoff
claims: a-sa07-f003922-c1, a-sT12-f008237-c1

## Question `wasm-core-sum-types`

### wasm-core-sum-types--p1
First-class sum types would let compilers emit a `br_table`-like instruction for exhaustively matching on cases instead of a chain of `br_on_cast` checks, which is easier to optimize and lets tools like binaryen reason over a closed case set.
tag: tradeoff
claims: a-sa05-f003074-c4

### wasm-core-sum-types--p2
A custom type descriptor can already store an integer tag for `br_table` dispatch without wasting per-variant space, so primitive sum types would mainly save the trailing cast check — which requires substantial new Wasm machinery for limited additional gain.
tag: tradeoff
claims: a-sa05-f003074-c5

## Question `wasm-instantiate-streaming-vs-bytes`

### wasm-instantiate-streaming-vs-bytes--p1
There's no need for the complex wrapping into a `Response`; `instantiateStreaming` has no benefit once the whole file is already loaded as a blob, so revert to the regular `instantiate`, which can take the bytes directly.
tag: fact
claims: b-sR09-f003815-c1

## Question `wasm-monolithic-vs-small-components`

### wasm-monolithic-vs-small-components--p1
Decoupling the core classification logic into its own Wasm component kept the HTTP control flow lean, standard, and easy to maintain, with the WIT files serving as the single source of truth for the boundary.
tag: tradeoff
claims: b-sR11-f005053-c1

## Question `wasm-panic-hook`

### wasm-panic-hook--p1
Installing the panic hook turns a cryptic, difficult-to-debug "RuntimeError: unreachable executed" trap message into Rust's actual formatted panic message in the console.
tag: fact
claims: a-sB02-f000256-c16

## Question `wasm-panic-unwind-vs-abort`

### wasm-panic-unwind-vs-abort--p1
Added `panic=unwind` support for `wasm32-unknown-unknown` via the WebAssembly Exception Handling proposal so panics can be recovered from without discarding instance state, since `panic=abort`'s default full-reinitialization recovery wipes in-memory state for stateful workloads; shipped behind a flag with plans to make it the default.
tag: tradeoff
claims: a-sa12-f004598-c1

## Question `wasm-precise-traps-store-tearing`

### wasm-precise-traps-store-tearing--p1
Implements precise store-trap semantics by prepending a same-size load before every store on architectures with store tearing, so a trapping store traps via the load first; shipped on by default, accepting a measured ~2% cost on one benchmarked chip pending Wasm spec clarification.
tag: tradeoff
claims: a-02-f001181-c1

## Question `wasm-runtime-swap-vs-host-target`

### wasm-runtime-swap-vs-host-target--p1
The two Wasm targets warrant different answers: swap the async runtime for a browser shim when targeting `wasm32-unknown-unknown`, but for `wasm32-wasip2/3` compile most of the stack unchanged and depend on the existing runtime gaining support for that platform (including UDP/TCP sockets) instead.
tag: tradeoff
claims: b-sR05-f002177-c1

## Question `wasm-undefined-symbols-error`

### wasm-undefined-symbols-error--p1
The current default silently turns undefined or typo'd symbols into WebAssembly imports instead of a build error, pushing the failure from where the mistake is introduced to a later, often confusing runtime failure; removing that default aligns wasm with how all other platforms already treat undefined symbols as an error, and existing intentional users can opt back in per-symbol.
tag: tradeoff
claims: b-sb23-f009737-c1

## Question `web-api-wrapper-raw-vs-rust-types`

### web-api-wrapper-raw-vs-rust-types--p1
A hook exposing browser search params should return a `HashMap<String, String>` rather than the raw `UrlSearchParams` handle.
tag: taste
claims: a-sR07-f002271-c1

## Question `web-framework-actor-vs-tower`

### web-framework-actor-vs-tower--p1
Directs students to default to Clap for CLI and Actix for web "unless you have a compelling reason to switch to a new framework."
tag: taste
claims: a-sB01-f000149-c2

### web-framework-actor-vs-tower--p2
Both frameworks are fast and production-ready, but Axum's design philosophy — simplicity and tight Tokio integration — is "often preferred" over Actix Web's actor-model design and its own mature middleware system.
tag: taste
claims: a-sa26-f011605-c2

## Question `web-framework-macro-free-api`

### web-framework-macro-free-api--p1
What makes the framework stand out in the Rust landscape is specifically its macro-free API design, predictable error-handling model, and Tower-based middleware system.
tag: taste
claims: a-sa26-f011605-c1

## Question `web-session-store-default`

### web-session-store-default--p1
Following Rails' precedent, argues new apps should start with an encrypted-and-signed cookie session store (switchable later) to keep initial friction low, even while granting Rails itself calls the choice "controversial."
tag: tradeoff
claims: b-sb04-f001365-c1

### web-session-store-default--p2
Data stored on the client cannot be force-invalidated or have permissions changed on the fly, negating whatever effort skipping a server-side store saves; separately, encrypted cookies are called not good practice in production since they can enable replay attacks and similar vulnerabilities, with server-side storage always the better choice.
tag: tradeoff
claims: b-sb04-f001365-c2, b-sb04-f001365-c3

## Question `web-wasm-target-workaround-vs-target`

### web-wasm-target-workaround-vs-target--p1
Argues the root cause is the lack of a way to signal wasm-bindgen usage, and that a proper dedicated Wasm-web target would fix this class of problem generally, now that the project has active maintainers again.
tag: taste
claims: a-sa06-f003558-c1

### web-wasm-target-workaround-vs-target--p2
Says there has been zero progress on a proper Web-WASM target in about four years and holds no hope of getting one anytime soon, so the immediate need is a solution that works with current stable Rust and the declared MSRV.
tag: fact
claims: a-sa06-f003558-c2

## Question `what-counts-as-semver-breaking`

### what-counts-as-semver-breaking--p1
Adding a variant to a public enum not marked `#[non_exhaustive]` is classified as breaking, because downstream match expressions that were previously exhaustive stop compiling.
tag: fact
claims: b-bk03-f000267-c12

### what-counts-as-semver-breaking--p2
A dependency bump forces a major-version bump of the crate itself when the dependency's own semver-incompatible change exposes types that appear in the crate's public API, since two incompatible versions of the same crate can't unify for downstream consumers; a purely internal dependency needs no changelog entry at all.
tag: fact
claims: b-bk03-f000267-c13

### what-counts-as-semver-breaking--p3
An MSRV bump is itself classified as a breaking change for the crate, not a minor or patch-level change.
tag: fact
claims: b-bk03-f000267-c14

## Question `wit-dependency-keyword-design`

### wit-dependency-keyword-design--p1
Favors a single `dependency` keyword with locked/unlocked inferred from the syntax that follows it, for regularity and to keep vocabulary aligned with how package managers already use the word "dependency" to refer to implementations.
tag: taste
claims: b-sR05-f001983-c1

## Question `wit-export-direct-vs-interface`

### wit-export-direct-vs-interface--p1
While a world can export a bare function directly, the recommended best practice is to wrap related functions inside a named interface which the world then exports, since this is more modular, extensible, and matches how WIT is used in real multi-function components.
tag: taste
claims: a-sR08-f003033-c1

## Question `work-stealing-vs-thread-per-core`

### work-stealing-vs-thread-per-core--p1
Across 360 benchmarked configurations spanning balanced/unbalanced and CPU- through IO-heavy workloads on three runtimes, io_uring-based executor-per-thread did not strictly outperform epoll-based work-stealing even in the scenario designed to favor it, and work-stealing itself showed unexplained throughput anomalies at certain thread counts; concludes results are inconclusive on "which is faster" and the right choice depends on the application's own workload shape.
tag: fact
claims: a-sa18-f009026-c1

## Question `wrap-third-party-types-in-public-api`

### wrap-third-party-types-in-public-api--p1
Because the language has no standard u256 type, one of several third-party crate implementations is chosen but not exposed directly — it's wrapped behind a local named type, so the underlying crate choice stays swappable.
tag: tradeoff
claims: b-bk03-f000267-c17

## Question `xcframework-tooling-vs-hand-built`

### xcframework-tooling-vs-hand-built--p1
XCFramework's on-disk structure is simple enough that some teams build it by hand, but chose to stick to Apple's official `xcodebuild -create-xcframework` tooling to combine the per-target static libraries, headers and module map instead of replicating that structure manually.
tag: taste
claims: a-sa27-f012237-c2
