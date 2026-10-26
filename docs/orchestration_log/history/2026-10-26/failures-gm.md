# 2026-10-26 — failures

## Commit over a masked record-check FAIL

What happened: span gm committed 8e04ed7 while `gym records check` reported 1 FAIL, docs/conventions.md 22 tokens over its 3000 budget after the commons carve-out edit.

Mechanism: the check ran as `uv run gym records check | tail -1 && git commit`; the pipe's status is tail's, so the FAIL never stopped the chain.

Correction: the rule was trimmed under budget and recommitted as 9fa0295; the check now writes to a file and the commit runs only on a grep for `0 FAIL`.

## Events written to the root checkout from a worktree session

What happened: Nine events lines of span gm landed in the root checkout's events-gm.md while the span's branch lives in gym.worktrees/manager, blocking the fast-forward of main.

Mechanism: The Bash tool resets cwd to the start directory after each call, and memento events add resolves the events file from cwd, so calls without cd wrote to the root.

Correction: The nine lines were appended to the worktree copy and the root file restored before the fast-forward; every memento call now starts with cd into the worktree.
