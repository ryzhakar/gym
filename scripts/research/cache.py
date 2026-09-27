"""Durable source cache for gym's research agents.

One fetch per source, ever. Subcommands:
  get <doi-or-url>          cache hit -> print text path; miss -> fetch, save, print path
  ingest-tmp                pull DOIs out of /tmp/*.pdf, cache each
  fetch-csv <csv>           fetch every row's url by source-class route; write a status csv

Cache layout: CACHE/<key>.txt (or .abstract.txt) + CACHE/index.csv (key,doi_or_url,route,fetched_at,agent,chars).
Key = DOI lowercased, '/' -> '_'; or first 12 hex of sha1(url) when there is no DOI.

Not a scraping project: each route gets at most two genuine tries, then the source is logged
unreachable and left for a research agent to fetch by hand.
"""
import csv
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

CACHE = Path("/Users/ryzhakar/pp/gym/docs/orchestration_log/recon/cache")
INDEX = CACHE / "index.csv"
INDEX_FIELDS = ["key", "doi_or_url", "route", "fetched_at", "agent", "chars"]
AGENT = "cache-script"
UA = "Mozilla/5.0 (gym-research-cache; +https://github.com/ryzhakar)"
UNPAYWALL_EMAIL = "gym-research@example.org"
DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"<>]+")
ARXIV_ID_RE = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")
PAYWALLED_DOMAINS = {
    "packtpub.com", "amazon.com", "manning.com", "leanpub.com",
    "edx.org", "linkedin.com",
}


class FetchError(Exception):
    def __init__(self, tried: list[str]):
        super().__init__("; ".join(tried))
        self.tried = tried


@dataclass
class Fetched:
    text: str
    route: str


# --- primitives -------------------------------------------------------------

def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def doi_key(doi: str) -> str:
    return doi.strip().lower().replace("/", "_")


def url_key(url: str) -> str:
    return hashlib.sha1(url.encode()).hexdigest()[:12]


def http_get(url: str, headers: dict | None = None, timeout: int = 25) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def http_get_json(url: str, headers: dict | None = None, timeout: int = 25):
    return json.loads(http_get(url, headers, timeout))


class _TextExtractor(HTMLParser):
    """Strips tags for a plain-text rendering. No dependency; good enough for archival text."""

    SKIP_TAGS = {"script", "style", "noscript", "template"}

    def __init__(self):
        super().__init__()
        self._skip = 0
        self.chunks: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP_TAGS:
            self._skip += 1
        if tag in ("p", "br", "div", "li", "h1", "h2", "h3", "h4", "tr", "blockquote"):
            self.chunks.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP_TAGS and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.chunks.append(data)


def html_to_text(raw: bytes) -> str:
    parser = _TextExtractor()
    parser.feed(raw.decode("utf-8", errors="replace"))
    text = html.unescape("".join(parser.chunks))
    lines = [ln.strip() for ln in text.splitlines()]
    return "\n".join(ln for ln in lines if ln)


# Cloudflare/login-wall stub markers. "just a moment..." keeps its ellipsis literally:
# without it, the phrase also occurs in ordinary prose ("...in just a moment, its
# memory layout...") and false-positives.
CHALLENGE_MARKERS = (
    "cf-browser-verification",
    "enable javascript and cookies to continue",
    "checking your browser before accessing",
    "attention required! | cloudflare",
    "just a moment...",
)
MIN_PAGE_CHARS = 1500  # below this, an "HTML route" page is more likely a stub than an article


def validate_page_text(text: str, min_chars: int = MIN_PAGE_CHARS) -> str:
    """Reject a bot-challenge/login-wall stub or a suspiciously thin page.

    Only called on whole-page text from an HTML-producing route (route_html, the html
    branch of fetch_pdf_or_html, wayback, europe-pmc, browser) - never on routes whose
    real content is naturally short (a single reddit comment, a GitHub PR title, an
    abstract, an individual Discourse post folded into a longer thread).
    """
    lower = text.lower()
    for marker in CHALLENGE_MARKERS:
        if marker in lower:
            raise FetchError([f"bot-wall/login-wall marker matched ({len(text)} chars)"])
    if len(text) < min_chars:
        raise FetchError([f"page too short to trust ({len(text)} chars, min {min_chars})"])
    return text


CLIENT_REDIRECT_RE = re.compile(
    rb'location\.replace\(\s*["\']([^"\']+)["\']|'
    rb'http-equiv=["\']refresh["\'][^>]*url=([^"\'>]+)',
    re.I,
)


