# Blind fill input, batch 1, file 13 of 13

For each Claim below, name the one Position of its Question that the Claim supports (a Position id from the list), or `none` if it supports none of them. The Claims are in random order.

## Question `ui-async-data-cache-vs-component`

When a UI component needs asynchronously-fetched data to render, should that data live in a cache on a shared owner object (populated by a hover/eager prefetch, read synchronously at render), or should the component itself own the async fetch and render a loading state until it resolves?

Positions:
- `ui-async-data-cache-vs-component--p1`: Component owns async lifecycle
- `ui-async-data-cache-vs-component--alt1`: A cache on a shared owner object, populated by prefetch

Claims:
- `a-sa13-f004772-c1` · Voice: SomeoneToIgnore · Source: https://github.com/zed-industries/zed/pull/58618 (`f004772`) · Date: 2026-08-06 · Locator: comment @SomeoneToIgnore 2026-08-06T16:47:14Z
  - Quote: "let the menu entity fetch its own data asynchronously... That is how every picker in Zed works."
  - Paraphrase: argues the hand-rolled outline cache, its hover-triggered prefetch, and its version-keyed invalidation are accidental complexity that exists only because the popover builder is synchronous; the fix is to let the menu entity spawn its own async fetch and render a loading state, "how every picker in Zed works" and how the PR's own path dropdown already behaves
- `a-sa13-f004772-c2` · Voice: ysalitrynskyi · Source: https://github.com/zed-industries/zed/pull/58618 (`f004772`) · Date: 2026-08-07 · Locator: comment @ysalitrynskyi 2026-08-07T17:45:21Z
  - Quote: "One async menu entity now serves both listings: fetches its own data (buffer_outline_items / expand_entry per step), no outline cache, no prefetch, no re-anchoring flag."
  - Paraphrase: reworked along the reviewer's architecture note rather than point-fixing; one async menu entity now fetches its own data per step, eliminating the cache, prefetch, and re-anchoring flag "by construction, not patched"

## Question `ui-dsl-vs-plain-rust`

