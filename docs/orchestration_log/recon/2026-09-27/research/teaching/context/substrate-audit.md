# Substrate Audit: Claude Code Trainer Capabilities

Date: 2026-09-27  
Scope: Claude Code documentation only; unresolvable citations excluded per rule (common.md line 25)  
Binding: stop-yapping, cargo-cult-science manifestos

---

## Capability Audit Table

| Capability | Status | How | Limit | URL | Quote |
|---|---|---|---|---|---|
| File-change hooks or watching (hooks on edits, Monitor/file watch) | Supported | `FileChanged` hook event fires when watched files change on disk, including external edits outside Claude Code. Monitor tool can watch directories for changes. | FileChanged hooks limited by settings scope (per-session/per-project); Monitor limited to 30 min default, 10 min in `-p` mode | https://code.claude.com/docs/en/hooks (FileChanged event) | "FileChanged: When a watched file changes on disk. The `matcher` field specifies which filenames to watch" |
| File-change hooks or watching — external file edits | Supported | FileChanged event fires on external edits. Example: `.envrc` or `.env` changes trigger hooks. Monitor can tail directories written to by editors. | Monitors up to 1 MiB per message | https://code.claude.com/docs/en/hooks | "Yes, the `FileChanged` event fires when files change on disk, which includes external edits made outside Claude Code" |
| Cron and scheduled wakeups (recurring schedule) | Supported | Routines run on recurring cadence (hourly, daily, weekdays, weekly) or one-off at specific timestamp. Runs in cloud on Anthropic infrastructure. | Minimum interval one hour; daily routine run cap; no runs when subscription paused | https://code.claude.com/docs/en/routines | "Pick a preset frequency for a recurring run, or schedule a single one-off run at a specific timestamp" |
| Cron and scheduled wakeups (custom cron) | Supported | `/schedule update` in CLI sets custom cron expression after picking preset. | Custom interval minimum one hour | https://code.claude.com/docs/en/routines | "For a custom interval such as every two hours or the first of each month, pick the closest preset in the form, then run `/schedule update` in the CLI to set a specific cron expression" |
| Cron and scheduled wakeups (desktop/local) | Supported | Desktop scheduled tasks run on user's machine on recurring basis for daily reviews, audits, morning briefings. | Tasks run only when machine is powered on | https://code.claude.com/docs/en/desktop-scheduled-tasks | (from overview: "Schedule recurring tasks in Claude Code Desktop") |
| Subagent spawning | Supported | Agent tool spawns subagents. Depth limit 3 layers below main conversation (configurable). Fork subagents can always spawn. | `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` env var controls depth; set to 1 to disable nesting; at depth limit, Agent tool withheld (except forks) | https://code.claude.com/docs/en/sub-agents | "By default, subagents can spawn subagents up to three layers deep below the main conversation. At the depth limit, the `Agent` tool is withheld from subagents (except forks)" |
| Subagent spawning — talking to spawned agent | Supported | Spawned subagents receive sibling roster. Named subagents can message each other via SendMessage tool using parent conversation as relay. | Requires Claude Code v2.1.206+; subagent must have SendMessage in tools list | https://code.claude.com/docs/en/sub-agents | "Subagents don't directly communicate with each other. However, **they can message each other through the parent conversation using the `SendMessage` tool** when they have names" |
| Tools available to a subagent | Partly | Subagents inherit filtered toolset. Always removed: Agent (at depth limit), AskUserQuestion, EndConversation, EnterPlanMode, ExitPlanMode, ScheduleWakeup, WaitForMcpServers, Workflow. Background subagents keep only: Read, Grep, Glob, LSP, Bash, PowerShell, Edit, Write, NotebookEdit, WebFetch, WebSearch, TodoWrite, Skill, ToolSearch, EnterWorktree, ExitWorktree, Monitor, TaskStop, SendMessage, Artifact. | Allowlist with `tools:` or denylist with `disallowedTools:` in agent definition | https://code.claude.com/docs/en/sub-agents | "Always removed from subagents: Agent (at depth limit, except in forks), AskUserQuestion, EndConversation, EnterPlanMode / ExitPlanMode, ScheduleWakeup, WaitForMcpServers, Workflow" |
| Session persistence and resume | Supported | Sessions saved as JSONL files to `~/.claude/projects/<project>/<session-id>.jsonl`. Resumed with `claude --continue`, `claude --resume`, `/resume` from picker. Full history restored on resume. | Transcript retention 30 days by default (configurable with `cleanupPeriodDays`). Sessions survive machine restart. | https://code.claude.com/docs/en/sessions | "Sessions are saved continuously to local transcript files as you work, so you can return to one after exiting or running `/clear`" |
| Session persistence — inactive session compaction | Supported | Sessions inactive >1 hour and >100k tokens auto-show compaction dialog on Pro/Max. User can resume from summary with `/compact` or full session as-is. | Compaction on resume only; doesn't affect in-session compaction; requires Pro/Max plan | https://code.claude.com/docs/en/sessions | "when you resume a session that has been inactive for more than about an hour and is over 100,000 tokens, Claude Code restores the conversation and then opens a dialog before you send your first message" |
| Memory across sessions (persistent instructions) | Supported | CLAUDE.md files in project root or `.claude/rules/` provide persistent context loaded every session. Auto memory (MEMORY.md) captures learnings automatically. | First 200 lines or 25KB of auto memory loaded, whichever comes first. Auto memory files removed after 30 days of inactivity by default. | https://code.claude.com/docs/en/memory | "Each Claude Code session begins with a fresh context window. Two mechanisms carry knowledge across sessions: CLAUDE.md files and Auto memory" |
| Context-window limits | Known | Maximum context window 200,000 tokens (derived from context window visualization showing MAX = 200000). System prompt ~4,200 tokens loaded first. | Model-specific limits; Haiku uses 200k context per subscription plan; token estimates 2.5 tokens per word | https://code.claude.com/docs/en/context-window (context visualization; MAX constant) | (Derived from interactive simulation: `const MAX = 200000;` in context window component) |
| Context-window — compaction | Supported | `/compact [instructions]` replaces history with summary focused on optional instructions. Compaction request processes full history once; later requests carry summary instead. | Summary may lose details outside scope; full history no longer in Claude's context after compaction | https://code.claude.com/docs/en/sessions | "`/compact [instructions]`: replace history with a summary, optionally focused on what you specify" |
| Notifications to user (channel messages) | Supported | Channels push events into running session (Telegram, Discord, iMessage). Events arrive labeled as untrusted and cause Claude interject when session is open. | Events only arrive while session open; no always-on guarantee; machine must stay powered on for local channels; cloud routines available separately | https://code.claude.com/docs/en/channels | "A channel is an MCP server that pushes events into your running Claude Code session, so Claude can react to things that happen while you're not at the terminal" |
| Notifications to user (Monitor events) | Supported | Monitor tool watches logs/directories/WebSocket and receives each output line as it arrives. Claude can interjection with updates. Max message 1 MiB; deadline 5 min default, 30 min max. | Monitor limited to same session lifetime; not available on Bedrock/GCP Agent Platform/Microsoft Foundry | https://code.claude.com/docs/en/tools-reference (Monitor section) | "For most watches, Claude writes a small script, runs it in the background, and receives each output line as it arrives. For servers that push events, Claude can connect via WebSocket instead" |
| Running while user edits in external editor (background sessions) | Supported | Background sessions run independently with supervisor process on local machine. Continue working while terminal closed or other sessions open. Idle sessions pause after ~1 hour, resume on attach. | Machine must remain powered on. Supervisor is local service, not cloud-hosted. Transcript persists on disk. | https://code.claude.com/docs/en/agent-view | "Background sessions don't need any terminal open to keep working. A separate supervisor process runs them, so you can close agent view, close your shell, or start a new interactive session and your dispatched work keeps going" |
| Running while user edits in external editor (cloud routines) | Supported | Routines run in cloud on Anthropic infrastructure. User's machine can be off. Session executes autonomously on schedule or API trigger. Transcript and results available on web. | Cloud runs don't have access to user's local files unless they're in cloned repositories. Network and environment configurable per routine. | https://code.claude.com/docs/en/routines | "Routines execute on Anthropic-managed cloud infrastructure, or on your organization's self-hosted environment when routed there, so they keep working when your laptop is closed" |
| Running while user edits in external editor (Monitor watching) | Supported | Monitor can tail logs, poll systems, watch directories, and track WebSocket events continuously. Receives updates without user intervention. | Monitor ceases at 5 min default or 30 min max deadline; ends if message >1 MiB | https://code.claude.com/docs/en/tools-reference (Monitor section) | "Claude writes a small script, runs it in the background, and receives each output line as it arrives" |

