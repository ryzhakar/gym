## f005676 — IronClaw (Agent OS README) (2026-02-13, en)
### Questions
- Q: When rewriting an existing agent/runtime project (originally TypeScript), should the rewrite target Rust for native performance, memory safety and single-binary distribution, or stay on a managed-runtime language for lower rewrite cost?
  concepts: rewrite-in-rust, memory safety, single binary, native performance; domains_live: other; positions_seen: rust-over-typescript-for-rewrite
- Q: For sandboxing untrusted tool/plugin code inside a Rust agent runtime, should isolation be built on a WASM sandbox with capability-based permissions, or on Docker-style OS containers?
  concepts: WASM sandbox, capability-based security, Docker, process isolation; domains_live: wasm;other; positions_seen: wasm-sandbox-over-docker-for-untrusted-tools
### Claims
- voice: IronClaw (nearai/ironclaw project) | connection: the project's own README, a Rust project installed via `cargo install --locked --path crates/app/ironclaw_cli` | position: rust-over-typescript-for-rewrite | date: 2026-02-13 | locator: § OpenClaw Heritage (Key differences) | paraphrase: States its rewrite from the TypeScript-based OpenClaw chose Rust specifically for native performance, memory safety, and shipping as a single binary, in contrast to the original's TypeScript runtime. | quote: "Rust vs TypeScript - Native performance, memory safety, single binary" | practiced_evidence: https://github.com/nearai/ironclaw | flag: voice-unverified
- voice: IronClaw (nearai/ironclaw project) | connection: the project's own README | position: wasm-sandbox-over-docker-for-untrusted-tools | date: 2026-02-13 | locator: § OpenClaw Heritage (Key differences); § Security (WASM Sandbox) | paraphrase: Runs untrusted, dynamically-built tools inside WASM containers with capability-based, opt-in permissions instead of Docker-style isolation, reserving Docker for a separate, heavier orchestrator/worker tier; justifies the WASM choice as lighter-weight. | quote: "WASM sandbox vs Docker - Lightweight, capability-based security" | practiced_evidence: https://github.com/nearai/ironclaw | flag: voice-unverified

## f005692 — A fully snapshotable Wasm interpreter (2026-03-11, en)
### Questions
- Q: For time-travel debugging of a Rust-hosted Wasm interpreter, should state be snapshotted at every single instruction for exact rollback, or at exponentially-spaced intervals to bound memory use on long-running programs?
  concepts: time-travel debugging, wasm interpreter, snapshot/restore, exponential decay history; domains_live: wasm; positions_seen: exponential-decay-snapshotting-over-per-instruction
### Claims
- voice: matthewkim | connection: author of the gabagool Rust Wasm interpreter under discussion, links own repo and code throughout the thread | position: exponential-decay-snapshotting-over-per-instruction | date: 2026-03-16 | locator: lobste.rs thread eu5uiz, comment 2026-03-16T07:57:28 | paraphrase: Moves off an initially-considered naive per-instruction snapshot strategy (exact rollback but memory-hungry) toward an exponential-decay snapshot buffer, after a commenter's pointer to "decaying histories," because it gives good general-purpose asymptotic memory behavior for long-lived programs; starts building a debugger on top of it. | quote: "the exponential decay buffer was such a cool topic, I decided to write about it" | practiced_evidence: https://github.com/friendlymatthew/gabagool | flag: voice-unverified

## f005733 — PathString::slice dangling reference UB - add Miri to CI (2026-05-15, en)
### Questions
- Q: When porting a large, unsafe-heavy systems codebase from another language (e.g. Zig) to Rust, should the first pass aim for a fast, mechanical 1:1 structural port that accepts temporary soundness debt to be hardened afterward, or an incremental, test-verified rewrite done component by component?
  concepts: rewrite-in-rust, unsafe, soundness, incremental migration, Miri; domains_live: core;other; positions_seen: fast-1to1-port-then-harden
- Q: When a Rust type wraps a raw pointer to data it does not own, must it carry a `PhantomData`-tracked lifetime (and note whether it needs exclusive access) to stay sound, even though the raw pointer itself carries no lifetime?
  concepts: raw pointers, lifetimes, PhantomData, provenance, unsafe, aliasing; domains_live: core; positions_seen: raw-ptr-wrapper-needs-phantom-lifetime
- Q: Should every use of `unsafe` in a Rust codebase be closely reviewed by someone experienced with Rust before merging, and should porting from a language with different memory-management semantics (e.g. Zig) avoid mechanical 1:1 translation of its patterns?
  concepts: unsafe review, memory-management semantics, undefined behavior, code review process; domains_live: core; positions_seen: review-all-unsafe-no-1to1-mechanical-port
