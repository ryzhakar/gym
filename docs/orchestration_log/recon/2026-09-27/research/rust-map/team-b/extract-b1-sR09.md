For each source: what must a Rust practitioner decide, and where do the sources conflict on it?

## f003809 — apache/datafusion issue #18566, "Release DataFusion 52.0.0" (2025-11-09 → 2026-01-13, domain: distributed)

Nothing new. Reason: a release-coordination tracking issue (checklists, downstream-consumer testing, vote scheduling). One thread (tschwarzinger, RDF Fusion) surfaces a real `Arc`-cloning bug around `DynamicFilterPhysicalExpr`'s inner/outer `Arc` and asks why the type isn't `Clone`, but no maintainer states a Position on a debated design question — adriangb calls it a likely bug to patch, not a considered tradeoff.

## f003815 — wasm-bindgen/wasm-bindgen PR #4795, "fix: revert deno wasm loading template" (2025-11-10 → 2026-01-16, domain: wasm)

Question and Claim.

- Question: once a `.wasm` file is already fully loaded into memory as bytes/a blob, should the loader still route it through the streaming compile/instantiate API, or fall back to the plain bytes-based `instantiate`?
  - Claim — Voice: RReverser (wasm-bindgen maintainer). Position: drop the streaming wrapper when the bytes are already in hand; it buys nothing there.
    Quote: "There's no need for the complex wrapping into a `Response` - `instantiateStreaming` doesn't have any benefits when we already loaded the whole file as a blob. Let's just revert to the regular `instantiate` which can take the bytes directly."
    Values: simplicity vs. reflexively reaching for the "faster-sounding" streaming API even where it can't help. Source: wasm-bindgen/wasm-bindgen#4795, comment 2025-11-14T13:35:08Z. Locator: L657-L661.

## f003938 — Yew blog, "Yew 0.22 - For Real This Time" (2025-11-29, domain: frontend)

Question and Claim.

- Question: should a component-templating macro (like Yew's `html!`) support native imperative control flow (`for`, `if`) written inline, or require iterator-adapter/functional-expression style?
  - Claim — Voice: Mattuwu (Yew maintainer). Position: add native `for`-loop syntax to `html!` alongside the existing iterator-adapter style, because it's "more natural."
    Quote: "You can now use for-loops directly in the `html!` macro, making iteration more natural" — contrasted with the prior iterator-adapter form shown in the same post ("Before - using iterator adapters ... { for items.iter().map(|item| html! { <li>{ item }</li> }) }").
    Values: approachability/ergonomics vs. staying within a purely functional/expression-based DSL style. Source: yew.rs/blog/2025/11/29/release-0-22, "For-Loops in html!" section. Locator: L712-L727.

## f003955 — embassy-rs/embassy PR #4989, "Upstream embassy-mcxa" (2025-12-04 → 2025-12-09, domain: embedded)

Question and Claims.

- Question: should a new chip-family HAL be merged into the monorepo immediately as its own separate crate to unblock waiting users, or held back until it can be integrated into the unified/combined HAL from the start?
  - Claim — Voice: jamesmunns (embassy maintainer). Position: land it as a side crate now; unify later once the shared metapac/combined HAL is ready.
    Quote: "I wanted to get our previously private work upstreamed ASAP (so we can basically deprecate/archive odp/embassy-mcxa). If there's a path to moving mcxa into embassy-nxp, we can do it now that the code is in the same repo."
    Values: iteration speed / unblocking users vs. architectural cohesion up front. Source: embassy-rs/embassy#4989, comment 2025-12-04T18:32:46Z. Locator: L817-L820.
  - Claim — Voice: felipebalbi (NXP embedded engineer, embassy-nxp contributor). Position: same — merge as-is now, deprecate in favor of the unified HAL once ready.
    Quote: "The idea is that we can get this merged as is, once the metapac is ready, we can switch to it. Then once the combined HAL is ready, it shouldn't be a big deal to deprecate this and have users switch."
    Values: same as above. Source: embassy-rs/embassy#4989, comment 2025-12-04T18:35:15Z. Locator: L824-L827.

## f004166 — Cloudflare blog, "Building a serverless, post-quantum Matrix homeserver" (2026-01-27, domain: cloud-workers)

Nothing new. Reason: read in full past the site's tag-cloud navigation to the article body. The core Matrix protocol port ("event authorization, room state resolution, cryptographic verification") is explicitly done "in TypeScript using the Hono framework"; Rust appears only as an illustrative Durable Object snippet (`#[durable_object] pub struct UserKeysObject`) for atomic key storage. No Position on a contested Rust practitioner decision is stated — it's an architecture case study (mapping Postgres/Redis/mutexes onto D1/KV/Durable Objects) with Rust as an incidental implementation detail, not its subject.

## f004371 — Swift forums, "'New Codable' prototype available for feedback" (2026-03-06 → 2026-08-25, domain: swift-interop)

Nothing new. Reason: read in full (a long-running Apple swift-foundation design thread, kperryua/Apple leading). Rust's serde (and the `musli` and `struct-patch` crates) are repeatedly invoked as design precedent and inspiration — e.g. "I will point at Rust Serde a lot... as evidence its designs do work for real projects," and a detailed comparison of serde's `#[patch(nesting)]` approach for the "patching" feature — but every participant (kperryua, tera, sliemeobn, filip-sakel, taylorswift, kiel, Jon_Shier, duan, and others) is a Swift-side contributor with no established Rust track record under this source (no crate maintained, no Rust production role, no Rust project/foundation role, no Rust book/course/talk/post). No Voice qualifies to anchor a Rust Claim, so despite the heavy Rust-serde engagement, this source yields no Rust map content — the same pattern as the Swift Mutex pitch thread in batch b1-sR03.

Summary: 6 sources read, 0 unreachable. 3 Questions raised with 4 Claims logged (wasm-bindgen#4795: streaming-vs-direct instantiate; Yew 0.22: imperative-for vs. iterator-adapter macro syntax; embassy#4989: land-now-unify-later HAL sequencing, with 2 independent Voices holding the same Position). 3 sources verdicted Nothing new — a release-logistics tracking issue, a Cloudflare architecture case study where Rust is incidental, and a long Swift forum thread that discusses Rust serde extensively but has no participant who qualifies as a Rust Voice — each with its stated reason.
