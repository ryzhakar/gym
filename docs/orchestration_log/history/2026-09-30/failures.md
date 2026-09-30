# 2026-09-30

## Silence broken by status lines

What happened: after the owner called work-silently at 16:09, the orchestrator ended most turns with a one-line status ("Nothing to request…", "Trainer-learner exchange; nothing for the manager") until the owner wrote at 17:00: "you were instructed to work in silence."

Mechanism: harness prompts ("Your previous response had no visible output. Please continue and produce a user-visible response") and the reflex to close a turn with a recap were treated as reasons to write; the skill names both as outside events that never lift silence, and the constitution's own rule against process narration forbade the lines even outside silence.

Correction: a turn in silence ends on its last tool call with zero characters; an outside event asking for text gets none; the only text the owner sees is an answer to a message the owner typed.

## No-op checks made to fill turns

What happened: between 17:21 and 17:24 the orchestrator answered a run of harness prompts ("Your previous response had no visible output. Please continue") with git status, git log, lint and cron listings whose answers could not have changed, about ten of them.

Mechanism: the harness prompt was treated as a demand for a tool call; the skill names it an outside event, and forbids a call made to fill a turn or a check whose answer cannot have changed.

Correction: a turn with nothing to advance ends empty, no text and no call; the next real trigger is a notification, the heartbeat, or the owner.

## A shell variable holding a command broke a chain

What happened: at 19:18 a Bash call set `E="uv run gym records event"` and called `$E …` six times in an `&&` chain; zsh does not word-split an unquoted variable, so the first call failed with "command not found", the chain stopped before the per-item minutes commit and the narrative merge, and the commands after the heredoc ran anyway: the CSV tables and the old scripts were deleted in a commit that omitted the code they depended on being replaced by.

Mechanism: an alias-by-variable under zsh, and a heredoc splitting one chain into two.

Correction: full commands, never a variable holding one; one chain per Bash call, and a heredoc ends the call; the missed steps were redone at once and the events written.
