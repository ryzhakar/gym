# W-1 to W-12: premises of the Items, Procedure and Tooling bullets

Independent check. Prescriptions and opinions are marked NOT JUDGED; the facts under them are judged where stated.

Sources, and how they are cited:

- `E<n>`: line n of `training/rust/sessions/2026-10-01T15-56/events.md`. Local time (EEST).
- `T<n>`: line n (1-based) of the trainer JSONL. The file stamps UTC; local = UTC + 3 h. Times below are local.
- `G:<path>`: `git show 5c540de:<path>`. Items under `training/rust/items/`, code under `src/gym/train/`.
- Workspace: `training/rust/work/2026-10-01T15-56/u02-enums-match/`, read with `stat`.
- Scratch runs: 5c540de code extracted with `git archive` into the session scratchpad, `uv run`.

Bank state: `git log 5c540de..HEAD -- training/rust/items src/gym/train` shows no commit before 20:46 on 2026-10-01. The last session event is 18:14. So 5c540de is the bank and the code the session ran on.

Evidence copies: `review/evidence/premises/`, listed in its `MANIFEST.md`.

## W-1 Items: the cap, or its absence

### W-1.1 Say the cap, or its absence, in every item's text.
Verdict: NOT JUDGED (PRESCRIPTION).
Evidence: none sought. The facts under it are W-1.2 to W-1.5.
Bears on: item texts of the Rust bank.

### W-1.2 The u02 reuse-1 item text states neither a cap nor its absence.
Verdict: CONFIRMED.
Evidence: `G:training/rust/items/u02-enums-match/reuse-1/spec.md`, 8 lines. `grep -i -E 'minute|cap|clock|stop at'` over it returns no line. The same grep returns no line for u02 reuse-2 and unshown, nor for reuse-1 and reuse-2 of u01 and u03. Contrast in u02: `attempt.md` line 24 reads "10 minutes, unaided, compiler on. Stop at 10, finished or not." Each probe-a spec reads "10 minutes for p1, p2 and p3 together."
Bears on: `spec.md` of u02 reuse-1.

### W-1.3 The u02 reuse-2 item text states neither a cap nor its absence.
Verdict: CONFIRMED.
Evidence: `G:training/rust/items/u02-enums-match/reuse-2/spec.md`, same grep, no hit. T215 (17:08:25), the trainer's presentation of reuse-2, quotes the spec. The word "cap" does not occur in the message. Its clock text: `Write "go" when you start and "done" when you stop.`
Bears on: `spec.md` of u02 reuse-2.

### W-1.4 The learner assumed a cap on reuse-2.
Verdict: CONFIRMED. The belief is read from the learner's words; no source records it directly.
Evidence: T223 (17:24:21) learner: "clock ran out". T235 (17:25:44) learner: "wait, there was no cap?". T241 (17:25:53) trainer: "Correct, there was no cap. I checked the spec, and the words "cap" and "minute" do not appear in it. I said "no cap" when I presented reuse-1 and left it out for reuse-2." E37: "learner stopped at 13.53 min believing a clock ran out". Last save 17:24:05 (T227, stat), 13.52 min after the trainer's go-logging command at 17:10:33.6 (T218).
Bears on: the learner's stop on reuse-2 at 17:24.

### W-1.5 The learner assumed a cap on reuse-1.
Verdict: UNVERIFIABLE. Missing: any learner statement of a belief about a cap on reuse-1. A contrary indication exists.
Evidence: T148 (16:32:56), trainer presenting reuse-1: "The spec sets no cap. Time runs from 16:32 to your last save." Learner messages during reuse-1: T177 (16:54:13) "go"; T185 (17:01:17) "i can use the rustbook, can't i? / can't remember the value pattern matching syntax"; T193 (17:06:10) "did not finish, stuck on syntax stuff". None names a cap or a clock. Last save 17:05:36 (T197, stat), 11.26 min after the go-logging command.
Bears on: the learner's stop on reuse-1 at 17:05.

## W-2 Items: the sensor attempt

### W-2.1 The attempt item asks for two forms.
Verdict: CONFIRMED.
Evidence: `G:.../u02-enums-match/attempt.md` lines 7-8: "1. `src/enum_form.rs`: `Reading` as an enum." and "2. `src/flat_form.rs`: `Reading` as a struct, with no `enum` anywhere in the file." Line 3: "Edit: src/enum_form.rs, src/flat_form.rs".
Bears on: `attempt.md` of u02.

