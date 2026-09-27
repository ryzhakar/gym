## f002567 — Support importing safetensors format (2025-01-20, en)

### Questions
- Q: When adding support for a new but closely related serialization format, should the implementation start as a decoupled, dedicated design or as pragmatic duplication of the existing similar format's code, refactored later?
  concepts: serialization formats, recorders, code de-duplication, API decoupling; domains_live: ml; positions_seen: dedicated-decoupled-recorder-from-the-start (antimora), duplicate-now-refactor-later (wandbrandon), reduce-duplication-before-merge (laggui)
- Q: When a user requests a new capability variant of an existing type (e.g. a byte-based recorder alongside a file-based one), should the library add a new dedicated type or extend the existing type via a configuration option?
  concepts: API surface growth, configuration options vs. new types; domains_live: ml; positions_seen: extend-via-option (antimora), new-dedicated-type-requested (ivila)

### Claims
- voice: antimora | position: dedicated-decoupled-recorder-from-the-start | date: 2025-01-27 | locator: comment @antimora 2025-01-27T22:21:47Z | paraphrase: proposes a dedicated `SafeTensorFileRecorder` independent from the PyTorch recorder, with a configurable adapter (defaulting to PyTorchAdapter), to keep formats decoupled from the start. | quote: "I suggest creating a dedicated `SafeTensorFileRecorder` to handle SafeTensor files independently from PyTorch's `.pt` files." | practiced_evidence: none
- voice: wandbrandon | position: duplicate-now-refactor-later | date: 2025-01-28 | locator: comment @wandbrandon 2025-01-28T02:40:30Z | paraphrase: copied the PyTorch recorder implementation wholesale into a new SafeTensors recorder as a base, planning cleanup later. | quote: "It's a lot of new files that are essentially copied code but with little adjustments." | practiced_evidence: none
- voice: laggui | position: reduce-duplication-before-merge | date: 2025-05-01 | locator: comment @laggui 2025-05-01T15:11:57Z | paraphrase: argues the new SafeTensors doc section is nearly identical to the PyTorch one and questions whether keeping them as two separate sections adds value. | quote: "I'm not sure if there is actual value in the current state to have two sections, where the biggest difference is the file recorder used." | practiced_evidence: none
- voice: laggui | position: reduce-duplication-before-merge | date: 2025-05-05 | locator: comment @laggui 2025-05-05T14:00:50Z | paraphrase: objects to merging a large amount of test/example duplication with the intent to fix it later, given the PR's size. | quote: "I am not in favor of introducing such a big amount of duplication just to eventually fix it (or even worse, remain unchanged for longer)..." | practiced_evidence: none
- voice: antimora | position: keep-separate-for-pragmatic-reasons | date: 2025-05-02 | locator: comment @antimora 2025-05-02T18:44:04Z | paraphrase: after an offline discussion, decided to keep PyTorch and SafeTensors doc sections separate (same format/language) rather than merge them now, calling it easier for the time being. | quote: "We discussed offline to keep two sections separate but have the same format and language between the two... For now it seems it's easier to have two." | practiced_evidence: none
- voice: antimora | position: extend-via-option | date: 2025-03-13 | locator: comment @antimora 2025-03-13T14:41:08Z, replying to @ivila's 2025-03-12T03:41:24Z request for a `SafeTensorBytesRecorder` | paraphrase: rejects adding a new recorder type for byte-based loading; proposes an argument/option on the existing recorder instead. | quote: "We don't need a new type. We can provide with an arg option." | practiced_evidence: none

## f002584 — Vim Roadmap 2025 (2025-01-22, en)

### Nothing new
Single-author roadmap post announcing planned Vim-mode work in the Zed editor; no other Voice is present and no contested point is raised.

## f002615 — Use #[instability::unstable] where possible, cleanup and improve consistency (2025-01-29, en)

