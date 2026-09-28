## mrsubidubi
name: Finn Evers (MrSubidubi)
identity: https://github.com/MrSubidubi — GitHub profile discloses name "Finn Evers", company "@zed-industries"; same account posts PR review comments directly in zed-industries/zed
type: builder
verdict: MEETS
track_record:
- production: reviews code in zed-industries/zed, a 60.5MB-Rust-dominant production codebase (Zed editor); GitHub profile lists company @zed-industries — https://github.com/zed-industries/zed/pull/38102 (2025-09-27); https://api.github.com/repos/zed-industries/zed/languages (checked 2026-09-28)
influence:
- (none found)
checked: crate-dependents (no crates.io account found), role (no team-page listing found beyond employer field).

## ms2ger
name: Ms2ger
identity: https://github.com/Ms2ger — GitHub profile (company @Igalia, created 2009, 344 followers), crates.io account (id 2155) tied to same GitHub login
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `group-by` crate, 1 real reverse dependency (`eson`) confirmed via owner_user — https://crates.io/api/v1/crates/group-by/reverse_dependencies (checked 2026-09-28)
influence:
- employed at Igalia (contracted browser-engine/Rust work, e.g. Servo) per GitHub company field — https://github.com/Ms2ger (2026-09-28)
checked: production, role, book/course/talk/post — not pursued once crate-dependents confirmed MEETS. Note: the claim's own `gap` field flags the track record as uncertain from the source alone (a 2015 IRC quote reposted by @bluss); the crates.io tie was found independently of that source.

