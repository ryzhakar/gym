# Sensor review: blocks I-1, A-1 to A-7, AR-1 to AR-3

Session 2026-10-01T15-56, unit u02-enums-match, items `attempt` and `attempt-return`. Checker: sensor. Evidence copies and manifest: `evidence/attempt/` (beside this file).

## Sources used

- **Events:** `/Users/ryzhakar/pp/gym/training/rust/sessions/2026-10-01T15-56/events.md`, local time EEST (UTC+3). Cited as `events.md:N`, N = line number.
- **Transcript:** the trainer JSONL. Timestamps are UTC in the file; local = UTC+3, checked: first line 12:56:31Z, `open` event 15:56. Cited as `JSONL line N` (1-based), local time. Verbatim extracts of every cited line: `evidence/attempt/transcript/transcript-excerpts.md`.
- **Workspace:** `/Users/ryzhakar/pp/gym/training/rust/work/2026-10-01T15-56/u02-enums-match/`, file times by `stat`.
- **Bank and tool code:** commit 5c540de, read with `git show`.
- **Recomputation:** scratch copies under `/private/tmp/claude-501/-Users-ryzhakar-pp-gym/ec07cfbc-f770-4796-8634-8de1e1de31b8/scratchpad/sensor/`, rustc 1.91.1, cargo 1.91.1. Nothing written under `training/` besides this file and `evidence/`.

Disclosures:
- The JSONL holds the trainer's write command for the barred `session.md`. My tool-call listing printed its first 1200 characters. They match claims.md blocks I-1 to A-3. I read no more of it.
- `key/` was not opened. Whether held-out tests exist for the `attempt` item is not checked.
- The 16:14 `enum_form.rs` was overwritten later and exists only in the transcript (JSONL line 75). The 16:14 `flat_form.rs` equals the bank stub. The workspace holds the 17:52 versions of both.
- Words such as "should" and "fixed" appear only inside verbatim quotes of the learner.

## I-1

### I-1.1 Unit u02-enums-match was taken from the due `next_unit` row.
Verdict: CONFIRMED.
Evidence: JSONL line 19 (15:56:34), summons status block: `next_unit  u02-enums-match  2026-10-01`. JSONL line 39 (15:56:50), fresh `gym train status`: same row, only row in "Due queue". `events.md:2`: `trainer | start | unit=u02-enums-match`. Rule, `git show 5c540de:.claude/agents/gym-trainer.md`: "Take the unit from a due `revisit` row, else a due `next_unit` row".
Bears on: the unit-pick rule; the due queue row for u02-enums-match.

### I-1.2 No `delayed_probe` was due on 2026-10-01; u01's falls on 2026-10-07.
Verdict: CONFIRMED.
Evidence: JSONL line 19, status tail: `2026-09-30T18:24 | manager | queue | unit=u01-own-move-borrow kind=delayed_probe due=2026-10-07`. "Due queue" lists no `delayed_probe`. JSONL line 70 (15:57:41), trainer: "The u01 delayed probe is due 2026-10-07, so none is due today."
Bears on: the due queue; the u01 delayed_probe row.

### I-1.3 Baseline b6-enum is a predict-output item.
Verdict: CONFIRMED.
Evidence: `git show 5c540de:training/rust/items/baseline/b6-enum/spec.md`: title `b6-enum · predict the output`; `Edit: prediction.txt`; "Write its exact stdout into `prediction.txt`".
Bears on: item bank entry baseline/b6-enum.

### I-1.4 The learner passed b6-enum in session 2026-09-30T15-40.
Verdict: CONFIRMED.
Evidence: JSONL line 44 (15:56:55), trainer's grep of the 2026-09-30T15-40 events: `2026-09-30T17:19 | trainer | attempt | unit=baseline item=b6-enum result=pass minutes=2.15`. The five other baseline items read `result=fail` in the same output. Status, JSONL line 39: `baseline  pass`.
Bears on: the baseline attempt event for b6-enum in session 2026-09-30T15-40.

