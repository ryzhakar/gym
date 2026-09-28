## fasterthanlime
name: Amos Wenger (fasterthanlime)
identity: https://github.com/fasterthanlime (bio: "hi, I'm amos! co-host of self-directed research podcast, teacher, video maker, software mercenary"; blog fasterthanli.me matches Source domain)
type: educator
verdict: MEETS
track_record:
- crate-dependents: owns `facet` on crates.io; 202 real reverse dependents — https://crates.io/api/v1/crates/facet/reverse_dependencies?per_page=1 (2026-09-28)
influence:
- crate `facet` (reflection/serde-adjacent), 202 dependent crates, owner confirmed as github.com/fasterthanlime — https://crates.io/api/v1/crates/facet/owners (2026-09-28)
- long-form technical writing at fasterthanli.me, cited as a Voice by this map's own Source (does-dioxus-spark-joy) — https://fasterthanli.me/articles/does-dioxus-spark-joy (2025-11-22)
checked: production, role, book/course/talk/post (not separately verified beyond crate-dependents; likely also meets via reach but not confirmed with a TWiR/HN/Lobsters link in this pass)

## federico-mena-quintero
name: Federico Mena Quintero
identity: https://github.com/federicomenaquintero (bio: "GNOME co-founder"; blog viruta.org matches Source domain exactly)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `librsvg` on crates.io; 2 real reverse dependents — https://crates.io/api/v1/crates/librsvg/reverse_dependencies?per_page=1 (2026-09-28)
- role: GNOME co-founder (self-stated bio), long-time librsvg maintainer — https://github.com/federicomenaquintero (2026-09-28)
influence:
- crate `librsvg`, 2 dependent crates, sole confirmed crates.io owner (co-owner: WhatAmISupposedToPutHere) — https://crates.io/api/v1/crates/librsvg/owners (2026-09-28)
- GNOME co-founder role, employer SUSE — https://github.com/federicomenaquintero (2026-09-28)
checked: production, book/course/talk/post (not separately verified)

## felipebalbi
name: Felipe Balbi
identity: https://github.com/felipebalbi → personal site https://balbi.sh/ ("Felipe Balbi is a firmware and embedded systems developer... I work mostly in Rust and C")
type: builder
verdict: MEETS
track_record:
- production: 115 merged PRs into embassy-rs/embassy, including PR #5175 adding SPI driver support for the NXP MCXA276 family (embassy-mcxa, under the NXP-affiliated OpenDevicePartnership org) — https://github.com/embassy-rs/embassy/pull/5175 (2026-01-07)
influence:
- 115 merged pull requests into embassy-rs/embassy (count via GitHub search) — https://github.com/embassy-rs/embassy/pulls?q=is%3Apr+is%3Amerged+author%3Afelipebalbi (2026-09-28)
checked: crate-dependents (not a crates.io owner — no account found under alternate check for embassy-nxp: owner is Dirbaio), role (not an embassy-rs public org member), book/course/talk/post

## felipebalbi-nxp-embedded-engineer-embassy-nxp-contributor
name: felipebalbi (NXP embedded engineer, embassy-nxp contributor)
identity: https://github.com/felipebalbi → https://balbi.sh/ — same person as the `felipebalbi` Voice above; the NXP-employee framing is not self-confirmed on his own site (which states only "firmware and embedded systems developer," no employer named) but is corroborated by his merged work on embassy-mcxa (NXP MCXA-family chips) under OpenDevicePartnership
type: builder
verdict: MEETS
track_record:
- production: same PR #5175 (embassy-mcxa NXP MCXA276 SPI driver), plus embassy-rs/embassy#4989 comment on HAL merge strategy — https://github.com/embassy-rs/embassy/pull/4989 (2025-12-04)
influence:
- same 115 merged embassy-rs/embassy PRs as the `felipebalbi` Voice — https://github.com/embassy-rs/embassy/pulls?q=is%3Apr+is%3Amerged+author%3Afelipebalbi (2026-09-28)
checked: crate-dependents, role, book/course/talk/post — no direct evidence found; NXP employment specifically is inferred from chip-family context, not stated by the Voice or a profile

## ferrous-systems-jonathan
name: Ferrous Systems (Jonathan)
identity: untied — the post's byline is the bare first name "Jonathan" (confirmed via the Ferrous Systems blog index, which lists posts by first name only: Ana, Jessie, Jynn, Julia, Jonathan, Brigitte); no surname, GitHub handle, or profile page found tying it to a real person
type: unset
verdict: UNKNOWN
track_record: none found — identity could not be tied to a checkable profile
influence: none found
checked: crate-dependents, production, role, book/course/talk/post — all blocked on the untied identity; Ferrous Systems itself is a known embedded-Rust consultancy (ferrous-systems.com), but that institutional fact does not establish who "Jonathan" is

