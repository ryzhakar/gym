# Review 03: probe and learner. Blocks P-1 to P-5, L-1 to L-4

Session 2026-10-01T15-56, unit u02-enums-match, trainer subagent, learner Arthur. Times are local (EEST, UTC+3). Claims read from `docs/orchestration_log/recon/2026-10-01/feedback/claims.md`; each block is a hypothesis.

## Sources used

- **events.md**: `training/rust/sessions/2026-10-01T15-56/events.md`, cited by line number.
- **JSONL**: the trainer transcript, cited by JSONL line number. Verbatim excerpts, all 26 learner messages and the probe section are durable at `training/rust/sessions/2026-10-01T15-56/review/evidence/p1-tokens/transcript/transcript-excerpts.md`.
- **WS**: learner workspace `training/rust/work/2026-10-01T15-56/u02-enums-match/`, file times by `stat`. Learner-written files for my three items are copied to `review/evidence/<item>/` with `MANIFEST.md`. Copies of the other items made by other checkers are cited where used.
- **5c540de**: `git show 5c540de:<path>`. Tool code `src/gym/train/probe.py`, `schema.py`, `events.py`, `cli.py`. Items `training/rust/items/`.
- **Scratch runs**: on copies under the session scratchpad, no write under `training/` or the repo besides review output. Locked tests of p1, p2, p3 run on copies of the learner crates. Walk predictions recompiled with `rustc`.
- **Not used**: `session.md`, anything under `history/`, `key/` (not opened, not run), `recon/` except `claims.md` and the two prompt files. The summons and the 2026-09-30 events are read only as quoted in tool results inside the transcript (JSONL 19, 44, 46). The trainer's own narrative heredoc (JSONL 353) is the account, not evidence.
- **Limits**: held-out tests live under `key/`. I recompute locked tests only. Whether the learner was unaided is established by no source.

## Block P-1

### P-1.1 Confidence value 4 was logged
Verdict: CONFIRMED
Evidence:
- events.md lines 47 to 49: `2026-10-01T17:55 | trainer | confidence | unit=u02-enums-match item=p1-tokens value=4 request=none`, same for `p2-tilt-status`, `p3-alert`.
- Learner, JSONL 282, 17:54:46, two lines: ``confident, 4.`` and ``stage, then i say go.``
Bears on: the three `confidence` event lines of the session record.

### P-1.2 One confidence event per problem
Verdict: CONFIRMED
Evidence:
- events.md lines 47 to 49: three events, one per item, same value.
- The learner gave one rating. Trainer asked, JSONL 273, 17:53:23: ``Rate your confidence for the unit from 0 to 4. The rating predicts the unit, not the unseen problems.``
- Trainer definition, JSONL 32, `run-the-probe`: it prescribes logging the single rating once per problem as a `confidence` event with `item=<problem directory name>` and the same value. The log shape follows that rule; one learner reply fills three lines.
Bears on: the `confidence` lines and the `status` confidence column for u02.

### P-1.3 The probe was staged at 17:55
Verdict: CONFIRMED
Evidence:
- events.md line 50: `2026-10-01T17:55 | tool:probe | probe-start | unit=u02-enums-match which=probe-a problems=p1-tokens,p2-tilt-status,p3-alert`.
- JSONL 295, 17:55:14: `uv run gym train probe stage ... immediate --session 2026-10-01T15-56 2>&1; date`. Output of `date`: `Thu Oct  1 17:55:14 EEST 2026`.
Bears on: the `probe-start` event line.

### P-1.4 Staging was at the learner's request, before "go"
Verdict: CONFIRMED
Evidence:
- Learner JSONL 282, 17:54:46: ``stage, then i say go.`` Stage ran 17:55:14.
- Learner "go": JSONL 301, 17:56:08.5, ``problem 1 go``. Stage precedes it by 54.5 s.
Bears on: the order of stage and "go" for probe-a.

