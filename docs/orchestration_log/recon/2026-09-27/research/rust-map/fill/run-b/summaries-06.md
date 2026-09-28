# Blind fill summaries, batch 1, file 06 (run b)

## grouped-vs-field-optionality--p1: Grouped optionality
tag: taste
Advocates hold that when several query parameters only make sense together, semantically you want to know whether all of them were specified as a group, not check a mess of several individual `Option` values.
Claims: b-sb08-f002538-c1

## grouped-vs-field-optionality--p2: Field level optionality
tag: taste
Advocates hold each query field should be wrapped in `Option` individually, arguing this best reflects the reality of how query parameters actually work, and that they have never seen a real case where a set of parameters is optional as a whole group rather than individually.
Claims: b-sb08-f002538-c2, b-sb08-f002538-c3

## gui-accessibility-first-class--p1: First class requirement
tag: taste
Advocates hold that Windows support, screen-reader accessibility and IME input are core seriousness criteria for evaluating a Rust GUI framework, not afterthoughts — if these rank below chasing trends, "you are not serious."
Claims: b-sb21-f008390-c4

## gui-custom-renderer-vs-native--p1: Build a custom modular GPU-based renderer rather than reuse an existing engine
tag: taste
Advocates hold their renderer is distinguished from "existing solutions" by being free, open-source and extremely modular, built around a custom GPU-based drawing layer.
Claims: a-sa26-f011305-c6

## hal-driver-typestate--encode-in-types: Encode it in types
tag: tradeoff
Advocates hold a driver's mode should be a typestate generic parameter (e.g. `Uart<T, M>` with `M` = `Blocking`/`Async`), determined by how the driver is constructed rather than by a cargo feature flag.
Claims: b-sb03-f000715-c1

## hal-driver-typestate--runtime-or-raw: A simpler runtime mechanism or raw form
tag: tradeoff
Advocates hold the same runtime-binding problem (moving interrupt handling off link-time binding) can be solved without introducing typestate at all.
Claims: b-sb03-f000715-c2

## hal-driver-typestate--typestate-costly: Typestate is possible but costly
tag: tradeoff
Advocates hold that typestate could resolve a design ambiguity, but adopting it "gets annoying later," naming it as a real but ongoing complexity cost.
Claims: b-sb05-f001512-c2

## hal-expose-private-facilities--p1: HAL should expose a public version of the private cache-flush function
tag: taste
Advocates hold that when they had to copy a private cache-flush function definition to get needed behavior, a public version of it is "required" and worth the HAL maintainers adding.
Claims: b-sT05-f002499-c8

## handle-identity-traits-vs-store-methods--p1: Store scoped explicit methods
tag: fact
Advocates hold that identity/equality on a handle type is surprising and unsound as a bare trait impl because it doesn't hold across import/export boundaries for the same underlying resource; correct identity comparison needs a store borrow, so it should live in separate methods (`is_same(&store, ...)`, `identity_key(&store)`) rather than `PartialEq`/`Eq`/`Hash`.
Claims: b-sb16-f005000-c8, b-sb16-f005000-c7

## handle-identity-traits-vs-store-methods--p2: Exclude lazily populated field from identity key
tag: fact
Advocates hold that a field which starts unset and gets filled in later cannot safely be used alone as part of a hash/identity key, because it would collide distinct values before being filled and change a single value's own key mid-lifetime, breaking `HashMap` use; the actual identity key needs other, stable fields instead.
Claims: b-sb16-f005000-c9

## hard-dependency-vs-pluggable-interface--pluggable-interface: Keep a pluggable interface
tag: tradeoff
Advocates hold a crate should avoid hard-pinning one implementation: a hard dependency forces a release every time the pinned crate releases, and breaks on platforms or org policies (e.g. FIPS mandates) the pinned implementation can't satisfy, so the interface should be made swappable via feature flags instead.
Claims: a-sR06-f001989-c1, a-sR13-f004586-c1

## hard-dependency-vs-pluggable-interface--hard-dependency-behind-feature: A hard dependency behind a feature flag is fine
tag: tradeoff
Advocates hold a hard dependency is fine as long as it sits behind a feature flag, rather than requiring a fully pluggable interface.
Claims: a-sR06-f001989-c2

## hardware-interrupt-scheduling--p1: Hardware-interrupt-driven (SRP-based) scheduling preferred over software-kernel scheduling
tag: fact
Advocates hold the Cortex-M hardware interrupt/priority model maps directly onto Stack Resource Policy scheduling, giving zero-cost, compile-time-computed ceilings that a thread-based RTOS's software kernel cannot achieve.
Claims: a-sB01-f000227-c2

