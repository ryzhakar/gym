# Independent check, blocks R1-1 to R1-5 and R2-1 to R2-4 (reuse-1, reuse-2), session 2026-10-01T15-56

Checker: practice-items. Peer account: `docs/orchestration_log/recon/2026-10-01/feedback/claims.md`, blocks R1-1..R1-5, R2-1..R2-4. Each block split into atomic assertions.

## Sources used

- **Events:** `training/rust/sessions/2026-10-01T15-56/events.md`, cited `events:<line>`. Local time EEST (UTC+3).
- **Transcript:** trainer JSONL `agent-atrainer-2026-10-01T15-56-8caa8e8a57aecaa9.jsonl`, 364 records. Cited `J<n>` = zero-based record index, then local time. Local = UTC + 3 h. Quotes verbatim.
- **Workspace:** `training/rust/work/2026-10-01T15-56/u02-enums-match/`. File times read with `stat`. Copies in `review/evidence/reuse-1/` and `review/evidence/reuse-2/`, each with `MANIFEST.md`.
- **Commit 5c540de:** `training/rust/items/` (README, `hints.yaml`, `reuse-1/`, `reuse-2/`), `src/gym/train/`, `.claude/agents/gym-trainer.md`. Transcript J31 holds the trainer definition as it read it. It equals the 5c540de file after whitespace trim.
- **Scratch work:** `cargo`/`rustc` 1.91.1 on copies under the session scratchpad, subdirectory `practice-items-checker/`. Nothing written under `training/` except my output and evidence copies. No `gym train` command run.

## Limits and disclosures

- **Shared scratch file overwritten.** A first scratch dump in the shared scratchpad directory was overwritten by another process mid-read, in a different format. I regenerated my own dump from the JSONL in a private subdirectory and re-read every quoted passage from it.
- **Narrative reached me through the transcript.** J352 (18:15:05) holds the trainer's write of its session narrative, which ends in a list of the trainer's own conclusions about items, procedure and tooling. J356 holds its closing message to the learner. A `grep` for "supplied|authored" printed J352 in full. I read neither `session.md` nor any file barred by the common prompt. No verdict below rests on J352 or J356 as evidence.
- **Post-session commit subjects seen.** `git log` printed subjects of later commits. I use one as corroboration in R2-3.3 (commit 7a0e1f4 adds `practice.py`). Its time is after the session closed.
- **Key files not read.** I read no `key/` path. Held-out tests were not run by me. Where a verdict says "right", it rests on spec text, visible and structure tests, and edge tests I wrote in scratch.
- **Reasoning not recorded.** 57 of 58 thinking blocks in the transcript are empty. Trainer intent is visible only in logged notes and messages.
- **Minutes figures.** The trainer computed minutes from a `date +%s` run by its own tool call, not from the learner's "go" message. Gaps: 7.1 s for reuse-1, 4.3 s for reuse-2 (J176 vs J179; J215 vs J217).

---

## R1-1

### R1-1.1 reuse-1 was presented at 16:32

Verdict: CONFIRMED.
Evidence: `events:20` `2026-10-01T16:32 | trainer | present | unit=u02-enums-match item=reuse-1 request=none`. J147 16:32:56 trainer text opens "Right. A variable exists only if a pattern names it." and ends "**Next item: reuse-1.**" with the spec text.
Bears on: event line 20 and the reuse-1 presentation message.

### R1-1.2 The learner's "go" came at 16:54

Verdict: CONFIRMED.
Evidence: J176 16:54:13 learner text: "go". `events:24` `2026-10-01T16:54 | trainer | present | ... item=reuse-1`. The event kind is `present`, not a go mark. The trainer's J179 call wrote it at 16:54:20. Workspace `reuse-1/target/CACHEDIR.TAG` and `Cargo.lock` carry mtime 16:53:40, 33 s before "go": build-tool activity on the crate preceded the message.
Bears on: event line 24; the workspace `target/` and `Cargo.lock` times.

### R1-1.3 The learner stopped at 17:05

Verdict: PARTLY. Last save 17:05:36. Stop message 17:06:10.
Evidence: J196 17:06:15 `stat` output: `17:05:36 src/lib.rs`. Workspace `reuse-1/src/lib.rs` mtime `2026-10-01T17:05:36` (epoch 1790863536.854). Learner message J192 17:06:10: "did not finish, stuck on syntax stuff". Events 26 to 30 carry 17:06. 17:05 holds for the last save only. The words reached the trainer 34 s after it.
Bears on: reuse-1 `src/lib.rs` modification time; event lines 26 to 30.

