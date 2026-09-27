# Strike check — batch 1, third-pass Claims

Auditor: t4-audit (opus). 2026-09-27T20:50Z.

Scope: every `- voice:` line in `team-{a,b}/extract-b1-sT*.md`. Team A has 18, team B 36; both counts equal the read logs' `claims` sums. Extract files are not edited.

Rules: `prompts/t2-extract.md` rules 3, 6, 8, 9, plus the lead's strike list:
- practice without a reason or a named alternative;
- diagnoses;
- support requests;
- tentative plans;
- Claims answering a different decision than their Question;
- Voices with no Rust connection in the source (self-reported use counts).

Each Claim was checked against its bundle text (`samples/bundles/b1-team-{a,b}-T*.txt`). For f000576, the check used cache `c0a6bea7195d`, as the extractor did. Every quote in a KEEP Claim was found verbatim in the source.

**Claim id.** Team letter plus the Claim's position in file order: files sorted, `- voice:` lines in file order. `#k` is the Claim's ordinal inside its sT file. The `audit-b1-third.md` sample used the same `#k` ordinals.

**How requests are split.** A request to a maintainer is struck as a support request when its only reason is the requester's own situation (my app won't compile; lets us drop our patches). It is kept, marked weak, when it gives a general design reason (portability; "it is required").

## Totals

| team | Claims | KEEP | of which weak | STRIKE |
|---|---|---|---|---|
| a | 18 | 15 | 1 | 3 |
| b | 36 | 23 | 8 | 13 |
| total | 54 | 38 | 9 | 16 |

Strikes by ground:

| ground | a | b |
|---|---|---|
| another community's decision (rule 9: Swift/Hylo argument, Rust only as comparison) | 2 | 1 |
| answers a different decision than its Question | 1 | 4 |
| diagnosis or assessment, not a decision | 0 | 4 |
| support request (own-situation reason) | 0 | 2 |
| practice without a reason, or support-answer aside | 0 | 2 |

The team B strikes by ground sum to 13 because b28 has two grounds (tentative plan and different decision) and is counted under the different-decision row only.

## Team A

| id | frame / file #k | Voice / Position | verdict | reason |
|---|---|---|---|---|
| a01 | f001319 sT04 #1 | dignifiedquire / break-compat-with-transition-window | KEEP | Breaks 0.13 relay compatibility for a handshake one roundtrip shorter, softened by keeping old relays 4 weeks. |
| a02 | f001650 sT04 #2 | ramfox / cancel-safety-required-in-library | KEEP (weak) | Missing cancel-safety treated as a critical bug that delayed the release. The "library vs caller" framing is the extractor's. |
| a03 | f002226 sT07 #1 | Karl / restrict-and-lint-confusables | **STRIKE** | Argues what Swift should do ("We should revisit which code-points are allowed"). Rust is cited as the better model; no Rust decision is at stake (rule 9). |
| a04 | f002883 sT07 #2 | daxpedda / release-on-request | KEEP | "relatively low cost so I favor making one as soon as requested". A reason given; maintainer role shown. |
| a05 | f003375 sT08 #1 | n0 / length-prefixed-framing-on-one-stream | KEEP | Rejects `write_all`/`read_all`-per-stream ("fine while you are getting familiar") for framed messages, with a reason. |
| a06 | f004169 sT08 #2 | ramfox / unified-generic-typestate | KEEP | `Connection<T>` replaces duplicated state structs, with a stated reason (de-duplication). |
| a07 | f004169 sT08 #3 | ramfox / non-exhaustive-for-future-variants | KEEP | Non-exhaustive `TransportAddr` replaces `ConnectionType` because custom transports are planned. |
| a08 | f004169 sT08 #4 | ramfox / connection-layer-hooks | KEEP | Auth in hooks "so individual protocols don't need to handle authentication themselves". |
| a09 | f004205 sT10 #1 | Alvae / scoped access suffices | **STRIKE** | Speaks for Hylo ("we're betting that Hylo does not need Rust-like references") in a Swift design thread. The Question is Rust's language design, not a practitioner decision (rule 9). |
| a10 | f004960 sT11 #1 | n0 / authenticated by default, library unopinionated | KEEP | Managed relays authenticated by default, with a reason (a leaked URL lets anyone use the relay). Defect: two Positions in one Claim; the merge should split them. |
| a11 | f007659 sT11 #1 | maahl / size-optimized release profile | KEEP | Profile adopted with a measured reason (3.6→1.8 MB, cold start 20→17 ms). Self-reported Rust use. |
| a12 | f007659 sT11 #2 | maahl / zip via cargo-lambda, container only when needed | **STRIKE** | Different decision. The quote recommends the Cargo Lambda tool; Docker is offered "if, for some reason, you need" it, not rejected. Zip vs container is never argued. |
| a13 | f007659 sT11 #3 | maahl / typed response struct | KEEP | A `Serialize` struct replaces unvalidated JSON "to leverage Rust's strong typing". |
| a14 | f008237 sT12 #1 | ideas.reify.ing author / component model over C ABI | KEEP | C ABIs "not only fragile but also dangerous". A named alternative plus a reason; Rust use self-reported. |
| a15 | f008237 sT12 #2 | ideas.reify.ing author / minimal imports | KEEP | Whole `wasi:cli` world pulled for `format!` is "useless"; the author filed the rustc issue. |
| a16 | f008455 sT12 #3 | rustunit / pure-Rust bindings via objc2 | KEEP | "without having to write objc but pure rust instead". A named alternative. |
| a17 | f009632 sT12 #4 | Rust Leadership Council / revised 2024 draft | KEEP | Revised policy against the named 2023 draft, with a reason (addresses the concerns). Governance counts. |
| a18 | f009704 sT12 #5 | Jake Goulding / demote to Tier 2 | KEEP | Demotion with a reason: the tier policy requires CI tests, and the free runners are ending. |

