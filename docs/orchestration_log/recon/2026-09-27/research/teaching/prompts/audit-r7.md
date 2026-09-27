# Saturation audit after rounds 6–7 — instructions

Read ROOT/prompts/audit-r5.md and ROOT/prompts/audit.md and follow them; they bind you. Changes:

1. Rounds 6 and 7 ran at the same time as two independent full-population captures (ROOT/prompts/round-6-7.md). Rules 1 and 2 use rounds 6 and 7 as the pair; rule 1's "two consecutive rounds" reads as these two captures.
2. Void rule: a database attempted with logged retries and blocked (HTTP 429/503, budget exhausted) counts as searched, not void (decided 2026-09-27 under the owner's 2026-09-26 handover); a database never attempted still voids the round.
3. Normalize axis strings before rule 5 (`skill_per_hour` = `skill per hour`, `skill/hour` likewise).
4. Seed coverage (rule 3): recompute from the ledger, as in your r5 audit.
5. Output ROOT/audit/saturation-r7.md; per need SATURATED / OPEN / VOID-ROUND, and for each OPEN need a round-8 brief from this audit's arithmetic only.
