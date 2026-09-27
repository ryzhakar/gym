## f009334 — Request: Provide an official way to deprecate a crate. NOT yank. Yank is stupid (2026-04-15, internals)

### Questions
- Q: Should crates.io/Cargo offer a dedicated "deprecate" mechanism (per-version, non-breaking) distinct from yank, rather than relying on yank or Cargo.toml maintenance badges?
  concepts: crate deprecation, yank, semver, registry metadata; domains_live: core; positions_seen: new dedicated deprecate mechanism needed; existing tools (yank for serious cases, badges.maintenance for the rest) already suffice
- Q: Should crate "maintenance status" metadata be author-declared and decayed/expired automatically over time, or purely opt-in with no forced expiry or automated notification?
  concepts: maintenance status, opt-in metadata, crate abandonment signaling; domains_live: core; positions_seen: status should auto-decay so it can't go stale; status should be opt-in only, no forced decay, no unsolicited emails

### Claims
- voice: KSXGitHub | position: new dedicated deprecate mechanism needed | date: 2026-04-15 | locator: OP | paraphrase: yank is too alarmist/breaking for this use; wants a `cargo deprecate <pkg>[@range] -m <reason>` that marks specific version ranges without forcing a break | quote: "Yank breaks things. It is also way too alarmist." | practiced_evidence: none
- voice: kornel | position: new dedicated deprecate mechanism needed, grounded in registry data | date: 2026-04-18 | locator: comment ~14 | paraphrase: from analyzing crates.io data, genuinely "done" evergreen crates are rare (roughly 10-1000 out of 100,000+ old crates); giving authors a way to affirmatively mark a crate fine helps users filter the 99% that are abandonware | quote: "if they stumble upon an old crate, it's a 99% chance that it will be some outdated abandonware" | practiced_evidence: lib.rs (kornel runs lib.rs and describes heuristics he built there to detect "done" crates)
- voice: lewis | position: existing tools (badges.maintenance in Cargo.toml) already suffice, just need better indexer support | date: 2026-04-21 | locator: comment ~19 | paraphrase: points to the existing `badges.maintenance.status` field, which lib.rs already renders, as already solving whole-crate deprecation | quote: "Isn't this what the badges.maintenance field in Cargo.toml is for?" | practiced_evidence: pros-sys crate (lewis used this field to mark his own crate deprecated)
- voice: KSXGitHub | position: new dedicated deprecate mechanism needed (rebuttal to lewis) | date: 2026-04-21 | locator: comment ~20 | paraphrase: the maintenance badge only deprecates a whole crate, not individual problematic versions, so it doesn't solve the stated problem | quote: "this badge deprecate[s] the whole crate ... we only want to deprecate some versions of a crate" | practiced_evidence: none
- voice: Ltrlg | position: existing tools (yank) already suffice for the serious case | date: 2026-04-22 | locator: comment ~21 | paraphrase: a version with a serious security vulnerability should be yanked outright, not merely soft-deprecated, since yanking is proportionate to serious risk | quote: "In this case that version really should be yanked ... If the vulnerability can be qualified as 'serious' then yanking is not 'way too alarmist'" | practiced_evidence: none
- voice: dlight | position: maintenance status should auto-decay | date: 2026-04-17 | locator: comment ~6 | paraphrase: without decay, a crate could be marked maintained once and never revisited for years while still showing as maintained | quote: "The system does not work if the information isn't up to date." | practiced_evidence: none
- voice: steffahn | position: status should be opt-in only, no forced decay or notification | date: 2026-04-17 | locator: comment ~10 | paraphrase: modeled on "last seen online" indicators — sharing status should be opt-in per crate, changeable later, and any reminder emails must be a separate, one-time opt-in per person, not automatic | quote: "the crate author could opt in to setting such status information on their crates, but they shouldn't be forced" | practiced_evidence: none

## f009654 — crates.io security incident: improperly stored session cookies (2025-04-11, project-blog)

### Nothing new
No contested Question: this is an incident disclosure with a single set of facts and remediation steps, with no Voice arguing a Position against another.

## f009657 — Faster linking times with 1.90.0 stable on Linux using the LLD linker (2025-09-01, project-blog)

### Questions
- Q: Should Rust switch its default linker on the most popular target (x86_64-unknown-linux-gnu) from the system linker to a faster non-GNU linker (lld), accepting a small risk of incompatibility?
  concepts: linker, rust-lld, compile times, target defaults; domains_live: core; positions_seen: switch the default because the speed win is large and the compatibility risk is small and escapable via a flag

### Claims
- voice: Rémy Rakic (on behalf of the compiler performance working group) | position: make rust-lld the default linker on x86_64-unknown-linux-gnu for stable releases | date: 2025-09-01 | locator: "Summary, and call for testing" section | paraphrase: after internal testing on CI, crater and nightly since May 2024 with no major issues, the team judges the ~7x incremental-link / 40% end-to-end speedup on the ripgrep benchmark worth the small risk that lld isn't bug-for-bug compatible with GNU ld, keeping an escape hatch (`-C linker-features=-lld`) | quote: "it's a drop-in replacement for the vast majority of cases, but lld is not bug-for-bug compatible with GNU ld" | practiced_evidence: rust-lang/rust (the change itself, shipped in 1.90.0, with linked benchmark results)

