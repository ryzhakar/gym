# Extraction — batch 1, team B, slice sb20

Framing: for each source, what must a Rust practitioner decide, and where do the sources conflict on it?

ROW 153 is absent from the bundle (dropped by the bundler); skipped per instructions.

## f007213 — "Bypassing" specialization in Rust...: Follow-up (2025-07-26, en)

### Questions
- Q: when a type needs specialization-like behavior (methods gated on stronger trait bounds, e.g. `Read+Write+Seek` vs `Read+Seek`) but Rust's real specialization is unstable, do you fake it with a runtime-checked field set from trait-bound-gated impl blocks, or reach for a different pattern entirely?
  concepts: specialization, trait bounds, generics over storage traits; domains_live: core; positions_seen: runtime-checked optional field (`sync_fn: Option<SyncFn>`) set only from impls gated on the stronger bound, single constructor for both RO/RW cases (Oakchris1955)

### Claims
- voice: Oakchris1955 | position: single-constructor design with an `Option<SyncFn>` field toggled from trait-bound-gated impl blocks, replacing separate RO/RW constructors | date: 2025-07-26 | locator: section "The solution" | paraphrase: instead of two constructors (one for read-only, one for read-write), keep one constructor and one `sync_fn` field defaulted to `None`; only impls bound on `Read + Write + Seek` can set it to `Some`, which fixes a bug where RWFile writes silently failed to sync | quote: "Instead of using 2 constructors, one for a RO filesystem and another for a R/W filesystem, we use one for both cases." | practiced_evidence: none (crate name given, `simple_fatfs`, but no repo URL in the captured text)

## f007290 — Does Dioxus spark joy? (2025-11-22, en)

### Questions
- Q: is Rust (via a fullstack WASM framework like Dioxus) ready to replace JavaScript/TypeScript frameworks for frontend and fullstack web development?
  concepts: WASM frontend, server-side rendering, hydration, hot patching, DWARF debugging; domains_live: frontend, wasm; positions_seen: not yet — use Rust on the backend and TypeScript on the frontend for now, while remaining optimistic about where Dioxus is headed (fasterthanlime)
- Q: is the complexity practitioners feel in fullstack reactive frameworks (hooks, effects, suspense, hydration mismatches) accidental complexity added by the framework, or essential complexity inherent to the fullstack problem itself?
  concepts: hooks, reactivity, hydration, suspense; domains_live: frontend, web; positions_seen: essential, not accidental (fasterthanlime)
- Q: when a WASM framework offers hot-patching (fast, stateful code reload) that is incompatible with DWARF-based native debugging, should a practitioner enable hot-patching during development anyway?
  concepts: hot patching (Subsecond), DWARF debugging, WASM tooling; domains_live: wasm, frontend; positions_seen: tradeoff reported without a recommendation — enabling hot-patch breaks DWARF debugging and vice versa (fasterthanlime)

### Claims
- voice: fasterthanlime | position: fullstack Rust-to-WASM frameworks are not yet a substitute for JS frameworks; ship Rust on the backend and TypeScript on the frontend meanwhile | date: 2025-11-22 | locator: section "Does Dioxus spark joy?" | paraphrase: after using Dioxus for a real project, the verdict is "not yet" — it is still unpleasant compared to the author's Svelte 5 "gold standard," even though the author is excited about the trajectory | quote: "In the meantime, I'll be doing Rust on the backend, and TypeScript on the frontend." | practiced_evidence: none (repo for the quizzing app built with Dioxus is referenced only as "an upcoming project," no URL given)
- voice: fasterthanlime | position: the hooks/reactivity complexity in a fullstack framework is essential, not accidental | date: 2025-11-22 | locator: section "Love-hate" | paraphrase: the long list of Dioxus hooks and the fact that breaking hook rules produces silent misbehavior rather than a compile or runtime error feels intimidating, but that is because fullstack apps are inherently complicated, not because Dioxus added needless complexity | quote: "It's that full stack stuff is complicated. It truly is. It's not that Dioxus added complexity where we didn't need any." | practiced_evidence: none

