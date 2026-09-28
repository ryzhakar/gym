# Blind fill summaries, batch 1, file 02 of 13 (run b)

## boxed-closure-tuple-vs-named-field--p1
Summary: The type should be a tuple-struct field holding `Box<dyn Fn(&S) -> bool>` directly, so it can hold stateful closures (one capturing a level number, say), noting `Box` costs nothing extra for a non-capturing closure.
Tag: taste
Claims: b-sb14-f004398-c1

## boxed-closure-tuple-vs-named-field--p2
Summary: The original design deliberately stayed away from exposing the trait object in the public field so that users would never need to write `Box::new` at a call site themselves.
Tag: tradeoff
Claims: b-sb14-f004398-c2

## boxed-closure-tuple-vs-named-field--p3
Summary: A `new` constructor that performs the boxing internally keeps the `Box<dyn Fn>` representation while letting a call site read as plain `DespawnOnExitWith::new(|state| ...)`, mitigating the friction of boxing without changing the field's shape.
Tag: tradeoff
Claims: b-sb14-f004398-c3

## boxed-closure-tuple-vs-named-field--p4
Summary: Once a constructor already does the boxing, the tuple struct's main ergonomic benefit is gone, and "stores a boxed function" is tricky for newcomers to read off a bare tuple field, so the field should be named for clarity.
Tag: tradeoff
Claims: b-sb14-f004398-c4

## boxed-vs-hand-written-future--p1
Summary: `Box::pin(async move {...})` is the idiomatic default for middleware that must do work after the inner future resolves; on Lambda the one heap allocation per request is irrelevant, so hand-rolling a `poll`-based struct with `pin-project` to save it is reserved for a tight loop on a busy server, not the general case.
Tag: tradeoff
Claims: b-sb22-f008906-c2

## breaking-rename-for-vocabulary--p1
Summary: A term left over from an earlier, broader project scope ("node") is dropped from the vocabulary everywhere it appears in the public API, because the moment right before 1.0 is the moment to align naming with the current mental model, even though it breaks every caller using the old names.
Tag: taste
Claims: b-sR08-f003731-c2

## breaking-wire-change-in-minor--p1
Summary: A protocol improvement is shipped even though it makes new instances unable to talk to the previous minor release, accepting the incompatibility while softening its landing by keeping the old servers running for several more weeks.
Tag: tradeoff
Claims: a-sT04-f001319-c1

## build-tool-cargo-subcommand-vs-standalone--p1
Summary: A subcommand is functionally identical to a standalone binary plus a few injected environment variables, so an ecosystem tool aiming for wide reuse should register as a `cargo` subcommand; a standalone "cargo plus plus" replacement fragments and, in the strong form of this view, is how you kill an ecosystem.
Tag: tradeoff
Claims: a-sa05-f003025-c2, a-sa05-f003025-c1

## build-tool-cargo-subcommand-vs-standalone--p2
Summary: Cargo cannot run, test or bench wasm, iOS or Android projects, and its own limitations and slow development cycle push high-usage tools like wasm-bindgen and a project's own CLI to be standalone wrappers or replacements rather than subcommands, especially once the tool's needs (asset handling, a default index.html) are too specific for a general-purpose stable tool to absorb.
Tag: tradeoff
Claims: a-sa05-f003025-c3, a-sa05-f003025-c4, a-sa05-f003025-c5

## built-in-async-runtime--p1
Summary: Rust is a low-level language that strives for minimal runtime overhead, so unlike languages whose runtime bundles memory management and exception handling, it leaves the async runtime's scope limited and lets you choose one depending on your requirements rather than providing one — at the cost of an extra step to get started.
Tag: fact
Claims: b-bk01-f000233-c2

## builtin-package-manager-effect--p1
Summary: Not even thinking to look for a C/C++ library, because any that existed would have had to be vendored by copying source into the project, versus a single `cargo add` for the Rust equivalent, is read as evidence that having a good, builtin package manager changes what a developer will even attempt.
Tag: tradeoff
Claims: a-sR15-f008241-c2

## byte-vs-bit-packed-cells--p1
Summary: One byte per cell wastes seven of every eight bits and that cost is named explicitly against the bit-packed alternative; the resolution offered is a rewrite onto `FixedBitSet`.
Tag: fact
Claims: b-bk02-f000256-c4

