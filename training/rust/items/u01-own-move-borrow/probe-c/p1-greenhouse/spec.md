# u01 probe-c p1 · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- `grow_short_plants` adds `growth` to every plant strictly shorter than the tallest plant, and returns the tallest plant's height from before the change.
- Keep the signature of `grow_short_plants`. `tallest` is yours to change.
- No copy of the vector or of any plant: no `clone`, `to_owned`, `to_vec` or `to_string` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