### Claims
- voice: Jarred-Sumner | connection: owns/leads the Bun project and directed its Rust port, commenting on his own repository's issue | position: fast-1to1-port-then-harden | date: 2026-05-16 | locator: issue #30719, comment 2026-05-16T04:59:27Z | paraphrase: Defends the Rust port's current state as an intentional first phase that mirrors the original Zig code 1:1 as its "starting point," with soundness and idiom improvements ("making it better") to follow, rather than treating the initial port as production-ready or fully reviewed. | quote: "the Rust port is intended to be as close as possible to a 1:1 mapping of the original Zig code - which is the starting point. We are making it better." | practiced_evidence: https://github.com/oven-sh/bun | flag: voice-unverified
- voice: TehPers | connection: walks through a concrete Rust fix (adding a `PhantomData<&'a [u8]>` marker field) for the reported unsound type, demonstrating hands-on command of Rust's lifetime/aliasing model | position: raw-ptr-wrapper-needs-phantom-lifetime | date: 2026-05-15 | locator: issue #30719, comment 2026-05-15T04:46:26Z | paraphrase: Argues that a type holding a raw pointer to borrowed data must explicitly track that data's lifetime (and whether it needs exclusive access) via `PhantomData`, rather than letting the pointer silently carry no lifetime information, because skipping this is exactly what produces use-after-free/aliasing UB like the reported bug. | quote: "If a type holds a pointer to some data that it does not own, it *must* track the lifetime of that data." | practiced_evidence: none | flag: voice-unverified
- voice: JavaDerg | connection: walks through the codebase's actual pointer/lifetime-erasure mechanics line by line (linking the exact source lines) to explain why the bug is unsound | position: review-all-unsafe-no-1to1-mechanical-port | date: 2026-05-14 | locator: issue #30719, comment 2026-05-14T18:53:38Z | paraphrase: Argues every `unsafe` usage in the codebase needs proper review, and that Rust is not suited to a straight 1:1 translation from a language with a different memory-management scheme (here, Zig), because doing so reintroduces use-after-free and invalid-aliasing bugs that Rust's model is supposed to rule out. | quote: "It is highly adviced that every usage of unsafe is properly reviewed in the codebase. Rust is not suited for a 1:1 translation from other languages with different memory managment schemes." | practiced_evidence: none | flag: voice-unverified

## f005755 — Kyde (a fast native commit and diff code editor) (2026-06-22, en)
### Nothing new
reason-code: no-rust-voice
reason: The README's sole voice, the project's author, explicitly disclaims any Rust connection ("I don't know Rust"), so the project's stack choices (gpui, shelling out to `git`, no libgit2) cannot be logged as a Rust practitioner's Claim even though the README states them.

## f005840 — Embedded Rust in Production ..? (2024-02-07, en)
### Questions
- Q: For a new embedded-firmware project, should you choose Rust over C given Rust's steeper learning curve and a smaller hiring pool, trading upfront cost for far fewer runtime bugs and debugging time in production?
  concepts: embedded Rust, ESP32, memory safety, hiring/training cost, reliability; domains_live: embedded; positions_seen: rust-over-c-for-embedded-despite-hiring-cost
