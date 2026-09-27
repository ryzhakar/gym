# Blind fill A — summaries, batch 1, file 02

### boxed-closure-tuple-vs-named-field--p4
Summary: Once a constructor is already required to do the boxing, the type should be a one-field named struct rather than a tuple struct, because a bare boxed function in a tuple field is unclear to Rust newcomers, and the constructor already removes the main ergonomic reason to prefer a tuple struct.
Tag: taste
Claims: b-sb14-f004398-c4

### boxed-closure-tuple-vs-named-field--p3
Summary: A `new` constructor that performs the boxing internally lets call sites just write `Type::new(|state| ...)`, so the type can keep its `Box<dyn Fn>` representation without callers writing `Box::new` themselves.
Tag: tradeoff
Claims: b-sb14-f004398-c3

### boxed-closure-tuple-vs-named-field--p1
Summary: The predicate should be stored as `Box<dyn Fn(&S) -> bool>` in a public tuple-struct field so stateful closures that capture values (e.g. a level number) can be used, not just hard-coded literals; `Box` won't allocate for non-capturing closures anyway.
Tag: tradeoff
Claims: b-sb14-f004398-c1

### boxed-closure-tuple-vs-named-field--p2
Summary: The original design deliberately stayed away from exposing the trait object directly in a public field, specifically so users would never need to write `Box::new` at call sites.
Tag: tradeoff
Claims: b-sb14-f004398-c2

### boxed-vs-hand-written-future--p1
Summary: For Lambda specifically, a boxed dynamic future (`Box::pin(async move {...})`) is the idiomatic default for middleware needing post-response work, since Lambda's cost profile makes a single per-request heap allocation irrelevant; hand-rolling a `pin-project`-based future to avoid that allocation is reserved for a tight loop on a busy server, at the cost of ~30 extra lines, a new struct and a new dependency.
Tag: tradeoff
Claims: b-sb22-f008906-c2

### breaking-rename-for-vocabulary--p1
Summary: A library should perform a broad breaking rename across its whole public API pre-1.0 to align vocabulary with its current mental model — dropping a term left over from an earlier, broader project scope — even though it breaks every caller, because pre-1.0 is the right moment to make that change.
Tag: tradeoff
Claims: b-sR08-f003731-c2

### breaking-wire-change-in-minor--p1
Summary: A pre-1.0 networking library can ship a breaking wire-protocol change in a routine minor release for a real protocol improvement (here, dropping a full round-trip from every new connection), accepting that new and old nodes can no longer talk to each other, and softening the break with a transition window (here, keeping the old infrastructure running for several more weeks).
Tag: tradeoff
Claims: a-sT04-f001319-c1

### build-tool-cargo-subcommand-vs-standalone--p1
Summary: A subcommand is functionally identical to a standalone binary plus a few injected environment variables, so a Rust-ecosystem tool aiming for wide reuse and a healthy ecosystem should register as a `cargo` subcommand rather than compete as a standalone "cargo-plus-plus" tool.
Tag: taste
Claims: a-sa05-f003025-c2, a-sa05-f003025-c1

### build-tool-cargo-subcommand-vs-standalone--p2
Summary: Cargo cannot run, test or bench wasm/iOS/Android projects and its development cycle is slow, so high-usage ecosystem tools (wasm-bindgen and similar) end up standalone by necessity, and a project's own CLI (e.g. Bevy's) can reasonably be designed as a cargo wrapper/replacement rather than a subcommand, with narrow project-specific needs better served outside a general-purpose stable tool like Cargo.
Tag: tradeoff
Claims: a-sa05-f003025-c3, a-sa05-f003025-c4, a-sa05-f003025-c5

### built-in-async-runtime--p1
Summary: Rust is a low-level language that strives for minimal runtime overhead, so unlike languages whose runtime handles memory management, exception handling and the like, it leaves choice of async runtime to the ecosystem rather than building one in, even though this means an extra step (picking a runtime crate) to get started.
Tag: tradeoff
Claims: b-bk01-f000233-c2

### builtin-package-manager-effect--p1
Summary: A good built-in package manager changes engineering practice in a way bolted-on dependency management doesn't: it wasn't even worth checking whether a comparable C/C++ library existed, because even if one did, its source would have had to be vendored by hand, whereas `cargo add half` made pulling in equivalent functionality trivially easy.
Tag: fact
Claims: a-sR15-f008241-c2

### byte-vs-bit-packed-cells--p1
Summary: Representing each cell with a full byte makes iterating over cells easy but wastes seven of every eight bits per cell; a `FixedBitSet`-based, bit-packed rewrite is the resolution to that waste.
Tag: tradeoff
Claims: b-bk02-f000256-c4

