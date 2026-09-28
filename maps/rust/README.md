# Rust opinion map — v0.1 (provisional)

Compiled from batch 1's resolved research output (t5 compile, 2026-09-28;
corrected the same day — source enrichment, date and quote fixes). Every
entry below is provisional: nothing in this map has passed grading. See
`docs/opinion-map.md` for the map's architecture and `docs/subjects/rust.md`
for Rust's scope.

## What batch 1 covers

401 Questions, 607 Positions, 771 Claims, 399 Voices, 267 Sources, 1,447
Concepts, across the 12 domains in `domains/` (10 target domains, `core`,
`other`). Every Question is `status: open`; none has been closed, graded, or
checked.

## Declared limits

- **Coverage is far from saturated.** Chapman unseen-species estimate: 25.0%
  (`swift-interop`) to 49.2% (`core`) across strata; every stratum fails the
  10% closure threshold (`merge-v3/estimate/closure-b1.md`).
- **Merge agreement:** the merge check's population reading agreed 78.0%
  [69.3, 84.7] (`merge-check3/merge-check-b1.md`).
- **Fill agreement:** blind Claim→Position fill agreed 98.7% before
  resolution (762/772); blind Position→tag fill agreed 67.6% (410/607)
  (`fill/resolve-b1.md`).
- **English only.** This batch's sampling and fill did not cover the
  German/Chinese/Ukrainian frames.
- **Paywalled books are unreachable** to the extractors.
- **Position summaries** were picked between two candidate fills by lexical
  overlap with the Claims' own quoted words, not by a semantic read of all
  candidates (`fill/resolve-b1.md` § Summaries).
- **Claims and Voices are unverified.** No Tier-3 pass has fetched a Claim's
  source to confirm it, or checked a Voice's track record.
- **No grading has run.** No paired-cases or ITT check exists; `MAP/checks/`
  is empty this batch.

## Known issues (this compile)

- **2 Claims marked `position: unresolved`** by lead ruling
  (`a-sa30-f013276-c5`, `b-sb23-f009334-c2`) — see
  `RECON/compile/compile-b1.md`.
- **9 Positions carry no `tag`**: fill-tag resolution was a three-way split
  or an ambiguous single-run vote; the schema's tag enum has no "unresolved"
  value, so it is omitted rather than force-filled.
- **7 suspected duplicate Positions**, not merged (a merger's job, not the
  compiler's): `bounded-grid-universe`, `ffi-copy-vs-share`,
  `generics-vs-dyn-for-abstraction`, `library-io-factored-out`,
  `opt-level-z-vs-s`, `profile-before-optimizing`,
  `reproduce-wasm-bugs-natively` (`fill/resolve-b1.md` § Key comparison).
- **1 Claim excluded** (`a-saL1-f005454-c5`): resolved to "supports no
  Position", and the schema has no slot for that outcome.
- **Every Voice carries only `name`.** No Tier-3 voice-verification pass has
  run this batch, so `type` and `track_record` are not established; all 399
  Voices fail the validator's required-field and track-record checks by
  design — this is the one gap the correction pass did not close (lead
  ruling: it belongs to the Voice-verification pass, not the compiler).
- **Sources carry `url`, `title`, `kind`, `language` and (for 261 of 267) a
  `date`**, transcribed from the source-frame registry
  (`frame/frame*.csv`, `samples/batch-1-team-{a,b}.csv`). `kind` is set
  directly from the registry's `class` column where unambiguous, and from
  the referenced URL's own structure (GitHub issue/PR vs. repo, a known
  forum host, a video host, else a post) where the class only names how the
  source was discovered. **6 Sources have no day-precision date** in the
  registry either — the same 6 living-doc sources (`f000149`, `f000217`,
  `f000227`, `f000233`, `f000256`, `f000267`) behind many of the 70 unset
  Claim dates below — and are left with `date` unset.
- **70 Claim dates are left unset** (year/month-only, or the source states
  none at all) rather than invented; **9 were normalized** to a
  day-precision date named elsewhere in an otherwise-undated Date string
  (5 Wayback captures, 3 reposts, 1 the Voice's own retrospective-post
  date), each with a `gap` note where the date is a proxy rather than the
  original's own. Full list of the 70: `RECON/compile/compile-b1.md`.
- **9 Claim quotes exceeded the 300-character cap**; each is now cut at a
  word boundary to the cap plus an ellipsis, with the paraphrase (already
  authored, unedited) carrying the rest.

Full accounting: `RECON/compile/compile-b1.md`.

## Upkeep

This map is live and provisional by default (`docs/opinion-map.md` § Done and
upkeep). Batch 2+ research, Tier-3 verification, and grading extend and
correct it in place — nothing here is final.
