# u01-own-move-borrow · probe-b spec, revision 2

For the second author. Rewrite `training/rust/items/u01-own-move-borrow/probe-b/` and `key/probe-b/` from this file alone. The three existing probe-b items fail the isomorph check (`trainer/checks/P3-isomorph.md`): a rename-only port of probe-a's key passes p2 and p3, and p3's key takes a route its own spec bans. Replace them. Do not open the unit's `probe-a/`, its `key/`, or any other item, except the one file this spec names under "Bans".

## Purpose

The delayed probe, run unaided at least 7 days after the unit's practice. It is isomorph b of the immediate probe (PLAN:17, PLAN:97; rust.yaml rules.spacing). A pass has to mean the learner still resolves ownership and borrow conflicts. That rules out recalling probe-a's answer, and it rules out passing without the mechanism.

## The rule that decides every slot

**Same Concept, same move, different structure.** Each slot below names the structural difference, drawn from data shape, return type, ownership direction and call site. That difference must be fixed in probe-b's locked signature or visible tests, so that probe-a's solution body, with every identifier renamed, does not compile against probe-b's tests or fails one of them. The descriptions of probe-a below are at the level of types and moves only, and they are enough to check this without opening probe-a.

## The unit's mechanism

Four subgoals, from the unit's worked example. Read the conflict: which value, where it was moved or borrowed, where it is used after. Decide what each use needs: own it, read it, or change it. Reorder or narrow so that no move or borrow overlaps a later use. Copy or move: `Copy` types duplicate for free, and a clone is a second value that hides a conflict.

## Items

All three are fix-the-compile-error, the cluster's baseline form (baseline.yaml ties_to_probes). Each stub fails `cargo build` with exactly the error named for its slot, and nothing else. The fix is 1 to 3 changed lines.

### p1 · E0502, a borrow read out as a `Copy` value

- Same move: a shared borrow obtained from a reading method on a collection is still alive at a mutating call on the same collection. The learner reads out the `Copy` value it points to before the mutation.
- probe-a's shape: the collection holds plain integers, the reading method yields one of them, the mutation appends, and the function returns a bare integer with 0 for the empty case.
- **Required differences: data shape and return type.** The collection holds structs that are not `Copy` (each with at least one `String` field). The `Copy` value the learner needs is an integer field of the selected element, not the element itself. The element is selected by a reading method that takes no closure, such as `first`, `last` or `get`, because closures and iterator adapters belong to u06. The mutation is something other than an append, such as `remove`, `insert`, `swap` or `truncate`. The function returns an `Option` of that integer, `None` for the empty collection.
- Tests enforce: the signature is locked; the returned value is the one from before the mutation; the collection is not copied, checked through the heap addresses of the surviving elements' `String` fields; the empty case gives `None`.

### p2 · E0382 at a call site, lend instead of give

- Same move: a function takes an owned non-`Copy` collection, and the caller uses the collection after the call. The learner decides what the callee's use needs and changes the parameter to a borrow.
- probe-a's shape: the callee only reads, so a shared borrow fits, and reading what the caller needs before the call also works.
- **Required difference: ownership direction.** The callee changes the collection in place, for example by trimming, sorting, or marking entries. The caller's return value depends both on that change and on the collection afterwards. The only fix is a mutable borrow: a shared borrow does not compile, and reading before the call gives the wrong answer.
- Tests enforce: the caller's signature is locked, and the callee's signature is free; the visible and held-out cases fail for a reorder-only fix; the heap addresses of the collection's strings are unchanged after the call, which catches rebuilt strings; a source scan bans `clone`, `to_owned`, `to_vec` and `to_string`.

### p3 · E0382 in a loop, "value moved here, in previous iteration of loop"

- Same move: a value is consumed on every iteration of a loop, and the learner makes that use borrow instead.
- probe-a's shape: a small all-integer struct is passed as an owned argument to a free helper function.
- **Required differences: call site and data shape.** The consuming use is a method call whose receiver is taken by value, and the learner changes the receiver to a borrow. The struct owns heap data (at least one `String` or `Vec` field), so it cannot be `Copy` at all. Visible tests call the method with method syntax and use the struct after the loop, so a free function replacing the method does not compile against them.
- Tests enforce: the outer function's signature is locked, and the struct is locked as written, fields and derives included; the not-Copy lock described under "Bans"; a scan bans a clone call; held-out cases with zero, one, and several iterations.

Difficulty: each item is solvable in about 3 minutes by a learner who has the mechanism, with the compiler as the only aid. p2 and p3 each have exactly one legitimate fix family. p1 may admit more than one way to read the value out, and any of them passes.

## Bans probe-a enforces, carried over

- **Not-Copy lock (p3, and p1's element struct).** A visible, locked `tests/structure.rs` that fails to compile if the struct is `Copy`. It uses two blanket impls of a probe trait, one of them bounded on `Copy`, so that a `Copy` struct makes the probe call ambiguous. A reference implementation is `/Users/ryzhakar/pp/gym/training/rust/items/u01-own-move-borrow/probe-a/p3-shift/tests/structure.rs`. It is the one probe-a file you may open, it holds no part of probe-a's solution, and you use only its mechanism with your own type name. The spec states the rule and says the test enforces it.
- **Clone bans** as each slot lists, stated in the item's spec.
- **The key obeys every ban.** Run the structure test and the scans against the key. The previous p3 key derived `Copy` against its own spec.

## Surfaces already used: do not reuse

Word lists, rosters counted by first letter, playlists and track queues, scores below a maximum, broadcasts to recipients, inboxes, score boards, lines-and-bytes summaries, points shifted by an offset. The previous probe-b domains (restock maxima, tag reports, temperature bands) may be kept only if the slot's required differences are met.

## Conventions

- Each item is a standalone cargo crate at `probe-b/p<n>-<slug>/`: edition 2021, std only, its own empty `[workspace]` table, package name `u01-probe-b-p<n>`.
- `spec.md` in each crate: a title line, exactly one `Edit:` line, the rules as bullets naming every locked test file, then `Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.`
- Locked test files (`tests/visible.rs`, `tests/structure.rs`) are byte-identical in the stub and in `key/probe-b/p<n>-<slug>/`. The key adds `tests/heldout.rs`.
- Grading copies the learner's `Edit:` files into a copy of the key and runs `cargo test`.
- A signature lock is a held-out test that assigns the function or method to a function-pointer type written out in full.
- Build only in scratch, never in the item tree (cargo writes `Cargo.lock` beside the manifest).
- No hints: probes are unaided (PLAN:50).

## Acceptance before handing back

1. Key `cargo test --no-fail-fast` green. Stub red. Stub files graded on the key red.
2. For each slot, write down the required difference, and point to the locked signature or visible test that fixes it in place.
3. Workarounds written out and graded, red. For p1: a copied collection. For p2: a shared borrow, a reorder-only fix, and rebuilt strings. For p3: a derived `Copy` (it must fail to compile), a clone call, and a free function in place of the method. At least one legitimate alternative graded green where the slot admits one.
4. Results go in `trainer/checks/P3-probe-b-selfcheck.md`. The isomorph check, which ports probe-a's key by renaming, is rerun by a fresh sonnet (PLAN:74), not by the author.
