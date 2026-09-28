# P3 hint review, u01–u03

Reviewer: fresh opus instance, 2026-09-28. Wrote no item. Inputs: `training/rust/items/README.md`; each unit's `hints.yaml`, `example.md`, `attempt.md`, the `spec.md`, stub and `key/` of every hinted problem; fable-plan.md § 4 P3 row (line 74) and § 6 O7 (line 113).

## Totals

- Levels reviewed: 36 (3 units × 4 problems × 3 levels).
- SAFE: 32 (of which 6 borderline, marked "borderline" in reason).
- LEAKS: 3. u01 unshown L3, u03 reuse-1 L3, u03 reuse-2 L3.
- USELESS: 1. u03 reuse-2 L2.
- Plan gate (line 74, "marks any level that states the solution: 0"): not met. 3 levels leak.

## Line used

- LEAKS: the level names the specific API or construct *and* the argument or target it applies to, so what remains is transcription.
- SAFE, borderline: names a construct or type but leaves at least one derivation to the learner, such as where it goes, what to pass, or how many sites.
- The line is mine. A stricter reader would move u01 reuse-2 L3 and u03 unshown L3 to LEAKS. A looser reader would call u03 reuse-1 L3 SAFE, because example.md subgoal 3 shows the same move in full.

## Verdicts

