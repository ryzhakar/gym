# Deliberate practice — resolution

Tier 4 resolver, 2026-09-27. Two disputes:
- (1) How much of expert performance deliberate practice (DP) explains. Ericsson and colleagues vs Macnamara, Hambrick and colleagues.
- (2) Whether DP applies to programming. This is the practitioner dispute in ROOT/needs/breadth-r2.md.

Inputs:
- ROOT/index/index.md, expertise #2–#22 and coaching #1–#3 and #20–#25, plus the Disputes lines [coaching] Ericsson vs Macnamara and [adult-skill] DP explanatory power.
- ROOT/needs/n5-r2.md, the disagreements note on Macnamara, Moreau & Hambrick 2016.
- ROOT/needs/n6-r2.md, claim N6-r2-02.
- ROOT/needs/breadth-r2.md, the high-signal find on DP for programmers.
- ROOT/ledger/claims.csv rows touching DP.

Counts:
- Full texts read: 11. Whole: E1 key sections, E3, E4, M4, X1. Section-targeted: E2, M3, E5, X2, X3, X4.
- Practitioner threads read in full: 2.
- Abstract only: 2 (M1, M2).
- Unread leads: 12.
- API calls: Unpaywall 25, Crossref 21 (7 searches, 14 DOI resolutions), Semantic Scholar 5, PubMed efetch 1, Europe PMC 1, PMC efetch 3, arXiv 1, OSF 1 (failed), Princeton DataSpace 1 (no hit), KOPS DSpace 4, HN Algolia 1, lobste.rs 1.
- WebSearch 0 and OpenAlex 0: budgets spent.

## The Contradiction

Dispute 1: how much of performance DP explains.
- Side E (Ericsson, Krampe & Tesch-Römer 1993; Ericsson & Harwell 2019; Ericsson 2020): individual differences "can largely be accounted for" by accumulated DP, even among elite performers. Meta-analyses showing less used the wrong definition.
- Side M (Macnamara, Hambrick & Oswald 2014; Macnamara, Moreau & Hambrick 2016; Hambrick et al. 2014, 2020; Macnamara & Maitra 2019): DP explains a moderate, domain-varying share. It is smallest in professions and among elite performers, and it leaves most variance unexplained.

Dispute 2: does DP apply to programming?
- Practitioners (HN 19690959, lobste.rs uu6v1o): the construct may not apply to programming at all, because code is reused rather than rehearsed, and programming skill has no agreed measure.
- The academic literature in the index does not address programming.

What the texts show:
- Dispute 1 is three disputes stacked:
  - what counts as DP (definition);
  - how practice is measured (retrospective hours, unreliability corrections);
  - whose sample (skill level, domain).
- Once these are held fixed, the two camps' numbers mostly agree.
- Dispute 2 has no outcome data on either side. The practitioner objections each map onto one of the preconditions DP itself states.

## Primary Source Checks

### E1. Ericsson, Krampe & Tesch-Römer 1993

DOI 10.1037/0033-295x.100.3.363. Crossref: Psychological Review 1993, no update-to.

Read: PDF from projects.ict.usc.edu author mirror, 44 pp. Sections read: pp. 363, 366–369, 380–381, 392–393, 399. The results tables were skimmed, not read line by line.

- Conditions for DP, p. 367: "attend to the task and exert effort … immediate informative feedback and knowledge of results … repeatedly perform the same or similar tasks". Also: "In the absence of adequate feedback, efficient learning is impossible and improvement only minimal even for highly motivated subjects."
- Teacher, p. 368: "the teacher designs practice activities that the individual can engage in between meetings with the teacher. We call these practice activities deliberate practice". The same page also says: "deliberate practice is a highly structured activity, the explicit goal of which is to improve performance."
- Domain precondition, p. 368: "In all major domains there has been a steady accumulation of knowledge about the best methods to attain a high level of performance".
- Strong claims:
  - "individual differences in ultimate performance can largely be accounted for by differential amounts of past and current levels of practice" (p. 392);
  - "sufficient account of the major facts" (p. 392);
  - "impossible for an individual with less accumulated practice at some age to catch up with the best individuals" (p. 393);
  - "we reject any important role for innate ability" (p. 399).
