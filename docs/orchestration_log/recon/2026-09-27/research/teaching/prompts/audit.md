# Saturation audit — instructions

Read ROOT/prompts/common.md first; it binds you.

Rules to compute: PLAN §5 lines 242–260 (five per-need saturation conditions, void-round rules). Decided thresholds: unseen ≤10% of S≥2 sources, and the Stage C cap of three rounds (after round 3 the map ships with this audit as its confidence section).

Inputs: ROOT/ledger/sources.csv (columns found_by_agent, round, needs, S), ROOT/ledger/claims.csv, ROOT/ledger/claims-status.csv (last row per claim_id governs), the search-log sections of every ROOT/needs/n*-r*.md and breadth-r*.md, ROOT/verify/seed-probe.md.

Compute per need N1–N7, showing the arithmetic in the report (you are a calculator; no script file is kept — do throwaway arithmetic with `uv run python -c` in /tmp and paste inputs and outputs):
1. Per round: sources tagged to the need; new vs already seen (by normalized DOI/URL); new with S≥3; new with S=2.
2. Rule 1: two consecutive rounds with zero new S≥3 and ≤1 new S=2 — PASS/FAIL.
3. Rule 2: Lincoln–Petersen on DOIs between the two most recent rounds for S≥2 sources: n1, n2, m, N̂ = n1·n2/m (Chapman form (n1+1)(n2+1)/(m+1)−1 when m is small), seen, unseen fraction — PASS if ≤10%; m=0 is FAIL (estimate undefined).
4. Rule 3: seed coverage from seed-probe.md per need (≥80% of S≥2 seed citations found independently) — PASS/FAIL; note the round-3 N2/N3 prompt leak.
5. Rule 4: every claim for the need VERIFIED, REFUTED or UNVERIFIABLE — count SURVEYED left.
6. Rule 5: each axis (skill per hour, durability, transfer, sustainability) holds ≥1 VERIFIED claim or a logged "no evidence" entry.
7. Void rounds: flag any round whose log lacks queries, databases or hit counts, or reuses >30% of a prior round's queries.
8. Verdict per need: SATURATED / OPEN / VOID-ROUND.

Output: ROOT/audit/saturation-r3.md — one table per rule, one verdict table, the arithmetic, and a paragraph per need on what the gap is.

End with a 3-sentence notification summary.
