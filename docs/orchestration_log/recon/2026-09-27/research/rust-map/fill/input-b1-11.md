# Blind fill input, batch 1, file 11 of 13

For each Claim below, name the one Position of its Question that the Claim supports (a Position id from the list), or `none` if it supports none of them. The Claims are in random order.

## Question `rust-vs-c-inherent-performance`

Does safe Rust cost performance against C/C++, or can it match or beat it?

Positions:
- `rust-vs-c-inherent-performance--no-inherent-advantage`: No inherent advantage; social factors dominate
- `rust-vs-c-inherent-performance--types-enable-optimizations`: Rust's type system enables optimizations C lacks
- `rust-vs-c-inherent-performance--real-overheads`: Rust has real overheads: initialization, forced refactors and copies
- `rust-vs-c-inherent-performance--init-cost-narrow`: Initialization cost is a narrow edge case
- `rust-vs-c-inherent-performance--composability-wins`: Composability lets engineers ship better data structures
- `rust-vs-c-inherent-performance--safe-rust-matches`: Safe Rust matches C for demanding work (embedded display, 3D)
- `rust-vs-c-inherent-performance--safety-cost-acceptable`: A real safety cost is an acceptable trade
- `rust-vs-c-inherent-performance--p1`: Rust idioms default to faster collections

Claims:
- `a-saL1-f005516-c9` · Voice: dataangel · Source: https://lobste.rs/s/in8yn9 (`f005516`) · Date: 2025-06-12 · Locator: reply, 2025-06-12T07:56:20-05:00 and 2025-06-13T20:10:53-05:00
  - Quote: "safe Rust requires you to provide a value at construction time, which is not based on dataflow analysis. For example if you make a very large array, you must spend the time to zero init the entire thing even if you always write to elements before reading them."
  - Paraphrase: Argues safe Rust requires a value at construction time (not just before use via dataflow analysis, as for ordinary variables), so a large array or a small-object allocator must eagerly zero-initialize memory it may never read before writing, and the cost compounds with more allocations, sometimes bloating codegen enough to block inlining and further optimization.
- `b-sb26-f013214-c4` · Voice: parasyte · Source: https://users.rust-lang.org/t/game-dev-in-rust-some-notes-on-the-mess/104939 (`f013214`) · Date: 2024-01-10 · Locator: reply timestamped 2024-01-10T18:33:17
  - Quote: "Personally, I would prefer a 10% perf hit (40 FPS) for a memory safe implementation that doesn't crash."
  - Paraphrase: cites a session where Ark: Survival Ascended crashed three times and topped out near 45 FPS despite an unsafe/unmanaged-heavy implementation, to argue relaxed memory safety isn't a performance free lunch; states a personal preference for "a 10% perf hit (40 FPS) for a memory safe implementation that doesn't crash," and separately reports deliberately abandoning an early Bevy game project after three months as a "fail fast" call once its immaturity became clear, later moving to Godot
- `a-saL1-f005516-c2` · Voice: rtpg · Source: https://lobste.rs/s/in8yn9 (`f005516`) · Date: 2025-06-09 · Locator: reply, 2025-06-09T20:16:56-05:00
  - Quote: "a language with 'more' semantic granularity will have more leeway to give you free optimizations... if your codebase is filled with iteration rather than array access, you just don't need your bounds checks!"
  - Paraphrase: Argues a language with more semantic granularity gives the compiler more true invariants to exploit, e.g. Rust code built on iteration rather than raw array access can eliminate bounds checks entirely; cautions that "like for like" benchmarking between languages is inherently ambiguous.
- `a-saL1-f005516-c5` · Voice: kornel · Source: https://lobste.rs/s/in8yn9 (`f005516`) · Date: 2025-06-10 · Locator: reply, 2025-06-10T08:19:54-05:00
  - Quote: "C doesn't have easily accessible hashmaps, so implementations tend to default to linear searches, until it becomes a problem... That means the discussion is just about which language makes it easier to write fast programs."
  - Paraphrase: Frames the practical gap as partly ecosystem-driven: C's lack of an easily-reached-for hashmap pushes real-world C code toward slow linear searches until forced to fix (citing a GitLab backup-time postmortem), while Rust's easy hashmaps and parallel iterators make fast-by-default code more common in practice.
- `a-saL1-f005516-c3` · Voice: steveklabnik · Source: https://lobste.rs/s/in8yn9 (`f005516`) · Date: 2025-06-10 · Locator: reply, 2025-06-10T14:15:50-05:00
  - Quote: "Rust puts the equivalent of `restrict` on every reference that doesn't contain an `UnsafeCell`, so it is doing a bit more than you assume here, and that is in the type system."
  - Paraphrase: States Rust puts the equivalent of C's `restrict` on every reference that doesn't contain an `UnsafeCell`, meaning the no-aliasing guarantee is encoded in the type system, not just a vague folk claim, and that Rust is also ahead on pointer provenance semantics.
- `a-saL1-f005516-c12` · Voice: dataangel · Source: https://lobste.rs/s/in8yn9 (`f005516`) · Date: 2025-06-10 · Locator: reply, 2025-06-10T11:09:00-05:00
  - Quote: "trivial new features can require large refactorings because they necessitate new borrowing schemes."
  - Paraphrase: Disputes that Rust is generally "faster" in this practical-design-choice sense, saying trivial new features can require large refactorings because they necessitate new borrowing schemes, and separately notes extra clones/`Rc` are commonly added just to satisfy the borrow checker where they aren't algorithmically necessary.
