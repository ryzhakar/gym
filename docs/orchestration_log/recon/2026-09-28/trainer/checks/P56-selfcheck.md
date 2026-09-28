# P5/P6 self-check — learner record and session logistics

Run: `uv run pytest scripts/train/tests -v` (47 tests) and `uv run python scripts/train/check_record.py`
against the committed `training/rust/record/*.csv` (header-only at this point).

## `uv run pytest scripts/train/tests -v`

```
============================= test session starts ==============================
platform darwin -- Python 3.11.11, pytest-9.1.1, pluggy-1.6.0 -- /Users/ryzhakar/pp/gym/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/ryzhakar/pp/gym
configfile: pyproject.toml
collecting ... collected 47 items

scripts/train/tests/test_bash_guard.py::test_chaining_token_is_denied[;] PASSED
scripts/train/tests/test_bash_guard.py::test_chaining_token_is_denied[&&] PASSED
scripts/train/tests/test_bash_guard.py::test_chaining_token_is_denied[||] PASSED
scripts/train/tests/test_bash_guard.py::test_chaining_token_is_denied[|] PASSED
scripts/train/tests/test_bash_guard.py::test_chaining_token_is_denied[>] PASSED
scripts/train/tests/test_bash_guard.py::test_chaining_token_is_denied[`] PASSED
scripts/train/tests/test_bash_guard.py::test_cargo_with_the_right_cwd_is_allowed PASSED
scripts/train/tests/test_bash_guard.py::test_cargo_with_the_wrong_cwd_is_denied PASSED
scripts/train/tests/test_bash_guard.py::test_the_logger_call_is_allowed PASSED
scripts/train/tests/test_bash_guard.py::test_main_reads_stdin_and_prints_a_decision PASSED
scripts/train/tests/test_check_record.py::test_clean_file_has_no_findings PASSED
scripts/train/tests/test_check_record.py::test_bad_enum_is_a_fail PASSED
scripts/train/tests/test_check_record.py::test_bad_date_is_a_fail PASSED
scripts/train/tests/test_check_record.py::test_timestamps_going_backward_is_a_fail PASSED
scripts/train/tests/test_check_record.py::test_wrong_header_is_a_fail PASSED
scripts/train/tests/test_check_record.py::test_missing_file_is_a_fail PASSED
scripts/train/tests/test_check_record.py::test_main_exits_1_on_any_fail PASSED
scripts/train/tests/test_check_record.py::test_main_exits_0_when_all_clean PASSED
scripts/train/tests/test_log.py::test_valid_row_is_stamped_and_appended PASSED
scripts/train/tests/test_log.py::test_hand_typed_timestamp_is_refused PASSED
scripts/train/tests/test_log.py::test_malformed_row_is_refused[<lambda>-missing] PASSED
scripts/train/tests/test_log.py::test_malformed_row_is_refused[<lambda>-unknown] PASSED
scripts/train/tests/test_log.py::test_malformed_row_is_refused[<lambda>-not 'true' or 'false'] PASSED
scripts/train/tests/test_log.py::test_malformed_row_is_refused[<lambda>-below 0] PASSED
scripts/train/tests/test_log.py::test_malformed_row_is_refused[<lambda>-not an integer] PASSED
scripts/train/tests/test_log.py::test_malformed_row_is_refused[<lambda>-empty] PASSED
scripts/train/tests/test_log.py::test_append_refuses_a_timestamp_before_the_last_row PASSED
scripts/train/tests/test_log.py::test_append_refuses_a_mismatched_header PASSED
scripts/train/tests/test_log.py::test_append_refuses_a_missing_file PASSED
scripts/train/tests/test_log.py::test_parse_turn_flags_matches_the_trainer_definitions_literal_invocation PASSED
scripts/train/tests/test_log.py::test_parse_turn_flags_maps_request_none_to_blank PASSED
scripts/train/tests/test_log.py::test_turn_fields_computes_minute_from_the_session_id_never_a_hand_typed_one PASSED
scripts/train/tests/test_log.py::test_turn_fields_refuses_a_malformed_session_id PASSED
scripts/train/tests/test_log.py::test_turn_alias_round_trips_through_build_and_append PASSED
scripts/train/tests/test_log.py::test_main_turn_alias_appends_to_turns_csv PASSED
scripts/train/tests/test_probe.py::test_assert_no_key_refuses_any_key_path PASSED
scripts/train/tests/test_probe.py::test_item_text_excludes_key PASSED
scripts/train/tests/test_probe.py::test_probe_dir_refuses_a_key_target PASSED
scripts/train/tests/test_probe.py::test_run_probe_grades_with_cargo_test_and_logs_a_row PASSED
scripts/train/tests/test_probe.py::test_run_probe_warns_over_cap PASSED
scripts/train/tests/test_session.py::test_close_writes_session_and_queue_rows PASSED
scripts/train/tests/test_session.py::test_open_with_no_due_probe_hands_off_to_the_next_unit PASSED
scripts/train/tests/test_session.py::test_open_runs_a_due_delayed_probe_then_hands_off PASSED
scripts/train/tests/test_session.py::test_launch_command_carries_the_full_allowlist PASSED
scripts/train/tests/test_session.py::test_a_read_of_any_key_path_is_denied_by_the_pattern PASSED
scripts/train/tests/test_session.py::test_launch_command_scopes_the_hook_to_the_named_unit_only PASSED
scripts/train/tests/test_session.py::test_open_session_prints_a_launch_command_with_the_deny_rule PASSED

