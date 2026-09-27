# Found-DOI grading pass, r6-r7 gap (t3-grade-found-r67)

Scope: audit/saturation-r7.md rule 4 flagged 85 of 269 Found ids across the fourteen n*-r6.md /
n*-r7.md need files as ungraded in ledger/sources.csv. Every id appearing in a `## Found DOIs`
section was re-extracted from the fourteen files (n4-r7.md and n6-r7.md carry no such section, per
the audit); after de-duplicating four ids the round files themselves flag as "not counted as
separate sources" (two duplicate Crossref registrations of one 2004 contextual-interference
article, and two ids explicitly marked `=` an already-graded sibling id), 103 distinct listed ids
had no S/R/O anywhere in the ledger. All 103 were fetched via
`uv run python scripts/research/cache.py get <id>` (parallel batch, 10-way); 11 ERIC ids that
cache.py's browser route timed out on were re-fetched directly from `api.ies.ed.gov` and cached
under the same `sha1(url)[:12]` key scheme cache.py uses, with an index.csv row appended for each.
The line-687 row (`10.1207/s1532690xci2203_4`, S0/R0/O0 flagged "not graded") was also fixed: its
abstract, unreachable via every route cache.py tries, was recovered from OpenAlex's
`abstract_inverted_index` and graded for real (S2 R1 O0), cached, and appended as a new row alongside
the existing placeholder rows (append-only; the bad row was not edited or removed).

## Counts

- **99** ledger rows appended for the 103-4 de-duplicated ids, plus **1** fix row for the line-687
  DOI = **100** rows total, all under `found_by_agent=t3-grade-found-r67`.
- **S>=3: 19** rows (includes 3 S4 meta-analyses/systematic-reviews: `10.2466/pms.99.4.116-126`
  contextual-interference meta-analysis, `10.3102/00346543061002213` feedback-timing meta-analysis,
  `10.1080/00461520.2011.611369` VanLehn's tutoring-effectiveness review for N1, plus two S4 items
  under N7 read from full PMC text — a three-level SLA-pedagogical-agents meta-analysis and a
  PRISMA systematic review of 24 RCTs on AI-driven neurodevelopmental-disorder interventions).
- **S0 excluded: 4** — one retracted/withdrawn article (`10.1016/j.humov.2019.03.011`, already in
  index/exclusion-register.md entry 7, now also closed in sources.csv), two AEA trial registrations
  with no results yet, and one authors'-reply correspondence letter (no primary data) — all four
  named against snake-oil register criteria 1 or 3, per PLAN Sec.4, not used as a "not graded"
  placeholder.
- **full_text_read=Y: 8** (one review paper, one recovered-abstract OpenAlex reconstruction, and six
  PMC/arXiv/PeerJ/ACL full texts read for N7).
- **title-only (Crossref metadata, no abstract, no OA route succeeded): 19.**
- **landing-page-only (publisher page with no abstract extractable): 11.**
- Remaining ~62 rows are graded from a genuine abstract (ERIC, Crossref, cache.py, or a paper's own
  abstract section) without the full body text.

## By need

N1: 6 · N2: 11 · N3: 19 · N4: 2 · N5: 42 · N6: 1 · N7: 20 (N5 dominates because n5-r7.md alone
listed ~36 ids, most of them ERIC expert/novice-teacher comparisons never graded).

## What stayed genuinely unreachable

For the 19 title-only and 11 landing-page-only rows, cache.py's full route battery
(Unpaywall/arXiv-search/Semantic Scholar/Europe PMC/OpenAlex/CORE/browser) was exhausted and
returned no OA location, a 403/404, or a bot-wall; grades for these rest on the title (and,
where Crossref carried one, an abstract) alone and are flagged as such in the `flags` column so a
future round can supersede them with content-derived grades.

## Notification summary

100 sources.csv rows appended (99 for previously-ungraded Found ids across N1-N7's r6/r7 rounds,
plus one real replacement grade for the line-687 DOI that was wrongly carrying an S0 "not graded"
placeholder), all tagged `found_by_agent=t3-grade-found-r67`; 19 graded S>=3, 4 excluded at S0
against named snake-oil-register criteria (one retraction, two empty trial registrations, one
correspondence letter), and 30 rest on title/landing-page metadata alone after every OA route
failed. 11 ERIC records unreachable through cache.py's browser route were recovered via the ERIC
API directly and cached; one classic tutoring-diagnosis paper's abstract was recovered via
OpenAlex's abstract_inverted_index after every other route failed.
