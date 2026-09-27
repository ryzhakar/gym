## f002499 — Implement `wait_for_done` for `DpiTransfer` (2025-01-03, en)
### Nothing new
`nothing new` — deep hardware DMA/PSRAM-bandwidth debugging on esp-hal's DPI display driver; no contested Rust API-design decision, just diagnosis of a device-specific timing/glitch problem.

## f002501 — allow_headers config allways falls back to * (2025-01-03, en)
### Nothing new
`nothing new` — a loco-rs CORS-config bug report and its fix; a diagnosis-and-patch exchange, not a contested design decision.

## f002517 — Mark unstable modules, make `macros` private (2025-01-07, en)
### Questions
- Q: Before a crate's 1.0 release, should an unreviewed API surface (e.g. the interrupt API) default to stable unless a blocker is raised, or stay marked unstable until the team explicitly agrees it is ready?
  concepts: API stability, semver, 1.0 release process, `#[unstable]` attribute; domains_live: embedded; positions_seen: stable-unless-flagged (MabezDev, initial), unstable-until-agreed-ready (Dominaezzz, bugadani, jessebraham; MabezDev after reversing)
- Q: Should the proc-macro re-exports that a required language-level macro (e.g. `entry`, the crate's `main`) depends on be marked unstable along with everything else, or kept stable because the crate is unusable without them?
  concepts: API stability, proc-macros, `#[unstable]` attribute; domains_live: embedded; positions_seen: needs-to-stay-usable (bugadani)
### Claims
- voice: MabezDev | position: stable-unless-flagged | date: 2025-01-10 | locator: comment 2025-01-10T12:44:33Z | paraphrase: without a known blocking issue, sees no problem exposing the interrupt API as stable for now, having assumed the team was already aligned | quote: "if there isn't anything else then I don't see any issue in exposing this as stable, at least for now." | practiced_evidence: none
- voice: Dominaezzz | position: unstable-until-agreed-ready | date: 2025-01-10 | locator: comment 2025-01-10T12:26:08Z | paraphrase: objects that interrupts are being stabilized, since prior PRs assumed they would stay unstable and some interrupt enum variants don't make sense for the CPU-driven driver | quote: "The PRs targeting interrupts so far have done so under the assumption that they won't be stabilized." | practiced_evidence: none
- voice: MabezDev | position: unstable-until-agreed-ready | date: 2025-01-10 | locator: comment 2025-01-10T13:08:42Z | paraphrase: after push back, reverses course and agrees the interrupt API isn't ready, marking it unstable for now | quote: "After some push back, I'm 180'ing. I agree with the general consensus that the interrupt API might not be ready." | practiced_evidence: none
- voice: bugadani | position: needs-to-stay-usable | date: 2025-01-09 | locator: comment 2025-01-09T13:55:03Z | paraphrase: the entry macro must stay usable/stable since without it users cannot write main and thus cannot use the crate at all | quote: "`entry` quite obviously needs to be stable - if you can't write `main`, how would you use the crate?" | practiced_evidence: none

## f002518 — cuda: add opt-in BF16 support for pre-Ampere GPUs (2025-01-07, en)
### Questions
- Q: Should a GPU-targeting Rust crate's build script compile device code (PTX) only for the build host's own compute capability, or build/distribute for multiple architectures to stay portable across heterogeneous multi-GPU systems?
  concepts: build.rs, native/device codegen, portability, GPU targeting; domains_live: ml; positions_seen: compile-for-build-host-only (ivarflakstad), needs-portable-multi-arch-support (haricot, raised as a concern)
- Q: When a contribution bundles many independent changes into one large branch, should maintainers ask for it to be split into small isolated PRs before merging, or review and land the large branch as one unit?
  concepts: contribution review process, PR granularity; domains_live: ml, core; positions_seen: split-into-small-isolated-prs (ivarflakstad)
### Claims
- voice: ivarflakstad | position: compile-for-build-host-only | date: 2025-10-25 | locator: comment 2025-10-25T10:12:19Z | paraphrase: PTX is compiled per-machine via build.rs at build time, not distributed as one binary to all users | quote: "The ptx is compiled for your machine via `build.rs` at compile time. It is not one binary distributed to everyone." | practiced_evidence: https://github.com/huggingface/candle
- voice: haricot | position: needs-portable-multi-arch-support | date: 2025-10-25 | locator: comment 2025-10-25T10:29:20Z | paraphrase: compiling only for the build host's compute capability may break portability across systems with multiple different GPUs | quote: "the current build script only compiles for the compute capacity active on the build host, which may break portability across heterogeneous multi-GPU systems, it seems." | practiced_evidence: none
- voice: ivarflakstad | position: split-into-small-isolated-prs | date: 2026-06-21 | locator: comment 2026-06-21T09:32:07Z | paraphrase: reviewing one huge combined branch is hard and risky; better to treat it as a development hub and extract small isolated PRs for merging | quote: "I think having this branch as the hub where backwards cuda compatibility is developed - and then extract only the required code into isolated PRs is a good way to get the improvements merged." | practiced_evidence: none

## f002538 — Missing `OptionalFromRequestParts` implementation for the `Host` extractor from the axum-extra crate (2025-01-12, en)
### Questions
- Q: When several related query parameters only make sense together, should an extractor treat the whole group as one optional unit (all-or-nothing), or should each field be wrapped in `Option` individually?
  concepts: query extractors, `Option<T>` extractor pattern, request parsing; domains_live: web; positions_seen: grouped-optionality (taladar), field-level-optionality (Turbo87, jplatte)
### Claims
- voice: taladar | position: grouped-optionality | date: 2025-01-14 | locator: comment 2025-01-14T14:21:43Z | paraphrase: when several query params only make sense together, wants to know if all were specified as a group rather than checking several individual Option fields | quote: "Semantically 99% of the time when I even want several query parameters stored in the same value I want to know if all of them have been specified though, not a mess of several `Option` values" | practiced_evidence: none
- voice: Turbo87 | position: field-level-optionality | date: 2025-01-14 | locator: comment 2025-01-14T14:17:35Z | paraphrase: recommends wrapping each query field individually in Option rather than a whole-group optional extractor, since that best reflects how query parameters actually work | quote: "I would recommend to wrap all your query fields with Option instead, since that best reflects reality of how query parameters work." | practiced_evidence: axum-extra (Turbo87 moving OptionalQuery toward deprecation)
- voice: jplatte | position: field-level-optionality | date: 2025-01-14 | locator: comment 2025-01-14T18:44:03Z | paraphrase: has never seen a real case where a set of query parameters is optional as a whole group rather than individually | quote: "I have never seen a set of query parameters that are optional _as a group_, rather than individually." | practiced_evidence: none

## f002542 — Bytecode Alliance Election Results (2025-01-14, en)
### Nothing new
`nothing new` — governance announcement of TSC/Board election results; no contested point, purely a results report.

## f002550 — iroh 0.31.0 - Back At Fighting Fit (2025-01-15, en)
### Nothing new
`nothing new` — release-notes blog post (bug fixes, breaking changes, a `Result`-to-infallible API change stated without argued rationale); no contested decision from a named Voice.
