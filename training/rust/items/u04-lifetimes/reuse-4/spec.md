# u04 reuse-4 · refactor to borrow

Edit: src/lib.rs

Cap: 10 minutes. Recorded, never a stop.

`src/lib.rs` works, and `tests/visible.rs` passes. It copies every piece of the log into a new `String`. Make it borrow from the log text instead, so `tests/structure.rs` passes too.

- Keep the names `Entry`, `Entry::parse`, `level`, `source`, `message`, `entries` and `first_message`, and keep each function returning the same text, now borrowed from the log instead of copied. The types that carry it are yours to change.
- No `String`, `.clone()`, `to_string`, `to_owned` or `Box` in `src/lib.rs`. Comments do not count.
- `tests/visible.rs` and `tests/structure.rs` are locked. `tests/structure.rs` checks the rule above in your source. Held-out tests add cases.
