## antimora-tracel-ai-burn-maintainer
name: Dilshod Tadjibaev (antimora)
identity: https://github.com/antimora
type: builder
verdict: MEETS
track_record:
- crate-dependents: burn has real reverse dependents on crates.io (e.g. `fsrs` v6.6.2 depends on `burn`) — https://crates.io/api/v1/crates/burn/reverse_dependencies (2026-09-28)
- role: GitHub bio self-identifies "Working on Speech Recognition and Burn (Deep Learning Framework in Rust)"; author of the exact PR review comments quoted in the claims — https://github.com/tracel-ai/burn/pull/4813 (2026-04-21)
influence:
- Reviews gating merges into burn, a Rust deep-learning framework with downstream crates depending on it — https://github.com/tracel-ai/burn/pull/5617 (2026-09-08)
checked: production, book/course/talk/post

## antonio-pirino
name: Antonio Pirino (GitHub: apiraino; video title spells surname "Piraino")
identity: https://github.com/apiraino — tied via rust-lang/team person file listing his exact GitHub id 6098822
type: builder
verdict: MEETS
track_record:
- role: `apiraino` is a listed member in rust-lang/team's `teams/compiler.toml` and `teams/archive/wg-prioritization.toml`, matching his own on-stage description of being "merged into the compiler team" after running the prioritization/regressions working group — https://github.com/rust-lang/team/blob/master/teams/compiler.toml (2026-09-28)
influence:
- Self-reported track record since 2018 doing regression triage/prioritization for the Rust compiler, presented at a Rust conference — https://youtube.com/watch?v=-3KKeeZkYog (2025-06-10)
checked: crate-dependents, production, book/course/talk/post

## araz-abishov
name: Araz Abishov
identity: https://github.com/ArazAbishov — blog field on profile (abishov.com) matches claim source exactly
type: builder
verdict: MEETS
track_record:
- crate-dependents: `pvec` crate (repo pvec-rs) has 0 reverse dependencies on crates.io — https://crates.io/api/v1/crates/pvec/reverse_dependencies (2026-09-28) — does not meet bar
- book/course/talk/post: his post "Visualizing Persistent Vectors with Rust and WebAssembly" (the exact claim source) was linked from This Week in Rust 2026-02-18 — https://github.com/rust-lang/this-week-in-rust/blob/master/content/2026-02-18-this-week-in-rust.md (2026-02-18)
influence:
- Author of pvec-rs (RRB-tree persistent vector implementation), ~3.1k crates.io downloads total — https://crates.io/api/v1/crates/pvec (2026-09-28)
checked: production, role

## arnaud-gourlay
name: Arnaud Gourlay
identity: https://github.com/agourlay — blog field matches claim source (agourlay.github.io) exactly
type: builder
verdict: MEETS
track_record:
- production: GitHub profile lists company "@qdrant"; Qdrant is a Rust vector database/search engine — https://github.com/qdrant/qdrant (2026-09-28)
- production: recent commits authored by `agourlay` merged into qdrant/qdrant, e.g. "feat: optional dial9 Tokio telemetry..." 2026-09-03 — https://github.com/qdrant/qdrant/commits?author=agourlay (2026-09-28)
influence:
- Ships Rust in production at Qdrant (an adopter in the target "distributed systems"/ML-adjacent space) — https://github.com/qdrant/qdrant (2026-09-28)
checked: crate-dependents, role, book/course/talk/post

## arqu
name: Asmir Avdicevic (arqu)
identity: https://github.com/arqu
type: builder
verdict: MEETS
track_record:
- production: authored the exact post-mortem blog post ("by Arqu") describing a production relay outage for n0-computer/iroh — https://iroh.computer/blog/relay-down-a-post-mortem (2024-11-19)
- production: commits authored by `arqu` merged into n0-computer/iroh — https://github.com/n0-computer/iroh/commits?author=arqu (2026-09-28)
influence:
- Engineer on iroh, a Rust P2P networking crate with real reverse dependents (e.g. `iroh-gossip`) — https://crates.io/api/v1/crates/iroh/reverse_dependencies (2026-09-28)
checked: crate-dependents (personal), role, book/course/talk/post

