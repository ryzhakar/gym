For each source: what must a Rust practitioner decide, and where do the sources conflict on it?

Team b, batch 1, third pass, slice T08. Rules 1–8 of t2-extract.md applied.

## f004371 — "New Codable" prototype available for feedback (2026-03-06, en)

Read: all 79 posts (bundle count matches Discourse `posts_count` 79).

### Nothing new
Every statement that names Rust, serde, musli, serde_with or struct-patch comes from Swift Forums handles (chiefly @kperryua) designing a Swift API, and the source shows none of them with a public Rust track record, so under the Voice bar (docs/subjects/rust.md § Scope) the thread holds no Claim and shows no Rust practitioners in disagreement.

Dropped under the Voice bar (candidate topics for traceability, not Questions): serde vs musli data-model shape (@kperryua 2026-03-06T18:15, final paragraph); per-field serde attributes vs type-wide apply via serde_with (@kperryua 2026-05-19T21:09); type-level case renaming vs explicit per-field keys (@kperryua 2026-05-14T19:50–21:55); patching via a separate struct-patch type vs integrated into decode (@kperryua 2026-05-21T20:27).

## f004581 — Agents Week: network performance update (2026-04-17, en)

### Nothing new
The only Rust in the source is a post tag; the body (Lai Yi Ohlsen) covers network-ranking methodology (connection time, trimean, RUM) and results, and states no decision a Rust practitioner makes.

## f004688 — When "idle" isn't idle: how a Linux kernel optimization became a QUIC bug (2026-05-12, en)

### Nothing new
The post (Esteban Carisimo, Antonio Vicente) diagnoses and fixes a CUBIC idle-detection bug in quiche's `cubic.rs`; its reasoned decision is a bug fix with one correct answer (measure idle from the last ACK, not the last send), and its other statements are practice without a stated reason (CUBIC default, BBRv3 on a growing share of deployments), so under rule 8 none is a Rust practitioner's contested decision.
