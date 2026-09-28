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

---

# Revision 2 (2026-09-28): probe-b rewritten from the revision-2 specs

This revision replaces every item above. The earlier sections record revision 1, whose items are deleted. Inputs: the three `trainer/specs/*-probe-b-spec.md` revision 2, the README, `u01-own-move-borrow/probe-a/p3-shift/tests/structure.rs` (for the probe-trait mechanism only), and `u02-enums-match/reuse-1/tests/structure.rs` lines 1–165. Nothing else under `items/<unit>/` was opened. Everything was built in `/private/tmp/gym-scratch/t-p3-author-b/`; no `target/` or `Cargo.lock` is in the item tree (checked with `find`). Locked files are byte-identical between stub and key (`cmp` over every file outside `src/` and `prediction.txt`).

## Items

| unit | slot | crate | form |
|---|---|---|---|
| u01 | p1 | `p1-pallet-row` | fix E0502 |
| u01 | p2 | `p2-name-tidy` | fix E0382 at a call site |
| u01 | p3 | `p3-delivery-zone` | fix E0382 in a loop (method receiver) |
| u02 | p1 | `p1-lift-log` | predict-output |
| u02 | p2 | `p2-quote-book` | fix E0004 from guards |
| u02 | p3 | `p3-trail-advice` | write-to-tests, no catch-all |
| u03 | p1 | `p1-note-transpose` | write-to-tests |
| u03 | p2 | `p2-port-vlan` | fix E0277 ×2 |
| u03 | p3 | `p3-lap-spread` | write-to-tests, replace panics |

## Required differences and what locks them

Paths are relative to `training/rust/items/<unit>/key/probe-b/`.

- **u01 p1: data shape and return type.** The row holds `Pallet { label: String, weight_kg: u32 }` (`p1-pallet-row/src/lib.rs:1`). `tests/structure.rs` keeps it not `Copy`. The signature returns `Option<u32>` (`tests/heldout.rs:22`), and an empty row gives `None`. The element is read with `first`, and the mutation is `insert(0, _)`. The visible test `tests/visible.rs:8` builds `Pallet` values, so a body written for plain integers with a bare-integer return does not compile. The `zero-for-empty-bare-u32` row shows the return type failing.
- **u01 p2: ownership direction.** The callee sorts and dedups in place, and the caller returns `removed` plus the last name after sorting (`p2-name-tidy/src/lib.rs:14`, locked at `tests/heldout.rs:26`). A shared borrow does not compile (E0596). A reorder-only fix fails 5 tests. Rebuilt strings fail the heap-address tests (`tests/heldout.rs:58`).
- **u01 p3: call site and data shape.** The consuming use is `zone.covers(..)` with a by-value `self` receiver. `Zone` owns a `String` and a `Vec<u32>` (`p3-delivery-zone/src/lib.rs:1`). The visible test `tests/visible.rs:13` calls the method with method syntax and reads `zone.name` after the loop. A free function fails with E0599, and a derived `Copy` fails with E0204.
- **u02 p1: data shape.** It uses the struct-like `Lift::Trip { from, to }`. It has a nested literal-plus-binding arm (`Trip { from: 0, to }`), a guard that compares two fields (`from == to`, `to > from`), `t @ -3..=-1`, `'o' | 'O'`, and a guard on a `String` (`starts_with("FIRE")`). Two values fall through to their variant's general arm (`Trip { 9, 6 }`, `Alarm("stuck")`). The test reads `prediction.txt` relative to the working directory.
- **u02 p2: data shape and return type.** The scrutinee is `Quote::Pair { bid: i64, ask: i64 }` with a second variant, `Halted`. The guards are `bid > ask`, `bid == ask`, `bid < ask`, and the function returns the crate enum `Book` (`p2-quote-book/src/lib.rs:1,7,15`, locked at `tests/heldout.rs:22`).
- **u02 p3: return type and data shape.** It returns `Advice { Go, Caution(u8), Stop }`. `Segment::Path(Surface)` carries a crate enum, so those arms need nested patterns (`p3-trail-advice/src/lib.rs:1,7,15`, locked at `tests/heldout.rs:9`). `Climb` has two range thresholds (300, 800) and a `roped` override. The scanner is `tests/structure.rs`, lines 1–165 copied verbatim, plus `every_arm_names_a_variant` at line 169.
- **u03 p1: call site, data shape and return type.** `transpose(text, semitones: i8)` strips the prefix `N`, parses a `u8`, and applies `checked_add_signed`, so it can overflow in both directions. It returns `Pitch { written, sounding }` (`p1-note-transpose/src/lib.rs:11,17`, locked at `tests/heldout.rs:34`).
- **u03 p2: data shape and return type.** It parses `port: &str` as `u8` and `vlan: &str` as `u16`, from two arguments with no split, and returns `Link { port: u8, vlan: u16 }` (`p2-port-vlan/src/lib.rs:11,17`, locked at `tests/heldout.rs:41`). `link("256", "1")` shows the per-type overflow. The `From` check is `tests/structure.rs`, lines 1–165 copied verbatim, plus `no_from_impl` at line 169.
- **u03 p3: data shape and return type.** It takes one `&str`, split by `split_terminator(';')`. The stub seeds from `fields[0]`, which panics on empty input, and unwraps inside the loop. It returns `Spread { fastest, slowest }` (`p3-lap-spread/src/lib.rs:8,14`, locked at `tests/heldout.rs:26`).

