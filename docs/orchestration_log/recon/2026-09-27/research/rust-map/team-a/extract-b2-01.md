Framing: For each source, where do competent Rust practitioners disagree?

## f000095 — The Anachro Book (unknown, en)
### Nothing new
reason-code: off-subject
reason: Documents the Anachro network protocol and PC hardware architecture (planes, layers, backplane pinouts, card modules); it is a hardware/protocol specification, not a decision about Rust the language or its practice.

## f000098 — WASM It (unknown, en)
### Nothing new
reason-code: no-decision
reason: Talk reports concrete native-vs-WASM platform differences the author hit in the Amethyst engine (event loops, thread pools, config sources, shader linkage, audio buffers, networking) as diagnosed constraints of each runtime, not an argued decision on how Rust code should be written.

## f000176 — Bevy Book (unknown (living document), en)
### Questions
- Q: When maintaining a widely-depended-on crate, should its Minimum Supported Rust Version policy track the latest stable Rust release, or pin to an older stable version for broader downstream compatibility?
  concepts: MSRV, Cargo, toolchain policy, breaking-change cadence; domains_live: desktop-cli-ui; positions_seen: track-latest-stable-MSRV (Bevy)
- Q: For a project chasing faster iterative compiles, should it adopt nightly-only compiler features (the Cranelift codegen backend, generic sharing) for dev builds despite their immaturity, or stay entirely on stable Rust with the LLVM backend?
  concepts: nightly Rust, Cranelift codegen backend, generic sharing, compile times; domains_live: desktop-cli-ui, wasm; positions_seen: nightly-cranelift-for-dev-llvm-for-ship (Bevy)
- Q: Should a Rust crate or plugin default to convenience dependencies and default features, or aim for a small crate size (opt-in features, default-features = false) to control downstream compile times?
  concepts: Cargo features, default-features, dependency bloat, compile times; domains_live: core; positions_seen: minimize-deps-and-default-features (Bevy)
- Q: Should a Rust project's build configuration replace the platform's default linker with a faster alternative (lld or Mold) to cut link times, accepting Mold's narrower platform support and stability caveats?
  concepts: linker, lld, Mold, link time, build configuration; domains_live: core; positions_seen: switch-to-alt-linker-for-speed (Bevy)
### Claims
- voice: Bevy | connection: official documentation ("the Bevy Book") of the Bevy game engine crate (crates.io: `bevy`), a widely-depended-on Rust game engine | position: track-latest-stable-MSRV | date: unknown (living document, no publish/version date given) | locator: "Setup" chapter, "Ensuring Rust Is Up To Date" section | paraphrase: States Bevy's Minimum Supported Rust Version is "the latest stable release" of Rust, reasoning that Bevy relies heavily on ongoing improvements in the language and compiler. | quote: "Bevy relies heavily on improvements in the Rust language and compiler." | practiced_evidence: none | flag: voice-unverified
- voice: Bevy | connection: official documentation of the Bevy game engine crate | position: nightly-cranelift-for-dev-llvm-for-ship | date: unknown (living document, no publish/version date given) | locator: "Setup" chapter, "Enable Fast Compiles" → "Cranelift" section | paraphrase: Recommends the nightly-only Cranelift codegen backend for faster iterative dev builds (about 30% faster than LLVM), while noting it is still immature — Wasm builds don't work, MacOS builds can crash — and that a shipped build should still use LLVM. | quote: "When shipping your game, you should still compile it with LLVM." | practiced_evidence: none | flag: voice-unverified
- voice: Bevy | connection: official documentation of the Bevy game engine crate | position: minimize-deps-and-default-features | date: unknown (living document, no publish/version date given) | locator: "Building Bevy's Ecosystem" chapter, "Small Crate Size" section | paraphrase: Advises third-party plugin authors to keep crate size small — disable default features, avoid large new dependencies, gate optional functionality behind Cargo features — specifically to avoid long build times for the plugin and for projects depending on it. | quote: "To avoid long build times in your plugin (and in projects using it), you should aim for a small crate size: Only include the Bevy features you absolutely need." | practiced_evidence: none | flag: voice-unverified
- voice: Bevy | connection: official documentation of the Bevy game engine crate | position: switch-to-alt-linker-for-speed | date: unknown (living document, no publish/version date given) | locator: "Setup" chapter, "Enable Fast Compiles" → "Alternative Linkers" section | paraphrase: Recommends replacing the default Rust linker with lld, or Mold for even more speed, to cut the compiler's link-step time, while naming Mold's tradeoff directly against the default it replaces. | quote: "Mold is up to 5× (five times!) faster than LLD, but with a few caveats like limited platform support and occasional stability issues." | practiced_evidence: none | flag: voice-unverified

## f000182 — Tealdeer User Manual (unknown (living document), en)
### Nothing new
reason-code: off-subject
reason: User manual for the tldr-in-Rust CLI tool covers installation methods, command-line flags and TOML configuration sections; it contains no decision about Rust language or practice, only end-user usage of the compiled tool.

## f000202 — Rust GPU Dev Guide (unknown (living document), en)
### Questions
- Q: Once an experimental compiler-backend feature (here, the SPIR-T shader IR framework in rust-gpu's linker) has matured, should the project keep it behind a togglable flag indefinitely, or drop the escape hatch and make it mandatory to cut ongoing maintenance and testing cost?
  concepts: compiler backend design, feature flags, intermediate representations, maintenance cost vs. configurability; domains_live: other; positions_seen: make-mandatory-drop-toggle (rust-gpu project / EmbarkStudios)
### Claims
- voice: rust-gpu project (EmbarkStudios) | connection: maintainers' own dev guide for the rust-gpu compiler backend crate (rustc_codegen_spirv), which compiles Rust to SPIR-V GPU shaders | position: make-mandatory-drop-toggle | date: unknown (living document, no publish/version date given) | locator: "'Codegen args'" chapter, "--spirt (until 0.6.0)" / "--no-spirt (0.6.0 and 0.7.0)" entries | paraphrase: States that as of rust-gpu 0.8.0 the SPIR-T shader IR framework is always used and the earlier --spirt/--no-spirt toggle has been removed, reasoning that keeping it configurable would add ongoing cost to maintenance, testing and further feature development. | quote: "as of rust-gpu 0.8.0, SPIR-🇹 is always being used and cannot be disabled (to reduce the cost of maintenance, testing and further feature development)." | practiced_evidence: none | flag: voice-unverified
