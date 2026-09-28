# t1-union — instructions

Read RECON/prompts/common.md first; it binds you.

Inputs: every RECON/frame/frame-*-en.csv (English classes). Non-English CSVs (`-zh`, `-de`, `-uk`) form frame v2 later; do not include them. PLAN lines 96–98 (your row and the gate).

Task, scripted with `uv run python` (never by hand):
1. Read all English frame CSVs; validate each has the header `url,title,author_handle,date,language,class,domain_hints,transcript_available,window`; report any file that fails, and skip nothing silently.
2. Normalize URLs (scheme, trailing slash, `www.`, tracking params `utm_*`); dedupe across classes; a URL in several classes keeps all class names joined by `;` and the union of domain hints.
3. Keep only window=in rows for sampling; keep window=older rows in a separate file.
4. Assign frame ids `f000001…` in a stable order (sort by class, then date, then url).
5. Write RECON/frame/frame.csv (header: frame_id + the nine columns), RECON/frame/frame-older.csv, and RECON/frame/frame-stats.md: counts per class, per domain hint (strata ids from common.md), per hint-less; duplicates removed; per-file validation results; sha256 of frame.csv.

Scope: union only; no relevance judgment; no sampling.

End with a 3-sentence notification summary: total frame rows, per-stratum spread, sha256.
