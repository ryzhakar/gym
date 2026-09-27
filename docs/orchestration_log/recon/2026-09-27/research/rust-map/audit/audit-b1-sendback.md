# Audit — batch 1, send-back pass

Auditor: t4-audit (opus), never an extractor. 2026-09-27T16:40Z.

Rules applied:
- `prompts/t4-merge.md` § t4-audit.
- `prompts/t2-extract.md`, rules 1–7. Rule 6: a single Voice's declared Position is a Claim; "single-voice" or "no opposing view" is never a reason. Rule 7: stub text is `unreachable`.
- `prompts/common.md`.
- Batch-1 audit: `audit/audit-b1.md`.

Scope: `team-{a,b}/readlog-b1-sR*.csv` and `extract-b1-sR*.md`; bundles `samples/bundles/b1-team-{a,b}-R*.txt`; `b1-team-{a,b}-R-manifest.csv`.

## Verdict

| team | sampled | misses | verdict |
|---|---|---|---|
| a | 6 nothing-new + 1 dropped | f004169 (judgment, rule 6); f000149 (on-subject drop); f011484 (record, see below) | **FAIL** |
| b | 5 nothing-new + 0 dropped (no drops) | f002233 (judgment, rule 6); f005312 (judgment, rule 6) | **FAIL** |

Rule 6 is still not applied as written. Three of the four judgment misses are release notes or READMEs where the project declares a decision on a Rust-level engineering choice, framed against the alternative it replaced or declined. The extractors log these as Nothing new because nobody argues back. The misses are narrower than in batch 1: all three batch-1 misses were re-extracted (see Regression), and the dismissals no longer mostly say "single-voice". What remains are rewordings of the same ground: "against another view" (f004169) and "against a competing view" (f002233).

## Method

**Scope match.** The send-back re-extracted exactly batch 1's nothing-new populations. Team A: 92 R-manifest rows, 90 kept, 2 dropped (`no-text`), 90 read-log rows. Team B: 101 R-manifest rows, 101 kept, 101 read-log rows. Every read-log id has an extract section; no duplicate ids.

**Population, still nothing-new.** A send-back read-log row with `read=yes`, `new_questions=0` and `claims=0`. Team A: 60. Team B: 49. The read log is used, not the extract headings, because the sR extracts mix formats: `### Nothing new`, a bare "Nothing new. Reason:", and `### Questions` / `None.`. Unreachable rows are excluded: team A 2, team B 2.

**Population, dropped.** R-manifest `status=dropped`. Team A: 2. Team B: 0.

**Sample size.** ceil(10%): team A 6 + 1, team B 5 + 0.

**Seed.** `1503125270`, generated inside the same process that drew the sample (`secrets.randbits(31)`), so it was fixed before any output existed. It was the only draw. Per-team RNG: `random.Random(f"{SEED}-{team}-sendback")`. The run reproduces from RECON with `uv run python draw2.py 1503125270`:

```python
import csv, glob, math, random, sys, secrets
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else secrets.randbits(31)
for t in "ab":
    rl = {}
    for f in sorted(glob.glob(f"team-{t}/readlog-b1-sR*.csv")):
        for r in csv.reader(open(f)):
            if r[0] != "frame_id": rl[r[0]] = r
    pop = sorted(k for k, r in rl.items() if r[2] == "yes" and r[4].strip() == "0" and r[5].strip() == "0")
    man = list(csv.DictReader(open(f"samples/bundles/b1-team-{t}-R-manifest.csv")))
    dropped = sorted(r["id"] for r in man if r["status"] == "dropped")
    rng = random.Random(f"{SEED}-{t}-sendback")
    print(t, sorted(rng.sample(pop, math.ceil(0.1 * len(pop)))),
          sorted(rng.sample(dropped, math.ceil(0.1 * len(dropped)))))
```

**Re-read.** Each source was read from its R bundle slice. f000149 has no cached text: I fetched the live page to read it and did not write it to the cache, because `cache.py`'s 1,500-char gate rejects it. Its full stripped text is summarized below. For f002042 (a Swift forum thread), I read all Rust-bearing posts in full and scanned the rest.

