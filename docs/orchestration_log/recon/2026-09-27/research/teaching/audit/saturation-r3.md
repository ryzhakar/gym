# Saturation audit — round 3

Scope: N1–N7, rounds through r3 (the Stage C cap). Rules: PLAN §5 lines 242–260. Thresholds: unseen
≤10% of S≥2 sources (Lincoln–Petersen); Stage C cap = 3 rounds (reached — this audit ships as the
confidence section, no further rounds gated on it). N5-r3-13 has no row in `claims-status.csv`;
treated as SURVEYED (claims.csv's own status), per dispatch.

## Headline, before the tables

Every need fails at least three of the five per-need conditions. **None is SATURATED.** Two
findings apply across all seven needs and are not per-need noise:

1. **Rule 2 (capture–recapture) is structurally undefined for every need, by ledger design, not by
   literature exhaustion.** `sources.csv` is append-only: an agent who re-finds an already-known
   source does not re-append a row for it (confirmed by direct inspection — zero within-need DOI
   duplicates across any round, for any need). Capture–recapture requires m = overlap between two
   rounds' capture sets; m is therefore 0 by construction in every single case, for every need,
   regardless of whether the field is actually exhausted. Rule 2 cannot discriminate saturated from
   open needs on this ledger schema as built. This is reported as a method-validity finding, not
   folded silently into the FAIL count as if it were ordinary evidence of non-saturation.
2. **Rule 4 (ledger closure) fails everywhere, substantially.** Every need carries 5–19 claims still
   SURVEYED. This is real backlog, not an artifact — Tier 3 verification has not caught up with Tier
   2 survey output.

## Rule 1 — two consecutive rounds, zero new S≥3, ≤1 new S=2

Arithmetic (need-tagged rows in `sources.csv`, grouped by round; a row counts once per need it is
tagged to; "new" = DOI not already tagged to this need in an earlier round — confirmed 0 within-need
repeats exist, so every tagged row in a round is by construction new to that need):

```
N1: round 1: new_S≥3=6  new_S=2=4   |  round 3: new_S≥3=5  new_S=2=1
N2: round 1: new_S≥3=5  new_S=2=3   |  round 3: new_S≥3=6  new_S=2=1
N3: round 1: new_S≥3=7  new_S=2=5   |  round 3: new_S≥3=7  new_S=2=2
N4: round 2: new_S≥3=4  new_S=2=5   |  round 3: new_S≥3=2  new_S=2=9
N5: round 2: new_S≥3=1  new_S=2=2   |  round 3: new_S≥3=1  new_S=2=7
N6: round 2: new_S≥3=6  new_S=2=3   |  round 3: new_S≥3=4  new_S=2=3
N7: round 1: new_S≥3=11 new_S=2=5   |  round 2: new_S≥3=0 new_S=2=2  |  round 3: new_S≥3=9 new_S=2=1
```

| need | 2 most recent rounds | new S≥3 (r, r+1) | new S=2 (r, r+1) | Rule 1 |
|---|---|---|---|---|
| N1 | r1, r3 | 6, 5 | 4, 1 | FAIL |
| N2 | r1, r3 | 5, 6 | 3, 1 | FAIL |
| N3 | r1, r3 | 7, 7 | 5, 2 | FAIL |
| N4 | r2, r3 | 4, 2 | 5, 9 | FAIL |
| N5 | r2, r3 | 1, 1 | 2, 7 | FAIL |
| N6 | r2, r3 | 6, 4 | 3, 3 | FAIL |
| N7 | r2, r3 | 0, 9 | 2, 1 | FAIL |

Every need's most recent round found new S≥3 sources (N7's round 2 alone hit zero, then round 3 —
a fresh agent, fresh query set — surfaced 9 more). Rule 1 fails everywhere; the fields are not
running dry at this level of query effort.

## Rule 2 — Lincoln–Petersen capture–recapture, S≥2 sources, two most recent rounds

```python
set1 = {DOI : S in {2,3,4}, round==r}
set2 = {DOI : S in {2,3,4}, round==r+1}
m = len(set1 & set2)
```

Output:

```
N1: round1 n1=10  round3 n2=6   overlap m=0
N2: round1 n1=8   round3 n2=7   overlap m=0
N3: round1 n1=12  round3 n2=9   overlap m=0
N4: round2 n1=9   round3 n2=11  overlap m=0
N5: round2 n1=3   round3 n2=8   overlap m=0
N6: round2 n1=9   round3 n2=7   overlap m=0
N7: round2 n1=2   round3 n2=10  overlap m=0
```

