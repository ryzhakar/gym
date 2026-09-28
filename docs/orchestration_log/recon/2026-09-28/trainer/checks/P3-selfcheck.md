# P3 self-check · baseline and units u01–u03

Checked by: the drill author itself (opus, claude-opus-5-5), 2026-09-28. This is an author self-check, not a P7 check: no fresh instance, no swapped order. Recon grade.

Items: `training/rust/items/` (layout and grading rule in its `README.md`). Probe-b specs: `trainer/specs/<unit>-probe-b-spec.md`.

## Method

- Checker: a scratch script, `check_items.py` (uv, stdlib only), run as `uv run --no-project python check_items.py <items> <overlays>`. Scratch is disposable, so the script is described here, not kept.
- Per problem: `cargo test --no-fail-fast` on the key; the same on the stub; the stub's `Edit:` files copied into a copy of the key and tested ("graded"); every non-edit file of the stub byte-compared with the key's copy ("locked files"). Fresh target dirs every run.
- Overlays: known workarounds, each graded against the key, must be red. Legitimate alternative solutions, marked `legit:`, must be green, so that no item demands the key's exact form.
- Hints: every `hints.yaml` parsed (pyyaml via `uv run --with`). Each checked for exactly 3 levels per problem, no line of 8+ characters from its unit's `key/`, and no code tokens.

## Results

Toolchain and run stamp:

```
cargo 1.91.1 (ea2d97820 2025-10-10)
rustc 1.91.1 (ed61e7d7e 2025-11-07)
2026-09-28T14:22
```

