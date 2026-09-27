# Adjudication, batch 1 merges

Adjudicator: opus, 2026-09-27. Inputs: `merge/crosswalk-b1.csv` (M1), `merge2/crosswalk-b1.csv` (M2), `team-{a,b}/extract-b1-*.md`. Output: `merge-final/crosswalk-b1.csv`, `merge-final/estimate/closure-b1.md`.

## Test applied

Two team-local Questions are one Question only if no competent practitioner could hold opposite Positions on them without contradicting themselves. In practice, three things keep a pair apart:
- One framing adds a condition a practitioner could reasonably treat as decisive, such as scale, platform, criticality, or "small and fixed".
- The two Questions offer different pairs of alternatives.
- The two Questions appeal to different Values.

Shared keywords, a shared source or a shared author never join a pair. I decided only the pairs M1 and M2 disagree on, plus where to place the items only M2 saw. I did not re-test groupings both merges agree on (see Caveats).

## 1. Alignment

- Both merges use the same team-local id, `<team>-<slice>-<frame_id>-q<k>`. M1 carries it in `team_question_ids` and M2 in `team_local_id`.
- I parsed every extract independently, using the markers `- Q:`, `- Question:` and `### Question —`. The parse gave 450 team-local Questions (a 225, b 225). Both merges drop the same 10 superseded sa14/sa15 entries (f005360 ×4, f005454 ×3, f005516 ×3), which saL1 replaces. That leaves 440 crosswalkable.
- Every id in either merge exists in my parse. Text-to-id identity was spot-checked through M1's "unsure" list and every disputed cluster below, and all matched.
- M2 has all 440. M1 has 420. The 20 it lacks are all team-b entries using the `- Question:` marker (sR03 ×6, sR05 ×11, sR09 ×3), so M1 missed them in parsing, not by choice. No item is in M1 only.

The 20 M2-only items, each checked against the whole population and every same-source entry from the other team:

| team-local id | final id | reason |
| --- | --- | --- |
| b-sR03-f001160-q1 | depend-vs-hand-roll | general "pay code cost to shrink dependency footprint vs take the dependency" is the canonical Question itself |
| b-sR05-f002453-q1 | depend-vs-hand-roll | same general Question; its extractor names f001160 as the same |
| b-sR05-f002341-q1 | memory-safety-and-resource-leaks | same source, same Voice (Arqu), same Question as a-sR07-f002341-q1 |
| b-sR05-f002466-q1 | scratch-register-param-vs-encapsulated | same comment as a-sa05-f002466-q1, but different alternatives (param vs encapsulate / types vs convention); "typed handles passed as params" is coherent, so kept apart |
| b-sR03-f000763-q1 | example-data-domain-struct-vs-generic | no match in population |
| b-sR03-f000763-q2 | single-pass-vs-multi-pass-iteration | no match |
| b-sR03-f000763-q3 | enum-glob-import-in-match | no match |
| b-sR03-f000889-q1 | ship-polyfill-before-spec | stopgap Questions (pure-rust-crypto, embedded-interpreter) choose a workaround for a platform gap, not "ship before a standard" |
| b-sR03-f001160-q2 | generated-size-vs-runtime-performance | no match |
| b-sR05-f001983-q1 | wit-dependency-keyword-design | no match |
| b-sR05-f002048-q1 | multiple-algorithms-autotune | no match |
| b-sR05-f002048-q2 | kernel-constants-hardcode-vs-comptime | per-dtype-constant (b-sR10-f004573-q2) is match-vs-metadata derivation, not hardcode-vs-parameter |
| b-sR05-f002151-q1 | young-integration-in-tree-vs-out-of-tree | the maturity condition ("young") is decisive; one can put features in the main crate generally and still keep young integrations out |
| b-sR05-f002151-q2 | platform-gating-feature-vs-target-cfg | nightly gating (b-sb06-f002033-q1) and the cfg-wasm proxy (b-sb22-f009062-q2) are different decisions |
| b-sR05-f002177-q1 | wasm-runtime-swap-vs-host-target | custom-wasm-target-vs-wasi runs unmodified programs, not a choice of async runtime |
| b-sR05-f002326-q1 | std-naming-convention-imperfect-fit | "into_ must consume" (strict) and "reuse raw_parts loosely" can be held together |
| b-sR05-f002453-q2 | trait-api-forced-arc-self | no match |
| b-sR09-f003815-q1 | wasm-instantiate-streaming-vs-bytes | no match |
| b-sR09-f003938-q1 | view-macro-native-control-flow | no match |
| b-sR09-f003955-q1 | land-hal-separate-now-vs-unified-later | a sequencing question; both Voices agree to unify, so this is not pac-crate-per-chip-vs-shared |