### P-1.5 The trainer normally stages on "go"
Verdict: CONFIRMED (written procedure). One probe was staged in the session, so "normally" is not observable inside it.
Evidence:
- Definition, JSONL 32, `run-the-probe`: `gym train probe stage` runs "on the learner's go, which copies the problems to the work path, logs a `probe-start`".
- Summons as read, JSONL 19, line 51: ``on the learner's "go"``.
- Trainer to learner: JSONL 160 (16:50:07) ``the tool starts the clock when I stage, which I do on your "go"``; JSONL 273 ``Clock: it starts when I stage the problems on your "go".``
Bears on: the trainer definition's probe rule and the summons probe paragraph.

### P-1.6 The tool clock started before the learner started
Verdict: CONFIRMED, with the origin precise.
Evidence:
- probe.py:253 `started = datetime.strptime(start_row["timestamp"], TIMESTAMP_FORMAT)`; schema.py:30 `TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M"` (no seconds); events.py:87 stamps with it. Origin = 17:55:00.
- Learner "go" 17:56:08.5. Origin precedes it by 68.5 s. The stage command ran 17:55:14, 54.5 s before "go".
- WS `p1-tokens/Cargo.lock` and `target/` first written 17:55:56, 12.5 s before "go": a cargo run in the crate during the setup gap. Who or what ran it is not in the sources.
Bears on: `minutes` and `total_minutes` of the three `probe-item` lines.

## Block P-2

### P-2.1 p1 is a predict-the-output item and passed
Verdict: CONFIRMED
Evidence:
- Spec as staged (identical to 5c540de): `"# u02 probe-a p1 · predict the output"`, `Edit: prediction.txt`.
- events.md line 52: `problem=p1-tokens result=pass`.
- Scratch run of the locked test on a copy of the learner crate: `test prediction_matches_stdout ... ok`. The test runs the binary and compares stdout to `prediction.txt` (5c540de `tests/predict.rs`).
- Not established: who or what ran cargo in `p1-tokens` at 17:55:56 and 17:56:36 (WS `target/`, fingerprint files only at 17:56:36; executables and objects all 18:13:26, grading). Items README, JSONL 38: ``rust-analyzer's `cargo check` on open leaves a `target/` directory; that is not a run of the program.`` The artifacts do not separate a rust-analyzer check from a learner `cargo` call.
Bears on: `p1-tokens/prediction.txt` and the p1 `probe-item` line.

### P-2.2 p2 is a compile-error repair item and passed
Verdict: CONFIRMED
Evidence:
- Spec body: `cargo test` fails: the crate does not compile. Make it pass.
- Stub at 5c540de line 4, compiled in scratch: ``error[E0308]: mismatched types`` at `None => "none",`, expected `String`, found `&str`.
- Learner file vs stub (`diff`): line 4 only, `None => "none",` to `None => "none".to_string(),`.
- events.md line 53: `result=pass`. Scratch run of locked test: `reports_each_case ... ok`.
Bears on: `p2-tilt-status/src/lib.rs` and the p2 `probe-item` line.

### P-2.3 p3 is a write-to-the-tests item with no `_` arm and passed
Verdict: CONFIRMED
Evidence:
- Spec heading ``u02 probe-a p3 · write to the tests``; rule ``Every arm names its variant: no `_` arm and no catch-all binding.``
- Stub at 5c540de: `alert` body `todo!()`. Learner file: seven arms, the last `Status::Temp(_) | Status::Humidity(..) | Status::Battery { .. } => None`.
- events.md line 54: `result=pass`. Scratch run: `every_arm_names_its_variant ... ok`; `battery`, `humidity`, `missing`, `temperatures` all ok.
Bears on: `p3-alert/src/lib.rs` and the p3 `probe-item` line.

### P-2.4 All three have fraction 1.0
Verdict: PARTLY. Recorded: confirmed. Recomputed: locked tests only.
Evidence:
- events.md lines 52 to 54: `fraction=1.0000` on each.
- probe.py:107-113: fraction = passed / (passed + failed) summed over every test binary, after held-out files from `key/` are copied in (probe.py:149-162).
- Recomputed on scratch copies, locked tests: p1 1 of 1, p2 1 of 1, p3 5 of 5. Held-out tests not opened or run by me; that share of the 1.0000 rests on the tool line.
Bears on: the `fraction` field of the three `probe-item` lines.

