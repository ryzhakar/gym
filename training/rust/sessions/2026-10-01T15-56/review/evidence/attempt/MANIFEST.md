# Evidence manifest, item `attempt` (blocks I-1, A-1 to A-7, AR-1 to AR-3)

Copied by the sensor checker from /Users/ryzhakar/pp/gym/training/rust/work/2026-10-01T15-56/u02-enums-match/ (gitignored). Copies made with `cp -p`, checked with `cmp`. Times are local (EEST, UTC+3). Original sizes and modification times, read with `stat`.

## Learner and workspace files

| copy | original | size | original mtime | note |
|---|---|---|---|---|
| src/enum_form.rs | attempt/src/enum_form.rs | 966 bytes | 2026-10-01T17:52:37 | Final state. The 16:14 state, overwritten since, is in transcript/read-of-attempt-at-16-14-25.txt. |
| src/flat_form.rs | attempt/src/flat_form.rs | 1027 bytes | 2026-10-01T17:51:53 | Final state. Untouched stub at 16:14, same transcript file. |
| example-chat.md | example-chat.md | 2583 bytes | 2026-10-01T17:08:19 | Written by the trainer, not the learner. Created 16:32:44, appended 17:08. Lines 1-23 are the attempt walk; lines 25-30 belong to reuse-1. |

No prediction or note file written by the learner exists for this item. `attempt/attempt.md`, `attempt/Cargo.toml`, `attempt/src/lib.rs`, `attempt/tests/visible.rs` and `example.md` are byte-identical to commit 5c540de (checked with `git show 5c540de:training/rust/items/u02-enums-match/<path> | diff`), so they are not copied.

## Extracts from the trainer transcript (outside the repo, not durable)

| copy | size | mtime of the copy | content |
|---|---|---|---|
| transcript/read-of-attempt-at-16-14-25.txt | 2792 bytes | 2026-10-01T21:26:02 | Tool result of the trainer's read at 16:14:25: file mtimes, enum_form.rs and flat_form.rs as they stood, `cargo test` output. JSONL line 75. |
| transcript/read-of-attempt-at-17-52-50.txt | 3209 bytes | 2026-10-01T21:26:02 | Same read at 17:52:50: final files and the 14-test green output. JSONL line 266. |
| transcript/transcript-excerpts.md | 64906 bytes | 2026-10-01T21:30:27 | Learner and trainer messages and tool calls cited in 01-sensor.md, verbatim, with JSONL line numbers, UTC and local times. |

The two read files are the tool result text only, split out by script. Not workspace files, not learner-written.
