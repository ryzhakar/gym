# Digest — agents-reference.md

Source: `/Users/ryzhakar/pp/claude-skills/orchestration_log/reference/agents-reference.md` (2799 lines).

## 1. What it is

Reference manual for Claude Code's platform contract on plugin-defined agents (subagents): definition, discovery, dispatch, execution, termination (L13). Generated from a multi-agent research wave, 78 official Claude Code doc pages, published 2026-04-20 (L3-6). Every non-obvious claim is a verbatim blockquote with source URL; where docs are silent, it says so explicitly (L18-19,46).

Audience: "agent authors who require a self-contained reference" (L14).

Out of scope: Claude Agent SDK, any specific plugin/marketplace, non-CLI/IDE product surfaces (L15).

Sections:
- §1 Frontmatter & file format — L50-277
- §2 Discovery & loading — L280-423
- §3 Description-trigger semantics — L426-531
- §4 Tool restriction contract — L534-806
- §5 Model selection — L809-1012
- §6 Invocation lifecycle — L1015-1117
- §7 Context isolation — L1120-1202
- §8 Output routing — L1205-1378
- §9 Permissions, sandbox, IAM — L1381-1692
- §10 Subagent hook events — L1695-1947
- §11 Plugin packaging for agents — L1950-2152
- Appendix A, footguns (critical→minor) — L2155-2632
- Appendix B, documented silences — L2635-2753
- Appendix C, citation index — L2756-2799

## 2. Rules for writing an agent definition

**File form.** Markdown + YAML frontmatter (`---`-delimited); body = system prompt (L60,62). Only `name` and `description` required (L94,115).

**Frontmatter fields, allowed values, defaults:**

| Field | Allowed values | Default | Line |
|---|---|---|---|
| `name` | lowercase letters + hyphens | none | L98,119 |
| `description` | free text: when Claude should delegate | none | L99,123 |
| `tools` | comma-separated tool names; `Agent`/`Agent(type,...)` | inherit all | L100 |
| `disallowedTools` | comma-separated tool names | none denied | L101 |
| `model` | `sonnet`\|`opus`\|`haiku`\|full ID (e.g. `claude-opus-4-7`)\|`inherit` | `inherit` | L102,821 |
| `permissionMode` | `default`\|`acceptEdits`\|`auto`\|`dontAsk`\|`bypassPermissions`\|`plan` | inherit parent | L103 |
| `maxTurns` | positive integer | undocumented | L104 |
| `skills` | list of skill names | none | L105 |
| `mcpServers` | list: server-name string or inline def | none | L106 |
| `hooks` | object, hook-event keys → arrays | none | L107 |
| `memory` | `user`\|`project`\|`local` | none | L108,199-205 |
| `background` | boolean | `false` | L109,213 |
| `effort` | `low`\|`medium`\|`high`\|`xhigh`\|`max` | inherit session | L110,217 |
| `isolation` | `worktree` only | none | L111,221,225 |
| `color` | `red,blue,green,yellow,purple,orange,pink,cyan` | none | L112,229 |
| `initialPrompt` | free text; commands/skills processed | none | L113,233 |

**Plugin-shipped agents support only a subset**: `name, description, model, effort, maxTurns, tools, disallowedTools, skills, memory, background, isolation` (L90,332,2004). `hooks`, `mcpServers`, `permissionMode` are silently ignored when loaded from a plugin (L86-88,2002).

**Body.** Markdown after frontmatter = system prompt; subagent receives only this plus basic env (cwd) — NOT the full Claude Code system prompt (L239-241).

**Loading.** Agents load at session start; a manually-added file needs a session restart or `/agents` to load immediately (L245-247); `/reload-plugins` also picks it up without restart (L362-367).

**Tools — rules:**
- Omit `tools` → inherit ALL tools from parent, including MCP (L131,549,704).
- Set `tools` → exclusive allowlist (L131,553).
- Set `disallowedTools` alone → inherit everything except listed (L555-557).
- Both set → `disallowedTools` applied first, `tools` resolved against remainder; a tool in both is removed (L147,561).
- `Agent(type,...)` in `tools` restricts which subagent types may be spawned — only takes effect when the agent runs as main thread via `claude --agent` (L131,135,137,653).
- Bare `Agent` (no parens) = unrestricted spawn; omitting `Agent` entirely = no spawn allowed (L131,659,663).
- Subagents can never spawn subagents; `Agent(type)` in a subagent's own `tools` has no effect (L137,267-268,1081-1085).
- `EnterWorktree`/`ExitWorktree` never available to subagents regardless of `tools` (L579,581,706).
- Enabling any `memory:` scope unconditionally re-enables Read/Write/Edit, even over an explicit `disallowedTools` exclusion (L207-209,258).

**Model choice — rules:**
- Accepted frontmatter values: `sonnet`, `opus`, `haiku`, a full model ID, or `inherit`; omitted defaults to `inherit` (L821,826,923).
- `inherit` = the main conversation's model, nothing else (L830-836).
- Per-invocation resolution ladder, in order: (1) `CLAUDE_CODE_SUBAGENT_MODEL` env var, (2) per-invocation `model` param Claude passes, (3) frontmatter `model`, (4) main conversation's model (L840-845,958-963).
- `ANTHROPIC_DEFAULT_OPUS_MODEL`/`_SONNET_MODEL`/`_HAIKU_MODEL` reshape what an alias resolves to — orthogonal to, not part of, the ladder (L868-874,965-967).
- Built-in subagent defaults: Explore = Haiku; Plan and general-purpose = inherit; statusline-setup = Sonnet; Claude Code Guide = Haiku (L935-941).

