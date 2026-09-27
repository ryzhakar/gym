# Extract — batch 1, send-back, team a

Framing: for each source, where do competent Rust practitioners disagree?

## f004815 — https://materialize.com/blog/transaction-processing-in-the-data-plane (2026-06-17, domain-subframes)

Nothing new — no Rust-relevant content. Long technical post by Frank McSherry (Materialize Chief Scientist; creator of timely-dataflow/differential-dataflow, both real Rust crates with dependents — qualifies as a Voice), plus a Claude-authored appendix. Entirely SQL/database-internals content (`WITH MUTUALLY RECURSIVE`, query planning, optimistic concurrency control): no Rust language or practice discussion anywhere in the piece.

## f004865 — https://iroh.computer/blog/an-iroh-powered-smart-fan (2026-07-02, domain-subframes)

Voice: Rüdiger Klaehn (iroh maintainer, n0 inc — maintains a crate with real dependents).

### Question — Cargo project layout when combining a host crate and an embedded/different-toolchain crate
- Position (Klaehn, separate-projects): keep host and embedded (cross-compiled) code in fully separate, non-workspace Cargo projects when toolchains differ and a patched dependency is needed for one side only.
- Claim: "Note that we need different toolchains and want to keep the option to use a patch of iroh for the ESP32 variant, so the two directories are completely separate Rust projects. We do not use a workspace." — locator: "Basic setup" section. Domain: embedded.

### Question — how much review AI-written code needs before shipping it, for code outside the author's own expertise
- Position (Klaehn, light-touch-for-peripheral-code): acceptable to let an LLM write a whole peripheral component (a JS/WASM GUI) you lack expertise in, and ship it after only a brief check, rather than deep review — ties to the AI-assisted-Rust candidate Question already flagged in rust.md § Findings.
- Claim: "I am not a javascript developer, so the WASM GUI is vibe coded. I just briefly checked it." — locator: "A proper GUI" section. Domain: web/embedded (WASM GUI for an embedded device).

## f004904 — https://materialize.com/blog/what-is-a-live-context-graph (2026-07-16, domain-subframes)

Nothing new — no Rust content. Product/marketing post by Michelle Gienow (journalist-turned-developer, no established Rust track record) about a general "live context graph" architecture pattern for AI agents. No Rust language or practice discussed.

## f004960 — https://iroh.computer/blog/authenticated-relays (2026-07-30, domain-subframes)

Nothing new — no contested Rust Question. Product-feature post by Rae McKelvey (n0/iroh) describing iroh's new capability-token relay authentication. Rust code shown (`Endpoint::bind`, `#[tokio::main]`) is illustrative of the product's own API, not an argued Position on a live Rust practitioner disagreement.

## f004962 — https://materialize.com/blog/2026-07-product-update (2026-07-31, domain-subframes)

Nothing new — no Rust content, no named Voice. Pure product changelog (Kafka source versioning, autoscaling, MCP OAuth).

## f005287 — https://mastodon.social/@kornel/112626463128422583 (2024-06-16, hn-lobsters)

Voice: Kornel (kornelski — lib.rs maintainer, multiple crates.io crates with real dependents; qualifies as Voice).

### Question — should crates.io-published bytes be checked against their source repository, and should such findings be released even incomplete
- Position (Kornel, verify-and-publish-raw): built a comparator between crates.io tarballs and their git repos across nearly all of crates.io, and released the raw dataset rather than withholding it for private review first.
- Claim: "I've compared nearly all Rust crates.io crates to contents of their git repositories. Here's a dump of this data... I'm releasing the data, because I don't have time to review it all." — locator: original post + reply to `@guenther`, 2024-06-16. Domain: core (package ecosystem/supply chain).

## f005693 — https://github.com/onecli/onecli (2026-03-12, hn-lobsters)

Nothing new — no argued Position. README names Rust for one component ("Rust Gateway": MITM credential-injecting proxy) in an otherwise polyglot (TypeScript/Next.js, Postgres) system, but states this as a bare architecture fact with no stated rationale and no engagement with any Rust-practitioner disagreement.

## f005702 — https://sycamore.dev (2026-04-01, hn-lobsters)

Voice: the Sycamore project (institution/builder type; real crate, 303k crates.io downloads, 73 contributors — qualifies as Voice).

### Question — should a Rust web UI framework use fine-grained (signal-based) reactivity or virtual-DOM diffing
- Position (Sycamore, fine-grained-reactivity): fine-grained reactivity is the right model, contrasted implicitly with vdom-diffing frameworks (e.g. Yew).
- Claim: "Sycamore's reactivity system is fine-grained, meaning that only the parts of your app that need to be updated will be." — locator: front page, "Fine-Grained Reactivity" feature blurb. Domain: web/frontend.

## f007341 — https://forgestream.idverse.com/blog/20260313-rust-export (2026-02-09, individual-blogs)

Voice: Oliver Moss (IDVerse engineer, ships Rust in production per bio — qualifies as Voice).

### Question — how much defensive engineering (RAII/type-level guards) is warranted against a failure mode judged unlikely to occur in practice
- Position (Moss, guard-even-theoretical-leaks): worth adding an RAII (`Drop`-based) guard for a resource-leak path he judges may never actually occur, over leaving it unhandled — appeals to Value: correctness over minimal/pragmatic effort.
- Claim: "this is a problem in theory and may not ever occur in practice, but I figured it would be best to guard for this using some good old-fashioned RAII." — locator: "Polish" section. Domain: web (Rust/WASM frontend).

## f007472 — https://teaql.io/blog/human-nonhuman-query-predicates (2026-08-13, individual-blogs)

Nothing new — not Rust-specific. TeaQL's own code-generator naming convention (`whoAreActive` vs `whichAreActive`), applied identically across six target languages (Java, Rust, Go, Python, .NET, TypeScript); no Rust-particular practice or disagreement, just one vendor's cross-language API-generation style tagged with "rust" among other language tags.

## f007659 — https://maahl.net/blog/rust-aws-lambda (2023-11-29, individual-blogs;twir-links)

Nothing new — no qualifying Voice. Author states "I am very much a beginner in Rust" and the post is an individual, unattributed-readership tutorial; no crate maintenance, production Rust use beyond this toy project, project/foundation role, or established book/course/talk is claimed. The one external voice quoted (a Hashicorp org member) speaks only about Terraform, not Rust.

## f007703 — https://rust.code-maven.com/rocket-hello-world (2023-12-27, individual-blogs;twir-links)

Nothing new — no contested Question. Voice qualifies (Gabor Szabo, Rust Maven — maintains OSS Rust projects, teaches Rust courses), but the post is a neutral "hello world" Rocket-framework tutorial with no argued Position or disagreement (e.g. no stance versus Actix-web/Axum).