### W-2.2 Each form holds five functions.
Verdict: CONFIRMED.
Evidence: `attempt.md` line 10: "Each file defines `Reading` and the same five functions". Listed: `temp`, `fault`, `off` (line 12), `label` (line 13), `fault_code` (line 20). Count: 5.
Bears on: `attempt.md` of u02.

### W-2.3 The attempt cap is 10 minutes.
Verdict: CONFIRMED.
Evidence: `attempt.md` line 24: "10 minutes, unaided, compiler on. Stop at 10, finished or not." T70 (15:57:41), presentation: "I check the 10-minute cap against that save time after you return."
Bears on: cap line of `attempt.md` of u02.

### W-2.4 The learner's first state took 16 minutes of wall time.
Verdict: CONFIRMED as a wall-clock span, staging to last save. It is not a measure of the learner's working time, and no source marks the learner's start.
Evidence: T75 (16:14:25), stat run by the trainer: "16:14:04 src/enum_form.rs", "15:57:25 src/flat_form.rs", "15:57:25 src/lib.rs", "15:57:25 tests/visible.rs", "15:57:25 Cargo.toml". The 15:57:25 files are the `cp -R` staging (T60-T61, 15:57:24-25). 16:14:04 minus 15:57:25 = 16 min 39 s = 16.65 min, recomputed. E6 logs minutes=16.65. From the presentation message (T70, 15:57:41.6): 16.37 min. The learner's first return, T71 (16:14:19): "did enum variant, not the struct." E7 (16:16) logged "over the 10 min cap"; E21 (16:50) retracts: "attempt minutes=16.65 ran from staging to last save and includes env setup and message lag; the over-cap claim is unsupported". T149 (16:49:29) learner: "i need time to set the env up every time. on top of that, i'm not guaranteed to see the message instantly." The 16:14 file state survives only in T75; the workspace file was overwritten at 17:52:37.
Bears on: `minutes=16.65` of the attempt event (E6) and the cap of `attempt.md`.

### W-2.5 Split the halves or raise the cap.
Verdict: NOT JUDGED (PRESCRIPTION).
Evidence: none sought.
Bears on: `attempt.md` of u02.

## W-3 Items: the probe-a shared cap

### W-3.1 Probe-a's cap is 10 minutes, shared across p1, p2 and p3.
Verdict: CONFIRMED.
Evidence: `G:.../probe-a/p1-tokens/spec.md` line 7, `p2-tilt-status/spec.md` line 11, `p3-alert/spec.md` line 14: "10 minutes for p1, p2 and p3 together." E50: `probe-start ... problems=p1-tokens,p2-tilt-status,p3-alert`. T334 (18:13:26): `probe grade ... --cap-minutes 10`. E52-E54: `over_cap=yes total_minutes=18.44`.
Bears on: the three probe-a `spec.md` files and the `--cap-minutes` value of the grade call.

### W-3.2 The three probe-a problems are write-heavy.
Verdict: REFUTED. It holds for p3 only.
Evidence: item types, `G`: p1 title "u02 probe-a p1 · predict the output", `Edit: prediction.txt`. p2 title ends "the compile error", body "`cargo test` fails: the crate does not compile. Make it pass." p3 title "u02 probe-a p3 · write to the tests". Learner output against the stubs (stub bytes from `git show`, learner bytes from `evidence/premises/`):

| problem | file | stub bytes | learner bytes | difference |
|---|---|---|---|---|
| p1 | prediction.txt | 0 | 78 (9 lines) | +78 |
| p2 | src/lib.rs | 288 | 300 | +12; one line differs: `None => "none",` became `None => "none".to_string(),` |
| p3 | src/lib.rs | 241 (11 lines) | 785 (19 lines) | +544 |

T357 (18:15:14), trainer to learner: "Problem 1 is the same type as the baseline item you passed before practice, so it adds little evidence of learning. Only problem 3 asks for a full write." T331 (18:13:18) learner, after all three: "the amount of typing is completely non-trivial, i think the time limit this short is unfair here. non-copy-pastable stuff." It names no problem.
Bears on: the shared cap of probe-a and the item mix of `probe-a/`.

