## f000098 — WASM It (2020-05-04, en)
### Questions
- Q: When porting an existing native Rust application (designed for synchronous execution) to WASM, should the WASM support be retrofitted into the existing codebase, or should a WASM-capable design be built from scratch?
  concepts: wasm, event loop, architecture/porting; domains_live: wasm
  positions_seen: retrofit-existing-app, design-from-scratch
- Q: When Rust code designed around a parallel thread pool (e.g. rayon) is compiled to run in the browser via WASM, should it keep parallel task dispatch, or fall back to sequential execution?
  concepts: threading, wasm, event loop, rayon; domains_live: wasm
  positions_seen: keep-parallel-dispatch, sequential-execution-for-wasm
### Claims
- voice: azriel91 | connection: author of the wasm_it porting notes and the Rust game azriel91/autexousious (built on the Amethyst engine); gave this talk at the Rust Auckland meetup | position: design-from-scratch | date: 2020-05-04 | locator: § Worth Mentioning | paraphrase: recommends starting a WASM-capable application from scratch rather than retrofitting an existing native, synchronous-designed app, because bolting the asynchronous, browser-controlled event model onto an existing synchronous design afterward is messy | quote: "If you have the option to begin from scratch, choose that." | practiced_evidence: none | flag: voice-unverified
- voice: azriel91 | connection: author of the wasm_it porting notes and the Rust game azriel91/autexousious (built on the Amethyst engine); gave this talk at the Rust Auckland meetup | position: sequential-execution-for-wasm | date: 2020-05-04 | locator: § Multithreading | paraphrase: switched the WASM build to sequential task execution instead of the native parallel (rayon thread-pool) dispatch, because in the browser tasks submitted to workers only run once control returns to the browser, so the main thread would otherwise block waiting on tasks that can never complete | quote: "When adding WASM support, sequential execution is used." | practiced_evidence: https://github.com/azriel91/autexousious | flag: voice-unverified