### c-maintainers-rust-bindings-duty--p1
Summary: A C maintainer will fix their own C code but is not obligated to fix Rust bindings that break as a result, and should not be forced to learn Rust just because Rust bindings now depend on their subsystem.
Tag: taste
Claims: b-sb18-f005332-c1

### c-maintainers-rust-bindings-duty--p2
Summary: Rust adoption in a C codebase depends on C maintainers' cooperation: being blocked from pushing small, Rust-motivated robustness and lifetime fixes into the C code causes real harm — kernel panics that trace back to bugs in that C code rather than to the Rust side — and the resulting friction and exhaustion is itself a reason people leave the effort.
Tag: tradeoff
Claims: b-sb18-f005332-c2, b-sb18-f005332-c3

### c-maintainers-rust-bindings-duty--p3
Summary: Slower-than-expected Rust adoption is attributable to old-time C kernel developers being unfamiliar with and unenthusiastic about learning a new, quite different language, compounded by instability in the Rust kernel infrastructure itself — not to bad faith on either side.
Tag: fact
Claims: b-sb18-f005332-c4

### cancel-safety-requirement--cancel-safety-required
Summary: Cancel safety on `recv` is a hard requirement for async RPC/mpmc channels used internally, not a nice-to-have: a library whose `recv` occasionally lost notifications under cancellation caused stuck tasks in practice, and a non-cancel-safe RPC channel found in production was treated as a critical bug serious enough to break a fixed release cadence and ship an out-of-cycle fix.
Tag: fact
Claims: b-sb17-f005159-c4, a-sT04-f001650-c1

### cfg-wasm-as-reduced-platform-proxy--p1
Summary: Crates widely special-case behavior (e.g. swapping in a `fetch()`-based HTTP client) whenever they detect the "wasm" target family or `wasm32` architecture, which is wrong for a target that actually has full Linux syscall access; deliberately misreporting that target metadata is the current workaround to defeat those assumptions, used reluctantly pending the ecosystem becoming aware that fully-featured Wasm targets exist.
Tag: tradeoff
Claims: b-sb22-f009062-c2

### cli-flag-convenience-vs-consistency--p1
Summary: A new command's destructive-action flag should follow the same `--no-dry-run` naming every other command in the tool already uses, for the sake of consistency across the tool's command surface.
Tag: taste
Claims: b-sb09-f003036-c1

### cli-flag-convenience-vs-consistency--p2
Summary: Getting this particular flag wrong isn't actually dangerous, and `--no-dry-run` is annoying enough to type that a shorter, less consistent default might be worth the deviation.
Tag: tradeoff
Claims: b-sb09-f003036-c2

### cli-flags-mirror-familiar-tool--p1
Summary: A niche, protocol-specific CLI tool's flags should mirror an already-familiar general-purpose tool's conventions — here, curl's — on the "principle of least surprise," rather than inventing new flag names for the tool's own domain.
Tag: taste
Claims: a-sa14-f004947-c1

### cli-output-overwrite-default--p1
Summary: A CLI tool that repeatedly writes an output file should overwrite the same filename by default, so past shell commands can be reused unedited to view the latest result; this also matches a peer tool's (samply's) behavior, which nobody has been heard complaining about.
Tag: taste
Claims: b-sb13-f004160-c3

### cli-output-overwrite-default--p2
Summary: The output filename should include a timestamp by default, or at least from the second run onward, so that a new result never silently replaces an old one.
Tag: tradeoff
Claims: b-sb13-f004160-c4

### cli-tool-single-vs-multi-protocol--p1
Summary: A debugging CLI should bundle every related protocol a team operates — here, OHTTP, CONNECT proxying, MASQUE and (soon) Privacy Pass — into one tool, since existing narrow, single-protocol tools were each useful on their own but nothing combined them all in one place.
Tag: tradeoff
Claims: b-sR11-f004947-c1

### close-future-result-vs-infallible--p1
Summary: A close/shutdown future should be infallible rather than return a `Result`; an endpoint's `close()` future was changed from `Result`-returning to infallible.
Tag: tradeoff
Claims: b-sT05-f002550-c3

### cloud-lock-in-source--p1
Summary: The compute platform you deploy to is a smaller vendor lock-in risk than the managed data/SDK layer you build against — switching a Postgres-backed service to a proprietary store like DynamoDB, CosmosDB or Firestore forces a specific SDK and data model that locks you in more than any compute choice, whereas structuring the codebase with entry-point adapters around a core business-logic crate (ports-and-adapters/hexagonal architecture) lets the same application run on Fargate/ECS or Lambda interchangeably.
Tag: tradeoff
Claims: a-sa24-f011220-c2

