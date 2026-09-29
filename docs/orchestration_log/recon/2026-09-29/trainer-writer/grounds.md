# gym-trainer.md — grounds per instruction

Companion to `.claude/agents/gym-trainer.md`. The body carries no claim ids (skill-creation: never argue); this file carries them. Claim status and grades are the last row per claim_id in `docs/orchestration_log/recon/2026-09-27/research/teaching/ledger/claims-status.csv`; quotes in `verify/claims/<id>.md`. Owner rulings are `docs/orchestration_log/history/2026-09-26/events.md` line numbers. "Platform" is `orchestration_log/reference/agents-reference.md` in claude-skills; "Learning" is the built-in Learning output style in cli.js and the learning-output-style plugin.

## Frontmatter

| field | ground |
|---|---|
| `name` | platform §1: lowercase and hyphens; `claude --agent gym-trainer` (task) |
| `description` | platform §1, §3; skill-creation open-the-skill (one sentence of what, then conditions); owner ruling 2026-09-29: the manager summons the trainer, no `claude --agent` launch |
| `tools: Read, Glob, Grep, Bash` | platform §4 SV-4 (omitted `tools` inherits everything, MCP included); no Write or Edit because the trainer never produces the practice output (N7-r1-01, N1-r1-01/N7-r3-03, N7-r1-08, N7-r1-09; `resolve/ai-access-resolution.md` moderator 1); Bash for build/test commands (ruling 105 "watching the work", 122) and for `scripts/train/log.py`; no `Agent` so the main thread spawns nothing (platform §4) |
| no `model` | platform §5 SV-33: `inherit` follows the session's `--model`; `sessions.trainer_model` in `record_schema.py` logs whichever ran |
| no `memory` | platform §1 SV-6: `memory` re-enables Write and Edit unconditionally; the learner record is the memory |
| no `hooks`, `permissionMode`, `initialPrompt` | platform §1, §6: the manager's summons sets the launch surface; initialPrompt would add a turn the open tag already covers |

## Body

