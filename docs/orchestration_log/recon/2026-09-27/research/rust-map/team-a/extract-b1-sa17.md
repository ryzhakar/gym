## f007659 — Create a Lambda in Rust using Terraform (2023-11-05, en)

### Nothing new
`nothing new` — self-described-beginner's step-by-step Lambda/Terraform tutorial with settled release-profile tuning (opt-level=z, lto, codegen-units=1, panic=abort, strip) and Reddit-sourced tips; no contested point argued, just documented technique.

## f007703 — Rocket: Web-based Hello World! with tests (2023-12-27, en)

### Nothing new
`nothing new` — pure Rocket-framework hello-world tutorial with tests; no disagreement raised.

## f007736 — Rust macros taking care of some Lambda boilerplate (2024-01-10, en)

### Questions
- Q: Should a procedural macro be used to eliminate repetitive Lambda-handler boilerplate in Rust, or should the boilerplate be written out explicitly?
  concepts: macros (attribute macros, proc-macro), boilerplate; domains_live: cloud-workers, core; positions_seen: macro-not-worth-it-by-default (with a narrow exception)

### Claims
- voice: Sam Van Overmeire | position: macro-not-worth-it-by-default | date: 2024-01-10 | locator: paragraph beginning "Before continuing: would you ever want to use a macro like this?" | paraphrase: Defaults against using an attribute macro to strip Lambda-handler boilerplate in real applications, since the boilerplate is usually minor or main() needs custom per-Lambda initialization anyway; reserves the macro for many simple Lambdas, low tolerance for boilerplate, or macro experimentation. | quote: "Before continuing: would you ever want to use a macro like this? For real applications: default to no." | practiced_evidence: none stated (illustrative macro built for the post, not a shipped crate)

## f007797 — Deploying Axum to Lambda and ECS, using Lambda Web Adapter (2024-02-16, en)

### Questions
- Q: Should a Rust web service targeting AWS be deployed to Lambda or to a long-running container platform (ECS/Fargate)?
  concepts: async runtimes, cloud deployment; domains_live: cloud-workers; positions_seen: workload-dependent-split (Lambda for infrequent/test traffic, ECS for always-on production)

### Claims
- voice: Sam Van Overmeire | position: lambda-for-infrequent-ecs-for-24-7 | date: 2024-02-16 | locator: paragraph beginning "Lambda Web Adapter not only makes it easier..." | paraphrase: Using Lambda Web Adapter to keep one Axum app deployable to either target, argues Lambda suits infrequently-used or test environments while ECS/Fargate is cheaper for always-on production traffic — accepting a test/prod infrastructure mismatch for the cost savings. | quote: "An application that runs 24/7 on prod can be costly on Lambda, but cheap on ECS. On the other hand, if you have one or more infrequently used test environments, Lambda is the better choice." | practiced_evidence: none stated (example project shown in the post, not an independently maintained repo)

## f007846 — How Meilisearch Updates a Millions Vector Embeddings Database in Under a Minute (2024-03-25, en)

### Questions
- Q: For shared mutable state on a hot parallel path in Rust, should code use a Mutex or a lock-free approach (atomics)?
  concepts: concurrency, atomics, Mutex, rayon; domains_live: ml, core; positions_seen: lock-free-atomics-preferred-for-hot-path (Mutex tried first and rejected)

### Claims
- voice: Kerollmops (Tamo) | position: lock-free-atomics-over-mutex-for-hot-path | date: 2024-03-25 | locator: § "Sharing an Iterator Over the Available IDs" → § "The Final Solution" | paraphrase: Rejected a Mutex-guarded shared iterator for concurrent tree-node ID generation because it forces threads to wait on the lock; replaced it with a lock-free design (RoaringBitmap::select plus AtomicU32/AtomicU64/AtomicBool) that lets threads generate IDs without synchronization. | quote: "That is safe and will yield the right results, but won't scale well as all the threads have to wait for each other on the lock." | practiced_evidence: https://github.com/meilisearch/arroy (ConcurrentNodeIds shipped in arroy, used in Meilisearch production)

## f007884 — Designing an efficient memory layout in Rust with unsafe & unions (2024-04-28, en)

### Questions
- Q: For a value that can be one of several known types, should Rust code use dynamic dispatch (Box<dyn Trait>), a tagged enum, or unsafe unions/tagged-pointer packing?
  concepts: unsafe, enums, dynamic dispatch (dyn Trait), tagged pointers, memory layout; domains_live: desktop-cli-ui, core; positions_seen: enum-dispatch-default, dyn-trait-avoid-when-avoidable, unsafe-unions-for-memory-squeeze

