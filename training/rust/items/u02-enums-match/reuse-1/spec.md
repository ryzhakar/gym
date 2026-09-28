# u02 reuse-1 · write to the tests

Edit: src/lib.rs

Implement `price`, in cents, so `cargo test` passes. `Ticket` stays as written.

- Adult: 65 or older 800; otherwise 1200.
- Child: under 3 free; otherwise 600.
- Group of n people: 0 people 0; 10 or more, 900 each; otherwise 1000 each.
- Staff: free.
- One `match`, and every arm names its variant: no `_` arm and no catch-all binding. `..` inside a variant's pattern is fine.
- `tests/visible.rs` and `tests/structure.rs` are locked. `tests/structure.rs` checks the two rules above in your source. Held-out tests add the boundaries.
