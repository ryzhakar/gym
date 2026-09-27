# t5-map-v3 — instructions

Read ROOT/prompts/t5-map-v2.md and follow it in full, with ROOT/prompts/t5-evidence-map.md; they bind you. Changes for v3:

1. Output ROOT/synthesis/evidence-map-v3.md; it supersedes evidence-map-v2.md. Say what changed from v2 and why, claim by claim, in "Changes from v2".
2. Status: the owner ruled the research complete on sources (2026-09-27, trace events.md). Collection stopped after round 8. The map is final on sources, work in progress on reading: say so in its first paragraph.
3. Confidence section: the verdict tables of ROOT/audit/saturation-r7.md, plus round 8's coverage estimates per need (ROOT/capture/r8-screen/n{k}-labels.csv tallied against ROOT/capture/r8{a,b}/n{k}-results.csv — run `uv run python /Users/ryzhakar/pp/gym/scripts/research/search.py tally` per need and paste the output). Declare each need's unseen fraction as a gap, never hidden.
4. Inputs add rounds 4–7 (ROOT/needs/n*-r4..r7.md), their verify files, ROOT/verify/found-dois-graded*.md. The last row per claim_id in claims-status.csv governs.
5. Unresolved disagreements: list every disagreement the round 4–7 need files and verify files flag (e.g. contextual interference lab vs field, expert tutors' diagnosis vs diagnosis-centric AI tutors); mark which ones would change the Pareto set if resolved the other way.
