# Saturation audit after round 5 — instructions

Read ROOT/prompts/audit.md and follow it in full; it binds you. Changes:

1. Rounds in scope: all rounds present (1–5); rules 1 and 2 use the two most recent rounds, 4 and 5.
2. Rule 2 inputs: the `## Found DOIs` sections of ROOT/needs/n{k}-r4.md and n{k}-r5.md (new and seen both count as captured), restricted to sources with S≥2 in ROOT/ledger/sources.csv; normalize DOIs (lowercase, strip `https://doi.org/`). A need whose r4 or r5 file lacks the section is VOID-ROUND for rule 2.
3. No Stage C cap: the owner's ruling is "done at saturation" (trace events.md line 116). A need that is not SATURATED gets a one-paragraph brief of what round 6 should look for, drawn only from this audit's arithmetic and the claims' gaps, never from outside knowledge.
4. Rule 4 reads ROOT/ledger/claims-status.csv, last row per claim_id governs; claims with S≤2 need no verification and count as closed for rule 4.

Output: ROOT/audit/saturation-r5.md.

End with a 3-sentence notification summary: verdict per need, the round-6 needs, the biggest gap.
