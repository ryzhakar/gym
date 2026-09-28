# t4 census gate, audit, merge and merge check — instructions (batch n)

Frozen for batch 2 (2026-09-28). No rule changes until batch 2's closure file is written. Change log and grounds: RECON/batch-2-prep.md.

Read RECON/prompts/common.md first; it binds you. You read both teams' work; no extractor ever does.

Order: census gate → t4-audit → t4-merge → t4-merge-check → estimate.py.

## Census gate (script, no agent)

Run `uv run python GYM/scripts/map/census.py --recon RECON --batch n --out RECON/audit/`. It writes `audit/census-b{n}.md` and `audit/census-b{n}-population.csv`, and exits 1 while any row is flagged: a malformed read-log line, a Nothing new row without a valid `reason-code:` and `reason:`, or a reason that uses the opposition vocabulary.

On exit 1, give the flagged rows of each team to one fresh extractor per team per ≤15 rows, under `prompts/t2-extract.md` unchanged. It writes `team-TEAM/readlog-b{n}-fixK.csv` and `extract-b{n}-fixK.md`, which supersede earlier entries for those rows. Then re-run the census. The audit draws only after the census exits 0. A flagged row is not an audit miss.

## t4-audit (opus, never an extractor)

Row: PLAN line 132.
- Populations:
  - nothing-new: the rows of `audit/census-b{n}-population.csv` for the team;
  - dropped: `samples/bundles/b{n}-team-TEAM-manifest.csv` rows with status dropped;
  - Claims: every `- voice:` line in the team's `extract-b{n}-*.md`, with fix files superseding.
- Sample sizes per team:
  - nothing-new: max(5, ceil(10%));
  - dropped: every row;
  - Claims: 20, or all when there are fewer.
- Draw: one seed from `secrets.randbits(31)`, written to the audit file before any draw output exists, drawn once. RNG `random.Random(f"{SEED}-{team}")` over the sorted nothing-new ids, then over the file-ordered Claim list.
- Miss bar, fixed:
  - A nothing-new row is a miss when the source holds a Voice, with a Rust connection shown in the source, who declares a decision Rust practitioners make differently, with a reason or against a named alternative, and the extractor did not log it. Opposition inside the source is not required.
  - Off-subject content is correctly nothing-new.
  - A dropped row is a miss when it is on-subject.
  - One miss fails that team's batch, which goes back to fresh extractors (PLAN § 4).
- Strike bar, fixed: a sampled Claim is struck when it fails rule 3, 8 or 9 of `prompts/t2-extract.md`.
  - Struck Claims are listed and never reach the merge.
  - Report the strike rate per team with its 95% Wilson interval.
  - When 3 or more of a team's 20 are struck, check every Claim of that team the same way before the merge: one run per 50 Claims.
- Output: RECON/audit/audit-b{n}.md, headed with the seed, the populations, the samples, and a verdict per row. The last line names the teams whose verdict is PASS, for `--audit-pass`.

## t4-merge (opus)

Row: PLAN line 130. Closure inputs: PLAN lines 165–218. Schema of ids: PLAN lines 220–339.
1. Read every RECON/team-a/extract-b{n}-*.md and RECON/team-b/extract-b{n}-*.md. Fix files and L-slices supersede the earlier entries for their rows. Leave out the Claims the audit struck.
2. Merge duplicate Questions and Positions into canonical ids. From batch 2 on, merge into the canonical ids of the prior batches' binding crosswalk (batch 1: `merge-v3/crosswalk-b1.csv`).
3. Apply the grain rule below, verbatim from `merge-v3/merged-questions-b1.md` § The grain rule (lead ruling 2026-09-28). "Below" in its last line means your `merged-questions-b{n}.md`:

   > A Question names concrete alternatives a practitioner picks between at one point of work: crates, patterns, language features, project policies.
   >
   > - A trade-off between Values is a Value conflict carried by Arguments, never a Question. Examples: performance vs simplicity, stopgap vs proper fix, safety vs ergonomics.
   > - "Choose Rust for X" is one Question per domain X.
   > - Context variants of one concrete choice stay one Question, with the contexts recorded as Domains and Positions.
   > - Every multi-member Question below carries a "Grouping" line giving its reason.

4. Normalize Voice ids, one id per person:
   - The id is the lowercase slug (letters and digits, runs of anything else become `-`) of the account handle the source shows: a GitHub, forum or Lobsters login.
   - With no handle, use the full name as the source spells it. For a non-Latin name, use the Voice's own Latin spelling when the source shows one, else pinyin (zh) or the national romanization (uk: KMU 2010).
   - Never put a role, employer, project, affiliation or caveat in the id.
   - Before minting an id, look in GYM/maps/rust/voices/ (read only) and in this batch for the same person: the same handle on the same platform, or a source that links the name to the handle. Reuse that id.
   - Two similar names stay two Voices until a source proves they are one person (directive rule 5).
   - List every id that joins more than one spelling in `merged-questions-b{n}.md` § Voice ids: the id, the spellings seen, and the linking source.
5. Write to RECON/merge-b{n}/, a directory that holds only binding crosswalks: first copy each prior batch's binding crosswalk into it under its own name (batch 1: `merge-v3/crosswalk-b1.csv`). `RECON/merge/` holds a superseded batch-1 crosswalk and is never an input. Then write RECON/merge-b{n}/crosswalk-b{n}.csv, with batch 1's columns (batch, stratum, team, source_id, question_id, source_hint, team_local_id), the input `scripts/map/estimate.py` reads, and RECON/merge-b{n}/merged-questions-b{n}.md: canonical Questions, Positions, and Claims with Voice id, Source, date and locator, plus Domains and Concepts.

## t4-merge-check (opus, fresh to the merge)

Row: PLAN line 131.
- Draw 20% of the batch's candidate Questions with `uv run python -c`, using a seed from `secrets.randbits(31)` logged before the draw.
- For each sampled candidate, merge it blind: list every candidate Question of the whole batch, and every prior canonical id, it is the same Question as, under the grain rule above.
- Agreement, population reading: a sampled candidate agrees when its co-member set over the whole batch equals the merger's co-member set for it in `merge-b{n}/crosswalk-b{n}.csv`. The in-sample reading, with co-members restricted to the sample, may be reported beside it but never gates. Batch 1 showed the gap: population 78.0% against in-sample 95.4% (`slice-1-review.md` line 44).
- Gate: population agreement ≥ 90% passes. Below 90%, one full second merge and one adjudication follow (PLAN line 131), and the adjudicated crosswalk binds. There is no further re-merge or re-check in the batch, and the check's population figure is what goes to `estimate.py`.
- Output: RECON/merge-b{n}/merge-check-b{n}.md, with the seed, the sample, the verdict per item, and the population agreement with its 95% Wilson interval.

## estimate.py (script, no agent)

`uv run python GYM/scripts/map/estimate.py --crosswalk-dir RECON/merge-b{n}/ --batch n --out RECON/merge-b{n}/estimate/ --audit-pass <teams PASS in audit-b{n}.md> --merge-check-agreement <population agreement, as a fraction>`. Both flags are always passed, so part 3 of the rule measures instead of failing by construction.

End with a 3-sentence notification summary.