def follow_client_redirect(url: str, raw: bytes, timeout: int = 25, max_hops: int = 4) -> bytes:
    """Given an already-fetched page, follow a chain of client-side redirects.

    urllib already follows real HTTP 3xx; some sites (e.g. blog.rust-lang.org
    without a trailing slash, or rtic.rs's two-hop stub-page chain) instead serve
    a 200 page whose body redirects via JS or meta-refresh, which urllib cannot see.
    """
    seen = {url}
    for _ in range(max_hops):
        m = CLIENT_REDIRECT_RE.search(raw)
        if not m:
            return raw
        target = urllib.parse.urljoin(url, (m.group(1) or m.group(2)).decode())
        if target in seen:
            return raw
        seen.add(target)
        url, raw = target, http_get(target, timeout=timeout)
    return raw


def http_get_html(url: str, timeout: int = 25) -> bytes:
    return follow_client_redirect(url, http_get(url, timeout=timeout), timeout=timeout)


def pdf_to_text(pdf_path: Path) -> str:
    out = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        capture_output=True, timeout=60,
    )
    return out.stdout.decode("utf-8", errors="replace")


def gh_api(path: str, extra: list[str] | None = None) -> str:
    cmd = ["gh", "api", path] + (extra or [])
    out = subprocess.run(cmd, capture_output=True, timeout=30)
    if out.returncode != 0:
        raise FetchError([f"gh api {path}: {out.stderr.decode(errors='replace')[:200]}"])
    return out.stdout.decode("utf-8", errors="replace")


def wayback_snapshot_url(url: str) -> str:
    # safe="": archive.org's availability endpoint silently returns no match if the url
    # param's own '/' are left unescaped (quote()'s default safe='/') - confirmed by testing
    # the same query both ways; fully encoding it is what actually matches a snapshot.
    avail = http_get_json(f"https://archive.org/wayback/available?url={urllib.parse.quote(url, safe='')}")
    snap = avail.get("archived_snapshots", {}).get("closest", {}).get("url")
    if not snap:
        raise FetchError([f"wayback: no snapshot for {url}"])
    return snap


def wayback_fallback(url: str) -> str:
    return validate_page_text(html_to_text(http_get(wayback_snapshot_url(url))))


# --- index --------------------------------------------------------------

def read_index() -> list[dict]:
    if not INDEX.exists() or INDEX.stat().st_size == 0:
        return []
    with INDEX.open(newline="") as f:
        return list(csv.DictReader(f))


def append_index(row: dict):
    is_new = not INDEX.exists() or INDEX.stat().st_size == 0
    with INDEX.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=INDEX_FIELDS)
        if is_new:
            w.writeheader()
        w.writerow(row)


def find_cached(doi_or_url: str) -> dict | None:
    # last match wins: the index is an append-only log shared by many concurrent agents,
    # so a later row (e.g. a manual re-fetch after a bad one) supersedes an earlier one.
    needle = doi_or_url.strip().lower()
    hit = None
    for row in read_index():
        if row["doi_or_url"].strip().lower() == needle:
            hit = row
    return hit


def save_text(key: str, text: str, route: str, doi_or_url: str, abstract: bool = False) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    suffix = ".abstract.txt" if abstract else ".txt"
    path = CACHE / f"{key}{suffix}"
    path.write_text(text)
    append_index({
        "key": key, "doi_or_url": doi_or_url, "route": "abstract" if abstract else route,
        "fetched_at": now_iso(), "agent": AGENT, "chars": len(text),
    })
    return path


# --- DOI routes (used by `get`) -----------------------------------------

def normalize_doi(s: str) -> str:
    s = s.strip()
    s = re.sub(r"^https?://(dx\.)?doi\.org/", "", s, flags=re.I)
    s = re.sub(r"^doi:\s*", "", s, flags=re.I)
    return s


def is_doi(s: str) -> bool:
    return bool(DOI_RE.match(normalize_doi(s)))


def fetch_pdf_or_html(url: str) -> str:
    raw = http_get(url)
    if raw[:5] == b"%PDF-":
        with tempfile.NamedTemporaryFile(suffix=".pdf") as tf:
            tf.write(raw)
            tf.flush()
            return pdf_to_text(Path(tf.name))
    return validate_page_text(html_to_text(follow_client_redirect(url, raw)))


def unpaywall_route(doi: str) -> str:
    data = http_get_json(f"https://api.unpaywall.org/v2/{doi}?email={UNPAYWALL_EMAIL}")
    loc = data.get("best_oa_location") or {}
    url = loc.get("url_for_pdf") or loc.get("url")
    if not url:
        raise FetchError(["unpaywall: no OA location"])
    return fetch_pdf_or_html(url)


