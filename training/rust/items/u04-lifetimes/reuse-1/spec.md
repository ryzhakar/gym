# u04 reuse-1 · predict the compiler

Edit: prediction.txt

Cap: 5 minutes. Recorded, never a stop.

- Read `cases/1.rs` to `cases/6.rs` without compiling them. Each is compiled alone as a library, edition 2021.
- For each, write one line into `prediction.txt`: the case number, a space, then `ok`, lowercase, if it compiles, or the code of the first error as rustc prints it, e.g. `3 E0502` or `3 ok`.
- `cases/` and `tests/visible.rs` are locked.
