# Fill A — position summaries, file 06

## grouped-vs-field-optionality

### grouped-vs-field-optionality--p1 (Grouped optionality)
Advocates say when several query parameters only make sense together, what matters 99% of the time is knowing whether all of them were specified as one unit, not sorting through a mess of several independent `Option` values.
Tag: tradeoff.
Claims: b-sb08-f002538-c1.

### grouped-vs-field-optionality--p2 (Field-level optionality)
Advocates recommend wrapping every query field in `Option` individually, arguing this best reflects the reality of how query parameters actually arrive, and report never having seen a real case where a set of parameters is optional as a whole group rather than one by one.
Tag: tradeoff.
Claims: b-sb08-f002538-c2, b-sb08-f002538-c3.

## gui-accessibility-first-class

### gui-accessibility-first-class--p1 (First-class requirement)
Advocates treat Windows support, screen-reader accessibility, and IME input as core seriousness criteria for any Rust GUI framework, not nice-to-haves — pointedly against roadmaps that rank "trend chasing AI" above them, after a survey found most libraries fail at least one of the three.
Tag: tradeoff.
Claims: b-sb21-f008390-c4.

## gui-custom-renderer-vs-native

### gui-custom-renderer-vs-native--p1 (Build a custom modular GPU-based renderer)
Advocates position their renderer (Blitz) against unnamed "existing solutions" as free, open-source, and extremely modular — a hybrid that alternates native system widgets with a custom GPU-based drawing layer rather than fully wrapping native widgets or an existing browser engine.
Tag: tradeoff.
Claims: a-sa26-f011305-c6.

## hal-driver-typestate

### hal-driver-typestate--encode-in-types (Encode it in types)
Advocates propose a typestate `Uart<T: Instance, M>` where `M` is `Blocking` or `Async`, with per-mode constructors, so a Cargo feature no longer determines whether a driver is async, moving interrupt handling from link-time binding to a runtime-installed array.
Tag: tradeoff.
Claims: b-sb03-f000715-c1.

### hal-driver-typestate--runtime-or-raw (A simpler runtime mechanism or raw form)
Advocates had a similar runtime-binding idea independently, arrived at without introducing a typestate at all.
Tag: tradeoff.
Claims: b-sb03-f000715-c2.

### hal-driver-typestate--typestate-costly (Typestate is possible but costly)
Advocates concede type-state could resolve an ambiguity (default TX/RX pins) but flag that it adds ongoing complexity that becomes annoying later.
Tag: tradeoff.
Claims: b-sb05-f001512-c2.

## hal-expose-private-facilities

### hal-expose-private-facilities--p1 (HAL should expose a public version)
Advocates, after having to copy out a private cache-flush function definition to get their code working, say it's worth making a public version of that facility available since it's required.
Tag: tradeoff.
Claims: b-sT05-f002499-c8.

## handle-identity-traits-vs-store-methods

### handle-identity-traits-vs-store-methods--p1 (Store-scoped explicit methods)
Advocates say pointer-identity equality on a bare handle is surprising because it doesn't hold across import/export boundaries even for the same underlying function, so correct identity needs a store borrow and must be separate methods (`is_same(&store, ...)`, `identity_key(&store)`) rather than literal `Eq`/`Hash` impls.
Tag: fact.
Claims: b-sb16-f005000-c8, b-sb16-f005000-c7.

### handle-identity-traits-vs-store-methods--p2 (Exclude lazily populated field from identity key)
Advocates report discovering a candidate identity-key field starts as `None` and gets filled in later, so using it alone as a hash/identity key would collide two never-imported functions and change a function's own key mid-lifetime, breaking `HashMap` use — so that field is excluded and `(vmctx, array_call)` plus `type_index` is used instead.
Tag: fact.
Claims: b-sb16-f005000-c9.

## hard-dependency-vs-pluggable-interface