Domain dispute (one item): a-sR14-f007341-q1 reads "Domain: web (Rust/WASM frontend)". M2 takes the value before the parenthetical (web), and does so for all 5 sR14 entries. M1 also added frontend. Final: web, because it is the one rule applied across sR14; applying M1's reading consistently would also add wasm here and wasm to f004865-q2. Apart from this item, per-Question domains agree for 349 of 350 M1 Questions. `source_hint` agrees on all 420 shared items.

## 2. Agreement before adjudication

On the 420 items both merges contain:

| measure | value |
| --- | --- |
| items whose co-member set is identical | 369 / 420 = 87.9% |
| same, over 440, with M1's 20 gaps counted as disagreement | 369 / 440 = 83.9% |
| co-grouped pairs: M1 / M2 / both / union | 108 / 65 / 62 / 111 → 55.9% (Jaccard) |
| multi-member groups identical | 32 (M1 has 47, M2 has 41) |
| disputed pairs | 49: 46 grouped by M1 only, 3 grouped by M2 only |

M1 merges far more than M2. 46 of the 49 disputes are M1 merging what M2 keeps apart.

## 3. Decisions (one line per disputed pair)

"M1+" means M1 grouped the pair and M2 did not; "M2+" means the reverse.

C1 `depend-vs-hand-roll`
- M1+ a-02-f001053-q1 × a-sR06-f002016-q1: APART. f001053 weighs control and performance against reusing a crate. The core Question weighs dependency footprint and audit cost. Different Value.
- M1+ a-02-f001053-q1 × a-sa04-f002865-q1: APART, same reason.
- M1+ a-02-f001053-q1 × a-sa14-f005079-q2: APART, same reason.
- M1+ a-02-f001053-q1 × a-saL2-f011092-q3: APART. Persistent-data-structure crate vs vendor SDK maturity: different alternatives.
- M1+ a-sR06-f002016-q1 × a-saL2-f011092-q3: APART. f011092-q3 turns on how uneven vendor Rust SDKs are, not on footprint.
- M1+ a-sa04-f002865-q1 × a-saL2-f011092-q3: APART, same reason.
- M1+ a-sa14-f005079-q2 × a-saL2-f011092-q3: APART, same reason.

C2 `macro-vs-boilerplate`
- M1+ a-sR08-f003082-q1 × a-sa23-f011186-q3: TOGETHER. "Prefer a function unless codegen is needed" and "use macros like salt" answer one question, how readily to reach for macros. Holding "liberally" on one and "only when needed" on the other contradicts.
- M1+ a-sR08-f003082-q1 × a-sa17-f007736-q1: APART. The Lambda Question is conditioned on a small, fixed boilerplate. Someone who uses macros liberally can coherently decline it; Sam Van Overmeire says it is worth it with many Lambdas.
- M1+ a-sR08-f003082-q1 × b-sb20-f007736-q1: APART, same reason.
- M1+ a-sR08-f003082-q1 × b-sb20-f007760-q1: APART, same reason.
- M1+ a-sa23-f011186-q3 × a-sa17-f007736-q1: APART, same reason.
- M1+ a-sa23-f011186-q3 × b-sb20-f007736-q1: APART, same reason.
- M1+ a-sa23-f011186-q3 × b-sb20-f007760-q1: APART, same reason.
- M1+ a-sR08-f003082-q1 × b-sR10-f004804-q2: APART. f004804 asks whether a macro may hide construction requirements (transparency vs ergonomics), not how often to use macros.
- M1+ a-sa23-f011186-q3 × b-sR10-f004804-q2: APART, same reason.
- M1+ a-sa17-f007736-q1 × b-sR10-f004804-q2: APART. Removing boilerplate and hiding API requirements are different alternatives.
- M1+ b-sR10-f004804-q2 × b-sb20-f007736-q1: APART, same reason.
- M1+ b-sR10-f004804-q2 × b-sb20-f007760-q1: APART, same reason.

