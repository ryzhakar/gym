## vectorware
name: Vectorware
identity: https://github.com/vectorware (org bio: "Making everything modern, fast, and secure."), company blog vectorware.com
type: builder
verdict: MEETS
track_record:
- crate-dependents/production: self-described "first GPU-native software company", building on rust-gpu (spirv-std has 13 real reverse dependencies) — https://crates.io/api/v1/crates/spirv-std/reverse_dependencies (checked 2026-09-28); own blog post on GPU async/await architecture — https://vectorware.com/blog/async-await-on-gpu (2026-02-18)
influence:
- positions itself as building on the existing rust-gpu/rust-cuda open-source ecosystem
checked: role, book/course/talk/post not separately checked (crate-dependents/production already holds)

## vitalyd
name: vitalyd
identity: https://github.com/vitalyd — no bio/company/blog; users.rust-lang.org profile page shows only username and avatar, no further identity
type: critic
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account (404)
- checked production: no employer/job page found
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: a single 2017 forum reply on users.rust-lang.org is substantive but is neither a book, course, talk, nor a post meeting the widely-read bar
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold (the map's own claim record already flags this voice's track record as uncertain)

## vorpal
name: Vorpal
identity: https://github.com/Vorpal — no bio/company/blog
type: critic
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account (404)
- checked production: no employer/job page found
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: none found
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## vri
name: vri
identity: https://github.com/VRI — no bio/company/blog
type: critic
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account (404)
- checked production: no employer/job page found
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: none found
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## wandbrandon
name: Brandon Wand
identity: https://github.com/wandbrandon (real name given, no bio/company)
type: builder
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account (404)
- checked production: no employer/job page found
- checked role: only 1 PR authored in tracel-ai/burn (`gh api search/issues?q=repo:tracel-ai/burn+author:wandbrandon+is:pr` → 1) — thin, third-party contribution, not a maintainer role
- checked book/course/talk/post: none found
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## warre-snaet
name: Warre Snaet
identity: https://snaetwarre.github.io/My-Portofolio (self-authored portfolio blog)
type: builder
verdict: MEETS
track_record:
- post: "Building a 24MB Offline AI with Rust + Burn" was linked from This Week in Rust — `gh api search/code?q=intelligent-disease-detection+repo:rust-lang/this-week-in-rust` → content/2026-01-28-this-week-in-rust.md (checked 2026-09-28)
influence:
- own project post detailing a real edge-inference deployment (Rust+Burn compiling to native GPU/CPU/WASM/mobile targets) — https://snaetwarre.github.io/My-Portofolio/blog/intelligent-disease-detection.html (2026-01-28)
checked: crate-dependents, production, role not separately checked (post already holds)

## wedson-almeida-filho
name: Wedson Almeida Filho
identity: widely documented lead of the Rust-for-Linux project, quoted in his own kernel-mailing-list resignation post via ArsTechnica — https://arstechnica.com/gadgets/2024/09/rust-in-linux-lead-retires-rather-than-deal-with-more-nontechnical-nonsense
type: language-designer
verdict: MEETS
track_record:
- role: founding lead maintainer of the Rust-for-Linux project (Linux kernel Rust support) for almost 4 years — https://arstechnica.com/gadgets/2024/09/rust-in-linux-lead-retires-rather-than-deal-with-more-nontechnical-nonsense (2024-09-04)
influence:
- led the effort to bring Rust into the Linux kernel, a foundational Rust-systems-programming milestone
checked: crate-dependents, production, book/course/talk/post not separately checked (role already holds)

## wingertge-pr-author-tracel-ai-burn-contributor
name: Genna Wingert (wingertge)
identity: https://github.com/wingertge (real name given)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `macerator` (1.14M downloads, 8 real reverse dependencies) — https://crates.io/api/v1/crates/macerator/reverse_dependencies (checked 2026-09-28)
influence:
- macerator (SIMD abstraction crate) has a substantial real dependent ecosystem
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## withoutboats
name: withoutboats
identity: widely documented former Rust language/core team member, co-author of async/await and Pin — commenting on lobste.rs — https://lobste.rs/s/7rtvnp
type: language-designer
verdict: MEETS
track_record:
- role: former Rust core team member, key contributor to the design and implementation of async/await in Rust — https://lobste.rs/s/7rtvnp (2024-08-02)
influence:
- comments carry recognized design authority in async-Rust architecture discussions
checked: crate-dependents, production, book/course/talk/post not separately checked (role already holds)