| problem | key `cargo test` | stub `cargo test` | stub graded on key | locked files |
|---|---|---|---|---|
| baseline/b1-own | green: 5 passed; 0 failed | red: no test result; build error[E0382]: borrow of moved value: `words` | red: no test result; build error[E0382]: borrow of moved value: `words` | identical |
| baseline/b2-life | green: 5 passed; 0 failed | red: no test result; build error[E0106]: missing lifetime specifier | red: no test result; build error[E0106]: missing lifetime specifier | identical |
| baseline/b3-result | green: 9 passed; 0 failed | red: 0 passed; 3 failed | red: 0 passed; 9 failed | identical |
| baseline/b4-traits | green: 6 passed; 0 failed | red: no test result; build error[E0432]: unresolved import `b4_traits::total_area` | red: no test result; build error[E0432]: unresolved import `b4_traits::total_area` | identical |
| baseline/b5-iter | green: 1 passed; 0 failed | red: 0 passed; 1 failed | red: 0 passed; 1 failed | identical |
| baseline/b6-enum | green: 1 passed; 0 failed | red: 0 passed; 1 failed | red: 0 passed; 1 failed | identical |
| u01-own-move-borrow/attempt | green: 6 passed; 0 failed | red: no test result; build error[E0382]: borrow of moved value: `names` | red: no test result; build error[E0382]: borrow of moved value: `names` | identical |
| u01-own-move-borrow/reuse-1 | green: 6 passed; 0 failed | red: no test result; build error[E0502]: cannot borrow `*scores` as mutable because it is also borrowed as immutable | red: no test result; build error[E0502]: cannot borrow `*scores` as mutable because it is also borrowed as immutable | identical |
| u01-own-move-borrow/reuse-2 | green: 5 passed; 0 failed | red: no test result; build error[E0382]: use of moved value: `msg` | red: no test result; build error[E0382]: use of moved value: `msg` | identical |
| u01-own-move-borrow/unshown | green: 5 passed; 0 failed | red: no test result; build error[E0507]: cannot move out of `self.pending` which is behind a mutable reference | red: no test result; build error[E0507]: cannot move out of `self.pending` which is behind a mutable reference | identical |
| u01-own-move-borrow/probe-a/p1-board | green: 4 passed; 0 failed | red: no test result; build error[E0502]: cannot borrow `self.scores` as mutable because it is also borrowed as immutable | red: no test result; build error[E0502]: cannot borrow `self.scores` as mutable because it is also borrowed as immutable | identical |
| u01-own-move-borrow/probe-a/p2-summary | green: 5 passed; 0 failed | red: no test result; build error[E0382]: borrow of moved value: `lines` | red: no test result; build error[E0382]: borrow of moved value: `lines` | identical |
| u01-own-move-borrow/probe-a/p3-shift | green: 5 passed; 0 failed | red: no test result; build error[E0382]: use of moved value: `offset` | red: no test result; build error[E0382]: use of moved value: `offset` | identical |
| u02-enums-match/attempt | green: 14 passed; 0 failed | red: no test result; build error[E0432]: unresolved imports `u02_attempt::enum_form::fault`, `u02_attempt::enum_form::fault_code`, `u02_attempt::enum_form::label`, `u02_attempt::enum_form::off`, `u02_attempt::enum_form::temp` | red: no test result; build error[E0432]: unresolved imports `u02_attempt::enum_form::fault`, `u02_attempt::enum_form::fault_code`, `u02_attempt::enum_form::label`, `u02_attempt::enum_form::off`, `u02_attempt::enum_form::temp` | identical |
| u02-enums-match/reuse-1 | green: 6 passed; 0 failed | red: 0 passed; 4 failed | red: 1 passed; 5 failed | identical |
| u02-enums-match/reuse-2 | green: 6 passed; 0 failed | red: no test result; build error[E0432]: unresolved imports `u02_reuse_2::cost`, `u02_reuse_2::dot`, `u02_reuse_2::endpoint`, `u02_reuse_2::line`, `u02_reuse_2::pen_up` | red: no test result; build error[E0432]: unresolved imports `u02_reuse_2::cost`, `u02_reuse_2::dot`, `u02_reuse_2::endpoint`, `u02_reuse_2::line`, `u02_reuse_2::pen_up` | identical |
| u02-enums-match/unshown | green: 4 passed; 0 failed | red: 0 passed; 2 failed | red: 0 passed; 4 failed | identical |
| u02-enums-match/probe-a/p1-tokens | green: 1 passed; 0 failed | red: 0 passed; 1 failed | red: 0 passed; 1 failed | identical |
| u02-enums-match/probe-a/p2-sign | green: 4 passed; 0 failed | red: no test result; build error[E0004]: non-exhaustive patterns: `Some(_)` not covered | red: no test result; build error[E0004]: non-exhaustive patterns: `Some(_)` not covered | identical |
| u02-enums-match/probe-a/p3-alert | green: 6 passed; 0 failed | red: 0 passed; 4 failed | red: 1 passed; 5 failed | identical |
| u03-result-question-mark/attempt | green: 13 passed; 0 failed | red: no test result; build error[E0432]: unresolved import `u03_attempt::explicit::parse_line` | red: no test result; build error[E0432]: unresolved import `u03_attempt::explicit::parse_line` | identical |
| u03-result-question-mark/reuse-1 | green: 9 passed; 0 failed | red: 0 passed; 3 failed | red: 0 passed; 9 failed | identical |
| u03-result-question-mark/reuse-2 | green: 8 passed; 0 failed | red: 0 passed; 4 failed | red: 0 passed; 8 failed | identical |
| u03-result-question-mark/unshown | green: 8 passed; 0 failed | red: no test result; build error[E0308]: mismatched types | red: no test result; build error[E0308]: mismatched types | identical |
| u03-result-question-mark/probe-a/p1-duration | green: 9 passed; 0 failed | red: 0 passed; 4 failed | red: 0 passed; 9 failed | identical |
| u03-result-question-mark/probe-a/p2-size | green: 7 passed; 0 failed | red: no test result; build error[E0277]: `?` couldn't convert the error to `SizeError` | red: no test result; build error[E0277]: `?` couldn't convert the error to `SizeError` | identical |
| u03-result-question-mark/probe-a/p3-average | green: 6 passed; 0 failed | red: 1 passed; 2 failed | red: 2 passed; 4 failed | identical |

