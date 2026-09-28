## dist1ll
name: Adrian Alic
identity: https://github.com/dist1ll (crates.io login match confirms account; blog https://alic.dev)
type: builder
verdict: FAILS
track_record:
- crate-dependents: owns only `hltv` on crates.io, 0 reverse dependencies — https://crates.io/api/v1/crates/hltv/reverse_dependencies (2026-09-28)
influence:
- blog posts on systems/Rust topics get low reach: "Beating the Fastest Lexer Generator in Rust" peaked at 5 HN points, well under the 100-point bar — https://news.ycombinator.com/item?id=37564363 (2023-06)
checked: crate-dependents (found, below bar), production, role, book/course/talk/post

## dlight
name: Elias Gabriel Amaral da Silva
identity: https://github.com/dlight (internals.rust-lang.org profile website field points to github.com/dlight, confirming the forum account is this person) — https://internals.rust-lang.org/u/dlight.json
type: builder
verdict: FAILS
track_record:
- crate-dependents: owns merged_range2, orgasm, p-macro, pdftotext — all 0 reverse dependencies — https://crates.io/api/v1/crates/orgasm/reverse_dependencies (2026-09-28)
influence:
- none found meeting the bar; forum posts on internals.rust-lang.org are technical proposals, not measured for reach
checked: crate-dependents (found, 0), production, role, book/course/talk/post

## dominaezzz
name: Dominic Fischer
identity: https://github.com/dominaezzz (crates.io login match; bio "I tend to do Rust these days")
type: builder
verdict: FAILS
track_record:
- crate-dependents: owns only `max342x`, 0 reverse dependencies — https://crates.io/api/v1/crates/max342x/reverse_dependencies (2026-09-28)
influence:
- active reviewer/contributor on esp-rs/esp-hal (embedded HAL), e.g. approved PR #2900 and #5744, but esp-rs is a community org, not a rust-lang team or an employer — https://github.com/esp-rs/esp-hal/pull/5744 (2026-06-17)
checked: crate-dependents (found, 0), production, role, book/course/talk/post

## dominaezzz-esp-hal-reviewer
name: Dominic Fischer (same GitHub account as Voice `dominaezzz`)
identity: https://github.com/dominaezzz — the cited claim's quote and timestamp (2026-06-15T21:09:39Z, "safely useable is too vague...") match verbatim the first review comment by GitHub user `Dominaezzz` on esp-rs/esp-hal PR #5744; this is not a distinct person from `dominaezzz`
type: builder
verdict: FAILS
track_record:
- crate-dependents: same account as `dominaezzz` — owns only `max342x`, 0 reverse dependencies — https://crates.io/api/v1/crates/max342x/reverse_dependencies (2026-09-28)
influence:
- same PR-review activity on esp-rs/esp-hal as `dominaezzz` — https://github.com/esp-rs/esp-hal/pull/5744 (2026-06-17)
checked: crate-dependents (found, 0), production, role, book/course/talk/post

## dragondev1906
name: unset (GitHub name/bio empty; internals.rust-lang.org profile exists but carries no display name)
identity: https://github.com/DragonDev1906 — untied to a real name; pseudonymous but the handle is consistent across GitHub and internals.rust-lang.org
type: builder
verdict: FAILS
track_record:
- crate-dependents: no crates.io account found for this handle — https://crates.io/api/v1/users/dragondev1906 (2026-09-28)
influence:
- none found; the cited internals.rust-lang.org post is a design-discussion reply, not measured for reach
checked: crate-dependents (none found), production, role, book/course/talk/post

