For each source: what must a Rust practitioner decide, and where do the sources conflict on it?

## f001398 — SE-0430 (second review): `sendable` parameter and result values (2024-05-07, en)

### Nothing new
A Swift Evolution review of how to spell the region-isolation parameter modifier (`sendable` vs `sending` and others); it was accepted as `sending`. Rust comes up only in comparisons: @filip-sakel cites Rust's `Unique<T>` (2024-05-08T00:44:45Z), and @beccadax describes Rust's ownership model as struggling with cyclic object graphs (2024-05-08T05:35:59Z). Neither shows a Rust connection in the source, and under rule 9 Swift-community arguments are not mapped onto Rust Questions.

## f001609 — Healing Connections After Network Migration (2024-06-17, en)

### Nothing new
An explainer by ramfox (iroh) on how iroh keeps connections alive when a network changes: netcheck probes, CallMeMaybe and Ping disco messages, and addressing by Node ID rather than IP. It describes how iroh works. It declares no Rust decision against an alternative.

## f001890 — iroh 0.23.0 - Welcoming Node.js to the family! (2024-08-21, en)

### Questions
- Q: Should a Rust API expose one type's methods through another via `Deref` (delegation by deref), or through explicit accessor methods?
  concepts: Deref-based delegation; API structure; accessor methods; breaking changes; domains_live: core; decentralized-iroh; positions_seen: drop Deref, use explicit accessor `node.net()` (n0/iroh)

### Claims
- voice: n0, inc. / iroh team (post by ramfox) | flag: voice-unverified | position: drop Deref delegation for explicit accessors | date: 2024-08-21 | locator: § "Letting net stand on its own"; § Breaking Changes > API Changes > iroh, first bullet | paraphrase: The release pulls the networking methods out of the node methods, so users now call `node.net().node_addr()` instead of `node.node().node_addr()`. It lists "No more deref of iroh::net::Client to iroh::client::node::Node" as a breaking change, replacing the earlier deref-based grouping. The stated reason is to let net "stand on its own". The Voice's Rust connection is shown in the source: the post is written by the maintainers of the Rust crates iroh, iroh-net and iroh-blobs and includes Rust code. | quote: "No more deref of iroh::net::Client to iroh::client::node::Node" | practiced_evidence: https://github.com/n0-computer/iroh/releases/tag/v0.23.0 (named in the post, not opened)

Not logged, stated with no reason: flume replaced by async-channel (`FlumeProgressSender` is now `AsyncChannelProgressSender`), `LocalSwarmDiscovery` no longer `UnwindSafe`, and Node.js bindings built through napi. The ConnectionInfo→RemoteInfo rename gives a reason, but it is a naming fix specific to this project.

## f001953 — Compare (diff) two files (zed-industries/zed #17100) (2024-08-29, en)

### Nothing new
A feature-request thread about diffing two files in Zed's UI. It contains no Rust content or decision.

## f001990 — Easy Embeddings Indexing Pipelines with Redpanda and Neon (2024-09-06, en)

### Nothing new
A no-code tutorial (Redpanda Connect YAML, Ollama embeddings, pgvector on Neon). It does not mention Rust.

## f002233 — iroh 0.27.0 - Squashing Bugs and Taking Names (2024-10-24, en)

### Questions
- Q: Should a Rust crate switch test-only or staging behaviour through Cargo features and `#[cfg(test)]`, or through a runtime environment variable?
  concepts: Cargo features (`test-utils`); `#[cfg(test)]`; runtime configuration via environment variables; test vs production infrastructure; domains_live: core; decentralized-iroh; positions_seen: runtime env var only (n0/iroh), cfg/feature gating (the replaced approach, no Voice defends it here)

### Claims
- voice: n0, inc. / iroh team (post by ramfox) | flag: voice-unverified | position: select staging vs production by runtime env var, not by cfg/features | date: 2024-10-24 | locator: § "Sensible config options can go a looooong way" | paraphrase: A bug made builds pick the wrong relay servers (production vs staging), and the old config made it "too easy to point production code to our staging relays". So iroh-net no longer uses the `test-utils` feature or `#[cfg(test)]` to decide which infrastructure code runs against. It relies only on the `IROH_FORCE_STAGING_RELAYS` environment variable, behind a new `force_staging_infra` function. | quote: "We no longer rely on the test-utils feature or the #[cfg(test)] annotations for determining whether code runs against production or staging infrastructure" | practiced_evidence: https://github.com/n0-computer/iroh/releases/tag/v0.27.0 (named in the post, not opened)

Not logged: `Endpoint::builder().discovery_n0()` replacing a hand-built `ConcurrentDiscovery::from_services(vec![Box::new(..)])`. It is a convenience method replacing a manual setup, with no contested Rust decision stated.

## f002301 — Add `unregister_system` command (bevyengine/bevy #16340) (2024-11-11, en)

### Nothing new
A PR review about naming (`remove_system` → `unregister_system`), justified in the thread because "remove" suggests the opposite of `add_systems`. The naming consistency is specific to Bevy. No Rust-wide decision is contested.
