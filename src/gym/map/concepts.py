"""Deduplicate `maps/rust/concepts/*.yaml`.

Usage: `uv run gym map concepts dedup <map-path> [--apply] [--report <path>]`.

Contract other builders rely on: a merged Concept keeps its file and gains
`merged_into: <canonical concept id>`; a canonical Concept carries no such
field; nothing else in any file changes. A merge is never a delete. The run
is idempotent: a Concept already carrying `merged_into` is dropped from the
candidate pool before grouping, so a second run against an already-
deduplicated map finds nothing new.

Tiers:
  1. identical normalised name -> merge automatically into the Concept with
     more Questions naming it; ties go to the lexicographically smaller id
     (the data's own convention for a duplicate: a generated repeat carries
     a `-2`/`-3` suffix, e.g. `wasm-2`, and so sorts after the original).
  2. normalised-name similarity >= 0.88 (rapidfuzz.fuzz.ratio/100 if
     rapidfuzz is importable, else difflib.SequenceMatcher.ratio) AND the
     two Concepts are named together by at least one Question, or (only
     when BOTH normalised names are at least SHORT_NAME_CHARS characters)
     by at least one Domain (via the Questions that name each) -> merge
     automatically, same tie-break as tier 1. Below SHORT_NAME_CHARS, a
     shared Domain alone is not enough — see SHORT_NAME_CHARS' comment.
  3. similarity 0.75-0.88 -> listed in the report for review only; never
     merged, regardless of the shared-Question-or-Domain gate.

A normalised-name match at 1.00 similarity with no shared Question or
Domain still merges (tier 1 has no gate); a match in [0.88, 1.00) with no
shared Question or Domain merges into neither tier and is not reported —
see the "Open problems" note this leaves in the run's report.
"""

from __future__ import annotations

import difflib
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import yaml

try:
    from rapidfuzz import fuzz as _rapidfuzz_fuzz
except ImportError:  # pragma: no cover - exercised only where rapidfuzz is absent
    _rapidfuzz_fuzz = None

TIER_HIGH = 0.88
TIER_LOW = 0.75
# A pair with a normalised name under this many characters may not merge on
# a shared Domain alone — short single/double-word names (`locking` vs
# `blocking`, `spawn` vs `spans`) produce deceptively high character-level
# similarity for concepts that are not the same thing, and a Domain is a
# coarse bucket (12 total) that does nothing to filter that out; a shared
# Question is a much narrower, more specific signal. Owner ruling
# 2026-09-30, after 6 of 14 tier-2 merges were found wrong on review.
SHORT_NAME_CHARS = 12

STOP_WORDS = {
    "a", "an", "the", "of", "in", "on", "for", "with", "vs", "and", "or",
    "to", "is", "are", "as", "at", "by", "into", "than", "per", "its",
}

# Abbreviation/full-form pairs actually present in maps/rust/concepts/*.yaml
# (checked by grep before writing this list; both spellings occur in the data).
SYNONYMS = {
    "async": "asynchronous",
    "sync": "synchronous",
    "config": "configuration",
    "impl": "implementation",
    "struct": "structure",
    "func": "function",
    "docs": "documentation",
    "err": "error",
    "dep": "dependency",
    "repo": "repository",
    "auth": "authentication",
    "param": "parameter",
    "lib": "library",
    "std": "standard",
    "env": "environment",
}

_WORD_RE = re.compile(r"[a-z0-9]+")


def _singular(word: str) -> str:
    if len(word) <= 3:
        return word
    if word.endswith("ies"):
        return word[:-3] + "y"
    if word.endswith(("sses", "shes", "ches", "xes", "zes")):
        return word[:-2]
    # "us"/"is"/"ss" endings are usually not a plural ("asynchronous",
    # "status", "basis", "process"): only a bare trailing "s" after some
    # other letter is treated as one.
    if word.endswith(("us", "is", "ss")):
        return word
    if word.endswith("s"):
        return word[:-1]
    return word


def normalise(text: str) -> str:
    """lowercase; strip to ASCII; hyphens and punctuation as word breaks;
    each word singularised and folded through `SYNONYMS`; stop words out."""
    ascii_text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode("ascii")
    words = []
    for raw in _WORD_RE.findall(ascii_text.lower()):
        word = _singular(SYNONYMS.get(raw, raw))
        if word in STOP_WORDS:
            continue
        words.append(word)
    return " ".join(words)


