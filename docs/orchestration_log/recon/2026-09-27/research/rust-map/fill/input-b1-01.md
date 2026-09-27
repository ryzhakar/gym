# Blind fill input, batch 1, file 01 of 13

For each Claim below, name the one Position of its Question that the Claim supports (a Position id from the list), or `none` if it supports none of them. The Claims are in random order.

## Question `absolute-instant-periodic-timing`

For repeated/periodic timing in async embedded Rust, should each wait be computed from an accumulating absolute instant, or from a fresh relative delay each iteration?

Positions:
- `absolute-instant-periodic-timing--p1`: Accumulate absolute instant to avoid drift
- `absolute-instant-periodic-timing--alt1`: Delay by a fresh relative duration each iteration

Claims:
- `a-sB04-f000227-c2` · Voice: RTIC developers · Source: https://rtic.rs/ (`f000227`) · Date: undated (living doc, v2.x) · Locator: "2.8. Delay and Timeout using Monotonics"
  - Quote: "Any additional delays incurred as we iterate around this loop are compensated for by delaying until 'previous + 1000' as opposed to 'now + 1000' (which would cause our loop timing to drift)."
  - Paraphrase: Recommends incrementing a stored absolute instant and calling delay_until against it, instead of delaying by a fresh relative duration each loop iteration, because relative delays accumulate drift from the work done each iteration

## Question `actor-vs-shared-locks`

In an async networking server, should connection management go through an actor or through shared data structures with locks?

Positions:
- `actor-vs-shared-locks--p1`: Remove the actor; use lock-based data structures
- `actor-vs-shared-locks--alt1`: Keep an actor for connection management

Claims:
- `b-sT05-f002550-c2` · Voice: ramfox, matheus23 · Source: https://iroh.computer/blog/iroh-0-31-0-back-to-fighting-fit (`f002550`) · Date: 2025-01-15 · Locator: § Deadlock on the relay (not released)
  - Quote: "removing an unnecessary actor and using some higher-order data structures"
  - Paraphrase: refactor removed "an unnecessary actor" to cut layers, then needed a follow-up to fix a deadlock

## Question `ad-hoc-special-case-vs-general-mechanism`

When migrating a compiler backend to a new, more systematic instruction-assembler abstraction, and an instruction needs special-cased handling (e.g. custom flag-setting/printing) that the new abstraction doesn't yet cleanly support, should the PR merge the ad hoc special case now or block on designing the general mechanism first?

Positions:
- `ad-hoc-special-case-vs-general-mechanism--p1`: Resist ad hoc design general solution first
- `ad-hoc-special-case-vs-general-mechanism--p2`: Merge as is and refactor later

Claims:
- `b-sb09-f003052-c1` · Voice: abrown · Source: https://github.com/bytecodealliance/wasmtime/pull/10836 (`f003052`) · Date: 2025-05-28 · Locator: comment @abrown 2025-05-28T17:56:16Z
  - Quote: "I'm not a big fan of this; the `lock_` stuff below already seemed unfortunate but now this opens a whole new can of worms... I just think we should think through a better long-term solution."
  - Paraphrase: objects to adding another special-cased "custom" printing mechanism for compare instructions' flags, noting the existing `lock_` special case was already unfortunate, and argues for a better long-term solution before merging.
- `b-sb09-f003052-c2` · Voice: abrown · Source: https://github.com/bytecodealliance/wasmtime/pull/10836 (`f003052`) · Date: 2025-06-02 · Locator: comment @abrown 2025-06-02T17:48:01Z
  - Quote: "Ok, let's leave this as-is for now but we'll need to refactor to something more like the `custom` logic introduced by @alexcrichton..."
  - Paraphrase: shifts to accepting the current approach for now, deferring the cleanup to a follow-up refactor building on a separate "custom" logic PR by another contributor.
- `b-sb09-f003052-c3` · Voice: rahulchaphalkar · Source: https://github.com/bytecodealliance/wasmtime/pull/10836 (`f003052`) · Date: 2025-06-03 · Locator: comment @rahulchaphalkar 2025-06-03T16:18:30Z
  - Quote: "I agree with the idea that lets push the external printing patch first, and then rebase on that."
  - Paraphrase: agrees to sequence the work by letting the external-printing refactor PR land first and rebasing this PR on top of it, rather than blocking this PR on redesigning the mechanism inline.

## Question `additive-features`

Should a crate's Cargo feature flags always be strictly additive (the crate builds with any subset of features, including none), or is it acceptable for disabling a feature (like `std`) to change what builds successfully on certain targets?

Positions:
- `additive-features--p1`: Features must stay additive
- `additive-features--p2`: Disabling a feature can change buildability

Claims:
- `b-sb10-f003186-c2` · Voice: salmans · Source: https://github.com/bytecodealliance/wasmtime/pull/11152 (`f003186`) · Date: 2025-06-27 · Locator: PR description, 2025-06-27T21:18:19Z
  - Quote: "This fix will disable standard library features for dependents that use wasmtime with `default-features = false`."
  - Paraphrase: the fix intentionally disables standard-library-dependent features for dependents using `default-features = false`, changing what builds under that configuration
- `b-sb10-f003186-c1` · Voice: alexcrichton · Source: https://github.com/bytecodealliance/wasmtime/pull/11152 (`f003186`) · Date: 2025-06-30 · Locator: comment 2025-06-30T18:19:37Z
  - Quote: "the `std` feature should not be necessary to just build the crate, even on Linux/Windows targets. In essence these CI changes shouldn't be necessary."
  - Paraphrase: the `std` feature should not be required just to build the crate on Linux/Windows targets; requiring it defeats the point of feature gating

## Question `affine-types-vs-formal-verification`

Does Rust's affine-type system provide sufficient correctness guarantees, or is further formal verification (linear/dependent types, model checkers) needed on top of it?

Positions:
- `affine-types-vs-formal-verification--p1`: Needs stronger formal guarantees
- `affine-types-vs-formal-verification--p2`: Combine rust with formal tools

