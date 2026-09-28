# Parse a port and its VLAN

Edit: src/lib.rs

- Make the crate compile and pass the tests.
- `link` parses `port` as a `u8` and `vlan` as a `u16`. A port that is not a `u8`: `BadPort`. A VLAN that is not a `u16`: `BadVlan`. Each carries the parse's error. VLAN 0: `ReservedVlan`. The first failing step is the one reported.
- Keep `LinkError`, `Link` and the signature of `link` as written.
- No `From` impl in `src/lib.rs`; `tests/structure.rs` checks it.
- No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!`.
- Locked: `tests/visible.rs`, `tests/structure.rs`.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
