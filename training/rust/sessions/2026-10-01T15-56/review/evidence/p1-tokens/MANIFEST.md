# Evidence, item p1-tokens (unit u02-enums-match, probe-a), session 2026-10-01T15-56

Copied from the gitignored workspace /Users/ryzhakar/pp/gym/training/rust/work/2026-10-01T15-56/u02-enums-match/p1-tokens/ on 2026-10-01 (about 21:26 local) with `cp -p`, checked with `cmp`. Times are local (EEST, UTC+3), read with `stat` before copying; the copy keeps them.

| copy | workspace origin | bytes | modified | sha256 |
|---|---|---|---|---|
| prediction.txt | p1-tokens/prediction.txt (the item's Edit line) | 78 | 2026-10-01T17:59:21 | f2e0abac094cdde386f897b79249a805acce5bb4231714cd99579c7b159de05d |

Notes
- No other learner-written or note file exists for this item. `Cargo.toml`, `spec.md`, `src/main.rs`, `tests/predict.rs` are byte-identical to commit 5c540de (`git show 5c540de:training/rust/items/u02-enums-match/probe-a/p1-tokens/<path> | cmp`), so they are not copied. `Cargo.lock` and `target/` are cargo output, not copied.
- `src/main.rs` modification time is 2026-09-28T14:11:01, which is why the tool read minutes=0.00 for this item (the tool reads `src/` only).
- Workspace `target/` timing: first cargo run 17:55:56 (before the learner's "go" at 17:56:08), second 17:56:36 (fingerprint files only), the rest 18:13:26 (grading). The sources do not name who or what ran cargo at 17:55:56 and 17:56:36.

## Extracts from the trainer transcript (outside the repo, not durable)

| copy | bytes | file written | sha256 | content |
|---|---|---|---|---|
| transcript/transcript-excerpts.md | 39995 | 2026-10-01T21:30:07 | 130327c388900e783af67808b9a14c9deddc5c57ef5253838869cc2406004271 | A: all 26 learner messages with JSONL line, UTC and local time. B: the trainer messages that carry the walk's five prediction questions (JSONL lines 92, 100, 112, 120, 128, 136). C: the probe section, JSONL lines 273 to 357 (confidence, staging, go, done, grading, report), text, tool calls and tool results verbatim. Not workspace files, not learner-written; produced by script from the JSONL. The same file serves p2-tilt-status, p3-alert and blocks L-1 to L-4. |