| overlay | graded on key | expected |
|---|---|---|
| baseline/b1-own · clone the input to dodge the move | red: 4 passed; 1 failed | red |
| baseline/b1-own · follow the compiler: iterate by reference, push copies | red: 4 passed; 1 failed | red |
| baseline/b1-own · delete the use: count the kept words | red: 2 passed; 3 failed | red |
| baseline/b1-own · legit: retain in place, then split off the count | green: 5 passed; 0 failed | green |
| baseline/b2-life · follow the compiler: one lifetime on all three | red: no test result; build error[E0597]: `sep` does not live long enough | red |
| baseline/b2-life · return an owned String | red: no test result; build error[E0308]: mismatched types | red |
| baseline/b2-life · legit: lifetime only on line and the result, with 'b named | green: 5 passed; 0 failed | green |
| baseline/b3-result · legit: From impl plus question mark | green: 9 passed; 0 failed | green |
| baseline/b3-result · correct values, no question mark | red: 8 passed; 1 failed | red |
| baseline/b3-result · unwrap the parse | red: 4 passed; 5 failed | red |
| baseline/b4-traits · slice of trait objects, not generic | red: no test result; build error[E0308]: mismatched types | red |
| baseline/b4-traits · legit: impl Trait in argument position | green: 6 passed; 0 failed | green |
| baseline/b5-iter · eager model: all maps run before the filter | red: 0 passed; 1 failed | red |
| baseline/b5-iter · take keeps pulling after it has its one item | red: 0 passed; 1 failed | red |
| baseline/b6-enum · range 1..=3 read as including 0 | red: 0 passed; 1 failed | red |
| baseline/b6-enum · legit: right answer with trailing spaces and a final blank line | green: 1 passed; 0 failed | green |
| u01-own-move-borrow/probe-a/p2-summary · clone the lines for the callee | red: 4 passed; 1 failed | red |
| u01-own-move-borrow/probe-a/p2-summary · legit: count first, keep byte_total as written | green: 5 passed; 0 failed | green |
| u01-own-move-borrow/probe-a/p3-shift · legit: add borrows the offset | green: 5 passed; 0 failed | green |
| u01-own-move-borrow/probe-a/p3-shift · clone the offset each time | red: 4 passed; 1 failed | red |
| u01-own-move-borrow/reuse-1 · clone the vector to read the max | red: 5 passed; 1 failed | red |
| u01-own-move-borrow/reuse-1 · legit: copied() on the max | green: 6 passed; 0 failed | green |
| u01-own-move-borrow/reuse-2 · clone msg on every call | red: 4 passed; 1 failed | red |
| u01-own-move-borrow/unshown · take the compiler's borrow help, then copy | red: 4 passed; 1 failed | red |
| u01-own-move-borrow/unshown · legit: drain the vector | green: 5 passed; 0 failed | green |
| u01-own-move-borrow/unshown · legit: mem::replace with a new vector | green: 5 passed; 0 failed | green |
| u02-enums-match/probe-a/p1-tokens · guard on Num read as not matching -4 | red: 0 passed; 1 failed | red |
| u02-enums-match/probe-a/p2-sign · legit: last arm unguarded | green: 4 passed; 0 failed | green |
| u02-enums-match/probe-a/p2-sign · fill the gap with a panicking arm | red: 3 passed; 1 failed | red |
| u02-enums-match/reuse-1 · legit: guards in place of ranges | green: 6 passed; 0 failed | green |
| u02-enums-match/reuse-1 · group boundary off by one: more than 10 in place of 10 or more | red: 5 passed; 1 failed | red |
| u02-enums-match/reuse-1 · catch-all arm | red: 5 passed; 1 failed | red |
| u02-enums-match/unshown · two nested matches | red: 3 passed; 1 failed | red |
| u03-result-question-mark/probe-a/p2-size · one From impl for both parses | red: 5 passed; 2 failed | red |
| u03-result-question-mark/probe-a/p3-average · legit: manual index, explicit match | green: 6 passed; 0 failed | green |
| u03-result-question-mark/probe-a/p3-average · guard the empty case, keep the unwrap | red: 3 passed; 3 failed | red |
| u03-result-question-mark/reuse-1 · both parse errors mapped to BadX | red: 6 passed; 3 failed | red |
| u03-result-question-mark/unshown · map_err in place of From | red: 7 passed; 1 failed | red |

failures: 0

Hints:

```
u01-own-move-borrow: 4 problems, 12 hints
u02-enums-match: 4 problems, 12 hints
u03-result-question-mark: 4 problems, 12 hints
violations: 0
```

Totals: 27 problems (6 baseline, 7 per unit ×3). 27 keys green, 27 stubs red, 27 stubs red when graded, 27 lock sets identical. 38 overlays: 25 workarounds red, 13 legitimate alternatives green. 36 hints, 0 violations.

## Found during the check, for other pieces