- `a-saL1-f005516-c4` · Voice: dataangel · Source: https://lobste.rs/s/in8yn9 (`f005516`) · Date: 2025-06-10 · Locator: reply, 2025-06-10T07:16:21-05:00
  - Quote: "if you spend a little time looking at Rust disassembly on nontrivial examples it becomes very obvious... There's a reason the Rust solutions don't win on highload.fun"
  - Paraphrase: Counters that real Rust disassembly shows concrete recurring costs: bounds checks on every array/division/shift access, "unsafe"-gated SIMD intrinsics, poorly-optimizing iterators (citing open rustc codegen issues), `RefCell` overhead, un-collapsible layers of `Result<>` wrapping, and clones/`Rc` added defensively to satisfy the borrow checker — concluding this is why Rust solutions don't top competitive-programming performance leaderboards.
- `a-sa15-f005516-c1` · Voice: Bryan Cantrill · Source: https://lobste.rs/s/in8yn9 (`f005516`) · Date: undated in this source (an anonymous commenter quotes a Cantrill talk via youtu.be/HgtRAbE1nBM?t=2450 with no air date given here; two Cantrill blog posts are also named — bcantrill.dtrace.org/2018/09/18/falling-in-love-with-rust/ and .../2018/09/28/the-relative-performance-of-c-and-rust/ — whose URL-embedded dates, 2018-09-18 and 2018-09-28, are not independently confirmed since those posts were not fetched) · Locator: blockquote citing "Bryan Cantrill @ https://youtu.be/HgtRAbE1nBM?t=2450"
  - Quote: "the reason I could use a B-Tree and not an AVL tree, is because of that composability of Rust... I would still use an AVL tree in C even though I know I'm giving up some small amount of performance, but in Rust, I get to use a B-Tree."
  - Paraphrase: argues Rust's composability lets him reach for a B-Tree where in C he'd stick to an AVL tree, because an intrusive C B-Tree implementation is too risky to trust ("up in everything's underwear")
- `a-saL1-f005516-c13` · Voice: david_chisnall · Source: https://lobste.rs/s/in8yn9 (`f005516`) · Date: 2025-06-11 · Locator: reply, 2025-06-11T02:18:49-05:00
  - Quote: "It is *trivial* to write code that is abstract over data structures... In C, implementation details of the data structure tend to leak unless you're *really* careful."
  - Paraphrase: Argues the biggest practical performance advantage of C++ or Rust over C is that it's trivial to write code abstract over data structures, so a wrong choice found in profiling can be swapped easily; in C, implementation details leak through unless wrapped in painful macros — describes replacing his own hand-rolled generic concurrent hash table (many macros) with an off-the-shelf container plus a lock, which was both more maintainable and faster.
- `b-sb26-f013214-c3` · Voice: John_Nagle · Source: https://users.rust-lang.org/t/game-dev-in-rust-some-notes-on-the-mess/104939 (`f013214`) · Date: 2024-01-13 · Locator: reply timestamped 2024-01-13T20:31:31
  - Quote: "In safe Rust (I don't use \"unsafe\" in my own code at all) it's not bad."
  - Paraphrase: states his metaverse client's several coordinated CPU-bound threads (refresh, per-frame update, event processing, asset-decoding) doing entirely different work would be "really hard" to coordinate safely in C++, but works acceptably in safe Rust with no `unsafe` used anywhere in his own code
- `a-saL1-f005516-c10` · Voice: rpjohnst · Source: https://lobste.rs/s/in8yn9 (`f005516`) · Date: 2025-06-11 · Locator: reply, 2025-06-11T11:16:03-05:00 and 2025-06-12T10:09:38-05:00
  - Quote: "Rust merely requires init *before use* based on dataflow analysis. Surely the C code you're comparing with doesn't read from uninitialized variables to a noticeable degree?"
  - Paraphrase: Repeatedly presses that Rust has no implicit default initialization and only requires init-before-use by dataflow analysis, so the described cost should only bite in narrow cases like large arrays or read buffers, not "all variables" broadly, and questions whether the allocator scenario generalizes.
- `a-saL1-f005516-c1` · Voice: ajdecon · Source: https://lobste.rs/s/in8yn9 (`f005516`) · Date: 2025-06-09 · Locator: reply, 2025-06-09T14:34:18-05:00
  - Quote: "there's no inherent reason for either language to be faster. It's all project specific... it's often just because they're much older codebases and have been optimized over a long time."
  - Paraphrase: Agrees there's no inherent reason either language is faster; to the extent C codebases are faster today it's mostly because they're older and have had more engineer-hours of optimization, not a property of C itself.
- `a-saL1-f005516-c11` · Voice: ssokolow · Source: https://lobste.rs/s/in8yn9 (`f005516`) · Date: 2025-06-10 · Locator: reply, 2025-06-10T09:04:39-05:00 and 2025-06-10T11:32:55-05:00
  - Quote: "I would still use an AVL tree in C even though I know I'm giving up some small amount of performance, but in Rust, I get to use a B-Tree." (quoting Bryan Cantrill)
  - Paraphrase: Argues Rust wins in the sense of what design choices engineers are actually willing to ship (versus benchmark racing); quotes Bryan Cantrill's account of choosing a safe, composable B-Tree in Rust where he'd have defaulted to a less-optimal AVL tree in C, because a hand-rolled intrusive B-Tree in C carries too much memory-corruption risk to trust.

## Question `rust-vs-gc-for-multitenant-runtime`

Should a secure multi-tenant runtime that executes untrusted user code (e.g. a serverless JavaScript isolate hypervisor) be built in a language like Rust rather than a garbage-collected language like Go?

Positions:
- `rust-vs-gc-for-multitenant-runtime--p1`: Rust for reliability and explicit performance
- `rust-vs-gc-for-multitenant-runtime--alt1`: A garbage-collected language such as Go

