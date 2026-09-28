## bryan-cantrill
name: Bryan Cantrill
identity: https://github.com/bcantrill (bio: "Oxide Computer Company", blog dtrace.org/blogs/bmc) — untied to lobste.rs quoter, but the Voice is Cantrill himself (quoted via YouTube talk), not the poster
type: institution
verdict: MEETS
track_record:
- production: co-founder/CTO, Oxide Computer Company; Oxide's Hubris embedded OS is Rust (3616 stars) — https://github.com/oxidecomputer/hubris (checked 2026-09-28)
- role: CTO, Oxide Computer Company (Rust-first hardware/firmware company) — https://github.com/bcantrill (checked 2026-09-28)
influence:
- Widely cited "falling in love with Rust" essay, quoted in a Rust talk (youtu.be/HgtRAbE1nBM?t=2450) referenced on lobste.rs — https://lobste.rs/s/in8yn9 (2026, exact date not in source)
checked: crate-dependents (no personal crates.io ownership found), book/course/talk/post (not separately checked; production/role already MEETS)

## bsder
name: bsder
identity: untied
type: unset
verdict: UNKNOWN
track_record: none found
influence: none found
checked: crate-dependents, production, role, book/course/talk/post — all unreachable pending identity; lobste.rs profile fetch (lobste.rs/u/bsder.json) returned HTTP 429 (rate-limited) on repeated tries; a GitHub account "BSDer" exists but has no bio, 1 follower, 4 repos — not confirmable as the same handle (2026-09-28)

## bstrie-attribution-hedged-by-the-poster-themselves-im
name: unset — attribution itself is hedged ("I'm pretty sure it's @bstrie") by the poster (@carols10cents) in the cited source
identity: untied
type: unset
verdict: UNKNOWN
track_record: none found
influence: none found
checked: crate-dependents, production, role, book/course/talk/post — none checked; identity cannot be tied because the source itself only guesses the attribution (source: https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681, quoting "33:52 of Rusty Radio Episode 2")

## bugadani
name: Dániel Buga
identity: https://github.com/bugadani (bio "Always trying to reimplement the wheel.", 140 followers, 173 public repos) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: 1,344 authored commits to esp-rs/esp-hal, plus 5 PRs merged as author (#2128, #5296, #3510, #2546, #5744) — https://github.com/esp-rs/esp-hal/commits?author=bugadani (checked 2026-09-28)
- crate-dependents: esp-hal has real crates.io reverse dependents (e.g. esp-bootloader-esp-idf 0.6.0) — https://crates.io/api/v1/crates/esp-hal/reverse_dependencies (checked 2026-09-28); not the crates.io owner of record (owners: MabezDev, jessebraham, github:esp-rs:espressif)
influence:
- 1,344 commits to esp-hal, the primary Espressif embedded-Rust HAL — https://github.com/esp-rs/esp-hal/commits?author=bugadani (checked 2026-09-28)
checked: production (no separate employer-Rust evidence sought; role/crate-dependents already MEETS), book/course/talk/post (not checked)

## bugadani-esp-hal-maintainer
name: Dániel Buga (same person as bugadani; PR review comment on esp-hal identifies them as "esp-hal maintainer")
identity: https://github.com/bugadani (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: same as bugadani — 1,344 authored commits to esp-rs/esp-hal — https://github.com/esp-rs/esp-hal/commits?author=bugadani (checked 2026-09-28)
influence:
- see bugadani entry; esp-hal has confirmed real reverse dependents — https://crates.io/api/v1/crates/esp-hal/reverse_dependencies (checked 2026-09-28)
checked: crate-dependents (contributor, not listed owner), production, book/course/talk/post