### R1-1.4 The learner's words were "stuck on syntax"

Verdict: CONFIRMED. Quote truncated.
Evidence: J192 17:06:10, full message: "did not finish, stuck on syntax stuff". The claim's fragment is a verbatim substring. It omits "did not finish," and "stuff".
Bears on: learner message J192.

### R1-1.5 The Rust Book was allowed on practice items

Verdict: CONFIRMED.
Evidence: `training/rust/items/README.md:28` at 5c540de: "Practice items: the same, plus the standard library docs and the Rust Book. Any LLM and AI completion stay forbidden." The README names no item as a "practice item". Its line 27 sets the narrower list for "Baseline and probe items". reuse-1 is neither, so line 28 covers it by exclusion. J188 17:01:29 shows the trainer grepping this same line.
Bears on: items README, section "Tools allowed to the learner".

### R1-1.6 The learner asked about it

Verdict: CONFIRMED.
Evidence: J184 17:01:17 learner: "i can use the rustbook, can't i?\ncan't remember the value pattern matching syntax". `events:25` logs the answer as `feedback ... request=explain`. J191 17:01:30 trainer: "Yes. On practice items the Rust Book and the standard library docs are allowed."
Bears on: learner message J184; event line 25.

---

## R1-2

### R1-2.1 `Adult` and `Child` are declared with braces

Verdict: CONFIRMED.
Evidence: `items/u02-enums-match/reuse-1/src/lib.rs:2-3` at 5c540de: `Adult { age: u8 },` `Child { age: u8 },`. Workspace file identical on those lines. `Group(u32)` at line 4 uses parentheses.
Bears on: the `Ticket` enum declaration.

### R1-2.2 The arms used parentheses and `age:` inside them

Verdict: PARTLY. Two of four arms match the description.
Evidence: Workspace `reuse-1/src/lib.rs`, final bytes (copy `evidence/reuse-1/lib.rs`):
```
Ticket::Adult(age: (0..=65)) => 1200,
Ticket::Adult{_} => 800,
Ticket::Child(age: ..3) => 0,
Ticket::Child(_) => 600,
```
`Adult(age: ...)` and `Child(age: ...)` have parentheses with `age:`. `Child(_)` has parentheses and `_`, no `age:`. `Adult{_}` has braces. Lines 11 to 14.
Bears on: the four arms of `price` in reuse-1 `src/lib.rs`.

### R1-2.3 The arms included `Adult{_}`

Verdict: CONFIRMED.
Evidence: line 12 above. Scratch compile of `match t { Ticket::Adult{_} => 800 }`: `error: expected field pattern, found `_`` with help "to omit remaining fields, use `..`".
Bears on: arm 2 of `price`.

### R1-2.4 Parse error; no test ran

Verdict: CONFIRMED.
Evidence: J196 17:06:15 `cargo test` tail:
```
error: expected one of `)`, `,`, `@`, `if`, or `|`, found `:`
  --> src/lib.rs:11:26
error: could not compile `u02-reuse-1` (lib) due to 1 previous error
error: could not compile `u02-reuse-1` (lib test) due to 1 previous error
```
No `running N tests` line. Scratch rerun on a copy of the workspace crate gave the same text.
Bears on: reuse-1 build at 17:06; event line 26 `build ... result=compile-error`.

### R1-2.5 `0..=65` includes 65, which the spec prices 800

Verdict: CONFIRMED.
Evidence: `reuse-1/spec.md:7` at 5c540de: "Adult: 65 or older 800; otherwise 1200." Learner arm 1: `0..=65 => 1200`. An inclusive range ending at 65 contains 65. Visible tests (`tests/visible.rs:5-6`) probe ages 30 and 70 only. Spec line 12: "Held-out tests add the boundaries."
Bears on: reuse-1 `spec.md` line 7; arm 1 of `price`.

### R1-2.6 There was no `Group` or `Staff` arm

Verdict: CONFIRMED.
Evidence: the four arms above name only `Adult` and `Child`. Scratch compile of the same arms rewritten with braces (my construction, syntax only): `error[E0004]: non-exhaustive patterns: `Ticket::Group(_)` and `Ticket::Staff` not covered`.
Bears on: arm set of `price`.

