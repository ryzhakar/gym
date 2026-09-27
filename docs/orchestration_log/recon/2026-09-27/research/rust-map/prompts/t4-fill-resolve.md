# t4 fill resolve — instructions (opus, fresh)

Read RECON/prompts/common.md first; it binds you. Row: PLAN §2 table, t4-fill-resolve-b<n> (third blind fill on disagreements, majority; three-way split → `unresolved`).

1. Join RECON/fill/run-a/positions-*.csv and run-b/positions-*.csv on (claim_id, question_id); apply RECON/merge-v3/fill-remap-b1.csv to both first. List rows present in only one run.
2. Agreements (same Position) pass. For every disagreement and one-sided row, fill it yourself, blind to both runs' answers: read the input entry (RECON/fill/input-b1-*.md) and, when needed, the source via `uv run python GYM/scripts/research/cache.py get <url>`; pick a Position id, `none`, or `new position: <line>`.
3. Majority of the three decides; a three-way split is `unresolved` (excluded from the evidence minimum until an adjudicator reads the source).
4. Summaries and tags: where run-a and run-b tag a Position differently (fact/tradeoff/taste), decide by the same majority with your own tag; pick the summary that states the Position in its advocates' own terms, or merge the two without adding claims.

Outputs: RECON/fill/resolved-b1.csv (claim_id, question_id, run_a, run_b, third, final, status agree|majority|unresolved), RECON/fill/positions-final-b1.md (per Position: final summary, tag, Claim ids), RECON/fill/resolve-b1.md (agreement rate before resolution, counts, every unresolved row).

End with a 3-sentence notification summary.