## hook-api-pointer-vs-address--p1: Keep the raw pointer type in the hook API rather than reducing to an address
tag: taste
Advocates hold the pointer should be passed as-is to hooks to avoid loss of information, trusting the caller not to alter it.
Claims: a-sa11-f004512-c2

## hook-api-pointer-vs-address--p2: An address is sufficient information for the hook
tag: taste
Advocates hold they aren't sure what information a hook would need beyond the pointer's address, so reducing to `usize` is sufficient.
Claims: a-sa11-f004512-c3

## host-and-embedded-cargo-layout--p1: Separate projects
tag: tradeoff
Advocates hold that host and embedded (cross-compiled) code should live in fully separate, non-workspace Cargo projects when the toolchains differ and a patched dependency is needed for only one side.
Claims: a-sR14-f004865-c1

## hot-patching-for-iteration--hot-patch: Hot-patch for iteration speed
tag: tradeoff
Advocates hold that hot-patching a running binary (Subsecond: recompiling only changed crates and linking them to hardcoded addresses at runtime, skipping the normal link step) is the way to get near-instant iteration, accepting "a huge number of quirks, edge cases, incomprehensible behavior" to make it work, and treat remaining rustc-level costs (like incremental-artifact disk copying) as further ground to close toward "blink and miss it" hotpatch speed.
Claims: a-sa26-f011305-c5, b-sb09-f002719-c3, b-sb09-f002719-c1

## hot-patching-for-iteration--faster-codegen-backend: Faster full rebuilds via an alternate codegen backend
tag: tradeoff
Advocates hold that swapping in the cranelift codegen backend as an optional flag for hot-reload builds meaningfully speeds full rebuilds, reporting roughly halved build times on their machine.
Claims: b-sb09-f002719-c2

## http-body-unknown-size--p1: Distinguish unknown from zero
tag: taste
Advocates hold that special-casing a response as `content-length: 0` when its true length couldn't be cheaply computed is conceptually wrong, and that the default should switch to an explicit "unknown size" body instead.
Claims: a-sa12-f004637-c1

## http-body-unknown-size--p2: Cautious narrow fix
tag: taste
Advocates hold that changing the default to "unknown size" is too broad a change, risking silent behavior changes for unrelated responses that don't care about HEAD requests; the fix should work without requiring unfamiliar users to opt in explicitly.
Claims: a-sa12-f004637-c2

## http-error-status-in-result--unified-response-type: Errors are ordinary responses (`Ok(response)`, one enum)
tag: taste
Advocates hold that HTTP responses, success and error alike, should be one enum value the handler returns, or wrapped as `Ok(response)`: a pre-baked design that "just works" the moment it's dropped in, and — critically for platforms like API Gateway/Lambda — keeps an intentional 401/403/429/500 from being mistaken for an invocation failure and turned into a generic 502.
Claims: a-saL1-f005454-c1, b-sb22-f008906-c4, b-sb22-f008906-c3

## http-error-status-in-result--errors-in-err-channel: Split success and error types so `?` works
tag: taste
Advocates hold that splitting response variants into a success side and an error side (e.g. 2xx/3xx vs 4xx/5xx) restores normal `?`-operator ergonomics, granting this is more convenient for users at the cost of extra library-side complexity (needing parallel success/error status-code types).
Claims: a-saL1-f005454-c3, a-saL1-f005454-c2

## human-written-code-standard--human-written-for-critical-code: Hold critical work to human-written-only
tag: taste
Advocates hold, as a personal standard rather than an argued position, that core project code (and its accompanying writing) should be entirely human-written, after an earlier LLM-assisted attempt proved controversial.
Claims: a-sa15-f005821-c2

## human-written-code-standard--light-review-for-peripheral-code: A brief check is enough for peripheral code
tag: taste
Advocates hold it's acceptable to let an LLM write a whole peripheral component in a language/domain you lack expertise in, and ship it after only a brief check rather than deep review.
Claims: a-sR14-f004865-c2

## immediate-vs-retained-gui--message-passing-for-realtime: Elm-style message passing fits real-time, stateful apps
tag: tradeoff
Advocates hold that a real-time, stateful app needs a genuinely event-based library that can synchronize external state changes (e.g. audio playback ticks) with UI redraws while supporting custom canvas drawing, choosing a message-passing framework specifically for that reason.
Claims: a-sa15-f005857-c1

