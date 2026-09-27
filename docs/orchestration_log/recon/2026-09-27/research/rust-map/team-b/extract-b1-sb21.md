## f008390 — A 2025 Survey of Rust GUI Libraries (2025-04-16, en)

### Questions
- Q: For a Rust desktop app that needs a web-capable UI, should the frontend logic stay in the same Rust execution context as the backend (Dioxus-style, calling straight into the WebView glue), or should it run as an independent frontend runtime talking to a host process over a serialized IPC boundary (Tauri's architecture)?
  concepts: Diet Electron, WebView2/WebKitGTK, wasm-bindgen IPC, split-brain architecture, compile-time type safety; domains_live: desktop-cli-ui;frontend; positions_seen: reject-split-brain-untyped-ipc (boringcactus / Melody), single-execution-context-preferred (boringcactus / Melody, re: Dioxus)
- Q: Should a Rust GUI framework define UI structure through a bespoke DSL with dedicated tooling (Slint's own language, Makepad's `live_design!` macro), or should it stick to plain Rust code with no macros/DSL (egui's immediate-mode API)?
  concepts: DSL-driven UI, macro-driven UI, immediate mode API; domains_live: desktop-cli-ui; positions_seen: value-depends-on-priorities (boringcactus / Melody: tooling-and-error-messages favor a DSL like Slint; avoiding DSLs/macros entirely favors egui)
- Q: For typical small-to-medium desktop UIs, does the immediate-mode vs. retained-mode GUI architecture choice actually matter, or is it a difference that only shows up at larger scale?
  concepts: immediate mode, retained mode, widget lifetime, GPU/game-engine integration; domains_live: desktop-cli-ui; positions_seen: doesnt-matter-at-small-scale (boringcactus / Melody)
- Q: When choosing or building a Rust GUI framework, should Windows support and screen-reader/IME accessibility be treated as a first-class, load-bearing requirement rather than an afterthought?
  concepts: screen reader accessibility (Windows Narrator), IME input, cross-platform parity; domains_live: desktop-cli-ui; positions_seen: first-class-requirement (boringcactus / Melody)

### Claims
- voice: boringcactus (Melody) | position: reject-split-brain-untyped-ipc | date: 2025-04-16 | locator: § "Tauri" | paraphrase: Tauri's host-process/WebView split forces an IPC boundary where frontend calls take an untyped `&str` command name and `JsValue` args, so a field rename on the host side fails only at runtime instead of compile time; combined with the architectural split this made the author "genuinely hate" the design | quote: "Half the point of Rust is the sheer quantity of bugs that it can catch at compile time, and if your IPC is just tossing strings around and praying at runtime, you may as well be just writing vanilla JavaScript." | practiced_evidence: none (own trial project, not a maintained crate)
- voice: boringcactus (Melody) | position: value-depends-on-priorities | date: 2025-04-16 | locator: § "Conclusion" | paraphrase: recommends egui to readers who want zero DSL/macros and plain Rust, and Slint to readers who want a DSL with serious dev-tooling investment (better error-message ceiling since it's a standalone language, not just macros); does not pick an overall winner between the two approaches | quote: "If you want to avoid DSLs and macros and write only regular Rust, egui offers that... If you like DSL-driven UIs that are putting serious effort into developer tooling, Slint might be for you." | practiced_evidence: none
- voice: boringcactus (Melody) | position: doesnt-matter-at-small-scale | date: 2025-04-16 | locator: § "Digression: 'Immediate mode' and 'retained mode'" | paraphrase: immediate mode avoids widget-lifetime bookkeeping and is easier to integrate into a game engine's GPU loop; retained mode can perform better by not rebuilding the whole UI every frame, but at the scale of the task in this post ("Hello, world!" label + input) the difference is untestable | quote: "I'm not sure I love immediate mode on principle, although at this scale it extremely doesn't matter." | practiced_evidence: none
- voice: boringcactus (Melody) | position: first-class-requirement | date: 2025-04-16 | locator: § intro (context-setting) / § "digression: the irony you may have noticed" | paraphrase: most of the 43 surveyed libraries fail Windows support, screen-reader accessibility, or IME input (or all three); the author treats these as core seriousness criteria for evaluating a GUI framework, not nice-to-haves | quote: "if Windows support is lower on your roadmap than trend chasing AI bullshit, you are not serious." | practiced_evidence: https://github.com (per-library survey results in "The Table" section of the post itself)

### Nothing new
(none — this source was the richest in the batch)

---

## f008396 — Async from scratch 2: Wake me maybe (2025-04-16, en)

### Questions
- Q: For a hand-built async I/O reactor on Linux, should you build the readiness-notification layer on `epoll` (mature, stable) or on `io_uring` (newer, potentially faster but more experimental)?
  concepts: epoll, io_uring, Waker, reactor thread, readiness-based I/O; domains_live: core; positions_seen: epoll-for-now-as-the-standard-tradeoff (Natalie Klestrup Röijezon / natkr)

### Claims
- voice: Natalie Klestrup Röijezon (natkr) | position: epoll-for-now-as-the-standard-tradeoff | date: 2025-04-16 | locator: footnote 9 (§ "Sleepy I/O") | paraphrase: chooses epoll for the tutorial's reactor because it hits the "standard" balance of being neither too slow nor too experimental, while noting io_uring might take over that role "in a few years" | quote: "Not the only API, there are others. But it's the one that hits the 'standard' tradeoff between not being too slow or too experimental." | practiced_evidence: none (tutorial code, not a maintained crate)

### Nothing new
(none)

---

## f008583 — How to set up Rust logging in AWS Lambda for AWS CloudWatch (2025-09-03, en)

### Questions
- Q: When you need full error context in structured logs (e.g. the alternate `{:#}` display), does declaring error types with `thiserror` alone suffice, or do you need to wrap them in `anyhow`/`eyre` to get that context out?
  concepts: thiserror, anyhow, eyre, alternate Display format, error-context propagation; domains_live: cloud-workers;core; positions_seen: thiserror-insufficient-wrap-in-anyhow-or-eyre (Tomas Tauber)

### Claims
- voice: Tomas Tauber | position: thiserror-insufficient-wrap-in-anyhow-or-eyre | date: 2025-09-03 | locator: § "Error logging" | paraphrase: `thiserror` currently only supports the default `{}` Display format and loses error context (e.g. AWS SDK's `Unhandled` variant losing the underlying resource info); wrapping errors in `anyhow` or `eyre` recovers the alternate `{:#}` display that carries full context | quote: "The thiserror crate currently only supports the default {} display format, which loses the error context. One workaround for this is to wrap the errors in anyhow or eyre that support the alternate display format." | practiced_evidence: none (recommendation, not tied to a specific maintained repo)

### Nothing new
(none)

---

## f008692 — The Embedded Rustacean Issue #58 (2025-11-12, en)

### Nothing new
`nothing new`: this is a curated link-roundup newsletter (news, jobs, event listings, "noteworthy mentions"); it states no position of its own and raises no Question — per the opinion map's own finding, curated lists are Sources for Conventions/practice evidence, not sources of disagreement.

---

## f008793 — Writing iOS XCTests in Rust (2026-02-04, en)

### Questions
- Q: For iOS UI testing, should a Rust practitioner write the test harness directly in Rust via `objc2`/`objc2-xc-test`/`objc2-xc-ui-automation` bindings (bypassing the standard Xcode-project/Swift XCTest workflow entirely), or stay on the standard Swift-based XCTest setup?
  concepts: objc2, XCTest, XCUIAutomation, XCTRunner bundling, code coverage via LLVM profiling; domains_live: swift-interop; positions_seen: workable-but-not-production-ready (Sebastian Imlay / simlay)

### Claims
- voice: Sebastian Imlay (simlay) | position: workable-but-not-production-ready | date: 2026-02-04 | locator: § "Closing thoughts" | paraphrase: an all-Rust XCTest harness (bundling both the app and a `#![no_main]` XCTest bundle built from objc2 bindings) works and lets you drive UI automation and code coverage without ever opening Xcode, but exit-status detection is unreliable, on-device operation is unclear, and the whole setup is "brittle"; he still prefers the Makefile/CLI workflow over `xcodebuild` tooling day to day | quote: "This is a pretty brittle setup and I'm not sure I suggest it in production." | practiced_evidence: https://github.com (code subdirectory of the post's own repo, URL not given verbatim in text)

### Nothing new
(none)

---

## f008801 — Visualizing persistent vectors with Rust and WebAssembly (2026-02-18, en)

### Nothing new
`nothing new`: a technical explainer and tool announcement (pvec-rs, an RRB-tree persistent vector compiled to WASM for visualization); it references Niko Matsakis's observation that Rust collections have an expensive clone but does not quote him directly or argue against a competing Position — no contested claim is stated by the Voice.

---

## f008808 — Async/await on the GPU (2026-02-18, en)

### Questions
- Q: For structured concurrent GPU programming, is it better to reuse an existing general-purpose language's async/await abstraction (Rust's `Future`/async-await) than to adopt a purpose-built DSL/compiler stack (JAX, Triton, NVIDIA CUDA Tile)?
  concepts: Future trait, structured concurrency, warp specialization, CUDA Tile, function-coloring problem; domains_live: ml; positions_seen: reuse-existing-async-model-over-new-dsl (VectorWare)

### Claims
- voice: VectorWare | position: reuse-existing-async-model-over-new-dsl | date: 2026-02-18 | locator: § "Rust's Future trait and async/await" | paraphrase: JAX, Triton and CUDA Tile each require a new Python-based DSL/compiler and a break from existing CPU code/libraries; Rust's Future trait already encodes structured, composable concurrency without committing to an execution model, so it can be run unchanged on the GPU and reuse the existing async ecosystem (they ported the `Embassy` embedded executor with very few changes) — while acknowledging it still carries the same function-coloring problem async/await has on the CPU | quote: "We believe Rust's Future trait and async/await provide such an abstraction. They encode structured concurrency directly in an existing language without committing to a specific execution model." | practiced_evidence: none named (internal compiler/runtime work, not yet a published crate)

### Nothing new
(none)
