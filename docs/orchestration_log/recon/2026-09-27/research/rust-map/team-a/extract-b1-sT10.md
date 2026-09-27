For each source: where do competent Rust practitioners disagree?

## f004205 — ~Escapable, Span, Ownership Annotations, etc (2026-02-04, en)

### Questions
- Q: Does most safe Rust need first-class, escapable references with lifetime annotations (`fn foo(x: T) -> &U`)? Or would scoped access, a closure taking the borrow (`fn foo<R>(x: T, action: impl FnOnce(&U) -> R) -> R`) or a yielding projection, cover nearly every use case, leaving the rest to localized unsafe?
  concepts: references; lifetimes; borrow checker; continuation-passing / closure-scoped access; HashMap::entry; language complexity; domains_live: core; positions_seen: first-class references needed (the source attributes this to "many in the Rust community", no named Voice); scoped access suffices

### Claims
- voice: Alvae | position: scoped access suffices | date: 2026-02-06 | locator: post @Alvae 2026-02-06T04:32:56Z, paragraphs 2–4 and the HashMap::entry paragraph; supporting post @Alvae 2026-02-06T10:16:22Z, last paragraph | paraphrase: rewriting a reference-returning Rust function as one that passes the borrow to a closure avoids escaping references in the vast majority of cases she has met in practice. The entry pattern, which many in the Rust community cite to justify first-class references, is expressible without them. In Rust, lifetime annotations cannot be ignored even by code that never uses references, because they surface in diagnostics | quote: "This transformation is sufficient to avoid the kind of escaping references that Rust offers in the vast majority of cases I have encountered in practice." | practiced_evidence: none | flag: voice-unverified (Rust connection in source: writes the Rust transformation and reports practice with such cases; also speaks for Hylo, "we're betting that Hylo does not need Rust-like references")

Not logged under rules 8–9:
- @dabrahams 2026-02-05T22:05:48Z makes the strongest statements on Rust: "the way lifetime annotations creep into the type system via generics is among the worst complexity effects they've had on Rust". He also says there is "a small corner of problems that Rust can solve safely, but only at a huge cost in language complexity". The source shows no Rust use, crate or role; he mentions only conversations "with Rust folks".
- @Dmitriy_Ignatyev 2026-02-05T08:36:01Z compares Swift with Rust from "what I understand" and says "I’m not deeply experienced with Rust". No Rust use is shown, and his side concerns Swift's design.
- All other posts argue Swift or Hylo design.

## f004229 — Seamless TiDB Cloud Upgrades: Replicating Production Workloads with Traffic Replay (2026-01-27, en)

### Nothing new
nothing new — a product post on TiDB Cloud's traffic-replay upgrade testing; it names no Rust decision, no Rust code and no Rust Voice (frame date 2026-02-09; page byline Ming Zhang, 2026-01-27).

## f004369 — Ctrl-C in psql gives me the heebie-jeebies (2026-03-05, en)

### Nothing new
nothing new — the post covers Postgres CancelRequest security (plaintext cancel, 4-byte keys, protocol 3.2) and the author's Ruby proxy Elephantshark; Rust does not appear.

## f004378 — TiDB Community Quarterly Roundup: Q4 2025 Discussion Topics (2026-03-06, en)

### Nothing new
nothing new — a community-manager roundup of TiDB migration, pricing and feature-gap questions; no Rust decision, code or Voice appears.

## f004414 — Building a Voice-First AI Journal: What I Learned About AI Memory, Vector Search, and TiDB (2026-03-11, en)

### Nothing new
nothing new — the decisions it declares (drop Mem0, per-exchange embeddings, TiDB over Postgres + Pinecone, Claude Haiku for synthesis) concern a JavaScript/web AI app, not Rust (frame date 2026-03-13; page byline Chris Dabatos, 2026-03-11).

## f004555 — Introducing Zed's Agent Metrics (2026-04-09, en)

### Nothing new
nothing new — the post publishes AI-agent usage and latency telemetry inside Zed; it states no decision about Rust or Rust practice.

## f004562 — Git repo not recognized in a project (2026-04-11, en)

### Nothing new
nothing new — a Zed bug report and triage thread about the git panel and git binary selection; Rust appears only as `crates/...rs` paths in logs, with no contested point.

## f004581 — Agents Week: network performance update (2026-04-17, en)

### Nothing new
nothing new — the post reports Cloudflare's network-latency rankings and attributes the gains to new locations and connection-handling software. It is tagged "Rust", but its text names no Rust decision or Rust code.
