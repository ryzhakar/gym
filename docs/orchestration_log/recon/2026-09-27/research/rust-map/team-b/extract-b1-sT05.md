For each source: what must a Rust practitioner decide, and where do the sources conflict on it?

Team b, batch 1, slice T05, third pass. Source text: bundle RECON/samples/bundles/b1-team-b-T05.txt; nothing fetched. Durations in the read log are estimates.

## f002499 — Implement `wait_for_done` for `DpiTransfer` (esp-rs/esp-hal#2884) (2025-01-03, en)

### Questions
- Q: How should an ESP32-S3 Rust firmware feed a large RGB (DPI) display from PSRAM framebuffers: cyclic DMA straight from PSRAM, restarted transfers, SRAM bounce buffers refilled from PSRAM, XIP from PSRAM, or abandon RGB for an I8080 panel?
  concepts: DMA descriptors; PSRAM bandwidth; bounce buffers; XIP; esp-hal DPI driver; I8080; domains_live: embedded; positions_seen: infinite cyclic DMA buffer; restart DMA periodically; bounce buffers + Mem2Mem DMA without XIP; acyclic bounce buffers restarted per frame; switch to I8080 display
- Q: Can bare-metal Rust (esp-hal) match Arduino/esp-idf C for demanding display work on ESP32-S3?
  concepts: esp-hal vs esp-idf/Arduino; hardware-resource efficiency; domains_live: embedded; positions_seen: bare Rust no worse, a matter of methodical alignment
- Q: Is an async executor (embassy) safe to use around timing-critical DMA display output, or does it cause the glitches?
  concepts: embassy; async on bare metal; flash/PSRAM bus contention; domains_live: embedded; positions_seen: dpi does not work well with embassy; cause is flash-bandwidth contention, not async per se
- Q: When a HAL keeps a needed low-level facility private (cache writeback, DMA interrupts for a driver-owned channel), should users drop to the PAC / copy private code, or should the HAL expose a public version?
  concepts: HAL vs PAC; API surface; unsafe register access; domains_live: embedded; positions_seen: HAL should expose a public version (PAC workaround advised as instruction only)
- Q: Should a Rust project keep a GitHub Discussions area for support and design talk, or remove it?
  concepts: project community infrastructure; knowledge retention; domains_live: core; positions_seen: removal cost lost knowledge (dissent); project removed it (no Voice in source)
