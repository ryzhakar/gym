## lonjil
name: lonjil
identity: untied
type: unset
verdict: UNKNOWN
checked: crate-dependents, production, role, book/course/talk/post — lobste.rs profile self-describes as "A mystery...", GitHub account (github.com/lonjil) discloses no name, no matching crates.io account found

## lorenzleutgeb
name: Lorenz Leutgeb
identity: https://github.com/lorenzleutgeb (name: Lorenz Leutgeb; company: Max Planck Institute for Informatics; blog lorenz.leutgeb.xyz)
type: builder
verdict: MEETS
track_record:
- crate-dependents: owns crates.io `radicle` crate, 22 reverse dependents — https://crates.io/api/v1/crates/radicle/reverse_dependencies (checked 2026-09-28)
- crate-dependents: owns `git-ref-format`, 1 reverse dependent — https://crates.io/api/v1/crates/git-ref-format/reverse_dependencies (checked 2026-09-28)
influence:
- owns 28 published crates under this account (radicle-*, git-ref-format-*) — https://crates.io/api/v1/crates?user_id=154369 (checked 2026-09-28)
checked: production, role, book/course/talk/post — not pursued, crate-dependents already MEETS

## louisfd-tracel-ai-burn-maintainer
name: Louis Fortier-Dubois
identity: https://github.com/louisfd (name: Louis Fortier-Dubois; bio "Co-founder @ Tracel AI"; public member of tracel-ai org)
type: builder
verdict: MEETS
track_record:
- role: public member of the tracel-ai GitHub org, which owns the `burn` crate via its "Core" team — https://api.github.com/orgs/tracel-ai/public_members (checked 2026-09-28)
- crate-dependents: `burn` (co-owned by the tracel-ai:core team), 324 reverse dependents — https://crates.io/api/v1/crates/burn/reverse_dependencies (checked 2026-09-28)
influence:
- authored the autotuned conv2d/conv_transpose2d im2col-GEMM PR reviewed in the claim source — https://github.com/tracel-ai/burn/pull/2287 (2024-09)
checked: production, book/course/talk/post — not pursued, role + crate-dependents already MEETS

## lqd
name: Rémy Rakic
identity: https://github.com/lqd (name: Rémy Rakic; public member of rust-lang org)
type: builder
verdict: MEETS
track_record:
- role: listed in the rust-lang/team GitHub repo across teams.toml, types.toml, wg-polonius.toml and compiler.toml — https://github.com/rust-lang/team (checked 2026-09-28)
influence:
- monthly progress reporter for the Polonius project goal on the official Rust blog — https://blog.rust-lang.org/2025/05/26/april-project-goals-update (2025-05-07)
checked: crate-dependents, production, book/course/talk/post — not pursued, role already MEETS

## ltrlg
name: Ltrlg
identity: untied
type: unset
verdict: UNKNOWN
checked: crate-dependents, production, role, book/course/talk/post — internals.rust-lang.org profile (trust_level 2) discloses no name, bio or website; no matching GitHub or crates.io account found

## luca-casonato
name: Luca Casonato
identity: self-introduced by full name and employer in the cited talk itself ("I'm Luca... software engineer at the Deno company"), matching the Voice name — https://youtube.com/watch?v=YcujtU0LA9Y (2024-02-13)
type: builder
verdict: MEETS
track_record:
- production: Deno core engineer, describing Deno's own Rust runtime's error-handling, allocation and crates.io-only dependency practices in a first-person conference talk — https://youtube.com/watch?v=YcujtU0LA9Y (2024-02-13)
influence:
- self-reports chairing WinterCG (W3C community group) and sitting on TC39 in the same talk — https://youtube.com/watch?v=YcujtU0LA9Y (2024-02-13)
checked: crate-dependents, role, book/course/talk/post — not pursued, production already MEETS