1. **P6, probe.py, one crate per probe.** `probe-a/` is three standalone crates (`p1-*`, `p2-*`, `p3-*`), because a cargo workspace with one member that fails to compile prints no test result for any member (measured, cargo 1.91.1). `probe.py` takes one `crate_dir` and logs one row. It needs to loop over the three items and log one row each, which is what PLAN:89 already asks for.
2. **P6, probe.py, partial counts.** `run_cargo_test` calls `cargo test` without `--no-fail-fast`, so cargo stops at the first failing test binary and the continuous measure counts only part of the tests (measured: the u02 reuse-1 stub graded as 1 passed, 1 failed without the flag, and 1 passed, 5 failed with it).
3. **P6, grading needs the key.** Held-out tests live only in `key/`. Grading copies the learner's `Edit:` files into a copy of the key (README § Grading). `probe.py` refuses every `key/` path by design, so the grade step needs its own process that the learner and trainer cannot read. Open point for P6, default: a separate `grade.py` run after the probe window closes.
4. **P6, predict-output.** "No running before the prediction is submitted" (baseline.yaml forms) is not enforced by the crate. The runner has to withhold `cargo run` and `cargo test` until submission.
5. **Any grader, stale builds.** An earlier predict test read `prediction.txt` through the compile-time `env!("CARGO_MANIFEST_DIR")`. With a reused target dir and a copy that kept its mtimes, cargo judged the test fresh and read a deleted path, so a correct prediction graded red. Fixed: the tests read the file relative to the working directory, which `cargo test` sets to the package root. Re-checked with a reused target dir: wrong prediction red, right one green.
6. **P1 allowlist.** The allowlist grants `UNIT/attempt.md` but not `UNIT/attempt/**`, the attempt crate. The trainer sees the attempt only through the learner's copy under `training/rust/<unit>/`. That works if session.py copies `attempt/` there; otherwise it is an allowlist gap.
7. **Deviation from baseline.yaml.** The fix-the-compile-error pass rule says the locked test file is "checked by hash". The items lock it by grading on the key's copy instead, which gives the same guarantee without a hash list.

## Declared limits

- Time caps are the author's sizing, unmeasured. The blind solve by a fresh sonnet (PLAN:74) has not run.
- Hints are unreviewed. The fresh-opus hint check (PLAN:74) has not run. Three level-3 hints come closest to the answer and need the reviewer's eye first: u01 unshown (names the module std::mem), u02 unshown (names a tuple scrutinee), u03 unshown (names From::from).
- Source scans ban named methods only. A copy made through `.into()` or `String::from` passes the ban in u01 attempt, reuse-2 and probe-a p2. A heap-address test catches it where the output keeps the input's strings (b1, u01 attempt `drop_shorter_than_first`, u01 unshown), and nowhere else.
- Text scans also catch innocent text: `enum` in any comment of u02 attempt's `flat_form.rs` (so also `enumerate`), a comment containing `match ` in u02 unshown, a `?` in a comment of u03 attempt's `explicit.rs`. Each spec states its ban.
- u01 reuse-2: rustc's note under E0382 names the fix (change `deliver`'s parameter to borrow), so the item is easier than designed.
- u03 example: the quoted E0277 message names `From<ParseIntError>`, the unshown problem's component. The example never shows `From` in use.
- u02 unshown: two nested matches solve the logic and fail only the one-match rule. The rule forces the component; the transfer claim of N2-r1-06 is about solving, so this rule is a default, unmeasured.
- Attempts carry no held-out tests. They are practice, never scored for an axis (PLAN:96–97).
- Each unit's attempt asks for two approaches (rust.yaml forms.attempt-first, EV:239): u01 caller-side and callee-side fixes, u02 enum and flat struct, u03 explicit match and `?`.
- MAP concept files for these units hold names only (e.g. `maps/rust/concepts/ownership.yaml`, two lines). Items were authored from Rust semantics, as rust.yaml's u06 gap note already anticipates for thin units.

## Missing

- `probe-b/` for u01–u03: the second author writes these from the three specs.
- The P7 checks for P3 (PLAN:74): blind solve, hint review, isomorph check.

## Revision 1 · after P3-hint-review.md and P3-blind-solve.md

Revised by the drill author (opus, claude-opus-5-5), 2026-09-28. Builds ran only in `/private/tmp/gym-scratch/t-p3-author-a/`, on a copy of `training/rust/items/`. The first round ran cargo with `--manifest-path` against the item tree itself, which writes a `Cargo.lock` beside each manifest. Those files were deleted at the end of that round. Whether the stray `Cargo.lock` files the blind solve found under u01 probe-a came from that round or from the blind solve's subagent, the record does not show.

### Hints (P3-hint-review.md)

