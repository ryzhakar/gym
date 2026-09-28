# u03 reuse-2 · write to the tests

Edit: src/lib.rs

Implement `withdraw` so `cargo test` passes. `TxError` stays as written.

- `amount_text` must parse as a `u64`; otherwise `BadAmount`, carrying the parse error.
- An amount of 0 is `Zero`.
- An amount above the balance is `Insufficient`, carrying both numbers. Detect it with the subtraction itself: `u64::checked_sub`.
- Otherwise return the new balance.
- Propagate with `?`. No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.
