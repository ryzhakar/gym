# Parse a ticket tag

Edit: src/lib.rs

- Make the crate compile and pass the tests.
- `parse_tag` splits `text` at the first `:` into a name and a code. No `:` in the input: `NoColon`. A code that is not a `u32`: `BadCode`, carrying the parse's error.
- On success it returns the name, owned, and the code.
- Keep `TagError` and the signature of `parse_tag` as written.
- No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!`.
- Locked: `tests/visible.rs`.

Cap: 3 minutes. Recorded, never a stop.

Probe: unaided, trainer closed.
