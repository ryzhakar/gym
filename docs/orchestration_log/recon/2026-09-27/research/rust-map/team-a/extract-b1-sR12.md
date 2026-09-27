# Extract — batch 1, send-back, team a

Framing: for each source, where do competent Rust practitioners disagree?

## f004174 — https://forums.swift.org/t/what-is-copyable-for/84437 (2026-01-28, domain-subframes)

Nothing new — no qualifying Rust Voice. Long Swift Forums thread on `~Copyable`, rich with disagreement, but the disagreement is among Swift/C++ practitioners (dabrahams, Slava_Pestov, jrose, Joe_Groff, ben-lev, and others) about Swift's own ownership feature. A few comments compare to Rust in passing (e.g. `@Nobody1707` on `Copy`/`Clone`, `@jrose` noting Rust atomics/Mutex allow moving) but none establishes itself as a Voice with a public Rust track record per rust.md's Voice rule — no crate maintenance, production Rust use, project/foundation role, or Rust book/course/talk/post is claimed by any participant. No Claim to log.

## f004205 — https://forums.swift.org/t/escapable-span-ownership-annotations-etc/84566 (2026-02-04, domain-subframes)

Nothing new — same reason as f004174. Dave Abrahams (`dabrahams`, Hylo language designer) and the Hylo team (`Alvae`) argue at length that Rust-style first-class references/lifetimes are unneeded complexity Swift should avoid, using Rust code (`fn foo(x: T) -> &U { &x.something }`) as a comparison point, and note "the same conversation with Rust folks" elsewhere — but this is Hylo/Swift designers arguing about Rust from outside it, not a Rust practitioner's own Position. No participant claims a Rust track record. No Claim to log.

## f004229 — https://pingcap.com/blog/seamless-tidb-cloud-upgrades-replicating-production-workloads-traffic-replay (2026-02-09, domain-subframes)

Nothing new — no Rust content. Single-author PingCAP product post (Ming Zhang) describing TiDB Cloud's "Traffic Replay" testing tool for database upgrades. Mentions TiKV only as a nav-menu product link; the article itself never discusses Rust, language design, or any practitioner disagreement. No Voice, no Claim.

## f004369 — https://neon.com/blog/ctrl-c-in-psql-gives-me-the-heebie-jeebies (2026-03-05, domain-subframes)

Nothing new — no Rust content. Single-author Neon blog post (George MacKerron) on the Postgres `CancelRequest`/`Ctrl-C` protocol quirk and his Ruby-based `Elephantshark` proxy tool. Entirely about the Postgres wire protocol and libpq/psql (C); no Rust practitioner, no Rust-relevant claim.
