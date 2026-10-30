# u04 probe-b p2 · write to the tests

Edit: src/lib.rs

Write the struct `Pairs` and its `impl` so `cargo test` passes. `Pairs`, `new` and `next_pair` are `pub`.

- `Pairs::new(query)` takes a `&str` of `key=value` pieces separated by `;`, such as `"size=9;color=red"`. `Pairs` borrows `query`; it holds no `String`.
- `pairs.next_pair()` returns `Option<(&str, &str)>`: the next piece split at its first `=` into key and value, both slices of `query`. A piece with no `=` is all key, with the value `""`. After the last piece it returns `None`, and on every later call.
- The pieces are the text between `;`s. Empty pieces, from a leading, doubled or trailing `;`, are skipped. The empty query has no pieces.
- The tests keep pairs after the `Pairs` is gone, and hold several pairs at once.
- `tests/visible.rs` is locked. Held-out tests add cases.

Cap: 6 minutes. Recorded, never a stop.

Probe: unaided, trainer closed.