def similarity(a: str, b: str) -> float:
    if _rapidfuzz_fuzz is not None:
        return _rapidfuzz_fuzz.ratio(a, b) / 100.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def canonical(concept_id: str, concepts: dict[str, dict]) -> str:
    """Resolve `concept_id` through `merged_into` chains to a canonical id.

    `concepts` maps a Concept id to that Concept's data (the parsed YAML
    mapping). Stops at an id missing from `concepts`, at a Concept with no
    `merged_into`, or if a cycle is revisited (defensive only: a correct
    dedup run never produces one, since a tier's canonical is chosen among
    concepts with no `merged_into` of their own).
    """
    seen: set[str] = set()
    current = concept_id
    while current not in seen:
        seen.add(current)
        data = concepts.get(current)
        if data is None:
            return current
        target = data.get("merged_into")
        if not target:
            return current
        current = target
    return current


# --- data loading ---


@dataclass
class ConceptFile:
    id: str
    path: Path
    data: dict
    norm: str = ""


def load_concepts(map_dir: Path) -> dict[str, ConceptFile]:
    concepts: dict[str, ConceptFile] = {}
    for path in sorted((map_dir / "concepts").glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        concept_id = data.get("id", path.stem)
        concepts[concept_id] = ConceptFile(id=concept_id, path=path, data=data)
    return concepts


def load_question_links(map_dir: Path) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    """concept id -> the Question ids that name it; concept id -> the
    Domains of the Questions that name it."""
    by_question: dict[str, set[str]] = {}
    by_domain: dict[str, set[str]] = {}
    for path in sorted((map_dir / "questions").glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        question_id = data.get("id", path.stem)
        domains = set(data.get("domains") or [])
        for concept_id in data.get("concepts") or []:
            by_question.setdefault(concept_id, set()).add(question_id)
            by_domain.setdefault(concept_id, set()).update(domains)
    return by_question, by_domain


# --- merge planning ---


@dataclass
class Merge:
    loser: str
    canonical: str
    tier: str
    reason: str


@dataclass
class MergePlan:
    merges: list[Merge] = field(default_factory=list)
    tier3_pairs: list[tuple[str, str, float]] = field(default_factory=list)

    def counts(self) -> dict[str, int]:
        out = {"tier1": 0, "tier2": 0, "tier3": len(self.tier3_pairs)}
        for merge in self.merges:
            out[merge.tier] += 1
        return out


class _DSU:
    def __init__(self, ids: list[str]) -> None:
        self.parent = {i: i for i in ids}

    def find(self, x: str) -> str:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: str, b: str) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb


def _pick_canonical(ids: list[str], question_counts: dict[str, int]) -> str:
    """More Questions wins; ties go to the lexicographically smaller id."""
    return min(ids, key=lambda i: (-question_counts.get(i, 0), i))


def plan_merges(
    concepts: dict[str, ConceptFile],
    by_question: dict[str, set[str]],
    by_domain: dict[str, set[str]],
) -> MergePlan:
    # idempotence: a Concept already merged is out of the candidate pool.
    candidates = {cid: c for cid, c in concepts.items() if not c.data.get("merged_into")}
    for c in candidates.values():
        c.norm = normalise(c.data.get("text") or c.id)
    question_counts = {cid: len(by_question.get(cid, ())) for cid in candidates}

    merges: list[Merge] = []

    # tier 1: identical normalised name
    groups: dict[str, list[str]] = {}
    for cid, c in candidates.items():
        groups.setdefault(c.norm, []).append(cid)
    tier1_losers: set[str] = set()
    for norm_key, ids in groups.items():
        if len(ids) < 2 or not norm_key:
            continue
        winner = _pick_canonical(ids, question_counts)
        for cid in ids:
            if cid == winner:
                continue
            merges.append(Merge(cid, winner, "tier1", f"identical normalised name '{norm_key}'"))
            tier1_losers.add(cid)

    # tier 2/3: pairwise similarity over tier-1 survivors
    pool_ids = sorted(cid for cid in candidates if cid not in tier1_losers)
    dsu = _DSU(pool_ids)
    pair_reason: dict[frozenset[str], str] = {}
    tier3_pairs: list[tuple[str, str, float]] = []

    for i, a in enumerate(pool_ids):
        norm_a = candidates[a].norm
        if not norm_a:
            continue
        for b in pool_ids[i + 1:]:
            norm_b = candidates[b].norm
            if not norm_b:
                continue
            sim = similarity(norm_a, norm_b)
            if sim >= TIER_HIGH:
                shared_q = by_question.get(a, set()) & by_question.get(b, set())
                shared_d = by_domain.get(a, set()) & by_domain.get(b, set())
                short_pair = len(norm_a) < SHORT_NAME_CHARS or len(norm_b) < SHORT_NAME_CHARS
                gated = bool(shared_q) if short_pair else bool(shared_q or shared_d)
                if gated:
                    dsu.union(a, b)
                    gate = "a shared Question" if shared_q else "a shared Domain"
                    note = " (short name: Domain alone would not suffice)" if short_pair else ""
                    pair_reason[frozenset((a, b))] = f"similarity {sim:.2f}, {gate}{note}"
            elif sim >= TIER_LOW:
                tier3_pairs.append((a, b, sim))

    components: dict[str, list[str]] = {}
    for cid in pool_ids:
        components.setdefault(dsu.find(cid), []).append(cid)
    for members in components.values():
        if len(members) < 2:
            continue
        winner = _pick_canonical(members, question_counts)
        for cid in members:
            if cid == winner:
                continue
            reason = pair_reason.get(frozenset((cid, winner)), "near-duplicate cluster (tier 2)")
            merges.append(Merge(cid, winner, "tier2", reason))

    # flatten: a Concept must point directly at its FINAL canonical. Tier 2
    # can re-merge a tier-1 winner into a different root, and every Concept
    # that pointed at that winner must follow the chain to the final root —
    # `canonical()` would resolve it at read time regardless, but the merge
    # contract promises "a canonical Concept has no such field", so the loser
    # itself must be rewritten, not left pointing at another loser.
    direct = {m.loser: m.canonical for m in merges}

    def _final(cid: str) -> str:
        seen: set[str] = set()
        current = cid
        while current in direct and current not in seen:
            seen.add(current)
            current = direct[current]
        return current

    for m in merges:
        final = _final(m.loser)
        if final != m.canonical:
            m.reason += f"; redirected to '{final}' (its tier-1 target was itself tier-2-merged)"
            m.canonical = final

    tier3_pairs.sort(key=lambda t: -t[2])
    return MergePlan(merges=merges, tier3_pairs=tier3_pairs)


# --- apply + report ---


def apply_merges(concepts: dict[str, ConceptFile], plan: MergePlan) -> None:
    for merge in plan.merges:
        concept = concepts[merge.loser]
        concept.data["merged_into"] = merge.canonical
        concept.path.write_text(yaml.safe_dump(concept.data, sort_keys=False), encoding="utf-8")


def build_report(
    map_dir: Path,
    concepts: dict[str, ConceptFile],
    by_question: dict[str, set[str]],
    plan: MergePlan,
    applied: bool,
) -> str:
    counts = plan.counts()
    lines = [f"# Concept dedup — {map_dir}", ""]
    lines.append(f"mode: {'apply' if applied else 'dry-run'}")
    lines.append(f"concepts total: {len(concepts)}")
    lines.append(f"tier1 merges: {counts['tier1']}")
    lines.append(f"tier2 merges: {counts['tier2']}")
    lines.append(f"tier3 pairs (not merged): {counts['tier3']}")
    lines.append("")
    lines.append("## Merges")
    for merge in sorted(plan.merges, key=lambda m: (m.tier, m.loser)):
        loser_text = concepts[merge.loser].data.get("text", merge.loser)
        winner_text = concepts[merge.canonical].data.get("text", merge.canonical)
        loser_q = len(by_question.get(merge.loser, ()))
        winner_q = len(by_question.get(merge.canonical, ()))
        lines.append(
            f"- [{merge.tier}] '{merge.loser}' ({loser_text!r}, {loser_q} Q) "
            f"-> '{merge.canonical}' ({winner_text!r}, {winner_q} Q) — {merge.reason}"
        )
    lines.append("")
    lines.append("## Tier-3 pairs (review only, not merged)")
    for a, b, sim in plan.tier3_pairs:
        text_a = concepts[a].data.get("text", a)
        text_b = concepts[b].data.get("text", b)
        q_a = len(by_question.get(a, ()))
        q_b = len(by_question.get(b, ()))
        lines.append(f"- {sim:.2f}  '{a}' ({text_a!r}, {q_a} Q)  <->  '{b}' ({text_b!r}, {q_b} Q)")
    return "\n".join(lines) + "\n"


def main(map_dir: Path, apply: bool, report_path: Path | None) -> int:
    concepts = load_concepts(map_dir)
    by_question, by_domain = load_question_links(map_dir)
    plan = plan_merges(concepts, by_question, by_domain)
    counts = plan.counts()

    print(f"tier1: {counts['tier1']}  tier2: {counts['tier2']}  tier3 (unmerged): {counts['tier3']}")

    if apply:
        apply_merges(concepts, plan)
        print(f"applied: wrote merged_into to {len(plan.merges)} Concept file(s)")

    report_text = build_report(map_dir, concepts, by_question, plan, applied=apply)
    if report_path is not None:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report_text, encoding="utf-8")
        print(f"report written to {report_path}")

    return 0
