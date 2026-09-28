# u03-result-question-mark · probe-b spec

For the second author. Write `training/rust/items/u03-result-question-mark/probe-b/` and `key/probe-b/` from this file alone. Do not open the unit's `probe-a/`, `key/`, or any other item: the isomorph check (PLAN:74) is valid only if probe-b comes from the spec.

## Purpose

The delayed probe, run unaided at least 7 days after the unit's practice. It is isomorph b of the immediate probe (PLAN:17, PLAN:97; rust.yaml rules.spacing). A pass has to mean the learner still turns fallible steps into one error type and propagates with `?`, without panicking on input: never by remembering probe-a, and never without the mechanism.

## The unit's mechanism

Four subgoals, from the unit's worked example: list the fallible steps (each call returning a `Result` or an `Option`, with its error type, plus the function's own checks); pick the function's error type (an enum with a variant per failure the caller must tell apart); convert each failure into that type (`map_err` on a `Result`, `ok_or` on an `Option`, an early `Err` return for an own check); propagate with `?` and return `Ok` at the end, with no `unwrap`, `expect` or `panic!` on input-controlled paths. The unit's unshown problem added conversion through `From` impls, and probe-b does not require it.

## Items

The error enum is given in every item and stays as written. Loops are plain `for` loops; no iterator adapter beyond what a `for` loop and a counter can do (u06 is a later unit). `enumerate` is allowed but must not be needed.

| slot | form | what it must test | what the tests must enforce |
|---|---|---|---|
| p1 | write-to-tests | parse a short text through three fallible steps of different kinds: one `Option` from a std string method, one `Result<_, ParseIntError>` from a parse, and one `Option` from a checked integer operation, into a 3-variant enum where one variant carries the `ParseIntError` | every variant reached by a visible test; held-out tests at the edges of the numeric type (the largest value that succeeds, the smallest that overflows), empty input, and the unit or separator alone; a source scan bans `unwrap`, `expect`, `panic!`, `unreachable!`, `todo!` |
| p2 | fix-the-compile-error | E0277 "`?` couldn't convert the error": a function returning `Result<_, OwnError>` applies `?` directly to two parses of the same std error type that must map to two different variants | behaviour locked so that a single `From` impl, which maps both parses to one variant, fails a test; the spec bans any `From` impl and a visible, locked `tests/structure.rs` checks the source for the `From` token outside comments and literals, so the learner never spends the probe on that dead end; signature locked; the no-panic scan as in p1; held-out cases where the first failing step must be the one reported |
| p3 | write-to-tests (replace panics) | a stub that works on good input but calls `unwrap` inside a loop and divides or indexes in a way that panics on empty input. The learner returns an error for the empty case and for the first bad element, with that element's position | the happy path passes on the stub, the error cases fail on it; held-out cases with the bad element first, last, and at the only position; the no-panic scan |

Difficulty: about 3 minutes each for a learner who has the mechanism. p2's fix is at most 2 changed lines. p1 and p3 are each at most about 8 lines of body.

## Surfaces already used in this unit: do not reuse

`name=count` config lines; `HH:MM` clock times; `x,y` points; bank withdrawals with a balance; UTF-8 sensor bytes; durations with an `s` or `m` suffix; `WxH` sizes and their area; the integer average of number strings; `host:port` addresses. Pick new domains, such as semantic-version triples, RGB triplets, ranges written `lo..hi`, or seat codes like `B12`.

## Conventions

- Each item is a standalone cargo crate at `probe-b/p<n>-<slug>/`: edition 2021, std only, its own empty `[workspace]` table, package name `u03-probe-b-p<n>`.
- `spec.md` in each crate: a title line, exactly one `Edit:` line naming the learner's files, the rules as bullets, then `Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.`
- `tests/visible.rs`, locked. `key/probe-b/p<n>-<slug>/` is the full crate: the reference solution, a byte-identical `tests/visible.rs`, and `tests/heldout.rs`.
- Tests that compare against a specific `ParseIntError` build it by parsing the same text in the test and taking its error branch through a `match`, never with a bare literal.
- Grading copies the learner's `Edit:` files into a copy of the key and runs `cargo test`.
- A signature lock is a held-out test that assigns the function to a function-pointer type written out in full.
- No hints: probes are unaided (PLAN:50).

## Isomorph, not copy

Same form per slot, the same kinds of fallible step in the same number, and the same size of error enum. New function, types, domain and inputs. Copying probe-a's key into probe-b must fail to compile against probe-b's tests.

## Acceptance before handing back

1. Key `cargo test --no-fail-fast` green. Stub red. Stub files graded on the key red.
2. Workarounds written out and graded, red: an `unwrap` kept on one step; a `match` that returns the right values but reports the wrong variant for one step; for p2, one `From` impl in place of two `map_err`; for p3, guarding only the empty case. At least one legitimate alternative, green: for p3, an explicit `match` with an early return in place of `map_err` and `?`, for example.
3. The results go in `trainer/checks/P3-probe-b-selfcheck.md`, in the table shape of `P3-selfcheck.md`. The isomorph check itself is run by a fresh sonnet (PLAN:74), not by the author.
