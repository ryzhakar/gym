# t3 fill — instructions (blind duplicate Position assignment)

Read RECON/prompts/common.md first; it binds you. Row: PLAN §2 table, t3-fill-a/t3-fill-b; owner ruling in GYM/docs/subjects/rust.md § Research for the map ("filled twice, blind").

Your prompt names FILL (a or b) and one or more RECON/fill/input-b1-NN.md files.

1. For each Claim: which listed Position does the Voice's own words support — a Position id, `none`, or `new position: <one line>`. Judge from the quote and the source (open the source via `uv run python GYM/scripts/research/cache.py get <url>` when the quote alone is ambiguous).
2. For each Position that has at least one Claim: a one-paragraph summary in its advocates' own terms (no verdict), and a tag fact / tradeoff / taste (GYM/docs/opinion-map.md § Judgment).
3. Never open RECON/fill/key-b1.csv, RECON/merge*/, or the other fill's outputs.

Outputs: RECON/fill/run-FILL/positions-NN.csv (claim_id,question_id,position,confidence high|low,reason) and RECON/fill/run-FILL/summaries-NN.md (per Position: summary, tag, Claim ids).

End with a 3-sentence notification summary.
