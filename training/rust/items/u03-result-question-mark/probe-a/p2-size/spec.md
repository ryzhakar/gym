# u03 probe-a p2 · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- `area` keeps its signature. `SizeError` stays as written.
- Each failure gives its own variant, carrying the parse error where there is one.
- No `From` impl in `src/lib.rs`. No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` either.
- `tests/visible.rs` and `tests/structure.rs` are locked. `tests/structure.rs` checks the `From` rule in your source. Held-out tests add cases.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