**Description wording / triggering — rules:**
- `description` is the sole frontmatter field that governs auto-delegation (L442,444).
- Dispatcher reads exactly three inputs: the user's request text, the `description` field, current context (L448-452).
- Write "use proactively" (or "Proactively") in `description` to encourage more frequent auto-delegation (L472); shown in 3 of 4 official examples (L476-481).
- Escalating explicit-invocation methods: natural language (weakest — "Claude decides whether to delegate", L487-491) → `@-mention` (guarantees the named subagent runs for one task, but Claude still writes its task prompt — the mention does not control what prompt it receives, L493-499) → `--agent <name>`/`agent` setting (replaces the entire main-session system prompt; not a routing decision, L501-507).
- `description`-based routing does not apply when a subagent definition is reused as an agent-team teammate: only `tools` and `model` carry over, and the body is appended as additional instructions rather than replacing anything (L527-529).

## 3. Multi-turn human interaction, drift prevention, prompt eval

**Resuming a subagent across turns** (closest analog to "talks with a human over many turns"): Claude resumes a completed subagent via the `SendMessage` tool, `to` = the subagent's agent ID (L1105-1107,1350). Gated behind `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` — absent that flag, the agent ID the orchestrator receives is otherwise unusable (L1107,2554-2558, MD-24). A stopped subagent that receives a `SendMessage` auto-resumes in the background without a new Agent invocation (L1352). Resumed subagents "retain their full conversation history, including all previous tool calls, results, and reasoning... picks up exactly where it stopped rather than starting fresh" (L1354,2559).

Background subagents cannot ask the human anything: `AskUserQuestion` calls fail (the tool call fails, not the subagent) but the subagent continues with degraded output (L1076-1077,2380-2384).

**Instruction drift**: the document has no section named for this. The one directly relevant mechanism is that a stated conversational boundary ("don't push to production") is not a rule — the auto-mode classifier re-reads it from the transcript on each check, so it is silently lost once context compaction removes the message that stated it; "for a hard guarantee, add a deny rule instead" (L2368-2372, SV-30). Separately, `SubagentStop` loop control (`stop_hook_active`) prevents a stop-blocking hook from re-firing forever, but this guards hook loops, not instruction drift (L2176-2182,1889-1895, CR-2).

**Prompt evaluation / testing**: no dedicated section or terminology. Adjacent tooling only: `/reload-plugins` reloads plugins/skills/agents/hooks without restart for local iteration (L362-367); `--plugin-dir` loads a local plugin copy for a session, taking precedence over an installed marketplace copy of the same name for testing (L398-404,2144); `claude agents` CLI command lists all agents grouped by source and flags which are overridden (L374-376). No prompt-grading, eval-harness, or A/B-testing guidance is given anywhere in this manual.

## 4. Contradictions and version-specific details

**Version gates**, verbatim-sourced:
- v2.1.63 — `Task` tool renamed `Agent`; `Task(...)` still works as an alias (L139,271,1025,2612).
- v2.1.83+ — required for `auto` permission mode (L1499).
- v2.1.110+ — required for plugin dependency version constraints (L2121).
- 2026-04-19 — Claude Haiku 3 (`claude-3-haiku-20240307`) retires; frontmatter pins get no auto-migration (L906,2518-2522).
- 2026-06-15 — Claude Sonnet 4 / Opus 4 (the `-20250514` builds) retire (L902-904).
- 2026-04-23 — Enterprise pay-as-you-go / API default model switches to Opus 4.7 (L931).

**Marked contradictions:**
- CLAUDE.md loading inside an Agent-tool subagent: the CLI-facing `sub-agents.md` source implies only the definition body + env details arrive; the SDK-facing `agent-sdk-agent-loop.md` source states CLAUDE.md does load. Not resolved between the two (L2530-2532,2698, MD-19).
- Same model alias, different actual model by provider: on the Anthropic API `opus`→Opus 4.7, `sonnet`→Sonnet 4.6; on Bedrock/Vertex/Foundry `opus`→Opus 4.6, `sonnet`→Sonnet 4.5 — Opus 4.6 additionally lacks the `xhigh` effort level available on 4.7 (L992,2392-2396, SV-34).
- "Use proactively" is presented as the trigger-shaping mechanism (L472) yet the manual states no threshold, frequency, or firing condition is ever defined for it — the phrase's effect is asserted, not specified (L481,511-513,2454-2458, MD-6).
- Model-resolution ladder ambiguity: `ANTHROPIC_MODEL` sits above the settings `model` field in the Phase-A (main-conversation) ladder, but whether it can override an explicit subagent frontmatter `model:` value (Phase B) is never stated (L2490-2492, MD-12).

3-sentence summary: This manual specifies the full frontmatter contract for Claude Code agent definitions (14 optional fields plus required `name`/`description`), the tool-inheritance and model-resolution ladders, and how `description` alone drives auto-delegation, with plugin-shipped agents losing `hooks`/`mcpServers`/`permissionMode` silently. It documents almost nothing on multi-turn human-facing subagents beyond a flag-gated `SendMessage` resume path, and nothing at all on instruction-drift prevention or prompt evaluation/testing as named practices. It flags real cross-provider and cross-doc contradictions (alias-to-model divergence, CLAUDE.md loading) plus several version-dated retirements an agent-definition writer must account for.
