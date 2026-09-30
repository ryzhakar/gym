# u01 probe-c p2 · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- `cycle` moves the track at the front of `Queue` to the back, and returns the byte length of the track now at the front, or 0 when the queue is empty.
- `cycle_count_history` calls `cycle` once per requested cycle and records what each call returned, in order.
- Keep the signature of `cycle_count_history`. `cycle` is yours to change.
- No copy of the vector or of any track: no `clone`, `to_owned`, `to_vec` or `to_string` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
