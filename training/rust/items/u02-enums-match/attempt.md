# u02 attempt · enums and match

Edit: src/enum_form.rs, src/flat_form.rs

Crate: `attempt/`. A sensor sends one of three readings: a temperature in whole degrees Celsius, a fault with a numeric code, or off. Model it twice, and make `cargo test` pass.

1. `src/enum_form.rs`: `Reading` as an enum.
2. `src/flat_form.rs`: `Reading` as a struct, with no `enum` anywhere in the file.

Each file defines `Reading` and the same five functions:

- `temp(celsius: i32)`, `fault(code: u8)`, `off()`: each builds a `Reading`.
- `label(r: Reading) -> String`:
  - temperature 30 or above: `"hot <c>"`
  - temperature below 0: `"freezing <c>"`
  - any other temperature: `"temp <c>"`
  - fault code 0: `"fault unknown"`
  - any other fault: `"fault <code>"`
  - off: `"off"`
- `fault_code(r: Reading) -> Option<u8>`: the code of a fault, 0 included, and `None` for anything else.

The tests reach `Reading` only through these functions, so its inside is yours. `tests/visible.rs` is locked.

10 minutes, unaided, compiler on. Over 10 is recorded, never a stop.
