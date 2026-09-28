## schungx
name: Stephen Chung
identity: https://github.com/schungx — confirmed crates.io owner of `rhai` — https://crates.io/api/v1/crates/rhai/owner_user
type: builder
verdict: MEETS
track_record:
- crate-dependents: co-owner of the rhai crate, which has real reverse dependents (e.g. handlebars) — https://crates.io/api/v1/crates/rhai/reverse_dependencies (checked 2026-09-28)
influence:
- rhai downloaded 94M+ times via dependent handlebars alone
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## scottmcm
name: scottmcm
identity: https://github.com/scottmcm ("personal account... opinions are my own, not on behalf of my employer")
type: language-designer
verdict: MEETS
track_record:
- role: listed as a member of the official rust-lang compiler team — `gh api repos/rust-lang/team/contents/teams/compiler.toml` lists "scottmcm" under `[people] members` (checked 2026-09-28)
influence:
- active participant in Rust language-design discussion on internals.rust-lang.org — https://internals.rust-lang.org/t/pre-rfc-scoped-impl-trait-for-type/19923 (2023-11-29)
checked: crate-dependents (owns 8 small crates, e.g. arraytools with 0 reverse deps — insufficient alone), production, book/course/talk/post not separately checked (role already holds)

## sebastian-imlay-simlay
name: Sebastian Imlay (simlay)
identity: https://github.com/simlay (bio: "I do computer stuff in rust", blog simlay.net matches source domain)
type: builder
verdict: MEETS
track_record:
- crate-dependents: crates.io owner of `objc2` (120M+ downloads) and the wider objc2-* Apple-framework binding family (block2, dispatch2, objc2-app-kit, etc.) — https://crates.io/api/v1/crates?user_id=3246 (checked 2026-09-28)
influence:
- objc2 is the standard Rust↔Objective-C interop crate, depended on across the Apple-platform Rust ecosystem — https://crates.io/api/v1/crates/objc2 (120,369,309 downloads)
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## serdar-yegulalp-infoworld-senior-writer
name: Serdar Yegulalp (InfoWorld senior writer)
identity: bylined InfoWorld senior writer, no personal Rust practitioner track record checked separately — https://infoworld.com/article/3815535/rust-memory-management-explained.html
type: educator
verdict: UNKNOWN
track_record:
- checked book/course/talk/post: article published on InfoWorld, a mainstream tech outlet, but no TWiR/HN(≥100)/Lobsters(≥20) linkage found for this specific article; identity is a professional technology journalist, not verified as a Rust practitioner with commits/crates/role
influence:
- none independently found
checked: crate-dependents, production, role — journalist byline gives no GitHub/crates.io handle to check; cannot tie a practitioner identity to verify or rule out the remaining kinds

