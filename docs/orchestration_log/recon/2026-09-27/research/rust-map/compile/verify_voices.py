"""Apply the Voice-verification pass (RECON/verify/voices-chunk-00..15.md,
voices-calibration.md) onto MAP/voices/ and MAP/claims/. Transcribes only.
See RECON/compile/compile-b1.md for known issues and gap accounting.
"""
import re
import glob
import yaml
from pathlib import Path
from collections import Counter, defaultdict

RECON = Path("/Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27/research/rust-map")
MAP = Path("/Users/ryzhakar/pp/gym/maps/rust")
VALID_TYPES = {"builder", "educator", "language-designer", "institution", "critic", "leaver"}

issues = []


def parse_evidence(text: str):
    """'description — url1[, url2...] (date-ish)' -> (evidence, url, date).
    The first http(s) url found is the primary url; any trailing date
    (YYYY-MM-DD, bare or inside "checked ...") is extracted; everything else
    stays folded back into evidence so nothing stated is dropped."""
    text = text.strip()
    m = re.search(r"https?://\S+", text)
    if not m:
        return text, None, None
    before = text[: m.start()]
    before = re.sub(r"[\s—\-]+$", "", before).strip()
    url = m.group(0).rstrip(").,;”’")
    after = text[m.end():]
    # A trailing "(... YYYY-MM-DD ...)" is dropped whole (it's the researcher's
    # checked/fetched note); a date elsewhere is still captured.
    paren_m = re.search(r"\(([^()]*?)(\d{4}-\d{2}-\d{2})([^()]*?)\)\s*$", after)
    if paren_m:
        date = paren_m.group(2)
        extra = after[: paren_m.start()].strip()
    else:
        date_m = re.search(r"(\d{4}-\d{2}-\d{2})", after)
        date = date_m.group(1) if date_m else None
        extra = (after[: date_m.start()] + after[date_m.end():]).strip(" ()") if date_m else after.strip(" ()")
    evidence = before
    if extra:
        evidence = f"{before} {extra}".strip()
    # Cosmetic only: a date/checked-note parenthetical elsewhere in the text
    # (not at the very end) leaves an empty or comma-only "( )" behind once
    # its date is pulled out; collapse those. Never touches wording.
    evidence = re.sub(r"\(\s*,?\s*\)", "", evidence)
    evidence = re.sub(r"\s{2,}", " ", evidence).strip(" ,")
    return evidence, url, date


# ---------------------------------------------------------------------------
# 1. Parse the 16 chunk files
# ---------------------------------------------------------------------------

FIELD_RE = re.compile(r"^(name|identity|type|verdict|track_record|influence|checked): ?(.*)$")


def parse_chunk_block(block_text: str):
    lines = block_text.splitlines()
    vid = lines[0].strip()
    fields = {"name": "", "type": "unset", "verdict": "UNKNOWN", "track_record": [], "influence": []}
    i = 1
    cur = None
    cur_list_target = None
    while i < len(lines):
        line = lines[i]
        m = FIELD_RE.match(line)
        if m:
            key, rest = m.groups()
            cur = key
            if key in ("name", "type", "verdict"):
                fields[key] = rest.strip()
                cur_list_target = None
            elif key in ("track_record", "influence"):
                cur_list_target = key
                if rest.strip() and not rest.strip().startswith("-"):
                    # single-line "none found ..." variant, or a bare inline value: empty list
                    pass
            elif key == "checked":
                cur_list_target = None
        elif cur_list_target and line.startswith("- "):
            item = line[2:].strip()
            is_placeholder = item.strip("()").lower().startswith("none") and "http" not in item
            if item and not is_placeholder:
                km = re.match(r"^([a-zA-Z][a-zA-Z/,\- ]*?): (.*)$", item)
                if km:
                    kind, rest = km.groups()
                    # "checked <kind>: <negative finding>" bullets (a FAILS
                    # voice's per-kind rule-out, e.g. "checked role: no team
                    # page found") are the same "no evidence" signal as
                    # "(none found)", not a positive track record — as is a
                    # bare "none ..."/"none checkable ..." rest.
                    kind_is_negative_check = kind.strip().lower().startswith("checked")
                    rest_is_placeholder = rest.strip("()").lower().startswith("none") and "http" not in rest
                    if not kind_is_negative_check and not rest_is_placeholder:
                        evidence, url, date = parse_evidence(rest)
                        fields[cur_list_target].append(dict(kind=kind.strip(), evidence=evidence, url=url, date=date))
                else:
                    evidence, url, date = parse_evidence(item)
                    fields[cur_list_target].append(dict(kind=None, evidence=evidence, url=url, date=date))
        i += 1
    return vid, fields