### I-1.5 So the learner was not a novice in the unit.
Verdict: PARTLY.
Evidence: Rule, `git show 5c540de:.claude/agents/gym-trainer.md`: "a novice in the unit (a learner whose baseline item on it failed)". b6-enum passed (I-1.4). No file I may read maps b6-enum to u02-enums-match: `git grep -n -i b6 5c540de` outside `key/` hits only `baseline.py:39` and b6's own files. The program in `b6-enum/stub/src/main.rs` uses enum variants, `match`, a guard, a range and `n @ 1..=3`, the constructs of u02's example. The rule applies if b6-enum counts as the baseline item on u02; that mapping is inferred from content, not recorded.
Bears on: the novice rule in the trainer definition; the mapping of baseline items to units.

### I-1.6 The block was written from the events logged and the workspace read; no line comes from the learner's account.
Verdict: PARTLY.
Evidence: Confirmed part: the work-state facts in A-1, A-2 and AR-2 come from the trainer's own reads and runs: JSONL line 75 (16:14:25, `stat`, `cat`, `cargo test`), line 79 (16:15:40, scratch run), line 266 (17:52:51, `stat`, `cat`, `cargo test`). Not confirmable: how the narrative author worked; no source records it. Lines that report learner statements exist in these blocks and are sourced from learner messages: A-1.2 (line 71), A-3.3 (line 149), A-6 (lines 101, 113, 121, 129, 137), AR-1.4 (line 274). If "the learner's account" means the learner's own report of their work, the work-state facts do not rest on it. If it means anything the learner said, the blocks cite it in four places.
Bears on: the provenance statement of the session narrative.

## A-1

### A-1.1 The attempt was presented at 15:57.
Verdict: CONFIRMED.
Evidence: `events.md:3`: `2026-10-01T15:57 | trainer | present | unit=u02-enums-match item=attempt request=none`. JSONL line 66 (15:57:29), same line printed by `gym train log`. JSONL line 70 (15:57:41), item text posted: "The item starts at 15:57."
Bears on: the `present` event for item attempt.

### A-1.2 At 16:14 the learner wrote that the enum form was done and the struct form was not.
Verdict: CONFIRMED.
Evidence: JSONL line 71 (16:14:19), learner: "did enum variant, not the struct."
Bears on: the learner's first message after the attempt.

### A-1.3 At 16:14 `enum_form.rs` held `Temperature(i32)`, `Fault(u8)`, `Off`.
Verdict: CONFIRMED.
Evidence: JSONL line 75 (16:14:25), `cat src/enum_form.rs`: `pub enum Reading { Temperature(i32), Fault(u8), Off, }`. Constructors `temp(celsius: i32)`, `fault(code: u8)`, `off()` match line 12 of the bank `attempt.md`. File mtime then 16:14:04.
Bears on: `attempt/src/enum_form.rs` at 16:14.

### A-1.4 That shape is right.
Verdict: NOT JUDGED (OPINION). The facts under it: A-1.3, and 5 of 7 selected enum-form tests passing including the structure test `enum_form_is_an_enum` (A-2.3).
Bears on: the enum type definition in `enum_form.rs`.

### A-1.5 `flat_form.rs` was untouched at 16:14.
Verdict: CONFIRMED.
Evidence: JSONL line 75: `15:57:25 src/flat_form.rs`, the same mtime as `lib.rs`, `visible.rs` and `Cargo.toml` copied at staging; `enum_form.rs` reads 16:14:04. I split the `cat` output of that line and compared the `flat_form.rs` section with `git show 5c540de:training/rust/items/u02-enums-match/attempt/src/flat_form.rs` by script: byte-identical.
Bears on: `attempt/src/flat_form.rs` at 16:14.

### A-1.6 So `cargo test` did not compile, from unresolved imports.
Verdict: CONFIRMED.
Evidence: JSONL line 75: `error[E0432]: unresolved imports u02_attempt::flat_form::fault, ...fault_code, ...label, ...off, ...temp` at `tests/visible.rs:4:38`; `could not compile u02-attempt (test "visible") due to 1 previous error`. Recomputed on a scratch copy built from the bank crate, the 16:14 `enum_form.rs` and the bank `flat_form.rs`: same E0432. `events.md:4`: `build ... result=compile-error`.
Bears on: the `cargo test` run on the attempt crate at 16:14.

## A-2