## arqu-n0-computer-iroh-engineer-production-post-mortem-author
name: Asmir Avdicevic (arqu) — same real person as voice `arqu`, verified independently
identity: https://github.com/arqu
type: builder
verdict: MEETS
track_record:
- production: same post-mortem, "by Arqu", n0-computer/iroh production relay outage — https://iroh.computer/blog/relay-down-a-post-mortem (2024-11-19)
- role: commit history on n0-computer/iroh under handle `arqu` — https://github.com/n0-computer/iroh (2026-09-28)
influence:
- Same as `arqu`: iroh has real crates.io dependents — https://crates.io/api/v1/crates/iroh/reverse_dependencies (2026-09-28)
checked: crate-dependents (personal), book/course/talk/post

## arthur-zucker-hugging-face-tokenizers-team
name: Arthur Zucker
identity: https://github.com/ArthurZucker — bio "@huggingface", company @huggingface
type: builder
verdict: MEETS
track_record:
- crate-dependents: `tokenizers` crate has real dependents (e.g. `candle-core`) and 8.7M+ downloads on the dependent version alone — https://crates.io/api/v1/crates/tokenizers/reverse_dependencies (2026-09-28)
- role: commits authored by `ArthurZucker` merged into huggingface/tokenizers — https://github.com/huggingface/tokenizers/commits?author=ArthurZucker (2026-09-28)
- production: co-authored the official HF blog post announcing tokenizers v1, naming the crate split described in the claims — https://huggingface.co/blog/tokenizers-v1 (2026-09-21)
influence:
- Maintainer-level contributor to `tokenizers`, one of the most-depended-on ML-adjacent Rust crates — https://crates.io/api/v1/crates/tokenizers (2026-09-28)
checked: book/course/talk/post

