## f004905 — SE-0538: Disconnected (2026-07-17, en)
### Nothing new
Every participant is a Swift core-team or compiler engineer discussing Swift's own naming bikeshed; passing comparisons to Rust (Cell, mem::replace) are asides by non-Rust Voices, so no Voice here carries the public Rust track record a Claim requires.

## f004947 — We're open-sourcing our privacy proxy CLI (2026-07-27, en)
### Questions
- Q: Should a debugging CLI for a protocol specialize narrowly, one tool per protocol, or bundle several related protocols into one tool?
  concepts: CLI design, tool scope; domains_live: desktop-cli-ui; positions_seen: broad multi-protocol tool
### Claims
- voice: Hannah Wang, Ben Yang, Fisher Darling (Cloudflare) | position: one CLI should cover every privacy protocol a team operates (OHTTP, CONNECT proxying, MASQUE, Privacy Pass), rather than a narrow tool per protocol | date: 2026-07-27 | locator: "Why build our own tool?" section | paraphrase: existing OHTTP-only tools (Thomson's Rust implementation, Wood's Go implementation) were useful but narrow; pvcli's differentiator is combining OHTTP, CONNECT proxying, MASQUE and Privacy Pass in one place | quote: "nothing combines OHTTP, CONNECT proxying, MASQUE and Privacy Pass (coming soon) all in one place" | practiced_evidence: https://github.com/cloudflareresearch/pvcli

## f004960 — Protect your relays (2026-07-30, en)
### Questions
- Q: Should a networking library dictate a specific authentication scheme for its own infrastructure, or stay unopinionated and let operators build their own?
  concepts: API design, mechanism vs. policy; domains_live: decentralized-iroh; positions_seen: library stays unopinionated by default, ships an opinionated managed option alongside it
### Claims
- voice: Rae McKelvey (iroh / n0) | position: iroh itself stays unopinionated about relay authentication, leaving the scheme to whoever self-hosts a relay; token-based auth is an opinionated default only for the managed iroh Services offering | date: 2026-07-30 | locator: "The problem: a relay URL is a credential you can't revoke" section | paraphrase: self-run relays are untouched — "you can build your own authentication scheme" — while managed relays now default to API-key-scoped tokens | quote: "iroh is unopinionated about that" | practiced_evidence: https://iroh.computer (iroh_services preset, shipped)

## f004993 — Bevy's Sixth Birthday (2026-08-10, en)
### Questions
- Q: Should a Rust open-source project accept AI-assisted contributions, and how should that be policed?
  concepts: AI-assisted Rust, contribution norms; domains_live: core; positions_seen: strict no-AI policy tried and being revised; personal anti-AI stance
- Q: How should an open-source Rust project's priorities be decided and communicated to its community?
  concepts: governance, roadmaps; domains_live: core; positions_seen: lightweight, non-authoritative "Goals" signal instead of a fixed roadmap or ad hoc "build first, yell for attention"
### Claims
- voice: Carter Anderson (@cart, Bevy creator and Project Lead) | position: a strict no-AI policy was the wrong tool even though AI-assisted work is a real concern; personally opposed to using AI in his own development workflow and worried about AI eroding a community of competent engine developers | date: 2026-08-10 | locator: "AI Policy #" section | paraphrase: the strict "no-AI" policy adopted this year "solved many problems but created many others" (toxic witch hunts, incentivized lying to maintainers, unenforceable), so the community (led by @alice-i-cecile) is drafting a replacement | quote: "solved many problems but created many others (including fostering toxic witch hunts, incentivizing lying to maintainers, enforcement was a hard / impossible task)" | practiced_evidence: none (replacement policy not yet published)
- voice: Carter Anderson (@cart, Bevy creator and Project Lead) | position: project direction should be communicated through a lightweight, non-authoritative "Goals" system (staffed/unstaffed as a focus signal) rather than a fixed roadmap or the prior ad hoc culture | date: 2026-08-10 | locator: "Bevy Project Goals #" section | paraphrase: the initial rollout felt "dictatorial" because staffed/unstaffed was framed as active/inactive; loosened so any approved Goal can get a Working Group even unstaffed, while staffing still signals leadership focus | quote: "This is notably not a 'roadmap' ... This is also not authoritative." | practiced_evidence: https://bevy.org (Bevy Project Goals process, in use)

