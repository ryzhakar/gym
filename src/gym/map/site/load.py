"""Data layer for the map site: YAML in, canonical Concepts and derived edges out.

Nothing here knows about HTML. Two consumers: `graph` (the Concept graph,
the front door) and `matrix` (Bertin's reorderable matrix, moved unchanged
from the single-file site.py).

Canonical Concepts
------------------
A Concept file may carry `merged_into: <id>` naming the Concept it was
folded into by the dedup pass. Every reference is resolved through that
chain to its canonical id; a Concept with no `merged_into` is canonical.
The chain is followed to a fixed point and is cycle-safe: a cycle resolves
to the lexicographically smallest id on it, so the result never depends on
which member the walk started from.

Edges
-----
The owner's rule (docs/opinion-map.md, Form, 2026-09-30): an edge between
two Concepts holds every Question that touches both. So for one Question,
every unordered pair of its *canonical* Concepts gains weight 1 and that
Question's id joins the edge's container. Weight therefore always equals
the number of Questions on the edge -- the one invariant the tests check
against an independent pass over the YAML.

Two raw Concepts on one Question that resolve to the same canonical
Concept collapse to a single node and yield no self-loop; the pair is
simply not there once the Question's Concepts are deduplicated.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from pathlib import Path

import yaml


def load_kind(map_dir: Path, name: str) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for f in sorted((map_dir / name).glob("*.yaml")):
        out[f.stem] = yaml.safe_load(f.read_text()) or {}
    return out


def canonical_map(concepts: dict[str, dict]) -> dict[str, str]:
    """Every Concept id -> the canonical id it resolves to.

    A missing or empty `merged_into` means the Concept is canonical. A
    `merged_into` pointing at an id this map does not hold stops the walk
    there and the last known id wins, so a dangling pointer never drops a
    Concept. A cycle resolves to its smallest member.
    """
    canon: dict[str, str] = {}
    for cid in concepts:
        seen: list[str] = []
        seen_set: set[str] = set()
        cur = cid
        while True:
            if cur in canon:
                cur = canon[cur]
                break
            seen.append(cur)
            seen_set.add(cur)
            nxt = (concepts.get(cur) or {}).get("merged_into")
            if not nxt or nxt not in concepts:
                break
            if nxt in seen_set:
                # A cycle resolves to the smallest id *on the cycle*, not the
                # smallest id walked: an id that merely points into a cycle
                # from outside is not part of it and must not win.
                cur = min(seen[seen.index(nxt):])
                break
            cur = nxt
        for s in seen:
            canon[s] = cur
    return canon


def concept_label(concepts: dict[str, dict], cid: str) -> str:
    return (concepts.get(cid) or {}).get("text") or cid


def question_concept_sets(
    questions: dict[str, dict],
    concepts: dict[str, dict],
    canon: dict[str, str],
) -> dict[str, list[str]]:
    """Per Question: its canonical Concepts, deduplicated, sorted."""
    out: dict[str, list[str]] = {}
    for qid, q in questions.items():
        ids = {
            canon[cid] for cid in (q.get("concepts") or []) if cid in concepts
        }
        out[qid] = sorted(ids)
    return out


def derive_edges(
    q_concepts: dict[str, list[str]],
) -> dict[tuple[str, str], list[str]]:
    """Unordered Concept pair -> the Question ids touching both, sorted."""
    edges: dict[tuple[str, str], list[str]] = defaultdict(list)
    for qid in sorted(q_concepts):
        for a, b in combinations(q_concepts[qid], 2):
            edges[(a, b)].append(qid)
    return {pair: sorted(qids) for pair, qids in edges.items()}


def weighted_degree(edges: dict[tuple[str, str], list[str]]) -> dict[str, int]:
    deg: dict[str, int] = defaultdict(int)
    for (a, b), qids in edges.items():
        deg[a] += len(qids)
        deg[b] += len(qids)
    return dict(deg)


def dominant_domain(
    questions: dict[str, dict],
    domains: dict[str, dict],
    q_concepts: dict[str, list[str]],
) -> dict[str, str]:
    """Per canonical Concept: the Domain most of its Questions are live in.

    Counted over the Questions touching the Concept, one vote per
    (Question, Domain) pair. Ties break on the Domain id, so the answer is
    fixed by the data alone. A Concept whose Questions name no Domain is
    absent from the result.
    """
    tally: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for qid, cids in q_concepts.items():
        dids = [d for d in (questions[qid].get("domains") or []) if d in domains]
        for cid in cids:
            for did in dids:
                tally[cid][did] += 1
    out: dict[str, str] = {}
    for cid, counts in tally.items():
        out[cid] = min(sorted(counts), key=lambda d: (-counts[d], d))
    return out


def voice_numbering(voices: dict[str, dict]) -> dict[str, int]:
    """One stable number per Voice, sorted by id.

    The one numbering for the whole page (owner ruling 2026-09-30): every
    view that needs to show an anonymous "Voice N" label calls this same
    function rather than inventing its own, so a Voice reads the same
    number in the Graph panel's Claim list and the Matrix's columns.
    """
    return {vid: i + 1 for i, vid in enumerate(sorted(voices))}


def walk_payload(
    questions: dict[str, dict],
    positions: dict[str, dict],
    arguments: dict[str, dict],
    claims: dict[str, dict],
    voices: dict[str, dict],
    sources: dict[str, dict],
    values: dict[str, dict],
    domains: dict[str, dict],
) -> dict:
    """Everything the Concept panel needs to open a Question in full.

    Calls `voice_numbering()` for its Claim numbers and also returns that
    same mapping as `voice_number`, so a caller that only wants the
    numbering (page.py, for the page's top-level shared field) does not
    have to reach into this payload's internals for it.
    """
    args_by_position: dict[str, list[str]] = defaultdict(list)
    for aid, a in arguments.items():
        args_by_position[a.get("position")].append(aid)

    claims_by_position: dict[str, list[str]] = defaultdict(list)
    for cid, c in claims.items():
        pid = c.get("position")
        if pid in positions and c.get("voice") in voices:
            claims_by_position[pid].append(cid)

    voice_number = voice_numbering(voices)

    positions_out: dict[str, dict] = {}
    for pid, p in positions.items():
        args = []
        for aid in sorted(args_by_position.get(pid, [])):
            a = arguments[aid]
            args.append(
                {
                    "side": a.get("side"),
                    "text": a.get("text"),
                    "values": [
                        values[v]["text"] for v in (a.get("values") or []) if v in values
                    ],
                }
            )
        cl = []
        for cid in sorted(claims_by_position.get(pid, [])):
            c = claims[cid]
            src = sources.get(c.get("source")) or {}
            cl.append(
                {
                    "voice": c["voice"],
                    "n": voice_number[c["voice"]],
                    "date": c.get("date"),
                    "paraphrase": c.get("paraphrase"),
                    "quote": c.get("quote"),
                    "checked": bool(c.get("checked")),
                    "source": {"title": src.get("title"), "url": src.get("url")},
                }
            )
        cl.sort(key=lambda r: (r["date"] or "", r["n"]))
        positions_out[pid] = {
            "question": p.get("question"),
            "summary": p.get("summary"),
            "tag": p.get("tag"),
            "arguments": args,
            "claims": cl,
        }

    pos_by_question: dict[str, list[str]] = defaultdict(list)
    for pid, p in positions.items():
        if p.get("question") in questions:
            pos_by_question[p["question"]].append(pid)

    questions_out = {
        qid: {
            "text": q.get("text"),
            "positions": sorted(pos_by_question.get(qid, [])),
            "domains": [d for d in (q.get("domains") or []) if d in domains],
        }
        for qid, q in questions.items()
    }

    return {
        "questions": questions_out,
        "positions": positions_out,
        "voice_names": {vid: (v.get("name") or vid) for vid, v in voices.items()},
        "domains": {did: (d.get("text") or did) for did, d in domains.items()},
        "voice_number": voice_number,
    }
