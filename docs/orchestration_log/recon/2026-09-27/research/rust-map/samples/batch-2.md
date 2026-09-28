# Rust map — batch 2 sample

Drawn 2026-09-28 by r-batch2-prep, after the prompts were frozen (`batch-2-prep.md`). Current state after replacements: 285 rows per team, every row with cached text (§ Replacements, `batch-2-prep.md` § 8). The draw tables below describe the original 292-row draw.

## Inputs (sha256 verified before use)

| file | sha256 | rows (window=in) |
|---|---|---|
| `frame/frame.csv` | `99ea45bb67b8c64238c7cff0286ca74cd4c27db06aa96c20b9b6f6823dab80e7` (matches `frame-stats.md`) | 11,083 |
| `frame/frame-v2-nonen.csv` | `969e697f66488ab8b79e9dc11e76a84271b5764f684c11e740c1b34918a7f445` (matches `frame-v2-stats.md`) | 2,248 |
| `frame/frame-swift-fix-drop.csv` | `2c79632e3437b8b71c54464b79ca4ced1977b2af47549d23fc02317213165e6f` | 169 ids |
| `samples/frame-b2-input.csv` (built below) | `17204ed5e3889715cd612ddf541411297b66597d6bdb2577b0699c38f78cf72d` | 13,148 |
| `samples/cells-b2.csv` | `5db7b3eaeca222acebf22ae19f3cc1c0b8d4546a2750e16ee74222c914e0ea09` | 16 cells |

## Seed

`1311957526` for team a; team b reads seed+1 = `1311957527` (sampler contract). The seed came from `secrets.randbits(31)` in the step before the draw. It was the only draw. Re-running the command below into a scratch directory that holds batch 1's files gives byte-identical team files, checked by `cmp`.

## Commands (from GYM)

```
uv run python scripts/map/prepare_frame.py --frame RECON/frame/frame.csv --frame RECON/frame/frame-v2-nonen.csv --drop RECON/frame/frame-swift-fix-drop.csv --out RECON/samples/frame-b2-input.csv
uv run python scripts/map/sample.py --frame RECON/samples/frame-b2-input.csv --out RECON/samples --batch 2 --cells RECON/samples/cells-b2.csv --by-class --seed 1311957526
```

`prepare_frame.py` applies batch 1's rules unchanged: hint-less rows go to `core`, `other`-only rows are excluded, and non-strata hints are stripped. It also keeps only `window=in` rows and applies the swift-interop drop list (`frame/frame-swift-fix.md`). Read 13,331 rows, dropped 169 by the list, wrote 13,148: en 10,924 (including the 10 English uk-conference talks in frame v2 that are not `other`-only), zh 2,089, uk 103, de 32. Run on `frame.csv` alone, it reproduces `frame-b1-input.csv` byte for byte (`scripts/map/test_sample.py`).

`--by-class` splits each cell's quota evenly across its source classes; a class is the first `;`-token of the class string. Rows a team already drew in an earlier batch, or in an earlier cell of this batch, are excluded.

## Cells (`cells-b2.csv`)

| language | cells | per team | ground |
|---|---|---|---|
| en | core, ml, desktop-cli-ui, embedded, wasm | 18 each | `slice-1-review.md` line 123, targets (1) and (5) |
| zh | core, ml, web, distributed, desktop-cli-ui, embedded, decentralized-iroh, wasm, frontend: every zh cell with ≥ 18 frame rows (zh cloud-workers 4 and swift-interop 4 are not drawn) | 18 each | same line, target (6) |
| uk | the whole language as one cell | 20 | same |
| de | the whole language as one cell | 20 | same |

## Per-cell draw (pool = rows left for the team when the cell is drawn)

