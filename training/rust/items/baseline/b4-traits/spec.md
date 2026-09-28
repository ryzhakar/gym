# b4-traits · write to the tests

Edit: src/lib.rs

Make `cargo test` pass.

- Implement `Area` for `Rect` (width times height) and for `Square` (side squared).
- Write `total_area`: one generic function over any type that implements `Area`. It takes a slice of that type and returns the sum of the areas, `0.0` for an empty slice.
- Held-out tests call `total_area` with a type of their own that implements `Area`.

Cap: 2.5 minutes. Compiler and `rustc --explain` allowed. Nothing else.