### A-2.1 `label` had the hot and freezing branches swapped.
Verdict: CONFIRMED.
Evidence: JSONL line 75, `enum_form.rs` lines 22-24: `if degrees < 0 { format!("hot {degrees}") } else if degrees >= 30 { format!("freezing {degrees}") }`. Spec, `attempt.md`: 30 or above gives "hot <c>", below 0 gives "freezing <c>". Scratch run (A-2.3): `left: "hot -1" right: "freezing -1"` and `left: "freezing 30" right: "hot 30"`.
Bears on: `label` in `attempt/src/enum_form.rs` at 16:14.

### A-2.2 `fault_code` ended in a `_ => None` arm.
Verdict: CONFIRMED. The file reads `_ => { None }` with braces. Same meaning.
Evidence: JSONL line 75, `enum_form.rs`: `match r { Reading::Fault(code) => {Some(code)} _ => { None } }`. The final file, `evidence/attempt/src/enum_form.rs` line 17, holds `_ => { None }` too.
Bears on: `fault_code` in `attempt/src/enum_form.rs`.

### A-2.3 A scratch copy of the trainer's, with `flat_form` stubbed, gave 4 of 6 enum behaviour tests green.
Verdict: CONFIRMED.
Evidence: JSONL line 78 (16:15:38), command: scratch copy, `printf 'pub use crate::enum_form::*;\n' > $S/src/flat_form.rs`, `cargo test enum_form`. JSONL line 79 (16:15:40): `fault_codes ok, faults ok, off_label ok, plain_temp ok, freezing_below_0 FAILED, hot_from_30 FAILED`; `test result: FAILED. 5 passed; 2 failed`. The 7th selected test is `enum_form_is_an_enum`, a structure test, ok. I rebuilt the crate from the bank files and the 16:14 `enum_form.rs` in my scratch directory and got the same: 4 of 6 behaviour tests pass, 5 of 7 selected. `events.md:5`: `build ... result=4-of-6-pass`.
Bears on: the scratch test run on the 16:14 enum form; build event `4-of-6-pass`.

### A-2.4 The learner's workspace was left as written.
Verdict: CONFIRMED, with a note on `target/`.
Evidence: Every trainer command that touches the workspace `attempt/` directory: lines 60 and 65 (15:57:24-29, staging: `cp -R` of the bank crate in, `mv attempt.md` in), line 74 (`stat`, `cat`, `cargo test`), line 78 (`cp -R ... attempt/. $S/` into the scratch directory, source read-only), line 257 (`stat` of the two source files), line 265 (`stat`, `cat`, `cargo test`). After staging, none writes `src/` or `tests/`. The scratch copy lived under `.../scratchpad/u02-scratch`. `cargo test` run inside `attempt/` can write `target/`; `target/` mtimes cannot tell the trainer's runs from the learner's. `Cargo.lock` (15:58:44), `target/CACHEDIR.TAG` (15:58:45) predate the trainer's first cargo run in `attempt/` (16:14:25). The trainer also added files elsewhere in the unit workspace: `example.md`, `example-chat.md`, `reuse-1/`, `reuse-2/`, none in `attempt/`.
Bears on: the files under `attempt/src/` and `attempt/tests/`.

## A-3

### A-3.1 Time was logged as 16.65 minutes and over the 10 minute cap.
Verdict: CONFIRMED.
Evidence: `events.md:6`: `attempt ... result=fail minutes=16.65`. `events.md:7` note: "last save 16.65 min after start, over the 10 min cap, unenforced while working". Cap in the item, `attempt.md` last line: "10 minutes, unaided, compiler on. Stop at 10, finished or not."
Bears on: the `attempt` event minutes field; the feedback note of 16:16.

### A-3.2 The figure ran from staging to last save.
Verdict: CONFIRMED.
Evidence: Recomputed: last save 16:14:04 (JSONL line 75) minus staging copy time 15:57:25 (mtime of `lib.rs`, `visible.rs`, `Cargo.toml`, `attempt.md`, same line and workspace) = 999 s = 16.65 min exactly. Other starts give other numbers: from the `date +%s` epoch file written 15:57:29 (JSONL line 65), 16.58; from the item message, JSONL line 70 at 15:57:41, 16.38. Two descriptions of the start exist: `events.md:21` says "from staging", the trainer's message at JSONL line 160 (16:50:07) says "The clock ran from my message to your last save". The number matches the first only.
Bears on: the minutes figure of the `attempt` event; the start mark of the attempt clock.

