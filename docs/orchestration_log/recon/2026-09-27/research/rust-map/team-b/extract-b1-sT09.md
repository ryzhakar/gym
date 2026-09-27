For each source: what must a Rust practitioner decide, and where do the sources conflict on it?

Team b, batch 1, third pass, slice T09. Rules 1–8 of t2-extract.md and the lead's clarifications (declarations only; Voice bar holds) applied.

## f004905 — SE-0538: Disconnected (2026-07-17, en)

Read: all 34 posts (bundle count matches Discourse `posts_count` 34).

### Nothing new
The review is about naming a Swift concurrency type and its methods (Disconnected / Sending / Sent, take / consume, swap / exchange). It is argued by Swift Forums handles, and the source shows none of them with a public Rust track record. Rust appears only as analogy: "reads somewhat like a Rust lifetime error" (@aviva), "it appears Rust has a \"replace\"" (@jamieQ), "Rust's Cell" (@nkbelov). None of it is a Rust practitioner's decision.

## f005201 — lapce/lapce README (2023-12-28, en)

### Nothing new
The README lists Lapce's stack and features: pure Rust, Floem UI, xi-editor rope, wgpu, WASI plugins. It gives no reason for any choice and names no rejected alternative, so under rule 8 this is practice, not a declared Position.

## f005312 — dani-garcia/vaultwarden README (2024-08-14, en)

### Questions
- Q: Should a Rust web service terminate TLS itself through its framework or a TLS crate, or sit behind a reverse proxy that terminates TLS?
  concepts: Rocket built-in TLS; reverse proxy; deployment; domains_live: web; cloud-workers; positions_seen: reverse proxy in front, framework TLS unused

### Claims
- voice: Vaultwarden maintainers (dani-garcia/vaultwarden) | position: reverse proxy over the framework's built-in TLS | date: 2024-08-14 (frame date; the README revision read is undated and current) | locator: README § Usage, paragraph "While Vaultwarden is based upon the Rocket web framework…" | paraphrase: Rocket supports TLS, but the maintainers recommend setting up a reverse proxy instead and link to proxy examples. The README also requires HTTPS for the web vault. | quote: "While Vaultwarden is based upon the Rocket web framework which has built-in support for TLS our recommendation would be that you setup a reverse proxy" | flag: voice-unverified | practiced_evidence: https://github.com/dani-garcia/vaultwarden (container images publish on port 80, compose example binds 127.0.0.1:8000:80)

Note: the README gives no explicit reason. It qualifies under rule 8 only because it names the alternative (built-in TLS).

## f005314 — spring-rs/spring-rs README (now summer-rs) (2024-08-17, en)

### Questions
- Q: Should a Rust backend be built on an opinionated convention-over-configuration framework with a component/plugin registry and dependency-injection-style extractors (Spring Boot style), or by composing libraries such as axum and sqlx directly?
  concepts: convention over configuration; plugin system; component registry; procedural macros (`#[component]`, `#[auto_config]`); axum; sqlx; toml configuration; domains_live: web; distributed; positions_seen: convention-over-configuration framework (summer-rs)

### Claims
- voice: summer-rs project (github.com/spring-rs/spring-rs, README now titled summer-rs; no individual maintainer named in the source) | position: convention-over-configuration application framework wrapping axum, sqlx and others as plugins | date: 2024-08-17 (frame date; the README revision read is undated, describes crate `summer` 0.4) | locator: README intro paragraph, § Features, § component macros | paraphrase: the framework puts convention over configuration, following Spring Boot, and offers an extensible plugin system over Rust crates. It claims ease of use through a concise API and optional procedural macros. The `#[component]` macro removes the need to implement the Plugin trait by hand. | quote: "summer-rs is an application framework that emphasizes convention over configuration, inspired by Java's SpringBoot" | flag: voice-unverified | practiced_evidence: https://github.com/spring-rs/spring-rs (crates summer, summer-web, summer-sqlx …)

Note for the verifier: the source shows no crates.io dependents count; it gives only a reverse-dependencies link. The Voice bar is unverified.

## f005440 — Rust memory management explained (2025-02-12, en)

### Questions
- Q: When should a Rust program reach for shared ownership (Rc/Arc) or runtime-checked borrowing (RefCell) instead of restructuring for single ownership and compile-time borrows?
  concepts: ownership; Box; Rc; Arc; RefCell; borrow checker; domains_live: core; positions_seen: Rc/Arc when reader count is hard to know, RefCell only for a narrow set of runtime-only problems

