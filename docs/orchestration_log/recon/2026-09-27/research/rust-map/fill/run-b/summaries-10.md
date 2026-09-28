# Blind fill B, batch 1, file 10 — Position summaries

## reflection-type-model-and-mutation--open-design-space — Unresolved
Advocates describe the in-progress compiler/std reflection MVP as an open, contested design space with more open questions than answers: whether to describe types from the compiler's internal model or from what's useful to a user, whether description should be driven by serialization needs, and whether mutation through reflection is sound at all, given it could violate invariants expressed nowhere but the code.
Tag: fact
Claims: b-sb24-f011413-c4, a-sa25-f011413-c7

## reject-connections-before-handshake--p1 — Reject early
Advocates add a hook so a public endpoint can accept, reject, or retry an incoming connection by address, endpoint ID, or ALPN before the handshake finishes, because rejecting early is far cheaper than accepting and then closing — benchmarked at roughly 30x the throughput of address-based rejection versus accept-then-close.
Tag: fact
Claims: a-sR13-f004586-c3

## release-lto--p1 — Enable LTO in release builds despite longer compile times
Advocates state LTO makes the output both smaller and faster at runtime, via more inlining and pruning, and recommend it despite the longer compilation it costs.
Tag: tradeoff
Claims: b-bk02-f000256-c13

## release-on-request--p1 — Release on request
Advocates hold that cutting a release is relatively low cost, so a release should follow as soon as a fix is requested, with a tracking issue so a request made in a closed PR isn't lost.
Tag: taste
Claims: a-sT07-f002883-c1

## release-sequencing-after-dependency-major--p1 — Ship against the planned dependency minor
Advocates reason that since the next dependency release is a minor version, it should already work with the current major, so there is no need to wait for or sequence after a future major bump.
Tag: fact
Claims: b-sT07-f003809-c2

## replace-battle-tested-c-with-rust--p1 — Rust by default with pragmatic C exceptions
Advocates aim to implement a project and its dependencies in Rust as much as reasonably possible, but treat pragmatic exceptions as legitimate — for instance, not rewriting a widely shared cryptographic library in Rust when the same upstream C implementation other major projects already rely on is available.
Tag: tradeoff
Claims: b-bk03-f000267-c1

## replace-battle-tested-c-with-rust--reject-moral-framing — Not a moral imperative; an economic choice
Advocates reject casting language choice as a moral question: one points out that the same "moral imperative" logic, taken seriously, would demand replacing Rust itself with something formally stronger, showing the framing proves too much; another argues correctness and safety outcomes are driven by who funds the work (citing unfunded xz-utils maintenance) rather than by language choice; a third states plainly that real moral imperatives exist in the industry, and language choice isn't one of them.
Tag: taste
Claims: b-sb19-f005743-c1, b-sb19-f005743-c2, b-sb19-f005743-c3

## replace-battle-tested-c-with-rust--safety-not-enough — Memory safety is far from enough; model checking needed
Advocates state plainly that Rust "isn't nearly enough" on its own, and that any conversation about writing safer software should include model checking (CBMC for C, Kani for Rust, SPARK for Ada) regardless of the language chosen.
Tag: taste
Claims: b-sb26-f012849-c2

## replace-battle-tested-c-with-rust--bootstrap-undermines-case — The bootstrap trust gap undermines the safety argument
Advocates argue language-level memory safety is moot if the compiler's own bootstrap chain can't be trusted, and that by the same "moral imperative" logic this would make avoiding Rust — until its bootstrapping is fixed — the actual imperative.
Tag: taste
Claims: b-sb19-f005743-c8

## replace-battle-tested-c-with-rust--only-maintenance-improves-code — Age alone does not improve code; maintenance does
Advocates reframe a cited study as showing that active use and ongoing maintenance reduce bugs over time, not the simple passage of time, and separately reject the "old codebases are more optimized/battle-tested" meme as false in general — it depends entirely on whether someone actually spent time optimizing or fuzzing the code, illustrated by a Rust crate beating glibc's iconv due to iconv's fundamentally slow architecture.
Tag: fact
Claims: a-saL1-f005516-c8, a-saL1-f005516-c7

## replace-battle-tested-c-with-rust--broad-quality-improvement — A broad quality improvement; pushback is mostly habit
Advocates, after decades writing C/C++, state Rust keeps them from an entire class of mistakes that were too easy to make in any language without garbage collection, and characterize pushback against Rust as belly-aching from people too attached to what they've used for decades.
Tag: taste
Claims: b-sb26-f012849-c1