### A-3.3 The learner objected that setup and message lag are inside that figure.
Verdict: PARTLY.
Evidence: Confirmed: JSONL line 149 (16:49:29), learner: "no, i don't like the clock pattern you use. i need time to set the env up every time. on top of that, i'm not guaranteed to see the message instantly. the nature of our communication is asynchronous." Not confirmed: the message does not name the 16.65 figure, the attempt or the cap. It follows the reuse-1 presentation at JSONL line 148 (16:32:56, "Time runs from 16:32 to your last save") by 16 min 33 s. The link to the attempt's figure is made by the trainer: JSONL line 160, "Agreed. The clock ran from my message to your last save. That included your setup time and your reading delay." and `events.md:21`.
Bears on: the learner's message of 16:49:29; the clock rule for practice items.

### A-3.4 Setup and message lag are inside the 16.65 figure.
Verdict: PARTLY.
Evidence: Inside by construction: the figure starts at staging, 15:57:25, 16 s before the item message (JSONL line 70, 15:57:41). First sign of a cargo process in the crate: `Cargo.lock` 15:58:44, `target/CACHEDIR.TAG` 15:58:45, 79 s after staging and 15 min 41 s before the trainer's first cargo run in `attempt/` (16:14:25). Unverifiable: how much of 999 s was setup or reading delay. No source holds the learner's first read of the message or first edit; `enum_form.rs` carries only its last save, and birth time equals mtime on both source files, so each was replaced at its last save.
Bears on: the composition of the minutes figure.

### A-3.5 A correction was logged at 16:50.
Verdict: CONFIRMED.
Evidence: `events.md:21`: `2026-10-01T16:50 | trainer | feedback | unit=u02-enums-match item=attempt ... note="correction: attempt minutes=16.65 ran from staging to last save and includes env setup and message lag; the over-cap claim is unsupported; fail stands on tests ..."`. JSONL line 156 (16:50:04): the log command.
Bears on: the feedback event of 16:50 on item attempt.

### A-3.6 The fail stands on the tests.
Verdict: CONFIRMED.
Evidence: Recomputed (A-1.6, A-2.3): `cargo test` on the 16:14 state does not compile; with `flat_form` stubbed 2 of 6 behaviour tests fail. No time figure is needed for either.
Bears on: the `attempt` result `fail`.

### A-3.7 The minutes figure does not stand as a measure.
Verdict: NOT JUDGED (OPINION). Facts under it: A-3.2, A-3.4. One more fact: `events.md:6` still carries `minutes=16.65`; no later `attempt` line for this item replaces it. `evidence/attempt/example-chat.md` line 5, written 16:32:44 and last saved 17:08:19, reads "last save 16.65 min after start, cap 10", with no mention of the 16:50 correction.
Bears on: the `attempt` event minutes field; `example-chat.md` line 5.

## A-4

### A-4.1 The feedback named the swapped branches.
Verdict: CONFIRMED.
Evidence: JSONL line 92 (16:16:07), trainer to learner: "`enum_form`, `label`: the branches are swapped. Below 0 returns "hot". 30 and up returns "freezing"." `events.md:7` note: "label has branches swapped: below 0 gives hot, 30 and up gives freezing".
Bears on: the feedback turn of 16:16 and its event.

### A-4.2 The feedback named their two failing tests.
Verdict: CONFIRMED.
Evidence: JSONL line 92: "`hot_from_30` and `freezing_below_0` fail, and the other four behaviour tests pass." `events.md:7`: "so hot_from_30 and freezing_below_0 fail".
Bears on: the feedback turn of 16:16.

### A-4.3 The feedback named the unwritten struct half.
Verdict: CONFIRMED.
Evidence: JSONL line 92: "The struct half is unwritten." `events.md:7`: "flat_form not written".
Bears on: the feedback turn of 16:16.

### A-4.4 The feedback named the compile stop.
Verdict: CONFIRMED.
Evidence: JSONL line 92: "`cargo test` does not compile. The test file imports five functions from `flat_form`, and that file defines none." `events.md:7`: "so cargo test does not compile".
Bears on: the feedback turn of 16:16.

## A-5

