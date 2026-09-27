## f005516 — Is Rust faster than C? (2025-06-09, en)

Caveat: this lobste.rs capture carries no per-comment usernames or timestamps (only paragraph breaks marked `---`); most commenters are unidentified. Only Bryan Cantrill is name-identified in the text, so he is the only Voice a Claim can be pinned to here.

### Questions
- Q: Is Rust systematically faster than C, or does the apparent gap owe to non-language factors (codebase age, engineer-hours invested, hardware-era assumptions)?
  concepts: performance-comparison, codebase-age, hardware-assumptions; domains_live: core; positions_seen: no-inherent-language-speed-difference, rust-idioms-default-to-faster-collections, c-lets-you-skip-work-rust-forces
- Q: Does Rust's stronger type system (aliasing/`noalias`, provenance, expressiveness) give the compiler real optimization leverage C compilers lack, or is the effect mostly ecosystem/library convenience rather than a language-level speed edge?
  concepts: type-system, aliasing, compiler-optimization, LLVM; domains_live: core; positions_seen: type-system-enables-real-optimizations, effect-is-ecosystem-not-language, borrow-checker-insufficient-for-noalias
- Q: Do Rust's safety defaults (bounds checks, mandatory initialization, `Result` wrapping, `Rc`/clone insertion to satisfy the borrow checker) impose a meaningful runtime cost in practice, or does the optimizer erase it?
  concepts: bounds-checking, zero-initialization, borrow-checker, RefCell; domains_live: core; positions_seen: safety-defaults-have-measurable-cost, optimizer-erases-most-of-it

### Claims
- voice: Bryan Cantrill | position: rust-idioms-default-to-faster-collections | date: undated in this source (an anonymous commenter quotes a Cantrill talk via youtu.be/HgtRAbE1nBM?t=2450 with no air date given here; two Cantrill blog posts are also named — bcantrill.dtrace.org/2018/09/18/falling-in-love-with-rust/ and .../2018/09/28/the-relative-performance-of-c-and-rust/ — whose URL-embedded dates, 2018-09-18 and 2018-09-28, are not independently confirmed since those posts were not fetched) | locator: blockquote citing "Bryan Cantrill @ https://youtu.be/HgtRAbE1nBM?t=2450" | paraphrase: argues Rust's composability lets him reach for a B-Tree where in C he'd stick to an AVL tree, because an intrusive C B-Tree implementation is too risky to trust ("up in everything's underwear") | quote: "the reason I could use a B-Tree and not an AVL tree, is because of that composability of Rust... I would still use an AVL tree in C even though I know I'm giving up some small amount of performance, but in Rust, I get to use a B-Tree." | practiced_evidence: none

---

## f005604 — Oxy is Cloudflare's Rust-based next generation proxy framework (2023-03-02, en)

Note: the in-body byline reads "March 2, 2023"; the row header carries a later re-syndication date (2025-11-03, hn-lobsters). The Claim below is dated to the in-body byline.

### Questions
- Q: When several internal Rust services need similar network-framework capabilities, should the org consolidate them into one shared framework built on existing async-ecosystem crates, or keep purpose-built frameworks separate even at the cost of overlap?
  concepts: framework-design, code-reuse, tokio, hyper, extensibility; domains_live: distributed, web; positions_seen: reuse-and-consolidate-on-ecosystem-crates, keep-separate-for-differing-objectives

### Claims
- voice: Ivan Nikulin | position: reuse-and-consolidate-on-ecosystem-crates | date: 2023-03-02 | locator: "Technology choice" section | paraphrase: states Oxy is deliberately built on top of existing open-source crates (hyper, tokio) rather than reinventing them, prioritizing faster iteration and battle-tested code, while contributing fixes back upstream; two of the team are now core maintainers of tokio/hyper | quote: "We intentionally tried to stand on the shoulders of the giants with this project and avoid reinventing the wheel." | practiced_evidence: cloudflare/boring, cloudflare/quiche (named open-sourced building blocks); Oxy itself (proprietary, not inspectable)

---

## f005693 — onecli (2026-03-12, en)

### Nothing new
`nothing new`: a product README for a team-agent-harness platform. Rust is named only once, as the original implementation language of a credential vault component ("a credential vault for AI agents, built in Rust"); no Voice declares or argues a Position on any contested Rust question.

---

## f005702 — Sycamore (2026-04-01, en)

### Nothing new
`nothing new`: a marketing/features page for a reactive Rust/WASM web UI library. It asserts feature claims (fine-grained reactivity, compile-time type-checked UI, SSR) but no named Voice argues a position against an alternative or contests another practitioner's view within this page.

---

## f005821 — A tail-call interpreter in (nightly) Rust (2026-04-05, en)

### Questions
- Q: Does Rust's nightly `become` tail-call feature produce reliably good codegen across targets, or is it currently good on some architectures and poor on others?
  concepts: tail-calls, nightly-features, codegen, LLVM, calling-conventions, WebAssembly; domains_live: core, wasm; positions_seen: strong-win-on-arm64, poor-inconsistent-elsewhere
- Q: When a project's code is partly produced with LLM assistance in earlier iterations, should a specific piece of performance-critical work be held to a "human-written only" personal standard?
  concepts: ai-assisted-rust, authorship-norms; domains_live: core; positions_seen: human-written-only-as-personal-standard