- Design: violin students at a music academy, 3 groups × 10 (plus 10 professionals); pianists in Study 2. Skill group = faculty nomination and department. Practice measures: a retrospective interview of weekly hours per year, and a 1-week diary.
- Inside the founding study, the concurrent measure did not separate the top two groups, p. 380: "the two best groups of young violinists did not differ from each other in their amount of practice alone" in the diary week. Only the retrospective accumulated estimates separated them.
- Grade S2 R2 O2. O2 because the outcome is attained unaided performance years after practice began. The predictor is a retrospective self-report. Flags: n<30 per cell; interviewers not blind (per E3 below).

### E2. Ericsson & Harwell 2019

DOI 10.3389/fpsyg.2019.02396. Crossref: Frontiers in Psychology, no update. Read: Frontiers PDF, pp. 1–13.

- The claim at issue: Macnamara et al. 2014 measured "structured practice", not DP. The broad definition admitted lectures, TV watching and team practice (pp. 5–6).
- Three sequential inclusion criteria (pp. 9–11):
  1. reproducibly superior performance;
  2. practice directed at the target performance;
  3. solitary practice.
- Result, p. 11: "games (r = 0.50, k = 5), music (r = 0.71, k = 3), and sports (r = 0.58, k = 5). It is notable that no effect sizes from the domain of professions met the criteria (k = 0) and only the study of Spelling Bee performance … remained for the education category (r = 0.31, k = 1)."
- Pooled: "r = 0.54, 95% CI = [0.44, 0.63] … approximately 29% of the variance" (p. 11). After correction with practice reliability 0.6 and performance reliability 0.8: "61%" (pp. 12–13).
- Moderator, teacher vs self-guided, p. 11: "rdeliberate = 0.56 … rpurposeful = 0.51 … [Q(1) = 0.22, p = 0.64]."
- Moderator, objective vs relative performance measure: "robjective = 0.49, rrelative = 0.65 … Q(1) = 1.45, p = 0.23."
- Measurement: weekly estimates vs diaries correlate "between 0.60 and 0.75" for the current year. Ward et al. 2007 found "high reliability for estimates only for the most recent 5 years". The authors write: "It is plausible that the reliability and accuracy of estimates of weekly practice for as much as 15–20 years earlier will be considerably lower" (p. 8).
- Skill level: the 1%-among-elite result "is completely consistent with the severe restriction of range". But "none of the studies of only elite samples analyzed by Macnamara et al. (2016) passed our three criteria" (p. 12).
- Recency, citing Krampe & Ericsson 1996 (secondary here):
  - older expert pianists averaged 57,739 h of practice vs 17,927 h for young experts, "yet the older experts' performance was not superior";
  - "accumulated amount of solitary practice during the last 10 years was the measure that best predicted" performance (p. 7).
- Grade S3 R2 O2. A meta-reanalysis with k = 14 and two moderators. Heterogeneity statistics are not in the pages read. The inclusion criteria were applied post hoc by the theory's author. Flag: the author has a stake in the outcome.

### E3. Macnamara & Maitra 2019, preregistered replication of E1

DOI 10.1098/rsos.190327. Crossref: Royal Society Open Science, no update.

Read: PMC6731745 full-text XML, ~11,000 words, whole text.

