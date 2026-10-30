# u04 probe-a p2 · write to the tests

Edit: src/lib.rs

Write the struct `Row` and its `impl` so `cargo test` passes. `Row`, `new` and `next_field` are `pub`.

- `Row::new(line)` takes a `&str` holding comma-separated fields, such as `"ash,birch,cedar"`. `Row` borrows `line`; it holds no `String`.
- `row.next_field()` returns `Option<&str>`: the next field, a slice of `line`. After the last field it returns `None`, and on every later call.
- The fields are the pieces between commas: a line with n commas has n + 1 fields, empty ones included. The empty line is one empty field.
- The tests keep fields after the `Row` is gone, and hold several fields at once.
- `tests/visible.rs` is locked. Held-out tests add cases.

Cap: 6 minutes. Recorded, never a stop.

Probe: unaided, trainer closed.
