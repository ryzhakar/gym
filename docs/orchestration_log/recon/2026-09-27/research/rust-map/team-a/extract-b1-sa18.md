Checked prior batch (b1-sa15) Questions for recurrence before writing new ones: none of this batch's disagreements restate one already logged there, so no wording was reused.

## f008389 — Replicating state changes across language barriers with Rust, UniFFI, and proc macros (2025-03-27, en)

### Questions
- Q: When a Rust core pushes state changes across an FFI boundary to a declarative native UI (e.g. SwiftUI), should the boundary API return full/partial state snapshots for the UI to diff, or should the Rust side track and emit only the changed fields itself?
  concepts: FFI, UniFFI, proc-macros, state-diffing, declarative-UI; domains_live: swift-interop; positions_seen: rust-side-tracks-and-emits-diffs, ui-diffs-full-snapshot-itself

### Claims
- voice: TantalusPath (Serendipity Systems LLC) | position: rust-side-tracks-and-emits-diffs | date: 2025-03-27 | locator: "How procedural macros made it better" section | paraphrase: after iterating through three worse designs (manual return-value wiring, one-function-per-field event handlers, an all-optional `StateUpdateModel` requiring manual `Some`-checking on the Swift side), settled on a derive proc macro that generates a companion struct plus a diff enum, so the Rust side tracks uncommitted field changes and the Swift side gets a `[FieldValue]` diff it applies via an exhaustive `switch`, which the Swift compiler will fail to build if a new field isn't handled | quote: "If a state field is added or removed on the Rust side, this Swift function will fail compilers' enum exhaustiveness checks until it is added." | practiced_evidence: TantalusPath app (shipped); reports the more efficient unidirectional-only version of the same macro is already used in their other app, ChessTiles

---

## f008455 — iOS Deep-Linking with Bevy (2025-05-18, en)

### Nothing new
`nothing new`: a solo how-to (rustunit) showing that winit 0.30.10 plus the `objc2` crate now lets Bevy iOS apps hook `AppDelegate` in pure Rust, replacing the previous options of forking winit or doing without deep-link support. No contesting Voice or argued Position beyond "this is now possible and easier."

---

## f008566 — The Embedded Rustacean Issue #52 (2025-08-15, en)

### Nothing new
`nothing new`: a newsletter link roundup (headlines and one-line teasers only, full articles not included in this source). The one quoted aphorism ("Clean code always looks like it was written by someone who cares," Robert C. Martin) is not a Rust-specific declaration by a Voice with a Rust track record.

---

## f008583 — How to set up Rust logging in AWS Lambda for AWS CloudWatch (2025-09-02, en)

### Questions
- Q: When logging or wrapping errors in Rust, does `thiserror`'s default `{}` `Display` (which drops the source-error chain) create a real diagnostic gap that needs a workaround (`anyhow`/`eyre`, or the alternate `{:#}` format), or is this a non-issue in practice?
  concepts: error-handling, thiserror, anyhow, eyre, tracing, structured-logging; domains_live: cloud-workers, core; positions_seen: alternate-display-plus-anyhow-eyre-needed-for-full-context

