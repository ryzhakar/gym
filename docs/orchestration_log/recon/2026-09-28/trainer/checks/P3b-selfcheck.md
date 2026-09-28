# P3b self-check: probe-b isomorphs u01–u03

Author: second drill author (opus), 2026-09-28. Written from `trainer/specs/<unit>-probe-b-spec.md` and `training/rust/items/README.md` only. Nothing under `training/rust/items/<unit>/` other than the new probe-b paths was opened, and `P3-selfcheck.md` was not read either, so the table below uses its own shape.

## Outputs

- Stubs: `training/rust/items/<unit>/probe-b/p{1,2,3}-*/`
- Keys: `training/rust/items/<unit>/key/probe-b/p{1,2,3}-*/`. This follows README:8 and the specs' line 3. The dispatch wrote "probe-b/key/", which I read as shorthand for that layout.
- Items: u01 `p1-restock-max` (fix E0502), `p2-tag-report` (fix E0382 at a call), `p3-temp-band` (fix E0382 in a loop). u02 `p1-clock-log` (predict-output), `p2-status-class` (fix E0004 from guards), `p3-parcel-alert` (write-to-tests). u03 `p1-kib-size` (write-to-tests), `p2-int-range` (fix E0277 ×2), `p3-hex-channel` (replace panics).
- The stub's `Cargo.toml`, `spec.md` and `tests/visible.rs` are byte-identical to the key's copies (`cmp`, 27 of 27 files).

## Method