## wofo-quoting-the-dropshot-projects-own-stated-design-goal
name: wofo (quoting the Dropshot project's own stated design goal)
identity: https://github.com/wofo — no bio, company, or blog
type: critic
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account found
- checked production: no employer/job page found
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: none found
influence:
- none found (the claim itself is wofo relaying a quote from the Dropshot project, not an original credential of wofo's own)
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## worldsender
name: WorldSEnder
identity: https://github.com/WorldSEnder (bio: "Rust aficionado... Maintainer @yewstack")
type: builder
verdict: MEETS
track_record:
- role: self-declared maintainer of Yew, a major Rust web framework
- crate-dependents: owns `tracing-web` (2.8M downloads, 35 real reverse dependencies) — https://crates.io/api/v1/crates/tracing-web/reverse_dependencies (checked 2026-09-28)
influence:
- tracing-web is a widely depended-upon crate; yew-autoprops and wasm_split_* crates also published
checked: production, book/course/talk/post not separately checked (role/crate-dependents already hold)

## wucke13
name: wucke13
identity: https://github.com/wucke13 (company: German Aerospace Center (DLR))
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns `a653rs` (ARINC 653 aerospace real-time OS bindings, 4 real reverse dependencies) — https://crates.io/api/v1/crates/a653rs/reverse_dependencies (checked 2026-09-28); also owns `rosenpass` (a known post-quantum-secure VPN protocol crate)
influence:
- a653rs crate family used in real aerospace real-time systems work at DLR
checked: production, role, book/course/talk/post not separately checked (crate-dependents already holds)

## yakira-neko
name: Yakira
identity: https://github.com/yakira-neko (first name given, no company/blog)
type: critic
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account (404)
- checked production: no employer/job page found
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: none found
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## yanshay
name: yanshay
identity: https://github.com/yanshay — creator of SpoolEase, confirmed via project site and GitHub repo — https://github.com/yanshay/spoolease
type: builder
verdict: MEETS
track_record:
- production: ships "SpoolEase," a real 3D-printing filament-management hardware product (NFC/RFID console + scale) built in Rust, 554 GitHub stars — `gh api repos/yanshay/spoolease` → language: Rust (checked 2026-09-28)
influence:
- real embedded-Rust hardware product with an active user community (esp-hal-based, per the claim's own source context)
checked: crate-dependents, role, book/course/talk/post not separately checked (production already holds)

## yatekii
name: Noah Hüsser (Yatekii)
identity: https://github.com/Yatekii (bio: "creating https://probe.rs")
type: builder
verdict: MEETS
track_record:
- role/crate-dependents: creator of probe-rs, a real embedded ARM/RISC-V debugging toolset (2,953 GitHub stars), with 1,066 commits authored — `gh api search/commits?q=repo:probe-rs/probe-rs+author:Yatekii` → 1066 (checked 2026-09-28)
influence:
- probe-rs is a widely used embedded Rust debugging tool
checked: production, book/course/talk/post not separately checked (role/crate-dependents already hold)

## yawaramin
name: Yawar Amin
identity: https://github.com/yawaramin (blog dev.to/yawaramin, bio "🐫" — OCaml-focused)
type: critic
verdict: FAILS
track_record:
- checked crate-dependents: crates.io account exists but owns 0 published crates — https://crates.io/api/v1/crates?user_id=355758 (checked 2026-09-28)
- checked production: no Rust employer/job page found (known primarily as an OCaml developer)
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: no Rust-specific authored content found
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## yevgen-safronov-nikita-lapkov-j-r-me-schneider-cloudflare
name: Yevgen Safronov, Nikita Lapkov, Jérôme Schneider (Cloudflare, R2 SQL)
identity: bylined authors of an official Cloudflare engineering blog post — https://blog.cloudflare.com/r2-sql-deep-dive
type: builder
verdict: MEETS
track_record:
- production: Cloudflare engineers describing the architecture of R2 SQL, a real shipped Cloudflare distributed query engine — https://blog.cloudflare.com/r2-sql-deep-dive (2025-09-25)
influence:
- official company engineering blog documenting a production system built at scale
checked: crate-dependents, role, book/course/talk/post not separately checked (production already holds)

## yinho999
name: naiker (yinho999)
identity: https://github.com/yinho999 (real name "naiker" given)
type: builder
verdict: FAILS
track_record:
- checked crate-dependents: owns crates `kuber` and `loco-oauth2`, both with 0 real reverse dependencies — https://crates.io/api/v1/crates/loco-oauth2/reverse_dependencies (checked 2026-09-28)
- checked production: no employer/job page found
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: none found
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## ysalitrynskyi
name: Yevhen Salitrynskyi
identity: https://github.com/ysalitrynskyi (real name given, company "YS Progress Inc.")
type: builder
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account found
- checked production: no employer post or job page from YS Progress Inc. naming Rust in production found
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: none found
influence:
- none found
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## yuri-iozzelli
name: Yuri Iozzelli
identity: bylined "Principal Software Engineer @ Leaning Technologies," X handle @YIozzelli — https://labs.leaningtech.com/blog/browserpod-rust (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- production: Principal Software Engineer authoring an employer post on BrowserPod, Leaning Technologies' real Rust-in-browser product — https://labs.leaningtech.com/blog/browserpod-rust (2026-08-26)
influence:
- documents production engineering tradeoffs (ecosystem `cfg(wasm)` handling) for a shipped product
checked: crate-dependents, role, book/course/talk/post not separately checked (production already holds)

## zackw
name: Zack Weinberg
identity: https://github.com/zackw (bio explicitly states "I do security research and misc systems coding", blog owlfolio.org)
type: critic
verdict: FAILS
track_record:
- checked crate-dependents: no crates.io account (404)
- checked production: no employer/job page found (bio explicitly states not looking for one; no Rust-production claim)
- checked role: no Rust project/foundation team page listing
- checked book/course/talk/post: no Rust-specific authored content found; his internals.rust-lang.org post is a design-discussion reply, not a book/course/talk/widely-read post
influence:
- none found meeting the bar
checked: crate-dependents, production, role, book/course/talk/post — all checked, none hold

## zaidoon-abd-al-hadi
name: Zaidoon Abd Al Hadi
identity: named in-text (not the byline) by Cloudflare engineering-blog authors Kevin Guthrie and Mariia Iurchenko as a colleague who contributed the key insight — https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/ (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- production: credited by named Cloudflare engineers, in an official Cloudflare engineering post, with the specific technical insight (byte-array struct packing) that shipped in a real production RAM-saving optimization — https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/ (2026-09-18)
influence:
- contribution documented in an official company engineering post about a shipped production optimization
checked: crate-dependents, role, book/course/talk/post not separately checked (production already holds); identity is tied via named colleague-credit rather than a byline — not guessed beyond what the source states

## zcash-foundation-zebra-project
name: Zcash Foundation / Zebra project
identity: official project book/site — https://zebra.zfnd.org/
type: institution
verdict: MEETS
track_record:
- production/role: Zebra is the Zcash Foundation's own full node implementation, written in Rust, with its own published design-rationale book — https://zebra.zfnd.org/ (book)
influence:
- production consensus-critical node software for a major cryptocurrency network
checked: crate-dependents, book/course/talk/post not separately checked (production/role already hold)

## zeke-hunter-green
name: Zeke Hunter Green (per official talk credit: "Z. Hunter Green")
identity: YouTube oEmbed: "S. Cutler, D. Hugenroth, Z. Hunter Green: 'Secure Messaging: The Guardian's Whistleblowing System'", published by channel Rust Foundation — https://www.youtube.com/oembed?url=https://youtube.com/watch?v=8n13Oh8c0r4 (checked 2026-09-28)
type: builder
verdict: MEETS
track_record:
- production: co-presents a Rust Foundation-hosted talk on The Guardian's production whistleblowing/secure-messaging system — https://youtube.com/watch?v=8n13Oh8c0r4 (2025-10-03)
influence:
- talk hosted/published by the Rust Foundation's own YouTube channel
checked: crate-dependents, role, book/course/talk/post not separately checked (production/talk already holds)
