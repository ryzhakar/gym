# u02 probe-a p3 · write to the tests

Edit: src/lib.rs

Implement `alert` so `cargo test` passes. `Status` stays as written.

- Temperature 40 or above: `"heat <t>"`. Temperature -20 or below: `"frost <t>"`. Any other temperature: no alert.
- Humidity above 90: `"damp <h>"`. Otherwise no alert.
- Battery while charging: no alert. Battery under 10 percent and not charging: `"battery <p>"`. Otherwise no alert.
- Missing: `"no data"`.
- No `_` arm: every arm names its variant.
- `tests/visible.rs` is locked. Held-out tests add the boundaries.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
