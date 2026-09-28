## 2e71828
name: 2e71828
identity: untied
type: unset
verdict: UNKNOWN
track_record:
- (none found)
influence:
- (none found)
checked: crate-dependents, production, role, book/course/talk/post — all blocked: GitHub account https://github.com/2e71828 exists but has 0 public repos, no name, no bio; internals.rust-lang.org profile (id 6499) has no display name either. No independent identity tie found.

## aatch
name: James Miller (Aatch)
identity: https://github.com/Aatch — GitHub profile confirms 69 authored PRs against rust-lang/rust including MIR inlining work
type: builder
verdict: MEETS
track_record:
- role: authored 69 PRs against rust-lang/rust (e.g. "[MIR] Initial implementation of inlining" #36593, "[MIR] Implement Inlining" #36648) — https://github.com/rust-lang/rust/pull/36593 (2016-09-15)
- crate-dependents: owns/maintains `noise` (noise-rs), 129 real reverse dependents on crates.io — https://crates.io/api/v1/crates/noise/reverse_dependencies (checked 2026-09-28)
influence:
- 129 crates depend on noise-rs — https://crates.io/api/v1/crates/noise/reverse_dependencies (2026-09-28)
- 69 merged/authored contributions to rustc itself, including foundational MIR inlining — https://github.com/rust-lang/rust/pull/36593 (2016-09-15)
checked: production, book/course/talk/post — no additional evidence sought once role+crate-dependents confirmed MEETS.

## abrown
name: Andrew Brown
identity: https://github.com/abrown — public member of the bytecodealliance GitHub org
type: builder
verdict: MEETS
track_record:
- role: public member of the bytecodealliance org (Wasmtime's governing foundation) — https://api.github.com/orgs/bytecodealliance/public_members (checked 2026-09-28)
- production: active reviewer/contributor on bytecodealliance/wasmtime PRs (e.g. PR #9234, #10836) — https://github.com/bytecodealliance/wasmtime/pull/9234 (2024-09-20)
influence:
- Wasmtime has 803 real crates.io reverse dependents — https://crates.io/api/v1/crates/wasmtime/reverse_dependencies (2026-09-28)
checked: crate-dependents (no personal crate found), book/course/talk/post — not needed once role confirmed MEETS.

## adam
name: Adam Chalmers
identity: https://adamchalmers.com — blog confirms Rust production work at Cloudflare and Zoo.dev, and a talk on API-schema/codegen themes matching the source video (EuroRust 2024, "Code as contract as code")
type: builder
verdict: MEETS
track_record:
- production: builds KCL at Zoo.dev in Rust; previously maintained API servers/clients in Rust at Cloudflare — https://adamchalmers.com (checked 2026-09-28)
- talk: EuroRust 2024 talk on API/schema codegen matching source video content — https://youtube.com/watch?v=bjgGboWCTDw (2024, EuroRust)
influence:
- EuroRust conference talk slot (major European Rust conference) — https://youtube.com/watch?v=bjgGboWCTDw (2024-11-20 per claim date)
checked: crate-dependents, role — not pursued once production+talk confirmed MEETS.

## adam-surname-unconfirmed-self-id-only
name: Adam Chalmers (surname unconfirmed in-source; tied externally)
identity: https://adamchalmers.com — same EuroRust 2024 talk (source f011186) as voice `adam`; the in-video self-ID gave only a first name, but topic/employer/video match ties it to Adam Chalmers
type: builder
verdict: MEETS
track_record:
- production: same as `adam` — Cloudflare/Zoo.dev Rust work — https://adamchalmers.com (checked 2026-09-28)
- talk: same EuroRust 2024 talk — https://youtube.com/watch?v=bjgGboWCTDw (2024)
influence:
- same EuroRust 2024 conference slot — https://youtube.com/watch?v=bjgGboWCTDw (2024-11-20 per claim date)
checked: crate-dependents, role — not pursued once production+talk confirmed MEETS.

## adriangb
name: Adrian Garcia Badaracco
identity: https://github.com/adriangb — crates.io confirms `github_username_matches: true`
type: builder
verdict: MEETS
track_record:
- crate-dependents: sole owner of `pgpq` crate, 1 real reverse dependent — https://crates.io/api/v1/crates/pgpq/reverse_dependencies (checked 2026-09-28)
- production: maintainer-level contributor across arrow-rs/datafusion Rust codebases (also known as Pydantic's maintainer, cross-project) — https://github.com/adriangb (checked 2026-09-28)
influence:
- pgpq: 283 GitHub stars — https://github.com/adriangb/pgpq (checked 2026-09-28)
checked: role, book/course/talk/post — not pursued once crate-dependents confirmed MEETS.

## afetisov
name: Anton Fetisov
identity: https://internals.rust-lang.org/u/afetisov (Discourse profile gives real name "Anton Fetisov", trust_level 2) and https://github.com/afetisov (name "Anton") — same handle, consistent identity across both platforms
type: unset
verdict: FAILS
track_record:
- (none found)
influence:
- (none found)
checked: crate-dependents (GitHub has 10 repos, all forks/0 stars, no crates.io account under this login — https://crates.io/api/v1/users/afetisov returned Not Found, checked 2026-09-28), production (no employer/production post found), role (not listed on any rust-lang team), book/course/talk/post (forum posts only, no talks/books/widely-linked posts found) — all four kinds checked, none holds.

## ajdecon
name: Adam DeConinck
identity: https://github.com/ajdecon (name "Adam DeConinck", company IonQ, blog ajdecon.org)
type: unset
verdict: FAILS
track_record:
- (none found)
influence:
- (none found)
checked: crate-dependents (one 1-star tutorial repo `rust-embedded-discovery`, no crates.io account found — https://crates.io/api/v1/users/ajdecon returned Not Found, checked 2026-09-28), production (no Rust-in-production evidence found for IonQ or elsewhere), role (none), book/course/talk/post (personal blog ajdecon.org shows no Rust-specific published content found) — all four kinds checked, none holds.

## alamb
name: Andrew Lamb
identity: https://github.com/alamb — bio: "Staff Engineer at @influxdata, @apache {Arrow, DataFusion, Parquet} PMC, ASF Member"
type: institution
verdict: MEETS
track_record:
- role: Apache Software Foundation member and PMC member for Arrow, DataFusion, Parquet — https://github.com/alamb (checked 2026-09-28)
- production: Staff Engineer at InfluxData building on these Rust projects — https://github.com/alamb (checked 2026-09-28)
influence:
- DataFusion has 424 real crates.io reverse dependents — https://crates.io/api/v1/crates/datafusion/reverse_dependencies (2026-09-28)
checked: crate-dependents (personal), book/course/talk/post — not pursued once role+production confirmed MEETS.

## alandekok
name: Alan DeKok
identity: https://github.com/alandekok — bio/company "FreeRADIUS", well-documented FreeRADIUS project lead
type: unset
verdict: FAILS
track_record:
- (none found)
influence:
- (none found)
checked: crate-dependents (0 Rust repos on GitHub — https://github.com/alandekok?tab=repositories, checked 2026-09-28), production (FreeRADIUS is a C project; no Rust-in-production evidence found), role (0 contributions to rust-lang/rust — https://github.com/search, checked 2026-09-28), book/course/talk/post (none found) — all four kinds checked, none holds. His claim is a critique of "replace C with Rust" framing from outside Rust practice.

## alejandra-gonz-lez
name: Alejandra González
identity: https://github.com/blyxyas — bio: "Clippy team member @rust-lang", blog goose.love matches the claim's source domain
type: builder
verdict: MEETS
track_record:
- role: Clippy team member at rust-lang — https://github.com/blyxyas (checked 2026-09-28)
- post: authored the incremental-compilation performance blog post cited as source — https://blog.goose.love/posts/improving-the-incremental-system-in-the-rust-compiler (2025-11-04)
influence:
- Clippy has 305 real crates.io reverse dependents — https://crates.io/api/v1/crates/clippy/reverse_dependencies (2026-09-28)
checked: crate-dependents (personal), production — not pursued once role confirmed MEETS.

## alejandra-gonz-lez-blyxyas
name: Alejandra González (@blyxyas)
identity: https://github.com/blyxyas — same person as `alejandra-gonz-lez`; this id's source is her bio in the Rust blog's Maintainers-in-Residence announcement
type: builder
verdict: MEETS
track_record:
- role: named a Rust Foundation "Maintainer in Residence" — https://blog.rust-lang.org/2026/08/26/announcing-our-first-maintainers-in-residence (2026-08-26)
- role: Clippy team member at rust-lang — https://github.com/blyxyas (checked 2026-09-28)
influence:
- Clippy has 305 real crates.io reverse dependents — https://crates.io/api/v1/crates/clippy/reverse_dependencies (2026-09-28)
checked: crate-dependents (personal), production — not pursued once role confirmed MEETS.

## aleksandr-petrosyan
name: Aleksandr Petrosyan
identity: EuroRust 2023 speaker listing (video metadata confirms talk title "Reinforcement learning as a testing methodology - Aleksandr Petrosyan - EuroRust 2023") — https://youtube.com/watch?v=LO7tvIed-YQ
type: builder
verdict: MEETS
track_record:
- talk: spoke at EuroRust 2023, a major European Rust conference — https://youtube.com/watch?v=LO7tvIed-YQ (2023-11-15)
influence:
- EuroRust 2023 conference talk slot — https://youtube.com/watch?v=LO7tvIed-YQ (2023-11-15)
checked: crate-dependents, production, role — not pursued once talk confirmed MEETS.

## alex-crichton
name: Alex Crichton
identity: byline "Alex Crichton" on bytecodealliance.org articles about Wasmtime, tied to https://github.com/alexcrichton by matching name, employer (Bytecode Alliance/Wasmtime) and subject matter
type: language-designer
verdict: MEETS
track_record:
- role: 2,149 merged/authored PRs against rust-lang/rust — https://api.github.com/search/issues?q=repo:rust-lang/rust+author:alexcrichton+type:pr+is:merged (checked 2026-09-28)
- post: authored the Wasmtime LTS release policy article cited as source — https://bytecodealliance.org/articles/wasmtime-lts (2025-04-22)
influence:
- Wasmtime has 803 real crates.io reverse dependents — https://crates.io/api/v1/crates/wasmtime/reverse_dependencies (2026-09-28)
- 2,149 contributions to the Rust compiler itself — https://github.com/rust-lang/rust/pulls?q=author%3Aalexcrichton (checked 2026-09-28)
checked: crate-dependents (personal) — not pursued once role confirmed MEETS overwhelmingly.

## alexcrichton
name: Alex Crichton
identity: https://github.com/alexcrichton (email alex@alexcrichton.com, 5,473 followers) — same person as `alex-crichton`
type: language-designer
verdict: MEETS
track_record:
- role: 2,149 merged/authored PRs against rust-lang/rust, historically Cargo team lead and wasm-bindgen creator — https://api.github.com/search/issues?q=repo:rust-lang/rust+author:alexcrichton+type:pr+is:merged (checked 2026-09-28)
- production: active reviewer on bytecodealliance/wasmtime (9 claims logged, PRs #5079, #2033, #3186, #5000, #4721) — https://github.com/bytecodealliance/wasmtime/pull/14294 (2026-09-09)
influence:
- 5,473 GitHub followers — https://github.com/alexcrichton (checked 2026-09-28)
- Wasmtime has 803 real crates.io reverse dependents — https://crates.io/api/v1/crates/wasmtime/reverse_dependencies (2026-09-28)
checked: crate-dependents (personal), book/course/talk/post — not pursued once role confirmed MEETS.

## alice-i-cecile
name: Alice Cecile
identity: https://github.com/alice-i-cecile — bio: "Building Bevy", company "Bevy Foundation"
type: builder
verdict: MEETS
track_record:
- role: lead maintainer, Bevy Foundation — https://github.com/alice-i-cecile (checked 2026-09-28)
influence:
- Bevy has 2,045 real crates.io reverse dependents — https://crates.io/api/v1/crates/bevy/reverse_dependencies (2026-09-28)
- 1,015 GitHub followers — https://github.com/alice-i-cecile (checked 2026-09-28)
checked: crate-dependents (personal), production, book/course/talk/post — not pursued once role confirmed MEETS.

## alonely0
name: Guillem L. Jara
identity: https://github.com/Alonely0 — bio matches blog domain alonely0.github.io (claim source)
type: unset
verdict: FAILS
track_record:
- (none found)
influence:
- (none found)
checked: crate-dependents (crates `voila` and `lariv` both have 0 real reverse dependents — https://crates.io/api/v1/crates/voila/reverse_dependencies and https://crates.io/api/v1/crates/lariv/reverse_dependencies, checked 2026-09-28), production (no employer/production evidence found), role (none), book/course/talk/post (the cited blog post reached Hacker News but with only 1 point, below the ≥100-point bar — https://hn.algolia.com/api/v1/search?query=alonely0, checked 2026-09-28; no Lobsters/TWiR link found) — all four kinds checked, none holds at the required bar.

## amos-fasterthanlime
name: Amos Wenger
identity: https://github.com/fasterthanlime (crates.io confirms `github_username_matches: true`) and https://fasterthanli.me
type: educator
verdict: MEETS
track_record:
- post/talk: long-running Rust blog/video series at fasterthanli.me, explicitly named in gym's own ground-truth doc as a current affinity of the project's owner — https://fasterthanli.me (checked 2026-09-28)
influence:
- multiple GitHub repos with hundreds of stars (jsmad 757, mevi 736) — https://github.com/fasterthanlime (checked 2026-09-28)
checked: crate-dependents, production, role — not pursued once educator track record confirmed MEETS.

## andrei-alexandrescu-creator-of-d
name: Andrei Alexandrescu
identity: https://github.com/andralex — bio: "Researcher, software engineer, and author", company @NVIDIA; well-documented creator of the D language and author of "Modern C++ Design"
type: unset
verdict: FAILS
track_record:
- (none found)
influence:
- (none found)
checked: crate-dependents (0 Rust repositories on GitHub — https://github.com/andralex?tab=repositories, checked 2026-09-28), production (NVIDIA role is not Rust-specific), role (no rust-lang team or foundation membership found), book/course/talk/post (no Rust book/course/talk found; the cited quote is a TWiR repost of an outside-perspective Reddit comment about Rust's design, not authored Rust content) — all four kinds checked, none holds. Matches the claim's own logged gap: "no confirmed Rust track record."

## andrew-jakubowicz
name: Andrew Jakubowicz
identity: https://github.com/AndrewJakubowicz (blog andrewjakubowicz.me) and https://github.com/ajakubowicz-canva (bio links back to the personal account), confirming the Canva affiliation independently
type: builder
verdict: MEETS
track_record:
- production: built Rust/Wasm work at Canva (ajakubowicz-canva GitHub account) — https://github.com/ajakubowicz-canva (checked 2026-09-28)
- talk: co-presented "Debunking Rust Wasm Performance Myths" at RustWeek — https://youtube.com/watch?v=wDoqQkEylY8 (2026, RustWeek; oembed title confirms "at RustWeek")
influence:
- RustWeek conference talk slot, published by the RustNL channel — https://youtube.com/watch?v=wDoqQkEylY8 (2026-06-11 per claim date)
checked: crate-dependents, role — not pursued once production+talk confirmed MEETS.

## andrew-jakubowicz-and-co-presenter-canva
name: Andrew Jakubowicz and co-presenter Taj Pereira (Canva)
identity: same RustWeek talk as `andrew-jakubowicz`; oembed title confirms "Debunking Rust Wasm Performance Myths (Andrew Jakubowicz & Taj Pereira at RustWeek)" — https://youtube.com/watch?v=wDoqQkEylY8
type: builder
verdict: MEETS
track_record:
- talk: co-presented at RustWeek — https://youtube.com/watch?v=wDoqQkEylY8 (2026-06-11)
- production: Canva affiliation confirmed via Andrew Jakubowicz's Canva GitHub account — https://github.com/ajakubowicz-canva (checked 2026-09-28)
influence:
- RustWeek conference talk slot — https://youtube.com/watch?v=wDoqQkEylY8 (2026-06-11 per claim date)
checked: crate-dependents, role — not pursued once production+talk confirmed MEETS. Co-presenter Taj Pereira's own identity was not independently tied beyond the shared talk credit.

## andrews05
name: andrews05 (real name not disclosed on GitHub)
identity: https://github.com/andrews05 — crates.io co-owner record and GitHub org membership independently confirm the same account controls oxipng
type: builder
verdict: MEETS
track_record:
- crate-dependents: co-owner of `oxipng` on crates.io (alongside shssoichiro, AlexTMjugador), 70 real reverse dependents — https://crates.io/api/v1/crates/oxipng/reverse_dependencies and https://crates.io/api/v1/crates/oxipng/owners (checked 2026-09-28)
- role: member of the `oxipng` GitHub org — https://api.github.com/orgs/oxipng/members (checked 2026-09-28)
influence:
- oxipng repo has 4,240 GitHub stars — https://github.com/oxipng/oxipng (checked 2026-09-28)
- 127 authored PRs across Rust repositories on GitHub, the large majority to oxipng — https://api.github.com/search/issues?q=author:andrews05+type:pr+language:rust (checked 2026-09-28)
checked: production, book/course/talk/post — not pursued once crate-dependents confirmed MEETS. Real name not disclosed; identity tied via account control (crates.io ownership + org membership), not a legal-name profile.

## anthonygrondin
name: Anthony Grondin
identity: https://github.com/AnthonyGrondin — bio: "@Jafiot", blog anthony-grondin.ca
type: unset
verdict: FAILS
track_record:
- (none found)
influence:
- (none found)
checked: crate-dependents (no crates.io account found for this login — https://crates.io/api/v1/users/AnthonyGrondin returned Not Found, checked 2026-09-28; all embedded-Rust repos are forks), production (no evidence Jafiot ships Rust found), role (not a public member of the esp-rs org — https://api.github.com/orgs/esp-rs/public_members lists 7 members, this login absent, checked 2026-09-28), book/course/talk/post (none found) — all four kinds checked, none holds, despite 16 merged PRs to esp-hal and 4 to embassy showing real contribution activity that falls short of the bar's specific kinds.

## anthonytorlucci
name: Anthony Torlucci
identity: https://github.com/anthonytorlucci — crates.io confirms `github_username_matches: true`
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns the `rlevo` crate family; `rlevo-core` has 6 real reverse dependents — https://crates.io/api/v1/crates/rlevo-core/reverse_dependencies (checked 2026-09-28)
influence:
- `rlevo` (12 GitHub stars) — https://github.com/anthonytorlucci/rlevo (checked 2026-09-28)
- 3 authored PRs against tracel-ai/burn — https://api.github.com/search/issues?q=repo:tracel-ai/burn+author:anthonytorlucci+type:pr (checked 2026-09-28)
checked: production, role, book/course/talk/post — not pursued once crate-dependents confirmed MEETS.

## antimora
name: Dilshod Tadjibaev
identity: https://github.com/antimora — bio: "Working on Speech Recognition and Burn (Deep Learning Framework in Rust)"
type: builder
verdict: MEETS
track_record:
- production: core contributor building Burn, a Rust deep-learning framework, in production use — https://github.com/antimora (checked 2026-09-28)
influence:
- Burn has 324 real crates.io reverse dependents — https://crates.io/api/v1/crates/burn/reverse_dependencies (2026-09-28)
- 174 GitHub followers — https://github.com/antimora (checked 2026-09-28)
checked: crate-dependents (personal), role, book/course/talk/post — not pursued once production confirmed MEETS.
