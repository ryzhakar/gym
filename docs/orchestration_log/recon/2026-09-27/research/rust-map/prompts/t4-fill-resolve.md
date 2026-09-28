# t4 fill resolve — instructions (opus, fresh)

Frozen for batch 2 (2026-09-28). No rule changes until batch 2's fill resolution is written. Change log and grounds: RECON/batch-2-prep.md.

Read RECON/prompts/common.md first; it binds you. Row: PLAN § 2 table, t4-fill-resolve-b<n>: a third blind fill on disagreements, majority decides, and a three-way split is `unresolved`.

1. Join RECON/fill/run-a/positions-b{n}-*.csv and run-b/positions-b{n}-*.csv on (claim_id, question_id). If the merger wrote a remap for the batch (`merge-b{n}/fill-remap-b{n}.csv`), apply it to both first. List the rows present in only one run.
2. Agreements (same Position) pass. For every disagreement and every one-sided row, fill it yourself, blind to both runs' answers. Settle and write every third fill before you print or open anything that shows a run's answer for that row. Read the input entry (RECON/fill/input-b{n}-*.md) and, when needed, the source via `uv run python GYM/scripts/research/cache.py get <url>`. Pick a Position id, `none`, or `new position: <line>`.
3. Majority of the three decides. A three-way split is `unresolved`, excluded from the evidence minimum until an adjudicator reads the source.
4. Tags: where run-a and run-b tag a Position differently, decide by the same majority, with your own tag written blind to both. Where only one run tagged it, that tag and yours decide: equal passes, different is `unresolved`. Use the definitions `prompts/t3-fill.md` gave both runs, verbatim:
   - **fact**: a checkable claim about the world that evidence could settle;
   - **tradeoff**: each side buys something at a cost, and context decides;
   - **taste**: a preference of style, naming, norms or values that no evidence would settle.
5. Summaries: pick the summary that states the Position in its advocates' own terms, or merge the two without adding claims. Say per Position how it was picked.

Outputs:
- RECON/fill/resolved-b{n}.csv: claim_id, question_id, run_a, run_b, third, final, status (agree|majority|unresolved).
- RECON/fill/positions-final-b{n}.md: per Position, the final summary, tag and Claim ids.
- RECON/fill/resolve-b{n}.md: agreement rates before resolution for Positions and tags, counts, and every unresolved row.
- RECON/fill/checks-b{n}.csv, with columns question_id, subject (the claim_id for fill-position, the position id for fill-tag), check (fill-position|fill-tag), run_a, run_b, run_c, agree (true|false), resolution (majority|unresolved|empty when agree). One fill-position row per Claim and one fill-tag row per Position. Compile turns these into `MAP/checks/` records (schema kind `check`) so validator rule 4 can read them.

End with a 3-sentence notification summary.