## immediate-vs-retained-gui--doesnt-matter-at-small-scale: The choice does not matter for small-to-medium UIs
tag: fact
Advocates hold that while immediate mode avoids widget-lifetime bookkeeping and integrates more easily into a game engine's GPU loop, and retained mode can perform better by not rebuilding the whole UI every frame, at the scale of a small UI the difference is untestable in practice.
Claims: b-sb21-f008390-c3

## impl-trait-syntax-reuse--p1: Apit syntax reuse was a mistake
tag: taste
Advocates hold, as a personal view, that argument-position impl Trait sharing the same `impl Trait` syntax as return-position impl Trait was a design mistake.
Claims: a-sa30-f013276-c2

## in-app-vs-infrastructure-concern--delegate-tls-to-proxy: Terminate TLS in a reverse proxy
tag: tradeoff
Advocates hold that even though the app framework supports TLS natively, the recommended setup terminates TLS in a reverse proxy instead.
Claims: b-sT09-f005312-c1

## in-app-vs-infrastructure-concern--rate-limit-in-app: Build rate limiting in the app; gateway usage plans fall short
tag: tradeoff
Advocates hold that platform-level rate limiting (API Gateway usage plans) falls short in practice — invisible to clients, no rate-limit headers, pre-provisioned API keys capped at 10,000 per account/region, and only day/week/month windows rather than the short window actually needed — so rate limiting needs to be built into the app.
Claims: b-sb22-f008906-c6

## in-app-vs-infrastructure-concern--p1: A self-written in-process server removes nginx's role rather than replacing it
tag: fact
Advocates hold that nginx's real value in front of a service is decoupled operational concerns — flood protection, bandwidth throttling, load balancing, TLS termination — for performance and separation-of-concerns reasons, and that an in-process Rust server which doesn't reproduce those concerns is removing nginx's role, not replacing it.
Claims: a-sa14-f005360-c7

## incremental-invalidation-redesign--p1: Redesign around atomic levels and data dependencies
tag: tradeoff
Advocates hold that incremental invalidation should represent what compilation stage a change actually needs (AST/HIR/MIR/codegen) as an explicit "atomic level," with fine-grained data dependencies (like LTO flags) tracked separately, plus a two-stage fingerprint that only rebuilds to name-resolution to check whether a dependent actually used a changed definition — so `cargo check`/clippy/build stop redoing each other's work and needless dependent rebuilds shrink.
Claims: a-sa18-f008694-c1

## incremental-port-vs-rewrite-to-rust--p1: Incremental port only hot paths
tag: tradeoff
Advocates hold existing JS code bases don't need to be thrown away: port the most performance-sensitive functions to Rust for immediate benefit, and you can stop there.
Claims: a-sB02-f000256-c1

## infrastructure-from-code-vs-iac--p1: Provision infrastructure from code annotations over Docker or Terraform
tag: tradeoff
Advocates hold that an in-code annotation provisioning a database is "pretty simple" next to running Docker locally and managing Postgres by hand or with an IaC tool like Terraform in production.
Claims: b-sT09-f011688-c2

## instant-min-max--p1: Oppose instant extrema fraught
tag: fact
Advocates hold Instant's API contract doesn't guarantee a fixed reference time — a conforming implementation could start/stop its reference timer dynamically — so a MIN value wouldn't reliably denote a stable point in time, and separately that Instant values aren't portable or stable across reboots, making exposing its extrema more hazardous than SystemTime's case.
Claims: a-sa19-f009196-c2, a-sa19-f009196-c1

## instant-min-max--p2: Instant extrema fraught, prefer saturating ops
tag: tradeoff
Advocates hold SystemTime::MIN/MAX seem reasonable but Instant::MIN/MAX seem fraught for the reasons already raised, proposing saturating arithmetic methods directly on Instant instead of exposing its extrema.
Claims: a-sa19-f009196-c3

## instant-min-max--p3: Support instant bound for saturating arithmetic
tag: tradeoff
Advocates hold they want an Instant minimum/maximum (or equivalent) specifically to support saturating arithmetic in use cases like a token-bucket rate limiter, where moving a timestamp below the representable minimum should saturate rather than panic.
Claims: a-sa19-f009196-c4

## internal-hazmat-api-for-performance--p1: It is worth bypassing BLAKE3's public API for the internal SIMD entry point
tag: tradeoff
Advocates hold that after finding no public support for batch-hashing multiple blobs, repurposing the internal `hash_many` SIMD entry point is worth a 17x combined SIMD+rayon speedup, even though it silently produces wrong results (rather than panicking) if its unchecked preconditions are violated on a real SIMD platform.
Claims: a-sR09-f003702-c1

