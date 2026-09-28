# t5 compile — instructions (batch n)

Frozen for batch 2 (2026-09-28). Change log and grounds: RECON/batch-2-prep.md.

Read RECON/prompts/common.md first; it binds you. Row: PLAN line 141. MAP = GYM/maps/rust; its shape is MAP/schema.yaml, and nothing else declares a kind, field or enum.

You transcribe; you never author. Every value you write comes from a named input file. Where an input holds no value for a required field, leave the field unset and list it; never infer, merge, split, reword or judge. You may write a script for the transcription (batch 1's is `compile/compile.py`); reuse its mechanical rules, named below, so both batches read one way.

## Stages

The lead's dispatch names the stage. Each stage appends one section to RECON/compile/compile-b{n}.md and ends with a validator run.

**A — entities and fill checks.** Runs after t4-fill-resolve.

Inputs:
- `merge-b{n}/merged-questions-b{n}.md`, including § Voice ids;
- `merge-b{n}/crosswalk-b{n}.csv`;
- `fill/resolved-b{n}.csv`, `fill/positions-final-b{n}.md`, `fill/resolve-b{n}.md`, `fill/checks-b{n}.csv`;
- `audit/audit-b{n}.md`, for the struck Claims;
- `samples/batch-{n}-team-{a,b}.csv`, `frame/frame.csv` and `frame/frame-v2-nonen.csv`, for Source fields.

1. **Questions.** A canonical id new to MAP gets a file: text, concepts, domains, `status: open`. An id already in MAP keeps its file. Add only domains and concepts the merged file gives it that the file lacks, and list each addition.
2. **Positions.**
   - A new id gets its final summary and tag from `positions-final-b{n}.md`; an `unresolved` tag leaves `tag` unset, and the Position is listed.
   - An existing id keeps its summary and tag. When batch n's final summary or tag differs, list both in § Not applied; the lead rules.
3. **Claims.** One file per `resolved-b{n}.csv` row, id = claim_id.
   - `position` = final. A final of `unresolved` is written as `position: unresolved`.
   - A final of `none` or `new position: …` is not written; list it.
   - A Claim the audit struck is never written.
   - Fields come from the merged file: voice (the normalized id), source (the frame id), date, locator, paraphrase, quote.
   - Dates follow compile.py `normalize_date`: keep a leading ISO date and drop a trailing time or qualifier; leave the date unset when there is no day-precision date.
   - Quotes over 300 characters follow compile.py `truncate_quote`.
   - A `voice-unverified` flag or a caveat from the extract goes to `gap`, joined with "; ".
   - `practiced: unknown`.
4. **Voices.** A Voice id new to MAP gets a file holding `name`. `type` and `track_record` are left for the Voice pass, and their validator FAILs are expected and listed. An existing Voice file is not touched.
5. **Sources.** A frame id new to MAP gets a file: url, title, date and language from its frame row; `kind` by compile.py `classify_kind`; `frame: {batch: n, team: <a|b|a;b>, class: <frame class>}`.
6. **Concepts.** One entity per distinct phrase not already in MAP, using compile.py `slugify` and its id-collision rule (numeric suffix, listed).
7. **Checks.** Each row of `fill/checks-b{n}.csv` becomes one record appended to `MAP/checks/<subject>.yaml`. The subject is the claim id for fill-position and the position id for fill-tag.
   - The record is `{check, run_a: {<field>: <value>}, run_b: {…}, run_c: {…} only when a third fill exists, agree, resolution only when present}`. The field is `position` for fill-position and `tag` for fill-tag.
   - Existing records in the file are kept.
   - Batch 1 has no such CSV. Its checks can be derived the same way from `fill/resolved-b1.csv` and `fill/resolve-b1.md` § Tags when the dispatch names batch 1. The `fill/run-{a,b}/` summaries hold the runs' tags.

**B — Voice pass.** Runs after t3-voice and its calibration for batch n: `verify/voices-b{n}-*.md` and `verify/voices-calibration-b{n}.md`.
- Write `name`, `type`, `track_record` and `influence` as the files give them.
- Merge the same-person id pairs the calibration lists: keep one id, repoint the Claims, and list the pairs.
- Add `voice-below-bar` (FAILS) or `voice-unverified` (UNKNOWN) to the Voice's Claims' `gap`, as batch 1 did (`compile-b1.md` § Voice-verification pass).

**C — Claim pass.** Runs after t3-claim adjudication for batch n (`verify/claims-final-b{n}.csv`).
- Apply corrected locator, date and paraphrase, and `drop_quote`.
- Write `practiced` where it is not `unknown`.
- A non-CONFIRMED verdict goes into `gap` as one line, as batch 1 did (`compile-b1.md` § Claim-verification pass).

**D — Arguments.** Runs after t3-args (`args/arguments-<chunk>.md` for the chunks the dispatch names).
- One file per Argument in MAP/arguments/, with position, side, text, values and sources exactly as the file gives them.
- A `value-candidate:` Argument is not written; list it.
- A Position marked `no argument in sources` is listed.

## Validator

After every stage: `uv run python GYM/scripts/map/check_map.py --map GYM/maps/rust`. Paste its output verbatim into the stage's section of compile-b{n}.md, with FAIL counts by rule, before and after the stage.
- Fix only format failures your own transcription caused: a mis-cased enum, a wrong id, a missing required field whose value is in an input.
- Every other FAIL stays and is listed with the input that lacks the value.

## Scope

- Write only MAP/** and RECON/compile/compile-b{n}.md, plus your script under RECON/compile/.
- Never open RECON/team-a/ or team-b/. Read extracts only through the merged file.
- Never edit `MAP/schema.yaml`. A needed field it lacks goes to compile-b{n}.md § Schema notes.
- Update MAP/README.md counts only: the numbers per kind and the batch list.

End with a 3-sentence notification summary: stage, files written per kind, and validator FAIL count.
