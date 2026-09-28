# Classify a quote

Edit: src/lib.rs

- Make the crate compile and pass the tests.
- A `Pair` whose bid is above its ask is `Crossed`, equal to it `Locked`, below it `Normal`. `Halted` is `Closed`.
- Keep `Quote`, `Book` and the signature of `book` as written.
- The match keeps at most four arms.
- No `panic!`, `unreachable!`, `todo!` or `unimplemented!`.
- Locked: `tests/visible.rs`.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
