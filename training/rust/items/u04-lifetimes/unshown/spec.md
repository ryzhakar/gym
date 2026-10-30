# u04 unshown · write to the tests

Edit: src/lib.rs

Cap: 10 minutes. Recorded, never a stop.

Write two public functions in `src/lib.rs` so `cargo test` passes. Each takes a `line` and a `marker`, both text.

- `after(line, marker)`: the text of `line` after the first `marker`; the whole of `line` when `marker` does not occur. The result is that part of `line` itself, not a copy.
- `swap(line, marker)`: `line` with the two sides around the first `marker` swapped, the marker kept between them: `"key=value"` with `"="` gives `"value=key"`. The whole of `line` when `marker` does not occur.
- A caller keeps each result after `marker` is dropped.
- Choose the parameter and return types yourself. No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!`.
- `tests/visible.rs` and `tests/structure.rs` are locked. `tests/structure.rs` checks the rule above in your source; comments and string literals do not count. Held-out tests add cases.
