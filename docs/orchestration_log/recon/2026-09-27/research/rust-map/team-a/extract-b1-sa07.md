## f003594 — AI: Agent & tools just stop working no matter the model/provider (2025-09-27, en)
### Nothing new
`nothing new`: bug-report thread on Zed's agent panel stalling across Mistral, Copilot, OpenRouter, llama.cpp providers; no Rust language or practice disagreement raised.

## f003702 — Hashing multiple blobs with BLAKE3 (2025-10-15, en)
### Nothing new
`nothing new`: solo benchmarking walkthrough by Rüdiger Klaehn (n0/iroh) reaching into BLAKE3's internal `Platform::hash_many` API; no opposing position or contested framing present in the source itself.

## f003704 — ONNX-IR Refactor - Op/Node-Centric Architecture (2025-10-16, en)
### Questions
- Q: Should a processing pipeline use runtime type erasure with up/down-casting, or a compile-time associated type on the processing trait?
  concepts: traits, associated-types, type-erasure, dynamic-dispatch; domains_live: ml, core; positions_seen: type-erasure-with-casting (status quo), associated-type-on-trait (laggui, proposed)
- Q: Should a bounded, safety-first multi-pass graph algorithm favor a simple iterative fixed-point loop, or a more complex event-driven re-trigger design?
  concepts: graph-traversal, iterative-convergence, complexity-vs-performance; domains_live: ml, core; positions_seen: simple-iterative-bounded (antimora, held and shipped), event-driven-retrigger (antimora, considered and rejected)
- Q: Should a fixed, closed set of graph node kinds be represented as an enum, or via trait objects/dynamic dispatch?
  concepts: enums, sum-types, trait-objects, extensibility; domains_live: ml, core; positions_seen: enum-of-nodes (antimora, adopted after offline discussion)
- Q: Should a struct under construction hold a lifetime-bound reference into shared mutable build state, or should construction use a builder consumed into an immutable owned structure?
  concepts: lifetimes, builder-pattern, ownership; domains_live: ml, core; positions_seen: builder-consume-to-immutable (laggui, proposed)
### Claims
- voice: laggui | position: associated-type-on-trait | date: 2025-11-03 | locator: PR #3872, comment 2025-11-03T20:43:16Z | paraphrase: proposes replacing the NodeConfig trait's runtime type erasure and up/down-casting with an associated config type on NodeProcessor | quote: "This would remove the need for `NodeConfig` trait entirely." | practiced_evidence: none
- voice: antimora | position: simple-iterative-bounded | date: 2025-11-07 | locator: PR #3872, comment 2025-11-07T17:03:28Z | paraphrase: kept the iterative type-inference loop (bounded to 10 passes, down from 100) over a more efficient graph-retrigger design because the iterative approach was safer and bug-free | quote: "this iterative approached was the safest and bug free compared to graph re-trigger approach, which would have been more efficient but it was complex" | practiced_evidence: https://github.com/tracel-ai/burn/pull/3872
- voice: antimora | position: enum-of-nodes | date: 2025-11-07 | locator: PR #3872, comment 2025-11-07T15:47:01Z | paraphrase: agreed, after offline discussion, to redo the Graph representation as node enums | quote: "We will redo as a graph of node enums" | practiced_evidence: https://github.com/tracel-ai/burn/issues/3988
- voice: laggui | position: builder-consume-to-immutable | date: 2025-11-03 | locator: PR #3872, comment 2025-11-03T20:17:51Z | paraphrase: calls the current reliance on `_graph_data` a lifetime hack and proposes a builder that consumes GraphState into an immutable OnnxGraph so Argument can reference the tensor store directly | quote: "The reliance on `_graph_data` here feels like a lifetime hack." | practiced_evidence: none

## f003716 — API for traversing `Relationship`s and `RelationshipTarget`s in dynamic contexts (2025-10-19, en)
### Questions
- Q: When a trait's correct implementation is required for memory safety, should the trait itself be marked `unsafe`, or should the unsafe boundary sit on the consuming method instead?
  concepts: unsafe, soundness, trait-safety-contracts; domains_live: core; positions_seen: unsafe-consuming-fn (eugineerd, shipped design; urben1680, agreed), unsafe-trait (eugineerd, raised as an alternative)
- Q: Should a value that can be one of two related-but-distinct kinds be modeled as one enum with variant matching, or split into two separate types?
  concepts: enums, sum-types, api-ergonomics; domains_live: core; positions_seen: split-into-two-structs (cBournhonesque, proposed), single-enum (status quo)
### Claims
- voice: eugineerd | position: unsafe-consuming-fn | date: 2025-10-20 | locator: PR #21601, comment 2025-10-20T17:20:03Z | paraphrase: says correctness must be enforced either by marking the Relationship trait unsafe or by leaving RelationshipAccessor::relationship unsafe since the implementer can't be trusted; the shipped design leaves the accessor method unsafe rather than the trait | quote: "either mark `Relationship` trait unsafe and mention that `ENTITY_FIELD_OFFSET` must be correct to be safely implemented, or we'd have to leave `RelationshipAccessor::relationship` unsafe" | practiced_evidence: https://github.com/bevyengine/bevy/pull/21601
- voice: urben1680 | position: unsafe-consuming-fn | date: 2025-10-20 | locator: PR #21601, comment 2025-10-20T17:52:07Z | paraphrase: accepts the design where the derive macro is trusted to build a valid accessor and the unsafe contract lands on the caller/consuming method rather than the trait | quote: "Then I agree on the design here." | practiced_evidence: none
- voice: cBournhonesque | position: split-into-two-structs | date: 2025-10-23 | locator: PR #21601, comment 2025-10-23T14:14:41Z | paraphrase: found the enum-based accessor confusing when traversing relations dynamically and suggests splitting it into two separate structs plus friendlier wrapper methods | quote: "I think it might be better to split it into 2 separate structs?" | practiced_evidence: none

## f003922 — Build MCP Servers with Wasmcp and Spin (2025-11-25, en)
### Questions
- Q: Should agent tool implementations couple to a specific language's SDK and calling runtime, or be built as portable WebAssembly components composed independently of language and runtime?
  concepts: wasm-components, wasi, composability, mcp; domains_live: wasm, cloud-workers, distributed; positions_seen: wasm-component-composition (Ian McDonald / wasmcp)
### Claims
- voice: Ian McDonald | position: wasm-component-composition | date: 2025-11-25 | locator: blog post, § "Wasmcp" | paraphrase: argues that SDK-based tool calling couples tool instances to the calling application's runtime and can't be reused externally, and that composing independently-built WebAssembly components (regardless of source language) solves discovery, portability and sandboxing better | quote: "Tool calling implemented by an AI SDK couples tool instances to an application's runtime... We need a layer of indirection between models and their tools." | practiced_evidence: https://github.com/wasmcp/wasmcp