### W-3.3 The three problems took about 15.5 go-based minutes.
Verdict: PARTLY. The arithmetic of the stated parts holds. The figure is not reproduced by any anchor. "Go-based" holds for p1 only.
Evidence: E55 (18:14): "go-based working time about 3.4 for p1, 1.1 for p2, 11 for p3, about 15.5 total against the 10 minute shared cap". 3.4 + 1.1 + 11 = 15.5. The learner sent "go" once in the probe: T301 (17:56:08.5) "problem 1 go". Later learner messages: T315 (17:59:37.4) "done with problem 1. / setting 2."; T323 (18:00:58.4) "done problem 2 / setting 3". No "go" for p2 or p3, though the trainer asked for one at T322 and T330. Last saves: p1 prediction.txt 17:59:21.1 (T319); p2 src/lib.rs 18:00:49.4 (T327); p3 src/lib.rs 18:12:34.6 (workspace stat). Minutes recomputed, last save minus anchor:

| problem | learner message | trainer command | other anchor |
|---|---|---|---|
| p1 | 3.21 (17:56:08.5) | 3.07 (17:56:16.7) | 3.35 (present stamp 17:56:00, E51) |
| p2 | 1.20 (17:59:37.4) | 1.08 (17:59:44.7) | 1.47 (p1 last save) |
| p3 | 11.60 (18:00:58.4) | 11.54 (18:01:02.3) | 11.75 (p2 last save) |
| sum | 16.02 | 15.69 | |

Single span, p1 go message to p3 last save: 16.44 min; from the trainer's command: 16.30 min. Stated 15.5 sits 0.2 to 0.9 below every recomputed total. Every recomputed total exceeds 10 min by 5.7 to 6.4. Tool figures for comparison: E52-E54 `total_minutes=18.44`, from the minute-truncated stage stamp 17:55:00 to the grade call at 18:13:26.
Bears on: the `probe-a` feedback note (E55) and the over-cap reading of probe-a.

### W-3.4 Recalibrate or drop the shared cap.
Verdict: NOT JUDGED (PRESCRIPTION).
Evidence: none sought.
Bears on: the shared cap of probe-a.

## W-4 Items: hint ladders and the compile stage

### W-4.1 The supplied hint ladders assume the tests run.
Verdict: PARTLY. True of the level-1 rung of u02 reuse-1 and u03 reuse-1. Not true of the other 13 of 15 ladders.
Evidence: `G:training/rust/items/{u01-own-move-borrow,u02-enums-match,u03-result-question-mark}/hints.yaml`, 15 ladders (u01 4, u02 5, u03 6). Level-1 text, grouped:

| level-1 rung points at | ladders | count |
|---|---|---|
| a test run | u02 reuse-1: "Run the tests and read which ticket gets the wrong price."; u03 reuse-1: "Read which test fails and which variant it expected." | 2 |
| compiler output | u01 attempt, reuse-1, reuse-2, unshown (E0502, E0382, E0507); u02 reuse-2-distance: "Read the compiler's message at the line that computes a line's cost."; u03 unshown | 6 |
| neither | u02 attempt, reuse-2, unshown; u03 attempt-propagate, attempt-explicit, reuse-2, reuse-3 | 7 |

In u02: 1 of 5 ladders. Each file's header reads "Level 1 points at the evidence", with no stage named. E29 states the reuse-1 case: "supplied hint ladder skipped because level 1 assumes the tests run".
Bears on: `hints.yaml` of u01, u02 and u03.

### W-4.2 The reuse-1 attempt stalled at a syntax error before any test ran.
Verdict: CONFIRMED.
Evidence: T197 (17:06:15), `cargo test` in reuse-1: "error: expected one of `)`, `,`, `@`, `if`, or `|`, found `:`" at `src/lib.rs:11:26`, then "error: could not compile `u02-reuse-1` (lib) due to 1 previous error". Learner file, `evidence/premises/reuse-1/src/lib.rs` (mtime 17:05:36): line 11 `Ticket::Adult(age: (0..=65)) => 1200,`, line 12 `Ticket::Adult{_} => 800,`. T185 (17:01:17) learner: "can't remember the value pattern matching syntax". T193 (17:06:10): "did not finish, stuck on syntax stuff".
Bears on: the reuse-1 attempt (E27, `result=fail minutes=11.27`).

