# Audit — batch 1, third pass

Auditor: t4-audit (opus), never an extractor. 2026-09-27T20:45Z.

Rules applied:
- `prompts/t4-merge.md` § t4-audit.
- `prompts/t2-extract.md`, rules 1–9. Rule 8: practice without a reason or a named alternative is no Claim. Rule 9: a Claim needs a Voice whose Rust connection shows in the source, flagged `voice-unverified`; no mapping of other language communities' arguments onto Rust.
- Prior audits: `audit/audit-b1.md`, `audit/audit-b1-sendback.md`.

Scope: `team-{a,b}/readlog-b1-sT*.csv` and `extract-b1-sT*.md`; bundles `samples/bundles/b1-team-{a,b}-T*.txt`; `b1-team-{a,b}-T-manifest.csv`.

## Verdict

| team | nothing-new sampled | drops audited | misses | verdict |
|---|---|---|---|---|
| a | 5 of 46 | 1 of 1 (f000217) | f000217 (on-subject drop, reachable) | **FAIL** |
| b | 5 of 33 | 0 (no drops) | none | **PASS** |

Claims check (reported separately; false positives are struck and do not fail a team):

| team | Claims in pass | sampled | struck |
|---|---|---|---|
| a | 18 | 2 | 0 |
| b | 36 | 4 | 3 |

Team B's nothing-new rows hold up. Its sample of logged Claims does not: 3 of 4 sampled Claims are diagnoses, requests or tentative plans, which rule 8 excludes. Team A's content judgments hold up in both samples. It fails on a dropped Rust source whose recorded drop reason is false.

## Method

**Scope match.** Third-pass rows are exactly the send-back's still-nothing-new rows:
- Team A: 60 such rows, plus `f000217` carried from the R-manifest drops (61 T-manifest rows: 60 kept, 1 dropped).
- Team B: 49 rows (49 kept).

Every read-log id has an extract section; no duplicates. `f000149`, the send-back's on-subject drop and one of its misses, is not in the T-manifest, the sT read logs or any sT extract. It was not carried forward (see Open carry-overs).

**Population, nothing-new.** A sT read-log row with `read=yes`, `new_questions=0` and `claims=0`. Team A: 46. Team B: 33.

**Sample size, nothing-new.** max(5, ceil(10%)): 5 per team.

**Drops.** Every T-manifest drop: team A 1, team B 0.

**Population, Claims.** Every `- voice:` line in the sT extracts. Team A: 18. Team B: 36. Both counts equal the read logs' `claims` sums.

**Sample size, Claims.** ceil(10%): team A 2, team B 4.

Claims logged in earlier passes (batch 1 and send-back) are outside this check, though rules 8–9 postdate them.

**Seed.** `500922438`, generated inside the process that drew all three samples, so it was fixed before any output existed. It was the only draw. RNG: `random.Random(f"{SEED}-{team}-third")`: first the nothing-new sample from the sorted population, then the Claim indices from the file-ordered Claim list. The run reproduces from RECON with `uv run python draw3.py 500922438`:

```python
import csv, glob, math, random, re, sys, secrets
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else secrets.randbits(31)
for t in "ab":
    rl = {}
    for f in sorted(glob.glob(f"team-{t}/readlog-b1-sT*.csv")):
        for r in csv.reader(open(f)):
            if r[0] != "frame_id": rl[r[0]] = r
    pop = sorted(k for k, r in rl.items() if r[2] == "yes" and r[4].strip() == "0" and r[5].strip() == "0")
    claims = []
    for f in sorted(glob.glob(f"team-{t}/extract-b1-sT*.md")):
        cur = None
        for line in open(f):
            if line.startswith("## "):
                m = re.findall(r"f\d{6}", line); cur = m[0] if m else None
            if re.match(r"\s*[-*]\s*(\*\*)?voice", line, re.I): claims.append((cur, f, line))
    rng = random.Random(f"{SEED}-{t}-third")
    s1 = sorted(rng.sample(pop, min(max(5, math.ceil(0.1 * len(pop))), len(pop))))
    s3 = sorted(rng.sample(range(len(claims)), math.ceil(0.1 * len(claims))))
    print(t, s1, [claims[i][0] for i in s3])
```

