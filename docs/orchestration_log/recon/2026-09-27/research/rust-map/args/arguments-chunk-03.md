## rust-for-web-frontend
### rust-for-web-frontend--isomorphic-rust-web
- for | Unlike Loco, which replicates Rails-style scaffolding with a separate React frontend, Leptos lets a developer define server functions callable directly from client code, with the client/server interface auto-generated, so moving logic between browser and server is "almost effortless" | values: simplicity | sources: f012146@~07:06-08:07
- against | no argument in sources

### rust-for-web-frontend--not-yet-for-frontend
- for | After building a real project with Dioxus, the verdict is "not yet" — it remains unpleasant next to Svelte 5 (the author's ergonomic gold standard), even while feeling optimistic about generational references cutting event-handler boilerplate, working server functions, and the framework's trajectory; the plan is Rust on the backend, TypeScript on the frontend in the meantime | values: approachability | sources: f007290@"Does Dioxus spark joy?"
- against | no argument in sources

### rust-for-web-frontend--rust-wasm-compute-bound-only
- for | Rewriting a Rust/WASM parser into pure TypeScript showed the Rust computation was never the bottleneck — the entire cost was the WASM/JS boundary (serialize in, serialize out); WASM wins only for compute-bound work with rare boundary crossings (image/video, crypto, physics) and loses on parsing into JS objects or frequently-called functions on small inputs, because V8's JIT closes the raw-compute gap | values: performance | sources: f005699@"When WASM Actually Helps"/"Key Takeaways"
- against | A hand-optimized hex-color-parsing function — string-heavy, minimal computation, allocating on return, "very hostile" to Wasm on paper, exactly the profile the compute-bound-only rule would exclude — still beat its JavaScript control by roughly 2x once copying was eliminated, so "the blanket advice to use WebAssembly on only heavy compute is too simple" | values: performance | sources: f011460@[18:28]-[22:37]

### rust-for-web-frontend--rust-wasm-over-js-broadly
- for | JS's dynamic typing and GC pauses make web performance unreliable; Rust gives low-level control without that non-determinism, ships no runtime so `.wasm` stays small, and lets teams port only hot-path functions incrementally rather than rewrite everything | values: performance | sources: f000256@"Why Rust and WebAssembly?" § "Low-Level Control with High-Level Ergonomics"
- for | wasm-bindgen gives a range of abstraction levels rather than one opinionated boundary, and a hand-optimized hex-color-parsing function beat its JavaScript control by roughly 2x despite being "very hostile" to Wasm on paper (string copy, minimal computation, allocation on return) | values: performance | sources: f011460@[18:28]-[22:37]
- against | Rewriting a Rust/WASM parser to plain TypeScript found the Rust computation was never the slow part; parsing structured text into JS objects and frequently-called functions on small inputs lose to WASM because the serialization/boundary tax dominates and V8's JIT closes the raw-compute gap | values: performance | sources: f005699@"When WASM Actually Helps"/"Key Takeaways"

## rust-in-process-server-new-capability
### rust-in-process-server-new-capability--p1
- for | Making well-written C safe to *use* generally requires isolating it in a separate process the way nginx does; Rust instead lets an expert's high-performance, "cursed" code be reused safely as a library by less-expert programmers in the same language — that reuse, not an abstract "Rust safe, C dangerous" claim, is what's novel | values: correctness | sources: f005360@matklad reply 2024-10-14T07:01:58-05:00
- against | Framing a memory-safe language's libraries against C/C++'s dangers is "getting really old" — nginx and Apache, both written in C, already work fine as web servers | values: stability | sources: f005360@pm reply 2024-10-13T18:31:49-05:00

### rust-in-process-server-new-capability--p2
- for | Framing a memory-safe language's libraries against C/C++'s dangers is "getting really old" — nginx and Apache, both written in C, already work fine as web servers | values: stability | sources: f005360@pm reply 2024-10-13T18:31:49-05:00
- against | Making well-written C safe to *use* generally requires isolating it in a separate process the way nginx does; Rust instead lets an expert's high-performance code be reused safely as a library by less-expert programmers in the same language — that reuse is what's novel | values: correctness | sources: f005360@matklad reply 2024-10-14T07:01:58-05:00

## rust-lang-org-ai-assistant
### rust-lang-org-ai-assistant--p1
- for | Making an AI-assistant feature opt-in (hidden unless enabled by a preference) would defuse resistance, noting people already bring raw ChatGPT output to the forum for help, so a built-in, opt-in assistant could improve on that status quo | values: value-candidate: adoption-friction (flagged: argues from community acceptance/rollout strategy, not from correctness, simplicity, iteration-speed, performance, stability or approachability) | sources: f013224@forum post 2024-03-02T18:37:26.330Z
- against | no argument in sources

### rust-lang-org-ai-assistant--p2
- no argument in sources (its only Claim is excluded: gap voice-below-bar)

### rust-lang-org-ai-assistant--p3
- no argument in sources (its only Claim is excluded: gap voice-below-bar)

## rust-vs-c-inherent-performance
### rust-vs-c-inherent-performance--composability-wins
- for | Rust's composability lets an engineer reach for a B-Tree where in C they'd stick to the safer-to-ship AVL tree, because a hand-rolled intrusive C B-Tree is too risky to trust ("up in everything's underwear"); what wins in practice is what engineers are actually willing to ship, not who tops a benchmark, and a hand-rolled generic concurrent hash table was in practice replaced by an off-the-shelf container plus a lock, coming out both more maintainable and faster | values: simplicity, performance | sources: f005516@ssokolow reply 2025-06-10T09:04:39-05:00 (quoting Bryan Cantrill)
- against | Trivial new features can force large refactorings because they necessitate new borrowing schemes, and extra clones/`Rc` are commonly added just to satisfy the borrow checker in situations where they aren't algorithmically necessary — so the "engineers are willing to ship it" framing doesn't hold in the replying voice's own experience | values: performance | sources: f005516@dataangel reply 2025-06-10T11:09:00-05:00

### rust-vs-c-inherent-performance--init-cost-narrow
- for | Rust has no default initialization; it merely requires init *before use* based on dataflow analysis, the same as for an ordinary variable — so any zero-init cost should only bite in narrow cases like large arrays or read buffers, not as a blanket tax, and it's fair to ask whether the allocator scenario generalizes at all | values: correctness, performance | sources: f005516@rpjohnst replies 2025-06-11T11:16:03-05:00 and 2025-06-12T10:09:38-05:00
- against | Safe Rust requires a value at construction time, not just before use by dataflow analysis — a large array or a small-object allocator must eagerly zero-init memory it may never read first, and the cost compounds with more allocations, sometimes bloating codegen enough to block inlining and further optimization | values: performance | sources: f005516@dataangel reply 2025-06-12T07:56:20-05:00 and 2025-06-13T20:10:53-05:00

### rust-vs-c-inherent-performance--no-inherent-advantage
- for | no argument in sources (its only Claim is excluded: gap voice-below-bar)
- against | Looking at actual disassembly on nontrivial examples shows recurring, real costs: mandatory heap-then-stack-allocation patterns, zero-init by default, bounds checks on array/division/shift access, unsafe-gated SIMD intrinsics, iterators that optimize poorly, `RefCell` overhead, and un-collapsible `Result` wrapping — which is why Rust solutions don't top competitive-programming leaderboards | values: performance | sources: f005516@dataangel reply 2025-06-10T07:16:21-05:00

### rust-vs-c-inherent-performance--p1
- for | The practical gap is partly ecosystem-driven: C's lack of an easily-reached-for hashmap pushes real code toward slow linear searches until it becomes a forced problem (citing a GitLab backup-time postmortem), while Rust's easy hashmaps and parallel iterators make fast-by-default collections and code the norm in practice — so the live discussion is just which language makes it easier to write fast programs | values: performance, iteration-speed | sources: f005516@kornel reply 2025-06-10T08:19:54-05:00
- against | no argument in sources

### rust-vs-c-inherent-performance--real-overheads
- for | Safe Rust has real, measurable costs: it requires a value at construction time rather than dataflow-based init-before-use, so a large array or small-object allocator ends up eagerly zero-initializing memory it may never read, sometimes bloating codegen enough to block inlining; trivial features can force large refactors via new borrowing schemes, and clones or `Rc` get added defensively to satisfy the borrow checker where they aren't algorithmically necessary; disassembly on nontrivial examples shows bounds checks, unsafe-gated SIMD intrinsics, poorly-optimizing iterators, `RefCell` overhead, and un-collapsible `Result` wrapping | values: performance | sources: f005516@dataangel replies 2025-06-10T07:16:21-05:00, 2025-06-10T11:09:00-05:00, 2025-06-12T07:56:20-05:00, 2025-06-13T20:10:53-05:00
- against | Rust doesn't require init for all variables broadly — it merely requires init-before-use based on dataflow analysis, the same as any ordinary variable; the zero-init cost should only bite in narrow cases like large arrays or read buffers, not as a blanket tax | values: correctness, performance | sources: f005516@rpjohnst replies 2025-06-11T11:16:03-05:00 and 2025-06-12T10:09:38-05:00

### rust-vs-c-inherent-performance--safe-rust-matches
- for | Safe Rust, with zero `unsafe` in the author's own code, handles several coordinated CPU-bound threads (refresh, per-frame update, event processing, asset decoding) doing entirely different work acceptably, where the same coordination would be "really hard" to get right safely in C++ | values: correctness | sources: f013214@John_Nagle reply 2024-01-13T20:31:31
- against | no argument in sources

### rust-vs-c-inherent-performance--safety-cost-acceptable
- for | A real safety cost is worth paying: citing a session where an unsafe/unmanaged-heavy game (Ark: Survival Ascended) crashed three times and topped out near 45 FPS, a 10% perf hit (40 FPS) for a memory-safe implementation that doesn't crash is preferable, and would likely be an acceptable tradeoff generally for people who "just want to play games instead of deal with constant unnecessary interruptions" | values: correctness, performance | sources: f013214@parasyte reply 2024-01-10T18:33:17
- against | no argument in sources

### rust-vs-c-inherent-performance--types-enable-optimizations
- for | Rust puts the equivalent of C's `restrict` on every reference that doesn't contain an `UnsafeCell`, so the no-aliasing guarantee is encoded in the type system rather than left as convention, and Rust is also ahead on pointer-provenance semantics — a real, structural edge over "it's all project-specific" framings | values: correctness, performance | sources: f005516@steveklabnik reply 2025-06-10T14:15:50-05:00
- against | "Rust doesn't stand out" on the one thing that would really matter (aliasing): the borrow checker tells the compiler a reference is the only one that may *modify* through it, but not that nobody else has *access* at all, which is what would actually enable more optimizations — so in practice the discussion is just about which language makes it easier to write fast programs, an ecosystem/library question rather than a language one | values: performance | sources: f005516@qznc reply 2025-06-10T13:45:44-05:00

## safe-wrapper-soundness-scope
### safe-wrapper-soundness-scope--p1
- no argument in sources (its only Claim is excluded: gap voice-below-bar)

### safe-wrapper-soundness-scope--p2
- for | Without a full formal proof, a cache writeback is, as far as can be told, generally a safe operation, and invalidate isn't called on these paths — so the current alignment guarantees are reasonable to call fine for this type at this time, even granting the phrasing is "wishy-washy" | values: correctness | sources: f004804@bugadani PR review comment 2026-06-17T07:36:32Z
- against | no argument in sources

## same-state-transition-trigger
### same-state-transition-trigger--p1
- no argument in sources (its only Claim is excluded: gap voice-below-bar)

### same-state-transition-trigger--p2
- for | It doesn't really make sense to react to changing into a state you're already in — that's a no-op by nature and shouldn't trigger anything | values: simplicity | sources: f004398@Freyja-moth comment 2026-03-12T16:51:05Z
- against | Some users have specifically pushed for allowing same-state transitions to trigger, precisely to support a "reload" pattern, so the naive (non-special-cased) behavior is the right default | values: value-candidate: use-case-flexibility (flagged: argues from accommodating a requested usage pattern, not from the six listed values) | sources: f004398@alice-i-cecile comment 2026-03-12T19:46:57Z

### same-state-transition-trigger--p3
- for | Some users have specifically pushed for allowing same-state transitions to trigger, precisely to support a "reload" pattern, so the naive (non-special-cased) behavior is the right default here | values: value-candidate: use-case-flexibility (flagged: argues from accommodating a requested usage pattern, not from the six listed values) | sources: f004398@alice-i-cecile comment 2026-03-12T19:46:57Z
- against | It doesn't really make sense to react to changing into a state you're already in — that's a no-op by nature and shouldn't trigger anything | values: simplicity | sources: f004398@Freyja-moth comment 2026-03-12T16:51:05Z

## scoped-impls-nameable
### scoped-impls-nameable--p1
- for | Naming these implementations is "squarely detrimental," mainly for clarity but also syntactically and for ease of use; anonymity keeps coherence checking simple within one scope, lets the module double as the name in error messages, and avoids the breaking-change rules naming would force whenever an implementation is later broadened | values: simplicity, stability | sources: f009123@Tamschi reply 2023-12-05T20:39:46.548Z
- against | Names are wanted: with them, two implementations of the same trait/type could coexist in one module (e.g. case-sensitive and case-insensitive `Eq`), and an explicit mechanism to specify a type with explicitly chosen impls would let the implicit scoped-impl behavior desugar from something writable, and let compiler error messages point at a normal path instead of "the impl from this module" | values: approachability, simplicity | sources: f009123@scottmcm reply 2023-11-29T03:31:09.374Z; f009123@Nadrieril reply 2023-12-05T13:43:01.887Z

### scoped-impls-nameable--p2
- for | Names are wanted: an explicit mechanism to specify a type along with explicitly chosen impls would make the implicit scoped-impl behavior desugar from something writable, making it easier to follow what's happening even if users rarely write the explicit form by hand; names would also let two implementations of the same trait/type coexist in one module and let compiler errors point at a normal path instead of "the impl from this module" | values: approachability, simplicity | sources: f009123@scottmcm reply 2023-11-29T03:31:09.374Z; f009123@Nadrieril reply 2023-12-05T13:43:01.887Z
- against | Naming these implementations is "squarely detrimental," mainly for clarity but also syntactically and for ease of use; anonymity keeps coherence checking simple within one scope, lets the module double as the name in error messages, and avoids the breaking-change rules naming would force whenever an implementation is later broadened | values: simplicity, stability | sources: f009123@Tamschi reply 2023-12-05T20:39:46.548Z

## scratch-register-type-enforced
### scratch-register-type-enforced--encode-in-types
- for | As a further-out fix beyond minimizing live ranges, proposes relying on the type system to identify/audit scratch-register usage, or providing exclusive access to scratch registers analogous to allocatable registers, since passing a scratch register as a parameter extends its live range and raises unintentional-clobbering risk | values: correctness | sources: f002466@saulecabrera comment 2025-01-04T16:38:14Z
- against | no argument in sources

### scratch-register-type-enforced--p1
- for | Because scratch registers aren't tracked by the regalloc and must be used sparingly and with extreme caution — a misuse risking unintentional clobbering and subtle bugs — the live range should be minimized and passing them as parameters avoided, even if that means redefining signatures and accepting duplication across ISA-specific paths | values: correctness | sources: f002466@saulecabrera comment 2025-01-04T16:38:14Z
- against | no argument in sources

## serde-centralization
### serde-centralization--p1
- for | Rust's orphan rules have created a real ecosystem composition problem: crates that want to interoperate with a popular derive macro like serde must piggyback on it rather than add independent support, which functionally corners the ecosystem around one crate | values: simplicity | sources: f011413@~00:03:06-00:04:00
- against | no argument in sources

### serde-centralization--p2
- for | Rather than generating a new derive for every new trait or behavior, crates should ship structural data about their types once and let behaviors build generically over that data — the many-crates-on-one-derive idea is sound, but the strategy needs adjusting | values: simplicity, iteration-speed | sources: f011413@~00:04:00-00:05:00
- against | no argument in sources

## serialization-format-choice
### serialization-format-choice--cbor-for-no-std
- for | Switched metadata serialization from MessagePack (`rmp-serde`) to CBOR (`ciborium`) because `rmp-serde` isn't no-std compatible and its upstream has been inactive over a year, while CBOR is IETF-standardized, serde-recommended, no-std-capable, and preserves enum variant information | values: stability | sources: f003587@PR #3792 comment 2025-10-10T14:21:49Z
- against | no argument in sources

### serialization-format-choice--established-binary-format
- for | Postcard is preferred over a bespoke or JSON serialization as a simpler, well-defined format similar to what's already being generated; separately, since postcard is non-self-describing, enum case order must be preserved as a stability contract for the protocol to remain stable long-term — a requirement to design around, not a reason to avoid it | values: simplicity, stability | sources: f002300@PR comment 2024-11-20; f003590@§ RPC protocol
- against | no argument in sources

### serialization-format-choice--no-custom-format
- for | After evaluating `serde_yml`, `serde_yaml` and `facet-yaml`, YAML tooling in the Rust ecosystem is a dead end for i128 support; defining a custom config language is an alternative, but probably too much effort to "just try it" | values: correctness | sources: f003030@comment @bjoernQ 2025-06-05T11:30:38Z
- against | The YAML spec doesn't *mandate* support for wider integers, but it also doesn't *forbid* them, so the sudden pessimism about the format isn't warranted | values: correctness | sources: f003030@comment @bugadani 2025-06-05T11:43:25Z

### serialization-format-choice--p1
- for | Bincode is called out as a risky format for anything new because it depends on the exact order and type of struct fields; legacy column families keep it, but new ones should not use it | values: stability | sources: f000267@Zebra Cached State Database Implementation § Data Formats
- against | no argument in sources

### serialization-format-choice--ship-now-switch-later
- for | This format is strictly internal right now, so proceed with YAML plus workarounds, and switch library or format later if something better shows up | values: iteration-speed | sources: f003030@comment @MabezDev 2025-06-10T09:48:30Z
- against | no argument in sources

### serialization-format-choice--toml-for-consistency
- for | Why not TOML, to stay consistent with the rest of the Rust ecosystem? | values: value-candidate: ecosystem-consistency (flagged: argues from matching ecosystem convention, not from the six listed values) | sources: f003030@comment @okhsunrog 2025-05-24T17:23:55Z
- against | TOML's representation is inconvenient for this use case; YAML is the nicest representation available | values: approachability | sources: f003030@comment @bjoernQ 2025-05-24T17:33:48Z

### serialization-format-choice--yaml-for-convenience
- for | TOML's representation is inconvenient for this use case; YAML is the nicest representation available, and the spec doesn't forbid wider integers even if it doesn't mandate them, so the missing i128 support is a library gap worth patching (or trying an alternative crate like facet-yaml) rather than a reason to abandon YAML — especially since `serde_yml` itself looks unmaintained | values: approachability, correctness | sources: f003030@comment @bjoernQ 2025-05-24T17:33:48Z; f003030@comments @bugadani 2025-06-04T15:24:04Z, 2025-06-04T15:39:12Z, 2025-06-05T11:43:25Z
- against | Why not TOML, to stay consistent with the rest of the Rust ecosystem? Separately: after evaluating `serde_yml`, `serde_yaml` and `facet-yaml`, YAML tooling is a dead end for i128 support | values: value-candidate: ecosystem-consistency; correctness | sources: f003030@comment @okhsunrog 2025-05-24T17:23:55Z; f003030@comment @bjoernQ 2025-06-05T11:30:38Z

## shared-hw-resource-refcount-vs-raii
### shared-hw-resource-refcount-vs-raii--p1
- for | Unless references are counted per modem clock controller, repeatedly calling the function to disable the PHY clock on one controller would eventually disable it even while a different modem still relies on it — so a `RadioClockController` needs its own per-modem reference count | values: correctness | sources: f003169@Frostie314159 comment 2025-06-24T13:26:21Z
- against | Questions why a separate controller and manual ref-count are needed at all when only the peripheral singletons — already unique and exclusive by construction — can touch the clock; the clock-control logic should live directly on the radio peripheral structs instead | values: simplicity | sources: f003169@bugadani comment 2025-06-25T13:18:42Z

### shared-hw-resource-refcount-vs-raii--p2
- for | Questions why a separate controller and manual ref-count are needed at all when only the peripheral singletons — already unique and exclusive by construction — can touch the clock; proposes implementing the clock-control logic directly on the radio peripheral structs; the author ultimately removed the separate ref-counted controller in favor of this | values: simplicity | sources: f003169@bugadani comment 2025-06-25T13:18:42Z; f003169@Frostie314159 comment 2025-07-01T15:05:34Z
- against | Unless references are counted per modem clock controller, repeatedly calling the function to disable the PHY clock on one controller would eventually disable it even while a different modem still relies on it | values: correctness | sources: f003169@Frostie314159 comment 2025-06-24T13:26:21Z

## shared-mutable-state-vs-explicit-passing
### shared-mutable-state-vs-explicit-passing--restructure-for-explicit-ownership
- for | Preference runs toward moving mutable state to its owning context rather than wrapping it for sharing: move state onto the owning `Session` rather than adding an internal `Mutex`; prefer no `Arc` even after conceding an immediate `Sync` bound currently requires it; object to a `Buffer` holding an `Arc<Mutex<>>` that lets callers change encoding invisibly, wanting it passed/returned explicitly instead | values: simplicity | sources: f002155@yatekii comments 2024-12-03, 2024-12-19; f003414@conradirwin comment 2025-10-28T01:59:12Z
- against | no argument in sources

### shared-mutable-state-vs-explicit-passing--shared-where-structure-demands
- for | `Rc`/`Arc` are recommended when the program's structure makes it hard to tell how many readers a piece of data will have; `RefCell` moves borrow rules to runtime, works only single-threaded, and panics on violation, so it fits only a narrow range of problems | values: correctness | sources: f005440@§ Automatic memory management and Rust types, paragraphs 3-4
- against | no argument in sources

## silent-fallback-vs-explicit-error
### silent-fallback-vs-explicit-error--fail-loudly
- for | An `allow_missing = true` option that lets the build succeed and then 404 at request time turns a build-time problem into a silent runtime one — a bad default; `unwrap_or_default()` mostly hides the problem rather than fixing it, since a server function that actually sets `ResponseOptions` would silently fail to have its header/status applied; asks whether the code should return an error when multiple TCP sockets are listed, rather than silently using the first, since picking the first could cause odd behavior if it's the wrong one | values: correctness | sources: f004706@PR review comment 2026-09-18T18:13:56Z; f000669@issue #2112 comment 2024-03-29T14:49:12Z; f005079@comment 2026-09-10T22:28:43Z
- against | Proposes patching leptos-axum so a missing `ResponseOptions` context resolves via `unwrap_or_default()` instead of panicking — a workaround for callers who don't touch `ResponseOptions` anyway | values: approachability | sources: f000669@issue #2112 comment 2024-03-06T15:53:46Z

### silent-fallback-vs-explicit-error--silent-fallback
- for | Proposes patching leptos-axum so a missing `ResponseOptions` context resolves via `unwrap_or_default()` instead of panicking — a workaround for callers who don't touch `ResponseOptions` anyway | values: approachability | sources: f000669@issue #2112 comment 2024-03-06T15:53:46Z
- against | The `unwrap_or_default()` fix "mostly hides the problem rather than fixing it," since a server function that actually sets `ResponseOptions` would silently fail to have its header/status applied; better to find and fix the real cause | values: correctness | sources: f000669@issue #2112 comment 2024-03-29T14:49:12Z

## spi-hardware-cs-in-spibus
### spi-hardware-cs-in-spibus--p1
- for | Chip select should just be an ordinary GPIO `Output` pin — that way one bus can address as many targets as there are available GPIOs; hardware chip-select complicates the embedded-hal `SpiBus`/`SpiDevice` split, which is why most HALs tend not to use it | values: simplicity | sources: f004055@jamesmunns comment 2026-01-05T14:30:11Z; f004055@felipebalbi comment 2026-01-07T19:47:44Z
- against | no argument in sources

### spi-hardware-cs-in-spibus--p2
- no argument in sources (its only Claim is excluded: gap voice-below-bar)

## std-naming-conventions-strictness
### std-naming-conventions-strictness--loose
- no argument in sources (its only Claim is excluded: gap voice-below-bar)

### std-naming-conventions-strictness--strict
- for | `into_` should only be used where the method actually consumes `self` — a name that doesn't match its ownership signature should be renamed; `to_owned` is not a bad name: the receiver is neither doing the owning nor being owned, it's being copied into a different form, so `own()` would misdescribe the operation, and the Rust API Guidelines document is the standing rationale for the `to_` prefix here | values: correctness | sources: f003587@PR #3792 review comments 2025-10-09T12:33:22Z, 2025-10-09T13:27:11Z; f009236@replies 2025-01-07T16:10:44, 2025-01-08T01:57:00
- against | no argument in sources

## tail-expression-vs-explicit-return
### tail-expression-vs-explicit-return--p1
- for | Coming from a lot of Rust work, the last-expression rule seriously hurts readability for both function returns and `if` expressions — worst of all when the block is long and the last expression sits far from the assignment it feeds | values: approachability | sources: f000576@post @andrews05 2023-11-17T03:44:40Z
- against | no argument in sources

### tail-expression-vs-explicit-return--p2
- no argument in sources (its only Claim is excluded: gap voice-below-bar)

## test-via-real-entry-point
### test-via-real-entry-point--p1
- for | Existing tests drive the toggle/switch methods directly rather than the deferred mouse-event path itself, so they'd keep passing even if the real keybinding wiring broke — wants at least one test to dispatch the real action via a keystroke against the real strip, since "nothing tests the actual gesture" even after a fix | values: correctness | sources: f004772@comment 2026-08-06T16:39:43Z; f004772@comment 2026-08-07T22:48:19Z
- against | no argument in sources

### test-via-real-entry-point--p2
- for | The dangerous bugs aren't in new code, they're in what old code used to do that nothing does anymore — a refactor can silently stop enforcing a check with no test failing and no diff showing a deleted check; requires inventorying every rejection the old code could produce, testing every parse-time rejection through the actual production entry point rather than only the check's own unit tests, and auditing fallible conversions (`.ok()`, `unwrap_or`, defaulted `try_from`) that could silently turn an invalid value into one a check treats as benign, citing two real incidents that slipped through this exact gap with green CI | values: correctness | sources: f000267@Refactoring Consensus-Critical Code
- against | no argument in sources

## tokio-as-default-runtime
### tokio-as-default-runtime--p1
- for | Recommends Tokio as the guide's runtime for most readers because it's general purpose, the most popular in the ecosystem, and good for both getting started and production, while noting other runtimes may perform better or simplify code in some circumstances | values: approachability | sources: f000233@chapter "Async and Await" § The runtime
- against | There is no asynchronous runtime in the standard library, and none are officially recommended — Tokio, async-std, smol and fuchsia-async are listed as options without ranking, and cross-runtime incompatibility (Tokio's mio-based reactor vs. the async-executor/futures-I/O-trait world of async-std and smol) is a reason to research fit before committing to one | values: stability | sources: f000233@chapter "The Async Ecosystem" § Popular Async Runtimes

### tokio-as-default-runtime--p2
- for | There is no asynchronous runtime in the standard library, and none are officially recommended — Tokio, async-std, smol and fuchsia-async are listed as options without ranking, and cross-runtime incompatibility is a reason to research fit before committing to one | values: stability | sources: f000233@chapter "The Async Ecosystem" § Popular Async Runtimes
- against | Recommends Tokio as the guide's runtime for most readers because it's general purpose, the most popular in the ecosystem, and good for both getting started and production | values: approachability | sources: f000233@chapter "Async and Await" § The runtime

### tokio-as-default-runtime--tokio-default
- for | Despite criticisms of Tokio, the alternatives are limited — async-std stale, smol inactive, glommio Linux-only — so Tokio remains the best option, reinforced by being quinn's default | values: stability | sources: f005159@article body, "Choosing a Runtime" section
- against | no argument in sources

## tokio-axum-vs-nginx-performance
### tokio-axum-vs-nginx-performance--p1
- no argument in sources (its only Claim is excluded: gap voice-below-bar)

### tokio-axum-vs-nginx-performance--p2
- for | Cloudflare has replaced nginx in production with the Tokio-based Pingora proxy — Tokio is pretty fast out of the box, and Rust's async has been designed from the ground up to be very low overhead | values: performance | sources: f005360@kornel reply 2024-10-13T08:05:40-05:00
- against | no argument in sources

### tokio-axum-vs-nginx-performance--p3
- for | Tokio and Hyper are both very fast on their own, but Axum adds its own routing/extractor overhead on top — surprising, since Actix-Web previously topped benchmarks while also providing routing and extractors, so Axum wasn't expected to differ much; where complex path routing and extractors aren't needed, it's probably better to use Hyper and Tower directly | values: performance | sources: f005360@mattya reply 2024-10-13T08:47:00-05:00; f005360@kornel reply 2024-10-13T09:11:28-05:00
- against | no argument in sources

## trait-impl-boilerplate-mechanism
### trait-impl-boilerplate-mechanism--p1
- no argument in sources (its only Claim is excluded: gap voice-below-bar)

### trait-impl-boilerplate-mechanism--p2
- for | There's really no need to write out `type Item = i32;` when it's the only possible thing given the method body — the compiler should infer associated types like `Iterator::Item` from context, simplifying `Add`, `Sub`, `IntoIterator` and `Deref` impls without new surface syntax | values: simplicity | sources: f009292@reply 2025-09-08T23:27:35.279Z
- against | no argument in sources

## typed-wrapper-vs-raw-access
### typed-wrapper-vs-raw-access--p1
- for | A raw matrix type cannot guarantee it represents a pure rotation, isometry, or even an invertible transform, so dedicated transformation types are recommended instead of raw matrices | values: correctness | sources: f000217@"Computer-graphics recipes" chapter, "Transformations using Matrix4"
- against | no argument in sources

### typed-wrapper-vs-raw-access--p2
- for | Repeatedly questions raw volatile register operations in favor of PAC-generated typed accessors, treating a missing PAC accessor as a bug to be fixed in the PAC itself rather than worked around with manual bit ops; likewise, typing a column family's name out every time is error-prone (a typo causes a panic since the column family doesn't exist), so the name and type of each column family should be defined once and every read/write routed through a typed method | values: correctness | sources: f004055@comments 2026-01-05T14:14:27Z, 2026-01-07T19:35:31Z; f000267@Zebra Cached State Database Implementation § Adding a Column Family
- against | no argument in sources

## unchecked-unwrap-vs-safe-abort
### unchecked-unwrap-vs-safe-abort--p1
- for | Panics translate into aborts on wasm32-unknown-unknown anyway, so a safe helper that calls `process::abort()` on None/Err gives the same behavior as unwrap without the formatted-panic code bloat | values: performance | sources: f000256@§ "Shrinking .wasm Code Size" — "Avoid Panicking"
- against | no argument in sources (p2 and p3 present a further, riskier option rather than a rebuttal)

### unchecked-unwrap-vs-safe-abort--p2
- for | The `unreachable` crate's unsafe `unchecked_unwrap` is a further, riskier alternative, restricted to cases where the programmer is "110% sure" the assumption holds — and only in release builds, keeping checked behavior in debug | values: performance, correctness | sources: f000256@§ "Shrinking .wasm Code Size" — "Avoid Panicking"
- against | no argument in sources (this option is presented as an additional, stricter step beyond p1, not a rebuttal of it)

### unchecked-unwrap-vs-safe-abort--p3
- for | The safe `process::abort`-based `unwrap_abort` is the default way to drop panic-infrastructure bloat; the unsafe `unchecked_unwrap` is a further step, explicitly conditioned on near-total certainty plus a debug build that still checks | values: performance, correctness | sources: f000256@§ "Shrinking .wasm Code Size" — "Avoid Panicking"
- against | no argument in sources

## unsafe-mental-model
### unsafe-mental-model--p1
- for | Unsafe code isn't for violating Rust's invariants, it's for maintaining them manually | values: correctness | sources: f012469@post by @bluss dated 2015-04-27T11:36:54Z
- against | no argument in sources

### unsafe-mental-model--p2
- for | Using unsafe is less "nuclear option" and more "diplomacy has failed" | values: correctness | sources: f012469@post by @rgdmarshall dated 2015-12-14T07:53:53Z
- against | no argument in sources

## wasi-path-workaround-vs-breaking-fix
### wasi-path-workaround-vs-breaking-fix--p1
- no argument in sources (its only Claim is excluded: gap voice-below-bar)

### wasi-path-workaround-vs-breaking-fix--p2
- no argument in sources (its only Claim is excluded: gap voice-below-bar)

## wasm-allocator-choice
### wasm-allocator-choice--p1
- for | wee_alloc is designed for situations where you need some kind of allocator but not a particularly fast one, and happily trades allocation speed for smaller code size — the default allocator costs roughly 10KB, and wee_alloc saves most of that | values: performance | sources: f000256@§ "Shrinking .wasm Code Size" — "Avoid Allocation or Switch to wee_alloc"
- against | no argument in sources (p2 and p3 present alternative/complementary size-reduction techniques from the same guide, not a rebuttal)

### wasm-allocator-choice--p2
- for | For a single-instance program, exporting operations on a static mut global with double-buffering removes all dynamic allocation entirely, allowing a `#![no_std]` crate with no allocator dependency at all, for maximum size reduction | values: performance | sources: f000256@§ "Shrinking .wasm Size" — exercise on static mut globals
- against | no argument in sources

### wasm-allocator-choice--p3
- for | The choice is explicitly a speed-for-size trade: the default allocator's ~10KB footprint is the cost of keeping it, and wee_alloc's slower allocation is the cost of switching | values: performance | sources: f000256@§ "Shrinking .wasm Code Size" → Avoid Allocation or Switch to wee_alloc
- against | no argument in sources

## wasm-core-sum-types
### wasm-core-sum-types--p1
- for | The most immediate benefit first-class sum types would give over shoe-horning sum types into struct subtypes is a `br_table`-like instruction for exhaustively matching on cases — easier to optimize than a chain of `br_on_cast` checks, and lets tools like binaryen reason over a closed case set | values: performance, simplicity | sources: f003074@comment @fitzgen 2025-06-16T18:35:42Z
- against | A custom type descriptor can already store an integer tag for `br_table` dispatch without wasting per-variant space, so primitive sum types would mainly save the trailing cast check — which would require adding a case construct to Wasm, "quite a bit of machinery" for not a lot of relevant generic optimizations | values: simplicity | sources: f003074@comment @rossberg 2025-06-16T21:05:40Z

### wasm-core-sum-types--p2
- for | A custom type descriptor can already store an integer tag for `br_table` dispatch without wasting per-variant space, so primitive sum types would mainly save the trailing cast check — which would require adding a case construct to Wasm, quite a bit of machinery for not a hell lot of relevant generic optimizations | values: simplicity | sources: f003074@comment @rossberg 2025-06-16T21:05:40Z
- against | The most immediate benefit first-class sum types would give over shoe-horning sum types into struct subtypes is a `br_table`-like instruction for exhaustively matching on cases — easier to optimize and lets tools like binaryen reason over a closed case set | values: performance, simplicity | sources: f003074@comment @fitzgen 2025-06-16T18:35:42Z

## web-framework-actor-vs-tower
### web-framework-actor-vs-tower--p1
- for | Defaults students to Clap for CLI and Actix for web, "unless you have a compelling reason to switch to a new framework" | values: approachability | sources: f000149@Chapter 1, project spec bullet on frameworks
- against | no argument in sources

### web-framework-actor-vs-tower--p2
- for | Actix Web uses the actor model and has its own mature middleware system; both frameworks are fast and production-ready, but Axum's design philosophy is often preferred for its simplicity and tight integration with Tokio | values: simplicity | sources: f011605@FAQ "What is the difference between Axum and Actix Web?"
- against | no argument in sources

## web-session-store-default
### web-session-store-default--p1
- for | Following Rails' precedent, new apps should start by storing sessions inside the cookie, both encrypted and signed, switchable later via `tower-sessions` — Rails itself calls the choice "controversial," but it keeps initial friction low | values: approachability | sources: f001365@issue #561 comment 2024-06-24T06:14:39Z
- against | There's no way to force-invalidate a session or change permissions on the fly when the data lives on the client, so whatever effort is saved by skipping a server-side store is negated by that inflexibility | values: correctness | sources: f001365@issue #561 comment 2024-06-24T06:50:58Z

### web-session-store-default--p2
- for | There's no way to force-invalidate a session or change permissions on the fly when the data lives on the client, so whatever effort is saved by skipping a server-side store is negated by that inflexibility; encrypted cookies also aren't good practice in production since they can enable replay attacks — storing sensitive data server-side is always the better choice | values: correctness | sources: f001365@issue #561 comment 2024-06-24T06:50:58Z
- against | Following Rails' precedent, new apps should start by storing sessions inside the cookie, both encrypted and signed, switchable later via `tower-sessions`, to keep initial friction low | values: approachability | sources: f001365@issue #561 comment 2024-06-24T06:14:39Z

## web-wasm-target-workaround-vs-target
### web-wasm-target-workaround-vs-target--p1
- for | The root cause is the lack of a way to signal wasm-bindgen usage to the compiler — there should finally be a discussion of a proper `wasm32-web`/`wasm32-bindgen` target instead, now that the project has active maintainers again, to fix this class of problem generally | values: stability | sources: f003558@comment 2025-09-19T12:38:24Z
- against | There has been zero progress on a proper Web-WASM target in about four years with no hope of getting one anytime soon, so the immediate need is a solution that works with current stable Rust and the declared MSRV | values: iteration-speed | sources: f003558@comments 2025-09-19T12:53:59Z, 2025-09-19T13:06:16Z

### web-wasm-target-workaround-vs-target--p2
- for | There has been zero progress on a proper Web-WASM target in about four years with no hope of getting one anytime soon, so the immediate need is a solution that works with current stable Rust and the declared MSRV | values: iteration-speed | sources: f003558@comments 2025-09-19T12:53:59Z, 2025-09-19T13:06:16Z
- against | The root cause is the lack of a way to signal wasm-bindgen usage to the compiler — there should finally be a discussion of a proper `wasm32-web`/`wasm32-bindgen` target instead, now that the project has active maintainers again | values: stability | sources: f003558@comment 2025-09-19T12:38:24Z

## what-counts-as-semver-breaking
### what-counts-as-semver-breaking--p1
- for | Adding a variant to a public enum that is not marked `#[non_exhaustive]` is breaking, because downstream match expressions that were previously exhaustive stop compiling | values: stability | sources: f000267@Changelog Guidelines § Part 3, "What is breaking for library consumers?"
- against | no argument in sources

### what-counts-as-semver-breaking--p2
- for | A dependency bump forces a major-version bump of the crate itself when the dependency's own semver-incompatible change exposes types that appear in the crate's public API, since two incompatible versions of the same crate can't unify for downstream consumers; a purely internal dependency needs no changelog entry at all | values: stability | sources: f000267@Changelog Guidelines § Dependency updates
- against | no argument in sources

### what-counts-as-semver-breaking--p3
- for | An MSRV bump is itself classified as a breaking change for the crate, not a minor or patch-level change | values: stability | sources: f000267@Changelog Guidelines § Part 4, Compatibility
- against | no argument in sources