chunk_records = {}
for fp in sorted(glob.glob(str(RECON / "verify" / "voices-chunk-*.md"))):
    text = Path(fp).read_text(encoding="utf-8")
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        vid, fields = parse_chunk_block(block)
        chunk_records[vid] = fields

issues.append(("chunk-parsed", f"{len(chunk_records)} Voice blocks parsed from voices-chunk-00..15.md"))

# ---------------------------------------------------------------------------
# 2. Parse the calibration file's two tables + name corrections
# ---------------------------------------------------------------------------

calib_text = (RECON / "verify" / "voices-calibration.md").read_text(encoding="utf-8")
calib_lines = calib_text.splitlines()

DASH_IDS = set()  # ids whose calibration kind is '-' (no kind holds)
calib_rows = {}  # id -> {"verdict": ..., "kind_cell": ..., "evidence_cell": ...}
section = None
for line in calib_lines:
    if line.startswith("## (a)"):
        section = "a"
        continue
    if line.startswith("## (b)"):
        section = "b"
        continue
    if line.startswith("##"):
        section = None
        continue
    if section and line.startswith("|") and not line.startswith("|---"):
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells[0] == "id":
            continue
        vid, old, new, kind, evurl, reason = cells
        calib_rows[vid] = dict(verdict=new, kind=kind, evidence_cell=evurl, reason=reason)
        if kind == "—":
            DASH_IDS.add(vid)

issues.append(("calibration-rows", f"{len(calib_rows)} ids re-checked in voices-calibration.md"))

# Hand-resolved special cases (compound or ambiguous 'kind' cells; auditable,
# not a generic splitter guessing at free text — see compile-b1.md).
COMPOUND_OVERRIDES = {
    "bryan-cantrill": [
        dict(kind="production", evidence="co-founder/CTO, Oxide's own product", url="https://github.com/oxidecomputer/hubris", date=None),
        dict(kind="role", evidence="co-founder/CTO, Oxide's own product", url="https://github.com/oxidecomputer/hubris", date=None),
    ],
    "playfulfence": [
        dict(kind="production", evidence="espressif tag, esp-hal PR", url="https://github.com/esp-rs/esp-hal/pull/5002", date=None),
        dict(kind="role", evidence="esp-rs org member (single-project org)", url="https://github.com/esp-rs/esp-hal/pull/5002", date=None),
    ],
    "the8472": [
        dict(kind="role", evidence="listed under [people] members in official rust-lang/team files teams/libs.toml and teams/crate-maintainers.toml (also named in libs-fcp.toml, libs-ping.toml, archive/libs-api.toml, compiler.toml); live-confirmed via `gh api`",
             url="https://github.com/rust-lang/team/blob/main/teams/libs.toml", date="2026-09-28"),
        dict(kind="crate-dependents", evidence="owns `btrfs2` (2 real reverse deps) and `platter-walk` (2)",
             url="https://crates.io/api/v1/crates/btrfs2/reverse_dependencies", date=None),
    ],
}
# 'book/course/talk/post' is a grouped label in the calibration table, not a
# schema kind; the specific kind is picked from what the row's own text says
# (a stated "talk" vs. a described paper/publication).
GROUPED_KIND_PICK = {
    "luke-wagner-fastly-w3c-bytecode-alliance-component-model-co": "post",
    "lukewagner": "post",
    "rossberg": "post",
    "wedson-almeida-filho": "talk",
}
SKIP_OVERRIDE = {"steffahn"}  # calibration only re-confirms; chunk's own entry already holds and has a url

