# t3 voice verifier — instructions

Read RECON/prompts/common.md first; it binds you. Directive variant: search — search freely for track-record evidence; log every URL you rely on.

Your prompt names chunk files under RECON/verify/voice-chunks/, one Voice id per line. Work them in the order given; finish and write one chunk's output before starting the next.

Per Voice:
1. Read MAP/voices/<id>.yaml and every MAP/claims/*.yaml whose `voice` is that id (grep), and the Sources they cite: they tell you who the Voice is (handle, host, project). A handle alone is ambiguous: tie identity to the handle's own profile page (GitHub, forum, reddit user page) before crediting any record to it.
2. Check the bar in GYM/docs/subjects/rust.md § Scope (Voices), each kind:
   - crate-dependents: crates.io API `https://crates.io/api/v1/crates/<crate>/reverse_dependencies?per_page=1` → `meta.total`; owners via `/api/v1/users/<login>` and `/api/v1/crates?user_id=<id>`. Real dependents = ≥1.
   - production: employer post, talk or job page naming Rust in production.
   - role: Rust project or foundation team page (rust-lang.org/governance, GitHub rust-lang team repo via `gh api`).
   - book/course/talk/post: listing URL; a post counts when linked from This Week in Rust, or ≥100 Hacker News points, or ≥20 Lobsters comments.
3. Type, one of: builder, educator, language-designer, institution, critic, leaver. Choose from evidence, not name.
4. Influence lines per GYM/docs/subjects/rust.md § Influence evidence, each with url and date.
5. Verdict MEETS if ≥1 kind holds with evidence; FAILS if you checked every kind and none holds; UNKNOWN if identity cannot be tied or sources are unreachable. Never guess.

Output per chunk: RECON/verify/voices-<chunk>.md, one section per Voice:
```
## <id>
name: <display name as evidenced>
identity: <profile url tying handle to person or org> | untied
type: <enum> | unset
verdict: MEETS | FAILS | UNKNOWN
track_record:
- <kind>: <one line> — <url> (<date>)
influence:
- <one line> — <url> (<date>)
checked: <kinds checked with no evidence found>
```

Scope: write only your output files. Never edit MAP/. Never open RECON/team-a/, team-b/, merge*/, fill/, audit/.

Tools: Read, Grep, Glob, WebSearch, WebFetch, Bash (`curl -s` for crates.io with a User-Agent header `gym-research (arthur)`, `gh api`, `uv run python /Users/ryzhakar/pp/gym/scripts/research/cache.py get <url>`), Write.

After each chunk, notify in one line: chunk, MEETS / FAILS / UNKNOWN counts. End with a 3-sentence summary.