C3 `human-written-code-standard`
- M1+ a-sR14-f004865-q2 × a-sa15-f005821-q2: APART. How much review AI code for peripheral components needs, vs whether critical code must be human-written: one person can hold "human-only for hot paths" and "light review for a vibe-coded GUI".

C4 `default-features-minimal-vs-inclusive`
- M1+ a-sa02-f002127-q1 × b-sb25-f011435-q2: APART. On-by-default for less friction vs a curation bar (a), against compiled surface vs dependency count (b): different Values.

C5 `optional-parameters-api-shape`
- M1+ a-sa06-f003414-q4 × b-sb05-f001512-q3: APART. Separate function vs a longer argument list, against a Config struct vs many constructors. "Separate fn" and "Config struct" can be held together.
- M1+ a-sa06-f003414-q4 × b-sb10-f003222-q2: APART. `_with_opts` plus wrappers is neither side of a's choice.
- M1+ b-sb05-f001512-q3 × b-sb10-f003222-q2: APART. with_opts-plus-wrappers combines both of b-sb05's sides, so its Claim does not pin to either.

C6 `platform-logic-module-vs-inline` / `extract-single-use-function`
- M2+ a-sa14-f005079-q4 × b-sb04-f001392-q3: APART. a is module vs same file, and its winning Position still extracts a helper function. That is b's "extract" side, so opposite Positions coexist.

C7 `silent-fallback-vs-explicit-error`
- M1+ a-sa14-f005079-q5 × b-sb03-f000669-q1: APART. "Error on ambiguous caller input" and "silent default for missing context under load" coexist in one person, who weighs API correctness against serving under load.
- M1+ a-sa14-f005079-q5 × b-sR10-f004706-q1: APART. b adds a build-time vs runtime axis.
- M1+ b-sR10-f004706-q1 × b-sb03-f000669-q1: APART, same reason.

C8 `immediate-vs-retained-gui`
- M1+ a-sa15-f005857-q1 × b-sb21-f008390-q3: APART. "Elm-style fits real-time sync" and "the choice doesn't matter at small scale" are compatible.

C9 `named-default-args-overloading`
- M1+ a-sa18-f009104-q1 × b-sb24-f011312-q6: APART. "Reject all for simplicity" in general alongside "yes to overloading for interop only" is coherent.

C10 `library-panic`
- M1+ a-sa21-f011069-q3 × b-sb05-f001512-q1: APART. A general panic policy against a HAL-config instance. "Panic is fine if documented" alongside "HAL constructors should return Result" is coherent.
- M1+ b-sR10-f004573-q1 × b-sb05-f001512-q1: APART, same reason.
- M1+ b-sR12-f005421-q1 × b-sb05-f001512-q1: APART, same reason.

C11 `rust-for-high-level-apps` / `rust-for-web-frontend`
- M2+ a-sa26-f011305-q1 × a-sa26-f012146-q1: APART. f012146 reuses f011305's wording, but its positions_seen (Leptos isomorphic vs Loco plus JS) are both Rust web frameworks. Its Claim does not answer "push Rust into high-level or keep it to systems".
- M1+ a-sa26-f012146-q1 × b-sb20-f007290-q1: APART. Which model is preferable (a) vs whether Rust is ready today (b). fasterthanlime's own Claim holds both "optimistic about fullstack Rust" and "TS frontend for now".

