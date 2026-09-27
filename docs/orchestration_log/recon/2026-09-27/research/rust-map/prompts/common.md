# Rust map research — common instructions for every agent

RECON = /Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27/research/rust-map
PLAN = RECON/fable-plan.md
MAP = /Users/ryzhakar/pp/gym/maps/rust
GYM = /Users/ryzhakar/pp/gym

## Context

gym builds an opinion map of Rust: every Question where competent Rust practitioners disagree, with Positions pinned to dated Claims from real Voices. Architecture: GYM/docs/opinion-map.md. Rust scope: GYM/docs/subjects/rust.md. Target domains: GYM/docs/ground-truth.md § Target domains. Research question: PLAN lines 24–26. Strata: PLAN line 34.

## Strata ids (fixed; use exactly these)

web · distributed · decentralized-iroh · ml · desktop-cli-ui · swift-interop · frontend · cloud-workers · wasm · embedded · core · other

## Rules

1. Read PLAN lines 345–355 (directive block) and follow it, with the variant your prompt names.
2. Write only your output path(s); `mkdir -p` missing directories.
3. Never read other files under RECON, or anything under GYM/docs/orchestration_log/, unless your prompt names them. Team A never reads RECON/team-b/, team B never RECON/team-a/.
4. No verdicts, no recommendations on tradeoffs or taste.
5. No git commands that write.
6. Final message: 3-sentence summary suitable for a notification, naming your output path and counts.

## Tools

GitHub: always `gh api` (authenticated: 5000 requests/hour, search 30/minute; `gh api -X GET search/issues -f q='repo:X comments:>=20 created:>=2023-09-26' --paginate`; `gh api graphql` for Discussions). Never unauthenticated curl to api.github.com.

WebSearch, WebFetch, Read, Write, Bash for `mkdir -p`, `curl` against public APIs (GitHub, crates.io, Discourse JSON, YouTube listing pages) and `uv run python` for throwaway parsing.

## Source cache (durable; owner ruling 2026-09-27)

CACHE = /Users/ryzhakar/pp/gym/docs/orchestration_log/recon/cache/ — shared by every research and every round.
1. Before fetching any source, look it up: `grep -i "<doi-or-url>" CACHE/index.csv`. A hit: read CACHE/<key>.txt; never fetch it again.
2. After any successful fetch, save the full text before using it: key = DOI lowercased with `/` → `_`, or for a URL without DOI the first 12 hex of `sha1(url)`; text to CACHE/<key>.txt (pdftotext -layout for PDFs; readable text for HTML, transcripts for talks); append one row to CACHE/index.csv: `key,doi_or_url,route,fetched_at,agent,chars`.
3. Once `scripts/research/cache.py` exists, use `uv run python /Users/ryzhakar/pp/gym/scripts/research/cache.py get <doi-or-url>` instead; it does 1–2 and prints the text path.
4. Abstract-only text is saved as CACHE/<key>.abstract.txt with route `abstract`; it never counts as full text.
