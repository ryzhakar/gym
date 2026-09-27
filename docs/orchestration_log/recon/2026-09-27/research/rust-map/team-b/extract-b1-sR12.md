For each source: what must a Rust practitioner decide, and where do the sources conflict on it?

## f005085 — perf(flex): optimize views, copies, in-place ops, and Rayon parallelism (2026-09-08, English)

### Questions
- Q: Should a safety/dense-storage invariant that several call sites rely on be duplicated inline as ad hoc boolean expressions, or encapsulated as one named method on the owning type that states the contract?
  concepts: encapsulation, invariants, unsafe, maintainability; domains_live: ml, core; positions_seen: encapsulate-as-named-method
- Q: When several hand-written data structures are near-duplicate specializations differing only by array length/arity (e.g. a 2-stride vs. 3-stride zip), should they be unified into one type parameterized by a const generic, or kept as separate hand-specialized versions?
  concepts: const generics, monomorphization, code duplication; domains_live: ml, core; positions_seen: unify-via-const-generics

### Claims
- voice: antimora (Tracel AI / burn maintainer) | position: encapsulate-as-named-method | date: 2026-09-08 | locator: PR review comment, 2026-09-08T21:11:40Z | paraphrase: the same dense/non-broadcast check is duplicated verbatim at two call sites gating `storage_mut()`, so drift between them would silently produce a bad write instead of a compile error; it should be a single method on `Layout` that documents the actual contract | quote: "This is duplicated verbatim at `ops/gather_scatter.rs:18`. Both copies gate `storage_mut()`, so a drift between them is a bad write rather than a compile error... Reads better as a single method on `Layout` carrying the actual contract." | practiced_evidence: none
- voice: antimora (Tracel AI / burn maintainer) | position: unify-via-const-generics | date: 2026-09-08 | locator: PR review comment, 2026-09-08T21:11:40Z | paraphrase: `Zip3Nest` is `ZipNest` with a third stride array threaded through, and the two have already drifted from each other inside this same PR; a `Nest<const N: usize>` would cover both with identical codegen since it monomorphizes | quote: "Stepping back, `Zip3Nest` is `ZipNest` with a third stride array threaded through every line, and the two have already drifted inside this PR... A `Nest<const N: usize>` would cover both, and `CollapsedLayout` at N=1, with identical codegen since it monomorphizes. Not blocking, but the drift is already real rather than hypothetical." | practiced_evidence: none

### Nothing new

## f005120 — tokenizers v1: encode, decode and scaling, measured (2026-09-21, English)

### Questions
- Q: Should a library ship as one crate with feature flags gating optional subsets, or be split into a workspace of smaller crates so consumers link only what they use?
  concepts: workspaces, crate splitting, feature flags, compile/link footprint; domains_live: ml, core; positions_seen: split-into-workspace
- Q: In a hot loop, should working memory be a caller-owned scratch buffer reused across calls, or freshly allocated per call for simplicity?
  concepts: allocation, buffer reuse, hot-path performance; domains_live: ml, core; positions_seen: caller-owned-scratch-buffer

### Claims
- voice: Arthur Zucker / Hugging Face tokenizers team | position: split-into-workspace | date: 2026-09-21 | locator: table row "workspace split" / "Progress Towards V1" | paraphrase: the single tokenizers crate became a workspace so `tk-encode` is the only required runtime piece and `tk-serialize`, `tk-convert`, `tk-train` are linked only when an application actually needs them | quote: "one crate became a workspace: tk-encode is the required runtime, and tk-serialize, tk-convert and tk-train are linked only when an application needs them." | practiced_evidence: https://crates.io/crates/tokenizers (workspace split shipped in the v1 release candidate)
- voice: Arthur Zucker / Hugging Face tokenizers team | position: caller-owned-scratch-buffer | date: 2026-09-21 | locator: section "The Merge Loop" | paraphrase: the previous implementation allocated fresh memory and a new priority queue per pre-token; v1 instead reuses a scratch buffer owned by the caller so the merge loop never touches the allocator | quote: "v1 reuses a scratch buffer owned by the caller, removing those repeated allocations... the merge working set lives in a caller-owned scratch buffer; the loop never touches the allocator." | practiced_evidence: https://crates.io/crates/tokenizers

### Nothing new

## f005169 — Callgraph analysis: Writing custom lints for fun and profit (2026-04-08 / published 2026-04-01, English)

### Questions
- Q: How should a Rust project statically verify a property like "this function never panics" or "this function never calls unvalidated code" across a codebase: clippy lints, a new effect-type system, a link-time hack, a cfg-forked standard library, or a custom compiler driver?
  concepts: static verification, panics, effect systems, monomorphization, custom lints, safety-critical certification; domains_live: embedded, core; positions_seen: custom-compiler-driver-post-mono

### Claims
- voice: Jynn (Ferrous Systems, Ferrocene team) | position: custom-compiler-driver-post-mono | date: 2026-04-08 | locator: section "What have we learned?" (whole post walks the alternatives it rejects: clippy lints, effect-type systems, link-time no_panic hack, cfg-forked std) | paraphrase: for certifying that validated `core` functions only call other validated functions (generalizable to "never panics"), clippy lints don't recurse into dependencies and only cover hard-coded library types; an effect-type system would require a new language; a link-time hack is optimization-dependent, has no async support, breaks under `panic = "abort"`/no_std, and is unsafe to use in library crates; cfg-forking the standard library affects every consumer and breaks tooling. A custom rustc driver with a post-monomorphization MIR pass was the most accurate approach and is what Ferrocene now ships and certifies against | quote: "For Ferrocene, the most accurate approach was to write a custom rustc driver which uses a post-monomorphization pass to detect all resolved function calls." | practiced_evidence: Ferrocene 26.05 (in production certification use, per the post)

