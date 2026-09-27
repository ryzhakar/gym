For each source: where do competent Rust practitioners disagree?

## f004596 — Unable to connect to local network after prolonged use (no route to host) (2026-04-21, en)

### Nothing new
nothing new — a Zed bug thread about macOS Local Network privacy (missing `NSLocalNetworkUsageDescription`) and workarounds; no Rust decision is argued.

## f004815 — Transaction Processing in the Data Plane (2026-06-17, en)

### Nothing new
nothing new — Frank McSherry's post designs transaction resolution as recursive SQL views under incremental view maintenance in Materialize, with a Claude-written tuning appendix; the text names no Rust decision and contains no Rust code.

## f004904 — What Is a Live Context Graph? (2026-07-16, en)

### Nothing new
nothing new — a Materialize marketing explainer on read-time versus write-time transformation for agent context; Rust does not appear.

## f004960 — Protect your relays (2026-07-30, en)

### Questions
- Q: Should iroh relays admit any endpoint that knows the relay URL (open), or only endpoints presenting an issued, endpoint-bound token (authenticated)? And should the iroh library itself impose an authentication scheme?
  concepts: iroh relays; NAT traversal fallback; capability tokens; endpoint public keys; access control; domains_live: decentralized-iroh; positions_seen: authenticated by default (managed relays); open relay (pre-June-2026 default, kept for existing deployments); library stays unopinionated, operator builds auth

### Claims
- voice: n0, inc. (Iroh Services), post by Rae McKelvey | position: authenticated by default (managed relays), library unopinionated for self-hosted relays | date: 2026-07-30 | locator: intro ("we've decided that managed relays on Iroh Services are now authenticated by default") and "The problem: a relay URL is a credential you can't revoke" | paraphrase: an open relay's URL ships in every client and leaks, so anyone can spend its finite bandwidth. Managed relays deployed from June 2026 onward require a signed, expiring, endpoint-bound token issued from the project's API key, while earlier relays stay open unless switched. For self-run relays, iroh leaves authentication to the operator | quote: "If the relay accepts anyone, then anyone who learns its URL can push traffic through it." | practiced_evidence: none (the post shows `iroh_services::preset().api_secret_from_env()` usage, not a repo) | flag: voice-unverified (Rust connection in source: iroh Rust API code, `use iroh::Endpoint`)

## f004962 — Product Update: July 2026 (2026-07-31, en)

### Nothing new
nothing new — a Materialize feature list (Kafka source versioning, autoscaling, bounded staleness, MCP OAuth); no Rust decision appears.

## f005693 — onecli/onecli README (2026-03-12, en)

### Nothing new
nothing new — the README says OneCLI "started as a credential vault for AI agents, built in Rust" and lists a Rust gateway. That is declared practice with no Rust decision, reason or rejected alternative (rule 8). The stated pivot is about product scope (single-user to teams), not Rust.

## f007472 — Who Are Active? Human and Non-human Predicates in Generated Query APIs (2026-08-13, en)

### Nothing new
nothing new — the post decides predicate grammar (`whoAreActive` versus `whichAreActive`) in TeaQL's generator for six target languages, with Java as the reference. Rust is only one target, and nothing about the decision is specific to Rust.

## f007659 — Create a Lambda in Rust using Terraform (2023-11-05, en)

### Questions
- Q: Should a Rust AWS Lambda be built with a size-optimized release profile (`opt-level = "z"`, `lto = true`, `codegen-units = 1`, `panic = "abort"`, `strip`) rather than the default release profile, trading compile time and unwinding for binary size and cold start?
  concepts: Cargo profiles; LTO; panic strategy; binary size; cold start; domains_live: cloud-workers; positions_seen: size-optimized profile; default release profile
- Q: Should a Rust Lambda ship as a zipped `provided.al2` bootstrap built by cargo-lambda, or as a container image?
  concepts: cargo-lambda; cross-compilation (zig); container images; deployment packaging; domains_live: cloud-workers; positions_seen: zip via cargo-lambda (default); container image (when needed)
- Q: Should a Rust service handler return a typed, `serde::Serialize` response struct or an untyped `serde_json::Value`?
  concepts: serde; strong typing; JSON; handler signatures; domains_live: cloud-workers; web; core; positions_seen: typed response struct; untyped Value

### Claims
- voice: maahl (maahl.net) | position: size-optimized release profile | date: 2023-11-05 | locator: § "Bonus performance improvements" | paraphrase: adopted a size-optimized release profile on feedback from Reddit user u/HenryQFnord, accepting longer compiles and no unwinding, for a smaller binary; measured 3.6 MB → 1.8 MB and cold start 20 ms → 17 ms, and expects larger gains on bigger programs | quote: "Adding all of these options took us from a 3.6MB binary to a 1.8MB one, which should speed up the cold start of the Lambda." | practiced_evidence: none (the post links a GitHub repo, and the URL is not in the text) | flag: voice-unverified (Rust connection in source: self-reported beginner Rust use, repo with per-section commits)
- voice: maahl (maahl.net) | position: zip via cargo-lambda (default); container image only when needed | date: 2023-11-05 | locator: § "Cargo Lambda" and § "Dockerize the Lambda" | paraphrase: prefers Cargo Lambda for local runs, hot reload and arm64 zip builds, with a container image only "if, for some reason" it is required; reports a multi-stage build shrinking the image from 2.64 GB to 343 MB, and could not combine cargo-chef with cargo-lambda | quote: "The Rust runtime for Lambda is best interacted with using Cargo Lambda." | practiced_evidence: none | flag: voice-unverified
- voice: maahl (maahl.net) | position: typed response struct | date: 2023-11-05 | locator: § "A more structured response" | paraphrase: replaces untyped JSON output with a `Serialize` struct so the compiler validates the response shape | quote: "We can, however, leverage Rust's strong typing to do the work for us." | practiced_evidence: none | flag: voice-unverified

Not logged: choosing arm64 over x86_64 for AWS cost, and building artifacts outside Terraform. Neither is a Rust decision.

## f007703 — Rocket: Web-based Hello World! with tests (2023-12-27, en)

### Nothing new
nothing new — a step-by-step Rocket 0.5 tutorial (dependencies, route, mount, test client) by Gabor Szabo that gives instructions only; no decision is stated with a reason or against an alternative (rule 8).