Claims:
- `a-sa22-f011092-c1` · Voice: Luca Casonato · Source: https://youtube.com/watch?v=YcujtU0LA9Y (`f011092`) · Date: 2024-02-13 · Locator: transcript ~00:01:46-00:10:30 (talk, timestamps approximate from auto-captions)
  - Quote: "[Go] does not have the same reliability or strictness or customizability or performance that languages like rust or even C++ for that matter do"
  - Paraphrase: Describes Deno's own history of first trying Go for its multi-tenant sandboxed runtime, and rejecting it because it lacked the reliability, strictness, customizability and performance needed to safely execute untrusted code for many tenants; chose Rust (with some C++ for the embedded V8 engine) instead, citing exhaustive Result/Option-based error handling, transparent/explicit allocation cost (no hidden allocations without an explicit `.clone()`), no conflict between a host garbage collector and V8's own GC in the same process, and easy C++ interop needed to embed V8 safely via `rusty_v8`-style bindings.

## Question `rust-worth-it-for-failure-heavy-infra`

Rust for failure-heavy network infrastructure?

Positions:
- `rust-worth-it-for-failure-heavy-infra--rust-for-failure-heavy-infra`: Yes for failure-heavy, high-throughput infrastructure: ownership and pattern matching tame edge cases
- `rust-worth-it-for-failure-heavy-infra--alt1`: A simpler implementation language (e.g. Python)

Claims:
- `b-sb19-f005948-c1` · Voice: Eric Zhang · Source: https://modal.com/blog/serverless-http (`f005948`) · Date: 2024-03-20 · Locator: § "Edge cases and errors" / opening
  - Quote: "Rust's pattern matching and ownership help with managing the casework."
  - Paraphrase: HTTP has many edge cases and Modal's ingress needs to handle malformed/out-of-order events from possibly-malicious clients; Rust's ownership and pattern matching were chosen specifically to manage that casework, and switching from a prior Python-based ingress to this Rust one cut 502 errors by 99.7%
- `a-sa15-f005948-c1` · Voice: Eric Zhang · Source: https://modal.com/blog/serverless-http (`f005948`) · Date: 2024-03-14 · Locator: "Edge cases and errors" section
  - Quote: "This was tricky! HTTP has quite a few edge cases, so we used Rust for its speed and to help manage the complexity." / "Rust's pattern matching and ownership help with managing the casework."
  - Paraphrase: reports building `modal-http` (HTTP/WebSocket-to-function-call translation service) in Rust on hyper/tokio specifically for speed and to help manage the many concurrent failure cases (client disconnects, malformed/out-of-order events, spot preemption); credits the language's pattern matching and ownership for handling that casework, and separately reports that replacing an earlier Python-based ingress with this Rust service cut 502 errors by 99.7%

## Question `safe-wrapper-soundness-scope`

When a type wraps an unsafe operation and is labeled "safe," must that safety guarantee hold under every generic instantiation/composition, or is a narrower guarantee acceptable if the common case is sound?

Positions:
- `safe-wrapper-soundness-scope--p1`: Overpromising is unsound
- `safe-wrapper-soundness-scope--p2`: Pragmatic judgment call acceptable

Claims:
- `b-sR10-f004804-c1` · Voice: Dominaezzz (esp-hal reviewer) · Source: https://github.com/esp-rs/esp-hal/pull/5744 (`f004804`) · Date: 2026-06-15 · Locator: PR review comment, 2026-06-15T21:09:39Z
  - Quote: "\"safely useable\" is too vague and I feel it over promises a bit... Example of over promising, `Box<InternalMemory<[DmaDescriptor; 10]>, ExternalMemory>` is not safe to use."
  - Paraphrase: calling the new reference type "safely useable" overpromises, since a composition such as boxing it with external-memory backing is not actually safe to use
- `b-sR10-f004804-c2` · Voice: bugadani (esp-hal maintainer, PR author) · Source: https://github.com/esp-rs/esp-hal/pull/5744 (`f004804`) · Date: 2026-06-17 · Locator: PR review comment, 2026-06-17T07:36:32Z
  - Quote: "Wishy-washy, but a cache writeback is generally a safe operation as far as I can tell, and we don't call invalidate on these I think. So I think we're fine with the DmaDescriptor alignment in this type, at this time."
  - Paraphrase: without a full proof, a cache writeback is judged safe enough in practice for this type's current alignment guarantees, given invalidate isn't called on these paths

## Question `same-state-transition-trigger`

For a component that triggers on a state-machine transition matching a predicate, should a transition into the same state the entity is already in be treated as a no-op (never triggering), or should it be allowed to trigger, to support "reload" style use cases?

Positions:
- `same-state-transition-trigger--p1`: Raises same state transition question
- `same-state-transition-trigger--p2`: Suppress same state transitions
- `same-state-transition-trigger--p3`: Allow naive no suppression

Claims:
- `b-sb14-f004398-c6` · Voice: Freyja-moth · Source: https://github.com/bevyengine/bevy/pull/23315 (`f004398`) · Date: 2026-03-12 · Locator: comment @Freyja-moth 2026-03-12T16:51:05Z
  - Quote: "I don't think it really makes sense to react to changing to a state you're already in."
  - Paraphrase: argues it doesn't make sense to react to a transition into a state the entity is already in.
- `b-sb14-f004398-c5` · Voice: chescock · Source: https://github.com/bevyengine/bevy/pull/23315 (`f004398`) · Date: 2026-03-12 · Locator: comment @chescock 2026-03-12T14:28:50Z
  - Quote: "this check prevents despawning on same-state transitions. Do we really want to prevent that?"
  - Paraphrase: questions whether transitions into the same state the entity is already in should be excluded from triggering the predicate, noting it's unclear which behavior is wanted without more use-case knowledge.
- `b-sb14-f004398-c7` · Voice: alice-i-cecile · Source: https://github.com/bevyengine/bevy/pull/23315 (`f004398`) · Date: 2026-03-12 · Locator: comment @alice-i-cecile 2026-03-12T19:46:57Z
  - Quote: "Some folks have actually pushed for allowing same-state transitions precisely for a \"reload\" pattern. IMO we should use the naive behavior here."
  - Paraphrase: overrides Freyja-moth's suppression, noting some users specifically want same-state transitions to trigger for a "reload" pattern, and the naive (non-special-cased) behavior should be used.

