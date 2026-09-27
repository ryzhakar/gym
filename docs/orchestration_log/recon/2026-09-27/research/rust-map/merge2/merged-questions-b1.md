# Merged Questions — Rust map batch 1, second blind merge

Merger: t4-merge2-b1 (opus), blind to RECON/merge/ and RECON/audit/. Test for one Question: a competent practitioner could not hold opposite Positions on the members. Shared keywords never merge.

## Inputs and counts

- Parsed every `team-a/extract-b1-*.md` and `team-b/extract-b1-*.md` (original slices, send-back sR, supplementary saL1/saL2); Question markers `- Q:`, `- Question:` (team-b sR03/sR05/sR09), `### Question —` (team-a sR14).
- 450 team-local Questions found; 10 superseded by saL1 (below); 440 crosswalked (team A 215, team B 225).
- Canonical Questions: 385; 42 with more than one member. Team A covers 203, team B 210, shared 28.
- Team-local id: `<team>-<slice>-<frame_id>-q<k>`, slice = extract file suffix, k = order within that source section.
- `question_domains`: the extractor's `domains_live`, filtered to the 12 strata ids; for team-b sR03/sR05/sR09 entries, which give no per-Question domains, the source header's `domain:` is used; team-a sR14 uses its `Domain:` line. `source_hint`: the frame's `domain_hints` from `samples/batch-1-team-<t>.csv`.

## Superseded, not crosswalked

saL1 re-extracted f005360, f005454, f005516 with commenter names; per the dispatch its entries replace the earlier ones:

- `a-sa14-f005360-q1` → replaced by saL1 entries for f005360
- `a-sa14-f005360-q2` → replaced by saL1 entries for f005360
- `a-sa14-f005360-q3` → replaced by saL1 entries for f005360
- `a-sa14-f005360-q4` → replaced by saL1 entries for f005360
- `a-sa14-f005454-q1` → replaced by saL1 entries for f005454
- `a-sa14-f005454-q2` → replaced by saL1 entries for f005454
- `a-sa14-f005454-q3` → replaced by saL1 entries for f005454
- `a-sa15-f005516-q1` → replaced by saL1 entries for f005516
- `a-sa15-f005516-q2` → replaced by saL1 entries for f005516
- `a-sa15-f005516-q3` → replaced by saL1 entries for f005516

## Merged Questions

### m2b1-q005 — When is Rust→Wasm worth it over plain JavaScript: only for heavy compute with minimal interop, or more broadly?
- members: `b-sR01-f000256-q1`, `a-sa26-f011460-q1`, `a-sa26-f011460-q2`, `b-sb19-f005699-q1`
- domains: frontend, wasm, web
- reason: all choose Rust+Wasm vs JS by workload (UNSURE: a-q1 asks if JS is enough, a-q2 whether small functions qualify)

### m2b1-q023 — Should a large change land as one big PR, or be split into small incrementally mergeable PRs?
- members: `a-02-f000993-q1`, `b-sb08-f002518-q2`
- domains: core, ml
- reason: same review decision

### m2b1-q025 — Should shared mutable state go through interior mutability (Arc<Mutex>, Rc<RefCell>), or should ownership be redesigned to pass mutable access explicitly?
- members: `a-sR07-f002155-q1`, `a-sa06-f003414-q2`, `b-sb04-f001022-q1`
- domains: core, desktop-cli-ui, embedded
- reason: all choose interior-mutable sharing vs explicit threading of &mut/context (UNSURE: three different contexts)

### m2b1-q029 — Should a library pay implementation cost (vendoring, hand-rolling, uglier code) to shrink its dependency footprint, or take the dependency?
- members: `b-sR03-f001160-q1`, `b-sR05-f002453-q1`, `a-sa04-f002865-q1`, `a-sa14-f005079-q2`, `a-sR06-f002016-q1`
- domains: core, decentralized-iroh, embedded, ml, wasm
- reason: all weigh own code vs a dependency for footprint/audit cost; b-sR05 names b-sR03's as the same (UNSURE: contexts differ — syn feature, intrusive list, systemd protocol, libtorch audit)

