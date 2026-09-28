# u03 probe-a p1 · write to the tests

Edit: src/lib.rs

Implement `seconds` so `cargo test` passes. `DurationError` stays as written.

- Input: a whole number followed by a unit, `s` for seconds or `m` for minutes, such as `"90s"` or `"5m"`. Return the duration in seconds.
- No `s` or `m` at the end: `NoUnit`. The number does not parse as a `u32`: `BadNumber`, carrying the parse error. Minutes whose total in seconds does not fit a `u32`: `TooLong`.
- Propagate with `?`. No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
