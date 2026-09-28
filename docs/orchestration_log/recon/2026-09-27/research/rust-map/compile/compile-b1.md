# Compile, batch 1 — Rust map v0.1

t5 compile, 2026-09-28, with a correction pass the same day (lead ruling:
"three of the four gaps are transcription, not content; close them. Voice
type/track_record stays a declared gap for the Voice-verification pass.").
Wrote MAP entity files from batch 1's resolved fill output
(`merge-v3/merged-questions-b1.md`, `fill/positions-final-b1.md`,
`fill/resolved-b1.csv`, `fill/resolve-b1.md`, `fill/key-b1.csv`,
`fill/input-b1-01..13.md`) plus, for the correction pass, the source-frame
registry (`frame/frame.csv`, `frame/frame-older.csv`,
`frame/frame-v2-nonen.csv`, `samples/batch-1-team-a.csv`,
`samples/batch-1-team-b.csv`) — per `MAP/schema.yaml`. Compiler script:
`docs/orchestration_log/recon/2026-09-27/research/rust-map/compile/compile.py`
(archived; not part of MAP).

## Counts written

| kind | files | home |
| --- | --- | --- |
| question | 401 | `MAP/questions/` |
| position | 607 | `MAP/positions/` |
| claim | 771 | `MAP/claims/` |
| voice | 399 | `MAP/voices/` |
| source | 267 | `MAP/sources/` |
| concept | 1447 | `MAP/concepts/` |
| value | 6 (untouched, pre-seeded) | `MAP/values/` |
| domain | 12 (untouched, pre-seeded) | `MAP/domains/` |
| argument, convention, check | 0 (not in this compile's scope) | — |

772 Claim rows were resolved in batch 1 (`fill/resolved-b1.csv`); 771 are
written (1 excluded — see below).

## Disposition of the 772 resolved rows

- **769** carry a Position id, taken from `fill/positions-final-b1.md`'s
  per-Position `Claims:` lines.
- **2** carry `position: unresolved`, per the schema's `allow: [unresolved]`:
  - `b-sb23-f009334-c2` (`crate-maintenance-signaling`) — native: `resolved-b1.csv` final = `unresolved` (a genuine three-way split; see `resolve-b1.md` § Unresolved rows).
  - `a-sa30-f013276-c5` (`dyn-compatibility-rules-relaxation`) — by lead ruling, overriding `resolved-b1.csv`'s recorded majority result (`--p2`). `resolve-b1.md` § Method step 3 flags this row's blind-fill process as compromised (a blinding lapse) and names it for adjudication; removed from `dyn-compatibility-rules-relaxation--p2`'s Claim list and marked unresolved here.
- **1** excluded: `a-saL1-f005454-c5` (`middleware-hook-vs-typestate`) resolved to `final: none` (supports no Position). The schema's `claim.position` field allows only a Position id or the literal `unresolved`; no slot for "resolved to no Position," so this Claim is not written.

## Position tags: 9 left untagged

`fill/resolve-b1.md` § Tags lists 9 Positions where the blind fill-tag process
produced no majority. The schema's `tag` enum (`fact`/`tradeoff`/`taste`) has
no "unresolved" value, so these 9 are written with `tag` omitted:
`ai-authored-community-contributions--p1`,
`dedicated-methods-vs-manual-composition--p1`, `doctests-must-compile--p1`,
`dyn-compatibility-rules-relaxation--p2`,
`mutex-vs-atomics--atomics-carry-own-bugs`,
`replace-battle-tested-c-with-rust--safety-not-enough`,
`rust-vs-c-inherent-performance--safe-rust-matches`,
`same-state-transition-trigger--p3`, `ui-dsl-vs-plain-rust--p1`.

## 7 declared duplicate Positions (not merged)

`fill/resolve-b1.md` § Key comparison identifies 7 Questions where the
merger's original Position label and the blind-fill-resolved Position are
different labels for the same choice (all 7 are Rust-and-WebAssembly-book
Claims, `a-sB02-f000256-*`). Collapsing duplicate Positions is a merge
decision, out of this compile's scope. Declared, not merged:
`bounded-grid-universe`, `ffi-copy-vs-share`,
`generics-vs-dyn-for-abstraction`, `library-io-factored-out`,
`opt-level-z-vs-s`, `profile-before-optimizing`,
`reproduce-wasm-bugs-natively`.

## 2 Questions with no Domain

`lambda-build-tooling` and `rust-for-backend-services-vs-jvm` are carried
only by a re-homed Claim, with no team-local crosswalk row. Their
`merged-questions-b1.md` entries state `Domains: none (no team-local
member)` verbatim; `domains: []` is written and a `notes` line records the
gap.

## Correction pass: Claim dates (lead ruling)

Rule: normalize to ISO where the input's date is unambiguous; where only a
year or month is known, or the source states none, leave the field unset
and list it — never guess a day. Of the 79 originally non-ISO Claim dates:

- **9 normalized** to a day-precision date named elsewhere in the same Date
  string, rather than the (undated) headline value:
  - 5 Wayback capture dates (`a-sB01-f000217-c1,c2,c3,c4,c5`) — the
    underlying document is undated; the capture date is used, with a
    `gap` note that it is a capture date, not the document's own.
  - 3 repost dates (`a-sa28-f012469-c5,c11,c12`) — the original post is
    undated; the repost date is used, same `gap` note pattern.
  - 1 (`a-sa18-f009104-c1`) — the Claim itself restates an "over a decade"
    view, but the Date field names the day the Voice wrote *this*
    retrospective post (2026-09-21), which is the Claim's own date, not a
    proxy; used directly, no `gap` note.
- **70 left unset** (no day-precision date anywhere in the string), listed
  in full at the end of this report:
  - 44 living-document placeholders ("undated"/"unknown (living
    document/doc)").
  - 17 year-only (`a-sB02-f000256-*`, all "2018").
  - 3 year-only (`a-sB01-f000149-*`, "2023 (course release date stated in
    source)").
  - 6 individually-judged: 4 from a single source (`f005332`) giving only a
    month/season or an explicitly undated clip; 1 (`a-sa28-f012469-c9`)
    whose only other dates belong to two different, unfetched posts; 1
    (`a-sa15-f005516-c1`) whose only other dates belong to two different,
    unconfirmed, unfetched blog posts.

Net effect on the validator: these 70 claims each now fail *two* rules
(missing required field `date`, and — since `parse_date(None)` still isn't
ISO — "date is not ISO") where before they failed one (a non-ISO string
value). This is intentional: an absent field is a more honest
representation than a value that merely looks like it satisfies the
schema, and 9 of the original 79 are now genuinely fixed.

## Correction pass: overlong Claim quotes (lead ruling)

All 9 quotes over the 300-character cap (max 400) were cut at a word
boundary to fit within the cap plus a single-character ellipsis (`…`); the
paraphrase (a separately authored field, already covering the same
substance) carries what the cut removed. No paraphrase was edited.

## Correction pass: Source enrichment (lead ruling)

All 267 Sources matched a row in the frame registry by frame id (0 needed
the URL fallback). `title` and `language` are transcribed verbatim.

`kind` is set from the row's `class` column where unambiguous
(`books-courses` → `book`, `talks` → `talk`; no Source in this batch has
class `rfc` or `survey`). Six classes name *how the source was discovered*
(`domain-subframes`, `hn-lobsters`, `individual-blogs`, `twir-links`,
`users-forum`, `internals`, `project-blog`), not what it is — for these, the
referenced URL's own structure decides: a GitHub issue/PR/discussion URL is
`thread`, any other `github.com` URL is `code`, a known forum host
(`internals.rust-lang.org`, `users.rust-lang.org`, `lobste.rs`,
`news.ycombinator.com`) or a `/t/...` path is `thread`, a `youtube.com`/
`bilibili.com` URL is `talk`, and anything else (blog posts, a lone social
post) is `post`. Resulting distribution across the 267 Sources: `post` 120,
`thread` 119, `talk` 19, `book` 6, `code` 3.

`date` is the registry's `date` column, truncated to its date portion where
it carries a time component (`T00:00:00` etc., 261 Sources); **6 Sources
have no day-precision date** in the registry either (`f000149` "unknown";
`f000217`, `f000227`, `f000233`, `f000256`, `f000267` "unknown (living
document)") and are left with `date` unset — the same 6 frame ids already
flagged as Claim-level living-doc gaps.

## Voice: still a declared gap (unchanged, by lead ruling)

All 399 Voices still carry only `name`. No Tier-3 voice-verification pass
(fable-plan.md § 4: track-record bar, `type` tag, influence evidence) has
run; nothing in this compile's inputs states a Voice's `type` or
`track_record`, and the lead ruling that opened this correction pass keeps
this one a declared gap for that pass, not the compiler, to close.

## Mechanical id-collision handling (62 cases, no content change)

1,447 Concepts are transcribed one entity per distinct phrase string (never
merged, never split). 62 times, two distinct phrases (or a phrase and an
existing Question id) slugified to the same id; each later one was
disambiguated with a numeric suffix (`-2`, `-3`, …) rather than silently
overwriting the earlier entity — a filename-uniqueness mechanic (schema
rule 2), not a content decision.

## 43 Claims carry a `gap`

30 where the input's Voice field carried an explicit `[voice-unverified]`
marker (all 30 Rust-and-WebAssembly-book Claims); 13 where the input's
Voice field carried an inline researcher caveat beyond the name itself
(split at the source's own " — " separator; one, `a-sa28-f012469-c5`, an
explicit voice-eligibility question left for merge/audit — this same Claim
also carries the repost-date note above, joined with "; "). `gap`'s stated
purpose (fable-plan.md) is "code contradicting the declaration" — reused
here for lack of any other free-text slot on Claim.

## Validator run

`uv run python scripts/map/check_map.py --map maps/rust`

**1,354 FAIL** (down from 2,364 before this correction pass), by rule:

| cause | count | status |
| --- | --- | --- |
| Voice missing `type` (required-field) | 399 | declared gap — Voice-verification pass |
| Voice missing `track_record` (required-field) | 399 | declared gap — Voice-verification pass |
| Voice `track_record` has no url (rule 6) | 399 | declared gap — Voice-verification pass |
| Source missing `date` (required-field, 6 Sources) | 6 | declared gap — no day-precision date in the frame registry |
| Position missing `tag` (required-field, 9 Positions) | 9 | declared gap — 3-way fill-tag split |
| Question missing `domains` (required-field, 2 Questions) | 2 | declared gap — no team-local crosswalk row |
| Claim missing `date` (required-field, 70 Claims) | 70 | declared gap — no day-precision date in source |
| Claim date not ISO (same 70 Claims, `None` also fails the ISO check) | 70 | declared gap — see above |

Fixed this pass (no longer failing): Source required-field FAILs
1,068 → 6 (267 Sources × 4 fields, down to 6 Sources × 1 field, `date`);
Claim quote over 300 characters, 9 → 0. Net: 1,010 fewer FAILs than the
previous run (2,364 → 1,354).

## 70 Claims with date left unset (full list)

| claim | source Date field |
| --- | --- |
| `a-sB01-f000149-c1` | 2023 (course release date stated in source; no chapter-level date) |
| `a-sB01-f000149-c2` | 2023 (course release date stated in source) |
| `a-sB01-f000149-c3` | 2023 (course release date stated in source) |
| `a-sB01-f000227-c1` | undated (living doc, "documentation for RTIC v2.x") |
| `a-sB01-f000227-c2` | undated (living doc) |
| `a-sB01-f000227-c3` | undated (living doc) |
| `a-sB01-f000227-c4` | undated (living doc) |
| `a-sB02-f000256-c1` | 2018 |
| `a-sB02-f000256-c10` | 2018 |
| `a-sB02-f000256-c11` | 2018 |
| `a-sB02-f000256-c12` | 2018 |
| `a-sB02-f000256-c13` | 2018 |
| `a-sB02-f000256-c14` | 2018 |
| `a-sB02-f000256-c15` | 2018 |
| `a-sB02-f000256-c16` | 2018 |
| `a-sB02-f000256-c17` | 2018 |
| `a-sB02-f000256-c2` | 2018 |
| `a-sB02-f000256-c3` | 2018 |
| `a-sB02-f000256-c4` | 2018 |
| `a-sB02-f000256-c5` | 2018 |
| `a-sB02-f000256-c6` | 2018 |
| `a-sB02-f000256-c7` | 2018 |
| `a-sB02-f000256-c8` | 2018 |
| `a-sB02-f000256-c9` | 2018 |
| `a-sB04-f000227-c1` | undated (living doc, v2.x) |
| `a-sB04-f000227-c2` | undated (living doc, v2.x) |
| `a-sB04-f000227-c3` | undated (living doc, v2.x) |
| `a-sB04-f000227-c4` | undated (living doc, v2.x) |
| `a-sB04-f000227-c5` | undated (living doc, v2.x) |
| `a-sR01-f000227-c1` | unknown (living document, no publish/version date given) |
| `a-sR01-f000227-c2` | unknown (living document, no publish/version date given) |
| `a-sa15-f005516-c1` | undated in this source (an anonymous commenter quotes a Cantrill talk via youtu.be/HgtRAbE1nBM?t=2450 with no air date given here; two Cantrill blog posts are also named — bcantrill.dtrace.org/2018/09/18/falling-in-love-with-rust/ and .../2018/09/28/the-relative-performance-of-c-and-rust/ — whose URL-embedded dates, 2018-09-18 and 2018-09-28, are not independently confirmed since those posts were not fetched) |
| `a-sa28-f012469-c9` | blog post undated in source; cited 2016-04-03 and again 2018-04-25 |
| `b-bk02-f000256-c1` | unknown (living doc) |
| `b-bk02-f000256-c10` | unknown (living doc) |
| `b-bk02-f000256-c11` | unknown (living doc) |
| `b-bk02-f000256-c12` | unknown (living doc) |
| `b-bk02-f000256-c13` | unknown (living doc) |
| `b-bk02-f000256-c2` | unknown (living doc) |
| `b-bk02-f000256-c3` | unknown (living doc) |
| `b-bk02-f000256-c4` | unknown (living doc) |
| `b-bk02-f000256-c5` | unknown (living doc) |
| `b-bk02-f000256-c6` | unknown (living doc) |
| `b-bk02-f000256-c7` | unknown (living doc) |
| `b-bk02-f000256-c8` | unknown (living doc) |
| `b-bk02-f000256-c9` | unknown (living doc) |
| `b-bk03-f000267-c1` | unknown (living document) |
| `b-bk03-f000267-c10` | unknown (living document) |
| `b-bk03-f000267-c11` | unknown (living document) |
| `b-bk03-f000267-c12` | unknown (living document) |
| `b-bk03-f000267-c13` | unknown (living document) |
| `b-bk03-f000267-c14` | unknown (living document) |
| `b-bk03-f000267-c15` | unknown (living document) |
| `b-bk03-f000267-c16` | unknown (living document) |
| `b-bk03-f000267-c17` | unknown (living document) |
| `b-bk03-f000267-c2` | unknown (living document) |
| `b-bk03-f000267-c3` | unknown (living document) |
| `b-bk03-f000267-c4` | unknown (living document) |
| `b-bk03-f000267-c5` | unknown (living document) |
| `b-bk03-f000267-c6` | unknown (living document) |
| `b-bk03-f000267-c7` | unknown (living document) |
| `b-bk03-f000267-c8` | unknown (living document) |
| `b-bk03-f000267-c9` | unknown (living document) |
| `b-sR01-f000233-c1` | undated (living document; no revision date on page) |
| `b-sR01-f000233-c2` | undated (living document) |
| `b-sR01-f000256-c1` | undated (living document) |
| `b-sb18-f005332-c1` | undated (conference talk clip, reported in the 2024-09-04 article) |
| `b-sb18-f005332-c2` | 2024-08 (week before the 2024-09-04 article) |
| `b-sb18-f005332-c3` | late August 2024 (Mastodon post, per the article) |
| `b-sb18-f005332-c4` | August 2024 (public appearance, per the article) |



## Voice-verification pass (lead ruling, 2026-09-28)

Applied `RECON/verify/voices-chunk-00..15.md` (399 Voice blocks — one per
existing Voice — from a Tier-3 track-record check) and
`RECON/verify/voices-calibration.md` (a re-check of 118 of those: 112
original MEETS candidates whose only cited evidence was production/role,
5 FAILS candidates whose `checked` field mentioned commits or merged PRs,
plus steffahn). Calibration's verdicts and evidence override the chunk
files wherever both speak; the chunk file's own evidence is used as-is
elsewhere. Script:
`docs/orchestration_log/recon/2026-09-27/research/rust-map/compile/verify_voices.py`.

### Verdict counts (399 original ids, before merging)

| verdict | count |
| --- | --- |
| MEETS | 300 |
| FAILS | 77 |
| UNKNOWN | 22 |

301 of these 399 are set by the chunk files unchanged; 117 are set by the
calibration's override (steffahn's calibration row is a pure re-confirmation
of the chunk's own finding, so the chunk's own track_record — already
url-bearing — was kept rather than replaced with the calibration table's
non-url `gh api` citation of the same fact).

### Per-Voice fields written

- **MEETS**: `type`, `track_record` (kind, evidence, url, date — parsed
  from the chunk/calibration prose) and `influence` written as evidenced.
- **FAILS / UNKNOWN**: `type` and `track_record` left unset where the chunk
  file itself found nothing ("checked <kind>: no evidence found" bullets,
  and the single-line "none found"/"none meets the bar" variants, are a
  negative finding, not a track record — transcribed as absence, not as
  content). Where a FAILS/UNKNOWN entry's chunk file nonetheless names an
  identity-based `type` guess independent of the bar (some do), that guess
  is transcribed as given.
- **2 illegal `type` values**: `ralfjung` and
  `r-my-rakic-on-behalf-of-the-compiler-performance-working` give
  `type: role` in their chunk file — not one of the six legal Voice types
  (`role` is a *track_record kind* word, not a type). Left unset rather
  than guessed; both keep their real, url-bearing `track_record` (MEETS on
  other grounds).
- **10 MEETS Voices have no url anywhere in `track_record`**: `bjoernq`,
  `jamesmunns`, `jessebraham`, `laggui`, `ssokolow`, `stefan-baumgartner`,
  `vaultwarden-maintainers-dani-garcia-vaultwarden`, `warre-snaet`,
  `yanshay`, `yatekii` — each one's only cited evidence is a `gh api ...`
  command or a bare description, not a browsable URL. Transcribed as
  given; these fail the validator's track-record-url check despite being
  genuinely established.

### Same-person merges (18 clusters, 25 ids merged away)

14 clusters from the calibration file's "Same-person id pairs" list, plus
4 named directly in the chunk files (dominaezzz, jkelleyrtp/jonathan-kelly,
kornel, nazmul-idris — none of these four are in the calibration table).
The canonical id per cluster is the bare/shortest handle-like id; every
other member's `track_record`/`influence` lines are unioned into the
canonical (deduped; a pure "same as `<canonical>`" cross-reference with no
url of its own is dropped rather than kept as a content-free line), and
every Claim naming a merged-away id is repointed to the canonical id.
40 Claims were repointed.

| canonical | merged away |
| --- | --- |
| arqu | arqu-n0-computer-iroh-engineer-production-post-mortem-author |
| dignifiedquire | dignifiedquire-byline-iroh-blog-rust-connection-in-source, dignifiedquire-iroh-n0-computer, dignifiedquire-n0-computer-iroh-maintainer, iroh-n0-dignifiedquire-post-author |
| bugadani-esp-hal-maintainer | bugadani-esp-hal-maintainer-pr-author |
| cfallin | cfallin-chris-fallin |
| felipebalbi | felipebalbi-nxp-embedded-engineer-embassy-nxp-contributor |
| fitzgen | fitzgen-bytecode-alliance-wasmtime-core-arbitrary-crate |
| lukewagner | luke-wagner-fastly-w3c-bytecode-alliance-component-model-co |
| saulecabrera | saulecabrera-bytecode-alliance-wasmtime-winch-baseline |
| ramfox | ramfox-byline-iroh-blog-rust-connection-in-source-iroh, ramfox-matheus23, ramfox-matheus23-iroh-n0-blog-authors |
| jamesmunns | jamesmunns-embassy-maintainer |
| jakub-ber-nek-on-behalf-of-the-rust-funding-team | jakub-ber-nek-on-behalf-of-the-rust-project-mentorship-team |
| hannah-wang-ben-yang-and-fisher-darling | hannah-wang-ben-yang-fisher-darling-cloudflare |
| b5 | dig-b5-and-ramfox-iroh-team |
| r-diger-klaehn-n0-iroh-iroh-blobs | iroh-n0-friedel-ziegelmayer-r-diger-klaehn-post-authors |
| dominaezzz | dominaezzz-esp-hal-reviewer |
| jkelleyrtp | jonathan-kelly, jonathan-kelly-likely-kelley-unconfirmed |
| kornel | kornel-2, kornel-forum-handle-identity-track-record-not-established |
| nazmul-idris-r3bl-tui-maintainer | nas-ceo-founder-rebel-author-developerlife-com-maintainer |

Not merged, though similarly named: bare `bugadani` and bare
`r-diger-klaehn` are distinct files from their maintainer/blog-suffixed
namesakes above and are outside the named lists — left untouched rather
than guessed into a cluster.

### Name correction

`sam-cutter` → id renamed to `sam-cutler`, `name` corrected to "Sam Cutler"
(YouTube oEmbed title evidence in the calibration file; the id itself was
the misspelling, so it was renamed and its 2 Claims repointed, not just the
`name` field). `zeke-hunter-green` was checked and is not a misspelling
(same oEmbed title).

### Claims: `gap` added for FAILS/UNKNOWN Voices

Rule: MEETS → nothing more. FAILS → `voice-below-bar`. UNKNOWN →
`voice-unverified` (same text the initial compile already used for the 30
Rust-and-WebAssembly-book Claims whose Voice field was explicitly
`[voice-unverified]`; joined with `; ` rather than duplicated where a Claim
already carried a `gap`). **107 Claims gapped `voice-below-bar`**; **28
gapped `voice-unverified`** by this pass specifically (`voice-unverified`
across both sources: 58 Claims total, 0 overlap with `voice-below-bar`).
These Claims are excluded from "resolved Claims" per rule 4's
`resolved_claims` filter in spirit, though no Question in this batch is
`status: closed` for that filter to actually gate.

Two re-run artifacts, not real gaps: while iterating the script, 2 Claims
(`b-sb24-f011295-c1`, `b-sb24-f011295-c2`) were briefly logged as
"voice has no verification entry" because a *second* run read back their
already-renamed `voice: sam-cutler` field (the chunk files key this person
under `sam-cutter`). Both Claims are correct in the final state — `sam-cutler`
is MEETS, needs no gap — this is a script-idempotency note, not a content
finding.

### Voices: final counts

374 Voice files (399 originals − 25 merged away). Type distribution:
builder 219, unset 88, institution 29, educator 22, language-designer 12,
critic 4.

### Validator run

`uv run python scripts/map/check_map.py --map maps/rust`

**427 FAIL** (up from 1,354 before this pass — see below for why "up" is
the correct direction here), by rule:

| cause | count | vs. previous pass |
| --- | --- | --- |
| Voice missing `type` | 88 | was 399 (declared gap) — now most MEETS Voices have one |
| Voice missing `track_record` | 86 | was 399 — now most MEETS Voices have one |
| Voice `track_record` has no url (rule 6) | 96 | was 399 — 86 FAILS/UNKNOWN Voices genuinely have none, 10 MEETS Voices cite a `gh api` command instead of a url |
| Source missing `date` (6 Sources) | 6 | unchanged |
| Position missing `tag` (9 Positions) | 9 | unchanged |
| Question missing `domains` (2 Questions) | 2 | unchanged |
| Claim missing `date` (70 Claims) | 70 | unchanged |
| Claim date not ISO (same 70 Claims) | 70 | unchanged |

Voice FAILs did not drop to (399 − 300 MEETS) × 3 = 297 as a first estimate
might suggest, because merging cut the Voice count to 374 (fewer files to
fail, but also fewer files to pass) and because fixing this pass's own
parsing bugs *increased* the count partway through: two classes of chunk-file
bullet — `checked <kind>: <negative finding>` and a bare `none checkable`
sentence — read at first pass as if they were positive track-record entries
(they are the FAILS/UNKNOWN explanation, phrased to look like evidence).
Once corrected, several dozen FAILS/UNKNOWN Voices that had briefly acquired
a fabricated-looking `type` and `track_record` correctly lost them again,
adding required-field FAILs that a wrong-but-present value had been masking.
Reported here because a FAIL count moving in the "wrong" direction from a
mid-pass bug fix should never be assumed to reflect regression: the
1,354 → 427 comparison is the one that matters, taken pass-to-pass on
correct data.

Full output verbatim follows.

```
FAIL  maps/rust/questions/lambda-build-tooling.yaml  missing required field 'domains'
FAIL  maps/rust/questions/rust-for-backend-services-vs-jvm.yaml  missing required field 'domains'
FAIL  maps/rust/positions/ai-authored-community-contributions--p1.yaml  missing required field 'tag'
FAIL  maps/rust/positions/dedicated-methods-vs-manual-composition--p1.yaml  missing required field 'tag'
FAIL  maps/rust/positions/doctests-must-compile--p1.yaml  missing required field 'tag'
FAIL  maps/rust/positions/dyn-compatibility-rules-relaxation--p2.yaml  missing required field 'tag'
FAIL  maps/rust/positions/mutex-vs-atomics--atomics-carry-own-bugs.yaml  missing required field 'tag'
FAIL  maps/rust/positions/replace-battle-tested-c-with-rust--safety-not-enough.yaml  missing required field 'tag'
FAIL  maps/rust/positions/rust-vs-c-inherent-performance--safe-rust-matches.yaml  missing required field 'tag'
FAIL  maps/rust/positions/same-state-transition-trigger--p3.yaml  missing required field 'tag'
FAIL  maps/rust/positions/ui-dsl-vs-plain-rust--p1.yaml  missing required field 'tag'
FAIL  maps/rust/voices/2e71828.yaml  missing required field 'type'
FAIL  maps/rust/voices/2e71828.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/afetisov.yaml  missing required field 'type'
FAIL  maps/rust/voices/afetisov.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/ajdecon.yaml  missing required field 'type'
FAIL  maps/rust/voices/ajdecon.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/alandekok.yaml  missing required field 'type'
FAIL  maps/rust/voices/alandekok.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/alonely0.yaml  missing required field 'type'
FAIL  maps/rust/voices/alonely0.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/andrei-alexandrescu-creator-of-d.yaml  missing required field 'type'
FAIL  maps/rust/voices/andrei-alexandrescu-creator-of-d.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/anthonygrondin.yaml  missing required field 'type'
FAIL  maps/rust/voices/anthonygrondin.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/badeend.yaml  missing required field 'type'
FAIL  maps/rust/voices/badeend.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/bogdan-petru.yaml  missing required field 'type'
FAIL  maps/rust/voices/bogdan-petru.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/bruce-perens.yaml  missing required field 'type'
FAIL  maps/rust/voices/bruce-perens.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/bsder.yaml  missing required field 'type'
FAIL  maps/rust/voices/bsder.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/bstrie-attribution-hedged-by-the-poster-themselves-im.yaml  missing required field 'type'
FAIL  maps/rust/voices/bstrie-attribution-hedged-by-the-poster-themselves-im.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/chayan-mistry.yaml  missing required field 'type'
FAIL  maps/rust/voices/chayan-mistry.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/chescock.yaml  missing required field 'type'
FAIL  maps/rust/voices/chescock.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/co-presenter-taj-touch-unclear.yaml  missing required field 'type'
FAIL  maps/rust/voices/co-presenter-taj-touch-unclear.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/coreh.yaml  missing required field 'type'
FAIL  maps/rust/voices/coreh.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/crazyboyqcd.yaml  missing required field 'type'
FAIL  maps/rust/voices/crazyboyqcd.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/danieljoyce.yaml  missing required field 'type'
FAIL  maps/rust/voices/danieljoyce.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/dataangel.yaml  missing required field 'type'
FAIL  maps/rust/voices/dataangel.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/david-chisnall.yaml  missing required field 'type'
FAIL  maps/rust/voices/david-chisnall.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/dhruv-ahuja.yaml  missing required field 'type'
FAIL  maps/rust/voices/dhruv-ahuja.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/durka42.yaml  missing required field 'type'
FAIL  maps/rust/voices/durka42.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/ferrous-systems-jonathan.yaml  missing required field 'type'
FAIL  maps/rust/voices/ferrous-systems-jonathan.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/haricot.yaml  missing required field 'type'
FAIL  maps/rust/voices/haricot.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/ian-mcdonald.yaml  missing required field 'type'
FAIL  maps/rust/voices/ian-mcdonald.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/ian-whitney-blog-post-rust-via-its-core-values-cited.yaml  missing required field 'type'
FAIL  maps/rust/voices/ian-whitney-blog-post-rust-via-its-core-values-cited.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/im-lunex.yaml  missing required field 'type'
FAIL  maps/rust/voices/im-lunex.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/inactive-user.yaml  missing required field 'type'
FAIL  maps/rust/voices/inactive-user.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/jackdk.yaml  missing required field 'type'
FAIL  maps/rust/voices/jackdk.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/jasn-armstrng.yaml  missing required field 'type'
FAIL  maps/rust/voices/jasn-armstrng.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/jumpnbrownweasel.yaml  missing required field 'type'
FAIL  maps/rust/voices/jumpnbrownweasel.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/justin-handville.yaml  missing required field 'type'
FAIL  maps/rust/voices/justin-handville.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/jvcmarcenes.yaml  missing required field 'type'
FAIL  maps/rust/voices/jvcmarcenes.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/kev009.yaml  missing required field 'type'
FAIL  maps/rust/voices/kev009.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/khimru.yaml  missing required field 'type'
FAIL  maps/rust/voices/khimru.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/kibwen.yaml  missing required field 'type'
FAIL  maps/rust/voices/kibwen.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/kingcol13.yaml  missing required field 'type'
FAIL  maps/rust/voices/kingcol13.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/kristoff.yaml  missing required field 'type'
FAIL  maps/rust/voices/kristoff.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/lake.yaml  missing required field 'type'
FAIL  maps/rust/voices/lake.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/lewis.yaml  missing required field 'type'
FAIL  maps/rust/voices/lewis.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/lilnasy.yaml  missing required field 'type'
FAIL  maps/rust/voices/lilnasy.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/lonjil.yaml  missing required field 'type'
FAIL  maps/rust/voices/lonjil.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/ltrlg.yaml  missing required field 'type'
FAIL  maps/rust/voices/ltrlg.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/madhadron.yaml  missing required field 'type'
FAIL  maps/rust/voices/madhadron.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/mattya.yaml  missing required field 'type'
FAIL  maps/rust/voices/mattya.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/mordecai-emmanuel-etukudo.yaml  missing required field 'type'
FAIL  maps/rust/voices/mordecai-emmanuel-etukudo.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/mtset.yaml  missing required field 'type'
FAIL  maps/rust/voices/mtset.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/nakedible.yaml  missing required field 'type'
FAIL  maps/rust/voices/nakedible.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/nick-kuntz.yaml  missing required field 'type'
FAIL  maps/rust/voices/nick-kuntz.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/nobody1707.yaml  missing required field 'type'
FAIL  maps/rust/voices/nobody1707.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/ouillie.yaml  missing required field 'type'
FAIL  maps/rust/voices/ouillie.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/pavel-perikov.yaml  missing required field 'type'
FAIL  maps/rust/voices/pavel-perikov.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/pickfire.yaml  missing required field 'type'
FAIL  maps/rust/voices/pickfire.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/pm.yaml  missing required field 'type'
FAIL  maps/rust/voices/pm.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/primoly.yaml  missing required field 'type'
FAIL  maps/rust/voices/primoly.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/quinedot.yaml  missing required field 'type'
FAIL  maps/rust/voices/quinedot.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/r-my-rakic-on-behalf-of-the-compiler-performance-working.yaml  missing required field 'type'
FAIL  maps/rust/voices/ralfjung.yaml  missing required field 'type'
FAIL  maps/rust/voices/renkenono.yaml  missing required field 'type'
FAIL  maps/rust/voices/renkenono.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/romgrk.yaml  missing required field 'type'
FAIL  maps/rust/voices/romgrk.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/rtpg.yaml  missing required field 'type'
FAIL  maps/rust/voices/rtpg.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/serdar-yegulalp-infoworld-senior-writer.yaml  missing required field 'type'
FAIL  maps/rust/voices/serdar-yegulalp-infoworld-senior-writer.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/simolus3.yaml  missing required field 'type'
FAIL  maps/rust/voices/simolus3.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/skifire13.yaml  missing required field 'type'
FAIL  maps/rust/voices/skifire13.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/smarcd.yaml  missing required field 'type'
FAIL  maps/rust/voices/smarcd.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/softmaximalist-pr-author-burn-contributor.yaml  missing required field 'type'
FAIL  maps/rust/voices/softmaximalist-pr-author-burn-contributor.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/st0rmbtw.yaml  missing required field 'type'
FAIL  maps/rust/voices/st0rmbtw.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/summer-rs-project-github-com-spring-rs-spring-rs-readme-now.yaml  missing required field 'type'
FAIL  maps/rust/voices/summer-rs-project-github-com-spring-rs-spring-rs-readme-now.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/superdump.yaml  missing required field 'type'
FAIL  maps/rust/voices/superdump.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/tapghoul.yaml  missing required field 'type'
FAIL  maps/rust/voices/tapghoul.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/ted-tso.yaml  missing required field 'type'
FAIL  maps/rust/voices/ted-tso.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/teohhanhui.yaml  missing required field 'type'
FAIL  maps/rust/voices/teohhanhui.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/tim-mccallum-bytecode-alliance.yaml  missing required field 'type'
FAIL  maps/rust/voices/tim-mccallum-bytecode-alliance.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/toastal.yaml  missing required field 'type'
FAIL  maps/rust/voices/toastal.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/totalkrill.yaml  missing required field 'type'
FAIL  maps/rust/voices/totalkrill.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/unidentified-reviewer.yaml  missing required field 'type'
FAIL  maps/rust/voices/unidentified-reviewer.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/urben1680.yaml  missing required field 'type'
FAIL  maps/rust/voices/urben1680.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/vangata-ve.yaml  missing required field 'type'
FAIL  maps/rust/voices/vangata-ve.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/vitalyd.yaml  missing required field 'type'
FAIL  maps/rust/voices/vitalyd.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/vorpal.yaml  missing required field 'type'
FAIL  maps/rust/voices/vorpal.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/vri.yaml  missing required field 'type'
FAIL  maps/rust/voices/vri.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/wandbrandon.yaml  missing required field 'type'
FAIL  maps/rust/voices/wandbrandon.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/wofo-quoting-the-dropshot-projects-own-stated-design-goal.yaml  missing required field 'type'
FAIL  maps/rust/voices/wofo-quoting-the-dropshot-projects-own-stated-design-goal.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/yakira-neko.yaml  missing required field 'type'
FAIL  maps/rust/voices/yakira-neko.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/yawaramin.yaml  missing required field 'type'
FAIL  maps/rust/voices/yawaramin.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/yinho999.yaml  missing required field 'type'
FAIL  maps/rust/voices/yinho999.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/ysalitrynskyi.yaml  missing required field 'type'
FAIL  maps/rust/voices/ysalitrynskyi.yaml  missing required field 'track_record'
FAIL  maps/rust/voices/zackw.yaml  missing required field 'type'
FAIL  maps/rust/voices/zackw.yaml  missing required field 'track_record'
FAIL  maps/rust/claims/a-sB01-f000149-c1.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB01-f000149-c2.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB01-f000149-c3.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB01-f000227-c1.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB01-f000227-c2.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB01-f000227-c3.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB01-f000227-c4.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c1.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c10.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c11.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c12.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c13.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c14.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c15.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c16.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c17.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c2.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c3.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c4.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c5.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c6.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c7.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c8.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB02-f000256-c9.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB04-f000227-c1.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB04-f000227-c2.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB04-f000227-c3.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB04-f000227-c4.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB04-f000227-c5.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sR01-f000227-c1.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sR01-f000227-c2.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sa15-f005516-c1.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sa28-f012469-c9.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk02-f000256-c1.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk02-f000256-c10.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk02-f000256-c11.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk02-f000256-c12.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk02-f000256-c13.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk02-f000256-c2.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk02-f000256-c3.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk02-f000256-c4.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk02-f000256-c5.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk02-f000256-c6.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk02-f000256-c7.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk02-f000256-c8.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk02-f000256-c9.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c1.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c10.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c11.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c12.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c13.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c14.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c15.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c16.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c17.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c2.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c3.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c4.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c5.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c6.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c7.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c8.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-bk03-f000267-c9.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-sR01-f000233-c1.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-sR01-f000233-c2.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-sR01-f000256-c1.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-sb18-f005332-c1.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-sb18-f005332-c2.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-sb18-f005332-c3.yaml  missing required field 'date'
FAIL  maps/rust/claims/b-sb18-f005332-c4.yaml  missing required field 'date'
FAIL  maps/rust/sources/f000149.yaml  missing required field 'date'
FAIL  maps/rust/sources/f000217.yaml  missing required field 'date'
FAIL  maps/rust/sources/f000227.yaml  missing required field 'date'
FAIL  maps/rust/sources/f000233.yaml  missing required field 'date'
FAIL  maps/rust/sources/f000256.yaml  missing required field 'date'
FAIL  maps/rust/sources/f000267.yaml  missing required field 'date'
FAIL  maps/rust/claims/a-sB01-f000149-c1.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB01-f000149-c2.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB01-f000149-c3.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB01-f000227-c1.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB01-f000227-c2.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB01-f000227-c3.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB01-f000227-c4.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c1.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c10.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c11.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c12.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c13.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c14.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c15.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c16.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c17.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c2.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c3.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c4.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c5.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c6.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c7.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c8.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB02-f000256-c9.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB04-f000227-c1.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB04-f000227-c2.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB04-f000227-c3.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB04-f000227-c4.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sB04-f000227-c5.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sR01-f000227-c1.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sR01-f000227-c2.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sa15-f005516-c1.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/a-sa28-f012469-c9.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk02-f000256-c1.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk02-f000256-c10.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk02-f000256-c11.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk02-f000256-c12.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk02-f000256-c13.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk02-f000256-c2.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk02-f000256-c3.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk02-f000256-c4.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk02-f000256-c5.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk02-f000256-c6.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk02-f000256-c7.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk02-f000256-c8.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk02-f000256-c9.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c1.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c10.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c11.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c12.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c13.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c14.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c15.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c16.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c17.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c2.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c3.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c4.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c5.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c6.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c7.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c8.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-bk03-f000267-c9.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-sR01-f000233-c1.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-sR01-f000233-c2.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-sR01-f000256-c1.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-sb18-f005332-c1.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-sb18-f005332-c2.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-sb18-f005332-c3.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/claims/b-sb18-f005332-c4.yaml  date 'None' is not ISO (YYYY-MM-DD)
FAIL  maps/rust/voices/2e71828.yaml  no track_record line with a url
FAIL  maps/rust/voices/afetisov.yaml  no track_record line with a url
FAIL  maps/rust/voices/ajdecon.yaml  no track_record line with a url
FAIL  maps/rust/voices/alandekok.yaml  no track_record line with a url
FAIL  maps/rust/voices/alonely0.yaml  no track_record line with a url
FAIL  maps/rust/voices/andrei-alexandrescu-creator-of-d.yaml  no track_record line with a url
FAIL  maps/rust/voices/anthonygrondin.yaml  no track_record line with a url
FAIL  maps/rust/voices/badeend.yaml  no track_record line with a url
FAIL  maps/rust/voices/bjoernq.yaml  no track_record line with a url
FAIL  maps/rust/voices/bogdan-petru.yaml  no track_record line with a url
FAIL  maps/rust/voices/bruce-perens.yaml  no track_record line with a url
FAIL  maps/rust/voices/bsder.yaml  no track_record line with a url
FAIL  maps/rust/voices/bstrie-attribution-hedged-by-the-poster-themselves-im.yaml  no track_record line with a url
FAIL  maps/rust/voices/chayan-mistry.yaml  no track_record line with a url
FAIL  maps/rust/voices/chescock.yaml  no track_record line with a url
FAIL  maps/rust/voices/co-presenter-taj-touch-unclear.yaml  no track_record line with a url
FAIL  maps/rust/voices/coreh.yaml  no track_record line with a url
FAIL  maps/rust/voices/crazyboyqcd.yaml  no track_record line with a url
FAIL  maps/rust/voices/danieljoyce.yaml  no track_record line with a url
FAIL  maps/rust/voices/dataangel.yaml  no track_record line with a url
FAIL  maps/rust/voices/david-chisnall.yaml  no track_record line with a url
FAIL  maps/rust/voices/dhruv-ahuja.yaml  no track_record line with a url
FAIL  maps/rust/voices/durka42.yaml  no track_record line with a url
FAIL  maps/rust/voices/ferrous-systems-jonathan.yaml  no track_record line with a url
FAIL  maps/rust/voices/haricot.yaml  no track_record line with a url
FAIL  maps/rust/voices/ian-mcdonald.yaml  no track_record line with a url
FAIL  maps/rust/voices/ian-whitney-blog-post-rust-via-its-core-values-cited.yaml  no track_record line with a url
FAIL  maps/rust/voices/im-lunex.yaml  no track_record line with a url
FAIL  maps/rust/voices/inactive-user.yaml  no track_record line with a url
FAIL  maps/rust/voices/jackdk.yaml  no track_record line with a url
FAIL  maps/rust/voices/jamesmunns.yaml  no track_record line with a url
FAIL  maps/rust/voices/jasn-armstrng.yaml  no track_record line with a url
FAIL  maps/rust/voices/jessebraham.yaml  no track_record line with a url
FAIL  maps/rust/voices/jumpnbrownweasel.yaml  no track_record line with a url
FAIL  maps/rust/voices/justin-handville.yaml  no track_record line with a url
FAIL  maps/rust/voices/jvcmarcenes.yaml  no track_record line with a url
FAIL  maps/rust/voices/kev009.yaml  no track_record line with a url
FAIL  maps/rust/voices/khimru.yaml  no track_record line with a url
FAIL  maps/rust/voices/kibwen.yaml  no track_record line with a url
FAIL  maps/rust/voices/kingcol13.yaml  no track_record line with a url
FAIL  maps/rust/voices/kristoff.yaml  no track_record line with a url
FAIL  maps/rust/voices/laggui.yaml  no track_record line with a url
FAIL  maps/rust/voices/lake.yaml  no track_record line with a url
FAIL  maps/rust/voices/lewis.yaml  no track_record line with a url
FAIL  maps/rust/voices/lilnasy.yaml  no track_record line with a url
FAIL  maps/rust/voices/lonjil.yaml  no track_record line with a url
FAIL  maps/rust/voices/ltrlg.yaml  no track_record line with a url
FAIL  maps/rust/voices/madhadron.yaml  no track_record line with a url
FAIL  maps/rust/voices/mattya.yaml  no track_record line with a url
FAIL  maps/rust/voices/mordecai-emmanuel-etukudo.yaml  no track_record line with a url
FAIL  maps/rust/voices/mtset.yaml  no track_record line with a url
FAIL  maps/rust/voices/nakedible.yaml  no track_record line with a url
FAIL  maps/rust/voices/nick-kuntz.yaml  no track_record line with a url
FAIL  maps/rust/voices/nobody1707.yaml  no track_record line with a url
FAIL  maps/rust/voices/ouillie.yaml  no track_record line with a url
FAIL  maps/rust/voices/pavel-perikov.yaml  no track_record line with a url
FAIL  maps/rust/voices/pickfire.yaml  no track_record line with a url
FAIL  maps/rust/voices/pm.yaml  no track_record line with a url
FAIL  maps/rust/voices/primoly.yaml  no track_record line with a url
FAIL  maps/rust/voices/quinedot.yaml  no track_record line with a url
FAIL  maps/rust/voices/renkenono.yaml  no track_record line with a url
FAIL  maps/rust/voices/romgrk.yaml  no track_record line with a url
FAIL  maps/rust/voices/rtpg.yaml  no track_record line with a url
FAIL  maps/rust/voices/serdar-yegulalp-infoworld-senior-writer.yaml  no track_record line with a url
FAIL  maps/rust/voices/simolus3.yaml  no track_record line with a url
FAIL  maps/rust/voices/skifire13.yaml  no track_record line with a url
FAIL  maps/rust/voices/smarcd.yaml  no track_record line with a url
FAIL  maps/rust/voices/softmaximalist-pr-author-burn-contributor.yaml  no track_record line with a url
FAIL  maps/rust/voices/ssokolow.yaml  no track_record line with a url
FAIL  maps/rust/voices/st0rmbtw.yaml  no track_record line with a url
FAIL  maps/rust/voices/stefan-baumgartner.yaml  no track_record line with a url
FAIL  maps/rust/voices/summer-rs-project-github-com-spring-rs-spring-rs-readme-now.yaml  no track_record line with a url
FAIL  maps/rust/voices/superdump.yaml  no track_record line with a url
FAIL  maps/rust/voices/tapghoul.yaml  no track_record line with a url
FAIL  maps/rust/voices/ted-tso.yaml  no track_record line with a url
FAIL  maps/rust/voices/teohhanhui.yaml  no track_record line with a url
FAIL  maps/rust/voices/tim-mccallum-bytecode-alliance.yaml  no track_record line with a url
FAIL  maps/rust/voices/toastal.yaml  no track_record line with a url
FAIL  maps/rust/voices/totalkrill.yaml  no track_record line with a url
FAIL  maps/rust/voices/unidentified-reviewer.yaml  no track_record line with a url
FAIL  maps/rust/voices/urben1680.yaml  no track_record line with a url
FAIL  maps/rust/voices/vangata-ve.yaml  no track_record line with a url
FAIL  maps/rust/voices/vaultwarden-maintainers-dani-garcia-vaultwarden.yaml  no track_record line with a url
FAIL  maps/rust/voices/vitalyd.yaml  no track_record line with a url
FAIL  maps/rust/voices/vorpal.yaml  no track_record line with a url
FAIL  maps/rust/voices/vri.yaml  no track_record line with a url
FAIL  maps/rust/voices/wandbrandon.yaml  no track_record line with a url
FAIL  maps/rust/voices/warre-snaet.yaml  no track_record line with a url
FAIL  maps/rust/voices/wofo-quoting-the-dropshot-projects-own-stated-design-goal.yaml  no track_record line with a url
FAIL  maps/rust/voices/yakira-neko.yaml  no track_record line with a url
FAIL  maps/rust/voices/yanshay.yaml  no track_record line with a url
FAIL  maps/rust/voices/yatekii.yaml  no track_record line with a url
FAIL  maps/rust/voices/yawaramin.yaml  no track_record line with a url
FAIL  maps/rust/voices/yinho999.yaml  no track_record line with a url
FAIL  maps/rust/voices/ysalitrynskyi.yaml  no track_record line with a url
FAIL  maps/rust/voices/zackw.yaml  no track_record line with a url

counts per kind:
  question: 401
  position: 607
  argument: 0
  value: 6
  voice: 374
  claim: 771
  source: 267
  convention: 0
  domain: 12
  concept: 1447
per stratum (domain):
  cloud-workers: questions open=38 closed=0
  core: questions open=209 closed=0
  decentralized-iroh: questions open=41 closed=0
  desktop-cli-ui: questions open=44 closed=0
  distributed: questions open=58 closed=0
  embedded: questions open=70 closed=0
  frontend: questions open=25 closed=0
  ml: questions open=42 closed=0
  other: questions open=22 closed=0
  swift-interop: questions open=8 closed=0
  wasm: questions open=71 closed=0
  web: questions open=56 closed=0
claims confirmed (resolved to a Position): 769 / 771
voices: 374

map: 427 FAIL
```