- Design: "double-blind procedure". Preregistered at osf.io/khjs7 and osf.io/jyn5w, results-blind accepted. Sample: n = 39 violin students (13 per group), Cleveland Institute of Music and Case Western Reserve University (Methods 2, Table 2).
- Core result, §3.5: "the best violinists (M = 8224 …) had not accumulated significantly more practice alone by age 18 than the good violinists (M = 9844 …), t24 = −0.93, p = 0.364, d = −0.38."
- Effect size: "Ericsson et al.'s [1] comparison … explained 48% of the variance … Our comparison … explained 26%" (§4).
- Definition test, §3.5: accumulated teacher-designed practice and accumulated practice alone "explain similar amounts of performance variance". η² = 0.23 [0.02, 0.41] vs η² = 0.26 [0.03, 0.44]; the two correlate at r = 0.72.
- Measurement: estimates exceed diary-logged practice (F1,35 = 19.62, p < 0.001), but the bias "did not differ across groups" (§3.4). This matches E1's own finding.
- The authors' own alternative explanation: "it could be that the importance of deliberate practice diminishes at high levels of expertise in music, as has been demonstrated in sports" (§4).
- Enjoyment rating of practice alone (Table 5): 7.23 in the original, 7.27 in the replication. Neither is marked significantly above or below the grand mean. So E1's "not inherently enjoyable" (p. 368) is not supported by either sample's ratings. Effort was rated high in both (8.00 H, 8.29 H).
- Grade S2 R2 O2. Observational, small N, but preregistered and blind. Flag: n = 13 per group.

### M1. Macnamara, Hambrick & Oswald 2014, and its 2018 corrigendum

DOI 10.1177/0956797614535810. Crossref: `updated-by: ['correction']`; the corrigendum 10.1177/0956797618769891 has `update-to` → 10.1177/0956797614535810.

Read: abstract only (PubMed 24986855). Unpaywall, Semantic Scholar, Europe PMC and the author pages have no OA copy.

- Abstract, uncorrected: "26% … games, 21% … music, 18% … sports, 4% … education, and less than 1% for professions."
- Corrected figures, as reported by the same authors in M3 (p. 5): "14% of the variance in performance overall, and 24% for games, 23% for music, 20% for sports, 5% for education, and 1% for professions".
- Definition, from the abstract: "engagement in structured activities created specifically to improve performance in a domain". M3 p. 5 adds that they "include[d] both teacher- and performer-designed activities."
- Ericsson 2020 (E4) states that the dissertation version was subtitled "Cognitive Abilities, Experiential Factors and Predictability of the Task Environment". The predictability moderator and the practice-measurement moderator of this meta-analysis are not in the abstract. They were not read and do not enter this resolution.
- Grade S4 R2 O2, from the abstract. Flag: abstract-only read; the numbers are taken from M3's full text.

### M2. Macnamara, Moreau & Hambrick 2016, sports

DOI 10.1177/1745691616635591. Crossref: Perspectives on Psychological Science, no update. Read: abstract only (PubMed 27217246).

- "deliberate practice accounted for 18% of the variance in sports performance … only 1% of the variance in performance among elite-level performers."
- "athletes who reached a high level of skill did not begin their sport earlier in childhood than lower skill athletes."
- Grade S4 R2 O2. Flag: abstract-only read.

### M3. Hambrick, Macnamara & Oswald 2020

DOI 10.3389/fpsyg.2020.01134. Crossref: Frontiers in Psychology, no update. Read: Frontiers PDF, pp. 2–10.

- Definition drift, documented with quotes (Fig. 2, p. 3). Ericsson 1998: "designed … by a teacher or the performers themselves". Ericsson 2015: "When this type of training is supervised and guided by a teacher, it is called 'deliberate practice'."
- Table 2 (p. 8): "seven of the eight effect sizes they coded as deliberate practice were from studies previously rejected by Ericsson (2014a)". Ericsson 2014a "rejected 87 of the 88 studies" (p. 5).
- Sensitivity of E2's 61% to the assumed reliabilities (Table 3, p. 10):
  - with deliberate-practice r = 0.56, variance explained ranges from 38.7% (reliabilities 0.9/0.9) to 87.1% (0.6/0.6);
  - with reliabilities 0.8/0.8 it is "49%".
- Ericsson's own earlier reliability statements, quoted: "test-retest reliabilities at or above 0.80" (Tuffiash et al. 2007) and "between 0.7 and 0.8" (Ericsson 2012).
- Chess, via Gobet & Campitelli 2007: hours "required to reach 'master' status … ranged from 3,016 to 23,608 h—a difference of nearly a factor of 8" (p. 4). E2 p. 7 reports 1,612–14,196 h for solitary practice alone from the same paper. Different measure; both are wide.
- Grade S1 (review). It is used here only as the full-text carrier of M1's corrected numbers and of E2's sensitivity arithmetic.