### hard-dependency-vs-pluggable-interface--pluggable-interface (Keep a pluggable interface)
Advocates want to avoid a hard dependency that would force a new release whenever an unrelated crate releases, and make a swappable interface (e.g. TLS crypto provider via feature flags) so platforms where the default backend can't build, or orgs that mandate a different certified backend, aren't stuck.
Tag: tradeoff.
Claims: a-sR06-f001989-c1, a-sR13-f004586-c1.

### hard-dependency-vs-pluggable-interface--hard-dependency-behind-feature (A hard dependency behind a feature flag is fine)
Advocates push back that a hard dependency is acceptable as long as it sits behind a feature flag.
Tag: tradeoff.
Claims: a-sR06-f001989-c2.

## hardware-interrupt-scheduling

### hardware-interrupt-scheduling--p1 (Hardware-interrupt-driven, SRP-based scheduling)
Advocates argue the Cortex-M hardware interrupt/priority model maps directly onto Stack Resource Policy scheduling, giving zero-cost, compile-time-computed ceilings that a thread-based RTOS's software kernel can't reach.
Tag: tradeoff.
Claims: a-sB01-f000227-c2.

## hook-api-pointer-vs-address

### hook-api-pointer-vs-address--p1 (Keep the raw pointer type)
Advocates say the pointer should be passed as-is to the hook to avoid loss of information, with the caller trusted not to alter it.
Tag: tradeoff.
Claims: a-sa11-f004512-c2.

### hook-api-pointer-vs-address--p2 (An address is sufficient)
Advocates respond that they aren't sure what information a hook would need beyond the pointer's address.
Tag: tradeoff.
Claims: a-sa11-f004512-c3.

## host-and-embedded-cargo-layout

### host-and-embedded-cargo-layout--p1 (Separate projects)
Advocates keep host and embedded/cross-compiled code as fully separate, non-workspace Cargo projects when the toolchains differ and one side needs a patched dependency the other doesn't.
Tag: tradeoff.
Claims: a-sR14-f004865-c1.

## hot-patching-for-iteration

### hot-patching-for-iteration--hot-patch (Hot-patch for iteration speed)
Advocates describe "Subsecond," which hot-patches a running binary by recompiling only changed crates and linking them to hardcoded addresses at runtime, skipping the normal linking step entirely — despite, by their own account, a huge number of quirks and edge cases needed to make it work — paired with a "zerolink"/"thinlink" mechanism that automatically dynamically links workspace crates against a cached dependencies dylib.
Tag: tradeoff.
Claims: b-sb09-f002719-c1, a-sa26-f011305-c5.

### hot-patching-for-iteration--faster-codegen-backend (Faster full rebuilds via an alternate codegen backend)
Advocates propose adding the Cranelift codegen backend as an optional flag for hot-reload builds, reporting it roughly halved measured build times on their own machine.
Tag: tradeoff.
Claims: b-sb09-f002719-c2.

## http-body-unknown-size

### http-body-unknown-size--p1 (Distinguish unknown from zero)
Advocates want `impl IntoResponse for ()` to use an explicit "unknown size" body instead of an empty one, arguing that special-casing `content-length: 0` when the true size can't be cheaply known is conceptually wrong.
Tag: tradeoff.
Claims: a-sa12-f004637-c1.

### http-body-unknown-size--p2 (Cautious narrow fix)
Advocates resist making `()` default to unknown size across the board, worried it could silently change behavior for unrelated responses that don't care about HEAD requests, and want a fix that works without requiring unfamiliar users to opt in explicitly.
Tag: tradeoff.
Claims: a-sa12-f004637-c2.

## http-error-status-in-result

### http-error-status-in-result--unified-response-type (Errors are ordinary responses)
Advocates put every HTTP response — success and error alike — into one enum or return type returned directly by the handler, since there aren't really "successful" or "unsuccessful" responses, just responses; one advocate frames a drop-in `Ok(response)` middleware that "just works" the moment it's added, worth the cost of a baked-in response shape, as the reason an escaping `Err` gets mistranslated by upstream infrastructure (e.g. API Gateway) into a generic 502 instead of the deliberately designed 401/403/429/500.
Tag: tradeoff.
Claims: a-saL1-f005454-c1, b-sb22-f008906-c4, b-sb22-f008906-c3.

