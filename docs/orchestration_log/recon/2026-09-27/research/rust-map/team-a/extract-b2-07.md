## f005337 — Is Linux collapsing under its own weight? On Rust for Linux (2024-09-05, en)

### Questions
- Q: When a safe Rust abstraction over a legacy C kernel API becomes hard to express cleanly, should the fix change the C-side API/semantics, or should the Rust abstraction absorb the complexity through runtime workarounds?
  concepts: FFI abstraction design, ownership/lifetime encoding, kernel API contracts, unsafe boundary; domains_live: embedded, core; positions_seen: fix-the-c-side-over-runtime-workarounds (inactive-user)

### Claims
- voice: inactive-user | connection: posted a first-person account of writing the Rust safe abstraction for drm_sched in the Linux kernel, describing implementation tradeoffs in their own work | position: fix-the-c-side-over-runtime-workarounds | date: 2024-09-07 | locator: comment by @inactive-user, 2024-09-07T06:01:23 | paraphrase: When a legacy C API's implicit contract is too tangled to encode safely in Rust's type system without heavy workaround complexity (extra reference-counting layers, deferred async cleanup), the better fix is to change the C-side semantics rather than pile complexity into the Rust abstraction — as happened with drm_sched job lifetimes. | quote: "writing a Rust abstraction without touching the C is *possible* but it's *impractical* and clearly the wrong technical decision." | practiced_evidence: none | flag: voice-unverified

## f005350 — Rewriting Rust: A Response (2024-09-27, en)

### Nothing new
reason-code: no-rust-voice
reason: Gavin Howard critiques Rust's Pin, Box and async-color design from outside as the designer of his own language Yao, comparing it to Rust throughout, but never states his own Rust use or a Rust role.

## f005351 — Announcing iceoryx2 v0.4.0 (2024-09-28, en)

### Questions
- Q: Should a Rust IPC library size its shared-memory service buffers using compile-time-fixed configuration, or allow runtime-determined dynamic sizing?
  concepts: static vs. dynamic sizing, const generics/fixed buffers vs. allocation, shared-memory IPC; domains_live: distributed, embedded, core; positions_seen: dynamic-sizing-over-compile-time-config (Christian Eltzschig / iceoryx2 team)

### Claims
- voice: Christian Eltzschig | connection: core team author of iceoryx2, a Rust IPC crate published on crates.io (linked from the post) | position: dynamic-sizing-over-compile-time-config | date: 2024-09-28 | locator: section "Highlights › Runtime-sized services" | paraphrase: iceoryx2 replaced iceoryx1's compile-time-fixed memory pool configuration with runtime-sized services, letting a dynamic-sized typed array (like a Rust slice) be sent without pre-declaring pool sizes at compile time. | quote: "We've overcome the compile-time memory configuration limitation of iceoryx1." | practiced_evidence: none | flag: voice-unverified

## f005626 — Announcing Prisma 7: Rust-Free, Faster, and More Compatible (2025-11-19, en)

### Questions
- Q: When should a Rust core inside a library or product be replaced with a higher-level language, trading raw performance for contributor accessibility and simpler cross-runtime interop?
  concepts: FFI/interop overhead, contributor accessibility, Rust as an embedded engine inside another language's ecosystem; domains_live: web, cloud-workers; positions_seen: move-off-rust-for-contributor-access-and-ffi-cost (Prisma)

### Claims
- voice: Prisma | connection: built and maintained the Prisma Client's core query engine in Rust for years before this migration, as declared in this post | position: move-off-rust-for-contributor-access-and-ffi-cost | date: 2025-11-19 | locator: section "Moving away from Rust" | paraphrase: Prisma moved its ORM client's core off Rust and onto TypeScript because Rust's contribution bar was too high for community contributors and the Rust-to-JS-runtime communication layer was slower than plain JavaScript, despite Rust's raw-performance premise. | quote: "A side effect of the client being built in Rust is that we were limiting who can contribute to the ORM." | practiced_evidence: none | flag: voice-unverified

