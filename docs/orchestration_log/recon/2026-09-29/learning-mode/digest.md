# Digest — Learning / Explanatory / plugin behaviors

Refs: `learning-output-style.md` (L), `explanatory-output-style.md` (E), `plugin-learning-output-style.md` (P).

## Learning style (L:25-103)

- Trigger threshold: "ask the human to contribute 2-10 line code pieces when generating 20+ lines involving" design decisions, business logic with multiple approaches, key algorithms/interfaces (L:32-35).
- Track the ask: put "a specific todo item like 'Request human input on [specific decision]'" in the TodoList when planning one (L:37).
- Mark before asking: "You must first add a TODO(human) section into the codebase with your editing tools before making the Learn by Doing request" — "one and only one TODO(human) section" (L:54-55).
- Fixed request shape: `**Context:**` / `**Your Task:**` (file + TODO(human), no line numbers) / `**Guidance:**` under a `● **Learn by Doing**` header (L:44-50).
- Hand back and stop: "Don't take any action or output anything after the Learn by Doing request. Wait for human implementation before proceeding." (L:56).
- After the human writes it: "Share one insight connecting their code to broader patterns or system effects. Avoid praise or repetition." (L:93-94).
- Tone: "collaborative and encouraging," balance completion with learning (L:28).
- Also carries the Insight-block behavior verbatim (L:96-102), identical to Explanatory's.

## Explanatory style (E:22-35)

- No hand-back, no TODO(human), no human-authored code — Claude keeps writing everything.
- Governs one behavior only: insight blocks "before and after writing code" — fenced `★ Insight ─...─` / 2-3 points / `─...─` — "included in the conversation, not in the codebase," specific to "the codebase or the code you just wrote, rather than general programming concepts" (E:29-34).
- Tone license: "you may exceed typical length constraints, but remain focused and relevant" (E:25).

## Plugin: learning-output-style (P:66-... unescaped block)

- Same trigger frame as L but phrased as philosophy, not a hard line count/threshold: "identify opportunities where the user can write 5-10 lines of meaningful code that shapes the solution" (P:70).
- Contribution categories match L's list almost 1:1, expanded to six: business logic, error handling, algorithm choice, data structures, UX decisions, design patterns/architecture (P:74-80).
- Request protocol adds prep steps L doesn't specify: "Create the file with surrounding context," add a signature, comment the purpose, "Mark the location with TODO or clear placeholder" — then explain what/why, reference file+location, give trade-offs, frame as valuable not busy-work, keep it 5-10 lines (P:82-... "How to Request Contributions" / "When requesting").
- Explicit exclusion list L lacks: don't ask for "boilerplate," "obvious implementations," "configuration or setup code," "simple CRUD operations" (Balance section).
- Folds Explanatory in wholesale, same insight-block format, plus one instruction E doesn't have: "Provide insights as you write code, not just at the end."
- No TODO(human) requirement, no "wait, do nothing further" hand-back rule — those are L-only.

## Harness-bound vs. portable

Harness-bound (assumes output-style machinery / hooks / a live main session, none of which a subagent has):
- L/E as *named modes* selected via `outputStyle` and merged with `keepCodingInstructions` (both files' front matter) — a subagent has no mode switch to select.
- P's entire delivery mechanism: a `SessionStart` hook writing `hookSpecificOutput.additionalContext` (P:23-41) — subagents aren't sessions with hooks; this only fires once per interactive session start.
- L's TodoList-integration instruction (L:37-42) assumes the interactive CLI's TodoWrite/TodoList feature.
- L's literal "wait for human implementation before proceeding" (L:56) assumes a human is present turn-by-turn — a trainer subagent talking to Arthur has this, but a subagent used for anything else does not.

Portable to a subagent's own system prompt (pure text, no harness dependency):
- The trigger heuristic (what counts as worth a hand-back) and the exclusion list (P's Balance section) — reusable as-is.
- The Request Format template (Context/Your Task/Guidance) and the TODO(human) convention.
- The Insight-block format and its content rule (codebase-specific, not generic) — both L and E's version, P's "as you write, not just at the end" refinement.
- The tone lines ("collaborative and encouraging," "frame as valuable input... not busy work").

## Overlap / differences

- L and P overlap almost completely on *what* to ask for; P is the more operational one — it adds prep steps and an explicit don't-ask list that L leaves implicit.
- L is stricter about the TODO(human) mechanic (exactly one, added before asking, no line numbers) — P never mentions TODO(human) by name, just "TODO or clear placeholder."
- E is a strict subset of P: P = L's request protocol + E's insight blocks, merged, per its own README ("combines the unshipped Learning output style with explanatory functionality").
- Only L has the hard hand-back rule (stop after asking); P implies it but never states "do nothing further" as explicitly.
