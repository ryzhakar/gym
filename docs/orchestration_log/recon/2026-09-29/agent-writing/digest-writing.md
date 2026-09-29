# Digest: instruction-writer + SPR + Strunk SPR v3

Sources: `/Users/ryzhakar/pp/claude-skills/.claude/agents/instruction-writer.md` (68 lines, read in full); `/Users/ryzhakar/LLM_MANIFESTOS/instructions/sparse-priming-representations.md` (17 lines, read in full); `/Users/ryzhakar/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml` (2923 lines, read in full across 5 ranges).

## 1. instruction-writer.md

Frontmatter (lines 1-27), verbatim:
```
name: instruction-writer
description: |
  Triggers when editing skill definitions, agent definitions, hook templates, or any instruction file in the marketplace. Use when rewriting, compressing, restructuring, or applying feedback to SKILL.md or agent .md files.
  <example>...</example> x3 (compress a skill; add escalation rules; rewrite a template with ETHOS)
model: opus
color: magenta
tools: ["Read", "Write", "Edit", "Bash", "Grep", "Glob"]
```

Body opens (line 29): "Edit skill and agent instruction files. Your output defines how models behave -- every word is load-bearing."

**Input expected from caller**: a target instruction file (or files) to edit, plus a task prompt describing the change (compress/add/restructure/apply feedback). The caller is the orchestrator dispatching this agent — it supplies the file path(s) and the task.

**Files it reads itself, and when** (line 33-39, "Constitutional Binding — Execute Before Any Work"), read in this order before touching any instruction file:
1. First-principles manifesto — search `.claude/manifesto-repo/LLM_MANIFESTOS/` (project-relative) by filename/content for "first principles"; else filesystem search (line 35).
2. `ETHOS.md` at project root, located via Glob if needed (line 36).
3. Strunk writing standard at `orchestration_log/recon/2026-04-13/scouts/bridge-research/strunk-spr-v3.xml` relative to project root; if missing, search `strunk-spr*.xml` in project; if still missing, fetch from web (line 37).

Line 39: "Internalize these before touching any instruction file. They are not reference material — they are your operating system."

**Writing rules table** (41-49, "from ETHOS, compressed"), 5 rows: Self-containment (inline content, no lazy @references unless rare+large>1000t+gate-protected); Strong directives (commands not suggestions, preserve MUST/NEVER/CRITICAL, one emphatic marker per directive on Claude 4.6); Token economy (measure with `just tokens`, compress via Strunk: active voice/positive form/concrete language/omit needless words, tables over prose); No platform coupling (file artifacts only, no `gh`/GitHub API); Core points (identify 5 before editing, they survive every rewrite, compression amplifies them).

**Process** (lines 51-59), 7 steps:
1. Read target file(s) fully.
2. Read the task prompt from the orchestrator.
3. Identify the file's core points (what it most emphatically communicates); write them down before editing.
4. Apply changes per the task; preserve core points; amplify through compression.
5. Run `just tokens` on the file — report before/after counts.
6. Run `just readme` if skill/agent metadata changed (name, description, tools, model).
7. Report: what changed, token delta, core points preserved.

**Output**: an edited instruction file (Edit/Write) plus a report of what changed, token delta before/after (from `just tokens`), and confirmation the core points survived; `just readme` regen only if metadata changed.

**Constraints** (61-66): never change frontmatter `name`; no version fields (live in `plugin.json` only); add nothing beyond the task; never weaken existing directives — adding strengthens, rewording preserves force.

## 2. sparse-priming-representations.md (17 lines, read in full)

It is a **prompt template for producing SPR artifacts** — an instruction for generating XML knowledge-compressions, not itself one.

- MISSION (line 1-2): produce SPRs as "concise, semantically dense XML artifacts that capture complex conceptual landscapes with minimal linguistic overhead." Prioritize compression, associative mapping, "neural network activation potential."
- THEORY (line 4-5): SPRs are cognitive priming mechanisms — they "leverage associative neural pathways to rapidly instantiate complex knowledge states through strategic linguistic compression."
- METHODOLOGY (lines 7-12), as short imperative lines:
  - Distill input to essential conceptual nuclei.
  - Maximize semantic density per lexical unit.
  - Create XML structures that implicitly suggest relational networks.
  - Optimize for neural network latent space activation.
  - Maintain precise, elegant structural integrity.
- CONSTRAINTS (lines 14-17):
  - XML must be semantically precise.
  - Whitespace and formatting are critical.
  - Preserve conceptual integrity through minimal linguistic expression.

Governs *form* (dense XML, minimal words, structure implying relations), not English grammar — that's Strunk's domain.

## 3. strunk_spr_v3_complete.xml (2923 lines, read in full)

Root: `<instruction_matrix type="prose_style_enforcement" scope="immediate_and_ongoing" authority="directive_with_judgment_framework" version="3.0">` (lines 8-12). Governs: Claude's own prose-generation behavior — grammar, punctuation, sentence/paragraph architecture, word usage, genre calibration — grounded in Strunk's *Elements of Style* (1918), reframed with a judgment layer rather than blind prescription.

