# rust-trainer session allowlist

For the session builder (P6, `scripts/train/session.py`). Applied to the trainer subagent's session at launch. Default deny: anything not allowed below is denied. Deny beats allow. Trainer rule 7 (`trainer/agent/trainer.md`) points here.

Paths: `UNIT` = the unit's item directory under `trainer/items/<unit>/` (recon, v0) or its committed home; `CRATE` = `/Users/ryzhakar/pp/gym/training/rust/<unit>/`; `RECORD` = `/Users/ryzhakar/pp/gym/training/rust/record/`.

## Allow

| tool | pattern | why (trainer rule) |
|---|---|---|
| Read | `UNIT/attempt.md`, `UNIT/example.md`, `UNIT/hints.yaml`, `UNIT/reuse-1/**`, `UNIT/reuse-2/**`, `UNIT/unshown/**` | 8 |
| Read | `CRATE/**` | 8, 28 |
| Read | `RECORD/**` | 8 (record tail) |
| Glob | `CRATE/**` | 28 (find the spot the learner points at) |
| Bash | `uv run python /Users/ryzhakar/pp/gym/scripts/train/log.py turn *` | 36 |
| Bash | `cargo check` and `cargo test`, with any flags, cwd `CRATE` | 7, 25 |

## Deny

| tool | pattern | why |
|---|---|---|
| Read, Glob | `**/key/**` | 9; T8 |
| Read, Glob | `**/probe-*/**` | 9, 19 |
| Read, Glob | `UNIT/**` outside the allow rows above | 8 |
| Bash | `cargo run*`, `cargo build*`, `cargo add*`, `cargo install*`, any `cargo` other than check and test | 7 (no write into the crate) |
| Bash | any command containing `>`, `>>`, `\|`, `;`, `&&`, `tee`, `cp`, `mv`, `rm`, `cat`, `sed`, `echo`, `python` outside the log.py line | 7 |
| Bash | `git *` | common.md rule 1 |
| Write, Edit, NotebookEdit, Grep, WebFetch, WebSearch, Agent, Task* | all | tools not granted: 39; not in frontmatter |

## Claude Code permission form, as a starting point

```
allow:
  - Read(UNIT/attempt.md)
  - Read(UNIT/example.md)
  - Read(UNIT/hints.yaml)
  - Read(UNIT/reuse-1/**)
  - Read(UNIT/reuse-2/**)
  - Read(UNIT/unshown/**)
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
  - Bash(git *)
```

Open points, with defaults:
- Prefix patterns `cargo check*` and `cargo test*` still admit shell chaining (`cargo test; cat key/x`). Default: session.py adds a PreToolUse hook that rejects any Bash command containing `;`, `&&`, `||`, `|`, `>`, or a backtick. `default, unmeasured`.
- Permission syntax is written from memory of Claude Code settings rules; P6 verifies against the installed version. `default, unmeasured`.
- `cwd` cannot be pinned by a permission rule; the hook also rejects `cargo` commands whose cwd is not `CRATE`. `default, unmeasured`.
