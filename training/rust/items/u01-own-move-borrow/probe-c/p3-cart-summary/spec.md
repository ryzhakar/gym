# u01 probe-c p3 · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- `cart_summary` returns `"<n> items cleared, now empty: <true/false>"`, where `<n>` is the number of items `Cart::empty_out` removed.
- `cart_summary`'s signature stays. `Cart::empty_out` is yours to change.
- No copies: no `clone`, `to_owned`, `to_vec` or `to_string` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
