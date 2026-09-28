# Trainer build — shared brief (gym, 2026-09-28)

Your dispatch prompt's first line binds you; read each element there in full before working.

Roots:
- PLAN = /Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-28/trainer/fable-plan.md, the trainer program plan. Your piece's row is in § 4, its stage in § 3, the formats in § 5, the defaults in § 6.
- TRAINER = /Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-28/trainer/, for drafts and check logs.
- EVIDENCE = /Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27/research/teaching/synthesis/evidence-map-v3.md, the teaching evidence map. Cite findings by claim id and grade.
- MAP = /Users/ryzhakar/pp/gym/maps/rust/, the Rust opinion map v0.1: provisional, thin (see its README).
- Committed homes (decided 2026-09-28): the learner record and workspace go in /Users/ryzhakar/pp/gym/training/rust/; scripts go in /Users/ryzhakar/pp/gym/scripts/train/.

Decided defaults, from PLAN § 6: O1–O13 as written, except O1. For O1 the learner record is a product committed under training/rust/, and the memento schema is not amended. The trainer's manifesto stack is the owner's to set and stays unset in v0. The trainer runs on opus.

Rules:
1. Write only your output paths; `mkdir -p` where needed. Run no git command.
2. Python only, managed and run with `uv`. Rust through `cargo`.
3. Every rule you write that rests on the evidence cites its claim id. Anything the evidence does not settle is marked `default, unmeasured`.
4. Cite by path and line. Never paste another file's content into yours.
5. No owner questions. Write open points with a default.
6. Final message: a 3-sentence summary suitable for a notification, naming your outputs.

## Scratch

Keep temporary files in your own directory, /private/tmp/gym-scratch/<your agent name>/; never write scratch to a shared path such as /tmp directly (decided 2026-09-28, after concurrent agents overwrote each other).
