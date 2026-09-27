"""Serial search step for gym's teaching-research saturation rounds.

Agents write queries; this script does the searching. Two subcommands:

  run <queries.txt> <out.csv>            search every query, write one results csv
  found <out.csv> <found.md> [--sources <sources.csv>]
                                          distinct DOIs from a run, marked new/seen

Query file format (one query per line):
  - blank lines and lines starting with `#` are ignored
  - a line may start with `openalex:` or `crossref:` (case-insensitive) to search
    only that database; a bare line searches both
  - example:
      # spaced practice, K-12
      openalex: spaced retrieval practice classroom
      crossref: distributed practice mathematics

Databases: OpenAlex (`GET /works?search=`) and Crossref (`GET /works?query=`),
50 results per query, `mailto` set for the polite pool. OpenAlex on this IP is
rate-limited (HTTP 429/503, daily budget) — calls run strictly serially, 1s
between them, with backoff on 429/503 (advertised Retry-After or "retry in Ns"
in the body, else 40s), up to 6 attempts before a query is logged `blocked`.

`run` flags:
  --db {openalex,crossref,both}   restrict to one database (default both); a
                                   query line's own prefix still narrows further
                                   (the effective set is the intersection) — a
                                   query left with no db to search is skipped,
                                   emitting no row
  --append                        add to an existing out.csv instead of
                                   overwriting it (no header rewritten); lets
                                   Crossref and OpenAlex passes for the same
                                   queries.txt land in one file across runs

OpenAlex circuit breaker: this IP has a daily OpenAlex budget. If a response
body mentions "budget" (its exhaustion message), or 3 OpenAlex queries in a
row come back blocked, OpenAlex is switched off for the rest of the run — every
remaining OpenAlex query is logged `skipped-budget` with no request and no
retries. Crossref is unaffected. Re-run later with `--db openalex --append`.

out.csv columns: query,db,status,hits,doi,title,year,abstract
  - status is one of: ok, zero, blocked, skipped-budget
  - one row per result when status=ok (hits = total matches the API reports,
    repeated on every row for that query)
  - one summary row, fields blank but status+hits, when status is zero,
    blocked, or skipped-budget
  - abstract is plain text: rebuilt from OpenAlex's inverted index, or Crossref's
    JATS-tagged abstract with tags stripped

found.md: distinct normalized DOIs across every ok row in out.csv, each marked
`new` (not in sources.csv) or `seen` (already there), as a `## Found DOIs` list.
"""
import argparse
import csv
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import cache  # noqa: E402  (normalize_doi reuse)

UA = "Mozilla/5.0 (gym-research-search; +https://github.com/ryzhakar)"
MAILTO = "gym-research@example.org"
FIELDS = ["query", "db", "status", "hits", "doi", "title", "year", "abstract"]
DEFAULT_SOURCES = Path(
    "/Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27"
    "/research/teaching/ledger/sources.csv"
)
RETRY_STATUSES = {429, 503}
MAX_ATTEMPTS = 6
DEFAULT_BACKOFF = 40.0
PACE_SECONDS = 1.0
BUDGET_RE = re.compile(r"budget", re.I)
BREAKER_STREAK = 3


class BudgetExhausted(Exception):
    """Raised when a response body names the daily-budget exhaustion, not a transient 429."""


# --- http --------------------------------------------------------------

def retry_wait(header: str | None, body: str) -> float:
    if header and header.strip().isdigit():
        return float(header.strip())
    m = re.search(r"retry in (\d+)", body, re.I)
    return float(m.group(1)) if m else DEFAULT_BACKOFF


def fetch_json(url: str) -> dict | None:
    """GET url as json. Returns None (blocked) after MAX_ATTEMPTS on 429/503.

    Raises BudgetExhausted immediately, no retries, if a body names the budget.
    """
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code not in RETRY_STATUSES:
                raise
            try:
                body = e.read().decode("utf-8", "ignore")
            except Exception:
                body = ""
            if BUDGET_RE.search(body):
                raise BudgetExhausted(body[:200])
            if attempt == MAX_ATTEMPTS:
                return None
            time.sleep(retry_wait(e.headers.get("Retry-After") if e.headers else None, body))
    return None


# --- db-specific search --------------------------------------------------

def clean_doi(s: str) -> str:
    return cache.normalize_doi(s or "").lower()


def rebuild_abstract(inverted_index: dict | None) -> str:
    if not inverted_index:
        return ""
    positions: dict[int, str] = {}
    last = -1
    for word, idxs in inverted_index.items():
        for i in idxs:
            positions[i] = word
            last = max(last, i)
    return " ".join(positions.get(i, "") for i in range(last + 1)).strip()


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s or "").strip()


def search_openalex(query: str) -> tuple[str, int, list[dict]]:
    url = (
        "https://api.openalex.org/works?search=" + urllib.parse.quote(query)
        + "&per-page=50&mailto=" + MAILTO
        + "&select=id,doi,title,publication_year,abstract_inverted_index"
    )
    data = fetch_json(url)
    if data is None:
        return "blocked", 0, []
    hits = data.get("meta", {}).get("count", 0)
    rows = [
        {
            "doi": clean_doi(r.get("doi") or ""),
            "title": r.get("title") or "",
            "year": r.get("publication_year") or "",
            "abstract": rebuild_abstract(r.get("abstract_inverted_index")),
        }
        for r in data.get("results", [])
    ]
    return ("ok", hits, rows) if rows else ("zero", 0, [])


