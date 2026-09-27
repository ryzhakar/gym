# t1-merge — instructions

Read ROOT/prompts/common.md first; it binds you.

Inputs: every file in ROOT/index/fields/ (six fields: education, cs-education, expertise, coaching, ai-tutoring, adult-skill), ROOT/index/exclusion-register.md. PLAN lines 125–131 (your row and the Tier 1 gate), 96–99 (ledger schemas), 144 (calibration set).

Task:
1. Dedupe anchors across fields by DOI (normalize: lowercase, strip `https://doi.org/`); by URL when no DOI. Keep every field an anchor came from.
2. Drop nothing silently: an anchor matching the exclusion register goes to a `## Excluded` section with the register entry number.
3. Write ROOT/index/index.md:
   # Teaching research — merged index
   ## Anchors by field (one section per field; table: # | DOI/URL | authors, year | title | kind | fields | one line)
   ## Cross-field anchors (in 2+ fields)
   ## Disputes (union of field disputes, deduped)
   ## Excluded
   ## Statistics: total unique; per field; per kind; cross-field count; unresolved citations dropped (list)
4. Seed ROOT/ledger/sources.csv with the header at PLAN line 98 and one row per unique anchor (S, R, O blank; found_by_agent=t1-merge; round=0; full_text_read=N).
5. Create ROOT/ledger/claims.csv with the header at PLAN line 99 only.
6. Write ROOT/verify/calibration-set.md: five anchors chosen to span strength bands as the S table defines them (one likely S4 meta-analysis, one S3 RCT, one S2 coded observation, one S1 practitioner account, one flagged or borderline), each with DOI/URL and why chosen; no grades.

Scope: merge only; no grading, no new searching.

End with a 3-sentence notification summary: unique anchors, cross-field count, exclusions.
