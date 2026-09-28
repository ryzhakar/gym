# u01-own-move-borrow · probe-b spec

For the second author. Write `training/rust/items/u01-own-move-borrow/probe-b/` and `key/probe-b/` from this file alone. Do not open the unit's `probe-a/`, `key/`, or any other item: the isomorph check (PLAN:74) is valid only if probe-b comes from the spec.

## Purpose

The delayed probe, run unaided at least 7 days after the unit's practice. It is isomorph b of the immediate probe (PLAN:17, PLAN:97; rust.yaml rules.spacing). A pass has to mean the learner still resolves ownership and borrow conflicts: never by remembering probe-a, and never without the mechanism.

## The unit's mechanism

Four subgoals, from the unit's worked example: read the conflict (which value, where moved or borrowed, where used after); decide what each use needs (own, read, change); reorder or narrow so that no move or borrow overlaps a later use; copy or move (`Copy` types duplicate for free, and a clone is a second value that hides a conflict). Every item needs at least two of these.

## Items

Three items, all in the form fix-the-compile-error, the cluster's baseline form (baseline.yaml ties_to_probes). Each stub fails `cargo build` with exactly the error named for its slot, and nothing else. The fix is 1 to 3 changed lines.

| slot | error | what the learner must do | what the tests must enforce |
|---|---|---|---|
| p1 | E0502: a shared borrow of a collection (or of a struct field holding one), obtained from a reading method, is used after a mutating call on the same collection | see that the borrowed thing is only needed as a `Copy` value, and take that value before the mutation | signature locked; no copy of the collection (a source scan for a clone call and for `to_vec`); the returned value is the one from before the mutation, and an empty-collection case is covered |
| p2 | E0382 at a call site: a function takes an owned non-`Copy` collection it only reads, and the caller uses the collection after the call | either change what the callee takes (a borrow), or read what the caller needs before the move; both must pass | the caller's signature locked, the callee free to change; a source scan bans clone, `to_owned`, `to_vec`, `to_string`; held-out cases with empty and multi-element input |
| p3 | E0382 inside a loop, "value moved here, in previous iteration of loop": a small all-integer struct is passed by value to a helper on each iteration | make the helper borrow the struct | the outer function's signature locked; the struct locked as written, derives included; a visible `tests/structure.rs` that fails to compile if the struct is `Copy` (two blanket impls of a probe trait, one bounded on `Copy`, so a `Copy` struct makes the call ambiguous); a scan bans a clone call; held-out cases with zero, one, and several iterations |

Difficulty: each item is solvable in about 3 minutes by a learner who has the mechanism, with the compiler's messages as the only aid. The compiler's first suggestion must not by itself pass the held-out tests wherever that can be arranged; where it can (p2's "change this parameter to borrow" note), it is still one legitimate route.

## Surfaces already used in this unit: do not reuse

Word lists (keep or drop by length), rosters of names, counting names by first letter, playlists and track queues, lifting scores below a maximum, broadcasting a message to recipients, draining an inbox, score boards, lines-and-bytes summaries, shifting points by an offset. Pick new domains, such as inventory counts, temperature logs, or tag lists.

## Conventions

- Each item is a standalone cargo crate at `probe-b/p<n>-<slug>/`: edition 2021, std only, its own empty `[workspace]` table, package name `u01-probe-b-p<n>`.
- `spec.md` in each crate: a title line, exactly one `Edit:` line naming the learner's files, the rules as bullets, then `Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.`
- `tests/visible.rs`, locked. `key/probe-b/p<n>-<slug>/` is the full crate: the reference solution, a byte-identical `tests/visible.rs`, and `tests/heldout.rs`.
- Grading copies the learner's `Edit:` files into a copy of the key and runs `cargo test`.
- A signature lock is a held-out test that assigns the function to a function-pointer type written out in full, so any change to the signature fails to compile.
- Where copying is the workaround, prefer a heap-address check (the returned strings or vector are the originals) over a grep, since a grep for `clone` misses other copies.
- No hints: probes are unaided (PLAN:50).

## Isomorph, not copy

Same error code, same count of errors, same size of fix as the slot says. New names, types, domain and data. Copying probe-a's key into probe-b must fail to compile against probe-b's tests.

## Acceptance before handing back

1. Key `cargo test --no-fail-fast` green. Stub red. Stub files graded on the key red.
2. For every item, the two easiest workarounds written out and graded: red. At least one legitimate alternative: green. For this unit the workarounds are a clone of the moved or borrowed value, deleting the later use, and changing a locked signature.
3. The results go in `trainer/checks/P3-probe-b-selfcheck.md`, in the table shape of `P3-selfcheck.md`. The isomorph check itself is run by a fresh sonnet (PLAN:74), not by the author.