### E4. Ericsson 2020, reply to Macnamara & Hambrick 2020

DOI 10.1007/s00426-020-01368-3. Crossref: Psychological Research, no update. Read: PMC8049893, whole text.

- Five criteria: "The task must be well defined with a clear goal … perform the task by themselves … immediate informative and actionable feedback … 'repeatedly perform the same or similar tasks' … designed and performed in accordance with individualized instruction and guidance of a teacher."
- Purposeful practice = criteria 1–4 without criterion 5.
- Predictability condition, stated by Ericsson himself: "motivated students studying with an experienced teacher of reading Tarot cards, who engage in their assigned practice are very unlikely to increase the accuracy of their predictions".
- Hours vs quality: "These sums of hours of practice do not estimate the maximal accounts of performance by practice".
- Grade S1 (theory).

### E5. Platz, Kopiez, Lehmann & Wolf 2014, music

DOI 10.3389/fpsyg.2014.00646. Crossref: Frontiers in Psychology, no update. Read: Frontiers PDF, abstract, methods, pp. 3–4 and 9–11.

- Abstract: "13 studies (total N = 788) … objectively assessed musical achievement … rc = 0.61; 95% CI [0.54, 0.67] for the relationship between task-relevant practice (which by definition includes DP) and musical achievement."
- Specificity: sight-reading performance is "less well predicted by accumulated generic deliberate practice … than by the accumulated amount of task-specific deliberate practice" (p. 4).
- Own limit: "there is a lack of controlled empirical studies based on the expertise theory in the domain of music" (p. 11).
- Heterogeneity reported for the reanalysed Hambrick 2014 sample: "I2 = 60.3%".
- Grade S4 R2 O2.

### M4. Hambrick, Altmann, Oswald, Meinz & Gobet 2014, "Facing facts"

DOI 10.3389/fpsyg.2014.00751. Crossref authors: Hambrick, Altmann, Oswald, Meinz, Gobet. Read: 2-page PDF, whole text.

- "Deliberate practice accounted for about one-third of the reliable variance in performance in each domain [chess, music]".
- Measurement: "using retrospective questionnaires to measure deliberate practice could lead to inflated correlations … if people base practice estimates on their skill rather than recollections".
- Grade S1 (commentary).

### X1. McGaghie, Issenberg, Cohen, Barsuk & Wayne 2011, the only experimental evidence in this set

DOI 10.1097/acm.0b013e318217e119. Crossref: Academic Medicine, no update. Read: PMC3102783, whole text.

- Design: meta-analysis, "14 studies … 633 learners": residents, medical students and fellows.
- Comparison: simulation-based medical education with DP vs "traditional clinical education or a pre-intervention baseline". Of the 14 studies, 6 are randomized trials and 4 are pre-post baselines (Table 1).
- Result: "overall effect size … 0.71 (95% confidence interval, 0.65–0.76)". The effect is a correlation.
- DP elements (List 1): well-defined objectives, "appropriate level of difficulty", "focused, repetitive practice", "rigorous, reliable measurements", "informative feedback", "mastery standard".
- Scope limit: "primarily addresses acquisition of medical procedural skills. It does not cover … judgment under pressure, medical decision-making … It is not known if the DP model is suited to these skills."
- Confound noted here: the contrast is structured simulation practice against clinical exposure. It is not DP against an equal-time alternative practice, so the DP ingredients are not isolated.
- Outcomes are mostly checklist scores on simulators right after training. One trial is scored on 10 real cholecystectomies.
- Heterogeneity is not reported in the text.
- Grade S3 R2 O1.

### X2. Sonnentag & Kleine 2000, insurance agents, professions

DOI 10.1348/096317900166895. Crossref: J. Occupational and Organizational Psychology, no update.

Read: KOPS repository PDF via the DSpace API, pp. 87–100: methods, results, limitations.

