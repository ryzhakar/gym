# t3 fill — instructions (blind duplicate Position assignment)

Frozen for batch 2 (2026-09-28). No rule changes until batch 2's fill resolution is written. Change log and grounds: RECON/batch-2-prep.md.

Read RECON/prompts/common.md first; it binds you. Row: PLAN § 2 table, t3-fill-a/t3-fill-b. Owner ruling: GYM/docs/subjects/rust.md § Research for the map ("filled twice, blind").

Your prompt names FILL (a or b), BATCH n, and one or more RECON/fill/input-b{n}-NN.md files.

1. For each Claim: which listed Position the Voice's own words support. Answer with a Position id, `none`, or `new position: <one line>`. Judge from the quote and the source. When the quote alone is ambiguous, open the source with `uv run python GYM/scripts/research/cache.py get <url>`. For a non-English source, judge from the original-language quote, not only the English paraphrase.
2. For each Position that has at least one Claim, write a one-paragraph summary in its advocates' own terms, with no verdict. Give it one tag (GYM/docs/opinion-map.md § Judgment), by these definitions, fixed for the batch:
   - **fact**: a checkable claim about the world that evidence could settle;
   - **tradeoff**: each side buys something at a cost, and context decides;
   - **taste**: a preference of style, naming, norms or values that no evidence would settle.

   The tag describes the Position as its advocates state it, not the Question as a whole. Use exactly one of the three words.
3. Never open RECON/fill/key-b{n}.csv, RECON/merge*/, or the other fill's outputs.

Outputs:
- RECON/fill/run-FILL/positions-b{n}-NN.csv, columns claim_id, question_id, position, confidence (high|low), reason;
- RECON/fill/run-FILL/summaries-b{n}-NN.md, per Position: summary, tag, Claim ids.

Batch 1's unsuffixed `positions-NN.csv` files stay as they are.

End with a 3-sentence notification summary.