## Team B

| id | frame / file #k | Voice / Position | verdict | reason |
|---|---|---|---|---|
| b01 | f000267 sT01 #1 | Zcash Foundation / dual MIT/Apache, MIT-only by provenance | **STRIKE** | The dual licence is stated as practice with no reason. MIT-only is compliance with upstream licences, not a view on the dual-vs-single Question. The date is the access date, not the Voice's. |
| b02 | f000576 sT02 #1 | andrews05 / tail-expression-hurts-readability | KEEP | "someone who has been working with Rust a lot lately … seriously hurts readability". Judges Rust's own rule from Rust use. |
| b03 | f000576 sT02 #2 | Nobody1707 / tail-expression-reads-better | KEEP (weak) | "I find implicit return of the last expression in Rust much easier to read". Rust connection only as "my (also anecdotal) experience". |
| b04 | f000576 sT02 #3 | stackotter / tail-expression-reads-better | **STRIKE** | The preference is for Swift syntax ("Assuming another keyword is chosen I'd still likely prefer bare last expressions"). Rust appears only as the source of bias; it answers Swift's decision. |
| b05 | f001890 sT04 #1 | n0 / drop Deref delegation for explicit accessors | KEEP (weak) | Changelog "No more deref of …" names the replaced design (rule 6, last sentence). No reason given. |
| b06 | f002233 sT04 #2 | n0 / runtime env var, not cfg/features | KEEP | Drops `test-utils`/`#[cfg(test)]` switching, with a reason (a bug pointed builds at staging relays). |
| b07 | f002499 sT05 #1 | Dominaezzz / infinite cyclic DMA buffer | KEEP | "In my own projects … I avoid restarting transfers and I always use an infinite DMA buffer". Practice against a named alternative, with its limit stated. |
| b08 | f002499 sT05 #2 | EliteTK / bounce buffers + Mem2Mem DMA, no XIP | KEEP | Design with reasons (glitch-free output under PSRAM stalls; CPU copy "glacial"). |
| b09 | f002499 sT05 #3 | Limeth / acyclic descriptors restarted per frame | KEEP (weak) | Cyclic failed after the first frame, so acyclic plus restart, "although not as nice". An early experiment. |
| b10 | f002499 sT05 #4 | yanshay / stay on I8080 | KEEP | Kept the I8080 display because flash contention and PSRAM bandwidth slowed the app. |
| b11 | f002499 sT05 #5 | EliteTK / bare Rust no worse than Arduino | **STRIKE** | Assessment, not a decision: "I don't see why this should be any worse with bare rust". |
| b12 | f002499 sT05 #6 | yanshay / esp-hal dpi does not work well under embassy | **STRIKE** | Diagnosis from experiments ("I believe it has to do with embassy in some way"). |
| b13 | f002499 sT05 #7 | Dominaezzz / cause is bus bandwidth, not async runtime | **STRIKE** | Diagnosis ("This is PSRAM bandwidth issue at it purest"). |
| b14 | f002499 sT05 #8 | yanshay / HAL should expose cache flush | KEEP (weak) | "worth making some public version available, it is required". A feature request with a general reason. |
| b15 | f002499 sT05 #9 | Dominaezzz / removing the discussion area lost knowledge | KEEP (weak) | Objects to a named project decision (deleting Discussions), with a reason (knowledge lost). |
| b16 | f002499 sT05 #10 | yanshay / removing the discussion area lost knowledge | KEEP (weak) | Same as b15 ("no alternative location for such discussion now"). |
| b17 | f002501 sT05 #11 | kaplanelad / no backport to 0.13.x | KEEP | Maintainer declines a backport and recommends upgrading, with a reason ("the new version introduces some excellent features"). |
| b18 | f002501 sT05 #12 | Mettwasser / fix on the old minor | **STRIKE** | Support request with an own-situation reason ("so many breaking changes that I can't get my app to compile"). |
| b19 | f002550 sT05 #13 | ramfox, matheus23 / runtime PathSelection behind test-utils | KEEP | "DEV_RELAY_ONLY compile time environment variable has been completely dropped". A named alternative. Note: the opposite direction to b06, same Voice at a later date. |
| b20 | f002550 sT05 #14 | ramfox, matheus23 / remove the actor | KEEP | "removing an unnecessary actor", with a reason (fewer layers). |
| b21 | f002550 sT05 #15 | ramfox, matheus23 / infallible close | KEEP (weak) | Changelog "instead of returning a Result". A named alternative, no reason. |
| b22 | f002775 sT05 #16 | Jonathan Pallant / donate under a permissive licence | KEEP | "As long-time advocates of open-source development, we are proud to be able to donate". A reason given. |
| b23 | f003044 sT05 #17 | jkelleyrtp / explicit devtools connection | **STRIKE** | A support-answer aside ("we don't do this implicitly") describing current behaviour. No reason; the same comment says "We should probably change the logging". |
| b24 | f003044 sT05 #18 | pickfire / loosen serde to `^1` | KEEP (weak) | A request with a general reason ("so that it can be more portable for packages that uses an older serde version"). |
| b25 | f003044 sT05 #19 | frederikhors / hot-patching worth it | **STRIKE** | A bug report, not a decision: "2.7 seconds instead of 13 … BUT … IT'S NOT WORKING!" |
| b26 | f003809 sT07 #1 | brancz / arrow 58 first, then DataFusion | **STRIKE** | Request with an own-situation reason ("allow us not to have to carry some patches"; "No worries if not"). |
| b27 | f003809 sT07 #2 | alamb / ship DF 52 against arrow 57.2 minor | KEEP | Release decision with a reason ("Since it is a minor version … you should be able to update"). |
| b28 | f003809 sT07 #3 | comphead / replicate the dropped trait downstream | **STRIKE** | Tentative plan ("just started experiments, plan B is …"). It also answers a different decision than the release-sequencing Question. |
| b29 | f003809 sT07 #4 | adriangb / rework downstream | **STRIKE** | Different decision: coping with the removed `SchemaAdapter`, not release sequencing. |
| b30 | f004166 sT07 #5 | Nick Kuntz / serverless edge primitives | KEEP | Workers/D1/KV/R2/DO over a VPS+Postgres+Redis stack, with reasons ("different data needs different consistency guarantees"; operations disappear, cost scales to zero). Rust connection: workers-rs code in the post. The prose says the port is "in TypeScript using the Hono framework", which contradicts that code; tier 3 should check. |
| b31 | f004166 sT07 #6 | Nick Kuntz / drop foreign keys | **STRIKE** | Different decision: a D1 schema-integrity choice, not edge primitives vs VPS. This changes the KEEP given at `audit-b1-third.md` C6, under the lead's explicit criterion. |
| b32 | f005312 sT09 #1 | vaultwarden maintainers / reverse proxy over built-in TLS | KEEP | Names the rejected alternative (Rocket's built-in TLS); rule 8 is met by the named alternative. |
| b33 | f005314 sT09 #2 | summer-rs project / convention-over-configuration framework | **STRIKE** | Different decision. The README's reasons compare against Java SpringBoot/JVM and C/C++, never against composing axum/sqlx directly, which is what the Question asks. |
| b34 | f005440 sT09 #3 | Serdar Yegulalp / Rc/Arc when reader count unclear, RefCell narrow | KEEP | A conditional recommendation with reasons; a Rust post counts as a Rust connection (rule 9). The extractor's caveats about technical errors are for tier 3. |
| b35 | f011688 sT09 #4 | Joshua Mo / durable Postgres-backed queue | KEEP | "Without durable job queues, our jobs would disappear if our web service has any outages!" |
| b36 | f011688 sT09 #5 | Joshua Mo / provision from code annotations | KEEP | Named alternatives (Docker, Terraform, manual Postgres) and a reason (simplicity). A vendor tutorial; the extractor flagged it. |

## Notes

- **Earlier audit verdicts that current rules reverse.** f003375 (a05), f001890 (b05) and f011688 (b35, b36) were passes in `audit-b1.md` or `audit-b1-sendback.md` and now hold kept Claims. Under the current rule 6 (its release-note/tutorial clause was added after those audits) and rule 8, those Nothing new verdicts would have been misses. This affects no team's earlier verdict: each of those audits already failed both teams on other rows.
- **Strike rate.** Team B's rate is 13/36. Its content is high-volume GitHub threads (esp-hal, loco, dioxus, datafusion), where diagnoses, requests and plans dominate. Team A's 3/18 are all cross-community or off-Question.
- **Weak KEEPs.** 9 KEEPs are marked weak: a single-sentence request or aside, a changelog line with no reason, or a thin Rust connection. Tier 3 or the blind fill should look at these first.