`/private/tmp/gym-scratch/p3b-author/grade.py` (uv, Python) copies each crate to scratch and runs `cargo test --no-fail-fast` with cargo 1.91.1. Each check gets its own `CARGO_TARGET_DIR`. For grading, it copies the key and overlays the `Edit:` file (the stub's file, or a variant from `/private/tmp/gym-scratch/p3b-author/variants/`). green = exit 0.

The harness's first run shared one target dir per item. `copytree` preserves mtimes, so cargo reused stale builds, and the prediction test read the key's own `prediction.txt` through the `CARGO_MANIFEST_DIR` baked into the binary. That run gave 13 false greens. With one target dir per check, all of them turned red as expected. The results below are from the fixed run only.

## Results (68 checks, 0 mismatches)

| item | check | expected | got | verdict | cargo test |
|---|---|---|---|---|---|
| u01/p1-restock-max | key | green | green | ok | 6 passed, 0 failed |
| u01/p1-restock-max | stub crate | red | red | ok | compile error: E0502 |
| u01/p1-restock-max | stub graded on key | red | red | ok | compile error: E0502 |
| u01/p1-restock-max | alt-iter-copied-max | green | green | ok | 6 passed, 0 failed |
| u01/p1-restock-max | change-signature-take-owned | red | red | ok | compile error: E0308, E0308, E0308, E0308, E0308, E0308, E0308, E0308 |
| u01/p1-restock-max | clone-the-stock | red | red | ok | 5 passed, 1 failed (stock_is_not_copied) |
| u01/p1-restock-max | delete-later-use-read-after-push | red | red | ok | 3 passed, 3 failed (empty_stock_gives_none, repeated_restocks_each_report_the_maximum_before_them, returns_the_maximum_from_before_the_addition) |
| u01/p2-tag-report | key | green | green | ok | 6 passed, 0 failed |
| u01/p2-tag-report | stub crate | red | red | ok | compile error: E0382 |
| u01/p2-tag-report | stub graded on key | red | red | ok | compile error: E0382 |
| u01/p2-tag-report | alt-read-total-before-move | green | green | ok | 6 passed, 0 failed |
| u01/p2-tag-report | change-caller-signature | red | red | ok | compile error: E0308, E0308, E0308, E0308, E0308 |
| u01/p2-tag-report | clone-the-tags | red | red | ok | 5 passed, 1 failed (tags_are_not_copied) |
| u01/p2-tag-report | copy-by-rebuilding | red | red | ok | 5 passed, 1 failed (tags_are_not_copied) |
| u01/p2-tag-report | delete-later-use | red | red | ok | 3 passed, 3 failed (many_tags_match_exactly, single_tag_that_is_not_urgent, counts_urgent_tags_and_all_tags) |
| u01/p3-temp-band | key | green | green | ok | 7 passed, 0 failed |
| u01/p3-temp-band | stub crate | red | red | ok | compile error: E0382 |
| u01/p3-temp-band | stub graded on key | red | red | ok | compile error: E0382 |
| u01/p3-temp-band | alt-helper-borrows | green | green | ok | 7 passed, 0 failed |
| u01/p3-temp-band | change-field-types | red | red | ok | compile error: E0308, E0308, E0308, E0308 |
| u01/p3-temp-band | change-outer-signature | red | red | ok | compile error: E0308, E0308, E0308, E0308, E0308, E0308, E0308 |
| u01/p3-temp-band | clone-each-iteration | red | red | ok | 6 passed, 1 failed (no_clone_call) |
| u01/p3-temp-band | delete-later-use | red | red | ok | 4 passed, 3 failed (several_readings_at_and_beyond_the_bounds, one_reading_inside_and_one_outside, counts_readings_inside_the_band) |
| u02/p1-clock-log | key | green | green | ok | 1 passed, 0 failed |
| u02/p1-clock-log | stub crate | red | red | ok | 0 passed, 1 failed (prediction_matches_the_output) |
| u02/p1-clock-log | stub graded on key | red | red | ok | 0 passed, 1 failed (prediction_matches_the_output) |
| u02/p1-clock-log | alt-correct-with-trailing-whitespace | green | green | ok | 1 passed, 0 failed |
| u02/p1-clock-log | misread-guard-ignored | red | red | ok | 0 passed, 1 failed (prediction_matches_the_output) |
| u02/p1-clock-log | misread-literal-beats-earlier-guard | red | red | ok | 0 passed, 1 failed (prediction_matches_the_output) |
| u02/p1-clock-log | misread-range-exclusive | red | red | ok | 0 passed, 1 failed (prediction_matches_the_output) |
| u02/p2-status-class | key | green | green | ok | 7 passed, 0 failed |
| u02/p2-status-class | stub crate | red | red | ok | compile error: E0004 |
| u02/p2-status-class | stub graded on key | red | red | ok | compile error: E0004 |
| u02/p2-status-class | alt-ranges-instead-of-guards | green | green | ok | 7 passed, 0 failed |
| u02/p2-status-class | alt-wildcard-replaces-guarded-arm | green | green | ok | 7 passed, 0 failed |
| u02/p2-status-class | panicking-filler-arm | red | red | ok | 5 passed, 2 failed (no_arm_added, no_panicking_arm) |
| u02/p2-status-class | wildcard-arm-wrong-answer | red | red | ok | 5 passed, 2 failed (every_boundary, each_class_once) |
| u02/p2-status-class | wildcard-filler-arm-added | red | red | ok | 6 passed, 1 failed (no_arm_added) |
| u02/p3-parcel-alert | key | green | green | ok | 14 passed, 0 failed |
| u02/p3-parcel-alert | stub crate | red | red | ok | 0 passed, 8 failed (delayed_short, heavy, delivered, freight, delayed_long, light_and_fragile, light_and_sturdy, lost) |
| u02/p3-parcel-alert | stub graded on key | red | red | ok | 3 passed, 11 failed (delay_boundaries, weight_boundaries_fragile, weight_boundaries_sturdy, delayed_short, delayed_long, freight, delivered, heavy, light_and_sturdy, light_and_fragile, lost) |
| u02/p3-parcel-alert | alt-guards-instead-of-ranges | green | green | ok | 14 passed, 0 failed |
| u02/p3-parcel-alert | off-by-one-delay-threshold | red | red | ok | 13 passed, 1 failed (delay_boundaries) |
| u02/p3-parcel-alert | off-by-one-freight-threshold | red | red | ok | 12 passed, 2 failed (weight_boundaries_sturdy, weight_boundaries_fragile) |
| u02/p3-parcel-alert | off-by-one-heavy-threshold | red | red | ok | 12 passed, 2 failed (weight_boundaries_fragile, weight_boundaries_sturdy) |
| u02/p3-parcel-alert | wildcard-arm | red | red | ok | 13 passed, 1 failed (no_wildcard_arm) |
| u03/p1-kib-size | key | green | green | ok | 14 passed, 0 failed |
| u03/p1-kib-size | stub crate | red | red | ok | 0 passed, 4 failed (missing_unit, too_large, converts_a_size, bad_number) |
| u03/p1-kib-size | stub graded on key | red | red | ok | 2 passed, 12 failed (largest_count_that_fits, empty_input, count_too_big_to_parse, negative_and_spaced_counts, smallest_count_that_overflows, zero, unit_alone, no_panic_on_input, converts_a_size, too_large, missing_unit, bad_number) |
| u03/p1-kib-size | alt-explicit-match-early-return | green | green | ok | 14 passed, 0 failed |
| u03/p1-kib-size | match-wrong-variant-for-parse | red | red | ok | 10 passed, 4 failed (negative_and_spaced_counts, count_too_big_to_parse, unit_alone, bad_number) |
| u03/p1-kib-size | overflow-unchecked | red | red | ok | 12 passed, 2 failed (smallest_count_that_overflows, too_large) |
| u03/p1-kib-size | unwrap-kept-on-parse | red | red | ok | 9 passed, 5 failed (negative_and_spaced_counts, count_too_big_to_parse, no_panic_on_input, unit_alone, bad_number) |
| u03/p2-int-range | key | green | green | ok | 13 passed, 0 failed |
| u03/p2-int-range | stub crate | red | red | ok | compile error: E0277, E0277 |
| u03/p2-int-range | stub graded on key | red | red | ok | compile error: E0277, E0277 |
| u03/p2-int-range | alt-explicit-match | green | green | ok | 13 passed, 0 failed |
| u03/p2-int-range | high-checked-before-low | red | red | ok | 12 passed, 1 failed (low_reported_before_high) |
| u03/p2-int-range | one-from-impl | red | red | ok | 9 passed, 4 failed (extremes, empty_high, only_the_first_separator_splits, bad_high) |
| u03/p2-int-range | unwrap-kept-on-high | red | red | ok | 8 passed, 5 failed (empty_high, extremes, no_panic_on_input, only_the_first_separator_splits, bad_high) |
| u03/p2-int-range | wrong-variant-for-high | red | red | ok | 9 passed, 4 failed (empty_high, extremes, only_the_first_separator_splits, bad_high) |
| u03/p3-hex-channel | key | green | green | ok | 11 passed, 0 failed |
| u03/p3-hex-channel | stub crate | red | red | ok | 1 passed, 2 failed (no_channels, bad_channel_in_the_middle) |
| u03/p3-hex-channel | stub graded on key | red | red | ok | 4 passed, 7 failed (bad_channel_first, bad_channel_last, bad_channel_alone, first_of_two_bad_channels, no_panic_on_input, bad_channel_in_the_middle, no_channels) |
| u03/p3-hex-channel | alt-explicit-match-early-return | green | green | ok | 11 passed, 0 failed |
| u03/p3-hex-channel | guard-only-empty | red | red | ok | 5 passed, 6 failed (first_of_two_bad_channels, bad_channel_last, bad_channel_first, bad_channel_alone, no_panic_on_input, bad_channel_in_the_middle) |
| u03/p3-hex-channel | index-counted-from-one | red | red | ok | 6 passed, 5 failed (first_of_two_bad_channels, bad_channel_first, bad_channel_last, bad_channel_alone, bad_channel_in_the_middle) |
| u03/p3-hex-channel | wrong-variant-for-empty | red | red | ok | 10 passed, 1 failed (no_channels) |

## Stub build errors (`cargo build`, fix-the-compile-error items)

| item | errors | spec slot |
|---|---|---|
| u01/p1 | `error[E0502]: cannot borrow `*stock` as mutable because it is also borrowed as immutable`, 1 error | E0502, borrow from `iter().max()` used after `push` |
| u01/p2 | `error[E0382]: borrow of moved value: `tags``, 1 error | E0382 at a call site |
| u01/p3 | `error[E0382]: use of moved value: `band``, 1 error, with "value moved here, in previous iteration of loop" | E0382 in a loop |
| u02/p2 | `error[E0004]: non-exhaustive patterns: `Response::Status(_)` not covered`, 1 error | E0004 from a guarded last arm |
| u03/p2 | `error[E0277]: `?` couldn't convert the error to `RangeError``, 2 errors | E0277 on two parses |

The u03/p2 stub first failed with E0271 ("type mismatch resolving `<i32 as FromStr>::Err == RangeError`"), because `let lo: i32 = lo.parse()?` lets inference take the error type from the return type. The stub and key now use `parse::<i32>()`, which gives E0277. That row reflects the fixed stub.

What the compiler suggests, per stub:
- u01/p1: nothing.
- u01/p2: first a note to change `count_matching`'s parameter to a borrow, which is a legitimate route and passes (spec allows this). Then a help to clone, which the scan fails.
- u01/p3: first a note to borrow in `contains`, which is legitimate. Then "if `Band` implemented `Clone`, you could clone the value", which the scan fails. Then "move the expression out of the loop", which does not apply because `reading` changes each iteration.
- u02/p2: add a wildcard or explicit arm. The natural fillers (`todo!()`, or an added `_` arm) fail `no_panicking_arm` / `no_arm_added`.
- u03/p2: implement `From<ParseIntError>`. A single impl fails (`one-from-impl` row).

## Things the specs left open (default, unmeasured)

1. u02/p2: a `_` arm returning a wrong answer, when added after the guarded arms, is never reached, so behaviour tests alone cannot fail it. The held-out test `no_arm_added` therefore caps the match at 7 `=>`, the stub's own count, and `spec.md` states that rule. A `_` arm that replaces the guarded last arm and returns `"server error"` passes, because it is the unguarded fix.
2. u02/p3: the `_` scan catches `_ =>` in any textual form and `_ if`. A plain binding catch-all such as `other => None` passes the scan. That is a known residual.
3. u01/p2: the report returns only counts, so there are no returned heap addresses to check. The copy check is a textual ban (clone, to_owned, to_vec, to_string, collect, String::from, format!, .into(). A rebuild through `collect` is caught (`copy-by-rebuilding` row). Rarer copies such as `String::new() + t` evade it.
4. Enum sizes the specs don't fix: u03/p2 `RangeError` has 3 variants. u03/p3 `ChannelError` has 2 (`Empty`, `BadChannel { index }`), and the index counts from 0.
5. u02/p1 `tests/heldout.rs` holds only a comment. The visible test already compares the whole output.
6. u02/p1: the guard-ignored misreading differs from the correct output on 3 lines (1, 3, 7). The range-exclusive misreading differs on line 5, and literal-beats-guard on line 1.
7. Not checked by me: that probe-a's key fails to compile against these tests, and that probe-a's prediction differs from this output. Both are left to the fresh-sonnet isomorph check (PLAN:74), since I never opened probe-a. The 3-minute difficulty target is unmeasured.
8. The checks file name follows the dispatch (`P3b-selfcheck.md`), not the specs' line 47/48 (`P3-probe-b-selfcheck.md`).
