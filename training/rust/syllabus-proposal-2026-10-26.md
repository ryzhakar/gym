# Rust syllabus proposal, 2026-10-26

Trainer (trainer-u3), on the manager's summons of 2026-10-26 (recon/2026-10-26/gm/summons-syllabus.md). Inputs: grievances report and probe-transfer report (same dir), `gym train status training/rust`, every non-key spec under items/u01..u03, all attempt and probe-item events of the four sessions, curriculum draft recon/2026-09-28/trainer/curriculum/rust.yaml. No key/ path read.

## Item types in the bank today

| unit | practice items | probe items |
|---|---|---|
| u01 | fix ×4 (attempt, reuse-1, reuse-2, unshown) | probe-a fix ×3; probe-b write ×3; probe-c fix ×3 |
| u02 | write ×4 | predict, fix, write (both sides) |
| u03 | write ×5 | probe-a write, fix, refactor; probe-b write ×3 |

Every unit's practice holds one type. Probes test types the practice never drilled (u02's predict, u03's fix and refactor).

## #23 Consecutive items cannot differ in type

Change: each unit's practice holds at least three types (write, fix, predict; refactor where it fits), ordered so no two consecutive items share one. New units are authored that way from the start. Existing units get one predict and, for u02/u03, one fix item each.

Items added:
- u03 reuse-4 · predict: a `?` chain with two failing steps; the learner writes which `Err` comes out for four inputs. Drills early return order.
- u03 reuse-5 · fix: a function returning `Result` that uses `?` on an `Option` (E0277) and on an error with no `From` impl.
- u01 reuse-3 · predict: a `Vec` mutated and read in different orders (`insert(0, …)` then `first()`, `push` then `last()`, `take` then reading the source). See #30.
- u02 reuse-3 · predict: overlapping arms, a guard, an `@` binding with a range; the learner writes which arm fires. See #30.
- u02 reuse-4 · fix: a non-exhaustive match and an unreachable arm.

## #30 Revisits target evaluation order, which no item drills

Both delayed-probe failures on 2026-10-26 were order faults, not faults of the unit's construct: u01 p1 read the row's front after inserting into it; u02 p1 missed that the first matching arm wins and how `t @ -3..=-1` binds. The u01 reuse-3 and u02 reuse-3 predict items above are the drill. The 2026-11-02 revisits run them, then one fix or write item of the unit. Each revisit queues a fresh delayed probe at least 7 days later, on a side the learner has not seen: u01 probe-c (exists), u02 probe-c (to write, with one order-trace problem).

## #25 Caps too tight

The learner's own passing times, by type (minutes):

| type | practice passes | probe passes |
|---|---|---|
| fix, one file | 4.95, 2.68 (u01) | 1.50, 1.33, 2.38 (u01 a) |
| write, one function | 6.82, 10.05, 6.30 (u03); 25.43 (u02 reuse-2, after two fails) | about 2.3, 2.3, 1.1 (u01 b, from cumulative figures); 4.12, about 12.4 (u02 b) |
| predict | none practised | 3.25 to save (u02 b, failed 8 of 10 lines) |
| two-file attempt | 9.62 (u01, fix); 15.4 (u02 redo), 16.22 (u03 redo) | n/a |

New caps, written as a `Cap:` line in every spec (recorded, never a stop, per items README):
- Attempt: one file, one form, cap 10. u02 and u03 attempts keep their two files and take cap 20, since both second passes ran 15 to 16. Units from u04 on author single-file attempts.
- Practice: fix 5, predict 5, write 10, refactor 10.
- Probe problems: fix 3, predict 4, write 6, refactor 6. Each probe spec drops "10 minutes for p1, p2 and p3 together" for its own `Cap:` line, so `over_cap` reads per problem. Values for u03 probe-a: p1 6, p2 3 (fix; 6 if rewritten to write, below), p3 6. These supersede any value in the train-fixes branch.

Basis: cap = about the learner's slower passing time of that type, so it marks a slow pass and does not set the target. Thin evidence: 2 to 4 passes per type. Re-derive after u04.

## #26 No compile-stage rung

Change: every hints.yaml gains a unit-level `compile:` ladder, used first whenever the build is red, before the problem's own ladder:
1. Run `cargo check` and read only the first error: its code, the line it names, and its label.
2. Run `rustc --explain <code>`. Which type does the compiler say it expected at that spot, and which did your code give?
3. The fix makes the expected and given types meet at that spot, either by changing what the code gives or by converting it there. Every other error is ignored until this one is gone.

No level names a change or carries code.

## #24 u03 probe-a measures recall on p2 and p3

Adopt the transfer report's smallest fixes before the probe runs:
- p1-duration: unchanged (shallow transfer).
- p2-dose-admin: rewrite. Look up the dose by drug name (`Option` from a slice lookup, absent gives `UnknownDrug`). Drop the sentence naming `checked_sub`. Seed `?` on that `Option` (E0277). Swap the bad-number test for an unknown-drug one. Retitle from "u03 replacement r3 · fix the compile error" to "u03 probe-a p2 · fix the compile error". Also retitle u02 probe-a p2 from "replacement r1".
- p3-average: each element becomes `label=number`, add `NoEquals { index }`, and change the visible tests as the report says.
- Keys and held-out tests are written by an authoring agent and checked by a blind solve; the trainer never opens them.

## Unit order

1. 2026-10-27, u03 resume: reuse-3 (write), reuse-4 (predict, new), reuse-5 (fix, new), one confidence rating, immediate probe-a (p2/p3 rewritten). Queue the u03 delayed probe-b 7 days later, and re-queue the open `revisit` row as `resume` once that kind lands.
2. u04-lifetimes, next unit per the curriculum draft. Its baseline b2-life failed (0.73 min), so the learner is a novice in it: attempt, then a subgoal-labelled worked example walked in conversation. Its attempt is a fix item, a different type from u03's write. The items need writing, 3 types, single-file attempt, caps above, compile ladder.
3. 2026-11-02, u01 and u02 revisits (#30), each followed by a queued delayed probe on probe-c 7 days or more later.
4. u05 generics-traits, u06 closures-iterators, u07 shared-ownership, u08 trait objects, then judgment units u09 to u12, per the curriculum draft. Each unit's revisits run at 7, 30 and 90 days.

## Authoring work this needs, in order of need

1. For 2026-10-27: u03 reuse-4 and reuse-5, the rewrites of probe-a p2 and p3, `Cap:` lines on u03, and the u03 compile ladder.
2. Before u04 starts: the full u04 bank.
3. Before 2026-11-02: u01 reuse-3, u02 reuse-3 and reuse-4, u02 probe-c, the compile ladders for u01 and u02, and `Cap:` lines on u01 and u02.

Authors: an opus agent per item, its keys checked by `cargo test` green on key and red on stub, then a blind solve by a fresh sonnet from stub and spec. Summoned by the trainer after the owner's verdict.

## Tool defect found while reading

`gym train status` shows the u01 and u02 DELAYED PROBE as `pass (2026-10-26)`. It reads the last `probe-item` row of the side, which is p3, a pass. Both probes were 2 of 3, with p1 failed. The unit column should read the side as a whole.

## Verdict

Owner, 2026-10-26, in the question tool: "Approve all".
