## f002142 — `ComponentHook` based `Parent`/`Children` Management (2024-10-03, en)
### Questions
- Q: Should an ECS's relationship "edge" components be public types with the exclusivity (one-to-one, one-to-many, many-to-many, ...) encoded at the type level for compile-time correctness and ergonomics, or should the edge-storing components be private (mutable only via commands/hooks) with a single consistent query API regardless of exclusivity?
  concepts: ECS, relationships, type-level invariants, component visibility, query ergonomics; domains_live: other; positions_seen: type-level-exclusivity-public, private-edges-runtime-consistency
- Q: Should ECS relationships be stored as archetype-fragmenting edges (entities with different relationship targets end up in different archetypes, enabling wildcard/nested-join/traversal query operations), or as non-fragmenting components (all related entities can share the same archetype/table, favoring dense cache-friendly iteration for common hierarchical cases)?
  concepts: ECS, archetype fragmentation, query operations, cache-friendly iteration, hierarchy traversal; domains_live: other; positions_seen: fragmenting-enables-more-queries, non-fragmenting-preferred-for-hierarchies
### Claims
- voice: bushrat011899 | position: type-level-exclusivity-public | date: 2024-10-20 | locator: PR #15635, comment 2024-10-20T08:31:44Z | paraphrase: prefers public edge components whose type encodes the relationship's exclusivity (one-to-many derefs to `Entity`, many-to-one to `[Entity]`), because it makes incorrect usage fail to compile, improves error messages, and keeps the model close to what `Parent`/`Children` already are for users and for reflection/scene formats (BSN/`ron`) | quote: "I believe it is nicer that the type has a different interface based on the exclusivity - it makes the difference explicit in code, and incorrect usage not compile" | practiced_evidence: https://github.com/bevyengine/bevy/pull/15635
- voice: iiYese | position: private-edges-runtime-consistency | date: 2024-10-20 | locator: PR #15635, comment 2024-10-20T10:57:04Z | paraphrase: argues type-level exclusivity is not even correct (an entity can still hold both `OneToOne<R>` and `OneToMany<R>`) and forces every query site to know and restate the edge shape; consistency of one query API matters more than having the option | quote: "Consistency is more important here than options... Being at a type level is not a benefit it is the option." | practiced_evidence: https://github.com/iiYese/aery (author's own relations crate for Bevy)
- voice: iiYese | position: fragmenting-enables-more-queries | date: 2024-10-20 | locator: PR #15635, comment 2024-10-20T11:38:42Z | paraphrase: lists concrete query operations (wildcard queries, named wildcard queries, nested joins, efficient up-traversal, efficient sibling queries) that are only possible when relationship edges are exposed at the archetype level, which this PR's component-based (non-fragmenting) approach does not provide | quote: "You cannot do many query operations when edge information is not exposed at an archetype level." | practiced_evidence: https://github.com/iiYese/aery
- voice: nakedible | position: non-fragmenting-preferred-for-hierarchies | date: 2024-10-20 | locator: PR #15635, comment 2024-10-20T08:31:44Z | paraphrase: states that fragmenting relationships would be useless for their use case and would just produce one archetype per entity, whereas the non-fragmenting, relationship-type-keyed approach in this PR is what they actually need (and reports that a Bevy ECS SME independently suggested the same to them) | quote: "Fragmenting relationships are totally useless for my use cases, and will just lead to one archetype per entity." | practiced_evidence: none

## f002151 — Makes the `wasm32-wasip1/2` target a first-class citizen for Leptos's Server-Side (2024-10-05, en)
### Nothing new
`nothing new` — a collaborative WASI-target integration PR (custom async executor, `leptos_wasi` crate, wasmCloud/Spin ecosystem support); every design suggestion from reviewers (using the `wasi` crate over raw `wit_bindgen`, targeting `wasm32-wasip2` via `cfg` once stable, splitting into its own crate) is accepted without pushback, so no contested point surfaces.

## f002177 — Tracking: WebAssembly support for iroh (2024-10-10, en)
### Nothing new
`nothing new` — a tracking issue and Q&A about iroh's browser/WASI support (relay-only mode, WebSocket-to-relay, discovery limits in sandboxes); the maintainer (matheus23) answers architecture questions authoritatively and unopposed, so no live disagreement is stated.

## f002233 — iroh 0.27.0 - Squashing Bugs and Taking Names (2024-10-24, en)
### Nothing new
`nothing new` — a single-author release-notes blog post (bug fixes, config simplification, Discovery API streamlining); no second voice or contested point.

## f002301 — Add `unregister_system` command (2024-11-11, en)
### Nothing new
`nothing new` — a small, uncontested naming/rename PR (`remove_system` → `unregister_system`); the one naming question raised is resolved by the maintainer with no pushback.

## f002307 — Leading slash with env::current_dir() in Windows (2024-11-12, en)
### Questions
- Q: When a Rust WASM extension host hits a known-bad upstream WASI behavior (a spurious leading `/` in Windows paths from `std::env::current_dir`) that has both a correct-but-breaking extension-API fix on offer and a pragmatic non-breaking user-space workaround, should the project ship the pragmatic workaround now, or hold out for the correct breaking fix (with API versioning to preserve compatibility)?
  concepts: WASI, wasm extension API, breaking changes, API versioning, Windows path handling, upstream vs. workaround fixes; domains_live: desktop-cli-ui;wasm; positions_seen: pragmatic-workaround-preferred, correct-breaking-fix-preferred
### Claims
- voice: lilnasy | position: pragmatic-workaround-preferred | date: 2025-02-03 | locator: issue #20559, comment 2025-02-03T09:43:55Z | paraphrase: after a workaround PR (#22600) was closed for not being an ideal fix, argues it's still worth shipping since it makes real-world extensions (Astro, Svelte) work now, and packages it as a community Windows build | quote: "the fix wasn't ideal, but perfect shouldn't be the enemy of functional" | practiced_evidence: https://github.com/lilnasy/zed-windows-builds
- voice: yakira-neko | position: correct-breaking-fix-preferred | date: 2025-02-10 | locator: issue #20559, comment 2025-02-10T09:59:32Z | paraphrase: argues the proper fix is the extension-API change in PR #14905, and even though it is a breaking change, compatibility should be handled by shipping a new extension-API version rather than settling permanently for the older workaround | quote: "I believe that #14905 is the best way to solve this issue. Moreover, it is definitely a break[ing] change." | practiced_evidence: none

## f002326 — Auto-initialize PSRAM (2024-11-15, en)
### Nothing new
`nothing new` — an embedded-HAL PR (esp-hal) with naming bikeshed (`psram_pointer` → `psram_raw_info`, `psram_range` visibility) and a debugging exchange over a crash; all points converge to agreement, no persisting disagreement.

## f002341 — Relay outage: A post-mortem (2024-11-19, en)
### Nothing new
`nothing new` — a single-author incident post-mortem (n0/iroh); narrates root cause and fixes with no second voice or contested design point.

## f002453 — iroh 0.30.0 - Slimming Down (2024-12-17, en)
### Nothing new
`nothing new` — a single-author release-notes blog post (API reshuffling, new `Watchable` type, dependency reduction, breaking-changes list); no disagreement stated.

## f002466 — Winch: implement fpu to int conversions for aarch64 (2024-12-21, en)
### Nothing new
`nothing new` — a detailed register-allocation code review in wasmtime's Winch baseline compiler (scratch-register clobbering risk, method-splitting); the reviewer's proposal is accepted by the author with no persisting disagreement.