### P-2.5 Over cap: yes
Verdict: CONFIRMED
Evidence:
- events.md lines 52 to 54: `over_cap=yes`, `total_minutes=18.44`.
- probe.py:254-255: `over_cap = "yes" if total_minutes > cap_minutes`; cap 10 (`--cap-minutes 10`, JSONL 334).
- Learner "go" 17:56:08.5 to "done" 18:13:18.8 = 17.17 min, also over 10.
Bears on: the `over_cap` field of the `probe-item` lines.

### P-2.6 The cap was recorded, not enforced
Verdict: CONFIRMED
Evidence:
- probe.py:246-247 docstring: `over_cap ... recorded only, never enforced or refused`.
- Transcript: no trainer text between JSONL 314 (17:56:23) and 322 (17:59:49), none between 330 (18:01:06) and 357 (18:15:14). The first trainer action after 18:01:06 is the grade at 18:13:26, after the learner's "done" at 18:13:18.8. The learner kept working to a last save at 18:12:34.6.
Bears on: the probe procedure and the three `probe-item` lines.

## Block P-3

### P-3.1 p1 tool minutes are 0.00
Verdict: CONFIRMED
Evidence:
- events.md line 52: `minutes=0.00`.
- Recomputed: probe.py:260 `minutes_since(started, latest_mtime_under(work_dir / "src"))`. WS `p1-tokens/src/main.rs` mtime 2026-09-28T14:11:01, before the 17:55:00 origin. probe.py:222-225 floors to 0.0.
Bears on: the `minutes` field of the p1 `probe-item` line.

### P-3.2 The cause is that the tool reads `src/` only and p1 edits `prediction.txt`
Verdict: CONFIRMED
Evidence:
- probe.py:199-205 and :260: only files under `<problem>/src`.
- p1 spec: `Edit: prediction.txt`, at the crate root. WS `p1-tokens/prediction.txt` mtime 17:59:21.1, 4.35 min after the 17:55:00 origin and 3.21 min after "go".
Bears on: `gym train probe grade`, function `latest_mtime_under` call on `work_dir / "src"`.

### P-3.3 p2 tool minutes are 5.82
Verdict: CONFIRMED
Evidence:
- events.md line 53: `minutes=5.82`.
- Recomputed: WS `p2-tilt-status/src/lib.rs` mtime 18:00:49.42 minus 17:55:00 = 5.824 min.
Bears on: the `minutes` field of the p2 `probe-item` line.

### P-3.4 p3 tool minutes are 17.58
Verdict: CONFIRMED
Evidence:
- events.md line 54: `minutes=17.58`.
- Recomputed: WS `p3-alert/src/lib.rs` mtime 18:12:34.62 minus 17:55:00 = 17.577 min.
Bears on: the `minutes` field of the p3 `probe-item` line.

### P-3.5 Total is 18.44
Verdict: CONFIRMED to the precision the sources allow
Evidence:
- events.md lines 52 to 54: `total_minutes=18.44` on each.
- probe.py:254: now minus 17:55:00. `date` printed `18:13:26` at the start of the grading command (JSONL 335). 18:13:26.0 gives 18.433, 18:13:27.0 gives 18.450. The tool's own `now` is not logged; 18.44 is inside that range.
Bears on: the `total_minutes` field and `close` event `probe_minutes=18.44` (events.md line 59).

### P-3.6 The span runs from stage to grade
Verdict: PARTLY
Evidence:
- End confirmed: grade command ran at 18:13:26, 7.2 s after the learner's "done" at 18:13:18.8.
- Start is not the stage instant. Origin is the stage event's stamp cut to the minute: 17:55:00. Stage ran 17:55:14. Stage to grade is 18.20 min; the tool says 18.44. probe.py:213-221 states this limit in its docstring. Per-problem `minutes` (5.82, 17.58) share the origin.
Bears on: `minutes` and `total_minutes` fields of the `probe-item` lines.

## Block P-4

