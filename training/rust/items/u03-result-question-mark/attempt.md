# u03 attempt · Result and `?`

Edit: src/explicit.rs, src/propagate.rs

Crate: `attempt/`. A config line reads `name=count`. Write `parse_line(line: &str) -> Result<(&str, u32), LineError>` twice, and make `cargo test` pass.

1. `src/explicit.rs`: without the `?` operator. The character `?` must not appear anywhere in that file.
2. `src/propagate.rs`: with `?` for the failures.

Rules, the same for both:

- Split at the first `=`. No `=` at all: `LineError::NoEquals`.
- Nothing before the `=`: `LineError::EmptyName`.
- The part after the `=` must parse as a `u32`; otherwise `LineError::BadCount`, carrying the parse error.
- On success, return the name, borrowed from `line`, and the count.
- No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` in either file.

`LineError` is in `src/lib.rs` and stays as written. `tests/visible.rs` is locked.

10 minutes, unaided, compiler on. Stop at 10, finished or not.
