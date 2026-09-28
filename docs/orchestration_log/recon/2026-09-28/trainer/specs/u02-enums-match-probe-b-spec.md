# u02-enums-match · probe-b spec, revision 2

For the second author. Rewrite `training/rust/items/u02-enums-match/probe-b/` and `key/probe-b/` from this file alone. The existing probe-b items fail the isomorph check (`trainer/checks/P3-isomorph.md`). A rename-only port of probe-a's key passes p2 and p3, and p3 has no real structure check, so a bound catch-all gets through. Replace them. Do not open the unit's `probe-a/`, its `key/`, or any other item, except the one file this spec names under "Bans".

## Purpose

The delayed probe, run unaided at least 7 days after the unit's practice. It is isomorph b of the immediate probe (PLAN:17, PLAN:97; rust.yaml rules.spacing). A pass has to mean the learner still models cases as enum variants and writes and reads `match` correctly. That rules out recalling probe-a's answer, and it rules out passing without the mechanism.

## The rule that decides every slot

**Same Concept, same move, different structure.** Each slot below names the structural difference, drawn from data shape, return type, ownership direction and call site. That difference must be fixed in probe-b's locked signature, its given enum, or its visible tests, so that probe-a's solution body, with every identifier renamed, does not compile against probe-b's tests or fails one of them. For p1, which has no learner code, the rule applies to the prediction instead: probe-a's output lines, renamed, must not be probe-b's output. The descriptions of probe-a below are at the level of types and moves only.

## The unit's mechanism

Four subgoals, from the unit's worked example. Name the cases: one variant per case, carrying only its data. Cover every case: one arm per variant, and the compiler's non-exhaustive error lists what is missing. Order arms from specific to general: the first match wins, and literals, ranges and guards come before the plain binding. Bind what the arm uses: destructuring, `@` with a range, `..`. A guard does not count toward exhaustiveness.

Matches are by value, on enums with owned or `Copy` data. No references in patterns, since match ergonomics belongs to u01's cluster (rust.yaml u02 gap note).

## Items

### p1 · predict-output

- Same move: trace first-match-wins through guards, literals, `@` ranges and an or-pattern, and find the fall-through to a variant's general arm.
- probe-a's shape: a 4-variant enum whose variants are all tuple-like or unit (one integer, one `char`, one `String`, one empty), about 9 values, one line printed per value.
- **Required difference: data shape.** At least one struct-like variant with two named fields, where one arm is a nested pattern that tests one field against a literal and binds the other. At least one arm whose guard compares two bound fields to each other. Keep an `@` range, an or-pattern of two literals, a guard on a `String` field, and one fall-through. About 9 values.
- Tests enforce: the predicted stdout equals the actual. At least three lines must differ between a reader who applies first-match-wins with guards correctly and one who does not.

### p2 · fix-the-compile-error, E0004 from guards only

- Same move: every value is covered logically, but the last arm of one variant carries a guard, so the compiler reports that variant as not covered. The learner makes the covering arm unguarded.
- probe-a's shape: the scrutinee is an `Option` of an integer, the three guards compare that integer to zero, and the function returns a `String`.
- **Required differences: data shape and return type.** The scrutinee is a crate enum with a struct-like variant of two integer fields, and the three guards compare the two fields to each other (less, equal, greater). The function returns another crate enum, given in the stub and locked, not a `String`. A second variant keeps the match from being a single-variant match.
- Tests enforce: behaviour for every case; a source scan bans `panic!`, `unreachable!`, `todo!` and `unimplemented!`, so a panicking filler arm fails; signature locked; held-out tests at the integer extremes, and with equal fields at both extremes.

### p3 · write-to-tests, no catch-all

