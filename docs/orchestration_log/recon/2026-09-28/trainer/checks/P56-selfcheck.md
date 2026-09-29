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

## Repointing the trainer's grants at the staged copies (team lead, 2026-09-28, go-ahead on the flagged item above)

Every place `CRATE` meant `training/rust/<unit>/` now means the staged practice copy,
`training/rust/work/<session_id>/<unit>/practice/`:

- `session.unit_paths(unit, session_id)` — now takes `session_id` too. `UNIT` (`items/<unit>/`) is
  prose-only from here: `attempt.md`, `example.md`, `hints.yaml`. `CRATE` is the staged practice dir.
- `session.permission_settings(unit, session_id)` — dropped the direct `Read(UNIT/reuse-1/**)`,
  `Read(UNIT/reuse-2/**)`, `Read(UNIT/unshown/**)` rows entirely (the staged copy covers them via
  `CRATE/**`); kept the three prose rows.
- `session.write_settings_file`/`trainer_launch_command` — both thread `session_id` through; a
  direct call still defaults to a fresh one, but the docstring is explicit that nothing is staged
  under a session id nobody staged anything into.
- **Kept the two staging areas apart on purpose.** `probe.stage_item` gained a required `kind`
  argument (`"probe"` from `probe.py`, `"practice"` from `session.stage_practice_items`), so a
  session that runs a delayed probe for a unit *and* practices that same unit in the same session
  never has the probe's staged copy fall inside `CRATE/**` by a naming or path coincidence — rule 19,
  the trainer must never see a probe. `PRACTICE_STAGE_KIND = "practice"` names the segment
  `unit_paths` and `permission_settings` both point at.
- **`trainer_guard.py`'s cwd check widened, not loosened.** `CRATE` now holds several sibling crates
  (`attempt/`, `reuse-1/`, `reuse-2/`, `unshown/`), so `cargo test`'s cwd is one of them, not `CRATE`
  itself. `cwd_is_under(cwd, crate)` accepts `crate` or anything starting with `crate + "/"` — a
  string-prefix trap (`.../practice-extra` incorrectly passing a bare `.startswith(crate)`) is
  covered by its own test.
- **`docs/orchestration_log/recon/2026-09-28/trainer/agent/allowlist.md` updated to match** — UNIT/CRATE
  redefined, the direct reuse/unshown/attempt reads moved from "Allow" to an explicit callout under
  "Deny", the "Claude Code permission form" section brought current, and the three "Open points" from
  the original draft rewritten as built-and-tested facts (the hook, the cwd check, the verified
  `--settings` syntax) rather than defaults. `allowlist.md` is still prose kept in sync by hand, not
  parsed at run time — the same disclosed relationship as before, just re-synced.

12 new/changed tests: `test_trainer_guard.py` gained
`test_cargo_in_a_sibling_crate_under_the_staged_practice_dir_is_allowed` and
`test_cargo_just_outside_the_staged_practice_dir_is_denied` (the string-prefix trap, explicitly);
`test_session.py`'s allowlist tests now pass an explicit `session_id` and assert the
reuse-1/reuse-2/unshown/attempt rows are *absent* from `allow` (they used to assert presence);
`test_probe.py`'s `stage_item`/byte-identical tests updated for the new `kind` segment in the staged
path.

```
$ uv run pytest scripts/train/tests
============================== 74 passed in 7.29s ==============================
$ uv run python scripts/train/check_record.py
record: 0 FAIL
```

Verified live against the real repo (a scratch `session_id`, no actual staging triggered by a bare
`permission_settings()` call, so nothing needed cleanup): `permission_settings("u01-own-move-borrow",
"verify-sess")` produces `CRATE = .../training/rust/work/verify-sess/u01-own-move-borrow/practice`
and a hook command naming that exact path with `--crate`.

**Not done, not asked**: `ensure_unit_crate`'s `cargo new` workspace scaffold at
`training/rust/<unit>/` is still called from `open_session` (an existing, passing test depends on
it) but is no longer where any permission grant points — it's now unused by the trainer's own
sandbox. Flagging it as dead weight rather than removing it unasked: happy to delete it (and the
`training/rust/Cargo.toml` workspace machinery it maintains) on the word, since nothing reads it now.

## Removed the dead scaffold (team lead, 2026-09-28, go-ahead on the item above)

