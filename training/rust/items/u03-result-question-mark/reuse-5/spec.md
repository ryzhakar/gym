# u03 reuse-5 · fix the compile error

Edit: src/lib.rs

Cap: 5 minutes. Recorded, never a stop.

`cargo test` fails: the crate does not compile. Make it pass.

- `host_port` keeps its signature. `AddrError` stays as written.
- Input `"host:port"`, split at the first `:`. No `:`: `NoColon`.
- The port must parse as a `u16`; otherwise `BadPort`, carrying the parse error.
- A port below 1024 is `Reserved`, carrying the port.
- On success, return the host, borrowed from `addr`, and the port.
- Propagate with `?`. No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.
