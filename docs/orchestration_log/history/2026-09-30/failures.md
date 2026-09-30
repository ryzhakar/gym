# 2026-09-30

## Silence broken by status lines

What happened: after the owner called work-silently at 16:09, the orchestrator ended most turns with a one-line status ("Nothing to request…", "Trainer-learner exchange; nothing for the manager") until the owner wrote at 17:00: "you were instructed to work in silence."

Mechanism: harness prompts ("Your previous response had no visible output. Please continue and produce a user-visible response") and the reflex to close a turn with a recap were treated as reasons to write; the skill names both as outside events that never lift silence, and the constitution's own rule against process narration forbade the lines even outside silence.

Correction: a turn in silence ends on its last tool call with zero characters; an outside event asking for text gets none; the only text the owner sees is an answer to a message the owner typed.