def arxiv_route(doi: str) -> str:
    # arXiv DOIs (10.48550/arXiv.<id>) name the paper directly; skip the search API.
    m = re.match(r"10\.48550/arxiv\.(.+)", doi, re.I)
    if m:
        return fetch_pdf_or_html(f"https://arxiv.org/pdf/{m.group(1)}")
    # safe=':/' matches arXiv's own examples; an encoded ':' trips their edge WAF into a 406.
    # arXiv's export API also asks for >=3s between requests; one retry covers a burst hit.
    q = urllib.parse.quote(f'doi:"{doi}"', safe=":/")
    url = f"https://export.arxiv.org/api/query?search_query={q}&max_results=1"
    for attempt in (0, 3):
        if attempt:
            time.sleep(attempt)
        try:
            raw = http_get(url)
            break
        except urllib.error.HTTPError as e:
            if e.code != 406 or attempt:
                raise
    m = re.search(r"arxiv\.org/abs/([\w.\-/]+)", raw.decode(errors="replace"))
    if not m:
        raise FetchError(["arxiv: no matching entry"])
    return fetch_pdf_or_html(f"https://arxiv.org/pdf/{m.group(1)}")


def semantic_scholar_route(doi: str) -> str:
    data = http_get_json(
        f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=openAccessPdf,abstract"
    )
    pdf = (data.get("openAccessPdf") or {}).get("url")
    if pdf:
        return fetch_pdf_or_html(pdf)
    if data.get("abstract"):
        raise FetchError(["semantic-scholar: abstract only"])  # caller saves as abstract
    raise FetchError(["semantic-scholar: no OA pdf, no abstract"])


def europe_pmc_route(doi: str) -> str:
    hit = http_get_json(
        f"https://www.ebi.ac.uk/europepmc/webservices/rest/search"
        f"?query=DOI:{doi}&resultType=core&format=json"
    )
    results = hit.get("resultList", {}).get("result", [])
    if not results:
        raise FetchError(["europe-pmc: no result"])
    result = results[0]
    pmcid = result.get("pmcid")
    if pmcid:
        raw = http_get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML")
        return validate_page_text(html_to_text(raw))
    for link in result.get("fullTextUrlList", {}).get("fullTextUrl", []):
        if link.get("documentStyle") == "pdf" and link.get("availability", "").startswith("Open"):
            return fetch_pdf_or_html(link["url"])
    raise FetchError(["europe-pmc: no OA full text"])


def openalex_route(doi: str) -> str:
    data = http_get_json(f"https://api.openalex.org/works/https://doi.org/{doi}")
    candidates = [(data.get("open_access") or {}).get("oa_url"),
                  (data.get("best_oa_location") or {}).get("pdf_url")]
    candidates += [loc.get("pdf_url") for loc in data.get("locations", [])]
    for url in candidates:
        if url:
            try:
                return fetch_pdf_or_html(url)
            except Exception:  # noqa: BLE001 - try the next candidate location
                continue
    raise FetchError(["openalex: no reachable pdf_url"])


def core_route(doi: str) -> str:
    key = os.environ.get("CORE_API_KEY")
    if not key:
        raise FetchError(["core: no CORE_API_KEY configured, skipped"])
    data = http_get_json(
        f'https://api.core.ac.uk/v3/search/works?q=doi:"{doi}"',
        headers={"Authorization": f"Bearer {key}"},
    )
    hits = data.get("results", [])
    if not hits or not hits[0].get("downloadUrl"):
        raise FetchError(["core: no downloadUrl"])
    return fetch_pdf_or_html(hits[0]["downloadUrl"])


def browser_route(url: str) -> str:
    """Headless-render fallback for JS/Cloudflare-gated pages. Requires Playwright + Chromium;
    both are provisioned once by `ensure_browser()`, which drops this route entirely if either
    install fails, rather than eating a `get`/`fetch-csv` call's two-genuine-tries budget."""
    if not ensure_browser():
        raise FetchError(["browser: playwright/chromium unavailable, route dropped"])
    from playwright.sync_api import sync_playwright  # noqa: PLC0415 - only imported when installed

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(user_agent=UA)
        # domcontentloaded, not networkidle: many sites poll analytics forever and never idle.
        page.goto(url, timeout=20000, wait_until="domcontentloaded")
        page.wait_for_timeout(1500)  # let client-side redirects/hydration settle
        try:
            content = page.content()
        except Exception:  # noqa: BLE001 - still navigating; one more beat is enough
            page.wait_for_timeout(1500)
            content = page.content()
        browser.close()
    return validate_page_text(html_to_text(content.encode()))


_BROWSER_STATE = {"checked": False, "available": False}


def ensure_browser() -> bool:
    if _BROWSER_STATE["checked"]:
        return _BROWSER_STATE["available"]
    _BROWSER_STATE["checked"] = True
    try:
        import playwright  # noqa: F401
    except ImportError:
        _BROWSER_STATE["available"] = False
        return False
    out = subprocess.run(["uv", "run", "playwright", "install", "chromium"],
                          capture_output=True, timeout=180)
    _BROWSER_STATE["available"] = out.returncode == 0
    return _BROWSER_STATE["available"]