## luciano-mammino
name: Luciano Mammino
identity: https://loige.co (byline "Author Luciano Mammino"; own domain with About/Books/Speaking sections)
type: educator
verdict: MEETS
track_record:
- book/course/talk/post: "Writing Middlewares for Rust Lambda Functions" (loige.co), linked from This Week in Rust issue 2026-05-06 — https://loige.co/writing-middlewares-for-rust-lambda-functions (2026-05-03); TWiR: https://github.com/rust-lang/this-week-in-rust/blob/main/content/2026-05-06-this-week-in-rust.md (2026-05-06)
influence:
- co-authoring the book "Crafting Lambda Functions in Rust" with James Eastham — https://loige.co/coauthoring-a-book-about-rust-and-lambda (2024-12-16)
checked: crate-dependents, production, role — not pursued, book/post bar already MEETS

## luke-wagner-fastly-w3c-bytecode-alliance-component-model-co
name: Luke Wagner
identity: https://github.com/lukewagner (name: Luke Wagner; company: Fastly; public member of bytecodealliance org)
type: builder
verdict: MEETS
track_record:
- role: public member of the bytecodealliance GitHub org (steward of wasmtime/wit-bindgen, the Rust-based runtime and tooling built on the Component Model he co-designs) — https://api.github.com/orgs/bytecodealliance/public_members (checked 2026-09-28). Note: this ties him to Bytecode Alliance governance, not literally a rust-lang.org page; flagged rather than silently equated
influence:
- primary author/driver of the WIT `map<K,V>` and dependency-syntax proposals — https://github.com/WebAssembly/component-model/pull/554 (2025-08-14); https://github.com/WebAssembly/component-model/pull/393 (2024-09-10)
checked: crate-dependents, production, book/course/talk/post — not pursued, role already MEETS

## lukechu10
name: Luke
identity: https://github.com/lukechu10 (crates.io owner login matches GitHub login exactly; blog lukechu.dev)
type: builder
verdict: MEETS
track_record:
- crate-dependents: sole owner of `sycamore` crate, 19 reverse dependents — https://crates.io/api/v1/crates/sycamore/reverse_dependencies (checked 2026-09-28)
checked: production, role, book/course/talk/post — not pursued, crate-dependents already MEETS

## lukewagner
name: Luke Wagner
identity: https://github.com/lukewagner (name: Luke Wagner; company: Fastly; public member of bytecodealliance org) — same GitHub account as the `luke-wagner-fastly-w3c-bytecode-alliance-component-model-co` Voice above
type: builder
verdict: MEETS
track_record:
- role: public member of the bytecodealliance GitHub org; co-designer of the WebAssembly Component Model — https://api.github.com/orgs/bytecodealliance/public_members (checked 2026-09-28)
influence:
- authored the CABI special-case-lowering proposal for `option`/`result` types — https://github.com/WebAssembly/component-model/issues/525 (2025-06-04)
checked: crate-dependents, production, book/course/talk/post — not pursued, role already MEETS

## maahl-maahl-net
name: maahl (no legal name disclosed)
identity: https://maahl.net/cv/ — a self-hosted CV disclosing a specific, checkable professional history (Tech Lead at Xeneta, Oslo, PhD) tied to the same domain that hosts the blog; no printed legal name found
type: educator
verdict: MEETS
track_record:
- book/course/talk/post: "Create a Lambda in Rust using Terraform" (maahl.net), linked from This Week in Rust issue 2023-11-29 — https://maahl.net/blog/rust-aws-lambda (2023-11-05); TWiR: https://github.com/rust-lang/this-week-in-rust/blob/main/content/2023-11-29-this-week-in-rust.md (2023-11-29)
checked: crate-dependents, production, role — CV states "Rust: beginner" and lists Python/SQL as the day-job stack at Xeneta, not Rust in production; no crate ownership or project-role evidence found