### R1-2.7 Result fail

Verdict: CONFIRMED.
Evidence: `events:27` `attempt ... result=fail minutes=11.27`. Build did not compile; zero tests passed (R1-2.4).
Bears on: event line 27.

### R1-2.8 The time was 11.27 minutes

Verdict: PARTLY. 11.27 reproduces from the trainer's start. From the learner's "go" it is 11.38.
Evidence: J179 tool_use 13:54:20.495Z ran `date +%s`, result 13:54:20.843Z, so epoch second 13:54:20Z. Last save `stat -f %m` integer 14:05:36Z. 676 s / 60 = 11.267, printed 11.27 at J200. Learner "go" at J176 13:54:13.409Z. To integer save: 682.6 s = 11.38 min. To fractional save 14:05:36.854Z: 683.4 s = 11.39 min. J207 17:06:59 trainer text: "Time was 11.3 minutes, from "go" to your last save."
Bears on: event line 27 `minutes=11.27`; the minutes start point.

---

## R1-3

### R1-3.1 No supplied hint was given

Verdict: CONFIRMED.
Evidence: `events.md` holds zero `hint` events (grep `| hint |`, 0 matches over 59 lines). No assistant text between J183 and J214 contains text of the three reuse-1 ladder entries (`hints.yaml:24`, `:26`, `:28`). Phrase search over 15 phrases (14 from the reuse-1, reuse-2 and reuse-2-distance ladders, plus "supplied before authored") found one hit in all assistant text: J135 16:28, the trainer's own "Subgoal 4, bind what the arm uses" heading in the attempt walk, before reuse-1. J207 17:06:59 trainer: "I gave no hint because the supplied hints assume the tests run, and yours stops at the parser." One reply carried a pointer: J191 17:01:30 "The pattern syntax from our walk is in `example-chat.md`", logged as `feedback request=explain` at `events:25`, not as `hint`.
Bears on: event kinds logged for reuse-1; `hints.yaml` reuse-1 ladder.

### R1-3.2 Level 1 says to run the tests and read the wrong price

Verdict: CONFIRMED.
Evidence: `items/u02-enums-match/hints.yaml:23-24` at 5c540de: "level: 1" "Run the tests and read which ticket gets the wrong price. Compare the value you return with the rule for that variant in spec.md." Level 2 (`:26`): "Subgoal 3, order arms from specific to general. For some variant, an arm that matches every value comes before an arm meant for some of them." Level 3 (`:28`): "Arms are tried top to bottom and the first match wins. A field pattern can hold a literal or a range, and n @ followed by a range both tests the value and binds it." Levels 2 and 3 do not mention running tests. Definition line 32 sets escalation 1 to 2 to 3 "after a failed attempt at the level before; never on a request alone".
Bears on: `hints.yaml` reuse-1 ladder.

### R1-3.3 The build stopped at the parser

Verdict: CONFIRMED.
Evidence: R1-2.4. Error text "expected one of `)`, `,`, `@`, `if`, or `|`, found `:`" is a syntax error from the parser. No type-check message appears.
Bears on: reuse-1 build output at 17:06.

### R1-3.4 So level 1 "did not fit"

Verdict: NOT JUDGED (OPINION). Facts under it: R1-3.2 and R1-3.3, both CONFIRMED.
Evidence: none beyond those.
Bears on: fit between `hints.yaml` level 1 and the 17:06 build state.

### R1-3.5 "Supplied before authored" is a rule the trainer was under

Verdict: PARTLY. A rule of this substance exists. The quoted words do not.
Evidence: `.claude/agents/gym-trainer.md:32` at 5c540de (same text at J31): "Give the item's supplied hint before one you compose, logging `source=supplied` for the first and `source=authored` for the second; never compose one while a supplied one stands unused." Exact phrase "supplied before authored": 0 matches in that file and 0 in `git grep` of 5c540de. The rule orders a supplied hint ahead of a composed one. It states no case for giving no hint.
Bears on: the trainer definition, hint rule at line 32.

### R1-3.6 Giving no supplied hint was a deviation from that rule

Verdict: NOT JUDGED (OPINION, a classification). Rule text and facts are in R1-3.1 and R1-3.5.
Evidence: no `hint` event and no composed hint exist for reuse-1. The trainer did give authored `feedback` and `instruction` naming the fault (J207).
Bears on: reuse-1 hint handling against the definition's hint rule.