## f005050 — Announcing Spin v4.1 (2026-08-26, en)
### Questions
- Q: Should a Wasm component sandbox grant capabilities by default (ambient authority), or require every capability — including for middleware and dependencies — to be explicitly listed?
  concepts: capability-based security, sandboxing, WASI; domains_live: wasm; positions_seen: explicit-only, no ambient authority, even for middleware
- Q: When retiring a legacy compatibility path, should maintainers break it immediately or deprecate it gradually with warnings?
  concepts: breaking changes, deprecation policy, semver; domains_live: wasm; positions_seen: gradual, warned deprecation over an immediate break
### Claims
- voice: The Spin Project | position: middleware components get no ambient authority; every capability a middleware needs (e.g. an outbound host) must be explicitly listed in the trigger's inherit_configuration, exactly like any other component dependency | date: 2026-08-26 | locator: "Middleware doesn't get a free pass on capabilities" section | paraphrase: an auth middleware can reach an endpoint only because the underlying component grants that capability and the trigger explicitly inherits it; otherwise the middleware gets nothing | quote: "Middleware gets no ambient authority." | practiced_evidence: https://github.com/spinframework/spin (shipped in 4.1)
- voice: The Spin Project | position: a deprecated compatibility shim (WAGI) should be phased out with warnings and migration time, not removed outright | date: 2026-08-26 | locator: "A heads-up on WAGI" section | paraphrase: 4.1 starts printing deprecation warnings and drops WAGI examples from the repo, but existing WAGI components keep running | quote: "this is the start of a gradual, managed deprecation, not a break" | practiced_evidence: https://github.com/spinframework/spin

## f005053 — Component Composition with Spin 4.0 (2026-08-27, en)
### Questions
- Q: Within one Wasm application, should logic be kept in a single monolithic component, or decoupled into several small components composed via WIT interfaces?
  concepts: component composition, WIT, modularity; domains_live: wasm; positions_seen: decouple into small, independently-versioned components
### Claims
- voice: Thorsten Hans | position: self-contained pieces of application logic (e.g. a classifier) should be split into their own Wasm component, composed into the app via a WIT interface and a declared spin.toml dependency, rather than living inline in the HTTP-triggered component | date: 2026-08-27 | locator: "Recap" section | paraphrase: decoupling the classification logic into its own component "kept the HTTP control flow lean, standard, and easy to maintain," with WIT files as "the single source of truth" for the boundary | quote: "By decoupling the core classification logic into its own Wasm component, we kept the HTTP control flow lean, standard, and easy to maintain" | practiced_evidence: https://github.com/ThorstenHans/component-composition-spin

## f005071 — Xanadu Was Waiting for Agents (2026-09-01, en)
### Questions
- Q: For a multi-actor collaborative system (humans and agents editing together), should convergence come from CRDTs or from a coordinating mechanism (locking, operational transform, a single authoritative server)?
  concepts: CRDTs, distributed state, concurrent editing; domains_live: distributed; positions_seen: CRDTs, no coordination required
### Claims
- voice: Nathan Sobo (Zed founder) | position: convergence for a multi-actor, human-and-agent live document should come from CRDTs rather than a coordinating or locking mechanism | date: 2026-09-01 | locator: "The dependency tree exists today" section | paraphrase: lists CRDTs, "formalized in 2011," as "the center of Zed's own work for the past decade," letting a Delta worktree be "edited by several people and agents on different continents at once" with no coordination step | quote: "Convergence without coordination." | practiced_evidence: https://zed.dev (Zed and Delta/DeltaDB, shipped)