calib_overrides = {}  # id -> {"verdict": ..., "track_record": [...] or None (== leave chunk's), "type_unset": bool}
for vid, row in calib_rows.items():
    if vid in SKIP_OVERRIDE:
        continue
    verdict = "MEETS" if row["verdict"] == "MEETS" else "FAILS"
    if vid in DASH_IDS:
        calib_overrides[vid] = dict(verdict=verdict, track_record=[], type_unset=True)
        continue
    if vid in COMPOUND_OVERRIDES:
        calib_overrides[vid] = dict(verdict=verdict, track_record=COMPOUND_OVERRIDES[vid], type_unset=False)
        continue
    kind = GROUPED_KIND_PICK.get(vid, row["kind"])
    evidence, url, date = parse_evidence(row["evidence_cell"])
    if not evidence:
        # the "evidence url" cell was a bare url with no descriptive text;
        # the row's "reason" cell carries the actual description in that case.
        evidence, _, _ = parse_evidence(row["reason"])
        if not evidence:
            evidence = row["reason"]
    calib_overrides[vid] = dict(verdict=verdict, track_record=[dict(kind=kind, evidence=evidence, url=url, date=date)], type_unset=False)

issues.append(("calibration-overrides-built", f"{len(calib_overrides)} ids get a calibration-sourced track_record (steffahn excluded — chunk's own entry already holds)"))

# Name correction
RENAME = {"sam-cutter": "sam-cutler"}
NAME_FIX = {"sam-cutter": "Sam Cutler"}  # applied to whichever id it ends up as

# ---------------------------------------------------------------------------
# 3. Merge clusters (calibration's 14 groups + 4 named in chunk files)
# ---------------------------------------------------------------------------

MERGE_GROUPS = [
    ["arqu", "arqu-n0-computer-iroh-engineer-production-post-mortem-author"],
    ["dignifiedquire", "dignifiedquire-byline-iroh-blog-rust-connection-in-source",
     "dignifiedquire-iroh-n0-computer", "dignifiedquire-n0-computer-iroh-maintainer",
     "iroh-n0-dignifiedquire-post-author"],
    ["bugadani-esp-hal-maintainer", "bugadani-esp-hal-maintainer-pr-author"],
    ["cfallin", "cfallin-chris-fallin"],
    ["felipebalbi", "felipebalbi-nxp-embedded-engineer-embassy-nxp-contributor"],
    ["fitzgen", "fitzgen-bytecode-alliance-wasmtime-core-arbitrary-crate"],
    ["lukewagner", "luke-wagner-fastly-w3c-bytecode-alliance-component-model-co"],
    ["saulecabrera", "saulecabrera-bytecode-alliance-wasmtime-winch-baseline"],
    ["ramfox", "ramfox-byline-iroh-blog-rust-connection-in-source-iroh",
     "ramfox-matheus23", "ramfox-matheus23-iroh-n0-blog-authors"],
    ["jamesmunns", "jamesmunns-embassy-maintainer"],
    ["jakub-ber-nek-on-behalf-of-the-rust-funding-team", "jakub-ber-nek-on-behalf-of-the-rust-project-mentorship-team"],
    ["hannah-wang-ben-yang-and-fisher-darling", "hannah-wang-ben-yang-fisher-darling-cloudflare"],
    ["b5", "dig-b5-and-ramfox-iroh-team"],
    ["r-diger-klaehn-n0-iroh-iroh-blobs", "iroh-n0-friedel-ziegelmayer-r-diger-klaehn-post-authors"],
    # Named in chunk files (team-lead's dispatch), not in the calibration table:
    ["dominaezzz", "dominaezzz-esp-hal-reviewer"],
    ["jkelleyrtp", "jonathan-kelly", "jonathan-kelly-likely-kelley-unconfirmed"],
    ["kornel", "kornel-2", "kornel-forum-handle-identity-track-record-not-established"],
    ["nazmul-idris-r3bl-tui-maintainer", "nas-ceo-founder-rebel-author-developerlife-com-maintainer"],
]

canonical_of = {}       # any-member-id -> canonical id
for group in MERGE_GROUPS:
    canonical = group[0]
    for member in group:
        canonical_of[member] = canonical