### http-error-status-in-result--errors-in-err-channel (Split success and error types so `?` works)
Advocates grant that splitting response variants into a Result-like type — 2xx/3xx on one side, 4xx/5xx on the other — would make the `?` operator usable again, at the cost of extra library-side complexity (e.g. a parallel `SuccessStatusCode` type).
Tag: tradeoff.
Claims: a-saL1-f005454-c3, a-saL1-f005454-c2.

## human-written-code-standard

### human-written-code-standard--human-written-for-critical-code (Hold critical work to human-written-only)
Advocates state, as a personal standard rather than an argued position, that all of a project's core code — and even the blog post describing it — is human-written, after an earlier LLM-assisted attempt "proved controversial."
Tag: taste.
Claims: a-sa15-f005821-c2.

### human-written-code-standard--light-review-for-peripheral-code (A brief check is enough for peripheral code)
Advocates find it acceptable to let an LLM write an entire peripheral component outside their own expertise (a JS/WASM GUI) and ship it after only a brief check rather than deep review.
Tag: taste.
Claims: a-sR14-f004865-c2.

## immediate-vs-retained-gui

### immediate-vs-retained-gui--doesnt-matter-at-small-scale (The choice does not matter at small scale)
Advocates note immediate mode avoids widget-lifetime bookkeeping and integrates easily into a game engine's GPU loop, while retained mode can perform better by not rebuilding the whole UI every frame — but at the scale of a small task the difference is untestable, so they aren't sure they love immediate mode "on principle" even though it doesn't matter here.
Tag: tradeoff.
Claims: b-sb21-f008390-c3.

### immediate-vs-retained-gui--message-passing-for-realtime (Elm-style message passing fits real-time, stateful apps)
Advocates chose a message-passing library (Iced) specifically because the app needed to synchronize audio-playback state with UI redraws while also drawing custom canvas content, piping a playback-tick channel into UI messages via its subscription mechanism, and report being satisfied enough not to have evaluated alternatives.
Tag: tradeoff.
Claims: a-sa15-f005857-c1.

## impl-trait-syntax-reuse

### impl-trait-syntax-reuse--p1 (APIT syntax reuse was a mistake)
Advocates state, as a personal view, that argument-position impl Trait sharing the exact same `impl Trait` syntax as return-position impl Trait was a design mistake, at minimum in terms of sharing the syntax.
Tag: taste.
Claims: a-sa30-f013276-c2.

## in-app-vs-infrastructure-concern

### in-app-vs-infrastructure-concern--p1 (A self-written in-process server removes nginx's role rather than replacing it)
Advocates argue that nginx's actual value in front of an HTTP service is providing decoupled operational concerns — flood protection, bandwidth throttling, load balancing, TLS termination — that a new in-process server doesn't reproduce, so dropping nginx removes that role rather than replacing it.
Tag: tradeoff.
Claims: a-sa14-f005360-c7.

### in-app-vs-infrastructure-concern--delegate-tls-to-proxy (Terminate TLS in a reverse proxy)
Advocates recommend setting up a reverse proxy for TLS even though their own web framework has built-in TLS support, and require HTTPS for a sensitive component (the web vault).
Tag: tradeoff.
Claims: b-sT09-f005312-c1.

### in-app-vs-infrastructure-concern--rate-limit-in-app (Build rate limiting in the app; gateway usage plans fall short)
Advocates detail why an API gateway's usage plans don't substitute for in-app rate limiting: on HTTP API v2 they don't exist at all, even on REST they're invisible to clients (no rate-limit headers, just a bare 429), require pre-provisioned API keys up to a hard per-account cap, and only offer day/week/month windows rather than the fine-grained window the use case needs.
Tag: tradeoff.
Claims: b-sb22-f008906-c6.

## incremental-invalidation-redesign