## arthurbrussee
name: Arthur Brussee
identity: https://github.com/ArthurBrussee — company "DeepMind"
type: builder
verdict: MEETS
track_record:
- role: authored the exact quoted review comment (2024-07-26T01:00:25Z) on egui PR #4849 — https://github.com/emilk/egui/pull/4849 (2024-07-26)
- crate-dependents: owns `brush`, a 3D Gaussian-splatting Rust project with 5,115 GitHub stars — https://github.com/ArthurBrussee/brush (2026-09-28)
influence:
- Employed at DeepMind; maintains `brush`, a well-known Rust 3D-reconstruction project intersecting the ML-adjacent target domain — https://github.com/ArthurBrussee/brush (2026-09-28)
checked: production (DeepMind's own Rust-in-production naming not directly evidenced), book/course/talk/post

## asahi-lina
name: Hoshino Lina (publicly known as "Asahi Lina")
identity: https://github.com/HoshinoLina — persona corroborated independently by Ars Technica reporting
type: builder
verdict: MEETS
track_record:
- production: wrote the Apple GPU (Asahi) driver's Rust code for the mainline-adjacent Asahi Linux kernel effort; the only kernel panics traced to the surrounding C code, per her own Mastodon statement quoted by a reputable outlet — https://arstechnica.com/gadgets/2024/09/rust-in-linux-lead-retires-rather-than-deal-with-more-nontechnical-nonsense (2024-09, per article)
influence:
- Developer on the Asahi Linux project; GPU driver work is widely cited in Rust-for-Linux discourse — https://arstechnica.com/gadgets/2024/09/rust-in-linux-lead-retires-rather-than-deal-with-more-nontechnical-nonsense (2024-09)
checked: crate-dependents, role, book/course/talk/post

## async-book-rust-lang-github-io-rust-async-working-group
name: async-book (Rust Async Working Group)
identity: https://github.com/rust-lang/async-book — official rust-lang org repository, 2,215 stars
type: institution
verdict: MEETS
track_record:
- book/course/talk/post: the book itself is the listing URL, published under the official rust-lang GitHub org — https://github.com/rust-lang/async-book (2026-09-28)
influence:
- The canonical Rust project book on async programming, maintained by the Rust Async Working Group — https://rust-lang.github.io/async-book (2026-09-27, claim date)
checked: crate-dependents, production, role (not applicable to an institutional voice)

## aturon-aaron-turon-rust-language-design-team
name: Aaron Turon (aturon)
identity: https://github.com/aturon — bio "Engineer at Fastly, working on Compute", company Fastly
type: language-designer
verdict: MEETS
track_record:
- role: listed in rust-lang/team's `teams/lang.toml`, `teams/libs.toml`, `teams/cargo.toml`, and multiple archived working groups (`wg-net`, `core`, `initial-design-and-impl`) — https://github.com/rust-lang/team/tree/master/teams (2026-09-28)
influence:
- Former Rust language-design team lead, quoted and archived in the community's This Week in Rust "quote of the week" thread — https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (2017-08-31)
checked: crate-dependents, production, book/course/talk/post

## author-of-ideas-reifying-ideas-reify-ing
name: ifsheldon (GitHub handle; no public legal name given)
identity: https://github.com/ifsheldon — owns both the blog's own source repo (`ideas_reifying`) and the `wasi_mindmap` example repo the article links to
type: builder
verdict: MEETS
track_record:
- book/course/talk/post: a release note by the same author (`serde-const-default` v0.1) was linked from This Week in Rust 2026-05-27 — https://github.com/rust-lang/this-week-in-rust/blob/master/content/2026-05-27-this-week-in-rust.md (2026-05-27)
- crate-dependents: `serde-const-default` has 0 reverse dependencies on crates.io — https://crates.io/api/v1/crates/serde-const-default/reverse_dependencies (2026-09-28) — does not meet bar
influence:
- Author of the WASIp2 guide referenced in the claims, and of the `wasi_mindmap` example repo it points to — https://ideas.reify.ing/en/blog/complete-guide-to-wasip2-for-rust-python-programmers (2026-09-22)
checked: production, role

## author-of-ideas-reifying-ideas-reify-ing-not-named-in-the
name: ifsheldon — same underlying identity as the voice above, verified independently
identity: https://github.com/ifsheldon
type: builder
verdict: MEETS
track_record:
- book/course/talk/post: same TWiR-linked release note by the same GitHub account — https://github.com/rust-lang/this-week-in-rust/blob/master/content/2026-05-27-this-week-in-rust.md (2026-05-27)
influence:
- Same WASIp2 guide and example repo — https://ideas.reify.ing/en/blog/complete-guide-to-wasip2-for-rust-python-programmers (2026-09-22)
checked: crate-dependents, production, role

## b5
name: Brendan O'Brien (b5)
identity: https://github.com/b5 — bio "Caretaker at @n0-computer"
type: builder
verdict: MEETS
track_record:
- production: authored the exact blog post ("by b5") announcing iroh's FFI bindings policy — https://iroh.computer/blog/ffi-updates (2025-02-12)
- role: self-described "Caretaker at @n0-computer", the org behind iroh
influence:
- Caretaker-level role at n0-computer/iroh, a Rust P2P crate with real crates.io dependents — https://crates.io/api/v1/crates/iroh/reverse_dependencies (2026-09-28)
checked: crate-dependents (personal), book/course/talk/post

## badeend
name: Dave Bakker
identity: https://github.com/badeend — crates.io account cross-check confirms same login (id 297534)
type: builder
verdict: FAILS
track_record: none found meeting the bar
influence:
- Active commenter on the WebAssembly component model spec (map ordering/duplicate-key semantics) but no owned crates on crates.io, no commits merged into WebAssembly/component-model, and no Rust project/foundation role found — https://github.com/WebAssembly/component-model/pull/554 (2025-08-24)
checked: crate-dependents, production, role, book/course/talk/post

## bd103
name: BD103 (GitHub handle; blog bd103.dev)
identity: https://github.com/BD103 — public member of the bevyengine org, listed on bevy.org's community people page
type: builder
verdict: MEETS
track_record:
- role: public member of the `bevyengine` GitHub org and listed on the official Bevy community people page — https://bevy.org/community/people/ (2026-09-28)
- role: 97 commits authored by `BD103` merged into bevyengine/bevy — https://github.com/bevyengine/bevy/commits?author=BD103 (2026-09-28)
influence:
- Recognized Bevy project team member (self-described "Bevy contributor, Rust enthusiast, and CI wizard") — https://bevy.org/community/people/ (2026-09-28)
checked: crate-dependents, production, book/course/talk/post

## benwis-leptos-maintainer
name: Ben Wishovich (benwis)
identity: https://github.com/benwis — blog benw.is
type: builder
verdict: MEETS
track_record:
- role: authored the exact quoted comment (2024-10-06T02:05:17Z) on leptos-rs/leptos#3063, and in the same thread creates a new repo under the leptos-rs org and adds another user as maintainer ("I've created the leptos_wasi repo under the leptos org and added you as a maintainer") — https://github.com/leptos-rs/leptos/issues/3063 (2024-10-06)
influence:
- Maintainer-level access on the leptos-rs org (repo creation + maintainer appointment authority), a widely used Rust frontend framework — https://github.com/leptos-rs/leptos (2026-09-28)
checked: crate-dependents (personal), production, book/course/talk/post

## bjoernq
name: Björn Quentin (bjoernQ)
identity: https://github.com/bjoernQ — bio "@espressif 💖 Rust everywhere 💖"
type: builder
verdict: MEETS
track_record:
- production: company field "@espressif"; Espressif is the semiconductor company behind the ESP32 chips that esp-hal targets
- role: 100+ commits (capped at page size) authored by `bjoernQ` merged into esp-rs/esp-hal — https://github.com/esp-rs/esp-hal/commits?author=bjoernQ (2026-09-28)
influence:
- Core/lead maintainer of esp-hal, the Rust embedded HAL for Espressif chips (target domain: embedded) — https://github.com/esp-rs/esp-hal (2026-09-28)
checked: crate-dependents (personal), book/course/talk/post

## bjorn3
name: bjorn3 (GitHub handle; no public legal name)
identity: https://github.com/bjorn3 — bio company "@tweedegolf"; listed in rust-lang/team's person directory (`people/bjorn3.toml`)
type: builder
verdict: MEETS
track_record:
- role: member of rust-lang/team `teams/compiler.toml`, `teams/rust-for-linux.toml`, `teams/wg-parallel-rustc.toml`, `teams/goal-owners.toml` — https://github.com/rust-lang/team/tree/master/teams (2026-09-28)
- role: authored the exact quoted review comment (2026-09-07T21:21:42Z) on bytecodealliance/wasmtime#14294 — https://github.com/bytecodealliance/wasmtime/pull/14294 (2026-09-07)
- crate-dependents: author of `rustc_codegen_cranelift`, an alternate Rust compiler codegen backend (19 stars on the personal fork used for development; shipped as part of upstream rustc) — https://github.com/bjorn3/rustc_codegen_cranelift (2026-09-28)
influence:
- Rust compiler team member and Rust-for-Linux team member; author of the cranelift codegen backend used for fast debug builds — https://github.com/rust-lang/team/blob/master/teams/compiler.toml (2026-09-28)
checked: production, book/course/talk/post

## bogdan-petru
name: bogdan-petru (GitHub handle; no public legal name, company, or bio)
identity: https://github.com/bogdan-petru — handle confirmed as author of the exact quoted PR comments
type: builder
verdict: FAILS
track_record: none found meeting the bar
influence:
- 10+ commits authored by `bogdan-petru` merged into embassy-rs/embassy (a widely used embedded async Rust framework), but not an org member, no owned crate, and no employer/role evidence found — https://github.com/embassy-rs/embassy/pull/5175 (2026-02-05)
checked: crate-dependents, production, role, book/course/talk/post

## bojan-serafimov
name: Bojan Serafimov
identity: byline on Neon's own company blog: "Bojan Serafimov – Software Engineer" (no linked GitHub/LinkedIn profile found, but the name, title and employer are directly published by Neon)
type: builder
verdict: MEETS
track_record:
- production: authored the exact blog post as a Neon (part of Databricks) Software Engineer, describing production use of the `rpds` Rust crate in Neon's storage engine's WAL-indexing read path — https://neon.com/blog/persistent-structures-in-neons-wal-indexing (2023-05-19 byline date; claim dated 2024-03-01)
influence:
- Software Engineer at Neon, a Rust-based serverless Postgres storage engine (target domain: distributed systems) — https://neon.com/blog/persistent-structures-in-neons-wal-indexing (2023-05-19)
checked: crate-dependents (personal), role, book/course/talk/post

## boringcactus-melody
name: Melody Horn (boringcactus)
identity: https://github.com/boringcactus — blog https://www.boringcactus.com matches claim source exactly
type: critic
verdict: MEETS
track_record:
- book/course/talk/post: "A 2025 Survey of Rust GUI Libraries" (the exact claim source) was linked from This Week in Rust 2025-04-16 — https://github.com/rust-lang/this-week-in-rust/blob/master/content/2025-04-16-this-week-in-rust.md (2025-04-16)
influence:
- Author of a recurring, widely cited annual "State of Rust GUI libraries" survey (2021, 2023, 2025 editions found via HN), max recorded HN score 18 (below the ≥100 bar on its own, but the TWiR link independently satisfies the post bar) — https://hn.algolia.com/api/v1/search?query=boringcactus%20rust%20gui (2026-09-28)
checked: crate-dependents, production, role

## brooklyn-zelenka
name: Brooklyn Zelenka (expede)
identity: https://github.com/expede — blog notes.brooklynzelenka.com matches claim source exactly; company "@inkandswitch"
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns 47 crates.io crates under this account (e.g. `bijoux`, `beekem`), several with real downstream dependents — e.g. `bijoux` has 4 reverse dependencies — https://crates.io/api/v1/crates/bijoux/reverse_dependencies (2026-09-28)
influence:
- Researcher/engineer at Ink & Switch; maintains multiple Rust crates in the local-first/CRDT space (`keyhive`, `subduction`, `bijoux` family) — https://github.com/inkandswitch (2026-09-28)
checked: production, role, book/course/talk/post

## brooksmtownsend-wasmcloud-engineer-contributor-to-mio-tokio
name: Brooks Townsend (brooksmtownsend)
identity: https://github.com/brooksmtownsend — company "@cosmonic"; public member of the wasmCloud GitHub org
type: builder
verdict: MEETS
track_record:
- role: public member of the `wasmCloud` GitHub org — https://github.com/orgs/wasmCloud/people (2026-09-28)
- role: authored the exact quoted comment (2024-10-11T13:37:26Z) on leptos-rs/leptos#3063 about `wasm32-wasip2` — https://github.com/leptos-rs/leptos/pull/3063 (2024-10-11)
influence:
- wasmCloud engineer (Cosmonic); wasmCloud is a Rust-based WebAssembly orchestration platform (target domains: wasm, distributed systems) — https://github.com/orgs/wasmCloud/people (2026-09-28)
checked: crate-dependents (personal), production (direct mio/tokio contribution not found under this exact handle/repo), book/course/talk/post

## bruce-perens
name: Bruce Perens
identity: https://github.com/bruceperens — blog perens.com; independently one of the most publicly documented identities in open source (OSI co-founder, former Debian Project Leader)
type: critic
verdict: FAILS
track_record: none of the four bar kinds found meeting it for Rust specifically
influence:
- Wrote a widely commented (473 reactions, 96 comments) LinkedIn post praising Rust over C/C++ for low-level work, matching the claim quote exactly, but the post was not found linked from This Week in Rust and has no confirmed ≥100 HN or ≥20 Lobsters discussion — https://linkedin.com/posts/bruce-perens_i-have-written-in-dozens-of-computer-languages-activity-7413127858266734592-iMc5 (2026-01, per Wayback capture)
- Has one small, unpublished (not on crates.io) personal Rust repo (`lume`) — https://github.com/bruceperens/lume (2026-09-28)
checked: crate-dependents, production, role, book/course/talk/post