issues.append(("merge-groups", f"{len(MERGE_GROUPS)} same-person clusters, {sum(len(g) for g in MERGE_GROUPS) - len(MERGE_GROUPS)} duplicate ids merged away"))

# ---------------------------------------------------------------------------
# 4. Resolve each original id's final verdict/type/track_record/influence
# ---------------------------------------------------------------------------

ILLEGAL_TYPE_IDS = set()
final_by_id = {}  # original id (pre-rename, pre-merge) -> {verdict, type, track_record, influence, name}
for vid, rec in chunk_records.items():
    verdict = rec["verdict"]
    type_ = rec["type"] if rec["type"] in VALID_TYPES else None
    if rec["type"] not in VALID_TYPES and rec["type"] != "unset":
        ILLEGAL_TYPE_IDS.add(vid)
        issues.append(("illegal-type-value", f"voice '{vid}': chunk file gives type '{rec['type']}', not one of {sorted(VALID_TYPES)}; left unset."))
    track_record = rec["track_record"]
    influence = rec["influence"]
    if vid in calib_overrides:
        ov = calib_overrides[vid]
        verdict = ov["verdict"]
        track_record = ov["track_record"]
        if ov["type_unset"]:
            type_ = None
    if verdict != "MEETS" and not track_record:
        # rule: no evidence exists for this FAILS/UNKNOWN voice -> type unset too
        type_ = None
    name = NAME_FIX.get(vid, rec["name"])
    final_by_id[vid] = dict(verdict=verdict, type=type_, track_record=track_record, influence=influence, name=name)

n_meets = sum(1 for r in final_by_id.values() if r["verdict"] == "MEETS")
n_fails = sum(1 for r in final_by_id.values() if r["verdict"] == "FAILS")
n_unknown = sum(1 for r in final_by_id.values() if r["verdict"] == "UNKNOWN")
issues.append(("verdict-counts", f"MEETS {n_meets}, FAILS {n_fails}, UNKNOWN {n_unknown} (of {len(final_by_id)} original ids)"))

# ---------------------------------------------------------------------------
# 5. Apply the name correction/rename, then the merges
# ---------------------------------------------------------------------------


def resolve_id(original_id: str) -> str:
    renamed = RENAME.get(original_id, original_id)
    return canonical_of.get(renamed, renamed)


def dedupe_track_list(items):
    seen = set()
    out = []
    for it in items:
        ev = (it.get("evidence") or "").strip().lower()
        if not it.get("url") and (ev.startswith("same as") or ev.startswith("duplicate") or "duplicate of" in ev or ev in ("", "same", "same.")):
            continue  # pure cross-reference to another cluster member; adds nothing once merged
        key = (it.get("kind"), it.get("url"), ev)
        if key in seen:
            continue
        seen.add(key)
        out.append(it)
    return out


final_voice_ids = set(resolve_id(vid) for vid in chunk_records)
merged_voice = {}  # final voice id -> {name, type, track_record, influence}
for fvid in final_voice_ids:
    # every original id that resolves to this final id
    members = [vid for vid in chunk_records if resolve_id(vid) == fvid]
    canonical_member = RENAME.get(fvid, fvid) if fvid in chunk_records else fvid
    # the canonical member is the group's first element (or the id itself if unmerged)
    base = fvid if fvid in chunk_records else None
    if base is None:
        # fvid came from a rename (sam-cutler); find the pre-rename source
        pre = [k for k, v in RENAME.items() if v == fvid][0]
        base = pre
    base_rec = final_by_id[base]
    track_record = list(base_rec["track_record"])
    influence = list(base_rec["influence"])
    for m in members:
        if m == base:
            continue
        track_record += final_by_id[m]["track_record"]
        influence += final_by_id[m]["influence"]
    track_record = dedupe_track_list(track_record)
    influence = dedupe_track_list(influence)
    merged_voice[fvid] = dict(name=base_rec["name"], type=base_rec["type"],
                               track_record=track_record, influence=influence)
    if len(members) > 1:
        issues.append(("voice-merge", f"{sorted(m for m in members if m != base)} merged into '{fvid}' (same person; RECON/verify/voices-calibration.md and, for dominaezzz/jkelleyrtp/kornel/nazmul-idris clusters, the chunk files' own same-person notes)"))