### Claims
- voice: Dominaezzz | position: infinite cyclic DMA buffer, never restart transfers | date: 2026-01-29 | locator: comment 2026-01-29T04:49:37Z | paraphrase: in own projects every framebuffer's last DMA descriptor points to its first; switching buffers = relinking descriptors; breaks down once PSRAM bandwidth enters | quote: "I avoid restarting transfers and I always use an infinite DMA buffer" | practiced_evidence: none | flag: voice-unverified
- voice: EliteTK | position: SRAM bounce buffers refilled from PSRAM by Mem2Mem DMA, no XIP | date: 2026-09-06 | locator: comment 2026-09-06T10:36:52Z | paraphrase: two PSRAM framebuffers, two 1/16 bounce buffers in RAM, looping DMA to LCD, 8x descriptors to locate the emitted slice via DMA_OUT_CHx interrupt; cancels late refills; 31.1 FPS glitch-free; CPU copy rejected as "glacial" | quote: "double-buffered glitch-free output without relying on XiP from PSRAM" | practiced_evidence: none | flag: voice-unverified
- voice: Limeth | position: bounce buffers with acyclic descriptors, restart per frame | date: 2026-02-16 | locator: comment 2026-02-16T23:59:16Z | paraphrase: cyclic descriptors failed after the first frame; acyclic descriptors restarted each frame work; open to upstreaming a generic solution to esp-hal | quote: "using acyclic descriptors and restarting the transmission after each frame seems to be fine, although not as nice" | practiced_evidence: https://forgejo.limeth.cz/limeth/acid/compare/master...bounce_buffer (WIP, self-described) | flag: voice-unverified
- voice: yanshay | position: stay on an I8080 display for a PSRAM-heavy app | date: 2026-09-06 | locator: comment 2026-09-06T19:24:30Z | paraphrase: had a bounce-buffer Slint renderer working, but flash contention and PSRAM bandwidth slowed the application; kept a smaller I8080 display | quote: "didn't switch device and still use an I8080 display at lower size and resolution" | practiced_evidence: none | flag: voice-unverified
- voice: EliteTK | position: bare Rust is no worse than Arduino for ESP32-S3 + DPI | date: 2026-02-03 | locator: comment 2026-02-03T10:34:12Z | paraphrase: Arduino users build sophisticated DPI-display devices on ESP32-S3 (mostly with XIP from PSRAM); bare Rust needs methodical alignment with what they do differently | quote: "I don't see why this should be any worse with bare rust" | practiced_evidence: none | flag: voice-unverified
- voice: yanshay | position: esp-hal dpi does not work well under embassy | date: 2026-02-02 | locator: comment 2026-02-02T19:47:24Z | paraphrase: identical code works in sync program; embassy task layout and Timer awaits shift the image; concludes a low-level clock/interrupt interaction | quote: "dpi with esp-hal is doesn't seem to be functional for embassy apps" | practiced_evidence: https://github.com/yanshay/esp32s3-rgb-async (shared 2026-02-03T11:42:07Z; experiment branches) | flag: voice-unverified
- voice: Dominaezzz | position: cause is bus bandwidth, not the async runtime | date: 2026-02-02 | locator: comments 2026-02-02T17:31:48Z, 2026-02-02T20:24:42Z | paraphrase: PSRAM bandwidth starvation; embassy's scheduler executing from flash steals bandwidth from DMA | quote: "I won't be surprised if it's due to the scheduler code executing from flash" | practiced_evidence: none | flag: voice-unverified
- voice: yanshay | position: HAL should expose a public version of the private cache-flush function | date: 2026-02-02 | locator: comment 2026-02-02T16:13:30Z | paraphrase: had to copy a private function definition to flush PSRAM cache; Dominaezzz answered with esp-hal#3982 | quote: "worth making some public version available, it is required" | practiced_evidence: none | flag: voice-unverified
- voice: Dominaezzz | position: removing the discussion area lost knowledge | date: 2026-01-29 | locator: comment 2026-01-29T15:21:38Z; 2026-02-03T11:59:00Z | paraphrase: explanations (incl. one by "Igor" on bus arbitration) lived in a deleted discussion | quote: "a lot of what I'm explaining now used to exist in a discussion but it's all been deleted now" | practiced_evidence: none | flag: voice-unverified
- voice: yanshay | position: removing the discussion area lost knowledge | date: 2026-02-03 | locator: comment 2026-02-03T10:18:50Z (P.S.) | paraphrase: design talk is forced into an ill-fitting issue after the discussion area's removal | quote: "no alternative location for such discussion now with the removal of the discussion area" | practiced_evidence: none | flag: voice-unverified
### Caveats
- Which body removed esp-hal's Discussions, and why, is not stated in the source; the removing side has no Voice here.
- The embassy Question is partly a diagnosis dispute; the practitioner decision it bears on (async executor near timing-critical DMA) is inferred from yanshay's conclusion.
- All Voices show Rust use in-thread (esp-hal code); track records unverified. Dominaezzz's "use the PAC" is an instruction, not a Claim (rule 8).

## f002501 — allow_headers config allways falls back to * (loco-rs/loco#1133) (2025-01-03, en)

### Questions
- Q: When a framework fix lands after a breaking release, should maintainers backport it to the previous minor line or require users to upgrade?
  concepts: semver pre-1.0 minors; backports; upgrade cost of upstream breaking changes (axum 0.8 path syntax); domains_live: web, core; positions_seen: no backport, upgrade recommended; backport branch on old minor requested
