## f008237 — A Complete Guide to WASIp2 for Rust and Python Programmers (2025-01-01, en)

### Nothing new
A technical WASIp2/component-model tutorial (Rust and Python guest/host examples); the one candidate dispute — the author's own filed issue that `rustc` pulls in the whole `wasi:cli` world for a simple `format!` call — is reported as an unresolved bug, not an argued Position against a competing view, and no author name/handle is given anywhere on the page to establish a Voice.

---

## f008241 — Floating point to hex converter – now supports 16-bit floats, plus I rewrote it in Rust and WebAssembly! (2025-01-08, en)

### Questions
- Q: When an allocation-avoiding type like `Cow<str>` would only save a negligible amount of work, should a Rust programmer still prefer it over a plain `String`, for the sake of making allocations visible in the code?
  concepts: `Cow`, allocation, idiomatic Rust; domains_live: core, web; positions_seen: prefer-cow-for-allocation-visibility-even-at-negligible-gain (gregstoll)
- Q: Does a language's built-in, first-party package manager (like Cargo) meaningfully change engineering practice compared to bolted-on/ecosystem-only dependency management (as in C/C++)?
  concepts: package management, dependency ecosystem, tooling; domains_live: core; positions_seen: builtin-package-manager-changes-practice (gregstoll)

### Claims
- voice: gregstoll | position: prefer-cow-for-allocation-visibility-even-at-negligible-gain | date: 2025-01-08 | locator: section "Step 2: Adding 16-bit float support", paragraph on the `Cow<&str>` commit | paraphrase: switched query parsing from `String` to `std::borrow::Cow<&str>`; likes that Rust makes allocations visible, which pushes them to avoid allocations even when the performance impact is minuscule | quote: "I really like how obvious Rust makes it when you're doing allocations and that makes me want to avoid them, even when the performance impact is minuscule." | practiced_evidence: https://gregstoll.wordpress.com/2025/01/08/floating-point-to-hex-converter-now-supports-16-bit-floats-plus-i-rewrote-it-in-rust-and-webassembly (linked commit)
- voice: gregstoll | position: builtin-package-manager-changes-practice | date: 2025-01-08 | locator: section "Maybe…Rust?" | paraphrase: didn't even think to look for a C/C++ library with `f16`/bfloat support, because even if one existed they'd have had to vendor its source; running `cargo add half` was trivially easy by comparison, which they read as evidence that a good builtin package manager matters | quote: "I think this is an example of why having a good builtin package manager matters; even if I had found a C/C++ one I would have had to copy its source into my project or something. […] But just running cargo add half is so easy!" | practiced_evidence: none

---

## f008381 — The Embedded Rustacean Issue #42 (2025-04-02, en)

### Nothing new
A bi-monthly link-roundup newsletter (news, article titles, crate/event/job listings); no Voice's own argued words appear beyond headlines and one unattributed inspirational quote, so no disagreement can be extracted from the source itself.

---

## f008455 — iOS Deep-Linking with Bevy (2025-05-28, en)

### Nothing new
A step-by-step tutorial on wiring `AppDelegate` URL-open callbacks into a Bevy app via `objc2` and the new `bevy_ios_app_delegate` crate; purely instructional, no contested design Position is argued anywhere in the post.

---

## f008566 — The Embedded Rustacean Issue #52 (2025-08-20, en)

### Nothing new
Same link-roundup newsletter format as Issue #42; no Voice's own argued words beyond headlines.

---

## f008777 — The Embedded Rustacean Issue #63 (2026-01-21, en)

### Nothing new
Same link-roundup newsletter format; no Voice's own argued words beyond headlines.

---

## f008940 — Scientific Computing in Rust Monthly #18 (2026-05-27, en)

### Nothing new
A release-notes/link newsletter (crate updates, an event announcement, two publication pointers); the one item with editorial framing (the `image-rs` `fast_blur` article) is described, not quoted, and its actual argument lives in a linked article this source doesn't reproduce.

---

## f009074 — The Embedded Rustacean Issue #79 (2026-09-02, en)

### Nothing new
Same link-roundup newsletter format; no Voice's own argued words beyond headlines.

---

## f009090 — Can You Use ESP32 as SWD Programmer for STM32 with Rust? (2026-09-16, en)

### Nothing new
A from-scratch SWD-protocol implementation tutorial (bit-banged GPIO, request/ACK framing, full working `no_std` code); purely instructional walkthrough, no contested design Position is argued.

---

## f009632 — Next Steps on the Rust Trademark Policy (2024-11-06, en)

### Nothing new
A Leadership Council announcement that a revised trademark-policy draft is open for final feedback; it references that "many members of our community were concerned" about an earlier draft but does not quote or restate any specific competing Position, so no Claim can be located in the source itself.

---

## f009704 — Demoting x86_64-apple-darwin to Tier 2 with host tools (2025-08-19, en)

### Nothing new
A factual policy-application announcement (GitHub dropped free macOS x86_64 CI runners, so the target no longer meets the Tier 1 testing requirement); no opposing view is present or argued against in the post.

---

## f009751 — Announcing our first Maintainers in Residence (2026-08-26, en)

### Questions
- Q: Does funding maintainers directly (vs. relying on volunteer labor) materially change the sustainability and quality of critical Rust infrastructure maintenance?
  concepts: open-source funding models, maintainer burnout, project governance; domains_live: core; positions_seen: paid-maintenance-improves-focus-and-sustainability (Alejandra González, Jonas Böttiger, Gen Li)

### Claims
- voice: Alejandra González (@blyxyas) | position: paid-maintenance-improves-focus-and-sustainability | date: 2026-08-26 | locator: bio section "Alejandra González (@blyxyas)" | paraphrase: being funded lets her put her full effort into the project without financial anxiety, directly boosting her productivity | quote: "Funding is the system that helps me pour my heart into a project without worrying about making ends meet. Having those needs met is a game-changer and boosts my productivity." | practiced_evidence: none
- voice: Jonas Böttiger (@joboet) | position: paid-maintenance-improves-focus-and-sustainability | date: 2026-08-26 | locator: bio section "Jonas Böttiger (@joboet)" | paraphrase: funding removes the tradeoff between doing the maintenance work he loves and taking a better-paid job elsewhere | quote: "Getting funding for my work is a dream come true. It will allow me to continue doing the thing I love instead of worrying about whether I should rather invest all that time in a money-earning job with much less positive impact on the world around me." | practiced_evidence: none

---

## f011484 — RFCs for changes to Rust (2023-09-27, en)

### Nothing new
The RFC repository's process document (when an RFC is required, the FCP mechanism, sub-team sign-off, postponement); it describes the governance mechanism itself rather than any one Voice arguing a Position on a contested substantive question.

---

## f011614 — The Tianyi-33 Satellite Equipped with RROS Successfully Entered Orbit (2023-12-20, en)

### Nothing new
A short, unbylined news announcement that BUPT's Rust-based dual-kernel OS (RROS) flew on the Tianyi-33 satellite; purely factual, no argued Position on a contested question.
