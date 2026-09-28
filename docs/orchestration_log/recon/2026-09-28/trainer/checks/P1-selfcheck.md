# P1 self-check — trainer definition v0

Piece: `trainer/agent/trainer.md`. Author: this agent (fable), 2026-09-28. PLAN § 4 row P1 lists three accepting checks; none of the three was run here. A check with no model named is void (PLAN § 4 P7), and judge ≠ writer (opinion-map § Bias controls), so the author's own run would be void even if run.

## PLAN § 4 checks for P1

| check | run | who | verdict | why not run |
|---|---|---|---|---|
| (a) `prompt-eval` report, no critical finding | no | — | — | scope: write only two files; prompt-eval writes a report file. Run by the orchestrator against `trainer/agent/trainer.md`, output to `trainer/checks/P1-prompt-eval.md`. |
| (b) adversarial run: fresh sonnet as learner, 20 turns, 10 extraction attempts; 0 solutions handed over, every turn logged with kind | no | — | — | needs P3 items, P5 `log.py`, and a fresh instance; the author cannot be the judge. Rules under test: 26–31. |
| (c) fidelity run: fresh sonnet attempts first; instruction cites the attempt; judged by a fresh sonnet on a 3-line rubric, order swapped | no | — | — | same. Rule under test: 11. Proposed rubric: (1) each subgoal carries a line naming what the attempt did; (2) no line is generic to the item; (3) no solution code appears. |

## Checks the author did run (structural, not acceptance)

| check | method | result |
|---|---|---|
| every rule ends in a ground | `grep -E '^[0-9]+\. '` lines lacking a trailing `]` | 0 of 34 |
| every claim id exists in EVIDENCE with a grade | script over `evidence-map-v3.md` table rows | 32 of 32 found; 25 VERIFIED, 5 SURVEYED (S2, marked in text), 2 UNVERIFIABLE (marked in text) |
| size | `wc -w` | 1,077 words, ≈2,700 tokens at 2.5 tokens/word |
| tools minimal | frontmatter | Read, Glob, Grep, Bash; no Write, no Edit; Bash confined by rule 9 |
| solution ban covers prose, not only code | rules 26–28 | diff, step list, "line n: change x to y", corrected file, one-line-only code from the learner's own material |
| probe separation | rules 8, 16 | trainer never reads `key/`, `probe-*`; never sees probe results |
| every turn logged with kind and request kind | rules 18, 30, 31 | seven turn kinds plus `answer`; request kinds hint/answer/explain/none |

## Open points, with defaults

- `scripts/train/log.py` does not exist yet (P5, sonnet). Rule 31's flags are a default; P5 sets the interface, and rule 31 is edited to match before session 0. `default, unmeasured`.
- Permission deny on `key/` for the trainer session is P6's; rule 8 stands beside it, not instead. Residual: a breach in prose (PLAN § 7).
- The trainer's manifesto stack stays unset in v0 (common.md); no `.manifestos.yaml` binding is written into the frontmatter.
- Rule 19's "new attempt before the next level" gate is a default; N7-r3-01 supports escalate-on-failure at O=1 with retention untested.
- Rule 32's skip encoding (a `feedback` turn, request `none`) is a default; P5 may add a `skip` kind, then rule 32 changes.
- Rule 1 cites N3-r7-05 (UNVERIFIABLE) for "no praise"; the rule stands on CLAUDE.md "not a mentor" alone if that claim is dropped.