def fetch_by_doi(doi: str) -> Fetched:
    tried = []
    routes = (
        ("unpaywall", unpaywall_route), ("arxiv", arxiv_route),
        ("semantic-scholar", semantic_scholar_route), ("europe-pmc", europe_pmc_route),
        ("openalex", openalex_route), ("core", core_route),
    )
    for name, fn in routes:
        try:
            return Fetched(fn(doi), name)
        except Exception as e:  # noqa: BLE001 - route boundary, we re-raise as FetchError below
            tried.append(f"{name}: {e}")
    # last resort: semantic scholar abstract-only, saved separately by caller
    try:
        data = http_get_json(
            f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=abstract"
        )
        if data.get("abstract"):
            return Fetched(data["abstract"], "abstract")
    except Exception as e:  # noqa: BLE001
        tried.append(f"semantic-scholar-abstract: {e}")
    try:
        return Fetched(browser_route(f"https://doi.org/{doi}"), "browser")
    except Exception as e:  # noqa: BLE001
        tried.append(f"browser: {e}")
    raise FetchError(tried)


# --- fetch-csv routes -----------------------------------------------------

def gh_repo_of(url: str):
    m = re.search(r"github\.com/([^/]+)/([^/]+)(?:/(issues|pull|pulls)/(\d+))?", url)
    if not m:
        return None
    owner, repo, kind, num = m.groups()
    return owner, repo.removesuffix(".git"), kind, num


def attributed(item: dict, login_path=("user", "login")) -> str:
    """`@<login> · <created_at>:` + body, so an extractor can name a Claim's Voice
    without an extra `gh api` / Discourse / reddit call. Empty string if there's no body."""
    body = item.get("body") or ""
    if not body:
        return ""
    login = item
    for step in login_path:
        login = (login or {}).get(step)
    return f"@{login or 'unknown'} · {item.get('created_at', '')}:\n{body}"


def route_github(url: str) -> Fetched:
    parsed = gh_repo_of(url)
    if not parsed:
        raise FetchError(["github: unparseable url"])
    owner, repo, kind, num = parsed
    if kind and num:
        thread_kind = "issues" if kind in ("issues",) else "issues"  # comments live under /issues/ for PRs too
        meta = json.loads(gh_api(f"repos/{owner}/{repo}/{thread_kind}/{num}"))
        comments = json.loads(gh_api(f"repos/{owner}/{repo}/issues/{num}/comments", ["--paginate"]) or "[]")
        parts = [meta.get("title", ""), attributed(meta)]
        parts += [attributed(c) for c in comments]
        if kind in ("pull", "pulls"):  # inline code-review comments live on a separate endpoint
            try:
                review_comments = json.loads(
                    gh_api(f"repos/{owner}/{repo}/pulls/{num}/comments", ["--paginate"]) or "[]"
                )
            except FetchError:
                review_comments = []
            parts += [attributed(c) for c in review_comments]
        return Fetched("\n\n---\n\n".join(p for p in parts if p), "gh-api-thread")
    meta = json.loads(gh_api(f"repos/{owner}/{repo}"))
    try:
        readme = gh_api(f"repos/{owner}/{repo}/readme", ["-H", "Accept: application/vnd.github.raw"])
    except FetchError:
        readme = ""
    text = (meta.get("description") or "") + "\n\n" + readme
    return Fetched(text, "gh-api-repo")


def discourse_topic_json_url(url: str) -> str:
    m = re.match(r"(https?://[^/]+/t/[^/]+/\d+)", url)
    return (m.group(1) if m else url.split("?")[0]) + ".json"


def route_discourse(url: str) -> Fetched:
    base = discourse_topic_json_url(url)
    data = http_get_json(base)
    stream = data.get("post_stream", {})
    have = {p["id"]: p for p in stream.get("posts", [])}
    all_ids = stream.get("stream", list(have.keys()))
    missing = [i for i in all_ids if i not in have]
    topic_root = base.rsplit("/", 1)[0]
    for i in range(0, len(missing), 50):
        chunk = missing[i:i + 50]
        qs = "&".join(f"post_ids[]={pid}" for pid in chunk)
        try:
            more = http_get_json(f"{topic_root.rsplit('/t/', 1)[0]}/t/{data['id']}/posts.json?{qs}")
            for p in more.get("post_stream", {}).get("posts", []):
                have[p["id"]] = p
        except Exception:  # noqa: BLE001 - best effort; first page already has the gist
            break
    ordered = [have[i] for i in all_ids if i in have]

    def attributed_post(p: dict) -> str:
        text = html_to_text(p.get("cooked", "").encode())
        if not text:
            return ""
        return f"@{p.get('username', 'unknown')} · {p.get('created_at', '')}:\n{text}"

    body = "\n\n---\n\n".join(t for t in (attributed_post(p) for p in ordered) if t)
    return Fetched(f"{data.get('title', '')}\n\n{body}", "discourse-json")


