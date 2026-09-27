For each source: what must a Rust practitioner decide, and where do the sources conflict on it?

## f004423 — iroh 0.97.0 - Custom Transports & noq (2026-03-16, English)

### Questions
- Q: Given Rust has no stable async Drop, should a type's cleanup rely on Drop's best-effort behavior, or require an explicit async close call?
  concepts: async runtimes, Drop, resource lifecycle; domains_live: decentralized-iroh, distributed, core; positions_seen: explicit-close-required
- Q: When part of a library's API isn't ready for stabilization, should it ship gated behind an explicit "unstable" feature flag alongside the stable release, or should the release wait until everything is ready?
  concepts: feature flags, API stability, semver; domains_live: decentralized-iroh, distributed, core; positions_seen: ship-gated-unstable

### Claims
- voice: dignifiedquire (iroh/n0 computer) | position: explicit-close-required | date: 2026-03-16 | locator: section "2. Changes to Endpoint closing" / "Endpoint Lifecycle Improvements" | paraphrase: Endpoint no longer attempts best-effort graceful close on drop; callers must await endpoint.close() explicitly, or resources close ungracefully and an error is logged | quote: "Starting with this release, the Endpoint no longer attempts to close connections gracefully when dropped. To gracefully close the endpoint, always await endpoint.close() before dropping the last instance of an endpoint or terminating your application." | practiced_evidence: https://github.com/n0-computer/iroh (PR #3879)
- voice: dignifiedquire (iroh/n0 computer) | position: ship-gated-unstable | date: 2026-03-16 | locator: section "Custom Transports" / "Current status" | paraphrase: the custom-transport API ships now but stays behind an unstable feature flag and is declared unstable even past the 1.0 stabilization line | quote: "As the name suggests, the custom transport API is unstable and will remain so for some time even after iroh 1.0 is released." | practiced_evidence: https://github.com/n0-computer/iroh (PR #3845, feature flag unstable-custom-transports)

### Nothing new

## f004573 — Add native det (determinant) tensor operation (2026-04-15 to 2026-04-22, English)

### Questions
- Q: Should a numeric operation panic on invalid/unsupported input (e.g. a quantized dtype), and if so, must the panic condition be spelled out in the function's own documentation?
  concepts: panics, error handling, docs-as-contract; domains_live: ml, core; positions_seen: panic-is-fine-if-documented, prevent-via-explicit-check
- Q: When a generic numeric algorithm needs a per-dtype constant (e.g. a singularity epsilon), should the value be hardcoded via an exhaustive match on the dtype, or derived generically from the type's own metadata (a trait method)?
  concepts: generics, traits, exhaustive match, floating-point; domains_live: ml, core; positions_seen: derive-from-metadata-generally-better, reject-metadata-for-this-specific-use

### Claims
- voice: antimora (Tracel AI / burn maintainer) | position: panic-is-fine-if-documented | date: 2026-04-21 | locator: PR review comment, 2026-04-21T14:39:58Z | paraphrase: the QFloat panic path is acceptable but must be listed in the function's `# Panics` docs so a user isn't surprised by it | quote: "The `# Panics` list should include the QFloat case (added in the new `TensorCheck::det` at check.rs:1403-1409). Right now a user hitting it gets a panic with no heads-up from the docs." | practiced_evidence: none
- voice: softmaximalist (PR author, burn contributor) | position: prevent-via-explicit-check | date: 2026-04-19 | locator: PR review comment, 2026-04-19T18:47:03Z | paraphrase: rather than let a quantized input fail deep inside LU decomposition, add an explicit TensorCheck that rejects it up front with a clear message | quote: "Hence, I have added a tensor check to reject a quantized input tensor." | practiced_evidence: https://github.com/tracel-ai/burn/pull/4813 (test_det_quantized_tensor)
- voice: antimora (Tracel AI / burn maintainer) | position: derive-from-metadata-generally-better | date: 2026-04-21 | locator: PR review comment, 2026-04-21T14:45:21Z | paraphrase: hardcoded per-dtype epsilon constants should be replaced by a generic accessor on the dtype's own precision metadata, since it is self-documenting and handles all float dtypes including Flex32 uniformly | quote: "`burn_std::FloatDType::finfo()` would be a strict improvement over the hardcoded constants here... self-documenting, dtype-correct, and Flex32 falls out for free." | practiced_evidence: none
- voice: antimora (Tracel AI / burn maintainer) | position: reject-metadata-for-this-specific-use | date: 2026-04-21 | locator: PR review comment, 2026-04-21T14:45:23Z | paraphrase: for this particular pivot-replacement site, machine epsilon is the wrong semantic quantity regardless of dtype, so the exact-zero check should stay rather than switch to finfo | quote: "On whether to use `finfo` here instead: I'd say no... the pivot-replacement here is better off staying exact-zero." | practiced_evidence: none