| tag | sentence (first words) | ground |
|---|---|---|
| open-the-session | Read the session inputs the manager hands over… | owner ruling 2026-09-29 (the manager, gym's main session, is the learner's entrypoint and summons the trainer); task: subject, commands, paths are runtime inputs; the input list mirrors `record_schema.FILES` and `log.py turn --session` |
| | Ask the manager for a missing input… | first-principles: no invented inputs |
| | Mind the training; never administration… | owner ruling 2026-09-29: trainer minds training only; session, item, confidence, probe and queue rows, scheduling and probes are the manager's; probes run with the trainer absent |
| | Read the record tail for hint history and baselines, set difficulty and hint timing from its probe rows… | N3-r4-08/09 (hint history predicts help need); N1-r7-08, N1-r7-04 (self-report is not learning); rulings 114, 120 (early measurement in training; adapt to specific students); `items.kind baseline` |
| | Log the unit's opening as `start` | `record_schema.py` turns.kind `start`; `log.py` docstring |
| log-every-turn | Log each turn… `log.py turn …` | `log.py` `turn` alias, flags, `--request`; N7-r3-02 (answer-vs-hint count moves with the unaided test; map: "log every assistant turn as answer-request vs hint") |
| | Take the timestamp and minute from the printed row | `log.py`: refuses hand-typed timestamp, computes `minute` |
| | Set `--kind` to … | `record_schema.FILES["turns"]["kind"]` enum |
| | `--note` on `ladder-gap` only | `record_schema.note_required_iff_ladder_gap`; `log.py` docstring |
| | Log a handed-over solution as `answer` | `record_schema.py`: "answer" is the breach case; cargo-cult: publish both kinds of result |
| speak-to-the-learner | blunt, terse and clear… never praise… | ruling 121; Learning "Avoid praise or repetition" (survives, loses its encouraging tone per settled conflict); stop-yapping |
| | Name a file and a spot in words; never by line number | Learning: "mention file and TODO(human) but do not include line numbers"; hand-back survives without a workspace edit |
| | Speak of the work… never counsel beyond it | CLAUDE.md prime directive: elite personal trainer, "Not a mentor" |
| present-the-item | Present a concept item… then stop; never explain before the attempt | N3-r1-02 / N2-r1-10 (attempt before instruction, g 0.36); N7-r2-01 (the LLM default is to reveal early; `resolve/we-vs-pf-resolution.md`); Learning: "Don't take any action or output anything after the request. Wait." |
| | Present a strategy item with instruction first | Sinha & Kapur Table 5: domain-general skills −0.17, 8 comparisons, instruction first (resolution moderator 3) |
| | consecutive items differ in type | N2-r1-02, N2-r7-01 (interleaving, K-12 field RCT); N2-r5-01/05 (motor, lab-bound) |
| | Log a `present` turn | `record_schema.py` kind `present` |
| | Write nothing after presenting | Learning stop-after-hand-back |
| watch-the-work | read what changed… run the build and test commands | rulings 105, 122 (continuous watching); N4-r2-10 (performance-based cues beat explanation-based); N1-r6-07 (a knowledge check misses what a performance measure catches); map: continuous watching has no learning-outcome study, owner ruling stands |
| | When the learner points at a spot | ruling 122 (learner calls attention to a spot) |
| | Bring a skipped item back | N3-r1-07 (S2; exercises on bypassed material) |
| | announced break → next action in one line | N6-r5-03/04 (warning before an interruption; first action after resuming slowest; lab, seconds scale); ruling 118 "life interruptions" via the map's calibration section; thin |
| respond-to-a-request | hints, questions and instruction; never the solution… or an edit | N7-r1-01, N1-r1-01, N7-r1-08, N7-r1-09, N3-r1-11 (four RCTs; harm from copying, correct solutions included); N7-r1-02 (hints remove the harm) |
| | say the copied solution lowers the unaided test and offer a hint | N7-r3-02 (feedback naming the cost of offloading, OR 1.51 [0.98, 2.33], immediate) |
| | `hint-1` after an attempt | attempt-first member; N7-r1-02 |
| | supplied hint before a composed one | N3-r3-04, N3-r5-04/05 (human-authored hints and explanations beat LLM-generated, two RCTs); transfer: the item directory can carry authored hints |
| | Escalate after a failed attempt at the level before; fall silent once the learner moves | N7-r3-01 (support that escalates on failure and fades on take-up; O=1 assisted); `record_schema.py` hint-1/2/3 |
| | `question` that has the learner predict or choose the next move; never recite understanding | N7-r3-04c (Socratic guidance, R=3 O=2, transfer of LLM use); N7-r4-07/08 (self-explanation prompts on LLM practice: null); N4-r7-02 SURVEYED (predict-the-output probes) |
| | hint unasked when the record predicts a request | N3-r4-08/09 (proactive hints from hint history: ~20% less time, d .45; non-LLM) |
| | `ladder-gap` → instruction | `record_schema.py` kind `ladder-gap`; PS-I: instruction follows the attempt |
| instruct-after-the-attempt | built on that attempt: name the principle, contrast with the canonical approach in words | Sinha & Kapur Table 3: instruction building on student solutions 0.56 vs 0.20 (resolution moderator 1); "in words" keeps the harm boundary (assistant never produces the practice output) |
| | novice or blank attempt → subgoal-labeled worked example on a different problem | N2-r1-05/06 (R=3 O=2, 36% more tasks correct, transfer f .58); Hartmann 2021 in the resolution (thin generation → modeled attempt beats own); Kalyuga 2003 expertise reversal (examples for novices); `items.kind baseline` |
| | close with a fresh isomorphic item; never the solution to the item at hand | N1-r1-01 design (probe items paired to practice items); harm evidence |
| give-feedback | on the learner's own code… after an attempt or a test run | Learning/Explanatory: insight "specific to the code you just wrote, rather than general programming concepts"; timing has no verified value (N3-r1-04, N3-r7-05 UNVERIFIABLE) so one timing is chosen and held, per `synthesis/first-protocol.md` |
| | Leave the artifact as written | N7-r7-03/04 (LLM writing aid: product up, learner flat) |
| | Read the unit's delayed probe as its outcome; never practice score, confidence or felt progress | N1-r1-01 (assistant removed, held-out items); N1-r1-09 (delay is part of the instrument); N1-r6-05/06 (immediate and 2-week rankings reverse); N1-r4-10, N7-r1-09, N1-r7-08, N1-r7-04, N1-r6-09; ruling 104 (learned = unaided and lasting); owner ruling 2026-09-29 (the probe is the manager's, trainer absent) |
| | Point at probe results; never at feedback on past self-judgments | N1-r4-01/02, N4-r6-05, N1-r3-11 (calibration feedback null, worse on correct cases); N4-r2-10 |

## Choices the evidence did not make

- Feedback timing: after the attempt or test run. No verified timing value exists; the choice follows attempt-first for coherence.
- `hint-1` gated on an attempt: Liu's hint users ≈ control is cross-sectional; the gate is the attempt-first member applied to the first hint.
- "In words" for the canonical approach: PS-I studies show canonical solutions to the same problem after attempts; the body forbids pasting runnable code for the learner's item because the LLM default (N7-r2-01) is early reveal and the harm mechanism is copying.
- Break note: N6-r5-03/04 is a lab result at the scale of seconds; implementation intentions for resuming (N6-r4-01…-04) are SURVEYED S2.
- Removed on the owner's 2026-09-29 ruling, now the manager's: probe running and scoring (N1-r3-01 threshold plus continuous; `items` rows), confidence logging (`confidence` rows), spacing and the `queue` rows (N2-r1-01, N2-r7-03/04), the mastery gate at the immediate probe (N1-r6-06).
