# Rust opinion map — v0.1 (provisional)

Compiled from batch 1's resolved research output (t5 compile, 2026-09-28;
corrected the same day — source enrichment, date and quote fixes; a
Voice-verification pass, a Claim-verification pass, and an Arguments compile
followed the same day). Every entry below is provisional: nothing in this
map has passed grading. See `docs/opinion-map.md` for the map's architecture
and `docs/subjects/rust.md` for Rust's scope.

## What batch 1 covers

401 Questions, 607 Positions, 771 Claims, 374 Voices, 429 Arguments, 267
Sources, 1,447 Concepts, across the 12 domains in `domains/` (10 target
domains, `core`, `other`). Every Question is `status: open`; none has been
closed, graded, or checked. Arguments cover 259 Positions under 114
Questions (a partial pass, not all 607/401) — see "Arguments" below.

## Voices, by verdict

Of 399 originally-compiled Voice ids, a Tier-3 track-record check
(`RECON/verify/voices-chunk-00..15.md`, `voices-calibration.md`) found:

| verdict | ids | what happened |
| --- | --- | --- |
| MEETS | 300 | `type` and `track_record` written; nothing added to its Claims |
| FAILS | 77 | `type`/`track_record` left unset (no evidence found); its Claims gapped `voice-below-bar` |
| UNKNOWN | 22 | same as FAILS; its Claims gapped `voice-unverified` |

25 of the 399 ids turned out to be the same person under a different id
(same-person clusters, `RECON/compile/compile-b1.md` § Voice-verification
pass) and were merged into 18 canonical ids, with their Claims repointed —
**374 Voice files remain**. One id (`sam-cutter`) was itself a
mis-transcription and was renamed to `sam-cutler`.

**Claims gapped this pass:** 107 `voice-below-bar`, 28 `voice-unverified`.
Combined with the 30 Claims already gapped `voice-unverified` at compile
time (an explicit `[voice-unverified]` marker in the source), 58 Claims
carry `voice-unverified` in total, 0 overlapping with `voice-below-bar`.

## Claims, verified

**664 of the 771 Claims** — every one except the 107 already gapped
`voice-below-bar`, which stay unverified — **were checked against their
Source on 2026-09-28** (quote and date fidelity; `RECON/verify/claims-final.csv`,
`claims-adjudication.md`). 648 confirmed as-is; 16 were corrected:

| what was wrong | count | fix |
| --- | --- | --- |
| date wrong | 8 | `date` corrected |
| quote not verbatim (typo silently fixed, or a cut with no ellipsis) | 2 | quote removed, paraphrase untouched (already accurate) |
| quote unfaithful (ASR-transcript garble, or two non-adjacent statements spliced by an ellipsis) | 5 | quote removed, paraphrase corrected |
| paraphrase over-attributed the source | 1 | paraphrase corrected, quote kept (it was verbatim) |

Every one of the 664 also carries `practiced: unknown` (this check was of
quote/date fidelity to the Source, not of the Voice's own code). The 648
confirmed Claims carry no per-Claim marker — `MAP/schema.yaml` has no
status/check field for `claim`, so this statement is it. The 16 corrected
ones carry a one-line note in `gap` (e.g. "verified 2026-09-28: date
corrected"). Full row-by-row detail: `RECON/compile/compile-b1.md` §
Claim-verification pass.

## Arguments

**429 Arguments**, `for`/`against` a Position, each with a fixed Value
(`approachability`, `correctness`, `iteration-speed`, `performance`,
`simplicity`, `stability`) and its Source(s) — covering 259 of 607
Positions under 114 of 401 Questions; the rest have none yet (this batch's
Arguments pass, `RECON/args/arguments-chunk-00..03.md`, is partial, not
exhaustive). 58 more Arguments were found but excluded: their only Values
were proposed-but-not-fixed `value-candidate:` names, logged instead —
never merged into MAP — at `RECON/args/value-candidates.md` (34 distinct
names, 68 occurrences; most frequent: `security` 8, `attribution-norms` 6).

Simulating validator rule 4 (the `status: closed` evidence minimum) minus
its check-record requirement — no fill-position/fill-tag/itt check exists
yet for anything — **4 Questions already meet it structurally**:
`merge-expensive-feature-with-limits`, `http-error-status-in-result`,
`depend-vs-hand-roll`, `generics-vs-dyn-for-abstraction`.

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
- **Checked is not graded.** 664 of 771 Claims had their quote/date checked
  against the Source on 2026-09-28 (see "Claims, verified" above; the 107
  `voice-below-bar` Claims are not checked and stay that way); Voices have a
  track-record check (see "Voices, by verdict"). Neither is grading: no
  paired-cases or ITT check exists anywhere; `MAP/checks/` is empty this
  batch.

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
- **Voice type/track_record: now established for MEETS Voices** (see
  "Voices, by verdict" above). 2 Voices (`ralfjung`,
  `r-my-rakic-on-behalf-of-the-compiler-performance-working`) give an
  illegal `type` value (`role` — a track_record kind word, not a Voice
  type) in the source chunk file; `type` left unset rather than guessed,
  `track_record` otherwise intact.
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
