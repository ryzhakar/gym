# u04 probe-b p1 · fix the compile error

Edit: src/lib.rs

`cargo test` fails. Make it pass.

- The bodies of `bracketed` and `domain_or` are correct. The edit sites are their signatures.
- Both keep returning a borrowed `&str`, not an owned `String`.
- `tests/visible.rs` is locked. Held-out tests add cases.

Cap: 3 minutes. Recorded, never a stop.

Probe: unaided, trainer closed.
