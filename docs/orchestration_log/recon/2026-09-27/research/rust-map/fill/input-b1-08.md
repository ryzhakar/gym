# Blind fill input, batch 1, file 08 of 13

For each Claim below, name the one Position of its Question that the Claim supports (a Position id from the list), or `none` if it supports none of them. The Claims are in random order.

## Question `middleware-hook-vs-typestate`

Should a web framework provide a generic "runs on every request" middleware hook, or is it better to omit global middleware in favor of an explicit typestate pattern that forces handlers to obtain capabilities (like authorization) only by calling through the relevant subsystem?

Positions:
- `middleware-hook-vs-typestate--p1`: Typestate explicit preferred over middleware
- `middleware-hook-vs-typestate--p2`: Global per request middleware hook expected

Claims:
- `a-saL1-f005454-c4` · Voice: steveklabnik · Source: https://lobste.rs/s/pjtizh (`f005454`) · Date: 2025-02-25 · Locator: reply, 2025-02-25T07:13:08-06:00, elaborated 2025-02-25T09:05:55-06:00
  - Quote: "I'm into it. I'm a big fan of the typestate pattern... I like that it's so straightforward. No more worrying about the order various handlers run…"
  - Paraphrase: Endorses Dropshot's deliberate omission of a generic per-request middleware hook in favor of the typestate pattern: a handler can only obtain an `Authorization` value by calling through the authorization subsystem (itself requiring a `User` obtained only via authentication), eliminating the subtle ordering/dependency bugs he associates with Rails-style before/after/around middleware.
- `a-saL1-f005454-c5` · Voice: insanitybit · Source: https://lobste.rs/s/pjtizh (`f005454`) · Date: 2025-02-25 · Locator: reply, 2025-02-25T01:56:21-06:00, quoting the Dropshot README's own FAQ
  - Quote: "Why is there no way to add an API handler function that runs on every request? How has this design choice played out? It's been a few years, I'm curious to hear lessons learned."
  - Paraphrase: Flags that Dropshot's own documentation anticipates this as a natural question — i.e. that a global per-request middleware hook is the design most users expect from a web framework — and asks how omitting it has played out in practice.

## Question `minimal-vs-batteries-std`

Should Rust (as language and standard library) aim for minimalism — a small core deferring functionality to crates.io — or be a fuller, "medium-sized"/batteries-included system?

Positions:
- `minimal-vs-batteries-std--p1`: Rust targets medium not minimal
- `minimal-vs-batteries-std--p2`: Stdlib is not batteries included

Claims:
- `a-sa28-f012469-c4` · Voice: DanielKeep (author of "The Little Book of Rust Macros," cited independently elsewhere in this same thread) · Source: https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (`f012469`) · Date: 2015-06-12 · Locator: post by @DanielKeep dated 2015-06-12T13:06:31Z
  - Quote: "Buy Your Own Damn Batteries. cf. 'Python: Batteries Included'."
  - Paraphrase: frames Rust's stdlib philosophy as the opposite of Python's "batteries included"