## c-maintainers-rust-bindings-duty--p1
Summary: A C maintainer will fix their own C code but is not going to be forced to learn Rust or take responsibility for fixing Rust bindings that break as a result of a C-side change.
Tag: tradeoff
Claims: b-sb18-f005332-c1

## c-maintainers-rust-bindings-duty--p2
Summary: Every kernel panic in a Rust GPU driver traces to bugs in the C code it wraps, not to the Rust code itself, and being blocked by a C maintainer from pushing small robustness and lifetime fixes to that C code — alongside the exhaustion that drove a maintainer resignation over "nontechnical nonsense" rather than technical disagreement — is offered as evidence that Rust's success in the kernel needs active C-side cooperation, not just tolerance.
Tag: tradeoff
Claims: b-sb18-f005332-c3, b-sb18-f005332-c2

## c-maintainers-rust-bindings-duty--p3
Summary: The pushback against Rust in the kernel is attributed to old-time C kernel developers being unfamiliar with and unenthusiastic about learning a new, quite different language, plus instability in the Rust kernel infrastructure itself — not to bad faith — framing slow adoption as a practical, expected friction rather than a moral failing on either side.
Tag: tradeoff
Claims: b-sb18-f005332-c4

## cancel-safety-requirement--cancel-safety-required
Summary: Cancel safety on `recv` is treated as a must-have: a channel library found occasionally losing notifications under cancellation was swapped out for one that fixed the reproducer, and a separate discovery that RPC channels were not cancel-safe was serious enough to break a team's own release cadence to land a fix immediately, rather than documenting the gap as a caller's responsibility.
Tag: tradeoff
Claims: b-sb17-f005159-c4, a-sT04-f001650-c1

## cfg-wasm-as-reduced-platform-proxy--p1
Summary: Crates that special-case behavior whenever they see the "wasm" target family or `wasm32` architecture get it wrong for a target with full Linux syscall access, so metadata is deliberately misreported to defeat those assumptions — called "hacks" that the team would rather not need, pending the ecosystem recognizing that fully-featured Wasm targets exist.
Tag: fact
Claims: b-sb22-f009062-c2

## cli-flag-convenience-vs-consistency--p1
Summary: Every other command in the tool already uses `--no-dry-run`, so the new command should match that pattern for consistency rather than introduce a differently-shaped flag.
Tag: taste
Claims: b-sb09-f003036-c1

## cli-flag-convenience-vs-consistency--p2
Summary: Getting this particular flag wrong is not actually dangerous, and `--no-dry-run` is annoying enough to type that a shorter, default-on-dry-run naming is worth considering, even while conceding the point if the team prefers consistency.
Tag: taste
Claims: b-sb09-f003036-c2

## cli-flags-mirror-familiar-tool--p1
Summary: A niche protocol tool's flags are designed around curl's argument conventions on purpose, under a stated "principle of least surprise," rather than inventing fresh names for its own domain.
Tag: tradeoff
Claims: a-sa14-f004947-c1

## cli-output-overwrite-default--p1
Summary: Overwriting the same output filename by default is preferred because it lets a shell history entry be reused unedited to view the latest result, and it matches a peer tool's behavior that nobody has complained about.
Tag: taste
Claims: b-sb13-f004160-c3

## cli-output-overwrite-default--p2
Summary: Timestamping the output filename — by default, or at least from the second run onward — is recommended so that a new profile never silently overwrites and discards a previous one.
Tag: tradeoff
Claims: b-sb13-f004160-c4

## cli-tool-single-vs-multi-protocol--p1
Summary: Existing single-protocol tools for OHTTP were useful but narrow; the differentiator for a new tool is combining OHTTP, CONNECT proxying, MASQUE and (soon) Privacy Pass in one place, since nothing else does.
Tag: taste
Claims: b-sR11-f004947-c1

## close-future-result-vs-infallible--p1
Summary: An endpoint's close future is changed to be infallible rather than returning a `Result`, stated as a breaking change with no further justification given in the release notes.
Tag: fact
Claims: b-sT05-f002550-c3

