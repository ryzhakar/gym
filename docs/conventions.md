# Conventions

## Commit

### commit-as-you-go
when    a unit of work is finished
do      commit it at once, after `record-check` passes
never   a finished unit left uncommitted; a push without the owner's word
why     records count as durable only once committed
ground  owner ruling 2026-09-26

### commit-message
when    committing
do      one line, conventional: `type(scope): subject`
never   a second line: no body, no trailer, no attribution or co-author line
ground  owner ruling 2026-09-26

### atomic-commits
when    committing anything but memento changes
do      one logical change per commit
never   unrelated changes bundled into one commit
ground  owner ruling 2026-09-26
except  memento changes follow `memento-commits`

### memento-commits
when    committing memento changes: records, the schema, the map, memento's scripts
do      one large-grain commit per batch, `chore(memento): <kind of update>`, e.g. setup, events, ruling, close
never   a description in place of the kind; memento changes split into atomic commits
why     memento is the one exception to atomicity
ground  owner ruling 2026-09-26

## Records

### record-check
when    before committing a change that touches a record
do      `uv run gym records check`; commit only on 0 FAIL
never   a commit over a FAIL; a format rule trusted to reading alone
why     the schema's formats, grounds and pointers are checked by a program, not by attention
ground  owner ruling 2026-09-26 (competera's scripts port as a deterministic value-add); owner ruling 2026-09-30 (one typer app)

### event-lines
when    writing an event line or closing a span
do      `uv run gym records event <actor> <kind> <what>`; `uv run gym records close --state … --open … --next …`
never   a hand-typed timestamp or close block
why     the clock and git stamp them, and a malformed line is refused at write time
ground  owner ruling 2026-09-26 (competera's scripts port as a deterministic value-add); owner ruling 2026-09-30 (one typer app)

### memento-by-orchestrator
when    memento work: pat-down, events, span closes, record edits
do      the orchestrator reads and writes the records itself, through `gym records event`, `gym records close` and direct edits
never   a record read or write delegated to an agent; a second carve-out from agentic-delegation's file prohibition
why     "memento is the sole exception: orchestrator keeps their records themselves"
ground  owner ruling 2026-09-30

## Code

### python-via-uv
when    writing anything for gym's administration: building, a one-off run, a script kept for consistent reuse
do      Python, managed and launched with `uv`
never   a script in another language; Python run outside uv
why     "everything uses python and get's managed and launched via `uv`"
ground  owner ruling 2026-09-26
except  Rust Arthur writes in training is his own work, not administration

## Owner

### questions-in-the-tool
when    asking the owner anything
do      put everything the owner needs to see inside the question tool call itself: context, quotes, options, trade-offs, previews, written for a reader with no other or prior knowledge
never   a wall of conversation text; a question that leans on an earlier message
why     the owner does not read conversation text: "i won't read your walls of text here, ever."
ground  owner ruling 2026-09-26

## Training

### session-records
when    a training session runs
do      the manager opens `training/<subject>/sessions/<id>/` with `gym train open` before the summons and closes it with `gym train close` after the trainer returns; the trainer logs every turn with `gym train log`; feedback and instruction lines carry their substance in `note=`
never   a session on shared tables; a turn logged nowhere; feedback that survives only in a transcript
why     "surely a training session should have its own record and events"; the learning moments of the first session lived only in the trainer's transcript
ground  owner ruling 2026-09-30

### session-ids
when    naming a session or any path derived from it
do      `YYYY-MM-DDTHH-MM`, hyphens only
never   a colon in a path
why     a colon in a path breaks cargo on macOS, the DYLD_FALLBACK_LIBRARY_PATH separator
ground  history/2026-09-30/events.md, 16:28

### direct-sessions
when    the learner trains
do      the learner converses with the trainer in the trainer's own session; the manager summons it with a summons file under recon and does its own work meanwhile
never   the manager relaying turns between learner and trainer
why     "the goal is not for you to relay shit to me, but for me to train with them in their subagent session"
ground  owner ruling 2026-09-30

### trainer-summons
when    the manager summons the trainer
do      a prompt file carrying subject, workspace, items directory, session id, the status output and the opening item; the trainer holds every tool and may summon agents of its own; the key/ ban stays a rule in its definition
never   a summons that exists only in conversation; a tool restriction standing in for the key/ rule
ground  owner ruling 2026-09-30

### probes-by-trainer
when    a probe runs
do      the trainer stages and grades it from its own shell with `gym train probe stage` and `gym train probe grade` on the learner's "go" and "done"; the learner runs no command
never   the learner doing administration; the trainer opening key/
why     "you exist so i can focus on the learning, not administration"
ground  owner ruling 2026-09-30, in session, confirmed in the question tool

### session-narrative
when    a session ends
do      the trainer writes the session's narrative, per item what the learner did, the fault or pass, the feedback, the principle, misconceptions and tool quirks, into the session record before its close block
never   a trainer instance released before its narrative is written
why     the first session's feedback was recoverable only because the instance was still resumable
ground  owner ruling 2026-09-30

## Communication

### silence-holds
when    silence is on (marker `.claude/work-silently` present)
do      a turn ends on its last useful tool call or on nothing; the owner's typed words alone get an answer
never   a status line; a no-op call or a check made to fill a turn; text on a harness prompt, a reminder or an agent notification
why     "no fucking status lines. never ever."; "nothing warrants visible output"; "even less nonsensical tool calls"
ground  owner ruling 2026-09-30

### token-thrift
when    writing anything an agent or the owner reads
do      the fewest tokens that carry the instruction; prompts state inputs, task, output, scope
never   yapping in agent-facing text; a restated context; a preamble
why     "as little token spend on your part as possible. no yapping in agent-facing communication. clarity ≠ verbosity."; "maximum achievement per token."
ground  owner ruling 2026-09-30

