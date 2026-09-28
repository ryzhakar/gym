# u03 probe-a p3 · write to the tests

Edit: src/lib.rs

`average` works on good input and panics on bad input. Make it return errors instead, so `cargo test` passes. `AvgError` and the signature stay as written.

- No values: `AvgError::Empty`.
- The first value that does not parse as an `i64`: `AvgError::Bad`, with its index and the parse error.
- Otherwise the sum divided by the count, with integer division.
- No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
