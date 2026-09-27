For each source: where do competent Rust practitioners disagree?

Team a, batch 1, third pass, slice T08. All seven sources read from the bundle; none visibly cut, no fetch made. Rules in force: 1–9 of t2-extract.md — a Claim needs a Voice whose Rust connection shows in the source, taking a side on a Rust decision with a reason or against a named alternative; flagged `voice-unverified` for tier 3; arguments from other language communities are not mapped onto Rust Questions.

## f003266 — Is this a bug in automatic reference counting? (2025-07-17, en)

### Nothing new
A Swift thread on `consume` and copies into `consuming` parameters; Rust appears only in John_McCall's description (2025-07-17T17:55) that Rust always moves into consuming positions while Swift copies to avoid source breaks, which describes Rust and argues a Swift decision, and no participant shows a Rust connection in the source.

## f003375 — Tutorial: Message Framing with iroh (2025-08-12, en)

### Questions
- Q: On a QUIC stream, should a protocol send several length-prefixed messages over one stream, or one message per stream written with `write_all` and read to the end before closing?
  concepts: QUIC streams; message framing; length prefix; varints; protocol design; domains_live: decentralized-iroh; distributed; positions_seen: length-prefixed-framing-on-one-stream (against whole-stream-per-message)

### Claims
- voice: n0 (post by ramfox, matheus23, b5) | position: length-prefixed-framing-on-one-stream | date: 2025-08-12 | locator: § Intro and § Framed Messages, paragraphs on `write_all`/`read_all` | paraphrase: writing one chunk with `write_all`, reading it all, then closing the stream is fine while learning, but real protocols should send multiple logical messages per stream, each prefixed by its length, so the protocol is designed as messages rather than bytes and variable-length messages are handled | quote: "This is fine while you are getting familiar, but when you go to write your protocols you will want something more sophisticated." | practiced_evidence: https://github.com/n0-computer/iroh (named in the post: dumbpipe, sendme, iroh-examples framed messages example; not opened) | flag: voice-unverified — Rust connection in the source: the authors write for n0 as iroh's makers ("how we at n0 like to serialize") and the tutorial is Rust with cargo, tokio, iroh.

Left out: `anyhow` "allows us to do easy error handling" and the ALPN naming "conventions we recommend" are a dependency gloss and a recommendation without an alternative or reason on a contested choice (rule 8); `u8` vs larger or varint length prefixes is stated as a size trade-off instruction, not a Position.

## f003389 — Neon's Microsoft Azure Native Integration is Generally Available (2025-05-07, en)

### Nothing new
A product announcement by Monica Steinke (Neon) about Azure integration; Rust never appears.

## f003594 — AI: Agent & tools just stop working no matter the model/provider (2025-09-27, en)

### Nothing new
A Zed bug report about agent stalls across model providers; the comments are reproduction reports and triage (morgankrey closing it 2026-06-09 to split failure modes), with no Rust decision argued.

## f004065 — Delivering at Scale: How Ninja Van Powers Millions of Shipments with TiDB (2025-09-02, en)

### Nothing new
A PingCAP customer story (M. Nivanya, recapping Mani Kuramboyina's talk) on moving from MySQL/Galera to TiDB after evaluating Vitess, CockroachDB and AliCloud ADB; Rust never appears (TiKV is only a nav/tag link), and no Voice shows a Rust connection.

## f004166 — Building a serverless, post-quantum Matrix homeserver (2026-01-27, en)

### Nothing new
Nick Kuntz (Cloudflare) argues running a Matrix homeserver on Workers, D1, KV, R2 and Durable Objects instead of a VPS with PostgreSQL and Redis, and dropping D1 foreign keys for application-enforced integrity; these are platform and storage decisions argued without reference to Rust, so they are not a Rust decision under rule 9. Doubt to record: the post says the protocol logic was ported "in TypeScript using the Hono framework" yet shows Rust snippets (`#[durable_object]`, `kv.put(&format!(…))`) and mentions "porting Tuwunel"; the Rust connection is real but the language of the port is inconsistent in the source (the post notes it was updated at 11:45 a.m. PT).

## f004169 — iroh 0.96.0 - The QUIC Multipaths to 1.0 (2026-01-27, en)

### Questions
- Q: Should a Rust API express protocol states as one generic type with a typestate parameter (`Connection<T>`), or as separate concrete types per state?
  concepts: typestate; generics; API design; code duplication; 0-RTT; domains_live: core; decentralized-iroh; positions_seen: unified-generic-typestate (replacing separate-state-structs)
- Q: Should a public enum that may gain variants be `non_exhaustive` before a crate's 1.0, trading exhaustive matching for room to add variants without a breaking change?
  concepts: `#[non_exhaustive]`; semver; forward compatibility; 1.0 stability; domains_live: core; positions_seen: non-exhaustive-for-future-variants
- Q: Should authentication and similar concerns for iroh protocols live in connection-layer hooks (middleware), or inside each protocol implementation?
  concepts: middleware; connection interception; authentication; separation of concerns; domains_live: decentralized-iroh; positions_seen: connection-layer-hooks (against per-protocol auth)

### Claims
- voice: ramfox | position: unified-generic-typestate | date: 2026-01-27 | locator: § "0-RTT and the Connection API changes" | paraphrase: separate `OutgoingZeroRttConnection` and `IncomingZeroRttConnection` structs duplicated the whole connection API and stopped 0-RTT connections sharing code paths; a single `Connection<T>` with a state parameter restores that flexibility and de-duplicates the code, with state-specific signatures only where authentication differs | quote: "we've de-duplicated a bunch of code that was the same over the three different variaties of connections" | practiced_evidence: https://github.com/n0-computer/iroh | flag: voice-unverified — Rust connection in the source: author of the iroh release post, "our implementation".
- voice: ramfox | position: non-exhaustive-for-future-variants | date: 2026-01-27 | locator: § "TransportAddr rather than conn_type and ConnectionType" | paraphrase: because custom transports (bluetooth, WebRTC) are a planned direction, iroh 1.0 must handle new address kinds, so `TransportAddr` is a non-exhaustive enum replacing `ConnectionType` | quote: "we need to make sure that iroh 1.0 can handle supporting different kinds of addresses" | practiced_evidence: https://github.com/n0-computer/iroh | flag: voice-unverified — as above.
- voice: ramfox | position: connection-layer-hooks | date: 2026-01-27 | locator: § "Endpoint Hooks", `auth-hook` example paragraph and the paragraph after it | paraphrase: an `EndpointHooks` trait intercepts connections before connect and after handshake, so authentication, authorization, rate limiting and observability sit at the connection layer and individual protocols stay on their core logic instead of each handling auth | quote: "individual protocols don't need to handle authentication themselves" | practiced_evidence: https://github.com/n0-computer/iroh | flag: voice-unverified — as above.

Left out: switching from custom holepunching to the IETF QUIC-NAT-Traversal draft, and multipath, are networking-protocol decisions internal to iroh that its users do not make and that are not argued as Rust choices; the `Discovery` → `AddressLookup` rename is a naming clarification without a contested alternative.
