## f005938 — Why building a Rust LSP is hard (2026-09-16, en)

### Questions
- Q: Should a Rust LSP maintain an incremental, memoized in-memory index (a salsa-style database), or eagerly index everything once and offload state to the filesystem?
  concepts: incremental computation, salsa, indexing strategy, LSP architecture; domains_live: desktop-cli-ui, core; positions_seen: eager-full-index-to-filesystem (Rust Glancer) vs. incremental-memoized-salsa (rust-analyzer, described)
- Q: Should an LSP eagerly discover and index workspaces the user did not explicitly open, or stay strict and require an explicit Cargo.toml in scope before indexing?
  concepts: workspace discovery, user intent inference, LSP activation; domains_live: desktop-cli-ui; positions_seen: strict-lazy-workspace-discovery (Rust Glancer) vs. eager-workspace-discovery (rust-analyzer, described)
- Q: Should each workspace an LSP serves run in its own OS process for crash isolation, or should all workspaces share one process?
  concepts: process isolation, memory fragmentation, LSP server architecture; domains_live: desktop-cli-ui, core; positions_seen: process-per-workspace-isolation (Rust Glancer) vs. single-shared-process (rust-analyzer, described)
- Q: Should symbol-under-cursor resolution rely on a precomputed full semantic analysis with span lookups, or on lazily matching syntax nodes to semantic elements?
  concepts: cursor resolution, lazy vs. eager analysis, refactoring support; domains_live: desktop-cli-ui; positions_seen: span-based-over-full-analysis (Rust Glancer) vs. syntax-node-matching-over-lazy-analysis (rust-analyzer, described)

### Claims
- voice: popzxc | connection: self-declared author/maintainer of Rust Glancer, "an experimental Rust LSP", building it "for quite a while now" | position: eager-full-index-to-filesystem | date: 2026-09-16 | locator: section "Server, at your service" | paraphrase: Rust Glancer eagerly indexes the whole workspace once and offloads the resulting state to the filesystem, prioritizing low RAM and instant editor restarts, instead of rust-analyzer's incremental, memoized salsa database that only computes what a query directly asks for. | quote: "Rust Glancer wants to eagerly do as much work as possible and tries to index everything once and then offload the state to the filesystem." | practiced_evidence: none | flag: voice-unverified
- voice: popzxc | connection: self-declared author/maintainer of Rust Glancer, "an experimental Rust LSP", building it "for quite a while now" | position: strict-lazy-workspace-discovery | date: 2026-09-16 | locator: section "One workspace, two workspace" | paraphrase: Rust Glancer requires a Cargo.toml to be in scope and will not start indexing a workspace until the user actually opens it, staying strict about not guessing the user's intent, whereas rust-analyzer is eager about workspace discovery and will go outside the project directory to be helpful. | quote: "it requires Cargo.toml to be in scope for analysis to run, and it will not start indexing workspace until you actually open it." | practiced_evidence: none | flag: voice-unverified
- voice: popzxc | connection: self-declared author/maintainer of Rust Glancer, "an experimental Rust LSP", building it "for quite a while now" | position: process-per-workspace-isolation | date: 2026-09-16 | locator: section "One workspace, two workspace" | paraphrase: Rust Glancer models each workspace as a separate OS process (engine) so a crash in one workspace never brings down the whole server and allocations from different workspaces don't share memory, unlike rust-analyzer's single-process model (a natural consequence of using salsa), even though this makes Rust Glancer's own architecture more convoluted and works against typical LSP design. | quote: "each workspace is modeled as a separate process (engine)... crash in any of the editors does not mean global crash." | practiced_evidence: none | flag: voice-unverified
- voice: popzxc | connection: self-declared author/maintainer of Rust Glancer, "an experimental Rust LSP", building it "for quite a while now" | position: span-based-over-full-analysis | date: 2026-09-16 | locator: section "Cursor: the god of LSP" | paraphrase: Rust Glancer resolves the symbol under the cursor by running full semantic analysis up front and then locating the most precise span, the opposite of rust-analyzer's approach of matching syntax nodes to semantic elements lazily, because rust-analyzer's own writeup says the span-based approach is too slow for an LSP that wants to do the least analysis possible and is less convenient for refactoring — tradeoffs Rust Glancer accepts since it already commits to full analysis. | quote: "Rust Glancer takes an almost opposite position here... it defaults to full analysis that is offloaded to the filesystem." | practiced_evidence: none | flag: voice-unverified