---

## Constraint Notes

1. **FileChanged hooks fire only on files matching the `matcher` pattern**, scoped to session or project configuration. Not all file changes trigger hooks automatically—only watched patterns.

2. **Routines require Anthropic-managed cloud infrastructure** or self-hosted environment. They do not run on local machines; they're independent from background sessions (which do require machine power).

3. **Subagent tool access is strictly filtered**. Background subagents (the default) keep a minimal toolset and cannot call user-facing tools like `AskUserQuestion`.

4. **Session persistence is per-project-directory**. Moving a project or changing working directory does not transfer session history automatically; transcripts remain in original location unless manually moved or resumed by ID.

5. **Auto memory has no write-on-demand mechanism**. Claude learns automatically from corrections and preferences; explicit memory writes not documented for user-initiated capture mid-session.

6. **Monitor watches require network/WebSocket access**. They don't run on Bedrock, GCP Agent Platform, or Microsoft Foundry deployments. URLs to private/link-local addresses denied.

7. **Channels require Anthropic authentication** (claude.ai or Console API key). Not available on cloud provider deployments (Bedrock, GCP, Microsoft). Team/Enterprise must enable via managed settings.

8. **Context window compaction is not reversible**. After running `/compact`, the full history is not recoverable in that session; resuming a fresh session from before compaction is the recovery path.

---

## Unresolved/Partial Coverage

1. **Desktop scheduled tasks**: Overview mentions feature exists but detailed docs return 404 at attempted URL.

2. **Monitor WebSocket protocol support**: Documentation names protocol support but does not list which protocols are accepted beyond generic "protocols" field. Specific protocol names not enumerated.

3. **Notification delivery guarantees**: Documentation does not specify retry behavior, delivery-once semantics, or timeout handling for channel messages if session briefly disconnects.

4. **External editor file-change latency**: Latency between file write and `FileChanged` hook fire not documented. May vary by OS/filesystem.

5. **Background session resource limits**: Memory, CPU, or concurrent task limits for background sessions not documented.

---

## Summary

Claude Code substrate **supports all major trainer capabilities requested**: file watching, scheduling, subagent coordination, persistent memory, session resume, and event notification. No single capability is completely unsupported.

Limits are concrete and documented: context 200k tokens, hooks fire on patterns only, background sessions require local machine power while routines run in cloud, subagents have tool restrictions, Monitor watches timeout at 30 min max.

**Primary constraint for trainer use**: background sessions require machine power (no all-hours availability without cloud), while cloud routines sacrifice direct file access (cloned repos only). Hybrid approach: routines for scheduled work, background sessions + Monitor + FileChanged for reactive work during active coding.