## replace-battle-tested-c-with-rust--narrow-niche — Rust's legitimate niche is narrow
Advocates frame Rust's proper role as displacing C specifically in very-low-level or constrained-environment work, judging its contribution to areas like OS kernel development as minor.
Tag: taste
Claims: b-sb26-f012849-c3

## replace-battle-tested-c-with-rust--replace-with-rust — Replace it; memory safety outweighs the testing record
Advocates argue for moving off C-based implementations despite their long testing record: one cites a long history of memory-safety vulnerabilities in C-based TLS plus roughly 2x lower measured latency in a Rust alternative as reason for the field to move on; another migrates a project off heavily-tested and continuously-fuzzed C image codecs to a Rust crate, explicitly acknowledging the Rust crates are comparatively less developed, but framing the migration itself as the way to find and close that gap.
Tag: tradeoff
Claims: b-sb19-f005964-c1, a-sa15-f006797-c1

## replace-battle-tested-c-with-rust--age-means-battle-tested — Old C is more optimized and reliable for its age
Advocates cite a Google security study on Android to argue that older code tends to have fewer bugs.
Tag: fact
Claims: a-saL1-f005516-c6

## repr-c-for-persistent-memory--p1 — Repr C required
Advocates hold that `#[repr(C)]` is needed to keep an object's in-memory layout stable across binary versions, since Rust's default layout carries no such guarantee.
Tag: fact
Claims: b-sb19-f005836-c2

## repr-packed-vs-byte-array--p1 — Avoid repr(packed); use byte-array getters
Advocates reject the tempting `#[repr(packed)]` shortcut as "controversial for good reasons," instead storing the fields as a raw byte array with typed getter methods — a safer, more verbose approach that compiles to the same layout without exposing misaligned references.
Tag: tradeoff
Claims: b-sb17-f005113-c1

## reproduce-wasm-bugs-natively--p2 — Native #[test]/#[bench] for non-JS bugs, not debugging on the wasm target directly
Advocates hold that wasm's debugging story is still immature (no DWARF-equivalent, stepping through raw instructions), so bugs and benchmarks not tied to JS/Web-API interaction should be reproduced as native tests to use more mature OS-native profilers and tooling — while cautioning to first confirm via a browser profiler that the bottleneck is actually in the wasm before investing in native profiling.
Tag: tradeoff
Claims: a-sB02-f000256-c15, b-bk02-f000256-c8

## required-signals-vs-option-pins--p1 — Require an explicit signal value for every input/output
Advocates argue that once a change lands, no driver should accept `Option<PIN>`; users should explicitly set every signal, even to a placeholder value, mainly to prevent a previous configuration's settings from lingering.
Tag: taste
Claims: a-sR06-f002005-c2

## restrict-external-construction--p1 — Restrict external construction of the validated type
Advocates lean toward not letting external callers construct the type at all, and independently agree this makes sense since every value of the type is created internally anyway.
Tag: taste
Claims: a-sa11-f004265-c4, a-sa11-f004265-c5

## retain-joinhandles--p1 — Always retain and poll JoinHandles
Advocates warn that Tokio makes it easy — and even implicitly encourages, via its own examples — dropping a `JoinHandle` and letting a task run detached, silently swallowing any panic inside it; they recommend always polling handles (via `buffered_unordered`, `JoinSet`, or a custom aborting wrapper) so panics surface.
Tag: taste
Claims: b-sb17-f005159-c5

## reuse-vs-purpose-built-unwind--p1 — Prefer reuse of existing unwind logic
Advocates do not want a second, parallel implementation of debuginfo-less unwinding built alongside one that is already implemented and battle-tested in the codebase, though they are fine with two separate collection methods coexisting.
Tag: tradeoff
Claims: b-sb13-f004160-c1

## reuse-vs-purpose-built-unwind--p2 — Prefer a purpose-built implementation for performance
Advocates choose a simpler, purpose-built frame-pointer-only unwinder over the codebase's existing general unwind machinery, because the general implementation does more than this use case needs and is roughly 100x slower for the purpose.
Tag: tradeoff
Claims: b-sb13-f004160-c2

## roadmap-performance-vs-features--p1 — Perf first for a quarter
Advocates argue the project is already in good shape on extensibility and customizability, so it should dedicate one or two quarters specifically to performance rather than new features.
Tag: taste
Claims: b-sR04-f001724-c1

## roadmap-performance-vs-features--p2 — Feature work also serves perf
Advocates argue an in-progress feature proposal is not purely a detour from the performance push, since it would itself improve performance (e.g. enabling late materialization for certain array/string representations), while still agreeing to rescope it to be easier to manage given the perf-quarter priority.
Tag: tradeoff
Claims: b-sR04-f001724-c2

