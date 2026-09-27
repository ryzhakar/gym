# Blind fill input, batch 1, file 02 of 13

For each Claim below, name the one Position of its Question that the Claim supports (a Position id from the list), or `none` if it supports none of them. The Claims are in random order.

## Question `boxed-closure-tuple-vs-named-field`

When a public API wraps a `Box<dyn Fn>` behind a required constructor function, should the wrapped closure live in an unnamed tuple-struct field or a named field, given that a constructor already replaces the field's main ergonomic argument (avoiding `Box::new` at call sites)?

Positions:
- `boxed-closure-tuple-vs-named-field--p1`: Tuple struct with constructor
- `boxed-closure-tuple-vs-named-field--p2`: Avoid trait objects in public field
- `boxed-closure-tuple-vs-named-field--p3`: Constructor function mitigates boxing friction
- `boxed-closure-tuple-vs-named-field--p4`: Named field for clarity

Claims:
- `b-sb14-f004398-c4` · Voice: alice-i-cecile · Source: https://github.com/bevyengine/bevy/pull/23315 (`f004398`) · Date: 2026-03-12 · Locator: comment @alice-i-cecile 2026-03-12T19:51:53Z
  - Quote: "The \"stores a boxed function\" is quite tricky for folks who are newer to Rust, so I want to try to optimize clarity. We're already relying on a `new` constructor to do the boxing, so the main benefit of tuple structs is lost."
  - Paraphrase: once a constructor is already required to do the boxing, argues the type should be a one-field named struct rather than a tuple struct, since a boxed function's meaning is unclear to Rust newcomers from a bare tuple field.
- `b-sb14-f004398-c3` · Voice: chescock · Source: https://github.com/bevyengine/bevy/pull/23315 (`f004398`) · Date: 2026-03-11 · Locator: comment @chescock 2026-03-11T20:53:19Z
  - Quote: "one way to mitigate it would be with a constructor function... and then it's just `DespawnOnExitWith::new(|state| true)`."
  - Paraphrase: proposes a `new` constructor that performs the boxing internally, so the type keeps the `Box<dyn Fn>` representation while call sites just write `DespawnOnExitWith::new(|state| ...)`.
- `b-sb14-f004398-c1` · Voice: chescock · Source: https://github.com/bevyengine/bevy/pull/23315 (`f004398`) · Date: 2026-03-11 · Locator: comment @chescock 2026-03-11T19:12:28Z
  - Quote: "It might be useful to let this be used with closures that capture values, like `GameState::Level(level_number)` instead of hard-coded `2`."
  - Paraphrase: suggests storing the predicate as `Box<dyn Fn(&S) -> bool>` in a public tuple-struct field so stateful closures (e.g. capturing a level number) can be used, noting `Box` won't allocate for non-capturing closures.
- `b-sb14-f004398-c2` · Voice: Freyja-moth · Source: https://github.com/bevyengine/bevy/pull/23315 (`f004398`) · Date: 2026-03-11 · Locator: comment @Freyja-moth 2026-03-11T20:24:35Z
  - Quote: "I'd chosen to stay away from trait objects so that users didn't need to write `Box::new` everywhere."
  - Paraphrase: explains the original design avoided exposing the trait object directly so users wouldn't need to write `Box::new` at every call site.

## Question `boxed-vs-hand-written-future`

when a tower `Service::call` needs to inspect or transform the response after the inner future resolves, should its associated `Future` be a boxed dynamic future (`Pin<Box<dyn Future<...> + Send>>`, built with `Box::pin(async move {...})`), or a hand-written `poll`-driven future struct (via `pin-project`) that avoids the heap allocation?

Positions:
- `boxed-vs-hand-written-future--p1`: Prefer `Box::pin(async move {...})` (one heap allocation per request) over a hand-rolled `poll`-based future struct for middleware that needs post-response work, given Lambda's cost profile
- `boxed-vs-hand-written-future--alt1`: Hand-written `poll`-based future struct with no allocation

Claims:
- `b-sb22-f008906-c2` · Voice: Luciano Mammino · Source: https://loige.co/writing-middlewares-for-rust-lambda-functions (`f008906`) · Date: 2026-05-03 · Locator: section "What did we trade?"
  - Quote: "Down: zero heap allocations per request... In Lambda, that is irrelevant. In a tight loop on a busy server, it can matter."
  - Paraphrase: a hand-rolled `LogFuture<F>` with `pin-project` avoids all per-request heap allocation at the cost of ~30 extra lines, an extra struct, and a new dependency; in Lambda that allocation "is irrelevant," so the boxed-async shape is the idiomatic default, and hand-rolling is reserved for a tight loop on a busy server

## Question `breaking-rename-for-vocabulary`

Should a library perform a broad breaking rename across its whole public API to align vocabulary with its current mental model, or keep legacy names for compatibility?

Positions:
- `breaking-rename-for-vocabulary--p1`: Rename for vocabulary consistency pre 1.0
- `breaking-rename-for-vocabulary--alt1`: Keep legacy names for compatibility

Claims:
- `b-sR08-f003731-c2` · Voice: ramfox · Source: https://iroh.computer/blog/iroh-0-94-0-the-endpoint-takeover (`f003731`) · Date: 2025-10-22 · Locator: § "Changing from Node to Endpoint everywhere"
  - Quote: "We've officially made the decision to remove the word "node" from our vocabulary... In preparation for 1.0, that has been rectified."
  - Paraphrase: dropped "node" from iroh's vocabulary project-wide (`NodeAddr`→`EndpointAddr`, `node_id`→`endpoint_id`, etc.), reasoning that the term was a holdover from an earlier, broader project scope, and that pre-1.0 is the right moment to align vocabulary with the current mental model despite the breaking change this causes.

## Question `breaking-wire-change-in-minor`

Should a pre-1.0 Rust networking library ship breaking wire-protocol changes in a routine minor release for a protocol improvement, or keep compatibility with the previous release?

Positions:
- `breaking-wire-change-in-minor--p1`: Break compat with transition window
- `breaking-wire-change-in-minor--alt1`: Keep wire compatibility with the previous release