### R1-3.7 The skip was on purpose and is logged in the instruction note

Verdict: CONFIRMED. The trainer's reasoning itself is not recorded.
Evidence: `events:29` `instruction ... item=reuse-1 ... note="... supplied hint ladder skipped because level 1 assumes the tests run"`. Same text in the J203 call, 17:06:55. J207 repeats the reason to the learner. Thinking blocks around J198 and J202 are empty.
Bears on: event line 29.

---

## R1-4

### R1-4.1 The instruction principle was "pattern mirrors the variant declaration"

Verdict: CONFIRMED.
Evidence: `events:29` (17:06) and `events:31` (17:08) both carry `principle="pattern mirrors the variant declaration"`. Learner-facing wording at J207: "**Principle:** a pattern copies the shape of the variant's declaration." Two `instruction` events exist for this principle.
Bears on: event lines 29 and 31.

### R1-4.2 The prediction offered four patterns against `Click { x, y }` and `Scroll(i32)`

Verdict: CONFIRMED.
Evidence: J207 17:06:59:
```
enum Event { Click { x: i32, y: i32 }, Scroll(i32) }
a. `Event::Click(x, y)`  b. `Event::Click { x, y }`  c. `Event::Scroll { d }`  d. `Event::Scroll(d)`
```
"Which of these compile?" Declared fields are `x: i32, y: i32`; the claim writes `Click { x, y }`, which is pattern b.
Bears on: the prediction question in J207.

### R1-4.3 The learner chose the two valid ones

Verdict: CONFIRMED.
Evidence: J208 17:08:04 learner: "b & d". Scratch compile: `Click { x, y }` and `Scroll(d)` give warnings only. `Click(x, y)` and `Scroll { d }` give errors (R1-4.4).
Bears on: learner message J208.

### R1-4.4 E0164 and E0769 were checked by compiling

Verdict: CONFIRMED.
Evidence: J199 17:06:45 ran `rustc --edition 2021` on four variants. J200 output: `error[E0164]: expected tuple struct or tuple variant, found struct variant `Ev::Click`` for `Click(x, y)`; `error[E0769]: tuple variant `Ev::Scroll` written as struct variant` for `Scroll { d }`. Scratch rerun reproduced both. The check used enum `Ev` with a `_ => 1` arm and ran at 17:06:45, before the learner's answer at 17:08:04. J214 17:08:25: "I checked both by compiling."
Bears on: the compile check at J199; `events:31` note.

---

## R1-5

### R1-5.1 reuse-1 was never re-attempted

Verdict: CONFIRMED, with a limit on what the sources can exclude.
Evidence: Last reuse-1 event is `events:31` (17:08). No later event names `item=reuse-1`. After J208, no learner message mentions reuse; the one later tool call naming reuse-1 is J352 (18:15:05), the narrative write. J214 17:08:25: "`reuse-1` stays logged as fail" and "it is not scored". Workspace `reuse-1/src/lib.rs` mtime still 17:05:36, content equal to J196. Limit one: `reuse-1/target/` holds build files stamped 17:09:43, 4 min 7 s after the last save and 46 s before the reuse-2 "go" at 17:10:29. The author of that build is not determinable from the sources. README line 29 notes rust-analyzer leaves `target/` on open. Limit two: an attempt that left no save cannot show in file times.
Bears on: reuse-1 workspace crate; events after line 31.

---

## R2-1

### R2-1.1 reuse-2 was presented at 17:08

Verdict: CONFIRMED.
Evidence: `events:32` `2026-10-01T17:08 | trainer | present | ... item=reuse-2`. J214 17:08:25 holds the item text, "**Next item: reuse-2.**"
Bears on: event line 32.

### R2-1.2 The learner's "go" came at 17:10

Verdict: CONFIRMED.
Evidence: J215 17:10:29 learner: "go". `events:33` `present ... item=reuse-2` at 17:10, written by J217 17:10:33. Workspace `reuse-2/target/CACHEDIR.TAG` mtime 17:10:02 and `Cargo.lock` 17:09:57, before "go".
Bears on: event line 33.

### R2-1.3 The learner stopped at 17:24

