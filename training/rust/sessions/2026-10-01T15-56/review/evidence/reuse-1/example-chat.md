# u02 attempt · instruction record

What was said in conversation after the attempt, 2026-10-01. Worked example: `example.md`, window events.

Attempt: `enum_form.rs` written, `label` thresholds swapped (below 0 gave hot, 30 and up gave freezing); `flat_form.rs` not written; last save 16.65 min after start, cap 10.

## Subgoal 1 · name the cases
Question: code reads `x` off a key press, flat struct vs enum, does it compile.
Learner: a struct with all fields required cannot be built; fields would need to be Option; the enum needs match first, then field access.
Fact: flat struct builds (constructor fills dummies), `e.x` compiles and returns the dummy. Option fields compile too; the check moves to run time. Enum: E0609, right.

## Subgoal 2 · cover every case
Question: match with no `Close` arm and no `_` arm. Learner: non-exhaustive, right (E0004).
Question: add `Stale(u8)` to `Reading`; which of `label` and `fault_code` stops compiling, what does the other return. Learner: `label` stops; `fault_code` returns None. Right.
Point: `_ => None` decided the answer for `Stale`; naming `Temperature(_) | Off` forces the decision.

## Subgoal 3 · order arms from specific to general
Question: `Key(c)` before `Key('q')`. Learner: compiles, `q` gets the generic arm. Right (warning: unreachable pattern).
Point: the if-chain inside one arm gets no unreachable check; separate range or guard arms do.

## Subgoal 4 · bind what the arm uses
Question: `Scroll(1..=3)` body prints `{d}`. Learner: does not compile, variable not in scope. Right (E0425).
Point: `Scroll(d @ 1..=3)` tests the range and keeps the value. A guard arm `Click { x, y } if x == y` binds both fields and the guard reads them. A guarded arm does not count toward exhaustiveness.

## reuse-1 · instruction after the failed attempt
Attempt: arms wrote `Adult(age: (0..=65))`, `Adult{_}` and `Child(age: ..3)` for variants declared with braces; parse error, no test ran.
Principle: a pattern copies the shape of the variant's declaration.
Question: `enum Event { Click { x: i32, y: i32 }, Scroll(i32) }`; which compile: `Click(x, y)`, `Click { x, y }`, `Scroll { d }`, `Scroll(d)`. Learner: `Click { x, y }` and `Scroll(d)`. Right.
Facts, checked by compiling: `Click(x, y)` is E0164, a struct variant written as tuple. `Scroll { d }` is E0769, a tuple variant written as struct.
Shapes: named fields take braces and `name: pattern` per field, with `..` for the rest, as in `Click { x: 0, y: 0 }`. Tuple variants take parentheses and a pattern per position, as in `Scroll(d @ 1..=3)` or `Scroll(1..=3)`.