| finding | change |
|---|---|
| LEAKS u01 unshown L3 | Now states the invariant (the field holds a valid Vec at every moment, so the old one leaves only as something valid takes its place) and says std has a function for that exchange. It no longer names the module or the value to put in. |
| LEAKS u03 reuse-1 L3 | Now points at subgoal 3 of the example and asks the learner to compare what BadX and BadY take and give back. It no longer names map_err or the variant-as-function. |
| LEAKS u03 reuse-2 L3 | Now says checked_sub answers with an Option and the function with a Result, points at subgoal 3 of the example, and says both numbers are in scope. It no longer names ok_or or the step sequence. |
| USELESS u03 reuse-2 L2 | Now names subgoal 3 and the three routes into TxError (a parse, an own check, a subtraction). The reviewer's rewrite, "put the operator after the subtraction", names a change, which trainer.md rule 32(b) forbids, so it was not used. |
| wrong `?` rule, u03 attempt L3 | Now says `?` converts through the From trait, that nothing converts into LineError here, and that an Option is not a Result. It agrees with the u03 unshown ladder. |
| wrong subgoal, u01 attempt L2 | Now splits the misses: subgoal 3 for drop_shorter_than_first and caller_side, subgoal 2 for callee_side. |
| wrong subgoal, u03 reuse-1 L2 | Now subgoal 3: two parses of one std type become two variants. |
| missing ladder, u03 attempt explicit.rs | New problem key `attempt-explicit` (scope `src/explicit.rs`). The old ladder is renamed `attempt-propagate` (scope `src/propagate.rs`). |
| missing ladder, u02 reuse-2 i32 to u32 | New problem key `reuse-2-distance`: the compiler message at the cost line; subgoal 4; a negative difference does not fit a u32, and integer types have an unsigned-distance method. |
| borderline, u01 reuse-2 L3 | "A String lends itself as a &str" is removed. It now states only that an owned parameter takes the value on each call and that the parameter type decides take-or-borrow. |
| borderline, u03 unshown L3 | "ReadError::from is that same function" is removed. It now says a conversion trait has one method, with its signature in the docs and a body that is the fitting variant. The spec now names the two impls (below), so level 3 had to move off naming them. |

The reviewer's "unverified" compiler claims were checked in the first round's runs: u01 reuse-2's E0382 note does name the parameter change (quoted in the first round's declared limits); u01 unshown's E0507 helps are "consider borrowing here" and "consider cloning"; u03 unshown's visible test fails with E0308 mismatched types.

### Items (P3-blind-solve.md)

| finding | change |
|---|---|
| unenforced structural bans: u02 reuse-1, reuse-2, probe-a/p3-alert (and u02 unshown's one-match/no-if) | New visible, locked `tests/structure.rs` in each, which the grader runs as part of `cargo test`. It blanks comments and string and char literals, extracts every arm pattern of every `match`, and flags alternatives that are `_`, a bare binding, or anything not starting with a type or a path. It also counts `match` and `if` tokens. The scanner was tested first on known-good and known-bad sources, including nested matches, block bodies, guards, or-patterns, `{{` in format strings, and a `'}'` char literal. The duplicate scans in `heldout.rs` were removed. The specs now say `..` inside a variant's pattern is fine, and a bare catch-all binding is banned as well as `_`. |
| u01 probe-a/p3-shift: derive Copy skips the lesson | The spec now says `Point` stays as written, derives included, and must not become `Copy`. A new `tests/structure.rs` fails to compile if `Point` is `Copy`, through two blanket impls of a probe trait, one bounded on `Copy`. The key now borrows in `add`. A hand-written `impl Copy` is also caught. |
| u03 probe-a/p2-size: From detour | The spec now bans any `From` impl, and `tests/structure.rs` checks the source for the `From` token outside comments and literals. |
| u03 unshown: From impls unstated | The spec now says in prose: implement `From<Utf8Error>` and `From<ParseIntError>` for `ReadError`, so `?` converts each std error by itself. |
| probe-b specs | u01 p3 slot is now borrow-only with the not-Copy check; u02 now requires a visible structure check for structural rules; u03 p2 now bans `From`, checked in the source. |

### Rerun

```
cargo 1.91.1 (ea2d97820 2025-10-10)
rustc 1.91.1 (ed61e7d7e 2025-11-07)
2026-09-28T15:59
```