- Sample: n = 100 insurance agents, mean experience 11.7 years. Performance = supervisor ratings.
- Results:
  - "Years of experience … was no significant predictor";
  - "the amount of current time spent on deliberate practice accounted for an additional 6% of variance";
  - "neither the cumulative amount of time spent on supporting activities … nor the cumulative amount of time spent on deliberate practice … accounted for significant percentages".
- Measurement: interview vs 1-week diary "r = .35 … N = 69". In the subsample with regular activities, r = .57 (N = 32).
- "cross-sectional … third variables explanations cannot be ruled out".
- Grade S2 R2 O1. O1: the outcome is a third-party job rating, not a standardized unaided test.

### X3. Sonnentag 1998, professional software designers

DOI 10.1037/0021-9010.83.5.703. Crossref: J. Applied Psychology, no update. Read: KOPS PDF, abstract and hypothesis sections, targeted results.

- "Forty professional software designers … High performers were identified by a peer-nomination method and performance on a design task. Verbal protocol analysis based on a comparison of 12 high and 12 moderate performers".
- Findings: high performers "showed more feedback processing". "High and moderate performers did not differ with respect to length of experience. None of the differences between the two performance groups could be explained by length of experience."
- The paper does not measure DP hours.
- Grade S2 R3 O1.

### X4. Baltes & Diehl 2018, theory of software development expertise

DOI 10.1145/3236024.3236061. Crossref: ESEC/FSE 2018. Read: arXiv 1807.06087v4, abstract and §§4–6, targeted.

- Mixed-methods survey, n = 335 developers. "experience is not necessarily related to expertise" (abstract). Expertise was self-assessed.
- On measurement: "it may be difficult to find objective measures for quantifying expert performance in software development" (§4.1).
- Monitoring: "38.7% of the 204 participants who answered that question said that they regularly monitor their activity". "the most important monitoring activity was peer review" (§5).
- Grade S1 R3 O0. A survey with self-assessment and no performance outcome.

### P1. Practitioner threads, read in full

HN Algolia item 19690959 and lobste.rs /s/uu6v1o.json.

- HN, 2019-04-18, 6 points. The skeptical reply: "programming is against repetition. You'll repeat a piano concert over and over until its perfect … Programming on the other hand relies on reuse". The same thread also offers competitive-programming problems as a candidate DP unit, and rewriting one function several ways and ranking the versions.
- lobste.rs is dated 2016-12-25, score 23. breadth-r2 gives "2019, 26 pts". The thread is mostly practice routines, not skepticism. They include a daily 20-minute exercise streak, rewrite-from-memory of expert code, a personal bug log with targeted drills, and seeking reviewers.
- The skeptical statement there is the linked blog author's summary: "Being a mostly creative medium with an abstract, immeasurable definition of programming skill, deliberate practice for programming can't exist in the same way or to the same extent". It adds: "Some aspects of programming have a clean, short feedback loop … Most aspects of programming have no analogue for programming challenges."
- Grade S1 R3 O0 for both threads. No outcome data.

## Moderators

