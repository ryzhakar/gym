## f002466 — Winch: implement fpu to int conversions for aarch64 (2024-12-21, en)

### Questions
- Q: When a temporary/scratch register must cross a function boundary, should its safe use be enforced by the type system (dedicated types, exclusive access), or left to convention and reviewer discipline?
  concepts: unsafe, register-allocation, API-design; domains_live: wasm; positions_seen: type-enforced-safety, convention-and-review

### Claims
- voice: saulecabrera | position: type-enforced-safety | date: 2025-01-04 | locator: comment @saulecabrera 2025-01-04T16:38:14Z | paraphrase: proposes relying on the type system to identify/audit scratch-register usage, or exclusive access analogous to allocatable registers, because passing a scratch register as a parameter extends its live range and raises unintentional-clobbering risk | quote: "relying on the type system to identify/audit scratch register usage and/or providing exclusive access to the scratch registers" | practiced_evidence: none

---

## f003025 — Support hotpatching systems (2025-05-19, en)

### Questions
- Q: Should ecosystem build tooling that outgrows Cargo's scope ship as a `cargo` subcommand, or as an independent CLI / cargo-replacement?
  concepts: cargo, build-tooling, ecosystem-fragmentation; domains_live: core, desktop-cli-ui; positions_seen: cargo-subcommand, standalone-or-replacement

- Q: When one project's open-source code is copied, stripped of branding, and rehosted by another developer without prior coordination, is that ordinary open-source practice or a breach of collaborative norms ("bad form")?
  concepts: open-source-governance, licensing, forking, branding; domains_live: core

### Claims
- voice: teohhanhui | position: cargo-subcommand | date: 2025-06-01 | locator: comment @teohhanhui 2025-06-01T09:36:41Z | paraphrase: rejects a standalone "cargo plus plus" tool; ecosystem tools should be `cargo` subcommands | quote: "That's how you kill an ecosystem. It should be a `cargo` subcommand, please." | practiced_evidence: none
- voice: TapGhoul | position: cargo-subcommand | date: 2025-06-01 | locator: comment @TapGhoul 2025-06-01T11:36:46Z | paraphrase: subcommands are functionally identical to standalone binaries plus a few injected env vars, so a rust-ecosystem tool aiming for wide reuse should still register as a subcommand | quote: "I'd argue that a subsecond CLI tool makes a lot of sense as a cargo subcommand, given the general pattern I've seen." | practiced_evidence: none
- voice: jkelleyrtp | position: standalone-or-replacement | date: 2025-06-01 | locator: comment @jkelleyrtp 2025-06-01T09:00:03Z | paraphrase: cargo cannot run/test/bench wasm, iOS or Android projects, so wasm-bindgen and similar high-usage tools are standalone by necessity, and dx follows that pattern since Dioxus is not exclusively a Rust tool | quote: "wasm-bindgen is the most used cli in the rust ecosystem and it is not a subcommand." | practiced_evidence: dx / dioxus-cli
- voice: janhohenheim | position: standalone-or-replacement | date: 2025-06-01 | locator: comment @janhohenheim 2025-06-01T11:49:48Z | paraphrase: cargo's limitations and slow development cycle led Bevy to design its CLI as a cargo wrapper/replacement rather than a subcommand | quote: "The frustrations with cargo's limitations and its glacial development cycle has led this very project to design the Bevy CLI alpha as a cargo replacement / wrapper and not a subcommand." | practiced_evidence: bevy_cli
- voice: BD103 | position: standalone-or-replacement | date: 2025-06-01 | locator: comment @BD103 2025-06-01T19:12:02Z | paraphrase: Bevy-specific needs (asset handling, default index.html for the web feature) don't fit a general-purpose stable tool like Cargo; better to build 3rd-party tools on top of Cargo than have Cargo grow narrow features | quote: "it's less that Cargo is lacking features and more that certain features are too specific to be included in a standard Rust distribution." | practiced_evidence: bevy_cli web feature
- voice: cart | position: branding-and-coordination-matter | date: 2025-06-01 | locator: comment @cart 2025-06-01T22:35:03Z | paraphrase: taking a project's work wholesale and redistributing it without discussing it first is "bad form" even where the license permits it, because banners/brands carry the social and financial capital that sustains maintainers | quote: "If someone were to publish a 'debranded' Bevy Reflect without discussing it with us, I would consider that bad form. Legal according to the license, but bad form nonetheless." | practiced_evidence: none
- voice: hecrj | position: no-entitlement-forking-is-core-of-oss | date: 2025-06-02 | locator: comment @hecrj 2025-06-02T02:49:06Z | paraphrase: producers of open source are not entitled to control over branding or how their code is reused; forking and improving others' code is the essence of open source, not a breach of it | quote: "I don't think 'producers' of open source should be entitled to anything; the same way 'consumers' aren't either. This is the real beauty of open source—a gift with no expectations." | practiced_evidence: iced, cargo-hot (experimental fork of subsecond concepts)
- voice: jkelleyrtp | position: branding-and-coordination-matter | date: 2025-06-02 | locator: comment @jkelleyrtp 2025-06-02T07:00:30Z | paraphrase: copying, stripping, and renaming another team's code, then seeking maintainers for it, without reaching out first, is disrespectful of the original authors' investment even though the license allows it | quote: "Instead of reaching out with an offer to help modularize the subsecond engine, you went straight to copy-pasting our code into a new project, stripping it down, renaming it, and then started shopping around for help to maintain it." | practiced_evidence: dx / subsecond

