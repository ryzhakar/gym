# u01 reuse-1 · fix the compile error

Edit: src/lib.rs

Cap: none. Time is recorded and never stops you.

`cargo test` fails: the crate does not compile. Make it pass.

- `lift_below_top` adds `bonus` to every score strictly below the highest score and returns the highest score (0 when there are none).
- Keep the signature. No copy of the vector: no `clone()` and no `to_vec`.
- `tests/visible.rs` is locked. Held-out tests add cases.