def route_reddit(url: str) -> Fetched:
    def walk(children):
        out = []
        for c in children:
            d = c.get("data", {})
            body = d.get("body") or d.get("selftext") or d.get("title", "")
            if body:
                created = d.get("created_utc")
                when = (datetime.fromtimestamp(created, tz=timezone.utc).isoformat()
                        if created else "")
                out.append(f"@{d.get('author', 'unknown')} · {when}:\n{body}")
            out += walk((d.get("replies") or {}).get("data", {}).get("children", []))
        return out

    path = url.split("//", 1)[1].split("/", 1)[1].split("?")[0].rstrip("/")
    tried = []
    for host in ("reddit.com", "old.reddit.com"):
        try:
            data = http_get_json(f"https://{host}/{path}.json", headers={"Accept": "application/json"})
        except Exception as e:  # noqa: BLE001 - reddit's anti-bot wall; try the next host
            tried.append(f"{host}: {e}")
            continue
        parts = walk(data[0]["data"]["children"]) if data else []
        parts += walk(data[1]["data"]["children"]) if len(data) > 1 else []
        return Fetched("\n\n---\n\n".join(parts), f"reddit-json-{host}")
    try:  # reddit's own anti-bot wall blocks both hosts' .json; a rendered page may pass
        return Fetched(browser_route(url), "browser")
    except Exception as e:  # noqa: BLE001
        tried.append(f"browser: {e}")
    raise FetchError(tried)


def route_hn(url: str) -> Fetched:
    m = re.search(r"[?&]id=(\d+)", url)
    if not m:
        raise FetchError(["hn: no item id in url"])
    data = http_get_json(f"https://hn.algolia.com/api/v1/items/{m.group(1)}")

    def walk(node: dict) -> list[str]:
        out = []
        text = node.get("text")
        if text:
            out.append(attributed({"body": html_to_text(text.encode()), "user": node.get("author"),
                                    "created_at": node.get("created_at")}, login_path=("user",)))
        for child in node.get("children") or []:
            out += walk(child)
        return out

    parts = [data.get("title", "")] + walk(data)
    return Fetched("\n\n---\n\n".join(p for p in parts if p), "hn-algolia")


def route_lobsters(url: str) -> Fetched:
    try:
        data = http_get_json(url.rstrip("/") + ".json")
        parts = [data.get("title", ""),
                 attributed({"body": data.get("description_plain", ""),
                             "user": data.get("submitter_user"), "created_at": data.get("created_at")},
                            login_path=("user",))]
        parts += [attributed({"body": c.get("comment_plain", ""),
                               "user": c.get("commenting_user"), "created_at": c.get("created_at")},
                              login_path=("user",))
                  for c in data.get("comments", [])]
        return Fetched("\n\n---\n\n".join(p for p in parts if p), "lobsters-json")
    except Exception as e:  # noqa: BLE001
        text = validate_page_text(html_to_text(http_get(url)))
        return Fetched(text, "html-fallback-after:" + str(e)[:80])


VTT_INLINE_TAG_RE = re.compile(r"<[^>]+>")
VTT_TIME_RANGE_RE = re.compile(r"(\d{2}):(\d{2}):(\d{2})\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}")
VTT_MARKER_EVERY_SECS = 60


def vtt_to_text(raw: str) -> str:
    """Flatten a yt-dlp auto-sub VTT into plain, deduplicated, timestamped text.

    YouTube's auto-captions are "rolling": each cue repeats the previous settled line, then
    grows a new line word by word with inline `<00:00:09.230><c>word</c>` timing tags. Naively
    stripping only the `-->` timing lines (the old approach) leaves those inline tags and the
    word-by-word growth in place, so the same phrase appears ~5-10x with mostly-duplicate,
    non-identical text - the actual cause of talks getting cut off well before their real
    length once a slice hits its char budget. A cue's last line is "settled" (one clean,
    complete phrase, no inline tags) once it has finished growing; every settled line appears
    exactly once, in order, so collecting only those reconstructs the transcript with no
    duplication and no gaps. A `[mm:ss]` marker is inserted roughly every 60s of video time.
    """
    out_lines: list[str] = []
    last_emitted = ""
    next_marker = 0
    pending: tuple[int, str] | None = None
    for block in raw.split("\n\n"):
        start_sec = None
        text_lines = []
        for ln in block.splitlines():
            m = VTT_TIME_RANGE_RE.search(ln)
            if m:
                start_sec = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
                continue
            s = ln.strip()
            if not s or s.isdigit() or ln.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
                continue
            text_lines.append(ln)
        if not text_lines or start_sec is None:
            continue
        last_line = text_lines[-1]
        cleaned = VTT_INLINE_TAG_RE.sub("", last_line).strip()
        if not cleaned:
            continue
        if "<" in last_line:  # still growing word-by-word; wait for its settled repeat
            pending = (start_sec, cleaned)
            continue
        if cleaned == last_emitted:
            pending = None
            continue
        if start_sec >= next_marker:
            out_lines.append(f"[{start_sec // 60:02d}:{start_sec % 60:02d}]")
            next_marker = start_sec + VTT_MARKER_EVERY_SECS
        out_lines.append(cleaned)
        last_emitted = cleaned
        pending = None
    if pending and pending[1] != last_emitted:  # video ended mid-cue; the tail wasn't repeated
        start_sec, cleaned = pending
        if start_sec >= next_marker:
            out_lines.append(f"[{start_sec // 60:02d}:{start_sec % 60:02d}]")
        out_lines.append(cleaned)
    return "\n".join(out_lines)