### W-4.3 The supplied reuse-1 ladder went unused.
Verdict: CONFIRMED.
Evidence: E29 (17:06): "supplied hint ladder skipped because level 1 assumes the tests run". T208 (17:06:59) trainer: "I gave no hint because the supplied hints assume the tests run and yours stops at the parser." The 59 events hold no `hint` event and no `ladder-gap` event. The learner's three `request=explain` events on reuse-1 (E22, E23, E25) are procedure questions; none asks for a hint.
Bears on: the reuse-1 ladder in `hints.yaml` of u02.

### W-4.4 Add a compile-stage rung for syntax stalls, as reuse-1 needed.
Verdict: NOT JUDGED (PRESCRIPTION; "needed" is OPINION). The stall it cites is W-4.2.
Evidence: none sought.
Bears on: `hints.yaml` of u02.

## W-5 Items: types inside probe-a

### W-5.1 Probe-a mixes item types.
Verdict: CONFIRMED.
Evidence: `G`: p1 title "predict the output"; p2 body "`cargo test` fails: the crate does not compile. Make it pass." (title ends "the compile error"); p3 title "write to the tests". Three types in three problems.
Bears on: `probe-a/` of u02.

### W-5.2 Probe-a p1 repeats the baseline's type.
Verdict: PARTLY. p1 matches the type of baseline b6 and b5. The baseline as a whole holds all three types.
Evidence: `G:.../baseline/b6-enum/spec.md` line 5: "Read `src/main.rs`. Write its exact stdout into `prediction.txt`, one printed line per line." p1 `spec.md` carries the same sentence with `Edit: prediction.txt`. Baseline titles, `G`: b1-own and b2-life carry the compile-error title; b3-result and b4-traits "write to the tests"; b5-iter and b6-enum "predict the output". E55 states the narrower form: "p1 is the type of baseline b6".
Bears on: `probe-a/p1-tokens/` and `baseline/b6-enum/`.

### W-5.3 Probe-a p2 is u01's type.
Verdict: CONFIRMED.
Evidence: `G:.../u01-own-move-borrow/attempt.md` line 5: "`cargo test` fails: the crate does not compile. Make it pass." p2 `spec.md` line 5: the same sentence. u01 reuse-1, reuse-2, unshown, probe-a p1 to p3 and probe-c p1 to p3 carry the compile-error title.
Bears on: `probe-a/p2-tilt-status/`.

## W-6 Items: the next unit

### W-6.1 No unit in the bank differs in type from u02.
Verdict: PARTLY. False as written, since u01 differs. True among units with no events of their own, which is u03 alone.
Evidence: u02 practice items: `attempt.md` line 5 "Model it twice, and make `cargo test` pass."; reuse-1, reuse-2 and unshown titled "write to the tests". u01: `attempt.md` line 5 "`cargo test` fails: the crate does not compile. Make it pass."; reuse-1, reuse-2, unshown carry the compile-error title. T39 (15:56:50), status at session start: units listed are baseline and u01 only; u03 holds no event. T70 (15:57:41): u01's delayed probe is due 2026-10-07. The definition's pick rule (T32, `<open-the-session>`): "the first unit with no events of its own, of a type ... differing from the last unit's".
Bears on: the unit bank, `training/rust/items/`, and the `next_unit` row.

### W-6.2 u03 is also write-to-tests.
Verdict: CONFIRMED.
Evidence: `G:.../u03-result-question-mark/attempt.md` line 5: "Write `parse_line(...)` twice, and make `cargo test` pass." reuse-1, reuse-2, reuse-3 and unshown are titled "write to the tests". Its probe-a is mixed: p1 and p3 "write to the tests", p2 a compile-error item.
Bears on: items of u03.

### W-6.3 `next_unit` was queued to u03.
Verdict: CONFIRMED.
Evidence: E58 (18:14): `queue unit=u03-result-question-mark kind=next_unit due=2026-10-02`. T345 (18:14:20), the logging command.
Bears on: the due queue.

