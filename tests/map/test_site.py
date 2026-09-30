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
    # does the labelling instead, verbatim: numbers come from the page-wide
    # `DATA.voice_number` (load.py, assigned once over all sorted voice ids),
    # not from the Matrix's own subset/column order -- this is what makes a
    # Voice's number the same in the Matrix and the Graph panel (owner
    # ruling 2026-09-30).
    html = out.read_text(encoding="utf-8")
    assert (
        'return "Voice " + (DATA.voice_number.hasOwnProperty(vid) ? DATA.voice_number[vid] : "?");'
        in html
    )
    assert '"voice_number":' in html


def test_default_subset_is_a_fixed_point(tmp_path: Path) -> None:
    """The Matrix's own bipartite-fixed-point filter is retired (owner ruling
    2026-09-30): the default view is now cocluster()'s non-thin core exactly,
    row/col order and all (src/gym/map/cluster.py, wired in matrix.py)."""
    out = tmp_path / "index.html"
    build_site(ROOT / "maps" / "rust", out)
    data = _load_data(out)
    clustering = data["clustering"]
    default = data["default_subset"]

    core_questions = set(clustering["row_order"]) - set(clustering["thin_rows"])
    core_voices = set(clustering["col_order"]) - set(clustering["thin_cols"])
    assert set(default["questions"]) == core_questions
    assert set(default["voices"]) == core_voices

    # cocluster()'s own 2-core is degree-only (min_row_degree=2 surviving
    # Voices, min_col_degree=2 surviving Questions) -- the old standalone
    # filter's extra ">= 2 distinct Positions per Question" requirement is
    # gone along with it, since it was never part of cocluster()'s thin rule.
    q_voices: dict[str, set[str]] = {}
    v_questions: dict[str, set[str]] = {}
    for cell in data["matrix"]:
        if cell["v"] in core_voices and cell["q"] in core_questions:
            q_voices.setdefault(cell["q"], set()).add(cell["v"])
            v_questions.setdefault(cell["v"], set()).add(cell["q"])
    for qid in core_questions:
        assert len(q_voices.get(qid, set())) >= 2
    for vid in core_voices:
        assert len(v_questions.get(vid, set())) >= 2

    # Measured on the current maps/rust data with cocluster()'s defaults
    # (min_row_degree=2, min_col_degree=2); matches cocluster-report.md's
    # 62 Questions / 51 Voices across the 5 live blocks.
    assert (len(core_questions), len(core_voices)) == (62, 51)
    assert data["meta"]["default"]["cells"] == len(
        [
            c
            for c in data["matrix"]
            if c["q"] in core_questions and c["v"] in core_voices
        ]
    )


def test_matrix_blocks_render_and_row_order_matches_clustering(
    tmp_path: Path,
) -> None:
    """Block outlines render in the Matrix view for maps/rust, dashed and
    labelled "discussion" exactly where a block's agreement is under 0.75,
    and the row order the Matrix draws is cocluster()'s row_order (core
    prefix, thin rows parked at the end)."""
    from playwright.sync_api import sync_playwright

    out = tmp_path / "index.html"
    build_site(ROOT / "maps" / "rust", out)
    data = _load_data(out)
    clustering = data["clustering"]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1600, "height": 1000})
        page.goto(out.resolve().as_uri())
        page.click("#btn-view-matrix")
        page.wait_for_selector("svg#matrix rect.block-outline")

        outline_count = page.eval_on_selector_all(
            "svg#matrix rect.block-outline", "els => els.length"
        )
        discussion_count = page.eval_on_selector_all(
            "svg#matrix rect.block-outline.block-discussion", "els => els.length"
        )
        row_ids = page.eval_on_selector_all(
            "svg#matrix text.lbl[data-axis='row']",
            "els => els.map(e => e.getAttribute('data-id'))",
        )
        browser.close()

    live_blocks = [b for b in clustering["blocks"] if b["rows"] and b["cols"]]
    assert outline_count == len(live_blocks)
    assert outline_count > 0
    expected_discussion = sum(1 for b in live_blocks if b["agreement"] < 0.75)
    assert discussion_count == expected_discussion

    n_thin = len(clustering["thin_rows"])
    core_row_order = clustering["row_order"][
        : len(clustering["row_order"]) - n_thin
    ]
    assert row_ids == core_row_order


def test_matrix_voice_numbers_match_shared_numbering(tmp_path: Path) -> None:
    """A Voice's "Voice N" label in the Matrix is DATA.voice_number[vid] --
    the same numbering the Graph panel's Claim list shows (owner ruling
    2026-09-30: one stable number per Voice for the whole page)."""
    from playwright.sync_api import sync_playwright

    out = tmp_path / "index.html"
    build_site(ROOT / "maps" / "rust", out)
    data = _load_data(out)
    voice_number = data["voice_number"]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1600, "height": 1000})
        page.goto(out.resolve().as_uri())
        page.click("#btn-view-matrix")
        page.wait_for_selector("svg#matrix text.lbl[data-axis='col']")
        cols = page.eval_on_selector_all(
            "svg#matrix text.lbl[data-axis='col']",
            "els => els.map(e => ({id: e.getAttribute('data-id'), "
            "text: e.textContent}))",
        )
        browser.close()

    assert cols
    for c in cols:
        assert c["text"] == "Voice " + str(voice_number[c["id"]])


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
        # The Concept graph is the front door now (owner ruling 2026-09-30),
        # so the Matrix is one click away rather than the landing view.
        page.click("#btn-view-matrix")
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