### Claims
- voice: kaplanelad | position: no backport to 0.13.x; upgrade | date: 2025-01-10 | locator: comment 2025-01-10T16:08:08Z | paraphrase: points to loco upgrade guide for axum breaking changes; declines applying the CORS fix to 0.13.x | quote: "Unfortunately, I can't apply this fix to version 0.13.x. It's recommended to upgrade" | practiced_evidence: https://github.com/loco-rs/loco (fix PR #1152 merged to master only, per thread) | flag: voice-unverified
- voice: Mettwasser | position: fix should be available on the old minor | date: 2025-01-10 | locator: comment 2025-01-10T15:44:55Z | paraphrase: master has too many breaking changes to compile the app; asks for a branch based on 0.13.2 | quote: "Could you make a branch that is based on `0.13.2`?" | practiced_evidence: none | flag: voice-unverified
### Caveats
- Mettwasser's position is a request with a reason (breaking changes block compiling). Mettwasser later upgraded and reported CORS working (2025-01-10T16:22:14Z).

## f002542 — Bytecode Alliance Election Results (2025-01-14, en)

### Nothing new
Election announcement listing winners and outgoing officers; it states no choice among alternatives and no position on any Rust or Wasm practice.

## f002550 — iroh 0.31.0 - Back At Fighting Fit (2025-01-15, en)

### Questions
- Q: Should test-only behaviour switches be compile-time environment variables or runtime API options gated behind a cargo feature?
  concepts: cargo features (test-utils); compile-time env vars; testability; domains_live: decentralized-iroh, core; positions_seen: runtime option behind test-utils feature (replaced compile-time env var)
- Q: In an async networking server, should connection management go through an actor or through shared data structures with locks?
  concepts: actor pattern; Mutex/locks; deadlock risk; domains_live: decentralized-iroh, distributed; positions_seen: remove actor, use higher-order lock-based structures (with a deadlock follow-up)
- Q: Should a close/shutdown future return a Result or be infallible?
  concepts: API error design; graceful shutdown; domains_live: decentralized-iroh, core; positions_seen: infallible close (replaced Result-returning close)
### Claims
- voice: ramfox, matheus23 (iroh / n0 blog authors) | position: runtime PathSelection::RelayOnly behind test-utils, drop DEV_RELAY_ONLY env var | date: 2025-01-15 | locator: § relay-only mode for testing | paraphrase: compile-time env var dropped; option threaded through the stack when test-utils is enabled; framed as "more programmatically sound" | quote: "The DEV_RELAY_ONLY compile time environment variable has been completely dropped" | practiced_evidence: iroh PR #3056 (cited in post; no URL in bundle text) | flag: voice-unverified
- voice: ramfox, matheus23 | position: remove the actor; use lock-based data structures | date: 2025-01-15 | locator: § Deadlock on the relay (not released) | paraphrase: refactor removed "an unnecessary actor" to cut layers, then needed a follow-up to fix a deadlock | quote: "removing an unnecessary actor and using some higher-order data structures" | practiced_evidence: iroh PR #3099 (cited in post) | flag: voice-unverified
- voice: ramfox, matheus23 | position: infallible close future | date: 2025-01-15 | locator: § Breaking Changes › iroh › changed | paraphrase: Endpoint::close's future no longer returns a Result | quote: "iroh::Endpoint::close's future is now infallible, instead of returning a Result" | practiced_evidence: none | flag: voice-unverified
### Caveats
- The post gives no argument for the infallible close; kept under rule 8 on its named alternative ("instead of returning a Result"). Joint authorship: two handles, one Source, so these count as one Source per Claim, not two independent ones.

## f002584 — Vim Roadmap 2025 (2025-01-22, en)

### Nothing new
The one declared position (Conrad Irwin prefers talking before PRs) is general OSS practice from a Voice whose Rust connection the source text does not show (rule 9); the rest is Vim-emulation planning with no Rust decision.

## f002755 — Introducing Qdrant Cloud's New Enterprise-Ready Vector Search (2025-03-04, en)

### Nothing new
Product announcement of cloud management features (API, RBAC, SSO, API keys, monitoring); it contains no Rust content and no decision stated against an alternative a Rust practitioner makes.

## f002775 — Rust on Cortex-R52 (2025-03-11, en)

