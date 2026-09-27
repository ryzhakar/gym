# Calibration set

Five anchors from `index/index.md`, one per S band plus one flagged/borderline case,
chosen to span the bands the plan's §4 S table defines (meta-analysis/systematic
review → practitioner account). No grades assigned here — that is Tier 2's job;
this set only fixes which five sources every round-1 grader scores, so grading
drift across agents is visible.

1. **Likely S4 — meta-analysis.** Cepeda, Pashler, Vul, Wixted et al., 2006, "Distributed practice in verbal recall tasks: a review and quantitative synthesis." DOI: `10.1037/0033-2909.132.3.354`.
   Why: a quantitative synthesis across many spacing-effect studies reporting how the effect varies with a moderator (inter-study-lag/retention-interval ratio) — the shape §4 names for S4. Also a cross-field anchor (education, expertise), so a grading disagreement here is visible from two field angles at once.

2. **Likely S3 — single RCT with a control.** Rohrer, Dedrick, Hartwig & Cheung, 2020, "A randomized controlled trial of interleaved mathematics practice." DOI: `10.1037/edu0000367`.
   Why: a cluster-randomized field trial (real classrooms, not a lab task) with a control condition (blocked practice) and a delayed outcome test — a clean single-RCT case, distinct from the meta-analytic and observational bands on either side of it.

3. **Likely S2 — systematic observation with coding.** Partington, Cushion & Harvey, 2013, "Effect of athletes' age on the coaching behaviours of professional top-level youth soccer coaches." DOI: `10.1080/02640414.2013.835063`.
   Why: coded observation of real coaching sessions (not self-report, not an RCT) — the exact case §4 names for S2 ("coded coaching sessions").

4. **Likely S1 — practitioner/expert account.** Klein & Crandall, 1990, "Recognition-Primed Decision Strategies." DOI: `10.21236/ada226887`.
   Why: the coaching field file itself flags this as an unrefereed technical report (S1) — a documented, not inferred, S1 case, useful precisely because its own source file already named the concern this calibration set is meant to catch.

5. **Flagged/borderline.** Jurenka, Kunesch, McKee et al. (LearnLM Team, Google DeepMind), 2024, "Towards Responsible Development of Generative AI for Education: An Evaluation-Driven Approach." DOI: `10.48550/arxiv.2407.12687`.
   Why: vendor-authored, evaluating the vendor's own model, and an arXiv preprint (not peer-reviewed) — three separate reasons a grader might disagree on placement, and the ai-tutoring field file already flags it as vendor-authored, making any grading drift on this one attributable to the S/R/O call itself rather than to missed context.