### W-6.4 The queueing rested on the type match.
Verdict: UNVERIFIABLE. Missing: any stated reason for the queue row. The trainer JSONL holds 58 thinking blocks with 229 characters in all, none about the queue.
Evidence: circumstance only. T341 (18:13:52) the trainer ran `head -12 u03-result-question-mark/attempt.md; ... head -8 u01-own-move-borrow/attempt.md; ...`. T345 logged the queue 28 s later. T357 lists the queue rows with no reason.
Bears on: the `next_unit` row (E58).

## W-7 Procedure: the clock

### W-7.1 From 16:50 the practice clock started on the learner's "go".
Verdict: CONFIRMED.
Evidence: T160 (16:50:07) trainer: "Practice items, from now: write "go" when your environment is ready and you start. Time is that message to your last save." Learner "go" messages: T177 16:54:13.4 (reuse-1), T216 17:10:29.3 (reuse-2), T301 17:56:08.5 (probe p1). Logged minutes are reproduced from the trainer's go-logging command, 7.1 s and 4.3 s after the messages (T180 16:54:20.5, T218 17:10:33.6): reuse-1 17:05:36 minus 16:54:20.5 = 11.26 (E27 11.27); reuse-2 17:24:05 minus 17:10:33.6 = 13.52 (E35 13.53), 17:35:59 gives 25.42 (E39 25.43). No "go" exists for p2 or p3 (see W-3.3).
Bears on: `minutes=` of E27, E35, E39 and the clock rule in the trainer definition.

### W-7.2 With no "go", the clock starts on the trainer's message.
Verdict: CONFIRMED as adopted at 17:53 and applied to the attempt-return. Whether the learner gave the permission earlier is UNVERIFIABLE from the allowed sources.
Evidence: T261 (17:37:17) trainer: `Write "go" when you start and "done" when you stop.` The learner's reply T262 (17:52:44) opens "done"; no "go" in the session between. E43 minutes=15.4: last save 17:52:37 (T266, stat) minus the trainer's command 17:37:13.5 (T257) = 15.39, recomputed. T273 (17:53:23) trainer: "You sent no "go", so this is an upper bound". T274 (17:53:23) learner: "i explicitly let you assume i started on your message, sorry for no notification". T281 (17:53:31) trainer: "From now on, with no "go", the clock starts at my message." E46: "the permission was not in the trainer's record before this message". Missing for the earlier grant: any session record before 2026-10-01T15-56, outside the allowed sources.
Bears on: `minutes=15.4` of E43 and the clock rule.

### W-7.3 State it at presentation.
Verdict: NOT JUDGED (PRESCRIPTION).
Evidence: context only. Clock statements made at presentations: T70 (15:57:41) "Time runs from start to your last file save."; T148 (16:32:56) "Time runs from 16:32 to your last save."; T215 (17:08:25) and T261 (17:37:17) `Write "go" when you start and "done" when you stop.`; T273 (17:53:23) for the probe, "Clock: it starts when I stage the problems on your "go"." No presentation text carries the no-"go" fallback before T281.
Bears on: presentation messages of the trainer.

## W-8 Procedure: staging before "go"

### W-8.1 A probe was staged before the learner's "go".
Verdict: CONFIRMED.
Evidence: T282 (17:54:46) learner: "confident, 4. / stage, then i say go." T295-T296: `probe stage` run; `date` prints "Thu Oct  1 17:55:14 EEST 2026". E50 (17:55): `probe-start`. T301 (17:56:08.5) learner: "problem 1 go". Gap stage to go: 54.4 s. The definition, T32 (identical to `G:.claude/agents/gym-trainer.md`, byte compare True): "`uv run gym train probe stage <unit dir> immediate|delayed --session <session id>` on the learner's go". T300 (17:55:19): "The tool's clock started at the stage, 17:55, so its recorded minutes include your setup."
Bears on: the `probe-start` event (E50) and the stage step of the trainer definition.

### W-8.2 The tool has no start mark.
Verdict: CONFIRMED.
Evidence: `G:src/gym/train/cli.py` lines 60-86: `probe stage` takes unit dir, side, `--session`; `probe grade` takes the same plus `--cap-minutes`. `G:src/gym/train/probe.py` line 253: `started = datetime.strptime(start_row["timestamp"], TIMESTAMP_FORMAT)`, the `probe-start` event stamp; lines 213-214 note it is truncated to the minute. `schema.py` `KINDS` holds 18 kinds; none marks a go. Scratch run: `log_event(..., "go", ...)` returns "refused, unknown kind: 'go'".
Bears on: `gym train probe stage` and `gym train probe grade`.

