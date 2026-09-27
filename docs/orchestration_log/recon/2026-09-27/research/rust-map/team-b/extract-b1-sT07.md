For each source: what must a Rust practitioner decide, and where do the sources conflict on it?

Team b, batch 1, slice T07, under rules 6–9. Source text: bundle RECON/samples/bundles/b1-team-b-T07.txt; nothing fetched. Durations in the read log are estimates.

## f003756 — Keeping the Internet fast and secure: introducing Merkle Tree Certificates (2025-10-28, en)

### Nothing new
The decisions (batch-signed Merkle Tree Certificates over drop-in PQ certificates; bootstrap certificates instead of becoming a CA) are WebPKI/TLS protocol choices. Rust appears only as a post tag, and no author shows a Rust connection in the text (rule 9).

## f003809 — Release DataFusion `52.0.0` (Dec 2025 / Jan 2026) (apache/datafusion#18566) (2025-11-09, en)

### Questions
- Q: Should a Rust library release wait for, or be sequenced after, a new major version of a core dependency (arrow 58 before DataFusion 52), or ship on schedule against the current major's minor?
  concepts: release coordination across crate ecosystems; major vs minor dependency bumps; downstream patch carrying; domains_live: core, distributed; positions_seen: release arrow major first so downstream can drop patches; ship on the planned arrow minor
- Q: When a library removes a public trait in a major release (DataFusion dropping `SchemaAdapter`), should downstream vendor the removed trait or rework their integration, and does the migration cost count against the removal?
  concepts: breaking changes; semver majors; vendoring; downstream migration cost; domains_live: core, distributed; positions_seen: replicate the dropped trait in the downstream codebase as fallback; rework, the cost is on downstream's own hacky use
### Claims
- voice: brancz | position: release arrow 58 first, then DataFusion | date: 2026-01-06 | locator: comment 2026-01-06T15:32:51Z | paraphrase: asks for arrow 58 then a DataFusion update then release, so downstream stops carrying patches and uses upstream | quote: "it would just allow us not to have to carry some patches and actually use upstream once df 52 is out" | practiced_evidence: none | flag: voice-unverified
- voice: alamb | position: ship DataFusion 52 against the planned arrow minor (57.2.0) | date: 2026-01-06 | locator: comment 2026-01-06T15:41:44Z | paraphrase: the next arrow release is minor 57.2.0; being minor, it should work with DataFusion 52, so no reordering | quote: "Since it is a minor version I think you should be able to update to use it with DataFusion 52" | practiced_evidence: https://github.com/apache/arrow-rs/issues/8465 (linked release ticket) | flag: voice-unverified
- voice: comphead | position: replicate the dropped trait downstream as fallback | date: 2026-01-06 | locator: comments 2026-01-06T17:13:01Z, 2026-01-06T17:30:28Z | paraphrase: the SchemaAdapter removal lengthens Comet's upgrade; plan B is to copy SchemaAdapter into the Comet codebase | quote: "plan B is to replicate SchemaAdapter in Comet codebase" | practiced_evidence: none | flag: voice-unverified
- voice: adriangb | position: rework downstream; the cost falls on downstream's own misuse | date: 2026-01-06 | locator: comment 2026-01-06T17:17:48Z | paraphrase: Pydantic was hit by the same removal, but because of its own hacky dynamically generated columns filled by SchemaAdapter; offers to work through issues | quote: "that's mostly on us for doing *horrifying* things in the first place" | practiced_evidence: none | flag: voice-unverified
### Caveats
- The downstream test checklist, the holiday-timed stabilization and tschwarzinger's question on why `DynamicFilterPhysicalExpr` lacks `Clone` are practice or an open question with no declared Position, so no Claims (rule 8). alamb's answer does not refuse brancz's reordering outright; it states the planned sequence.
- All Voices show Rust connection in-thread (DataFusion/arrow-rs release work, Rust code, cargo tests); track records unverified.

## f004166 — Building a serverless, post-quantum Matrix homeserver (2026-01-27, en)

### Questions
- Q: Should a stateful protocol server be built on serverless edge primitives (Workers, D1, KV, R2, Durable Objects) rather than a traditional VPS + Postgres + Redis stack?
  concepts: serverless; Durable Objects for strong consistency; per-data consistency choice; scale-to-zero cost; domains_live: cloud-workers, distributed; positions_seen: serverless edge primitives, each data class on the primitive matching its consistency need
- Q: On eventually consistent storage, should referential integrity be enforced by database foreign keys or in application code?
  concepts: eventual consistency; foreign keys; D1/SQLite; domains_live: cloud-workers, distributed; positions_seen: drop foreign keys, enforce in application code
### Claims
- voice: Nick Kuntz | position: serverless edge primitives, per-data consistency | date: 2026-01-27 | locator: § storage primitives ("The key insight from porting Tuwunel…"); § conclusion | paraphrase: D1 for queryable durable data, KV for OAuth tokens, R2 for media, Durable Objects where atomicity is required (one-time key claims); argues operations vanish and cost scales to zero | quote: "different data needs different consistency guarantees" | practiced_evidence: none (repo mentioned, no URL in bundle text) | flag: voice-unverified
- voice: Nick Kuntz | position: drop foreign keys, enforce integrity in app code | date: 2026-01-27 | locator: § D1 ("We learned one hard lesson") | paraphrase: D1's eventual consistency broke FK checks across sequential writes, so all FKs were removed | quote: "We removed all foreign keys and enforce referential integrity in application code." | practiced_evidence: none | flag: voice-unverified
### Caveats
- The source contradicts itself on language: it says the protocol logic was ported "in TypeScript using the Hono framework", yet shows a Rust `async fn claim_otk(&self, algorithm: &str) -> Result<Option<Key>>`, speaks of "porting Tuwunel", and carries the Rust tag. The Rust connection rests on that snippet and tag alone and may fail tier 3.
- The post was updated to call it "a proof of concept and a personal project".
