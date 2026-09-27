# Audit — batch 1

Auditor: t4-audit (opus), never an extractor. 2026-09-27T16:11Z. Rules applied: `prompts/t4-merge.md` § t4-audit, `prompts/t2-extract.md`, `prompts/common.md`, PLAN lines 132, 345–386.

## Verdict

| team | sampled | misses | verdict |
|---|---|---|---|
| a | 10 nothing-new + 1 dropped | 1 judgment miss (f012428), 1 record miss (f000227), 1 miss by the rule's wording only (f011125) | **FAIL** |
| b | 11 nothing-new + 1 dropped | 1 judgment miss (f002937) | **FAIL** |

Shared cause: both teams' extractors dismiss sources because no second Voice opposes the first inside the source. The rule is "`nothing new` only when the source raises no contested point at all" (PLAN t2 skeleton), and a Claim is "one Voice holding one Position": nothing requires opposition inside a single source. Census of all nothing-new reasons (not sampled, every section): team A 11 of 97 cite a missing opposing or second Voice, team B 30 of 101. Not every one of these is a miss: many also state a sound ground. The count shows how widespread the test is.

## Method

**Population, nothing-new.** One row per frame_id, merged across every read-log file of the team, L-slice entries included. A row counts as nothing-new when every entry reads `yes` and `new_questions` sums to 0 over all its entries. So a row that an L-slice re-logged as `0 … already extracted`, after an earlier slice logged Questions for it, is not nothing-new. Team A: 92 rows. Team B: 101 rows. Unreachable rows (team A, 7 paywalled books) are excluded, since there is nothing to re-read.

**Population, dropped.** Manifest rows with `status=dropped`. Team A: 10. Team B: 9.

**Sample size.** ceil(10%) of each population: team A 10 + 1, team B 11 + 1.

**Seed.** `2034695869`, fixed before any draw output existed, used for the only draw made. A `secrets.randbits(31)` value (`1853667790`) was generated in the same step and never used. No redraw. Per-team RNG: `random.Random(f"{SEED}-{team}")`. The run reproduces from RECON as the working directory with `uv run python draw.py 2034695869`:

```python
import csv, glob, math, random, sys
SEED = int(sys.argv[1])
def parse(r):  # tolerates the malformed rows listed under Defects
    if len(r) == 7: return r[0], r[1], r[2], r[4], r[5]
    if len(r) > 7: return r[0], r[1], r[2], r[-3], r[-2]
    if len(r) == 6: return r[0], r[1], r[2], r[4], r[5]
    raise ValueError(r)
for t in "ab":
    ent = {}
    for f in sorted(glob.glob(f"team-{t}/readlog-b1-*.csv")):
        for r in csv.reader(open(f)):
            if r[0] == "frame_id": continue
            fid, url, read, nq, cl = parse(r)
            ent.setdefault(fid, []).append((f, url, read, int(nq), int(cl)))
    pop = sorted(fid for fid, es in ent.items()
                 if all(e[2] == "yes" for e in es) and sum(e[3] for e in es) == 0)
    man = list(csv.DictReader(open(f"samples/bundles/b1-team-{t}-manifest.csv")))
    dropped = sorted(r["id"] for r in man if r["status"] == "dropped")
    rng = random.Random(f"{SEED}-{t}")
    s1 = sorted(rng.sample(pop, math.ceil(0.1 * len(pop))))
    s2 = sorted(rng.sample(dropped, math.ceil(0.1 * len(dropped))))
    print(t, s1, s2)
```

**Re-read.** Each sampled source was read from the text the extractor had: the bundle slice named in the manifest, or the cache file for team A's pre-bundle rows 1–30. Where the cache now holds fuller text than the extractor saw, both were read (f000227). For two Swift-internal forum threads (f001837, f003923), I read the Rust-bearing passages in full and scanned the rest; the scan found no Rust content beyond the passages quoted.

**Miss bar, fixed before grading.** A sampled row is a miss when the source holds a Voice's declared Position, in their own words, on a decision Rust practitioners face and are known to split on. Opposition inside the source is not required. Off-subject content (no Rust decision) is correctly nothing-new. A dropped row is a miss when it is on-subject.

Grades:
- **Miss:** the Position comes with a reason or against an alternative, on a recognized dispute.
- **Weak:** an aside, a mission statement, or a marginal dispute. Weak items are listed for a ruling and do not set the verdict. Counting them would change neither verdict.

