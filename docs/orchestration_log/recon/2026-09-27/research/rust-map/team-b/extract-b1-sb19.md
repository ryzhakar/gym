## f005691 — Notes on Writing Wasm (2026-03-08, en)

### Questions
- Q: When wrapping Rust types for wasm-bindgen, should a practitioner write manual `js_sys` conversions or lean into bindgen's generated glue (accepting its naming/wrapper conventions)?
  concepts: wasm-bindgen, FFI boundary, newtype wrappers; domains_live: wasm;frontend; positions_seen: lean-into-bindgen-glue (Brooklyn Zelenka)

### Claims
- voice: Brooklyn Zelenka | position: lean-into-bindgen-glue | date: 2026-03-08 | locator: § "Should You Write Manual Bindings?" | paraphrase: manual conversion with js_sys is a reasonable but time-consuming, brittle strategy; leaning into bindgen's glue (with naming conventions) buys better compile-time feedback | quote: "I see a fair amount of code online that seems to prefer manual conversions with js_sys. This is a reasonable strategy, but I have found it to be time consuming and brittle." | practiced_evidence: https://github.com (wasm_refgen crate, named but URL not given in text)

### Nothing new
(none — one Question/Claim extracted above)

---

## f005699 — Rewriting our Rust WASM Parser in TypeScript (2026-03-20, en)

### Questions
- Q: For a given workload, does compiling Rust to WASM for browser execution actually beat a pure JS/TypeScript implementation, once the JS↔WASM boundary cost is counted?
  concepts: wasm-bindgen boundary cost, serde-wasm-bindgen, JIT compilation, algorithmic complexity vs language choice; domains_live: wasm;frontend; positions_seen: wasm-only-for-compute-bound-minimal-interop (Thesys Engineering Team)

### Claims
- voice: Thesys Engineering Team | position: wasm-only-for-compute-bound-minimal-interop | date: 2026-03-20 | locator: § "When WASM Actually Helps" / "Key Takeaways" | paraphrase: WASM wins only for compute-bound work with rare boundary crossings (image/video, crypto, physics, porting existing C/C++ libs); it loses for parsing structured text into JS objects and for frequently-called functions on small inputs, because the serialization/boundary tax dominates and V8's JIT closes the raw-compute gap | quote: "The Rust parsing itself was never the slow part. The overhead was entirely in the boundary" | practiced_evidence: none given (no repo URL in text)

### Nothing new
(none)

---

## f005743 — Memory safety is a matter of life and death (lobste.rs thread) (2026-06-02, en)

### Questions
- Q: Is adopting a memory-safe language (Rust) a moral imperative, or an engineering/economic tradeoff decision like any other?
  concepts: memory safety, moral framing of tooling choices, economics of open-source maintenance; domains_live: core; positions_seen: reject-moral-framing (toastal, mtset, alandekok, duncan_bayne, hobbified), economic-choice (alandekok)
- Q: Does Rust's affine-type system provide sufficient correctness guarantees, or is further formal verification (linear/dependent types, model checkers) needed on top of it?
  concepts: affine types, linear types, dependent types, Frama-C, TrustInSoft; domains_live: core; positions_seen: needs-stronger-formal-guarantees (toastal, madhadron), combine-rust-with-formal-tools (wucke13)
- Q: Is "memory safety" the right frame for language-correctness discourse, or is "correctness" (of which memory safety is one part) the property that actually matters?
  concepts: memory safety vs correctness; domains_live: core; positions_seen: correctness-is-the-real-target (kristoff)
- Q: Does Rust's toolchain-bootstrapping trust gap (rustc's own build chain depending on prior binaries/other compilers) undermine memory-safety arguments for adopting it?
  concepts: bootstrappable builds, mrustc, supply-chain trust; domains_live: core; positions_seen: bootstrapping-undermines-safety-argument (jackdk)
- Q: Should the Rust project prioritize speed of consensus / shipping over slower, more inclusive decision-making (e.g. long-nightly-gated APIs, stabilization pace)?
  concepts: RFC process, nightly-only APIs, project governance, BDFL model; domains_live: core; positions_seen: process-speed-risks-exclusion (lake)