### codegen-macro-vs-generated-source--p1
Summary: A code generator should emit its output as a normal, on-disk Rust crate (source directory, `Cargo.toml`, `.rs` files) rather than as procedural-macro expansion, because macro output is hard to debug and can produce confusing compile errors, even though macros have their appeal.
Tag: tradeoff
Claims: a-sa23-f011186-c2

### compile-time-cost-of-generated-crates--p1
Summary: Large autogenerated API crates can dominate a project's slowest-compiling dependencies, especially in release mode, but after looking for ways to shrink them, it's better to accept the long compile time than to give users a lower-quality API.
Tag: tradeoff
Claims: a-sa23-f011186-c5

### compile-time-typed-dsl--p1
Summary: Hosting a DSL's programs as compile-time types buys zero runtime cost and no dynamic loading, at the cost of not being able to easily run DSL programs that are loaded into a host application at runtime (config files, plugins, game mods).
Tag: tradeoff
Claims: a-sa16-f007175-c2

### compile-time-vs-runtime-switches--runtime-switch
Summary: Test-only or staging-vs-production behavior should be switched at runtime rather than through Cargo features, `#[cfg]` or compile-time environment variables: a compile-time env var was dropped entirely in favor of a runtime-threaded option described as "more programmatically sound," and separately, after a bug let production code silently point at staging infrastructure via a build-time feature/`#[cfg(test)]` check, the choice of infrastructure was moved to rely solely on a runtime-checked environment variable behind a dedicated function.
Tag: tradeoff
Claims: b-sT05-f002550-c1, b-sT04-f002233-c1

### compiler-triage-automation--p1
Summary: Routine compiler-team triage bookkeeping shouldn't be fully automated: contributors have only a finite amount of time and are a precious asset, so a human judgment call on when to nudge a reviewer avoids over-pressuring them, even while external contributors also expect a timely response.
Tag: tradeoff
Claims: b-sb23-f011235-c1

### component-abi-special-case-lowerings--p1
Summary: Ad hoc special-cased lowerings for common shapes — `ref.null` for `none`/no-error, a boolean `i32` for a no-payload `result` — are licensed at the CABI level when they're a significant win, and `option` is common enough that this qualifies.
Tag: tradeoff
Claims: a-sa05-f003074-c1

### component-abi-special-case-lowerings--p2
Summary: The premise behind the proposed optimization is disputed: languages with parametric polymorphism (e.g. Java's `Optional`) typically can't perform the null-for-none specialization at all without costly runtime type dispatch, so the optimization wouldn't apply to anywhere near the claimed proportion of cases in practice.
Tag: fact
Claims: a-sa05-f003074-c2

### component-abi-special-case-lowerings--p3
Summary: Allowing extra matched shapes for special-cased lowerings risks a slippery slope — "how many shapes is enough" — so any widening of matchable shapes needs an explicit design principle rather than case-by-case allowances.
Tag: tradeoff
Claims: a-sa05-f003074-c3

### component-map-duplicate-keys--p1
Summary: Bindings generators must normalize duplicate map keys to a defined winner (last-key-wins), and the spec wording should be strengthened from merely expecting this to explicitly requiring it, even though the Component Model itself cannot enforce the property.
Tag: tradeoff
Claims: b-sb11-f003384-c2, b-sb11-f003384-c1

### component-map-duplicate-keys--p2
Summary: Uniqueness of map keys should be mandated by the spec and enforced at the component boundary rather than silently tolerated, though there's room to differ on the enforcement mechanism — whether a violation should trap or the lowering side should just silently keep the final value.
Tag: tradeoff
Claims: b-sb11-f003384-c3, b-sb11-f003384-c4

### component-map-duplicate-keys--p3
Summary: A host should be allowed, but not required, to deduplicate map keys with well-defined last-value-overwrites semantics when merging does occur, by analogy to how NaN payload canonicalization is optional rather than mandatory at component boundaries.
Tag: tradeoff
Claims: b-sb11-f003384-c5

### component-map-ordering--p1
Summary: Bindings should be expected to preserve `map` entry order, since most target languages' Map types do, and the component-model type should be renamed (e.g. to `dict` or `ordered-map`) to avoid confusion with non-order-preserving maps.
Tag: tradeoff
Claims: b-sb11-f003384-c6

### component-map-ordering--p2
Summary: The basic `map` type should not guarantee any order — most languages' basic map/hash-map types don't either (Rust's HashMap, .NET's Dictionary, Java's HashMap, Go's map), and 9 times out of 10 an ordering isn't needed anyway; an ordered variant is available separately via `list<tuple<key,value>>` if ever required.
Tag: tradeoff
Claims: b-sb11-f003384-c7, b-sb11-f003384-c8

### component-map-ordering--p3
Summary: If a deterministic execution profile can't randomly permute and doesn't normalize map order, then order becomes an observable part of `map`'s semantics whether intended or not — a consequence worth discussing on its own rather than a settled question.
Tag: fact
Claims: b-sb11-f003384-c9

### compress-debug-sections-default--p1
Summary: Setting `--compress-debug-sections=zstd` as the default linker flag for Linux targets is worth doing, based on a measured shrink of a hello-world project's `target/` from 4.7M to 1.5M plus a modest build-time improvement.
Tag: fact
Claims: b-sb22-f009132-c1

### compress-debug-sections-default--p2
Summary: The stated motivation for the change hasn't been pinned down — is `target/` big from duplication across projects, stale files, or genuinely unused debug info? — and reaching for compression as a default fix, ahead of that analysis, would slow down (or not obviously help) every debug build.
Tag: tradeoff
Claims: b-sb22-f009132-c2

### compress-debug-sections-default--p3
Summary: Making zstd-compressed debug sections the Linux default can't happen yet because mainstream enterprise/LTS distro tooling (e.g. Ubuntu 22.04 LTS's gdb/binutils) doesn't support them, which would silently break the debugging experience for developers required to use those distros at work.
Tag: fact
Claims: b-sb22-f009132-c3

