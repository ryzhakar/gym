# P2 self-check — curriculum v0

Checker: the author, opus (claude-opus-5-5), 2026-09-28. This is self-graded. PLAN:73 requires a fresh sonnet to run the N2 check. This file does not replace that check (PLAN:128: the author grades itself).

Files checked: `trainer/curriculum/rust.yaml`, `trainer/curriculum/baseline.yaml`, by `trainer/curriculum/check.py`.

## Script result

Run with `uv run python docs/orchestration_log/recon/2026-09-28/trainer/curriculum/check.py` from the repo root. Result: 240 PASS, 0 FAIL, 8 WARN, exit 0. Each WARN is a map gap declared in `rust.yaml`, not a defect of the check.

I tested the checker against broken copies, written to the scratchpad only. It exited 1 on each of these breaks: a misspelled concept id, an `after` pointing forward, a judgment unit with extra concepts, a missing form, a form whose kind mismatches the unit, a dropped `needs-arguments`, first revisit at 3 days, and 4 write-to-tests baseline items.

Full output, verbatim, is at the end of this file.

## N2 checklist, applied per unit

Checklist: FP:52–57, as amended by EV:1088–1090 and EV:1108–1110. Items:

- C1 unit shape: a subgoal-labeled worked example, then reuse tasks, then an unshown-component task (FP:52).
- C2 attempt first, instruction second; skipped for domain-general skills (FP:53). Fidelity conditions: instruction built on the attempt; multiple attempts (EV:1088, EV:239).
- C3 interleave once two or more types exist, never two consecutive of one type (FP:54; applied-setting caveat EV:1108).
- C4 return at a gap sized to the retention wanted, month-scale for multi-month retention; log the gap (FP:55; EV:1109).
- C5 log the unit form each session (FP:56).
- C6 no claim that part-task or whole-task order is evidence-backed (FP:57; EV:1110).

Marks: **met** means the curriculum data states it. **spec** means stated here, realized only when P3 authors or P5/P6 log. **viol** means violated. **n/a** means the item does not apply.

| unit | C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|---|
| u01-own-move-borrow | spec | met | n/a when first (one type exists); met after | met | spec | met |
| u02-enums-match | spec | met | met | met | spec | met |
| u03-result-question-mark | spec | met | met | met | spec | met |
| u04-lifetimes | spec | met | met | met | spec | met |
| u05-generics-traits | spec | met | met | met | spec | met |
| u06-closures-iterators | spec; thinnest (no iterator Concept in MAP) | met | met | met | spec | met |
| u07-shared-ownership | spec | met | met | met | spec | met |
| u08-trait-objects | spec | met | met | met | spec | met |
| u09-j-shared-mutable-state | **viol** | met, with a risk | met | met | spec | met |
| u10-j-generics-vs-dyn | **viol** | met, with a risk | met | met | spec | met |
| u11-j-library-panic | **viol** | met, with a risk | met | met | spec | met |
| u12-j-enum-vs-dyn | **viol** | met, with a risk | met | met | spec | met |

Violations and risks, stated in full:

1. **C1 fails for u09–u12.** A judgment drill has no worked example, reuse tasks or unshown-component task. The form comes from T7 (PLAN:21), not from N2. No evidence exists for its learning effect. It is marked `default, unmeasured` in `rust.yaml` forms.judgment-drill. One fix: give each drill a worked Argument, then scenarios in the same Domain, then a scenario in a Domain no unit used. The Arguments must exist first (`needs-arguments`), and the fix stays untested.
2. **C2 risk for u09–u12.** Weighing tradeoffs may count as a domain-general skill, where attempt-first reverses (−0.17, 8 comparisons; FP:53, EV:239). Nothing settles it. The drill keeps its take-a-Position-first order.
3. **C2 fidelity.** The "multiple attempts" condition was missing from the first draft. `forms.attempt-first` now asks for at least two approaches where the problem admits more than one. The "thin generation favours a demonstrated attempt" condition (EV:239) rests on a SURVEYED source only, so the form does not use it.
4. **C3 was first violated for u09–u12.** The draft's interleave rule mixed only mechanism types. It now mixes all practiced units. It depends on P3 supplying unused items and scenarios per earlier unit. If P3 does not, C3 fails in practice.
5. **C4 values unmeasured.** 7/30/90 rests on lab verbal-recall data (N2-r1-01, R=1). 30 matches "≥1 month for ≥6-month retention". 90 is an extrapolation. The first-probe floor of 7 days is O3.
6. **C1–C5 carry no adult, CS, ≥7-day evidence** (EV:247). Every mark above is a hypothesis under test (PLAN:133).

