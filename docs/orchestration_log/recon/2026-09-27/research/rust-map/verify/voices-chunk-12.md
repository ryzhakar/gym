## ramfox-matheus23
name: ramfox, matheus23
identity: https://github.com/ramfox (bio: company n0.computer) | https://github.com/matheus23 (bio: Philipp Krüger, company @n0-computer)
type: builder
verdict: MEETS
track_record:
- production: iroh maintainers at n0.computer, authored 0.31.0 release/blog post — https://iroh.computer/blog/iroh-0-31-0-back-to-fighting-fit (2025-01-15)
influence:
- iroh (n0.computer) release notes read by iroh's dependent ecosystem — https://iroh.computer/blog/iroh-0-31-0-back-to-fighting-fit (2025-01-15)
checked: crate-dependents, role, book/course/talk/post not separately checked (production already holds)

## ramfox-matheus23-iroh-n0-blog-authors
name: ramfox, matheus23 (iroh / n0 blog authors)
identity: https://github.com/ramfox | https://github.com/matheus23 — same pair as above, explicit "iroh/n0 blog authors" tag
type: builder
verdict: MEETS
track_record:
- production: same iroh 0.31.0 blog post, n0.computer employees — https://iroh.computer/blog/iroh-0-31-0-back-to-fighting-fit (2025-01-15)
influence:
- iroh release blog, read by iroh integrators — https://iroh.computer/blog/iroh-0-31-0-back-to-fighting-fit (2025-01-15)
checked: crate-dependents, role, book/course/talk/post not separately checked (production already holds)

