# u01 probe-a p2 · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- `summary` returns `"<number of lines> lines, <total bytes> bytes"`.
- `summary`'s signature stays. `byte_total` is yours to change.
- No copies: no `clone`, `to_owned`, `to_vec` or `to_string` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
