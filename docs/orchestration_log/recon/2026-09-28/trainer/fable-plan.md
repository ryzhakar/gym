# Trainer program — plan

Planner: trainer-planner (fable), 2026-09-28. Plan only. Inputs: CLAUDE.md, ground-truth.md, user_deferred_items.md, evidence-map-v3.md, first-protocol.md, rulings-brief.md, events 2026-09-26 lines 99–134, opinion-map.md, maps/rust/README.md and schema.yaml, slice-1-review.md § 3, substrate-audit.md. Claim ids and grades (S R O) are the evidence map's. Bound: stop-yapping, first-principles, cargo-cult-science, simple-made-easy.

Prime directive: the smallest thing Arthur can train with this week, on evidence, with a path to better.

## 1. Object

Goal 1: master hard CS skills, Rust first, with speed, efficacy, efficiency; practice verifiably aligned with the owner's values. Learned = done unaided + it lasts (ruling line 104). Axes: skill per hour, durability, transfer, sustainability (line 113).

A finished program, tested from the learner record alone, never from self-report:

| test | pass condition | axis |
|---|---|---|
| T1 available | any hour, one command opens a bounded session on the next-due unit; nothing to prepare by hand | sustainability |
| T2 unaided | every session ends in a probe with the assistant closed, on held-out isomorphic items, logged per item as pass/fail plus a continuous measure | instrument (N1-r1-01 3 2 1; N1-r3-01 4 1 2) |
| T3 lasts | ≥7-day probes on trained Concepts above the same-form baseline, read per item, never as a fitted curve | durability (N1-r1-09 4 1 2; N1-r1-02 3 1 1) |
| T4 transfers | items needing a component no unit showed, and Question scenarios in a Domain no unit used, above baseline | transfer (N2-r1-06 3 3 2) |
| T5 per hour | practice minutes per unit logged; T3 read against minutes, not sessions | skill per hour (N2-r7-04 4 1 2: gains at equal time) |
| T6 returns | date, duration, gap per session as raw rows; first-unit pass after a gap ≥14 days vs before | sustainability (N6-r3-04 3 1 1 only; nothing verified at week scale) |
| T7 values | judgment drills over map Questions: a Position taken, Arguments given, Values named; graded against the map's Arguments, not against the owner's affinities | Goal 1 alignment clause; map Job 1 |
| T8 honest | the record shows every solution handed over as a breach; assisted scores never enter T3–T5 | N7-r1-01, N1-r1-01, N7-r1-08 (3 3 1): harm replicated ×4 |

Not a mentor (CLAUDE.md): no career talk, no motivation talk; drills, hints, probes, record.

## 2. Pieces

| piece | what it is | rests on (section · claim · S R O) | grade of the ground |
|---|---|---|---|
| P1 trainer agent definition | one agent file: role, turn rules, breach rules, log calls, probe hand-off | N3/N7 · hints never solutions N7-r1-02 (3 1 1), harm N7-r1-01/N1-r1-01/N7-r1-08 · attempt-first N3-r1-02 (4 2 2) with fidelity conditions · Socratic turn N7-r3-04c (3 3 2) · cost-of-offloading feedback N7-r3-02 (3 1 1) · substrate default reveals solutions N7-r2-01 (S2) | strong on harm; weak on gain: hints "harm removed, no gain"; Socratic outcome LLM-assisted |
| P2 curriculum | data file: ordered units, each a Concept cluster or a Question, its form, its Domain; spacing and interleaving rules as data | N2 · subgoal-labeled worked examples N2-r1-05/06 (3 3 2, n=40) · interleaving N2-r1-02 (3 1 2, K-12 field; applied motor −0.01 N2-r5-06) · spacing N2-r1-01 (4 1 2, lab recall) · problem-based practice N2-r3-01 (4 2 2, months) at immediate cost N2-r3-02 | one R=3 study; interleaving field evidence K-12 only; spacing never tested on a learner under a computed schedule |
| P3 drills | item bank per unit: attempt problem, subgoal-labeled worked example, reuse problems, unshown-component problem, isomorphic probe pairs, hint ladder | N2-r1-05/06 · human-authored hints beat generated N3-r3-04, N3-r5-04 (3 2 1 ×2) · exercises on bypassed material N3-r1-07 (2 1 1) | hint-authorship result is the one gym cannot satisfy (Claude alone): pre-authored is the nearest form, untested |
| P4 measurement | scripts over the record: per-axis read-outs, detectability, breach counts | N1 · instrument facts (map § Pareto, instrument facts) · self-report opposite to learning N1-r7-08 (3 1 1) · assisted-format moves assisted score only N1-r4-10 (3 2 2) · calibration unfixable by feedback N4-r6-05 (3 3 1) · one learner detects d ≥ 1.0–1.5 (map § Calibration) | strong on what not to read; nothing measures probe cost per session |
| P5 learner record | append-only value files: sessions, items, turns, confidence (quarantined), queue | N1 checklist (first-protocol § Measure) · answer-vs-hint count tracks the unaided test N7-r3-02 · hint history feeds proactive timing N3-r4-08/09 (3 2 1) · irregular activity: retrospective hours unreliable r=.35 (DP resolution) | grounded on instrument facts; proactive timing non-LLM, one study |
| P6 session logistics | workspace, launcher, probe runner, hooks, closing | substrate-audit: FileChanged hooks, Monitor ≤30 min, no assistant lock-out · watching has no learning-outcome study (N3-r3-06 4 2 0) · interruption warning N6-r5-03 (3 1 1, lab) | substrate facts; watching unproven |
| P7 checks | per-piece acceptance: script gates, fresh-instance learner, blind graders with swapped order | opinion-map § Bias controls (judge ≠ writer; LLM graders favour own output) · learner as adversary N7-r7-07 (S2) | design rules, owner-ratified |

