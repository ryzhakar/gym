# u01 worked example · ownership, moves, borrows

Four subgoals. Every problem in this unit is solved by working through them in this order.

1. **Read the conflict.** Which value, where it was moved or borrowed, where it is used after.
2. **Decide what each use needs.** Own it, read it (`&`), or change it (`&mut`).
3. **Reorder or narrow.** Arrange the code so that no move or borrow overlaps a later use of the same value.
4. **Copy or move.** `Copy` types duplicate for free. Everything else moves. A `clone` is a second value: it hides a conflict and does not fix one.

## The problem

```rust
/// Moves every track into `queue`. Returns how many tracks were moved and the
/// byte length of the first one. Panics when `tracks` is empty.
pub fn enqueue(queue: &mut Vec<String>, tracks: Vec<String>) -> (usize, usize) {
    let first = &tracks[0];
    for t in tracks {
        queue.push(t);
    }
    (tracks.len(), first.len())
}
```

A test also checks that the strings in `queue` are the strings that came in, at the same heap addresses.

## Subgoal 1 · Read the conflict

`cargo build` gives two errors. The labels under each error name the three places that matter.

```
error[E0505]: cannot move out of `tracks` because it is borrowed
3 |     let first = &tracks[0];
  |                  ------ borrow of `tracks` occurs here
4 |     for t in tracks {
  |              ^^^^^^ move out of `tracks` occurs here
7 |     (tracks.len(), first.len())
  |                    ----- borrow later used here
```

```
error[E0382]: borrow of moved value: `tracks`
4 |     for t in tracks {
  |              ------ `tracks` moved due to this implicit call to `.into_iter()`
7 |     (tracks.len(), first.len())
  |      ^^^^^^ value borrowed here after move
```

Both errors concern one value, `tracks`, and one move of it: the `for` loop on line 4. Line 3 borrows `tracks` before the move, and line 7 uses the borrow and `tracks` itself after it.

## Subgoal 2 · Decide what each use needs

| use | line | needs |
|---|---|---|
| `queue.push(t)` | 5 | to own each `String`: `queue` stores it |
| `tracks.len()` | 7 | a read of `tracks`, once |
| `first.len()` | 7 | a read of the first track, once |

The loop has to own the strings, so the move on line 4 stays. The two uses on line 7 need only reads, and each read produces a number.

The compiler's help offers `for t in &tracks`. That turns the loop's use into a read, but line 5 needs ownership:

```
error[E0308]: mismatched types
5 |         queue.push(t);
  |               ---- ^ expected `String`, found `&String`
```

A borrow does not fit this use. The move stays.

## Subgoal 3 · Reorder or narrow

The reads must happen while `tracks` is still owned here, which means before line 4. Take both numbers first:

```rust
pub fn enqueue(queue: &mut Vec<String>, tracks: Vec<String>) -> (usize, usize) {
    let count = tracks.len();
    let first_len = tracks[0].len();
    for t in tracks {
        queue.push(t);
    }
    (count, first_len)
}
```

`tracks[0].len()` borrows `tracks` only for the length of that expression. No borrow is alive when the loop moves `tracks`.

## Subgoal 4 · Copy or move

`count` and `first_len` are `usize`, and `usize` is `Copy`. Holding one keeps nothing borrowed, so the move on line 4 is free to happen.

The first error's other help, `&tracks.clone()[0]`, clears E0505 only. E0382 stays, because the loop still moves `tracks` before line 7. Getting a build out of clones takes a second one, `for t in tracks.clone()`. `queue` then holds copies, and the address test fails. A clone is right when the program needs a second, independent value. This one does not.

`cargo test`: green.
