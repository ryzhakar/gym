# t2 extractor — instructions (team A and team B)

Frozen for batch 2 (2026-09-28). No rule changes until batch 2's audit, merge check and census are written. Change log and grounds: RECON/batch-2-prep.md.

Read RECON/prompts/common.md first; it binds you. Directive variant: Tier 2. Read only your assigned sources; never search for a source, follow a link to one, or add one.

Your prompt names TEAM (a or b), BATCH n, your agent id j, and your rows of RECON/samples/batch-n-team-TEAM.csv.

Framing, first line of your work:
- team a: "For each source: where do competent Rust practitioners disagree?"
- team b: "For each source: what must a Rust practitioner decide, and where do the sources conflict on it?"

Context to read first: GYM/docs/opinion-map.md § Language and § Evidence rules; GYM/docs/subjects/rust.md § Scope.

Skeleton: PLAN lines 368–386 (t2 extractor). Where this file differs from it, this file wins.

## Outputs

- OUTPUT 1: RECON/team-TEAM/readlog-bn-j.csv, header `frame_id,url,read,locator_span,new_questions,claims,minutes`. Exactly 7 fields per line. Quote any field that holds a comma. `new_questions` and `claims` are integers; the reason for a zero goes in the extract, never in these columns.
- OUTPUT 2: RECON/team-TEAM/extract-bn-j.md. One section per source, headed `## {frame_id} — {title} ({date}, {language})`, holding `### Questions` and `### Claims`, or `### Nothing new` alone.
- Claim line: `- voice: <name or handle exactly as the source shows it> | connection: <the Rust connection the source shows> | position: <label> | date: YYYY-MM-DD | locator: <...> | paraphrase: <...> | quote: "<≤1, short>" | practiced_evidence: <repo url or none> | flag: voice-unverified`. The `voice:` field holds the name or handle only, with no role, employer, affiliation or caveat. Those go in `connection:`.
- Nothing new block, exactly these two lines:
  ```
  ### Nothing new
  reason-code: off-subject | no-decision | no-rust-voice
  reason: <one sentence>
  ```
  - `off-subject`: the source holds no decision about Rust.
  - `no-decision`: Rust content, but no declared Position (rule 8).
  - `no-rust-voice`: the only declared Positions come from Voices with no Rust connection in the source (rule 9).

  The reason sentence says what the source contains. It never cites the absence of disagreement, opposition, dispute, pushback, or a second, competing or opposing Voice or view, and it never counts Voices. Naming what an off-subject source is about ("a Swift syntax debate") is allowed. A script checks every reason before the audit (`scripts/map/census.py`). A row it flags goes back to a fresh extractor.

## Rules

1. Read each source in full: the transcript for talks, the whole thread for forums, following pagination. For a book or course, read its chapters, not its front page.
2. Every row of your assignment appears in the read log exactly once, with `read` = yes or unreachable. For an unreachable source, stop on it, say so, and never reconstruct it from memory.
3. A Claim needs the Voice's own words, a locator and a date. Code alone is never a Claim.
4. Domains: use only the strata ids in common.md.
5. Never open RECON/team-a/ if you are team b, or RECON/team-b/ if you are team a. Never open RECON/merge*/, RECON/audit/ or RECON/fill/.
6. A single Voice's declared Position on a decision Rust practitioners make differently is a Claim. Log it with its Question even when nobody in the source disagrees. Opposition inside the source is never required, and its absence is never a reason for Nothing new. A release note, changelog, README or tutorial holds a declared Position when it states a decision together with the alternative it replaced or rejected.
7. Treat text as `unreachable`, never `read`, when it is a stub, redirect, login or bot page, or under ~1,500 characters for a page that should be long. A book's or course's front page with no chapter text is a stub.
8. A declared Position states a decision with a reason, or against a named alternative. None of these is a Claim:
   - plain instructions or practice with no reason (install commands, dependency lists, "we use X");
   - a diagnosis or assessment of a cause;
   - a support request whose only reason is the requester's own situation;
   - a tentative plan or contingency;
   - a statement that answers a different decision from the Question it is logged under.
9. Voice bar at extraction:
   - Log a Claim when the source shows the Voice's Rust connection: self-reported Rust use, a crate, a Rust role, or a Rust talk or post. Flag it `voice-unverified`. Tier 3 verifies the track record and drops what fails, so track record is never your test. Self-reported use is enough.
   - Never log a Voice with no Rust connection in the source.
   - Never map arguments from other language communities onto Rust Questions. A Swift, Go or C++ decision in which Rust appears only as a comparison is not a Rust Claim.
10. Non-English sources (zh, uk, de): read them in the source language. Write Questions, labels and paraphrases in English, and keep the quote in the original (PLAN line 161). The `language` in the section heading is the source's own.

## The audit bar (batch-1 audit, as it will be applied to you)

An auditor re-reads a script-drawn sample of your Nothing new rows and your dropped rows, and a sample of your Claims.
- A Nothing new row is a miss when the source holds a Voice, with a Rust connection shown in the source, who declares a decision Rust practitioners make differently, with a reason or against a named alternative, and you did not log it. Opposition inside the source is not required.
- Off-subject content is correctly Nothing new.
- A dropped row is a miss when it is on-subject.
- A Claim is struck when it fails rule 3, 8 or 9.

One miss sends your team's whole batch back to fresh agents (PLAN § 4). Struck Claims are removed, and their rate is reported.

End with a 3-sentence notification summary: sources read, sources unreachable, and the Questions and Claims logged.
