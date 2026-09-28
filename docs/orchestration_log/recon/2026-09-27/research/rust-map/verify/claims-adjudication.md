# Claims adjudication

664 claims total (all 16 chunk files). Verdict counts, final:

| verdict | count |
|---|---|
| CONFIRMED | 648 |
| DATE-WRONG | 8 |
| UNFAITHFUL | 8 |

Original chunk-file counts (before any edit): CONFIRMED 656, DATE-WRONG 7, UNFAITHFUL 1. Net change: 8 rows moved off CONFIRMED (6 → UNFAITHFUL, 1 → DATE-WRONG, plus one row that was already UNFAITHFUL before this adjudication touched it — see below).

## Method

Recheck scope (per instructions): every row with a non-empty note or correction column (353 rows) plus a script-drawn random 10% of the 311 clean rows (31 rows, seed 20260927) — 384 rows total, marked `basis=recheck` in claims-final.csv; the remaining 280 rows are `basis=file`.

Two passes, both against the source cache (`scripts/research/cache.py get <url>`, re-fetching on a miss):

1. Automated: for every row in scope, split the claim's `quote` on `...`/`…`/`[...]`, normalize whitespace/quote-marks/markdown emphasis, and check each fragment against the cached source text (exact substring, then a 6-word prefix/suffix fallback to tolerate a quoter's own truncation at a fragment's edge). Flagged 74 of 384 as not-exact; a second pass narrowed that to 11 whose prefix and suffix both failed to match (the other 63 were markdown/link/backtick formatting artifacts of the extraction, confirmed by hand on a subsample).
2. Manual: every row whose note text itself hinted at a problem (regex over "not exact", "differs", "typo", "silently", "omit", "does not match", etc. — 14 hits across all verdicts), plus all 11 automated hold-outs, plus 3 full manual spot-checks (quote + date + locator) among the random-sample HITs — read directly against MAP/claims, MAP/sources and the cache text.

**Mid-adjudication correction.** claims-chunk-05.md, -06.md and -07.md were edited by their own verifier after this adjudication's first read of them (five rows moved CONFIRMED → UNFAITHFUL/DATE-WRONG). Re-read fresh on notice; one of the five (a-sa21-f011069-c1) was a row this adjudication had already independently flagged from the original file. All five were independently re-verified against the cache below rather than taken on trust.

## Rows changed and why

Eight CONFIRMED rows were misquotes or a wrong date passed with a note instead of a verdict — the failure mode this adjudication exists to catch. Two were caught here for the first time (chunk-04, untouched by any other edit); six had already been corrected in the chunk files by their own verifier and were independently re-verified against the cache, agreeing in every case:

Caught here (chunk-04, still CONFIRMED in the file at time of adjudication):
- **a-sa14-f005079-c2** (alexcrichton, wasmtime PR #14294): quote drops the source's leading "Personally" with no ellipsis marking the cut. Not verbatim → UNFAITHFUL, drop_quote=yes. Paraphrase unaffected, kept.
- **a-sa14-f005079-c6** (alexcrichton, same PR): source has the typo "therea re multiple TCP sockets"; the claim quote silently normalizes to "there are". Not verbatim → UNFAITHFUL, drop_quote=yes. Paraphrase unaffected, kept.

Already corrected in the file, independently confirmed against the cache:
- **a-sa21-f011069-c1** (aleksandr-petrosyan, EuroRust talk): "right? Well, no." is absent from the auto-caption transcript, which jumps from "The simple solution is usually right," straight to the next clause → UNFAITHFUL, drop_quote=yes.
- **a-sa24-f011220-c1** (james-eastham, conference talk): transcript at ~38:29–39:29 reads "...just consider serous see how that might help you" (auto-caption garble of "serverless"), not the clean word quoted → UNFAITHFUL, drop_quote=yes.
- **a-sa25-f011413-c1** (amos-fasterthanlime): transcript at ~02:09 reads "...run and memorize getting granting it full disk and network access just in case" — a genuine stuttered ASR rendering; the claim's "...[grant]" presents an editorial cleanup as an ellipsis over omitted text → UNFAITHFUL, drop_quote=yes.
- **a-sa25-f011413-c6** (amos-fasterthanlime, same talk): the Canada/lie wordplay at ~19:19–20:21 is introduced with "All of these are probably lies," not "microbenchmarks are always lies" — that stronger phrase occurs on its own, much earlier in the transcript. The claim's ellipsis splices two non-adjacent statements into one quote, changing the hedge → UNFAITHFUL, drop_quote=yes.
- **a-sa27-f012237-c2** (ian-wagner, Stadia Maps blog): page byline reads "Published: December 3, 2024," one day before the claim's stated 2024-12-04 → DATE-WRONG, corrected_date=2024-12-03.
- **a-saL2-f011092-c1** (luca-casonato, conference talk): transcript at ~34:25 reads "...that would cause our test weed to fail..." (auto-caption garble of "test suite"); the claim's "test [suite]" presents an editorial cleanup as an ellipsis over omitted text → UNFAITHFUL, drop_quote=yes.

All other notes and correction-column entries in the chunk files held up on recheck: the 7 pre-existing DATE-WRONG rows' corrected_date values were spot-checked against the actual comment/byline timestamp in 3 of 7, all matching; a-sa15-f005821-c1 (WASM benchmark causal overstatement, already UNFAITHFUL before this adjudication) and b-sb23-f009657-c1 (already CONFIRMED with corrected_locator filled in) needed no change. Several CONFIRMED rows carried notes about a quote's ellipsis spanning real distance in the source (a-sa18-f009104-c3, b-sR11-f004993-c2, a-saL1-f005454-c1, b-sb23-f011178-c1) or matching a source's own typo verbatim (a-sa20-f009698-c1, a-sa28-f012469-c4) — all confirmed as legitimate continuous-passage ellipses or intentional typo-preservation, not violations.

## Random-recheck disagreement

31 of 311 clean rows sampled (seed 20260927). 0 disagreed with the chunk-file verdict after recheck (0/31, 0%) — under the 2-row threshold, so no advance flag is warranted. 6 of the 31 were flagged MISS by the automated fragment check; all 6 resolved as formatting artifacts (markdown links, backticks, line-wrap) on manual cache inspection, matching source verbatim in substance.