## rpc-error-detail-vs-flat-outcome--p1 — Flat outcome enum over `Result<T, E>`
Advocates make an RPC response a plain enum rather than a `Result` carrying a detailed error, because serializing detailed errors is often a real pain and failure specifics like stack traces are "nobody's business" — the enum tells the caller only enough to decide whether retrying makes sense.
Tag: tradeoff
Claims: a-sa06-f003590-c1

## rtic-is-an-rtos--p1 — RTIC is a (hardware-accelerated) RTOS
Advocates (the project's own developers) state that from their point of view RTIC is a hardware-accelerated RTOS — using hardware like the NVIC on Cortex-M or CLIC on RISC-V to perform scheduling rather than a classical software kernel — while noting another common view in the community instead calls it a concurrency framework.
Tag: fact
Claims: a-sB01-f000227-c1, a-sR01-f000227-c1

## rust-core-guidelines-document--p1 — Enforce via compiler and Clippy lints rather than write a guidelines document
Advocates hold that Rust's preferred solution is to avoid needing a prescriptive guidelines document at all: the language is designed to be statically analyzable so the compiler enforces as much as possible, and when a gotcha is discovered, the community tends to write a Clippy lint for it rather than document a best practice, with popular crates serving as de-facto standards.
Tag: fact
Claims: a-sa26-f011993-c1 (voice track record not established in this source)

## rust-cuda-vs-cpp-kernels--p1 — Rust-cuda is the right direction despite CUDA's vendor lock-in and current gaps
Advocates present a Rust-native GPU-kernel toolchain (kernels and host code both in Rust) as an exciting alternative to C++/CUDA, while conceding under audience pressure that they know of no equivalent for other GPU vendors and that almost all real GPU work today still goes through C++ kernels with a thin Rust host layer.
Tag: tradeoff
Claims: b-sb23-f011233-c1

## rust-efficiency-for-cloud-workloads--p1 — Large quantified advantage
Advocates endorse a cited industry article's figures as making the case for Rust: at least 50% less energy, up to 75% less CPU time, and up to 95% less memory versus Python, Ruby, and JavaScript.
Tag: fact
Claims: a-sB01-f000149-c3

## rust-for-ai-generated-code--p1 — Rust is the best language for an AI-coding future
Advocates argue that as AI increasingly writes code and humans architect systems, Rust's compiler acts as an independent, automatic check on AI-generated code — catching issues like memory leaks — that other languages' compilers don't provide.
Tag: taste
Claims: a-sa26-f011443-c2

## rust-for-backend-services-vs-jvm--rust-over-jvm — Rust over the JVM or C/C++ for backend services
Advocates build a Rust application framework explicitly modeled on Spring Boot's convention-over-configuration philosophy, with an extensible plugin system over Rust crates and procedural macros (e.g. `#[component]`) replacing hand-written trait implementations, positioning it as a Rust-native alternative for the audience Spring Boot serves.
Tag: taste
Claims: b-sT09-f005314-c1

## rust-for-high-level-apps--push-rust-into-high-level-apps — Push Rust into high-level application development
Advocates argue Rust's mission should not be exclusive to systems/"core" software, and that high-level Rust application development deserves the same investment.
Tag: taste
Claims: a-sa26-f011305-c1

## rust-for-high-level-apps--less-productive-for-prototyping — Today Rust is less productive than high-level frameworks for prototyping
Advocates report that long compile times and language rigidity made their own project's users more productive with existing tools (React, FastAPI) than with early high-level Rust tooling.
Tag: fact
Claims: a-sa26-f011305-c2

## rust-for-lambda-vs-interpreted--p1 — Worth it for Lambda
Advocates argue Rust's compiled binaries lower both the memory and execution-time dimensions of Lambda's billing formula compared to JavaScript and Python, and that its explicit Option/Result handling catches edge cases earlier; they report cold starts of 10-60ms, roughly 10-20x faster than the interpreted alternatives.
Tag: fact
Claims: b-sb19-f007042-c1

## rust-for-mlops-vs-python--p1 — Rust-first default
Advocates set Rust as the first-choice language for cloud/data/MLOps work, falling back to Python only when necessary.
Tag: taste
Claims: a-sB01-f000149-c1

## rust-for-web-frontend--rust-wasm-over-js-broadly — Rust/Wasm beats JS broadly, even for small string-heavy functions
Advocates argue JS's dynamic typing and GC pauses make web performance unreliable, while Rust gives low-level control without that non-determinism, ships no runtime so `.wasm` stays small, and allows porting only hot-path functions incrementally; separately, advocates set out to debunk as myths the claims that Rust FFI is too slow, that wasm should be reserved for only the heaviest compute, and that JavaScript is fast enough — backing this with a hand-optimized hex-color-parsing function that beat its JavaScript counterpart by roughly 2x despite being "very hostile" to wasm (string copying, minimal computation, allocation on return).
Tag: fact
Claims: b-sR01-f000256-c1, a-sa26-f011460-c1, a-sa26-f011460-c2

## rust-for-web-frontend--rust-wasm-compute-bound-only — Rust/Wasm only for compute-bound work with minimal interop
Advocates report that wasm wins only for compute-bound work with rare boundary crossings (image/video, crypto, physics, porting existing C/C++ libraries), and loses for parsing structured text into JS objects or for frequently-called functions on small inputs, because the serialization/boundary tax dominates and the JIT closes the raw-compute gap.
Tag: fact
Claims: b-sb19-f005699-c1

## rust-for-web-frontend--isomorphic-rust-web — A unified isomorphic Rust client/server model
Advocates contrast a framework that replicates Rails-style scaffolding with a separate React frontend against one that lets a developer define server functions callable directly from client code, with the client/server interface auto-generated so logic can move between client and server almost effortlessly.
Tag: taste
Claims: a-sa26-f012146-c1

## rust-for-web-frontend--not-yet-for-frontend — Not yet for frontends: Rust backend, TypeScript frontend
Advocates, after using a Rust frontend framework on a real project, conclude "not yet" — it remains unpleasant compared to their JavaScript-ecosystem gold standard, even while feeling optimistic about its trajectory, and choose Rust for the backend and TypeScript for the frontend in the meantime.
Tag: taste
Claims: b-sb20-f007290-c1

## rust-in-process-server-new-capability--p1 — Rust enables safe in-process libification
Advocates argue the interesting part of an embeddable Rust HTTP server library is that it "lib-ifies" the web-server concept in a way that was never realistic to do safely in C/C++; refining the framing further, they argue it isn't "Rust safe, C dangerous" in the abstract, but that making well-written C safe to use generally requires isolating it in a separate process, whereas Rust lets expert-written, high-performance code be reused safely as a library by less-expert programmers — genuinely novel.
Tag: fact
Claims: a-saL1-f005360-c1, a-saL1-f005360-c2

## rust-in-process-server-new-capability--p2 — Safety framing is overstated
Advocates push back that framing a memory-safe language's libraries against C/C++'s dangers is "getting really old," pointing out that nginx and Apache — both written in C — already work fine as web servers.
Tag: taste
Claims: a-saL1-f005360-c3

## rust-lang-org-ai-assistant--p1 — Acceptable if strictly opt-in
Advocates argue making the feature opt-in (hidden unless enabled by a preference) would defuse resistance, noting people already bring raw ChatGPT output to the forum for help, so a built-in, opt-in assistant could improve on that status quo.
Tag: taste
Claims: a-sa29-f013224-c1

## rust-lang-org-ai-assistant--p2 — Should not host an LLM feature; the economics are a net negative
Advocates argue LLMs are expensive to run well, that only VC-subsidized companies can offer good models cheaply, and that tuning response quality is a full-time job the community can't sustain — so users are better served using existing third-party AI services themselves.
Tag: tradeoff
Claims: a-sa29-f013224-c2

## rust-lang-org-ai-assistant--p3 — The real problem is inadequate full-text search, not the absence of an LLM
Advocates report that current documentation search matches only type/item names, not documentation prose, citing a concrete search miss, and argue proper full-text search would be the bigger win.
Tag: fact
Claims: a-sa29-f013224-c3

## rust-ml-edge-inference-vs-python--p1 — Rust/Burn viable for edge inference
Advocates choose Rust+Burn over Python/PyTorch for an offline, zero-connectivity model targeting phones and laptops, citing a single ~24MB binary versus ~7.1GB of PyTorch dependencies, sub-100ms cold start versus PyTorch's ~3s, and one codebase compiling to native GPU, CPU, WASM and mobile targets — concluding the stack is legitimate specifically for edge inference, not for training.
Tag: fact
Claims: a-sa18-f008787-c1

## rust-trademark-policy--p1 — Revised 2024 draft
Advocates (the Leadership Council) state that after community concern about the 2023 draft, the revised policy is legally sound, protects the language's integrity, and addresses the prevailing concerns raised.
Tag: fact
Claims: a-sT12-f009632-c1
