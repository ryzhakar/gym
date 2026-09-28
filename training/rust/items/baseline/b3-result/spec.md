# b3-result · write to the tests

Edit: src/lib.rs

Implement `port_of` so `cargo test` passes.

- Input `"host:port"`. Return the port as a `u16`. The host is not checked and may be empty.
- The port is everything after the first `:`.
- No `:` at all gives `AddrError::MissingColon`. A port that does not parse as a `u16` gives `AddrError::BadPort`, carrying the parse error.
- Propagate each failure with `?`. No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` anywhere in `src/lib.rs`; held-out tests check the source.
- Held-out tests add more inputs, including an error case for each step.

Cap: 2.5 minutes. Compiler and `rustc --explain` allowed. Nothing else.