## mabezdev
name: Scott Mabin
identity: https://github.com/MabezDev (name: Scott Mabin; company: @espressif; crates.io owner login matches GitHub exactly)
type: builder
verdict: MEETS
track_record:
- crate-dependents: direct owner of `esp-hal`, 116 reverse dependents — https://crates.io/api/v1/crates/esp-hal/reverse_dependencies (checked 2026-09-28)
checked: production, role, book/course/talk/post — not pursued, crate-dependents already MEETS

## madhadron
name: Fred Ross (circumstantial tie only)
identity: https://github.com/madhadron discloses the name Fred Ross and blog madhadron.com; this is the same rare handle as the lobste.rs commenter but the two accounts are not explicitly cross-linked
type: unset
verdict: FAILS
checked: crate-dependents (no crates.io account under this handle or name), production, role, book/course/talk/post — no Rust production employer, project/foundation role, crate, or widely-read Rust work found for this identity; the single lobste.rs comment proposing a model checker is the only Rust-related evidence located

## madoshakalaka
name: Siyuan Yan
identity: https://github.com/Madoshakalaka (name: Siyuan Yan; bio "Maintainer at @yewstack"; public member of yewstack org)
type: builder
verdict: MEETS
track_record:
- crate-dependents: direct owner of `yew` crate, 318 reverse dependents — https://crates.io/api/v1/crates/yew/reverse_dependencies (checked 2026-09-28)
checked: production, role, book/course/talk/post — not pursued, crate-dependents already MEETS

## matheus23-iroh-maintainer-n0
name: Philipp Krüger
identity: https://github.com/matheus23 (name: Philipp Krüger; company: @n0-computer; public member of n0-computer org; blog irreactive.com)
type: builder
verdict: MEETS
track_record:
- crate-dependents: `iroh` (owned by dignifiedquire + the n0-computer:iroh-publisher team; matheus23 is a public n0-computer org member), 276 reverse dependents — https://crates.io/api/v1/crates/iroh/reverse_dependencies (checked 2026-09-28); org membership — https://api.github.com/orgs/n0-computer/public_members (checked 2026-09-28)
checked: production, role, book/course/talk/post — not pursued, crate-dependents already MEETS

## matheus23-n0-computer-iroh-maintainer
name: Philipp Krüger
identity: https://github.com/matheus23 (same account as `matheus23-iroh-maintainer-n0` above)
type: builder
verdict: MEETS
track_record:
- crate-dependents: `iroh`, 276 reverse dependents, via n0-computer org membership — https://crates.io/api/v1/crates/iroh/reverse_dependencies (checked 2026-09-28)
checked: production, role, book/course/talk/post — not pursued, crate-dependents already MEETS

## matklad
name: Alex Kladov
identity: https://github.com/matklad (name: Alex Kladov; company: @tigerbeetle; blog matklad.github.io)
type: builder
verdict: MEETS
track_record:
- crate-dependents: co-owner of `rust-analyzer` crate (with rust-lang-owner and Veykril) — https://crates.io/api/v1/crates/rust-analyzer/owners (checked 2026-09-28)
checked: production, role, book/course/talk/post — not pursued, crate-dependents already MEETS

## matt-keeter
name: Matt Keeter
identity: https://github.com/mkeeter (name: Matt Keeter; own blog mattkeeter.com with an "about" page)
type: builder
verdict: MEETS
track_record:
- crate-dependents: sole owner of `fidget` crate, 1 reverse dependent — https://crates.io/api/v1/crates/fidget/reverse_dependencies (checked 2026-09-28)
checked: production, role, book/course/talk/post — not pursued, crate-dependents already MEETS

