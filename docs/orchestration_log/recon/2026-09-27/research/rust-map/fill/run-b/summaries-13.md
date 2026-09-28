# Summaries, batch 1 file 13 (fill b)

## Question `ui-async-data-cache-vs-component`

### ui-async-data-cache-vs-component--p1
Summary: The hand-rolled outline cache, its hover-triggered prefetch, and its version-keyed invalidation are accidental complexity that only exists because the popover builder is synchronous. Let the menu entity spawn its own async fetch and render a loading state instead — "how every picker in Zed works" — and the cache, prefetch and re-anchoring flag disappear by construction, not by patching.
Tag: tradeoff
Claims: a-sa13-f004772-c1, a-sa13-f004772-c2

## Question `ui-dsl-vs-plain-rust`

### ui-dsl-vs-plain-rust--p1
Summary: If you want to avoid DSLs and macros and write only regular Rust, egui offers that; if you like DSL-driven UIs with serious developer-tooling investment (a better error-message ceiling since it's a standalone language, not just macros), Slint might be for you — no overall winner between the two approaches.
Tag: taste
Claims: b-sb21-f008390-c2

## Question `ui-state-scoped-lifetimes-vs-runtime-handles`

### ui-state-scoped-lifetimes-vs-runtime-handles--p1
Summary: The `'bump`-lifetime scope model doesn't work for `'static` futures and produces confusing lifetime errors — replace it with `Copy` signals backed by a generational-box allocator: essentially a light form of garbage collection bolted onto Rust, using component lifecycles as the trigger for dropping state.
Tag: tradeoff
Claims: b-sb17-f005144-c1

## Question `unchecked-unwrap-vs-safe-abort`

### unchecked-unwrap-vs-safe-abort--p1
Summary: Panics translate into aborts on wasm32-unknown-unknown anyway, so a safe helper that calls `process::abort()` on None/Err gives the same behavior as unwrap without the formatted-panic code bloat.
Tag: tradeoff
Claims: a-sB02-f000256-c8

### unchecked-unwrap-vs-safe-abort--p2
Summary: The `unreachable` crate's unsafe `unchecked_unwrap` is a further, riskier alternative, restricted to cases where the programmer is "110% sure" the assumption holds — and only in release builds, keeping checked behavior in debug.
Tag: tradeoff
Claims: a-sB02-f000256-c9

### unchecked-unwrap-vs-safe-abort--p3
Summary: The safe `process::abort`-based `unwrap_abort` is the default way to drop panic-infrastructure bloat; the unsafe `unchecked_unwrap` is a further step, explicitly conditioned on near-total certainty plus a debug build that still checks.
Tag: tradeoff
Claims: b-bk02-f000256-c12

## Question `uniffi-packaging-xcode-vs-script`

### uniffi-packaging-xcode-vs-script--p1
Summary: It's possible to wire UniFFI's binding generation into an Xcode build phase, but given the relative difficulty of doing that and the overall flakiness of the Xcode build process, a simple, reliable shell script was chosen instead — at the cost of needing a manual rebuild after Rust changes.
Tag: tradeoff
Claims: a-sa27-f012237-c1

## Question `unmaintained-dependency-weight`

### unmaintained-dependency-weight--p1
Summary: A crate flagged unmaintained, buggy and legacy per a RustSec advisory should give way to a more modern crate, even if that replacement's stated focus (e.g. the Web) is narrower than the original's scope.
Tag: tradeoff
Claims: a-sa06-f003414-c1

## Question `unsafe-fields-design`

### unsafe-fields-design--p1
Summary: Field safety tooling reduces to two rules: a field should be marked unsafe if it carries a safety invariant of any kind, and a field marked unsafe is unsafe to use — settled after an observation that the additive/subtractive dichotomy and its Drop-related concerns could be sidestepped, since a field already can't be put into an unsound-to-drop state without unsafe code.
Tag: tradeoff
Claims: a-sa20-f009698-c2

## Question `unsafe-mental-model`

### unsafe-mental-model--p1
Summary: Unsafe code isn't for violating Rust's invariants, it's for maintaining them manually.
Tag: fact
Claims: a-sa28-f012469-c11

### unsafe-mental-model--p2
Summary: Using unsafe is less "nuclear option" and more "diplomacy has failed."
Tag: taste
Claims: a-sa28-f012469-c12

## Question `unsafe-trait-vs-unsafe-method`

### unsafe-trait-vs-unsafe-method--p1
Summary: Correctness here must be enforced either by marking the trait itself unsafe, or by leaving the consuming accessor method unsafe, since the implementer can't otherwise be trusted; the design that shipped trusts the derive macro to build a valid accessor and puts the unsafe contract on the consuming method instead of the trait.
Tag: tradeoff
Claims: a-sa07-f003716-c2, a-sa07-f003716-c1

## Question `unstable-feature-gate-vs-wait`

### unstable-feature-gate-vs-wait--ship-gated-unstable
Summary: New functionality (a `PathSelector` trait and its types; a custom-transport API) ships now, gated behind an unstable flag, explicitly excluded from the stability guarantees and expected to stay unstable for some time — even past a 1.0 release.
Tag: tradeoff
Claims: b-sR10-f004741-c2, b-sR10-f004423-c2

## Question `unstable-marking-of-required-macros`

### unstable-marking-of-required-macros--p1
Summary: `entry` quite obviously needs to be stable — if you can't write `main`, how would you use the crate at all?
Tag: fact
Claims: b-sb08-f002517-c4

## Question `verify-crates-io-against-source`

### verify-crates-io-against-source--p1
Summary: Built a comparator between crates.io tarballs and their git repositories across nearly all of crates.io, and released the raw dataset rather than holding it back, because there wasn't time to review it all first.
Tag: tradeoff
Claims: a-sR14-f005287-c1

## Question `view-macro-native-control-flow`

### view-macro-native-control-flow--p1
Summary: You can now use for-loops directly in the `html!` macro, alongside the existing iterator-adapter form, making iteration more natural.
Tag: taste
Claims: b-sR09-f003938-c1

## Question `warn-missing-edition`

### warn-missing-edition--p1
Summary: rustc ought to warn whenever it is invoked without an `--edition`, since almost nobody writing a rustc invocation today should be using the 2015 edition. Implemented as an undismissable "note" rather than a lint specifically so `forbid`/`deny(warnings)` setups used by build probes aren't broken by it; the only people affected are those explicitly comparing textual compiler output in scripts.
Tag: tradeoff
Claims: a-sa19-f009343-c2, a-sa19-f009343-c1

## Question `wasi-path-workaround-vs-breaking-fix`

### wasi-path-workaround-vs-breaking-fix--p1
Summary: A prior workaround wasn't an ideal fix, but perfect shouldn't be the enemy of functional — it's still worth shipping since it makes real-world extensions work now, packaged as a community Windows build.
Tag: tradeoff
Claims: b-sb07-f002307-c1

### wasi-path-workaround-vs-breaking-fix--p2
Summary: The proper fix is the extension-API change, and even though it's a breaking change, compatibility should be handled by shipping a new extension-API version rather than settling permanently for the older workaround.
Tag: tradeoff
Claims: b-sb07-f002307-c2

## Question `wasip2-std-minimal-imports`

### wasip2-std-minimal-imports--p1
Summary: Using a simple std facility like `format!` makes the compiled component import the whole `wasi:cli` world, including interfaces that are useless in this case (such as `wasi:cli/env`) — filed as an issue that's still open.
Tag: fact
Claims: a-sT12-f008237-c2

## Question `wasm-allocator-choice`

### wasm-allocator-choice--p1
Summary: wee_alloc is designed for situations where you need some kind of allocator but not a particularly fast one, and happily trades allocation speed for smaller code size — the default allocator costs roughly 10KB, and wee_alloc saves most of that.
Tag: tradeoff
Claims: a-sB02-f000256-c11

### wasm-allocator-choice--p2
Summary: For a single-instance program, exporting operations on a static mut global with double-buffering removes all dynamic allocation entirely, allowing a `#![no_std]` crate with no allocator dependency at all — maximum size reduction.
Tag: tradeoff
Claims: a-sB02-f000256-c12

### wasm-allocator-choice--p3
Summary: The choice is explicitly a speed-for-size trade: the default allocator's ~10KB footprint is the cost of keeping it, and wee_alloc's slower allocation is the cost of switching.
Tag: tradeoff
Claims: b-bk02-f000256-c11

## Question `wasm-bindgen-manual-vs-generated-glue`

### wasm-bindgen-manual-vs-generated-glue--p1
Summary: A fair amount of code online prefers manual conversions with js_sys — a reasonable strategy, but found to be time-consuming and brittle in practice; leaning into bindgen's generated glue, and accepting its naming/wrapper conventions, buys better compile-time feedback.
Tag: tradeoff
Claims: b-sb19-f005691-c1

## Question `wasm-boundary-serde-vs-getters`

### wasm-boundary-serde-vs-getters--p1
Summary: After surveying GitHub crates, people are mostly doing the right thing already: serde-wasm-bindgen (more ergonomic, more allocation) for cold paths like config initialization, and wasm-bindgen getters/reflection (faster, less ergonomic) for hot paths, when needed.
Tag: tradeoff
Claims: a-sa26-f011460-c3

## Question `wasm-bundler-choice`

### wasm-bundler-choice--p1
Summary: webpack is not required for working with Rust and WebAssembly — it's just the bundler and development server chosen for convenience here; Parcel and Rollup also support wasm as ES modules, and using Rust+wasm with no bundler at all is viable too.
Tag: taste
Claims: a-sB02-f000256-c17

## Question `wasm-capabilities-explicit-vs-ambient`

### wasm-capabilities-explicit-vs-ambient--p1
Summary: Middleware gets no ambient authority — it can reach an endpoint only because the underlying component grants that capability and the trigger explicitly inherits it; otherwise it gets nothing.
Tag: tradeoff
Claims: b-sR11-f005050-c1

## Question `wasm-components-for-interop`

### wasm-components-for-interop--wasm-components
Summary: SDK-based tool calling couples tool instances to the calling application's runtime and can't be reused externally — a layer of indirection between models and their tools is needed, and composing independently-built WebAssembly components, regardless of source language, solves discovery, portability and sandboxing better. The foundation of software interop is still legacy C ABIs, which are fragile and dangerous; composing through compatible WIT interfaces relieves that pain.
Tag: tradeoff
Claims: a-sa07-f003922-c1, a-sT12-f008237-c1

## Question `wasm-core-sum-types`

### wasm-core-sum-types--p1
Summary: The most immediate benefit first-class sum types would give over shoe-horning sum types into struct subtypes is a `br_table`-like instruction for exhaustively matching on cases — easier to optimize than a chain of `br_on_cast` checks, and lets tools like binaryen reason over a closed case set.
Tag: tradeoff
Claims: a-sa05-f003074-c4

### wasm-core-sum-types--p2
Summary: A custom type descriptor can already store an integer tag for `br_table` dispatch without wasting per-variant space, so primitive sum types would mainly save the trailing cast check — which would require adding a case construct to Wasm, quite a bit of machinery for not a hell lot of relevant generic optimizations.
Tag: tradeoff
Claims: a-sa05-f003074-c5

## Question `wasm-instantiate-streaming-vs-bytes`

### wasm-instantiate-streaming-vs-bytes--p1
Summary: There's no need for the complex wrapping into a `Response` — `instantiateStreaming` doesn't have any benefits when the whole file is already loaded as a blob; revert to the regular `instantiate`, which can take the bytes directly.
Tag: fact
Claims: b-sR09-f003815-c1

## Question `wasm-monolithic-vs-small-components`

### wasm-monolithic-vs-small-components--p1
Summary: Decoupling the core classification logic into its own Wasm component kept the HTTP control flow lean, standard, and easy to maintain, with WIT files as the single source of truth for the boundary between them.
Tag: tradeoff
Claims: b-sR11-f005053-c1

## Question `wasm-panic-hook`

### wasm-panic-hook--p1
Summary: Rather than getting cryptic, difficult-to-debug `RuntimeError: unreachable executed` messages, installing `console_error_panic_hook` gives Rust's actual formatted panic message in the console.
Tag: fact
Claims: a-sB02-f000256-c16

## Question `wasm-panic-unwind-vs-abort`

### wasm-panic-unwind-vs-abort--p1
Summary: To recover from panics without discarding instance state, panic=unwind support for wasm32-unknown-unknown was added to wasm-bindgen via the WebAssembly Exception Handling proposal, because panic=abort's default full-reinitialization recovery wipes in-memory state for stateful workloads like Durable Objects.
Tag: tradeoff
Claims: a-sa12-f004598-c1

## Question `wasm-precise-traps-store-tearing`

### wasm-precise-traps-store-tearing--p1
Summary: On architectures with store tearing (ARMv8, RISC-V), prepend a same-size load to every store so that if the store will trap, the load traps too — implemented and shipped off by default, accepting a measured ~2% cost on Apple M2 Pro, pending Wasm spec clarification.
Tag: tradeoff
Claims: a-02-f001181-c1

## Question `wasm-runtime-swap-vs-host-target`

### wasm-runtime-swap-vs-host-target--p1
Summary: The two Wasm targets warrant different answers: swap out tokio for a browser shim (wasm-bindgen-futures) when targeting `wasm32-unknown-unknown`, but for `wasm32-wasip2/3` compile most of the stack unchanged and depend on tokio gaining support for that platform, including UDP/TCP sockets, instead.
Tag: tradeoff
Claims: b-sR05-f002177-c1

## Question `wasm-undefined-symbols-error`

### wasm-undefined-symbols-error--p1
Summary: All native platforms consider undefined symbols an error by default, so passing `--allow-undefined` introduces surprising behavior specific to WebAssembly targets that kicks a mistake down the road to a confusing runtime failure; removing it as the default aligns wasm with how every other platform already behaves, and existing intentional users can opt back in per-symbol.
Tag: tradeoff
Claims: b-sb23-f009737-c1

## Question `web-api-wrapper-raw-vs-rust-types`

### web-api-wrapper-raw-vs-rust-types--p1
Summary: A hook exposing browser search params should return a `HashMap<String, String>` rather than the raw `UrlSearchParams` handle.
Tag: taste
Claims: a-sR07-f002271-c1

## Question `web-framework-actor-vs-tower`

### web-framework-actor-vs-tower--p1
Summary: Default students to Clap for CLI and Actix for web, unless they have a compelling reason to switch to a new framework.
Tag: taste
Claims: a-sB01-f000149-c2

### web-framework-actor-vs-tower--p2
Summary: Actix Web uses the actor model and has its own mature middleware system; both frameworks are fast and production-ready, but Axum's design philosophy is often preferred for its simplicity and tight integration with Tokio.
Tag: taste
Claims: a-sa26-f011605-c2

## Question `web-framework-macro-free-api`

### web-framework-macro-free-api--p1
Summary: What makes Axum stand out in the Rust framework landscape is its macro-free API design, its predictable error-handling model, and its own middleware system built on Tower.
Tag: taste
Claims: a-sa26-f011605-c1

## Question `web-session-store-default`

### web-session-store-default--p1
Summary: Following Rails' precedent, new apps should start by storing sessions inside the cookie, both encrypted and signed, switchable later via `tower-sessions` — Rails itself calls the choice "controversial," but it keeps initial friction low.
Tag: tradeoff
Claims: b-sb04-f001365-c1

### web-session-store-default--p2
Summary: There's no way to force-invalidate a session or change permissions on the fly when the data lives on the client, so whatever effort is saved by skipping a server-side store is negated by that inflexibility; encrypted cookies also aren't good practice in production since they can enable replay attacks and similar vulnerabilities — storing sensitive data server-side is always the better choice.
Tag: fact
Claims: b-sb04-f001365-c2, b-sb04-f001365-c3

## Question `web-wasm-target-workaround-vs-target`

### web-wasm-target-workaround-vs-target--p1
Summary: The root cause is the lack of a way to signal wasm-bindgen usage to the compiler — shouldn't there finally be a discussion of a proper `wasm32-web`/`wasm32-bindgen` target instead, now that the project has active maintainers again, to fix this class of problem generally?
Tag: tradeoff
Claims: a-sa06-f003558-c1

### web-wasm-target-workaround-vs-target--p2
Summary: There's been zero progress on a Web WASM target in about four years and no hope of getting one anytime soon; `getrandom` needs a solution that works with current stable Rust and the declared MSRV now, and hypothetical language changes are out of scope.
Tag: tradeoff
Claims: a-sa06-f003558-c2

## Question `what-counts-as-semver-breaking`

### what-counts-as-semver-breaking--p1
Summary: Adding a variant to a public enum that is not marked `#[non_exhaustive]` is breaking, because downstream match expressions that were previously exhaustive stop compiling.
Tag: fact
Claims: b-bk03-f000267-c12

### what-counts-as-semver-breaking--p2
Summary: A dependency bump forces a major-version bump of the crate itself when the dependency's own semver-incompatible change exposes types that appear in the crate's public API, since two incompatible versions of the same crate can't unify for downstream consumers; a dependency used only internally needs no changelog entry at all.
Tag: fact
Claims: b-bk03-f000267-c13

### what-counts-as-semver-breaking--p3
Summary: Raising the minimum supported Rust version is itself classified as a breaking change for a crate, not a minor or patch-level change.
Tag: fact
Claims: b-bk03-f000267-c14

## Question `wit-dependency-keyword-design`

### wit-dependency-keyword-design--p1
Summary: What if just the word "dependency" were used, and "locked" vs. "unlocked"/"range" were inferred from the syntax after the `@` — the word "dependency" is already used by package managers and their build-config files (npm/package.json, cargo/Cargo.toml) to exclusively refer to implementations, so this keeps vocabulary aligned and regular.
Tag: taste
Claims: b-sR05-f001983-c1

## Question `wit-export-direct-vs-interface`

### wit-export-direct-vs-interface--p1
Summary: A world can export a bare function directly, but that isn't the recommended approach — the recommended best practice is to wrap related functions inside an interface, which the world then exports, since it's more modular, extensible, and matches how WIT is used in real multi-function components.
Tag: taste
Claims: a-sR08-f003033-c1

## Question `work-stealing-vs-thread-per-core`

### work-stealing-vs-thread-per-core--p1
Summary: Across 360 benchmarked configurations spanning balanced/unbalanced and low-to-high-scale, CPU- through IO-heavy HTTP/2 workloads, io_uring (Glommio) didn't strictly outperform epoll-based runtimes even under a "noisy neighbor" scenario designed to favor work-stealing, and tokio's work-stealing configuration showed unexplained throughput anomalies at 8/12 threads. The choice between executor-per-thread and work-stealing isn't a simple matter of "which is faster" but which architecture best aligns with the application's own logic.
Tag: fact
Claims: a-sa18-f009026-c1

## Question `wrap-third-party-types-in-public-api`

### wrap-third-party-types-in-public-api--p1
Summary: Because Rust has no standard u256 type, one of several third-party crate implementations gets picked, but it's never exposed directly — it's wrapped behind a local `ExpandedDifficulty` type, so the underlying crate choice stays swappable.
Tag: tradeoff
Claims: b-bk03-f000267-c17

## Question `xcframework-tooling-vs-hand-built`

### xcframework-tooling-vs-hand-built--p1
Summary: XCFramework's on-disk structure is simple enough that some teams build it by hand, but sticking to Apple's official `xcodebuild -create-xcframework` tooling to combine the per-target static libraries, headers and module map is preferred over replicating that structure manually.
Tag: taste
Claims: a-sa27-f012237-c2