### Nothing new

## f005201 — lapce (2023-12-28, English)

### Nothing new
`nothing new` — a project README (features, install, contributing, license); no Voice states a position on any contested Rust-practitioner decision.

## f005312 — vaultwarden (2024-08-14, English)

### Nothing new
`nothing new` — a project README (features, deployment, disclaimer); no Voice states a position on any contested Rust-practitioner decision.

## f005314 — spring-rs / summer-rs (2024-08-17, English)

### Nothing new
`nothing new` — a project README describing a Spring-Boot-inspired framework's features and plugin catalog; no Voice argues for its design choices against an alternative.

## f005421 — rhai (2025-01-17, English)

### Questions
- Q: Should a library ever panic on invalid input, or should it always signal failure through Result/Option instead? (same disagreement first logged in extract-b1-sR10.md, f005085/burn: antimora's "panic-is-fine-if-documented" and softmaximalist's "prevent-via-explicit-check")
  concepts: panics, error handling, library design guarantees; domains_live: core, embedded; positions_seen: never-panic (this source), panic-is-fine-if-documented (burn, prior batch), prevent-via-explicit-check (burn, prior batch)

### Claims
- voice: Rhai project (rhaiscript maintainers) | position: never-panic | date: 2025-01-17 | locator: README section "Protected against attacks", sub-item "_Don't Panic_ guarantee" | paraphrase: Rhai treats any panic reaching the host application as a bug in Rhai itself, not an acceptable outcome, and is coded under that guarantee | quote: "_Don't Panic_ guarantee - Any panic is a bug. Rhai subscribes to the motto that a library should never panic the host system, and is coded with this in mind." | practiced_evidence: https://github.com/rhaiscript/rhai (README states it "Passes Miri")

### Nothing new

## f005440 — Rust memory management explained (2025-02-12, English)

### Nothing new
`nothing new` — a tutorial explainer of ownership, scope, RAII, Box/Rc/Arc/RefCell aimed at newcomers; it restates settled, undisputed language mechanics rather than a point where practitioners disagree, and its author (a technology journalist covering many languages) is not a Voice with a Rust track record.

## f005504 — helix-db (2025-05-13, English)

### Nothing new
`nothing new` — a product README (SDK usage across four languages, cloud setup); no Voice argues for a Rust design choice against an alternative.

## f005668 — Swift is a more convenient Rust (2026-01-31, English)

### Questions
- Q: Should a language's memory-model default favor explicitness/performance (opt into convenience, as Rust's move/borrow-by-default with Cow/Rc as opt-in) or convenience (opt into performance, as Swift's copy-on-write-by-default with ownership as opt-in)?
  concepts: ownership, borrowing, Cow, defaults, ergonomics vs. performance; domains_live: swift-interop, core; positions_seen: domain-dependent-tradeoff
- Q: Should indirection for a recursive data type be explicit (the programmer writes `Box<T>`) or implicit (a compiler-inferred/annotated indirection, as Swift's `indirect` keyword)?
  concepts: recursive types, Box, indirection, enums; domains_live: swift-interop, core; positions_seen: explicit-favorably-framed

### Claims
- voice: nmn (nmn.sh blog author) | position: domain-dependent-tradeoff | date: 2026-01-31 | locator: section "Convenience has its costs" | paraphrase: neither default is simply better; Rust's performance-first default suits systems, embedded, compilers and browser engines, Swift's convenience-first default suits UI, servers and parts of compilers/operating systems, and the author expects the overlap between the two to grow over time | quote: "I would say both languages have their uses. Rust is better for systems and embedded programming... Swift is better for writing UI and servers and some parts of compilers and operating systems. Over time I expect to see the overlap get bigger." | practiced_evidence: none
- voice: nmn (nmn.sh blog author) | position: explicit-favorably-framed | date: 2026-01-31 | locator: section "Rust's compiler catches problems. Swift's compiler solves some of them" | paraphrase: contrasting Rust's `Box<TreeNode<T>>` for a recursive enum with Swift's `indirect` keyword, the author frames Rust's requirement to write the indirection explicitly as forcing the programmer to confront the problem directly, versus Swift handling it more automatically | quote: "This makes the problem explicit and forces you to deal with it directly, Swift is a little more, automatic." | practiced_evidence: none

### Nothing new

## f005802 — Andreas Thom Mastodon thread on OpenAI and unpublished mathematics (2026-09-10, English)

### Nothing new
`nothing new` — the thread concerns trust in OpenAI's handling of unpublished mathematical research (the Buckmaster–Alpöge blow-up results) and has no Rust content of any kind.

## f007125 — Rust HashMap notes (2025-03-30, English)

### Nothing new
`nothing new` — the author's own research notes explaining hashbrown/SwissTable's existing, settled internal design (control bytes, SIMD probing, growth factors); no Voice argues for this design against a live alternative, it is description of what already shipped.
