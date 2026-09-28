# Batch 2 preparation — Rust map

Preparer: r-batch2-prep, 2026-09-28. Prime directive: one bar for the whole batch, fixed before the first read. Every prompt a batch-2 agent reads is fixed by the sha256 below. The four changed prompts are headed "Frozen for batch 2 (2026-09-28)". No extraction, content judgment, edits under `maps/`, or git commands were used.

## 1. Frozen prompt set (sha256, 2026-09-28)

| file | state | sha256 |
|---|---|---|
| `prompts/common.md` | unchanged | `90961877fa257941967f51ab5d6e3dfefbf768ba7c978e718a2ab0c8298bfab5` |
| `prompts/t2-extract.md` | rewritten, frozen | see § 6 |
| `prompts/t3-fill.md` | rewritten, frozen | see § 6 |
| `prompts/t4-merge.md` | rewritten, frozen | see § 6 |
| `prompts/t4-fill-resolve.md` | rewritten, frozen | see § 6 |
| `prompts/t3-claim.md` | unchanged | `f49c0bc7776d5b27b1c6a06a9939270635158f458d7588177642e42970c72eb2` |
| `prompts/t3-voice.md` | unchanged | `2fba53298fb6e7cb3e545030ca3d7f1a0e92f563c2248941e6b6389d9a5701ae` |
| `prompts/t3-args.md` | unchanged | `fe4ca684777f1a92e63c7ad659d66c6be5a962a60473833ce7e9d8be59090315` |
| `prompts/t1-frame.md`, `t1-union.md` | not used in batch 2 | — |

## 2. Changes and their grounds