## fitzgen
name: Nick Fitzgerald (fitzgen)
identity: https://github.com/fitzgen (name: "Nick Fitzgerald", blog fitzgen.com)
type: builder
verdict: MEETS
track_record:
- role: public member of the Bytecode Alliance GitHub org — https://github.com/orgs/bytecodealliance/people (2026-09-28)
- production: 1094 merged PRs into bytecodealliance/wasmtime (803 real reverse dependents on the `wasmtime` crate) — https://github.com/bytecodealliance/wasmtime/pulls?q=is%3Apr+is%3Amerged+author%3Afitzgen (2026-09-28)
influence:
- Bytecode Alliance team role; wasmtime crate 803 dependents — https://crates.io/api/v1/crates/wasmtime/reverse_dependencies?per_page=1 (2026-09-28)
- original author of the widely-used `arbitrary` crate (now owned by nagisa/rust-fuzz, not fitzgen) — https://crates.io/api/v1/crates/arbitrary/owners (2026-09-28)
checked: crate-dependents (not a current crates.io owner of a crate himself), book/course/talk/post

## fitzgen-bytecode-alliance-wasmtime-core-arbitrary-crate
name: fitzgen (Bytecode Alliance / Wasmtime core, `arbitrary` crate author)
identity: https://github.com/fitzgen — same person as the `fitzgen` Voice above
type: builder
verdict: MEETS
track_record:
- role: public member of the Bytecode Alliance GitHub org — https://github.com/orgs/bytecodealliance/people (2026-09-28)
- production: PR #10924 review comments on bytecodealliance/wasmtime — https://github.com/bytecodealliance/wasmtime/pull/10924 (2025-06-12)
influence:
- same as `fitzgen`: Bytecode Alliance role, 1094 merged wasmtime PRs, wasmtime crate 803 dependents — https://crates.io/api/v1/crates/wasmtime/reverse_dependencies?per_page=1 (2026-09-28)
checked: crate-dependents (not current owner of `arbitrary`), book/course/talk/post

## freyja-moth
name: Freyja-moth
identity: https://github.com/Freyja-moth — no display name given, but the handle owns real, verifiable crates.io crates matching the GitHub account
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `bevy_monitors` on crates.io; 4 real reverse dependents — https://crates.io/api/v1/crates/bevy_monitors/reverse_dependencies?per_page=1 (2026-09-28)
- production: 7 merged PRs into bevyengine/bevy (2045 real reverse dependents on the `bevy` crate) — https://github.com/bevyengine/bevy/pulls?q=is%3Apr+is%3Amerged+author%3AFreyja-moth (2026-09-28)
influence:
- crate `bevy_monitors`, 4 dependent crates, confirmed sole owner — https://crates.io/api/v1/crates/bevy_monitors/owners (2026-09-28)
- 7 merged pull requests into bevyengine/bevy, a crate with 2045 dependents — https://crates.io/api/v1/crates/bevy/reverse_dependencies?per_page=1 (2026-09-28)
checked: role, book/course/talk/post

