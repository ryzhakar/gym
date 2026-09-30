"""Test for the map site generator. Run: `uv run pytest tests/map/test_site.py`."""

from __future__ import annotations

import json
import re
from pathlib import Path

from gym.map.site import main as build_site
from gym.paths import ROOT


def _load_data(out: Path) -> dict:
    html = out.read_text(encoding="utf-8")
    m = re.search(
        r'<script id="data" type="application/json">(.*?)</script>', html, re.S
    )
    assert m is not None
    return json.loads(m.group(1))


def test_site_builds_on_rust_map(tmp_path: Path) -> None:
    out = tmp_path / "index.html"
    build_site(ROOT / "maps" / "rust", out)
    assert out.exists()
    assert out.stat().st_size > 100_000
    # Spec asked for the literal string "Voice 1"; it never appears in the
    # static file (or in the prototype's own committed index.html) because
    # voice labels ("Voice " + index) are computed client-side by the page's
    # JS, not baked in by the Python builder. Asserting the JS fragment that
    # does the labelling instead, verbatim and stable through reorder/drag:
    # numbers come from `voiceNumber`, assigned once in `resetOrders`, never
    # from the live `colOrder` position. See migrate-map-report.md for the
    # full note on the original "Voice 1" assertion.
    html = out.read_text(encoding="utf-8")
    assert (
        'return "Voice " + (voiceNumber.hasOwnProperty(vid) ? voiceNumber[vid] : "?");'
        in html
    )


def test_default_subset_is_a_fixed_point(tmp_path: Path) -> None:
    out = tmp_path / "index.html"
    build_site(ROOT / "maps" / "rust", out)
    data = _load_data(out)
    default = data["default_subset"]
    questions = set(default["questions"])
    voices = set(default["voices"])

    # Re-derive both filters restricted to this subset; a true fixed point
    # is unchanged by one more round of both filters.
    q_voices: dict[str, set[str]] = {}
    q_positions: dict[str, set[str]] = {}
    v_questions: dict[str, set[str]] = {}
    for cell in data["matrix"]:
        if cell["v"] in voices:
            q_voices.setdefault(cell["q"], set()).add(cell["v"])
            q_positions.setdefault(cell["q"], set()).add(cell["position"])
        if cell["q"] in questions:
            v_questions.setdefault(cell["v"], set()).add(cell["q"])

    for qid in questions:
        assert len(q_voices.get(qid, set())) >= 2
        assert len(q_positions.get(qid, set())) >= 2
    for vid in voices:
        assert len(v_questions.get(vid, set())) >= 2

    # Reported against the prototype's one-pass 113 x 61: iterating the two
    # filters to a fixed point (a bipartite 2-core) is strictly tighter,
    # since a one-pass survivor can depend on a partner the other filter
    # later removes. Measured on the current maps/rust data — see the
    # site-v02 report for the run this asserts against.
    assert (len(questions), len(voices)) == (41, 43)
    assert data["meta"]["default"]["cells"] == len(
        [c for c in data["matrix"] if c["q"] in questions and c["v"] in voices]
    )


def test_checked_marker_present_in_data(tmp_path: Path) -> None:
    out = tmp_path / "index.html"
    build_site(ROOT / "maps" / "rust", out)
    data = _load_data(out)
    claims = data["claims"]
    checked = [c for c in claims.values() if c["checked"]]
    provisional = [c for c in claims.values() if not c["checked"]]
    assert checked and provisional
    sample = next(c for c in checked)
    assert set(["date", "method", "verdict"]).issubset(sample["checked"].keys())
    # "practiced" is dropped: nothing in the page's data or script should
    # still read that field for the checked/provisional distinction.
    html = out.read_text(encoding="utf-8")
    assert "practiced" not in html


def test_voice_numbering_stable_through_drag(tmp_path: Path) -> None:
    """A dragged column keeps its "Voice N" label; only its position moves."""
    from playwright.sync_api import sync_playwright

    out = tmp_path / "index.html"
    build_site(ROOT / "maps" / "rust", out)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1600, "height": 1000})
        page.goto(out.resolve().as_uri())
        page.wait_for_selector("svg#matrix text.lbl[data-axis='col']")

        def col_labels() -> dict[str, str]:
            return {
                h["id"]: h["text"]
                for h in page.eval_on_selector_all(
                    "svg#matrix text.lbl[data-axis='col']",
                    "els => els.map(e => ({id: e.getAttribute('data-id'), "
                    "text: e.textContent}))",
                )
            }

        before = col_labels()
        assert len(before) >= 2
        first_id, second_id = list(before.keys())[0], list(before.keys())[1]

        boxes = {
            h["id"]: h["box"]
            for h in page.eval_on_selector_all(
                "svg#matrix rect.hit[data-axis='col']",
                """els => els.map(e => {
                    const r = e.getBoundingClientRect();
                    return {id: e.getAttribute('data-id'), box: {x: r.x, y: r.y, w: r.width, h: r.height}};
                })""",
            )
        }
        b1, b2 = boxes[first_id], boxes[second_id]
        page.mouse.move(b1["x"] + b1["w"] / 2, b1["y"] + b1["h"] / 2)
        page.mouse.down()
        page.mouse.move(b1["x"] + b1["w"] / 2 + 20, b1["y"] + b1["h"] / 2, steps=5)
        page.mouse.move(b2["x"] + b2["w"] / 2, b2["y"] + b2["h"] / 2, steps=5)
        page.mouse.up()

        after = col_labels()
        browser.close()

    # The drag moved a column (order changed)...
    assert list(before.keys()) != list(after.keys())
    # ...but every Voice id's own label text is unchanged.
    assert before[first_id] == after[first_id]
    assert before[second_id] == after[second_id]
    for vid, text in before.items():
        assert after.get(vid) == text