## bugadani-esp-hal-maintainer-pr-author
name: Dániel Buga (same person; PR author role on esp-hal PR #5744)
identity: https://github.com/bugadani (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: authored and merged esp-hal PR #5744 — https://github.com/esp-rs/esp-hal/pull/5744 (merged; checked 2026-09-28)
influence:
- see bugadani entry
checked: crate-dependents (contributor, not listed owner), production, book/course/talk/post

## bunnybites
name: Bunny (bunnyBites)
identity: https://github.com/bunnyBites (10 followers, 78 public repos, no bio/real name given) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: 15 authored commits merged into DioxusLabs/dioxus, including PR #1610 (merged 2024-01-08) — https://github.com/DioxusLabs/dioxus/pull/1610 (checked 2026-09-28)
- crate-dependents: dioxus has 435 real crates.io reverse dependents — https://crates.io/api/v1/crates/dioxus/reverse_dependencies (checked 2026-09-28); not a listed crates.io owner
influence:
- 15 merged commits to Dioxus, a widely-depended Rust GUI framework — https://github.com/DioxusLabs/dioxus/commits?author=bunnyBites (checked 2026-09-28)
checked: production, book/course/talk/post

## burntsushi
name: Andrew Gallant
identity: https://github.com/BurntSushi (bio "I love to code.", 13,267 followers, blog burntsushi.net, company @openai) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- crate-dependents: crates.io owner of `regex` (owners: BurntSushi, rust-lang-owner, github:rust-lang-nursery:regex-owners) — https://crates.io/api/v1/crates/regex/owners (checked 2026-09-28)
influence:
- maintains regex, ripgrep and other foundational Rust crates with massive downstream use (per crates.io ownership above)
checked: production, role, book/course/talk/post — not separately checked (crate-dependents already MEETS)

## bushrat011899
name: Zachary Harrold
identity: https://github.com/bushrat011899 (27 followers, 88 public repos) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: 154 authored commits to bevyengine/bevy — https://github.com/bevyengine/bevy/commits?author=bushrat011899 (checked 2026-09-28)
- crate-dependents: bevy has 2,045 real crates.io reverse dependents — https://crates.io/api/v1/crates/bevy/reverse_dependencies (checked 2026-09-28); not a listed crates.io owner
influence:
- 154 merged commits to Bevy, a major Rust game engine — https://github.com/bevyengine/bevy/commits?author=bushrat011899 (checked 2026-09-28)
checked: production, book/course/talk/post

## cad97
name: Crystal Durham
identity: https://github.com/CAD97 (bio "Software engineer, programming languages nerd, @rust-lang enthusiast", company @canonical, 196 followers) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- crate-dependents: crates.io owner (user id 6845) of `erasable`, which has 9 real reverse dependents — https://crates.io/api/v1/crates/erasable/reverse_dependencies (checked 2026-09-28); also owns cad97-prelude, drop-take, cstr8, conformance, and others
influence:
- owns and maintains multiple published crates, incl. erasable (9 dependents) — https://crates.io/api/v1/crates?user_id=6845 (checked 2026-09-28)
checked: production, role, book/course/talk/post — not separately checked (crate-dependents already MEETS)

## caio-c410-f3r
name: Caio
identity: https://github.com/c410-f3r (bio present, 89 followers, 277 public repos; personal blog c410-f3r.github.io matches the cited source) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- crate-dependents: crates.io owner (user id 25891) of `cl-aux` (2 real reverse dependents) and `cl-traits` (3 real reverse dependents) — https://crates.io/api/v1/crates/cl-aux/reverse_dependencies, https://crates.io/api/v1/crates/cl-traits/reverse_dependencies (checked 2026-09-28)
influence:
- personal blog post comparing tokio/smol/glommio executor models under real HTTP workloads — https://c410-f3r.github.io/thoughts/work-stealing-vs-executor-per-thread-evaluating-different-http-server-workloads-with-tokio-smol-and-glommio (undated in source; not independently checked for TWiR/HN/Lobsters reach, unnecessary since crate-dependents already MEETS)
checked: production, role, book/course/talk/post reach bar — not separately checked

## cart
name: Carter Anderson
identity: https://github.com/cart (bio "Creator of Bevy Engine | GameDev | Programmer | Artist | Previously Senior Software Engineer at Microsoft", 2,005 followers, company @bevyengine) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- crate-dependents: sole listed personal owner of `bevy` on crates.io (owners: cart, github:bevyengine:publish), which has 2,045 real reverse dependents — https://crates.io/api/v1/crates/bevy/owners, https://crates.io/api/v1/crates/bevy/reverse_dependencies (checked 2026-09-28)
- role: creator and Project Lead of the Bevy game engine — https://github.com/cart (checked 2026-09-28)
influence:
- creator/lead of Bevy, a major Rust game engine with 2,045 real dependents; authored merged PR #17398 (merged 2025-01-18) — https://github.com/bevyengine/bevy/pull/17398 (checked 2026-09-28)
checked: production, book/course/talk/post — not separately checked (crate-dependents + role already MEETS)

## carter-anderson-cart-bevy-creator-and-project-lead
name: Carter Anderson (@cart, Bevy creator and Project Lead) — same real person as the `cart` Voice above
identity: https://github.com/cart (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- crate-dependents / role: identical to `cart` — crates.io owner of `bevy` (2,045 real reverse dependents), Project Lead — https://crates.io/api/v1/crates/bevy/owners (checked 2026-09-28)
influence:
- quoted in Bevy's own sixth-birthday announcement post — https://bevy.org/news/bevys-sixth-birthday (undated exact day in source; 2026)
checked: production, book/course/talk/post

## cbjamo
name: Caleb Jamison
identity: https://github.com/CBJamo (8 followers, 68 public repos) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: 92 authored commits to embassy-rs/embassy, incl. merged PR #3243 (merged 2024-08-12) — https://github.com/embassy-rs/embassy/pull/3243, https://github.com/embassy-rs/embassy/commits?author=CBJamo (checked 2026-09-28)
- crate-dependents: embassy-executor has 199 real crates.io reverse dependents — https://crates.io/api/v1/crates/embassy-executor/reverse_dependencies (checked 2026-09-28); not a listed crates.io owner
influence:
- 92 merged commits to Embassy, a widely-used async embedded Rust framework — https://github.com/embassy-rs/embassy/commits?author=CBJamo (checked 2026-09-28)
checked: production, book/course/talk/post

## cbournhonesque
name: Periwink (GitHub handle cBournhonesque)
identity: https://github.com/cBournhonesque (48 followers, 55 public repos) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns/maintains `lightyear`, a Bevy multiplayer-networking crate (1,161 GitHub stars) with 9 real crates.io reverse dependents — https://github.com/cBournhonesque/lightyear, https://crates.io/api/v1/crates/lightyear/reverse_dependencies (checked 2026-09-28)
- role: 45 authored commits to bevyengine/bevy — https://github.com/bevyengine/bevy/commits?author=cBournhonesque (checked 2026-09-28)
influence:
- maintains lightyear (9 real dependents) and contributes to Bevy core (45 commits)
checked: production, book/course/talk/post

## cecton
name: Cecile Tonglet
identity: https://github.com/cecton (bio "🦀 Rustacean", company @rustminded, 417 followers, blog cecton.com) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: 31 authored commits to yewstack/yew, a widely-depended Rust web framework (318 real crates.io reverse dependents) — https://github.com/yewstack/yew/commits?author=cecton, https://crates.io/api/v1/crates/yew/reverse_dependencies (checked 2026-09-28)
- crate-dependents: crates.io owner (user id 37119) of several published crates (aws-zip, dfu-core, cargo-git, etc.); reverse-dependent counts for these not individually verified
influence:
- contributes to Yew core; runs @rustminded, a Rust consultancy
checked: production, book/course/talk/post

## celso-martinho-ruskin-constant-rui-figueira-and-lu-s-duarte
name: Celso Martinho, Ruskin Constant, Rui Figueira, and Luís Duarte
identity: credited by name as authors on Cloudflare's own engineering blog — https://blog.cloudflare.com/kitesurf (checked via cache, 2026-09-28); no individual personal profile pages independently checked
type: institution
verdict: MEETS
track_record:
- production: named engineers at Cloudflare describing "Kitesurf," a production Cloudflare system; post mentions Rust 23 times — https://blog.cloudflare.com/kitesurf (checked 2026-09-28)
influence:
- authored a Cloudflare engineering blog post on a shipped production system built in Rust — https://blog.cloudflare.com/kitesurf (2026, exact day not captured)
checked: crate-dependents, role, book/course/talk/post — not checked (production already MEETS)

## cfallin
name: Chris Fallin
identity: https://github.com/cfallin (bio "Software engineer with a focus on compilers. Currently hacking on WebAssembly-related technologies at F5.", blog cfallin.org, company F5, 570 followers) (checked 2026-09-28)
type: language-designer
verdict: MEETS
track_record:
- role: 914 authored commits to bytecodealliance/wasmtime — https://github.com/bytecodealliance/wasmtime/commits?author=cfallin (checked 2026-09-28); wasmtime has 803 real crates.io reverse dependents — https://crates.io/api/v1/crates/wasmtime/reverse_dependencies (checked 2026-09-28)
- production: employed at F5 working on WebAssembly-related (Rust) technology per own GitHub bio
influence:
- 914 commits to Wasmtime/Cranelift, the reference WebAssembly runtime and compiler backend used across the ecosystem
checked: crate-dependents (not the crates.io owner of record; owners are bytecodealliance publish accounts), book/course/talk/post

## cfallin-chris-fallin
name: cfallin (Chris Fallin) — same real person as the `cfallin` Voice above
identity: https://github.com/cfallin (checked 2026-09-28)
type: language-designer
verdict: MEETS
track_record:
- role: same as cfallin — 914 authored commits to bytecodealliance/wasmtime — https://github.com/bytecodealliance/wasmtime/commits?author=cfallin (checked 2026-09-28)
influence:
- filed/discussed wasmtime issue #8573 as a recognized project contributor — https://github.com/bytecodealliance/wasmtime/issues/8573 (checked 2026-09-28)
checked: crate-dependents, production (already covered under cfallin), book/course/talk/post

## chayan-mistry
name: Chayan Mistry
identity: https://github.com/chayanforyou (bio "Software Engineer | Robotics Learner", company "Square Health Ltd.", 125 followers) — matches the Medium byline via the linked GitHub sample repo in the post (checked 2026-09-28)
type: unset
verdict: FAILS
track_record: none found
influence:
- personal Medium tutorial "Rust in Android Development: Complete Guide," 19 Medium followers, no evidence of wider syndication found — https://chayanmistry.medium.com/rust-in-android-development-complete-guide-5f3313f40e50 (2026-05-12)
checked: crate-dependents (no crates.io account found for chayanforyou or chayan-mistry — https://crates.io/api/v1/users/chayanforyou, checked 2026-09-28), production (no employer-Rust evidence found; Square Health Ltd. is not shown using Rust), role (none found), book/course/talk/post (post not linked from This Week in Rust; zero Hacker News hits for the URL or title — https://hn.algolia.com/api/v1/search?query=chayanmistry.medium.com, checked 2026-09-28; Lobsters not checked but no corroborating signal found)

## chescock
name: Chris Russell
identity: https://github.com/chescock (5 followers, 10 public repos) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: 102 authored commits to bevyengine/bevy — https://github.com/bevyengine/bevy/commits?author=chescock (checked 2026-09-28)
influence:
- 102 merged commits to Bevy core (2,045 real dependents) — https://crates.io/api/v1/crates/bevy/reverse_dependencies (checked 2026-09-28)
checked: crate-dependents (no personal crate ownership found), production, book/course/talk/post

## clarfonthey
name: Clar Fon
identity: https://github.com/clarfonthey (blog usr.ltdk.xyz, 78 followers, 125 public repos) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- role: 8 authored commits to bevyengine/bevy, incl. merged PR #15586 (merged 2024-10-07) — https://github.com/bevyengine/bevy/pull/15586 (checked 2026-09-28)
influence:
- merged contribution to Bevy core (2,045 real dependents)
checked: crate-dependents (no personal crate ownership checked), production, book/course/talk/post

## cliff-l-biffle
name: Cliff L. Biffle
identity: https://github.com/cbiffle (bio "I'm pretty into this stuff.", company "Oxide Computer", blog cliffle.com — matches the cited source domain, 767 followers) (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- production: employed at Oxide Computer; author of the "Hubris" writeup on his own blog, cliffle.com/blog/exhubris-super — https://cliffle.com/blog/exhubris-super (checked 2026-09-28); Hubris (oxidecomputer/hubris) is a real, public Rust embedded OS (3,616 GitHub stars)
- role: Oxide Computer engineer, creator/co-creator of the Hubris OS
influence:
- widely-read personal blog on embedded Rust systems (cliffle.com), cited directly by this map's Findings
checked: crate-dependents (no crates.io ownership checked), book/course/talk/post reach bar (not separately checked; production already MEETS)

## cloudflare-hyperdrive-team
name: Cloudflare (Hyperdrive team)
identity: official Cloudflare engineering blog post attributed to the Hyperdrive product team — https://blog.cloudflare.com/elephants-in-tunnels-how-hyperdrive-connects-to-databases-inside-your-vpc-networks (checked 2026-09-28); no individual named author in the fetched text
type: institution
verdict: MEETS
track_record:
- production: describes Hyperdrive, a live Cloudflare product; post mentions Rust 23 times — https://blog.cloudflare.com/elephants-in-tunnels-how-hyperdrive-connects-to-databases-inside-your-vpc-networks (checked 2026-09-28)
influence:
- Cloudflare engineering blog post on a production system built in Rust (2026, exact day not captured in cached text)
checked: crate-dependents, role, book/course/talk/post — not checked (production already MEETS)

## co-presenter-taj-touch-unclear
name: "Touch" (per the video transcript, not "Taj"), co-presenter alongside "Andrew," software engineer at Canva
identity: untied — first name only ("Touch"), no surname or profile page found in the transcript; web search budget was exhausted this session before a name-resolution search could run
type: unset
verdict: UNKNOWN
track_record: none found
influence:
- co-presented a Rust/WebAssembly performance talk with a Canva engineer named Andrew — https://youtube.com/watch?v=wDoqQkEylY8 (undated in transcript)
checked: crate-dependents, production, role, book/course/talk/post — all blocked by unresolved identity
