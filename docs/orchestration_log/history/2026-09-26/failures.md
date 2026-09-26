# 2026-09-26 — failures

## Questions framed on keeping files the owner wanted dissolved

What happened: the first question round asked whether doc/TASK.md and doc/SPEC.md each still held, were out of date, or should stop counting, which presumed both would stay whole. The owner rejected it: "both these tasks are for you to dissolve".

Mechanism: memento:setup's file-ruling procedure was applied as written — every collected file kept whole and ruled on as a unit — without first checking whether the owner wanted the notes kept as files at all.

Correction: both notes were dissolved into their homes and archived whole; the rounds after it asked about content, not about files.

## Question context put in conversation text

What happened: the second question round carried its context — where each part of the notes would go, the draft goals, the plan of rounds — in conversation text above the question tool, and its questions leaned on that text. The owner rejected it: "i won't read your walls of text here, ever."

Mechanism: conversation text was assumed read before the questions were answered.

Correction: docs/conventions.md rule `questions-in-the-tool`; every later question carried its own context, quotes and previews.

## A list offered as a pitch

What happened: asked to present the setup, the first answer was five bullets followed by a ratification question. The owner: "this does not count as presenting or pitching."

Mechanism: "the least amount of words possible" was read as the fewest items rather than the densest presentation; the setup's shape — which file loads when, and what each holds — never appeared, and ratification was asked before anything was presented.

Correction: the setup was presented as one diagram of the files by load time, with the working loop beneath it.

## References read past need before the binding report

What happened: binding the you stack, the rule agentic-delegation defers to was found in memento's authority-check, and reading went on: a second grep over memento, the manifesto plugin's hooks.json and drift-reminder.sh, and a diff of the injected oath against its SKILL.md, written through a scratchpad file. The owner interrupted: "SORT YOURSELF OUT FIRST".

Mechanism: every reference was checked alike; none was classed cursory or indispensable before opening, though the owner's request asked for exactly that split. The scratchpad write broke agentic-delegation's file-touch ban.

Correction: reading stopped; the binding report classed every reference first. Commitment: class a reference before opening it; open only indispensable ones.

## A cd moved the harness working directory

What happened: a Bash call opened with `cd` into .claude/manifesto-repo/LLM_MANIFESTOS; later calls ran from the manifesto repo, not gym's root.

Mechanism: the harness keeps the working directory across Bash calls; a `cd` inside a compound command moves it for every call after.

Correction: working directory reset to /Users/ryzhakar/pp/gym; later calls use absolute paths, or `cd` to gym's root only.