### W-8.3 Decide whether a probe may be staged before the learner starts, or give the tool a start mark.
Verdict: NOT JUDGED (PRESCRIPTION).
Evidence: none sought. The facts under it are W-8.1 and W-8.2.
Bears on: the stage step of the trainer definition and `gym train probe`.

## W-9 Procedure: event kinds

### W-9.1 A procedure answer fits no event kind.
Verdict: REFUTED against the schema in code. The trainer definition's kind list omits the kind that exists.
Evidence: `G:src/gym/train/schema.py` lines 138-143: "mechanics ... (setup, rules, clarifying questions — not an item turn) went unlogged; `unit` is optional since a procedural turn need not belong to any one unit." then `"procedure": {"note": nonempty}`; line 254: `"procedure": {"unit": nonempty}` as optional field. Scratch run on 5c540de code: `log_event(subj, "2026-10-01T15-56", "trainer", "procedure", ['unit=u02-enums-match', 'note=where to run cargo'])` accepted and wrote a line; so did the same without `unit`. `KINDS` (18): answer, attempt, build, close, confidence, feedback, hint, instruction, ladder-gap, open, present, probe-item, probe-start, procedure, question, queue, request, start. The definition (T32) lists kinds in `<log-every-turn>` without `procedure` and adds "never a kind or a field outside these"; "procedure" appears there once, in the closing heading of the narrative rule: "... in the items, in the procedure, in the tooling". T56, `gym train log --help`, lists no kinds. The six events in W-9.2 are setup, rules and clarifying turns.
Bears on: `KINDS` in `schema.py` and `<log-every-turn>` of the trainer definition.

### W-9.2 Six procedure answers were logged as `feedback`, each with a note saying so.
Verdict: PARTLY. Six of the 12 `feedback` events concern the clock, the cap or procedure. Three notes say no kind fits.
Evidence: E21 (16:50) "correction: attempt minutes=16.65 ran from staging ..."; E22 (16:51), E23 (16:53), E25 (17:01) each "procedure answer, no kind fits: ..."; E37 (17:25) "correction: reuse-2 spec has no cap ..."; E46 (17:53) "procedure: learner states standing permission ...". Counts by note: containing "no kind fits" 3 (E22, E23, E25); beginning "procedure" 4 (E22, E23, E25, E46); beginning "correction" 2 (E21, E37). The other six `feedback` events (E7, E28, E36, E40, E44, E55) judge the learner's work.
Bears on: the `feedback` events of the session record.

### W-9.3 "Go" marks were logged as `present`.
Verdict: CONFIRMED.
Evidence: T180 (16:54:20.5) after the learner's go at T177: `uv run gym train log ... present unit=u02-enums-match item=reuse-1`, giving E24. T218 (17:10:33.6) after T216: `present ... item=reuse-2`, giving E33. T304 (17:56:16.7) after T301: `present ... item=p1-tokens`, giving E51. Three of the 7 `present` events are go marks (E24, E33, E51). The other four are presentations (E3, E20, E32, E41). reuse-1 and reuse-2 each hold two `present` lines.
Bears on: `present` events E24, E33, E51.

### W-9.4 Add a kind.
Verdict: NOT JUDGED (PRESCRIPTION).
Evidence: none sought. The facts under it are W-9.1 to W-9.3.
Bears on: `KINDS` in `schema.py`.

## W-10 Tooling: predict-output minutes

### W-10.1 Probe-a p1 minutes read 0.00.
Verdict: CONFIRMED.
Evidence: E52 (18:13): `probe-item ... problem=p1-tokens result=pass minutes=0.00 total_minutes=18.44 over_cap=yes fraction=1.0000`.
Bears on: the `minutes` field of E52.

