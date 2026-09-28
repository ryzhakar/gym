# rust-trainer session allowlist

For the session builder (P6, `scripts/train/session.py`). Applied to the trainer subagent's session at launch. Default deny: anything not allowed below is denied. Deny beats allow. Trainer rule 7 (`trainer/agent/trainer.md`) points here.

`items/` stays read-only in use (owner ruling, 2026-09-28): the learner never edits a committed stub directly. `session.py` copies each stub crate it needs to a session-scoped working copy before the trainer (or a probe) ever touches it; the trainer's own grants point at its copy, never at `items/`'s own reuse-1/reuse-2/unshown/attempt crates.

Paths: `UNIT` = the unit's item directory, `/Users/ryzhakar/pp/gym/training/rust/items/<unit>/` — prose only from here on: `attempt.md`, `example.md`, `hints.yaml`, none of them ever edited. `CRATE` = `/Users/ryzhakar/pp/gym/training/rust/work/<session-id>/<unit>/practice/`, the staged copies of `attempt/`, `reuse-1/`, `reuse-2/`, `unshown/` (whichever exist), one sibling crate per subdirectory — a probe's own staged copies live beside it under `.../work/<session-id>/<unit>/probe/`, a different `kind` segment the trainer's grants never reach, on purpose (rule 19: the trainer never sees a probe). `RECORD` = `/Users/ryzhakar/pp/gym/training/rust/record/`.

## Allow

| tool | pattern | why (trainer rule) |
|---|---|---|
| Read | `UNIT/attempt.md`, `UNIT/example.md`, `UNIT/hints.yaml` | 8 |
| Read | `CRATE/**` | 8, 28 |
| Read | `RECORD/**` | 8 (record tail) |
| Glob | `CRATE/**` | 28 (find the spot the learner points at) |
| Bash | `uv run python /Users/ryzhakar/pp/gym/scripts/train/log.py turn *` | 36 |
| Bash | `cargo check` and `cargo test`, with any flags, cwd `CRATE` or a subdirectory of it (one of its sibling crates) | 7, 25 |

## Deny

| tool | pattern | why |
|---|---|---|
| Read, Glob | `**/key/**` | 9; T8 |
| Read, Glob | `**/probe-*/**` | 9, 19 |
| Read, Glob | `UNIT/**` outside the allow rows above (in particular: `UNIT/reuse-1/**`, `UNIT/reuse-2/**`, `UNIT/unshown/**`, `UNIT/attempt/**` — the staged copy is read instead) | 8; owner ruling 2026-09-28 |
| Bash | `cargo run*`, `cargo build*`, `cargo add*`, `cargo install*`, any `cargo` other than check and test | 7 (no write into the crate) |
| Bash | any command containing `>`, `>>`, `\|`, `;`, `&&`, `tee`, `cp`, `mv`, `rm`, `cat`, `sed`, `echo`, `python` outside the log.py line | 7 |
| Bash | `git *` | common.md rule 1 |
| Write, Edit, NotebookEdit, Grep, WebFetch, WebSearch, Agent, Task* | all | tools not granted: 39; not in frontmatter |

## Claude Code permission form, as built (P6, `scripts/train/session.py::permission_settings`)

```
allow:
  - Read(UNIT/attempt.md)
  - Read(UNIT/example.md)
  - Read(UNIT/hints.yaml)
  - Read(CRATE/**)
  - Read(RECORD/**)
  - Glob(CRATE/**)
  - Bash(uv run python /Users/ryzhakar/pp/gym/scripts/train/log.py turn *)
  - Bash(cargo check*)
  - Bash(cargo test*)
deny:
  - Read(**/key/**)
  - Glob(**/key/**)
  - Read(**/probe-*/**)
  - Glob(**/probe-*/**)
  - Bash(cargo run*)
  - Bash(cargo build*)
  - Bash(cargo add*)
  - Bash(cargo install*)
  - Bash(git *)
```

Built and adversarially tested (`scripts/train/hooks/trainer_guard.py`, `scripts/train/tests/test_trainer_guard.py`, `scripts/train/tests/test_probe.py`, `scripts/train/tests/test_session.py` — P56-selfcheck.md carries the full record):
- The prefix patterns `cargo check*`/`cargo test*` still admit shell chaining after them by permission text alone. Closed by `trainer_guard.py`, a `PreToolUse` hook matching `Bash|Read|Glob`: denies any Bash command containing `;`, `&&`, `\|\|`, `\|`, `>`, `<`, a backtick, `$(`, or a literal newline, regardless of what precedes it; denies a Bash command naming a `key`/`probe-*` path segment even with none of those present; denies a `Read`/`Glob` call on such a path directly, a second check on top of the permission list above.
- `cwd` cannot be pinned by a permission rule. `trainer_guard.py --crate CRATE` denies a `cargo` call whose cwd is not `CRATE` itself or one of its sibling crates (`CRATE/attempt`, `CRATE/reuse-1`, ...).
- Permission syntax (`--settings`, `permissions.allow`/`.deny`, `hooks.PreToolUse`) verified against the installed `claude --help` (`--settings <file-or-json>` takes a path; `session.py` writes one fresh per launch, gitignored under `training/rust/work/`).