Deleted from `scripts/train/session.py`: `ensure_unit_crate`, `workspace_path`, `read_members`,
`write_workspace`, and the now-unused `TRAINING_ROOT` constant and `import re`/`import subprocess`
lines (nothing else in the file used either). Removed the `ensure_unit_crate(unit)` call from
`open_session` — staging the next unit's practice items is now the whole of that branch. No
`training/rust/Cargo.toml` existed as a committed file (it was only ever generated at runtime,
already gitignored under `training/**/Cargo.lock` alongside `training/**/target/`), so there was
nothing further to delete on disk.

In `test_session.py`: dropped the `TRAINING_ROOT` monkeypatch (the attribute no longer exists on
`session`), the `read_workspace_members` helper, and the two workspace-specific assertions
(`"unit-2" in read_workspace_members(...)"`, the `Cargo.toml` existence check) from
`test_open_with_no_due_probe_hands_off_to_the_next_unit` — which no longer needs `cargo` at all now
that nothing in its path calls it, so its `@pytest.mark.skipif(CARGO_MISSING, ...)` came off too.
Updated both files' module docstrings, which still described "a unit's crate is created on demand
and joins the workspace."

```
$ uv run pytest scripts/train/tests
============================== 74 passed in 7.33s ==============================
$ uv run python scripts/train/check_record.py
record: 0 FAIL
```

Same test count as before (74): this was a deletion of dead assertions and dead production code
together, not a net-new test.

## `log.py`'s `turn` kinds and `note` field (team lead, 2026-09-29)

`record_schema.py`'s `turns.kind` enum gained `start`, `present`, `ladder-gap` alongside the v0.1
set. Added a `note` column (`free_text`: any string, including empty — its requiredness isn't a
column-shape question). `note` is required (non-blank) for `kind == "ladder-gap"` and refused as
non-blank for every other kind — a rule no single column's own validator can express, since it never
sees another column's value. Added `record_schema.ROW_CHECKS`, a new, small mechanism: whole-row
rules applied after every per-column check passes, keyed by file name (only `turns` has one so far).
Wired into both `log.py`'s `build_row` and `check_record.py`'s `check_file`, so a malformed row is
refused at write time and a hand-edited one is still caught by the checker.

`log.py`'s `turn` CLI alias gained a `--note` flag. Read rust-trainer.md v0.2 rule 38's own words
before wiring it up — "`--note` is required for `ladder-gap`, otherwise absent" — so a non-ladder-gap
turn is expected to *omit* the flag, not pass `--note none`; `turn_fields` now defaults `note` to
blank when the flag is missing entirely (an explicit `--note none` still works too, for a trainer
that passes one anyway — the earlier "any flag value of exactly `none` maps to blank" rule, kept).
Regenerated `training/rust/record/turns.csv`'s header straight from the schema (it was still
header-only — nothing to migrate).

`training/rust/record/turns.csv`: `timestamp,session,n,kind,item,minute,request_kind,note`.

14 new/changed tests across `test_log.py` and `test_check_record.py`: all v0.1/v0.2 kinds accepted;
`ladder-gap` without a note refused (both at write time and by the checker); a non-`ladder-gap` kind
with a note refused (both); `ladder-gap` with a note accepted and clean; `--note none` maps to
blank; **`--note` omitted entirely also defaults to blank** (the actual v0.2 invocation shape, not
just the `none`-flag one — caught by reading rule 38's exact wording rather than assuming symmetry
with `--request`).

## Trainer v0.2 installed (team lead, 2026-09-29)

`trainer.md` already showed `# rust-trainer v0.2` when checked — copied verbatim to
`.claude/agents/rust-trainer.md` (diffed identical after the copy).

## P6 dry run, end to end (team lead, 2026-09-29)

Live repo, real `u01-own-move-borrow`, real record files — not an isolated tmp copy, per the ask.
Backed up all five record CSVs and a full `sha256` manifest of `training/rust/items/` before
touching anything, so both could be verified byte-identical (record: reverted; items/: never
touched) and restored exactly afterward.

**Setup**: appended a `queue.csv` row (`kind=next_unit, unit=u01-own-move-borrow`) via `log.py` so
`session.py open` would pick u01 as the next unit.