C12 `externref-in-rust`
- M1+ a-sa29-f013113-q1 × a-sa29-f013113-q2: APART. q1 has a third, middle-path option. One can favour language extension in general (q2) and the table-index path for externref (q1).

C13 `ai-authored-community-contributions`
- M1+ a-sa29-f013224-q2 × b-sR11-f004993-q1: APART. Whether to write prose with an LLM, vs a project's contribution policy (ban vs manage). "Dislike LLM prose" alongside "no ban" is coherent.
- M1+ a-sa29-f013224-q2 × b-sR13-f009740-q1: APART, same reason.
- M1+ a-sa29-f013224-q2 × b-sb15-f004721-q1: APART. alexcrichton's "author accountable and in the loop" is compatible with jasn-armstrng's "my points, LLM composition".
- M1+ b-sR11-f004993-q1 × b-sb20-f007942-q1: APART. Contribution policy vs AI content in a curated publication.
- M1+ b-sR13-f009740-q1 × b-sb20-f007942-q1: APART, same reason.
- M1+ b-sb15-f004721-q1 × b-sb20-f007942-q1: APART, same reason.

C14 `http-error-status-in-result`
- M1+ a-saL1-f005454-q1 × b-sb22-f008906-q4: APART. q4 trades response-shape flexibility against drop-in use. Mammino weighs it as its own decision, and q3's rule ("Err for failures an outer layer translates") allows either answer.
- M1+ b-sb22-f008906-q3 × b-sb22-f008906-q4: APART, same reason.

C15 `middleware-hook-vs-typestate` / `tower-middleware-vs-handler-helpers`
- M2+ a-saL1-f005454-q2 × b-sb22-f008906-q1: APART. The non-middleware side differs (typestate vs ad hoc helpers). "Typestate over middleware" alongside "tower over helpers" is coherent.

C16 `nightly-in-production`
- M1+ a-saL2-f011092-q5 × b-sb23-f011233-q2: APART. "Stable-only in general" alongside "portable_simd for numeric kernels" is coherent. b appeals to SIMD ergonomics and safety.

C17 `typestate-vs-runtime-checks`
- M1+ b-sb03-f000715-q1 × b-sb05-f001512-q2: APART. Driver mode vs config validity, and b-sb05 is explicitly "given the complexity". The answer changes with context.
- M1+ b-sb03-f000715-q1 × b-sb24-f011295-q2: APART. Typestate for crypto keys alongside a runtime check for driver mode is coherent.
- M1+ b-sb05-f001512-q2 × b-sb24-f011295-q2: APART, same reason.

Outcome: 1 of 49 disputed pairs ends TOGETHER and 48 APART. All 3 M2+ pairs are APART. Of the 46 M1+ pairs, 45 are APART and 1 (a-sR08 × a-sa23) is TOGETHER. Compared with M2 over all 440 items, the final crosswalk keeps 70 of M2's 73 co-grouped pairs and adds 1.

## 4. Final counts

| measure | M1 | M2 | final |
| --- | --- | --- | --- |
| team-local Questions crosswalked | 420 | 440 | 440 |
| canonical Questions | 350 | 385 | 387 |
| a-only | 167 | 175 | 177 |
| b-only | 152 | 182 | 184 |
| both | 31 | 28 | 26 |
| multi-member canonical | 47 | 42 | 40 |
| crosswalk rows | 740 | — | 721 |

Crosswalk shape: one row per (team, source, canonical Question, stratum). `stratum` is the union of the members' domains (M2's per-item `question_domains`), giving one row per Domain. When one team logged two local Questions in the same source that map to one canonical Question, they share a row, joined in `team_local_id`.

## 5. Estimate

`uv run python scripts/map/estimate.py --crosswalk-dir merge-final --batch 1 --out merge-final/estimate` (no `--audit-pass`, no `--merge-check-agreement`, so part 3 FAILs by construction):