## mtset
name: mtset
identity: untied
type: unset
verdict: UNKNOWN
track_record:
- (none found)
influence:
- (none found)
checked: crate-dependents, production, role, book/course/talk/post — all blocked on identity. Lobste.rs profile page (https://lobste.rs/u/mtset) would not render (too short to trust after retries). A GitHub account "MTset" exists but belongs to "Mark Tsikanovski," an IBM-assembler-era programmer whose bio has no connection to the lobste.rs comment; too weak a match to tie. The self-description "card-carrying RESF member" (Rust Evangelism Strike Force, an in-joke term, not a real org) gives no verifiable identity.

## musicalninjadad
name: MusicalNinjaDad
identity: https://github.com/MusicalNinjaDad — GitHub profile (Switzerland, bio "Dad, physicist, neurodivergent"), crates.io account (id 271012) tied to same login
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `build_safely`, 10 real reverse dependencies — https://crates.io/api/v1/crates/build_safely/reverse_dependencies (checked 2026-09-28)
influence:
- also owns `thread_safely` (1 dependent), `ninja-build_rs` (1 dependent), `proc_macro2_diagnostic` (2 dependents) — https://crates.io/api/v1/crates?user_id=271012 (2026-09-28)
checked: production, role, book/course/talk/post — not pursued once crate-dependents confirmed MEETS.

## n0-inc-iroh-services-post-by-rae-mckelvey
name: Rae McKelvey (n0, inc.)
identity: https://iroh.computer/blog/authenticated-relays — n0's own company blog, byline "July 30, 2026 by Rae McKelvey"
type: institution
verdict: MEETS
track_record:
- production: authored n0's official blog post on Iroh Services' managed-relay authentication, describing production infrastructure for the `iroh` crate — https://iroh.computer/blog/authenticated-relays (2026-07-30)
- crate-dependents: n0 maintains `iroh`, 276 real reverse dependencies on crates.io — https://crates.io/api/v1/crates/iroh/reverse_dependencies (checked 2026-09-28)
influence:
- iroh has 276 crates.io reverse dependents — https://crates.io/api/v1/crates/iroh/reverse_dependencies (2026-09-28)
checked: role, book/course/talk/post — not needed once production+crate-dependents confirmed MEETS. No independent GitHub/crates.io account found for "Rae McKelvey" specifically; credited via the employer-post byline only.

## n0-inc-iroh-team-post-by-ramfox
name: ramfox (Kasey, n0.computer)
identity: https://github.com/ramfox — GitHub profile (company "n0.computer", email kasey@n0.computer), confirmed public member of the n0-computer GitHub org
type: institution
verdict: MEETS
track_record:
- crate-dependents: n0-computer (ramfox's employer/org) maintains `iroh`, 276 real reverse dependencies; ramfox is a confirmed public member of the org — https://crates.io/api/v1/crates/iroh/reverse_dependencies (checked 2026-09-28); https://api.github.com/orgs/n0-computer/public_members (2026-09-28)
- production: authored official iroh changelog posts (iroh 0.23, 0.27) documenting shipped API changes in the `iroh`/`iroh-net` crates — https://iroh.computer/blog/iroh-0-23-welcoming-nodejs-to-the-family (2024-08-21); https://iroh.computer/blog/iroh-0-27-0-Squashing-Bugs-And-Taking-Names (2024-10-24)
influence:
- iroh has 276 crates.io reverse dependents — https://crates.io/api/v1/crates/iroh/reverse_dependencies (2026-09-28)
checked: role, book/course/talk/post — not needed once production+crate-dependents confirmed MEETS.

## n0-post-by-ramfox-matheus23-b5
name: ramfox, matheus23 (Philipp Krüger), b5 (Brendan O'Brien) — n0, inc.
identity: https://github.com/ramfox, https://github.com/matheus23, https://github.com/b5 — all three confirmed public members of the n0-computer GitHub org; matheus23 and b5 disclose real names (Philipp Krüger, Brendan O'Brien) on their GitHub profiles
type: educator
verdict: MEETS
track_record:
- production: co-authored n0's official tutorial on QUIC message framing with the `iroh::Endpoint` API, an n0-maintained crate shipped in production — https://iroh.computer/blog/message-framing-tutorial (2025-08-12)
- crate-dependents: n0-computer maintains `iroh`, 276 real reverse dependencies — https://crates.io/api/v1/crates/iroh/reverse_dependencies (checked 2026-09-28)
influence:
- iroh has 276 crates.io reverse dependents — https://crates.io/api/v1/crates/iroh/reverse_dependencies (2026-09-28)
checked: role, book/course/talk/post — not needed once production+crate-dependents confirmed MEETS.

## nadrieril
name: Nadrieril
identity: https://github.com/Nadrieril — GitHub profile (company "Inria", Paris, 136 followers), crates.io account (id 46178) tied to same login
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `pest_consume`, 20 real reverse dependencies — https://crates.io/api/v1/crates/pest_consume/reverse_dependencies (checked 2026-09-28)
influence:
- also owns `serde_dhall` (10 dependents), `dhall` (3 dependents) — https://crates.io/api/v1/crates?user_id=46178 (2026-09-28)
- employed at Inria (French national research institute) per GitHub profile — https://github.com/Nadrieril (2026-09-28)
checked: production, role, book/course/talk/post — not pursued once crate-dependents confirmed MEETS.

## nakedible
name: Nuutti Kotivuori (nakedible)
identity: https://github.com/nakedible — GitHub profile discloses name "Nuutti Kotivuori"; same account self-confirms in the source thread ("@nakedible is my primary open source account")
type: unset
verdict: FAILS
track_record:
- (none found)
influence:
- (none found)
checked: crate-dependents (owns `agentknock`, `datealgo`, `finfmt` on crates.io, all 0 reverse dependencies — https://crates.io/api/v1/crates?user_id=213166, checked 2026-09-28); production (personal blog https://nakedible.org states "Rust is my current passion" and describes a fintech/payments career, but names no specific employer shipping Rust in production); role (no Rust project/foundation team-page listing found); book/course/talk/post (personal blog only, no crate/book/course found, no TWiR/HN/Lobsters signal checked found for it).

## narsil
name: Nicolas Patry (Narsil)
identity: https://github.com/Narsil — GitHub profile discloses name "Nicolas Patry", company "@huggingface", 859 followers; crates.io account (id 79201) tied to same login
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `candle-core` (Hugging Face's Rust ML framework), 617 real reverse dependencies — https://crates.io/api/v1/crates/candle-core/reverse_dependencies (checked 2026-09-28)
influence:
- employed at Hugging Face; also owns `candle-flash-attn`, `bindgen_cuda` and other candle-ecosystem crates — https://github.com/Narsil (2026-09-28)
checked: production, role, book/course/talk/post — not pursued once crate-dependents confirmed MEETS.

## nas-ceo-founder-rebel-author-developerlife-com-maintainer
name: Nazmul Idris ("Nas" — CEO/founder Rebel, developerlife.com)
identity: self-disclosed on camera ("Hi, I'm Nas. I'm the CEO and founder of Rebel and the author of developer life and maintainer of the Rebel, Dewey Crates") — cross-confirmed: developerlife.com's byline is "Nazmul Idris" and crates.io shows the r3bl_* crates (Rebel's product line) owned by GitHub user nazmulidris ("Nazmul Idris") — https://youtube.com/watch?v=K5SY-lc8nTE (2025-03-26); https://crates.io/api/v1/crates/r3bl_tui/owner_user (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `r3bl_tui`, 6 real reverse dependencies — https://crates.io/api/v1/crates/r3bl_tui/reverse_dependencies (checked 2026-09-28)
influence:
- (none found)
checked: production, role, book/course/talk/post — not pursued once crate-dependents confirmed MEETS. Note: this Voice and the separately-listed `nazmul-idris-r3bl-tui-maintainer` (this same chunk) are the same person under two different Voice ids — both self-disclosures and crates.io ownership point to Nazmul Idris / r3bl_tui.

## natalie-klestrup-r-ijezon-natkr
name: Natalie Klestrup Röijezon (natkr)
identity: https://natkr.com — personal blog, full name in page title ("natkr's ramblings"); GitHub account (natkr) exists but has 0 public repos, no crates.io account
type: educator
verdict: MEETS
track_record:
- book/course/talk/post: "Async from scratch 2: Wake me maybe" (the exact claimed source) is linked from This Week in Rust issue 2025-04-16 — https://natkr.com/2025-04-15-async-from-scratch-2/ ; https://github.com/rust-lang/this-week-in-rust/blob/main/content/2025-04-16-this-week-in-rust.md (checked 2026-09-28)
influence:
- the series' part 3 ("Async from scratch 3") reached 44 Hacker News points — https://news.ycombinator.com/item?id=44066237 (2025-05-22)
checked: crate-dependents (no crates.io account found), production, role — not pursued once book/course/talk/post confirmed MEETS.

## nathan-sobo-zed-founder
name: Nathan Sobo
identity: https://zed.dev/blog/agentic-xanadu — Zed's own company blog, byline "Nathan Sobo"; publicly known founder/CEO of Zed Industries
type: builder
verdict: MEETS
track_record:
- production: authored Zed's official company blog post discussing "Zed's own work" of the past decade; zed-industries/zed is a 60.5MB-Rust-dominant production codebase — https://zed.dev/blog/agentic-xanadu (2026-09-01); https://api.github.com/repos/zed-industries/zed/languages (checked 2026-09-28)
influence:
- (none found)
checked: crate-dependents, role, book/course/talk/post — not pursued once production confirmed MEETS. The post itself never uses the word "Rust"; the production tie rests on Zed's well-documented Rust codebase and Sobo's founder role, not on an explicit in-post statement.

## nathanielsimard
name: Nathaniel Simard
identity: https://github.com/nathanielsimard — GitHub profile discloses name "Nathaniel Simard", bio "CEO @tracel-ai - Building Burn"; crates.io account (id 17406) tied to same login
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `burn` (Tracel AI's ML framework), 324 real reverse dependencies — https://crates.io/api/v1/crates/burn/reverse_dependencies (checked 2026-09-28)
- production: authored Burn's official end-of-year blog post announcing Burn Central and CubeCL, and reviews Burn's own PRs — https://burn.dev/blog/burn-end-of-year-review (2025-12-19); https://github.com/tracel-ai/burn/pull/3792 (2025-10-09)
influence:
- burn has 324 crates.io reverse dependents — https://crates.io/api/v1/crates/burn/reverse_dependencies (2026-09-28)
checked: role, book/course/talk/post — not needed once crate-dependents+production confirmed MEETS.

## nazmul-idris-r3bl-tui-maintainer
name: Nazmul Idris
identity: https://github.com/nazmulidris — crates.io owner_user of `r3bl_tui`, name "Nazmul Idris"; developerlife.com byline is "Nazmul Idris"
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `r3bl_tui`, 6 real reverse dependencies — https://crates.io/api/v1/crates/r3bl_tui/reverse_dependencies (checked 2026-09-28)
influence:
- (none found)
checked: production, role, book/course/talk/post — not pursued once crate-dependents confirmed MEETS. Note: same person as `nas-ceo-founder-rebel-author-developerlife-com-maintainer` (this same chunk) under a second Voice id.

## nemo157
name: Nemo157
identity: https://github.com/Nemo157 — GitHub profile discloses name "Nemo157", blog https://nemo157.com, created 2009, 227 followers; crates.io account (id 782) tied to same login
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `bs58`, 1434 real reverse dependencies, and `async-compression`, 363 real reverse dependencies — https://crates.io/api/v1/crates/bs58/reverse_dependencies (checked 2026-09-28); https://crates.io/api/v1/crates/async-compression/reverse_dependencies (checked 2026-09-28)
influence:
- bs58 has 1434 crates.io reverse dependents; async-compression has 363 — https://crates.io/api/v1/crates?user_id=782 (2026-09-28)
checked: production, role, book/course/talk/post — not pursued once crate-dependents confirmed MEETS.

## newpavlov
name: Artyom Pavlov (newpavlov)
identity: https://github.com/newpavlov — GitHub profile discloses name "Artyom Pavlov", 212 followers; crates.io account (id 5059) tied to same login
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns RustCrypto core crates `digest` (1180 real reverse dependencies), `hmac` (3909), `aes` (1424), `cipher` (376), `crypto-common` (86) — https://crates.io/api/v1/crates/digest/reverse_dependencies (checked 2026-09-28); ownership confirmed via https://crates.io/api/v1/crates/digest/owner_user
influence:
- maintains ~100 RustCrypto crates in total (https://crates.io/api/v1/crates?user_id=5059, 2026-09-28); `hmac` alone has 3909 reverse dependents
checked: production, role, book/course/talk/post — not pursued once crate-dependents confirmed MEETS.

## nick-kuntz
name: Nick Kuntz
identity: https://github.com/nkuntz1934 — GitHub profile discloses name "Nick K", bio "Senior Engineering TPM @ Cloudflare", email nicholas.kuntz@cloudflare.com — matches the Cloudflare blog byline
type: unset
verdict: FAILS
track_record:
- (none found)
influence:
- (none found)
checked: crate-dependents (no crates.io account found for nkuntz1934 or nick-kuntz-dev); production (the claimed source, blog.cloudflare.com/serverless-matrix-homeserver-workers, is tagged "Rust" on Cloudflare's site but the article's own text states the port was built "in TypeScript using the Hono framework"; his own GitHub repo behind the post, `matrix-workers`, is TypeScript; he only forked `n0-computer/iroh`, no authored Rust code found; role is TPM, not engineering); role (no Rust project/foundation team-page listing found); book/course/talk/post (the post itself is not about Rust work he authored, so it cannot ground this kind even though it appears on a corporate blog).

## nico
name: Nico Burns
identity: https://github.com/nicoburns — GitHub profile discloses name "Nico Burns"; self-introduced in the source video as "Nico ... works on Servo, maintains Blitz ... Taffy ... blessed.rs"; crates.io account (id 168409) confirmed co-owner of `taffy`
type: builder
verdict: MEETS
track_record:
- crate-dependents: co-owns `taffy`, 184 real reverse dependencies, and owns `blitz`/`blitz-dom` and related crates — https://crates.io/api/v1/crates/taffy/reverse_dependencies (checked 2026-09-28); https://crates.io/api/v1/crates/taffy/owner_user
influence:
- taffy has 184 crates.io reverse dependents; co-owned with Jonathan Kelley (Dioxus) and Alice Cecile (Bevy) — https://crates.io/api/v1/crates/taffy/owner_user (2026-09-28)
checked: production, role, book/course/talk/post — not pursued once crate-dependents confirmed MEETS.

## nico-blitz-dioxus-labs-maintains-servo-adjacent-blitz-taffy
name: Nico Burns
identity: https://github.com/nicoburns — same identity and evidence as the `nico` Voice above (this same chunk); self-introduced in the same source video
type: builder
verdict: MEETS
track_record:
- crate-dependents: co-owns `taffy`, 184 real reverse dependencies, and owns `blitz`/`blitz-dom`/`blitz-html`/etc. — https://crates.io/api/v1/crates/taffy/reverse_dependencies (checked 2026-09-28)
influence:
- taffy has 184 crates.io reverse dependents — https://crates.io/api/v1/crates/taffy/owner_user (2026-09-28)
checked: production, role, book/course/talk/post — not pursued once crate-dependents confirmed MEETS. Note: same person as the `nico` Voice id in this chunk — two Voice ids for one person.

## nicole-tietz-sokolskaya
name: Nicole Tietz-Sokolskaya
identity: https://github.com/ntietz — GitHub profile discloses name "Nicole", blog field https://ntietz.com matches the claimed source domain exactly; crates.io account (id 241126) tied to same login
type: builder
verdict: MEETS
track_record:
- book/course/talk/post: the exact claimed post ("Rust needs a web framework for lazy developers") is linked from This Week in Rust issue 2024-10-02 — https://ntietz.com/blog/rust-needs-a-web-framework-for-lazy-developers ; https://github.com/rust-lang/this-week-in-rust/blob/main/content/2024-10-02-this-week-in-rust.md (checked 2026-09-28)
influence:
- (none found beyond the TWiR listing)
checked: crate-dependents (owns `cryptoy`, `ltl-args`, `pi-compression`, `routem`, all 0 reverse dependencies); production; role — not pursued once book/course/talk/post confirmed MEETS.

## nikomatsakis
name: Niko Matsakis
identity: https://github.com/rust-lang/team/blob/main/people/nikomatsakis.toml — rust-lang/team repository lists `name = "Niko Matsakis"`, `github = "nikomatsakis"`
type: language-designer
verdict: MEETS
track_record:
- role: listed in the rust-lang/team registry (the canonical Rust project team-membership source) — https://github.com/rust-lang/team/blob/main/people/nikomatsakis.toml (checked 2026-09-28)
influence:
- (none found beyond the team listing)
checked: crate-dependents, production, book/course/talk/post — not pursued once role confirmed MEETS.

## nmn-nmn-sh-blog-author
name: Naman Goel (nmn)
identity: https://github.com/nmn — GitHub profile discloses name "Naman Goel", blog field "nmn.sh" (exact match to claimed source domain), company "Facebook", 803 followers
type: critic
verdict: MEETS
track_record:
- book/course/talk/post: "Swift is a more convenient Rust" reached 328 Hacker News points and 357 comments — https://nmn.sh/blog/2023-10-02-swift-is-the-more-convenient-rust ; https://news.ycombinator.com/item?id=46841374 (checked 2026-09-28)
influence:
- (none found)
checked: crate-dependents, production, role — not pursued once book/course/talk/post confirmed MEETS.

## noah-gift
name: Noah Gift
identity: https://github.com/noahgift — well-documented public figure (Founder of Pragmatic AI Labs, Duke Engineer-in-Residence, AWS ML Hero); crates.io account (id 342066) tied to same login
type: educator
verdict: MEETS
track_record:
- crate-dependents: owns `aprender` ("next-generation ML framework in pure Rust"), 12 real reverse dependencies — https://crates.io/api/v1/crates/aprender/reverse_dependencies (checked 2026-09-28)
influence:
- aprender has 123,503 total downloads; also owns `apr-cli` (1 reverse dependency) in the same ecosystem — https://crates.io/api/v1/crates?user_id=342066 (2026-09-28)
- authors "Small Rust Tutorial For MLOps," part of a Duke Coursera specialization — https://nogibjj.github.io/rust-tutorial (2023)
checked: production, role — not pursued once crate-dependents confirmed MEETS. book/course/talk/post checked separately: no TWiR link and no Hacker News hits found for the course itself, so that kind alone would not have qualified.

## nobody1707
name: Nobody1707
identity: https://github.com/Nobody1707 — GitHub account exists (created 2010, 4 public repos, one in Rust) but discloses no real name, no bio, 2 followers
type: unset
verdict: FAILS
track_record:
- (none found)
influence:
- (none found)
checked: crate-dependents (no crates.io account found); production (no evidence found); role (no evidence found); book/course/talk/post (the claimed source is a single forum reply on forums.swift.org, not an authored book/course/talk/post of their own).