### Questions
- Q: For optional, pre-1.0 dependencies whose traits a crate implements, should the crate gate the exposure behind one coarse "unstable" feature flag, behind per-dependency (or per-dependency-version) feature flags, or simply drop the integration and re-add it only if users ask?
  concepts: feature flags, semver stability, unstable attribute, optional trait impls; domains_live: embedded; positions_seen: blanket-unstable-flag (bjoernQ, initial), per-dependency-subfeature (MabezDev), just-remove-and-readd-on-demand (bjoernQ, later), need-an-explicit-policy (bugadani, jessebraham)

### Claims
- voice: bugadani | position: cfg-gate-hidden-impls-not-unstable-attribute | date: 2025-01-29 | locator: comment @bugadani 2025-01-29T12:14:24Z | paraphrase: argues private structs/functions don't need `#[instability::unstable]`; hidden impls can just be `#[cfg(feature = "unstable")]`-gated instead of documented as unstable. | quote: "We don't need to document a hidden impl, whether it's stable or not." | practiced_evidence: none
- voice: bugadani | position: per-function-not-per-block-annotation | date: 2025-01-29 | locator: comment @bugadani 2025-01-29T12:13:30Z | paraphrase: the `#[unstable]` attribute should sit on each function rather than on whole inherent impl blocks. | quote: "We shouldn't use `#[unstable]` on inherent impl blocks, the attribute should be placed on each function." | practiced_evidence: none
- voice: bjoernQ | position: blanket-unstable-flag | date: 2025-01-29 | locator: comment @bjoernQ 2025-01-29T13:13:58Z | paraphrase: the impl is marked unstable because the underlying `ufmt` dependency is still pre-1.0 (0.2.0). | quote: "I think the intention of having this unstable is that `ufmt` is 0.2.0" | practiced_evidence: none
- voice: bugadani | position: need-an-explicit-policy | date: 2025-01-29 | locator: comment @bugadani 2025-01-29T12:33:55Z | paraphrase: neither blanket-unstable nor per-dependency-version features feel right; the project needs a general policy on how to handle pre-1.0 optional trait dependencies. | quote: "Hiding every one of these behind \"unstable\" seems a bit off to me... but also a dependency+version feature... may be a bit too granular... I think we might want to come up with a policy regarding them." | practiced_evidence: none
- voice: jessebraham | position: need-an-explicit-policy | date: 2025-01-29 | locator: comment @jessebraham 2025-01-29T13:02:37Z | paraphrase: agrees the blanket-unstable approach is ham-fisted but is wary of accumulating many per-dependency-version features. | quote: "I agree that gating this all behind the `unstable` feature is probably a bit of a ham-fisted approach, however I'm also not super excited about the prospect of potentially accumulating a bunch of different versions of various dependencies..." | practiced_evidence: none
- voice: MabezDev | position: per-dependency-subfeature | date: 2025-01-29 | locator: comment @MabezDev 2025-01-29T15:44:45Z | paraphrase: proposes expanding the "unstable" feature into named sub-features like `unstable-ufmt` per dependency. | quote: "One option is to expand the `unstable` feature to have `unstable-ufmt` etc... maybe for dependencies it makes sense?" | practiced_evidence: none
- voice: bjoernQ | position: just-remove-and-readd-on-demand | date: 2025-01-30 | locator: comment @bjoernQ 2025-01-30T10:14:28Z | paraphrase: argues it's simpler to just remove optional integrations (as was done for embedded-hal-nb) and re-add them later if users complain, rather than design feature-flag machinery. | quote: "we spend more time talking/thinking about it than it would take to remove and re-add it" | practiced_evidence: none
- voice: bugadani | position: need-an-explicit-policy | date: 2025-01-30 | locator: comment @bugadani 2025-01-30T10:24:54Z | paraphrase: pushes back that ufmt is not the only such dependency (rand-core, embassy-embedded-hal, log, etc.), so ad hoc removal doesn't resolve the underlying question of what to do with unstable optional dependencies generally. | quote: "My point is, we need to figure out these dependencies, and what we do with them. We can remove a specific example, but the issue doesn't go away just from that." | practiced_evidence: none

