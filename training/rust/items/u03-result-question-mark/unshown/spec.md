# u03 unshown · write to the tests

Edit: src/lib.rs

Implement `parse_reading` so `cargo test` passes. `ReadError` stays as written.

- The bytes must be UTF-8 (`std::str::from_utf8`); otherwise `ReadError::Utf8`, carrying the error.
- The text, with surrounding whitespace trimmed, must parse as a `u32`; otherwise `ReadError::Number`, carrying the error.
- Implement `From<Utf8Error>` and `From<ParseIntError>` for `ReadError`, so that `?` converts each std error into its variant by itself. The tests also call `ReadError::from` on each std error directly.
- Propagate with `?`, with no `map_err` and no `match` in `src/lib.rs`. No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` either.
- `tests/visible.rs` is locked. Held-out tests add cases.
