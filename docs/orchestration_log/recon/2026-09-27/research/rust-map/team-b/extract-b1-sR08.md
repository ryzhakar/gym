## f003531 — Do not serialize buffers containing bundled files (2025-09-13, en)
### Questions
- Q: Should a piece of state with more than two meaningful outcomes be represented as a bool (with special-cased checks layered around it) or as a named enum?
  concepts: enums, boolean blindness, state/API design, type-safety; domains_live: desktop-cli-ui; positions_seen: enum-over-bool-for-tri-state-clarity
### Claims
- voice: MrSubidubi | position: enum-over-bool-for-tri-state-clarity | date: 2025-10-10 | locator: PR #38102, review comment 2025-10-10T21:34:30Z | paraphrase: instead of adding another special-cased check around the existing `serialize_dirty_buffers` boolean, suggests changing it to a named enum (`Always`/`Dirty`/`Never`) for readability. | quote: "Could we perhaps fix the logic above instead or change `self.serialize_dirty_buffers` to be an enum instead ... With that, this might be more readable and understandable, what do you think?" | practiced_evidence: https://github.com/zed-industries/zed/pull/38102 (merged as a `SerializationMode` enum)
- voice: im-lunex | position: enum-over-bool-for-tri-state-clarity | date: 2025-10-16 | locator: PR #38102, comment 2025-10-16T09:45:09Z | paraphrase: implemented the suggested `SerializationMode` enum in place of the boolean flag and judges it the safer, clearer choice. | quote: "The use of enum was the right decision - so neater and more secure." | practiced_evidence: https://github.com/zed-industries/zed/pull/38102 (merged)

## f003540 — Release DataFusion `50.1.0` (minor) (2025-09-16, en)
### Questions
- Q: When adding new methods to a public trait, should you give them default implementations to avoid a breaking change, or bump the major version?
  concepts: trait evolution, semver, default trait methods, API stability; domains_live: other; positions_seen: default-impls-to-avoid-breaking-change
### Claims
- voice: milenkovicm | position: default-impls-to-avoid-breaking-change | date: 2025-09-19 | locator: issue comment, 2025-09-19T15:47:59Z | paraphrase: added default implementations for two new `FunctionRegistry` trait methods so they would not trigger a backward-incompatible change in the 50.1.0 minor release, planning to make them required (unimplemented) only in the next major version. | quote: "I have provided default implementation for those two methods for now, so they do not trigger backward incompatible change. will revert them back to unmplemented methods for df 51 release" | practiced_evidence: https://github.com/apache/datafusion/pull/17650 (merged, backported, released in 50.1.0)
- voice: alamb | position: default-impls-to-avoid-breaking-change | date: 2025-09-18 | locator: issue comment, 2025-09-18T18:04:21Z | paraphrase: endorses adding the two new trait methods and shipping them in the 50.1.0 minor release rather than waiting for a major version bump. | quote: "I think adding two new methods and releasing `50.1.0` sounds good to me" | practiced_evidence: https://github.com/apache/datafusion (50.1.0 released per the thread's final comment)

## f003550 — Add torch.cross like functionality support (2025-09-17, en)
### Questions
- Q: Should a Rust practitioner follow an AI code-review tool's suggestions by default, or evaluate them critically before acting?
  concepts: AI-assisted Rust, code review, tooling trust; domains_live: ml; positions_seen: critically-evaluate-not-blindly-follow
### Claims
- voice: laggui | position: critically-evaluate-not-blindly-follow | date: 2025-09-19 | locator: PR #3743, review comment 2025-09-19T19:54:02Z | paraphrase: dismisses a Copilot review comment telling the author to avoid `&3` as unnecessary noise (passing a reference to a literal is fine), and redirects attention to a real bug the AI reviewer missed — an unsupported vectorization size on some cubecl backends. | quote: "You didn't need to follow Copilot's advice here 😄 passing &3 is fine." | practiced_evidence: https://github.com/tracel-ai/burn/pull/3743 (merged)

