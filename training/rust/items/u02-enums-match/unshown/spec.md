# u02 unshown · write to the tests

Edit: src/lib.rs

Implement `next` so `cargo test` passes. `Door` and `Action` stay as written.

- Closed + Pull → Open. Open + Push → Closed. Closed + Lock → Locked. Locked + Unlock → Closed.
- Every other pair leaves the door as it is.
- `next` uses exactly one `match` and no `if`.
- `tests/visible.rs` and `tests/structure.rs` are locked. `tests/structure.rs` checks the rule above in your source. Held-out tests check all twelve pairs.
