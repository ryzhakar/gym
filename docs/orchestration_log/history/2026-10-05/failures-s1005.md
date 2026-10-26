## Tooling edited in the live tree during a training session

What happened: the per-problem-caps agent edited src/gym/train/ in the main working tree while session 2026-10-05T21-58 ran from it; the gym CLI there was broken from 22:00 to 22:06, and the trainer logged through a worktree at HEAD.

Mechanism: the session was started while a tooling change was in flight, and the implementer was not isolated in a worktree.

Correction: a tooling change made while a session runs goes through a worktree-isolated agent and lands by commit only.
