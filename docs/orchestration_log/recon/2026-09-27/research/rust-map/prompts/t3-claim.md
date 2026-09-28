# t3 claim verifier — instructions

Frozen for batch 2 (2026-09-28). Only file names changed from batch 1, so that batch n's files never overwrite batch 1's. Change log: RECON/batch-2-prep.md.

Read RECON/prompts/common.md first; it binds you. Directive variant: Tier 3 — read only each Claim's own Source; never search for another.

Your prompt names chunk files under RECON/verify/claim-chunks/, named `b{n}-NN` from batch 2 on, one Claim id per line. Work them in the order given; finish and write one chunk's output before starting the next. Do the work yourself; spawn no subagents.

Per Claim:
1. Read MAP/claims/<id>.yaml and its MAP/sources/<source>.yaml (url, title, date).
2. Fetch the Source through the cache first: `uv run python /Users/ryzhakar/pp/gym/scripts/research/cache.py get <url>`; fetch live only on a cache miss. Unreachable → verdict UNREACHABLE; never reconstruct from memory.
3. Go to the locator. Verdict:
   - CONFIRMED: the Voice said it, there, on that date, and the paraphrase and quote are faithful.
   - NOT-FOUND: nothing at or near the locator says it.
   - MISATTRIBUTED: someone said it, but not this Voice.
   - DATE-WRONG: said by the Voice, dated otherwise.
   - UNFAITHFUL: said by the Voice, but the paraphrase or quote says more or other than the source.
   Give the corrected locator, date, or a one-line faithful paraphrase where you can.
4. practiced: `unknown` by default. Check code only when the Claim declares a practice in code the Voice maintains and the Source or the Voice's MAP file names that repository: fetch it once; `true` if the code shows the practice, `gap` with url if it contradicts.

Output per chunk: RECON/verify/claims-<chunk>.md, one table:
| claim_id | verdict | corrected_locator | corrected_date | corrected_paraphrase | practiced | gap_url | note |
Every id in the chunk gets exactly one row.

Scope: write only your output files. Never edit MAP/. Never open RECON/team-a/, team-b/, merge*/, fill/, audit/.

Tools: Read, Grep, Glob, Bash (cache.py, `gh api`, `curl -s`), WebFetch on cache misses, Write.

After each chunk, notify in one line: chunk, counts per verdict. End with a 3-sentence summary.

## Adjudication (t3-claim-adjudicate)

Four verifiers applied the verdicts unevenly: misquotes, quotes absent from the source and wrong dates were passed as CONFIRMED with a note. Read every chunk output of the batch: RECON/verify/claims-b{n}-*.md (batch 1: claims-chunk-*.md). Build RECON/verify/claims-final-b{n}.csv (batch 1: claims-final.csv) with the header `claim_id,verdict,corrected_locator,corrected_date,corrected_paraphrase,drop_quote,practiced,gap_url,basis`, one row for each id in RECON/verify/claim-chunks/all-b{n}.txt (batch 1: all.txt). Apply the definitions above strictly:
- A quote that is absent from the source or not verbatim (an ellipsis joining one continuous passage is verbatim) → UNFAITHFUL, drop_quote=yes, and keep the paraphrase if it is faithful.
- A date differing from the source's own date for that statement → DATE-WRONG, with corrected_date.
- A locator off while the content is correct → CONFIRMED, with corrected_locator.
Re-check from the cache every row whose note or correction column is non-empty, plus a script-drawn random 10% of clean rows (seed logged). basis = `file` or `recheck`. Write RECON/verify/claims-adjudication-b{n}.md (batch 1: claims-adjudication.md) with: counts per verdict, rows changed from the chunk files and why, the disagreement rate on the random 10%, and the seed. If the rechecked random rows disagree with the files on more than 2 of them, say so first.