### incremental-invalidation-redesign--p1 (Redesign around atomic levels and data dependencies)
Advocates pitch representing what stage a compilation needs (AST/HIR/MIR/codegen) as an explicit "atomic level," plus tracking fine-grained data dependencies like LTO flags separately, so that `cargo check`, `clippy`, and `build` stop redoing each other's work and unrelated flag changes stop invalidating unrelated tools.
Tag: tradeoff.
Claims: a-sa18-f008694-c1.

## incremental-port-vs-rewrite-to-rust

### incremental-port-vs-rewrite-to-rust--p1 (Incremental port, only hot paths)
Advocates say existing JS code bases don't need to be thrown away: port the most performance-sensitive functions to Rust for immediate benefit, and stopping there is a legitimate option.
Tag: tradeoff.
Claims: a-sB02-f000256-c1.

## infrastructure-from-code-vs-iac

### infrastructure-from-code-vs-iac--p1 (Provision infrastructure from code annotations)
Advocates present an in-code annotation for provisioning a database as "pretty simple" next to running Docker locally or hand-managing Postgres with an IaC tool like Terraform in production.
Tag: tradeoff.
Claims: b-sT09-f011688-c2.

## instant-min-max

### instant-min-max--p1 (Oppose instant extrema, fraught)
Advocates say `Instant`'s API contract does not guarantee a fixed reference time — a conforming implementation could start or stop its reference timer dynamically — so a `MIN` value wouldn't reliably denote a stable point, and separately that `Instant` values aren't portable or stable across reboots, making its extrema more hazardous than `SystemTime`'s.
Tag: fact.
Claims: a-sa19-f009196-c2, a-sa19-f009196-c1.

### instant-min-max--p2 (Instant extrema fraught; prefer saturating ops)
Advocates agree `SystemTime::MIN`/`MAX` seem reasonable but `Instant::MIN`/`MAX` seem fraught for the reasons already raised, and propose adding saturating-arithmetic methods directly on `Instant` instead of exposing its extremal values.
Tag: tradeoff.
Claims: a-sa19-f009196-c3.

### instant-min-max--p3 (Support instant bound for saturating arithmetic)
Advocates want an `Instant` minimum or maximum specifically to support saturating arithmetic in a real use case (a token-bucket rate limiter), where moving a timestamp below the representable minimum should saturate rather than panic.
Tag: tradeoff.
Claims: a-sa19-f009196-c4.

## internal-hazmat-api-for-performance

### internal-hazmat-api-for-performance--p1 (Worth bypassing the public API)
Advocates, finding the public API has no support for hashing multiple independent blobs at once, repurpose an internal, precondition-checked-only-outside SIMD entry point to get a 17x combined speedup over sequential hashing, explicitly accepting that violating its unchecked preconditions on a real SIMD platform silently produces wrong results rather than panicking.
Tag: tradeoff.
Claims: a-sR09-f003702-c1.

## internal-service-abstraction-trait

### internal-service-abstraction-trait--p1 (Service abstraction internally)
Advocates route all communication between a project's stateful internal components through an internal asynchronous request/response abstraction built on a buffered service trait — described as "microservices in one process" — so that internal storage-engine behaviors stay from leaking into the external API and the backing store stays replaceable.
Tag: tradeoff.
Claims: b-bk03-f000267-c4.

## intra-doc-links

### intra-doc-links--p1 (Use rustdoc intra-doc links)
Advocates say doc comments should reference types and functions via rustdoc intra-doc links rather than plain text, both because it makes documentation easier to navigate and because the rustdoc lint will then catch a typo'd or renamed reference that plain text would silently leave stale.
Tag: tradeoff.
Claims: b-bk03-f000267-c16.

## io-safety-op-placement-in-main

### io-safety-op-placement-in-main--p1 (Must run at the very start of main)
Advocates argue an fd-inheritance setup should be called at the start of `main` specifically to ensure no other fd takes the place of a missing one, framing any later placement as an I/O-safety violation.
Tag: fact.
Claims: a-sa14-f005079-c1.

