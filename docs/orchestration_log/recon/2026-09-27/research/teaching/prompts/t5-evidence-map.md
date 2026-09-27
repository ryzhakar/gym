# t5-evidence-map — instructions

Read ROOT/prompts/common.md first; it binds you.

Skeleton and format: PLAN lines 404–420 (t5-evidence-map). Follow exactly. Gate: PLAN lines 172–174 (reviewer greps for "the trainer should" and rejects).

Inputs, files only, nothing from your own knowledge — read every file under ROOT except ROOT/seed.md:
- ROOT/context/*, ROOT/index/index.md (statistics and dispute sections), ROOT/index/exclusion-register.md
- ROOT/needs/*.md (all rounds; later rounds may exist — use every round present)
- ROOT/verify/claims/*.md, ROOT/verify/seed-probe.md, ROOT/verify/calibration-set.md
- ROOT/resolve/*.md
- ROOT/ledger/claims.csv, ROOT/ledger/sources.csv, ROOT/ledger/claims-status.csv (append-only: the LAST row per claim_id governs status and grades; blank S/R/O in that row fall back to the claim's latest non-blank grades; verified_by labels are unreliable, the verify file is authoritative)
- ROOT/synthesis/first-protocol.md (the Stage A brief this map replaces)

Rules:
1. Claims enter the Pareto table and recommendations only with status VERIFIED, O≥1. SURVEYED, UNVERIFIABLE and O=0 claims are reported in their need tables with their status, never promoted.
2. Carry every scope correction the resolutions and verification files record.
3. Calibration to the owner reads rulings 118–121 from ROOT/context/rulings-brief.md in that section only.
4. Coverage and confidence: report seed coverage from verify/seed-probe.md; note that seed coverage for knowledge-component and struggle/intervention blocks from round 3 on is not an independent measure (orchestrator prompt leak, recorded).
5. Say where the first-protocol.md checklist changes because of later evidence.
6. Not a design: forbidden strings "the trainer should", "architecture", "mode", "ladder".

Output: ROOT/synthesis/evidence-map.md

End with a 3-sentence notification summary: answer in one sentence, the Pareto set, the biggest gap.