---

## f003033 — Bytecode Alliance: Running WebAssembly Components From the Command Line (2025-05-21, en)

### Nothing new
`nothing new`: a how-to tutorial on `wasmtime run --invoke`/WAVE syntax; no Voice states a contested position.

---

## f003074 — Pre-Proposal: Wasm GC Support in the Canonical ABI (2025-06-03, en)

### Questions
- Q: In the Component Model's GC canonical ABI, should common shapes (e.g. `null` for `none`/`error`, a boolean `i32` for a no-payload `result`) get ad hoc special-cased lowerings for efficiency, or should the ABI stick to one regular, shape-driven lowering rule per component type?
  concepts: canonical-abi, wasm-gc, type-lowering; domains_live: wasm; positions_seen: ad-hoc-optimize-common-shapes, regular-lowering-only

- Q: Should core Wasm eventually gain a primitive sum-type / tagged-union construct (with e.g. a `br_table`-like case-matching instruction), or is representing variants as `struct` subtyping trees in a shared `rec` group sufficient?
  concepts: wasm-gc, variants, type-system; domains_live: wasm; positions_seen: primitive-sum-types-worthwhile, marginal-benefit-over-encoding

### Claims
- voice: lukewagner | position: ad-hoc-optimize-common-shapes | date: 2025-06-04 | locator: comment @lukewagner 2025-06-04T21:38:44Z | paraphrase: proposes letting `ref.null` represent `none`/no-error when the inner type disallows null, and using a boolean `i32` for no-payload `result`, since these shapes are extremely common and "licensed" as CABI-level wins even though ad hoc | quote: "we are licensed to do that in the CABI when it's a significant win and `option` is very common" | practiced_evidence: none
- voice: rossberg | position: regular-lowering-only | date: 2025-06-06 | locator: comment @rossberg 2025-06-06T09:39:34Z | paraphrase: disputes that the null-for-none optimization would apply to anywhere near 95% of options in practice, because languages with parametric polymorphism (e.g. Java's Optional) typically cannot perform that specialization without costly runtime type dispatch | quote: "FWIW, I don't think it is gonna be even close to 95%. Languages with parametric polymorphism typically don't or can't do such a specialisation" | practiced_evidence: none
- voice: fitzgen | position: cautious-of-shape-proliferation | date: 2025-06-13 | locator: comment @fitzgen 2025-06-13T19:02:24Z | paraphrase: allowing extra matched shapes like `i31ref` risks a slippery slope of "how many shapes is enough," so any widening of matchable shapes needs an explicit design principle, not case-by-case allowances | quote: "It seems to me like this could potentially be a slippery slope: How many shapes is enough?" | practiced_evidence: none
- voice: fitzgen | position: primitive-sum-types-worthwhile | date: 2025-06-16 | locator: comment @fitzgen 2025-06-16T18:35:42Z | paraphrase: first-class sum types would let compilers emit a `br_table`-like exhaustive match instead of a chain of `br_on_cast` checks, which is easier to optimize and lets tools like binaryen reason over a closed case set | quote: "The most immediate benefit that first-class sum types would give us over shoe-horning sum types into struct subtypes would be a br_table-like instruction for exhaustively matching on cases" | practiced_evidence: none
- voice: rossberg | position: marginal-benefit-over-encoding | date: 2025-06-16 | locator: comment @rossberg 2025-06-16T21:05:40Z | paraphrase: a custom type descriptor can already store an integer tag for `br_table` dispatch without wasting per-variant space, so primitive sum types would mainly save the trailing cast check, which requires substantial new Wasm machinery for limited additional gain | quote: "Saving the cast would essentially require adding a case construct to Wasm, which would be quite a bit of machinery. Other than that, sum types do not offer a hell lot of relevant generic optimisations" | practiced_evidence: none

---

## f003082 — Add initial porting of table_ops from arbitrary to mutatis (2025-06-04, en)

### Nothing new
`nothing new`: a routine fuzz-mutator port; the reviewer's (fitzgen) simplification suggestions (avoid `pub`, derive `Default`, use a helper over a macro, fix an accidental O(n²) loop) are all accepted by the author without pushback — no disagreement between practitioners is voiced.

---

## f003126 — Adding TextOutline component to add outlining by upstreaming implementation (2025-06-14, en)

### Questions
- Q: When a feature is useful but the only available implementation is algorithmically expensive (here, exponential batch count with glyph/outline count), should a game engine merge it now with documented limits, or hold it out of core until an efficient approach exists?
  concepts: performance, API-surface, feature-gating; domains_live: desktop-cli-ui, other; positions_seen: ship-with-documented-limits, hold-for-proper-solution

### Claims
- voice: TotalKrill | position: ship-with-documented-limits | date: 2025-06-16 | locator: comment @TotalKrill 2025-06-16T16:10:03Z | paraphrase: an enum of fixed, small widths (Px1/Px2/Px3) makes the performance ceiling explicit to users while still shipping the feature for the common case | quote: "I would argue that we could go with a clearer enum of Px1, Px2, Px3... It would also quite clearly communicate the limitations of this implementation, while still allowing us to have it." | practiced_evidence: none
- voice: UkoeHB | position: ship-with-documented-limits | date: 2025-06-16 | locator: comment @UkoeHB 2025-06-16T20:45:49Z | paraphrase: documents the cost in the public API doc comment (exponential growth with width) rather than blocking the feature | quote: "The computation cost of the outline increases exponentially with width in the current implementation, so it is not recommended to use a width greater than 3." | practiced_evidence: bevy_slow_text_outline crate (moved here after the PR closed)
- voice: ickshonpe | position: hold-for-proper-solution | date: 2025-06-19 | locator: comment @ickshonpe 2025-06-19T09:25:27Z | paraphrase: even with the batching fixes, most users will not read the docs closely enough to avoid the performance cliff, and the implementation still has visible artifact bugs under transform/rotation | quote: "I'm feeling very negative about it now, even with all the improvements that have been made... most users aren't going to carefully read the docs for text outlines." | practiced_evidence: none
- voice: alice-i-cecile | position: hold-for-proper-solution | date: 2025-06-19 | locator: comment @alice-i-cecile 2025-06-19T00:58:08Z | paraphrase: reluctant to merge something this inefficient and rough; asks whether an offline font-preprocessing/baking approach could substitute, and ultimately wants a proper SDF-based text rendering solution instead | quote: "I'm really reluctant to merge something this slow and jank, even though I appreciate that it's better than it could have been." | practiced_evidence: none

---

## f003169 — Allow splitting control over modem clocks (2025-06-24, en)

### Questions
- Q: For a shared hardware resource with an enable/disable lifecycle (a radio PHY clock shared across peripherals), should safety rest on a reference-counted controller object, or on RAII-style exclusive ownership tied to the peripheral singletons themselves?
  concepts: ownership, RAII, concurrency-primitives, embedded-resource-management; domains_live: embedded; positions_seen: reference-counted-controller, raii-exclusive-ownership

### Claims
- voice: Frostie314159 | position: reference-counted-controller | date: 2025-06-24 | locator: comment @Frostie314159 2025-06-24T13:26:21Z / 2025-06-24T15:18:21Z | paraphrase: proposes a `RadioClockController` that counts references per modem so disabling one modem's use of the shared PHY clock doesn't disable it out from under another modem still relying on it | quote: "unless we count the reference for each modem clock controller individually, just repeatedly calling the function to disable the PHY clock on one modem clock controller, would eventually disable the PHY clock, even if different modems still rely on it." | practiced_evidence: esp-hal PR 3687 (superseded within the same PR, see below)
- voice: bugadani | position: raii-exclusive-ownership | date: 2025-06-25 | locator: comment @bugadani 2025-06-25T13:18:42Z / 2025-06-25T13:29:48Z | paraphrase: questions why a separate `RadioClockController` and manual ref-count are needed at all if only the peripheral singletons (already unique/exclusive by construction) can touch the clock; proposes implementing the clock-control logic directly on the radio peripheral structs instead | quote: "I'd just implement all relevant code for the radio singletons, then only radio users could meddle with any of this." | practiced_evidence: esp-hal (adopted in this PR by 2025-07-01)
- voice: Frostie314159 | position: raii-exclusive-ownership | date: 2025-07-01 | locator: comment @Frostie314159 2025-07-01T15:05:34Z | paraphrase: having converged with the reviewer, removes the separate `RadioClockController` and reduces the design to a single shared PHY ref-count guarded by the peripheral-singleton pattern | quote: "I've removed it with the latest commit." | practiced_evidence: esp-hal PR 3687 merged form

---

## f003238 — How GoodData turbocharged AI analytics with Qdrant (2025-07-09, en)

### Nothing new
`nothing new`: a vendor case-study/marketing post about a customer's RAG architecture; no Voice with a public Rust track record states a contested technical position.
