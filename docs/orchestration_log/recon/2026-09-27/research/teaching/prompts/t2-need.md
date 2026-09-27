# t2 need surveyor — instructions

Read ROOT/prompts/common.md first; it binds you.

Your prompt names the need Nk, the round r, and the index field sections to start from.

1. Need definitions: PLAN lines 178–196 (§3). Your need's row is the decision you serve; stay inside it.
2. Skeleton and report format: PLAN lines 316–340 (t2-need surveyor). Follow it exactly: search log, calibration grades, claims by axis (four axes, each with rows or "No evidence found. Queries: …"), disagreements, excluded, not read, out of scope seen.
3. Grading: PLAN lines 198–239, verbatim. Every source graded S, R, O.
4. Context: ROOT/context/rulings-brief.md (read first). N3 and N7 also read ROOT/context/substrate-audit.md.
5. Inputs: ROOT/index/index.md (your named sections; starting point, not boundary), ROOT/index/exclusion-register.md, ROOT/verify/calibration-set.md (grade its 5 sources first).
6. Ledgers: append rows to ROOT/ledger/sources.csv and ROOT/ledger/claims.csv with the headers at PLAN lines 98–99. Append with `>>` in one write per batch of rows; never rewrite the files. claim_id = `Nk-r{r}-{nn}`.
7. Search ≥12 queries across ≥3 databases; log every query with hit counts and new-vs-seen.
8. Full text wherever reachable (Unpaywall, arXiv, PMC, author pages); `full_text_read` honest.
9. ≥10 claims, each with source DOI, quote location, S/R/O, axes, status SURVEYED.

10. From round 4 on (saturation fixes, decided after the round-3 audit):
    a. Add a section `## Found DOIs` listing every DOI or URL your queries surfaced that meets the need, one per line, marked `new` or `seen` — seen sources are listed even though they get no new ledger row. The audit's capture-recapture reads this list.
    b. Never leave S, R or O blank: grade unreachable sources from their abstract or metadata with `full_text_read=N` and flag `abstract-only`; a blank grade voids the round.

Output: ROOT/needs/n{k}-r{r}.md plus ledger rows.

End with a 3-sentence notification summary: claims, sources, full texts read, axes with no evidence.