Verdict: CONFIRMED.
Evidence: J226 17:24:27 `stat`: `17:24:05 src/lib.rs`. J222 17:24:21 learner message. Both in minute 17:24.
Bears on: reuse-2 `src/lib.rs` time at the first read; message J222.

### R2-1.4 The learner's words were "clock ran out"

Verdict: CONFIRMED.
Evidence: J222 17:24:21 learner text: "clock ran out".
Bears on: learner message J222.

### R2-1.5 No cap exists in the spec

Verdict: CONFIRMED.
Evidence: `items/u02-enums-match/reuse-2/spec.md` at 5c540de, all 11 lines read; no time limit stated. `git grep -i -E 'cap|minute|clock|timed|time limit'` over `reuse-1/` and `reuse-2/` at 5c540de, `key/` excluded: 0 matches. J237 17:25:51 trainer grep of workspace and item copies: `exit 1`. Items README states no practice cap. The default 10 in `src/gym/train/probe.py:196` (`CAP_MINUTES_DEFAULT = 10.0`) applies to `probe grade` and baseline grade.
Bears on: reuse-2 `spec.md`; items README.

### R2-1.6 The trainer had not said so when presenting

Verdict: CONFIRMED.
Evidence: J214 17:08:25 presentation: closes "Write "go" when you start and "done" when you stop." No statement on a cap. J221 17:10:34: "Clock started 17:10. Write "done" when finished." The first reuse-2 statement is J233 17:25:01: "The spec sets no cap." For contrast J147 16:32:56, reuse-1: "The spec sets no cap."
Bears on: messages J214 and J221.

### R2-1.7 The omission was the trainer's own

Verdict: NOT JUDGED (OPINION, attribution). The fact beneath it is R2-1.6, CONFIRMED.
Evidence: J240 17:25:53 trainer: "I said "no cap" when I presented reuse-1 and left it out for reuse-2. That was my omission."
Bears on: message J240.

### R2-1.8 A correction was logged at 17:25

Verdict: CONFIRMED.
Evidence: `events:37` `2026-10-01T17:25 | trainer | feedback | ... item=reuse-2 request=explain note="correction: reuse-2 spec has no cap and trainer did not say so when presenting it; ..."`.
Bears on: event line 37.

### R2-1.9 The learner continued

Verdict: CONFIRMED.
Evidence: J234 17:25:44 learner: "wait, there was no cap?" J240 trainer: "Keep working on reuse-2." Workspace `reuse-2/src/lib.rs` mtime 17:35:59, 11 min 54 s after 17:24:05. J241 17:36:08 learner: "done". Source differs between J226 and J244 (R2-2).
Bears on: reuse-2 `src/lib.rs` after 17:25; message J241.

---

## R2-2

Source for the first state: J226 17:24:27 `cat src/lib.rs` (27 lines), copy `evidence/reuse-2/lib.rs.state-at-17-24.from-transcript`. The workspace no longer holds it.

### R2-2.1 In the first state the enum was right

Verdict: CONFIRMED against spec, visible and structure tests, and my edge tests. Held-out tests not run by anyone.
Evidence: First-state enum: `Dot(i32, i32)`, `Line{x1: i32, y1: i32, x2: i32, y2: i32}`, `PenUp`. Spec (`reuse-2/spec.md:5`): "Define the type `Command` as an enum", three commands. Scratch: first state plus three constructors plus `.into()` replaced by `as u32`: `command_is_an_enum ... ok`, `every_arm_names_its_variant ... ok`.
Bears on: `Command` declaration in the 17:24 state.

### R2-2.2 In the first state `endpoint` was right

Verdict: CONFIRMED against the same scope.
Evidence: spec line 9: dot ends at its point, line at second point, pen up `None`. First-state arms: `PenUp => None`, `Dot(x, y) => Some((x, y))`, `Line { x2, y2, .. } => Some((x2, y2))`. Scratch tests passed: `endpoint(dot(1,2))`, `line(0,0,5,6)`, `line(5,6,0,0)`, `pen_up()`, plus visible `endpoints`.
Bears on: `endpoint` in the 17:24 state.

### R2-2.3 `cost` converted `i32` to `u32` with `into` (E0277)

Verdict: CONFIRMED.
Evidence: First-state line 23: `let cost: u32 = std::cmp::max(x_length.abs() + y_length.abs(), 1).into();`. J226 output: `error[E0277]: the trait bound `u32: From<i32>` is not satisfied` at `src/lib.rs:23:79`. Scratch rerun on the transcript text: same code and position.
Bears on: `cost` line 23 in the 17:24 state.