| problem | key `cargo test` | stub `cargo test` | stub graded on key | locked files |
|---|---|---|---|---|
| baseline/b1-own | green: 5 passed; 0 failed | red: no test result; build error[E0382]: borrow of moved value: `words` | red: no test result; build error[E0382]: borrow of moved value: `words` | identical |
| baseline/b2-life | green: 5 passed; 0 failed | red: no test result; build error[E0106]: missing lifetime specifier | red: no test result; build error[E0106]: missing lifetime specifier | identical |
| baseline/b3-result | green: 9 passed; 0 failed | red: 0 passed; 3 failed | red: 0 passed; 9 failed | identical |
| baseline/b4-traits | green: 6 passed; 0 failed | red: no test result; build error[E0432]: unresolved import `b4_traits::total_area` | red: no test result; build error[E0432]: unresolved import `b4_traits::total_area` | identical |
| baseline/b5-iter | green: 1 passed; 0 failed | red: 0 passed; 1 failed | red: 0 passed; 1 failed | identical |
| baseline/b6-enum | green: 1 passed; 0 failed | red: 0 passed; 1 failed | red: 0 passed; 1 failed | identical |
| u01-own-move-borrow/attempt | green: 6 passed; 0 failed | red: no test result; build error[E0382]: borrow of moved value: `names` | red: no test result; build error[E0382]: borrow of moved value: `names` | identical |
| u01-own-move-borrow/reuse-1 | green: 6 passed; 0 failed | red: no test result; build error[E0502]: cannot borrow `*scores` as mutable because it is also borrowed as immutable | red: no test result; build error[E0502]: cannot borrow `*scores` as mutable because it is also borrowed as immutable | identical |
| u01-own-move-borrow/reuse-2 | green: 5 passed; 0 failed | red: no test result; build error[E0382]: use of moved value: `msg` | red: no test result; build error[E0382]: use of moved value: `msg` | identical |
| u01-own-move-borrow/unshown | green: 5 passed; 0 failed | red: no test result; build error[E0507]: cannot move out of `self.pending` which is behind a mutable reference | red: no test result; build error[E0507]: cannot move out of `self.pending` which is behind a mutable reference | identical |
| u01-own-move-borrow/probe-a/p1-board | green: 4 passed; 0 failed | red: no test result; build error[E0502]: cannot borrow `self.scores` as mutable because it is also borrowed as immutable | red: no test result; build error[E0502]: cannot borrow `self.scores` as mutable because it is also borrowed as immutable | identical |
| u01-own-move-borrow/probe-a/p2-summary | green: 5 passed; 0 failed | red: no test result; build error[E0382]: borrow of moved value: `lines` | red: no test result; build error[E0382]: borrow of moved value: `lines` | identical |
| u01-own-move-borrow/probe-a/p3-shift | green: 6 passed; 0 failed | red: no test result; build error[E0382]: use of moved value: `offset` | red: no test result; build error[E0382]: use of moved value: `offset` | identical |
| u02-enums-match/attempt | green: 14 passed; 0 failed | red: no test result; build error[E0432]: unresolved imports `u02_attempt::enum_form::fault`, `u02_attempt::enum_form::fault_code`, `u02_attempt::enum_form::label`, `u02_attempt::enum_form::off`, `u02_attempt::enum_form::temp` | red: no test result; build error[E0432]: unresolved imports `u02_attempt::enum_form::fault`, `u02_attempt::enum_form::fault_code`, `u02_attempt::enum_form::label`, `u02_attempt::enum_form::off`, `u02_attempt::enum_form::temp` | identical |
| u02-enums-match/reuse-1 | green: 7 passed; 0 failed | red: 1 passed; 5 failed | red: 1 passed; 6 failed | identical |
| u02-enums-match/reuse-2 | green: 7 passed; 0 failed | red: no test result; build error[E0432]: unresolved imports `u02_reuse_2::cost`, `u02_reuse_2::dot`, `u02_reuse_2::endpoint`, `u02_reuse_2::line`, `u02_reuse_2::pen_up` | red: no test result; build error[E0432]: unresolved imports `u02_reuse_2::cost`, `u02_reuse_2::dot`, `u02_reuse_2::endpoint`, `u02_reuse_2::line`, `u02_reuse_2::pen_up` | identical |
| u02-enums-match/unshown | green: 4 passed; 0 failed | red: 0 passed; 3 failed | red: 0 passed; 4 failed | identical |
| u02-enums-match/probe-a/p1-tokens | green: 1 passed; 0 failed | red: 0 passed; 1 failed | red: 0 passed; 1 failed | identical |
| u02-enums-match/probe-a/p2-sign | green: 4 passed; 0 failed | red: no test result; build error[E0004]: non-exhaustive patterns: `Some(_)` not covered | red: no test result; build error[E0004]: non-exhaustive patterns: `Some(_)` not covered | identical |
| u02-enums-match/probe-a/p3-alert | green: 6 passed; 0 failed | red: 1 passed; 4 failed | red: 1 passed; 5 failed | identical |
| u03-result-question-mark/attempt | green: 13 passed; 0 failed | red: no test result; build error[E0432]: unresolved import `u03_attempt::explicit::parse_line` | red: no test result; build error[E0432]: unresolved import `u03_attempt::explicit::parse_line` | identical |
| u03-result-question-mark/reuse-1 | green: 9 passed; 0 failed | red: 0 passed; 3 failed | red: 0 passed; 9 failed | identical |
| u03-result-question-mark/reuse-2 | green: 8 passed; 0 failed | red: 0 passed; 4 failed | red: 0 passed; 8 failed | identical |
| u03-result-question-mark/unshown | green: 8 passed; 0 failed | red: no test result; build error[E0308]: mismatched types | red: no test result; build error[E0308]: mismatched types | identical |
| u03-result-question-mark/probe-a/p1-duration | green: 9 passed; 0 failed | red: 0 passed; 4 failed | red: 0 passed; 9 failed | identical |
| u03-result-question-mark/probe-a/p2-size | green: 8 passed; 0 failed | red: no test result; build error[E0277]: `?` couldn't convert the error to `SizeError` | red: no test result; build error[E0277]: `?` couldn't convert the error to `SizeError` | identical |
| u03-result-question-mark/probe-a/p3-average | green: 6 passed; 0 failed | red: 1 passed; 2 failed | red: 2 passed; 4 failed | identical |

