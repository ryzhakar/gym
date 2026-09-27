# Merge check 3 — Rust batch 1, merge-v3 (operational grain)

Checker: opus, blind, 2026-09-28. Blind grouping: `merge-check3/blind-grouping-b1.md`, written before any file under `merge*/` or `audit/` was opened. Scripts and intermediates are in the checker's scratchpad (not committed); they are `pop.py`, `groups.py` and `compare.py`.

## Setup

- Population: 558 team-local Questions (565 parsed, minus 7 sa14/sa15 entries that saL1 re-logged). My re-log mapping was derived blind and matches merge-v3's supersession list exactly.
- Id scheme check: every one of the 558 ids resolves in `merge-v3/crosswalk-b1.csv` (544) or merge-v3's Claim-less removal list (14). No id is unmatched in either direction.
- Seed **20260928**. Draw: `random.Random(20260928).sample(sorted(ids), 112)`. Sample size **112**.
- Excluded as removed by merge-v3 (Claim-less): `a-sT11-f007659-q2`, `b-sT05-f003044-q3`, `b-sb20-f007290-q3`. **109 items can be evaluated.**
- Co-member set: the other population members that share an item's Question. Removed items are dropped on both sides. I report two readings:
  - **in-sample**: co-members restricted to the sample. This is the dispatch's reading.
  - **population**: all co-members. This is stricter: for each sampled item I searched all 558.

## Result (blind)

| reading | agree | 95% Wilson |
| --- | --- | --- |
| in-sample | 104/109 = **95.4%** | [89.7, 98.0] |
| population | 85/109 = **78.0%** | [69.3, 84.7] |
| in-sample, excluding items with no in-sample co-member on either side | 14/19 = 73.7% | [51.2, 88.2] |
| population, excluding items that are singletons on both sides | 28/52 = 53.8% | [40.5, 66.7] |

Threats to validity:
- **The in-sample figure is inflated by construction.** 90 of the 109 items have no in-sample co-member on either side, so they agree trivially. The population figure is the informative one.
- **Blind grouping read only the Question text.** merge-v3 also read the Claims. At least one disagreement (`a-sa26-f012146-q1`) comes from this asymmetry, and the asymmetry biases against merge-v3.
- **One judge, same model family as the merger (opus).** Correlated framing pushes agreement up. The two errors run in opposite directions.
- **Borderline items.** I judged that 5 sampled items are not Questions under the rule. merge-v3 keeps all 5. This does not enter the co-member figure; see the last section.

## Disagreements (population reading; `IN` = also an in-sample disagreement)

"Mine" is my blind group. "v3" is merge-v3's `question_id` and co-members. Each entry gives my blind reason and my verdict after reading merge-v3's Grouping line.

1. `a-sB02-f000256-q3` (S8). v3 `ffi-copy-vs-share`.
   - Mine adds `a-sa26-f011460-q3` (serde-wasm-bindgen vs getters). v3 splits it out as `wasm-boundary-serde-vs-getters`.
   - Blind reason: getters keep the object in Wasm, so it is copy vs handle.
   - After reason: **v3 right.** The alternatives named are different crates or approaches.
2. `a-sR06-f001989-q1` (S12). v3 `hard-dependency-vs-pluggable-interface`.
   - v3 adds `a-sR13-f004586-q1` (TLS backend: hard dependency vs pluggable provider). Mine is a singleton.
   - After reason: **v3 right.** The alternatives are the same: a hard dependency or an interface any implementation can supply. I missed it.
3. `a-sR07-f002271-q1` (S15). v3 `web-api-wrapper-raw-vs-rust-types`, a singleton.
   - Mine adds `b-bk03-f000267-q15` (third-party type in the public API vs a local wrapper).
   - Blind reason: both pick, at the API signature, between exposing the dependency's type and exposing a type the crate controls.
   - After reason: **held.** merge-v3 gives no Grouping reason. The motivations differ (ergonomics vs stability), but the alternative is the same.
4. `a-sT12-f008237-q1` (S23). v3 `wasm-components-for-interop`.
   - v3 adds `a-sa07-f003922-q1` (agent tools: language SDK vs Wasm components). Mine is a singleton; I rejected it because "SDK" is not "C-ABI".
   - After reason: **v3 right.** Both choose Wasm components against a native binding. That is a context variant.
5. `a-sT12-f008455-q1` (S24) and `b-sb21-f008793-q1` (S102). v3 `all-rust-vs-platform-native-tooling`.
   - v3 adds the Android JNI Questions `b-sb20-f007678-q1` and `b-sb22-f008914-q1`, plus `b-sb13-f004367-q1` (wasm-bindgen-test vs Playwright). Mine groups only the two objc2 items.
   - After reason: **v3 right.** I had already merged iOS AppDelegate with XCTest across points of work, and by that same logic the other platforms are context. Two items.
