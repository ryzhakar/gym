# u03 probe-a p2 · fix the compile error

Edit: src/lib.rs

`cargo test` fails: the crate does not compile. Make it pass.

- `administer` keeps its signature. `DoseError` stays as written.
- The dose of `drug` is the number of the first entry in `doses` whose name equals `drug` exactly; no such entry: `UnknownDrug`.
- A dose of 0 is `Empty`.
- A dose above `stock` is `TooMuch`, carrying both numbers. The stock never goes below 0.
- Otherwise return the stock left after the dose.
- No `unwrap`, `expect`, `panic!`, `unreachable!` or `todo!` in `src/lib.rs`.
- `tests/visible.rs` is locked. Held-out tests add cases.

Cap: 3 minutes. Recorded, never a stop.

Probe: unaided, trainer closed.
