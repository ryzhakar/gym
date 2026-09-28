## notfilippo
name: Filippo
identity: https://github.com/notfilippo (bio "Finding events, really fast @Datadog"; company "@Datadog @apache")
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `datasketches` crate on crates.io, 2 real reverse dependencies — https://crates.io/api/v1/crates/datasketches/reverse_dependencies (2026-09-28)
checked: production (no employer post tying Datadog to Rust-in-production for him specifically); role (not listed on Apache DataFusion's committers/PMC governance page)

## oakchris1955
name: Oakchris1955 (GitHub login; real name not disclosed)
identity: https://github.com/Oakchris1955; own blog oakchris1955.eu
type: educator
verdict: MEETS
track_record:
- book/course/talk/post: "Bypassing specialization in Rust" (the original post in the same series as our cited claim) is linked from This Week in Rust — https://github.com/rust-lang/this-week-in-rust/blob/master/content/2025-07-23-this-week-in-rust.md (2025-07-23), linking https://oakchris1955.eu/posts/bypassing_specialization/
checked: the claim's actual source is the follow-up post (oakchris1955.eu/posts/bypassing_specialization_followup, 2025-07-26), a distinct URL from the TWiR-linked original; the original itself scored only 46 HN points, below the ≥100 bar — https://hn.algolia.com/api/v1/search?query=oakchris1955 (2026-09-28); no separate reach signal found for the follow-up itself; crate-dependents/production/role: nothing found

## obi1kenobi
name: Predrag Gruevski
identity: https://github.com/obi1kenobi (blog predr.ag)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `trustfall` (11 reverse deps) and `cargo-semver-checks` (6 reverse deps) — https://crates.io/api/v1/crates/trustfall/reverse_dependencies, https://crates.io/api/v1/crates/cargo-semver-checks/reverse_dependencies (2026-09-28)
influence:
- owns 10 published crates total (apidiff, cargo-invariant, trustfall, cargo-semver-checks, etc.) — https://crates.io/api/v1/crates?user_id=167649 (2026-09-28)

## okhsunrog
name: Danila Gornushko
identity: https://github.com/okhsunrog (blog okhsunrog.dev)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `lcd-async` (3 reverse deps) among 17 published embedded-driver crates — https://crates.io/api/v1/crates/lcd-async/reverse_dependencies (2026-09-28)
influence:
- also owns `drv8301-dd` (1 reverse dep) — https://crates.io/api/v1/crates/drv8301-dd/reverse_dependencies (2026-09-28)

## osiewicz
name: Piotr Osiewicz
identity: https://github.com/osiewicz (bio "@zed-industries, @wezel-build")
type: builder
verdict: MEETS
track_record:
- production: employed at Zed Industries; cited claim is his own PR comment on zed-industries/zed, Zed's own Rust editor codebase shipped in production — https://github.com/zed-industries/zed/pull/13253 (2024-06-19)
checked: crate-dependents (no crates.io account found)

## ouillie
name: Will Noble
identity: https://github.com/ouillie
type: critic
verdict: FAILS
checked: crate-dependents (no crates.io account under `ouillie`); production (no employer disclosed, no Rust-in-production statement found); role (not a public member of the WebAssembly or bytecodealliance GitHub orgs); book/course/talk/post (none found)

## ozankabak
name: Mehmet Ozan Kabak
identity: https://github.com/ozankabak
type: builder
verdict: MEETS
track_record:
- role: listed as Apache DataFusion PMC member on the project's official governance page — https://datafusion.apache.org/contributor-guide/governance.html (2026-09-28)
influence:
- co-founder/CEO of Synnada, Inc., which builds on DataFusion in Rust — https://github.com/ozankabak (2026-09-28)

## parasyte
name: Jay Oster
identity: https://github.com/parasyte (blog kodewerx.org)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `pixels` crate, 69 reverse dependencies — https://crates.io/api/v1/crates/pixels/reverse_dependencies (2026-09-28)

## pauan
name: Pauan (GitHub login; no real name disclosed; bio "Former Rust Wasm Core member")
identity: https://github.com/Pauan
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `futures-signals` (46 reverse deps) and `dominator` (13 reverse deps) — https://crates.io/api/v1/crates/futures-signals/reverse_dependencies, https://crates.io/api/v1/crates/dominator/reverse_dependencies (2026-09-28)

## pavel-perikov
name: Pavel Perikov (name as it appears on the LinkedIn comment itself)
identity: untied — only a display name on a LinkedIn comment (genuine commenter account, per the archived page's "Report this comment" affordance), no linked profile page or cross-platform account found under this name
type: critic
verdict: UNKNOWN
checked: crate-dependents (no crates.io account found under this name); production (no employer disclosed); role (no matching Rust-project team page, no GitHub account found); book/course/talk/post (none found); identity (no persistent profile beyond the comment's display name, so nothing can be safely credited to this person)

## pickfire
name: Ivan Tham
identity: https://github.com/pickfire (blog pickfire.llk.moe)
type: builder
verdict: FAILS
checked: crate-dependents (owns `babelfish`, `eva`, `ve`, all 0 reverse dependencies — https://crates.io/api/v1/crates/eva/reverse_dependencies, 2026-09-28); production (no employer disclosed); role (not a public member of the DioxusLabs GitHub org); book/course/talk/post (no TWiR/HN/Lobsters reach found for pickfire.llk.moe)

## playfulfence
name: Kirill Mikhailov
identity: https://github.com/playfulFence (GitHub profile discloses real name and company "@espressif")
type: builder
verdict: MEETS
track_record:
- production: GitHub profile lists company `@espressif`, a real Rust-embedded employer (esp-rs) — https://api.github.com/users/playfulFence (2026-09-28)
- role: authored and had merged PR #5002 to esp-rs/esp-hal (Espressif's Rust embedded HAL), 166 authored commits in that repo, public member of the esp-rs GitHub org — https://github.com/esp-rs/esp-hal/pull/5002 (2026-02-17), https://api.github.com/search/commits?q=author:playfulFence+repo:esp-rs/esp-hal (2026-09-28), https://api.github.com/users/playfulFence/orgs (2026-09-28)
checked: crate-dependents (not checked separately — role/production already established); book/course/talk/post (not checked)

## pm
name: pm (a GitHub account with this exact login exists, but nothing ties it to the lobste.rs commenter)
identity: untied — "pm" is too generic a handle to tie the lobste.rs commenter to any specific person; no cross-reference in the source content
type: unset
verdict: UNKNOWN
checked: identity only — handle-collision risk too high to credit any track-record kind to this id

## porky11
name: Fabio Krapohl
identity: https://github.com/porky11 (blog p11c.xyz; bio "Game system architect")
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `scalars` (16 reverse deps), `inner-space` (15), and `vector-space` (9), among 101 published crates — https://crates.io/api/v1/crates/scalars/reverse_dependencies (2026-09-28)

## primoly
name: primoly (GitHub login; no real name disclosed)
identity: https://github.com/primoly — own GitHub profile ties the PR comment to a consistent handle, but discloses no name or employer
type: critic
verdict: FAILS
checked: crate-dependents (no crates.io account under `primoly`); production (no employer disclosed); role (not a public member of the WebAssembly or bytecodealliance GitHub orgs); book/course/talk/post (none found; the account's 17 public repos are all forks of wasm-ecosystem tools, no original blog/talk)

## quanyi-ma
name: Quanyi Ma
identity: https://github.com/genedna (GitHub `name` field = "Quanyi Ma"; blog maquanyi.com)
type: builder
verdict: MEETS
track_record:
- talk: "Embracing Monorepo and LLM Evolution," Rust Global @ RustConf 2024, published on the Rust Foundation's own YouTube channel and linked from This Week in Rust — https://www.youtube.com/watch?v=qHcfiCmcIf8, https://github.com/rust-lang/this-week-in-rust/blob/master/content/2024-11-20-this-week-in-rust.md (2024-11-20)
influence:
- top contributor to gitmono-dev/mega (formerly web3infra-foundation/mega), an open-source Rust monorepo engine, 518 stars — https://github.com/gitmono-dev/mega (2026-09-28)

## quinedot
name: QuineDot (GitHub login; no real name disclosed)
identity: https://github.com/QuineDot — own GitHub profile ties the forum handle to a consistent identity; no name or employer disclosed
type: educator
verdict: FAILS
checked: crate-dependents (no crates.io account found); production (no employer disclosed); role (no rust-lang team listing); book/course/talk/post (author of the widely-referenced rust-learning guide at quinedot.github.io/rust-learning; no This Week in Rust link found, and its highest-scoring known HN submission reached only 7 points, below the ≥100 bar — https://hn.algolia.com/api/v1/search?query=QuineDot, 2026-09-28)

## r-diger-klaehn
name: Rüdiger Klaehn
identity: https://github.com/rklaehn — byline "by Rüdiger Klaehn" on iroh.computer/blog (n0-computer's official product blog); confirmed contributor to n0-computer/iroh on GitHub
type: builder
verdict: MEETS
track_record:
- production: authors multiple posts on n0-computer's official iroh product blog about building iroh, a Rust P2P networking library with 276 crates.io reverse dependencies, e.g. — https://iroh.computer/blog/async-rust-challenges-in-iroh (2024-07-31)
- crate-dependents: owns `bao-tree` (16 reverse deps) and `iroh-blake3` (3 reverse deps) — https://crates.io/api/v1/crates/bao-tree/reverse_dependencies (2026-09-28)
influence:
- iroh (team-owned crate he contributes to) has 276 crates.io reverse dependents — https://crates.io/api/v1/crates/iroh/reverse_dependencies (2026-09-28)

## r-diger-klaehn-n0-iroh-iroh-blobs
name: Rüdiger Klaehn (n0, iroh/iroh-blobs) — same person as `r-diger-klaehn`, a disambiguation of the same id
identity: same as `r-diger-klaehn` above
type: builder
verdict: MEETS
track_record:
- production: this claim's source is https://iroh.computer/blog/hashing-multiple-blobs-with-BLAKE3 (2025-10-15), byline confirmed "by Rüdiger Klaehn", discussing the iroh-blobs component's BLAKE3 hashing internals
checked: not re-derived independently — same person and evidence base as `r-diger-klaehn`

## r-my-rakic-on-behalf-of-the-compiler-performance-working
name: Rémy Rakic (on behalf of the compiler performance working group)
identity: byline on the official Rust Blog — https://blog.rust-lang.org/2025/09/01/rust-lld-on-1.90.0-stable
type: role
verdict: MEETS
track_record:
- role: posts on the official Rust Blog explicitly on behalf of the compiler performance working group, a rust-lang project working group — https://blog.rust-lang.org/2025/09/01/rust-lld-on-1.90.0-stable (2025-09-01)

## rae-mckelvey-iroh-n0
name: Rae McKelvey (iroh / n0)
identity: name disclosed as byline on n0-computer's official iroh product blog — https://iroh.computer/blog/authenticated-relays (no separate GitHub account confirmed under this name)
type: builder
verdict: MEETS
track_record:
- production: authors a post on n0-computer's official iroh blog about a production security feature (authenticated relays) for iroh, a Rust library with 276 crates.io reverse dependents — https://iroh.computer/blog/authenticated-relays (2026-07-30)

## rahulchaphalkar
name: Rahul
identity: https://github.com/rahulchaphalkar (company "Intel Corporation")
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns Intel's `openvino` Rust bindings (4 reverse deps) and `ittapi` (8 reverse deps) — https://crates.io/api/v1/crates/openvino/reverse_dependencies, https://crates.io/api/v1/crates/ittapi/reverse_dependencies (2026-09-28)

## ralfjung
name: Ralf Jung
identity: https://github.com/RalfJung (blog ralfj.de)
type: role
verdict: MEETS
track_record:
- role: lead of the rust-lang `opsem` team and lead+member of the rust-lang `miri` team per the official rust-lang/team governance repo — https://github.com/rust-lang/team/blob/master/teams/opsem.toml, https://github.com/rust-lang/team/blob/master/teams/miri.toml (2026-09-28)

## ramfox
name: ramfox (GitHub login; no real name disclosed)
identity: https://github.com/ramfox (company "n0.computer"; public member of the n0-computer GitHub org; contributor to n0-computer/iroh; byline "by ramfox" on multiple iroh.computer/blog posts)
type: builder
verdict: MEETS
track_record:
- production: authors multiple posts on n0-computer's official iroh product blog about building iroh, a Rust library with 276 crates.io reverse dependents, e.g. — https://iroh.computer/blog/iroh-0-96-0-the-quic-multipaths-to-1-0 (2026-01-27)
influence:
- owns `n0-error` crate, 46 crates.io reverse dependencies — https://crates.io/api/v1/crates/n0-error/reverse_dependencies (2026-09-28)

## ramfox-byline-iroh-blog-rust-connection-in-source-iroh
name: ramfox — same person as `ramfox`, a disambiguation of the same id
identity: same as `ramfox` above
type: builder
verdict: MEETS
track_record:
- production: this claim's source is https://iroh.computer/blog/iroh-0-19-make-it-your-own (2024-06-27), byline confirmed "by ramfox"
checked: not re-derived independently — same person and evidence base as `ramfox`