Claims:
- `b-sb19-f005743-c5` · Voice: madhadron · Source: https://lobste.rs/s/67tqpz (`f005743`) · Date: 2026-06-02 · Locator: comment at 2026-06-02T12:39:44-05:00
  - Quote: "Or we could insist on something like Frama C or other model checkers integrated in."
  - Paraphrase: proposes integrated model checkers (e.g. Frama-C) as the stronger alternative/complement to a type system
- `b-sb19-f005743-c6` · Voice: wucke13 · Source: https://lobste.rs/s/67tqpz (`f005743`) · Date: 2026-06-05 · Locator: comment at 2026-06-05T04:25:37-05:00
  - Quote: "I believe TrustInSoft offers a Frama C port to Rust, so, not mutually exclusive with the use of Rust!"
  - Paraphrase: formal-verification tooling (TrustInSoft's Frama-C port) can sit alongside Rust rather than replace it
- `b-sb19-f005743-c4` · Voice: toastal · Source: https://lobste.rs/s/67tqpz (`f005743`) · Date: 2026-06-02 · Locator: comment at 2026-06-02T12:14:03-05:00
  - Quote: "Affine types do not offer the same guarantees as linear types + dependent types."
  - Paraphrase: Rust's affine types are weaker than linear+dependent type guarantees

## Question `ai-agents-and-explicit-syntax`

Does the rise of AI coding agents change the cost/benefit calculus for verbose, explicit call-site syntax (like named arguments) that was previously judged not worth its typing cost for human authors?

Positions:
- `ai-agents-and-explicit-syntax--p1`: Agents shift calculus toward explicit named syntax
- `ai-agents-and-explicit-syntax--alt1`: Agents do not change the case against explicit named syntax

Claims:
- `a-sa18-f009104-c3` · Voice: Steve Klabnik · Source: https://steveklabnik.com/writing/arguing-about-arguments (`f009104`) · Date: 2026-09-21 · Locator: "I'm okay with named parameters now" section
  - Quote: "what changed my opinion is coding agents, actually... 'What's good for humans is true for agents' strikes again."
  - Paraphrase: attributes his change of mind to coding agents — since he is "not typing myself anymore," the verbosity cost of named arguments no longer weighs against their call-site clarity benefit, and reasons the clarity gain is if anything larger for an agent reading the call site than for a human, while explicitly noting he hasn't run real evals on this

## Question `ai-authored-community-contributions`

Should a Rust project or venue accept AI-authored contributions and content (proposals, PRs, newsletters), and under what policy: ban, disclosure, accountability or review?

Positions:
- `ai-authored-community-contributions--reject-ai-authored-content`: Undesirable: it erases the author's voice, or readers do not want it
- `ai-authored-community-contributions--acceptable-if-substance-is-own`: Acceptable when the substance is the contributor's own and the model only composes
- `ai-authored-community-contributions--acceptable-if-marked`: Assistance is fine; unmarked AI content is the problem
- `ai-authored-community-contributions--human-must-stay-accountable`: Acceptable only with the human author in the loop and accountable, per project policy
- `ai-authored-community-contributions--manage-through-review-not-ban`: A real problem, but managed through review and policy, not a ban
- `ai-authored-community-contributions--p1`: Welcome with disclosure and accountability

Claims:
- `b-sR11-f004993-c1` · Voice: Carter Anderson (@cart, Bevy creator and Project Lead) · Source: https://bevy.org/news/bevys-sixth-birthday (`f004993`) · Date: 2026-08-10 · Locator: "AI Policy #" section
  - Quote: "solved many problems but created many others (including fostering toxic witch hunts, incentivizing lying to maintainers, enforcement was a hard / impossible task)"
  - Paraphrase: the strict "no-AI" policy adopted this year "solved many problems but created many others" (toxic witch hunts, incentivized lying to maintainers, unenforceable), so the community (led by @alice-i-cecile) is drafting a replacement
- `a-sa29-f013224-c4` · Voice: jdahlstrom · Source: https://users.rust-lang.org/t/an-ai-assistant-llm-for-rust-lang-org/107676 (`f013224`) · Date: 2024-03-04T12:46:37Z · Locator: forum posts 2024-03-02T18:18:23.273Z and 2024-03-04T12:46:37.433Z
  - Quote: "It has such an obvious style that I can't even imagine the amount of eye-rolling going on amongst teachers and TAs grading student work these days"
  - Paraphrase: identifies the original proposal's style as obviously LLM-written and, when the author defended the practice, says he'd be more impressed if the message hadn't read as ">90% written by ChatGPT" prompted toward a predetermined conclusion
- `a-sa29-f013224-c6` · Voice: steffahn · Source: https://users.rust-lang.org/t/an-ai-assistant-llm-for-rust-lang-org/107676 (`f013224`) · Date: 2024-03-04T13:26:21Z · Locator: forum post, 2024-03-04T13:26:21.593Z
  - Quote: "clearly marked AI-generated content is generally not going to bring you into much of any trouble"
  - Paraphrase: cites the forum's rules against machine-generated content, noting clearly marked AI content rarely causes trouble, while unmarked, low-effort AI spam is what the rule is meant to prevent
- `b-sR13-f009740-c1` · Voice: Jakub Beránek, on behalf of the Rust Project mentorship team · Source: https://blog.rust-lang.org/2026/04/30/gsoc-2026-selected-projects (`f009740`) · Date: 2026-04-30 · Locator: paragraph on the 96 submitted proposals
  - Quote: "we somewhat struggled with some AI-generated proposals ... but it stayed manageable"
  - Paraphrase: "Like many other GSoC organizations this year, we somewhat struggled with some AI-generated proposals and low-quality contributions generated using AI agents, but it stayed manageable."
- `b-sb20-f007942-c1` · Voice: Rust GameDev Working Group · Source: https://gamedev.rs/news/051 (`f007942`) · Date: 2024-06-05 · Locator: section "Survey Results #"
  - Quote: "Readers do not want anything in the newsletter generated by AI."
  - Paraphrase: after surveying 52 readers on how to improve the newsletter, the WG reports that readers are generally positive about it, are content with its frequency, but explicitly do not want anything in it generated by AI
- `b-sb15-f004721-c1` · Voice: alexcrichton · Source: https://github.com/bytecodealliance/wasmtime/pull/13459 (`f004721`) · Date: 2026-05-23 · Locator: PR #13459, comment 2026-05-23T15:42:24Z
  - Quote: "Notably this looks like a very large wall of text generated by an AI. Please ensure that you are yourself in the loop on all communication because you, after all, own this change and are responsible for it."
  - Paraphrase: tells the PR author to read the Bytecode Alliance's AI tool use policy, flags that the PR description reads as a large wall of AI-generated text, and stresses the author must stay personally in the loop on all communication because they own and are responsible for the change
- `a-sa29-f013224-c5` · Voice: jasn-armstrng · Source: https://users.rust-lang.org/t/an-ai-assistant-llm-for-rust-lang-org/107676 (`f013224`) · Date: 2024-03-04T13:47:53Z · Locator: forum post, 2024-03-04T13:47:53.039Z
  - Quote: "I gave it my points and it did the rest. Why would you assume that my thought process and prompt was that casual?"
  - Paraphrase: defends having used an LLM to write the original post, explaining that writing this kind of communication isn't a personal strength, that he supplied the points himself, and seeing no issue with that division of labor
- `b-bk03-f000267-c6` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Contributing § AI-Assisted Contributions
  - Quote: "What matters is the quality of the result and the contributor's understanding of it, not whether AI was involved."
  - Paraphrase: Zebra welcomes AI-assisted contributions; what matters is the quality of the result and the contributor's own understanding of it, not whether AI was involved, provided AI usage is disclosed in the PR description and the human contributor remains the sole responsible author, able to explain the logic and trade-offs of every change

## Question `ai-review-suggestions`

Should a Rust practitioner follow an AI code-review tool's suggestions by default, or evaluate them critically before acting?

Positions:
- `ai-review-suggestions--p1`: Critically evaluate not blindly follow
- `ai-review-suggestions--alt1`: Follow AI review suggestions by default

Claims:
- `b-sR08-f003550-c1` · Voice: laggui · Source: https://github.com/tracel-ai/burn/pull/3743 (`f003550`) · Date: 2025-09-19 · Locator: PR #3743, review comment 2025-09-19T19:54:02Z
  - Quote: "You didn't need to follow Copilot's advice here 😄 passing &3 is fine."
  - Paraphrase: dismisses a Copilot review comment telling the author to avoid `&3` as unnecessary noise (passing a reference to a literal is fine), and redirects attention to a real bug the AI reviewer missed — an unsupported vectorization size on some cubecl backends.

## Question `all-rust-vs-platform-native-tooling`

Where Rust meets a host platform (Android JNI, iOS AppDelegate and XCTest, browser E2E tests), write the glue and tests in Rust, or in the platform's language and tools?

Positions:
- `all-rust-vs-platform-native-tooling--all-rust`: Write it in Rust (the `jni` crate, `objc2`, `wasm-bindgen-test`)
- `all-rust-vs-platform-native-tooling--all-rust-workable-not-production`: All-Rust is workable but brittle, not production-ready (iOS XCTest)
- `all-rust-vs-platform-native-tooling--platform-native-glue`: Write the glue in the platform's language for its tooling (C++ JNI in Android Studio)

Claims:
- `b-sb20-f007678-c1` · Voice: Emily Dixon · Source: https://mux.com/blog/practical-client-side-rust-for-android-ios-and-web (`f007678`) · Date: 2023-12-13 · Locator: section "Rust for Android," subsection "The app"
  - Quote: "Many guides write the JNI and FFI layers in Rust, but I chose to write the JNI side in C++ instead."
  - Paraphrase: many guides write both the FFI (Rust↔C) and JNI (C↔JVM) layers in Rust, but doing the JNI side in C++ instead lets Android Studio's native-C++ project tooling (code generation, build automation, code analysis, jump-to-declaration) work across the boundary, at the cost of one extra language
- `b-sb22-f008914-c1` · Voice: Chayan Mistry · Source: https://chayanmistry.medium.com/rust-in-android-development-complete-guide-5f3313f40e50 (`f008914`) · Date: 2026-05-12 · Locator: section "Writing Rust Code," subsection "Basic Structure"
  - Quote: "JNI functions must follow this naming pattern: Java_<package>_<class>_<method>"
  - Paraphrase: the tutorial's whole worked example is `#[no_mangle] pub extern "C" fn Java_com_example_rustdemo_MainActivity_helloFromRust(...)` functions written in Rust, following the `Java_<package>_<class>_<method>` naming convention, built via `cargo-ndk`, with no C++ intermediary anywhere in the pipeline
- `b-sb13-f004367-c1` · Voice: Madoshakalaka · Source: https://github.com/yewstack/yew/pull/4046 (`f004367`) · Date: 2026-03-05 · Locator: PR description 2026-03-05T15:54:42Z
  - Quote: "This is a pure-Rust E2E testing approach that requires no non-Rust dependencies like Playwright, Cypress, or Selenium."
  - Paraphrase: builds SSR hydration E2E tests as a pure-Rust `wasm-bindgen-test` harness specifically so the project avoids adding non-Rust E2E dependencies like Playwright, Cypress or Selenium
- `a-sT12-f008455-c1` · Voice: rustunit · Source: https://rustunit.com/blog/2025/05-18-bevy-ios-deep-linking (`f008455`) · Date: 2025-05-18 · Locator: § "Receive app open options", paragraph 1; intro paragraphs 1–3
  - Quote: "Thanks to the objc2 crate we can use native objc APIs without having to write objc but pure rust instead."
  - Paraphrase: before winit 0.30.10, winit registered its own AppDelegate and Bevy iOS users had to drop winit to get lifecycle hooks. With the fix, rustunit uses `objc2` to call native Objective-C APIs from pure Rust and wraps that in the `bevy_ios_app_delegate` crate
- `b-sb21-f008793-c1` · Voice: Sebastian Imlay (simlay) · Source: https://simlay.net/posts/2026-01-rust-xctesting (`f008793`) · Date: 2026-02-04 · Locator: § "Closing thoughts"
  - Quote: "This is a pretty brittle setup and I'm not sure I suggest it in production."
  - Paraphrase: an all-Rust XCTest harness (bundling both the app and a `#![no_main]` XCTest bundle built from objc2 bindings) works and lets you drive UI automation and code coverage without ever opening Xcode, but exit-status detection is unreliable, on-device operation is unclear, and the whole setup is "brittle"; he still prefers the Makefile/CLI workflow over `xcodebuild` tooling day to day

## Question `api-handler-as-async-trait`

Should an HTTP API's handler signature be defined using an async trait decoupled from any concrete implementation, so tooling can extract API/schema information without compiling a real implementation?

Positions:
- `api-handler-as-async-trait--p1`: Define API endpoints via async traits decoupled from implementation
- `api-handler-as-async-trait--alt1`: Define handlers as concrete functions, not via an async trait

Claims:
- `a-sa14-f005454-c3` · Voice: sunshowers · Source: https://lobste.rs/s/pjtizh (`f005454`) · Date: 2025-02-24 · Locator: comment 2025-02-24T16:37:04
  - Quote: "I hope Rust projects more generally adopt this pattern, since it helps extract API information without needing to compile (or even have) a concrete implementation at hand."
  - Paraphrase: describes contributing async-trait-based API definitions to Dropshot shortly after async traits stabilized, noting the value is extracting API information without needing a concrete implementation compiled or even present

## Question `api-schema-spec-first-vs-code-first`

Should an HTTP API's OpenAPI schema be generated from the Rust server code, or should code be generated from a hand-written spec?

Positions:
- `api-schema-spec-first-vs-code-first--p1`: Generate the OpenAPI spec from code, not code from the spec
- `api-schema-spec-first-vs-code-first--p2`: Code-first schema generation

Claims:
- `a-sa23-f011186-c1` · Voice: Adam (surname unconfirmed; self-ID only) · Source: https://youtube.com/watch?v=bjgGboWCTDw (`f011186`) · Date: 2024-11-20 · Locator: ~00:10:56
  - Quote: "a better idea is don't hand write the spec don't rely on a programmer spec instead have your API server generate the spec"
  - Paraphrase: don't hand-write the OpenAPI spec or rely on a programmer-maintained one; have the API server generate it, since a generated spec is provably in sync with the server that produced it
- `a-sa14-f005454-c1` · Voice: wofo (quoting the Dropshot project's own stated design goal) · Source: https://lobste.rs/s/pjtizh (`f005454`) · Date: 2025-02-24 · Locator: comment 2025-02-24T08:08:32
  - Quote: "[An] important goal for us was to build something with strong OpenAPI support, and particularly where the code could be the source of truth and a spec could be generated from the code that thus could not diverge from the implementation."
  - Paraphrase: highlights a quote from the Dropshot project explaining that an important goal was for code to be the source of truth with the spec generated from it, specifically so the spec couldn't diverge from the implementation, noting no existing crate did this

## Question `async-by-default-host-interfaces`

Should a framework's host/runtime interfaces be async by default, or should async stay an opt-in path alongside a synchronous default?

Positions:
- `async-by-default-host-interfaces--p1`: Async by default
- `async-by-default-host-interfaces--alt1`: Keep a synchronous default with async as opt-in

Claims:
- `b-sR10-f004809-c1` · Voice: The Spin Project (Fermyon / CNCF Spin, institution) · Source: https://spinframework.dev/blog/announcing-spin-4-0 (`f004809`) · Date: 2026-06-15 · Locator: sections "WASI Preview 3: stabilized and supported long-term" / "Async everywhere: Spin's host interfaces are now async"
  - Quote: "WASIp3 is now the default platform for new applications... we've asyncified Spin's host interfaces so I/O-heavy handlers actually get concurrency instead of blocking the instance."
  - Paraphrase: WASIp3's async model, previously experimental and opt-in, is now the default for new applications, and Spin's own host interfaces (KV, SQLite, Postgres, Redis, outbound HTTP) were rewritten to be async so handlers get real concurrency instead of blocking

## Question `async-drop-raii-vs-close`

Without async `Drop`, should async resources keep RAII cleanup, or require an explicit async `close`?

Positions:
- `async-drop-raii-vs-close--preserve-raii-with-workarounds`: Keep RAII, working around the missing async Drop
- `async-drop-raii-vs-close--explicit-close-required`: Require an explicit async close; `Drop` is best effort only

Claims:
- `b-sR10-f004423-c1` · Voice: dignifiedquire (iroh/n0 computer) · Source: https://iroh.computer/blog/iroh-0-97-0-custom-transports-and-noq (`f004423`) · Date: 2026-03-16 · Locator: section "2. Changes to Endpoint closing" / "Endpoint Lifecycle Improvements"
  - Quote: "Starting with this release, the Endpoint no longer attempts to close connections gracefully when dropped. To gracefully close the endpoint, always await endpoint.close() before dropping the last instance of an endpoint or terminating your application."
  - Paraphrase: Endpoint no longer attempts best-effort graceful close on drop; callers must await endpoint.close() explicitly, or resources close ungracefully and an error is logged
- `b-sR10-f004741-c1` · Voice: Friedel Ziegelmayer & Rüdiger Klaehn (iroh/n0 computer) · Source: https://iroh.computer/blog/iroh-1-0-0-rc-1 (`f004741`) · Date: 2026-05-27 · Locator: section "⚡ Faster Endpoint::close"
  - Quote: "Shutdown now skips the draining period when it can. Closing is near-instant when the peer already closed remotely, and roughly one RTT otherwise if there is no packet loss."
  - Paraphrase: explicit endpoint.close() is now cheaper too — shutdown skips the draining period when possible, reinforcing close as the primary, first-class shutdown path rather than relying on drop
- `b-sb17-f005159-c2` · Voice: Rüdiger Klaehn · Source: https://iroh.computer/blog/async-rust-challenges-in-iroh (`f005159`) · Date: 2024-07-31 · Locator: article body, "Drop" section
  - Quote: "I refuse to give up on RAII. I might provide an async shutdown function that tries to do a gentle shutdown. But every entity should also attempt to clean up on Drop."
  - Paraphrase: refuses to abandon RAII for async resources; instead builds cleanup on cancel tokens or blocking-safe/force-send queues so `Drop` can still trigger a clean shutdown

## Question `async-fn-in-traits-cost`

Should you use `async fn` in traits (via the `async-trait` crate or async-fn-in-trait) given its cost?

Positions:
- `async-fn-in-traits-cost--p1`: Acceptable for most applications; avoid in hot low-level public APIs
- `async-fn-in-traits-cost--alt1`: Avoid async fn in traits because of its per-call cost

Claims:
- `b-bk01-f000233-c14` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "Workarounds to Know and Love" § async in Traits
  - Quote: "should be considered when deciding whether to use this functionality in the public API of a low-level function that is expected to be called millions of times a second."
  - Paraphrase: using async fn in traits (via the async-trait crate on stable, or async-fn-in-trait on nightly) costs a heap allocation per function call; calls this not a significant cost for the vast majority of applications, but says it should be weighed when deciding whether to expose the functionality in the public API of a low-level function expected to be called millions of times a second.

## Question `async-for-cpu-bound-work`

Is async Rust (e.g. Tokio) an appropriate choice for CPU-intensive work?

Positions:
- `async-for-cpu-bound-work--p1`: Qualified yes, against the "never use async for CPU work" meme
- `async-for-cpu-bound-work--alt1`: Never use async Rust for CPU-intensive work

Claims:
- `b-bk01-f000233-c6` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "IO and issues with blocking" § CPU-intensive work
  - Quote: "There is a meme that you should simply not use async Rust ... for CPU-intensive work, but that is an over-simplification."
  - Paraphrase: explicitly rejects the common claim that async Rust/Tokio should never be used for CPU-intensive work as an over-simplification; the real constraint is that mixing IO-bound/latency-sensitive tasks with CPU-bound/long-running tasks needs special handling, not avoidance of async altogether.

## Question `async-hook-cancellation-upfront`

When designing an async-computation hook API, should cancellation semantics be committed to upfront even at the cost of a larger initial API surface, or postponed until real usage demonstrates the need?

Positions:
- `async-hook-cancellation-upfront--p1`: Ship minimal now
- `async-hook-cancellation-upfront--alt1`: Commit to cancellation semantics up front

Claims:
- `a-02-f000957-c1` · Voice: Ekleog · Source: https://github.com/yewstack/yew/pull/3609 (`f000957`) · Date: 2024-02-20 · Locator: PR description
  - Quote: "Yew is not stable yet, and probably at least 90% of the use cases are covered by this API, so I think it makes sense to postpone the decision after verifying that there is an actual need."
  - Paraphrase: argues the initial `use_async` hook should ship without baking in cancellation semantics, since Yew isn't stable yet and the design likely covers ~90% of use cases; cancellation can be added later as a variant if real need emerges

## Question `async-io-with-sync-storage`

When your chosen async I/O library (e.g. quinn for QUIC) is paired with a storage/database layer that only offers a synchronous API (as with embedded databases like redb, rocksdb, sled, sqlite), should you treat that combination as an avoidable architecture mismatch to design around from the outset — including avoiding constructs like `LocalSet` and `!Send` futures — or accept it as a practical necessity, since no viable async-native alternative exists and non-`Send` futures are often unavoidable when wrapping such resources?

Positions:
- `async-io-with-sync-storage--p1`: Incompatible deps should be avoided
- `async-io-with-sync-storage--p2`: Sync storage is unavoidable given available options

Claims:
- `b-sb18-f005307-c1` · Voice: withoutboats · Source: https://lobste.rs/s/7rtvnp (`f005307`) · Date: 2024-08-02 · Locator: lobste.rs/s/7rtvnp, comment 2024-08-02T06:30:40-05:00
  - Quote: "I would have regarded quinn and redb as incompatible dependencies because of this mismatch and looked for a different solution."
  - Paraphrase: argues iroh's choice of quinn (async QUIC) together with redb (blocking storage) creates the impedance mismatch that is the source of many of their described problems, and separately that `LocalSet` and `FuturesUnordered` should generally be avoided
- `b-sb18-f005307-c2` · Voice: rklaehn · Source: https://lobste.rs/s/7rtvnp (`f005307`) · Date: 2024-08-06 · Locator: lobste.rs/s/7rtvnp, comment 2024-08-06T06:41:54-05:00
  - Quote: "What is the alternative? ... They *all* have a sync api."
  - Paraphrase: as the blog post's author and an iroh maintainer, responds "what is the alternative?" — every in-process database they evaluated (rocksdb, redb, sled, sqlite) has a synchronous API, so the mismatch isn't a foreseeable design error, and non-`Send` futures are often unavoidable when a future must capture a non-`Send` database/transaction handle

## Question `async-rust-production-ready`

Is async Rust production-ready today given its known gaps?

Positions:
- `async-rust-production-ready--p1`: Reliable despite rough edges
- `async-rust-production-ready--alt1`: Not production-ready because of its gaps

Claims:
- `b-sR01-f000233-c2` · Voice: Rust Async Book (async-book, rust-lang.github.io) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: undated (living document) · Locator: § "Development of Async Rust", paragraph 1
  - Quote: "Async Rust ... is reliable and performant. It is used in production in some of the most demanding situations at the largest tech companies."
  - Paraphrase: stable async is reliable and performant and used in production at large tech companies, though ergonomics (not reliability) are rough around async iterators/streams, async in traits, and async destruction.

## Question `async-transport-asyncread-vs-sink-stream`

For a custom async I/O transport abstraction in Rust that must work across several carriers (raw TCP, TLS, WebSocket-wrapped tunnel), should the abstraction be built against the tokio-style `AsyncRead`/`AsyncWrite` traits, or against the `Sink`/`Stream` traits that most existing async WebSocket libraries expose?

Positions:
- `async-transport-asyncread-vs-sink-stream--p1`: Build the transport abstraction against `AsyncRead`/`AsyncWrite`, not `Sink`/`Stream`
- `async-transport-asyncread-vs-sink-stream--alt1`: Build it against `Sink`/`Stream`

Claims:
- `a-sa03-f002236-c1` · Voice: Cloudflare (Hyperdrive team) · Source: https://blog.cloudflare.com/elephants-in-tunnels-how-hyperdrive-connects-to-databases-inside-your-vpc-networks (`f002236`) · Date: 2024-10-25 · Locator: article body, "The way we accomplish this..." section
  - Quote: "The primary reason is that Hyperdrive operates across multiple threads (thanks to the tokio runtime), and so we rely on our connections to also handle Send, Sync, and Unpin. None of the available solutions had all five traits handled."
  - Paraphrase: States that available OSS WebSocket-over-async libraries built on `Sink`/`Stream` did not jointly satisfy `Send`, `Sync`, `Unpin` together with `AsyncRead`/`AsyncWrite`, so Hyperdrive wrote its own translation layer to keep its entire custom Postgres handler generic over `AsyncRead`/`AsyncWrite` streams instead.

## Question `async-vs-threads`

Should a Rust program model concurrency with async/await tasks, or with OS threads (on embedded: hand-written run-to-completion or state-machine tasks)?

Positions:
- `async-vs-threads--async-for-io-wait-and-no-os`: Async where work waits on I/O or there is no OS
- `async-vs-threads--async-tasks-on-embedded`: Async tasks compiled to static executors beat manual task splitting on embedded
- `async-vs-threads--p1`: Async/await preferred for ergonomics over manual state-machine sub-tasking
- `async-vs-threads--p2`: Async for large numbers of (esp. IO-bound) tasks and constrained environments; plain threads otherwise

Claims:
- `a-sB01-f000227-c3` · Voice: RTIC developers · Source: https://rtic.rs/ (`f000227`) · Date: undated (living doc) · Locator: Preface, "RTIC into the Future"
  - Quote: "The answer is - improved ergonomics!"
  - Paraphrase: States that without async/await a programmer must manually split a task into sub-tasks and track state, whereas async/await builds the progression mechanism automatically at compile time via Futures
- `a-sR01-f000227-c2` · Voice: RTIC project (rtic.rs maintainers, unnamed individually) · Source: https://rtic.rs/ (`f000227`) · Date: unknown (living document, no publish/version date given) · Locator: § "RTIC into the Future"
  - Quote: "So with the technical stuff out of the way, what does async/await bring to the table? The answer is - improved ergonomics!"
  - Paraphrase: the maintainers argue async/await brings "improved ergonomics" over manual sub-task splitting, is compatible with SRP because the compiler forbids awaiting while holding a resource, and avoids dynamic allocation (which would panic on OOM) by using compile-time-generated static executors.
- `b-bk01-f000233-c11` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "Why Async?" § Async vs threads in Rust / § Async in Rust vs other languages
  - Quote: "asynchronous programming is not better than threads, but different."
  - Paraphrase: OS threads need no new programming model and let existing sync code run unchanged (and support OS-level thread-priority tuning for latency-sensitive work), but come with real CPU/memory overhead per thread; async gives orders-of-magnitude more concurrent tasks for the same overhead, especially for IO-bound workloads like servers and databases, and (being zero-cost, needing no heap allocation or dynamic dispatch) can run in constrained environments like embedded systems — at the cost of larger compiled binaries from generated state machines plus a bundled runtime. Explicitly frames this as "not better than threads, but different": use threads if you don't need async's performance benefits.
- `b-sR01-f000233-c1` · Voice: Rust Async Book (async-book, rust-lang.github.io) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: undated (living document; no revision date on page) · Locator: § "What is Async Programming and why would you do it?", paragraph 2
  - Quote: "This makes async programming a good fit for systems which need to handle very many concurrent tasks and where those tasks spend a lot of time waiting"
  - Paraphrase: async fits systems handling many concurrent tasks that spend most of their time waiting (e.g. client responses, IO), and also fits microcontrollers with very limited memory and no OS-provided threads.

## Question `aya-vs-libbpf-rs`

For writing eBPF programs from Rust, should you use a pure-Rust implementation with no libbpf/BCC dependency (Aya), or a Rust wrapper around the native C `libbpf` library with the eBPF program itself written in C (libbpf-rs)?

Positions:
- `aya-vs-libbpf-rs--p1`: No strong preference used libbpf rs for familiarity
- `aya-vs-libbpf-rs--alt1`: Pure-Rust eBPF with Aya
- `aya-vs-libbpf-rs--alt2`: C eBPF programs with libbpf-rs

Claims:
- `b-sb24-f011306-c2` · Voice: Lalit Basin · Source: https://youtube.com/watch?v=OWCj8mDbAXc (`f011306`) · Date: 2025-10-03 · Locator: [19:32]-[20:34]
  - Quote: "most of the examples which I'm going to talk here would be lib BPF using libf BPF RS for no specific reasons uh I know that there are I maintainers and developers probably sitting somewhere in the audience don't please don't judge me you guys are doing the awesome job"
  - Paraphrase: Aya is pure Rust for both the kernel-space and user-space program with only experimental CO-RE support and no libbpf/BCC/kernel-header dependency; libbpf-rs wraps the C libbpf library, so the eBPF program is written in C/compiled with clang+LLVM while the user-space program is Rust, with CO-RE supported by default; he used libbpf-rs for the talk's examples "for no specific reason"

## Question `batch-crypto-verification`

Should CPU-bound cryptographic verification in an async Rust service be batched for throughput?

Positions:
- `batch-crypto-verification--p1`: Batch verify for throughput
- `batch-crypto-verification--alt1`: Verify each request individually

Claims:
- `b-bk03-f000267-c5` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Design Overview § zebra-consensus; Parallel Verification RFC § Summary
  - Quote: "perform automatic, transparent batch processing of contemporaneous verification requests"
  - Paraphrase: zebra-consensus uses the tower-batch-control crate to automatically and transparently batch contemporaneous signature/proof verification requests, rather than verifying each request independently; the Parallel Verification RFC gives the reason directly — serial, one-block-at-a-time verification (as in zcashd) is too slow during initial sync, so Zebra defers data dependencies and batches signature/proof/script verification to parallelize it

## Question `batteries-included-web-framework`

Should a Rust backend use an opinionated batteries-included framework (Rails/Django/Spring-style), or compose libraries such as axum and sqlx directly?

Positions:
- `batteries-included-web-framework--batteries-included`: Use or build a convention-over-configuration, batteries-included framework
- `batteries-included-web-framework--alt1`: Compose minimal libraries (axum, sqlx) directly

Claims:
- `b-sb19-f005872-c1` · Voice: Nicole Tietz-Sokolskaya · Source: https://ntietz.com/blog/rust-needs-a-web-framework-for-lazy-developers (`f005872`) · Date: 2024-10-02 · Locator: § "Imagining the future I want"
  - Quote: "I'd much rather have a single web framework that handles it all, with clean upgrade instructions between versions."
  - Paraphrase: existing minimalist frameworks (actix-web, axum) and SPA frameworks (Yew, Leptos, Dioxus) each require substantial manual wiring (routing, templates, auth, DB, admin, etc.); the ecosystem needs one integrated toolkit instead, which she is starting to build ("newt")

## Question `become-tail-call-codegen`

Does Rust's nightly `become` tail-call feature produce reliably good codegen across targets, or is it currently good on some architectures and poor on others?

Positions:
- `become-tail-call-codegen--p1`: Strong win on arm64
- `become-tail-call-codegen--alt1`: Poor or inconsistent codegen on other targets (x86-64, Wasm)

Claims:
- `a-sa15-f005821-c1` · Voice: Matt Keeter · Source: https://mattkeeter.com/blog/2026-04-05-tailcall (`f005821`) · Date: 2026-04-05 · Locator: "Performance results" section, ARM64 and x86-64 benchmark tables plus WASM benchmark table
  - Quote: "the tail-call interpreter handily beats my hand-written assembly on both benchmarks" (ARM64); "oh no... it's outperforming the VM, but is still losing to the assembly backend" (x86-64)
  - Paraphrase: on ARM64 (M1) the tail-call interpreter beats both the plain VM and Keeter's own hand-written ARM64 assembly; on x86-64 it beats the VM but still loses to hand-written assembly; compiled to WASM it is 1.2–4.6x slower than the plain VM across Firefox, Chrome and wasmtime, which he attributes to the codegen (register spills to the stack) not translating well to the WASM stack machine

## Question `behavioral-equivalence-testing-method`

For verifying that a rewritten/ported system stays behaviorally equivalent to the original when correct behavior includes emergent, hard-to-specify effects (e.g. a physics-engine exploit), should you rely on unit/integration tests, naive property-based (fuzzing) testing, or a heuristic-guided reinforcement-learning search?

Positions:
- `behavioral-equivalence-testing-method--p1`: Unit and integration tests insufficient
- `behavioral-equivalence-testing-method--p2`: Naive property based testing insufficient
- `behavioral-equivalence-testing-method--p3`: Heuristic guided rl search preferred

Claims:
- `a-sa21-f011069-c1` · Voice: Aleksandr Petrosyan · Source: https://youtube.com/watch?v=LO7tvIed-YQ (`f011069`) · Date: 2023-11-15 · Locator: ~00:14:50-00:18:00 ("So, unit testing?... Wrong again.")
  - Quote: "The simple solution is usually right, right? Well, no."
  - Paraphrase: Rejects both unit tests and integration tests for verifying his DarkPlaces-to-Rust physics port preserves an emergent exploit (strafe-jumping): the divergence only shows up late in long play sessions, no fixed tolerance works everywhere, and a single integration test's result can't be extrapolated to the whole game.
- `a-sa21-f011069-c2` · Voice: Aleksandr Petrosyan · Source: https://youtube.com/watch?v=LO7tvIed-YQ (`f011069`) · Date: 2023-11-15 · Locator: ~00:18:50-00:20:30 (discussing Hypothesis and Rust's PropTest)
  - Quote: "checking all possible values and finding regressions is the right path, but the fuzziness, the way in which it was introduced in property-based testing is inherently random."
  - Paraphrase: Found property-based testing inadequate alone because the input space (keyboard holds, frame counts, continuous mouse movement) grows exponentially, and pure random search produces inputs "a human would not even be capable of producing," giving many false negatives against his goal of preserving a human-discoverable exploit; notes Rust has PropTest but he didn't use it.
- `a-sa21-f011069-c3` · Voice: Aleksandr Petrosyan · Source: https://youtube.com/watch?v=LO7tvIed-YQ (`f011069`) · Date: 2023-11-15 · Locator: ~00:20:30-00:23:00
  - Quote: "we want to have a Markov process, which should hint to you that we're talking about reinforcement learning at some point."
  - Paraphrase: Concludes the right approach is a heuristic-constrained ("tame," Markov-process) reinforcement-learning-style search biased toward human-plausible inputs, rather than fixed test cases or unconstrained fuzzing — treating "the exploit stays reachable within human-plausible effort" as the correctness criterion instead of exact input/output matching; implemented with the Rurel crate.

## Question `benchmark-colocation-with-crate`

When a function moves to a different crate in a multi-crate Rust workspace, should its benchmark move with it, using `git mv` to preserve file history?

Positions:
- `benchmark-colocation-with-crate--p1`: Colocate benchmark with owning crate
- `benchmark-colocation-with-crate--alt1`: Leave the benchmark where it is

Claims:
- `a-sR04-f001096-c2` · Voice: LaurentMazare · Source: https://github.com/huggingface/candle/pull/1819 (`f001096`) · Date: 2025-01-13 · Locator: comment "I think moving the benchmark to `candle-nn` would be good, (do it with `git mv` so as to preserve history)."
  - Quote: "I think moving the benchmark to `candle-nn` would be good, (do it with `git mv` so as to preserve history)."
  - Paraphrase: a benchmark should live in the crate that defines the function it measures; use `git mv` on relocation to preserve file history

## Question `bitflags-vs-generated-variants`

Should combinatorial pipeline state be represented as an explicit generated array/struct of bool-driven variants, or as bitflags with named constants?

Positions:
- `bitflags-vs-generated-variants--p1`: Bitflags preferred
- `bitflags-vs-generated-variants--p2`: Explicit array generation

Claims:
- `b-sb01-f000493-c1` · Voice: superdump · Source: https://github.com/bevyengine/bevy/pull/10156 (`f000493`) · Date: 2023-10-17 · Locator: PR #10156, 2nd comment
  - Quote: "Bit flags take a lot less space, and are arguably clearer when using named constants like the bitflag crate offers."
  - Paraphrase: the bool-per-combination approach used here "felt a bit off"; bit flags can generate combinations procedurally, take less space, and are arguably clearer with named constants (citing the bitflag crate)
- `b-sb01-f000493-c2` · Voice: coreh · Source: https://github.com/bevyengine/bevy/pull/10156 (`f000493`) · Date: 2023-10-17 · Locator: PR #10156, 3rd comment
  - Quote: "The amount of combinations here (32) makes this a little bit more daunting to fully enumerate like that (6) which is why I added the code to generate it in an array."
  - Paraphrase: the two approaches are mostly the same in principle, but with 32 combinations here versus 6 in the prior PR, enumerating by hand is more daunting, which is why the code generates the array instead

## Question `blocking-work-in-async`

How should CPU-bound or blocking work be integrated into an async program?

Positions:
- `blocking-work-in-async--p1`: Match mechanism to work shape
- `blocking-work-in-async--alt1`: Run blocking or CPU-bound work directly on the async runtime

Claims:
- `b-bk01-f000233-c7` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "IO and issues with blocking" § Other blocking operations
  - Quote: "If you're doing blocking IO, you should probably use spawn_blocking. ... If you have a thread that will run forever, you should use std::thread::spawn rather than use any kind of thread pool"
  - Paraphrase: gives a decision rule: use `spawn_blocking` for blocking IO; use `std::thread::spawn` (not a thread-pool slot) for a thread that will run forever; use a dedicated thread pool (e.g. Rayon) or a second async runtime for sustained CPU-bound work; accepts a dedicated thread or spawn_blocking as an easy-but-suboptimal choice when performance needs are modest.

## Question `borrowck-self-referential-structs`

Should Rust's borrow checker be extended to natively support safe self-referential structs, instead of requiring `unsafe`/`Pin`/crates like `ouroboros`?

Positions:
- `borrowck-self-referential-structs--p1`: Extend borrow checker
- `borrowck-self-referential-structs--alt1`: Keep requiring `unsafe`, `Pin` or crates like ouroboros

Claims:
- `b-sb19-f007207-c3` · Voice: Jimmy Hartzell · Source: https://thecodedmessage.com/posts/rust-features-2 (`f007207`) · Date: 2025-07-21 · Locator: § "Self-Referential Structs: Absolutely."
  - Quote: "Self-Referential Structs: Absolutely... I think it'll be the type of feature where we'll wonder how we ever lived without it."
  - Paraphrase: a subset of self-referential structs (borrowing only from a heap allocation owned by a sibling field, without mutating it) could be proven safe by a smarter borrow checker without needing `Pin`; he wants this more than fields-in-traits because he hits the need for it regularly

## Question `borrowed-build-state-vs-builder`

Should a struct under construction hold a lifetime-bound reference into shared mutable build state, or should construction use a builder consumed into an immutable owned structure?

Positions:
- `borrowed-build-state-vs-builder--p1`: Builder consume to immutable
- `borrowed-build-state-vs-builder--alt1`: Hold a lifetime-bound reference into shared build state

Claims:
- `a-sa07-f003704-c4` · Voice: laggui · Source: https://github.com/tracel-ai/burn/pull/3872 (`f003704`) · Date: 2025-11-03 · Locator: PR #3872, comment 2025-11-03T20:17:51Z
  - Quote: "The reliance on `_graph_data` here feels like a lifetime hack."
  - Paraphrase: calls the current reliance on `_graph_data` a lifetime hack and proposes a builder that consumes GraphState into an immutable OnnxGraph so Argument can reference the tensor store directly

## Question `bounded-grid-universe`

How should an in-principle infinite simulation grid be bounded in finite memory: a growing region, fixed edges, or a fixed periodic (toroidal) universe?

Positions:
- `bounded-grid-universe--p1`: Fixed periodic(chosen)
- `bounded-grid-universe--p2`: Fixed-size, periodic (toroidal) universe, over unbounded-growable or fixed-non-wrapping

Claims:
- `b-bk02-f000256-c1` · Voice: rustwasm working group (Rust and WebAssembly book) [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: unknown (living doc) · Locator: § "Implementing Conway's Game of Life" → Design → Infinite Universe
  - Quote: "We will implement the third option."
  - Paraphrase: names three ways to bound an infinite universe in finite memory — unbounded expansion (worst case: unbounded slowdown/OOM), fixed edges (kills patterns like gliders that reach the boundary), and fixed periodic wrap-around — and picks the third so patterns "can keep running forever."
- `a-sB02-f000256-c2` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "Implementing Conway's Game of Life" — "Design" — "Infinite Universe"
  - Quote: "We will implement the third option."
  - Paraphrase: of three ways to bound the infinite universe (expanding dirty-region tracking, fixed non-periodic, fixed periodic/wraparound), the tutorial picks periodic wraparound because unbounded expansion risks running out of memory and fixed non-periodic edges snuff out infinite patterns like gliders.
