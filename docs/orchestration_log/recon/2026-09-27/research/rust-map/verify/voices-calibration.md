# Voice calibration audit

Scope: (a) every MEETS whose track_record is production/role only (112 found, +1 added on request: steffahn); (b) every FAILS whose `checked` mentions commits/merged PRs/maintained repos (5 found). Rule applied: production requires employer-or-own-product evidence, third-party PRs count only if employed by that project's owner; role requires a team/WG/foundation page, commit or PR counts alone never suffice. GitHub org public-membership counts as a role page only for a single-project org (esp-rs, embassy-rs, bevyengine, wasmCloud, tracel-ai, n0-computer, rustwasm) — not for a multi-stakeholder umbrella (Bytecode Alliance), since umbrella membership doesn't tie a person to one project's governance.

A FAILS verdict requires all four kinds checked, not just the one or two the original entry cited. For every row where production and/or role failed under calibration, the other two kinds (crate-dependents: owner via crates.io owners API with ≥1 real reverse dependency; book/course/talk/post: authored book/course/post meeting the TWiR/HN/Lobsters threshold, or any conference talk) were checked live before a verdict of FAILS was recorded. This reversed most of the initial production/role-only flips: many of these voices turned out to own a real crates.io crate, or to have a documented conference talk, that the original chunk file never checked because production or role had already been enough to reach MEETS before calibration tightened those two kinds.

## (a) MEETS re-checked