| moderator | what the texts show | sources |
|---|---|---|
| Domain | Structured practice, corrected: games 24%, music 23%, sports 20%, education 5%, professions 1%. Narrow definition: games r = .50, music .71, sports .58, education .31 (k = 1), professions k = 0 qualifying studies. Professions outside the meta-analyses: current DP +6% variance, cumulative n.s. (insurance agents). Software: no study relates practice to an objective performance measure; experience length does not separate high from moderate professional designers. | M1 via M3; E2; X2; X3 |
| Definition | Structured practice (broad) r ≈ .38 overall (M3 p. 8); purposeful/deliberate (narrow) r = .54. Teacher-guided vs self-guided: r .56 vs .51, p = .64 (E2). Teacher-designed vs practice alone: 23% vs 26% (E3). Two independent datasets from opposing camps agree that the teacher criterion does not raise the correlation. | E2, E3, M3 |
| Measurement | Retrospective estimates overstate diary-logged practice, with equal bias across groups (E1, E3). Estimate–diary agreement: r .60–.75 for the current year (E2); r = .35 in a profession with irregular activities (X2). Beyond ~5 years back, estimates lose reliability (Ward 2007 via E2). The variance explained depends on the assumed reliabilities: the same r = .56 gives 39%–87% (M3 Table 3). In E1 the concurrent diary did not separate the best from the good group; only retrospective totals did. Under blind interviewing (E3) the retrospective totals did not separate them either. No study in this set measures practice prospectively over years. | E1, E2, E3, M3, M4, X2 |
| Skill level | Elite athletes: 1% (M2). Best vs good violinists: n.s. (E3). E2 attributes this to range restriction, but no elite-only sample met its criteria. Both readings predict the same thing: practice amount separates people less as samples get more homogeneous at the top. The 1993 claim "even among elite performers" is the part that fails. | M2, E2, E3 |
| Predictability / feedback validity | Ericsson's own boundary condition is valid, immediate feedback (E1 p. 367; the Tarot example in E4). The predictability moderator of M1 exists only as a dissertation subtitle quoted in E4; it was not read. | E1, E4 |
| Recency | Current or recent practice predicts current performance; cumulative lifetime practice does not, or does less well. Older pianists with ~3× the hours of young experts were not better. | X2; Krampe & Ericsson 1996 via E2 |
| Experimental vs correlational | The only controlled evidence is procedural medical skill: SBME with DP vs clinical exposure, r = .71, immediate simulated outcomes, DP ingredients not isolated. The correlational literature cannot say whether practice causes skill, or whether skill and motivation cause practice (M4's inflation concern; X2's own limitation). | X1, M4, X2 |

## Verdict

Dispute 1. Both sides are right under different conditions:

- Ericsson's side holds for this: goal-directed solitary practice with feedback correlates substantially with attained, objectively measured performance, in domains with an established training tradition (games, music, sports).
  - Narrow definition: r ≈ .50–.71 (E2, E5).
  - Broad definition: 20–24% of variance (M1 corrected).
  - The one controlled literature, procedural medicine, shows large gains over unstructured clinical exposure (X1).
- Macnamara and Hambrick's side holds for this: the 1993 strong claims fail.
  - The blind preregistered replication did not separate the best from the good violinists (E3).
  - Elite sports: 1% (M2).
  - Professions: 1% broad (M1), and zero qualifying studies narrow (E2).
  - Hours to chess master vary about 8-fold (M3).
  - "Impossible … to catch up" (E1 p. 393) is contradicted by E3's data and by the 1993 confidence interval that E3 cites.
- The dispute is not resolvable at the level of "X% of variance". Across definitions and reliability assumptions, estimates run from 14% (broad, uncorrected) to 87% (narrow, low assumed reliability). The data from both camps fit inside that band. What moves the number is the definition and the measurement model, not new observations.
- Where the camps' data converge:
  - practice amount matters, and more for non-elite samples;
  - the teacher-design criterion adds nothing measurable (E2, E3);
  - recent practice beats lifetime totals (E2, X2);
  - retrospective hours are a biased, reliability-limited instrument (E1, E2, E3).

Dispute 2, whether DP applies to programming: UNRESOLVED on evidence.
- No source in the tree measures any practice type against an objective programming performance outcome.
- The practitioner objections restate DP's own preconditions:
  - "against repetition" = E4 criterion 4;
  - "immeasurable definition of programming skill" = E2 criterion 1 (reproducible performance), which also emptied the professions category (k = 0);
  - no established training methods = E1 p. 368 and criterion 5.
- Criterion 5 carries no measured weight in the correlational data (Definition row). So "programming lacks teachers with a centuries-old curriculum" says little about whether purposeful practice (criteria 1–4) works there.
- The two conditions with support elsewhere are the ones programming sub-skills differ on: a measurable target performance and immediate valid feedback.
- The evidence closest to the domain (X3) finds that feedback processing, not years of experience, separates high from moderate professional designers. That is n = 24 compared, cross-sectional.
- One practitioner claim is checkable and unmeasured: some sub-skills have "a clean, short feedback loop" and most do not.