## cloud-lock-in-source--p1
Summary: Adopting a proprietary managed-data service (a specific SDK and data model) locks a project in more than the choice of compute platform does; structuring the codebase around a core business-logic crate with entry-point adapters lets the same application run on Fargate/ECS or Lambda interchangeably, which is offered as the actual fix for lock-in fears about serverless compute.
Tag: tradeoff
Claims: a-sa24-f011220-c2

## codegen-macro-vs-generated-source--p1
Summary: A code generator emits a normal, on-disk Rust crate — source directory, `Cargo.toml`, `.rs` files — rather than expanding inline as a procedural macro, because macro-generated output is hard to debug and macros can produce confusing compile errors.
Tag: tradeoff
Claims: a-sa23-f011186-c2

## compile-time-cost-of-generated-crates--p1
Summary: Large autogenerated API crates dominate a project's slowest-compiling dependencies, especially in release mode; after looking for ways to shrink them, the long compile time is accepted deliberately in order to keep giving users a high-quality generated API.
Tag: tradeoff
Claims: a-sa23-f011186-c5

## compile-time-typed-dsl--p1
Summary: Hosting a DSL's programs as compile-time types buys zero-runtime-cost, no-dynamic-loading interpretation, at the explicit cost of being unable to easily run DSL programs loaded into a host application at runtime — config files, plugins, game mods and the like.
Tag: tradeoff
Claims: a-sa16-f007175-c2

## compile-time-vs-runtime-switches--runtime-switch
Summary: A compile-time environment variable used to pick test-only behavior is dropped entirely — described as "more programmatically sound" — and a related infrastructure-selection bug (production code silently pointed at staging relays) is fixed by moving off the `test-utils` feature and `#[cfg(test)]` entirely, relying only on a runtime-checked environment variable behind a dedicated function.
Tag: fact
Claims: b-sT05-f002550-c1, b-sT04-f002233-c1

## compiler-triage-automation--p1
Summary: A manual, cross-referenced bookkeeping process for nudging PR reviewers is kept rather than fully automated, because contributors have only a finite amount of time and are "a precious asset" — a human judgment call on when to nudge protects that limited time even though external contributors also expect timely responses.
Tag: tradeoff
Claims: b-sb23-f011235-c1

## component-abi-special-case-lowerings--p1
Summary: Representing `none`/no-error as `ref.null` and a no-payload `result` as a boolean `i32` is proposed as something the canonical ABI is "licensed" to do ad hoc, because `option` and no-payload results are extremely common enough that the special-casing is a significant, worthwhile win.
Tag: tradeoff
Claims: a-sa05-f003074-c1

