# u03-result-question-mark · probe-b spec, revision 2

For the second author. Rewrite `training/rust/items/u03-result-question-mark/probe-b/` and `key/probe-b/` from this file alone. The existing probe-b items fail the isomorph check (`trainer/checks/P3-isomorph.md`): a rename-only port of probe-a's key passes all three, and p2 lacks the `From` source check. Replace them. Do not open the unit's `probe-a/`, its `key/`, or any other item, except the one file this spec names under "Bans".

## Purpose

The delayed probe, run unaided at least 7 days after the unit's practice. It is isomorph b of the immediate probe (PLAN:17, PLAN:97; rust.yaml rules.spacing). A pass has to mean the learner still turns fallible steps into one error type and propagates them with `?`, without panicking on input. That rules out recalling probe-a's answer, and it rules out passing without the mechanism.

## The rule that decides every slot

**Same Concept, same move, different structure.** Each slot below names the structural difference, drawn from data shape, return type, ownership direction and call site. That difference must be fixed in probe-b's locked signature, its given types, or its visible tests, so that probe-a's solution body, with every identifier renamed, does not compile against probe-b's tests or fails one of them. Changing a constant, a separator or a suffix is a rename, not a structural difference. The previous probe-b items differed from probe-a only in those, and they failed the check. The descriptions of probe-a below are at the level of types and moves only.

## The unit's mechanism

Four subgoals, from the unit's worked example. List the fallible steps: each call returning a `Result` or an `Option`, with its error type, plus the function's own checks. Pick the function's error type: an enum with a variant for each failure the caller must tell apart. Convert each failure into that type: `map_err` on a `Result`, `ok_or` on an `Option`, an early `Err` return for an own check. Propagate with `?` and return `Ok` at the end, with no `unwrap`, `expect` or `panic!` on paths the input controls.

The error enum and every output type are given in each stub and stay as written. Loops are plain `for` loops. No iterator adapter is needed beyond what a `for` loop and a counter can do, since u06 is a later unit.

## Items

### p1 · write-to-tests, three kinds of fallible step

- Same move: an `Option` from a std string method, a `Result<_, ParseIntError>` from a parse, and an `Option` from a checked integer operation, each converted into a 3-variant error enum, one variant carrying the `ParseIntError`.
- probe-a's shape: one text argument; the string step removes a suffix; one parse; a checked multiplication by a constant; the result is a bare integer.
- **Required differences: call site (signature), data shape and return type.** The function takes a second, numeric argument, and the checked operation combines the parsed number with that argument. Use an operation other than multiplication, such as a checked add or a checked subtraction, so that both overflow directions matter. The string step splits the text or removes a prefix, not a suffix. The success value is a given struct with two named fields, one of them the parsed number and the other the checked result.
- Tests enforce: every error variant reached by a visible test; held-out tests at the edges of the numeric types (the largest value that succeeds, the first that fails), with empty input, and with the prefix or separator alone; the panic scan.

### p2 · fix-the-compile-error, two parses of one std error type

- Same move: `?` is applied directly to two parses whose std error type is the same, and the two must map to two different variants of the function's error enum. The fix is a conversion per step, 2 changed lines.
- probe-a's shape: one text split into two parts, both parsed to the same integer type, and the success value is one integer computed from both.
- **Required differences: data shape and return type.** The two parses target two different integer types that share `ParseIntError`, for example a `u8` and a `u16`. One of the two texts comes from a second function argument, not from splitting the first. The success value is a given struct holding both parsed values as their own types, not a number computed from them.
- Tests enforce: behaviour locked so that a single `From` impl, which maps both parses to one variant, fails a test; the `From` source check under "Bans"; signature locked; the panic scan; held-out cases where the first failing step is the one reported.

### p3 · write-to-tests, replace the panics

- Same move: a stub that works on good input but panics on bad input. It calls `unwrap` inside a loop, and it panics on empty input through an index. The learner returns an error for the empty case and for the first bad element, with that element's position.
- probe-a's shape: the input is a slice of string slices; the stub panics on empty through a division; the success value is one aggregate integer.
- **Required differences: data shape and return type.** The input is a single delimited string that the function splits itself, so the position counts fields of the split. The stub seeds its running values from the first field by indexing, which is where it panics on empty input. The success value is a given struct or tuple of two aggregates computed in one pass, such as the smallest and largest value.
- Tests enforce: the happy path passes on the stub and the error cases fail on it; held-out cases with the bad field first, last, and as the only field, and with an empty field between two separators; the panic scan.

Difficulty: about 3 minutes each for a learner who has the mechanism. p2's fix is at most 2 changed lines. p1 and p3 each have at most about 10 lines of body.

## Bans probe-a enforces, carried over

- **`From` source check (p2).** The item's spec bans any `From` impl in `src/lib.rs`. A visible, locked `tests/structure.rs` checks it. Build that file from the scanner at `/Users/ryzhakar/pp/gym/training/rust/items/u02-enums-match/reuse-1/tests/structure.rs`: copy lines 1 to 165 verbatim, everything above the line that starts `const SRC`. That part is the scanner and nothing else, and reuse-1's own tests below it are not yours. Then write your own test asserting that `count_word` finds no `From` token in `src/lib.rs`. The scanner blanks comments and string and char literals, so a comment mentioning `From` does not trip it.
- **Panic scan (every slot).** A source scan bans `unwrap`, `expect`, `panic!`, `unreachable!` and `todo!`. The spec states the ban.
- **The key obeys every ban.** Run the structure test and the scans against the key.

## Surfaces already used: do not reuse

`name=count` config lines; `HH:MM` times; `x,y` points; withdrawals from a balance; UTF-8 sensor bytes; durations with an `s` or `m` suffix; `WxH` sizes; averages of number strings; `host:port` addresses. The previous probe-b domains (sizes in KiB, integer ranges, hex colour channels) may be kept only if the slot's required differences are met.

## Conventions

- Each item is a standalone cargo crate at `probe-b/p<n>-<slug>/`: edition 2021, std only, its own empty `[workspace]` table, package name `u03-probe-b-p<n>`.
- `spec.md` in each crate: a title line, exactly one `Edit:` line, the rules as bullets naming every locked test file, then `Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.`
- Locked test files are byte-identical in the stub and in `key/probe-b/p<n>-<slug>/`. The key adds `tests/heldout.rs`.
- Tests that compare against a specific `ParseIntError` build it by parsing the same text in the test and taking the error branch through a `match`.
- Grading copies the learner's `Edit:` files into a copy of the key and runs `cargo test`.
- A signature lock is a held-out test that assigns the function to a function-pointer type written out in full.
- Build only in scratch, never in the item tree.
- No hints: probes are unaided (PLAN:50).

## Acceptance before handing back

1. Key `cargo test --no-fail-fast` green. Stub red. Stub files graded on the key red.
2. For each slot, write down the required difference, and point to the locked signature, given type, or visible test that fixes it in place.
3. Workarounds written out and graded, red: an `unwrap` kept on one step; values right but one step reported under the wrong variant; for p2, one `From` impl (it must fail the structure test); for p3, guarding only the empty case. At least one legitimate alternative graded green, for example for p3 an explicit `match` with an early return in place of `map_err` and `?`.
4. Results go in `trainer/checks/P3-probe-b-selfcheck.md`. The isomorph check is rerun by a fresh sonnet (PLAN:74), not by the author.
