# Claude Code Agent Frontmatter Fields — Current Bundle Reference
Date: 2026-09-29
Bundle: v2.1.284 (@anthropic-ai/.claude-code-2DTsDk1V)
Sources: Installed bundle analysis, official docs (code.claude.com/docs/en/sub-agents, code.claude.com/docs/en/plugins-reference), local research records (claude-skills recon 2026-04-17)

---

## Q1: Full List of Frontmatter Fields

**16 official fields**, verified from https://code.claude.com/docs/en/sub-agents "Supported frontmatter fields" table:

| Field | Type | Required | Valid values | Default |
|---|---|---|---|---|
| `name` | string | **Yes** | lowercase letters, hyphens | error if missing |
| `description` | string | **Yes** | when Claude should delegate to this agent | error if missing |
| `model` | string | No | `sonnet`, `opus`, `haiku`, full model ID (e.g. `claude-opus-4-7`), or `inherit` | `inherit` |
| `tools` | string/array | No | tool names (e.g. `Read, Write, Bash` or `["Read", "Write"]`); inherits all if omitted | inherits all parent tools |
| `disallowedTools` | string/array | No | tool names to deny | none |
| `maxTurns` | integer | No | max agentic turns before stop | unlimited |
| `effort` | string | No | `low`, `medium`, `high`, `xhigh`, `max` | inherits session effort |
| `skills` | array | No | skill names to inject (full content loaded, not inherited from parent) | none |
| `mcpServers` | array | No | MCP server names or inline definitions | none |
| `hooks` | object | No | lifecycle hooks scoped to agent | none |
| `memory` | string | No | `user`, `project`, or `local` | none (no persistence) |
| `background` | boolean | No | `true` to run as background task | `false` |
| `isolation` | string | No | `worktree` (only valid value); runs in temp git worktree | no isolation |
| `color` | string | No | `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan` | none |
| `initialPrompt` | string | No | auto-submitted as first turn when agent runs via `--agent` flag or agent setting | none |
| `permissionMode` | string | No | `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan` | `default` |

**Field that stops CLAUDE.md loading**: None. No frontmatter field explicitly blocks CLAUDE.md loading into an agent. However, context loading depends on invocation path (see Q2).

---

## Q2: Subagent CLAUDE.md Loading — Context-Dependent

**Short answer: Loading depends on how the agent is invoked; no single rule applies to all agents.**

### Path 1: Agent as main session (`claude --agent <name>`)
- **Project CLAUDE.md**: YES, loads via normal message flow
- **User CLAUDE.md**: Likely yes (implied by "normal message flow" but not explicitly named)
- Source: https://code.claude.com/docs/en/sub-agents — "CLAUDE.md files and project memory still load through the normal message flow."

### Path 2: Agent team teammate (experimental, `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
- **Project CLAUDE.md**: YES, confirmed
- **User CLAUDE.md**: Implied by "same project context as regular session" but unconfirmed
- Source: https://code.claude.com/docs/en/agent-teams — "A teammate loads the same project context as a regular session: CLAUDE.md, MCP servers, and skills."

### Path 3: Standard subagent invocation (Agent tool call)
- **Project CLAUDE.md**: UNCONFIRMED / possibly NO
- **User CLAUDE.md**: NO confirmation
- Source: https://code.claude.com/docs/en/sub-agents — "Subagents receive only this system prompt (plus basic environment details like working directory), not the full Claude Code system prompt."
- Gap: The phrase "only system prompt plus env details" suggests CLAUDE.md may not load, but docs do not confirm or deny it explicitly for this path.

**Key finding**: The system prompt field in the agent definition replaces the default Claude Code system prompt entirely. Whether project CLAUDE.md loads as additional context alongside this system prompt (paths 1 & 2) or does not load at all (path 3) depends on the invocation method.

**Does subagent replace or append to system prompt?** For path 1 & 2, CLAUDE.md loads "through the normal message flow" — treated as conversation context, not system prompt. For path 3, the agent's system prompt is stated to be the complete context minus env details. The agent body does not append to CLAUDE.md; rather, the two operate on separate tracks depending on invocation.

**Bundle evidence**: The cli.js minified bundle at `/opt/homebrew/lib/node_modules/@anthropic-ai/.claude-code-2DTsDk1V/cli.js` references `model`, `reasoning`, `tools`, `timeout`, `system` fields in grep results, but is not readable for invocation-specific CLAUDE.md handling logic. Official docs are the authoritative source here.

---

## Q3: Settings Keys Scoping CLAUDE.md Loading

**Official settings field identified**: `CLAUDE_CODE_DISABLE_CLAUDE_MDS`

| Setting | Type | Scope | Effect | Source |
|---|---|---|---|---|
| `CLAUDE_CODE_DISABLE_CLAUDE_MDS` | environment variable | global (affects main session and all subagents) | set to `1` to prevent loading any CLAUDE.md files | https://code.claude.com/docs/en/env-vars |

**No per-agent settings key found.** The official documentation does not list a settings.json key (e.g., `claudeMdExcludes`, `disableCLAUDEmd`, etc.) that scopes CLAUDE.md loading per agent in `.claude/agents/*.md` or project settings.json.

The disable flag is environment-variable only and applies globally — all sessions and all agents in that session respect it equally.

**Plugin agent restriction**: Plugin agents do not support `hooks`, `mcpServers`, or `permissionMode` frontmatter fields (those fields are ignored). No restriction on CLAUDE.md loading is documented for plugin agents.

**Note on isolation**: The `isolation: worktree` field creates an isolated git worktree, but this does not affect CLAUDE.md loading — it only affects filesystem and git state.

---

## Verification Against Installed Bundle

**Model version: v2.1.284**. Verified via `claude --version`.

Bundle path: `/opt/homebrew/lib/node_modules/@anthropic-ai/.claude-code-2DTsDk1V/cli.js`

The bundle is minified and does not expose source logic for field validation or invocation-path branching. Verification relied on:
1. Local research records from claude-skills recon 2026-04-17 (Tier 1 research: agent-frontmatter-spec.md, context-isolation-constraints.md, model-field-semantics.md)
2. Official docs at code.claude.com (primary source, current as of 2026-09-29)
3. Direct inspection of example agent files in the codebase

**Unconfirmed findings** noted above are NOT in the bundle documentation as of the docs version loaded in this research.

---

## Summary

Frontmatter has 16 official fields (name, description, model, tools, disallowedTools, maxTurns, effort, skills, mcpServers, hooks, memory, background, isolation, color, initialPrompt, permissionMode); no field blocks CLAUDE.md loading. Standard subagents (`Agent()` invocation) receive only their system prompt plus env details—CLAUDE.md loading unconfirmed for this path. Agents invoked as `--agent` or as agent-team members do load project CLAUDE.md. No per-agent settings key scopes CLAUDE.md; a global env var (`CLAUDE_CODE_DISABLE_CLAUDE_MDS`) disables it for all agents.

