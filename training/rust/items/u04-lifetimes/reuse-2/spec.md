# u04 reuse-2 · write to the tests

Edit: src/lib.rs

Cap: 10 minutes. Recorded, never a stop.

Write `Header`, its `impl`, and the two functions below, so `cargo test` passes. The lifetime annotations are yours to write.

- `Header` is a struct with two public fields, `name` and `value`. Both are string slices borrowed from the line the header was parsed from, never `String`.
- `Header::parse(line)` splits `line` at its first `": "`: `"Content-Type: text/html; charset=utf-8"` gives name `"Content-Type"` and value `"text/html; charset=utf-8"`. A line with no `": "` gives `None`.
- `header.main_value()` is the value up to its first `;`, or the whole value if it has none: `"text/html"` for the header above.
- Nothing is trimmed, and an empty part is kept: `": x"` gives name `""`, `"X-Empty: "` gives value `""`, and a value `"a ; b"` gives main value `"a "`.
- The tests use `main_value()`'s result after the header is gone: dropped, moved, or left behind in a function that returns it.
- `tests/visible.rs` is locked. Held-out tests add cases.