def route_video(url: str) -> Fetched:
    with tempfile.TemporaryDirectory() as td:
        out = subprocess.run(
            ["yt-dlp", "--write-auto-subs", "--skip-download", "--sub-lang", "en",
             "--sub-format", "vtt", "-o", f"{td}/%(id)s.%(ext)s", url],
            capture_output=True, timeout=90,
        )
        vtts = list(Path(td).glob("*.vtt"))
        if not vtts:
            raise FetchError([f"yt-dlp: no subtitles ({out.stderr.decode(errors='replace')[:150]})"])
        text = vtt_to_text(vtts[0].read_text(errors="replace"))
        if not text:
            raise FetchError(["yt-dlp: subtitles present but empty after cleanup"])
        return Fetched(text, "yt-dlp-subs")


def route_html(url: str) -> Fetched:
    tried = []
    for name, fn in (("html", lambda: validate_page_text(html_to_text(http_get_html(url)))),
                      ("wayback", lambda: wayback_fallback(url)),
                      ("browser", lambda: browser_route(url))):
        try:
            return Fetched(fn(), name)
        except Exception as e:  # noqa: BLE001 - route boundary, exhausted below
            tried.append(f"{name}: {e}")
    raise FetchError(tried)


def domain_of(url: str) -> str:
    return urllib.parse.urlparse(url).netloc.removeprefix("www.")


def fetch_by_class_route(url: str, source_class: str) -> Fetched:
    d = domain_of(url)
    if "reddit.com" in d:
        return route_reddit(url)
    if d in ("internals.rust-lang.org", "users.rust-lang.org", "forums.swift.org"):
        return route_discourse(url)
    if "github.com" in d:
        return route_github(url)
    if d in ("youtube.com", "youtu.be"):
        return route_video(url)
    if d == "news.ycombinator.com":
        return route_hn(url)
    if "lobste.rs" in d:
        return route_lobsters(url)
    if "books-courses" in source_class and d in PAYWALLED_DOMAINS:
        raise FetchError([f"paywalled domain {d}: not attempted (owner ruling, not a scraping project)"])
    return route_html(url)


# --- books: for books-courses, the book is the source, not its front page ------------

BOOK_MAX_PAGES = 60
BOOK_MAX_CHARS = 400_000
BOOK_LINK_RE = re.compile(rb'<a\s+[^>]*href="([^"#][^"]*)"[^>]*>(.*?)</a>', re.S)
BOOK_TAG_STRIP_RE = re.compile(rb"<[^>]+>")


class _BookPrintExtractor(_TextExtractor):
    """Like _TextExtractor, but marks each mdBook chapter boundary. mdBook's print.html
    concatenates the whole book as one page, one <h1> per chapter (plus a first, book-title
    <h1> from the menu) - marking every <h1> this way satisfies the "## <chapter title>"
    requirement without needing to separately track chapter names."""

    def handle_starttag(self, tag, attrs):
        super().handle_starttag(tag, attrs)
        if tag == "h1":
            self.chunks.append("## ")


def mdbook_print_to_text(raw: bytes) -> str:
    parser = _BookPrintExtractor()
    parser.feed(raw.decode("utf-8", errors="replace"))
    text = html.unescape("".join(parser.chunks))
    lines = [ln.strip() for ln in text.splitlines()]
    return "\n".join(ln for ln in lines if ln)


def looks_like_a_book(raw: bytes) -> bool:
    return raw.count(b"<h1") >= 3  # a lone 404/redirect page won't have this many


def print_html_url(root_url: str) -> str:
    return root_url.rstrip("/") + "/print.html"