## Results (76 checks: 75 as expected, 0 mismatches, 1 residual marked `info`)

Harness: `/private/tmp/gym-scratch/t-p3-author-b/grade.py`. Each check gets its own `CARGO_TARGET_DIR`. Variants are in `/private/tmp/gym-scratch/t-p3-author-b/variants/`. Each key row runs the key's own structure tests and scans, so the keys obey every ban.

| item | check | expected | got | verdict | cargo test |
|---|---|---|---|---|---|
| u01/p1-pallet-row | key | green | green | ok | 8 passed, 0 failed |
| u01/p1-pallet-row | stub crate | red | red | ok | compile error: E0502 |
| u01/p1-pallet-row | stub graded on key | red | red | ok | compile error: E0502 |
| u01/p1-pallet-row | alt-get-zero | green | green | ok | 8 passed, 0 failed |
| u01/p1-pallet-row | alt-map-before-insert | green | green | ok | 8 passed, 0 failed |
| u01/p1-pallet-row | copied-row | red | red | ok | 7 passed, 1 failed (no_clone) |
| u01/p1-pallet-row | read-after-insert | red | red | ok | 5 passed, 3 failed (empty_row_gives_none, weight_is_the_one_from_before_the_insert, returns_the_old_front_weight) |
| u01/p1-pallet-row | rebuilt-row | red | red | ok | 7 passed, 1 failed (surviving_pallets_keep_their_strings) |
| u01/p1-pallet-row | zero-for-empty-bare-u32 | red | red | ok | compile error: E0308, E0308, E0308, E0308, E0308, E0308 |
| u01/p2-name-tidy | key | green | green | ok | 9 passed, 0 failed |
| u01/p2-name-tidy | stub crate | red | red | ok | compile error: E0382 |
| u01/p2-name-tidy | stub graded on key | red | red | ok | compile error: E0382 |
| u01/p2-name-tidy | clone-the-list | red | red | ok | 6 passed, 3 failed (last_name_is_the_original_string, names_are_not_copied, surviving_repeat_is_the_first_one) |
| u01/p2-name-tidy | give-and-take-back | probe | green | info | 9 passed, 0 failed |
| u01/p2-name-tidy | rebuilt-strings | red | red | ok | 7 passed, 2 failed (last_name_is_the_original_string, surviving_repeat_is_the_first_one) |
| u01/p2-name-tidy | reorder-only | red | red | ok | 4 passed, 5 failed (last_input_is_not_the_last_name, all_the_same, last_name_is_the_original_string, surviving_repeat_is_the_first_one, removes_repeats_and_reports_the_last_name) |
| u01/p2-name-tidy | shared-borrow | red | red | ok | compile error: E0596, E0596 |
| u01/p3-delivery-zone | key | green | green | ok | 10 passed, 0 failed |
| u01/p3-delivery-zone | stub crate | red | red | ok | compile error: E0382 |
| u01/p3-delivery-zone | stub graded on key | red | red | ok | compile error: E0382 |
| u01/p3-delivery-zone | change-outer-signature | red | red | ok | compile error: E0308, E0308, E0308, E0308, E0308, E0382, E0308, E0308 |
| u01/p3-delivery-zone | clone-call-by-value-receiver | red | red | ok | compile error: E0283, E0382 |
| u01/p3-delivery-zone | clone-call | red | red | ok | compile error: E0283 |
| u01/p3-delivery-zone | derive-copy | red | red | ok | compile error: E0204 |
| u01/p3-delivery-zone | free-function | red | red | ok | compile error: E0599 |
| u02/p1-lift-log | key | green | green | ok | 1 passed, 0 failed |
| u02/p1-lift-log | stub crate | red | red | ok | 0 passed, 1 failed (prediction_matches_the_output) |
| u02/p1-lift-log | stub graded on key | red | red | ok | 0 passed, 1 failed (prediction_matches_the_output) |
| u02/p1-lift-log | alt-correct-with-trailing-whitespace | green | green | ok | 1 passed, 0 failed |
| u02/p1-lift-log | misread-guard-ignored | red | red | ok | 0 passed, 1 failed (prediction_matches_the_output) |
| u02/p1-lift-log | misread-later-arm-over-earlier | red | red | ok | 0 passed, 1 failed (prediction_matches_the_output) |
| u02/p1-lift-log | misread-range-excludes-end | red | red | ok | 0 passed, 1 failed (prediction_matches_the_output) |
| u02/p2-quote-book | key | green | green | ok | 8 passed, 0 failed |
| u02/p2-quote-book | stub crate | red | red | ok | compile error: E0004 |
| u02/p2-quote-book | stub graded on key | red | red | ok | compile error: E0004 |
| u02/p2-quote-book | alt-equal-as-the-unguarded-arm | green | green | ok | 8 passed, 0 failed |
| u02/p2-quote-book | alt-if-chain-in-one-arm | green | green | ok | 8 passed, 0 failed |
| u02/p2-quote-book | panicking-filler-arm | red | red | ok | 6 passed, 2 failed (no_arm_added, no_panicking_arm) |
| u02/p2-quote-book | unreachable-wildcard-added | red | red | ok | 7 passed, 1 failed (no_arm_added) |
| u02/p2-quote-book | wrong-answer-equal-is-normal | red | red | ok | 5 passed, 3 failed (equal_at_both_extremes, neighbours, each_state_once) |
| u02/p2-quote-book | wrong-answer-guard-widened | red | red | ok | 5 passed, 3 failed (neighbours, equal_at_both_extremes, each_state_once) |
| u02/p3-trail-advice | key | green | green | ok | 14 passed, 0 failed |
| u02/p3-trail-advice | stub crate | red | red | ok | 1 passed, 8 failed (closed, deep_river, long_climb_roped, long_climb_unroped, middle_climb, paths, short_climb, shallow_river) |
| u02/p3-trail-advice | stub graded on key | red | red | ok | 3 passed, 11 failed (climb_boundaries_unroped, climb_boundaries_roped, river_boundaries, long_climb_roped, long_climb_unroped, middle_climb, closed, deep_river, shallow_river, paths, short_climb) |
| u02/p3-trail-advice | alt-guards-instead-of-ranges | green | green | ok | 14 passed, 0 failed |
| u02/p3-trail-advice | alt-wildcards-inside-variant-patterns | green | green | ok | 14 passed, 0 failed |
| u02/p3-trail-advice | bound-catch-all | red | red | ok | 13 passed, 1 failed (every_arm_names_a_variant) |
| u02/p3-trail-advice | nested-match-catch-all | red | red | ok | 13 passed, 1 failed (every_arm_names_a_variant) |
| u02/p3-trail-advice | off-by-one-300 | red | red | ok | 12 passed, 2 failed (climb_boundaries_unroped, climb_boundaries_roped) |
| u02/p3-trail-advice | off-by-one-50 | red | red | ok | 13 passed, 1 failed (river_boundaries) |
| u02/p3-trail-advice | off-by-one-800 | red | red | ok | 12 passed, 2 failed (climb_boundaries_unroped, climb_boundaries_roped) |
| u02/p3-trail-advice | wildcard-arm | red | red | ok | 13 passed, 1 failed (every_arm_names_a_variant) |
| u03/p1-note-transpose | key | green | green | ok | 13 passed, 0 failed |
| u03/p1-note-transpose | stub crate | red | red | ok | 0 passed, 4 failed (out_of_range, moves_a_note_up_and_down, bad_number, missing_prefix) |
| u03/p1-note-transpose | stub graded on key | red | red | ok | 2 passed, 11 failed (empty_input, bottom_edge, prefix_elsewhere, no_panic_on_input, number_edges, prefix_alone, top_edge, missing_prefix, bad_number, moves_a_note_up_and_down, out_of_range) |
| u03/p1-note-transpose | alt-explicit-match | green | green | ok | 13 passed, 0 failed |
| u03/p1-note-transpose | alt-own-range-check | green | green | ok | 13 passed, 0 failed |
| u03/p1-note-transpose | overflow-unchecked | red | red | ok | 10 passed, 3 failed (bottom_edge, top_edge, out_of_range) |
| u03/p1-note-transpose | unwrap-kept-on-parse | red | red | ok | 9 passed, 4 failed (no_panic_on_input, prefix_alone, number_edges, bad_number) |
| u03/p1-note-transpose | wrong-variant-for-parse | red | red | ok | 10 passed, 3 failed (prefix_alone, number_edges, bad_number) |
| u03/p2-port-vlan | key | green | green | ok | 13 passed, 0 failed |
| u03/p2-port-vlan | stub crate | red | red | ok | compile error: E0277, E0277 |
| u03/p2-port-vlan | stub graded on key | red | red | ok | compile error: E0277, E0277 |
| u03/p2-port-vlan | alt-explicit-match | green | green | ok | 13 passed, 0 failed |
| u03/p2-port-vlan | one-from-impl | red | red | ok | 9 passed, 4 failed (vlan_parse_reported_before_the_reserved_check, vlan_overflow, no_from_impl, bad_vlan) |
| u03/p2-port-vlan | unwrap-kept-on-vlan | red | red | ok | 9 passed, 4 failed (no_panic_on_input, vlan_parse_reported_before_the_reserved_check, vlan_overflow, bad_vlan) |
| u03/p2-port-vlan | vlan-parsed-first | red | red | ok | 12 passed, 1 failed (port_reported_first) |
| u03/p2-port-vlan | wrong-variant-for-vlan | red | red | ok | 10 passed, 3 failed (vlan_overflow, vlan_parse_reported_before_the_reserved_check, bad_vlan) |
| u03/p3-lap-spread | key | green | green | ok | 14 passed, 0 failed |
| u03/p3-lap-spread | stub crate | red | red | ok | 1 passed, 2 failed (bad_lap_in_the_middle, empty_input) |
| u03/p3-lap-spread | stub graded on key | red | red | ok | 5 passed, 9 failed (empty_field_between_separators, bad_lap_last, extremes, first_of_two_bad_laps, bad_lap_alone, bad_lap_first, no_panic_on_input, empty_input, bad_lap_in_the_middle) |
| u03/p3-lap-spread | alt-explicit-match-early-return | green | green | ok | 14 passed, 0 failed |
| u03/p3-lap-spread | guard-only-empty | red | red | ok | 6 passed, 8 failed (bad_lap_first, empty_field_between_separators, first_of_two_bad_laps, bad_lap_alone, extremes, no_panic_on_input, bad_lap_last, bad_lap_in_the_middle) |
| u03/p3-lap-spread | position-from-one | red | red | ok | 7 passed, 7 failed (empty_field_between_separators, bad_lap_last, first_of_two_bad_laps, extremes, bad_lap_first, bad_lap_alone, bad_lap_in_the_middle) |
| u03/p3-lap-spread | split-not-terminator | red | red | ok | 13 passed, 1 failed (trailing_separator_ends_the_list) |
| u03/p3-lap-spread | wrong-variant-for-empty | red | red | ok | 13 passed, 1 failed (empty_input) |

