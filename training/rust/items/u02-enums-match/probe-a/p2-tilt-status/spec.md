# u02 replacement r1 · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- `tilt_status` keeps its signature and its four answers: `"none"`, `"right <n>"`, `"level"`, `"left <n>"`.
- No arm may panic: no `panic!`, `unreachable!`, `todo!` or `unimplemented!` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
