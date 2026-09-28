# u01 reuse-2 · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- `broadcast` returns one line per recipient, in order: `"<recipient>: <msg>"`.
- `broadcast`'s signature stays as it is. `deliver` is yours to change.
- No copy of `msg`: no `clone`, `to_owned` or `to_string` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.
