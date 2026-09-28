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