### io-safety-op-placement-in-main--p2 (Exact placement doesn't need enforcement)
Advocates push back that it isn't worth contorting a CLI's structure to guarantee an operation happens literally at the start of `fn main`, since the entrypoints are fully controlled and the current placement during startup is already fine.
Tag: tradeoff.
Claims: a-sa14-f005079-c2.

## jit-code-alignment

### jit-code-alignment--p1 (32-byte default reasonable)
Advocates note the CPU frontend fetches aligned 32B/64B chunks, so a function starting mid-chunk wastes fetch bandwidth, and suspect 32-byte function alignment would be a more reasonable default than the current 16-byte one.
Tag: fact.
Claims: b-sR04-f001401-c1.

## js-tooling-in-rust

### js-tooling-in-rust--p1 (Rust is the standout choice for JS/TS tooling)
Advocates call Rust "the big star" in JavaScript and TypeScript tooling and infrastructure, framing it as addressing the most significant unsolved issue in the current tooling ecosystem: performance.
Tag: taste.
Claims: b-sb26-f012866-c1.

### js-tooling-in-rust--p2 (Replace established JS tooling with a Rust toolchain)
Advocates state their project's explicit goal is replacing Prettier- and ESLint-style JavaScript tooling with a Rust-implemented toolchain, framing the payoff as both raw speed and a more consistent developer experience than the tools it replaces.
Tag: tradeoff.
Claims: b-sb26-f012866-c2.

## kernel-constants-hardcode-vs-comptime

### kernel-constants-hardcode-vs-comptime--hardcode-for-this-use (Hardcode for this specific use)
Advocates argue that for a particular pivot-replacement site, machine epsilon is the wrong semantic quantity regardless of dtype, so an exact-zero check should stay hardcoded rather than switch to a dtype-derived value.
Tag: tradeoff.
Claims: b-sR10-f004573-c4.

### kernel-constants-hardcode-vs-comptime--parameterize-constants (Pass through a comptime struct or derive from metadata)
Advocates say it's fine to hardcode values for now as long as they're passed to the kernel via a comptime struct, so a future backend-specific change doesn't require touching the kernel body; separately, a generic accessor on the dtype's own precision metadata is called a strict improvement over hardcoded per-dtype constants, self-documenting and handling all float dtypes uniformly.
Tag: tradeoff.
Claims: b-sR05-f002048-c2, b-sR10-f004573-c3.

## keyed-access-copy-vs-clone-keys

### keyed-access-copy-vs-clone-keys--p1 (Copy-only keys)
Advocates deliberately require `Copy` on keys for a keyed-access trait, specifically to stop users reaching for `Clone` keys when a cheaper option exists.
Tag: tradeoff.
Claims: b-sb13-f003963-c3.

### keyed-access-copy-vs-clone-keys--p2 (Allow Clone keys)
Advocates argue the trait should also accept `Clone` key types, since types like `Arc<str>` are cheap to clone and reasonable as keys even though cloning large objects generally is not.
Tag: tradeoff.
Claims: b-sb13-f003963-c4.

## lambda-build-tooling

### lambda-build-tooling--cargo-lambda-by-default (Cargo Lambda by default; Docker only when needed)
Advocates prefer Cargo Lambda for local runs, hot reload, and arm64 zip builds, reaching for a container image only if for some reason it's required, and report a multi-stage Docker build shrinking an image from 2.64 GB to 343 MB when they did need one.
Tag: tradeoff.
Claims: a-sT11-f007659-c2.

## lambda-release-profile-size

### lambda-release-profile-size--p1 (Size-optimized release profile)
Advocates adopted a size-optimized release profile on outside feedback, accepting longer compiles and no unwinding, and measured a binary shrinking from 3.6 MB to 1.8 MB with cold start improving from 20 ms to 17 ms, expecting larger gains on bigger programs.
Tag: tradeoff.
Claims: a-sT11-f007659-c1.
