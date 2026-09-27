## f000149 — Small Rust Tutorial For MLOps (2023, English)

### Questions

- Q: For cloud/data/MLOps work, should Rust be the default language over Python?
  concepts: language-choice-heuristic, MLOps, systems-vs-scripting; domains_live: ml, cloud-workers, core; positions_seen: Rust-first default

- Q: For a Rust web microservice, should Actix be the default framework absent a specific reason to pick another?
  concepts: web-framework-default, CLI-framework-default; domains_live: web, cloud-workers; positions_seen: Actix-default (with Clap for CLI)

- Q: Is Rust's efficiency advantage over Python/Ruby/JS (energy, CPU, memory) large enough to justify adoption for cloud workloads?
  concepts: energy-efficiency, CPU-time, memory-usage, sustainability; domains_live: cloud-workers, core; positions_seen: large-quantified-advantage

### Claims

- voice: Noah Gift | position: Rust-first default | date: 2023 (course release date stated in source; no chapter-level date) | locator: Chapter 1, "Heuristic: Rust if you can, Python if you must" | paraphrase: Sets Rust as the first-choice language for the course's cloud/data/MLOps projects, falling back to Python only when necessary | quote: "Rust if you can, Python if you must" | practiced_evidence: none
- voice: Noah Gift | position: Actix-default for web, Clap for CLI | date: 2023 (course release date stated in source) | locator: Chapter 1, project spec bullet on frameworks | paraphrase: Directs students to default to Clap (CLI) and Actix (web) "unless you have a compelling reason to switch to a new framework" | quote: "unless you have a compelling reason to switch to a new framework" | practiced_evidence: https://github.com/nogibjj/rust-mlops-template
- voice: Noah Gift | position: large-quantified-advantage | date: 2023 (course release date stated in source) | locator: "Sustainability" chapter | paraphrase: Endorses an AWS article's numbers as "nailing" the case for Rust, stating Rust cuts energy ~50%+, CPU time up to 75%, memory up to 95% versus Python/Ruby/JS | quote: "Rust uses at least 50% less energy than languages like Python." | practiced_evidence: none (voice-unverified — source attributes the measurement to an AWS article, not to Noah Gift's own benchmark)

## f000217 — About nalgebra / nalgebra docs (living document, English)

### Questions

- Q: For linear algebra/transforms in Rust, should you prefer nalgebra's strongly-typed API (compile-time dimension/invariant checks) or the simpler, GLM-style nalgebra-glm API?
  concepts: type-level-dimension-checking, ergonomics-vs-rigor, homogeneous-coordinates; domains_live: ml, core; positions_seen: nalgebra for rigor and dynamically-sized cases; nalgebra-glm for simplicity and GLM-familiarity

- Q: Should transformations be represented as dedicated invariant-preserving newtypes (Isometry3, Rotation3, ...) or as raw 4x4/3x3 matrices?
  concepts: newtype-invariants, raw-matrix-flexibility; domains_live: core; positions_seen: dedicated types recommended, raw matrices lack guarantees

- Q: When a matrix's size is known at compile time, should code prefer fixed (stack-allocated) resizing/operations over dynamic (heap-allocated) ones?
  concepts: const-generics-sizing, stack-vs-heap-allocation; domains_live: core, embedded; positions_seen: prefer fixed/static sizing whenever possible

- Q: Does compiling to WebAssembly require disabling the standard library (no_std), the way embedded targets do?
  concepts: no_std, wasm32-unknown-unknown, libstd; domains_live: wasm, embedded; positions_seen: no_std is embedded-only, not needed for wasm

- Q: Should an API add a dedicated method for every composed operation (e.g. append/prepend a rotation) even when it gives no performance benefit over manual composition?
  concepts: API-surface-minimalism, zero-cost-justification; domains_live: core; positions_seen: omit methods that add no perf benefit, compose manually instead

### Claims