No piece rests on: gaze training (perceptual, no text analogue), mastery learning over video, expert-dialogue tutor (pre-LLM, K-12), gamified portal (D30), elite-coach margin (N5: nothing verified separates elite from adequate; the "elite" in the role name is the owner's framing, not a measured margin).

## 3. Staging

### Stage 0 — first session, this week

Needs: P1 v0, P3 for a baseline set and 3 units, P5 files plus validator, P6 workspace, launcher, probe runner. Nothing else.

Session 0, ~60 min:

1. Baseline, unaided, script-run, 15 min cap: 6 items over the core cluster (ownership and borrowing; lifetimes; Result and `?`; traits and generics; iterators and closures; enums and match). Forms: 2 predict-output, 2 fix-the-compile-error, 2 write-to-tests. Logged per item. Purpose: the value T3 is read against (N1-r3-02); unit 1 = lowest-pass cluster. A selection rule, not a diagnosis (first-protocol: adapt on no unverified diagnosis; structured items hold, N4-r2-05/06).
2. Unit 1, attempt-first: 10 min unaided attempt with the compiler, trainer silent; then instruction built on that attempt: the subgoal-labeled worked example, each step group named by the subgoal, tied to what the attempt did; then 2 problems reusing the subgoals; then 1 needing a component the example did not show. Hints only, from the ladder. ~35 min.
3. Immediate probe: trainer session closed; probe runner presents 3 held-out isomorphic items; 10 min cap; logged as O=1.
4. Close: session row, queue rows (delayed probe for unit 1 due ≥7 days; unit 2 next).

Session n ≥ 1: due delayed probes first, script-run, before the trainer opens; then the next unit; from unit 2 on, reuse problems interleave types from units 1..n, no two consecutive of one type.

### Increments and triggers

| stage | adds | trigger |
|---|---|---|
| 1 | spacing queue sized to the retention target (month-scale revisits); FileChanged hook appending file events to the record; judgment drills from map Questions with ≥2 Positions and Arguments; hint ladder pre-authored for units 4–12 | 3 sessions logged; first ≥7-day probe done; `maps/rust/arguments/` non-empty (r-args-1..4 running) |
| 2 | first per-axis read-out; problem-based block: one multi-session build in a target Domain, probed on the Concepts it exercised; proactive hint timing from the learner's own hint history; cost-of-offloading line in the trainer's turn | 8 units with delayed probes (d ≥ 1.4 detectable, map § Calibration); hint history ≥ 30 rows |
| 3 | within-learner form comparison (attempt-first vs example-first, alternated by unit, procedural vs transfer items read separately); interleaved vs blocked on the learner's own practice (D1 field test) | 16 units (d ≥ 1.03); read-out 1 shows no large harm |
| 4 | orientation drills (place a README or code sample on the Questions it touches) once Positions carry tells; second subject | map tells non-empty (0 today); owner names the subject |

Each increment is a data or script change; the trainer definition changes only when a rule changes.

## 4. Per piece: author, inputs, output, check

Output root: `/Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-28/trainer/`. Tiers: fable = few calls, highest judgment (definitions, reviews); opus = content that must be correct Rust and correct pedagogy, and the live trainer; sonnet = scripts, checkers, blind solves, graders; haiku = format checks only. Recon is disposable; pieces that must persist get a committed home in § 6.

| piece | author | inputs | output | check that accepts |
|---|---|---|---|---|
| P1 trainer definition v0 | fable (one file, every line a rule with its claim id) | this plan; first-protocol checklists; evidence-map § LLM transfer; rulings 120–122; `.manifestos.yaml` form | `trainer/agent/trainer.md` | (a) `prompt-eval` skill report, no critical finding; (b) adversarial run: a fresh sonnet plays the learner for 20 turns, 10 of them extraction attempts (paste my code and fix it; give the answer, I am out of time): 0 solutions handed over, every turn logged with kind; (c) fidelity run: a fresh sonnet plays a learner who attempts first; the trainer's instruction cites the attempt; judged by a fresh sonnet against a 3-line rubric, order swapped |
| P2 curriculum v0 | opus drafts, fable reviews | `maps/rust/concepts/`, `questions/` (core, ≥2 Positions), `domains/`; evidence checklists | `trainer/curriculum/rust.yaml`: units 1–12; each `{id, kind: mechanism|judgment, concepts: [ids], question?: id, domain, form, revisit_at_days}` | script: every id resolves in `maps/rust/`; every unit names its form; a fresh sonnet checks each unit against the N2 checklist and lists violations; 0 violations |
| P3 drills, baseline + units 1–3 | opus (Rust that compiles; subgoal labels; hint ladder); one item pair per author, isomorph by a second opus from the first's spec only | P2 units; the Rust map's Concept text; no source code from elsewhere | `trainer/items/<unit>/` : `attempt.md`, `example.md` (subgoal-labeled), `reuse-1..2/`, `unshown/`, `probe-a/`, `probe-b/` (isomorphs), `hints.yaml` (3 levels, no code), `key/` (reference solutions, tests) | script: `cargo test` green on every key, red on every stub; blind solve by a fresh sonnet from stub and spec alone, key hidden: solvable, rubric unambiguous; a fresh opus reads `hints.yaml` and marks any level that states the solution: 0; isomorph check: a fresh sonnet given probe-a's key cannot pass probe-b without new work (fails on copy) |
| P4 measurement scripts | sonnet | P5 file formats; map § Calibration detectability table | `scripts/train/readout.py`: per-axis tables, breach count, detectable d at current n | unit tests on synthetic records; a fresh sonnet reads the output and confirms no assisted or confidence row enters an axis |
| P5 learner record | sonnet (validator + log CLI), fable sets the format | first-protocol § Measure checklist | `training/rust/record/` (home, § 6): `sessions.csv`, `items.csv`, `turns.csv`, `confidence.csv`, `queue.csv`; `scripts/train/log.py`, `scripts/train/check_record.py` | validator refuses a malformed row; hand-typed timestamps refused (event-lines convention); round trip on session 0 |
| P6 logistics | sonnet | substrate-audit; conventions (python via uv) | `scripts/train/session.py` (open: due probes, then spawn trainer with unit and record tail; close: queue), `scripts/train/probe.py` (presents items, times, logs; refuses to open `key/` during practice), `training/rust/` cargo workspace, one crate per unit | dry run with a fresh sonnet as learner end to end; the trainer process is not running during the probe (checked by the script's own log); permission deny rule on `key/` for the trainer session |
| P7 checks | as listed | — | check logs beside each piece, `trainer/checks/<piece>.md`: who checked, which model, swapped order, verdict | a check with no model named is void (map § Bias controls 4) |

Trainer runtime model: opus by default (long sessions, tool use, cost); fable where the owner allows. Every session row records the model.

## 5. Measurement

What gets logged each session (raw rows, appended, never edited):

| file | row | fields |
|---|---|---|
| sessions | one per session | date, start, minutes, gap_days since last, units, trainer model, probe_minutes, assistant_closed (learner attests; no lock-out exists), interruptions |
| items | one per item attempt | item id, unit, kind (baseline / practice / probe-immediate / probe-delayed), delay_days from the unit's practice, pass, continuous (tests passed fraction; compile errors; predicted-output edit distance), minutes, attempts |
| turns | one per trainer turn | session, n, kind (hint-1/2/3, question, feedback, instruction, answer=breach), at which item and minute, learner request kind (hint / answer / explain) |
| confidence | one per probe item, quarantined | confidence 0–4; never joined to an axis (N1-r7-04, N1-r7-08, N4-r6-05) |
| queue | one per due event | delayed probe due date per unit; revisit due date; next unit |

Per axis:

- Skill per hour: immediate-probe pass fraction and continuous measure per unit, over practice minutes. Same-session only, O=1. Reported beside T3, never instead of it (rankings reverse, N1-r6-05/06).
- Durability: delayed-probe pass on isomorph b at ≥7 days, per item, beside the immediate result on isomorph a. First probe on any unit ≥7 days. A delayed probe relearns (N1-r3-06, unverifiable): one delayed probe per unit, then the unit enters the spacing queue.
- Transfer: unshown-component items per unit; judgment drills on a new Domain scenario for a known Question (Stage 1). Graded by script where tests exist; by two fresh sonnets, swapped order, rubric from the map's Arguments where not; agreement logged.
- Sustainability: T6 rows only. Nothing verified at week scale; the plan claims nothing here for months. Landmark restarts (N6-r3-04) logged as a datum, not designed for.

Caveats the read-out prints every time: n units with delayed probes and the smallest detectable d (8 → 1.4; 12 → 1.2; 16 → 1.03); baseline vs post confounded by everything (no control condition before Stage 3); breach count; assisted rows excluded; confidence excluded; self-report excluded. Cost per probe: actual minutes logged so the 10-minute cap gets a figure (no claim measures it).

## 6. Open points, defaults, grounds

| # | point | default | ground |
|---|---|---|---|
| O1 | home of the learner record and workspace | `training/rust/`, committed; memento schema gains a `learner` kind (tier journal, verification witnessed, home `training/{subject}/record/`) on the owner's word; until then the files are still committed there | records count durable only once committed (conventions); schema amended on the owner's word alone (memento.yaml); recon is gitignored |
| O2 | session length | ~60 min, probe ≤10 min, hard stop; shorter sessions allowed, never longer | irregular bursts (line 115); probe cap is the first-protocol default, unmeasured |
| O3 | first delayed probe | ≥7 days after the unit | O=2 rubric; no measured cost |
| O4 | feedback timing | end of attempt, fixed for Stage 0–1, recorded | no verified timing value (N3 gaps) |
| O5 | first cluster and Domain | core; unit 1 = lowest baseline pass | core has 209 Questions, most Concepts; target Domains later |
| O6 | trainer runtime model | opus | cost and latency; owner may raise to fable |
| O7 | hint authorship | pre-authored ladder per item, reviewed by a fresh instance; in-session improvisation logged as `hint-improv` | human-authored beat generated ×2 (N3-r3-04, N3-r5-04); pre-authored is untested; logging lets Stage 2 compare |
| O8 | Arthur's own projects as practice | not in Stage 0; Stage 2 problem-based block uses a fresh build in a target Domain, probed on its Concepts | problem-based durability (N2-r3-01) at immediate cost; ruling 118 "building real things"; unprobed project work is O=0 |
| O9 | watching | Stage 0: the trainer reads the workspace on each turn and when the learner points at a spot; Stage 1: FileChanged hook appends events to the record; no proactive interruption | ruling 122; watching has no learning-outcome study; raters agree on where to intervene barely above chance (N3-r6-07, S2) |
| O10 | judgment drill grading | two fresh sonnets, swapped order, rubric = the Question's Arguments; disagreement → unresolved, not adjudicated by the trainer | map § Bias controls; no verdicts on taste |
| O11 | language of drills | English; Ukrainian items only if the owner asks | map batch 1 English only |
| O12 | the map's thinness | curriculum v0 takes Concepts from core Questions and Questions with ≥2 Positions and Arguments (5 today, more as r-args lands); Concept frequency across Questions is not read as importance | 275 of 401 Questions single-Position; 0 Arguments at review time; sampling artifacts |
| O13 | breach handling | a handed-over solution voids the unit's probes for the axes and the unit is re-authored | T8 |

Owner-set, recommended only: trainer manifesto stack. Recommend stop-yapping (ruling 121: blunt, terse, clear) and cargo-cult-science (never claim learned; report every breach and doubt). Recommend against simple-made-easy on the trainer: a bound Value lean would grade judgment drills toward one Position; the map forbids verdicts on tradeoff or taste. Recommend against first-principles on the trainer: it pulls toward lecturing over hint-giving. Purposes to write are the owner's.

## 7. Validity threats

| threat | how it fools the plan | what the plan does; residual |
|---|---|---|
| assisted contamination | a second Claude, a search, or the trainer left open during a probe; no lock-out exists | attestation logged; probe runner separate from the trainer; residual: rests on the learner |
| the author grades itself | the same model family writes items, hints, probes and grades judgment drills; LLM graders favour own output | fresh instances, swapped order, model named per check; residual: same family, correlated blind spots |
| isomorph illusion | probe b is probe a with names changed; a pass is recall of a | isomorph check (copy of a's key fails b); residual: judged by a model |
| small n | 8 units detect d ≥ 1.4; literature effects 0.2–0.7; a null read-out means nothing for months | read-out prints detectable d; no method dropped on a null before Stage 3 |
| pre/post confound | baseline to post improves from anything: compiler exposure, the owner's day job, regression from a low baseline | Stage 3 within-learner alternation; residual: no control learner |
| probe as relearning | each delayed probe teaches; durability inflates | one delayed probe per unit; then spacing queue |
| cargo-cult checklists | every N2/N3 box ticked, no learning: the forms are copied from K-12 and lab; adults, CS-adjacent, ≥7 days: zero verified claims | read-outs are the only claim; the checklists are hypotheses under test, marked so in P2 |
| LLM default reveals solutions | attempt-first depends on the assistant not doing this (N7-r2-01); the harm mechanism is copying | breach rule, adversarial check, `key/` denied; residual: a breach in prose, not code |
| generated hints | the verified-weaker form is the only one available | pre-authored and reviewed; improvisation logged; residual: untested |
| self-report leaks | the owner says it works; the trainer's impression; confidence | quarantined columns; T1–T8 read from record only |
| owner shaping the product | ruling 120: traits must not shape the end product; the plan calibrates order and feedback style only | curriculum rules are generic; the record shows which units were chosen by baseline, not preference |
| map thinness | Concept lists reflect batch-1 sampling (core 49% unseen); a curriculum built on them inherits the holes | O12; units carry the map's provisional mark; Stage 4 waits for tells |
| interleaving in the field | applied-setting motor null (N2-r5-06); the cognitive field RCT is K-12 | Stage 3 tests it on the learner's own practice |
| Hawthorne and the hook | watching may change behaviour, not learning; size unknown (N3-r3-06) | events logged, not acted on, until an outcome comparison exists |
| "elite" without a margin | nothing verified separates an elite coach from an adequate one on a learner outcome (N5) | the role name is the owner's; no claim of margin in P1 |
| planner by analogy | this plan resembles tutoring systems; resemblance is not evidence | each piece cites its claim and grade; a piece with no claim is marked a default |
| horizon | sustainability cannot be measured this month; the program may fail on T6 while passing T2–T5 | T6 rows from session 0; no verdict on sustainability before a 14-day gap has happened |

---

Notification summary: Session 0 is a 60-minute unit — a 15-minute unaided script-run baseline over six core Rust Concept items, one attempt-first unit with a subgoal-labeled worked example, reuse and unshown-component problems under hints only, then a 3-item unaided probe with the trainer closed, all logged as raw rows; it needs the trainer definition v0, three units of items with hint ladders and isomorphic probes, the record files, a probe runner and a launcher, nothing else. Stages add spacing, hooks and judgment drills at 3 sessions, read-outs, a problem-based build and proactive hint timing at 8 delayed-probed units, within-learner form comparisons at 16, and map-orientation drills once Positions carry tells. Biggest open point: where the learner record lives — the plan defaults to a committed `training/rust/` with a `learner` kind added to the memento schema on the owner's word, since recon is gitignored and an uncommitted record is not durable.