### Claims
- voice: alonely0 | position: enum-dispatch-default | date: 2024-04-28 | locator: § "Enum dispatch", opening | paraphrase: Recommends enums (enum_dispatch-style) as the default over dynamic dispatch for a fixed set of known types, since it drops heap allocation and vtable indirection while staying entirely safe. | quote: "The naive approach, which is the one I'd recommend myself, would be to use enums." | practiced_evidence: none stated (worked example for a planned CLI spreadsheet, not yet a published crate)
- voice: alonely0 | position: dyn-trait-avoid-when-avoidable | date: 2024-04-28 | locator: § "A first attempt: dynamic dispatch", closing paragraph | paraphrase: Treats Box<dyn Trait> as the slowest and least idiomatic option, worth using mainly as a guaranteed-two-word size bound or as a fallback for one oversized enum variant, to be avoided otherwise. | quote: "it's the slowest and least idiomatic" | practiced_evidence: none stated
- voice: alonely0 | position: unsafe-unions-for-memory-squeeze | date: 2024-04-28 | locator: § "Now with unions, also known as C's untagged enums..." | paraphrase: Goes beyond the enum-dispatch default into unsafe unions with hand-rolled tagged pointers (ManuallyDrop, ptr aliasing via transmute_copy) to shrink the value below the default enum's size, treating it as a deliberate, specialized escalation past safe Rust when memory layout is worth the unsafety. | quote: "Unions are not just an archaic tool from the long forgotten era of Dennis Ritchie, they are still a very useful tool which can yield amazing results in the right han[ds]" | practiced_evidence: none stated (first post in a planned series; code not yet a published crate)

## f008217 — Crash recovery in 256 bytes: the exhubris supervisor (2024-12-14, en)

### Questions
- Q: In an embedded OS kernel, should crash-recovery policy (restart strategy, backoff, giving up) be hardcoded into the kernel, or left to an application-defined supervisor task?
  concepts: fault handling, kernel/task boundary, IPC; domains_live: embedded; positions_seen: policy-in-userspace-supervisor-not-kernel
- Q: In safety/crash-sensitive embedded Rust, should panics be eliminated for a given task at compile time, or tolerated and handled via runtime crash recovery?
  concepts: panics, no_std, embedded, compile-time guarantees; domains_live: embedded; positions_seen: compile-time-no-panic-for-the-one-critical-task (supervisor), runtime-recovery-for-ordinary-tasks

### Claims
- voice: Cliff L. Biffle | position: policy-in-userspace-supervisor-not-kernel | date: 2024-12-14 | locator: § "The role of the supervisor in Hubris" | paraphrase: Hubris's kernel deliberately does not hardcode a crash-restart policy (immediate restart, backoff, giving up); it only records the fault and notifies a userspace supervisor task, leaving the recovery policy to the application programmer because the correct policy depends on context. | quote: "My conclusion is that there is no right answer to this question... So, Hubris leaves it up to you, the programmer." | practiced_evidence: https://github.com/oxidecomputer/hubris ("the same ... restart-on-crash policy is what we use in Oxide's production firmware")
- voice: Cliff L. Biffle | position: compile-time-no-panic-for-the-one-critical-task | date: 2024-12-14 | locator: § "Who supervises the supervisor?" | paraphrase: Because nothing restarts the supervisor task itself if it crashes, recommends compiling it with userlib's no-panic feature so any unoptimized-away panic becomes a link failure, catching a whole class of crashes at compile time for that one task rather than relying on runtime recovery (which has no one above it). | quote: "This provides a way to ensure, at compile time, that a task cannot panic." | practiced_evidence: https://github.com/oxidecomputer/hubris (minisuper's Cargo.toml enables the feature)

## f008237 — A Complete Guide to WASIp2 for Rust and Python Programmers (2025-01-08 / updated 2026-09-22, en)

### Nothing new
`nothing new` — a WASIp2/component-model tutorial (WIT, worlds, wit-bindgen, wasmtime hosting). It documents a filed, unresolved GitHub issue that trivial std usage (e.g. format!) pulls the whole wasi:cli world into a wasm32-wasip2 component, but presents this only as an acknowledged bug/limitation, not as a live disagreement between named positions.

## f008241 — Floating point to hex converter: now supports 16-bit floats, rewritten in Rust and WebAssembly (2025-01-08, en)

### Nothing new
`nothing new` — personal project rewrite log (Python/C to Rust, then wasm-bindgen); states personal preferences (avoiding allocations via Cow, avoiding frontend frameworks) as individual taste, not a contested point argued against another position.

## f008381 — The Embedded Rustacean Issue #42 (2025-03-28, en)

### Nothing new
`nothing new` — bi-monthly link-roundup newsletter (headlines and external links only); no original declared position of its own to extract a Claim from.
