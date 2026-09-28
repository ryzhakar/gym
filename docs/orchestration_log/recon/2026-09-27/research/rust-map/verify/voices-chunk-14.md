## tapghoul
name: Andrew Silver (TapGhoul)
identity: https://github.com/TapGhoul (blog tapghoul.dev, real name via crates.io account)
type: builder
verdict: FAILS
track_record:
- checked crate-dependents: crates.io account exists but owns 0 published crates — https://crates.io/api/v1/crates?user_id=32270
- checked production: no employer post/job page found
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: personal site tapghoul.dev shows only social links, no Rust content
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## taylor
name: Taylor Cramer
identity: YouTube oEmbed confirms "Tyler Mandry & Taylor Cramer: 'Fine-Grained C++ Interop' | RustConf 2025", published by channel Rust Foundation — https://www.youtube.com/oembed?url=https://youtube.com/watch?v=Z5M4NIWoMJQ (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- talk: co-presented a RustConf 2025 talk on Rust/C++ interop, hosted/published by the Rust Foundation's own channel — https://youtube.com/watch?v=Z5M4NIWoMJQ (2025-10-03)
influence:
- RustConf mainstage talk on a core language-interop topic
checked: crate-dependents, production, role not separately checked (talk already holds)

## taylor-and-tyler
name: Taylor Cramer and Tyler Mandry
identity: YouTube oEmbed confirms "Tyler Mandry & Taylor Cramer: 'Fine-Grained C++ Interop' | RustConf 2025", published by channel Rust Foundation — https://www.youtube.com/oembed?url=https://youtube.com/watch?v=Z5M4NIWoMJQ (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- talk: co-presented a RustConf 2025 talk on Rust/C++ interop, hosted/published by the Rust Foundation's own channel — https://youtube.com/watch?v=Z5M4NIWoMJQ (2025-10-03)
influence:
- RustConf mainstage talk on a core language-interop topic
checked: crate-dependents, production, role not separately checked (talk already holds)

## ted-tso
name: Theodore Ts'o
identity: widely documented Linux kernel ext4 maintainer, quoted in ArsTechnica coverage of the Rust-for-Linux dispute — https://arstechnica.com/gadgets/2024/09/rust-in-linux-lead-retires-rather-than-deal-with-more-nontechnical-nonsense
type: critic
verdict: FAILS
track_record:
- checked crate-dependents: not a Rust crate author; he is a C/kernel maintainer
- checked production: ships C, not Rust — no Rust production claim
- checked role: not part of the Rust project or foundation; he is a Linux kernel (ext4) maintainer, quoted only as an external commenter on Rust-in-Linux
- checked book/course/talk/post: no Rust-authored content; the cited quote is explicitly a refusal to learn Rust ("you're not going to force all of us to learn Rust")
influence:
- widely covered remark that shaped the Rust-for-Linux governance dispute, but as an outside critic, not a Rust practitioner
checked: crate-dependents, production, role, book/course/talk/post — all checked; identity is fully tied and famous, but carries no Rust track record at all