### Claims
- voice: Michael Lohr | connection: led an embedded Rust rewrite (ESP32/ESP-IDF, no_std/std) run in production for over a year at STABL Energy | position: rust-over-c-for-embedded-despite-hiring-cost | date: 2024-02-07 | locator: post body, closing paragraph | paraphrase: After a year-plus running a Rust ESP32 rewrite of a previously unreliable C implementation in production with effectively zero known bugs, states that given the same choice again he would pick Rust over C for embedded work, despite Rust taking longer to write and being harder to hire/train for than C. | quote: "If, in the future, I were faced with a choice between C and Rust for embedded development again, I would most likely choose Rust because of how successfully we used it in the past." | practiced_evidence: none (STABL Energy's firmware repository is not linked) | flag: voice-unverified

## f005842 — What part of Rust compilation is the bottleneck? (2024-03-20, en)
### Questions
- Q: When deciding where to invest effort speeding up Rust builds, should the Rust project prioritize frontend (type-checking/borrow-checking) throughput, or backend/linker (codegen and linking) throughput?
  concepts: rustc compilation pipeline, frontend/backend/linker, incremental compilation, Cranelift, linker choice (lld/mold); domains_live: core; positions_seen: prioritize-backend-linker-over-frontend
### Claims
- voice: kobzol | connection: built the compilation-breakdown visualization for the official rustc benchmark suite and authors the `cargo-wizard` tool, self-described rustc-perf contributor | position: prioritize-backend-linker-over-frontend | date: 2024-03-20 | locator: post body, § "Which artifact type is more important?" | paraphrase: Based on measured frontend/backend/linker splits across ripgrep and ~90 library crates, argues the interactive edit-build-run cycle (which is dominated by compiling linkable binary/test artifacts, not libraries) is the real developer-experience bottleneck, and that backend codegen and linking (e.g. a Cranelift backend, defaulting to `lld`) are therefore the parts most worth improving, over frontend (type/borrow-checking) work. | quote: "I personally consider the interactive edit-build-run cycle to be the biggest bottleneck when developing Rust code... That is also why I think that the backend and the linker are the things that could be improved the most." | practiced_evidence: https://github.com/rust-lang/rustc-perf | flag: voice-unverified

## f006880 — Just a simple Nix Flake for Rust and WASM (2024-04-05, en)
### Nothing new
reason-code: no-decision
reason: A single-file Nix flake recipe for building a Rust `wasm32-unknown-unknown` crate, shared as a working solution with no reasoned decision against a named alternative approach.

## f007606 — Improving Node.js with Rust-Wasm Library (2023-10-25, en)
### Nothing new
reason-code: no-decision
reason: A wasm-bindgen tutorial benchmarking a Rust/Wasm Fibonacci implementation against a naive pure-JavaScript one; it reports a speed result but states no reasoned decision against a real competing Rust-ecosystem alternative (e.g. native N-API addons).

## f007802 — ESP Embedded Rust: Command Line Interface (2024-02-28, en)
### Questions
- Q: Among several similarly-featured `no_std` CLI crates for embedded Rust (e.g. `terminal-cli`, `embedded-cli`, `light-cli`, `menu`), should download/popularity count be the deciding factor when none stands out on features alone?
  concepts: no_std, embedded CLI crates, crate selection, crates.io downloads; domains_live: embedded; positions_seen: pick-by-popularity-among-similar-crates
### Claims
- voice: Omar Hiari | connection: self-described "Rustacean," embedded engineer authoring an embedded-Rust blog series (esp_idf_hal/esp32 code throughout) | position: pick-by-popularity-among-similar-crates | date: 2024-02-28 | locator: post body, Introduction | paraphrase: Surveyed several `no_std` CLI crates (`terminal-cli`, `embedded-cli`, `light-cli`, `menu`) and, finding them all similarly well-abstracted and feature-complete, picked `menu` specifically because it had the most downloads. | quote: "I ended up going for menu based on the number of downloads since it seemed to be the most popular." | practiced_evidence: https://github.com/apollolabsdev/ESP32C3 | flag: voice-unverified

## f007844 — Embedded Rust Bluetooth on ESP: BLE Server (2024-03-27, en)
### Nothing new
reason-code: no-decision
reason: A tutorial building a BLE GATT server with the esp32-nimble crate; the one comment touching a design tradeoff (NimBLE's footprint vs. bluedroid) is offered as an untested guess ("my understanding is...so I figure"), not a declared decision.

## f007972 — What is a CIDR trie and how can it help you? (2024-06-26, en)
### Questions
- Q: When a trie node's children have a small, fixed, known branching factor (e.g. 2, for a binary/CIDR trie), should the node store them in a fixed-size array, or in a growable collection like `Vec` or `HashMap`?
  concepts: trie, fixed-size array, Vec, HashMap, allocation avoidance; domains_live: core; positions_seen: fixed-array-over-vec-for-known-branching-factor
- Q: For a small, well-understood data-structure need inside a Rust project, should you write a minimal purpose-built implementation yourself, or pull in a general-purpose crate (e.g. `trie_rs`) that already covers the general case?
  concepts: dependency hygiene, crate maintenance cost, minimalism, supply-chain risk; domains_live: core; positions_seen: roll-your-own-over-dependency-for-simple-cases
### Claims
- voice: Sven Kanoldt | connection: author of a "practical rust bites" blog series, writes and explains the Rust CIDR-trie implementation himself, links own GitHub/dev.to | position: fixed-array-over-vec-for-known-branching-factor | date: 2024-06-26 | locator: post body, § Implementation | paraphrase: For a binary CIDR trie's child pointers, chooses a fixed-size `[Option<Box<Node>>; 2]` array over a `Vec`, explicitly to avoid extra allocations on insert; notes the choice is branching-factor-specific and that a arbitrary-key trie (e.g. 256-way for bytes) would instead favor a `HashMap`. | quote: "This is a common pattern in Rust to represent a tree structure. This avoids further allocations when inserting nodes." | practiced_evidence: https://d34dl0ck.me | flag: voice-unverified
- voice: Sven Kanoldt | connection: same, post's closing recommendation to readers | position: roll-your-own-over-dependency-for-simple-cases | date: 2024-06-26 | locator: post body, § Conclusion | paraphrase: While acknowledging the general-purpose `trie_rs` crate exists for more complex cases, recommends keeping a small dependency list and writing the minimal trie yourself for a simple, well-understood need, because every added dependency costs ongoing maintenance and reduces control over security and stability. | quote: "I want to encourage you to mind a clean and small dependency list in your projects. Be aware that every external dependency comes with the cost of maintenance and less control over security and stability." | practiced_evidence: https://d34dl0ck.me | flag: voice-unverified

## f008318 — The Embedded Rustacean Issue #39 (2025-02-19, en)
### Nothing new
reason-code: no-decision
reason: A bi-monthly newsletter curating embedded-Rust news, events, crate-release and job links; it names topics other posts argue about (e.g. Rust-in-Linux-kernel disputes) but states no decision of its own in the linked-list text.