### A-5.1 The instruction was a four-subgoal walk on the window-events example.
Verdict: CONFIRMED.
Evidence: Chat turns at JSONL lines 92 (flat vs enum `Event`), 112 ("Subgoal 1, name the cases", "Subgoal 2 prediction"), 120 ("Subgoal 2, cover every case"), 128 ("Subgoal 3, order arms from specific to general"), 136 ("Subgoal 4, bind what the arm uses"), 148 (close). Example: window input events, key, click, scroll, close, as in `example.md` of the bank. `events.md:8, 11, 13, 15, 17, 19`: six `instruction` events.
Bears on: the instruction turns of 16:16 to 16:32; `example.md`.

### A-5.2 One prediction question came before each subgoal.
Verdict: PARTLY. Subgoals 1, 3 and 4 each had one prediction question. Subgoal 2 had two.
Evidence: Subgoal 1: JSONL line 92 (16:16:07), re-asked in other words at line 100 (16:18:46). Subgoal 2: line 112 (16:22:04), missing `Close` arm; line 120 (16:24:12), `Stale(u8)` added, two numbered parts. Subgoal 3: line 128 (16:26:43), `Key(c)` before `Key('q')`, two numbered parts. Subgoal 4: line 136 (16:28:15), `Scroll(1..=3)` using `d`. Five distinct prediction questions, six with the reword. `events.md` lists six `question` lines (9, 10, 12, 14, 16, 18). The definition, `git show 5c540de:.claude/agents/gym-trainer.md`: "asking a prediction question before each".
Bears on: the question turns of the walk; the `question` events 9 to 18.

### A-5.3 Four principles were named: variant carries only its own data; cover every case; order arms from specific to general; bind what the arm uses.
Verdict: CONFIRMED.
Evidence: `events.md:8, 11` `principle="variant carries only its own data"`; `:13` `principle="cover every case"`; `:15` `principle="order arms from specific to general"`; `:17, 19` `principle="bind what the arm uses"`. Exactly these four strings across the six events.
Bears on: the `principle` fields of the instruction events.

### A-5.4 The walk was written to `example-chat.md` in the workspace.
Verdict: CONFIRMED.
Evidence: Workspace file exists, 2583 bytes, mtime 2026-10-01T17:08:19, 30 lines; lines 7-23 record subgoals 1 to 4 with the questions, the learner's answers and the points made. Created by the trainer's command at 16:32:44 (`cat > $W/example-chat.md`, JSONL line 140, result at 141), appended 17:08 with the reuse-1 section (lines 25-30). `events.md:19` note: "record in workspace example-chat.md". Copy: `evidence/attempt/example-chat.md`. Line 5 still carries the retracted over-cap text (A-3.7).
Bears on: `work/.../u02-enums-match/example-chat.md`.

## A-6

### A-6.1 The first question ("what happens") was too vague, and the learner said so.
Verdict: CONFIRMED.
Evidence: JSONL line 92: "What happens in the flat form? What happens in the enum form?" JSONL line 93 (16:18:37), learner: "what do you mean "what happens"? you need to get better at clear non-verbose communication." JSONL line 100 (16:18:46), trainer: ""What happens" was vague."
Bears on: the subgoal 1 question turn.

### A-6.2 It was reworded to compile-or-not.
Verdict: CONFIRMED.
Evidence: JSONL line 100: "1. Flat struct: does it compile? If yes, what is `x`? 2. Enum: does it compile?" `events.md:10`: `question ... request=explain`.
Bears on: the reworded question of 16:18:46.

### A-6.3 The learner held that a struct with all fields required cannot be built, that its fields would need to be `Option`, and that reading `x` off a key press cannot compile.
Verdict: CONFIRMED, with a limit on the third clause.
Evidence: JSONL line 101 (16:21:35), learner: "in currently listed form the struct cannot be instantiated as is since there are required fields. all of them should be options. then you would read event.x, unpack the option enum, and get your value." and "without either of these two i don't see how that code could compile." Limit: the learner took the `Option` form, or the enum, to compile. The "cannot compile" holds for the form as listed.
Bears on: the learner's answer to the subgoal 1 prediction.

