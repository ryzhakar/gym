# t5-first-protocol — instructions

Read ROOT/prompts/common.md first; it binds you.

Skeleton and format: PLAN lines 384–402 (t5-first-protocol). Follow exactly.

Inputs, files only, nothing from your own knowledge:
- ROOT/context/rulings-brief.md, ROOT/context/substrate-audit.md
- ROOT/needs/n1-r1.md, n2-r1.md, n3-r1.md, n7-r1.md, breadth-r1.md
- ROOT/verify/claims/*.md
- ROOT/ledger/claims.csv (survey rows) and ROOT/ledger/claims-status.csv (verification status and re-grades; where they differ, claims-status.csv governs)
- ROOT/ledger/sources.csv

Rules:
1. Include only claims whose claims-status.csv row says VERIFIED with S≥2 and O≥1.
2. Each section: what the evidence supports, then what the first sessions therefore do, as a checklist the owner can act on and check. Not a design (ruling line 108): forbidden strings "the trainer should", "architecture", "mode", "ladder".
3. Cite a verify/claims file per claim. Carry every caveat a verification file records (population, delay, preprint-only, inferred numbers).
4. Population honesty: say when a claim was measured on K-12, undergraduates, or professionals.
5. Early measurement (PLAN §8 open point 8, default: unaided delayed probes capped at 10 minutes per session until N1 sets a figure): state the probe N1's verified claims support.
6. Section "Not covered yet": N4 diagnosis, N5 elite margin, N6 sustain — and what their absence means for the first sessions.

Output: ROOT/synthesis/first-protocol.md

End with a 3-sentence notification summary: claims used, what the first sessions do, the biggest open risk.
