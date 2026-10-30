# u04 attempt · lifetimes

Edit: src/lib.rs

Crate: `attempt/`. Three functions over sensor readings such as `"12.5kg"`. `cargo test` fails. Make it pass.

- Every function body is correct and stays as written. The edit sites are the three signatures.
- Every function keeps returning a borrowed `&str`, not an owned `String`.
- An error reported inside `tests/visible.rs` is still fixed in a signature.
- `tests/visible.rs` is locked. Held-out tests add cases.

Unaided, compiler and `rustc --explain` on.

Cap: 10 minutes. Recorded, never a stop.