### R2-2.4 In the first state `dot`, `line` and `pen_up` were not defined

Verdict: CONFIRMED.
Evidence: First state has `Command`, `endpoint`, `cost`; no `dot`, `line`, `pen_up`. Scratch: first state with only the `.into()` line replaced: `error[E0432]: unresolved imports `u02_reuse_2::dot`, `u02_reuse_2::line`, `u02_reuse_2::pen_up`` at `tests/visible.rs:1:25`. Final state (J244) defines them in lines 29 to 31.
Bears on: function set in the 17:24 state.

### R2-2.5 `Dot(x, y)` bound two unused values

Verdict: CONFIRMED.
Evidence: First-state line 19: `Command::Dot(x, y) => 1,`. Scratch compile: `warning: unused variable: `x`` at `src/lib.rs:19:22` and `y` at `19:25`. Final state line 19 reads `Command::Dot(..) => 1,`.
Bears on: `Dot` arm of `cost` at 17:24.

---

## R2-3

### R2-3.1 At 17:36 visible and structure tests were green

Verdict: CONFIRMED.
Evidence: J244 17:36:13 `cargo test`: `command_is_an_enum ... ok`, `every_arm_names_its_variant ... ok`, `costs ... ok`, `endpoints ... ok`; two `test result: ok. 2 passed; 0 failed`. Scratch rerun on a copy of the workspace `lib.rs` (equal to J244 text): same four tests green. File mtime 17:35:59.
Bears on: reuse-2 final `src/lib.rs`; event line 38.

### R2-3.2 Held-out tests were not run

Verdict: CONFIRMED.
Evidence: `events:40` note: "held-out not run". No trainer tool call touches held-out tests for reuse-2. J244 output lists only `tests/structure.rs` and `tests/visible.rs` plus doc-tests. The locked test files in the workspace carry mtime 17:08:19, the staging time.
Bears on: reuse-2 grading scope; event line 40.

### R2-3.3 No command grades practice items

Verdict: CONFIRMED for the tool as it stood during the session.
Evidence: J248 17:36:19 `gym train --help` lists `open, log, close, status, check, probe, baseline`. At 5c540de `src/gym/train/cli.py:27-32` admits `which` only as `immediate`, `delayed`, `probe-[a-z]`. `probe.py:40-55` resolves to `probe-a`/`probe-b`/`probe-<letter>`. `probe.py:136-137` builds `key/<side>/<problem>`. `baseline.py:34` points at `items/baseline`. No path to `reuse-N`, `attempt` or `unshown`. `src/gym/train/practice.py` is absent at 5c540de. Commit 7a0e1f4 (2026-10-01 20:59:15 +0300, after the 20:42 close at `events:59`) adds it. Items README line 14 documents a by-hand grading procedure that copies `key/<problem>/`; that is not a command.
Bears on: `gym train` command set at 5c540de; items README grading section.

### R2-3.4 `key/` stayed closed

Verdict: CONFIRMED for the trainer.
Evidence: Scan of all 60 trainer tool calls for `key/`, `\bkey\b`, `heldout`, `held-out`. Calls touching item trees exclude key paths: J35 `ls -R training/rust/items | grep -v '/key'`; J42 `find ... -not -path '*/key/*'`. Other hits are text inside log notes and narrative (J256, J268, J352) or the word in another sense: "key press", "key arm", `fn key` (J103, J107, J131, J139). J360 greps `recon/2026-09-28/trainer/` for "held-out|heldout", not `key/`. Definition line 44: "Leave grading to the command; never open, read or print a `key/` path." The `gym train probe grade` call at J333 (18:13:26) reads `key/` by design inside the tool; the trainer did not.
Bears on: trainer tool calls against `training/rust/items/**/key/`.

### R2-3.5 The trainer's scratch test showed `x2 - x1` overflows from `i32::MIN` to `i32::MAX`, a debug panic

