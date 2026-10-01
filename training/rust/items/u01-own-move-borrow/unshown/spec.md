# u01 unshown · fix the compile error

Edit: src/lib.rs

Cap: none. Time is recorded and never stops you.

`cargo test` fails: the crate does not compile. Make it pass.

- `drain_all` hands over every pending message, oldest first, and leaves the inbox with none pending. `done` grows by the number handed over.
- The messages handed over are the original strings. A test checks their heap addresses.
- Keep the signature of `drain_all` and the fields of `Inbox`. No `clone`, `to_owned`, `to_vec` or `to_string` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.
