# u03 reuse-3 · write to the tests

Edit: src/lib.rs

Cap: none. Time is recorded and never stops you.

Implement `tally` so `cargo test` passes. `Tally` and `TallyError` stay as written.

- Input is whitespace-separated ballot counts, e.g. `"120 98 143"`.
- No counts at all: `TallyError::NoBallots`.
- The first count that does not parse as a `u32`: `TallyError::BadEntry`, with its position (counting from 0) and the parse error.
- Otherwise the total of all counts and the largest one.
- Propagate with `?`. No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.
