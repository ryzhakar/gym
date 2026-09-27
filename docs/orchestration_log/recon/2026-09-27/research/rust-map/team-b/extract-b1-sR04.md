## f001398 — SE-0430 (second review): `sendable` parameter and result values (2024-05-07, en)
### Nothing new
`nothing new` — this is a Swift Evolution keyword-naming review thread; every participant argues about Swift's own `sendable`/`sending`/`transferring` spelling, and none is established in this text as a Voice with a Rust track record. Rust is invoked only twice, in passing, by non-Rust-voices explaining Swift's feature by contrast (Rust's `Unique<T>`, Rust's trouble with cyclic object graphs) — neither is a declared position on a Rust practitioner decision.

## f001401 — Small difference makes suspicion performance decreasing (2024-05-07, en)
### Questions
- Q: What function/code alignment should a JIT-style code generator use to avoid wasting instruction-fetch bandwidth?
  concepts: code generation, cache-line alignment, instruction fetch, JIT compilation; domains_live: wasm; positions_seen: 32-byte-default-reasonable
### Claims
- voice: cfallin (Chris Fallin) | position: 32-byte-default-reasonable | date: 2024-05-14 | locator: issue comment, 2024-05-14T17:03:22Z | paraphrase: the CPU frontend fetches aligned 32B/64B chunks, so a function starting mid-chunk wastes fetch bandwidth; he suspects 32-byte function alignment (Cranelift/Wasmtime x86-64 currently uses 16-byte) would be a more reasonable default in general. | quote: "I suspect a 32B function alignment would be a pretty reasonable default in general" | practiced_evidence: none (proposed as a possible follow-up PR to https://github.com/bytecodealliance/wasmtime, not yet merged in this thread)

## f001515 — iroh 0.17.0 - Everything Is A Little Better (2024-05-24, en)
### Questions
- Q: Should a public-facing name prioritize brevity/memorability or explicit clarity?
  concepts: API naming, public interface design; domains_live: decentralized-iroh; positions_seen: rename-for-clarity-over-fun-brevity
### Claims
- voice: dignifiedquire | position: rename-for-clarity-over-fun-brevity | date: 2024-05-24 | locator: § "The MagicEndpoint is dead, long live the Endpoint" | paraphrase: renamed the public type `MagicEndpoint` to plain `Endpoint`, reasoning that a fun/evocative name became a liability once it got too long, even though the team liked it. | quote: "Fun names are great, but sometimes they get in the way, and while we all loved MagicEndpoint as a name, it just became too long." | practiced_evidence: https://github.com/n0-computer/iroh (renamed type shipped in 0.17.0)

## f001609 — Healing Connections After Network Migration (2024-06-17, en)
### Nothing new
`nothing new` — an explanatory architecture post on how iroh's relay/hole-punching connection migration works; it describes a mechanism the software performs automatically, with no argued position on a decision a Rust practitioner makes differently.

## f001617 — Add language-agnostic snippets (2024-06-19, en)
### Questions
- Q: Should a public-facing name prioritize brevity/memorability or explicit clarity?
  concepts: API naming, tooling/extension naming; domains_live: desktop-cli-ui; positions_seen: name-for-clarity-over-brevity
### Claims
- voice: osiewicz | position: name-for-clarity-over-brevity | date: 2024-06-19 | locator: PR #13253, comment 2024-06-19T11:34:20Z | paraphrase: declined a suggestion to shorten the language-server's name to the abbreviation "scls", preferring to spell out "snippets" so users can infer what the name means. | quote: "I think it makes sense to spell out `snippets` explicitly in the name to make it a bit easier on the users." | practiced_evidence: https://github.com/zed-industries/zed/pull/13253 (merged, full name kept)

## f001724 — 2024 Q3-Q4 Roadmap? (2024-07-12, en)
### Questions
- Q: Should a project's roadmap prioritize performance-focused effort over new-capability work when both compete for the same limited contributor time?
  concepts: project roadmap prioritization, contributor time allocation, performance engineering; domains_live: core; positions_seen: perf-first-for-a-quarter, feature-work-also-serves-perf
### Claims
- voice: ozankabak | position: perf-first-for-a-quarter | date: 2024-07-13 | locator: issue comment, 2024-07-13T09:20:20Z | paraphrase: DataFusion is already in good shape on extensibility/customizability, so the project should dedicate one or two quarters specifically to performance rather than new features. | quote: "It would be great to have one or two quarters where we focus on perf." | practiced_evidence: none stated directly
- voice: notfilippo | position: feature-work-also-serves-perf | date: 2024-07-14 | locator: issue comment, 2024-07-14T17:55:14Z | paraphrase: argues his in-progress logical-types proposal is not purely a feature detour, since it would itself improve performance (late materialization for REE arrays/string views); still agrees to rescope it to be easier to manage given the perf-quarter push. | quote: "I would argue that introducing proper support for logical types would benefit performance, especially in late materialization for REE arrays and string views." | practiced_evidence: https://github.com/apache/datafusion/pull/11160

## f001749 — Upgrade winit to 0.30.2 (2024-07-18, en)
### Questions
- Q: When an external callback API erases a reference's lifetime so it can be stored for later, how should the resulting unsafe surface be structured to stay sound?
  concepts: unsafe, lifetimes, aliasing, FFI/callback integration; domains_live: desktop-cli-ui; positions_seen: thread-local-scoped-storage-over-raw-pointer-cast
- Q: When a transitive dependency upgrade trades one bug for another, should you pin to the older broken version, ship with the new regression, or hold the release?
  concepts: dependency version pinning, semver upgrades, regression management; domains_live: desktop-cli-ui; positions_seen: never-ship-a-known-crash-prefer-soft-guardrails
### Claims
- voice: ArthurBrussee | position: thread-local-scoped-storage-over-raw-pointer-cast | date: 2024-07-26 | locator: PR #4849, comment 2024-07-26T01:00:25Z | paraphrase: the prior integration cast away an `&ActiveEventLoop`'s lifetime to store it for a later callback, which he judged unsound (possible aliased mutable reference, no real outlives guarantee from winit); replaced it with a thread-local holding the pointer only for the paint call's duration — still `unsafe`, but easier to reason about. | quote: "That's really not allowed! At any point there might be an aliased mutable reference, and the comment about how the lifetime outlives the callback doesnt really make sense to me - winit is free to do what it wants!" | practiced_evidence: https://github.com/emilk/egui/pull/4849 (merged)
- voice: emilk | position: never-ship-a-known-crash-prefer-soft-guardrails | date: 2024-07-23 | locator: PR #4849, comment 2024-07-23T13:27:16Z | paraphrase: rejects shipping a version that always crashes on exit on macOS as a tradeoff; between that, shipping with a narrower crash on one feature path (with a guardrail steering users away from it), and blocking the release on an upstream fix, treats the always-crash option as off the table. | quote: "Having eframe always crash on exit on Mac is not an option imho." | practiced_evidence: https://github.com/emilk/egui/pull/4849 (merged; resolved instead by ArthurBrussee's fix above)
