## f011305 — Dioxus: the future of high-level Rust (2025-10-03, en)

Speaker self-identifies as "Jonathan Kelly" (likely "Jonathan Kelley" — auto-caption name garble, flagged for t3 voice verification), creator/lead developer of "Diosis"/"Daxis" (the caption's rendering of Dioxus), a cross-platform Rust application framework with 30,000+ GitHub stars.

### Questions
- Q: should Rust be pushed into high-level, rapid-prototyping application development, or kept to systems/"core" software?
  concepts: application frameworks, systems vs application programming; domains_live: desktop-cli-ui, frontend, web, other; positions_seen: push-Rust-into-high-level-dev (Jonathan Kelley/Dioxus)
- Q: do Rust's compile times and language rigidity make it less productive than high-level frameworks (React, FastAPI) for rapid prototyping?
  concepts: compile times, developer productivity, language ergonomics; domains_live: core, web, frontend; positions_seen: yes-less-productive-but-worth-fixing (Jonathan Kelley)
- Q: should Rust adopt a lightweight/automatic-clone mechanism (e.g. reference-counted "generational box" ergonomics) for callback-heavy UI code, trading some compile-time guarantees for runtime checks?
  concepts: ownership, clone ergonomics, async/callbacks; domains_live: core, frontend, desktop-cli-ui; positions_seen: add-lightweight-clones-to-Rust (Jonathan Kelley, proposed as a project goal); opposed-or-skeptical (unnamed — Kelley states "not everyone may agree" and "opinions were divided" without naming the dissenters)
- Q: should Rust macros get first-class IDE tooling (autocomplete, hover, partial expansion) via new mechanisms, or is today's macro opacity accepted as a tradeoff for macro power?
  concepts: macros, DSLs, IDE tooling; domains_live: core; positions_seen: build-new-tooling-for-macro-IDE-support (Jonathan Kelley, re: "partial expressions" library)
- Q: should a hot-reload/hot-patch mechanism bypass the normal cargo build/linking pipeline to get near-instant iteration, even at the cost of many platform-specific edge cases?
  concepts: build tooling, linkers, hot reload; domains_live: core, desktop-cli-ui, embedded; positions_seen: bypass-the-linker-for-speed (Jonathan Kelley, re: "Subsecond")
- Q: should a Rust GUI framework build its own modular rendering engine rather than wrap native platform widgets or an existing browser engine?
  concepts: GUI rendering, native widgets vs custom renderer; domains_live: desktop-cli-ui, frontend; positions_seen: build-custom-modular-renderer (Jonathan Kelley, re: "Blitz")

### Claims
- voice: Jonathan Kelly [likely Kelley; unconfirmed] | position: push Rust into high-level application development | date: 2025-10-03 | locator: ~03:01 | paraphrase: Rust's mission should not be exclusive to systems/"core" software; high-level Rust development deserves the same investment | quote: "I don't think this should be exclusive to so-called core software" | practiced_evidence: Dioxus (30,000+ GitHub stars, in use at Airbus and the European Space Agency per the talk)
- voice: Jonathan Kelly | position: Rust is currently less productive than high-level frameworks for prototyping | date: 2025-10-03 | locator: ~02:01 | paraphrase: long compile times and language rigidity made Dioxus's own users more productive with existing tools like React and FastAPI than with early high-level Rust | quote: "we realized that Rust just wasn't that fast to write. Due to the long compile times and language rigidity, our users were simply more productive" | practiced_evidence: none stated beyond his own framework's user feedback
- voice: Jonathan Kelly | position: add lightweight/automatic clone ergonomics to Rust itself | date: 2025-10-03 | locator: ~15:06-16:09 | paraphrase: proposed a Rust project goal adding lightweight clones for types like reference-counted smart pointers, prototyped as "generational box"; acknowledges it is contested | quote: "this is a controversial change in the Rust language. Not everyone may agree, but in my opinion, this is critical to the success of high-level Rust" / "Opinions were divided" | practiced_evidence: "generational box" crate, described as already used in Dioxus
- voice: Jonathan Kelly | position: build new tooling rather than accept macro IDE opacity | date: 2025-10-03 | locator: ~13:06 | paraphrase: since Rust macros don't support autocomplete or partial expansion, they built a separate library ("partial expressions") to give macro-based DSLs IDE support | quote: "Rust macros do not support things like autocomplete and partial expansion. So we developed new libraries, such as partial expressions, to make it easier to write high-quality Rust DSLs" | practiced_evidence: used in Dioxus's RSX macro tooling per the talk
- voice: Jonathan Kelly | position: bypass cargo's build/link pipeline for hot-patching | date: 2025-10-03 | locator: ~22:12-23:12 | paraphrase: "Subsecond" hot-patches running Rust binaries by recompiling only changed crates and linking them to hardcoded addresses at runtime, skipping the normal linking step, despite "a huge number of quirks, edge cases, incomprehensible behavior" needed to make it work | quote: "it bypasses the traditional cargo build system, almost completely eliminating the expensive linking step that slows down incremental development" | practiced_evidence: Subsecond, stated to be integrated into Bevy and "ICE" (unclear which project; garbled name)
- voice: Jonathan Kelly | position: build a custom modular GPU-based renderer rather than reuse an existing engine | date: 2025-10-03 | locator: ~17:09-18:10 | paraphrase: Dioxus's Blitz renderer alternates native system widgets with a custom GPU-based drawing layer, positioned against unnamed "existing solutions" as free, open-source, and modular | quote: "unlike existing solutions, Blitz is free, open source, and extremely modular" | practiced_evidence: Blitz, stated to render sites like Hacker News and BBC and to embed into Bevy

## f011443 — Shaping Tomorrow's Software Engineer: Why Rust Belongs in the Academy (2026-06-11, en)

Speaker: Mordecai Emmanuel Etukudo, self-identified as project team lead at Rust Stations Africa / co-organizer of Rust Nigeria, contributor to Rust 101 and the Rust educational team. Remote talk, likely at a European Rust conference (venue unnamed in the transcript excerpt).

### Questions
- Q: should introductory CS/software-engineering curricula teach a systems language like Rust directly (to force understanding of memory, concurrency, ownership), or is teaching via high-level frameworks and abstractions sufficient?
  concepts: education, ownership, memory, concurrency; domains_live: other; positions_seen: teach-Rust-directly-in-the-academy (Mordecai Etukudo)
- Q: is Rust the best-suited language for an AI-driven future where machines write code and humans architect systems (because the compiler independently checks AI-generated code)?
  concepts: AI-assisted Rust, compiler guarantees; domains_live: ml, core, other; positions_seen: yes-Rust-is-best-for-AI-generated-code (Mordecai Etukudo)

### Claims
- voice: Mordecai Emmanuel Etukudo | position: teach Rust directly to force systems understanding | date: 2026-06-11 | locator: ~01:10-02:10 | paraphrase: modern software education over-focuses on frameworks and abstractions and under-teaches how systems actually work (memory, concurrency, performance, tradeoffs); learning Rust forces students to confront ownership, memory, and error handling directly, concepts other languages abstract away | quote: "The modern software education... focus more on teaching people about framework and a lot of abstractions... it's not bad to use frameworks... but it's nice to understand what is going on behind the wood" | practiced_evidence: Rust Africa campus tour and workshops, cited student outcomes ("Oh, I now understand how this system work")
- voice: Mordecai Emmanuel Etukudo | position: Rust is the best language for an AI-coding future | date: 2026-06-11 | locator: ~13:17-14:18 | paraphrase: as AI increasingly writes code and humans architect systems, Rust's compiler acts as an independent, automatic check on AI-generated code that other languages' compilers don't provide | quote: "Rust is the best language for AI because AI is is like bare machine... with Rust, which the compiler have already... is already there to vet your system and know that this code is not having memory leaks" | practiced_evidence: none stated

## f011460 — Debunking Rust/Wasm performance myths (Canva) (2026-06-11, en)

Speakers: Andrew Jakubowicz (software engineer at Canva, using Rust professionally for ~8 years) and a co-presenter transcribed inconsistently as "Touch"/"Taj" (final applause names "Josh Pereira" — name uncertain, flagged for t3 voice verification). Both describe maintaining Rust/Wasm crates at Canva (one names having "crates that I maintain," e.g. "Velo").

### Questions
- Q: is JavaScript "fast enough" for typical web workloads, making Rust+Wasm unnecessary outside of the heaviest-compute applications?
  concepts: WebAssembly, JavaScript performance, FFI; domains_live: wasm, frontend, web; positions_seen: no-Rust+Wasm-beats-JS-more-broadly (Andrew Jakubowicz / co-presenter), contrasted against a blanket claim they attribute to unnamed articles ("JavaScript is fast enough")
- Q: should WebAssembly be reserved for heavy-compute workloads only, or is it competitive even for small, string-heavy, low-computation functions?
  concepts: WebAssembly, FFI design, string marshaling; domains_live: wasm, frontend; positions_seen: Wasm-competitive-even-for-small-functions-with-hand-tuned-FFI (Andrew Jakubowicz)
- Q: at the Rust/Wasm↔JavaScript FFI boundary, should code favor ergonomic serialization (serde-wasm-bindgen) or manual/structural field access (wasm-bindgen getters), trading ergonomics against performance?
  concepts: wasm-bindgen, serialization, FFI ergonomics; domains_live: wasm, frontend; positions_seen: use-serde-for-cold-paths-getters-for-hot-paths (Andrew Jakubowicz, describing what he found practiced on GitHub)

### Claims
- voice: Andrew Jakubowicz and co-presenter (Canva) | position: Rust+Wasm beats "JS is fast enough" as a blanket claim | date: 2026-06-11 | locator: ~01:10 | paraphrase: articles claiming Rust FFI is too slow, that Wasm should be reserved for the heaviest compute, and that JavaScript is fast enough, are myths the talk sets out to bust with benchmarks | quote: "we're going to be sharing how to design your Rust FFI so that it's fast... Rust and WebAssembly can be blazingly fast for a variety of applications... and that JavaScript is not always fast enough" | practiced_evidence: benchmark site referenced in the talk (URL not spoken)
- voice: co-presenter ("Taj"/"Touch"/unclear) | position: Wasm is competitive even for small, low-computation, string-heavy functions | date: 2026-06-11 | locator: ~18:28-19:29 | paraphrase: after hand-optimizing a hex-color-parsing function (pre-allocating memory, skipping UTF-16→UTF-8 conversion, packing bits), the Wasm version beat the JavaScript control by roughly 2x despite the function being "very hostile" to Wasm (string copy, minimal computation, allocation on return) | quote: "if WebAssembly is competitive here, then maybe the blanket advice to use WebAssembly on only heavy compute is too simple" | practiced_evidence: benchmark shown in the talk (Chrome results), code said to be published in "the book" referenced by the speakers
- voice: Andrew Jakubowicz | position: choose serde-wasm-bindgen vs wasm-bindgen getters based on hot/cold path | date: 2026-06-11 | locator: ~25:39 | paraphrase: after surveying GitHub crates, found people mostly using serde-wasm-bindgen (more ergonomic, more allocation) for cold paths like config initialization, and wasm-bindgen getters/reflection (faster, less ergonomic) for hot paths | quote: "from serving some GitHub crates, I found people are mostly doing the like the right thing, basically. Using serde-wasm-bindgen for cold paths, config initialization, and then using wasm-bindgen getters... if they're needed" | practiced_evidence: his own GitHub crate survey, described but not quantified in the talk

## f011484 — Rust RFCs process README (2023-09-27, en)

### Nothing new
`nothing new` — this is the RFC repository's own process documentation (README), describing the governance mechanism itself (how RFCs are filed, reach final comment period, etc.); it states no Voice's position on a contested Question, only the institutional process, consistent with the existing finding that curated/reference documents record conclusions or process, not disagreements.

## f011605 — The Ultimate Guide to Axum: From Hello World to Production in Rust (2023-12-06, updated 2025-07-04, en)

Voice: Joshua Mo, byline on the shuttle.rs company blog.

### Questions
- Q: should a Rust web framework favor a macro-free, type/extractor-driven API design, or a macro-based route/handler declaration syntax?
  concepts: web frameworks, macros, API design; domains_live: web; positions_seen: macro-free-api-design-as-a-selling-point (Joshua Mo, re: Axum)
- Q: should a Rust web framework be built around the actor model, or around a Service/Layer (Tower) middleware model?
  concepts: web frameworks, actor model, middleware; domains_live: web; positions_seen: Tower-Service/Layer-model-often-preferred-for-simplicity (Joshua Mo, re: Axum vs Actix Web)

### Claims
- voice: Joshua Mo | position: macro-free API design is a distinguishing strength | date: 2023-12-06 (updated 2025-07-04) | locator: heading "Getting Started with Axum: Building REST APIs in Rust" (intro paragraph) | paraphrase: Axum stands out among Rust web frameworks specifically for its macro-free API design, predictable error handling, and Tower-based middleware | quote: "What makes Axum stand out in the Rust programming landscape is its macro free api design, predictable error handling model, and own middleware system built on Tower" | practiced_evidence: none stated beyond describing Axum's own design
- voice: Joshua Mo | position: Axum's Tower-based design is often preferred over Actix Web's actor model | date: 2023-12-06 (updated 2025-07-04) | locator: FAQ "What is the difference between Axum and Actix Web?" | paraphrase: both frameworks are fast and production-ready, but Axum's simplicity and tight Tokio integration is "often preferred" over Actix Web's actor-model design | quote: "Actix Web uses the actor model and has its own mature middleware system. Both are fast and production-ready, but Axum's design philosophy is often preferred for its simplicity and tight integration with Tokio" | practiced_evidence: none stated (no usage data given)

## f011614 — The Tianyi-33 Satellite Equipped with RROS Successfully Entered Orbit (2023-12-20, en)

### Nothing new
`nothing new` — a factual news announcement that RROS (a Rust-based dual-kernel real-time OS) launched aboard a satellite; it states no contested Question or Voice position, only an achievement report.

## f011684 — Diagnosing Memory Leaks with Flame Graphs and Jemalloc (2024-01-31, en)

Voice: Lei Huang, Software Engineer, GreptimeDB.

### Questions
- Q: should a Rust database's heap-profiling instrumentation (e.g. jemalloc mem-prof) be compiled in and enabled by default, or opt-in via a build feature flag?
  concepts: memory profiling, build features, observability tooling; domains_live: core, other; positions_seen: currently-off-by-default-with-open-internal-debate (GreptimeDB team, no side taken by this Voice)

### Claims
- voice: Lei Huang | position: none declared — reports an open, unresolved internal debate | date: 2024-01-31 | locator: section "Enabling Heap Profiling in GreptimeDB" | paraphrase: GreptimeDB currently ships with heap profiling (mem-prof) off by default, compiled in only via a cargo feature flag; whether it should be on by default is an active, unresolved discussion the author points readers to rather than settles | quote: "The discussion about whether the mem-prof feature should be enabled by default is ongoing in greptimedb#3166. You are welcome to share your opinion there" | practiced_evidence: GreptimeDB's own shipped default (off), stated in the article

## f011993 — "Is there something like Rust Core Guidelines (like C++ Core Guidelines)?" (users.rust-lang.org thread) (2024-07-03/04, en)

### Questions
- Q: should Rust have a prescriptive "core guidelines" document (as C++ has C++ Core Guidelines), or rely on compiler enforcement plus automated lints (Clippy) and de-facto popular-crate conventions instead?
  concepts: language guidelines, Clippy lints, idiomatic Rust, static analysis; domains_live: core; positions_seen: prefer-compiler-and-lint-enforcement-over-a-guidelines-document (forum user "kornel")

### Claims
- voice: kornel (forum handle; identity/track record not established by this source, flagged for t3 verification) | position: enforce via compiler and Clippy lints rather than write a guidelines document | date: 2024-07-04T18:13:51.115Z | locator: https://users.rust-lang.org/t/is-there-something-like-rust-core-guidelines-like-c-core-guidelines/113850/3 (post 3) | paraphrase: Rust's preferred solution is to avoid needing such a document at all — the language is designed to be statically analyzable so the compiler enforces as much of "the guidelines" as possible, and for softer/more subjective conventions, Clippy lints are written instead of documenting best practices, with popular crates serving as de-facto standards | quote: "In Rust, the preferred solution is to avoid the need for such document to exist... Whenever a gotcha is discovered in Rust, instead of documenting the best practice that avoids it, someone writes a Clippy lint for it" | practiced_evidence: cargo clippy itself, cited as containing "hundreds of lints detecting unidiomatic or suspiciously looking code"

## f012146 — Rust review: Loco.rs vs Rails, vs Leptos/Dioxus (2024-10-09, en)

Speaker not self-identified within the read portion of the transcript (video opens mid-talk at [00:01]); appears to be a Rust-focused YouTube reviewer covering the loco.rs framework. Flagged for t3 voice/track-record verification — identity and public Rust track record not established by this source alone.

### Questions
- Q: should Rust be pushed into high-level, rapid-prototyping application development, or kept to systems/"core" software? [reusing wording from f011305]
  concepts: application frameworks, isomorphic client/server code; domains_live: web, frontend; positions_seen: unified-isomorphic-Rust-client/server-model-preferred (this reviewer, re: Leptos), vs Rails-style-server-MVC-with-separate-JS-frontend (Loco, as described by the reviewer)

### Claims
- voice: unidentified reviewer | position: prefers Leptos's isomorphic client/server model over Loco's Rails-style MVC + separate JS frontend | date: 2024-10-09 | locator: ~07:06-08:07 | paraphrase: while Loco replicates Rails's batteries-included scaffolding (CLI generators, DB migrations, auth out of the box) and defaults to a separate React frontend, Leptos instead lets a developer define server functions callable directly from client code, with the client/server interface auto-generated, and lets logic move between client and server "almost effortless[ly]" | quote: "leptos is my absolute favorite way to build web applications these days so I'm a little biased... what lepos does have though is a lot more flexibility on whether you'd like a given piece of logic to run on the browser or on the server" | practiced_evidence: none stated (personal preference, not usage data)