### P-4.1 The go-based times are taken from mtimes
Verdict: PARTLY
Evidence:
- Ends are file mtimes: p1 `prediction.txt` 17:59:21.1, p2 `lib.rs` 18:00:49.4, p3 `lib.rs` 18:12:34.6.
- Starts are a "go" only for p1 (JSONL 301, 17:56:08.5). Sequence after it: learner JSONL 315, 17:59:37.4, ``done with problem 1.`` / ``setting 2.``; trainer JSONL 322, 17:59:49, ``Write "go" for problem 2.``; learner JSONL 323, 18:00:58.4, ``done problem 2`` / ``setting 3``; trainer JSONL 330, 18:01:06, ``Write "go" for problem 3.``; learner JSONL 331, 18:13:18.8, ``done. ...``. No learner "go" for p2 or p3. events.md holds one `present` for the probe, line 51 (p1).
Bears on: the trainer's go-based minutes in `events.md` line 55.

### P-4.2 p1 go-based time is about 3.4 min
Verdict: PARTLY
Evidence:
- Recomputed from the learner's "go": 17:56:08.5 to 17:59:21.1 = 3.21 min. Differs by 0.19.
- 3.35 reproduces only from the `present` event's minute stamp 17:56:00; 3.09 from the trainer's own epoch call at 17:56:16 (JSONL 304).
Bears on: the p1 go-based figure in `events.md` line 55.