**Step 1 — `session.py open`, a fresh sonnet playing the learner.** Dispatched a fresh `sonnet`
subagent with an explicit, doubled-down instruction not to execute the printed
`claude --agent rust-trainer ...` line under any circumstance — only to run `session.py open`, read
the output as a learner would, and quote that line back verbatim. It complied exactly: ran the
command, reported `due delayed probes run: none`, `next unit: u01-own-move-borrow`, and the full
launch command (embedding a real `.trainer-settings.json` path and the session/unit/items/record
prompt), and did not invoke it. Its own first-impression note, worth relaying: the printed "sessions
tail"/"items tail" sections show only bare CSV headers with no "no history yet" framing, and the
same header text appears a second time inside the launch prompt's quoted argument — by design (the
trainer gets its own copy of the tail as initial context), but it reads as a doubled, unexplained
artifact to a first-time viewer. Not fixed here — a copy/documentation clarity issue, not a
correctness one; flagging for whoever owns the launch prompt's wording next.

**Real bug found: a colon in a session id breaks `cargo test` on macOS.** The fresh sonnet's real
`session_id` (`2026-09-29T12:20`, from `session.new_session_id()`) got used literally as a
`training/rust/work/` directory name. Every previous test used a harmless stand-in (`"sess-1"`)
that never contains a colon, so this never showed up before a real dry run used a real id. Cargo
puts the crate's own absolute path into `$DYLD_FALLBACK_LIBRARY_PATH` before invoking the linker,
and that env var uses `:` as its list separator — `error: failed to join paths from
'$DYLD_FALLBACK_LIBRARY_PATH' together`. Confirmed in isolation first (a bare `cargo init` in a
`:`-containing directory reproduces it, nothing else involved). Fixed with `probe.session_path_segment`,
replacing every `:` with `-` before it's ever used as a path component; wired into both
`probe.stage_item` and `session.unit_paths`/`permission_settings` (which builds the same path
independently for `CRATE`) so the two can't drift apart again. Two new tests, including a real
`cargo test` regression test reproducing the exact failure and confirming the fix.

