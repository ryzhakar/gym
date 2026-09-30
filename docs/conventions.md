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
do      `uv run python scripts/check_records.py`; commit only on 0 FAIL
never   a commit over a FAIL; a format rule trusted to reading alone
why     the schema's formats, grounds and pointers are checked by a program, not by attention
ground  owner ruling 2026-09-26 (competera's scripts port as a deterministic value-add)

### event-lines
when    writing an event line or closing a span
do      `uv run python scripts/event.py <actor> <kind> <what>`; `uv run python scripts/close_span.py --state … --open … --next …`
never   a hand-typed timestamp or close block
why     the clock and git stamp them, and a malformed line is refused at write time
ground  owner ruling 2026-09-26 (competera's scripts port as a deterministic value-add)

### memento-by-orchestrator
when    memento work: pat-down, events, span closes, record edits
do      the orchestrator reads and writes the records itself, through scripts/event.py, scripts/close_span.py and direct edits
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