- Same move: write one `match` whose arms cover a given enum. The arms need range thresholds, a boolean field that overrides a threshold, and a variant that always answers the same way, with every arm naming its variant.
- probe-a's shape: a flat 4-variant enum (tuple-like and one struct-like with an integer and a `bool`), mapped to `Option<String>`.
- **Required differences: return type and data shape.** The function returns a crate enum with three variants, one of them carrying data (for example a level with a number), given in the stub and locked, not an `Option<String>`. One variant of the input enum carries a second crate enum as a field, so that some arms need a nested pattern naming the inner variant. Keep two range thresholds on one variant and a `bool` override.
- Tests enforce: visible tests cover each rule once, and held-out tests cover every boundary on both sides; the structure check under "Bans".

Difficulty: about 3 minutes each for a learner who has the mechanism. p1 is read without the compiler. p2's fix is at most 2 changed lines. p3 is about 8 to 12 arms.

## Bans probe-a enforces, carried over

- **Bound catch-all and `_` scan (p3).** A visible, locked `tests/structure.rs` built from the scanner at `/Users/ryzhakar/pp/gym/training/rust/items/u02-enums-match/reuse-1/tests/structure.rs`. Copy lines 1 to 165 verbatim, everything above the line that starts `const SRC`. That part is the scanner and nothing else, and reuse-1's own tests below it are not yours. Then write your own test that asserts `arms_not_naming_a_variant` returns nothing for `src/lib.rs`. The scanner blanks comments and string and char literals, and flags any arm alternative that is `_`, a bare binding, or anything not starting with a type or a path. A text search for `_` before `=>` is not enough: the isomorph check passed a bound catch-all through exactly that search.
- **Panic scan (p2)** as listed there.
- The spec of each item states its rules, including that `..` inside a variant's pattern is fine, and names every locked test file.
- **The key obeys every ban.** Run the structure test against the key.

## Surfaces already used: do not reuse

Sensor readings as temperature, fault and off; window input events; ticket pricing; plotter commands; door states; lexer tokens; signs of an optional integer; sensor status alerts; robot commands. The previous probe-b domains (clock logs, response status classes, parcel alerts) may be kept only if the slot's required differences are met.

## Conventions

- Each item is a standalone cargo crate at `probe-b/p<n>-<slug>/`: edition 2021, std only, its own empty `[workspace]` table, package name `u02-probe-b-p<n>`.
- `spec.md` in each crate: a title line, exactly one `Edit:` line, the rules as bullets, then `Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.`
- Locked test files are byte-identical in the stub and in `key/probe-b/p<n>-<slug>/`. The key adds `tests/heldout.rs`.
- Predict-output: `src/main.rs`; an empty `prediction.txt` in the stub and the exact stdout in the key's copy; one test that runs the binary through the `CARGO_BIN_EXE_<package name>` environment variable, reads `prediction.txt` relative to the working directory (never through a compile-time manifest path), compares after trimming trailing whitespace per line and at the end, and never prints the actual output.
- Grading copies the learner's `Edit:` files into a copy of the key and runs `cargo test`.
- A signature lock is a held-out test that assigns the function to a function-pointer type written out in full.
- Build only in scratch, never in the item tree.
- No hints: probes are unaided (PLAN:50).

## Acceptance before handing back

1. Key `cargo test --no-fail-fast` green. Stub red. Stub files graded on the key red.
2. For each slot, write down the required difference, and point to the locked signature, given enum, or visible test that fixes it in place.
3. Workarounds written out and graded, red. For p2: a panicking filler arm, and a wrong-answer fix. For p3: a `_` arm, a bound catch-all under any name, a catch-all hidden inside a nested `match`, and an off-by-one at each threshold. At least one legitimate alternative graded green, for example guards in place of ranges.
4. For p1, three wrong predictions written out, each from a different misreading (guard ignored, range bounds off by one, a later arm taken over an earlier one), each graded red.
5. Results go in `trainer/checks/P3-probe-b-selfcheck.md`. The isomorph check is rerun by a fresh sonnet (PLAN:74), not by the author.