**Miss bar (nothing-new rows).** Rules 6, 8 and 9 as written. A miss is a Voice, with a Rust connection shown in the source, declaring a decision Rust practitioners make differently, with a reason or against a named alternative, and not logged. A dropped row is a miss when it is on-subject.

**Strike bar (Claims).** A Claim is struck when it fails rule 8 (no decision, or no reason and no named alternative), rule 9 (no Rust connection in the source, or another community's argument mapped onto Rust), or rule 3 (no own words, locator or date). A mismatch between the Claim's Position and its logged Question is noted but not struck.

## Team A — nothing-new rows

| frame_id | source | extractor's reason (short) | verdict |
|---|---|---|---|
| f001677 | forums.swift.org, set literals pitch | Swift syntax; no Rust-connected Voice | pass |
| f002042 | forums.swift.org, SE-0446 | Rust passages describe Rust, take no side on a Rust decision | pass (note D1) |
| f004065 | pingcap.com, Ninja Van story | no Rust; TiKV only in nav | pass |
| f004174 | forums.swift.org, "What is ~Copyable for?" | contested points argued by Swift Voices about Swift; rule 9 | pass |
| f004562 | zed issue 53694, git panel | bug triage | pass |
| f000217 (drop) | nalgebra.org/docs | `no-text` | **MISS** |

**f004174, checked closely.** The single Position about Rust is @Nobody1707, 2026-01-29T22:01:36Z: "I'm honestly not convinced that Rust was wrong in making Copy a refinement of Clone". The same post shows no Rust use: "an abstraction over a Clonable protocol" is Swift. The destructor-versus-consuming-close dispute (@FranzBusch 2026-01-29T20:32) is a live Rust Question too, but it is argued about Swift's `deinit`. Rule 9 bars both. The pass stands.

**f000217 — MISS.** On-subject: the nalgebra user guide (Rust linear-algebra crate), `books-courses`, strata core and ml. The drop rests on "html/wayback/browser all failed (DNS unresolved, no wayback snapshot)" (`prefetch-b1-status.csv` lines 8 and 409). The Wayback lookup queried only the bare host. The www host has snapshots, found at audit time via `archive.org/wayback/available`:
- `http://web.archive.org/web/20250210193839/https://www.nalgebra.org:443/docs/`
- `…/20250824053211/http://www.nalgebra.org/`

The snapshot page ("About nalgebra", about 1,000 chars stripped) is the guide's front page. Its body is 11 linked chapters, among them "Performance tricks", "WASM and embedded targets" and "Generic programming". I read the snapshot in scratch and did not write it to the cache (the same deviation as f000149 in the send-back, for the same reason: it would bypass `cache.py`'s route order and length gate).

## Team B — nothing-new rows

| frame_id | source | extractor's reason (short) | verdict |
|---|---|---|---|
| f002301 | bevy PR 16340, `unregister_system` | Bevy-local naming | pass |
| f004371 | forums.swift.org, "New Codable" prototype | Rust/serde mentions come from Swift designers; no Claim | pass (note D1) |
| f005504 | HelixDB README | product docs; no decision against an alternative | pass |
| f007125 | darkcoding.net, Rust HashMap notes | describes std's design; no choice argued | pass |
| f008692 | Embedded Rustacean #58 | link roundup; the mission belief names no alternative | pass (same row as batch 1 W2) |

**f004371, checked closely.** Every Rust-bearing post (23 lines) was read in full. @kperryua evaluates serde, musli, serde_with and struct-patch as models for a Swift API. Examples:
- 2026-03-06T18:15: "the general shape of the musli crate was a better fit for adapting to Swift"
- 2026-05-21: "the best choice for Swift here would be to follow a path similar to Rust's"

None of these takes a side on a Rust decision; rule 9 bars mapping them. At 2026-05-19T21:09 he reports a Rust-side dispute ("I have indeed seen complaints about this requirement") without joining it. The pass stands.

## Claims check

