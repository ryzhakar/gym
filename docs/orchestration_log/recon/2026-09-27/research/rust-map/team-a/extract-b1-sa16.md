## f007175 — Hypershell: A Type-Level DSL for Shell-Scripting in Rust (2025-06-14, en)

### Questions
- Q: Should optional/alternate implementations in a Rust library be selected via Cargo feature flags, or via generic type-level component wiring (traits/generics, e.g. CGP-style)?
  concepts: generics, traits, macros; domains_live: core; positions_seen: generic-wiring-over-feature-flags
- Q: Is hosting a Rust DSL's programs as compile-time types (zero runtime cost, no dynamic loading) worth trading away runtime-loaded/dynamic DSL programs?
  concepts: macros, type-level programming, DSLs; domains_live: desktop-cli-ui, core; positions_seen: compile-time-typed-dsl

### Claims
- voice: Soares Chen | position: generic-wiring-over-feature-flags | date: 2025-06-14 | locator: § Modularity of HandleSimpleExec | paraphrase: CGP-style generic component wiring lets alternative implementations coexist and be tested together, avoiding the combinatorial-testing burden of Cargo feature flags. | quote: "This generic approach is also less error-prone than feature flags, as all alternative implementations can coexist and be tested simultaneously" | practiced_evidence: https://github.com/contextgeneric/cgp
- voice: Soares Chen | position: compile-time-typed-dsl | date: 2025-06-14 | locator: § Disadvantages, Dynamic Loading | paraphrase: Hosting DSL programs as compile-time types trades away runtime dynamic loading (config files, plugins, game mods) for zero-cost, compile-time interpretation. | quote: "since the DSL is hosted at compile time, this technique cannot be easily used to run DSL programs loaded into a host application during runtime" | practiced_evidence: https://github.com/contextgeneric/cgp

## f007341 — Exporting files from a Rust/WASM frontend (2026-02-09, en)

### Nothing new
`nothing new` — practical web_sys/WASM file-export tutorial (Blob + object-URL + Drop-based RAII cleanup); presents one working technique without contrasting alternatives or naming any contested point among practitioners.

## f007472 — Who Are Active? Human and Non-human Predicates in Generated Query APIs (2026-08-13, en)

### Nothing new
`nothing new` — TeaQL's internal naming-grammar rule for its generated query API, applied identically across Java/Rust/Go/Python/.NET/TypeScript; a settled in-house convention with no Rust-specific contested point and no disagreement voiced.

## f007483 — Building a Plugin System for Rust: WebAssembly vs Native vs Scripting Language vs Rules Engine (2026-08-18, en)

### Questions
- Q: How should a Rust application implement a plugin system: native dynamic libraries, an embedded scripting language, WebAssembly, or an expression/rules engine?
  concepts: FFI, unsafe, ABI stability, WASM, sandboxing; domains_live: desktop-cli-ui, embedded, wasm, core; positions_seen: native-dylib (rejected), scripting-language (preferred default), wasm (too immature), expression-engine (safe but limited)

### Claims
- voice: Sylvain Kerkour | position: native-dylib-rejected | date: 2026-08-18 | locator: § Native Libraries | paraphrase: Rejects native dynamic libraries as a Rust plugin mechanism: no stable ABI, no sandboxing (a buggy or malicious plugin can crash or compromise the host), and compiled-code distribution hides backdoors and is harder for users to share/audit than scripts. | quote: "For all these reasons I don't recommend using dynamic libraries as plugins." | practiced_evidence: none stated
- voice: Sylvain Kerkour | position: scripting-language-preferred | date: 2026-08-18 | locator: § Scripting language, closing paragraph | paraphrase: Recommends embedding QuickJS (over V8/deno_core and over Lua) as the default plugin approach: small binary size, no JIT, faster cold starts, easier integration. | quote: "For all these reasons I recommend embedding QuickJS to build a plugin system as the default approach, and to evaluate the other methods only if there are too many drawbacks for your specific use case." | practiced_evidence: none stated
- voice: Sylvain Kerkour | position: wasm-too-immature | date: 2026-08-18 | locator: § WASM, closing paragraph | paraphrase: Judges WebAssembly currently too immature for a Rust plugin system despite its sandboxing strength, citing uneven cross-language WASM support and churning toolchains/targets (WASI p1, p2). | quote: "I think that WebAssembly is currently too immature to be used for a plugin system and will make the life of developers wanting to create plugins hard." | practiced_evidence: none stated
- voice: Sylvain Kerkour | position: expression-engine-for-bounded-untrusted-eval | date: 2026-08-18 | locator: § Expression engine, closing paragraph | paraphrase: For his own project he forked CEL to a boolean-only subset because non-Turing expression languages give bounded, predictable-runtime evaluation of untrusted user input; recommends QuickJS instead for most other projects. | quote: "expressions evaluating to a bool is the easiest and safest way to achieve that, but for most projects I would recommend integrating QuickJS." | practiced_evidence: none stated

## f007657 — (claimed: MLIR with Rust, edgarluque.com/blog/mlir-with-rust, 2023-11-29)

UNREACHABLE. The URL now resolves to an unrelated Turkish-language gambling/slot-game guide ("Sweet Bonanza Oyna"), confirmed by a direct fetch — the domain has been hijacked/repurposed and no longer hosts the original MLIR-with-Rust article. Stopped on it; not reconstructed from memory.