**Miss bar.** The same bar as batch 1, now also stated by rule 6. A miss is a Voice's declared Position, in their own words, on a decision Rust practitioners make differently, with a reason or against an alternative, that is not logged. Opposition inside the source is not required. Off-subject content (no Rust decision) is correctly nothing-new. An on-subject dropped row is a miss.

## Team A

| frame_id | source | extractor's reason (short) | verdict |
|---|---|---|---|
| f002042 | forums.swift.org, SE-0446 Nonescapable types | Swift-internal; Rust used as comparison | pass (note N1) |
| f003375 | iroh.computer, message-framing tutorial | neutral tutorial; varints named, not argued | pass |
| f004169 | iroh.computer, iroh 0.96 release | "records no Voice arguing a contested position against another view" | **MISS** |
| f004229 | pingcap.com, TiDB traffic replay | no Rust content (TiKV only in nav) | pass |
| f004414 | pingcap.com, voice-first AI journal | no Rust content | pass (the Positions in it are about a JavaScript/TiDB stack) |
| f011484 | github.com/rust-lang/rfcs/labels/final-comment-period | RFC process README, "rather than any one Voice arguing a Position" | **MISS (record)**, see below |
| f000149 (dropped) | nogibjj.github.io/rust-tutorial | `no-text` | **MISS (on-subject drop)** |

**f004169 — MISS.** Voice: ramfox, for the iroh project. Date: 2026-01-27. Locator: § "0-RTT and the Connection API changes".
- Quote: "Rather than having completely separate OutgoingZeroRttConnection and IncomingZeroRttConnection types that duplicate the entire connection API, we now have a unified Connection<T> type where T describes the connection state"
- Reason given: "we've de-duplicated a bunch of code … added back flexibility".

This is a declared Position, against a named alternative, on how to encode an object's states in Rust types: a state type parameter versus separate structs. It is a decision Rust practitioners make differently (the typestate trade-off). Domains: decentralized-iroh, core. The same post also declares, with reasons:
- a non-exhaustive `TransportAddr` enum for forward compatibility (§ "TransportAddr rather than conn_type");
- auth handled as connection-layer hooks, so that "individual protocols don't need to handle authentication themselves" (§ "Endpoint Hooks").

The extractor's ground, no Voice arguing "against another view", is the ground rule 6 forbids.

**f011484 — MISS (record).** The URL is the RFC repo's `final-comment-period` label listing. The bundled text (13,805 chars) is the repo README, a different Source. The same send-back handled the identical case at f012963 (UCG `final-comment-period` search that returned only the README) as `unreachable`. Here it was logged `read=yes` and nothing new. There are two ways to read this, and both leave the row wrong:
1. **The README is not the source.** The row should be `unreachable` (t2 rule 1 and PLAN directive rule 1: evidence only from the source itself). It is mislogged as read and empty.
2. **The README is the source, as the extractor treated it.** It holds a declared governance Position (Rust project, institution Voice; README § "What the process is"): the FCP motion "does not require consensus amongst all participants in the RFC thread (which is usually impossible)". Governance disputes count (`docs/subjects/rust.md` § Scope). The dismissal, "rather than any one Voice arguing a Position", is the rule-6 ground again.

Team A's verdict does not depend on this row.

**f000149 — MISS (on-subject drop).** The R-manifest drop reason, `no-text`, is not accurate: the page was fetched and rejected as thin (`prefetch-b1-status.csv` lines 7 and 408: html 973 chars, wayback 1,188, browser 973). The live page, re-fetched by me at audit time, is the landing page of an mdBook course, "Learning Rust Tips — Small Rust Tutorial For MLOps". It has a 15-entry chapter list (Getting Started with Rust … Distributed Computing and Concurrency with Rust … Serverless … AI Assisted Coding) and one line: 'Use GitHub ecosystem to "LEVEL UP" to a more powerful language in Rust'. The row is on-subject: a Rust course, `books-courses`. The 973 chars are the book's front page; the chapters, which are the source's body, were never fetched. Batch 1 left open whether a true no-text drop of an on-subject row counts. This drop's text is not absent, it is truncated to the front page, so it counts under the rule's own wording either way.

