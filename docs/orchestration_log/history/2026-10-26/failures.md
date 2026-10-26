# 2026-10-26 — failures

## Commit over a masked record-check FAIL

What happened: span gm committed 8e04ed7 while `gym records check` reported 1 FAIL, docs/conventions.md 22 tokens over its 3000 budget after the commons carve-out edit.

Mechanism: the check ran as `uv run gym records check | tail -1 && git commit`; the pipe's status is tail's, so the FAIL never stopped the chain.

Correction: the rule was trimmed under budget and recommitted as 9fa0295; the check now writes to a file and the commit runs only on a grep for `0 FAIL`.