| need | n1 | n2 | m | N̂ | unseen % | Rule 2 |
|---|---|---|---|---|---|---|
| N1 | 10 | 6 | 0 | undefined | undefined | FAIL |
| N2 | 8 | 7 | 0 | undefined | undefined | FAIL |
| N3 | 12 | 9 | 0 | undefined | undefined | FAIL |
| N4 | 9 | 11 | 0 | undefined | undefined | FAIL |
| N5 | 3 | 8 | 0 | undefined | undefined | FAIL |
| N6 | 9 | 7 | 0 | undefined | undefined | FAIL |
| N7 | 2 | 10 | 0 | undefined | undefined | FAIL |

m=0 in all seven cases — per rule, FAIL/undefined, not "100% unseen." Root cause: the ledger's own
append convention (§ headline finding 1) makes m=0 the default outcome whenever a round's search
recognizes a source it already knows and correctly declines to re-append it — which is exactly what
the "seen" columns in every round's own search log report happening repeatedly (e.g. N3-r3 logs 1
seen; N6-r3 logs 1 seen; N2-r1 logs multiple "5", "6" seen counts per query) — those recognitions
never reach `sources.csv` as a second row, so the capture-recapture statistic computed from the CSV
alone cannot see them. The rule as specified (computed over ledger DOI sets) is not measuring what
it is meant to measure under this ledger's write convention.

## Rule 3 — seed coverage (seed-probe.md), by need

