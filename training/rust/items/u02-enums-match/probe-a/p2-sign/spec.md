# u02 probe-a p2 · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- `sign_of` keeps its signature and its four answers: `"none"`, `"positive <n>"`, `"zero"`, `"negative <n>"`.
- No arm may panic: no `panic!`, `unreachable!`, `todo!` or `unimplemented!` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
