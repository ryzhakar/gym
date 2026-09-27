## f002643 — How to Build GitHub Copilot Extensions (2025-02-06, English)

### Questions

None.

### Claims

None.

### Nothing new

`nothing new` — a Python/FastAPI tutorial (by Layer) for wiring a GitHub Copilot extension via webhook subscription; no Rust content or Rust voice appears anywhere in it.

## f002685 — javascript event loop becomes extremely slow in wayland (2025-02-18, English)

### Questions

- Q: When an external caller drives a Rust windowing event loop via `pump_events` with a timeout, should any non-negative `Some(duration)` timeout force `ControlFlow::Poll`, or only a zero-duration timeout?
  concepts: event loop control flow, windowing, async/external-loop integration; domains_live: desktop-cli-ui; positions_seen: any-Some-duration forces Poll (sigmaSd); only-Zero forces Poll (tronical)

### Claims

- voice: sigmaSd | position: any `Some(duration)` timeout passed to `pump_events` should force `ControlFlow::Poll` | date: 2025-02-20 | locator: GitHub issue comment, 2025-02-20T10:24 | paraphrase: proposed broadening the workaround so that every non-nil duration, not just zero, forces Poll | quote: "any duration as long that its Some, should make the controlflow Poll" | practiced_evidence: none (proposal only, not merged)

- voice: tronical (Olivier Goffart, Slint co-founder/maintainer) | position: special-case only `Duration::ZERO` to force `ControlFlow::Poll`; leave other durations to winit's own handling | date: 2025-02-20 | locator: GitHub issue comment, 2025-02-20T13:08 | paraphrase: reconsidered the broader fix and narrowed the workaround to only the zero-duration case, reasoning it doesn't make sense to return `Wait` when a nonzero duration like `Some(2s)` was explicitly requested — that should be winit's own responsibility to handle correctly | quote: "I'll do this workaround only for `Zero`... I'll leave it to the winit implementation to handle that correctly" | practiced_evidence: https://github.com/slint-ui/slint (Slint's winit backend, where the narrower fix landed per the thread)

## f002883 — Workaround for a TextDecoder bug in Safari causing a RangeError to be thrown (2025-04-06, English)

### Questions

None.

### Claims

None.

### Nothing new

`nothing new` — a one-off empirical safety-margin choice (1MiB buffer before Safari's `TextDecoder` throws `RangeError` past 2GiB); the maintainers' back-and-forth is about pinning down this bug's exact byte threshold, not a recurring or generalizable Rust practice disagreement.

## f003033 — Running WebAssembly (Wasm) Components From the Command Line (2025-05-21, English)

### Questions

- Q: When defining a Wasm component's WIT world, should a function be exported directly from the world, or wrapped inside a named interface that the world then exports?
  concepts: WIT, Wasm Component Model, API design; domains_live: wasm; positions_seen: prefer wrapping in a named interface

### Claims

- voice: Tim McCallum (Bytecode Alliance) | position: wrap related functions inside a named interface and export the interface, rather than exporting a raw function from the world | date: 2025-05-21 | locator: "WIT" section | paraphrase: while a world can export a bare function directly, doing so isn't the recommended approach; wrapping functions in an interface is more modular, extensible, and matches how WIT is used in real multi-function components | quote: "the recommended best practice is to wrap related functions inside an interface, which you then export from your world" | practiced_evidence: none cited beyond the article's own worked example

## f003082 — Add initial porting of table_ops from arbitrary to mutatis (2025-06-04, English)

### Questions

- Q: When a repeated Rust code pattern could be generated either by a declarative macro or by a plain function/derive, which should be preferred?
  concepts: macros vs. functions, code generation, API ergonomics; domains_live: core; wasm; positions_seen: prefer function/derive over a macro absent a real codegen need

### Claims

- voice: fitzgen (Bytecode Alliance / Wasmtime core, `arbitrary` crate author) | position: prefer a plain function (or a derived `Default`) over a declarative macro when the macro isn't doing real code generation | date: 2025-06-12 | locator: PR #10924 review comments | paraphrase: reviewing a macro used to produce a fixed empty-value sequence, argued it should just be `TableOps::default()` derived on the type, and that if the sequence were needed in several places it should be a function rather than a macro | quote: "if we did want to create this particular sequence in a bunch of places we should just use a function rather than a macro" | practiced_evidence: https://github.com/bytecodealliance/wasmtime/pull/10924 (change applied in the reviewed PR)

## f003238 — How GoodData turbocharged AI analytics with Qdrant (2025-07-09, English)

### Questions

None.

### Claims

None.

### Nothing new

`nothing new` — a customer case study on GoodData's RAG/analytics stack built on Qdrant; entirely business/product outcomes (latency numbers, deployment story), no Rust design content.

## f003266 — Is this a bug in automatic reference counting? (2025-07-17, English)

### Questions

None.

### Claims

None.

### Nothing new

`nothing new` — the whole thread is a Swift ARC/`consume`/ownership debugging discussion (theundergroundsorcerer, jrose, John_McCall, et al.); Rust is invoked once, by John_McCall, as settled fact ("If Swift always consumed in these situations, as Rust does...") to explain why Swift's `consuming` parameters still copy by default — a contrast point for a Swift design choice, not a live Rust disagreement or a Rust voice's Position.

## f003375 — Tutorial: Message Framing with iroh (2025-08-12, English)

### Questions

None.

### Claims

None.

### Nothing new

`nothing new` — a neutral iroh/QUIC tutorial on manual length-prefixed message framing (`write_u8`/`read_exact`); it names an alternative technique (varints) without arguing for either, and defers its own serialization preference to a separate linked example rather than stating a position here.

## f003389 — Neon's Microsoft Azure Native Integration is Generally Available (2025-08-14, English)

### Questions

None.

### Claims

None.

### Nothing new

`nothing new` — a product/partnership announcement about Neon's Azure Marketplace GA; no Rust content.

## f003580 — R2 SQL: a deep dive into our new distributed query engine (2025-09-25, English)

### Questions

- Q: Should a Rust vectorized query engine process rows fully sequentially in large batches (cache-friendly, low interpretation overhead), fully in parallel per-row, or partition data into parallel batched streams?
  concepts: vectorized execution, query engine architecture, partitioning; domains_live: distributed; core; positions_seen: hybrid partition-based batching (DataFusion's model, endorsed by Cloudflare's R2 SQL team)

### Claims

- voice: Yevgen Safronov, Nikita Lapkov, Jérôme Schneider (Cloudflare, R2 SQL) | position: partition-based batch execution (vectorized batches within a partition, parallelized across partitions) captures the benefits of both fully-sequential and fully-parallel row processing | date: 2025-09-25 | locator: "Apache DataFusion" section | paraphrase: contrasted a fully-sequential "tight loop" (cache-friendly, low interpretation overhead) against fully-parallel per-row processing (better core utilization), and endorsed DataFusion's partition model as achieving both at once | quote: "DataFusion's architecture allows us to achieve a balance on this scale, reaping benefits from both ends." | practiced_evidence: R2 SQL, Cloudflare's production distributed query engine described in the post, built on DataFusion

## f003594 — AI: Agent & tools just stop working no matter the model/provider (2025-09-27, English)

### Questions

None.

### Claims

None.

### Nothing new

`nothing new` — a long bug-report thread about Zed's AI agent panel silently stalling across LLM providers (Mistral, OpenRouter, llama.cpp, Copilot); entirely about agent/tool-calling integration bugs, no Rust language content even though Zed itself is written in Rust.
