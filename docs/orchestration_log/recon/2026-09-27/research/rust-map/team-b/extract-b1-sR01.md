## f000233 — Asynchronous Programming in Rust (unknown (living document), en)
### Questions
- Q: When should a Rust practitioner reach for async instead of threads?
  concepts: async runtimes, threads, concurrency, cancellation; domains_live: embedded, web, distributed, other; positions_seen: async-for-io-wait-and-no-os
- Q: Is async Rust production-ready today given its known gaps?
  concepts: async runtimes, async traits, streams, async destructors; domains_live: core; positions_seen: reliable-despite-rough-edges
### Claims
- voice: Rust Async Book (async-book, rust-lang.github.io) | position: async-for-io-wait-and-no-os | date: undated (living document; no revision date on page) | locator: § "What is Async Programming and why would you do it?", paragraph 2 | paraphrase: async fits systems handling many concurrent tasks that spend most of their time waiting (e.g. client responses, IO), and also fits microcontrollers with very limited memory and no OS-provided threads. | quote: "This makes async programming a good fit for systems which need to handle very many concurrent tasks and where those tasks spend a lot of time waiting" | practiced_evidence: none
- voice: Rust Async Book (async-book, rust-lang.github.io) | position: reliable-despite-rough-edges | date: undated (living document) | locator: § "Development of Async Rust", paragraph 1 | paraphrase: stable async is reliable and performant and used in production at large tech companies, though ergonomics (not reliability) are rough around async iterators/streams, async in traits, and async destruction. | quote: "Async Rust ... is reliable and performant. It is used in production in some of the most demanding situations at the largest tech companies." | practiced_evidence: none

## f000256 — Rust and WebAssembly (unknown (living document), en)
### Questions
- Q: Why (if at all) should Rust be chosen over JavaScript as a WebAssembly compile target?
  concepts: WebAssembly, garbage collection/runtime overhead, JS interop, binary size; domains_live: wasm, frontend, web; positions_seen: rust-for-perf-and-size-and-no-rewrite
### Claims
- voice: Rust and WebAssembly Book (rustwasm.github.io, unmaintained) | position: rust-for-perf-and-size-and-no-rewrite | date: undated (living document) | locator: chapter "Why Rust and WebAssembly?" § "Low-Level Control with High-Level Ergonomics" | paraphrase: JS's dynamic typing and GC pauses make Web performance unreliable; Rust gives low-level control without that non-determinism, ships no runtime so .wasm stays small, and lets teams port only hot-path JS functions rather than rewrite everything. | quote: "Rust gives programmers low-level control and reliable performance." | practiced_evidence: none

Note: the bundled text for this source was the book's landing page/TOC only (front matter, no prose on the actual question) — visibly cut for a source that should be long. Refetched the chapter "Why Rust and WebAssembly?" directly to check for contested content; found the above.

## f000267 — Zebra (unknown (living document), en)
### Nothing new
`nothing new` — the page is install/build/CI documentation for one specific node implementation (Docker vs manual build, GCC-15 workaround, dual MIT/Apache-2.0 licensing stated as fact); it presents no argued position on a question Rust practitioners decide differently, only operational instructions.

## f000464 — Quantized Implementations are slow (2023-10-06 → 2024-03-02, en)
### Questions
- Q: Does quantization reliably speed up inference in candle, or only for some model architectures?
  concepts: quantization, memory-bound vs compute-bound kernels, matmul backends, Apple Accelerate; domains_live: ml; positions_seen: quantization-helps-memory-bound-only
- Q: Should GPU (Metal) backend work be prioritized ahead of further CPU/quantization optimization in candle?
  concepts: GPU backends, roadmap prioritization; domains_live: ml; positions_seen: prioritize-metal-next
### Claims
- voice: LaurentMazare | position: quantization-helps-memory-bound-only | date: 2023-10-08 | locator: issue comment, 2023-10-08T11:39:13Z | paraphrase: T5's cross-attention involves much larger matmuls than llama/mistral, making it compute- rather than memory-bound on M1/M2; quantization's usual speedup comes from being memory-bound, so it's hard to beat Apple Accelerate (possibly Neural-Engine-backed) here even after tuning min/max-len parameters. | quote: "my guess would be that it's much less memory bound in this case and in this case it's pretty hard to outperform the work done by apple on accelerate" | practiced_evidence: https://github.com/huggingface/candle (candle-core/src/quantized/k_quants.rs, cited directly in thread)
- voice: LaurentMazare | position: prioritize-metal-next | date: 2023-10-06 | locator: issue comment, 2023-10-06T09:20:02Z | paraphrase: Metal/GPU support is the top engineering priority for candle's next major push, ahead of further quantized-CPU work. | quote: "Metal support is at the top of the priority list for the next large thing" | practiced_evidence: none
