## f000227 — RTIC Preface (unknown, living document)

### Questions
- Q: Is RTIC (and a hardware-scheduled, compile-time-analyzed concurrency model generally) an RTOS, or is it a concurrency framework rather than an operating system?
  concepts: RTIC; RTOS; Stack Resource Policy (SRP); hardware-accelerated scheduling; domains_live: embedded; positions_seen: "hardware-accelerated RTOS" (RTIC project); "concurrency framework, no software kernel" (unattributed community view, no named Voice — not a Claim)
- Q: Should real-time/embedded Rust frameworks model concurrency with async/await tasks rather than classical run-to-completion/interrupt-only tasks?
  concepts: async/await; static allocation; Futures; SRP run-to-completion requirement; domains_live: embedded; positions_seen: "async/await, statically compiled, improves ergonomics without violating SRP or requiring dynamic allocation" (RTIC project)

### Claims
- voice: RTIC project (rtic.rs maintainers, unnamed individually) | position: RTIC is a hardware-accelerated RTOS | date: unknown (living document, no publish/version date given) | locator: § "Is RTIC an RTOS?" | paraphrase: from the maintainers' own view RTIC is a hardware-accelerated RTOS because it uses hardware (e.g. NVIC on Cortex-M) rather than a software kernel to perform scheduling. | quote: "RTIC is a hardware accelerated RTOS that utilizes the hardware such as the NVIC on Cortex-M MCUs, CLIC on RISC-V etc. to perform scheduling, rather than the more classical software kernel." | practiced_evidence: none
- voice: RTIC project (rtic.rs maintainers, unnamed individually) | position: async/await task modeling, compiled to static per-priority executors, is preferable to manual sub-task/state-machine splitting for real-time embedded work | date: unknown (living document, no publish/version date given) | locator: § "RTIC into the Future" | paraphrase: the maintainers argue async/await brings "improved ergonomics" over manual sub-task splitting, is compatible with SRP because the compiler forbids awaiting while holding a resource, and avoids dynamic allocation (which would panic on OOM) by using compile-time-generated static executors. | quote: "So with the technical stuff out of the way, what does async/await bring to the table? The answer is - improved ergonomics!" | practiced_evidence: none

### Nothing new
Not applicable — this source raised contested points (see Questions above).

---

## f000256 — Rust and WebAssembly book, Introduction (unknown, living document)

### Nothing new
`nothing new` — the read section is only front matter (audience, how to read the book, contribution note); it takes no position on any contested point.

---

## f000508 — SE-0410: Atomics review thread, swift.org forums (2023-10-23 to 2023-11-17)

### Nothing new
`nothing new` — this is a Swift Evolution review of a Swift standard-library proposal; participants (Joe_Groff, John_McCall, lorentey, wadetregaskis, Alejandro, Douglas_Gregor, others) are Swift core-team/community members with no established Rust track record in this source, and the handful of Rust mentions (e.g. comparing a proposed attribute to Rust's `UnsafeCell`, noting Rust ownership as a precedent for exclusivity) are passing analogies inside a Swift-internal design debate, not a Rust practitioners' disagreement.

---

## f000538 — yewstack/yew PR #3509 "Dynamic Prop Labels" (2023-11-01 to 2025-05-04)

### Questions
- Q: In a `ToTokens` impl for a proc-macro AST enum, should each arm call `to_tokens` on the matched variant directly, or is it acceptable to build an intermediate `TokenStream` and feed it into the outer one?
  concepts: proc-macro; `ToTokens`; `TokenStream`; domains_live: web; core; positions_seen: "match each variant and call `to_tokens` directly, avoid the intermediate allocation" (its-the-shrimp)
- Q: When a new macro feature's behavior largely overlaps existing generic tests, should reviewers ask for a dedicated test of the new case anyway, or is that redundant?
  concepts: test coverage; proc-macro testing; domains_live: web; positions_seen: "add a dedicated test for the new case" (cecton); "redundant — already covered by more general tests" (kirillsemyonkin)

### Claims
- voice: its-the-shrimp | position: avoid building a temporary `TokenStream` in a `ToTokens` impl; match on the enum and call `to_tokens` on the matched arm directly | date: 2025-05-04 | locator: PR #3509, comment 2025-05-04T12:20:47Z | paraphrase: suggests rewriting the `impl ToTokens` so each match arm calls `to_tokens` on its inner value directly, rather than constructing a `TokenStream` from one variant and feeding it into another. | quote: "to avoid allocating a temporary TokenStream just to feed it into another TokenStream" | practiced_evidence: none
- voice: cecton | position: a new prop-label feature should get its own dedicated test even where the new code path overlaps generic behavior | date: 2023-11-06 | locator: PR #3509, comment 2023-11-06T14:58:24Z | paraphrase: asks the author to add a test covering `Option<AttrValue>` prop values specifically for the new dynamic-prop-label path. | quote: "Maybe you can add a test to make sure this case also works?" | practiced_evidence: none
- voice: kirillsemyonkin | position: a dedicated test for behavior already covered by more general, feature-independent tests is unnecessary | date: 2023-11-06 | locator: PR #3509, comment 2023-11-06T15:34:46Z | paraphrase: questions the value of the requested test, arguing optional-value handling is already exercised by tests not specific to dynamic props. | quote: "Optional values for properties are supposed to be already tested by more general tests that are not inherent to dynamic props." | practiced_evidence: none

### Nothing new
Not applicable — this source raised contested points (see Questions above). (The rest of the thread — CI/benchmark bot output, a wording nit on a panic message, an unrelated FIXME clarification — carries no further contested point.)

---

## f000545 — zed-industries/zed issue #4382 "Zen mode" (2023-11-04 to 2025-08-15)

### Nothing new
`nothing new` — a product feature-request thread about hiding editor UI chrome (tabs, gutter, status bar) and configuring fonts; no Rust language, tooling, or practice question is raised at any point in the thread.

---

## f000801 — Neon blog, "Semantic search using OpenAI, pg_embedding and Neon" (2023-08-25)

### Nothing new
`nothing new` — a TypeScript/Next.js/Postgres tutorial on building semantic search with OpenAI embeddings; contains no Rust content of any kind.