### A-6.4 In fact the constructor fills dummies, the read compiles, and the `Option` form moves the check to run time.
Verdict: CONFIRMED.
Evidence: Recomputed with rustc 1.91.1. A struct `Flat { kind: u8, ch: char, x: i32, y: i32, amount: i32 }` built by `key(c)` with zeros compiles and prints `0 a 0 0`. A struct `Opt { kind: u8, x: Option<i32> }` built with `x: None` compiles and `o.x.unwrap()` panics at run time: `called Option::unwrap() on a None value`, exit 101. The trainer's own compile at JSONL line 105 (16:21:58) showed the same classes of result.
Bears on: the flat-struct and `Option` forms of the window `Event`.

### A-6.5 The enum prediction was right.
Verdict: CONFIRMED, on the trainer's reading.
Evidence: Recomputed: reading `e.x` on `Ev::Key('a')` gives `error[E0609]: no field x on type Ev`; also JSONL line 105. The learner's answer at line 101 names no error: "you would match the enum variant and THEN access the field on click." "Right" rests on reading that as "direct access does not compile". `events.md:11`: "learner right on match-then-access".
Bears on: the learner's enum answer; error E0609.

### A-6.6 The learner predicted E0004 on a missing `Close` arm.
Verdict: CONFIRMED.
Evidence: JSONL line 113 (16:24:01), learner: "won't compile: the compiler reports non-exhaustive enum matching." Recomputed: `error[E0004]: non-exhaustive patterns: Event::Close not covered`. The code E0004 is the trainer's (JSONL line 120); the learner did not name it.
Bears on: the subgoal 2 first prediction.

### A-6.7 `Stale(u8)` stops `label` and leaves `fault_code` returning `None`; the learner predicted this.
Verdict: CONFIRMED.
Evidence: JSONL line 121 (16:26:30), learner: "label stops compiling ... that's what it returens [None]". Recomputed on the 16:14 `enum_form.rs` with `Stale(u8)` added: `cargo check` gives `error[E0004]: non-exhaustive patterns: Reading::Stale(_) not covered` at the `label` match only. With a `Stale` arm added to `label`, a test `assert_eq!(fault_code(Reading::Stale(1)), None)` passes. The trainer did not compile this case in the session; it asserted the outcome in chat.
Bears on: the `Stale(u8)` prediction.

### A-6.8 `Key(c)` before `Key('q')` compiles and `q` takes the generic arm; the learner predicted this.
Verdict: CONFIRMED.
Evidence: JSONL line 129 (16:27:50), learner: "should compile, the quit key does not register and return generic handling." Recomputed: `warning: unreachable pattern`, builds, prints `key q`. Not compiled by the trainer in the session; `example.md` of the bank shows the warning text.
Bears on: the subgoal 3 prediction.

### A-6.9 `Scroll(1..=3)` using `d` fails with E0425; the learner predicted this.
Verdict: CONFIRMED.
Evidence: JSONL line 137 (16:32:29), learner: "does not compile on one of the arms referencing a variable that's not in scope". Recomputed: `error[E0425]: cannot find value d in this scope`. The code E0425 appears in `example-chat.md` line 22 and `events.md:19`, not in the chat reply (JSONL line 148). Not compiled by the trainer in the session.
Bears on: the subgoal 4 prediction.

## A-7

### A-7.1 The learner's misconception was that the flat form is not buildable without `Option`.
Verdict: CONFIRMED.
Evidence: JSONL line 101: "the struct cannot be instantiated as is since there are required fields. all of them should be options." Recomputed (A-6.4): the struct is buildable with every field a plain value.
Bears on: the learner's model of the flat struct form.

### A-7.2 The hand-tracking cost of the flat form was met only after the walk.
Verdict: PARTLY.
Evidence: Confirmed: `flat_form.rs` was the untouched stub at 16:14 (A-1.5), so no flat form existed before the walk. The only flat form is the 17:51:53 save: `temperature: Option<i32>`, `fault: Option<u8>`, off as both `None`, final arm `Reading{..} => format!("off")`. The trainer called it "the hand-tracking the example described" (`events.md:44`). Not confirmed: that the learner "met" the cost. No learner message mentions it; the file shows the form, not the learner's view of it.
Bears on: `attempt/src/flat_form.rs`; the cost of the flat form in the worked example.

## AR-1

