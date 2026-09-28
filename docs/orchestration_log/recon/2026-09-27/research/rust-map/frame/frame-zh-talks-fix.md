# Frame fix, zh conference-talks: Tier 1 change (2026-09-28)

Preparer: r-batch2-prep. This was found while cutting the batch-2 bundles, after the draw and before any read. `frame-v2-nonen.csv` is not edited. The fix is a drop list, `frame/frame-zh-talks-fix-drop.csv`, which the batch-2 bundler applies (`scripts/research/bundle.py`, `frame_fix_drops`).

## Finding

All 104 in-window zh conference-talks rows (the 2024 and 2025 editions) carry synthetic URLs, `https://rustcc.cn/20NNconf/schedule.html#talk-N`. The anchors point at no element: the pages have no ids and no per-talk links, and the frame builder wrote the anchors as a fallback (`frame/frame-conference-talks-zh.md` § Per-talk URL fix, "2023, 2024, 2025 … no per-talk URL exists anywhere found").

The prefetch fetched the same schedule page for every row. The texts are identical within each edition: 16,315 chars for 2024 and 38,015 for 2025. The schedule holds titles and speaker names only, with no abstract and no transcript. The talks' videos sit in a Bilibili collection that could not be resolved to single talks.

A talk title is not a source that can hold a Claim (rule 3: own words, locator, date).

## Rule (mechanical)

A frame row is dropped from reading when its URL matches `^https://rustcc\.cn/20\d\dconf/schedule\.html#talk-\d+$`.

## Counts

- Frame v2, in window: 104 rows dropped (2024: 49, 2025: 55). That is every in-window zh conference-talks row.
- Drop list sha256 `d01c05c3eaf98501a92ff1a1b5cfa55b3cf9a8771046e5ad7bf447a95ea6ff5e`.
- Batch 2: 33 of team a's 162 zh rows and 33 of team b's 162 are on the list. They appear in the bundle manifests as `dropped`, reason `frame-fix:frame-zh-talks-fix-drop`.

## Resolution (lead ruling 2026-09-28, option 1)

Each dropped row was redrawn from the same (zh, hint) cell's other classes: `sample.py --replace --other-class`, seed 682461957. 29 per team were replaced. The 4 zh/frontend rows per team have no replacement, because every other row of that cell was already drawn. The table is in `samples/batch-2.md` § Replacements.
