## f001096 — Metal: Improved reduce and softmax (2024-03-08, en)

### Questions
- Q: Should numeric reductions in a Rust ML kernel (e.g. softmax) accumulate in a higher-precision type than the input/output dtype?
  concepts: numeric precision, reduction kernels, GPU kernels; domains_live: ml; positions_seen: accumulate-in-float-for-precision
- Q: When a function moves to a different crate in a multi-crate Rust workspace, should its benchmark move with it, using `git mv` to preserve file history?
  concepts: workspace/crate organization, benchmarks, git history; domains_live: ml, core; positions_seen: colocate-benchmark-with-owning-crate

### Claims
- voice: ivarflakstad | position: accumulate-in-float-for-precision | date: 2025-01-13 | locator: comment "Should probably accumulate with float in softmax to preserve precision. Shouldn't affect performance at all." | paraphrase: numeric reductions should accumulate in float32 even when the surrounding tensors are lower precision, to avoid precision loss, at negligible performance cost | quote: "Should probably accumulate with float in softmax to preserve precision." | practiced_evidence: https://github.com/huggingface/candle/pull/1819 (merged)
- voice: LaurentMazare | position: colocate-benchmark-with-owning-crate | date: 2025-01-13 | locator: comment "I think moving the benchmark to `candle-nn` would be good, (do it with `git mv` so as to preserve history)." | paraphrase: a benchmark should live in the crate that defines the function it measures; use `git mv` on relocation to preserve file history | quote: "I think moving the benchmark to `candle-nn` would be good, (do it with `git mv` so as to preserve history)." | practiced_evidence: https://github.com/huggingface/candle/pull/1819 (merged)

## f001244 — Next.js authentication using Clerk, Drizzle ORM, and Neon (2024-04-02, en)

### Nothing new
nothing new — the article is a Next.js/TypeScript/Postgres tutorial with no Rust content and no Voice with a Rust track record.

## f001271 — Qdrant Hybrid Cloud and Haystack for Enterprise RAG (2024-04-10, en)

### Nothing new
nothing new — marketing copy for a product integration; the one quote (deepset's Developer Relations Lead) is promotional, not a declared Position on any Rust practitioner decision.

## f001319 — Iroh 0.14.0 - Dial the world (2024-04-18, en)

### Nothing new
nothing new — a changelog announcing features and a cancel-safety bug fix; it narrates what shipped rather than declaring a Position on a contested decision, and the only candidate evidence (the `ProtocolHandler` trait returning a boxed future) is code alone, which the evidence rules exclude as a Claim.

## f001531 — How to create previews with anonymized production-like data in seconds (2024-05-28, en)

### Nothing new
nothing new — Neon/Neosync product marketing with no Rust content and no named Voice with a Rust track record.

## f001578 — Add an interface to your Neon database via Outerbase (2024-06-07, en)

### Nothing new
nothing new — Neon/Outerbase product marketing with no Rust content and no named Voice with a Rust track record.

## f001650 — iroh 0.19.0 - Make it your own (2024-06-27, en)

### Nothing new
nothing new — a changelog listing new APIs and breaking renames without argued reasoning; the type-parameter removals and API changes are code/API alone, which the evidence rules exclude as a Claim absent a declared reason.

## f001677 — [Proposal] Set literals (2024-07-04, en)

### Nothing new
nothing new — a Swift Evolution forum thread debating Swift-language set-literal syntax; Rust is named once only as an aside about brace omission and no Rust practitioner or Rust decision is discussed.
