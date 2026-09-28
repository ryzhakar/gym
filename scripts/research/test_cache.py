"""Tests for the batch-2 additions to cache.py. Run: `uv run --with pytest pytest scripts/research/test_cache.py`."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import cache  # noqa: E402

BEVY_REDIRECT = (b'<!doctype html><script>window.location.replace(target + hash);</script><noscript>'
                 b'<meta content="0; url=https://bevy.org/learn/quick-start/introduction/" http-equiv=refresh></noscript>')


def test_redirect_with_reversed_unquoted_meta_attributes() -> None:
    match = cache.CLIENT_REDIRECT_RE.search(BEVY_REDIRECT)
    assert next(g for g in match.groups() if g) == b"https://bevy.org/learn/quick-start/introduction/"


def test_redirect_classic_forms_still_match() -> None:
    for raw in (b'<script>location.replace("/2/")</script>', b'<meta http-equiv="refresh" content="0; url=/next">'):
        assert cache.CLIENT_REDIRECT_RE.search(raw)


def test_toc_from_a_chapter_entry_with_unquoted_links() -> None:
    page = b'<a href=/learn/quick-start/setup/>Setup</a><a href="../apps/">Apps</a><a href=https://x.org/y>Out</a>'
    links = cache.extract_toc_links(page, "https://bevy.org/learn/quick-start/introduction/")
    assert [url for url, _ in links] == ["https://bevy.org/learn/quick-start/setup", "https://bevy.org/learn/quick-start/apps"]


def test_book_classes_and_paywall() -> None:
    assert cache.is_book_class("books-courses;twir-links") and cache.is_book_class("books")
    assert not cache.is_book_class("talks")
    try:
        cache.fetch_by_class_route("https://dpunkt.de/produkt/rust", "books", "de")
    except cache.FetchError as error:
        assert "paywalled" in error.tried[0]
    else:
        raise AssertionError("paywalled book was fetched")


def test_book_roots_climb_from_a_chapter_page() -> None:
    assert cache.book_root_candidates("https://plotly.github.io/plotly.rs/content/getting_started.html") == [
        "https://plotly.github.io/plotly.rs/content/getting_started.html", "https://plotly.github.io/plotly.rs/content",
        "https://plotly.github.io/plotly.rs", "https://plotly.github.io/"]
    assert cache.book_root_candidates("https://x.org/")[0] == "https://x.org/"


def test_whole_rustcc_page_passes_below_the_length_floor() -> None:
    page = "标题\n发表于 2024-03-07\n正文\n评论区\n还没有评论\n©2016~2020 Rust.cc 版权所有"
    assert cache.validate_page_text(page, url="https://rustcc.cn/article?id=x") == page
    try:
        cache.validate_page_text("评论区 only", url="https://rustcc.cn/article?id=y")
    except cache.FetchError:
        pass
    else:
        raise AssertionError("a page missing the footer passed")
