# t3 arguments — instructions

Read RECON/prompts/common.md first; it binds you. Directive variant: Tier 3 — read only the Sources the Question's Claims cite; never search for another.

Your prompt names one chunk file under RECON/args/chunks/, one Question id per line. Do the work yourself; spawn no subagents. Write output after every 8 Questions so a crash loses little.

Per Question:
1. Read MAP/questions/<id>.yaml, every MAP/positions/<id>--*.yaml, and every MAP/claims/*.yaml whose position is one of them (grep). Skip Claims whose `gap` contains `voice-below-bar`; read the rest.
2. For each cited Source, read it from the cache: `uv run python /Users/ryzhakar/pp/gym/scripts/research/cache.py get <url>` (url from MAP/sources/<source>.yaml).
3. For each Position, write the Arguments the Sources give for it and against it. An Argument is a reason a Voice offers, written in its advocates' terms, never in yours, and never an Argument no Source states. Each Argument names the Values it appeals to, from MAP/values/ (correctness, simplicity, iteration speed, performance, stability, approachability). When none fits, write `value-candidate: <name>` and flag the Argument; never force one of the six.
4. Each Argument lists the Source ids it comes from and one locator.
5. A Position whose Sources give no Argument gets a line saying `no argument in sources`.

Output: RECON/args/arguments-<chunk>.md, one section per Question:
```
## <question id>
### <position id>
- for | <text> | values: <v1>, <v2> | sources: <id>@<locator>
- against | <text> | values: ... | sources: ...
```

Scope: write only your output file. Never edit MAP/. No web access beyond cache.py (a cache miss is logged as `source unreachable: <id>`).

Tools: Read, Grep, Glob, Bash (cache.py), Write.

End with a 3-sentence summary: Questions done, Arguments written, Positions with none, value candidates.