### P-4.3 p2 go-based time is about 1.1 min
Verdict: PARTLY
Evidence:
- No "go". From the learner's "done with problem 1. setting 2." 17:59:37.4 to the 18:00:49.4 save = 1.20 min. Differs by 0.10.
- 1.09 reproduces from 17:59:44 (the trainer's `date` call, JSONL 319); 1.47 from the p1 save.
Bears on: the p2 go-based figure in `events.md` line 55.

### P-4.4 p3 go-based time is about 11 min
Verdict: PARTLY
Evidence:
- No "go". From the learner's "done problem 2 setting 3" 18:00:58.4 to the 18:12:34.6 save = 11.60 min. Differs by 0.60; rounds to 12.
- 11.48 reproduces from the trainer reply at 18:01:06 (JSONL 330); 11.54 from 18:01:02 (the trainer's `date` call, JSONL 327).
Bears on: the p3 go-based figure in `events.md` line 55.

### P-4.5 The go-based total is about 15.5 min
Verdict: PARTLY
Evidence:
- 3.4 + 1.1 + 11 = 15.5, the account's own sum. From learner-message origins: 3.21 + 1.20 + 11.60 = 16.02. First "go" to last save: 17:56:08.5 to 18:12:34.6 = 16.44. First "go" to "done" 18:13:18.8: 17.17. Both are over 10 min.
Bears on: the go-based total in `events.md` line 55 and the narrative's probe-time line.

### P-4.6 The learner said the 10-minute cap is unfair for this much typing
Verdict: CONFIRMED
Evidence:
- JSONL 331, 18:13:18.8: ``done. the amount of typing is completely non-trivial, i think the time limit this short is unfair here. non-copy-pastable stuff.`` The message does not name 10 minutes. The specs do: ``10 minutes for p1, p2 and p3 together.``
Bears on: the probe cap of 10 minutes in the p1, p2, p3 specs.

### P-4.7 The cap was recorded and never enforced
Verdict: CONFIRMED
Evidence: see P-2.6.
Bears on: the probe procedure.

### P-4.8 All three passed
Verdict: CONFIRMED
Evidence: events.md lines 52 to 54, `result=pass` on each; scratch runs in P-2.1 to P-2.3.
Bears on: the three `probe-item` lines.

## Block P-5

### P-5.1 p1 is the same type as baseline b6
Verdict: CONFIRMED
Evidence:
- Both specs: predict-the-output, `Edit: prediction.txt`, run no program before submitting (5c540de `baseline/b6-enum/spec.md`, p1 `spec.md`). Items README, JSONL 38: ``Predict-output items: the learner's only file is `prediction.txt`.``
- Same shape: enum with data variants, one `match` function with guards, literal and range-binding arms (`Cmd::Wait(n @ 1..=3)` in b6; `Token::Num(n @ 1..=9)` in p1), a `main` printing one line per value.
Bears on: items `baseline/b6-enum/` and `probe-a/p1-tokens/`.

### P-5.2 b6 was passed before practice
Verdict: CONFIRMED, from the trainer's tool output. I did not open the 2026-09-30 file.
Evidence:
- JSONL 46, grep of `sessions/2026-09-30T15-40/events.md`: `2026-09-30T17:19 | trainer | attempt | unit=baseline item=b6-enum result=pass minutes=2.15`. In the same output b1-own, b2-life, b3-result, b4-traits, b5-iter are `result=fail`.
- u02 practice began 2026-10-01T15:57 (events.md lines 2 and 3).
Bears on: the baseline lines of session 2026-09-30T15-40.

### P-5.3 So p1 adds little evidence of learning
Verdict: NOT JUDGED (OPINION). The facts under it are P-5.1 and P-5.2.
Evidence: none judged.
Bears on: the reading of the p1 `probe-item` line.

### P-5.4 p2 is a compile-error repair item, u01's type
Verdict: CONFIRMED
Evidence:
- p2 spec body: `cargo test` fails: the crate does not compile. Make it pass.
- u01 `attempt.md` head, JSONL 342, same sentence: `cargo test` fails: the crate does not compile. Make it pass.
- The compile error is E0308, `&str` where `String` is expected (P-2.2). The edit is one token.
Bears on: items `u02-enums-match/probe-a/p2-tilt-status/` and `u01-own-move-borrow/attempt.md`.

### P-5.5 Only p3 asks for the full write
Verdict: CONFIRMED
Evidence: p1 edits one prediction file; p2 stub holds a complete match and the learner added one `.to_string()`; p3 stub body is `todo!()` and the spec says ``Implement `alert` so `cargo test` passes.``
Bears on: the specs of p1, p2, p3.

### P-5.6 An immediate probe is not retention evidence
Verdict: NOT JUDGED (OPINION).
Evidence: facts it rests on. The probe ran as `immediate` (JSONL 295). Last practice item ended 17:53 (events.md line 43, `attempt-return result=pass`); the p1 "go" came 17:56:08.5, 2.8 min after the trainer's 17:53:23 message. A delayed probe is queued for 2026-10-08 (events.md line 56).
Bears on: the `probe-a` result and the queue lines.

### P-5.7 Closing of every other assistant is not confirmed in words
Verdict: CONFIRMED
Evidence:
- Trainer asked twice: JSONL 273, an `Assistants:` rule line telling the learner to close every other assistant; JSONL 300 ``Close every other assistant, then write "go".``
- Every learner message from 17:53:23 on (JSONL 274, 282, 301, 315, 323, 331, 358) read; none mentions assistants.
- events.md line 59, manager close: `assistant_closed=no`. Summons, JSONL 19 line 55, defines the report item as ``whether the learner closed every other assistant``; the CLI help for the flag reads ``yes/no: did the trainer close the session`` (5c540de `cli.py:130`).
Bears on: the `assistant_closed` field of the close event.

### P-5.8 The learner proceeded on the trainer's instruction to close them
Verdict: PARTLY
Evidence:
- Confirmed: the learner wrote "go" at 17:56:08.5, 49 s after the 17:55:19 instruction (JSONL 300, 301).
- Not established: that the learner closed any assistant. No source records it either way.
Bears on: the `assistant_closed` field and the unaided status of the probe.

## Block L-1

### L-1.1 Four of five predictions were right
Verdict: PARTLY. Holds for the five walk questions. Scope is not stated in the account.
Evidence: learner replies in the walk, recomputed by compiling.

| # | JSONL, time | Learner said | Recomputed | Result |
|---|---|---|---|---|
| 1 | 101, 16:21:35 | flat struct cannot be built, fields must be `Option`; enum needs match then access | flat struct with dummy fields compiles, `e.x` prints `0`; `Option` form compiles; enum gives E0609 | wrong on flat, right on enum |
| 2 | 113, 16:24:01 | won't compile, non-exhaustive | E0004, `Event::Close` not covered | right |
| 3 | 121, 16:26:30 | `label` stops, `fault_code` returns `None` | `label` E0004 on `Stale`; `fault_code` returns `None` | right |
| 4 | 129, 16:27:50 | compiles, `q` takes generic arm | compiles with unreachable-pattern warning; prints `key q` | right |
| 5 | 137, 16:32:29 | does not compile, variable not in scope | E0425, cannot find value `d` | right |

- Replies: 5, right 4, with reply 1 counted wrong. Sub-predictions as claims.md A-6 lists them (flat, enum, E0004, Stale, `q`, E0425): 6, right 5.
- Outside the walk: reuse-1, JSONL 209, 17:08:04, ``b & d``; recomputed by me, right (`Click { x, y }` and `Scroll(d)` compile; `Click(x, y)` gives E0164 and `Scroll { d }` gives E0769). Session total by replies: 6 of 7 right.
Bears on: the unit's prediction questions, `example-chat.md` lines 1 to 23.

### L-1.2 Exhaustiveness held in the probe
Verdict: PARTLY
Evidence:
- Holds where a locked test enforces it: p3 learner arms all name a variant; `every_arm_names_its_variant ... ok` (P-2.3). p2 adds no arm.
- Not shown unforced: WS `attempt/src/enum_form.rs` mtime 17:52:37, 2.6 min before the stage, still ends `fault_code` with `_ => { None }` (JSONL 266, evidence copy `review/evidence/attempt/src/enum_form.rs`). The "cover every case" instruction was given 16:24 (events.md line 13).
Bears on: `p3-alert/src/lib.rs` and `attempt/src/enum_form.rs`.

### L-1.3 Ordering held in the probe
Verdict: CONFIRMED
Evidence:
- p3 learner file places the catch-all `Status::Temp(_) | ... => None` last. Scratch copy with that arm moved first: `humidity` and `temperatures` fail (five unreachable-pattern warnings). The graded pass therefore needs this order.
- p1: the learner's nine predicted lines (evidence copy `p1-tokens/prediction.txt`) match stdout where result depends on arm order (`Token::Op('+' | '-')` before `Token::Op(c)`, guard arms before plain arms). Locked test passes.
- Unaided is not established (P-5.7).
Bears on: `p3-alert/src/lib.rs` and `p1-tokens/prediction.txt`.

### L-1.4 Binding held in the probe
Verdict: CONFIRMED
Evidence: p3 learner file binds with `t @ ..=-20`, `t @ 40..`, `h @ 91..`, `p @ ..10` (lines 11, 12, 13, 16) and prints the bound value; tests pass. p1 prediction `digit 9` depends on `n @ 1..=9`.
Bears on: `p3-alert/src/lib.rs`.

### L-1.5 The enum design held in the probe
Verdict: REFUTED as a probe result
Evidence:
- p3 spec: `Status` stays as written. Stub holds the enum. p1: `Token` is defined in locked `src/main.rs`. p2 uses `Option<i32>` from std. No probe item asks the learner to define an enum.
- The learner's enum definitions in the session are `Reading` (attempt, 16:14) and `Command` (reuse-2). Both are practice items.
Bears on: items `probe-a/p1-tokens`, `p2-tilt-status`, `p3-alert`.

## Block L-2

### L-2.1 Pattern syntax for named-field variants caused friction
Verdict: CONFIRMED
Evidence:
- WS `reuse-1/src/lib.rs` mtime 17:05:36 (evidence copy `review/evidence/reuse-1/lib.rs`): `Ticket::Adult(age: (0..=65)) => 1200,`, `Ticket::Adult{_} => 800,`, `Ticket::Child(age: ..3) => 0,`. `Adult` and `Child` are declared with braces.
- cargo, JSONL 197: ``error: expected one of `)`, `,`, `@`, `if`, or `|`, found `:` `` at `src/lib.rs:11:26`.
- Learner, JSONL 185, 17:01:17: ``can't remember the value pattern matching syntax``; JSONL 193, 17:06:10: ``did not finish, stuck on syntax stuff``.
Bears on: item `reuse-1`.

### L-2.2 Integer conversion between signed and unsigned caused friction
Verdict: CONFIRMED
Evidence:
- reuse-2 state read 17:24:27 (evidence `review/evidence/reuse-2/lib.rs.state-at-17-24.from-transcript`): `let cost: u32 = std::cmp::max(x_length.abs() + y_length.abs(), 1).into();`. cargo, JSONL 227: ``error[E0277]: the trait bound `u32: From<i32>` is not satisfied``.
- Final state (17:35:59) uses `(x2 - x1).unsigned_abs()`. Recomputed on a scratch copy: `line(i32::MIN,0,i32::MAX,0)` panics `attempt to subtract with overflow` in debug and returns 1 in release.
Bears on: item `reuse-2`, function `cost`.

### L-2.3 The spec's list of required items was read incompletely, twice: struct half, three constructors
Verdict: PARTLY. Omissions confirmed. Cause not established.
Evidence:
- Attempt, 16:14:25 (JSONL 75): `flat_form.rs` mtime 15:57:25, the staged stub; `cargo test` E0432 unresolved imports. Learner JSONL 71: ``did enum variant, not the struct.`` The learner names the struct half as not done.
- reuse-2, 17:24:27 (JSONL 227): `lib.rs` defines `endpoint` and `cost`; `dot`, `line`, `pen_up` absent, though the spec lists them. Learner JSONL 223, 17:24:21: ``clock ran out``. The spec had no cap (JSONL 239, grep exit 1; JSONL 241).
- No source records the learner's reason for the first omission. For the second the recorded reason is a belief that a clock ran out. No source shows what the learner read.
Bears on: items `attempt` (`flat_form.rs`) and `reuse-2` (`dot`, `line`, `pen_up`).

### L-2.4 The three frictions are recurring
Verdict: PARTLY
Evidence:
- In this session: the omission appears in two items. Named-field syntax fails in one item, then is written correctly in `reuse-2` `Command::Line { x2, y2, .. }`, in `flat_form.rs` `Reading{temperature: Some(degrees), ..}`, in p3 `Status::Battery { charging: true, .. }` and `Status::Battery { percent: p @ ..10, charging: false }`. Signed/unsigned appears in one item (two manifestations, L-2.2).
- Earlier sessions are outside my sources, so recurrence across sessions is not checked.
Bears on: items `reuse-1`, `reuse-2`, `attempt`, `p3-alert`.

## Block L-3

### L-3.1 `.to_owned()` is called on a value that is already a `String`
Verdict: CONFIRMED
Evidence: evidence copies `attempt/src/enum_form.rs:33` and `attempt/src/flat_form.rs:28`: `label.to_owned()`. `label` is bound by `let label = match r { ... format!(...) ... }`, every arm a `format!`, so `String`. Present at 16:14:25 (JSONL 75) and at 17:52:37.
Bears on: `attempt/src/enum_form.rs`, `attempt/src/flat_form.rs`.

### L-3.2 `.to_string()` is called on values that are already `String`
Verdict: CONFIRMED
Evidence: evidence copy `p3-alert/src/lib.rs` lines 11, 12, 13, 14, 16: `Some(format!("frost {t}").to_string())` and four more of the same form. `format!` returns `String`.
Bears on: `p3-alert/src/lib.rs`.

### L-3.3 `format!("off")` is used for a literal
Verdict: CONFIRMED
Evidence: `attempt/src/enum_form.rs:31` `Reading::Off => format!("off")`; `attempt/src/flat_form.rs:26` `Reading{..} => format!("off")`; also `format!("fault unknown")` at `enum_form.rs:28`, `flat_form.rs:23`; and `format!("no data")` in p3 line 14.
Bears on: `attempt/src/enum_form.rs`, `attempt/src/flat_form.rs`, `p3-alert/src/lib.rs`.

### L-3.4 These lie outside the unit
Verdict: NOT JUDGED (OPINION, a classification). The facts are L-3.1 to L-3.3. The unit item texts concern enums and `match`.
Evidence: none judged.
Bears on: the unit's scope in `training/rust/items/u02-enums-match/`.

## Block L-4

### L-4.1 The learner flagged one vague question
Verdict: CONFIRMED
Evidence:
- JSONL 93, 16:18:37: ``what do you mean "what happens"? you need to get better at clear non-verbose communication.`` Trainer reworded it, JSONL 100: ``"What happens" was vague.``
- No other learner message among the 26 (excerpts file, part A) flags a question as vague.
Bears on: the first prediction question of the walk, events.md lines 9 and 10.

### L-4.2 The learner flagged the clock design
Verdict: CONFIRMED
Evidence: JSONL 149, 16:49:29, two lines: ``no, i don't like the clock pattern you use.`` / ``i need time to set the env up every time. on top of that, i'm not guaranteed to see the message instantly. the nature of our communication is asynchronous.`` Trainer logged a correction, events.md line 21.
Bears on: the practice-item clock rule.

### L-4.3 These two are the learner's communication flags
Verdict: PARTLY
Evidence: other objections or procedure questions in the learner messages:
- JSONL 161, 16:51:33: the learner asks how to adapt to running from the workspace root and whether a folder parameter is needed for every command (verbatim in the excerpts file). Trainer withdrew its advice, events.md line 22.
- JSONL 235, 17:25:44: ``wait, there was no cap?``
- JSONL 274, 17:53:23: ``i explicitly let you assume i started on your message, sorry for no notification``
- JSONL 331, 18:13:18: probe time limit unfair (P-4.6).
- JSONL 358, 18:17:48: ``but why aren't you the one to set up the units and such? make zero sense to me that you, the trainer, do not handle the real training material, the process, etc.. all of those are your calls to make.`` This one is outside both named flags.
Whether 161, 235, 274 and 331 fall under "the clock design" depends on the reading; 358 does not.
Bears on: the communication paragraph of the account.

## Where the sources contradict the account

- **L-1.5**: the account lists enum design as held in the probe. The probe specs supply the enum (p3 spec: `Status` stays as written; p1 `Token` in locked source) or use `Option` (p2).
- **L-1.2**: exhaustiveness held where a locked test forbids `_` (p3). The attempt-return `enum_form.rs` saved 17:52:37, 2.6 min before staging, still ends `fault_code` with `_ => { None }`.
- **L-1.1 and A-6**: L-1 says four of five. A-6 itemises six predictions with five right (flat wrong, enum right, four more right). The two blocks count different units.
- **L-2.3**: the cause "incomplete reading of the spec" is not in any source. The learner's recorded words are ``did enum variant, not the struct.`` and ``clock ran out``.
- **P-4.1 to P-4.5**: "go-based" holds for p1 only; no "go" was sent for p2 or p3. Recomputed from learner messages: 3.21, 1.20, 11.60, total 16.02, against 3.4, 1.1, 11, 15.5.
- **P-3.6**: the tool origin is the stage event cut to the minute, 17:55:00, not the stage instant 17:55:14. Stage to grade is 18.20 min, the tool reports 18.44.
- **Trainer message, not an account block**: JSONL 300, 17:55:19, ``The cap check uses the go-based figure.`` probe.py:254-255 judges `over_cap` against `total_minutes`, the stage-to-grade span. The recorded `over_cap=yes` came from the tool span. The go-based totals (15.5, 16.02) are also over 10.
- **L-4.3**: the learner raised at least five further objections or process questions (JSONL 161, 235, 274, 331, 358); the block names two.

## Counts

| Verdict | Count |
|---|---|
| Confirmed | 33 |
| Refuted | 1 |
| Partly | 13 |
| Unverifiable | 0 |
| Not judged | 3 |
| Total assertions | 50 |

Unverifiable sub-parts inside Partly verdicts: held-out share of fraction (P-2.4), whether the learner closed any assistant (P-5.8), the learner's reason for the unwritten struct half and the missing constructors (L-2.3), recurrence across sessions (L-2.4).