============================== 47 passed in 1.58s ==============================
```

## `uv run python scripts/train/check_record.py`

```
record: 0 FAIL
```

## Trainer launch allowlist (team lead, 2026-09-28) — read from allowlist.md, not reconstructed

`session.permission_settings(unit)` and `session.trainer_launch_command(unit)` are built directly
from `docs/orchestration_log/recon/2026-09-28/trainer/agent/allowlist.md`'s Allow/Deny tables and
"Claude Code permission form", with `UNIT`/`CRATE`/`RECORD` substituted per unit (absolute paths, as
the file gives them). The launch uses `--settings` (verified against `claude --help`: `--settings
<file-or-json>` takes a JSON string inline, not only a file path) carrying `permissions.allow`,
`permissions.deny`, and a `hooks.PreToolUse` entry for `scripts/train/bash_guard.py`, plus
`--permission-mode dontAsk` so anything outside the allowlist is refused outright. The agent
definition is installed at `.claude/agents/rust-trainer.md` (copied from `trainer/agent/trainer.md`
so `--agent rust-trainer` resolves it). Example (`unit-1`, settings JSON abbreviated):

```
claude --agent rust-trainer --permission-mode dontAsk --settings '{"permissions":{"allow":["Read(/Users/ryzhakar/pp/gym/training/rust/items/unit-1/attempt.md)",...,"Bash(uv run python /Users/ryzhakar/pp/gym/scripts/train/log.py turn *)","Bash(cargo check*)","Bash(cargo test*)"],"deny":["Read(**/key/**)","Glob(**/key/**)","Read(**/probe-*/**)","Glob(**/probe-*/**)","Bash(cargo run*)","Bash(cargo build*)","Bash(cargo add*)","Bash(cargo install*)","Bash(git *)"]},"hooks":{"PreToolUse":[{"matcher":"Bash","hooks":[{"type":"command","command":"uv run python /Users/ryzhakar/pp/gym/scripts/train/bash_guard.py --crate /Users/ryzhakar/pp/gym/training/rust/unit-1","timeout":5}]}]}}' '<session, unit, items, record tail>'
```

`scripts/train/bash_guard.py` is the `PreToolUse` hook `allowlist.md`'s "Open points" call for: it
denies any Bash command containing `;`, `&&`, `||`, `|`, `>`, or a backtick (chaining after an
allowed `cargo check*`/`cargo test*` prefix), and denies a `cargo` command whose cwd is not the
unit's own crate (a permission pattern can't pin cwd). Tested in `test_bash_guard.py` directly
(the `check()` function) and through a real subprocess call (`test_main_reads_stdin_and_prints_a_decision`).

Tests asked for explicitly:
- **the launch carries the deny rules** — `test_session.py::test_launch_command_carries_the_full_allowlist`
  parses the embedded `--settings` JSON and asserts every deny row from `allowlist.md` is present,
  every allow row is present verbatim, and no `Bash(*)` blanket sneaks in; plus the hook command
  names `bash_guard.py` with the right `--crate`.
- **a Read of any key/ path is denied** — `test_session.py::test_a_read_of_any_key_path_is_denied_by_the_pattern`
  translates the `Read(**/key/**)` pattern (and every emitted allow pattern) into a regex mirroring
  Claude Code's glob syntax (`**` any run, `*` no `/`) and checks it matches three representative
  `key/` paths under the real item root, while no allow pattern matches them. **Honest limitation**:
  this verifies the pattern text would deny those paths if Claude Code's own matcher works as
  documented; it is not a live end-to-end run of a nested `claude` session actually attempting the
  read (that would need a real spawned CLI session with its own auth/cost, which I did not run).

## `log.py`'s `turn` alias — a cross-piece gap found and closed

`trainer.md` rule 36 invokes `uv run python .../log.py turn --session <id> --n <n> --kind <k>
--item <item id> --request <hint|answer|explain|none>`; `log.py`'s existing CLI only understood
`log.py <sessions|items|turns|confidence|queue> field=value ...`. As written, the trainer could
never log a turn — `argv[1] == "turn"` didn't match any file name — so rule 37 ("an unlogged turn
is never sent") would halt every unit immediately. Since I own `log.py` (P5), I closed this myself
rather than only flagging it: `log.py turn ...` is now an alias for `turns`, parsed in the flag form
rule 36 uses, `--request none` mapping to the blank `request_kind` a trainer-initiated turn carries.
`minute` is computed by `log.py` itself — elapsed minutes since `--session`'s own timestamp — never
accepted as a flag, matching rule 11 ("the trainer has no clock"). Covered by six new tests in
`test_log.py` (`test_parse_turn_flags_*`, `test_turn_fields_*`, `test_turn_alias_round_trips_*`,
`test_main_turn_alias_appends_to_turns_csv`). Flagging this rather than silently patching: P1's
`trainer.md` and `allowlist.md` were not re-read against this change, so if either changes rule 36's
flag names later, `TURN_FLAG_COLUMNS` in `log.py` needs updating with them.

## Hook rebuilt to the P1 eval v0.1's exact remaining finding, adversarially tested (team lead, 2026-09-28)

The eval (`trainer/checks/P1-prompt-eval.md` § v0.1, "Remaining findings") named the exact residual
gap: `cargo check*`/`cargo test*` prefix patterns still admit shell chaining to `key/`, the fix is
"designed, not built or tested," and closing it requires "(a) the PreToolUse hook is built, (b) an
adversarial Bash-chaining attempt is run against it and fails." That eval predates my first hook
build in this file's earlier section (`bash_guard.py`, single-directory Bash-only matcher, inline
`--settings` JSON) — team lead's follow-up asked for a wider rebuild, which supersedes it:

- **Location**: `scripts/train/hooks/trainer_guard.py` (old `scripts/train/bash_guard.py` and its
  test deleted — `git status` now shows both as `D`, for the next commit to pick up).
- **Chain tokens widened**: `;`, `&&`, `\|\|`, `\|`, `>`, `<`, backtick, `$(` (added `<` and `$(`).
- **Denies a `key`/`probe-*` path segment named in a Bash command even with no chaining** — e.g.
  `cat training/rust/items/u01/key/x` alone, not just `cargo test; cat key/x` — belt-and-suspenders
  under the same tool the eval flagged.
- **Matcher widened to `Bash|Read|Glob`**: the hook now also denies a `Read`/`Glob` call whose
  argument names a `key`/`probe-*` path segment, a second check on top of `allowlist.md`'s own
  permission-list deny (which the eval called "solid" already) — checked against every string value
  in `tool_input`, not a guessed field name, since the exact Read/Glob argument key isn't pinned down
  here.
- **`--settings` now a generated file**, not inline JSON: `session.write_settings_file(unit)` writes
  `training/rust/<unit>/.trainer-settings.json` fresh on every `trainer_launch_command` call (never
  committed, same as the crate tree it sits beside).

New test file `test_trainer_guard.py` (13 tests) covers exactly what was asked: the chained command
is denied (all 8 tokens, parametrized) and a Read of a `key/` path is denied (`check()` directly and
through a real subprocess over stdin); the logger call and a plain `cargo test --manifest-path
training/rust/u01/Cargo.toml` are allowed (both the team lead's literal examples).

**Adversarial run against the real generated command** (the eval's condition (b), literally, not
just unit-tested): built `session.write_settings_file`'s actual hook command for a scratch unit,
then piped the eval's own named attack string through it as a real subprocess:

```
hook command: uv run python /Users/ryzhakar/pp/gym/scripts/train/hooks/trainer_guard.py --crate /Users/ryzhakar/pp/gym/training/rust/adv-unit
payload command: cargo test --manifest-path training/rust/adv-unit/Cargo.toml; cat training/rust/items/adv-unit/key/solution.rs
decision: {"hookSpecificOutput": {"permissionDecision": "deny", "permissionDecisionReason": "chaining token ';' is not allowed in a trainer session Bash call"}}
```

Denied. The scratch unit's crate directory was removed afterward; `training/rust/` holds only
`record/` and `items/` (P3's, not mine) again.

```
============================== 57 passed in 1.62s ==============================
```

`check_record.py` still `record: 0 FAIL`.

## Coverage against the original brief's four required cases

- malformed row refused: `test_log.py::test_malformed_row_is_refused` (6 mutations) plus `test_hand_typed_timestamp_is_refused`.
- timestamps stamped: `test_log.py::test_valid_row_is_stamped_and_appended` and `test_append_refuses_a_timestamp_before_the_last_row`.
- `key/` never read by probe.py: `test_probe.py::test_assert_no_key_refuses_any_key_path`,
  `test_item_text_excludes_key`, `test_probe_dir_refuses_a_key_target`.
- session open/close round trip on a synthetic unit with a stub item: `test_session.py` (all three
  round-trip tests), using `cargo new --lib` crates and a stub `probe-b/prompt.md` under a temp
  items root — no real trainer, curriculum, or item content involved.

No FAIL, no skip on this machine (`cargo` is on PATH); the `@pytest.mark.skipif(CARGO_MISSING, ...)`
guards are a defensive default for a machine without `cargo`, not exercised here.

## Follow-up: reported gaps in `$(`, `<`, a second line, and key-path arguments (team lead, 2026-09-28)

Checked each of the four against `scripts/train/hooks/trainer_guard.py` as committed (`29cefa9`)
before changing anything:

- `$(` — already in `CHAIN_TOKENS`; direct call and a live subprocess both denied the team lead's
  exact reported command (`cargo test --manifest-path training/rust/u01/Cargo.toml
  $(cat training/rust/items/u01/key/x)`), reason `chaining token '$(' is not allowed`.
- `<` — already in `CHAIN_TOKENS`; `test_chained_bash_command_is_denied[<]` already covered it and
  passed.
- any argument with a `key` path component — already checked by `command_denied_segment` regardless
  of chaining; `test_bash_naming_a_key_path_is_denied_even_without_chaining` already covered it.
- a second line (a literal newline in one Bash call) — **this one was genuinely missing.** `"\n"`
  was not in `CHAIN_TOKENS`; a two-line command whose second line named no `key`/`probe-*` segment
  (e.g. `cargo test --manifest-path ...\nrm -rf /tmp/whatever`) would have passed. Added `"\n"` to
  `CHAIN_TOKENS`; a bare newline is now denied on its own, not only incidentally when the second
  line happens to reference `key/`.

I'm reporting the first three as already-passing rather than silently re-implementing them, since my
direct testing (both `trainer_guard.check_bash()` called in-process and the real script over stdin
via subprocess) shows them denied against the exact command given. If a live run still lets one of
these three through, the discrepancy is worth a closer look — possibly an outer shell evaluating
`$(...)` before the payload ever reaches this script, which would be a caller-side issue, not this
hook's. Four new/updated tests added: the three tokens plus the exact reported command
(`test_the_exact_reported_command_substitution_gap_is_denied`), and the new bare-newline case
(`test_a_second_line_with_no_key_reference_is_still_denied`).

```
$ uv run pytest scripts/train/tests/test_trainer_guard.py -v
...
============================== 23 passed in 0.06s ==============================
```

Full suite: `uv run pytest scripts/train/tests` → 60 passed. `check_record.py` → `record: 0 FAIL`.
"Live checking comes later with the adversarial trainer run," per the team lead's note — nothing
further attempted here beyond the direct and subprocess checks above.

## Probe runner fixes, from P3-selfcheck.md "Found during the check" (team lead, 2026-09-28)

Three asked fixes, all in `scripts/train/probe.py`:

1. **One crate per problem, one row per item.** `probe-a/`/`probe-b/` hold several standalone
   problem crates (`p1-*`, `p2-*`, ...), not one. `list_problem_dirs` finds every subdirectory with
   its own `Cargo.toml`; `run_probe` presents all of them under one shared timer (each problem's own
   `spec.md` says so: "10 minutes for p1, p2 and p3 together" — one `wait()` call, not one per item),
   then grades and logs each separately. `probe_dir`/`crate_dir` as a single-crate argument is gone
   from `run_probe`'s and `main`'s signature; `session.py`'s call site updated to match (dropped the
   now-meaningless `crate_dir` argument to `run_probe`, kept `ensure_unit_crate` only for the
   trainer's own practice-unit crate, unrelated to probes).
2. **`cargo test --no-fail-fast`.** `run_cargo_test` now passes the flag; a new
   `test_run_cargo_test_uses_no_fail_fast` locks the exact argument in with a stubbed `subprocess.run`.
3. **Grading copies `key/`'s held-out tests in, then removes them.** `grade_item` copies every file
   under `key/<which>/<problem>/tests/` that the learner's own `tests/` doesn't already have (i.e.
   the held-out ones — `visible.rs` is never touched) into the learner's problem directory, runs
   `cargo test --no-fail-fast` there against the learner's actual edited source, then deletes exactly
   what it copied in, in a `finally` — cleanup runs even when `cargo test` itself fails to build. This
   reads `key/` (by design: the team lead's ruling that the no-key rule binds the trainer session,
   `allowlist.md`, not this script's own grading step), but never *prints* anything from it —
   `item_text` (presentation) and `grade_item` (grading) are separate code paths; `assert_no_key`
   still refuses any `key/` path handed to the presentation side, untouched.

**A fourth thing I found while actually running this against P3's real `u01` items**, not asked for
but load-bearing: the old `run_cargo_test` called `sys.exit` on "no test result", meaning a build
failure aborted grading — but P3's own stub items are *routinely* unedited "fix the compile error"
stubs that don't compile yet (P3-selfcheck's own table shows this for most of u01's probe-a stubs).
That would have crashed the probe on the first un-fixed item and never logged the other two, let
alone the failing one. Changed `run_cargo_test` to grade a build failure as `(False, 0.0)` — a full
miss, not a script abort — since every item must still get its row (T8). Also found: a real grading
run leaves `target/` inside the item's own directory (each problem declares its own `[workspace]`),
which crashed a second presentation of the same item on a binary file inside it; `item_text` now
skips `target/` the same way it skips `key/`.

Verified end to end against the real, unedited `training/rust/items/u01-own-move-borrow/probe-a/`
(all three problems, all still unedited stubs — the correct, expected `false, 0.0000` for each,
matching P3-selfcheck's own recorded stub-compile-error table exactly), then cleaned up every
artifact that run left behind: the `target/` directories, the `Cargo.lock` files `cargo test`
generated, and reverted `training/rust/record/items.csv` to header-only (my verification calls wrote
real rows to the live record — caught via `git diff` before reporting, not left in).

```
$ uv run pytest scripts/train/tests
============================== 69 passed in 8.36s ==============================
$ uv run python scripts/train/check_record.py
record: 0 FAIL
```

New/changed tests in `test_probe.py`: `test_list_problem_dirs_finds_every_crate_sorted`,
`test_list_problem_dirs_refuses_an_empty_directory`, `test_heldout_test_files_excludes_what_the_learner_already_has`,
`test_grade_item_copies_heldout_runs_and_cleans_up`, `test_grade_item_fails_a_wrong_implementation_and_still_cleans_up`,
`test_grade_item_grades_a_build_failure_as_a_full_miss_and_still_cleans_up`,
`test_run_probe_logs_every_item_even_when_one_fails_to_compile`,
`test_run_probe_grades_every_item_and_logs_one_row_each`, `test_run_cargo_test_uses_no_fail_fast`,
`test_item_text_skips_a_build_directory_without_choking_on_binary_files`. `test_session.py`'s
due-probe round trip rebuilt against a real minimal crate + `key/` mirror in place of the old
`probe-b/prompt.md` stub.

## `items/` stays read-only: staged working copies (team lead, 2026-09-28)

Added `probe.stage_item(source_dir, session_id, unit) -> Path`: copies a stub crate to
`training/rust/work/<session_id>/<unit>/<source_dir.name>/` (gitignored — `.gitignore` gained
`training/rust/work/`, next to the existing `training/**/target/`/`training/**/Cargo.lock` lines).
`run_probe` now stages every problem before presenting or grading it; presentation and grading both
operate on the staged copy, never on `training/rust/items/` directly. `session_id` is a new required
positional argument to `run_probe` and `probe.py`'s CLI (`--session-id`); `session.py` generates one
`session_id` per `open_session` call and threads it through both the due probes and the trainer
launch prompt (`trainer_launch_command` now takes an optional `session_id`, defaulting to a fresh
one only when called directly, e.g. from tests).

For "session.py for practice problems": added `session.stage_practice_items(items_root, unit,
session_id)`, staging whichever of `attempt/`, `reuse-1/`, `reuse-2/`, `unshown/` exist for a unit
into the same `training/rust/work/<session_id>/<unit>/<item>/` shape, reusing `probe.stage_item`
rather than a second copy of the copy logic. Wired into `open_session` right after
`ensure_unit_crate(unit)` for the next unit.

**Deliberately not done, flagged rather than silently folded in**: `permission_settings`'s `CRATE`
(the trainer's Read/Glob/Bash grant) still names `training/rust/<unit>/` — `ensure_unit_crate`'s
empty `cargo new` workspace member — not the staged `training/rust/work/<session_id>/<unit>/`
directory practice items now actually live in. Right now staging happens but the trainer's own
permission grants don't point at it yet, which is the same gap P3-selfcheck's finding #6 named
before this message ("that works if session.py copies attempt/ there; otherwise it is an allowlist
gap") — this closes half of it (the copying) but not the other half (repointing `CRATE`). Repointing
it also means moving the `Read(UNIT/reuse-1/**)` etc. patterns (currently granted straight off
`items/`, itself now stale under this ruling) to the staged location, and updating `bash_guard.py`'s
`--crate` argument and the hook's cwd check to match. That's a further, consequential change to the
trainer's whole permission surface — asking before touching it rather than quietly redefining what
the trainer can read mid-session.

New tests: `test_probe.py::test_stage_item_copies_to_work_root_leaving_the_source_untouched` and
**`test_run_probe_leaves_items_byte_identical`** (the test explicitly asked for) — a full snapshot of
`items/` before and after a probe run whose `wait` callback edits the *staged* copy's `src/lib.rs`
to something else entirely, asserting the snapshot is unchanged. `test_session.py`'s
`test_open_stages_the_next_units_practice_items_leaving_items_byte_identical` covers the same
property for `stage_practice_items`.

```
$ uv run pytest scripts/train/tests
============================== 72 passed in 9.46s ==============================
$ uv run python scripts/train/check_record.py
record: 0 FAIL
```

`training/rust/work/` confirmed gitignored (`git check-ignore -v`) and cleaned up after a manual
check; the real `training/rust/items/` tree was untouched by any of my own testing this round (the
files showing as modified/untracked under `items/` in `git status` are other agents' concurrent P3
work, unrelated to this change).