### AR-1.1 The attempt-return was presented at 17:37.
Verdict: CONFIRMED.
Evidence: `events.md:41`: `2026-10-01T17:37 | trainer | present | unit=u02-enums-match item=attempt-return`. JSONL line 257 (17:37:13) log command; line 261 (17:37:17), message "Next: return to the sensor attempt".
Bears on: the `present` event for item attempt-return.

### AR-1.2 The learner wrote the completion message at about 17:52.
Verdict: CONFIRMED.
Evidence: JSONL line 262 (17:52:44), learner: "done, fixed". Last save of `enum_form.rs` 17:52:37 (JSONL line 266).
Bears on: the learner's message of 17:52:44.

### AR-1.3 No "go" was sent.
Verdict: CONFIRMED.
Evidence: Learner messages in the JSONL between 17:37:17 and 17:52:44: none. Previous learner message JSONL line 242 ("done", 17:36:08, reuse-2); next, line 262. The trainer had asked for one, line 261: "Write "go" when you start and "done" when you stop." `events.md:44` note: "learner sent no go".
Bears on: the clock start for item attempt-return.

### AR-1.4 The learner then said the clock may start at the trainer's message when no "go" is sent.
Verdict: CONFIRMED as to what was said.
Evidence: JSONL line 274 (17:53:23), learner: "i explicitly let you assume i started on your message, sorry for no notification". The text says an earlier permission existed; the "when no go is sent" condition is the trainer's reading. No earlier learner message in this transcript grants it. The nearest earlier message on the subject, JSONL line 149 (16:49:29), objects to the clock starting at the message: "i don't like the clock pattern you use". Whether the permission was given in some other session is not recoverable from the sources. `events.md:46`: "the permission was not in the trainer's record before this message".
Bears on: the clock rule when no "go" is sent; the learner's message of 17:53:23.

### AR-1.5 15.4 minutes stands.
Verdict: CONFIRMED as arithmetic and as the trainer's last word.
Evidence: Recomputed: last save 17:52:37 minus the `present` log time 17:37:13 = 924 s = 15.40 min. From the message time 17:37:17 the result is 920 s = 15.33 min. `events.md:43`: `minutes=15.4`. JSONL line 273 (17:53:23) first called it "an upper bound"; line 277 (17:53:29) and `events.md:46` set it as "the measure, not an upper bound".
Bears on: the minutes field of the attempt-return event.

## AR-2

### AR-2.1 14 of 14 visible tests were green.
Verdict: CONFIRMED.
Evidence: JSONL line 266 (17:52:51): `running 14 tests ... test result: ok. 14 passed; 0 failed`. Recomputed on a scratch copy of the final workspace files: same. The 14 include the two structure tests, which live in `tests/visible.rs`.
Bears on: `cargo test` on the attempt crate at 17:52.

### AR-2.2 `label` in the enum form returns the right branches at 17:52.
Verdict: CONFIRMED.
Evidence: `evidence/attempt/src/enum_form.rs` lines 23-24: `if degrees < 0 { format!("freezing {degrees}") } else if degrees >= 30 { format!("hot {degrees}") }`. `enum_form::hot_from_30` and `freezing_below_0` ok at JSONL line 266.
Bears on: `label` in `attempt/src/enum_form.rs`.

### AR-2.3 `flat_form` uses two `Option` fields with off as both `None`.
Verdict: CONFIRMED.
Evidence: `evidence/attempt/src/flat_form.rs`: `temperature: Option<i32>`, `fault: Option<u8>`; `off()` is `Reading{temperature: None, fault: None}`.
Bears on: the `Reading` struct in `attempt/src/flat_form.rs`.

### AR-2.4 The type admits both fields set, resolved only by arm order.
Verdict: CONFIRMED.
Evidence: Recomputed in a scratch copy, in-module test: `Reading{temperature: Some(5), fault: Some(3)}` builds; `label` returns `temp 5` (first arm wins); `fault_code` returns `Some(3)`. The two functions disagree on that value. Fields are private, so only code in the module can build it.
Bears on: the `Reading` struct and `label` arm order in `attempt/src/flat_form.rs`.