## f002719 — Binary patching rust hot-reloading, sub-second rebuilds, independent server/client hot-reload (2025-02-25, en)

### Questions
- Q: To shorten the Rust edit-compile-run loop, should tooling pursue binary/process-level hot-patching (skip rebuilding and relinking) or faster full-rebuild codegen (e.g. an alternate codegen backend)?
  concepts: compile times, hot-patching, dynamic linking, codegen backend; domains_live: desktop-cli-ui, frontend, wasm; positions_seen: binary-hot-patching (jkelleyrtp, dx/subsecond), faster-codegen-backend (DrewRidley, cranelift)

### Claims
- voice: jkelleyrtp | position: binary-hot-patching-plus-dynamic-linking | date: 2025-03-18 | locator: comment @jkelleyrtp 2025-03-18T21:13:39Z | paraphrase: describes "zerolink"/"thinlink", an approach that automatically dynamically links workspace crates against a cached dependencies dylib to speed up builds, alongside the subsecond hot-patching mechanism. | quote: "our new approach for drastically speeding up rust compile times by automatically using dynamic linking" | practiced_evidence: https://github.com/DioxusLabs/dioxus/pull/3797
- voice: DrewRidley | position: faster-codegen-backend | date: 2025-03-19 | locator: comment @DrewRidley 2025-03-19T19:41:13Z | paraphrase: suggests adding the cranelift codegen backend as an optional flag for hot-reload builds, reporting it roughly halved build times on their machine (600ms to 300ms). | quote: "I found on my M3 Pro Macbook it brings down the average times from ~600ms to ~300ms." | practiced_evidence: none
- voice: jkelleyrtp | position: binary-hot-patching-plus-dynamic-linking | date: 2025-03-19 | locator: comment @jkelleyrtp 2025-03-19T20:56:59Z | paraphrase: reports profiling showed 100-300ms of a ~500ms build spent copying incremental artifacts to disk, and points to an upstream rustc PR aiming to remove that cost, wanting it to reach "blink and you miss it" hotpatch speed. | quote: "I did some profiling of rustc and about 100-300ms is spent copying incremental artifacts on disk." | practiced_evidence: none

## f002755 — Introducing Qdrant Cloud's New Enterprise-Ready Vector Search (2025-03-04, en)

### Nothing new
Vendor product-announcement post about Qdrant Cloud's enterprise features (RBAC, SSO, monitoring); not about Rust and raises no contested point among Rust practitioners.

## f002775 — Rust on Cortex-R52 (2025-03-10, en)

### Nothing new
Single-voice company announcement (Ferrous Systems) of newly published open-source Rust support libraries for Arm Cortex-R52; no disagreement or decision point is present.

## f002827 — Vibe Coding RAG with our MCP server (2025-03-21, en)

### Nothing new
Vendor webinar recap about using AI coding assistants (Cursor, Copilot, Aider, Claude Code) with a Qdrant MCP server to build a Python/JS RAG demo; not about Rust and raises no contested point among Rust practitioners.

## f002937 — Wasmtime LTS Releases (2025-04-22, en)

### Nothing new
Single-voice (Alex Crichton) announcement of Wasmtime's new LTS release policy; states a policy without an opposing view present in the source.

## f003030 — Define configs in YAML files (2025-05-20, en)

### Questions
- Q: When an internal Rust tool's config needs a data type (i128) that mainstream serialization-format libraries in the ecosystem don't support well, should the project pick the ecosystem-conventional format anyway and patch around the gap, narrow the type requirement to fit an existing format, or invent a custom config format?
  concepts: serialization formats, i128 support, config DSLs, ecosystem conventions; domains_live: embedded; positions_seen: prefer-toml-for-consistency (okhsunrog), yaml-is-more-convenient (bjoernQ), patch-the-yaml-library (bugadani), narrow-to-i64-and-ship (bjoernQ, actual PR change), custom-config-language-considered-and-rejected-as-too-costly (bjoernQ), ship-now-switch-format-later (MabezDev)
