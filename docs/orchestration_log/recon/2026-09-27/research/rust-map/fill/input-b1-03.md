# Blind fill input, batch 1, file 03 of 13

For each Claim below, name the one Position of its Question that the Claim supports (a Position id from the list), or `none` if it supports none of them. The Claims are in random order.

## Question `cpp-binding-tool-choice`

For binding a large existing C++ API surface to Rust, should you use a low-level C-ABI-only generator (bindgen/cbindgen), a manually-declared bridge macro with boxed indirection (CXX), a hand-written interface-description-language with explicit layout control ("Zengar"), or native compiler integration across clang and rustc (Crubit)?

Positions:
- `cpp-binding-tool-choice--p1`: No single tool fits everyone
- `cpp-binding-tool-choice--alt1`: bindgen/cbindgen
- `cpp-binding-tool-choice--alt2`: CXX
- `cpp-binding-tool-choice--alt3`: a hand-written interface description
- `cpp-binding-tool-choice--alt4`: native compiler integration (Crubit)

Claims:
- `b-sb24-f011312-c1` · Voice: Taylor · Source: https://youtube.com/watch?v=Z5M4NIWoMJQ (`f011312`) · Date: 2025-10-03 · Locator: [05:14]-[10:18]
  - Quote: "within the realm of C++ interop, no two projects want exactly the same thing... So can there ever really be one interop solution to rule them all?"
  - Paraphrase: bindgen/cbindgen only handle C-ABI-compatible functions, forcing manual unsafe conversion for any RAII/generic/user-defined type; CXX adds safer higher-level types but requires manually redeclaring items and boxing everything since it can't see existing types' memory layout; "Zengar" lets users specify size/alignment to pass by value but requires a separate IDL file, which doesn't scale to huge API surfaces; Crubit gets maximum coverage via native clang+rustc integration but requires a clang toolchain, which not every project can use

## Question `cpp-bindings-default-unsafe`

When binding C++ APIs whose safety depends on undocumented preconditions, should every C++ function be marked `unsafe` in Rust by default, or should the binding rely on C++-side safety annotations plus type-based heuristics to mark functions safe where possible?

Positions:
- `cpp-bindings-default-unsafe--p1`: Reject blanket unsafe use annotations and heuristics
- `cpp-bindings-default-unsafe--alt1`: Mark every bound C++ function `unsafe` by default

Claims:
- `b-sb24-f011312-c2` · Voice: Taylor · Source: https://youtube.com/watch?v=Z5M4NIWoMJQ (`f011312`) · Date: 2025-10-03 · Locator: [12:21]-[14:24]
  - Quote: "When all your code says unsafe, it stops meaning anything."
  - Paraphrase: marking every C++ function `unsafe` in Rust makes the annotation meaningless (the fish shell project forked its own version of auto-cxx just to turn `unsafe` off entirely); Crubit instead combines optional C++-side safety annotations with type-based heuristics so callers only see `unsafe` on genuinely dangerous APIs

## Question `cpp-mutable-reference-representation`

