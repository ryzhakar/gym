# u03 reuse-6 · write to the tests

Edit: src/lib.rs

Cap: 10 minutes. Recorded, never a stop.

Implement `weigh` so `cargo test` passes. `Load` and `LoadError` stay as written.

- Input is a parcel manifest, one weight in grams per line, e.g. `"1200\n850\n40"`.
- No lines at all: `LoadError::Empty`.
- Lines are read in order. The first line that does not parse as a `u32`: `LoadError::BadLine`, with its position (counting from 0) and the parse error.
- If adding a line's weight takes the running total past `u32::MAX`: `LoadError::Overflow`.
- Stop at the first error: lines after it are neither parsed nor added.
- Otherwise the total weight and the heaviest parcel.
- Propagate with `?`. No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.