## Question `scoped-impls-nameable`

Should scoped trait implementations be nameable, or must they stay anonymous?

Positions:
- `scoped-impls-nameable--p1`: Anonymous impls required for coherence
- `scoped-impls-nameable--p2`: Named impls for clarity

Claims:
- `a-sa19-f009123-c1` · Voice: Tamschi · Source: https://internals.rust-lang.org/t/pre-rfc-scoped-impl-trait-for-type/19923 (`f009123`) · Date: 2023-12-05 · Locator: reply to scottmcm/Nadrieril, 2023-12-05T20:39:46.548Z
  - Quote: "Regarding proper-naming implementations: I'm very strongly opposed to it, since I think it is squarely detrimental here, mainly in terms of clarity but also syntactically and for ease of use."
  - Paraphrase: Opposes naming scoped implementations; anonymity keeps coherence checking simple within one scope, lets the module double as an error-message name, and avoids new breaking-change rules that naming would introduce when an implementation is later broadened.
- `a-sa19-f009123-c3` · Voice: Nadrieril · Source: https://internals.rust-lang.org/t/pre-rfc-scoped-impl-trait-for-type/19923 (`f009123`) · Date: 2023-12-05 · Locator: reply, 2023-12-05T13:43:01.887Z
  - Quote: "I would suggest that you provide an explicit mechanism to specify a type along with explicitly chosen impls."
  - Paraphrase: Suggests an explicit naming mechanism so the implicit scoped-impl behavior desugars from something writable, making the proposal easier to explain even if users rarely write the explicit form.
- `a-sa19-f009123-c2` · Voice: scottmcm · Source: https://internals.rust-lang.org/t/pre-rfc-scoped-impl-trait-for-type/19923 (`f009123`) · Date: 2023-11-29 · Locator: reply, 2023-11-29T03:31:09.374Z
  - Quote: "I feel like they wanted names, and with names you even define two impls ... I think it would be nice to give normal paths to named things in those errors."
  - Paraphrase: Wants names for non-global impls so two implementations of the same trait/type can coexist in one module, and so compiler error messages can use a normal path instead of "the impl from this module".

## Question `scratch-buffer-vs-per-call-alloc`

In a hot loop, should working memory be a caller-owned scratch buffer reused across calls, or freshly allocated per call for simplicity?

Positions:
- `scratch-buffer-vs-per-call-alloc--p1`: Caller owned scratch buffer
- `scratch-buffer-vs-per-call-alloc--alt1`: Allocate fresh working memory per call

Claims:
- `b-sR12-f005120-c2` · Voice: Arthur Zucker / Hugging Face tokenizers team · Source: https://huggingface.co/blog/tokenizers-v1 (`f005120`) · Date: 2026-09-21 · Locator: section "The Merge Loop"
  - Quote: "v1 reuses a scratch buffer owned by the caller, removing those repeated allocations... the merge working set lives in a caller-owned scratch buffer; the loop never touches the allocator."
  - Paraphrase: the previous implementation allocated fresh memory and a new priority queue per pre-token; v1 instead reuses a scratch buffer owned by the caller so the merge loop never touches the allocator

## Question `scratch-register-type-enforced`

For a scratch register crossing a function boundary, enforce safe use by types and explicit parameters, or encapsulate it by convention?

Positions:
- `scratch-register-type-enforced--encode-in-types`: Encode it in types
- `scratch-register-type-enforced--p1`: Minimize the live range and avoid passing scratch registers around as parameters, even if it means redefining signatures and accepting some duplication across ISA-specific paths

Claims:
- `a-sa05-f002466-c1` · Voice: saulecabrera · Source: https://github.com/bytecodealliance/wasmtime/pull/9889 (`f002466`) · Date: 2025-01-04 · Locator: comment @saulecabrera 2025-01-04T16:38:14Z
  - Quote: "relying on the type system to identify/audit scratch register usage and/or providing exclusive access to the scratch registers"
  - Paraphrase: proposes relying on the type system to identify/audit scratch-register usage, or exclusive access analogous to allocatable registers, because passing a scratch register as a parameter extends its live range and raises unintentional-clobbering risk
- `b-sR05-f002466-c1` · Voice: saulecabrera (Bytecode Alliance, Wasmtime Winch baseline-compiler maintainer) · Source: https://github.com/bytecodealliance/wasmtime/pull/9889 (`f002466`) · Date: 2025-01-04 · Locator: bytecodealliance/wasmtime#9889, comment 2025-01-04T16:38:14Z. · L2288-L2319.
  - Quote: "the unintentional clobbering risk is particularly important in the case of scratch registers in Winch: even though they can be used for any purpose, one important detail about them is that they are not tracked by Winch's regalloc therefore they must be used sparingly and with extreme caution... Ideally, the live range of the scratch registers should be as short as possible to avoid potential bugs."
  - Paraphrase: minimize the live range and avoid passing scratch registers around as parameters, even if it means redefining signatures and accepting some duplication across ISA-specific paths.

## Question `semver-break-signaling-in-ci`

How should a Rust crate signal and enforce semver-breaking changes in CI and release tooling?

Positions:
- `semver-break-signaling-in-ci--p1`: Title marker plus commit marker gates ci
- `semver-break-signaling-in-ci--other`: Other / none of these

Claims:
- `b-bk03-f000267-c7` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Contributing § Pull Requests, "Declare breaking changes"
  - Quote: "The PR gate reads the title: that is what skips semver-checks and requires a breaking change fragment."
  - Paraphrase: a change that breaks a published crate's public API must be marked with `!` in both the PR title and the branch commit introducing the break, because the CI gate reads the PR title to skip semver-checks and require a breaking-change fragment, while release-plz separately reads the commits landing on main — which include the branch commits — to decide the major-version bump

