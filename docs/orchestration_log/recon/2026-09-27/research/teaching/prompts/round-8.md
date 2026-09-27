# Round 8 — script capture (decided 2026-09-27 under the owner's 2026-09-26 handover)

Two independent captures per need (8a, 8b), then one reader per need.

## Query writer (one agent per need per capture)
1. Read only: PLAN §3 lines 178–196 (your need's row), ROOT/context/rulings-brief.md, ROOT/index/index.md section names. Never read ROOT/needs/, ROOT/ledger/, ROOT/audit/, or the other capture's file.
2. Write 25–40 queries a searcher would run to find every relevant source for the need, the obvious ones included; vary vocabulary across fields (education, cs-education, expertise, coaching, ai-tutoring, adult-skill). Format per `uv run python /Users/ryzhakar/pp/gym/scripts/research/search.py --help`.
3. Output: ROOT/capture/r8{a|b}/n{k}-queries.txt. Nothing else.

## Search (script, orchestrator runs it)
`search.py run` then `search.py found` per query file → ROOT/capture/r8{a|b}/n{k}-results.csv and n{k}-found.md.

## Reader (one agent per need, after both captures)
1. Inputs: both n{k}-found.md files and their results CSVs (abstracts included).
2. Grade every `new` id S/R/O (PLAN lines 198–239) from the abstract; for S≥3 get full text via cache.py and grade from it. Append sources.csv rows (csv module; round 8; found_by_agent = your name; needs = N{k}).
3. For each new S≥3 source read in full, write claims per t2-need.md step 9 into claims.csv (claim_id N{k}-r8-nn), and a report ROOT/needs/n{k}-r8.md: search log = the two query files and result counts; claims by axis; Found DOIs = the union, each line tagged `8a`, `8b` or `8a 8b`.

## Screener (one agent per need, after each search pass)
1. Read only: PLAN §3 lines 178–196 (your need's row), ROOT/context/rulings-brief.md, and ROOT/capture/r8-screen/n{k}-screen.csv (doi,title,year,in_ledger — no capture column; never look for which capture found a row).
2. Label every row: `relevant` = Y when the title (and year) plausibly reports evidence or a method the need's decision would use, for any learner population; N otherwise; U when the title alone cannot tell. Judge by the need row, never by what earlier rounds found.
3. Write ROOT/capture/r8-screen/n{k}-labels.csv (doi,relevant) with Python's csv module, every row labeled; work through the file in chunks of ~300 rows.
4. Report counts Y/N/U. Then run `uv run python /Users/ryzhakar/pp/gym/scripts/research/search.py tally` on your labels (Y only) and the two result files ROOT/capture/r8a/n{k}-results.csv, ROOT/capture/r8b/n{k}-results.csv, and paste its output.