issues.append(("final-voice-count", f"{len(merged_voice)} Voice ids after {len(chunk_records) - len(merged_voice)} merged away"))

# ---------------------------------------------------------------------------
# 5b. Lead ruling: rewrite the 10 MEETS Voices whose only track_record
# citation was a `gh api` command (no browsable url) as the url that command
# reads. Transcription only — same evidence, no new claim, just the command
# turned into the page a person can open. Hardcoded per voice (a handful of
# cases, each individually checked), not a generic command parser.
# ---------------------------------------------------------------------------

GH_API_URL_PATCH = {
    "bjoernq": {"track_record": [
        dict(kind="production", evidence="esp-rs/esp-hal is Espressif's own chip HAL; @espressif company field",
             url="https://github.com/esp-rs/esp-hal", date=None),
    ]},
    "jamesmunns": {"track_record": [
        dict(kind="role", evidence="embassy-rs org membership (single-project org)",
             url="https://github.com/orgs/embassy-rs/people", date=None),
    ]},
    "jessebraham": {"track_record": [
        dict(kind="role", evidence="esp-rs org membership (single-project org)",
             url="https://github.com/orgs/esp-rs/people", date=None),
    ]},
    "laggui": {"track_record": [
        dict(kind="role", evidence="tracel-ai org membership (single-project org)",
             url="https://github.com/orgs/tracel-ai/people", date=None),
    ]},
    "ssokolow": {"track_record": [
        dict(kind="book/post", evidence="referenced/linked in This Week in Rust across at least 3 separate issues (2017-06-27, 2019-09-03, 2019-12-10)",
             url="https://github.com/search?q=ssokolow+repo%3Arust-lang%2Fthis-week-in-rust&type=code", date="2026-09-28"),
    ]},
    "stefan-baumgartner": {
        "track_record": [
            dict(kind="course", evidence='runs multiple named Rust training repos — "microservice-rust-workshop" (26 stars), "idiomatic-rust-workshop", "rust-fundamentals-training-april-2022", "rust-course-jku-2023-2024" (a university course), "refactoring-rust-tutorial"',
                 url="https://github.com/ddprrt?tab=repositories", date="2026-09-28"),
        ],
        "influence": [
            dict(kind=None, evidence="his JetBrains guest post on Rust vs. JS/TS was picked up in This Week in Rust (1 hit)",
                 url="https://github.com/search?q=rust-vs-javascript-typescript+repo%3Arust-lang%2Fthis-week-in-rust&type=code", date="2026-09-28"),
        ],
    },
    "vaultwarden-maintainers-dani-garcia-vaultwarden": {"track_record": [
        dict(kind="production/crate-dependents", evidence="Vaultwarden is a widely deployed Rust Bitwarden-compatible server with 68,245 GitHub stars, built on the Rocket web framework",
             url="https://github.com/dani-garcia/vaultwarden", date="2026-09-28"),
    ]},
    "warre-snaet": {"track_record": [
        dict(kind="post", evidence='"Building a 24MB Offline AI with Rust + Burn" was linked from This Week in Rust (2026-01-28 issue)',
             url="https://github.com/search?q=intelligent-disease-detection+repo%3Arust-lang%2Fthis-week-in-rust&type=code", date=None),
    ]},
    "yanshay": {"track_record": [
        dict(kind="production", evidence='ships "SpoolEase," a real 3D-printing filament-management hardware product (NFC/RFID console + scale) built in Rust, 554 GitHub stars',
             url="https://github.com/yanshay/spoolease", date="2026-09-28"),
    ]},
    "yatekii": {"track_record": [
        dict(kind="role/crate-dependents", evidence="creator of probe-rs, a real embedded ARM/RISC-V debugging toolset (2,953 GitHub stars), with 1,066 commits authored",
             url="https://github.com/probe-rs/probe-rs/commits?author=Yatekii", date=None),
    ]},
}

for fvid, patch in GH_API_URL_PATCH.items():
    for field, items in patch.items():
        merged_voice[fvid][field] = items
    issues.append(("gh-api-url-rewrite", f"voice '{fvid}': gh api command citation(s) rewritten as the browsable url the command reads."))