`seed-citations.csv` carries no N1–N7 tag — only "seed section" (1–7), which the plan does not map
1:1 to needs (seed-probe.md's own words: "Seed sections don't map 1:1 onto the project's N1–N7").
Mapping below is this audit's own best-effort assignment, using the plan's one explicit instruction
("KC modeling → N2; struggle metrics → N4," §3) plus content fit for the rest; it is inferred, not
authored by seed-probe or the plan, and several sections span more than one need.

**Recorded prompt leak (per the audit's own instruction to note it):** `t5-evidence-map.md` line 19
and `evidence-map.md` line 276 record that round-3 query sets for N2 (knowledge-component block) and
N3 (struggle/intervention block) were built from dispatch sub-areas that mirror seed §7 and §6
respectively — an orchestrator-level leak of the seed's own structure into round-3 dispatch prompts,
not a violation by the surveying agents (who never read seed.md). Round 3's seed-coverage numbers for
N2 and N3 are therefore not an independent test for those needs; the record also states round 3 found
none of the leaked sections' seed citations anyway, so the leak did not inflate coverage — the
independence violation exists whether or not it changed the number.

| need | mapped seed section(s) | citations w/ data | found independently | Rule 3 |
|---|---|---|---|---|
| N1 | §1 target/proxies | 7 | 0 | FAIL (0%) |
| N2 | §4 practice design + §7 KC/learning-curve core | 11 + 4 | 2 + 0 | FAIL (§4 alone reaches seed-probe's own "clears it" verdict on its 2 checkable items; §7, the plan's own explicit N2 mapping, is 0/4 — net FAIL; round-3 contribution not independent, see leak above) |
| N3 | §6 struggle/confusion/intervene | 11 | 1 (ProgSnap2, ungraded) | FAIL (9%; round-3 contribution not independent, see leak above) |
| N4 | §3 diagnosis/misconceptions | 5 | 0 | FAIL (0%) |
| N5 | §5 feedback/coaching | 1 checkable (Wooden) | 0 | FAIL (0%) |
| N6 | no dedicated section; nearest proxy = interruption/resumption items inside §6 (Iqbal & Bailey, Parnin & Rugaber, Tanaka) | 3 | 0 | FAIL (0%) — weak proxy, N6 has no seed section of its own |
| N7 | §2 tutoring effect sizes | 8 | 3 (Shen & Tamkin, Wang/Tutor CoPilot, Jurenka) | FAIL (37.5%) |

All seven FAIL the ≥80% bar. Two seed citations were checked and found to contradict the seed's own
paraphrase (Lee et al. 2026: 118% inflation, not 75%; Sinha & Kapur's mechanism list and scaffolding
claim) — reported per seed-probe.md, not re-derived here.

## Rule 4 — ledger closure (no claim left SURVEYED)

```
N1: total=25  VERIFIED=8  SURVEYED=12  UNVERIFIABLE=4  REFUTED=1
N2: total=21  VERIFIED=9  SURVEYED=5   UNVERIFIABLE=7
N3: total=22  VERIFIED=7  SURVEYED=8   UNVERIFIABLE=7
N4: total=22  VERIFIED=5  SURVEYED=17
N5: total=23  VERIFIED=3  SURVEYED=19  REFUTED=1
N6: total=24  VERIFIED=5  SURVEYED=12  UNVERIFIABLE=7
N7: total=29  VERIFIED=17 SURVEYED=9   UNVERIFIABLE=1  REFUTED=2
```
(claims-status.csv's last row per claim_id applied as override; N5-r3-13 counted SURVEYED, no
status row, per dispatch note.)

| need | total claims | SURVEYED remaining | Rule 4 |
|---|---|---|---|
| N1 | 25 | 12 | FAIL |
| N2 | 21 | 5 | FAIL |
| N3 | 22 | 8 | FAIL |
| N4 | 22 | 17 | FAIL |
| N5 | 23 | 19 | FAIL |
| N6 | 24 | 12 | FAIL |
| N7 | 29 | 9 | FAIL |

FAIL everywhere; N4 and N5 have Tier 3 coverage under 25% of their claims.

## Rule 5 — axis closure (each of 4 axes: ≥1 VERIFIED claim, or a logged "no evidence" entry)

```
N1: skill_per_hour VERIFIED=4  durability=3  transfer=1  sustainability=0
N2: skill_per_hour VERIFIED=4  durability=3  transfer=3  sustainability=2
N3: skill_per_hour VERIFIED=6  durability=1  transfer=1  sustainability=0
N4: skill_per_hour VERIFIED=3  durability=1  transfer=1  sustainability=0
N5: skill_per_hour VERIFIED=0  durability=0  transfer=2  sustainability=1
N6: skill_per_hour VERIFIED=0  durability=2  transfer=0  sustainability=4
N7: skill_per_hour VERIFIED=13 durability=6  transfer=5  sustainability=1
```

Where a count is 0, checked against the need's own "Claims by axis" sections for an explicit
"no evidence found" entry with queries (the rule's escape clause) versus an unresolved claim that
blocks the escape:

- N1 sustainability: 0 VERIFIED. Not an escape — 3 claims exist (N1-r1-12, N1-r1-13 SURVEYED;
  N1-r3-12 REFUTED), evidence was found and left unresolved. **FAIL.**
- N3 sustainability: 0 VERIFIED. Escape applies — both r1 and r3 log explicit "No evidence found"
  with queries, correctly scoped ("N3's forced axes are skill/hour and durability; sustain-axis...
  is N6's territory"). **PASS.**
- N4 sustainability: 0 VERIFIED. Escape applies — both r2 and r3 log explicit "No evidence found"
  with queries, same scoping logic as N3. **PASS.**
- N5 skill_per_hour: 0 VERIFIED. Not an escape — 6 SURVEYED claims exist across r2/r3 (expert/novice
  teacher-attention studies), no "no evidence" note; evidence found, not verified. **FAIL.**
- N5 durability: 0 VERIFIED. Not a clean escape — N5-r2-06 exists (SURVEYED, never resolved) before
  r2's "no further evidence" note, and r3 separately logs a proper "No evidence found this round"
  with queries; the round-2 claim's open status blocks full escape. **FAIL.**
- N6 skill_per_hour: 0 VERIFIED. Escape applies — both r2 and r3 log explicit "No evidence found"
  with queries, correctly scoped to N6 not forcing this axis. **PASS.**
- N6 transfer: 0 VERIFIED. r2 logged "No evidence found" (escape), but **r3 broke it**: N6-r3-10 is
  a real transfer-tagged claim (SURVEYED, unresolved) found this round. The exemption does not
  survive round 3. **FAIL.**

| need | skill/hour | durability | transfer | sustainability | Rule 5 |
|---|---|---|---|---|---|
| N1 | PASS | PASS | PASS | FAIL | **FAIL** |
| N2 | PASS | PASS | PASS | PASS | **PASS** |
| N3 | PASS | PASS | PASS | PASS (escape) | **PASS** |
| N4 | PASS | PASS | PASS | PASS (escape) | **PASS** |
| N5 | FAIL | FAIL | PASS | PASS | **FAIL** |
| N6 | PASS (escape) | PASS | FAIL | PASS | **FAIL** |
| N7 | PASS | PASS | PASS | PASS | **PASS** |

## Void rounds

Checked: queries/databases/hit-counts present (all 15 need-rounds and both breadth rounds carry
these — none void on that ground); exact-string query reuse across a need's own round pair (0%
byte-identical reuse found for any need — no round is void on that ground under a strict,
computable reading; several round pairs are close paraphrases of the same handful of concepts,
e.g. N1's "felt learning illusion of competence fluency" (r1) / "fluency illusion of competence
measurement" (r3), noted as a qualitative overlap but not counted, since only exact-string reuse is
objectively computable from the logs without guessing a similarity threshold); every source row
carries S/R/O:

```
N1 round 3: 7 of 16 tagged rows missing S/R/O  (44%)
N2 round 3: 3 of 10 tagged rows missing S/R/O  (30%)
N4 round 2: 1 of 17 tagged rows missing S/R/O  (6%)
N5 round 2: 15 of 24 tagged rows missing S/R/O (63%)
N5 round 3: 5 of 13 tagged rows missing S/R/O  (38%)
N3, N6, N7: 0 missing in any round
```

Rule, applied literally ("if any source row lacks S/R/O"), makes N1-r3, N2-r3, N4-r2, N5-r2, N5-r3
**void**. All 31 missing-grade rows carry the same mechanism, checked directly: a resolved
DOI/title, an honestly logged `full_text_read=N`, and a `flags` entry stating why ("UNREACHABLE —
Unpaywall no OA location," "Semantic Scholar abstract elided by publisher," "Cloudflare/bot-challenge
on fetch," one DNS failure). No row in this set skipped a database, under-logged a query, or
guessed a grade — this is the PRINCIPLES-mandated refusal to grade a source without reading it,
not a rushed round. The void designation is therefore mechanically correct per the stated rule and
substantively misleading if read as "this round was sloppy": these rounds were, if anything, more
conservative about grading than average. Applied as written regardless — the rule does not carve
out an exception for honest non-grading, and carving one out here would be this auditor overriding
a stated threshold rather than computing against it.

N5 is void in **both** of its rounds — no valid round pair exists for it at all.

## Verdict

| need | Rule 1 | Rule 2 | Rule 3 | Rule 4 | Rule 5 | Void round(s) | **Verdict** |
|---|---|---|---|---|---|---|---|
| N1 | FAIL | FAIL | FAIL | FAIL | FAIL | r3 (44%) | **VOID-ROUND** |
| N2 | FAIL | FAIL | FAIL | FAIL | PASS | r3 (30%) | **VOID-ROUND** |
| N3 | FAIL | FAIL | FAIL | FAIL | PASS | none | **OPEN** |
| N4 | FAIL | FAIL | FAIL | FAIL | PASS | r2 (6%, marginal) | **VOID-ROUND** |
| N5 | FAIL | FAIL | FAIL | FAIL | FAIL | r2 (63%) + r3 (38%) | **VOID-ROUND** |
| N6 | FAIL | FAIL | FAIL | FAIL | FAIL | none | **OPEN** |
| N7 | FAIL | FAIL | FAIL | FAIL | PASS | none | **OPEN** |

No need is SATURATED. Four needs (N1, N2, N4, N5) cannot even be judged cleanly yet — a round in
their most recent pair is void per the literal rule and needs a re-run before rules 1–2 mean
anything for them. Three needs (N3, N6, N7) have clean, non-void data and still fail on volume
(Rule 1), closure (Rule 4), and seed coverage (Rule 3); N6 additionally fails axis closure. Rule 2
contributes no real signal anywhere (see headline finding 1) and should not be read as "90%+ unseen"
for any of the seven — it is undefined, not measured.

## Per-need gap, one paragraph each

**N1 (Measure).** Round 3 is void (7/16 sources ungraded, all paywalled/unreachable, honestly
logged) — re-run before anything else here is trustworthy. Setting that aside, round 3 still
surfaced 5 new S≥3 sources and 12 of 25 claims sit SURVEYED; sustainability has zero VERIFIED
claims and is not covered by a "no evidence" escape (three claims sit open, one REFUTED). Seed
coverage for the target/proxies question (§1) is 0/7 — none of the seed's own proxy-validity
citations (Bastani, Chi/Siler/Jeong, Person et al., Koli Calling) were found independently.

**N2 (Unit and order of practice).** Round 3 is void (3/10 ungraded). Rule 1 fails outright — round
3 alone added 6 new S≥3 sources on knowledge-component granularity, mastery learning, and
project-based learning that round 1 never touched. Axis closure is the one clean pass among the
five needs without it (N2, N3, N4, N7). Seed coverage is the most structurally confused of the
seven: the plan itself splits N2's seed evidence across §4 (practice design, which seed-probe calls
cleared) and §7 (knowledge-component/learning-curve core, 0/4 found), and round 3's contribution to
either is not an independent test — the round-3 query set for the KC block was built from a
dispatch that mirrored seed §7's own structure.

**N3 (Session shape and intervention).** No void round — the cleanest data of the seven, and still
fails 4 of 5 rules. Round 3 found 7 new S≥3 sources on unproductive-struggle detection, interruption
recovery, and reactivity/observer effects that round 1's hint-timing/impasse/scaffolding focus never
surfaced — the field is not thinning. 8 of 22 claims remain SURVEYED. Rule 3's 9% (1/11, and that 1
ungraded) is the second-worst seed-coverage number on record, and it is contaminated: round 3's
struggle/intervention query set mirrors seed §6's own structure (recorded prompt leak), so a higher
number here would not have meant independent confirmation anyway.

**N4 (Diagnosis).** Round 2 is void on a single unreachable-blog row (6% of round 2, the mildest
void trigger of the five) — re-run is still required by the rule as written, though this is the
weakest case for one. 17 of 22 claims remain SURVEYED — the largest unresolved-claim backlog
relative to total claims in the whole project. Seed coverage is 0/5 for diagnosis/misconceptions
(§3): none of Crichton et al.'s Rust-ownership misconception work — directly relevant to this
project's own first subject — has been independently found by any survey round.

**N5 (Elite margin).** Both rounds are void (63% and 38% ungraded respectively) — no valid round
pair exists yet for this need; it is the least trustworthy data in the project as it stands. Rule 5
also fails here specifically (not just via the void designation): skill/hour and durability both
have SURVEYED claims sitting open with no verification and no logged "no evidence," so even setting
the void issue aside this need's axis closure would fail. Seed coverage is 0% — Tharp & Gallimore's
coded Wooden analysis, the seed's only checkable coaching citation, was never checked by anyone.

**N6 (Sustain).** No void round. Round 2's "no evidence" exemptions for skill/hour and transfer held
for skill/hour into round 3, but round 3 broke the transfer exemption by surfacing a genuine
(unverified) transfer-tagged claim — the escape does not survive a second round of searching. 12 of
24 claims remain SURVEYED. N6 has no dedicated seed section; the nearest proxy (interruption/
resumption items folded into seed §6) found 0 of 3 independently, which is a weak signal either way
given the mismatch.

**N7 (LLM transfer).** No void round; the strongest need on 4 of 5 rules (Rule 5 fully closed, only
9 of 29 claims SURVEYED — the best closure ratio of the seven). Still fails Rule 1 decisively: round
2 hit zero new S≥3 sources, which would have been the first half of a saturation signal, and round
3 — a fresh agent working from the plan and substrate-audit only, explicitly not from prior rounds —
immediately found 9 more via citation-chasing off two anchor DOIs (Bastani, Kestin), a method the
earlier keyword-search rounds hadn't used. Seed coverage (§2, tutoring effect sizes) is 37.5%
(3/8) — the best of the seven and still well under the 80% bar.

---
Analysis: 477 sources.csv rows, 166 claims.csv rows, 88 claims-status.csv rows read; arithmetic run
via `uv run python` over copies in scratch, no script file kept in ROOT. 3 needs (N3, N6, N7) have
clean, judgeable round pairs; 4 (N1, N2, N4, N5) need a round re-run before Rules 1–2 apply to them
at all. Zero needs are SATURATED; Rule 2 is reported as undefined everywhere rather than as evidence
of non-saturation, since m=0 is a structural property of this ledger's append-only convention, not a
measurement of the literature.
