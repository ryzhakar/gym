# Exclusion register

Fetched: 2026-09-27.

Method note: every DOI below resolved directly against Crossref (retraction/original pair via
`update-to`) or Crossref bibliographic search. Retraction *reasons* came from the publisher's
retraction notice via WebSearch, not a full-text read of the notice PDF — flagged per entry where
the reason is secondary-source or unconfirmed. No `full_text_read` claims are made for the
underlying studies themselves; this register checks exclusion status, not the papers' findings.

## Queries

| query | database | hits |
|---|---|---|
| `update-type:retraction` + "learning" | Crossref | 3051 |
| `update-type:retraction` + "education" | Crossref | 2384 |
| `update-type:retraction` + "tutoring coaching expertise" | Crossref | 15 |
| `update-type:retraction` + "deliberate practice" | Crossref | 548 |
| `update-type:retraction` + "expertise acquisition skill" | Crossref | 126 |
| `update-type:retraction` + "retrieval practice spaced learning feedback" | Crossref | 3743 |
| bibliographic: Pashler learning styles concepts evidence | Crossref | 1 match |
| bibliographic: Kirschner stop propagating learning styles myth | Crossref | 1 match |
| bibliographic: Melby-Lervåg Hulme working memory training effective | Crossref | 1 match |
| bibliographic: Sala Gobet working memory training typically developing | Crossref | 1 match |
| bibliographic: Simons do brain-training programs work | Crossref | 1 match |
| bibliographic: Witkowski 35 years NLP research | Crossref | 1 match |
| bibliographic: Sturt NLP systematic review health outcomes | Crossref | 1 match |
| bibliographic: Hyatt Brain Gym building stronger brains | Crossref | 1 match |
| bibliographic: Spaulding Mostert Beam Brain Gym effective | Crossref | 1 match |
| bibliographic: Howard-Jones neuroscience education myths messages | Crossref | 1 match |
| bibliographic: Hines left brain right brain mythology management training | Crossref | 1 match |
| bibliographic: Corballis left brain right brain facts fantasies | Crossref | 1 match |
| bibliographic: Allinson Hayes cognitive style index organizational research | Crossref | 1 match |
| "Lumosity efficacy cognitive training" | OpenAlex | 0 (daily budget exhausted, no API key) |
| "FTC Lumosity settlement deceptive advertising" | WebSearch | web |
| "PhotoReading independent scientific evaluation" | WebSearch | web |
| "HBDI independent validation criticism" | WebSearch | web |
| retraction-reason lookups (7 titles, one search each) | WebSearch | web |

## Entries