## Question `serde-centralization`

Should Rust's derive/serialization ecosystem centralize around one blessed crate (serde) that other crates interoperate through, given orphan rules make independent multi-crate composition hard?

Positions:
- `serde-centralization--p1`: Orphan rules force derive centralization
- `serde-centralization--p2`: Ship type data instead of more derives

Claims:
- `a-sa25-f011413-c3` · Voice: Amos (fasterthanlime) · Source: https://youtube.com/watch?v=11m5HRMvPmU (`f011413`) · Date: 2026-06-11 · Locator: ~00:04:00–00:05:00
  - Quote: "the idea of many crates building upon a singular derive is, in my opinion, sound. We just have to kind of adjust our strategy... we might consider shipping data about our types"
  - Paraphrase: rather than generating a new derive for every new trait/behavior, crates should ship structural data about their types once, and build behaviors generically over that data
- `a-sa25-f011413-c2` · Voice: Amos (fasterthanlime) · Source: https://youtube.com/watch?v=11m5HRMvPmU (`f011413`) · Date: 2026-06-11 · Locator: ~00:03:06–00:04:00
  - Quote: "rust orphan rules have created an ecosystem composition problem"
  - Paraphrase: Rust's orphan rules mean crates that want to interoperate with a popular derive macro (serde) must piggyback on it rather than add independent support, functionally cornering the ecosystem around one crate

## Question `serialization-format-choice`

Which serialization format for a given constraint: postcard, JSON, CBOR, MessagePack, TOML, YAML or bincode?

Positions:
- `serialization-format-choice--established-binary-format`: An established binary format (postcard), with variant order as a stability contract
- `serialization-format-choice--cbor-for-no-std`: CBOR over MessagePack for no-std
- `serialization-format-choice--toml-for-consistency`: TOML for ecosystem consistency
- `serialization-format-choice--yaml-for-convenience`: YAML for convenience, patching the library
- `serialization-format-choice--no-custom-format`: A custom config language is too costly
- `serialization-format-choice--ship-now-switch-later`: Ship now, switch format later
- `serialization-format-choice--p1`: Avoid bincode for new persisted data

Claims:
- `b-sb09-f003030-c4` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/3504 (`f003030`) · Date: 2025-06-04 · Locator: comment @bugadani 2025-06-04T15:39:12Z
  - Quote: "I'd probably give https://crates.io/crates/facet-yaml a try"
  - Paraphrase: suggests trying the facet-yaml crate as a better-maintained alternative.
- `b-sb09-f003030-c6` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/3504 (`f003030`) · Date: 2025-06-05 · Locator: comment @bugadani 2025-06-05T11:43:25Z
  - Quote: "I get that the spec doesn't _mandate_ support for wider integers but it also doesn't forbid them, so why this sudden negativity?"
  - Paraphrase: pushes back that the YAML spec doesn't forbid wider integers, questioning bjoernQ's pessimism about the format.
- `b-sb09-f003030-c3` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/3504 (`f003030`) · Date: 2025-06-04 · Locator: comment @bugadani 2025-06-04T15:24:04Z
  - Quote: "I'd still prefer adding i128 support to whatever yaml library we pick - which probably shouldn't be serde_yml as it looks quite unmaintained."
  - Paraphrase: would rather add i128 support to whichever YAML library is chosen than change the config's type range, and flags serde_yml as likely unmaintained.
- `a-sa03-f002300-c1` · Voice: ealmloff · Source: https://github.com/DioxusLabs/dioxus/pull/3195 (`f002300`) · Date: 2024-11-11 · Locator: PR comment, responding to review
  - Quote: "I don't love having a bespoke serialization format. postcard is a much simpler well defined serialization format that might be easier to target than json. I think it is pretty similar to what we are currently generating"
  - Paraphrase: Responds to a suggestion that the serialized bytes be valid JSON by noting this would need much more const-time logic to format strings/numbers with uncertain compile-time cost, and states a preference for targeting postcard, an existing well-defined serialization format, over keeping a bespoke one.
- `b-bk03-f000267-c9` · Voice: Zcash Foundation / Zebra project · Source: https://zebra.zfnd.org/ (`f000267`) · Date: unknown (living document) · Locator: Zebra Cached State Database Implementation § Data Formats
  - Quote: "bincode is a risky format to use, because it depends on the exact order and type of struct fields. Do not use it for new column families."
  - Paraphrase: legacy column families use bincode via serde for note commitment trees, but this is called out as a risky choice for anything new because it depends on the exact order and type of struct fields, unlike the project's custom IntoDisk/FromDisk implementations used elsewhere
- `b-sb09-f003030-c2` · Voice: bjoernQ · Source: https://github.com/esp-rs/esp-hal/pull/3504 (`f003030`) · Date: 2025-05-24 · Locator: comment @bjoernQ 2025-05-24T17:33:48Z
  - Quote: "the toml representation is ... Quite inconvenient - IMHO yaml is the nicest representation here"
  - Paraphrase: finds TOML's representation inconvenient for this use case and considers YAML the nicest representation available.
- `b-sb09-f003030-c1` · Voice: okhsunrog · Source: https://github.com/esp-rs/esp-hal/pull/3504 (`f003030`) · Date: 2025-05-24 · Locator: comment @okhsunrog 2025-05-24T17:23:55Z
  - Quote: "Why not toml, to be consistent with the Rust ecosystem?"
  - Paraphrase: questions why the PR uses YAML instead of TOML, for consistency with the Rust ecosystem.
