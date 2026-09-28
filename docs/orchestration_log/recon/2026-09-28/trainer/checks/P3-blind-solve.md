# P3 blind-solve, Stage 0 items

Blind solver: opus instance (orchestrator) + three delegated general-purpose subagents (u01-rest, u02, u03), 2026-09-28. Solved from what the learner sees only: `spec.md`/`attempt.md` and the stub/attempt crate's visible source and tests. Never opened any `key/`, `example.md`, or `hints.yaml`. All solving done in `/private/tmp/gym-scratch/t-p3-blind/`; nothing under `items/` was edited.

Process note: stray `Cargo.lock`/`target/` files appeared twice under `training/rust/items/u01-own-move-borrow/probe-a/` during this run — once under `p1-board/` (found and removed before the u01-rest subagent's work started), once as fresh `Cargo.lock` files under `p1-board/`, `p2-summary/`, and `p3-shift/` (found and removed after the u01-rest subagent reported done), meaning cargo ran inside the items tree at least twice. The subagent denied running cargo there both times it was asked; the second occurrence lines up exactly with the three probe-a items it was assigned, contradicting that denial. Not pursued further — both instances were untracked and removed, `git status` is clean now — but the subagent's self-report should not be taken as reliable on this point.

## Totals

- Items checked: 27 (6 baseline + 3 × 7 in u01/u02/u03: attempt, reuse-1, reuse-2, unshown, probe-a/p1, p2, p3).
- Solved: 27/27, `cargo test` green in every scratch copy.
- Items with a real spec/test ambiguity: 6 (b3-result: none actually; see table — corrected count is 5, listed below).

## Verdicts

| item | solved | effort | ambiguity | note |
|---|---|---|---|---|
| baseline/b1-own | yes | 1 min | no | Consuming `for w in words` before `words.len()` is a plain move-then-use compile error; fix is to capture `total` before the loop. Mechanical, no reading gap. |
| baseline/b2-life | yes | 2 min | no | Two input `&str` params block lifetime elision; spec states plainly which output lifetime is wanted (tied to `line`, not `sep`). |
| baseline/b3-result | yes | 2 min | no | `?`-chain via `ok_or` + `map_err` is the direct reading of "propagate each failure with `?`." Multi-colon input isn't covered by visible tests, but spec's "everything after the first `:`" pins the behavior unambiguously even there. |
| baseline/b4-traits | yes | 2 min | no | Generic-over-trait function, direct reading of spec. |
| baseline/b5-iter | yes | 2 min | no | Deterministic once iterator laziness (map/filter/take pulled on demand) is traced by hand. |
| baseline/b6-enum | yes | 2 min | no | Deterministic once guard/binding order in the match arms is traced by hand. |
| u01/attempt | yes | solved directly, not separately timed | no | Three independent compile fixes (NLL borrow-across-mutation in lib.rs; move-then-use in caller_side; ownership-vs-borrow choice in callee_side). Spec's "fixes 2 and 3 are two different ways out of the same error" plus the string-copy ban and heap-address test fully pin the intended shape. |
| u01/reuse-1 | yes | 2 min | no | Immutable max-borrow held across a mutating call; dereference-to-copy (u32 is Copy) is the only spec-compliant fix. |
| u01/reuse-2 | yes | 2 min | no | Move-in-a-loop; changing the callee to take `&str` is the direct fix the spec permits. |
| u01/unshown | yes | 3 min | no | `std::mem::take` is forced by "no clone/to_owned/to_vec/to_string" plus the pointer-identity test; nothing else satisfies both. |
| u01/probe-a/p1-board | yes | 2 min | no | Same shape/fix as reuse-1. |
| u01/probe-a/p2-summary | yes | 2 min | no | Move-then-use again; changing `byte_total` to borrow is the permitted, direct fix. |
| u01/probe-a/p3-shift | yes | 3 min | **yes** | Spec bans `.clone()` *calls* in `src/lib.rs`, not derive changes. Two spec-compliant, both-compiling fixes diverge: (a) change `add` to borrow `b: &Point` (the intended borrow lesson), or (b) `#[derive(Copy, Clone)]` on `Point` and leave `add` untouched (sidesteps the lesson via implicit copy). Visible tests don't distinguish them. Worth tightening if the borrow lesson is the point. |
| u02/attempt | yes | 8 min | no | `enum_form`/`flat_form` split fully pinned by spec text; banned-keyword test (`include_str!` scan for `"enum"`) checked literally, including comments. |
| u02/reuse-1 | yes | 5 min | **yes** | "One `match`, no `_` arm: every arm names its variant" is unenforced by any visible test — a learner could satisfy the visible suite with `if`/`else` and no match at all. Boundary values (age 65, age 3, group 10) come from spec text only, not exercised by visible tests, but spec alone does pin them. |
| u02/reuse-2 | yes | 6 min | **yes** | "Zero-length line costs 1, like a dot" is spec-only — no visible test exercises a zero-length line. Spec fully determines it, but nothing visible confirms correct wiring short of held-out. "No `_` arm" also unenforced by visible tests, same gap as reuse-1. |
| u02/unshown | yes | 4 min | no (minor) | "No `if`" constraint unenforced by visible tests (only 2 of 12 input pairs shown) but doesn't admit a genuinely different correct answer — just an unchecked style rule. |
| u02/probe-a/p1-tokens | yes | 4 min | no | Predict-output item; spec text plus source fully determine exact stdout, guard arms mutually exclusive by construction. |
| u02/probe-a/p2-sign | yes | 3 min | no | Broken code is a classic non-exhaustive-guarded-match compile error; panic/unreachable/todo ban forces restructuring guards rather than papering over with a catch-all. Single correct fix. |
| u02/probe-a/p3-alert | yes | 6 min | **yes** | "No `_` arm: every arm names its variant" vs. battery arms using `Battery { charging: true, .. }` / `Battery { .. }` — struct-update `..` names the variant but elides fields. A stricter reading could disallow `..` too; spec doesn't say. Doesn't block solving (both readings converge on the same working code) but the constraint's own visible-test coverage is nil either way. |
| u03/attempt | yes | 8 min | no | Two files, `explicit.rs` (no `?`) and `propagate.rs` (`?`); spec and the split-at-first-`=` test agree directly. Banned-token scan is comment-inclusive; explicit.rs's own doc comment spells out "question-mark" rather than `?`, so it's safe by construction, not by luck. |
| u03/reuse-1 | yes | 4 min | no | `split_once` + `map_err` + `?`; "when both numbers are bad, x is reported" fully pins arm order, confirmed by a visible test. |
| u03/reuse-2 | yes | 4 min | no | `checked_sub` named explicitly in spec; order of Zero-check vs. subtract stated explicitly too. |
| u03/unshown | yes | 6 min | **yes** | Spec bans `map_err` and `match`, achievable only via `impl From<Utf8Error>`/`impl From<ParseIntError> for ReadError` so `?` auto-converts — spec never states these impls are needed. The one visible test naming `ReadError::from` is the only signal; a learner who reads only the prose (not that test name) would not obviously arrive at "write two From impls." |
| u03/probe-a/p1-duration | yes | 5 min | no (minor) | "2h" → `NoUnit` is implied ("ends in s or m") rather than stated outright, but a visible test confirms it directly, closing the gap. |
| u03/probe-a/p2-size | yes | 5 min | **yes** | Given broken code uses bare `?` on `ParseIntError` for two variants (`BadWidth`/`BadHeight`) that can't share one `From` impl. Spec's "`SizeError` stays as written" could be misread as forbidding a `From`-based fix — but no single `From` impl can distinguish width from height anyway, so `map_err` is the only workable fix. Ambiguity resolves by necessity, not by what the spec states; a learner could burn time on the unstated `From` dead end before finding this out. |
| u03/probe-a/p3-average | yes | 5 min | no | Empty/Bad{index,source}/integer-division fully specified. Visible tests don't exercise the divide-by-zero path directly (the Empty check intercepts it first), but the panic-ban still forces removing `.unwrap()` regardless of that gap. |

## Cross-item observations

- Structural bans ("no `_` arm," "one match," "no `if`") recur across u02/u03 and are consistently unenforced by visible tests — a learner could satisfy `cargo test` while violating the stated style constraint, in every one of reuse-1, reuse-2, unshown (u02) and p3-alert. Only u02/attempt checks a structural ban (`enum` keyword) by scanning source text; none of the match/if/wildcard bans get the same treatment.
- Two items (u01/probe-a/p3-shift, u03/probe-a/p2-size) have spec wording narrow enough to admit a technically-compliant fix that misses the intended lesson (derive-Copy instead of borrowing; a doomed From-impl detour instead of map_err). Neither is a test failure — both compile and pass visible suites — but both are worth a tighter spec line if the point is to force one specific technique.
- One item (u03/unshown) requires inferring an unstated technique (two `From` impls) from a single test name rather than from prose; everything else was directly determined by spec text and visible tests together.

## Blockers

None. All 27 items solvable blind, unaided, within the stated time caps where given; no crate failed to compile or hung.