### AR-2.5 The last arm cannot be checked by the compiler.
Verdict: CONFIRMED.
Evidence: `flat_form.rs` line 26: `Reading{..} => format!("off")`, matches every value. Recomputed: adding a third field `stale: Option<bool>` to `Reading` and setting it in `off()` compiles with one warning, `field stale is never read`; the catch-all arm still labels the value "off".
Bears on: the final arm of `label` in `attempt/src/flat_form.rs`.

### AR-2.6 `fault_code` in the enum form still ends in `_ => None` after the cover-every-case instruction.
Verdict: CONFIRMED. File text is `_ => { None }`.
Evidence: `evidence/attempt/src/enum_form.rs` line 17. Instruction on that principle: `events.md:13` (16:24), JSONL line 120. Recomputed (A-6.7): a new variant leaves `fault_code` compiling.
Bears on: `fault_code` in `attempt/src/enum_form.rs`.

## AR-3

### AR-3.1 The result was a pass on the visible tests.
Verdict: CONFIRMED.
Evidence: `events.md:42, 43`: `build ... result=visible-green`, `attempt ... item=attempt-return result=pass minutes=15.4`. AR-2.1.
Bears on: the attempt event for item attempt-return.

### AR-3.2 The held-out tests were not run.
Verdict: CONFIRMED.
Evidence: `events.md:44` note: "held-out not run". The workspace crate holds `tests/visible.rs` only (`ls attempt/tests`). No command in the JSONL names a `heldout.rs` file or opens a `key/` path. The `key/` strings in commands are exclusion filters (`-not -path '*/key/*'`, `grep -v '/key'`) and note text. `ls -R` at 15:56:50 printed file names below `key/` directories, not contents (JSONL line 38). A grep at 18:18 (JSONL line 361) searched planning notes for the word "held-out", not tests.
Bears on: the grading of the attempt-return item.

## Where the sources contradict the account

- **A-5.2:** the account says one prediction question before each subgoal. Subgoal 2 had two. Subgoal 1's was asked twice.
- **A-3.3:** the account says the learner objected that setup and message lag are inside "that figure". The learner's message does not name the figure, the attempt or the cap.
- **A-3.7 and A-5.4:** the account says the figure does not stand and that the walk was written to `example-chat.md`. That file's line 5 still states "last save 16.65 min after start, cap 10", saved at 17:08, after the 16:50 correction. `events.md:6` still carries `minutes=16.65`.
- **I-1.6:** read as "nothing the learner said", the account contradicts itself: A-1.2, A-3.3, A-6 and AR-1.4 report learner messages. Read as "the learner's own report of their work", no contradiction.
- **A-6 and L-1:** A-6 lists six predictions with five right (flat, enum, `Close`, `Stale`, `Key('q')`, `Scroll`). L-1 reads "four of five". The two blocks count subgoal 1 differently; the learner gave five answers (JSONL lines 101, 113, 121, 129, 137). L-1 is outside this review.

## Counts

| Verdict | Count | Assertions |
|---|---|---|
| CONFIRMED | 47 | I-1.1 to I-1.4; A-1.1 to A-1.3, A-1.5, A-1.6; A-2.1 to A-2.4; A-3.1, A-3.2, A-3.5, A-3.6; A-4.1 to A-4.4; A-5.1, A-5.3, A-5.4; A-6.1 to A-6.9; A-7.1; AR-1.1 to AR-1.5; AR-2.1 to AR-2.6; AR-3.1, AR-3.2 |
| REFUTED | 0 | none |
| PARTLY | 6 | I-1.5, I-1.6, A-3.3, A-3.4, A-5.2, A-7.2 |
| UNVERIFIABLE | 0 | none whole; parts inside I-1.6 (the author's process), A-3.4 (size of setup and lag), AR-1.4 (an earlier permission, not asserted by the account) |
| NOT JUDGED | 2 | A-1.4, A-3.7 |

Total: 55 assertions in 11 blocks.

## Summary

55 atomic assertions checked across 11 blocks: 47 confirmed, 0 refuted, 6 partly, 0 unverifiable as a whole, 2 opinions not judged. The partial verdicts: one prediction question per subgoal (subgoal 2 had two), the learner's clock objection (it names no figure), the size of setup and lag, the novice inference, the provenance line, and the hand-tracking claim. The workspace file example-chat.md still carries the 16.65 minute over-cap line that the 16:50 correction retracted.