- `a-sa06-f003590-c2` · Voice: Rüdiger Klaehn · Source: https://iroh.computer/blog/lets-write-a-dht-1 (`f003590`) · Date: 2025-09-26 · Locator: § RPC protocol
  - Quote: "Postcard is a non-self-describing format, so we need to make sure to keep the order of the enum cases if we want the protocol to be long-term stable"
  - Paraphrase: states postcard is non-self-describing, so enum case order must be preserved for the protocol to remain stable long-term; this is presented as a requirement to design around, not a reason to avoid postcard
- `b-sb09-f003030-c7` · Voice: MabezDev · Source: https://github.com/esp-rs/esp-hal/pull/3504 (`f003030`) · Date: 2025-06-10 · Locator: comment @MabezDev 2025-06-10T09:48:30Z
  - Quote: "this is strictly \"internal\" right now, so we can proceed with yaml + some work arounds, then if a better library, or a more appropriate format shows up we can switch to it."
  - Paraphrase: since the format is currently internal-only, proposes proceeding with YAML plus workarounds now and switching library or format later if something better appears.
- `b-sb09-f003030-c5` · Voice: bjoernQ · Source: https://github.com/esp-rs/esp-hal/pull/3504 (`f003030`) · Date: 2025-06-05 · Locator: comment @bjoernQ 2025-06-05T11:30:38Z
  - Quote: "So YAML doesn't seem to be a good way forward... Maybe defining our own config-language would be an alternative - but probalby too much effort to \"just try it\""
  - Paraphrase: after evaluating serde_yml, serde_yaml and facet-yaml, concludes YAML tooling in the Rust ecosystem is a dead end for i128 support, floats designing a custom config language, but judges it too much effort to "just try it".
- `b-sR08-f003587-c1` · Voice: antimora · Source: https://github.com/tracel-ai/burn/pull/3792 (`f003587`) · Date: 2025-10-10 · Locator: PR #3792, comment 2025-10-10T14:21:49Z
  - Quote: "I switched from MessagePack to CBOR for metadata serialization due to rmp-serde's limitations"
  - Paraphrase: switched the new format's metadata serialization from MessagePack (`rmp-serde`) to CBOR (`ciborium`) because `rmp-serde` isn't no-std compatible and its upstream project has been inactive for over a year, while CBOR is an IETF-standardized, Serde-recommended, no-std-capable format that also preserves enum variant information.

## Question `service-fault-isolation-degrade`

Should a unit failure in a long-running service stop it, or be contained and degraded?

Positions:
- `service-fault-isolation-degrade--contain-and-continue`: Contain, log, keep serving
- `service-fault-isolation-degrade--alt1`: Let the failure propagate and stop the process or loop

Claims:
- `a-sR05-f001981-c1` · Voice: matheus23 (iroh maintainer, n0) · Source: https://iroh.computer/blog/iroh-0-24-0-quinn-11 (`f001981`) · Date: 2024-09-04 · Locator: "API Changes" section
  - Quote: "don't treat errors there as fatal"
  - Paraphrase: `Incoming::accept` can fail for benign network reasons; such failures should be logged and passed over, not treated as fatal
- `a-sa14-f004985-c3` · Voice: Celso Martinho, Ruskin Constant, Rui Figueira, and Luís Duarte · Source: https://blog.cloudflare.com/kitesurf (`f004985`) · Date: 2026-08-06 · Locator: § Design decisions / Exception handling
  - Quote: "any failure degrades to a blank frame or a missing element, never a dead session"
  - Paraphrase: commit as a design rule, before writing code, that any failure degrades to a blank frame or missing element rather than crashing the session, since the browser must render hostile, unreliable pages without ever dropping the one it's holding

## Question `share-via-combinator-vs-separate-impls`

When two operations are logically distinct (a local op returning a `Tensor` vs. a collective op returning a `{PeerId: Tensor}` map) but share underlying logic, should the crate share code via a combinator abstraction or keep them separately implemented?

Positions:
- `share-via-combinator-vs-separate-impls--p1`: Extract a shared combinator even if unexposed
- `share-via-combinator-vs-separate-impls--alt1`: Keep the operations separately implemented

Claims:
- `a-sR11-f003983-c2` · Voice: crutcher · Source: https://github.com/tracel-ai/burn/pull/4157 (`f003983`) · Date: 2025-12-12 · Locator: comment 2025-12-12T20:24:57Z
  - Quote: "we probably want a local op-combinator library to avoid that duplication, even if those ops aren't shared to users"
  - Paraphrase: `reduce_sum` (local) and `all_reduce_sum` (collective) are different operations, but the duplication between them is real and worth solving with an internal op-combinator library, even if that library never reaches end users

## Question `shared-hw-resource-refcount-vs-raii`

For a shared hardware resource with an enable/disable lifecycle (a radio PHY clock shared across peripherals), should safety rest on a reference-counted controller object, or on RAII-style exclusive ownership tied to the peripheral singletons themselves?

Positions:
- `shared-hw-resource-refcount-vs-raii--p1`: Reference counted controller
- `shared-hw-resource-refcount-vs-raii--p2`: Raii exclusive ownership

Claims:
- `a-sa05-f003169-c1` · Voice: Frostie314159 · Source: https://github.com/esp-rs/esp-hal/pull/3687 (`f003169`) · Date: 2025-06-24 · Locator: comment @Frostie314159 2025-06-24T13:26:21Z / 2025-06-24T15:18:21Z
  - Quote: "unless we count the reference for each modem clock controller individually, just repeatedly calling the function to disable the PHY clock on one modem clock controller, would eventually disable the PHY clock, even if different modems still rely on it."
  - Paraphrase: proposes a `RadioClockController` that counts references per modem so disabling one modem's use of the shared PHY clock doesn't disable it out from under another modem still relying on it