**N1 (f002042, not a miss).** The thread has a real exchange about Rust: Xazax-hun, 2024-10-07T15:49, "I rarely see T: 'static in real world Rust code"; Joe_Groff, 2024-10-07T16:35, "explicit 'static requirements come up often in async code". But the decision under discussion is Swift's (`~Escapable`), and Xazax-hun concedes at 16:00 ("This sounds like a strong justification"). The extractor's added ground, "no participant is established with a Rust track record", is a Voice-bar check that belongs to t3-voice, not Tier 2. It is not decisive here.

## Team B

| frame_id | source | extractor's reason (short) | verdict |
|---|---|---|---|
| f001246 | neon.com, Developer Days 1 | event announcement, no Rust | pass |
| f002233 | iroh.computer, iroh 0.27 release | "none is framed as a Position against a competing view" | **MISS** |
| f003634 | neon.com, "The Invisible Database" | marketing, no Rust | pass (0 "rust" tokens) |
| f003719 | neon.com, time-variant DAGs in Postgres | SQL/PLpgSQL only | pass (0 "rust" tokens) |
| f005312 | github.com/dani-garcia/vaultwarden README | "no Voice states a position on any contested Rust-practitioner decision" | **MISS** |

**f002233 — MISS.** Voice: ramfox, for the iroh project. Date: 2024-10-24. Locator: § "Sensible config options can go a looooong way".
- Quote: "We no longer rely on the test-utils feature or the #[cfg(test)] annotations for determining whether code runs against production or staging infrastructure, but only on the IROH_FORCE_STAGING_RELAYS environment variable"
- Reason given: a bug that selected the wrong relay when building binaries, and the aim to "simplify the logic".

This is a declared Position against the replaced alternative, on a decision Rust practitioners make differently: Cargo features or `cfg(test)` versus a runtime switch for test-versus-production behaviour. Domains: core, decentralized-iroh. The extractor's ground, not framed "against a competing view", is false on the text: the post names the alternative it dropped. Rule 6 forbids that ground anyway. This is the weaker of team B's two misses; it is a miss if rule 6 is read as written.

**f005312 — MISS.** Voice: the vaultwarden maintainers (README, repo dani-garcia/vaultwarden). Date: 2024-08-14 (frame date; living document). Locator: § "Usage".
- Quote: "While Vaultwarden is based upon the Rocket web framework which has built-in support for TLS our recommendation would be that you setup a reverse proxy"

This is a declared recommendation, against the named alternative (the framework's built-in TLS), on terminating TLS in a Rust web service or in a proxy in front of it. Batch 1 already logged Claims on this dispute (f005360, lobste.rs "Replacing nginx with axum"). Domains: web.

## Regression (not sampled)

The batch-1 audit's misses were re-extracted:
- f000227: 2 Questions, 2 Claims, full page.
- f012428: 1 Question, 1 Claim.
- f002937: 1 Question, 1 Claim.

f008777 now has an extract section (`extract-b1-sR15.md`).

A phrase census over every send-back nothing-new reason (a match on stated reasons, not a re-read) still finds the forbidden "no opposition" ground:
- team A: 3 (f004169, f008237, f009704);
- team B: 2 (f002233, f002499). One further team B hit, f001246, is a false positive in a summary line.

## Defects (not misses)

- The sR extracts use three formats for Nothing new (see Method). The PLAN skeleton has one, `### Nothing new`.
- f004414: extract header date 2026-03-13; the article's dateline reads 2026-03-11.
- f000149: R-manifest `reason=no-text`, but the status CSV shows the text was fetched and rejected as thin.

## Limits of this audit

- The samples are small (6 and 5 rows); one miss fails a team. Team A's verdict rests on f004169 and f000149. Team B's rests on f002233 and f005312; either alone suffices.
- For f002233 and f005312, "a decision Rust practitioners make differently" is judged from knowledge of Rust discourse, supported for f005312 by an existing batch-1 Question. Suppose rule 6 were narrowed to exclude project policies and recommendations that are not argued in general terms. Then f002233 would not count; f005312 is the more defensible of the two.
- f000149's content was read from the live page on 2026-09-27, not from a cache snapshot. The page may differ from what the prefetch saw (973 chars then; the stripped text I read is of similar size).