### Nothing new

## f004581 — Agents Week: network performance update (2026-04-17, English)

### Nothing new
`nothing new` — the post is a company-wide network-performance recap (RUM methodology, trimean of connection times, new PoPs); it names no Rust-specific design decision or Voice position, only aggregate metrics.

## f004688 — When "idle" isn't idle: how a Linux kernel optimization became a QUIC bug (2026-05-12, English)

### Nothing new
`nothing new` — the disagreement traced (Jana Iyengar vs. Neal Cardwell vs. Eric Dumazet on epoch-shift semantics) is a Linux TCP/kernel congestion-control dispute later ported into quiche's Rust code; no Voice states a position on a Rust-practitioner decision (the fix itself, `cmp::max` over two `Option<Instant>` fields, is not argued for against any alternative).

## f004706 — Further extend the axum API to support embedded files through RustEmbed (2026-05-19 to 2026-09-26, English)

### Questions
- Q: When an expected embedded resource (e.g. a static asset) is missing, should the framework fail the build, or degrade silently at runtime (e.g. serve a 404)?
  concepts: build-time vs runtime failure, error handling; domains_live: web, frontend, core; positions_seen: fail-the-build

### Claims
- voice: gbj (Greg Johnston, Leptos creator) | position: fail-the-build | date: 2026-09-18 | locator: PR review comment, 2026-09-18T18:13:56Z | paraphrase: an `allow_missing = true` option that lets the build succeed and then 404 at request time is a bad default, because it converts a build-time problem into a silent runtime one | quote: "`allow_missing = true` seems bad because it allows for a successful build → 404 rather than a build failure." | practiced_evidence: none

### Nothing new

## f004741 — iroh 1.0.0-rc.1 - The last one (2026-05-27, English)

### Questions
- Q: Given Rust has no stable async Drop, should a type's cleanup rely on Drop's best-effort behavior, or require an explicit async close call?
  concepts: async runtimes, Drop, resource lifecycle; domains_live: decentralized-iroh, distributed, core; positions_seen: explicit-close-required (continued practice)
- Q: When part of a library's API isn't ready for stabilization, should it ship gated behind an explicit "unstable" feature flag alongside the stable release, or should the release wait until everything is ready?
  concepts: feature flags, API stability, semver; domains_live: decentralized-iroh, distributed, core; positions_seen: ship-gated-unstable
- Q: Should an extensible policy/configuration surface (e.g. connection access control) be expressed as a closed enum, or as an open trait?
  concepts: traits, enums, extensibility, API design; domains_live: decentralized-iroh, distributed, core; positions_seen: trait-over-enum

### Claims
- voice: Friedel Ziegelmayer & Rüdiger Klaehn (iroh/n0 computer) | position: explicit-close-required | date: 2026-05-27 | locator: section "⚡ Faster Endpoint::close" | paraphrase: explicit endpoint.close() is now cheaper too — shutdown skips the draining period when possible, reinforcing close as the primary, first-class shutdown path rather than relying on drop | quote: "Shutdown now skips the draining period when it can. Closing is near-instant when the peer already closed remotely, and roughly one RTT otherwise if there is no packet loss." | practiced_evidence: https://github.com/n0-computer/iroh (PR #4270, fixes #4201)
- voice: Friedel Ziegelmayer & Rüdiger Klaehn (iroh/n0 computer) | position: ship-gated-unstable | date: 2026-05-27 | locator: section "🛣️ Configurable path selection" | paraphrase: the new PathSelector trait and its types ship now but stay behind the unstable-custom-transports flag and are explicitly excluded from the 1.0 stability guarantee | quote: "The trait and the new types are gated behind the unstable-custom-transports feature. Keep in mind that this means they are not covered by the 1.0 stability guarantees and may break in future releases." | practiced_evidence: https://github.com/n0-computer/iroh (#4232)
- voice: Friedel Ziegelmayer & Rüdiger Klaehn (iroh/n0 computer) | position: trait-over-enum | date: 2026-05-27 | locator: section "🔐 Pluggable relay access control" | paraphrase: the closed `AccessConfig` enum was replaced by an open `AccessControl` trait with `on_connect`/`on_disconnect` hooks, so embedders can implement arbitrary policy rather than choosing among enum variants | quote: "The relay's access control has been redesigned. The AccessConfig enum is gone, replaced by an AccessControl trait with on_connect and on_disconnect hooks." | practiced_evidence: https://github.com/n0-computer/iroh (#4276)