### W-10.2 The cause is that the tool reads only `src/`.
Verdict: CONFIRMED for probe grading. Baseline grading reads top-level files.
Evidence: `G:src/gym/train/probe.py` line 260: `item_minutes = minutes_since(started, latest_mtime_under(work_dir / "src"))`. The learner's only edited file in p1 is `prediction.txt` at the crate root (README, T38: "the learner's only file is `prediction.txt`"). Workspace p1: `src/main.rs` mtime 2026-09-28T14:11:01.789, `prediction.txt` 2026-10-01T17:59:21. Recompute with the 5c540de functions on the workspace, start 17:55:00:

| problem | latest mtime under src/ | minutes_since | E52-E54 |
|---|---|---|---|
| p1 | 2026-09-28T14:11:01.789 | 0.00 (unfloored -4543.97) | 0.00 |
| p2 | 2026-10-01T18:00:49.424 | 5.82 | 5.82 |
| p3 | 2026-10-01T18:12:34.620 | 17.58 | 17.58 |

`G:src/gym/train/baseline.py` lines 112-114: "Covers `src/lib.rs` items and `prediction.txt` items (top-level, not under `src/`) alike, unlike probe's own `latest_mtime_under`, which only ever looks under a problem's `src/`." p1 was the only predict-output item graded by the probe tool this session.
Bears on: `latest_mtime_under` and `run_grade` in `probe.py`.

## W-11 Tooling: practice grading

### W-11.1 No command grades practice items against held-out tests.
Verdict: CONFIRMED.
Evidence: `G:src/gym/train/cli.py` commands: `open`, `log`, `probe stage`, `probe grade`, `baseline stage`, `baseline grade`, `close`, `status`, `check`. `probe.py` lines 44-55: a side is `immediate`, `delayed` or `probe-[a-z]`; line 136-137: the key path is `key/<side>/<problem>`. Practice keys sit at `key/attempt`, `key/reuse-1`, `key/reuse-2`, `key/unshown` (`git ls-tree`, names only). `baseline grade` takes baseline item ids. `G:training/rust/items/README.md`, Grading: by hand, "Copy `key/<problem>/` to a scratch directory, copy the learner's `Edit:` files into it, run `cargo test`." E40: "no command grades practice items and key/ stays closed". The definition forbids opening a key path (T32, `<run-the-probe>`).
Bears on: `cli.py` of `gym train` and the Grading section of the items README.

### W-11.2 The two practice passes of the session were logged on visible tests, held-out tests unrun.
Verdict: PARTLY. True of reuse-2. For the attempt-return the key holds no held-out file.
Evidence: E39-E40, reuse-2 `result=pass`, "visible and structure tests green; held-out not run". E43-E44, attempt-return `result=pass`, "14 of 14 visible tests green both forms, held-out not run". `git ls-tree -r --name-only 5c540de -- training/rust/items/u02-enums-match/key`, names only, contents unread: `key/reuse-1/tests`, `key/reuse-2/tests` and `key/unshown/tests` each hold `heldout.rs`; `key/attempt/tests` holds `visible.rs` alone. The README line "Pass = every test green" is the rule the claim cites.
Bears on: events E39, E40, E43, E44 and the `key/` trees of u02.

### W-11.3 Add a command so a pass means every test green.
Verdict: NOT JUDGED (PRESCRIPTION).
Evidence: none sought. The facts under it are W-11.1 and W-11.2.
Bears on: `gym train` commands.

## W-12 Tooling: modification times at staging

### W-12.1 Probe staging keeps the source files' old modification times.
Verdict: CONFIRMED.
Evidence: `G:src/gym/train/probe.py` line 132: `shutil.copytree(source_dir, work_dir)`, default copy function `copy2`, which keeps mtimes. Workspace against bank files, compared at microsecond resolution: p1 `src/main.rs` 2026-09-28T14:11:01.789488 equal; p1 `tests/predict.rs` 2026-09-28T14:22:05.268817 equal; p2 `spec.md` 2026-09-30T19:37:44.844565 equal; p3 `tests/structure.rs` 2026-09-28T15:57:38.454211 equal. T327 (18:01:02) shows the staged files at 2026-09-28 and 2026-09-30 beside `Cargo.lock` at 2026-10-01 17:55:56. Contrast: practice crates staged by the trainer with `cp -R` carry new mtimes (15:57:25, T75).
Bears on: `stage_item` in `probe.py` and the `src/` mtimes of staged crates.

