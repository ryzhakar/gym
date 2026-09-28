# Fill resolution, batch 1

t4-fill-resolve-b1, 2026-09-28. Inputs: `fill/run-a/positions-01..13.csv` and `summaries-01..13.md`, `fill/run-b/` the same, `fill/input-b1-01..13.md`, `fill/key-b1.csv`, `merge-v3/fill-remap-b1.csv`. Outputs: `fill/resolved-b1.csv`, `fill/positions-final-b1.md`. The resolver wrote neither fill. Both runs' low-confidence flags were ignored; every row went through the fixed rule.

## Method

1. Both runs' rows joined on (claim_id, question_id), with `fill-remap-b1.csv` applied to both first. The remap touches 8 rows; in both runs each of the 8 held the remap's old Position, so all 8 mapped cleanly.
2. Where A and B named the same Position (or both `none`), the row passes as `agree`.
3. For every disagreement, a third fill blind to both runs' answers: read the input entry and, for 5 of 10 rows, the cached source (`third` column; reasons below). Blinding lapse: the resolver settled all 10 choices before seeing any run answer for these rows, but before writing them to file it printed a parse listing of which Positions each run had summarised, which exposes some run answers. As a check, a fresh opus instance given only the 10 input entries and the source cache filled them blind: it matched the resolver on 9 of 10. It differs on `a-sa30-f013276-c5` (check `--p1`, resolver `--p2`). With the check as the third fill, that row would resolve to `--p1`, so it is flagged for the adjudicator. Every other outcome is the same under either third fill.
4. Majority of three decides; a three-way split is `unresolved`.
5. Tags: where A and B tagged a Position differently, a third tag, blind to both, decided by majority. Where only one run summarised a Position (because the other run put its Claim elsewhere), that tag plus the third tag decide: equal passes, different is `unresolved`. The resolver wrote 188 of the 202 third tags blind. For the other 14, both runs' tags had shown on screen while the summary format was being inspected, so their third tag comes from the fresh blind instance above. The resolver's own non-blind tags matched it on 9 of 14 and were discarded. Criteria for both: fact means a checkable claim about the world that evidence could settle; tradeoff means each side buys something at a cost and context decides; taste means a preference of style, naming, norms or values that no evidence would settle. `opinion-map.md` names the three tags but does not define them.
6. Summaries: for each Position, a run whose summary covers exactly the final Claims is eligible. Between two eligible summaries, the one sharing the higher proportion of the Claims' quoted words is picked, as a check that it states the Position in its advocates' own terms; on a tie the shorter one is picked. This is a lexical proxy, not a reading of all 1,214 summaries, and none were merged. Each Position's source and score are given in `positions-final-b1.md`.

## Position assignment

- Rows: A 772, B 772; present in only one run: 0; duplicate keys: 0.
- Agreement before resolution: 762/772 = 98.70%.
- Disagreements: 10. Resolved by the third fill (majority): 9. Unresolved (three-way split): 1.

