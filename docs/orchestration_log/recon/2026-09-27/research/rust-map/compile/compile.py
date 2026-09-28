"""Compile the Rust map's data layer v0.1 from batch 1's resolved outputs.
Transcribes only; every value traced to a named input file. See
RECON/compile/compile-b1.md for known issues and gap accounting.
"""
import csv
import re
import glob
import yaml
from pathlib import Path
from urllib.parse import urlparse
from collections import Counter, defaultdict

RECON = Path("/Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27/research/rust-map")
MAP = Path("/Users/ryzhakar/pp/gym/maps/rust")

VALID_DOMAINS = {"web", "distributed", "decentralized-iroh", "ml", "desktop-cli-ui",
                 "swift-interop", "frontend", "cloud-workers", "wasm", "embedded", "core", "other"}
VALUE_IDS = {"approachability", "correctness", "iteration-speed", "performance", "simplicity", "stability"}

issues = []  # (topic, detail) pairs for compile-b1.md


def slugify(s: str, max_len: int = 60) -> str:
    s = s.strip().lower()
    s = re.sub(r"[`'\"]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    s = s or "x"
    if len(s) > max_len:
        s = s[:max_len].rsplit("-", 1)[0]
    return s


class IdRegistry:
    def __init__(self):
        self.by_id = {}  # id -> kind

    def reserve(self, kind, id_):
        self.by_id[id_] = kind

    def register(self, kind, base_id):
        # Every call is a genuinely new entity (callers only register on first
        # sight of a distinct name/phrase/id) — so ANY existing occupant of the
        # slug, same kind or not, is a collision that must not silently merge.
        cand = base_id
        n = 2
        while cand in self.by_id:
            cand = f"{base_id}-{n}"
            n += 1
        if cand != base_id:
            issues.append(("id-collision", f"{kind} '{base_id}' collided with existing {self.by_id[base_id]}; renamed to '{cand}'"))
        self.by_id[cand] = kind
        return cand


registry = IdRegistry()
for d in VALID_DOMAINS:
    registry.reserve("domain", d)
for v in VALUE_IDS:
    registry.reserve("value", v)

# ---------------------------------------------------------------------------
# 1. Parse merged-questions-b1.md: text, domains, concepts per canonical question
# ---------------------------------------------------------------------------

mq_text = (RECON / "merge-v3" / "merged-questions-b1.md").read_text(encoding="utf-8")
mq_start = mq_text.index("## Canonical Questions")
mq_sections = re.split(r"^### ", mq_text[mq_start:], flags=re.M)[1:]

questions = {}  # qid -> {text, domains, concepts_phrases, notes}
concept_phrase_first_text = {}  # phrase -> original text (first seen)

for sec in mq_sections:
    qid = re.match(r"^`([^`]+)`", sec).group(1)
    registry.reserve("question", qid)
    qtext = re.search(r"^\*\*Question\.\*\* (.*?)$", sec, re.M).group(1)
    dom_line = re.search(r"^- Domains: (.*)$", sec, re.M).group(1)
    con_line = re.search(r"^- Concepts: (.*)$", sec, re.M).group(1)
    domains_raw = [d.strip() for d in dom_line.split(",")]
    notes = None
    domains = []
    for d in domains_raw:
        if d in VALID_DOMAINS:
            domains.append(d)
        else:
            notes = f"Domain not established: merged-questions-b1.md states '{d}' (no team-local member)."
    concepts_phrases = [c.strip() for c in con_line.split(";") if c.strip()]
    for c in concepts_phrases:
        concept_phrase_first_text.setdefault(c, c)
    questions[qid] = dict(text=qtext, domains=domains, concepts_phrases=concepts_phrases, notes=notes)

issues.append(("questions-parsed", f"{len(questions)} canonical Questions parsed from merged-questions-b1.md"))

# ---------------------------------------------------------------------------
# 2. Parse positions-final-b1.md: per-question positions with summary/tag/claims
# ---------------------------------------------------------------------------

pf_text = (RECON / "fill" / "positions-final-b1.md").read_text(encoding="utf-8")
pf_lines = pf_text.splitlines()

positions = {}  # pid -> {question, label, summary, tag_or_None, claims:[ids]}
i = 0
cur_qid = None
while i < len(pf_lines):
    line = pf_lines[i]
    mq = re.match(r"^## Question `([^`]+)`$", line)
    if mq:
        cur_qid = mq.group(1)
        i += 1
        continue
    mp = re.match(r"^### (\S+) — (.*)$", line)
    if mp:
        pid, label = mp.groups()
        registry.reserve("position", pid)
        j = i + 1
        block = []
        while j < len(pf_lines) and not pf_lines[j].startswith("### ") and not pf_lines[j].startswith("## "):
            block.append(pf_lines[j])
            j += 1
        blocktext = "\n".join(block)
        summary_m = re.search(r"^Summary: (.*?)(?:\n\n|\Z)", blocktext, re.S | re.M)
        tag_m = re.search(r"^Tag: (\S+)", blocktext, re.M)
        claims_m = re.search(r"^Claims: (.*)$", blocktext, re.M)
        tag = tag_m.group(1) if tag_m else None
        if tag == "unresolved":
            tag = None
            issues.append(("tag-unresolved", f"position '{pid}': fill-tag resolution was a three-way split or ambiguous single-run vote (resolve-b1.md); tag omitted (schema enum has no 'unresolved' value)."))
        claim_ids = [c.strip() for c in claims_m.group(1).split(",")] if claims_m and claims_m.group(1).strip() else []
        positions[pid] = dict(question=cur_qid, label=label,
                               summary=summary_m.group(1).strip() if summary_m else "",
                               tag=tag, claims=claim_ids)
        i = j
        continue
    i += 1

issues.append(("positions-parsed", f"{len(positions)} Positions parsed from positions-final-b1.md"))

# ---------------------------------------------------------------------------
# 3. Owner/lead override: a-sa30-f013276-c5 is unresolved (resolve-b1.md's
#    blinding-lapse adjudication flag), overriding its resolved-b1.csv 'final'
#    value of dyn-compatibility-rules-relaxation--p2.
# ---------------------------------------------------------------------------

OVERRIDE_UNRESOLVED = {"a-sa30-f013276-c5"}
EXCLUDE_NONE = set()

claim_to_position = {}
for pid, p in positions.items():
    kept = []
    for cid in p["claims"]:
        if cid in OVERRIDE_UNRESOLVED:
            issues.append(("adjudication-override", f"claim '{cid}' removed from position '{pid}' and marked position: unresolved per lead ruling (resolve-b1.md: blinding lapse on this row; adjudicator flag)."))
            claim_to_position[cid] = "unresolved"
            continue
        kept.append(cid)
        claim_to_position[cid] = pid
    p["claims"] = kept

# ---------------------------------------------------------------------------
# 4. Parse resolved-b1.csv to find claims positions-final-b1.md left unplaced:
#    final == 'none' (excluded) or 'unresolved' (native).
# ---------------------------------------------------------------------------

resolved_rows = []
with open(RECON / "fill" / "resolved-b1.csv", encoding="utf-8") as f:
    header = f.readline()
    for line in f:
        parts = line.rstrip("\n").split(",")
        claim_id, question_id, run_a, run_b, third, final, status = parts
        resolved_rows.append(dict(claim_id=claim_id, question_id=question_id, final=final, status=status))

for row in resolved_rows:
    cid, final = row["claim_id"], row["final"]
    if cid in claim_to_position:
        continue  # already placed via positions-final-b1.md (or overridden)
    if final == "none":
        EXCLUDE_NONE.add(cid)
        issues.append(("excluded-none", f"claim '{cid}' (question '{row['question_id']}'): resolved-b1.csv final='none' (supports no Position); schema's position field allows only a Position id or the literal 'unresolved', so this claim is excluded from the map."))
    elif final == "unresolved":
        claim_to_position[cid] = "unresolved"
    else:
        issues.append(("anomaly", f"claim '{cid}' final='{final}' not found in positions-final-b1.md and not none/unresolved — anomaly, excluded"))
        EXCLUDE_NONE.add(cid)

issues.append(("resolved-csv-rows", f"{len(resolved_rows)} rows read from resolved-b1.csv"))

# ---------------------------------------------------------------------------
# 5. Parse input-b1-*.md: per-claim voice/source/date/locator/quote/paraphrase
# ---------------------------------------------------------------------------

CLAIM_RE = re.compile(r"^- `([^`]+)` · Voice: (.*?) · Source: (.*?) · Date: (.*?) · Locator: (.*)$")
SRC_RE = re.compile(r"^(\S+) \(`([^`]+)`\)$")

claim_meta = {}
for fp in sorted(glob.glob(str(RECON / "fill" / "input-b1-*.md"))):
    lines = Path(fp).read_text(encoding="utf-8").splitlines()
    k = 0
    while k < len(lines):
        m = CLAIM_RE.match(lines[k])
        if m:
            cid, voice_raw, source_raw, date_raw, locator = m.groups()
            src_m = SRC_RE.match(source_raw.strip())
            src_url, src_frame = src_m.groups() if src_m else (source_raw.strip(), None)
            quote = None
            paraphrase = None
            j = k + 1
            while j < len(lines) and lines[j].startswith("  - "):
                if lines[j].startswith("  - Quote: "):
                    quote = lines[j][len("  - Quote: "):].strip()
                    if quote.startswith('"') and quote.endswith('"'):
                        quote = quote[1:-1]
                elif lines[j].startswith("  - Paraphrase: "):
                    paraphrase = lines[j][len("  - Paraphrase: "):].strip()
                j += 1
            voice_unverified = "[voice-unverified]" in voice_raw
            voice_name = voice_raw.replace("[voice-unverified]", "").strip()
            voice_caveat = None
            if " — " in voice_name:
                voice_name, voice_caveat = voice_name.split(" — ", 1)
                voice_name = voice_name.strip()
                voice_caveat = voice_caveat.strip()
            claim_meta[cid] = dict(voice_name=voice_name, voice_unverified=voice_unverified,
                                    voice_caveat=voice_caveat,
                                    source_url=src_url, source_frame=src_frame,
                                    date_raw=date_raw.strip(), locator=locator.strip(),
                                    quote=quote, paraphrase=paraphrase, file=Path(fp).name)
            k = j
        else:
            k += 1

issues.append(("claims-parsed", f"{len(claim_meta)} Claim metadata records parsed from input-b1-*.md"))

# ---------------------------------------------------------------------------
# 6. Date normalization
#
# Rule (lead ruling, this pass): normalize to ISO where the input's date is
# unambiguous (month names, full dates); where only a year or month is known,
# or the source states no date at all, leave the field unset and list it.
# Never guess a day. Three small classes of "non-ISO but a full date is
# actually stated somewhere in the string" are resolved by exact claim id
# (auditable, not a regex guess): a Wayback capture date, a stated repost
# date, and one claim whose Date field names the day its own retrospective
# post was published. Every other non-ISO Date is either day-precision but
# oddly punctuated (handled mechanically below) or lacks day precision
# entirely (left unset).
# ---------------------------------------------------------------------------

ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ISO_PREFIX = re.compile(r"^(\d{4}-\d{2}-\d{2})(.*)$")

# Claim id -> (iso date, gap note or None). The original is undated; the date
# used is a stand-in (an archive capture, or a repost) named directly in the
# claim's own Date field.
WAYBACK_OR_REPOST_DATES = {
    "a-sB01-f000217-c5": ("2025-01-21", "date is a Wayback capture timestamp, not the underlying document's own date"),
    "a-sB01-f000217-c3": ("2025-01-15", "date is a Wayback capture timestamp, not the underlying document's own date"),
    "a-sB01-f000217-c1": ("2025-02-16", "date is a Wayback capture timestamp, not the underlying document's own date"),
    "a-sB01-f000217-c4": ("2025-03-22", "date is a Wayback capture timestamp, not the underlying document's own date"),
    "a-sB01-f000217-c2": ("2025-01-21", "date is a Wayback capture timestamp, not the underlying document's own date"),
    "a-sa28-f012469-c5": ("2015-09-01", "date is the item's repost date; the original is undated in source"),
    "a-sa28-f012469-c11": ("2015-04-27", "date is the item's repost date; the original is undated in source"),
    "a-sa28-f012469-c12": ("2015-12-14", "date is the item's repost date; the original is undated in source"),
    # The claim itself ("over a decade") is old; the Date field names when the
    # Voice wrote *this* retrospective statement, which is the Claim's own date.
    "a-sa18-f009104-c1": ("2026-09-21", None),
}

n_clean = 0
n_truncated_time = 0
n_truncated_qualifier = 0
n_named_override = 0
n_unset = 0


def normalize_date(raw: str, cid: str):
    global n_clean, n_truncated_time, n_truncated_qualifier, n_named_override, n_unset
    if ISO_DATE.match(raw):
        n_clean += 1
        return raw, None
    m = ISO_PREFIX.match(raw)
    if m:
        rest = m.group(2)
        if rest.startswith("T"):
            n_truncated_time += 1
        else:
            n_truncated_qualifier += 1
            issues.append(("date-qualifier-dropped", f"claim '{cid}': Date field '{raw}' — kept leading date '{m.group(1)}', dropped trailing qualifier '{rest.strip()}'."))
        return m.group(1), None
    if cid in WAYBACK_OR_REPOST_DATES:
        n_named_override += 1
        date_val, note = WAYBACK_OR_REPOST_DATES[cid]
        issues.append(("date-named-override", f"claim '{cid}': Date field '{raw}' — used '{date_val}' (a day-precision date named in the string itself), not the undated original."))
        return date_val, note
    n_unset += 1
    issues.append(("date-unset", f"claim '{cid}': Date field '{raw}' carries no day-precision date (year/month only, or the source states no date); date field left unset rather than guessed."))
    return None, None


# ---------------------------------------------------------------------------
# 7. Build Voices, Sources, Concepts registries + Claim records
# ---------------------------------------------------------------------------

def truncate_quote(q: str, limit: int = 300, ellipsis: str = "…") -> str:
    """Cut at a word boundary to the schema's cap, plus an ellipsis. The
    paraphrase (a separate, already-authored field) carries the rest of the
    meaning; this never rewrites or summarizes — it only shortens verbatim
    text at a word break."""
    if len(q) <= limit:
        return q
    budget = limit - len(ellipsis) - 1  # 1 for the space before the ellipsis
    cut = q[:budget]
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    cut = cut.rstrip(" ,;:—-")
    return f"{cut} {ellipsis}"


voice_id_by_name = {}   # exact name string -> id
voices = {}             # id -> {name}

source_by_frame = {}    # frame_id -> {url, teams:set}
n_quotes_truncated = 0

concept_id_by_phrase = {}
concepts = {}           # id -> {text}

claims_out = {}         # id -> data dict

all_claim_ids = set(claim_meta.keys())
placed_or_unresolved = set(claim_to_position.keys())
unaccounted = all_claim_ids - placed_or_unresolved - EXCLUDE_NONE
if unaccounted:
    issues.append(("anomaly-unaccounted", f"{len(unaccounted)} claims parsed from input files have no position/unresolved/excluded disposition: {sorted(unaccounted)[:10]}"))

for cid, meta in claim_meta.items():
    if cid in EXCLUDE_NONE:
        continue
    pos = claim_to_position.get(cid)
    if pos is None:
        continue  # already flagged above as anomaly

    # Voice
    vname = meta["voice_name"]
    if vname not in voice_id_by_name:
        vid = registry.register("voice", slugify(vname))
        voice_id_by_name[vname] = vid
        voices[vid] = dict(name=vname)
    vid = voice_id_by_name[vname]

    # Source
    frame = meta["source_frame"]
    if frame is None:
        issues.append(("source-unparsed", f"claim '{cid}': Source field '{meta['source_url']}' has no frame id in backticks; claim excluded (no valid source relation)"))
        continue
    team = cid.split("-")[0]
    if frame not in source_by_frame:
        registry.reserve("source", frame)
        source_by_frame[frame] = dict(url=meta["source_url"], teams={team})
    else:
        rec = source_by_frame[frame]
        if rec["url"] != meta["source_url"]:
            issues.append(("source-url-mismatch", f"source '{frame}': claim '{cid}' states url '{meta['source_url']}' but source already registered with '{rec['url']}'; first-seen url kept."))
        rec["teams"].add(team)

    date_final, date_gap_note = normalize_date(meta["date_raw"], cid)

    claim_data = dict(
        id=cid,
        voice=vid,
        position=pos,
        source=frame,
    )
    if date_final is not None:
        claim_data["date"] = date_final
    claim_data["locator"] = meta["locator"]
    claim_data["paraphrase"] = meta["paraphrase"]
    if meta["quote"]:
        quote = meta["quote"]
        if len(quote) > 300:
            n_quotes_truncated += 1
            truncated = truncate_quote(quote)
            issues.append(("quote-truncated", f"claim '{cid}': quote was {len(quote)} characters, cut at a word boundary to {len(truncated)} (schema cap 300); the paraphrase carries the rest."))
            quote = truncated
        claim_data["quote"] = quote
    gap_parts = []
    if meta["voice_unverified"]:
        gap_parts.append("voice-unverified")
    if meta["voice_caveat"]:
        gap_parts.append(meta["voice_caveat"])
        issues.append(("voice-caveat", f"claim '{cid}': input's Voice field carried an inline eligibility caveat beyond the name; name truncated to '{vname}', caveat moved to claim.gap."))
    if date_gap_note:
        gap_parts.append(date_gap_note)
    if gap_parts:
        claim_data["gap"] = "; ".join(gap_parts)
    claims_out[cid] = claim_data

issues.append(("claims-written", f"{len(claims_out)} Claim entities to write"))
issues.append(("voices-written", f"{len(voices)} Voice entities to write"))
issues.append(("sources-written", f"{len(source_by_frame)} Source entities to write"))

# Concepts (from question concept phrases)
for qid, q in questions.items():
    ids = []
    for phrase in q["concepts_phrases"]:
        if phrase not in concept_id_by_phrase:
            cid_ = registry.register("concept", slugify(phrase))
            concept_id_by_phrase[phrase] = cid_
            concepts[cid_] = dict(text=phrase)
        ids.append(concept_id_by_phrase[phrase])
    q["concept_ids"] = ids

issues.append(("concepts-written", f"{len(concepts)} Concept entities to write"))

# ---------------------------------------------------------------------------
# 7b. Source enrichment: title/kind/date/language from the frame registry
#     (lead ruling, this pass). Matched by frame id first, URL second.
# ---------------------------------------------------------------------------

FRAME_REGISTRY_FILES = [
    RECON / "frame" / "frame.csv",
    RECON / "frame" / "frame-older.csv",
    RECON / "frame" / "frame-v2-nonen.csv",
    RECON / "samples" / "batch-1-team-a.csv",
    RECON / "samples" / "batch-1-team-b.csv",
]


def load_frame_registry():
    by_id = {}
    by_url = {}
    for fp in FRAME_REGISTRY_FILES:
        with open(fp, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                fid = row.get("frame_id") or row.get("id")
                if fid and fid not in by_id:
                    by_id[fid] = row
                url = row.get("url")
                if url and url not in by_url:
                    by_url[url] = row
    return by_id, by_url


frame_by_id, frame_by_url = load_frame_registry()

# class -> kind, direct where the class is unambiguous.
CLASS_KIND = {"books-courses": "book", "talks": "talk", "rfc": "rfc", "survey": "survey"}
TALK_HOSTS = {"youtube.com", "www.youtube.com", "bilibili.com", "www.bilibili.com"}
THREAD_HOSTS = {"internals.rust-lang.org", "users.rust-lang.org", "lobste.rs", "news.ycombinator.com"}


def classify_kind(url: str, klass: str) -> str:
    """kind from the frame's class column (lead ruling). Most classes name
    the kind directly; 'domain-subframes', 'hn-lobsters', 'individual-blogs',
    'twir-links', 'users-forum', 'internals' and 'project-blog' are discovery
    frames whose class names *how the source was found*, not what it is —
    resolved by the referenced URL's own structure (GitHub issue/PR vs. repo,
    known forum host, a single social post, else a post)."""
    klass = klass or ""
    for token, kind in CLASS_KIND.items():
        if token in klass:
            return kind
    host = urlparse(url).netloc
    path = urlparse(url).path
    if host in TALK_HOSTS:
        return "talk"
    if host == "github.com":
        if "/issues/" in path or "/pull/" in path or "/discussions/" in path:
            return "thread"
        return "code"
    if host in THREAD_HOSTS or path.startswith("/t/"):
        return "thread"
    return "post"


n_source_enriched = 0
n_source_not_in_registry = 0
n_source_date_unset = 0

for frame, rec in source_by_frame.items():
    row = frame_by_id.get(frame) or frame_by_url.get(rec["url"])
    if row is None:
        n_source_not_in_registry += 1
        issues.append(("source-not-in-registry", f"source '{frame}' ({rec['url']}): no row in frame.csv/frame-older.csv/frame-v2-nonen.csv/batch-1-team-{{a,b}}.csv by id or url; title/kind/date/language left unset."))
        rec["enrichment"] = None
        continue
    if row.get("url", "").strip() != rec["url"].strip():
        issues.append(("source-registry-url-mismatch", f"source '{frame}': claims state url '{rec['url']}' but the matched registry row's url is '{row['url']}'; both kept as-is (registry match was by id)."))
    kind = classify_kind(row["url"], row.get("class", ""))
    reg_date = (row.get("date") or "").strip()
    date_val = None
    if ISO_DATE.match(reg_date):
        date_val = reg_date
    else:
        m = ISO_PREFIX.match(reg_date)
        if m:
            date_val = m.group(1)
        else:
            n_source_date_unset += 1
            issues.append(("source-date-unset", f"source '{frame}': frame registry date '{reg_date}' carries no day-precision date; date field left unset rather than guessed."))
    n_source_enriched += 1
    rec["enrichment"] = dict(title=row.get("title", "").strip() or None, kind=kind,
                              date=date_val, language=(row.get("language") or "").strip() or None)

issues.append(("source-enrichment", f"{n_source_enriched} Sources enriched from the frame registry; {n_source_not_in_registry} not found in it; {n_source_date_unset} enriched Sources still lack a day-precision date."))

# ---------------------------------------------------------------------------
# 8. Write YAML files
# ---------------------------------------------------------------------------


def dump(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, width=100000, default_flow_style=False)


n_written = Counter()

for qid, q in questions.items():
    data = {"id": qid, "text": q["text"], "concepts": q["concept_ids"], "domains": q["domains"], "status": "open"}
    if q["notes"]:
        data["notes"] = q["notes"]
    dump(MAP / "questions" / f"{qid}.yaml", data)
    n_written["question"] += 1

for pid, p in positions.items():
    data = {"id": pid, "question": p["question"], "summary": p["summary"]}
    if p["tag"]:
        data["tag"] = p["tag"]
    dump(MAP / "positions" / f"{pid}.yaml", data)
    n_written["position"] += 1

for cid, data in claims_out.items():
    dump(MAP / "claims" / f"{cid}.yaml", data)
    n_written["claim"] += 1

for vid, v in voices.items():
    data = {"id": vid, "name": v["name"]}
    dump(MAP / "voices" / f"{vid}.yaml", data)
    n_written["voice"] += 1

for frame, rec in source_by_frame.items():
    teams = sorted(rec["teams"])
    data = {"id": frame, "url": rec["url"]}
    enr = rec.get("enrichment")
    if enr:
        if enr["title"]:
            data["title"] = enr["title"]
        if enr["kind"]:
            data["kind"] = enr["kind"]
        if enr["date"]:
            data["date"] = enr["date"]
        if enr["language"]:
            data["language"] = enr["language"]
    data["frame"] = {"batch": 1, "team": teams[0] if len(teams) == 1 else teams}
    dump(MAP / "sources" / f"{frame}.yaml", data)
    n_written["source"] += 1

for cid_, c in concepts.items():
    data = {"id": cid_, "text": c["text"]}
    dump(MAP / "concepts" / f"{cid_}.yaml", data)
    n_written["concept"] += 1

print("=== written ===")
for k, v in n_written.items():
    print(k, v)

print("\n=== claim date normalization ===")
print("clean:", n_clean, "truncated-time:", n_truncated_time, "truncated-qualifier:", n_truncated_qualifier,
      "named-override:", n_named_override, "left-unset:", n_unset)
print("\n=== quote truncation ===")
print("truncated:", n_quotes_truncated)
print("\n=== source enrichment ===")
print("enriched:", n_source_enriched, "not-in-registry:", n_source_not_in_registry, "still-date-unset:", n_source_date_unset)

print("\n=== issues (count by topic) ===")
topic_counts = Counter(t for t, _ in issues)
for t, n in topic_counts.most_common():
    print(t, n)

# Persist full issues log for compile-b1.md
SCRATCH = Path("/private/tmp/claude-501/-Users-ryzhakar-pp-gym/24588f30-a8bd-46c9-8d8f-3b9d74cdd27f/scratchpad")
SCRATCH.mkdir(parents=True, exist_ok=True)
with open(SCRATCH / "issues.log", "w", encoding="utf-8") as f:
    for t, d in issues:
        f.write(f"{t}\t{d}\n")
