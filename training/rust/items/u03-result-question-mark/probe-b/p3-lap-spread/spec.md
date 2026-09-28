# Fastest and slowest lap

Edit: src/lib.rs

- `spread` reads lap times in whole seconds separated by `;`, split as `str::split_terminator(';')` splits them, and returns the fastest and the slowest lap.
- The current code is right for good input. Make it return an error instead of panicking.
- Empty input: `Empty`.
- A field that is not a `u32`: `BadLap`, with the position of the first such field, counting from 0.
- Keep `LapError`, `Spread` and the signature of `spread` as written.
- No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!`.
- Locked: `tests/visible.rs`.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