## Deviations from PLAN

- **O5 (PLAN:111), unit 1 = lowest baseline pass:** narrowed to failed clusters whose units are authored. With P3's Stage 0 set of u01–u03, a failed lifetimes, traits or iterators cluster cannot be unit 1. Default: the restriction, so session 0 does not block on authoring. Alternative A: P3 authors the first unit of all 6 clusters (u01–u06) before session 0, about twice the Stage 0 load, and then O5 holds exactly. Alternative B: run the baseline standalone first, then author the promoted unit, which splits session 0.
- **Unit schema:** four fields beyond PLAN:73 (`cluster`, `after`, `status`, `gap`). The reasons are in the `rust.yaml` header.

## Map thinness, declared

- The iterators/closures cluster has no iterator Concept, no Fn-trait Concept, and no core Question with ≥2 Positions (u06).
- There is no Concept for `Result` or `?` (u03), and none for lifetime elision or `'static` in core (u04).
- Duplicate Concept ids: pattern-matching and pattern-matching-2, associated-types and associated-types-2, and five dispatch ids.
- MAP/arguments/ is absent: 0 Arguments, so all 4 judgment units are `needs-arguments`. Upstream r-args chunks (`recon/2026-09-27/research/rust-map/args/chunks/`) name all 4 Questions. That was checked by grep, not read.
- A suspected duplicate Position is listed for generics-vs-dyn-for-abstraction (MAP/README.md Known issues). The compiled map holds 2 Positions of opposite direction.
- Every id is provisional: MAP v0.1 is ungraded, and core is 49.2% unseen (MAP/README.md).

## Process note

To run a negative test, a temporary copy of the checker was written to `trainer/check_neg_tmp.py`, outside the permitted output paths, and deleted in the same command. No other file outside the four outputs was written.

## Full script output