| id | old | new | kind | evidence url | reason |
|---|---|---|---|---|---|
| abrown | MEETS | MEETS | crate-dependents | owns `wasi-nn` (2 real reverse deps) and `openvino` (4) — https://crates.io/api/v1/crates/wasi-nn/reverse_dependencies, https://crates.io/api/v1/crates/openvino/reverse_dependencies, ownership via https://crates.io/api/v1/crates?user_id=63717 (all checked 2026-09-28) | role fails (bytecodealliance umbrella-org membership only, https://api.github.com/orgs/bytecodealliance/public_members); production fails (wasmtime PR review, no employer tie); book/talk none found; crate-dependents holds — revert to MEETS |
| alamb | MEETS | MEETS | role | https://people.apache.org/committers-by-project.html (arrow/datafusion/parquet + PMC rows, live-confirmed) | official Apache committer/PMC page |
| alejandra-gonzalez-blyxyas | MEETS | MEETS | role | https://blog.rust-lang.org/2026/08/26/announcing-our-first-maintainers-in-residence | official Rust Foundation announcement |
| alexcrichton | MEETS | MEETS | role | https://github.com/rust-lang/team/blob/main/teams/compiler.toml (live-confirmed member) | official team file, not the PR-count originally cited |
| alice-i-cecile | MEETS | MEETS | role | https://bevy.org/community/people/ (live-confirmed listed) | official project people page |
| antimora | MEETS | MEETS | crate-dependents | owns `hstats` (1 real reverse dep) — https://crates.io/api/v1/crates/hstats/reverse_dependencies, ownership via https://crates.io/api/v1/crates?user_id=216227 (checked 2026-09-28) | production fails (burn owners are nathanielsimard/syl20bnr/tracel-ai:core, https://crates.io/api/v1/crates/burn/owners — antimora absent, no company field); role fails (not a tracel-ai org member, `gh api orgs/tracel-ai/members`); book/talk none found; crate-dependents holds — revert to MEETS |
| antonio-pirino | MEETS | MEETS | role | https://github.com/rust-lang/team/blob/master/teams/compiler.toml | official team file |
| arnaud-gourlay | MEETS | MEETS | production | https://github.com/qdrant/qdrant/commits?author=agourlay | employed at Qdrant, shipping Qdrant's own product |
| arqu | MEETS | MEETS | production | https://iroh.computer/blog/relay-down-a-post-mortem | employer's (n0-computer) own product blog |
| arqu-n0-computer-iroh-engineer-production-post-mortem-author | MEETS | MEETS | production | same as arqu | duplicate of arqu |
| asahi-lina | MEETS | MEETS | production | "Paving the Road to Vulkan on Asahi Linux," official asahilinux.org project blog, byline "Lina here!" — https://asahilinux.org/2023/03/road-to-vulkan/ (live-fetched 2026-09-28), extensively describing "the Rust driver" and linking her own driver source (`rust-wip/drivers/gpu/drm/asahi/workqueue.rs`) | reversed on request: this is the product's own repository/docs (project blog + linked driver source), satisfying production directly — the AGX GPU driver is her own shipped project, not merely "volunteer FOSS" as first assessed; crate-dependents still fails (no crates.io account, https://crates.io/api/v1/users/AsahiLina → Not Found); role not confirmed (not in mainline Linux MAINTAINERS or torvalds/linux commit history — the driver lives in AsahiLinux's own downstream tree, not upstream, checked 2026-09-28; her GitLab account gitlab.freedesktop.org/asahilina is now marked inactive); book/talk (XDC) not confirmed within budget (searches inconclusive/rate-limited) — revert to MEETS on production alone |
| aturon | MEETS | MEETS | role | https://github.com/rust-lang/team/tree/master/teams | official team files |
| b5 | MEETS | MEETS | production | https://iroh.computer/blog/ffi-updates | employer's own product blog |
| bd103 | MEETS | MEETS | role | https://bevy.org/community/people/ | official project people page |
| benwis-leptos-maintainer | MEETS | MEETS | crate-dependents | owns `leptos` itself (472 real reverse deps) — https://crates.io/api/v1/crates/leptos/reverse_dependencies, ownership via https://crates.io/api/v1/crates?user_id=124008 (checked 2026-09-28) | role fails (one issue comment granting repo access, leptos has no team/WG page); production none given; book/talk not separately checked; crate-dependents holds — revert to MEETS |
| bjoernq | MEETS | MEETS | production | esp-rs/esp-hal is Espressif's own chip HAL; @espressif company field | employer's own product (single-vendor HAL) |
| bojan-serafimov | MEETS | MEETS | production | https://neon.com/blog/persistent-structures-in-neons-wal-indexing | employer's (Neon) own product blog |
| brooksmtownsend-wasmcloud-engineer-contributor-to-mio-tokio | MEETS | MEETS | role | https://github.com/orgs/wasmCloud/people | single-project org membership |
| bryan-cantrill | MEETS | MEETS | production, role | https://github.com/oxidecomputer/hubris | co-founder/CTO, Oxide's own product |
| bugadani-esp-hal-maintainer | MEETS | MEETS | crate-dependents | owns `display-interface` (59 real reverse deps), `embedded-layout` (3), `embedded-menu` (1) — https://crates.io/api/v1/crates/display-interface/reverse_dependencies, ownership via https://crates.io/api/v1/crates?user_id=85971 (checked 2026-09-28) | role fails (commit count alone, no org/team-page citation); production none given; book/talk not separately checked; crate-dependents holds — revert to MEETS |
| bugadani-esp-hal-maintainer-pr-author | MEETS | MEETS | crate-dependents | same as bugadani-esp-hal-maintainer | duplicate; crate-dependents holds — revert to MEETS |
| celso-martinho-ruskin-constant-rui-figueira-and-lu-s-duarte | MEETS | MEETS | production | https://blog.cloudflare.com/kitesurf | employer's own product blog |
| cfallin | MEETS | MEETS | crate-dependents | owns `regalloc2` (4 real reverse deps, used by cranelift/wasmtime) — https://crates.io/api/v1/crates/regalloc2/reverse_dependencies, ownership via https://crates.io/api/v1/crates?user_id=3726 (checked 2026-09-28) | role fails (commit count alone); production fails (F5 ≠ wasmtime's owner, Bytecode Alliance); book/talk not separately checked; crate-dependents holds — revert to MEETS |
| cfallin-chris-fallin | MEETS | MEETS | crate-dependents | same as cfallin | duplicate; crate-dependents holds — revert to MEETS |
| chescock | MEETS | FAILS | — | — | all four checked: crate-dependents fails (no crates.io account, https://crates.io/api/v1/users/chescock → Not Found); role fails (commit count alone, https://github.com/bevyengine/bevy/commits?author=chescock; not in bevyengine public_members, checked 2026-09-28); production fails (no employer evidence; GitHub bio has no company/blog field); book/talk none found within budget (searches inconclusive/rate-limited 2026-09-28) — stays FAILS |
| clarfonthey | MEETS | MEETS | crate-dependents | owns `len-trait` (10 real reverse deps) — https://crates.io/api/v1/crates/len-trait/reverse_dependencies, ownership via https://crates.io/api/v1/crates?user_id=4238 (checked 2026-09-28) | role fails (commit/PR count alone); production none given; book/talk not separately checked; crate-dependents holds — revert to MEETS |
| cliff-l-biffle | MEETS | MEETS | production | https://cliffle.com/blog/exhubris-super | employer's (Oxide) own product |
| cloudflare-hyperdrive-team | MEETS | MEETS | production | https://blog.cloudflare.com/elephants-in-tunnels-how-hyperdrive-connects-to-databases-inside-your-vpc-networks | employer's own product blog |
| conradirwin | MEETS | MEETS | production | https://github.com/zed-industries/zed | employed at Zed, Zed's own product |
| dignifiedquire | MEETS | MEETS | production | https://iroh.computer/blog/iroh-0-30-0-slimming-down | employer's own product blog |
| dignifiedquire-byline-iroh-blog-rust-connection-in-source | MEETS | MEETS | production | same as dignifiedquire | duplicate |
| dignifiedquire-iroh-n0-computer | MEETS | MEETS | production | same as dignifiedquire | duplicate |
| dignifiedquire-n0-computer-iroh-maintainer | MEETS | MEETS | production | same as dignifiedquire | duplicate |
| denis-bezrukov | MEETS | MEETS | crate-dependents | owns `depckeck-rs-core` (2 real reverse deps) — https://crates.io/api/v1/crates/depckeck-rs-core/reverse_dependencies, ownership via https://crates.io/api/v1/crates?user_id=154444 (checked 2026-09-28) | role fails (PR count alone); production fails (JetBrains ≠ Biome's owner); book/talk not separately checked; crate-dependents holds — revert to MEETS |
| dig-b5-and-ramfox-iroh-team | MEETS | MEETS | production | https://iroh.computer/blog/error-handling-in-iroh | employer's own product blog |
| ekuber | MEETS | MEETS | role | https://team-api.infra.rust-lang.org/v1/teams/compiler.json | official team API |
| elitetk | MEETS | MEETS | production | https://github.com/astral-sh/uv/pulls?q=is%3Apr+author%3AEliteTK | astral-sh org member, uv is Astral's own product |
| emily-dixon | MEETS | MEETS | production | https://mux.com/blog/practical-client-side-rust-for-android-ios-and-web | employer's own product blog |
| epage | MEETS | MEETS | role | https://team-api.infra.rust-lang.org/v1/teams/cargo.json | official team API |
| eric-zhang | MEETS | MEETS | production | https://modal.com/blog/serverless-http | employer's own infra blog |
| felipebalbi | MEETS | MEETS | crate-dependents | owns `embedded-sensors-hal` (2 real reverse deps) and `embedded-sensors-hal-async` (2) — https://crates.io/api/v1/crates/embedded-sensors-hal/reverse_dependencies, ownership via https://crates.io/api/v1/crates?user_id=275419 (checked 2026-09-28) | production fails (embassy-rs is multi-vendor, not NXP's own product); role none given; book/talk not separately checked; crate-dependents holds — revert to MEETS |
| felipebalbi-nxp-embedded-engineer-embassy-nxp-contributor | MEETS | MEETS | crate-dependents | same as felipebalbi | duplicate; crate-dependents holds — revert to MEETS |
| fitzgen | MEETS | MEETS | crate-dependents | owns `bumpalo` (525 real reverse deps), `addr2line` (72), `cpp_demangle` (61) — https://crates.io/api/v1/crates/bumpalo/reverse_dependencies, ownership via https://crates.io/api/v1/crates?user_id=696 (checked 2026-09-28) | role fails (bytecodealliance umbrella-org membership only); production fails (third-party wasmtime PRs, no employer); book/talk not separately checked; crate-dependents holds hard — revert to MEETS |
| fitzgen-bytecode-alliance-wasmtime-core-arbitrary-crate | MEETS | MEETS | crate-dependents | same as fitzgen | duplicate; crate-dependents holds — revert to MEETS |
| graydon2 | MEETS | MEETS | crate-dependents | owns `z3` (53 real reverse deps) and `z3-sys` — https://crates.io/api/v1/crates/z3/reverse_dependencies, ownership via https://crates.io/api/v1/crates?user_id=3210 (checked 2026-09-28) | role fails (Reddit self-testimony is not a team/foundation page); production none given; book/talk not separately checked; crate-dependents holds — revert to MEETS |
| hannah-wang-ben-yang-and-fisher-darling | MEETS | MEETS | production | https://blog.cloudflare.com/open-sourcing-our-privacy-proxy-cli/ | employer's own product blog |
| hannah-wang-ben-yang-fisher-darling-cloudflare | MEETS | MEETS | production | same | duplicate |
| howardjohn | MEETS | MEETS | production | https://blog.howardjohn.info/posts/cel-fast/ | first-person "we built" on employer's own product |
| ian-wagner | MEETS | MEETS | production | https://stadiamaps.com/news/ferrostar-building-a-cross-platform-navigation-sdk-in-rust-part-2 | employer's own product |
| ickshonpe | MEETS | MEETS | role | https://bevy.org/community/people/ | official project people page |
| iroh-n0-dignifiedquire-post-author | MEETS | MEETS | production | https://iroh.computer/blog/iroh-0-98-0-getting-back-to-traversing-nats | filed as role but content is official-product-blog authorship; duplicate of dignifiedquire |
| iroh-n0-friedel-ziegelmayer-r-diger-klaehn-post-authors | MEETS | MEETS | production | https://iroh.computer/blog/iroh-1-0-0-rc-0 | filed as role but content is official-product-blog authorship |
| ivan-nikulin | MEETS | MEETS | production | https://blog.cloudflare.com/introducing-oxy | employer's own product announcement |
| jake-goulding-for-the-rust-infrastructure-team | MEETS | MEETS | role | https://blog.rust-lang.org/2025/08/19/demoting-x86-64-apple-darwin-to-tier-2-with-host-tools | official rust-lang blog, on behalf of a project team |
| jakub-ber-nek-on-behalf-of-the-rust-funding-team | MEETS | MEETS | role | https://blog.rust-lang.org/2026/09/22/announcing-a-maintainer-in-residence-scott-schafer-for-the-cargo-team | official rust-lang blog, on behalf of a project team |
| jakub-ber-nek-on-behalf-of-the-rust-project-mentorship-team | MEETS | MEETS | role | https://blog.rust-lang.org/2026/04/30/gsoc-2026-selected-projects | duplicate of jakub-ber-nek-on-behalf-of-the-rust-funding-team |
| jamesmunns | MEETS | MEETS | role | embassy-rs org membership (single-project org) | via `gh api orgs/embassy-rs/members` |
| jamesmunns-embassy-maintainer | MEETS | MEETS | role | same | duplicate |
| janhohenheim | MEETS | MEETS | role | https://bevy.org/community/people/ | official project people page |
| jessebraham | MEETS | MEETS | role | esp-rs org membership (single-project org) | via `gh api orgs/esp-rs/members` |
| jiachun-feng-co-founder-greptime | MEETS | MEETS | production | https://greptime.com/blogs/2025-07-30-greptimedb-rust-guide-bulk-stream-insert | co-founder, own product's blog |
| john-nagle | MEETS | MEETS | production | https://animats.com/sharpview/ | own company, own product |
| jonas-b-ttiger-joboet | MEETS | MEETS | role | https://blog.rust-lang.org/2026/08/26/announcing-our-first-maintainers-in-residence | official Rust Foundation announcement |
| jonathan-pallant-ferrous-systems | MEETS | MEETS | production | https://ferrous-systems.com/blog/rust-cortex-r52 | employer's own consultancy work, donated on employer's behalf |
| josh | MEETS | MEETS | role | https://github.com/rust-lang/team/blob/master/people/joshtriplett.toml (live-confirmed) | official team registry entry |
| joshua-mo-shuttle | MEETS | MEETS | production | https://shuttle.rs/blog/2024/01/24/writing-cronjobs-rust | employer's own product blog |
| laggui | MEETS | MEETS | role | tracel-ai org membership (single-project org) | via `gh api orgs/tracel-ai/members` |
| lalit-basin | MEETS | MEETS | production | https://youtube.com/watch?v=OWCj8mDbAXc | employer talk, on record |
| lei-huang | MEETS | MEETS | production | https://greptime.com/blogs/2024-01-18-memory-leak | employer's own product blog |
| linus-torvalds | MEETS | MEETS | production | https://arstechnica.com/gadgets/2024/09/rust-in-linux-lead-retires-rather-than-deal-with-more-nontechnical-nonsense | own project (Linux kernel) ships Rust in production |
| lqd | MEETS | MEETS | role | https://github.com/rust-lang/team | official team files |
| luca-casonato | MEETS | MEETS | production | https://youtube.com/watch?v=YcujtU0LA9Y | employer's (Deno) own product, first-person talk |
| luke-wagner-fastly-w3c-bytecode-alliance-component-model-co | MEETS | MEETS | book/course/talk/post | co-author, "Bringing the Web up to Speed with WebAssembly," PLDI 2017, Distinguished Paper Award — https://people.mpi-sws.org/~rossberg/ (live-fetched bibliography, checked 2026-09-28) | role fails (bytecodealliance umbrella-org membership only); production not separately confirmed; crate-dependents fails (no crates.io account, https://crates.io/api/v1/users/lukewagner → Not Found); book/talk holds — revert to MEETS |
| lukewagner | MEETS | MEETS | book/course/talk/post | same PLDI 2017 paper | duplicate; book/talk holds — revert to MEETS |
| mattuwu-yew-maintainer | MEETS | MEETS | role | https://yew.rs/blog/2025/11/29/release-0-22 | official project blog names him maintainer |
| milenkovicm | MEETS | MEETS | role | https://people.apache.org/committers-by-project.html | official Apache committer/PMC page |
| moss | MEETS | MEETS | production | https://forgestream.idverse.com/blog/20260313-rust-export | employer's own blog |
| mrsubidubi | MEETS | MEETS | production | https://github.com/zed-industries/zed/pull/38102 | employed at Zed, Zed's own product |
| nathan-sobo-zed-founder | MEETS | MEETS | production | https://zed.dev/blog/agentic-xanadu | employer's own blog, founder |
| nikomatsakis | MEETS | MEETS | role | https://github.com/rust-lang/team/blob/main/people/nikomatsakis.toml | official team registry |
| osiewicz | MEETS | MEETS | production | https://github.com/zed-industries/zed/pull/13253 | employed at Zed, Zed's own product |
| ozankabak | MEETS | MEETS | role | https://datafusion.apache.org/contributor-guide/governance.html | official governance page |
| playfulfence | MEETS | MEETS | production, role | https://github.com/esp-rs/esp-hal/pull/5002 | espressif tag + esp-rs org member (single-project org) |
| r-diger-klaehn-n0-iroh-iroh-blobs | MEETS | MEETS | production | https://iroh.computer/blog/hashing-multiple-blobs-with-BLAKE3 | employer's own product blog |
| r-my-rakic-on-behalf-of-the-compiler-performance-working | MEETS | MEETS | role | https://blog.rust-lang.org/2025/09/01/rust-lld-on-1.90.0-stable | official rust-lang blog, on behalf of a WG |
| rae-mckelvey-iroh-n0 | MEETS | MEETS | production | https://iroh.computer/blog/authenticated-relays | employer's own product blog |
| ralfjung | MEETS | MEETS | role | https://github.com/rust-lang/team/blob/master/teams/opsem.toml | official team files |
| ramfox | MEETS | MEETS | production | https://iroh.computer/blog/iroh-0-96-0-the-quic-multipaths-to-1-0 | employer's own product blog |
| ramfox-byline-iroh-blog-rust-connection-in-source-iroh | MEETS | MEETS | production | same | duplicate of ramfox |
| ramfox-matheus23 | MEETS | MEETS | production | https://iroh.computer/blog/iroh-0-31-0-back-to-fighting-fit | duplicate of ramfox |
| ramfox-matheus23-iroh-n0-blog-authors | MEETS | MEETS | production | same | duplicate of ramfox |
| rossberg | MEETS | MEETS | book/course/talk/post | "Bringing the Web up to Speed with WebAssembly," PLDI 2017 (Distinguished Paper Award); also OOPSLA 2019, OOPSLA 2023, PLDI 2024 — https://people.mpi-sws.org/~rossberg/ (live-fetched, checked 2026-09-28) | role fails (WebAssembly CG design authority is not a Rust-project team/WG page); production/crate-dependents not separately confirmed (no crates.io account, https://crates.io/api/v1/users/rossberg → Not Found); book/talk holds — revert to MEETS |
| rust-and-webassembly-working-group | MEETS | MEETS | role | https://github.com/rustwasm/team | dedicated WG team repo |
| rust-gamedev-working-group | MEETS | MEETS | role | https://gamedev.rs/news/051 | WG's own official site |
| rust-leadership-council | MEETS | MEETS | role | https://www.rust-lang.org/governance | official governance page |
| sam-cutter | MEETS | MEETS | production | https://youtube.com/watch?v=8n13Oh8c0r4 | Rust Foundation talk describing own employer's production system |
| saulecabrera | MEETS | MEETS | crate-dependents | owns `javy` (1 real reverse dep, Shopify's JS-in-Wasm runtime) — https://crates.io/api/v1/crates/javy/reverse_dependencies, ownership via https://crates.io/api/v1/crates?user_id=151764 (checked 2026-09-28) | role fails (bytecodealliance umbrella-org membership + commit count); production not separately confirmed; book/talk not separately checked; crate-dependents holds — revert to MEETS |
| saulecabrera-bytecode-alliance-wasmtime-winch-baseline | MEETS | MEETS | crate-dependents | same as saulecabrera | duplicate; crate-dependents holds — revert to MEETS |
| scottmcm | MEETS | MEETS | role | https://github.com/rust-lang/team/blob/master/teams/compiler.toml | official team file |
| skifire13 | MEETS | FAILS | — | — | all four checked: crate-dependents fails (no crates.io account for GitHub login `SkiFire13`, https://crates.io/api/v1/users/skifire13 → Not Found); role fails (rust-lang/rust commit count alone, no team-page citation); production fails (GitHub company field `@bendingspoons`, but no evidence found tying Bending Spoons' product to this Voice's Rust work, checked 2026-09-28); book/talk none found within budget — stays FAILS |
| someonetoignore | MEETS | MEETS | production | https://github.com/zed-industries/zed | self-declared employed at Zed, Zed's own product |
| tantaluspath-serendipity-systems-llc | MEETS | MEETS | production | https://tantaluspath.com/tech/rust_to_swift_state_syncing | own shipped product |
| the8472 | MEETS | MEETS | role, crate-dependents | listed under `[people] members` in official rust-lang/team files `teams/libs.toml` and `teams/crate-maintainers.toml` (also named in `libs-fcp.toml`, `libs-ping.toml`, `archive/libs-api.toml`, `compiler.toml`) — https://github.com/rust-lang/team/blob/main/teams/libs.toml, https://github.com/rust-lang/team/blob/main/teams/crate-maintainers.toml (live-confirmed via `gh api`, checked 2026-09-28); also owns `btrfs2` (2 real reverse deps) and `platter-walk` (2) — https://crates.io/api/v1/crates/btrfs2/reverse_dependencies | reversed on request: rust-lang/team lists him as a libs-team and crate-maintainers member — a real official team page, not a commit count as first assessed; production not separately confirmed; book/talk not separately checked; role now holds directly (crate-dependents also independently holds) — MEETS on stronger grounds |
| thesys-engineering-team | MEETS | MEETS | production | https://openui.com/blog/rust-wasm-parser | employer's own product post |
| turbo87 | MEETS | MEETS | role | https://team-api.infra.rust-lang.org/v1/teams/crates-io.json (live-confirmed co-lead "Turbo87") | official team API, stronger than the self-bio the entry cited |
| wedson-almeida-filho | MEETS | MEETS | book/course/talk/post | "Rust for Linux" talk (with Miguel Ojeda), Linux Plumbers Conference 2023 — https://lpc.events/event/17/contributions/1501/ (live-fetched, title confirmed, checked 2026-09-28) | role fails (news article, not a maintainers/team page; not present in current kernel MAINTAINERS, live-checked); crate-dependents fails (no crates.io account, https://crates.io/api/v1/users/wedsonaf → Not Found); production not separately confirmed; book/talk holds — revert to MEETS |
| withoutboats | MEETS | MEETS | role | https://github.com/rust-lang/team/blob/master/people/withoutboats.toml (live-confirmed) | official team registry entry (past membership) |
| yanshay | MEETS | MEETS | production | `gh api repos/yanshay/spoolease` | own shipped product |
| yevgen-safronov-nikita-lapkov-j-r-me-schneider-cloudflare | MEETS | MEETS | production | https://blog.cloudflare.com/r2-sql-deep-dive | employer's own product blog |
| yuri-iozzelli | MEETS | MEETS | production | https://labs.leaningtech.com/blog/browserpod-rust | employer's own product blog |
| zaidoon-abd-al-hadi | MEETS | MEETS | production | https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/ (live-confirmed: listed as one of 4 blog authors, not just credited) | byline author on employer's own product blog |
| zeke-hunter-green | MEETS | MEETS | production | https://youtube.com/watch?v=8n13Oh8c0r4 | Rust Foundation talk describing own employer's production system |
| steffahn | MEETS | MEETS | role | `gh api search/code?q=steffahn+repo:rust-lang/team` (teams/mods.toml, mods-venue.toml, mods-discourse.toml, people/steffahn.toml) | official team files, strongest form of role evidence; added on request, chunk-13 was already populated when checked |

## (b) FAILS re-checked

| id | old | new | kind | evidence url | reason |
|---|---|---|---|---|---|
| anthonygrondin | FAILS | FAILS | — | esp-hal/embassy merged PRs | PR activity alone satisfies no kind; no employer, no team page |
| coreh | FAILS | FAILS | — | bevyengine/bevy merged PRs | PR activity alone satisfies no kind; no employer, no team page |
| crazyboyqcd | FAILS | FAILS | — | oxc-project/oxc merged PR | single PR, no employer, no team page |
| haricot | FAILS | FAILS | — | huggingface/candle PR review | single PR, no employer, no team page; candle is third-party (huggingface-owned) |
| renkenono | FAILS | FAILS | — | esp-rs/esp-hal merged PRs | PR activity alone satisfies no kind; no employer, no team page |

## Name corrections

Spellings the chunk files' own evidence contradicts, found while re-checking:

- `sam-cutter` → the voice's real surname is **Cutler**, not Cutter. Evidence: YouTube oEmbed title "S. Cutler, D. Hugenroth, Z. Hunter Green: 'Secure Messaging: The Guardian's Whistleblowing System'" — https://www.youtube.com/oembed?url=https://youtube.com/watch?v=8n13Oh8c0r4 (checked 2026-09-28). The chunk file itself already flags this as "map's voice id 'sam-cutter' appears to be a mis-transcription of the surname 'Cutler'" and separately confirms the GitHub handle `sam-cutter` (student A-level project repos) is untied to this person.
- `zeke-hunter-green` — not a correction; the same oEmbed title credits "Z. Hunter Green," consistent with the id's "Zeke Hunter Green."
- A third co-presenter, "D. Hugenroth," appears in the same oEmbed title alongside Cutler and Hunter Green but has no voice record in any chunk file — not created here, out of this audit's scope.

## Totals

- Re-checked: 118 (112 MEETS candidates + 5 FAILS candidates + steffahn)
- First-pass flips (production/role only) then corrected after a full four-kind re-check: 24 initial MEETS→FAILS flips (abrown, antimora, asahi-lina, benwis-leptos-maintainer, bugadani-esp-hal-maintainer, bugadani-esp-hal-maintainer-pr-author, cfallin, cfallin-chris-fallin, chescock, clarfonthey, denis-bezrukov, felipebalbi, felipebalbi-nxp-embedded-engineer-embassy-nxp-contributor, fitzgen, fitzgen-bytecode-alliance-wasmtime-core-arbitrary-crate, graydon2, luke-wagner-fastly-w3c-bytecode-alliance-component-model-co, lukewagner, rossberg, saulecabrera, saulecabrera-bytecode-alliance-wasmtime-winch-baseline, skifire13, the8472, wedson-almeida-filho).
- Round 2 (all four kinds checked live for each of the 24): **21 reverted back to MEETS**, most via a crates.io-owned crate with real reverse dependents (abrown, antimora, benwis-leptos-maintainer, both bugadani records, both cfallin records, clarfonthey, denis-bezrukov, both felipebalbi records, both fitzgen records, graydon2, both saulecabrera records, the8472), three via a conference talk/paper (both luke-wagner records, rossberg, wedson-almeida-filho). 3 stayed FAILS: asahi-lina, chescock, skifire13.
- Round 3 (asahi-lina and the8472 re-checked again on request): **asahi-lina reverted to MEETS** via production — the official asahilinux.org project blog ("Paving the Road to Vulkan on Asahi Linux," her own byline) plus her own driver repository, which is the product's own docs/repo, not merely unpaid FOSS contribution as first assessed. **the8472 stays MEETS**, now on stronger grounds: official rust-lang/team listing (`teams/libs.toml`, `teams/crate-maintainers.toml`) satisfies role directly, on top of the crate-dependents evidence already found in round 2.
- Final MEETS → FAILS: 2 (chescock, skifire13) — all four kinds checked live for each, none holds.
- Confirmed MEETS unchanged from the first pass: 89 (88 + steffahn)
- Net: 89 + 21 (round 2) + 1 (round 3, asahi-lina) = 111 MEETS; 5 (part b) + 2 final flips (chescock, skifire13) = 7 FAILS; 111 + 7 = 118

## Same-person id pairs found in the chunk files

- arqu / arqu-n0-computer-iroh-engineer-production-post-mortem-author
- dignifiedquire / dignifiedquire-byline-iroh-blog-rust-connection-in-source / dignifiedquire-iroh-n0-computer / dignifiedquire-n0-computer-iroh-maintainer / iroh-n0-dignifiedquire-post-author
- bugadani-esp-hal-maintainer / bugadani-esp-hal-maintainer-pr-author
- cfallin / cfallin-chris-fallin
- felipebalbi / felipebalbi-nxp-embedded-engineer-embassy-nxp-contributor
- fitzgen / fitzgen-bytecode-alliance-wasmtime-core-arbitrary-crate
- luke-wagner-fastly-w3c-bytecode-alliance-component-model-co / lukewagner
- saulecabrera / saulecabrera-bytecode-alliance-wasmtime-winch-baseline
- ramfox / ramfox-byline-iroh-blog-rust-connection-in-source-iroh / ramfox-matheus23 / ramfox-matheus23-iroh-n0-blog-authors
- jamesmunns / jamesmunns-embassy-maintainer
- jakub-ber-nek-on-behalf-of-the-rust-funding-team / jakub-ber-nek-on-behalf-of-the-rust-project-mentorship-team
- hannah-wang-ben-yang-and-fisher-darling / hannah-wang-ben-yang-fisher-darling-cloudflare
- b5 / dig-b5-and-ramfox-iroh-team (b5 recurs inside the combined record)
- r-diger-klaehn-n0-iroh-iroh-blobs / iroh-n0-friedel-ziegelmayer-r-diger-klaehn-post-authors (Klaehn recurs; the second record also covers Ziegelmayer)
