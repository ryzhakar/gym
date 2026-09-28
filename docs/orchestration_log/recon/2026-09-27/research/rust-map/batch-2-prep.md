# Batch 2 preparation — Rust map

Preparer: r-batch2-prep, 2026-09-28. Prime directive: one bar for the whole batch, fixed before the first read. Every prompt a batch-2 agent reads is fixed by the sha256 below. Every changed or new prompt is headed "Frozen for batch 2 (2026-09-28)". No extraction, content judgment, edits under `maps/`, or git commands were used.

## 1. Frozen prompt set (sha256, 2026-09-28)

| file | state | sha256 |
|---|---|---|
| `prompts/common.md` | unchanged | `90961877fa257941967f51ab5d6e3dfefbf768ba7c978e718a2ab0c8298bfab5` |
| `prompts/t2-extract.md` | rewritten, frozen | see § 6 |
| `prompts/t3-fill.md` | rewritten, frozen | see § 6 |
| `prompts/t4-merge.md` | rewritten, frozen | see § 6 |
| `prompts/t4-fill-resolve.md` | rewritten, frozen | see § 6 |
| `prompts/t3-claim.md` | file names batch-scoped, frozen | see § 6 |
| `prompts/t3-voice.md` | file names batch-scoped plus one scope line, frozen | see § 6 |
| `prompts/t3-args.md` | chunk names batch-scoped, frozen | see § 6 |
| `prompts/t5-compile.md` | new, frozen | see § 6 |
| `prompts/t1-frame.md`, `t1-union.md` | not used in batch 2 | — |

## 2. Changes and their grounds

