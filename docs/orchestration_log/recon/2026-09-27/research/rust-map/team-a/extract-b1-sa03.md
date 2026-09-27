Framing: For each source, where do competent Rust practitioners disagree?

Source: RECON/samples/bundles/b1-team-a-03.txt (already fetched; read from bundle, not re-fetched). Note on dates: gh-api-thread caches in this bundle strip per-comment usernames/timestamps, keeping only the source's own date and explicit `@mentions`; where a Claim's voice is not self-signed, named in the frame register as the source's author, or unambiguously named by a reply addressing them, no Claim is written — only a `positions_seen` label — and the Claim date used is the source's own date, not an individual comment timestamp.

## f002226 — SE-0451: Raw identifiers (2024-10-24, en)
### Nothing new
`nothing new` — full 749-line Swift Evolution review thread read (raw-identifier syntax, leading digits, natural-language test names); Rust is cited twice as prior art (its rejection of certain zero-width combining characters as identifier starts, and its built-in confusable-identifier lint) by Swift language designers arguing their own proposal, not as a claim by a Rust practitioner; out of subject for the Rust map.

## f002236 — Elephants in tunnels: how Hyperdrive connects to databases inside your VPC networks (2024-10-25, en)
### Questions
- Q: For a custom async I/O transport abstraction in Rust that must work across several carriers (raw TCP, TLS, WebSocket-wrapped tunnel), should the abstraction be built against the tokio-style `AsyncRead`/`AsyncWrite` traits, or against the `Sink`/`Stream` traits that most existing async WebSocket libraries expose?
  concepts: `AsyncRead`/`AsyncWrite` vs. `Sink`/`Stream` traits, `Send`/`Sync`/`Unpin` bounds, generic transport abstraction, tokio ecosystem; domains_live: cloud-workers; positions_seen: Cloudflare (Hyperdrive team) — standardize the whole handler on `AsyncRead`/`AsyncWrite` and write a custom WebSocket-to-`AsyncRead`/`AsyncWrite` translation layer; existing OSS WebSocket-over-async libraries (unnamed) — built on the `Sink`/`Stream` paradigm instead
### Claims
- voice: Cloudflare (Hyperdrive team) | position: build the transport abstraction against `AsyncRead`/`AsyncWrite`, not `Sink`/`Stream` | date: 2024-10-25 | locator: article body, "The way we accomplish this..." section | paraphrase: States that available OSS WebSocket-over-async libraries built on `Sink`/`Stream` did not jointly satisfy `Send`, `Sync`, `Unpin` together with `AsyncRead`/`AsyncWrite`, so Hyperdrive wrote its own translation layer to keep its entire custom Postgres handler generic over `AsyncRead`/`AsyncWrite` streams instead. | quote: "The primary reason is that Hyperdrive operates across multiple threads (thanks to the tokio runtime), and so we rely on our connections to also handle Send, Sync, and Unpin. None of the available solutions had all five traits handled." | practiced_evidence: Hyperdrive itself (Cloudflare's own production system implementing this)

## f002243 — Feat/2361 segmentation mask (2024-10-26, en)
### Questions
- Q: Should a machine-learning dataset abstraction that loads segmentation masks/images eagerly materialize every item into memory (e.g. building an `InMemoryDataset`), or support lazy/streaming access, given that images or datasets can be large?
  concepts: dataset/iterator abstractions, eager vs. lazy materialization, memory footprint; domains_live: ml; positions_seen: anthonytorlucci (PR author) and laggui (maintainer, referenced) — jointly flag the current eager `InMemoryDataset` materialization as a likely problem for large images/datasets, with no resolution yet proposed in this source
### Claims
- voice: anthonytorlucci | position: current eager in-memory materialization is inadequate for large datasets, unresolved | date: 2024-10-26 | locator: PR review comment | paraphrase: Notes that `new_segmentation_with_items` ultimately calls `with_items`, which builds an `InMemoryDataset`, and that maintainer laggui had already flagged this as potentially problematic for large images or large datasets, without yet knowing the fix. | quote: "As @laggui pointed out, this could be problematic for large images or large datasets. I'm not sure what the solution is here." | practiced_evidence: tracel-ai/burn#2426 (own PR containing the flagged design)

## f002271 — Support query parameters in routes (2024-11-03, en)
### Nothing new
`nothing new` — implementation/bug-fix thread (query-parameter routing, a reload bug, a client-side-navigation ordering bug) with a passing, uncontested suggestion to use Selenium-based e2e testing; no opposing position is raised.

## f002300 — Restore manganis optimizations (2024-11-11, en)
### Questions
- Q: For compile-time-generated serialized data embedded via a macro (an asset descriptor built with `const` Rust and serialized at compile time), should the wire format be made valid/human-readable JSON, kept as the current bespoke binary format, or switched to an established binary serde format like postcard?
  concepts: const evaluation, macro-generated data, serialization format choice (JSON vs. bespoke vs. postcard), compile-time cost; domains_live: frontend; positions_seen: reviewer (unattributed) — would like the serialized bytes to be valid JSON; ealmloff (PR author) — avoid a bespoke format, but prefers moving toward an established format like postcard over JSON, citing the added const-time logic JSON would require
### Claims
- voice: ealmloff | position: prefer an established binary format (postcard) over both the current bespoke format and JSON | date: 2024-11-11 | locator: PR comment, responding to review | paraphrase: Responds to a suggestion that the serialized bytes be valid JSON by noting this would need much more const-time logic to format strings/numbers with uncertain compile-time cost, and states a preference for targeting postcard, an existing well-defined serialization format, over keeping a bespoke one. | quote: "I don't love having a bespoke serialization format. postcard is a much simpler well defined serialization format that might be easier to target than json. I think it is pretty similar to what we are currently generating" | practiced_evidence: DioxusLabs/dioxus#3195 (own PR containing the current bespoke serializer)

## f002341 — Relay outage: A post-mortem (2024-11-19, en)
### Nothing new
`nothing new` — single-author (Arqu) incident post-mortem; states as uncontested fact that "Rust's memory safety guarantees do not mitigate memory leaks" while describing a tokio task/thread leak, but no opposing position is present to disagree with.

## f002347 — Basic filtering examples for users of the bevy_log. (2024-11-21, en)
### Nothing new
`nothing new` — documentation-only PR; thread is contributor onboarding, CI/formatting fixes (`cargo fmt`, ensuring doc code blocks compile), and a joke about LLVM vs. LLM; no design disagreement present.

## f002356 — Deno Language Server doesn't work with brackets in filename (2024-11-22, en)
### Questions
- Q: When a Rust project's forked dependency must serialize URIs per a spec that requires strict RFC3986 percent-encoding (here, LSP's `TextDocumentIdentifier`), should it use the widely-adopted `url` crate (WHATWG URL Standard, which does not percent-encode brackets) or switch to a stricter RFC3986-compliant crate like `fluent-uri`?
  concepts: URI/URL encoding standards (RFC3986 vs. WHATWG), LSP protocol compliance, forked-dependency maintenance burden, crate choice for spec conformance; domains_live: desktop-cli-ui; positions_seen: commenter (unattributed) — Zed's `lsp-types` fork should upgrade to `fluent-uri` for spec-correct percent-encoding; the fork's existing choice (unattributed, inferred only from the fork's branch name `zed-main-no-url-changes`) — keep the `url` crate, for reasons not stated in this source
