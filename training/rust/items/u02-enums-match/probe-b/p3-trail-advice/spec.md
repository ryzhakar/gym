# Advise on a trail segment

Edit: src/lib.rs

- `advise` returns the advice for one segment.
- `Climb` under 300 metres: `Go`. From 300 to 799 metres: `Caution(2)`. 800 metres or more: `Stop`, unless `roped` is true, then `Caution(3)`.
- `Path(Surface::Paved)`: `Go`. `Path(Surface::Gravel)`: `Caution(1)`. `Path(Surface::Ice)`: `Stop`.
- `River` under 50 cm deep: `Caution(1)`. 50 cm or more: `Stop`.
- `Closed`: always `Stop`.
- Keep `Surface`, `Segment`, `Advice` and the signature of `advise` as written.
- Every arm of every `match` names a variant: no `_` arm and no catch-all binding. `_` and `..` inside a variant's pattern are fine. `tests/structure.rs` checks it.
- Locked: `tests/visible.rs`, `tests/structure.rs`.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