| # | change | where | ground |
|---|---|---|---|
| P1 | Rules 6–9 folded into one numbered list. Rule 8 now carries the lead's strike list (diagnoses, support requests, tentative plans, off-Question). Rule 9 says track record is never the extractor's test. | `prompts/t2-extract.md` § Rules | `audit/audit-b1-sendback.md` header (rule 6 re-worded mid-batch); `audit-b1-third.md` line 7 (rules 8–9 added); `strike-b1-third.md` lines 7–14 (strike list); `audit-b1-third.md` § Notes D1 (rule-9 misread by both teams); `slice-1-review.md` line 125 |
| P2 | The batch-1 audit bar, stated to the extractor | `t2-extract.md` § The audit bar | `audit-b1.md` line 51; `audit-b1-sendback.md` line 52; `audit-b1-third.md` lines 72, 74 (the third pass's bar, the latest; the earlier two are narrower wordings of the same bar) |
| P3 | One Nothing-new format, with `reason-code:` (off-subject, no-decision, no-rust-voice) and a `reason:` sentence that never mentions opposition or how many Voices speak | `t2-extract.md` § Outputs | `audit-b1-sendback.md` line 122 (three formats in use); `audit-b1.md` line 12 (census 11/97 and 30/101 on the opposition ground) |
| P4 | Read log: exactly 7 fields, comma fields quoted, no prose in integer columns | `t2-extract.md` § Outputs | `audit-b1.md` lines 121–122 |
| P5 | `voice:` holds the name or handle only; qualifiers move to a new `connection:` field | `t2-extract.md` § Outputs | `slice-1-review.md` line 125 (25 ids for 18 people from extractor naming); `maps/rust/voices/` holds ids such as `antimora-tracel-ai-burn-maintainer` next to `antimora` (read only) |
| P6 | A book's or course's front page is a stub, so the row is unreachable; chapters must be read | `t2-extract.md` rules 1, 7 | `audit-b1-third.md` line 132 (f000149, f000217) |
| P7 | Non-English sources: read in the source language, paraphrase in English, quote in the original | `t2-extract.md` rule 10 | `fable-plan.md` line 161; batch 2 is the first non-English batch (plan OP7, line 478) |
| P8 | Nothing-new census as a script gate before the audit draws. Flagged rows go to fresh `-fixK` extractors, not to a whole-batch send-back. | `scripts/map/census.py`; `t4-merge.md` § Census gate | `slice-1-review.md` line 125 ("a script-sized check … as a gate before the audit draws"); `audit-b1.md` line 12 |
| P9 | Audit populations come from the census output. Sample sizes: nothing-new max(5, ⌈10%⌉) (third pass's rule); every drop; 20 Claims per team (was ⌈10%⌉ = 2 and 4). One seed, drawn once. | `t4-merge.md` § t4-audit | `audit-b1-third.md` lines 44, 72; `slice-1-review.md` line 125 ("sized above 4"). Decided here: 20 is the smallest round sample where one team's 95% Wilson interval on a strike rate like batch 1's 13/36 excludes 0 by a wide margin |
| P10 | Strike escalation fixed in advance: 3 or more of 20 struck triggers a full strike check of that team's Claims before the merge | `t4-merge.md` § t4-audit | `strike-b1-third.md` line 108 (13/36 on a full check after 3/4 in the sample); `audit-b1-third.md` § Limits. Decided here so the reaction is not chosen after the numbers are seen |
| P11 | Grain rule passed to merger and checker verbatim | `t4-merge.md` step 3 | `merge-v3/merged-questions-b1.md` lines 5–12; `slice-1-review.md` line 125 |
| P12 | Merge check gates on the population reading only; below 90%, one second merge and one adjudication, then stop | `t4-merge.md` § t4-merge-check | `fable-plan.md` line 131; `slice-1-review.md` lines 44, 56 (in-sample 95.4% against population 78.0%; three merges and three checks in batch 1) |
| P13 | Voice ids normalized at merge (handle slug, no qualifiers, lookup in `maps/rust/voices/`, § Voice ids listing) | `t4-merge.md` step 4 | `slice-1-review.md` lines 49, 125; `fable-plan.md` line 353 (directive rule 5) |
| P14 | Batch 2 merges into a new `merge-b2/` that holds only binding crosswalks (a copy of `merge-v3/crosswalk-b1.csv` plus b2) | `t4-merge.md` step 5 | `estimate.py` reads every `crosswalk-b*.csv` in its directory (lines 34–41), and `merge/crosswalk-b1.csv` is superseded (`slice-1-review.md` line 5) |
| P15 | `estimate.py` is always run with `--audit-pass` and `--merge-check-agreement` | `t4-merge.md` § estimate.py | `slice-1-review.md` lines 31, 125 |
| P16 | Tag definitions written into the fill prompt and the resolver prompt verbatim | `prompts/t3-fill.md` step 2; `t4-fill-resolve.md` step 4 | `fill/resolve-b1.md` line 11; `slice-1-review.md` line 46 (tags 67.6%, definitions written after the fact) |
| P17 | Resolver writes every third fill before printing anything that shows a run's answer | `t4-fill-resolve.md` step 2 | `fill/resolve-b1.md` line 9 (blinding lapse) |
| P18 | Resolver writes `fill/checks-b2.csv` for compile to turn into `MAP/checks/` | `t4-fill-resolve.md` § Outputs | `slice-1-review.md` lines 56, 125; `maps/rust/schema.yaml` lines 102–113 (kind `check`) |
| P19 | Batch-suffixed fill paths (`positions-b{n}-NN.csv`), so batch 1's files are not overwritten | `t3-fill.md`, `t4-fill-resolve.md` | batch 1's unsuffixed `fill/run-{a,b}/positions-NN.csv` |
| S1 | Sampler: `--by-class` splits each cell's k evenly across source classes, and rows already drawn in the batch leave later pools. `--cells` gives per-cell k, with `*` for a whole-language cell. The default path is unchanged. | `scripts/map/sample.py` | `slice-1-review.md` line 123, target (2) (domain-subframes took 57% of reads at 3.4 Q/hour against 8+ for books and talks); `fable-plan.md` line 102 |
| S2 | Frame preparation moved from an inline script into `scripts/map/prepare_frame.py`, with the same rules plus `window=in` and `--drop` | `scripts/map/prepare_frame.py` | `samples/batch-1.md` lines 7–47 |
| S3 | Tests: batch 1 re-drawn from seed 1786744536, matching both team files byte for byte; `prepare_frame.py` reproduces `frame-b1-input.csv`; by-class quotas; census gate | `scripts/map/test_sample.py`, `test_census.py` | `samples/batch-1.md` line 5 |
| F1 | swift-interop: 169 forums.swift.org rows dropped by a title-and-path rule | `frame/frame-swift-fix.md`, `frame-swift-fix-drop.csv` | `slice-1-review.md` lines 29, 123, target (3) |
| D1 | Batch 2 drawn: en core, ml, desktop-cli-ui, embedded, wasm at 18; the 9 zh cells with ≥ 18 rows at 18; uk and de as whole-language cells at 20 | `samples/batch-2.md` | `slice-1-review.md` line 123, targets (1), (5), (6); the lead's dispatch |

Test run, 2026-09-28: `uv run --with pytest pytest scripts/map/` gave 7 passed (6 sampler, 1 census). pytest is not a project dependency; `--with` adds it for the run only.

## 3. Batch 2 size

292 rows per team, 584 in all, 445 distinct frame ids (139 drawn by both teams).
- en: 90 per team.
- zh: 162 per team.
- uk: 20 per team.
- de: 20 per team.

Seed `1311957526`. Details are in `samples/batch-2.md`.

## 4. Agent runs, projected end to end

Batch 1's actual runs, from this session's agent roster (names, not an events log; a resumed agent counts once):
- about 68 extraction agents over three passes and supplementary slices, for 396 sampled rows (`r-x-*`, `r-xr-*`, `r-xt-*`, `r-xb-*`);
- 2 merges, 3 merge checks, 1 adjudication;
- about 3 audits;
- 5 Claim-verification runs, 5 Voice runs, 8 fill runs plus 1 resolver, 4 argument runs, 1 compile.

That is about 100 in all, against the plan's ~70 for the slice (`fable-plan.md` line 453).

Batch 2 projection. The Claim count scales batch 1's 771 Claims per 396 rows, about 1.95 per row, giving about 1,140 Claims. Per-run capacities follow batch 1's practice, not the plan's nominal sizes.

| stage | base runs | basis |
|---|---|---|
| extraction | 40 | ⌈292/15⌉ = 20 per team (`fable-plan.md` line 108) |
| census fix | 2 | one fresh extractor per team, assuming ≤ 15 flagged rows each |
| audit | 2 | one per team: about 13 nothing-new re-reads, every drop, 20 Claims |
| merge + merge check | 2 | P12 |
| Claim verification | 8 | 7 at batch 1's ~166 Claims per run, plus 1 adjudicator |
| Voices | 5 | batch 1: 399 ids in 5 runs; zh, uk and de add mostly new ids |
| fills + resolve | 14 | batch 1's 8 runs for 772 Claims, scaled to about 12; resolver 1; fresh blind check 1 |
| arguments | 5 | batch 1: 4 |
| compile | 1 | |
| base total | 79 | |

Contingent runs, each fixed in advance by the frozen rules:
- audit send-back: +21 per failed team (20 extractors and a re-audit). Batch 1 failed both teams on pass 1 and pass 2.
- full strike check: about +12 per team (~570 Claims at 50 per run).
- merge check < 90%: +2.

Worst case: 79 + 42 + 24 + 2 = 147.

Runs per unseen Question cannot be projected honestly. It depends on how many new canonical Questions batch 2 yields, and the English second draw and the first non-English draw have no yield history. Batch 1 gives about 4 seen Questions per run (399 from about 100 runs). After batch 2, compute runs ÷ (canonical ids in `merge-b2/crosswalk-b2.csv` absent from `merge-v3/crosswalk-b1.csv`).

## 5. What batch 2 cannot fix

Prerequisites outside this preparer's scope, still open before the first read:
- **No re-sample mode.** The plan says unreachable rows are re-sampled by the script (`fable-plan.md` line 111), but `sample.py` has no such mode, and the files read here do not record whether batch 1's unreachable rows (A 10, B 3, `slice-1-review.md` line 9) were replaced. The draw holds 3 (team a) and 5 (team b) paywalled book pages. Until a mode exists, those rows stay unread.
- **Prefetch.** Chapter enumeration for books and docs sites, and a retry window for yt-dlp (`slice-1-review.md` line 125), belong to `scripts/research/`, outside this preparer's code scope. P6 makes an extractor mark a front page unreachable rather than read, but only the bundler can fetch the chapters. 23–25 youtube.com rows per team face the 429 risk (`prefetch-b1.md` line 22).
- **Compile.** Compile has no prompt file. Its dispatch must turn `fill/checks-b2.csv` into `MAP/checks/` records, or validator rule 4 still gates nothing. The validator's 417 FAILs (`slice-1-review.md` line 53) are compile- and verify-side and untouched.
- **Census calibration.** The census gate has not been run against batch 1's extracts to check that it recovers the auditor's 11/97 and 30/101. Reading those files needs a ruling under common.md rule 3, which was asked of the lead. It is a phrase gate, not a re-read: a reason that avoids the words but rests on the forbidden ground passes it. The audit remains the check.

Limits of the design that the numbers should be read against:
- **Strata that get no second English batch.** web, distributed, decentralized-iroh, frontend, cloud-workers and swift-interop are not drawn as English cells. The first four get zh-only reads plus incidental English rows through secondary hints (en web 17–18 rows per team). cloud-workers and swift-interop get almost nothing. `estimate.py` part 2 counts the batches present in a stratum's crosswalk rows, whatever cell drew them, so it can PASS for a stratum no batch-2 cell targeted. Read part 2 against `samples/batch-2.md`.
- **Languages pooled in one estimate.** Language is a reporting dimension (`fable-plan.md` line 34, OP2), so `estimate.py` pools zh and en captures per stratum. zh reads are a first batch and en reads a second, so catchability differs by language inside one estimate, which Chapman assumes away.
- **Class balancing makes inclusion unequal.** Rows in small classes are drawn close to whole: zh frontend 18 of 19 and 18 of 18; de 20 of 32. Frame ids drawn by both teams rose to 139 of 292 per team (en 28/90, zh 86/162), against 17/198 in batch 1. A shared source gives both teams the same Questions, which raises m and lowers N̂, a bias toward closure. Batch 1 already showed the effect: one shared book carried 11 of 51 two-team Questions (`slice-1-review.md` line 31). `estimate.py` cannot separate recaptures from shared sources. Report m with shared-source-only recaptures removed beside it before any stratum is called closed; this needs an `estimate.py` column not written here.
- **zh newsletter links.** Hint-less zh rows go to core under batch 1's rule. weekly-newsletter-links is 64–65 of 162 zh rows per team, because it dominates the small zh cells (wasm: 25 of 28 frame rows). Class balancing caps it inside core but not in cells where it is most of the pool.
- **uk GitHub repos.** 7 of 20 uk rows per team are GitHub repos: code, never a Claim (rule 3). Expect mostly no-decision rows.
- **swift-interop.** The drop rule reads titles and paths. Any Rust Position in the body of a dropped Swift thread is lost; seven audited threads found none. 43 rows remain, and swift-interop is not drawn in batch 2.
- **Owner-ruled audit mechanics.** The one-miss whole-batch send-back (`fable-plan.md` line 167) is owner-ruled and unchanged, and at max(5, 10%) per team one borderline row still decides a team. The census removes the recorded failure mode, not the sensitivity.
- **Question identity.** The grain rule is fixed, but batch 2's merge may re-cut batch-1 canonical ids. Identity stability (`slice-1-review.md` line 131) should be measured from `merge-v3/crosswalk-b1.csv` against the batch-2 crosswalk before grading.
- **Correlated misses.** Misses shared by the two Claude teams stay invisible to both estimators (`fable-plan.md` line 178, § 9 T1).

## 6. Hashes of the files this preparation wrote (computed after the last edit)

| file | sha256 |
|---|---|
| `prompts/t2-extract.md` | `143907dc070fea3fd7b0074eb17e6c86bb1dc31b0ed694d38aed22b8dc39c73f` |
| `prompts/t3-fill.md` | `adc6e95dde30dd758309c1131f49c727d2cc92a26ca9db90ed424cc3b8f2935d` |
| `prompts/t4-merge.md` | `314d09e25a7bddc54c76ff7405668c35a35c8a2518b3921a060a998af21321b3` |
| `prompts/t4-fill-resolve.md` | `5e787782a02abee09cb67af24f130c9f0b35e01b0a5adb9a4360cfa9f8eabb1e` |
| `scripts/map/sample.py` | `f8c3be0c9ee4d3a6a5a51058ff8aa4b23364085dd5479efaddbc3e714b64eda5` |
| `scripts/map/prepare_frame.py` | `1a60c0ae220928e660cfce38d3fe84a727564f50352a915f67ccb3afe5cc8ec9` |
| `scripts/map/census.py` | `016a30aeb7b735d56b1451048d84b1524864fe3b55112581a36b5cdfdc5a5bf8` |
| `scripts/map/test_sample.py` | `d2d56241c1057aa5ee258d72911c96bc85fa4d0d884e96032edfe59e1e957cb1` |
| `scripts/map/test_census.py` | `b9ac74c7e617d09cbba82ed07ab87598b2118d47d5e271bf59b6cdeca8cd5860` |
| `frame/frame-swift-fix.md` | `687f5592b865c3c740668efe99db866d7e89ac55aedc73cb2b4ee4818b8d6686` |
| `frame/frame-swift-fix-drop.csv` | `2c79632e3437b8b71c54464b79ca4ced1977b2af47549d23fc02317213165e6f` |
| `samples/frame-b2-input.csv` | `17204ed5e3889715cd612ddf541411297b66597d6bdb2577b0699c38f78cf72d` |
| `samples/cells-b2.csv` | `5db7b3eaeca222acebf22ae19f3cc1c0b8d4546a2750e16ee74222c914e0ea09` |
| `samples/batch-2-team-a.csv` | `b6953c2821d64a02db709b28daff2a1df475edc3140515a86a937c3e4c5311b1` |
| `samples/batch-2-team-b.csv` | `0171e9a737d619750c6044effd215d672f899ce1bbd2f4223edfe434e36360d1` |
| `samples/batch-2.md` | `e913c9cfdc7eb12566fac93209fd8fa439cca1c1b75b40f35872d0430ec5c73c` |

`batch-2-prep.md` itself is not hashed here.
