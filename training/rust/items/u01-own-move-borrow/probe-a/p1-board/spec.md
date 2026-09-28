# u01 probe-a p1 · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- `record` appends `score` and returns the best score from before the append, 0 when the board was empty.
- Keep the signature. No copy of the vector: no `clone()` and no `to_vec`.
- `tests/visible.rs` is locked. Held-out tests add cases.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
