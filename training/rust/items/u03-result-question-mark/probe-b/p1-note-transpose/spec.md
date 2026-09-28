# Transpose a note

Edit: src/lib.rs

- `transpose` reads a note written `N` followed by its number, such as `"N60"`, and moves it by `semitones`.
- On success it returns the written number and the sounding number, both `u8`.
- No `N` at the start: `MissingPrefix`.
- The number is not a valid `u8`: `BadNumber`, carrying the parse's error.
- The moved note is below 0 or above 255: `OutOfRange`.
- Keep `PitchError`, `Pitch` and the signature of `transpose` as written.
- No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!`.
- Locked: `tests/visible.rs`.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