- voice: Dimforge (nalgebra maintainers) | position: nalgebra for rigor and dynamically-sized cases; nalgebra-glm for simplicity | date: capture 2025-02-16 (Wayback; underlying doc undated, "living document") | locator: "The nalgebra-glm crate" chapter, "Should I use nalgebra or nalgebra-glm?" | paraphrase: States the choice depends on taste/background — nalgebra for stronger typing and dynamically-sized matrices, nalgebra-glm for those used to C++ GLM or wanting more straightforward functions | quote: "If you prefer more rigorous treatments of transformations, with type-level restrictions, then go for nalgebra." | practiced_evidence: https://github.com/dimforge/nalgebra
- voice: Dimforge (nalgebra maintainers) | position: dedicated types recommended over raw matrices | date: capture 2025-01-21 (Wayback; underlying doc undated) | locator: "Computer-graphics recipes" chapter, "Transformations using Matrix4" | paraphrase: Argues a raw Matrix4 cannot guarantee it represents a pure rotation, isometry, or even an invertible transform, so dedicated transformation types are recommended instead | quote: "That's why all the transformation types are recommended instead of raw matrices." | practiced_evidence: none
- voice: Dimforge (nalgebra maintainers) | position: prefer fixed/static sizing whenever possible | date: capture 2025-01-15 (Wayback; underlying doc undated) | locator: "Vectors and matrices" chapter, "Matrix resizing" | paraphrase: States fixed (compile-time-known) resizing should be preferred over dynamic resizing whenever possible, because dynamic resizing always produces heap-allocated results | quote: "Indeed, dynamic resizing will produce heap-allocated results because the size of the output matrix cannot be deduced at compile-time." | practiced_evidence: none
- voice: Dimforge (nalgebra maintainers) | position: no_std is embedded-only, not needed for wasm | date: capture 2025-03-22 (Wayback; underlying doc undated) | locator: "WASM and embedded targets" chapter, "For embedded development" | paraphrase: Explicitly corrects the assumption that wasm compilation needs libstd disabled; that step is necessary only for embedded, not for browser/wasm targets | quote: "You do not need to disable libstd when compiling to wasm!" | practiced_evidence: none
- voice: Dimforge (nalgebra maintainers) | position: omit methods with no perf benefit, compose manually | date: capture 2025-01-21 (Wayback; underlying doc undated) | locator: "Computer-graphics recipes" chapter, note after "Homogeneous raw transformation matrix modification" table | paraphrase: Explains there is no append/prepend-rotation method because a dedicated method gives no performance benefit over building the rotation matrix and multiplying it in | quote: "That is because a specific method does not provide any performance benefit." | practiced_evidence: none

## f000227 — RTIC book, Preface (living document, English)

Only the Preface chapter is present in this bundle; the table of contents lists chapters 1–8 (RTIC by example, Monotonics, migration guide, etc.) that are not included here and so were not read.

### Questions

- Q: Is RTIC itself an RTOS, or is it better described as a concurrency framework with no software kernel?
  concepts: RTOS-definition, hardware-accelerated-scheduling, software-kernel; domains_live: embedded; positions_seen: RTIC-team: it is a (hardware-accelerated) RTOS; unattributed community view: it is a concurrency framework, not an RTOS

- Q: Should a real-time Rust scheduler drive task dispatch from hardware interrupt priority hardware (NVIC/CLIC) rather than a software kernel, the way most RTOSes do?
  concepts: Stack-Resource-Policy, static-priority-ceiling, zero-cost-scheduling; domains_live: embedded; positions_seen: hardware-interrupt-driven (SRP-based) scheduling preferred over software-kernel scheduling

- Q: For real-time task modelling, is async/await preferable to hand-written state-machine sub-tasking?
  concepts: async-await, run-to-completion, cooperative-multitasking; domains_live: embedded; positions_seen: async/await preferred for ergonomics

- Q: In resource-constrained real-time systems, should allocation be static rather than dynamic?
  concepts: static-allocation, no-heap, panic-on-oom; domains_live: embedded; positions_seen: static allocation preferred

### Claims

- voice: RTIC developers (rtic.rs maintainers) | position: RTIC is a (hardware-accelerated) RTOS | date: undated (living doc, "documentation for RTIC v2.x") | locator: Preface, "Is RTIC an RTOS?" | paraphrase: From the developers' own point of view RTIC is an RTOS that uses hardware (NVIC/CLIC) to perform scheduling rather than a classical software kernel, against an "another common view from the community" that calls it a concurrency framework instead — that opposing view is not attributed to a named, checkable Voice in this source | quote: "From RTIC's developers point of view; RTIC is a hardware accelerated RTOS" | practiced_evidence: https://rtic.rs (project itself)
- voice: RTIC developers | position: hardware-interrupt-driven (SRP-based) scheduling preferred over software-kernel scheduling | date: undated (living doc) | locator: Preface, "RTIC the hardware accelerated real-time scheduler" | paraphrase: Argues the Cortex-M hardware interrupt/priority model maps directly onto Stack Resource Policy scheduling, giving zero-cost, compile-time-computed ceilings, and states this is why SRP-based scheduling is out of reach for a "thread based RTOS" | quote: "In this way RTIC fuses SRP based preemptive scheduling with a zero-cost hardware accelerated implementation" | practiced_evidence: https://rtic.rs
- voice: RTIC developers | position: async/await preferred for ergonomics over manual state-machine sub-tasking | date: undated (living doc) | locator: Preface, "RTIC into the Future" | paraphrase: States that without async/await a programmer must manually split a task into sub-tasks and track state, whereas async/await builds the progression mechanism automatically at compile time via Futures | quote: "The answer is - improved ergonomics!" | practiced_evidence: https://rtic.rs
- voice: RTIC developers | position: static allocation preferred over dynamic in real-time systems | date: undated (living doc) | locator: Preface, "RTIC into the Future" | paraphrase: States dynamic allocation is problematic for resource-constrained real-time systems on both performance and reliability grounds (Rust panics on out-of-memory), so static allocation is the preferable approach | quote: "Thus, static allocation is the preferable approach!" | practiced_evidence: https://rtic.rs
