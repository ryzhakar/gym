# Parse an integer range

Edit: src/lib.rs

- Make the crate compile and pass the tests.
- `parse_range` reads `lo..hi`, two `i32` values around the first `..`, and returns `(lo, hi)`.
- No `..`: `NoSeparator`. `lo` is not an `i32`: `BadLow`. `hi` is not an `i32`: `BadHigh`. Each carries the parse's error where it has one. The first failing step is the one reported.
- Keep `RangeError` and the signature of `parse_range` as written.
- No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!`.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
