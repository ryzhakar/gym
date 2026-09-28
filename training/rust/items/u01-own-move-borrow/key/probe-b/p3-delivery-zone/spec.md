# Count orders inside a delivery zone

Edit: src/lib.rs

- Make the crate compile and pass the tests.
- `Zone::covers` says whether a postcode is one of the zone's postcodes. `count_covered` returns how many orders the zone covers.
- Keep the signature of `count_covered` and `Zone` as written, fields and derives included. `Zone` stays not `Copy`; `tests/structure.rs` checks it.
- `covers` stays a method of `Zone`.
- No clone call.
- Locked: `tests/visible.rs`, `tests/structure.rs`.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