## f007364 — Interpreting near native speeds with CEL and Rust (2026-03-04, en)

### Questions
- Q: should structs/enums carry lifetime parameters (borrowed data) to avoid heap allocation and copying, or should you avoid putting lifetime parameters on structs, as a rule of thumb, and keep data owned?
  concepts: lifetimes, borrowing, zero-copy design, ownership; domains_live: core; positions_seen: embrace lifetime parameters deliberately, rewriting an owned `Value` enum as `Value<'a>` with `Borrowed`/`Owned` variants, to eliminate a measured bottleneck (howardjohn) — conflicts with f007608 below, which states the opposite rule of thumb

### Claims
- voice: howardjohn | position: add lifetime parameters to the core value/type representation to allow zero-copy borrowing, deliberately trading struct/API complexity for measured performance | date: 2026-03-04 | locator: section "References#" preceded by "Native types in CEL#" and "References#" (value type redefinition under heading "References#" appears just after "Ultimate solution"); exact quote is from the paragraph beginning "First, we need references!" | paraphrase: converting `Value` from an owned enum to `Value<'a>` with `Cow`-like `Borrowed`/`Owned` variants (and a `Dynamic`/`DynamicType` trait for native Rust types) was the key change that let a CEL evaluation get within ~10ns of native code, versus 147ns for the original owned/hashmap-based implementation | quote: "First, we need references! We change Value to not be owned" | practiced_evidence: none (Agentgateway's CEL crate is discussed but no repository URL is given in the captured text)

## f007608 — Object Soup is Made of Indexes (2023-10-25, en)

### Questions
- Q: how do you represent a mutable, cyclic, many-to-many object graph ("object soup") in Rust: `Rc<RefCell<T>>`/`Arc<Mutex<T>>`, raw/unsafe pointers, or an index-into-a-`Vec`/arena design?
  concepts: interior mutability, Rc/RefCell, Arc/Mutex, unsafe pointers, arenas, ECS; domains_live: core; positions_seen: index/arena-based design, avoiding both `Rc<RefCell<T>>` (leak- and panic-prone) and raw pointers (undefined-behavior-prone) (jacko.io)
- Q: should structs/enums carry lifetime parameters (borrowed data), or should you avoid putting lifetime parameters on structs, as a rule of thumb?
  concepts: lifetimes, borrowing, struct design; domains_live: core; positions_seen: avoid lifetime parameters on structs as a rule of thumb (jacko.io) — conflicts with f007364 above, which embraces them for a measured performance win

### Claims
- voice: jacko.io | position: model cyclic/many-to-many mutable object graphs with a `Vec` (or `HashMap`/`Slab`/`SlotMap`) of objects referring to each other by index, not with `Rc<RefCell<T>>` or raw pointers | date: 2023-10-25 | locator: section "Part Four: Indexes" | paraphrase: `Rc<RefCell<T>>` compiles for "object soup" but leaks memory on reference cycles and panics on self-referential mutable borrows (`already mutably borrowed: BorrowError`); raw/unsafe pointers hit the same aliasing problems and risk undefined behavior; keeping objects in a `Vec` and referring to each other by `usize` index avoids both, turns aliasing bugs into compiler errors, and serializes/parallelizes cleanly with `serde`/`rayon` | quote: "This is how we write object soup in Rust." | practiced_evidence: none
- voice: jacko.io | position: avoid putting lifetime parameters on structs, as a general rule of thumb | date: 2023-10-25 | locator: footnote to the paragraph beginning "Playing with these examples is educational" in section "Part Two: Borrowing" | paraphrase: while experimenting with borrow-checker fights builds useful intuition, the actionable takeaway when you get stuck is to keep lifetime parameters off your struct definitions | quote: "a good rule of thumb is to avoid putting lifetime parameters on structs" | practiced_evidence: none

## f007678 — Practical Client-side Rust for Android, iOS, and Web (2023-12-13, en)

### Questions
- Q: for an Android app calling into a shared Rust library, should the JNI-facing binding layer be hand-written in Rust (alongside the Rust↔C FFI layer), or written in C++ instead?
  concepts: JNI, FFI, cross-language bindings, Android/NDK tooling; domains_live: other; positions_seen: write the JNI layer in C++, trading an extra language at the boundary for Android Studio's code generation, build automation, and header-level code navigation, which Cargo/Rust tooling lacked at the time (Emily Dixon) — the source itself notes this goes against how "many guides" do it
- Q: across a Rust FFI boundary (to Kotlin/Java, Swift, or JavaScript), should complex data be copied across, or shared by reference/pointer?
  concepts: FFI memory management, ownership across language boundaries; domains_live: swift-interop, other; positions_seen: prefer copying data across the boundary over sharing it, for memory-safety and simplicity, accepting the performance cost (Emily Dixon)

### Claims
- voice: Emily Dixon | position: write the Android JNI-facing bindings in C++ rather than in Rust | date: 2023-12-13 | locator: section "Rust for Android," subsection "The app" | paraphrase: many guides write both the FFI (Rust↔C) and JNI (C↔JVM) layers in Rust, but doing the JNI side in C++ instead lets Android Studio's native-C++ project tooling (code generation, build automation, code analysis, jump-to-declaration) work across the boundary, at the cost of one extra language | quote: "Many guides write the JNI and FFI layers in Rust, but I chose to write the JNI side in C++ instead." | practiced_evidence: https://github.com/daytime-em/rs-hybrid-cross-platform (rustlib/android bindings)
- voice: Emily Dixon | position: copy data across FFI boundaries rather than sharing it by reference | date: 2023-12-13 | locator: section "Rust for Android," paragraph beginning "On the Rust side, you'll need to encapsulate" | paraphrase: creating an FFI struct that copies out of the Rust result object (rather than sharing a pointer into it) costs a small performance penalty but guarantees memory management on one side of a binding can't affect the other side, which the author judges worth it "more often than not" | quote: "Copying immutable data is generally safer and easier than trying to share it." | practiced_evidence: https://github.com/daytime-em/rs-hybrid-cross-platform

## f007736 — Rust macros taking care of some Lambda boilerplate (2024-01-17, en)

### Questions
- Q: is writing a custom procedural macro to eliminate a small, fixed amount of per-function setup boilerplate (an AWS Lambda's `main`/tracing setup) worth the added indirection, versus just accepting the boilerplate?
  concepts: procedural macros, attribute macros, boilerplate reduction; domains_live: cloud-workers; positions_seen: default to no for real applications — only worthwhile with many very simple Lambdas, a low tolerance for boilerplate, or wanting to experiment with macros (Sam Van Overmeire)

### Claims
- voice: Sam Van Overmeire | position: a boilerplate-removing procedural macro is usually not worth writing for real Lambda applications | date: 2024-01-17 | locator: paragraph beginning "Before continuing: would you ever want to use a macro like this?" | paraphrase: for most real applications either the boilerplate is tolerable or you'll want custom initialization code in `main` that a fully-generated `main` forecloses; the macro pays off mainly if you have many simple Lambdas, a very low tolerance for boilerplate, or want to experiment with macros and serverless | quote: "For real applications: default to no." | practiced_evidence: none (macro code shown inline; no repository URL given)

## f007760 — Rust macros taking care of even more Lambda boilerplate (2024-01-31, en)

### Questions
- Q: is writing a custom procedural macro to eliminate a small, fixed amount of per-function setup boilerplate (an AWS Lambda's `main`/tracing/client-initialization setup) worth the added indirection, versus just accepting the boilerplate?
  concepts: procedural macros, attribute macros, boilerplate reduction, AWS SDK client setup; domains_live: cloud-workers; positions_seen: same as f007736 — worthwhile mainly when you have many simple Lambdas or only need AWS clients with sensible defaults; a bit of boilerplate is otherwise an acceptable price for main-function flexibility (Sam Van Overmeire)

### Claims
- voice: Sam Van Overmeire | position: a boilerplate-removing procedural macro is usually not worth writing; boilerplate is an acceptable cost of `main`-function flexibility | date: 2024-01-31 | locator: paragraph beginning "As a reminder: in the previous blog post" | paraphrase: reiterating the prior post's stance while extending the macro to auto-initialize AWS SDK clients found among the handler's parameters — still frames the macro as useful only for callers with many simple, client-only Lambdas | quote: "A bit of boilerplate is acceptable when this helps you retain the flexibility to customize your main function, adding any (initialization) code you require." | practiced_evidence: none

## f007797 — Deploying Axum to Lambda and ECS, using Lambda Web Adapter (2024-02-21, en)

### Questions
- Q: should a Rust web service (e.g., an Axum app) target one deployment substrate uniformly, or run on Lambda for test/dev and on a container orchestrator (ECS/Fargate) for production, accepting an infrastructure mismatch between environments?
  concepts: Lambda Web Adapter, serverless vs. container deployment, cost/infra-parity tradeoff; domains_live: cloud-workers; positions_seen: splitting environments (Lambda for infrequently-used test environments, ECS for always-on production) is floated as a cost-saving option, explicitly named as a tradeoff rather than a clear recommendation (Sam Van Overmeire)

### Claims
- voice: Sam Van Overmeire | position: consider deploying test/dev environments to Lambda and production to ECS to balance cost against infra-parity, rather than picking one substrate for both | date: 2024-02-21 | locator: closing paragraph, beginning "Lambda Web Adapter not only makes it easier" | paraphrase: because Lambda Web Adapter decouples the Axum app from any one runtime, an app that is costly to run 24/7 on Lambda but cheap on ECS could run infrequent test environments on Lambda and production on ECS; the author calls this "a tradeoff" since test and production would then run on meaningfully different infrastructure, but says the cost savings can be worth it in some scenarios | quote: "It's a tradeoff because there is now a meaningful difference between the infrastructure your code runs on in test versus production. But in some scenarios, the cost savings might be worth it." | practiced_evidence: none (CDK snippets shown inline; no repository URL given)

## f007942 — This Month in Rust GameDev #51 (2024-06-05, en)

### Questions
- Q: should Rust community publications (newsletters, blog posts) include AI-generated content?
  concepts: AI-assisted/machine-written content, community norms; domains_live: other; positions_seen: readers surveyed by the Rust GameDev newsletter reject AI-generated newsletter content (Rust GameDev Working Group, reporting a reader survey)

### Claims
- voice: Rust GameDev Working Group | position: the newsletter's readership does not want AI-generated content included | date: 2024-06-05 | locator: section "Survey Results #" | paraphrase: after surveying 52 readers on how to improve the newsletter, the WG reports that readers are generally positive about it, are content with its frequency, but explicitly do not want anything in it generated by AI | quote: "Readers do not want anything in the newsletter generated by AI." | practiced_evidence: none (survey results said to be detailed in a linked blog post, not fetched — out of scope per Tier 2 rules)

## f007973 — Comprehensive guide to nom parsing (2023-02-20, en)

### Nothing new
`nothing new` — this is a straight how-to tutorial for the `nom` parser-combinator crate (hex-color, CSS-like, natural-language, and Markdown parsing examples); it teaches one library's usage and error-reporting features throughout, and at no point stakes out or contrasts a position on a contested Rust design question (e.g. it never argues for parser combinators over hand-written parsers, `pest`, or other alternatives).
