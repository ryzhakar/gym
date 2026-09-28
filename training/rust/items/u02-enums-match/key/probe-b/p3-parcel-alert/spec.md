# Alert on a parcel

Edit: src/lib.rs

- `alert` returns the alert for a parcel, or `None` when it needs none.
- `Weighed` of 20000 grams or more: `"freight"`.
- `Weighed` of 5000 to 19999 grams: `"heavy"`.
- `Weighed` under 5000 grams: `"fragile"` if `fragile` is true, otherwise no alert.
- `Delayed(days)` of 3 days or more: `"late <days> days"`, e.g. `"late 4 days"`. Fewer days: no alert.
- `Lost`: always `"lost"`.
- `Delivered`: no alert.
- Keep `Parcel` and the signature of `alert` as written.
- No `_` arm.

Probe: unaided, trainer closed. 10 minutes for p1, p2 and p3 together.
