# Put a pallet at the front of the row

Edit: src/lib.rs

- Make the crate compile and pass the tests.
- `push_front` puts `incoming` at the front of `row` and returns the weight of the pallet that was at the front before, or `None` if `row` was empty.
- Keep the signature of `push_front` and `Pallet` as written. `Pallet` stays not `Copy`; `tests/structure.rs` checks it.
- No copy of the row or of any pallet: no `clone`. The tests check that the pallets' labels are the original strings.
- Locked: `tests/visible.rs`, `tests/structure.rs`.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