Disclosure: this tiering was worded after reading team A's rows and before grading team B's. The bar itself did not change.

## Team A

| frame_id | source | extractor's reason (short) | verdict |
|---|---|---|---|
| f000227 | rtic.rs (RTIC book) | "bare redirect stub … 75 characters" | **MISS (record)**, see below |
| f000545 | zed issue 4382, Zen mode | editor UX, not Rust | pass |
| f001837 | forums.swift.org, actor async setters | Swift-internal, one Rust analogy | pass |
| f002016 | wasmtime PR 9234, PyTorch backend | cargo-vet logistics, CI | pass |
| f002271 | sycamore PR 752, query params | implementation thread | pass |
| f002883 | wasm-bindgen PR 4472, Safari TextDecoder | converging bug workaround | pass, weak item W1 |
| f007472 | teaql.io, query predicates | in-house naming rule, cross-language | pass |
| f008777 | Embedded Rustacean #63 | no extract section (see Defects) | pass, weak item W2 |
| f012428 | YouTube K5SY-lc8nTE, Rust polymorphism | "uncontested … not contested by another named voice" | **MISS** |
| f012963 | UCG issues search, FCP label | bundle held README; extractor re-queried, 0 open issues | pass |
| f011125 (dropped) | YouTube FaCxNZNnWGY, Oxidize: reusable code with WebAssembly | no-text, yt-dlp 429 | **MISS by the rule's wording**, see below |

**f012428 — MISS.** Voice: Nas (self-introduced at [00:02] as author of developerlife and maintainer of the r3bl crates; the transcript spells it "Rebel, Dewey"). Date: 2025-03-26 (frame date).
- [01:03]: "if you're coming from an object-oriented … background … rest can seem a little bit … restrictive … it's a bit cumbersome than probably other languages … that are object-oriented … there's a trade-off"
- [34:17]: "arguably it's more verbose and somewhat confusing especially if you're coming from something like cotlin or java or typescript"

The talk models an Android/DOM-style view hierarchy by emulating inheritance with supertraits and `Vec<&mut dyn Component<…>>`. This is a declared Position with a reason (monomorphization, no GC) on a recognized dispute. Candidate Question: should OO-style view hierarchies be modeled in Rust with supertraits and trait objects, and is the lack of inheritance a real cost? Domains: desktop-cli-ui, frontend, core. The extractor's own entry names this remark and sets it aside only because no second Voice contests it in the source, a ground the rules do not give. Counter-reading: the remark is hedged, tutorial-grade and not the talk's thesis. Even so it is still a declared Position, and the rule sets no bar on how strongly it is argued.

**f000227 — MISS (record).** Extract written 09:44:23 local; the cache then held a 75-char redirect stub. The browser re-fetch landed at 09:46 local (`cache/0ae387ef9986.txt`, 11,754 chars). The extractor read honestly, but logged `read=yes`/nothing-new where t2 rule 2 required `unreachable`. The bundler then excluded rows 1–30 as "already extracted", so the recovered text was never extracted. That text raises contested points, from the RTIC project (institution, undated living document):
- "From RTIC's developers point of view; RTIC is a hardware accelerated RTOS … Another common view from the community is that RTIC is a concurrency framework"
- "in the setting of resource constrained real-time systems, dynamic allocations are problematic … Thus, static allocation is the preferable approach!"
- "the commonly adopted threading model does not lend itself well to static analysis … SRP based scheduling is in the general case out of reach for any thread based RTOS"

The failure is in logging, not in reading judgment. The effect is the one the audit exists to catch: a source recorded as empty that is not empty.

**f011125 — MISS by the rule's wording.** On-subject (Oxidize talk, wasm;web). Dropped as `no-text`, which is true: YouTube 429 on every try (`prefetch-b1-status.csv` lines 175, 578, 815). The rule reads "a dropped row that is on-subject" fails the batch. Here the drop reason is correct and re-extraction cannot help; the remedy is a re-fetch. Ruling requested: does a true no-text drop of an on-subject row count? Team A's verdict does not depend on it.

## Team B