Claims:
- `a-sT04-f001319-c1` · Voice: dignifiedquire (byline, iroh blog; Rust connection in source: iroh release post with Rust API code) · Source: https://iroh.computer/blog/iroh-0-14-0-dial-the-world (`f001319`) · Date: 2024-04-18 · Locator: section "Faster relay handshakes"
  - Quote: "Unfortunately, this means the new relays can not talk to 0.13.0 nodes."
  - Paraphrase: The relay handshake was refactored to drop a full roundtrip on every new connection. The team accepted that new relays cannot talk to 0.13.0 nodes, and softened it by keeping the old relays running for at least 4 more weeks.

## Question `build-tool-cargo-subcommand-vs-standalone`

Should ecosystem build tooling that outgrows Cargo's scope ship as a `cargo` subcommand, or as an independent CLI / cargo-replacement?

Positions:
- `build-tool-cargo-subcommand-vs-standalone--p1`: Cargo subcommand
- `build-tool-cargo-subcommand-vs-standalone--p2`: Standalone or replacement

Claims:
- `a-sa05-f003025-c3` · Voice: jkelleyrtp · Source: https://github.com/bevyengine/bevy/issues/19296 (`f003025`) · Date: 2025-06-01 · Locator: comment @jkelleyrtp 2025-06-01T09:00:03Z
  - Quote: "wasm-bindgen is the most used cli in the rust ecosystem and it is not a subcommand."
  - Paraphrase: cargo cannot run/test/bench wasm, iOS or Android projects, so wasm-bindgen and similar high-usage tools are standalone by necessity, and dx follows that pattern since Dioxus is not exclusively a Rust tool
- `a-sa05-f003025-c4` · Voice: janhohenheim · Source: https://github.com/bevyengine/bevy/issues/19296 (`f003025`) · Date: 2025-06-01 · Locator: comment @janhohenheim 2025-06-01T11:49:48Z
  - Quote: "The frustrations with cargo's limitations and its glacial development cycle has led this very project to design the Bevy CLI alpha as a cargo replacement / wrapper and not a subcommand."
  - Paraphrase: cargo's limitations and slow development cycle led Bevy to design its CLI as a cargo wrapper/replacement rather than a subcommand
- `a-sa05-f003025-c5` · Voice: BD103 · Source: https://github.com/bevyengine/bevy/issues/19296 (`f003025`) · Date: 2025-06-01 · Locator: comment @BD103 2025-06-01T19:12:02Z
  - Quote: "it's less that Cargo is lacking features and more that certain features are too specific to be included in a standard Rust distribution."
  - Paraphrase: Bevy-specific needs (asset handling, default index.html for the web feature) don't fit a general-purpose stable tool like Cargo; better to build 3rd-party tools on top of Cargo than have Cargo grow narrow features
- `a-sa05-f003025-c2` · Voice: TapGhoul · Source: https://github.com/bevyengine/bevy/issues/19296 (`f003025`) · Date: 2025-06-01 · Locator: comment @TapGhoul 2025-06-01T11:36:46Z
  - Quote: "I'd argue that a subsecond CLI tool makes a lot of sense as a cargo subcommand, given the general pattern I've seen."
  - Paraphrase: subcommands are functionally identical to standalone binaries plus a few injected env vars, so a rust-ecosystem tool aiming for wide reuse should still register as a subcommand
- `a-sa05-f003025-c1` · Voice: teohhanhui · Source: https://github.com/bevyengine/bevy/issues/19296 (`f003025`) · Date: 2025-06-01 · Locator: comment @teohhanhui 2025-06-01T09:36:41Z
  - Quote: "That's how you kill an ecosystem. It should be a `cargo` subcommand, please."
  - Paraphrase: rejects a standalone "cargo plus plus" tool; ecosystem tools should be `cargo` subcommands

## Question `built-in-async-runtime`

Should the language provide a built-in async runtime, or leave runtime choice to the crate ecosystem?

Positions:
- `built-in-async-runtime--p1`: No built-in runtime, ecosystem choice
- `built-in-async-runtime--alt1`: Provide a built-in async runtime in the language

Claims:
- `b-bk01-f000233-c2` · Voice: async-book (rust-lang.github.io, Rust Async Working Group) · Source: https://rust-lang.github.io/async-book (`f000233`) · Date: 2026-09-27 · Locator: chapter "Async and Await" § The runtime
  - Quote: "Rust lets you choose one depending on your requirements, rather than providing one."
  - Paraphrase: Rust is a low-level language that strives for minimal runtime overhead, so unlike many languages whose runtime does memory management, exception handling, etc., Rust's async runtime has limited scope and is left to the ecosystem rather than built in; this means getting started requires an extra step (choosing a runtime crate).

## Question `builtin-package-manager-effect`

Does a language's built-in, first-party package manager (like Cargo) meaningfully change engineering practice compared to bolted-on/ecosystem-only dependency management (as in C/C++)?

Positions:
- `builtin-package-manager-effect--p1`: Builtin package manager changes practice
- `builtin-package-manager-effect--alt1`: A built-in package manager does not materially change practice

Claims:
- `a-sR15-f008241-c2` · Voice: gregstoll · Source: https://gregstoll.wordpress.com/2025/01/08/floating-point-to-hex-converter-now-supports-16-bit-floats-plus-i-rewrote-it-in-rust-and-webassembly (`f008241`) · Date: 2025-01-08 · Locator: section "Maybe…Rust?"
  - Quote: "I think this is an example of why having a good builtin package manager matters; even if I had found a C/C++ one I would have had to copy its source into my project or something. […] But just running cargo add half is so easy!"
  - Paraphrase: didn't even think to look for a C/C++ library with `f16`/bfloat support, because even if one existed they'd have had to vendor its source; running `cargo add half` was trivially easy by comparison, which they read as evidence that a good builtin package manager matters

## Question `byte-vs-bit-packed-cells`

Should per-cell state be stored one byte per cell or packed as bits?

Positions:
- `byte-vs-bit-packed-cells--p1`: Bit-packed FixedBitSet over one-byte-per-cell Vec<Cell>
- `byte-vs-bit-packed-cells--alt1`: One byte per cell

Claims:
- `b-bk02-f000256-c4` · Voice: rustwasm working group (Rust and WebAssembly book) [voice-unverified] · Source: https://rustwasm.github.io/docs/book (`f000256`) · Date: unknown (living doc) · Locator: § "Implementing Conway's Game of Life" exercises, Answer 2
  - Quote: "Representing each cell with a byte makes iterating over cells easy, but it comes at the cost of wasting memory."
  - Paraphrase: names the byte-per-cell layout's cost explicitly (wastes 7 of 8 bits per cell) against the bit-packed alternative, and provides the FixedBitSet-based rewrite as the resolution.