def try_fetch_book_print_page(root_url: str) -> bytes | None:
    """mdBook sites publish a /print.html with the whole book on one page, in chapter
    order - by far the simplest, fewest-requests way to get a book's full text. Tried
    direct first, then via Wayback, for the given root and its www variant."""
    candidates = [root_url]
    parsed = urllib.parse.urlparse(root_url)
    if not parsed.netloc.startswith("www."):
        candidates.append(root_url.replace(parsed.netloc, "www." + parsed.netloc, 1))
    for candidate in candidates:
        target = print_html_url(candidate)
        try:
            raw = http_get(target)
            if looks_like_a_book(raw):
                return raw
        except Exception:  # noqa: BLE001 - try the next candidate/route
            pass
        try:
            raw = http_get(wayback_snapshot_url(target))
            if looks_like_a_book(raw):
                return raw
        except Exception:  # noqa: BLE001 - try the next candidate
            pass
    return None


def fetch_front_page_raw(root_url: str) -> tuple[bytes, str]:
    """The book's front page, and the base URL chapter links were resolved against (a
    Wayback snapshot URL if that's where the page came from - chapter links found on an
    archived page are already absolute into the Wayback machine, so no rewriting is
    needed)."""
    parsed = urllib.parse.urlparse(root_url)
    candidates = [root_url]
    if not parsed.netloc.startswith("www."):
        candidates.append(root_url.replace(parsed.netloc, "www." + parsed.netloc, 1))
    tried = []
    for candidate in candidates:
        try:
            return follow_client_redirect(candidate, http_get(candidate)), candidate
        except Exception as e:  # noqa: BLE001 - direct fetch failed; try wayback next
            tried.append(f"{candidate}: {e}")
    try:
        snap = wayback_snapshot_url(root_url)
        return http_get(snap), snap
    except Exception as e:  # noqa: BLE001 - exhausted; report every route tried
        tried.append(f"wayback({root_url}): {e}")
    raise FetchError(tried)


def _no_port(url: str) -> str:
    """Strip an explicit ':443'/':80'-style port before a '/' - a Wayback-archived page's
    own URL sometimes carries one while its sibling links (resolved relative, without a
    port) don't, which breaks a same-root prefix check that isn't port-blind."""
    return re.sub(r":\d+(?=/)", "", url)


def extract_same_root_links(raw: bytes, base_url: str) -> list[tuple[str, str]]:
    """(absolute_url, link_text) for every <a> under the same path-root as base_url, in
    document order, deduped - a book's table of contents when it has no print.html."""
    root = _no_port(base_url.rstrip("/"))
    seen: set[str] = {_no_port(base_url.split("#")[0].rstrip("/"))}
    out = []
    for m in BOOK_LINK_RE.finditer(raw):
        href = m.group(1).decode(errors="replace").strip()
        text = BOOK_TAG_STRIP_RE.sub(b"", m.group(2)).decode(errors="replace").strip()
        if not href or not text:
            continue
        abs_url = urllib.parse.urljoin(base_url, href).split("#")[0].rstrip("/")
        abs_url_normalized = _no_port(abs_url)
        if not abs_url_normalized.startswith(root) or abs_url_normalized in seen:
            continue
        seen.add(abs_url_normalized)
        out.append((abs_url, text))
    return out


def fetch_book(url: str) -> Fetched:
    """The book is the source, not its front page: fetch the whole thing, front page
    first, chapters after in table-of-contents order, capped at BOOK_MAX_PAGES fetches /
    BOOK_MAX_CHARS total. Prefers a single /print.html request when the site is mdBook;
    otherwise crawls the front page's own table-of-contents links."""
    print_raw = try_fetch_book_print_page(url)
    if print_raw is not None:
        text = mdbook_print_to_text(print_raw)
        if len(text) > BOOK_MAX_CHARS:
            text = text[:BOOK_MAX_CHARS] + f"\n[... truncated at {BOOK_MAX_CHARS:,} chars ...]\n"
        return Fetched(text, "book-print")

    front_raw, base_url = fetch_front_page_raw(url)
    front_text = html_to_text(front_raw)
    links = extract_same_root_links(front_raw, base_url)[:BOOK_MAX_PAGES]

    parts = [front_text]
    total = len(front_text)
    for chapter_url, title in links:
        if total >= BOOK_MAX_CHARS:
            break
        try:
            chapter_text = html_to_text(http_get(chapter_url))
        except Exception:  # noqa: BLE001 - one missing chapter shouldn't sink the book
            continue
        piece = f"## {title}\n{chapter_text}"
        parts.append(piece[:max(0, BOOK_MAX_CHARS - total)])
        total += len(piece)
    text = "\n\n".join(parts)
    if len(text) > BOOK_MAX_CHARS:
        text = text[:BOOK_MAX_CHARS] + f"\n[... truncated at {BOOK_MAX_CHARS:,} chars ...]\n"
    return Fetched(text, "book-crawl")


# --- subcommands ----------------------------------------------------------