## f009737 — Changes to WebAssembly targets and handling undefined symbols (2026-04-04, project-blog;twir-links)

### Questions
- Q: Should Rust's WebAssembly targets treat undefined symbols as a hard link error by default (matching native platforms), even though some code intentionally relies on the current silent-import behavior?
  concepts: wasm-ld, --allow-undefined, symbol resolution, wasm_import_module; domains_live: wasm; positions_seen: remove the historical --allow-undefined default so undefined symbols become build-time errors, with an explicit opt-in (`#[link(wasm_import_module = ...)]` or `-Clink-arg=--allow-undefined`) for the rare intentional case

### Claims
- voice: Alex Crichton | position: remove --allow-undefined as the wasm-target default; undefined symbols should error at build time like on native platforms | date: 2026-04-04 | locator: "What's wrong with --allow-undefined?" section | paraphrase: the current default silently turns undefined/typo'd symbols into WebAssembly imports instead of producing a build error, which "kicks the can down the road" from where a mistake is introduced to where it surfaces (often as a confusing runtime failure); removing it aligns wasm with how all other platforms already behave, and existing intentional users can opt back in per-symbol | quote: "All native platforms consider undefined symbols to be an error by default, and thus by passing --allow-undefined rustc is introducing surprising behavior on WebAssembly targets." | practiced_evidence: rust-lang/rust#149868 (change landing in nightly, shipping with Rust 1.96 on 2026-05-28)

## f009740 — Announcing Google Summer of Code 2026 selected projects (2026-04-30, project-blog;twir-links)

### Nothing new
Purely an announcement of accepted GSoC proposals and mentors; no Voice takes a Position on a contested point.

## f009755 — Announcing a Maintainer in Residence: Scott Schafer for the Cargo team (2026-09-22, project-blog;twir-links)