## Question `c-maintainers-rust-bindings-duty`

When a C-subsystem maintainer changes their C code in a way that breaks the corresponding Rust abstraction/bindings, should the C maintainer be expected to help keep the Rust side correct (or at least not block small Rust-motivated robustness fixes to the C code), or is it legitimate for C maintainers to fix only their own C code and decline responsibility for Rust bindings entirely?

Positions:
- `c-maintainers-rust-bindings-duty--p1`: C maintainers not obligated to rust
- `c-maintainers-rust-bindings-duty--p2`: Rust needs c maintainer cooperation
- `c-maintainers-rust-bindings-duty--p3`: Adoption slow for practical reasons

Claims:
- `b-sb18-f005332-c4` · Voice: Linus Torvalds · Source: https://arstechnica.com/gadgets/2024/09/rust-in-linux-lead-retires-rather-than-deal-with-more-nontechnical-nonsense (`f005332`) · Date: August 2024 (public appearance, per the article) · Locator: arstechnica.com article, quoting his remarks at a public appearance
  - Quote: "I was expecting [Rust] updates to be faster, but part of the problem is that old-time kernel developers are used to C and don't know Rust. They're not exactly excited about having to learn a new language that is, in some respects, very different. So there's been some pushback on Rust."
  - Paraphrase: agrees there has been pushback on Rust, attributing it to old-time C kernel developers being unfamiliar with and unenthusiastic about learning a new, quite different language, plus instability in the Rust kernel infrastructure itself, rather than to bad faith
