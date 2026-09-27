# t2 extractor — instructions (team A and team B)

Read RECON/prompts/common.md first; it binds you. Directive variant: Tier 2 — read only your assigned sources; never search for, follow to, or add a source.

Your prompt names: TEAM (a or b), BATCH n, your agent id j, and your rows of RECON/samples/batch-n-team-TEAM.csv.

Framing, first line of your work:
- team a: "For each source: where do competent Rust practitioners disagree?"
- team b: "For each source: what must a Rust practitioner decide, and where do the sources conflict on it?"

Context to read first: GYM/docs/opinion-map.md § Language and § Evidence rules; GYM/docs/subjects/rust.md § Scope.

Skeleton and output formats: PLAN lines 368–386 (t2 extractor). Follow them exactly:
- OUTPUT 1: RECON/team-TEAM/readlog-bn-j.csv, header `frame_id,url,read,locator_span,new_questions,claims,minutes`
- OUTPUT 2: RECON/team-TEAM/extract-bn-j.md, one section per source (Questions, Claims, or Nothing new with its one-sentence reason).

Rules:
1. Read each source in full (transcript for talks; the whole thread for forums, following pagination).
2. Every row of your assignment appears in the read log exactly once: `read` = yes or unreachable. Unreachable: stop on it, say so, never reconstruct from memory.
3. A Claim needs the Voice's own words, a locator, a date. Code alone is never a Claim.
4. Domains: strata ids from common.md only.
5. Never open RECON/team-a/ if you are team b, or RECON/team-b/ if you are team a. Never open RECON/merge/, RECON/audit/, RECON/fill/.

End with a 3-sentence notification summary: sources read, unreachable, Questions and Claims logged.

Clarifications after the batch-1 audit (decided 2026-09-27 under the owner's 2026-09-26 handover):
6. A single Voice's declared Position on a decision Rust practitioners make differently is a Claim; log it with its Question even when nobody in the source disagrees. "Single-voice" or "no opposing view in this source" is never a reason for Nothing new. A release note, changelog, README or tutorial that states a decision together with the alternative it replaced or rejected holds a declared Position.
7. Text that is a stub, redirect, login or bot page, or under ~1,500 characters for a page that should be long, is `unreachable`, never `read`.