## Impact on claims

| claim / record | before | after | why |
|---|---|---|---|
| N6-r2-02 (Krampe & Ericsson 1996, maintenance predicted by later-adulthood DP) | SURVEYED, S2 R2 O2, abstract | SURVEYED, unchanged | Primary not re-read. Consistent with E2's description ("last 10 years … best predicted"; 57,739 vs 17,927 h, "not superior") and with X2 (current, not cumulative). Tier 3 should read the primary before VERIFIED. |
| index expertise #3 / coaching #2 / cross-field #3 (Macnamara 2014 one-liner: 26/21/18/4/<1) | as written | correct to 24/23/20/5/1, overall 14% | Crossref marks 10.1177/0956797614535810 `updated-by: correction` (10.1177/0956797618769891). The corrected values come from the same authors in M3 p. 5. The index quotes the uncorrected abstract. |
| index expertise #4 (corrigendum "Corrects computational errors in #2") | as written | should reference #3 | #2 is Ericsson 1993; the corrigendum's update-to is the Macnamara 2014 DOI. |
| index expertise #11 ("Hambrick, Macnamara & Oswald 2014 … defending #2/#5 against Ericsson's rebuttals") | as written | authors Hambrick, Altmann, Oswald, Meinz & Gobet; a commentary on Platz et al. 2014 | Crossref author list; the text opens "A commentary on … Platz". |
| index coaching #23 ("triggers Ericsson's 2020 reply") | as written | Ericsson 2020 replies to Macnamara & Hambrick 2020, Psychol Res | E4 abstract: "In their commentary, Macnamara and Hambrick (Psychol Res…)". |
| index coaching #22 ("defends the original narrow definition") | as written | holds; add that it re-includes 7 of 8 DP effects Ericsson 2014a had rejected | M3 Table 2. |
| n5-r2 disagreement note (Macnamara 2016, "effect smaller for elite") | "to verify" | abstract-read: 1% among elite; no full text | M2 abstract. |
| breadth-r2 high-signal find (DP for programmers) | "two independent venues converging on the same skepticism", lobste.rs "2019, 26 pts" | lobste.rs 2016-12-25, score 23; mostly practice routines; skepticism = one HN reply plus one blog summary | P1 full JSON read. |
| ledger codekata row (breadth-r1, "kata as DP unit") | S1 R3 O0 | unchanged | No outcome data exists for it. It is also an instance of the unverified Dispute 2. |

New claims proposed for Tier 3. Not appended to the ledger: this prompt does not authorize ledger writes.

| id | claim | best source | S R O | population |
|---|---|---|---|---|
| DP-R-01 | Under blind, preregistered retrospective interviewing, accumulated solitary practice did not differ between best and good conservatory violinists (d = −0.38, p = .364); overall group variance explained was 26% vs the original 48%. | E3 | 2 2 2 | young-adult conservatory violinists, n = 39 |
| DP-R-02 | Teacher-guided and self-guided goal-directed practice correlate equally with attained performance (r .56 vs .51, p = .64; 23% vs 26%). | E2, E3 | 3 2 2 | games, music and sports samples; violinists |
| DP-R-03 | In a profession (insurance sales), current DP added 6% of variance in supervisor-rated performance; cumulative DP and years of experience did not predict. | X2 | 2 2 1 | adult professionals, n = 100 |
| DP-R-04 | High- vs moderate-performing professional software designers differed in feedback processing and local planning, not in years of experience. | X3 | 2 3 1 | professional software designers, 12 vs 12 |
| DP-R-05 | Simulation-based practice with DP components beat traditional clinical education for procedural medical skills, pooled r = .71 (14 studies, 633 learners); non-procedural skills untested. | X1 | 3 2 1 | medical residents and students |
| DP-R-06 | Variance explained by DP is not identifiable from current data: 14% (broad, uncorrected) to 61–87% (narrow, corrected), depending on definition and assumed reliability. | M3 Table 3, E2, M1 | 3 2 2 | pooled expertise samples |