- `a-sa05-f003169-c3` · Voice: Frostie314159 · Source: https://github.com/esp-rs/esp-hal/pull/3687 (`f003169`) · Date: 2025-07-01 · Locator: comment @Frostie314159 2025-07-01T15:05:34Z
  - Quote: "I've removed it with the latest commit."
  - Paraphrase: having converged with the reviewer, removes the separate `RadioClockController` and reduces the design to a single shared PHY ref-count guarded by the peripheral-singleton pattern
- `a-sa05-f003169-c2` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/3687 (`f003169`) · Date: 2025-06-25 · Locator: comment @bugadani 2025-06-25T13:18:42Z / 2025-06-25T13:29:48Z
  - Quote: "I'd just implement all relevant code for the radio singletons, then only radio users could meddle with any of this."
  - Paraphrase: questions why a separate `RadioClockController` and manual ref-count are needed at all if only the peripheral singletons (already unique/exclusive by construction) can touch the clock; proposes implementing the clock-control logic directly on the radio peripheral structs instead

## Question `shared-model-crate-vs-domain-split`

When a Bevy codebase grows past tens of thousands of lines and single-crate compile times become disruptive, should shared types be pulled into one low-level crate that everything depends on (simple, but the worst-case recompile unit), or should the codebase instead be split along domain lines to avoid any single always-recompiled root crate?

Positions:
- `shared-model-crate-vs-domain-split--p1`: Keep one shared low-level "model" crate rather than doing a full domain-driven crate split
- `shared-model-crate-vs-domain-split--alt1`: Split the codebase along domain lines

Claims:
- `b-sb25-f012561-c2` · Voice: Tristan · Source: https://youtube.com/watch?v=_FIDuLV0ZsA (`f012561`) · Date: 2025-06-18 · Locator: ~26:33-27:33 (audience Q&A)
  - Quote: "when the splits occured it was already too late ... I couldn't find the time and the energy to ... split"
  - Paraphrase: when asked directly by an audience member whether he considered a domain-driven crate separation instead of "everything depends on model," he says he could have, but the split happened too late in the project's life to be worth the time and energy, so `model` became a catch-all for whatever must be shared, kept as small as discipline allows

## Question `shared-mutable-state-vs-explicit-passing`

When to use `Rc`/`Arc` with `RefCell`/`Mutex`, and when to restructure for single ownership, explicit `&mut` or context passing?

Positions:
- `shared-mutable-state-vs-explicit-passing--restructure-for-explicit-ownership`: Avoid implicit shared state; pass context or `&mut`, drop forced `Arc`
- `shared-mutable-state-vs-explicit-passing--shared-where-structure-demands`: `Rc`/`Arc` where reader count is hard to know; `RefCell` narrowly

Claims:
- `a-sR07-f002155-c1` · Voice: Yatekii · Source: https://github.com/probe-rs/probe-rs/pull/2852 (`f002155`) · Date: 2024-12-03 · Locator: comment "I dont think the Mutex is necessary as the sequences are held on the session which should then go into the mutex. Not internally."
  - Quote: "I dont think the Mutex is necessary as the sequences are held on the session which should then go into the mutex."
  - Paraphrase: rather than adding a `Mutex` inside the type to satisfy a `Sync` bound, move the mutable state to the owning `Session` and access it there
- `b-sT09-f005440-c1` · Voice: Serdar Yegulalp (InfoWorld senior writer) · Source: https://infoworld.com/article/3815535/rust-memory-management-explained.html (`f005440`) · Date: 2025-02-12 · Locator: § Automatic memory management and Rust types, paragraphs 3–4
  - Quote: "Do use them when the structure of a program makes it hard to tell how many readers will exist for a given piece of data."
  - Paraphrase: Rc and Arc are recommended when it is hard to tell how many readers a piece of data will have. RefCell moves the borrow rules to run time, works only in single-threaded code and panics on violation. Hence it fits only a narrow range of problems.
- `b-sb04-f001022-c1` · Voice: romgrk · Source: https://github.com/zed-industries/zed/pull/8632 (`f001022`) · Date: 2024-03-02 · Locator: PR #8632, comment 2024-03-02T18:19:01Z
  - Quote: "Actually I'm not sure that would work."
  - Paraphrase: retracts an earlier suggestion to turn the client state fields into `Rc<RefCell<_>>`s, since dispatching an action from inside an active borrow (e.g. a key press changing the keyboard-focused window) would still panic; the only approach that currently works is cloning whatever refs are needed before dropping the state and then dispatching
- `a-sR07-f002155-c2` · Voice: Yatekii · Source: https://github.com/probe-rs/probe-rs/pull/2852 (`f002155`) · Date: 2024-12-19 · Locator: comment "Ah, I disregarded that fact. I would prefer no Arc 🤔 Maybe we can reevaluate in the future."
  - Quote: "I would prefer no Arc 🤔 Maybe we can reevaluate in the future."
  - Paraphrase: prefers avoiding Arc-based shared ownership for this type even after conceding the immediate `Sync` constraint requires it, wanting to revisit the design later
- `a-sa06-f003414-c2` · Voice: ConradIrwin · Source: https://github.com/zed-industries/zed/pull/36497 (`f003414`) · Date: 2025-10-28 · Locator: comment 2025-10-28T01:59:12Z
  - Quote: "I don't like that the Buffer contains an Arc<Mutex<>> that allows callers to change the encoding without the buffer knowing"
  - Paraphrase: objects to a `Buffer` containing an `Arc<Mutex<>>` that lets callers change encoding without the buffer knowing; wants the encoding passed/returned explicitly instead
- `b-sb04-f001022-c2` · Voice: romgrk · Source: https://github.com/zed-industries/zed/pull/8632 (`f001022`) · Date: 2024-03-02 · Locator: PR #8632, comment 2024-03-02T18:19:01Z
  - Quote: "the rest of the codebase seems to be using the pattern of passing a `cx` context down the stack, which avoids this kind of issue"
  - Paraphrase: floats passing a `cx` context down the stack, mirroring the pattern the rest of the codebase already uses, as a way to sidestep the reentrant-borrow panic entirely, alongside noting that Warp's Rust UI blog describes hitting the same `RefCell`/`borrow_mut` crash class in production

