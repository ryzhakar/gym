"""Apply the Claim-verification pass (RECON/verify/claims-final.csv,
claims-adjudication.md) onto MAP/claims. Transcribes only. See
RECON/compile/compile-b1.md for accounting.
"""
import csv
import yaml
from pathlib import Path
from collections import Counter

RECON = Path("/Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27/research/rust-map")
MAP = Path("/Users/ryzhakar/pp/gym/maps/rust")

FIELD_ORDER = ["id", "voice", "position", "source", "date", "locator", "paraphrase", "quote", "practiced", "gap", "superseded_by"]

GAP_NOTE = {
    "DATE-WRONG": "verified 2026-09-28: date corrected",
    "UNFAITHFUL-drop-only": "verified 2026-09-28: quote not verbatim to source; removed",
    "UNFAITHFUL-drop-and-paraphrase": "verified 2026-09-28: quote not faithful to source; removed, paraphrase corrected",
    "UNFAITHFUL-paraphrase-only": "verified 2026-09-28: paraphrase overstated the source; corrected (quote kept, verbatim)",
}

rows = list(csv.DictReader(open(RECON / "verify" / "claims-final.csv", encoding="utf-8")))

counts = Counter()
locator_set = 0
date_set = 0
quote_dropped = 0
paraphrase_set = 0
gapped = 0

for row in rows:
    cid = row["claim_id"]
    path = MAP / "claims" / f"{cid}.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    if row["corrected_locator"]:
        data["locator"] = row["corrected_locator"]
        locator_set += 1
    if row["corrected_date"]:
        data["date"] = row["corrected_date"]
        date_set += 1
    if row["drop_quote"] == "yes":
        data.pop("quote", None)
        quote_dropped += 1
    if row["corrected_paraphrase"]:
        data["paraphrase"] = row["corrected_paraphrase"]
        paraphrase_set += 1
    if row["gap_url"]:
        # none present in this batch; kept for completeness if a future batch adds one
        data["gap_url"] = row["gap_url"]

    data["practiced"] = row["practiced"]

    verdict = row["verdict"]
    counts[verdict] += 1
    if verdict != "CONFIRMED":
        if verdict == "DATE-WRONG":
            note = GAP_NOTE["DATE-WRONG"]
        elif row["drop_quote"] == "yes" and row["corrected_paraphrase"]:
            note = GAP_NOTE["UNFAITHFUL-drop-and-paraphrase"]
        elif row["drop_quote"] == "yes":
            note = GAP_NOTE["UNFAITHFUL-drop-only"]
        else:
            note = GAP_NOTE["UNFAITHFUL-paraphrase-only"]
        existing = [g.strip() for g in (data.get("gap") or "").split(";") if g.strip()]
        if note not in existing:
            existing.append(note)
        data["gap"] = "; ".join(existing)
        gapped += 1

    ordered = {k: data[k] for k in FIELD_ORDER if k in data}
    for k in data:
        if k not in ordered:
            ordered[k] = data[k]

    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(ordered, f, allow_unicode=True, sort_keys=False, width=100000, default_flow_style=False)

print("rows processed:", len(rows))
print("verdicts:", dict(counts))
print("locator set:", locator_set, "date set:", date_set, "quote dropped:", quote_dropped, "paraphrase set:", paraphrase_set)
print("gap note added (non-CONFIRMED):", gapped)