### W-12.2 The tool's floor at zero hides it.
Verdict: CONFIRMED.
Evidence: `G:src/gym/train/probe.py` line 225: `return max(0.0, (touched - reference).total_seconds() / 60)`; docstring lines 209-211: "floored at 0 ... an untouched problem gets minutes=0". Recompute for p1: unfloored -4543.97 min, logged as 0.00 (E52).
Bears on: `minutes_since` in `probe.py`.

### W-12.3 A start mark would be cleaner.
Verdict: NOT JUDGED (OPINION).
Evidence: none sought.
Bears on: `gym train probe stage`.

## Where the sources contradict the account

- **W-3.2:** the account calls all three probe-a problems write-heavy. Item types and byte counts show p1 and p2 are not. The trainer's own T357 says "Only problem 3 asks for a full write."
- **W-9.1:** the account says no event kind fits a procedure answer. `schema.py` at 5c540de holds a `procedure` kind built for setup, rules and clarifying turns. The trainer definition omits it.
- **W-9.2:** the account says six feedback events carry a note saying so. Six concern procedure or correction; three say "no kind fits".
- **W-6.1:** the account says no unit differs in type from u02. u01 differs. The sentence holds only among units without events, which is u03.
- **W-4.1:** the account says the supplied ladders assume the tests run. Two level-1 rungs of 15 do.
- **W-3.3:** the account gives about 15.5 go-based minutes. Recomputation gives 15.7 to 16.4 under every anchor. Only p1 had a "go".
- **W-1.5:** the account says the learner assumed a cap on reuse-1. The trainer told the learner "The spec sets no cap" at presentation. No learner statement of a cap exists.
- **W-5.2:** the account says p1 repeats the baseline's type. The baseline holds three types; p1 matches b5 and b6.
- **W-11.2:** the premise that practice passes skipped tests holds for reuse-2. E44 records "held-out not run" for the attempt-return, where the key holds no held-out file.
- **W-2.4:** E7 logged the attempt as over its cap at 16.65 min; E21 retracts it. The 16-minute span stays, as a wall-clock span only.

## Counts

| verdict | count |
|---|---|
| confirmed | 24 |
| refuted | 2 |
| partly | 6 |
| unverifiable | 2 |
| not judged | 9 |
| total assertions | 43 |

Not judged: W-1.1, W-2.5, W-3.4, W-4.4, W-7.3, W-8.3, W-9.4, W-11.3, W-12.3. Refuted: W-3.2, W-9.1. Partly: W-3.3, W-4.1, W-5.2, W-6.1, W-9.2, W-11.2. Unverifiable: W-1.5, W-6.4. The earlier grant of the no-"go" permission (W-7.2) is also unverifiable; the verdict of W-7.2 counts the confirmed part.

## Checker notes

- **Shared scratchpad:** at about 21:20 I moved another agent's `parse.py` and `view.py` into my own subdirectory by mistake and put them back with `mv -n` within a minute. Another agent had overwritten my first parse output in the shared scratchpad before I read it. My work after that sits under `scratchpad/w-premises/`.
- **Narrative exposure:** the trainer's tool call that wrote the session narrative (T353) was in the transcript view I printed. I saw its first 5000 characters; the last 2268 I did not view. `session.md` itself I did not open. I used none of that text as evidence.
- **Git log exposure:** the `git log` listing printed subjects of commits made after the session. I read none of their content.
- **Not checked:** the learner's real start moment for any item; whether `Cargo.lock` mtimes mark starts; the contents of any `key/` file; whether the learner gave the no-"go" permission before this session.
- **Directory name:** evidence copies sit under `evidence/premises/`, not per item, so they cannot collide with other checkers' manifests.

## Summary

Premises W-1 to W-12 split into 43 assertions: 24 confirmed, 2 refuted, 6 partly, 2 unverifiable, 9 prescriptions or opinions not judged.
Refuted: the three probe-a problems are not all write-heavy, since only p3 is, and a procedure answer does fit an event kind, since a `procedure` kind exists in the code.
Partly: the 15.5 go-based minutes, the ladders assuming tests run, the baseline's type, the no-differing-unit premise, the six procedure notes and the unrun held-out premise; unverifiable: the learner's assumed cap on reuse-1 and the reason u03 was queued.