## mattuwu-yew-maintainer
name: Mattuwu (no legal name disclosed)
identity: byline on Yew's own official blog, "Mattuwu — Maintainer of Yew" — https://yew.rs/blog/2025/11/29/release-0-22 (2025-11-29). The GitHub account `mattuwu` discloses no name and is not a public member of the yewstack org, so the tie rests on the project's own site rather than an independently corroborated profile
type: builder
verdict: MEETS
track_record:
- role: authored and is bylined "Maintainer of Yew" on the project's own official release-announcement post — https://yew.rs/blog/2025/11/29/release-0-22 (2025-11-29)
checked: crate-dependents (not a crates.io owner of `yew`), production, book/course/talk/post

## mattya
name: mattya
identity: untied
type: unset
verdict: UNKNOWN
checked: crate-dependents, production, role, book/course/talk/post — lobste.rs profile self-describes as "A mystery...", GitHub account discloses no name, no matching crates.io account found

## michael-de-silva
name: Michael de Silva
identity: crustyengineer.com, site copyright footer "© 2026 Michael de Silva"
type: educator
verdict: MEETS
track_record:
- book/course/talk/post: "Axum: Multi-tenancy (with Hexarch) and Abstracting the Repository Layer", linked from This Week in Rust issue 2025-10-22 — https://crustyengineer.com/blog/axum-multi-tenancy-abstract-repository-layer (2025-10-19); TWiR: https://github.com/rust-lang/this-week-in-rust/blob/main/content/2025-10-22-this-week-in-rust.md (2025-10-22)
checked: crate-dependents, production, role — not pursued, book/post bar already MEETS

## milenkovicm
name: Marko Milenković
identity: https://github.com/milenkovicm (name: Marko Milenković; bio "@apache DataFusion committer & PMC member"), confirmed against Apache's own roster
type: builder
verdict: MEETS
track_record:
- role: listed as both a DataFusion committer and DataFusion PMC member on Apache's official committers-by-project roster — https://people.apache.org/committers-by-project.html (checked 2026-09-28; rows `datafusion-milenkovicm`, `datafusion-pmc-milenkovicm`)
influence:
- 27 authored pull requests and 20 authored commits against apache/datafusion — https://github.com/apache/datafusion (checked 2026-09-28)
checked: crate-dependents, production, book/course/talk/post — not pursued, role already MEETS

## mordecai-emmanuel-etukudo
name: Mordecai Emmanuel Etukudo
identity: introduced by full name by the conference MC and self-introduces on camera — https://youtube.com/watch?v=RROFUwKZbCA (2026-06-11)
type: unset
verdict: FAILS
checked: crate-dependents (none found), production (none found), role (self-described "project team lead at Rust Stations Africa" and "co-organizer of Rust Nigeria" — regional community roles, not a rust-lang.org/foundation team-page listing found via `gh api` on rust-lang/team), book/course/talk/post (the talk itself is real and identity is tied, but it was not found linked from any This Week in Rust issue, and searches for the talk title, video ID, and speaker/group name returned zero Hacker News hits and no Lobsters results)

## moss
name: Oliver Moss
identity: forgestream.idverse.com author bio: "Oliver is a Rust engineer... Oliver joined IDVerse in 2025"
type: builder
verdict: MEETS
track_record:
- production: IDVerse's own engineering blog states "We use Rust for our frontend projects," authored by an identified IDVerse engineer — https://forgestream.idverse.com/blog/20260313-rust-export (2026-02-09)
checked: crate-dependents, role, book/course/talk/post — not pursued, production already MEETS

## mrgvsv
name: Gino Valente
identity: https://github.com/MrGVSV (name: Gino Valente; company: @Shopify; blog ginovalente.me; public member of bevyengine org)
type: builder
verdict: MEETS
track_record:
- crate-dependents: public member of the bevyengine org (co-maintainer alongside owner `cart` and team `publish`) for `bevy`, 2045 reverse dependents — https://crates.io/api/v1/crates/bevy/reverse_dependencies (checked 2026-09-28); org membership — https://api.github.com/orgs/bevyengine/public_members (checked 2026-09-28)
checked: production, role, book/course/talk/post — not pursued, crate-dependents already MEETS