def cmd_get(doi_or_url: str) -> int:
    hit = find_cached(doi_or_url)
    if hit:
        print(CACHE / f"{hit['key']}.txt" if hit["route"] != "abstract" else CACHE / f"{hit['key']}.abstract.txt")
        return 0
    query = doi_or_url
    if is_doi(query):
        doi = normalize_doi(query)
        key = doi_key(doi)
        try:
            fetched = fetch_by_doi(doi)
        except FetchError as e:
            print(f"FAILED {doi}: {'; '.join(e.tried)}", file=sys.stderr)
            return 1
        path = save_text(key, fetched.text, fetched.route, doi_or_url, abstract=fetched.route == "abstract")
        print(path)
        return 0
    key = url_key(query)
    try:
        fetched = route_html(query)
    except FetchError as e:
        print(f"FAILED {query}: {'; '.join(e.tried)}", file=sys.stderr)
        return 1
    path = save_text(key, fetched.text, fetched.route, doi_or_url)
    print(path)
    return 0


def cmd_ingest_tmp() -> int:
    pdfs = sorted(Path("/tmp").glob("*.pdf"))
    ingested, skipped = 0, []
    for pdf in pdfs:
        try:
            text = pdf_to_text(pdf)
        except Exception as e:  # noqa: BLE001
            skipped.append(f"{pdf.name}: pdftotext failed ({e})")
            continue
        matches = list(DOI_RE.finditer(text[:6000]))
        if matches:
            # pdftotext sometimes wraps a DOI across a line break, leaving a truncated
            # match earlier in the text (e.g. "10.1371/journal."); the full one is longer.
            longest = max(matches, key=lambda mm: len(mm.group(0)))
            doi = normalize_doi(longest.group(0).rstrip(".,);"))
        elif ARXIV_ID_RE.match(pdf.stem):
            # arXiv registers a DOI (10.48550/arXiv.<id>) for every paper since Feb 2022;
            # the filename already carries that id, so no scraping is needed to recover it.
            doi = f"10.48550/arXiv.{pdf.stem}"
        else:
            skipped.append(f"{pdf.name}: no DOI in first pages, filename isn't an arXiv id")
            continue
        key = doi_key(doi)
        if find_cached(doi):
            continue
        save_text(key, text, "tmp-ingest", doi)
        ingested += 1
    print(f"ingested={ingested} skipped={len(skipped)}")
    for s in skipped:
        print(f"  skip: {s}")
    return 0


DEFAULT_STATUS_CSV = (
    "/Users/ryzhakar/pp/gym/docs/orchestration_log/recon/2026-09-27/research/"
    "rust-map/samples/prefetch-b1-status.csv"
)


def cmd_fetch_csv(csv_path: str, status_csv: str = DEFAULT_STATUS_CSV) -> int:
    rows = list(csv.DictReader(Path(csv_path).open(newline="")))
    status_path = Path(status_csv)
    is_new = not status_path.exists()
    with status_path.open("a", newline="") as sf:
        w = csv.writer(sf)
        if is_new:
            w.writerow(["id", "url", "class", "status", "key", "chars", "route"])
        for row in rows:
            url, source_class, rid = row["url"], row["class"], row["id"]
            hit = find_cached(url)
            if hit:
                w.writerow([rid, url, source_class, "cached", hit["key"], hit["chars"], hit["route"]])
                continue
            key = url_key(url)
            try:
                fetched = fetch_by_class_route(url, source_class)
            except FetchError as e:
                w.writerow([rid, url, source_class, "failed", "", 0, "; ".join(e.tried)[:300]])
                continue
            except Exception as e:  # noqa: BLE001
                w.writerow([rid, url, source_class, "failed", "", 0, f"unexpected: {e}"[:300]])
                continue
            save_text(key, fetched.text, fetched.route, url)
            w.writerow([rid, url, source_class, "fetched", key, len(fetched.text), fetched.route])
    print(f"wrote {status_path}")
    return 0


def cmd_fetch_book(url: str) -> int:
    """books-courses: the book is the source. Fetches the whole book (print.html when the
    site is mdBook, else a table-of-contents crawl) and saves it under the URL's own key,
    same as a normal fetch - `get`/`fetch-csv` will pick it up as any other cache hit."""
    try:
        fetched = fetch_book(url)
    except FetchError as e:
        print(f"FAILED {url}: {'; '.join(e.tried)}", file=sys.stderr)
        return 1
    path = save_text(url_key(url), fetched.text, fetched.route, url)
    print(path)
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd, rest = argv[1], argv[2:]
    if cmd == "get" and rest:
        return cmd_get(rest[0])
    if cmd == "ingest-tmp":
        return cmd_ingest_tmp()
    if cmd == "fetch-csv" and rest:
        return cmd_fetch_csv(*rest[:2])
    if cmd == "fetch-book" and rest:
        return cmd_fetch_book(rest[0])
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