| cell | pool a | drawn a | pool b | drawn b |
|---|---|---|---|---|
| de/* | 32 | 20 | 32 | 20 |
| en/core | 5307 | 18 | 5306 | 18 |
| en/desktop-cli-ui | 2414 | 18 | 2417 | 18 |
| en/embedded | 674 | 18 | 675 | 18 |
| en/ml | 294 | 18 | 291 | 18 |
| en/wasm | 329 | 18 | 327 | 18 |
| uk/* | 103 | 20 | 103 | 20 |
| zh/core | 1713 | 18 | 1713 | 18 |
| zh/decentralized-iroh | 32 | 18 | 32 | 18 |
| zh/desktop-cli-ui | 41 | 18 | 41 | 18 |
| zh/distributed | 42 | 18 | 42 | 18 |
| zh/embedded | 40 | 18 | 41 | 18 |
| zh/frontend | 19 | 18 | 18 | 18 |
| zh/ml | 104 | 18 | 105 | 18 |
| zh/wasm | 26 | 18 | 27 | 18 |
| zh/web | 85 | 18 | 81 | 18 |

Every cell got its full quota. Rows per team: 292 (en 90, zh 162, uk 20, de 20), none drawn twice within a team, none reused from the team's batch 1, and none from the swift drop list.

## Rows per class (team a / team b)

| language | class | a | b |
|---|---|---|---|
| en | books-courses | 10 | 10 |
| en | hn-lobsters | 10 | 10 |
| en | talks | 10 | 9 |
| en | twir-links | 10 | 12 |
| en | individual-blogs | 9 | 9 |
| en | domain-subframes | 8 | 9 |
| en | project-blog | 8 | 7 |
| en | internals | 6 | 7 |
| en | users-forum | 7 | 7 |
| en | rfc | 7 | 6 |
| en | youtube (frame v2) | 5 | 4 |
| zh | weekly-newsletter-links | 65 | 64 |
| zh | forum-threads | 52 | 53 |
| zh | conference-talks | 33 | 33 |
| zh | qa-topics | 12 | 12 |
| uk | dou / github / youtube | 7 / 7 / 6 | 6 / 7 / 7 |
| de | blogs / podcasts / books / talks | 9 / 6 / 3 / 2 | 9 / 6 / 3 / 2 |

domain-subframes is 8–9 of the 90 English rows per team (about 10%), against 227 of 396 (57%) in batch 1.

## Rows per stratum, counting every hint a row carries (as `batch-1.md` does)

| stratum | a | b |
|---|---|---|
| en core / ml / desktop-cli-ui / embedded / wasm | 33 / 19 / 21 / 21 / 18 | 32 / 21 / 21 / 20 / 18 |
| en web (secondary hints only) | 17 | 18 |
| en frontend / iroh / distributed / swift-interop | 5 / 1 / 0 / 1 | 4 / 0 / 2 / 0 |
| zh core / ml / web / distributed / desktop-cli-ui / embedded / iroh / wasm / frontend | 21 / 22 / 26 / 18 / 20 / 19 / 19 / 20 / 19 | 19 / 21 / 30 / 18 / 19 / 19 / 19 / 20 / 19 |

## Overlap between teams

139 frame ids were drawn by both teams: en 28 of 90, zh 86 of 162, uk 10 of 20, de 15 of 20. Batch 1 had 17 of 198. Small classes and small cells are drawn close to whole, so both teams read them. This is the capture-recapture signal, but it is also a source of recapture that reflects shared reading more than coverage (`batch-2-prep.md` § What batch 2 cannot fix).

Cross-batch: 1 of team a's batch-2 rows is in team b's batch 1, and 2 of team b's batch-2 rows are in team a's batch 1. This is allowed: replacement across teams is the design, and replacement within a team is not.

## Known reachability risks in the draw (by host, not fetched)

- Paywalled or publisher book pages: team a 3 (linkedin.com, rheinwerk-verlag.de, dpunkt.de), team b 5 (pragprog.com, leanpub.com, edx.org, rheinwerk-verlag.de, dpunkt.de). Batch 1 did not attempt these domains (`prefetch-b1.md` lines 20, 26, owner ruling).
- youtube.com: team a 25 rows, team b 23. Batch 1 lost 5 talks to HTTP 429 (`prefetch-b1.md` line 22).

## Replacements (lead ruling 2026-09-28)

Paywalled book and course pages are never fetched (owner ruling, `prefetch-b1.md` lines 20 and 26). They were replaced before any read with `sample.py --replace`. Each replacement is drawn from the row's own (language, hint, class) cell, excluding every row the team has drawn in any batch or had replaced. The RNG is `Random(f"{seed}-{team}")`, and every swap is logged in `batch-2-team-{a,b}-replaced.csv`.

The paywall host list is the one in `scripts/research/cache.py` PAYWALLED_DOMAINS: batch 1's six hosts, plus pragprog.com, rheinwerk-verlag.de, dpunkt.de, pluralsight.com, udemy.com, coursera.org, educative.io and oreilly.com. A replacement that lands on a listed host is replaced in the next round.

The cell sidecars `batch-2-team-{a,b}-cells.csv` come from re-running the draw with seed 1311957526. That re-run wrote team files byte-identical to the logged draw (sha256 unchanged from the Inputs table above).

| round | seed | input | team | replaced → replacement | cell / class | pool |
|---|---|---|---|---|---|---|
| 1 | 1511926367 | `replace-b2-r1.csv` | a | f000144 (linkedin.com) → f000088 | en/ml / books-courses | 5 |
| 1 | 1511926367 | | a | f013433 (rheinwerk-verlag.de) → none | de/* / books | 0 |
| 1 | 1511926367 | | a | f013435 (dpunkt.de) → none | de/* / books | 0 |
| 1 | 1511926367 | | b | f000070 (pragprog.com) → f000182 (dbrgn.github.io/tealdeer) | en/desktop-cli-ui / books-courses | 12 |
| 1 | 1511926367 | | b | f000088 (leanpub.com) → f000149 (nogibjj.github.io/rust-tutorial) | en/ml / books-courses | 6 |
| 1 | 1511926367 | | b | f000114 (edx.org) → f000207 (fyrox-book.github.io) | en/desktop-cli-ui / books-courses | 11 |
| 1 | 1511926367 | | b | f013433 → none | de/* / books | 0 |
| 1 | 1511926367 | | b | f013435 → none | de/* / books | 0 |
| 2 | 1284475788 | `replace-b2-r2.csv` | a | f000088 (leanpub.com, drawn in round 1) → f000202 (embarkstudios.github.io/rust-gpu/book) | en/ml / books-courses | 4 |

| 3 | 621279008 | `replace-b2-r3.csv` (rows the prefetch logged unreachable after two tries) | a | f005313 → f005351; f005514 → f005692; f005855 → f005691; f007187 → f008141; f011134 → f011219; f011173 → f011369; f011336 → f011370; f013434 → none | en/core/hn-lobsters; en/wasm/hn-lobsters ×2; en/core/individual-blogs; en/embedded/talks ×2; en/ml/talks; de/*/books | 623; 5; 4; 1892; 31; 30; 6; 0 |
| 3 | 621279008 | | b | f005514 → f005692; f005855 → f005676; f007507 → f008860; f011194 → f011372; f011336 → f011286; f011546 → f011863; f013434 → none; f015639 → f015635 | en/wasm/hn-lobsters ×2; en/desktop-cli-ui/individual-blogs; en/core/talks; en/ml/talks; en/core/twir-links; de/*/books; en/core/youtube | 3; 2; 68; 268; 4; 1553; 0; 4 |

| 4 | 72851214 | `replace-b2-r4.csv` (golem.de consent wall: html, Wayback and browser all returned the wall; found while bundling) | a | f013430 → f013416 | de/* / blogs | 12 |
| 4 | 72851214 | | b | f013431 → f013414 | de/* / blogs | 12 |

After round 2, neither team holds a row on a listed host. Round 3 replaced the rows the prefetch could not reach, as the plan requires (`fable-plan.md` line 111). All 13 replacements were then fetched (`prefetch-b2-replacements.csv`).

- The de/books class holds 3 frame rows, and each team had drawn all 3. The two paywalled ones and rust-lernen.de (no chapter text) have no replacement, so de is 17 rows per team, not 20.
- Rows per team are now 289: en 90, zh 162, uk 20, de 17.
- Teams share 136 frame ids (was 139); 442 distinct ids.
- f000149 is batch 1's send-back miss, never read in batch 1 (`audit-b1-third.md` § Open carry-overs). Team B now reads it in batch 2.

Commands (from GYM), after the re-run that wrote the sidecars:

```
uv run python scripts/map/sample.py --frame RECON/samples/frame-b2-input.csv --out RECON/samples --batch 2 --replace RECON/samples/replace-b2-r1.csv --seed 1511926367
uv run python scripts/map/sample.py --frame RECON/samples/frame-b2-input.csv --out RECON/samples --batch 2 --replace RECON/samples/replace-b2-r2.csv --seed 1284475788
uv run python scripts/map/sample.py --frame RECON/samples/frame-b2-input.csv --out RECON/samples --batch 2 --replace RECON/samples/replace-b2-r3.csv --seed 621279008
uv run python scripts/map/sample.py --frame RECON/samples/frame-b2-input.csv --out RECON/samples --batch 2 --replace RECON/samples/replace-b2-r4.csv --seed 72851214
```

Round 5 (lead ruling 2026-09-28, option 1): the 33 zh conference-talks rows per team, dropped by the Tier 1 fix in `frame/frame-zh-talks-fix.md`, were redrawn with `--replace --other-class`. Each came from the same (zh, hint) cell's other classes, excluding every row the team has drawn or had replaced. Seed `682461957`; input `replace-b2-r5.csv`; every swap is in `batch-2-team-{a,b}-replaced.csv`.

```
uv run python scripts/map/sample.py --frame RECON/samples/frame-b2-input.csv --out RECON/samples --batch 2 --replace RECON/samples/replace-b2-r5.csv --other-class --seed 682461957
```

| team | redrawn | forum-threads | weekly-newsletter-links | qa-topics | no replacement |
|---|---|---|---|---|---|
| a | 29 | 16 | 12 | 1 | 4 |
| b | 29 | 17 | 11 | 1 | 4 |

The 4 with no replacement are zh/frontend rows (f013474, f013501, f013533, f013538). That cell holds 19 frame rows, and each team had already drawn every other one. All 51 distinct replacement rows were fetched (`prefetch-b2-replacements-r5.csv`: 39 fetched, 12 already cached).

Final: 285 rows per team (en 90, zh 158, uk 20, de 17); 132 frame ids shared; 438 distinct.

Replacement files, sha256 after round 5: see `batch-2-prep.md` § 6.