Should a Rust GUI framework define UI structure through a bespoke DSL with dedicated tooling (Slint's own language, Makepad's `live_design!` macro), or should it stick to plain Rust code with no macros/DSL (egui's immediate-mode API)?

Positions:
- `ui-dsl-vs-plain-rust--p1`: Value depends on priorities
- `ui-dsl-vs-plain-rust--alt1`: A bespoke DSL with tooling (Slint, Makepad)
- `ui-dsl-vs-plain-rust--alt2`: plain Rust with no DSL or macros (egui)

Claims:
- `b-sb21-f008390-c2` · Voice: boringcactus (Melody) · Source: https://boringcactus.com/2025/04/13/2025-survey-of-rust-gui-libraries.html (`f008390`) · Date: 2025-04-16 · Locator: § "Conclusion"
  - Quote: "If you want to avoid DSLs and macros and write only regular Rust, egui offers that... If you like DSL-driven UIs that are putting serious effort into developer tooling, Slint might be for you."
  - Paraphrase: recommends egui to readers who want zero DSL/macros and plain Rust, and Slint to readers who want a DSL with serious dev-tooling investment (better error-message ceiling since it's a standalone language, not just macros); does not pick an overall winner between the two approaches

## Question `ui-state-scoped-lifetimes-vs-runtime-handles`

Should a Rust UI/reactive framework model component state with borrow-checker-scoped lifetimes tied to the component (arena/bump allocation: zero-clone access in event handlers, but confusing lifetime errors and incompatible with `'static` futures), or with a runtime-tracked `Copy` handle backed by generational/GC-like reclamation (uniform across closures, futures and threads, at the cost of adding a small runtime-tracking layer)?

Positions:
- `ui-state-scoped-lifetimes-vs-runtime-handles--p1`: Copy runtime tracked state
- `ui-state-scoped-lifetimes-vs-runtime-handles--alt1`: Borrow-checker-scoped lifetimes tied to the component

Claims:
- `b-sb17-f005144-c1` · Voice: Jonathan Kelley · Source: https://dioxuslabs.com/blog/release-050 (`f005144`) · Date: 2024-03-21 · Locator: article body, "Goodbye scopes and lifetimes!" / "Copy state" sections
  - Quote: "Dioxus 0.5 fixes this issue by first removing scopes and the 'bump lifetime and then introducing a new Copy state management solution called signals... With Copy state, we've essentially bolted on a light form of garbage collection into Rust that uses component lifecycles as the triggers for dropping state."
  - Paraphrase: removes the `'bump`-lifetime scope model because it doesn't work for `'static` futures and produces confusing lifetime errors, replacing it with `Copy` signals backed by a generational-box allocator, describing the result as a lightweight GC bolted onto Rust

## Question `unchecked-unwrap-vs-safe-abort`

For values statically safe to unwrap, a safe abort wrapper or unsafe unchecked unwrap?

Positions:
- `unchecked-unwrap-vs-safe-abort--p1`: Safe-abort(default recommendation)
- `unchecked-unwrap-vs-safe-abort--p2`: Unsafe unchecked(conditional)
- `unchecked-unwrap-vs-safe-abort--p3`: Prefer a safe abort-on-None/Err wrapper over unsafe unchecked unwrapping; reserve the unsafe route for near-certainty, kept checked in debug builds

Claims:
- `a-sB02-f000256-c8` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "Shrinking .wasm Code Size" — "Avoid Panicking"
  - Quote: "panics translate into aborts in wasm32-unknown-unknown anyways, so this gives you the same behavior but without the code bloat."
  - Paraphrase: to cut panic-related code bloat from unwrap, prefer a safe helper that calls process::abort() on None/Err over letting the formatted panic machinery run, since panics compile down to aborts on wasm32-unknown-unknown anyway.
- `b-bk02-f000256-c12` · Voice: rustwasm working group (Rust and WebAssembly book) [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: unknown (living doc) · Locator: § "Shrinking .wasm Code Size" → Avoid Panicking
  - Quote: "You really only want to use this unsafe approach when you 110% know that the assumption holds, and the compiler just isn't smart enough to see it."
  - Paraphrase: presents the safe `process::abort`-based `unwrap_abort` as the default way to drop panic-infrastructure bloat, and names the `unreachable` crate's unsafe `unchecked_unwrap` as a further, riskier step, explicitly conditioning its use on near-total certainty plus a debug build that still checks.
- `a-sB02-f000256-c9` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "Shrinking .wasm Code Size" — "Avoid Panicking"
  - Quote: "You really only want to use this unsafe approach when you 110% know that the assumption holds."
  - Paraphrase: the unreachable crate's unsafe unchecked_unwrap is offered as a further alternative, but restricted to cases where the programmer is "110% sure" the assumption holds, and only in release builds, keeping checked behavior in debug.

## Question `uniffi-packaging-xcode-vs-script`

When packaging a Rust core library for Apple platforms (iOS) via UniFFI, should the FFI-binding and packaging steps run as an Xcode build phase or as an external script/CI pipeline outside Xcode?

Positions:
- `uniffi-packaging-xcode-vs-script--p1`: Run Rust-to-Swift FFI packaging as an external shell-script/CI pipeline, not as an Xcode build phase
- `uniffi-packaging-xcode-vs-script--alt1`: An Xcode build phase

Claims:
- `a-sa27-f012237-c1` · Voice: Ian Wagner · Source: https://stadiamaps.com/news/ferrostar-building-a-cross-platform-navigation-sdk-in-rust-part-2 (`f012237`) · Date: 2024-12-04 · Locator: section "Generating the FFI Bindings", paragraph starting "NOTE: It is possible to integrate these steps into Xcode."
  - Quote: "given the relative difficulty of doing this and the overall flakiness of the Xcode build process, we opted for a simple, reliable shell script"
  - Paraphrase: it is possible to wire UniFFI's binding generation into an Xcode build phase, but Stadia Maps rejected that given the difficulty and the overall flakiness of the Xcode build process, choosing a plain shell script invoked manually/by CI instead, at the cost of needing a manual rebuild after Rust changes

## Question `unmaintained-dependency-weight`

When two crates cover the same need, how much should an unmaintained/flagged dependency (per RustSec) count against it versus its narrower scope fit?

Positions:
- `unmaintained-dependency-weight--p1`: Prefer actively-maintained broad-scope crate over flagged narrow one
- `unmaintained-dependency-weight--alt1`: Prefer the narrower-scope crate despite its maintenance status

Claims:
- `a-sa06-f003414-c1` · Voice: CrazyboyQCD · Source: https://github.com/zed-industries/zed/pull/36497 (`f003414`) · Date: 2025-08-30 · Locator: comment 2025-08-30T08:19:58Z
  - Quote: "it is unmaintained, buggy and legacy, so I think a more mordern crate would be better"
  - Paraphrase: argues `encoding` is unmaintained, buggy and legacy per a linked RustSec advisory, so a more modern crate (`encoding_rs`, or possibly ICU) is preferable even though `encoding_rs`'s stated focus is the Web

## Question `unsafe-fields-design`

Should unsafe struct fields be expressed with a minimal, purely field-level rule set (mark the field unsafe if it carries a safety invariant; using it is then unsafe), or with a hybrid design that mixes syntactic markers and wrapper types?

Positions:
- `unsafe-fields-design--p1`: Minimal field level rules
- `unsafe-fields-design--alt1`: A hybrid of syntactic markers and wrapper types

Claims:
- `a-sa20-f009698-c2` · Voice: @jswrenn · Source: https://blog.rust-lang.org/2025/05/26/april-project-goals-update (`f009698`) · Date: 2025-04-18 · Locator: "Unsafe Fields" section, comment posted 2025-04-18
  - Quote: "we can reduce field safety tooling to two rules: a field should be marked unsafe if it carries a safety invariant (of any kind); a field marked unsafe is unsafe to use."
  - Paraphrase: reports that after an observation from Ralf (that the additive/subtractive dichotomy and its Drop-related design concerns could be sidestepped, since a field already can't be put into an unsound-to-drop state without unsafe code), the RFC settled on two rules — a field is marked unsafe if it carries a safety invariant, and a field marked unsafe is unsafe to use — and that remaining discussion is now mostly about weighing this against a proposed alternative that mixes syntactic knobs and wrapper types

## Question `unsafe-mental-model`

What is `unsafe`'s proper mental model — a manual-invariant-maintenance discipline still bound by the same rules, or a permissive escape hatch?

Positions:
- `unsafe-mental-model--p1`: Unsafe is manual invariant maintenance not permission to break rules
- `unsafe-mental-model--p2`: Unsafe is a last resort not a nuclear option

Claims:
- `a-sa28-f012469-c11` · Voice: Ms2ger — track record uncertain in this source (recurring named contributor across 2015-2016, no confirmed authored crate/book found here); logged with this caveat · Source: https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (`f012469`) · Date: undated original; reposted 2015-04-27 · Locator: post by @bluss dated 2015-04-27T11:36:54Z
  - Quote: "unsafe code isn't for violating Rust's invariants, it's for maintaining them manually"
  - Paraphrase: states unsafe's purpose is upholding Rust's invariants by hand, not license to violate them
- `a-sa28-f012469-c12` · Voice: Aatch — track record uncertain in this source · Source: https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (`f012469`) · Date: undated original; reposted 2015-12-14 · Locator: post by @rgdmarshall dated 2015-12-14T07:53:53Z, sourced "on /r/rust"
  - Quote: "[Using unsafe is] less 'nuclear option' and more 'diplomacy has failed'."
  - Paraphrase: frames using unsafe as closer to "diplomacy has failed" than to reaching for an extreme, rarely-justified tool

## Question `unsafe-trait-vs-unsafe-method`

When a trait's correct implementation is required for memory safety, should the trait itself be marked `unsafe`, or should the unsafe boundary sit on the consuming method instead?

Positions:
- `unsafe-trait-vs-unsafe-method--p1`: Unsafe consuming fn
- `unsafe-trait-vs-unsafe-method--alt1`: Mark the trait itself `unsafe`

Claims:
- `a-sa07-f003716-c2` · Voice: urben1680 · Source: https://github.com/bevyengine/bevy/pull/21601 (`f003716`) · Date: 2025-10-20 · Locator: PR #21601, comment 2025-10-20T17:52:07Z
  - Quote: "Then I agree on the design here."
  - Paraphrase: accepts the design where the derive macro is trusted to build a valid accessor and the unsafe contract lands on the caller/consuming method rather than the trait
- `a-sa07-f003716-c1` · Voice: eugineerd · Source: https://github.com/bevyengine/bevy/pull/21601 (`f003716`) · Date: 2025-10-20 · Locator: PR #21601, comment 2025-10-20T17:20:03Z
  - Quote: "either mark `Relationship` trait unsafe and mention that `ENTITY_FIELD_OFFSET` must be correct to be safely implemented, or we'd have to leave `RelationshipAccessor::relationship` unsafe"
  - Paraphrase: says correctness must be enforced either by marking the Relationship trait unsafe or by leaving RelationshipAccessor::relationship unsafe since the implementer can't be trusted; the shipped design leaves the accessor method unsafe rather than the trait

## Question `unstable-feature-gate-vs-wait`

Ship unready API behind an unstable flag, or wait?

Positions:
- `unstable-feature-gate-vs-wait--ship-gated-unstable`: Ship it behind an unstable gate
- `unstable-feature-gate-vs-wait--alt1`: Wait until the API is ready before releasing it

Claims:
- `b-sR10-f004741-c2` · Voice: Friedel Ziegelmayer & Rüdiger Klaehn (iroh/n0 computer) · Source: https://iroh.computer/blog/iroh-1-0-0-rc-1 (`f004741`) · Date: 2026-05-27 · Locator: section "🛣️ Configurable path selection"
  - Quote: "The trait and the new types are gated behind the unstable-custom-transports feature. Keep in mind that this means they are not covered by the 1.0 stability guarantees and may break in future releases."
  - Paraphrase: the new PathSelector trait and its types ship now but stay behind the unstable-custom-transports flag and are explicitly excluded from the 1.0 stability guarantee
- `b-sR10-f004423-c2` · Voice: dignifiedquire (iroh/n0 computer) · Source: https://iroh.computer/blog/iroh-0-97-0-custom-transports-and-noq (`f004423`) · Date: 2026-03-16 · Locator: section "Custom Transports" / "Current status"
  - Quote: "As the name suggests, the custom transport API is unstable and will remain so for some time even after iroh 1.0 is released."
  - Paraphrase: the custom-transport API ships now but stays behind an unstable feature flag and is declared unstable even past the 1.0 stabilization line

## Question `unstable-marking-of-required-macros`

Should the proc-macro re-exports that a required language-level macro (e.g. `entry`, the crate's `main`) depends on be marked unstable along with everything else, or kept stable because the crate is unusable without them?

Positions:
- `unstable-marking-of-required-macros--p1`: Needs to stay usable
- `unstable-marking-of-required-macros--alt1`: Mark them unstable along with everything else

Claims:
- `b-sb08-f002517-c4` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/2900 (`f002517`) · Date: 2025-01-09 · Locator: comment 2025-01-09T13:55:03Z
  - Quote: "`entry` quite obviously needs to be stable - if you can't write `main`, how would you use the crate?"
  - Paraphrase: the entry macro must stay usable/stable since without it users cannot write main and thus cannot use the crate at all

## Question `verify-crates-io-against-source`

should crates.io-published bytes be checked against their source repository, and should such findings be released even incomplete

Positions:
- `verify-crates-io-against-source--p1`: Verify and publish raw
- `verify-crates-io-against-source--alt1`: Do not check published bytes
- `verify-crates-io-against-source--alt2`: withhold findings until reviewed

Claims:
- `a-sR14-f005287-c1` · Voice: Kornel · Source: https://mastodon.social/@kornel/112626463128422583 (`f005287`) · Date: 2024-06-16 · Locator: original post + reply to `@guenther`, 2024-06-16
  - Quote: "I've compared nearly all Rust crates.io crates to contents of their git repositories. Here's a dump of this data... I'm releasing the data, because I don't have time to review it all."
  - Paraphrase: built a comparator between crates.io tarballs and their git repos across nearly all of crates.io, and released the raw dataset rather than withholding it for private review first.

## Question `view-macro-native-control-flow`

should a component-templating macro (like Yew's `html!`) support native imperative control flow (`for`, `if`) written inline, or require iterator-adapter/functional-expression style?

Positions:
- `view-macro-native-control-flow--p1`: Add native `for`-loop syntax to `html!` alongside the existing iterator-adapter style, because it's "more natural."
- `view-macro-native-control-flow--alt1`: Require iterator-adapter or functional-expression style

Claims:
- `b-sR09-f003938-c1` · Voice: Mattuwu (Yew maintainer) · Source: https://yew.rs/blog/2025/11/29/release-0-22 (`f003938`) · Date: 2025-11-29 · Locator: yew.rs/blog/2025/11/29/release-0-22, "For-Loops in html!" section. · L712-L727.
  - Quote: "You can now use for-loops directly in the `html!` macro, making iteration more natural" — contrasted with the prior iterator-adapter form shown in the same post ("Before - using iterator adapters ... { for items.iter().map(|item| html! { <li>{ item }</li> }) }").
  - Paraphrase: add native `for`-loop syntax to `html!` alongside the existing iterator-adapter style, because it's "more natural."

## Question `warn-missing-edition`

Should rustc warn (or emit a note) whenever it is invoked without an explicit `--edition`, given how much edition-dependent behaviour has accumulated?

Positions:
- `warn-missing-edition--p1`: Support warn on missing edition
- `warn-missing-edition--alt1`: Do not warn when `--edition` is missing

Claims:
- `a-sa19-f009343-c2` · Voice: ekuber · Source: https://internals.rust-lang.org/t/code-compiles-on-playground-but-fails-when-passed-via-stdin-to-rustc/24393 (`f009343`) · Date: 2026-06-21 · Locator: linked PR rust-lang/rust#158102 (opened 2026-06-18), own reply 2026-06-21T22:53:55.156Z
  - Quote: "I implemented this as an undismisable note, which could also be a warning... The only people affected would be those explicitly comparing textual compiler output in scripts."
  - Paraphrase: Implemented the warning as an undismissable "note" rather than a lint specifically so `forbid`/`deny(warnings)` setups used by build probes aren't broken by it.
- `a-sa19-f009343-c1` · Voice: kpreid · Source: https://internals.rust-lang.org/t/code-compiles-on-playground-but-fails-when-passed-via-stdin-to-rustc/24393 (`f009343`) · Date: 2026-06-11 · Locator: reply, 2026-06-11T18:43:32.982Z
  - Quote: "rustc ought to warn whenever it is invoked without an --edition, because almost nobody writing a rustc invocation today should be using the 2015 edition."
  - Paraphrase: Given how significant edition differences have become, rustc should warn whenever invoked with no `--edition`, since almost no one today intends the 2015 default; notes a prior attempt stalled because many UI test suites set no edition and would gain new warnings.

## Question `wasi-path-workaround-vs-breaking-fix`

When a Rust WASM extension host hits a known-bad upstream WASI behavior (a spurious leading `/` in Windows paths from `std::env::current_dir`) that has both a correct-but-breaking extension-API fix on offer and a pragmatic non-breaking user-space workaround, should the project ship the pragmatic workaround now, or hold out for the correct breaking fix (with API versioning to preserve compatibility)?

Positions:
- `wasi-path-workaround-vs-breaking-fix--p1`: Pragmatic workaround preferred
- `wasi-path-workaround-vs-breaking-fix--p2`: Correct breaking fix preferred

Claims:
- `b-sb07-f002307-c2` · Voice: yakira-neko · Source: https://github.com/zed-industries/zed/issues/20559 (`f002307`) · Date: 2025-02-10 · Locator: issue #20559, comment 2025-02-10T09:59:32Z
  - Quote: "I believe that #14905 is the best way to solve this issue. Moreover, it is definitely a break[ing] change."
  - Paraphrase: argues the proper fix is the extension-API change in PR #14905, and even though it is a breaking change, compatibility should be handled by shipping a new extension-API version rather than settling permanently for the older workaround
- `b-sb07-f002307-c1` · Voice: lilnasy · Source: https://github.com/zed-industries/zed/issues/20559 (`f002307`) · Date: 2025-02-03 · Locator: issue #20559, comment 2025-02-03T09:43:55Z
  - Quote: "the fix wasn't ideal, but perfect shouldn't be the enemy of functional"
  - Paraphrase: after a workaround PR (#22600) was closed for not being an ideal fix, argues it's still worth shipping since it makes real-world extensions (Astro, Svelte) work now, and packages it as a community Windows build

## Question `wasip2-std-minimal-imports`

Should Rust's standard library on `wasm32-wasip2` import only the WASI interfaces a program uses, rather than the whole `wasi:cli` world whenever a simple std facility such as `format!` is used?

Positions:
- `wasip2-std-minimal-imports--p1`: Minimal imports
- `wasip2-std-minimal-imports--alt1`: Keep importing the whole `wasi:cli` world

Claims:
- `a-sT12-f008237-c2` · Voice: author of Ideas Reifying (ideas.reify.ing) · Source: https://ideas.reify.ing/en/blog/complete-guide-to-wasip2-for-rust-python-programmers (`f008237`) · Date: 2026-09-22 · Locator: § "Standard Libraries", last paragraph; § "Issues and Contribute", unresolved list
  - Quote: "the Rust compiler will include the whole wasi:cli world that includes some interfaces that are useless in this case"
  - Paraphrase: using a simple std facility makes the compiled component import the whole `wasi:cli` world, including useless interfaces such as `wasi:cli/env`; the author filed this as an issue that is still open

## Question `wasm-allocator-choice`

Keep the default wasm allocator, switch to a small one (wee_alloc), or drop allocation?

Positions:
- `wasm-allocator-choice--p1`: Switch to wee_alloc
- `wasm-allocator-choice--p2`: Eliminate-allocation/no_std
- `wasm-allocator-choice--p3`: Swap the default dlmalloc-derived allocator for wee_alloc (or drop dynamic allocation) when code size outweighs allocation speed

Claims:
- `a-sB02-f000256-c11` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "Shrinking .wasm Code Size" — "Avoid Allocation or Switch to wee_alloc"
  - Quote: "wee_alloc is an allocator designed for situations where you need some kind of allocator, but do not need a particularly fast allocator, and will happily trade allocation speed for smaller code size."
  - Paraphrase: the default dlmalloc-based allocator costs ~10KB; replacing it with wee_alloc trades allocation speed for saving most of that size, recommended when allocation can't be avoided entirely.
- `a-sB02-f000256-c12` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "Shrinking .wasm Size" — exercise on static mut globals
  - Quote: "This removes all dynamic allocation from our Game of Life implementation, and we can make it a #![no_std] crate that doesn't include an allocator."
  - Paraphrase: for a single-instance program, exporting operations on a static mut global (with double-buffering) removes all dynamic allocation, allowing a #![no_std] crate with no allocator dependency at all, for maximum size reduction.
- `b-bk02-f000256-c11` · Voice: rustwasm working group (Rust and WebAssembly book) [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: unknown (living doc) · Locator: § "Shrinking .wasm Code Size" → Avoid Allocation or Switch to wee_alloc
  - Quote: "wee_alloc is an allocator designed for situations where you need some kind of allocator, but do not need a particularly fast allocator, and will happily trade allocation speed for smaller code size."
  - Paraphrase: names the default allocator's ~10KB footprint as the cost of keeping it, and wee_alloc's slower allocation as the cost of switching, framing the choice explicitly as a speed-for-size trade.

## Question `wasm-bindgen-manual-vs-generated-glue`

When wrapping Rust types for wasm-bindgen, should a practitioner write manual `js_sys` conversions or lean into bindgen's generated glue (accepting its naming/wrapper conventions)?

Positions:
- `wasm-bindgen-manual-vs-generated-glue--p1`: Lean into bindgen glue
- `wasm-bindgen-manual-vs-generated-glue--alt1`: Manual `js_sys` conversions

Claims:
- `b-sb19-f005691-c1` · Voice: Brooklyn Zelenka · Source: https://notes.brooklynzelenka.com/Blog/Notes-on-Writing-Wasm (`f005691`) · Date: 2026-03-08 · Locator: § "Should You Write Manual Bindings?"
  - Quote: "I see a fair amount of code online that seems to prefer manual conversions with js_sys. This is a reasonable strategy, but I have found it to be time consuming and brittle."
  - Paraphrase: manual conversion with js_sys is a reasonable but time-consuming, brittle strategy; leaning into bindgen's glue (with naming conventions) buys better compile-time feedback

## Question `wasm-boundary-serde-vs-getters`

at the Rust/Wasm↔JavaScript FFI boundary, should code favor ergonomic serialization (serde-wasm-bindgen) or manual/structural field access (wasm-bindgen getters), trading ergonomics against performance?

Positions:
- `wasm-boundary-serde-vs-getters--p1`: Choose serde-wasm-bindgen vs wasm-bindgen getters based on hot/cold path
- `wasm-boundary-serde-vs-getters--alt1`: Always serde-wasm-bindgen
- `wasm-boundary-serde-vs-getters--alt2`: always wasm-bindgen getters

Claims:
- `a-sa26-f011460-c3` · Voice: Andrew Jakubowicz · Source: https://youtube.com/watch?v=wDoqQkEylY8 (`f011460`) · Date: 2026-06-11 · Locator: ~25:39
  - Quote: "from serving some GitHub crates, I found people are mostly doing the like the right thing, basically. Using serde-wasm-bindgen for cold paths, config initialization, and then using wasm-bindgen getters... if they're needed"
  - Paraphrase: after surveying GitHub crates, found people mostly using serde-wasm-bindgen (more ergonomic, more allocation) for cold paths like config initialization, and wasm-bindgen getters/reflection (faster, less ergonomic) for hot paths

## Question `wasm-bundler-choice`

Which JS bundler/dev-server should front a Rust+wasm web app: webpack, an alternative bundler, or none?

Positions:
- `wasm-bundler-choice--p1`: Webpack(chosen, "for convenience")
- `wasm-bundler-choice--alt1`: Parcel or Rollup
- `wasm-bundler-choice--alt2`: no bundler

Claims:
- `a-sB02-f000256-c17` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "Hello, World!" — "Install the dependencies"
  - Quote: "webpack is not required for working with Rust and WebAssembly, it is just the bundler and development server we've chosen for convenience here."
  - Paraphrase: the tutorial's template uses webpack as bundler/dev-server, stating this isn't required — Parcel and Rollup are named as also supporting wasm as ES modules, and using Rust+wasm with no bundler at all is called viable — webpack is picked "for convenience."

## Question `wasm-capabilities-explicit-vs-ambient`

Should a Wasm component sandbox grant capabilities by default (ambient authority), or require every capability — including for middleware and dependencies — to be explicitly listed?

Positions:
- `wasm-capabilities-explicit-vs-ambient--p1`: Middleware components get no ambient authority; every capability a middleware needs (e.g. an outbound host) must be explicitly listed in the trigger's inherit_configuration, exactly like any other component dependency
- `wasm-capabilities-explicit-vs-ambient--alt1`: Grant ambient authority by default

Claims:
- `b-sR11-f005050-c1` · Voice: The Spin Project · Source: https://spinframework.dev/blog/announcing-spin-4-1 (`f005050`) · Date: 2026-08-26 · Locator: "Middleware doesn't get a free pass on capabilities" section
  - Quote: "Middleware gets no ambient authority."
  - Paraphrase: an auth middleware can reach an endpoint only because the underlying component grants that capability and the trigger explicitly inherits it; otherwise the middleware gets nothing

## Question `wasm-components-for-interop`

Wasm components (WIT) or language SDKs and C-ABI for interop?

Positions:
- `wasm-components-for-interop--wasm-components`: Wasm components
- `wasm-components-for-interop--alt1`: Language-specific SDKs or C-ABI FFI

Claims:
- `a-sa07-f003922-c1` · Voice: Ian McDonald · Source: https://spinframework.dev/blog/mcp-with-wasmcp (`f003922`) · Date: 2025-11-25 · Locator: blog post, § "Wasmcp"
  - Quote: "Tool calling implemented by an AI SDK couples tool instances to an application's runtime... We need a layer of indirection between models and their tools."
  - Paraphrase: argues that SDK-based tool calling couples tool instances to the calling application's runtime and can't be reused externally, and that composing independently-built WebAssembly components (regardless of source language) solves discovery, portability and sandboxing better
- `a-sT12-f008237-c1` · Voice: author of Ideas Reifying (ideas.reify.ing; not named in the text) · Source: https://ideas.reify.ing/en/blog/complete-guide-to-wasip2-for-rust-python-programmers (`f008237`) · Date: 2026-09-22 · Locator: § "Compose with wasmbuilder.app", last paragraph; § "Personal Notes and Beyond WASIp2", paragraph 1
  - Quote: "The foundation of software interops is still legacy C ABIs, which are not only fragile but also dangerous."
  - Paraphrase: composing components through compatible WIT interfaces relieves the pain of gluing programs through C ABIs, which the author calls fragile and dangerous as a foundation for interop

## Question `wasm-core-sum-types`

Should core Wasm eventually gain a primitive sum-type / tagged-union construct (with e.g. a `br_table`-like case-matching instruction), or is representing variants as `struct` subtyping trees in a shared `rec` group sufficient?

Positions:
- `wasm-core-sum-types--p1`: Primitive sum types worthwhile
- `wasm-core-sum-types--p2`: Marginal benefit over encoding

Claims:
- `a-sa05-f003074-c5` · Voice: rossberg · Source: https://github.com/WebAssembly/component-model/issues/525 (`f003074`) · Date: 2025-06-16 · Locator: comment @rossberg 2025-06-16T21:05:40Z
  - Quote: "Saving the cast would essentially require adding a case construct to Wasm, which would be quite a bit of machinery. Other than that, sum types do not offer a hell lot of relevant generic optimisations"
  - Paraphrase: a custom type descriptor can already store an integer tag for `br_table` dispatch without wasting per-variant space, so primitive sum types would mainly save the trailing cast check, which requires substantial new Wasm machinery for limited additional gain
- `a-sa05-f003074-c4` · Voice: fitzgen · Source: https://github.com/WebAssembly/component-model/issues/525 (`f003074`) · Date: 2025-06-16 · Locator: comment @fitzgen 2025-06-16T18:35:42Z
  - Quote: "The most immediate benefit that first-class sum types would give us over shoe-horning sum types into struct subtypes would be a br_table-like instruction for exhaustively matching on cases"
  - Paraphrase: first-class sum types would let compilers emit a `br_table`-like exhaustive match instead of a chain of `br_on_cast` checks, which is easier to optimize and lets tools like binaryen reason over a closed case set

## Question `wasm-instantiate-streaming-vs-bytes`

once a `.wasm` file is already fully loaded into memory as bytes/a blob, should the loader still route it through the streaming compile/instantiate API, or fall back to the plain bytes-based `instantiate`?

Positions:
- `wasm-instantiate-streaming-vs-bytes--p1`: Drop the streaming wrapper when the bytes are already in hand; it buys nothing there
- `wasm-instantiate-streaming-vs-bytes--alt1`: Route through the streaming instantiate API anyway

Claims:
- `b-sR09-f003815-c1` · Voice: RReverser (wasm-bindgen maintainer) · Source: https://github.com/wasm-bindgen/wasm-bindgen/pull/4795 (`f003815`) · Date: 2025-11-14 · Locator: wasm-bindgen/wasm-bindgen#4795, comment 2025-11-14T13:35:08Z. · L657-L661.
  - Quote: "There's no need for the complex wrapping into a `Response` - `instantiateStreaming` doesn't have any benefits when we already loaded the whole file as a blob. Let's just revert to the regular `instantiate` which can take the bytes directly."
  - Paraphrase: drop the streaming wrapper when the bytes are already in hand; it buys nothing there.

## Question `wasm-monolithic-vs-small-components`

Within one Wasm application, should logic be kept in a single monolithic component, or decoupled into several small components composed via WIT interfaces?

Positions:
- `wasm-monolithic-vs-small-components--p1`: Self-contained pieces of application logic (e.g. a classifier) should be split into their own Wasm component, composed into the app via a WIT interface and a declared spin.toml dependency, rather than living inline in the HTTP-triggered component
- `wasm-monolithic-vs-small-components--alt1`: One monolithic component

Claims:
- `b-sR11-f005053-c1` · Voice: Thorsten Hans · Source: https://spinframework.dev/blog/component-composition-spin-4-0 (`f005053`) · Date: 2026-08-27 · Locator: "Recap" section
  - Quote: "By decoupling the core classification logic into its own Wasm component, we kept the HTTP control flow lean, standard, and easy to maintain"
  - Paraphrase: decoupling the classification logic into its own component "kept the HTTP control flow lean, standard, and easy to maintain," with WIT files as "the single source of truth" for the boundary

## Question `wasm-panic-hook`

For panics on wasm32-unknown-unknown, install a panic hook (console_error_panic_hook) or accept the default trap message?

Positions:
- `wasm-panic-hook--p1`: Install panic hook
- `wasm-panic-hook--alt1`: Accept the default trap message, no hook

Claims:
- `a-sB02-f000256-c16` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "Debugging Rust-Generated WebAssembly" — "Logging Panics"
  - Quote: "Rather than getting cryptic, difficult-to-debug RuntimeError: unreachable executed error messages, this gives you Rust's formatted panic message."
  - Paraphrase: installing console_error_panic_hook turns a cryptic "RuntimeError: unreachable executed" trap into Rust's actual formatted panic message in the console; the tutorial's own exercise has the reader remove the hook and asks "Not as useful is it?" as the reason to keep it.

## Question `wasm-panic-unwind-vs-abort`

For Rust compiled to WebAssembly (wasm32-unknown-unknown), should panics use the platform default of panic=abort, or panic=unwind (running destructors and preserving instance state across a single failed request)?

Positions:
- `wasm-panic-unwind-vs-abort--p1`: Panic unwind for reliability
- `wasm-panic-unwind-vs-abort--alt1`: panic=abort (the platform default)

Claims:
- `a-sa12-f004598-c1` · Voice: Guy Bedford, Hood Chatham, and Logan Gatlin (Cloudflare Workers/wasm-bindgen team) · Source: https://blog.cloudflare.com/making-rust-workers-reliable (`f004598`) · Date: 2026-04-22 · Locator: blog post, § "Implementing panic=unwind with WebAssembly Exception Handling"
  - Quote: "To recover from panics without discarding instance state, we needed panic=unwind support for wasm32-unknown-unknown in wasm-bindgen"
  - Paraphrase: added panic=unwind support to wasm-bindgen/Rust Workers via the WebAssembly Exception Handling proposal because panic=abort's default full-reinitialization recovery wipes in-memory state for stateful workloads like Durable Objects; shipped behind a flag in Rust Workers 0.8.0 with plans to make it the default

## Question `wasm-precise-traps-store-tearing`

On hardware with "store-tearing" behavior, where a partial store can have observable side effects before trapping, should a WebAssembly runtime pay a load-before-store performance cost to guarantee precise, spec-compliant trap semantics, or accept imprecise traps as an acceptable, mostly theoretical risk on rare/low-power hardware?

Positions:
- `wasm-precise-traps-store-tearing--p1`: Load before store opt in
- `wasm-precise-traps-store-tearing--alt1`: Accept imprecise traps

Claims:
- `a-02-f001181-c1` · Voice: cfallin · Source: https://github.com/bytecodealliance/wasmtime/pull/8221 (`f001181`) · Date: 2024-03-22 · Locator: PR description
  - Quote: "This PR implements the idea first proposed [...] namely to prepend a load of the same size to every store. The idea is that if the store will trap, the load will as well."
  - Paraphrase: implements precise store-trap semantics (prepending a same-size load before every store) on architectures with store tearing (ARMv8, RISC-V), shipped off by default, accepting a measured ~2% cost on Apple M2 Pro, pending Wasm spec clarification

## Question `wasm-runtime-swap-vs-host-target`

when compiling an async networking stack to a non-native target, should you swap the async runtime/networking primitives for target-specific shims, or keep the existing runtime (tokio) and target a platform that can host it directly?

Positions:
- `wasm-runtime-swap-vs-host-target--p1`: The two Wasm targets warrant different answers — swap out tokio for a browser shim when targeting `wasm32-unknown-unknown`, but for `wasm32-wasip2/3` compile most of the stack unchanged and depend on tokio gaining support for that platform instead
- `wasm-runtime-swap-vs-host-target--alt1`: Always swap in target-specific shims
- `wasm-runtime-swap-vs-host-target--alt2`: always keep tokio and target a platform that hosts it

Claims:
- `b-sR05-f002177-c1` · Voice: matheus23 (n0-computer/iroh maintainer) · Source: https://github.com/n0-computer/iroh/issues/2799 (`f002177`) · Date: 2026-04-27 · Locator: n0-computer/iroh#2799, comment 2026-04-27T08:40:49Z. · L1518-L1524.
  - Quote: "Instead of swapping out tokio with another runtime (wasm-bindgen-futures/'the browser' in that case)... we'd instead try to compile most of the stack to wasm32-wasip2/3... So this means we'd be dependent on tokio to work under that platform and for it to support UDP/TCP sockets."
  - Paraphrase: the two Wasm targets warrant different answers — swap out tokio for a browser shim when targeting `wasm32-unknown-unknown`, but for `wasm32-wasip2/3` compile most of the stack unchanged and depend on tokio gaining support for that platform instead.

## Question `wasm-undefined-symbols-error`

Should Rust's WebAssembly targets treat undefined symbols as a hard link error by default (matching native platforms), even though some code intentionally relies on the current silent-import behavior?

Positions:
- `wasm-undefined-symbols-error--p1`: Remove --allow-undefined as the wasm-target default; undefined symbols should error at build time like on native platforms
- `wasm-undefined-symbols-error--alt1`: Keep the silent-import default (`--allow-undefined`)

Claims:
- `b-sb23-f009737-c1` · Voice: Alex Crichton · Source: https://blog.rust-lang.org/2026/04/04/changes-to-webassembly-targets-and-handling-undefined-symbols (`f009737`) · Date: 2026-04-04 · Locator: "What's wrong with --allow-undefined?" section
  - Quote: "All native platforms consider undefined symbols to be an error by default, and thus by passing --allow-undefined rustc is introducing surprising behavior on WebAssembly targets."
  - Paraphrase: the current default silently turns undefined/typo'd symbols into WebAssembly imports instead of producing a build error, which "kicks the can down the road" from where a mistake is introduced to where it surfaces (often as a confusing runtime failure); removing it aligns wasm with how all other platforms already behave, and existing intentional users can opt back in per-symbol

## Question `web-api-wrapper-raw-vs-rust-types`

When wrapping a browser Web API (e.g. `UrlSearchParams`) inside a Rust frontend-framework hook, should the API surface the raw web-sys type or convert it to an idiomatic Rust collection?

Positions:
- `web-api-wrapper-raw-vs-rust-types--p1`: Convert to rust collection
- `web-api-wrapper-raw-vs-rust-types--alt1`: Surface the raw `web-sys` type

Claims:
- `a-sR07-f002271-c1` · Voice: lukechu10 · Source: https://github.com/sycamore-rs/sycamore/pull/752 (`f002271`) · Date: 2024-11-03 · Locator: comment on router.rs (2024-11-03T22:58:52Z)
  - Quote: "we should return a `HashMap<String, String>` from search params to values"
  - Paraphrase: a hook exposing browser search params should return a `HashMap<String, String>` rather than the raw `UrlSearchParams` handle

## Question `web-framework-actor-vs-tower`

Which Rust web framework to default to: Actix (actor model) or Axum (Tower)?

Positions:
- `web-framework-actor-vs-tower--p1`: Actix-default for web, Clap for CLI
- `web-framework-actor-vs-tower--p2`: Axum's Tower-based design is often preferred over Actix Web's actor model

Claims:
- `a-sa26-f011605-c2` · Voice: Joshua Mo · Source: https://shuttle.rs/blog/2023/12/06/using-axum-rust (`f011605`) · Date: 2023-12-06 (updated 2025-07-04) · Locator: FAQ "What is the difference between Axum and Actix Web?"
  - Quote: "Actix Web uses the actor model and has its own mature middleware system. Both are fast and production-ready, but Axum's design philosophy is often preferred for its simplicity and tight integration with Tokio"
  - Paraphrase: both frameworks are fast and production-ready, but Axum's simplicity and tight Tokio integration is "often preferred" over Actix Web's actor-model design
- `a-sB01-f000149-c2` · Voice: Noah Gift · Source: https://nogibjj.github.io/rust-tutorial (`f000149`) · Date: 2023 (course release date stated in source) · Locator: Chapter 1, project spec bullet on frameworks
  - Quote: "unless you have a compelling reason to switch to a new framework"
  - Paraphrase: Directs students to default to Clap (CLI) and Actix (web) "unless you have a compelling reason to switch to a new framework"

## Question `web-framework-macro-free-api`

should a Rust web framework favor a macro-free, type/extractor-driven API design, or a macro-based route/handler declaration syntax?

Positions:
- `web-framework-macro-free-api--p1`: Macro-free API design is a distinguishing strength
- `web-framework-macro-free-api--alt1`: A macro-based route and handler declaration syntax

Claims:
- `a-sa26-f011605-c1` · Voice: Joshua Mo · Source: https://shuttle.rs/blog/2023/12/06/using-axum-rust (`f011605`) · Date: 2023-12-06 (updated 2025-07-04) · Locator: heading "Getting Started with Axum: Building REST APIs in Rust" (intro paragraph)
  - Quote: "What makes Axum stand out in the Rust programming landscape is its macro free api design, predictable error handling model, and own middleware system built on Tower"
  - Paraphrase: Axum stands out among Rust web frameworks specifically for its macro-free API design, predictable error handling, and Tower-based middleware

## Question `web-session-store-default`

Should a Rust web framework default new apps to a client-side (encrypted + signed cookie) session store for low-friction onboarding, or push toward a server-side session store (e.g. via `tower-sessions`) because client-stored session data cannot be force-invalidated or have permissions changed on the fly?

Positions:
- `web-session-store-default--p1`: Cookie store default with encryption
- `web-session-store-default--p2`: Server side store preferred

Claims:
- `b-sb04-f001365-c2` · Voice: schungx · Source: https://github.com/loco-rs/loco/issues/561 (`f001365`) · Date: 2024-06-24 · Locator: issue #561, comment 2024-06-24T06:50:58Z
  - Quote: "there is no way to force-invalidate a session, or to change permissions on the fly"
  - Paraphrase: objects that data stored on the client cannot be force-invalidated or have permissions changed on the fly, so whatever effort is saved by skipping a server-side store is negated by that inflexibility
- `b-sb04-f001365-c1` · Voice: jondot · Source: https://github.com/loco-rs/loco/issues/561 (`f001365`) · Date: 2024-06-24 · Locator: issue #561, comment 2024-06-24T06:14:39Z
  - Quote: "I believe we should do the same by _starting with storing inside the cookie_ both encrypted and signed"
  - Paraphrase: following Rails' precedent, argues Loco should start new apps with an encrypted-and-signed cookie session store (switchable later via `tower-sessions`) to keep initial friction low, even though Rails itself calls the choice "controversial"
- `b-sb04-f001365-c3` · Voice: yinho999 · Source: https://github.com/loco-rs/loco/issues/561 (`f001365`) · Date: 2025-04-02 · Locator: issue #561, comment 2025-04-02T04:59:56Z
  - Quote: "the encrypted cookie is not a good practice in production environment since it can cause reply attacks and other vulnerabilities"
  - Paraphrase: states plainly that encrypted cookies are not good practice in production because they can enable replay attacks and similar vulnerabilities, and that storing sensitive data server-side is always the better choice

## Question `web-wasm-target-workaround-vs-target`

Facing the absence of a proper Web-WASM Rust target, should the ecosystem work around it now with crate-feature plumbing, or push to get the target itself built first?

Positions:
- `web-wasm-target-workaround-vs-target--p1`: Pursue a real Web-WASM target instead of another workaround
- `web-wasm-target-workaround-vs-target--p2`: Ship the workaround now, a new target isn't realistic soon

Claims:
- `a-sa06-f003558-c2` · Voice: newpavlov · Source: https://github.com/wasm-bindgen/wasm-bindgen/issues/4667 (`f003558`) · Date: 2025-09-19 · Locator: comment 2025-09-19T12:53:59Z; 2025-09-19T13:06:16Z
  - Quote: "I don't have any hope for getting it anytime soon"
  - Paraphrase: says there has been zero progress on a Web WASM target in about 4 years, `getrandom` needs a solution that works with the current stable Rust and declared MSRV, and hypothetical language changes are out of scope for this issue
- `a-sa06-f003558-c1` · Voice: CryZe · Source: https://github.com/wasm-bindgen/wasm-bindgen/issues/4667 (`f003558`) · Date: 2025-09-19 · Locator: comment 2025-09-19T12:38:24Z
  - Quote: "Shouldn't we finally discuss a proper wasm32-web / wasm32-bindgen target instead"
  - Paraphrase: argues the root cause is the lack of a way to signal wasm-bindgen usage, and that a proper `wasm32-web` target would fix this class of problem generally, now that the project has active maintainers again

## Question `what-counts-as-semver-breaking`

What counts as a semver-breaking change for a published Rust crate's public API?

Positions:
- `what-counts-as-semver-breaking--p1`: Enum variant addition breaks without non exhaustive
- `what-counts-as-semver-breaking--p2`: Dependency type leakage forces lockstep major bump
- `what-counts-as-semver-breaking--p3`: Msrv bump is breaking

Claims:
- `b-bk03-f000267-c12` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Changelog Guidelines § Part 3, "What is breaking for library consumers?"
  - Quote: "Adding a variant to a public enum that is not marked #[non_exhaustive] is also breaking: downstream match expressions that were exhaustive stop compiling."
  - Paraphrase: adding a variant to a public enum that is not marked #[non_exhaustive] is classified as a breaking change, because downstream match expressions that were previously exhaustive stop compiling
- `b-bk03-f000267-c13` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Changelog Guidelines § Dependency updates
  - Quote: "That lockstep is breaking, so the fragment kind is breaking and the release bumps the major version."
  - Paraphrase: a dependency bump only needs a changelog entry, and forces a major-version bump of the crate itself, when the dependency's own semver-incompatible version change exposes types that appear in the crate's public API, since two incompatible versions of the same crate can't unify for downstream consumers; a dependency used only internally needs no entry at all
- `b-bk03-f000267-c14` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Changelog Guidelines § Part 4, Compatibility
  - Quote: "an MSRV bump is itself a breaking change"
  - Paraphrase: raising the minimum supported Rust version is itself classified as a breaking change for a crate (and is listed as "Yes/Yes" for both crate and zebrad changelogs), rather than a minor or patch-level change

## Question `wit-dependency-keyword-design`

should WIT syntax name a dependency-on-implementation with dedicated keywords (`locked-dep`/`unlocked-dep`), or with one generic keyword (`dependency`) whose lock state is inferred from the version syntax that follows it?

Positions:
- `wit-dependency-keyword-design--p1`: Favors the single `dependency` keyword with locked/unlocked inferred from the trailing syntax, for regularity and to keep vocabulary aligned with how package managers already use the word "dependency."
- `wit-dependency-keyword-design--alt1`: Dedicated keywords (`locked-dep`, `unlocked-dep`)

Claims:
- `b-sR05-f001983-c1` · Voice: Luke Wagner (Fastly; W3C/Bytecode Alliance component-model co-designer) · Source: https://github.com/WebAssembly/component-model/pull/393 (`f001983`) · Date: 2024-09-10 · Locator: WebAssembly/component-model#393, comments 2024-09-10T20:00:17Z and 2024-09-11T19:36:18Z. · L406-L465.
  - Quote: "What if we used just the word 'dependency' and inferred 'locked' vs. 'unlocked'/'range' from the syntax after the `@`." And: "the word 'dependency' is used by package managers and their associated build-config files (e.g., `npm`/`package.json`, `cargo`/`Cargo.toml`, etc) to exclusively refer to *implementations*."
  - Paraphrase: favors the single `dependency` keyword with locked/unlocked inferred from the trailing syntax, for regularity and to keep vocabulary aligned with how package managers already use the word "dependency."

## Question `wit-export-direct-vs-interface`

When defining a Wasm component's WIT world, should a function be exported directly from the world, or wrapped inside a named interface that the world then exports?

Positions:
- `wit-export-direct-vs-interface--p1`: Wrap related functions inside a named interface and export the interface, rather than exporting a raw function from the world
- `wit-export-direct-vs-interface--alt1`: Export the function directly from the world

Claims:
- `a-sR08-f003033-c1` · Voice: Tim McCallum (Bytecode Alliance) · Source: https://bytecodealliance.org/articles/invoking-component-functions-in-wasmtime-cli (`f003033`) · Date: 2025-05-21 · Locator: "WIT" section
  - Quote: "the recommended best practice is to wrap related functions inside an interface, which you then export from your world"
  - Paraphrase: while a world can export a bare function directly, doing so isn't the recommended approach; wrapping functions in an interface is more modular, extensible, and matches how WIT is used in real multi-function components

## Question `work-stealing-vs-thread-per-core`

For async Rust HTTP servers, is a work-stealing runtime (Tokio's default) or an executor-per-thread/"thread-per-core" runtime (Glommio, or Tokio/Smol configured with a `LocalRuntime`/`LocalExecutor` per thread) the better architecture — and is either one simply faster, or is the right choice workload-dependent?

Positions:
- `work-stealing-vs-thread-per-core--p1`: Choice is workload dependent not universally faster
- `work-stealing-vs-thread-per-core--alt1`: Work-stealing is better
- `work-stealing-vs-thread-per-core--alt2`: thread-per-core is better

Claims:
- `a-sa18-f009026-c1` · Voice: Caio (c410-f3r) · Source: https://c410-f3r.github.io/thoughts/work-stealing-vs-executor-per-thread-evaluating-different-http-server-workloads-with-tokio-smol-and-glommio (`f009026`) · Date: 2026-08-05 · Locator: "Final words" section, after 360 benchmarked configurations across 90 scenarios
  - Quote: "the benchmarks aren't conclusive. The choice between Executor-Per-Thread and Work-Stealing doesn't seem like a simple matter of \"which is faster\" but rather which architecture best aligns with your specific application logic."
  - Paraphrase: ran balanced/unbalanced, low/medium/high-scale, CPU- through IO-heavy HTTP/2 workloads across tokio (work-stealing and executor-per-thread configurations), smol-ept and glommio-ept; found io_uring (Glommio) did not strictly outperform epoll-based runtimes even under the unbalanced "noisy neighbor" scenario designed to favor work-stealing, and that tokio's work-stealing configuration specifically showed unexplained throughput anomalies at 8/12 threads with no logged errors on either side; concludes the results are inconclusive on "which is faster" and that the right choice depends on the application's own workload shape

## Question `wrap-third-party-types-in-public-api`

Should a crate depend on a third-party type directly in its public API, or wrap it behind a local newtype/abstraction?

Positions:
- `wrap-third-party-types-in-public-api--p1`: Abstract over third party crate choice
- `wrap-third-party-types-in-public-api--alt1`: Use the third-party type directly in the public API

Claims:
- `b-bk03-f000267-c17` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Contextual Difficulty Validation RFC § Fundamental data types
  - Quote: "Zebra abstracts over the chosen u256 implementation using its ExpandedDifficulty type."
  - Paraphrase: because Rust has no standard u256 type, Zebra picks one of several third-party crate implementations but does not expose it directly — it wraps the chosen implementation behind its own ExpandedDifficulty type, so the underlying crate choice stays swappable

## Question `xcframework-tooling-vs-hand-built`

When assembling a Rust static library into an XCFramework for Swift distribution, should you hand-build the XCFramework's directory structure or use Apple's `xcodebuild -create-xcframework` tooling?

Positions:
- `xcframework-tooling-vs-hand-built--p1`: Use Apple's official `xcodebuild -create-xcframework` rather than hand-assembling the XCFramework directory
- `xcframework-tooling-vs-hand-built--alt1`: Hand-assemble the XCFramework directory

Claims:
- `a-sa27-f012237-c2` · Voice: Ian Wagner · Source: https://stadiamaps.com/news/ferrostar-building-a-cross-platform-navigation-sdk-in-rust-part-2 (`f012237`) · Date: 2024-12-04 · Locator: section "Generating the XCFramework", opening paragraph
  - Quote: "Some teams actually do this by hand, since it's a relatively simple structure, but we'll stick to Apple's official tooling."
  - Paraphrase: XCFramework's on-disk structure is simple enough that some teams build it by hand, but Stadia Maps scripts `xcodebuild -create-xcframework` to combine the per-target static libraries, headers and module map instead of replicating that structure manually