For C++ mutable references crossing into Rust (which, unlike Rust's `&mut`, are not guaranteed exclusive and can alias), should the FFI binding represent them as raw unsafe pointers, `Cell`-based interior mutability, or a new native non-exclusive C++-style reference type added to Rust?

Positions:
- `cpp-mutable-reference-representation--p1`: None satisfying yet add native cpp reference type
- `cpp-mutable-reference-representation--alt1`: Raw unsafe pointers
- `cpp-mutable-reference-representation--alt2`: `Cell`-based interior mutability

Claims:
- `b-sb24-f011312-c3` · Voice: Taylor and Tyler · Source: https://youtube.com/watch?v=Z5M4NIWoMJQ (`f011312`) · Date: 2025-10-03 · Locator: [19:27]-[25:34]
  - Quote: "None of these approaches are perfect, but with some help from the Rust compiler, we can begin to offer safer and more ergonomic APIs."
  - Paraphrase: raw pointers force every reference-taking method (including all method calls, via `self`) to be unsafe; `Cell` assumes invariants C++ references don't provide (safe projection through `Option`/`Vec`, and `Sync`-safety for thread-safe C++ types); their proposed alternative is a new C++-style reference type in Rust where mutation-that-can-invalidate-a-reference is unsafe, but this needs new compiler features (generalized field projection, auto-referencing for custom reference types) that don't exist yet

## Question `crate-maintenance-signaling`

How should crates.io signal that a crate or version should not be used: a per-version deprecation, decaying maintenance status, or the existing yank and badges?

Positions:
- `crate-maintenance-signaling--new-deprecate-mechanism`: A dedicated per-version deprecation mechanism
- `crate-maintenance-signaling--existing-tools-suffice`: Existing tools suffice (maintenance badges, yank for serious cases)
- `crate-maintenance-signaling--status-auto-decays`: Maintenance status should decay automatically
- `crate-maintenance-signaling--status-opt-in-only`: Status opt-in only, no forced decay

Claims:
- `b-sb23-f009334-c3` · Voice: lewis · Source: https://internals.rust-lang.org/t/request-provide-an-official-way-to-deprecate-a-crate-not-yank-yank-is-stupid/24174 (`f009334`) · Date: 2026-04-21 · Locator: comment ~19
  - Quote: "Isn't this what the badges.maintenance field in Cargo.toml is for?"
  - Paraphrase: points to the existing `badges.maintenance.status` field, which lib.rs already renders, as already solving whole-crate deprecation
- `b-sb23-f009334-c1` · Voice: KSXGitHub · Source: https://internals.rust-lang.org/t/request-provide-an-official-way-to-deprecate-a-crate-not-yank-yank-is-stupid/24174 (`f009334`) · Date: 2026-04-15 · Locator: OP
  - Quote: "Yank breaks things. It is also way too alarmist."
  - Paraphrase: yank is too alarmist/breaking for this use; wants a `cargo deprecate <pkg>[@range] -m <reason>` that marks specific version ranges without forcing a break
- `b-sb23-f009334-c2` · Voice: kornel · Source: https://internals.rust-lang.org/t/request-provide-an-official-way-to-deprecate-a-crate-not-yank-yank-is-stupid/24174 (`f009334`) · Date: 2026-04-18 · Locator: comment ~14
  - Quote: "if they stumble upon an old crate, it's a 99% chance that it will be some outdated abandonware"
  - Paraphrase: from analyzing crates.io data, genuinely "done" evergreen crates are rare (roughly 10-1000 out of 100,000+ old crates); giving authors a way to affirmatively mark a crate fine helps users filter the 99% that are abandonware
- `b-sb23-f009334-c4` · Voice: KSXGitHub · Source: https://internals.rust-lang.org/t/request-provide-an-official-way-to-deprecate-a-crate-not-yank-yank-is-stupid/24174 (`f009334`) · Date: 2026-04-21 · Locator: comment ~20
  - Quote: "this badge deprecate[s] the whole crate ... we only want to deprecate some versions of a crate"
  - Paraphrase: the maintenance badge only deprecates a whole crate, not individual problematic versions, so it doesn't solve the stated problem
- `b-sb23-f009334-c7` · Voice: steffahn · Source: https://internals.rust-lang.org/t/request-provide-an-official-way-to-deprecate-a-crate-not-yank-yank-is-stupid/24174 (`f009334`) · Date: 2026-04-17 · Locator: comment ~10
  - Quote: "the crate author could opt in to setting such status information on their crates, but they shouldn't be forced"
  - Paraphrase: modeled on "last seen online" indicators — sharing status should be opt-in per crate, changeable later, and any reminder emails must be a separate, one-time opt-in per person, not automatic
- `b-sb23-f009334-c5` · Voice: Ltrlg · Source: https://internals.rust-lang.org/t/request-provide-an-official-way-to-deprecate-a-crate-not-yank-yank-is-stupid/24174 (`f009334`) · Date: 2026-04-22 · Locator: comment ~21
  - Quote: "In this case that version really should be yanked ... If the vulnerability can be qualified as 'serious' then yanking is not 'way too alarmist'"
  - Paraphrase: a version with a serious security vulnerability should be yanked outright, not merely soft-deprecated, since yanking is proportionate to serious risk
- `b-sb23-f009334-c6` · Voice: dlight · Source: https://internals.rust-lang.org/t/request-provide-an-official-way-to-deprecate-a-crate-not-yank-yank-is-stupid/24174 (`f009334`) · Date: 2026-04-17 · Locator: comment ~6
  - Quote: "The system does not work if the information isn't up to date."
  - Paraphrase: without decay, a crate could be marked maintained once and never revisited for years while still showing as maintained

## Question `crdt-vs-coordination`

For a multi-actor collaborative system (humans and agents editing together), should convergence come from CRDTs or from a coordinating mechanism (locking, operational transform, a single authoritative server)?

Positions:
- `crdt-vs-coordination--p1`: Convergence for a multi-actor, human-and-agent live document should come from CRDTs rather than a coordinating or locking mechanism
- `crdt-vs-coordination--alt1`: A coordinating mechanism (locking, operational transform, an authoritative server)

Claims:
- `b-sR11-f005071-c1` · Voice: Nathan Sobo (Zed founder) · Source: https://zed.dev/blog/agentic-xanadu (`f005071`) · Date: 2026-09-01 · Locator: "The dependency tree exists today" section
  - Quote: "Convergence without coordination."
  - Paraphrase: lists CRDTs, "formalized in 2011," as "the center of Zed's own work for the past decade," letting a Delta worktree be "edited by several people and agents on different continents at once" with no coordination step

## Question `current-thread-runtime-for-blocking`

Is it acceptable practice to run blocking synchronous I/O (e.g. database calls) inside a dedicated single-threaded ("current_thread") Tokio runtime on its own OS thread, or does limiting a Tokio runtime to a single thread carry negative internal ramifications that make this an anti-pattern except when no other OS threads are available?

Positions:
- `current-thread-runtime-for-blocking--p1`: Single threaded runtime fine for n1 scheduling
- `current-thread-runtime-for-blocking--alt1`: A single-threaded runtime is an anti-pattern unless no other threads are available

Claims:
- `b-sb18-f005307-c3` · Voice: withoutboats · Source: https://lobste.rs/s/7rtvnp (`f005307`) · Date: 2024-08-02 · Locator: lobste.rs/s/7rtvnp, comment 2024-08-02T08:03:38-05:00
  - Quote: "I believe that Jon Gjengset is wrong about this. If you want to N:1 scheduling of async tasks (instead of M:N), using the single threaded runtime is the right choice."
  - Paraphrase: responding to kbknapp's report that Jon Gjengset warned against using Tokio's single-threaded runtime except when no OS threads are available, states this warning is wrong: if you want N:1 scheduling of async tasks, the single-threaded runtime is the right tool, though combining it with blocking syscalls on that thread is unusual

## Question `custom-allocator-restart-persistence`

To persist Rust objects across process/container restarts, should a practitioner build a custom raw-memory `Allocator` (memfd + systemd FD store + mmap) rather than serializing state to an external store (file/Redis) on shutdown/startup?

Positions:
- `custom-allocator-restart-persistence--p1`: Custom allocator for restart persistence
- `custom-allocator-restart-persistence--alt1`: Serialize state to an external store (file, Redis) on shutdown

Claims:
- `b-sb19-f005836-c1` · Voice: Graham King · Source: https://darkcoding.net/software/rust-systemd-memory-remains (`f005836`) · Date: 2024-01-17 · Locator: § opening / "An allocator backed by persistent memory"
  - Quote: "We are going to stitch three things together to make Rust objects that survive program restart."
  - Paraphrase: combining systemd's FD store, `memfd_create`, and a custom Rust `Allocator` lets an object's backing memory survive a `systemctl restart`, as an alternative to his own prior practice of serializing state to Redis or a temp file on restart

## Question `custom-bytes-type-vs-vec-u8`

At an API boundary where allocation strategy matters (e.g. future backend-managed/pinned memory), should owned byte buffers be typed as `Vec<u8>` or a custom wrapper type?

Positions:
- `custom-bytes-type-vs-vec-u8--p1`: Custom bytes type over vec u8 at boundaries
- `custom-bytes-type-vs-vec-u8--alt1`: Use `Vec<u8>` at the boundary

Claims:
- `b-sR08-f003587-c3` · Voice: nathanielsimard · Source: https://github.com/tracel-ai/burn/pull/3792 (`f003587`) · Date: 2025-10-09 · Locator: PR #3792, review comment 2025-10-09T13:32:53Z
  - Quote: "We should replace all instances of `Vec<u8>` by `burn_common::Bytes`, `&[u8]` and `&mut [u8]` are OK"
  - Paraphrase: asks that owned buffer types at the store's API boundary use `burn_common::Bytes` rather than `Vec<u8>`, while leaving borrowed `&[u8]`/`&mut [u8]` as-is, so a future backend-managed allocation strategy (e.g. pinned GPU memory) can be substituted later.

## Question `custom-wasm-target-vs-wasi`

when the goal is running an existing, unmodified Rust/Linux program (with threads, filesystem, subprocesses) inside a sandbox, should you target the standardized WASI Rust targets (wasm32-wasip1/2/3), or define and require a custom, non-standard Rust target tailored to the sandbox's own syscall/threading model?

Positions:
- `custom-wasm-target-vs-wasi--p1`: Define a custom Rust compilation target (`wasm32-browserpod-linux-musl`) rather than port to a WASI target, for running unmodified existing Rust programs in-browser
- `custom-wasm-target-vs-wasi--alt1`: Port to the standard WASI targets

Claims:
- `b-sb22-f009062-c1` · Voice: Yuri Iozzelli · Source: https://labs.leaningtech.com/blog/browserpod-rust (`f009062`) · Date: 2026-08-13 · Locator: section "Why not just pick WASI?"
  - Quote: "BrowserPod already solves these problems, so we decided to skip the middleman and implement our own Rust target."
  - Paraphrase: porting `yarn` to WASI would mean touching every `std::os::unix` call site, removing thread usage entirely (wasip3's cooperative threading is new and unsupported by std or tokio), and accepting the loss of shelling out to `git`/`node`; since BrowserPod's own kernel already solves filesystem, networking, subprocesses and real per-thread parallelism, the team wrote a custom target instead of doing that porting work

## Question `debug-assert-vs-infallible`

In a library, should an internal invariant be enforced with `debug_assert!` (documents and tests the assumption, but only panics in debug builds), or should the code be rewritten to be infallible so the assumption can never be violated even conceptually?

Positions:
- `debug-assert-vs-infallible--p1`: Keep debug asserts
- `debug-assert-vs-infallible--p2`: Prefer infallible code

Claims:
- `b-sb04-f001392-c4` · Voice: joshka · Source: https://github.com/ratatui/ratatui/pull/1089 (`f001392`) · Date: 2024-05-11 · Locator: PR #1089, comment 2024-05-11T02:47:17Z
  - Quote: "I don't like debug_asserts at all, especially in a library."
  - Paraphrase: dislikes `debug_assert!` in a library because when the assumption is wrong, it surfaces as a hard-to-report panic in the library's users' users, fixable only by a coordinated release of both projects, so the code should instead be made infallible
- `b-sb04-f001392-c3` · Voice: EdJoPaTo · Source: https://github.com/ratatui/ratatui/pull/1089 (`f001392`) · Date: 2024-05-11 · Locator: PR #1089, comment 2024-05-11T09:13:41Z
  - Quote: "What I liked about it were the assumptions actually tested."
  - Paraphrase: values `debug_assert!` for documenting and actually testing an assumption in the code, and is only "fine" with it being replaced because the change came with enough tests to cover the same ground

## Question `dedicated-design-vs-duplicate-now`

When adding support for a new but closely related serialization format, should the implementation start as a decoupled, dedicated design or as pragmatic duplication of the existing similar format's code, refactored later?

Positions:
- `dedicated-design-vs-duplicate-now--p1`: Dedicated decoupled recorder from the start
- `dedicated-design-vs-duplicate-now--p2`: Duplicate now refactor later
- `dedicated-design-vs-duplicate-now--p3`: Reduce duplication before merge
- `dedicated-design-vs-duplicate-now--p4`: Keep separate for pragmatic reasons

Claims:
- `b-sb09-f002567-c4` · Voice: laggui · Source: https://github.com/tracel-ai/burn/pull/2721 (`f002567`) · Date: 2025-05-05 · Locator: comment @laggui 2025-05-05T14:00:50Z
  - Quote: "I am not in favor of introducing such a big amount of duplication just to eventually fix it (or even worse, remain unchanged for longer)..."
  - Paraphrase: objects to merging a large amount of test/example duplication with the intent to fix it later, given the PR's size.
- `b-sb09-f002567-c1` · Voice: antimora · Source: https://github.com/tracel-ai/burn/pull/2721 (`f002567`) · Date: 2025-01-27 · Locator: comment @antimora 2025-01-27T22:21:47Z
  - Quote: "I suggest creating a dedicated `SafeTensorFileRecorder` to handle SafeTensor files independently from PyTorch's `.pt` files."
  - Paraphrase: proposes a dedicated `SafeTensorFileRecorder` independent from the PyTorch recorder, with a configurable adapter (defaulting to PyTorchAdapter), to keep formats decoupled from the start.
- `b-sb09-f002567-c3` · Voice: laggui · Source: https://github.com/tracel-ai/burn/pull/2721 (`f002567`) · Date: 2025-05-01 · Locator: comment @laggui 2025-05-01T15:11:57Z
  - Quote: "I'm not sure if there is actual value in the current state to have two sections, where the biggest difference is the file recorder used."
  - Paraphrase: argues the new SafeTensors doc section is nearly identical to the PyTorch one and questions whether keeping them as two separate sections adds value.
- `b-sb09-f002567-c2` · Voice: wandbrandon · Source: https://github.com/tracel-ai/burn/pull/2721 (`f002567`) · Date: 2025-01-28 · Locator: comment @wandbrandon 2025-01-28T02:40:30Z
  - Quote: "It's a lot of new files that are essentially copied code but with little adjustments."
  - Paraphrase: copied the PyTorch recorder implementation wholesale into a new SafeTensors recorder as a base, planning cleanup later.
- `b-sb09-f002567-c5` · Voice: antimora · Source: https://github.com/tracel-ai/burn/pull/2721 (`f002567`) · Date: 2025-05-02 · Locator: comment @antimora 2025-05-02T18:44:04Z
  - Quote: "We discussed offline to keep two sections separate but have the same format and language between the two... For now it seems it's easier to have two."
  - Paraphrase: after an offline discussion, decided to keep PyTorch and SafeTensors doc sections separate (same format/language) rather than merge them now, calling it easier for the time being.

## Question `dedicated-methods-vs-manual-composition`

Should an API add a dedicated method for every composed operation (e.g. append/prepend a rotation) even when it gives no performance benefit over manual composition?

Positions:
- `dedicated-methods-vs-manual-composition--p1`: Omit methods with no perf benefit, compose manually
- `dedicated-methods-vs-manual-composition--alt1`: Add a dedicated method for every composed operation

Claims:
- `a-sB01-f000217-c5` · Voice: Dimforge (nalgebra maintainers) · Source: https://nalgebra.org/docs (`f000217`) · Date: capture 2025-01-21 (Wayback; underlying doc undated) · Locator: "Computer-graphics recipes" chapter, note after "Homogeneous raw transformation matrix modification" table
  - Quote: "That is because a specific method does not provide any performance benefit."
  - Paraphrase: Explains there is no append/prepend-rotation method because a dedicated method gives no performance benefit over building the rotation matrix and multiplying it in

## Question `dedicated-test-for-overlapping-case`

When a new macro feature's behavior largely overlaps existing generic tests, should reviewers ask for a dedicated test of the new case anyway, or is that redundant?

Positions:
- `dedicated-test-for-overlapping-case--p1`: A new prop-label feature should get its own dedicated test even where the new code path overlaps generic behavior
- `dedicated-test-for-overlapping-case--p2`: A dedicated test for behavior already covered by more general, feature-independent tests is unnecessary

Claims:
- `a-sR01-f000538-c2` · Voice: cecton · Source: https://github.com/yewstack/yew/pull/3509 (`f000538`) · Date: 2023-11-06 · Locator: PR #3509, comment 2023-11-06T14:58:24Z
  - Quote: "Maybe you can add a test to make sure this case also works?"
  - Paraphrase: asks the author to add a test covering `Option<AttrValue>` prop values specifically for the new dynamic-prop-label path.
- `a-sR01-f000538-c3` · Voice: kirillsemyonkin · Source: https://github.com/yewstack/yew/pull/3509 (`f000538`) · Date: 2023-11-06 · Locator: PR #3509, comment 2023-11-06T15:34:46Z
  - Quote: "Optional values for properties are supposed to be already tested by more general tests that are not inherent to dynamic props."
  - Paraphrase: questions the value of the requested test, arguing optional-value handling is already exercised by tests not specific to dynamic props.

## Question `dedupe-transitive-dependency-versions`

Should a Rust library actively chase down and eliminate duplicate transitive dependency versions (e.g., two copies of `rustls`) in its dependency tree?

Positions:
- `dedupe-transitive-dependency-versions--p1`: Actively reduce duplicated transitive dependencies by upgrading
- `dedupe-transitive-dependency-versions--alt1`: Accept duplicate transitive versions

Claims:
- `a-sR05-f001981-c2` · Voice: matheus23 (iroh maintainer, n0) · Source: https://iroh.computer/blog/iroh-0-24-0-quinn-11 (`f001981`) · Date: 2024-09-04 · Locator: "🤝 Transitive dependencies" section
  - Quote: "we were generally able to reduce duplicated dependencies"
  - Paraphrase: upgrading iroh's `quinn` dependency was valued because it let iroh drop duplicated copies of shared dependencies, shrinking its overall dependency footprint

## Question `default-features-minimal-vs-inclusive`

Should an optional capability (a format, codec or heap profiling) be on in a crate's default features, or opt-in?

Positions:
- `default-features-minimal-vs-inclusive--inclusive-defaults`: Enable by default for minimal friction
- `default-features-minimal-vs-inclusive--minimal-defaults`: Compile in only what is used
- `default-features-minimal-vs-inclusive--unresolved-reported`: Reported as an open debate, no side taken (heap profiling)

Claims:
- `b-sb25-f011435-c2` · Voice: Nico · Source: https://youtube.com/watch?v=J1KcRkV_fvk (`f011435`) · Date: 2026-06-11 · Locator: ~31:30-32:31 (audience Q&A on dependency counts)
  - Quote: "you should be able to only compile in what you're actually using"
  - Paraphrase: contrasts Servo's ~1,000 dependencies (dominated by SpiderMonkey, WebGL, XR) with Blitz's ~300, achieved by enabling only 4 of 20 available image codecs by default and making SVG/networking support opt-in per deployment
- `a-sa26-f011684-c1` · Voice: Lei Huang · Source: https://greptime.com/blogs/2024-01-18-memory-leak (`f011684`) · Date: 2024-01-31 · Locator: section "Enabling Heap Profiling in GreptimeDB"
  - Quote: "The discussion about whether the mem-prof feature should be enabled by default is ongoing in greptimedb#3166. You are welcome to share your opinion there"
  - Paraphrase: GreptimeDB currently ships with heap profiling (mem-prof) off by default, compiled in only via a cargo feature flag; whether it should be on by default is an active, unresolved discussion the author points readers to rather than settles
- `a-sa02-f002127-c1` · Voice: clarfonthey · Source: https://github.com/bevyengine/bevy/pull/15586 (`f002127`) · Date: 2024-10-02 · Locator: PR comment
  - Quote: "Kinda just would prefer the path of least friction and we can change the defaults later."
  - Paraphrase: weighing reviewer pushback that niche formats (QOI, GIF) shouldn't be defaults, the author leans toward shipping with minimal friction now and adjusting defaults later rather than pre-curating by popularity

## Question `defensive-guards-for-unlikely-failures`

how much defensive engineering (RAII/type-level guards) is warranted against a failure mode judged unlikely to occur in practice

Positions:
- `defensive-guards-for-unlikely-failures--p1`: Guard even theoretical leaks
- `defensive-guards-for-unlikely-failures--alt1`: Leave unlikely failure modes unguarded

Claims:
- `a-sR14-f007341-c1` · Voice: Moss · Source: https://forgestream.idverse.com/blog/20260313-rust-export (`f007341`) · Date: 2026-02-09 · Locator: "Polish" section
  - Quote: "this is a problem in theory and may not ever occur in practice, but I figured it would be best to guard for this using some good old-fashioned RAII."
  - Paraphrase: worth adding an RAII (`Drop`-based) guard for a resource-leak path he judges may never actually occur, over leaving it unhandled — appeals to Value: correctness over minimal/pragmatic effort.

## Question `defer-multithreaded-encoding`

When a resource (a Metal command buffer/lock) needs coordinated access from multiple threads, should the implementation wait on the lock (with a timeout) now, or defer multithreaded encoding until single-threaded use has proven the design?

Positions:
- `defer-multithreaded-encoding--p1`: Defer multithreading decision
- `defer-multithreaded-encoding--alt1`: Implement multithreaded lock handling now

Claims:
- `b-sb03-f000569-c1` · Voice: Narsil · Source: https://github.com/huggingface/candle/pull/1318 (`f000569`) · Date: 2023-12-15 · Locator: PR #1318, comment 2023-12-15T11:24:19Z
  - Quote: "I think I'm ok delaying this decision when the current implem for single threaded as proven it's worth"
  - Paraphrase: in multithreaded encoding we'd need to decide whether to wait on the lock with a timeout (since deadlocks could happen); okay with delaying that decision until the single-threaded implementation has proven its worth, since multithreaded command encoding doesn't yet show much benefit

## Question `depend-vs-hand-roll`

Should a project take a dependency (a crate, bindings tree, safe-wrapper crate like rustix, or vendor SDK), or hand-roll or vendor its own code to keep the dependency footprint small?

Positions:
- `depend-vs-hand-roll--take-the-dependency`: Take the existing, tested crate (persistent data structures, an intrusive-list crate, `rustix` over raw libc)
- `depend-vs-hand-roll--hand-roll-or-vendor`: Keep a hand-rolled or vendored implementation, or a lean internal wrapper over a weak vendor SDK
- `depend-vs-hand-roll--minimize-footprint`: Minimize the dependency footprint even at the cost of uglier code or release cycles; audit burden too high

Claims:
- `a-saL2-f011092-c3` · Voice: Luca Casonato · Source: https://youtube.com/watch?v=YcujtU0LA9Y (`f011092`) · Date: 2024-02-13 · Locator: ~00:26:21-00:28:24
  - Quote: "there's one thing that kind of sucks right now in [Rust] though which is the story around third party integrations and like third party SDKs... our experience with this is that you end up building a lot of little mini SDKs"
  - Paraphrase: describes the Rust vendor-SDK ecosystem as a weak point — AWS's SDK exists but doesn't retry S3 uploads correctly, GCP has no official Rust SDK (its in-progress one went dormant), Azure's is not yet ready, Stripe has no first-party SDK — so the team builds and maintains its own small internal "mini SDKs" (types plus retry handling) for cloud storage, IAM, secrets, Let's Encrypt, npm registry access, and GitHub
- `a-sR06-f002016-c1` · Voice: abrown · Source: https://github.com/bytecodealliance/wasmtime/pull/9234 (`f002016`) · Date: 2024-09-20 · Locator: PR #9234, comment 2024-09-20T00:30:47Z
  - Quote: "The `cargo vet` situation is a bit much:"
  - Paraphrase: posts the full `cargo vet` diff/inspect list generated by the new dependency tree (`tch`, `torch-sys`, `ndarray`, `zip`, `cipher`, etc., some entries thousands of lines) and characterizes the situation as excessive.
- `a-sa04-f002865-c2` · Voice: Dirbaio · Source: https://github.com/embassy-rs/embassy/pull/4035 (`f002865`) · Date: 2025-04-01 · Locator: PR comment ("Some concerns")
  - Quote: "I don't think we should add `cordyceps` as a dep, I'd prefer to keep the data structures self-contained for something as foundational as the executor. Having it all in-tree means we can make changes as needed without having to coordinate across repos, and less abstraction means it's clearer what's going on in this case IMO."
  - Paraphrase: objects to adding `cordyceps` as a dependency for something as foundational as the executor, preferring the data structures stay self-contained and in-tree so the project can change them without cross-repo coordination, keeping the abstraction surface minimal
- `a-sa14-f005079-c4` · Voice: alexcrichton · Source: https://github.com/bytecodealliance/wasmtime/pull/14294 (`f005079`) · Date: 2026-09-09 · Locator: comments 2026-09-09T04:26:50Z; 2026-09-09T04:27:52Z; 2026-09-09T04:28:26Z; 2026-09-09T04:29:20Z
  - Quote: "Could this use `rustix::io::fcntl_setfd` with error handling?"
  - Paraphrase: repeatedly suggests replacing raw/manual syscall handling (fcntl, fstat, getsockname, socket options) with the corresponding `rustix` safe-wrapper functions
- `a-sa04-f002865-c1` · Voice: jamesmunns · Source: https://github.com/embassy-rs/embassy/pull/4035 (`f002865`) · Date: 2025-04-01 · Locator: PR comment ("I'd like to try and make the case for keeping the cordyceps dependency!")
  - Quote: "Cordyceps is fairly exhaustively tested, with both miri and loom, which helps to avoid regressions potentially caused by changes."
  - Paraphrase: argues embassy-executor should keep the `cordyceps` dependency rather than hand-roll/vendor the data structures, citing its miri+loom test coverage, shared usage and maintenance with the `maitake` executor, and tested user APIs that reduce unsafe surface area
- `a-sa14-f005079-c3` · Voice: alexcrichton · Source: https://github.com/bytecodealliance/wasmtime/pull/14294 (`f005079`) · Date: 2026-09-08 · Locator: comment 2026-09-08T14:23:10Z
  - Quote: "The implementation in this crate looks pretty thin -- would it be possible to vendor the implementation here?"
  - Paraphrase: asks whether the thin crate implementing the systemd listen-fd protocol could just be vendored directly, since the protocol is set externally and unlikely to change much
- `a-02-f001053-c1` · Voice: Bojan Serafimov · Source: https://neon.com/blog/persistent-structures-in-neons-wal-indexing (`f001053`) · Date: 2024-03-01 · Locator: "Rust Persistent Data Structures (RPDS) to the rescue" / "Conclusion" sections
  - Quote: "There are more popular persistent data structure libraries in Rust, but this one deserves a lot more credit for its clean API, correct results (!!!), and more than good enough performance."
  - Paraphrase: rather than hand-roll a balanced 2D segment tree with lazy propagation, the team reached for the `rpds` crate to build a copy-on-write layer map, crediting it over more popular alternatives
- `b-sR03-f001160-c1` · Voice: daxpedda (wasm-bindgen maintainer) · Source: https://github.com/wasm-bindgen/wasm-bindgen/pull/3898 (`f001160`) · Date: 2024-04-03 · Locator: wasm-bindgen/wasm-bindgen#3898, comment 2024-04-03T06:30:56Z. · L2338-L2341.
  - Quote: "This is pretty ugly indeed, but I think it's very important for a library like `wasm-bindgen` to reduce its dependency footprint."
  - Paraphrase: accept the uglier code; minimizing dependencies matters more.
- `b-sR05-f002453-c1` · Voice: dignifiedquire (n0-computer/iroh maintainer) · Source: https://iroh.computer/blog/iroh-0-30-0-slimming-down (`f002453`) · Date: 2024-12-17 · Locator: iroh.computer/blog/iroh-0-30-0-slimming-down, 2024-12-17. · L2007-L2097.
  - Quote: "Less is more, simpler is better. This release we focused on cleaning up iroh APIs, streamlining the protocol APIs, and reducing our dependency load!" And: "Irohs dependency load is not the smallest, so while preparing the API for 1.0, we are also trying to reduce the number of required dependencies."
  - Paraphrase: actively spend release cycles cutting dependencies ahead of a 1.0 API, even though it means a wave of breaking changes.

## Question `dependency-upgrade-regression-handling`

When a transitive dependency upgrade trades one bug for another, should you pin to the older broken version, ship with the new regression, or hold the release?

Positions:
- `dependency-upgrade-regression-handling--p1`: Never ship a known crash prefer soft guardrails
- `dependency-upgrade-regression-handling--alt1`: Ship with the new regression
- `dependency-upgrade-regression-handling--alt2`: pin the older version
- `dependency-upgrade-regression-handling--alt3`: hold the release for an upstream fix

Claims:
- `b-sR04-f001749-c2` · Voice: emilk · Source: https://github.com/emilk/egui/pull/4849 (`f001749`) · Date: 2024-07-23 · Locator: PR #4849, comment 2024-07-23T13:27:16Z
  - Quote: "Having eframe always crash on exit on Mac is not an option imho."
  - Paraphrase: rejects shipping a version that always crashes on exit on macOS as a tradeoff; between that, shipping with a narrower crash on one feature path (with a guardrail steering users away from it), and blocking the release on an upstream fix, treats the always-crash option as off the table.

## Question `dependency-version-requirement-width`

How wide should a library's dependency version requirements be (e.g. serde `^1` vs a recent minimum)?

Positions:
- `dependency-version-requirement-width--p1`: Loosen serde requirement to `^1`
- `dependency-version-requirement-width--alt1`: Require a recent minimum version

Claims:
- `b-sT05-f003044-c2` · Voice: pickfire · Source: https://github.com/DioxusLabs/dioxus/issues/4195 (`f003044`) · Date: 2025-05-27 · Locator: comment 2025-05-27T17:05:52Z
  - Quote: "Can subsecond have serde being `^1` so that it can be more portable"
  - Paraphrase: subsecond's serde requirement blocked adding an axum hello-world example; asks for `^1` for portability with older serde

## Question `deprecate-gradually-vs-break`

When retiring a legacy compatibility path, should maintainers break it immediately or deprecate it gradually with warnings?

Positions:
- `deprecate-gradually-vs-break--p1`: A deprecated compatibility shim (WAGI) should be phased out with warnings and migration time, not removed outright
- `deprecate-gradually-vs-break--alt1`: Break the legacy path immediately

Claims:
- `b-sR11-f005050-c2` · Voice: The Spin Project · Source: https://spinframework.dev/blog/announcing-spin-4-1 (`f005050`) · Date: 2026-08-26 · Locator: "A heads-up on WAGI" section
  - Quote: "this is the start of a gradual, managed deprecation, not a break"
  - Paraphrase: 4.1 starts printing deprecation warnings and drops WAGI examples from the repo, but existing WAGI components keep running

## Question `deref-delegation-vs-accessors`

Should a Rust API expose one type's methods through another via `Deref` (delegation by deref), or through explicit accessor methods?

Positions:
- `deref-delegation-vs-accessors--p1`: Drop Deref delegation for explicit accessors
- `deref-delegation-vs-accessors--alt1`: Delegate through `Deref`

Claims:
- `b-sT04-f001890-c1` · Voice: n0, inc. / iroh team (post by ramfox) · Source: https://iroh.computer/blog/iroh-0-23-welcoming-nodejs-to-the-family (`f001890`) · Date: 2024-08-21 · Locator: § "Letting net stand on its own"; § Breaking Changes > API Changes > iroh, first bullet
  - Quote: "No more deref of iroh::net::Client to iroh::client::node::Node"
  - Paraphrase: The release pulls the networking methods out of the node methods, so users now call `node.net().node_addr()` instead of `node.node().node_addr()`. It lists "No more deref of iroh::net::Client to iroh::client::node::Node" as a breaking change, replacing the earlier deref-based grouping. The stated reason is to let net "stand on its own". The Voice's Rust connection is shown in the source: the post is written by the maintainers of the Rust crates iroh, iroh-net and iroh-blobs and includes Rust code.

## Question `derive-arithmetic-ops`

Should std provide `#[derive]` for arithmetic operator traits with field-wise semantics?

Positions:
- `derive-arithmetic-ops--support-fieldwise-derive`: Add it, like Clone/Debug
- `derive-arithmetic-ops--oppose-semantics-ambiguous`: Reject: field-wise arithmetic is wrong or rarely useful
- `derive-arithmetic-ops--prefer-delegation-mechanism`: Reject in favor of a delegation mechanism
- `derive-arithmetic-ops--ecosystem-crates-suffice`: Leave it to ecosystem crates

Claims:
- `b-sb22-f009292-c2` · Voice: 2e71828 · Source: https://internals.rust-lang.org/t/pre-rfc-derive-support-for-arithmetic-traits-add-sub-mul-div-on-structs/23482 (`f009292`) · Date: 2025-09-02 · Locator: reply timestamped 2025-09-02T17:47:25
  - Quote: "My main concern is whether unconstrained field-wise projection of these operators is really all that common."
  - Paraphrase: challenges the OP's own `TcpPort` example directly, asking why anyone would add two `TcpPort`s together, to argue the class of cases where naive field-wise addition is actually correct is narrower than the RFC assumes
- `a-sa19-f009292-c2` · Voice: 2e71828 · Source: https://internals.rust-lang.org/t/pre-rfc-derive-support-for-arithmetic-traits-add-sub-mul-div-on-structs/23482 (`f009292`) · Date: 2025-09-02 · Locator: reply, 2025-09-02T17:47:25.304Z
  - Quote: "My main concern is whether unconstrained field-wise projection of these operators is really all that common."
  - Paraphrase: Doubts unconstrained field-wise derive is broadly useful, since most wrapper structs that need arithmetic (complex numbers, quaternions, matrices) have their own non-field-wise rules.
- `a-sa19-f009292-c4` · Voice: Vorpal · Source: https://internals.rust-lang.org/t/pre-rfc-derive-support-for-arithmetic-traits-add-sub-mul-div-on-structs/23482 (`f009292`) · Date: 2025-09-05 · Locator: reply, 2025-09-05T08:06:03.300Z
  - Quote: "It is not obvious what the derives for arithmetic operators should do. There isn't a single right answer."
  - Paraphrase: Even for simple newtypes there is no single correct semantics (e.g. whether Radians/Degrees arithmetic should wrap modulo 2π/360), unlike Clone or Debug where the standard derive is almost always right.
- `a-sa19-f009292-c1` · Voice: vangata-ve · Source: https://internals.rust-lang.org/t/pre-rfc-derive-support-for-arithmetic-traits-add-sub-mul-div-on-structs/23482 (`f009292`) · Date: 2025-09-02 · Locator: OP, 2025-09-02T17:06:42.006Z
  - Quote: "This is pointless busywork when the only sensible behavior is to perform the operation field by field."
  - Paraphrase: Manually implementing Add/Sub/Mul/Div for structs where field-wise operation is the obviously sensible behaviour is needless busywork; std should support deriving them the way it does Clone/Debug/Copy.
- `a-sa19-f009292-c6` · Voice: porky11 · Source: https://internals.rust-lang.org/t/pre-rfc-derive-support-for-arithmetic-traits-add-sub-mul-div-on-structs/23482 (`f009292`) · Date: 2026-01-16 · Locator: reply, 2026-01-16T20:01:40.626Z
  - Quote: "No need to have it in the core fo the language. That's kind of the point of the Rust package manager, that the core language includes the important things while most things are outsourced to libraries."
  - Paraphrase: derive_more already covers this well; the core language/std should stay minimal and leave most conveniences to libraries, which is the point of having a package manager.
- `a-sa19-f009292-c3` · Voice: jdahlstrom · Source: https://internals.rust-lang.org/t/pre-rfc-derive-support-for-arithmetic-traits-add-sub-mul-div-on-structs/23482 (`f009292`) · Date: 2025-09-02 · Locator: reply, 2025-09-02T19:56:12.974Z
  - Quote: "Addition and scalar multiplication make sense for vectors, but for points they are meaningless in general."
  - Paraphrase: Invokes affine-space math (points vs. vectors/translations) to argue field-wise addition is often meaningless, e.g. adding two geographic coordinates, so a naive derive would default to semantically wrong behaviour.
- `b-sb22-f009292-c3` · Voice: jdahlstrom · Source: https://internals.rust-lang.org/t/pre-rfc-derive-support-for-arithmetic-traits-add-sub-mul-div-on-structs/23482 (`f009292`) · Date: 2025-09-02 · Locator: reply timestamped 2025-09-02T19:56:12
  - Quote: "it makes no sense to add together the coordinates of two cities, but the difference of two coordinates is entirely meaningful."
  - Paraphrase: distinguishes vector spaces (where addition and scalar multiplication are meaningful) from affine spaces of points and translations — `Instant`/`Duration`, Celsius/Fahrenheit, geographic coordinates, pointers/`ptrdiff_t` — where adding two points is meaningless and only point+translation or point−point make sense
- `b-sb22-f009292-c1` · Voice: vangata-ve · Source: https://internals.rust-lang.org/t/pre-rfc-derive-support-for-arithmetic-traits-add-sub-mul-div-on-structs/23482 (`f009292`) · Date: 2025-09-02 · Locator: opening post, section "Rationale"
  - Quote: "This is pointless busywork when the only sensible behavior is to perform the operation field by field."
  - Paraphrase: hand-writing (or pulling in `derive_more` for) trivial field-wise arithmetic on numeric structs is unnecessary busywork std could eliminate the way it already does for `Clone`; the derive would require `T: Add` on generic fields and intentionally excludes enums, where manual impls are judged clearer
- `a-sa19-f009292-c5` · Voice: kornel · Source: https://internals.rust-lang.org/t/pre-rfc-derive-support-for-arithmetic-traits-add-sub-mul-div-on-structs/23482 (`f009292`) · Date: 2025-09-02 · Locator: reply, 2025-09-02T20:24:36.828Z
  - Quote: "This may be better solved by delegation syntax or generalised macros for constructing derives."
  - Paraphrase: A basic field-wise arithmetic derive can only encode one relationship between fields (e.g. a Point), so it doesn't generalize to matrices, quaternions or complex numbers; a delegation syntax or generalized derive-construction macro would serve better.
- `b-sb22-f009292-c4` · Voice: DragonDev1906 · Source: https://internals.rust-lang.org/t/pre-rfc-derive-support-for-arithmetic-traits-add-sub-mul-div-on-structs/23482 (`f009292`) · Date: 2025-09-04 · Locator: reply timestamped 2025-09-04T07:06:14
  - Quote: "the existence of them in derive_more shows that they are useful and the most sane default implementation is fieldwise operation."
  - Paraphrase: draws a direct analogy to deriving `Debug` on a struct holding a large `Vec<u8>` — not always the ideal implementation, but still a sane default you skip when it doesn't fit; points to `derive_more`'s existing arithmetic derives as evidence of real demand

## Question `desktop-webview-ipc-vs-single-context`

For a Rust desktop app that needs a web-capable UI, should the frontend logic stay in the same Rust execution context as the backend (Dioxus-style, calling straight into the WebView glue), or should it run as an independent frontend runtime talking to a host process over a serialized IPC boundary (Tauri's architecture)?

Positions:
- `desktop-webview-ipc-vs-single-context--p1`: Reject split brain untyped ipc
- `desktop-webview-ipc-vs-single-context--alt1`: An independent frontend runtime over a serialized IPC boundary (Tauri)

Claims:
- `b-sb21-f008390-c1` · Voice: boringcactus (Melody) · Source: https://boringcactus.com/2025/04/13/2025-survey-of-rust-gui-libraries.html (`f008390`) · Date: 2025-04-16 · Locator: § "Tauri"
  - Quote: "Half the point of Rust is the sheer quantity of bugs that it can catch at compile time, and if your IPC is just tossing strings around and praying at runtime, you may as well be just writing vanilla JavaScript."
  - Paraphrase: Tauri's host-process/WebView split forces an IPC boundary where frontend calls take an untyped `&str` command name and `JsValue` args, so a field rename on the host side fails only at runtime instead of compile time; combined with the architectural split this made the author "genuinely hate" the design

## Question `divergent-signature-for-forever-tasks`

Should a long-running/background task use a divergent (`-> !`) function signature rather than one that returns?

Positions:
- `divergent-signature-for-forever-tasks--p1`: Prefer divergent signature for run forever tasks
- `divergent-signature-for-forever-tasks--alt1`: An ordinary returning signature

Claims:
- `a-sB04-f000227-c3` · Voice: RTIC developers · Source: https://rtic.rs/ (`f000227`) · Date: undated (living doc, v2.x) · Locator: "2.3. Software tasks & spawn", "Divergent tasks"
  - Quote: "The key advantage of divergent tasks is that they receive a 'static context, and local resources have 'static lifetime."
  - Paraphrase: Recommends the `-> !` (divergent) task signature for tasks meant to run forever, because it grants a 'static context/local-resource lifetime and makes the run-forever intent explicit versus a normal returning signature

## Question `docs-as-rust-vs-markdown`

When migrating a documentation/blog site's content out of a JS-based static-site generator's Markdown-derivative format, should the content be authored directly as Rust source (a DSL enabling compile-time link validation and cross-version deduplication) or kept close to Markdown for editor tooling and authoring ergonomics, with a lighter embedding mechanism for interactive components?

Positions:
- `docs-as-rust-vs-markdown--p1`: Docs as rust source for compile time checks and dedup
- `docs-as-rust-vs-markdown--p2`: Keep markdown for authoring ergonomics
- `docs-as-rust-vs-markdown--p3`: Downgrade to plain markdown plus custom component delimiters

Claims:
- `b-sb14-f004399-c1` · Voice: Madoshakalaka · Source: https://github.com/yewstack/yew/pull/4069 (`f004399`) · Date: 2026-03-11 · Locator: PR description @Madoshakalaka 2026-03-11T10:47:39Z
  - Quote: "We have compile-time validated doc links that go through the spa router... Data-as-code allows us to deduplicate greatly."
  - Paraphrase: rewrote the docs site's content as Rust source instead of MDX, citing compile-time-validated internal/external doc links and data-as-code deduplication across doc versions as the payoff.
- `b-sb14-f004399-c4` · Voice: Madoshakalaka · Source: https://github.com/yewstack/yew/pull/4069 (`f004399`) · Date: 2026-04-11 · Locator: comment @Madoshakalaka 2026-04-11T08:52:48Z
  - Quote: "I think we should downgrade all our mdx to plain markdown files. And invent our own way to embed Yew components instead."
  - Paraphrase: after researching mdx-capable crates, decides to drop mdx/Rust-source authoring in favor of plain Markdown with a custom comment-delimiter convention for embedding Yew components.
- `b-sb14-f004399-c3` · Voice: Madoshakalaka · Source: https://github.com/yewstack/yew/pull/4069 (`f004399`) · Date: 2026-04-09 · Locator: comment @Madoshakalaka 2026-04-09T14:21:28Z
  - Quote: "I can get behind this sentiment. Valid concerns. I'll do some research on mdx parsers and see if we can achieve the same thing with minimal edits to the mdx files."
  - Paraphrase: concedes WorldSEnder's concern is valid and agrees to research whether Markdown-based authoring can be preserved.
- `b-sb14-f004399-c2` · Voice: WorldSEnder · Source: https://github.com/yewstack/yew/pull/4069 (`f004399`) · Date: 2026-04-09 · Locator: comment @WorldSEnder 2026-04-09T14:02:40Z
  - Quote: "I would not want to write a blog post in this format, I would want to write the markdown where this came from... my editor understands markdown more or less, it does not understand this."
  - Paraphrase: objects to fully replacing MDX docs with Rust source, arguing the magic macros are a barrier to writing content and that ordinary editor/language tooling understands Markdown but not this Rust DSL.