### Nothing new
A funding/staffing announcement narrating a decision already made (fund a full-time Cargo maintainer via RFMF); it states history (the team's past feature freeze, funding losses) but no Voice argues a contested Position against another in this text.

## f011133 — Slint as a Rust alternative to QML for GUI development (2024-07-01, talks)

### Questions
- Q: For cross-platform desktop/embedded GUI development from Rust, should a team adopt a new compile-time-checked toolkit (Slint) over a mature, runtime-interpreted one (Qt/QML), given Slint's smaller ecosystem (missing multimedia, 3D, multi-window, automated UI testing, no iOS support yet)?
  concepts: Slint, QML, Qt, declarative UI, build-time vs runtime type checking; domains_live: desktop-cli-ui; positions_seen: adopt Slint for new Rust-based GUI work because compile-time error catching, portability and escaping Qt licensing/lock-in outweigh its current feature gaps

### Claims
- voice: David Vin (Felgo) | position: prefer Slint over QML/Qt for new Rust GUI work despite Slint's current feature gaps | date: 2024-07-01 | locator: "so should you switch to slint" (closing section, ~23:37) | paraphrase: having reimplemented an existing QML demo app in Slint from scratch, he argues Slint's build-time-checked, Rust-native, easily cross-compiled model is worth the tradeoff against QML's more mature multimedia/3D/testing tooling and Qt's licensing costs, especially for embedded targets | quote: "for me it seems that the slint is the best toolkit currently for rust" | practiced_evidence: Felgo's open-source "rusty weather app" (a from-scratch Slint reimplementation of an existing QML demo, referenced in the talk)

## f011178 — Embracing Monorepo and LLM Evolution (2024-11-18, talks; RustConf 2024)

### Questions
- Q: For hosting large monorepos, should Git object storage move off the traditional filesystem-based backend and into a distributed database (as Google Piper/Meta Sapling do), combined with decentralizing hosting itself rather than relying on a centralized host like GitHub?
  concepts: monorepo, Git internals (blob/tree/commit objects), Git LFS, decentralized hosting, GTM/P2P networking; domains_live: distributed;decentralized-iroh; positions_seen: replace file-based Git storage with a database-backed engine and decentralize the hosting layer over a P2P network, in Rust, to avoid single-vendor control and scale to monorepo sizes

### Claims
- voice: Quanyi Ma | position: rebuild Git's storage engine on a database and decentralize hosting rather than depend on a centralized host | date: 2024-11-18 | locator: ~06:14-11:22 | paraphrase: argues centralized hosts like GitHub can unilaterally access all data or use it for AI training/deletion, so his project (Mega, built in Rust) stores Git objects in a database (mirroring how Google's Piper and Meta's Sapling scale monorepos) and layers a GTM-based P2P network on top so repositories can be cloned/pushed without a single central node | quote: "being centralized ... can access all data and can take action like ... training AI or deleting projects" | practiced_evidence: Mega (open-source project on GitHub under the Web3 Infrastructure Foundation, described as already used as a backend by other projects such as Crius Pro)

## f011233 — Parallel Programming in Rust: Techniques for Blazing Speed (2025-02-26, talks)

### Questions
- Q: For GPU kernel programming from Rust, should the ecosystem invest in a community-driven Rust-native toolchain (rust-cuda) rather than continuing to write kernels in C++/CUDA with a thin Rust host layer, given CUDA's vendor lock-in and rust-cuda's current feature gaps?
  concepts: rust-cuda, CUDA, PTX, GPU kernels, vendor lock-in; domains_live: ml;other; positions_seen: back rust-cuda because it lets kernels and host code both be written in Rust and stays community- rather than vendor-controlled, versus the practical reality (raised by the audience) that almost all real GPU work today still goes through vendor C++/CUDA because non-CUDA/non-C++ tooling lags
- Q: For performance-sensitive numeric code, should Rust developers prefer the ergonomic, nightly-only `std::simd` portable-SIMD API over stable but manual target-feature-gated intrinsics?
  concepts: portable_simd, target_feature, SIMD, stable vs nightly; domains_live: core; positions_seen: use portable_simd as the default choice for its safety and ergonomics despite it being nightly-only, versus staying on stable with manually gated intrinsics and runtime feature detection

### Claims
- voice: Evgenii Seliverstov | position: rust-cuda is the right direction despite CUDA's vendor lock-in and the ecosystem's current gaps | date: 2025-02-26 | locator: ~45:52-48:54 (GPU section + audience Q&A) | paraphrase: presents Rust-CUDA (kernels and host code both in Rust, wrapping LLVM/NVVM/PTX) as the exciting alternative to writing kernels in C++/CUDA; when the audience presses on CUDA being vendor-specific and asks about AMD/other-vendor equivalents, he concedes he knows of none and that almost all real GPU work still goes through C++ kernels with a thin Rust host layer | quote: "it allows us to write kernels in Rust instead of C++ ... I'm really excited about this" | practiced_evidence: none (personal research/opinion, not a maintained crate)
- voice: Evgenii Seliverstov | position: choose lock-free/message-passing designs over mutex-based shared state only once contention is actually high; otherwise prefer plain mutexes | date: 2025-02-26 | locator: ~29:29-30:32 | paraphrase: explicit decision rule offered to the audience: if there are many threads and heavy lock contention, move to lock-free data structures (crossbeam, parking_lot); if a lock is rarely contended, a normal mutex-based structure is simpler and just as good, because lock-free implementations bring their own hazards (e.g. the ABA problem) | quote: "if you have a lot of chats and you have a lot of locks you should probably go with lock free data structures[;] if the lock is rarely acquired ... you better use the normal mutex" | practiced_evidence: none
- voice: Evgenii Seliverstov | position: portable_simd should be the default choice for SIMD code despite being nightly-only | date: 2025-02-26 | locator: ~36:39-39:43 | paraphrase: contrasts writing raw target-feature-gated intrinsics (unsafe, verbose, must be manually wrapped and feature-detected at runtime) with std::simd's portable_simd, which lets you write safe, ordinary-looking iterator code that the compiler lowers to the right instructions per architecture; recommends it as "the choice" even though it currently requires nightly | quote: "you don't need to write all the ins[truction]s ... you write the safe code not unsafe ... portable Sy[md] is the choice" | practiced_evidence: none

## f011235 — Contributing to the Rust compiler (without writing patches) (2025-06-10, talks)

### Questions
- Q: Should routine compiler-team process work (PR triage/bookkeeping, nudging reviewers, tracking regressions) be fully automated, or does it need a human doing it manually to protect contributors' limited time and avoid over-pinging them?
  concepts: PR triage, prioritization working group, contributor time, automation of process; domains_live: core; positions_seen: keep this work partly manual by deliberate choice, because full automation would risk pinging volunteer reviewers too aggressively, versus the implicit alternative (raised by the speaker himself as a question) of automating it completely

### Claims
- voice: Antonio Pirino | position: keep PR-nudging/triage bookkeeping partly manual rather than fully automating it | date: 2025-06-10 | locator: ~05:14-06:15 | paraphrase: he maintains a manual markdown bookkeeping file cross-referenced against the triage bot's oldest-PR list, and explicitly poses "why can this not be completely automated?" to himself, answering that contributors have only a finite amount of time and are "a precious asset," so a human judgment call on when to nudge a reviewer avoids over-pressuring them, even though external contributors also expect timely responses | quote: "there is one thing that is ... that I really care about ... we have on one end [a finite] amount of resources[; c]ontributors ... can allocate only a[f]inite amount of time" | practiced_evidence: none (describes his own ongoing process work, not a published tool)
