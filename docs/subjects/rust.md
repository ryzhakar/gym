# Rust

Owner rulings of 2026-09-25 (doc/SPEC.md, archived at docs/orchestration_log/archive/SPEC.md), separated from the map's architecture on the owner's ruling of 2026-09-26; entered 2026-09-26. Later rulings are marked where they stand.

## Scope

- **Questions:** all of Rust, culture included. Governance and community disputes count, for example norms about AI-written contributions.
- **Depth and breadth** stay the owner's call, and the owner's interest in Rust is high (owner ruling 2026-09-26).
- **Closing the Question set** is settled when Rust's research starts (owner ruling 2026-09-26; `docs/user_deferred_items.md`).
- **Domains of particular interest:** the target domains in `docs/ground-truth.md`.

## The Language in Rust

- **Question**, for example: should a library ever panic?
- **Concepts** include ownership, lifetimes, async runtimes, macros, unsafe.
- **Domains** include CLI, web, embedded, Wasm.
- **Sources** include RFCs and crates; tells include `Cargo.toml` signatures.
- **Candidate Question:** AI-assisted Rust, in its own right, since norms about machine-written work are contested (see Findings).

## Findings

Preliminary research found five things about Rust; each grounds a rule in `docs/opinion-map.md` § Design rules and where they come from.

| Finding | Source |
| --- | --- |
| Voices change Positions. No Boilerplate's older scripts (up to video 43) recommend tokio; video 48 argues for synchronous Rust, threads and rayon | [async script](https://www.namtao.com/async-isn-t-real-and-can-t-hurt-you/), [script index](https://www.namtao.com/nb/) |
| Loud is not common. No Boilerplate runs nightly by default; the 2025 State of Rust survey found most people on stable, with nightly use declining | [toolkit](https://www.namtao.com/rust-toolkit-2026/), [survey](https://blog.rust-lang.org/2026/03/02/2025-State-Of-Rust-Survey-results) |
| Questions are domain-local. Async is optional in a CLI but native to iroh 1.0 and to WASI 0.3 components, both released June 2026 | [iroh 1.0](https://iroh.computer/blog/the-road-to-iroh-1-0), [WASI 0.3](https://wasi.dev/releases/wasi-p3) |
| Existing curation records conclusions, not disagreements: crate lists and idiom lists state answers without the debate | [idiomatic-rust](https://github.com/mre/idiomatic-rust) |
| Norms about machine-written work are contested. The Rust project retracted an LLM-drafted blog post in March 2026 | [retraction note](https://blog.rust-lang.org/2026/03/20/rust-challenges) |

## Practice data

The community survey is the annual State of Rust survey. The package registry is crates.io: downloads, and how many crates depend on a given crate.

## Influence evidence

Crates maintained and how many projects depend on them; reach of books, courses or channels; roles in the Rust project or at major adopters.
