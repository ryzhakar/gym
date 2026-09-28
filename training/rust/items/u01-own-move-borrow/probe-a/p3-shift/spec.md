# u01 probe-a p3 · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- `shift_all` returns every point moved by `offset`, in order.
- `shift_all`'s signature stays. `Point`'s fields stay. Anything else in `src/lib.rs` is yours to change.
- No `.clone()` call in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
