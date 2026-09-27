# Teaching research — common instructions for every agent

ROOT = /Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27/research/teaching/
PLAN = ROOT/fable-plan.md

## Context

gym trains people in CS-adjacent hard skills with LLM trainers. This research builds an evidence map of teaching and coaching methods that produce skill done unaided and lasting, and how each transfers onto an LLM substrate. Research question: PLAN lines 60–66. Not a design.

## Rules

1. Read PLAN lines 264–287 (PRINCIPLES, DO NOT) and follow them. Where you grade, read PLAN lines 198–239 (S, R, O, snake-oil) and apply them verbatim.
2. Write only your output path(s); `mkdir -p` missing directories. Ledger CSVs (ROOT/ledger/) only where your prompt says append; append, never edit.
3. Never read ROOT/seed.md, /Users/ryzhakar/pp/gym/docs/orchestration_log/history/, /Users/ryzhakar/pp/gym/docs/subjects/, or other files under recon/ — unless your prompt names them.
4. Subject-neutral: no programming language, framework or tool name as a frame.
5. No git commands that write.
6. Final message: 3-sentence summary suitable for a notification, naming your output path and counts (entries, queries, full texts read).

## Tools

WebSearch, WebFetch (OpenAlex, ERIC, Crossref, Unpaywall, arXiv, PMC, OSF, HN Algolia — endpoints PLAN lines 46–58), Read, Write, Bash for `mkdir -p` and `curl` against those APIs.

Full text, the working route: `curl -s "https://api.unpaywall.org/v2/<DOI>?email=gym-research@example.org"` → `best_oa_location.url_for_pdf` → `curl -sL -o /tmp/<id>.pdf <url>` → `pdftotext -layout /tmp/<id>.pdf - | less` (poppler's pdftotext is installed at /opt/homebrew/bin/pdftotext). Also arXiv PDFs, PMC `https://www.ncbi.nlm.nih.gov/pmc/articles/<PMCID>/`, author pages, Semantic Scholar per-DOI `openAccessPdf`. OpenAlex is rate-limited on this IP: use Crossref and Unpaywall first.

## Prime directive

Evidence from primary sources, resolved citations, honest `full_text_read`. Report evidence, not conclusions. An unresolvable citation is not a citation.

## Source cache (durable; owner ruling 2026-09-27)

CACHE = /Users/ryzhakar/pp/gym/docs/orchestration_log/recon/cache/ — shared by every research and every round.
1. Before fetching any source, look it up: `grep -i "<doi-or-url>" CACHE/index.csv`. A hit: read CACHE/<key>.txt; never fetch it again.
2. After any successful fetch, save the full text before using it: key = DOI lowercased with `/` → `_`, or for a URL without DOI the first 12 hex of `sha1(url)`; text to CACHE/<key>.txt (pdftotext -layout for PDFs; readable text for HTML, transcripts for talks); append one row to CACHE/index.csv: `key,doi_or_url,route,fetched_at,agent,chars`.
3. Once `scripts/research/cache.py` exists, use `uv run python /Users/ryzhakar/pp/gym/scripts/research/cache.py get <doi-or-url>` instead; it does 1–2 and prints the text path.
4. Abstract-only text is saved as CACHE/<key>.abstract.txt with route `abstract`; it never counts as full text.