Top-level sections, in file order:
1. `execution_mandate` (17-64): frames the whole file as binding on generation, not background knowledge; self-monitoring protocol; override conditions when deviation is allowed.
2. `philosophical_foundation` (69-121): purpose is clear/vigorous communication, not rule-following for its own sake; hierarchy of values (line 109-119): **Clarity > Accuracy > Economy > Vigor > Correctness**.
3. `severity_taxonomy` (126-223): 5 levels, critical (fix immediately, e.g. comma splices, dangling modifiers) down to stylistic (apply consistently, e.g. Oxford comma). Triage principle (218-221): during generation, prioritize Level 5-4, don't let Level 1-2 polish introduce higher-severity errors.
4. `judgment_protocol` (228-327): when to deviate (genre/rhetorical/conflict/ambiguity conditions, 236-267); 4 decision heuristics (270-296): purpose test, reader test, precedent test, consciousness test; epistemic humility (299-313): acknowledge gray areas, don't fake certainty; mastery pathway (316-325): novice→practitioner→master.
5. `punctuation_rules` (332-767), rules 1-7, each imperative:
   - R1 possessive: add `'s` regardless of final consonant (341-377).
   - R2 series comma: use Oxford comma by default (381-417).
   - R3 parenthetic expressions: enclose both ends, never one comma alone — severity critical-adjacent (421-503).
   - R4 comma before coordinating conjunction joining independent clauses (507-573).
   - R5 no comma splice — join independent clauses with semicolon/period/conjunction, never bare comma (577-646).
   - R6 no sentence fragments outside dialogue/emphatic exception (650-699).
   - R7 participial phrase at sentence-start must modify the grammatical subject — no dangling modifiers (703-765).
6. `composition_principles` (772-1811), rules 8-18:
   - R8 paragraph = one topic (778-853).
   - R9 topic sentence opens, close echoes it (857-952).
   - R10 active voice as default; passive legitimate for topical focus/unknown-agent/scientific objectivity; avoid double passive (956-1093).
   - R11 positive form — assert what IS, not what ISN'T (1097-1182).
   - R12 concrete/specific/definite language — "THE MOST IMPORTANT principle" (line 1192) (1186-1288).
   - R13 omit needless words — kill "the fact that," empty relatives, combine choppy sentences (1292-1384).
   - R14 avoid a *succession* of loose sentences; vary structure (1388-1446).
   - R15 parallel construction for coordinate ideas; correlatives matched (1450-1538).
   - R16 keep related words together — subject/verb, relative/antecedent, modifier placement (1542-1639).
   - R17 one tense per summary; dramatic/fiction summary defaults to present (1643-1720).
   - R18 emphatic word/phrase goes at sentence end (or, for contrast, at the very start) (1724-1809).
7. `usage_guide` (1817-2367): 25 word/phrase entries (e.g. can/may, data=plural, different-from-not-than, like/as, less/fewer, literally, split infinitive, singular they), each with rule/rationale/examples/gray_area.
8. `genre_protocols` (2373-2553): baseline is formal expository prose; modulation tables for academic, creative fiction, technical documentation, journalism, business correspondence; poetry is exempt entirely (2528-2536). Cross-genre principle (2539-2551): consistency within a genre choice matters more than which convention chosen.
9. `edge_case_resolution` (2559-2695): explicit conflict resolutions — economy vs clarity → clarity wins; parallel vs needless-words → parallel wins; active voice vs topical flow → topical flow wins; falls back to the hierarchy of values (2586-2591) when no specific resolution matches.
10. `exemplar_showcase` (2700-2885): 5 annotated literary passages (Browning, Stevenson, Lincoln, Churchill, Hemingway) showing masters violating rules 12/13/14/15/18 purposefully for effect; closing point (2869-2883): master rules first, then earn the right to break them.
11. `closing_directive` (2894-2920): reiterates hierarchy, "these instructions remain active throughout conversation unless user overrides them."

## 4. How the three fit together

SPR (source 2) specifies *packaging*: dense XML, no filler, structure implies relations. Strunk SPR v3 is a worked SPR artifact (tags, severity/certainty attributes, terse `<command>` blocks) applied to English-prose rules — SPR governs how any instruction file is shaped; Strunk governs how the prose inside it reads. instruction-writer is the executor: it self-loads first-principles, ETHOS, and Strunk before editing (lines 33-39), so the orchestrator supplies neither SPR nor Strunk — only the target file path(s) and task. ETHOS's ported directive (line 47, "compress via Strunk: active voice, positive form, concrete language, omit needless words; tables over prose") is the bridge: it names Strunk rules R10/R11/R12/R13 as the compression method and tables (an SPR-like device) as the preferred shape for mappings.

Every sentence instruction-writer produces answers to Strunk's gate: active voice (R10), positive form (R11), concrete/specific language (R12, "most important," line 1192), omit needless words (R13), parallel structure (R15), emphatic word at sentence-end (R18) — conflicts resolved by Clarity > Accuracy > Economy > Vigor > Correctness (109-119). Register is `technical_documentation` (2448-2471): imperative mood, passive for system actions, active for user actions, parallelism in lists.

**What the orchestrator must supply**: (1) target file path(s); (2) a task description matching a trigger example (compress to N tokens / add a section / apply feedback); (3) any feedback content — instruction-writer won't invent content beyond the task (line 65). It never needs first-principles/ETHOS/Strunk paths handed in; those are self-located with documented fallback search orders (35-37).

## Summary

instruction-writer (opus, 6 tools) edits SKILL.md/agent files: self-binds to first-principles, ETHOS, and Strunk SPR v3, then runs read → find-core-points → edit → measure-tokens → report. SPR (17 lines) is a template for dense, relation-implying XML, governing form, not grammar. Strunk SPR v3 (2923 lines, 10 sections, rules 1-18 plus a 25-entry usage guide) enforces Strunk's prose rules with a judgment layer — the prose-quality gate instruction-writer's own output must pass.