### Claims
- voice: Tomas Tauber | position: alternate-display-plus-anyhow-eyre-needed-for-full-context | date: 2025-09-02 | locator: "Error logging" section | paraphrase: recommends logging errors with the alternate `{:#}` display because it preserves the full source-error chain (e.g. AWS SDK's `Unhandled` variants), and flags that `thiserror` currently only supports the default `{}` format, losing that context, so the workaround is to wrap errors in `anyhow` or `eyre` which support the alternate display | quote: "The thiserror crate currently only supports the default {} display format, which loses the error context. One workaround for this is to wrap the errors in anyhow or eyre that support the alternate display format." | practiced_evidence: none (recommendation, not tied to a named shipped project in this source)

---

## f008651 — Axum: Multi-tenancy (with Hexarch) and Abstracting the Repository Layer (2025-10-19, en)

### Questions
- Q: In a layered Rust service architecture, does splitting the repository layer into per-tenant/per-domain sub-crates (a crate boundary as an added abstraction layer) pay for itself in encapsulation and reuse, or is it unneeded indirection?
  concepts: repository-pattern, hexagonal-architecture, sqlx, workspace-crate-boundaries, encapsulation; domains_live: web, core; positions_seen: crate-boundary-abstraction-pays-for-itself

### Claims
- voice: Michael de Silva | position: crate-boundary-abstraction-pays-for-itself | date: 2025-10-19 | locator: "Another 'abstraction' to the repository layer" section | paraphrase: splits Postgres access into per-domain sub-crates (e.g. `accounts`, `payments`) behind an `interfaces` crate, arguing this keeps sub-crate public APIs stable (they only deal in primitive types) while the repository-facing types can change freely, and lets the Postgres stack be shared with another engineer decoupled from the host Axum app; explicitly flags this against a critique ("daymare was just commenting on the need for constant abstractions") without fully rebutting it, and closes by asking readers whether this is extreme | quote: "the sub-crates only care about primitive types... types used by the repository interface can change (as much as they need to), without impacting the sub-crate API." | practiced_evidence: his own workspace layout (shown), not yet extended to full Axum handler examples

---

## f008694 — [Talk] Improving the Incremental System in the Rust Compiler (2025-11-04, en)

### Questions
- Q: Should the Rust compiler's/Cargo's incremental-rebuild invalidation be redesigned around explicit "atomic level" targets (AST/HIR/MIR/codegen) plus separately-tracked data dependencies (e.g. codegen flags), instead of today's coarser per-flag/per-command invalidation?
  concepts: incremental-compilation, query-system, dependency-graph, cargo-check-vs-build, compile-times; domains_live: core; positions_seen: redesign-around-atomic-levels-and-data-dependencies

### Claims
- voice: Alejandra González | position: redesign-around-atomic-levels-and-data-dependencies | date: 2025-11-04 | locator: talk script, "atomic levels and data dependencies" section onward | paraphrase: a Clippy-team performance contributor pitches representing what stage a compilation needs (AST/HIR/MIR/codegen) as an explicit "atomic level" tag, plus tracking fine-grained "data dependencies" (e.g. link-time-optimization flags) separately, so `cargo check`/`clippy`/`build` stop redoing each other's work from scratch, and describes a further "two-stage fingerprint" (rebuild only to name-resolution to check if a dependent actually used a changed definition) to cut needless dependent rebuilds | quote: "So LTO options wouldn't impact clippy, for example." | practiced_evidence: none stated as merged/shipped in this source (presented as a conceptual redesign/talk, not a landed feature)

---

## f008787 — Building a 24MB Offline AI with Rust + Burn (2026-01-24, en)

### Questions
- Q: For offline/edge ML inference (no cloud connectivity, consumer hardware), is a Rust-based stack (Burn) a viable or superior alternative to the default Python/PyTorch stack, despite Python's ecosystem dominance for training?
  concepts: burn, edge-ml, wasm, tauri, deployment-size, cold-start; domains_live: ml, embedded, desktop-cli-ui, wasm; positions_seen: rust-burn-viable-for-edge-inference

### Claims
- voice: Warre Snaet | position: rust-burn-viable-for-edge-inference | date: 2026-01-24 | locator: "Why Rust? The Burn Framework Decision" and "Conclusion" sections | paraphrase: chose Rust+Burn over Python/PyTorch for an offline plant-disease-detection model targeting phones/laptops with zero connectivity, citing a single ~24MB binary vs. ~7.1GB of PyTorch dependencies (300x), <100ms cold start vs. PyTorch's ~3s, and one model/codebase compiling to native GPU (wgpu), CPU (ndarray), WASM and Tauri-mobile targets; concludes the stack is legitimate for edge inference specifically, not for training | quote: "Rust + Burn is a legitimate ML stack. Not for training transformers, but for edge inference? It's hard to beat." | practiced_evidence: his own shipped pipeline, deployed to desktop (eframe), browser (WASM/ONNX Runtime Web) and an iPhone 12 via Tauri, with measured benchmarks across all three

---

## f008940 — Scientific Computing in Rust Monthly #18 (2026-05-27, en)

### Nothing new
`nothing new`: a newsletter of crate releases and event announcements (burn, cuda-oxide, delaunay, numra, rayon, pluot). Release-note descriptions state authors' design choices in passing (e.g. delaunay's "safe Rust with no unsafe code" goal) but none is a first-person argued Position contesting another practitioner within this source.

---

## f009026 — Work Stealing vs. Executor-Per-Thread: Evaluating different HTTP server workloads with Tokio, Smol and Glommio (2026-08-05, en)