| claim_id | question_id | run_a | run_b | third | final | third-fill reason |
|---|---|---|---|---|---|---|
| `a-sB02-f000256-c2` | `bounded-grid-universe` | `--p2` | `--p1` | `--p2` | `--p2` | p1 and p2 state the same choice; p2 carries the comparison the claim makes (periodic over growable and fixed-edge); pick is between duplicates |
| `a-sa15-f005821-c1` | `become-tail-call-codegen` | `--alt1` | `--p1` | `--alt1` | `--alt1` | question asks reliable-across-targets vs good-on-some; claim reports ARM64 win, x86-64 loses to asm, WASM 1.2-4.6x slower; conclusion asks for tips on x86 and WASM; the cross-target inconsistency is what alt1 states |
| `a-sa30-f013276-c5` | `dyn-compatibility-rules-relaxation` | `--p1` | `--p2` | `--p2` | `--p2` | 'The rules are too constraining' matches p2; p1 is 'for this case' (quinedot's higher-ranked dyn EventStore), which parasyte does not address; both are present in the quote |
| `a-saL1-f005454-c5` | `middleware-hook-vs-typestate` | `--p2` | `none` | `none` | `none` | source lobste.rs 2025-02-25T01:56: quotes the FAQ and asks 'How has this design choice played out?'; a question, no stance; follow-ups say 'Makes sense to me' |
| `b-bk03-f000267-c3` | `feature-flags-vs-separate-crates` | `--p1` | `--split-into-crates` | `--p1` | `--p1` | quote is 'modular, library-first design': p1 label verbatim |
| `b-bk03-f000267-c6` | `ai-authored-community-contributions` | `--acceptable-if-substance-is-own` | `--p1` | `--p1` | `--p1` | welcomes AI-assisted work, requires disclosure in PR and the human as sole responsible author: welcome + disclosure + accountability |
| `b-sb09-f002719-c3` | `hot-patching-for-iteration` | `none` | `--hot-patch` | `--hot-patch` | `--hot-patch` | source PR #3797 2025-03-19T20:56:59Z: cranelift suggested as an addition to hot reloading, not an alternative; he names rustc artifact copying as the remaining cost and wants 'blink and you miss it' hotpatching |
| `b-sb23-f009334-c2` | `crate-maintenance-signaling` | `--new-deprecate-mechanism` | `--status-opt-in-only` | `--status-auto-decays` | `unresolved` | source @kornel 2026-04-18T03:31: old=bad by default for 99% of crates, author affirms an old crate is fine; replies to the decay vs opt-in exchange and rejects doing nothing for the 99% (against dlight's 'if the author does nothing, it should work as today') |
| `b-sb25-f011435-c1` | `feature-flags-vs-separate-crates` | `--split-into-crates` | `--p1` | `--split-into-crates` | `--split-into-crates` | separate project; small core with rendering, parsing, networking, windowing behind traits: 'modular crates joined by traits' |
| `b-sb26-f013214-c3` | `rust-vs-c-inherent-performance` | `--safe-rust-matches` | `none` | `--safe-rust-matches` | `--safe-rust-matches` | source 2024-01-13T20:31: several CPUs coordinated for 'good performance' in a 3D metaverse client, hard in C++, 'not bad' in safe Rust with no unsafe |

### Unresolved rows

- `b-sb23-f009334-c2` · `crate-maintenance-signaling`: A `crate-maintenance-signaling--new-deprecate-mechanism`, B `crate-maintenance-signaling--status-opt-in-only`, third `crate-maintenance-signaling--status-auto-decays`. Left out of the evidence minimum until an adjudicator reads the source (`internals.rust-lang.org/t/…/24174`, @kornel 2026-04-18T03:31:27Z). All three readings are defensible: kornel argues for an author-affirmed "still fine" mark and against leaving the 99% untouched, and names neither per-version deprecation, decay nor opt-in.

## Tags

- Agreement before resolution, over the 607 Positions both runs summarised (the runs' own ids, before the remap): 410/607 = 67.55%.
- Final Positions with at least one Claim: 607. Tag agree: 406 (405 where A and B matched, 1 where the only run's tag matched the third). Resolved by the third tag (majority): 192 (191 two-against-one, plus `wrap-third-party-types-in-public-api--controlled-type`, where each run's two remapped source Positions carried taste and tradeoff and the third tag, tradeoff, is in both runs). Unresolved: 9.
- A final `positions-final-b1.md` entry with tag `unresolved` stays untagged until adjudicated.

| Position | A | B | third | why unresolved |
|---|---|---|---|---|
| `ai-authored-community-contributions--p1` | - | tradeoff | taste | one run only, differs from third |
| `dedicated-methods-vs-manual-composition--p1` | tradeoff | fact | taste | three-way split |
| `doctests-must-compile--p1` | taste | fact | tradeoff | three-way split |
| `dyn-compatibility-rules-relaxation--p2` | - | fact | tradeoff | one run only, differs from third |
| `mutex-vs-atomics--atomics-carry-own-bugs` | tradeoff | taste | fact | three-way split |
| `replace-battle-tested-c-with-rust--safety-not-enough` | fact | taste | tradeoff | three-way split |
| `rust-vs-c-inherent-performance--safe-rust-matches` | tradeoff | - | fact | one run only, differs from third |
| `same-state-transition-trigger--p3` | taste | fact | tradeoff | three-way split |
| `ui-dsl-vs-plain-rust--p1` | fact | taste | tradeoff | three-way split |

## Summaries

- Source: run-a 312, run-b 295.
- Picked by quoted-word share: 388; tied on share, shorter taken: 207; only run whose summary covers the final Claims: 8; only run with a summary: 4.
- Positions where only one run's summary covers the final Claims (the other run's summary was written with a Claim that resolution moved in or out), and that run's summary was taken: `ai-authored-community-contributions--acceptable-if-substance-is-own` (run-b); `bounded-grid-universe--p2` (run-a); `crate-maintenance-signaling--new-deprecate-mechanism` (run-b); `crate-maintenance-signaling--status-opt-in-only` (run-a); `dyn-compatibility-rules-relaxation--p1` (run-b); `feature-flags-vs-separate-crates--p1` (run-a); `feature-flags-vs-separate-crates--split-into-crates` (run-a); `hot-patching-for-iteration--hot-patch` (run-b).
- Run summaries left without a final Claim, not carried: A `middleware-hook-vs-typestate--p2`; B `become-tail-call-codegen--p1`, `bounded-grid-universe--p1`.

## Key comparison

`key-b1.csv` (the merger's own assignment, 772 rows) was compared with the final after the remap was applied to the key. Before the remap, 5 key rows carry pre-remap question ids, and those resolve cleanly. After it, all 772 keys match a resolved row, and all 8 remapped rows agree with the key.

Final differs from the key on 23 rows: 19 where A and B agreed against the key, 3 decided by majority, 1 unresolved. No row was changed to match the key: the rule has the blind fills decide. Seven of the rows are Rust and WebAssembly Book Claims (`a-sB02-f000256-*`) keyed to `--p1`. In six, both runs moved the Claim to `--p2` or `--p3`; in one (`bounded-grid-universe`) the majority did. In all seven Questions the key's `--p1` is a short label that restates the Position both runs chose (for example `opt-level-z-vs-s--p1` "Measure both(recommended)" against `--p2` "Never assume opt-level='z' beats opt-level='s' for binary size — measure both"; `library-io-factored-out--p1` "Factor-out-I/O" against `--p3`). These are duplicate Positions for the merger to collapse. They are not fill errors.

| claim_id | question_id | key | final | status |
|---|---|---|---|---|
| `b-sb19-f005743-c5` | `affine-types-vs-formal-verification` | `--p1` | `--p2` | agree |
| `a-sa23-f011186-c1` | `api-schema-spec-first-vs-code-first` | `--p2` | `--p1` | agree |
| `a-sa15-f005821-c1` | `become-tail-call-codegen` | `--p1` | `--alt1` | majority |
| `a-sB02-f000256-c2` | `bounded-grid-universe` | `--p1` | `--p2` | majority |
| `b-sb16-f005000-c5` | `coupled-debug-accessor-vs-primitive` | `--p3` | `--p2` | agree |
| `b-sb23-f009334-c2` | `crate-maintenance-signaling` | `--new-deprecate-mechanism` | `unresolved` | unresolved |
| `b-sb14-f004399-c3` | `docs-as-rust-vs-markdown` | `--p1` | `--p2` | agree |
| `a-sB02-f000256-c3` | `ffi-copy-vs-share` | `--p1` | `--p2` | agree |
| `a-sB02-f000256-c10` | `generics-vs-dyn-for-abstraction` | `--p1` | `--p2` | agree |
| `a-sT11-f004960-c1b` | `library-auth-opinionated-vs-unopinionated` | `--unopinionated-library` | `--authenticated-managed-default` | agree |
| `b-sb10-f003222-c1` | `library-error-type-opaque-vs-typed` | `--concrete-typed-errors` | `--hybrid-snafu` | agree |
| `a-sB02-f000256-c13` | `library-io-factored-out` | `--p1` | `--p3` | agree |
| `a-saL1-f005454-c5` | `middleware-hook-vs-typestate` | `--p2` | `none` | majority |
| `a-sB02-f000256-c7` | `opt-level-z-vs-s` | `--p1` | `--p2` | agree |
| `a-sB02-f000256-c6` | `profile-before-optimizing` | `--p1` | `--p2` | agree |
| `b-sb19-f005743-c9` | `project-decision-speed-vs-inclusion` | `--p1` | `--alt1` | agree |
| `b-sR04-f001515-c1` | `public-naming-brevity-vs-clarity` | `--clarity-over-brevity` | `--alt1` | agree |
| `a-sB02-f000256-c15` | `reproduce-wasm-bugs-natively` | `--p1` | `--p2` | agree |
| `a-saL1-f005516-c5` | `rust-vs-c-inherent-performance` | `--types-enable-optimizations` | `--p1` | agree |
| `a-sa15-f005516-c1` | `rust-vs-c-inherent-performance` | `--p1` | `--composability-wins` | agree |
| `a-sa19-f009196-c5` | `timer-instant-overflow-panic` | `--p1` | `--p2` | agree |
| `a-sa09-f004055-c1` | `typed-wrapper-vs-raw-access` | `--encode-in-types` | `--p2` | agree |
| `a-sa09-f004055-c2` | `typed-wrapper-vs-raw-access` | `--encode-in-types` | `--p2` | agree |