## f005943 — Bare-metal Rust in Android (2023-10-11, en)

UNREACHABLE — the fetched page is only the blog's chrome (labels list and year/month archive navigation); no article body about Rust in Android was captured, so the source could not be read.

## f006820 — the rust project has a burnout problem (2024-01-16, en)

### Questions
- Q: Should a Rust project's active contributors/maintainers treat their volunteer work as a bounded job with hard limits, or as an open-ended personal responsibility for the project's survival?
  concepts: maintainer burnout, project governance, contributor culture; domains_live: core; positions_seen: bounded-volunteer-responsibility-over-heroic-self-sacrifice (jyn)

### Claims
- voice: jyn | connection: self-reports living through "my own burnout from rust" as an active Rust project contributor, thanked by name-recognized rustc/rust-lang contributors (@Gankra, @ManishEarth, @estebank, and others) for feedback on the post | position: bounded-volunteer-responsibility-over-heroic-self-sacrifice | date: 2024-01-16 | locator: section "what can i do about it" | paraphrase: A burned-out Rust maintainer should treat their contribution as a bounded job — no overtime, no volunteering at every turn — rather than accept the belief that the project's survival depends on their own unpaid, unbounded effort. | quote: "if the project cannot survive without you personally putting in unpaid overtime, perhaps it does not deserve to survive." | practiced_evidence: none | flag: voice-unverified

## f007538 — Embedded Rust BSPs with uFerris & Xiao: LDR Support with ADC (2026-09-15, en)

### Questions
- Q: Should a board-support-package struct hold one field per component (a small type wrapping the several HAL objects a peripheral needs), or let each of the HAL's returned objects sit on the board struct as its own separate field?
  concepts: board support package design, embedded HAL composition, struct field modeling; domains_live: embedded; positions_seen: component-struct-per-peripheral-over-flat-fields (Omar Hiari)
- Q: Should a sensor-reading driver function return the raw sensor count and leave unit conversion to the caller, or perform the physical-unit conversion (lux, millivolts) inside the driver itself?
  concepts: driver API design, unit conversion, embedded sensor abstractions; domains_live: embedded; positions_seen: raw-sensor-count-over-driver-side-unit-conversion (Omar Hiari)

### Claims
- voice: Omar Hiari | connection: self-declared "Rustacean 🦀" embedded engineer, author of the µFerris & Xiao BSP series and its GitHub repo theembeddedrustacean/learn-bsp-rs | position: component-struct-per-peripheral-over-flat-fields | date: 2026-09-15 | locator: section "The Board Struct" | paraphrase: Wrap the several HAL objects a peripheral needs (e.g. an ADC driver plus its pin) in one small named component struct and give the board a single field for it, rather than letting each HAL object sit on the board struct as its own field, so the board struct stays a list of what the physical board has rather than a list of what the HAL API happened to hand back. | quote: "the struct stops being a list of what is on the board and becomes a list of what the HAL handed back." | practiced_evidence: https://github.com/theembeddedrustacean/learn-bsp-rs | flag: voice-unverified
- voice: Omar Hiari | connection: self-declared "Rustacean 🦀" embedded engineer, author of the µFerris & Xiao BSP series and its GitHub repo theembeddedrustacean/learn-bsp-rs | position: raw-sensor-count-over-driver-side-unit-conversion | date: 2026-09-15 | locator: section "The Board Control Functions" | paraphrase: A BSP's sensor-reading function should return the raw ADC count, not lux or millivolts, and leave unit conversion as an optional caller-side addition, rather than folding the conversion formulas into the driver. | quote: "the function returns a raw count, not lux or millivolts. This is the design decision of the post." | practiced_evidence: https://github.com/theembeddedrustacean/learn-bsp-rs | flag: voice-unverified

## f007990 — The Minimal Rust-Wasm Setup for 2024 (2024-06-17, en)

