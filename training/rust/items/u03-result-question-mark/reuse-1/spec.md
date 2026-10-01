# u03 reuse-1 · write to the tests

Edit: src/lib.rs

Cap: none. Time is recorded and never stops you.

Implement `parse_point` so `cargo test` passes. `Point` and `PointError` stay as written.

- Input `"x,y"`, split at the first `,`. No spaces are allowed around the numbers.
- No `,`: `MissingComma`. A bad x: `BadX`. A bad y: `BadY`. Each carries the parse error. When both numbers are bad, x is reported.
- Propagate with `?`. No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.
