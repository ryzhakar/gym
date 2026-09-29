## f000258 — wasm-pack docs (unknown (living document), en)

### Questions
- Q: Should a wasm-bindgen crate use `wee_alloc` as its global allocator to shrink code size?
  concepts: wee_alloc, global allocator, code size, WebAssembly; domains_live: wasm, frontend; positions_seen: default to Rust's standard global allocator, keep wee_alloc opt-in
- Q: Should a wasm-bindgen project install a custom panic hook for browser-readable panic messages?
  concepts: console_error_panic_hook, panic messages, debugging; domains_live: wasm, frontend; positions_seen: enable console_error_panic_hook by default (zero cost when unused)

### Claims
- voice: wasm-pack | connection: official documentation/tool of the rust-wasm group, the Rust→WebAssembly packaging tool | position: leave the standard global allocator as default, keep wee_alloc opt-in | date: 2026-09-28 | locator: § wee_alloc | paraphrase: the project template ships with the wee_alloc feature present but not enabled by default (only console_error_panic_hook is default-on), because wee_alloc "trades off size for speed" and "is not competitive in terms of performance with the default global allocator." | quote: "wee_alloc trades off size for speed. It has a tiny code-size footprint, but it is not competitive in terms of performance with the default global allocator" | practiced_evidence: none | flag: voice-unverified
- voice: wasm-pack | connection: official documentation/tool of the rust-wasm group | position: enable console_error_panic_hook by default | date: 2026-09-28 | locator: § src/utils.rs / What is console_error_panic_hook? | paraphrase: the project template enables the console_error_panic_hook feature by default because it turns an opaque "RuntimeError: Unreachable executed" browser error into the real Rust panic message, and costs nothing when the feature is off since the hook function inlines to empty. | quote: "there is no run-time performance or code-size penalty incurred by its use" | practiced_evidence: none | flag: voice-unverified

## f000516 — Model Wishlist (2023-10-25, en)

### Nothing new
reason-code: off-subject
reason: A candle (Rust ML crate) GitHub issue tracking which pretrained ML models the community wants ported to the library; the whole thread is a running vote/list of model requests (musicgen, JinaBert, Marian-MT, Stable Diffusion LCM, StyleTTS2, etc.) and claim-staking comments, with no decision about Rust language or ecosystem practice.

## f001122 — `embedded-test` integration (2024-03-14, en)

### Questions
- Q: Should embedded on-target test execution be a separate CLI command from normal flashing-and-running, or unified via runtime autodetection?
  concepts: probe-rs test, probe-rs run, autodetection, CLI design; domains_live: embedded; positions_seen: unify via ELF autodetection, replacing a separate `probe-rs test` subcommand
- Q: Should Rust embedded on-target testing be built on the existing defmt-test framework, or a new one?
  concepts: embedded-test, defmt-test, riscv, async tests; domains_live: embedded; positions_seen: author a new framework (embedded-test) instead of extending defmt-test, to gain riscv and async test-function support

### Claims
- voice: t-moe | connection: probe-rs contributor, author of this PR integrating embedded-test into probe-rs (a Rust embedded debug/flash tool) | position: unify test and run execution via ELF autodetection, retiring the separate `probe-rs test` subcommand | date: 2024-03-14 | locator: PR #2292 top comment | paraphrase: rewrote the test-integration branch so `probe-rs run` autodetects whether the ELF is a test binary (via an embedded-test linker symbol) and behaves accordingly, replacing the previous design of a distinct `probe-rs test` subcommand. | quote: "`probe-rs run` will now autodetect whether it is a test binary or a normal binary. You no longer need `probe-rs test`" | practiced_evidence: https://github.com/probe-rs/probe-rs/pull/2292 | flag: voice-unverified
- voice: t-moe | connection: probe-rs contributor, author of embedded-test | position: author embedded-test rather than extend defmt-test | date: 2024-03-21 | locator: PR #2292 comment, 2024-03-21T09:35:25Z | paraphrase: explains embedded-test was created because defmt-test did not support RISC-V targets or async test functions, choosing to build a new on-target test framework rather than extend the existing one. | quote: "I've created embedded-test because defmt-test did not support riscv or async test functions." | practiced_evidence: https://github.com/probe-rs/embedded-test | flag: voice-unverified