## renkenono
name: renken (bensaber.net; GitHub renkenono)
identity: https://bensaber.net (self-identifies "I'm Renken", links github.com/renkenono) — https://github.com/renkenono
type: builder
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account for renkenono (404) — https://crates.io/api/v1/users/renkenono
- checked production: no employer post or job page found; bensaber.net names Rust only as a personal interest, no production claim
- checked role: not listed on any Rust project/foundation team page; esp-hal owner team is `github:esp-rs:espressif`, renkenono not a member
- checked book/course/talk/post: none found
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — 8 merged bugfix PRs to esp-rs/esp-hal exist (https://github.com/esp-rs/esp-hal, search author:renkenono, 4 fix-titled + 4 more, total_count 4 via `is:pr`) but this is contributor activity, not a maintained crate, employer claim, team role, or authored content — none of the four kinds hold

## rhai-project-rhaiscript-maintainers
name: Rhai project (rhaiscript maintainers)
identity: crate owners sophiajt, luciusmagn, schungx — https://crates.io/api/v1/crates/rhai/owner_user
type: institution
verdict: MEETS
track_record:
- crate-dependents: rhai has real reverse dependents (e.g. handlebars 6.4.4) — https://crates.io/api/v1/crates/rhai/reverse_dependencies (checked 2026-09-28)
influence:
- rhai crate downloaded 94M+ times by dependent handlebars alone — https://crates.io/api/v1/crates/rhai/reverse_dependencies (checked 2026-09-28)
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## rklaehn
name: Rüdiger Klaehn
identity: https://github.com/rklaehn (bio "Old grumpy hacker", real name given)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns 30+ published crates incl. range-collections (6.9M downloads), inplace-vec-builder (7.4M downloads), quic-rpc, several iroh-* crates — https://crates.io/api/v1/crates?user_id=65577 (checked 2026-09-28)
- production: iroh-blobs 0.90 release notes, iroh maintainer — https://iroh.computer/blog/iroh-blobs-0-90-changes (2025-07-04)
influence:
- range-collections and inplace-vec-builder each downloaded millions of times by dependents — https://crates.io/api/v1/crates?user_id=65577 (checked 2026-09-28)
checked: role, book/course/talk/post not separately checked (crate-dependents already holds)

## romgrk
name: Rom Grk
identity: https://github.com/romgrk (bio: "C/C++, Rust, Typescript, vim & dharma", no employer given)
type: builder
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account (404) — https://crates.io/api/v1/users/romgrk
- checked production: 13 merged PRs to zed-industries/zed (`gh api search/issues?q=repo:zed-industries/zed+author:romgrk+is:pr+is:merged` → 13) is real contribution, but no employer post/job page/talk names romgrk as shipping Rust in production — GitHub bio shows no employer
- checked role: not a zed-industries org member signal (no company field); no Rust project/foundation team page listing
- checked book/course/talk/post: none found
influence:
- none found beyond the merged code contributions themselves
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold as stated (community PR contribution to a third-party project is not itself one of the four kinds)

## rossberg
name: Andreas Rossberg
identity: GitHub handle "rossberg", commenting as WebAssembly component-model spec participant — https://github.com/WebAssembly/component-model/issues/525
type: language-designer
verdict: MEETS
track_record:
- role: active designer on the WebAssembly component-model spec repo (WebAssembly CG), commenting with design authority on Wasm core semantics — https://github.com/WebAssembly/component-model/issues/525 (comments 2025-06-06, 2025-06-16)
influence:
- direct technical pushback shaping component-model ABI design discussion — https://github.com/WebAssembly/component-model/issues/525 (2025-06-16)
checked: crate-dependents, production, book/course/talk/post not separately checked (role already holds)

## rpjohnst
name: Russell Johnston
identity: https://github.com/rpjohnst (real name given, blog abubalay.com)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns crate `dioptre` with 1 real reverse dependency — https://crates.io/api/v1/crates/dioptre/reverse_dependencies (checked 2026-09-28)
influence:
- dioptre (struct field projection) has a downstream dependent — https://crates.io/api/v1/crates/dioptre/reverse_dependencies (checked 2026-09-28)
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## rreverser-wasm-bindgen-maintainer
name: Ingvar Stepanyan (RReverser)
identity: https://github.com/RReverser (bio: "WebAssembly consultant", company Cloudflare, blog rreverser.com)
type: builder
verdict: MEETS
track_record:
- role/production: wasm-bindgen maintainer commenting with merge authority on wasm-bindgen#4795, employed at Cloudflare as WebAssembly consultant — https://github.com/wasm-bindgen/wasm-bindgen/pull/4795 (2025-11-14)
influence:
- wasm-bindgen is the standard Rust↔JS/Wasm glue crate, massively depended upon — https://github.com/wasm-bindgen/wasm-bindgen/pull/4795 (2025-11-14)
checked: crate-dependents, book/course/talk/post not separately checked (role already holds)

## rtic-developers
name: RTIC developers
identity: crate owners korken89 (Emil Fresk), perlindgren, AfoHT (Henrik Tjäder); org team github:rtic-rs:devs — https://crates.io/api/v1/crates/rtic/owner_user, owner_team
type: institution
verdict: MEETS
track_record:
- crate-dependents: rtic crate has real reverse dependents (e.g. stm32f4xx-hal 0.23.0, 832K downloads) — https://crates.io/api/v1/crates/rtic/reverse_dependencies (checked 2026-09-28)
influence:
- RTIC book at rtic.rs, an established embedded Rust framework — https://rtic.rs/ (book)
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## rtic-developers-rtic-rs-maintainers
name: RTIC developers (rtic.rs maintainers)
identity: same as above — crate owners korken89, perlindgren, AfoHT; team github:rtic-rs:devs
type: institution
verdict: MEETS
track_record:
- crate-dependents: rtic crate real dependents confirmed — https://crates.io/api/v1/crates/rtic/reverse_dependencies (checked 2026-09-28)
influence:
- rtic.rs book, standard reference for interrupt-driven embedded Rust — https://rtic.rs/ (book)
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## rtic-project-rtic-rs-maintainers-unnamed-individually
name: RTIC project (rtic.rs maintainers, unnamed individually)
identity: rtic.rs book/site, maintained by crate-owner team above (individuals not separately named in this claim's source)
type: institution
verdict: MEETS
track_record:
- book: rtic.rs is a maintained project book documenting a real crate with real dependents — https://rtic.rs/ (checked via crates.io reverse_dependencies, 2026-09-28)
influence:
- reference documentation for the RTIC framework — https://rtic.rs/
checked: production, role not separately checked (book + crate-dependents already hold)

## rtpg
name: Raphael Gaschignard
identity: https://github.com/rtpg (bio: "Programmer (Mostly Python)", blog rtpg.co)
type: critic
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account (404) — https://crates.io/api/v1/users/rtpg
- checked production: no employer/job page naming Rust in production found
- checked role: not listed on any Rust project or foundation team page
- checked book/course/talk/post: no Rust repos of substance (only a fork of reedline, all owned repos are Python/JS/other languages); no post found meeting the TWiR/HN(≥100)/Lobsters(≥20) bar
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## rust-and-webassembly-book-rustwasm-github-io-unmaintained
name: Rust and WebAssembly Book (rustwasm.github.io, unmaintained)
identity: https://rustwasm.github.io/docs/book — published by GitHub org rustwasm ("Rust and WebAssembly", https://github.com/rustwasm)
type: institution
verdict: MEETS
track_record:
- book: official Rust-and-WebAssembly book, published under the rustwasm working-group org — https://rustwasm.github.io/docs/book
influence:
- reference book for Rust/Wasm; org also ships wasm-snip, wee_alloc, wasm_game_of_life — https://github.com/rustwasm (checked 2026-09-28)
checked: crate-dependents, production, role not separately checked (book already holds)

## rust-and-webassembly-working-group
name: Rust and WebAssembly Working Group
identity: GitHub org rustwasm, description "🦀 + 🕸️ = 💖", team repo rustwasm/team — https://github.com/rustwasm (checked 2026-09-28)
type: institution
verdict: MEETS
track_record:
- role: working group with dedicated team repo and multiple maintained crates/book under the rustwasm org — https://github.com/rustwasm/team
influence:
- maintains rustwasm.github.io/docs/book, wasm-snip, wee_alloc — https://github.com/rustwasm
checked: crate-dependents, production, book/course/talk/post not separately checked (role already holds)

## rust-async-book-async-book-rust-lang-github-io
name: Rust Async Book (async-book, rust-lang.github.io)
identity: https://rust-lang.github.io/async-book — published under the official rust-lang GitHub org
type: institution
verdict: MEETS
track_record:
- book: official Rust project documentation on async programming, hosted under rust-lang.github.io — https://rust-lang.github.io/async-book
influence:
- canonical reference for async Rust, cited across the ecosystem
checked: crate-dependents, production, role not separately checked (book already holds)

## rust-gamedev-working-group
name: Rust GameDev Working Group
identity: GitHub org rust-gamedev, mission "making rust the default language choice for game development" — https://github.com/rust-gamedev (checked 2026-09-28)
type: institution
verdict: MEETS
track_record:
- role: working group publishing "This Month in Rust GameDev" and gamedev.rs — https://gamedev.rs/news/051 (2024-06-05)
influence:
- arewegameyet.rs (767 stars), gamedev.rs (397 stars), wg coordination repo (520 stars) — https://github.com/rust-gamedev
checked: crate-dependents, production, book/course/talk/post not separately checked (role already holds)

## rust-leadership-council
name: Rust Leadership Council
identity: official Rust project governance body — https://www.rust-lang.org/governance/teams/leadership-council
type: institution
verdict: MEETS
track_record:
- role: "Charged with the success of the Rust Project as whole, consisting of representatives from top-level teams" — https://www.rust-lang.org/governance
influence:
- issued the Rust trademark policy update cited by the map — https://blog.rust-lang.org/2024/11/06/trademark-update (2024-11-06)
checked: crate-dependents, production, book/course/talk/post not separately checked (role already holds)

## rustunit
name: Rustunit (Stephan, founder)
identity: https://rustunit.com ("I am Stephan, Founder of Rustunit"); crate owner of bevy_ios_app_delegate
type: builder
verdict: MEETS
track_record:
- production: ships Bevy/iOS games and apps (tabataly, zoolitaire, tinytakeoff) and publishes the bevy_ios_app_delegate crate documented in a production deep-linking post — https://rustunit.com/blog/2025/05-18-bevy-ios-deep-linking (2025-05-18)
- crate-dependents: bevy_ios_app_delegate crate exists on crates.io (checked ownership; reverse-dep count not independently re-verified beyond production evidence)
influence:
- blog post documents a real shipped-app fix using objc2 from pure Rust — https://rustunit.com/blog/2025/05-18-bevy-ios-deep-linking (2025-05-18)
checked: role, book/course/talk/post not separately checked (production already holds)

## rustwasm-working-group-rust-and-webassembly-book
name: rustwasm working group (Rust and WebAssembly book)
identity: same GitHub org rustwasm as above — https://github.com/rustwasm
type: institution
verdict: MEETS
track_record:
- role + book: working group org publishing the Rust and WebAssembly book — https://rustwasm.github.io/docs/book
influence:
- reference documentation plus wasm-snip, wee_alloc, wasm_game_of_life crates/tools — https://github.com/rustwasm
checked: crate-dependents, production not separately checked (role + book already hold)

## salmans
name: Salman Saghafi
identity: https://github.com/salmans (real name given)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns crate razor-fol with 2 real reverse dependencies — https://crates.io/api/v1/crates/razor-fol/reverse_dependencies (checked 2026-09-28)
influence:
- razor-fol (first-order theory parsing/manipulation) has downstream dependents — https://crates.io/api/v1/crates/razor-fol/reverse_dependencies (checked 2026-09-28)
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## sam-cutter
name: S. Cutler (per official talk credit; map's voice id "sam-cutter" appears to be a mis-transcription of the surname "Cutler")
identity: YouTube oEmbed title "S. Cutler, D. Hugenroth, Z. Hunter Green: 'Secure Messaging: The Guardian's Whistleblowing System'", published by channel Rust Foundation — https://www.youtube.com/oembed?url=https://youtube.com/watch?v=8n13Oh8c0r4 (checked 2026-09-28); GitHub user "sam-cutter" (student A-level project repos) does NOT appear to be the same person — untied to that handle
type: builder
verdict: MEETS
track_record:
- production: co-presents a Rust Foundation-hosted talk on The Guardian's production whistleblowing/secure-messaging system, describing the team's own Rust code style choices — https://youtube.com/watch?v=8n13Oh8c0r4 ([12:09]-[13:10], 2025-10-03)
influence:
- talk hosted/published by the Rust Foundation's own YouTube channel — https://www.youtube.com/oembed?url=https://youtube.com/watch?v=8n13Oh8c0r4
checked: crate-dependents, role, book/course/talk/post not separately checked (production/talk already holds); identity spelling flagged for correction, not re-guessed

## sam-van-overmeire
name: Sam Van Overmeire
identity: Medium author @sam.van.overmeire — https://medium.com/@sam.van.overmeire/rust-macros-taking-care-of-some-lambda-boilerplate-96244d9e1924
type: educator
verdict: MEETS
track_record:
- post: Rust macros/Lambda-boilerplate post linked from This Week in Rust — confirmed via `gh api search/code?q=overmeire+repo:rust-lang/this-week-in-rust` (7 hits across issues), e.g. https://github.com/rust-lang/this-week-in-rust/blob/master/content/2024-01-17-this-week-in-rust.md (checked 2026-09-28)
influence:
- repeat TWiR inclusion (7 separate issues reference "overmeire") indicates a recurring, widely-read blogger — `gh api search/code?q=overmeire+repo:rust-lang/this-week-in-rust`
checked: crate-dependents, production, role not separately checked (post already holds)

## saulecabrera
name: Saúl Cabrera
identity: https://github.com/saulecabrera (blog saulecabrera.dev); public member of GitHub org bytecodealliance — `gh api orgs/bytecodealliance/public_members` includes "saulecabrera" (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: public member of the Bytecode Alliance org, with 189 commits authored in bytecodealliance/wasmtime — `gh api search/commits?q=repo:bytecodealliance/wasmtime+author:saulecabrera` → total_count 189 (checked 2026-09-28)
influence:
- substantial commit history in Wasmtime, a widely-depended-on Wasm runtime — https://github.com/bytecodealliance/wasmtime/pull/9889 (2025-01-04)
checked: crate-dependents, production, book/course/talk/post not separately checked (role already holds)

## saulecabrera-bytecode-alliance-wasmtime-winch-baseline
name: saulecabrera (Bytecode Alliance, Wasmtime Winch baseline-compiler maintainer)
identity: same as above — https://github.com/saulecabrera, Bytecode Alliance public member
type: builder
verdict: MEETS
track_record:
- role: 189 commits to bytecodealliance/wasmtime, Bytecode Alliance public member — `gh api search/commits?q=repo:bytecodealliance/wasmtime+author:saulecabrera` (checked 2026-09-28)
influence:
- Winch baseline compiler work within Wasmtime — https://github.com/bytecodealliance/wasmtime/pull/9889 (2025-01-04)
checked: crate-dependents, production, book/course/talk/post not separately checked (role already holds)
