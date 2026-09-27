# Rounds 6 and 7 — changes to t2-need.md (decided after audit/saturation-r5.md)

Rounds 6 and 7 run at the same time as two independent captures of the same population; their overlap is rule 2's estimate. Follow ROOT/prompts/t2-need.md in full, including step 10, with these changes:

1. Full population, no avoid-lists: derive queries from your need's row of PLAN §3 (lines 178–196) as a searcher who wants every relevant source, the obvious ones included. Never avoid a source or an angle because an earlier round may have found it.
2. Fresh eyes stay: do not read ROOT/needs/ and never open the other round's files.
3. Databases: OpenAlex is required (it is named in every field list): `https://api.openalex.org/works?search=<q>&per-page=50&mailto=gym-research@example.org`; on HTTP 429 sleep 40 s and retry, up to 5 times per query, and log each retry. Also Crossref, ERIC, PMC, arXiv. Sleep 1 s between other calls.
4. Grade every source in your `## Found DOIs` list with S, R, O: from full text where cached or reachable, else from the abstract with full_text_read=N and flag abstract-only. Read full text only for sources whose abstract grade is S≥3.
5. Text: get every source through `uv run python /Users/ryzhakar/pp/gym/scripts/research/cache.py get <doi-or-url>` first (see the "Source cache" section of ROOT/prompts/common.md).
6. Ledger rows: write CSV with Python's csv module (quoting every field that holds a comma); never hand-join fields.