## friedel-ziegelmayer-r-diger-klaehn-iroh-n0-computer
name: Friedel Ziegelmayer & Rüdiger Klaehn (iroh/n0 computer)
identity: https://github.com/dignifiedquire (Friedel Ziegelmayer) and https://github.com/rklaehn (Rüdiger Klaehn, bio "Old grumpy hacker... Independent hacker") — both confirmed real GitHub identities matching the display name
type: builder
verdict: MEETS
track_record:
- crate-dependents: dignifiedquire is confirmed owner of `iroh` on crates.io; 276 real reverse dependents — https://crates.io/api/v1/crates/iroh/reverse_dependencies?per_page=1 (2026-09-28)
- production: rklaehn has 314 merged PRs into n0-computer/iroh — https://github.com/n0-computer/iroh/pulls?q=is%3Apr+is%3Amerged+author%3Arklaehn (2026-09-28)
influence:
- crate `iroh`, 276 dependent crates, owner dignifiedquire (team github:n0-computer:iroh-publisher co-owns) — https://crates.io/api/v1/crates/iroh/owners (2026-09-28)
- 314 merged PRs by rklaehn into the iroh core repo — https://github.com/n0-computer/iroh (2026-09-28)
checked: role (neither found as a public member of n0-computer's public org member list, though both are clearly core to the project by commit/ownership record), book/course/talk/post

## frostie314159
name: Simon Neuenhausen (Frostie314159)
identity: https://github.com/Frostie314159 (name: "Simon Neuenhausen", bio: "I like writing code in Rust...")
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `ether-type` on crates.io; 3 real reverse dependents — https://crates.io/api/v1/crates/ether-type/reverse_dependencies?per_page=1 (2026-09-28)
- production: 9 merged PRs into esp-rs/esp-hal (116 real reverse dependents on `esp-hal`) — https://github.com/esp-rs/esp-hal/pulls?q=is%3Apr+is%3Amerged+author%3AFrostie314159 (2026-09-28)
influence:
- crate `ether-type`, 3 dependent crates, confirmed owner — https://crates.io/api/v1/crates/ether-type/owners (2026-09-28)
- 9 merged PRs into esp-rs/esp-hal, a crate with 116 dependents — https://crates.io/api/v1/crates/esp-hal/reverse_dependencies?per_page=1 (2026-09-28)
checked: role, book/course/talk/post

## gbj
name: Greg Johnston (gbj)
identity: https://github.com/gbj (name: "Greg Johnston")
type: builder
verdict: MEETS
track_record:
- crate-dependents: co-owns `leptos` on crates.io (with benwis); 472 real reverse dependents — https://crates.io/api/v1/crates/leptos/reverse_dependencies?per_page=1 (2026-09-28)
influence:
- crate `leptos`, 472 dependent crates, confirmed co-owner — https://crates.io/api/v1/crates/leptos/owners (2026-09-28)
checked: production, role, book/course/talk/post (not separately verified beyond crate ownership)

## gbj-greg-johnston-leptos-creator
name: gbj (Greg Johnston, Leptos creator)
identity: https://github.com/gbj — same person as the `gbj` Voice above
type: builder
verdict: MEETS
track_record:
- crate-dependents: co-owns `leptos`; 472 real reverse dependents — https://crates.io/api/v1/crates/leptos/reverse_dependencies?per_page=1 (2026-09-28)
influence:
- same as `gbj`: crate `leptos`, 472 dependents — https://crates.io/api/v1/crates/leptos/owners (2026-09-28)
checked: production, role, book/course/talk/post

## glademiller
name: Glade Miller (glademiller)
identity: https://github.com/glademiller (name: "Glade Miller")
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `openapiv3` on crates.io (13,286,696 total downloads); 185 real reverse dependents — https://crates.io/api/v1/crates/openapiv3/reverse_dependencies?per_page=1 (2026-09-28)
- production: 4 merged PRs into actix/actix-web (1723 real reverse dependents on `actix-web`) — https://github.com/actix/actix-web/pulls?q=is%3Apr+is%3Amerged+author%3Aglademiller (2026-09-28)
influence:
- crate `openapiv3`, 185 dependent crates, confirmed sole owner — https://crates.io/api/v1/crates/openapiv3/owners (2026-09-28)
checked: role, book/course/talk/post

## graham-king
name: Graham King
identity: https://github.com/grahamking (name: "Graham King", blog: http://darkcoding.net — matches Source domain exactly)
type: builder
verdict: MEETS
track_record:
- book/course/talk/post: the post itself (rust-systemd-memory-remains) is linked from This Week in Rust, issue 2024-01-17 — https://github.com/rust-lang/this-week-in-rust/blob/main/content/2024-01-17-this-week-in-rust.md (2024-01-17)
influence:
- TWiR-linked post on a custom persistent-memory Rust allocator; GitHub account (company: NVIDIA) — https://darkcoding.net/software/rust-systemd-memory-remains/ (2024-01-17)
checked: crate-dependents, production, role

## graydon2-graydon-hoare-rusts-original-language-designer
name: Graydon Hoare (graydon2)
identity: https://old.reddit.com/user/graydon2 (via Wayback Machine snapshot) — the account speaks in the first person as Rust's designer: "Rust's bootstrap compiler was in OCaml... my preference is for non-GC-centered languages... I was targeting a niche I knew to be GC hostile," matching Graydon Hoare's well-documented authorship of Rust. GitHub account https://github.com/graydon (name: "Graydon Hoare") is the same real person, though GitHub does not itself confirm the reddit handle
type: language-designer
verdict: MEETS
track_record:
- role: Rust's original language designer, self-testifying at length about design decisions on the bootstrap compiler and GC policy — https://web.archive.org/web/20251219122448/https://old.reddit.com/user/graydon2 (2026-09-28, snapshot dated; underlying comments ~2026-08)
influence:
- widely quoted originator of Rust's design philosophy; this Voice's Claim itself was surfaced via a "TWiR quote of the week" thread — https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (2015-06-29)
checked: crate-dependents, production, book/course/talk/post (not separately checked; role evidence alone is dispositive)

## gregstoll
name: Greg Stoll (gregstoll)
identity: https://github.com/gregstoll (name: "Greg Stoll", company "@mozilla", blog gregstoll.com)
type: builder
verdict: MEETS
track_record:
- book/course/talk/post: the post itself (floating-point-to-hex-converter, Rust+WebAssembly rewrite) is linked from This Week in Rust, issue 2025-01-08 — https://github.com/rust-lang/this-week-in-rust/blob/main/content/2025-01-08-this-week-in-rust.md (2025-01-08)
influence:
- TWiR-linked post; Mozilla employee (per GitHub profile), though the post itself is framed as a personal/hobby project, not employer production work — https://gregstoll.wordpress.com/2025/01/08/floating-point-to-hex-converter-now-supports-16-bit-floats-plus-i-rewrote-it-in-rust-and-webassembly/ (2025-01-08)
checked: crate-dependents, production (Mozilla employment confirmed but not tied to this Rust work), role

## guy-bedford-hood-chatham-and-logan-gatlin
name: Guy Bedford, Hood Chatham, and Logan Gatlin
identity: Guy Bedford = https://github.com/guybedford (name "Guy Bedford", company "Cloudflare"); Hood Chatham = https://github.com/hoodmane (name "Hood Chatham", well-known Pyodide maintainer); Logan Gatlin = https://github.com/logan-gatlin (bio "Systems Engineer at Cloudflare")
type: builder
verdict: MEETS
track_record:
- production: all three tied to Cloudflare (Guy Bedford and Logan Gatlin by GitHub company field; blog post itself is on blog.cloudflare.com) shipping Rust panic=unwind support for Cloudflare Workers — https://blog.cloudflare.com/making-rust-workers-reliable/ (2026-04-22)
- crate-dependents: Guy Bedford owns `wasm-bindgen` on crates.io; 5393 real reverse dependents — https://crates.io/api/v1/crates/wasm-bindgen/reverse_dependencies?per_page=1 (2026-09-28)
influence:
- shipped panic=unwind for wasm-bindgen/Rust Workers, flagged in Rust Workers 0.8.0 — https://blog.cloudflare.com/making-rust-workers-reliable/ (2026-04-22)
- crate `wasm-bindgen`, 5393 dependent crates, Guy Bedford confirmed co-owner — https://crates.io/api/v1/crates/wasm-bindgen/owners (2026-09-28)
checked: role, book/course/talk/post

## guy-bedford-hood-chatham-and-logan-gatlin-cloudflare
name: Guy Bedford, Hood Chatham, and Logan Gatlin (Cloudflare Workers/wasm-bindgen team)
identity: same three people as the Voice above, same ties
type: builder
verdict: MEETS
track_record:
- production: same Cloudflare Workers panic=unwind shipment — https://blog.cloudflare.com/making-rust-workers-reliable/ (2026-04-22)
- crate-dependents: Guy Bedford owns `wasm-bindgen`; 5393 real reverse dependents — https://crates.io/api/v1/crates/wasm-bindgen/reverse_dependencies?per_page=1 (2026-09-28)
influence:
- same as the non-Cloudflare-suffixed Voice above
checked: role, book/course/talk/post

## guybedford
name: Guy Bedford
identity: https://github.com/guybedford (name "Guy Bedford", company "Cloudflare", blog guybedford.com, twitter guybedford)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `wasm-bindgen` on crates.io (with RReverser, daxpedda, and the wasm-bindgen-publish team); 5393 real reverse dependents — https://crates.io/api/v1/crates/wasm-bindgen/reverse_dependencies?per_page=1 (2026-09-28)
- role: author of active RFC #3987 ("RFC: Externref lang item for Wasm targets") on rust-lang/rfcs — https://github.com/rust-lang/rfcs/pull/3987 (2026-07-29)
influence:
- crate `wasm-bindgen`, 5393 dependent crates, confirmed co-owner — https://crates.io/api/v1/crates/wasm-bindgen/owners (2026-09-28)
- open RFC proposing a new Wasm externref type for Rust, actively discussed — https://github.com/rust-lang/rfcs/pull/3987 (2026-07-30)
checked: production (Cloudflare employer confirmed but not separately tied to this specific RFC), book/course/talk/post

## hannah-wang-ben-yang-and-fisher-darling
name: Hannah Wang, Ben Yang, and Fisher Darling
identity: Hannah Wang = official Cloudflare author page https://blog.cloudflare.com/author/hannah-wang/ ; Ben Yang = https://blog.cloudflare.com/author/ben-yang/ ; Fisher Darling = https://github.com/fisherdarling (bio "Systems Engineer at @cloudflare... interests are Rust, Cybersecurity, cloud architecture")
type: builder
verdict: MEETS
track_record:
- production: all three are Cloudflare staff (per official Cloudflare author pages and Fisher Darling's GitHub bio) who built and shipped `pvcli`, a Rust CLI for OHTTP/CONNECT/MASQUE/Privacy Pass — https://blog.cloudflare.com/open-sourcing-our-privacy-proxy-cli/ (2026-07-27)
influence:
- Cloudflare-employed builders of a released Rust tool, `pvcli` — https://blog.cloudflare.com/open-sourcing-our-privacy-proxy-cli/ (2026-07-27)
checked: crate-dependents, role, book/course/talk/post

## hannah-wang-ben-yang-fisher-darling-cloudflare
name: Hannah Wang, Ben Yang, Fisher Darling (Cloudflare)
identity: same three people and ties as the Voice above
type: builder
verdict: MEETS
track_record:
- production: same pvcli shipment at Cloudflare — https://blog.cloudflare.com/open-sourcing-our-privacy-proxy-cli/ (2026-07-27)
influence:
- same as the non-suffixed Voice above
checked: crate-dependents, role, book/course/talk/post

## haricot
name: Nicolas Pascal (haricot)
identity: https://github.com/haricot (name: "Nicolas PASCAL")
type: unset
verdict: FAILS
track_record: none found
influence: none found
checked: crate-dependents (no crates.io account exists for this login — https://crates.io/api/v1/users/haricot returns "Not Found", checked 2026-09-28), production (no employer/production evidence found; his own non-fork repos are Django/Jetson tooling in Shell/Python, not Rust), role (no Rust project team page found), book/course/talk/post (no blog, talk or course found; the single Claim is one PR-review comment, with 1 merged PR total into huggingface/candle — not itself a post)

## hecrj
name: Héctor (hecrj)
identity: https://github.com/hecrj (name: "Héctor", bio "I play code and write games.")
type: builder
verdict: MEETS
track_record:
- crate-dependents: sole owner of `iced` on crates.io; 384 real reverse dependents — https://crates.io/api/v1/crates/iced/reverse_dependencies?per_page=1 (2026-09-28)
influence:
- crate `iced`, a widely used Rust GUI framework, 384 dependent crates, confirmed sole owner — https://crates.io/api/v1/crates/iced/owners (2026-09-28)
checked: production, role, book/course/talk/post (not separately verified beyond crate ownership)

## howardjohn
name: John Howard (howardjohn)
identity: https://github.com/howardjohn (name "John Howard", bio "Istio and Agentgateway @ Solo.io", blog blog.howardjohn.info — matches Source domain)
type: builder
verdict: MEETS
track_record:
- production: authored the CEL-evaluation optimization post for Agentgateway (a Solo.io product), explicitly building Rust in production: "When building out Agentgateway, we had a desire to introduce an embedded expression language..." — https://blog.howardjohn.info/posts/cel-fast/ (2026-03-04)
influence:
- Rust performance work shipped in Agentgateway at Solo.io, 60% real-workload throughput gain (250K→400K QPS) cited in the post — https://blog.howardjohn.info/posts/cel-fast/ (2026-03-04)
checked: crate-dependents, role, book/course/talk/post (post itself found no TWiR/HN/Lobsters engagement signal in this pass, but production kind already meets)

## hsivonen
name: Henri Sivonen (hsivonen)
identity: https://github.com/hsivonen (name "Henri Sivonen", company "@mozilla", blog hsivonen.fi)
type: builder
verdict: MEETS
track_record:
- crate-dependents: sole owner of `encoding_rs` on crates.io; 1283 real reverse dependents — https://crates.io/api/v1/crates/encoding_rs/reverse_dependencies?per_page=1 (2026-09-28)
- production: Mozilla employee (per GitHub profile), `encoding_rs` ships in Firefox — https://github.com/hsivonen (2026-09-28)
influence:
- crate `encoding_rs`, used by Firefox and 1283 dependent crates, confirmed sole owner — https://crates.io/api/v1/crates/encoding_rs/owners (2026-09-28)
checked: role, book/course/talk/post
