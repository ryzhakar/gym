# Merged Questions, batch 1, operational grain (merge-v3)

Merger: t4-merge (opus), 2026-09-28. This supersedes `merge-v2/`. Companion files: `merge-v3/crosswalk-b1.csv` and `merge-v3/estimate/closure-b1.md`.

## The grain rule (lead ruling 2026-09-28)

A Question names concrete alternatives a practitioner picks between at one point of work: crates, patterns, language features, project policies.

- A trade-off between Values is a Value conflict carried by Arguments, never a Question. Examples: performance vs simplicity, stopgap vs proper fix, safety vs ergonomics.
- "Choose Rust for X" is one Question per domain X.
- Context variants of one concrete choice stay one Question, with the contexts recorded as Domains and Positions.
- Every multi-member Question below carries a "Grouping" line giving its reason.

This follows the merge check (`merge-check2/merge-check-b1.md`: 54.3% agreement, with 16 GRAIN and 7 HOLD verdicts against merge-v2).

## What changed from merge-v2

Families merge-v2 grouped by value axis are split into their concrete Questions. Where a member is not joined to another member facing the same concrete alternatives, it goes back to its merge-final id.

| merge-v2 family | now | how |
| --- | --- | --- |
| `choose-rust-for-a-domain` | 10 Questions, one per domain | `rust-for-web-frontend` (6 members: Wasm vs JS, fullstack readiness, isomorphic Rust), `rust-for-high-level-apps` (2), `rust-worth-it-for-failure-heavy-infra` (2), and singletons for serverless, multi-tenant runtimes, edge ML, JS tooling, GPU kernels, games, AI-written code. The book adds `rust-for-mlops-vs-python`. b33 is re-homed to a new `rust-for-backend-services-vs-jvm` |
| `ship-stopgap-now-vs-proper-fix` | 10 Questions | each a singleton at its merge-final id: Polonius scope cut, WASI path workaround, web-wasm target, polyfill before spec, pure-Rust crypto, embedded interpreter, expensive feature, ad hoc special case, HAL landed separately, FFI bindings lag |
| `typestate-vs-runtime-checks` | 9 Questions | `hal-driver-typestate` (esp-hal mode and config), `scratch-register-type-enforced` (joined with team b's reading of the same wasmtime comment, the merge check's flag), `typed-wrapper-vs-raw-access` (PAC accessors, plus the book's typed KV accessors and nalgebra newtypes), `encode-invariant-in-representation` (plus Zebra's exhaustive enums), and singletons for crypto-key typestate, ECS edge exclusivity, typed ECS ids, `NonNull`, typed Lambda responses |
| `manual-optimization-vs-simplicity` | 7 singletons | ToTokens temporary, `Cow`, single-pass iteration, scratch buffers, fast paths, lazy forms, boxed futures |
| `ergonomics-vs-explicitness` | 6 Questions | one per language feature: auto-clone, match ergonomics (keeps the id), CoW defaults, implicit indirection, properties, tail expressions |
| `unify-vs-duplicate-implementations`, `design-for-future-now-vs-defer`, `scope-of-rust-safety-guarantees`, `silent-fallback-vs-explicit-error`, `break-vs-preserve-compatibility`, `unstable-feature-gate-vs-wait`, `release-cadence` | their concrete Questions | mostly merge-final ids. Kept together: `memory-safety-and-resource-leaks` (both teams, one post-mortem) and `unstable-feature-gate-vs-wait` (the two iroh releases) |
| `shared-mutable-state-vs-explicit-passing` | 4 Questions | `object-graph-representation`, `trait-api-forced-arc-self` and `ui-state-scoped-lifetimes-vs-runtime-handles` split out, per the merge check's HOLDs |
| `feature-flags-vs-separate-crates` | 2 Questions | `shared-model-crate-vs-domain-split` (how to split, not whether) split out |
| `generated-size-vs-runtime-performance`, `batch-parallelism-strategy`, `roadmap-performance-vs-features`, `dependency-selection-maintenance-quality` | split | value-axis joins, split per the merge check's HOLDs |
| `static-vs-dynamic-dispatch` | 2 Questions | `enum-vs-dyn-trait-closed-set` and `generics-vs-dyn-for-abstraction`: different alternatives |
| `ffi-copy-vs-share` | 4 Questions | serde vs getters, manual vs generated glue, raw Web API types; the copy-vs-share core stays |
| `macro-vs-boilerplate`, `optional-parameters-api-shape`, `extract-single-use-function`, `tower-middleware-vs-handler-helpers`, `human-written-code-standard`, `public-naming-brevity-vs-clarity`, `std-naming-conventions-strictness`, `oop-patterns-in-rust`, `cli-flags-mirror-familiar-tool`, `tracing-crate-vs-otel-api`, `nightly-feature-gating-in-libraries`, `platform-gating-feature-vs-target-cfg`, `borrowed-vs-owned-data` | narrowed | members naming different alternatives go back to their merge-final ids |

Kept as one Question because the alternatives are concrete and the same:
- `library-panic`, `library-error-type-opaque-vs-typed`, `depend-vs-hand-roll`, `replace-battle-tested-c-with-rust`, `serialization-format-choice` (a choice among named formats), `in-app-vs-infrastructure-concern`, `all-rust-vs-platform-native-tooling`, `async-vs-threads`, `lambda-vs-containers`, `default-features-minimal-vs-inclusive`.
- `replace-battle-tested-c-with-rust` keeps its moral, age and bootstrap members as Arguments on the concrete replace-or-reuse choice. The merge check marked that group MISS, which agrees with merge-v2.

## Inputs, parsing and supersession

- **Inputs:** everything merge-v2 read, plus the book pass. That is team a `extract-b1-sB01.md`, `sB02.md` and `sB04.md` (team a's sB03 does not exist), and team b `extract-b1-bk01.md` to `bk03.md`: the async book, the Rust and WebAssembly book, and Zebra.
- **Team b's book pass file names:** the book pass first wrote over team b's original `extract-b1-sb01–sb03.md` and read logs. The originals were restored to disk at 2026-09-28 00:08. They match my parse of 2026-09-27 exactly. The book pass now sits in `bk01–bk03`, and ids use slice `bk`.
- **Supersession, corrected (lead ruling):** saL1 supersedes sa14/sa15 only where it re-logged a Question or Claim (`supersede.txt` in my scratchpad records each case).
  - Dropped as re-logged:
    - a-sa14-f005360-q1, q2, q3
    - a-sa14-f005454-q2
    - a-sa15-f005516-q1, q2, q3
    - Claims a-sa14-f005360-c1, c2, c3, c4, c6 and a-sa14-f005454-c2, each re-logged by saL1 with the same Voice.
  - Restored with their Claims:
    - a-sa14-f005360-q4, "replaced nginx vs removed its role" (pm), now in `in-app-vs-infrastructure-concern`.
    - a-sa14-f005454-q1, OpenAPI code-first (wofo), now in `api-schema-spec-first-vs-code-first`.
    - a-sa14-f005454-q3, handler signature as an async trait (sunshowers), now `api-handler-as-async-trait`.
  - Restored Claims on re-logged Questions:
    - a-sa14-f005360-c5 (yawaramin) goes to a-saL1-f005360-q3.
    - a-sa15-f005516-c1 (Bryan Cantrill) goes to a-saL1-f005516-q1.
- **Carried from merge-v2:**
  - the third-pass strikes (11 dropped; a12, b28, b29, b31 and b33 re-homed);
  - the a10 split;
  - the rule that a capture needs a Question backed by a valid Claim, which again removes 14 team-local Questions (listed below);
  - the four earlier orphans. The book adds one more: a-sB04-f000227-c6 repeats sR01's RTIC async Claim, and there is no Question for it in sB04.

## Counts

- Team-local Questions in the crosswalk: 544 (team a 261, team b 283). The book pass adds 71 (team a 31, team b 40).
- Canonical Questions: 405. 403 have captures, and 2 are carried only by re-homed Claims (`lambda-build-tooling`, `rust-for-backend-services-vs-jvm`). Of the 403: team a only 170, team b only 184, both 49. With more than one member: 77.
- The book pass makes 11 Questions two-team, mostly because both teams read the Rust and WebAssembly book (f000256, a shared sample row): `bounded-grid-universe`, `ffi-copy-vs-share`, `profile-before-optimizing`, `opt-level-z-vs-s`, `unchecked-unwrap-vs-safe-abort`, `generics-vs-dyn-for-abstraction`, `wasm-allocator-choice`, `library-io-factored-out`, `reproduce-wasm-bugs-natively`, `typed-wrapper-vs-raw-access` and `test-via-real-entry-point`.
- Canonical ids: 322 from merge-final, 83 new.
- Claims placed: 768 under team-local Questions, plus 2 re-homed onto Questions with no member. 5 orphans.

## Removed captures (Claim-less, as in merge-v2)

These are removed from the crosswalk because no valid Claim backs them:
- a-02-f000993-q1 and a-02-f000993-q2
- a-sT07-f002226-q1 and a-sT10-f004205-q1
- a-sT11-f007659-q2
- a-sa03-f002356-q1
- b-sT01-f000267-q1
- b-sT05-f002499-q2, b-sT05-f002499-q3, b-sT05-f003044-q1 and b-sT05-f003044-q3
- b-sT09-f005314-q1
- b-sb20-f007290-q3
- b-sb25-f011684-q1

The reasons are the same as in merge-v2's "Removed captures" table. Every new book-pass and restored Question has at least one Claim.

## Crosswalk

- Columns: `batch, stratum, team, source_id, question_id, source_hint, team_local_id`.
- `stratum` is the union of the canonical Question's Domains, per the lead's ruling.
- The crosswalk has 1,103 rows (merge-v2: 1,378). Finer Questions carry fewer unioned Domains.

## Estimate

| stratum | n1 | n2 | m | seen | Chapman N̂ | unseen % | Chao1 N̂ | unseen % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cloud-workers | 30 | 17 | 9 | 38 | 54.8 | 30.7% | 94.3 | 59.7% |
| core | 121 | 123 | 34 | 210 | 431.2 | 51.3% | 575.7 | 63.5% |
| decentralized-iroh | 23 | 28 | 10 | 41 | 62.3 | 34.2% | 63.0 | 34.9% |
| desktop-cli-ui | 29 | 25 | 10 | 44 | 69.9 | 37.1% | 129.3 | 66.0% |
| distributed | 34 | 40 | 15 | 59 | 88.7 | 33.5% | 128.1 | 54.0% |
| embedded | 49 | 37 | 16 | 70 | 110.8 | 36.8% | 188.2 | 62.8% |
| frontend | 15 | 15 | 5 | 25 | 41.7 | 40.0% | 225.0 | 88.9% |
| ml | 21 | 29 | 8 | 42 | 72.3 | 41.9% | 138.1 | 69.6% |
| other | 11 | 17 | 6 | 22 | 29.9 | 26.3% | 59.5 | 63.0% |
| swift-interop | 6 | 4 | 2 | 8 | 10.7 | 25.0% | 20.5 | 61.0% |
| wasm | 43 | 44 | 16 | 71 | 115.5 | 38.5% | 160.3 | 55.7% |
| web | 40 | 29 | 12 | 57 | 93.6 | 39.1% | 145.9 | 60.9% |

- Every stratum FAILs. The two-batch rule (2) and the audit/merge-check rule (3) fail by construction. Rule 4 (at least 10 Questions seen) fails for swift-interop, with 8.
- Against merge-v2, m fell in every stratum (core 41→34, embedded 22→16), and the Chapman unseen fraction rose to 25–51%. The finer grain removes the broad Questions that were propping up m.
- Chao1 stays high because most Questions are singletons (f1 is large).
- Much of the remaining m in `wasm` and `frontend` comes from the one book both teams read, f000256. That is a legitimate recapture: the same sampled source, extracted independently by both teams.

## Groupings I was least sure of

1. `typed-wrapper-vs-raw-access`: it joins PAC register accessors with Zebra's typed KV accessors and nalgebra newtypes.
2. `web-framework-actor-vs-tower`: it joins a course's "Actix by default" with an Axum-vs-Actix comparison, taking the Question to be which framework to default to.
3. `in-app-vs-infrastructure-concern`: now TLS, rate limiting and nginx's operational role.
4. `scratch-register-type-enforced`: the two teams framed one wasmtime comment differently. The adjudicator kept it apart; the merge check flagged it as a lost match.
5. `rust-for-web-frontend`: it holds Wasm-vs-JS performance and fullstack readiness together as one domain.
6. `serialization-format-choice`: one choice among named formats across five constraints.
7. `replace-battle-tested-c-with-rust`: its moral, age and bootstrap Questions are Arguments rather than concrete choices, but they stay here as Positions.

## Canonical Questions

Ordered by: found by both teams first, then by member count, then by id.

### `depend-vs-hand-roll`

**Question.** Should a project take a dependency (a crate, bindings tree, safe-wrapper crate like rustix, or vendor SDK), or hand-roll or vendor its own code to keep the dependency footprint small?

- Grouping: Same concrete choice, dependency or own code; the object and the arguments (control, audit burden, SDK quality) vary.
- Absorbs merge-final ids: `libc-direct-vs-rustix`, `persistent-ds-adopt-crate-vs-hand-roll`, `vendor-sdk-vs-internal-wrapper`
- Teams: a, b · members (context): `a-02-f001053-q1` (f001053, distributed, core); `a-sR06-f002016-q1` (f002016, ml, core); `a-sa04-f002865-q1` (f002865, embedded); `a-sa14-f005079-q2` (f005079, core); `a-sa14-f005079-q3` (f005079, core); `a-saL2-f011092-q3` (f011092, cloud-workers, distributed); `b-sR03-f001160-q1` (f001160, wasm); `b-sR05-f002453-q1` (f002453, decentralized-iroh)
- Domains: cloud-workers, core, decentralized-iroh, distributed, embedded, ml, wasm
- Concepts: persistent/immutable data structures; library adoption; build-vs-buy; supply-chain auditing (`cargo vet`); dependency-tree size; FFI bindings crates; dependency management; intrusive data structures; unsafe code; embedded executors; miri; loom; dependency vendoring; protocol stability; supply chain; unsafe FFI; safe wrapper crates; rustix; vendor SDKs; ecosystem maturity; cloud integrations
- Positions:
  - `depend-vs-hand-roll--take-the-dependency` — Take the existing, tested crate (persistent data structures, an intrusive-list crate, `rustix` over raw libc)
    - **Bojan Serafimov** · Source `f001053` · date 2024-03-01 · locator "Rust Persistent Data Structures (RPDS) to the rescue" / "Conclusion" sections — rather than hand-roll a balanced 2D segment tree with lazy propagation, the team reached for the `rpds` crate to build a copy-on-write layer map, crediting it over more popular alternatives Quote: "There are more popular persistent data structure libraries in Rust, but this one deserves a lot more credit for its clean API, correct results (!!!), and more than good enough performance." [`a-02-f001053-c1`, team a]
    - **jamesmunns** · Source `f002865` · date 2025-04-01 · locator PR comment ("I'd like to try and make the case for keeping the cordyceps dependency!") — argues embassy-executor should keep the `cordyceps` dependency rather than hand-roll/vendor the data structures, citing its miri+loom test coverage, shared usage and maintenance with the `maitake` executor, and tested user APIs that reduce unsafe surface area Quote: "Cordyceps is fairly exhaustively tested, with both miri and loom, which helps to avoid regressions potentially caused by changes." [`a-sa04-f002865-c1`, team a]
    - **alexcrichton** · Source `f005079` · date 2026-09-09 · locator comments 2026-09-09T04:26:50Z; 2026-09-09T04:27:52Z; 2026-09-09T04:28:26Z; 2026-09-09T04:29:20Z — repeatedly suggests replacing raw/manual syscall handling (fcntl, fstat, getsockname, socket options) with the corresponding `rustix` safe-wrapper functions Quote: "Could this use `rustix::io::fcntl_setfd` with error handling?" [`a-sa14-f005079-c4`, team a]
  - `depend-vs-hand-roll--hand-roll-or-vendor` — Keep a hand-rolled or vendored implementation, or a lean internal wrapper over a weak vendor SDK
    - **Dirbaio** · Source `f002865` · date 2025-04-01 · locator PR comment ("Some concerns") — objects to adding `cordyceps` as a dependency for something as foundational as the executor, preferring the data structures stay self-contained and in-tree so the project can change them without cross-repo coordination, keeping the abstraction surface minimal Quote: "I don't think we should add `cordyceps` as a dep, I'd prefer to keep the data structures self-contained for something as foundational as the executor. Having it all in-tree means we can make changes as needed without having to coordinate across repos, and less abstraction means it's clearer what's going on in this case IMO." [`a-sa04-f002865-c2`, team a]
    - **alexcrichton** · Source `f005079` · date 2026-09-08 · locator comment 2026-09-08T14:23:10Z — asks whether the thin crate implementing the systemd listen-fd protocol could just be vendored directly, since the protocol is set externally and unlikely to change much Quote: "The implementation in this crate looks pretty thin -- would it be possible to vendor the implementation here?" [`a-sa14-f005079-c3`, team a]
    - **Luca Casonato** · Source `f011092` · date 2024-02-13 · locator ~00:26:21-00:28:24 — describes the Rust vendor-SDK ecosystem as a weak point — AWS's SDK exists but doesn't retry S3 uploads correctly, GCP has no official Rust SDK (its in-progress one went dormant), Azure's is not yet ready, Stripe has no first-party SDK — so the team builds and maintains its own small internal "mini SDKs" (types plus retry handling) for cloud storage, IAM, secrets, Let's Encrypt, npm registry access, and GitHub Quote: "there's one thing that kind of sucks right now in [Rust] though which is the story around third party integrations and like third party SDKs... our experience with this is that you end up building a lot of little mini SDKs" [`a-saL2-f011092-c3`, team a]
  - `depend-vs-hand-roll--minimize-footprint` — Minimize the dependency footprint even at the cost of uglier code or release cycles; audit burden too high
    - **abrown** · Source `f002016` · date 2024-09-20 · locator PR #9234, comment 2024-09-20T00:30:47Z — posts the full `cargo vet` diff/inspect list generated by the new dependency tree (`tch`, `torch-sys`, `ndarray`, `zip`, `cipher`, etc., some entries thousands of lines) and characterizes the situation as excessive. Quote: "The `cargo vet` situation is a bit much:" [`a-sR06-f002016-c1`, team a]
    - **daxpedda (wasm-bindgen maintainer)** · Source `f001160` · date 2024-04-03 · locator wasm-bindgen/wasm-bindgen#3898, comment 2024-04-03T06:30:56Z. · L2338-L2341. — accept the uglier code; minimizing dependencies matters more. Quote: "This is pretty ugly indeed, but I think it's very important for a library like `wasm-bindgen` to reduce its dependency footprint." [`b-sR03-f001160-c1`, team b]
    - **dignifiedquire (n0-computer/iroh maintainer)** · Source `f002453` · date 2024-12-17 · locator iroh.computer/blog/iroh-0-30-0-slimming-down, 2024-12-17. · L2007-L2097. — actively spend release cycles cutting dependencies ahead of a 1.0 API, even though it means a wave of breaking changes. Quote: "Less is more, simpler is better. This release we focused on cleaning up iroh APIs, streamlining the protocol APIs, and reducing our dependency load!" And: "Irohs dependency load is not the smallest, so while preparing the API for 1.0, we are also trying to reduce the number of required dependencies." [`b-sR05-f002453-c1`, team b]
- Positions seen by the extractor (`a-02-f001053-q1`): adopt-existing-crate (author/Neon), hand-roll-bespoke-structure (same source's own rejected "failed attempt" path)
- Positions seen by the extractor (`a-sR06-f002016-q1`): "the auditing burden from this dependency tree is excessive" (abrown)
- Positions seen by the extractor (`a-sa04-f002865-q1`): adopt-external-tested-dependency (PR author), keep-self-contained-hand-rolled (reviewer)
- Positions seen by the extractor (`a-sa14-f005079-q2`): vendor the implementation directly, since the underlying protocol documented by a third party is unlikely to change and the existing crate's implementation looked thin
- Positions seen by the extractor (`a-sa14-f005079-q3`): prefer a safe-wrapper crate's (`rustix`) equivalent functions over raw manual libc calls, even for small one-off operations
- Positions seen by the extractor (`a-saL2-f011092-q3`): build-lean-internal-wrapper-SDKs (Luca Casonato)
- Positions seen by the extractor (`b-sR03-f001160-q1`): accept the uglier code; minimizing dependencies matters more. (daxpedda (wasm-bindgen maintainer))
- Positions seen by the extractor (`b-sR05-f002453-q1`): actively spend release cycles cutting dependencies ahead of a 1.0 API, even thou (dignifiedquire (n0-computer/iroh maintainer))

### `replace-battle-tested-c-with-rust`

**Question.** Should battle-tested C/C++ code (codecs, TLS, upstream dependencies) be replaced or reimplemented in Rust, or reused?

- Grouping: One concrete choice; the moral, broad-quality, age and bootstrap-trust Questions are Arguments on it, carried as Positions.
- Absorbs merge-final ids: `bootstrap-trust-gap`, `memory-safe-language-moral-imperative`, `old-c-battle-tested-by-age`, `rust-broad-quality-improvement-over-c`
- Teams: a, b · members (context): `a-sa15-f006797-q1` (f006797, core, desktop-cli-ui); `a-saL1-f005516-q2` (f005516, core); `b-bk03-f000267-q1` (f000267, core); `b-sb19-f005743-q1` (f005743, core); `b-sb19-f005743-q4` (f005743, core); `b-sb19-f005964-q1` (f005964, web, core); `b-sb26-f012849-q1` (f012849, core, embedded)
- Domains: core, desktop-cli-ui, embedded, web
- Concepts: memory-safety; ffi; migration; fuzzing; maturity-vs-safety-tradeoff; code age; memory-safety vulnerability provenance; software maintenance; dependency trust; unsafe; rewrite-in-Rust; memory safety; moral framing of tooling choices; economics of open-source maintenance; bootstrappable builds; mrustc; supply-chain trust; Rustls; OpenSSL; BoringSSL; TLS handshake latency; ownership/borrow checking; formal verification
- Positions:
  - `replace-battle-tested-c-with-rust--replace-with-rust` — Replace it; memory safety outweighs the testing record
    - **Federico Mena Quintero** · Source `f006797` · date 2023-12-22 · locator "Se buscan probadores" section — librsvg is dropping gdk-pixbuf's C image decoders in favor of the Rust `image-rs` crate to move the stack off memory-unsafe codecs, while explicitly acknowledging that the incumbent C libraries (libpng, libjpeg-turbo) are heavily tested and continuously fuzzed, and that the Rust decoder crates are comparatively less developed on performance and exotic-format support; frames the migration as an opportunity to find and fix exactly those gaps rather than a claim that the Rust crates are already equally mature Quote: "Digan lo que digan sobre el código sin seguridad de memoria como libpng y libjpeg-turbo, ese código está muy bien probado y se le hace fuzzing todo el tiempo. Los huacales de Rust para decodificar imágenes todavía no están tan bien desarrollados... creo que esta es una buena oportunidad para encontrar exactamente qué es lo que les falta." [`a-sa15-f006797-c1`, team a]
    - **Dirkjan Ochtman** · Source `f005964` · date 2025-05-14 · locator § "What is Rustls?" / "Conclusion" — OpenSSL and its derivatives have a long history of memory-safety vulnerabilities; Rustls now shows roughly 2x lower handshake latency than OpenSSL in their benchmarks, so the field should move off C-based TLS Quote: "It's time for the Internet to move away from C-based TLS." [`b-sb19-f005964-c1`, team b]
  - `replace-battle-tested-c-with-rust--broad-quality-improvement` — A broad quality improvement; pushback is mostly habit
    - **Bruce Perens** · Source `f012849` · date 2026-01-14 (post marked "1mo" at capture) · locator the post itself, paragraphs beginning "I am a better programmer in Rust" and "Over the long term" — after decades writing C/C++ (and Pixar-internal languages), Perens states Rust keeps him from an entire class of mistakes that were too easy to make in any language without garbage collection, and dismisses pushback against Rust as belly-aching from people too attached to what they've used for decades Quote: "I am a better programmer in Rust for anything low-level or high-performance. It just keeps me from making an entire class of mistakes that were too easy to make in any language without garbage-collection." [`b-sb26-f012849-c1`, team b]
  - `replace-battle-tested-c-with-rust--age-means-battle-tested` — Old C is more optimized and reliable for its age
    - **tumdum** · Source `f005516` · date 2025-06-10 · locator reply, 2025-06-10T07:41:05-05:00 — Cites a Google security-blog study on Android finding most memory-safety vulnerabilities live in recently changed code, taking this as support for older code tending to have fewer bugs. Quote: "it was shown that old code has less bugs" [`a-saL1-f005516-c6`, team a]
  - `replace-battle-tested-c-with-rust--only-maintenance-improves-code` — Age alone does not improve code; maintenance does
    - **hsivonen** · Source `f005516` · date 2025-06-10 · locator reply, 2025-06-10T00:43:48-05:00 and 2025-06-10T10:38:09-05:00 — Rejects the "old codebases are more optimized/battle-tested" meme as false in general — it depends on whether someone actually spent time optimizing or fuzzing; his own encoding_rs (a Rust crate) beat glibc's iconv because of iconv's fundamentally slow architecture, and unfuzzed "battle-tested" old code can still hide bugs the first real fuzzer finds. Quote: "The meme that old codebases are more optimized... really annoys me. It depends on whether someone has taken the time to optimize performance." [`a-saL1-f005516-c7`, team a]
    - **fanf** · Source `f005516` · date 2025-06-10 · locator reply, 2025-06-10T07:57:08-05:00 — Reframes the cited Google study's takeaway as being about active use and maintenance reducing bugs over time, not the simple passage of time. Quote: "The takeaway from that Google study should be that code gets less buggy due lots of active use and maintenance. The simple passage of time does not fix bugs." [`a-saL1-f005516-c8`, team a]
  - `replace-battle-tested-c-with-rust--reject-moral-framing` — Not a moral imperative; an economic choice
    - **toastal** · Source `f005743` · date 2026-06-02 · locator comment at 2026-06-02T12:14:03-05:00 — escalating "moral imperative" logic could equally be used to demand replacing Rust itself with something formally stronger, which shows the framing proves too much Quote: "We must abolish Rust for something stronger with proofs. This is a moral imperative. /s" [`b-sb19-f005743-c1`, team b]
    - **alandekok** · Source `f005743` · date 2026-06-02 · locator comment at 2026-06-02T12:36:53-05:00 — correctness/safety outcomes are driven by who funds the work, not by language choice alone; citing unfunded xz-utils maintenance Quote: "Correctness and safety is an _economic_ choice.  No one is funding fixes to xz utils.  Yet people are making millions of dollars off of it." [`b-sb19-f005743-c2`, team b]
    - **mtset** · Source `f005743` · date 2026-06-02 · locator comment at 2026-06-02T14:37:20-05:00 — there are genuine moral imperatives in the industry, but language choice isn't one of them Quote: "There are many real moral imperatives in our industry; Rust isn't one." [`b-sb19-f005743-c3`, team b]
  - `replace-battle-tested-c-with-rust--bootstrap-undermines-case` — The bootstrap trust gap undermines the safety argument
    - **jackdk** · Source `f005743` · date 2026-06-02 · locator comment at 2026-06-02T17:16:20-05:00 — language-level memory safety is moot if the compiler's own bootstrap chain can't be trusted; would make avoiding Rust (until bootstrapping is fixed, e.g. keeping mrustc close to mainline) the "moral imperative" by the same logic Quote: "all the language-level memory safety cannot help you because your compiler itself could be compromised" [`b-sb19-f005743-c8`, team b]
  - `replace-battle-tested-c-with-rust--safety-not-enough` — Memory safety is far from enough; model checking needed
    - **Justin Handville** · Source `f012849` · date 2026-01-14 · locator comment, "1mo" — states plainly that Rust "isn't nearly enough" on its own, and that whichever language you use, you should pair it with a model checker — CBMC for C, Kani for Rust, SPARK for Ada — rather than treat the language choice itself as the safety question Quote: "There's far more to writing safe software than memory safety. Rust isn't nearly enough. Any conversation about writing safer software should talk about model checking." [`b-sb26-f012849-c2`, team b]
  - `replace-battle-tested-c-with-rust--narrow-niche` — Rust's legitimate niche is narrow
    - **Pavel Perikov** · Source `f012849` · date 2026-01-14 · locator comment, "1mo" — contrasts what Perikov calls "Rust evangelists coming from Python or JS" with Perens's C/C++ background, framing Rust's proper role as displacing C specifically in very-low-level/constrained work, while judging its contribution to OS kernel development as minor ("almost nothing... but still some progress") Quote: "Finally Rust finds its niche: replace C. The only niche it belongs to: very low level programming and constrained environments." [`b-sb26-f012849-c3`, team b]
  - `replace-battle-tested-c-with-rust--p1` — rust-by-default-with-pragmatic-c-exceptions
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Design Overview § Desiderata — Zebra and its dependencies should be implemented in Rust as much as reasonably possible, but pragmatic exceptions apply — e.g. it doesn't make sense to rewrite libsecp256k1 in Rust when the same upstream library Bitcoin uses is already available Quote: "it probably doesn't make sense to rewrite libsecp256k1 in Rust, instead of using the same upstream library as Bitcoin" (flag: voice-unverified) [`b-bk03-f000267-c1`, team b]
- Positions seen by the extractor (`a-sa15-f006797-q1`): prioritize-memory-safety-despite-lower-maturity
- Positions seen by the extractor (`a-saL1-f005516-q2`): age-correlates-with-optimization-and-reliability; age-itself-does-not-improve-code-only-active-maintenance-does
- Positions seen by the extractor (`b-bk03-f000267-q1`): rust-by-default-with-pragmatic-c-exceptions
- Positions seen by the extractor (`b-sb19-f005743-q1`): reject-moral-framing (toastal, mtset, alandekok, duncan_bayne, hobbified), economic-choice (alandekok)
- Positions seen by the extractor (`b-sb19-f005743-q4`): bootstrapping-undermines-safety-argument (jackdk)
- Positions seen by the extractor (`b-sb19-f005964-q1`): replace-c-tls-with-rust (Dirkjan Ochtman)
- Positions seen by the extractor (`b-sb26-f012849-q1`): an unambiguous, long-term-winning quality improvement, with pushback against it "mostly substance-free" (Bruce Perens); memory safety alone is not enough — safer software requires model checking/formal verification regardless of language (Justin Handville, naming CBMC for C, Kani for Rust, SPARK for Ada); Rust's real niche is narrow — "very low level programming and constrained environments," with little value added for something like OS kernels specifically (Pavel Perikov)

### `ai-authored-community-contributions`

**Question.** Should a Rust project or venue accept AI-authored contributions and content (proposals, PRs, newsletters), and under what policy: ban, disclosure, accountability or review?

- Grouping: One project-policy choice with the same alternatives; forum, PR, mentoring and newsletter are contexts.
- Absorbs merge-final ids: `ai-generated-community-prose`
- Teams: a, b · members (context): `a-sa29-f013224-q2` (f013224, core); `b-bk03-f000267-q6` (f000267, core); `b-sR11-f004993-q1` (f004993, core); `b-sR13-f009740-q1` (f009740, core); `b-sb15-f004721-q1` (f004721, wasm, core); `b-sb20-f007942-q1` (f007942, other)
- Domains: core, other, wasm
- Concepts: AI-generated content; forum norms; authenticity/tone; moderation rules; AI-assisted development; code review; contributor accountability; AI-assisted Rust; contribution norms; AI-assisted contribution norms; governance; code review process; AI-assisted/machine-written content; community norms
- Positions:
  - `ai-authored-community-contributions--reject-ai-authored-content` — Undesirable: it erases the author's voice, or readers do not want it
    - **jdahlstrom** · Source `f013224` · date 2024-03-04T12:46:37Z · locator forum posts 2024-03-02T18:18:23.273Z and 2024-03-04T12:46:37.433Z — identifies the original proposal's style as obviously LLM-written and, when the author defended the practice, says he'd be more impressed if the message hadn't read as ">90% written by ChatGPT" prompted toward a predetermined conclusion Quote: "It has such an obvious style that I can't even imagine the amount of eye-rolling going on amongst teachers and TAs grading student work these days" [`a-sa29-f013224-c4`, team a]
    - **Rust GameDev Working Group** · Source `f007942` · date 2024-06-05 · locator section "Survey Results #" — after surveying 52 readers on how to improve the newsletter, the WG reports that readers are generally positive about it, are content with its frequency, but explicitly do not want anything in it generated by AI Quote: "Readers do not want anything in the newsletter generated by AI." [`b-sb20-f007942-c1`, team b]
  - `ai-authored-community-contributions--acceptable-if-substance-is-own` — Acceptable when the substance is the contributor's own and the model only composes
    - **jasn-armstrng** · Source `f013224` · date 2024-03-04T13:47:53Z · locator forum post, 2024-03-04T13:47:53.039Z — defends having used an LLM to write the original post, explaining that writing this kind of communication isn't a personal strength, that he supplied the points himself, and seeing no issue with that division of labor Quote: "I gave it my points and it did the rest. Why would you assume that my thought process and prompt was that casual?" [`a-sa29-f013224-c5`, team a]
  - `ai-authored-community-contributions--acceptable-if-marked` — Assistance is fine; unmarked AI content is the problem
    - **steffahn** · Source `f013224` · date 2024-03-04T13:26:21Z · locator forum post, 2024-03-04T13:26:21.593Z — cites the forum's rules against machine-generated content, noting clearly marked AI content rarely causes trouble, while unmarked, low-effort AI spam is what the rule is meant to prevent Quote: "clearly marked AI-generated content is generally not going to bring you into much of any trouble" [`a-sa29-f013224-c6`, team a]
  - `ai-authored-community-contributions--human-must-stay-accountable` — Acceptable only with the human author in the loop and accountable, per project policy
    - **alexcrichton** · Source `f004721` · date 2026-05-23 · locator PR #13459, comment 2026-05-23T15:42:24Z — tells the PR author to read the Bytecode Alliance's AI tool use policy, flags that the PR description reads as a large wall of AI-generated text, and stresses the author must stay personally in the loop on all communication because they own and are responsible for the change Quote: "Notably this looks like a very large wall of text generated by an AI. Please ensure that you are yourself in the loop on all communication because you, after all, own this change and are responsible for it." [`b-sb15-f004721-c1`, team b]
  - `ai-authored-community-contributions--manage-through-review-not-ban` — A real problem, but managed through review and policy, not a ban
    - **Carter Anderson (@cart, Bevy creator and Project Lead)** · Source `f004993` · date 2026-08-10 · locator "AI Policy #" section — the strict "no-AI" policy adopted this year "solved many problems but created many others" (toxic witch hunts, incentivized lying to maintainers, unenforceable), so the community (led by @alice-i-cecile) is drafting a replacement Quote: "solved many problems but created many others (including fostering toxic witch hunts, incentivizing lying to maintainers, enforcement was a hard / impossible task)" [`b-sR11-f004993-c1`, team b]
    - **Jakub Beránek, on behalf of the Rust Project mentorship team** · Source `f009740` · date 2026-04-30 · locator paragraph on the 96 submitted proposals — "Like many other GSoC organizations this year, we somewhat struggled with some AI-generated proposals and low-quality contributions generated using AI agents, but it stayed manageable." Quote: "we somewhat struggled with some AI-generated proposals ... but it stayed manageable" [`b-sR13-f009740-c1`, team b]
  - `ai-authored-community-contributions--p1` — welcome-with-disclosure-and-accountability
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Contributing § AI-Assisted Contributions — Zebra welcomes AI-assisted contributions; what matters is the quality of the result and the contributor's own understanding of it, not whether AI was involved, provided AI usage is disclosed in the PR description and the human contributor remains the sole responsible author, able to explain the logic and trade-offs of every change Quote: "What matters is the quality of the result and the contributor's understanding of it, not whether AI was involved." (flag: voice-unverified) [`b-bk03-f000267-c6`, team b]
- Positions seen by the extractor (`a-sa29-f013224-q2`): acceptable when the substance/points are the poster's own and the LLM only handles composition (jasn-armstrng, defending the OP) vs. objectionable because it erases the poster's voice/tone and reads as argument-first rationalization (jdahlstrom; 2e71828) vs. rule-based middle position: unmarked AI content is the problem the forum's rules target, clearly marked AI content is broadly tolerated (steffahn, citing the forum's own rules against machine-generated content)
- Positions seen by the extractor (`b-bk03-f000267-q6`): welcome-with-disclosure-and-accountability
- Positions seen by the extractor (`b-sR11-f004993-q1`): strict no-AI policy tried and being revised; personal anti-AI stance
- Positions seen by the extractor (`b-sR13-f009740-q1`): treat it as a real but manageable quality-control problem, rather than grounds for an outright ban
- Positions seen by the extractor (`b-sb15-f004721-q1`): human-must-stay-in-the-loop-per-policy
- Positions seen by the extractor (`b-sb20-f007942-q1`): readers surveyed by the Rust GameDev newsletter reject AI-generated newsletter content (Rust GameDev Working Group, reporting a reader survey)

### `feature-flags-vs-separate-crates`

**Question.** Should functionality live in one crate (feature flags, in-tree, a monolithic binary) or in separate, independently usable crates?

- Grouping: Same one-crate-vs-split choice; the Bevy shared-model-crate Question (how to split) stays apart.
- Absorbs merge-final ids: `modular-engine-vs-monolithic`, `repository-layer-sub-crates`, `young-integration-in-tree-vs-out-of-tree`
- Teams: a, b · members (context): `a-sR13-f004685-q2` (f004685, decentralized-iroh, core); `a-sa18-f008651-q1` (f008651, web, core); `b-bk03-f000267-q3` (f000267, core, distributed); `b-sR05-f002151-q1` (f002151, wasm); `b-sR12-f005120-q1` (f005120, ml, core); `b-sb25-f011435-q1` (f011435, web)
- Domains: core, decentralized-iroh, distributed, ml, wasm, web
- Concepts: crate structure; modularity; release cadence; repository-pattern; hexagonal-architecture; sqlx; workspace-crate-boundaries; encapsulation; workspace organization; crate boundaries; scope discipline; workspaces; crate splitting; feature flags; compile/link footprint; browser engine architecture; Servo; Ladybird; trait boundaries between crates
- Positions:
  - `feature-flags-vs-separate-crates--split-into-crates` — Split into separate crates or modular crates joined by traits
    - **iroh/n0 (Friedel Ziegelmayer & Rüdiger Klaehn, post authors)** · Source `f004685` · date 2026-05-11 · locator § "Sometimes things have to move out" — `DhtAddressLookup`, `MdnsAddressLookup` and `AccessLimit` were moved out of the `iroh` crate into their own crates/repos to allow independent versioning and release schedules and to reduce the number of optional features in the main crate Quote: "This allows us to have a different versioning and release schedule for these components. It is also helpful to reduce the number of optional features in iroh." [`a-sR13-f004685-c2`, team a]
    - **Michael de Silva** · Source `f008651` · date 2025-10-19 · locator "Another 'abstraction' to the repository layer" section — splits Postgres access into per-domain sub-crates (e.g. `accounts`, `payments`) behind an `interfaces` crate, arguing this keeps sub-crate public APIs stable (they only deal in primitive types) while the repository-facing types can change freely, and lets the Postgres stack be shared with another engineer decoupled from the host Axum app; explicitly flags this against a critique ("daymare was just commenting on the need for constant abstractions") without fully rebutting it, and closes by asking readers whether this is extreme Quote: "the sub-crates only care about primitive types... types used by the repository interface can change (as much as they need to), without impacting the sub-crate API." [`a-sa18-f008651-c1`, team a]
    - **benwis (Leptos maintainer)** · Source `f002151` · date 2024-10-06 · locator leptos-rs/leptos#3063, comment 2024-10-06T02:05:17Z. · L1097-L1100. — keep new integrations out of the main crates. Quote: "We're keeping most new integrations out of the main crates to reduce the time needed to release a new feature." [`b-sR05-f002151-c1`, team b]
    - **Arthur Zucker / Hugging Face tokenizers team** · Source `f005120` · date 2026-09-21 · locator table row "workspace split" / "Progress Towards V1" — the single tokenizers crate became a workspace so `tk-encode` is the only required runtime piece and `tk-serialize`, `tk-convert`, `tk-train` are linked only when an application actually needs them Quote: "one crate became a workspace: tk-encode is the required runtime, and tk-serialize, tk-convert and tk-train are linked only when an application needs them." [`b-sR12-f005120-c1`, team b]
    - **Nico (Blitz/Dioxus Labs; maintains Servo-adjacent Blitz, Taffy, blessed.rs)** · Source `f011435` · date 2026-06-11 · locator ~10:14-11:16 — after contributing modularity work to Servo and getting "do we have to do this?" rather than buy-in, he concluded a separate project was needed; Blitz is built around a small core (BlitzDom: DOM tree, layout, styling) with everything else — rendering, HTML parsing, networking, windowing — behind traits as swappable/reusable pieces Quote: "I was getting a lot of more like do we have to do this?" [`b-sb25-f011435-c1`, team b]
  - `feature-flags-vs-separate-crates--p1` — modular-library-first
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Design Overview § Architecture; Contributing § Pull Requests — in contrast to zcashd's monolithic architecture inherited from its Bitcoin Core fork origins, Zebra is factored into independently reusable library crates (zebra-chain, zebra-network, zebra-state, etc.) so each can be reused outside the zebrad full node; the contributing guide names this as a scope boundary — Zebra stays a minimal validator node and pushes wallets, explorers, and mining pools to separate projects (Zaino, Zallet, librustzcash) Quote: "Zebra has a modular, library-first design, with the intent that each component can be independently reused outside of the zebrad full node" (flag: voice-unverified) [`b-bk03-f000267-c3`, team b]
- Positions seen by the extractor (`a-sR13-f004685-q2`): split-into-separate-crates (iroh)
- Positions seen by the extractor (`a-sa18-f008651-q1`): crate-boundary-abstraction-pays-for-itself
- Positions seen by the extractor (`b-bk03-f000267-q3`): modular-library-first
- Positions seen by the extractor (`b-sR05-f002151-q1`): keep new integrations out of the main crates. (benwis (Leptos maintainer))
- Positions seen by the extractor (`b-sR12-f005120-q1`): split-into-workspace
- Positions seen by the extractor (`b-sb25-f011435-q1`): modularity should be a first-class design goal, accepting smaller scope/feature gaps in exchange for reusable pieces (Blitz); modularity is secondary to shipping a complete monolithic engine, added only where a component happened to already be separable (Servo, as the author experienced trying to push it there)

### `library-error-type-opaque-vs-typed`

**Question.** Opaque (`anyhow`) or concrete typed (`thiserror`/`snafu`) error types, and do typed errors need an opaque wrapper for logged context?

- Grouping: Same concrete crate-level choice across library, application and logging contexts.
- Absorbs merge-final ids: `thiserror-display-loses-context`
- Teams: a, b · members (context): `a-sa14-f005149-q1` (f005149, core); `a-sa18-f008583-q1` (f008583, cloud-workers, core); `a-saL2-f011092-q6` (f011092, core); `b-sb10-f003188-q2` (f003188, distributed, decentralized-iroh); `b-sb10-f003222-q1` (f003222, distributed, decentralized-iroh); `b-sb21-f008583-q1` (f008583, cloud-workers, core)
- Domains: cloud-workers, core, decentralized-iroh, distributed
- Concepts: error handling; anyhow vs thiserror; backtrace propagation; error-handling; thiserror; anyhow; eyre; tracing; structured-logging; structured errors; `anyhow` vs `thiserror`/`snafu`; concrete vs opaque error types; alternate Display format; error-context propagation
- Positions:
  - `library-error-type-opaque-vs-typed--concrete-typed-errors` — Concrete, enumerable error types over `anyhow`
    - **ramfox** · Source `f003188` · date 2025-06-27 · locator "💥 Concrete Errors 💥" section / Breaking Changes list — all iroh public APIs now return concrete error types instead of anyhow::Error, a large change touching most of the codebase Quote: "all public APIs return concrete error types, rather than anyhow::Error" [`b-sb10-f003188-c2`, team b]
    - **rklaehn** · Source `f003222` · date 2025-07-04 · locator "Errors" section — iroh-blobs has vastly reduced its use of anyhow, switching to the snafu crate for concrete errors with backtraces and span traces Quote: "Compared to the old blobs, we have vastly reduced the usage of anyhow for errors. Instead we use the snafu crate to provide concrete errors, with some additional features like backtraces and span traces." [`b-sb10-f003222-c1`, team b]
  - `library-error-type-opaque-vs-typed--hybrid-snafu` — A hybrid with automatic backtraces (snafu)
    - **dig, b5, and ramfox (iroh team)** · Source `f005149` · date 2025-08-22 · locator § Enter Snafu: The Hybrid Approach — after experimenting with both dominant approaches, settle on snafu because it gives enum-based precision like thiserror plus automatic backtrace capture per variant, working around the `Into`-trait conflict that otherwise forces a choice between ergonomic `?` and backtraces Quote: "Snafu is essentially thiserror on steroids... Automatic backtrace capture when constructing error variants" [`a-sa14-f005149-c1`, team a]
  - `library-error-type-opaque-vs-typed--typed-over-time` — Move toward typed errors as the codebase matures; keep `anyhow` for some things
    - **Luca Casonato** · Source `f011092` · date 2024-02-13 · locator ~00:48:46 (Q&A) — reflecting on lessons learned building Deno, says he started out happily using anyhow for error handling broadly, but over time came to see well-structured, typed error handling as far more valuable, while noting they still use anyhow for some things Quote: "I gained... an appreciation for very robust error handling... in the beginning I was very happy to use... anyhow for many things and we still do use anyhow for things but... as time went on I realized... having really structured errors is something that's super super valuable" [`a-saL2-f011092-c6`, team a]
  - `library-error-type-opaque-vs-typed--wrap-in-anyhow-for-context` — For logged context, wrap typed errors in `anyhow`/`eyre`
    - **Tomas Tauber** · Source `f008583` · date 2025-09-02 · locator "Error logging" section — recommends logging errors with the alternate `{:#}` display because it preserves the full source-error chain (e.g. AWS SDK's `Unhandled` variants), and flags that `thiserror` currently only supports the default `{}` format, losing that context, so the workaround is to wrap errors in `anyhow` or `eyre` which support the alternate display Quote: "The thiserror crate currently only supports the default {} display format, which loses the error context. One workaround for this is to wrap the errors in anyhow or eyre that support the alternate display format." [`a-sa18-f008583-c1`, team a]
    - **Tomas Tauber** · Source `f008583` · date 2025-09-03 · locator § "Error logging" — `thiserror` currently only supports the default `{}` Display format and loses error context (e.g. AWS SDK's `Unhandled` variant losing the underlying resource info); wrapping errors in `anyhow` or `eyre` recovers the alternate `{:#}` display that carries full context Quote: "The thiserror crate currently only supports the default {} display format, which loses the error context. One workaround for this is to wrap the errors in anyhow or eyre that support the alternate display format." [`b-sb21-f008583-c1`, team b]
- Positions seen by the extractor (`a-sa14-f005149-q1`): neither extreme — a hybrid (snafu: enum-based precision with automatic backtrace capture at each variant) as a practical middle path between anyhow's ergonomics and thiserror's precision
- Positions seen by the extractor (`a-sa18-f008583-q1`): alternate-display-plus-anyhow-eyre-needed-for-full-context
- Positions seen by the extractor (`a-saL2-f011092-q6`): move-toward-structured-errors-over-time (Luca Casonato), still-uses-anyhow-for-some-things (Luca Casonato, hybrid in practice)
- Positions seen by the extractor (`b-sb10-f003188-q2`): concrete-errors-over-anyhow (ramfox)
- Positions seen by the extractor (`b-sb10-f003222-q1`): concrete-errors-over-anyhow (rklaehn)
- Positions seen by the extractor (`b-sb21-f008583-q1`): thiserror-insufficient-wrap-in-anyhow-or-eyre (Tomas Tauber)

### `library-panic`

**Question.** On invalid input or a violated precondition, panic (`unwrap`, documented panics) or return `Result`?

- Grouping: Same panic-vs-Result choice; libraries, HAL constructors, numeric ops and production code are contexts.
- Absorbs merge-final ids: `hal-constructor-result-vs-panic`, `runtime-checkable-precondition-result-vs-unsafe`, `unwrap-in-production`
- Teams: a, b · members (context): `a-sa06-f003414-q3` (f003414, core); `a-sa09-f004055-q3` (f004055, embedded, core); `a-sa21-f011069-q3` (f011069, core); `b-sR10-f004573-q1` (f004573, ml, core); `b-sR12-f005421-q1` (f005421, core, embedded); `b-sb05-f001512-q1` (f001512, embedded)
- Domains: core, embedded, ml
- Concepts: error handling; panics; error-handling; unsafe; API-design; control flow; docs-as-contract; library design guarantees; embedded HAL API design
- Positions:
  - `library-panic--never-panic-return-result` — Return `Result`; constructors and runtime-checkable conditions return errors
    - **jamesmunns** · Source `f004055` · date 2026-01-05 · locator comment @jamesmunns 2026-01-05T14:16:51Z — questions why a memory-transfer function is `unsafe` and an `assert` was reintroduced in place of a `Result`; proposes a fallible `try_` variant with a panicking convenience wrapper on top Quote: "why did you remove the Result and switch it back to an assert? If we're going to do that, I'd prefer to have a try_transfer_mem_to_mem that returns a Result and have the main transfer_mem_to_mem just call that with an unwrap." [`a-sa09-f004055-c6`, team a]
    - **bogdan-petru** · Source `f004055` · date 2026-02-05 · locator comment @bogdan-petru 2026-02-05T01:10:05Z — converges by making the memory-transfer function safe, returning `Result<Transfer<'_>, Error>` with runtime validation that the source/destination buffers are DMA-accessible Quote: "Safe function: mem_to_mem() is now a safe function (not unsafe)... Returns Result: It returns Result<Transfer<'_>, Error> instead of using asserts... Returns Error::BufferNotAccessible if validation fails." [`a-sa09-f004055-c7`, team a]
    - **Rhai project (rhaiscript maintainers)** · Source `f005421` · date 2025-01-17 · locator README section "Protected against attacks", sub-item "_Don't Panic_ guarantee" — Rhai treats any panic reaching the host application as a bug in Rhai itself, not an acceptable outcome, and is coded under that guarantee Quote: "_Don't Panic_ guarantee - Any panic is a bug. Rhai subscribes to the motto that a library should never panic the host system, and is coded with this in mind." [`b-sR12-f005421-c1`, team b]
    - **MabezDev** · Source `f001512` · date 2024-06-11 · locator comment 2024-06-11T10:24:37Z — constructors should return Result rather than unwrap/panic internally Quote: "We shouldn't unwrap here, let's make new and friends fallible I think" [`b-sb05-f001512-c1`, team b]
  - `library-panic--no-ad-hoc-panics` — No ad hoc panics; only control-flow-contingent ones
    - **Aleksandr Petrosyan** · Source `f011069` · date 2023-11-15 · locator ~00:32:20-00:32:40 — Used a panic as an ad hoc short-circuit to bail out of a search after too long, but states he considers ad hoc panics bad practice, preferring panics reserved for specific cases tied to control flow — while explicitly flagging that other Rust practitioners may disagree with him. Quote: "I don't think that having ad hoc panics in your code is a good idea... maybe experts of about Rust will tell me otherwise, but I don't like panics in my code which are ad hoc." [`a-sa21-f011069-c5`, team a]
  - `library-panic--unwrap-only-in-tests` — `unwrap` only in tests or provably safe spots
    - **ConradIrwin** · Source `f003414` · date 2025-10-28 · locator comment 2025-10-28T01:59:12Z — flags new `unwrap()`s as needing early returns instead, with unwrap acceptable only in tests or where the current function makes panics provably impossible Quote: "unwrap is OK in tests and also when you can tell by reading the current function that it can't ever unwrap" [`a-sa06-f003414-c3`, team a]
  - `library-panic--prevent-via-explicit-check` — Prevent the invalid case with an explicit check
    - **softmaximalist (PR author, burn contributor)** · Source `f004573` · date 2026-04-19 · locator PR review comment, 2026-04-19T18:47:03Z — rather than let a quantized input fail deep inside LU decomposition, add an explicit TensorCheck that rejects it up front with a clear message Quote: "Hence, I have added a tensor check to reject a quantized input tensor." [`b-sR10-f004573-c2`, team b]
  - `library-panic--panic-fine-if-documented` — Panicking is fine if documented
    - **antimora (Tracel AI / burn maintainer)** · Source `f004573` · date 2026-04-21 · locator PR review comment, 2026-04-21T14:39:58Z — the QFloat panic path is acceptable but must be listed in the function's `# Panics` docs so a user isn't surprised by it Quote: "The `# Panics` list should include the QFloat case (added in the new `TensorCheck::det` at check.rs:1403-1409). Right now a user hitting it gets a panic with no heads-up from the docs." [`b-sR10-f004573-c1`, team b]
- Positions seen by the extractor (`a-sa06-f003414-q3`): early-return instead of `unwrap()` except in tests or when the current function makes non-panic provable by inspection
- Positions seen by the extractor (`a-sa09-f004055-q3`): safe-result-returning-api, unsafe-or-panicking-api
- Positions seen by the extractor (`a-sa21-f011069-q3`): no-ad-hoc-panics-only-control-flow-contingent
- Positions seen by the extractor (`b-sR10-f004573-q1`): panic-is-fine-if-documented, prevent-via-explicit-check
- Positions seen by the extractor (`b-sR12-f005421-q1`): never-panic (this source), panic-is-fine-if-documented (burn, prior batch), prevent-via-explicit-check (burn, prior batch)
- Positions seen by the extractor (`b-sb05-f001512-q1`): fallible-constructors (MabezDev)

### `rust-for-web-frontend`

**Question.** Should browser and frontend code be written in Rust (Wasm, fullstack frameworks) rather than JavaScript/TypeScript?

- Grouping: One domain, web frontends: Rust/Wasm vs JS performance, fullstack readiness and isomorphic Rust are contexts of the same choice.
- Absorbs merge-final ids: `isomorphic-rust-vs-js-frontend`, `wasm-vs-js-performance`
- Teams: a, b · members (context): `a-sa26-f011460-q1` (f011460, wasm, frontend, web); `a-sa26-f011460-q2` (f011460, wasm, frontend); `a-sa26-f012146-q1` (f012146, web, frontend); `b-sR01-f000256-q1` (f000256, wasm, frontend, web); `b-sb19-f005699-q1` (f005699, wasm, frontend); `b-sb20-f007290-q1` (f007290, frontend, wasm)
- Domains: frontend, wasm, web
- Concepts: WebAssembly; JavaScript performance; FFI; FFI design; string marshaling; application frameworks; isomorphic client/server code; garbage collection/runtime overhead; JS interop; binary size; wasm-bindgen boundary cost; serde-wasm-bindgen; JIT compilation; algorithmic complexity vs language choice; WASM frontend; server-side rendering; hydration; hot patching; DWARF debugging
- Positions:
  - `rust-for-web-frontend--rust-wasm-over-js-broadly` — Rust/Wasm beats JS broadly, even for small string-heavy functions; small size and incremental adoption
    - **Andrew Jakubowicz and co-presenter (Canva)** · Source `f011460` · date 2026-06-11 · locator ~01:10 — articles claiming Rust FFI is too slow, that Wasm should be reserved for the heaviest compute, and that JavaScript is fast enough, are myths the talk sets out to bust with benchmarks Quote: "we're going to be sharing how to design your Rust FFI so that it's fast... Rust and WebAssembly can be blazingly fast for a variety of applications... and that JavaScript is not always fast enough" [`a-sa26-f011460-c1`, team a]
    - **co-presenter ("Taj"/"Touch"/unclear)** · Source `f011460` · date 2026-06-11 · locator ~18:28-19:29 — after hand-optimizing a hex-color-parsing function (pre-allocating memory, skipping UTF-16→UTF-8 conversion, packing bits), the Wasm version beat the JavaScript control by roughly 2x despite the function being "very hostile" to Wasm (string copy, minimal computation, allocation on return) Quote: "if WebAssembly is competitive here, then maybe the blanket advice to use WebAssembly on only heavy compute is too simple" [`a-sa26-f011460-c2`, team a]
    - **Rust and WebAssembly Book (rustwasm.github.io, unmaintained)** · Source `f000256` · date undated (living document) · locator chapter "Why Rust and WebAssembly?" § "Low-Level Control with High-Level Ergonomics" — JS's dynamic typing and GC pauses make Web performance unreliable; Rust gives low-level control without that non-determinism, ships no runtime so .wasm stays small, and lets teams port only hot-path JS functions rather than rewrite everything. Quote: "Rust gives programmers low-level control and reliable performance." [`b-sR01-f000256-c1`, team b]
  - `rust-for-web-frontend--rust-wasm-compute-bound-only` — Rust/Wasm only for compute-bound work with minimal interop
    - **Thesys Engineering Team** · Source `f005699` · date 2026-03-20 · locator § "When WASM Actually Helps" / "Key Takeaways" — WASM wins only for compute-bound work with rare boundary crossings (image/video, crypto, physics, porting existing C/C++ libs); it loses for parsing structured text into JS objects and for frequently-called functions on small inputs, because the serialization/boundary tax dominates and V8's JIT closes the raw-compute gap Quote: "The Rust parsing itself was never the slow part. The overhead was entirely in the boundary" [`b-sb19-f005699-c1`, team b]
  - `rust-for-web-frontend--isomorphic-rust-web` — A unified isomorphic Rust client/server model over server MVC plus a JS frontend
    - **unidentified reviewer** · Source `f012146` · date 2024-10-09 · locator ~07:06-08:07 — while Loco replicates Rails's batteries-included scaffolding (CLI generators, DB migrations, auth out of the box) and defaults to a separate React frontend, Leptos instead lets a developer define server functions callable directly from client code, with the client/server interface auto-generated, and lets logic move between client and server "almost effortless[ly]" Quote: "leptos is my absolute favorite way to build web applications these days so I'm a little biased... what lepos does have though is a lot more flexibility on whether you'd like a given piece of logic to run on the browser or on the server" [`a-sa26-f012146-c1`, team a]
  - `rust-for-web-frontend--not-yet-for-frontend` — Not yet for frontends: Rust backend, TypeScript frontend
    - **fasterthanlime** · Source `f007290` · date 2025-11-22 · locator section "Does Dioxus spark joy?" — after using Dioxus for a real project, the verdict is "not yet" — it is still unpleasant compared to the author's Svelte 5 "gold standard," even though the author is excited about the trajectory Quote: "In the meantime, I'll be doing Rust on the backend, and TypeScript on the frontend." [`b-sb20-f007290-c1`, team b]
- Positions seen by the extractor (`a-sa26-f011460-q1`): no-Rust+Wasm-beats-JS-more-broadly (Andrew Jakubowicz / co-presenter), contrasted against a blanket claim they attribute to unnamed articles ("JavaScript is fast enough")
- Positions seen by the extractor (`a-sa26-f011460-q2`): Wasm-competitive-even-for-small-functions-with-hand-tuned-FFI (Andrew Jakubowicz)
- Positions seen by the extractor (`a-sa26-f012146-q1`): unified-isomorphic-Rust-client/server-model-preferred (this reviewer, re: Leptos), vs Rails-style-server-MVC-with-separate-JS-frontend (Loco, as described by the reviewer)
- Positions seen by the extractor (`b-sR01-f000256-q1`): rust-for-perf-and-size-and-no-rewrite
- Positions seen by the extractor (`b-sb19-f005699-q1`): wasm-only-for-compute-bound-minimal-interop (Thesys Engineering Team)
- Positions seen by the extractor (`b-sb20-f007290-q1`): not yet — use Rust on the backend and TypeScript on the frontend for now, while remaining optimistic about where Dioxus is headed (fasterthanlime)

### `all-rust-vs-platform-native-tooling`

**Question.** Where Rust meets a host platform (Android JNI, iOS AppDelegate and XCTest, browser E2E tests), write the glue and tests in Rust, or in the platform's language and tools?

- Grouping: Same choice between named alternatives (jni crate vs C++, objc2 vs Swift/ObjC, wasm-bindgen-test vs Playwright); the platform is context.
- Absorbs merge-final ids: `frontend-e2e-pure-rust-vs-js`, `jni-layer-rust-vs-cpp`, `xctest-in-rust`
- Teams: a, b · members (context): `a-sT12-f008455-q1` (f008455, swift-interop, desktop-cli-ui); `b-sb13-f004367-q1` (f004367, frontend); `b-sb20-f007678-q1` (f007678, other); `b-sb21-f008793-q1` (f008793, swift-interop); `b-sb22-f008914-q1` (f008914, other)
- Domains: desktop-cli-ui, frontend, other, swift-interop
- Concepts: objc2; AppDelegate; winit; Bevy; Swift/Objective-C interop; E2E testing; `wasm-bindgen-test`; JS interop dependencies; visual regression testing; JNI; FFI; cross-language bindings; Android/NDK tooling; XCTest; XCUIAutomation; XCTRunner bundling; code coverage via LLVM profiling; cargo-ndk
- Positions:
  - `all-rust-vs-platform-native-tooling--all-rust` — Write it in Rust (the `jni` crate, `objc2`, `wasm-bindgen-test`)
    - **rustunit** · Source `f008455` · date 2025-05-18 · locator § "Receive app open options", paragraph 1; intro paragraphs 1–3 — before winit 0.30.10, winit registered its own AppDelegate and Bevy iOS users had to drop winit to get lifecycle hooks. With the fix, rustunit uses `objc2` to call native Objective-C APIs from pure Rust and wraps that in the `bevy_ios_app_delegate` crate Quote: "Thanks to the objc2 crate we can use native objc APIs without having to write objc but pure rust instead." (flag: voice-unverified (Rust connection in source: publishes Bevy/Rust crates and offers Rust consulting)) [`a-sT12-f008455-c1`, team a]
    - **Madoshakalaka** · Source `f004367` · date 2026-03-05 · locator PR description 2026-03-05T15:54:42Z — builds SSR hydration E2E tests as a pure-Rust `wasm-bindgen-test` harness specifically so the project avoids adding non-Rust E2E dependencies like Playwright, Cypress or Selenium Quote: "This is a pure-Rust E2E testing approach that requires no non-Rust dependencies like Playwright, Cypress, or Selenium." [`b-sb13-f004367-c1`, team b]
    - **Chayan Mistry** · Source `f008914` · date 2026-05-12 · locator section "Writing Rust Code," subsection "Basic Structure" — the tutorial's whole worked example is `#[no_mangle] pub extern "C" fn Java_com_example_rustdemo_MainActivity_helloFromRust(...)` functions written in Rust, following the `Java_<package>_<class>_<method>` naming convention, built via `cargo-ndk`, with no C++ intermediary anywhere in the pipeline Quote: "JNI functions must follow this naming pattern: Java_<package>_<class>_<method>" [`b-sb22-f008914-c1`, team b]
  - `all-rust-vs-platform-native-tooling--all-rust-workable-not-production` — All-Rust is workable but brittle, not production-ready (iOS XCTest)
    - **Sebastian Imlay (simlay)** · Source `f008793` · date 2026-02-04 · locator § "Closing thoughts" — an all-Rust XCTest harness (bundling both the app and a `#![no_main]` XCTest bundle built from objc2 bindings) works and lets you drive UI automation and code coverage without ever opening Xcode, but exit-status detection is unreliable, on-device operation is unclear, and the whole setup is "brittle"; he still prefers the Makefile/CLI workflow over `xcodebuild` tooling day to day Quote: "This is a pretty brittle setup and I'm not sure I suggest it in production." [`b-sb21-f008793-c1`, team b]
  - `all-rust-vs-platform-native-tooling--platform-native-glue` — Write the glue in the platform's language for its tooling (C++ JNI in Android Studio)
    - **Emily Dixon** · Source `f007678` · date 2023-12-13 · locator section "Rust for Android," subsection "The app" — many guides write both the FFI (Rust↔C) and JNI (C↔JVM) layers in Rust, but doing the JNI side in C++ instead lets Android Studio's native-C++ project tooling (code generation, build automation, code analysis, jump-to-declaration) work across the boundary, at the cost of one extra language Quote: "Many guides write the JNI and FFI layers in Rust, but I chose to write the JNI side in C++ instead." [`b-sb20-f007678-c1`, team b]
- Positions seen by the extractor (`a-sT12-f008455-q1`): pure-Rust bindings via objc2; native objc/Swift glue; roll your own instead of winit (the pre-0.30.10 only option)
- Positions seen by the extractor (`b-sb13-f004367-q1`): pure-rust-e2e-no-js-deps (Madoshakalaka; its-the-shrimp and futursolo's stances are reported second-hand in this source, not independently quoted)
- Positions seen by the extractor (`b-sb20-f007678-q1`): write the JNI layer in C++, trading an extra language at the boundary for Android Studio's code generation, build automation, and header-level code navigation, which Cargo/Rust tooling lacked at the time (Emily Dixon) — the source itself notes this goes against how "many guides" do it
- Positions seen by the extractor (`b-sb21-f008793-q1`): workable-but-not-production-ready (Sebastian Imlay / simlay)
- Positions seen by the extractor (`b-sb22-f008914-q1`): write the JNI functions directly in Rust with the `jni` crate (`#[no_mangle] extern "C" fn Java_...`) and `cargo-ndk` for cross-compiling — the mainstream approach this tutorial teaches as the default, in direct contrast to f007678's choice to move the JNI layer to C++ (Chayan Mistry)

### `macro-vs-boilerplate`

**Question.** Should a repeated pattern be written with a macro, or as plain code (functions, derives, explicit boilerplate)?

- Grouping: Same "macro or plain code" choice; macro-free framework APIs and macros hiding API requirements stay apart.
- Absorbs merge-final ids: `macros-sparingly-vs-liberally`
- Teams: a, b · members (context): `a-sR08-f003082-q1` (f003082, core, wasm); `a-sa17-f007736-q1` (f007736, cloud-workers, core); `a-sa23-f011186-q3` (f011186, core); `b-sb20-f007736-q1` (f007736, cloud-workers); `b-sb20-f007760-q1` (f007760, cloud-workers)
- Domains: cloud-workers, core, wasm
- Concepts: macros vs. functions; code generation; API ergonomics; macros (attribute macros; proc-macro); boilerplate; macros; procedural macros; attribute macros; boilerplate reduction; AWS SDK client setup
- Positions:
  - `macro-vs-boilerplate--macros-sparingly` — Use macros sparingly; prefer functions, derives or macro-free APIs; boilerplate is an acceptable price
    - **fitzgen (Bytecode Alliance / Wasmtime core, `arbitrary` crate author)** · Source `f003082` · date 2025-06-12 · locator PR #10924 review comments — reviewing a macro used to produce a fixed empty-value sequence, argued it should just be `TableOps::default()` derived on the type, and that if the sequence were needed in several places it should be a function rather than a macro Quote: "if we did want to create this particular sequence in a bunch of places we should just use a function rather than a macro" [`a-sR08-f003082-c1`, team a]
    - **Sam Van Overmeire** · Source `f007736` · date 2024-01-10 · locator paragraph beginning "Before continuing: would you ever want to use a macro like this?" — Defaults against using an attribute macro to strip Lambda-handler boilerplate in real applications, since the boilerplate is usually minor or main() needs custom per-Lambda initialization anyway; reserves the macro for many simple Lambdas, low tolerance for boilerplate, or macro experimentation. Quote: "Before continuing: would you ever want to use a macro like this? For real applications: default to no." [`a-sa17-f007736-c1`, team a]
    - **Adam** · Source `f011186` · date 2024-11-20 · locator ~00:11:27 — Rust's macro system is both one of its best and one of its worst features; very powerful but should be used carefully and in small amounts Quote: "I think macros are kind of like salt you want to use a little" [`a-sa23-f011186-c3`, team a]
    - **Sam Van Overmeire** · Source `f007736` · date 2024-01-17 · locator paragraph beginning "Before continuing: would you ever want to use a macro like this?" — for most real applications either the boilerplate is tolerable or you'll want custom initialization code in `main` that a fully-generated `main` forecloses; the macro pays off mainly if you have many simple Lambdas, a very low tolerance for boilerplate, or want to experiment with macros and serverless Quote: "For real applications: default to no." [`b-sb20-f007736-c1`, team b]
    - **Sam Van Overmeire** · Source `f007760` · date 2024-01-31 · locator paragraph beginning "As a reminder: in the previous blog post" — reiterating the prior post's stance while extending the macro to auto-initialize AWS SDK clients found among the handler's parameters — still frames the macro as useful only for callers with many simple, client-only Lambdas Quote: "A bit of boilerplate is acceptable when this helps you retain the flexibility to customize your main function, adding any (initialization) code you require." [`b-sb20-f007760-c1`, team b]
- Positions seen by the extractor (`a-sR08-f003082-q1`): prefer function/derive over a macro absent a real codegen need
- Positions seen by the extractor (`a-sa17-f007736-q1`): macro-not-worth-it-by-default (with a narrow exception)
- Positions seen by the extractor (`a-sa23-f011186-q3`): use-sparingly-("like salt") (Adam)
- Positions seen by the extractor (`b-sb20-f007736-q1`): default to no for real applications — only worthwhile with many very simple Lambdas, a low tolerance for boilerplate, or wanting to experiment with macros (Sam Van Overmeire)
- Positions seen by the extractor (`b-sb20-f007760-q1`): same as f007736 — worthwhile mainly when you have many simple Lambdas or only need AWS clients with sensible defaults; a bit of boilerplate is otherwise an acceptable price for main-function flexibility (Sam Van Overmeire)

### `proc-macro-derives-vs-reflection-shape`

**Question.** Per-trait proc-macro derives, or runtime reflection shape data (facet)?

- Grouping: Same concrete choice in one talk, logged by both teams in several parts.
- Absorbs merge-final ids: `element-type-dependent-serialization`, `runtime-reflection-vs-codegen-tradeoff`
- Teams: a, b · members (context): `a-sa25-f011413-q1` (f011413, core); `a-sa25-f011413-q3` (f011413, core, desktop-cli-ui); `b-sb24-f011413-q1` (f011413, core); `b-sb24-f011413-q2` (f011413, core); `b-sb24-f011413-q3` (f011413, core)
- Domains: core, desktop-cli-ui
- Concepts: procedural macros; derive macros; compile times; build-time code execution; reflection; vtables; runtime performance; build times; proc macros; orphan rules; ecosystem network effects; reflection/shape data; serde(with); Rust specialization (unstable/unsound on nightly); runtime type dispatch via reflection; generated LLVM IR; Cranelift JIT; reflection runtime overhead; App Store/binary-size constraints
- Positions:
  - `proc-macro-derives-vs-reflection-shape--proc-macros-costly` — Proc macros are costly and unsolved
    - **Amos (fasterthanlime)** · Source `f011413` · date 2026-06-11 · locator ~00:02:04–00:02:37 — procedural macros are a pure AST transform shaped as Rust source that the compiler must compile, optimize, run, and grant disk/network access to "just in case"; many people have tried to fix this and nothing has stuck Quote: "why is a pure AST transform shaped as a rust source we have to compile and optimize and run and... [grant] it full disk and network access just in case" [`a-sa25-f011413-c1`, team a]
  - `proc-macro-derives-vs-reflection-shape--ship-shape-data` — Ship shape data; reflection avoids annotation gaps
    - **Amos (fasterthanlime)** · Source `f011413` · date 2026-06-11 · locator [02:09]-[04:09] — every new Rust behavior (Debug, Display, Deserialize, ...) tends to spawn its own trait and proc-macro derive; proc macros are costly (compile/optimize/run arbitrary code with disk/network access) and each new derive macro has to independently win ecosystem-wide adoption because of orphan rules; facet instead derives a single associated `SHAPE` constant per type (name, offset, alignment, type id, variants, attributes, doc comments, ...) that many downstream behaviors (a colorized Debug, structural diffing, CLI parsing, JSON Schema export, TypeScript codegen) can all consume from one derive Quote: "Instead of trying to turn our types into more code... we might consider shipping data about our types." [`b-sb24-f011413-c1`, team b]
    - **Amos (fasterthanlime)** · Source `f011413` · date 2026-06-11 · locator [08:11]-[10:12] — Serde needs an explicit `#[serde(with = ...)]` annotation to serialize `Vec<u8>` as raw bytes instead of a numeric sequence, because Rust has no stable (or nightly-safe) specialization to detect the element type automatically; a reflection-based serializer can inspect the concrete element type at runtime and pick the right encoding without any annotation Quote: "it would be nice if Serde was actually able to like do that for us without the annotation, right? But that would mean... you would have to specialize on the T... which is not a thing in Rust stable and should not be a thing in Rust nightly either." [`b-sb24-f011413-c2`, team b]
  - `proc-macro-derives-vs-reflection-shape--reflection-doesnt-clearly-win` — Reflection's runtime cost is real and a JIT is no general answer
    - **Amos (fasterthanlime)** · Source `f011413` · date 2026-06-11 · locator ~00:06:23–00:07:00 — he expected reflection to trade only build time for runtime speed, but measured build times as "a wash" and runtime performance as unconditionally worse ("100%" in the case shown), calling this inherent to reflection-based systems Quote: "Uh I was wrong... performance is worse. Runtime performance is worse... it by by design it is much slower and that's a fact of life. You can do nothing to change that." [`a-sa25-f011413-c4`, team a]
    - **Amos (fasterthanlime)** · Source `f011413` · date 2026-06-11 · locator ~00:10:31–00:11:03 — a JIT (Cranelift) can close or beat the reflection performance gap, but shipping one isn't viable broadly — rejected outright on Apple platforms, and disliked by users due to unexplained binary size and warm-up cost Quote: "obviously shipping a jit is not an option for everyone... if you're shipping for Apple platforms, Apple's going to get really mad at you" [`a-sa25-f011413-c5`, team a]
    - **Amos (fasterthanlime)** · Source `f011413` · date 2026-06-11 · locator [05:09]-[09:12] — he expected reflection to trade worse runtime performance for meaningfully better build times versus Serde's generated code, but build times turned out roughly the same either way, and runtime performance is unambiguously worse by design; a Cranelift JIT built on the reflected type data can beat Serde in a microbenchmark, but shipping a JIT is not viable for many targets (Apple platform policy, user-visible binary bloat, warmup cost) Quote: "This is a negative result that I have to report... the build times are like meh... performance is worse. Runtime performance is worse. We were right about that." [`b-sb24-f011413-c3`, team b]
- Positions seen by the extractor (`a-sa25-f011413-q1`): "proc macros are a rough but load-bearing stopgap, kept for lack of a stuck alternative" vs. "the whole shape — AST transform compiled/run/optimized with disk+network access 'just in case' — is wrong and nothing proposed has replaced it"
- Positions seen by the extractor (`a-sa25-f011413-q3`): "reflection is worth the tradeoff in ergonomics-sensitive domains (test assertions, CLI parsing/config, GUIs, RPC schema negotiation)" vs. "compile-time codegen stays faster and reflection's build-time win doesn't reliably materialize"
- Positions seen by the extractor (`b-sb24-f011413-q1`): ship-shape-data-not-more-derives (Amos)
- Positions seen by the extractor (`b-sb24-f011413-q2`): reflection-avoids-the-missing-annotation-problem (Amos)
- Positions seen by the extractor (`b-sb24-f011413-q3`): reflection-doesnt-clearly-win-and-jit-isnt-generally-shippable (Amos)

### `serialization-format-choice`

**Question.** Which serialization format for a given constraint: postcard, JSON, CBOR, MessagePack, TOML, YAML or bincode?

- Grouping: Same choice among named formats; compile-time embedding, wire stability, no-std, i128 and versioned persistence are contexts.
- Absorbs merge-final ids: `config-format-for-unsupported-type`, `const-serialized-asset-format`, `no-std-serialization-format`, `postcard-for-stable-wire-protocol`
- Teams: a, b · members (context): `a-sa03-f002300-q1` (f002300, frontend); `a-sa06-f003590-q2` (f003590, decentralized-iroh); `b-bk03-f000267-q9` (f000267, core); `b-sR08-f003587-q1` (f003587, ml, embedded); `b-sb09-f003030-q1` (f003030, embedded)
- Domains: core, decentralized-iroh, embedded, frontend, ml
- Concepts: const evaluation; macro-generated data; serialization format choice (JSON vs. bespoke vs. postcard); compile-time cost; serialization format; protocol stability; wire compatibility; serialization; serde; bincode; schema evolution; data format stability; serialization format choice; no-std; MessagePack; CBOR; serialization formats; i128 support; config DSLs; ecosystem conventions
- Positions:
  - `serialization-format-choice--established-binary-format` — An established binary format (postcard), with variant order as a stability contract
    - **ealmloff** · Source `f002300` · date 2024-11-11 · locator PR comment, responding to review — Responds to a suggestion that the serialized bytes be valid JSON by noting this would need much more const-time logic to format strings/numbers with uncertain compile-time cost, and states a preference for targeting postcard, an existing well-defined serialization format, over keeping a bespoke one. Quote: "I don't love having a bespoke serialization format. postcard is a much simpler well defined serialization format that might be easier to target than json. I think it is pretty similar to what we are currently generating" [`a-sa03-f002300-c1`, team a]
    - **Rüdiger Klaehn** · Source `f003590` · date 2025-09-26 · locator § RPC protocol — states postcard is non-self-describing, so enum case order must be preserved for the protocol to remain stable long-term; this is presented as a requirement to design around, not a reason to avoid postcard Quote: "Postcard is a non-self-describing format, so we need to make sure to keep the order of the enum cases if we want the protocol to be long-term stable" [`a-sa06-f003590-c2`, team a]
  - `serialization-format-choice--cbor-for-no-std` — CBOR over MessagePack for no-std
    - **antimora** · Source `f003587` · date 2025-10-10 · locator PR #3792, comment 2025-10-10T14:21:49Z — switched the new format's metadata serialization from MessagePack (`rmp-serde`) to CBOR (`ciborium`) because `rmp-serde` isn't no-std compatible and its upstream project has been inactive for over a year, while CBOR is an IETF-standardized, Serde-recommended, no-std-capable format that also preserves enum variant information. Quote: "I switched from MessagePack to CBOR for metadata serialization due to rmp-serde's limitations" [`b-sR08-f003587-c1`, team b]
  - `serialization-format-choice--toml-for-consistency` — TOML for ecosystem consistency
    - **okhsunrog** · Source `f003030` · date 2025-05-24 · locator comment @okhsunrog 2025-05-24T17:23:55Z — questions why the PR uses YAML instead of TOML, for consistency with the Rust ecosystem. Quote: "Why not toml, to be consistent with the Rust ecosystem?" [`b-sb09-f003030-c1`, team b]
  - `serialization-format-choice--yaml-for-convenience` — YAML for convenience, patching the library
    - **bjoernQ** · Source `f003030` · date 2025-05-24 · locator comment @bjoernQ 2025-05-24T17:33:48Z — finds TOML's representation inconvenient for this use case and considers YAML the nicest representation available. Quote: "the toml representation is ... Quite inconvenient - IMHO yaml is the nicest representation here" [`b-sb09-f003030-c2`, team b]
    - **bugadani** · Source `f003030` · date 2025-06-04 · locator comment @bugadani 2025-06-04T15:24:04Z — would rather add i128 support to whichever YAML library is chosen than change the config's type range, and flags serde_yml as likely unmaintained. Quote: "I'd still prefer adding i128 support to whatever yaml library we pick - which probably shouldn't be serde_yml as it looks quite unmaintained." [`b-sb09-f003030-c3`, team b]
    - **bugadani** · Source `f003030` · date 2025-06-04 · locator comment @bugadani 2025-06-04T15:39:12Z — suggests trying the facet-yaml crate as a better-maintained alternative. Quote: "I'd probably give https://crates.io/crates/facet-yaml a try" [`b-sb09-f003030-c4`, team b]
    - **bugadani** · Source `f003030` · date 2025-06-05 · locator comment @bugadani 2025-06-05T11:43:25Z — pushes back that the YAML spec doesn't forbid wider integers, questioning bjoernQ's pessimism about the format. Quote: "I get that the spec doesn't _mandate_ support for wider integers but it also doesn't forbid them, so why this sudden negativity?" [`b-sb09-f003030-c6`, team b]
  - `serialization-format-choice--no-custom-format` — A custom config language is too costly
    - **bjoernQ** · Source `f003030` · date 2025-06-05 · locator comment @bjoernQ 2025-06-05T11:30:38Z — after evaluating serde_yml, serde_yaml and facet-yaml, concludes YAML tooling in the Rust ecosystem is a dead end for i128 support, floats designing a custom config language, but judges it too much effort to "just try it". Quote: "So YAML doesn't seem to be a good way forward... Maybe defining our own config-language would be an alternative - but probalby too much effort to \"just try it\"" [`b-sb09-f003030-c5`, team b]
  - `serialization-format-choice--ship-now-switch-later` — Ship now, switch format later
    - **MabezDev** · Source `f003030` · date 2025-06-10 · locator comment @MabezDev 2025-06-10T09:48:30Z — since the format is currently internal-only, proposes proceeding with YAML plus workarounds now and switching library or format later if something better appears. Quote: "this is strictly \"internal\" right now, so we can proceed with yaml + some work arounds, then if a better library, or a more appropriate format shows up we can switch to it." [`b-sb09-f003030-c7`, team b]
  - `serialization-format-choice--p1` — avoid-bincode-for-new-persisted-data
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Zebra Cached State Database Implementation § Data Formats — legacy column families use bincode via serde for note commitment trees, but this is called out as a risky choice for anything new because it depends on the exact order and type of struct fields, unlike the project's custom IntoDisk/FromDisk implementations used elsewhere Quote: "bincode is a risky format to use, because it depends on the exact order and type of struct fields. Do not use it for new column families." (flag: voice-unverified) [`b-bk03-f000267-c9`, team b]
- Positions seen by the extractor (`a-sa03-f002300-q1`): reviewer (unattributed) — would like the serialized bytes to be valid JSON; ealmloff (PR author) — avoid a bespoke format, but prefers moving toward an established format like postcard over JSON, citing the added const-time logic JSON would require
- Positions seen by the extractor (`a-sa06-f003590-q2`): use postcard for compactness, but treat enum-variant order as an append-only contract that must never be reordered
- Positions seen by the extractor (`b-bk03-f000267-q9`): avoid-bincode-for-new-persisted-data
- Positions seen by the extractor (`b-sR08-f003587-q1`): cbor-over-messagepack-for-no-std
- Positions seen by the extractor (`b-sb09-f003030-q1`): prefer-toml-for-consistency (okhsunrog), yaml-is-more-convenient (bjoernQ), patch-the-yaml-library (bugadani), narrow-to-i64-and-ship (bjoernQ, actual PR change), custom-config-language-considered-and-rejected-as-too-costly (bjoernQ), ship-now-switch-format-later (MabezDev)

### `async-vs-threads`

**Question.** Should a Rust program model concurrency with async/await tasks, or with OS threads (on embedded: hand-written run-to-completion or state-machine tasks)?

- Grouping: Same concrete concurrency-model choice; embedded RTIC and the async book are contexts.
- Absorbs merge-final ids: `embedded-async-vs-run-to-completion`
- Teams: a, b · members (context): `a-sB01-f000227-q3` (f000227, embedded); `a-sR01-f000227-q2` (f000227, embedded); `b-bk01-f000233-q10` (f000233, core, embedded, web, distributed); `b-sR01-f000233-q1` (f000233, embedded, web, distributed, other)
- Domains: core, distributed, embedded, other, web
- Concepts: async-await; run-to-completion; cooperative-multitasking; async/await; static allocation; Futures; SRP run-to-completion requirement; async; OS threads; thread pool; zero-cost abstraction; async runtimes; threads; concurrency; cancellation
- Positions:
  - `async-vs-threads--async-for-io-wait-and-no-os` — Async where work waits on I/O or there is no OS
    - **Rust Async Book (async-book, rust-lang.github.io)** · Source `f000233` · date undated (living document; no revision date on page) · locator § "What is Async Programming and why would you do it?", paragraph 2 — async fits systems handling many concurrent tasks that spend most of their time waiting (e.g. client responses, IO), and also fits microcontrollers with very limited memory and no OS-provided threads. Quote: "This makes async programming a good fit for systems which need to handle very many concurrent tasks and where those tasks spend a lot of time waiting" [`b-sR01-f000233-c1`, team b]
  - `async-vs-threads--async-tasks-on-embedded` — Async tasks compiled to static executors beat manual task splitting on embedded
    - **RTIC project (rtic.rs maintainers, unnamed individually)** · Source `f000227` · date unknown (living document, no publish/version date given) · locator § "RTIC into the Future" — the maintainers argue async/await brings "improved ergonomics" over manual sub-task splitting, is compatible with SRP because the compiler forbids awaiting while holding a resource, and avoids dynamic allocation (which would panic on OOM) by using compile-time-generated static executors. Quote: "So with the technical stuff out of the way, what does async/await bring to the table? The answer is - improved ergonomics!" [`a-sR01-f000227-c2`, team a]
  - `async-vs-threads--p1` — async/await preferred for ergonomics over manual state-machine sub-tasking
    - **RTIC developers** · Source `f000227` · date undated (living doc) · locator Preface, "RTIC into the Future" — States that without async/await a programmer must manually split a task into sub-tasks and track state, whereas async/await builds the progression mechanism automatically at compile time via Futures Quote: "The answer is - improved ergonomics!" [`a-sB01-f000227-c3`, team a]
  - `async-vs-threads--p2` — async for large numbers of (esp. IO-bound) tasks and constrained environments; plain threads otherwise
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "Why Async?" § Async vs threads in Rust / § Async in Rust vs other languages — OS threads need no new programming model and let existing sync code run unchanged (and support OS-level thread-priority tuning for latency-sensitive work), but come with real CPU/memory overhead per thread; async gives orders-of-magnitude more concurrent tasks for the same overhead, especially for IO-bound workloads like servers and databases, and (being zero-cost, needing no heap allocation or dynamic dispatch) can run in constrained environments like embedded systems — at the cost of larger compiled binaries from generated state machines plus a bundled runtime. Explicitly frames this as "not better than threads, but different": use threads if you don't need async's performance benefits. Quote: "asynchronous programming is not better than threads, but different." [`b-bk01-f000233-c11`, team b]
- Positions seen by the extractor (`a-sB01-f000227-q3`): async/await preferred for ergonomics
- Positions seen by the extractor (`a-sR01-f000227-q2`): "async/await, statically compiled, improves ergonomics without violating SRP or requiring dynamic allocation" (RTIC project)
- Positions seen by the extractor (`b-bk01-f000233-q10`): async for large numbers of (esp. IO-bound) tasks and constrained/embedded environments; plain threads when async's performance benefits aren't needed
- Positions seen by the extractor (`b-sR01-f000233-q1`): async-for-io-wait-and-no-os

### `ffi-copy-vs-share`

**Question.** At a Rust FFI or JS boundary, should data be copied or serialized across, or shared by reference or opaque handle?

- Grouping: Same choice; JNI and the Rust+Wasm book (both teams) are contexts.
- Teams: a, b · members (context): `a-sB02-f000256-q3` (f000256, web, wasm); `b-bk02-f000256-q2` (f000256, wasm, frontend); `b-sb20-f007678-q2` (f007678, swift-interop, other); `b-sb22-f008914-q2` (f008914, swift-interop, other)
- Domains: frontend, other, swift-interop, wasm, web
- Concepts: FFI boundary design; wasm-bindgen; wasm_bindgen; linear memory; FFI memory management; ownership across language boundaries; FFI parameter types; string conversion overhead; borrowing across a language boundary
- Positions:
  - `ffi-copy-vs-share--convert-or-copy` — Convert or copy into idiomatic types (copy across FFI, Rust collections, lean on generated glue)
    - **Emily Dixon** · Source `f007678` · date 2023-12-13 · locator section "Rust for Android," paragraph beginning "On the Rust side, you'll need to encapsulate" — creating an FFI struct that copies out of the Rust result object (rather than sharing a pointer into it) costs a small performance penalty but guarantees memory management on one side of a binding can't affect the other side, which the author judges worth it "more often than not" Quote: "Copying immutable data is generally safer and easier than trying to share it." [`b-sb20-f007678-c2`, team b]
  - `ffi-copy-vs-share--share-or-borrow` — Pass borrowed references to avoid conversion overhead
    - **Chayan Mistry** · Source `f008914` · date 2026-05-12 · locator section "Performance Considerations," subsection "2. Use Appropriate Data Types" — contrasts `pub fn process_string(s: String) -> String` (marked inefficient, string-conversion overhead) with `pub fn process_string(s: &str) -> String` (marked efficient), as one of four listed performance practices alongside minimizing JNI call count and release-profile tuning Quote: "✅ Efficient: Use references when possible" [`b-sb22-f008914-c2`, team b]
  - `ffi-copy-vs-share--p1` — opaque-handles(recommended)
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Interfacing Rust and JavaScript" — a good JS↔wasm interface keeps large, long-lived data as Rust types living in wasm linear memory, exposed to JS only as opaque handles, to minimize copying and serialization overhead across the boundary. Quote: "we want to optimize for the following properties: Minimizing copying... Minimizing serializing and deserializing." [`a-sB02-f000256-c3`, team a]
  - `ffi-copy-vs-share--p2` — minimize copying/serializing across the JS↔wasm boundary; expose long-lived Rust data as opaque handles, return small copyable results
    - **rustwasm working group (Rust and WebAssembly book) [voice-unverified]** · Source `f000256` · date unknown (living doc) · locator § "Interfacing Rust and JavaScript" — states a general interface-design rule of thumb for wasm_bindgen boundaries — large, long-lived structures should live in Rust/wasm linear memory and be exposed to JS only as opaque handles, with JS calling functions that do the heavy work and return small results, to avoid copy/serialize overhead; separately names "return only the cells that changed" (a delta-based design) as a viable alternative it does not adopt, citing implementation difficulty. Quote: "a good JavaScript↔WebAssembly interface design is often one where large, long-lived data structures are implemented as Rust types that live in the WebAssembly linear memory, and are exposed to JavaScript as opaque handles." [`b-bk02-f000256-c2`, team b]
  - `ffi-copy-vs-share--p3` — replace a Display-generated JS String with a raw pointer + Uint8Array overlay onto wasm linear memory
    - **rustwasm working group (Rust and WebAssembly book) [voice-unverified]** · Source `f000256` · date unknown (living doc) · locator § "Rendering to Canvas Directly from Memory" — the tutorial's initial render() returns a Rust-formatted String, which it then names as a source of "unnecessary copies," and replaces it with a pointer-returning render so JS reads the cell buffer directly out of wasm memory. Quote: "Generating (and allocating) a String in Rust and then having wasm-bindgen convert it to a valid JavaScript string makes unnecessary copies of the universe's cells." [`b-bk02-f000256-c3`, team b]
- Positions seen by the extractor (`a-sB02-f000256-q3`): opaque-handles(recommended), copy-serialize(discouraged)
- Positions seen by the extractor (`b-bk02-f000256-q2`): opaque handles + small copyable results (chosen general principle); return only changed deltas (named alternative, judged harder to implement); raw pointer + JS typed-array overlay (chosen concrete instance, replacing an initial Display→String copy)
- Positions seen by the extractor (`b-sb20-f007678-q2`): prefer copying data across the boundary over sharing it, for memory-safety and simplicity, accepting the performance cost (Emily Dixon)
- Positions seen by the extractor (`b-sb22-f008914-q2`): prefer borrowed references (`&str`) over owned/copied types (`String`) at the JNI boundary to avoid conversion overhead — in tension with f007678's stated preference for copying data across FFI boundaries for safety/simplicity (Chayan Mistry)

### `generics-vs-dyn-for-abstraction`

**Question.** Should Rust code abstract with generics (static dispatch, associated types) or with `dyn Trait` and type erasure?

- Grouping: Same choice; dependency injection, pipelines and code size are contexts where the answer flips (trait objects win for wasm size).
- Absorbs merge-final ids: `type-erasure-vs-associated-type`
- Teams: a, b · members (context): `a-sB02-f000256-q9` (f000256, wasm, embedded, core); `a-sa07-f003704-q1` (f003704, ml, core); `a-sa30-f013276-q1` (f013276, core, web); `b-bk02-f000256-q8` (f000256, wasm, core)
- Domains: core, embedded, ml, wasm, web
- Concepts: static vs dynamic dispatch; monomorphization bloat; traits; associated-types; type-erasure; dynamic-dispatch; trait objects; dyn Trait; generics; static vs. dynamic dispatch; type erasure; object safety; monomorphization; dynamic dispatch; code size
- Positions:
  - `generics-vs-dyn-for-abstraction--static-by-default` — Enums or generics; avoid `dyn` when possible
    - **laggui** · Source `f003704` · date 2025-11-03 · locator PR #3872, comment 2025-11-03T20:43:16Z — proposes replacing the NodeConfig trait's runtime type erasure and up/down-casting with an associated config type on NodeProcessor Quote: "This would remove the need for `NodeConfig` trait entirely." [`a-sa07-f003704-c1`, team a]
    - **parasyte — track record not established from this source** · Source `f013276` · date 2024-12-05 · locator post 2024-12-05T23:20:50.930Z — challenges the OP's motivation for reaching for type erasure, stating it more often costs than it buys Quote: "Type erasure often hurts more than it helps, but there must be some other motivation for it than making the code 'more abstract'." [`a-sa30-f013276-c3`, team a]
    - **parasyte — track record not established from this source** · Source `f013276` · date 2024-12-06 · locator post 2024-12-06T04:21:54.051Z — ranks generics, enums, and `dyn Trait` as all valid dependency-injection mechanisms but singles out `dyn Trait` as having disproportionately narrow benefit for its cost Quote: "dyn Trait can also be used for dependency injection. It's pure dynamic dispatch, of course. But the benefits for its use are extremely narrow, and it comes with more downsides than the one thing it has going for it." [`a-sa30-f013276-c4`, team a]
    - **jumpnbrownweasel — track record not established from this source** · Source `f013276` · date 2024-12-05 · locator post 2024-12-05T22:41:05.581Z — states the OP's desired abstraction isn't achievable with trait objects because they are much less capable than generics for this purpose Quote: "This abstraction doesn't seem possible with trait objects, as they're not nearly as capable as generics and you're pushing them over their limits. Abstraction in Rust is better supported with generics." [`a-sa30-f013276-c7`, team a]
  - `generics-vs-dyn-for-abstraction--p1` — trait-objects-for-size
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Shrinking .wasm Code Size" — "Use Trait Objects Instead of Generic Type Parameters" — generic functions get monomorphized into one copy per type, growing code size; trait objects emit a single function using dynamic dispatch instead, at the cost of lost compiler optimization opportunities and added indirect-call overhead. Quote: "The downside is the loss of the compiler optimization opportunities and the added cost of indirect, dynamically dispatched function calls." [`a-sB02-f000256-c10`, team a]
  - `generics-vs-dyn-for-abstraction--p2` — use trait objects instead of generic type parameters to cut code size, accepting slower indirect calls and lost per-type inlining
    - **rustwasm working group (Rust and WebAssembly book) [voice-unverified]** · Source `f000256` · date unknown (living doc) · locator § "Shrinking .wasm Code Size" → Use Trait Objects Instead of Generic Type Parameters — contrasts monomorphized generics, which emit one function copy per concrete type and enable per-type optimization, against trait objects, which emit a single dynamically-dispatched copy; names the size win and the speed/inlining loss explicitly as the trade. Quote: "If you use trait objects instead of type parameters... only a single version of the function is emitted in the .wasm. The downside is the loss of the compiler optimization opportunities and the added cost of indirect, dynamically dispatched function calls." [`b-bk02-f000256-c9`, team b]
- Positions seen by the extractor (`a-sB02-f000256-q9`): trait-objects(recommended here for size, at cost of perf and optimizer opportunities)
- Positions seen by the extractor (`a-sa07-f003704-q1`): type-erasure-with-casting (status quo), associated-type-on-trait (laggui, proposed)
- Positions seen by the extractor (`a-sa30-f013276-q1`): "generics are the better/proper way to do abstraction in Rust; dyn Trait's benefits are extremely narrow and it carries real downsides" (parasyte, jumpnbrownweasel — convergent, no opposing voice quoted in this source; the OP's own attempts to lean on `dyn` for ergonomic reasons are visible in the thread but the OP isn't established as a qualifying Voice)
- Positions seen by the extractor (`b-bk02-f000256-q8`): trait objects — one function body, dynamic dispatch (chosen for size); generics — per-type copies, better optimization/inlining (named alternative, rejected on size grounds)

### `lambda-vs-containers`

**Question.** Should a Rust service run serverless (Lambda, edge Workers) or on long-running containers or VPSes?

- Grouping: Same deployment-substrate choice.
- Teams: a, b · members (context): `a-sa17-f007797-q1` (f007797, cloud-workers); `a-sa24-f011220-q1` (f011220, cloud-workers, distributed); `b-sT07-f004166-q1` (f004166, cloud-workers, distributed); `b-sb20-f007797-q1` (f007797, cloud-workers)
- Domains: cloud-workers, distributed
- Concepts: async runtimes; cloud deployment; cold start; warm start; serverless spectrum; container orchestration; Tower/Axum-on-Lambda; scale-to-zero; serverless; Durable Objects for strong consistency; per-data consistency choice; scale-to-zero cost; Lambda Web Adapter; serverless vs. container deployment; cost/infra-parity tradeoff
- Positions:
  - `lambda-vs-containers--serverless-first` — Default to serverless once measured, or build on edge primitives
    - **James Eastham** · Source `f011220` · date 2024-12-13 · locator ~38:52-39:58 — after porting the same Rust web API and Kafka-consuming background service from Fargate (512 MB, always-on) to Lambda, latency and p50/p99 held steady, memory use dropped to a fraction of the container's, cold starts were a small minority of invocations (3/850 for the background service, 4/1,350 for the web API), and the idle 24/7 container cost/sustainability problem went away; he concludes serverless, not the container/Kubernetes path, is what should be reached for by default, including for teams that later "graduate" to Kubernetes once they understand their workload Quote: "next time you're looking to deploy a rust application into production just consider serverless see how that might help you" [`a-sa24-f011220-c1`, team a]
    - **Nick Kuntz** · Source `f004166` · date 2026-01-27 · locator § storage primitives ("The key insight from porting Tuwunel…"); § conclusion — D1 for queryable durable data, KV for OAuth tokens, R2 for media, Durable Objects where atomicity is required (one-time key claims); argues operations vanish and cost scales to zero Quote: "different data needs different consistency guarantees" (flag: voice-unverified) [`b-sT07-f004166-c1`, team b]
  - `lambda-vs-containers--split-by-workload` — Serverless for infrequent or test traffic, containers for always-on
    - **Sam Van Overmeire** · Source `f007797` · date 2024-02-16 · locator paragraph beginning "Lambda Web Adapter not only makes it easier..." — Using Lambda Web Adapter to keep one Axum app deployable to either target, argues Lambda suits infrequently-used or test environments while ECS/Fargate is cheaper for always-on production traffic — accepting a test/prod infrastructure mismatch for the cost savings. Quote: "An application that runs 24/7 on prod can be costly on Lambda, but cheap on ECS. On the other hand, if you have one or more infrequently used test environments, Lambda is the better choice." [`a-sa17-f007797-c1`, team a]
    - **Sam Van Overmeire** · Source `f007797` · date 2024-02-21 · locator closing paragraph, beginning "Lambda Web Adapter not only makes it easier" — because Lambda Web Adapter decouples the Axum app from any one runtime, an app that is costly to run 24/7 on Lambda but cheap on ECS could run infrequent test environments on Lambda and production on ECS; the author calls this "a tradeoff" since test and production would then run on meaningfully different infrastructure, but says the cost savings can be worth it in some scenarios Quote: "It's a tradeoff because there is now a meaningful difference between the infrastructure your code runs on in test versus production. But in some scenarios, the cost savings might be worth it." [`b-sb20-f007797-c1`, team b]
- Positions seen by the extractor (`a-sa17-f007797-q1`): workload-dependent-split (Lambda for infrequent/test traffic, ECS for always-on production)
- Positions seen by the extractor (`a-sa24-f011220-q1`): Lambda/FaaS-first for production Rust services once measured (Eastham: cold starts become statistically negligible at scale — 3 of 850 and 4 of 1,350 invokes — with equal or better latency and a fourth to fifth of the memory footprint) vs. cold-start skepticism (unnamed, described by Eastham as "people bashing cold starts all over the internet") and long-running-container-first for a one-person team wanting a simple imperative/request-response model over Lambda's reactive, poll-driven programming model (Eastham's own earlier-stated position before he reverses it: "surely lambda's not an option right", ~16:00)
- Positions seen by the extractor (`b-sT07-f004166-q1`): serverless edge primitives, each data class on the primitive matching its consistency need
- Positions seen by the extractor (`b-sb20-f007797-q1`): splitting environments (Lambda for infrequently-used test environments, ECS for always-on production) is floated as a cost-saving option, explicitly named as a tradeoff rather than a clear recommendation (Sam Van Overmeire)

### `optional-parameters-api-shape`

**Question.** Without overloading or default arguments, one configurable entry point (options or Config struct, enum) or several specialized functions and constructors?

- Grouping: Same API-shape choice; new-type-vs-option and state-accessor splits stay apart.
- Absorbs merge-final ids: `config-struct-vs-many-constructors`, `conversion-api-without-overloading`, `separate-fn-vs-longer-signature`
- Teams: a, b · members (context): `a-01-f000530-q1` (f000530, desktop-cli-ui); `a-sa06-f003414-q4` (f003414, desktop-cli-ui); `b-sb05-f001512-q3` (f001512, embedded); `b-sb10-f003222-q2` (f003222, distributed, decentralized-iroh)
- Domains: decentralized-iroh, desktop-cli-ui, distributed, embedded
- Concepts: traits (`Into`); generics; enums; naming conventions; API surface size; absence of method overloading; API surface design; function signatures; config struct; builder pattern; API surface; optional parameters; `impl Into<T>`; API ergonomics
- Positions:
  - `optional-parameters-api-shape--one-configurable-entry` — One entry point: a `Config` struct, `_with_opts`, an enum discriminant, an option on the existing type
    - **MrGVSV** · Source `f000530` · date 2023-10-30 · locator PR comment, mid-thread (identity inferred from a later reply addressed "@MrGVSV I like the idea with the enum...") — Suggests a `ColorSpace` enum passed as a second constructor argument instead of one method per color space, to avoid multiplying method names for every combination. Quote: "I'm still wondering if it would make sense to introduce a `ColorSpace` enum and just specify that as a second parameter so we don't have to introduce a bunch of new methods for each color space." [`a-01-f000530-c2`, team a]
    - **MabezDev** · Source `f001512` · date 2024-06-11 · locator comment 2024-06-11T10:22:55Z — once a setting is part of the config, it should not be public as a separate method — everything should go through the config struct Quote: "If this is part of the config now, then I don't think this should be public anymore, we should do everything through the config struct" [`b-sb05-f001512-c3`, team b]
    - **rklaehn** · Source `f003222` · date 2025-07-04 · locator "Options" section — Rust has neither overloading nor default parameters, so each operation exposes an `_with_opts` method taking an Options struct (the closest mapping to the underlying RPC message), plus convenience wrapper methods using `impl Into<T>` for common cases Quote: "in other languages, you might solve this issue with either overloading or with default parameters. But rust has neither, for very good reasons. So we have come up with the following pattern." [`b-sb10-f003222-c2`, team b]
  - `optional-parameters-api-shape--separate-specialized-entries` — Separate specialized functions or primitives
    - **st0rmbtw** · Source `f000530` · date 2023-10-30 · locator PR body, Objective/Changelog section — Proposes replacing the generic `Color::from(T)`/`T::from(Color)` conversions with one explicitly-named method per source type and per color space, so the target color space is always visible at the call site rather than inferred from context. Quote: "Added a new `Color::rgba_from_array([f32; 4]) -> Color` method." [`a-01-f000530-c1`, team a]
    - **EuclidDivisionLemma** · Source `f003414` · date 2025-09-13 · locator comment 2025-09-13T06:20:43Z — weighs three options (keep `load_with_encoding` separate; one `load` with UTF-16 auto-detection at the cost of 4 args; drop auto-detection for a 2-arg `load`) and flags readability cost of merging Quote: "having a single function will require us to pass four arguments in all those places, making the code significantly less readable" [`a-sa06-f003414-c4`, team a]
  - `optional-parameters-api-shape--drop-feature-keep-signature-small` — Drop the feature to keep the signature small
    - **ConradIrwin** · Source `f003414` · date 2025-09-12 · locator comment 2025-09-12T19:43:46Z — is willing to merge without automatic BOM/UTF-16 detection to keep the `load` call simple, i.e. picks fewer arguments over the extra feature Quote: "I'd also be OK to merge a v1 of this work without the BOM detection" [`a-sa06-f003414-c5`, team a]
  - `optional-parameters-api-shape--many-constructors-criticized` — Many constructors (status quo, criticized)
    - **jessebraham** · Source `f001512` · date 2024-05-30 · locator comment 2024-05-30T12:38:44Z — the proliferation of constructors without documentation makes the API hard to understand Quote: "there are way too many constructors and not enough documentation" [`b-sb05-f001512-c4`, team b]
- Positions seen by the extractor (`a-01-f000530-q1`): explicit-named-methods (st0rmbtw, PR author); generic `impl Into<T>` conversion (unattributed reviewer, raised as a question then partly walked back — "This only works for Vec4"); single constructor + `ColorSpace` enum discriminant (MrGVSV)
- Positions seen by the extractor (`a-sa06-f003414-q4`): keep a separate `load_with_encoding` function to avoid a 4-argument `load`; vs. accept a single simpler function by dropping a feature (automatic UTF-16 detection) to keep arguments to two
- Positions seen by the extractor (`b-sb05-f001512-q3`): config-struct-consolidation (MabezDev), many-constructors-status-quo-criticized (jessebraham)
- Positions seen by the extractor (`b-sb10-f003222-q2`): with-opts-plus-convenience-wrappers (rklaehn)

### `rust-vs-c-inherent-performance`

**Question.** Does safe Rust cost performance against C/C++, or can it match or beat it?

- Grouping: Same performance question; b-sT05-f002499-q2 is removed as Claim-less.
- Absorbs merge-final ids: `composability-vs-borrowck-friction`, `init-requirement-perf-cost`, `safe-rust-for-high-perf-games`
- Teams: a, b · members (context): `a-saL1-f005516-q1` (f005516, core); `a-saL1-f005516-q3` (f005516, core, embedded); `a-saL1-f005516-q4` (f005516, core); `b-sb26-f013214-q2` (f013214, other, embedded)
- Domains: core, embedded, other
- Concepts: compiler optimization; type systems; aliasing (`noalias`/`restrict`); benchmarking methodology; zero-initialization; `MaybeUninit`; allocators; dataflow analysis; codegen/inlining; data-structure abstraction; borrow checker; defensive cloning/`Rc`; late-bound vs. early-optimized language design; unsafe; memory safety; concurrency; crash rates
- Positions:
  - `rust-vs-c-inherent-performance--no-inherent-advantage` — No inherent advantage; social factors dominate
    - **ajdecon** · Source `f005516` · date 2025-06-09 · locator reply, 2025-06-09T14:34:18-05:00 — Agrees there's no inherent reason either language is faster; to the extent C codebases are faster today it's mostly because they're older and have had more engineer-hours of optimization, not a property of C itself. Quote: "there's no inherent reason for either language to be faster. It's all project specific... it's often just because they're much older codebases and have been optimized over a long time." [`a-saL1-f005516-c1`, team a]
  - `rust-vs-c-inherent-performance--types-enable-optimizations` — Rust's type system enables optimizations C lacks
    - **rtpg** · Source `f005516` · date 2025-06-09 · locator reply, 2025-06-09T20:16:56-05:00 — Argues a language with more semantic granularity gives the compiler more true invariants to exploit, e.g. Rust code built on iteration rather than raw array access can eliminate bounds checks entirely; cautions that "like for like" benchmarking between languages is inherently ambiguous. Quote: "a language with 'more' semantic granularity will have more leeway to give you free optimizations... if your codebase is filled with iteration rather than array access, you just don't need your bounds checks!" [`a-saL1-f005516-c2`, team a]
    - **steveklabnik** · Source `f005516` · date 2025-06-10 · locator reply, 2025-06-10T14:15:50-05:00 — States Rust puts the equivalent of C's `restrict` on every reference that doesn't contain an `UnsafeCell`, meaning the no-aliasing guarantee is encoded in the type system, not just a vague folk claim, and that Rust is also ahead on pointer provenance semantics. Quote: "Rust puts the equivalent of `restrict` on every reference that doesn't contain an `UnsafeCell`, so it is doing a bit more than you assume here, and that is in the type system." [`a-saL1-f005516-c3`, team a]
    - **kornel** · Source `f005516` · date 2025-06-10 · locator reply, 2025-06-10T08:19:54-05:00 — Frames the practical gap as partly ecosystem-driven: C's lack of an easily-reached-for hashmap pushes real-world C code toward slow linear searches until forced to fix (citing a GitLab backup-time postmortem), while Rust's easy hashmaps and parallel iterators make fast-by-default code more common in practice. Quote: "C doesn't have easily accessible hashmaps, so implementations tend to default to linear searches, until it becomes a problem... That means the discussion is just about which language makes it easier to write fast programs." [`a-saL1-f005516-c5`, team a]
  - `rust-vs-c-inherent-performance--real-overheads` — Rust has real overheads: initialization, forced refactors and copies
    - **dataangel** · Source `f005516` · date 2025-06-10 · locator reply, 2025-06-10T07:16:21-05:00 — Counters that real Rust disassembly shows concrete recurring costs: bounds checks on every array/division/shift access, "unsafe"-gated SIMD intrinsics, poorly-optimizing iterators (citing open rustc codegen issues), `RefCell` overhead, un-collapsible layers of `Result<>` wrapping, and clones/`Rc` added defensively to satisfy the borrow checker — concluding this is why Rust solutions don't top competitive-programming performance leaderboards. Quote: "if you spend a little time looking at Rust disassembly on nontrivial examples it becomes very obvious... There's a reason the Rust solutions don't win on highload.fun" [`a-saL1-f005516-c4`, team a]
    - **dataangel** · Source `f005516` · date 2025-06-12 · locator reply, 2025-06-12T07:56:20-05:00 and 2025-06-13T20:10:53-05:00 — Argues safe Rust requires a value at construction time (not just before use via dataflow analysis, as for ordinary variables), so a large array or a small-object allocator must eagerly zero-initialize memory it may never read before writing, and the cost compounds with more allocations, sometimes bloating codegen enough to block inlining and further optimization. Quote: "safe Rust requires you to provide a value at construction time, which is not based on dataflow analysis. For example if you make a very large array, you must spend the time to zero init the entire thing even if you always write to elements before reading them." [`a-saL1-f005516-c9`, team a]
    - **dataangel** · Source `f005516` · date 2025-06-10 · locator reply, 2025-06-10T11:09:00-05:00 — Disputes that Rust is generally "faster" in this practical-design-choice sense, saying trivial new features can require large refactorings because they necessitate new borrowing schemes, and separately notes extra clones/`Rc` are commonly added just to satisfy the borrow checker where they aren't algorithmically necessary. Quote: "trivial new features can require large refactorings because they necessitate new borrowing schemes." [`a-saL1-f005516-c12`, team a]
  - `rust-vs-c-inherent-performance--init-cost-narrow` — Initialization cost is a narrow edge case
    - **rpjohnst** · Source `f005516` · date 2025-06-11 · locator reply, 2025-06-11T11:16:03-05:00 and 2025-06-12T10:09:38-05:00 — Repeatedly presses that Rust has no implicit default initialization and only requires init-before-use by dataflow analysis, so the described cost should only bite in narrow cases like large arrays or read buffers, not "all variables" broadly, and questions whether the allocator scenario generalizes. Quote: "Rust merely requires init *before use* based on dataflow analysis. Surely the C code you're comparing with doesn't read from uninitialized variables to a noticeable degree?" [`a-saL1-f005516-c10`, team a]
  - `rust-vs-c-inherent-performance--composability-wins` — Composability lets engineers ship better data structures
    - **ssokolow** · Source `f005516` · date 2025-06-10 · locator reply, 2025-06-10T09:04:39-05:00 and 2025-06-10T11:32:55-05:00 — Argues Rust wins in the sense of what design choices engineers are actually willing to ship (versus benchmark racing); quotes Bryan Cantrill's account of choosing a safe, composable B-Tree in Rust where he'd have defaulted to a less-optimal AVL tree in C, because a hand-rolled intrusive B-Tree in C carries too much memory-corruption risk to trust. Quote: "I would still use an AVL tree in C even though I know I'm giving up some small amount of performance, but in Rust, I get to use a B-Tree." (quoting Bryan Cantrill) [`a-saL1-f005516-c11`, team a]
    - **david_chisnall** · Source `f005516` · date 2025-06-11 · locator reply, 2025-06-11T02:18:49-05:00 — Argues the biggest practical performance advantage of C++ or Rust over C is that it's trivial to write code abstract over data structures, so a wrong choice found in profiling can be swapped easily; in C, implementation details leak through unless wrapped in painful macros — describes replacing his own hand-rolled generic concurrent hash table (many macros) with an off-the-shelf container plus a lock, which was both more maintainable and faster. Quote: "It is *trivial* to write code that is abstract over data structures... In C, implementation details of the data structure tend to leak unless you're *really* careful." [`a-saL1-f005516-c13`, team a]
  - `rust-vs-c-inherent-performance--safe-rust-matches` — Safe Rust matches C for demanding work (embedded display, 3D)
    - **John_Nagle** · Source `f013214` · date 2024-01-13 · locator reply timestamped 2024-01-13T20:31:31 — states his metaverse client's several coordinated CPU-bound threads (refresh, per-frame update, event processing, asset-decoding) doing entirely different work would be "really hard" to coordinate safely in C++, but works acceptably in safe Rust with no `unsafe` used anywhere in his own code Quote: "In safe Rust (I don't use \"unsafe\" in my own code at all) it's not bad." [`b-sb26-f013214-c3`, team b]
  - `rust-vs-c-inherent-performance--safety-cost-acceptable` — A real safety cost is an acceptable trade
    - **parasyte** · Source `f013214` · date 2024-01-10 · locator reply timestamped 2024-01-10T18:33:17 — cites a session where Ark: Survival Ascended crashed three times and topped out near 45 FPS despite an unsafe/unmanaged-heavy implementation, to argue relaxed memory safety isn't a performance free lunch; states a personal preference for "a 10% perf hit (40 FPS) for a memory safe implementation that doesn't crash," and separately reports deliberately abandoning an early Bevy game project after three months as a "fail fast" call once its immaturity became clear, later moving to Godot Quote: "Personally, I would prefer a 10% perf hit (40 FPS) for a memory safe implementation that doesn't crash." [`b-sb26-f013214-c4`, team b]
  - `rust-vs-c-inherent-performance--p1` — rust-idioms-default-to-faster-collections
    - **Bryan Cantrill** · Source `f005516` · date undated in this source (an anonymous commenter quotes a Cantrill talk via youtu.be/HgtRAbE1nBM?t=2450 with no air date given here; two Cantrill blog posts are also named — bcantrill.dtrace.org/2018/09/18/falling-in-love-with-rust/ and .../2018/09/28/the-relative-performance-of-c-and-rust/ — whose URL-embedded dates, 2018-09-18 and 2018-09-28, are not independently confirmed since those posts were not fetched) · locator blockquote citing "Bryan Cantrill @ https://youtu.be/HgtRAbE1nBM?t=2450" — argues Rust's composability lets him reach for a B-Tree where in C he'd stick to an AVL tree, because an intrusive C B-Tree implementation is too risky to trust ("up in everything's underwear") Quote: "the reason I could use a B-Tree and not an AVL tree, is because of that composability of Rust... I would still use an AVL tree in C even though I know I'm giving up some small amount of performance, but in Rust, I get to use a B-Tree." [`a-sa15-f005516-c1`, team a]
- Positions seen by the extractor (`a-saL1-f005516-q1`): no-inherent-advantage-social-factors-dominate; stronger-type-system-enables-compiler-optimizations-c-lacks; rust-has-real-overheads-that-hurt-practical-perf
- Positions seen by the extractor (`a-saL1-f005516-q3`): safe-rust-init-requirement-has-real-perf-cost; init-cost-is-narrow-edge-case-not-general-issue
- Positions seen by the extractor (`a-saL1-f005516-q4`): composability-enables-better-real-world-data-structures; borrow-checker-forces-costly-refactors-and-copies
- Positions seen by the extractor (`b-sb26-f013214-q2`): a demanding, highly concurrent 3D client is fully achievable in 100% safe Rust with no `unsafe` (John_Nagle); a measurable performance cost for memory safety is an acceptable, even preferable, trade — "playing loose with safety" is not a free lunch for performance either, evidenced by a shipped title with safety-linked crashes (parasyte)

### `shared-mutable-state-vs-explicit-passing`

**Question.** When to use `Rc`/`Arc` with `RefCell`/`Mutex`, and when to restructure for single ownership, explicit `&mut` or context passing?

- Grouping: Same concrete choice; object graphs, `Arc<Self>` receivers and runtime-tracked UI handles stay apart.
- Teams: a, b · members (context): `a-sR07-f002155-q1` (f002155, embedded, core); `a-sa06-f003414-q2` (f003414, desktop-cli-ui, core); `b-sT09-f005440-q1` (f005440, core); `b-sb04-f001022-q1` (f001022, desktop-cli-ui, core)
- Domains: core, desktop-cli-ui, embedded
- Concepts: interior mutability; Arc; Sync bounds; ownership design; API design; ownership; Box; Rc; RefCell; borrow checker; borrow panics; event loop; context-passing pattern
- Positions:
  - `shared-mutable-state-vs-explicit-passing--restructure-for-explicit-ownership` — Avoid implicit shared state; pass context or `&mut`, drop forced `Arc`
    - **Yatekii** · Source `f002155` · date 2024-12-03 · locator comment "I dont think the Mutex is necessary as the sequences are held on the session which should then go into the mutex. Not internally." — rather than adding a `Mutex` inside the type to satisfy a `Sync` bound, move the mutable state to the owning `Session` and access it there Quote: "I dont think the Mutex is necessary as the sequences are held on the session which should then go into the mutex." [`a-sR07-f002155-c1`, team a]
    - **Yatekii** · Source `f002155` · date 2024-12-19 · locator comment "Ah, I disregarded that fact. I would prefer no Arc 🤔 Maybe we can reevaluate in the future." — prefers avoiding Arc-based shared ownership for this type even after conceding the immediate `Sync` constraint requires it, wanting to revisit the design later Quote: "I would prefer no Arc 🤔 Maybe we can reevaluate in the future." [`a-sR07-f002155-c2`, team a]
    - **ConradIrwin** · Source `f003414` · date 2025-10-28 · locator comment 2025-10-28T01:59:12Z — objects to a `Buffer` containing an `Arc<Mutex<>>` that lets callers change encoding without the buffer knowing; wants the encoding passed/returned explicitly instead Quote: "I don't like that the Buffer contains an Arc<Mutex<>> that allows callers to change the encoding without the buffer knowing" [`a-sa06-f003414-c2`, team a]
    - **romgrk** · Source `f001022` · date 2024-03-02 · locator PR #8632, comment 2024-03-02T18:19:01Z — retracts an earlier suggestion to turn the client state fields into `Rc<RefCell<_>>`s, since dispatching an action from inside an active borrow (e.g. a key press changing the keyboard-focused window) would still panic; the only approach that currently works is cloning whatever refs are needed before dropping the state and then dispatching Quote: "Actually I'm not sure that would work." [`b-sb04-f001022-c1`, team b]
    - **romgrk** · Source `f001022` · date 2024-03-02 · locator PR #8632, comment 2024-03-02T18:19:01Z — floats passing a `cx` context down the stack, mirroring the pattern the rest of the codebase already uses, as a way to sidestep the reentrant-borrow panic entirely, alongside noting that Warp's Rust UI blog describes hitting the same `RefCell`/`borrow_mut` crash class in production Quote: "the rest of the codebase seems to be using the pattern of passing a `cx` context down the stack, which avoids this kind of issue" [`b-sb04-f001022-c2`, team b]
  - `shared-mutable-state-vs-explicit-passing--shared-where-structure-demands` — `Rc`/`Arc` where reader count is hard to know; `RefCell` narrowly
    - **Serdar Yegulalp (InfoWorld senior writer)** · Source `f005440` · date 2025-02-12 · locator § Automatic memory management and Rust types, paragraphs 3–4 — Rc and Arc are recommended when it is hard to tell how many readers a piece of data will have. RefCell moves the borrow rules to run time, works only in single-threaded code and panics on violation. Hence it fits only a narrow range of problems. Quote: "Do use them when the structure of a program makes it hard to tell how many readers will exist for a given piece of data." (flag: voice-unverified) [`b-sT09-f005440-c1`, team b]
- Positions seen by the extractor (`a-sR07-f002155-q1`): prefer-redesign-over-mutex-or-arc (Yatekii)
- Positions seen by the extractor (`a-sa06-f003414-q2`): no implicit shared mutable state, make changes explicit in the type signature
- Positions seen by the extractor (`b-sT09-f005440-q1`): Rc/Arc when reader count is hard to know, RefCell only for a narrow set of runtime-only problems
- Positions seen by the extractor (`b-sb04-f001022-q1`): rc-refcell-doubtful, context-passing-preferred

### `default-features-minimal-vs-inclusive`

**Question.** Should an optional capability (a format, codec or heap profiling) be on in a crate's default features, or opt-in?

- Grouping: Same Cargo-defaults choice; image formats, engine codecs and production heap profiling are contexts.
- Absorbs merge-final ids: `heap-profiling-default`, `per-capability-features-vs-bundled`
- Teams: a, b · members (context): `a-sa02-f002127-q1` (f002127, desktop-cli-ui); `a-sa26-f011684-q1` (f011684, core, other); `b-sb25-f011435-q2` (f011435, web, core)
- Domains: core, desktop-cli-ui, other, web
- Concepts: feature flags; API defaults; crate ecosystem curation; memory profiling; build features; observability tooling; binary size; compile time; dependency count
- Positions:
  - `default-features-minimal-vs-inclusive--inclusive-defaults` — Enable by default for minimal friction
    - **clarfonthey** · Source `f002127` · date 2024-10-02 · locator PR comment — weighing reviewer pushback that niche formats (QOI, GIF) shouldn't be defaults, the author leans toward shipping with minimal friction now and adjusting defaults later rather than pre-curating by popularity Quote: "Kinda just would prefer the path of least friction and we can change the defaults later." [`a-sa02-f002127-c1`, team a]
  - `default-features-minimal-vs-inclusive--minimal-defaults` — Compile in only what is used
    - **Nico** · Source `f011435` · date 2026-06-11 · locator ~31:30-32:31 (audience Q&A on dependency counts) — contrasts Servo's ~1,000 dependencies (dominated by SpiderMonkey, WebGL, XR) with Blitz's ~300, achieved by enabling only 4 of 20 available image codecs by default and making SVG/networking support opt-in per deployment Quote: "you should be able to only compile in what you're actually using" [`b-sb25-f011435-c2`, team b]
  - `default-features-minimal-vs-inclusive--unresolved-reported` — Reported as an open debate, no side taken (heap profiling)
    - **Lei Huang** · Source `f011684` · date 2024-01-31 · locator section "Enabling Heap Profiling in GreptimeDB" — GreptimeDB currently ships with heap profiling (mem-prof) off by default, compiled in only via a cargo feature flag; whether it should be on by default is an active, unresolved discussion the author points readers to rather than settles Quote: "The discussion about whether the mem-prof feature should be enabled by default is ongoing in greptimedb#3166. You are welcome to share your opinion there" [`a-sa26-f011684-c1`, team a]
- Positions seen by the extractor (`a-sa02-f002127-q1`): prefer-minimal-friction-defaults (PR author), curate-by-popularity-or-quality (reviewers, unattributed)
- Positions seen by the extractor (`a-sa26-f011684-q1`): currently-off-by-default-with-open-internal-debate (GreptimeDB team, no side taken by this Voice)
- Positions seen by the extractor (`b-sb25-f011435-q2`): default to the smallest compiled surface, enabling codecs/capabilities one at a time per deployment (Blitz: ~300 total dependencies, 4 image codecs enabled by default of 20 available); accept a large bundled dependency tree because the core scripting engine alone dominates it anyway (implicit contrast drawn with Servo's ~1,000 dependencies, dominated by SpiderMonkey)

### `enum-vs-dyn-trait-closed-set`

**Question.** Should a set of kinds be modelled as an enum or as trait objects (`dyn Trait`, an open trait)?

- Grouping: Same enum-vs-trait-object choice; closed node kinds and an extensible policy are contexts where the answer flips.
- Absorbs merge-final ids: `closed-enum-vs-open-trait-for-policy`
- Teams: a, b · members (context): `a-sa07-f003704-q3` (f003704, ml, core); `a-sa17-f007884-q1` (f007884, desktop-cli-ui, core); `b-sR10-f004741-q3` (f004741, decentralized-iroh, distributed, core)
- Domains: core, decentralized-iroh, desktop-cli-ui, distributed, ml
- Concepts: enums; sum-types; trait-objects; extensibility; unsafe; dynamic dispatch (dyn Trait); tagged pointers; memory layout; traits; API design
- Positions:
  - `enum-vs-dyn-trait-closed-set--static-by-default` — Enums or generics; avoid `dyn` when possible
    - **antimora** · Source `f003704` · date 2025-11-07 · locator PR #3872, comment 2025-11-07T15:47:01Z — agreed, after offline discussion, to redo the Graph representation as node enums Quote: "We will redo as a graph of node enums" [`a-sa07-f003704-c3`, team a]
    - **alonely0** · Source `f007884` · date 2024-04-28 · locator § "Enum dispatch", opening — Recommends enums (enum_dispatch-style) as the default over dynamic dispatch for a fixed set of known types, since it drops heap allocation and vtable indirection while staying entirely safe. Quote: "The naive approach, which is the one I'd recommend myself, would be to use enums." [`a-sa17-f007884-c1`, team a]
    - **alonely0** · Source `f007884` · date 2024-04-28 · locator § "A first attempt: dynamic dispatch", closing paragraph — Treats Box<dyn Trait> as the slowest and least idiomatic option, worth using mainly as a guaranteed-two-word size bound or as a fallback for one oversized enum variant, to be avoided otherwise. Quote: "it's the slowest and least idiomatic" [`a-sa17-f007884-c2`, team a]
  - `enum-vs-dyn-trait-closed-set--open-trait-for-extensibility` — An open trait for extensible policy
    - **Friedel Ziegelmayer & Rüdiger Klaehn (iroh/n0 computer)** · Source `f004741` · date 2026-05-27 · locator section "🔐 Pluggable relay access control" — the closed `AccessConfig` enum was replaced by an open `AccessControl` trait with `on_connect`/`on_disconnect` hooks, so embedders can implement arbitrary policy rather than choosing among enum variants Quote: "The relay's access control has been redesigned. The AccessConfig enum is gone, replaced by an AccessControl trait with on_connect and on_disconnect hooks." [`b-sR10-f004741-c3`, team b]
  - `enum-vs-dyn-trait-closed-set--unsafe-unions-for-memory` — Unsafe unions when memory must be squeezed
    - **alonely0** · Source `f007884` · date 2024-04-28 · locator § "Now with unions, also known as C's untagged enums..." — Goes beyond the enum-dispatch default into unsafe unions with hand-rolled tagged pointers (ManuallyDrop, ptr aliasing via transmute_copy) to shrink the value below the default enum's size, treating it as a deliberate, specialized escalation past safe Rust when memory layout is worth the unsafety. Quote: "Unions are not just an archaic tool from the long forgotten era of Dennis Ritchie, they are still a very useful tool which can yield amazing results in the right han[ds]" [`a-sa17-f007884-c3`, team a]
- Positions seen by the extractor (`a-sa07-f003704-q3`): enum-of-nodes (antimora, adopted after offline discussion)
- Positions seen by the extractor (`a-sa17-f007884-q1`): enum-dispatch-default, dyn-trait-avoid-when-avoidable, unsafe-unions-for-memory-squeeze
- Positions seen by the extractor (`b-sR10-f004741-q3`): trait-over-enum

### `http-error-status-in-result`

**Question.** Should HTTP-level error statuses travel in `Err` or as `Ok(response)`?

- Grouping: Same choice for handlers and tower middleware.
- Absorbs merge-final ids: `ratelimit-middleware-err-vs-shortcircuit`
- Teams: a, b · members (context): `a-saL1-f005454-q1` (f005454, web, core); `b-sb22-f008906-q3` (f008906, cloud-workers, web); `b-sb22-f008906-q4` (f008906, cloud-workers, distributed)
- Domains: cloud-workers, core, distributed, web
- Concepts: HTTP API design; sum types for responses; OpenAPI generation; `?` operator ergonomics; tower Service::Future's Result; error propagation; Lambda invocation errors; middleware API design; short-circuiting; error typing
- Positions:
  - `http-error-status-in-result--unified-response-type` — Errors are ordinary responses (`Ok(response)`, one enum)
    - **CobaltCause** · Source `f005454` · date 2025-02-24 · locator reply, 2025-02-24T19:01:11-06:00 — Describes a design where all HTTP responses (success and error) live in one enum returned directly by the handler (not wrapped in `Result`), which keeps status-code categorization simple but means `?` doesn't work directly and needs a separate inner function plus manual matching to bridge back into the enum. Quote: "there aren't really 'successful' or 'unsuccessful' responses, just responses... you have to define a separate function that returns e.g. `Result`... and then use `match`... to convert the `Result`'s inner values into your handler function's enum." [`a-saL1-f005454-c1`, team a]
    - **Luciano Mammino** · Source `f008906` · date 2026-05-03 · locator section "The HTTP rule of thumb" — an `Err` that escapes all the way to `lambda_http::run` is treated as an invocation error, so API Gateway answers the client with a generic 502 instead of the carefully designed 401/403/429/500 — avoiding that confusion is the entire reason for the rule Quote: "Return Ok(response) for anything you want the client to see, even when the response is a 401, 403, 429, or 500." [`b-sb22-f008906-c3`, team b]
    - **Luciano Mammino** · Source `f008906` · date 2026-05-03 · locator section "Back to the rate limiter" — weighed both designs explicitly — a descriptive `Err` keeps callers in full control of the response shape but requires every consumer to write a translation layer; a pre-baked `Ok(response)` "just works" the moment it's dropped into a `ServiceBuilder`, at the cost of a baked-in response shape (mitigated later with `on_over_limit`/`on_unavailable` override hooks) Quote: "We will go with option 2. A drop-in middleware that just works is worth a lot in practice." [`b-sb22-f008906-c4`, team b]
  - `http-error-status-in-result--errors-in-err-channel` — Split success and error types so `?` works
    - **sunshowers** · Source `f005454` · date 2025-02-24 · locator reply, 2025-02-24T19:22:07-06:00 — Suggests separating response variants into a Result-like type split along status-code ranges (2xx/3xx success vs. 4xx/5xx error) to restore `?`-operator usability. Quote: "What do you think of separating out successful and unsuccessful variants into a result type? 2xx and 3xx on one side, 4xx and 5xx on the other." [`a-saL1-f005454-c2`, team a]
    - **CobaltCause** · Source `f005454` · date 2025-02-24 · locator reply, 2025-02-24T21:22:14-06:00 — Grants the split-type approach could work and would make `?` more usable, at the cost of extra library-side complexity (needing a `SuccessStatusCode` alongside Dropshot's existing `ErrorStatusCode`), while noting personally it wouldn't matter much since he keeps HTTP-aware code out of his core business logic anyway. Quote: "That could work. I think doing it that way could be more convenient for users because `?` would be usable... but at the cost of some library-side complexity." [`a-saL1-f005454-c3`, team a]
- Positions seen by the extractor (`a-saL1-f005454-q1`): unified-enum-simpler-framework; split-success-error-for-ergonomics
- Positions seen by the extractor (`b-sb22-f008906-q3`): return `Ok(response)` for anything the client should see, and reserve `Err` for transport-level failures an outer layer is actually prepared to translate — otherwise an escaped `Err` becomes a generic 502 at the API Gateway, burying the intended status code (Luciano Mammino)
- Positions seen by the extractor (`b-sb22-f008906-q4`): short-circuit with a pre-baked `Ok(response)`, trading response-shape flexibility for a middleware that works with zero extra code the moment it's dropped into a `ServiceBuilder` (Luciano Mammino)

### `in-app-vs-infrastructure-concern`

**Question.** Should operational concerns (TLS termination, rate limiting, flood protection) be handled inside the Rust service or by infrastructure in front (nginx, reverse proxy, API gateway)?

- Grouping: Same placement choice; sa14's "replaced nginx vs removed its role" Question is restored here.
- Absorbs merge-final ids: `rate-limit-middleware-vs-gateway`
- Teams: a, b · members (context): `a-sa14-f005360-q4` (f005360, web); `b-sT09-f005312-q1` (f005312, web, cloud-workers); `b-sb22-f008906-q6` (f008906, cloud-workers)
- Domains: cloud-workers, web
- Concepts: reverse proxy responsibilities; operational concerns; decoupling; Rocket built-in TLS; reverse proxy; deployment; API Gateway usage plans; quota headers; serverless rate limiting
- Positions:
  - `in-app-vs-infrastructure-concern--delegate-tls-to-proxy` — Terminate TLS in a reverse proxy
    - **Vaultwarden maintainers (dani-garcia/vaultwarden)** · Source `f005312` · date 2024-08-14 (frame date; the README revision read is undated and current) · locator README § Usage, paragraph "While Vaultwarden is based upon the Rocket web framework…" — Rocket supports TLS, but the maintainers recommend setting up a reverse proxy instead and link to proxy examples. The README also requires HTTPS for the web vault. Quote: "While Vaultwarden is based upon the Rocket web framework which has built-in support for TLS our recommendation would be that you setup a reverse proxy" (flag: voice-unverified) [`b-sT09-f005312-c1`, team b]
  - `in-app-vs-infrastructure-concern--rate-limit-in-app` — Build rate limiting in the app; gateway usage plans fall short
    - **Luciano Mammino** · Source `f008906` · date 2026-05-03 · locator section "Why not just use API Gateway usage plans?" — usage plans don't exist at all on HTTP API v2, are invisible to clients even on REST (no `X-RateLimit-*` headers, just a bare 429), require API keys pre-provisioned up to a hard cap of 10,000 per account/region, and only offer DAY/WEEK/MONTH windows rather than the 15-minute window the tutorial wants Quote: "Even on REST, usage plans are invisible to clients... There are no X-RateLimit-* response headers (or any other quota hint)." [`b-sb22-f008906-c6`, team b]
  - `in-app-vs-infrastructure-concern--p1` — a self-written in-process server removes nginx's role rather than replacing it
    - **pm** · Source `f005360` · date 2024-10-13 · locator comment 2024-10-13T14:37:28 — argues that what's being described is removing nginx, not replacing it, because nginx's actual value is providing decoupled operational concerns (flood protection, bandwidth throttling, load balancing, TLS termination) that the new in-process server doesn't reproduce Quote: "Nginx is often put in front of http services written in any language... People do it for performance reasons and to access solutions to problems that can be decoupled from the actual response logic" [`a-sa14-f005360-c7`, team a]
- Positions seen by the extractor (`a-sa14-f005360-q4`): this is removing, not replacing — nginx's real value is providing operational concerns decoupled from the response logic, which a self-written in-process server doesn't reproduce just by serving the same requests
- Positions seen by the extractor (`b-sT09-f005312-q1`): reverse proxy in front, framework TLS unused
- Positions seen by the extractor (`b-sb22-f008906-q6`): build custom middleware — usage plans don't exist on HTTP API v2, expose no `X-RateLimit-*` client-facing quota headers even on REST APIs, cap at 10,000 API keys per account/region, and only offer coarse DAY/WEEK/MONTH windows (Luciano Mammino)

### `tokio-as-default-runtime`

**Question.** Tokio as the default async runtime, or alternatives?

- Grouping: Same choice in three sources.
- Teams: a, b · members (context): `a-sa29-f012940-q2` (f012940, web, distributed, cloud-workers); `b-bk01-f000233-q3` (f000233, core, web, distributed); `b-sb17-f005159-q1` (f005159, decentralized-iroh)
- Domains: cloud-workers, core, decentralized-iroh, distributed, web
- Concepts: async runtime; Tokio; networking ecosystem; alternate runtimes; async-std; smol; async runtime choice; platform support; ecosystem maturity
- Positions:
  - `tokio-as-default-runtime--tokio-default` — Tokio
    - **Dhruv Ahuja** · Source `f012940` · date 2026-03-11 · locator section "Powered by Tokio" — describes the demo's web server and telemetry layer as built on Tokio, characterizing it as "often regarded as the one true async runtime" and the power behind much of Rust's networking ecosystem, without naming or engaging any specific alternative-runtime advocate Quote: "Tokio, which is often regarded as the one true async runtime, and powers much of Rust's networking ecosystem" [`a-sa29-f012940-c2`, team a]
    - **Rüdiger Klaehn** · Source `f005159` · date 2024-07-31 · locator article body, "Choosing a Runtime" section — despite criticisms of Tokio, judges the alternatives (async-std stale, smol inactive, glommio Linux-only) too limited, and picks Tokio as iroh's runtime, reinforced by it being quinn's default Quote: "Although there are criticisms of Tokio, the alternatives are limited... Consequently, Tokio remains the best option for iroh." [`b-sb17-f005159-c1`, team b]
  - `tokio-as-default-runtime--p1` — Tokio as default runtime
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "Async and Await" § The runtime — recommends Tokio as the runtime for most of the guide because it is general purpose, the most popular in the ecosystem, and good for both getting started and production; notes other runtimes may give better performance or simpler code in some circumstances. Quote: "It's a general purpose runtime and is the most popular runtime in the ecosystem." [`b-bk01-f000233-c3`, team b]
  - `tokio-as-default-runtime--p2` — no official recommendation, list options neutrally
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "The Async Ecosystem" § Popular Async Runtimes — states flatly that no runtime is officially recommended and lists Tokio, async-std, smol and fuchsia-async as options without ranking them, then discusses cross-runtime incompatibility (Tokio's mio-based reactor and its own AsyncRead/AsyncWrite are not directly compatible with async-std/smol, which use the async-executor crate and futures' I/O traits) as a reason to research fit before committing. Flagged as an internal conflict: this contradicts this same source's earlier, newer chapter recommending Tokio by name as the default (see the Tokio-as-default Claim above) — the book's own top-of-page notice that it is "currently undergoing a rewrite" and that the `print.html` output concatenates old and new chapters is the likely mechanism (see this section's Coverage note). Quote: "There is no asynchronous runtime in the standard library, and none are officially recommended." [`b-bk01-f000233-c4`, team b]
- Positions seen by the extractor (`a-sa29-f012940-q2`): Tokio as the de facto default ("often regarded as the one true async runtime") for this kind of application (Dhruv Ahuja) vs. no named counter-voice in this source (flagged as weakly evidenced — the hedge "often regarded as" signals contested status without naming who contests it)
- Positions seen by the extractor (`b-bk01-f000233-q3`): Tokio as default (chapter "Async and Await"); no official recommendation, list options neutrally (chapter "The Async Ecosystem") — an internal conflict between the book's rewritten and older chapters, see Claims
- Positions seen by the extractor (`b-sb17-f005159-q1`): tokio-is-the-best-practical-choice (Rüdiger Klaehn)

### `typed-wrapper-vs-raw-access`

**Question.** Should low-level data (registers, byte stores, raw matrices) be accessed through typed wrappers or accessors, or raw?

- Grouping: Same typed-wrapper choice; PAC registers, a key-value store and nalgebra transforms are contexts.
- Absorbs merge-final ids: `pac-typed-accessors-vs-raw-bitops`
- Teams: a, b · members (context): `a-sB01-f000217-q2` (f000217, core); `a-sa09-f004055-q1` (f004055, embedded); `b-bk03-f000267-q8` (f000267, core, distributed)
- Domains: core, distributed, embedded
- Concepts: newtype-invariants; raw-matrix-flexibility; unsafe; register-access; API-design; type safety; newtype pattern; database access patterns
- Positions:
  - `typed-wrapper-vs-raw-access--encode-in-types` — Encode it in types
    - **jamesmunns** · Source `f004055` · date 2026-01-05 · locator comment @jamesmunns 2026-01-05T14:14:27Z — repeatedly questions raw volatile register operations in favor of PAC-generated typed accessors Quote: "Why use raw volatile ops here instead of PAC operations?" [`a-sa09-f004055-c1`, team a]
    - **felipebalbi** · Source `f004055` · date 2026-01-07 · locator comment @felipebalbi 2026-01-07T19:35:31Z — treats a missing PAC accessor as a bug to be fixed in the PAC itself rather than worked around with manual bit ops Quote: "PAC gives you accessors for these bits, if it doesn't, let me know so we can patch the PAC as that would be a bug." [`a-sa09-f004055-c2`, team a]
  - `typed-wrapper-vs-raw-access--p1` — dedicated types recommended over raw matrices
    - **Dimforge (nalgebra maintainers)** · Source `f000217` · date capture 2025-01-21 (Wayback; underlying doc undated) · locator "Computer-graphics recipes" chapter, "Transformations using Matrix4" — Argues a raw Matrix4 cannot guarantee it represents a pure rotation, isometry, or even an invertible transform, so dedicated transformation types are recommended instead Quote: "That's why all the transformation types are recommended instead of raw matrices." [`a-sB01-f000217-c2`, team a]
  - `typed-wrapper-vs-raw-access--p2` — typed-wrapper-over-raw-api
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Zebra Cached State Database Implementation § Adding a Column Family — most column families could be accessed with low-level methods taking any type, but that is error-prone (wrong types on read vs write, a typo'd column-family-name string causing a panic); instead, define the name and type of each column family once, add a typed method that returns that type, and route every read/write through it Quote: "If we type the column family name out every time, a typo can lead to a panic, because the column family doesn't exist." (flag: voice-unverified) [`b-bk03-f000267-c8`, team b]
- Positions seen by the extractor (`a-sB01-f000217-q2`): dedicated types recommended, raw matrices lack guarantees
- Positions seen by the extractor (`a-sa09-f004055-q1`): typed-pac-preferred, raw-manual-bitops
- Positions seen by the extractor (`b-bk03-f000267-q8`): typed-wrapper-over-raw-api

### `bounded-grid-universe`

**Question.** How should an in-principle infinite simulation grid be bounded in finite memory: a growing region, fixed edges, or a fixed periodic (toroidal) universe?

- Grouping: Both teams logged the same Rust+Wasm book chapter.
- Teams: a, b · members (context): `a-sB02-f000256-q2` (f000256, wasm, core); `b-bk02-f000256-q1` (f000256, wasm)
- Domains: core, wasm
- Concepts: memory bounding; cellular automata; state representation; memory bounds
- Positions:
  - `bounded-grid-universe--p1` — fixed-periodic(chosen)
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Implementing Conway's Game of Life" — "Design" — "Infinite Universe" — of three ways to bound the infinite universe (expanding dirty-region tracking, fixed non-periodic, fixed periodic/wraparound), the tutorial picks periodic wraparound because unbounded expansion risks running out of memory and fixed non-periodic edges snuff out infinite patterns like gliders. Quote: "We will implement the third option." [`a-sB02-f000256-c2`, team a]
  - `bounded-grid-universe--p2` — fixed-size, periodic (toroidal) universe, over unbounded-growable or fixed-non-wrapping
    - **rustwasm working group (Rust and WebAssembly book) [voice-unverified]** · Source `f000256` · date unknown (living doc) · locator § "Implementing Conway's Game of Life" → Design → Infinite Universe — names three ways to bound an infinite universe in finite memory — unbounded expansion (worst case: unbounded slowdown/OOM), fixed edges (kills patterns like gliders that reach the boundary), and fixed periodic wrap-around — and picks the third so patterns "can keep running forever." Quote: "We will implement the third option." [`b-bk02-f000256-c1`, team b]
- Positions seen by the extractor (`a-sB02-f000256-q2`): growing-region, fixed-non-periodic, fixed-periodic(chosen)
- Positions seen by the extractor (`b-bk02-f000256-q1`): growable region (unbounded, risks OOM); fixed non-wrapping edges (kills edge-crossing patterns); fixed periodic/toroidal wrapping (chosen)

### `cancel-safety-requirement`

**Question.** Must async Rust APIs (RPC channels, mpmc `recv`) be cancel-safe?

- Grouping: Same requirement asked of iroh RPC and of channel crates.
- Absorbs merge-final ids: `channel-cancel-safety`
- Teams: a, b · members (context): `a-sT04-f001650-q1` (f001650, core, decentralized-iroh, distributed); `b-sb17-f005159-q4` (f005159, decentralized-iroh)
- Domains: core, decentralized-iroh, distributed
- Concepts: async; cancellation safety; futures; RPC; channels; cancel safety; `Future::poll` cancellation; mpmc channels; flume; async-channel
- Positions:
  - `cancel-safety-requirement--cancel-safety-required` — Cancel safety is required; its absence is a bug or rules a crate out
    - **ramfox (byline, iroh blog; Rust connection in source: iroh release post, Rust code, and "the quic-rpc crate, which is a crate that we've written")** · Source `f001650` · date 2024-06-27 · locator section "Better late than never" — The team broke its two-week release cadence because it found a rare, high-load critical bug: its RPC channels were not cancel-safe. They fixed it in quic-rpc and upgraded iroh before releasing. The documented-caller-responsibility alternative is not named in the source; the Position rests on the stated reason (critical bug, fix immediately). Quote: "Turns out, our RPC channels were not cancel-safe." (flag: voice-unverified Not logged, as practice with no reason (rule 8): the ProtocolBuilder, `Builder::disable_docs()`, the RPC connection APIs, the relay config changes, and the Breaking Changes list (for example "Builder loses the E type parameter").) [`a-sT04-f001650-c1`, team a]
    - **Rüdiger Klaehn** · Source `f005159` · date 2024-07-31 · locator article body, "Choosing an mpmc channel" section — found flume's `recv` occasionally not cancel-safe in practice (lost notifications causing stuck tasks), and requires cancel-safety on recv even though flume intentionally accepts a cancel-safety gap on `send` for performance; switches to async-channel, which fixed the reproducer Quote: "cancel safety for recv is a must in many places where we use it internally... So for now we are going to use async-channel as the standard mpmc queue." [`b-sb17-f005159-c4`, team b]
- Positions seen by the extractor (`a-sT04-f001650-q1`): cancel-safety-required-in-library
- Positions seen by the extractor (`b-sb17-f005159-q4`): cancel-safe-recv-is-a-must (Rüdiger Klaehn)

### `derive-arithmetic-ops`

**Question.** Should std provide `#[derive]` for arithmetic operator traits with field-wise semantics?

- Grouping: Both teams logged the same thread.
- Teams: a, b · members (context): `a-sa19-f009292-q1` (f009292, core); `b-sb22-f009292-q1` (f009292, core)
- Domains: core
- Concepts: derive macros; operator overloading; newtypes; affine spaces; std-vs-ecosystem scope; affine vs. vector spaces
- Positions:
  - `derive-arithmetic-ops--support-fieldwise-derive` — Add it, like Clone/Debug
    - **vangata-ve** · Source `f009292` · date 2025-09-02 · locator OP, 2025-09-02T17:06:42.006Z — Manually implementing Add/Sub/Mul/Div for structs where field-wise operation is the obviously sensible behaviour is needless busywork; std should support deriving them the way it does Clone/Debug/Copy. Quote: "This is pointless busywork when the only sensible behavior is to perform the operation field by field." [`a-sa19-f009292-c1`, team a]
    - **vangata-ve** · Source `f009292` · date 2025-09-02 · locator opening post, section "Rationale" — hand-writing (or pulling in `derive_more` for) trivial field-wise arithmetic on numeric structs is unnecessary busywork std could eliminate the way it already does for `Clone`; the derive would require `T: Add` on generic fields and intentionally excludes enums, where manual impls are judged clearer Quote: "This is pointless busywork when the only sensible behavior is to perform the operation field by field." [`b-sb22-f009292-c1`, team b]
    - **DragonDev1906** · Source `f009292` · date 2025-09-04 · locator reply timestamped 2025-09-04T07:06:14 — draws a direct analogy to deriving `Debug` on a struct holding a large `Vec<u8>` — not always the ideal implementation, but still a sane default you skip when it doesn't fit; points to `derive_more`'s existing arithmetic derives as evidence of real demand Quote: "the existence of them in derive_more shows that they are useful and the most sane default implementation is fieldwise operation." [`b-sb22-f009292-c4`, team b]
  - `derive-arithmetic-ops--oppose-semantics-ambiguous` — Reject: field-wise arithmetic is wrong or rarely useful
    - **2e71828** · Source `f009292` · date 2025-09-02 · locator reply, 2025-09-02T17:47:25.304Z — Doubts unconstrained field-wise derive is broadly useful, since most wrapper structs that need arithmetic (complex numbers, quaternions, matrices) have their own non-field-wise rules. Quote: "My main concern is whether unconstrained field-wise projection of these operators is really all that common." [`a-sa19-f009292-c2`, team a]
    - **jdahlstrom** · Source `f009292` · date 2025-09-02 · locator reply, 2025-09-02T19:56:12.974Z — Invokes affine-space math (points vs. vectors/translations) to argue field-wise addition is often meaningless, e.g. adding two geographic coordinates, so a naive derive would default to semantically wrong behaviour. Quote: "Addition and scalar multiplication make sense for vectors, but for points they are meaningless in general." [`a-sa19-f009292-c3`, team a]
    - **Vorpal** · Source `f009292` · date 2025-09-05 · locator reply, 2025-09-05T08:06:03.300Z — Even for simple newtypes there is no single correct semantics (e.g. whether Radians/Degrees arithmetic should wrap modulo 2π/360), unlike Clone or Debug where the standard derive is almost always right. Quote: "It is not obvious what the derives for arithmetic operators should do. There isn't a single right answer." [`a-sa19-f009292-c4`, team a]
    - **2e71828** · Source `f009292` · date 2025-09-02 · locator reply timestamped 2025-09-02T17:47:25 — challenges the OP's own `TcpPort` example directly, asking why anyone would add two `TcpPort`s together, to argue the class of cases where naive field-wise addition is actually correct is narrower than the RFC assumes Quote: "My main concern is whether unconstrained field-wise projection of these operators is really all that common." [`b-sb22-f009292-c2`, team b]
    - **jdahlstrom** · Source `f009292` · date 2025-09-02 · locator reply timestamped 2025-09-02T19:56:12 — distinguishes vector spaces (where addition and scalar multiplication are meaningful) from affine spaces of points and translations — `Instant`/`Duration`, Celsius/Fahrenheit, geographic coordinates, pointers/`ptrdiff_t` — where adding two points is meaningless and only point+translation or point−point make sense Quote: "it makes no sense to add together the coordinates of two cities, but the difference of two coordinates is entirely meaningful." [`b-sb22-f009292-c3`, team b]
  - `derive-arithmetic-ops--prefer-delegation-mechanism` — Reject in favor of a delegation mechanism
    - **kornel** · Source `f009292` · date 2025-09-02 · locator reply, 2025-09-02T20:24:36.828Z — A basic field-wise arithmetic derive can only encode one relationship between fields (e.g. a Point), so it doesn't generalize to matrices, quaternions or complex numbers; a delegation syntax or generalized derive-construction macro would serve better. Quote: "This may be better solved by delegation syntax or generalised macros for constructing derives." [`a-sa19-f009292-c5`, team a]
  - `derive-arithmetic-ops--ecosystem-crates-suffice` — Leave it to ecosystem crates
    - **porky11** · Source `f009292` · date 2026-01-16 · locator reply, 2026-01-16T20:01:40.626Z — derive_more already covers this well; the core language/std should stay minimal and leave most conveniences to libraries, which is the point of having a package manager. Quote: "No need to have it in the core fo the language. That's kind of the point of the Rust package manager, that the core language includes the important things while most things are outsourced to libraries." [`a-sa19-f009292-c6`, team a]
- Positions seen by the extractor (`a-sa19-f009292-q1`): support-fieldwise-derive; oppose-semantics-too-ambiguous; oppose-prefer-delegation-mechanism; ecosystem-crates-suffice
- Positions seen by the extractor (`b-sb22-f009292-q1`): add it, mirroring how `#[derive(Clone)]` already works and eliminating "pointless busywork" for the unambiguous cases (vangata-ve, echoed by DragonDev1906's "useful in most cases" framing); reject or heavily qualify it, because most real wrapper types needing these traits (complex numbers, quaternions, matrices, and especially affine-space types like points, `Instant`, geographic coordinates) have non-field-wise or outright meaningless field-wise semantics (2e71828, jdahlstrom)

### `hot-patching-for-iteration`

**Question.** Should the Rust edit-compile loop use binary hot-patching (Subsecond) or faster full rebuilds?

- Grouping: Same tooling choice; b-sT05-f003044-q3 is removed as Claim-less after its strike.
- Teams: a, b · members (context): `a-sa26-f011305-q5` (f011305, core, desktop-cli-ui, embedded); `b-sb09-f002719-q1` (f002719, desktop-cli-ui, frontend, wasm)
- Domains: core, desktop-cli-ui, embedded, frontend, wasm
- Concepts: build tooling; linkers; hot reload; compile times; hot-patching; dynamic linking; codegen backend
- Positions:
  - `hot-patching-for-iteration--hot-patch` — Hot-patch for iteration speed
    - **Jonathan Kelly** · Source `f011305` · date 2025-10-03 · locator ~22:12-23:12 — "Subsecond" hot-patches running Rust binaries by recompiling only changed crates and linking them to hardcoded addresses at runtime, skipping the normal linking step, despite "a huge number of quirks, edge cases, incomprehensible behavior" needed to make it work Quote: "it bypasses the traditional cargo build system, almost completely eliminating the expensive linking step that slows down incremental development" [`a-sa26-f011305-c5`, team a]
    - **jkelleyrtp** · Source `f002719` · date 2025-03-18 · locator comment @jkelleyrtp 2025-03-18T21:13:39Z — describes "zerolink"/"thinlink", an approach that automatically dynamically links workspace crates against a cached dependencies dylib to speed up builds, alongside the subsecond hot-patching mechanism. Quote: "our new approach for drastically speeding up rust compile times by automatically using dynamic linking" [`b-sb09-f002719-c1`, team b]
    - **jkelleyrtp** · Source `f002719` · date 2025-03-19 · locator comment @jkelleyrtp 2025-03-19T20:56:59Z — reports profiling showed 100-300ms of a ~500ms build spent copying incremental artifacts to disk, and points to an upstream rustc PR aiming to remove that cost, wanting it to reach "blink and you miss it" hotpatch speed. Quote: "I did some profiling of rustc and about 100-300ms is spent copying incremental artifacts on disk." [`b-sb09-f002719-c3`, team b]
  - `hot-patching-for-iteration--faster-codegen-backend` — Faster full rebuilds via an alternate codegen backend
    - **DrewRidley** · Source `f002719` · date 2025-03-19 · locator comment @DrewRidley 2025-03-19T19:41:13Z — suggests adding the cranelift codegen backend as an optional flag for hot-reload builds, reporting it roughly halved build times on their machine (600ms to 300ms). Quote: "I found on my M3 Pro Macbook it brings down the average times from ~600ms to ~300ms." [`b-sb09-f002719-c2`, team b]
- Positions seen by the extractor (`a-sa26-f011305-q5`): bypass-the-linker-for-speed (Jonathan Kelley, re: "Subsecond")
- Positions seen by the extractor (`b-sb09-f002719-q1`): binary-hot-patching (jkelleyrtp, dx/subsecond), faster-codegen-backend (DrewRidley, cranelift)

### `immediate-vs-retained-gui`

**Question.** Immediate-mode or retained/Elm-style GUI architecture for a Rust desktop app?

- Grouping: Same architecture choice.
- Absorbs merge-final ids: `elm-style-gui-for-realtime`
- Teams: a, b · members (context): `a-sa15-f005857-q1` (f005857, desktop-cli-ui); `b-sb21-f008390-q3` (f008390, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: GUI-architecture; message-passing; subscriptions; canvas-rendering; immediate mode; retained mode; widget lifetime; GPU/game-engine integration
- Positions:
  - `immediate-vs-retained-gui--message-passing-for-realtime` — Elm-style message passing fits real-time, stateful apps
    - **Arnaud Gourlay** · Source `f005857` · date 2024-07-14 · locator "Building a UI" and "Putting it all together" sections — chose Iced specifically because the app needed an event-based library that could synchronize audio playback state with UI redraws while also supporting custom canvas drawing; used Iced's `Subscription` mechanism to pipe a `tokio::sync::watch` channel of playback ticks into UI messages, and reports being satisfied enough that he did not evaluate other GUI libraries Quote: "I needed a truly event-based library to handle the synchronization during playback while also being able to draw the tablature in a custom way with some kind of canvas abstraction... Spoiler alert: I am very happy with my choice so I did not try other libraries." [`a-sa15-f005857-c1`, team a]
  - `immediate-vs-retained-gui--doesnt-matter-at-small-scale` — The choice does not matter for small-to-medium UIs
    - **boringcactus (Melody)** · Source `f008390` · date 2025-04-16 · locator § "Digression: 'Immediate mode' and 'retained mode'" — immediate mode avoids widget-lifetime bookkeeping and is easier to integrate into a game engine's GPU loop; retained mode can perform better by not rebuilding the whole UI every frame, but at the scale of the task in this post ("Hello, world!" label + input) the difference is untestable Quote: "I'm not sure I love immediate mode on principle, although at this scale it extremely doesn't matter." [`b-sb21-f008390-c3`, team b]
- Positions seen by the extractor (`a-sa15-f005857-q1`): message-passing-fits-realtime-sync
- Positions seen by the extractor (`b-sb21-f008390-q3`): doesnt-matter-at-small-scale (boringcactus / Melody)

### `library-auth-opinionated-vs-unopinionated`

**Question.** Should a networking library impose an authentication scheme for its relays, or stay unopinionated?

- Grouping: Same choice in two iroh posts.
- Teams: a, b · members (context): `a-sT11-f004960-q1` (f004960, decentralized-iroh); `b-sR11-f004960-q1` (f004960, decentralized-iroh)
- Domains: decentralized-iroh
- Concepts: iroh relays; NAT traversal fallback; capability tokens; endpoint public keys; access control; API design; mechanism vs. policy
- Positions:
  - `library-auth-opinionated-vs-unopinionated--authenticated-managed-default` — The managed service authenticates relays by default (a10a, split from a10)
    - **n0, inc. (Iroh Services), post by Rae McKelvey** · Source `f004960` · date 2026-07-30 · locator intro ("we've decided that managed relays on Iroh Services are now authenticated by default") and "The problem: a relay URL is a credential you can't revoke" — an open relay's URL ships in every client and leaks, so anyone can spend its finite bandwidth. Managed relays deployed from June 2026 onward require a signed, expiring, endpoint-bound token issued from the project's API key, while earlier relays stay open unless switched. For self-run relays, iroh leaves authentication to the operator Quote: "If the relay accepts anyone, then anyone who learns its URL can push traffic through it." (flag: voice-unverified (Rust connection in source: iroh Rust API code, `use iroh::Endpoint`)) [`a-sT11-f004960-c1a`, team a]
  - `library-auth-opinionated-vs-unopinionated--unopinionated-library` — The library stays unopinionated; operators choose the scheme for self-hosted relays (a10b, split from a10)
    - **n0, inc. (Iroh Services), post by Rae McKelvey** · Source `f004960` · date 2026-07-30 · locator intro ("we've decided that managed relays on Iroh Services are now authenticated by default") and "The problem: a relay URL is a credential you can't revoke" — an open relay's URL ships in every client and leaks, so anyone can spend its finite bandwidth. Managed relays deployed from June 2026 onward require a signed, expiring, endpoint-bound token issued from the project's API key, while earlier relays stay open unless switched. For self-run relays, iroh leaves authentication to the operator Quote: "If the relay accepts anyone, then anyone who learns its URL can push traffic through it." (flag: voice-unverified (Rust connection in source: iroh Rust API code, `use iroh::Endpoint`)) [`a-sT11-f004960-c1b`, team a]
    - **Rae McKelvey (iroh / n0)** · Source `f004960` · date 2026-07-30 · locator "The problem: a relay URL is a credential you can't revoke" section — self-run relays are untouched — "you can build your own authentication scheme" — while managed relays now default to API-key-scoped tokens Quote: "iroh is unopinionated about that" [`b-sR11-f004960-c1`, team b]
- Positions seen by the extractor (`a-sT11-f004960-q1`): authenticated by default (managed relays); open relay (pre-June-2026 default, kept for existing deployments); library stays unopinionated, operator builds auth
- Positions seen by the extractor (`b-sR11-f004960-q1`): library stays unopinionated by default, ships an opinionated managed option alongside it

### `library-io-factored-out`

**Question.** Should a portable library perform its own I/O and threads, or take in-memory data and leave I/O to the caller?

- Grouping: Both teams logged the same Rust+Wasm book chapter.
- Teams: a, b · members (context): `a-sB02-f000256-q11` (f000256, wasm, embedded, core); `b-bk02-f000256-q4` (f000256, wasm, core)
- Domains: core, embedded, wasm
- Concepts: portability; I/O abstraction; wasm target constraints; sans-io design; portability across wasm/native
- Positions:
  - `library-io-factored-out--p1` — factor-out-I/O
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "How to Add WebAssembly Support to a General-Purpose Crate" — "Avoid Performing I/O Directly" — since the Web has no filesystem and only async I/O, a portable library should factor I/O out of itself, taking input slices from callers rather than reading files or performing I/O itself. Quote: "Factor I/O out of your library, let users perform the I/O and then pass the input slices to your library instead." [`a-sB02-f000256-c13`, team a]
  - `library-io-factored-out--p2` — bring-your-own-threads
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "How to Add WebAssembly Support to a General-Purpose Crate" — "Avoid Spawning Threads" — since spawning threads panics on wasm32-unknown-unknown, a portable library should factor thread spawning out to the caller, similar to factoring out I/O, which also plays nicer with apps that own a custom thread pool. Quote: "Another option is to factor out thread spawning from your library and allow users to \"bring their own threads\"." [`a-sB02-f000256-c14`, team a]
  - `library-io-factored-out--p3` — factor I/O out of a portable library; accept in-memory slices, let the caller perform I/O
    - **rustwasm working group (Rust and WebAssembly book) [voice-unverified]** · Source `f000256` · date unknown (living doc) · locator § "How to Add WebAssembly Support to a General-Purpose Crate" → Avoid Performing I/O Directly — gives a before/after refactor turning a `fs::read`-based function into one taking `&[u8]`, reasoning that the Web has no filesystem and I/O there is always asynchronous. Quote: "Factor I/O out of your library, let users perform the I/O and then pass the input slices to your library instead." [`b-bk02-f000256-c5`, team b]
- Positions seen by the extractor (`a-sB02-f000256-q11`): factor-out-I/O(recommended), bring-your-own-threads(recommended)
- Positions seen by the extractor (`b-bk02-f000256-q4`): perform I/O inside the library (implicit status quo, rejected); factor I/O out, take slices, let the caller do I/O (chosen)

### `memory-safety-and-resource-leaks`

**Question.** Do Rust's safety guarantees prevent resource leaks?

- Grouping: Both teams logged the same iroh post-mortem.
- Teams: a, b · members (context): `a-sR07-f002341-q1` (f002341, distributed, core); `b-sR05-f002341-q1` (f002341, distributed)
- Domains: core, distributed
- Concepts: memory safety guarantees; resource leaks; async task lifecycle
- Positions:
  - `memory-safety-and-resource-leaks--safety-does-not-prevent-leaks` — It does not prevent resource leaks
    - **Arqu** · Source `f002341` · date 2024-11-19 · locator "The Nitty Gritty" section, memory-issues paragraph — Rust's memory-safety guarantees address memory corruption, not leaks; the team leaked tokio tasks and threads in production and only found them through load testing and profiling Quote: "Rust's memory safety guarantees do not mitigate memory leaks" [`a-sR07-f002341-c1`, team a]
    - **Arqu (n0-computer/iroh engineer, production post-mortem author)** · Source `f002341` · date 2024-11-19 · locator iroh.computer/blog/relay-down-a-post-mortem, "The Nitty Gritty" section, 2024-11-19. · L1958-L1971. — safety guarantees are not sufficient; the team had to add load simulation, profiling and explicit fixes for two separate leaked-task/thread bugs, and states the gap outright. Quote: "Rust's memory safety guarantees do not mitigate memory leaks." [`b-sR05-f002341-c1`, team b]
- Positions seen by the extractor (`a-sR07-f002341-q1`): safety-does-not-prevent-leaks (Arqu)
- Positions seen by the extractor (`b-sR05-f002341-q1`): safety guarantees are not sufficient; the team had to add load simulation, profi (Arqu (n0-computer/iroh engineer, production post-mortem author))

### `mutex-vs-atomics`

**Question.** Locks or lock-free atomics for shared mutable state?

- Grouping: Same choice in two sources.
- Teams: a, b · members (context): `a-sa17-f007846-q1` (f007846, ml, core); `b-sb18-f005600-q1` (f005600, core, distributed)
- Domains: core, distributed, ml
- Concepts: concurrency; atomics; Mutex; rayon; locks; compare-and-swap; deadlock; livelock
- Positions:
  - `mutex-vs-atomics--atomics-over-locks` — Avoid locks; prefer atomics
    - **Kerollmops (Tamo)** · Source `f007846` · date 2024-03-25 · locator § "Sharing an Iterator Over the Available IDs" → § "The Final Solution" — Rejected a Mutex-guarded shared iterator for concurrent tree-node ID generation because it forces threads to wait on the lock; replaced it with a lock-free design (RoaringBitmap::select plus AtomicU32/AtomicU64/AtomicBool) that lets threads generate IDs without synchronization. Quote: "That is safe and will yield the right results, but won't scale well as all the threads have to wait for each other on the lock." [`a-sa17-f007846-c1`, team a]
    - **bsder** · Source `f005600` · date 2025-11-01 · locator lobste.rs/s/fzro7f, comment 2025-11-01T01:54:49-05:00 — argues atomics and compare-and-swap are fine — worst case you get livelock, which is rare and usually recovers — while locks are "always a disaster waiting to happen" because something will die holding one and the whole system grinds to a halt; goes as far as saying a lock's mere existence, even inside a library, is always a programming bug Quote: "In fact, I would argue that the existence of a \"lock\" is *always* a programming bug even inside a library." [`b-sb18-f005600-c1`, team b]
  - `mutex-vs-atomics--atomics-carry-own-bugs` — Atomics carry their own bug class
    - **inactive-user** · Source `f005600` · date 2025-11-01 · locator lobste.rs/s/fzro7f, comment 2025-11-01T02:14:18-05:00 (context: also 2025-10-31T23:05:36-05:00, arguing neither locks nor hand-rolled atomics belong in ordinary application code — stick to a well-tested concurrency library) — pushes back that framing atomics/CAS as the safe alternative glosses over the fact that races (stale/inconsistent reads) are themselves a real bug class, not a lesser evil Quote: "You say that like race conditions (with atomics) are not a bad thing" [`b-sb18-f005600-c2`, team b]
  - `mutex-vs-atomics--mutex-unless-contended` — Plain mutexes unless contention is high (orphan Claim)
    - **Evgenii Seliverstov** · Source `f011233` · date 2025-02-26 · locator ~29:29-30:32 — explicit decision rule offered to the audience: if there are many threads and heavy lock contention, move to lock-free data structures (crossbeam, parking_lot); if a lock is rarely contended, a normal mutex-based structure is simpler and just as good, because lock-free implementations bring their own hazards (e.g. the ABA problem) Quote: "if you have a lot of chats and you have a lot of locks you should probably go with lock free data structures[;] if the lock is rarely acquired ... you better use the normal mutex" [`b-sb23-f011233-c2`, team b]
- Positions seen by the extractor (`a-sa17-f007846-q1`): lock-free-atomics-preferred-for-hot-path (Mutex tried first and rejected)
- Positions seen by the extractor (`b-sb18-f005600-q1`): avoid-locks-prefer-atomics-cas, race-conditions-are-also-a-real-problem

### `named-default-args-overloading`

**Question.** Should Rust add named arguments, default arguments or overloading (including for interop)?

- Grouping: Same language-feature proposals; overloading for C++ interop is a context.
- Absorbs merge-final ids: `overloading-for-interop`
- Teams: a, b · members (context): `a-sa18-f009104-q1` (f009104, core); `b-sb24-f011312-q6` (f011312, core)
- Domains: core
- Concepts: named-parameters; default-arguments; function-overloading; function-dispatch; api-ergonomics; language-simplicity; function overloading; trait-based dispatch (`From`/`Into`); type inference cost
- Positions:
  - `named-default-args-overloading--reject-all-for-simplicity` — Reject all
    - **Steve Klabnik** · Source `f009104` · date long-standing prior view, "over a decade" per this 2026-09-21 post's own framing (no earlier dated source read; retrospective self-report only) · locator "These features make me uneasy" section — has for years opposed Rust adding named parameters, optional/default arguments and function overloading (all requested since at least a 12-year-old GitHub issue), arguing the features are numerous, mutually entangled, and that Rust's current rule — one function, one signature, write a differently-named function or a builder if you need variants — keeps the language simple at an acceptable cost Quote: "I've grown to enjoy Rust's simplicity in this area... that's why I've pushed back against the various proposals to extend Rust in this way all of these years." [`a-sa18-f009104-c1`, team a]
  - `named-default-args-overloading--named-parameters-only` — Named parameters only
    - **Steve Klabnik** · Source `f009104` · date 2026-09-21 · locator "I'm okay with named parameters now" section — still opposes optional/default arguments and overloading, but has become open specifically to named parameters (not the other bundled features), while flagging unresolved language-design problems the proposal would need to solve: parameters are patterns not names, function-values erase parameter names, left-to-right evaluation order conflicts with letting call sites reorder named arguments (worked example: `consume(data, data.len())` vs. a hypothetical `consume(length: data.len(), data: data)`), and renaming a parameter becomes a breaking change Quote: "I think Rust could be okay with named parameters, but not optional or default ones." [`a-sa18-f009104-c2`, team a]
  - `named-default-args-overloading--overloading-for-interop` — Overloading, at least for interop
    - **Taylor and Tyler** · Source `f011312` · date 2025-10-03 · locator [28:38]-[30:39] — Rust has avoided overloading to keep call resolution clear and preserve type inference, but C++ API maintainers rely on being able to add overloads without breaking existing callers; Rust already effectively fakes overloading via trait dispatch (e.g. multiple `From` impls, `Into`'s return-type-directed dispatch) inconsistently, and built-in overloading would also resolve the earlier aliasing problem by letting the compiler pick a safe (exclusive) vs. unsafe (possibly-aliased) overload based on the caller's reference Quote: "Today, Rust should just support built-in overloading, especially for interop with existing languages." [`b-sb24-f011312-c6`, team b]
- Positions seen by the extractor (`a-sa18-f009104-q1`): reject-all-for-simplicity, open-to-named-parameters-only
- Positions seen by the extractor (`b-sb24-f011312-q6`): yes-add-overloading-for-interop (Taylor/Tyler)

### `nightly-in-production`

**Question.** Should production code depend on nightly-only features (e.g. portable SIMD) or stay on stable?

- Grouping: Same choice; numeric kernels are a context.
- Absorbs merge-final ids: `portable-simd-nightly-vs-stable-intrinsics`
- Teams: a, b · members (context): `a-saL2-f011092-q5` (f011092, core); `b-sb23-f011233-q2` (f011233, core)
- Domains: core
- Concepts: stable vs nightly Rust; unstable features; portable_simd; target_feature; SIMD; stable vs nightly
- Positions:
  - `nightly-in-production--stable-only` — Stable only
    - **Luca Casonato** · Source `f011092` · date 2024-02-13 · locator ~00:46:45-00:47:45 (Q&A) — states plainly that the team does not, has not, and does not plan to rely on unstable Rust features (with a possible narrow exception for an unstable JSON test-message-format flag he wasn't sure was still unstable), and that all their foundational crates are published to crates.io with no unpublished dependencies Quote: "we do not rely on unstable features and we have not relied on unstable features and we are not planning to rely on unstable features" [`a-saL2-f011092-c5`, team a]
  - `nightly-in-production--nightly-when-it-pays` — Nightly when its safety and ergonomics pay (portable SIMD)
    - **Evgenii Seliverstov** · Source `f011233` · date 2025-02-26 · locator ~36:39-39:43 — contrasts writing raw target-feature-gated intrinsics (unsafe, verbose, must be manually wrapped and feature-detected at runtime) with std::simd's portable_simd, which lets you write safe, ordinary-looking iterator code that the compiler lowers to the right instructions per architecture; recommends it as "the choice" even though it currently requires nightly Quote: "you don't need to write all the ins[truction]s ... you write the safe code not unsafe ... portable Sy[md] is the choice" [`b-sb23-f011233-c3`, team b]
- Positions seen by the extractor (`a-saL2-f011092-q5`): stable-only (Luca Casonato / Deno)
- Positions seen by the extractor (`b-sb23-f011233-q2`): use portable_simd as the default choice for its safety and ergonomics despite it being nightly-only, versus staying on stable with manually gated intrinsics and runtime feature detection

### `opt-level-z-vs-s`

**Question.** For size-optimized builds, can opt-level="z" be assumed smaller than "s", or must both be measured?

- Grouping: Both teams logged the same Rust+Wasm book chapter.
- Teams: a, b · members (context): `a-sB02-f000256-q7` (f000256, wasm); `b-bk02-f000256-q9` (f000256, wasm)
- Domains: wasm
- Concepts: build config; LTO; codegen; compiler optimization flags; code size
- Positions:
  - `opt-level-z-vs-s--p1` — measure-both(recommended)
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Shrinking .wasm Code Size" — "Tell LLVM to Optimize for Size Instead of Speed" — opt-level="s" can sometimes produce smaller binaries than the more aggressive opt-level="z", so the choice should be measured rather than assumed. Quote: "Note that, surprisingly enough, opt-level = \"s\" can sometimes result in smaller binaries than opt-level = \"z\". Always measure!" [`a-sB02-f000256-c7`, team a]
  - `opt-level-z-vs-s--p2` — never assume opt-level="z" beats opt-level="s" for binary size — measure both
    - **rustwasm working group (Rust and WebAssembly book) [voice-unverified]** · Source `f000256` · date unknown (living doc) · locator § "Shrinking .wasm Code Size" → Tell LLVM to Optimize for Size Instead of Speed — after presenting "z" as the more aggressive size flag, flags the counterintuitive case where "s" wins, as a reason no flag choice should be trusted unmeasured. Quote: "Note that, surprisingly enough, opt-level = \"s\" can sometimes result in smaller binaries than opt-level = \"z\". Always measure!" [`b-bk02-f000256-c10`, team b]
- Positions seen by the extractor (`a-sB02-f000256-q7`): measure-both(recommended), assume-z-smaller(rejected)
- Positions seen by the extractor (`b-bk02-f000256-q9`): never assume, measure both (chosen); assume the more aggressive size flag always wins (rejected as unsafe assumption)

### `oss-framework-monetization`

**Question.** Release Rust work fully open (with a paid layer alongside), or keep features or toolchains proprietary?

- Grouping: Same open-vs-proprietary choice.
- Teams: a, b · members (context): `a-sa09-f004016-q1` (f004016, core, ml); `b-sT05-f002775-q1` (f002775, embedded)
- Domains: core, embedded, ml
- Concepts: open-source-governance; monetization; licensing; Ferrocene; qualification (ISO 26262, IEC 61508, IEC 62304); cortex-r-rt; Embedded Devices WG
- Positions:
  - `oss-framework-monetization--fully-open` — Fully open, paid layer alongside or donate permissively
    - **nathanielsimard** · Source `f004016` · date 2025-12-19 · locator § "Announcing Burn Central" — frames Burn Central's business model as adding a paid cloud layer alongside a fully-capable free/local plan, explicitly contrasted with paywalling core features Quote: "I've always envisioned a business model based on adding value through complementarity, rather than restricting features behind a paywall." [`a-sa09-f004016-c1`, team a]
    - **Jonathan Pallant (Ferrous Systems)** · Source `f002775` · date 2025-03-11 · locator press-release body, Pallant quote paragraph — libraries and examples (incl. cortex-r-rt, mirroring the Cortex-M set) donated to the Rust Project's Embedded Devices WG; headline frames "Under Open Source License" as the first Quote: "As long-time advocates of open-source development, we are proud to be able to donate this project to the community" (flag: voice-unverified) [`b-sT05-f002775-c1`, team b]
- Positions seen by the extractor (`a-sa09-f004016-q1`): complementary-paid-layer, feature-paywall
- Positions seen by the extractor (`b-sT05-f002775-q1`): open source under permissive licence, donated to the Rust Project's WG

### `pac-crate-per-chip-vs-shared`

**Question.** One shared PAC crate with features, or one per chip?

- Grouping: Both teams logged the same PR.
- Teams: a, b · members (context): `a-sa01-f001838-q1` (f001838, embedded); `b-sb06-f001838-q1` (f001838, embedded)
- Domains: embedded
- Concepts: peripheral-access crates (PAC); Cargo features; code generation (chiptool); embedded HAL crate organization; crate organization; PAC (peripheral access crate) generation
- Positions:
  - `pac-crate-per-chip-vs-shared--single-crate-with-features` — One shared crate
    - **CBJamo** · Source `f001838` · date 2024-08-09 · locator PR comment, mid-thread (rp-pac#5 follow-up) — After a reviewer argued for the `stm32-metapac` pattern (one PAC crate covering related chips, feature-gated) over separate per-chip crates, the PR author reports it was easier than expected and that Cargo features "cleaned up" once unified into a single `rp-pac`. Quote: "I had assumed it'd be hard to do, but it wasn't too bad. I just updated the update.sh to make both and hand wrote a tiny lib.rs. Features did indeed clean up with the single pac." [`a-sa01-f001838-c1`, team a]
    - **Dirbaio** · Source `f001838` · date 2024-08-09 · locator PR #3243, comment 2024-08-09T07:14:06Z — prefers adding rp235x support to the existing `rp-pac` crate (the `stm32-metapac` pattern) rather than a new per-chip crate (the `nrfxxx-pac` pattern already used elsewhere in the embassy org), since it's much less annoying to release and manage Cargo features Quote: "I think we should add rp235x to `rp-pac` (`stm32-metapac` style) instead of making separate crates per chip (`nrfxxx-pac` style). It's much less annoying to release and manage Cargo features." [`b-sb06-f001838-c1`, team b]
- Positions seen by the extractor (`a-sa01-f001838-q1`): reviewer (unattributed) — one shared PAC crate per chip family, gated by features, is easier to release and maintain; CBJamo (PR author) — initially organizing per chip, then adopting the shared-crate approach once shown it was feasible
- Positions seen by the extractor (`b-sb06-f001838-q1`): single-crate-with-features, separate-crate-per-chip

### `paid-maintainers-for-infrastructure`

**Question.** Volunteers or funded maintainers for critical Rust infrastructure?

- Grouping: Same choice in two Rust-project posts.
- Teams: a, b · members (context): `a-sR15-f009751-q1` (f009751, core); `b-sR13-f009755-q1` (f009755, core)
- Domains: core
- Concepts: open-source funding models; maintainer burnout; project governance; OSS sustainability; maintainer funding; governance
- Positions:
  - `paid-maintainers-for-infrastructure--fund-maintainers` — Fund dedicated maintainers
    - **Alejandra González (@blyxyas)** · Source `f009751` · date 2026-08-26 · locator bio section "Alejandra González (@blyxyas)" — being funded lets her put her full effort into the project without financial anxiety, directly boosting her productivity Quote: "Funding is the system that helps me pour my heart into a project without worrying about making ends meet. Having those needs met is a game-changer and boosts my productivity." [`a-sR15-f009751-c1`, team a]
    - **Jonas Böttiger (@joboet)** · Source `f009751` · date 2026-08-26 · locator bio section "Jonas Böttiger (@joboet)" — funding removes the tradeoff between doing the maintenance work he loves and taking a better-paid job elsewhere Quote: "Getting funding for my work is a dream come true. It will allow me to continue doing the thing I love instead of worrying about whether I should rather invest all that time in a money-earning job with much less positive impact on the world around me." [`a-sR15-f009751-c2`, team a]
    - **Jakub Beránek, on behalf of the Rust Funding team** · Source `f009755` · date 2026-09-22 · locator "Why Cargo?" section — the Cargo team "struggled with meeting its maintenance demands" after members left or lost funding, so the Funding team used Leadership Council and AWS money to open a new full-time Maintainer in Residence position; explicitly framed as partial relief, not a full fix Quote: "Even though we know that a single full-time maintainer will not completely solve the maintenance struggles of the Cargo team, we hope that it will improve the situation" [`b-sR13-f009755-c1`, team b]
- Positions seen by the extractor (`a-sR15-f009751-q1`): paid-maintenance-improves-focus-and-sustainability (Alejandra González, Jonas Böttiger, Gen Li)
- Positions seen by the extractor (`b-sR13-f009755-q1`): fund a full-time paid Maintainer in Residence via the Rust Foundation Maintainers Fund plus corporate donations (AWS)

### `porting-to-rust-safety`

**Question.** Does a straight port of C or C++ to Rust give memory safety?

- Grouping: Same question in two talks.
- Teams: a, b · members (context): `a-sa21-f011069-q2` (f011069, core); `b-sb24-f011312-q4` (f011312, core)
- Domains: core
- Concepts: unsafe; memory safety; undefined behavior; refactoring; gradual C++-to-Rust migration; aliasing-based optimization; undefined behavior introduced by translation
- Positions:
  - `porting-to-rust-safety--naive-port-not-safe` — No; restructure or risk new UB
    - **Aleksandr Petrosyan** · Source `f011069` · date 2023-11-15 · locator ~00:10:50-00:11:10 — Chose Rust partly to eliminate memory leaks and undefined behavior, but found this harder than expected because the existing C-style code's organization didn't allow refactoring into a safe version — implying a straight port that preserves the original architecture does not by itself deliver Rust's safety benefits. Quote: "Getting rid of memory leaks turned out to be a lot harder... because of the... way in which the code was organized didn't really allow me to refactor it into a safe version." [`a-sa21-f011069-c4`, team a]
    - **Taylor** · Source `f011312` · date 2025-10-03 · locator [17:27]-[18:27] — pure Rust can't create mutably-aliasing references, so if a ported function relies on C++'s permissive aliasing (e.g. a mutable reference/field that in fact aliases other pointers), naively translating it into Rust and letting the optimizer assume exclusivity can silently change program behavior and introduce new undefined behavior that wasn't present in the original C++ Quote: "This is a huge issue for gradual C++ to Rust migration... This is terrible. Rust, you were supposed to destroy the undefined behavior, not join it." [`b-sb24-f011312-c4`, team b]
- Positions seen by the extractor (`a-sa21-f011069-q2`): rewrite-alone-insufficient-requires-architectural-refactor
- Positions seen by the extractor (`b-sb24-f011312-q4`): no-naive-porting-can-introduce-new-UB (Taylor)

### `profile-before-optimizing`

**Question.** Guide optimization by profiling data or by hypothesis?

- Grouping: Both teams logged the same Rust+Wasm book chapter.
- Teams: a, b · members (context): `a-sB02-f000256-q6` (f000256, core); `b-bk02-f000256-q6` (f000256, wasm, core)
- Domains: core, wasm
- Concepts: profiling discipline; performance methodology
- Positions:
  - `profile-before-optimizing--p1` — profile-first(recommended)
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Time Profiling" — "Making Time Run Faster" — a stated hypothesis (allocating/freeing a cells vector each tick is the bottleneck) was measured and found false — the cost was actually in computing the next generation — used as the reason to always let profiling guide optimization effort rather than intuition. Quote: "Looking at the timings, it is clear that my hypothesis is incorrect... Another reminder to always guide our efforts with profiling!" [`a-sB02-f000256-c6`, team a]
  - `profile-before-optimizing--p2` — let profiling data override the developer's hypothesis about where time is spent, every time
    - **rustwasm working group (Rust and WebAssembly book) [voice-unverified]** · Source `f000256` · date unknown (living doc) · locator § "Time Profiling" → Growing our Game of Life Universe; and → Making Time Run Faster — narrates two cases inside its own tutorial where the expected bottleneck was wrong — the fillStyle canvas setter, not tick(), ate 40% of frame time; and vector allocation, the author's stated hypothesis, turned out to have "negligible cost" — using both to argue profiling must drive optimization, not intuition. Quote: "Always let profiling guide your focus, since time may be spent in places you don't expect it to be." [`b-bk02-f000256-c7`, team b]
- Positions seen by the extractor (`a-sB02-f000256-q6`): profile-first(recommended; a stated hypothesis about allocation cost was measured and found wrong)
- Positions seen by the extractor (`b-bk02-f000256-q6`): profile first, let data override intuition (chosen, argued from two in-source cases where the hypothesis was wrong); optimize from hypothesis alone (implicitly rejected)

### `reflection-type-model-and-mutation`

**Question.** Should compiler reflection follow the compiler's model or users' needs, and allow mutation?

- Grouping: Both teams logged the same talk.
- Teams: a, b · members (context): `a-sa25-f011413-q4` (f011413, core); `b-sb24-f011413-q4` (f011413, core)
- Domains: core
- Concepts: reflection; soundness; invariants; mutation; compiler internals; reflection MVP (nightly; in the compiler/std); soundness of reflected mutation; design scope of built-in reflection
- Positions:
  - `reflection-type-model-and-mutation--open-design-space` — Unresolved
    - **Amos (fasterthanlime)** · Source `f011413` · date 2026-06-11 · locator ~00:21:20–00:22:05 (Q&A) — reporting secondhand on the in-progress compiler/std reflection MVP (a collaborator's name is auto-captioned inconsistently as "Ollie" at ~00:16:20 and "Ali" at ~00:21:20 — same effort, name not verifiable from this source, logged as an ambiguity rather than resolved), Amos says the team went back and forth on whether to model types from the compiler's internal view or from user-facing (de)serialization needs, and surfaced unresolved soundness concerns: reflection that permits mutation could violate invariants expressed nowhere but the code Quote: "there was a lot of concerns about soundness. Like if if you are able to mutate things, you can violate invariants that are just not expressed anywhere except for the code... there are more open questions than there are answers right now" [`a-sa25-f011413-c7`, team a]
    - **Amos (fasterthanlime)** · Source `f011413` · date 2026-06-11 · locator [20:21]-[21:21] (Q&A) — asked how the Rust project could make all this reflection complexity unnecessary, he says the in-progress compiler/std reflection MVP is still an open, contested design space — whether to describe types from the compiler's internal model or from what's useful to a user, whether to let it be driven by serialization needs, and whether mutation through reflection is sound at all given it can break invariants that exist only in code — and that the MVP is reportedly being rewritten from scratch Quote: "there are more open questions than there are answers right now." [`b-sb24-f011413-c4`, team b]
- Positions seen by the extractor (`a-sa25-f011413-q4`): reported secondhand by Amos as unresolved inside the Rust project's own reflection-MVP effort — "more open questions than there are answers right now"; no directly-quoted opposing voice in this source
- Positions seen by the extractor (`b-sb24-f011413-q4`): open-unresolved-design-space (Amos)

### `reproduce-wasm-bugs-natively`

**Question.** Reproduce wasm bugs and benchmarks as native tests first, or debug on the wasm target?

- Grouping: Both teams logged the same Rust+Wasm book chapter.
- Teams: a, b · members (context): `a-sB02-f000256-q12` (f000256, wasm, web); `b-bk02-f000256-q7` (f000256, wasm)
- Domains: wasm, web
- Concepts: debugging strategy; native vs wasm tooling maturity; debugging workflow; tooling maturity
- Positions:
  - `reproduce-wasm-bugs-natively--p1` — prefer-native-repro
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Debugging Rust-Generated WebAssembly" — "Avoid the Need to Debug WebAssembly in the First Place" — WebAssembly's debugging story is called immature (no DWARF-equivalent, stepping through raw wasm instructions); bugs not tied to JS/Web-API interaction should instead be reproduced as native #[test]s to use mature OS-native tooling. Quote: "the debugging story for WebAssembly is still immature... you will have an easier time finding and fixing bugs if you can isolate them in a smaller test cases that don't require interacting with JavaScript." [`a-sB02-f000256-c15`, team a]
  - `reproduce-wasm-bugs-natively--p2` — reproduce non-JS bugs as native #[test]/#[bench] under OS-native tools rather than debugging on the wasm/Web target directly
    - **rustwasm working group (Rust and WebAssembly book) [voice-unverified]** · Source `f000256` · date unknown (living doc) · locator § "Avoid the Need to Debug WebAssembly in the First Place"; § "Using #[bench] with Native Code" — recommends native reproduction because wasm's debugging story is immature (no DWARF-equivalent yet) and native profilers/`quickcheck` shrinkers are more mature, but warns not to over-apply this: confirm first via a browser profiler that the bottleneck is actually in the wasm before investing in native profiling. Quote: "you will have an easier time finding and fixing bugs if you can isolate them in a smaller test cases that don't require interacting with JavaScript." [`b-bk02-f000256-c8`, team b]
- Positions seen by the extractor (`a-sB02-f000256-q12`): prefer-native-repro(recommended; wasm debugger tooling called "immature"), debug-in-browser(fallback)
- Positions seen by the extractor (`b-bk02-f000256-q7`): reproduce natively when the bug doesn't involve JS/Web APIs (chosen, with the caveat of first confirming the bottleneck is actually in wasm); debug directly on the wasm/Web target (kept only for JS-interaction-specific issues)

### `rust-worth-it-for-failure-heavy-infra`

**Question.** Rust for failure-heavy network infrastructure?

- Grouping: Both teams logged the same post.
- Teams: a, b · members (context): `a-sa15-f005948-q1` (f005948, cloud-workers, distributed); `b-sb19-f005948-q1` (f005948, cloud-workers, distributed)
- Domains: cloud-workers, distributed
- Concepts: pattern-matching; ownership; error-handling; distributed-systems; hyper; tokio; pattern matching; ASGI-over-protobuf
- Positions:
  - `rust-worth-it-for-failure-heavy-infra--rust-for-failure-heavy-infra` — Yes for failure-heavy, high-throughput infrastructure: ownership and pattern matching tame edge cases
    - **Eric Zhang** · Source `f005948` · date 2024-03-14 · locator "Edge cases and errors" section — reports building `modal-http` (HTTP/WebSocket-to-function-call translation service) in Rust on hyper/tokio specifically for speed and to help manage the many concurrent failure cases (client disconnects, malformed/out-of-order events, spot preemption); credits the language's pattern matching and ownership for handling that casework, and separately reports that replacing an earlier Python-based ingress with this Rust service cut 502 errors by 99.7% Quote: "This was tricky! HTTP has quite a few edge cases, so we used Rust for its speed and to help manage the complexity." / "Rust's pattern matching and ownership help with managing the casework." [`a-sa15-f005948-c1`, team a]
    - **Eric Zhang** · Source `f005948` · date 2024-03-20 · locator § "Edge cases and errors" / opening — HTTP has many edge cases and Modal's ingress needs to handle malformed/out-of-order events from possibly-malicious clients; Rust's ownership and pattern matching were chosen specifically to manage that casework, and switching from a prior Python-based ingress to this Rust one cut 502 errors by 99.7% Quote: "Rust's pattern matching and ownership help with managing the casework." [`b-sb19-f005948-c1`, team b]
- Positions seen by the extractor (`a-sa15-f005948-q1`): ownership-and-pattern-matching-aid-correctness-at-scale
- Positions seen by the extractor (`b-sb19-f005948-q1`): worth-it-for-edge-case-heavy-infra (Eric Zhang / Modal)

### `scratch-register-type-enforced`

**Question.** For a scratch register crossing a function boundary, enforce safe use by types and explicit parameters, or encapsulate it by convention?

- Grouping: Both teams logged the same wasmtime review comment (the merge check's flag); the two framings name one concrete choice.
- Absorbs merge-final ids: `scratch-register-param-vs-encapsulated`
- Teams: a, b · members (context): `a-sa05-f002466-q1` (f002466, wasm); `b-sR05-f002466-q1` (f002466, wasm)
- Domains: wasm
- Concepts: unsafe; register-allocation; API-design
- Positions:
  - `scratch-register-type-enforced--encode-in-types` — Encode it in types
    - **saulecabrera** · Source `f002466` · date 2025-01-04 · locator comment @saulecabrera 2025-01-04T16:38:14Z — proposes relying on the type system to identify/audit scratch-register usage, or exclusive access analogous to allocatable registers, because passing a scratch register as a parameter extends its live range and raises unintentional-clobbering risk Quote: "relying on the type system to identify/audit scratch register usage and/or providing exclusive access to the scratch registers" [`a-sa05-f002466-c1`, team a]
  - `scratch-register-type-enforced--p1` — minimize the live range and avoid passing scratch registers around as parameters, even if it means redefining signatures and accepting some duplication across ISA-specific paths.
    - **saulecabrera (Bytecode Alliance, Wasmtime Winch baseline-compiler maintainer)** · Source `f002466` · date 2025-01-04 · locator bytecodealliance/wasmtime#9889, comment 2025-01-04T16:38:14Z. · L2288-L2319. — minimize the live range and avoid passing scratch registers around as parameters, even if it means redefining signatures and accepting some duplication across ISA-specific paths. Quote: "the unintentional clobbering risk is particularly important in the case of scratch registers in Winch: even though they can be used for any purpose, one important detail about them is that they are not tracked by Winch's regalloc therefore they must be used sparingly and with extreme caution... Ideally, the live range of the scratch registers should be as short as possible to avoid potential bugs." [`b-sR05-f002466-c1`, team b]
- Positions seen by the extractor (`a-sa05-f002466-q1`): type-enforced-safety, convention-and-review
- Positions seen by the extractor (`b-sR05-f002466-q1`): minimize the live range and avoid passing scratch registers around as parameters (saulecabrera (Bytecode Alliance, Wasmtime Winch baseline-compiler maintainer))

### `test-via-real-entry-point`

**Question.** Should tests go through the production entry point, or through internal methods?

- Grouping: Same testing choice in Zed and Zebra.
- Teams: a, b · members (context): `a-sa13-f004772-q2` (f004772, desktop-cli-ui, core); `b-bk03-f000267-q13` (f000267, core, distributed)
- Domains: core, desktop-cli-ui, distributed
- Concepts: testing-philosophy; integration-vs-unit-testing; refactoring safety; fallible conversions; ok()/unwrap_or; testing entry points vs helpers; silent regression
- Positions:
  - `test-via-real-entry-point--p1` — test-via-real-entry-point
    - **SomeoneToIgnore** · Source `f004772` · date 2026-08-06 · locator comment @SomeoneToIgnore 2026-08-06T16:39:43Z — objects that tests drive the navigation/re-anchoring functions as plain method calls against a bespoke harness, so they would keep passing even if the real keybinding wiring broke; wants at least one test to dispatch the actual action via a keystroke against the real strip Quote: "At least one test should dispatch editor::OpenBreadcrumbs via a keystroke against the real strip." [`a-sa13-f004772-c3`, team a]
    - **SomeoneToIgnore** · Source `f004772` · date 2026-08-07 · locator comment @SomeoneToIgnore 2026-08-07T22:48:19Z — notes that even after a gesture-handling fix, "nothing tests the actual gesture" — the toggle/switch tests still drive the methods directly rather than the deferred mouse-event path itself Quote: "nothing tests the actual gesture: the toggle/switch tests drive the methods directly, the deferred up-out path itself has zero coverage." [`a-sa13-f004772-c4`, team a]
  - `test-via-real-entry-point--p2` — entry-point-testing-plus-fallible-conversion-audit
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Refactoring Consensus-Critical Code (full page) — when a refactor moves or replaces code that enforces consensus rules, a check can silently stop being enforced without any test failing and without a diff showing a deleted check, because the danger is in what the old code used to do that nothing does anymore; the guide requires inventorying every rejection the old code could produce and naming its new home, testing every parse-time rejection through the actual production entry point rather than only through the check's own unit tests, and individually auditing fallible conversions (.ok(), unwrap_or, defaulted try_from) that could silently turn an invalid wire value into one a check treats as benign — citing two real incidents (#10461, #11386) where this exact failure mode slipped through with green CI Quote: "The dangerous bugs are not in the new code: they are in what the old code used to do that nothing does anymore." (flag: voice-unverified) [`b-bk03-f000267-c15`, team b]
- Positions seen by the extractor (`a-sa13-f004772-q2`): test-via-real-entry-point, test-via-internal-methods
- Positions seen by the extractor (`b-bk03-f000267-q13`): entry-point-testing-plus-fallible-conversion-audit

### `tower-middleware-vs-handler-helpers`

**Question.** Cross-cutting concerns in a middleware or connection-hook layer, or per handler or protocol?

- Grouping: Same choice; global middleware vs typestate stays apart.
- Teams: a, b · members (context): `a-sT08-f004169-q3` (f004169, decentralized-iroh); `b-sb22-f008906-q1` (f008906, cloud-workers, web)
- Domains: cloud-workers, decentralized-iroh, web
- Concepts: middleware; connection interception; authentication; separation of concerns; tower; Service/Layer traits; middleware composition; aws-lambda-rust-runtime
- Positions:
  - `tower-middleware-vs-handler-helpers--middleware-layer` — A middleware or connection-hook layer
    - **ramfox** · Source `f004169` · date 2026-01-27 · locator § "Endpoint Hooks", `auth-hook` example paragraph and the paragraph after it — an `EndpointHooks` trait intercepts connections before connect and after handshake, so authentication, authorization, rate limiting and observability sit at the connection layer and individual protocols stay on their core logic instead of each handling auth Quote: "individual protocols don't need to handle authentication themselves" (flag: voice-unverified — as above. Left out: switching from custom holepunching to the IETF QUIC-NAT-Traversal draft, and multipath, are networking-protocol decisions internal to iroh that its users do not make and that are not argued as Rust choices; the `Discovery` → `AddressLookup` rename is a naming clarification without a contested alternative.) [`a-sT08-f004169-c3`, team a]
    - **Luciano Mammino** · Source `f008906` · date 2026-05-03 · locator section "Does this pattern make sense in Rust?" — almost every Rust Lambda codebase reviewed in the last year bolts logging/auth/validation directly into the handler, sometimes via clever helpers, macros or trait extensions, none of which quite match the convenience and composability of the middleware engine already built into `aws-lambda-rust-runtime` via tower Quote: "None of them quite match the convenience and composability of a real middleware stack, though." [`b-sb22-f008906-c1`, team b]
- Positions seen by the extractor (`a-sT08-f004169-q3`): connection-layer-hooks (against per-protocol auth)
- Positions seen by the extractor (`b-sb22-f008906-q1`): adopt tower's built-in middleware engine over handler-embedded helpers/macros/trait extensions, which the author judges never quite as convenient or composable (Luciano Mammino)

### `unchecked-unwrap-vs-safe-abort`

**Question.** For values statically safe to unwrap, a safe abort wrapper or unsafe unchecked unwrap?

- Grouping: Both teams logged the same Rust+Wasm book chapter.
- Teams: a, b · members (context): `a-sB02-f000256-q8` (f000256, wasm, embedded); `b-bk02-f000256-q11` (f000256, wasm, core)
- Domains: core, embedded, wasm
- Concepts: panic avoidance; unwrap; code size; panic elimination; undefined behavior
- Positions:
  - `unchecked-unwrap-vs-safe-abort--p1` — safe-abort(default recommendation)
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Shrinking .wasm Code Size" — "Avoid Panicking" — to cut panic-related code bloat from unwrap, prefer a safe helper that calls process::abort() on None/Err over letting the formatted panic machinery run, since panics compile down to aborts on wasm32-unknown-unknown anyway. Quote: "panics translate into aborts in wasm32-unknown-unknown anyways, so this gives you the same behavior but without the code bloat." [`a-sB02-f000256-c8`, team a]
  - `unchecked-unwrap-vs-safe-abort--p2` — unsafe-unchecked(conditional)
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Shrinking .wasm Code Size" — "Avoid Panicking" — the unreachable crate's unsafe unchecked_unwrap is offered as a further alternative, but restricted to cases where the programmer is "110% sure" the assumption holds, and only in release builds, keeping checked behavior in debug. Quote: "You really only want to use this unsafe approach when you 110% know that the assumption holds." [`a-sB02-f000256-c9`, team a]
  - `unchecked-unwrap-vs-safe-abort--p3` — prefer a safe abort-on-None/Err wrapper over unsafe unchecked unwrapping; reserve the unsafe route for near-certainty, kept checked in debug builds
    - **rustwasm working group (Rust and WebAssembly book) [voice-unverified]** · Source `f000256` · date unknown (living doc) · locator § "Shrinking .wasm Code Size" → Avoid Panicking — presents the safe `process::abort`-based `unwrap_abort` as the default way to drop panic-infrastructure bloat, and names the `unreachable` crate's unsafe `unchecked_unwrap` as a further, riskier step, explicitly conditioning its use on near-total certainty plus a debug build that still checks. Quote: "You really only want to use this unsafe approach when you 110% know that the assumption holds, and the compiler just isn't smart enough to see it." [`b-bk02-f000256-c12`, team b]
- Positions seen by the extractor (`a-sB02-f000256-q8`): safe-abort(default recommendation), unsafe-unchecked(only when "110% sure", gated to release)
- Positions seen by the extractor (`b-bk02-f000256-q11`): safe process::abort-based wrapper (default-recommended); unsafe unchecked_unwrap, only when "110%" certain and kept checked in debug builds (conditionally endorsed, named as the riskier alternative)

### `wasm-allocator-choice`

**Question.** Keep the default wasm allocator, switch to a small one (wee_alloc), or drop allocation?

- Grouping: Both teams logged the same Rust+Wasm book chapter.
- Teams: a, b · members (context): `a-sB02-f000256-q10` (f000256, wasm, embedded); `b-bk02-f000256-q10` (f000256, wasm)
- Domains: embedded, wasm
- Concepts: allocator choice; code size vs speed
- Positions:
  - `wasm-allocator-choice--p1` — switch-to-wee_alloc
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Shrinking .wasm Code Size" — "Avoid Allocation or Switch to wee_alloc" — the default dlmalloc-based allocator costs ~10KB; replacing it with wee_alloc trades allocation speed for saving most of that size, recommended when allocation can't be avoided entirely. Quote: "wee_alloc is an allocator designed for situations where you need some kind of allocator, but do not need a particularly fast allocator, and will happily trade allocation speed for smaller code size." [`a-sB02-f000256-c11`, team a]
  - `wasm-allocator-choice--p2` — eliminate-allocation/no_std
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Shrinking .wasm Size" — exercise on static mut globals — for a single-instance program, exporting operations on a static mut global (with double-buffering) removes all dynamic allocation, allowing a #![no_std] crate with no allocator dependency at all, for maximum size reduction. Quote: "This removes all dynamic allocation from our Game of Life implementation, and we can make it a #![no_std] crate that doesn't include an allocator." [`a-sB02-f000256-c12`, team a]
  - `wasm-allocator-choice--p3` — swap the default dlmalloc-derived allocator for wee_alloc (or drop dynamic allocation) when code size outweighs allocation speed
    - **rustwasm working group (Rust and WebAssembly book) [voice-unverified]** · Source `f000256` · date unknown (living doc) · locator § "Shrinking .wasm Code Size" → Avoid Allocation or Switch to wee_alloc — names the default allocator's ~10KB footprint as the cost of keeping it, and wee_alloc's slower allocation as the cost of switching, framing the choice explicitly as a speed-for-size trade. Quote: "wee_alloc is an allocator designed for situations where you need some kind of allocator, but do not need a particularly fast allocator, and will happily trade allocation speed for smaller code size." [`b-bk02-f000256-c11`, team b]
- Positions seen by the extractor (`a-sB02-f000256-q10`): switch-to-wee_alloc(trades allocation speed for ~10KB size), eliminate-allocation/no_std(most size saved)
- Positions seen by the extractor (`b-bk02-f000256-q10`): switch to wee_alloc or avoid dynamic allocation entirely when size matters more than allocation speed (chosen); keep the default allocator (implicit status quo, faster but ~10KB heavier)

### `async-drop-raii-vs-close`

**Question.** Without async `Drop`, should async resources keep RAII cleanup, or require an explicit async `close`?

- Grouping: Same choice in three iroh sources.
- Teams: b · members (context): `b-sR10-f004423-q1` (f004423, decentralized-iroh, distributed, core); `b-sR10-f004741-q1` (f004741, decentralized-iroh, distributed, core); `b-sb17-f005159-q2` (f005159, decentralized-iroh)
- Domains: core, decentralized-iroh, distributed
- Concepts: async runtimes; Drop; resource lifecycle; RAII; `Drop`; async cleanup; cancel tokens; blocking-safe channels
- Positions:
  - `async-drop-raii-vs-close--preserve-raii-with-workarounds` — Keep RAII, working around the missing async Drop
    - **Rüdiger Klaehn** · Source `f005159` · date 2024-07-31 · locator article body, "Drop" section — refuses to abandon RAII for async resources; instead builds cleanup on cancel tokens or blocking-safe/force-send queues so `Drop` can still trigger a clean shutdown Quote: "I refuse to give up on RAII. I might provide an async shutdown function that tries to do a gentle shutdown. But every entity should also attempt to clean up on Drop." [`b-sb17-f005159-c2`, team b]
  - `async-drop-raii-vs-close--explicit-close-required` — Require an explicit async close; `Drop` is best effort only
    - **dignifiedquire (iroh/n0 computer)** · Source `f004423` · date 2026-03-16 · locator section "2. Changes to Endpoint closing" / "Endpoint Lifecycle Improvements" — Endpoint no longer attempts best-effort graceful close on drop; callers must await endpoint.close() explicitly, or resources close ungracefully and an error is logged Quote: "Starting with this release, the Endpoint no longer attempts to close connections gracefully when dropped. To gracefully close the endpoint, always await endpoint.close() before dropping the last instance of an endpoint or terminating your application." [`b-sR10-f004423-c1`, team b]
    - **Friedel Ziegelmayer & Rüdiger Klaehn (iroh/n0 computer)** · Source `f004741` · date 2026-05-27 · locator section "⚡ Faster Endpoint::close" — explicit endpoint.close() is now cheaper too — shutdown skips the draining period when possible, reinforcing close as the primary, first-class shutdown path rather than relying on drop Quote: "Shutdown now skips the draining period when it can. Closing is near-instant when the peer already closed remotely, and roughly one RTT otherwise if there is no packet loss." [`b-sR10-f004741-c1`, team b]
- Positions seen by the extractor (`b-sR10-f004423-q1`): explicit-close-required
- Positions seen by the extractor (`b-sR10-f004741-q1`): explicit-close-required (continued practice)
- Positions seen by the extractor (`b-sb17-f005159-q2`): preserve-raii-with-workarounds (Rüdiger Klaehn); give-up-raii-manual-close is named as an available alternative but not attributed to anyone advocating it

### `api-schema-spec-first-vs-code-first`

**Question.** Should an HTTP API's OpenAPI schema be generated from the Rust server code, or should code be generated from a hand-written spec?

- Grouping: Same concrete choice in two sources; sa14's f005454 entry is restored here (saL1 did not re-log it).
- Teams: a · members (context): `a-sa14-f005454-q1` (f005454, web); `a-sa23-f011186-q1` (f011186, web)
- Domains: web
- Concepts: OpenAPI generation; spec-first vs. code-first; schema drift; OpenAPI; schema generation; code generation
- Positions:
  - `api-schema-spec-first-vs-code-first--p1` — generate the OpenAPI spec from code, not code from the spec
    - **wofo (quoting the Dropshot project's own stated design goal)** · Source `f005454` · date 2025-02-24 · locator comment 2025-02-24T08:08:32 — highlights a quote from the Dropshot project explaining that an important goal was for code to be the source of truth with the spec generated from it, specifically so the spec couldn't diverge from the implementation, noting no existing crate did this Quote: "[An] important goal for us was to build something with strong OpenAPI support, and particularly where the code could be the source of truth and a spec could be generated from the code that thus could not diverge from the implementation." [`a-sa14-f005454-c1`, team a]
  - `api-schema-spec-first-vs-code-first--p2` — code-first schema generation
    - **Adam (surname unconfirmed; self-ID only)** · Source `f011186` · date 2024-11-20 · locator ~00:10:56 — don't hand-write the OpenAPI spec or rely on a programmer-maintained one; have the API server generate it, since a generated spec is provably in sync with the server that produced it Quote: "a better idea is don't hand write the spec don't rely on a programmer spec instead have your API server generate the spec" [`a-sa23-f011186-c1`, team a]
- Positions seen by the extractor (`a-sa14-f005454-q1`): code-first — generate the spec from code specifically so it can't diverge from the implementation, a goal the team didn't find already solved in any existing crate
- Positions seen by the extractor (`a-sa23-f011186-q1`): code-first/generate-from-server (Adam)

### `compile-time-vs-runtime-switches`

**Question.** Should test-only or staging behaviour be switched by Cargo features, `#[cfg]` or compile-time env vars, or by runtime options?

- Grouping: Same choice in two iroh releases.
- Teams: b · members (context): `b-sT04-f002233-q1` (f002233, core, decentralized-iroh); `b-sT05-f002550-q1` (f002550, decentralized-iroh, core)
- Domains: core, decentralized-iroh
- Concepts: Cargo features (`test-utils`); `#[cfg(test)]`; runtime configuration via environment variables; test vs production infrastructure; cargo features (test-utils); compile-time env vars; testability
- Positions:
  - `compile-time-vs-runtime-switches--runtime-switch` — Switch at runtime, dropping cfg or compile-time env vars
    - **n0, inc. / iroh team (post by ramfox)** · Source `f002233` · date 2024-10-24 · locator § "Sensible config options can go a looooong way" — A bug made builds pick the wrong relay servers (production vs staging), and the old config made it "too easy to point production code to our staging relays". So iroh-net no longer uses the `test-utils` feature or `#[cfg(test)]` to decide which infrastructure code runs against. It relies only on the `IROH_FORCE_STAGING_RELAYS` environment variable, behind a new `force_staging_infra` function. Quote: "We no longer rely on the test-utils feature or the #[cfg(test)] annotations for determining whether code runs against production or staging infrastructure" (flag: voice-unverified) [`b-sT04-f002233-c1`, team b]
    - **ramfox, matheus23 (iroh / n0 blog authors)** · Source `f002550` · date 2025-01-15 · locator § relay-only mode for testing — compile-time env var dropped; option threaded through the stack when test-utils is enabled; framed as "more programmatically sound" Quote: "The DEV_RELAY_ONLY compile time environment variable has been completely dropped" (flag: voice-unverified) [`b-sT05-f002550-c1`, team b]
- Positions seen by the extractor (`b-sT04-f002233-q1`): runtime env var only (n0/iroh), cfg/feature gating (the replaced approach, no Voice defends it here)
- Positions seen by the extractor (`b-sT05-f002550-q1`): runtime option behind test-utils feature (replaced compile-time env var)

### `crate-maintenance-signaling`

**Question.** How should crates.io signal that a crate or version should not be used: a per-version deprecation, decaying maintenance status, or the existing yank and badges?

- Grouping: Alternatives to one registry mechanism in one thread.
- Absorbs merge-final ids: `crate-deprecate-mechanism`, `maintenance-status-decay`
- Teams: b · members (context): `b-sb23-f009334-q1` (f009334, core); `b-sb23-f009334-q2` (f009334, core)
- Domains: core
- Concepts: crate deprecation; yank; semver; registry metadata; maintenance status; opt-in metadata; crate abandonment signaling
- Positions:
  - `crate-maintenance-signaling--new-deprecate-mechanism` — A dedicated per-version deprecation mechanism
    - **KSXGitHub** · Source `f009334` · date 2026-04-15 · locator OP — yank is too alarmist/breaking for this use; wants a `cargo deprecate <pkg>[@range] -m <reason>` that marks specific version ranges without forcing a break Quote: "Yank breaks things. It is also way too alarmist." [`b-sb23-f009334-c1`, team b]
    - **kornel** · Source `f009334` · date 2026-04-18 · locator comment ~14 — from analyzing crates.io data, genuinely "done" evergreen crates are rare (roughly 10-1000 out of 100,000+ old crates); giving authors a way to affirmatively mark a crate fine helps users filter the 99% that are abandonware Quote: "if they stumble upon an old crate, it's a 99% chance that it will be some outdated abandonware" [`b-sb23-f009334-c2`, team b]
    - **KSXGitHub** · Source `f009334` · date 2026-04-21 · locator comment ~20 — the maintenance badge only deprecates a whole crate, not individual problematic versions, so it doesn't solve the stated problem Quote: "this badge deprecate[s] the whole crate ... we only want to deprecate some versions of a crate" [`b-sb23-f009334-c4`, team b]
  - `crate-maintenance-signaling--existing-tools-suffice` — Existing tools suffice (maintenance badges, yank for serious cases)
    - **lewis** · Source `f009334` · date 2026-04-21 · locator comment ~19 — points to the existing `badges.maintenance.status` field, which lib.rs already renders, as already solving whole-crate deprecation Quote: "Isn't this what the badges.maintenance field in Cargo.toml is for?" [`b-sb23-f009334-c3`, team b]
    - **Ltrlg** · Source `f009334` · date 2026-04-22 · locator comment ~21 — a version with a serious security vulnerability should be yanked outright, not merely soft-deprecated, since yanking is proportionate to serious risk Quote: "In this case that version really should be yanked ... If the vulnerability can be qualified as 'serious' then yanking is not 'way too alarmist'" [`b-sb23-f009334-c5`, team b]
  - `crate-maintenance-signaling--status-auto-decays` — Maintenance status should decay automatically
    - **dlight** · Source `f009334` · date 2026-04-17 · locator comment ~6 — without decay, a crate could be marked maintained once and never revisited for years while still showing as maintained Quote: "The system does not work if the information isn't up to date." [`b-sb23-f009334-c6`, team b]
  - `crate-maintenance-signaling--status-opt-in-only` — Status opt-in only, no forced decay
    - **steffahn** · Source `f009334` · date 2026-04-17 · locator comment ~10 — modeled on "last seen online" indicators — sharing status should be opt-in per crate, changeable later, and any reminder emails must be a separate, one-time opt-in per person, not automatic Quote: "the crate author could opt in to setting such status information on their crates, but they shouldn't be forced" [`b-sb23-f009334-c7`, team b]
- Positions seen by the extractor (`b-sb23-f009334-q1`): new dedicated deprecate mechanism needed; existing tools (yank for serious cases, badges.maintenance for the rest) already suffice
- Positions seen by the extractor (`b-sb23-f009334-q2`): status should auto-decay so it can't go stale; status should be opt-in only, no forced decay, no unsolicited emails

### `encode-invariant-in-representation`

**Question.** Should a Rust data model encode its invariants in the representation (exhaustive enums, log2-stored sizes) so invalid states are unrepresentable, or validate at use?

- Grouping: Same modelling choice in wasmtime and Zebra.
- Teams: b · members (context): `b-bk03-f000267-q2` (f000267, core); `b-sb05-f001582-q1` (f001582, core, wasm)
- Domains: core, wasm
- Concepts: type system; enums; structural validity; parse-don't-validate; invalid-states-unrepresentable; type design; invariants
- Positions:
  - `encode-invariant-in-representation--encode-in-types` — Encode it in types
    - **fitzgen** · Source `f001582` · date 2024-06-10 · locator PR description, 2024-06-10T20:15:41Z — storing log2(page_size) instead of the raw page size cuts down on invalid states and the assertions needed elsewhere Quote: "In general, we store the log2(page_size) rather than the page size directly. This helps cut down on invalid states and properties we need to assert." [`b-sb05-f001582-c1`, team b]
  - `encode-invariant-in-representation--p1` — make-invalid-states-unrepresentable
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Design Overview § zebra-chain — zebra-chain's data structures are deliberately defined to enforce structural validity by making invalid states unrepresentable — e.g. the Transaction enum has one variant per transaction version, so it is impossible to construct a transaction with spend/output descriptions but no binding signature, or a version-2 (Sprout) transaction carrying Sapling proofs Quote: "making invalid states unrepresentable" (flag: voice-unverified) [`b-bk03-f000267-c2`, team b]
- Positions seen by the extractor (`b-bk03-f000267-q2`): make-invalid-states-unrepresentable
- Positions seen by the extractor (`b-sb05-f001582-q1`): encode-invariant-in-representation (fitzgen)

### `enum-vs-flags-and-optionals`

**Question.** Should multi-outcome or growing state be an enum, or a bool or a struct of optional fields?

- Grouping: Same modelling choice in two sources.
- Absorbs merge-final ids: `enum-vs-bool-for-state`, `enum-vs-struct-of-optionals-for-extension`
- Teams: b · members (context): `b-sR08-f003531-q1` (f003531, desktop-cli-ui); `b-sR08-f003731-q1` (f003731, decentralized-iroh)
- Domains: decentralized-iroh, desktop-cli-ui
- Concepts: enums; boolean blindness; state/API design; type-safety; `#[non_exhaustive]`; API extensibility; semver
- Positions:
  - `enum-vs-flags-and-optionals--enum` — Use a (non-exhaustive) enum
    - **MrSubidubi** · Source `f003531` · date 2025-10-10 · locator PR #38102, review comment 2025-10-10T21:34:30Z — instead of adding another special-cased check around the existing `serialize_dirty_buffers` boolean, suggests changing it to a named enum (`Always`/`Dirty`/`Never`) for readability. Quote: "Could we perhaps fix the logic above instead or change `self.serialize_dirty_buffers` to be an enum instead ... With that, this might be more readable and understandable, what do you think?" [`b-sR08-f003531-c1`, team b]
    - **im-lunex** · Source `f003531` · date 2025-10-16 · locator PR #38102, comment 2025-10-16T09:45:09Z — implemented the suggested `SerializationMode` enum in place of the boolean flag and judges it the safer, clearer choice. Quote: "The use of enum was the right decision - so neater and more secure." [`b-sR08-f003531-c2`, team b]
    - **ramfox** · Source `f003731` · date 2025-10-22 · locator § "Future proofing: Introducing TransportAddr" — replaced two independent fields (an optional relay URL and a set of socket addresses) with a single `#[non_exhaustive] enum TransportAddr { Relay(RelayUrl), Ip(SocketAddr) }`, so future transport kinds (e.g. WebRTC) can be added as new variants without another breaking change. Quote: "To combine them, and to allow for additions in the future, they are now represented as variants on a TransportAddr" [`b-sR08-f003731-c1`, team b]
- Positions seen by the extractor (`b-sR08-f003531-q1`): enum-over-bool-for-tri-state-clarity
- Positions seen by the extractor (`b-sR08-f003731-q1`): non-exhaustive-enum-over-struct-of-optionals

### `externref-in-rust`

**Question.** Should Rust add WebAssembly's `externref` as a new restricted language type, or keep it outside the core language?

- Grouping: q1 (represent externref) and q2 (extend the language for it) name one concrete choice in one RFC thread.
- Absorbs merge-final ids: `language-primitives-for-platform-interop`
- Teams: a · members (context): `a-sa29-f013113-q1` (f013113, wasm); `a-sa29-f013113-q2` (f013113, wasm)
- Domains: wasm
- Concepts: WASM externref; Abstract Machine; ABI; opaque host references; table-index representation; MIR; language extensibility; platform-specific target features; JS interop
- Positions:
  - `externref-in-rust--new-restricted-lang-type` — Add a restricted lang-item type; JS interop justifies a language change
    - **guybedford** · Source `f013113` · date 2026-07-29 · locator RFC #3987, opening post, 2026-07-29T00:09:07Z — proposes `core::arch::wasm32::externref`, legal only as a bare top-level type of function parameters/returns/locals, to let host references (e.g. JS values) marshal directly across foreign calls for interoperability and performance Quote: "an opaque, unforgeable reference to a WebAssembly host value, lowering to the Wasm externref reference type in function signatures" [`a-sa29-f013113-c1`, team a]
    - **guybedford** · Source `f013113` · date 2026-07-30T15:48:27Z · locator RFC #3987, comment 2026-07-30T15:48:27Z — responding directly to ds84182, argues JavaScript interop is a major quality-of-life story worth solving at the language level and that Rust has tackled harder, more niche problems before, while conceding the proposal must be justified for Rust on its own merits rather than by Clang precedent Quote: "JavaScript interop is not a complex or niche topic and this is a major quality of life improvement to that story" [`a-sa29-f013113-c5`, team a]
  - `externref-in-rust--must-fit-abstract-machine` — Reject types outside the Abstract Machine
    - **RalfJung** · Source `f013113` · date 2026-07-29T12:21:27Z and 2026-07-29T12:34:52Z · locator RFC #3987, comments 2026-07-29T12:21:27Z / 12:34:52Z — argues the RFC's semantics can't be expressed in the Abstract Machine used to justify MIR-transform and MIR-to-LLVM-IR correctness, calling this an unprecedented kind of break (worse than prior type-system-assumption-breaking RFCs), and that without integration into `Result`, async, `==`, or newtypes the feature will feel "bolted on" Quote: "this RFC is proposing to introduce a fundamentally new kind of thing to Rust only to then make that thing a complete nightmare to use for anything" [`a-sa29-f013113-c2`, team a]
  - `externref-in-rust--table-index-in-rust-code` — Table-index wrapper, real `externref` only at FFI
    - **juntyr** · Source `f013113` · date 2026-07-29T13:09:09Z · locator RFC #3987, comment 2026-07-29T13:09:09Z — proposes that `externref` act as a table index everywhere in Rust-only code, with the actual WASM `externref` only crossing at FFI boundaries, and an optimization pass eliding the table insert/extract round-trip when a value is merely passed through Quote: "a non-zero cost wrapper could work better" [`a-sa29-f013113-c3`, team a]
  - `externref-in-rust--keep-out-of-language-core` — Leave it to the compiler or runtime
    - **ds84182** · Source `f013113` · date 2026-07-30T02:36:47Z · locator RFC #3987, comment 2026-07-30T02:36:47Z — notes `__externref_t` is Clang's own non-standard extension, unmatched by GCC or MSVC, and argues WebAssembly's design oddities should be papered over by the compiler/runtime rather than by changing the language core for something this niche Quote: "I do not think languages should change at such a core level to support something extremely niche like this" [`a-sa29-f013113-c4`, team a]
- Positions seen by the extractor (`a-sa29-f013113-q1`): new opaque bare-position-only lang-item type mirroring Clang's `__externref_t` (guybedford, RFC author) vs. reject any type outside Rust's Abstract Machine semantics, represent it as a first-party table/index concept instead (RalfJung) vs. middle path: table-index in ordinary Rust code, real Wasm `externref` only crossing at `extern "C"` boundaries with compiler-elided conversions (juntyr, echoed by programmerjake and ds84182)
- Positions seen by the extractor (`a-sa29-f013113-q2`): JS interop is significant enough to justify a core-language change, and Rust has solved harder/more niche problems before (guybedford) vs. WASM's oddities are Clang-specific precedent (unmatched by GCC/MSVC) and belong in the compiler/runtime, not the language core (ds84182)

### `extract-single-use-function`

**Question.** Should single-use or repeated inline logic be extracted into a named function or method, or kept inline?

- Grouping: Same extract-or-inline choice at function and method level; module-level placement stays apart.
- Absorbs merge-final ids: `encapsulate-invariant-check-method`
- Teams: b · members (context): `b-sR12-f005085-q1` (f005085, ml, core); `b-sb04-f001392-q3` (f001392, core)
- Domains: core, ml
- Concepts: encapsulation; invariants; unsafe; maintainability; function extraction; code communication; single-use helpers; method length
- Positions:
  - `extract-single-use-function--extract-for-communication` — Extract into a named function or method
    - **antimora (Tracel AI / burn maintainer)** · Source `f005085` · date 2026-09-08 · locator PR review comment, 2026-09-08T21:11:40Z — the same dense/non-broadcast check is duplicated verbatim at two call sites gating `storage_mut()`, so drift between them would silently produce a bad write instead of a compile error; it should be a single method on `Layout` that documents the actual contract Quote: "This is duplicated verbatim at `ops/gather_scatter.rs:18`. Both copies gate `storage_mut()`, so a drift between them is a bad write rather than a compile error... Reads better as a single method on `Layout` carrying the actual contract." [`b-sR12-f005085-c1`, team b]
    - **joshka** · Source `f001392` · date 2024-05-11 · locator PR #1089, comment 2024-05-11T11:12:04Z — pulls span-visibility logic into its own method even though it has one caller, because a well-named function with a defined input/output lets the reader trust what it does without re-deriving it; functions are "a tool for communicating blocks of code", not just for reuse Quote: "Functions are not just a tool for reuse, they're a tool for communicating blocks of code like this." [`b-sb04-f001392-c5`, team b]
  - `extract-single-use-function--keep-inline` — Keep it inline where used
    - **EdJoPaTo** · Source `f001392` · date 2024-05-11 · locator PR #1089, comment 2024-05-11T09:24:22Z — argues against extracting the same logic into its own method, since it is very specific to one caller (`render_spans`) and pulling it out (and naming it `visible`) risks being misleading about what it actually guarantees Quote: "I don't think moving this into its own method is very useful. Its very specific to the render_span method." [`b-sb04-f001392-c6`, team b]
- Positions seen by the extractor (`b-sR12-f005085-q1`): encapsulate-as-named-method
- Positions seen by the extractor (`b-sb04-f001392-q3`): extract-for-communication, inline-when-single-use

### `ffi-ui-state-snapshots-vs-diffs`

**Question.** When Rust pushes state across a boundary to a UI, send whole snapshots or only deltas?

- Grouping: Same choice for SwiftUI and for a JS canvas.
- Teams: a · members (context): `a-sB02-f000256-q4` (f000256, web, wasm); `a-sa18-f008389-q1` (f008389, swift-interop)
- Domains: swift-interop, wasm, web
- Concepts: rendering strategy; wasm/js boundary; FFI; UniFFI; proc-macros; state-diffing; declarative-UI
- Positions:
  - `ffi-ui-state-snapshots-vs-diffs--p1` — whole-snapshot(chosen)
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Interfacing Rust and JavaScript in our Game of Life" — the tutorial exposes the whole universe (as a pointer into linear memory) each tick rather than the delta-based design, naming the delta approach as a viable but harder-to-implement alternative. Quote: "Another viable design alternative would be for Rust to return a list of every cell that changed states after each tick... The trade off is that this delta-based design is slightly more difficult to implement." [`a-sB02-f000256-c4`, team a]
  - `ffi-ui-state-snapshots-vs-diffs--p2` — rust-side-tracks-and-emits-diffs
    - **TantalusPath (Serendipity Systems LLC)** · Source `f008389` · date 2025-03-27 · locator "How procedural macros made it better" section — after iterating through three worse designs (manual return-value wiring, one-function-per-field event handlers, an all-optional `StateUpdateModel` requiring manual `Some`-checking on the Swift side), settled on a derive proc macro that generates a companion struct plus a diff enum, so the Rust side tracks uncommitted field changes and the Swift side gets a `[FieldValue]` diff it applies via an exhaustive `switch`, which the Swift compiler will fail to build if a new field isn't handled Quote: "If a state field is added or removed on the Rust side, this Swift function will fail compilers' enum exhaustiveness checks until it is added." [`a-sa18-f008389-c1`, team a]
- Positions seen by the extractor (`a-sB02-f000256-q4`): whole-snapshot(chosen), delta-based(alternative, harder to implement)
- Positions seen by the extractor (`a-sa18-f008389-q1`): rust-side-tracks-and-emits-diffs, ui-diffs-full-snapshot-itself

### `hal-driver-typestate`

**Question.** Should an embedded HAL driver encode its mode or configuration as a typestate generic, or keep a runtime mechanism?

- Grouping: Same esp-hal driver-API choice for mode and for configuration.
- Absorbs merge-final ids: `typestate-driver-mode`, `typestate-hal-config`
- Teams: b · members (context): `b-sb03-f000715-q1` (f000715, embedded); `b-sb05-f001512-q2` (f001512, embedded)
- Domains: embedded
- Concepts: typestate; generics; traits; interrupt handling; type-state pattern; embedded HAL API design
- Positions:
  - `hal-driver-typestate--encode-in-types` — Encode it in types
    - **MabezDev** · Source `f000715` · date 2024-01-05 · locator issue #1063, comment 2024-01-05T16:28:34Z — proposes a typestate `Uart<T: Instance, M>` where `M` is `Blocking` or `Async`, with per-mode constructors, so a cargo feature no longer determines whether a driver is async; interrupt handlers move from link-time binding to a runtime-installed `__INTERRUPTS` array Quote: "a feature should not determine a driver whether a driver is async or blocking, it should be determined by how its initialized." [`b-sb03-f000715-c1`, team b]
  - `hal-driver-typestate--runtime-or-raw` — A simpler runtime mechanism or raw form
    - **bjoernQ** · Source `f000715` · date 2024-01-05 · locator issue #1063, comment 2024-01-05T16:38:20Z — had a similar runtime-binding idea in mind independently, but without introducing the typestate Quote: "Basically, had a similar thing in mind (minus the type-state)." [`b-sb03-f000715-c2`, team b]
  - `hal-driver-typestate--typestate-costly` — Typestate is possible but costly
    - **bjoernQ** · Source `f001512` · date 2024-05-24 · locator comment 2024-05-24T15:15:23Z — type-state could resolve the TX/RX default-pin ambiguity but adds ongoing complexity Quote: "Maybe adding type-state but that gets annoying later" [`b-sb05-f001512-c2`, team b]
- Positions seen by the extractor (`b-sb03-f000715-q1`): typestate-mode-selection, simpler-runtime-mechanism
- Positions seen by the extractor (`b-sb05-f001512-q2`): type-state-suggested-but-costly (bjoernQ)

### `hard-dependency-vs-pluggable-interface`

**Question.** Should a crate hard-depend on one implementation (allocator, crypto backend) or expose a pluggable interface?

- Grouping: Same coupling choice.
- Absorbs merge-final ids: `hard-dependency-vs-interface-decoupling`, `pluggable-crypto-backend`
- Teams: a · members (context): `a-sR06-f001989-q1` (f001989, embedded); `a-sR13-f004586-q1` (f004586, decentralized-iroh, core)
- Domains: core, decentralized-iroh, embedded
- Concepts: crate coupling; global allocator; feature flags; dependency injection; TLS backend selection
- Positions:
  - `hard-dependency-vs-pluggable-interface--pluggable-interface` — Keep a pluggable interface
    - **bjoernQ** · Source `f001989` · date 2024-09-06 · locator PR #2099, comment 2024-09-06T09:38:15Z — explains the design choice was driven by wanting to avoid forcing a release of `esp-wifi` on every `esp-alloc` release. Quote: "I wanted to avoid a hard dependency in `esp-wifi` to not require a new release whenever `esp-alloc` gets a release." [`a-sR06-f001989-c1`, team a]
    - **iroh/n0 (dignifiedquire, post author)** · Source `f004586` · date 2026-04-17 · locator § "Pluggable Crypto Backends" — iroh 0.98 makes the TLS crypto provider swappable via feature flags (`ring` default, `aws-lc-rs` alternative, or a fully custom provider), because a hard-pinned `ring` dependency breaks on platforms where it can't build or where an org mandates a FIPS-certified backend Quote: "It's a problem if you're on a platform where ring doesn't build, if your org mandates a FIPS-certified backend like aws-lc-rs" [`a-sR13-f004586-c1`, team a]
  - `hard-dependency-vs-pluggable-interface--hard-dependency-behind-feature` — A hard dependency behind a feature flag is fine
    - **MabezDev** · Source `f001989` · date 2024-09-06 · locator PR #2099, comment 2024-09-06T11:10:19Z — pushes back on avoiding the dependency outright, proposing instead that the allocator-callback functions move into `esp-wifi` behind an `esp-alloc` feature. Quote: "Imo, the hard dependency is fine as we can add it behind a feature in esp-wifi." [`a-sR06-f001989-c2`, team a]
- Positions seen by the extractor (`a-sR06-f001989-q1`): "avoid the hard dependency, keep it an interface" (bjoernQ); "a hard dependency behind a feature flag is fine" (MabezDev)
- Positions seen by the extractor (`a-sR13-f004586-q1`): pluggable-by-default (iroh)

### `human-written-code-standard`

**Question.** How much of a project's own code may be AI-written, and with how much review: human-written only, or AI-written with light review?

- Grouping: Same authorship choice for critical and peripheral code; following AI review tools stays apart.
- Absorbs merge-final ids: `ai-code-review-depth`
- Teams: a · members (context): `a-sR14-f004865-q2` (f004865, web, embedded); `a-sa15-f005821-q2` (f005821, core)
- Domains: core, embedded, web
- Concepts: ai-assisted-rust; authorship-norms
- Positions:
  - `human-written-code-standard--human-written-for-critical-code` — Hold critical work to human-written-only
    - **Matt Keeter** · Source `f005821` · date 2026-04-05 · locator opening paragraphs, linking to his earlier post "Experimenting with LLMs" — states plainly, as a personal standard rather than an argued position, that all the tail-call code and the blog post itself are human-written, after an earlier LLM-assisted port "proved controversial" Quote: "I'm pleased to declare that all of the tail-call code is human-written... (This blog post is also entirely human-written, per my personal standards)" [`a-sa15-f005821-c2`, team a]
  - `human-written-code-standard--light-review-for-peripheral-code` — A brief check is enough for peripheral code
    - **Klaehn** · Source `f004865` · date 2026-07-02 · locator "A proper GUI" section — acceptable to let an LLM write a whole peripheral component (a JS/WASM GUI) you lack expertise in, and ship it after only a brief check, rather than deep review — ties to the AI-assisted-Rust candidate Question already flagged in rust.md § Findings. Quote: "I am not a javascript developer, so the WASM GUI is vibe coded. I just briefly checked it." [`a-sR14-f004865-c2`, team a]
- Positions seen by the extractor (`a-sR14-f004865-q2`): light-touch-for-peripheral-code (Klaehn)
- Positions seen by the extractor (`a-sa15-f005821-q2`): human-written-only-as-personal-standard

### `kernel-constants-hardcode-vs-comptime`

**Question.** Should backend- or dtype-specific kernel constants be hardcoded, or passed as comptime parameters or derived from type metadata?

- Grouping: Same choice in two burn PRs.
- Absorbs merge-final ids: `per-dtype-constant-match-vs-metadata`
- Teams: b · members (context): `b-sR05-f002048-q2` (f002048, ml); `b-sR10-f004573-q2` (f004573, ml, core)
- Domains: core, ml
- Concepts: generics; traits; exhaustive match; floating-point
- Positions:
  - `kernel-constants-hardcode-vs-comptime--parameterize-constants` — Pass through a comptime struct or derive from metadata
    - **louisfd (tracel-ai/burn maintainer)** · Source `f002048` · date 2024-09-23 · locator tracel-ai/burn#2287, comment 2024-09-23T14:26:38Z. · L977-L979. — hardcode for now but pass the values through a comptime struct so a future backend-specific change (e.g. a different warp/wavefront size on AMD) doesn't require touching the kernel body. Quote: "I think it's fine to hardcode these values for now, but they should be passed to the cube kernel via a comptime struct, because the day they will change (for amd it's 64 for instance) we won't have to change the kernels, just the launch." [`b-sR05-f002048-c2`, team b]
    - **antimora (Tracel AI / burn maintainer)** · Source `f004573` · date 2026-04-21 · locator PR review comment, 2026-04-21T14:45:21Z — hardcoded per-dtype epsilon constants should be replaced by a generic accessor on the dtype's own precision metadata, since it is self-documenting and handles all float dtypes including Flex32 uniformly Quote: "`burn_std::FloatDType::finfo()` would be a strict improvement over the hardcoded constants here... self-documenting, dtype-correct, and Flex32 falls out for free." [`b-sR10-f004573-c3`, team b]
  - `kernel-constants-hardcode-vs-comptime--hardcode-for-this-use` — Hardcode for this specific use
    - **antimora (Tracel AI / burn maintainer)** · Source `f004573` · date 2026-04-21 · locator PR review comment, 2026-04-21T14:45:23Z — for this particular pivot-replacement site, machine epsilon is the wrong semantic quantity regardless of dtype, so the exact-zero check should stay rather than switch to finfo Quote: "On whether to use `finfo` here instead: I'd say no... the pivot-replacement here is better off staying exact-zero." [`b-sR10-f004573-c4`, team b]
- Positions seen by the extractor (`b-sR05-f002048-q2`): hardcode for now but pass the values through a comptime struct so a future backe (louisfd (tracel-ai/burn maintainer))
- Positions seen by the extractor (`b-sR10-f004573-q2`): derive-from-metadata-generally-better, reject-metadata-for-this-specific-use

### `lifetimes-on-structs`

**Question.** Should structs carry lifetime parameters (borrowed data) or keep data owned?

- Grouping: Same choice in two posts.
- Teams: b · members (context): `b-sb20-f007364-q1` (f007364, core); `b-sb20-f007608-q2` (f007608, core)
- Domains: core
- Concepts: lifetimes; borrowing; zero-copy design; ownership; struct design
- Positions:
  - `lifetimes-on-structs--borrow-for-measured-performance` — Add lifetime parameters where a measured bottleneck justifies them
    - **howardjohn** · Source `f007364` · date 2026-03-04 · locator section "References#" preceded by "Native types in CEL#" and "References#" (value type redefinition under heading "References#" appears just after "Ultimate solution"); exact quote is from the paragraph beginning "First, we need references!" — converting `Value` from an owned enum to `Value<'a>` with `Cow`-like `Borrowed`/`Owned` variants (and a `Dynamic`/`DynamicType` trait for native Rust types) was the key change that let a CEL evaluation get within ~10ns of native code, versus 147ns for the original owned/hashmap-based implementation Quote: "First, we need references! We change Value to not be owned" [`b-sb20-f007364-c1`, team b]
  - `lifetimes-on-structs--owned-by-default` — Avoid lifetimes on structs as a rule; favor easy-mode owned types, especially for teams new to Rust
    - **jacko.io** · Source `f007608` · date 2023-10-25 · locator footnote to the paragraph beginning "Playing with these examples is educational" in section "Part Two: Borrowing" — while experimenting with borrow-checker fights builds useful intuition, the actionable takeaway when you get stuck is to keep lifetime parameters off your struct definitions Quote: "a good rule of thumb is to avoid putting lifetime parameters on structs" [`b-sb20-f007608-c2`, team b]
- Positions seen by the extractor (`b-sb20-f007364-q1`): embrace lifetime parameters deliberately, rewriting an owned `Value` enum as `Value<'a>` with `Borrowed`/`Owned` variants, to eliminate a measured bottleneck (howardjohn) — conflicts with f007608 below, which states the opposite rule of thumb
- Positions seen by the extractor (`b-sb20-f007608-q2`): avoid lifetime parameters on structs as a rule of thumb (jacko.io) — conflicts with f007364 above, which embraces them for a measured performance win

### `lts-release-channel`

**Question.** Should a project support older release lines (an LTS train, backports) or require upgrading?

- Grouping: Same support-window choice.
- Teams: b · members (context): `b-sR06-f002937-q1` (f002937, wasm, core); `b-sT05-f002501-q1` (f002501, web, core)
- Domains: core, wasm, web
- Concepts: release cadence; semver/API compatibility; security-fix support windows; ecosystem maintenance burden; semver pre-1.0 minors; backports; upgrade cost of upstream breaking changes (axum 0.8 path syntax)
- Positions:
  - `lts-release-channel--support-old-lines` — Keep older lines supported (LTS train, backport the fix)
    - **Alex Crichton** · Source `f002937` · date 2025-04-22 · locator "Wasmtime LTS Releases" article, paragraphs 2-4 (bytecodealliance.org/articles/wasmtime-lts) — Wasmtime previously supported each monthly release for only 2 months, forcing embedders to track upstream closely for security fixes; Wasmtime now designates every 12th release an LTS release, guaranteed 24 months of API-compatible security patches (no backported features), so users can upgrade yearly instead of monthly while still receiving guaranteed security fixes Quote: "This rate of change can be too fast for users so Wasmtime now supports LTS releases." [`b-sR06-f002937-c1`, team b]
  - `lts-release-channel--upgrade-instead` — No backport; upgrade
    - **kaplanelad** · Source `f002501` · date 2025-01-10 · locator comment 2025-01-10T16:08:08Z — points to loco upgrade guide for axum breaking changes; declines applying the CORS fix to 0.13.x Quote: "Unfortunately, I can't apply this fix to version 0.13.x. It's recommended to upgrade" (flag: voice-unverified) [`b-sT05-f002501-c1`, team b]
- Positions seen by the extractor (`b-sR06-f002937-q1`): "adopt a formal LTS release train, decoupled from the fast release cadence" (Alex Crichton / Wasmtime)
- Positions seen by the extractor (`b-sT05-f002501-q1`): no backport, upgrade recommended; backport branch on old minor requested

### `networking-lib-core-scope`

**Question.** Should a networking library bundle many protocols and transports in its core, or keep a minimal core with pluggable extensions?

- Grouping: Same choice in two iroh sources.
- Teams: a · members (context): `a-sR11-f004170-q1` (f004170, distributed, decentralized-iroh); `a-sa02-f002124-q1` (f002124, decentralized-iroh, distributed)
- Domains: decentralized-iroh, distributed
- Concepts: custom transports; trait objects; feature flags; dependency weight; library scope; minimalism vs batteries-included; protocol layering; API surface
- Positions:
  - `networking-lib-core-scope--minimal-core-pluggable` — Minimal core, pluggable trait extensions
    - **Rüdiger Klaehn** · Source `f004170` · date 2026-01-27 · locator section "What are iroh custom transports anyway?" — iroh will not build every candidate transport (WebTransport, Bluetooth, Tor, InfiniBand, ...) into the core; adding them all would create a maze of feature flags and drag in dependencies most users don't need, so the library exposes `CustomTransport`/`CustomEndpoint`/`CustomSender` traits for users to plug in only what they need Quote: "we do not want to add additional transports to the iroh codebase. That would make the code very complex with a maze of feature flags, add a lot of dependencies that most of our customers don't need" [`a-sR11-f004170-c1`, team a]
    - **ramfox** · Source `f002124` · date 2024-10-01 · locator opening section / "Docs are disabled by default" — iroh's maintainers deliberately shrank the library's default scope, disabling the higher-level "Docs" sync feature by default and reframing it as a separate protocol layered on the core networking primitive, restating an earlier decision that iroh's networking stack is "what iroh is" and everything else is a custom protocol Quote: "We're doubling down on iroh's networking stack as 'what iroh is' and describing everything else as a custom protocol." [`a-sa02-f002124-c1`, team a]
- Positions seen by the extractor (`a-sR11-f004170-q1`): minimal-core-plus-pluggable-traits (Rüdiger Klaehn)
- Positions seen by the extractor (`a-sa02-f002124-q1`): narrow-core-scope-by-default (author/iroh maintainers)

### `non-exhaustive-by-default`

**Question.** Should public enums and structs heading toward 1.0 default to `#[non_exhaustive]`?

- Grouping: Same choice in two iroh sources.
- Teams: a · members (context): `a-sR13-f004586-q2` (f004586, decentralized-iroh, core); `a-sT08-f004169-q2` (f004169, core)
- Domains: core, decentralized-iroh
- Concepts: API stability; semver; non_exhaustive; `#[non_exhaustive]`; forward compatibility; 1.0 stability
- Positions:
  - `non-exhaustive-by-default--non-exhaustive-by-default` — Yes
    - **iroh/n0 (dignifiedquire, post author)** · Source `f004586` · date 2026-04-17 · locator § "Breaking Changes", multiple types marked `#[non_exhaustive]` (`iroh::DirectAddrType`, `iroh::address_lookup::mdns::DiscoveryEvent`) — newly public/changed types are marked non-exhaustive so future variants can be added without a breaking change Quote: none (structural, not prose declaration) [`a-sR13-f004586-c2`, team a]
    - **ramfox** · Source `f004169` · date 2026-01-27 · locator § "TransportAddr rather than conn_type and ConnectionType" — because custom transports (bluetooth, WebRTC) are a planned direction, iroh 1.0 must handle new address kinds, so `TransportAddr` is a non-exhaustive enum replacing `ConnectionType` Quote: "we need to make sure that iroh 1.0 can handle supporting different kinds of addresses" (flag: voice-unverified — as above.) [`a-sT08-f004169-c2`, team a]
    - **iroh/n0 (Friedel Ziegelmayer & Rüdiger Klaehn, post authors)** · Source `f004685` · date 2026-05-11 · locator § "Non-exhaustive structs and enums" — restates and extends the 0.98 non_exhaustive Position — `PathEvent` and `IncomingLocalAddr` are marked non-exhaustive specifically to allow future variants without breaking the public API, requiring callers to add a wildcard match arm Quote: "PathEvent and IncomingLocalAddr are both #[non_exhaustive], so the compiler requires you to handle the case of variants we may add later." [`a-sR13-f004685-c3`, team a]
- Positions seen by the extractor (`a-sR13-f004586-q2`): non_exhaustive-by-default (iroh)
- Positions seen by the extractor (`a-sT08-f004169-q2`): non-exhaustive-for-future-variants

### `object-graph-representation`

**Question.** How to represent a cyclic mutable object graph: `Rc<RefCell>`, raw pointers, or indices into an arena?

- Grouping: Same concrete choice; split back out of shared-mutable-state.
- Teams: b · members (context): `b-sb20-f007608-q1` (f007608, core); `b-sb26-f013214-q3` (f013214, other, core)
- Domains: core, other
- Concepts: interior mutability; Rc/RefCell; Arc/Mutex; unsafe pointers; arenas; ECS; ownership mismatch; scripting-language embedding; handles
- Positions:
  - `object-graph-representation--indices-or-handles` — Indices into an arena, or a separate handle domain, for object graphs
    - **jacko.io** · Source `f007608` · date 2023-10-25 · locator section "Part Four: Indexes" — `Rc<RefCell<T>>` compiles for "object soup" but leaks memory on reference cycles and panics on self-referential mutable borrows (`already mutably borrowed: BorrowError`); raw/unsafe pointers hit the same aliasing problems and risk undefined behavior; keeping objects in a `Vec` and referring to each other by `usize` index avoids both, turns aliasing bugs into compiler errors, and serializes/parallelizes cleanly with `serde`/`rayon` Quote: "This is how we write object soup in Rust." [`b-sb20-f007608-c1`, team b]
    - **CAD97** · Source `f013214` · date 2024-05-04 · locator reply timestamped 2024-05-04T23:38:57 — attributes Rust's difficulty embedding scripting languages to a fundamental mismatch in how Rust and a guest language model mutability, ownership, generics, and callback-driven coupling; states games are "giant tangled graphs of mutable state with unclear and unstructured ownership," something Rust isn't well suited to represent directly, so the best approach he can picture pairs an ECS-ish API on the Rust side with an OO-ish API on the guest side, joined through handles — though he notes he has never actually built this out to prove it works Quote: "Games fundamentally are giant tangled graphs of mutable state with unclear and unstructured ownership, something Rust fundamentally isn't all that great at." [`b-sb26-f013214-c5`, team b]
- Positions seen by the extractor (`b-sb20-f007608-q1`): index/arena-based design, avoiding both `Rc<RefCell<T>>` (leak- and panic-prone) and raw pointers (undefined-behavior-prone) (jacko.io)
- Positions seen by the extractor (`b-sb26-f013214-q3`): for a Rust game engine embedding a guest scripting/modding language, model the guest world as a fully separate object-soup domain bridged only by opaque handles, since Rust's ownership/generics/callback model doesn't naturally accommodate the "giant tangled graph of mutable state" that games and their scripting layers are (CAD97) — the same handle/indirection position as f007608, applied to the scripting-integration case specifically

### `oss-reuse-attribution-norms`

**Question.** Is rehosting or reusing another project's code without coordination or credit acceptable?

- Grouping: Same norm in two disputes.
- Teams: a · members (context): `a-sa05-f003025-q2` (f003025, core); `a-sa13-f004772-q4` (f004772, core)
- Domains: core
- Concepts: open-source-governance; licensing; forking; branding; attribution; collaboration-norms
- Positions:
  - `oss-reuse-attribution-norms--coordination-and-credit-matter` — Coordination and credit matter
    - **cart** · Source `f003025` · date 2025-06-01 · locator comment @cart 2025-06-01T22:35:03Z — taking a project's work wholesale and redistributing it without discussing it first is "bad form" even where the license permits it, because banners/brands carry the social and financial capital that sustains maintainers Quote: "If someone were to publish a 'debranded' Bevy Reflect without discussing it with us, I would consider that bad form. Legal according to the license, but bad form nonetheless." [`a-sa05-f003025-c6`, team a]
    - **jkelleyrtp** · Source `f003025` · date 2025-06-02 · locator comment @jkelleyrtp 2025-06-02T07:00:30Z — copying, stripping, and renaming another team's code, then seeking maintainers for it, without reaching out first, is disrespectful of the original authors' investment even though the license allows it Quote: "Instead of reaching out with an offer to help modularize the subsecond engine, you went straight to copy-pasting our code into a new project, stripping it down, renaming it, and then started shopping around for help to maintain it." [`a-sa05-f003025-c8`, team a]
    - **SomeoneToIgnore** · Source `f004772` · date 2026-08-02 · locator comment @SomeoneToIgnore 2026-08-02T15:31:14Z — points out a function copy-pasted almost verbatim, bugs included, from a different open PR (#62051), and asks that a co-authored-by credit be added if code was really copied from it Quote: "How come a different PR has the very same function, almost verbatim, copy-pasted from [...] Including all the worst bugs of it... If you have really copied parts of the other PR, do add a co-authored-by metadata to this PR and include @interkelstar into that." [`a-sa13-f004772-c7`, team a]
    - **ysalitrynskyi** · Source `f004772` · date 2026-08-02 · locator comment @ysalitrynskyi 2026-08-02T18:58:14Z — concedes the point and adds attribution after the fact, crediting both prior PRs the navigation core derived from Quote: "Co-authored-by: Vlad Gevsky is now on the commits (including the base one), and the PR body credits both #62051 and #50719." [`a-sa13-f004772-c8`, team a]
  - `oss-reuse-attribution-norms--no-entitlement` — No entitlement to control reuse
    - **hecrj** · Source `f003025` · date 2025-06-02 · locator comment @hecrj 2025-06-02T02:49:06Z — producers of open source are not entitled to control over branding or how their code is reused; forking and improving others' code is the essence of open source, not a breach of it Quote: "I don't think 'producers' of open source should be entitled to anything; the same way 'consumers' aren't either. This is the real beauty of open source—a gift with no expectations." [`a-sa05-f003025-c7`, team a]
- Positions seen by the extractor (`a-sa13-f004772-q4`): branding-and-coordination-matter, no-entitlement-forking-is-core-of-oss

### `public-naming-brevity-vs-clarity`

**Question.** Should a public name favor brevity or clarity?

- Grouping: Same naming choice in two sources; naming a feature for its mechanism stays apart.
- Teams: b · members (context): `b-sR04-f001515-q1` (f001515, decentralized-iroh); `b-sR04-f001617-q1` (f001617, desktop-cli-ui)
- Domains: decentralized-iroh, desktop-cli-ui
- Concepts: API naming; public interface design; tooling/extension naming
- Positions:
  - `public-naming-brevity-vs-clarity--clarity-over-brevity` — Name for clarity and the literal mechanism
    - **dignifiedquire** · Source `f001515` · date 2024-05-24 · locator § "The MagicEndpoint is dead, long live the Endpoint" — renamed the public type `MagicEndpoint` to plain `Endpoint`, reasoning that a fun/evocative name became a liability once it got too long, even though the team liked it. Quote: "Fun names are great, but sometimes they get in the way, and while we all loved MagicEndpoint as a name, it just became too long." [`b-sR04-f001515-c1`, team b]
    - **osiewicz** · Source `f001617` · date 2024-06-19 · locator PR #13253, comment 2024-06-19T11:34:20Z — declined a suggestion to shorten the language-server's name to the abbreviation "scls", preferring to spell out "snippets" so users can infer what the name means. Quote: "I think it makes sense to spell out `snippets` explicitly in the name to make it a bit easier on the users." [`b-sR04-f001617-c1`, team b]
- Positions seen by the extractor (`b-sR04-f001515-q1`): rename-for-clarity-over-fun-brevity
- Positions seen by the extractor (`b-sR04-f001617-q1`): name-for-clarity-over-brevity

### `rtic-is-an-rtos`

**Question.** Is RTIC an RTOS or a concurrency framework?

- Grouping: Same question in two team-a reads of the RTIC book.
- Teams: a · members (context): `a-sB01-f000227-q1` (f000227, embedded); `a-sR01-f000227-q1` (f000227, embedded)
- Domains: embedded
- Concepts: RTOS-definition; hardware-accelerated-scheduling; software-kernel; RTIC; RTOS; Stack Resource Policy (SRP); hardware-accelerated scheduling
- Positions:
  - `rtic-is-an-rtos--p1` — RTIC is a (hardware-accelerated) RTOS
    - **RTIC developers (rtic.rs maintainers)** · Source `f000227` · date undated (living doc, "documentation for RTIC v2.x") · locator Preface, "Is RTIC an RTOS?" — From the developers' own point of view RTIC is an RTOS that uses hardware (NVIC/CLIC) to perform scheduling rather than a classical software kernel, against an "another common view from the community" that calls it a concurrency framework instead — that opposing view is not attributed to a named, checkable Voice in this source Quote: "From RTIC's developers point of view; RTIC is a hardware accelerated RTOS" [`a-sB01-f000227-c1`, team a]
    - **RTIC project (rtic.rs maintainers, unnamed individually)** · Source `f000227` · date unknown (living document, no publish/version date given) · locator § "Is RTIC an RTOS?" — from the maintainers' own view RTIC is a hardware-accelerated RTOS because it uses hardware (e.g. NVIC on Cortex-M) rather than a software kernel to perform scheduling. Quote: "RTIC is a hardware accelerated RTOS that utilizes the hardware such as the NVIC on Cortex-M MCUs, CLIC on RISC-V etc. to perform scheduling, rather than the more classical software kernel." [`a-sR01-f000227-c1`, team a]
- Positions seen by the extractor (`a-sB01-f000227-q1`): RTIC-team: it is a (hardware-accelerated) RTOS; unattributed community view: it is a concurrency framework, not an RTOS
- Positions seen by the extractor (`a-sR01-f000227-q1`): "hardware-accelerated RTOS" (RTIC project); "concurrency framework, no software kernel" (unattributed community view, no named Voice — not a Claim)

### `rust-for-high-level-apps`

**Question.** Should Rust be used for high-level, rapid-prototyping application development?

- Grouping: One domain, high-level apps: whether to push Rust there and its productivity for prototyping.
- Absorbs merge-final ids: `rust-prototyping-productivity`
- Teams: a · members (context): `a-sa26-f011305-q1` (f011305, desktop-cli-ui, frontend, web, other); `a-sa26-f011305-q2` (f011305, core, web, frontend)
- Domains: core, desktop-cli-ui, frontend, other, web
- Concepts: application frameworks; systems vs application programming; compile times; developer productivity; language ergonomics
- Positions:
  - `rust-for-high-level-apps--push-rust-into-high-level-apps` — Push Rust into high-level application development
    - **Jonathan Kelly [likely Kelley; unconfirmed]** · Source `f011305` · date 2025-10-03 · locator ~03:01 — Rust's mission should not be exclusive to systems/"core" software; high-level Rust development deserves the same investment Quote: "I don't think this should be exclusive to so-called core software" [`a-sa26-f011305-c1`, team a]
  - `rust-for-high-level-apps--less-productive-for-prototyping` — Today Rust is less productive than high-level frameworks for prototyping
    - **Jonathan Kelly** · Source `f011305` · date 2025-10-03 · locator ~02:01 — long compile times and language rigidity made Dioxus's own users more productive with existing tools like React and FastAPI than with early high-level Rust Quote: "we realized that Rust just wasn't that fast to write. Due to the long compile times and language rigidity, our users were simply more productive" [`a-sa26-f011305-c2`, team a]
- Positions seen by the extractor (`a-sa26-f011305-q1`): push-Rust-into-high-level-dev (Jonathan Kelley/Dioxus)
- Positions seen by the extractor (`a-sa26-f011305-q2`): yes-less-productive-but-worth-fixing (Jonathan Kelley)

### `service-fault-isolation-degrade`

**Question.** Should a unit failure in a long-running service stop it, or be contained and degraded?

- Grouping: Same containment choice.
- Teams: a · members (context): `a-sR05-f001981-q1` (f001981, distributed, decentralized-iroh); `a-sa14-f004985-q3` (f004985, wasm, cloud-workers)
- Domains: cloud-workers, decentralized-iroh, distributed, wasm
- Concepts: error handling; accept loops; async I/O; fault handling; panic containment; resilience by design
- Positions:
  - `service-fault-isolation-degrade--contain-and-continue` — Contain, log, keep serving
    - **matheus23 (iroh maintainer, n0)** · Source `f001981` · date 2024-09-04 · locator "API Changes" section — `Incoming::accept` can fail for benign network reasons; such failures should be logged and passed over, not treated as fatal Quote: "don't treat errors there as fatal" [`a-sR05-f001981-c1`, team a]
    - **Celso Martinho, Ruskin Constant, Rui Figueira, and Luís Duarte** · Source `f004985` · date 2026-08-06 · locator § Design decisions / Exception handling — commit as a design rule, before writing code, that any failure degrades to a blank frame or missing element rather than crashing the session, since the browser must render hostile, unreliable pages without ever dropping the one it's holding Quote: "any failure degrades to a blank frame or a missing element, never a dead session" [`a-sa14-f004985-c3`, team a]
- Positions seen by the extractor (`a-sR05-f001981-q1`): non-fatal, log-and-continue
- Positions seen by the extractor (`a-sa14-f004985-q3`): commit up front to catching faults at every boundary and degrading to a blank frame or missing element, never a dead session

### `std-naming-conventions-strictness`

**Question.** How strictly to follow std's `as_`/`to_`/`into_` naming convention?

- Grouping: Same convention in two sources; `raw_parts` naming stays apart.
- Absorbs merge-final ids: `into-naming-must-consume`, `to-owned-naming-convention`
- Teams: b · members (context): `b-sR08-f003587-q2` (f003587, ml); `b-sb22-f009236-q1` (f009236, core)
- Domains: core, ml
- Concepts: naming conventions; ownership semantics; API naming conventions; trait naming; Rust API Guidelines
- Positions:
  - `std-naming-conventions-strictness--strict` — Follow the convention strictly (`into_` consumes, `to_owned` is correct)
    - **nathanielsimard** · Source `f003587` · date 2025-10-09 · locator PR #3792, review comments 2025-10-09T12:33:22Z and 2025-10-09T13:27:11Z — objects to a method using `into_`-style naming that doesn't actually take ownership of `self`, insisting the name should match the ownership signature and proposing a rename. Quote: "The naming isn't correct here, into should consume a self. Maybe `from_mapped_value`" [`b-sR08-f003587-c2`, team b]
    - **steffahn** · Source `f009236` · date 2025-01-07 · locator reply timestamped 2025-01-07T16:10:44 — points directly to the Rust API Guidelines naming-conventions document as the standing rationale for the `to_` prefix here Quote: "In that framework, to_ is the correct naming choice." [`b-sb22-f009236-c2`, team b]
    - **jrose** · Source `f009236` · date 2025-01-08 · locator reply timestamped 2025-01-08T01:57:00 — the receiver of `to_owned` is neither doing the owning nor being owned — it is being copied into a different form — so `own()` would misdescribe the operation; naming here is inherently imperfect, but that doesn't make the existing name bad Quote: "no, I don't actually think to_owned is a bad name." [`b-sb22-f009236-c3`, team b]
  - `std-naming-conventions-strictness--loose` — Reuse the convention loosely, or rename to a bare verb
    - **jvcmarcenes** · Source `f009236` · date 2025-01-07 · locator opening post, and follow-up timestamped 2025-01-07T16:24:46 — argues by analogy that `Clone`/`Borrow` aren't named `ToCloned`/`AsBorrowed`, so the `to_`/`as_`/`into_` prefix convention is unneeded "morphology" when converting between representations of the *same* type, even while granting the prefix convention makes sense for genuine cross-type conversions like `IntoIterator` Quote: "It should just be Own... I'd much rather write \"whatever\".own() than \"whatever\".to_owned()." [`b-sb22-f009236-c1`, team b]
- Positions seen by the extractor (`b-sR08-f003587-q2`): into-must-consume-self
- Positions seen by the extractor (`b-sb22-f009236-q1`): bare-verb naming would be clearer and more consistent with `Clone`/`Borrow` (jvcmarcenes); the `to_`/`as_`/`into_` convention from the Rust API Guidelines is the correct, deliberate choice here (steffahn); `to_owned` is fine as-is because a bare verb like `own` would misdescribe an operation that copies into a new representation rather than "owning" anything (jrose)

### `trust-microbenchmarks`

**Question.** How far to trust microbenchmarks?

- Grouping: Same question in two sources.
- Teams: a · members (context): `a-sa25-f011413-q5` (f011413, core); `a-sa28-f012469-q1` (f012469, core)
- Domains: core
- Concepts: benchmarking methodology; floating-point precision; conference culture
- Positions:
  - `trust-microbenchmarks--distrust-by-default` — Distrust by default
    - **Amos (fasterthanlime)** · Source `f011413` · date 2026-06-11 · locator ~00:19:41–00:20:16 — his own "Canada" benchmark against serde_json is not apples-to-apples because it skips serde's precise floating-point rounding mode; he states microbenchmarks, especially conference ones given without a right of reply, should be treated as suspect by default Quote: "microbenchmarks are always lies... Canada is a lie. Not the country, the benchmark." [`a-sa25-f011413-c6`, team a]
    - **kibwen** · Source `f012469` · date 2015-06-06 · locator post by @llogiq dated 2015-06-06T16:29:42Z, sourced "on /r/rust" — declares blanket moral opposition to microbenchmarks Quote: "I'm morally opposed to microbenchmarks and think they should all be consumed by gaping fissures in the earth's crust" [`a-sa28-f012469-c1`, team a]
    - **bstrie (attribution hedged by the poster themselves: "I'm pretty sure it's @bstrie")** · Source `f012469` · date 2015-07-17 · locator post by @carols10cents dated 2015-07-17T01:06:52Z, citing "33:52 of Rusty Radio Episode 2" — benchmarks are a special category of lie, always risky to cite Quote: "I know that benchmarks are, always, generally, dangerous to quote because they're a special type of lie" [`a-sa28-f012469-c2`, team a]
- Positions seen by the extractor (`a-sa25-f011413-q5`): single position voiced in this source — "microbenchmarks are inherently misleading by default, distrust them, especially your own"; no opposing voice quoted here
- Positions seen by the extractor (`a-sa28-f012469-q1`): this source only adds further instances of "distrust microbenchmarks by default" (no opposing voice found here either)

### `unstable-feature-gate-vs-wait`

**Question.** Ship unready API behind an unstable flag, or wait?

- Grouping: Same choice in two iroh releases.
- Teams: b · members (context): `b-sR10-f004423-q2` (f004423, decentralized-iroh, distributed, core); `b-sR10-f004741-q2` (f004741, decentralized-iroh, distributed, core)
- Domains: core, decentralized-iroh, distributed
- Concepts: feature flags; API stability; semver
- Positions:
  - `unstable-feature-gate-vs-wait--ship-gated-unstable` — Ship it behind an unstable gate
    - **dignifiedquire (iroh/n0 computer)** · Source `f004423` · date 2026-03-16 · locator section "Custom Transports" / "Current status" — the custom-transport API ships now but stays behind an unstable feature flag and is declared unstable even past the 1.0 stabilization line Quote: "As the name suggests, the custom transport API is unstable and will remain so for some time even after iroh 1.0 is released." [`b-sR10-f004423-c2`, team b]
    - **Friedel Ziegelmayer & Rüdiger Klaehn (iroh/n0 computer)** · Source `f004741` · date 2026-05-27 · locator section "🛣️ Configurable path selection" — the new PathSelector trait and its types ship now but stay behind the unstable-custom-transports flag and are explicitly excluded from the 1.0 stability guarantee Quote: "The trait and the new types are gated behind the unstable-custom-transports feature. Keep in mind that this means they are not covered by the 1.0 stability guarantees and may break in future releases." [`b-sR10-f004741-c2`, team b]
- Positions seen by the extractor (`b-sR10-f004423-q2`): ship-gated-unstable
- Positions seen by the extractor (`b-sR10-f004741-q2`): ship-gated-unstable

### `wasm-components-for-interop`

**Question.** Wasm components (WIT) or language SDKs and C-ABI for interop?

- Grouping: Same interop choice.
- Absorbs merge-final ids: `agent-tools-as-wasm-components`
- Teams: a · members (context): `a-sT12-f008237-q1` (f008237, wasm, core); `a-sa07-f003922-q1` (f003922, wasm, cloud-workers, distributed)
- Domains: cloud-workers, core, distributed, wasm
- Concepts: WebAssembly component model; WIT; wit-bindgen; C ABI; FFI; composition; wasm-components; wasi; composability; mcp
- Positions:
  - `wasm-components-for-interop--wasm-components` — Wasm components
    - **author of Ideas Reifying (ideas.reify.ing; not named in the text)** · Source `f008237` · date 2026-09-22 · locator § "Compose with wasmbuilder.app", last paragraph; § "Personal Notes and Beyond WASIp2", paragraph 1 — composing components through compatible WIT interfaces relieves the pain of gluing programs through C ABIs, which the author calls fragile and dangerous as a foundation for interop Quote: "The foundation of software interops is still legacy C ABIs, which are not only fragile but also dangerous." (flag: voice-unverified (Rust connection in source: calls Rust a favorite, writes Rust guests and hosts, filed an issue in the Rust repository)) [`a-sT12-f008237-c1`, team a]
    - **Ian McDonald** · Source `f003922` · date 2025-11-25 · locator blog post, § "Wasmcp" — argues that SDK-based tool calling couples tool instances to the calling application's runtime and can't be reused externally, and that composing independently-built WebAssembly components (regardless of source language) solves discovery, portability and sandboxing better Quote: "Tool calling implemented by an AI SDK couples tool instances to an application's runtime... We need a layer of indirection between models and their tools." [`a-sa07-f003922-c1`, team a]
- Positions seen by the extractor (`a-sT12-f008237-q1`): component model over C ABI; C-ABI FFI (named as the incumbent, no Voice for it here)
- Positions seen by the extractor (`a-sa07-f003922-q1`): wasm-component-composition (Ian McDonald / wasmcp)

### `web-framework-actor-vs-tower`

**Question.** Which Rust web framework to default to: Actix (actor model) or Axum (Tower)?

- Grouping: Same framework choice; a course's "Actix by default" and a comparison favoring Axum.
- Teams: a · members (context): `a-sB01-f000149-q2` (f000149, web, cloud-workers); `a-sa26-f011605-q2` (f011605, web)
- Domains: cloud-workers, web
- Concepts: web-framework-default; CLI-framework-default; web frameworks; actor model; middleware
- Positions:
  - `web-framework-actor-vs-tower--p1` — Actix-default for web, Clap for CLI
    - **Noah Gift** · Source `f000149` · date 2023 (course release date stated in source) · locator Chapter 1, project spec bullet on frameworks — Directs students to default to Clap (CLI) and Actix (web) "unless you have a compelling reason to switch to a new framework" Quote: "unless you have a compelling reason to switch to a new framework" [`a-sB01-f000149-c2`, team a]
  - `web-framework-actor-vs-tower--p2` — Axum's Tower-based design is often preferred over Actix Web's actor model
    - **Joshua Mo** · Source `f011605` · date 2023-12-06 (updated 2025-07-04) · locator FAQ "What is the difference between Axum and Actix Web?" — both frameworks are fast and production-ready, but Axum's simplicity and tight Tokio integration is "often preferred" over Actix Web's actor-model design Quote: "Actix Web uses the actor model and has its own mature middleware system. Both are fast and production-ready, but Axum's design philosophy is often preferred for its simplicity and tight integration with Tokio" [`a-sa26-f011605-c2`, team a]
- Positions seen by the extractor (`a-sB01-f000149-q2`): Actix-default (with Clap for CLI)
- Positions seen by the extractor (`a-sa26-f011605-q2`): Tower-Service/Layer-model-often-preferred-for-simplicity (Joshua Mo, re: Axum vs Actix Web)

### `absolute-instant-periodic-timing`

**Question.** For repeated/periodic timing in async embedded Rust, should each wait be computed from an accumulating absolute instant, or from a fresh relative delay each iteration?

- Teams: a · members (context): `a-sB04-f000227-q2` (f000227, embedded)
- Domains: embedded
- Concepts: absolute-instant-scheduling; relative-delay-drift; Mono::delay_until
- Positions:
  - `absolute-instant-periodic-timing--p1` — accumulate-absolute-instant-to-avoid-drift
    - **RTIC developers** · Source `f000227` · date undated (living doc, v2.x) · locator "2.8. Delay and Timeout using Monotonics" — Recommends incrementing a stored absolute instant and calling delay_until against it, instead of delaying by a fresh relative duration each loop iteration, because relative delays accumulate drift from the work done each iteration Quote: "Any additional delays incurred as we iterate around this loop are compensated for by delaying until 'previous + 1000' as opposed to 'now + 1000' (which would cause our loop timing to drift)." [`a-sB04-f000227-c2`, team a]
- Positions seen by the extractor (`a-sB04-f000227-q2`): accumulate-absolute-instant-to-avoid-drift

### `actor-vs-shared-locks`

**Question.** In an async networking server, should connection management go through an actor or through shared data structures with locks?

- Teams: b · members (context): `b-sT05-f002550-q2` (f002550, decentralized-iroh, distributed)
- Domains: decentralized-iroh, distributed
- Concepts: actor pattern; Mutex/locks; deadlock risk
- Positions:
  - `actor-vs-shared-locks--p1` — remove the actor; use lock-based data structures
    - **ramfox, matheus23** · Source `f002550` · date 2025-01-15 · locator § Deadlock on the relay (not released) — refactor removed "an unnecessary actor" to cut layers, then needed a follow-up to fix a deadlock Quote: "removing an unnecessary actor and using some higher-order data structures" (flag: voice-unverified) [`b-sT05-f002550-c2`, team b]
- Positions seen by the extractor (`b-sT05-f002550-q2`): remove actor, use higher-order lock-based structures (with a deadlock follow-up)

### `ad-hoc-special-case-vs-general-mechanism`

**Question.** When migrating a compiler backend to a new, more systematic instruction-assembler abstraction, and an instruction needs special-cased handling (e.g. custom flag-setting/printing) that the new abstraction doesn't yet cleanly support, should the PR merge the ad hoc special case now or block on designing the general mechanism first?

- Teams: b · members (context): `b-sb09-f003052-q1` (f003052, wasm, core)
- Domains: core, wasm
- Concepts: compiler backend migration; instruction encoding abstraction; technical debt sequencing
- Positions:
  - `ad-hoc-special-case-vs-general-mechanism--p1` — resist-ad-hoc-design-general-solution-first
    - **abrown** · Source `f003052` · date 2025-05-28 · locator comment @abrown 2025-05-28T17:56:16Z — objects to adding another special-cased "custom" printing mechanism for compare instructions' flags, noting the existing `lock_` special case was already unfortunate, and argues for a better long-term solution before merging. Quote: "I'm not a big fan of this; the `lock_` stuff below already seemed unfortunate but now this opens a whole new can of worms... I just think we should think through a better long-term solution." [`b-sb09-f003052-c1`, team b]
  - `ad-hoc-special-case-vs-general-mechanism--p2` — merge-as-is-and-refactor-later
    - **abrown** · Source `f003052` · date 2025-06-02 · locator comment @abrown 2025-06-02T17:48:01Z — shifts to accepting the current approach for now, deferring the cleanup to a follow-up refactor building on a separate "custom" logic PR by another contributor. Quote: "Ok, let's leave this as-is for now but we'll need to refactor to something more like the `custom` logic introduced by @alexcrichton..." [`b-sb09-f003052-c2`, team b]
    - **rahulchaphalkar** · Source `f003052` · date 2025-06-03 · locator comment @rahulchaphalkar 2025-06-03T16:18:30Z — agrees to sequence the work by letting the external-printing refactor PR land first and rebasing this PR on top of it, rather than blocking this PR on redesigning the mechanism inline. Quote: "I agree with the idea that lets push the external printing patch first, and then rebase on that." [`b-sb09-f003052-c3`, team b]
- Positions seen by the extractor (`b-sb09-f003052-q1`): resist-ad-hoc-design-general-solution-first (abrown, initial), merge-as-is-and-refactor-later (abrown, revised; rahulchaphalkar)

### `additive-features`

**Question.** Should a crate's Cargo feature flags always be strictly additive (the crate builds with any subset of features, including none), or is it acceptable for disabling a feature (like `std`) to change what builds successfully on certain targets?

- Teams: b · members (context): `b-sb10-f003186-q1` (f003186, core, embedded)
- Domains: core, embedded
- Concepts: Cargo feature flags; additive features; no_std support
- Positions:
  - `additive-features--p1` — features-must-stay-additive
    - **alexcrichton** · Source `f003186` · date 2025-06-30 · locator comment 2025-06-30T18:19:37Z — the `std` feature should not be required just to build the crate on Linux/Windows targets; requiring it defeats the point of feature gating Quote: "the `std` feature should not be necessary to just build the crate, even on Linux/Windows targets. In essence these CI changes shouldn't be necessary." [`b-sb10-f003186-c1`, team b]
  - `additive-features--p2` — disabling-a-feature-can-change-buildability
    - **salmans** · Source `f003186` · date 2025-06-27 · locator PR description, 2025-06-27T21:18:19Z — the fix intentionally disables standard-library-dependent features for dependents using `default-features = false`, changing what builds under that configuration Quote: "This fix will disable standard library features for dependents that use wasmtime with `default-features = false`." [`b-sb10-f003186-c2`, team b]
- Positions seen by the extractor (`b-sb10-f003186-q1`): features-must-stay-additive (alexcrichton), disabling-a-feature-can-change-buildability (salmans, initial PR)

### `affine-types-vs-formal-verification`

**Question.** Does Rust's affine-type system provide sufficient correctness guarantees, or is further formal verification (linear/dependent types, model checkers) needed on top of it?

- Teams: b · members (context): `b-sb19-f005743-q2` (f005743, core)
- Domains: core
- Concepts: affine types; linear types; dependent types; Frama-C; TrustInSoft
- Positions:
  - `affine-types-vs-formal-verification--p1` — needs-stronger-formal-guarantees
    - **toastal** · Source `f005743` · date 2026-06-02 · locator comment at 2026-06-02T12:14:03-05:00 — Rust's affine types are weaker than linear+dependent type guarantees Quote: "Affine types do not offer the same guarantees as linear types + dependent types." [`b-sb19-f005743-c4`, team b]
    - **madhadron** · Source `f005743` · date 2026-06-02 · locator comment at 2026-06-02T12:39:44-05:00 — proposes integrated model checkers (e.g. Frama-C) as the stronger alternative/complement to a type system Quote: "Or we could insist on something like Frama C or other model checkers integrated in." [`b-sb19-f005743-c5`, team b]
  - `affine-types-vs-formal-verification--p2` — combine-rust-with-formal-tools
    - **wucke13** · Source `f005743` · date 2026-06-05 · locator comment at 2026-06-05T04:25:37-05:00 — formal-verification tooling (TrustInSoft's Frama-C port) can sit alongside Rust rather than replace it Quote: "I believe TrustInSoft offers a Frama C port to Rust, so, not mutually exclusive with the use of Rust!" [`b-sb19-f005743-c6`, team b]
- Positions seen by the extractor (`b-sb19-f005743-q2`): needs-stronger-formal-guarantees (toastal, madhadron), combine-rust-with-formal-tools (wucke13)

### `ai-agents-and-explicit-syntax`

**Question.** Does the rise of AI coding agents change the cost/benefit calculus for verbose, explicit call-site syntax (like named arguments) that was previously judged not worth its typing cost for human authors?

- Teams: a · members (context): `a-sa18-f009104-q2` (f009104, core)
- Domains: core
- Concepts: ai-assisted-rust; api-ergonomics; agent-readability
- Positions:
  - `ai-agents-and-explicit-syntax--p1` — agents-shift-calculus-toward-explicit-named-syntax
    - **Steve Klabnik** · Source `f009104` · date 2026-09-21 · locator "I'm okay with named parameters now" section — attributes his change of mind to coding agents — since he is "not typing myself anymore," the verbosity cost of named arguments no longer weighs against their call-site clarity benefit, and reasons the clarity gain is if anything larger for an agent reading the call site than for a human, while explicitly noting he hasn't run real evals on this Quote: "what changed my opinion is coding agents, actually... 'What's good for humans is true for agents' strikes again." [`a-sa18-f009104-c3`, team a]
- Positions seen by the extractor (`a-sa18-f009104-q2`): agents-shift-calculus-toward-explicit-named-syntax

### `ai-review-suggestions`

**Question.** Should a Rust practitioner follow an AI code-review tool's suggestions by default, or evaluate them critically before acting?

- Teams: b · members (context): `b-sR08-f003550-q1` (f003550, ml)
- Domains: ml
- Concepts: AI-assisted Rust; code review; tooling trust
- Positions:
  - `ai-review-suggestions--p1` — critically-evaluate-not-blindly-follow
    - **laggui** · Source `f003550` · date 2025-09-19 · locator PR #3743, review comment 2025-09-19T19:54:02Z — dismisses a Copilot review comment telling the author to avoid `&3` as unnecessary noise (passing a reference to a literal is fine), and redirects attention to a real bug the AI reviewer missed — an unsupported vectorization size on some cubecl backends. Quote: "You didn't need to follow Copilot's advice here 😄 passing &3 is fine." [`b-sR08-f003550-c1`, team b]
- Positions seen by the extractor (`b-sR08-f003550-q1`): critically-evaluate-not-blindly-follow

### `api-handler-as-async-trait`

**Question.** Should an HTTP API's handler signature be defined using an async trait decoupled from any concrete implementation, so tooling can extract API/schema information without compiling a real implementation?

- Teams: a · members (context): `a-sa14-f005454-q3` (f005454, web)
- Domains: web
- Concepts: async traits; API metadata extraction; trait-based API definition
- Positions:
  - `api-handler-as-async-trait--p1` — define API endpoints via async traits decoupled from implementation
    - **sunshowers** · Source `f005454` · date 2025-02-24 · locator comment 2025-02-24T16:37:04 — describes contributing async-trait-based API definitions to Dropshot shortly after async traits stabilized, noting the value is extracting API information without needing a concrete implementation compiled or even present Quote: "I hope Rust projects more generally adopt this pattern, since it helps extract API information without needing to compile (or even have) a concrete implementation at hand." [`a-sa14-f005454-c3`, team a]
- Positions seen by the extractor (`a-sa14-f005454-q3`): yes — define endpoints via async traits specifically so API/schema information can be extracted without needing to compile, or even have, a concrete implementation on hand

### `async-by-default-host-interfaces`

**Question.** Should a framework's host/runtime interfaces be async by default, or should async stay an opt-in path alongside a synchronous default?

- Teams: b · members (context): `b-sR10-f004809-q1` (f004809, wasm, cloud-workers, web)
- Domains: cloud-workers, wasm, web
- Concepts: async runtimes; concurrency model
- Positions:
  - `async-by-default-host-interfaces--p1` — async-by-default
    - **The Spin Project (Fermyon / CNCF Spin, institution)** · Source `f004809` · date 2026-06-15 · locator sections "WASI Preview 3: stabilized and supported long-term" / "Async everywhere: Spin's host interfaces are now async" — WASIp3's async model, previously experimental and opt-in, is now the default for new applications, and Spin's own host interfaces (KV, SQLite, Postgres, Redis, outbound HTTP) were rewritten to be async so handlers get real concurrency instead of blocking Quote: "WASIp3 is now the default platform for new applications... we've asyncified Spin's host interfaces so I/O-heavy handlers actually get concurrency instead of blocking the instance." [`b-sR10-f004809-c1`, team b]
- Positions seen by the extractor (`b-sR10-f004809-q1`): async-by-default

### `async-fn-in-traits-cost`

**Question.** Should you use `async fn` in traits (via the `async-trait` crate or async-fn-in-trait) given its cost?

- Teams: b · members (context): `b-bk01-f000233-q13` (f000233, core, web)
- Domains: core, web
- Concepts: async traits; async-trait; heap allocation
- Positions:
  - `async-fn-in-traits-cost--p1` — acceptable for most applications; avoid in hot low-level public APIs
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "Workarounds to Know and Love" § async in Traits — using async fn in traits (via the async-trait crate on stable, or async-fn-in-trait on nightly) costs a heap allocation per function call; calls this not a significant cost for the vast majority of applications, but says it should be weighed when deciding whether to expose the functionality in the public API of a low-level function expected to be called millions of times a second. Quote: "should be considered when deciding whether to use this functionality in the public API of a low-level function that is expected to be called millions of times a second." [`b-bk01-f000233-c14`, team b]
- Positions seen by the extractor (`b-bk01-f000233-q13`): acceptable for most applications; avoid in low-level, extremely hot public APIs

### `async-for-cpu-bound-work`

**Question.** Is async Rust (e.g. Tokio) an appropriate choice for CPU-intensive work?

- Teams: b · members (context): `b-bk01-f000233-q5` (f000233, core, ml, distributed)
- Domains: core, distributed, ml
- Concepts: blocking; CPU-bound work; runtime scheduling
- Positions:
  - `async-for-cpu-bound-work--p1` — qualified yes, against the "never use async for CPU work" meme
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "IO and issues with blocking" § CPU-intensive work — explicitly rejects the common claim that async Rust/Tokio should never be used for CPU-intensive work as an over-simplification; the real constraint is that mixing IO-bound/latency-sensitive tasks with CPU-bound/long-running tasks needs special handling, not avoidance of async altogether. Quote: "There is a meme that you should simply not use async Rust ... for CPU-intensive work, but that is an over-simplification." [`b-bk01-f000233-c6`, team b]
- Positions seen by the extractor (`b-bk01-f000233-q5`): qualified yes, against a "never use async for CPU work" meme

### `async-hook-cancellation-upfront`

**Question.** When designing an async-computation hook API, should cancellation semantics be committed to upfront even at the cost of a larger initial API surface, or postponed until real usage demonstrates the need?

- Teams: a · members (context): `a-02-f000957-q1` (f000957, frontend)
- Domains: frontend
- Concepts: async hooks; API stability; premature generality
- Positions:
  - `async-hook-cancellation-upfront--p1` — ship-minimal-now
    - **Ekleog** · Source `f000957` · date 2024-02-20 · locator PR description — argues the initial `use_async` hook should ship without baking in cancellation semantics, since Yew isn't stable yet and the design likely covers ~90% of use cases; cancellation can be added later as a variant if real need emerges Quote: "Yew is not stable yet, and probably at least 90% of the use cases are covered by this API, so I think it makes sense to postpone the decision after verifying that there is an actual need." [`a-02-f000957-c1`, team a]
- Positions seen by the extractor (`a-02-f000957-q1`): ship-minimal-now (author), commit-upfront (implicit alternative the author argues against)

### `async-io-with-sync-storage`

**Question.** When your chosen async I/O library (e.g. quinn for QUIC) is paired with a storage/database layer that only offers a synchronous API (as with embedded databases like redb, rocksdb, sled, sqlite), should you treat that combination as an avoidable architecture mismatch to design around from the outset — including avoiding constructs like `LocalSet` and `!Send` futures — or accept it as a practical necessity, since no viable async-native alternative exists and non-`Send` futures are often unavoidable when wrapping such resources?

- Teams: b · members (context): `b-sb18-f005307-q1` (f005307, distributed, decentralized-iroh)
- Domains: decentralized-iroh, distributed
- Concepts: async runtimes; sync/blocking I/O; embedded storage engines; Send bounds; LocalSet
- Positions:
  - `async-io-with-sync-storage--p1` — incompatible-deps-should-be-avoided
    - **withoutboats** · Source `f005307` · date 2024-08-02 · locator lobste.rs/s/7rtvnp, comment 2024-08-02T06:30:40-05:00 — argues iroh's choice of quinn (async QUIC) together with redb (blocking storage) creates the impedance mismatch that is the source of many of their described problems, and separately that `LocalSet` and `FuturesUnordered` should generally be avoided Quote: "I would have regarded quinn and redb as incompatible dependencies because of this mismatch and looked for a different solution." [`b-sb18-f005307-c1`, team b]
  - `async-io-with-sync-storage--p2` — sync-storage-is-unavoidable-given-available-options
    - **rklaehn** · Source `f005307` · date 2024-08-06 · locator lobste.rs/s/7rtvnp, comment 2024-08-06T06:41:54-05:00 — as the blog post's author and an iroh maintainer, responds "what is the alternative?" — every in-process database they evaluated (rocksdb, redb, sled, sqlite) has a synchronous API, so the mismatch isn't a foreseeable design error, and non-`Send` futures are often unavoidable when a future must capture a non-`Send` database/transaction handle Quote: "What is the alternative? ... They *all* have a sync api." [`b-sb18-f005307-c2`, team b]
- Positions seen by the extractor (`b-sb18-f005307-q1`): incompatible-deps-should-be-avoided, sync-storage-is-unavoidable-given-available-options

### `async-rust-production-ready`

**Question.** Is async Rust production-ready today given its known gaps?

- Teams: b · members (context): `b-sR01-f000233-q2` (f000233, core)
- Domains: core
- Concepts: async runtimes; async traits; streams; async destructors
- Positions:
  - `async-rust-production-ready--p1` — reliable-despite-rough-edges
    - **Rust Async Book (async-book, rust-lang.github.io)** · Source `f000233` · date undated (living document) · locator § "Development of Async Rust", paragraph 1 — stable async is reliable and performant and used in production at large tech companies, though ergonomics (not reliability) are rough around async iterators/streams, async in traits, and async destruction. Quote: "Async Rust ... is reliable and performant. It is used in production in some of the most demanding situations at the largest tech companies." [`b-sR01-f000233-c2`, team b]
- Positions seen by the extractor (`b-sR01-f000233-q2`): reliable-despite-rough-edges

### `async-transport-asyncread-vs-sink-stream`

**Question.** For a custom async I/O transport abstraction in Rust that must work across several carriers (raw TCP, TLS, WebSocket-wrapped tunnel), should the abstraction be built against the tokio-style `AsyncRead`/`AsyncWrite` traits, or against the `Sink`/`Stream` traits that most existing async WebSocket libraries expose?

- Teams: a · members (context): `a-sa03-f002236-q1` (f002236, cloud-workers)
- Domains: cloud-workers
- Concepts: `AsyncRead`/`AsyncWrite` vs. `Sink`/`Stream` traits; `Send`/`Sync`/`Unpin` bounds; generic transport abstraction; tokio ecosystem
- Positions:
  - `async-transport-asyncread-vs-sink-stream--p1` — build the transport abstraction against `AsyncRead`/`AsyncWrite`, not `Sink`/`Stream`
    - **Cloudflare (Hyperdrive team)** · Source `f002236` · date 2024-10-25 · locator article body, "The way we accomplish this..." section — States that available OSS WebSocket-over-async libraries built on `Sink`/`Stream` did not jointly satisfy `Send`, `Sync`, `Unpin` together with `AsyncRead`/`AsyncWrite`, so Hyperdrive wrote its own translation layer to keep its entire custom Postgres handler generic over `AsyncRead`/`AsyncWrite` streams instead. Quote: "The primary reason is that Hyperdrive operates across multiple threads (thanks to the tokio runtime), and so we rely on our connections to also handle Send, Sync, and Unpin. None of the available solutions had all five traits handled." [`a-sa03-f002236-c1`, team a]
- Positions seen by the extractor (`a-sa03-f002236-q1`): Cloudflare (Hyperdrive team) — standardize the whole handler on `AsyncRead`/`AsyncWrite` and write a custom WebSocket-to-`AsyncRead`/`AsyncWrite` translation layer; existing OSS WebSocket-over-async libraries (unnamed) — built on the `Sink`/`Stream` paradigm instead

### `aya-vs-libbpf-rs`

**Question.** For writing eBPF programs from Rust, should you use a pure-Rust implementation with no libbpf/BCC dependency (Aya), or a Rust wrapper around the native C `libbpf` library with the eBPF program itself written in C (libbpf-rs)?

- Teams: b · members (context): `b-sb24-f011306-q2` (f011306, core)
- Domains: core
- Concepts: Aya; libbpf-rs; BCC; kernel-space vs user-space program split
- Positions:
  - `aya-vs-libbpf-rs--p1` — no-strong-preference-used-libbpf-rs-for-familiarity
    - **Lalit Basin** · Source `f011306` · date 2025-10-03 · locator [19:32]-[20:34] — Aya is pure Rust for both the kernel-space and user-space program with only experimental CO-RE support and no libbpf/BCC/kernel-header dependency; libbpf-rs wraps the C libbpf library, so the eBPF program is written in C/compiled with clang+LLVM while the user-space program is Rust, with CO-RE supported by default; he used libbpf-rs for the talk's examples "for no specific reason" Quote: "most of the examples which I'm going to talk here would be lib BPF using libf BPF RS for no specific reasons uh I know that there are I maintainers and developers probably sitting somewhere in the audience don't please don't judge me you guys are doing the awesome job" [`b-sb24-f011306-c2`, team b]
- Positions seen by the extractor (`b-sb24-f011306-q2`): no-strong-preference-used-libbpf-rs-for-familiarity (Lalit Basin)

### `batch-crypto-verification`

**Question.** Should CPU-bound cryptographic verification in an async Rust service be batched for throughput?

- Teams: b · members (context): `b-bk03-f000267-q5` (f000267, distributed, core)
- Domains: core, distributed
- Concepts: batch processing; tower-batch-control; async verification
- Positions:
  - `batch-crypto-verification--p1` — batch-verify-for-throughput
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Design Overview § zebra-consensus; Parallel Verification RFC § Summary — zebra-consensus uses the tower-batch-control crate to automatically and transparently batch contemporaneous signature/proof verification requests, rather than verifying each request independently; the Parallel Verification RFC gives the reason directly — serial, one-block-at-a-time verification (as in zcashd) is too slow during initial sync, so Zebra defers data dependencies and batches signature/proof/script verification to parallelize it Quote: "perform automatic, transparent batch processing of contemporaneous verification requests" (flag: voice-unverified) [`b-bk03-f000267-c5`, team b]
- Positions seen by the extractor (`b-bk03-f000267-q5`): batch-verify-for-throughput

### `batteries-included-web-framework`

**Question.** Should a Rust backend use an opinionated batteries-included framework (Rails/Django/Spring-style), or compose libraries such as axum and sqlx directly?

- Grouping: Same framework choice; b-sT09-f005314-q1 lost its Claim to a re-home and is removed as a capture.
- Teams: b · members (context): `b-sb19-f005872-q1` (f005872, web)
- Domains: web
- Concepts: web framework scope; actix-web; axum; Leptos; Yew; Dioxus; "wire it up yourself"
- Positions:
  - `batteries-included-web-framework--batteries-included` — Use or build a convention-over-configuration, batteries-included framework
    - **Nicole Tietz-Sokolskaya** · Source `f005872` · date 2024-10-02 · locator § "Imagining the future I want" — existing minimalist frameworks (actix-web, axum) and SPA frameworks (Yew, Leptos, Dioxus) each require substantial manual wiring (routing, templates, auth, DB, admin, etc.); the ecosystem needs one integrated toolkit instead, which she is starting to build ("newt") Quote: "I'd much rather have a single web framework that handles it all, with clean upgrade instructions between versions." [`b-sb19-f005872-c1`, team b]
- Positions seen by the extractor (`b-sb19-f005872-q1`): needs-batteries-included-framework (Nicole Tietz-Sokolskaya)

### `become-tail-call-codegen`

**Question.** Does Rust's nightly `become` tail-call feature produce reliably good codegen across targets, or is it currently good on some architectures and poor on others?

- Teams: a · members (context): `a-sa15-f005821-q1` (f005821, core, wasm)
- Domains: core, wasm
- Concepts: tail-calls; nightly-features; codegen; LLVM; calling-conventions; WebAssembly
- Positions:
  - `become-tail-call-codegen--p1` — strong-win-on-arm64
    - **Matt Keeter** · Source `f005821` · date 2026-04-05 · locator "Performance results" section, ARM64 and x86-64 benchmark tables plus WASM benchmark table — on ARM64 (M1) the tail-call interpreter beats both the plain VM and Keeter's own hand-written ARM64 assembly; on x86-64 it beats the VM but still loses to hand-written assembly; compiled to WASM it is 1.2–4.6x slower than the plain VM across Firefox, Chrome and wasmtime, which he attributes to the codegen (register spills to the stack) not translating well to the WASM stack machine Quote: "the tail-call interpreter handily beats my hand-written assembly on both benchmarks" (ARM64); "oh no... it's outperforming the VM, but is still losing to the assembly backend" (x86-64) [`a-sa15-f005821-c1`, team a]
- Positions seen by the extractor (`a-sa15-f005821-q1`): strong-win-on-arm64, poor-inconsistent-elsewhere

### `behavioral-equivalence-testing-method`

**Question.** For verifying that a rewritten/ported system stays behaviorally equivalent to the original when correct behavior includes emergent, hard-to-specify effects (e.g. a physics-engine exploit), should you rely on unit/integration tests, naive property-based (fuzzing) testing, or a heuristic-guided reinforcement-learning search?

- Teams: a · members (context): `a-sa21-f011069-q1` (f011069, ml, other)
- Domains: ml, other
- Concepts: testing methodologies; property-based testing; reinforcement learning; fuzzing
- Positions:
  - `behavioral-equivalence-testing-method--p1` — unit-and-integration-tests-insufficient
    - **Aleksandr Petrosyan** · Source `f011069` · date 2023-11-15 · locator ~00:14:50-00:18:00 ("So, unit testing?... Wrong again.") — Rejects both unit tests and integration tests for verifying his DarkPlaces-to-Rust physics port preserves an emergent exploit (strafe-jumping): the divergence only shows up late in long play sessions, no fixed tolerance works everywhere, and a single integration test's result can't be extrapolated to the whole game. Quote: "The simple solution is usually right, right? Well, no." [`a-sa21-f011069-c1`, team a]
  - `behavioral-equivalence-testing-method--p2` — naive-property-based-testing-insufficient
    - **Aleksandr Petrosyan** · Source `f011069` · date 2023-11-15 · locator ~00:18:50-00:20:30 (discussing Hypothesis and Rust's PropTest) — Found property-based testing inadequate alone because the input space (keyboard holds, frame counts, continuous mouse movement) grows exponentially, and pure random search produces inputs "a human would not even be capable of producing," giving many false negatives against his goal of preserving a human-discoverable exploit; notes Rust has PropTest but he didn't use it. Quote: "checking all possible values and finding regressions is the right path, but the fuzziness, the way in which it was introduced in property-based testing is inherently random." [`a-sa21-f011069-c2`, team a]
  - `behavioral-equivalence-testing-method--p3` — heuristic-guided-rl-search-preferred
    - **Aleksandr Petrosyan** · Source `f011069` · date 2023-11-15 · locator ~00:20:30-00:23:00 — Concludes the right approach is a heuristic-constrained ("tame," Markov-process) reinforcement-learning-style search biased toward human-plausible inputs, rather than fixed test cases or unconstrained fuzzing — treating "the exploit stays reachable within human-plausible effort" as the correctness criterion instead of exact input/output matching; implemented with the Rurel crate. Quote: "we want to have a Markov process, which should hint to you that we're talking about reinforcement learning at some point." [`a-sa21-f011069-c3`, team a]
- Positions seen by the extractor (`a-sa21-f011069-q1`): unit-and-integration-tests-insufficient, naive-property-based-testing-insufficient, heuristic-guided-rl-search-preferred

### `benchmark-colocation-with-crate`

**Question.** When a function moves to a different crate in a multi-crate Rust workspace, should its benchmark move with it, using `git mv` to preserve file history?

- Teams: a · members (context): `a-sR04-f001096-q2` (f001096, ml, core)
- Domains: core, ml
- Concepts: workspace/crate organization; benchmarks; git history
- Positions:
  - `benchmark-colocation-with-crate--p1` — colocate-benchmark-with-owning-crate
    - **LaurentMazare** · Source `f001096` · date 2025-01-13 · locator comment "I think moving the benchmark to `candle-nn` would be good, (do it with `git mv` so as to preserve history)." — a benchmark should live in the crate that defines the function it measures; use `git mv` on relocation to preserve file history Quote: "I think moving the benchmark to `candle-nn` would be good, (do it with `git mv` so as to preserve history)." [`a-sR04-f001096-c2`, team a]
- Positions seen by the extractor (`a-sR04-f001096-q2`): colocate-benchmark-with-owning-crate

### `bitflags-vs-generated-variants`

**Question.** Should combinatorial pipeline state be represented as an explicit generated array/struct of bool-driven variants, or as bitflags with named constants?

- Teams: b · members (context): `b-sb01-f000493-q1` (f000493, core)
- Domains: core
- Concepts: bitflags; enums; combinatorial state; macros
- Positions:
  - `bitflags-vs-generated-variants--p1` — bitflags-preferred
    - **superdump** · Source `f000493` · date 2023-10-17 · locator PR #10156, 2nd comment — the bool-per-combination approach used here "felt a bit off"; bit flags can generate combinations procedurally, take less space, and are arguably clearer with named constants (citing the bitflag crate) Quote: "Bit flags take a lot less space, and are arguably clearer when using named constants like the bitflag crate offers." [`b-sb01-f000493-c1`, team b]
  - `bitflags-vs-generated-variants--p2` — explicit-array-generation
    - **coreh** · Source `f000493` · date 2023-10-17 · locator PR #10156, 3rd comment — the two approaches are mostly the same in principle, but with 32 combinations here versus 6 in the prior PR, enumerating by hand is more daunting, which is why the code generates the array instead Quote: "The amount of combinations here (32) makes this a little bit more daunting to fully enumerate like that (6) which is why I added the code to generate it in an array." [`b-sb01-f000493-c2`, team b]
- Positions seen by the extractor (`b-sb01-f000493-q1`): bitflags-preferred, explicit-array-generation

### `blocking-work-in-async`

**Question.** How should CPU-bound or blocking work be integrated into an async program?

- Teams: b · members (context): `b-bk01-f000233-q6` (f000233, core, distributed, ml)
- Domains: core, distributed, ml
- Concepts: spawn_blocking; dedicated thread; second runtime; Rayon
- Positions:
  - `blocking-work-in-async--p1` — match mechanism to work shape
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "IO and issues with blocking" § Other blocking operations — gives a decision rule: use `spawn_blocking` for blocking IO; use `std::thread::spawn` (not a thread-pool slot) for a thread that will run forever; use a dedicated thread pool (e.g. Rayon) or a second async runtime for sustained CPU-bound work; accepts a dedicated thread or spawn_blocking as an easy-but-suboptimal choice when performance needs are modest. Quote: "If you're doing blocking IO, you should probably use spawn_blocking. ... If you have a thread that will run forever, you should use std::thread::spawn rather than use any kind of thread pool" [`b-bk01-f000233-c7`, team b]
- Positions seen by the extractor (`b-bk01-f000233-q6`): match mechanism to work shape (spawn_blocking for bounded blocking work, dedicated thread for indefinite blocking work, thread pool/second runtime for sustained CPU work)

### `borrowck-self-referential-structs`

**Question.** Should Rust's borrow checker be extended to natively support safe self-referential structs, instead of requiring `unsafe`/`Pin`/crates like `ouroboros`?

- Teams: b · members (context): `b-sb19-f007207-q3` (f007207, core)
- Domains: core
- Concepts: self-referential structs; Pin; borrow checker; async state machines
- Positions:
  - `borrowck-self-referential-structs--p1` — extend-borrow-checker
    - **Jimmy Hartzell** · Source `f007207` · date 2025-07-21 · locator § "Self-Referential Structs: Absolutely." — a subset of self-referential structs (borrowing only from a heap allocation owned by a sibling field, without mutating it) could be proven safe by a smarter borrow checker without needing `Pin`; he wants this more than fields-in-traits because he hits the need for it regularly Quote: "Self-Referential Structs: Absolutely... I think it'll be the type of feature where we'll wonder how we ever lived without it." [`b-sb19-f007207-c3`, team b]
- Positions seen by the extractor (`b-sb19-f007207-q3`): extend-borrow-checker (Jimmy Hartzell)

### `borrowed-build-state-vs-builder`

**Question.** Should a struct under construction hold a lifetime-bound reference into shared mutable build state, or should construction use a builder consumed into an immutable owned structure?

- Teams: a · members (context): `a-sa07-f003704-q4` (f003704, ml, core)
- Domains: core, ml
- Concepts: lifetimes; builder-pattern; ownership
- Positions:
  - `borrowed-build-state-vs-builder--p1` — builder-consume-to-immutable
    - **laggui** · Source `f003704` · date 2025-11-03 · locator PR #3872, comment 2025-11-03T20:17:51Z — calls the current reliance on `_graph_data` a lifetime hack and proposes a builder that consumes GraphState into an immutable OnnxGraph so Argument can reference the tensor store directly Quote: "The reliance on `_graph_data` here feels like a lifetime hack." [`a-sa07-f003704-c4`, team a]
- Positions seen by the extractor (`a-sa07-f003704-q4`): builder-consume-to-immutable (laggui, proposed)

### `boxed-closure-tuple-vs-named-field`

**Question.** When a public API wraps a `Box<dyn Fn>` behind a required constructor function, should the wrapped closure live in an unnamed tuple-struct field or a named field, given that a constructor already replaces the field's main ergonomic argument (avoiding `Box::new` at call sites)?

- Teams: b · members (context): `b-sb14-f004398-q1` (f004398, core)
- Domains: core
- Concepts: trait objects; tuple structs vs. named structs; API ergonomics for newcomers
- Positions:
  - `boxed-closure-tuple-vs-named-field--p1` — tuple-struct-with-constructor
    - **chescock** · Source `f004398` · date 2026-03-11 · locator comment @chescock 2026-03-11T19:12:28Z — suggests storing the predicate as `Box<dyn Fn(&S) -> bool>` in a public tuple-struct field so stateful closures (e.g. capturing a level number) can be used, noting `Box` won't allocate for non-capturing closures. Quote: "It might be useful to let this be used with closures that capture values, like `GameState::Level(level_number)` instead of hard-coded `2`." [`b-sb14-f004398-c1`, team b]
  - `boxed-closure-tuple-vs-named-field--p2` — avoid-trait-objects-in-public-field
    - **Freyja-moth** · Source `f004398` · date 2026-03-11 · locator comment @Freyja-moth 2026-03-11T20:24:35Z — explains the original design avoided exposing the trait object directly so users wouldn't need to write `Box::new` at every call site. Quote: "I'd chosen to stay away from trait objects so that users didn't need to write `Box::new` everywhere." [`b-sb14-f004398-c2`, team b]
  - `boxed-closure-tuple-vs-named-field--p3` — constructor-function-mitigates-boxing-friction
    - **chescock** · Source `f004398` · date 2026-03-11 · locator comment @chescock 2026-03-11T20:53:19Z — proposes a `new` constructor that performs the boxing internally, so the type keeps the `Box<dyn Fn>` representation while call sites just write `DespawnOnExitWith::new(|state| ...)`. Quote: "one way to mitigate it would be with a constructor function... and then it's just `DespawnOnExitWith::new(|state| true)`." [`b-sb14-f004398-c3`, team b]
  - `boxed-closure-tuple-vs-named-field--p4` — named-field-for-clarity
    - **alice-i-cecile** · Source `f004398` · date 2026-03-12 · locator comment @alice-i-cecile 2026-03-12T19:51:53Z — once a constructor is already required to do the boxing, argues the type should be a one-field named struct rather than a tuple struct, since a boxed function's meaning is unclear to Rust newcomers from a bare tuple field. Quote: "The \"stores a boxed function\" is quite tricky for folks who are newer to Rust, so I want to try to optimize clarity. We're already relying on a `new` constructor to do the boxing, so the main benefit of tuple structs is lost." [`b-sb14-f004398-c4`, team b]
- Positions seen by the extractor (`b-sb14-f004398-q1`): tuple-struct-with-constructor (chescock, Freyja-moth's initial design), named-field-for-clarity (alice-i-cecile)

### `boxed-vs-hand-written-future`

**Question.** when a tower `Service::call` needs to inspect or transform the response after the inner future resolves, should its associated `Future` be a boxed dynamic future (`Pin<Box<dyn Future<...> + Send>>`, built with `Box::pin(async move {...})`), or a hand-written `poll`-driven future struct (via `pin-project`) that avoids the heap allocation?

- Teams: b · members (context): `b-sb22-f008906-q2` (f008906, core, cloud-workers)
- Domains: cloud-workers, core
- Concepts: async trait limitations (AFIT); dynamic dispatch; Pin/Box; zero-cost futures
- Positions:
  - `boxed-vs-hand-written-future--p1` — prefer `Box::pin(async move {...})` (one heap allocation per request) over a hand-rolled `poll`-based future struct for middleware that needs post-response work, given Lambda's cost profile
    - **Luciano Mammino** · Source `f008906` · date 2026-05-03 · locator section "What did we trade?" — a hand-rolled `LogFuture<F>` with `pin-project` avoids all per-request heap allocation at the cost of ~30 extra lines, an extra struct, and a new dependency; in Lambda that allocation "is irrelevant," so the boxed-async shape is the idiomatic default, and hand-rolling is reserved for a tight loop on a busy server Quote: "Down: zero heap allocations per request... In Lambda, that is irrelevant. In a tight loop on a busy server, it can matter." [`b-sb22-f008906-c2`, team b]
- Positions seen by the extractor (`b-sb22-f008906-q2`): box it — the one allocation per request is negligible in Lambda and the ergonomic win is worth it; reach for the hand-rolled poll'd future only in a tight loop on a busy server where that allocation would matter (Luciano Mammino)

### `breaking-rename-for-vocabulary`

**Question.** Should a library perform a broad breaking rename across its whole public API to align vocabulary with its current mental model, or keep legacy names for compatibility?

- Teams: b · members (context): `b-sR08-f003731-q2` (f003731, decentralized-iroh)
- Domains: decentralized-iroh
- Concepts: API naming; breaking changes; semver; vocabulary consistency
- Positions:
  - `breaking-rename-for-vocabulary--p1` — rename-for-vocabulary-consistency-pre-1.0
    - **ramfox** · Source `f003731` · date 2025-10-22 · locator § "Changing from Node to Endpoint everywhere" — dropped "node" from iroh's vocabulary project-wide (`NodeAddr`→`EndpointAddr`, `node_id`→`endpoint_id`, etc.), reasoning that the term was a holdover from an earlier, broader project scope, and that pre-1.0 is the right moment to align vocabulary with the current mental model despite the breaking change this causes. Quote: "We've officially made the decision to remove the word "node" from our vocabulary... In preparation for 1.0, that has been rectified." [`b-sR08-f003731-c2`, team b]
- Positions seen by the extractor (`b-sR08-f003731-q2`): rename-for-vocabulary-consistency-pre-1.0

### `breaking-wire-change-in-minor`

**Question.** Should a pre-1.0 Rust networking library ship breaking wire-protocol changes in a routine minor release for a protocol improvement, or keep compatibility with the previous release?

- Teams: a · members (context): `a-sT04-f001319-q1` (f001319, decentralized-iroh, distributed, core)
- Domains: core, decentralized-iroh, distributed
- Concepts: semver; pre-1.0 stability; wire-protocol compatibility; relays
- Positions:
  - `breaking-wire-change-in-minor--p1` — break-compat-with-transition-window
    - **dignifiedquire (byline, iroh blog; Rust connection in source: iroh release post with Rust API code)** · Source `f001319` · date 2024-04-18 · locator section "Faster relay handshakes" — The relay handshake was refactored to drop a full roundtrip on every new connection. The team accepted that new relays cannot talk to 0.13.0 nodes, and softened it by keeping the old relays running for at least 4 more weeks. Quote: "Unfortunately, this means the new relays can not talk to 0.13.0 nodes." (flag: voice-unverified Not logged, as practice with no reason (rule 8): "Iroh relies on redb", the redb v2 upgrade (a performance gain, but no alternative named), and DNS discovery based on pkarr.) [`a-sT04-f001319-c1`, team a]
- Positions seen by the extractor (`a-sT04-f001319-q1`): break-compat-with-transition-window

### `build-tool-cargo-subcommand-vs-standalone`

**Question.** Should ecosystem build tooling that outgrows Cargo's scope ship as a `cargo` subcommand, or as an independent CLI / cargo-replacement?

- Teams: a · members (context): `a-sa05-f003025-q1` (f003025, core, desktop-cli-ui)
- Domains: core, desktop-cli-ui
- Concepts: cargo; build-tooling; ecosystem-fragmentation
- Positions:
  - `build-tool-cargo-subcommand-vs-standalone--p1` — cargo-subcommand
    - **teohhanhui** · Source `f003025` · date 2025-06-01 · locator comment @teohhanhui 2025-06-01T09:36:41Z — rejects a standalone "cargo plus plus" tool; ecosystem tools should be `cargo` subcommands Quote: "That's how you kill an ecosystem. It should be a `cargo` subcommand, please." [`a-sa05-f003025-c1`, team a]
    - **TapGhoul** · Source `f003025` · date 2025-06-01 · locator comment @TapGhoul 2025-06-01T11:36:46Z — subcommands are functionally identical to standalone binaries plus a few injected env vars, so a rust-ecosystem tool aiming for wide reuse should still register as a subcommand Quote: "I'd argue that a subsecond CLI tool makes a lot of sense as a cargo subcommand, given the general pattern I've seen." [`a-sa05-f003025-c2`, team a]
  - `build-tool-cargo-subcommand-vs-standalone--p2` — standalone-or-replacement
    - **jkelleyrtp** · Source `f003025` · date 2025-06-01 · locator comment @jkelleyrtp 2025-06-01T09:00:03Z — cargo cannot run/test/bench wasm, iOS or Android projects, so wasm-bindgen and similar high-usage tools are standalone by necessity, and dx follows that pattern since Dioxus is not exclusively a Rust tool Quote: "wasm-bindgen is the most used cli in the rust ecosystem and it is not a subcommand." [`a-sa05-f003025-c3`, team a]
    - **janhohenheim** · Source `f003025` · date 2025-06-01 · locator comment @janhohenheim 2025-06-01T11:49:48Z — cargo's limitations and slow development cycle led Bevy to design its CLI as a cargo wrapper/replacement rather than a subcommand Quote: "The frustrations with cargo's limitations and its glacial development cycle has led this very project to design the Bevy CLI alpha as a cargo replacement / wrapper and not a subcommand." [`a-sa05-f003025-c4`, team a]
    - **BD103** · Source `f003025` · date 2025-06-01 · locator comment @BD103 2025-06-01T19:12:02Z — Bevy-specific needs (asset handling, default index.html for the web feature) don't fit a general-purpose stable tool like Cargo; better to build 3rd-party tools on top of Cargo than have Cargo grow narrow features Quote: "it's less that Cargo is lacking features and more that certain features are too specific to be included in a standard Rust distribution." [`a-sa05-f003025-c5`, team a]
- Positions seen by the extractor (`a-sa05-f003025-q1`): cargo-subcommand, standalone-or-replacement

### `built-in-async-runtime`

**Question.** Should the language provide a built-in async runtime, or leave runtime choice to the crate ecosystem?

- Teams: b · members (context): `b-bk01-f000233-q2` (f000233, core)
- Domains: core
- Concepts: async runtime; executor
- Positions:
  - `built-in-async-runtime--p1` — no built-in runtime, ecosystem choice
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "Async and Await" § The runtime — Rust is a low-level language that strives for minimal runtime overhead, so unlike many languages whose runtime does memory management, exception handling, etc., Rust's async runtime has limited scope and is left to the ecosystem rather than built in; this means getting started requires an extra step (choosing a runtime crate). Quote: "Rust lets you choose one depending on your requirements, rather than providing one." [`b-bk01-f000233-c2`, team b]
- Positions seen by the extractor (`b-bk01-f000233-q2`): no built-in runtime, ecosystem choice

### `builtin-package-manager-effect`

**Question.** Does a language's built-in, first-party package manager (like Cargo) meaningfully change engineering practice compared to bolted-on/ecosystem-only dependency management (as in C/C++)?

- Teams: a · members (context): `a-sR15-f008241-q2` (f008241, core)
- Domains: core
- Concepts: package management; dependency ecosystem; tooling
- Positions:
  - `builtin-package-manager-effect--p1` — builtin-package-manager-changes-practice
    - **gregstoll** · Source `f008241` · date 2025-01-08 · locator section "Maybe…Rust?" — didn't even think to look for a C/C++ library with `f16`/bfloat support, because even if one existed they'd have had to vendor its source; running `cargo add half` was trivially easy by comparison, which they read as evidence that a good builtin package manager matters Quote: "I think this is an example of why having a good builtin package manager matters; even if I had found a C/C++ one I would have had to copy its source into my project or something. […] But just running cargo add half is so easy!" [`a-sR15-f008241-c2`, team a]
- Positions seen by the extractor (`a-sR15-f008241-q2`): builtin-package-manager-changes-practice (gregstoll)

### `byte-vs-bit-packed-cells`

**Question.** Should per-cell state be stored one byte per cell or packed as bits?

- Teams: b · members (context): `b-bk02-f000256-q3` (f000256, wasm)
- Domains: wasm
- Concepts: state representation; memory layout
- Positions:
  - `byte-vs-bit-packed-cells--p1` — bit-packed FixedBitSet over one-byte-per-cell Vec<Cell>
    - **rustwasm working group (Rust and WebAssembly book) [voice-unverified]** · Source `f000256` · date unknown (living doc) · locator § "Implementing Conway's Game of Life" exercises, Answer 2 — names the byte-per-cell layout's cost explicitly (wastes 7 of 8 bits per cell) against the bit-packed alternative, and provides the FixedBitSet-based rewrite as the resolution. Quote: "Representing each cell with a byte makes iterating over cells easy, but it comes at the cost of wasting memory." [`b-bk02-f000256-c4`, team b]
- Positions seen by the extractor (`b-bk02-f000256-q3`): byte-per-cell (simple indexing, wastes memory); bit-packed FixedBitSet (memory-efficient, more complex indexing) — chosen as the refactor

### `c-maintainers-rust-bindings-duty`

**Question.** When a C-subsystem maintainer changes their C code in a way that breaks the corresponding Rust abstraction/bindings, should the C maintainer be expected to help keep the Rust side correct (or at least not block small Rust-motivated robustness fixes to the C code), or is it legitimate for C maintainers to fix only their own C code and decline responsibility for Rust bindings entirely?

- Teams: b · members (context): `b-sb18-f005332-q1` (f005332, core, embedded)
- Domains: core, embedded
- Concepts: governance; Rust-for-Linux; cross-language maintenance boundaries; memory safety; kernel culture
- Positions:
  - `c-maintainers-rust-bindings-duty--p1` — c-maintainers-not-obligated-to-rust
    - **Ted Ts'o** · Source `f005332` · date undated (conference talk clip, reported in the 2024-09-04 article) · locator arstechnica.com article, quoting an off-camera interjection during a Linux conference talk, identified by Wedson Almeida Filho in a Register interview — interjects during a talk (about Filho's request that a filesystem gain Rust bindings) that while he will fix his own C code, he will not fix Rust bindings that break as a result, and won't be forced to learn Rust Quote: "Here's the thing: you're not going to force all of us to learn Rust." [`b-sb18-f005332-c1`, team b]
  - `c-maintainers-rust-bindings-duty--p2` — rust-needs-c-maintainer-cooperation
    - **Wedson Almeida Filho** · Source `f005332` · date 2024-08 (week before the 2024-09-04 article) · locator arstechnica.com article, quoting his Linux kernel mailing list resignation post — resigns as Rust-for-Linux maintainer after almost 4 years, citing exhaustion with "nontechnical nonsense" rather than technical disagreement, and states the future of kernels is with memory-safe languages Quote: "After almost 4 years, I find myself lacking the energy and enthusiasm I once had to respond to some of the nontechnical nonsense, so it's best to leave it up to those who still have it in them." [`b-sb18-f005332-c2`, team b]
    - **Asahi Lina** · Source `f005332` · date late August 2024 (Mastodon post, per the article) · locator arstechnica.com article, quoting her Mastodon post — says she "regretfully completely understands" Filho's frustration, describes being blocked by a C maintainer from pushing small robustness/lifetime fixes to the DRM scheduler's C code, and that every kernel panic in her Apple GPU driver traces to bugs in that C code, not her Rust code Quote: "But I get the feeling that some Linux kernel maintainers just don't care about future code quality, or about stability or security any more. They just want to keep their C code and wish us Rust folks would go away." [`b-sb18-f005332-c3`, team b]
  - `c-maintainers-rust-bindings-duty--p3` — adoption-slow-for-practical-reasons
    - **Linus Torvalds** · Source `f005332` · date August 2024 (public appearance, per the article) · locator arstechnica.com article, quoting his remarks at a public appearance — agrees there has been pushback on Rust, attributing it to old-time C kernel developers being unfamiliar with and unenthusiastic about learning a new, quite different language, plus instability in the Rust kernel infrastructure itself, rather than to bad faith Quote: "I was expecting [Rust] updates to be faster, but part of the problem is that old-time kernel developers are used to C and don't know Rust. They're not exactly excited about having to learn a new language that is, in some respects, very different. So there's been some pushback on Rust." [`b-sb18-f005332-c4`, team b]
- Positions seen by the extractor (`b-sb18-f005332-q1`): c-maintainers-not-obligated-to-rust, rust-needs-c-maintainer-cooperation, adoption-slow-for-practical-reasons

### `cfg-wasm-as-reduced-platform-proxy`

**Question.** should crates use `cfg(target_family = "wasm")` / `cfg(target_arch = "wasm32")` as a proxy for "running in a reduced-functionality standalone browser build," given that some Wasm targets now offer full Linux syscall access (filesystem, threads, subprocesses)?

- Teams: b · members (context): `b-sb22-f009062-q2` (f009062, wasm, core)
- Domains: core, wasm
- Concepts: cfg-based capability detection; target metadata; Wasm target diversity
- Positions:
  - `cfg-wasm-as-reduced-platform-proxy--p1` — deliberately misreport target metadata (`target_family` without "wasm", `arch: "wasm64"`) to defeat crates' `cfg`-based assumptions that "wasm32" implies a reduced-functionality standalone web build
    - **Yuri Iozzelli** · Source `f009062` · date 2026-08-13 · locator section "The hacks we did along the way" — many crates special-case behavior (e.g. `reqwest` swapping in a `fetch()`-based client) whenever they see the "wasm" target family or `wasm32` arch, which is wrong for a target with full syscall access; the team calls these misreports "hacks" pending the ecosystem recognizing that fully-featured Wasm targets exist Quote: "we would love to get rid of these hacks, but the proper solution requires awareness in the ecosystem that fully-featured Wasm targets exist" [`b-sb22-f009062-c2`, team b]
- Positions seen by the extractor (`b-sb22-f009062-q2`): treat that convention as unreliable and worth working around at the target-definition level (dropping "wasm" from `target_family`, reporting `arch = "wasm64"`) until the ecosystem catches up to full-featured Wasm targets existing (Yuri Iozzelli)

### `cli-flag-convenience-vs-consistency`

**Question.** For a CLI flag guarding a destructive action where the safe default is dry-run, should the flag's naming prioritize brevity/typing convenience (default-on dry-run, `--no-dry-run` to opt out) or consistency with how sibling commands in the same tool name their flags?

- Teams: b · members (context): `b-sb09-f003036-q1` (f003036, embedded, core)
- Domains: core, embedded
- Concepts: CLI ergonomics; flag naming; tooling consistency
- Positions:
  - `cli-flag-convenience-vs-consistency--p1` — consistency-across-commands
    - **MabezDev** · Source `f003036` · date 2025-05-21 · locator comment @MabezDev 2025-05-21T14:11:47Z — argues the new command should use `--no-dry-run` like every other command in the tool, for consistency. Quote: "Everywhere else we've use the `--no-dry-run`, I think we should be consistent." [`b-sb09-f003036-c1`, team b]
  - `cli-flag-convenience-vs-consistency--p2` — convenience-over-consistency
    - **bugadani** · Source `f003036` · date 2025-05-21 · locator comment @bugadani 2025-05-21T14:48:33Z — reasons that getting this particular flag wrong isn't dangerous, and `--no-dry-run` is annoying enough to type that a different default might be worth it, though agrees to change it if asked. Quote: "my thinking was that this isn't actually dangerous to get wrong, but --no-dry-run is sufficiently annoying to type. I can change it, we'll hate it" [`b-sb09-f003036-c2`, team b]
- Positions seen by the extractor (`b-sb09-f003036-q1`): convenience-over-consistency (bugadani), consistency-across-commands (MabezDev)

### `cli-flags-mirror-familiar-tool`

**Question.** For a niche, protocol-specific CLI tool, should its flags follow the conventions of an already-familiar general-purpose tool (curl), or be designed fresh around the tool's own domain?

- Teams: a · members (context): `a-sa14-f004947-q1` (f004947, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: CLI design; interface conventions; principle of least surprise
- Positions:
  - `cli-flags-mirror-familiar-tool--p1` — mirror an established CLI's conventions rather than design fresh
    - **Hannah Wang, Ben Yang, and Fisher Darling** · Source `f004947` · date 2026-07-27 · locator § What pvcli can do — state they designed pvcli around curl's argument conventions on purpose, for familiarity, rather than inventing new flag names for the OHTTP/proxy domain Quote: "We designed it with the "principle of least surprise" in mind. As a result, a lot of the arguments are the same as curl's!" [`a-sa14-f004947-c1`, team a]
- Positions seen by the extractor (`a-sa14-f004947-q1`): deliberately mirror curl's flag conventions ("a lot of the arguments are the same as curl's") rather than invent a new interface vocabulary, explicitly citing the "principle of least surprise"

### `cli-output-overwrite-default`

**Question.** Should a CLI tool that repeatedly writes an output file overwrite the same filename by default (simpler, faster iteration, matches a peer tool's behavior), or auto-generate a timestamped filename by default to avoid silently discarding a previous result?

- Teams: b · members (context): `b-sb13-f004160-q2` (f004160, embedded)
- Domains: embedded
- Concepts: CLI UX; default behavior; data-loss avoidance vs iteration convenience
- Positions:
  - `cli-output-overwrite-default--p1` — default-overwrite-latest-output
    - **KingCol13** · Source `f004160` · date 2026-02-26 · locator comment 2026-02-26T18:56:23Z — prefers overwriting the same output filename by default so past shell commands can be reused unedited to view the latest profile, matching the behavior of the peer tool samply Quote: "I still have a preference for overwriting. Currently I don't have to edit the commands from my history to quickly display the new profile... This also matches `samply`'s behaviour which I couldn't find anyone complaining about." [`b-sb13-f004160-c3`, team b]
  - `cli-output-overwrite-default--p2` — default-timestamp-to-avoid-silent-overwrite
    - **bugadani** · Source `f004160` · date 2026-02-26 · locator comment 2026-02-26T08:51:24Z — recommends timestamping the output filename, by default or at least from the second run onward, so a new profile does not silently replace an old one Quote: "I think a passable strategy is to save the profile with the timestamp in the filename, either by default, or only for the second file and later." [`b-sb13-f004160-c4`, team b]
- Positions seen by the extractor (`b-sb13-f004160-q2`): default-overwrite-latest-output (KingCol13), default-timestamp-to-avoid-silent-overwrite (bugadani)

### `cli-tool-single-vs-multi-protocol`

**Question.** Should a debugging CLI for a protocol specialize narrowly, one tool per protocol, or bundle several related protocols into one tool?

- Teams: b · members (context): `b-sR11-f004947-q1` (f004947, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: CLI design; tool scope
- Positions:
  - `cli-tool-single-vs-multi-protocol--p1` — one CLI should cover every privacy protocol a team operates (OHTTP, CONNECT proxying, MASQUE, Privacy Pass), rather than a narrow tool per protocol
    - **Hannah Wang, Ben Yang, Fisher Darling (Cloudflare)** · Source `f004947` · date 2026-07-27 · locator "Why build our own tool?" section — existing OHTTP-only tools (Thomson's Rust implementation, Wood's Go implementation) were useful but narrow; pvcli's differentiator is combining OHTTP, CONNECT proxying, MASQUE and Privacy Pass in one place Quote: "nothing combines OHTTP, CONNECT proxying, MASQUE and Privacy Pass (coming soon) all in one place" [`b-sR11-f004947-c1`, team b]
- Positions seen by the extractor (`b-sR11-f004947-q1`): broad multi-protocol tool

### `close-future-result-vs-infallible`

**Question.** Should a close/shutdown future return a Result or be infallible?

- Teams: b · members (context): `b-sT05-f002550-q3` (f002550, decentralized-iroh, core)
- Domains: core, decentralized-iroh
- Concepts: API error design; graceful shutdown
- Positions:
  - `close-future-result-vs-infallible--p1` — infallible close future
    - **ramfox, matheus23** · Source `f002550` · date 2025-01-15 · locator § Breaking Changes › iroh › changed — Endpoint::close's future no longer returns a Result Quote: "iroh::Endpoint::close's future is now infallible, instead of returning a Result" (flag: voice-unverified) [`b-sT05-f002550-c3`, team b]
- Positions seen by the extractor (`b-sT05-f002550-q3`): infallible close (replaced Result-returning close)

### `cloud-lock-in-source`

**Question.** Is the primary source of cloud vendor lock-in the compute platform you deploy to, or the managed data/SDK layer you build against?

- Teams: a · members (context): `a-sa24-f011220-q2` (f011220, cloud-workers, distributed, core)
- Domains: cloud-workers, core, distributed
- Concepts: vendor lock-in; ports-and-adapters (hexagonal) architecture; managed database services; compute portability
- Positions:
  - `cloud-lock-in-source--p1` — compute-platform choice is a smaller lock-in risk than adopting a cloud's proprietary managed-data SDK; ports-and-adapters (hexagonal) architecture removes the compute-level lock-in concern
    - **James Eastham** · Source `f011220` · date 2024-12-13 · locator ~13:48-14:12 — refactoring a Postgres-backed service to a proprietary store like DynamoDB, CosmosDB or Firestore forces a specific SDK and data model, which locks you in more than the choice of compute; structuring the codebase with entry-point adapters around a core business-logic crate lets the same Rust application run on Fargate/ECS or Lambda interchangeably, which he presents as the fix for vendor lock-in fears about serverless compute Quote: "using proprietary database Services...that is more of a form of locking than the compute you choose to use" [`a-sa24-f011220-c2`, team a]
- Positions seen by the extractor (`a-sa24-f011220-q2`): compute choice is a minor, mitigable lock-in vector and proprietary data SDKs are the real lock-in (Eastham) vs. the unnamed "someone" inside his fictional scenario who frames avoiding managed services in general, including compute, as the organizational rule to follow

### `codegen-macro-vs-generated-source`

**Question.** should a Rust code generator emit its output as procedural-macro magic or as plain generated source files?

- Teams: a · members (context): `a-sa23-f011186-q2` (f011186, web, core)
- Domains: core, web
- Concepts: macros; code generation; crate design
- Positions:
  - `codegen-macro-vs-generated-source--p1` — plain-generated-source over macro-based codegen (for client generation specifically)
    - **Adam** · Source `f011186` · date 2024-11-20 · locator ~00:19:37 — his tool emits a normal on-disk Rust crate (source dir, Cargo.toml, .rs files) rather than inline macro output, because macro output is hard to debug and macros can produce confusing compile errors Quote: "it doesn't use macros it doesn't create this in line it's outputting normal rust code and this is I think a really good approach because as much as I do like using macros they're so hard to debug" [`a-sa23-f011186-c2`, team a]
- Positions seen by the extractor (`a-sa23-f011186-q2`): plain-generated-source-preferred-for-client-codegen (Adam), macro-driven-schema-extraction-favored-for-server-annotation (Adam, re: dropshot's `#[endpoint]` + schemars)

### `compile-time-cost-of-generated-crates`

**Question.** is a long compile time an acceptable cost of large generated/dependency-heavy crates in exchange for API correctness and ergonomics?

- Teams: a · members (context): `a-sa23-f011186-q5` (f011186, web, core)
- Domains: core, web
- Concepts: compile times; code generation; crate size
- Positions:
  - `compile-time-cost-of-generated-crates--p1` — accept long compile times for generated-crate quality
    - **Adam** · Source `f011186` · date 2024-11-20 · locator ~00:30:09 — large autogenerated API crates (his own and others', e.g. Stripe's) dominate his project's slowest-compiling dependencies, especially in release mode; after looking for ways to shrink them, he chose to accept the compile-time cost rather than sacrifice API quality Quote: "eventually I kind of just decided I'd rather eat the long compile time and be able to give really high quality API to my users" [`a-sa23-f011186-c5`, team a]
- Positions seen by the extractor (`a-sa23-f011186-q5`): accept-long-compile-times-for-quality (Adam)

### `compile-time-typed-dsl`

**Question.** Is hosting a Rust DSL's programs as compile-time types (zero runtime cost, no dynamic loading) worth trading away runtime-loaded/dynamic DSL programs?

- Teams: a · members (context): `a-sa16-f007175-q2` (f007175, desktop-cli-ui, core)
- Domains: core, desktop-cli-ui
- Concepts: macros; type-level programming; DSLs
- Positions:
  - `compile-time-typed-dsl--p1` — compile-time-typed-dsl
    - **Soares Chen** · Source `f007175` · date 2025-06-14 · locator § Disadvantages, Dynamic Loading — Hosting DSL programs as compile-time types trades away runtime dynamic loading (config files, plugins, game mods) for zero-cost, compile-time interpretation. Quote: "since the DSL is hosted at compile time, this technique cannot be easily used to run DSL programs loaded into a host application during runtime" [`a-sa16-f007175-c2`, team a]
- Positions seen by the extractor (`a-sa16-f007175-q2`): compile-time-typed-dsl

### `compiler-triage-automation`

**Question.** Should routine compiler-team process work (PR triage/bookkeeping, nudging reviewers, tracking regressions) be fully automated, or does it need a human doing it manually to protect contributors' limited time and avoid over-pinging them?

- Teams: b · members (context): `b-sb23-f011235-q1` (f011235, core)
- Domains: core
- Concepts: PR triage; prioritization working group; contributor time; automation of process
- Positions:
  - `compiler-triage-automation--p1` — keep PR-nudging/triage bookkeeping partly manual rather than fully automating it
    - **Antonio Pirino** · Source `f011235` · date 2025-06-10 · locator ~05:14-06:15 — he maintains a manual markdown bookkeeping file cross-referenced against the triage bot's oldest-PR list, and explicitly poses "why can this not be completely automated?" to himself, answering that contributors have only a finite amount of time and are "a precious asset," so a human judgment call on when to nudge a reviewer avoids over-pressuring them, even though external contributors also expect timely responses Quote: "there is one thing that is ... that I really care about ... we have on one end [a finite] amount of resources[; c]ontributors ... can allocate only a[f]inite amount of time" [`b-sb23-f011235-c1`, team b]
- Positions seen by the extractor (`b-sb23-f011235-q1`): keep this work partly manual by deliberate choice, because full automation would risk pinging volunteer reviewers too aggressively, versus the implicit alternative (raised by the speaker himself as a question) of automating it completely

### `component-abi-special-case-lowerings`

**Question.** In the Component Model's GC canonical ABI, should common shapes (e.g. `null` for `none`/`error`, a boolean `i32` for a no-payload `result`) get ad hoc special-cased lowerings for efficiency, or should the ABI stick to one regular, shape-driven lowering rule per component type?

- Teams: a · members (context): `a-sa05-f003074-q1` (f003074, wasm)
- Domains: wasm
- Concepts: canonical-abi; wasm-gc; type-lowering
- Positions:
  - `component-abi-special-case-lowerings--p1` — ad-hoc-optimize-common-shapes
    - **lukewagner** · Source `f003074` · date 2025-06-04 · locator comment @lukewagner 2025-06-04T21:38:44Z — proposes letting `ref.null` represent `none`/no-error when the inner type disallows null, and using a boolean `i32` for no-payload `result`, since these shapes are extremely common and "licensed" as CABI-level wins even though ad hoc Quote: "we are licensed to do that in the CABI when it's a significant win and `option` is very common" [`a-sa05-f003074-c1`, team a]
  - `component-abi-special-case-lowerings--p2` — regular-lowering-only
    - **rossberg** · Source `f003074` · date 2025-06-06 · locator comment @rossberg 2025-06-06T09:39:34Z — disputes that the null-for-none optimization would apply to anywhere near 95% of options in practice, because languages with parametric polymorphism (e.g. Java's Optional) typically cannot perform that specialization without costly runtime type dispatch Quote: "FWIW, I don't think it is gonna be even close to 95%. Languages with parametric polymorphism typically don't or can't do such a specialisation" [`a-sa05-f003074-c2`, team a]
  - `component-abi-special-case-lowerings--p3` — cautious-of-shape-proliferation
    - **fitzgen** · Source `f003074` · date 2025-06-13 · locator comment @fitzgen 2025-06-13T19:02:24Z — allowing extra matched shapes like `i31ref` risks a slippery slope of "how many shapes is enough," so any widening of matchable shapes needs an explicit design principle, not case-by-case allowances Quote: "It seems to me like this could potentially be a slippery slope: How many shapes is enough?" [`a-sa05-f003074-c3`, team a]
- Positions seen by the extractor (`a-sa05-f003074-q1`): ad-hoc-optimize-common-shapes, regular-lowering-only

### `component-map-duplicate-keys`

**Question.** When lifting/lowering a component-model `map<K,V>` value with duplicate keys, should bindings generators be required to normalize to a defined winner (e.g. last-key-wins), should the spec instead mandate key uniqueness as an enforced boundary constraint, or should a host be permitted but not required to deduplicate, leaving the behavior non-deterministic?

- Teams: b · members (context): `b-sb11-f003384-q1` (f003384, wasm)
- Domains: wasm
- Concepts: component-model value types; `map<K; V>`; CABI lifting/lowering; bindings generator contract; non-determinism vs determinism
- Positions:
  - `component-map-duplicate-keys--p1` — generators-must-normalize-last-wins
    - **lukewagner** · Source `f003384` · date 2025-08-20 · locator https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-20T16:16:14Z — proposes strengthening the spec wording so bindings generators are required, not merely expected, to normalize duplicate-key handling Quote: "would it make sense to say \"Although the Component Model cannot enforce this property, bindings generators **MUST** ...\"?" [`b-sb11-f003384-c1`, team b]
    - **lann** · Source `f003384` · date 2025-08-20 · locator https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-20T18:54:54Z — drafts the concrete requirement that generated map interfaces must behave as if duplicates were filtered with last-value-wins semantics Quote: "Generated map interfaces MUST behave as if duplicate entries have been filtered out (last duplicate key value wins). Map values with existing duplicate entries MAY be passed to other components." [`b-sb11-f003384-c2`, team b]
  - `component-map-duplicate-keys--p2` — mandate-uniqueness-enforced-at-boundary
    - **primoly** · Source `f003384` · date 2025-08-20 · locator https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-20T17:30:35Z — argues duplicate keys should not be silently tolerated; uniqueness should be a spec-mandated, boundary-enforced constraint Quote: "I think uniqueness of keys should be mandated by the spec and enforced at the boundary." [`b-sb11-f003384-c3`, team b]
    - **ouillie** · Source `f003384` · date 2025-08-20 · locator https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-20T18:52:54Z — agrees uniqueness should be mandated in the spec, but on violation the lowering side should just silently keep the final value rather than trap Quote: "I have no issue with mandating uniqueness in the spec... I don't think the lowering should trap." [`b-sb11-f003384-c4`, team b]
  - `component-map-duplicate-keys--p3` — host-may-not-must-dedupe
    - **badeend** · Source `f003384` · date 2025-08-24 · locator https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-24T19:46:08Z — argues hosts should be allowed, not required, to deduplicate keys, drawing an analogy to how NaN payload canonicalization is optional rather than mandatory at component boundaries Quote: "we could likewise non-deterministically allow-but-not-require duplicate keys to be merged (with well-defined last-value-overwrites semantics when such merging occurs)." [`b-sb11-f003384-c5`, team b]
- Positions seen by the extractor (`b-sb11-f003384-q1`): generators-must-normalize-last-wins (lukewagner, lann), mandate-uniqueness-enforced-at-boundary (primoly, ouillie), host-may-not-must-dedupe (badeend)

### `component-map-ordering`

**Question.** Should the component-model `map` type guarantee iteration order (and be renamed to signal that), or should it be explicitly unordered like the hash-map types of most host languages?

- Teams: b · members (context): `b-sb11-f003384-q2` (f003384, wasm)
- Domains: wasm
- Concepts: `map<K; V>`; iteration order; determinism; naming
- Positions:
  - `component-map-ordering--p1` — preserve-order-rename-type
    - **primoly** · Source `f003384` · date 2025-08-20 · locator https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-20T17:30:35Z — expects bindings to preserve entry order since most languages' Map types do, and would rename the type (e.g. `dict`, `ordered-map`) to avoid confusion with non-order-preserving maps Quote: "it should be expected that bindings will map `map` to a type that retains order. It would then also be a good idea to rename to something else (e.g. `dict`, `ordered-map`)" [`b-sb11-f003384-c6`, team b]
  - `component-map-ordering--p2` — unordered-by-default
    - **ouillie** · Source `f003384` · date 2025-08-20 · locator https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-20T18:52:54Z — argues the basic map type should not be ordered since most languages' basic map types aren't, with an ordered variant left to `list<tuple<key,value>>` if ever needed Quote: "I don't think the basic map type should be ordered. Most languages do not use an ordered basic map type because 9 times out of 10 you don't need an ordering for your maps." [`b-sb11-f003384-c7`, team b]
    - **badeend** · Source `f003384` · date 2025-08-24 · locator https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-24T19:46:08Z — keys of `map` should not guarantee any order, citing Rust's HashMap, .NET's Dictionary, Java's HashMap and Go's map as precedent for unordered semantics Quote: "Agree that keys of `map`s should not guarantee any order. This aligns with Rust's HashMap, .NET's Dictionary, Java's HashMap, Go's map, and probably more." [`b-sb11-f003384-c8`, team b]
  - `component-map-ordering--p3` — deterministic-profile-may-need-canonical-order
    - **lukewagner** · Source `f003384` · date 2025-08-26 · locator https://github.com/WebAssembly/component-model/pull/554 comment 2025-08-26T19:13:32Z — notes that if a deterministic execution profile doesn't normalize map order, order becomes an observable part of `map`'s semantics, which is a tradeoff worth discussing rather than settled Quote: "Since the deterministic profile can't randomly permute, if we don't normalize order in the deterministic profile, then that effectively makes order an observable part of the semantics of `map` values." [`b-sb11-f003384-c9`, team b]
- Positions seen by the extractor (`b-sb11-f003384-q2`): preserve-order-rename-type (primoly), unordered-by-default (ouillie, badeend), deterministic-profile-may-need-canonical-order (lukewagner)

### `compress-debug-sections-default`

**Question.** should rustc set `--compress-debug-sections=zstd` as the default linker flag for Linux targets, to shrink `target/` and binary size?

- Teams: b · members (context): `b-sb22-f009132-q1` (f009132, core)
- Domains: core
- Concepts: linker flags; debug info compression; zstd/zlib; rust-lld
- Positions:
  - `compress-debug-sections-default--p1` — make `--compress-debug-sections=zstd` the Linux default
    - **vri** · Source `f009132` · date 2023-12-17 · locator opening post — measured a hello-world project's `target/` shrinking from 4.7M to 1.5M and a modest `hyperfine`-measured build-time improvement (1.65s → 1.25s mean) with the flag enabled via `RUSTFLAGS`, and proposed defaulting it before filing a full MCP Quote: "I feel we should set --compress-debug-sections=zstd in the link args by default for linux rust targets." [`b-sb22-f009132-c1`, team b]
  - `compress-debug-sections-default--p2` — the stated motivation (shrinking `target/`) doesn't yet justify this specific fix, and if it ships at all it should apply to release builds only
    - **epage** · Source `f009132` · date 2023-12-18 · locator reply timestamped 2023-12-18T15:54:39 — argues the discussion should first pin down *why* `target/` is big — duplication across projects, stale files, or genuinely unused debug info — rather than reaching for compression as a default fix that would also slow down (or at least not obviously help) every debug build Quote: "I feel the motivation itself is lacking." [`b-sb22-f009132-c2`, team b]
  - `compress-debug-sections-default--p3` — this cannot become the Linux default until mainstream distro debugging/profiling tools support zstd-compressed debug sections
    - **Vorpal** · Source `f009132` · date 2023-12-24 · locator reply timestamped 2023-12-24T13:26:03, responding to glandium's data point that Ubuntu 22.04 LTS's gdb/binutils lack zstd support — many developers (including Vorpal) are required to use Ubuntu LTS or another enterprise distro at work, so shipping zstd-by-default would silently break their debugging experience until that tooling catches up Quote: "That seems like a showstopper for making this default... I don't see this going anywhere." [`b-sb22-f009132-c3`, team b]
- Positions seen by the extractor (`b-sb22-f009132-q1`): adopt it now as a low-hanging-fruit size/build-time win (vri); skeptical that the stated motivation justifies picking this fix at all, and if adopted, scope it to release builds only (epage); block it until common Linux distro tooling (gdb, binutils, valgrind, perf on Ubuntu LTS) actually supports zstd-compressed debug sections (Vorpal, corroborated by glandium's Ubuntu 22.04 data point)

### `consolidate-internal-network-frameworks`

**Question.** When several internal Rust services need similar network-framework capabilities, should the org consolidate them into one shared framework built on existing async-ecosystem crates, or keep purpose-built frameworks separate even at the cost of overlap?

- Teams: a · members (context): `a-sa15-f005604-q1` (f005604, distributed, web)
- Domains: distributed, web
- Concepts: framework-design; code-reuse; tokio; hyper; extensibility
- Positions:
  - `consolidate-internal-network-frameworks--p1` — reuse-and-consolidate-on-ecosystem-crates
    - **Ivan Nikulin** · Source `f005604` · date 2023-03-02 · locator "Technology choice" section — states Oxy is deliberately built on top of existing open-source crates (hyper, tokio) rather than reinventing them, prioritizing faster iteration and battle-tested code, while contributing fixes back upstream; two of the team are now core maintainers of tokio/hyper Quote: "We intentionally tried to stand on the shoulders of the giants with this project and avoid reinventing the wheel." [`a-sa15-f005604-c1`, team a]
- Positions seen by the extractor (`a-sa15-f005604-q1`): reuse-and-consolidate-on-ecosystem-crates, keep-separate-for-differing-objectives

### `const-generics-unify-specializations`

**Question.** When several hand-written data structures are near-duplicate specializations differing only by array length/arity (e.g. a 2-stride vs. 3-stride zip), should they be unified into one type parameterized by a const generic, or kept as separate hand-specialized versions?

- Teams: b · members (context): `b-sR12-f005085-q2` (f005085, ml, core)
- Domains: core, ml
- Concepts: const generics; monomorphization; code duplication
- Positions:
  - `const-generics-unify-specializations--p1` — unify-via-const-generics
    - **antimora (Tracel AI / burn maintainer)** · Source `f005085` · date 2026-09-08 · locator PR review comment, 2026-09-08T21:11:40Z — `Zip3Nest` is `ZipNest` with a third stride array threaded through, and the two have already drifted from each other inside this same PR; a `Nest<const N: usize>` would cover both with identical codegen since it monomorphizes Quote: "Stepping back, `Zip3Nest` is `ZipNest` with a third stride array threaded through every line, and the two have already drifted inside this PR... A `Nest<const N: usize>` would cover both, and `CollapsedLayout` at N=1, with identical codegen since it monomorphizes. Not blocking, but the drift is already real rather than hypothetical." [`b-sR12-f005085-c2`, team b]
- Positions seen by the extractor (`b-sR12-f005085-q2`): unify-via-const-generics

### `coupled-debug-accessor-vs-primitive`

**Question.** When a runtime needs to expose a narrow debugging capability that would be most efficient as a purpose-built accessor coupled to internal layout details, should the maintainers accept that coupled accessor (even once made asymptotically efficient), or insist on a smaller, decoupled, general-purpose primitive that pushes the assembling logic (and any inefficiency) out to the caller?

- Teams: b · members (context): `b-sb16-f005000-q1` (f005000, wasm, core)
- Domains: core, wasm
- Concepts: API surface minimalism; internal layout coupling; debugging APIs; encapsulation
- Positions:
  - `coupled-debug-accessor-vs-primitive--p1` — narrow-purpose-built-debug-accessor
    - **smarcd** · Source `f005000` · date 2026-08-12 · locator PR description @smarcd 2026-08-12T17:14:28Z — adds `debug_function_index`, a host-only, linear-search accessor for debugging tools, deliberately scoped to guest-debugging mode only. Quote: "Adds a host-only inverse to Instance::debug_function for debugging tools that need to serialize a same-instance funcref as a Wasm function index." [`b-sb16-f005000-c1`, team b]
    - **smarcd** · Source `f005000` · date 2026-08-13 · locator comment @smarcd 2026-08-13T15:49:36Z — rewrites `debug_function_index` to be O(1) via a lazily-built, module-level cached reverse table, addressing the performance objection while keeping the original narrow accessor design. Quote: "I pushed a rewrite that makes `debug_function_index` itself O(1) instead of scanning every function." [`b-sb16-f005000-c4`, team b]
  - `coupled-debug-accessor-vs-primitive--p2` — skeptical-of-narrow-internals-coupled-api
    - **alexcrichton** · Source `f005000` · date 2026-08-13 · locator comment @alexcrichton 2026-08-13T13:55:31Z — questions the use case, noting the API is inherently inefficient (linear search) and may not survive future refactorings, and wants to understand whether the cost of supporting it is justified. Quote: "This is a pretty powerful debugging capability which also sort of inherently can't be efficient (e.g. the linear search here) and may also not hold up in future possible refactorings." [`b-sb16-f005000-c2`, team b]
  - `coupled-debug-accessor-vs-primitive--p3` — prefer-generic-decoupled-primitive
    - **cfallin** · Source `f005000` · date 2026-08-13 · locator comment @cfallin 2026-08-13T14:34:17Z — argues the linear-search accessor makes a whole-store snapshot quadratic overall, and proposes instead adding `Func::eq`/`Func::hash` so the caller can build their own hashtable in a single linear pass, asymptotically better. Quote: "I could see a `Func::eq` implementation making sense (because the primitive is harder to argue against -- it may be independently useful)... asymptotically better." [`b-sb16-f005000-c3`, team b]
    - **cfallin** · Source `f005000` · date 2026-08-13 · locator comment @cfallin 2026-08-13T15:57:51Z — even with the O(1) fix, still prefers not taking on the coupling to `VMContext`'s internal layout and the added delicate logic for what is a niche use case, and again asks whether `Func::eq`/`Func::hash` plus an external algorithm could work instead. Quote: "I think that is still the sort of complexity that we would rather not take on if we don't have to... This is a whole lot of new functionality instead for a niche use-case." [`b-sb16-f005000-c5`, team b]
    - **smarcd** · Source `f005000` · date 2026-08-13 · locator comment @smarcd 2026-08-13T16:10:07Z — agrees the layout coupling isn't worth it, drops `debug_function_index`, and implements `Func::eq`/`Func::hash` as pointer-identity equality instead, letting the debugger build its own index map. Quote: "That's a fair concern — coupling to `VMContext`'s internal layout is more entanglement than this is worth. I dropped `debug_function_index` and pushed `Func::eq`/`Func::hash` instead, per your suggestion." [`b-sb16-f005000-c6`, team b]
- Positions seen by the extractor (`b-sb16-f005000-q1`): narrow-purpose-built-debug-accessor (smarcd, initial and revised), prefer-generic-decoupled-primitive (alexcrichton, cfallin)

### `cow-for-allocation-visibility`

**Question.** When an allocation-avoiding type like `Cow<str>` would only save a negligible amount of work, should a Rust programmer still prefer it over a plain `String`, for the sake of making allocations visible in the code?

- Teams: a · members (context): `a-sR15-f008241-q1` (f008241, core, web)
- Domains: core, web
- Concepts: `Cow`; allocation; idiomatic Rust
- Positions:
  - `cow-for-allocation-visibility--p1` — prefer-cow-for-allocation-visibility-even-at-negligible-gain
    - **gregstoll** · Source `f008241` · date 2025-01-08 · locator section "Step 2: Adding 16-bit float support", paragraph on the `Cow<&str>` commit — switched query parsing from `String` to `std::borrow::Cow<&str>`; likes that Rust makes allocations visible, which pushes them to avoid allocations even when the performance impact is minuscule Quote: "I really like how obvious Rust makes it when you're doing allocations and that makes me want to avoid them, even when the performance impact is minuscule." [`a-sR15-f008241-c1`, team a]
- Positions seen by the extractor (`a-sR15-f008241-q1`): prefer-cow-for-allocation-visibility-even-at-negligible-gain (gregstoll)

### `cpp-binding-tool-choice`

**Question.** For binding a large existing C++ API surface to Rust, should you use a low-level C-ABI-only generator (bindgen/cbindgen), a manually-declared bridge macro with boxed indirection (CXX), a hand-written interface-description-language with explicit layout control ("Zengar"), or native compiler integration across clang and rustc (Crubit)?

- Teams: b · members (context): `b-sb24-f011312-q1` (f011312, core)
- Domains: core
- Concepts: bindgen; cbindgen; CXX; IDL-based bridging; compiler integration; C-ABI
- Positions:
  - `cpp-binding-tool-choice--p1` — no-single-tool-fits-everyone
    - **Taylor** · Source `f011312` · date 2025-10-03 · locator [05:14]-[10:18] — bindgen/cbindgen only handle C-ABI-compatible functions, forcing manual unsafe conversion for any RAII/generic/user-defined type; CXX adds safer higher-level types but requires manually redeclaring items and boxing everything since it can't see existing types' memory layout; "Zengar" lets users specify size/alignment to pass by value but requires a separate IDL file, which doesn't scale to huge API surfaces; Crubit gets maximum coverage via native clang+rustc integration but requires a clang toolchain, which not every project can use Quote: "within the realm of C++ interop, no two projects want exactly the same thing... So can there ever really be one interop solution to rule them all?" [`b-sb24-f011312-c1`, team b]
- Positions seen by the extractor (`b-sb24-f011312-q1`): no-single-tool-fits-everyone (Taylor)

### `cpp-bindings-default-unsafe`

**Question.** When binding C++ APIs whose safety depends on undocumented preconditions, should every C++ function be marked `unsafe` in Rust by default, or should the binding rely on C++-side safety annotations plus type-based heuristics to mark functions safe where possible?

- Teams: b · members (context): `b-sb24-f011312-q2` (f011312, core)
- Domains: core
- Concepts: blanket unsafe; safety annotations; type-based heuristics; harm reduction
- Positions:
  - `cpp-bindings-default-unsafe--p1` — reject-blanket-unsafe-use-annotations-and-heuristics
    - **Taylor** · Source `f011312` · date 2025-10-03 · locator [12:21]-[14:24] — marking every C++ function `unsafe` in Rust makes the annotation meaningless (the fish shell project forked its own version of auto-cxx just to turn `unsafe` off entirely); Crubit instead combines optional C++-side safety annotations with type-based heuristics so callers only see `unsafe` on genuinely dangerous APIs Quote: "When all your code says unsafe, it stops meaning anything." [`b-sb24-f011312-c2`, team b]
- Positions seen by the extractor (`b-sb24-f011312-q2`): reject-blanket-unsafe-use-annotations-and-heuristics (Taylor)

### `cpp-mutable-reference-representation`

**Question.** For C++ mutable references crossing into Rust (which, unlike Rust's `&mut`, are not guaranteed exclusive and can alias), should the FFI binding represent them as raw unsafe pointers, `Cell`-based interior mutability, or a new native non-exclusive C++-style reference type added to Rust?

- Teams: b · members (context): `b-sb24-f011312-q3` (f011312, core)
- Domains: core
- Concepts: reference aliasing; Cell; exclusivity; field projection; auto-referencing
- Positions:
  - `cpp-mutable-reference-representation--p1` — none-satisfying-yet-add-native-cpp-reference-type
    - **Taylor and Tyler** · Source `f011312` · date 2025-10-03 · locator [19:27]-[25:34] — raw pointers force every reference-taking method (including all method calls, via `self`) to be unsafe; `Cell` assumes invariants C++ references don't provide (safe projection through `Option`/`Vec`, and `Sync`-safety for thread-safe C++ types); their proposed alternative is a new C++-style reference type in Rust where mutation-that-can-invalidate-a-reference is unsafe, but this needs new compiler features (generalized field projection, auto-referencing for custom reference types) that don't exist yet Quote: "None of these approaches are perfect, but with some help from the Rust compiler, we can begin to offer safer and more ergonomic APIs." [`b-sb24-f011312-c3`, team b]
- Positions seen by the extractor (`b-sb24-f011312-q3`): none-satisfying-yet-add-native-cpp-reference-type (Taylor/Tyler)

### `crdt-vs-coordination`

**Question.** For a multi-actor collaborative system (humans and agents editing together), should convergence come from CRDTs or from a coordinating mechanism (locking, operational transform, a single authoritative server)?

- Teams: b · members (context): `b-sR11-f005071-q1` (f005071, distributed)
- Domains: distributed
- Concepts: CRDTs; distributed state; concurrent editing
- Positions:
  - `crdt-vs-coordination--p1` — convergence for a multi-actor, human-and-agent live document should come from CRDTs rather than a coordinating or locking mechanism
    - **Nathan Sobo (Zed founder)** · Source `f005071` · date 2026-09-01 · locator "The dependency tree exists today" section — lists CRDTs, "formalized in 2011," as "the center of Zed's own work for the past decade," letting a Delta worktree be "edited by several people and agents on different continents at once" with no coordination step Quote: "Convergence without coordination." [`b-sR11-f005071-c1`, team b]
- Positions seen by the extractor (`b-sR11-f005071-q1`): CRDTs, no coordination required

### `current-thread-runtime-for-blocking`

**Question.** Is it acceptable practice to run blocking synchronous I/O (e.g. database calls) inside a dedicated single-threaded ("current_thread") Tokio runtime on its own OS thread, or does limiting a Tokio runtime to a single thread carry negative internal ramifications that make this an anti-pattern except when no other OS threads are available?

- Teams: b · members (context): `b-sb18-f005307-q2` (f005307, distributed, decentralized-iroh)
- Domains: decentralized-iroh, distributed
- Concepts: async runtimes; current_thread/single-threaded executors; blocking I/O bridging
- Positions:
  - `current-thread-runtime-for-blocking--p1` — single-threaded-runtime-fine-for-n1-scheduling
    - **withoutboats** · Source `f005307` · date 2024-08-02 · locator lobste.rs/s/7rtvnp, comment 2024-08-02T08:03:38-05:00 — responding to kbknapp's report that Jon Gjengset warned against using Tokio's single-threaded runtime except when no OS threads are available, states this warning is wrong: if you want N:1 scheduling of async tasks, the single-threaded runtime is the right tool, though combining it with blocking syscalls on that thread is unusual Quote: "I believe that Jon Gjengset is wrong about this. If you want to N:1 scheduling of async tasks (instead of M:N), using the single threaded runtime is the right choice." [`b-sb18-f005307-c3`, team b]
- Positions seen by the extractor (`b-sb18-f005307-q2`): single-threaded-runtime-fine-for-n1-scheduling

### `custom-allocator-restart-persistence`

**Question.** To persist Rust objects across process/container restarts, should a practitioner build a custom raw-memory `Allocator` (memfd + systemd FD store + mmap) rather than serializing state to an external store (file/Redis) on shutdown/startup?

- Teams: b · members (context): `b-sb19-f005836-q1` (f005836, core)
- Domains: core
- Concepts: custom Allocator trait (nightly); memfd_create; systemd File Descriptor Store; mmap
- Positions:
  - `custom-allocator-restart-persistence--p1` — custom-allocator-for-restart-persistence
    - **Graham King** · Source `f005836` · date 2024-01-17 · locator § opening / "An allocator backed by persistent memory" — combining systemd's FD store, `memfd_create`, and a custom Rust `Allocator` lets an object's backing memory survive a `systemctl restart`, as an alternative to his own prior practice of serializing state to Redis or a temp file on restart Quote: "We are going to stitch three things together to make Rust objects that survive program restart." [`b-sb19-f005836-c1`, team b]
- Positions seen by the extractor (`b-sb19-f005836-q1`): custom-allocator-for-restart-persistence (Graham King)

### `custom-bytes-type-vs-vec-u8`

**Question.** At an API boundary where allocation strategy matters (e.g. future backend-managed/pinned memory), should owned byte buffers be typed as `Vec<u8>` or a custom wrapper type?

- Teams: b · members (context): `b-sR08-f003587-q3` (f003587, ml)
- Domains: ml
- Concepts: buffer/allocator abstraction; API design; GPU memory
- Positions:
  - `custom-bytes-type-vs-vec-u8--p1` — custom-bytes-type-over-vec-u8-at-boundaries
    - **nathanielsimard** · Source `f003587` · date 2025-10-09 · locator PR #3792, review comment 2025-10-09T13:32:53Z — asks that owned buffer types at the store's API boundary use `burn_common::Bytes` rather than `Vec<u8>`, while leaving borrowed `&[u8]`/`&mut [u8]` as-is, so a future backend-managed allocation strategy (e.g. pinned GPU memory) can be substituted later. Quote: "We should replace all instances of `Vec<u8>` by `burn_common::Bytes`, `&[u8]` and `&mut [u8]` are OK" [`b-sR08-f003587-c3`, team b]
- Positions seen by the extractor (`b-sR08-f003587-q3`): custom-bytes-type-over-vec-u8-at-boundaries

### `custom-wasm-target-vs-wasi`

**Question.** when the goal is running an existing, unmodified Rust/Linux program (with threads, filesystem, subprocesses) inside a sandbox, should you target the standardized WASI Rust targets (wasm32-wasip1/2/3), or define and require a custom, non-standard Rust target tailored to the sandbox's own syscall/threading model?

- Teams: b · members (context): `b-sb22-f009062-q1` (f009062, wasm)
- Domains: wasm
- Concepts: WASI; custom rustc targets; wasm32-unknown-unknown/emscripten/wali; cross-compilation
- Positions:
  - `custom-wasm-target-vs-wasi--p1` — define a custom Rust compilation target (`wasm32-browserpod-linux-musl`) rather than port to a WASI target, for running unmodified existing Rust programs in-browser
    - **Yuri Iozzelli** · Source `f009062` · date 2026-08-13 · locator section "Why not just pick WASI?" — porting `yarn` to WASI would mean touching every `std::os::unix` call site, removing thread usage entirely (wasip3's cooperative threading is new and unsupported by std or tokio), and accepting the loss of shelling out to `git`/`node`; since BrowserPod's own kernel already solves filesystem, networking, subprocesses and real per-thread parallelism, the team wrote a custom target instead of doing that porting work Quote: "BrowserPod already solves these problems, so we decided to skip the middleman and implement our own Rust target." [`b-sb22-f009062-c1`, team b]
- Positions seen by the extractor (`b-sb22-f009062-q1`): build a custom target (`wasm32-browserpod-linux-musl`) rather than port to WASI, because WASI still requires `std::os::unix`→`std::os::wasi` porting work, has no real thread/parallelism support in even the newest wasip3 draft, and forces giving up functionality (like shelling out to `git`/`node`) that BrowserPod already provides natively (Yuri Iozzelli)

### `debug-assert-vs-infallible`

**Question.** In a library, should an internal invariant be enforced with `debug_assert!` (documents and tests the assumption, but only panics in debug builds), or should the code be rewritten to be infallible so the assumption can never be violated even conceptually?

- Teams: b · members (context): `b-sb04-f001392-q2` (f001392, core)
- Domains: core
- Concepts: debug_assert; panics; infallible code; library API design; testing
- Positions:
  - `debug-assert-vs-infallible--p1` — keep-debug-asserts
    - **EdJoPaTo** · Source `f001392` · date 2024-05-11 · locator PR #1089, comment 2024-05-11T09:13:41Z — values `debug_assert!` for documenting and actually testing an assumption in the code, and is only "fine" with it being replaced because the change came with enough tests to cover the same ground Quote: "What I liked about it were the assumptions actually tested." [`b-sb04-f001392-c3`, team b]
  - `debug-assert-vs-infallible--p2` — prefer-infallible-code
    - **joshka** · Source `f001392` · date 2024-05-11 · locator PR #1089, comment 2024-05-11T02:47:17Z — dislikes `debug_assert!` in a library because when the assumption is wrong, it surfaces as a hard-to-report panic in the library's users' users, fixable only by a coordinated release of both projects, so the code should instead be made infallible Quote: "I don't like debug_asserts at all, especially in a library." [`b-sb04-f001392-c4`, team b]
- Positions seen by the extractor (`b-sb04-f001392-q2`): keep-debug-asserts, prefer-infallible-code

### `dedicated-design-vs-duplicate-now`

**Question.** When adding support for a new but closely related serialization format, should the implementation start as a decoupled, dedicated design or as pragmatic duplication of the existing similar format's code, refactored later?

- Teams: b · members (context): `b-sb09-f002567-q1` (f002567, ml)
- Domains: ml
- Concepts: serialization formats; recorders; code de-duplication; API decoupling
- Positions:
  - `dedicated-design-vs-duplicate-now--p1` — dedicated-decoupled-recorder-from-the-start
    - **antimora** · Source `f002567` · date 2025-01-27 · locator comment @antimora 2025-01-27T22:21:47Z — proposes a dedicated `SafeTensorFileRecorder` independent from the PyTorch recorder, with a configurable adapter (defaulting to PyTorchAdapter), to keep formats decoupled from the start. Quote: "I suggest creating a dedicated `SafeTensorFileRecorder` to handle SafeTensor files independently from PyTorch's `.pt` files." [`b-sb09-f002567-c1`, team b]
  - `dedicated-design-vs-duplicate-now--p2` — duplicate-now-refactor-later
    - **wandbrandon** · Source `f002567` · date 2025-01-28 · locator comment @wandbrandon 2025-01-28T02:40:30Z — copied the PyTorch recorder implementation wholesale into a new SafeTensors recorder as a base, planning cleanup later. Quote: "It's a lot of new files that are essentially copied code but with little adjustments." [`b-sb09-f002567-c2`, team b]
  - `dedicated-design-vs-duplicate-now--p3` — reduce-duplication-before-merge
    - **laggui** · Source `f002567` · date 2025-05-01 · locator comment @laggui 2025-05-01T15:11:57Z — argues the new SafeTensors doc section is nearly identical to the PyTorch one and questions whether keeping them as two separate sections adds value. Quote: "I'm not sure if there is actual value in the current state to have two sections, where the biggest difference is the file recorder used." [`b-sb09-f002567-c3`, team b]
    - **laggui** · Source `f002567` · date 2025-05-05 · locator comment @laggui 2025-05-05T14:00:50Z — objects to merging a large amount of test/example duplication with the intent to fix it later, given the PR's size. Quote: "I am not in favor of introducing such a big amount of duplication just to eventually fix it (or even worse, remain unchanged for longer)..." [`b-sb09-f002567-c4`, team b]
  - `dedicated-design-vs-duplicate-now--p4` — keep-separate-for-pragmatic-reasons
    - **antimora** · Source `f002567` · date 2025-05-02 · locator comment @antimora 2025-05-02T18:44:04Z — after an offline discussion, decided to keep PyTorch and SafeTensors doc sections separate (same format/language) rather than merge them now, calling it easier for the time being. Quote: "We discussed offline to keep two sections separate but have the same format and language between the two... For now it seems it's easier to have two." [`b-sb09-f002567-c5`, team b]
- Positions seen by the extractor (`b-sb09-f002567-q1`): dedicated-decoupled-recorder-from-the-start (antimora), duplicate-now-refactor-later (wandbrandon), reduce-duplication-before-merge (laggui)

### `dedicated-methods-vs-manual-composition`

**Question.** Should an API add a dedicated method for every composed operation (e.g. append/prepend a rotation) even when it gives no performance benefit over manual composition?

- Teams: a · members (context): `a-sB01-f000217-q5` (f000217, core)
- Domains: core
- Concepts: API-surface-minimalism; zero-cost-justification
- Positions:
  - `dedicated-methods-vs-manual-composition--p1` — omit methods with no perf benefit, compose manually
    - **Dimforge (nalgebra maintainers)** · Source `f000217` · date capture 2025-01-21 (Wayback; underlying doc undated) · locator "Computer-graphics recipes" chapter, note after "Homogeneous raw transformation matrix modification" table — Explains there is no append/prepend-rotation method because a dedicated method gives no performance benefit over building the rotation matrix and multiplying it in Quote: "That is because a specific method does not provide any performance benefit." [`a-sB01-f000217-c5`, team a]
- Positions seen by the extractor (`a-sB01-f000217-q5`): omit methods that add no perf benefit, compose manually instead

### `dedicated-test-for-overlapping-case`

**Question.** When a new macro feature's behavior largely overlaps existing generic tests, should reviewers ask for a dedicated test of the new case anyway, or is that redundant?

- Teams: a · members (context): `a-sR01-f000538-q2` (f000538, web)
- Domains: web
- Concepts: test coverage; proc-macro testing
- Positions:
  - `dedicated-test-for-overlapping-case--p1` — a new prop-label feature should get its own dedicated test even where the new code path overlaps generic behavior
    - **cecton** · Source `f000538` · date 2023-11-06 · locator PR #3509, comment 2023-11-06T14:58:24Z — asks the author to add a test covering `Option<AttrValue>` prop values specifically for the new dynamic-prop-label path. Quote: "Maybe you can add a test to make sure this case also works?" [`a-sR01-f000538-c2`, team a]
  - `dedicated-test-for-overlapping-case--p2` — a dedicated test for behavior already covered by more general, feature-independent tests is unnecessary
    - **kirillsemyonkin** · Source `f000538` · date 2023-11-06 · locator PR #3509, comment 2023-11-06T15:34:46Z — questions the value of the requested test, arguing optional-value handling is already exercised by tests not specific to dynamic props. Quote: "Optional values for properties are supposed to be already tested by more general tests that are not inherent to dynamic props." [`a-sR01-f000538-c3`, team a]
- Positions seen by the extractor (`a-sR01-f000538-q2`): "add a dedicated test for the new case" (cecton); "redundant — already covered by more general tests" (kirillsemyonkin)

### `dedupe-transitive-dependency-versions`

**Question.** Should a Rust library actively chase down and eliminate duplicate transitive dependency versions (e.g., two copies of `rustls`) in its dependency tree?

- Teams: a · members (context): `a-sR05-f001981-q2` (f001981, decentralized-iroh, core)
- Domains: core, decentralized-iroh
- Concepts: dependency management; crate ecosystem bloat; semver
- Positions:
  - `dedupe-transitive-dependency-versions--p1` — actively reduce duplicated transitive dependencies by upgrading
    - **matheus23 (iroh maintainer, n0)** · Source `f001981` · date 2024-09-04 · locator "🤝 Transitive dependencies" section — upgrading iroh's `quinn` dependency was valued because it let iroh drop duplicated copies of shared dependencies, shrinking its overall dependency footprint Quote: "we were generally able to reduce duplicated dependencies" [`a-sR05-f001981-c2`, team a]
- Positions seen by the extractor (`a-sR05-f001981-q2`): actively reduce duplication via upgrades

### `defensive-guards-for-unlikely-failures`

**Question.** how much defensive engineering (RAII/type-level guards) is warranted against a failure mode judged unlikely to occur in practice

- Teams: a · members (context): `a-sR14-f007341-q1` (f007341, web)
- Domains: web
- Concepts: none given
- Positions:
  - `defensive-guards-for-unlikely-failures--p1` — guard-even-theoretical-leaks
    - **Moss** · Source `f007341` · date 2026-02-09 · locator "Polish" section — worth adding an RAII (`Drop`-based) guard for a resource-leak path he judges may never actually occur, over leaving it unhandled — appeals to Value: correctness over minimal/pragmatic effort. Quote: "this is a problem in theory and may not ever occur in practice, but I figured it would be best to guard for this using some good old-fashioned RAII." [`a-sR14-f007341-c1`, team a]
- Positions seen by the extractor (`a-sR14-f007341-q1`): guard-even-theoretical-leaks (Moss)

### `defer-multithreaded-encoding`

**Question.** When a resource (a Metal command buffer/lock) needs coordinated access from multiple threads, should the implementation wait on the lock (with a timeout) now, or defer multithreaded encoding until single-threaded use has proven the design?

- Teams: b · members (context): `b-sb03-f000569-q1` (f000569, ml)
- Domains: ml
- Concepts: locking; multithreading; deadlocks; error handling
- Positions:
  - `defer-multithreaded-encoding--p1` — defer-multithreading-decision
    - **Narsil** · Source `f000569` · date 2023-12-15 · locator PR #1318, comment 2023-12-15T11:24:19Z — in multithreaded encoding we'd need to decide whether to wait on the lock with a timeout (since deadlocks could happen); okay with delaying that decision until the single-threaded implementation has proven its worth, since multithreaded command encoding doesn't yet show much benefit Quote: "I think I'm ok delaying this decision when the current implem for single threaded as proven it's worth" [`b-sb03-f000569-c1`, team b]
- Positions seen by the extractor (`b-sb03-f000569-q1`): defer-multithreading-decision

### `dependency-upgrade-regression-handling`

**Question.** When a transitive dependency upgrade trades one bug for another, should you pin to the older broken version, ship with the new regression, or hold the release?

- Teams: b · members (context): `b-sR04-f001749-q2` (f001749, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: dependency version pinning; semver upgrades; regression management
- Positions:
  - `dependency-upgrade-regression-handling--p1` — never-ship-a-known-crash-prefer-soft-guardrails
    - **emilk** · Source `f001749` · date 2024-07-23 · locator PR #4849, comment 2024-07-23T13:27:16Z — rejects shipping a version that always crashes on exit on macOS as a tradeoff; between that, shipping with a narrower crash on one feature path (with a guardrail steering users away from it), and blocking the release on an upstream fix, treats the always-crash option as off the table. Quote: "Having eframe always crash on exit on Mac is not an option imho." [`b-sR04-f001749-c2`, team b]
- Positions seen by the extractor (`b-sR04-f001749-q2`): never-ship-a-known-crash-prefer-soft-guardrails

### `dependency-version-requirement-width`

**Question.** How wide should a library's dependency version requirements be (e.g. serde `^1` vs a recent minimum)?

- Teams: b · members (context): `b-sT05-f003044-q2` (f003044, core)
- Domains: core
- Concepts: Cargo version requirements; dependency portability
- Positions:
  - `dependency-version-requirement-width--p1` — loosen serde requirement to `^1`
    - **pickfire** · Source `f003044` · date 2025-05-27 · locator comment 2025-05-27T17:05:52Z — subsecond's serde requirement blocked adding an axum hello-world example; asks for `^1` for portability with older serde Quote: "Can subsecond have serde being `^1` so that it can be more portable" (flag: voice-unverified) [`b-sT05-f003044-c2`, team b]
- Positions seen by the extractor (`b-sT05-f003044-q2`): loosen to `^1` for portability

### `deprecate-gradually-vs-break`

**Question.** When retiring a legacy compatibility path, should maintainers break it immediately or deprecate it gradually with warnings?

- Teams: b · members (context): `b-sR11-f005050-q2` (f005050, wasm)
- Domains: wasm
- Concepts: breaking changes; deprecation policy; semver
- Positions:
  - `deprecate-gradually-vs-break--p1` — a deprecated compatibility shim (WAGI) should be phased out with warnings and migration time, not removed outright
    - **The Spin Project** · Source `f005050` · date 2026-08-26 · locator "A heads-up on WAGI" section — 4.1 starts printing deprecation warnings and drops WAGI examples from the repo, but existing WAGI components keep running Quote: "this is the start of a gradual, managed deprecation, not a break" [`b-sR11-f005050-c2`, team b]
- Positions seen by the extractor (`b-sR11-f005050-q2`): gradual, warned deprecation over an immediate break

### `deref-delegation-vs-accessors`

**Question.** Should a Rust API expose one type's methods through another via `Deref` (delegation by deref), or through explicit accessor methods?

- Teams: b · members (context): `b-sT04-f001890-q1` (f001890, core, decentralized-iroh)
- Domains: core, decentralized-iroh
- Concepts: Deref-based delegation; API structure; accessor methods; breaking changes
- Positions:
  - `deref-delegation-vs-accessors--p1` — drop Deref delegation for explicit accessors
    - **n0, inc. / iroh team (post by ramfox)** · Source `f001890` · date 2024-08-21 · locator § "Letting net stand on its own"; § Breaking Changes > API Changes > iroh, first bullet — The release pulls the networking methods out of the node methods, so users now call `node.net().node_addr()` instead of `node.node().node_addr()`. It lists "No more deref of iroh::net::Client to iroh::client::node::Node" as a breaking change, replacing the earlier deref-based grouping. The stated reason is to let net "stand on its own". The Voice's Rust connection is shown in the source: the post is written by the maintainers of the Rust crates iroh, iroh-net and iroh-blobs and includes Rust code. Quote: "No more deref of iroh::net::Client to iroh::client::node::Node" (flag: voice-unverified) [`b-sT04-f001890-c1`, team b]
- Positions seen by the extractor (`b-sT04-f001890-q1`): drop Deref, use explicit accessor `node.net()` (n0/iroh)

### `desktop-webview-ipc-vs-single-context`

**Question.** For a Rust desktop app that needs a web-capable UI, should the frontend logic stay in the same Rust execution context as the backend (Dioxus-style, calling straight into the WebView glue), or should it run as an independent frontend runtime talking to a host process over a serialized IPC boundary (Tauri's architecture)?

- Teams: b · members (context): `b-sb21-f008390-q1` (f008390, desktop-cli-ui, frontend)
- Domains: desktop-cli-ui, frontend
- Concepts: Diet Electron; WebView2/WebKitGTK; wasm-bindgen IPC; split-brain architecture; compile-time type safety
- Positions:
  - `desktop-webview-ipc-vs-single-context--p1` — reject-split-brain-untyped-ipc
    - **boringcactus (Melody)** · Source `f008390` · date 2025-04-16 · locator § "Tauri" — Tauri's host-process/WebView split forces an IPC boundary where frontend calls take an untyped `&str` command name and `JsValue` args, so a field rename on the host side fails only at runtime instead of compile time; combined with the architectural split this made the author "genuinely hate" the design Quote: "Half the point of Rust is the sheer quantity of bugs that it can catch at compile time, and if your IPC is just tossing strings around and praying at runtime, you may as well be just writing vanilla JavaScript." [`b-sb21-f008390-c1`, team b]
- Positions seen by the extractor (`b-sb21-f008390-q1`): reject-split-brain-untyped-ipc (boringcactus / Melody), single-execution-context-preferred (boringcactus / Melody, re: Dioxus)

### `divergent-signature-for-forever-tasks`

**Question.** Should a long-running/background task use a divergent (`-> !`) function signature rather than one that returns?

- Teams: a · members (context): `a-sB04-f000227-q3` (f000227, embedded)
- Domains: embedded
- Concepts: divergent-task-signature; 'static-context; run-forever-tasks
- Positions:
  - `divergent-signature-for-forever-tasks--p1` — prefer-divergent-signature-for-run-forever-tasks
    - **RTIC developers** · Source `f000227` · date undated (living doc, v2.x) · locator "2.3. Software tasks & spawn", "Divergent tasks" — Recommends the `-> !` (divergent) task signature for tasks meant to run forever, because it grants a 'static context/local-resource lifetime and makes the run-forever intent explicit versus a normal returning signature Quote: "The key advantage of divergent tasks is that they receive a 'static context, and local resources have 'static lifetime." [`a-sB04-f000227-c3`, team a]
- Positions seen by the extractor (`a-sB04-f000227-q3`): prefer-divergent-signature-for-run-forever-tasks

### `docs-as-rust-vs-markdown`

**Question.** When migrating a documentation/blog site's content out of a JS-based static-site generator's Markdown-derivative format, should the content be authored directly as Rust source (a DSL enabling compile-time link validation and cross-version deduplication) or kept close to Markdown for editor tooling and authoring ergonomics, with a lighter embedding mechanism for interactive components?

- Teams: b · members (context): `b-sb14-f004399-q1` (f004399, web, frontend, wasm)
- Domains: frontend, wasm, web
- Concepts: documentation-as-code; compile-time validated links; editor/tooling support; macros; MDX
- Positions:
  - `docs-as-rust-vs-markdown--p1` — docs-as-rust-source-for-compile-time-checks-and-dedup
    - **Madoshakalaka** · Source `f004399` · date 2026-03-11 · locator PR description @Madoshakalaka 2026-03-11T10:47:39Z — rewrote the docs site's content as Rust source instead of MDX, citing compile-time-validated internal/external doc links and data-as-code deduplication across doc versions as the payoff. Quote: "We have compile-time validated doc links that go through the spa router... Data-as-code allows us to deduplicate greatly." [`b-sb14-f004399-c1`, team b]
    - **Madoshakalaka** · Source `f004399` · date 2026-04-09 · locator comment @Madoshakalaka 2026-04-09T14:21:28Z — concedes WorldSEnder's concern is valid and agrees to research whether Markdown-based authoring can be preserved. Quote: "I can get behind this sentiment. Valid concerns. I'll do some research on mdx parsers and see if we can achieve the same thing with minimal edits to the mdx files." [`b-sb14-f004399-c3`, team b]
  - `docs-as-rust-vs-markdown--p2` — keep-markdown-for-authoring-ergonomics
    - **WorldSEnder** · Source `f004399` · date 2026-04-09 · locator comment @WorldSEnder 2026-04-09T14:02:40Z — objects to fully replacing MDX docs with Rust source, arguing the magic macros are a barrier to writing content and that ordinary editor/language tooling understands Markdown but not this Rust DSL. Quote: "I would not want to write a blog post in this format, I would want to write the markdown where this came from... my editor understands markdown more or less, it does not understand this." [`b-sb14-f004399-c2`, team b]
  - `docs-as-rust-vs-markdown--p3` — downgrade-to-plain-markdown-plus-custom-component-delimiters
    - **Madoshakalaka** · Source `f004399` · date 2026-04-11 · locator comment @Madoshakalaka 2026-04-11T08:52:48Z — after researching mdx-capable crates, decides to drop mdx/Rust-source authoring in favor of plain Markdown with a custom comment-delimiter convention for embedding Yew components. Quote: "I think we should downgrade all our mdx to plain markdown files. And invent our own way to embed Yew components instead." [`b-sb14-f004399-c4`, team b]
- Positions seen by the extractor (`b-sb14-f004399-q1`): docs-as-rust-source-for-compile-time-checks-and-dedup (Madoshakalaka, initial design), keep-markdown-for-authoring-ergonomics (WorldSEnder), downgrade-to-plain-markdown-plus-custom-component-delimiters (Madoshakalaka, revised after feedback)

### `doctests-must-compile`

**Question.** Should code blocks embedded in Rust doc comments be required to compile as doctests, or is it acceptable to leave illustrative snippets non-compiling?

- Teams: a · members (context): `a-sR07-f002347-q1` (f002347, core)
- Domains: core
- Concepts: doctests; documentation conventions
- Positions:
  - `doctests-must-compile--p1` — require-all-blocks-to-compile
    - **BD103** · Source `f002347` · date 2024-12-17 · locator comment on CI failures (2024-12-17T17:43:35Z) — Bevy's convention requires every doc-comment code block to be valid, compiling Rust because the project treats them as unit tests too Quote: "We require all code blocks to be valid Rust, since we treat them as unit tests as well." [`a-sR07-f002347-c1`, team a]
- Positions seen by the extractor (`a-sR07-f002347-q1`): require-all-blocks-to-compile (BD103)

### `downstream-vendor-removed-api-vs-rework`

**Question.** When a library removes a public API in a major release, should downstream vendor the removed piece or rework its integration, and does the migration cost count against the removal?

- Grouping: Singleton. Strikes b28 and b29 (answering a different decision than release sequencing) are re-homed here; merge-v2 had already linked them to this Question, the second one in their source.
- Teams: b · members (context): `b-sT07-f003809-q2` (f003809, core, distributed)
- Domains: core, distributed
- Concepts: breaking changes; semver majors; vendoring; downstream migration cost
- Positions:
  - `downstream-vendor-removed-api-vs-rework--vendor-removed-trait` — Replicate the dropped trait downstream as a fallback (a tentative plan; b28's second strike ground)
    - **comphead** · Source `f003809` · date 2026-01-06 · locator comments 2026-01-06T17:13:01Z, 2026-01-06T17:30:28Z — the SchemaAdapter removal lengthens Comet's upgrade; plan B is to copy SchemaAdapter into the Comet codebase Quote: "plan B is to replicate SchemaAdapter in Comet codebase" (flag: voice-unverified) [`b-sT07-f003809-c3`, team b]
  - `downstream-vendor-removed-api-vs-rework--rework-downstream` — Rework downstream; the cost falls on downstream's own misuse
    - **adriangb** · Source `f003809` · date 2026-01-06 · locator comment 2026-01-06T17:17:48Z — Pydantic was hit by the same removal, but because of its own hacky dynamically generated columns filled by SchemaAdapter; offers to work through issues Quote: "that's mostly on us for doing *horrifying* things in the first place" (flag: voice-unverified) [`b-sT07-f003809-c4`, team b]
- Positions seen by the extractor (`b-sT07-f003809-q2`): replicate the dropped trait in the downstream codebase as fallback; rework, the cost is on downstream's own hacky use

### `durable-job-queue-vs-in-process`

**Question.** Should scheduled or background jobs in a Rust service run on a durable, database-backed job queue (e.g. apalis with Postgres storage) or on an in-process scheduler whose jobs live only in memory?

- Teams: b · members (context): `b-sT09-f011688-q1` (f011688, web, cloud-workers)
- Domains: cloud-workers, web
- Concepts: apalis; PostgresStorage; cron; tower service layers; retry
- Positions:
  - `durable-job-queue-vs-in-process--p1` — durable Postgres-backed job queue
    - **Joshua Mo (Shuttle)** · Source `f011688` · date 2024-01-23 · locator § Hooking it all up, paragraph 1 — PostgresStorage is set up so the job queue is durable, with the reason that jobs would otherwise be lost when the service has an outage Quote: "Without durable job queues, our jobs would disappear if our web service has any outages!" (flag: voice-unverified) [`b-sT09-f011688-c1`, team b]
- Positions seen by the extractor (`b-sT09-f011688-q1`): durable Postgres-backed queue

### `dyn-compatibility-rules-relaxation`

**Question.** How constrained are `dyn Trait`'s object-safety rules, and how likely/soon could they be relaxed (e.g., via higher-ranked generic bounds or a next-generation trait solver)?

- Teams: a · members (context): `a-sa30-f013276-q4` (f013276, core)
- Domains: core
- Concepts: object safety; dyn compatibility; trait solver; higher-ranked bounds
- Positions:
  - `dyn-compatibility-rules-relaxation--p1` — dyn-trait-relaxation-for-this-case-is-far-off-or-never
    - **quinedot — track record not established from this source** · Source `f013276` · date 2024-12-06 · locator post 2024-12-06T01:21:37.914Z — sketches a hypothetical higher-ranked-bound `dyn EventStore` that would satisfy the OP's use case, then predicts it is not close, if it ever lands Quote: "But we're talking years and years, if ever; probably the dyn equivalent isn't plausible." [`a-sa30-f013276-c1`, team a]
  - `dyn-compatibility-rules-relaxation--p2` — dyn-trait-object-safety-rules-are-overly-constraining
    - **parasyte — track record not established from this source** · Source `f013276` · date 2024-12-06 · locator post 2024-12-06T05:54:27.164Z — expresses pessimism that `dyn Trait`'s object-safety constraints can be substantially relaxed, noting the trait-resolver rewrite ("next-gen trait solver") has been underway since 2015 Quote: "I am pessimistic on the outlook of dyn Trait, though. The rules are too constraining and I don't know if it's possible to lift many of them." [`a-sa30-f013276-c5`, team a]
- Positions seen by the extractor (`a-sa30-f013276-q4`): "the rules are too constraining, and it's unclear whether they can be lifted; a dyn-compatible fix for cases like the OP's is 'years and years, if ever' away" (parasyte, quinedot) — single-sided in this source

### `dynamic-ecs-component-typed-id`

**Question.** Should runtime-registered ("dynamic") ECS components carry a compile-time type witness (a typed ID wrapper constrained to `T: Component`) for safe access, or stay untyped so that scripting/runtime-defined component variants aren't forced into newtyping?

- Teams: a · members (context): `a-02-f001231-q1` (f001231, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: ECS; dynamic typing; phantom types; unsafe code
- Positions:
  - `dynamic-ecs-component-typed-id--p1` — typed-wrapper-for-safety
    - **ecoskey** · Source `f001231` · date 2024-03-30 · locator PR description ("Objective"/"Solution") — proposes wrapping dynamic `ComponentId`s in a typed `TypedComponentId<T>` witness so dynamic component access can be done safely, instead of manual pointer work and unsafe code Quote: "Add a wrapper around ComponentId with a type parameter T to act as a witness that that id corresponds to a component with type T. This allows registering multiple components with the same underlying type, that dynamic queries can access separately in a safe way." [`a-02-f001231-c1`, team a]
- Positions seen by the extractor (`a-02-f001231-q1`): typed-witness-wrapper (PR author), untyped-for-flexibility (reviewer, unattributed)

### `easy-mode-rust`

**Question.** When onboarding a team new to Rust on a security-critical project, should you write "easy mode Rust" (owned types instead of borrowed references, `Arc<RwLock<T>>` instead of lock-free structures) to keep the team approachable, or go straight for the most advanced/performant Rust idioms?

- Teams: b · members (context): `b-sb24-f011295-q1` (f011295, web, distributed, core)
- Domains: core, distributed, web
- Concepts: easy mode Rust; owned vs. borrowed types; Arc<RwLock<T>>; lock-free data structures; borrow checker onboarding cost
- Positions:
  - `easy-mode-rust--p1` — tasteful-combination-favoring-easy-mode
    - **Sam Cutter** · Source `f011295` · date 2025-10-03 · locator [12:09]-[13:10] — as the first Rust team at the Guardian, they deliberately avoided the most advanced/fastest Rust (lifetimes-heavy, lock-free structures) in favor of owned types and `Arc<RwLock<T>>`, to minimize borrow-checker friction for engineers new to Rust, while keeping the option to refactor toward performance later Quote: "In practice, this means instead of strrus containing references to other objects, we prefer our strs to be have owned types. This minimizes borrow checker headaches." [`b-sb24-f011295-c1`, team b]
- Positions seen by the extractor (`b-sb24-f011295-q1`): tasteful-combination-favoring-easy-mode (Sam Cutter, citing Andre Bergus's "easy mode Rust" framing from Rust Nation 2024)

### `ecs-events-first-architecture`

**Question.** In a growing Bevy/ECS game, should cross-system state changes flow through an events/observers-first architecture (systems never mutate each other's state directly) rather than direct shared mutable access, accepting the loss of transactional rollback and added boilerplate in exchange for decoupling?

- Teams: b · members (context): `b-sb25-f012561-q1` (f012561, other)
- Domains: other
- Concepts: Bevy ECS; events; observers/triggers; system ordering; atomicity
- Positions:
  - `ecs-events-first-architecture--p1` — build state changes as an events/observers cascade rather than direct system-to-system mutation, despite losing atomicity
    - **Tristan (solo Rust/Bevy game developer, "Green Fit Heaven")** · Source `f012561` · date 2025-06-18 · locator ~06:10-09:13 — modeling every state change (granting XP, playing a sound, updating a tile) as a hierarchy of events made each system easy to reason about in isolation and easy to reuse, at the cost that a failure partway through a cascade can't be rolled back, so every handler has to defensively stop propagation and keep the game in a stable state Quote: "it breaks atomicity ... if something fails ... you can't roll back the previous event" [`b-sb25-f012561-c1`, team b]
- Positions seen by the extractor (`b-sb25-f012561-q1`): go all-in on events, then migrate most of them to the newer observer/trigger primitive once available, because it guarantees same-frame execution and untangles ordering, versus the cost that a failed step in an event cascade can't be rolled back and every handler must defensively contain its own failures

### `ecs-relationship-fragmenting`

**Question.** Should ECS relationships be stored as archetype-fragmenting edges (entities with different relationship targets end up in different archetypes, enabling wildcard/nested-join/traversal query operations), or as non-fragmenting components (all related entities can share the same archetype/table, favoring dense cache-friendly iteration for common hierarchical cases)?

- Teams: b · members (context): `b-sb07-f002142-q2` (f002142, other)
- Domains: other
- Concepts: ECS; archetype fragmentation; query operations; cache-friendly iteration; hierarchy traversal
- Positions:
  - `ecs-relationship-fragmenting--p1` — fragmenting-enables-more-queries
    - **iiYese** · Source `f002142` · date 2024-10-20 · locator PR #15635, comment 2024-10-20T11:38:42Z — lists concrete query operations (wildcard queries, named wildcard queries, nested joins, efficient up-traversal, efficient sibling queries) that are only possible when relationship edges are exposed at the archetype level, which this PR's component-based (non-fragmenting) approach does not provide Quote: "You cannot do many query operations when edge information is not exposed at an archetype level." [`b-sb07-f002142-c3`, team b]
  - `ecs-relationship-fragmenting--p2` — non-fragmenting-preferred-for-hierarchies
    - **nakedible** · Source `f002142` · date 2024-10-20 · locator PR #15635, comment 2024-10-20T08:31:44Z — states that fragmenting relationships would be useless for their use case and would just produce one archetype per entity, whereas the non-fragmenting, relationship-type-keyed approach in this PR is what they actually need (and reports that a Bevy ECS SME independently suggested the same to them) Quote: "Fragmenting relationships are totally useless for my use cases, and will just lead to one archetype per entity." [`b-sb07-f002142-c4`, team b]
- Positions seen by the extractor (`b-sb07-f002142-q2`): fragmenting-enables-more-queries, non-fragmenting-preferred-for-hierarchies

### `ecs-relationship-source-of-truth`

**Question.** For an ECS relationship system, should the design enforce a single source of truth (only the `Relationship` component is authoritative, the reflected `RelationshipTarget` collection can't be populated directly), accepting that constraint in exchange for O(1) inserts and no runtime duplicate-scanning, or should both sides carry equal, symmetric authority for more flexibility at the cost of scanning/hashing to prevent duplicates?

- Teams: a · members (context): `a-sa04-f002554-q1` (f002554, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: ECS; relationships; source of truth; API surface; performance
- Positions:
  - `ecs-relationship-source-of-truth--p1` — single-source-of-truth-relationship
    - **cart** · Source `f002554` · date 2025-01-16 · locator PR description, "Relationships are the source of truth" section — argues `Relationship` should be the sole source of truth so `RelationshipTarget` is a pure reflection, accepting that populated target collections can't be spawned directly, in exchange for O(1) inserts and no runtime duplicate-scanning; contrasts this with a symmetric two-sided design (`evergreen_relations`) that needs scanning/hashing to prevent duplicates Quote: "We can rely on component lifecycles to protect us against duplicates, rather than needing to scan at runtime to ensure entities don't already exist (which results in quadratic runtime)." [`a-sa04-f002554-c1`, team a]
- Positions seen by the extractor (`a-sa04-f002554-q1`): single-source-of-truth (PR author), symmetric-source-of-truth (contrasted `evergreen_relations` approach, same source)

### `ecs-relationship-type-level-exclusivity`

**Question.** Should an ECS's relationship "edge" components be public types with the exclusivity (one-to-one, one-to-many, many-to-many, ...) encoded at the type level for compile-time correctness and ergonomics, or should the edge-storing components be private (mutable only via commands/hooks) with a single consistent query API regardless of exclusivity?

- Teams: b · members (context): `b-sb07-f002142-q1` (f002142, other)
- Domains: other
- Concepts: ECS; relationships; type-level invariants; component visibility; query ergonomics
- Positions:
  - `ecs-relationship-type-level-exclusivity--p1` — type-level-exclusivity-public
    - **bushrat011899** · Source `f002142` · date 2024-10-20 · locator PR #15635, comment 2024-10-20T08:31:44Z — prefers public edge components whose type encodes the relationship's exclusivity (one-to-many derefs to `Entity`, many-to-one to `[Entity]`), because it makes incorrect usage fail to compile, improves error messages, and keeps the model close to what `Parent`/`Children` already are for users and for reflection/scene formats (BSN/`ron`) Quote: "I believe it is nicer that the type has a different interface based on the exclusivity - it makes the difference explicit in code, and incorrect usage not compile" [`b-sb07-f002142-c1`, team b]
  - `ecs-relationship-type-level-exclusivity--p2` — private-edges-runtime-consistency
    - **iiYese** · Source `f002142` · date 2024-10-20 · locator PR #15635, comment 2024-10-20T10:57:04Z — argues type-level exclusivity is not even correct (an entity can still hold both `OneToOne<R>` and `OneToMany<R>`) and forces every query site to know and restate the edge shape; consistency of one query API matters more than having the option Quote: "Consistency is more important here than options... Being at a type level is not a benefit it is the option." [`b-sb07-f002142-c2`, team b]
- Positions seen by the extractor (`b-sb07-f002142-q1`): type-level-exclusivity-public, private-edges-runtime-consistency

### `ecs-ui-large-vs-small-systems`

**Question.** For complex UI built on an ECS with an immediate-mode UI library (egui), should you write large systems with many queries in one place (simpler control flow, but they frequently deadlock against the borrow checker), or split into many small per-widget systems (fewer conflicts per system, but requires repeated manual world/state access that itself risks borrow-checker errors)?

- Teams: b · members (context): `b-sb25-f012561-q3` (f012561, other)
- Domains: other
- Concepts: egui; ECS UI systems; borrow checker; widget-system pattern
- Positions:
  - `ecs-ui-large-vs-small-systems--p1` — still actively fighting the borrow checker over how to split large UI systems, with no settled solution
    - **Tristan** · Source `f012561` · date 2025-06-18 · locator ~19:24-20:26 — his large "god" UI systems with dozens of queries are simple to write but constantly conflict with the borrow checker; he tried a widget-per-system pattern proposed by another user in a GitHub discussion, which helps isolate systems but forces repeated manual `get_mut::<State>`/`get_mut::<World>` calls that themselves risk borrow errors — he calls it "an ongoing problem," not resolved Quote: "it's an ongoing problem for me, it's not ... deadly ... but it's an ongoing problem" [`b-sb25-f012561-c3`, team b]
- Positions seen by the extractor (`b-sb25-f012561-q3`): split into a widget-per-system pattern proposed in a GitHub discussion, still fighting the borrow checker on it and treating the problem as unsolved rather than settled

### `embedded-crash-policy-kernel-vs-supervisor`

**Question.** In an embedded OS kernel, should crash-recovery policy (restart strategy, backoff, giving up) be hardcoded into the kernel, or left to an application-defined supervisor task?

- Teams: a · members (context): `a-sa17-f008217-q1` (f008217, embedded)
- Domains: embedded
- Concepts: fault handling; kernel/task boundary; IPC
- Positions:
  - `embedded-crash-policy-kernel-vs-supervisor--p1` — policy-in-userspace-supervisor-not-kernel
    - **Cliff L. Biffle** · Source `f008217` · date 2024-12-14 · locator § "The role of the supervisor in Hubris" — Hubris's kernel deliberately does not hardcode a crash-restart policy (immediate restart, backoff, giving up); it only records the fault and notifies a userspace supervisor task, leaving the recovery policy to the application programmer because the correct policy depends on context. Quote: "My conclusion is that there is no right answer to this question... So, Hubris leaves it up to you, the programmer." [`a-sa17-f008217-c1`, team a]
- Positions seen by the extractor (`a-sa17-f008217-q1`): policy-in-userspace-supervisor-not-kernel

### `embedded-deferred-log-formatting`

**Question.** In embedded/no_std logging, should you format and print human-readable strings at the point of use, or defer formatting to the host by sending compact binary tokens and decoding off-device?

- Teams: a · members (context): `a-sa14-f005162-q1` (f005162, embedded)
- Domains: embedded
- Concepts: embedded logging; deferred formatting; defmt
- Positions:
  - `embedded-deferred-log-formatting--p1` — deferred/binary logging over on-device string formatting
    - **Ferrous Systems (Jonathan)** · Source `f005162` · date 2025-03-11 · locator § Rust for Microcontrollers — measures the same log line implemented via `rprintln!` (1675 instructions, converts f32 to string on-device) against `defmt::info!` (1050 instructions, sends the raw value plus a format-string ID) and generalizes that more efficient logging lets you log more for the same time/power cost Quote: "the more efficient your logging, the more you can log for a given cost in terms of time and power, so this kind of saving soon adds up!" [`a-sa14-f005162-c1`, team a]
- Positions seen by the extractor (`a-sa14-f005162-q1`): defer to compact binary/deferred-formatting logging (defmt) over on-device string formatting (`rprintln!`/`core::fmt::Write`), because it costs measurably fewer instructions per log call

### `embedded-framework-bundles-hal-and-executor`

**Question.** Should an embedded Rust concurrency solution bundle its own HAL and executor (batteries-included), or stay a framework-only layer that leaves HAL/PAC to the user and favors hardware-level resource exclusivity over software locking?

- Teams: a · members (context): `a-sB04-f000227-q5` (f000227, embedded)
- Domains: embedded
- Concepts: framework-scope; HAL-bundling; hardware-guarded-exclusivity
- Positions:
  - `embedded-framework-bundles-hal-and-executor--p1` — RTIC: framework-only, hardware-level exclusivity where possible; named alternative: Embassy bundles HAL + executor
    - **RTIC developers** · Source `f000227` · date undated (living doc, v2.x) · locator "5. RTIC and Embassy", "Differences" — States Embassy provides both a HAL and an executor/runtime (e.g. embassy-stm32, embassy-executor) while RTIC aims to provide only the execution framework, leaving PAC/HAL to the user (typically stm32-rs); RTIC additionally aims to give exclusive resource access as low-level as possible, ideally hardware-guarded, to avoid needing software-level locking Quote: "RTIC aims to provide exclusive access to resources at as low a level as possible, ideally guarded by some form of hardware protection." [`a-sB04-f000227-c5`, team a]
- Positions seen by the extractor (`a-sB04-f000227-q5`): RTIC: framework-only, hardware-level exclusivity where possible; named alternative: Embassy bundles HAL + executor

### `embedded-interpreter-stopgap`

**Question.** When a needed capability (like `eval`) isn't natively supported by the host platform, is it acceptable to run a full interpreter for that capability inside your own Rust-compiled Wasm module as a stopgap, even though it means "a runtime on top of a runtime"?

- Teams: a · members (context): `a-sa14-f004985-q2` (f004985, wasm, cloud-workers)
- Domains: cloud-workers, wasm
- Concepts: embedded interpreters; platform capability gaps; pragmatic tradeoffs
- Positions:
  - `embedded-interpreter-stopgap--p1` — embedded Rust interpreter as an acceptable stopgap for a missing platform capability
    - **Celso Martinho, Ruskin Constant, Rui Figueira, and Luís Duarte** · Source `f004985` · date 2026-08-06 · locator § How we built it / Yes, but evals — explain they use Boa (a Rust-implemented ECMAScript engine) to handle `eval` since Workers doesn't support it natively and a second isolate wouldn't share `globalThis`, calling the approach non-optimal but workable until native support lands Quote: "We are basically executing a runtime on top of a runtime, which doesn't seem optimal, and it isn't, but it works well enough" [`a-sa14-f004985-c2`, team a]
- Positions seen by the extractor (`a-sa14-f004985-q2`): use a Rust-implemented JS engine (Boa) as a temporary embedded interpreter until native eval support lands on the host platform, accepting the extra layer as good enough for now

### `embedded-panics-compile-time-vs-recovery`

**Question.** In safety/crash-sensitive embedded Rust, should panics be eliminated for a given task at compile time, or tolerated and handled via runtime crash recovery?

- Teams: a · members (context): `a-sa17-f008217-q2` (f008217, embedded)
- Domains: embedded
- Concepts: panics; no_std; embedded; compile-time guarantees
- Positions:
  - `embedded-panics-compile-time-vs-recovery--p1` — compile-time-no-panic-for-the-one-critical-task
    - **Cliff L. Biffle** · Source `f008217` · date 2024-12-14 · locator § "Who supervises the supervisor?" — Because nothing restarts the supervisor task itself if it crashes, recommends compiling it with userlib's no-panic feature so any unoptimized-away panic becomes a link failure, catching a whole class of crashes at compile time for that one task rather than relying on runtime recovery (which has no one above it). Quote: "This provides a way to ensure, at compile time, that a task cannot panic." [`a-sa17-f008217-c2`, team a]
- Positions seen by the extractor (`a-sa17-f008217-q2`): compile-time-no-panic-for-the-one-critical-task (supervisor), runtime-recovery-for-ordinary-tasks

### `emscripten-vs-native-rust-wasm`

**Question.** When compiling C/C++/Rust code to WebAssembly for a serverless runtime, should you go through an emulation layer like Emscripten, or compile natively from Rust straight to Wasm?

- Teams: a · members (context): `a-sa14-f004985-q1` (f004985, wasm, cloud-workers)
- Domains: cloud-workers, wasm
- Concepts: Wasm compilation strategy; emulation layers; wasm-bindgen
- Positions:
  - `emscripten-vs-native-rust-wasm--p1` — native Rust-to-Wasm over an Emscripten emulation layer
    - **Celso Martinho, Ruskin Constant, Rui Figueira, and Luís Duarte** · Source `f004985` · date 2026-08-06 · locator § Design decisions / Use Rust when possible — explain that Emscripten's mocked-dependency layers make compiled binaries bulky and slow, so they chose native Rust compiled directly to Wasm via wasm-bindgen instead Quote: "Instead, we opted for native Rust whenever possible and to compile directly to WebAssembly using wasm-bindgen, thus avoiding unnecessary emulation layers" [`a-sa14-f004985-c1`, team a]
- Positions seen by the extractor (`a-sa14-f004985-q1`): skip Emscripten's mocked-dependency emulation layer and compile native Rust to Wasm directly via wasm-bindgen, for a smaller and faster binary

### `emulate-specialization`

**Question.** when a type needs specialization-like behavior (methods gated on stronger trait bounds, e.g. `Read+Write+Seek` vs `Read+Seek`) but Rust's real specialization is unstable, do you fake it with a runtime-checked field set from trait-bound-gated impl blocks, or reach for a different pattern entirely?

- Teams: b · members (context): `b-sb20-f007213-q1` (f007213, core)
- Domains: core
- Concepts: specialization; trait bounds; generics over storage traits
- Positions:
  - `emulate-specialization--p1` — single-constructor design with an `Option<SyncFn>` field toggled from trait-bound-gated impl blocks, replacing separate RO/RW constructors
    - **Oakchris1955** · Source `f007213` · date 2025-07-26 · locator section "The solution" — instead of two constructors (one for read-only, one for read-write), keep one constructor and one `sync_fn` field defaulted to `None`; only impls bound on `Read + Write + Seek` can set it to `Some`, which fixes a bug where RWFile writes silently failed to sync Quote: "Instead of using 2 constructors, one for a RO filesystem and another for a R/W filesystem, we use one for both cases." [`b-sb20-f007213-c1`, team b]
- Positions seen by the extractor (`b-sb20-f007213-q1`): runtime-checked optional field (`sync_fn: Option<SyncFn>`) set only from impls gated on the stronger bound, single constructor for both RO/RW cases (Oakchris1955)

### `enum-glob-import-in-match`

**Question.** should match arms on an enum use a local glob import (`use Enum::*;`) to drop the type-qualified path, or keep variants fully qualified?

- Teams: b · members (context): `b-sR03-f000763-q3` (f000763, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: none given
- Positions:
  - `enum-glob-import-in-match--p1` — favors the local glob import for terser match arms.
    - **joshka** · Source `f000763` · date 2024-01-18 · locator ratatui/ratatui#840, comment 2024-01-18T01:32:39Z. · L125-L136. — favors the local glob import for terser match arms. Quote: "And add a `use KeyCode::*;` above this (inside the method) to drop the `Keycode::` from each." [`b-sR03-f000763-c3`, team b]
- Positions seen by the extractor (`b-sR03-f000763-q3`): favors the local glob import for terser match arms. (joshka)

### `epoll-vs-io-uring`

**Question.** For a hand-built async I/O reactor on Linux, should you build the readiness-notification layer on `epoll` (mature, stable) or on `io_uring` (newer, potentially faster but more experimental)?

- Teams: b · members (context): `b-sb21-f008396-q1` (f008396, core)
- Domains: core
- Concepts: epoll; io_uring; Waker; reactor thread; readiness-based I/O
- Positions:
  - `epoll-vs-io-uring--p1` — epoll-for-now-as-the-standard-tradeoff
    - **Natalie Klestrup Röijezon (natkr)** · Source `f008396` · date 2025-04-16 · locator footnote 9 (§ "Sleepy I/O") — chooses epoll for the tutorial's reactor because it hits the "standard" balance of being neither too slow nor too experimental, while noting io_uring might take over that role "in a few years" Quote: "Not the only API, there are others. But it's the one that hits the 'standard' tradeoff between not being too slow or too experimental." [`b-sb21-f008396-c1`, team b]
- Positions seen by the extractor (`b-sb21-f008396-q1`): epoll-for-now-as-the-standard-tradeoff (Natalie Klestrup Röijezon / natkr)

### `ergonomic-sugar-now-or-later`

**Question.** When shipping a small utility feature quickly, is it worth adding ergonomic sugar (a macro/trait wrapper) around the raw mechanism, or should that wait until it's shown to carry its weight?

- Teams: a · members (context): `a-sa11-f004512-q3` (f004512, embedded)
- Domains: embedded
- Concepts: API polish investment; YAGNI; incremental delivery
- Positions:
  - `ergonomic-sugar-now-or-later--p1` — ship the minimal raw mechanism now, add sugar only once it earns it
    - **bugadani** · Source `f004512` · date 2026-04-01 · locator comment 2026-04-01T20:16:11Z — acknowledges the PR was assembled quickly and says a macro/trait wrapper could be added for syntactic sugar later, but sees little reason to do it now Quote: "This PR was thrown together in 15 minutes. Whether this will be good enough or not, time will tell. We can add a macro and a trait to dress this up as a plugin, but there's very little reason to do that except for some syntactic sugar." [`a-sa11-f004512-c4`, team a]
- Positions seen by the extractor (`a-sa11-f004512-q3`): ship the raw low-level form now; add a macro/trait for sugar only if there's a real reason, since a quickly-assembled PR's sufficiency is not yet proven

### `ergonomics-vs-explicitness`

**Question.** Should Rust favor implicit ergonomic sugar (the 2017 "ergonomics initiative", e.g. match ergonomics) even where it costs the language's own stated core value of explicitness, or hold the line on explicitness?

- Teams: a · members (context): `a-sa28-f012469-q5` (f012469, core)
- Domains: core
- Concepts: explicitness; ergonomics; match ergonomics; core values
- Positions:
  - `ergonomics-vs-explicitness--p1` — explicitness-is-an-unstated-core-value
    - **Ian Whitney (blog post "Rust via its Core Values," cited independently twice, two years apart, by different posters — circumstantial evidence of being a genuinely referenced source)** · Source `f012469` · date blog post undated in source; cited 2016-04-03 and again 2018-04-25 · locator post by @nayru25 dated 2016-04-03T00:20:55Z; re-cited by @cg-cnu dated 2018-04-25T09:01:38Z — identifies explicitness as one of Rust's de facto core values despite it never being explicitly written down as a goal Quote: "Explicitness is the fourth core value of Rust. Ironically, I don't see that 'Explicitness' is ever explicitly stated as a goal of Rust." [`a-sa28-f012469-c9`, team a]
  - `ergonomics-vs-explicitness--p2` — ergonomics-initiative-RFCs-are-knowingly-controversial
    - **aturon (Aaron Turon, Rust language-design team)** · Source `f012469` · date 2017-08-31 · locator post by @MaloJaffre dated 2017-08-31T19:26:05Z, sourced "Aturon about ergonomics initiative RFCs" — self-aware acknowledgment that the 2017 ergonomics-initiative RFCs (pushing implicit sugar into hard-to-write corners) are controversial and will need walking back Quote: "Anywhere your code is hard to write, we'll be there, writing controversial RFCs then scaling them back! Resistance is futile!" [`a-sa28-f012469-c10`, team a]
- Positions seen by the extractor (`a-sa28-f012469-q5`): "explicitness is Rust's fourth core value, yet oddly never explicitly stated as a goal" (Ian Whitney, cited independently twice two years apart) vs. the ergonomics-initiative RFC author's own self-aware framing of the initiative's implicit-sugar RFCs as "controversial" (aturon)

### `error-enum-scope-module-vs-function`

**Question.** Should error enums be scoped per-module (one large enum for everything a module can fail at), or per-function/operation (smaller, descriptively-named enums scoped to what one call can fail at)?

- Teams: a · members (context): `a-sa14-f005149-q2` (f005149, core)
- Domains: core
- Concepts: error type granularity; API discoverability
- Positions:
  - `error-enum-scope-module-vs-function--p1` — scope error enums per-function, not per-module
    - **dig, b5, and ramfox (iroh team)** · Source `f005149` · date 2025-08-22 · locator § Concrete-error writing guidelines / Error enums are scoped to functions not modules — describe starting with one big per-module enum, finding it unwieldy, and moving to a nested/scoped hierarchy (e.g. `DialError` inside `ConnectError`) with names descriptive of the failure surface Quote: "Lean toward error enum names that are descriptive of the error, when logical" [`a-sa14-f005149-c2`, team a]
- Positions seen by the extractor (`a-sa14-f005149-q2`): lean toward small, descriptively-named, per-function error enums (e.g. `ConnectError`, `ParseError`) over one catch-all per-module enum, because the name alone then communicates the failure surface

### `esp32-psram-display-dma-strategy`

**Question.** How should an ESP32-S3 Rust firmware feed a large RGB (DPI) display from PSRAM framebuffers: cyclic DMA straight from PSRAM, restarted transfers, SRAM bounce buffers refilled from PSRAM, XIP from PSRAM, or abandon RGB for an I8080 panel?

- Teams: b · members (context): `b-sT05-f002499-q1` (f002499, embedded)
- Domains: embedded
- Concepts: DMA descriptors; PSRAM bandwidth; bounce buffers; XIP; esp-hal DPI driver; I8080
- Positions:
  - `esp32-psram-display-dma-strategy--p1` — infinite cyclic DMA buffer, never restart transfers
    - **Dominaezzz** · Source `f002499` · date 2026-01-29 · locator comment 2026-01-29T04:49:37Z — in own projects every framebuffer's last DMA descriptor points to its first; switching buffers = relinking descriptors; breaks down once PSRAM bandwidth enters Quote: "I avoid restarting transfers and I always use an infinite DMA buffer" (flag: voice-unverified) [`b-sT05-f002499-c1`, team b]
  - `esp32-psram-display-dma-strategy--p2` — SRAM bounce buffers refilled from PSRAM by Mem2Mem DMA, no XIP
    - **EliteTK** · Source `f002499` · date 2026-09-06 · locator comment 2026-09-06T10:36:52Z — two PSRAM framebuffers, two 1/16 bounce buffers in RAM, looping DMA to LCD, 8x descriptors to locate the emitted slice via DMA_OUT_CHx interrupt; cancels late refills; 31.1 FPS glitch-free; CPU copy rejected as "glacial" Quote: "double-buffered glitch-free output without relying on XiP from PSRAM" (flag: voice-unverified) [`b-sT05-f002499-c2`, team b]
  - `esp32-psram-display-dma-strategy--p3` — bounce buffers with acyclic descriptors, restart per frame
    - **Limeth** · Source `f002499` · date 2026-02-16 · locator comment 2026-02-16T23:59:16Z — cyclic descriptors failed after the first frame; acyclic descriptors restarted each frame work; open to upstreaming a generic solution to esp-hal Quote: "using acyclic descriptors and restarting the transmission after each frame seems to be fine, although not as nice" (flag: voice-unverified) [`b-sT05-f002499-c3`, team b]
  - `esp32-psram-display-dma-strategy--p4` — stay on an I8080 display for a PSRAM-heavy app
    - **yanshay** · Source `f002499` · date 2026-09-06 · locator comment 2026-09-06T19:24:30Z — had a bounce-buffer Slint renderer working, but flash contention and PSRAM bandwidth slowed the application; kept a smaller I8080 display Quote: "didn't switch device and still use an I8080 display at lower size and resolution" (flag: voice-unverified) [`b-sT05-f002499-c4`, team b]
- Positions seen by the extractor (`b-sT05-f002499-q1`): infinite cyclic DMA buffer; restart DMA periodically; bounce buffers + Mem2Mem DMA without XIP; acyclic bounce buffers restarted per frame; switch to I8080 display

### `example-data-domain-struct-vs-generic`

**Question.** in example/demo code, should tabular data be modeled with a dedicated domain struct or with generic collections (`Vec<Vec<String>>`)?

- Teams: b · members (context): `b-sR03-f000763-q1` (f000763, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: none given
- Positions:
  - `example-data-domain-struct-vs-generic--p1` — prefer a small dedicated struct even at the cost of extra ceremony, to show real-world data mapping.
    - **joshka (ratatui maintainer)** · Source `f000763` · date 2024-01-18 · locator ratatui/ratatui#840, comment 2024-01-18T22:51:17Z. · L424-L442. — prefer a small dedicated struct even at the cost of extra ceremony, to show real-world data mapping. Quote: "What about adding a small struct that has name, address, email and which gets generated in the app constructor instead of Vec<Vec<String>>? ... Obviously this is just gold plating things at this point. But it does give a nice way of showing how to map real world data into table columns." [`b-sR03-f000763-c1`, team b]
- Positions seen by the extractor (`b-sR03-f000763-q1`): prefer a small dedicated struct even at the cost of extra ceremony, to show real (joshka (ratatui maintainer))

### `exclusive-access-default-in-task-api`

**Question.** For a Rust task/resource API, should exclusive (&mut) access to shared state be the default, with shared (&-) read-only access only available opt-in?

- Teams: a · members (context): `a-sB04-f000227-q1` (f000227, embedded)
- Domains: embedded
- Concepts: exclusive-vs-shared-access; interior-mutability; lock-elision
- Positions:
  - `exclusive-access-default-in-task-api--p1` — default-exclusive, opt-in-shared-for-lock-elision
    - **RTIC developers (rtic.rs maintainers)** · Source `f000227` · date undated (living doc, v2.x) · locator "2.4. Resources", "Only shared (&-) access" — States the framework assumes exclusive mutable access by default; a task can opt into shared (&-) access instead, trading the ability to mutate for skipping the lock API even when the resource is contended across priorities Quote: "The advantage of specifying shared access (&-) to a resource is that no locks are required to access the resource even if the resource is contended by more than one task running at different priorities." [`a-sB04-f000227-c1`, team a]
- Positions seen by the extractor (`a-sB04-f000227-q1`): default-exclusive, opt-in-shared-for-lock-elision

### `executor-agnostic-libraries`

**Question.** Should a library that exposes an async API depend on a specific async executor or reactor?

- Teams: b · members (context): `b-bk01-f000233-q11` (f000233, core, web, distributed)
- Domains: core, distributed, web
- Concepts: executor; reactor; ecosystem compatibility; async I/O traits
- Positions:
  - `executor-agnostic-libraries--p1` — libraries should stay executor/reactor-agnostic
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "The Async Ecosystem" § Determining Ecosystem Compatibility — libraries exposing async APIs should not depend on a specific executor or reactor unless they must spawn tasks or define their own async I/O or timer futures; ideally only binaries own scheduling/running of tasks. Reasons from the ecosystem's actual fragmentation: Tokio's mio-based reactor and its own AsyncRead/AsyncWrite traits are not directly compatible with async-std or smol (which use the async-executor crate and futures' I/O traits), though compatibility layers like async_compat exist as a workaround. Quote: "Libraries exposing async APIs should not depend on a specific executor or reactor, unless they need to spawn tasks or define their own async I/O or timer futures." [`b-bk01-f000233-c12`, team b]
- Positions seen by the extractor (`b-bk01-f000233-q11`): no — libraries should stay executor/reactor-agnostic; only binaries should own runtime/task-scheduling choices

### `explicit-vs-convenience-memory-defaults`

**Question.** Should a language's memory-model default favor explicitness/performance (opt into convenience, as Rust's move/borrow-by-default with Cow/Rc as opt-in) or convenience (opt into performance, as Swift's copy-on-write-by-default with ownership as opt-in)?

- Teams: b · members (context): `b-sR12-f005668-q1` (f005668, swift-interop, core)
- Domains: core, swift-interop
- Concepts: ownership; borrowing; Cow; defaults; ergonomics vs. performance
- Positions:
  - `explicit-vs-convenience-memory-defaults--p1` — domain-dependent-tradeoff
    - **nmn (nmn.sh blog author)** · Source `f005668` · date 2026-01-31 · locator section "Convenience has its costs" — neither default is simply better; Rust's performance-first default suits systems, embedded, compilers and browser engines, Swift's convenience-first default suits UI, servers and parts of compilers/operating systems, and the author expects the overlap between the two to grow over time Quote: "I would say both languages have their uses. Rust is better for systems and embedded programming... Swift is better for writing UI and servers and some parts of compilers and operating systems. Over time I expect to see the overlap get bigger." [`b-sR12-f005668-c1`, team b]
- Positions seen by the extractor (`b-sR12-f005668-q1`): domain-dependent-tradeoff

### `explicit-vs-implicit-indirection`

**Question.** Should indirection for a recursive data type be explicit (the programmer writes `Box<T>`) or implicit (a compiler-inferred/annotated indirection, as Swift's `indirect` keyword)?

- Teams: b · members (context): `b-sR12-f005668-q2` (f005668, swift-interop, core)
- Domains: core, swift-interop
- Concepts: recursive types; Box; indirection; enums
- Positions:
  - `explicit-vs-implicit-indirection--p1` — explicit-favorably-framed
    - **nmn (nmn.sh blog author)** · Source `f005668` · date 2026-01-31 · locator section "Rust's compiler catches problems. Swift's compiler solves some of them" — contrasting Rust's `Box<TreeNode<T>>` for a recursive enum with Swift's `indirect` keyword, the author frames Rust's requirement to write the indirection explicitly as forcing the programmer to confront the problem directly, versus Swift handling it more automatically Quote: "This makes the problem explicit and forces you to deal with it directly, Swift is a little more, automatic." [`b-sR12-f005668-c2`, team b]
- Positions seen by the extractor (`b-sR12-f005668-q2`): explicit-favorably-framed

### `expose-fixed-array-vs-wrapper-type`

**Question.** When a fixed-size array (e.g. `[u8; 6]`) might later need to hold a same-shaped but larger variant (e.g. an 8-byte IEEE MAC), should the API expose the array type directly, or return a slice / wrap it in a dedicated type to keep the door open?

- Teams: a · members (context): `a-sa11-f004265-q1` (f004265, embedded)
- Domains: embedded
- Concepts: API design; newtype wrapping; forward compatibility
- Positions:
  - `expose-fixed-array-vs-wrapper-type--p1` — wrap raw array in a semantic type rather than exposing it directly
    - **MabezDev** · Source `f004265` · date 2026-02-18 · locator comment 2026-02-18T14:11:20Z — argues for wrapping `[u8; 6]` in a `Mac` type with derives and a `Display` impl, noting IEEE MACs are 8 bytes so the current shape could never return one Quote: "I think we should wrap `[u8; 6]` into a `Mac` type where we can derive some stuff, implement `Display`" [`a-sa11-f004265-c1`, team a]
  - `expose-fixed-array-vs-wrapper-type--p2` — return a slice instead of a fixed-size array
    - **MabezDev** · Source `f004265` · date 2026-02-19 · locator comment 2026-02-19T14:04:25Z — pushes back on returning `[u8; 6]`, preferring a slice-typed return Quote: "Return a slice, not [u8; 6]" [`a-sa11-f004265-c3`, team a]
- Positions seen by the extractor (`a-sa11-f004265-q1`): wrap in a semantic type (or return a slice) rather than exposing `[u8; 6]` directly, because a larger same-purpose variant is already foreseeable

### `expose-rustc-internals-rustdoc-json`

**Question.** When rustc has internal capability to correctly deduce information (implied trait bounds) that an external tool (cargo-semver-checks) cannot feasibly re-derive on its own, should that capability be exposed through a structured interface (rustdoc JSON) rather than left for external tools to approximate?

- Teams: a · members (context): `a-sa20-f009698-q4` (f009698, core)
- Domains: core
- Concepts: cargo-semver-checks; implied-bounds; rustdoc-json; semver-tooling
- Positions:
  - `expose-rustc-internals-rustdoc-json--p1` — expose-rustc-internals-via-rustdoc-json
    - **@obi1kenobi** · Source `f009698` · date 2025-05-03 · locator "Continue resolving `cargo-semver-checks` blockers for merging into cargo" section, comment posted 2025-05-03 — discovered that Rust's implied bounds (not stated explicitly at a definition site) are load-bearing for SemVer — missing them produces both false positives and false negatives — and that while it's technically infeasible for cargo-semver-checks to correctly deduce implied bounds itself, rustc already has this capability internally, so the team asked the rustdoc team to expose implied bounds in rustdoc JSON via those internal APIs Quote: "While technical limitations make it infeasible for cargo-semver-checks to correctly deduce implied bounds, rustc has this capability internally. We have asked the rustdoc team to expose implied bounds in rustdoc JSON by using those rustc internal APIs." [`a-sa20-f009698-c4`, team a]
- Positions seen by the extractor (`a-sa20-f009698-q4`): expose-rustc-internals-via-rustdoc-json

### `extend-foreign-trait-type`

**Question.** When a foreign trait's shared type (e.g. `embedded_hal::spi::Operation`) can't expose the hardware-specific capability a HAL needs, should the HAL define its own parallel type (accepting API duplication and a breaking change) to extend, or add narrowly scoped extension methods that leave the foreign type untouched?

- Teams: b · members (context): `b-sb06-f002027-q1` (f002027, embedded)
- Domains: embedded
- Concepts: embedded_hal; trait/type extension; orphan rule; API surface; breaking changes
- Positions:
  - `extend-foreign-trait-type--p1` — narrow-extension-methods
    - **elipsitz** · Source `f002027` · date 2024-09-17 · locator PR #479, comment 2024-09-17T20:43:31Z and 2024-09-23T15:36:19Z — initially wary of "bolting on another `Operation` enum without re-evaluating the complexity of the API," since the existing SPI API is already fairly unintuitive; leans toward a narrowly scoped `transaction_with_width` method or new enum variants instead of a second type Quote: "I'd be wary of bolting on another `Operation` enum without re-evaluating the complexity of the API." [`b-sb06-f002027-c1`, team b]
  - `extend-foreign-trait-type--p2` — own-parallel-type-with-conversion
    - **ivmarkov** · Source `f002027` · date 2024-09-23 · locator PR #479, comment 2024-09-23T16:21:54Z — argues the crate effectively already has "its own `Operation`... if you squint a little" (currently just a type-alias out of laziness); users should not need to know or care whether they're going through embedded_hal's `Operation` or the crate's own, so making it a real, independently extensible type is fine even as a breaking change Quote: "yet - it is something the user should neither know, nor care about" [`b-sb06-f002027-c2`, team b]
- Positions seen by the extractor (`b-sb06-f002027-q1`): own-parallel-type-with-conversion, narrow-extension-methods

### `fast-path-complexity`

**Question.** When a hand-tuned "fast path" optimization gives a large relative speedup on constrained/older hardware but a negligible absolute one on modern hardware, should a library keep the extra code complexity for the fast path, or drop it and favor the simpler code?

- Teams: b · members (context): `b-sb04-f001392-q1` (f001392, desktop-cli-ui, embedded, core)
- Domains: core, desktop-cli-ui, embedded
- Concepts: benchmarking; fast-path optimization; absolute vs. relative performance; embedded/legacy hardware; code simplicity
- Positions:
  - `fast-path-complexity--p1` — absolute-magnitude-decides
    - **joshka** · Source `f001392` · date 2024-05-11 · locator PR #1089, comment 2024-05-11T01:36:36Z — argues the fast path for left-aligned lines should be removed because, while the relative regression on a Raspberry Pi looks large, the absolute per-frame cost (~30ns on an M2 Mac) is not worth the added code complexity Quote: "It's important to look the absolute magnitude of a perf gain, and not just the relative amount." [`b-sb04-f001392-c1`, team b]
  - `fast-path-complexity--p2` — relative-impact-on-constrained-hw-matters
    - **EdJoPaTo** · Source `f001392` · date 2024-05-11 · locator PR #1089, comment 2024-05-11T09:13:41Z — argues the fast path is worth keeping because `Line` is one of the most-used core constructs and `Alignment::Left` is the common default, so a "relatively small" per-call regression compounds across hundreds of rendered cells per frame on low-power devices (own benchmarks on Raspberry Pi 1/2/4 showed 12-38% regressions without it) Quote: "Relatively small improvements will impact a lot of code depending on it." [`b-sb04-f001392-c2`, team b]
- Positions seen by the extractor (`b-sb04-f001392-q1`): absolute-magnitude-decides, relative-impact-on-constrained-hw-matters

### `feature-flag-trunk-vs-long-branch`

**Question.** Should incomplete or breaking Rust work be merged to main behind a Cargo feature flag (trunk-based development), or kept on a long-lived branch?

- Teams: b · members (context): `b-bk03-f000267-q11` (f000267, core)
- Domains: core
- Concepts: Cargo features; trunk-based development; branching strategy
- Positions:
  - `feature-flag-trunk-vs-long-branch--p1` — feature-flag-gate-on-trunk
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Zebra versioning and releases § Feature Flags — to keep main always releasable, experimental features and (unless urgent) breaking changes must be gated behind a Rust/Cargo feature flag rather than developed on a long-lived branch Quote: "To keep the main branch in a releasable state, experimental features must be gated behind a Rust feature flag." (flag: voice-unverified) [`b-bk03-f000267-c11`, team b]
- Positions seen by the extractor (`b-bk03-f000267-q11`): feature-flag-gate-on-trunk

### `feature-flags-vs-generic-wiring`

**Question.** Should optional/alternate implementations in a Rust library be selected via Cargo feature flags, or via generic type-level component wiring (traits/generics, e.g. CGP-style)?

- Teams: a · members (context): `a-sa16-f007175-q1` (f007175, core)
- Domains: core
- Concepts: generics; traits; macros
- Positions:
  - `feature-flags-vs-generic-wiring--p1` — generic-wiring-over-feature-flags
    - **Soares Chen** · Source `f007175` · date 2025-06-14 · locator § Modularity of HandleSimpleExec — CGP-style generic component wiring lets alternative implementations coexist and be tested together, avoiding the combinatorial-testing burden of Cargo feature flags. Quote: "This generic approach is also less error-prone than feature flags, as all alternative implementations can coexist and be tested simultaneously" [`a-sa16-f007175-c1`, team a]
- Positions seen by the extractor (`a-sa16-f007175-q1`): generic-wiring-over-feature-flags

### `feature-misuse-responsibility`

**Question.** When an opt-in crate feature can be misused by downstream crates (enabled unconditionally "for convenience"), is it the exposing crate's job to structure the API/placement to make misuse harder, or the misusing crate's bug to fix?

- Teams: a · members (context): `a-sa06-f003558-q2` (f003558, wasm)
- Domains: wasm
- Concepts: crate feature design; dependency graph hygiene; Cargo feature unification
- Positions:
  - `feature-misuse-responsibility--p1` — structure feature placement to discourage misuse
    - **newpavlov** · Source `f003558` · date 2025-09-19 · locator comment 2025-09-19T16:28:13Z — prefers the feature live in `js-sys` rather than `getrandom` directly, reasoning that a crate wrongly adding `js-sys` unconditionally is a more visible/unlikely mistake than wrongly enabling a `getrandom` feature, since the latter has no effect on non-WASM targets and so goes unpunished Quote: "such incorrect behavior does not get punished, while users would be more careful with js-sys" [`a-sa06-f003558-c3`, team a]
  - `feature-misuse-responsibility--p2` — misuse is the misusing crate's bug, not the exposing crate's design problem
    - **Pauan** · Source `f003558` · date 2025-09-21 · locator comment 2025-09-21T22:11:14Z; 2025-09-21T22:31:20Z — rejects the "protect against misuse" framing outright, arguing crates cannot be forced to behave properly by restructuring the API, that misbehaving crates should have issues/PRs filed against them directly, and that shifting the feature to `js-sys` only relocates the same possible mistake Quote: "This seems to me like a solution in search of a problem" [`a-sa06-f003558-c4`, team a]
- Positions seen by the extractor (`a-sa06-f003558-q2`): place/gate the feature so incorrect use is less likely (e.g. host it in `js-sys` rather than `getrandom` directly); vs. misuse is a bug in the misusing crate, not something the exposing crate should engineer around

### `feature-naming-mechanism-vs-capability`

**Question.** Should a feature's name describe only the literal mechanism it provides, or the higher-level capability that mechanism enables, when the feature itself is just the low-level primitive?

- Teams: a · members (context): `a-sa11-f004512-q4` (f004512, embedded)
- Domains: embedded
- Concepts: API naming; scope communication
- Positions:
  - `feature-naming-mechanism-vs-capability--p1` — name a feature for its literal mechanism, not the capability it implies
    - **AnthonyGrondin** · Source `f004512` · date 2026-04-01 · locator comment 2026-04-01T17:33:09Z — objects that "tracking" implies the library itself tracks allocations with little setup, when the feature really just adds hooking and nothing more, and argues the name should be more explicit about that Quote: "to me, `tracking` implies that the library itself is taking care of allocation tracking, without requiring much setup from the user. I think it should be more explicit, that this feature is simply adding hooking, and nothing more." [`a-sa11-f004512-c5`, team a]
- Positions seen by the extractor (`a-sa11-f004512-q4`): name the feature for what it literally does ("hooking") rather than implying it does more ("tracking") than the library actually provides out of the box

### `ffi-bindings-lag-pause-or-ship`

**Question.** When a Rust library's non-Rust-language FFI bindings lag behind the quality of its native Rust API, should maintainers keep shipping degraded bindings on every release, or pause bindings updates until the FFI/bridging story itself is fixed, accepting ecosystem-fragmentation risk in the meantime?

- Teams: a · members (context): `a-sa04-f002665-q1` (f002665, decentralized-iroh, swift-interop)
- Domains: decentralized-iroh, swift-interop
- Concepts: FFI; UniFFI; multi-language bindings; ecosystem fragmentation
- Positions:
  - `ffi-bindings-lag-pause-or-ship--p1` — pause-and-fix-ffi-first
    - **b5** · Source `f002665` · date 2025-02-12 · locator opening section ("Why?") — announces iroh will stop updating its Kotlin/Python/Swift/JavaScript FFI bindings on every release because the FFI experience doesn't yet match the "just works" bar the project holds Rust usage to, and because degraded bindings risk fragmenting the protocol ecosystem across languages Quote: "Because we don't think our FFI story is good enough right now. Our promise is to ship \"P2P that works\", and we're not hitting that \"just works\" experience in languages that aren't rust." [`a-sa04-f002665-c1`, team a]
- Positions seen by the extractor (`a-sa04-f002665-q1`): pause-and-fix-ffi-first (author/iroh maintainers)

### `ffi-tag-unwind-vs-abort`

**Question.** When an FFI/Wasm boundary must distinguish recoverable foreign exceptions from unrecoverable aborts, should the recoverable (unwind) case be explicitly tagged, or the unrecoverable (abort) case?

- Teams: a · members (context): `a-sa12-f004598-q2` (f004598, wasm, cloud-workers)
- Domains: cloud-workers, wasm
- Concepts: error-classification; ffi-boundary-safety; exception-handling
- Positions:
  - `ffi-tag-unwind-vs-abort--p1` — tag-unwinds-explicitly
    - **Guy Bedford, Hood Chatham, and Logan Gatlin** · Source `f004598` · date 2026-04-22 · locator blog post, § "Abort recovery" — chose to mark all definitely-unwind errors with exception tags, rather than marking all definitely-abort errors, to distinguish recoverable foreign exceptions from unrecoverable aborts at the Wasm boundary, because their existing raw WAT-level Exception Handling implementation made that direction easier Quote: "We had two options to solve this technically: either mark all errors which are definitely aborts, or mark all errors which are definitely unwinds. Either could have worked but we chose the latter." [`a-sa12-f004598-c2`, team a]
- Positions seen by the extractor (`a-sa12-f004598-q2`): tag-unwinds-explicitly (Cloudflare/wasm-bindgen team, chosen for ease of implementation)

### `fields-in-traits`

**Question.** Should Rust add "fields in traits" (a shared field, accessed through a vtable offset on `dyn Trait`, that every implementor must provide)?

- Teams: b · members (context): `b-sb19-f007207-q1` (f007207, core)
- Domains: core
- Concepts: fields in traits; associated types; dyn trait objects; vtable
- Positions:
  - `fields-in-traits--p1` — mildly-supportive-uncertain-use-case
    - **Jimmy Hartzell** · Source `f007207` · date 2025-07-21 · locator § "Merits of the Proposal" — fields-in-traits is a limited, distinct-enough feature that wouldn't harm Rust's design, but he doesn't personally have a compelling use case for it Quote: "my conclusion comes out to a shrug. This feature doesn't seem bad in any way... But I personally don't engage with a use case for it." [`b-sb19-f007207-c1`, team b]
- Positions seen by the extractor (`b-sb19-f007207-q1`): mildly-supportive-uncertain-use-case (Jimmy Hartzell)

### `final-trait-methods`

**Question.** Should Rust add `final`/non-overridable trait methods, and if so, must such methods still participate in dynamic dispatch (vtables) for soundness?

- Teams: a · members (context): `a-sa19-f009316-q1` (f009316, core)
- Domains: core
- Concepts: trait objects; dyn dispatch; vtables; sealed traits; specialization; TypeId
- Positions:
  - `final-trait-methods--p1` — support-final-methods
    - **newpavlov** · Source `f009316` · date 2026-01-07 · locator OP, 2026-01-07T21:26:16.248Z — Proposes a `#[non_overridable]` attribute for trait extension methods whose override could cause correctness bugs, potentially excluding such methods from vtables to shrink them. Quote: "I think something like #[non_overridable] could be a useful addition to the language." [`a-sa19-f009316-c1`, team a]
    - **josh** · Source `f009316` · date 2024-08-13 · locator linked RFC (joshtriplett/rfcs "final"), cited 2026-01-07T21:42:35.707Z — Points to an already-drafted RFC ("Trait method impl restrictions", using the reserved `final` keyword) letting any trait forbid overriding specific methods or associated functions. Quote: "Support restricting implementation of individual methods within traits, using the already reserved `final` keyword." [`a-sa19-f009316-c2`, team a]
  - `final-trait-methods--p2` — skeptical-limited-value-vs-free-functions
    - **afetisov** · Source `f009316` · date 2026-01-08 · locator reply, 2026-01-08T14:37:33.435Z — Doubts final methods offer real benefit beyond "minor sugar", since any trait bound or call used inside a final method can just as well be replicated with a corresponding free function. Quote: "Surely there are other benefits, besides minor sugar, for a new feature? Personally I can't think of any." [`a-sa19-f009316-c3`, team a]
  - `final-trait-methods--p3` — final-methods-need-vtable-for-soundness
    - **SkiFire13** · Source `f009316` · date 2026-01-08 · locator reply, 2026-01-08T21:16:18.959Z — Constructs a concrete example where a final method called through `dyn Trait` observably differs from an equivalent generic free function (via `TypeId::of::<Self>` vs. the erased type), showing final methods cannot simply desugar to free functions and must remain reachable via the vtable. Quote: "The .baz() method prints () because it's being monomorphized for () and inserted into the vtable, while the baz function call prints dyn playground::Foo..." [`a-sa19-f009316-c4`, team a]
    - **eggyal** · Source `f009316` · date 2026-03-12 · locator linked rust-lang/rust issue (opened 2026-03-10), cited 2026-03-12T06:00:48.747Z — Filed an I-unsound bug showing nightly's experimental `final` associated functions behave inconsistently with `dyn Trait` dispatch (an `assert_ne!` on `TypeId::of` via `dyn Trait` fails), confirming the vtable/soundness concern is a live, unresolved implementation problem rather than a purely theoretical one. Quote: "`final` methods should work the same as without it (if it works without it)" [`a-sa19-f009316-c5`, team a]
- Positions seen by the extractor (`a-sa19-f009316-q1`): support-final-methods; skeptical-limited-value-vs-free-functions; final-methods-need-vtable-for-soundness

### `fine-grained-reactivity-vs-vdom`

**Question.** should a Rust web UI framework use fine-grained (signal-based) reactivity or virtual-DOM diffing

- Teams: a · members (context): `a-sR14-f005702-q1` (f005702, web, frontend)
- Domains: frontend, web
- Concepts: none given
- Positions:
  - `fine-grained-reactivity-vs-vdom--p1` — fine-grained-reactivity
    - **Sycamore** · Source `f005702` · date 2026-04-01 · locator front page, "Fine-Grained Reactivity" feature blurb — fine-grained reactivity is the right model, contrasted implicitly with vdom-diffing frameworks (e.g. Yew). Quote: "Sycamore's reactivity system is fine-grained, meaning that only the parts of your app that need to be updated will be." [`a-sR14-f005702-c1`, team a]
- Positions seen by the extractor (`a-sR14-f005702-q1`): fine-grained-reactivity (Sycamore)

### `fixed-point-loop-vs-event-retrigger`

**Question.** Should a bounded, safety-first multi-pass graph algorithm favor a simple iterative fixed-point loop, or a more complex event-driven re-trigger design?

- Teams: a · members (context): `a-sa07-f003704-q2` (f003704, ml, core)
- Domains: core, ml
- Concepts: graph-traversal; iterative-convergence; complexity-vs-performance
- Positions:
  - `fixed-point-loop-vs-event-retrigger--p1` — simple-iterative-bounded
    - **antimora** · Source `f003704` · date 2025-11-07 · locator PR #3872, comment 2025-11-07T17:03:28Z — kept the iterative type-inference loop (bounded to 10 passes, down from 100) over a more efficient graph-retrigger design because the iterative approach was safer and bug-free Quote: "this iterative approached was the safest and bug free compared to graph re-trigger approach, which would have been more efficient but it was complex" [`a-sa07-f003704-c2`, team a]
- Positions seen by the extractor (`a-sa07-f003704-q2`): simple-iterative-bounded (antimora, held and shipped), event-driven-retrigger (antimora, considered and rejected)

### `fixed-vs-dynamic-matrix-sizing`

**Question.** When a matrix's size is known at compile time, should code prefer fixed (stack-allocated) resizing/operations over dynamic (heap-allocated) ones?

- Teams: a · members (context): `a-sB01-f000217-q3` (f000217, core, embedded)
- Domains: core, embedded
- Concepts: const-generics-sizing; stack-vs-heap-allocation
- Positions:
  - `fixed-vs-dynamic-matrix-sizing--p1` — prefer fixed/static sizing whenever possible
    - **Dimforge (nalgebra maintainers)** · Source `f000217` · date capture 2025-01-15 (Wayback; underlying doc undated) · locator "Vectors and matrices" chapter, "Matrix resizing" — States fixed (compile-time-known) resizing should be preferred over dynamic resizing whenever possible, because dynamic resizing always produces heap-allocated results Quote: "Indeed, dynamic resizing will produce heap-allocated results because the size of the output matrix cannot be deduced at compile-time." [`a-sB01-f000217-c3`, team a]
- Positions seen by the extractor (`a-sB01-f000217-q3`): prefer fixed/static sizing whenever possible

### `foreign-keys-vs-app-integrity`

**Question.** On eventually consistent storage, should referential integrity be enforced by database foreign keys or in application code?

- Grouping: Singleton. Strike b31 (a D1 schema decision, not edge primitives vs VPS) is re-homed here; merge-v2 had already linked it to this Question, the second one in its source.
- Teams: b · members (context): `b-sT07-f004166-q2` (f004166, cloud-workers, distributed)
- Domains: cloud-workers, distributed
- Concepts: eventual consistency; foreign keys; D1/SQLite
- Positions:
  - `foreign-keys-vs-app-integrity--app-enforced-integrity` — Drop foreign keys; enforce integrity in application code
    - **Nick Kuntz** · Source `f004166` · date 2026-01-27 · locator § D1 ("We learned one hard lesson") — D1's eventual consistency broke FK checks across sequential writes, so all FKs were removed Quote: "We removed all foreign keys and enforce referential integrity in application code." (flag: voice-unverified) [`b-sT07-f004166-c2`, team b]
- Positions seen by the extractor (`b-sT07-f004166-q2`): drop foreign keys, enforce in application code

### `form-values-list-vs-scalar-deserialization`

**Question.** When a UI framework's form-submission API hands back untyped, string-keyed values (e.g. a `HashMap<String, Vec<String>>`) for deserialization into a caller-defined struct via serde, should the ambiguity between a single value and a multi-value field (e.g. a multi-select) be resolved by an explicit schema/cardinality marker in the data, or by a permissive/heuristic deserializer that infers list-vs-scalar from the observed value count per field?

- Teams: a · members (context): `a-01-f000543-q1` (f000543, frontend)
- Domains: frontend
- Concepts: serde deserialization; generic/untyped form data; ambiguous cardinality; API ergonomics vs. correctness
- Positions:
  - `form-values-list-vs-scalar-deserialization--p1` — disambiguate scalar vs. list by observed value count (no schema change)
    - **bunnyBites** · Source `f000543` · date 2023-11-04 · locator PR comment responding to review — For multi-valued elements like a `<select multiple>`, the deserializer should infer list-vs-scalar for a field from how many values were observed for it, rather than adding an explicit list/scalar marker to the wire format. Quote: "I think for multi-valued elements like select, we would expect the same result as the 'values' (vector/array of values), which we can get to know based on the length of values." [`a-01-f000543-c1`, team a]
- Positions seen by the extractor (`a-01-f000543-q1`): reviewer (unattributed) — add an explicit list/scalar marker to the wire format, or make the deserializer polymorphic over single-value-vs-list; bunnyBites — infer list-vs-scalar from the observed value count per field, without changing the data shape

### `frontend-hook-naming`

**Question.** What naming convention should Rust reactive-frontend-framework hooks use, given no established convention exists across the ecosystem?

- Teams: a · members (context): `a-sR07-f002271-q2` (f002271, frontend)
- Domains: frontend
- Concepts: hook naming conventions; API naming
- Positions:
  - `frontend-hook-naming--p1` — use_-prefixed-noun-phrase
    - **lukechu10** · Source `f002271` · date 2024-11-03 · locator comment on router.rs (2024-11-03T22:54:24Z) — acknowledging no precise convention exists, proposes naming query/hash accessor hooks with a `use_<noun>` pattern (`use_search_query`, `use_location_hash`) Quote: "Although there isn't really a precise convention here, I think the hook would be better named `use_search_query` instead." [`a-sR07-f002271-c2`, team a]
- Positions seen by the extractor (`a-sR07-f002271-q2`): use_-prefixed-noun-phrase (lukechu10)

### `fullstack-reactive-complexity-essential`

**Question.** is the complexity practitioners feel in fullstack reactive frameworks (hooks, effects, suspense, hydration mismatches) accidental complexity added by the framework, or essential complexity inherent to the fullstack problem itself?

- Teams: b · members (context): `b-sb20-f007290-q2` (f007290, frontend, web)
- Domains: frontend, web
- Concepts: hooks; reactivity; hydration; suspense
- Positions:
  - `fullstack-reactive-complexity-essential--p1` — the hooks/reactivity complexity in a fullstack framework is essential, not accidental
    - **fasterthanlime** · Source `f007290` · date 2025-11-22 · locator section "Love-hate" — the long list of Dioxus hooks and the fact that breaking hook rules produces silent misbehavior rather than a compile or runtime error feels intimidating, but that is because fullstack apps are inherently complicated, not because Dioxus added needless complexity Quote: "It's that full stack stuff is complicated. It truly is. It's not that Dioxus added complexity where we didn't need any." [`b-sb20-f007290-c2`, team b]
- Positions seen by the extractor (`b-sb20-f007290-q2`): essential, not accidental (fasterthanlime)

### `futures-crate-vs-alternatives`

**Question.** Should a Rust library depend on the mainline `futures` crate for complex combinators (e.g. `FuturesUnordered`) despite known bugs in that unsafe-heavy code, or should it avoid `futures` altogether and assemble the needed functionality from several smaller alternative crates (futures-lite, futures-buffered, futures-util) at the cost of ergonomics and discoverability?

- Teams: b · members (context): `b-sb17-f005159-q3` (f005159, decentralized-iroh)
- Domains: decentralized-iroh
- Concepts: `futures` crate; `FuturesUnordered`; combinator bugs; crate fragmentation
- Positions:
  - `futures-crate-vs-alternatives--p1` — avoid-futures-crate-use-alternatives
    - **Rüdiger Klaehn** · Source `f005159` · date 2024-07-31 · locator article body, "Complex combinators in futures are buggy" section — after finding bugs in `futures`'s unsafe-heavy combinators (e.g. `FuturesUnordered`) that were impractical to fix upstream, drops the `futures` crate dependency entirely in favor of futures-lite, futures-buffered and futures-util Quote: "We have therefore decided to take the drastic step to stop using the futures crate altogether and use a set of crates to replace it: futures-lite for simple futures and streams combinators, futures-buffered to replace FuturesUnordered, and futures-util from the futures repo for the rare case where we want to use something from futures that is not covered by either." [`b-sb17-f005159-c3`, team b]
- Positions seen by the extractor (`b-sb17-f005159-q3`): avoid-futures-crate-use-alternatives (Rüdiger Klaehn)

### `game-logic-in-scripting-layer`

**Question.** when a Rust game engine embeds a scripting/modding language, should most game logic live in the hosted scripting language itself, or should Rust own the state with the scripting language calling into it through getter/setter shims?

- Teams: b · members (context): `b-sb26-f013214-q4` (f013214, other)
- Domains: other
- Concepts: scripting VM integration; engine architecture; state ownership
- Positions:
  - `game-logic-in-scripting-layer--p1` — keep the native (Rust) layer a thin, general-purpose platform and put effectively all game logic in the hosted scripting/VM language, rather than building a bridge for native code to touch mutable game state directly
    - **parasyte** · Source `f013214` · date 2024-05-05 · locator reply timestamped 2024-05-05T02:19:47 — points to long-standing precedent — browser JavaScript games, and older engines like SCUMM and Another World — for putting ~100% of game logic in the hosted language, with the unmanaged layer having "nothing to do with the game" as a general-purpose platform, and the real source of truth for state living in serialized data files (JSON, glTF, VRM) rather than in either language's live objects Quote: "one of the most consistent designs I've seen is putting 100% of the game logic into the hosted scripting language." [`b-sb26-f013214-c6`, team b]
- Positions seen by the extractor (`b-sb26-f013214-q4`): put effectively all game logic in the hosted scripting language, keeping the native (Rust) layer a thin general-purpose platform — precedented by browser-JS games and older engines like SCUMM and Another World, with the real source of truth for state living in serialized data files rather than in either language's live objects (parasyte)

### `gamedev-ecosystem-maturity`

**Question.** is Rust's 3D/graphics game-dev crate ecosystem (wgpu, Rend3, Bevy, egui, winit) mature enough for demanding, multi-year production projects, or does its ongoing API churn and thinness make such projects impractical today?

- Teams: b · members (context): `b-sb26-f013214-q1` (f013214, other)
- Domains: other
- Concepts: wgpu; Rend3; Bevy; egui; winit; crate ecosystem maturity; API churn
- Positions:
  - `gamedev-ecosystem-maturity--p1` — after three years building a demanding 3D metaverse client, the Rust graphics crate ecosystem (WGPU, Rend3, winit, egui) is not yet "ready for prime time"
    - **John_Nagle** · Source `f013214` · date 2024-01-06 (opening post), reaffirmed 2024-03-25 · locator opening post, and reply timestamped 2024-03-25T21:11 — describes the graphics crates as "tightly coupled," advancing in version lockstep with frequent breaking upgrades and documentation limited to rustdoc; over half his time across three years has gone to filing and chasing ecosystem bugs rather than his actual application; by March 2024 some things had measurably improved (Rend3 dropping a net-negative occlusion-culling optimization, a new `glam` release) but core stability problems (consistent frame rate under concurrent content updates) were still unresolved Quote: "The trouble is, the graphics crate ecosystem still isn't ready for prime time... Over half my time goes into dealing with ecosystem bugs." [`b-sb26-f013214-c1`, team b]
  - `gamedev-ecosystem-maturity--p2` — Rust game dev is not a flop, just early — game-industry technology adoption is inherently slow regardless of a technology's merits
    - **khimru** · Source `f013214` · date 2024-01-07 · locator reply timestamped 2024-01-07T00:24:43 — frames the situation with the Gartner hype-cycle "Trough of Disillusionment" label, and draws an analogy to games staying on MS-DOS for years after Windows existed — games moved only once 3D accelerator cards forced the issue, not because Windows was inherently better — arguing Rust lacks an equivalent forcing function, so any transition will take years or decades Quote: "So we are firmly in the Trough of Disillusionment stage? That's fine and kinda expected." [`b-sb26-f013214-c2`, team b]
- Positions seen by the extractor (`b-sb26-f013214-q1`): still not "ready for prime time" after three years of serious use, with over half of development time going to ecosystem bugs (John_Nagle); not a flop, just in an expected "Trough of Disillusionment" stage — game-industry tech adoption is always slow regardless of merit (khimru)

### `gating-pre-1-0-dependency-integrations`

**Question.** For optional, pre-1.0 dependencies whose traits a crate implements, should the crate gate the exposure behind one coarse "unstable" feature flag, behind per-dependency (or per-dependency-version) feature flags, or simply drop the integration and re-add it only if users ask?

- Teams: b · members (context): `b-sb09-f002615-q1` (f002615, embedded)
- Domains: embedded
- Concepts: feature flags; semver stability; unstable attribute; optional trait impls
- Positions:
  - `gating-pre-1-0-dependency-integrations--p1` — cfg-gate-hidden-impls-not-unstable-attribute
    - **bugadani** · Source `f002615` · date 2025-01-29 · locator comment @bugadani 2025-01-29T12:14:24Z — argues private structs/functions don't need `#[instability::unstable]`; hidden impls can just be `#[cfg(feature = "unstable")]`-gated instead of documented as unstable. Quote: "We don't need to document a hidden impl, whether it's stable or not." [`b-sb09-f002615-c1`, team b]
  - `gating-pre-1-0-dependency-integrations--p2` — per-function-not-per-block-annotation
    - **bugadani** · Source `f002615` · date 2025-01-29 · locator comment @bugadani 2025-01-29T12:13:30Z — the `#[unstable]` attribute should sit on each function rather than on whole inherent impl blocks. Quote: "We shouldn't use `#[unstable]` on inherent impl blocks, the attribute should be placed on each function." [`b-sb09-f002615-c2`, team b]
  - `gating-pre-1-0-dependency-integrations--p3` — blanket-unstable-flag
    - **bjoernQ** · Source `f002615` · date 2025-01-29 · locator comment @bjoernQ 2025-01-29T13:13:58Z — the impl is marked unstable because the underlying `ufmt` dependency is still pre-1.0 (0.2.0). Quote: "I think the intention of having this unstable is that `ufmt` is 0.2.0" [`b-sb09-f002615-c3`, team b]
  - `gating-pre-1-0-dependency-integrations--p4` — need-an-explicit-policy
    - **bugadani** · Source `f002615` · date 2025-01-29 · locator comment @bugadani 2025-01-29T12:33:55Z — neither blanket-unstable nor per-dependency-version features feel right; the project needs a general policy on how to handle pre-1.0 optional trait dependencies. Quote: "Hiding every one of these behind \"unstable\" seems a bit off to me... but also a dependency+version feature... may be a bit too granular... I think we might want to come up with a policy regarding them." [`b-sb09-f002615-c4`, team b]
    - **jessebraham** · Source `f002615` · date 2025-01-29 · locator comment @jessebraham 2025-01-29T13:02:37Z — agrees the blanket-unstable approach is ham-fisted but is wary of accumulating many per-dependency-version features. Quote: "I agree that gating this all behind the `unstable` feature is probably a bit of a ham-fisted approach, however I'm also not super excited about the prospect of potentially accumulating a bunch of different versions of various dependencies..." [`b-sb09-f002615-c5`, team b]
    - **bugadani** · Source `f002615` · date 2025-01-30 · locator comment @bugadani 2025-01-30T10:24:54Z — pushes back that ufmt is not the only such dependency (rand-core, embassy-embedded-hal, log, etc.), so ad hoc removal doesn't resolve the underlying question of what to do with unstable optional dependencies generally. Quote: "My point is, we need to figure out these dependencies, and what we do with them. We can remove a specific example, but the issue doesn't go away just from that." [`b-sb09-f002615-c8`, team b]
  - `gating-pre-1-0-dependency-integrations--p5` — per-dependency-subfeature
    - **MabezDev** · Source `f002615` · date 2025-01-29 · locator comment @MabezDev 2025-01-29T15:44:45Z — proposes expanding the "unstable" feature into named sub-features like `unstable-ufmt` per dependency. Quote: "One option is to expand the `unstable` feature to have `unstable-ufmt` etc... maybe for dependencies it makes sense?" [`b-sb09-f002615-c6`, team b]
  - `gating-pre-1-0-dependency-integrations--p6` — just-remove-and-readd-on-demand
    - **bjoernQ** · Source `f002615` · date 2025-01-30 · locator comment @bjoernQ 2025-01-30T10:14:28Z — argues it's simpler to just remove optional integrations (as was done for embedded-hal-nb) and re-add them later if users complain, rather than design feature-flag machinery. Quote: "we spend more time talking/thinking about it than it would take to remove and re-add it" [`b-sb09-f002615-c7`, team b]
- Positions seen by the extractor (`b-sb09-f002615-q1`): blanket-unstable-flag (bjoernQ, initial), per-dependency-subfeature (MabezDev), just-remove-and-readd-on-demand (bjoernQ, later), need-an-explicit-policy (bugadani, jessebraham)

### `generated-crates-escape-hatches`

**Question.** should generated crates be fully automatic, or must they leave handwritten escape hatches for what a schema can't express (e.g. trait impls)?

- Teams: a · members (context): `a-sa23-f011186-q4` (f011186, web, core)
- Domains: core, web
- Concepts: code generation; trait implementation
- Positions:
  - `generated-crates-escape-hatches--p1` — generated crates need handwritten escape hatches
    - **Adam** · Source `f011186` · date 2024-11-20 · locator ~00:25:33 — ~95% of his generated crate is codegen'd, but a dedicated `methods.rs` file holds handwritten trait impls and helpers (e.g. arithmetic on a generated `Angle` type) that can't be inferred from the OpenAPI schema alone, and the generator is written to never overwrite that file Quote: "support handwritten code I'd say 95% of the crate is generated" [`a-sa23-f011186-c4`, team a]
- Positions seen by the extractor (`a-sa23-f011186-q4`): hybrid-generated-plus-escape-hatch-file (Adam, ~95% generated + `methods.rs`)

### `generated-size-vs-runtime-performance`

**Question.** should a codegen tool trade a larger generated-output size for better runtime performance?

- Teams: b · members (context): `b-sR03-f001160-q2` (f001160, wasm)
- Domains: wasm
- Concepts: none given
- Positions:
  - `generated-size-vs-runtime-performance--p1` — favors performance over output size for this change.
    - **daxpedda** · Source `f001160` · date 2024-04-03 · locator wasm-bindgen/wasm-bindgen#3898, comment 2024-04-03T06:33:18Z. · L2343-L2347. — favors performance over output size for this change. Quote: "Generate JS bindings for WebIDL dictionary setters instead of using `Reflect`. This increases the size of the Web API bindings but should be more performant." [`b-sR03-f001160-c2`, team b]
- Positions seen by the extractor (`b-sR03-f001160-q2`): favors performance over output size for this change. (daxpedda)

### `generic-over-blocking-async`

**Question.** Should blocking and async variants of a peripheral driver share one generic implementation, or stay duplicated?

- Teams: b · members (context): `b-sb05-f001512-q4` (f001512, embedded)
- Domains: embedded
- Concepts: generics over mode; async/sync duplication
- Positions:
  - `generic-over-blocking-async--p1` — generic-over-mode
    - **MabezDev** · Source `f001512` · date 2024-05-29 · locator comment 2024-05-29T09:59:47Z — blocking and async constructors should share one generic implementation instead of duplicating methods Quote: "I think we should be able to have one impl that is generic over the mode." [`b-sb05-f001512-c5`, team b]
- Positions seen by the extractor (`b-sb05-f001512-q4`): generic-over-mode (MabezDev)

### `git-storage-database-decentralized`

**Question.** For hosting large monorepos, should Git object storage move off the traditional filesystem-based backend and into a distributed database (as Google Piper/Meta Sapling do), combined with decentralizing hosting itself rather than relying on a centralized host like GitHub?

- Teams: b · members (context): `b-sb23-f011178-q1` (f011178, distributed, decentralized-iroh)
- Domains: decentralized-iroh, distributed
- Concepts: monorepo; Git internals (blob/tree/commit objects); Git LFS; decentralized hosting; GTM/P2P networking
- Positions:
  - `git-storage-database-decentralized--p1` — rebuild Git's storage engine on a database and decentralize hosting rather than depend on a centralized host
    - **Quanyi Ma** · Source `f011178` · date 2024-11-18 · locator ~06:14-11:22 — argues centralized hosts like GitHub can unilaterally access all data or use it for AI training/deletion, so his project (Mega, built in Rust) stores Git objects in a database (mirroring how Google's Piper and Meta's Sapling scale monorepos) and layers a GTM-based P2P network on top so repositories can be cloned/pushed without a single central node Quote: "being centralized ... can access all data and can take action like ... training AI or deleting projects" [`b-sb23-f011178-c1`, team b]
- Positions seen by the extractor (`b-sb23-f011178-q1`): replace file-based Git storage with a database-backed engine and decentralize the hosting layer over a P2P network, in Rust, to avoid single-vendor control and scale to monorepo sizes

### `global-statics-vs-per-request-state`

**Question.** Under a concurrent-instance execution model, should shared state use global statics/OnceCell, or be scoped per-request with explicit synchronization?

- Teams: b · members (context): `b-sR10-f004809-q2` (f004809, wasm, cloud-workers)
- Domains: cloud-workers, wasm
- Concepts: shared state; concurrency; statics
- Positions:
  - `global-statics-vs-per-request-state--p1` — prefer-per-request-scoped-state
    - **The Spin Project (Fermyon / CNCF Spin, institution)** · Source `f004809` · date 2026-06-15 · locator section "Heads up on global state" — since one instance can now serve concurrent in-flight requests, code that used static/module-level/OnceCell "global" state must be audited and moved to per-request state or explicit synchronization Quote: "Audit any static, module-level, or OnceCell state and reach for per-request state or explicit synchronization where needed." [`b-sR10-f004809-c2`, team b]
- Positions seen by the extractor (`b-sR10-f004809-q2`): prefer-per-request-scoped-state

### `gpu-async-await-vs-dsl`

**Question.** For structured concurrent GPU programming, is it better to reuse an existing general-purpose language's async/await abstraction (Rust's `Future`/async-await) than to adopt a purpose-built DSL/compiler stack (JAX, Triton, NVIDIA CUDA Tile)?

- Teams: b · members (context): `b-sb21-f008808-q1` (f008808, ml)
- Domains: ml
- Concepts: Future trait; structured concurrency; warp specialization; CUDA Tile; function-coloring problem
- Positions:
  - `gpu-async-await-vs-dsl--p1` — reuse-existing-async-model-over-new-dsl
    - **VectorWare** · Source `f008808` · date 2026-02-18 · locator § "Rust's Future trait and async/await" — JAX, Triton and CUDA Tile each require a new Python-based DSL/compiler and a break from existing CPU code/libraries; Rust's Future trait already encodes structured, composable concurrency without committing to an execution model, so it can be run unchanged on the GPU and reuse the existing async ecosystem (they ported the `Embassy` embedded executor with very few changes) — while acknowledging it still carries the same function-coloring problem async/await has on the CPU Quote: "We believe Rust's Future trait and async/await provide such an abstraction. They encode structured concurrency directly in an existing language without committing to a specific execution model." [`b-sb21-f008808-c1`, team b]
- Positions seen by the extractor (`b-sb21-f008808-q1`): reuse-existing-async-model-over-new-dsl (VectorWare)

### `greptimedb-write-api-choice`

**Question.** When writing data to GreptimeDB from Rust, should an application use the low-latency Regular write API or the high-throughput Bulk Stream Insert API, and how should parallelism and compression be tuned for each?

- Teams: b · members (context): `b-sb25-f012642-q1` (f012642, other)
- Domains: other
- Concepts: GreptimeDB ingester; write API design; backpressure; compression tradeoffs
- Positions:
  - `greptimedb-write-api-choice--p1` — pick the write API by workload shape (Regular for low-latency/small-batch, Bulk for high-throughput/delay-tolerant), and tune parallelism/compression to the actual bottleneck rather than using one default configuration
    - **Jiachun Feng (Co-Founder, Greptime)** · Source `f012642` · date 2025-07-30 · locator "Summary" and "When to Use Which API" sections — presents a benchmark (2M rows, 22-field log schema) showing Bulk API at 155,099 rows/s versus Regular API at 104,237 rows/s (about 49% faster) under compression, then gives a decision table by use case (real-time alerting/IoT/dashboards → Regular; ETL/log collection/historical import → Bulk) and separate tuning guidance: match `parallelism` to whether the workload is network- or CPU-bound, and choose Zstd over LZ4 only when bandwidth, not CPU, is the constraint Quote: "Bulk API is more suitable for scenarios requiring higher throughput and can tolerate some latency" [`b-sb25-f012642-c1`, team b]
- Positions seen by the extractor (`b-sb25-f012642-q1`): choose per-scenario — Regular API for real-time/interactive/small-batch workloads where low latency matters more than throughput; Bulk Stream Insert API for batch/ETL/historical/log-ingestion workloads that can tolerate latency in exchange for throughput, tuning parallelism to whichever of network or CPU is the bottleneck and compression (Zstd vs LZ4 vs none) to whichever of bandwidth or CPU is scarcer

### `grouped-vs-field-optionality`

**Question.** When several related query parameters only make sense together, should an extractor treat the whole group as one optional unit (all-or-nothing), or should each field be wrapped in `Option` individually?

- Teams: b · members (context): `b-sb08-f002538-q1` (f002538, web)
- Domains: web
- Concepts: query extractors; `Option<T>` extractor pattern; request parsing
- Positions:
  - `grouped-vs-field-optionality--p1` — grouped-optionality
    - **taladar** · Source `f002538` · date 2025-01-14 · locator comment 2025-01-14T14:21:43Z — when several query params only make sense together, wants to know if all were specified as a group rather than checking several individual Option fields Quote: "Semantically 99% of the time when I even want several query parameters stored in the same value I want to know if all of them have been specified though, not a mess of several `Option` values" [`b-sb08-f002538-c1`, team b]
  - `grouped-vs-field-optionality--p2` — field-level-optionality
    - **Turbo87** · Source `f002538` · date 2025-01-14 · locator comment 2025-01-14T14:17:35Z — recommends wrapping each query field individually in Option rather than a whole-group optional extractor, since that best reflects how query parameters actually work Quote: "I would recommend to wrap all your query fields with Option instead, since that best reflects reality of how query parameters work." [`b-sb08-f002538-c2`, team b]
    - **jplatte** · Source `f002538` · date 2025-01-14 · locator comment 2025-01-14T18:44:03Z — has never seen a real case where a set of query parameters is optional as a whole group rather than individually Quote: "I have never seen a set of query parameters that are optional _as a group_, rather than individually." [`b-sb08-f002538-c3`, team b]
- Positions seen by the extractor (`b-sb08-f002538-q1`): grouped-optionality (taladar), field-level-optionality (Turbo87, jplatte)

### `gui-accessibility-first-class`

**Question.** When choosing or building a Rust GUI framework, should Windows support and screen-reader/IME accessibility be treated as a first-class, load-bearing requirement rather than an afterthought?

- Teams: b · members (context): `b-sb21-f008390-q4` (f008390, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: screen reader accessibility (Windows Narrator); IME input; cross-platform parity
- Positions:
  - `gui-accessibility-first-class--p1` — first-class-requirement
    - **boringcactus (Melody)** · Source `f008390` · date 2025-04-16 · locator § intro (context-setting) / § "digression: the irony you may have noticed" — most of the 43 surveyed libraries fail Windows support, screen-reader accessibility, or IME input (or all three); the author treats these as core seriousness criteria for evaluating a GUI framework, not nice-to-haves Quote: "if Windows support is lower on your roadmap than trend chasing AI bullshit, you are not serious." [`b-sb21-f008390-c4`, team b]
- Positions seen by the extractor (`b-sb21-f008390-q4`): first-class-requirement (boringcactus / Melody)

### `gui-custom-renderer-vs-native`

**Question.** should a Rust GUI framework build its own modular rendering engine rather than wrap native platform widgets or an existing browser engine?

- Teams: a · members (context): `a-sa26-f011305-q6` (f011305, desktop-cli-ui, frontend)
- Domains: desktop-cli-ui, frontend
- Concepts: GUI rendering; native widgets vs custom renderer
- Positions:
  - `gui-custom-renderer-vs-native--p1` — build a custom modular GPU-based renderer rather than reuse an existing engine
    - **Jonathan Kelly** · Source `f011305` · date 2025-10-03 · locator ~17:09-18:10 — Dioxus's Blitz renderer alternates native system widgets with a custom GPU-based drawing layer, positioned against unnamed "existing solutions" as free, open-source, and modular Quote: "unlike existing solutions, Blitz is free, open source, and extremely modular" [`a-sa26-f011305-c6`, team a]
- Positions seen by the extractor (`a-sa26-f011305-q6`): build-custom-modular-renderer (Jonathan Kelley, re: "Blitz")

### `hal-expose-private-facilities`

**Question.** When a HAL keeps a needed low-level facility private (cache writeback, DMA interrupts for a driver-owned channel), should users drop to the PAC / copy private code, or should the HAL expose a public version?

- Teams: b · members (context): `b-sT05-f002499-q4` (f002499, embedded)
- Domains: embedded
- Concepts: HAL vs PAC; API surface; unsafe register access
- Positions:
  - `hal-expose-private-facilities--p1` — HAL should expose a public version of the private cache-flush function
    - **yanshay** · Source `f002499` · date 2026-02-02 · locator comment 2026-02-02T16:13:30Z — had to copy a private function definition to flush PSRAM cache; Dominaezzz answered with esp-hal#3982 Quote: "worth making some public version available, it is required" (flag: voice-unverified) [`b-sT05-f002499-c8`, team b]
- Positions seen by the extractor (`b-sT05-f002499-q4`): HAL should expose a public version (PAC workaround advised as instruction only)

### `handle-identity-traits-vs-store-methods`

**Question.** When a wrapper/handle type's "true" identity requires dereferencing store-owned state that isn't safely reachable from the handle alone, should identity comparison be implemented as the standard `PartialEq`/`Eq`/`Hash` traits on the bare handle, or as separate methods that take an explicit store borrow?

- Teams: b · members (context): `b-sb16-f005000-q2` (f005000, wasm, core)
- Domains: core, wasm
- Concepts: trait-based equality; store-scoped state; handle types; identity keys
- Positions:
  - `handle-identity-traits-vs-store-methods--p1` — store-scoped-explicit-methods
    - **cfallin** · Source `f005000` · date 2026-08-13 · locator comment @cfallin 2026-08-13T17:28:44Z — objects that pointer-identity equality on the bare `Func` is surprising because it doesn't hold across import/export boundaries even for the same underlying function, and argues that correct identity needs a store borrow, so it should be separate methods rather than literal `Eq`/`Hash` trait impls. Quote: "equality (and hashing) *should* hold when a `Func` refers to the same function within a store, regardless how it's reached... we need to provide separate methods on the `Func` for this." [`b-sb16-f005000-c7`, team b]
    - **smarcd** · Source `f005000` · date 2026-08-13 · locator comment @smarcd 2026-08-13T17:43:55Z — agrees, replaces the trait impls with `Func::is_same(&store, ...)` and `Func::identity_key(&store)`, dereferencing into the `VMFuncRef`'s own identity so import/export copies of the same function compare equal. Quote: "pushed `Func::is_same(store, a, b)` and `Func::identity_key(store)` in place of the trait impls." [`b-sb16-f005000-c8`, team b]
  - `handle-identity-traits-vs-store-methods--p2` — exclude-lazily-populated-field-from-identity-key
    - **smarcd** · Source `f005000` · date 2026-08-14 · locator comment @smarcd 2026-08-14T05:14:00Z — discovers that one candidate identity-key field (`wasm_call`) starts as `None` and is filled in place later, so it can't safely be used alone as a hash/identity key (it would collide two never-imported functions, and change a function's own key mid-lifetime); keeps `(vmctx, array_call)` plus `type_index` instead. Quote: "Two never-imported host functions both read `wasm_call = None`, so they'd collide... Even a single `Func`'s key would change over the store's lifetime as it flips `None → Some`, which breaks `HashMap` use outright." [`b-sb16-f005000-c9`, team b]
- Positions seen by the extractor (`b-sb16-f005000-q2`): implement-standard-traits-on-bare-handle (smarcd, initial), store-scoped-explicit-methods (cfallin, smarcd revised)

### `hardware-interrupt-scheduling`

**Question.** Should a real-time Rust scheduler drive task dispatch from hardware interrupt priority hardware (NVIC/CLIC) rather than a software kernel, the way most RTOSes do?

- Teams: a · members (context): `a-sB01-f000227-q2` (f000227, embedded)
- Domains: embedded
- Concepts: Stack-Resource-Policy; static-priority-ceiling; zero-cost-scheduling
- Positions:
  - `hardware-interrupt-scheduling--p1` — hardware-interrupt-driven (SRP-based) scheduling preferred over software-kernel scheduling
    - **RTIC developers** · Source `f000227` · date undated (living doc) · locator Preface, "RTIC the hardware accelerated real-time scheduler" — Argues the Cortex-M hardware interrupt/priority model maps directly onto Stack Resource Policy scheduling, giving zero-cost, compile-time-computed ceilings, and states this is why SRP-based scheduling is out of reach for a "thread based RTOS" Quote: "In this way RTIC fuses SRP based preemptive scheduling with a zero-cost hardware accelerated implementation" [`a-sB01-f000227-c2`, team a]
- Positions seen by the extractor (`a-sB01-f000227-q2`): hardware-interrupt-driven (SRP-based) scheduling preferred over software-kernel scheduling

### `hook-api-pointer-vs-address`

**Question.** Should a low-level allocator-hook API pass the raw pointer type (`*mut u8`) through to callbacks, or reduce it to an address (`usize`) since only the address is needed?

- Teams: a · members (context): `a-sa11-f004512-q2` (f004512, embedded)
- Domains: embedded
- Concepts: API design; information preservation vs. minimalism
- Positions:
  - `hook-api-pointer-vs-address--p1` — keep the raw pointer type in the hook API rather than reducing to an address
    - **renkenono** · Source `f004512` · date 2026-04-01 · locator comment 2026-04-01T19:15:29Z — questions why the hook parameter is `usize` rather than `*mut u8`, arguing the pointer should be passed as-is to avoid loss of information, with the caller trusted not to alter it Quote: "It makes sense to provide the pointer as-is to the hooks IMO to avoid loss of information" [`a-sa11-f004512-c2`, team a]
  - `hook-api-pointer-vs-address--p2` — an address is sufficient information for the hook
    - **bugadani** · Source `f004512` · date 2026-04-01 · locator comment 2026-04-01T20:06:56Z — responds to renkenono's pointer-type objection by saying they aren't sure what more information the hook would need beyond the address Quote: "I'm not entirely sure what information you need other than the pointer's address" [`a-sa11-f004512-c3`, team a]
- Positions seen by the extractor (`a-sa11-f004512-q2`): keep the pointer type to avoid loss of information, the caller shouldn't alter it anyway; vs. an address is all the information a tracking hook actually needs

### `host-and-embedded-cargo-layout`

**Question.** Cargo project layout when combining a host crate and an embedded/different-toolchain crate

- Teams: a · members (context): `a-sR14-f004865-q1` (f004865, embedded)
- Domains: embedded
- Concepts: none given
- Positions:
  - `host-and-embedded-cargo-layout--p1` — separate-projects
    - **Klaehn** · Source `f004865` · date 2026-07-02 · locator "Basic setup" section — keep host and embedded (cross-compiled) code in fully separate, non-workspace Cargo projects when toolchains differ and a patched dependency is needed for one side only. Quote: "Note that we need different toolchains and want to keep the option to use a patch of iroh for the ESP32 variant, so the two directories are completely separate Rust projects. We do not use a workspace." [`a-sR14-f004865-c1`, team a]
- Positions seen by the extractor (`a-sR14-f004865-q1`): separate-projects (Klaehn)

### `http-body-unknown-size`

**Question.** When a response body's size cannot be determined without expensive computation, should an HTTP framework represent that as a distinct "unknown size" state, or default to treating it the same as a known-empty body?

- Teams: a · members (context): `a-sa12-f004637-q1` (f004637, web, core)
- Domains: core, web
- Concepts: api-design; option-semantics; http-body-trait
- Positions:
  - `http-body-unknown-size--p1` — distinguish-unknown-from-zero
    - **lorenzleutgeb** · Source `f004637` · date 2026-05-02 · locator axum issue #3741, comment 2026-05-02T11:59:01Z — proposes changing `impl IntoResponse for ()` to use `Body::unknown()` instead of `Body::empty()`, so a handler that can't cheaply determine its length on a HEAD request doesn't get a spurious `content-length: 0`, arguing the current special-casing is conceptually wrong Quote: "Special casing responses with `content-length: 0` is conceptually problematic." [`a-sa12-f004637-c1`, team a]
  - `http-body-unknown-size--p2` — cautious-narrow-fix
    - **davidpdrsn (axum maintainer)** · Source `f004637` · date 2026-05-02 · locator axum issue #3741, comment 2026-05-02T12:49:09Z — resists making `()` default to an unknown body size because it could silently change behavior for unrelated responses; wants a fix that works for users unfamiliar with axum's APIs rather than one requiring them to opt in explicitly Quote: "Changing `()` to have an unknown body size feels too broad to me. I worry that might impact other responses using `()` that don't care about HEAD requests." [`a-sa12-f004637-c2`, team a]
- Positions seen by the extractor (`a-sa12-f004637-q1`): distinguish-unknown-from-zero (lorenzleutgeb, proposed Body::unknown()), collapse-to-known-zero (status quo, http_body_util::Empty)

### `impl-trait-syntax-reuse`

**Question.** Was reusing the same `impl Trait` syntax for both return-position (RPIT) and argument-position (APIT) impl Trait a language design mistake?

- Teams: a · members (context): `a-sa30-f013276-q3` (f013276, core)
- Domains: core
- Concepts: impl Trait; APIT; RPIT; opaque types; syntax design
- Positions:
  - `impl-trait-syntax-reuse--p1` — apit-syntax-reuse-was-a-mistake
    - **quinedot — track record not established from this source** · Source `f013276` · date 2024-12-06 · locator post 2024-12-06T01:21:37.914Z, footnote 3 — states as a personal view that argument-position impl Trait (APIT) sharing the same `impl Trait` syntax as return-position impl Trait (RPIT) was a design mistake Quote: "one of a few reasons why some, myself included, feel that APIT was a mistake (at a minimum in terms of sharing the same syntax)" [`a-sa30-f013276-c2`, team a]
- Positions seen by the extractor (`a-sa30-f013276-q3`): "yes, at least in terms of sharing the same syntax" (quinedot, stated as a personal aside) — single-sided, no counter in this source

### `incremental-invalidation-redesign`

**Question.** Should the Rust compiler's/Cargo's incremental-rebuild invalidation be redesigned around explicit "atomic level" targets (AST/HIR/MIR/codegen) plus separately-tracked data dependencies (e.g. codegen flags), instead of today's coarser per-flag/per-command invalidation?

- Teams: a · members (context): `a-sa18-f008694-q1` (f008694, core)
- Domains: core
- Concepts: incremental-compilation; query-system; dependency-graph; cargo-check-vs-build; compile-times
- Positions:
  - `incremental-invalidation-redesign--p1` — redesign-around-atomic-levels-and-data-dependencies
    - **Alejandra González** · Source `f008694` · date 2025-11-04 · locator talk script, "atomic levels and data dependencies" section onward — a Clippy-team performance contributor pitches representing what stage a compilation needs (AST/HIR/MIR/codegen) as an explicit "atomic level" tag, plus tracking fine-grained "data dependencies" (e.g. link-time-optimization flags) separately, so `cargo check`/`clippy`/`build` stop redoing each other's work from scratch, and describes a further "two-stage fingerprint" (rebuild only to name-resolution to check if a dependent actually used a changed definition) to cut needless dependent rebuilds Quote: "So LTO options wouldn't impact clippy, for example." [`a-sa18-f008694-c1`, team a]
- Positions seen by the extractor (`a-sa18-f008694-q1`): redesign-around-atomic-levels-and-data-dependencies

### `incremental-port-vs-rewrite-to-rust`

**Question.** Port performance-critical JS incrementally into Rust, or rewrite the whole app?

- Teams: a · members (context): `a-sB02-f000256-q1` (f000256, web, wasm)
- Domains: wasm, web
- Concepts: incremental adoption
- Positions:
  - `incremental-port-vs-rewrite-to-rust--p1` — incremental-port-only-hot-paths
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Why Rust and WebAssembly?" — "Do Not Rewrite Everything" — existing JS code bases don't need to be thrown away; port the most performance-sensitive functions to Rust for immediate benefit, and you can stop there if you want. Quote: "Existing code bases don't need to be thrown away." [`a-sB02-f000256-c1`, team a]
- Positions seen by the extractor (`a-sB02-f000256-q1`): incremental-port-only-hot-paths

### `infrastructure-from-code-vs-iac`

**Question.** Should a Rust service's infrastructure (e.g. its database) be provisioned from annotations in the Rust code itself (infrastructure-from-code, Shuttle), or by separate Docker or IaC tooling such as Terraform?

- Teams: b · members (context): `b-sT09-f011688-q2` (f011688, cloud-workers, web)
- Domains: cloud-workers, web
- Concepts: shuttle_runtime; shuttle_shared_db; infrastructure from code; Docker; Terraform
- Positions:
  - `infrastructure-from-code-vs-iac--p1` — provision infrastructure from code annotations over Docker or Terraform
    - **Joshua Mo (Shuttle)** · Source `f011688` · date 2024-01-23 · locator § Adding a database, paragraph after the first code block — the `#[shuttle_shared_db::Postgres]` annotation is presented as "pretty simple" next to running Docker locally and managing Postgres by hand or with Terraform in production Quote: "In production, you would also need to manually instantiate and manage your Postgres instance or rely on an IaC (infrastructure as code) tool like Terraform." (flag: voice-unverified) [`b-sT09-f011688-c2`, team b]
- Positions seen by the extractor (`b-sT09-f011688-q2`): provision from code annotations

### `instant-min-max`

**Question.** Should `Instant` expose fixed extremal values (MIN/MAX), given it has no fixed reference epoch?

- Teams: a · members (context): `a-sa19-f009196-q1` (f009196, core)
- Domains: core
- Concepts: time APIs; Instant; SystemTime; monotonic clocks; saturating arithmetic
- Positions:
  - `instant-min-max--p1` — oppose-instant-extrema-fraught
    - **the8472** · Source `f009196` · date 2024-08-15 · locator reply, 2024-08-15T23:11:10.007Z — SystemTime::MIN/MAX might be reasonable, but Instant values aren't portable and aren't stable across reboots, so exposing extrema is more hazardous than SystemTime's case. Quote: "For SystemTime this might be reasonable to have, but the values wouldn't be portable. I think Instant would be more hazardous..." [`a-sa19-f009196-c1`, team a]
    - **farnz** · Source `f009196` · date 2024-08-16 · locator reply, 2024-08-16T08:43:34.961Z — Instant's current API contract does not guarantee a fixed reference time; a conforming implementation could start/stop its reference timer dynamically, so a MIN value wouldn't reliably denote a stable point in time. Quote: "This assumes that there is a fixed reference time for Instant, which isn't technically required at the moment." [`a-sa19-f009196-c2`, team a]
  - `instant-min-max--p2` — instant-extrema-fraught-prefer-saturating-ops
    - **burntsushi** · Source `f009196` · date 2024-08-16 · locator reply, 2024-08-16T13:04:57.183Z — SystemTime::MIN/MAX seem reasonable; Instant::MIN/MAX seem fraught for the reasons already raised, so proposes adding saturating arithmetic methods directly on Instant instead of exposing its extrema. Quote: "SystemTime::MIN and SystemTime::MAX seem reasonable to me... Instant::MIN and Instant::MAX seem fraught, for reasons already discussed." [`a-sa19-f009196-c3`, team a]
  - `instant-min-max--p3` — support-instant-bound-for-saturating-arithmetic
    - **kevincox** · Source `f009196` · date 2024-08-16 · locator reply, 2024-08-16T13:23:59.223Z — Wants an Instant minimum/maximum (or equivalent) to support saturating arithmetic in a token-bucket rate limiter, where moving a timestamp below the representable minimum should saturate rather than panic. Quote: "For my use case it is preferable to saturate." [`a-sa19-f009196-c4`, team a]
- Positions seen by the extractor (`a-sa19-f009196-q1`): oppose-instant-extrema-fraught; instant-extrema-fraught-prefer-saturating-ops; support-instant-bound-for-saturating-arithmetic

### `internal-hazmat-api-for-performance`

**Question.** When a crate's public API doesn't support an operation needed for performance (here, batch-hashing many small blobs with BLAKE3's SIMD `hash_many`), should a practitioner reach into the crate's internal/"hazmat" API and accept unchecked, precondition-violating footguns (silently wrong results rather than a panic on some platforms) for a large speedup, or stay within the safe public API and accept lower throughput?

- Teams: a · members (context): `a-sR09-f003702-q1` (f003702, decentralized-iroh, core)
- Domains: core, decentralized-iroh
- Concepts: internal/hazmat API access; unchecked preconditions; SIMD (`Platform::hash_many`); performance vs. API safety guarantees
- Positions:
  - `internal-hazmat-api-for-performance--p1` — it is worth bypassing BLAKE3's public API and using its internal `Platform::hash_many` SIMD entry point to batch-hash many small blobs, even though the internal function has unchecked preconditions that silently produce wrong results (rather than panicking) on real SIMD platforms
    - **Rüdiger Klaehn (n0, iroh/iroh-blobs)** · Source `f003702` · date 2025-10-15 · locator § "Using the internal platform API" and the note under § "Putting it all together" — after finding the public BLAKE3 API has no support for hashing multiple independent blobs at once, the author repurposes the internal, precondition-checked-only-outside `hash_many` SIMD entry point to get a 17x combined SIMD+rayon speedup over sequential hashing, explicitly noting the internal function will silently produce wrong results if its constraints (chunk count a multiple of `MAX_SIMD_DEGREE`, chunk length a multiple of `BLOCK_LEN`) are violated on a real SIMD platform, versus panicking on the portable fallback. Quote: "This is to be expected since we are using an internal API and preconditions are checked further outside." [`a-sR09-f003702-c1`, team a]
- Positions seen by the extractor (`a-sR09-f003702-q1`): "worth reaching into the internal API and accepting the footgun for the speedup" (Rüdiger Klaehn / n0)

### `internal-service-abstraction-trait`

**Question.** Should internal communication between a Rust application's components go through a service-abstraction trait (e.g. tower::Service), or via direct calls/shared state?

- Teams: b · members (context): `b-bk03-f000267-q4` (f000267, distributed, core)
- Domains: core, distributed
- Concepts: tower; Service trait; backpressure; async architecture
- Positions:
  - `internal-service-abstraction-trait--p1` — service-abstraction-internally
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Design Overview § Architecture; State Updates RFC § Guide-level explanation — all communication between Zebra's stateful components (state, mempool, verifiers, RPC) is handled through an internal asynchronous request/response abstraction built on a Buffered tower::Service, described as running as "microservices in one process," rather than through direct calls or shared state; the design note explains this keeps "internal" rocksdb behaviors from leaking into the "external" API, so the backing store stays replaceable Quote: "internal asynchronous RPC abstraction (\"microservices in one process\")" (flag: voice-unverified) [`b-bk03-f000267-c4`, team b]
- Positions seen by the extractor (`b-bk03-f000267-q4`): service-abstraction-internally

### `intra-doc-links`

**Question.** Should Rust doc comments reference types and functions via intra-doc links, or as plain text?

- Teams: b · members (context): `b-bk03-f000267-q14` (f000267, core)
- Domains: core
- Concepts: rustdoc; intra-doc links; documentation tooling
- Positions:
  - `intra-doc-links--p1` — use-rustdoc-intra-doc-links
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Doing Mass Renames in Zebra Code § Using rustdoc links to detect name changes — doc comments should reference types and functions via rustdoc intra-doc links rather than plain text, both for navigability and because the rustdoc lint will then catch a typo'd or renamed reference that plain text would silently leave stale Quote: "This makes the documentation easier to navigate, and our rustdoc lint will detect any typos or name changes." (flag: voice-unverified) [`b-bk03-f000267-c16`, team b]
- Positions seen by the extractor (`b-bk03-f000267-q14`): use-rustdoc-intra-doc-links

### `io-safety-op-placement-in-main`

**Question.** When an operation must run before any other file descriptor could occupy a reused slot (an I/O-safety hazard), must it happen at the very start of `main()`, or is "early enough, with nothing intervening" sufficient?

- Teams: a · members (context): `a-sa14-f005079-q1` (f005079, core)
- Domains: core
- Concepts: I/O safety; file descriptor lifetime; unsafe invariants
- Positions:
  - `io-safety-op-placement-in-main--p1` — an I/O-safety-critical operation must run at the very start of `main`
    - **bjorn3** · Source `f005079` · date 2026-09-07 · locator comment 2026-09-07T21:21:42Z — argues the fd-inheritance setup should be called at the start of main to ensure no other fd takes the place of a missing one, framing it as an I/O-safety violation otherwise Quote: "This should probably be called at the start of main to ensure no other fd takes the place of a missing fd, violating I/O-safety." [`a-sa14-f005079-c1`, team a]
  - `io-safety-op-placement-in-main--p2` — exact placement doesn't need to be enforced as long as nothing intervenes
    - **alexcrichton** · Source `f005079` · date 2026-09-08 · locator comment 2026-09-08T18:52:06Z — pushes back that it isn't worth contorting the CLI to guarantee this happens literally at the start of `fn main`, since Wasmtime controls all CLI entrypoints and the current placement during startup/CLI processing is fine Quote: "I wouldn't sweat this too much. I don't think it's worth contorting Wasmtime's CLI to make it apparent that this is happening right as `fn main` starts" [`a-sa14-f005079-c2`, team a]
- Positions seen by the extractor (`a-sa14-f005079-q1`): it must run at the very start of `main` to guarantee no other fd takes the missing slot first, vs. don't over-engineer visible placement — anywhere during startup/CLI processing is fine as long as nothing happens in between

### `jit-code-alignment`

**Question.** What function/code alignment should a JIT-style code generator use to avoid wasting instruction-fetch bandwidth?

- Teams: b · members (context): `b-sR04-f001401-q1` (f001401, wasm)
- Domains: wasm
- Concepts: code generation; cache-line alignment; instruction fetch; JIT compilation
- Positions:
  - `jit-code-alignment--p1` — 32-byte-default-reasonable
    - **cfallin (Chris Fallin)** · Source `f001401` · date 2024-05-14 · locator issue comment, 2024-05-14T17:03:22Z — the CPU frontend fetches aligned 32B/64B chunks, so a function starting mid-chunk wastes fetch bandwidth; he suspects 32-byte function alignment (Cranelift/Wasmtime x86-64 currently uses 16-byte) would be a more reasonable default in general. Quote: "I suspect a 32B function alignment would be a pretty reasonable default in general" [`b-sR04-f001401-c1`, team b]
- Positions seen by the extractor (`b-sR04-f001401-q1`): 32-byte-default-reasonable

### `js-tooling-in-rust`

**Question.** for developer tooling that serves the JavaScript/TypeScript ecosystem (linters, formatters, bundlers, parsers), should the tool itself be implemented in Rust rather than in JavaScript/TypeScript?

- Teams: b · members (context): `b-sb26-f012866-q1` (f012866, web, frontend, wasm)
- Domains: frontend, wasm, web
- Concepts: JS/TS tooling; Rust-for-tooling; WebAssembly bridge
- Positions:
  - `js-tooling-in-rust--p1` — Rust is the standout choice specifically for building JavaScript/TypeScript tooling and infrastructure
    - **Stefan Baumgartner** · Source `f012866` · date 2026-01-28 (quoted in this JetBrains post; his own original statement's date is not given in the captured text) · locator pull-quote in section "JavaScript / TypeScript," attributed "Author of the TypeScript Cookbook and TypeScript in 50 Lessons" — identifies performance as the most significant unsolved issue in the JS/TS tooling ecosystem, and states that Rust's language- and compiler-level safeguards make it easier to build successful tools in the first place, not just faster ones Quote: "Rust is undoubtedly the big star in JavaScript and TypeScript tooling and infrastructure. It addresses the most significant issue in the current tooling ecosystem: performance." [`b-sb26-f012866-c1`, team b]
  - `js-tooling-in-rust--p2` — replace established JavaScript-based tooling (Prettier, ESLint) with a Rust-implemented toolchain for better performance and a more consistent developer experience
    - **Denis Bezrukov** · Source `f012866` · date 2026-01-28 (quoted in this post) · locator pull-quote in section "Common Use Cases and Projects," attributed "Core Contributor in Biome" — states Biome's explicit goal is replacing Prettier/ESLint-style JS tooling with a Rust implementation, framing the payoff as both raw speed and a more consistent DX than the JS tools it replaces Quote: "Biome aims to replace existing JavaScript tooling like Prettier and ESLint with a Rust-implemented toolchain that offers better performance and a more consistent developer experience." [`b-sb26-f012866-c2`, team b]
- Positions seen by the extractor (`b-sb26-f012866-q1`): yes — Rust is "the big star" of JS/TS tooling and infrastructure specifically because of performance and compiler-enforced safeguards (Stefan Baumgartner, author of the TypeScript Cookbook); practiced directly by replacing JS-based tooling (Prettier, ESLint) with a Rust-implemented toolchain for performance and DX consistency (Denis Bezrukov, Biome core contributor)

### `keyed-access-copy-vs-clone-keys`

**Question.** Should a keyed-collection access API constrain key types to `Copy` (cheaper, but excludes types like `Arc<str>`), or accept `Clone` key types for flexibility at the cost of occasional clone overhead?

- Teams: b · members (context): `b-sb13-f003963-q2` (f003963, frontend)
- Domains: frontend
- Concepts: generic trait bounds; `Copy` vs `Clone`; keyed collection access; API ergonomics vs cost
- Positions:
  - `keyed-access-copy-vs-clone-keys--p1` — copy-only-keys
    - **TiemenSch** · Source `f003963` · date 2025-12-05 · locator PR description 2025-12-05T21:04:20Z — deliberately requires `Copy` on keys for the new `KeyedAccess` trait, to stop users reaching for `Clone` keys when a cheaper option exists Quote: "I made the assumption that requiring `Copy` on keys is good practice. This refrains users from using `Clone` keys rather than the cheaper options." [`b-sb13-f003963-c3`, team b]
  - `keyed-access-copy-vs-clone-keys--p2` — allow-clone-keys
    - **gbj** · Source `f003963` · date 2025-12-12 · locator comment 2025-12-12T20:16:51Z — argues the trait should also accept `Clone` key types, since cheaply-clonable types like `Arc<str>` are reasonable keys even though cloning large objects is not Quote: "And I would suggest allowing `Clone` key types as well: of course it's not a good idea to clone big objects around, but there are plenty of types like `Arc<str>` that would be reasonable to use as keys and are cheap to clone for this purpose." [`b-sb13-f003963-c4`, team b]
- Positions seen by the extractor (`b-sb13-f003963-q2`): copy-only-keys (TiemenSch), allow-clone-keys (gbj)

### `lambda-release-profile-size`

**Question.** Should a Rust AWS Lambda be built with a size-optimized release profile (`opt-level = "z"`, `lto = true`, `codegen-units = 1`, `panic = "abort"`, `strip`) rather than the default release profile, trading compile time and unwinding for binary size and cold start?

- Teams: a · members (context): `a-sT11-f007659-q1` (f007659, cloud-workers)
- Domains: cloud-workers
- Concepts: Cargo profiles; LTO; panic strategy; binary size; cold start
- Positions:
  - `lambda-release-profile-size--p1` — size-optimized release profile
    - **maahl (maahl.net)** · Source `f007659` · date 2023-11-05 · locator § "Bonus performance improvements" — adopted a size-optimized release profile on feedback from Reddit user u/HenryQFnord, accepting longer compiles and no unwinding, for a smaller binary; measured 3.6 MB → 1.8 MB and cold start 20 ms → 17 ms, and expects larger gains on bigger programs Quote: "Adding all of these options took us from a 3.6MB binary to a 1.8MB one, which should speed up the cold start of the Lambda." (flag: voice-unverified (Rust connection in source: self-reported beginner Rust use, repo with per-section commits)) [`a-sT11-f007659-c1`, team a]
- Positions seen by the extractor (`a-sT11-f007659-q1`): size-optimized profile; default release profile

### `land-hal-separate-now-vs-unified-later`

**Question.** should a new chip-family HAL be merged into the monorepo immediately as its own separate crate to unblock waiting users, or held back until it can be integrated into the unified/combined HAL from the start?

- Teams: b · members (context): `b-sR09-f003955-q1` (f003955, embedded)
- Domains: embedded
- Concepts: none given
- Positions:
  - `land-hal-separate-now-vs-unified-later--p1` — land it as a side crate now; unify later once the shared metapac/combined HAL is ready.
    - **jamesmunns (embassy maintainer)** · Source `f003955` · date 2025-12-04 · locator embassy-rs/embassy#4989, comment 2025-12-04T18:32:46Z. · L817-L820. — land it as a side crate now; unify later once the shared metapac/combined HAL is ready. Quote: "I wanted to get our previously private work upstreamed ASAP (so we can basically deprecate/archive odp/embassy-mcxa). If there's a path to moving mcxa into embassy-nxp, we can do it now that the code is in the same repo." [`b-sR09-f003955-c1`, team b]
  - `land-hal-separate-now-vs-unified-later--p2` — same — merge as-is now, deprecate in favor of the unified HAL once ready.
    - **felipebalbi (NXP embedded engineer, embassy-nxp contributor)** · Source `f003955` · date 2025-12-04 · locator embassy-rs/embassy#4989, comment 2025-12-04T18:35:15Z. · L824-L827. — same — merge as-is now, deprecate in favor of the unified HAL once ready. Quote: "The idea is that we can get this merged as is, once the metapac is ready, we can switch to it. Then once the combined HAL is ready, it shouldn't be a big deal to deprecate this and have users switch." [`b-sR09-f003955-c2`, team b]
- Positions seen by the extractor (`b-sR09-f003955-q1`): land it as a side crate now; unify later once the shared metapac/combined HAL is (jamesmunns (embassy maintainer)); same — merge as-is now, deprecate in favor of the unified HAL once ready. (felipebalbi (NXP embedded engineer, embassy-nxp contributor))

### `language-safety-vs-hw-isolation`

**Question.** Does Rust's memory safety meaningfully substitute for hardware/OS-level address-space isolation when running untrusted or mutually adversarial code in one process (single-address-space "libOS" designs)?

- Teams: a · members (context): `a-saL1-f005360-q2` (f005360, distributed, embedded, core)
- Domains: core, distributed, embedded
- Concepts: memory safety; sandboxing untrusted code; unikernels/library operating systems; capabilities and effects systems
- Positions:
  - `language-safety-vs-hw-isolation--p1` — language-safety-insufficient-for-untrusted-code
    - **matklad** · Source `f005360` · date 2024-10-15 · locator reply, 2024-10-15T10:57:36-05:00 — Rejects that Rust provides "language-level safety" sufficient for running mutually adversarial code in one address space; Rust protects against accidental misuse ("holding it wrong"), not deliberate misuse, which is what true fine-grained security would require. Quote: "We don't have language-level safety. Rust protects a user from 'holding it wrong,' but it doesn't protect from intentional misuse." [`a-saL1-f005360-c4`, team a]
    - **lonjil** · Source `f005360` · date 2024-10-15 · locator reply, 2024-10-15T13:39:05-05:00 — Argues language-level capabilities/effect systems can't solve multi-tenant isolation unless literally all code sharing the address space is such trusted, unsafe-forbidden code compiled by a trusted compiler; viable for a single-application unikernel, not for many mutually distrusting applications together. Quote: "Rust and (language-level) capabilities and effect systems are incapable of solving the problem unless absolutely all the code is such Rust code and unsafe is forbidden... Very viable for single application unikernel stuff, but not viable for many applications in the same address space." [`a-saL1-f005360-c6`, team a]
  - `language-safety-vs-hw-isolation--p2` — language-safety-a-major-step-toward-safe-libos
    - **dist1ll** · Source `f005360` · date 2024-10-15 · locator reply, 2024-10-15T13:13:15-05:00 — Concedes Rust "might not be there yet" for full language-level security, but argues it already solved the hardest combined problem (safety plus performance) needed to make a high-performance library-OS design viable, with missing pieces like capabilities/effects systems emerging next. Quote: "Rust might not be there yet, but it solved some of the hardest problems (safety + performance) that make a high-performance libOS not a total nightmare." [`a-saL1-f005360-c5`, team a]
- Positions seen by the extractor (`a-saL1-f005360-q2`): language-safety-insufficient-for-untrusted-code; language-safety-a-major-step-toward-safe-libos

### `large-pr-split`

**Question.** One large PR, or split into small PRs?

- Grouping: Same choice; the team-a member is removed as Claim-less.
- Teams: b · members (context): `b-sb08-f002518-q2` (f002518, ml, core)
- Domains: core, ml
- Concepts: contribution review process; PR granularity
- Positions:
  - `large-pr-split--split-into-small-prs` — Split before merging
    - **ivarflakstad** · Source `f002518` · date 2026-06-21 · locator comment 2026-06-21T09:32:07Z — reviewing one huge combined branch is hard and risky; better to treat it as a development hub and extract small isolated PRs for merging Quote: "I think having this branch as the hub where backwards cuda compatibility is developed - and then extract only the required code into isolated PRs is a good way to get the improvements merged." [`b-sb08-f002518-c3`, team b]
- Positions seen by the extractor (`b-sb08-f002518-q2`): split-into-small-isolated-prs (ivarflakstad)

### `leaky-signal-abstraction-electrical-config`

**Question.** Should an embedded HAL's peripheral-signal abstraction expose electrical-configuration details (drive strength, pull resistors, input/output mode) on the signal type itself, even though this leaks device-specific configuration into what is meant to be a clean peripheral-routing abstraction?

- Teams: a · members (context): `a-sR06-f002005-q1` (f002005, embedded)
- Domains: embedded
- Concepts: peripheral abstraction; leaky abstraction; GPIO signal routing
- Positions:
  - `leaky-signal-abstraction-electrical-config--p1` — the peripheral-signal abstraction is a leaky one that ideally wouldn't exist, but is kept for convenience
    - **bugadani** · Source `f002005` · date 2024-09-10 · locator PR #2128, comment 2024-09-10T08:14:33Z — says peripheral I/O ideally shouldn't need to know about drive strength, pull resistors or input/output mode, and calls the current design a leaky abstraction visible in the null methods `DummyPin`/`Level` must carry. Quote: "Peripheral I/O shouldn't, in an ideal world, care about GPIO drive strength, pull resistors, input/output mode, and this leaky abstraction really shows in the random null methods we must have on DummyPin/Level now." [`a-sR06-f002005-c1`, team a]
- Positions seen by the extractor (`a-sR06-f002005-q1`): "current design is a regretted but accepted leaky abstraction" (bugadani)

### `lightweight-clones-in-language`

**Question.** should Rust adopt a lightweight/automatic-clone mechanism (e.g. reference-counted "generational box" ergonomics) for callback-heavy UI code, trading some compile-time guarantees for runtime checks?

- Teams: a · members (context): `a-sa26-f011305-q3` (f011305, core, frontend, desktop-cli-ui)
- Domains: core, desktop-cli-ui, frontend
- Concepts: ownership; clone ergonomics; async/callbacks
- Positions:
  - `lightweight-clones-in-language--p1` — add lightweight/automatic clone ergonomics to Rust itself
    - **Jonathan Kelly** · Source `f011305` · date 2025-10-03 · locator ~15:06-16:09 — proposed a Rust project goal adding lightweight clones for types like reference-counted smart pointers, prototyped as "generational box"; acknowledges it is contested Quote: "this is a controversial change in the Rust language. Not everyone may agree, but in my opinion, this is critical to the success of high-level Rust" / "Opinions were divided" [`a-sa26-f011305-c3`, team a]
- Positions seen by the extractor (`a-sa26-f011305-q3`): add-lightweight-clones-to-Rust (Jonathan Kelley, proposed as a project goal); opposed-or-skeptical (unnamed — Kelley states "not everyone may agree" and "opinions were divided" without naming the dissenters)

### `lint-allow-broad-vs-narrow`

**Question.** When a macro-generated code path (e.g. `#[tracing::instrument]` reaching a value only through a trait method) triggers a false-positive unused/dead-code lint, should the fix be a broad `#![allow(unused)]` or a narrowly scoped allow on the specific item?

- Teams: a · members (context): `a-sR11-f003983-q1` (f003983, ml, core)
- Domains: core, ml
- Concepts: macros; trait dispatch; lints
- Positions:
  - `lint-allow-broad-vs-narrow--p1` — broad-allow-when-linter-blind-to-trait-indirection
    - **crutcher** · Source `f003983` · date 2025-12-15 · locator comment 2025-12-15T20:40:52Z — the blanket `#[allow(unused)]` stays because the compiler's lint can't see that `TensorMetadata` trait operations are being consumed via `#[tracing::instrument]`, so item-level allows would misfire Quote: "Because the rust linter isn't smart enough to understand that `TensorMetadata` trait operations are being used by `#[tracing::instrument]`" [`a-sR11-f003983-c1`, team a]
- Positions seen by the extractor (`a-sR11-f003983-q1`): broad-allow-when-linter-blind-to-trait-indirection (crutcher)

### `lld-default-linker`

**Question.** Should Rust switch its default linker on the most popular target (x86_64-unknown-linux-gnu) from the system linker to a faster non-GNU linker (lld), accepting a small risk of incompatibility?

- Teams: b · members (context): `b-sb23-f009657-q1` (f009657, core)
- Domains: core
- Concepts: linker; rust-lld; compile times; target defaults
- Positions:
  - `lld-default-linker--p1` — make rust-lld the default linker on x86_64-unknown-linux-gnu for stable releases
    - **Rémy Rakic (on behalf of the compiler performance working group)** · Source `f009657` · date 2025-09-01 · locator "Summary, and call for testing" section — after internal testing on CI, crater and nightly since May 2024 with no major issues, the team judges the ~7x incremental-link / 40% end-to-end speedup on the ripgrep benchmark worth the small risk that lld isn't bug-for-bug compatible with GNU ld, keeping an escape hatch (`-C linker-features=-lld`) Quote: "it's a drop-in replacement for the vast majority of cases, but lld is not bug-for-bug compatible with GNU ld" [`b-sb23-f009657-c1`, team b]
- Positions seen by the extractor (`b-sb23-f009657-q1`): switch the default because the speed win is large and the compatibility risk is small and escapable via a flag

### `llm-doc-edits-reproducibility`

**Question.** When using an LLM to bring doc-comment prose in a codebase to a consistent style, should the project make the process reproducible by pinning down and declaring exactly which model, prompt, and environment produced the edits, or should it instead adopt a formal controlled-language writing standard that constrains vocabulary/grammar enough to make the model's "taste" mostly irrelevant?

- Teams: b · members (context): `b-sb16-f004997-q1` (f004997, embedded)
- Domains: embedded
- Concepts: LLM-assisted code review; doc-comment style consistency; controlled natural language; reproducibility
- Positions:
  - `llm-doc-edits-reproducibility--p1` — pre-review-guidelines-for-llms
    - **bjoernQ** · Source `f004997` · date 2026-08-11 · locator PR description @bjoernQ 2026-08-11T12:34:57Z — expects the doc-consistency effort to trigger bikeshedding, and hopes it results in additions to DEVELOPER-GUIDELINES.md that also help LLMs pre-review changes. Quote: "I assume this will end up in a lot of bike-shedding which ideally should result in additions to the DEVELOPER-GUIDELINES.md to (not only) help LLMs in pre-reviewing changes." [`b-sb16-f004997-c1`, team b]
  - `llm-doc-edits-reproducibility--p2` — adopt-controlled-language-standard-ASD-STE100
    - **bugadani** · Source `f004997` · date 2026-08-11 · locator comment @bugadani 2026-08-11T12:39:59Z — proposes mandating a standard like ASD-STE100 Simplified Technical English so the prose style is consistent and free of "flowery nonsense." Quote: "I would also propose mandating some standard we should follow, like ASD-STE100 Simplified Technical English, so that the _style_ of the prose is also consistent, and free of any flowery nonsense." [`b-sb16-f004997-c2`, team b]
    - **bugadani** · Source `f004997` · date 2026-08-12 · locator comment @bugadani 2026-08-12T13:36:48Z — responds that a controlled-language standard largely removes model "taste" from the equation by constraining vocabulary and grammar, offering this as an alternative to MabezDev's process-heavy approach. Quote: "Simplified Technical English pretty much removes taste from the equation, it limits vocabulary and grammar, too." [`b-sb16-f004997-c4`, team b]
  - `llm-doc-edits-reproducibility--p3` — declare-model-prompt-and-clean-env
    - **MabezDev** · Source `f004997` · date 2026-08-12 · locator comment @MabezDev 2026-08-12T13:34:07Z — argues that to merge this kind of LLM-driven doc pass, the project must declare which model was used (since each model has its own "taste"), declare the exact prompt (wording changes the results), and run the update in a clean environment to avoid picking up incidental local agent rules. Quote: "We must declare what model we run this with. Each model has its own interpretation of the rules and its own \"taste\"... We need to declare the prompt we run with this... we should run these updates in a clean env." [`b-sb16-f004997-c3`, team b]
- Positions seen by the extractor (`b-sb16-f004997-q1`): declare-model-prompt-and-clean-env (MabezDev), adopt-controlled-language-standard-ASD-STE100 (bugadani)

### `macro-hides-construction-requirements`

**Question.** Should a macro hide an API's less-friendly construction requirements from the user, or should the API stay explicit even if less ergonomic?

- Teams: b · members (context): `b-sR10-f004804-q2` (f004804, embedded, core)
- Domains: core, embedded
- Concepts: macros; ergonomics vs. transparency
- Positions:
  - `macro-hides-construction-requirements--p1` — macros-may-hide-complexity
    - **bugadani (esp-hal maintainer, PR author)** · Source `f004804` · date 2026-06-15 · locator PR description, 2026-06-15T17:07:50Z — the new reference type makes constructing DMA buffers less friendly directly, but that friction is absorbed by the existing macros so end users don't see it Quote: "It makes constructing buffers a bit less friendly, but that's hidden from us by the macros currently." [`b-sR10-f004804-c3`, team b]
- Positions seen by the extractor (`b-sR10-f004804-q2`): macros-may-hide-complexity

### `macro-ide-tooling`

**Question.** should Rust macros get first-class IDE tooling (autocomplete, hover, partial expansion) via new mechanisms, or is today's macro opacity accepted as a tradeoff for macro power?

- Teams: a · members (context): `a-sa26-f011305-q4` (f011305, core)
- Domains: core
- Concepts: macros; DSLs; IDE tooling
- Positions:
  - `macro-ide-tooling--p1` — build new tooling rather than accept macro IDE opacity
    - **Jonathan Kelly** · Source `f011305` · date 2025-10-03 · locator ~13:06 — since Rust macros don't support autocomplete or partial expansion, they built a separate library ("partial expressions") to give macro-based DSLs IDE support Quote: "Rust macros do not support things like autocomplete and partial expansion. So we developed new libraries, such as partial expressions, to make it easier to write high-quality Rust DSLs" [`a-sa26-f011305-c4`, team a]
- Positions seen by the extractor (`a-sa26-f011305-q4`): build-new-tooling-for-macro-IDE-support (Jonathan Kelley, re: "partial expressions" library)

### `memory-safety-design-priority`

**Question.** Did Rust's design correctly prioritize memory safety as its one "hard problem," and is that tradeoff fair against other capabilities (e.g., metaprogramming/expressiveness) that consequently matured more slowly?

- Teams: a · members (context): `a-sa28-f012469-q3` (f012469, core)
- Domains: core
- Concepts: memory safety; metaprogramming; language design tradeoffs
- Positions:
  - `memory-safety-design-priority--p1` — rust-over-invested-in-safety-at-cost-of-metaprogramming
    - **Andrei Alexandrescu (creator of D) — Voice-eligibility caveat: no confirmed Rust track record per subject scope rules (maintains no Rust crate, no Rust role found in this source); logged per rule 5 (exact names, don't invent), eligibility left for merge/audit to rule on** · Source `f012469` · date reddit comment undated in source, reposted 2015-09-01 · locator post by @llogiq dated 2015-09-01T01:17:54Z, sourced "on reddit" — argues Rust spent so much of its design budget on memory-safety that it became lopsided, with little else developed Quote: "the language had to dedicate so much real estate to this (difficult) problem alone, it became a disharmonic creature with one bulging muscle and little of anything else" [`a-sa28-f012469-c5`, team a]
  - `memory-safety-design-priority--p2` — safety-first-was-the-right-call-metaprogramming-will-follow
    - **llogiq (Rust clippy maintainer)** · Source `f012469` · date 2015-09-01 · locator same post as above, llogiq's own reply — reframes Alexandrescu's critique as high praise — solving the hard part (memory management without GC) first is the right foundation, expects metaprogramming/expressiveness to mature later Quote: "I for one think of this as high praise for Rust – it's a young language, and having solved the hard part makes for a great foundation. I trust the other missing 'muscle' (mostly easier/more powerful metaprogramming) will come in time." [`a-sa28-f012469-c6`, team a]
- Positions seen by the extractor (`a-sa28-f012469-q3`): "Rust over-invested in one problem, becoming 'a disharmonic creature with one bulging muscle and little of anything else'" (Andrei Alexandrescu, D's creator — see Voice-eligibility caveat below) vs. "that's high praise; the missing muscle (metaprogramming) will come in time" (llogiq, Rust clippy maintainer)

### `memory-safety-vs-correctness-frame`

**Question.** Is "memory safety" the right frame for language-correctness discourse, or is "correctness" (of which memory safety is one part) the property that actually matters?

- Teams: b · members (context): `b-sb19-f005743-q3` (f005743, core)
- Domains: core
- Concepts: memory safety vs correctness
- Positions:
  - `memory-safety-vs-correctness-frame--p1` — correctness-is-the-real-target
    - **kristoff** · Source `f005743` · date 2026-06-02 · locator comment at 2026-06-02T13:32:19-05:00 — memory-safety-centric arguments miss that correctness is the broader property that matters Quote: "Every time a blog post over-fits on memory safety, it's a missed opportunity to talk about correctness, which is a strict superset and what actually matters." [`b-sb19-f005743-c7`, team b]
- Positions seen by the extractor (`b-sb19-f005743-q3`): correctness-is-the-real-target (kristoff)

### `merge-expensive-feature-with-limits`

**Question.** When a feature is useful but the only available implementation is algorithmically expensive (here, exponential batch count with glyph/outline count), should a game engine merge it now with documented limits, or hold it out of core until an efficient approach exists?

- Teams: a · members (context): `a-sa05-f003126-q1` (f003126, desktop-cli-ui, other)
- Domains: desktop-cli-ui, other
- Concepts: performance; API-surface; feature-gating
- Positions:
  - `merge-expensive-feature-with-limits--p1` — ship-with-documented-limits
    - **TotalKrill** · Source `f003126` · date 2025-06-16 · locator comment @TotalKrill 2025-06-16T16:10:03Z — an enum of fixed, small widths (Px1/Px2/Px3) makes the performance ceiling explicit to users while still shipping the feature for the common case Quote: "I would argue that we could go with a clearer enum of Px1, Px2, Px3... It would also quite clearly communicate the limitations of this implementation, while still allowing us to have it." [`a-sa05-f003126-c1`, team a]
    - **UkoeHB** · Source `f003126` · date 2025-06-16 · locator comment @UkoeHB 2025-06-16T20:45:49Z — documents the cost in the public API doc comment (exponential growth with width) rather than blocking the feature Quote: "The computation cost of the outline increases exponentially with width in the current implementation, so it is not recommended to use a width greater than 3." [`a-sa05-f003126-c2`, team a]
  - `merge-expensive-feature-with-limits--p2` — hold-for-proper-solution
    - **ickshonpe** · Source `f003126` · date 2025-06-19 · locator comment @ickshonpe 2025-06-19T09:25:27Z — even with the batching fixes, most users will not read the docs closely enough to avoid the performance cliff, and the implementation still has visible artifact bugs under transform/rotation Quote: "I'm feeling very negative about it now, even with all the improvements that have been made... most users aren't going to carefully read the docs for text outlines." [`a-sa05-f003126-c3`, team a]
    - **alice-i-cecile** · Source `f003126` · date 2025-06-19 · locator comment @alice-i-cecile 2025-06-19T00:58:08Z — reluctant to merge something this inefficient and rough; asks whether an offline font-preprocessing/baking approach could substitute, and ultimately wants a proper SDF-based text rendering solution instead Quote: "I'm really reluctant to merge something this slow and jank, even though I appreciate that it's better than it could have been." [`a-sa05-f003126-c4`, team a]
- Positions seen by the extractor (`a-sa05-f003126-q1`): ship-with-documented-limits, hold-for-proper-solution

### `metal-vs-cpu-priority-candle`

**Question.** Should GPU (Metal) backend work be prioritized ahead of further CPU/quantization optimization in candle?

- Teams: b · members (context): `b-sR01-f000464-q2` (f000464, ml)
- Domains: ml
- Concepts: GPU backends; roadmap prioritization
- Positions:
  - `metal-vs-cpu-priority-candle--p1` — prioritize-metal-next
    - **LaurentMazare** · Source `f000464` · date 2023-10-06 · locator issue comment, 2023-10-06T09:20:02Z — Metal/GPU support is the top engineering priority for candle's next major push, ahead of further quantized-CPU work. Quote: "Metal support is at the top of the priority list for the next large thing" [`b-sR01-f000464-c2`, team b]
- Positions seen by the extractor (`b-sR01-f000464-q2`): prioritize-metal-next

### `middleware-hook-vs-typestate`

**Question.** Should a web framework provide a generic "runs on every request" middleware hook, or is it better to omit global middleware in favor of an explicit typestate pattern that forces handlers to obtain capabilities (like authorization) only by calling through the relevant subsystem?

- Teams: a · members (context): `a-saL1-f005454-q2` (f005454, web, core)
- Domains: core, web
- Concepts: middleware/request hooks; typestate pattern; request handler design; authorization
- Positions:
  - `middleware-hook-vs-typestate--p1` — typestate-explicit-preferred-over-middleware
    - **steveklabnik** · Source `f005454` · date 2025-02-25 · locator reply, 2025-02-25T07:13:08-06:00, elaborated 2025-02-25T09:05:55-06:00 — Endorses Dropshot's deliberate omission of a generic per-request middleware hook in favor of the typestate pattern: a handler can only obtain an `Authorization` value by calling through the authorization subsystem (itself requiring a `User` obtained only via authentication), eliminating the subtle ordering/dependency bugs he associates with Rails-style before/after/around middleware. Quote: "I'm into it. I'm a big fan of the typestate pattern... I like that it's so straightforward. No more worrying about the order various handlers run…" [`a-saL1-f005454-c4`, team a]
  - `middleware-hook-vs-typestate--p2` — global-per-request-middleware-hook-expected
    - **insanitybit** · Source `f005454` · date 2025-02-25 · locator reply, 2025-02-25T01:56:21-06:00, quoting the Dropshot README's own FAQ — Flags that Dropshot's own documentation anticipates this as a natural question — i.e. that a global per-request middleware hook is the design most users expect from a web framework — and asks how omitting it has played out in practice. Quote: "Why is there no way to add an API handler function that runs on every request? How has this design choice played out? It's been a few years, I'm curious to hear lessons learned." [`a-saL1-f005454-c5`, team a]
- Positions seen by the extractor (`a-saL1-f005454-q2`): typestate-explicit-preferred-over-middleware; global-per-request-middleware-hook-expected

### `minimal-vs-batteries-std`

**Question.** Should Rust (as language and standard library) aim for minimalism — a small core deferring functionality to crates.io — or be a fuller, "medium-sized"/batteries-included system?

- Teams: a · members (context): `a-sa28-f012469-q2` (f012469, core)
- Domains: core
- Concepts: standard library scope; language surface area; crates.io ecosystem
- Positions:
  - `minimal-vs-batteries-std--p1` — rust-targets-medium-not-minimal
    - **graydon2 (Graydon Hoare, Rust's original language designer)** · Source `f012469` · date 2015-06-29 · locator post by @johansigfrids dated 2015-06-29T17:33:32Z, sourced "graydon2 on reddit" (no direct reddit permalink given) — states Rust never aimed to be minimal, targeted "medium sized" instead Quote: "Rust has never aimed to be a 'minimal' language, but a 'medium sized' one." [`a-sa28-f012469-c3`, team a]
  - `minimal-vs-batteries-std--p2` — stdlib-is-not-batteries-included
    - **DanielKeep (author of "The Little Book of Rust Macros," cited independently elsewhere in this same thread)** · Source `f012469` · date 2015-06-12 · locator post by @DanielKeep dated 2015-06-12T13:06:31Z — frames Rust's stdlib philosophy as the opposite of Python's "batteries included" Quote: "Buy Your Own Damn Batteries. cf. 'Python: Batteries Included'." [`a-sa28-f012469-c4`, team a]
- Positions seen by the extractor (`a-sa28-f012469-q2`): "Rust deliberately targeted 'medium-sized', not minimal" (graydon2, Rust's original language designer) vs. the community's own recurring "buy your own damn batteries" framing of stdlib as intentionally NOT batteries-included

### `missing-asset-build-fail-vs-runtime-degrade`

**Question.** When an expected embedded resource (e.g. a static asset) is missing, should the framework fail the build, or degrade silently at runtime (e.g. serve a 404)?

- Teams: b · members (context): `b-sR10-f004706-q1` (f004706, web, frontend, core)
- Domains: core, frontend, web
- Concepts: build-time vs runtime failure; error handling
- Positions:
  - `missing-asset-build-fail-vs-runtime-degrade--p1` — fail-the-build
    - **gbj (Greg Johnston, Leptos creator)** · Source `f004706` · date 2026-09-18 · locator PR review comment, 2026-09-18T18:13:56Z — an `allow_missing = true` option that lets the build succeed and then 404 at request time is a bad default, because it converts a build-time problem into a silent runtime one Quote: "`allow_missing = true` seems bad because it allows for a successful build → 404 rather than a build failure." [`b-sR10-f004706-c1`, team b]
- Positions seen by the extractor (`b-sR10-f004706-q1`): fail-the-build

### `missing-context-default-vs-surface`

**Question.** When a context a handler expects (e.g. `ResponseOptions`) is legitimately missing under load, should the code fall back to a silent safe default, or should the panic/error surface so the root cause gets found and fixed?

- Teams: b · members (context): `b-sb03-f000669-q1` (f000669, web)
- Domains: web
- Concepts: panics; Option/unwrap; error handling; context/dependency injection; defaults
- Positions:
  - `missing-context-default-vs-surface--p1` — silent-default-workaround
    - **glademiller** · Source `f000669` · date 2024-03-06 · locator issue #2112, comment 2024-03-06T15:53:46Z — proposes patching leptos-axum so the missing-context `.unwrap()` becomes `use_context::<ResponseOptions>().unwrap_or_default().0`, as a workaround for the panic, for callers not using `ResponseOptions` to modify the response Quote: "the workaround I am using at the moment is to patch leptos-axum by changing this line ... to let res_options = use_context::<ResponseOptions>().unwrap_or_default().0;" [`b-sb03-f000669-c1`, team b]
  - `missing-context-default-vs-surface--p2` — surface-and-fix-root-cause
    - **gbj** · Source `f000669` · date 2024-03-29 · locator issue #2112, comment 2024-03-29T14:49:12Z — worried the `unwrap_or_default()` fix "mostly *hides* the problem rather than fixing it," since a server function that actually sets `ResponseOptions` would silently fail to have its header/status applied; prefers finding and fixing the real cause (a disposed Runtime), to be revisited in 0.7 Quote: "I'm concerned that the solution ... mostly *hides* the problem rather than fixing it" [`b-sb03-f000669-c2`, team b]
- Positions seen by the extractor (`b-sb03-f000669-q1`): silent-default-workaround, surface-and-fix-root-cause

### `ml-dataset-eager-vs-lazy`

**Question.** Should a machine-learning dataset abstraction that loads segmentation masks/images eagerly materialize every item into memory (e.g. building an `InMemoryDataset`), or support lazy/streaming access, given that images or datasets can be large?

- Teams: a · members (context): `a-sa03-f002243-q1` (f002243, ml)
- Domains: ml
- Concepts: dataset/iterator abstractions; eager vs. lazy materialization; memory footprint
- Positions:
  - `ml-dataset-eager-vs-lazy--p1` — current eager in-memory materialization is inadequate for large datasets, unresolved
    - **anthonytorlucci** · Source `f002243` · date 2024-10-26 · locator PR review comment — Notes that `new_segmentation_with_items` ultimately calls `with_items`, which builds an `InMemoryDataset`, and that maintainer laggui had already flagged this as potentially problematic for large images or large datasets, without yet knowing the fix. Quote: "As @laggui pointed out, this could be problematic for large images or large datasets. I'm not sure what the solution is here." [`a-sa03-f002243-c1`, team a]
- Positions seen by the extractor (`a-sa03-f002243-q1`): anthonytorlucci (PR author) and laggui (maintainer, referenced) — jointly flag the current eager `InMemoryDataset` materialization as a likely problem for large images/datasets, with no resolution yet proposed in this source

### `modulo-vs-branch-wraparound`

**Question.** In hot loops needing wraparound indexing, use modulo arithmetic or branch on edge cases with a manually unrolled loop?

- Teams: a · members (context): `a-sB02-f000256-q5` (f000256, core, wasm)
- Domains: core, wasm
- Concepts: loop optimization; branch prediction
- Positions:
  - `modulo-vs-branch-wraparound--p1` — branch-unrolled(chosen)
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Time Profiling" — "Making Time Run Faster" — modulo-based edge wraparound in live_neighbor_count costs a div instruction on the common non-edge case; replacing it with if-branches and a manually unrolled neighbor loop lets the branch predictor do the work instead, measured at a 7.61x speedup. Quote: "if we use ifs for the edge cases and unroll this loop, the branches should be very well-predicted by the CPU's branch predictor." [`a-sB02-f000256-c5`, team a]
- Positions seen by the extractor (`a-sB02-f000256-q5`): modulo(original), branch-unrolled(chosen, 7.61x speedup measured)

### `multiple-algorithms-autotune`

**Question.** should a numerics/kernel library ship one fixed algorithm per operation, or ship several algorithm implementations and autotune between them at runtime?

- Teams: b · members (context): `b-sR05-f002048-q1` (f002048, ml)
- Domains: ml
- Concepts: none given
- Positions:
  - `multiple-algorithms-autotune--p1` — ship multiple algorithms (existing "direct" plus a new `im2col`/GEMM path) and autotune, even though the new path trades memory for speed.
    - **wingertge (PR author, tracel-ai/burn contributor)** · Source `f002048` · date 2024-09-17 · locator tracel-ai/burn#2287, PR description, 2024-09-17T15:20:57Z. · L853-L865. — ship multiple algorithms (existing "direct" plus a new `im2col`/GEMM path) and autotune, even though the new path trades memory for speed. Quote: "Adds the required infrastructure to autotune `conv2d` and `conv_transpose2d`, as well as adding a second algorithm based on `im2col` which provides significant speedups at the cost of memory usage." [`b-sR05-f002048-c1`, team b]
- Positions seen by the extractor (`b-sR05-f002048-q1`): ship multiple algorithms (existing "direct" plus a new `im2col`/GEMM path) and a (wingertge (PR author, tracel-ai/burn contributor))

### `multitenant-resource-allocation`

**Question.** should a multi-tenant compute platform allocate resources via static per-request/per-tenant reservation (Kubernetes-style CPU requests/limits), or via dynamic, system-wide throttling of individual noisy tenants?

- Teams: a · members (context): `a-saL2-f011092-q4` (f011092, cloud-workers, distributed)
- Domains: cloud-workers, distributed
- Concepts: resource scheduling; multi-tenancy; cloud infrastructure
- Positions:
  - `multitenant-resource-allocation--p1` — dynamic system-wide throttling over static per-tenant resource reservation
    - **Luca Casonato** · Source `f011092` · date 2024-02-13 · locator ~00:37:27-00:39:29 (Q&A, directly answering a comparison to Kubernetes-style CPU requests) — rather than measuring and reserving resources per tenant the way Kubernetes CPU requests/limits do, the platform measures utilization across the entire system and throttles an individual heavy tenant before throttling everyone else, accepting that a compute-intensive tenant may sometimes get lower throughput than dedicated hardware would give it Quote: "we have the ability... to isolate tenants in such a way that if there's a single tenant that comes and wants to use a bunch of resources we're going to throttle that single tenant before we throttle everyone else on the platform... we measure... the entire system" [`a-saL2-f011092-c4`, team a]
- Positions seen by the extractor (`a-saL2-f011092-q4`): dynamic-system-wide-throttling-over-static-per-tenant-reservation (Luca Casonato, contrasted directly against an audience member's Kubernetes-style approach)

### `multitenant-shared-readonly-pages`

**Question.** in a multi-tenant sandboxed runtime, should tenants share read-only memory pages (e.g. a JS engine's read-only heap) for efficiency, or should each tenant get fully isolated memory, given the side-channel risk (ASLR, Spectre-style timing attacks) shared pages introduce?

- Teams: a · members (context): `a-saL2-f011092-q2` (f011092, cloud-workers, distributed, core)
- Domains: cloud-workers, core, distributed
- Concepts: multi-tenant isolation; memory sharing; side-channel attacks; sandboxing
- Positions:
  - `multitenant-shared-readonly-pages--p1` — share read-only memory pages across tenants, mitigate side-channels via defense-in-depth
    - **Luca Casonato** · Source `f011092` · date 2024-02-13 · locator ~00:40:37-00:42:43 — the runtime shares memory pages across tenants only when they are entirely read-only and unmodifiable (e.g. V8's read-only heap of intrinsic JS strings); acknowledges this raises ASLR-adjacent concerns, and states they don't rely on a single security layer — they specifically avoid exposing high-resolution timers to block timing/Spectre-style side-channel attacks, on top of other sandbox layers Quote: "the things that we share are code pages that are entirely read only that can never be modified... V8 has a read-only heap" / "we don't rely on a single layer of security for any of our security measures... we take very specific care to avoid timing side channel attacks by not exposing any high resolution timers" [`a-saL2-f011092-c2`, team a]
- Positions seen by the extractor (`a-saL2-f011092-q2`): share-read-only-pages-plus-defense-in-depth-mitigations (Luca Casonato)

### `nalgebra-typed-api-vs-glm`

**Question.** For linear algebra/transforms in Rust, should you prefer nalgebra's strongly-typed API (compile-time dimension/invariant checks) or the simpler, GLM-style nalgebra-glm API?

- Teams: a · members (context): `a-sB01-f000217-q1` (f000217, ml, core)
- Domains: core, ml
- Concepts: type-level-dimension-checking; ergonomics-vs-rigor; homogeneous-coordinates
- Positions:
  - `nalgebra-typed-api-vs-glm--p1` — nalgebra for rigor and dynamically-sized cases; nalgebra-glm for simplicity
    - **Dimforge (nalgebra maintainers)** · Source `f000217` · date capture 2025-02-16 (Wayback; underlying doc undated, "living document") · locator "The nalgebra-glm crate" chapter, "Should I use nalgebra or nalgebra-glm?" — States the choice depends on taste/background — nalgebra for stronger typing and dynamically-sized matrices, nalgebra-glm for those used to C++ GLM or wanting more straightforward functions Quote: "If you prefer more rigorous treatments of transformations, with type-level restrictions, then go for nalgebra." [`a-sB01-f000217-c1`, team a]
- Positions seen by the extractor (`a-sB01-f000217-q1`): nalgebra for rigor and dynamically-sized cases; nalgebra-glm for simplicity and GLM-familiarity

### `narrating-comments`

**Question.** Should code carry comments that narrate what a simple, self-evident line or private helper does, or should comments be reserved for non-obvious rationale, with narrating comments treated as noise to remove?

- Teams: a · members (context): `a-sa13-f004772-q3` (f004772, core, desktop-cli-ui)
- Domains: core, desktop-cli-ui
- Concepts: code-comments; documentation; readability
- Positions:
  - `narrating-comments--p1` — no-narrating-comments
    - **SomeoneToIgnore** · Source `f004772` · date 2026-08-07 · locator comment @SomeoneToIgnore 2026-08-07T19:29:54Z — flags doc comments that narrate one-line private helpers and per-field docs as a repeating pattern across the file, arguing they should simply be deleted rather than kept or improved Quote: "doc comments narrating one-line private helpers... Same pattern all over the file... removing it all is way better than having them." [`a-sa13-f004772-c5`, team a]
    - **ysalitrynskyi** · Source `f004772` · date 2026-08-18 · locator comment @ysalitrynskyi 2026-08-18T21:51:50Z — complies by deleting the narrating comments across the touched files Quote: "Removed the duplicate and stripped the narrating comments across the files these changes touch." [`a-sa13-f004772-c6`, team a]
- Positions seen by the extractor (`a-sa13-f004772-q3`): no-narrating-comments, comments-explain-behavior

### `new-features-on-old-editions`

**Question.** When a new language capability doesn't interact with a prior edition's changed semantics, should it be made available on older Rust editions too, or should the edition boundary gate all new capabilities regardless of whether they actually interact with anything that changed?

- Teams: a · members (context): `a-sa20-f009698-q1` (f009698, core)
- Domains: core
- Concepts: editions; backward-compatibility; closures; capture-rules; combinatoric-explosion
- Positions:
  - `new-features-on-old-editions--p1` — extend-back-until-first-interaction
    - **@nikomatsakis** · Source `f009698` · date 2025-04-08 · locator "Experiment with ergonomic ref-counting" section, comment posted 2025-04-08 — reviewing a PR that limited a new `use` keyword/closures to Rust 2021+, argues the reason is not "features are edition-gated by default" but a missing tenet: editions exist to avoid combinatoric-explosion of untested feature/rule interactions, so a feature should be made available on older editions up until the point it interacts with something that changed in a later edition (here, `use` closures interact with the 2021 closure-capture-rule change) — and that you should never have to go back and modify an edition migration to work differently, which would signal the feature was pushed too far back Quote: "the reason we do editions and not fine-grained features is because we wish to avoid combianotoric explosion... you should never have to go back and modify an edition migration to work differently. That suggestions you are attempting to push the feature too far back." [`a-sa20-f009698-c1`, team a]
- Positions seen by the extractor (`a-sa20-f009698-q1`): extend-back-until-first-interaction, edition-boundary-gates-regardless

### `new-type-vs-option-for-variant`

**Question.** When a user requests a new capability variant of an existing type (e.g. a byte-based recorder alongside a file-based one), should the library add a new dedicated type or extend the existing type via a configuration option?

- Teams: b · members (context): `b-sb09-f002567-q2` (f002567, ml)
- Domains: ml
- Concepts: API surface growth; configuration options vs. new types
- Positions:
  - `new-type-vs-option-for-variant--p1` — extend-via-option
    - **antimora** · Source `f002567` · date 2025-03-13 · locator comment @antimora 2025-03-13T14:41:08Z, replying to @ivila's 2025-03-12T03:41:24Z request for a `SafeTensorBytesRecorder` — rejects adding a new recorder type for byte-based loading; proposes an argument/option on the existing recorder instead. Quote: "We don't need a new type. We can provide with an arg option." [`b-sb09-f002567-c6`, team b]
- Positions seen by the extractor (`b-sb09-f002567-q2`): extend-via-option (antimora), new-dedicated-type-requested (ivila)

### `nextest-vs-custom-runner`

**Question.** for scaling `cargo test` across a large multi-binary workspace, should a team adopt cargo-nextest, or build a custom test-runner wrapper when nextest's behavioral changes conflict with existing test assumptions?

- Teams: a · members (context): `a-saL2-f011092-q1` (f011092, core, cloud-workers)
- Domains: cloud-workers, core
- Concepts: testing tools; cargo test; cargo-nextest; CI infrastructure
- Positions:
  - `nextest-vs-custom-runner--p1` — custom test-runner wrapper over cargo-nextest
    - **Luca Casonato** · Source `f011092` · date 2024-02-13 · locator ~00:30:24-00:31:24 (wrapper description) and ~00:34:25-00:35:26 (Q&A on nextest) — built a custom wrapper around `cargo test` that builds test binaries on one machine, ships them to other machines as a zip, shards execution, and converts cargo's unstable JSON test output into JUnit XML; tried cargo-nextest first but rejected it because its different test-execution model (parallel processes) broke an assumption their own tests relied on — a global mutex used to hand out network ports one at a time — and fixing that would have taken more time than they had Quote: "we did actually try next test um but the problem with next test was that it changed too many other related things right like the way it runs its tests... that would cause our test [suite] to fail and we just didn't have the time" [`a-saL2-f011092-c1`, team a]
- Positions seen by the extractor (`a-saL2-f011092-q1`): custom-wrapper-over-nextest (Luca Casonato)

### `nightly-feature-autodetection`

**Question.** Should crates and their build scripts (build probes like autocfg) be free to auto-detect and use nightly-only compiler/library features by default, or must nightly-feature usage always require the final binary author's explicit opt-in?

- Teams: a · members (context): `a-sa19-f009343-q2` (f009343, core, desktop-cli-ui)
- Domains: core, desktop-cli-ui
- Concepts: nightly features; build scripts / build probes; cargo unstable flags (-Zallow-features); stability guarantees; autocfg
- Positions:
  - `nightly-feature-autodetection--p1` — nightly-features-must-be-explicit-opt-in
    - **RalfJung** · Source `f009343` · date 2026-06-30 · locator reply, 2026-06-30T12:20:20.661Z — Argues nearly all build probes are subtly broken because cargo doesn't give them enough information, and more fundamentally that nightly features should be opt-in, not opt-out; libraries auto-detecting and using them by default harms nightly users and compiler maintainers debugging regressions. Quote: "nightly features should be opt-in, not opt-out. That's how the entire Rust nightly feature system is designed." [`a-sa19-f009343-c3`, team a]
    - **epage** · Source `f009343` · date 2026-06-29 · locator reply, 2026-06-29T17:46:02.300Z — States the Rust Project's general principle that unstable features should only affect those who opted in, and that libraries auto-enabling nightly features runs counter to that principle. Quote: "there is a general principle within the Rust Project that unstable features only impact those who have opted in... Libraries auto-enabling features are running counter to that principle." [`a-sa19-f009343-c4`, team a]
    - **Nemo157** · Source `f009343` · date 2026-06-29 · locator reply, 2026-06-29T15:30:35.384Z — Wants to use nightly for unrelated ergonomic toolchain features while explicitly not consenting to dependencies silently using other unstable library or compiler features just because a nightly compiler was detected. Quote: "dependencies see that I am using a nightly compiler and attempt to use other unstable library or compiler features that I don't want them to." [`a-sa19-f009343-c5`, team a]
    - **kpreid** · Source `f009343` · date 2026-06-29 · locator reply, 2026-06-29T15:39:25.162Z — When switching to nightly for unrelated reasons (debug flags, a newer compiler), does not want dependencies to implicitly change behaviour by using unstable features; would want any such blanket opt-in to be a separate, explicit flag, never implied by nightly usage alone. Quote: "I don't want my project's dependencies to also implicitly change to making use of unstable features." [`a-sa19-f009343-c6`, team a]
  - `nightly-feature-autodetection--p2` — build-probes-should-default-to-detecting-and-using-nightly-features
    - **MusicalNinjaDad** · Source `f009343` · date 2026-06-29 · locator reply, 2026-06-29T15:04:10.084Z — As a "Group B" ergonomics-motivated developer, argues build probes defaulting to detect-and-use available nightly features is preferable to requiring manual opt-in flags, while acknowledging safety-critical ("Group A") users need a documented way to fully opt out. Quote: "Personally, I prefer a crate that documents clearly if they auto-detect & use nightly features to one that makes me go through that hassle, and choose accordingly." [`a-sa19-f009343-c7`, team a]
- Positions seen by the extractor (`a-sa19-f009343-q2`): nightly-features-must-be-explicit-opt-in; build-probes-should-default-to-detecting-and-using-nightly-features

### `nightly-gate-feature-vs-cfg`

**Question.** How should an unstable/nightly-only compiler feature be gated in library code — via a Cargo feature flag, or via a `--cfg` set through RUSTFLAGS?

- Teams: b · members (context): `b-sb06-f002033-q1` (f002033, core)
- Domains: core
- Concepts: cargo features; RUSTFLAGS; cfg; unstable/nightly features; CI
- Positions:
  - `nightly-gate-feature-vs-cfg--p1` — rustflags-cfg-gate
    - **alexcrichton** · Source `f002033` · date 2024-09-16 · locator PR #9251, comment 2024-09-16T15:40:18Z — recommends gating the tail-call code with `#[cfg(pulley_tail_call)]` set via `RUSTFLAGS`, rather than a Cargo feature, because a Cargo feature gets force-enabled by the "test with all features enabled" CI job even when the compiler in use is stable; this also lets the PR land, checked only by a dedicated nightly `cargo check` job, before upstream rustc codegen support for `become` exists Quote: "with a Cargo feature controlling this it unfortunately doesn't play well with our \"test with all features enabled\" in CI well because it enables the feature when a stable compiler is in use." [`b-sb06-f002033-c1`, team b]
- Positions seen by the extractor (`b-sb06-f002033-q1`): rustflags-cfg-gate

### `no-std-for-wasm`

**Question.** Does compiling to WebAssembly require disabling the standard library (no_std), the way embedded targets do?

- Teams: a · members (context): `a-sB01-f000217-q4` (f000217, wasm, embedded)
- Domains: embedded, wasm
- Concepts: no_std; wasm32-unknown-unknown; libstd
- Positions:
  - `no-std-for-wasm--p1` — no_std is embedded-only, not needed for wasm
    - **Dimforge (nalgebra maintainers)** · Source `f000217` · date capture 2025-03-22 (Wayback; underlying doc undated) · locator "WASM and embedded targets" chapter, "For embedded development" — Explicitly corrects the assumption that wasm compilation needs libstd disabled; that step is necessary only for embedded, not for browser/wasm targets Quote: "You do not need to disable libstd when compiling to wasm!" [`a-sB01-f000217-c4`, team a]
- Positions seen by the extractor (`a-sB01-f000217-q4`): no_std is embedded-only, not needed for wasm

### `nonnull-in-ffi-params`

**Question.** In FFI/wasm-bindgen-style APIs, should a safety-encoding wrapper type like `NonNull<T>` be accepted as a parameter even when it forces a runtime null check, or should the API stick to raw pointer types to avoid the check?

- Teams: a · members (context): `a-02-f000977-q1` (f000977, wasm)
- Domains: wasm
- Concepts: FFI; NonNull; runtime checks; API surface
- Positions:
  - `nonnull-in-ffi-params--p1` — avoid-runtime-null-check
    - **daxpedda** · Source `f000977` · date 2024-02-23 · locator PR body (top comment) — deliberately did not implement taking `NonNull<T>` as a parameter in the new atomic-pointer API, specifically to avoid adding a runtime check Quote: "I specifically didn't implement taking `NonNull<T>` as a parameter to avoid having to add a runtime check somewhere." [`a-02-f000977-c1`, team a]
- Positions seen by the extractor (`a-02-f000977-q1`): avoid-runtime-check (author), accept-runtime-check-for-safety (implicit alternative)

### `one-enum-vs-two-types`

**Question.** Should a value that can be one of two related-but-distinct kinds be modeled as one enum with variant matching, or split into two separate types?

- Teams: a · members (context): `a-sa07-f003716-q2` (f003716, core)
- Domains: core
- Concepts: enums; sum-types; api-ergonomics
- Positions:
  - `one-enum-vs-two-types--p1` — split-into-two-structs
    - **cBournhonesque** · Source `f003716` · date 2025-10-23 · locator PR #21601, comment 2025-10-23T14:14:41Z — found the enum-based accessor confusing when traversing relations dynamically and suggests splitting it into two separate structs plus friendlier wrapper methods Quote: "I think it might be better to split it into 2 separate structs?" [`a-sa07-f003716-c3`, team a]
- Positions seen by the extractor (`a-sa07-f003716-q2`): split-into-two-structs (cBournhonesque, proposed), single-enum (status quo)

### `oop-patterns-in-rust`

**Question.** Are classic OOP design patterns (e.g., Abstract Factory, as invoked via Clean/Hexagonal/Onion Architecture and DDD "ports and adapters") idiomatic to port into Rust, or does Rust favor different idioms (generics, enums) for the same structural goals?

- Teams: a · members (context): `a-sa30-f013276-q2` (f013276, core, web)
- Domains: core, web
- Concepts: design patterns; Abstract Factory; dependency injection; idiomatic Rust
- Positions:
  - `oop-patterns-in-rust--p1` — factories-are-rarely-idiomatic-in-rust
    - **jumpnbrownweasel — track record not established from this source** · Source `f013276` · date 2024-12-05 · locator post 2024-12-05T20:32:11.619Z — redirects the OP away from the Abstract Factory pattern toward generics, framing factories as a non-idiomatic import from other languages Quote: "I suggest trying to use generic types like Rc<E> above, if possible. Factories are rarely used in Rust." [`a-sa30-f013276-c6`, team a]
- Positions seen by the extractor (`a-sa30-f013276-q2`): "factories are rarely used in Rust; use generics instead" (jumpnbrownweasel) — single-sided in this source, though the OP's entire premise (porting Clean/Hexagonal Architecture's port-adapter pattern into Rust) implies the opposing practice exists in the wild, just not from a Voice this source can attribute

### `parser-combinator-vs-generator`

**Question.** Should Rust developers write parsers with a combinator library (nom) rather than a grammar-based generator (pest, lalrpop) or a hand-rolled recursive-descent parser?

- Teams: b · members (context): `b-sR13-f007973-q1` (f007973, core, desktop-cli-ui)
- Domains: core, desktop-cli-ui
- Concepts: parser combinators; zero-copy parsing; error reporting
- Positions:
  - `parser-combinator-vs-generator--p1` — nom-style parser combinators are the effective way to build parsers in Rust: small composable functions, no unnecessary allocation, and richer error reporting via VerboseError/context than a naive hand-rolled parser would give you
    - **Nazmul Idris (r3bl_tui maintainer)** · Source `f007973` · date 2023-02-20 · locator "Getting to know nom using lots of examples" section — "nom is very efficient and fast, it does not allocate memory when parsing if it doesn't have to, and it makes it very easy for you to do the same"; the article goes on to show context/convert_error as the way to get human-readable error messages out of a combinator chain Quote: "nom is very efficient and fast, it does not allocate memory when parsing if it doesn't have to" [`b-sR13-f007973-c1`, team b]
- Positions seen by the extractor (`b-sR13-f007973-q1`): combinators (nom) as the idiomatic, efficient choice

### `persistent-collections-cheap-clone`

**Question.** Should Rust's collections behave like true persistent (structural-sharing) values with cheap clone, rather than accepting the current model where clone is a full deep copy?

- Teams: b · members (context): `b-sR13-f008801-q1` (f008801, core)
- Domains: core
- Concepts: ownership; persistent data structures; RRB trees
- Positions:
  - `persistent-collections-cheap-clone--p1` — Rust would benefit from persistent, structural-sharing vector types (RRB trees) that make clone cheap (O(log n) path-copying) instead of the O(n) deep copy that ordinary owned collections force today
    - **Araz Abishov** · Source `f008801` · date 2026-02-12 · locator opening paragraphs, before "A quick intro to persistent vectors" — "Ownership means you must clone a vector if you want to keep using it after passing it somewhere else. As Niko Matsakis pointed out, Rust collections already behave like values; they just have an expensive clone. What if that clone could be nearly free?" — this framing motivates building pvec-rs Quote: "Rust collections already behave like values; they just have an expensive clone." [`b-sR13-f008801-c1`, team b]
- Positions seen by the extractor (`b-sR13-f008801-q1`): persistent/structural-sharing collections are worth building for Rust

### `pin-for-non-relocatable-cpp-types`

**Question.** For C++ types that cannot be relocated via a simple memcpy (self-referential types, e.g. small-string-optimized `std::string`), should Rust FFI bindings represent them using `Pin`, given Rust's general assumption that all types are memcpy-movable?

- Teams: b · members (context): `b-sb24-f011312-q5` (f011312, core)
- Domains: core
- Concepts: Pin; move constructors; self-referential types; memcpy-movability
- Positions:
  - `pin-for-non-relocatable-cpp-types--p1` — yes-pin-is-the-emerging-convention
    - **Taylor** · Source `f011312` · date 2025-10-03 · locator [25:34]-[27:36] — unsafe Rust code has long assumed all types can be relocated by bitwise memcopy, but most C++ types run a move constructor (e.g. small-string-optimized `std::string` stores a pointer into its own inline buffer); there's growing support for representing such non-memcopy-movable values with `Pin`, though the same aliasing/projection/auto-ref ergonomics gaps still apply to them Quote: "Thankfully, there's growing support for using Russ's pin type to represent values that can't be memcopy relocated." [`b-sb24-f011312-c5`, team b]
- Positions seen by the extractor (`b-sb24-f011312-q5`): yes-pin-is-the-emerging-convention (Taylor)

### `pin-project-vs-pin-project-lite`

**Question.** For pin projection, should a crate use the `pin-project` procedural-macro crate or the `pin-project-lite` declarative-macro crate?

- Teams: b · members (context): `b-bk01-f000233-q8` (f000233, core)
- Domains: core
- Concepts: Pin; pin projection; procedural macros
- Positions:
  - `pin-project-vs-pin-project-lite--p1` — pin-project-lite to avoid proc-macro deps, pin-project otherwise
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "Pinning" § Macros for pin projection — pin-project-lite is a declarative-macro alternative to the pin-project procedural macro, recommended when a project wants to avoid adding procedural-macro dependencies, at the cost of being less expressive and giving no custom error messages; pin-project is recommended otherwise. Quote: "Pin-project-lite is recommended if you want to avoid adding the procedural macro dependencies, and pin-project is recommended otherwise." [`b-bk01-f000233-c9`, team b]
- Positions seen by the extractor (`b-bk01-f000233-q8`): pin-project-lite to avoid proc-macro deps, pin-project otherwise for expressiveness/error messages

### `pin-vs-move-constructors`

**Question.** Should Rust have solved self-referential futures with a `Move` marker trait or C++-style move constructors instead of `Pin`?

- Teams: b · members (context): `b-bk01-f000233-q9` (f000233, core)
- Domains: core
- Concepts: Pin; Unpin; move semantics; self-referential types
- Positions:
  - `pin-vs-move-constructors--p1` — Pin's phased/place-based design over Move-trait or move-constructor alternatives
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "Pinning" § Alternatives and extensions — explains and defends why Rust did not solve self-referential futures with a `Move` marker trait (rejected: pinning is phased per-place while traits apply to a value's whole lifetime, and a Move trait would create widely "infectious" bounds plus backward-compatibility breakage) or C++-style move constructors (rejected: breaks Rust's invariant that objects can always be bitwise-moved, silently breaking unsafe code, and cannot fix up references held from outside the moved object). Quote: "The fundamental problem with this approach is that pinning today is a phased concept ... and types apply to the whole lifetime of values." [`b-bk01-f000233-c10`, team b]
- Positions seen by the extractor (`b-bk01-f000233-q9`): Pin's phased/place-based design over Move-trait or move-constructor alternatives

### `platform-gating-feature-vs-target-cfg`

**Question.** should platform-specific code be gated behind a Cargo feature flag, or behind a `#[cfg(target...)]`/target-triple check once the platform is a proper Rust target?

- Teams: b · members (context): `b-sR05-f002151-q2` (f002151, wasm)
- Domains: wasm
- Concepts: none given
- Positions:
  - `platform-gating-feature-vs-target-cfg--p1` — prefer target-based gating over feature flags once the target is stabilized.
    - **brooksmtownsend (wasmCloud engineer; contributor to mio/tokio-rs WASI socket support)** · Source `f002151` · date 2024-10-11 · locator leptos-rs/leptos#3063, comment 2024-10-11T13:37:26Z. · L1290-L1291. — prefer target-based gating over feature flags once the target is stabilized. Quote: "Once `wasm32-wasip2` is a stable target in Rust (coming in 1.82 afaik) the use of feature flags could be simplified, using the target directive instead." [`b-sR05-f002151-c2`, team b]
- Positions seen by the extractor (`b-sR05-f002151-q2`): prefer target-based gating over feature flags once the target is stabilized. (brooksmtownsend (wasmCloud engineer; contributor to mio/tokio-rs WASI socket support))

### `platform-logic-module-vs-inline`

**Question.** When adding a small piece of platform-specific logic used by only one call site, should it be factored into its own module/abstraction, or kept inline in the one file that uses it to minimize `#[cfg]` surface and review burden?

- Teams: a · members (context): `a-sa14-f005079-q4` (f005079, core)
- Domains: core
- Concepts: module boundaries; `#[cfg]` proliferation; unsafe API surface
- Positions:
  - `platform-logic-module-vs-inline--p1` — keep platform-specific logic inline rather than a separate abstraction
    - **alexcrichton** · Source `f005079` · date 2026-09-09 · locator comment 2026-09-09T04:31:28Z — prefers keeping all `serve.rs`-related code in `serve.rs`, marking the helper `unsafe` with a `// SAFETY` comment at the call site, over introducing a separate module with more `#[cfg]`s to validate Quote: "Personally I would prefer to keep all the `serve.rs`-related code in `serve.rs` and avoid extra abstractions here (which have more #[cfg] which is more to validate, etc)." [`a-sa14-f005079-c5`, team a]
- Positions seen by the extractor (`a-sa14-f005079-q4`): keep it inline in the using file, mark the helper function `unsafe`, and place a clear `// SAFETY` comment at the call site, rather than introducing a separate module with more `#[cfg]`s to validate

### `plugin-system-mechanism`

**Question.** How should a Rust application implement a plugin system: native dynamic libraries, an embedded scripting language, WebAssembly, or an expression/rules engine?

- Teams: a · members (context): `a-sa16-f007483-q1` (f007483, desktop-cli-ui, embedded, wasm, core)
- Domains: core, desktop-cli-ui, embedded, wasm
- Concepts: FFI; unsafe; ABI stability; WASM; sandboxing
- Positions:
  - `plugin-system-mechanism--p1` — native-dylib-rejected
    - **Sylvain Kerkour** · Source `f007483` · date 2026-08-18 · locator § Native Libraries — Rejects native dynamic libraries as a Rust plugin mechanism: no stable ABI, no sandboxing (a buggy or malicious plugin can crash or compromise the host), and compiled-code distribution hides backdoors and is harder for users to share/audit than scripts. Quote: "For all these reasons I don't recommend using dynamic libraries as plugins." [`a-sa16-f007483-c1`, team a]
  - `plugin-system-mechanism--p2` — scripting-language-preferred
    - **Sylvain Kerkour** · Source `f007483` · date 2026-08-18 · locator § Scripting language, closing paragraph — Recommends embedding QuickJS (over V8/deno_core and over Lua) as the default plugin approach: small binary size, no JIT, faster cold starts, easier integration. Quote: "For all these reasons I recommend embedding QuickJS to build a plugin system as the default approach, and to evaluate the other methods only if there are too many drawbacks for your specific use case." [`a-sa16-f007483-c2`, team a]
  - `plugin-system-mechanism--p3` — wasm-too-immature
    - **Sylvain Kerkour** · Source `f007483` · date 2026-08-18 · locator § WASM, closing paragraph — Judges WebAssembly currently too immature for a Rust plugin system despite its sandboxing strength, citing uneven cross-language WASM support and churning toolchains/targets (WASI p1, p2). Quote: "I think that WebAssembly is currently too immature to be used for a plugin system and will make the life of developers wanting to create plugins hard." [`a-sa16-f007483-c3`, team a]
  - `plugin-system-mechanism--p4` — expression-engine-for-bounded-untrusted-eval
    - **Sylvain Kerkour** · Source `f007483` · date 2026-08-18 · locator § Expression engine, closing paragraph — For his own project he forked CEL to a boolean-only subset because non-Turing expression languages give bounded, predictable-runtime evaluation of untrusted user input; recommends QuickJS instead for most other projects. Quote: "expressions evaluating to a bool is the easiest and safest way to achieve that, but for most projects I would recommend integrating QuickJS." [`a-sa16-f007483-c4`, team a]
- Positions seen by the extractor (`a-sa16-f007483-q1`): native-dylib (rejected), scripting-language (preferred default), wasm (too immature), expression-engine (safe but limited)

### `pointer-addr-vs-as-usize`

**Question.** When converting a raw pointer to an integer for a low-level hook/tracking API, should you cast with `as usize` or use the provenance-preserving `.addr()`?

- Teams: a · members (context): `a-sa11-f004512-q1` (f004512, embedded)
- Domains: embedded
- Concepts: pointer provenance; strict provenance API; unsafe FFI-adjacent code
- Positions:
  - `pointer-addr-vs-as-usize--p1` — prefer `.addr()` over `as usize` for pointer-to-integer conversion
    - **renkenono** · Source `f004512` · date 2026-04-01 · locator comment 2026-04-01T19:13:38Z; 2026-04-01T21:50:33Z — flags that casting a pointer to `usize` has implicit behavior around provenance, recommends `.addr()` since provenance isn't needed here and it "has a more explicitly defined behavior" Quote: "Casting the pointer to `usize` has implicit behavior e.g., in relation to provenance... I'd recommend using `addr()` instead" [`a-sa11-f004512-c1`, team a]
- Positions seen by the extractor (`a-sa11-f004512-q1`): use `.addr()` because it has more explicitly defined behavior with respect to provenance, over a plain `as usize` cast

### `polonius-scope-cut`

**Question.** When a new borrow-checker algorithm (Polonius) trades full expressiveness parity with the old implementation for an easier path to production-readiness, should the project accept the narrower formulation (and its known false positive on one loop/region case) to ship sooner, or hold out for full expressiveness?

- Teams: a · members (context): `a-sa20-f009698-q3` (f009698, core)
- Domains: core
- Concepts: polonius; borrow-checker; NLL; datalog; expressiveness-vs-shippability
- Positions:
  - `polonius-scope-cut--p1` — cut-scope-for-shippability
    - **@lqd** · Source `f009698` · date 2025-05-05 · locator "Scalable Polonius support on nightly" section, comment posted 2025-05-05 — reports the current datalog-based approximation of Polonius handles all UI tests except a case where loop control flow connects regions live before/after the loop, producing a false positive their older, slower, more comprehensive approach used to accept correctly; the team is actively discussing whether to cut scope and accept this formulation (which accepts "NLL problem case 3") in exchange for an easier path to production, while still evaluating what expressiveness limits it would impose outside that case Quote: "we're currently discussing whether we can cut scope here, as this formulation accepts NLL problem case 3. We'll need to evaluate what limits this formulation imposes on expressiveness... and whether it indeed has an easier path to becoming production ready." [`a-sa20-f009698-c3`, team a]
- Positions seen by the extractor (`a-sa20-f009698-q3`): cut-scope-for-shippability

### `portable-async-vs-sync-io`

**Question.** Should a portable crate needing I/O expose synchronous or async I/O, and how should it abstract wasm vs native?

- Teams: b · members (context): `b-bk02-f000256-q5` (f000256, wasm, core)
- Domains: core, wasm
- Concepts: async I/O; cross-target abstraction
- Positions:
  - `portable-async-vs-sync-io--p1` — for I/O that a portable library must perform itself, go async (generic over a Future type), or split by target with a trait plus #[cfg]-gated impls — never synchronous
    - **rustwasm working group (Rust and WebAssembly book) [voice-unverified]** · Source `f000256` · date unknown (living doc) · locator § "How to Add WebAssembly Support to a General-Purpose Crate" → Avoid Synchronous I/O — states synchronous I/O is a non-option on the Web, then names two concrete alternative architectures — a function generic over `F: Future`, or a trait implemented once per target behind `#[cfg(target_arch = "wasm32")]` — without picking one as universally superior. Quote: "If you must perform I/O in your library, then it cannot be synchronous. There is only asynchronous I/O on the Web." [`b-bk02-f000256-c6`, team b]
- Positions seen by the extractor (`b-bk02-f000256-q5`): generic-over-Future async API (one named option); trait + per-target #[cfg] implementations (second named option); synchronous I/O (rejected — impossible on Web)

### `portable-kernels-performance-cost`

**Question.** Can one compute framework abstract kernel programming over both GPU and CPU without sacrificing performance, or does hardware-portable abstraction necessarily cost performance versus a hardware-specific implementation?

- Teams: a · members (context): `a-sa09-f004016-q2` (f004016, ml)
- Domains: ml
- Concepts: comptime-specialization; portability; performance
- Positions:
  - `portable-kernels-performance-cost--p1` — comptime-specialization-avoids-the-tradeoff
    - **nathanielsimard** · Source `f004016` · date 2025-12-19 · locator § "CubeCL Architecture" — claims CubeCL disproves the assumed GPU/CPU portability-performance tradeoff by using `comptime` to specialize kernels per plane size and line size, including setting plane size to 1 for the CPU runtime rather than simulating GPU execution Quote: "The common consensus in the industry is that it is impossible to abstract GPU and CPU programming without sacrificing performance. However, through intentional design, we have succeeded in proving otherwise." [`a-sa09-f004016-c2`, team a]
- Positions seen by the extractor (`a-sa09-f004016-q2`): comptime-specialization-avoids-the-tradeoff, portability-costs-performance

### `postfix-await`

**Question.** Should `.await` be a postfix operator (`fut.await`) or a prefix operator, as in Python/JavaScript (`await fut`)?

- Teams: b · members (context): `b-bk01-f000233-q1` (f000233, core)
- Domains: core
- Concepts: async/await syntax
- Positions:
  - `postfix-await--p1` — postfix `.await`
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "Async and Await" § await — postfix `.await` is more ergonomic than prefix await in chains of method calls and field accesses; contrasts `fetch().await?.status_code` against the prefix-syntax equivalent `(await fetch())?.status_code`, calling the postfix form more natural to read in longer chains. Quote: "This is in contrast to languages like Python or JavaScript, where await is a prefix operator" [`b-bk01-f000233-c1`, team b]
- Positions seen by the extractor (`b-bk01-f000233-q1`): postfix (Rust)

### `pre-1-0-api-default-stability`

**Question.** Before a crate's 1.0 release, should an unreviewed API surface (e.g. the interrupt API) default to stable unless a blocker is raised, or stay marked unstable until the team explicitly agrees it is ready?

- Teams: b · members (context): `b-sb08-f002517-q1` (f002517, embedded)
- Domains: embedded
- Concepts: API stability; semver; 1.0 release process; `#[unstable]` attribute
- Positions:
  - `pre-1-0-api-default-stability--p1` — stable-unless-flagged
    - **MabezDev** · Source `f002517` · date 2025-01-10 · locator comment 2025-01-10T12:44:33Z — without a known blocking issue, sees no problem exposing the interrupt API as stable for now, having assumed the team was already aligned Quote: "if there isn't anything else then I don't see any issue in exposing this as stable, at least for now." [`b-sb08-f002517-c1`, team b]
  - `pre-1-0-api-default-stability--p2` — unstable-until-agreed-ready
    - **Dominaezzz** · Source `f002517` · date 2025-01-10 · locator comment 2025-01-10T12:26:08Z — objects that interrupts are being stabilized, since prior PRs assumed they would stay unstable and some interrupt enum variants don't make sense for the CPU-driven driver Quote: "The PRs targeting interrupts so far have done so under the assumption that they won't be stabilized." [`b-sb08-f002517-c2`, team b]
    - **MabezDev** · Source `f002517` · date 2025-01-10 · locator comment 2025-01-10T13:08:42Z — after push back, reverses course and agrees the interrupt API isn't ready, marking it unstable for now Quote: "After some push back, I'm 180'ing. I agree with the general consensus that the interrupt API might not be ready." [`b-sb08-f002517-c3`, team b]
- Positions seen by the extractor (`b-sb08-f002517-q1`): stable-unless-flagged (MabezDev, initial), unstable-until-agreed-ready (Dominaezzz, bugadani, jessebraham; MabezDev after reversing)

### `pre-1-0-canary-releases`

**Question.** Before a crate's 1.0 release, should breaking changes ship frequently in a fast pre-release ("canary") channel to get user feedback quickly, or should a team hold changes until they are fully finished before cutting each release?

- Teams: b · members (context): `b-sb10-f003188-q1` (f003188, distributed, decentralized-iroh)
- Domains: decentralized-iroh, distributed
- Concepts: pre-1.0 semver policy; release cadence; breaking changes
- Positions:
  - `pre-1-0-canary-releases--p1` — frequent-canary-releases-for-fast-feedback
    - **ramfox** · Source `f003188` · date 2025-06-27 · locator blog body, paragraph beginning "Last time we published a release blog" — waiting until everything was fully finished before releasing was not the best way to get a stable release into users' hands; three-week cycles and fast canary releases before 1.0 get feedback quickly and let the team move with confidence Quote: "we realized that waiting until we had everything worked through and finished before releasing was not actually the best way for us to get a stable release into the hands of our users." [`b-sb10-f003188-c1`, team b]
- Positions seen by the extractor (`b-sb10-f003188-q1`): frequent-canary-releases-for-fast-feedback (ramfox)

### `predicate-rules-vs-first-match`

**Question.** Should conditional configuration logic be expressed as independent boolean-predicate rules whose interaction is implicit, or as an ordered list of rules where the first matching condition wins?

- Teams: b · members (context): `b-sb09-f003030-q2` (f003030, embedded)
- Domains: embedded
- Concepts: config DSL semantics; conditional evaluation; ordering
- Positions:
  - `predicate-rules-vs-first-match--p1` — ordered-first-match-wins
    - **bugadani** · Source `f003030` · date 2025-06-11 · locator comment @bugadani 2025-06-11T07:49:35Z — after bjoernQ's predicate-function design produced a real bug (two mutually exclusive conditions both false), proposes redesigning the conditional rules as an ordered list evaluated first-match-wins. Quote: "What if we turned this into a match-style \"first condition wins\" situation?" [`b-sb09-f003030-c8`, team b]
- Positions seen by the extractor (`b-sb09-f003030-q2`): independent-predicate-functions (bjoernQ, initial design, later found buggy), ordered-first-match-wins (bugadani)

### `proc-macro-emitted-paths-hidden-deps`

**Question.** When a proc-macro conditionally emits a call into a crate (here, `tracing::instrument`) behind a feature flag inherited transitively through another crate's feature, should the macro hardcode an unqualified path that silently requires every downstream crate to independently declare that dependency in its own Cargo.toml, or should it use a fully-qualified/re-exported path so the hidden transitive requirement never surfaces as a downstream compile error?

- Teams: a · members (context): `a-01-f000701-q1` (f000701, frontend)
- Domains: frontend
- Concepts: proc-macros; Cargo feature unification; hidden/transitive dependencies; macro hygiene
- Positions:
  - `proc-macro-emitted-paths-hidden-deps--p1` — fix via feature-gating, not via requiring every downstream crate to declare the dependency
    - **DanielJoyce** · Source `f000701` · date 2024-01-02 · locator issue comment, mid-thread — Traces the root cause to `leptos_macro`'s `view!` macro unconditionally emitting `tracing::instrument` under `debug_assertions`/`ssr`, and proposes fixing it by having the `ssr` feature also enable `tracing`, or by reworking the macro's `cfg_attr` gating, rather than requiring every downstream crate to add `tracing` itself. Quote: "Fix is to have ssr feature also turn on tracing, or rework the cfg_attribute. Have not tested. ymmv" [`a-01-f000701-c1`, team a]
- Positions seen by the extractor (`a-01-f000701-q1`): DanielJoyce — treat it as a bug to fix by feature-gating (have `ssr` also enable `tracing`, or rework the macro's `cfg_attr`); a later, unattributed commenter — fix by using a fully-qualified `::tracing` path so the macro never assumes the invoking crate declared the dependency itself

### `project-decision-speed-vs-inclusion`

**Question.** Should the Rust project prioritize speed of consensus / shipping over slower, more inclusive decision-making (e.g. long-nightly-gated APIs, stabilization pace)?

- Teams: b · members (context): `b-sb19-f005743-q5` (f005743, core)
- Domains: core
- Concepts: RFC process; nightly-only APIs; project governance; BDFL model
- Positions:
  - `project-decision-speed-vs-inclusion--p1` — process-speed-risks-exclusion
    - **lake** · Source `f005743` · date 2026-06-02 · locator comment at 2026-06-02T13:04:24-05:00 — reads the (quoted, unnamed) source article as calling the community to sideline collaborative/inclusive decision-making in favor of faster "progress"; contrasts with frustration over long-stalled nightly-only APIs and floats wanting a BDFL model Quote: "We must learn to recognize when having a consensus is more important than having the right consensus, and in these cases, to pick progress over stagnation." [`b-sb19-f005743-c9`, team b]
- Positions seen by the extractor (`b-sb19-f005743-q5`): process-speed-risks-exclusion (lake)

### `project-discussions-area`

**Question.** Should a Rust project keep a GitHub Discussions area for support and design talk, or remove it?

- Teams: b · members (context): `b-sT05-f002499-q5` (f002499, core)
- Domains: core
- Concepts: project community infrastructure; knowledge retention
- Positions:
  - `project-discussions-area--p1` — removing the discussion area lost knowledge
    - **Dominaezzz** · Source `f002499` · date 2026-01-29 · locator comment 2026-01-29T15:21:38Z; 2026-02-03T11:59:00Z — explanations (incl. one by "Igor" on bus arbitration) lived in a deleted discussion Quote: "a lot of what I'm explaining now used to exist in a discussion but it's all been deleted now" (flag: voice-unverified) [`b-sT05-f002499-c9`, team b]
    - **yanshay** · Source `f002499` · date 2026-02-03 · locator comment 2026-02-03T10:18:50Z (P.S.) — design talk is forced into an ill-fitting issue after the discussion area's removal Quote: "no alternative location for such discussion now with the removal of the discussion area" (flag: voice-unverified) [`b-sT05-f002499-c10`, team b]
- Positions seen by the extractor (`b-sT05-f002499-q5`): removal cost lost knowledge (dissent); project removed it (no Voice in source)

### `project-priorities-communication`

**Question.** How should an open-source Rust project's priorities be decided and communicated to its community?

- Teams: b · members (context): `b-sR11-f004993-q2` (f004993, core)
- Domains: core
- Concepts: governance; roadmaps
- Positions:
  - `project-priorities-communication--p1` — project direction should be communicated through a lightweight, non-authoritative "Goals" system (staffed/unstaffed as a focus signal) rather than a fixed roadmap or the prior ad hoc culture
    - **Carter Anderson (@cart, Bevy creator and Project Lead)** · Source `f004993` · date 2026-08-10 · locator "Bevy Project Goals #" section — the initial rollout felt "dictatorial" because staffed/unstaffed was framed as active/inactive; loosened so any approved Goal can get a Working Group even unstaffed, while staffing still signals leadership focus Quote: "This is notably not a 'roadmap' ... This is also not authoritative." [`b-sR11-f004993-c2`, team b]
- Positions seen by the extractor (`b-sR11-f004993-q2`): lightweight, non-authoritative "Goals" signal instead of a fixed roadmap or ad hoc "build first, yell for attention"

### `properties-syntax`

**Question.** Should Rust support "properties" (field-access syntax that silently compiles to a getter/setter method call, as in Python/C#/Swift)?

- Teams: b · members (context): `b-sb19-f007207-q2` (f007207, core)
- Domains: core
- Concepts: properties; Deref; implicit method calls; field access
- Positions:
  - `properties-syntax--p1` — reject-properties
    - **Jimmy Hartzell** · Source `f007207` · date 2025-07-21 · locator § "Limitations of the Proposal" — field access should stay visibly cheap and side-effect-free; hiding a method call behind `foo.x` syntax is undesirable, especially in a systems language Quote: "it should be clear that it's doing a field access (cheap and with few potential unseen consequences) rather than a method call (which could do anything including crash, or block your thread on a network request)." [`b-sb19-f007207-c2`, team b]
- Positions seen by the extractor (`b-sb19-f007207-q2`): reject-properties (Jimmy Hartzell)

### `ptx-build-host-vs-multi-arch`

**Question.** Should a GPU-targeting Rust crate's build script compile device code (PTX) only for the build host's own compute capability, or build/distribute for multiple architectures to stay portable across heterogeneous multi-GPU systems?

- Teams: b · members (context): `b-sb08-f002518-q1` (f002518, ml)
- Domains: ml
- Concepts: build.rs; native/device codegen; portability; GPU targeting
- Positions:
  - `ptx-build-host-vs-multi-arch--p1` — compile-for-build-host-only
    - **ivarflakstad** · Source `f002518` · date 2025-10-25 · locator comment 2025-10-25T10:12:19Z — PTX is compiled per-machine via build.rs at build time, not distributed as one binary to all users Quote: "The ptx is compiled for your machine via `build.rs` at compile time. It is not one binary distributed to everyone." [`b-sb08-f002518-c1`, team b]
  - `ptx-build-host-vs-multi-arch--p2` — needs-portable-multi-arch-support
    - **haricot** · Source `f002518` · date 2025-10-25 · locator comment 2025-10-25T10:29:20Z — compiling only for the build host's compute capability may break portability across systems with multiple different GPUs Quote: "the current build script only compiles for the compute capacity active on the build host, which may break portability across heterogeneous multi-GPU systems, it seems." [`b-sb08-f002518-c2`, team b]
- Positions seen by the extractor (`b-sb08-f002518-q1`): compile-for-build-host-only (ivarflakstad), needs-portable-multi-arch-support (haricot, raised as a concern)

### `pump-events-timeout-poll`

**Question.** When an external caller drives a Rust windowing event loop via `pump_events` with a timeout, should any non-negative `Some(duration)` timeout force `ControlFlow::Poll`, or only a zero-duration timeout?

- Teams: a · members (context): `a-sR08-f002685-q1` (f002685, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: event loop control flow; windowing; async/external-loop integration
- Positions:
  - `pump-events-timeout-poll--p1` — any `Some(duration)` timeout passed to `pump_events` should force `ControlFlow::Poll`
    - **sigmaSd** · Source `f002685` · date 2025-02-20 · locator GitHub issue comment, 2025-02-20T10:24 — proposed broadening the workaround so that every non-nil duration, not just zero, forces Poll Quote: "any duration as long that its Some, should make the controlflow Poll" [`a-sR08-f002685-c1`, team a]
  - `pump-events-timeout-poll--p2` — special-case only `Duration::ZERO` to force `ControlFlow::Poll`; leave other durations to winit's own handling
    - **tronical (Olivier Goffart, Slint co-founder/maintainer)** · Source `f002685` · date 2025-02-20 · locator GitHub issue comment, 2025-02-20T13:08 — reconsidered the broader fix and narrowed the workaround to only the zero-duration case, reasoning it doesn't make sense to return `Wait` when a nonzero duration like `Some(2s)` was explicitly requested — that should be winit's own responsibility to handle correctly Quote: "I'll do this workaround only for `Zero`... I'll leave it to the winit implementation to handle that correctly" [`a-sR08-f002685-c2`, team a]
- Positions seen by the extractor (`a-sR08-f002685-q1`): any-Some-duration forces Poll (sigmaSd); only-Zero forces Poll (tronical)

### `pure-rust-crypto-stopgap`

**Question.** When targeting an unusual/constrained platform where the standard C-backed crypto backend won't build, is it acceptable to reach for a pure-Rust crypto implementation as a stopgap, even knowing a hardware-accelerated backend would be the "right" choice for production?

- Teams: a · members (context): `a-sa11-f004471-q1` (f004471, embedded)
- Domains: embedded
- Concepts: crypto provider selection; embedded constraints; rustls pluggable providers
- Positions:
  - `pure-rust-crypto-stopgap--p1` — pure-Rust crypto backend as an acceptable stopgap, not the end state
    - **Rüdiger Klaehn** · Source `f004471` · date 2026-03-24 · locator § Crypto provider — explains that both `ring` and `aws-lc-rs` fail on Xtensa because they wrap C code with platform-specific assembly; since rustls providers are pluggable, forks a pure-Rust backend (`rustls-rustcrypto`) down to only the two primitives iroh needs (disabling RSA, disabling certificate verification for the relay connection) to fit the binary-size budget, while stating hardware-accelerated crypto "would be the right thing to do for a production system" Quote: "The latter would be the right thing to do for a production system, but for now we are going to just do a pure rust version." [`a-sa11-f004471-c1`, team a]
- Positions seen by the extractor (`a-sa11-f004471-q1`): ship a minimal pure-Rust crypto backend (fork of `rustls-rustcrypto`, algorithms feature-gated down to the bare minimum) now, while naming hardware-accelerated as the correct long-term answer

### `quantization-speedup-candle`

**Question.** Does quantization reliably speed up inference in candle, or only for some model architectures?

- Teams: b · members (context): `b-sR01-f000464-q1` (f000464, ml)
- Domains: ml
- Concepts: quantization; memory-bound vs compute-bound kernels; matmul backends; Apple Accelerate
- Positions:
  - `quantization-speedup-candle--p1` — quantization-helps-memory-bound-only
    - **LaurentMazare** · Source `f000464` · date 2023-10-08 · locator issue comment, 2023-10-08T11:39:13Z — T5's cross-attention involves much larger matmuls than llama/mistral, making it compute- rather than memory-bound on M1/M2; quantization's usual speedup comes from being memory-bound, so it's hard to beat Apple Accelerate (possibly Neural-Engine-backed) here even after tuning min/max-len parameters. Quote: "my guess would be that it's much less memory bound in this case and in this case it's pretty hard to outperform the work done by apple on accelerate" [`b-sR01-f000464-c1`, team b]
- Positions seen by the extractor (`b-sR01-f000464-q1`): quantization-helps-memory-bound-only

### `query-engine-batching-parallelism`

**Question.** Should a Rust vectorized query engine process rows fully sequentially in large batches (cache-friendly, low interpretation overhead), fully in parallel per-row, or partition data into parallel batched streams?

- Teams: a · members (context): `a-sR08-f003580-q1` (f003580, distributed, core)
- Domains: core, distributed
- Concepts: vectorized execution; query engine architecture; partitioning
- Positions:
  - `query-engine-batching-parallelism--p1` — partition-based batch execution (vectorized batches within a partition, parallelized across partitions) captures the benefits of both fully-sequential and fully-parallel row processing
    - **Yevgen Safronov, Nikita Lapkov, Jérôme Schneider (Cloudflare, R2 SQL)** · Source `f003580` · date 2025-09-25 · locator "Apache DataFusion" section — contrasted a fully-sequential "tight loop" (cache-friendly, low interpretation overhead) against fully-parallel per-row processing (better core utilization), and endorsed DataFusion's partition model as achieving both at once Quote: "DataFusion's architecture allows us to achieve a balance on this scale, reaping benefits from both ends." [`a-sR08-f003580-c1`, team a]
- Positions seen by the extractor (`a-sR08-f003580-q1`): hybrid partition-based batching (DataFusion's model, endorsed by Cloudflare's R2 SQL team)

### `quic-framing-one-stream-vs-per-message`

**Question.** On a QUIC stream, should a protocol send several length-prefixed messages over one stream, or one message per stream written with `write_all` and read to the end before closing?

- Teams: a · members (context): `a-sT08-f003375-q1` (f003375, decentralized-iroh, distributed)
- Domains: decentralized-iroh, distributed
- Concepts: QUIC streams; message framing; length prefix; varints; protocol design
- Positions:
  - `quic-framing-one-stream-vs-per-message--p1` — length-prefixed-framing-on-one-stream
    - **n0 (post by ramfox, matheus23, b5)** · Source `f003375` · date 2025-08-12 · locator § Intro and § Framed Messages, paragraphs on `write_all`/`read_all` — writing one chunk with `write_all`, reading it all, then closing the stream is fine while learning, but real protocols should send multiple logical messages per stream, each prefixed by its length, so the protocol is designed as messages rather than bytes and variable-length messages are handled Quote: "This is fine while you are getting familiar, but when you go to write your protocols you will want something more sophisticated." (flag: voice-unverified — Rust connection in the source: the authors write for n0 as iroh's makers ("how we at n0 like to serialize") and the tutorial is Rust with cargo, tokio, iroh. Left out: `anyhow` "allows us to do easy error handling" and the ALPN naming "conventions we recommend" are a dependency gloss and a recommendation without an alternative or reason on a contested choice (rule 8); `u8` vs larger or varint length prefixes is stated as a size trade-off instruction, not a Position.) [`a-sT08-f003375-c1`, team a]
- Positions seen by the extractor (`a-sT08-f003375-q1`): length-prefixed-framing-on-one-stream (against whole-stream-per-message)

### `rate-limiter-algorithm`

**Question.** for a rate limiter, should you use a fixed-window counter, a token bucket, or a sliding window?

- Teams: b · members (context): `b-sb22-f008906-q5` (f008906, distributed, cloud-workers)
- Domains: cloud-workers, distributed
- Concepts: rate limiting algorithms; DynamoDB atomic counters; window-boundary burst
- Positions:
  - `rate-limiter-algorithm--p1` — use a fixed-window counter for the rate limiter, accepting its known boundary-burst weakness, rather than a token bucket or sliding window
    - **Luciano Mammino** · Source `f008906` · date 2026-05-03 · locator section "Fixed window vs token bucket vs sliding window: what we are giving up" — a motivated client can double its effective rate by firing requests at the edges of two adjacent fixed windows; token bucket and sliding window both eliminate that edge but cost an extra DynamoDB round trip (read-modify-write, or two reads) versus one atomic `ADD`; the post sticks with the fixed window "mostly because it keeps the DynamoDB schema minimal and easy to follow," leaving the algorithm swap as a follow-up Quote: "This is sometimes called the window boundary burst, and it is the textbook reason people move on from fixed windows in production-grade rate limiters." [`b-sb22-f008906-c5`, team b]
- Positions seen by the extractor (`b-sb22-f008906-q5`): fixed window, chosen pragmatically for a minimal DynamoDB schema and to keep a tutorial focused on middleware mechanics, while explicitly naming its boundary-burst weakness and that token bucket or sliding window are the standard production fixes (Luciano Mammino)

### `reactive-keyed-child-notification`

**Question.** When a reactive container's parent field is written as a whole (replaced or patched), should the reactivity system notify all of its keyed-child subscriptions by default (accepting some unnecessary re-notifications), or should notification require writing through the specific keyed accessor (precise, but silently misses updates if the user writes the parent instead)?

- Teams: b · members (context): `b-sb13-f003963-q1` (f003963, frontend)
- Domains: frontend
- Concepts: fine-grained reactivity; signal/trigger graph; keyed derived signals; false positives vs false negatives in change notification
- Positions:
  - `reactive-keyed-child-notification--p1` — default-notify-all-children-favor-no-false-negatives
    - **gbj** · Source `f003963` · date 2026-02-06 · locator comment 2026-02-06T17:19:48Z — concludes that broken reactivity (false negatives) is worse than unnecessary notifications (false positives), so the library should track the parent path by default and notify all keyed children on a parent write Quote: "I think your intuition is correct that \"false negatives\" (broken reactivity) here are worse than \"false positives\" (notifications that are technically unnecessary). I think going ahead with my Option 1 ... is probably the way to go." [`b-sb13-f003963-c1`, team b]
    - **TiemenSch** · Source `f003963` · date 2026-02-04 · locator comment 2026-02-04T13:10:55Z — independently reasons that fully replacing a value should be allowed to trigger all children, leaving precise-but-manual updates as an opt-in path rather than the default Quote: "I would expect that fully setting a new value is allowed to trigger all children and it would be OK to have the user patch/update specific fields instead to avoid too many false positives." [`b-sb13-f003963-c2`, team b]
- Positions seen by the extractor (`b-sb13-f003963-q1`): default-notify-all-children-favor-no-false-negatives (gbj, TiemenSch)

### `readability-vs-manual-optimization`

**Question.** When a compiler backend (LLVM/Cranelift) could optimize an eager computation away, should code still be written in the more efficient/lazy form?

- Teams: b · members (context): `b-sb05-f001582-q2` (f001582, core)
- Domains: core
- Concepts: compiler-trust; readability vs. micro-optimization
- Positions:
  - `readability-vs-manual-optimization--p1` — readability-over-manual-optimization-when-backend-cleans-up
    - **fitzgen** · Source `f001582` · date 2024-06-11 · locator comment 2024-06-11T16:35:49Z — eager vs. lazy default computation doesn't matter much here since LLVM can likely optimize it away, but the change is worth making for reader clarity Quote: "I think it probably doesn't matter much either way in this case, since there isn't anything here that could prevent LLVM from cleaning this up itself" [`b-sb05-f001582-c2`, team b]
- Positions seen by the extractor (`b-sb05-f001582-q2`): readability-over-manual-optimization-when-backend-cleans-up (fitzgen)

### `reduction-accumulation-precision`

**Question.** Should numeric reductions in a Rust ML kernel (e.g. softmax) accumulate in a higher-precision type than the input/output dtype?

- Teams: a · members (context): `a-sR04-f001096-q1` (f001096, ml)
- Domains: ml
- Concepts: numeric precision; reduction kernels; GPU kernels
- Positions:
  - `reduction-accumulation-precision--p1` — accumulate-in-float-for-precision
    - **ivarflakstad** · Source `f001096` · date 2025-01-13 · locator comment "Should probably accumulate with float in softmax to preserve precision. Shouldn't affect performance at all." — numeric reductions should accumulate in float32 even when the surrounding tensors are lower precision, to avoid precision loss, at negligible performance cost Quote: "Should probably accumulate with float in softmax to preserve precision." [`a-sR04-f001096-c1`, team a]
- Positions seen by the extractor (`a-sR04-f001096-q1`): accumulate-in-float-for-precision

### `reflection-security-risk`

**Question.** Does giving Rust code reflection-like or dynamic-loading capability introduce a security/soundness risk category that Rust's design has otherwise avoided?

- Teams: a · members (context): `a-sa28-f012469-q4` (f012469, core)
- Domains: core
- Concepts: reflection; dynamic loading; security; the (deprecated; ~2015) `Reflect` marker trait
- Positions:
  - `reflection-security-risk--p1` — universally-implemented-reflection-is-suspicious
    - **durka42 — track record uncertain in this source (recurring #rust-internals/IRC participant, no confirmed authored crate/book found here); logged with this caveat** · Source `f012469` · date 2015-12-01 · locator post by @XMPPwocky dated 2015-12-01T00:17:43Z, quoting an IRC/forum exchange about the (now-deprecated) `Reflect` marker trait — reacts to the `Reflect` trait (auto-implemented for all types) as inherently ominous Quote: "it's like tapping the Marauder's Map with your wand and saying 'I solemnly swear I am up to no good'" [`a-sa28-f012469-c7`, team a]
  - `reflection-security-risk--p2` — rust-lacks-reflection-and-that-closes-off-a-footgun-class
    - **vitalyd — track record uncertain in this source (recurring, substantive technical poster; no confirmed authored crate/book found here); logged with this caveat** · Source `f012469` · date 2017-09-12 · locator post by @vitalyd dated 2017-09-12T12:52:15Z — distinguishes a Java/Struts-style deserialization RCE footgun (enabled by reflection + dynamic class loading) from Rust, where the same outcome would require someone to deliberately build a serde-serializable type to do it — not an accidental byproduct of a language feature Quote: "Rust doesn't have dynamic class loading and reflection, but someone could build a serde serializable type to do custom remote command/process execution. It would be deliberate and not some oversight though, but still possible given enough will." [`a-sa28-f012469-c8`, team a]
- Positions seen by the extractor (`a-sa28-f012469-q4`): half-joking unease that a trait "implemented by all types" is inherently suspicious (durka42, 2015, weak evidentiary weight — see caveat) vs. a serious technical claim that Rust's *absence* of reflection/dynamic class loading closes off a whole footgun category that Java-style systems (e.g. Struts) have to guard against explicitly (vitalyd, 2017)

### `reject-connections-before-handshake`

**Question.** Should an async network server reject invalid/unauthenticated incoming connections before or after the handshake completes?

- Teams: a · members (context): `a-sR13-f004586-q3` (f004586, decentralized-iroh, distributed)
- Domains: decentralized-iroh, distributed
- Concepts: async runtimes; QUIC; connection handling
- Positions:
  - `reject-connections-before-handshake--p1` — reject-early
    - **iroh/n0 (dignifiedquire, post author)** · Source `f004586` · date 2026-04-17 · locator § "Rate Limiting in the Router" — the router gained an `incoming_filter` hook so a public endpoint can accept/reject/retry an incoming connection by address, endpoint ID, or ALPN before the handshake finishes, because rejecting early is far cheaper than accepting then closing Quote: "Rejecting early is much cheaper than closing the connection after it's established... Benchmarks on the PR show ~30x throughput for address-based rejection vs. accepting and closing." [`a-sR13-f004586-c3`, team a]
- Positions seen by the extractor (`a-sR13-f004586-q3`): reject-early (iroh)

### `release-lto`

**Question.** Should release builds enable LTO given its compile-time cost?

- Teams: b · members (context): `b-bk02-f000256-q12` (f000256, wasm)
- Domains: wasm
- Concepts: link-time optimization; build configuration
- Positions:
  - `release-lto--p1` — enable LTO in release builds despite longer compile times, for both smaller and faster wasm
    - **rustwasm working group (Rust and WebAssembly book) [voice-unverified]** · Source `f000256` · date unknown (living doc) · locator § "Shrinking .wasm Code Size" → Compiling with Link Time Optimizations (LTO) — states LTO's benefit (smaller and faster output, via more inlining/pruning) against its named cost (longer compilation), recommending it anyway. Quote: "Not only will it make the .wasm smaller, but it will also make it faster at runtime! The downside is that compilation will take longer." [`b-bk02-f000256-c13`, team b]
- Positions seen by the extractor (`b-bk02-f000256-q12`): enable LTO — smaller and faster at runtime, worth the slower compile (chosen); skip LTO to keep compiles fast (named alternative, implicitly rejected)

### `release-on-request`

**Question.** Should a Rust crate maintainer cut a release as soon as a user asks for a merged fix, or batch fixes into planned releases?

- Teams: a · members (context): `a-sT07-f002883-q1` (f002883, core, wasm)
- Domains: core, wasm
- Concepts: release cadence; crate maintenance; semver releases
- Positions:
  - `release-on-request--p1` — release-on-request
    - **daxpedda** · Source `f002883` · date 2025-08-06 · locator comment 2025-08-06T11:36 ("My 2¢"), follow-up 2025-08-06T11:43 — making a release costs little, so a release should follow as soon as one is requested; a request in a closed PR counts, with a tracking issue so it is not lost Quote: "making a release is relatively low cost so I favor making one as soon as requested" (flag: voice-unverified — Rust connection in the source is the maintainer role on wasm-bindgen stated in the same comment. Left out: the 1 MiB decoder margin (bes 2025-08-06T09:00 vs daxpedda's request for the exact failing byte count) is a JavaScript workaround detail, not a Rust decision; "Lets convert those to hex" and the `let`/`const` choice carry no reason on a Rust decision.) [`a-sT07-f002883-c1`, team a]
- Positions seen by the extractor (`a-sT07-f002883-q1`): release-on-request

### `release-sequencing-after-dependency-major`

**Question.** Should a Rust library release wait for, or be sequenced after, a new major version of a core dependency (arrow 58 before DataFusion 52), or ship on schedule against the current major's minor?

- Teams: b · members (context): `b-sT07-f003809-q1` (f003809, core, distributed)
- Domains: core, distributed
- Concepts: release coordination across crate ecosystems; major vs minor dependency bumps; downstream patch carrying
- Positions:
  - `release-sequencing-after-dependency-major--p1` — ship DataFusion 52 against the planned arrow minor (57.2.0)
    - **alamb** · Source `f003809` · date 2026-01-06 · locator comment 2026-01-06T15:41:44Z — the next arrow release is minor 57.2.0; being minor, it should work with DataFusion 52, so no reordering Quote: "Since it is a minor version I think you should be able to update to use it with DataFusion 52" (flag: voice-unverified) [`b-sT07-f003809-c2`, team b]
- Positions seen by the extractor (`b-sT07-f003809-q1`): release arrow major first so downstream can drop patches; ship on the planned arrow minor

### `repr-c-for-persistent-memory`

**Question.** Should Rust types that back raw/mmap'd persistent memory declare `#[repr(C)]`, given Rust makes no default layout guarantee across compiler/binary versions?

- Teams: b · members (context): `b-sb19-f005836-q2` (f005836, core)
- Domains: core
- Concepts: repr(C); memory layout stability; ABI
- Positions:
  - `repr-c-for-persistent-memory--p1` — repr-c-required
    - **Graham King** · Source `f005836` · date 2024-01-17 · locator § "Here's an arbitrary object we will use throught the post" — `#[repr(C)]` is needed to keep the in-memory layout stable across binary versions, since default Rust layout carries no such guarantee Quote: "The repr(C) ensures that the in-memory layout (representation) of this object doesn't change between versions of our binary. Rust makes no promises on memory layout unless you request a specific representation." [`b-sb19-f005836-c2`, team b]
- Positions seen by the extractor (`b-sb19-f005836-q2`): repr-c-required (Graham King)

### `repr-packed-vs-byte-array`

**Question.** When a struct's fields need a smaller in-memory footprint than natural alignment would otherwise give, should Rust code use `#[repr(packed)]` to force the tight layout (concise, but taking a reference to a misaligned field is undefined behavior), or should it store the fields packed into a raw byte array and expose them through typed accessor methods (safer, more verbose, same codegen)?

- Teams: b · members (context): `b-sb17-f005113-q1` (f005113, distributed)
- Domains: distributed
- Concepts: struct memory layout; alignment; `#[repr(packed)]`; undefined behavior; manual byte packing
- Positions:
  - `repr-packed-vs-byte-array--p1` — avoid-repr-packed-use-byte-array-getters
    - **Zaidoon Abd Al Hadi** · Source `f005113` · date 2026-09-18 · locator article body, "Storage improvements" section — rejects the tempting `#[repr(packed)]` shortcut to shrink the `Point` struct as "controversial for good reasons," and instead stores the hash/index pair as a raw `[u8; 6]` with getter methods, which compiles to the same layout without exposing misaligned references Quote: "You (meaning me) might be tempted to use #[repr(packed)], but that is controversial for good reasons. A safer but less readable solution is to store the hash and index as raw byte array and access them with getters. Both methods compile to the same thing." [`b-sb17-f005113-c1`, team b]
- Positions seen by the extractor (`b-sb17-f005113-q1`): avoid-repr-packed-use-byte-array-getters (Zaidoon Abd Al Hadi)

### `required-signals-vs-option-pins`

**Question.** When a driver constructor takes a set of GPIO/peripheral signals, should each signal be a required explicit value (even a placeholder like `Level::Low`), or should `Option<PIN>` be allowed so unused signals can be omitted?

- Teams: a · members (context): `a-sR06-f002005-q2` (f002005, embedded)
- Domains: embedded
- Concepts: driver constructor API design; `Option<PIN>` vs required value
- Positions:
  - `required-signals-vs-option-pins--p1` — driver constructors should require an explicit signal value for every input/output rather than accepting `Option<PIN>`
    - **Dominaezzz** · Source `f002005` · date 2024-09-09 · locator PR #2128, comment 2024-09-09T21:56:59Z — argues that once the PR lands, no driver should accept `Option<PIN>`; users should set every signal explicitly, mainly to prevent a previous driver's signal settings from lingering. Quote: "once this PR lands no drivers should be `Option<PIN>`, imo users should explicitly set each signal to something even if it's `Level::{Low, High}`." [`a-sR06-f002005-c2`, team a]
- Positions seen by the extractor (`a-sR06-f002005-q2`): "require an explicit value for every signal, no `Option<PIN>`" (Dominaezzz)

### `restrict-external-construction`

**Question.** For a small, always-internally-constructed validated type, should the public API expose fallible external construction, or restrict construction entirely to the crate's own internals?

- Teams: a · members (context): `a-sa11-f004265-q3` (f004265, embedded)
- Domains: embedded
- Concepts: API surface design; type validity invariants
- Positions:
  - `restrict-external-construction--p1` — restrict external construction of the validated type
    - **MabezDev** · Source `f004265` · date 2026-02-20 · locator comment 2026-02-20T09:47:34Z — says a constructor should return an error but leans toward not letting external callers create a Mac address at all Quote: "I'd be more in favour of not allowing others to create a Mac address initially" [`a-sa11-f004265-c4`, team a]
    - **playfulFence** · Source `f004265` · date 2026-02-20 · locator comment 2026-02-20T11:12:14Z — agrees with MabezDev that external construction doesn't make sense since all values are created internally Quote: "Yeah, agreed, doesn't make much sense, as they all will be created internally" [`a-sa11-f004265-c5`, team a]
- Positions seen by the extractor (`a-sa11-f004265-q3`): don't allow external construction at all, since every value in practice is created internally

### `retain-joinhandles`

**Question.** Should Tokio's `spawn`, when the task's result isn't otherwise needed, routinely be fire-and-forget with the `JoinHandle` dropped (Tokio's own examples do this), or should every spawned task's `JoinHandle`/`JoinSet` be retained and polled so a panic inside it is never silently swallowed?

- Teams: b · members (context): `b-sb17-f005159-q5` (f005159, decentralized-iroh)
- Domains: decentralized-iroh
- Concepts: `tokio::spawn`; `JoinHandle`; silent panic swallowing; `JoinSet`; structured concurrency
- Positions:
  - `retain-joinhandles--p1` — always-retain-and-poll-joinhandles
    - **Rüdiger Klaehn** · Source `f005159` · date 2024-07-31 · locator article body, "Detached tasks and swallowed panics" section — warns that Tokio makes it easy and "in fact encouraged" to drop a `JoinHandle` and let a task run detached, silently swallowing any panic inside it; recommends always polling handles (via `buffered_unordered`, `JoinSet`, or a custom `AbortingJoinHandle`) so panics surface Quote: "Avoid using tokio::spawn without handling the result... In the vast majority of async examples I have seen, tokio::spawn is called and the resulting JoinHandle is immediately discarded." [`b-sb17-f005159-c5`, team b]
- Positions seen by the extractor (`b-sb17-f005159-q5`): always-retain-and-poll-joinhandles (Rüdiger Klaehn)

### `reuse-vs-purpose-built-unwind`

**Question.** When a new profiling/debugging feature needs stack unwinding, should it reuse and refactor the codebase's existing general-purpose unwind implementation (more consistent, avoids duplicated maintenance) even where that path is much slower, or should it ship a separate, purpose-built implementation optimized for the feature's own constraints (faster, but duplicates unwind logic)?

- Teams: b · members (context): `b-sb13-f004160-q1` (f004160, embedded)
- Domains: embedded
- Concepts: code reuse vs duplication; stack unwinding; frame-pointer walking vs DWARF unwinding; maintenance burden vs performance
- Positions:
  - `reuse-vs-purpose-built-unwind--p1` — prefer-reuse-existing-unwind-logic
    - **bugadani** · Source `f004160` · date 2026-01-26 · locator comment 2026-01-26T19:58:25Z — is fine with two separate collection methods existing, but does not want a second, parallel implementation of debuginfo-less unwinding when a battle-tested one already exists in the codebase Quote: "What I would like to prevent is the parallel implementation of the unwinding-without-debuginfo code that we already have implemented and somewhat battle-tested." [`b-sb13-f004160-c1`, team b]
  - `reuse-vs-purpose-built-unwind--p2` — prefer-purpose-built-implementation-for-performance
    - **KingCol13** · Source `f004160` · date 2026-01-25 · locator PR description 2026-01-25T20:35:34Z — chose a simpler frame-pointer-only unwinder over the existing DWARF-based unwind machinery because the general implementation does more than needed and is far slower for this purpose Quote: "this may be more work since `probe-rs`'s unwind does more than is needed for this purpose and hence is ~100x slower than this frame pointer unwind." [`b-sb13-f004160-c2`, team b]
- Positions seen by the extractor (`b-sb13-f004160-q1`): prefer-reuse-existing-unwind-logic (bugadani), prefer-purpose-built-implementation-for-performance (KingCol13)

### `roadmap-performance-vs-features`

**Question.** Should a project's roadmap prioritize performance-focused effort over new-capability work when both compete for the same limited contributor time?

- Teams: b · members (context): `b-sR04-f001724-q1` (f001724, core)
- Domains: core
- Concepts: project roadmap prioritization; contributor time allocation; performance engineering
- Positions:
  - `roadmap-performance-vs-features--p1` — perf-first-for-a-quarter
    - **ozankabak** · Source `f001724` · date 2024-07-13 · locator issue comment, 2024-07-13T09:20:20Z — DataFusion is already in good shape on extensibility/customizability, so the project should dedicate one or two quarters specifically to performance rather than new features. Quote: "It would be great to have one or two quarters where we focus on perf." [`b-sR04-f001724-c1`, team b]
  - `roadmap-performance-vs-features--p2` — feature-work-also-serves-perf
    - **notfilippo** · Source `f001724` · date 2024-07-14 · locator issue comment, 2024-07-14T17:55:14Z — argues his in-progress logical-types proposal is not purely a feature detour, since it would itself improve performance (late materialization for REE arrays/string views); still agrees to rescope it to be easier to manage given the perf-quarter push. Quote: "I would argue that introducing proper support for logical types would benefit performance, especially in late materialization for REE arrays and string views." [`b-sR04-f001724-c2`, team b]
- Positions seen by the extractor (`b-sR04-f001724-q1`): perf-first-for-a-quarter, feature-work-also-serves-perf

### `rpc-error-detail-vs-flat-outcome`

**Question.** Should an RPC failure response be a `Result<T, E>` carrying a detailed error, or a flat enum exposing only coarse, intentionally limited outcomes?

- Teams: a · members (context): `a-sa06-f003590-q1` (f003590, decentralized-iroh)
- Domains: decentralized-iroh
- Concepts: error handling; RPC protocol design; serialization
- Positions:
  - `rpc-error-detail-vs-flat-outcome--p1` — flat outcome enum over `Result<T, E>` for RPC responses
    - **Rüdiger Klaehn** · Source `f003590` · date 2025-09-26 · locator § RPC protocol / KV store protocol — explains the DHT's `SetResponse` is a plain enum rather than `Result<(), SetError>` because serializing detailed errors is often painful and because failure specifics like stack traces are "nobody's business"; the enum only tells the caller enough to decide whether retrying makes sense Quote: "you have to be aware that serializing detailed errors is sometimes a big pain" [`a-sa06-f003590-c1`, team a]
- Positions seen by the extractor (`a-sa06-f003590-q1`): use a flat outcome enum (e.g. `ErrFull`, `ErrInvalid`) instead of `Result<(), SetError>`, deliberately omitting fine-grained error detail

### `rust-core-guidelines-document`

**Question.** should Rust have a prescriptive "core guidelines" document (as C++ has C++ Core Guidelines), or rely on compiler enforcement plus automated lints (Clippy) and de-facto popular-crate conventions instead?

- Teams: a · members (context): `a-sa26-f011993-q1` (f011993, core)
- Domains: core
- Concepts: language guidelines; Clippy lints; idiomatic Rust; static analysis
- Positions:
  - `rust-core-guidelines-document--p1` — enforce via compiler and Clippy lints rather than write a guidelines document
    - **kornel (forum handle; identity/track record not established by this source, flagged for t3 verification)** · Source `f011993` · date 2024-07-04T18:13:51.115Z · locator https://users.rust-lang.org/t/is-there-something-like-rust-core-guidelines-like-c-core-guidelines/113850/3 (post 3) — Rust's preferred solution is to avoid needing such a document at all — the language is designed to be statically analyzable so the compiler enforces as much of "the guidelines" as possible, and for softer/more subjective conventions, Clippy lints are written instead of documenting best practices, with popular crates serving as de-facto standards Quote: "In Rust, the preferred solution is to avoid the need for such document to exist... Whenever a gotcha is discovered in Rust, instead of documenting the best practice that avoids it, someone writes a Clippy lint for it" [`a-sa26-f011993-c1`, team a]
- Positions seen by the extractor (`a-sa26-f011993-q1`): prefer-compiler-and-lint-enforcement-over-a-guidelines-document (forum user "kornel")

### `rust-cuda-vs-cpp-kernels`

**Question.** For GPU kernel programming from Rust, should the ecosystem invest in a community-driven Rust-native toolchain (rust-cuda) rather than continuing to write kernels in C++/CUDA with a thin Rust host layer, given CUDA's vendor lock-in and rust-cuda's current feature gaps?

- Teams: b · members (context): `b-sb23-f011233-q1` (f011233, ml, other)
- Domains: ml, other
- Concepts: rust-cuda; CUDA; PTX; GPU kernels; vendor lock-in
- Positions:
  - `rust-cuda-vs-cpp-kernels--p1` — rust-cuda is the right direction despite CUDA's vendor lock-in and the ecosystem's current gaps
    - **Evgenii Seliverstov** · Source `f011233` · date 2025-02-26 · locator ~45:52-48:54 (GPU section + audience Q&A) — presents Rust-CUDA (kernels and host code both in Rust, wrapping LLVM/NVVM/PTX) as the exciting alternative to writing kernels in C++/CUDA; when the audience presses on CUDA being vendor-specific and asks about AMD/other-vendor equivalents, he concedes he knows of none and that almost all real GPU work still goes through C++ kernels with a thin Rust host layer Quote: "it allows us to write kernels in Rust instead of C++ ... I'm really excited about this" [`b-sb23-f011233-c1`, team b]
- Positions seen by the extractor (`b-sb23-f011233-q1`): back rust-cuda because it lets kernels and host code both be written in Rust and stays community- rather than vendor-controlled, versus the practical reality (raised by the audience) that almost all real GPU work today still goes through vendor C++/CUDA because non-CUDA/non-C++ tooling lags

### `rust-efficiency-for-cloud-workloads`

**Question.** Is Rust's efficiency advantage over Python/Ruby/JS (energy, CPU, memory) large enough to justify adoption for cloud workloads?

- Teams: a · members (context): `a-sB01-f000149-q3` (f000149, cloud-workers, core)
- Domains: cloud-workers, core
- Concepts: energy-efficiency; CPU-time; memory-usage; sustainability
- Positions:
  - `rust-efficiency-for-cloud-workloads--p1` — large-quantified-advantage
    - **Noah Gift** · Source `f000149` · date 2023 (course release date stated in source) · locator "Sustainability" chapter — Endorses an AWS article's numbers as "nailing" the case for Rust, stating Rust cuts energy ~50%+, CPU time up to 75%, memory up to 95% versus Python/Ruby/JS Quote: "Rust uses at least 50% less energy than languages like Python." [`a-sB01-f000149-c3`, team a]
- Positions seen by the extractor (`a-sB01-f000149-q3`): large-quantified-advantage

### `rust-for-ai-generated-code`

**Question.** is Rust the best-suited language for an AI-driven future where machines write code and humans architect systems (because the compiler independently checks AI-generated code)?

- Teams: a · members (context): `a-sa26-f011443-q2` (f011443, ml, core, other)
- Domains: core, ml, other
- Concepts: AI-assisted Rust; compiler guarantees
- Positions:
  - `rust-for-ai-generated-code--p1` — Rust is the best language for an AI-coding future
    - **Mordecai Emmanuel Etukudo** · Source `f011443` · date 2026-06-11 · locator ~13:17-14:18 — as AI increasingly writes code and humans architect systems, Rust's compiler acts as an independent, automatic check on AI-generated code that other languages' compilers don't provide Quote: "Rust is the best language for AI because AI is is like bare machine... with Rust, which the compiler have already... is already there to vet your system and know that this code is not having memory leaks" [`a-sa26-f011443-c2`, team a]
- Positions seen by the extractor (`a-sa26-f011443-q2`): yes-Rust-is-best-for-AI-generated-code (Mordecai Etukudo)

### `rust-for-lambda-vs-interpreted`

**Question.** Is Rust worth its steeper learning curve for AWS Lambda/serverless functions, compared to interpreted languages (Python, JavaScript)?

- Teams: b · members (context): `b-sb19-f007042-q1` (f007042, cloud-workers)
- Domains: cloud-workers
- Concepts: cold start latency; AWS Lambda; Cargo Lambda; Option/Result vs null
- Positions:
  - `rust-for-lambda-vs-interpreted--p1` — worth-it-for-lambda
    - **Luciano Mammino** · Source `f007042` · date 2024-12-16 · locator § "Why Rust and Lambda?" — Rust's compiled binaries lower both memory-cost and execution-time dimensions of Lambda's billing formula versus JS/Python, and its lack of null / explicit Option-Result handling catches edge cases earlier; observed cold starts of 10-60ms, roughly 10-20x faster than JS/Python Quote: "With Rust, in most circumstances, you can lower both dimensions, compared to interpreted languages such as JavaScript and Python." [`b-sb19-f007042-c1`, team b]
- Positions seen by the extractor (`b-sb19-f007042-q1`): worth-it-for-lambda (Luciano Mammino)

### `rust-for-mlops-vs-python`

**Question.** For cloud/data/MLOps work, should Rust be the default language over Python?

- Teams: a · members (context): `a-sB01-f000149-q1` (f000149, ml, cloud-workers, core)
- Domains: cloud-workers, core, ml
- Concepts: language-choice-heuristic; MLOps; systems-vs-scripting
- Positions:
  - `rust-for-mlops-vs-python--p1` — Rust-first default
    - **Noah Gift** · Source `f000149` · date 2023 (course release date stated in source; no chapter-level date) · locator Chapter 1, "Heuristic: Rust if you can, Python if you must" — Sets Rust as the first-choice language for the course's cloud/data/MLOps projects, falling back to Python only when necessary Quote: "Rust if you can, Python if you must" [`a-sB01-f000149-c1`, team a]
- Positions seen by the extractor (`a-sB01-f000149-q1`): Rust-first default

### `rust-in-process-server-new-capability`

**Question.** Does using Rust to embed a full HTTP server as an in-process library (rather than nginx-style multi-process isolation) represent a genuinely new capability, or is the "safe language vs. dangerous C" framing overstated since C-based servers already work fine?

- Teams: a · members (context): `a-saL1-f005360-q1` (f005360, web, distributed, core)
- Domains: core, distributed, web
- Concepts: memory safety; library vs. process isolation; unsafe code; reverse proxies
- Positions:
  - `rust-in-process-server-new-capability--p1` — rust-enables-safe-in-process-libification
    - **kev009** · Source `f005360` · date 2024-10-13 · locator reply, 2024-10-13T16:18:35-05:00 — Argues the interesting part of building an HTTP server as an embeddable Rust library (rather than picking an existing server) is that it is a "lib-ification" of the web-server concept that was never realistic to do safely in C/C++, putting the author in full control of the HTTP workflow instead of fitting into a gateway/module system. Quote: "it represents lib-ification of the web server concept in a way that could maybe be done with C++... but weren't very realistic due to the inherent dangers" [`a-saL1-f005360-c1`, team a]
    - **matklad** · Source `f005360` · date 2024-10-14 · locator reply, 2024-10-14T07:01:58-05:00 — Refines the framing: it isn't "Rust safe, C dangerous" in the abstract, but that making well-written C safe to *use* generally requires isolating it in a separate process (as nginx does), whereas Rust lets an expert's cursed, high-performance code be reused safely as a library by less-expert programmers in the same language — which is genuinely novel. Quote: "It's not 'Rust safe, C danger' but rather that, to make _using_ well-written C safe you generally need to put it in a different process... while Rust allows you to use it as a library... _This_ is novel." [`a-saL1-f005360-c2`, team a]
  - `rust-in-process-server-new-capability--p2` — safety-framing-is-overstated
    - **pm** · Source `f005360` · date 2024-10-13 · locator reply, 2024-10-13T18:31:49-05:00 — Pushes back that framing a memory-safe language's libraries against C/C++'s dangers is "getting really old," since nginx and Apache (both written in C) already work fine as web servers. Quote: "This line of thinking is getting really old. You're talking about the languages nginx and Apache are written in." [`a-saL1-f005360-c3`, team a]
- Positions seen by the extractor (`a-saL1-f005360-q1`): rust-enables-safe-in-process-libification; safety-framing-is-overstated

### `rust-lang-org-ai-assistant`

**Question.** Should rust-lang.org (or official Rust community properties) integrate an AI assistant/LLM feature — semantic search, chat assistant, or interactive tutorials?

- Teams: a · members (context): `a-sa29-f013224-q1` (f013224, core)
- Domains: core
- Concepts: LLM; semantic search; retrieval-augmented generation; hallucination; documentation search; opt-in design
- Positions:
  - `rust-lang-org-ai-assistant--p1` — an AI assistant for rust-lang.org is acceptable if strictly opt-in
    - **jumpnbrownweasel** · Source `f013224` · date 2024-03-02T18:37:26Z · locator forum post, 2024-03-02T18:37:26.330Z — argues that hiding the feature from the UI unless enabled by a preference would defuse resistance, noting people already bring raw ChatGPT output to the forum for help, so a built-in assistant could improve on that status quo Quote: "Making it completely opt in...would avoid some resistance" [`a-sa29-f013224-c1`, team a]
  - `rust-lang-org-ai-assistant--p2` — rust-lang.org should not host an LLM feature; the cost/quality economics make it a net negative for an underfunded open-source project
    - **afetisov** · Source `f013224` · date 2024-03-06T17:56:37Z · locator forum post, 2024-03-06T17:56:37.176Z — argues LLMs are expensive to run well, only VC-subsidized companies can offer good models cheaply, and tuning response quality is a full-time job the community can't sustain, so users are better served using existing third-party AI services themselves Quote: "there is nothing gained and multiple problems rising from providing LLM at rust-lang.org" [`a-sa29-f013224-c2`, team a]
  - `rust-lang-org-ai-assistant--p3` — rust-lang.org's real search problem is inadequate full-text documentation search, not the absence of an LLM
    - **Vorpal** · Source `f013224` · date 2024-03-02T23:39:28Z · locator forum post, 2024-03-02T23:39:28.336Z — reports that current docs.rs search matches only type/item names, not documentation prose, citing a concrete miss (searching "replace" instead of the actual function name "interpolate" in regex-automata), and argues proper full-text search would be the bigger win Quote: "I believe just adding proper full text search would be a huge step forward" [`a-sa29-f013224-c3`, team a]
- Positions seen by the extractor (`a-sa29-f013224-q1`): support, especially if strictly opt-in (jasn-armstrng's original proposal; jumpnbrownweasel; kevinmcfarlane surprised at "hostility... especially if it's something you can opt out of") vs. opposed on hallucination, copyright/ideological, and cost grounds, and skeptical it beats the status quo (kornel citing MDN's poorly received assistant; afetisov on run-cost economics; lgoeldner proposing a "counter movement" banning AI content/search citing hallucinations and energy use; caellian arguing it would be detrimental to forum Q&A dynamics) vs. narrower view that the real gap is full-text documentation search, not an LLM (Vorpal; jofas limiting agreement to "improved documentation reach" alone)

### `rust-ml-edge-inference-vs-python`

**Question.** For offline/edge ML inference (no cloud connectivity, consumer hardware), is a Rust-based stack (Burn) a viable or superior alternative to the default Python/PyTorch stack, despite Python's ecosystem dominance for training?

- Teams: a · members (context): `a-sa18-f008787-q1` (f008787, ml, embedded, desktop-cli-ui, wasm)
- Domains: desktop-cli-ui, embedded, ml, wasm
- Concepts: burn; edge-ml; wasm; tauri; deployment-size; cold-start
- Positions:
  - `rust-ml-edge-inference-vs-python--p1` — rust-burn-viable-for-edge-inference
    - **Warre Snaet** · Source `f008787` · date 2026-01-24 · locator "Why Rust? The Burn Framework Decision" and "Conclusion" sections — chose Rust+Burn over Python/PyTorch for an offline plant-disease-detection model targeting phones/laptops with zero connectivity, citing a single ~24MB binary vs. ~7.1GB of PyTorch dependencies (300x), <100ms cold start vs. PyTorch's ~3s, and one model/codebase compiling to native GPU (wgpu), CPU (ndarray), WASM and Tauri-mobile targets; concludes the stack is legitimate for edge inference specifically, not for training Quote: "Rust + Burn is a legitimate ML stack. Not for training transformers, but for edge inference? It's hard to beat." [`a-sa18-f008787-c1`, team a]
- Positions seen by the extractor (`a-sa18-f008787-q1`): rust-burn-viable-for-edge-inference

### `rust-trademark-policy`

**Question.** How should the Rust trademark policy govern use of the Rust name and marks? Should it follow the Rust Foundation's 2023 draft, which drew widespread community concern, or a revised policy shaped by that feedback?

- Teams: a · members (context): `a-sT12-f009632-q1` (f009632, core)
- Domains: core
- Concepts: trademark policy; Rust Foundation; Leadership Council; community governance
- Positions:
  - `rust-trademark-policy--p1` — revised 2024 draft
    - **Rust Leadership Council** · Source `f009632` · date 2024-11-06 · locator paragraphs 1–3 — after community concern about the 2023 draft, the Council, Project Directors and Foundation revised the policy. The Council calls the new draft legally sound and able to protect the language's integrity, says it addresses the prevailing concerns, and opens it for final feedback until 2024-11-20 Quote: "The Leadership Council is confident that this updated version of the policy has addressed the prevailing concerns about the initial draft" (flag: voice-unverified (Rust connection in source: Rust project governance body, Rust Blog)) [`a-sT12-f009632-c1`, team a]
- Positions seen by the extractor (`a-sT12-f009632-q1`): revised 2024 draft (Leadership Council); 2023 initial draft (Foundation, superseded); community concerns (no named Voice)

### `rust-vs-gc-for-multitenant-runtime`

**Question.** Should a secure multi-tenant runtime that executes untrusted user code (e.g. a serverless JavaScript isolate hypervisor) be built in a language like Rust rather than a garbage-collected language like Go?

- Teams: a · members (context): `a-sa22-f011092-q1` (f011092, cloud-workers, distributed, core)
- Domains: cloud-workers, core, distributed
- Concepts: memory safety without a garbage collector; multi-tenant isolation/sandboxing; FFI/embedding a C++ engine (V8); async runtime scheduling
- Positions:
  - `rust-vs-gc-for-multitenant-runtime--p1` — rust-for-reliability-and-explicit-performance
    - **Luca Casonato** · Source `f011092` · date 2024-02-13 · locator transcript ~00:01:46-00:10:30 (talk, timestamps approximate from auto-captions) — Describes Deno's own history of first trying Go for its multi-tenant sandboxed runtime, and rejecting it because it lacked the reliability, strictness, customizability and performance needed to safely execute untrusted code for many tenants; chose Rust (with some C++ for the embedded V8 engine) instead, citing exhaustive Result/Option-based error handling, transparent/explicit allocation cost (no hidden allocations without an explicit `.clone()`), no conflict between a host garbage collector and V8's own GC in the same process, and easy C++ interop needed to embed V8 safely via `rusty_v8`-style bindings. Quote: "[Go] does not have the same reliability or strictness or customizability or performance that languages like rust or even C++ for that matter do" [`a-sa22-f011092-c1`, team a]
- Positions seen by the extractor (`a-sa22-f011092-q1`): rust-for-reliability-and-explicit-performance

### `safe-wrapper-soundness-scope`

**Question.** When a type wraps an unsafe operation and is labeled "safe," must that safety guarantee hold under every generic instantiation/composition, or is a narrower guarantee acceptable if the common case is sound?

- Teams: b · members (context): `b-sR10-f004804-q1` (f004804, embedded, core)
- Domains: core, embedded
- Concepts: unsafe; soundness; generics; type-level safety guarantees
- Positions:
  - `safe-wrapper-soundness-scope--p1` — overpromising-is-unsound
    - **Dominaezzz (esp-hal reviewer)** · Source `f004804` · date 2026-06-15 · locator PR review comment, 2026-06-15T21:09:39Z — calling the new reference type "safely useable" overpromises, since a composition such as boxing it with external-memory backing is not actually safe to use Quote: "\"safely useable\" is too vague and I feel it over promises a bit... Example of over promising, `Box<InternalMemory<[DmaDescriptor; 10]>, ExternalMemory>` is not safe to use." [`b-sR10-f004804-c1`, team b]
  - `safe-wrapper-soundness-scope--p2` — pragmatic-judgment-call-acceptable
    - **bugadani (esp-hal maintainer, PR author)** · Source `f004804` · date 2026-06-17 · locator PR review comment, 2026-06-17T07:36:32Z — without a full proof, a cache writeback is judged safe enough in practice for this type's current alignment guarantees, given invalidate isn't called on these paths Quote: "Wishy-washy, but a cache writeback is generally a safe operation as far as I can tell, and we don't call invalidate on these I think. So I think we're fine with the DmaDescriptor alignment in this type, at this time." [`b-sR10-f004804-c2`, team b]
- Positions seen by the extractor (`b-sR10-f004804-q1`): overpromising-is-unsound, pragmatic-judgment-call-acceptable

### `same-state-transition-trigger`

**Question.** For a component that triggers on a state-machine transition matching a predicate, should a transition into the same state the entity is already in be treated as a no-op (never triggering), or should it be allowed to trigger, to support "reload" style use cases?

- Teams: b · members (context): `b-sb14-f004398-q2` (f004398, core)
- Domains: core
- Concepts: state machines; state transitions; ECS state-scoped entities
- Positions:
  - `same-state-transition-trigger--p1` — raises-same-state-transition-question
    - **chescock** · Source `f004398` · date 2026-03-12 · locator comment @chescock 2026-03-12T14:28:50Z — questions whether transitions into the same state the entity is already in should be excluded from triggering the predicate, noting it's unclear which behavior is wanted without more use-case knowledge. Quote: "this check prevents despawning on same-state transitions. Do we really want to prevent that?" [`b-sb14-f004398-c5`, team b]
  - `same-state-transition-trigger--p2` — suppress-same-state-transitions
    - **Freyja-moth** · Source `f004398` · date 2026-03-12 · locator comment @Freyja-moth 2026-03-12T16:51:05Z — argues it doesn't make sense to react to a transition into a state the entity is already in. Quote: "I don't think it really makes sense to react to changing to a state you're already in." [`b-sb14-f004398-c6`, team b]
  - `same-state-transition-trigger--p3` — allow-naive-no-suppression
    - **alice-i-cecile** · Source `f004398` · date 2026-03-12 · locator comment @alice-i-cecile 2026-03-12T19:46:57Z — overrides Freyja-moth's suppression, noting some users specifically want same-state transitions to trigger for a "reload" pattern, and the naive (non-special-cased) behavior should be used. Quote: "Some folks have actually pushed for allowing same-state transitions precisely for a \"reload\" pattern. IMO we should use the naive behavior here." [`b-sb14-f004398-c7`, team b]
- Positions seen by the extractor (`b-sb14-f004398-q2`): suppress-same-state-transitions (Freyja-moth), allow-naive-no-suppression (alice-i-cecile)

### `scoped-impls-nameable`

**Question.** Should scoped trait implementations be nameable, or must they stay anonymous?

- Teams: a · members (context): `a-sa19-f009123-q1` (f009123, core)
- Domains: core
- Concepts: trait coherence; orphan rules; scoped impls; trait implementation naming
- Positions:
  - `scoped-impls-nameable--p1` — anonymous-impls-required-for-coherence
    - **Tamschi** · Source `f009123` · date 2023-12-05 · locator reply to scottmcm/Nadrieril, 2023-12-05T20:39:46.548Z — Opposes naming scoped implementations; anonymity keeps coherence checking simple within one scope, lets the module double as an error-message name, and avoids new breaking-change rules that naming would introduce when an implementation is later broadened. Quote: "Regarding proper-naming implementations: I'm very strongly opposed to it, since I think it is squarely detrimental here, mainly in terms of clarity but also syntactically and for ease of use." [`a-sa19-f009123-c1`, team a]
  - `scoped-impls-nameable--p2` — named-impls-for-clarity
    - **scottmcm** · Source `f009123` · date 2023-11-29 · locator reply, 2023-11-29T03:31:09.374Z — Wants names for non-global impls so two implementations of the same trait/type can coexist in one module, and so compiler error messages can use a normal path instead of "the impl from this module". Quote: "I feel like they wanted names, and with names you even define two impls ... I think it would be nice to give normal paths to named things in those errors." [`a-sa19-f009123-c2`, team a]
    - **Nadrieril** · Source `f009123` · date 2023-12-05 · locator reply, 2023-12-05T13:43:01.887Z — Suggests an explicit naming mechanism so the implicit scoped-impl behavior desugars from something writable, making the proposal easier to explain even if users rarely write the explicit form. Quote: "I would suggest that you provide an explicit mechanism to specify a type along with explicitly chosen impls." [`a-sa19-f009123-c3`, team a]
- Positions seen by the extractor (`a-sa19-f009123-q1`): anonymous-impls-required-for-coherence; named-impls-for-clarity

### `scratch-buffer-vs-per-call-alloc`

**Question.** In a hot loop, should working memory be a caller-owned scratch buffer reused across calls, or freshly allocated per call for simplicity?

- Teams: b · members (context): `b-sR12-f005120-q2` (f005120, ml, core)
- Domains: core, ml
- Concepts: allocation; buffer reuse; hot-path performance
- Positions:
  - `scratch-buffer-vs-per-call-alloc--p1` — caller-owned-scratch-buffer
    - **Arthur Zucker / Hugging Face tokenizers team** · Source `f005120` · date 2026-09-21 · locator section "The Merge Loop" — the previous implementation allocated fresh memory and a new priority queue per pre-token; v1 instead reuses a scratch buffer owned by the caller so the merge loop never touches the allocator Quote: "v1 reuses a scratch buffer owned by the caller, removing those repeated allocations... the merge working set lives in a caller-owned scratch buffer; the loop never touches the allocator." [`b-sR12-f005120-c2`, team b]
- Positions seen by the extractor (`b-sR12-f005120-q2`): caller-owned-scratch-buffer

### `semver-break-signaling-in-ci`

**Question.** How should a Rust crate signal and enforce semver-breaking changes in CI and release tooling?

- Teams: b · members (context): `b-bk03-f000267-q7` (f000267, core)
- Domains: core
- Concepts: semver; conventional commits; release automation; CI gates
- Positions:
  - `semver-break-signaling-in-ci--p1` — title-marker-plus-commit-marker-gates-ci
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Contributing § Pull Requests, "Declare breaking changes" — a change that breaks a published crate's public API must be marked with `!` in both the PR title and the branch commit introducing the break, because the CI gate reads the PR title to skip semver-checks and require a breaking-change fragment, while release-plz separately reads the commits landing on main — which include the branch commits — to decide the major-version bump Quote: "The PR gate reads the title: that is what skips semver-checks and requires a breaking change fragment." (flag: voice-unverified) [`b-bk03-f000267-c7`, team b]
- Positions seen by the extractor (`b-bk03-f000267-q7`): title-marker-plus-commit-marker-gates-ci

### `serde-centralization`

**Question.** Should Rust's derive/serialization ecosystem centralize around one blessed crate (serde) that other crates interoperate through, given orphan rules make independent multi-crate composition hard?

- Teams: a · members (context): `a-sa25-f011413-q2` (f011413, core, web)
- Domains: core, web
- Concepts: orphan rules; trait coherence; serde; ecosystem composition
- Positions:
  - `serde-centralization--p1` — orphan-rules-force-derive-centralization
    - **Amos (fasterthanlime)** · Source `f011413` · date 2026-06-11 · locator ~00:03:06–00:04:00 — Rust's orphan rules mean crates that want to interoperate with a popular derive macro (serde) must piggyback on it rather than add independent support, functionally cornering the ecosystem around one crate Quote: "rust orphan rules have created an ecosystem composition problem" [`a-sa25-f011413-c2`, team a]
  - `serde-centralization--p2` — ship-type-data-instead-of-more-derives
    - **Amos (fasterthanlime)** · Source `f011413` · date 2026-06-11 · locator ~00:04:00–00:05:00 — rather than generating a new derive for every new trait/behavior, crates should ship structural data about their types once, and build behaviors generically over that data Quote: "the idea of many crates building upon a singular derive is, in my opinion, sound. We just have to kind of adjust our strategy... we might consider shipping data about our types" [`a-sa25-f011413-c3`, team a]
- Positions seen by the extractor (`a-sa25-f011413-q2`): "centralizing on one derive is sound in principle, the strategy just needs adjusting (ship type data instead of more code)" vs. the joking-but-pointed framing of that same centralization as a de facto monopoly ("cornered the entire market")

### `share-via-combinator-vs-separate-impls`

**Question.** When two operations are logically distinct (a local op returning a `Tensor` vs. a collective op returning a `{PeerId: Tensor}` map) but share underlying logic, should the crate share code via a combinator abstraction or keep them separately implemented?

- Teams: a · members (context): `a-sR11-f003983-q2` (f003983, ml, distributed)
- Domains: distributed, ml
- Concepts: code duplication; abstraction boundaries; collective/distributed tensor ops
- Positions:
  - `share-via-combinator-vs-separate-impls--p1` — extract-a-shared-combinator-even-if-unexposed
    - **crutcher** · Source `f003983` · date 2025-12-12 · locator comment 2025-12-12T20:24:57Z — `reduce_sum` (local) and `all_reduce_sum` (collective) are different operations, but the duplication between them is real and worth solving with an internal op-combinator library, even if that library never reaches end users Quote: "we probably want a local op-combinator library to avoid that duplication, even if those ops aren't shared to users" [`a-sR11-f003983-c2`, team a]
- Positions seen by the extractor (`a-sR11-f003983-q2`): extract-a-shared-combinator-even-if-unexposed (crutcher)

### `shared-hw-resource-refcount-vs-raii`

**Question.** For a shared hardware resource with an enable/disable lifecycle (a radio PHY clock shared across peripherals), should safety rest on a reference-counted controller object, or on RAII-style exclusive ownership tied to the peripheral singletons themselves?

- Teams: a · members (context): `a-sa05-f003169-q1` (f003169, embedded)
- Domains: embedded
- Concepts: ownership; RAII; concurrency-primitives; embedded-resource-management
- Positions:
  - `shared-hw-resource-refcount-vs-raii--p1` — reference-counted-controller
    - **Frostie314159** · Source `f003169` · date 2025-06-24 · locator comment @Frostie314159 2025-06-24T13:26:21Z / 2025-06-24T15:18:21Z — proposes a `RadioClockController` that counts references per modem so disabling one modem's use of the shared PHY clock doesn't disable it out from under another modem still relying on it Quote: "unless we count the reference for each modem clock controller individually, just repeatedly calling the function to disable the PHY clock on one modem clock controller, would eventually disable the PHY clock, even if different modems still rely on it." [`a-sa05-f003169-c1`, team a]
  - `shared-hw-resource-refcount-vs-raii--p2` — raii-exclusive-ownership
    - **bugadani** · Source `f003169` · date 2025-06-25 · locator comment @bugadani 2025-06-25T13:18:42Z / 2025-06-25T13:29:48Z — questions why a separate `RadioClockController` and manual ref-count are needed at all if only the peripheral singletons (already unique/exclusive by construction) can touch the clock; proposes implementing the clock-control logic directly on the radio peripheral structs instead Quote: "I'd just implement all relevant code for the radio singletons, then only radio users could meddle with any of this." [`a-sa05-f003169-c2`, team a]
    - **Frostie314159** · Source `f003169` · date 2025-07-01 · locator comment @Frostie314159 2025-07-01T15:05:34Z — having converged with the reviewer, removes the separate `RadioClockController` and reduces the design to a single shared PHY ref-count guarded by the peripheral-singleton pattern Quote: "I've removed it with the latest commit." [`a-sa05-f003169-c3`, team a]
- Positions seen by the extractor (`a-sa05-f003169-q1`): reference-counted-controller, raii-exclusive-ownership

### `shared-model-crate-vs-domain-split`

**Question.** When a Bevy codebase grows past tens of thousands of lines and single-crate compile times become disruptive, should shared types be pulled into one low-level crate that everything depends on (simple, but the worst-case recompile unit), or should the codebase instead be split along domain lines to avoid any single always-recompiled root crate?

- Teams: b · members (context): `b-sb25-f012561-q2` (f012561, other)
- Domains: other
- Concepts: crate splitting; compile times; incremental builds; domain-driven modularization
- Positions:
  - `shared-model-crate-vs-domain-split--p1` — keep one shared low-level "model" crate rather than doing a full domain-driven crate split
    - **Tristan** · Source `f012561` · date 2025-06-18 · locator ~26:33-27:33 (audience Q&A) — when asked directly by an audience member whether he considered a domain-driven crate separation instead of "everything depends on model," he says he could have, but the split happened too late in the project's life to be worth the time and energy, so `model` became a catch-all for whatever must be shared, kept as small as discipline allows Quote: "when the splits occured it was already too late ... I couldn't find the time and the energy to ... split" [`b-sb25-f012561-c2`, team b]
- Positions seen by the extractor (`b-sb25-f012561-q2`): keep one shared "model" crate that only holds what truly must cross domain boundaries, accepting it as the worst-case recompile surface, because a full domain-driven split wasn't worth the time/energy once the codebase was already large (Tristan's choice); split along domain lines from the start to avoid a shared-everything root crate (raised by an audience member as the alternative he didn't take)

### `ship-polyfill-before-spec`

**Question.** before a spec (WASI 0.3 async) is finalized, should the ecosystem ship stopgap/polyfill implementations to unblock development, or wait for the finished standard?

- Teams: b · members (context): `b-sR03-f000889-q1` (f000889, wasm)
- Domains: wasm
- Concepts: none given
- Positions:
  - `ship-polyfill-before-spec--p1` — favors shipping a polyfill ahead of the spec.
    - **Joel Dice (Fermyon, component-model/wasmtime contributor)** · Source `f000889` · date 2024-02-05 · locator bytecodealliance.org/articles/plumbers-day-2, "Async and WASI 0.3" section, talk timestamp 1:11:00. · L465-L472. — favors shipping a polyfill ahead of the spec. Quote: a "'polyfill' that devs can play with today while they're waiting for WASI 0.3 and real async." [`b-sR03-f000889-c1`, team b]
- Positions seen by the extractor (`b-sR03-f000889-q1`): favors shipping a polyfill ahead of the spec. (Joel Dice (Fermyon, component-model/wasmtime contributor))

### `silent-fallback-vs-explicit-error`

**Question.** When a caller's input is ambiguous or partially satisfiable (multiple matching sockets, or a requested feature with no usable input at all), should the code silently proceed with a plausible default, or fail with an explicit error?

- Teams: a · members (context): `a-sa14-f005079-q5` (f005079, core)
- Domains: core
- Concepts: fail-loud vs. silent fallback; explicit error handling; surprising behavior
- Positions:
  - `silent-fallback-vs-explicit-error--p1` — error on ambiguous multiple-socket input rather than silently pick one
    - **alexcrichton** · Source `f005079` · date 2026-09-10 · locator comment 2026-09-10T22:28:43Z — asks whether the code should return an error if multiple TCP sockets are listed, rather than silently using the first, since that could cause odd behavior if the first one happens to be the wrong one Quote: "Should this perhaps return an error if there are multiple TCP sockets listed? Because otherwise using the first feels like it might lead to odd behavior" [`a-sa14-f005079-c6`, team a]
  - `silent-fallback-vs-explicit-error--p2` — error rather than silently fall back when the flag was explicitly requested
    - **simolus3** · Source `f005079` · date 2026-09-11 · locator comment 2026-09-11T10:19:47Z — made the multiple-socket case an error, and also made it an error to have no usable socket at all, reasoning it would be surprising for `--systemd-listenfd` to silently fall back to wasmtime listening itself because of a mismatched environment variable Quote: "it might be surprising to explicitly indicate that inherited sockets are requested with `--systemd-listenfd` only to then have wasmtime listen itself because of a mismatched environment variable that's ignored" [`a-sa14-f005079-c7`, team a]
- Positions seen by the extractor (`a-sa14-f005079-q5`): return an explicit error rather than silently picking the first of several candidates, and error out rather than silently falling back to normal listening when the flag was explicitly requested but no usable input was found

### `single-pass-vs-multi-pass-iteration`

**Question.** should derived per-column values be computed in a single iterator pass or via several simpler passes/collects?

- Teams: b · members (context): `b-sR03-f000763-q2` (f000763, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: none given
- Positions:
  - `single-pass-vs-multi-pass-iteration--p1` — prefer single-pass computation over iterating a collected result multiple times.
    - **joshka** · Source `f000763` · date 2024-01-18 · locator ratatui/ratatui#840, comment 2024-01-18T22:33:34Z. · L403-L406. — prefer single-pass computation over iterating a collected result multiple times. Quote: "If you're iterating and collecting then iterating on the result 3 times or might be neater to iterate and collect the max for each column in a single iteration." [`b-sR03-f000763-c2`, team b]
- Positions seen by the extractor (`b-sR03-f000763-q2`): prefer single-pass computation over iterating a collected result multiple times. (joshka)

### `single-vs-multi-threaded-executor`

**Question.** Should an async application use a single-threaded or multi-threaded executor?

- Teams: b · members (context): `b-bk01-f000233-q12` (f000233, core, distributed, ml)
- Domains: core, distributed, ml
- Concepts: executor; multi-threading; synchronization overhead
- Positions:
  - `single-vs-multi-threaded-executor--p1` — measure for the specific workload, no blanket rule
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "The Async Ecosystem" § Single Threaded vs Multi-Threaded Executors — a multi-threaded executor can speed up workloads with many tasks by making progress on several simultaneously, but synchronizing data between tasks becomes more expensive; rather than defaulting to one or the other, recommends measuring performance for the application at hand when choosing between a single- and multi-threaded runtime. Quote: "It is recommended to measure performance for your application when you are choosing between a single- and a multi-threaded runtime." [`b-bk01-f000233-c13`, team b]
- Positions seen by the extractor (`b-bk01-f000233-q12`): no blanket rule — measure for the specific workload

### `slint-vs-qt`

**Question.** For cross-platform desktop/embedded GUI development from Rust, should a team adopt a new compile-time-checked toolkit (Slint) over a mature, runtime-interpreted one (Qt/QML), given Slint's smaller ecosystem (missing multimedia, 3D, multi-window, automated UI testing, no iOS support yet)?

- Teams: b · members (context): `b-sb23-f011133-q1` (f011133, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: Slint; QML; Qt; declarative UI; build-time vs runtime type checking
- Positions:
  - `slint-vs-qt--p1` — prefer Slint over QML/Qt for new Rust GUI work despite Slint's current feature gaps
    - **David Vin (Felgo)** · Source `f011133` · date 2024-07-01 · locator "so should you switch to slint" (closing section, ~23:37) — having reimplemented an existing QML demo app in Slint from scratch, he argues Slint's build-time-checked, Rust-native, easily cross-compiled model is worth the tradeoff against QML's more mature multimedia/3D/testing tooling and Qt's licensing costs, especially for embedded targets Quote: "for me it seems that the slint is the best toolkit currently for rust" [`b-sb23-f011133-c1`, team b]
- Positions seen by the extractor (`b-sb23-f011133-q1`): adopt Slint for new Rust-based GUI work because compile-time error catching, portability and escaping Qt licensing/lock-in outweigh its current feature gaps

### `sound-lifetime-erasure-in-callbacks`

**Question.** When an external callback API erases a reference's lifetime so it can be stored for later, how should the resulting unsafe surface be structured to stay sound?

- Teams: b · members (context): `b-sR04-f001749-q1` (f001749, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: unsafe; lifetimes; aliasing; FFI/callback integration
- Positions:
  - `sound-lifetime-erasure-in-callbacks--p1` — thread-local-scoped-storage-over-raw-pointer-cast
    - **ArthurBrussee** · Source `f001749` · date 2024-07-26 · locator PR #4849, comment 2024-07-26T01:00:25Z — the prior integration cast away an `&ActiveEventLoop`'s lifetime to store it for a later callback, which he judged unsound (possible aliased mutable reference, no real outlives guarantee from winit); replaced it with a thread-local holding the pointer only for the paint call's duration — still `unsafe`, but easier to reason about. Quote: "That's really not allowed! At any point there might be an aliased mutable reference, and the comment about how the lifetime outlives the callback doesnt really make sense to me - winit is free to do what it wants!" [`b-sR04-f001749-c1`, team b]
- Positions seen by the extractor (`b-sR04-f001749-q1`): thread-local-scoped-storage-over-raw-pointer-cast

### `spawn-vs-compose-futures`

**Question.** When running multiple futures concurrently, should you spawn separate tasks or compose them in place with `join!`/`select!`?

- Teams: b · members (context): `b-bk01-f000233-q4` (f000233, core, distributed, web)
- Domains: core, distributed, web
- Concepts: spawn; JoinHandle; join; select; structured concurrency
- Positions:
  - `spawn-vs-compose-futures--p1` — prefer spawn+JoinHandles for parallelism
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "Composing futures concurrently" § Alternatives / Final words — if parallelism is wanted (or not explicitly excluded), spawning tasks is usually a simpler alternative to join!/select!, being less error-prone, more general, and giving more predictable/fairer performance (each spawned task gets a fair scheduling share, unlike futures joined inside one task); spawning is traded off against being less structured, harder to reason about lifecycle and resource management. Quote: "Spawning tasks is usually less error-prone, more general, and performance is more predictable." [`b-bk01-f000233-c5`, team b]
- Positions seen by the extractor (`b-bk01-f000233-q4`): prefer spawn+JoinHandles for parallelism; join!/select! for explicit non-parallel composition

### `speculative-from-impls`

**Question.** When you can foresee wanting another blanket `From` impl for a type later, should you add related conversions now speculatively, or hold off to avoid a breaking compile error for downstream users when you do add it?

- Teams: a · members (context): `a-sa11-f004265-q2` (f004265, embedded)
- Domains: embedded
- Concepts: API stability; trait impl coherence; semver
- Positions:
  - `speculative-from-impls--p1` — avoid speculative trait impls that would break under a later addition
    - **MabezDev** · Source `f004265` · date 2026-02-19 · locator comment 2026-02-19T14:04:18Z; 2026-02-19T14:04:25Z — asks to remove a conversion because adding another `From` impl later would produce a compile error on existing code Quote: "Remove this, if we add another from impl later, we'll get a compile error on existing code." [`a-sa11-f004265-c2`, team a]
- Positions seen by the extractor (`a-sa11-f004265-q2`): don't add the impl now if adding another one later would conflict with it and break existing code

### `spi-hardware-cs-in-spibus`

**Question.** Should an SPI driver expose hardware chip-select (CS) control as part of the embedded-hal `SpiBus` trait, or restrict `SpiBus` to software/GPIO-controlled CS and handle hardware CS separately?

- Teams: a · members (context): `a-sa09-f004055-q2` (f004055, embedded)
- Domains: embedded
- Concepts: embedded-hal; ownership; API-design
- Positions:
  - `spi-hardware-cs-in-spibus--p1` — software-cs-via-spidevice
    - **jamesmunns** · Source `f004055` · date 2026-01-05 · locator comment @jamesmunns 2026-01-05T14:30:11Z — hardware chip-select complicates the embedded-hal `SpiBus`/`SpiDevice` split, so most HALs avoid it Quote: "In many other HALs, we tend to not utilize hardware chip selects, as this complicates the embedded-hal SpiBus vs SpiDevice implementations." [`a-sa09-f004055-c3`, team a]
    - **felipebalbi** · Source `f004055` · date 2026-01-07 · locator comment @felipebalbi 2026-01-07T19:47:44Z — prefers CS as ordinary GPIO `Output` pins so one bus can address as many targets as there are available GPIOs Quote: "I would rather use CS as regular Output GPIOs. This means we can talk to as many targets as we have available GPIOs for." [`a-sa09-f004055-c4`, team a]
  - `spi-hardware-cs-in-spibus--p2` — support-both-type-level-distinction
    - **bogdan-petru** · Source `f004055` · date 2026-02-05 · locator comment @bogdan-petru 2026-02-05T04:50:38Z — converges on marker types (`HardwareCs`, `NoCs`) so `SpiBus` is implemented only for the no-hardware-CS variant, while a separate constructor still exposes hardware CS for callers who want it Quote: "The SpiBus trait is now only implemented for Spi<..., NoCs>, following embedded-hal semantics where SpiBus represents exclusive bus access without CS management." [`a-sa09-f004055-c5`, team a]
- Positions seen by the extractor (`a-sa09-f004055-q2`): software-cs-via-spidevice, hardware-cs-in-spibus, support-both-type-level-distinction

### `stable-contract-api-vs-cli`

**Question.** For a Rust binary application distributed as a set of crates, which surface should be the versioned, stable contract — the published Rust library API, or the CLI/RPC surface?

- Teams: b · members (context): `b-bk03-f000267-q10` (f000267, core)
- Domains: core
- Concepts: semver; API stability scope; library vs binary
- Positions:
  - `stable-contract-api-vs-cli--p1` — rpc-cli-stable-rust-api-unstable
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Zebra versioning and releases § Deprecation practices, "Rust APIs" — the deprecation policy states that the Rust APIs of the Zebra crates are currently unstable and unsupported; the stable, versioned surface for interacting with Zebra is the zebrad commands and JSON-RPCs, not the Rust library API Quote: "The Rust APIs of the Zebra crates are currently unstable and unsupported. Use the zebrad commands or JSON-RPCs to interact with Zebra." (flag: voice-unverified) [`b-bk03-f000267-c10`, team b]
- Positions seen by the extractor (`b-bk03-f000267-q10`): rpc-cli-stable-rust-api-unstable

### `state-accessor-and-stream-split`

**Question.** Should a Rust crate's live-state accessor and its change-notification stream be one overloaded API or two separate primitives?

- Teams: a · members (context): `a-sR13-f004685-q1` (f004685, decentralized-iroh, core)
- Domains: core, decentralized-iroh
- Concepts: API design; async streams; ownership/lifetimes
- Positions:
  - `state-accessor-and-stream-split--p1` — split-into-two-primitives
    - **iroh/n0 (Friedel Ziegelmayer & Rüdiger Klaehn, post authors)** · Source `f004685` · date 2026-05-11 · locator § "Path observation API redesign" — the single `PathWatcher` primitive tried to serve both "what are the paths right now" and "tell me when paths change," so it was replaced by `Connection::paths()` (a lifetime-bound borrowed snapshot) and `Connection::path_events()` (a `'static` event stream), each answering one question Quote: "went through PathWatcher, a single primitive that tried to serve two very different consumers: code that wants \"what are the paths right now?\" and code that wants \"tell me when paths change\"" [`a-sR13-f004685-c1`, team a]
- Positions seen by the extractor (`a-sR13-f004685-q1`): split-into-two-primitives (iroh)

### `static-allocation-in-real-time`

**Question.** In resource-constrained real-time systems, should allocation be static rather than dynamic?

- Teams: a · members (context): `a-sB01-f000227-q4` (f000227, embedded)
- Domains: embedded
- Concepts: static-allocation; no-heap; panic-on-oom
- Positions:
  - `static-allocation-in-real-time--p1` — static allocation preferred over dynamic in real-time systems
    - **RTIC developers** · Source `f000227` · date undated (living doc) · locator Preface, "RTIC into the Future" — States dynamic allocation is problematic for resource-constrained real-time systems on both performance and reliability grounds (Rust panics on out-of-memory), so static allocation is the preferable approach Quote: "Thus, static allocation is the preferable approach!" [`a-sB01-f000227-c4`, team a]
- Positions seen by the extractor (`a-sB01-f000227-q4`): static allocation preferred

### `static-model-security-guarantees`

**Question.** Can a Rust-based real-time framework's compile-time static model provide stronger system-wide security guarantees (particularly integrity) than a traditional RTOS kernel, even a formally verified one?

- Teams: a · members (context): `a-sB04-f000227-q4` (f000227, embedded)
- Domains: embedded
- Concepts: static-task-resource-model; compile-time-aliasing-guarantees; kernel-security-scope
- Positions:
  - `static-model-security-guarantees--p1` — RTIC+Rust's static model extends integrity guarantees system-wide; traditional RTOS kernel security covers only the kernel
    - **RTIC developers** · Source `f000227` · date undated (living doc, v2.x) · locator "4. RTIC vs. the world", "Comparison regarding safety and security" — Argues that even a formally verified RTOS kernel like seL4 only claims integrity/confidentiality/availability for the kernel itself, not the whole system, especially once dynamic allocation is involved; RTIC's declarative static task/resource model plus Rust's compile-time aliasing, mutability and lifetime guarantees propagate integrity properties across the whole system instead Quote: "RTIC on the other hand holds your back. The declarative system wide model gives you a static set of tasks and resources, with precise control over what data is shared and between which parties." [`a-sB04-f000227-c4`, team a]
- Positions seen by the extractor (`a-sB04-f000227-q4`): RTIC+Rust's static model extends integrity guarantees system-wide; traditional RTOS kernel security (even seL4) covers only the kernel itself, not the whole system

### `static-verification-no-panic-mechanism`

**Question.** How should a Rust project statically verify a property like "this function never panics" or "this function never calls unvalidated code" across a codebase: clippy lints, a new effect-type system, a link-time hack, a cfg-forked standard library, or a custom compiler driver?

- Teams: b · members (context): `b-sR12-f005169-q1` (f005169, embedded, core)
- Domains: core, embedded
- Concepts: static verification; panics; effect systems; monomorphization; custom lints; safety-critical certification
- Positions:
  - `static-verification-no-panic-mechanism--p1` — custom-compiler-driver-post-mono
    - **Jynn (Ferrous Systems, Ferrocene team)** · Source `f005169` · date 2026-04-08 · locator section "What have we learned?" (whole post walks the alternatives it rejects: clippy lints, effect-type systems, link-time no_panic hack, cfg-forked std) — for certifying that validated `core` functions only call other validated functions (generalizable to "never panics"), clippy lints don't recurse into dependencies and only cover hard-coded library types; an effect-type system would require a new language; a link-time hack is optimization-dependent, has no async support, breaks under `panic = "abort"`/no_std, and is unsafe to use in library crates; cfg-forking the standard library affects every consumer and breaks tooling. A custom rustc driver with a post-monomorphization MIR pass was the most accurate approach and is what Ferrocene now ships and certifies against Quote: "For Ferrocene, the most accurate approach was to write a custom rustc driver which uses a post-monomorphization pass to detect all resolved function calls." [`b-sR12-f005169-c1`, team b]
- Positions seen by the extractor (`b-sR12-f005169-q1`): custom-compiler-driver-post-mono

### `std-mutex-vs-async-mutex`

**Question.** In async code, should locking default to a std (sync) `Mutex` or an async `Mutex`?

- Teams: b · members (context): `b-bk01-f000233-q7` (f000233, core, distributed)
- Domains: core, distributed
- Concepts: async Mutex; std::sync::Mutex; await points
- Positions:
  - `std-mutex-vs-async-mutex--p1` — prefer std Mutex where possible
    - **async-book (rust-lang.github.io, Rust Async Working Group)** · Source `f000233` · date 2026-09-27 · locator chapter "Channels, locking, and synchronization" § Locks — recommends using `std::Mutex` if you can, reserving the async `Mutex` for cases where the lock must be held across an `.await` point or protects an IO resource, because the async version is more expensive precisely because it supports being held across awaits. Quote: "use std::Mutex if you can" [`b-bk01-f000233-c8`, team b]
- Positions seen by the extractor (`b-bk01-f000233-q7`): prefer std Mutex where possible, async Mutex only across await points or for IO resources

### `std-naming-convention-imperfect-fit`

**Question.** should a crate's naming for a raw-pointer-plus-length accessor follow std's `raw_parts`/`from_raw_parts` convention even where the analogy is imperfect (no matching `into_raw_parts` exists here), or invent its own name when the fit is inexact?

- Teams: b · members (context): `b-sR05-f002326-q1` (f002326, embedded)
- Domains: embedded
- Concepts: none given
- Positions:
  - `std-naming-convention-imperfect-fit--p1` — reuse the `raw_parts`-style name anyway; std's convention doesn't have to apply exactly to a non-std crate.
    - **bugadani (esp-hal maintainer)** · Source `f002326` · date 2024-11-23 · locator esp-rs/esp-hal#2546, comment 2024-11-23T13:48:41Z. · L1903-L1905. — reuse the `raw_parts`-style name anyway; std's convention doesn't have to apply exactly to a non-std crate. Quote: "`raw_parts` works, I decided against it because there is no 'into_raw_parts', just 'from_raw_parts'. But we are also not the standard library, so I guess it's okay if the pattern doesn't apply to us." [`b-sR05-f002326-c1`, team b]
- Positions seen by the extractor (`b-sR05-f002326-q1`): reuse the `raw_parts`-style name anyway; std's convention doesn't have to apply  (bugadani (esp-hal maintainer))

### `synthetic-canary-vs-tracing`

**Question.** When a system's design forbids observing real user traffic (privacy/anonymity by design), should you build synthetic "canary" traffic that exercises the real system on a schedule, rather than instrumenting/tracing real messages for observability?

- Teams: b · members (context): `b-sb24-f011295-q3` (f011295, distributed, web)
- Domains: distributed, web
- Concepts: message canary; synthetic monitoring; tracing constraints under anonymity guarantees
- Positions:
  - `synthetic-canary-vs-tracing--p1` — synthetic-canary-over-tracing-real-traffic
    - **Zeke Hunter Green** · Source `f011295` · date 2025-10-03 · locator [30:28]-[32:28] — because the protocol requires that no timing information about real source messages ever leaves the on-premises cover node (to preserve anonymity), they cannot trace real messages; instead they run a "message canary" that sends real encrypted messages through the live system once an hour and measures delivery time, alarming if delivery exceeds 3 hours Quote: "we don't want any information on the timing of real source messages to go to any third parties... that means we can't uh add any tracing of real messages going through the system." [`b-sb24-f011295-c3`, team b]
- Positions seen by the extractor (`b-sb24-f011295-q3`): synthetic-canary-over-tracing-real-traffic (Zeke Hunter Green)

### `tail-expression-vs-explicit-return`

**Question.** Should a Rust block or function yield its value through an implicit tail expression (semicolon-less last line), or does that rule hurt readability enough to favour an explicit marker such as `return`?

- Teams: b · members (context): `b-sT02-f000576-q1` (f000576, core)
- Domains: core
- Concepts: tail expression / implicit last-expression value; semicolon significance; explicit `return`; expression-oriented blocks
- Positions:
  - `tail-expression-vs-explicit-return--p1` — tail-expression-hurts-readability
    - **andrews05** · Source `f000576` · date 2023-11-17 · locator post @andrews05 2023-11-17T03:44:40Z (quotes their own earlier SE-0380 review comment, whose date is not given in this source) — Says they are strongly opposed to any bare/last-expression rule on readability grounds. Draws on their Rust work: the rule "seriously hurts readability" for function returns and `if` expressions alike, most of all when the block is long and the last expression sits far from the assignment. Quote: "as someone who has been working with Rust a lot lately. I am really not a fan of the "last expression" rule" (flag: voice-unverified) [`b-sT02-f000576-c1`, team b]
  - `tail-expression-vs-explicit-return--p2` — tail-expression-reads-better
    - **Nobody1707** · Source `f000576` · date 2023-12-01 · locator post @Nobody1707 2023-12-01T17:02:06Z — Answers a claim that languages with last-expression evaluation are worse for it. Says their own experience runs the other way: Rust's implicit return of the last expression is much easier to read than return statements everywhere. Quote: "I find implicit return of the last expression in Rust much easier to read than if there were return statements everywhere." (flag: voice-unverified) [`b-sT02-f000576-c2`, team b]
- Positions seen by the extractor (`b-sT02-f000576-q1`): tail-expression-reads-better (Nobody1707, stackotter), tail-expression-hurts-readability (andrews05)

### `target-tier-without-ci`

**Question.** When free CI for a platform disappears, should the Rust project keep the target at Tier 1 by other means, or demote it (here x86_64-apple-darwin to Tier 2 with host tools) and accept less testing?

- Teams: a · members (context): `a-sT12-f009704-q1` (f009704, core, desktop-cli-ui)
- Domains: core, desktop-cli-ui
- Concepts: target tier policy; CI; macOS x86_64; GitHub runners; rustup distribution
- Positions:
  - `target-tier-without-ci--p1` — demote to Tier 2 with host tools
    - **Jake Goulding, for the Rust Infrastructure team** · Source `f009704` · date 2025-08-19 · locator § "Background", § "What changes?", § "Future" — Apple is ending x86_64 support, and GitHub is ending free macOS x86_64 runners for public repositories. The tier policy requires Tier 1 targets to run CI tests, so from 1.90.0 the target becomes Tier 2 with host tools; builds are still distributed, but the target will likely accumulate bugs faster and may be demoted further if it causes problems Quote: "Since the target tier policy requires that Tier 1 platforms must run tests in CI, the x86_64-apple-darwin target must be demoted to Tier 2." (flag: voice-unverified (Rust connection in source: writes for the Rust Infrastructure team on the Rust Blog)) [`a-sT12-f009704-c1`, team a]
- Positions seen by the extractor (`a-sT12-f009704-q1`): demote to Tier 2 with host tools; keep Tier 1 (the alternative the tier policy rules out without CI tests)

### `teach-rust-in-curricula`

**Question.** should introductory CS/software-engineering curricula teach a systems language like Rust directly (to force understanding of memory, concurrency, ownership), or is teaching via high-level frameworks and abstractions sufficient?

- Teams: a · members (context): `a-sa26-f011443-q1` (f011443, other)
- Domains: other
- Concepts: education; ownership; memory; concurrency
- Positions:
  - `teach-rust-in-curricula--p1` — teach Rust directly to force systems understanding
    - **Mordecai Emmanuel Etukudo** · Source `f011443` · date 2026-06-11 · locator ~01:10-02:10 — modern software education over-focuses on frameworks and abstractions and under-teaches how systems actually work (memory, concurrency, performance, tradeoffs); learning Rust forces students to confront ownership, memory, and error handling directly, concepts other languages abstract away Quote: "The modern software education... focus more on teaching people about framework and a lot of abstractions... it's not bad to use frameworks... but it's nice to understand what is going on behind the wood" [`a-sa26-f011443-c1`, team a]
- Positions seen by the extractor (`a-sa26-f011443-q1`): teach-Rust-directly-in-the-academy (Mordecai Etukudo)

### `threads-vs-simd-for-batch-work`

**Question.** When batch-hashing many small blobs (or a similar compute-bound batch workload), should you use thread-level parallelism (rayon), instruction-level parallelism (SIMD), or both, and when does each apply?

- Teams: b · members (context): `b-sR08-f003702-q1` (f003702, decentralized-iroh, ml)
- Domains: decentralized-iroh, ml
- Concepts: parallelism (SIMD vs. threads); rayon; BLAKE3; compute-bound batching
- Positions:
  - `threads-vs-simd-for-batch-work--p1` — simd-for-small-batches-combine-with-threads-for-large-batches
    - **Rüdiger Klaehn** · Source `f003702` · date 2025-10-15 · locator § "Combining instruction level parallelism and thread level parallelism" — SIMD alone is a good choice for a small batch — decent speedup, stays on one core, doesn't disturb the rest of the program — but for a large batch where the whole machine is available, combining SIMD with rayon's thread-level parallelism gives peak throughput (measured 17x over sequential, 2.1x over rayon alone). Quote: "Instruction level parallelism alone is frequently a good choice if you have a small batch of blobs to hash. You get a decent speed up but only use one CPU, and don't affect other parts of your program... For peak performance we can combine instruction level parallelism and thread level parallelism." [`b-sR08-f003702-c1`, team b]
- Positions seen by the extractor (`b-sR08-f003702-q1`): simd-for-small-batches-combine-with-threads-for-large-batches

### `tiered-checked-unchecked-apis`

**Question.** Should a high-performance Rust client API expose multiple tiers of the same builder operation — an unchecked/positional fast path alongside a checked/named-field safe path — rather than one safe-by-default interface?

- Teams: a · members (context): `a-sR16-f012642-q1` (f012642, distributed, core)
- Domains: core, distributed
- Concepts: API design; ergonomics vs. performance; unchecked/checked accessors
- Positions:
  - `tiered-checked-unchecked-apis--p1` — offer-tiered-apis
    - **Jiachun Feng (Co-Founder, Greptime)** · Source `f012642` · date 2025-07-30 · locator § "Three Insert Approaches" — the bulk-stream row builder deliberately exposes three ways to build the same row — a positional "Fast API" for best performance, a "Safe API" that validates field names, and an "Indexed API" balancing the two — so callers pick their own safety/performance tradeoff rather than the crate picking one for them Quote: "Fast API: Best performance, positional values / Safe API: Validates field names / Indexed API: Uses index for balance of safety and speed" [`a-sR16-f012642-c1`, team a]
- Positions seen by the extractor (`a-sR16-f012642-q1`): offer-tiered-apis (Greptime)

### `timer-instant-overflow-panic`

**Question.** When a scheduled timer/interval's next wake time would overflow the maximum representable `Instant`, should the runtime panic or silently never become ready again?

- Teams: a · members (context): `a-sa19-f009196-q2` (f009196, distributed, cloud-workers, core)
- Domains: cloud-workers, core, distributed
- Concepts: time APIs; panics vs graceful degradation; async runtimes (Tokio Interval)
- Positions:
  - `timer-instant-overflow-panic--p1` — panic-on-overflow
    - **kevincox** · Source `f009196` · date 2024-08-17 · locator reply, 2024-08-17T19:19:10.352Z — Argues the best behaviour is to keep a sleeping future alive but never fire it early, panicking only in the extremely unlikely case that Instant::now itself reaches Instant::MAX, since no reasonable behaviour exists past that point. Quote: "Panic if Instant::now reaches Instant::MAX... you never run a timer too early but you also don't panic upfront." [`a-sa19-f009196-c5`, team a]
  - `timer-instant-overflow-panic--p2` — never-ready-without-panic
    - **bjorn3** · Source `f009196` · date 2024-08-17 · locator reply, 2024-08-17T18:40:14.074Z — Criticizes Tokio's existing `far_future()` hack (used in `Interval::poll_tick`) as unnecessary; when a period is too large or the clock is nearly exhausted, the correct behaviour is to never register the future as ready again, not to wait based on a MAX-derived time that undershoots. Quote: "The only options are to panic or have the future never be ready ever again." [`a-sa19-f009196-c6`, team a]
- Positions seen by the extractor (`a-sa19-f009196-q2`): panic-on-overflow; never-ready-without-panic

### `tokio-axum-vs-nginx-performance`

**Question.** Is async Rust (Tokio-based web stacks) production-competitive with mature C-based servers like nginx "out of the box," or does the higher-level framework layer (e.g. Axum) add meaningful overhead that needs bypassing for performance?

- Teams: a · members (context): `a-saL1-f005360-q3` (f005360, web, cloud-workers, core)
- Domains: cloud-workers, core, web
- Concepts: async runtimes (Tokio); web frameworks (Axum/Hyper/Tower); reverse proxies; benchmark-driven framework choice
- Positions:
  - `tokio-axum-vs-nginx-performance--p1` — nginx's tuning advantage isn't matched by async Rust out of the box
    - **yawaramin** · Source `f005360` · date 2024-10-13 · locator comment 2024-10-13T05:36:31 — responds to a claim that async Rust should be competitive with nginx by pointing out nginx is highly-tuned async C++, while the compared Rust server is untuned "out of the box" Quote: "Difficult to see how that could be true since Nginx is highly-tuned async C++ and the async Rust is as is 'out of the box'." [`a-sa14-f005360-c5`, team a]
  - `tokio-axum-vs-nginx-performance--p2` — tokio-competitive-out-of-the-box
    - **kornel** · Source `f005360` · date 2024-10-13 · locator reply, 2024-10-13T08:05:40-05:00 — Points to Cloudflare's production replacement of nginx with the Tokio-based Pingora proxy as evidence Tokio is fast out of the box and Rust's async was designed from the ground up for low overhead. Quote: "Cloudflare has replaced nginx with tokio-based Pingora. Tokio is pretty fast out of the box, and Rust's async has been designed from the ground up to be very low overhead." [`a-saL1-f005360-c7`, team a]
  - `tokio-axum-vs-nginx-performance--p3` — axum-framework-overhead-hurts-raw-performance
    - **mattya** · Source `f005360` · date 2024-10-13 · locator reply, 2024-10-13T08:47:00-05:00 — Distinguishes Tokio/Hyper (both very fast) from Axum, which adds its own routing/extractor overhead on top; recommends using Hyper and Tower directly when complex path routing isn't needed. Quote: "Tokio and Hyper are both very fast, but this is using Axum which adds its own overhead... If you don't need complex path routing and 'extractors'... it's probably better to use Hyper and Tower directly." [`a-saL1-f005360-c8`, team a]
    - **kornel** · Source `f005360` · date 2024-10-13 · locator reply, 2024-10-13T09:11:28-05:00 — Expresses surprise/disappointment at Axum's overhead, noting Actix-Web previously topped benchmarks while also providing routing and extractors, so he hadn't expected Axum to differ much. Quote: "Oh, that's disappointing. Actix-Web used to be a benchmark-topping framework while having routing and extractors, so I didn't expect Axum to differ much." [`a-saL1-f005360-c9`, team a]
- Positions seen by the extractor (`a-saL1-f005360-q3`): tokio-competitive-out-of-the-box; axum-framework-overhead-hurts-raw-performance

### `totokens-intermediate-tokenstream`

**Question.** In a `ToTokens` impl for a proc-macro AST enum, should each arm call `to_tokens` on the matched variant directly, or is it acceptable to build an intermediate `TokenStream` and feed it into the outer one?

- Teams: a · members (context): `a-sR01-f000538-q1` (f000538, web, core)
- Domains: core, web
- Concepts: proc-macro; `ToTokens`; `TokenStream`
- Positions:
  - `totokens-intermediate-tokenstream--p1` — avoid building a temporary `TokenStream` in a `ToTokens` impl; match on the enum and call `to_tokens` on the matched arm directly
    - **its-the-shrimp** · Source `f000538` · date 2025-05-04 · locator PR #3509, comment 2025-05-04T12:20:47Z — suggests rewriting the `impl ToTokens` so each match arm calls `to_tokens` on its inner value directly, rather than constructing a `TokenStream` from one variant and feeding it into another. Quote: "to avoid allocating a temporary TokenStream just to feed it into another TokenStream" [`a-sR01-f000538-c1`, team a]
- Positions seen by the extractor (`a-sR01-f000538-q1`): "match each variant and call `to_tokens` directly, avoid the intermediate allocation" (its-the-shrimp)

### `trace-context-propagation-mechanism`

**Question.** For propagating distributed-trace context (W3C trace-context HTTP headers) across a network boundary without modifying application code, should you use library interposition (`LD_PRELOAD` hijacking libcurl/libssl calls) or an eBPF-based mechanism (kernel-level header injection)?

- Teams: b · members (context): `b-sb24-f011306-q3` (f011306, distributed, core)
- Domains: core, distributed
- Concepts: W3C trace context; LD_PRELOAD; BPF_PROBE_WRITE_USER; BPF arena; level-4 vs level-7 context propagation
- Positions:
  - `trace-context-propagation-mechanism--p1` — no-fully-good-solution-yet
    - **Lalit Basin** · Source `f011306` · date 2025-10-03 · locator [32:45]-[36:51] — injecting a new HTTP header for trace-context propagation from eBPF has no clean solution today — the kernel function that could write into user-space memory (`bpf_probe_write_user`) was locked down in August 2021 over security concerns, and its replacement (BPF arena, shared memory) zero-initializes on load and can crash the user-space program if headers were already allocated there; the traditional non-eBPF alternative, library interposition via `LD_PRELOAD` on libcurl/libssl, works well but becomes messy when those libraries are statically linked into the application Quote: "there is no one all good solution uh as of now for context propagation in the dist distributed scenarios." [`b-sb24-f011306-c3`, team b]
- Positions seen by the extractor (`b-sb24-f011306-q3`): no-fully-good-solution-yet (Lalit Basin: library interposition "works great" for dynamically-linked binaries but is messy for statically-linked ones; eBPF's own kernel-write primitive was locked down in Aug 2021 for security reasons and its replacement zero-initializes memory on load, risking crashes)

### `tracing-crate-vs-otel-api`

**Question.** For distributed tracing in Rust, should the ecosystem standardize on the widely-adopted `tracing` crate (Tokio's tracing API), on the OpenTelemetry-spec-compliant tracing API, or keep maintaining both with improved interop?

- Teams: b · members (context): `b-sb24-f011306-q1` (f011306, core, distributed)
- Domains: core, distributed
- Concepts: tracing crate; OpenTelemetry tracing API; distributed tracing spec compliance; ecosystem interop
- Positions:
  - `tracing-crate-vs-otel-api--p1` — keep-both-with-better-interop-for-now
    - **Lalit Basin** · Source `f011306` · date 2025-10-03 · locator [06:14]-[08:14] — the Tokio `tracing` crate is widely adopted but not fully suited to distributed tracing, while the OpenTelemetry tracing API is spec-compliant but far less adopted; the community has debated dropping one, but the current practical (and still unstable) path is to keep both and improve interop between them Quote: "the community has been debating how how to really interrop with both these APIs whether we should drop one of them or whether we should continue using both of them... currently the state is that uh both practical path is to keep both of them active and running and provide an improved interoperability across both of them." [`b-sb24-f011306-c1`, team b]
- Positions seen by the extractor (`b-sb24-f011306-q1`): keep-both-with-better-interop-for-now (Lalit Basin, OpenTelemetry Rust/C++ maintainer)

### `tracing-vs-log-for-otel`

**Question.** For a new Rust application adopting OpenTelemetry, should the logging facade be the span-native `tracing` crate, or a conventional logging crate bridged into OpenTelemetry later?

- Teams: a · members (context): `a-sa29-f012940-q1` (f012940, web, distributed, cloud-workers, core)
- Domains: cloud-workers, core, distributed, web
- Concepts: tracing crate; log crate; OTel bridge libraries; spans; structured logging
- Positions:
  - `tracing-vs-log-for-otel--p1` — use the `tracing` crate, not a conventional logging crate, as the logging facade for a new Rust app that will adopt OpenTelemetry
    - **Dhruv Ahuja** · Source `f012940` · date 2026-03-11 · locator section "State of Logging and OpenTelemetry" — notes the OpenTelemetry Rust project bridges existing loggers (rather than mandating its own API) but recommends `tracing` for new applications because its Span concept aligns with OTel spans; the demo app follows this, using `tracing` throughout instead of a plain logging crate Quote: "the project recommends using tracing for new Rust applications" [`a-sa29-f012940-c1`, team a]
- Positions seen by the extractor (`a-sa29-f012940-q1`): tracing-first from the start, per the OpenTelemetry Rust project's own stated recommendation (Dhruv Ahuja) vs. the described status-quo pattern of scaffolding with "the language's preferred logging libraries" first and retrofitting OTel via bridge libraries later (described in-source as the general, unnamed default)

### `trait-api-forced-arc-self`

**Question.** should a public trait's methods require callers to wrap `self` in `Arc` (shared ownership baked into the API), or accept a plain reference/generic `Self` and leave ownership to the caller?

- Teams: b · members (context): `b-sR05-f002453-q2` (f002453, decentralized-iroh)
- Domains: decentralized-iroh
- Concepts: none given
- Positions:
  - `trait-api-forced-arc-self--p1` — drop the forced `Arc` requirement from `ProtocolHandler` for a more flexible structure.
    - **dignifiedquire** · Source `f002453` · date 2024-12-17 · locator iroh.computer/blog/iroh-0-30-0-slimming-down, "Simpler ProtocolHandler API" section. · L2098-L2100. — drop the forced `Arc` requirement from `ProtocolHandler` for a more flexible structure. Quote: "Previously the `ProtocolHandler` trait required using explicit Arcs, but this is no longer required, allowing for a more flexible structure in defining protocols." [`b-sR05-f002453-c2`, team b]
- Positions seen by the extractor (`b-sR05-f002453-q2`): drop the forced `Arc` requirement from `ProtocolHandler` for a more flexible str (dignifiedquire)

### `trait-default-methods-vs-major-bump`

**Question.** When adding new methods to a public trait, should you give them default implementations to avoid a breaking change, or bump the major version?

- Teams: b · members (context): `b-sR08-f003540-q1` (f003540, other)
- Domains: other
- Concepts: trait evolution; semver; default trait methods; API stability
- Positions:
  - `trait-default-methods-vs-major-bump--p1` — default-impls-to-avoid-breaking-change
    - **milenkovicm** · Source `f003540` · date 2025-09-19 · locator issue comment, 2025-09-19T15:47:59Z — added default implementations for two new `FunctionRegistry` trait methods so they would not trigger a backward-incompatible change in the 50.1.0 minor release, planning to make them required (unimplemented) only in the next major version. Quote: "I have provided default implementation for those two methods for now, so they do not trigger backward incompatible change. will revert them back to unmplemented methods for df 51 release" [`b-sR08-f003540-c1`, team b]
    - **alamb** · Source `f003540` · date 2025-09-18 · locator issue comment, 2025-09-18T18:04:21Z — endorses adding the two new trait methods and shipping them in the 50.1.0 minor release rather than waiting for a major version bump. Quote: "I think adding two new methods and releasing `50.1.0` sounds good to me" [`b-sR08-f003540-c2`, team b]
- Positions seen by the extractor (`b-sR08-f003540-q1`): default-impls-to-avoid-breaking-change

### `trait-error-open-custom-variant`

**Question.** Should a public trait's associated error type be a closed, fully-enumerated set of variants, or include an open "custom"/user-extension variant so third-party implementors can propagate their own errors?

- Teams: a · members (context): `a-sa14-f005149-q3` (f005149, core)
- Domains: core
- Concepts: extensible error types; public trait design
- Positions:
  - `trait-error-open-custom-variant--p1` — give public-trait errors an open Custom/User variant
    - **dig, b5, and ramfox (iroh team)** · Source `f005149` · date 2025-08-22 · locator § Concrete-error writing guidelines / Errors for public traits should contain a Custom variant — for traits users can implement themselves (e.g. `Discovery`), the associated error type includes a `User` variant plus `from_err`/`from_err_box` helpers so implementors can propagate their own errors rather than being boxed into the crate's own failure modes Quote: "for traits that folks working with iroh can implement themselves, we needed to ensure that they could use the errors associated with that trait for their own purposes" [`a-sa14-f005149-c3`, team a]
- Positions seen by the extractor (`a-sa14-f005149-q3`): include a `Custom`/`User` variant (with helper constructors) on errors tied to a public, implementable trait, so implementors aren't limited to the crate's own enumerated failure modes

### `trait-impl-boilerplate-mechanism`

**Question.** How should Rust reduce boilerplate for simple trait implementations — new dedicated impl syntax, compiler-inferred associated types, or ecosystem derive-macro crates?

- Teams: a · members (context): `a-sa19-f009292-q2` (f009292, core)
- Domains: core
- Concepts: trait implementation ergonomics; associated types; macros; derive_more
- Positions:
  - `trait-impl-boilerplate-mechanism--p1` — new-impl-shorthand-syntax
    - **zackw** · Source `f009292` · date 2025-09-08 · locator reply, 2025-09-08T15:59:48.016Z — Proposes syntactic sugar such as `impl Display (self, f) for Type { ... }` for traits with exactly one required method, removing an indentation level and the need to look up the method's exact signature, beyond what derive alone offers. Quote: "I wonder if we could come up with a generalization of this macro that would be suitable as official syntactic sugar." [`a-sa19-f009292-c7`, team a]
  - `trait-impl-boilerplate-mechanism--p2` — infer-associated-types
    - **scottmcm** · Source `f009292` · date 2025-09-08 · locator reply, 2025-09-08T23:27:35.279Z — Rather than new impl syntax, wants the compiler to infer associated types (e.g. `Iterator::Item`) from the method body, which would simplify implementing Add, Sub, IntoIterator and Deref without adding new surface syntax. Quote: "there's really no need... for me to have to write the type Item = i32; because it's the only possible thing given that next." [`a-sa19-f009292-c8`, team a]
- Positions seen by the extractor (`a-sa19-f009292-q2`): new-impl-shorthand-syntax; infer-associated-types; ecosystem-crates-suffice

### `traits-as-inheritance-substitute`

**Question.** Is Rust's trait-based supertrait/subtrait polymorphism (no class inheritance) an adequate, ergonomic substitute for OOP-style inheritance, or does the required generic/trait-bound plumbing make it more verbose and confusing than an inheritance-based language?

- Teams: a · members (context): `a-sR16-f012428-q1` (f012428, core, desktop-cli-ui)
- Domains: core, desktop-cli-ui
- Concepts: traits; generics; subtyping/variance; static vs. dynamic dispatch
- Positions:
  - `traits-as-inheritance-substitute--p1` — adequate-but-more-verbose
    - **Nas (CEO/founder Rebel, author developerlife.com, maintainer of Rebel's Dewey crates)** · Source `f012428` · date 2025-03-26 · locator video ~[34:17]-[35:17] — modeling an OOP-style view/component hierarchy in Rust via supertrait/subtrait relationships (rather than inheritance) works, but doing it generically over the inner-storage type is a lot more work and, in his words, more verbose and confusing than the equivalent in Kotlin, Java or TypeScript Quote: "arguably it's more verbose and somewhat confusing especially if you're coming from something like cotlin or java or typescript" [`a-sR16-f012428-c1`, team a]
- Positions seen by the extractor (`a-sR16-f012428-q1`): adequate-but-more-verbose (Nas)

### `typed-response-struct-vs-untyped-value`

**Question.** Should a Rust service handler return a typed, `serde::Serialize` response struct or an untyped `serde_json::Value`?

- Teams: a · members (context): `a-sT11-f007659-q3` (f007659, cloud-workers, web, core)
- Domains: cloud-workers, core, web
- Concepts: serde; strong typing; JSON; handler signatures
- Positions:
  - `typed-response-struct-vs-untyped-value--p1` — typed response struct
    - **maahl (maahl.net)** · Source `f007659` · date 2023-11-05 · locator § "A more structured response" — replaces untyped JSON output with a `Serialize` struct so the compiler validates the response shape Quote: "We can, however, leverage Rust's strong typing to do the work for us." (flag: voice-unverified Not logged: choosing arm64 over x86_64 for AWS cost, and building artifacts outside Terraform. Neither is a Rust decision.) [`a-sT11-f007659-c3`, team a]
- Positions seen by the extractor (`a-sT11-f007659-q3`): typed response struct; untyped Value

### `typestate-crypto-keys`

**Question.** For security-critical code handling cryptographic keys, should key roles and verification status be encoded as distinct types checked at compile time (the typestate pattern), rather than checked with runtime assertions?

- Teams: b · members (context): `b-sb24-f011295-q2` (f011295, core)
- Domains: core
- Concepts: typestate pattern; newtype pattern; marker traits; compile-time misuse resistance
- Positions:
  - `typestate-crypto-keys--p1` — yes-use-typestate-for-keys
    - **Sam Cutter** · Source `f011295` · date 2025-10-03 · locator [17:10]-[21:12] — cryptographic keys are given a `Role` marker type and a verified/unverified type-state, so that e.g. passing a cover-node provisioning key where a journalist-provisioning key is required fails to compile, and an unverified key cannot be used for cryptographic operations until explicitly checked Quote: "Types give us superpowers. They allow us to encode the rules of our system in a way that can be checked compile time, helping prevent mistakes." [`b-sb24-f011295-c2`, team b]
- Positions seen by the extractor (`b-sb24-f011295-q2`): yes-use-typestate-for-keys (Sam Cutter, citing Cliff Biffle's typestate blog post)

### `typestate-generic-vs-separate-types`

**Question.** Should a Rust API express protocol states as one generic type with a typestate parameter (`Connection<T>`), or as separate concrete types per state?

- Teams: a · members (context): `a-sT08-f004169-q1` (f004169, core, decentralized-iroh)
- Domains: core, decentralized-iroh
- Concepts: typestate; generics; API design; code duplication; 0-RTT
- Positions:
  - `typestate-generic-vs-separate-types--p1` — unified-generic-typestate
    - **ramfox** · Source `f004169` · date 2026-01-27 · locator § "0-RTT and the Connection API changes" — separate `OutgoingZeroRttConnection` and `IncomingZeroRttConnection` structs duplicated the whole connection API and stopped 0-RTT connections sharing code paths; a single `Connection<T>` with a state parameter restores that flexibility and de-duplicates the code, with state-specific signatures only where authentication differs Quote: "we've de-duplicated a bunch of code that was the same over the three different variaties of connections" (flag: voice-unverified — Rust connection in the source: author of the iroh release post, "our implementation".) [`a-sT08-f004169-c1`, team a]
- Positions seen by the extractor (`a-sT08-f004169-q1`): unified-generic-typestate (replacing separate-state-structs)

### `ui-async-data-cache-vs-component`

**Question.** When a UI component needs asynchronously-fetched data to render, should that data live in a cache on a shared owner object (populated by a hover/eager prefetch, read synchronously at render), or should the component itself own the async fetch and render a loading state until it resolves?

- Teams: a · members (context): `a-sa13-f004772-q1` (f004772, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: state-ownership; async-data-fetching; API-design
- Positions:
  - `ui-async-data-cache-vs-component--p1` — component-owns-async-lifecycle
    - **SomeoneToIgnore** · Source `f004772` · date 2026-08-06 · locator comment @SomeoneToIgnore 2026-08-06T16:47:14Z — argues the hand-rolled outline cache, its hover-triggered prefetch, and its version-keyed invalidation are accidental complexity that exists only because the popover builder is synchronous; the fix is to let the menu entity spawn its own async fetch and render a loading state, "how every picker in Zed works" and how the PR's own path dropdown already behaves Quote: "let the menu entity fetch its own data asynchronously... That is how every picker in Zed works." [`a-sa13-f004772-c1`, team a]
    - **ysalitrynskyi** · Source `f004772` · date 2026-08-07 · locator comment @ysalitrynskyi 2026-08-07T17:45:21Z — reworked along the reviewer's architecture note rather than point-fixing; one async menu entity now fetches its own data per step, eliminating the cache, prefetch, and re-anchoring flag "by construction, not patched" Quote: "One async menu entity now serves both listings: fetches its own data (buffer_outline_items / expand_entry per step), no outline cache, no prefetch, no re-anchoring flag." [`a-sa13-f004772-c2`, team a]
- Positions seen by the extractor (`a-sa13-f004772-q1`): component-owns-async-lifecycle, cache-on-shared-owner

### `ui-dsl-vs-plain-rust`

**Question.** Should a Rust GUI framework define UI structure through a bespoke DSL with dedicated tooling (Slint's own language, Makepad's `live_design!` macro), or should it stick to plain Rust code with no macros/DSL (egui's immediate-mode API)?

- Teams: b · members (context): `b-sb21-f008390-q2` (f008390, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: DSL-driven UI; macro-driven UI; immediate mode API
- Positions:
  - `ui-dsl-vs-plain-rust--p1` — value-depends-on-priorities
    - **boringcactus (Melody)** · Source `f008390` · date 2025-04-16 · locator § "Conclusion" — recommends egui to readers who want zero DSL/macros and plain Rust, and Slint to readers who want a DSL with serious dev-tooling investment (better error-message ceiling since it's a standalone language, not just macros); does not pick an overall winner between the two approaches Quote: "If you want to avoid DSLs and macros and write only regular Rust, egui offers that... If you like DSL-driven UIs that are putting serious effort into developer tooling, Slint might be for you." [`b-sb21-f008390-c2`, team b]
- Positions seen by the extractor (`b-sb21-f008390-q2`): value-depends-on-priorities (boringcactus / Melody: tooling-and-error-messages favor a DSL like Slint; avoiding DSLs/macros entirely favors egui)

### `ui-state-scoped-lifetimes-vs-runtime-handles`

**Question.** Should a Rust UI/reactive framework model component state with borrow-checker-scoped lifetimes tied to the component (arena/bump allocation: zero-clone access in event handlers, but confusing lifetime errors and incompatible with `'static` futures), or with a runtime-tracked `Copy` handle backed by generational/GC-like reclamation (uniform across closures, futures and threads, at the cost of adding a small runtime-tracking layer)?

- Teams: b · members (context): `b-sb17-f005144-q1` (f005144, frontend)
- Domains: frontend
- Concepts: component state model; arena/bump lifetimes; `Copy` handles; generational indices; futures `'static` bound
- Positions:
  - `ui-state-scoped-lifetimes-vs-runtime-handles--p1` — copy-runtime-tracked-state
    - **Jonathan Kelley** · Source `f005144` · date 2024-03-21 · locator article body, "Goodbye scopes and lifetimes!" / "Copy state" sections — removes the `'bump`-lifetime scope model because it doesn't work for `'static` futures and produces confusing lifetime errors, replacing it with `Copy` signals backed by a generational-box allocator, describing the result as a lightweight GC bolted onto Rust Quote: "Dioxus 0.5 fixes this issue by first removing scopes and the 'bump lifetime and then introducing a new Copy state management solution called signals... With Copy state, we've essentially bolted on a light form of garbage collection into Rust that uses component lifecycles as the triggers for dropping state." [`b-sb17-f005144-c1`, team b]
- Positions seen by the extractor (`b-sb17-f005144-q1`): copy-runtime-tracked-state (Jonathan Kelley, Dioxus 0.5); scoped-bump-lifetime-state is named as the prior (0.1-0.4) design this Claim replaces, but is not independently quoted at its own date in this source

### `uniffi-packaging-xcode-vs-script`

**Question.** When packaging a Rust core library for Apple platforms (iOS) via UniFFI, should the FFI-binding and packaging steps run as an Xcode build phase or as an external script/CI pipeline outside Xcode?

- Teams: a · members (context): `a-sa27-f012237-q1` (f012237, swift-interop)
- Domains: swift-interop
- Concepts: UniFFI; Swift Package Manager binary targets; Xcode build phases; cross-compilation
- Positions:
  - `uniffi-packaging-xcode-vs-script--p1` — run Rust-to-Swift FFI packaging as an external shell-script/CI pipeline, not as an Xcode build phase
    - **Ian Wagner** · Source `f012237` · date 2024-12-04 · locator section "Generating the FFI Bindings", paragraph starting "NOTE: It is possible to integrate these steps into Xcode." — it is possible to wire UniFFI's binding generation into an Xcode build phase, but Stadia Maps rejected that given the difficulty and the overall flakiness of the Xcode build process, choosing a plain shell script invoked manually/by CI instead, at the cost of needing a manual rebuild after Rust changes Quote: "given the relative difficulty of doing this and the overall flakiness of the Xcode build process, we opted for a simple, reliable shell script" [`a-sa27-f012237-c1`, team a]
- Positions seen by the extractor (`a-sa27-f012237-q1`): external shell-script/CI pipeline for reliability (Ian Wagner/Stadia Maps — Xcode integration is possible but avoided as difficult and flaky) vs. Xcode-build-phase integration (unnamed alternative the source explicitly flags as "possible", implying some teams take it)

### `unmaintained-dependency-weight`

**Question.** When two crates cover the same need, how much should an unmaintained/flagged dependency (per RustSec) count against it versus its narrower scope fit?

- Teams: a · members (context): `a-sa06-f003414-q1` (f003414, desktop-cli-ui)
- Domains: desktop-cli-ui
- Concepts: dependency selection; crate maintenance signals
- Positions:
  - `unmaintained-dependency-weight--p1` — prefer actively-maintained broad-scope crate over flagged narrow one
    - **CrazyboyQCD** · Source `f003414` · date 2025-08-30 · locator comment 2025-08-30T08:19:58Z — argues `encoding` is unmaintained, buggy and legacy per a linked RustSec advisory, so a more modern crate (`encoding_rs`, or possibly ICU) is preferable even though `encoding_rs`'s stated focus is the Web Quote: "it is unmaintained, buggy and legacy, so I think a more mordern crate would be better" [`a-sa06-f003414-c1`, team a]
- Positions seen by the extractor (`a-sa06-f003414-q1`): prefer the actively maintained, broader-scope crate even if built for a narrower original use case (`encoding_rs` over `encoding`)

### `unsafe-fields-design`

**Question.** Should unsafe struct fields be expressed with a minimal, purely field-level rule set (mark the field unsafe if it carries a safety invariant; using it is then unsafe), or with a hybrid design that mixes syntactic markers and wrapper types?

- Teams: a · members (context): `a-sa20-f009698-q2` (f009698, core)
- Domains: core
- Concepts: unsafe-fields; RFC-design; drop-safety; wrapper-types
- Positions:
  - `unsafe-fields-design--p1` — minimal-field-level-rules
    - **@jswrenn** · Source `f009698` · date 2025-04-18 · locator "Unsafe Fields" section, comment posted 2025-04-18 — reports that after an observation from Ralf (that the additive/subtractive dichotomy and its Drop-related design concerns could be sidestepped, since a field already can't be put into an unsound-to-drop state without unsafe code), the RFC settled on two rules — a field is marked unsafe if it carries a safety invariant, and a field marked unsafe is unsafe to use — and that remaining discussion is now mostly about weighing this against a proposed alternative that mixes syntactic knobs and wrapper types Quote: "we can reduce field safety tooling to two rules: a field should be marked unsafe if it carries a safety invariant (of any kind); a field marked unsafe is unsafe to use." [`a-sa20-f009698-c2`, team a]
- Positions seen by the extractor (`a-sa20-f009698-q2`): minimal-field-level-rules, syntactic-knobs-plus-wrapper-types

### `unsafe-mental-model`

**Question.** What is `unsafe`'s proper mental model — a manual-invariant-maintenance discipline still bound by the same rules, or a permissive escape hatch?

- Teams: a · members (context): `a-sa28-f012469-q6` (f012469, core, embedded)
- Domains: core, embedded
- Concepts: unsafe; invariants; undefined behavior
- Positions:
  - `unsafe-mental-model--p1` — unsafe-is-manual-invariant-maintenance-not-permission-to-break-rules
    - **Ms2ger — track record uncertain in this source (recurring named contributor across 2015-2016, no confirmed authored crate/book found here); logged with this caveat** · Source `f012469` · date undated original; reposted 2015-04-27 · locator post by @bluss dated 2015-04-27T11:36:54Z — states unsafe's purpose is upholding Rust's invariants by hand, not license to violate them Quote: "unsafe code isn't for violating Rust's invariants, it's for maintaining them manually" [`a-sa28-f012469-c11`, team a]
  - `unsafe-mental-model--p2` — unsafe-is-a-last-resort-not-a-nuclear-option
    - **Aatch — track record uncertain in this source** · Source `f012469` · date undated original; reposted 2015-12-14 · locator post by @rgdmarshall dated 2015-12-14T07:53:53Z, sourced "on /r/rust" — frames using unsafe as closer to "diplomacy has failed" than to reaching for an extreme, rarely-justified tool Quote: "[Using unsafe is] less 'nuclear option' and more 'diplomacy has failed'." [`a-sa28-f012469-c12`, team a]
- Positions seen by the extractor (`a-sa28-f012469-q6`): single position recurring in this source — "unsafe isn't for violating invariants, it's for maintaining them manually" (Ms2ger) and "[unsafe is] less 'nuclear option', more 'diplomacy has failed'" (Aatch); no opposing voice quoted here either

### `unsafe-trait-vs-unsafe-method`

**Question.** When a trait's correct implementation is required for memory safety, should the trait itself be marked `unsafe`, or should the unsafe boundary sit on the consuming method instead?

- Teams: a · members (context): `a-sa07-f003716-q1` (f003716, core)
- Domains: core
- Concepts: unsafe; soundness; trait-safety-contracts
- Positions:
  - `unsafe-trait-vs-unsafe-method--p1` — unsafe-consuming-fn
    - **eugineerd** · Source `f003716` · date 2025-10-20 · locator PR #21601, comment 2025-10-20T17:20:03Z — says correctness must be enforced either by marking the Relationship trait unsafe or by leaving RelationshipAccessor::relationship unsafe since the implementer can't be trusted; the shipped design leaves the accessor method unsafe rather than the trait Quote: "either mark `Relationship` trait unsafe and mention that `ENTITY_FIELD_OFFSET` must be correct to be safely implemented, or we'd have to leave `RelationshipAccessor::relationship` unsafe" [`a-sa07-f003716-c1`, team a]
    - **urben1680** · Source `f003716` · date 2025-10-20 · locator PR #21601, comment 2025-10-20T17:52:07Z — accepts the design where the derive macro is trusted to build a valid accessor and the unsafe contract lands on the caller/consuming method rather than the trait Quote: "Then I agree on the design here." [`a-sa07-f003716-c2`, team a]
- Positions seen by the extractor (`a-sa07-f003716-q1`): unsafe-consuming-fn (eugineerd, shipped design; urben1680, agreed), unsafe-trait (eugineerd, raised as an alternative)

### `unstable-marking-of-required-macros`

**Question.** Should the proc-macro re-exports that a required language-level macro (e.g. `entry`, the crate's `main`) depends on be marked unstable along with everything else, or kept stable because the crate is unusable without them?

- Teams: b · members (context): `b-sb08-f002517-q2` (f002517, embedded)
- Domains: embedded
- Concepts: API stability; proc-macros; `#[unstable]` attribute
- Positions:
  - `unstable-marking-of-required-macros--p1` — needs-to-stay-usable
    - **bugadani** · Source `f002517` · date 2025-01-09 · locator comment 2025-01-09T13:55:03Z — the entry macro must stay usable/stable since without it users cannot write main and thus cannot use the crate at all Quote: "`entry` quite obviously needs to be stable - if you can't write `main`, how would you use the crate?" [`b-sb08-f002517-c4`, team b]
- Positions seen by the extractor (`b-sb08-f002517-q2`): needs-to-stay-usable (bugadani)

### `verify-crates-io-against-source`

**Question.** should crates.io-published bytes be checked against their source repository, and should such findings be released even incomplete

- Teams: a · members (context): `a-sR14-f005287-q1` (f005287, core)
- Domains: core
- Concepts: none given
- Positions:
  - `verify-crates-io-against-source--p1` — verify-and-publish-raw
    - **Kornel** · Source `f005287` · date 2024-06-16 · locator original post + reply to `@guenther`, 2024-06-16 — built a comparator between crates.io tarballs and their git repos across nearly all of crates.io, and released the raw dataset rather than withholding it for private review first. Quote: "I've compared nearly all Rust crates.io crates to contents of their git repositories. Here's a dump of this data... I'm releasing the data, because I don't have time to review it all." [`a-sR14-f005287-c1`, team a]
- Positions seen by the extractor (`a-sR14-f005287-q1`): verify-and-publish-raw (Kornel)

### `view-macro-native-control-flow`

**Question.** should a component-templating macro (like Yew's `html!`) support native imperative control flow (`for`, `if`) written inline, or require iterator-adapter/functional-expression style?

- Teams: b · members (context): `b-sR09-f003938-q1` (f003938, frontend)
- Domains: frontend
- Concepts: none given
- Positions:
  - `view-macro-native-control-flow--p1` — add native `for`-loop syntax to `html!` alongside the existing iterator-adapter style, because it's "more natural."
    - **Mattuwu (Yew maintainer)** · Source `f003938` · date 2025-11-29 · locator yew.rs/blog/2025/11/29/release-0-22, "For-Loops in html!" section. · L712-L727. — add native `for`-loop syntax to `html!` alongside the existing iterator-adapter style, because it's "more natural." Quote: "You can now use for-loops directly in the `html!` macro, making iteration more natural" — contrasted with the prior iterator-adapter form shown in the same post ("Before - using iterator adapters ... { for items.iter().map(|item| html! { <li>{ item }</li> }) }"). [`b-sR09-f003938-c1`, team b]
- Positions seen by the extractor (`b-sR09-f003938-q1`): add native `for`-loop syntax to `html!` alongside the existing iterator-adapter  (Mattuwu (Yew maintainer))

### `warn-missing-edition`

**Question.** Should rustc warn (or emit a note) whenever it is invoked without an explicit `--edition`, given how much edition-dependent behaviour has accumulated?

- Teams: a · members (context): `a-sa19-f009343-q1` (f009343, core, desktop-cli-ui)
- Domains: core, desktop-cli-ui
- Concepts: Rust editions; rustc CLI; tooling ergonomics; cargo/rustc coordination
- Positions:
  - `warn-missing-edition--p1` — support-warn-on-missing-edition
    - **kpreid** · Source `f009343` · date 2026-06-11 · locator reply, 2026-06-11T18:43:32.982Z — Given how significant edition differences have become, rustc should warn whenever invoked with no `--edition`, since almost no one today intends the 2015 default; notes a prior attempt stalled because many UI test suites set no edition and would gain new warnings. Quote: "rustc ought to warn whenever it is invoked without an --edition, because almost nobody writing a rustc invocation today should be using the 2015 edition." [`a-sa19-f009343-c1`, team a]
    - **ekuber** · Source `f009343` · date 2026-06-21 · locator linked PR rust-lang/rust#158102 (opened 2026-06-18), own reply 2026-06-21T22:53:55.156Z — Implemented the warning as an undismissable "note" rather than a lint specifically so `forbid`/`deny(warnings)` setups used by build probes aren't broken by it. Quote: "I implemented this as an undismisable note, which could also be a warning... The only people affected would be those explicitly comparing textual compiler output in scripts." [`a-sa19-f009343-c2`, team a]
- Positions seen by the extractor (`a-sa19-f009343-q1`): support-warn-on-missing-edition

### `wasi-path-workaround-vs-breaking-fix`

**Question.** When a Rust WASM extension host hits a known-bad upstream WASI behavior (a spurious leading `/` in Windows paths from `std::env::current_dir`) that has both a correct-but-breaking extension-API fix on offer and a pragmatic non-breaking user-space workaround, should the project ship the pragmatic workaround now, or hold out for the correct breaking fix (with API versioning to preserve compatibility)?

- Teams: b · members (context): `b-sb07-f002307-q1` (f002307, desktop-cli-ui, wasm)
- Domains: desktop-cli-ui, wasm
- Concepts: WASI; wasm extension API; breaking changes; API versioning; Windows path handling; upstream vs. workaround fixes
- Positions:
  - `wasi-path-workaround-vs-breaking-fix--p1` — pragmatic-workaround-preferred
    - **lilnasy** · Source `f002307` · date 2025-02-03 · locator issue #20559, comment 2025-02-03T09:43:55Z — after a workaround PR (#22600) was closed for not being an ideal fix, argues it's still worth shipping since it makes real-world extensions (Astro, Svelte) work now, and packages it as a community Windows build Quote: "the fix wasn't ideal, but perfect shouldn't be the enemy of functional" [`b-sb07-f002307-c1`, team b]
  - `wasi-path-workaround-vs-breaking-fix--p2` — correct-breaking-fix-preferred
    - **yakira-neko** · Source `f002307` · date 2025-02-10 · locator issue #20559, comment 2025-02-10T09:59:32Z — argues the proper fix is the extension-API change in PR #14905, and even though it is a breaking change, compatibility should be handled by shipping a new extension-API version rather than settling permanently for the older workaround Quote: "I believe that #14905 is the best way to solve this issue. Moreover, it is definitely a break[ing] change." [`b-sb07-f002307-c2`, team b]
- Positions seen by the extractor (`b-sb07-f002307-q1`): pragmatic-workaround-preferred, correct-breaking-fix-preferred

### `wasip2-std-minimal-imports`

**Question.** Should Rust's standard library on `wasm32-wasip2` import only the WASI interfaces a program uses, rather than the whole `wasi:cli` world whenever a simple std facility such as `format!` is used?

- Teams: a · members (context): `a-sT12-f008237-q2` (f008237, wasm)
- Domains: wasm
- Concepts: std; wasm32-wasip2; WASI imports; component size
- Positions:
  - `wasip2-std-minimal-imports--p1` — minimal imports
    - **author of Ideas Reifying (ideas.reify.ing)** · Source `f008237` · date 2026-09-22 · locator § "Standard Libraries", last paragraph; § "Issues and Contribute", unresolved list — using a simple std facility makes the compiled component import the whole `wasi:cli` world, including useless interfaces such as `wasi:cli/env`; the author filed this as an issue that is still open Quote: "the Rust compiler will include the whole wasi:cli world that includes some interfaces that are useless in this case" (flag: voice-unverified) [`a-sT12-f008237-c2`, team a]
- Positions seen by the extractor (`a-sT12-f008237-q2`): minimal imports (author, via a filed issue); current std behavior (no Voice defends it here)

### `wasm-bindgen-manual-vs-generated-glue`

**Question.** When wrapping Rust types for wasm-bindgen, should a practitioner write manual `js_sys` conversions or lean into bindgen's generated glue (accepting its naming/wrapper conventions)?

- Teams: b · members (context): `b-sb19-f005691-q1` (f005691, wasm, frontend)
- Domains: frontend, wasm
- Concepts: wasm-bindgen; FFI boundary; newtype wrappers
- Positions:
  - `wasm-bindgen-manual-vs-generated-glue--p1` — lean-into-bindgen-glue
    - **Brooklyn Zelenka** · Source `f005691` · date 2026-03-08 · locator § "Should You Write Manual Bindings?" — manual conversion with js_sys is a reasonable but time-consuming, brittle strategy; leaning into bindgen's glue (with naming conventions) buys better compile-time feedback Quote: "I see a fair amount of code online that seems to prefer manual conversions with js_sys. This is a reasonable strategy, but I have found it to be time consuming and brittle." [`b-sb19-f005691-c1`, team b]
- Positions seen by the extractor (`b-sb19-f005691-q1`): lean-into-bindgen-glue (Brooklyn Zelenka)

### `wasm-boundary-serde-vs-getters`

**Question.** at the Rust/Wasm↔JavaScript FFI boundary, should code favor ergonomic serialization (serde-wasm-bindgen) or manual/structural field access (wasm-bindgen getters), trading ergonomics against performance?

- Teams: a · members (context): `a-sa26-f011460-q3` (f011460, wasm, frontend)
- Domains: frontend, wasm
- Concepts: wasm-bindgen; serialization; FFI ergonomics
- Positions:
  - `wasm-boundary-serde-vs-getters--p1` — choose serde-wasm-bindgen vs wasm-bindgen getters based on hot/cold path
    - **Andrew Jakubowicz** · Source `f011460` · date 2026-06-11 · locator ~25:39 — after surveying GitHub crates, found people mostly using serde-wasm-bindgen (more ergonomic, more allocation) for cold paths like config initialization, and wasm-bindgen getters/reflection (faster, less ergonomic) for hot paths Quote: "from serving some GitHub crates, I found people are mostly doing the like the right thing, basically. Using serde-wasm-bindgen for cold paths, config initialization, and then using wasm-bindgen getters... if they're needed" [`a-sa26-f011460-c3`, team a]
- Positions seen by the extractor (`a-sa26-f011460-q3`): use-serde-for-cold-paths-getters-for-hot-paths (Andrew Jakubowicz, describing what he found practiced on GitHub)

### `wasm-bundler-choice`

**Question.** Which JS bundler/dev-server should front a Rust+wasm web app: webpack, an alternative bundler, or none?

- Teams: a · members (context): `a-sB02-f000256-q14` (f000256, web, wasm)
- Domains: wasm, web
- Concepts: build tooling; bundlers
- Positions:
  - `wasm-bundler-choice--p1` — webpack(chosen, "for convenience")
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Hello, World!" — "Install the dependencies" — the tutorial's template uses webpack as bundler/dev-server, stating this isn't required — Parcel and Rollup are named as also supporting wasm as ES modules, and using Rust+wasm with no bundler at all is called viable — webpack is picked "for convenience." Quote: "webpack is not required for working with Rust and WebAssembly, it is just the bundler and development server we've chosen for convenience here." [`a-sB02-f000256-c17`, team a]
- Positions seen by the extractor (`a-sB02-f000256-q14`): webpack(chosen, "for convenience"), parcel/rollup(named alternative, also supported), no-bundler(viable)

### `wasm-capabilities-explicit-vs-ambient`

**Question.** Should a Wasm component sandbox grant capabilities by default (ambient authority), or require every capability — including for middleware and dependencies — to be explicitly listed?

- Teams: b · members (context): `b-sR11-f005050-q1` (f005050, wasm)
- Domains: wasm
- Concepts: capability-based security; sandboxing; WASI
- Positions:
  - `wasm-capabilities-explicit-vs-ambient--p1` — middleware components get no ambient authority; every capability a middleware needs (e.g. an outbound host) must be explicitly listed in the trigger's inherit_configuration, exactly like any other component dependency
    - **The Spin Project** · Source `f005050` · date 2026-08-26 · locator "Middleware doesn't get a free pass on capabilities" section — an auth middleware can reach an endpoint only because the underlying component grants that capability and the trigger explicitly inherits it; otherwise the middleware gets nothing Quote: "Middleware gets no ambient authority." [`b-sR11-f005050-c1`, team b]
- Positions seen by the extractor (`b-sR11-f005050-q1`): explicit-only, no ambient authority, even for middleware

### `wasm-core-sum-types`

**Question.** Should core Wasm eventually gain a primitive sum-type / tagged-union construct (with e.g. a `br_table`-like case-matching instruction), or is representing variants as `struct` subtyping trees in a shared `rec` group sufficient?

- Teams: a · members (context): `a-sa05-f003074-q2` (f003074, wasm)
- Domains: wasm
- Concepts: wasm-gc; variants; type-system
- Positions:
  - `wasm-core-sum-types--p1` — primitive-sum-types-worthwhile
    - **fitzgen** · Source `f003074` · date 2025-06-16 · locator comment @fitzgen 2025-06-16T18:35:42Z — first-class sum types would let compilers emit a `br_table`-like exhaustive match instead of a chain of `br_on_cast` checks, which is easier to optimize and lets tools like binaryen reason over a closed case set Quote: "The most immediate benefit that first-class sum types would give us over shoe-horning sum types into struct subtypes would be a br_table-like instruction for exhaustively matching on cases" [`a-sa05-f003074-c4`, team a]
  - `wasm-core-sum-types--p2` — marginal-benefit-over-encoding
    - **rossberg** · Source `f003074` · date 2025-06-16 · locator comment @rossberg 2025-06-16T21:05:40Z — a custom type descriptor can already store an integer tag for `br_table` dispatch without wasting per-variant space, so primitive sum types would mainly save the trailing cast check, which requires substantial new Wasm machinery for limited additional gain Quote: "Saving the cast would essentially require adding a case construct to Wasm, which would be quite a bit of machinery. Other than that, sum types do not offer a hell lot of relevant generic optimisations" [`a-sa05-f003074-c5`, team a]
- Positions seen by the extractor (`a-sa05-f003074-q2`): primitive-sum-types-worthwhile, marginal-benefit-over-encoding

### `wasm-instantiate-streaming-vs-bytes`

**Question.** once a `.wasm` file is already fully loaded into memory as bytes/a blob, should the loader still route it through the streaming compile/instantiate API, or fall back to the plain bytes-based `instantiate`?

- Teams: b · members (context): `b-sR09-f003815-q1` (f003815, wasm)
- Domains: wasm
- Concepts: none given
- Positions:
  - `wasm-instantiate-streaming-vs-bytes--p1` — drop the streaming wrapper when the bytes are already in hand; it buys nothing there.
    - **RReverser (wasm-bindgen maintainer)** · Source `f003815` · date 2025-11-14 · locator wasm-bindgen/wasm-bindgen#4795, comment 2025-11-14T13:35:08Z. · L657-L661. — drop the streaming wrapper when the bytes are already in hand; it buys nothing there. Quote: "There's no need for the complex wrapping into a `Response` - `instantiateStreaming` doesn't have any benefits when we already loaded the whole file as a blob. Let's just revert to the regular `instantiate` which can take the bytes directly." [`b-sR09-f003815-c1`, team b]
- Positions seen by the extractor (`b-sR09-f003815-q1`): drop the streaming wrapper when the bytes are already in hand; it buys nothing t (RReverser (wasm-bindgen maintainer))

### `wasm-monolithic-vs-small-components`

**Question.** Within one Wasm application, should logic be kept in a single monolithic component, or decoupled into several small components composed via WIT interfaces?

- Teams: b · members (context): `b-sR11-f005053-q1` (f005053, wasm)
- Domains: wasm
- Concepts: component composition; WIT; modularity
- Positions:
  - `wasm-monolithic-vs-small-components--p1` — self-contained pieces of application logic (e.g. a classifier) should be split into their own Wasm component, composed into the app via a WIT interface and a declared spin.toml dependency, rather than living inline in the HTTP-triggered component
    - **Thorsten Hans** · Source `f005053` · date 2026-08-27 · locator "Recap" section — decoupling the classification logic into its own component "kept the HTTP control flow lean, standard, and easy to maintain," with WIT files as "the single source of truth" for the boundary Quote: "By decoupling the core classification logic into its own Wasm component, we kept the HTTP control flow lean, standard, and easy to maintain" [`b-sR11-f005053-c1`, team b]
- Positions seen by the extractor (`b-sR11-f005053-q1`): decouple into small, independently-versioned components

### `wasm-panic-hook`

**Question.** For panics on wasm32-unknown-unknown, install a panic hook (console_error_panic_hook) or accept the default trap message?

- Teams: a · members (context): `a-sB02-f000256-q13` (f000256, wasm, web)
- Domains: wasm, web
- Concepts: panic hook; error reporting
- Positions:
  - `wasm-panic-hook--p1` — install-panic-hook
    - **Rust and WebAssembly Working Group [voice-unverified]** · Source `f000256` · date 2018 · locator § "Debugging Rust-Generated WebAssembly" — "Logging Panics" — installing console_error_panic_hook turns a cryptic "RuntimeError: unreachable executed" trap into Rust's actual formatted panic message in the console; the tutorial's own exercise has the reader remove the hook and asks "Not as useful is it?" as the reason to keep it. Quote: "Rather than getting cryptic, difficult-to-debug RuntimeError: unreachable executed error messages, this gives you Rust's formatted panic message." [`a-sB02-f000256-c16`, team a]
- Positions seen by the extractor (`a-sB02-f000256-q13`): install-panic-hook(recommended), no-hook(rejected, "not as useful")

### `wasm-panic-unwind-vs-abort`

**Question.** For Rust compiled to WebAssembly (wasm32-unknown-unknown), should panics use the platform default of panic=abort, or panic=unwind (running destructors and preserving instance state across a single failed request)?

- Teams: a · members (context): `a-sa12-f004598-q1` (f004598, wasm, cloud-workers)
- Domains: cloud-workers, wasm
- Concepts: panic-handling; unwind-safety; wasm-compilation-targets
- Positions:
  - `wasm-panic-unwind-vs-abort--p1` — panic-unwind-for-reliability
    - **Guy Bedford, Hood Chatham, and Logan Gatlin (Cloudflare Workers/wasm-bindgen team)** · Source `f004598` · date 2026-04-22 · locator blog post, § "Implementing panic=unwind with WebAssembly Exception Handling" — added panic=unwind support to wasm-bindgen/Rust Workers via the WebAssembly Exception Handling proposal because panic=abort's default full-reinitialization recovery wipes in-memory state for stateful workloads like Durable Objects; shipped behind a flag in Rust Workers 0.8.0 with plans to make it the default Quote: "To recover from panics without discarding instance state, we needed panic=unwind support for wasm32-unknown-unknown in wasm-bindgen" [`a-sa12-f004598-c1`, team a]
- Positions seen by the extractor (`a-sa12-f004598-q1`): panic-unwind-for-reliability (Cloudflare Workers/wasm-bindgen team, adopted and planned as future default)

### `wasm-precise-traps-store-tearing`

**Question.** On hardware with "store-tearing" behavior, where a partial store can have observable side effects before trapping, should a WebAssembly runtime pay a load-before-store performance cost to guarantee precise, spec-compliant trap semantics, or accept imprecise traps as an acceptable, mostly theoretical risk on rare/low-power hardware?

- Teams: a · members (context): `a-02-f001181-q1` (f001181, wasm, embedded)
- Domains: embedded, wasm
- Concepts: Cranelift; trap semantics; memory safety; WebAssembly spec compliance; store tearing
- Positions:
  - `wasm-precise-traps-store-tearing--p1` — load-before-store-opt-in
    - **cfallin** · Source `f001181` · date 2024-03-22 · locator PR description — implements precise store-trap semantics (prepending a same-size load before every store) on architectures with store tearing (ARMv8, RISC-V), shipped off by default, accepting a measured ~2% cost on Apple M2 Pro, pending Wasm spec clarification Quote: "This PR implements the idea first proposed [...] namely to prepend a load of the same size to every store. The idea is that if the store will trap, the load will as well." [`a-02-f001181-c1`, team a]
- Positions seen by the extractor (`a-02-f001181-q1`): pay-for-precise-traps-opt-in (PR author), accept-imprecision-as-practically-irrelevant-on-tier1 (discussion converges toward this for production hardware, unattributed)

### `wasm-runtime-swap-vs-host-target`

**Question.** when compiling an async networking stack to a non-native target, should you swap the async runtime/networking primitives for target-specific shims, or keep the existing runtime (tokio) and target a platform that can host it directly?

- Teams: b · members (context): `b-sR05-f002177-q1` (f002177, decentralized-iroh)
- Domains: decentralized-iroh
- Concepts: none given
- Positions:
  - `wasm-runtime-swap-vs-host-target--p1` — the two Wasm targets warrant different answers — swap out tokio for a browser shim when targeting `wasm32-unknown-unknown`, but for `wasm32-wasip2/3` compile most of the stack unchanged and depend on tokio gaining support for that platform instead.
    - **matheus23 (n0-computer/iroh maintainer)** · Source `f002177` · date 2026-04-27 · locator n0-computer/iroh#2799, comment 2026-04-27T08:40:49Z. · L1518-L1524. — the two Wasm targets warrant different answers — swap out tokio for a browser shim when targeting `wasm32-unknown-unknown`, but for `wasm32-wasip2/3` compile most of the stack unchanged and depend on tokio gaining support for that platform instead. Quote: "Instead of swapping out tokio with another runtime (wasm-bindgen-futures/'the browser' in that case)... we'd instead try to compile most of the stack to wasm32-wasip2/3... So this means we'd be dependent on tokio to work under that platform and for it to support UDP/TCP sockets." [`b-sR05-f002177-c1`, team b]
- Positions seen by the extractor (`b-sR05-f002177-q1`): the two Wasm targets warrant different answers — swap out tokio for a browser sh (matheus23 (n0-computer/iroh maintainer))

### `wasm-undefined-symbols-error`

**Question.** Should Rust's WebAssembly targets treat undefined symbols as a hard link error by default (matching native platforms), even though some code intentionally relies on the current silent-import behavior?

- Teams: b · members (context): `b-sb23-f009737-q1` (f009737, wasm)
- Domains: wasm
- Concepts: wasm-ld; --allow-undefined; symbol resolution; wasm_import_module
- Positions:
  - `wasm-undefined-symbols-error--p1` — remove --allow-undefined as the wasm-target default; undefined symbols should error at build time like on native platforms
    - **Alex Crichton** · Source `f009737` · date 2026-04-04 · locator "What's wrong with --allow-undefined?" section — the current default silently turns undefined/typo'd symbols into WebAssembly imports instead of producing a build error, which "kicks the can down the road" from where a mistake is introduced to where it surfaces (often as a confusing runtime failure); removing it aligns wasm with how all other platforms already behave, and existing intentional users can opt back in per-symbol Quote: "All native platforms consider undefined symbols to be an error by default, and thus by passing --allow-undefined rustc is introducing surprising behavior on WebAssembly targets." [`b-sb23-f009737-c1`, team b]
- Positions seen by the extractor (`b-sb23-f009737-q1`): remove the historical --allow-undefined default so undefined symbols become build-time errors, with an explicit opt-in (`#[link(wasm_import_module = ...)]` or `-Clink-arg=--allow-undefined`) for the rare intentional case

### `web-api-wrapper-raw-vs-rust-types`

**Question.** When wrapping a browser Web API (e.g. `UrlSearchParams`) inside a Rust frontend-framework hook, should the API surface the raw web-sys type or convert it to an idiomatic Rust collection?

- Teams: a · members (context): `a-sR07-f002271-q1` (f002271, frontend, wasm)
- Domains: frontend, wasm
- Concepts: web-sys/wasm-bindgen API wrapping; idiomatic API surface
- Positions:
  - `web-api-wrapper-raw-vs-rust-types--p1` — convert-to-rust-collection
    - **lukechu10** · Source `f002271` · date 2024-11-03 · locator comment on router.rs (2024-11-03T22:58:52Z) — a hook exposing browser search params should return a `HashMap<String, String>` rather than the raw `UrlSearchParams` handle Quote: "we should return a `HashMap<String, String>` from search params to values" [`a-sR07-f002271-c1`, team a]
- Positions seen by the extractor (`a-sR07-f002271-q1`): convert-to-rust-collection (lukechu10)

### `web-framework-macro-free-api`

**Question.** should a Rust web framework favor a macro-free, type/extractor-driven API design, or a macro-based route/handler declaration syntax?

- Teams: a · members (context): `a-sa26-f011605-q1` (f011605, web)
- Domains: web
- Concepts: web frameworks; macros; API design
- Positions:
  - `web-framework-macro-free-api--p1` — macro-free API design is a distinguishing strength
    - **Joshua Mo** · Source `f011605` · date 2023-12-06 (updated 2025-07-04) · locator heading "Getting Started with Axum: Building REST APIs in Rust" (intro paragraph) — Axum stands out among Rust web frameworks specifically for its macro-free API design, predictable error handling, and Tower-based middleware Quote: "What makes Axum stand out in the Rust programming landscape is its macro free api design, predictable error handling model, and own middleware system built on Tower" [`a-sa26-f011605-c1`, team a]
- Positions seen by the extractor (`a-sa26-f011605-q1`): macro-free-api-design-as-a-selling-point (Joshua Mo, re: Axum)

### `web-session-store-default`

**Question.** Should a Rust web framework default new apps to a client-side (encrypted + signed cookie) session store for low-friction onboarding, or push toward a server-side session store (e.g. via `tower-sessions`) because client-stored session data cannot be force-invalidated or have permissions changed on the fly?

- Teams: b · members (context): `b-sb04-f001365-q1` (f001365, web)
- Domains: web
- Concepts: sessions; cookies; tower-sessions; request context; encryption; security; replay attacks
- Positions:
  - `web-session-store-default--p1` — cookie-store-default-with-encryption
    - **jondot** · Source `f001365` · date 2024-06-24 · locator issue #561, comment 2024-06-24T06:14:39Z — following Rails' precedent, argues Loco should start new apps with an encrypted-and-signed cookie session store (switchable later via `tower-sessions`) to keep initial friction low, even though Rails itself calls the choice "controversial" Quote: "I believe we should do the same by _starting with storing inside the cookie_ both encrypted and signed" [`b-sb04-f001365-c1`, team b]
  - `web-session-store-default--p2` — server-side-store-preferred
    - **schungx** · Source `f001365` · date 2024-06-24 · locator issue #561, comment 2024-06-24T06:50:58Z — objects that data stored on the client cannot be force-invalidated or have permissions changed on the fly, so whatever effort is saved by skipping a server-side store is negated by that inflexibility Quote: "there is no way to force-invalidate a session, or to change permissions on the fly" [`b-sb04-f001365-c2`, team b]
    - **yinho999** · Source `f001365` · date 2025-04-02 · locator issue #561, comment 2025-04-02T04:59:56Z — states plainly that encrypted cookies are not good practice in production because they can enable replay attacks and similar vulnerabilities, and that storing sensitive data server-side is always the better choice Quote: "the encrypted cookie is not a good practice in production environment since it can cause reply attacks and other vulnerabilities" [`b-sb04-f001365-c3`, team b]
- Positions seen by the extractor (`b-sb04-f001365-q1`): cookie-store-default-with-encryption, server-side-store-preferred

### `web-wasm-target-workaround-vs-target`

**Question.** Facing the absence of a proper Web-WASM Rust target, should the ecosystem work around it now with crate-feature plumbing, or push to get the target itself built first?

- Teams: a · members (context): `a-sa06-f003558-q1` (f003558, wasm)
- Domains: wasm
- Concepts: WASM compilation targets; ecosystem workarounds
- Positions:
  - `web-wasm-target-workaround-vs-target--p1` — pursue a real Web-WASM target instead of another workaround
    - **CryZe** · Source `f003558` · date 2025-09-19 · locator comment 2025-09-19T12:38:24Z — argues the root cause is the lack of a way to signal wasm-bindgen usage, and that a proper `wasm32-web` target would fix this class of problem generally, now that the project has active maintainers again Quote: "Shouldn't we finally discuss a proper wasm32-web / wasm32-bindgen target instead" [`a-sa06-f003558-c1`, team a]
  - `web-wasm-target-workaround-vs-target--p2` — ship the workaround now, a new target isn't realistic soon
    - **newpavlov** · Source `f003558` · date 2025-09-19 · locator comment 2025-09-19T12:53:59Z; 2025-09-19T13:06:16Z — says there has been zero progress on a Web WASM target in about 4 years, `getrandom` needs a solution that works with the current stable Rust and declared MSRV, and hypothetical language changes are out of scope for this issue Quote: "I don't have any hope for getting it anytime soon" [`a-sa06-f003558-c2`, team a]
- Positions seen by the extractor (`a-sa06-f003558-q1`): push for a real `wasm32-web`/`wasm32-bindgen` target before adding more workarounds; vs. ship a workaround now because the target has seen no progress and must work on current stable/MSRV

### `what-counts-as-semver-breaking`

**Question.** What counts as a semver-breaking change for a published Rust crate's public API?

- Teams: b · members (context): `b-bk03-f000267-q12` (f000267, core)
- Domains: core
- Concepts: semver; #[non_exhaustive]; enums; dependency versioning; MSRV; API evolution
- Positions:
  - `what-counts-as-semver-breaking--p1` — enum-variant-addition-breaks-without-non-exhaustive
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Changelog Guidelines § Part 3, "What is breaking for library consumers?" — adding a variant to a public enum that is not marked #[non_exhaustive] is classified as a breaking change, because downstream match expressions that were previously exhaustive stop compiling Quote: "Adding a variant to a public enum that is not marked #[non_exhaustive] is also breaking: downstream match expressions that were exhaustive stop compiling." (flag: voice-unverified) [`b-bk03-f000267-c12`, team b]
  - `what-counts-as-semver-breaking--p2` — dependency-type-leakage-forces-lockstep-major-bump
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Changelog Guidelines § Dependency updates — a dependency bump only needs a changelog entry, and forces a major-version bump of the crate itself, when the dependency's own semver-incompatible version change exposes types that appear in the crate's public API, since two incompatible versions of the same crate can't unify for downstream consumers; a dependency used only internally needs no entry at all Quote: "That lockstep is breaking, so the fragment kind is breaking and the release bumps the major version." (flag: voice-unverified) [`b-bk03-f000267-c13`, team b]
  - `what-counts-as-semver-breaking--p3` — msrv-bump-is-breaking
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Changelog Guidelines § Part 4, Compatibility — raising the minimum supported Rust version is itself classified as a breaking change for a crate (and is listed as "Yes/Yes" for both crate and zebrad changelogs), rather than a minor or patch-level change Quote: "an MSRV bump is itself a breaking change" (flag: voice-unverified) [`b-bk03-f000267-c14`, team b]
- Positions seen by the extractor (`b-bk03-f000267-q12`): enum-variant-addition-breaks-without-non-exhaustive, dependency-type-leakage-forces-lockstep-major-bump, msrv-bump-is-breaking

### `wit-dependency-keyword-design`

**Question.** should WIT syntax name a dependency-on-implementation with dedicated keywords (`locked-dep`/`unlocked-dep`), or with one generic keyword (`dependency`) whose lock state is inferred from the version syntax that follows it?

- Teams: b · members (context): `b-sR05-f001983-q1` (f001983, wasm)
- Domains: wasm
- Concepts: none given
- Positions:
  - `wit-dependency-keyword-design--p1` — favors the single `dependency` keyword with locked/unlocked inferred from the trailing syntax, for regularity and to keep vocabulary aligned with how package managers already use the word "dependency."
    - **Luke Wagner (Fastly; W3C/Bytecode Alliance component-model co-designer)** · Source `f001983` · date 2024-09-10 · locator WebAssembly/component-model#393, comments 2024-09-10T20:00:17Z and 2024-09-11T19:36:18Z. · L406-L465. — favors the single `dependency` keyword with locked/unlocked inferred from the trailing syntax, for regularity and to keep vocabulary aligned with how package managers already use the word "dependency." Quote: "What if we used just the word 'dependency' and inferred 'locked' vs. 'unlocked'/'range' from the syntax after the `@`." And: "the word 'dependency' is used by package managers and their associated build-config files (e.g., `npm`/`package.json`, `cargo`/`Cargo.toml`, etc) to exclusively refer to *implementations*." [`b-sR05-f001983-c1`, team b]
- Positions seen by the extractor (`b-sR05-f001983-q1`): favors the single `dependency` keyword with locked/unlocked inferred from the tr (Luke Wagner (Fastly; W3C/Bytecode Alliance component-model co-designer))

### `wit-export-direct-vs-interface`

**Question.** When defining a Wasm component's WIT world, should a function be exported directly from the world, or wrapped inside a named interface that the world then exports?

- Teams: a · members (context): `a-sR08-f003033-q1` (f003033, wasm)
- Domains: wasm
- Concepts: WIT; Wasm Component Model; API design
- Positions:
  - `wit-export-direct-vs-interface--p1` — wrap related functions inside a named interface and export the interface, rather than exporting a raw function from the world
    - **Tim McCallum (Bytecode Alliance)** · Source `f003033` · date 2025-05-21 · locator "WIT" section — while a world can export a bare function directly, doing so isn't the recommended approach; wrapping functions in an interface is more modular, extensible, and matches how WIT is used in real multi-function components Quote: "the recommended best practice is to wrap related functions inside an interface, which you then export from your world" [`a-sR08-f003033-c1`, team a]
- Positions seen by the extractor (`a-sR08-f003033-q1`): prefer wrapping in a named interface

### `work-stealing-vs-thread-per-core`

**Question.** For async Rust HTTP servers, is a work-stealing runtime (Tokio's default) or an executor-per-thread/"thread-per-core" runtime (Glommio, or Tokio/Smol configured with a `LocalRuntime`/`LocalExecutor` per thread) the better architecture — and is either one simply faster, or is the right choice workload-dependent?

- Teams: a · members (context): `a-sa18-f009026-q1` (f009026, distributed, web, cloud-workers)
- Domains: cloud-workers, distributed, web
- Concepts: work-stealing; thread-per-core; io_uring; epoll; tokio; glommio; smol; tail-latency
- Positions:
  - `work-stealing-vs-thread-per-core--p1` — choice-is-workload-dependent-not-universally-faster
    - **Caio (c410-f3r)** · Source `f009026` · date 2026-08-05 · locator "Final words" section, after 360 benchmarked configurations across 90 scenarios — ran balanced/unbalanced, low/medium/high-scale, CPU- through IO-heavy HTTP/2 workloads across tokio (work-stealing and executor-per-thread configurations), smol-ept and glommio-ept; found io_uring (Glommio) did not strictly outperform epoll-based runtimes even under the unbalanced "noisy neighbor" scenario designed to favor work-stealing, and that tokio's work-stealing configuration specifically showed unexplained throughput anomalies at 8/12 threads with no logged errors on either side; concludes the results are inconclusive on "which is faster" and that the right choice depends on the application's own workload shape Quote: "the benchmarks aren't conclusive. The choice between Executor-Per-Thread and Work-Stealing doesn't seem like a simple matter of \"which is faster\" but rather which architecture best aligns with your specific application logic." [`a-sa18-f009026-c1`, team a]
- Positions seen by the extractor (`a-sa18-f009026-q1`): choice-is-workload-dependent-not-universally-faster

### `wrap-third-party-types-in-public-api`

**Question.** Should a crate depend on a third-party type directly in its public API, or wrap it behind a local newtype/abstraction?

- Teams: b · members (context): `b-bk03-f000267-q15` (f000267, core)
- Domains: core
- Concepts: newtype pattern; abstraction over dependencies; API design
- Positions:
  - `wrap-third-party-types-in-public-api--p1` — abstract-over-third-party-crate-choice
    - **Zcash Foundation / Zebra project** · Source `f000267` · date unknown (living document) · locator Contextual Difficulty Validation RFC § Fundamental data types — because Rust has no standard u256 type, Zebra picks one of several third-party crate implementations but does not expose it directly — it wraps the chosen implementation behind its own ExpandedDifficulty type, so the underlying crate choice stays swappable Quote: "Zebra abstracts over the chosen u256 implementation using its ExpandedDifficulty type." (flag: voice-unverified) [`b-bk03-f000267-c17`, team b]
- Positions seen by the extractor (`b-bk03-f000267-q15`): abstract-over-third-party-crate-choice

### `xcframework-tooling-vs-hand-built`

**Question.** When assembling a Rust static library into an XCFramework for Swift distribution, should you hand-build the XCFramework's directory structure or use Apple's `xcodebuild -create-xcframework` tooling?

- Teams: a · members (context): `a-sa27-f012237-q2` (f012237, swift-interop)
- Domains: swift-interop
- Concepts: XCFramework; static-library packaging; lipo fat binaries
- Positions:
  - `xcframework-tooling-vs-hand-built--p1` — use Apple's official `xcodebuild -create-xcframework` rather than hand-assembling the XCFramework directory
    - **Ian Wagner** · Source `f012237` · date 2024-12-04 · locator section "Generating the XCFramework", opening paragraph — XCFramework's on-disk structure is simple enough that some teams build it by hand, but Stadia Maps scripts `xcodebuild -create-xcframework` to combine the per-target static libraries, headers and module map instead of replicating that structure manually Quote: "Some teams actually do this by hand, since it's a relatively simple structure, but we'll stick to Apple's official tooling." [`a-sa27-f012237-c2`, team a]
- Positions seen by the extractor (`a-sa27-f012237-q2`): use official `xcodebuild` tooling (Ian Wagner/Stadia Maps) vs. hand-assemble the XCFramework directory by hand (unnamed "some teams", described in source as viable given the format's simple structure)

### `lambda-build-tooling`

**Question.** Should Rust Lambdas be built and packaged with Cargo Lambda, or with a Docker-based toolchain?

- Grouping: New, carried only by the re-homed Claim a12 (strike: it recommends the Cargo Lambda tool, Docker only "if you need" it; zip vs container image is never argued). No team logged this Question, so it has no crosswalk row.
- Teams: none (re-homed Claim only) · members (context): 
- Domains: none (no team-local member)
- Concepts: none given
- Positions:
  - `lambda-build-tooling--cargo-lambda-by-default` — Cargo Lambda by default; Docker only when needed
    - **maahl (maahl.net)** · Source `f007659` · date 2023-11-05 · locator § "Cargo Lambda" and § "Dockerize the Lambda" — prefers Cargo Lambda for local runs, hot reload and arm64 zip builds, with a container image only "if, for some reason" it is required; reports a multi-stage build shrinking the image from 2.64 GB to 343 MB, and could not combine cargo-chef with cargo-lambda Quote: "The Rust runtime for Lambda is best interacted with using Cargo Lambda." (flag: voice-unverified) [`a-sT11-f007659-c2`, team a]

### `rust-for-backend-services-vs-jvm`

**Question.** Should backend services be written in Rust rather than on the JVM (Spring Boot) or in C/C++?

- Grouping: New, carried only by the re-homed Claim b33 (summer-rs), whose reasons compare against the JVM and C/C++, not against composing axum and sqlx. No team logged this Question, so it has no crosswalk row. Per the lead's grain ruling, choosing Rust is one Question per domain.
- Teams: none (re-homed Claim only) · members (context): 
- Domains: none (no team-local member)
- Concepts: none given
- Positions:
  - `rust-for-backend-services-vs-jvm--rust-over-jvm` — Rust over the JVM or C/C++ for backend services
    - **summer-rs project (github.com/spring-rs/spring-rs, README now titled summer-rs; no individual maintainer named in the source)** · Source `f005314` · date 2024-08-17 (frame date; the README revision read is undated, describes crate `summer` 0.4) · locator README intro paragraph, § Features, § component macros — the framework puts convention over configuration, following Spring Boot, and offers an extensible plugin system over Rust crates. It claims ease of use through a concise API and optional procedural macros. The `#[component]` macro removes the need to implement the Plugin trait by hand. Quote: "summer-rs is an application framework that emphasizes convention over configuration, inspired by Java's SpringBoot" (flag: voice-unverified) [`b-sT09-f005314-c1`, team b]
