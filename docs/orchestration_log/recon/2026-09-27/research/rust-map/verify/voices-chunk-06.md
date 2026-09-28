## ian-mcdonald
name: Ian McDonald
identity: https://github.com/bowlofarugula (bio: "Software Handyman", company "Extend"; name field "Ian McDonald" matches the byline "By Ian McDonald" on spinframework.dev, dated 2025-11-25; 141 commits to wasmcp/wasmcp) (checked 2026-09-28)
type: builder
verdict: FAILS
track_record: none found
influence:
- owns the `wasmcp` crate (7,126 downloads) but it has 0 real reverse dependencies — https://crates.io/api/v1/crates/wasmcp/reverse_dependencies (checked 2026-09-28)
checked: crate-dependents (wasmcp, wasmcp-macro, wasmcp-macros, wasmcp-wasi — 0 real dependents); production (no employer post naming Rust in production found); role (not a Rust project/foundation team member); book/course/talk/post (searched rust-lang/this-week-in-rust via `gh api search/code` for "wasmcp" and the post title — no hit; no HN/Lobsters thread found)

## ian-wagner
name: Ian Wagner
identity: https://stadiamaps.com/news/ferrostar-building-a-cross-platform-navigation-sdk-in-rust-part-2 (company bio: "Ian Wagner, Founder & Chief Architect... co-founder of Stadia Maps and leads engineering and operations") (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- production: Stadia Maps built and ships Ferrostar, a cross-platform turn-by-turn navigation SDK, with Rust as its shared core cross-compiled to iOS/Swift and Android/Kotlin — https://stadiamaps.com/news/ferrostar-building-a-cross-platform-navigation-sdk-in-rust-part-2 (published 2024-12-03, updated 2026-07-02)
influence:
- Founder & Chief Architect of Stadia Maps; wrote the two-part Ferrostar engineering series — https://stadiamaps.com/news/ferrostar-building-a-cross-platform-navigation-sdk-in-rust-part-2 (2024-12-03)
checked: crate-dependents, role (not checked; production bar already met)

## ian-whitney-blog-post-rust-via-its-core-values-cited
name: Ian Whitney
identity: untied — the Discourse/GitHub handle "iwhitney" used to attribute the quote carries no name, bio or repos confirming it is the same "Ian Whitney" credited as author of "Rust via its Core Values"; the blog post itself could not be located to verify authorship independently
type: unset
verdict: UNKNOWN
track_record: none found
influence:
- quoted as TWiR "Quote of the Week" on two separate occasions two years apart: by @nayru25 (2016-04-03) and re-cited by @cg-cnu (2018-04-25) — https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (2016-04-03; 2018-04-25)
checked: book/course/talk/post (repeat citation in the TWiR quote-of-the-week thread found, but no reachable copy of the original post and no confirmed profile for "iwhitney" — GitHub account exists with 0 public repos, no name/bio); crate-dependents, production, role (not checked — no identity to check against)

## ickshonpe
name: ickshonpe
identity: https://github.com/ickshonpe tied via https://bevy.org/community/people/ ("ickshonpe on GitHub", role "SME-UI") (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: listed Bevy team member, SME-UI (Subject Matter Expert, UI), on the official Bevy people page — https://bevy.org/community/people/ (checked 2026-09-28)
influence:
- 691 authored pull requests to bevyengine/bevy — via `gh api search/issues?q=repo:bevyengine/bevy+author:ickshonpe+type:pr` (checked 2026-09-28)
checked: crate-dependents (8 personally owned Bevy plugin crates checked — bevy_despawn_with, bevy_heterogeneous_texture_atlas_loader, bevy_fixed_sprites, bevy_mod_2d_hierarchy, bevy-ui-gradients, bevy_independent_transform, bevy-animated-text, bevy-ui-debug-overlay — all 0 real reverse dependents); production, book/course/talk/post (not checked; role bar already met)

## iiyese
name: iiYese
identity: https://github.com/iiYese (crates.io account id 182536, github_username_matches: true) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `aery` (25,005 downloads), 1 real reverse dependency — https://crates.io/api/v1/crates/aery/reverse_dependencies (checked 2026-09-28)
influence:
- also maintains aery_macros, bosons, moshimoshi, pencil_case, ssecs; authored bevyengine/bevy PR #15635 — https://github.com/bevyengine/bevy/pull/15635 (checked 2026-09-28)
checked: production, role (not a listed bevy.org team member; not checked further — crate-dependents bar already met)

