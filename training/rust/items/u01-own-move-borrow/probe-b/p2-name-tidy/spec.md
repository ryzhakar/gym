# Tidy a name list

Edit: src/lib.rs

- Make the crate compile and pass the tests.
- `tidy` sorts `names`, removes repeated names, and returns how many it removed and the last name in sorted order, or `None` for an empty list.
- Keep the signature of `tidy` and `Tidy` as written. Everything else in the file may change.
- No copy of the list or of any name: no `clone`, `to_owned`, `to_vec` or `to_string`. The tests check that the name returned is the original string.
- Locked: `tests/visible.rs`.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