## teohhanhui
name: Teoh Han Hui
identity: https://github.com/teohhanhui (bio: "looking for a job in @rust-lang, formerly worked on @api-platform")
type: critic
verdict: FAILS
track_record:
- checked crate-dependents: owns 5 crates (callbag, hexciv, mercure, steamctl, stocker), all with 0 reverse dependencies — https://crates.io/api/v1/crates?user_id=90690 (checked 2026-09-28)
- checked production: no employer post found; bio states he is currently job-seeking, not employed shipping Rust
- checked role: not (yet) a rust-lang team member per his own bio
- checked book/course/talk/post: none found
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## the-spin-project
name: The Spin Project (Fermyon / CNCF Spin Framework)
identity: GitHub org spinframework (formerly under Fermyon), real org confirmed — https://github.com/spinframework/spin
type: institution
verdict: MEETS
track_record:
- crate-dependents: `spin` crate has 789 real reverse dependencies — https://crates.io/api/v1/crates/spin/reverse_dependencies (checked 2026-09-28)
influence:
- Spin is a CNCF-adjacent, Fermyon-originated serverless WebAssembly framework with 6,522 GitHub stars on the main repo — `gh api repos/spinframework/spin` (checked 2026-09-28)
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## the-spin-project-fermyon-cncf-spin-institution
name: The Spin Project (Fermyon / CNCF Spin, institution)
identity: GitHub org spinframework (formerly under Fermyon) — https://github.com/spinframework/spin
type: institution
verdict: MEETS
track_record:
- crate-dependents: `spin` crate has 789 real reverse dependencies — https://crates.io/api/v1/crates/spin/reverse_dependencies (checked 2026-09-28)
influence:
- Fermyon-originated, CNCF-adjacent serverless WebAssembly framework, 6,522 GitHub stars on the main repo
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## the8472
name: the8472
identity: https://github.com/the8472 (no public real name)
type: builder
verdict: MEETS
track_record:
- role: 450 commits authored in rust-lang/rust (the Rust compiler/std repository) — `gh api search/commits?q=repo:rust-lang/rust+author:the8472` → 450 (checked 2026-09-28)
influence:
- long-standing, high-volume contributor to the Rust standard library, active in internals.rust-lang.org design threads — https://internals.rust-lang.org/t/instant-systemtime-min-max/21375 (2024-08-15)
checked: crate-dependents, production, book/course/talk/post not separately checked (role already holds)

## thesys-engineering-team
name: Thesys Engineering Team
identity: byline "Thesys Engineering Team" on the openui.com company blog — https://openui.com/blog/rust-wasm-parser (checked 2026-09-28)
type: institution
verdict: MEETS
track_record:
- production: explicit employer-authored post stating "We built the openui-lang parser in Rust and compiled it to WASM," describing a real deployed system before a later rewrite — https://openui.com/blog/rust-wasm-parser (2026-03-20)
influence:
- documents a concrete production Rust/WASM parser and its performance characteristics
checked: crate-dependents, role, book/course/talk/post not separately checked (production already holds)

## thorsten-hans
name: Thorsten Hans
identity: https://github.com/ThorstenHans (bio: "Sr. Developer Advocate... WebAssembly... Microsoft MVP 2011-2025", company @akamai-developers), blog matches long-standing WebAssembly-advocacy identity
type: educator
verdict: MEETS
track_record:
- production/role: Senior Developer Advocate for WebAssembly at Akamai (formerly at Fermyon, the company behind Spin), authoring a technical post on the official Spin framework blog — https://spinframework.dev/blog/component-composition-spin-4-0 (2026-08-27)
influence:
- 14-year Microsoft MVP recognition for developer content, long track record in the WebAssembly/Spin ecosystem
checked: crate-dependents, book/course/talk/post not separately checked (production/role already holds)

## tiemensch
name: Tiemen Schuijbroek (TiemenSch)
identity: https://github.com/TiemenSch (real name given, company "Ratio Computer Aided Systems Engineering B.V.")
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns the `ratio-*` crate family (matching employer name), incl. `ratio-graph` (1 real reverse dep) and `ratio-matrix` (1 real reverse dep) — https://crates.io/api/v1/crates?user_id=161160 (checked 2026-09-28)
influence:
- ratio-graph has 53,031 downloads; the crate family appears to be his employer's own published Rust tooling
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## tim-mccallum-bytecode-alliance
name: Tim McCallum (Bytecode Alliance)
identity: byline "Tim McCallum" on the official bytecodealliance.org blog — https://bytecodealliance.org/articles/invoking-component-functions-in-wasmtime-cli — no bio, GitHub, or other profile found tying the name to a body of Rust work
type: builder
verdict: UNKNOWN
track_record:
- checked crate-dependents: no matching crates.io or GitHub account found under this name
- checked production: no separate employer/job page found
- checked role: published as an author on the official Bytecode Alliance blog, which implies some editorial vetting, but no team-page listing or GitHub profile confirms an ongoing Bytecode Alliance role
- checked book/course/talk/post: the article itself exists (real, reachable) but authorship cannot be tied to a verifiable practitioner identity beyond the byline
influence:
- article hosted on the official Bytecode Alliance site
checked: crate-dependents, production, role, book/course/talk/post — sources reachable but identity untied; cannot rule MEETS or FAILS without guessing