### Nothing new

## f004804 — Create and use a new cacheline-aligned reference type (2026-06-15 to 2026-06-17, English)

### Questions
- Q: When a type wraps an unsafe operation and is labeled "safe," must that safety guarantee hold under every generic instantiation/composition, or is a narrower guarantee acceptable if the common case is sound?
  concepts: unsafe, soundness, generics, type-level safety guarantees; domains_live: embedded, core; positions_seen: overpromising-is-unsound, pragmatic-judgment-call-acceptable
- Q: Should a macro hide an API's less-friendly construction requirements from the user, or should the API stay explicit even if less ergonomic?
  concepts: macros, ergonomics vs. transparency; domains_live: embedded, core; positions_seen: macros-may-hide-complexity

### Claims
- voice: Dominaezzz (esp-hal reviewer) | position: overpromising-is-unsound | date: 2026-06-15 | locator: PR review comment, 2026-06-15T21:09:39Z | paraphrase: calling the new reference type "safely useable" overpromises, since a composition such as boxing it with external-memory backing is not actually safe to use | quote: "\"safely useable\" is too vague and I feel it over promises a bit... Example of over promising, `Box<InternalMemory<[DmaDescriptor; 10]>, ExternalMemory>` is not safe to use." | practiced_evidence: none
- voice: bugadani (esp-hal maintainer, PR author) | position: pragmatic-judgment-call-acceptable | date: 2026-06-17 | locator: PR review comment, 2026-06-17T07:36:32Z | paraphrase: without a full proof, a cache writeback is judged safe enough in practice for this type's current alignment guarantees, given invalidate isn't called on these paths | quote: "Wishy-washy, but a cache writeback is generally a safe operation as far as I can tell, and we don't call invalidate on these I think. So I think we're fine with the DmaDescriptor alignment in this type, at this time." | practiced_evidence: none
- voice: bugadani (esp-hal maintainer, PR author) | position: macros-may-hide-complexity | date: 2026-06-15 | locator: PR description, 2026-06-15T17:07:50Z | paraphrase: the new reference type makes constructing DMA buffers less friendly directly, but that friction is absorbed by the existing macros so end users don't see it | quote: "It makes constructing buffers a bit less friendly, but that's hidden from us by the macros currently." | practiced_evidence: https://github.com/esp-rs/esp-hal (PR #5744)

### Nothing new

## f004809 — Announcing Spin v4.0 (2026-06-15, English)

### Questions
- Q: Should a framework's host/runtime interfaces be async by default, or should async stay an opt-in path alongside a synchronous default?
  concepts: async runtimes, concurrency model; domains_live: wasm, cloud-workers, web; positions_seen: async-by-default
- Q: Under a concurrent-instance execution model, should shared state use global statics/OnceCell, or be scoped per-request with explicit synchronization?
  concepts: shared state, concurrency, statics; domains_live: wasm, cloud-workers; positions_seen: prefer-per-request-scoped-state

### Claims
- voice: The Spin Project (Fermyon / CNCF Spin, institution) | position: async-by-default | date: 2026-06-15 | locator: sections "WASI Preview 3: stabilized and supported long-term" / "Async everywhere: Spin's host interfaces are now async" | paraphrase: WASIp3's async model, previously experimental and opt-in, is now the default for new applications, and Spin's own host interfaces (KV, SQLite, Postgres, Redis, outbound HTTP) were rewritten to be async so handlers get real concurrency instead of blocking | quote: "WASIp3 is now the default platform for new applications... we've asyncified Spin's host interfaces so I/O-heavy handlers actually get concurrency instead of blocking the instance." | practiced_evidence: https://github.com/spinframework/spin (spin-sdk = "6.0")
- voice: The Spin Project (Fermyon / CNCF Spin, institution) | position: prefer-per-request-scoped-state | date: 2026-06-15 | locator: section "Heads up on global state" | paraphrase: since one instance can now serve concurrent in-flight requests, code that used static/module-level/OnceCell "global" state must be audited and moved to per-request state or explicit synchronization | quote: "Audit any static, module-level, or OnceCell state and reach for per-request state or explicit synchronization where needed." | practiced_evidence: none

### Nothing new