- Q: Should conditional configuration logic be expressed as independent boolean-predicate rules whose interaction is implicit, or as an ordered list of rules where the first matching condition wins?
  concepts: config DSL semantics, conditional evaluation, ordering; domains_live: embedded; positions_seen: independent-predicate-functions (bjoernQ, initial design, later found buggy), ordered-first-match-wins (bugadani)

### Claims
- voice: okhsunrog | position: prefer-toml-for-consistency | date: 2025-05-24 | locator: comment @okhsunrog 2025-05-24T17:23:55Z | paraphrase: questions why the PR uses YAML instead of TOML, for consistency with the Rust ecosystem. | quote: "Why not toml, to be consistent with the Rust ecosystem?" | practiced_evidence: none
- voice: bjoernQ | position: yaml-is-more-convenient | date: 2025-05-24 | locator: comment @bjoernQ 2025-05-24T17:33:48Z | paraphrase: finds TOML's representation inconvenient for this use case and considers YAML the nicest representation available. | quote: "the toml representation is ... Quite inconvenient - IMHO yaml is the nicest representation here" | practiced_evidence: none
- voice: bugadani | position: patch-the-yaml-library | date: 2025-06-04 | locator: comment @bugadani 2025-06-04T15:24:04Z | paraphrase: would rather add i128 support to whichever YAML library is chosen than change the config's type range, and flags serde_yml as likely unmaintained. | quote: "I'd still prefer adding i128 support to whatever yaml library we pick - which probably shouldn't be serde_yml as it looks quite unmaintained." | practiced_evidence: none
- voice: bugadani | position: patch-the-yaml-library | date: 2025-06-04 | locator: comment @bugadani 2025-06-04T15:39:12Z | paraphrase: suggests trying the facet-yaml crate as a better-maintained alternative. | quote: "I'd probably give https://crates.io/crates/facet-yaml a try" | practiced_evidence: none
- voice: bjoernQ | position: custom-config-language-considered-and-rejected-as-too-costly | date: 2025-06-05 | locator: comment @bjoernQ 2025-06-05T11:30:38Z | paraphrase: after evaluating serde_yml, serde_yaml and facet-yaml, concludes YAML tooling in the Rust ecosystem is a dead end for i128 support, floats designing a custom config language, but judges it too much effort to "just try it". | quote: "So YAML doesn't seem to be a good way forward... Maybe defining our own config-language would be an alternative - but probalby too much effort to \"just try it\"" | practiced_evidence: none
- voice: bugadani | position: patch-the-yaml-library | date: 2025-06-05 | locator: comment @bugadani 2025-06-05T11:43:25Z | paraphrase: pushes back that the YAML spec doesn't forbid wider integers, questioning bjoernQ's pessimism about the format. | quote: "I get that the spec doesn't _mandate_ support for wider integers but it also doesn't forbid them, so why this sudden negativity?" | practiced_evidence: none
- voice: MabezDev | position: ship-now-switch-format-later | date: 2025-06-10 | locator: comment @MabezDev 2025-06-10T09:48:30Z | paraphrase: since the format is currently internal-only, proposes proceeding with YAML plus workarounds now and switching library or format later if something better appears. | quote: "this is strictly \"internal\" right now, so we can proceed with yaml + some work arounds, then if a better library, or a more appropriate format shows up we can switch to it." | practiced_evidence: none
- voice: bugadani | position: ordered-first-match-wins | date: 2025-06-11 | locator: comment @bugadani 2025-06-11T07:49:35Z | paraphrase: after bjoernQ's predicate-function design produced a real bug (two mutually exclusive conditions both false), proposes redesigning the conditional rules as an ordered list evaluated first-match-wins. | quote: "What if we turned this into a match-style \"first condition wins\" situation?" | practiced_evidence: none