## component-abi-special-case-lowerings--p2
Summary: The claim that a null-for-none optimization would cover close to 95% of cases in practice is disputed, since languages with parametric polymorphism (such as Java's `Optional`) typically cannot perform that specialization without costly runtime type dispatch, undercutting the case for the ad hoc shortcut.
Tag: fact
Claims: a-sa05-f003074-c2

## component-abi-special-case-lowerings--p3
Summary: Allowing extra matched shapes for special-cased lowering risks becoming a slippery slope — "how many shapes is enough" — so any widening of what gets ad hoc treatment needs an explicit design principle behind it rather than case-by-case allowances.
Tag: tradeoff
Claims: a-sa05-f003074-c3

## component-map-duplicate-keys--p1
Summary: Bindings generators should be required — strengthened from merely expected to a spec-level MUST — to normalize a map with duplicate keys so that generated map interfaces behave as if duplicates were filtered out with last-value-wins semantics.
Tag: fact
Claims: b-sb11-f003384-c2, b-sb11-f003384-c1

## component-map-duplicate-keys--p2
Summary: Key uniqueness in a `map` should be mandated by the specification and enforced at the component boundary rather than silently tolerated, though on a violation the lowering side should keep the final value rather than trap.
Tag: tradeoff
Claims: b-sb11-f003384-c3, b-sb11-f003384-c4

## component-map-duplicate-keys--p3
Summary: A host should be allowed, but not required, to deduplicate a `map` with duplicate keys, with well-defined last-value-overwrites semantics only when such merging happens — drawing an analogy to how NaN payload canonicalization is optional, not mandatory, at component boundaries.
Tag: tradeoff
Claims: b-sb11-f003384-c5

## component-map-ordering--p1
Summary: Bindings are expected to preserve a `map`'s entry order, since most host languages' own Map types do, and the component-model type should be renamed to something like `dict` or `ordered-map` to avoid confusion with types that don't preserve order.
Tag: tradeoff
Claims: b-sb11-f003384-c6

## component-map-ordering--p2
Summary: The basic `map` type should not guarantee any order, since most languages' basic map types don't either — nine times out of ten you don't need ordering — with an explicitly ordered variant available separately as `list<tuple<key,value>>`, matching the precedent of Rust's HashMap, .NET's Dictionary, Java's HashMap and Go's map.
Tag: fact
Claims: b-sb11-f003384-c7, b-sb11-f003384-c8

## component-map-ordering--p3
Summary: A deterministic execution profile cannot randomly permute a map's order, so if that profile doesn't normalize order explicitly, order becomes an observable part of `map`'s semantics whether intended or not — a real tradeoff worth deciding on, not something settled by the general unordered default.
Tag: tradeoff
Claims: b-sb11-f003384-c9

## compress-debug-sections-default--p1
Summary: A hello-world project's `target/` directory measurably shrank (4.7M to 1.5M) and build time modestly improved (1.65s to 1.25s mean) with `--compress-debug-sections=zstd` enabled, which is offered as grounds to default the flag on Linux before filing a full MCP.
Tag: fact
Claims: b-sb22-f009132-c1

## compress-debug-sections-default--p2
Summary: The motivation itself is called lacking: before reaching for compression as a default fix, the discussion should first pin down why `target/` is actually big — duplication across projects, stale files, or genuinely unused debug info — since compression alone would also not obviously help, and would slow down, every debug build.
Tag: fact
Claims: b-sb22-f009132-c2

## compress-debug-sections-default--p3
Summary: Many developers are required to use Ubuntu LTS or another enterprise distro at work, whose gdb and binutils lack zstd support; shipping this by default would silently break their debugging experience, called a "showstopper" that leaves the proposal going nowhere until mainstream distro tooling catches up.
Tag: fact
Claims: b-sb22-f009132-c3

## consolidate-internal-network-frameworks--p1
Summary: A new internal framework is deliberately built to stand on the shoulders of existing, battle-tested open-source crates (hyper, tokio) rather than reinvent them, prioritizing faster iteration and contributing fixes back upstream — to the point that team members become core maintainers of the upstream crates.
Tag: tradeoff
Claims: a-sa15-f005604-c1

## const-generics-unify-specializations--p1
Summary: Two hand-specialized types differing only by stride count have already drifted apart from each other inside the very PR meant to add the second one, and a single type parameterized by a const generic would cover both with identical codegen once monomorphized, so the drift is treated as real rather than hypothetical.
Tag: fact
Claims: b-sR12-f005085-c2

## coupled-debug-accessor-vs-primitive--p1
Summary: A host-only, linear-search accessor deliberately scoped to guest-debugging mode is added, and when its linear-search cost is challenged it is rewritten to be O(1) via a lazily-built, module-level cached reverse table rather than abandoning the narrow, purpose-built design.
Tag: tradeoff
Claims: b-sb16-f005000-c1, b-sb16-f005000-c4

## coupled-debug-accessor-vs-primitive--p2
Summary: The whole use case is questioned: an API this inherently inefficient (linear search) may not survive future refactorings, and even once made asymptotically better, taking on the coupling to internal layout and its added delicate logic is still not worth it for what is a niche use case.
Tag: tradeoff
Claims: b-sb16-f005000-c2, b-sb16-f005000-c5

## coupled-debug-accessor-vs-primitive--p3
Summary: A smaller, general primitive — `Func::eq`/`Func::hash` as pointer-identity equality — is preferred because it is independently useful and lets the caller build their own index in a single linear pass, asymptotically better than the coupled accessor; the accessor's own author ultimately agrees the internal-layout coupling isn't worth it and drops it in favor of this primitive.
Tag: tradeoff
Claims: b-sb16-f005000-c3, b-sb16-f005000-c6

## cow-for-allocation-visibility--p1
Summary: Switching a query-parsing path from `String` to `Cow<&str>` is preferred specifically because Rust makes the presence of an allocation visible in the code, and that visibility is valued enough to chase even when the performance impact of avoiding the allocation is minuscule.
Tag: taste
Claims: a-sR15-f008241-c1