```
PASS  12 units (found 12)
PASS  unit ids unique
PASS  u01-own-move-borrow: no unknown fields 
PASS  u01-own-move-borrow: kind is mechanism|judgment (mechanism)
PASS  u01-own-move-borrow: names a defined form (attempt-first)
PASS  u01-own-move-borrow: form kind matches unit kind
PASS  u01-own-move-borrow: domain resolves (core)
PASS  u01-own-move-borrow: concept resolves (ownership)
PASS  u01-own-move-borrow: concept resolves (move-semantics)
PASS  u01-own-move-borrow: concept resolves (borrowing)
PASS  u01-own-move-borrow: concept resolves (borrow-checker)
PASS  u01-own-move-borrow: concept resolves (copy-vs-clone)
PASS  u01-own-move-borrow: concepts non-empty
PASS  u01-own-move-borrow: revisit_at_days ascending, first >= 7 ([7, 30, 90])
PASS  u01-own-move-borrow: mechanism unit names no question
PASS  u01-own-move-borrow: mechanism unit carries no status
PASS  u01-own-move-borrow: mechanism unit names its cluster
PASS  u02-enums-match: no unknown fields 
PASS  u02-enums-match: kind is mechanism|judgment (mechanism)
PASS  u02-enums-match: names a defined form (attempt-first)
PASS  u02-enums-match: form kind matches unit kind
PASS  u02-enums-match: domain resolves (core)
PASS  u02-enums-match: concept resolves (enums)
PASS  u02-enums-match: concept resolves (sum-types)
PASS  u02-enums-match: concept resolves (pattern-matching)
PASS  u02-enums-match: concept resolves (pattern-matching-2)
PASS  u02-enums-match: concept resolves (exhaustive-match)
PASS  u02-enums-match: concept resolves (option-semantics)
PASS  u02-enums-match: concepts non-empty
PASS  u02-enums-match: revisit_at_days ascending, first >= 7 ([7, 30, 90])
PASS  u02-enums-match: mechanism unit names no question
PASS  u02-enums-match: mechanism unit carries no status
PASS  u02-enums-match: mechanism unit names its cluster
WARN  u02-enums-match: map gap declared: pattern-matching and pattern-matching-2 are one Concept under two ids (texts "pattern-matc
PASS  u03-result-question-mark: no unknown fields 
PASS  u03-result-question-mark: kind is mechanism|judgment (mechanism)
PASS  u03-result-question-mark: names a defined form (attempt-first)
PASS  u03-result-question-mark: form kind matches unit kind
PASS  u03-result-question-mark: domain resolves (core)
PASS  u03-result-question-mark: concept resolves (error-handling)
PASS  u03-result-question-mark: concept resolves (error-propagation)
PASS  u03-result-question-mark: concept resolves (explicit-error-handling)
PASS  u03-result-question-mark: concept resolves (option-unwrap)
PASS  u03-result-question-mark: concept resolves (panics)
PASS  u03-result-question-mark: concepts non-empty
PASS  u03-result-question-mark: revisit_at_days ascending, first >= 7 ([7, 30, 90])
PASS  u03-result-question-mark: after u02-enums-match resolves and precedes it
PASS  u03-result-question-mark: mechanism unit names no question
PASS  u03-result-question-mark: mechanism unit carries no status
PASS  u03-result-question-mark: mechanism unit names its cluster
WARN  u03-result-question-mark: map gap declared: MAP has no Concept for `Result` itself or for the `?` operator; error-propagation is the n
PASS  u04-lifetimes: no unknown fields 
PASS  u04-lifetimes: kind is mechanism|judgment (mechanism)
PASS  u04-lifetimes: names a defined form (attempt-first)
PASS  u04-lifetimes: form kind matches unit kind
PASS  u04-lifetimes: domain resolves (core)
PASS  u04-lifetimes: concept resolves (lifetimes)
PASS  u04-lifetimes: concept resolves (ownership-lifetimes)
PASS  u04-lifetimes: concept resolves (owned-vs-borrowed-types)
PASS  u04-lifetimes: concept resolves (nll)
PASS  u04-lifetimes: concepts non-empty
PASS  u04-lifetimes: revisit_at_days ascending, first >= 7 ([7, 30, 90])
PASS  u04-lifetimes: after u01-own-move-borrow resolves and precedes it
PASS  u04-lifetimes: mechanism unit names no question
PASS  u04-lifetimes: mechanism unit carries no status
PASS  u04-lifetimes: mechanism unit names its cluster
WARN  u04-lifetimes: map gap declared: no Concept for lifetime elision or `'static` bounds in core; subtyping-variance left out a
PASS  u05-generics-traits: no unknown fields 
PASS  u05-generics-traits: kind is mechanism|judgment (mechanism)
PASS  u05-generics-traits: names a defined form (attempt-first)
PASS  u05-generics-traits: form kind matches unit kind
PASS  u05-generics-traits: domain resolves (core)
PASS  u05-generics-traits: concept resolves (generics)
PASS  u05-generics-traits: concept resolves (traits)
PASS  u05-generics-traits: concept resolves (trait-bounds)
PASS  u05-generics-traits: concept resolves (monomorphization)
PASS  u05-generics-traits: concept resolves (associated-types)
PASS  u05-generics-traits: concepts non-empty
PASS  u05-generics-traits: revisit_at_days ascending, first >= 7 ([7, 30, 90])
PASS  u05-generics-traits: after u01-own-move-borrow resolves and precedes it
PASS  u05-generics-traits: mechanism unit names no question
PASS  u05-generics-traits: mechanism unit carries no status
PASS  u05-generics-traits: mechanism unit names its cluster
WARN  u05-generics-traits: map gap declared: associated-types and associated-types-2 are one Concept under two ids; associated-types ke
PASS  u06-closures-iterators: no unknown fields 
PASS  u06-closures-iterators: kind is mechanism|judgment (mechanism)
PASS  u06-closures-iterators: names a defined form (attempt-first)
PASS  u06-closures-iterators: form kind matches unit kind
PASS  u06-closures-iterators: domain resolves (core)
PASS  u06-closures-iterators: concept resolves (closures)
PASS  u06-closures-iterators: concept resolves (eager-vs-lazy-materialization)
PASS  u06-closures-iterators: concepts non-empty
PASS  u06-closures-iterators: revisit_at_days ascending, first >= 7 ([7, 30, 90])
PASS  u06-closures-iterators: after u01-own-move-borrow resolves and precedes it
PASS  u06-closures-iterators: after u05-generics-traits resolves and precedes it
PASS  u06-closures-iterators: mechanism unit names no question
PASS  u06-closures-iterators: mechanism unit carries no status
PASS  u06-closures-iterators: mechanism unit names its cluster
WARN  u06-closures-iterators: map gap declared: MAP has no iterator Concept (only dataset-iterator-abstractions, ML-specific, left out) an
PASS  u07-shared-ownership: no unknown fields 
PASS  u07-shared-ownership: kind is mechanism|judgment (mechanism)
PASS  u07-shared-ownership: names a defined form (attempt-first)
PASS  u07-shared-ownership: form kind matches unit kind
PASS  u07-shared-ownership: domain resolves (core)
PASS  u07-shared-ownership: concept resolves (box)
PASS  u07-shared-ownership: concept resolves (rc)
PASS  u07-shared-ownership: concept resolves (refcell)
PASS  u07-shared-ownership: concept resolves (arc)
PASS  u07-shared-ownership: concept resolves (interior-mutability)
PASS  u07-shared-ownership: concepts non-empty
PASS  u07-shared-ownership: revisit_at_days ascending, first >= 7 ([7, 30, 90])
PASS  u07-shared-ownership: after u01-own-move-borrow resolves and precedes it
PASS  u07-shared-ownership: after u05-generics-traits resolves and precedes it
PASS  u07-shared-ownership: mechanism unit names no question
PASS  u07-shared-ownership: mechanism unit carries no status
PASS  u07-shared-ownership: mechanism unit names its cluster
PASS  u08-trait-objects: no unknown fields 
PASS  u08-trait-objects: kind is mechanism|judgment (mechanism)
PASS  u08-trait-objects: names a defined form (attempt-first)
PASS  u08-trait-objects: form kind matches unit kind
PASS  u08-trait-objects: domain resolves (core)
PASS  u08-trait-objects: concept resolves (trait-objects)
PASS  u08-trait-objects: concept resolves (dyn-trait)
PASS  u08-trait-objects: concept resolves (static-vs-dynamic-dispatch)
PASS  u08-trait-objects: concept resolves (impl-trait)
PASS  u08-trait-objects: concepts non-empty
PASS  u08-trait-objects: revisit_at_days ascending, first >= 7 ([7, 30, 90])
PASS  u08-trait-objects: after u05-generics-traits resolves and precedes it
PASS  u08-trait-objects: after u07-shared-ownership resolves and precedes it
PASS  u08-trait-objects: mechanism unit names no question
PASS  u08-trait-objects: mechanism unit carries no status
PASS  u08-trait-objects: mechanism unit names its cluster
WARN  u08-trait-objects: map gap declared: dispatch is split across near-duplicate ids (dynamic-dispatch, dynamic-dispatch-2, dyn-tra
PASS  u09-j-shared-mutable-state: no unknown fields 
PASS  u09-j-shared-mutable-state: kind is mechanism|judgment (judgment)
PASS  u09-j-shared-mutable-state: names a defined form (judgment-drill)
PASS  u09-j-shared-mutable-state: form kind matches unit kind
PASS  u09-j-shared-mutable-state: domain resolves (core)
PASS  u09-j-shared-mutable-state: concept resolves (interior-mutability)
PASS  u09-j-shared-mutable-state: concept resolves (arc)
PASS  u09-j-shared-mutable-state: concept resolves (ownership)
PASS  u09-j-shared-mutable-state: concept resolves (box)
PASS  u09-j-shared-mutable-state: concept resolves (rc)
PASS  u09-j-shared-mutable-state: concept resolves (refcell)
PASS  u09-j-shared-mutable-state: concept resolves (borrow-checker)
PASS  u09-j-shared-mutable-state: concepts non-empty
PASS  u09-j-shared-mutable-state: revisit_at_days ascending, first >= 7 ([7, 30, 90])
PASS  u09-j-shared-mutable-state: after u01-own-move-borrow resolves and precedes it
PASS  u09-j-shared-mutable-state: after u07-shared-ownership resolves and precedes it
PASS  u09-j-shared-mutable-state: question resolves (shared-mutable-state-vs-explicit-passing)
PASS  u09-j-shared-mutable-state: domain is one of the question's domains
PASS  u09-j-shared-mutable-state: question has >= 2 positions (2)
PASS  u09-j-shared-mutable-state: concepts = question concepts reachable through after (missing [], extra [])
PASS  u09-j-shared-mutable-state: marked needs-arguments (MAP/arguments has 0 files)
PASS  u10-j-generics-vs-dyn: no unknown fields 
PASS  u10-j-generics-vs-dyn: kind is mechanism|judgment (judgment)
PASS  u10-j-generics-vs-dyn: names a defined form (judgment-drill)
PASS  u10-j-generics-vs-dyn: form kind matches unit kind
PASS  u10-j-generics-vs-dyn: domain resolves (core)
PASS  u10-j-generics-vs-dyn: concept resolves (static-vs-dynamic-dispatch)
PASS  u10-j-generics-vs-dyn: concept resolves (traits)
PASS  u10-j-generics-vs-dyn: concept resolves (associated-types)
PASS  u10-j-generics-vs-dyn: concept resolves (trait-objects)
PASS  u10-j-generics-vs-dyn: concept resolves (dyn-trait)
PASS  u10-j-generics-vs-dyn: concept resolves (generics)
PASS  u10-j-generics-vs-dyn: concept resolves (monomorphization)
PASS  u10-j-generics-vs-dyn: concepts non-empty
PASS  u10-j-generics-vs-dyn: revisit_at_days ascending, first >= 7 ([7, 30, 90])
PASS  u10-j-generics-vs-dyn: after u05-generics-traits resolves and precedes it
PASS  u10-j-generics-vs-dyn: after u08-trait-objects resolves and precedes it
PASS  u10-j-generics-vs-dyn: question resolves (generics-vs-dyn-for-abstraction)
PASS  u10-j-generics-vs-dyn: domain is one of the question's domains
PASS  u10-j-generics-vs-dyn: question has >= 2 positions (2)
PASS  u10-j-generics-vs-dyn: concepts = question concepts reachable through after (missing [], extra [])
PASS  u10-j-generics-vs-dyn: marked needs-arguments (MAP/arguments has 0 files)
WARN  u10-j-generics-vs-dyn: map gap declared: MAP/README.md "Known issues" lists this Question among 7 with a suspected duplicate Positi
PASS  u11-j-library-panic: no unknown fields 
PASS  u11-j-library-panic: kind is mechanism|judgment (judgment)
PASS  u11-j-library-panic: names a defined form (judgment-drill)
PASS  u11-j-library-panic: form kind matches unit kind
PASS  u11-j-library-panic: domain resolves (core)
PASS  u11-j-library-panic: concept resolves (error-handling)
PASS  u11-j-library-panic: concept resolves (panics)
PASS  u11-j-library-panic: concepts non-empty
PASS  u11-j-library-panic: revisit_at_days ascending, first >= 7 ([7, 30, 90])
PASS  u11-j-library-panic: after u03-result-question-mark resolves and precedes it
PASS  u11-j-library-panic: question resolves (library-panic)
PASS  u11-j-library-panic: domain is one of the question's domains
PASS  u11-j-library-panic: question has >= 2 positions (5)
PASS  u11-j-library-panic: concepts = question concepts reachable through after (missing [], extra [])
PASS  u11-j-library-panic: marked needs-arguments (MAP/arguments has 0 files)
WARN  u11-j-library-panic: map gap declared: one of 5 Positions (no-ad-hoc-panics) is tagged taste; the map gives no verdict on taste, 
PASS  u12-j-enum-vs-dyn: no unknown fields 
PASS  u12-j-enum-vs-dyn: kind is mechanism|judgment (judgment)
PASS  u12-j-enum-vs-dyn: names a defined form (judgment-drill)
PASS  u12-j-enum-vs-dyn: form kind matches unit kind
PASS  u12-j-enum-vs-dyn: domain resolves (core)
PASS  u12-j-enum-vs-dyn: concept resolves (enums)
PASS  u12-j-enum-vs-dyn: concept resolves (sum-types)
PASS  u12-j-enum-vs-dyn: concept resolves (traits)
PASS  u12-j-enum-vs-dyn: concepts non-empty
PASS  u12-j-enum-vs-dyn: revisit_at_days ascending, first >= 7 ([7, 30, 90])
PASS  u12-j-enum-vs-dyn: after u02-enums-match resolves and precedes it
PASS  u12-j-enum-vs-dyn: after u08-trait-objects resolves and precedes it
PASS  u12-j-enum-vs-dyn: question resolves (enum-vs-dyn-trait-closed-set)
PASS  u12-j-enum-vs-dyn: domain is one of the question's domains
PASS  u12-j-enum-vs-dyn: question has >= 2 positions (3)
PASS  u12-j-enum-vs-dyn: concepts = question concepts reachable through after (missing [], extra [])
PASS  u12-j-enum-vs-dyn: marked needs-arguments (MAP/arguments has 0 files)
PASS  baseline: 6 items (found 6)
PASS  baseline: one item per mechanism cluster ({'ownership-borrowing': 1, 'lifetimes': 1, 'result-question-mark': 1, 'traits-generics': 1, 'iterators-closures': 1, 'enums-match': 1})
PASS  baseline: 2 items per form ({'fix-the-compile-error': 2, 'write-to-tests': 2, 'predict-output': 2})
PASS  baseline b1-own: names id
PASS  baseline b1-own: names cluster
PASS  baseline b1-own: names form
PASS  baseline b1-own: names tests
PASS  baseline b1-own: names pass
PASS  baseline b1-own: names continuous
PASS  baseline b2-life: names id
PASS  baseline b2-life: names cluster
PASS  baseline b2-life: names form
PASS  baseline b2-life: names tests
PASS  baseline b2-life: names pass
PASS  baseline b2-life: names continuous
PASS  baseline b3-result: names id
PASS  baseline b3-result: names cluster
PASS  baseline b3-result: names form
PASS  baseline b3-result: names tests
PASS  baseline b3-result: names pass
PASS  baseline b3-result: names continuous
PASS  baseline b4-traits: names id
PASS  baseline b4-traits: names cluster
PASS  baseline b4-traits: names form
PASS  baseline b4-traits: names tests
PASS  baseline b4-traits: names pass
PASS  baseline b4-traits: names continuous
PASS  baseline b5-iter: names id
PASS  baseline b5-iter: names cluster
PASS  baseline b5-iter: names form
PASS  baseline b5-iter: names tests
PASS  baseline b5-iter: names pass
PASS  baseline b5-iter: names continuous
PASS  baseline b6-enum: names id
PASS  baseline b6-enum: names cluster
PASS  baseline b6-enum: names form
PASS  baseline b6-enum: names tests
PASS  baseline b6-enum: names pass
PASS  baseline b6-enum: names continuous

240 PASS, 0 FAIL, 8 WARN
MAP: 1447 concepts, 401 questions, 12 domains, 607 positions, 0 arguments
```
