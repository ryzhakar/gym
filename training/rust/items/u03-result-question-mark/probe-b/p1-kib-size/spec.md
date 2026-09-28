# Convert a size in kibibytes

Edit: src/lib.rs

- `kib_to_bytes` reads a decimal count followed by `KiB`, such as `"64KiB"`, and returns the count times 1024 as a `u32`.
- No `KiB` at the end: `MissingUnit`.
- The count is not a valid `u32`: `BadNumber`, carrying the parse's error.
- The product does not fit in a `u32`: `TooLarge`.
- Keep `SizeError` and the signature of `kib_to_bytes` as written.
- No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!`.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