| overlay | graded on key | expected |
|---|---|---|
| baseline/b1-own · clone the input to dodge the move | red: 4 passed; 1 failed | red |
| baseline/b1-own · follow the compiler: iterate by reference, push copies | red: 4 passed; 1 failed | red |
| baseline/b1-own · delete the use: count the kept words | red: 2 passed; 3 failed | red |
| baseline/b1-own · legit: retain in place, then split off the count | green: 5 passed; 0 failed | green |
| baseline/b2-life · follow the compiler: one lifetime on all three | red: no test result; build error[E0597]: `sep` does not live long enough | red |
| baseline/b2-life · return an owned String | red: no test result; build error[E0308]: mismatched types | red |
| baseline/b2-life · legit: lifetime only on line and the result, with 'b named | green: 5 passed; 0 failed | green |
| baseline/b3-result · legit: From impl plus question mark | green: 9 passed; 0 failed | green |
| baseline/b3-result · correct values, no question mark | red: 8 passed; 1 failed | red |
| baseline/b3-result · unwrap the parse | red: 4 passed; 5 failed | red |
| baseline/b4-traits · slice of trait objects, not generic | red: no test result; build error[E0308]: mismatched types | red |
| baseline/b4-traits · legit: impl Trait in argument position | green: 6 passed; 0 failed | green |
| baseline/b5-iter · eager model: all maps run before the filter | red: 0 passed; 1 failed | red |
| baseline/b5-iter · take keeps pulling after it has its one item | red: 0 passed; 1 failed | red |
| baseline/b6-enum · range 1..=3 read as including 0 | red: 0 passed; 1 failed | red |
| baseline/b6-enum · legit: right answer with trailing spaces and a final blank line | green: 1 passed; 0 failed | green |
| u01-own-move-borrow/probe-a/p2-summary · clone the lines for the callee | red: 4 passed; 1 failed | red |
| u01-own-move-borrow/probe-a/p2-summary · legit: count first, keep byte_total as written | green: 5 passed; 0 failed | green |
| u01-own-move-borrow/probe-a/p3-shift · legit: add borrows the offset | green: 6 passed; 0 failed | green |
| u01-own-move-borrow/probe-a/p3-shift · clone the offset each time | red: 5 passed; 1 failed | red |
| u01-own-move-borrow/probe-a/p3-shift · derive Copy on Point, helper untouched | red: no test result; build error[E0283]: type annotations needed | red |
| u01-own-move-borrow/probe-a/p3-shift · impl Copy by hand in place of the derive | red: no test result; build error[E0283]: type annotations needed | red |
| u01-own-move-borrow/reuse-1 · clone the vector to read the max | red: 5 passed; 1 failed | red |
| u01-own-move-borrow/reuse-1 · legit: copied() on the max | green: 6 passed; 0 failed | green |
| u01-own-move-borrow/reuse-2 · clone msg on every call | red: 4 passed; 1 failed | red |
| u01-own-move-borrow/unshown · take the compiler's borrow help, then copy | red: 4 passed; 1 failed | red |
| u01-own-move-borrow/unshown · legit: drain the vector | green: 5 passed; 0 failed | green |
| u01-own-move-borrow/unshown · legit: mem::replace with a new vector | green: 5 passed; 0 failed | green |
| u02-enums-match/probe-a/p1-tokens · guard on Num read as not matching -4 | red: 0 passed; 1 failed | red |
| u02-enums-match/probe-a/p2-sign · legit: last arm unguarded | green: 4 passed; 0 failed | green |
| u02-enums-match/probe-a/p2-sign · fill the gap with a panicking arm | red: 3 passed; 1 failed | red |
| u02-enums-match/probe-a/p3-alert · legit: guards and field patterns with .. | green: 6 passed; 0 failed | green |
| u02-enums-match/probe-a/p3-alert · wildcard arm for the quiet cases | red: 5 passed; 1 failed | red |
| u02-enums-match/reuse-1 · catch-all by a bare binding | red: 6 passed; 1 failed | red |
| u02-enums-match/reuse-1 · legit: guards in place of ranges | green: 7 passed; 0 failed | green |
| u02-enums-match/reuse-1 · right prices from an if chain, no match | red: 6 passed; 1 failed | red |
| u02-enums-match/reuse-1 · group boundary off by one: more than 10 in place of 10 or more | red: 6 passed; 1 failed | red |
| u02-enums-match/reuse-1 · wildcard written with odd spacing and a comment | red: 6 passed; 1 failed | red |
| u02-enums-match/reuse-1 · catch-all arm | red: 6 passed; 1 failed | red |
| u02-enums-match/reuse-2 · legit: variants brought in with use Command::* | green: 7 passed; 0 failed | green |
| u02-enums-match/reuse-2 · wildcard arm for pen_up in endpoint | red: 6 passed; 1 failed | red |
| u02-enums-match/unshown · one match, with an if inside an arm | red: 3 passed; 1 failed | red |
| u02-enums-match/unshown · two nested matches | red: 3 passed; 1 failed | red |
| u03-result-question-mark/probe-a/p2-size · one From impl for both parses | red: 5 passed; 3 failed | red |
| u03-result-question-mark/probe-a/p2-size · From detour with a width-only impl, height via map_err | red: 7 passed; 1 failed | red |
| u03-result-question-mark/probe-a/p3-average · legit: manual index, explicit match | green: 6 passed; 0 failed | green |
| u03-result-question-mark/probe-a/p3-average · guard the empty case, keep the unwrap | red: 3 passed; 3 failed | red |
| u03-result-question-mark/reuse-1 · both parse errors mapped to BadX | red: 6 passed; 3 failed | red |
| u03-result-question-mark/unshown · legit: the two From impls the spec names | green: 8 passed; 0 failed | green |
| u03-result-question-mark/unshown · map_err in place of From | red: 7 passed; 1 failed | red |