## internal-service-abstraction-trait--p1: Service abstraction internally
tag: tradeoff
Advocates hold that communication between an app's internal stateful components should go through an internal asynchronous request/response abstraction built on a Buffered `tower::Service` — "microservices in one process" — rather than direct calls or shared state, so internal storage-layer behaviors never leak into the external API and the backing store stays replaceable.
Claims: b-bk03-f000267-c4

## intra-doc-links--p1: Use rustdoc intra doc links
tag: fact
Advocates hold doc comments should reference types and functions via rustdoc intra-doc links rather than plain text, both for navigability and because the rustdoc lint then catches a typo'd or renamed reference that plain text would silently leave stale.
Claims: b-bk03-f000267-c16

## io-safety-op-placement-in-main--p1: An I/O-safety-critical operation must run at the very start of `main`
tag: fact
Advocates hold that an fd-inheritance setup operation must be called at the very start of `main` to ensure no other file descriptor takes the place of a missing one, framing anything less as an I/O-safety violation.
Claims: a-sa14-f005079-c1

## io-safety-op-placement-in-main--p2: Exact placement doesn't need to be enforced as long as nothing intervenes
tag: tradeoff
Advocates hold it isn't worth contorting a CLI's structure to guarantee the operation happens literally at the start of `fn main`, since controlling all entrypoints and the current placement during startup/CLI processing is already fine.
Claims: a-sa14-f005079-c2

## jit-code-alignment--p1: 32 byte default reasonable
tag: fact
Advocates hold that since the CPU frontend fetches aligned 32B/64B chunks, a function starting mid-chunk wastes instruction-fetch bandwidth, so 32-byte function alignment would be a more reasonable default than the current 16-byte one.
Claims: b-sR04-f001401-c1

## js-tooling-in-rust--p1: Rust is the standout choice specifically for building JavaScript/TypeScript tooling and infrastructure
tag: taste
Advocates hold Rust is "undoubtedly the big star" in JS/TS tooling and infrastructure because it addresses the ecosystem's most significant unsolved issue, performance, while its language- and compiler-level safeguards also make it easier to build successful tools in the first place.
Claims: b-sb26-f012866-c1

## js-tooling-in-rust--p2: Replace established JavaScript-based tooling with a Rust-implemented toolchain
tag: taste
Advocates hold a Rust-implemented toolchain should explicitly aim to replace established JS tools like Prettier and ESLint, framing the payoff as both raw performance and a more consistent developer experience than the tools it replaces.
Claims: b-sb26-f012866-c2

## kernel-constants-hardcode-vs-comptime--parameterize-constants: Pass through a comptime struct or derive from metadata
tag: tradeoff
Advocates hold backend- or dtype-specific kernel constants should be passed through a comptime struct or derived from a generic accessor on the dtype's own precision metadata, so a future backend-specific value change or a new float dtype doesn't require touching the kernel body.
Claims: b-sR05-f002048-c2, b-sR10-f004573-c3

## kernel-constants-hardcode-vs-comptime--hardcode-for-this-use: Hardcode for this specific use
tag: fact
Advocates hold that for a specific site (a pivot-replacement check), a dtype-derived epsilon-style quantity is semantically the wrong tool regardless of dtype, and the value should stay an exact-zero constant rather than switch to a metadata-derived one.
Claims: b-sR10-f004573-c4

## keyed-access-copy-vs-clone-keys--p1: Copy only keys
tag: taste
Advocates hold key types should be deliberately constrained to `Copy`, to stop users reaching for costlier `Clone` keys when a cheaper option exists.
Claims: b-sb13-f003963-c3

## keyed-access-copy-vs-clone-keys--p2: Allow clone keys
tag: taste
Advocates hold the trait should also accept `Clone` key types, since cheaply-clonable types like `Arc<str>` are reasonable keys even though cloning large objects is not.
Claims: b-sb13-f003963-c4

## lambda-build-tooling--cargo-lambda-by-default: Cargo Lambda by default; Docker only when needed
tag: tradeoff
Advocates hold Cargo Lambda is the best way to interact with the Rust Lambda runtime for local runs, hot reload and arm64 zip builds, reaching for a container image only "if, for some reason" it's required.
Claims: a-sT11-f007659-c2

## lambda-release-profile-size--p1: Size-optimized release profile
tag: fact
Advocates hold a size-optimized release profile (opt-level "z", lto, codegen-units 1, panic abort, strip) is worth the longer compiles and lost unwinding, measuring a binary shrink from 3.6MB to 1.8MB and a cold start improvement from 20ms to 17ms, with larger gains expected on bigger programs.
Claims: a-sT11-f007659-c1
