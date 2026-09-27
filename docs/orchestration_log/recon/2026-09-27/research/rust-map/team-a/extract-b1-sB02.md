## f000256 — Rust and WebAssembly (2018, English)

### Questions

- Q: Port performance-critical JS incrementally into Rust, or rewrite the whole app?
  concepts: incremental adoption; domains_live: web, wasm; positions_seen: incremental-port-only-hot-paths

- Q: How to bound an in-principle-infinite cellular-automaton grid in finite memory: track a growing dirty region, a fixed non-periodic edge, or a fixed periodic (toroidal) edge?
  concepts: memory bounding, cellular automata; domains_live: wasm, core; positions_seen: growing-region, fixed-non-periodic, fixed-periodic(chosen)

- Q: At a Rust/JS boundary, expose large long-lived data by copying/serializing it across, or as an opaque handle into wasm linear memory?
  concepts: FFI boundary design, wasm-bindgen; domains_live: web, wasm; positions_seen: opaque-handles(recommended), copy-serialize(discouraged)

- Q: Expose the whole simulation state to JS each frame, or only the delta of what changed?
  concepts: rendering strategy, wasm/js boundary; domains_live: web, wasm; positions_seen: whole-snapshot(chosen), delta-based(alternative, harder to implement)

- Q: In hot loops needing wraparound indexing, use modulo arithmetic or branch on edge cases with a manually unrolled loop?
  concepts: loop optimization, branch prediction; domains_live: core, wasm; positions_seen: modulo(original), branch-unrolled(chosen, 7.61x speedup measured)

- Q: Should optimization work be guided by profiling measurements or by a developer's hypothesis about where cost lives?
  concepts: profiling discipline; domains_live: core; positions_seen: profile-first(recommended; a stated hypothesis about allocation cost was measured and found wrong)

- Q: For .wasm code-size builds, is opt-level="z" always smaller than "s", or must the choice be measured per build?
  concepts: build config, LTO, codegen; domains_live: wasm; positions_seen: measure-both(recommended), assume-z-smaller(rejected)

- Q: When avoiding panic-driven code bloat, should Option/Result unwrapping fail safely via process::abort(), or use unsafe unchecked assumption?
  concepts: panic avoidance, unwrap, code size; domains_live: wasm, embedded; positions_seen: safe-abort(default recommendation), unsafe-unchecked(only when "110% sure", gated to release)

- Q: For code-size-sensitive Rust, prefer generic functions (static dispatch, monomorphized) or trait objects (dynamic dispatch)?
  concepts: static vs dynamic dispatch, monomorphization bloat; domains_live: wasm, embedded, core; positions_seen: trait-objects(recommended here for size, at cost of perf and optimizer opportunities)

- Q: Should a size-sensitive wasm crate keep the default allocator, switch to a size-optimized allocator, or eliminate heap allocation entirely?
  concepts: allocator choice; domains_live: wasm, embedded; positions_seen: switch-to-wee_alloc(trades allocation speed for ~10KB size), eliminate-allocation/no_std(most size saved)

- Q: Should a portable library crate perform its own I/O and thread spawning, or factor those out to the caller?
  concepts: portability, I/O abstraction, wasm target constraints; domains_live: wasm, embedded, core; positions_seen: factor-out-I/O(recommended), bring-your-own-threads(recommended)

- Q: When debugging Rust-generated WebAssembly, reproduce the bug as a native Rust #[test]/#[bench] first, or debug inside the wasm/browser environment directly?
  concepts: debugging strategy, native vs wasm tooling maturity; domains_live: wasm, web; positions_seen: prefer-native-repro(recommended; wasm debugger tooling called "immature"), debug-in-browser(fallback)

- Q: For panics on wasm32-unknown-unknown, install a panic hook (console_error_panic_hook) or accept the default trap message?
  concepts: panic hook, error reporting; domains_live: wasm, web; positions_seen: install-panic-hook(recommended), no-hook(rejected, "not as useful")