### consolidate-internal-network-frameworks--p1
Summary: When several internal services need similar network-framework capabilities, the org should consolidate on existing async-ecosystem crates (hyper, tokio) rather than reinvent them, prioritizing faster iteration and battle-tested code, and contribute fixes back upstream.
Tag: tradeoff
Claims: a-sa15-f005604-c1

### const-generics-unify-specializations--p1
Summary: Near-duplicate hand-written specializations that differ only by array length/arity, and that are already drifting apart from each other inside the same change, should be unified into one type parameterized by a const generic, since monomorphization gives it identical codegen to the hand-specialized versions.
Tag: tradeoff
Claims: b-sR12-f005085-c2

### coupled-debug-accessor-vs-primitive--p1
Summary: A narrow, purpose-built debugging accessor — even one coupled to internal layout details and inherently linear-search-based — is an acceptable way to expose a needed capability, and it can later be rewritten to be asymptotically efficient (O(1) via a cached reverse table) without abandoning its narrow, purpose-built shape.
Tag: tradeoff
Claims: b-sb16-f005000-c1, b-sb16-f005000-c4

### coupled-debug-accessor-vs-primitive--p2
Summary: A powerful but inherently inefficient (linear-search) debugging capability that couples to internal layout details is worth questioning even once made asymptotically efficient, since the cost of maintaining that coupling — and its fragility to future refactoring — may not be justified for what is a niche use case.
Tag: tradeoff
Claims: b-sb16-f005000-c2, b-sb16-f005000-c5

### coupled-debug-accessor-vs-primitive--p3
Summary: Rather than a purpose-built accessor coupled to internal layout, expose a smaller, general-purpose primitive (e.g. `Func::eq`/`Func::hash`, pointer-identity comparisons) and let the caller assemble whatever structure (like a hashtable) they need in a single linear pass, which is independently useful and asymptotically better than the coupled accessor's linear search.
Tag: tradeoff
Claims: b-sb16-f005000-c3, b-sb16-f005000-c6

### cow-for-allocation-visibility--p1
Summary: Even when an allocation-avoiding type like `Cow<str>` would only save a negligible amount of work, it's still worth preferring over a plain `String`, because Rust makes allocations visible in the code in a way that makes you want to avoid them regardless of how small the performance impact actually is.
Tag: taste
Claims: a-sR15-f008241-c1

---
Notification: Filled positions-02.csv (60 claim rows) and summaries-02.md (48 positions) for input-b1-02.md, covering questions from `boxed-closure-tuple-vs-named-field` through `cow-for-allocation-visibility`. Four low-confidence calls are flagged: one boxed-closure claim lacks explicit constructor language for its assigned position, one build-tool claim only weakly implies subcommand vs standalone, one Linux-kernel claim infers a duty stance from a resignation rather than a direct statement, and one component-ABI claim disputes a premise without affirmatively picking a position. All others are high confidence from quote and paraphrase alone, no sources opened.