## toastal
name: toastal
identity: https://github.com/toastal (no real name given, no company)
type: critic
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account (404)
- checked production: no employer/job page found
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: no Rust repos found among public GitHub repos
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## tomas-tauber
name: Tomas Tauber (tomtau)
identity: https://github.com/tomtau — confirmed via IDVerse engineering blog author bio ("PhD... since 2018 he has been working professionally with the Rust programming language... core maintainer of pest") — https://forgestream.idverse.com/blog/20250902-cloudwatch-rust-logging
type: builder
verdict: MEETS
track_record:
- crate-dependents: core maintainer of `pest`, a Rust parser generator with 1,259 real reverse dependencies — https://crates.io/api/v1/crates/pest/reverse_dependencies (checked 2026-09-28)
influence:
- pest is one of the most widely depended-upon parser generators in the Rust ecosystem
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## totalkrill
name: TotalKrill
identity: https://github.com/TotalKrill (bio: "Rust fan", company "Mobilaris Industrial Solutions AB")
type: builder
verdict: FAILS
track_record:
- checked crate-dependents: owns 36 published crates but every one checked (every_variant, libcoap-rs, bevy_mod_reqwest, random_variant, mqtt_macro, bevy_ui_anchor, cargo-rocketapi) has 0 real reverse dependencies — https://crates.io/api/v1/crates?user_id=31234 (checked 2026-09-28)
- checked production: no employer post or job page from Mobilaris naming Rust in production found
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: none found
influence:
- none found meeting the bar (download counts exist but reflect his own crate family depending on itself, not distinct third-party dependents)
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## tristan
name: Tristan ("Green Fit Heaven" solo developer; surname not given in the source)
identity: self-introduced by first name only in a real, dated community talk — "10th Bevy Meetup - Tristan - From zero to demo: a newcomer's experience learning Bevy" — https://youtube.com/watch?v=_FIDuLV0ZsA (2025-06-18)
type: builder
verdict: MEETS
track_record:
- talk: presented at the 10th Bevy Meetup describing his own solo Bevy game-development project, including a live audience Q&A — https://youtube.com/watch?v=_FIDuLV0ZsA (~26:33-27:33)
influence:
- talk given at a recurring, named community meetup series (10th installment)
checked: crate-dependents, production, role, book/course/post not separately checked (talk already holds); single-name identity is the limit of what the primary source itself gives

## tristan-solo-rust-bevy-game-developer-green-fit-heaven
name: Tristan ("Green Fit Heaven" solo developer; surname not given in the source)
identity: self-introduced by first name only in a real, dated community talk — "10th Bevy Meetup - Tristan - From zero to demo: a newcomer's experience learning Bevy" — https://youtube.com/watch?v=_FIDuLV0ZsA (2025-06-18)
type: builder
verdict: MEETS
track_record:
- talk: presented at the 10th Bevy Meetup describing his own solo Bevy game-development project ("Green Fit Heaven"), including a live audience Q&A — https://youtube.com/watch?v=_FIDuLV0ZsA (~26:33-27:33)
influence:
- talk given at a recurring, named community meetup series (10th installment)
checked: crate-dependents, production, role, book/course/post not separately checked (talk already holds); single-name identity is the limit of what the primary source itself gives