### m2b1-q036 — Should logic used at one call site be extracted into its own function/module, or kept inline?
- members: `b-sb04-f001392-q3`, `a-sa14-f005079-q4`
- domains: core
- reason: same extract-vs-inline decision (UNSURE: a's reason is cfg surface)

### m2b1-q042 — Should a public name favour brevity/memorability or explicit clarity?
- members: `b-sR04-f001515-q1`, `b-sR04-f001617-q1`
- domains: decentralized-iroh, desktop-cli-ui
- reason: identical Question

### m2b1-q048 — Should related chip variants share one PAC crate gated by Cargo features, or get one PAC crate per chip?
- members: `a-sa01-f001838-q1`, `b-sb06-f001838-q1`
- domains: embedded
- reason: same PR, same decision: shared feature-gated PAC vs per-chip PAC

### m2b1-q049 — Should a long-running service treat an individual failure (bad connection, hostile input) as fatal, or contain it and keep serving/degrade?
- members: `a-sR05-f001981-q1`, `a-sa14-f004985-q3`
- domains: cloud-workers, decentralized-iroh, distributed, wasm
- reason: same crash-vs-contain decision for external failures

### m2b1-q059 — Should a foundational networking library keep a minimal core with pluggable extensions, or bundle more built-in functionality/transports?
- members: `a-sa02-f002124-q1`, `a-sR11-f004170-q1`
- domains: decentralized-iroh, distributed
- reason: both iroh core-scope: bundle vs minimal core plus extension points

### m2b1-q073 — Do Rust's memory-safety guarantees prevent resource leaks (leaked tasks/threads) in a long-running service, or must leak detection be engineered separately?
- members: `a-sR07-f002341-q1`, `b-sR05-f002341-q1`
- domains: core, distributed
- reason: same post-mortem, same claim by Arqu

### m2b1-q089 — Should hot-reload tooling hot-patch binaries (bypassing the normal build/link) or pursue faster full rebuilds?
- members: `a-sa26-f011305-q5`, `b-sb09-f002719-q1`
- domains: core, desktop-cli-ui, embedded, frontend, wasm
- reason: same edit-loop decision, same Voice on one side (UNSURE: a frames only the bypass cost)

### m2b1-q092 — Is copying another project's or contributor's open-source work without coordination or credit normal practice or a breach of norms?
- members: `a-sa05-f003025-q2`, `a-sa13-f004772-q4`
- domains: core
- reason: extractor linked them; same attribution-norm decision

### m2b1-q105 — Should a library use concrete, enumerable error types (thiserror/snafu) or a single opaque type (anyhow)?
- members: `b-sb10-f003188-q2`, `b-sb10-f003222-q1`, `a-sa14-f005149-q1`, `a-saL2-f011092-q6`
- domains: core, decentralized-iroh, distributed
- reason: all choose typed vs opaque errors (UNSURE for a-saL2-f011092-q6: framed by codebase maturity, not library vs app)

### m2b1-q127 — Should a closed set of known kinds be an enum, trait objects, or unsafe unions/tagged pointers?
- members: `a-sa07-f003704-q3`, `a-sa17-f007884-q1`
- domains: core, desktop-cli-ui, ml
- reason: same enum-vs-dyn decision for a known set

### m2b1-q155 — Should async cleanup rely on best-effort Drop (RAII with workarounds), or require an explicit async close()?
- members: `b-sR10-f004423-q1`, `b-sR10-f004741-q1`, `b-sb17-f005159-q2`
- domains: core, decentralized-iroh, distributed
- reason: identical Question across two iroh posts plus the same RAII-vs-close decision in f005159

### m2b1-q156 — Should API not ready for stabilization ship behind an explicit unstable feature flag, or should the release wait?
- members: `b-sR10-f004423-q2`, `b-sR10-f004741-q2`
- domains: core, decentralized-iroh, distributed
- reason: identical Question, two iroh posts

### m2b1-q162 — Should a library panic on invalid input (documented), or always signal failure through Result/explicit checks?
- members: `b-sR12-f005421-q1`, `b-sR10-f004573-q1`, `a-sa21-f011069-q3`
- domains: core, embedded, ml
- reason: same library-panic policy; b-sR12 names b-sR10's as the same disagreement (UNSURE for a-sa21: ad hoc bailout panics)

### m2b1-q171 — Should optional functionality live behind feature flags in one crate, or be split into separate crates?
- members: `a-sR13-f004685-q2`, `b-sR12-f005120-q1`
- domains: core, decentralized-iroh, ml
- reason: same decision: one crate with features vs split crates

### m2b1-q173 — Should Rust projects accept AI-assisted contributions, and how should that be policed (ban, accountability rule, normal review)?
- members: `b-sR11-f004993-q1`, `b-sR13-f009740-q1`, `b-sb15-f004721-q1`
- domains: core, wasm
- reason: same contribution-policy decision

### m2b1-q207 — Should async Rust standardize on Tokio as default runtime, or is a leaner/alternative runtime still a live choice?
- members: `a-sa29-f012940-q2`, `b-sb17-f005159-q1`
- domains: cloud-workers, decentralized-iroh, distributed, web
- reason: same runtime-default decision

### m2b1-q220 — Should HTTP-level failures be returned as Ok(response with status) / one unified response enum, or through the Err channel / split error types?
- members: `a-saL1-f005454-q1`, `b-sb22-f008906-q3`
- domains: cloud-workers, core, web
- reason: both decide whether HTTP errors live in Ok or Err (UNSURE: a is about ? ergonomics)

### m2b1-q221 — Should cross-cutting request concerns (auth, logging, rate limits) go in a global middleware stack, or be obtained explicitly per handler?
- members: `a-saL1-f005454-q2`, `b-sb22-f008906-q1`
- domains: cloud-workers, core, web
- reason: same middleware-vs-per-handler decision (UNSURE: a's alternative is typestate capabilities, b's is helpers/macros)

### m2b1-q226 — For shared mutable state, should concurrent code use Mutex or lock-free atomics/CAS?
- members: `a-sa17-f007846-q1`, `b-sb18-f005600-q1`
- domains: core, distributed, ml
- reason: same lock vs lock-free decision

### m2b1-q243 — For a failure-heavy, high-throughput ingress layer, do Rust's ownership model and pattern matching justify their cost over a simpler language?
- members: `a-sa15-f005948-q1`, `b-sb19-f005948-q1`
- domains: cloud-workers, distributed
- reason: same talk, same decision

### m2b1-q244 — Should a battle-tested C security library (codecs, TLS) be replaced by a memory-safe Rust implementation?
- members: `a-sa15-f006797-q1`, `b-sb19-f005964-q1`
- domains: core, desktop-cli-ui, web
- reason: same replace-C-with-Rust decision (UNSURE: a stresses the Rust crate's lower maturity)

### m2b1-q256 — Should structs/enums carry lifetime parameters (borrowed data), or keep data owned as a rule of thumb?
- members: `b-sb20-f007364-q1`, `b-sb20-f007608-q2`
- domains: core
- reason: identical Question

### m2b1-q258 — How to represent a mutable cyclic object graph: Rc<RefCell>/Arc<Mutex>, raw pointers, or indices into an arena?
- members: `b-sb20-f007608-q1`, `b-sb26-f013214-q3`
- domains: core, other
- reason: identical Question

### m2b1-q259 — For Android calling a shared Rust library, should the JNI layer be written in Rust or in C++?
- members: `b-sb20-f007678-q1`, `b-sb22-f008914-q1`
- domains: other
- reason: identical Question

### m2b1-q260 — Across a Rust FFI boundary (Kotlin/Swift/JS), should complex data be copied or shared by reference?
- members: `b-sb20-f007678-q2`, `b-sb22-f008914-q2`
- domains: other, swift-interop
- reason: identical Question

### m2b1-q261 — Is a custom proc macro worth it to remove small fixed per-function boilerplate (Lambda main/tracing setup), or should the boilerplate be written out?
- members: `a-sa17-f007736-q1`, `b-sb20-f007736-q1`, `b-sb20-f007760-q1`
- domains: cloud-workers, core
- reason: same author, same decision on Lambda-handler macro; f007760 is the same chapter series with identical framing

### m2b1-q262 — Should a Rust service on AWS run on Lambda/FaaS or on long-running containers (ECS/Fargate), or split by environment?
- members: `a-sa17-f007797-q1`, `b-sb20-f007797-q1`, `a-sa24-f011220-q1`
- domains: cloud-workers, distributed
- reason: all choose the compute substrate for a Rust service, Lambda vs containers; b's environment split is one Position on it

### m2b1-q263 — Is AI-generated prose acceptable in community communication (forum posts, proposals, newsletters)?
- members: `a-sa29-f013224-q2`, `b-sb20-f007942-q1`
- domains: core, other
- reason: both on AI-written text in community channels (UNSURE: forum post vs newsletter)

### m2b1-q275 — Does thiserror alone give enough error context in logs (source chain), or must errors be wrapped in anyhow/eyre or displayed with {:#}?
- members: `a-sa18-f008583-q1`, `b-sb21-f008583-q1`
- domains: cloud-workers, core
- reason: same source, same decision

### m2b1-q296 — Should std provide #[derive] for arithmetic operator traits with field-wise semantics?
- members: `a-sa19-f009292-q1`, `b-sb22-f009292-q1`
- domains: core
- reason: same thread, same proposal

### m2b1-q309 — Should critical Rust infrastructure run on volunteer maintainers or on directly funded maintainers?
- members: `a-sR15-f009751-q1`, `b-sR13-f009755-q1`
- domains: core
- reason: same funding decision

### m2b1-q311 — Does porting C/C++ code to Rust yield memory safety because it compiles, or does it require restructuring (and can introduce UB)?
- members: `a-sa21-f011069-q2`, `b-sb24-f011312-q4`
- domains: core
- reason: same porting-safety decision

### m2b1-q332 — Should Rust be pushed into high-level rapid application development, or kept to systems software?
- members: `a-sa26-f011305-q1`, `a-sa26-f012146-q1`
- domains: desktop-cli-ui, frontend, other, web
- reason: extractor reused wording

### m2b1-q345 — To add behaviours to types (serialize, debug, diff), should each get its own trait plus proc-macro derive, or should types expose one reflection shape many behaviours consume?
- members: `a-sa25-f011413-q1`, `b-sb24-f011413-q1`
- domains: core
- reason: same talk; both weigh per-trait proc-macro derives against a single shipped shape (UNSURE: a frames it as proc macros' cost, b as shape vs derives)

### m2b1-q347 — Is trading compile-time codegen for runtime reflection a good trade (ergonomics, build time vs runtime speed), and can JIT recover the speed?
- members: `a-sa25-f011413-q3`, `b-sb24-f011413-q3`
- domains: core, desktop-cli-ui
- reason: same talk, same runtime-vs-compile-time trade

### m2b1-q348 — Should compiler-level reflection model types as the compiler sees them or as users need them, and may reflection mutate?
- members: `a-sa25-f011413-q4`, `b-sb24-f011413-q4`
- domains: core
- reason: same talk, same open design question

### m2b1-q349 — How far should microbenchmark comparisons presented without rebuttal be trusted?
- members: `a-sa25-f011413-q5`, `a-sa28-f012469-q1`
- domains: core
- reason: extractor reused the Question verbatim across two talks

### m2b1-q358 — Should heap profiling (jemalloc mem-prof) be compiled in and on by default in a production service, or opt-in via a build flag?
- members: `a-sa26-f011684-q1`, `b-sb25-f011684-q1`
- domains: core, other
- reason: same source, same decision

## Kept apart after consideration

- `a-sa05-f002466-q1` / `b-sR05-f002466-q1` (m2b1-q077 / m2b1-q078): same comment; a asks type-enforcement vs convention, b asks parameter vs encapsulated live range — orthogonal, one can pass-as-parameter with typed exclusive access
- `a-sa09-f004055-q1` / `a-sa05-f002466-q1` (m2b1-q143 / m2b1-q077): extractor marked 'recurs here as'; typed PAC accessors vs raw volatile is a different decision from scratch-register discipline
- `a-sR09-f003702-q1` / `b-sR08-f003702-q1` (m2b1-q123 / m2b1-q124): same post; hazmat-API-for-speed vs rayon/SIMD choice are different decisions
- `a-sa14-f004947-q1` / `b-sR11-f004947-q1` (m2b1-q184 / m2b1-q185): same tool; mirror curl's flags vs one-tool-per-protocol are different decisions
- `a-sR16-f012642-q1` / `b-sb25-f012642-q1` (m2b1-q371 / m2b1-q372): same doc; tiered unchecked/checked builders vs Regular-vs-Bulk write API
- `a-sa25-f011413-q2` / `b-sb24-f011413-q2` (m2b1-q346 / m2b1-q350): same talk; serde centralization vs annotation-vs-reflection dispatch
- `a-sa29-f012940-q1` / `b-sb24-f011306-q1` (m2b1-q375 / m2b1-q337): tracing vs log-then-bridge, and tracing vs OpenTelemetry API: alternatives differ
- `a-sa26-f011305-q3` / `b-sb17-f005144-q1` (m2b1-q334 / m2b1-q204): language-level auto-clone vs a framework's generational handles; one can favour the handle and oppose the language change
- `a-sa18-f009104-q1` / `b-sb24-f011312-q6` (m2b1-q289 / m2b1-q344): general overloading/named args vs overloading for FFI only
- `b-sb19-f005743-q1` / `b-sb26-f012849-q1` (m2b1-q232 / m2b1-q373): moral imperative vs tradeoff, and broad improvement vs narrow value: one can hold 'big engineering win, not a moral matter'
- `a-saL2-f011092-q5` / `b-sb23-f011233-q2` (m2b1-q317 / m2b1-q327): nightly in production vs nightly std::simd: opposite answers are coherent
- `b-sb06-f002033-q1` / `a-sa19-f009343-q2` (m2b1-q056 / m2b1-q302): cargo feature vs --cfg gating, and autodetect vs explicit opt-in: related, alternatives differ
- `b-sR05-f002151-q2` / `a-sa06-f003558-q1` (m2b1-q064 / m2b1-q115): feature flag vs cfg(target) once a target exists, vs waiting for the target
- `b-sb05-f001512-q1` / `b-sR12-f005421-q1` (m2b1-q038 / m2b1-q162): HAL constructors on static config vs library panic policy: embedded practitioners hold opposite answers
- `a-sa15-f005857-q1` / `b-sb21-f008390-q3` (m2b1-q241 / m2b1-q272): Elm-style vs immediate for one app, vs whether the choice matters at small scale
- `b-sb03-f000669-q1` / `a-sa14-f004985-q3` (m2b1-q014 / m2b1-q049): surfacing a bug (missing context) vs containing hostile input

## Single-member Questions

| canonical | member | domains | Question |
| --- | --- | --- | --- |
| m2b1-q001 | `a-sR01-f000227-q1` | embedded | Is RTIC (and a hardware-scheduled, compile-time-analyzed concurrency model generally) an RTOS, or is it a concurrency framework rather than an operating system? |
| m2b1-q002 | `a-sR01-f000227-q2` | embedded | Should real-time/embedded Rust frameworks model concurrency with async/await tasks rather than classical run-to-completion/interrupt-only tasks? |
| m2b1-q003 | `b-sR01-f000233-q1` | embedded;web;distributed;other | When should a Rust practitioner reach for async instead of threads? |
| m2b1-q004 | `b-sR01-f000233-q2` | core | Is async Rust production-ready today given its known gaps? |
| m2b1-q006 | `b-sR01-f000464-q1` | ml | Does quantization reliably speed up inference in candle, or only for some model architectures? |
| m2b1-q007 | `b-sR01-f000464-q2` | ml | Should GPU (Metal) backend work be prioritized ahead of further CPU/quantization optimization in candle? |
| m2b1-q008 | `b-sb01-f000493-q1` | core | Should combinatorial pipeline state be represented as an explicit generated array/struct of bool-driven variants, or as bitflags with named constants? |
| m2b1-q009 | `a-01-f000530-q1` | desktop-cli-ui | When Rust's lack of method overloading forces a choice for a type-conversion API surface (e.g. building a `Color` from `Vec4`, `[f32; 4]`, `Vec3`, `[f32; 3]` across several color spaces), should the API expose one explicitly-named method per source-type-and-color-space combination, or a smaller set of generic methods parameterized by a trait bound (`impl Into<T>`) or an enum discriminant? |
| m2b1-q010 | `a-sR01-f000538-q1` | web;core | In a `ToTokens` impl for a proc-macro AST enum, should each arm call `to_tokens` on the matched variant directly, or is it acceptable to build an intermediate `TokenStream` and feed it into the outer one? |
| m2b1-q011 | `a-sR01-f000538-q2` | web | When a new macro feature's behavior largely overlaps existing generic tests, should reviewers ask for a dedicated test of the new case anyway, or is that redundant? |
| m2b1-q012 | `a-01-f000543-q1` | frontend | When a UI framework's form-submission API hands back untyped, string-keyed values (e.g. a `HashMap<String, Vec<String>>`) for deserialization into a caller-defined struct via serde, should the ambiguity between a single value and a multi-value field (e.g. a multi-select) be resolved by an explicit schema/cardinality marker in the data, or by a permissive/heuristic deserializer that infers list-vs-scalar from the observed value count per field? |
| m2b1-q013 | `b-sb03-f000569-q1` | ml | When a resource (a Metal command buffer/lock) needs coordinated access from multiple threads, should the implementation wait on the lock (with a timeout) now, or defer multithreaded encoding until single-threaded use has proven the design? |
| m2b1-q014 | `b-sb03-f000669-q1` | web | When a context a handler expects (e.g. `ResponseOptions`) is legitimately missing under load, should the code fall back to a silent safe default, or should the panic/error surface so the root cause gets found and fixed? |
| m2b1-q015 | `a-01-f000701-q1` | frontend | When a proc-macro conditionally emits a call into a crate (here, `tracing::instrument`) behind a feature flag inherited transitively through another crate's feature, should the macro hardcode an unqualified path that silently requires every downstream crate to independently declare that dependency in its own Cargo.toml, or should it use a fully-qualified/re-exported path so the hidden transitive requirement never surfaces as a downstream compile error? |
| m2b1-q016 | `b-sb03-f000715-q1` | embedded | Should a driver's mode (blocking vs. async) be encoded in the type system via a typestate generic, so the compiler prevents implementing async traits in blocking mode, or handled as a simpler runtime-only mechanism with no type-level distinction? |
| m2b1-q017 | `b-sR03-f000763-q1` | desktop-cli-ui | in example/demo code, should tabular data be modeled with a dedicated domain struct or with generic collections (`Vec<Vec<String>>`)? |
| m2b1-q018 | `b-sR03-f000763-q2` | desktop-cli-ui | should derived per-column values be computed in a single iterator pass or via several simpler passes/collects? |
| m2b1-q019 | `b-sR03-f000763-q3` | desktop-cli-ui | should match arms on an enum use a local glob import (`use Enum::*;`) to drop the type-qualified path, or keep variants fully qualified? |
| m2b1-q020 | `b-sR03-f000889-q1` | wasm | before a spec (WASI 0.3 async) is finalized, should the ecosystem ship stopgap/polyfill implementations to unblock development, or wait for the finished standard? |
| m2b1-q021 | `a-02-f000957-q1` | frontend | When designing an async-computation hook API, should cancellation semantics be committed to upfront even at the cost of a larger initial API surface, or postponed until real usage demonstrates the need? |
| m2b1-q022 | `a-02-f000977-q1` | wasm | In FFI/wasm-bindgen-style APIs, should a safety-encoding wrapper type like `NonNull<T>` be accepted as a parameter even when it forces a runtime null check, or should the API stick to raw pointer types to avoid the check? |
| m2b1-q024 | `a-02-f000993-q2` | ml | Should a generic tensor-container abstraction enforce a single uniform tensor type across backends, or allow different backends/precisions to coexist within the same container to support mixed-precision training and multi-backend graphs? |
| m2b1-q026 | `a-02-f001053-q1` | distributed;core | For performance-critical, correctness-sensitive infrastructure code, should teams reach for an existing (if less popular) persistent-data-structure crate, or hand-roll a bespoke specialized data structure for maximum control and performance? |
| m2b1-q027 | `a-sR04-f001096-q1` | ml | Should numeric reductions in a Rust ML kernel (e.g. softmax) accumulate in a higher-precision type than the input/output dtype? |
| m2b1-q028 | `a-sR04-f001096-q2` | ml;core | When a function moves to a different crate in a multi-crate Rust workspace, should its benchmark move with it, using `git mv` to preserve file history? |
| m2b1-q030 | `b-sR03-f001160-q2` | wasm | should a codegen tool trade a larger generated-output size for better runtime performance? |
| m2b1-q031 | `a-02-f001181-q1` | wasm;embedded | On hardware with "store-tearing" behavior, where a partial store can have observable side effects before trapping, should a WebAssembly runtime pay a load-before-store performance cost to guarantee precise, spec-compliant trap semantics, or accept imprecise traps as an acceptable, mostly theoretical risk on rare/low-power hardware? |
| m2b1-q032 | `a-02-f001231-q1` | desktop-cli-ui | Should runtime-registered ("dynamic") ECS components carry a compile-time type witness (a typed ID wrapper constrained to `T: Component`) for safe access, or stay untyped so that scripting/runtime-defined component variants aren't forced into newtyping? |
| m2b1-q033 | `b-sb04-f001365-q1` | web | Should a Rust web framework default new apps to a client-side (encrypted + signed cookie) session store for low-friction onboarding, or push toward a server-side session store (e.g. via `tower-sessions`) because client-stored session data cannot be force-invalidated or have permissions changed on the fly? |
| m2b1-q034 | `b-sb04-f001392-q1` | desktop-cli-ui;embedded;core | When a hand-tuned "fast path" optimization gives a large relative speedup on constrained/older hardware but a negligible absolute one on modern hardware, should a library keep the extra code complexity for the fast path, or drop it and favor the simpler code? |
| m2b1-q035 | `b-sb04-f001392-q2` | core | In a library, should an internal invariant be enforced with `debug_assert!` (documents and tests the assumption, but only panics in debug builds), or should the code be rewritten to be infallible so the assumption can never be violated even conceptually? |
| m2b1-q037 | `b-sR04-f001401-q1` | wasm | What function/code alignment should a JIT-style code generator use to avoid wasting instruction-fetch bandwidth? |
| m2b1-q038 | `b-sb05-f001512-q1` | embedded | Should embedded HAL constructors return `Result` instead of panicking (`unwrap`) on invalid configuration? |
| m2b1-q039 | `b-sb05-f001512-q2` | embedded | Should embedded HAL peripheral construction use the type-state pattern to enforce valid configuration at compile time, given the complexity it adds? |
| m2b1-q040 | `b-sb05-f001512-q3` | embedded | Should peripheral configuration be exposed through one `Config` struct set at construction, or through many individual constructors/`with_x` builder methods? |
| m2b1-q041 | `b-sb05-f001512-q4` | embedded | Should blocking and async variants of a peripheral driver share one generic implementation, or stay duplicated? |
| m2b1-q043 | `b-sb05-f001582-q1` | core;wasm | Should a type's representation encode an invariant directly (e.g. storing `log2(page_size)` instead of the raw value) to make invalid states unrepresentable, rather than validating separately at each use site? |
| m2b1-q044 | `b-sb05-f001582-q2` | core | When a compiler backend (LLVM/Cranelift) could optimize an eager computation away, should code still be written in the more efficient/lazy form? |
| m2b1-q045 | `b-sR04-f001724-q1` | core | Should a project's roadmap prioritize performance-focused effort over new-capability work when both compete for the same limited contributor time? |
| m2b1-q046 | `b-sR04-f001749-q1` | desktop-cli-ui | When an external callback API erases a reference's lifetime so it can be stored for later, how should the resulting unsafe surface be structured to stay sound? |
| m2b1-q047 | `b-sR04-f001749-q2` | desktop-cli-ui | When a transitive dependency upgrade trades one bug for another, should you pin to the older broken version, ship with the new regression, or hold the release? |
| m2b1-q050 | `a-sR05-f001981-q2` | decentralized-iroh;core | Should a Rust library actively chase down and eliminate duplicate transitive dependency versions (e.g., two copies of `rustls`) in its dependency tree? |
| m2b1-q051 | `b-sR05-f001983-q1` | wasm | should WIT syntax name a dependency-on-implementation with dedicated keywords (`locked-dep`/`unlocked-dep`), or with one generic keyword (`dependency`) whose lock state is inferred from the version syntax that follows it? |
| m2b1-q052 | `a-sR06-f001989-q1` | embedded | Should a HAL crate that needs allocator callback functions (e.g. `esp-wifi` needing `free_internal_heap`/`allocate_from_internal_ram`) take a hard Cargo dependency on the crate that implements them (e.g. `esp-alloc`), or keep the two crates decoupled behind a plain function-based interface any allocator can supply? |
| m2b1-q053 | `a-sR06-f002005-q1` | embedded | Should an embedded HAL's peripheral-signal abstraction expose electrical-configuration details (drive strength, pull resistors, input/output mode) on the signal type itself, even though this leaks device-specific configuration into what is meant to be a clean peripheral-routing abstraction? |
| m2b1-q054 | `a-sR06-f002005-q2` | embedded | When a driver constructor takes a set of GPIO/peripheral signals, should each signal be a required explicit value (even a placeholder like `Level::Low`), or should `Option<PIN>` be allowed so unused signals can be omitted? |
| m2b1-q055 | `b-sb06-f002027-q1` | embedded | When a foreign trait's shared type (e.g. `embedded_hal::spi::Operation`) can't expose the hardware-specific capability a HAL needs, should the HAL define its own parallel type (accepting API duplication and a breaking change) to extend, or add narrowly scoped extension methods that leave the foreign type untouched? |
| m2b1-q056 | `b-sb06-f002033-q1` | core | How should an unstable/nightly-only compiler feature be gated in library code — via a Cargo feature flag, or via a `--cfg` set through RUSTFLAGS? |
| m2b1-q057 | `b-sR05-f002048-q1` | ml | should a numerics/kernel library ship one fixed algorithm per operation, or ship several algorithm implementations and autotune between them at runtime? |
| m2b1-q058 | `b-sR05-f002048-q2` | ml | should hardware/backend-specific magic numbers used in a GPU kernel be hardcoded inline, or threaded through as a comptime-configurable parameter? |
| m2b1-q060 | `a-sa02-f002127-q1` | desktop-cli-ui | When gating a new optional capability (e.g. an image format) behind a feature flag, should the default favor minimal friction (enable it, narrow later if needed) or a curated bar of popularity/quality (keep it off until it clearly earns a place among defaults)? |
| m2b1-q061 | `b-sb07-f002142-q1` | other | Should an ECS's relationship "edge" components be public types with the exclusivity (one-to-one, one-to-many, many-to-many, ...) encoded at the type level for compile-time correctness and ergonomics, or should the edge-storing components be private (mutable only via commands/hooks) with a single consistent query API regardless of exclusivity? |
| m2b1-q062 | `b-sb07-f002142-q2` | other | Should ECS relationships be stored as archetype-fragmenting edges (entities with different relationship targets end up in different archetypes, enabling wildcard/nested-join/traversal query operations), or as non-fragmenting components (all related entities can share the same archetype/table, favoring dense cache-friendly iteration for common hierarchical cases)? |
| m2b1-q063 | `b-sR05-f002151-q1` | wasm | should a young, platform-specific integration (e.g. a new deploy target) live in-tree in a project's core crates, or ship as a separate out-of-tree crate? |
| m2b1-q064 | `b-sR05-f002151-q2` | wasm | should platform-specific code be gated behind a Cargo feature flag, or behind a `#[cfg(target...)]`/target-triple check once the platform is a proper Rust target? |
| m2b1-q065 | `b-sR05-f002177-q1` | decentralized-iroh | when compiling an async networking stack to a non-native target, should you swap the async runtime/networking primitives for target-specific shims, or keep the existing runtime (tokio) and target a platform that can host it directly? |
| m2b1-q066 | `a-sa03-f002236-q1` | cloud-workers | For a custom async I/O transport abstraction in Rust that must work across several carriers (raw TCP, TLS, WebSocket-wrapped tunnel), should the abstraction be built against the tokio-style `AsyncRead`/`AsyncWrite` traits, or against the `Sink`/`Stream` traits that most existing async WebSocket libraries expose? |
| m2b1-q067 | `a-sa03-f002243-q1` | ml | Should a machine-learning dataset abstraction that loads segmentation masks/images eagerly materialize every item into memory (e.g. building an `InMemoryDataset`), or support lazy/streaming access, given that images or datasets can be large? |
| m2b1-q068 | `a-sR07-f002271-q1` | frontend;wasm | When wrapping a browser Web API (e.g. `UrlSearchParams`) inside a Rust frontend-framework hook, should the API surface the raw web-sys type or convert it to an idiomatic Rust collection? |
| m2b1-q069 | `a-sR07-f002271-q2` | frontend | What naming convention should Rust reactive-frontend-framework hooks use, given no established convention exists across the ecosystem? |
| m2b1-q070 | `a-sa03-f002300-q1` | frontend | For compile-time-generated serialized data embedded via a macro (an asset descriptor built with `const` Rust and serialized at compile time), should the wire format be made valid/human-readable JSON, kept as the current bespoke binary format, or switched to an established binary serde format like postcard? |
| m2b1-q071 | `b-sb07-f002307-q1` | desktop-cli-ui;wasm | When a Rust WASM extension host hits a known-bad upstream WASI behavior (a spurious leading `/` in Windows paths from `std::env::current_dir`) that has both a correct-but-breaking extension-API fix on offer and a pragmatic non-breaking user-space workaround, should the project ship the pragmatic workaround now, or hold out for the correct breaking fix (with API versioning to preserve compatibility)? |
| m2b1-q072 | `b-sR05-f002326-q1` | embedded | should a crate's naming for a raw-pointer-plus-length accessor follow std's `raw_parts`/`from_raw_parts` convention even where the analogy is imperfect (no matching `into_raw_parts` exists here), or invent its own name when the fit is inexact? |
| m2b1-q074 | `a-sR07-f002347-q1` | core | Should code blocks embedded in Rust doc comments be required to compile as doctests, or is it acceptable to leave illustrative snippets non-compiling? |
| m2b1-q075 | `a-sa03-f002356-q1` | desktop-cli-ui | When a Rust project's forked dependency must serialize URIs per a spec that requires strict RFC3986 percent-encoding (here, LSP's `TextDocumentIdentifier`), should it use the widely-adopted `url` crate (WHATWG URL Standard, which does not percent-encode brackets) or switch to a stricter RFC3986-compliant crate like `fluent-uri`? |
| m2b1-q076 | `b-sR05-f002453-q2` | decentralized-iroh | should a public trait's methods require callers to wrap `self` in `Arc` (shared ownership baked into the API), or accept a plain reference/generic `Self` and leave ownership to the caller? |
| m2b1-q077 | `a-sa05-f002466-q1` | wasm | When a temporary/scratch register must cross a function boundary, should its safe use be enforced by the type system (dedicated types, exclusive access), or left to convention and reviewer discipline? |
| m2b1-q078 | `b-sR05-f002466-q1` | wasm | should a scratch/temporary resource that the register allocator doesn't track be exposed as an explicit function parameter (composable, flexible), or kept encapsulated with the shortest possible internal live range (safer, harder to misuse)? |
| m2b1-q079 | `b-sb08-f002517-q1` | embedded | Before a crate's 1.0 release, should an unreviewed API surface (e.g. the interrupt API) default to stable unless a blocker is raised, or stay marked unstable until the team explicitly agrees it is ready? |
| m2b1-q080 | `b-sb08-f002517-q2` | embedded | Should the proc-macro re-exports that a required language-level macro (e.g. `entry`, the crate's `main`) depends on be marked unstable along with everything else, or kept stable because the crate is unusable without them? |
| m2b1-q081 | `b-sb08-f002518-q1` | ml | Should a GPU-targeting Rust crate's build script compile device code (PTX) only for the build host's own compute capability, or build/distribute for multiple architectures to stay portable across heterogeneous multi-GPU systems? |
| m2b1-q082 | `b-sb08-f002538-q1` | web | When several related query parameters only make sense together, should an extractor treat the whole group as one optional unit (all-or-nothing), or should each field be wrapped in `Option` individually? |
| m2b1-q083 | `a-sa04-f002554-q1` | desktop-cli-ui | For an ECS relationship system, should the design enforce a single source of truth (only the `Relationship` component is authoritative, the reflected `RelationshipTarget` collection can't be populated directly), accepting that constraint in exchange for O(1) inserts and no runtime duplicate-scanning, or should both sides carry equal, symmetric authority for more flexibility at the cost of scanning/hashing to prevent duplicates? |
| m2b1-q084 | `b-sb09-f002567-q1` | ml | When adding support for a new but closely related serialization format, should the implementation start as a decoupled, dedicated design or as pragmatic duplication of the existing similar format's code, refactored later? |
| m2b1-q085 | `b-sb09-f002567-q2` | ml | When a user requests a new capability variant of an existing type (e.g. a byte-based recorder alongside a file-based one), should the library add a new dedicated type or extend the existing type via a configuration option? |
| m2b1-q086 | `b-sb09-f002615-q1` | embedded | For optional, pre-1.0 dependencies whose traits a crate implements, should the crate gate the exposure behind one coarse "unstable" feature flag, behind per-dependency (or per-dependency-version) feature flags, or simply drop the integration and re-add it only if users ask? |
| m2b1-q087 | `a-sa04-f002665-q1` | decentralized-iroh;swift-interop | When a Rust library's non-Rust-language FFI bindings lag behind the quality of its native Rust API, should maintainers keep shipping degraded bindings on every release, or pause bindings updates until the FFI/bridging story itself is fixed, accepting ecosystem-fragmentation risk in the meantime? |
| m2b1-q088 | `a-sR08-f002685-q1` | desktop-cli-ui | When an external caller drives a Rust windowing event loop via `pump_events` with a timeout, should any non-negative `Some(duration)` timeout force `ControlFlow::Poll`, or only a zero-duration timeout? |
| m2b1-q090 | `b-sR06-f002937-q1` | wasm;core | Should a fast-moving Rust ecosystem project (monthly feature releases) also commit to a formal long-term-support channel with a guaranteed multi-year security-fix window, or leave downstream stability entirely to users tracking upstream closely? |
| m2b1-q091 | `a-sa05-f003025-q1` | core;desktop-cli-ui | Should ecosystem build tooling that outgrows Cargo's scope ship as a `cargo` subcommand, or as an independent CLI / cargo-replacement? |
| m2b1-q093 | `b-sb09-f003030-q1` | embedded | When an internal Rust tool's config needs a data type (i128) that mainstream serialization-format libraries in the ecosystem don't support well, should the project pick the ecosystem-conventional format anyway and patch around the gap, narrow the type requirement to fit an existing format, or invent a custom config format? |
| m2b1-q094 | `b-sb09-f003030-q2` | embedded | Should conditional configuration logic be expressed as independent boolean-predicate rules whose interaction is implicit, or as an ordered list of rules where the first matching condition wins? |
| m2b1-q095 | `a-sR08-f003033-q1` | wasm | When defining a Wasm component's WIT world, should a function be exported directly from the world, or wrapped inside a named interface that the world then exports? |
| m2b1-q096 | `b-sb09-f003036-q1` | embedded;core | For a CLI flag guarding a destructive action where the safe default is dry-run, should the flag's naming prioritize brevity/typing convenience (default-on dry-run, `--no-dry-run` to opt out) or consistency with how sibling commands in the same tool name their flags? |
| m2b1-q097 | `b-sb09-f003052-q1` | wasm;core | When migrating a compiler backend to a new, more systematic instruction-assembler abstraction, and an instruction needs special-cased handling (e.g. custom flag-setting/printing) that the new abstraction doesn't yet cleanly support, should the PR merge the ad hoc special case now or block on designing the general mechanism first? |
| m2b1-q098 | `a-sa05-f003074-q1` | wasm | In the Component Model's GC canonical ABI, should common shapes (e.g. `null` for `none`/`error`, a boolean `i32` for a no-payload `result`) get ad hoc special-cased lowerings for efficiency, or should the ABI stick to one regular, shape-driven lowering rule per component type? |
| m2b1-q099 | `a-sa05-f003074-q2` | wasm | Should core Wasm eventually gain a primitive sum-type / tagged-union construct (with e.g. a `br_table`-like case-matching instruction), or is representing variants as `struct` subtyping trees in a shared `rec` group sufficient? |
| m2b1-q100 | `a-sR08-f003082-q1` | core;wasm | When a repeated Rust code pattern could be generated either by a declarative macro or by a plain function/derive, which should be preferred? |
| m2b1-q101 | `a-sa05-f003126-q1` | desktop-cli-ui;other | When a feature is useful but the only available implementation is algorithmically expensive (here, exponential batch count with glyph/outline count), should a game engine merge it now with documented limits, or hold it out of core until an efficient approach exists? |
| m2b1-q102 | `a-sa05-f003169-q1` | embedded | For a shared hardware resource with an enable/disable lifecycle (a radio PHY clock shared across peripherals), should safety rest on a reference-counted controller object, or on RAII-style exclusive ownership tied to the peripheral singletons themselves? |
| m2b1-q103 | `b-sb10-f003186-q1` | core;embedded | Should a crate's Cargo feature flags always be strictly additive (the crate builds with any subset of features, including none), or is it acceptable for disabling a feature (like `std`) to change what builds successfully on certain targets? |
| m2b1-q104 | `b-sb10-f003188-q1` | distributed;decentralized-iroh | Before a crate's 1.0 release, should breaking changes ship frequently in a fast pre-release ("canary") channel to get user feedback quickly, or should a team hold changes until they are fully finished before cutting each release? |
| m2b1-q106 | `b-sb10-f003222-q2` | distributed;decentralized-iroh | Given Rust has neither function overloading nor default parameter values, should optional/configurable operations expose a single `_with_opts(Options)` method (with convenience wrappers delegating to it), or another mechanism for common cases? |
| m2b1-q107 | `b-sb11-f003384-q1` | wasm | When lifting/lowering a component-model `map<K,V>` value with duplicate keys, should bindings generators be required to normalize to a defined winner (e.g. last-key-wins), should the spec instead mandate key uniqueness as an enforced boundary constraint, or should a host be permitted but not required to deduplicate, leaving the behavior non-deterministic? |
| m2b1-q108 | `b-sb11-f003384-q2` | wasm | Should the component-model `map` type guarantee iteration order (and be renamed to signal that), or should it be explicitly unordered like the hash-map types of most host languages? |
| m2b1-q109 | `a-sa06-f003414-q1` | desktop-cli-ui | When two crates cover the same need, how much should an unmaintained/flagged dependency (per RustSec) count against it versus its narrower scope fit? |
| m2b1-q110 | `a-sa06-f003414-q3` | core | Is `unwrap()` acceptable in production code, or should it be reserved for tests and provably-infallible cases? |
| m2b1-q111 | `a-sa06-f003414-q4` | desktop-cli-ui | When a function's required inputs grow, is it better to add a separate specialized function or grow one function's argument list? |
| m2b1-q112 | `b-sR08-f003531-q1` | desktop-cli-ui | Should a piece of state with more than two meaningful outcomes be represented as a bool (with special-cased checks layered around it) or as a named enum? |
| m2b1-q113 | `b-sR08-f003540-q1` | other | When adding new methods to a public trait, should you give them default implementations to avoid a breaking change, or bump the major version? |
| m2b1-q114 | `b-sR08-f003550-q1` | ml | Should a Rust practitioner follow an AI code-review tool's suggestions by default, or evaluate them critically before acting? |
| m2b1-q115 | `a-sa06-f003558-q1` | wasm | Facing the absence of a proper Web-WASM Rust target, should the ecosystem work around it now with crate-feature plumbing, or push to get the target itself built first? |
| m2b1-q116 | `a-sa06-f003558-q2` | wasm | When an opt-in crate feature can be misused by downstream crates (enabled unconditionally "for convenience"), is it the exposing crate's job to structure the API/placement to make misuse harder, or the misusing crate's bug to fix? |
| m2b1-q117 | `a-sR08-f003580-q1` | distributed;core | Should a Rust vectorized query engine process rows fully sequentially in large batches (cache-friendly, low interpretation overhead), fully in parallel per-row, or partition data into parallel batched streams? |
| m2b1-q118 | `b-sR08-f003587-q1` | ml;embedded | Which serialization format should a Rust library pick for a data format that needs no-std support? |
| m2b1-q119 | `b-sR08-f003587-q2` | ml | Should a method be named `into_foo` only when it actually consumes `self` (Rust's `into_`/`as_`/`to_` naming convention), or can `into_` be used more loosely? |
| m2b1-q120 | `b-sR08-f003587-q3` | ml | At an API boundary where allocation strategy matters (e.g. future backend-managed/pinned memory), should owned byte buffers be typed as `Vec<u8>` or a custom wrapper type? |
| m2b1-q121 | `a-sa06-f003590-q1` | decentralized-iroh | Should an RPC failure response be a `Result<T, E>` carrying a detailed error, or a flat enum exposing only coarse, intentionally limited outcomes? |
| m2b1-q122 | `a-sa06-f003590-q2` | decentralized-iroh | For a protocol meant to stay wire-compatible long-term, is a compact non-self-describing ordinal format (postcard) an acceptable choice, and what does using it commit you to? |
| m2b1-q123 | `a-sR09-f003702-q1` | decentralized-iroh;core | When a crate's public API doesn't support an operation needed for performance (here, batch-hashing many small blobs with BLAKE3's SIMD `hash_many`), should a practitioner reach into the crate's internal/"hazmat" API and accept unchecked, precondition-violating footguns (silently wrong results rather than a panic on some platforms) for a large speedup, or stay within the safe public API and accept lower throughput? |
| m2b1-q124 | `b-sR08-f003702-q1` | decentralized-iroh;ml | When batch-hashing many small blobs (or a similar compute-bound batch workload), should you use thread-level parallelism (rayon), instruction-level parallelism (SIMD), or both, and when does each apply? |
| m2b1-q125 | `a-sa07-f003704-q1` | ml;core | Should a processing pipeline use runtime type erasure with up/down-casting, or a compile-time associated type on the processing trait? |
| m2b1-q126 | `a-sa07-f003704-q2` | ml;core | Should a bounded, safety-first multi-pass graph algorithm favor a simple iterative fixed-point loop, or a more complex event-driven re-trigger design? |
| m2b1-q128 | `a-sa07-f003704-q4` | ml;core | Should a struct under construction hold a lifetime-bound reference into shared mutable build state, or should construction use a builder consumed into an immutable owned structure? |
| m2b1-q129 | `a-sa07-f003716-q1` | core | When a trait's correct implementation is required for memory safety, should the trait itself be marked `unsafe`, or should the unsafe boundary sit on the consuming method instead? |
| m2b1-q130 | `a-sa07-f003716-q2` | core | Should a value that can be one of two related-but-distinct kinds be modeled as one enum with variant matching, or split into two separate types? |
| m2b1-q131 | `b-sR08-f003731-q1` | decentralized-iroh | When a type may need to represent additional variants in the future (e.g. new transport kinds), should it be modeled as a `#[non_exhaustive]` enum of variants, or as a struct with independent optional fields per kind? |
| m2b1-q132 | `b-sR08-f003731-q2` | decentralized-iroh | Should a library perform a broad breaking rename across its whole public API to align vocabulary with its current mental model, or keep legacy names for compatibility? |
| m2b1-q133 | `b-sR09-f003815-q1` | wasm | once a `.wasm` file is already fully loaded into memory as bytes/a blob, should the loader still route it through the streaming compile/instantiate API, or fall back to the plain bytes-based `instantiate`? |
| m2b1-q134 | `a-sa07-f003922-q1` | wasm;cloud-workers;distributed | Should agent tool implementations couple to a specific language's SDK and calling runtime, or be built as portable WebAssembly components composed independently of language and runtime? |
| m2b1-q135 | `b-sR09-f003938-q1` | frontend | should a component-templating macro (like Yew's `html!`) support native imperative control flow (`for`, `if`) written inline, or require iterator-adapter/functional-expression style? |
| m2b1-q136 | `b-sR09-f003955-q1` | embedded | should a new chip-family HAL be merged into the monorepo immediately as its own separate crate to unblock waiting users, or held back until it can be integrated into the unified/combined HAL from the start? |
| m2b1-q137 | `b-sb13-f003963-q1` | frontend | When a reactive container's parent field is written as a whole (replaced or patched), should the reactivity system notify all of its keyed-child subscriptions by default (accepting some unnecessary re-notifications), or should notification require writing through the specific keyed accessor (precise, but silently misses updates if the user writes the parent instead)? |
| m2b1-q138 | `b-sb13-f003963-q2` | frontend | Should a keyed-collection access API constrain key types to `Copy` (cheaper, but excludes types like `Arc<str>`), or accept `Clone` key types for flexibility at the cost of occasional clone overhead? |
| m2b1-q139 | `a-sR11-f003983-q1` | ml;core | When a macro-generated code path (e.g. `#[tracing::instrument]` reaching a value only through a trait method) triggers a false-positive unused/dead-code lint, should the fix be a broad `#![allow(unused)]` or a narrowly scoped allow on the specific item? |
| m2b1-q140 | `a-sR11-f003983-q2` | ml;distributed | When two operations are logically distinct (a local op returning a `Tensor` vs. a collective op returning a `{PeerId: Tensor}` map) but share underlying logic, should the crate share code via a combinator abstraction or keep them separately implemented? |
| m2b1-q141 | `a-sa09-f004016-q1` | core;ml | Should a Rust OSS framework monetize by gating features behind a paywall, or by building a complementary paid layer (e.g. a hosted cloud/training service) on top of a fully-featured open core? |
| m2b1-q142 | `a-sa09-f004016-q2` | ml | Can one compute framework abstract kernel programming over both GPU and CPU without sacrificing performance, or does hardware-portable abstraction necessarily cost performance versus a hardware-specific implementation? |
| m2b1-q143 | `a-sa09-f004055-q1` | embedded | When a temporary/scratch register must cross a function boundary, should its safe use be enforced by the type system (dedicated types, exclusive access), or left to convention and reviewer discipline? — recurs here as: should peripheral registers be manipulated through typed PAC accessors, or through raw/manual volatile bit operations? |
| m2b1-q144 | `a-sa09-f004055-q2` | embedded | Should an SPI driver expose hardware chip-select (CS) control as part of the embedded-hal `SpiBus` trait, or restrict `SpiBus` to software/GPIO-controlled CS and handle hardware CS separately? |
| m2b1-q145 | `a-sa09-f004055-q3` | embedded;core | For an operation whose safety depends on a runtime-checkable condition (e.g. whether a DMA buffer sits in DMA-accessible memory), should the API perform the check and return a `Result`, or expose the operation as `unsafe`/panicking and push validation onto the caller? |
| m2b1-q146 | `b-sb13-f004160-q1` | embedded | When a new profiling/debugging feature needs stack unwinding, should it reuse and refactor the codebase's existing general-purpose unwind implementation (more consistent, avoids duplicated maintenance) even where that path is much slower, or should it ship a separate, purpose-built implementation optimized for the feature's own constraints (faster, but duplicates unwind logic)? |
| m2b1-q147 | `b-sb13-f004160-q2` | embedded | Should a CLI tool that repeatedly writes an output file overwrite the same filename by default (simpler, faster iteration, matches a peer tool's behavior), or auto-generate a timestamped filename by default to avoid silently discarding a previous result? |
| m2b1-q148 | `a-sa11-f004265-q1` | embedded | When a fixed-size array (e.g. `[u8; 6]`) might later need to hold a same-shaped but larger variant (e.g. an 8-byte IEEE MAC), should the API expose the array type directly, or return a slice / wrap it in a dedicated type to keep the door open? |
| m2b1-q149 | `a-sa11-f004265-q2` | embedded | When you can foresee wanting another blanket `From` impl for a type later, should you add related conversions now speculatively, or hold off to avoid a breaking compile error for downstream users when you do add it? |
| m2b1-q150 | `a-sa11-f004265-q3` | embedded | For a small, always-internally-constructed validated type, should the public API expose fallible external construction, or restrict construction entirely to the crate's own internals? |
| m2b1-q151 | `b-sb13-f004367-q1` | frontend | For a Rust/WASM frontend framework's end-to-end tests, should the harness be pure Rust (`wasm-bindgen-test`) to avoid non-Rust toolchain dependencies, or should it adopt an established JS-ecosystem E2E framework (Playwright/Cypress/Selenium) for richer capabilities such as visual-regression testing? |
| m2b1-q152 | `b-sb14-f004398-q1` | core | When a public API wraps a `Box<dyn Fn>` behind a required constructor function, should the wrapped closure live in an unnamed tuple-struct field or a named field, given that a constructor already replaces the field's main ergonomic argument (avoiding `Box::new` at call sites)? |
| m2b1-q153 | `b-sb14-f004398-q2` | core | For a component that triggers on a state-machine transition matching a predicate, should a transition into the same state the entity is already in be treated as a no-op (never triggering), or should it be allowed to trigger, to support "reload" style use cases? |
| m2b1-q154 | `b-sb14-f004399-q1` | web;frontend;wasm | When migrating a documentation/blog site's content out of a JS-based static-site generator's Markdown-derivative format, should the content be authored directly as Rust source (a DSL enabling compile-time link validation and cross-version deduplication) or kept close to Markdown for editor tooling and authoring ergonomics, with a lighter embedding mechanism for interactive components? |
| m2b1-q157 | `a-sa11-f004471-q1` | embedded | When targeting an unusual/constrained platform where the standard C-backed crypto backend won't build, is it acceptable to reach for a pure-Rust crypto implementation as a stopgap, even knowing a hardware-accelerated backend would be the "right" choice for production? |
| m2b1-q158 | `a-sa11-f004512-q1` | embedded | When converting a raw pointer to an integer for a low-level hook/tracking API, should you cast with `as usize` or use the provenance-preserving `.addr()`? |
| m2b1-q159 | `a-sa11-f004512-q2` | embedded | Should a low-level allocator-hook API pass the raw pointer type (`*mut u8`) through to callbacks, or reduce it to an address (`usize`) since only the address is needed? |
| m2b1-q160 | `a-sa11-f004512-q3` | embedded | When shipping a small utility feature quickly, is it worth adding ergonomic sugar (a macro/trait wrapper) around the raw mechanism, or should that wait until it's shown to carry its weight? |
| m2b1-q161 | `a-sa11-f004512-q4` | embedded | Should a feature's name describe only the literal mechanism it provides, or the higher-level capability that mechanism enables, when the feature itself is just the low-level primitive? |
| m2b1-q163 | `b-sR10-f004573-q2` | ml;core | When a generic numeric algorithm needs a per-dtype constant (e.g. a singularity epsilon), should the value be hardcoded via an exhaustive match on the dtype, or derived generically from the type's own metadata (a trait method)? |
| m2b1-q164 | `a-sR13-f004586-q1` | decentralized-iroh;core | Should a Rust networking crate hard-depend on one crypto/TLS backend, or expose the backend as a pluggable provider? |
| m2b1-q165 | `a-sR13-f004586-q2` | decentralized-iroh;core | Should public enums/structs in an API heading toward 1.0 default to `#[non_exhaustive]`, accepting the forced wildcard match arm it imposes on callers? |
| m2b1-q166 | `a-sR13-f004586-q3` | decentralized-iroh;distributed | Should an async network server reject invalid/unauthenticated incoming connections before or after the handshake completes? |
| m2b1-q167 | `a-sa12-f004598-q1` | wasm;cloud-workers | For Rust compiled to WebAssembly (wasm32-unknown-unknown), should panics use the platform default of panic=abort, or panic=unwind (running destructors and preserving instance state across a single failed request)? |
| m2b1-q168 | `a-sa12-f004598-q2` | wasm;cloud-workers | When an FFI/Wasm boundary must distinguish recoverable foreign exceptions from unrecoverable aborts, should the recoverable (unwind) case be explicitly tagged, or the unrecoverable (abort) case? |
| m2b1-q169 | `a-sa12-f004637-q1` | web;core | When a response body's size cannot be determined without expensive computation, should an HTTP framework represent that as a distinct "unknown size" state, or default to treating it the same as a known-empty body? |
| m2b1-q170 | `a-sR13-f004685-q1` | decentralized-iroh;core | Should a Rust crate's live-state accessor and its change-notification stream be one overloaded API or two separate primitives? |
| m2b1-q172 | `b-sR10-f004706-q1` | web;frontend;core | When an expected embedded resource (e.g. a static asset) is missing, should the framework fail the build, or degrade silently at runtime (e.g. serve a 404)? |
| m2b1-q174 | `b-sR10-f004741-q3` | decentralized-iroh;distributed;core | Should an extensible policy/configuration surface (e.g. connection access control) be expressed as a closed enum, or as an open trait? |
| m2b1-q175 | `a-sa13-f004772-q1` | desktop-cli-ui | When a UI component needs asynchronously-fetched data to render, should that data live in a cache on a shared owner object (populated by a hover/eager prefetch, read synchronously at render), or should the component itself own the async fetch and render a loading state until it resolves? |
| m2b1-q176 | `a-sa13-f004772-q2` | desktop-cli-ui;core | Should a test exercise a feature only by calling its internal methods directly against a bespoke test harness, or must at least one test dispatch the real keystroke/action through the actual UI entry point? |
| m2b1-q177 | `a-sa13-f004772-q3` | core;desktop-cli-ui | Should code carry comments that narrate what a simple, self-evident line or private helper does, or should comments be reserved for non-obvious rationale, with narrating comments treated as noise to remove? |
| m2b1-q178 | `b-sR10-f004804-q1` | embedded;core | When a type wraps an unsafe operation and is labeled "safe," must that safety guarantee hold under every generic instantiation/composition, or is a narrower guarantee acceptable if the common case is sound? |
| m2b1-q179 | `b-sR10-f004804-q2` | embedded;core | Should a macro hide an API's less-friendly construction requirements from the user, or should the API stay explicit even if less ergonomic? |
| m2b1-q180 | `b-sR10-f004809-q1` | wasm;cloud-workers;web | Should a framework's host/runtime interfaces be async by default, or should async stay an opt-in path alongside a synchronous default? |
| m2b1-q181 | `b-sR10-f004809-q2` | wasm;cloud-workers | Under a concurrent-instance execution model, should shared state use global statics/OnceCell, or be scoped per-request with explicit synchronization? |
| m2b1-q182 | `a-sR14-f004865-q1` | embedded | Cargo project layout when combining a host crate and an embedded/different-toolchain crate |
| m2b1-q183 | `a-sR14-f004865-q2` | web;embedded | how much review AI-written code needs before shipping it, for code outside the author's own expertise |
| m2b1-q184 | `a-sa14-f004947-q1` | desktop-cli-ui | For a niche, protocol-specific CLI tool, should its flags follow the conventions of an already-familiar general-purpose tool (curl), or be designed fresh around the tool's own domain? |
| m2b1-q185 | `b-sR11-f004947-q1` | desktop-cli-ui | Should a debugging CLI for a protocol specialize narrowly, one tool per protocol, or bundle several related protocols into one tool? |
| m2b1-q186 | `b-sR11-f004960-q1` | decentralized-iroh | Should a networking library dictate a specific authentication scheme for its own infrastructure, or stay unopinionated and let operators build their own? |
| m2b1-q187 | `a-sa14-f004985-q1` | wasm;cloud-workers | When compiling C/C++/Rust code to WebAssembly for a serverless runtime, should you go through an emulation layer like Emscripten, or compile natively from Rust straight to Wasm? |
| m2b1-q188 | `a-sa14-f004985-q2` | wasm;cloud-workers | When a needed capability (like `eval`) isn't natively supported by the host platform, is it acceptable to run a full interpreter for that capability inside your own Rust-compiled Wasm module as a stopgap, even though it means "a runtime on top of a runtime"? |
| m2b1-q189 | `b-sR11-f004993-q2` | core | How should an open-source Rust project's priorities be decided and communicated to its community? |
| m2b1-q190 | `b-sb16-f004997-q1` | embedded | When using an LLM to bring doc-comment prose in a codebase to a consistent style, should the project make the process reproducible by pinning down and declaring exactly which model, prompt, and environment produced the edits, or should it instead adopt a formal controlled-language writing standard that constrains vocabulary/grammar enough to make the model's "taste" mostly irrelevant? |
| m2b1-q191 | `b-sb16-f005000-q1` | wasm;core | When a runtime needs to expose a narrow debugging capability that would be most efficient as a purpose-built accessor coupled to internal layout details, should the maintainers accept that coupled accessor (even once made asymptotically efficient), or insist on a smaller, decoupled, general-purpose primitive that pushes the assembling logic (and any inefficiency) out to the caller? |
| m2b1-q192 | `b-sb16-f005000-q2` | wasm;core | When a wrapper/handle type's "true" identity requires dereferencing store-owned state that isn't safely reachable from the handle alone, should identity comparison be implemented as the standard `PartialEq`/`Eq`/`Hash` traits on the bare handle, or as separate methods that take an explicit store borrow? |
| m2b1-q193 | `b-sR11-f005050-q1` | wasm | Should a Wasm component sandbox grant capabilities by default (ambient authority), or require every capability — including for middleware and dependencies — to be explicitly listed? |
| m2b1-q194 | `b-sR11-f005050-q2` | wasm | When retiring a legacy compatibility path, should maintainers break it immediately or deprecate it gradually with warnings? |
| m2b1-q195 | `b-sR11-f005053-q1` | wasm | Within one Wasm application, should logic be kept in a single monolithic component, or decoupled into several small components composed via WIT interfaces? |
| m2b1-q196 | `b-sR11-f005071-q1` | distributed | For a multi-actor collaborative system (humans and agents editing together), should convergence come from CRDTs or from a coordinating mechanism (locking, operational transform, a single authoritative server)? |
| m2b1-q197 | `a-sa14-f005079-q1` | core | When an operation must run before any other file descriptor could occupy a reused slot (an I/O-safety hazard), must it happen at the very start of `main()`, or is "early enough, with nothing intervening" sufficient? |
| m2b1-q198 | `a-sa14-f005079-q3` | core | For low-level syscall-adjacent operations (fcntl, fstat, getsockname, socket options), should code call into libc directly with manual unsafe blocks, or use a safe-wrapper crate? |
| m2b1-q199 | `a-sa14-f005079-q5` | core | When a caller's input is ambiguous or partially satisfiable (multiple matching sockets, or a requested feature with no usable input at all), should the code silently proceed with a plausible default, or fail with an explicit error? |
| m2b1-q200 | `b-sR12-f005085-q1` | ml;core | Should a safety/dense-storage invariant that several call sites rely on be duplicated inline as ad hoc boolean expressions, or encapsulated as one named method on the owning type that states the contract? |
| m2b1-q201 | `b-sR12-f005085-q2` | ml;core | When several hand-written data structures are near-duplicate specializations differing only by array length/arity (e.g. a 2-stride vs. 3-stride zip), should they be unified into one type parameterized by a const generic, or kept as separate hand-specialized versions? |
| m2b1-q202 | `b-sb17-f005113-q1` | distributed | When a struct's fields need a smaller in-memory footprint than natural alignment would otherwise give, should Rust code use `#[repr(packed)]` to force the tight layout (concise, but taking a reference to a misaligned field is undefined behavior), or should it store the fields packed into a raw byte array and expose them through typed accessor methods (safer, more verbose, same codegen)? |
| m2b1-q203 | `b-sR12-f005120-q2` | ml;core | In a hot loop, should working memory be a caller-owned scratch buffer reused across calls, or freshly allocated per call for simplicity? |
| m2b1-q204 | `b-sb17-f005144-q1` | frontend | Should a Rust UI/reactive framework model component state with borrow-checker-scoped lifetimes tied to the component (arena/bump allocation: zero-clone access in event handlers, but confusing lifetime errors and incompatible with `'static` futures), or with a runtime-tracked `Copy` handle backed by generational/GC-like reclamation (uniform across closures, futures and threads, at the cost of adding a small runtime-tracking layer)? |
| m2b1-q205 | `a-sa14-f005149-q2` | core | Should error enums be scoped per-module (one large enum for everything a module can fail at), or per-function/operation (smaller, descriptively-named enums scoped to what one call can fail at)? |
| m2b1-q206 | `a-sa14-f005149-q3` | core | Should a public trait's associated error type be a closed, fully-enumerated set of variants, or include an open "custom"/user-extension variant so third-party implementors can propagate their own errors? |
| m2b1-q208 | `b-sb17-f005159-q3` | decentralized-iroh | Should a Rust library depend on the mainline `futures` crate for complex combinators (e.g. `FuturesUnordered`) despite known bugs in that unsafe-heavy code, or should it avoid `futures` altogether and assemble the needed functionality from several smaller alternative crates (futures-lite, futures-buffered, futures-util) at the cost of ergonomics and discoverability? |
| m2b1-q209 | `b-sb17-f005159-q4` | decentralized-iroh | For an async mpmc channel crossing the sync/async boundary, should cancel-safety on `recv` be treated as a non-negotiable requirement (ruling out otherwise-attractive crates like flume), or is losing cancel-safety on send/recv an acceptable tradeoff for performance or maturity? |
| m2b1-q210 | `b-sb17-f005159-q5` | decentralized-iroh | Should Tokio's `spawn`, when the task's result isn't otherwise needed, routinely be fire-and-forget with the `JoinHandle` dropped (Tokio's own examples do this), or should every spawned task's `JoinHandle`/`JoinSet` be retained and polled so a panic inside it is never silently swallowed? |
| m2b1-q211 | `a-sa14-f005162-q1` | embedded | In embedded/no_std logging, should you format and print human-readable strings at the point of use, or defer formatting to the host by sending compact binary tokens and decoding off-device? |
| m2b1-q212 | `b-sR12-f005169-q1` | embedded;core | How should a Rust project statically verify a property like "this function never panics" or "this function never calls unvalidated code" across a codebase: clippy lints, a new effect-type system, a link-time hack, a cfg-forked standard library, or a custom compiler driver? |
| m2b1-q213 | `a-sR14-f005287-q1` | core | should crates.io-published bytes be checked against their source repository, and should such findings be released even incomplete |
| m2b1-q214 | `b-sb18-f005307-q1` | distributed;decentralized-iroh | When your chosen async I/O library (e.g. quinn for QUIC) is paired with a storage/database layer that only offers a synchronous API (as with embedded databases like redb, rocksdb, sled, sqlite), should you treat that combination as an avoidable architecture mismatch to design around from the outset — including avoiding constructs like `LocalSet` and `!Send` futures — or accept it as a practical necessity, since no viable async-native alternative exists and non-`Send` futures are often unavoidable when wrapping such resources? |
| m2b1-q215 | `b-sb18-f005307-q2` | distributed;decentralized-iroh | Is it acceptable practice to run blocking synchronous I/O (e.g. database calls) inside a dedicated single-threaded ("current_thread") Tokio runtime on its own OS thread, or does limiting a Tokio runtime to a single thread carry negative internal ramifications that make this an anti-pattern except when no other OS threads are available? |
| m2b1-q216 | `b-sb18-f005332-q1` | core;embedded | When a C-subsystem maintainer changes their C code in a way that breaks the corresponding Rust abstraction/bindings, should the C maintainer be expected to help keep the Rust side correct (or at least not block small Rust-motivated robustness fixes to the C code), or is it legitimate for C maintainers to fix only their own C code and decline responsibility for Rust bindings entirely? |
| m2b1-q217 | `a-saL1-f005360-q1` | web;distributed;core | Does using Rust to embed a full HTTP server as an in-process library (rather than nginx-style multi-process isolation) represent a genuinely new capability, or is the "safe language vs. dangerous C" framing overstated since C-based servers already work fine? |
| m2b1-q218 | `a-saL1-f005360-q2` | distributed;embedded;core | Does Rust's memory safety meaningfully substitute for hardware/OS-level address-space isolation when running untrusted or mutually adversarial code in one process (single-address-space "libOS" designs)? |
| m2b1-q219 | `a-saL1-f005360-q3` | web;cloud-workers;core | Is async Rust (Tokio-based web stacks) production-competitive with mature C-based servers like nginx "out of the box," or does the higher-level framework layer (e.g. Axum) add meaningful overhead that needs bypassing for performance? |
| m2b1-q222 | `a-saL1-f005516-q1` | core | Is there an inherent language-level reason for Rust or C to be faster than the other, or does performance mainly reflect non-language factors (codebase age, engineering effort, ecosystem defaults) — and separately, does Rust's stronger type system (aliasing guarantees) let the compiler apply optimizations C cannot, or do Rust's own runtime costs offset that in practice? |
| m2b1-q223 | `a-saL1-f005516-q2` | core | Does old, long-maintained C code tend to be more optimized and reliable ("battle-tested") than newer Rust code simply because of its age? |
| m2b1-q224 | `a-saL1-f005516-q3` | core;embedded | Does safe Rust's requirement that values be initialized at construction time (rather than only before use, as C dataflow allows) impose a real, measurable performance cost — e.g. unnecessary zero-initialization in large arrays or small-object allocators? |
| m2b1-q225 | `a-saL1-f005516-q4` | core | Does Rust's composability (safe abstraction over data structures) let engineers actually ship better-optimized designs in practice than they would dare hand-roll in C, or does the borrow checker's own friction (forced refactors, defensive clones/`Rc`) offset that advantage? |
| m2b1-q227 | `a-sa15-f005604-q1` | distributed;web | When several internal Rust services need similar network-framework capabilities, should the org consolidate them into one shared framework built on existing async-ecosystem crates, or keep purpose-built frameworks separate even at the cost of overlap? |
| m2b1-q228 | `b-sR12-f005668-q1` | swift-interop;core | Should a language's memory-model default favor explicitness/performance (opt into convenience, as Rust's move/borrow-by-default with Cow/Rc as opt-in) or convenience (opt into performance, as Swift's copy-on-write-by-default with ownership as opt-in)? |
| m2b1-q229 | `b-sR12-f005668-q2` | swift-interop;core | Should indirection for a recursive data type be explicit (the programmer writes `Box<T>`) or implicit (a compiler-inferred/annotated indirection, as Swift's `indirect` keyword)? |
| m2b1-q230 | `b-sb19-f005691-q1` | wasm;frontend | When wrapping Rust types for wasm-bindgen, should a practitioner write manual `js_sys` conversions or lean into bindgen's generated glue (accepting its naming/wrapper conventions)? |
| m2b1-q231 | `a-sR14-f005702-q1` | web;frontend | should a Rust web UI framework use fine-grained (signal-based) reactivity or virtual-DOM diffing |
| m2b1-q232 | `b-sb19-f005743-q1` | core | Is adopting a memory-safe language (Rust) a moral imperative, or an engineering/economic tradeoff decision like any other? |
| m2b1-q233 | `b-sb19-f005743-q2` | core | Does Rust's affine-type system provide sufficient correctness guarantees, or is further formal verification (linear/dependent types, model checkers) needed on top of it? |
| m2b1-q234 | `b-sb19-f005743-q3` | core | Is "memory safety" the right frame for language-correctness discourse, or is "correctness" (of which memory safety is one part) the property that actually matters? |
| m2b1-q235 | `b-sb19-f005743-q4` | core | Does Rust's toolchain-bootstrapping trust gap (rustc's own build chain depending on prior binaries/other compilers) undermine memory-safety arguments for adopting it? |
| m2b1-q236 | `b-sb19-f005743-q5` | core | Should the Rust project prioritize speed of consensus / shipping over slower, more inclusive decision-making (e.g. long-nightly-gated APIs, stabilization pace)? |
| m2b1-q237 | `a-sa15-f005821-q1` | core;wasm | Does Rust's nightly `become` tail-call feature produce reliably good codegen across targets, or is it currently good on some architectures and poor on others? |
| m2b1-q238 | `a-sa15-f005821-q2` | core | When a project's code is partly produced with LLM assistance in earlier iterations, should a specific piece of performance-critical work be held to a "human-written only" personal standard? |
| m2b1-q239 | `b-sb19-f005836-q1` | core | To persist Rust objects across process/container restarts, should a practitioner build a custom raw-memory `Allocator` (memfd + systemd FD store + mmap) rather than serializing state to an external store (file/Redis) on shutdown/startup? |
| m2b1-q240 | `b-sb19-f005836-q2` | core | Should Rust types that back raw/mmap'd persistent memory declare `#[repr(C)]`, given Rust makes no default layout guarantee across compiler/binary versions? |
| m2b1-q241 | `a-sa15-f005857-q1` | desktop-cli-ui | For a real-time, stateful interactive Rust desktop app (synchronized audio playback + canvas redraw + UI), is a message-passing/subscription (Elm-style) GUI architecture the better fit over an immediate-mode one? |
| m2b1-q242 | `b-sb19-f005872-q1` | web | Should the Rust web ecosystem offer a monolithic, batteries-included framework (Django/Rails-style: routing, templates, auth, ORM, admin, hot reload) rather than the current "wire minimalist libraries yourself" norm (actix-web, axum, Leptos, Yew, Dioxus)? |
| m2b1-q245 | `b-sb19-f007042-q1` | cloud-workers | Is Rust worth its steeper learning curve for AWS Lambda/serverless functions, compared to interpreted languages (Python, JavaScript)? |
| m2b1-q246 | `a-sa16-f007175-q1` | core | Should optional/alternate implementations in a Rust library be selected via Cargo feature flags, or via generic type-level component wiring (traits/generics, e.g. CGP-style)? |
| m2b1-q247 | `a-sa16-f007175-q2` | desktop-cli-ui;core | Is hosting a Rust DSL's programs as compile-time types (zero runtime cost, no dynamic loading) worth trading away runtime-loaded/dynamic DSL programs? |
| m2b1-q248 | `b-sb19-f007207-q1` | core | Should Rust add "fields in traits" (a shared field, accessed through a vtable offset on `dyn Trait`, that every implementor must provide)? |
| m2b1-q249 | `b-sb19-f007207-q2` | core | Should Rust support "properties" (field-access syntax that silently compiles to a getter/setter method call, as in Python/C#/Swift)? |
| m2b1-q250 | `b-sb19-f007207-q3` | core | Should Rust's borrow checker be extended to natively support safe self-referential structs, instead of requiring `unsafe`/`Pin`/crates like `ouroboros`? |
| m2b1-q251 | `b-sb20-f007213-q1` | core | when a type needs specialization-like behavior (methods gated on stronger trait bounds, e.g. `Read+Write+Seek` vs `Read+Seek`) but Rust's real specialization is unstable, do you fake it with a runtime-checked field set from trait-bound-gated impl blocks, or reach for a different pattern entirely? |
| m2b1-q252 | `b-sb20-f007290-q1` | frontend;wasm | is Rust (via a fullstack WASM framework like Dioxus) ready to replace JavaScript/TypeScript frameworks for frontend and fullstack web development? |
| m2b1-q253 | `b-sb20-f007290-q2` | frontend;web | is the complexity practitioners feel in fullstack reactive frameworks (hooks, effects, suspense, hydration mismatches) accidental complexity added by the framework, or essential complexity inherent to the fullstack problem itself? |
| m2b1-q254 | `b-sb20-f007290-q3` | wasm;frontend | when a WASM framework offers hot-patching (fast, stateful code reload) that is incompatible with DWARF-based native debugging, should a practitioner enable hot-patching during development anyway? |
| m2b1-q255 | `a-sR14-f007341-q1` | web | how much defensive engineering (RAII/type-level guards) is warranted against a failure mode judged unlikely to occur in practice |
| m2b1-q257 | `a-sa16-f007483-q1` | desktop-cli-ui;embedded;wasm;core | How should a Rust application implement a plugin system: native dynamic libraries, an embedded scripting language, WebAssembly, or an expression/rules engine? |
| m2b1-q264 | `b-sR13-f007973-q1` | core;desktop-cli-ui | Should Rust developers write parsers with a combinator library (nom) rather than a grammar-based generator (pest, lalrpop) or a hand-rolled recursive-descent parser? |
| m2b1-q265 | `a-sa17-f008217-q1` | embedded | In an embedded OS kernel, should crash-recovery policy (restart strategy, backoff, giving up) be hardcoded into the kernel, or left to an application-defined supervisor task? |
| m2b1-q266 | `a-sa17-f008217-q2` | embedded | In safety/crash-sensitive embedded Rust, should panics be eliminated for a given task at compile time, or tolerated and handled via runtime crash recovery? |
| m2b1-q267 | `a-sR15-f008241-q1` | core;web | When an allocation-avoiding type like `Cow<str>` would only save a negligible amount of work, should a Rust programmer still prefer it over a plain `String`, for the sake of making allocations visible in the code? |
| m2b1-q268 | `a-sR15-f008241-q2` | core | Does a language's built-in, first-party package manager (like Cargo) meaningfully change engineering practice compared to bolted-on/ecosystem-only dependency management (as in C/C++)? |
| m2b1-q269 | `a-sa18-f008389-q1` | swift-interop | When a Rust core pushes state changes across an FFI boundary to a declarative native UI (e.g. SwiftUI), should the boundary API return full/partial state snapshots for the UI to diff, or should the Rust side track and emit only the changed fields itself? |
| m2b1-q270 | `b-sb21-f008390-q1` | desktop-cli-ui;frontend | For a Rust desktop app that needs a web-capable UI, should the frontend logic stay in the same Rust execution context as the backend (Dioxus-style, calling straight into the WebView glue), or should it run as an independent frontend runtime talking to a host process over a serialized IPC boundary (Tauri's architecture)? |
| m2b1-q271 | `b-sb21-f008390-q2` | desktop-cli-ui | Should a Rust GUI framework define UI structure through a bespoke DSL with dedicated tooling (Slint's own language, Makepad's `live_design!` macro), or should it stick to plain Rust code with no macros/DSL (egui's immediate-mode API)? |
| m2b1-q272 | `b-sb21-f008390-q3` | desktop-cli-ui | For typical small-to-medium desktop UIs, does the immediate-mode vs. retained-mode GUI architecture choice actually matter, or is it a difference that only shows up at larger scale? |
| m2b1-q273 | `b-sb21-f008390-q4` | desktop-cli-ui | When choosing or building a Rust GUI framework, should Windows support and screen-reader/IME accessibility be treated as a first-class, load-bearing requirement rather than an afterthought? |
| m2b1-q274 | `b-sb21-f008396-q1` | core | For a hand-built async I/O reactor on Linux, should you build the readiness-notification layer on `epoll` (mature, stable) or on `io_uring` (newer, potentially faster but more experimental)? |
| m2b1-q276 | `a-sa18-f008651-q1` | web;core | In a layered Rust service architecture, does splitting the repository layer into per-tenant/per-domain sub-crates (a crate boundary as an added abstraction layer) pay for itself in encapsulation and reuse, or is it unneeded indirection? |
| m2b1-q277 | `a-sa18-f008694-q1` | core | Should the Rust compiler's/Cargo's incremental-rebuild invalidation be redesigned around explicit "atomic level" targets (AST/HIR/MIR/codegen) plus separately-tracked data dependencies (e.g. codegen flags), instead of today's coarser per-flag/per-command invalidation? |
| m2b1-q278 | `a-sa18-f008787-q1` | ml;embedded;desktop-cli-ui;wasm | For offline/edge ML inference (no cloud connectivity, consumer hardware), is a Rust-based stack (Burn) a viable or superior alternative to the default Python/PyTorch stack, despite Python's ecosystem dominance for training? |
| m2b1-q279 | `b-sb21-f008793-q1` | swift-interop | For iOS UI testing, should a Rust practitioner write the test harness directly in Rust via `objc2`/`objc2-xc-test`/`objc2-xc-ui-automation` bindings (bypassing the standard Xcode-project/Swift XCTest workflow entirely), or stay on the standard Swift-based XCTest setup? |
| m2b1-q280 | `b-sR13-f008801-q1` | core | Should Rust's collections behave like true persistent (structural-sharing) values with cheap clone, rather than accepting the current model where clone is a full deep copy? |
| m2b1-q281 | `b-sb21-f008808-q1` | ml | For structured concurrent GPU programming, is it better to reuse an existing general-purpose language's async/await abstraction (Rust's `Future`/async-await) than to adopt a purpose-built DSL/compiler stack (JAX, Triton, NVIDIA CUDA Tile)? |
| m2b1-q282 | `b-sb22-f008906-q2` | core;cloud-workers | when a tower `Service::call` needs to inspect or transform the response after the inner future resolves, should its associated `Future` be a boxed dynamic future (`Pin<Box<dyn Future<...> + Send>>`, built with `Box::pin(async move {...})`), or a hand-written `poll`-driven future struct (via `pin-project`) that avoids the heap allocation? |
| m2b1-q283 | `b-sb22-f008906-q4` | cloud-workers;distributed | should a reusable rate-limiting middleware, on hitting its limit or losing its backing store, return a descriptive typed `Err` and trust the caller's outer layers to translate it into an HTTP response, or short-circuit itself with a pre-baked `Ok(response)` (429/503)? |
| m2b1-q284 | `b-sb22-f008906-q5` | distributed;cloud-workers | for a rate limiter, should you use a fixed-window counter, a token bucket, or a sliding window? |
| m2b1-q285 | `b-sb22-f008906-q6` | cloud-workers | should per-IP/per-user rate limiting on a Lambda-fronted API be built as custom middleware, or left to API Gateway usage plans? |
| m2b1-q286 | `a-sa18-f009026-q1` | distributed;web;cloud-workers | For async Rust HTTP servers, is a work-stealing runtime (Tokio's default) or an executor-per-thread/"thread-per-core" runtime (Glommio, or Tokio/Smol configured with a `LocalRuntime`/`LocalExecutor` per thread) the better architecture — and is either one simply faster, or is the right choice workload-dependent? |
| m2b1-q287 | `b-sb22-f009062-q1` | wasm | when the goal is running an existing, unmodified Rust/Linux program (with threads, filesystem, subprocesses) inside a sandbox, should you target the standardized WASI Rust targets (wasm32-wasip1/2/3), or define and require a custom, non-standard Rust target tailored to the sandbox's own syscall/threading model? |
| m2b1-q288 | `b-sb22-f009062-q2` | wasm;core | should crates use `cfg(target_family = "wasm")` / `cfg(target_arch = "wasm32")` as a proxy for "running in a reduced-functionality standalone browser build," given that some Wasm targets now offer full Linux syscall access (filesystem, threads, subprocesses)? |
| m2b1-q289 | `a-sa18-f009104-q1` | core | Should Rust adopt call-site ergonomics features common in other languages — named parameters, optional/default arguments, function overloading — or does the simplicity of "one name, one fixed signature" outweigh the ergonomic gains, given the complexity and interaction effects (evaluation order, patterns-not-names, function-as-value) these features would introduce? |
| m2b1-q290 | `a-sa18-f009104-q2` | core | Does the rise of AI coding agents change the cost/benefit calculus for verbose, explicit call-site syntax (like named arguments) that was previously judged not worth its typing cost for human authors? |
| m2b1-q291 | `a-sa19-f009123-q1` | core | Should scoped trait implementations be nameable, or must they stay anonymous? |
| m2b1-q292 | `b-sb22-f009132-q1` | core | should rustc set `--compress-debug-sections=zstd` as the default linker flag for Linux targets, to shrink `target/` and binary size? |
| m2b1-q293 | `a-sa19-f009196-q1` | core | Should `Instant` expose fixed extremal values (MIN/MAX), given it has no fixed reference epoch? |
| m2b1-q294 | `a-sa19-f009196-q2` | distributed;cloud-workers;core | When a scheduled timer/interval's next wake time would overflow the maximum representable `Instant`, should the runtime panic or silently never become ready again? |
| m2b1-q295 | `b-sb22-f009236-q1` | core | for a trait whose one method converts a value into a different representation of the same underlying type (e.g. `ToOwned::to_owned`), should the trait/method follow Rust's `as_`/`to_`/`into_` naming convention, or be named with a bare verb (as `Clone` and `Borrow` are)? |
| m2b1-q297 | `a-sa19-f009292-q2` | core | How should Rust reduce boilerplate for simple trait implementations — new dedicated impl syntax, compiler-inferred associated types, or ecosystem derive-macro crates? |
| m2b1-q298 | `a-sa19-f009316-q1` | core | Should Rust add `final`/non-overridable trait methods, and if so, must such methods still participate in dynamic dispatch (vtables) for soundness? |
| m2b1-q299 | `b-sb23-f009334-q1` | core | Should crates.io/Cargo offer a dedicated "deprecate" mechanism (per-version, non-breaking) distinct from yank, rather than relying on yank or Cargo.toml maintenance badges? |
| m2b1-q300 | `b-sb23-f009334-q2` | core | Should crate "maintenance status" metadata be author-declared and decayed/expired automatically over time, or purely opt-in with no forced expiry or automated notification? |
| m2b1-q301 | `a-sa19-f009343-q1` | core;desktop-cli-ui | Should rustc warn (or emit a note) whenever it is invoked without an explicit `--edition`, given how much edition-dependent behaviour has accumulated? |
| m2b1-q302 | `a-sa19-f009343-q2` | core;desktop-cli-ui | Should crates and their build scripts (build probes like autocfg) be free to auto-detect and use nightly-only compiler/library features by default, or must nightly-feature usage always require the final binary author's explicit opt-in? |
| m2b1-q303 | `b-sb23-f009657-q1` | core | Should Rust switch its default linker on the most popular target (x86_64-unknown-linux-gnu) from the system linker to a faster non-GNU linker (lld), accepting a small risk of incompatibility? |
| m2b1-q304 | `a-sa20-f009698-q1` | core | When a new language capability doesn't interact with a prior edition's changed semantics, should it be made available on older Rust editions too, or should the edition boundary gate all new capabilities regardless of whether they actually interact with anything that changed? |
| m2b1-q305 | `a-sa20-f009698-q2` | core | Should unsafe struct fields be expressed with a minimal, purely field-level rule set (mark the field unsafe if it carries a safety invariant; using it is then unsafe), or with a hybrid design that mixes syntactic markers and wrapper types? |
| m2b1-q306 | `a-sa20-f009698-q3` | core | When a new borrow-checker algorithm (Polonius) trades full expressiveness parity with the old implementation for an easier path to production-readiness, should the project accept the narrower formulation (and its known false positive on one loop/region case) to ship sooner, or hold out for full expressiveness? |
| m2b1-q307 | `a-sa20-f009698-q4` | core | When rustc has internal capability to correctly deduce information (implied trait bounds) that an external tool (cargo-semver-checks) cannot feasibly re-derive on its own, should that capability be exposed through a structured interface (rustdoc JSON) rather than left for external tools to approximate? |
| m2b1-q308 | `b-sb23-f009737-q1` | wasm | Should Rust's WebAssembly targets treat undefined symbols as a hard link error by default (matching native platforms), even though some code intentionally relies on the current silent-import behavior? |
| m2b1-q310 | `a-sa21-f011069-q1` | ml;other | For verifying that a rewritten/ported system stays behaviorally equivalent to the original when correct behavior includes emergent, hard-to-specify effects (e.g. a physics-engine exploit), should you rely on unit/integration tests, naive property-based (fuzzing) testing, or a heuristic-guided reinforcement-learning search? |
| m2b1-q312 | `a-sa22-f011092-q1` | cloud-workers;distributed;core | Should a secure multi-tenant runtime that executes untrusted user code (e.g. a serverless JavaScript isolate hypervisor) be built in a language like Rust rather than a garbage-collected language like Go? |
| m2b1-q313 | `a-saL2-f011092-q1` | core;cloud-workers | for scaling `cargo test` across a large multi-binary workspace, should a team adopt cargo-nextest, or build a custom test-runner wrapper when nextest's behavioral changes conflict with existing test assumptions? |
| m2b1-q314 | `a-saL2-f011092-q2` | cloud-workers;distributed;core | in a multi-tenant sandboxed runtime, should tenants share read-only memory pages (e.g. a JS engine's read-only heap) for efficiency, or should each tenant get fully isolated memory, given the side-channel risk (ASLR, Spectre-style timing attacks) shared pages introduce? |
| m2b1-q315 | `a-saL2-f011092-q3` | cloud-workers;distributed | for third-party cloud/vendor integrations in Rust, should a team rely on official vendor SDKs (where they exist), or build lean internal wrapper SDKs given how uneven vendor Rust support is? |
| m2b1-q316 | `a-saL2-f011092-q4` | cloud-workers;distributed | should a multi-tenant compute platform allocate resources via static per-request/per-tenant reservation (Kubernetes-style CPU requests/limits), or via dynamic, system-wide throttling of individual noisy tenants? |
| m2b1-q317 | `a-saL2-f011092-q5` | core | should production Rust software depend on nightly-only unstable features, or restrict itself entirely to stable Rust? |
| m2b1-q318 | `b-sb23-f011133-q1` | desktop-cli-ui | For cross-platform desktop/embedded GUI development from Rust, should a team adopt a new compile-time-checked toolkit (Slint) over a mature, runtime-interpreted one (Qt/QML), given Slint's smaller ecosystem (missing multimedia, 3D, multi-window, automated UI testing, no iOS support yet)? |
| m2b1-q319 | `b-sb23-f011178-q1` | distributed;decentralized-iroh | For hosting large monorepos, should Git object storage move off the traditional filesystem-based backend and into a distributed database (as Google Piper/Meta Sapling do), combined with decentralizing hosting itself rather than relying on a centralized host like GitHub? |
| m2b1-q320 | `a-sa23-f011186-q1` | web | should an API's schema be hand-authored or generated from the server's own code (spec-first vs code-first)? |
| m2b1-q321 | `a-sa23-f011186-q2` | web;core | should a Rust code generator emit its output as procedural-macro magic or as plain generated source files? |
| m2b1-q322 | `a-sa23-f011186-q3` | core | should Rust macros be used liberally or sparingly? |
| m2b1-q323 | `a-sa23-f011186-q4` | web;core | should generated crates be fully automatic, or must they leave handwritten escape hatches for what a schema can't express (e.g. trait impls)? |
| m2b1-q324 | `a-sa23-f011186-q5` | web;core | is a long compile time an acceptable cost of large generated/dependency-heavy crates in exchange for API correctness and ergonomics? |
| m2b1-q325 | `a-sa24-f011220-q2` | cloud-workers;distributed;core | Is the primary source of cloud vendor lock-in the compute platform you deploy to, or the managed data/SDK layer you build against? |
| m2b1-q326 | `b-sb23-f011233-q1` | ml;other | For GPU kernel programming from Rust, should the ecosystem invest in a community-driven Rust-native toolchain (rust-cuda) rather than continuing to write kernels in C++/CUDA with a thin Rust host layer, given CUDA's vendor lock-in and rust-cuda's current feature gaps? |
| m2b1-q327 | `b-sb23-f011233-q2` | core | For performance-sensitive numeric code, should Rust developers prefer the ergonomic, nightly-only `std::simd` portable-SIMD API over stable but manual target-feature-gated intrinsics? |
| m2b1-q328 | `b-sb23-f011235-q1` | core | Should routine compiler-team process work (PR triage/bookkeeping, nudging reviewers, tracking regressions) be fully automated, or does it need a human doing it manually to protect contributors' limited time and avoid over-pinging them? |
| m2b1-q329 | `b-sb24-f011295-q1` | web;distributed;core | When onboarding a team new to Rust on a security-critical project, should you write "easy mode Rust" (owned types instead of borrowed references, `Arc<RwLock<T>>` instead of lock-free structures) to keep the team approachable, or go straight for the most advanced/performant Rust idioms? |
| m2b1-q330 | `b-sb24-f011295-q2` | core | For security-critical code handling cryptographic keys, should key roles and verification status be encoded as distinct types checked at compile time (the typestate pattern), rather than checked with runtime assertions? |
| m2b1-q331 | `b-sb24-f011295-q3` | distributed;web | When a system's design forbids observing real user traffic (privacy/anonymity by design), should you build synthetic "canary" traffic that exercises the real system on a schedule, rather than instrumenting/tracing real messages for observability? |
| m2b1-q333 | `a-sa26-f011305-q2` | core;web;frontend | do Rust's compile times and language rigidity make it less productive than high-level frameworks (React, FastAPI) for rapid prototyping? |
| m2b1-q334 | `a-sa26-f011305-q3` | core;frontend;desktop-cli-ui | should Rust adopt a lightweight/automatic-clone mechanism (e.g. reference-counted "generational box" ergonomics) for callback-heavy UI code, trading some compile-time guarantees for runtime checks? |
| m2b1-q335 | `a-sa26-f011305-q4` | core | should Rust macros get first-class IDE tooling (autocomplete, hover, partial expansion) via new mechanisms, or is today's macro opacity accepted as a tradeoff for macro power? |
| m2b1-q336 | `a-sa26-f011305-q6` | desktop-cli-ui;frontend | should a Rust GUI framework build its own modular rendering engine rather than wrap native platform widgets or an existing browser engine? |
| m2b1-q337 | `b-sb24-f011306-q1` | core;distributed | For distributed tracing in Rust, should the ecosystem standardize on the widely-adopted `tracing` crate (Tokio's tracing API), on the OpenTelemetry-spec-compliant tracing API, or keep maintaining both with improved interop? |
| m2b1-q338 | `b-sb24-f011306-q2` | core | For writing eBPF programs from Rust, should you use a pure-Rust implementation with no libbpf/BCC dependency (Aya), or a Rust wrapper around the native C `libbpf` library with the eBPF program itself written in C (libbpf-rs)? |
| m2b1-q339 | `b-sb24-f011306-q3` | distributed;core | For propagating distributed-trace context (W3C trace-context HTTP headers) across a network boundary without modifying application code, should you use library interposition (`LD_PRELOAD` hijacking libcurl/libssl calls) or an eBPF-based mechanism (kernel-level header injection)? |
| m2b1-q340 | `b-sb24-f011312-q1` | core | For binding a large existing C++ API surface to Rust, should you use a low-level C-ABI-only generator (bindgen/cbindgen), a manually-declared bridge macro with boxed indirection (CXX), a hand-written interface-description-language with explicit layout control ("Zengar"), or native compiler integration across clang and rustc (Crubit)? |
| m2b1-q341 | `b-sb24-f011312-q2` | core | When binding C++ APIs whose safety depends on undocumented preconditions, should every C++ function be marked `unsafe` in Rust by default, or should the binding rely on C++-side safety annotations plus type-based heuristics to mark functions safe where possible? |
| m2b1-q342 | `b-sb24-f011312-q3` | core | For C++ mutable references crossing into Rust (which, unlike Rust's `&mut`, are not guaranteed exclusive and can alias), should the FFI binding represent them as raw unsafe pointers, `Cell`-based interior mutability, or a new native non-exclusive C++-style reference type added to Rust? |
| m2b1-q343 | `b-sb24-f011312-q5` | core | For C++ types that cannot be relocated via a simple memcpy (self-referential types, e.g. small-string-optimized `std::string`), should Rust FFI bindings represent them using `Pin`, given Rust's general assumption that all types are memcpy-movable? |
| m2b1-q344 | `b-sb24-f011312-q6` | core | Should Rust add built-in function overloading (at least for FFI/interop purposes), given it has historically avoided overloading in favor of traits, generics, and newtypes? |
| m2b1-q346 | `a-sa25-f011413-q2` | core;web | Should Rust's derive/serialization ecosystem centralize around one blessed crate (serde) that other crates interoperate through, given orphan rules make independent multi-crate composition hard? |
| m2b1-q350 | `b-sb24-f011413-q2` | core | When a generic container needs different (de)serialization behavior depending on its concrete element type (e.g. `Vec<u8>` as raw bytes vs. `Vec<f32>` as a numeric sequence), should this rely on manual per-field annotations (Serde's `#[serde(with = ...)]`, easy to forget) given Rust has no stable specialization, or should it use runtime reflection to detect the concrete type and dispatch automatically? |
| m2b1-q351 | `b-sb25-f011435-q1` | web | Should a Rust web/browser engine be built from the start as separable, independently-usable modular crates joined by traits (Blitz's approach), rather than as a monolithic-by-default engine where modularity is added incidentally and reluctantly (Servo's approach, and Ladybird's from-scratch full-browser approach)? |
| m2b1-q352 | `b-sb25-f011435-q2` | web;core | When building a modular engine, should each optional capability (JS engine, specific image/video codecs, networking, SVG) be its own compiled-in-only-if-used feature/crate, even at the cost of a much larger total dependency count spread across many small crates, rather than bundling capabilities together by default? |
| m2b1-q353 | `a-sa26-f011443-q1` | other | should introductory CS/software-engineering curricula teach a systems language like Rust directly (to force understanding of memory, concurrency, ownership), or is teaching via high-level frameworks and abstractions sufficient? |
| m2b1-q354 | `a-sa26-f011443-q2` | ml;core;other | is Rust the best-suited language for an AI-driven future where machines write code and humans architect systems (because the compiler independently checks AI-generated code)? |
| m2b1-q355 | `a-sa26-f011460-q3` | wasm;frontend | at the Rust/Wasm↔JavaScript FFI boundary, should code favor ergonomic serialization (serde-wasm-bindgen) or manual/structural field access (wasm-bindgen getters), trading ergonomics against performance? |
| m2b1-q356 | `a-sa26-f011605-q1` | web | should a Rust web framework favor a macro-free, type/extractor-driven API design, or a macro-based route/handler declaration syntax? |
| m2b1-q357 | `a-sa26-f011605-q2` | web | should a Rust web framework be built around the actor model, or around a Service/Layer (Tower) middleware model? |
| m2b1-q359 | `a-sa26-f011993-q1` | core | should Rust have a prescriptive "core guidelines" document (as C++ has C++ Core Guidelines), or rely on compiler enforcement plus automated lints (Clippy) and de-facto popular-crate conventions instead? |
| m2b1-q360 | `a-sa27-f012237-q1` | swift-interop | When packaging a Rust core library for Apple platforms (iOS) via UniFFI, should the FFI-binding and packaging steps run as an Xcode build phase or as an external script/CI pipeline outside Xcode? |
| m2b1-q361 | `a-sa27-f012237-q2` | swift-interop | When assembling a Rust static library into an XCFramework for Swift distribution, should you hand-build the XCFramework's directory structure or use Apple's `xcodebuild -create-xcframework` tooling? |
| m2b1-q362 | `a-sR16-f012428-q1` | core;desktop-cli-ui | Is Rust's trait-based supertrait/subtrait polymorphism (no class inheritance) an adequate, ergonomic substitute for OOP-style inheritance, or does the required generic/trait-bound plumbing make it more verbose and confusing than an inheritance-based language? |
| m2b1-q363 | `a-sa28-f012469-q2` | core | Should Rust (as language and standard library) aim for minimalism — a small core deferring functionality to crates.io — or be a fuller, "medium-sized"/batteries-included system? |
| m2b1-q364 | `a-sa28-f012469-q3` | core | Did Rust's design correctly prioritize memory safety as its one "hard problem," and is that tradeoff fair against other capabilities (e.g., metaprogramming/expressiveness) that consequently matured more slowly? |
| m2b1-q365 | `a-sa28-f012469-q4` | core | [reflection-carries-risk, continues the reflection thread opened in extract-b1-sa25.md's Q3/Q4] Does giving Rust code reflection-like or dynamic-loading capability introduce a security/soundness risk category that Rust's design has otherwise avoided? |
| m2b1-q366 | `a-sa28-f012469-q5` | core | Should Rust favor implicit ergonomic sugar (the 2017 "ergonomics initiative", e.g. match ergonomics) even where it costs the language's own stated core value of explicitness, or hold the line on explicitness? |
| m2b1-q367 | `a-sa28-f012469-q6` | core;embedded | What is `unsafe`'s proper mental model — a manual-invariant-maintenance discipline still bound by the same rules, or a permissive escape hatch? |
| m2b1-q368 | `b-sb25-f012561-q1` | other | In a growing Bevy/ECS game, should cross-system state changes flow through an events/observers-first architecture (systems never mutate each other's state directly) rather than direct shared mutable access, accepting the loss of transactional rollback and added boilerplate in exchange for decoupling? |
| m2b1-q369 | `b-sb25-f012561-q2` | other | When a Bevy codebase grows past tens of thousands of lines and single-crate compile times become disruptive, should shared types be pulled into one low-level crate that everything depends on (simple, but the worst-case recompile unit), or should the codebase instead be split along domain lines to avoid any single always-recompiled root crate? |
| m2b1-q370 | `b-sb25-f012561-q3` | other | For complex UI built on an ECS with an immediate-mode UI library (egui), should you write large systems with many queries in one place (simpler control flow, but they frequently deadlock against the borrow checker), or split into many small per-widget systems (fewer conflicts per system, but requires repeated manual world/state access that itself risks borrow-checker errors)? |
| m2b1-q371 | `a-sR16-f012642-q1` | distributed;core | Should a high-performance Rust client API expose multiple tiers of the same builder operation — an unchecked/positional fast path alongside a checked/named-field safe path — rather than one safe-by-default interface? |
| m2b1-q372 | `b-sb25-f012642-q1` | other | When writing data to GreptimeDB from Rust, should an application use the low-latency Regular write API or the high-throughput Bulk Stream Insert API, and how should parallelism and compression be tuned for each? |
| m2b1-q373 | `b-sb26-f012849-q1` | core;embedded | does adopting a language with compiler-enforced ownership/borrow-checked safety (Rust) constitute a broad, unambiguous quality improvement over established unmanaged low-level languages (C/C++), such that resistance to it mostly reflects habit rather than substantive technical concern — or is Rust's real value narrower than that? |
| m2b1-q374 | `b-sb26-f012866-q1` | web;frontend;wasm | for developer tooling that serves the JavaScript/TypeScript ecosystem (linters, formatters, bundlers, parsers), should the tool itself be implemented in Rust rather than in JavaScript/TypeScript? |
| m2b1-q375 | `a-sa29-f012940-q1` | web;distributed;cloud-workers;core | For a new Rust application adopting OpenTelemetry, should the logging facade be the span-native `tracing` crate, or a conventional logging crate bridged into OpenTelemetry later? |
| m2b1-q376 | `a-sa29-f013113-q1` | wasm | Should Rust represent WebAssembly's opaque `externref` host reference as a genuinely new, restricted first-class type that partly bypasses ordinary Rust type-system rules, or as an ordinary table-index value with special handling confined to the FFI boundary? |
| m2b1-q377 | `a-sa29-f013113-q2` | wasm | Should Rust's core language/type system be extended with new primitives to serve niche, platform-specific interop needs (like WASM `externref`), or should such platform oddities be handled entirely outside the language, in the compiler or runtime? |
| m2b1-q378 | `b-sb26-f013214-q1` | other | is Rust's 3D/graphics game-dev crate ecosystem (wgpu, Rend3, Bevy, egui, winit) mature enough for demanding, multi-year production projects, or does its ongoing API churn and thinness make such projects impractical today? |
| m2b1-q379 | `b-sb26-f013214-q2` | other;embedded | does high-performance, high-concurrency game/graphics programming require relaxing memory safety (via `unsafe` code or an unmanaged language) to hit performance and shipping-speed targets, or can idiomatic safe Rust deliver competitive results with no `unsafe` at all? |
| m2b1-q380 | `b-sb26-f013214-q4` | other | when a Rust game engine embeds a scripting/modding language, should most game logic live in the hosted scripting language itself, or should Rust own the state with the scripting language calling into it through getter/setter shims? |
| m2b1-q381 | `a-sa29-f013224-q1` | core | Should rust-lang.org (or official Rust community properties) integrate an AI assistant/LLM feature — semantic search, chat assistant, or interactive tutorials? |
| m2b1-q382 | `a-sa30-f013276-q1` | core;web | Should Rust abstraction and dependency injection favor static dispatch (generics) over dynamic dispatch (`dyn Trait`/type erasure), and how narrow are `dyn Trait`'s legitimate use cases? |
| m2b1-q383 | `a-sa30-f013276-q2` | core;web | Are classic OOP design patterns (e.g., Abstract Factory, as invoked via Clean/Hexagonal/Onion Architecture and DDD "ports and adapters") idiomatic to port into Rust, or does Rust favor different idioms (generics, enums) for the same structural goals? |
| m2b1-q384 | `a-sa30-f013276-q3` | core | Was reusing the same `impl Trait` syntax for both return-position (RPIT) and argument-position (APIT) impl Trait a language design mistake? |
| m2b1-q385 | `a-sa30-f013276-q4` | core | How constrained are `dyn Trait`'s object-safety rules, and how likely/soon could they be relaxed (e.g., via higher-ranked generic bounds or a next-generation trait solver)? |