| # | work or claim | criterion | check run | evidence (DOI/URL, quote ≤25 words) |
|---|---|---|---|---|
| 1 | Sternberg & Grigorenko, "Successful Intelligence in the Classroom," *Theory Into Practice* | 1 | Crossref retraction filter, query "education" | 10.1207/s15430421tip4304_5, retraction 10.1080/00405841.2018.1547600 (2018-11-27). Reason: prior near-identical publication elsewhere; "scientific content... was not in question" (secondary source, Retraction Watch). |
| 2 | Ferdik, "A Cluster Randomized Experiment of a Life Coaching Intervention Designed to Improve Correctional Officer Mental Health," *Criminology & Public Policy* | 1 | Crossref retraction filter, query "tutoring coaching expertise" | 10.1111/1745-9133.70000, retraction 10.1111/1745-9133.70014 (2026-03-01). "unresolved inconsistencies were identified that prevented the study's results from being independently reproduced" (secondary source). |
| 3 | Lichtenthaler, "The Role of Deliberate and Experiential Learning in Developing Capabilities: Insights from Technology Licensing," *J. Eng. Technol. Manage.* | 1 | Crossref retraction filter, query "deliberate practice" | 10.1016/j.jengtecman.2011.10.001, retraction 10.1016/j.jengtecman.2014.08.001 (2014-09-17). "discussions about the presentation of the empirical results following an investigation" (secondary source). |
| 4 | Yu, "Meta-analyses of effects of augmented reality on educational outcomes over a decade," *Interactive Learning Environments* | 1 | Crossref retraction filter, query "learning" | 10.1080/10494820.2023.2205899, retraction 10.1080/10494820.2024.2387893 (2024-08-06). "retracted at the request of the author who now believes it to require major revision" (secondary source). |
| 5 | Cao & Yu, "The impact of augmented reality on student attitudes, motivation, and learning achievements — a meta-analysis (2016–2023)," *Humanities and Social Sciences Communications* | 1 | Crossref retraction filter, query "learning"; cross-check on entry 4 | 10.1057/s41599-023-01852-2, retraction note 10.1057/s41599-024-03826-4. Retracted for "substantially overlap[ping]" with entry 4, same author; authors disagreed with the retraction (secondary source — see Contested). |
| 6 | "Effects of retrieval schedules on the acquisition of explicit, automatized-explicit, and implicit knowledge of L2 collocations," *Studies in Second Language Acquisition* | 1 | Crossref retraction filter, query "retrieval practice spaced learning feedback" | 10.1017/s0272263124000780, retraction/corrigendum 10.1017/s0272263125000087 (2025-01-27). Crossref record itself titled "CORRIGENDUM – RETRACTION"; publisher reason not located beyond the notice's existence. |
| 7 | "A test of the variability vs. specificity hypotheses in the retention of a motor skill," *Human Movement Science* | 1 | Crossref retraction filter, query "expertise acquisition skill" | 10.1016/j.humov.2019.03.011, marked WITHDRAWN in Crossref/PubMed (PMID 31272696); a differently-dated version (2025) exists at a separate DOI. Withdrawal reason not located. |
| 8 | Learning-styles matching hypothesis (instruction tailored to a learner's preferred "style" improves outcomes) | 4 | Two independent S4 reviews located and DOI-resolved | Pashler, McDaniel, Rohrer & Bjork (2008), 10.1111/j.1539-6053.2009.01038.x, *Psychological Science in the Public Interest*: no credible evidence for the meshing hypothesis. Kirschner (2017), 10.1016/j.compedu.2016.12.006, *Computers & Education*, "Stop propagating the learning styles myth." Corroborating: Howard-Jones (2014), 10.1038/nrn3817, *Nature Reviews Neuroscience*, lists learning styles among neuromyths. |
| 9 | Left-brain/right-brain hemisphere dominance drives learning or teaching style | 4 | Two independent S4-grade reviews located and DOI-resolved | Hines (1987), 10.2307/258066, *Academy of Management Review*, "Left Brain/Right Brain Mythology and Implications for Management and Training." Corballis (2014), 10.1371/journal.pbio.1001767, *PLoS Biology*, "Left Brain, Right Brain: Facts and Fantasies." Corroborating: Howard-Jones (2014), 10.1038/nrn3817. |
| 10 | Computerized "brain-training" programs produce far transfer to untrained cognitive abilities (incl. commercial products such as Lumosity) | 4 | Two independent S4 meta-analytic reviews located and DOI-resolved | Melby-Lervåg & Hulme (2013), 10.1037/a0028228, *Developmental Psychology*: no evidence of far transfer. Simons et al. (2016), 10.1177/1529100616661983, *Psychological Science in the Public Interest*, consensus review: "little evidence that training generalizes." Corroborating: Sala & Gobet (2017), 10.1037/dev0000265. Regulatory corroboration: FTC v. Lumos Labs (2016) found the company's transfer claims "unfounded." |
| 11 | Neuro-Linguistic Programming (NLP) techniques work via their claimed mechanism (used in coaching/tutoring practice) | 4 | Two independent systematic reviews located and DOI-resolved | Witkowski (2010), 10.2478/v10059-010-0008-0, *Polish Psychological Bulletin*: "the basic assumptions of NLP" are "not empirically supported." Sturt et al. (2012), 10.3399/bjgp12x658287, *British Journal of General Practice*: "no good-quality evidence that NLP interventions improve health-related outcomes." |
| 12 | Brain Gym / Educational Kinesiology movement exercises improve learning via the claimed neurological mechanism | 4 | Two independent reviews located and DOI-resolved | Hyatt (2007), 10.1177/07419325070280020201, *Remedial and Special Education*: claims "far exceed... the existing evidence base." Spaulding, Mostert & Beam (2010), 10.1080/09362830903462508, *Exceptionality*: "no...credible, scientific evidence" for the program's claims. |
| 13 | PhotoReading (Paul Scheele / Learning Strategies Corp.) — claimed reading rates to 25,000 wpm via "whole-mind" processing | 2 | WebSearch for independent peer-reviewed evaluation; none located | No peer-reviewed published research supporting the efficacy claim was found. The one existing study (NASA-commissioned, McNamara, unpublished, https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20000011599.pdf) found PhotoReading took no less time than normal reading and did not support the 25,000-wpm claim; developer dismissed the study. |
| 14 | Herrmann Brain Dominance Instrument (HBDI) / "Whole Brain Thinking" — commercial assessment marketed for training/learning design efficacy | 2 | OpenAlex citing-works search attempted (blocked, no API key); WebSearch + Crossref-resolved peer-reviewed source found instead | Allinson & Hayes (1996), 10.1111/j.1467-6486.1996.tb00801.x, *Journal of Management Studies*: "little or no published independent evaluation" of self-report training instruments including HBDI. Cross-refs entry 9 (mechanism it invokes). |

## Contested (evidence split; not excluded) — one line each

- Cao & Yu AR meta-analysis (entry 5): authors publicly disagreed with the retraction as unwarranted overlap-finding — status stands per Crossref but the "duplication" judgment itself is disputed by the authors.
- Sternberg "Successful Intelligence in the Classroom" (entry 1): retraction is a publication-record matter (duplicate publication), not a finding that the classroom-application claims are false — excluded here on criterion 1's letter, not on refuted substance.
- Growth mindset interventions: large multi-site RCTs (e.g., National Study of Learning Mindsets) and meta-analyses disagree on effect size and moderators; not excluded — S4 evidence is split, not convergent refutation.
- Lumosity specifically: an independent RCT exists (Kable et al. 2017, *J. Neuroscience*, S3, not a review) finding no transfer benefit — evaluation is locatable, so criterion 2 ("no third-party evaluation locatable") does not strictly apply; listed instead under entry 10's general brain-training refutation with FTC action as corroboration, not as its own S0 line.

## Statistics

Total: 14. By criterion: criterion 1 (retracted/expression of concern) = 7; criterion 4 (mechanism refuted by ≥2 independent S4 reviews) = 5; criterion 2 (commercial claim, no third-party evaluation locatable) = 2; criterion 3 (no primary data, no citation) = 0 found.
