# 2026-09-26

memento setup for gym, on the owner's request to follow competera's 2026-09-24 records refactor, joined with a spec-chef pass over the owner's two notes.

The owner handed gym's content and the project to Claude and ruled that doc/TASK.md and doc/SPEC.md dissolve into their own homes. Both originals sit whole in docs/orchestration_log/archive/. Questions reach the owner only inside the question tool (docs/conventions.md `questions-in-the-tool`).

Round 1 settled the layout (the opinion map's spec read on need), one standing goal (gym), the split between the map's architecture (docs/opinion-map.md) and its subjects (docs/subjects/, Rust first, depth and breadth set by the owner), and self-location's demotion to a possible application of a map. The map's focus became informing the user and exposing them to what they don't necessarily like.

Round 2 kept the map's three jobs and dropped the Deliberation test, leaving the tests' setup open with the owner; left any competera carry-over to the owner; set gym's operating model — an orchestrator that runs the administration and spawns elite trainer subagents the owner converses with, each able to bind its own manifesto stack; and put gym's administration on Python launched with uv. competera's three record scripts were ported; the linter caught 35 of 35 planted violations.

Gaps the spec pass found and did not put to the owner, for the map's research stage: no tie-break rule for duplicate extraction; no rule on where an Argument may come from, while every Claim needs a retrieved Source; who may open the map's site, given it names real people; no method for picking a Position's most-heard advocate; whether the Value set is closed or grows; whether Schools are stored or computed; and what check makes the practice "verifiably aligned" (Goal 1).

Round 3 set the commit discipline and the orchestrator's manifesto stack: competera's `you` block without the polars manifesto and dev-orchestration. The owner ratified every record standing on 2026-09-26 and queued two research tasks for the next session, run in parallel: the single best way of teaching, and Rust. Three questioning failures are in failures.md.

## Close — 2026-09-26T22:39

HEAD    3baf1a3 (dirty: docs/orchestration_log/history/2026-09-26/events.md, docs/orchestration_log/history/2026-09-26/session.md, docs/orchestration_log/history/2026-09-26/failures.md)
state   memento set up and ratified 2026-09-26; records lint clean
        orchestrator stack: stop-yapping, first-principles, cargo-cult-science, simple-made-easy, agentic-delegation
        no trainer yet
open    none: no tripwires, no delegations; commits local, none pushed
next    bind, memento:init; then both research tasks in parallel, the best way of teaching and Rust (docs/user_deferred_items.md)
