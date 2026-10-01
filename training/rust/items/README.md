# Rust item bank, Stage 0

Author: drill author (opus), 2026-09-28. Piece P3 of `docs/orchestration_log/recon/2026-09-28/trainer/fable-plan.md` § 4. Original Rust, edition 2021, std only.

## Layout

- `baseline/<item>/`: `spec.md` (what the learner sees), `stub/` (the crate the learner edits), `key/` (reference solution and all tests).
- `<unit>/`: `attempt.md` and `attempt/`; `example.md`; `reuse-1/`, `reuse-2/` and further `reuse-N/` where a unit's skill needs them (u03 holds three); `unshown/`; probe sides `probe-a/` (immediate), `probe-b/` (delayed) and further `probe-<letter>/` for a repeat of the unit (u01 holds `probe-c/`), each with `p1-*`, `p2-*`, `p3-*`; `hints.yaml`; `key/<problem>/` mirroring every problem path, probes included (`key/probe-a/p1-*`).
- Every problem is one standalone cargo crate: it declares its own `[workspace]`, so no item depends on another or on a parent workspace. A probe is three crates, not one workspace: one member that fails to compile makes cargo print no test result for any member (checked with cargo 1.91.1).
- Each problem's `spec.md` carries one `Edit:` line naming the files the learner may change. Nothing else in the crate is the learner's.
- A cap is a recorded time measure checked against the learner's last save, never enforced; `Cap: none` marks an item with no cap.

## Grading

Copy `key/<problem>/` to a scratch directory, copy the learner's `Edit:` files into it, run `cargo test`. Pass = every test green. The key holds the visible test files unchanged (`tests/visible.rs`, and `tests/structure.rs` where a spec names a structural rule such as no `_` arm, one `match`, no `From`, or a type that must not be `Copy`) plus `tests/heldout.rs`. The locked files, the program under a predict-output item included, are therefore always the key's, and editing them in the learner's crate changes nothing.

Predict-output items: the learner's only file is `prediction.txt`. Its test runs the item's binary and compares stdout to the prediction, with trailing whitespace trimmed per line and at the end. The test never prints the actual output.

## Not here

- `probe-b/`: written by a second author from `docs/orchestration_log/recon/2026-09-28/trainer/specs/<unit>-probe-b-spec.md`.
- Hints for probes and baseline: none. Both are unaided.

## Tools allowed to the learner

Owner ruling 2026-09-30, made in the first session.

- Baseline and probe items: `cargo build`, `cargo test`, `cargo check`, `rustc --explain`, bacon, rust-analyzer diagnostics and its quick fixes. Forbidden: clippy, documentation, web search, any LLM, AI completion.
- Practice items: the same, plus the standard library docs and the Rust Book. Any LLM and AI completion stay forbidden.
- rust-analyzer's `cargo check` on open leaves a `target/` directory; that is not a run of the program.
