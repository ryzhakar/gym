# u04 reuse-3 · fix the compile errors

Edit: src/lib.rs

Cap: 5 minutes. Recorded, never a stop.

`cargo test` fails: the crate does not compile. Make it pass by reordering lines.

- Both functions keep their signatures and the behaviour their doc comments state.
- No copy of a string: no `.clone()`, `.cloned()`, `to_owned`, `to_string` or `String::from` in `src/lib.rs`.
- `tests/visible.rs` and `tests/structure.rs` are locked. Held-out tests add cases.
