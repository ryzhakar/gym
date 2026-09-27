"""Build books-courses bundles: for batch-1, the book is the source, not its front page.

Usage: uv run python scripts/research/books.py <team-a|team-b>

Every batch-1 `class=books-courses` row, upgraded in `cache.py` via `fetch_book()` (a single
/print.html request for an mdBook site, else a table-of-contents crawl - see cache.py for the
fetch side of this; this script only reads the resulting cache and bundles it). A paywalled
site (PAYWALLED_DOMAINS in cache.py) stays `unreachable` - it was never attempted, by owner
ruling, and nothing here changes that.

Output: samples/bundles/b1-team-{team}-B{nn}.txt (~150k-char slices, never splitting a
source, same header format as bundle.py) and samples/bundles/b1-team-{team}-B-manifest.csv
(slice,data_row,id,url,status,reason,chars).
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import cache as c  # noqa: E402 - local module, path set above

RECON = Path("/Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27/research/rust-map")
SAMPLES = RECON / "samples"
BUNDLES = SAMPLES / "bundles"
STATUS_CSV = SAMPLES / "prefetch-b1-status.csv"
SLICE_TARGET_CHARS = 150_000


def latest_status_by_id_url() -> dict[tuple[str, str], dict]:
    latest: dict[tuple[str, str], dict] = {}
    for row in csv.DictReader(STATUS_CSV.open(newline="")):
        latest[(row["id"], row["url"])] = row
    return latest


def load_text(status_row: dict) -> str | None:
    key = status_row.get("key")
    if not key:
        return None
    for suffix in (".txt", ".abstract.txt"):
        p = c.CACHE / f"{key}{suffix}"
        if p.exists():
            return p.read_text(errors="replace")
    return None


def classify(text: str | None, url: str) -> str | None:
    """None if kept; else the drop reason (paywalled, no-text, stub, thin)."""
    if c.domain_of(url) in c.PAYWALLED_DOMAINS:
        return "paywalled"
    if text is None:
        return "no-text"
    lower = text.lower()
    if any(marker in lower for marker in c.CHALLENGE_MARKERS):
        return "stub"
    if len(text) < c.MIN_PAGE_CHARS:
        return "thin"
    return None


def build(team_arg: str) -> None:
    batch_rows = list(csv.DictReader((SAMPLES / f"batch-1-{team_arg}.csv").open(newline="")))
    status_by_id_url = latest_status_by_id_url()

    manifest: list[dict] = []
    kept: list[tuple[dict, str]] = []

    for data_row, batch_row in enumerate(batch_rows, start=1):
        if "books-courses" not in batch_row["class"].split(";"):
            continue
        status_row = status_by_id_url.get((batch_row["id"], batch_row["url"]), {})
        text = load_text(status_row)
        reason = classify(text, batch_row["url"])
        chars = len(text) if text is not None else 0
        manifest.append({
            "data_row": data_row, "id": batch_row["id"], "url": batch_row["url"],
            "status": "dropped" if reason else "kept", "reason": reason or "", "chars": chars,
        })
        if reason is None:
            kept.append((batch_row | {"data_row": data_row}, text))

    BUNDLES.mkdir(parents=True, exist_ok=True)
    for stale in BUNDLES.glob(f"b1-{team_arg}-B*.txt"):
        stale.unlink()  # fully rebuilt each run, like sendback.py's R/T passes

    slices: list[list[tuple[dict, str]]] = [[]]
    running = 0
    for row, text in kept:
        piece_len = min(len(text), SLICE_TARGET_CHARS)
        if slices[-1] and running + piece_len > SLICE_TARGET_CHARS:
            slices.append([])
            running = 0
        slices[-1].append((row, text))
        running += piece_len

    row_to_slice = {}
    for i, sl in enumerate(slices, start=1):
        if not sl:
            continue
        path = BUNDLES / f"b1-{team_arg}-B{i:02d}.txt"
        with path.open("w") as f:
            for row, text in sl:
                if len(text) > SLICE_TARGET_CHARS:
                    text = text[:SLICE_TARGET_CHARS] + "\n[... truncated at 150,000 chars ...]\n"
                header = (f"=== ROW {row['data_row']} | {row['id']} | {row['url']} | "
                          f"{row['date']} | {row['class']} ===")
                f.write(header + "\n" + text + "\n\n")
                row_to_slice[row["data_row"]] = i

    for entry in manifest:
        entry["slice"] = f"B{row_to_slice[entry['data_row']]:02d}" if entry["data_row"] in row_to_slice else ""

    manifest.sort(key=lambda e: e["data_row"])
    manifest_path = BUNDLES / f"b1-{team_arg}-B-manifest.csv"
    with manifest_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["slice", "data_row", "id", "url", "status", "reason", "chars"])
        w.writeheader()
        for entry in manifest:
            w.writerow({k: entry[k] for k in w.fieldnames})

    n_slices = sum(1 for sl in slices if sl)
    n_kept = sum(1 for e in manifest if e["status"] == "kept")
    n_dropped = len(manifest) - n_kept
    total_chars = sum(e["chars"] for e in manifest if e["status"] == "kept")
    print(f"{team_arg}: {len(manifest)} books-courses rows, {n_kept} kept ({total_chars:,} chars), "
          f"{n_dropped} dropped, {n_slices} slices -> {manifest_path}")


if __name__ == "__main__":
    build(sys.argv[1])