## f003587 — BurnpackStore (2025-09-26, en)
### Questions
- Q: Which serialization format should a Rust library pick for a data format that needs no-std support?
  concepts: serialization format choice, no-std, MessagePack, CBOR; domains_live: ml, embedded; positions_seen: cbor-over-messagepack-for-no-std
- Q: Should a method be named `into_foo` only when it actually consumes `self` (Rust's `into_`/`as_`/`to_` naming convention), or can `into_` be used more loosely?
  concepts: naming conventions, ownership semantics; domains_live: ml; positions_seen: into-must-consume-self
- Q: At an API boundary where allocation strategy matters (e.g. future backend-managed/pinned memory), should owned byte buffers be typed as `Vec<u8>` or a custom wrapper type?
  concepts: buffer/allocator abstraction, API design, GPU memory; domains_live: ml; positions_seen: custom-bytes-type-over-vec-u8-at-boundaries
### Claims
- voice: antimora | position: cbor-over-messagepack-for-no-std | date: 2025-10-10 | locator: PR #3792, comment 2025-10-10T14:21:49Z | paraphrase: switched the new format's metadata serialization from MessagePack (`rmp-serde`) to CBOR (`ciborium`) because `rmp-serde` isn't no-std compatible and its upstream project has been inactive for over a year, while CBOR is an IETF-standardized, Serde-recommended, no-std-capable format that also preserves enum variant information. | quote: "I switched from MessagePack to CBOR for metadata serialization due to rmp-serde's limitations" | practiced_evidence: https://github.com/tracel-ai/burn/pull/3792 (merged, tested on thumbv7m-none-eabi)
- voice: nathanielsimard | position: into-must-consume-self | date: 2025-10-09 | locator: PR #3792, review comments 2025-10-09T12:33:22Z and 2025-10-09T13:27:11Z | paraphrase: objects to a method using `into_`-style naming that doesn't actually take ownership of `self`, insisting the name should match the ownership signature and proposing a rename. | quote: "The naming isn't correct here, into should consume a self. Maybe `from_mapped_value`" | practiced_evidence: https://github.com/tracel-ai/burn/pull/3792 (merged)
- voice: nathanielsimard | position: custom-bytes-type-over-vec-u8-at-boundaries | date: 2025-10-09 | locator: PR #3792, review comment 2025-10-09T13:32:53Z | paraphrase: asks that owned buffer types at the store's API boundary use `burn_common::Bytes` rather than `Vec<u8>`, while leaving borrowed `&[u8]`/`&mut [u8]` as-is, so a future backend-managed allocation strategy (e.g. pinned GPU memory) can be substituted later. | quote: "We should replace all instances of `Vec<u8>` by `burn_common::Bytes`, `&[u8]` and `&mut [u8]` are OK" | practiced_evidence: https://github.com/tracel-ai/burn/pull/3792 (merged)

## f003634 — The Invisible Database: Running Postgres at Runtime (2025-10-02, en)
### Nothing new
`nothing new` — a product-marketing post by Neon's Product Marketing Lead about infrastructure requirements for AI agent platforms; no Rust code, crate, or implementation decision appears, and no Voice with a Rust track record is established in the text.

## f003685 — Neon Developer Days: Mark Your Calendars for March 29th, 2023 (2025-10-14, en)
### Nothing new
`nothing new` — a conference announcement listing session titles; no technical content or declared position of any kind.

## f003702 — Hashing multiple blobs with BLAKE3 (2025-10-15, en)
### Questions
- Q: When batch-hashing many small blobs (or a similar compute-bound batch workload), should you use thread-level parallelism (rayon), instruction-level parallelism (SIMD), or both, and when does each apply?
  concepts: parallelism (SIMD vs. threads), rayon, BLAKE3, compute-bound batching; domains_live: decentralized-iroh, ml; positions_seen: simd-for-small-batches-combine-with-threads-for-large-batches
### Claims
- voice: Rüdiger Klaehn | position: simd-for-small-batches-combine-with-threads-for-large-batches | date: 2025-10-15 | locator: § "Combining instruction level parallelism and thread level parallelism" | paraphrase: SIMD alone is a good choice for a small batch — decent speedup, stays on one core, doesn't disturb the rest of the program — but for a large batch where the whole machine is available, combining SIMD with rayon's thread-level parallelism gives peak throughput (measured 17x over sequential, 2.1x over rayon alone). | quote: "Instruction level parallelism alone is frequently a good choice if you have a small batch of blobs to hash. You get a decent speed up but only use one CPU, and don't affect other parts of your program... For peak performance we can combine instruction level parallelism and thread level parallelism." | practiced_evidence: https://github.com/rklaehn/BLAKE3 (linked benchmark repo); technique used in iroh-blobs per the post

## f003719 — Handling Time-Variant DAGs with Constraints in Postgres (2025-10-20, en)
### Nothing new
`nothing new` — a guest post by a traconiq engineer about Postgres schema/trigger design (temporal edges, deferred constraint triggers, PL/pgSQL conflict resolution); entirely SQL/Postgres content with no Rust code or Rust practitioner decision.

## f003731 — iroh 0.94.0 - The Endpoint Takeover (2025-10-22, en)
### Questions
- Q: When a type may need to represent additional variants in the future (e.g. new transport kinds), should it be modeled as a `#[non_exhaustive]` enum of variants, or as a struct with independent optional fields per kind?
  concepts: enums, `#[non_exhaustive]`, API extensibility, semver; domains_live: decentralized-iroh; positions_seen: non-exhaustive-enum-over-struct-of-optionals
- Q: Should a library perform a broad breaking rename across its whole public API to align vocabulary with its current mental model, or keep legacy names for compatibility?
  concepts: API naming, breaking changes, semver, vocabulary consistency; domains_live: decentralized-iroh; positions_seen: rename-for-vocabulary-consistency-pre-1.0
### Claims
- voice: ramfox | position: non-exhaustive-enum-over-struct-of-optionals | date: 2025-10-22 | locator: § "Future proofing: Introducing TransportAddr" | paraphrase: replaced two independent fields (an optional relay URL and a set of socket addresses) with a single `#[non_exhaustive] enum TransportAddr { Relay(RelayUrl), Ip(SocketAddr) }`, so future transport kinds (e.g. WebRTC) can be added as new variants without another breaking change. | quote: "To combine them, and to allow for additions in the future, they are now represented as variants on a TransportAddr" | practiced_evidence: https://github.com/n0-computer/iroh (shipped in 0.94.0)
- voice: ramfox | position: rename-for-vocabulary-consistency-pre-1.0 | date: 2025-10-22 | locator: § "Changing from Node to Endpoint everywhere" | paraphrase: dropped "node" from iroh's vocabulary project-wide (`NodeAddr`→`EndpointAddr`, `node_id`→`endpoint_id`, etc.), reasoning that the term was a holdover from an earlier, broader project scope, and that pre-1.0 is the right moment to align vocabulary with the current mental model despite the breaking change this causes. | quote: "We've officially made the decision to remove the word "node" from our vocabulary... In preparation for 1.0, that has been rectified." | practiced_evidence: https://github.com/n0-computer/iroh (shipped in 0.94.0; full breaking-changes list in the post)

## f003756 — Keeping the Internet fast and secure: introducing Merkle Tree Certificates (2025-10-28, en)
### Nothing new
`nothing new` — a WebPKI/cryptography protocol-design post by Cloudflare researchers (Merkle Tree Certificates, post-quantum TLS handshakes); tagged "Rust" on the site but the article itself never discusses Rust code, crates, or an implementation decision, and no Voice with a Rust track record is established in the text.