### Questions
- Q: For async Rust HTTP servers, is a work-stealing runtime (Tokio's default) or an executor-per-thread/"thread-per-core" runtime (Glommio, or Tokio/Smol configured with a `LocalRuntime`/`LocalExecutor` per thread) the better architecture — and is either one simply faster, or is the right choice workload-dependent?
  concepts: work-stealing, thread-per-core, io_uring, epoll, tokio, glommio, smol, tail-latency; domains_live: distributed, web, cloud-workers; positions_seen: choice-is-workload-dependent-not-universally-faster

### Claims
- voice: Caio (c410-f3r) | position: choice-is-workload-dependent-not-universally-faster | date: 2026-08-05 | locator: "Final words" section, after 360 benchmarked configurations across 90 scenarios | paraphrase: ran balanced/unbalanced, low/medium/high-scale, CPU- through IO-heavy HTTP/2 workloads across tokio (work-stealing and executor-per-thread configurations), smol-ept and glommio-ept; found io_uring (Glommio) did not strictly outperform epoll-based runtimes even under the unbalanced "noisy neighbor" scenario designed to favor work-stealing, and that tokio's work-stealing configuration specifically showed unexplained throughput anomalies at 8/12 threads with no logged errors on either side; concludes the results are inconclusive on "which is faster" and that the right choice depends on the application's own workload shape | quote: "the benchmarks aren't conclusive. The choice between Executor-Per-Thread and Work-Stealing doesn't seem like a simple matter of \"which is faster\" but rather which architecture best aligns with your specific application logic." | practiced_evidence: WTX (his own project, motivated this investigation after it scored anomalously low in a public HTTP benchmark arena); full benchmark code/data published (data.tar.xz)

---

## f009074 — The Embedded Rustacean Issue #79 (2026-08-28, en)

### Nothing new
`nothing new`: a newsletter link roundup. Headlines touching Rust debates (e.g. "Scaling Memory Safety: AI-Assisted Rewrites of C/C++ Dependencies to Rust", "Experimenting with Function Overloading in Rust: Why It Matters") are teasers only; the linked articles' content is not included in this source.

---

## f009090 — Can You Use ESP32 as SWD Programmer for STM32 with Rust? (2026-09-06, en)

### Nothing new
`nothing new`: a solo embedded tutorial implementing the ARM SWD debug protocol bit-by-bit in `no_std` Rust on an ESP32, to read an STM32's Debug Port IDCODE. Purely instructional; the author states his own implementation choices with no contesting Voice or argued Position on a disputed point.

---

## f009104 — Arguing about arguments (2026-09-21, en)

### Questions
- Q: Should Rust adopt call-site ergonomics features common in other languages — named parameters, optional/default arguments, function overloading — or does the simplicity of "one name, one fixed signature" outweigh the ergonomic gains, given the complexity and interaction effects (evaluation order, patterns-not-names, function-as-value) these features would introduce?
  concepts: named-parameters, default-arguments, function-overloading, function-dispatch, api-ergonomics, language-simplicity; domains_live: core; positions_seen: reject-all-for-simplicity, open-to-named-parameters-only
- Q: Does the rise of AI coding agents change the cost/benefit calculus for verbose, explicit call-site syntax (like named arguments) that was previously judged not worth its typing cost for human authors?
  concepts: ai-assisted-rust, api-ergonomics, agent-readability; domains_live: core; positions_seen: agents-shift-calculus-toward-explicit-named-syntax

### Claims
- voice: Steve Klabnik | position: reject-all-for-simplicity | date: long-standing prior view, "over a decade" per this 2026-09-21 post's own framing (no earlier dated source read; retrospective self-report only) | locator: "These features make me uneasy" section | paraphrase: has for years opposed Rust adding named parameters, optional/default arguments and function overloading (all requested since at least a 12-year-old GitHub issue), arguing the features are numerous, mutually entangled, and that Rust's current rule — one function, one signature, write a differently-named function or a builder if you need variants — keeps the language simple at an acceptable cost | quote: "I've grown to enjoy Rust's simplicity in this area... that's why I've pushed back against the various proposals to extend Rust in this way all of these years." | practiced_evidence: none
- voice: Steve Klabnik | position: open-to-named-parameters-only | date: 2026-09-21 | locator: "I'm okay with named parameters now" section | paraphrase: still opposes optional/default arguments and overloading, but has become open specifically to named parameters (not the other bundled features), while flagging unresolved language-design problems the proposal would need to solve: parameters are patterns not names, function-values erase parameter names, left-to-right evaluation order conflicts with letting call sites reorder named arguments (worked example: `consume(data, data.len())` vs. a hypothetical `consume(length: data.len(), data: data)`), and renaming a parameter becomes a breaking change | quote: "I think Rust could be okay with named parameters, but not optional or default ones." | practiced_evidence: none
- voice: Steve Klabnik | position: agents-shift-calculus-toward-explicit-named-syntax | date: 2026-09-21 | locator: "I'm okay with named parameters now" section | paraphrase: attributes his change of mind to coding agents — since he is "not typing myself anymore," the verbosity cost of named arguments no longer weighs against their call-site clarity benefit, and reasons the clarity gain is if anything larger for an agent reading the call site than for a human, while explicitly noting he hasn't run real evals on this | quote: "what changed my opinion is coding agents, actually... 'What's good for humans is true for agents' strikes again." | practiced_evidence: none (states explicitly: "I haven't run real evals on this yet")