failures: 0

Hints:

```
u01-own-move-borrow: 4 problems, 12 hints
u02-enums-match: 5 problems, 15 hints
u03-result-question-mark: 5 problems, 15 hints
violations: 0
```

Totals: 27 problems, 27 keys green, 27 stubs red, 27 stubs red when graded on the key, 27 lock sets identical. 50 overlays: 34 workarounds red, 16 legitimate alternatives green. 14 ladders, 42 hint levels, 0 violations of the hint scan (which checks shape and key code only; it is not the reviewer's leak judgement). `find training/rust/items -name Cargo.lock -o -name target`: 0.

### Limits added or changed

- The structure scanner is a text scanner, not a parser. It flags a legitimate top-level binding such as `x @ Ticket::Staff` as a catch-all, and it would misread raw strings that contain quote characters. Neither appears in any key or overlay.
- A learner who reads the not-Copy compile error in u01 probe-a p3 sees E0283 "type annotations needed". The spec and the test's comment state what that error means.
- u03 unshown now names its component in the spec, so it tests writing the two `From` impls and using `?` through them, not finding `From`. Its transfer claim under N2-r1-06 is weaker for it.
- The first-round limit about text scans in u02 unshown catching a `match ` inside a comment no longer holds: the scanner skips comments. The `enum` ban in u02 attempt's `flat_form.rs` and the `?` ban in u03 attempt's `explicit.rs` are unchanged, still substring scans.