## drewridley
name: Drew Ridley
identity: https://github.com/drewridley
type: builder
verdict: FAILS
track_record:
- crate-dependents: owns aiform-macros, bronzite(-client/-daemon/-macros/-query/-types), nevy, plumesplat, surrealguard — all 0 reverse dependencies — https://crates.io/api/v1/crates/nevy/reverse_dependencies (2026-09-28)
influence:
- 1 merged/opened PR to DioxusLabs/dioxus found (#3797), not evidence of a DioxusLabs role — https://github.com/DioxusLabs/dioxus/pull/3797 (2025-03-19)
checked: crate-dependents (found, 0), production, role, book/course/talk/post

## ds84182
name: Dwayne Slater
identity: https://github.com/ds84182
type: builder
verdict: FAILS
track_record:
- crate-dependents: no crates.io account found — https://crates.io/api/v1/users/ds84182 (2026-09-28)
influence:
- commented on rust-lang/rfcs PR #3987 ("Externref lang item for Wasm targets"), authored by Guy Bedford, not by ds84182 — https://github.com/rust-lang/rfcs/pull/3987 (2026-07-30)
checked: crate-dependents (none found), production, role, book/course/talk/post

## durka42
name: unknown
identity: untied — no GitHub account (404), no users.rust-lang.org profile findable; the cited claim is a 2015 quote embedded inside another user's (@XMPPwocky) forum post reporting an IRC exchange, not durka42 posting directly. A GitHub user `durka` (Alex Burka, embedded engineer) exists but nothing ties that account to the "durka42" handle specifically — crediting it would be a guess
type: unset
verdict: UNKNOWN
track_record: none — identity could not be tied
influence: none — identity could not be tied
checked: identity-tying attempted via GitHub, crates.io, users.rust-lang.org; none resolved

## ealmloff
name: Evan Almloff
identity: https://github.com/ealmloff (public member of the DioxusLabs GitHub org; crates.io login match)
type: builder
verdict: MEETS
track_record:
- production: bio "Working on the Rust ML and GUI ecosystem", company "Dioxus Labs"; public org member — https://github.com/ealmloff (2026-09-28)
- crate-dependents: owns dioxus-desktop, 23 reverse dependencies — https://crates.io/api/v1/crates/dioxus-desktop/reverse_dependencies (2026-09-28)
influence:
- maintains multiple dioxus-* crates including dioxus-cli, dioxus-desktop (23 dependents), dioxus-kit — https://crates.io/crates/dioxus-desktop (2026-09-28)
checked: role, book/course/talk/post (none found)

## ecoskey
name: Emerson Coskey
identity: https://github.com/ecoskey (crates.io login match; blog coskey.dev unreachable at fetch time)
type: builder
verdict: FAILS
track_record:
- crate-dependents: owns `gigs`, 0 reverse dependencies — https://crates.io/api/v1/crates/gigs/reverse_dependencies (2026-09-28)
influence:
- 61 PRs found against bevyengine/bevy (github search), a substantial open-source contribution record, but Bevy is a volunteer-run engine, not an employer or a rust-lang/foundation team — https://github.com/bevyengine/bevy/pulls?q=is%3Apr+author%3Aecoskey (2026-09-28)
checked: crate-dependents (found, 0), production, role, book/course/talk/post

## edjopato
name: unset (GitHub name/bio not given; "Full of cheese"); crates.io login match confirms same account
identity: https://github.com/edjopato (blog https://edjopato.de)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns tui-tree-widget, 71 reverse dependencies — https://crates.io/api/v1/crates/tui-tree-widget/reverse_dependencies (2026-09-28)
influence:
- tui-tree-widget is depended on by 71 crates in the ratatui/TUI ecosystem — https://crates.io/crates/tui-tree-widget (2026-09-28)
checked: production, role, book/course/talk/post (none found)

## eggyal
name: unset (GitHub and internals.rust-lang.org profiles both carry the bare handle, no display name)
identity: https://github.com/eggyal — pseudonymous but the handle is consistent and OAuth-verified across GitHub, crates.io and internals.rust-lang.org
type: builder
verdict: FAILS
track_record:
- crate-dependents: owns cabismo, copse, rattish, thinnable — all 0 reverse dependencies — https://crates.io/api/v1/crates/copse/reverse_dependencies (2026-09-28)
influence:
- none found meeting the bar
checked: crate-dependents (found, 0), production, role, book/course/talk/post

## ekleog
name: Léo Gaspard
identity: https://github.com/ekleog (blog https://ekleog.org/; crates.io login match)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns crdb-core, 10 reverse dependencies — https://crates.io/api/v1/crates/crdb-core/reverse_dependencies (2026-09-28) — caveat: all 10 listed dependents (crdb, crdb-cache, crdb-client, crdb-helpers, crdb-macros, crdb-postgres, crdb-server, crdb-sqlite, crdb-test-utils, crdb-indexed-db) are companion crates of the same crdb project he authors, not independent third-party adoption; still ≥1 per the literal reverse_dependencies bar
influence:
- maintains the crdb crate family (CRDT database toolkit) — https://crates.io/crates/crdb-core (2026-09-28)
checked: production, role, book/course/talk/post (none found)

## ekuber
name: Esteban Kuber
identity: https://internals.rust-lang.org/u/ekuber (display name "Esteban Kuber"); matches the rust-lang team roster entry for name "Esteban Kuber" / github_id 1606434, which resolves to GitHub login `estebank` — https://team-api.infra.rust-lang.org/v1/people.json ; https://github.com/estebank — note: GitHub handle `ekuber` itself belongs to an unrelated person and is NOT used here
type: institution
verdict: MEETS
track_record:
- role: member of the rust-lang `compiler` team (rustc diagnostics) — https://team-api.infra.rust-lang.org/v1/teams/compiler.json (2026-09-28)
influence:
- rust-lang compiler team member; long-running internals.rust-lang.org threads on diagnostics (e.g. "Compiler diagnostics improvement wishlist", 31 posts) — https://internals.rust-lang.org/t/compiler-diagnostics-improvement-wishlist/6886 (2018-03)
checked: crate-dependents, production, book/course/talk/post (none additionally needed once role held)

## elipsitz
name: Eli Lipsitz
identity: https://github.com/elipsitz
type: builder
verdict: FAILS
track_record:
- crate-dependents: no crates.io account found for this handle — https://crates.io/api/v1/users/elipsitz (2026-09-28)
influence:
- contributed to esp-rs/esp-idf (PR #479); personal Rust project gba-emulator (32 stars) — https://github.com/esp-rs/esp-idf/pull/479 (2024-09-17)
checked: crate-dependents (none found), production, role, book/course/talk/post

## elitetk
name: Tomasz Kramkowski
identity: https://github.com/EliteTK (public member of the astral-sh GitHub org)
type: builder
verdict: MEETS
track_record:
- production: 151 merged/opened PRs to astral-sh/uv (Rust-based Python package manager), public org member of astral-sh — https://github.com/astral-sh/uv/pulls?q=is%3Apr+author%3AEliteTK (2026-09-28)
influence:
- sustained contributor to uv, a widely-adopted Rust tool in the Python ecosystem — https://github.com/EliteTK (2026-09-28)
checked: crate-dependents (owns 0 crates on crates.io), role, book/course/talk/post

## emilk
name: Emil Ernerfeldt
identity: https://github.com/emilk (bio: "Rust coder, creator of egui, CTO of rerun.io"; crates.io login match)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns egui, 1228 reverse dependencies; eframe, 1059 reverse dependencies — https://crates.io/api/v1/crates/egui/reverse_dependencies (2026-09-28)
- production: CTO of Rerun.io, a Rust-based visualization company built on egui — https://github.com/emilk (2026-09-28)
influence:
- creator/maintainer of egui (1228 dependents) and eframe (1059 dependents), core to the Rust immediate-mode GUI ecosystem — https://crates.io/crates/egui (2026-09-28)
checked: role, book/course/talk/post (not needed; already MEETS on two kinds)

## emily-dixon
name: Emily Dixon
identity: https://mux.com/blog/practical-client-side-rust-for-android-ios-and-web (byline: Senior Software Engineer, Mux; no matching GitHub account found under this slug)
type: builder
verdict: MEETS
track_record:
- production: authored "Practical Client-Side Rust for Android, iOS, and Web" as a Mux (video infrastructure company) engineer, describing Rust used in Mux's mobile/web clients — https://mux.com/blog/practical-client-side-rust-for-android-ios-and-web (2023-12-13)
influence:
- post reached only 8 HN points, below the 100-point post bar; counted here for the production kind, not the post kind — https://news.ycombinator.com/item?id=38625810 (2023-12)
checked: crate-dependents, role, book/course/talk/post (post found but below bar)

## epage
name: Ed Page
identity: https://github.com/epage (crates.io login match)
type: institution
verdict: MEETS
track_record:
- role: member of the rust-lang `cargo` team — https://team-api.infra.rust-lang.org/v1/teams/cargo.json (2026-09-28)
influence:
- rust-lang Cargo team member; maintains the anstyle/anstream crate family used across the terminal-styling ecosystem — https://crates.io/crates/anstyle (2026-09-28)
checked: crate-dependents (owned crates like anstyle not individually re-checked past role confirmation), production, book/course/talk/post

## eric-zhang
name: Eric Zhang
identity: https://modal.com/blog/serverless-http (byline: Founding Engineer, Modal; Twitter @ekzhang1) tying to https://github.com/ekzhang (name match, bio match) — note: the Voice id "eric-zhang" does NOT match his actual GitHub login `ekzhang`; the GitHub account literally named `eric-zhang` is an unrelated person ("Marely Hull") and was correctly not used
type: builder
verdict: MEETS
track_record:
- production: Founding Engineer at Modal (serverless GPU/compute platform), authored "Serverless HTTP" describing Rust infrastructure work there — https://modal.com/blog/serverless-http (2024-03-14)
influence:
- currently listed at @thinking-machines-lab, formerly Modal founding engineer; personal site https://www.ekzhang.com — https://github.com/ekzhang (2026-09-28)
checked: crate-dependents, role, book/course/talk/post

## eucliddivisionlemma
name: unset (GitHub name/bio empty)
identity: https://github.com/EuclidDivisionLemma — untied to a real name
type: builder
verdict: FAILS
track_record:
- crate-dependents: no crates.io account found — https://crates.io/api/v1/users/eucliddivisionlemma (2026-09-28)
influence:
- opened zed-industries/zed PR #36497; small personal Rust repos (jangri, ruminate, numad), none with meaningful stars — https://github.com/zed-industries/zed/pull/36497 (2025-09-13)
checked: crate-dependents (none found), production, role, book/course/talk/post

## eugineerd
name: unset (GitHub name/bio empty)
identity: https://github.com/eugineerd — untied to a real name
type: builder
verdict: FAILS
track_record:
- crate-dependents: no crates.io account found — https://crates.io/api/v1/users/eugineerd (2026-09-28)
influence:
- 24 PRs found against bevyengine/bevy (github search), a real but volunteer-project contribution record, not an employer, role, or crate — https://github.com/bevyengine/bevy/pulls?q=is%3Apr+author%3Aeugineerd (2026-09-28)
checked: crate-dependents (none found), production, role, book/course/talk/post

## evgenii-seliverstov
name: Evgenii Seliverstov
identity: https://www.youtube.com/watch?v=zQgN75kdR9M — talk listed on the official "Rust Nation UK" conference YouTube channel, full name given as speaker
type: educator
verdict: MEETS
track_record:
- book/course/talk/post: spoke at Rust Nation UK, "Parallel Programming in Rust: Techniques for Blazing Speed" (official conference channel listing) — https://www.youtube.com/watch?v=zQgN75kdR9M (2025-02-26)
influence:
- conference talk on Rust parallelism/SIMD/GPU programming, published by Rust Nation UK's official channel — https://www.youtube.com/watch?v=zQgN75kdR9M (2025-02-26)
checked: crate-dependents, production, role (not needed; MEETS on talk)

## fanf
name: Tony Finch
identity: https://lobste.rs/u/fanf (og:description links to https://dotat.at/) tying to https://github.com/fanf2 (blog field matches dotat.at) — note: a DIFFERENT person, François Armand, owns the GitHub handle literally spelled `fanf`; that account was checked and correctly rejected as not matching this lobste.rs identity
type: builder
verdict: MEETS
track_record:
- crate-dependents: co-owns async-condvar-fair (with Ian Jackson), 3 reverse dependencies, 2.1M downloads — https://crates.io/api/v1/crates/async-condvar-fair/reverse_dependencies (2026-09-28); confirmed co-ownership at https://crates.io/api/v1/crates/async-condvar-fair/owners (2026-09-28)
influence:
- co-maintains async-condvar-fair (3 dependents, 2.1M downloads) and other Rust crates (hippotat, otter family) alongside Ian Jackson — https://crates.io/crates/async-condvar-fair (2026-09-28)
checked: production, role, book/course/talk/post (not needed; MEETS on crate-dependents)

## farnz
name: Simon Farnsworth
identity: https://github.com/farnz ; matching display name confirmed at https://internals.rust-lang.org/u/farnz.json
type: builder
verdict: FAILS
track_record:
- crate-dependents: no crates.io crates owned — https://crates.io/api/v1/crates?user_id=7095 (2026-09-28)
influence:
- longtime internals.rust-lang.org participant on stdlib API design (e.g. Instant::min/max thread), company listed as "@lunar-energy" but no public org membership or Rust-production evidence found — https://internals.rust-lang.org/t/instant-systemtime-min-max/21375 (2024-08-16)
checked: crate-dependents (found, 0), production, role, book/course/talk/post