### Claims
- voice: Matt Keeter | position: strong-win-on-arm64 | date: 2026-04-05 | locator: "Performance results" section, ARM64 and x86-64 benchmark tables plus WASM benchmark table | paraphrase: on ARM64 (M1) the tail-call interpreter beats both the plain VM and Keeter's own hand-written ARM64 assembly; on x86-64 it beats the VM but still loses to hand-written assembly; compiled to WASM it is 1.2–4.6x slower than the plain VM across Firefox, Chrome and wasmtime, which he attributes to the codegen (register spills to the stack) not translating well to the WASM stack machine | quote: "the tail-call interpreter handily beats my hand-written assembly on both benchmarks" (ARM64); "oh no... it's outperforming the VM, but is still losing to the assembly backend" (x86-64) | practiced_evidence: raven-uxn (his own repo); the tailcall PR is merged and shipped as the ARM64 default in the 0.3.0 release
- voice: Matt Keeter | position: human-written-only-as-personal-standard | date: 2026-04-05 | locator: opening paragraphs, linking to his earlier post "Experimenting with LLMs" | paraphrase: states plainly, as a personal standard rather than an argued position, that all the tail-call code and the blog post itself are human-written, after an earlier LLM-assisted port "proved controversial" | quote: "I'm pleased to declare that all of the tail-call code is human-written... (This blog post is also entirely human-written, per my personal standards)" | practiced_evidence: raven-uxn repo (this feature's commits)

---

## f005857 — Playing guitar tablatures in Rust (2024-07-14, en)

### Questions
- Q: For a real-time, stateful interactive Rust desktop app (synchronized audio playback + canvas redraw + UI), is a message-passing/subscription (Elm-style) GUI architecture the better fit over an immediate-mode one?
  concepts: GUI-architecture, message-passing, subscriptions, canvas-rendering; domains_live: desktop-cli-ui; positions_seen: message-passing-fits-realtime-sync

### Claims
- voice: Arnaud Gourlay | position: message-passing-fits-realtime-sync | date: 2024-07-14 | locator: "Building a UI" and "Putting it all together" sections | paraphrase: chose Iced specifically because the app needed an event-based library that could synchronize audio playback state with UI redraws while also supporting custom canvas drawing; used Iced's `Subscription` mechanism to pipe a `tokio::sync::watch` channel of playback ticks into UI messages, and reports being satisfied enough that he did not evaluate other GUI libraries | quote: "I needed a truly event-based library to handle the synchronization during playback while also being able to draw the tablature in a custom way with some kind of canvas abstraction... Spoiler alert: I am very happy with my choice so I did not try other libraries." | practiced_evidence: agourlay/ruxguitar (shipped, linked from the post)

---

## f005948 — Lambda on hard mode: Inside Modal's web infrastructure (2024-03-14, en)

### Questions
- Q: For a high-throughput, failure-heavy network service (translating HTTP/WebSocket traffic into distributed function calls), does Rust's pattern matching and ownership model meaningfully help manage the failure-case complexity, beyond raw speed?
  concepts: pattern-matching, ownership, error-handling, distributed-systems, hyper, tokio; domains_live: cloud-workers, distributed; positions_seen: ownership-and-pattern-matching-aid-correctness-at-scale

### Claims
- voice: Eric Zhang | position: ownership-and-pattern-matching-aid-correctness-at-scale | date: 2024-03-14 | locator: "Edge cases and errors" section | paraphrase: reports building `modal-http` (HTTP/WebSocket-to-function-call translation service) in Rust on hyper/tokio specifically for speed and to help manage the many concurrent failure cases (client disconnects, malformed/out-of-order events, spot preemption); credits the language's pattern matching and ownership for handling that casework, and separately reports that replacing an earlier Python-based ingress with this Rust service cut 502 errors by 99.7% | quote: "This was tricky! HTTP has quite a few edge cases, so we used Rust for its speed and to help manage the complexity." / "Rust's pattern matching and ownership help with managing the casework." | practiced_evidence: modal-http (named, in production; 99.7% reduction in 502s reported after replacing the prior Python ingress)

---

## f006797 — Librsvg usará decodificadores de imágenes en Rust desde la versión 2.58.0 (2023-12-22, es)

### Questions
- Q: When a safety-critical C library (image codecs) has decades of fuzzing and battle-testing, does the memory-safety case for migrating it to a less mature Rust crate outweigh the loss of that testing track record?
  concepts: memory-safety, ffi, migration, fuzzing, maturity-vs-safety-tradeoff; domains_live: core, desktop-cli-ui; positions_seen: prioritize-memory-safety-despite-lower-maturity

### Claims
- voice: Federico Mena Quintero | position: prioritize-memory-safety-despite-lower-maturity | date: 2023-12-22 | locator: "Se buscan probadores" section | paraphrase: librsvg is dropping gdk-pixbuf's C image decoders in favor of the Rust `image-rs` crate to move the stack off memory-unsafe codecs, while explicitly acknowledging that the incumbent C libraries (libpng, libjpeg-turbo) are heavily tested and continuously fuzzed, and that the Rust decoder crates are comparatively less developed on performance and exotic-format support; frames the migration as an opportunity to find and fix exactly those gaps rather than a claim that the Rust crates are already equally mature | quote: "Digan lo que digan sobre el código sin seguridad de memoria como libpng y libjpeg-turbo, ese código está muy bien probado y se le hace fuzzing todo el tiempo. Los huacales de Rust para decodificar imágenes todavía no están tan bien desarrollados... creo que esta es una buena oportunidad para encontrar exactamente qué es lo que les falta." | practiced_evidence: librsvg (merge request against its own main branch, named in the post)