### Claims
- voice: toastal | position: reject-moral-framing | date: 2026-06-02 | locator: comment at 2026-06-02T12:14:03-05:00 | paraphrase: escalating "moral imperative" logic could equally be used to demand replacing Rust itself with something formally stronger, which shows the framing proves too much | quote: "We must abolish Rust for something stronger with proofs. This is a moral imperative. /s" | practiced_evidence: none
- voice: alandekok | position: economic-choice | date: 2026-06-02 | locator: comment at 2026-06-02T12:36:53-05:00 | paraphrase: correctness/safety outcomes are driven by who funds the work, not by language choice alone; citing unfunded xz-utils maintenance | quote: "Correctness and safety is an _economic_ choice.  No one is funding fixes to xz utils.  Yet people are making millions of dollars off of it." | practiced_evidence: none
- voice: mtset | position: reject-moral-framing | date: 2026-06-02 | locator: comment at 2026-06-02T14:37:20-05:00 | paraphrase: there are genuine moral imperatives in the industry, but language choice isn't one of them | quote: "There are many real moral imperatives in our industry; Rust isn't one." | practiced_evidence: none
- voice: toastal | position: needs-stronger-formal-guarantees | date: 2026-06-02 | locator: comment at 2026-06-02T12:14:03-05:00 | paraphrase: Rust's affine types are weaker than linear+dependent type guarantees | quote: "Affine types do not offer the same guarantees as linear types + dependent types." | practiced_evidence: none
- voice: madhadron | position: needs-stronger-formal-guarantees | date: 2026-06-02 | locator: comment at 2026-06-02T12:39:44-05:00 | paraphrase: proposes integrated model checkers (e.g. Frama-C) as the stronger alternative/complement to a type system | quote: "Or we could insist on something like Frama C or other model checkers integrated in." | practiced_evidence: none
- voice: wucke13 | position: combine-rust-with-formal-tools | date: 2026-06-05 | locator: comment at 2026-06-05T04:25:37-05:00 | paraphrase: formal-verification tooling (TrustInSoft's Frama-C port) can sit alongside Rust rather than replace it | quote: "I believe TrustInSoft offers a Frama C port to Rust, so, not mutually exclusive with the use of Rust!" | practiced_evidence: none
- voice: kristoff | position: correctness-is-the-real-target | date: 2026-06-02 | locator: comment at 2026-06-02T13:32:19-05:00 | paraphrase: memory-safety-centric arguments miss that correctness is the broader property that matters | quote: "Every time a blog post over-fits on memory safety, it's a missed opportunity to talk about correctness, which is a strict superset and what actually matters." | practiced_evidence: none
- voice: jackdk | position: bootstrapping-undermines-safety-argument | date: 2026-06-02 | locator: comment at 2026-06-02T17:16:20-05:00 | paraphrase: language-level memory safety is moot if the compiler's own bootstrap chain can't be trusted; would make avoiding Rust (until bootstrapping is fixed, e.g. keeping mrustc close to mainline) the "moral imperative" by the same logic | quote: "all the language-level memory safety cannot help you because your compiler itself could be compromised" | practiced_evidence: none
- voice: lake | position: process-speed-risks-exclusion | date: 2026-06-02 | locator: comment at 2026-06-02T13:04:24-05:00 | paraphrase: reads the (quoted, unnamed) source article as calling the community to sideline collaborative/inclusive decision-making in favor of faster "progress"; contrasts with frustration over long-stalled nightly-only APIs and floats wanting a BDFL model | quote: "We must learn to recognize when having a consensus is more important than having the right consensus, and in these cases, to pick progress over stagnation." | practiced_evidence: none

### Nothing new
(none — this source was the densest in the batch)

---

## f005802 — Andreas Thom Mastodon thread on OpenAI/training-data trust (2026-09-10, en)

### Nothing new
`nothing new`: the thread concerns whether OpenAI can be trusted with unpublished mathematics research and training-data provenance; it contains no Rust-practitioner decision or Position and is out of subject scope.

---

## f005836 — The memory remains: Permanent memory with systemd and a Rust allocator (2024-01-17, en)

### Questions
- Q: To persist Rust objects across process/container restarts, should a practitioner build a custom raw-memory `Allocator` (memfd + systemd FD store + mmap) rather than serializing state to an external store (file/Redis) on shutdown/startup?
  concepts: custom Allocator trait (nightly), memfd_create, systemd File Descriptor Store, mmap; domains_live: core; positions_seen: custom-allocator-for-restart-persistence (Graham King)
- Q: Should Rust types that back raw/mmap'd persistent memory declare `#[repr(C)]`, given Rust makes no default layout guarantee across compiler/binary versions?
  concepts: repr(C), memory layout stability, ABI; domains_live: core; positions_seen: repr-c-required (Graham King)

### Claims
- voice: Graham King | position: custom-allocator-for-restart-persistence | date: 2024-01-17 | locator: § opening / "An allocator backed by persistent memory" | paraphrase: combining systemd's FD store, `memfd_create`, and a custom Rust `Allocator` lets an object's backing memory survive a `systemctl restart`, as an alternative to his own prior practice of serializing state to Redis or a temp file on restart | quote: "We are going to stitch three things together to make Rust objects that survive program restart." | practiced_evidence: none (post's own worked example, not a maintained crate)
- voice: Graham King | position: repr-c-required | date: 2024-01-17 | locator: § "Here's an arbitrary object we will use throught the post" | paraphrase: `#[repr(C)]` is needed to keep the in-memory layout stable across binary versions, since default Rust layout carries no such guarantee | quote: "The repr(C) ensures that the in-memory layout (representation) of this object doesn't change between versions of our binary. Rust makes no promises on memory layout unless you request a specific representation." | practiced_evidence: none

### Nothing new
(none)

---

## f005872 — Rust needs a web framework for lazy developers (2024-10-02, en)

### Questions
- Q: Should the Rust web ecosystem offer a monolithic, batteries-included framework (Django/Rails-style: routing, templates, auth, ORM, admin, hot reload) rather than the current "wire minimalist libraries yourself" norm (actix-web, axum, Leptos, Yew, Dioxus)?
  concepts: web framework scope, actix-web, axum, Leptos, Yew, Dioxus, "wire it up yourself"; domains_live: web; positions_seen: needs-batteries-included-framework (Nicole Tietz-Sokolskaya)

### Claims
- voice: Nicole Tietz-Sokolskaya | position: needs-batteries-included-framework | date: 2024-10-02 | locator: § "Imagining the future I want" | paraphrase: existing minimalist frameworks (actix-web, axum) and SPA frameworks (Yew, Leptos, Dioxus) each require substantial manual wiring (routing, templates, auth, DB, admin, etc.); the ecosystem needs one integrated toolkit instead, which she is starting to build ("newt") | quote: "I'd much rather have a single web framework that handles it all, with clean upgrade instructions between versions." | practiced_evidence: none (newt repo mentioned but "really not usable" / unpublished at time of writing)

### Nothing new
(none)

---

## f005948 — Lambda on hard mode: Inside Modal's web infrastructure (2024-03-20, en)

### Questions
- Q: For a high-throughput HTTP/WebSocket ingress layer with heavy edge-case and failure-mode handling, does Rust's ownership model and pattern matching justify its complexity over a simpler implementation language?
  concepts: ownership, pattern matching, hyper, tokio, ASGI-over-protobuf; domains_live: cloud-workers;distributed; positions_seen: worth-it-for-edge-case-heavy-infra (Eric Zhang / Modal)

### Claims
- voice: Eric Zhang | position: worth-it-for-edge-case-heavy-infra | date: 2024-03-20 | locator: § "Edge cases and errors" / opening | paraphrase: HTTP has many edge cases and Modal's ingress needs to handle malformed/out-of-order events from possibly-malicious clients; Rust's ownership and pattern matching were chosen specifically to manage that casework, and switching from a prior Python-based ingress to this Rust one cut 502 errors by 99.7% | quote: "Rust's pattern matching and ownership help with managing the casework." | practiced_evidence: none (internal service, not public)

### Nothing new
(none)

---

## f005964 — Rustls Server-Side Performance (2025-05-14, en)

### Questions
- Q: Should legacy C-based TLS stacks (OpenSSL) be replaced by memory-safe Rust implementations (Rustls), now that Rustls claims server-side performance parity or better?
  concepts: Rustls, OpenSSL, BoringSSL, TLS handshake latency, memory safety; domains_live: web;core; positions_seen: replace-c-tls-with-rust (Dirkjan Ochtman)

### Claims
- voice: Dirkjan Ochtman | position: replace-c-tls-with-rust | date: 2025-05-14 | locator: § "What is Rustls?" / "Conclusion" | paraphrase: OpenSSL and its derivatives have a long history of memory-safety vulnerabilities; Rustls now shows roughly 2x lower handshake latency than OpenSSL in their benchmarks, so the field should move off C-based TLS | quote: "It's time for the Internet to move away from C-based TLS." | practiced_evidence: https://github.com/rustls/rustls (named, URL not given in text)

### Nothing new
(none)

---

## f007042 — I am co-authoring a book about Rust and Lambda (2024-12-16, en)

### Questions
- Q: Is Rust worth its steeper learning curve for AWS Lambda/serverless functions, compared to interpreted languages (Python, JavaScript)?
  concepts: cold start latency, AWS Lambda, Cargo Lambda, Option/Result vs null; domains_live: cloud-workers; positions_seen: worth-it-for-lambda (Luciano Mammino)

### Claims
- voice: Luciano Mammino | position: worth-it-for-lambda | date: 2024-12-16 | locator: § "Why Rust and Lambda?" | paraphrase: Rust's compiled binaries lower both memory-cost and execution-time dimensions of Lambda's billing formula versus JS/Python, and its lack of null / explicit Option-Result handling catches edge cases earlier; observed cold starts of 10-60ms, roughly 10-20x faster than JS/Python | quote: "With Rust, in most circumstances, you can lower both dimensions, compared to interpreted languages such as JavaScript and Python." | practiced_evidence: https://github.com (Cargo Lambda, named, URL not given in text)

### Nothing new
(none)

---

## f007125 — Rust HashMap notes (2025-03-30, en)

### Nothing new
`nothing new`: raw research notes on hashbrown's SwissTable-derived internals (control bytes, probing, growth); purely descriptive of an existing design with no stated disagreement or practitioner decision point.

---

## f007207 — What Features Should Rust Have? Part II (2025-07-21, en)

### Questions
- Q: Should Rust add "fields in traits" (a shared field, accessed through a vtable offset on `dyn Trait`, that every implementor must provide)?
  concepts: fields in traits, associated types, dyn trait objects, vtable; domains_live: core; positions_seen: mildly-supportive-uncertain-use-case (Jimmy Hartzell)
- Q: Should Rust support "properties" (field-access syntax that silently compiles to a getter/setter method call, as in Python/C#/Swift)?
  concepts: properties, Deref, implicit method calls, field access; domains_live: core; positions_seen: reject-properties (Jimmy Hartzell)
- Q: Should Rust's borrow checker be extended to natively support safe self-referential structs, instead of requiring `unsafe`/`Pin`/crates like `ouroboros`?
  concepts: self-referential structs, Pin, borrow checker, async state machines; domains_live: core; positions_seen: extend-borrow-checker (Jimmy Hartzell)

### Claims
- voice: Jimmy Hartzell | position: mildly-supportive-uncertain-use-case | date: 2025-07-21 | locator: § "Merits of the Proposal" | paraphrase: fields-in-traits is a limited, distinct-enough feature that wouldn't harm Rust's design, but he doesn't personally have a compelling use case for it | quote: "my conclusion comes out to a shrug. This feature doesn't seem bad in any way... But I personally don't engage with a use case for it." | practiced_evidence: none
- voice: Jimmy Hartzell | position: reject-properties | date: 2025-07-21 | locator: § "Limitations of the Proposal" | paraphrase: field access should stay visibly cheap and side-effect-free; hiding a method call behind `foo.x` syntax is undesirable, especially in a systems language | quote: "it should be clear that it's doing a field access (cheap and with few potential unseen consequences) rather than a method call (which could do anything including crash, or block your thread on a network request)." | practiced_evidence: none
- voice: Jimmy Hartzell | position: extend-borrow-checker | date: 2025-07-21 | locator: § "Self-Referential Structs: Absolutely." | paraphrase: a subset of self-referential structs (borrowing only from a heap allocation owned by a sibling field, without mutating it) could be proven safe by a smarter borrow checker without needing `Pin`; he wants this more than fields-in-traits because he hits the need for it regularly | quote: "Self-Referential Structs: Absolutely... I think it'll be the type of feature where we'll wonder how we ever lived without it." | practiced_evidence: none (ouroboros crate cited as the current workaround, not his own)

### Nothing new
(none)
