For each source: where do competent Rust practitioners disagree?

Team a, batch 1, third pass, slice T07. All five sources read from the bundle; none visibly cut, no fetch made. Rules in force: 6, 8, 9 of t2-extract.md — a Claim needs a Voice whose Rust connection shows in the source, taking a side on a Rust decision with a reason or against a named alternative; flagged `voice-unverified` for tier 3; arguments from other language communities are not mapped onto Rust Questions.

## f002226 — SE-0451: Raw identifiers (2024-10-24, en)

### Questions
- Q: Should a language that accepts non-ASCII identifiers restrict them (UAX#31-style, no combining characters as identifier start) and warn on confusable identifiers, as rustc does with `confusable_idents` and `mixed_script_confusables`, or accept a broader character set?
  concepts: non-ASCII identifiers; UAX#31; UTS#55; confusable detection; lints; source-code security; domains_live: core; positions_seen: restrict-and-lint-confusables (Rust's shipped design, endorsed)

### Claims
- voice: Karl | position: restrict-and-lint-confusables | date: 2024-10-30 | locator: post 2024-10-30T08:14, "Rust is ahead of us here" and the two rustc output blocks | paraphrase: identifiers should never interact typographically with surrounding text; Rust gets this right by rejecting U+3099 as an identifier start and by warning on look-alike and mixed-script identifiers by default, where Swift gives no warning | quote: "Rust is ahead of us here." | practiced_evidence: none | flag: voice-unverified — the only Rust connection in the source is Karl's own rustc runs (`src/main.rs`, `src/lib.rs` output) in this post; no crate, role or stated Rust use. The side is taken in a Swift Evolution review and names Rust's shipped design as the better one; tier 3 should judge whether that counts as a Position on a Rust decision.

Left out: the rest of the review (test naming with raw identifiers, leading-digit enum cases, tuple `.0` vs `` .`0` ``, Unicode table versioning in the parser) is Swift design argued by Voices with no Rust connection in the source.

## f002488 — [Pitch] Explicit Specialization (2025-01-02, en)

### Nothing new
Swift Evolution pitch for `@specialize`; Rust is only described (SlugFiller 2025-01-03T02:47 and ben-cohen 2025-01-03T03:11 on Rust and C++ having no ABI for monomorphized generics), no one takes a side on a Rust decision, and no participant shows a Rust connection in the source.

## f002643 — How to Build GitHub Copilot Extensions (2025-02-06, en)

### Nothing new
A Python/FastAPI tutorial for a Copilot extension by Andrew Hamilton (Layer); Rust never appears.

## f002883 — Workaround for a TextDecoder bug in Safari causing a RangeError to be thrown (2025-04-06, en)

### Questions
- Q: Should a Rust crate maintainer cut a release as soon as a user asks for a merged fix, or batch fixes into planned releases?
  concepts: release cadence; crate maintenance; semver releases; domains_live: core; wasm; positions_seen: release-on-request

### Claims
- voice: daxpedda | position: release-on-request | date: 2025-08-06 | locator: comment 2025-08-06T11:36 ("My 2¢"), follow-up 2025-08-06T11:43 | paraphrase: making a release costs little, so a release should follow as soon as one is requested; a request in a closed PR counts, with a tracking issue so it is not lost | quote: "making a release is relatively low cost so I favor making one as soon as requested" | practiced_evidence: https://github.com/wasm-bindgen/wasm-bindgen (daxpedda merged this PR; says they are "not yet back to maintaining `wasm-bindgen`") | flag: voice-unverified — Rust connection in the source is the maintainer role on wasm-bindgen stated in the same comment.

Left out: the 1 MiB decoder margin (bes 2025-08-06T09:00 vs daxpedda's request for the exact failing byte count) is a JavaScript workaround detail, not a Rust decision; "Lets convert those to hex" and the `let`/`const` choice carry no reason on a Rust decision.

## f003238 — How GoodData turbocharged AI analytics with Qdrant (2025-07-09, en)

### Nothing new
A vendor case study (Daniel Azoulai, quoting Jan Soubusta of GoodData) on choosing Qdrant over DuckDB and pgvector for RAG; Rust never appears and no Voice shows a Rust connection.
