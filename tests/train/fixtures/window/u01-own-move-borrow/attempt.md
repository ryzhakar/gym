# u01 attempt · ownership, moves, borrows

Edit: src/lib.rs, src/caller_side.rs, src/callee_side.rs

Crate: `attempt/`. `cargo test` fails: the crate does not compile. Make it pass.

Three fixes:

1. `drop_shorter_than_first` in `src/lib.rs`.
2. `a_report` in `src/caller_side.rs`, by editing `a_report` only. `count_starting` stays as written; a test checks its signature.
3. `a_report` in `src/callee_side.rs`, by changing what `count_starting` takes. Edit `a_report` only where that change forces it.

Fixes 2 and 3 are two different ways out of the same error.

- No copies of any `String`: no `clone`, `to_owned`, `to_vec` or `to_string` in any file under `src/`. Tests check the source and the strings' heap addresses.
- `tests/visible.rs` is locked.

10 minutes, unaided, compiler on. Over 10 is recorded, never a stop.
