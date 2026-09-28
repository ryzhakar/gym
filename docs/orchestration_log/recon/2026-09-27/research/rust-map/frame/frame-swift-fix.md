# Frame fix, swift-interop: Tier 1 change (2026-09-28)

Preparer: r-batch2-prep. This is a Tier 1 change to the sampling frame and is logged as one (`slice-1-review.md` line 123, target (3)). `frame.csv` is not edited, so its sha256 `99ea45bb…80e7` stays the audit trail. The fix is a drop list, and `scripts/map/prepare_frame.py --drop` applies it when the sampler input is built.

## Rule (mechanical, fixed before any batch-2 draw)

A frame row is dropped from sampling when both hold:
1. its URL host, lowercased and with any `www.` removed, is `forums.swift.org`;
2. neither its title nor its URL path matches the regex `\brust`, case-insensitive. The regex matches rust, Rust's, rustc, rustup and rustls, but not trust or frustrat….

The rows are dropped, not reclassed. Removing their only hint (`swift-interop`) would make them hint-less, and the batch-1 rule then samples hint-less rows as `core`. That would move Swift-internal threads into core.

Ground: in batch 1, 27 of 38 swift-interop sampled rows were forums.swift.org threads. Every audit pass read them as Swift-internal and off-subject: `audit/audit-b1.md` f001837, f003923; `audit-b1-sendback.md` f002042; `audit-b1-third.md` f001677, f002042, f004174, f004371. The two strikes on rule 9 in `strike-b1-third.md` are Swift/Hylo arguments mapped onto Rust.

## Counts (by script, 2026-09-28)

| file | rows (window=in) | swift-interop hint rows | forums.swift.org rows | matched by rule | dropped |
|---|---|---|---|---|---|
| `frame.csv` | 11,083 | 212 | 169 | 0 | 169 |
| `frame-v2-nonen.csv` | 2,248 | 4 | 0 | 0 | 0 |

- All 169 dropped rows carry class `domain-subframes` and the single hint `swift-interop`. None carries a second hint, so no other stratum loses a row.
- In-window swift-interop rows left in `frame.csv`: 43. By sampling class: talks 13, hn-lobsters 8, domain-subframes 6, individual-blogs 5, internals 5, twir-links 4, books-courses 1, project-blog 1.
- Batch-1 swift-interop rows the rule would have dropped: team A 15 of 19, team B 12 of 19. That is 27 of 38, matching the review.
- `slice-1-review.md` quotes "169 of 262". The 262 is the `frame-stats.md` count across both windows; the in-window count is 212.

Drop list: `frame/frame-swift-fix-drop.csv` (columns frame_id, url, title; 169 rows; sha256 `2c79632e3437b8b71c54464b79ca4ced1977b2af47549d23fc02317213165e6f`).

Script that wrote it, run from RECON:

```python
import csv, re
from urllib.parse import urlparse
RUST = re.compile(r"\brust", re.I)
out = []
for path in ["frame/frame.csv", "frame/frame-v2-nonen.csv"]:
    for r in csv.DictReader(open(path, encoding="utf-8", newline="")):
        u = urlparse(r["url"])
        if u.netloc.lower().removeprefix("www.") == "forums.swift.org" and not RUST.search(r["title"]) and not RUST.search(u.path):
            out.append({"frame_id": r["frame_id"], "url": r["url"], "title": r["title"]})
with open("frame/frame-swift-fix-drop.csv", "w", encoding="utf-8", newline="") as h:
    w = csv.DictWriter(h, fieldnames=["frame_id", "url", "title"]); w.writeheader(); w.writerows(out)
```

## What this cannot show

- Some dropped threads carry Rust passages in their bodies. The auditors read such passages in f001837, f003923 and f002042 and found no loggable Position. The rule reads titles and paths only, so any Rust Position inside an unread Swift thread leaves the frame with it. Seven audited threads are the only evidence that the loss is small.
- 43 rows is a small stratum. Batch 1 used 4 (team A) and 7 (team B) of the rows that remain, so team A has 39 unused rows and team B 36. Rule 4 (seen ≥ 10 after three batches, or merge into core) still governs it.
- swift-interop is not among batch 2's drawn cells (`batch-2-prep.md`). The fix is in place for the first batch that draws it.
