# u03 replacement r3 · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- `administer` keeps its signature. `DoseError` stays as written.
- `dose_text` must parse as a `u32`; otherwise `BadAmount`, carrying the parse error.
- A dose of 0 is `Empty`.
- A dose above `stock` is `TooMuch`, carrying both numbers. Detect it with the subtraction itself: `u32::checked_sub`.
- Otherwise return the stock left after the dose.
- No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` either.
- `tests/visible.rs` is locked. Held-out tests add cases.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
