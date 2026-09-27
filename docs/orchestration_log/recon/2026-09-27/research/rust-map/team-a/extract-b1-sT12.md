For each source: where do competent Rust practitioners disagree?

## f008237 — A Complete Guide to WASIp2 for Rust and Python Programmers (2025-01-01 first listed; read version 0.3.0 dated 2026-09-22, en)

### Questions
- Q: For cross-language interop, should Rust code expose and consume WASI Preview 2 components (WIT interfaces, composition) or C-ABI FFI?
  concepts: WebAssembly component model; WIT; wit-bindgen; C ABI; FFI; composition; domains_live: wasm; core; positions_seen: component model over C ABI; C-ABI FFI (named as the incumbent, no Voice for it here)
- Q: Should Rust's standard library on `wasm32-wasip2` import only the WASI interfaces a program uses, rather than the whole `wasi:cli` world whenever a simple std facility such as `format!` is used?
  concepts: std; wasm32-wasip2; WASI imports; component size; domains_live: wasm; positions_seen: minimal imports (author, via a filed issue); current std behavior (no Voice defends it here)

### Claims
- voice: author of Ideas Reifying (ideas.reify.ing; not named in the text) | position: component model over C ABI | date: 2026-09-22 | locator: § "Compose with wasmbuilder.app", last paragraph; § "Personal Notes and Beyond WASIp2", paragraph 1 | paraphrase: composing components through compatible WIT interfaces relieves the pain of gluing programs through C ABIs, which the author calls fragile and dangerous as a foundation for interop | quote: "The foundation of software interops is still legacy C ABIs, which are not only fragile but also dangerous." | practiced_evidence: wasi_mindmap repository (named in the text; URL not in text) | flag: voice-unverified (Rust connection in source: calls Rust a favorite, writes Rust guests and hosts, filed an issue in the Rust repository)
- voice: author of Ideas Reifying (ideas.reify.ing) | position: minimal imports | date: 2026-09-22 | locator: § "Standard Libraries", last paragraph; § "Issues and Contribute", unresolved list | paraphrase: using a simple std facility makes the compiled component import the whole `wasi:cli` world, including useless interfaces such as `wasi:cli/env`; the author filed this as an issue that is still open | quote: "the Rust compiler will include the whole wasi:cli world that includes some interfaces that are useless in this case" | practiced_evidence: none | flag: voice-unverified

## f008381 — The Embedded Rustacean Issue #42 (2025-03-28, en)

### Nothing new
nothing new — a curated link list (news, tutorials, crate updates, events, jobs). The only editorial stance is a general belief in Rust as "the future of software in embedded systems", with no decision, reason or rejected alternative (rule 8).

## f008455 — iOS Deep-Linking with Bevy (2025-05-18, en)

### Questions
- Q: For iOS platform hooks such as AppDelegate calls in a Rust app, should the Rust side call Apple's Objective-C APIs directly through Rust bindings (`objc2`), or write native Objective-C/Swift glue? And should a windowing crate (winit) own the AppDelegate?
  concepts: objc2; AppDelegate; winit; Bevy; Swift/Objective-C interop; domains_live: swift-interop; desktop-cli-ui; positions_seen: pure-Rust bindings via objc2; native objc/Swift glue; roll your own instead of winit (the pre-0.30.10 only option)

### Claims
- voice: rustunit | position: pure-Rust bindings via objc2 | date: 2025-05-18 | locator: § "Receive app open options", paragraph 1; intro paragraphs 1–3 | paraphrase: before winit 0.30.10, winit registered its own AppDelegate and Bevy iOS users had to drop winit to get lifecycle hooks. With the fix, rustunit uses `objc2` to call native Objective-C APIs from pure Rust and wraps that in the `bevy_ios_app_delegate` crate | quote: "Thanks to the objc2 crate we can use native objc APIs without having to write objc but pure rust instead." | practiced_evidence: bevy_ios_app_delegate crate (named in the text; URL not in text) | flag: voice-unverified (Rust connection in source: publishes Bevy/Rust crates and offers Rust consulting)

## f008566 — The Embedded Rustacean Issue #52 (2025-08-20, en)

### Nothing new
nothing new — a curated link list; no Voice declares a decision in the text itself.

## f008777 — The Embedded Rustacean Issue #63 (2026-01-21, en)