### Questions
- Q: Should safety-critical Rust support crates and qualified toolchains be released open source (permissive), or kept proprietary?
  concepts: Ferrocene; qualification (ISO 26262, IEC 61508, IEC 62304); cortex-r-rt; Embedded Devices WG; licensing; domains_live: embedded; positions_seen: open source under permissive licence, donated to the Rust Project's WG
### Claims
- voice: Jonathan Pallant (Ferrous Systems) | position: donate Cortex-R support crates under a permissive open-source licence | date: 2025-03-11 | locator: press-release body, Pallant quote paragraph | paraphrase: libraries and examples (incl. cortex-r-rt, mirroring the Cortex-M set) donated to the Rust Project's Embedded Devices WG; headline frames "Under Open Source License" as the first | quote: "As long-time advocates of open-source development, we are proud to be able to donate this project to the community" | practiced_evidence: none | flag: voice-unverified
### Caveats
- The rejected alternative (proprietary) comes only from the headline's "First … Under Open Source License"; no other vendor is named. Ferrocene's open-source qualification documents are stated without reason or named alternative: practice, not a Claim (rule 8).

## f002827 — Vibe Coding RAG with our MCP server (2025-03-21, en)

### Nothing new
AI-assistant choice (Claude Code for built-in MCP, over Cursor, Copilot, Aider) is declared by a Voice with no Rust connection in the source, for a frontend app plus a Python MCP server; no Rust decision is at stake (rule 9).

## f003044 — Trying `subsecond` and: `Ignoring hotpatch since there is no ASLR reference` (DioxusLabs/dioxus#4195) (2025-05-25, en)

### Questions
- Q: Should dev-time hot-patching require an explicit hook in user code, or should tooling connect implicitly?
  concepts: subsecond; dioxus devtools; binary hot-patching; domains_live: frontend, web, desktop-cli-ui; positions_seen: explicit connect_subsecond() call, no implicit connection
- Q: How wide should a library's dependency version requirements be (e.g. serde `^1` vs a recent minimum)?
  concepts: Cargo version requirements; dependency portability; domains_live: core; positions_seen: loosen to `^1` for portability
- Q: Is binary hot-patching (subsecond / `dx serve --hotpatch`) worth adopting over plain cargo rebuilds for iteration speed?
  concepts: iteration speed; hot reload; incremental compilation; domains_live: web, frontend, desktop-cli-ui; positions_seen: hot-patch for speed (2.7 s vs 13 s)
### Claims
- voice: jkelleyrtp | position: explicit devtools connection, not implicit | date: 2025-05-25 | locator: comment 2025-05-25T12:41:55Z | paraphrase: hotpatch ignored because the client never connected; user must call connect_subsecond() in main | quote: "we don't do this implicitly" | practiced_evidence: https://github.com/DioxusLabs/dioxus | flag: voice-unverified
- voice: pickfire | position: loosen serde requirement to `^1` | date: 2025-05-27 | locator: comment 2025-05-27T17:05:52Z | paraphrase: subsecond's serde requirement blocked adding an axum hello-world example; asks for `^1` for portability with older serde | quote: "Can subsecond have serde being `^1` so that it can be more portable" | practiced_evidence: none | flag: voice-unverified
- voice: frederikhors | position: hot-patching worth it for iteration speed | date: 2025-05-26 | locator: comment 2025-05-26T00:18:05Z | paraphrase: on an ~86k-line Rust project, hot-patch took 2.7 s against 13 s with Cargo | quote: "2.7 seconds instead of 13 seconds with Cargo (night and day for me)" | practiced_evidence: none | flag: voice-unverified
### Caveats
- frederikhors's patches did not take effect in the real project (async fn and multi-crate bugs, per stefnotch). The speed Claim holds a preference, not a working result. pickfire's is a request, with no maintainer answer in the thread.

## f003080 — Redesigned Swift.org is now live (2025-06-04, en)

### Nothing new
Swift community thread; no poster shows a Rust connection, and Rust appears only as a cited tagline and a rejected option, so its arguments are not mapped onto Rust Questions (rule 9).
