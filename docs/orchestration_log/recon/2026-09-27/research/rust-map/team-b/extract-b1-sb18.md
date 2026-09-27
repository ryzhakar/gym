## f005169 — Callgraph analysis (2026-04-08, en)
### Nothing new
`nothing new` — a single-author (Jynn, Ferrous Systems) technical blog surveying approaches to verifying "this function never calls that function" (clippy lints, effect systems, linker tricks, cfg forks, a custom rustc driver) and explaining Ferrocene's own callgraph-analysis lint; no second voice or contested point.

## f005201 — Lapce (2023-12-28, en)
### Nothing new
`nothing new` — a project README (features, installation, contributing); no contested point.

## f005307 — Async Rust Challenges in Iroh (2024-08-01, en)
### Questions
- Q: When your chosen async I/O library (e.g. quinn for QUIC) is paired with a storage/database layer that only offers a synchronous API (as with embedded databases like redb, rocksdb, sled, sqlite), should you treat that combination as an avoidable architecture mismatch to design around from the outset — including avoiding constructs like `LocalSet` and `!Send` futures — or accept it as a practical necessity, since no viable async-native alternative exists and non-`Send` futures are often unavoidable when wrapping such resources?
  concepts: async runtimes, sync/blocking I/O, embedded storage engines, Send bounds, LocalSet; domains_live: distributed;decentralized-iroh; positions_seen: incompatible-deps-should-be-avoided, sync-storage-is-unavoidable-given-available-options
- Q: Is it acceptable practice to run blocking synchronous I/O (e.g. database calls) inside a dedicated single-threaded ("current_thread") Tokio runtime on its own OS thread, or does limiting a Tokio runtime to a single thread carry negative internal ramifications that make this an anti-pattern except when no other OS threads are available?
  concepts: async runtimes, current_thread/single-threaded executors, blocking I/O bridging; domains_live: distributed;decentralized-iroh; positions_seen: single-threaded-runtime-fine-for-n1-scheduling
### Claims
- voice: withoutboats | position: incompatible-deps-should-be-avoided | date: 2024-08-02 | locator: lobste.rs/s/7rtvnp, comment 2024-08-02T06:30:40-05:00 | paraphrase: argues iroh's choice of quinn (async QUIC) together with redb (blocking storage) creates the impedance mismatch that is the source of many of their described problems, and separately that `LocalSet` and `FuturesUnordered` should generally be avoided | quote: "I would have regarded quinn and redb as incompatible dependencies because of this mismatch and looked for a different solution." | practiced_evidence: none
- voice: rklaehn | position: sync-storage-is-unavoidable-given-available-options | date: 2024-08-06 | locator: lobste.rs/s/7rtvnp, comment 2024-08-06T06:41:54-05:00 | paraphrase: as the blog post's author and an iroh maintainer, responds "what is the alternative?" — every in-process database they evaluated (rocksdb, redb, sled, sqlite) has a synchronous API, so the mismatch isn't a foreseeable design error, and non-`Send` futures are often unavoidable when a future must capture a non-`Send` database/transaction handle | quote: "What is the alternative? ... They *all* have a sync api." | practiced_evidence: https://github.com/n0-computer/iroh (redb usage); https://github.com/n0-computer/beetle (prior rocksdb use)
- voice: withoutboats | position: single-threaded-runtime-fine-for-n1-scheduling | date: 2024-08-02 | locator: lobste.rs/s/7rtvnp, comment 2024-08-02T08:03:38-05:00 | paraphrase: responding to kbknapp's report that Jon Gjengset warned against using Tokio's single-threaded runtime except when no OS threads are available, states this warning is wrong: if you want N:1 scheduling of async tasks, the single-threaded runtime is the right tool, though combining it with blocking syscalls on that thread is unusual | quote: "I believe that Jon Gjengset is wrong about this. If you want to N:1 scheduling of async tasks (instead of M:N), using the single threaded runtime is the right choice." | practiced_evidence: none

## f005312 — Vaultwarden (2024-08-14, en)
### Nothing new
`nothing new` — a project README (features, deployment, disclaimer); no contested point.

## f005314 — spring-rs / summer-rs (2024-08-17, en)
### Nothing new
`nothing new` — a project README (a Spring-Boot-inspired Rust web framework, plugin catalog, code examples); no contested point.

## f005332 — Rust in Linux lead retires rather than deal with more "nontechnical nonsense" (2024-09-04, en)
### Questions
- Q: When a C-subsystem maintainer changes their C code in a way that breaks the corresponding Rust abstraction/bindings, should the C maintainer be expected to help keep the Rust side correct (or at least not block small Rust-motivated robustness fixes to the C code), or is it legitimate for C maintainers to fix only their own C code and decline responsibility for Rust bindings entirely?
  concepts: governance, Rust-for-Linux, cross-language maintenance boundaries, memory safety, kernel culture; domains_live: core;embedded; positions_seen: c-maintainers-not-obligated-to-rust, rust-needs-c-maintainer-cooperation, adoption-slow-for-practical-reasons