| frame_id | source | extractor's reason (short) | verdict |
|---|---|---|---|
| f000763 | ratatui PR 840, table example | example review, taste | pass |
| f000981 | materialize.com, data freshness | marketing, no Rust | pass (only "rust" hit is "Trust Center" in the footer) |
| f001401 | wasmtime issue 8573, alignment slowdown | converging diagnosis | pass |
| f001890 | iroh 0.23 release post | renames with rationale, no contest | pass |
| f002177 | iroh issue 2799, Wasm tracking | maintainer answers unopposed | pass |
| f002755 | qdrant.tech, enterprise features | vendor post, no Rust | pass |
| f002937 | bytecodealliance.org, Wasmtime LTS | "Single-voice … without an opposing view present in the source" | **MISS** |
| f003302 | neon.com, Postgres TLS defaults | Postgres, not Rust | pass (the 4 "rust" hits are inside "trust") |
| f004809 | spinframework.dev, Spin 4.0 | release/tutorial, no second voice | pass |
| f008692 | Embedded Rustacean #58 | link roundup, no position | pass, weak item W2 |
| f011688 | shuttle.rs, cronjobs tutorial | one way shown, no alternatives argued | pass |
| f003923 (dropped) | forums.swift.org, Advent of Code 2025 | off-subject | pass (only hit: "knock the rust off") |

**f002937 — MISS.** Voice: Alex Crichton for the Wasmtime project. Date: 2025-04-22.
- Paragraph 2: "This rate of change can be too fast for users so Wasmtime now supports LTS releases."
- "High-level summary" list: "Patch releases strive to maintain tooling compatibility (e.g. the Rust version required to compile Wasmtime) from the time of release."

This is a declared Position, with a reason and against the prior alternative (2-month support), on two recognized disputes: support windows and LTS lines for Rust software, and holding MSRV in patch releases. Candidate Question: should a Rust project offer long-term-support lines with a stable MSRV, or support only its latest release? Domains: wasm, core. The extractor set it aside only because no opposing view appears in the source. Counter-reading: this is a policy announcement, not an argument. Even so, an institution's declared policy with its rationale is a Claim under the opinion map's Voice types.

## Weak items (ruling requested; neither verdict depends on them)

- **W1 (team A, f002883):** "My 2¢: making a release is relatively low cost so I favor making one as soon as requested." This is a release-cadence aside by a maintainer "not yet back to maintaining", identified from the thread context; the frozen slice carries no per-comment authors or dates.
- **W2 (both teams, f008777 and f008692):** the Embedded Rustacean mission line, "the belief in Rust as a programming language with all the traits … that prime it to become the future of software in embedded systems". It is the same boilerplate in every issue, and both teams treated it alike.

## Defects found (format and logging, not misses)

- Team A, `extract-b1-sa18.md`: no section for f008777, though the read log lists it. OUTPUT 2 requires one section per source. It is the only such row in either team (census over all read logs).
- Team A, 6 read-log rows with unquoted commas in `locator_span` break CSV parsing: sa12 (f004581, f004598), sa25 (f011413), sa28 (f012469), sa30 (f013276), saL2 (f011069). In saL2 the text "no new Questions/Claims found" lands in the `new_questions` column.
- Team B, 18 read-log rows in sb23 and sb25 lack the `minutes` column (6 fields, not 7).
- Team A, f000227: `read=yes` over a 75-char stub (above). One out-of-sample row looks similar and was not verified: team B f012788 (`netstack.fm`), logged `yes` with locator "episode index; no transcript text".
- Frozen slices a-01…04 and b-01…02 carry GitHub text without per-comment authors or dates (the attribution fix came in bundle round 2). f002016, f002271 and f002883 are affected: a Claim from them could not name a dated Voice. This does not change any verdict here.

## Limits of this audit

- Each team was sampled once, 10–11 rows. One miss fails a team by rule, so the verdict is sensitive to how each flagged row is graded. Both judgment misses rest on counting a single Voice's declared Position, with no opposition in the source, as loggable. If the orchestrator rules that such Positions are not loggable at Tier 2, team B has no miss and passes. Team A then still has f000227 (record) and f011125 (the rule's wording).
- "Recognized dispute" is judged from knowledge of Rust discourse, not measured against the frame. The same judgment is asked of the extractors.
- The 11/97 and 30/101 census is a phrase match over stated reasons, not a re-read. It counts occurrences of the test, not misses.
