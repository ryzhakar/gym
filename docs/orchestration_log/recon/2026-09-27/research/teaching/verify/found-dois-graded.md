# Found-DOIs grading — ledger repair + unledgered-DOI grading

Task: (1) repair 3 malformed sources.csv lines; (2) grade every DOI in the `## Found DOIs`
sections of `needs/n7-r4.md`, `needs/n1-r5.md`, `needs/n6-r5.md` that had no row in
`ledger/sources.csv`, per PLAN lines 198-239.

## Ledger repair

Lines 565, 569, 576 of `ledger/sources.csv` (agent t2-n4-r5) each carried 18 fields instead of
17 because a comma inside an unquoted value (`delay_to_test`, `population`, or `design`) split
into an extra field. Rewrote all three via Python's `csv` module, preserving every original
value, merging the wrongly-split field back into one properly quoted string. Confirmed via
`csv.reader`: all 600 pre-existing lines (and the file's current 750 lines) now parse to exactly
17 fields, matching the header.

## Found-DOI grading

63 DOIs across the three needs files had no existing sources.csv row (55 in n7-r4, minus those
already used for claims and ledgered; 10 in n1-r5; 8 in n6-r5). Text obtained via
`uv run python scripts/research/cache.py get <doi>` for every one (a Python driver wrapping the
call with a 40s per-item timeout, since this sandbox has no `timeout(1)` binary), supplemented by
direct Crossref and Semantic Scholar per-DOI lookups for metadata and abstracts the cache script's
routes missed. Every row appended to `ledger/sources.csv` (found_by_agent=t3-grade-found, round =
the source need's round, needs = N1/N6/N7).

### Counts

- **Graded: 63** (10 N1, 8 N6, 45 N7)
- **S>=3: 16** (6 N1, 2 N6, 8 N7) — meta-analyses (personnel-selection validity literature),
  controlled quasi-experiments/RCTs (jel.v14n6p233, s11423-026-10672-5, AERA 1438448, the PeerJ
  basketball decision-training study recovered via its Table-3 DOI), and one large-N prospective
  study (bjhp.12637).
- **full_text_read=Y: 8** — genuine full text recovered (not just an abstract): bjhp.12637 (Europe
  PMC), the fpsyg/jel.v14n6p233 open-access journal copy, the PeerJ basketball paper (via its
  Table-3 DOI), the AERA 1438448 repository metadata+results page, two AERA 2026 iPosterSessions
  posters with real Methods/Results content, and the Spanish-language noesis.v3i7.67 study
  (confirmed by t2-n6-r5's own prior round).
- **Title-only (no abstract or text of any kind reachable): 21** — closed-access journals/IEEE/T&F
  chapters with no Crossref or Semantic Scholar abstract and no OA route; graded conservatively
  (S=1 by default, adjusted only where the title itself unambiguously names a design element,
  e.g. an explicit delay or an explicit "meta-analysis"/"qualitative study" label).
- **Remaining 34: abstract-level only** (Crossref, Semantic Scholar, or a paywalled landing page's
  own abstract paragraph), not full text.

### Notable finds during grading

- Two duplicate-DOI pairs identified and flagged rather than double-counted: the MIT Press
  "Recursion as a Usage-Based Skill" chapter (10.7551/mitpress/10406.003.0011 and
  10.7551/mitpress/9780262034319.003.0007, identical title/book) and the "ChatGPT as Co-Tutor"
  study preprinted on both SSRN (10.2139/ssrn.6316078) and Research Square
  (10.21203/rs.3.rs-8988029/v1, identical title and near-identical abstract).
- 10.31234/osf.io/umhtz is the OSF preprint of the already-ledgered 10.1080/23311908.2022.2041277
  (same title); graded identically and flagged as the same underlying source.
- 10.61686/niyvn39533's Crossref title field was blank; the real title ("Uncharted territory:
  unravelling the effect of feedback on diagnostic performance and confidence-accuracy calibration
  in physicians") was recovered from the actual NWO grant-registry page — it is a funded-project
  description, not a study report with data.
- 10.7717/peerj.7392/table-3 and 10.1109/tcss.2026.3656955/mm1 are both sub-resource DOIs (a table,
  a supplementary-material file) rather than article DOIs; the PeerJ one's parent article was
  identified and read in full (a genuine randomized quasi-experiment with a retention-test phase),
  upgrading it well past what its "just a table" DOI suggested.
