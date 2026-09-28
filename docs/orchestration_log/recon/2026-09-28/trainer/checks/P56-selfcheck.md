# P5/P6 self-check — learner record and session logistics

Run: `uv run pytest scripts/train/tests -v` (27 tests) and `uv run python scripts/train/check_record.py`
against the committed `training/rust/record/*.csv` (header-only at this point).

## `uv run pytest scripts/train/tests -v`

```
============================= test session starts ==============================
platform darwin -- Python 3.11.11, pytest-9.1.1, pluggy-1.6.0 -- /Users/ryzhakar/pp/gym/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/ryzhakar/pp/gym
configfile: pyproject.toml
collecting ... collected 27 items

scripts/train/tests/test_check_record.py::test_clean_file_has_no_findings PASSED [  3%]
scripts/train/tests/test_check_record.py::test_bad_enum_is_a_fail PASSED [  7%]
scripts/train/tests/test_check_record.py::test_bad_date_is_a_fail PASSED [ 11%]
scripts/train/tests/test_check_record.py::test_timestamps_going_backward_is_a_fail PASSED [ 14%]
scripts/train/tests/test_check_record.py::test_wrong_header_is_a_fail PASSED [ 18%]
scripts/train/tests/test_check_record.py::test_missing_file_is_a_fail PASSED [ 22%]
scripts/train/tests/test_check_record.py::test_main_exits_1_on_any_fail PASSED [ 25%]
scripts/train/tests/test_check_record.py::test_main_exits_0_when_all_clean PASSED [ 29%]
scripts/train/tests/test_log.py::test_valid_row_is_stamped_and_appended PASSED [ 33%]
scripts/train/tests/test_log.py::test_hand_typed_timestamp_is_refused PASSED [ 37%]
scripts/train/tests/test_log.py::test_malformed_row_is_refused[<lambda>-missing] PASSED [ 40%]
scripts/train/tests/test_log.py::test_malformed_row_is_refused[<lambda>-unknown] PASSED [ 44%]
scripts/train/tests/test_log.py::test_malformed_row_is_refused[<lambda>-not 'true' or 'false'] PASSED [ 48%]
scripts/train/tests/test_log.py::test_malformed_row_is_refused[<lambda>-below 0] PASSED [ 51%]
scripts/train/tests/test_log.py::test_malformed_row_is_refused[<lambda>-not an integer] PASSED [ 55%]
scripts/train/tests/test_log.py::test_malformed_row_is_refused[<lambda>-empty] PASSED [ 59%]
scripts/train/tests/test_log.py::test_append_refuses_a_timestamp_before_the_last_row PASSED [ 62%]
scripts/train/tests/test_log.py::test_append_refuses_a_mismatched_header PASSED [ 66%]
scripts/train/tests/test_log.py::test_append_refuses_a_missing_file PASSED [ 70%]
scripts/train/tests/test_probe.py::test_assert_no_key_refuses_any_key_path PASSED [ 74%]
scripts/train/tests/test_probe.py::test_item_text_excludes_key PASSED    [ 77%]
scripts/train/tests/test_probe.py::test_probe_dir_refuses_a_key_target PASSED [ 81%]
scripts/train/tests/test_probe.py::test_run_probe_grades_with_cargo_test_and_logs_a_row PASSED [ 85%]
scripts/train/tests/test_probe.py::test_run_probe_warns_over_cap PASSED  [ 88%]
scripts/train/tests/test_session.py::test_close_writes_session_and_queue_rows PASSED [ 92%]
scripts/train/tests/test_session.py::test_open_with_no_due_probe_hands_off_to_the_next_unit PASSED [ 96%]
scripts/train/tests/test_session.py::test_open_runs_a_due_delayed_probe_then_hands_off PASSED [100%]

============================== 27 passed in 1.41s ==============================
```

## `uv run python scripts/train/check_record.py`

```
record: 0 FAIL
```

## Coverage against the brief's four required cases

- malformed row refused: `test_log.py::test_malformed_row_is_refused` (6 mutations: missing field,
  unknown field, bad enum, out-of-range int, non-integer, empty string) plus `test_hand_typed_timestamp_is_refused`.
- timestamps stamped: `test_log.py::test_valid_row_is_stamped_and_appended` (the row's `timestamp` is
  the clock's, bounded to the test's own wall-clock window) and `test_append_refuses_a_timestamp_before_the_last_row`.
- `key/` never read by probe.py: `test_probe.py::test_assert_no_key_refuses_any_key_path`,
  `test_item_text_excludes_key`, `test_probe_dir_refuses_a_key_target`.
- session open/close round trip on a synthetic unit with a stub item: `test_session.py` (all three
  tests), using `cargo new --lib` crates and a stub `probe-b/prompt.md` under a temp items root —
  no real trainer, curriculum, or item content involved.

No FAIL, no skip on this machine (`cargo` is on PATH); the two `@pytest.mark.skipif(CARGO_MISSING, ...)`
guards in `test_probe.py` are a defensive default for a machine without `cargo`, not exercised here.