| stratum | n1 | n2 | m | seen | Chapman N̂ | unseen % | Chao1 N̂ | unseen % | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cloud-workers | 23 | 14 | 6 | 31 | 50.4 | 38.5% | 88.6 | 65.0% | FAIL |
| core | 112 | 92 | 21 | 183 | 476.7 | 61.6% | 691.9 | 73.6% | FAIL |
| decentralized-iroh | 15 | 22 | 4 | 33 | 72.6 | 54.5% | 81.0 | 59.3% | FAIL |
| desktop-cli-ui | 29 | 20 | 4 | 45 | 125.0 | 64.0% | 197.1 | 77.2% | FAIL |
| distributed | 25 | 23 | 6 | 42 | 88.1 | 52.4% | 115.1 | 63.5% | FAIL |
| embedded | 33 | 32 | 5 | 60 | 186.0 | 67.7% | 816.2 | 92.6% | FAIL |
| frontend | 15 | 15 | 2 | 28 | 84.3 | 66.8% | 366.0 | 92.3% | FAIL |
| ml | 20 | 24 | 5 | 39 | 86.5 | 54.9% | 175.1 | 77.7% | FAIL |
| other | 7 | 17 | 2 | 22 | 47.0 | 53.2% | 50.9 | 56.8% | FAIL |
| swift-interop | 4 | 4 | 0 | 8 | 24.0 | 66.7% | 32.5 | 75.4% | FAIL |
| wasm | 25 | 33 | 3 | 55 | 220.0 | 75.0% | 455.2 | 87.9% | FAIL |
| web | 30 | 19 | 4 | 45 | 123.0 | 63.4% | 325.2 | 86.2% | FAIL |

Parts 1, 2 and 3 FAIL in every stratum. Part 4 PASSes everywhere except swift-interop.

## Caveats that could change the result

- The estimate depends heavily on the identity test. The same script on M1's crosswalk gives Chapman N̂ of 74.0 (desktop-cli-ui), 53.0 (frontend), 116.0 (wasm) and 81.5 (web). The final crosswalk gives 125.0, 84.3, 220.0 and 123.0. The strict test lowers m (desktop 7→4, frontend 4→2, wasm 5→3, web 7→4), and with m this small one pair moves N̂ by tens of percent.
- The strict test runs into how the extractors write. They frame Questions in the context of their source, so the test splits context variants of one general trade-off. Under this test, capture-recapture counts context-specific Questions, and that population may never close. This is a design issue for the lead, not something adjudication can fix.
- Agreed groupings were not re-tested. Both merges put a-sR06-f002016-q1, a-sa04-f002865-q1 and a-sa14-f005079-q2 into `depend-vs-hand-roll`. The same test would likely split them (the executor case appeals to miri/loom testing, not footprint), and possibly `library-panic`'s core and the pair a-saL1-f005454-q1 × b-sb22-f008906-q3 too. A full re-test would lower m further.
- Closest call: a-sa05-f002466-q1 × b-sR05-f002466-q1, the same saulecabrera comment, kept apart. Merging it gives wasm m = 4.
- The a-sa09-f004055-q1 text opens with f002466's scratch-register wording before its own PAC Question ("recurs here as: …"), which looks like extractor carryover. Both merges treat it as the PAC Question. Not disputed, and left as is.
- Final ids are M1 slugs where the group derives from an M1 group, plus 38 new slugs. For ids whose members changed, the text of `merge/merged-questions-b1.md` no longer describes them: `depend-vs-hand-roll`, `macro-vs-boilerplate`, `library-panic`, `ai-authored-community-contributions`, `http-error-status-in-result`, `silent-fallback-vs-explicit-error`, `optional-parameters-api-shape`, `default-features-minimal-vs-inclusive`, `human-written-code-standard`, `externref-in-rust`, `named-default-args-overloading`, `nightly-in-production`, `immediate-vs-retained-gui`, `rust-for-web-frontend`, `memory-safety-and-resource-leaks`. No merged-questions file was written for the final crosswalk, which was not in scope.