| unit | problem | level | verdict | reason | rewrite |
|---|---|---|---|---|---|
| u01 | attempt | 1 | SAFE | Points at the three errors' labels and the order the lines run. | |
| u01 | attempt | 2 | SAFE | Names the conflict without the move. Mislabel: the callee_side fix is subgoal 2 (the parameter type), not subgoal 3. | |
| u01 | attempt | 3 | SAFE | Four rules. Which rule fits which function, and the edit, stay with the learner. | |
| u01 | reuse-1 | 1 | SAFE | Points at E0502's labels and the last use of the borrow. | |
| u01 | reuse-1 | 2 | SAFE | Borderline. "a reference, not a number" nearly says "take the number", but it names no operation. | |
| u01 | reuse-1 | 3 | SAFE | Borderline. States the borrow rule and that u32 is Copy. Where to copy the value out is left open. | |
| u01 | reuse-2 | 1 | SAFE | Points at the E0382 note. That note may state the fix itself (unverified, no cargo run). | |
| u01 | reuse-2 | 2 | SAFE | A question about what deliver needs. The answer comes from the learner. | |
| u01 | reuse-2 | 3 | SAFE | Borderline. States the ownership rule and that a String lends as &str. The signature change and the call-site borrow are still to derive. | |
| u01 | unshown | 1 | SAFE | Points at E0507 and rules out the compiler's two helps. | |
| u01 | unshown | 2 | SAFE | Prunes dead ends (reordering, the example). Weak but actionable. | |
| u01 | unshown | 3 | LEAKS | Names the module (std::mem), the operation (swap a new value in, take the old one out) and the value to put in (an empty Vec). Only the function's name is left to look up. | Through a mutable reference the field must hold a valid Vec at every moment, so the old Vec can leave only in the same step that something valid takes its place. Search the standard library docs for a function that does that exchange through a mutable reference. |
| u02 | attempt | 1 | SAFE | Borderline. An oblique question aimed at the flat form: which struct values do the constructors never build. It gives nothing to a learner stuck on the enum form. | |
| u02 | attempt | 2 | SAFE | Points to subgoal 1. Mostly restates the spec, but "different data or none" pushes the flat form toward a kind tag. | |
| u02 | attempt | 3 | SAFE | Enum versus struct rule. It implies a tag field but leaves the design. | |
| u02 | reuse-1 | 1 | SAFE | Points at the failing test against the spec's rule. | |
| u02 | reuse-1 | 2 | SAFE | Concept (arm order). It presumes an ordering bug, so a learner who misses a boundary (64/65, 2/3, 9/10) is misdirected. | |
| u02 | reuse-1 | 3 | SAFE | Pattern syntax the example already shows (`d @ 1..=3`). Ranges, boundaries and order are left to the learner. | |
| u02 | reuse-2 | 1 | SAFE | Points at what data each variant must hold. | |
| u02 | reuse-2 | 2 | SAFE | Names subgoals 1 and 3 and the special case, without the arm. | |
| u02 | reuse-2 | 3 | SAFE | The variant shapes it describes are already in spec.md. The guard rule is stated, not the guard. | |
| u02 | unshown | 1 | SAFE | Points at the concept: one match over two values. | |
| u02 | unshown | 2 | SAFE | Counts the cases. The spec already implies the 4/8 split. | |
| u02 | unshown | 3 | SAFE | Borderline. Names the tuple scrutinee, the unit's unshown piece, and position binding. The four arms and the realisation that a catch-all can return the bound door stay with the learner. | |
| u03 | attempt | 1 | SAFE | Maps variants to code lines. It does not say how each is produced. | |
| u03 | attempt | 2 | SAFE | Names subgoal 3 and the two foreign failure types. | |
| u03 | attempt | 3 | SAFE | States the rule, but inaccurately: `?` accepts any error convertible by From, not "only" the function's own type. This contradicts u03 unshown L3. | |
| u03 | reuse-1 | 1 | SAFE | Points at the failing test and where the input failed. | |
| u03 | reuse-1 | 2 | SAFE | Concept (one variant per step). Mislabel: the content is subgoal 3, not subgoal 2. | |
| u03 | reuse-1 | 3 | LEAKS | Names the API (map_err) and the argument (the tuple variant's name). With L2 this gives both parse lines verbatim. example.md shows the same line, so the marginal leak is small. | Subgoal 3 of the example shows how a parse error becomes a variant before the question-mark operator sees it. Compare what BadX and BadY take and give back with what that conversion needs. |
| u03 | reuse-2 | 1 | SAFE | Points at the spec's three failures and what detects each. | |
| u03 | reuse-2 | 2 | USELESS | "The subtraction is one of them." spec.md already says this ("Detect it with the subtraction itself: u64::checked_sub"). Nothing new to act on. | Subgoal 3, convert each failure. Put the question-mark operator straight after the subtraction, then read what the compiler says it found and what the function needs. |
| u03 | reuse-2 | 3 | LEAKS | A step sequence: checked_sub gives an Option, ok_or turns it into a Result, and the value passed carries fields. That is the Insufficient line in full. | checked_sub answers with an Option and the function answers with a Result. Subgoal 3 of the example shows how to cross from one to the other. Insufficient needs both numbers, and both are in scope on that line. |
| u03 | unshown | 1 | SAFE | Points at the compiler message for ReadError::from. The quoted wording "expect / find" is unverified; the error may be E0277, not E0308. | |
| u03 | unshown | 2 | SAFE | Rules out map_err and places the conversion inside `?`. Concept only. | |
| u03 | unshown | 3 | SAFE | Borderline. Names From::from as the hook, the unshown piece. The two trait impls and their syntax are still to write. | |

## Other findings (not leak verdicts)

- u03 attempt: no level serves `src/explicit.rs`, the form without `?`. A learner stuck there gets nothing.
- u02 reuse-2: no level covers the i32 coordinates to u32 cost step, a likely point to get stuck.
- u01 attempt L2 and u03 reuse-1 L2 name the wrong subgoal (see rows above). The ladder header ties level 2 to "the subgoal where the miss sits", so the mislabel breaks the ladder's own contract.
- u03 attempt L3 and u03 unshown L3 describe `?` in contradictory terms.
- Unverified: I ran no cargo, so the compiler-output claims in u01 reuse-2 L1, u01 unshown L1 and u03 unshown L1 were not checked.
- Process: I read the files with read-only shell `cat`, not only the listed Read and Glob tools. I edited nothing and ran no git commands.