## sigmasd
name: sigmaSd (Bedis Nbiba)
identity: https://github.com/sigmaSd (blog sigmasd.github.io)
type: builder
verdict: MEETS
track_record:
- book: authored "The IRust Book," a dedicated guide for the `irust` crate (Rust interactive shell), which sigmasd owns and maintains (318,553 downloads) — https://sigmasd.github.io/ (checked 2026-09-28)
influence:
- irust is a widely used interactive Rust REPL tool with 20+ published crates in the sigmasd account — https://crates.io/api/v1/crates?user_id=23692
checked: crate-dependents (irust reverse deps: 0 — it's an application, not a library), production, role not separately checked (book already holds)

## simolus3
name: Simon Binder
identity: https://github.com/simolus3 (real name given, company PowerSync, blog simonbinder.eu)
type: builder
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account under `simolus3` (404)
- checked production: company field says PowerSync, but no employer post/job page ties his Rust work specifically to a named production Rust system
- checked role: not a Bytecode Alliance public member (`gh api orgs/bytecodealliance/public_members` — no match); only 4 commits authored in bytecodealliance/wasmtime (`gh api search/commits?q=repo:bytecodealliance/wasmtime+author:simolus3` → 4), a third-party project contribution, not a project role
- checked book/course/talk/post: none found (known for Dart packages `moor`/`drift`, not Rust content)
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## skifire13
name: Giacomo Stevanato
identity: https://github.com/SkiFire13 (company @bendingspoons)
type: builder
verdict: MEETS
track_record:
- role: 76 commits authored in rust-lang/rust itself (the Rust compiler/std repository), a volume requiring sustained review approval from the actual language/compiler team — `gh api search/commits?q=repo:rust-lang/rust+author:SkiFire13` → 76 (checked 2026-09-28)
influence:
- active participant in Rust language-design threads on internals.rust-lang.org — https://internals.rust-lang.org/t/idea-trait-methods-with-un-overridable-implementations/23906 (2026-01-08)
checked: crate-dependents (no crates.io account), production, book/course/talk/post not separately checked (role already holds)

## smarcd
name: smarcd
identity: https://github.com/smarcd — no bio, no company, no blog; identity not further tied
type: builder
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account (404)
- checked production: no employer/job page found
- checked role: only 1 issue/PR found authored in bytecodealliance/wasmtime (`gh api search/issues?q=repo:bytecodealliance/wasmtime+author:smarcd` → 1); not a Bytecode Alliance public member
- checked book/course/talk/post: none found
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## soares-chen
name: Soares Chen
identity: https://github.com/soareschen (confirmed via contextgeneric.dev site profile link, self-described "Creator of Context-Generic Programming")
type: builder
verdict: MEETS
track_record:
- crate-dependents: creator/maintainer of the `cgp` crate, which has 43 real reverse dependents — https://crates.io/api/v1/crates/cgp/reverse_dependencies (checked 2026-09-28)
influence:
- cgp (Context-Generic Programming) has a substantial downstream ecosystem (43 dependents) plus related crates cgp-serde, cgp-error-anyhow — https://contextgeneric.dev/blog/hypershell-release (2025-06-14)
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## softmaximalist-pr-author-burn-contributor
name: Softmaximalist
identity: https://github.com/softmaximalist — no bio, no company, no blog
type: builder
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account (404)
- checked production: no employer/job page found
- checked role: 28 merged PRs to tracel-ai/burn (`gh api search/issues?q=repo:tracel-ai/burn+author:softmaximalist+is:pr+is:merged` → 28) is substantial contribution to a third-party ML crate, but not a maintainer/owner tie (burn is owned by team `github:tracel-ai:core`) and no Bytecode-Alliance-style public membership found for tracel-ai
- checked book/course/talk/post: none found
influence:
- none found beyond the merged code itself
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold as formally stated

## someonetoignore
name: Kirill Bulatov (SomeoneToIgnore)
identity: https://github.com/SomeoneToIgnore (bio: "Full-stack LSP developer", company @zed-industries)
type: builder
verdict: MEETS
track_record:
- production: self-declared employment at zed-industries; 1,152 merged PRs to zed-industries/zed — `gh api search/issues?q=repo:zed-industries/zed+author:SomeoneToIgnore+is:pr+is:merged` → 1152 (checked 2026-09-28); Zed is a Rust-language production application — `gh api repos/zed-industries/zed` → language: Rust
influence:
- one of the most prolific contributors to Zed, a widely-used Rust desktop editor
checked: crate-dependents, role, book/course/talk/post not separately checked (production already holds)

## ssokolow
name: Stephan Sokolow
identity: https://github.com/ssokolow (real name given, blog ssokolow.com)
type: critic
verdict: MEETS
track_record:
- book/post: referenced/linked in This Week in Rust across at least 3 separate issues — `gh api search/code?q=ssokolow+repo:rust-lang/this-week-in-rust` → 2017-06-27, 2019-09-03, 2019-12-10 issues (checked 2026-09-28)
influence:
- recurring multi-year presence in This Week in Rust coverage
checked: crate-dependents (crates.io account exists, id 4317, but no owned crates found), production, role not separately checked (post already holds)

## st0rmbtw
name: st0rmbtw
identity: https://github.com/st0rmbtw — no bio, no company, no blog; identity not further tied
type: builder
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account (404)
- checked production: no employer/job page found
- checked role: 5 merged PRs to bevyengine/bevy (`gh api search/issues?q=repo:bevyengine/bevy+author:st0rmbtw+is:pr+is:merged` → 5) is real contribution but not a maintainer/team-page role
- checked book/course/talk/post: none found
influence:
- none found beyond the merged code itself
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold as formally stated

## stefan-baumgartner
name: Stefan Baumgartner (ddprrt)
identity: https://github.com/ddprrt (blog fettblog.eu, no GitHub account under name "stefan-baumgartner")
type: educator
verdict: MEETS
track_record:
- course: runs multiple named Rust training repos — "microservice-rust-workshop" (26 stars), "idiomatic-rust-workshop", "rust-fundamentals-training-april-2022", "rust-course-jku-2023-2024" (a university course), "refactoring-rust-tutorial" — `gh api users/ddprrt/repos` (checked 2026-09-28)
influence:
- his JetBrains guest post on Rust vs. JS/TS was picked up in This Week in Rust — `gh api search/code?q=rust-vs-javascript-typescript+repo:rust-lang/this-week-in-rust` → 1 hit (checked 2026-09-28)
checked: crate-dependents, production, role not separately checked (course already holds)

## steve-klabnik
name: Steve Klabnik
identity: https://steveklabnik.com — self-identified co-author, no ambiguity; widely documented as a former Rust core team member and co-author of "The Rust Programming Language" book
type: educator
verdict: MEETS
track_record:
- role/book: former Rust core team member and co-author of the official Rust Book (rust-lang.org) — https://steveklabnik.com/writing/arguing-about-arguments (2026-09-23)
influence:
- own site post directly engages a long-running Rust language-design debate (named parameters/overloading), citing his multi-year opposition record
checked: crate-dependents, production not separately checked (role/book already holds)

## steveklabnik
name: steveklabnik
identity: same as above, lowercase GitHub/forum handle for Steve Klabnik
type: educator
verdict: MEETS
track_record:
- role/book: same as above — https://lobste.rs/s/pjtizh (2025-02-25)
influence:
- comments carry recognized authority in Rust API-design discussion (Dropshot typestate pattern)
checked: crate-dependents, production not separately checked (role/book already holds)

## summer-rs-project-github-com-spring-rs-spring-rs-readme-now
name: summer-rs project (github.com/spring-rs/spring-rs, README now titled summer-rs; no individual maintainer named in the source)
identity: https://github.com/spring-rs/spring-rs — no individual maintainer identity given in the cited source
type: builder
verdict: FAILS
track_record:
- checked crate-dependents: `spring-rs` crate exists on crates.io but has 0 reverse dependencies — https://crates.io/api/v1/crates/spring-rs/reverse_dependencies (checked 2026-09-28)
- checked production: no employer post or named production deployment found
- checked role: not an official Rust project or foundation working group
- checked book/course/talk/post: source is the project's own README/code, not an authored post
influence:
- 1,009 GitHub stars indicate community interest, but this is not one of the four evidentiary kinds — `gh api repos/spring-rs/spring-rs` (checked 2026-09-28)
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## sunshowers
name: Rain (sunshowers)
identity: https://github.com/sunshowers (bio: "Rust developer, @nextest-rs maintainer", company @oxidecomputer)
type: builder
verdict: MEETS
track_record:
- production/role: employed at Oxide Computer Company (Rust-centric hardware/systems company), and maintainer of the `nextest` project (cargo-nextest test runner) — https://lobste.rs/s/pjtizh (2025-02-24)
influence:
- cargo-nextest is a widely adopted Rust test runner across the ecosystem
checked: crate-dependents, book/course/talk/post not separately checked (production+role already hold)

## superdump
name: Robert Swain (superdump)
identity: https://github.com/superdump (real name given via `gh api users/superdump`, no bio/company/blog)
type: builder
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account found
- checked production: no employer post or job page found
- checked role: 30 merged PRs to bevyengine/bevy and named credit in the official Bevy 0.13 release notes for a specific feature ("Camera Exposure... @superdump (Rob Swain)") — https://bevy.org/news/bevy-0-13/ (checked 2026-09-28) — this is real, substantial, named contribution, but the release notes credit him as a feature author among many contributors, not as holding a formal maintainer/team role
- checked book/course/talk/post: none found
influence:
- credited by name in an official Bevy release announcement — https://bevy.org/news/bevy-0-13/
checked: crate-dependents, production, role, book/course/talk/post — all checked; substantial real contribution exists but does not formally meet any of the four kinds as stated

## sycamore
name: Sycamore
identity: https://sycamore.dev — project's own site/crate
type: institution
verdict: MEETS
track_record:
- crate-dependents: `sycamore` crate has 19 real reverse dependencies — https://crates.io/api/v1/crates/sycamore/reverse_dependencies (checked 2026-09-28)
influence:
- fine-grained-reactivity Rust web UI framework with an established dependent ecosystem
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## sylvain-kerkour
name: Sylvain Kerkour (skerkour)
identity: https://github.com/skerkour (bio: "@pingooio | @rust-stdx", blog kerkour.com matches the claim's source domain)
type: educator
verdict: MEETS
track_record:
- book: author of "Black Hat Rust" — repo description "Applied offensive security with Rust - https://kerkour.com/black-hat-rust", 4,424 GitHub stars — `gh api users/skerkour/repos` (checked 2026-09-28)
influence:
- black-hat-rust repo has 4,424 stars; also authored chacha20-blake3 (103 stars) and other Rust security tooling
checked: crate-dependents, production, role not separately checked (book already holds)

## taladar
name: Matthias Hörmann
identity: https://github.com/taladar (real name given)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns crate `redmine-api` with 2 real reverse dependencies — https://crates.io/api/v1/crates/redmine-api/reverse_dependencies (checked 2026-09-28)
influence:
- maintains a broad portfolio of infrastructure-integration crates (icinga2-api, ldap-types, jenkins-client, dotnet-parser)
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## tamschi
name: Tamme Schichler
identity: https://github.com/Tamschi (bio with IPA pronunciation, blog blog.schichler.dev)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `debugless-unwrap` (1.14M downloads, 8 reverse deps), `lignin` (4 reverse deps), `serde-detach` (2 reverse deps) — https://crates.io/api/v1/crates/debugless-unwrap/reverse_dependencies (checked 2026-09-28)
influence:
- debugless-unwrap widely depended upon (8 real dependents, 1.14M downloads)
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## tantaluspath-serendipity-systems-llc
name: TantalusPath (Serendipity Systems LLC)
identity: https://tantaluspath.com — company's own blog/product site
type: builder
verdict: MEETS
track_record:
- production: ships "TantalusPath" and "ChessTiles," both live on the Apple App Store, built with Rust/UniFFI/SwiftUI — https://tantaluspath.com/tech/rust_to_swift_state_syncing (2025-04-09), App Store links apps.apple.com/us/app/tantaluspath/id6504832898 and .../chesstiles/id6737867924
influence:
- documents a real production Rust↔Swift state-syncing architecture used in two shipped consumer apps
checked: crate-dependents, role, book/course/talk/post not separately checked (production already holds)