### Nothing new
nothing new — a curated link list. Linked titles such as "Rust's Downfall: From Rising Star to Rejected by Major Projects" are pointers to other pages, which Tier 2 does not follow.

## f008940 — Scientific Computing in Rust Monthly #18 (2026-05-27, en)

### Nothing new
nothing new — the newsletter describes crates in third-party summaries, which directive rule 1 treats as hypotheses, not declarations. It says numra is "native Rust with no FFI to C or FORTRAN" and delaunay is "Written in safe Rust with no unsafe code". Neither is a Claim, because neither is in the crate authors' own words; candidate Questions for a later pass are pure-Rust numerics versus BLAS/LAPACK FFI, and forbidding unsafe in libraries.

## f009074 — The Embedded Rustacean Issue #79 (2026-09-02, en)

### Nothing new
nothing new — a curated link list and community program notice; no decision is declared in the text.

## f009090 — Can You Use ESP32 as SWD Programmer for STM32 with Rust? (2026-09-06, updated 2026-09-16, en)

### Nothing new
nothing new — a step-by-step tutorial that bit-bangs SWD with esp-hal. Choosing the ESP32 over a second STM32 is about hardware at hand, and no Rust decision is stated against an alternative (rule 8).

## f009632 — Next Steps on the Rust Trademark Policy (2024-11-06, en)

### Questions
- Q: How should the Rust trademark policy govern use of the Rust name and marks? Should it follow the Rust Foundation's 2023 draft, which drew widespread community concern, or a revised policy shaped by that feedback?
  concepts: trademark policy; Rust Foundation; Leadership Council; community governance; domains_live: core; positions_seen: revised 2024 draft (Leadership Council); 2023 initial draft (Foundation, superseded); community concerns (no named Voice)

### Claims
- voice: Rust Leadership Council | position: revised 2024 draft | date: 2024-11-06 | locator: paragraphs 1–3 | paraphrase: after community concern about the 2023 draft, the Council, Project Directors and Foundation revised the policy. The Council calls the new draft legally sound and able to protect the language's integrity, says it addresses the prevailing concerns, and opens it for final feedback until 2024-11-20 | quote: "The Leadership Council is confident that this updated version of the policy has addressed the prevailing concerns about the initial draft" | practiced_evidence: none | flag: voice-unverified (Rust connection in source: Rust project governance body, Rust Blog)

## f009704 — Demoting x86_64-apple-darwin to Tier 2 with host tools (2025-08-19, en)

### Questions
- Q: When free CI for a platform disappears, should the Rust project keep the target at Tier 1 by other means, or demote it (here x86_64-apple-darwin to Tier 2 with host tools) and accept less testing?
  concepts: target tier policy; CI; macOS x86_64; GitHub runners; rustup distribution; domains_live: core; desktop-cli-ui; positions_seen: demote to Tier 2 with host tools; keep Tier 1 (the alternative the tier policy rules out without CI tests)

### Claims
- voice: Jake Goulding, for the Rust Infrastructure team | position: demote to Tier 2 with host tools | date: 2025-08-19 | locator: § "Background", § "What changes?", § "Future" | paraphrase: Apple is ending x86_64 support, and GitHub is ending free macOS x86_64 runners for public repositories. The tier policy requires Tier 1 targets to run CI tests, so from 1.90.0 the target becomes Tier 2 with host tools; builds are still distributed, but the target will likely accumulate bugs faster and may be demoted further if it causes problems | quote: "Since the target tier policy requires that Tier 1 platforms must run tests in CI, the x86_64-apple-darwin target must be demoted to Tier 2." | practiced_evidence: none | flag: voice-unverified (Rust connection in source: writes for the Rust Infrastructure team on the Rust Blog)

## f011484 — rust-lang/rfcs label: final-comment-period (2023-09-27, en)

### Nothing new
unreachable — the cached text is the rust-lang/rfcs README, not the `final-comment-period` label listing at the URL. The listing is a time-varying set of PR titles whose 2023-09-27 state cannot be recovered, and it is not reconstructed from the README or from memory.

## f011614 — The Tianyi-33 Satellite Equipped with RROS Successfully Entered Orbit (2023-12-09, en)

### Nothing new
nothing new — a launch announcement stating that the Rust-based dual-kernel RTOS RROS flies on Tianyi-33; no decision is argued with a reason or against an alternative.