## im-lunex
name: ʟᴜɴᴇx (im-lunex)
identity: https://github.com/im-lunex (bio "i love compilers and messing around them", blog https://im-lunex.vercel.app/) (checked 2026-09-28)
type: builder
verdict: FAILS
track_record: none found
influence:
- authored zed-industries/zed PR #38102 (Zed is a production Rust code editor); owns Rust repos "wave" and a "rust-analyzer" fork, none published to crates.io — https://github.com/zed-industries/zed/pull/38102 (checked 2026-09-28)
checked: crate-dependents (no crates.io account registered under this handle); production (no employer/production post found); role (not a listed team member of any Rust project checked); book/course/talk/post (none found)

## inactive-user
name: inactive-user (Lobsters' own display label for a deactivated/removed account)
identity: untied
type: unset
verdict: UNKNOWN
track_record: none found
influence: none found
checked: identity — "inactive-user" is Lobsters' placeholder for a deleted account, not a real handle; no profile exists to tie to a person, so crate-dependents/production/role/book-course-talk-post could not be checked — https://lobste.rs/s/fzro7f (comment dated 2025-11-01)

## iroh-n0-dignifiedquire-post-author
name: Friedel Ziegelmayer (GitHub: dignifiedquire)
identity: https://github.com/dignifiedquire (GitHub name field "Friedel Ziegelmayer"; byline "by dignifiedquire" on https://iroh.computer/blog/iroh-0-98-0-getting-back-to-traversing-nats) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: author of the official iroh project release blog post ("iroh 0.98.0 — Getting back to traversing NATs"), 497 authored/merged pull requests to n0-computer/iroh — https://iroh.computer/blog/iroh-0-98-0-getting-back-to-traversing-nats (2026-04-17); PR count via `gh api search/issues?q=repo:n0-computer/iroh+author:dignifiedquire+type:pr` (checked 2026-09-28)
influence:
- core maintainer of iroh, a Rust P2P networking stack — one of gym's named target domains ("decentralized systems built on iroh") — https://iroh.computer/blog/iroh-0-98-0-getting-back-to-traversing-nats (2026-04-17)
checked: crate-dependents, production (not checked; role bar already met)

## iroh-n0-friedel-ziegelmayer-r-diger-klaehn-post-authors
name: Friedel Ziegelmayer & Rüdiger Klaehn
identity: https://github.com/dignifiedquire (Friedel Ziegelmayer); https://github.com/rklaehn (GitHub name field "Rüdiger Klaehn", bio "Old grumpy hacker... Independent hacker") — both tied via byline "by Friedel Ziegelmayer & Rüdiger Klaehn" on https://iroh.computer/blog/iroh-1-0-0-rc-0 (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: co-authors of the official "iroh 1.0.0-rc.0 — The first release candidate" project blog post; 497 (Ziegelmayer) and 391 (Klaehn) authored/merged pull requests to n0-computer/iroh — https://iroh.computer/blog/iroh-1-0-0-rc-0 (2026-05-11); PR counts via `gh api search/issues?q=repo:n0-computer/iroh+author:<login>+type:pr` (checked 2026-09-28)
influence:
- announced iroh's first 1.0 release candidate after four years of work and 50+ releases — https://iroh.computer/blog/iroh-1-0-0-rc-0 (2026-05-11)
checked: crate-dependents, production (not checked; role bar already met)

## its-the-shrimp
name: Tim Kurdov (its-the-shrimp)
identity: https://github.com/its-the-shrimp (GitHub name field "Tim Kurdov"; crates.io account id 241121, github_username_matches: true) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `shrimple-parser` (14,216 downloads), 2 real reverse dependencies — https://crates.io/api/v1/crates/shrimple-parser/reverse_dependencies (checked 2026-09-28)
influence:
- also maintains yew-fmt (26,054 downloads), shrimple-telegram, permissive-search; authored yewstack/yew PR #3509 — https://github.com/yewstack/yew/pull/3509 (checked 2026-09-28)
checked: production, role (not checked; crate-dependents bar already met)

## ivan-nikulin
name: Ivan Nikulin
identity: https://blog.cloudflare.com/introducing-oxy (official Cloudflare blog byline "Ivan Nikulin") (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- production: authored Cloudflare's official announcement of Oxy, "Cloudflare's Rust-based next generation proxy framework," underlying the Zero Trust Gateway, iCloud Private Relay second-hop proxy, and internal egress routing in production — https://blog.cloudflare.com/introducing-oxy (2023-03-02)
influence:
- Oxy handles "massive amounts of daily traffic" across multiple Cloudflare production services — https://blog.cloudflare.com/introducing-oxy (2023-03-02)
checked: crate-dependents, role (not checked; production bar already met)

## ivarflakstad
name: ivarflakstad
identity: https://github.com/ivarflakstad (public huggingface org member; crates.io co-owner of candle-core alongside LaurentMazare and Narsil) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- crate-dependents: co-owns `candle-core`, 617 real reverse dependencies — https://crates.io/api/v1/crates/candle-core/reverse_dependencies (checked 2026-09-28)
- role: public member of the huggingface GitHub org, 106 authored pull requests to huggingface/candle — via `gh api orgs/huggingface/members` and `gh api search/issues?q=repo:huggingface/candle+author:ivarflakstad+type:pr` (checked 2026-09-28)
influence:
- candle is Hugging Face's Rust ML framework — one of gym's named target domains ("machine learning adjacent to burn and candle")
checked: production (not checked; two bars already met)

## ivmarkov
name: ivmarkov
identity: https://github.com/ivmarkov (crates.io user id 127313, github_username_matches: true) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `edge-executor` (254,489 downloads), 5 real reverse dependencies — https://crates.io/api/v1/crates/edge-executor/reverse_dependencies (checked 2026-09-28); co-owns `esp-idf-svc` with MabezDev and github:esp-rs:espressif — https://crates.io/api/v1/crates/esp-idf-svc/owners (checked 2026-09-28)
influence:
- esp-idf-svc is Espressif's official Rust embedded-systems services crate, part of gym's "embedded" target domain
checked: role (not a public esp-rs GitHub org member per `gh api orgs/esp-rs/members`); production (not checked; crate-dependents bar already met)

## jackdk
name: jackdk
identity: untied — lobste.rs profile unreachable (HTTP 429, rate-limited on every retry); a GitHub account "jackdk" exists but has no name, bio, or public repos, so it cannot be confirmed as the same person
type: unset
verdict: UNKNOWN
track_record: none found
influence: none found
checked: identity (https://lobste.rs/u/jackdk returned 429 Too Many Requests on repeated attempts, including via the cache script); crate-dependents, production, role, book/course/talk/post (not checked — no confirmed identity to check against)

## jacko-io
name: Jack O'Connor
identity: https://github.com/oconnor663 (GitHub name field "Jack O'Connor", blog field "http://jacko.io" matching the cited source's own domain) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `blake3`, 3,777 real reverse dependencies — https://crates.io/api/v1/crates/blake3/reverse_dependencies (checked 2026-09-28)
influence:
- author of the BLAKE3 hash function and its reference Rust crate, depended on across the ecosystem
checked: production, role (not checked; crate-dependents bar already met)

## jake-goulding-for-the-rust-infrastructure-team
name: Jake Goulding
identity: https://github.com/shepmaster (GitHub name field "Jake Goulding", company "@integer32llc") (checked 2026-09-28)
type: institution
verdict: MEETS
track_record:
- role: authored the official Rust project blog post "Demoting x86_64-apple-darwin to Tier 2 with host tools," "on behalf of the Infrastructure team" — https://blog.rust-lang.org/2025/08/19/demoting-x86-64-apple-darwin-to-tier-2-with-host-tools (2025-08-19)
influence:
- speaks for the Rust project's Infrastructure team on official platform-tier decisions; works at Integer 32, a Rust consultancy
checked: crate-dependents, production (not checked; role bar already met)

## jakub-ber-nek-on-behalf-of-the-rust-funding-team
name: Jakub Beránek
identity: https://github.com/Kobzol (GitHub name field "Jakub Beránek"; bio: "Member of the Rust Leadership Council and the Rust Compiler and Infrastructure teams... Sovereign Tech Fellow") (checked 2026-09-28)
type: institution
verdict: MEETS
track_record:
- role: authored the official Rust project blog post "Announcing a Maintainer in Residence: Scott Schafer for the Cargo team," "on behalf of the Funding team" — https://blog.rust-lang.org/2026/09/22/announcing-a-maintainer-in-residence-scott-schafer-for-the-cargo-team (2026-09-22); independently confirmed as Rust Leadership Council / Compiler / Infrastructure teams member via GitHub bio
influence:
- directs Rust Foundation Maintainers Fund (RFMF) allocations as a Rust Leadership Council member
checked: crate-dependents, production (not checked; role bar already met)

## jakub-ber-nek-on-behalf-of-the-rust-project-mentorship-team
name: Jakub Beránek
identity: https://github.com/Kobzol (same person as above)
type: institution
verdict: MEETS
track_record:
- role: authored the official Rust project blog post "Announcing Google Summer of Code 2026 selected projects," "on behalf of the mentorship team" — https://blog.rust-lang.org/2026/04/30/gsoc-2026-selected-projects (2026-04-30)
influence: (same as jakub-ber-nek-on-behalf-of-the-rust-funding-team)
checked: crate-dependents, production (not checked; role bar already met)

## james-eastham
name: James Eastham
identity: https://github.com/jeastham1993 (bio: "Building serverless things... .NET & Rust wrangler... Public speaker, content-creator", company "Datadog", blog https://jameseastham.co.uk) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- talk: conference talk walking through porting a real Rust web API and Kafka-consuming background service from Fargate to Lambda, with production latency/memory/cold-start measurements (3/850 and 4/1,350 invocations) — https://youtube.com/watch?v=x4yUfs0GrI4 (referenced 2024-12-13)
- production: same talk documents an actual production Rust workload migration and its measured outcomes
influence:
- Datadog developer advocate and public speaker/content-creator on serverless Rust workloads
checked: crate-dependents, role (not checked; talk/production bars already met)

## jamesmunns
name: James Munns
identity: https://github.com/jamesmunns (bio: "Bringing Rust to new places... Resources Team @ Rust Embedded Working Group", company "@oxidecomputer") (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: public GitHub org member of embassy-rs, 412 authored commits to embassy-rs/embassy — via `gh api orgs/embassy-rs/members` and `gh api search/commits?q=repo:embassy-rs/embassy+author:jamesmunns` (checked 2026-09-28); also self-describes as "Resources Team @ Rust Embedded Working Group"
influence:
- works at Oxide Computer (Rust-first firmware/cloud company); maintains embassy, a widely used embedded async Rust framework, part of gym's "embedded" target domain
checked: crate-dependents, production (not checked; role bar already met)

## jamesmunns-embassy-maintainer
name: jamesmunns (embassy maintainer)
identity: https://github.com/jamesmunns (same person as jamesmunns above)
type: builder
verdict: MEETS
track_record:
- role: public GitHub org member of embassy-rs, 412 authored commits to embassy-rs/embassy (same evidence as jamesmunns) — https://github.com/embassy-rs/embassy/pull/4989 (source PR, checked 2026-09-28)
influence: (same as jamesmunns)
checked: crate-dependents, production (not checked; role bar already met)

## janhohenheim
name: Jan Hohenheim
identity: https://github.com/janhohenheim tied via https://bevy.org/community/people/ ("Jan Hohenheim... janhohenheim on GitHub... Works with Bevy for Neuroinformatics") (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: listed Bevy team member on the official Bevy people page; creator of the Foxtrot template and Yarn Spinner for Rust — https://bevy.org/community/people/ (checked 2026-09-28)
influence:
- "Works with Bevy for Neuroinformatics" at the Institute of Neuroinformatics, UZH/ETH Zurich (per GitHub profile)
checked: crate-dependents, production (not checked; role bar already met)

## jasn-armstrng
name: Jason Armstrong
identity: https://github.com/jasn-armstrng (GitHub name field "Jason Armstrong † | Data Engineer | Nomad"; same distinctive handle spelling as the Discourse username — strong tie) (checked 2026-09-28)
type: unset
verdict: FAILS
track_record: none found
influence:
- public repo "100-Days-Of-Rust" indicates a learning project, not maintained/production work — https://github.com/jasn-armstrng/100-Days-Of-Rust (checked 2026-09-28)
checked: crate-dependents (no crates.io account registered under this handle); production (no evidence found); role (no evidence found); book/course/talk/post (the forum comment defending AI-assisted writing is not itself a book/course/talk, and no TWiR/HN/Lobsters qualification found for anything he authored)

## jdahlstrom
name: Johannes Dahlström
identity: https://github.com/jdahlstrom (GitHub name field "Johannes Dahlström", matches the Discourse handle "jdahlstrom" exactly; crates.io user id 144271) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `retrofire-core`, 3 real reverse dependencies — https://crates.io/api/v1/crates/retrofire-core/reverse_dependencies (checked 2026-09-28)
influence:
- retrofire, a from-scratch Rust software 3D renderer (80 GitHub stars)
checked: production, role (not checked; crate-dependents bar already met)

## jessebraham
name: Jesse Braham
identity: https://github.com/jessebraham (GitHub name field "Jesse Braham"; public GitHub org member of esp-rs) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: public GitHub org member of esp-rs, co-owner of esp-idf-svc, contributor to esp-rs/esp-hal — via `gh api orgs/esp-rs/members` (checked 2026-09-28)
influence:
- esp-hal is Espressif's official Rust hardware abstraction layer for ESP32 microcontrollers, part of gym's "embedded" target domain
checked: crate-dependents, production (not checked; role bar already met)