### Claims
- voice: Serdar Yegulalp (InfoWorld senior writer) | position: use Rc/Arc when program structure makes reader count hard to tell; keep RefCell to a narrow range of runtime-only problems | date: 2025-02-12 | locator: § Automatic memory management and Rust types, paragraphs 3–4 | paraphrase: Rc and Arc are recommended when it is hard to tell how many readers a piece of data will have. RefCell moves the borrow rules to run time, works only in single-threaded code and panics on violation. Hence it fits only a narrow range of problems. | quote: "Do use them when the structure of a program makes it hard to tell how many readers will exist for a given piece of data." | flag: voice-unverified | practiced_evidence: none

Caveats for the verifier: (1) The Voice bar rests on "widely read post". The source shows a technology journalist who covers Rust among other languages and shows no Rust code of his own. (2) The article contains technical errors that bear on its authority. It says Rc/Arc make "the object can only be read-only". Several of its "compiling" examples would not compile, e.g. `data = 3` for a `Box<i32>` and `c = 32` for a `Box<i64>`.

## f005504 — HelixDB/helix-db README (2025-05-13, en)

### Nothing new
The README is product and SDK documentation: install commands, query DSL examples in four languages, and the cloud offering. "No build or deploy step" for queries names no alternative, and no Rust practitioner's decision is stated with a reason.

## f005802 — Andreas Thom on Mathstodon, reply to tristanbuckmaster (2026-09-09, en)

### Nothing new
The thread is about whether mathematicians can trust OpenAI with unpublished work. It contains no Rust content at all.

## f007125 — Rust HashMap notes, Graham King (2025-03-30, en)

### Nothing new
These are research notes on how std's hashbrown/SwissTable HashMap works: layout, probing, growth. The comparison with chaining tables describes std's design and is not something a practitioner chooses. The default SipHash hasher is described, not argued for or against.

## f008692 — The Embedded Rustacean Issue #58 (2025-11-07, en)

### Nothing new
The issue is a curated link roundup: news, tutorials, crate releases, events and jobs. It declares no decision beyond the newsletter's general belief in Rust for embedded, which names no alternative inside Rust practice.

## f009654 — crates.io security incident: improperly stored session cookies (2025-04-11, en)

### Nothing new
The incident report (Adam Harvey for the crates.io team) says cookie values reached Sentry, all cookies are now redacted and all sessions are invalidated. Its one reasoned decision, invalidating sessions "out of an abundance of caution", is incident response, not a decision Rust practitioners make differently.

## f011688 — Writing Cronjobs in Rust (2024-01-23, en)

### Questions
- Q: Should scheduled or background jobs in a Rust service run on a durable, database-backed job queue (e.g. apalis with Postgres storage) or on an in-process scheduler whose jobs live only in memory?
  concepts: apalis; PostgresStorage; cron; tower service layers; retry; domains_live: web; cloud-workers; positions_seen: durable Postgres-backed queue
- Q: Should a Rust service's infrastructure (e.g. its database) be provisioned from annotations in the Rust code itself (infrastructure-from-code, Shuttle), or by separate Docker or IaC tooling such as Terraform?
  concepts: shuttle_runtime; shuttle_shared_db; infrastructure from code; Docker; Terraform; domains_live: cloud-workers; web; positions_seen: provision from code annotations

### Claims
- voice: Joshua Mo (Shuttle) | position: durable Postgres-backed job queue | date: 2024-01-23 | locator: § Hooking it all up, paragraph 1 | paraphrase: PostgresStorage is set up so the job queue is durable, with the reason that jobs would otherwise be lost when the service has an outage | quote: "Without durable job queues, our jobs would disappear if our web service has any outages!" | flag: voice-unverified | practiced_evidence: shuttle-hq/shuttle-examples subfolder shuttle-cron (named in source, not opened)
- voice: Joshua Mo (Shuttle) | position: provision infrastructure from code annotations over Docker or Terraform | date: 2024-01-23 | locator: § Adding a database, paragraph after the first code block | paraphrase: the `#[shuttle_shared_db::Postgres]` annotation is presented as "pretty simple" next to running Docker locally and managing Postgres by hand or with Terraform in production | quote: "In production, you would also need to manually instantiate and manage your Postgres instance or rely on an IaC (infrastructure as code) tool like Terraform." | flag: voice-unverified | practiced_evidence: none (vendor tutorial; Shuttle is the author's employer's product)

Note for the verifier: this is a vendor tutorial. Both Positions promote the vendor's product (Shuttle) and its example stack.