| # | team | frame_id | Voice / Position | verdict |
|---|---|---|---|---|
| C1 | a | f001650 | ramfox / cancel-safety-required-in-library | keep (weak) |
| C2 | a | f008237 | author of ideas.reify.ing / minimal imports | keep |
| C3 | b | f002499 #7 | Dominaezzz / cause is bus bandwidth, not the async runtime | **STRUCK** (rule 8) |
| C4 | b | f002501 #12 | Mettwasser / fix should be available on the old minor | **STRUCK** (rule 8) |
| C5 | b | f003809 #3 | comphead / replicate the dropped trait downstream as fallback | **STRUCK** (rule 8; also off-Question) |
| C6 | b | f004166 #6 | Nick Kuntz / drop foreign keys, enforce integrity in app code | keep (Question-fit note) |

- **C1, keep (weak).** Source § "Better late than never": the team broke its two-week cadence because "we found a critical bug … our RPC channels were not cancel-safe", and fixed it in their own `quic-rpc` crate (Rust connection shown). Treating a missing cancel-safety guarantee as a critical library bug is a decision with a reason. The "library versus caller responsibility" framing is the extractor's; the Claim concedes the alternative is not named. Kept, because the reason is stated.
- **C2, keep.** "the Rust compiler will include the whole wasi:cli world that includes some interfaces that are useless in this case". The alternative is the current std behaviour, the reason is given, and the author filed the issue. Rust connection: "I will write programs in Python and Rust. These two are my favorite", plus an issue "in Rust repository, filed by me".
- **C3, struck.** Comments 2026-02-02T17:31:48Z ("This is PSRAM bandwidth issue at it purest") and 20:24:42Z ("I won't be surprised if it's due to the scheduler code executing from flash"). This is a causal diagnosis, not a decision. The one decision-like passage lists options without choosing: "You can choose to restart the DMA transfer … Or you can start looking into bounce buffers".
- **C4, struck.** 2025-01-10T15:44:55Z: "there are so many breaking changes that I can't get my app to compile 🫠 Could you make a branch that is based on `0.13.2`?". A one-off support request is not a declared Position on backport policy. The sibling Claim by kaplanelad (maintainer declines, with a reason) is a decision and stands. It was not sampled.
- **C5, struck.** 2026-01-06T17:30:28Z: "in Comet we just started experiments, plan B is to replicate SchemaAdapter in Comet codebase". A tentative contingency with no reason for choosing it over the unnamed plan A. It also answers a different decision (coping with a removed upstream trait) from the logged Question (release sequencing against arrow 58).
- **C6, keep.** § D1: "D1's eventual consistency breaks foreign key constraints … We removed all foreign keys and enforce referential integrity in application code". A decision with a reason. Rust connection: workers-rs code in the post (`#[durable_object]`, `kv.put(&format!(…))?`). Note: the post also says the protocol logic was ported "in TypeScript using the Hono framework", which contradicts its Rust snippets, and the FK decision is a D1/SQLite schema choice more than a Rust one. The Position also sits loosely under the logged Question (edge primitives versus VPS stack). The merge should weigh this.

## Notes and defects (not misses)

- **D1, rule-9 misread (both teams).** f002042 (team A) calls Xazax-hun's "writing non-trivial amount of Rust in the past" "self-report, not a bar criterion". f004371 (team B) cites "no public Rust track record". Rule 9 names self-reported Rust use as a connection, and track record is tier 3's check. Neither verdict changes: neither source holds a Position on a Rust decision.
- **Book and guide front pages.** f000149 (send-back) and f000217 (here) are both `books-courses` URLs where the fetch stops at a roughly 1,000-char front page and the chapters are never fetched. The same pattern may affect other `books-courses` rows kept or dropped in batch 1. I have not checked beyond these two.

## Open carry-overs

- **f000149** (nogibjj rust-tutorial): a send-back miss, absent from the third pass. Still unread.
- **f000217:** re-fetch through the www Wayback snapshot and the chapter pages, then extract.

## Limits of this audit

- The Claim samples are small (2 and 4). Three of team B's four sampled Claims are struck. At this rate team B's 36 third-pass Claims likely hold several more rule-8 failures; that is an inference from 4 rows, not a measurement. Checking all 36 would settle it.
- Team A's FAIL rests on a single drop. The fault lies in the fetch (a Wayback lookup that missed the www host), not in an extractor's judgment.
- Team B's PASS rests on 5 of 33 rows.