**Step 2 — `probe.py` on u01 `probe-a`, a scripted correct answer.** Wrote real, correct Rust fixes
for all three stub items (`p1-board`: read the max before pushing, not after; `p2-summary`: borrow
the lines instead of consuming them; `p3-shift`: borrow the offset per iteration instead of moving
it, without making `Point` `Copy` — `probe-a/p3-shift` has since grown a `tests/structure.rs` that
fails to compile if `Point` becomes `Copy`, read and respected). First attempt (pre-fix) correctly
graded all three `false, 0.0` — the colon bug, not a scoring bug, confirmed by inspecting the staged
files directly (the edits *did* land; grading just couldn't run `cargo test` at all). Second attempt,
after the path fix: all three graded `true, 1.0000`, logged as six real `items.csv` rows total (three
failed attempts, three corrected ones).

**Step 3 — `session.py close`.** Hit the `--minutes` argparse bug in the same pass (see below);
fixed, then closed cleanly: one `sessions.csv` row, a `delayed_probe` queue row for u01 due in 7
days, a `next_unit` row for a scratch placeholder unit.

**Second real bug found: `--minutes` parsed as a float.** `argparse`'s `--minutes` was `type=float`;
`--minutes 45` produced `"45.0"`, which `sessions.minutes` (`int_at_least`) refused outright. Every
existing test called `close_session()` directly with a Python `int` literal, never through `main()`
with a string argument, so this never surfaced before a real CLI invocation. Fixed: `type=int`,
matching the schema (`--probe-minutes` stays `float`, matching `probe_minutes`'s own column). One
new regression test going through `session.main()` itself, not `close_session()` directly.

**Step 4 — confirmed.** `check_record.py` → `record: 0 FAIL` throughout. `training/rust/items/`'s
full `sha256` manifest identical before vs. after every step (probe grading and practice staging
both operate on `training/rust/work/` copies only). Record showed exactly what was expected: 1
session row, 6 item rows (3 failed + 3 corrected), 3 queue rows (the setup row, the delayed-probe
row, the next-unit row).

**Step 5 — reverted.** All five record CSVs restored to their exact pre-dry-run byte content (all
were header-only before and after — this dry run is the first thing to have written real rows to
them at all). Removed the scratch `training/rust/work/` tree. `check_record.py` confirmed clean
again post-revert.

```
$ uv run pytest scripts/train/tests
============================== 88 passed in 7.77s ==============================
$ uv run python scripts/train/check_record.py    # after the revert
record: 0 FAIL
```

Two real, previously-undetected bugs found and fixed by actually running the system end to end
rather than only through unit tests with harmless stand-in values — both are exactly the kind of
gap a dry run exists to catch (a real session id, a real CLI invocation, both avoided by every
existing test's own convenience shortcuts).

## `session.py` and its launch cruft, dropped (owner ruling, via team lead, 2026-09-29)

The manager summons the trainer as a subagent directly — nothing runs `claude --agent ...`, so the
generated `--settings` file, the printed launch command, and the whole permission/allowlist model
`session.py` built around them are gone. `log.py`, `record_schema.py`, `check_record.py`, `probe.py`
(with its own staging, kept) and `scripts/train/hooks/trainer_guard.py` (kept, wiring now whoever's
job it is outside this file) stay; only session.py-only code came out of them.

### Files deleted

- `scripts/train/session.py`
- `scripts/train/tests/test_session.py`
- `docs/orchestration_log/recon/2026-09-28/trainer/agent/allowlist.md`

### Every function (and its module-level constants) removed with `session.py`

`unit_paths`, `permission_settings`, `new_session_id`, `write_settings_file`,
`trainer_launch_command`, `stage_practice_items`, `completed_delayed_probe_units`,
`due_delayed_probes`, `next_unit`, `record_tail`, `open_session`, `gap_days_since_last_session`,
`close_session`, `main` (session.py's own CLI entry point) — plus the module constants
`PRACTICE_ITEM_NAMES`, `DEFAULT_ITEMS_ROOT`, `TRAINER_GUARD`, `PRACTICE_STAGE_KIND`,
`KEY_DENY_PATTERN`. (`ensure_unit_crate`/`workspace_path`/`read_members`/`write_workspace` and
`TRAINING_ROOT` were already removed in the previous "dead scaffold" pass, so they weren't in the
file to remove again here.)

### Every test removed with `test_session.py`

`test_close_writes_session_and_queue_rows`, `test_main_close_parses_minutes_as_an_integer`,
`test_open_with_no_due_probe_hands_off_to_the_next_unit`,
`test_open_stages_the_next_units_practice_items_leaving_items_byte_identical`,
`test_open_runs_a_due_delayed_probe_then_hands_off`, `test_launch_command_carries_the_full_allowlist`,
`test_a_read_of_any_key_path_is_denied_by_the_pattern`,
`test_launch_command_scopes_the_hook_to_the_named_unit_only`,
`test_open_session_prints_a_launch_command_with_the_deny_rule`.

### What came out of the files that stayed

- **`probe.py`**: `stage_item` lost its `kind` parameter and the `<kind>/` path segment
  (`training/rust/work/<session_id>/<unit>/<item>/`, not `.../<unit>/probe/<item>/`). `kind`
  existed for exactly one reason — keeping `probe.py`'s own probe-staging apart from
  `session.py`'s practice-staging under the same session and unit, so the trainer's `CRATE/**`
  grant could never accidentally reach a probe's staged copy (rule 19). With practice-staging gone,
  there is nothing left to disambiguate against, so the parameter and segment were simplified away
  rather than kept as a needless required argument every caller has to satisfy for a collision that
  no longer exists. Two call sites and two tests updated to match.
- **`log.py`**: one comment's citation of `allowlist.md`'s Bash pattern removed (the substantive
  point — this is rule 38's literal invocation — kept).
- **`scripts/train/hooks/trainer_guard.py`**: its module docstring and `cwd_is_under`'s docstring
  no longer describe `session.py`'s specific launch mechanism or cite `allowlist.md` by name; the
  hook's own behavior (what it checks, why) is unchanged — nothing in its logic existed solely for
  `session.py`, so nothing but prose moved.

### Verified clean

```
$ uv run pytest scripts/train/tests
============================== 79 passed in 8.09s ==============================
$ uv run python scripts/train/check_record.py
record: 0 FAIL
$ uv run python scripts/check_records.py     # the outer, repo-wide memento check
records: 0 FAIL
```

Swept `scripts/train/` for every remaining mention of `allowlist.md`, `session.py`,
`trainer_launch_command`, `permission_settings`, `write_settings_file`, `PRACTICE_STAGE_KIND`,
`stage_practice_items` after the edits: none found. `.claude/memento-map.md` and the outer
`check_records.py`'s pointer check don't reference either deleted path (`docs/orchestration_log/recon/`
paths and `.claude/agents/*.md` both sit outside what that checker scans), so neither deletion needed
a corresponding map or pointer fix.