6. `a-sa17-f007797-q1` (S32). v3 `lambda-vs-containers`.
   - v3 adds `b-sT07-f004166-q1` (edge Workers vs VPS) and `b-sb20-f007797-q1` (team b's reading of the same source). Mine has `a-sa24-f011220-q1` only.
   - After reason: **v3 right.** I noted blind that f004166 fits, then left it out. f007797 is the same source and the same dispute.
7. `a-sa18-f008583-q1` (S35) and `a-saL2-f011092-q6` (S52), **IN**. v3 `library-error-type-opaque-vs-typed`, which absorbs the thiserror-Display question.
   - Mine keeps `thiserror-Display drops the chain` {a-sa18-f008583-q1, b-sb21-f008583-q1} apart from opaque-vs-typed {a-saL2-f011092-q6, a-sa14-f005149-q1, b-sb10-f003188-q2, b-sb10-f003222-q1}.
   - Blind reason: different point of work; one logs existing typed errors, the other designs the error type.
   - After reason: **v3 right.** The alternatives are the same crates (anyhow/eyre vs thiserror alone). "Typed errors need an opaque wrapper to log context" is a Position on that choice. Two items.
8. `a-sa25-f011413-q1` (S41). v3 `proc-macro-derives-vs-reflection-shape`.
   - v3 adds `b-sb24-f011413-q2` (`#[serde(with)]` annotations vs reflection dispatch).
   - After reason: **v3 right.** It is the same derives-vs-reflection choice from the same talk. I misread it blind from the truncated text.
9. `a-sa26-f011305-q2` (S42, **IN**) and `a-sa26-f012146-q1` (S44, **IN**).
   - Mine puts f012146-q1 with f011305-q1/q2 in `rust-for-high-level-apps`, because its text reuses f011305's wording. v3 puts f012146-q1 in `rust-for-web-frontend`.
   - After reason: **v3 right.** f012146's only Claim is Leptos's isomorphic client/server model vs Loco's Rails MVC with a separate JS frontend. That is the frontend domain, and the reused wording is misleading. This is the text-only asymmetry noted above. Two items.
10. `a-saL1-f005516-q1` (S49). v3 `rust-vs-c-inherent-performance`.
    - v3 adds `a-saL1-f005516-q3` (initialisation cost), `a-saL1-f005516-q4` (composability vs borrow-checker friction) and `b-sb26-f013214-q2` (does game dev need `unsafe` for speed?). Mine is a singleton.
    - After reason: **v3 right.** Each is a narrower cost or benefit inside "does safe Rust cost performance against C/C++".
11. `a-saL1-f005516-q2` (S50). v3 `replace-battle-tested-c-with-rust`.
    - v3 adds `b-sb19-f005743-q1` (moral imperative), `b-sb19-f005743-q4` (bootstrap trust) and `b-sb26-f012849-q1` (broad quality improvement).
    - After reason: **v3 right.** I had put this item, an age argument, on that choice as an Argument. Consistency requires the moral, trust and quality arguments too.
12. `a-saL2-f011092-q3` (S51). v3 `depend-vs-hand-roll`.
    - v3 adds `a-sR06-f002016-q1` (take the tch/libtorch bindings tree vs the audit burden).
    - After reason: **v3 right.** It is the same choice: take the dependency or not.
13. `b-bk01-f000233-q6` (S56). v3 `blocking-work-in-async`, a singleton.
    - Mine adds `b-bk01-f000233-q5` (is async suitable for CPU-bound work?), `b-sb18-f005307-q1` (async I/O with sync storage) and `b-sb18-f005307-q2` (a current_thread runtime for blocking I/O).
    - After reason: **held for sb18-q2.** A dedicated current_thread runtime is one of the mechanisms for integrating blocking work. Concede bk01-q5: whether to use async differs from how to integrate. sb18-q1 is weakly held. merge-v3 gives no Grouping reason.
14. `b-sR05-f002048-q2` (S65). v3 `kernel-constants-hardcode-vs-comptime`.
    - v3 adds `b-sR10-f004573-q2` (per-dtype constant: match vs trait metadata).
    - After reason: **v3 right.** It is hardcode vs parameterise or derive in two burn PRs.
15. `b-sR08-f003731-q1` (S67). v3 `enum-vs-flags-and-optionals`.
    - v3 adds `b-sR08-f003531-q1` (bool vs enum).
    - Blind reason: the alternative sets differ ({non_exhaustive enum, struct of optional fields} vs {bool, enum}), and so does the motive (extensibility vs more than two outcomes).
    - After reason: **held, weakly.**
16. `b-sR10-f004706-q1` (S69). v3 `missing-asset-build-fail-vs-runtime-degrade`, a singleton.
    - Mine adds `a-sa14-f005079-q5` (ambiguous input: silent default vs error), `b-sb03-f000669-q1` (missing context: default vs surface the panic) and `a-sa14-f004985-q3` (crash vs degrade).
    - After reason: **held for f005079-q5 and f000669-q1.** The same concrete choice, error or silent default when something expected is missing, appears in three contexts. merge-v3 split the whole family as a value axis without a per-member reason. Concede f004985-q3: stopping or containing a whole service is a fault-isolation choice, which v3 places in `service-fault-isolation-degrade`.
17. `b-sb05-f001512-q2` (S80). v3 `hal-driver-typestate`.
    - Mine adds `b-sb24-f011295-q2` (typestate vs runtime assertions for crypto keys).
    - After reason: **held.** v3's reason ("same esp-hal driver-API choice") limits the Question to one crate. The concrete pattern choice, typestate vs runtime check, is the same, and the domain is context under the rule.
18. `b-sb15-f004721-q1` (S89). v3 `ai-authored-community-contributions`.
    - v3 adds `b-sb20-f007942-q1` (AI content in newsletters).
    - After reason: **v3 right.** I had already included forum posts. Newsletters are one more venue.
19. `b-sb19-f005699-q1` (S93), **IN**. v3 `rust-for-web-frontend`.
    - v3 adds `a-sa26-f012146-q1` and `b-sb20-f007290-q1` (is fullstack Dioxus ready to replace JS frameworks?). Mine has only the Wasm-vs-JS performance items.
    - After reason: **v3 right.** "Choose Rust for X" means one Question per domain, so readiness and performance are both contexts of X = web frontend.
20. `b-sb22-f009236-q1` (S103). v3 `std-naming-conventions-strictness`.
    - Mine adds `b-sR05-f002326-q1` (`raw_parts` naming). v3 deliberately keeps it apart.
    - After reason: **v3 right.** These are different conventions, so the named alternatives differ.
21. `b-sb23-f011233-q2` (S105). v3 `nightly-in-production`.
    - v3 adds `a-saL2-f011092-q5` (nightly-only features in production vs stable).
    - After reason: **v3 right.** `std::simd` on nightly is the same choice applied to numeric kernels.

## After-reason tally (report only; the blind figure is the result)

- Population disagreements: 24 items. Of these, v3 is right on 19 after reading its reason: S8, S12, S23, S24, S102, S32, S35, S52, S41, S42, S44, S49, S50, S51, S65, S89, S93, S103, S105.
- Held: 5 items, all population-only, none in-sample:
  - S15 (raw web-sys type vs wrapper);
  - S56 (blocking-work integration, for sb18-q2);
  - S67 (enum vs bool/optionals);
  - S69 (error vs silent default, for f005079-q5 and f000669-q1);
  - S80 (typestate across domains).
- Every one of the 5 in-sample disagreements goes to v3 after its reason.
- My own error pattern:
  - under-merging context variants that the rule explicitly joins (platforms, venues, deployment substrates);
  - grouping by wording rather than by Claims (f012146).
- v3's pattern on the 5 held items: 4 are split singletons with no Grouping line. The fifth (S80) is scoped to one crate. All 5 lean toward over-splitting in the families it re-split from merge-v2.

## Not a Question under the rule (my blind judgment; merge-v3 keeps all five)

| team-local id | v3 id | why |
| --- | --- | --- |
| `a-sa11-f004512-q3` | `ergonomic-sugar-now-or-later` | YAGNI timing, a Value trade-off |
| `b-sb09-f003052-q1` | `ad-hoc-special-case-vs-general-mechanism` | stopgap vs proper fix, which the rule names as a Value |
| `a-sa28-f012469-q3` | `memory-safety-design-priority` | a retrospective on language design; no practitioner choice |
| `b-sb19-f005743-q3` | `memory-safety-vs-correctness-frame` | a framing of discourse; no practitioner choice |
| `b-bk03-f000267-q12` | `what-counts-as-semver-breaking` | a knowledge question; no alternatives |

`b-sb09-f003052-q1` conflicts with merge-v3's own header. The header says `stopgap vs proper fix` is never a Question, yet merge-v3 split the `ship-stopgap-now-vs-proper-fix` family into 10 singleton Questions, "ad hoc special case" among them, instead of removing them. The lead should rule on whether those 10 are Questions or Value conflicts.