- `a-sa28-f012469-c3` · Voice: graydon2 (Graydon Hoare, Rust's original language designer) · Source: https://users.rust-lang.org/t/twir-quote-of-the-week/328/1681 (`f012469`) · Date: 2015-06-29 · Locator: post by @johansigfrids dated 2015-06-29T17:33:32Z, sourced "graydon2 on reddit" (no direct reddit permalink given)
  - Quote: "Rust has never aimed to be a 'minimal' language, but a 'medium sized' one."
  - Paraphrase: states Rust never aimed to be minimal, targeted "medium sized" instead

## Question `missing-asset-build-fail-vs-runtime-degrade`

When an expected embedded resource (e.g. a static asset) is missing, should the framework fail the build, or degrade silently at runtime (e.g. serve a 404)?

Positions:
- `missing-asset-build-fail-vs-runtime-degrade--p1`: Fail the build
- `missing-asset-build-fail-vs-runtime-degrade--alt1`: Let the build succeed and degrade at runtime (serve a 404)

Claims:
- `b-sR10-f004706-c1` · Voice: gbj (Greg Johnston, Leptos creator) · Source: https://github.com/leptos-rs/leptos/pull/4715 (`f004706`) · Date: 2026-09-18 · Locator: PR review comment, 2026-09-18T18:13:56Z
  - Quote: "`allow_missing = true` seems bad because it allows for a successful build → 404 rather than a build failure."
  - Paraphrase: an `allow_missing = true` option that lets the build succeed and then 404 at request time is a bad default, because it converts a build-time problem into a silent runtime one

## Question `missing-context-default-vs-surface`

When a context a handler expects (e.g. `ResponseOptions`) is legitimately missing under load, should the code fall back to a silent safe default, or should the panic/error surface so the root cause gets found and fixed?

Positions:
- `missing-context-default-vs-surface--p1`: Silent default workaround
- `missing-context-default-vs-surface--p2`: Surface and fix root cause

Claims:
- `b-sb03-f000669-c2` · Voice: gbj · Source: https://github.com/leptos-rs/leptos/issues/2112 (`f000669`) · Date: 2024-03-29 · Locator: issue #2112, comment 2024-03-29T14:49:12Z
  - Quote: "I'm concerned that the solution ... mostly *hides* the problem rather than fixing it"
  - Paraphrase: worried the `unwrap_or_default()` fix "mostly *hides* the problem rather than fixing it," since a server function that actually sets `ResponseOptions` would silently fail to have its header/status applied; prefers finding and fixing the real cause (a disposed Runtime), to be revisited in 0.7
- `b-sb03-f000669-c1` · Voice: glademiller · Source: https://github.com/leptos-rs/leptos/issues/2112 (`f000669`) · Date: 2024-03-06 · Locator: issue #2112, comment 2024-03-06T15:53:46Z
  - Quote: "the workaround I am using at the moment is to patch leptos-axum by changing this line ... to let res_options = use_context::<ResponseOptions>().unwrap_or_default().0;"
  - Paraphrase: proposes patching leptos-axum so the missing-context `.unwrap()` becomes `use_context::<ResponseOptions>().unwrap_or_default().0`, as a workaround for the panic, for callers not using `ResponseOptions` to modify the response

## Question `ml-dataset-eager-vs-lazy`

Should a machine-learning dataset abstraction that loads segmentation masks/images eagerly materialize every item into memory (e.g. building an `InMemoryDataset`), or support lazy/streaming access, given that images or datasets can be large?

Positions:
- `ml-dataset-eager-vs-lazy--p1`: Current eager in-memory materialization is inadequate for large datasets, unresolved
- `ml-dataset-eager-vs-lazy--alt1`: Eager in-memory materialization is adequate
- `ml-dataset-eager-vs-lazy--alt2`: lazy or streaming access

Claims:
- `a-sa03-f002243-c1` · Voice: anthonytorlucci · Source: https://github.com/tracel-ai/burn/pull/2426 (`f002243`) · Date: 2024-10-26 · Locator: PR review comment
  - Quote: "As @laggui pointed out, this could be problematic for large images or large datasets. I'm not sure what the solution is here."
  - Paraphrase: Notes that `new_segmentation_with_items` ultimately calls `with_items`, which builds an `InMemoryDataset`, and that maintainer laggui had already flagged this as potentially problematic for large images or large datasets, without yet knowing the fix.

## Question `modulo-vs-branch-wraparound`

In hot loops needing wraparound indexing, use modulo arithmetic or branch on edge cases with a manually unrolled loop?

Positions:
- `modulo-vs-branch-wraparound--p1`: Branch unrolled(chosen)
- `modulo-vs-branch-wraparound--alt1`: Modulo arithmetic

Claims:
- `a-sB02-f000256-c5` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "Time Profiling" — "Making Time Run Faster"
  - Quote: "if we use ifs for the edge cases and unroll this loop, the branches should be very well-predicted by the CPU's branch predictor."
  - Paraphrase: modulo-based edge wraparound in live_neighbor_count costs a div instruction on the common non-edge case; replacing it with if-branches and a manually unrolled neighbor loop lets the branch predictor do the work instead, measured at a 7.61x speedup.

## Question `multiple-algorithms-autotune`

should a numerics/kernel library ship one fixed algorithm per operation, or ship several algorithm implementations and autotune between them at runtime?

Positions:
- `multiple-algorithms-autotune--p1`: Ship multiple algorithms (existing "direct" plus a new `im2col`/GEMM path) and autotune, even though the new path trades memory for speed
- `multiple-algorithms-autotune--alt1`: One fixed algorithm per operation

Claims:
- `b-sR05-f002048-c1` · Voice: wingertge (PR author, tracel-ai/burn contributor) · Source: https://github.com/tracel-ai/burn/pull/2287 (`f002048`) · Date: 2024-09-17 · Locator: tracel-ai/burn#2287, PR description, 2024-09-17T15:20:57Z. · L853-L865.
  - Quote: "Adds the required infrastructure to autotune `conv2d` and `conv_transpose2d`, as well as adding a second algorithm based on `im2col` which provides significant speedups at the cost of memory usage."
  - Paraphrase: ship multiple algorithms (existing "direct" plus a new `im2col`/GEMM path) and autotune, even though the new path trades memory for speed.

## Question `multitenant-resource-allocation`

should a multi-tenant compute platform allocate resources via static per-request/per-tenant reservation (Kubernetes-style CPU requests/limits), or via dynamic, system-wide throttling of individual noisy tenants?

Positions:
- `multitenant-resource-allocation--p1`: Dynamic system-wide throttling over static per-tenant resource reservation
- `multitenant-resource-allocation--alt1`: Static per-tenant reservation (Kubernetes-style requests and limits)

Claims:
- `a-saL2-f011092-c4` · Voice: Luca Casonato · Source: https://youtube.com/watch?v=YcujtU0LA9Y (`f011092`) · Date: 2024-02-13 · Locator: ~00:37:27-00:39:29 (Q&A, directly answering a comparison to Kubernetes-style CPU requests)
  - Quote: "we have the ability... to isolate tenants in such a way that if there's a single tenant that comes and wants to use a bunch of resources we're going to throttle that single tenant before we throttle everyone else on the platform... we measure... the entire system"
  - Paraphrase: rather than measuring and reserving resources per tenant the way Kubernetes CPU requests/limits do, the platform measures utilization across the entire system and throttles an individual heavy tenant before throttling everyone else, accepting that a compute-intensive tenant may sometimes get lower throughput than dedicated hardware would give it

## Question `multitenant-shared-readonly-pages`

in a multi-tenant sandboxed runtime, should tenants share read-only memory pages (e.g. a JS engine's read-only heap) for efficiency, or should each tenant get fully isolated memory, given the side-channel risk (ASLR, Spectre-style timing attacks) shared pages introduce?

Positions:
- `multitenant-shared-readonly-pages--p1`: Share read-only memory pages across tenants, mitigate side-channels via defense-in-depth
- `multitenant-shared-readonly-pages--alt1`: Fully isolated memory per tenant

Claims:
- `a-saL2-f011092-c2` · Voice: Luca Casonato · Source: https://youtube.com/watch?v=YcujtU0LA9Y (`f011092`) · Date: 2024-02-13 · Locator: ~00:40:37-00:42:43
  - Quote: "the things that we share are code pages that are entirely read only that can never be modified... V8 has a read-only heap" / "we don't rely on a single layer of security for any of our security measures... we take very specific care to avoid timing side channel attacks by not exposing any high resolution timers"
  - Paraphrase: the runtime shares memory pages across tenants only when they are entirely read-only and unmodifiable (e.g. V8's read-only heap of intrinsic JS strings); acknowledges this raises ASLR-adjacent concerns, and states they don't rely on a single security layer — they specifically avoid exposing high-resolution timers to block timing/Spectre-style side-channel attacks, on top of other sandbox layers

## Question `mutex-vs-atomics`

Locks or lock-free atomics for shared mutable state?

Positions:
- `mutex-vs-atomics--atomics-over-locks`: Avoid locks; prefer atomics
- `mutex-vs-atomics--atomics-carry-own-bugs`: Atomics carry their own bug class
- `mutex-vs-atomics--mutex-unless-contended`: Plain mutexes unless contention is high

Claims:
- `b-sb23-f011233-c2` · Voice: Evgenii Seliverstov · Source: https://youtube.com/watch?v=zQgN75kdR9M (`f011233`) · Date: 2025-02-26 · Locator: ~29:29-30:32
  - Quote: "if you have a lot of chats and you have a lot of locks you should probably go with lock free data structures[;] if the lock is rarely acquired ... you better use the normal mutex"
  - Paraphrase: explicit decision rule offered to the audience: if there are many threads and heavy lock contention, move to lock-free data structures (crossbeam, parking_lot); if a lock is rarely contended, a normal mutex-based structure is simpler and just as good, because lock-free implementations bring their own hazards (e.g. the ABA problem)
- `b-sb18-f005600-c2` · Voice: inactive-user · Source: https://lobste.rs/s/fzro7f (`f005600`) · Date: 2025-11-01 · Locator: lobste.rs/s/fzro7f, comment 2025-11-01T02:14:18-05:00 (context: also 2025-10-31T23:05:36-05:00, arguing neither locks nor hand-rolled atomics belong in ordinary application code — stick to a well-tested concurrency library)
  - Quote: "You say that like race conditions (with atomics) are not a bad thing"
  - Paraphrase: pushes back that framing atomics/CAS as the safe alternative glosses over the fact that races (stale/inconsistent reads) are themselves a real bug class, not a lesser evil
- `b-sb18-f005600-c1` · Voice: bsder · Source: https://lobste.rs/s/fzro7f (`f005600`) · Date: 2025-11-01 · Locator: lobste.rs/s/fzro7f, comment 2025-11-01T01:54:49-05:00
  - Quote: "In fact, I would argue that the existence of a \"lock\" is *always* a programming bug even inside a library."
  - Paraphrase: argues atomics and compare-and-swap are fine — worst case you get livelock, which is rare and usually recovers — while locks are "always a disaster waiting to happen" because something will die holding one and the whole system grinds to a halt; goes as far as saying a lock's mere existence, even inside a library, is always a programming bug
- `a-sa17-f007846-c1` · Voice: Kerollmops (Tamo) · Source: https://blog.kerollmops.com/how-meilisearch-updates-a-millions-vector-embeddings-database-in-under-a-minute (`f007846`) · Date: 2024-03-25 · Locator: § "Sharing an Iterator Over the Available IDs" → § "The Final Solution"
  - Quote: "That is safe and will yield the right results, but won't scale well as all the threads have to wait for each other on the lock."
  - Paraphrase: Rejected a Mutex-guarded shared iterator for concurrent tree-node ID generation because it forces threads to wait on the lock; replaced it with a lock-free design (RoaringBitmap::select plus AtomicU32/AtomicU64/AtomicBool) that lets threads generate IDs without synchronization.

## Question `nalgebra-typed-api-vs-glm`

For linear algebra/transforms in Rust, should you prefer nalgebra's strongly-typed API (compile-time dimension/invariant checks) or the simpler, GLM-style nalgebra-glm API?

Positions:
- `nalgebra-typed-api-vs-glm--p1`: Nalgebra for rigor and dynamically-sized cases; nalgebra-glm for simplicity
- `nalgebra-typed-api-vs-glm--alt1`: Always nalgebra's strongly typed API
- `nalgebra-typed-api-vs-glm--alt2`: always the GLM-style nalgebra-glm API

Claims:
- `a-sB01-f000217-c1` · Voice: Dimforge (nalgebra maintainers) · Source: https://nalgebra.org/docs (`f000217`) · Date: capture 2025-02-16 (Wayback; underlying doc undated, "living document") · Locator: "The nalgebra-glm crate" chapter, "Should I use nalgebra or nalgebra-glm?"
  - Quote: "If you prefer more rigorous treatments of transformations, with type-level restrictions, then go for nalgebra."
  - Paraphrase: States the choice depends on taste/background — nalgebra for stronger typing and dynamically-sized matrices, nalgebra-glm for those used to C++ GLM or wanting more straightforward functions

## Question `named-default-args-overloading`

Should Rust add named arguments, default arguments or overloading (including for interop)?

Positions:
- `named-default-args-overloading--reject-all-for-simplicity`: Reject all
- `named-default-args-overloading--named-parameters-only`: Named parameters only
- `named-default-args-overloading--overloading-for-interop`: Overloading, at least for interop

Claims:
- `b-sb24-f011312-c6` · Voice: Taylor and Tyler · Source: https://youtube.com/watch?v=Z5M4NIWoMJQ (`f011312`) · Date: 2025-10-03 · Locator: [28:38]-[30:39]
  - Quote: "Today, Rust should just support built-in overloading, especially for interop with existing languages."
  - Paraphrase: Rust has avoided overloading to keep call resolution clear and preserve type inference, but C++ API maintainers rely on being able to add overloads without breaking existing callers; Rust already effectively fakes overloading via trait dispatch (e.g. multiple `From` impls, `Into`'s return-type-directed dispatch) inconsistently, and built-in overloading would also resolve the earlier aliasing problem by letting the compiler pick a safe (exclusive) vs. unsafe (possibly-aliased) overload based on the caller's reference
- `a-sa18-f009104-c1` · Voice: Steve Klabnik · Source: https://steveklabnik.com/writing/arguing-about-arguments (`f009104`) · Date: long-standing prior view, "over a decade" per this 2026-09-21 post's own framing (no earlier dated source read; retrospective self-report only) · Locator: "These features make me uneasy" section
  - Quote: "I've grown to enjoy Rust's simplicity in this area... that's why I've pushed back against the various proposals to extend Rust in this way all of these years."
  - Paraphrase: has for years opposed Rust adding named parameters, optional/default arguments and function overloading (all requested since at least a 12-year-old GitHub issue), arguing the features are numerous, mutually entangled, and that Rust's current rule — one function, one signature, write a differently-named function or a builder if you need variants — keeps the language simple at an acceptable cost
- `a-sa18-f009104-c2` · Voice: Steve Klabnik · Source: https://steveklabnik.com/writing/arguing-about-arguments (`f009104`) · Date: 2026-09-21 · Locator: "I'm okay with named parameters now" section
  - Quote: "I think Rust could be okay with named parameters, but not optional or default ones."
  - Paraphrase: still opposes optional/default arguments and overloading, but has become open specifically to named parameters (not the other bundled features), while flagging unresolved language-design problems the proposal would need to solve: parameters are patterns not names, function-values erase parameter names, left-to-right evaluation order conflicts with letting call sites reorder named arguments (worked example: `consume(data, data.len())` vs. a hypothetical `consume(length: data.len(), data: data)`), and renaming a parameter becomes a breaking change

## Question `narrating-comments`

Should code carry comments that narrate what a simple, self-evident line or private helper does, or should comments be reserved for non-obvious rationale, with narrating comments treated as noise to remove?

Positions:
- `narrating-comments--p1`: No narrating comments
- `narrating-comments--alt1`: Comments that explain what the code does

Claims:
- `a-sa13-f004772-c6` · Voice: ysalitrynskyi · Source: https://github.com/zed-industries/zed/pull/58618 (`f004772`) · Date: 2026-08-18 · Locator: comment @ysalitrynskyi 2026-08-18T21:51:50Z
  - Quote: "Removed the duplicate and stripped the narrating comments across the files these changes touch."
  - Paraphrase: complies by deleting the narrating comments across the touched files
- `a-sa13-f004772-c5` · Voice: SomeoneToIgnore · Source: https://github.com/zed-industries/zed/pull/58618 (`f004772`) · Date: 2026-08-07 · Locator: comment @SomeoneToIgnore 2026-08-07T19:29:54Z
  - Quote: "doc comments narrating one-line private helpers... Same pattern all over the file... removing it all is way better than having them."
  - Paraphrase: flags doc comments that narrate one-line private helpers and per-field docs as a repeating pattern across the file, arguing they should simply be deleted rather than kept or improved

## Question `networking-lib-core-scope`

Should a networking library bundle many protocols and transports in its core, or keep a minimal core with pluggable extensions?

Positions:
- `networking-lib-core-scope--minimal-core-pluggable`: Minimal core, pluggable trait extensions
- `networking-lib-core-scope--alt1`: Bundle many protocols and transports in the core

Claims:
- `a-sa02-f002124-c1` · Voice: ramfox · Source: https://iroh.computer/blog/iroh-0-26-0-Say-Hello-to-Your-Neighbors (`f002124`) · Date: 2024-10-01 · Locator: opening section / "Docs are disabled by default"
  - Quote: "We're doubling down on iroh's networking stack as 'what iroh is' and describing everything else as a custom protocol."
  - Paraphrase: iroh's maintainers deliberately shrank the library's default scope, disabling the higher-level "Docs" sync feature by default and reframing it as a separate protocol layered on the core networking primitive, restating an earlier decision that iroh's networking stack is "what iroh is" and everything else is a custom protocol
- `a-sR11-f004170-c1` · Voice: Rüdiger Klaehn · Source: https://iroh.computer/blog/tor-custom-transport (`f004170`) · Date: 2026-01-27 · Locator: section "What are iroh custom transports anyway?"
  - Quote: "we do not want to add additional transports to the iroh codebase. That would make the code very complex with a maze of feature flags, add a lot of dependencies that most of our customers don't need"
  - Paraphrase: iroh will not build every candidate transport (WebTransport, Bluetooth, Tor, InfiniBand, ...) into the core; adding them all would create a maze of feature flags and drag in dependencies most users don't need, so the library exposes `CustomTransport`/`CustomEndpoint`/`CustomSender` traits for users to plug in only what they need

## Question `new-features-on-old-editions`

When a new language capability doesn't interact with a prior edition's changed semantics, should it be made available on older Rust editions too, or should the edition boundary gate all new capabilities regardless of whether they actually interact with anything that changed?

Positions:
- `new-features-on-old-editions--p1`: Extend back until first interaction
- `new-features-on-old-editions--alt1`: The edition boundary gates all new capabilities

Claims:
- `a-sa20-f009698-c1` · Voice: @nikomatsakis · Source: https://blog.rust-lang.org/2025/05/26/april-project-goals-update (`f009698`) · Date: 2025-04-08 · Locator: "Experiment with ergonomic ref-counting" section, comment posted 2025-04-08
  - Quote: "the reason we do editions and not fine-grained features is because we wish to avoid combianotoric explosion... you should never have to go back and modify an edition migration to work differently. That suggestions you are attempting to push the feature too far back."
  - Paraphrase: reviewing a PR that limited a new `use` keyword/closures to Rust 2021+, argues the reason is not "features are edition-gated by default" but a missing tenet: editions exist to avoid combinatoric-explosion of untested feature/rule interactions, so a feature should be made available on older editions up until the point it interacts with something that changed in a later edition (here, `use` closures interact with the 2021 closure-capture-rule change) — and that you should never have to go back and modify an edition migration to work differently, which would signal the feature was pushed too far back

## Question `new-type-vs-option-for-variant`

When a user requests a new capability variant of an existing type (e.g. a byte-based recorder alongside a file-based one), should the library add a new dedicated type or extend the existing type via a configuration option?

Positions:
- `new-type-vs-option-for-variant--p1`: Extend via option
- `new-type-vs-option-for-variant--alt1`: Add a new dedicated type

Claims:
- `b-sb09-f002567-c6` · Voice: antimora · Source: https://github.com/tracel-ai/burn/pull/2721 (`f002567`) · Date: 2025-03-13 · Locator: comment @antimora 2025-03-13T14:41:08Z, replying to @ivila's 2025-03-12T03:41:24Z request for a `SafeTensorBytesRecorder`
  - Quote: "We don't need a new type. We can provide with an arg option."
  - Paraphrase: rejects adding a new recorder type for byte-based loading; proposes an argument/option on the existing recorder instead.

## Question `nextest-vs-custom-runner`

for scaling `cargo test` across a large multi-binary workspace, should a team adopt cargo-nextest, or build a custom test-runner wrapper when nextest's behavioral changes conflict with existing test assumptions?

Positions:
- `nextest-vs-custom-runner--p1`: Custom test-runner wrapper over cargo-nextest
- `nextest-vs-custom-runner--alt1`: Adopt cargo-nextest

Claims:
- `a-saL2-f011092-c1` · Voice: Luca Casonato · Source: https://youtube.com/watch?v=YcujtU0LA9Y (`f011092`) · Date: 2024-02-13 · Locator: ~00:30:24-00:31:24 (wrapper description) and ~00:34:25-00:35:26 (Q&A on nextest)
  - Quote: "we did actually try next test um but the problem with next test was that it changed too many other related things right like the way it runs its tests... that would cause our test [suite] to fail and we just didn't have the time"
  - Paraphrase: built a custom wrapper around `cargo test` that builds test binaries on one machine, ships them to other machines as a zip, shards execution, and converts cargo's unstable JSON test output into JUnit XML; tried cargo-nextest first but rejected it because its different test-execution model (parallel processes) broke an assumption their own tests relied on — a global mutex used to hand out network ports one at a time — and fixing that would have taken more time than they had

## Question `nightly-feature-autodetection`

Should crates and their build scripts (build probes like autocfg) be free to auto-detect and use nightly-only compiler/library features by default, or must nightly-feature usage always require the final binary author's explicit opt-in?

Positions:
- `nightly-feature-autodetection--p1`: Nightly features must be explicit opt in
- `nightly-feature-autodetection--p2`: Build probes should default to detecting and using nightly features

Claims:
- `a-sa19-f009343-c5` · Voice: Nemo157 · Source: https://internals.rust-lang.org/t/code-compiles-on-playground-but-fails-when-passed-via-stdin-to-rustc/24393 (`f009343`) · Date: 2026-06-29 · Locator: reply, 2026-06-29T15:30:35.384Z
  - Quote: "dependencies see that I am using a nightly compiler and attempt to use other unstable library or compiler features that I don't want them to."
  - Paraphrase: Wants to use nightly for unrelated ergonomic toolchain features while explicitly not consenting to dependencies silently using other unstable library or compiler features just because a nightly compiler was detected.
- `a-sa19-f009343-c4` · Voice: epage · Source: https://internals.rust-lang.org/t/code-compiles-on-playground-but-fails-when-passed-via-stdin-to-rustc/24393 (`f009343`) · Date: 2026-06-29 · Locator: reply, 2026-06-29T17:46:02.300Z
  - Quote: "there is a general principle within the Rust Project that unstable features only impact those who have opted in... Libraries auto-enabling features are running counter to that principle."
  - Paraphrase: States the Rust Project's general principle that unstable features should only affect those who opted in, and that libraries auto-enabling nightly features runs counter to that principle.
- `a-sa19-f009343-c3` · Voice: RalfJung · Source: https://internals.rust-lang.org/t/code-compiles-on-playground-but-fails-when-passed-via-stdin-to-rustc/24393 (`f009343`) · Date: 2026-06-30 · Locator: reply, 2026-06-30T12:20:20.661Z
  - Quote: "nightly features should be opt-in, not opt-out. That's how the entire Rust nightly feature system is designed."
  - Paraphrase: Argues nearly all build probes are subtly broken because cargo doesn't give them enough information, and more fundamentally that nightly features should be opt-in, not opt-out; libraries auto-detecting and using them by default harms nightly users and compiler maintainers debugging regressions.
- `a-sa19-f009343-c7` · Voice: MusicalNinjaDad · Source: https://internals.rust-lang.org/t/code-compiles-on-playground-but-fails-when-passed-via-stdin-to-rustc/24393 (`f009343`) · Date: 2026-06-29 · Locator: reply, 2026-06-29T15:04:10.084Z
  - Quote: "Personally, I prefer a crate that documents clearly if they auto-detect & use nightly features to one that makes me go through that hassle, and choose accordingly."
  - Paraphrase: As a "Group B" ergonomics-motivated developer, argues build probes defaulting to detect-and-use available nightly features is preferable to requiring manual opt-in flags, while acknowledging safety-critical ("Group A") users need a documented way to fully opt out.
- `a-sa19-f009343-c6` · Voice: kpreid · Source: https://internals.rust-lang.org/t/code-compiles-on-playground-but-fails-when-passed-via-stdin-to-rustc/24393 (`f009343`) · Date: 2026-06-29 · Locator: reply, 2026-06-29T15:39:25.162Z
  - Quote: "I don't want my project's dependencies to also implicitly change to making use of unstable features."
  - Paraphrase: When switching to nightly for unrelated reasons (debug flags, a newer compiler), does not want dependencies to implicitly change behaviour by using unstable features; would want any such blanket opt-in to be a separate, explicit flag, never implied by nightly usage alone.

## Question `nightly-gate-feature-vs-cfg`

How should an unstable/nightly-only compiler feature be gated in library code — via a Cargo feature flag, or via a `--cfg` set through RUSTFLAGS?

Positions:
- `nightly-gate-feature-vs-cfg--p1`: Rustflags cfg gate
- `nightly-gate-feature-vs-cfg--alt1`: Gate with a Cargo feature flag

Claims:
- `b-sb06-f002033-c1` · Voice: alexcrichton · Source: https://github.com/bytecodealliance/wasmtime/pull/9251 (`f002033`) · Date: 2024-09-16 · Locator: PR #9251, comment 2024-09-16T15:40:18Z
  - Quote: "with a Cargo feature controlling this it unfortunately doesn't play well with our \"test with all features enabled\" in CI well because it enables the feature when a stable compiler is in use."
  - Paraphrase: recommends gating the tail-call code with `#[cfg(pulley_tail_call)]` set via `RUSTFLAGS`, rather than a Cargo feature, because a Cargo feature gets force-enabled by the "test with all features enabled" CI job even when the compiler in use is stable; this also lets the PR land, checked only by a dedicated nightly `cargo check` job, before upstream rustc codegen support for `become` exists

## Question `nightly-in-production`

Should production code depend on nightly-only features (e.g. portable SIMD) or stay on stable?

Positions:
- `nightly-in-production--stable-only`: Stable only
- `nightly-in-production--nightly-when-it-pays`: Nightly when its safety and ergonomics pay (portable SIMD)

Claims:
- `a-saL2-f011092-c5` · Voice: Luca Casonato · Source: https://youtube.com/watch?v=YcujtU0LA9Y (`f011092`) · Date: 2024-02-13 · Locator: ~00:46:45-00:47:45 (Q&A)
  - Quote: "we do not rely on unstable features and we have not relied on unstable features and we are not planning to rely on unstable features"
  - Paraphrase: states plainly that the team does not, has not, and does not plan to rely on unstable Rust features (with a possible narrow exception for an unstable JSON test-message-format flag he wasn't sure was still unstable), and that all their foundational crates are published to crates.io with no unpublished dependencies
- `b-sb23-f011233-c3` · Voice: Evgenii Seliverstov · Source: https://youtube.com/watch?v=zQgN75kdR9M (`f011233`) · Date: 2025-02-26 · Locator: ~36:39-39:43
  - Quote: "you don't need to write all the ins[truction]s ... you write the safe code not unsafe ... portable Sy[md] is the choice"
  - Paraphrase: contrasts writing raw target-feature-gated intrinsics (unsafe, verbose, must be manually wrapped and feature-detected at runtime) with std::simd's portable_simd, which lets you write safe, ordinary-looking iterator code that the compiler lowers to the right instructions per architecture; recommends it as "the choice" even though it currently requires nightly

## Question `no-std-for-wasm`

Does compiling to WebAssembly require disabling the standard library (no_std), the way embedded targets do?

Positions:
- `no-std-for-wasm--p1`: No_std is embedded-only, not needed for wasm
- `no-std-for-wasm--alt1`: Wasm requires `no_std`, as embedded does

Claims:
- `a-sB01-f000217-c4` · Voice: Dimforge (nalgebra maintainers) · Source: https://nalgebra.org/docs (`f000217`) · Date: capture 2025-03-22 (Wayback; underlying doc undated) · Locator: "WASM and embedded targets" chapter, "For embedded development"
  - Quote: "You do not need to disable libstd when compiling to wasm!"
  - Paraphrase: Explicitly corrects the assumption that wasm compilation needs libstd disabled; that step is necessary only for embedded, not for browser/wasm targets

## Question `non-exhaustive-by-default`

Should public enums and structs heading toward 1.0 default to `#[non_exhaustive]`?

Positions:
- `non-exhaustive-by-default--non-exhaustive-by-default`: Yes
- `non-exhaustive-by-default--alt1`: Keep public types exhaustive

Claims:
- `a-sT08-f004169-c2` · Voice: ramfox · Source: https://iroh.computer/blog/iroh-0-96-0-the-quic-multipaths-to-1-0 (`f004169`) · Date: 2026-01-27 · Locator: § "TransportAddr rather than conn_type and ConnectionType"
  - Quote: "we need to make sure that iroh 1.0 can handle supporting different kinds of addresses"
  - Paraphrase: because custom transports (bluetooth, WebRTC) are a planned direction, iroh 1.0 must handle new address kinds, so `TransportAddr` is a non-exhaustive enum replacing `ConnectionType`
- `a-sR13-f004685-c3` · Voice: iroh/n0 (Friedel Ziegelmayer & Rüdiger Klaehn, post authors) · Source: https://iroh.computer/blog/iroh-1-0-0-rc-0 (`f004685`) · Date: 2026-05-11 · Locator: § "Non-exhaustive structs and enums"
  - Quote: "PathEvent and IncomingLocalAddr are both #[non_exhaustive], so the compiler requires you to handle the case of variants we may add later."
  - Paraphrase: restates and extends the 0.98 non_exhaustive Position — `PathEvent` and `IncomingLocalAddr` are marked non-exhaustive specifically to allow future variants without breaking the public API, requiring callers to add a wildcard match arm
- `a-sR13-f004586-c2` · Voice: iroh/n0 (dignifiedquire, post author) · Source: https://iroh.computer/blog/iroh-0-98-0-getting-back-to-traversing-nats (`f004586`) · Date: 2026-04-17 · Locator: § "Breaking Changes", multiple types marked `#[non_exhaustive]` (`iroh::DirectAddrType`, `iroh::address_lookup::mdns::DiscoveryEvent`)
  - Quote: none (structural, not prose declaration)
  - Paraphrase: newly public/changed types are marked non-exhaustive so future variants can be added without a breaking change

## Question `nonnull-in-ffi-params`

In FFI/wasm-bindgen-style APIs, should a safety-encoding wrapper type like `NonNull<T>` be accepted as a parameter even when it forces a runtime null check, or should the API stick to raw pointer types to avoid the check?

Positions:
- `nonnull-in-ffi-params--p1`: Avoid runtime null check
- `nonnull-in-ffi-params--alt1`: Accept `NonNull<T>` and pay the runtime check

Claims:
- `a-02-f000977-c1` · Voice: daxpedda · Source: https://github.com/wasm-bindgen/wasm-bindgen/pull/3852 (`f000977`) · Date: 2024-02-23 · Locator: PR body (top comment)
  - Quote: "I specifically didn't implement taking `NonNull<T>` as a parameter to avoid having to add a runtime check somewhere."
  - Paraphrase: deliberately did not implement taking `NonNull<T>` as a parameter in the new atomic-pointer API, specifically to avoid adding a runtime check

## Question `object-graph-representation`

How to represent a cyclic mutable object graph: `Rc<RefCell>`, raw pointers, or indices into an arena?

Positions:
- `object-graph-representation--indices-or-handles`: Indices into an arena, or a separate handle domain, for object graphs
- `object-graph-representation--alt1`: `Rc<RefCell<T>>` or `Arc<Mutex<T>>`
- `object-graph-representation--alt2`: raw or unsafe pointers

Claims:
- `b-sb26-f013214-c5` · Voice: CAD97 · Source: https://users.rust-lang.org/t/game-dev-in-rust-some-notes-on-the-mess/104939 (`f013214`) · Date: 2024-05-04 · Locator: reply timestamped 2024-05-04T23:38:57
  - Quote: "Games fundamentally are giant tangled graphs of mutable state with unclear and unstructured ownership, something Rust fundamentally isn't all that great at."
  - Paraphrase: attributes Rust's difficulty embedding scripting languages to a fundamental mismatch in how Rust and a guest language model mutability, ownership, generics, and callback-driven coupling; states games are "giant tangled graphs of mutable state with unclear and unstructured ownership," something Rust isn't well suited to represent directly, so the best approach he can picture pairs an ECS-ish API on the Rust side with an OO-ish API on the guest side, joined through handles — though he notes he has never actually built this out to prove it works
- `b-sb20-f007608-c1` · Voice: jacko.io · Source: https://jacko.io/object_soup.html (`f007608`) · Date: 2023-10-25 · Locator: section "Part Four: Indexes"
  - Quote: "This is how we write object soup in Rust."
  - Paraphrase: `Rc<RefCell<T>>` compiles for "object soup" but leaks memory on reference cycles and panics on self-referential mutable borrows (`already mutably borrowed: BorrowError`); raw/unsafe pointers hit the same aliasing problems and risk undefined behavior; keeping objects in a `Vec` and referring to each other by `usize` index avoids both, turns aliasing bugs into compiler errors, and serializes/parallelizes cleanly with `serde`/`rayon`

## Question `one-enum-vs-two-types`

Should a value that can be one of two related-but-distinct kinds be modeled as one enum with variant matching, or split into two separate types?

Positions:
- `one-enum-vs-two-types--p1`: Split into two structs
- `one-enum-vs-two-types--alt1`: Keep one enum with variant matching

Claims:
- `a-sa07-f003716-c3` · Voice: cBournhonesque · Source: https://github.com/bevyengine/bevy/pull/21601 (`f003716`) · Date: 2025-10-23 · Locator: PR #21601, comment 2025-10-23T14:14:41Z
  - Quote: "I think it might be better to split it into 2 separate structs?"
  - Paraphrase: found the enum-based accessor confusing when traversing relations dynamically and suggests splitting it into two separate structs plus friendlier wrapper methods

## Question `oop-patterns-in-rust`

Are classic OOP design patterns (e.g., Abstract Factory, as invoked via Clean/Hexagonal/Onion Architecture and DDD "ports and adapters") idiomatic to port into Rust, or does Rust favor different idioms (generics, enums) for the same structural goals?

Positions:
- `oop-patterns-in-rust--p1`: Factories are rarely idiomatic in rust
- `oop-patterns-in-rust--alt1`: Port OOP patterns such as factories directly

Claims:
- `a-sa30-f013276-c6` · Voice: jumpnbrownweasel — track record not established from this source · Source: https://users.rust-lang.org/t/abstract-factory-trait-with-generic-method/122066 (`f013276`) · Date: 2024-12-05 · Locator: post 2024-12-05T20:32:11.619Z
  - Quote: "I suggest trying to use generic types like Rc<E> above, if possible. Factories are rarely used in Rust."
  - Paraphrase: redirects the OP away from the Abstract Factory pattern toward generics, framing factories as a non-idiomatic import from other languages

## Question `opt-level-z-vs-s`

For size-optimized builds, can opt-level="z" be assumed smaller than "s", or must both be measured?

Positions:
- `opt-level-z-vs-s--p1`: Measure both(recommended)
- `opt-level-z-vs-s--p2`: Never assume opt-level="z" beats opt-level="s" for binary size — measure both

Claims:
- `b-bk02-f000256-c10` · Voice: rustwasm working group (Rust and WebAssembly book) [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: unknown (living doc) · Locator: § "Shrinking .wasm Code Size" → Tell LLVM to Optimize for Size Instead of Speed
  - Quote: "Note that, surprisingly enough, opt-level = \"s\" can sometimes result in smaller binaries than opt-level = \"z\". Always measure!"
  - Paraphrase: after presenting "z" as the more aggressive size flag, flags the counterintuitive case where "s" wins, as a reason no flag choice should be trusted unmeasured.
- `a-sB02-f000256-c7` · Voice: Rust and WebAssembly Working Group [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: 2018 · Locator: § "Shrinking .wasm Code Size" — "Tell LLVM to Optimize for Size Instead of Speed"
  - Quote: "Note that, surprisingly enough, opt-level = \"s\" can sometimes result in smaller binaries than opt-level = \"z\". Always measure!"
  - Paraphrase: opt-level="s" can sometimes produce smaller binaries than the more aggressive opt-level="z", so the choice should be measured rather than assumed.

## Question `optional-parameters-api-shape`

Without overloading or default arguments, one configurable entry point (options or Config struct, enum) or several specialized functions and constructors?

Positions:
- `optional-parameters-api-shape--one-configurable-entry`: One entry point: a `Config` struct, `_with_opts`, an enum discriminant, an option on the existing type
- `optional-parameters-api-shape--separate-specialized-entries`: Separate specialized functions or primitives
- `optional-parameters-api-shape--drop-feature-keep-signature-small`: Drop the feature to keep the signature small
- `optional-parameters-api-shape--many-constructors-criticized`: Many constructors (status quo, criticized)

Claims:
- `a-01-f000530-c2` · Voice: MrGVSV · Source: https://github.com/bevyengine/bevy/pull/10321 (`f000530`) · Date: 2023-10-30 · Locator: PR comment, mid-thread (identity inferred from a later reply addressed "@MrGVSV I like the idea with the enum...")
  - Quote: "I'm still wondering if it would make sense to introduce a `ColorSpace` enum and just specify that as a second parameter so we don't have to introduce a bunch of new methods for each color space."
  - Paraphrase: Suggests a `ColorSpace` enum passed as a second constructor argument instead of one method per color space, to avoid multiplying method names for every combination.
- `a-sa06-f003414-c5` · Voice: ConradIrwin · Source: https://github.com/zed-industries/zed/pull/36497 (`f003414`) · Date: 2025-09-12 · Locator: comment 2025-09-12T19:43:46Z
  - Quote: "I'd also be OK to merge a v1 of this work without the BOM detection"
  - Paraphrase: is willing to merge without automatic BOM/UTF-16 detection to keep the `load` call simple, i.e. picks fewer arguments over the extra feature
- `b-sb05-f001512-c3` · Voice: MabezDev · Source: https://github.com/esp-rs/esp-hal/pull/1592 (`f001512`) · Date: 2024-06-11 · Locator: comment 2024-06-11T10:22:55Z
  - Quote: "If this is part of the config now, then I don't think this should be public anymore, we should do everything through the config struct"
  - Paraphrase: once a setting is part of the config, it should not be public as a separate method — everything should go through the config struct
- `b-sb10-f003222-c2` · Voice: rklaehn · Source: https://iroh.computer/blog/iroh-blobs-0-90-changes (`f003222`) · Date: 2025-07-04 · Locator: "Options" section
  - Quote: "in other languages, you might solve this issue with either overloading or with default parameters. But rust has neither, for very good reasons. So we have come up with the following pattern."
  - Paraphrase: Rust has neither overloading nor default parameters, so each operation exposes an `_with_opts` method taking an Options struct (the closest mapping to the underlying RPC message), plus convenience wrapper methods using `impl Into<T>` for common cases
- `a-01-f000530-c1` · Voice: st0rmbtw · Source: https://github.com/bevyengine/bevy/pull/10321 (`f000530`) · Date: 2023-10-30 · Locator: PR body, Objective/Changelog section
  - Quote: "Added a new `Color::rgba_from_array([f32; 4]) -> Color` method."
  - Paraphrase: Proposes replacing the generic `Color::from(T)`/`T::from(Color)` conversions with one explicitly-named method per source type and per color space, so the target color space is always visible at the call site rather than inferred from context.
- `a-sa06-f003414-c4` · Voice: EuclidDivisionLemma · Source: https://github.com/zed-industries/zed/pull/36497 (`f003414`) · Date: 2025-09-13 · Locator: comment 2025-09-13T06:20:43Z
  - Quote: "having a single function will require us to pass four arguments in all those places, making the code significantly less readable"
  - Paraphrase: weighs three options (keep `load_with_encoding` separate; one `load` with UTF-16 auto-detection at the cost of 4 args; drop auto-detection for a 2-arg `load`) and flags readability cost of merging
- `b-sb05-f001512-c4` · Voice: jessebraham · Source: https://github.com/esp-rs/esp-hal/pull/1592 (`f001512`) · Date: 2024-05-30 · Locator: comment 2024-05-30T12:38:44Z
  - Quote: "there are way too many constructors and not enough documentation"
  - Paraphrase: the proliferation of constructors without documentation makes the API hard to understand

## Question `oss-framework-monetization`

Release Rust work fully open (with a paid layer alongside), or keep features or toolchains proprietary?

Positions:
- `oss-framework-monetization--fully-open`: Fully open, paid layer alongside or donate permissively
- `oss-framework-monetization--alt1`: Gate features behind a paywall, or keep the work proprietary

Claims:
- `b-sT05-f002775-c1` · Voice: Jonathan Pallant (Ferrous Systems) · Source: https://ferrous-systems.com/blog/rust-cortex-r52 (`f002775`) · Date: 2025-03-11 · Locator: press-release body, Pallant quote paragraph
  - Quote: "As long-time advocates of open-source development, we are proud to be able to donate this project to the community"
  - Paraphrase: libraries and examples (incl. cortex-r-rt, mirroring the Cortex-M set) donated to the Rust Project's Embedded Devices WG; headline frames "Under Open Source License" as the first
- `a-sa09-f004016-c1` · Voice: nathanielsimard · Source: https://burn.dev/blog/burn-end-of-the-year-review (`f004016`) · Date: 2025-12-19 · Locator: § "Announcing Burn Central"
  - Quote: "I've always envisioned a business model based on adding value through complementarity, rather than restricting features behind a paywall."
  - Paraphrase: frames Burn Central's business model as adding a paid cloud layer alongside a fully-capable free/local plan, explicitly contrasted with paywalling core features

## Question `oss-reuse-attribution-norms`

Is rehosting or reusing another project's code without coordination or credit acceptable?

Positions:
- `oss-reuse-attribution-norms--coordination-and-credit-matter`: Coordination and credit matter
- `oss-reuse-attribution-norms--no-entitlement`: No entitlement to control reuse

Claims:
- `a-sa05-f003025-c8` · Voice: jkelleyrtp · Source: https://github.com/bevyengine/bevy/issues/19296 (`f003025`) · Date: 2025-06-02 · Locator: comment @jkelleyrtp 2025-06-02T07:00:30Z
  - Quote: "Instead of reaching out with an offer to help modularize the subsecond engine, you went straight to copy-pasting our code into a new project, stripping it down, renaming it, and then started shopping around for help to maintain it."
  - Paraphrase: copying, stripping, and renaming another team's code, then seeking maintainers for it, without reaching out first, is disrespectful of the original authors' investment even though the license allows it
- `a-sa05-f003025-c6` · Voice: cart · Source: https://github.com/bevyengine/bevy/issues/19296 (`f003025`) · Date: 2025-06-01 · Locator: comment @cart 2025-06-01T22:35:03Z
  - Quote: "If someone were to publish a 'debranded' Bevy Reflect without discussing it with us, I would consider that bad form. Legal according to the license, but bad form nonetheless."
  - Paraphrase: taking a project's work wholesale and redistributing it without discussing it first is "bad form" even where the license permits it, because banners/brands carry the social and financial capital that sustains maintainers
- `a-sa05-f003025-c7` · Voice: hecrj · Source: https://github.com/bevyengine/bevy/issues/19296 (`f003025`) · Date: 2025-06-02 · Locator: comment @hecrj 2025-06-02T02:49:06Z
  - Quote: "I don't think 'producers' of open source should be entitled to anything; the same way 'consumers' aren't either. This is the real beauty of open source—a gift with no expectations."
  - Paraphrase: producers of open source are not entitled to control over branding or how their code is reused; forking and improving others' code is the essence of open source, not a breach of it
- `a-sa13-f004772-c7` · Voice: SomeoneToIgnore · Source: https://github.com/zed-industries/zed/pull/58618 (`f004772`) · Date: 2026-08-02 · Locator: comment @SomeoneToIgnore 2026-08-02T15:31:14Z
  - Quote: "How come a different PR has the very same function, almost verbatim, copy-pasted from [...] Including all the worst bugs of it... If you have really copied parts of the other PR, do add a co-authored-by metadata to this PR and include @interkelstar into that."
  - Paraphrase: points out a function copy-pasted almost verbatim, bugs included, from a different open PR (#62051), and asks that a co-authored-by credit be added if code was really copied from it
- `a-sa13-f004772-c8` · Voice: ysalitrynskyi · Source: https://github.com/zed-industries/zed/pull/58618 (`f004772`) · Date: 2026-08-02 · Locator: comment @ysalitrynskyi 2026-08-02T18:58:14Z
  - Quote: "Co-authored-by: Vlad Gevsky is now on the commits (including the base one), and the PR body credits both #62051 and #50719."
  - Paraphrase: concedes the point and adds attribution after the fact, crediting both prior PRs the navigation core derived from
