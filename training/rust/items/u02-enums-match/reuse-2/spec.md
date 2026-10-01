# u02 reuse-2 · write to the tests

Edit: src/lib.rs

Cap: none. Time is recorded and never stops you.

A plotter takes three commands: draw a dot at (x, y); draw a line from (x1, y1) to (x2, y2); lift the pen. Define the type `Command` as an enum, then these functions, so `cargo test` passes:

- `dot(x: i32, y: i32)`, `line(x1: i32, y1: i32, x2: i32, y2: i32)`, `pen_up()`: each returns a `Command`.
- `cost(c: Command) -> u32`: a dot costs 1. A line costs its horizontal plus its vertical distance, and a line of length zero costs 1, like a dot. Lifting the pen costs 0.
- `endpoint(c: Command) -> Option<(i32, i32)>`: where the pen ends. A dot ends at its point and a line at its second point. Lifting the pen gives `None`.

Every arm of every `match` names its variant: no `_` arm and no catch-all binding. `..` inside a variant's pattern is fine. `tests/visible.rs` and `tests/structure.rs` are locked; `tests/structure.rs` checks this rule and that `Command` is an enum. Held-out tests add cases.