### Questions
- Q: When building with wasm-pack, should you use the non-default `--target web` build, or wasm-pack's default bundler/Node-oriented target?
  concepts: wasm-pack targets, tooling minimalism, JS bundler integration; domains_live: wasm, frontend; positions_seen: wasm-pack-target-web-over-bundler-default (dzfrias)

### Claims
- voice: dzfrias | connection: self-reported author who built and blogged this minimal Rust+Wasm setup, with a linked GitHub repository for feedback | position: wasm-pack-target-web-over-bundler-default | date: 2024-06-17 | locator: footnote 5 | paraphrase: Build with `wasm-pack build --target web` instead of wasm-pack's default bundler-oriented target, because skipping bundler/Node integration removes external tooling (no npm needed) and simplifies a minimal setup, even though that target is not the default. | quote: "It's not the default, but I think it simplifies things a lot and reduces the number of external tools (no npm!)" | practiced_evidence: none | flag: voice-unverified

## f008141 — Dyn Box Vs. Generics (2024-10-28, en)

### Questions
- Q: For a public library API that exposes a type over a trait, should the type parameter use generics or Box<dyn Trait>?
  concepts: static vs. dynamic dispatch, library API design, binary size and flexibility tradeoffs; domains_live: core; positions_seen: prefer-generics-over-box-dyn-for-library-apis (Christian Visintin)

### Claims
- voice: Christian Visintin | connection: self-reports "even I used Box dyn a lot in place of generics in my early days with Rust," writing from experience with both approaches | position: prefer-generics-over-box-dyn-for-library-apis | date: 2024-10-28 | locator: section "Conclusions" | paraphrase: For a public library API exposing a trait-typed field, prefer generics over Box<dyn Trait> even though Box dyn looks simpler for newcomers and can win on binary size in some cases, because generics give the common case of simple, non-wrapped user implementations better performance and more flexibility. | quote: "generics should be preferred instead." | practiced_evidence: none | flag: voice-unverified

## f008275 — The Embedded Rustacean Issue #37 (2025-01-22, en)

### Nothing new
reason-code: no-decision
reason: This is a bi-monthly link-aggregation newsletter curating embedded-Rust news, articles, jobs and events; it states no decision of its own, only pointers to other sources.

## f008325 — A Rustacean's Guide to Embedded World 2025 (2025-02-26, en)

### Nothing new
reason-code: no-decision
reason: The post is a directory of companies and booths showcasing Rust at a trade show, with marketing descriptions of each vendor's offering; it states no decision with a reason against a named alternative.

## f008686 — Neural Networks with Candle (2025-11-05, en)

### Nothing new
reason-code: no-decision
reason: This is a step-by-step Candle tutorial porting a PyTorch textbook example to Rust; its explanations (e.g. dropping an incomplete last batch, using 32-bit floats) are generic machine-learning practice rather than a decision specific to how Rust practitioners build things.

## f008879 — claudectl: stop tab-hunting your AI agents (2026-04-15, en)

### Questions
- Q: For a polling-based CLI/TUI tool whose I/O is fast local filesystem reads, should it pull in an async runtime (tokio/async-std), or stay synchronous?
  concepts: async vs. sync architecture, binary size, when async is justified; domains_live: desktop-cli-ui; positions_seen: sync-over-async-runtime-for-fast-local-io (mercurialsolo)
- Q: For reading process CPU/memory info, should a small Rust CLI shell out to `ps` and parse its output, or depend on a cross-platform crate like sysinfo?
  concepts: process introspection, dependency footprint, binary size; domains_live: desktop-cli-ui; positions_seen: shell-out-over-sysinfo-crate-for-binary-size (mercurialsolo)
- Q: For release binaries, should Cargo profiles use `lto = "thin"` or `lto = "fat"`?
  concepts: link-time optimization, binary size vs. compile time; domains_live: desktop-cli-ui, core; positions_seen: thin-lto-over-fat-lto (mercurialsolo)
- Q: Should a small monitoring/TUI binary build with `panic = "abort"`, or keep the default unwinding panic behavior?
  concepts: panic strategy, binary size, failure behavior for a TUI holding terminal state; domains_live: desktop-cli-ui; positions_seen: panic-abort-over-unwind-for-tui-safety (mercurialsolo)
