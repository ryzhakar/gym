# t4 merge, merge check and audit — instructions (batch n)

Read RECON/prompts/common.md first; it binds you. You read both teams' work; no extractor ever does.

## t4-merge (opus, long-lived across batches)
Row: PLAN line 130; closure inputs: PLAN lines 165–218; schema of ids: PLAN lines 220–339.
1. Read every RECON/team-a/extract-b{n}-*.md and RECON/team-b/extract-b{n}-*.md (supplementary slices L1, L2 included; where an L-slice re-extracts a row, it supersedes that row's earlier entries).
2. Merge duplicate Questions and Positions into canonical ids; a Question is the same only when competent practitioners would argue the same decision, never by shared keywords.
3. Write RECON/merge/crosswalk-b{n}.csv (team, team-local Question id, canonical Question id, source frame_id) — the capture–recapture input for scripts/map/estimate.py — and RECON/merge/merged-questions-b{n}.md (canonical Question, Positions, Claims with Voice/Source/date/locator, Domains, Concepts).
4. From batch 2 on, merge into the prior crosswalks' canonical ids.

## t4-merge-check (opus, fresh to the merge)
Row: PLAN line 131. Draw the 20% sample with `uv run python -c` and a logged seed; merge it blind; report agreement to RECON/merge/merge-check-b{n}.md.

## t4-audit (opus, never an extractor)
Row: PLAN line 132. Sample 10% of `nothing new` read-log rows per team, and 10% of rows the bundler dropped (RECON/samples/bundles/b{n}-team-*-manifest.csv, status dropped), seeded; re-read each; one miss (a Question, Position or Claim the extractor should have logged, or a dropped row that is on-subject) fails that team's batch. Output RECON/audit/audit-b{n}.md.

End with a 3-sentence notification summary.