- `b-sb18-f005332-c1` · Voice: Ted Ts'o · Source: https://arstechnica.com/gadgets/2024/09/rust-in-linux-lead-retires-rather-than-deal-with-more-nontechnical-nonsense (`f005332`) · Date: undated (conference talk clip, reported in the 2024-09-04 article) · Locator: arstechnica.com article, quoting an off-camera interjection during a Linux conference talk, identified by Wedson Almeida Filho in a Register interview
  - Quote: "Here's the thing: you're not going to force all of us to learn Rust."
  - Paraphrase: interjects during a talk (about Filho's request that a filesystem gain Rust bindings) that while he will fix his own C code, he will not fix Rust bindings that break as a result, and won't be forced to learn Rust
- `b-sb18-f005332-c2` · Voice: Wedson Almeida Filho · Source: https://arstechnica.com/gadgets/2024/09/rust-in-linux-lead-retires-rather-than-deal-with-more-nontechnical-nonsense (`f005332`) · Date: 2024-08 (week before the 2024-09-04 article) · Locator: arstechnica.com article, quoting his Linux kernel mailing list resignation post
  - Quote: "After almost 4 years, I find myself lacking the energy and enthusiasm I once had to respond to some of the nontechnical nonsense, so it's best to leave it up to those who still have it in them."
  - Paraphrase: resigns as Rust-for-Linux maintainer after almost 4 years, citing exhaustion with "nontechnical nonsense" rather than technical disagreement, and states the future of kernels is with memory-safe languages
- `b-sb18-f005332-c3` · Voice: Asahi Lina · Source: https://arstechnica.com/gadgets/2024/09/rust-in-linux-lead-retires-rather-than-deal-with-more-nontechnical-nonsense (`f005332`) · Date: late August 2024 (Mastodon post, per the article) · Locator: arstechnica.com article, quoting her Mastodon post
  - Quote: "But I get the feeling that some Linux kernel maintainers just don't care about future code quality, or about stability or security any more. They just want to keep their C code and wish us Rust folks would go away."
  - Paraphrase: says she "regretfully completely understands" Filho's frustration, describes being blocked by a C maintainer from pushing small robustness/lifetime fixes to the DRM scheduler's C code, and that every kernel panic in her Apple GPU driver traces to bugs in that C code, not her Rust code

## Question `cancel-safety-requirement`

Must async Rust APIs (RPC channels, mpmc `recv`) be cancel-safe?

Positions:
- `cancel-safety-requirement--cancel-safety-required`: Cancel safety is required; its absence is a bug or rules a crate out
- `cancel-safety-requirement--alt1`: Cancel safety is a documented caller responsibility, or an acceptable trade for performance

Claims:
- `b-sb17-f005159-c4` · Voice: Rüdiger Klaehn · Source: https://iroh.computer/blog/async-rust-challenges-in-iroh (`f005159`) · Date: 2024-07-31 · Locator: article body, "Choosing an mpmc channel" section
  - Quote: "cancel safety for recv is a must in many places where we use it internally... So for now we are going to use async-channel as the standard mpmc queue."
  - Paraphrase: found flume's `recv` occasionally not cancel-safe in practice (lost notifications causing stuck tasks), and requires cancel-safety on recv even though flume intentionally accepts a cancel-safety gap on `send` for performance; switches to async-channel, which fixed the reproducer
- `a-sT04-f001650-c1` · Voice: ramfox (byline, iroh blog; Rust connection in source: iroh release post, Rust code, and "the quic-rpc crate, which is a crate that we've written") · Source: https://iroh.computer/blog/iroh-0-19-make-it-your-own (`f001650`) · Date: 2024-06-27 · Locator: section "Better late than never"
  - Quote: "Turns out, our RPC channels were not cancel-safe."
  - Paraphrase: The team broke its two-week release cadence because it found a rare, high-load critical bug: its RPC channels were not cancel-safe. They fixed it in quic-rpc and upgraded iroh before releasing. The documented-caller-responsibility alternative is not named in the source; the Position rests on the stated reason (critical bug, fix immediately).

## Question `cfg-wasm-as-reduced-platform-proxy`

should crates use `cfg(target_family = "wasm")` / `cfg(target_arch = "wasm32")` as a proxy for "running in a reduced-functionality standalone browser build," given that some Wasm targets now offer full Linux syscall access (filesystem, threads, subprocesses)?

Positions:
- `cfg-wasm-as-reduced-platform-proxy--p1`: Deliberately misreport target metadata (`target_family` without "wasm", `arch: "wasm64"`) to defeat crates' `cfg`-based assumptions that "wasm32" implies a reduced-functionality standalone web build
- `cfg-wasm-as-reduced-platform-proxy--alt1`: Treat `cfg(target_family = "wasm")` as a reliable proxy for a reduced platform

Claims:
- `b-sb22-f009062-c2` · Voice: Yuri Iozzelli · Source: https://labs.leaningtech.com/blog/browserpod-rust (`f009062`) · Date: 2026-08-13 · Locator: section "The hacks we did along the way"
  - Quote: "we would love to get rid of these hacks, but the proper solution requires awareness in the ecosystem that fully-featured Wasm targets exist"
  - Paraphrase: many crates special-case behavior (e.g. `reqwest` swapping in a `fetch()`-based client) whenever they see the "wasm" target family or `wasm32` arch, which is wrong for a target with full syscall access; the team calls these misreports "hacks" pending the ecosystem recognizing that fully-featured Wasm targets exist

## Question `cli-flag-convenience-vs-consistency`

For a CLI flag guarding a destructive action where the safe default is dry-run, should the flag's naming prioritize brevity/typing convenience (default-on dry-run, `--no-dry-run` to opt out) or consistency with how sibling commands in the same tool name their flags?

Positions:
- `cli-flag-convenience-vs-consistency--p1`: Consistency across commands
- `cli-flag-convenience-vs-consistency--p2`: Convenience over consistency

Claims:
- `b-sb09-f003036-c1` · Voice: MabezDev · Source: https://github.com/esp-rs/esp-hal/pull/3510 (`f003036`) · Date: 2025-05-21 · Locator: comment @MabezDev 2025-05-21T14:11:47Z
  - Quote: "Everywhere else we've use the `--no-dry-run`, I think we should be consistent."
  - Paraphrase: argues the new command should use `--no-dry-run` like every other command in the tool, for consistency.
- `b-sb09-f003036-c2` · Voice: bugadani · Source: https://github.com/esp-rs/esp-hal/pull/3510 (`f003036`) · Date: 2025-05-21 · Locator: comment @bugadani 2025-05-21T14:48:33Z
  - Quote: "my thinking was that this isn't actually dangerous to get wrong, but --no-dry-run is sufficiently annoying to type. I can change it, we'll hate it"
  - Paraphrase: reasons that getting this particular flag wrong isn't dangerous, and `--no-dry-run` is annoying enough to type that a different default might be worth it, though agrees to change it if asked.

## Question `cli-flags-mirror-familiar-tool`

For a niche, protocol-specific CLI tool, should its flags follow the conventions of an already-familiar general-purpose tool (curl), or be designed fresh around the tool's own domain?

Positions:
- `cli-flags-mirror-familiar-tool--p1`: Mirror an established CLI's conventions rather than design fresh
- `cli-flags-mirror-familiar-tool--alt1`: Design flags fresh around the tool's own domain

Claims:
- `a-sa14-f004947-c1` · Voice: Hannah Wang, Ben Yang, and Fisher Darling · Source: https://blog.cloudflare.com/open-sourcing-our-privacy-proxy-cli (`f004947`) · Date: 2026-07-27 · Locator: § What pvcli can do
  - Quote: "We designed it with the "principle of least surprise" in mind. As a result, a lot of the arguments are the same as curl's!"
  - Paraphrase: state they designed pvcli around curl's argument conventions on purpose, for familiarity, rather than inventing new flag names for the OHTTP/proxy domain

## Question `cli-output-overwrite-default`

Should a CLI tool that repeatedly writes an output file overwrite the same filename by default (simpler, faster iteration, matches a peer tool's behavior), or auto-generate a timestamped filename by default to avoid silently discarding a previous result?

Positions:
- `cli-output-overwrite-default--p1`: Default overwrite latest output
- `cli-output-overwrite-default--p2`: Default timestamp to avoid silent overwrite

Claims:
- `b-sb13-f004160-c4` · Voice: bugadani · Source: https://github.com/probe-rs/probe-rs/pull/3789 (`f004160`) · Date: 2026-02-26 · Locator: comment 2026-02-26T08:51:24Z
  - Quote: "I think a passable strategy is to save the profile with the timestamp in the filename, either by default, or only for the second file and later."
  - Paraphrase: recommends timestamping the output filename, by default or at least from the second run onward, so a new profile does not silently replace an old one
- `b-sb13-f004160-c3` · Voice: KingCol13 · Source: https://github.com/probe-rs/probe-rs/pull/3789 (`f004160`) · Date: 2026-02-26 · Locator: comment 2026-02-26T18:56:23Z
  - Quote: "I still have a preference for overwriting. Currently I don't have to edit the commands from my history to quickly display the new profile... This also matches `samply`'s behaviour which I couldn't find anyone complaining about."
  - Paraphrase: prefers overwriting the same output filename by default so past shell commands can be reused unedited to view the latest profile, matching the behavior of the peer tool samply

## Question `cli-tool-single-vs-multi-protocol`

Should a debugging CLI for a protocol specialize narrowly, one tool per protocol, or bundle several related protocols into one tool?

Positions:
- `cli-tool-single-vs-multi-protocol--p1`: One CLI should cover every privacy protocol a team operates (OHTTP, CONNECT proxying, MASQUE, Privacy Pass), rather than a narrow tool per protocol
- `cli-tool-single-vs-multi-protocol--alt1`: One narrow tool per protocol

Claims:
- `b-sR11-f004947-c1` · Voice: Hannah Wang, Ben Yang, Fisher Darling (Cloudflare) · Source: https://blog.cloudflare.com/open-sourcing-our-privacy-proxy-cli (`f004947`) · Date: 2026-07-27 · Locator: "Why build our own tool?" section
  - Quote: "nothing combines OHTTP, CONNECT proxying, MASQUE and Privacy Pass (coming soon) all in one place"
  - Paraphrase: existing OHTTP-only tools (Thomson's Rust implementation, Wood's Go implementation) were useful but narrow; pvcli's differentiator is combining OHTTP, CONNECT proxying, MASQUE and Privacy Pass in one place

## Question `close-future-result-vs-infallible`

Should a close/shutdown future return a Result or be infallible?

Positions:
- `close-future-result-vs-infallible--p1`: Infallible close future
- `close-future-result-vs-infallible--alt1`: Return a `Result` from close

Claims:
- `b-sT05-f002550-c3` · Voice: ramfox, matheus23 · Source: https://iroh.computer/blog/iroh-0-31-0-back-to-fighting-fit (`f002550`) · Date: 2025-01-15 · Locator: § Breaking Changes › iroh › changed
  - Quote: "iroh::Endpoint::close's future is now infallible, instead of returning a Result"
  - Paraphrase: Endpoint::close's future no longer returns a Result

## Question `cloud-lock-in-source`

Is the primary source of cloud vendor lock-in the compute platform you deploy to, or the managed data/SDK layer you build against?

Positions:
- `cloud-lock-in-source--p1`: Compute-platform choice is a smaller lock-in risk than adopting a cloud's proprietary managed-data SDK; ports-and-adapters (hexagonal) architecture removes the compute-level lock-in concern
- `cloud-lock-in-source--alt1`: The compute platform is the primary lock-in

Claims:
- `a-sa24-f011220-c2` · Voice: James Eastham · Source: https://youtube.com/watch?v=x4yUfs0GrI4 (`f011220`) · Date: 2024-12-13 · Locator: ~13:48-14:12
  - Quote: "using proprietary database Services...that is more of a form of locking than the compute you choose to use"
  - Paraphrase: refactoring a Postgres-backed service to a proprietary store like DynamoDB, CosmosDB or Firestore forces a specific SDK and data model, which locks you in more than the choice of compute; structuring the codebase with entry-point adapters around a core business-logic crate lets the same Rust application run on Fargate/ECS or Lambda interchangeably, which he presents as the fix for vendor lock-in fears about serverless compute

## Question `codegen-macro-vs-generated-source`

should a Rust code generator emit its output as procedural-macro magic or as plain generated source files?

Positions:
- `codegen-macro-vs-generated-source--p1`: Plain-generated-source over macro-based codegen (for client generation specifically)
- `codegen-macro-vs-generated-source--alt1`: Emit output as procedural-macro expansion

Claims:
- `a-sa23-f011186-c2` · Voice: Adam · Source: https://youtube.com/watch?v=bjgGboWCTDw (`f011186`) · Date: 2024-11-20 · Locator: ~00:19:37
  - Quote: "it doesn't use macros it doesn't create this in line it's outputting normal rust code and this is I think a really good approach because as much as I do like using macros they're so hard to debug"
  - Paraphrase: his tool emits a normal on-disk Rust crate (source dir, Cargo.toml, .rs files) rather than inline macro output, because macro output is hard to debug and macros can produce confusing compile errors

## Question `compile-time-cost-of-generated-crates`

is a long compile time an acceptable cost of large generated/dependency-heavy crates in exchange for API correctness and ergonomics?

Positions:
- `compile-time-cost-of-generated-crates--p1`: Accept long compile times for generated-crate quality
- `compile-time-cost-of-generated-crates--alt1`: Shrink generated crates to cut compile time, even at a cost to the API

Claims:
- `a-sa23-f011186-c5` · Voice: Adam · Source: https://youtube.com/watch?v=bjgGboWCTDw (`f011186`) · Date: 2024-11-20 · Locator: ~00:30:09
  - Quote: "eventually I kind of just decided I'd rather eat the long compile time and be able to give really high quality API to my users"
  - Paraphrase: large autogenerated API crates (his own and others', e.g. Stripe's) dominate his project's slowest-compiling dependencies, especially in release mode; after looking for ways to shrink them, he chose to accept the compile-time cost rather than sacrifice API quality

## Question `compile-time-typed-dsl`

Is hosting a Rust DSL's programs as compile-time types (zero runtime cost, no dynamic loading) worth trading away runtime-loaded/dynamic DSL programs?

Positions:
- `compile-time-typed-dsl--p1`: Compile time typed dsl
- `compile-time-typed-dsl--alt1`: Runtime-loaded, dynamic DSL programs

Claims:
- `a-sa16-f007175-c2` · Voice: Soares Chen · Source: https://contextgeneric.dev/blog/hypershell-release (`f007175`) · Date: 2025-06-14 · Locator: § Disadvantages, Dynamic Loading
  - Quote: "since the DSL is hosted at compile time, this technique cannot be easily used to run DSL programs loaded into a host application during runtime"
  - Paraphrase: Hosting DSL programs as compile-time types trades away runtime dynamic loading (config files, plugins, game mods) for zero-cost, compile-time interpretation.

## Question `compile-time-vs-runtime-switches`

Should test-only or staging behaviour be switched by Cargo features, `#[cfg]` or compile-time env vars, or by runtime options?

Positions:
- `compile-time-vs-runtime-switches--runtime-switch`: Switch at runtime, dropping cfg or compile-time env vars
- `compile-time-vs-runtime-switches--alt1`: Switch at compile time (Cargo features, `#[cfg]`, compile-time env vars)

Claims:
- `b-sT05-f002550-c1` · Voice: ramfox, matheus23 (iroh / n0 blog authors) · Source: https://iroh.computer/blog/iroh-0-31-0-back-to-fighting-fit (`f002550`) · Date: 2025-01-15 · Locator: § relay-only mode for testing
  - Quote: "The DEV_RELAY_ONLY compile time environment variable has been completely dropped"
  - Paraphrase: compile-time env var dropped; option threaded through the stack when test-utils is enabled; framed as "more programmatically sound"
- `b-sT04-f002233-c1` · Voice: n0, inc. / iroh team (post by ramfox) · Source: https://iroh.computer/blog/iroh-0-27-0-Squashing-Bugs-And-Taking-Names (`f002233`) · Date: 2024-10-24 · Locator: § "Sensible config options can go a looooong way"
  - Quote: "We no longer rely on the test-utils feature or the #[cfg(test)] annotations for determining whether code runs against production or staging infrastructure"
  - Paraphrase: A bug made builds pick the wrong relay servers (production vs staging), and the old config made it "too easy to point production code to our staging relays". So iroh-net no longer uses the `test-utils` feature or `#[cfg(test)]` to decide which infrastructure code runs against. It relies only on the `IROH_FORCE_STAGING_RELAYS` environment variable, behind a new `force_staging_infra` function.

## Question `compiler-triage-automation`

Should routine compiler-team process work (PR triage/bookkeeping, nudging reviewers, tracking regressions) be fully automated, or does it need a human doing it manually to protect contributors' limited time and avoid over-pinging them?

Positions:
- `compiler-triage-automation--p1`: Keep PR-nudging/triage bookkeeping partly manual rather than fully automating it
- `compiler-triage-automation--alt1`: Fully automate the triage bookkeeping

Claims:
- `b-sb23-f011235-c1` · Voice: Antonio Pirino · Source: https://youtube.com/watch?v=-3KKeeZkYog (`f011235`) · Date: 2025-06-10 · Locator: ~05:14-06:15
  - Quote: "there is one thing that is ... that I really care about ... we have on one end [a finite] amount of resources[; c]ontributors ... can allocate only a[f]inite amount of time"
  - Paraphrase: he maintains a manual markdown bookkeeping file cross-referenced against the triage bot's oldest-PR list, and explicitly poses "why can this not be completely automated?" to himself, answering that contributors have only a finite amount of time and are "a precious asset," so a human judgment call on when to nudge a reviewer avoids over-pressuring them, even though external contributors also expect timely responses

## Question `component-abi-special-case-lowerings`

In the Component Model's GC canonical ABI, should common shapes (e.g. `null` for `none`/`error`, a boolean `i32` for a no-payload `result`) get ad hoc special-cased lowerings for efficiency, or should the ABI stick to one regular, shape-driven lowering rule per component type?

Positions:
- `component-abi-special-case-lowerings--p1`: Ad hoc optimize common shapes
- `component-abi-special-case-lowerings--p2`: Regular lowering only
- `component-abi-special-case-lowerings--p3`: Cautious of shape proliferation

Claims:
- `a-sa05-f003074-c2` · Voice: rossberg · Source: https://github.com/WebAssembly/component-model/issues/525 (`f003074`) · Date: 2025-06-06 · Locator: comment @rossberg 2025-06-06T09:39:34Z
  - Quote: "FWIW, I don't think it is gonna be even close to 95%. Languages with parametric polymorphism typically don't or can't do such a specialisation"
  - Paraphrase: disputes that the null-for-none optimization would apply to anywhere near 95% of options in practice, because languages with parametric polymorphism (e.g. Java's Optional) typically cannot perform that specialization without costly runtime type dispatch
- `a-sa05-f003074-c1` · Voice: lukewagner · Source: https://github.com/WebAssembly/component-model/issues/525 (`f003074`) · Date: 2025-06-04 · Locator: comment @lukewagner 2025-06-04T21:38:44Z
  - Quote: "we are licensed to do that in the CABI when it's a significant win and `option` is very common"
  - Paraphrase: proposes letting `ref.null` represent `none`/no-error when the inner type disallows null, and using a boolean `i32` for no-payload `result`, since these shapes are extremely common and "licensed" as CABI-level wins even though ad hoc
- `a-sa05-f003074-c3` · Voice: fitzgen · Source: https://github.com/WebAssembly/component-model/issues/525 (`f003074`) · Date: 2025-06-13 · Locator: comment @fitzgen 2025-06-13T19:02:24Z
  - Quote: "It seems to me like this could potentially be a slippery slope: How many shapes is enough?"
  - Paraphrase: allowing extra matched shapes like `i31ref` risks a slippery slope of "how many shapes is enough," so any widening of matchable shapes needs an explicit design principle, not case-by-case allowances

## Question `component-map-duplicate-keys`

When lifting/lowering a component-model `map<K,V>` value with duplicate keys, should bindings generators be required to normalize to a defined winner (e.g. last-key-wins), should the spec instead mandate key uniqueness as an enforced boundary constraint, or should a host be permitted but not required to deduplicate, leaving the behavior non-deterministic?

Positions:
- `component-map-duplicate-keys--p1`: Generators must normalize last wins
- `component-map-duplicate-keys--p2`: Mandate uniqueness enforced at boundary
- `component-map-duplicate-keys--p3`: Host may not must dedupe

Claims:
- `b-sb11-f003384-c5` · Voice: badeend · Source: https://github.com/WebAssembly/component-model/pull/554 (`f003384`) · Date: 2025-08-24 · Locator: https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-24T19:46:08Z
  - Quote: "we could likewise non-deterministically allow-but-not-require duplicate keys to be merged (with well-defined last-value-overwrites semantics when such merging occurs)."
  - Paraphrase: argues hosts should be allowed, not required, to deduplicate keys, drawing an analogy to how NaN payload canonicalization is optional rather than mandatory at component boundaries
- `b-sb11-f003384-c2` · Voice: lann · Source: https://github.com/WebAssembly/component-model/pull/554 (`f003384`) · Date: 2025-08-20 · Locator: https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-20T18:54:54Z
  - Quote: "Generated map interfaces MUST behave as if duplicate entries have been filtered out (last duplicate key value wins). Map values with existing duplicate entries MAY be passed to other components."
  - Paraphrase: drafts the concrete requirement that generated map interfaces must behave as if duplicates were filtered with last-value-wins semantics
- `b-sb11-f003384-c3` · Voice: primoly · Source: https://github.com/WebAssembly/component-model/pull/554 (`f003384`) · Date: 2025-08-20 · Locator: https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-20T17:30:35Z
  - Quote: "I think uniqueness of keys should be mandated by the spec and enforced at the boundary."
  - Paraphrase: argues duplicate keys should not be silently tolerated; uniqueness should be a spec-mandated, boundary-enforced constraint
- `b-sb11-f003384-c4` · Voice: ouillie · Source: https://github.com/WebAssembly/component-model/pull/554 (`f003384`) · Date: 2025-08-20 · Locator: https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-20T18:52:54Z
  - Quote: "I have no issue with mandating uniqueness in the spec... I don't think the lowering should trap."
  - Paraphrase: agrees uniqueness should be mandated in the spec, but on violation the lowering side should just silently keep the final value rather than trap
- `b-sb11-f003384-c1` · Voice: lukewagner · Source: https://github.com/WebAssembly/component-model/pull/554 (`f003384`) · Date: 2025-08-20 · Locator: https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-20T16:16:14Z
  - Quote: "would it make sense to say \"Although the Component Model cannot enforce this property, bindings generators **MUST** ...\"?"
  - Paraphrase: proposes strengthening the spec wording so bindings generators are required, not merely expected, to normalize duplicate-key handling

## Question `component-map-ordering`

Should the component-model `map` type guarantee iteration order (and be renamed to signal that), or should it be explicitly unordered like the hash-map types of most host languages?

Positions:
- `component-map-ordering--p1`: Preserve order rename type
- `component-map-ordering--p2`: Unordered by default
- `component-map-ordering--p3`: Deterministic profile may need canonical order

Claims:
- `b-sb11-f003384-c7` · Voice: ouillie · Source: https://github.com/WebAssembly/component-model/pull/554 (`f003384`) · Date: 2025-08-20 · Locator: https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-20T18:52:54Z
  - Quote: "I don't think the basic map type should be ordered. Most languages do not use an ordered basic map type because 9 times out of 10 you don't need an ordering for your maps."
  - Paraphrase: argues the basic map type should not be ordered since most languages' basic map types aren't, with an ordered variant left to `list<tuple<key,value>>` if ever needed
- `b-sb11-f003384-c8` · Voice: badeend · Source: https://github.com/WebAssembly/component-model/pull/554 (`f003384`) · Date: 2025-08-24 · Locator: https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-24T19:46:08Z
  - Quote: "Agree that keys of `map`s should not guarantee any order. This aligns with Rust's HashMap, .NET's Dictionary, Java's HashMap, Go's map, and probably more."
  - Paraphrase: keys of `map` should not guarantee any order, citing Rust's HashMap, .NET's Dictionary, Java's HashMap and Go's map as precedent for unordered semantics
- `b-sb11-f003384-c6` · Voice: primoly · Source: https://github.com/WebAssembly/component-model/pull/554 (`f003384`) · Date: 2025-08-20 · Locator: https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-20T17:30:35Z
  - Quote: "it should be expected that bindings will map `map` to a type that retains order. It would then also be a good idea to rename to something else (e.g. `dict`, `ordered-map`)"
  - Paraphrase: expects bindings to preserve entry order since most languages' Map types do, and would rename the type (e.g. `dict`, `ordered-map`) to avoid confusion with non-order-preserving maps
- `b-sb11-f003384-c9` · Voice: lukewagner · Source: https://github.com/WebAssembly/component-model/pull/554 (`f003384`) · Date: 2025-08-26 · Locator: https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-26T19:13:32Z
  - Quote: "Since the deterministic profile can't randomly permute, if we don't normalize order in the deterministic profile, then that effectively makes order an observable part of the semantics of `map` values."
  - Paraphrase: notes that if a deterministic execution profile doesn't normalize map order, order becomes an observable part of `map`'s semantics, which is a tradeoff worth discussing rather than settled

## Question `compress-debug-sections-default`

should rustc set `--compress-debug-sections=zstd` as the default linker flag for Linux targets, to shrink `target/` and binary size?

Positions:
- `compress-debug-sections-default--p1`: Make `--compress-debug-sections=zstd` the Linux default
- `compress-debug-sections-default--p2`: The stated motivation (shrinking `target/`) doesn't yet justify this specific fix, and if it ships at all it should apply to release builds only
- `compress-debug-sections-default--p3`: This cannot become the Linux default until mainstream distro debugging/profiling tools support zstd-compressed debug sections

Claims:
- `b-sb22-f009132-c1` · Voice: vri · Source: https://internals.rust-lang.org/t/pre-mcp-set-compressed-debug-sections-zstd-as-the-default-for-linux/20039 (`f009132`) · Date: 2023-12-17 · Locator: opening post
  - Quote: "I feel we should set --compress-debug-sections=zstd in the link args by default for linux rust targets."
  - Paraphrase: measured a hello-world project's `target/` shrinking from 4.7M to 1.5M and a modest `hyperfine`-measured build-time improvement (1.65s → 1.25s mean) with the flag enabled via `RUSTFLAGS`, and proposed defaulting it before filing a full MCP
- `b-sb22-f009132-c3` · Voice: Vorpal · Source: https://internals.rust-lang.org/t/pre-mcp-set-compressed-debug-sections-zstd-as-the-default-for-linux/20039 (`f009132`) · Date: 2023-12-24 · Locator: reply timestamped 2023-12-24T13:26:03, responding to glandium's data point that Ubuntu 22.04 LTS's gdb/binutils lack zstd support
  - Quote: "That seems like a showstopper for making this default... I don't see this going anywhere."
  - Paraphrase: many developers (including Vorpal) are required to use Ubuntu LTS or another enterprise distro at work, so shipping zstd-by-default would silently break their debugging experience until that tooling catches up
- `b-sb22-f009132-c2` · Voice: epage · Source: https://internals.rust-lang.org/t/pre-mcp-set-compressed-debug-sections-zstd-as-the-default-for-linux/20039 (`f009132`) · Date: 2023-12-18 · Locator: reply timestamped 2023-12-18T15:54:39
  - Quote: "I feel the motivation itself is lacking."
  - Paraphrase: argues the discussion should first pin down *why* `target/` is big — duplication across projects, stale files, or genuinely unused debug info — rather than reaching for compression as a default fix that would also slow down (or at least not obviously help) every debug build

## Question `consolidate-internal-network-frameworks`

When several internal Rust services need similar network-framework capabilities, should the org consolidate them into one shared framework built on existing async-ecosystem crates, or keep purpose-built frameworks separate even at the cost of overlap?

Positions:
- `consolidate-internal-network-frameworks--p1`: Reuse and consolidate on ecosystem crates
- `consolidate-internal-network-frameworks--alt1`: Keep purpose-built frameworks separate

Claims:
- `a-sa15-f005604-c1` · Voice: Ivan Nikulin · Source: https://blog.cloudflare.com/introducing-oxy (`f005604`) · Date: 2023-03-02 · Locator: "Technology choice" section
  - Quote: "We intentionally tried to stand on the shoulders of the giants with this project and avoid reinventing the wheel."
  - Paraphrase: states Oxy is deliberately built on top of existing open-source crates (hyper, tokio) rather than reinventing them, prioritizing faster iteration and battle-tested code, while contributing fixes back upstream; two of the team are now core maintainers of tokio/hyper

## Question `const-generics-unify-specializations`

When several hand-written data structures are near-duplicate specializations differing only by array length/arity (e.g. a 2-stride vs. 3-stride zip), should they be unified into one type parameterized by a const generic, or kept as separate hand-specialized versions?

Positions:
- `const-generics-unify-specializations--p1`: Unify via const generics
- `const-generics-unify-specializations--alt1`: Keep separate hand-specialized versions

Claims:
- `b-sR12-f005085-c2` · Voice: antimora (Tracel AI / burn maintainer) · Source: https://github.com/tracel-ai/burn/pull/5617 (`f005085`) · Date: 2026-09-08 · Locator: PR review comment, 2026-09-08T21:11:40Z
  - Quote: "Stepping back, `Zip3Nest` is `ZipNest` with a third stride array threaded through every line, and the two have already drifted inside this PR... A `Nest<const N: usize>` would cover both, and `CollapsedLayout` at N=1, with identical codegen since it monomorphizes. Not blocking, but the drift is already real rather than hypothetical."
  - Paraphrase: `Zip3Nest` is `ZipNest` with a third stride array threaded through, and the two have already drifted from each other inside this same PR; a `Nest<const N: usize>` would cover both with identical codegen since it monomorphizes

## Question `coupled-debug-accessor-vs-primitive`

When a runtime needs to expose a narrow debugging capability that would be most efficient as a purpose-built accessor coupled to internal layout details, should the maintainers accept that coupled accessor (even once made asymptotically efficient), or insist on a smaller, decoupled, general-purpose primitive that pushes the assembling logic (and any inefficiency) out to the caller?

Positions:
- `coupled-debug-accessor-vs-primitive--p1`: Narrow purpose built debug accessor
- `coupled-debug-accessor-vs-primitive--p2`: Skeptical of narrow internals coupled api
- `coupled-debug-accessor-vs-primitive--p3`: Prefer generic decoupled primitive

Claims:
- `b-sb16-f005000-c3` · Voice: cfallin · Source: https://github.com/bytecodealliance/wasmtime/pull/14128 (`f005000`) · Date: 2026-08-13 · Locator: comment @cfallin 2026-08-13T14:34:17Z
  - Quote: "I could see a `Func::eq` implementation making sense (because the primitive is harder to argue against -- it may be independently useful)... asymptotically better."
  - Paraphrase: argues the linear-search accessor makes a whole-store snapshot quadratic overall, and proposes instead adding `Func::eq`/`Func::hash` so the caller can build their own hashtable in a single linear pass, asymptotically better.
- `b-sb16-f005000-c2` · Voice: alexcrichton · Source: https://github.com/bytecodealliance/wasmtime/pull/14128 (`f005000`) · Date: 2026-08-13 · Locator: comment @alexcrichton 2026-08-13T13:55:31Z
  - Quote: "This is a pretty powerful debugging capability which also sort of inherently can't be efficient (e.g. the linear search here) and may also not hold up in future possible refactorings."
  - Paraphrase: questions the use case, noting the API is inherently inefficient (linear search) and may not survive future refactorings, and wants to understand whether the cost of supporting it is justified.
- `b-sb16-f005000-c1` · Voice: smarcd · Source: https://github.com/bytecodealliance/wasmtime/pull/14128 (`f005000`) · Date: 2026-08-12 · Locator: PR description @smarcd 2026-08-12T17:14:28Z
  - Quote: "Adds a host-only inverse to Instance::debug_function for debugging tools that need to serialize a same-instance funcref as a Wasm function index."
  - Paraphrase: adds `debug_function_index`, a host-only, linear-search accessor for debugging tools, deliberately scoped to guest-debugging mode only.
- `b-sb16-f005000-c6` · Voice: smarcd · Source: https://github.com/bytecodealliance/wasmtime/pull/14128 (`f005000`) · Date: 2026-08-13 · Locator: comment @smarcd 2026-08-13T16:10:07Z
  - Quote: "That's a fair concern — coupling to `VMContext`'s internal layout is more entanglement than this is worth. I dropped `debug_function_index` and pushed `Func::eq`/`Func::hash` instead, per your suggestion."
  - Paraphrase: agrees the layout coupling isn't worth it, drops `debug_function_index`, and implements `Func::eq`/`Func::hash` as pointer-identity equality instead, letting the debugger build its own index map.
- `b-sb16-f005000-c5` · Voice: cfallin · Source: https://github.com/bytecodealliance/wasmtime/pull/14128 (`f005000`) · Date: 2026-08-13 · Locator: comment @cfallin 2026-08-13T15:57:51Z
  - Quote: "I think that is still the sort of complexity that we would rather not take on if we don't have to... This is a whole lot of new functionality instead for a niche use-case."
  - Paraphrase: even with the O(1) fix, still prefers not taking on the coupling to `VMContext`'s internal layout and the added delicate logic for what is a niche use case, and again asks whether `Func::eq`/`Func::hash` plus an external algorithm could work instead.
- `b-sb16-f005000-c4` · Voice: smarcd · Source: https://github.com/bytecodealliance/wasmtime/pull/14128 (`f005000`) · Date: 2026-08-13 · Locator: comment @smarcd 2026-08-13T15:49:36Z
  - Quote: "I pushed a rewrite that makes `debug_function_index` itself O(1) instead of scanning every function."
  - Paraphrase: rewrites `debug_function_index` to be O(1) via a lazily-built, module-level cached reverse table, addressing the performance objection while keeping the original narrow accessor design.

## Question `cow-for-allocation-visibility`

When an allocation-avoiding type like `Cow<str>` would only save a negligible amount of work, should a Rust programmer still prefer it over a plain `String`, for the sake of making allocations visible in the code?

Positions:
- `cow-for-allocation-visibility--p1`: Prefer cow for allocation visibility even at negligible gain
- `cow-for-allocation-visibility--alt1`: Use a plain `String` when the gain is negligible

Claims:
- `a-sR15-f008241-c1` · Voice: gregstoll · Source: https://gregstoll.wordpress.com/2025/01/08/floating-point-to-hex-converter-now-supports-16-bit-floats-plus-i-rewrote-it-in-rust-and-webassembly (`f008241`) · Date: 2025-01-08 · Locator: section "Step 2: Adding 16-bit float support", paragraph on the `Cow<&str>` commit
  - Quote: "I really like how obvious Rust makes it when you're doing allocations and that makes me want to avoid them, even when the performance impact is minuscule."
  - Paraphrase: switched query parsing from `String` to `std::borrow::Cow<&str>`; likes that Rust makes allocations visible, which pushes them to avoid allocations even when the performance impact is minuscule