## Question `ship-polyfill-before-spec`

before a spec (WASI 0.3 async) is finalized, should the ecosystem ship stopgap/polyfill implementations to unblock development, or wait for the finished standard?

Positions:
- `ship-polyfill-before-spec--p1`: Favors shipping a polyfill ahead of the spec
- `ship-polyfill-before-spec--alt1`: Wait for the finished standard

Claims:
- `b-sR03-f000889-c1` · Voice: Joel Dice (Fermyon, component-model/wasmtime contributor) · Source: https://bytecodealliance.org/articles/plumbers-day-2 (`f000889`) · Date: 2024-02-05 · Locator: bytecodealliance.org/articles/plumbers-day-2, "Async and WASI 0.3" section, talk timestamp 1:11:00. · L465-L472.
  - Quote: a "'polyfill' that devs can play with today while they're waiting for WASI 0.3 and real async."
  - Paraphrase: favors shipping a polyfill ahead of the spec.

## Question `silent-fallback-vs-explicit-error`

When a caller's input is ambiguous or partially satisfiable (multiple matching sockets, or a requested feature with no usable input at all), should the code silently proceed with a plausible default, or fail with an explicit error?

Positions:
- `silent-fallback-vs-explicit-error--p1`: Error on ambiguous multiple-socket input rather than silently pick one
- `silent-fallback-vs-explicit-error--p2`: Error rather than silently fall back when the flag was explicitly requested

Claims:
- `a-sa14-f005079-c6` · Voice: alexcrichton · Source: https://github.com/bytecodealliance/wasmtime/pull/14294 (`f005079`) · Date: 2026-09-10 · Locator: comment 2026-09-10T22:28:43Z
  - Quote: "Should this perhaps return an error if there are multiple TCP sockets listed? Because otherwise using the first feels like it might lead to odd behavior"
  - Paraphrase: asks whether the code should return an error if multiple TCP sockets are listed, rather than silently using the first, since that could cause odd behavior if the first one happens to be the wrong one
- `a-sa14-f005079-c7` · Voice: simolus3 · Source: https://github.com/bytecodealliance/wasmtime/pull/14294 (`f005079`) · Date: 2026-09-11 · Locator: comment 2026-09-11T10:19:47Z
  - Quote: "it might be surprising to explicitly indicate that inherited sockets are requested with `--systemd-listenfd` only to then have wasmtime listen itself because of a mismatched environment variable that's ignored"
  - Paraphrase: made the multiple-socket case an error, and also made it an error to have no usable socket at all, reasoning it would be surprising for `--systemd-listenfd` to silently fall back to wasmtime listening itself because of a mismatched environment variable

## Question `single-pass-vs-multi-pass-iteration`

should derived per-column values be computed in a single iterator pass or via several simpler passes/collects?

Positions:
- `single-pass-vs-multi-pass-iteration--p1`: Prefer single-pass computation over iterating a collected result multiple times
- `single-pass-vs-multi-pass-iteration--alt1`: Several simpler passes or collects

Claims:
- `b-sR03-f000763-c2` · Voice: joshka · Source: https://github.com/ratatui/ratatui/pull/840 (`f000763`) · Date: 2024-01-18 · Locator: ratatui/ratatui#840, comment 2024-01-18T22:33:34Z. · L403-L406.
  - Quote: "If you're iterating and collecting then iterating on the result 3 times or might be neater to iterate and collect the max for each column in a single iteration."
  - Paraphrase: prefer single-pass computation over iterating a collected result multiple times.

## Question `single-vs-multi-threaded-executor`

Should an async application use a single-threaded or multi-threaded executor?

Positions:
- `single-vs-multi-threaded-executor--p1`: Measure for the specific workload, no blanket rule
- `single-vs-multi-threaded-executor--alt1`: A single-threaded executor by default
- `single-vs-multi-threaded-executor--alt2`: a multi-threaded executor by default

Claims:
- `b-bk01-f000233-c13` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "The Async Ecosystem" § Single Threaded vs Multi-Threaded Executors
  - Quote: "It is recommended to measure performance for your application when you are choosing between a single- and a multi-threaded runtime."
  - Paraphrase: a multi-threaded executor can speed up workloads with many tasks by making progress on several simultaneously, but synchronizing data between tasks becomes more expensive; rather than defaulting to one or the other, recommends measuring performance for the application at hand when choosing between a single- and multi-threaded runtime.

## Question `slint-vs-qt`

For cross-platform desktop/embedded GUI development from Rust, should a team adopt a new compile-time-checked toolkit (Slint) over a mature, runtime-interpreted one (Qt/QML), given Slint's smaller ecosystem (missing multimedia, 3D, multi-window, automated UI testing, no iOS support yet)?

Positions:
- `slint-vs-qt--p1`: Prefer Slint over QML/Qt for new Rust GUI work despite Slint's current feature gaps
- `slint-vs-qt--alt1`: Qt/QML

Claims:
- `b-sb23-f011133-c1` · Voice: David Vin (Felgo) · Source: https://youtube.com/watch?v=fexqx6bh1OE (`f011133`) · Date: 2024-07-01 · Locator: "so should you switch to slint" (closing section, ~23:37)
  - Quote: "for me it seems that the slint is the best toolkit currently for rust"
  - Paraphrase: having reimplemented an existing QML demo app in Slint from scratch, he argues Slint's build-time-checked, Rust-native, easily cross-compiled model is worth the tradeoff against QML's more mature multimedia/3D/testing tooling and Qt's licensing costs, especially for embedded targets
