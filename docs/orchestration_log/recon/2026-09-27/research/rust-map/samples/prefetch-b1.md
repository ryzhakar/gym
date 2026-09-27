Constitution: stop-yapping, simple-made-easy, cargo-cult-science — bound, per teammate directive. Fragments below, not prose; every failure and false-positive found is disclosed, not smoothed over.

# Prefetch — batch 1

Script: `scripts/research/cache.py`. Cache: `docs/orchestration_log/recon/cache/` (shared, append-only index). Status CSV: `docs/orchestration_log/recon/2026-09-27/research/rust-map/samples/prefetch-b1-status.csv`.

## Per-team counts

| team | cached (hit) | fetched (new) | dropped (stub/thin) | failed | rows |
|---|---|---|---|---|---|
| team-a | 179 | 3 | 4 | 12 | 198 |
| team-b | 17 | 177 | 1 | 3 | 198 |
| **total** | 196 | 180 | 5 | 15 | 396 |

`cached` = URL already in the shared index (ingest-tmp, `get` tests, or the other team's identical row). `dropped` = text fetched but rejected by the stub/thin-content gate (below). `failed` = every route for that URL exhausted.

## Failed, by class and reason

team-a (12):
- books-courses × 5 — packtpub.com, amazon.com, manning.com, leanpub.com, edx.org: paywalled domain, not attempted (owner ruling — not a scraping project)
- books-courses × 1 — nalgebra.org/docs: DNS `NXDOMAIN`-equivalent (`nodename nor servname provided`) + no Wayback snapshot on retry (html, wayback, browser: 3 tries)
- talks × 5 — YouTube auto-subs, all `yt-dlp: HTTP Error 429: Too Many Requests`; retried after a delay, still 429 (2 tries; YouTube-side throttle, not a structural block)
- twir-links × 1 — rust-lang.zulipchat.com deep link: html/wayback/browser all ran (3 tries); browser rendered the app shell only, no thread text — see "False positive found" below

team-b (3):
- books-courses × 2 — manning.com, linkedin.com/learning: paywalled domain, not attempted
- individual-blogs;twir-links × 1 — gamedev.rs: domain is dead (`NXDOMAIN`); html + wayback both tried

Two-genuine-tries budget held everywhere except the DOI chain (which was always multi-hop by design) and the html/wayback/browser cascade (3 steps, since browser is a cheap last resort, not a scrape retry).

## Dropped (stub/thin-content gate)

5 rows had real, on-topic text fetched but under the 1,500-char floor (§ below): `nogibjj.github.io/rust-tutorial` (973), `artificialworlds.net/.../error-handling` (1147), `artificialworlds.net/.../jezpuck-1` (988), `rustacean-station.org/episode/jonathan-kelley` (1098), `notes.eatonphil.com/.../datafusion-53` (349, itself a redirect stub to an external post never followed further). Manual read of the first four confirmed genuine short articles, not stubs — the length floor is deliberately conservative per the owner's defect-fix ruling and over-rejects some legitimate short pages. Flagged here rather than silently lost.

## ingest-tmp

Ran against the 64 PDFs present in `/tmp` at run time. Two genuine tries per PDF: (1) regex-search the first ~6000 chars of `pdftotext -layout` output for a DOI, taking the longest match (a PDF had a line-wrapped, truncated DOI earlier in the text — fixed to prefer the fullest match); (2) if no DOI, check whether the filename itself is an arXiv id (`\d{4}\.\d{4,5}`) and derive `10.48550/arXiv.<id>` — arXiv registers that DOI for every paper since Feb 2022, so this is provenance, not scraping.

- Ingested: 20 (17 by in-text DOI, 3 by filename arXiv-id)
- Skipped: 44 (no DOI in text, filename not an arXiv id) — left for an agent to identify by hand

## Cache state

- 414 index rows, 15M on disk
- Route mix: html 163, gh-api-thread 114, discourse-json 40, tmp-ingest 22, yt-dlp-subs 18, browser 11, unpaywall 9, gh-api-repo 8, abstract 8, wayback 8, lobsters-json 6, europe-pmc 3, arxiv 1, semantic-scholar 1, plus 2 rows (`pmc`, `figshare-pdf`) written by other agents sharing this cache
- `get` tested on 3 DOIs before the batch run: 2 full-text hits (unpaywall; arXiv-derived-DOI), 1 honest no-OA failure (`10.1038/nphys1170` — no Unpaywall location, no arXiv match, no Semantic Scholar OA/abstract)
- `fetch-csv` smoke-tested on 10 mixed-class rows before the full run

## Defects found and fixed mid-run

1. **arXiv API 406**: an encoded `:` in the search-query URL tripped arXiv's edge WAF. Fixed by leaving `:` and `/` unescaped (`quote(..., safe=":/")`), matching arXiv's own query examples. Also added a 3s backoff-and-retry once, since arXiv's export API rate-limits at roughly 1 req/3s.
2. **Client-side redirects invisible to urllib**: `blog.rust-lang.org` (missing trailing slash) and `rtic.rs` (a two-hop stub-page chain) both serve a 200 page whose body redirects via JS/meta-refresh. Fixed with a redirect-chain follower (up to 4 hops, cycle-guarded) run after every raw fetch.
3. **Reddit's own anti-bot wall**: `reddit.com` and `old.reddit.com` both 403 ("whoa there, pardner") for automated `.json` fetches from this sandbox's egress. No further reddit-specific route exists; falls through to the browser fallback (works — see below).
4. **PDF DOI mis-extraction**: one PLOS PDF had a line-wrapped, truncated `10.1371/journal.` earlier in the text than the real `10.1371/journal.pone.0153490`. `ingest-tmp` now takes the longest DOI match in the scanned window, not the first.

## Scope addition: mirrors + headless browser (owner ruling, mid-run)

Added to the `get`/DOI chain, in order after Unpaywall/arXiv/Semantic Scholar: **Europe PMC** (search by DOI, then `fullTextXML` for the PMC full text) and **OpenAlex** (`oa_url` / `best_oa_location.pdf_url` / `locations[].pdf_url`) — both verified working on a live DOI (51,664 and 82,724 chars respectively). **CORE** added but self-skips immediately (`no CORE_API_KEY configured`) — no key was provisioned; a real try would need one.

**Headless browser** (Playwright + Chromium, installed via `uv add playwright` + `uv run playwright install chromium`, both succeeded): kept, not dropped — it rendered a plain page (`example.com`) correctly on the first try, then rescued 8 of the 18 stub cases below, including reddit (`old.reddit.com` bot-wall bypassed by rendering the actual page; got real title/post/top-comment text). It is now the last-resort step in the DOI chain (rendering `doi.org/<doi>`), in `route_html` (after direct fetch + Wayback both fail), and in `route_reddit` (after both JSON hosts 403).

Caveat found while validating it: on `rust-lang.zulipchat.com`'s deep-link URL, the browser rendered only the app shell (settings menu, "No matches") — no actual thread text, because the anonymous/web-public render never resolved the `#narrow/.../near/<id>` hash route in the time budget. That entry was deleted rather than kept as a false "success" (see below).

## Defect found and fixed: bot-wall/login-wall stubs saved as if they were real text

A surveyor caught `cache.py` saving a Cloudflare/loading-shell page as if it were the source's full text (`10.1038/s41598-024-65753-3`, saved via `unpaywall` at 226 chars — since overwritten by another agent's manual `pmc`-route fetch, 142,321 chars, so that specific DOI's cached text is fine now; only the stale 226-char index row was the defect).

**Fix**: a `validate_page_text()` gate, run on every whole-page HTML-derived fetch (`route_html`, the HTML branch of `fetch_pdf_or_html` used by the DOI mirrors, Wayback, Europe PMC's XML, and the browser route) — never on routes whose real content is naturally short (a single Reddit comment, a GitHub PR title, an abstract, one Discourse post folded into a longer thread). Rejects and falls through to the next route if:
- text matches a known challenge/login-wall marker (`cf-browser-verification`, `enable javascript and cookies to continue`, `checking your browser before accessing`, `attention required! | cloudflare`, `just a moment...` — the last kept its literal ellipsis, since without it the phrase also occurs in ordinary prose and false-positived on one real article), or
- text is under 1,500 chars from an HTML-producing route.

Also fixed `find_cached()` to return the **last** matching index row, not the first — the index is append-only and shared by many concurrent agents, so a later correction (like the manual `pmc` re-fetch above) must supersede an earlier bad row for the same source.

**Rescan of the full shared cache** (414 rows, all agents' contributions, not just this run's): 18 stub/thin-content matches by the new gate.

- Re-fetched all 18 via `get` (delete text + index row, refetch): **8 fully recovered** with real content, mostly via the new browser fallback — `rtic.rs` (11,754 chars), `mastodon.social/@kornel` toot (1,575), `kerkour.com` blog (12,325), `mathstodon.xyz/@andreasthom` toot (5,333), a LinkedIn post (17,889, via Wayback), plus 3 DOIs recovered as an abstract or a real (if paywalled) landing page (`10.31234/osf.io/yaxvw` abstract, `10.1037/xlm0000251` and `10.1037/e480982008-001` PsycNet pages).
- **1 false "recovery" caught and reverted**: the Zulip deep link (see caveat above) passed the 1,500-char floor on UI chrome alone (settings menu, "No matches") while carrying zero real thread text. Deleted rather than kept; recorded as `failed`, not `dropped`, since no usable text was ever produced.
- **9 confirmed still-unreachable** after every route: `nalgebra.org/docs` (DNS + no Wayback snapshot), `10.1016/j.edurev.2023.100537` (11 chars, real abstract never found), `10.35542/osf.io/fse72_v1` (OSF JS shell, no mirror had it), `10.5465/ambpp.2015.17679abstract` (browser hit a login wall — marker match), and the 5 `dropped`-not-`failed` cases already listed above (real short content, held to a stricter bar).
- **2 marker false-positives identified and excluded from the rescan** (not deleted — genuinely fine): a Rust unions blog post (13,975 chars; matched on "...in **just a moment**, its memory layout..." in ordinary prose) and a YouTube subtitle track (256,207 chars; matched on spoken "...view in **just a moment** so I just wanted..."). Confirmed by finding the exact match context before trusting the flag.

`prefetch-b1-status.csv` updated for every affected batch row: 5 flipped to `fetched` (rtic.rs, the two toots, kerkour, LinkedIn), 5 flipped to `dropped` (thin-content, listed above), 2 flipped to `failed` (nalgebra, Zulip).

Net after all fixes: cache rescanned clean — **0 remaining bot-wall/thin-content matches** out of 414 rows.

## Bundles

`scripts/research/bundle.py <team-a|team-b>`. Per row: keep only if cached text exists, isn't a bot/login stub (`CHALLENGE_MARKERS`, reused from `cache.py`), and is ≥1,500 chars — else `dropped` with one reason (`no-text`, `stub`, `thin`, `off-subject`). Kept rows cut in CSV order into ≈150k-char slices, never splitting a source; an oversized source becomes its own slice, truncated at 150,000 chars with a marker line. Team-a's data rows 1–30 excluded (already extracted elsewhere) — not counted below.

**Off-subject rule, corrected (round 1).** First pass dropped anything mentioning "rust" fewer than 3 times, which threw out 64 real Rust sources that just don't repeat the word much (candle/esp-hal/probe-rs/uniffi-rs GitHub issues, iroh.computer posts, etc. — flagged by a surveyor). Fixed: a row is `off-subject` only when it has **zero** "rust" mentions *and* its URL isn't a `github.com` URL, a `*.rs` / `docs.rs` / `crates.io` host, or one of this batch's own `class=domain-subframes` hosts. Everything else with real text is kept, regardless of mention count.

**GitHub/Discourse/reddit attribution (round 2).** Cached GitHub issue/PR text had no comment authors, so an extractor couldn't name a Claim's Voice without an extra `gh api` call. Fixed in `cache.py`: every GitHub issue/PR body and comment (including inline PR review comments, now fetched too), every Discourse post, and every reddit comment/post is now prefixed `@<login-or-username-or-author> · <created_at>:` before being saved. Re-fetched all 154 batch-1 rows that had used the `gh-api-thread` or `discourse-json` route (no `reddit-json` rows existed yet — reddit is still blocked at the JSON-API level for this egress, see above; only its browser-rendered fallback has succeeded so far, and that path doesn't carry structured per-comment authors).

**forums.swift.org rule (round 3).** Swift-internal threads with a passing Rust comparison produced zero Questions in every slice read, so `forums.swift.org` rows are now held to their own bar: kept only with ≥3 "rust" mentions, dropped as `off-subject` otherwise — overriding the domain-subframes pass-through above for this one host specifically.

**Frozen slices.** Team-a slices 01–04 and team-b slices 01–02 were already assigned to an extractor and are left untouched (files and manifest rows unchanged) through all three rounds above; only unassigned rows were reclassified against the current rules and re-fetched text, then packed into new slices numbered after the frozen range (team-a from 05, team-b from 03).

| team | rows total | frozen (untouched) | kept | dropped | no-text | stub | thin | off-subject (of which swift-forum) | new slices |
|---|---|---|---|---|---|---|---|---|---|
| team-a | 168 (30 excluded) | 29 | 157 | 11 | 8 | 0 | 1 | 2 (2) | 28 (05–32) |
| team-b | 198 | 6 | 189 | 9 | 3 | 0 | 0 | 6 (6) | 32 (03–34) |

All 8 off-subject drops in this round are forums.swift.org rows caught by the new host-specific rule — the general zero-mention/domain-subframes rule alone produced 0 off-subject drops among the unassigned rows, same as round 1. `no-text`/`thin` counts shifted slightly from round 1 (team-a: 9→8 no-text, 7→1 thin) because the re-fetch itself pulled fuller GitHub/Discourse threads for a few rows that had incomplete data before.

Output: `samples/bundles/b1-{team}-{jj}.txt` (66 files total, including the 6 frozen: team-a 32, team-b 34), `samples/bundles/b1-team-a-manifest.csv`, `samples/bundles/b1-team-b-manifest.csv` (frozen rows unchanged in place, all other rows replaced).

**Talk transcript truncation (round 5).** Talks were hitting the 150k-char slice cap at 26–34 minutes into much longer recordings (`a-21` EuroRust, `a-22` Deno talk, flagged by a surveyor). Root cause, confirmed by inspecting a raw `.vtt`: YouTube's auto-captions are "rolling" — each cue repeats the previous settled line, then grows a new line word by word with inline `<00:00:09.230><c>word</c>` timing tags. The old code only stripped full `-->` timing lines and did an exact-line `dict.fromkeys` dedup; it never touched the inline tags, so the same phrase resurfaced 5–10x as slightly different (still-growing) strings that dedup couldn't catch, burning through the char budget on near-duplicate noise long before the talk was over.

Fix in `cache.py` (`vtt_to_text`, replacing the old inline stripping in `route_video`): a cue's last line is "settled" — one clean, complete phrase — once it stops growing (no inline tags left on it); every settled line appears exactly once, in cue order, so collecting only those reconstructs the full transcript with no duplication and no gaps, plus a `[mm:ss]` marker roughly every 60s. Verified live on the EuroRust talk (`LO7tvIed-YQ`, 37:06 runtime): old approach would have kept truncating well short; new output is 31,564 chars, ends at `[36:01]` with "Thank you for your time" — the actual end of the talk, not a cutoff.

Re-fetched every video URL in both batches: 20 `class=talks` rows plus 3 more tagged only `twir-links` that also happen to be `youtube.com` links (the defect is about the URL, not the class label — caught one of these, `f012428`, still truncated in a freshly-built slice on the first bundle pass, which is what surfaced the gap). 19 of 23 succeeded, all now 9,894–49,691 chars (nowhere near the cap); 4 EuroRust/RustConf videos still hit YouTube's own subtitle-endpoint rate limit (`HTTP 429`) on both the original attempt and this re-fetch — the same persistent, structural throttle noted in round 1, not something this fix touches.

Freeze widened to team-a slices 01–25 (+L1) and team-b 01–20. `bundle.py`'s supplement mechanism is now a small ordered list of (name, predicate) rules instead of one hardcoded `L1`/`hn-lobsters` case, so adding the talk-truncation rule was a one-line addition: a frozen `class=talks` row whose *frozen* manifest `chars` exceeded 150,000 (i.e. it was truncated) goes to `L2`. A row stays "sticky" to its assigned supplement on every future rerun even if fresher text would no longer match the original predicate (a fixed talk's char count drops back under 150k) — needed once `is_frozen_slice`/the claim logic had to treat `L2` the same way it already treated `L1`.

team-a has 4 `L2` rows — exactly the EuroRust/Deno-family videos named, all now complete, no truncation marker. team-b has 0: its truncated talks (5 of them, in what were slices 25/27/28/29/31) were still in the *unassigned* range under the new freeze boundary, so they were simply reclassified and repacked fresh this round rather than needing a supplement. One truncation remains anywhere in the corpus: `users.rust-lang.org/t/twir-quote-of-the-week` (`f012469`, team-a slice 28) — a genuinely large Discourse thread, unrelated to this defect, left as designed (an oversized source becomes its own truncated slice).

| team | rows total | frozen (incl. supplemented) | kept | dropped | no-text | stub | thin | off-subject | new slices | L1 | L2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| team-a | 168 (30 excluded) | 139 | 158 | 10 | 7 | 0 | 1 | 2 | 5 (26–30) | 11 | 4 |
| team-b | 198 | 151 | 189 | 9 | 3 | 0 | 0 | 6 | 6 (21–26) | 19 | 0 |

`no-text` dropped by one for team-a (8→7) versus round 4 because one of the 3 previously-429'd talk rows in that team's unassigned range happened to succeed on this attempt. team-b's L1 count grew from 0 to 19 as a side effect of the wider freeze alone — all 19 of its `hn-lobsters`-class rows now sit in the newly-frozen 17–20 range and get swept in by the existing L1 rule, nothing new to re-fetch there.

Output: 59 `.txt` files total (team-a 32: 30 numbered including 4 now-orphaned-but-untouched old slices + `L1` + `L2`; team-b 27: 26 numbered + `L1`), both manifests updated (frozen numeric rows untouched; `L1`/`L2` rows' `slice` and `chars` columns repointed to the fresher copy).

**lobste.rs/HN attribution + wider freeze (round 4).** `lobsters-json` carried comment text with no username (`row f005516`, in slice a-15, flagged by a surveyor); the same gap existed for a Hacker News route that didn't exist yet. Fixed in `cache.py`: `route_lobsters` now reads lobste.rs's own JSON fields (`commenting_user`/`created_at`, `submitter_user` for the story) instead of the unattributed HTML scrape it fell back to before; a new `route_hn` fetches `hn.algolia.com/api/v1/items/<id>` (`author`/`created_at`) for `news.ycombinator.com` URLs, wired into `fetch_by_class_route`. Both use the same `@<login> · <date>:` prefix as GitHub/Discourse/reddit. No `news.ycombinator.com` URL actually appears in either batch-1 CSV, so the HN route is provisioned but untested against batch data; verified live instead against `hn.algolia.com/api/v1/items/1` (Aug '06 PG/sama thread) — correct authors and dates.

Re-fetched the 6 lobste.rs rows in scope (3 per team; `get` was tried first and found to route generic URLs through `route_html`, bypassing the fix entirely — switched to calling `fetch_by_class_route` directly, which dispatches correctly). All 6 now save via `lobsters-json` with real usernames (spot-checked: 54 `@` lines in the `f005516` capture).

Freeze widened to team-a slices 01–20 and team-b slices 01–16 (what was "new" in round 3 is now frozen too). Of the frozen rows, every `class=hn-lobsters` row — not just the 3 re-fetched lobste.rs ones, the whole class, per the instruction — gets its current cached text written to a supplementary `b1-{team}-L1.txt`, with its manifest `slice` column repointed to `L1` (`chars` updated to match; the original numbered slice file is left exactly as it was). Team-a has 11 such rows (3 lobste.rs + 8 already-fine mastodon/blog/GitHub rows carried along for a single lookup location); team-b has 0, because its 3 lobste.rs rows already sat above the new frozen_max (slices 18–19) and were simply reclassified and repacked as ordinary unassigned rows.

| team | rows total | frozen (incl. L1-supplemented) | kept | dropped | no-text | stub | thin | off-subject | new slices | L1 rows |
|---|---|---|---|---|---|---|---|---|---|---|
| team-a | 168 (30 excluded) | 134 | 157 | 11 | 8 | 0 | 1 | 2 | 12 (21–32) | 11 |
| team-b | 198 | 113 | 189 | 9 | 3 | 0 | 0 | 6 | 18 (17–34) | 0 |

kept/dropped totals are unchanged from round 3 for both teams — this round only re-routed *where* the 6 lobste.rs rows' text lives (all were already `kept` before and after; the fresher text didn't cross the 1,500-char or "rust" thresholds either way).

A rerun-safety bug caught before it shipped: `load_frozen()` parsed every `slice` value as `int(...)`, which crashes on a manifest that already contains `"L1"` from a prior run of this same script — fixed to treat `L1` as frozen-forever, and fixed the stale-slice-file cleanup loop (same `int()` assumption) to skip non-numeric slice filenames like `b1-team-a-L1.txt`.

Output: 67 `.txt` files total (team-a 32 numbered + 1 `L1`, team-b 34 numbered), manifests updated in place (frozen numeric rows still untouched; only the 11 team-a `hn-lobsters` rows had their `slice`/`chars` columns repointed to `L1`).
