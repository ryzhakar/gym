# u02-enums-match · probe-b spec

For the second author. Write `training/rust/items/u02-enums-match/probe-b/` and `key/probe-b/` from this file alone. Do not open the unit's `probe-a/`, `key/`, or any other item: the isomorph check (PLAN:74) is valid only if probe-b comes from the spec.

## Purpose

The delayed probe, run unaided at least 7 days after the unit's practice. It is isomorph b of the immediate probe (PLAN:17, PLAN:97; rust.yaml rules.spacing). A pass has to mean the learner still models cases as enum variants and writes and reads `match` correctly: never by remembering probe-a, and never without the mechanism.

## The unit's mechanism

Four subgoals, from the unit's worked example: name the cases (one variant per case, carrying only its data); cover every case (one arm per variant, with the compiler's non-exhaustive error listing what is missing); order arms from specific to general (the first match wins, and literals, ranges and guards come before the plain binding); bind what the arm uses (destructuring, `@` with a range, `..`). The example also states that a guard does not count toward exhaustiveness.

## Items

Matches are by value, on enums with owned or `Copy` data. No references in patterns: match ergonomics belongs to u01's cluster (rust.yaml u02 gap note).

| slot | form | what it must test | what the tests must enforce |
|---|---|---|---|
| p1 | predict-output | a `match` over a 4-variant enum (one variant carrying a `String`, one carrying nothing, one an integer, one a `char`), over about 9 values printed one per line. Must include: a guard on the first arm of a variant that catches some values, a literal arm after that guard, an `@` binding with an inclusive range, an or-pattern of two literals, a guard on a `String` field, and one value that falls through to the general arm of its variant | the predicted stdout equals the actual. At least three lines must differ between a reader who applies first-match-wins with guards correctly and one who does not, for example a negative value caught by a guard before a literal or range arm |
| p2 | fix-the-compile-error | E0004 caused only by guards: every value is logically covered, but the last arm of one variant is guarded, so the compiler reports that variant's general pattern as not covered | behaviour for every case locked by tests; a source scan bans `panic!`, `unreachable!`, `todo!`, `unimplemented!`, so a panicking filler arm fails; signature locked; held-out tests at the integer extremes |
| p3 | write-to-tests | a function from a given 4-variant enum (one struct-like variant with two fields, one of them a `bool`) to `Option<String>`. The rules need: two range thresholds on one variant, one threshold on another, a boolean field that overrides a threshold, and one variant that always alerts | visible tests cover each rule once, held-out tests cover every boundary value on both sides, and a source scan bans a `_` arm (the textual forms of an underscore wildcard followed by `=>`) |

Difficulty: about 3 minutes each for a learner who has the mechanism. p1 is read without the compiler. p2's fix is at most 2 changed lines. p3 is about 8 to 10 arms.

## Surfaces already used in this unit: do not reuse

Sensor readings as temperature, fault and off; window input events (key, click, scroll, close); ticket pricing (adult, child, group, staff); plotter commands (dot, line, pen up); a door state machine; lexer tokens (number, operator, word, end); signs of an optional integer; sensor status alerts (temperature, humidity, battery, missing); robot commands (move, wait, say, quit). Pick new domains, such as parcel sizes, chess-clock events, or HTTP-like status classes.

## Conventions

- Each item is a standalone cargo crate at `probe-b/p<n>-<slug>/`: edition 2021, std only, its own empty `[workspace]` table, package name `u02-probe-b-p<n>`.
- `spec.md` in each crate: a title line, exactly one `Edit:` line naming the learner's files, the rules as bullets, then `Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.`
- `tests/visible.rs`, locked. `key/probe-b/p<n>-<slug>/` is the full crate: the reference solution, a byte-identical `tests/visible.rs`, and `tests/heldout.rs`.
- Predict-output: `src/main.rs`; an empty `prediction.txt` in the stub and the exact stdout in the key's copy; one test that runs the binary through the `CARGO_BIN_EXE_<package name>` environment variable, compares after trimming trailing whitespace per line and at the end, and never prints the actual output.
- Grading copies the learner's `Edit:` files into a copy of the key and runs `cargo test`.
- Structural rules (no `_` arm, every arm names its variant, one `match`, no `if`) are checked in a visible, locked `tests/structure.rs` that the spec names. The check reads the source with comments and string and char literals blanked, extracts each arm's pattern, and flags any alternative that is `_`, a bare binding, or anything not starting with a type or path. `..` inside a variant's pattern stays allowed, and the spec says so.
- A signature lock is a held-out test that assigns the function to a function-pointer type written out in full.
- No hints: probes are unaided (PLAN:50).

## Isomorph, not copy

Same form per slot, same pattern features, same count of arms within about two. New enum, variants, domain and values. Copying probe-a's key into probe-b must fail to compile against probe-b's tests, and probe-a's prediction must not equal probe-b's output.

## Acceptance before handing back

1. Key `cargo test --no-fail-fast` green. Stub red. Stub files graded on the key red.
2. Workarounds written out and graded, red: for p2, a panicking filler arm and a `_` arm returning a wrong answer; for p3, a `_` arm, and an off-by-one at each threshold. At least one legitimate alternative, green: guards in place of ranges, for example.
3. For p1, three wrong predictions written out, each from a different misreading (guard ignored, range bounds off by one, a later arm taken over an earlier one): each graded red.
4. The results go in `trainer/checks/P3-probe-b-selfcheck.md`, in the table shape of `P3-selfcheck.md`. The isomorph check itself is run by a fresh sonnet (PLAN:74), not by the author.