def search_crossref(query: str) -> tuple[str, int, list[dict]]:
    url = (
        "https://api.crossref.org/works?query=" + urllib.parse.quote(query)
        + "&rows=50&mailto=" + MAILTO
    )
    data = fetch_json(url)
    if data is None:
        return "blocked", 0, []
    msg = data.get("message", {})
    hits = msg.get("total-results", 0)
    rows = []
    for it in msg.get("items", []):
        titles = it.get("title") or []
        date_parts = (it.get("issued") or {}).get("date-parts") or [[]]
        year = date_parts[0][0] if date_parts and date_parts[0] else ""
        rows.append(
            {
                "doi": clean_doi(it.get("DOI") or ""),
                "title": titles[0] if titles else "",
                "year": year,
                "abstract": strip_tags(it.get("abstract", "")),
            }
        )
    return ("ok", hits, rows) if rows else ("zero", 0, [])


SEARCHERS = {"openalex": search_openalex, "crossref": search_crossref}


# --- query file ----------------------------------------------------------

def parse_queries(path: Path) -> list[tuple[str, list[str]]]:
    out = []
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        dbs = list(SEARCHERS)
        for prefix in SEARCHERS:
            if line.lower().startswith(prefix + ":"):
                line = line[len(prefix) + 1:].strip()
                dbs = [prefix]
                break
        out.append((line, dbs))
    return out


# --- commands --------------------------------------------------------------

def blank_row(query: str, db: str, status: str, hits) -> dict:
    return {"query": query, "db": db, "status": status, "hits": hits,
            "doi": "", "title": "", "year": "", "abstract": ""}


def cmd_run(queries_path: Path, out_path: Path, db_filter: str, append: bool) -> None:
    wanted = set(SEARCHERS) if db_filter == "both" else {db_filter}
    openalex_disabled = False
    openalex_streak = 0
    rows = []
    for query, dbs in parse_queries(queries_path):
        for db in (d for d in dbs if d in wanted):
            if db == "openalex" and openalex_disabled:
                rows.append(blank_row(query, db, "skipped-budget", ""))
                print(f"{query!r} openalex skipped-budget")
                continue
            time.sleep(PACE_SECONDS)
            try:
                status, hits, results = SEARCHERS[db](query)
            except BudgetExhausted as e:
                print(f"openalex budget exhausted: {e} -- disabling openalex for the rest of this run")
                openalex_disabled = True
                rows.append(blank_row(query, db, "blocked", 0))
                continue
            print(f"{query!r} {db} {status} hits={hits}")
            if status == "ok":
                for r in results:
                    rows.append({"query": query, "db": db, "status": status, "hits": hits, **r})
            else:
                rows.append(blank_row(query, db, status, hits))
            if db == "openalex":
                openalex_streak = openalex_streak + 1 if status == "blocked" else 0
                if openalex_streak >= BREAKER_STREAK:
                    print(f"openalex blocked {BREAKER_STREAK}x in a row -- disabling openalex for the rest of this run")
                    openalex_disabled = True
    mode = "a" if (append and out_path.exists()) else "w"
    with out_path.open(mode, newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if mode == "w":
            w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} rows -> {out_path} ({'appended' if mode == 'a' else 'new'})")


def cmd_found(out_path: Path, found_path: Path, sources_path: Path) -> None:
    existing = set()
    if sources_path.exists():
        with sources_path.open(newline="") as f:
            for row in csv.DictReader(f):
                v = (row.get("doi_or_url") or "").strip()
                if v:
                    existing.add(clean_doi(v))

    seen: dict[str, tuple[str, str]] = {}
    with out_path.open(newline="") as f:
        for row in csv.DictReader(f):
            doi = (row.get("doi") or "").strip()
            if row.get("status") == "ok" and doi:
                seen.setdefault(doi, (row.get("title", ""), row.get("year", "")))

    lines = ["## Found DOIs", ""]
    new_count = 0
    for doi in sorted(seen):
        title, year = seen[doi]
        tag = "seen" if doi in existing else "new"
        new_count += tag == "new"
        lines.append(f"- `{doi}` — {title} ({year}) — {tag}")
    found_path.write_text("\n".join(lines) + "\n")
    print(f"distinct={len(seen)} new={new_count} seen={len(seen) - new_count}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    p_run = sub.add_parser("run")
    p_run.add_argument("queries", type=Path)
    p_run.add_argument("out", type=Path)
    p_run.add_argument("--db", choices=["openalex", "crossref", "both"], default="both")
    p_run.add_argument("--append", action="store_true")

    p_found = sub.add_parser("found")
    p_found.add_argument("out", type=Path)
    p_found.add_argument("found_md", type=Path)
    p_found.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)

    args = p.parse_args()
    if args.cmd == "run":
        cmd_run(args.queries, args.out, args.db, args.append)
    elif args.cmd == "found":
        cmd_found(args.out, args.found_md, args.sources)


if __name__ == "__main__":
    main()