# ---------------------------------------------------------------------------
# 6. Write MAP/voices/: one file per final id, delete every merged-away/renamed
#    original file first.
# ---------------------------------------------------------------------------


def dump(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, width=100000, default_flow_style=False)


def track_record_yaml(items):
    out = []
    for it in items:
        d = {"kind": it["kind"]} if it.get("kind") else {}
        d["evidence"] = it["evidence"]
        if it.get("url"):
            d["url"] = it["url"]
        if it.get("date"):
            d["date"] = it["date"]
        out.append(d)
    return out


existing_voice_files = {p.stem for p in (MAP / "voices").glob("*.yaml")}
removed_files = existing_voice_files - set(merged_voice.keys())
for stem in removed_files:
    (MAP / "voices" / f"{stem}.yaml").unlink()

n_voice_written = 0
for fvid, rec in merged_voice.items():
    data = {"id": fvid, "name": rec["name"]}
    if rec["type"]:
        data["type"] = rec["type"]
    if rec["track_record"]:
        data["track_record"] = track_record_yaml(rec["track_record"])
    if rec["influence"]:
        data["influence"] = track_record_yaml(rec["influence"])
    dump(MAP / "voices" / f"{fvid}.yaml", data)
    n_voice_written += 1

issues.append(("voices-written", f"{n_voice_written} Voice files written; {len(removed_files)} removed (merged away or renamed)"))

# ---------------------------------------------------------------------------
# 7. Repoint MAP/claims/: voice id through rename+merge, and gap for
#    FAILS/UNKNOWN voices (rule: FAILS -> voice-below-bar, UNKNOWN ->
#    voice-unverified; MEETS -> nothing more).
# ---------------------------------------------------------------------------

GAP_TEXT = {"FAILS": "voice-below-bar", "UNKNOWN": "voice-unverified"}

n_claims_repointed = 0
n_claims_gapped = Counter()
claim_files = sorted((MAP / "claims").glob("*.yaml"))
for p in claim_files:
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    old_voice = data.get("voice")
    if old_voice not in final_by_id:
        issues.append(("claim-voice-not-in-verification", f"claim '{p.stem}': voice '{old_voice}' has no entry in any chunk file; left as-is, ungapped."))
        continue
    new_voice = resolve_id(old_voice)
    verdict = final_by_id[old_voice]["verdict"]
    changed = False
    if new_voice != old_voice:
        data["voice"] = new_voice
        changed = True
        n_claims_repointed += 1
    gap_text = GAP_TEXT.get(verdict)
    if gap_text:
        existing = [g.strip() for g in (data.get("gap") or "").split(";") if g.strip()]
        if gap_text not in existing:
            existing.append(gap_text)
            data["gap"] = "; ".join(existing)
            changed = True
        n_claims_gapped[verdict] += 1
    if changed:
        dump(p, data)

issues.append(("claims-repointed", f"{n_claims_repointed} Claims repointed to a merged/renamed voice id"))
issues.append(("claims-gapped", f"{n_claims_gapped['FAILS']} Claims gapped voice-below-bar, {n_claims_gapped['UNKNOWN']} gapped voice-unverified"))

print("chunk_records:", len(chunk_records))
print("calib_overrides:", len(calib_overrides))
print("merge groups:", len(MERGE_GROUPS), "members total:", sum(len(g) for g in MERGE_GROUPS))
print("final voice count:", len(merged_voice))
print("verdicts: MEETS", n_meets, "FAILS", n_fails, "UNKNOWN", n_unknown)
print("illegal type ids:", sorted(ILLEGAL_TYPE_IDS))
print("voices written:", n_voice_written, "removed:", len(removed_files))
print("claims repointed:", n_claims_repointed, "claims gapped:", dict(n_claims_gapped))

with open("/private/tmp/claude-501/-Users-ryzhakar-pp-gym/24588f30-a8bd-46c9-8d8f-3b9d74cdd27f/scratchpad/voice-issues.log", "w", encoding="utf-8") as f:
    for t, d in issues:
        f.write(f"{t}\t{d}\n")