## f003036 — Apply release plan (2025-05-21, en)

### Questions
- Q: For a CLI flag guarding a destructive action where the safe default is dry-run, should the flag's naming prioritize brevity/typing convenience (default-on dry-run, `--no-dry-run` to opt out) or consistency with how sibling commands in the same tool name their flags?
  concepts: CLI ergonomics, flag naming, tooling consistency; domains_live: embedded, core; positions_seen: convenience-over-consistency (bugadani), consistency-across-commands (MabezDev)

### Claims
- voice: MabezDev | position: consistency-across-commands | date: 2025-05-21 | locator: comment @MabezDev 2025-05-21T14:11:47Z | paraphrase: argues the new command should use `--no-dry-run` like every other command in the tool, for consistency. | quote: "Everywhere else we've use the `--no-dry-run`, I think we should be consistent." | practiced_evidence: none
- voice: bugadani | position: convenience-over-consistency | date: 2025-05-21 | locator: comment @bugadani 2025-05-21T14:48:33Z | paraphrase: reasons that getting this particular flag wrong isn't dangerous, and `--no-dry-run` is annoying enough to type that a different default might be worth it, though agrees to change it if asked. | quote: "my thinking was that this isn't actually dangerous to get wrong, but --no-dry-run is sufficiently annoying to type. I can change it, we'll hate it" | practiced_evidence: none

## f003044 — Trying `subsecond` and: `Ignoring hotpatch since there is no ASLR reference`. What does it mean? (2025-05-25, en)

### Nothing new
Bug-reproduction and troubleshooting thread for the experimental `subsecond` hot-patching library (alpha, async functions not patching correctly, later found to need `HotFn::current`/sync wrapper); documents an implementation limitation but no competing Position among practitioners on how the feature should be designed.

## f003052 — x64: Convert `compare` instructions to the new assembler (2025-05-27, en)

### Questions
- Q: When migrating a compiler backend to a new, more systematic instruction-assembler abstraction, and an instruction needs special-cased handling (e.g. custom flag-setting/printing) that the new abstraction doesn't yet cleanly support, should the PR merge the ad hoc special case now or block on designing the general mechanism first?
  concepts: compiler backend migration, instruction encoding abstraction, technical debt sequencing; domains_live: wasm, core; positions_seen: resist-ad-hoc-design-general-solution-first (abrown, initial), merge-as-is-and-refactor-later (abrown, revised; rahulchaphalkar)

### Claims
- voice: abrown | position: resist-ad-hoc-design-general-solution-first | date: 2025-05-28 | locator: comment @abrown 2025-05-28T17:56:16Z | paraphrase: objects to adding another special-cased "custom" printing mechanism for compare instructions' flags, noting the existing `lock_` special case was already unfortunate, and argues for a better long-term solution before merging. | quote: "I'm not a big fan of this; the `lock_` stuff below already seemed unfortunate but now this opens a whole new can of worms... I just think we should think through a better long-term solution." | practiced_evidence: none
- voice: abrown | position: merge-as-is-and-refactor-later | date: 2025-06-02 | locator: comment @abrown 2025-06-02T17:48:01Z | paraphrase: shifts to accepting the current approach for now, deferring the cleanup to a follow-up refactor building on a separate "custom" logic PR by another contributor. | quote: "Ok, let's leave this as-is for now but we'll need to refactor to something more like the `custom` logic introduced by @alexcrichton..." | practiced_evidence: none
- voice: rahulchaphalkar | position: merge-as-is-and-refactor-later | date: 2025-06-03 | locator: comment @rahulchaphalkar 2025-06-03T16:18:30Z | paraphrase: agrees to sequence the work by letting the external-printing refactor PR land first and rebasing this PR on top of it, rather than blocking this PR on redesigning the mechanism inline. | quote: "I agree with the idea that lets push the external printing patch first, and then rebase on that." | practiced_evidence: none