Verdict: CONFIRMED.
Evidence: J252 17:36:32 built a copy `u02r2` in the scratchpad with `tests/extra.rs` and ran `cargo test --test extra`. J253: `test wide ... FAILED`, `thread 'wide' panicked at src/lib.rs:21:33: attempt to subtract with overflow`. The test: `cost(line(i32::MIN,0,i32::MAX,0)) == u32::MAX`. Final-state line 21: `let x_length: u32 = (x2 - x1).unsigned_abs();`. My scratch rerun: same panic at 21:33. The learner's workspace was not edited by the trainer's test.
Bears on: `cost`, line 21 of the final reuse-2 `src/lib.rs`.

### R2-3.6 The same input gives a wrong wrap in release

Verdict: CONFIRMED by my run. The trainer ran no release build.
Evidence: No `--release` in any trainer tool call. My scratch `cargo test --release --test extra` on a copy of the final file: `cost(line(MIN,0,MAX,0)) = 1`; the assertion reports `left: 1`, `right: 4294967295`. The spec's horizontal distance for that line is 4294967295. In a release profile `x2 - x1` wraps to -1, and `unsigned_abs` gives 1.
Bears on: release-profile behavior of `cost` for extreme lines.

---

## R2-4

### R2-4.1 Result: pass on visible and structure tests

Verdict: CONFIRMED.
Evidence: `events:38` `build ... result=visible-green`; `events:39` `attempt ... result=pass minutes=25.43`. Tests per R2-3.1. The same session found a failing edge test (R2-3.5), and held-out tests did not run (R2-3.2).
Bears on: event lines 38 and 39.

### R2-4.2 The time was 25.43 minutes

Verdict: PARTLY. 25.43 reproduces from the trainer's start. From the learner's "go" it is 25.51.
Evidence: J217 tool_use 14:10:33.622Z ran `date +%s`, result 14:10:33.870Z, epoch second 14:10:33Z. Last save integer 14:35:59Z. 1526 s / 60 = 25.433. Learner "go" J215 14:10:29.288Z; to fractional save 14:35:59.691Z (epoch 1790865359.691): 1530.4 s = 25.51 min. Same method on the first state: 14:24:05Z minus 14:10:33Z = 13.533, logged 13.53 at `events:35`; from "go" 13.60.
Bears on: event line 39 `minutes=25.43`; event line 35 `minutes=13.53`.

### R2-4.3 The minutes include the pause while the learner read the reply

Verdict: CONFIRMED that the interval contains the exchange. The pause length is not recorded.
Evidence: Interval 17:10:33 to 17:35:59 contains J233 17:25:01 (trainer reply), J234 17:25:44 (learner "wait, there was no cap?"), J240 17:25:53. 43.6 s lie between J233 and J234. Reading time is not separable: only the last save time is recorded, with no save log. J256 17:37:13 events note: "minutes include the pause while the learner read the trainer reply".
Bears on: the reuse-2 minutes window.

---

## Where the sources contradict the account

- **R1-1.3** says "stopped at 17:05". Last save was 17:05:36. The learner's stop message was 17:06:10 and the events carry 17:06.
- **R1-2.2** says the arms used parentheses and `age:` inside them. `Child(_)` has parentheses and `_`; `Adult{_}` has braces. Two of four arms have `age:`.
- **R1-2.8 and R2-4.2** give minutes as from "go". The logged figures start at the trainer's own command, 7.1 s (reuse-1) and 4.3 s (reuse-2) after the "go" messages. From the messages: 11.38, 25.51 and, for the reuse-2 first read, 13.60.
- **R1-3.5** puts "supplied before authored" in quotation marks. The phrase appears in no file at 5c540de. The nearest text is `gym-trainer.md:32`.

Doubts the sources leave open, not contradictions:

- **R1-5.1.** The crate's `target/` shows build files at 17:09:43 with the source unsaved since 17:05:36. Who ran that build is not recorded.
- **R2-2.1 and R2-2.2.** "Right" rests on spec text, visible and structure tests and my edge tests. Held-out tests were not run by the trainer or by me.
- **R1-3.7.** Intent is evidenced by the logged reason only; the trainer's reasoning is not in the transcript.

## Counts

- Confirmed: 41
- Refuted: 0
- Partly: 5 (R1-1.3, R1-2.2, R1-2.8, R1-3.5, R2-4.2)
- Unverifiable: 0
- Not judged: 3 (R1-3.4, R1-3.6, R2-1.7)
- Assertions in total: 49. Per block: R1-1 6, R1-2 8, R1-3 7, R1-4 4, R1-5 1, R2-1 9, R2-2 5, R2-3 6, R2-4 3.
