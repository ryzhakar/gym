# Sources searched — learning-mode scout, 2026-09-29

Claude Code version: 2.1.284 (`claude --version`).

## 1. Installed Claude Code bundle

- `which claude` → aliased to `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude`. Resolved actual binary via `npm root -g`, `npm ls -g` → `@anthropic-ai/claude-code`, npm-global install at `/opt/homebrew/lib/node_modules/@anthropic-ai/.claude-code-2DTsDk1V/cli.js` (11,780,929 bytes, minified, effectively single-line).
- Searched `cli.js` for `Explanatory:{name` (grep, then python `str.find` for exact offset since grep `{n}` reps didn't slice cleanly on the huge line). **Hit.** Found the shared output-styles object literal (`o96`) containing both `Explanatory` and `Learning` built-in style definitions, name/description/prompt/keepCodingInstructions for each. Full text extracted.
- Resolved template interpolations inside the extracted prompts:
  - `${uDq}` — the shared "## Insights" block, defined immediately before `o96` in the same module. **Hit**, verbatim text captured.
  - `${r6.bullet}` / `${r6.star}` — traced `r6` to a module-scoped symbol table (vendored `figures`-style Unicode symbol map) at offset ~3,130,810 / confirmed `star:"★"` at ~3,135,300 and `bullet:"●"` in the same table. **Hit.**
- Searched for `"Learning"` as a literal (grep `-o`) — matched but grep's fixed-width windowing missed it in one pass (needed the python offset approach above instead); no separate miss, same object covers it.
- Searched `TODO(human)` (6 occurrences) — confirmed all originate from the `Learning` style's example-request text, no other unrelated usage.
- **Output**: `learning-output-style.md`, `explanatory-output-style.md`.

## 2. Plugin caches

- `/Users/ryzhakar/.claude/plugins/` and `/Users/ryzhakar/.claude-competera/plugins/` — same directory tree in practice (identical listings; not investigated further whether one is a symlink/mirror of the other, out of scope).
- `grep -rli "explanatory|outputStyle|TODO(human)"` across both plugin caches — **miss** (no plugin-local files matched; those markers only exist inside the npm cli.js bundle, already covered above).
- `installed_plugins.json` grep for learn/explanat — **miss** (no such plugin currently installed in this profile).
- `plugin-catalog-cache.json` (526 KB, full marketplace catalog snapshot) searched via python JSON walk + regex for "learning" — **hit**: found catalog entries for `learning-output-style@claude-plugins-official` (description: "Interactive learning mode that requests meaningful code contributions at decision points (mimics the unshipped Learning output style)") and a reference to `explanatory-output-style` (category "learning", source `./plugins/explanatory-output-style`, same marketplace/repo).
- The `claude-plugins-official` marketplace is cloned locally under `/Users/ryzhakar/.claude/plugins/marketplaces/claude-plugins-official/`. `find .../plugins/learning-output-style` — **hit**: full plugin present (`plugin.json`, `README.md`, `hooks/hooks.json`, `hooks-handlers/session-start.sh`). All read and reproduced verbatim in `plugin-learning-output-style.md`, including unescaping the `\n`-escaped JSON string in the hook script (marked as such).
- `find .../plugins/explanatory-output-style` — **miss**. The catalog references this plugin but its directory was never cloned into this local marketplace checkout (only `learning-output-style/` exists on disk). Not recovered from cache; would need step 3 (GitHub fetch) to get its hook script directly. Not attempted since the built-in `Explanatory` style text (step 1) already gives the underlying prompt, and the learning-output-style README states it "includes all of that functionality."

## 3. Public docs / GitHub

Not attempted — steps 1 and 2 both succeeded (built-in styles found in the installed bundle; the learning-output-style plugin found fully cloned in the local marketplace cache). Per task scope, step 3 was a fallback only.

## Gaps

- The standalone `explanatory-output-style` plugin's own hook script (as opposed to the built-in `Explanatory` output style, which is captured) was not directly recovered — its directory isn't present in the local marketplace clone. If the exact plugin-hook wording (as distinct from the built-in style prompt) is needed, that requires fetching `github.com/anthropics/claude-code/tree/main/plugins/explanatory-output-style` (per the learning-output-style README's own link) or `anthropics/claude-plugins-public`.
- Did not verify whether `/Users/ryzhakar/.claude/plugins/` and `/Users/ryzhakar/.claude-competera/plugins/` are genuinely separate installs or share underlying storage — irrelevant to the task, not chased further.