## f005691 — Notes on Writing Wasm (2025-12-27, en)

### Questions
- Q: When binding Rust to JS via wasm-bindgen, should crossing types use manual js_sys conversions, or lean on bindgen's generated glue plus a naming convention?
  concepts: wasm-bindgen, FFI ergonomics, compile-time feedback; domains_live: wasm, frontend; positions_seen: lean-on-bindgen-glue-over-manual-conversions (Brooklyn Zelenka)
- Q: Should Wasm-exported Rust wrapper types that represent handles derive Copy?
  concepts: Copy semantics, handle safety, wasm-bindgen exports; domains_live: wasm; positions_seen: no-copy-on-exported-handle-types (Brooklyn Zelenka)
- Q: Should Rust values crossing the Wasm/JS boundary be passed by reference with interior mutability, or by ownership transfer?
  concepts: ownership across an FFI boundary, interior mutability, ABI handles; domains_live: wasm; positions_seen: pass-by-reference-over-consuming-ownership-at-boundary (Brooklyn Zelenka)

### Claims
- voice: Brooklyn Zelenka | connection: self-reported "I've been writing an increasing amount of Rust-based Wasm over the past few years" and author of the wasm_refgen crate described in the post | position: lean-on-bindgen-glue-over-manual-conversions | date: 2025-12-27 | locator: section "Should You Write Manual Bindings?" | paraphrase: Rather than hand-writing manual conversions via js_sys when crossing the Wasm boundary, prefer wasm-bindgen's generated glue with the naming/reference patterns in this post, because manual dyn_into-based conversions are time-consuming and brittle and get no compiler help when Rust-side types change. | quote: "if you lean into its glue... you can get much better compile-time feedback." | practiced_evidence: none | flag: voice-unverified
- voice: Brooklyn Zelenka | connection: self-reported "I've been writing an increasing amount of Rust-based Wasm over the past few years" and author of the wasm_refgen crate described in the post | position: no-copy-on-exported-handle-types | date: 2025-12-27 | locator: section "Don't Derive Copy" | paraphrase: Exported Wasm-bound wrapper types that represent a handle to a resource should not derive Copy, even though deriving Copy wherever possible is the normal habit in Rust code, because Copy makes it trivially easy to duplicate a handle and produce null-pointer bugs; Copy stays fine only for pure IntoWasmAbi data, never for handles. | quote: "Copy is only acceptable when exporting wrapping around pure data that has IntoWasmAbi, never for handles." | practiced_evidence: none | flag: voice-unverified
- voice: Brooklyn Zelenka | connection: self-reported "I've been writing an increasing amount of Rust-based Wasm over the past few years" and author of the wasm_refgen crate described in the post | position: pass-by-reference-over-consuming-ownership-at-boundary | date: 2025-12-27 | locator: section "Prefer Passing By Refence (by Default)" | paraphrase: Default to passing values across the Wasm boundary by reference, wrapped in Rc<RefCell<T>> or Arc<Mutex<T>>, rather than consuming/owning them, because consuming a value is legal to the Rust compiler but leaves the JS-side handle dangling with no compiler-enforced safety, while the reference-counting cost is negligible next to the cost of crossing the boundary itself. | quote: "pass by &reference and use interior mutability." | practiced_evidence: none | flag: voice-unverified

## f005692 — A fully snapshotable Wasm interpreter (2026-03-11, en)

### Nothing new
reason-code: no-decision
reason: The thread is collaborative brainstorming among the interpreter's author and commenters about time-travel-debugging data structures, with no declared Position stated against a named alternative.

## f005802 — Andreas Thom on OpenAI and unpublished mathematics (2026-09-10, en)

### Nothing new
reason-code: off-subject
reason: The thread is about trust in OpenAI's handling of unpublished mathematics research and training-data transparency; it holds no Rust content at all.
