# 2026-10-30T15-41
subject: rust
learner: arthur
trainer model: claude-opus-5-5, session trainer-u3
gap_days: 4.13

## Narrative

Unit u03-result-question-mark, revisit due 2026-10-27, run 4.13 days after the last session. Items: reuse-3, instruction, reuse-6 (authored this session), immediate probe-a. Session 15:41 to 16:56.

### reuse-3 · write to the tests

The learner implemented `tally`. In a first try, not saved, he put `?` inside the `map` closure and the compiler refused (his own account; no build of that version was logged). The saved version collects every parse into `Vec<Result<u32, TallyError>>` with `map_err` to `BadEntry`, then applies `?` per element in a later loop. A second `Vec<&str>` exists only for the emptiness check. The graded run passed at 1.00. The time was 27.02 minutes, from go 15:44 to the last save 16:11, against a cap of 10.

Feedback: the attempt was eager, because every entry was parsed before the first `?`. I also noted the extra Vec, and that `total += ballot` can overflow `u32`, which the item doesn't test. The learner asked whether it could be lazy. Principles named, one per instruction turn:
- `?` returns from the enclosing closure;
- a closure's return type is inferred from all its exits, so the tail `u32` and the `?` exit cannot agree;
- a closure cannot return from its caller, so laziness comes from the consumer.

He predicted correctly that, without `collect`, a `for` loop over the `map` parses entries up to and including the bad one and no more.

Misconception shown: he read the closure's type as changing when the error propagated, when it is one type fixed by all exits. He also took collecting as the only way out once `?` failed in the closure.

### reuse-6 · write to the tests (isomorphic, authored mid-session)

An opus agent authored reuse-6 during the instruction: a parcel manifest, `weigh`, and `LoadError` with Empty, BadLine{line, source} and Overflow. It has 3 visible tests and 7 held-out ones. One held-out test checks laziness: an eager collect returns `BadLine` where the spec demands `Overflow`. The key passes 10 of 10 and the stub 0 of 10.

The learner wrote it lazily: the `map` closure yields a `Result`, the `for` loop applies `?` per line, and the sum uses `checked_add(...).ok_or(Overflow)?`. The graded run passed at 1.00. The time was about 10.8 minutes, from 16:19 to 16:29:49, against a cap of 10.

Fault: `Empty` is decided by `grams == 0` after the loop, so `"0\n0"` returns `Empty` although it has lines. The held-out tests miss it, which is an item gap.

### Immediate probe-a

Confidence was 4 for the unit, conditioned by the learner on "if the unit is the same one". He asked before go whether one go covers all three problems. I answered that it does, and that the minutes count per problem from the previous problem's newest save.

The graded run passed 3 of 3 at fraction 1.00. Total 19.78 minutes:
- p1-duration: 11.22 minutes, over its cap of 6;
- p2-dose-admin: 2.86 minutes, within its cap of 3;
- p3-average: 5.70 minutes, within its cap of 6.

Feedback per problem: the slice in p1 is safe but `strip_suffix` does the same in one step; in p2 the `return` before the tail `if` is redundant; p3 used `?` per entry in the loop, lazily, with `checked_div` mapped to `Empty`.

The learner reports that most of the probe time went to splitting the trailing unit character from the number in p1, and that he reached for regex, which is not in std. That is a threat to validity: p1's minutes mix a string-API search with the `?` target, so p1's over-cap time is not evidence on the target. I named the std means, `strip_suffix` and `split_at`.

The unit closes on the immediate pass. The delayed probe-b is queued for 2026-11-06 and is the unit's outcome.

### Queue

- delayed_probe for u03 on 2026-11-06;
- next_unit u04-lifetimes on 2026-11-02, alongside the u01 and u02 revisits already due then;
- next_unit u05-str-slicing on 2026-11-09, the learner's request after p1, a small unit on std string splitting.

## What to change

- Items: add a held-out case to u03 reuse-6 where every line is 0, so the test checks `Empty` against lines rather than against the total. Check u03 probe-b and later string-input items for a std string API the learner has not met, such as `strip_suffix` and `split_at`. Such an API inflates the minutes off-target; either teach it first (u05) or give the split in the stub. Author the u04 bank before 2026-11-02, and the u05 bank.
- Procedure: reuse-3's ten-minute cap held neither the target nor the cost of the string API. Caps stay recorded, never a stop. Confidence was asked once for the unit as specified; the learner's conditional "if the unit is the same one" suggests the prompt should say that the probe is on unit u03, `Result` and `?`.
- Tooling: `gym train log` printed the go time to the minute only, so practice minutes come from that minute and are approximate. Add a seconds-precision `at=` to `go`, as `probe-go` has. In my own shell, a variable holding the log command failed with exit 127 under zsh; a shell function works.

## Close — 2026-10-30T20:46

state   3/3 probe item(s) passed; queued delayed_probe:u03-result-question-mark@2026-11-06, next_unit:u04-lifetimes@2026-11-02, next_unit:u05-str-slicing@2026-11-09
open    none
next    u03 delayed probe 2026-11-06; u04-lifetimes from 2026-11-02
