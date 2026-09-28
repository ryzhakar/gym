# t1 frame builder — instructions

Read RECON/prompts/common.md first. Directive variant: search freely for listing pages; log every URL.

Your prompt names CLASS, LANG (en), the PLAN row describing the class, and listing hints.

Task (PLAN lines 357–366, the t1 frame builder skeleton):
1. Enumerate EVERY item of the class from its listings. The frame is a population, not a reading list: never judge relevance.
2. Prefer APIs and machine listings (GitHub API, Discourse JSON, HN Algolia, repo contents, RSS/Atom, sitemaps). Script with `curl` and `uv run python` in /tmp scratch; never hand-type rows.
3. Window: items dated 2023-09-26 to 2026-09-27, plus older items only where the class is small (books, RFCs, survey) — mark `older` in a trailing column if outside the window.
4. Write RECON/frame/frame-CLASS-en.csv, header exactly:
   url,title,author_handle,date,language,class,domain_hints,transcript_available,window
   domain_hints: strata ids from common.md § Strata ids that the title, section or tags suggest, `;`-separated, or empty. transcript_available: yes|no|n/a. window: in|older.
5. Write RECON/frame/frame-CLASS-en.md: count, date range, listing method (commands/URLs), pages or endpoints that failed, where you stopped and why.

Be exhaustive. Partial listing = failure unless stated with reason.

End with a 3-sentence notification summary: count, window, failures.