| # | change | where | ground |
|---|---|---|---|
| P1 | Rules 6–9 folded into one numbered list. Rule 8 now carries the lead's strike list (diagnoses, support requests, tentative plans, off-Question). Rule 9 says track record is never the extractor's test. | `prompts/t2-extract.md` § Rules | `audit/audit-b1-sendback.md` header (rule 6 re-worded mid-batch); `audit-b1-third.md` line 7 (rules 8–9 added); `strike-b1-third.md` lines 7–14 (strike list); `audit-b1-third.md` § Notes D1 (rule-9 misread by both teams); `slice-1-review.md` line 125 |
| P2 | The batch-1 audit bar, stated to the extractor | `t2-extract.md` § The audit bar | `audit-b1.md` line 51; `audit-b1-sendback.md` line 52; `audit-b1-third.md` lines 72, 74 (the third pass's bar, the latest; the earlier two are narrower wordings of the same bar) |
| P3 | One Nothing-new format, with `reason-code:` (off-subject, no-decision, no-rust-voice) and a `reason:` sentence that never cites missing opposition or counts Voices | `t2-extract.md` § Outputs | `audit-b1-sendback.md` line 122 (three formats in use); `audit-b1.md` line 12 (census 11/97 and 30/101 on the opposition ground) |
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
| P20 | Compile prompt: transcription in four stages (A entities and fill checks, B Voice pass, C Claim pass, D Arguments), each ending in a verbatim `check_map.py` run. `fill/checks-b2.csv` becomes `MAP/checks/<subject>.yaml` records. Existing Position summaries and tags are never overwritten; differences go to the lead. | `prompts/t5-compile.md` | lead dispatch 2026-09-28 item 4; `fable-plan.md` line 141; `compile/compile-b1.md` (batch 1's stages and mechanical rules, reused by name: `normalize_date`, `truncate_quote`, `classify_kind`, `slugify`); `check_map.py` lines 81–91, 189–191 (checks keyed by entity id; `agree` or a non-unresolved `resolution`) |
| P21 | Verification and argument outputs batch-scoped (`claims-final-b{n}.csv`, `voices-calibration-b{n}.md`, chunk names `b{n}-NN`). Without this, batch 2's adjudication would read batch 1's chunk files and overwrite `claims-final.csv`. | `prompts/t3-claim.md`, `t3-voice.md`, `t3-args.md` | the batch-1 prompts' fixed names (`t3-claim.md` adjudication, `t3-voice.md` calibration audit) |
| S4 | Sampler `--replace`: swaps listed rows for a draw from the same (language, hint, class) cell, excluding every row the team has drawn or had replaced. It is seeded and logged in `batch-n-team-T-replaced.csv`. The by-class draw now writes `batch-n-team-T-cells.csv`, recording which cell drew each row. | `scripts/map/sample.py`; `test_sample.py` | `fable-plan.md` line 111 ("re-sampled by the script"); lead dispatch 2026-09-28 item 2 |
| R1 | Prefetch: book-class rows are fetched as whole books (mdBook `print.html`, tried at the URL and up to two parent directories, else a table-of-contents crawl, now also through chapter-entry URLs and unquoted links). A rustcc.cn page that shows its comment section and footer passes below the 1,500-character floor. A book with no chapters is unreachable. YouTube rows get language-matched subtitles and 20 s spacing; a row answered with 429 gets its second, last try after a 600 s window. Client redirects written with reversed or unquoted meta attributes are followed. | `scripts/research/cache.py` | lead dispatch 2026-09-28 item 3; `slice-1-review.md` line 125; `audit-b1-third.md` line 132; `prefetch-b1.md` line 22 |
| R2 | Paywall list extended with pragprog.com, rheinwerk-verlag.de, dpunkt.de, pluralsight.com, udemy.com, coursera.org, educative.io, oreilly.com | `cache.py` PAYWALLED_DOMAINS | owner ruling in `prefetch-b1.md` lines 20, 26 (paywalled domains not attempted), applied to publisher and paid-course hosts |
| D1 | Batch 2 drawn: en core, ml, desktop-cli-ui, embedded, wasm at 18; the 9 zh cells with ≥ 18 rows at 18; uk and de as whole-language cells at 20 | `samples/batch-2.md` | `slice-1-review.md` line 123, targets (1), (5), (6); the lead's dispatch |

Test run, 2026-09-28: `uv run --with pytest pytest scripts/map/` gave 8 passed (7 sampler, including `--replace`; 1 census); `uv run --with pytest pytest scripts/research/test_cache.py` gave 6 passed. pytest is not a project dependency; `--with` adds it for the run only.

## 3. Batch 2 size

After replacements: 289 rows per team, 578 in all, 442 distinct frame ids (136 drawn by both teams). Every row has cached text (§ 8).
- en: 90 per team.
- zh: 162 per team.
- uk: 20 per team.
- de: 17 per team. The de books class had no row left for its three unreachable rows.

Draw seed `1311957526`; replacement seeds `1511926367`, `1284475788` and `621279008`. Details are in `samples/batch-2.md`.

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
| extraction | 40 | ⌈289/15⌉ = 20 per team (`fable-plan.md` line 108) |
| census fix | 2 | one fresh extractor per team. Batch 1's third-pass flag rate (1/47, 1/33; § 7) on about 130 nothing-new rows per team gives ≤ 3 flags each |
| audit | 2 | one per team: about 13 nothing-new re-reads, every drop, 20 Claims |
| merge + merge check | 2 | P12 |
| Claim verification | 8 | 7 at batch 1's ~166 Claims per run, plus 1 adjudicator |
| Voices | 5 | batch 1: 399 ids in 5 runs; zh, uk and de add mostly new ids |
| fills + resolve | 14 | batch 1's 8 runs for 772 Claims, scaled to about 12; resolver 1; fresh blind check 1 |
| arguments | 5 | batch 1: 4 |
| compile | 3 | stages A, B+C, D of `t5-compile.md`, one resumed agent per stage |
| base total | 81 | |

Contingent runs, each fixed in advance by the frozen rules:
- audit send-back: +21 per failed team (20 extractors and a re-audit). Batch 1 failed both teams on pass 1 and pass 2.
- full strike check: about +12 per team (~570 Claims at 50 per run).
- census at batch 1's first-pass flag rate (23%, 39%; § 7) instead of its third-pass rate: +6 (30–50 flagged rows per team, 3–4 fix runs each instead of 1).
- merge check < 90%: +2.

Worst case: 81 + 42 + 24 + 2 + 6 = 155.

Runs per unseen Question cannot be projected honestly. It depends on how many new canonical Questions batch 2 yields, and the English second draw and the first non-English draw have no yield history. Batch 1 gives about 4 seen Questions per run (399 from about 100 runs). After batch 2, compute runs ÷ (canonical ids in `merge-b2/crosswalk-b2.csv` absent from `merge-v3/crosswalk-b1.csv`).

## 5. What batch 2 cannot fix

Prerequisites closed by the lead's dispatch of 2026-09-28 (items 2–4):
- **Replacement.** 8 paywalled book rows and 16 prefetch-unreachable rows were replaced, or dropped when their cell was empty (S4, `samples/batch-2.md` § Replacements).
- **Compile.** `prompts/t5-compile.md` turns `fill/checks-b2.csv` into `MAP/checks/` records (P20). The validator's 417 FAILs (`slice-1-review.md` line 53) stay until stages B and C.
- **Prefetch.** Done; results in § 8.

Still open:
- **Bundler.** `scripts/research/bundle.py` and `books.py` hard-code batch 1: `samples/batch-1-team-*.csv`, `prefetch-b1-status.csv`, frozen slice numbers. Batch 2's extractors need a batch-2 bundle, and these scripts need a batch parameter before they can cut one. `bundle.py` also drops any text under 1,500 characters as thin, which would drop the 67 whole-but-short rustcc.cn pages the cache now accepts (R1). It needs the same `COMPLETE_PAGE_MARKERS` exemption. This is outside the dispatch's code scope (`cache.py` only).

Limits of the design that the numbers should be read against:
- **Strata that get no second English batch.** web, distributed, decentralized-iroh, frontend, cloud-workers and swift-interop are not drawn as English cells. The first four get zh-only reads plus incidental English rows through secondary hints (en web 17–18 rows per team). cloud-workers and swift-interop get almost nothing. `estimate.py` part 2 counts the batches present in a stratum's crosswalk rows, whatever cell drew them, so it can PASS for a stratum no batch-2 cell targeted. Read part 2 against `samples/batch-2.md`.
- **Languages pooled in one estimate.** Language is a reporting dimension (`fable-plan.md` line 34, OP2), so `estimate.py` pools zh and en captures per stratum. zh reads are a first batch and en reads a second, so catchability differs by language inside one estimate, which Chapman assumes away.
- **Class balancing makes inclusion unequal.** Rows in small classes are drawn close to whole: zh frontend 18 of 19 and 18 of 18; de 20 of 32. Frame ids drawn by both teams rose to 139 of 292 per team in the draw (en 28/90, zh 86/162), and 136 of 289 after replacements, against 17/198 in batch 1. A shared source gives both teams the same Questions, which raises m and lowers N̂, a bias toward closure. Batch 1 already showed the effect: one shared book carried 11 of 51 two-team Questions (`slice-1-review.md` line 31). `estimate.py` cannot separate recaptures from shared sources. Report m with shared-source-only recaptures removed beside it before any stratum is called closed; this needs an `estimate.py` column not written here.
- **zh newsletter links.** Hint-less zh rows go to core under batch 1's rule. weekly-newsletter-links is 64–65 of 162 zh rows per team, because it dominates the small zh cells (wasm: 25 of 28 frame rows). Class balancing caps it inside core but not in cells where it is most of the pool.
- **uk GitHub repos.** 7 of 20 uk rows per team are GitHub repos: code, never a Claim (rule 3). Expect mostly no-decision rows.
- **swift-interop.** The drop rule reads titles and paths. Any Rust Position in the body of a dropped Swift thread is lost; seven audited threads found none. 43 rows remain, and swift-interop is not drawn in batch 2.
- **Owner-ruled audit mechanics.** The one-miss whole-batch send-back (`fable-plan.md` line 167) is owner-ruled and unchanged, and at max(5, 10%) per team one borderline row still decides a team. The census removes the recorded failure mode, not the sensitivity.
- **Question identity.** The grain rule is fixed, but batch 2's merge may re-cut batch-1 canonical ids. Identity stability (`slice-1-review.md` line 131) should be measured from `merge-v3/crosswalk-b1.csv` against the batch-2 crosswalk before grading.
- **Correlated misses.** Misses shared by the two Claude teams stay invisible to both estimators (`fable-plan.md` line 178, § 9 T1).

- **Census is a phrase gate.** It does not re-read the source. A reason that avoids the listed phrasings but still rests on the forbidden ground passes it, so the audit remains the check (§ 7).

## 6. Hashes of the files this preparation wrote (computed after the last edit, 2026-09-28)

| file | sha256 |
|---|---|
| `prompts/t2-extract.md` | `4ee00bd528b56598a020435183472f81e302a6c252fd64279b503b8b8ba7b59d` |
| `prompts/t3-fill.md` | `adc6e95dde30dd758309c1131f49c727d2cc92a26ca9db90ed424cc3b8f2935d` |
| `prompts/t4-merge.md` | `ab889f51cb8dfb4754c7c9dd9abc84c6791591386b35525b5c4f22bfd71f6002` |
| `prompts/t4-fill-resolve.md` | `5e787782a02abee09cb67af24f130c9f0b35e01b0a5adb9a4360cfa9f8eabb1e` |
| `prompts/t3-claim.md` | `7d5e9099c9d6c565337d4a16959f70152016b1267b3da7b3bce2a8b3ed86d62b` |
| `prompts/t3-voice.md` | `7a6220e807ef3db5c69bd251a1f68f75cdb83320537f14e9c0406a0a953e5e9f` |
| `prompts/t3-args.md` | `9ea1fd96ebc5d9c88f21989f2bf4948c2cf0286363f1195e974df8cf40840835` |
| `prompts/t5-compile.md` | `2b7f87b841dd6621f748e4b2440b9269648398e412b72db2e4e6f4e4dcbdb096` |
| `scripts/map/sample.py` | `ca417b208aa5258c321fbb04c42fb08c8c2484e6038a8ed911e0545cb7c7cc9f` |
| `scripts/map/prepare_frame.py` | `1a60c0ae220928e660cfce38d3fe84a727564f50352a915f67ccb3afe5cc8ec9` |
| `scripts/map/census.py` | `e4aa9fded74a38cd62aa777a5372fa995e704a87abe15ac2286580c8ad441409` |
| `scripts/map/test_sample.py` | `e9a3acf9c9b66fc83cc824d8827f71182e827a69ba18ab1f11fc6bbb0c32369d` |
| `scripts/map/test_census.py` | `b9ac74c7e617d09cbba82ed07ab87598b2118d47d5e271bf59b6cdeca8cd5860` |
| `scripts/research/cache.py` | `ba0e6cfb0c4fdc073261867b99dc2558768698da8b2c34276561a9464715aaf6` |
| `scripts/research/test_cache.py` | `c497b57302eb8dbb94bf48e7a8c9d147596f94babc6c9a1bfe06067fff793f97` |
| `frame/frame-swift-fix.md` | `687f5592b865c3c740668efe99db866d7e89ac55aedc73cb2b4ee4818b8d6686` |
| `frame/frame-swift-fix-drop.csv` | `2c79632e3437b8b71c54464b79ca4ced1977b2af47549d23fc02317213165e6f` |
| `samples/frame-b2-input.csv` | `17204ed5e3889715cd612ddf541411297b66597d6bdb2577b0699c38f78cf72d` |
| `samples/cells-b2.csv` | `5db7b3eaeca222acebf22ae19f3cc1c0b8d4546a2750e16ee74222c914e0ea09` |
| `samples/batch-2-team-a.csv` | `0b81a50a7f3fc15609d93b0023bcf70e91ee3c6ac77cd1d4245d97b2aba2e02f` |
| `samples/batch-2-team-b.csv` | `ab11cb46b70798634f7c6f0b004453d278effc1b3aabf9e696490f44d428137f` |
| `samples/batch-2-team-a-cells.csv` | `5341242e4345f27757dd3408930b3372a9ff5c5e22c4890faeac5c799cdb2844` |
| `samples/batch-2-team-b-cells.csv` | `6ceefe5ee86bd3ae6b8eb4bd83d4c213f063bad7010cdde11c00e65d7bb4b8e3` |
| `samples/batch-2-team-a-replaced.csv` | `88e85b01185a763d5e36c500bef0f7be41a282585d03800a5cc724ce128b144a` |
| `samples/batch-2-team-b-replaced.csv` | `1da8febf1f2fe3279556e6ff81a025550833a50883c05b44fdbbb1737159ac93` |
| `samples/replace-b2-r1.csv` | `02491fae284b21fc187990de82231f4245e4895c6cd26ff0406aca546a8b1395` |
| `samples/replace-b2-r2.csv` | `71512afd160c0cb25ca0ed4dfb63e2076a20e7834f33cd61eb3679d501ffc26c` |
| `samples/replace-b2-r3.csv` | `068d3630a8d6825b5ec9354db28d48e76f9b2fcb3ae8ae305e974cce60bc6bcf` |
| `samples/prefetch-b2-input.csv` | `92d5f85244b1624e5556048e0586a60fd67143f30a31d7a19442f48105f0e128` |
| `samples/prefetch-b2-rerun.csv` | `ca1a85b744a3c1aed13a719fa398961e70c7a16df3d54a21a3e79ca688223ea3` |
| `samples/prefetch-b2-replacements.csv` | `492945083074a37a93c4f71cef312a8d41a42d75f37d86fb0b1686662b21e686` |
| `samples/prefetch-b2-status.csv` | `a6db44611d6b7d5d9bb9a7b8f160061a51f0a014affe8226140ecdffa89d97ae` |
| `samples/batch-2.md` | `698e1be9abbb18ce3d45623cdc9b6b79a4ee3fefeadb55a59b49f0b0dc0cec89` |

`batch-2-prep.md` itself is not hashed here. The draw's original team files (before replacements) were `b6953c28…` (a) and `0171e9a7…` (b); `samples/batch-2.md` gives the commands that re-derive the current files from them.

## 7. Census calibration on batch 1 (lead ruling 2026-09-28)

The lead allowed the census to run over `team-{a,b}/extract-b1-*.md` and `readlog-b1-*.csv`. Only counts and matched reason lines were read. Word matching is a gate, not the audit. It stops reasons that state the forbidden ground in its usual words before the audit draws. Whether a Nothing-new row hides a Position is decided only by the audit's re-read.

**Method.** Batch 1's reasons use the old formats: `### Nothing new` followed by text, a bare "Nothing new. Reason:", and "Not applicable" blocks. `census.py` as written flags all of them for a missing `reason-code:`, which is the intended format gate for batch 2. To calibrate the phrase test alone, a throwaway parser took the text of every Nothing-new block per section and applied the pattern to it.
- first pass: every file except `-sR*` and `-sT*`;
- send-back: `-sR*`;
- third pass: `-sT*`.

The parser counts every block, so its denominators run higher than the auditor's (102 against 97 for team A, 122 against 101 for team B).

**First pattern: rejected.** It banned every opposition word (disagree, debate, contested and others). It flagged 73 of 102 (A) and 81 of 122 (B) first-pass reasons against the auditor's 11 and 30. Most of its hits describe an off-subject topic ("a Swift Evolution thread debating syntax"), or use the plan skeleton's own allowed ground ("raises no contested point", `fable-plan.md` line 384).

**Adopted pattern** (`census.py` FORBIDDEN). It flags only reasons that cite missing opposition or count Voices: no disagreement, dispute, pushback or counter-argument; a competing, opposing or other Voice or view; single or one Voice; "against another …". It does not flag topic words or "contested".

| pass | team | reasons | flagged | auditor's census | auditor-named rows caught |
|---|---|---|---|---|---|
| first | a | 102 | 23 | 11 of 97 | — |
| first | b | 122 | 47 | 30 of 101 | — |
| send-back | a | 53 | 9 | 3 (f004169, f008237, f009704) | 3 of 3 |
| send-back | b | 50 | 7 | 2 (f002233, f002499), plus 1 false positive (f001246) | 2 of 2; f001246 also flagged |
| third | a | 47 | 1 (f002488 "no one takes a side") | — | — |
| third | b | 33 | 1 (f004371 "no Rust practitioners in disagreement") | — | — |

**Reading.**
- Recall on the 5 rows the auditors named is 5 of 5.
- The pattern flags about twice the auditor's count. The extra hits are reasons like "no disagreement appears" (f008381, f002542), which state the ground without naming a Voice.
- The frozen t2 prompt now bans exactly what the pattern flags (§ Outputs, reason sentence). Under it, a flag is a prompt violation, not a judgment call.
- The flag rate fell from 23–39% at the first pass to 2–3% at the third, after rule 6 was in force. The base projection (§ 4) uses the third-pass rate; the contingency uses the first-pass rate.

**Limits.**
- The auditor's census was itself a phrase match, never published as a pattern, so agreement on counts is not agreement on rows. Only the 5 named rows are checkable.
- A reason can rest on the forbidden ground in words the pattern does not list, and pass.
- The throwaway parser is not `census.py`'s parser, because the formats differ. `census.py`'s own parser is tested only on the batch-2 format (`test_census.py`).

## 8. Prefetch, batch 2 (2026-09-28)

`uv run python scripts/research/cache.py fetch-csv samples/prefetch-b2-input.csv samples/prefetch-b2-status.csv`, run over the 442 distinct ids of the 290-row draw; then the re-run and replacement passes below. The status file is append-only: the last line per id wins, as `bundle.py` reads it.

| pass | rows | fetched or cached | failed |
|---|---|---|---|
| main run (html first, YouTube last, 20 s apart) | 442 | 360 | 82 |
| re-run of rows failed by this preparer's own gates, not by the site (`prefetch-b2-rerun.csv`): 67 whole rustcc.cn pages under the length floor, 4 books entered at a chapter page | 71 | 70 | 1 (rust-lernen.de: a publisher page with no chapter text) |
| replacements of round 3 (`prefetch-b2-replacements.csv`) | 13 | 13 | 0 |

Final state: every one of the 578 row-draws (289 per team) has cached text.

Failed rows, each after its two genuine tries, were replaced in round 3:
- YouTube: 4 answered HTTP 429 on both tries, the second after the 600 s window; 1 has no subtitles (f015639, a conference trailer).
- Dead or unreachable hosts: polyfight.io (DNS), legendofworlds.com (TLS), a 404 at blog.sheerluck.dev, and a 403 at phoronix.com. No Wayback snapshot existed for any of them.
- Short pages under the floor on both html and Wayback: trynova.dev (804 chars) and ralfj.de/minirust-talk (903 chars). Both may be whole short pages; the floor treats them as stubs, as batch 1's did (`prefetch-b1.md` § Dropped).

Final routes: html 292, yt-dlp-subs 32 (plus replacements), discourse-json 25, gh-api-thread 24, wayback 18, book-print 15, gh-api-repo 15, browser 4, lobsters-json 3, book-crawl 2.

Limits:
- The rustcc.cn exemption tests that a page rendered whole (comment section and footer present), not that it holds anything.
- A `book-print` result found at a parent directory is that directory's book. For a chapter URL inside a larger site, that may be a wider book than the row named (lang-team design notes came back as the whole lang-team book).
- Transcripts are YouTube auto-captions: their locators are `[mm:ss]` markers every 60 s, and names and code in them are often garbled.
