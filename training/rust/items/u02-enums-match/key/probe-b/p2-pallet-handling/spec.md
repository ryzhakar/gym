# Classify a pallet load

Edit: src/lib.rs

- Make the crate compile and pass the tests.
- A crate heavier than 500 kg is `Careful`. A crate that is fragile, any weight, is also `Careful`. Any other crate is `Normal`. An empty pallet is `Skip`.
- Keep `Load`, `Handling` and the signature of `handling` as written.
- The match keeps at most four arms.
- No `panic!`, `unreachable!`, `todo!` or `unimplemented!`.
- Locked: `tests/visible.rs`.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