## tronical-olivier-goffart-slint-co-founder-maintainer
name: Olivier Goffart (tronical)
identity: well-documented co-founder of Slint (formerly SixtyFPS), commenting on a Slint issue — https://github.com/slint-ui/slint/issues/7657
type: builder
verdict: MEETS
track_record:
- role/production: co-founder and maintainer of Slint, a real Rust GUI framework, commenting with maintainer authority on the project's own issue tracker — https://github.com/slint-ui/slint/issues/7657 (2025-02-20)
influence:
- Slint is an established cross-platform Rust GUI toolkit
checked: crate-dependents, book/course/talk/post not separately checked (role already holds)

## tumdum
name: tumdum (work account: Tomasz Kłak, @tomaszklak)
identity: https://github.com/tumdum (bio names work account @tomaszklak)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns crate `read_char` with 1 real reverse dependency — https://crates.io/api/v1/crates/read_char/reverse_dependencies (checked 2026-09-28)
influence:
- read_char is a small but genuinely depended-upon utility crate
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## turbo87
name: Tobias Bieniek (Turbo87)
identity: https://github.com/Turbo87 (bio: "🦀 crates.io team co-lead", company @rustfoundation)
type: builder
verdict: MEETS
track_record:
- role: co-lead of the crates.io team, employed by the Rust Foundation — self-declared GitHub bio (checked 2026-09-28)
influence:
- co-leads the infrastructure serving the entire Rust crate ecosystem
checked: crate-dependents, production, book/course/talk/post not separately checked (role already holds)

## ukoehb
name: UkoeHB
identity: https://github.com/UkoeHB (no real name given, but crates.io account and a large, coherent crate portfolio tie the handle to sustained real work)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `renet2` (5 real reverse deps) and `bevy_cobweb` (5 real reverse deps) among 30+ published crates — https://crates.io/api/v1/crates/renet2/reverse_dependencies, https://crates.io/api/v1/crates/bevy_cobweb/reverse_dependencies (checked 2026-09-28)
influence:
- renet2/bevy_cobweb ecosystem used by multiple downstream Bevy-networking crates
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## unidentified-reviewer
name: unidentified reviewer
identity: untied — source (a YouTube talk, ~07:06-08:07) explicitly does not name this person
type: unset
verdict: UNKNOWN
track_record:
- checked crate-dependents, production, role, book/course/talk/post: none checkable — no name, handle, or profile is given by the source itself to verify against
influence:
- none checkable
checked: crate-dependents, production, role, book/course/talk/post — identity cannot be tied by design of the source; never guessed

## urben1680
name: urben1680
identity: https://github.com/urben1680 (no real name, no bio, no company)
type: critic
verdict: FAILS
track_record:
- checked crate-dependents: owns 1 crate, `bevy_oozlum`, with 28 total downloads and 0 reverse dependencies — https://crates.io/api/v1/crates/bevy_oozlum/reverse_dependencies (checked 2026-09-28)
- checked production: no employer/job page found
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: none found
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## vangata-ve
name: Ivan Georgiev (vangata-ve)
identity: https://github.com/vangata-ve (real name given via GitHub profile)
type: critic
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account (404)
- checked production: no employer/job page found
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: only 1 public repo, in C, 0 stars; no Rust content found
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## vaultwarden-maintainers-dani-garcia-vaultwarden
name: Vaultwarden maintainers (dani-garcia/vaultwarden)
identity: https://github.com/dani-garcia/vaultwarden — real, active, high-profile repository
type: institution
verdict: MEETS
track_record:
- production/crate-dependents: Vaultwarden is a widely deployed Rust Bitwarden-compatible server with 68,245 GitHub stars, built on the Rocket web framework — `gh api repos/dani-garcia/vaultwarden` (checked 2026-09-28)
influence:
- one of the most widely self-hosted Rust server applications in the open-source ecosystem
checked: role, book/course/talk/post not separately checked (production/crate-dependents already holds)