### Claims
- voice: Ted Ts'o | position: c-maintainers-not-obligated-to-rust | date: undated (conference talk clip, reported in the 2024-09-04 article) | locator: arstechnica.com article, quoting an off-camera interjection during a Linux conference talk, identified by Wedson Almeida Filho in a Register interview | paraphrase: interjects during a talk (about Filho's request that a filesystem gain Rust bindings) that while he will fix his own C code, he will not fix Rust bindings that break as a result, and won't be forced to learn Rust | quote: "Here's the thing: you're not going to force all of us to learn Rust." | practiced_evidence: none
- voice: Wedson Almeida Filho | position: rust-needs-c-maintainer-cooperation | date: 2024-08 (week before the 2024-09-04 article) | locator: arstechnica.com article, quoting his Linux kernel mailing list resignation post | paraphrase: resigns as Rust-for-Linux maintainer after almost 4 years, citing exhaustion with "nontechnical nonsense" rather than technical disagreement, and states the future of kernels is with memory-safe languages | quote: "After almost 4 years, I find myself lacking the energy and enthusiasm I once had to respond to some of the nontechnical nonsense, so it's best to leave it up to those who still have it in them." | practiced_evidence: none
- voice: Asahi Lina | position: rust-needs-c-maintainer-cooperation | date: late August 2024 (Mastodon post, per the article) | locator: arstechnica.com article, quoting her Mastodon post | paraphrase: says she "regretfully completely understands" Filho's frustration, describes being blocked by a C maintainer from pushing small robustness/lifetime fixes to the DRM scheduler's C code, and that every kernel panic in her Apple GPU driver traces to bugs in that C code, not her Rust code | quote: "But I get the feeling that some Linux kernel maintainers just don't care about future code quality, or about stability or security any more. They just want to keep their C code and wish us Rust folks would go away." | practiced_evidence: https://github.com/AsahiLinux (Apple GPU driver, written in Rust)
- voice: Linus Torvalds | position: adoption-slow-for-practical-reasons | date: August 2024 (public appearance, per the article) | locator: arstechnica.com article, quoting his remarks at a public appearance | paraphrase: agrees there has been pushback on Rust, attributing it to old-time C kernel developers being unfamiliar with and unenthusiastic about learning a new, quite different language, plus instability in the Rust kernel infrastructure itself, rather than to bad faith | quote: "I was expecting [Rust] updates to be faster, but part of the problem is that old-time kernel developers are used to C and don't know Rust. They're not exactly excited about having to learn a new language that is, in some respects, very different. So there's been some pushback on Rust." | practiced_evidence: none

## f005421 — Rhai (2025-01-17, en)
### Nothing new
`nothing new` — a project README for an embedded scripting language; no contested point.

## f005440 — Rust memory management explained (2025-02-12, en)
### Nothing new
`nothing new` — a single-author tutorial (Serdar Yegulalp) walking through scope, ownership, `Box`, `Rc`/`Arc`, and `RefCell`; explanatory, not framed around any disagreement.

## f005504 — HelixDB (2025-05-13, en)
### Nothing new
`nothing new` — a project README (graph-vector database, SDK setup across four languages, cloud deployment); no contested point.

## f005600 — Futurelock (2025-10-31, en)
### Questions
- Q: In concurrent Rust systems, should hand-written locks (`Mutex`) be avoided in favor of atomics/compare-and-swap-based (lock-free) data structures — on the reasoning that a stuck lock is "always a disaster" while livelock from atomics is rarer and usually self-recovers — or is this framing misleading, since atomics/CAS carry their own correctness burden (reasoning about stale vs. current data) that is just as real a bug class as the deadlocks they avoid?
  concepts: concurrency, locks, atomics, compare-and-swap, deadlock, livelock; domains_live: core;distributed; positions_seen: avoid-locks-prefer-atomics-cas, race-conditions-are-also-a-real-problem
### Claims
- voice: bsder | position: avoid-locks-prefer-atomics-cas | date: 2025-11-01 | locator: lobste.rs/s/fzro7f, comment 2025-11-01T01:54:49-05:00 | paraphrase: argues atomics and compare-and-swap are fine — worst case you get livelock, which is rare and usually recovers — while locks are "always a disaster waiting to happen" because something will die holding one and the whole system grinds to a halt; goes as far as saying a lock's mere existence, even inside a library, is always a programming bug | quote: "In fact, I would argue that the existence of a \"lock\" is *always* a programming bug even inside a library." | practiced_evidence: none
- voice: inactive-user | position: race-conditions-are-also-a-real-problem | date: 2025-11-01 | locator: lobste.rs/s/fzro7f, comment 2025-11-01T02:14:18-05:00 (context: also 2025-10-31T23:05:36-05:00, arguing neither locks nor hand-rolled atomics belong in ordinary application code — stick to a well-tested concurrency library) | paraphrase: pushes back that framing atomics/CAS as the safe alternative glosses over the fact that races (stale/inconsistent reads) are themselves a real bug class, not a lesser evil | quote: "You say that like race conditions (with atomics) are not a bad thing" | practiced_evidence: none

## f005668 — Swift is a more convenient Rust (2026-01-31, en)
### Nothing new
`nothing new` — a single-author comparative essay (Rust's "bottom-up" ownership vs. Swift's "top-down" copy-on-write defaults, syntax comparisons, cross-platform Swift); states many of the author's own positions on Rust/Swift tradeoffs, but no second voice engages or contests them in this source.