## Stub build errors and compiler hints

- u01 p1: `E0502` cannot borrow `*row` as mutable, 1 error. No hint.
- u01 p2: `E0382` borrow of moved value `names`, 1 error. The compiler first suggests borrowing the parameter in `drop_repeats`. A shared borrow then fails with E0596, and the mutable borrow is the fix. Its second suggestion is to clone, which the scan and the heap test fail.
- u01 p3: `E0382` use of moved value `zone`, labelled "`zone` moved due to this method call, in previous iteration of loop", 1 error. rustc 1.91 phrases the spec's "value moved here, in previous iteration of loop" this way for a method call.
- u02 p2: `E0004` `Quote::Pair { .. }` not covered, 1 error. The hint is to add a wildcard or explicit arm. A panicking or unreachable filler fails `no_panicking_arm` / `no_arm_added`.
- u03 p2: `E0277` ``?` couldn't convert the error to `LinkError``, 2 errors. The hint is to implement `From<ParseIntError>`, and `no_from_impl` fails that.

## Open points and defaults (default, unmeasured)

1. **Residual, u01 p2.** The callee takes the list by value and hands it back as a tuple (`give-and-take-back`), and that passes all tests. The spec leaves the callee's signature free, so no test can refuse this route without locking it. It is a second fix family, against the spec's "exactly one". The default is to leave it open and flag it to the isomorph checker.
2. u02 p2 keeps revision 1's arm cap (at most 4 `=>`), stated in `spec.md`. It exists because an unreachable filler returning a wrong answer (`unreachable-wildcard-added`) passes every behaviour test.
3. u01 p3 locks derives with a `Clone` probe in `tests/heldout.rs`, built on the same ambiguity mechanism. Because of it, a clone workaround fails to compile (E0283) before the clone-call scan runs.
4. u03 p3 uses `split_terminator(';')` so that empty input yields no fields and the stub's `fields[0]` panics, as the spec asks. `spec.md` names that method, and a trailing `;` ends the list (the `split-not-terminator` row is red). The stated behaviour is `Empty` only for `""`, and `";"` is `BadLap { position: 0 }`.
5. u03 p2 adds an own check, `ReservedVlan` for VLAN 0, which gives a 3-variant enum. The spec does not fix the size.
6. The scanner's `arms_not_naming_a_variant` scans every `match` in `src/lib.rs`, nested ones included. That is how `nested-match-catch-all` fails. `Segment::Path(_)` after the named surfaces still passes, because it names its variant (`alt-wildcards-inside-variant-patterns`).
7. I did not run a rename-port of probe-a's key, because I never opened probe-a. Each difference above is fixed in a locked signature, a given type, or a visible test, and the isomorph rerun (PLAN:74) is the fresh sonnet's. The 3-minute difficulty is unmeasured.
8. The checks file keeps the dispatch's name (`P3b-selfcheck.md`). The specs name `P3-probe-b-selfcheck.md`.
