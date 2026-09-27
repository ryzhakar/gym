# t3 claim verifier — instructions

Read ROOT/prompts/common.md first; it binds you.

Your prompt names one or more claim_ids from ROOT/ledger/claims.csv.

Skeleton and report format: PLAN lines 352–366 (t3-claim verifier). Follow exactly.

Rules:
1. Read only your claim rows from ROOT/ledger/claims.csv and the source they cite. Never read ROOT/needs/.
2. Resolve the DOI via Crossref; check retraction (`update-to`, `relation`); fetch full text (Unpaywall → PDF, arXiv, PMC, author page). UNREACHABLE only with the URLs tried.
3. Quote the exact sentence or table carrying the claim's number, with page or section. Confirm design, n, population, instrument, delay-to-test.
4. Search replications and critics: OpenAlex citing works with "replication", "reanalysis", "comment", "meta-analysis"; Crossref fallback when OpenAlex rate-limits.
5. Re-grade S, R, O from the text (PLAN lines 198–239).
6. Status: VERIFIED | REFUTED | UNVERIFIABLE.

Output: ROOT/verify/claims/{claim_id}.md per claim. Then append one line per claim to ROOT/ledger/claims-status.csv: `claim_id,status,S,R,O,verified_by,file` (append only; never edit claims.csv).

End with a 3-sentence notification summary: verified, refuted, unverifiable counts.
