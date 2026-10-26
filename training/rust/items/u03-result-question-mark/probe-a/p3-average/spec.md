# u03 probe-a p3 · write to the tests

Edit: src/lib.rs

`average` works on good input and panics on bad input. Make it return errors instead, so `cargo test` passes. `AvgError` and the signature stay as written.

- Each entry is written `label=number`, split at the first `=`. The label may be anything.
- No entries: `AvgError::Empty`.
- Entries are checked in order, and the first bad one is reported with its index (counting from 0): no `=` in it is `AvgError::NoEquals`; a number that does not parse as an `i64` is `AvgError::Bad`, with the parse error.
- Otherwise the sum of the numbers divided by the count, with integer division. The sum fits an `i64`.
- No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.

Cap: 6 minutes. Recorded, never a stop.

Probe: unaided, trainer closed.