- Q: Which JS bundler/dev-server should front a Rust+wasm web app: webpack, an alternative bundler, or none?
  concepts: build tooling, bundlers; domains_live: web, wasm; positions_seen: webpack(chosen, "for convenience"), parcel/rollup(named alternative, also supported), no-bundler(viable)

### Claims

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: incremental-port-only-hot-paths | date: 2018 | locator: § "Why Rust and WebAssembly?" — "Do Not Rewrite Everything" | paraphrase: existing JS code bases don't need to be thrown away; port the most performance-sensitive functions to Rust for immediate benefit, and you can stop there if you want. | quote: "Existing code bases don't need to be thrown away." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: fixed-periodic(chosen) | date: 2018 | locator: § "Implementing Conway's Game of Life" — "Design" — "Infinite Universe" | paraphrase: of three ways to bound the infinite universe (expanding dirty-region tracking, fixed non-periodic, fixed periodic/wraparound), the tutorial picks periodic wraparound because unbounded expansion risks running out of memory and fixed non-periodic edges snuff out infinite patterns like gliders. | quote: "We will implement the third option." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: opaque-handles(recommended) | date: 2018 | locator: § "Interfacing Rust and JavaScript" | paraphrase: a good JS↔wasm interface keeps large, long-lived data as Rust types living in wasm linear memory, exposed to JS only as opaque handles, to minimize copying and serialization overhead across the boundary. | quote: "we want to optimize for the following properties: Minimizing copying... Minimizing serializing and deserializing." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: whole-snapshot(chosen) | date: 2018 | locator: § "Interfacing Rust and JavaScript in our Game of Life" | paraphrase: the tutorial exposes the whole universe (as a pointer into linear memory) each tick rather than the delta-based design, naming the delta approach as a viable but harder-to-implement alternative. | quote: "Another viable design alternative would be for Rust to return a list of every cell that changed states after each tick... The trade off is that this delta-based design is slightly more difficult to implement." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: branch-unrolled(chosen) | date: 2018 | locator: § "Time Profiling" — "Making Time Run Faster" | paraphrase: modulo-based edge wraparound in live_neighbor_count costs a div instruction on the common non-edge case; replacing it with if-branches and a manually unrolled neighbor loop lets the branch predictor do the work instead, measured at a 7.61x speedup. | quote: "if we use ifs for the edge cases and unroll this loop, the branches should be very well-predicted by the CPU's branch predictor." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: profile-first(recommended) | date: 2018 | locator: § "Time Profiling" — "Making Time Run Faster" | paraphrase: a stated hypothesis (allocating/freeing a cells vector each tick is the bottleneck) was measured and found false — the cost was actually in computing the next generation — used as the reason to always let profiling guide optimization effort rather than intuition. | quote: "Looking at the timings, it is clear that my hypothesis is incorrect... Another reminder to always guide our efforts with profiling!" | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: measure-both(recommended) | date: 2018 | locator: § "Shrinking .wasm Code Size" — "Tell LLVM to Optimize for Size Instead of Speed" | paraphrase: opt-level="s" can sometimes produce smaller binaries than the more aggressive opt-level="z", so the choice should be measured rather than assumed. | quote: "Note that, surprisingly enough, opt-level = \"s\" can sometimes result in smaller binaries than opt-level = \"z\". Always measure!" | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: safe-abort(default recommendation) | date: 2018 | locator: § "Shrinking .wasm Code Size" — "Avoid Panicking" | paraphrase: to cut panic-related code bloat from unwrap, prefer a safe helper that calls process::abort() on None/Err over letting the formatted panic machinery run, since panics compile down to aborts on wasm32-unknown-unknown anyway. | quote: "panics translate into aborts in wasm32-unknown-unknown anyways, so this gives you the same behavior but without the code bloat." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: unsafe-unchecked(conditional) | date: 2018 | locator: § "Shrinking .wasm Code Size" — "Avoid Panicking" | paraphrase: the unreachable crate's unsafe unchecked_unwrap is offered as a further alternative, but restricted to cases where the programmer is "110% sure" the assumption holds, and only in release builds, keeping checked behavior in debug. | quote: "You really only want to use this unsafe approach when you 110% know that the assumption holds." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: trait-objects-for-size | date: 2018 | locator: § "Shrinking .wasm Code Size" — "Use Trait Objects Instead of Generic Type Parameters" | paraphrase: generic functions get monomorphized into one copy per type, growing code size; trait objects emit a single function using dynamic dispatch instead, at the cost of lost compiler optimization opportunities and added indirect-call overhead. | quote: "The downside is the loss of the compiler optimization opportunities and the added cost of indirect, dynamically dispatched function calls." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: switch-to-wee_alloc | date: 2018 | locator: § "Shrinking .wasm Code Size" — "Avoid Allocation or Switch to wee_alloc" | paraphrase: the default dlmalloc-based allocator costs ~10KB; replacing it with wee_alloc trades allocation speed for saving most of that size, recommended when allocation can't be avoided entirely. | quote: "wee_alloc is an allocator designed for situations where you need some kind of allocator, but do not need a particularly fast allocator, and will happily trade allocation speed for smaller code size." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: eliminate-allocation/no_std | date: 2018 | locator: § "Shrinking .wasm Size" — exercise on static mut globals | paraphrase: for a single-instance program, exporting operations on a static mut global (with double-buffering) removes all dynamic allocation, allowing a #![no_std] crate with no allocator dependency at all, for maximum size reduction. | quote: "This removes all dynamic allocation from our Game of Life implementation, and we can make it a #![no_std] crate that doesn't include an allocator." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: factor-out-I/O | date: 2018 | locator: § "How to Add WebAssembly Support to a General-Purpose Crate" — "Avoid Performing I/O Directly" | paraphrase: since the Web has no filesystem and only async I/O, a portable library should factor I/O out of itself, taking input slices from callers rather than reading files or performing I/O itself. | quote: "Factor I/O out of your library, let users perform the I/O and then pass the input slices to your library instead." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: bring-your-own-threads | date: 2018 | locator: § "How to Add WebAssembly Support to a General-Purpose Crate" — "Avoid Spawning Threads" | paraphrase: since spawning threads panics on wasm32-unknown-unknown, a portable library should factor thread spawning out to the caller, similar to factoring out I/O, which also plays nicer with apps that own a custom thread pool. | quote: "Another option is to factor out thread spawning from your library and allow users to \"bring their own threads\"." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: prefer-native-repro | date: 2018 | locator: § "Debugging Rust-Generated WebAssembly" — "Avoid the Need to Debug WebAssembly in the First Place" | paraphrase: WebAssembly's debugging story is called immature (no DWARF-equivalent, stepping through raw wasm instructions); bugs not tied to JS/Web-API interaction should instead be reproduced as native #[test]s to use mature OS-native tooling. | quote: "the debugging story for WebAssembly is still immature... you will have an easier time finding and fixing bugs if you can isolate them in a smaller test cases that don't require interacting with JavaScript." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: install-panic-hook | date: 2018 | locator: § "Debugging Rust-Generated WebAssembly" — "Logging Panics" | paraphrase: installing console_error_panic_hook turns a cryptic "RuntimeError: unreachable executed" trap into Rust's actual formatted panic message in the console; the tutorial's own exercise has the reader remove the hook and asks "Not as useful is it?" as the reason to keep it. | quote: "Rather than getting cryptic, difficult-to-debug RuntimeError: unreachable executed error messages, this gives you Rust's formatted panic message." | practiced_evidence: none

- voice: Rust and WebAssembly Working Group [voice-unverified] | position: webpack(chosen, "for convenience") | date: 2018 | locator: § "Hello, World!" — "Install the dependencies" | paraphrase: the tutorial's template uses webpack as bundler/dev-server, stating this isn't required — Parcel and Rollup are named as also supporting wasm as ES modules, and using Rust+wasm with no bundler at all is called viable — webpack is picked "for convenience." | quote: "webpack is not required for working with Rust and WebAssembly, it is just the bundler and development server we've chosen for convenience here." | practiced_evidence: none

### Nothing new

(none — every chapter read yielded at least one declared Position)