- Q: For a small fixed-size rolling buffer (e.g. 3 samples), should code use the idiomatic VecDeque, or a plain Vec with remove(0)?
  concepts: idiomatic-vs-pragmatic data structure choice, micro-optimization vs. simplicity; domains_live: core; positions_seen: boring-vec-over-idiomatic-vecdeque-for-tiny-n (mercurialsolo)

### Claims
- voice: mercurialsolo | connection: self-declared author of claudectl, a published Rust crate ("cargo install claudectl", source at github.com/mercurialsolo/claudectl, linked in the post) | position: sync-over-async-runtime-for-fast-local-io | date: 2026-04-15 | locator: section "Why No Async Runtime" | paraphrase: claudectl stays fully synchronous and polls every 2 seconds instead of pulling in tokio or async-std, because its I/O (ps calls, local file seeks) is fast local work, not blocking network/database I/O, so an async runtime would only add 2-3MB of binary size, more compile time, and more complex control flow for no practical benefit. | quote: "Async is justified when you're waiting on I/O that would block the thread... When your I/O is local filesystem reads under 1ms, synchronous code is simpler and faster." | practiced_evidence: github.com/mercurialsolo/claudectl | flag: voice-unverified
- voice: mercurialsolo | connection: self-declared author of claudectl, a published Rust crate ("cargo install claudectl", source at github.com/mercurialsolo/claudectl, linked in the post) | position: shell-out-over-sysinfo-crate-for-binary-size | date: 2026-04-15 | locator: section "Keeping the Binary Under 1 MB" | paraphrase: claudectl shells out to `ps` and parses its stdout for CPU/memory/TTY/command-args instead of depending on the sysinfo crate, because sysinfo pulls in platform-specific FFI bindings and adds roughly 500KB, and the cost of one process spawn per 2-second tick is negligible by comparison. | quote: "The sysinfo crate is excellent but pulls in platform-specific FFI bindings and adds ~500KB." | practiced_evidence: github.com/mercurialsolo/claudectl | flag: voice-unverified
- voice: mercurialsolo | connection: self-declared author of claudectl, a published Rust crate ("cargo install claudectl", source at github.com/mercurialsolo/claudectl, linked in the post) | position: thin-lto-over-fat-lto | date: 2026-04-15 | locator: section "Keeping the Binary Under 1 MB" | paraphrase: claudectl's release profile uses `lto = "thin"` rather than `lto = "fat"`, because thin LTO recovers about 90% of fat LTO's binary-size reduction at a fraction of the link time, a difference of under 50KB for this project against a noticeably shorter compile. | quote: "thin LTO gets ~90% of fat LTO's size reduction at a fraction of the link time." | practiced_evidence: github.com/mercurialsolo/claudectl | flag: voice-unverified
- voice: mercurialsolo | connection: self-declared author of claudectl, a published Rust crate ("cargo install claudectl", source at github.com/mercurialsolo/claudectl, linked in the post) | position: panic-abort-over-unwind-for-tui-safety | date: 2026-04-15 | locator: section "Keeping the Binary Under 1 MB" | paraphrase: claudectl's release profile sets `panic = "abort"` to drop the unwinding machinery, saving 100-200KB and making failure predictable — a panic kills the process immediately rather than risk a half-crashed TUI left holding a corrupted terminal state. | quote: "a panic kills the process immediately, which is the right behavior for a monitoring tool." | practiced_evidence: github.com/mercurialsolo/claudectl | flag: voice-unverified
- voice: mercurialsolo | connection: self-declared author of claudectl, a published Rust crate ("cargo install claudectl", source at github.com/mercurialsolo/claudectl, linked in the post) | position: boring-vec-over-idiomatic-vecdeque-for-tiny-n | date: 2026-04-15 | locator: section "Multi-Signal Status Inference: The Hard Problem" | paraphrase: For a 3-sample rolling CPU average, claudectl uses a plain Vec with remove(0) instead of the more idiomatic VecDeque, because at that tiny size the extra allocation overhead of switching data structures doesn't matter and the simpler type wins. | quote: "A VecDeque would be more idiomatic here, but Vec with remove(0) on 3 elements is fast enough that the allocation overhead of switching doesn't matter. Boring code wins." | practiced_evidence: github.com/mercurialsolo/claudectl | flag: voice-unverified