## What this means for practice units for adult CS-adjacent learners (evidence only)

- Accumulated hours are the instrument the whole dispute rests on. That instrument is:
  - retrospective;
  - biased upward;
  - reliable to about 0.6–0.8 for the last year or two;
  - weaker for irregular activity (r = .35 when activities are not weekly, X2).
- An irregular-burst adult practice pattern is the case where the instrument does worst.
- Recent practice predicts current performance better than lifetime totals (X2; Krampe & Ericsson via E2).
- The ingredients with support are the four task conditions: a clear goal, performable alone, immediate informative feedback, and repetition of the same or similar tasks (E1 p. 367, E4). Evidence for them:
  - correlational in music, games and sports (E2, E5);
  - controlled only in procedural medicine, and not isolated from "more structured practice" (X1).
- Task-specific practice predicts task-specific performance better than generic practice in the same domain (E5 p. 4; Lehmann & Ericsson 1996 via E2).
- Who designs the practice, teacher or performer, shows no measurable difference in two datasets from opposing camps (E2, E3). No source here tests an automated or LLM designer.
- For professional software work, the one process study finds feedback processing, not tenure, separating high from moderate performers (X3). Survey respondents name peer review as their main feedback source; 38.7% report regular self-monitoring (X4).
- No source measures a practice-to-outcome relation for programming.
- An objective, reproducible performance measure is DP's first criterion (E2). It is also what both camps' meta-analyses needed to count a study at all. For software, this measure is named as missing by an academic source (X4) and by a practitioner source (P1). An evidence map that wants to test practice effects in this domain depends on the unaided performance probe (N1) existing.
- Effort is rated high and enjoyment middling, not low, for solitary practice in both violin samples (E3 Table 5). The 1993 claim "not inherently enjoyable" is not what the ratings show. This bears on sustainability (N6).
- Range: the correlations are larger in mixed-skill and sub-elite samples than in elite ones (M2, E3). Adult novices to intermediates sit in the range where practice amount separates people most, though no study in this set sampled that population in a CS-adjacent domain.

## Unread leads

- Macnamara, Hambrick & Oswald 2014 full text: closed. Holds the predictability and measurement-method moderators.
- Macnamara 2014 dissertation, Princeton: not found in DataSpace.
- Kahneman & Klein 2009, 10.1037/a0016755: closed. Predictability of the environment as a condition for expertise.
- Macnamara, Moreau & Hambrick 2016 full text: closed.
- Plant, Ericsson, Hill & Asberg 2005: closed.
- Hambrick et al. 2014, Intelligence: closed.
- Charness et al. 2005: closed.
- Miller et al. 2018 reanalysis: not located.
- "Deliberate Practice in Programming", ECSEE 2020, 10.1145/3396802.3396815: closed.
- "Integrating Deliberate Practice in Software Engineering Education", ICERI 2024, 10.21125/iceri.2024.1331: closed.
- Zhou & Mockus, developer task-difficulty progression, cited in X4: not resolved.
- Krampe & Ericsson 1996 primary: carried via E2 only.

## Notification summary

Wrote ROOT/resolve/deliberate-practice-resolution.md: 13 sources checked (11 full texts, 2 abstract only) plus 2 practitioner threads read in full, 12 unread leads listed, about 65 API calls, 6 new claims proposed and 9 index/ledger/claim corrections. Verdict on how much deliberate practice explains: both camps are right under different conditions. Goal-directed practice with feedback correlates substantially with measured performance in games, music and sports (r ≈ .5–.7 under the narrow definition), but the 1993 strong claims fail: the blind replication, elite athletes (1%) and professions (1%, and zero qualifying studies under the narrow definition) all contradict them, and the "variance explained" figure moves between 14% and 87% depending on the definition and the assumed reliability of retrospective hours. Whether it applies to programming is unresolved: no study measures practice against objective programming performance, the practitioner objections restate deliberate practice's own preconditions, and the teacher criterion those objections lean on shows no measured effect in either camp's data.
