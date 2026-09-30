"""Test for the map site generator. Run: `uv run pytest tests/map/test_site.py`."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

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


def _load_yaml_kind(map_dir: Path, name: str) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for f in sorted((map_dir / name).glob("*.yaml")):
        out[f.stem] = yaml.safe_load(f.read_text()) or {}
    return out


def test_graph_node_and_edge_counts_match_a_direct_pass_over_maps_rust(
    tmp_path: Path,
) -> None:
    """Independently re-derive the Graph's nodes and edges straight from the
    YAML files -- not by calling gym.map.site's own graph builder -- and
    check the built page's embedded data agrees. Concept-Concept edges are
    read from concept.related only; never inferred from co-occurrence."""
    map_dir = ROOT / "maps" / "rust"
    questions = _load_yaml_kind(map_dir, "questions")
    positions = _load_yaml_kind(map_dir, "positions")
    arguments = _load_yaml_kind(map_dir, "arguments")
    concepts = _load_yaml_kind(map_dir, "concepts")
    domains = _load_yaml_kind(map_dir, "domains")
    values = _load_yaml_kind(map_dir, "values")

    degree: dict[str, float] = defaultdict(float)
    edge_count = 0
    cc_edges = 0

    for qid, q in questions.items():
        for cid in q.get("concepts") or []:
            if cid in concepts:
                degree[f"question:{qid}"] += 1
                degree[f"concept:{cid}"] += 1
                edge_count += 1
        for did in q.get("domains") or []:
            if did in domains:
                degree[f"question:{qid}"] += 1
                degree[f"domain:{did}"] += 1
                edge_count += 1

    pos_to_question = {pid: p.get("question") for pid, p in positions.items()}
    qv_weight: dict[tuple[str, str], int] = defaultdict(int)
    for a in arguments.values():
        qid = pos_to_question.get(a.get("position"))
        if qid not in questions:
            continue
        for vid in a.get("values") or []:
            if vid in values:
                qv_weight[(qid, vid)] += 1
    for (qid, vid), w in qv_weight.items():
        degree[f"question:{qid}"] += w
        degree[f"value:{vid}"] += w
        edge_count += 1

    for cid, c in concepts.items():
        for rid in c.get("related") or []:
            if rid in concepts:
                degree[f"concept:{cid}"] += 1
                degree[f"concept:{rid}"] += 1
                edge_count += 1
                cc_edges += 1

    expected_node_count = sum(1 for d in degree.values() if d > 0)

    out = tmp_path / "index.html"
    build_site(map_dir, out)
    data = _load_data(out)
    graph = data["graph"]

    assert graph["counts"]["nodes_full"] == expected_node_count
    assert graph["counts"]["edges_full"] == edge_count
    assert graph["concept_concept_count"] == cc_edges
    # This map's concept.related is unpopulated today -- the one edge type
    # the data does not supply -- and the legend must say so, not infer it.
    assert cc_edges == 0
    assert len(graph["nodes"]) == expected_node_count
    assert len(graph["edges"]) == edge_count


def test_graph_default_subset_includes_domains_and_values(tmp_path: Path) -> None:
    """v1 default-subset rule: Concepts of degree >=3, their Questions, and
    every Domain/Value those Questions link to -- independently re-derived
    from the YAML (not via gym.map.site.build_graph_data) and checked
    against the built page's embedded data. v0's rule stopped at the
    Questions, so no Domain or Value ever appeared without "Show all"."""
    map_dir = ROOT / "maps" / "rust"
    questions = _load_yaml_kind(map_dir, "questions")
    positions = _load_yaml_kind(map_dir, "positions")
    arguments = _load_yaml_kind(map_dir, "arguments")
    concepts = _load_yaml_kind(map_dir, "concepts")
    domains = _load_yaml_kind(map_dir, "domains")
    values = _load_yaml_kind(map_dir, "values")

    degree: dict[str, float] = defaultdict(float)
    q_concepts: dict[str, set[str]] = defaultdict(set)
    q_domains: dict[str, set[str]] = defaultdict(set)
    for qid, q in questions.items():
        for cid in q.get("concepts") or []:
            if cid in concepts:
                degree[f"concept:{cid}"] += 1
                q_concepts[qid].add(cid)
        for did in q.get("domains") or []:
            if did in domains:
                q_domains[qid].add(did)

    pos_to_question = {pid: p.get("question") for pid, p in positions.items()}
    q_values: dict[str, set[str]] = defaultdict(set)
    for a in arguments.values():
        qid = pos_to_question.get(a.get("position"))
        if qid not in questions:
            continue
        for vid in a.get("values") or []:
            if vid in values:
                q_values[qid].add(vid)

    expected_default_concepts = {cid for cid in concepts if degree.get(f"concept:{cid}", 0) >= 3}
    expected_default_questions = {
        qid for qid, cids in q_concepts.items() if cids & expected_default_concepts
    }
    expected_default_domains = {
        did for qid in expected_default_questions for did in q_domains.get(qid, ())
    }
    expected_default_values = {
        vid for qid in expected_default_questions for vid in q_values.get(qid, ())
    }

    out = tmp_path / "index.html"
    build_site(map_dir, out)
    data = _load_data(out)
    graph = data["graph"]
    node_by_id = {n["id"]: n for n in graph["nodes"]}
    default_ids = set(graph["default_subset"])

    got_by_kind: dict[str, set[str]] = defaultdict(set)
    for nid in default_ids:
        n = node_by_id[nid]
        got_by_kind[n["kind"]].add(n["raw"])

    assert got_by_kind["concept"] == expected_default_concepts
    assert got_by_kind["question"] == expected_default_questions
    assert got_by_kind["domain"] == expected_default_domains
    assert got_by_kind["value"] == expected_default_values
    assert len(default_ids) == graph["counts"]["nodes_default"]
    # v1's own contribution: every Domain and every Value appears, unlike v0.
    assert expected_default_domains == set(domains)
    assert expected_default_values == set(values)


def test_graph_view_switch_and_node_click_opens_panel() -> None:
    from playwright.sync_api import sync_playwright

    out = ROOT / ".pytest_graph_view_tmp.html"
    try:
        build_site(ROOT / "maps" / "rust", out)
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1600, "height": 1000})
            console_errors: list[str] = []
            page.on(
                "console",
                lambda msg: console_errors.append(msg.text)
                if msg.type == "error"
                else None,
            )
            page.on("pageerror", lambda exc: console_errors.append(str(exc)))

            page.goto(out.resolve().as_uri())
            page.click("#btn-view-graph")
            page.wait_for_selector("svg#graph .gnode")
            assert page.eval_on_selector(
                "#graphwrap", "el => el.style.display"
            ) != "none"

            # A force layout can leave nodes visually overlapping, so the
            # node is clicked by dispatching straight to its element rather
            # than relying on Playwright's pointer-hit-testing.
            node = page.query_selector("svg#graph .gnode")
            assert node is not None
            node.evaluate("el => el.dispatchEvent(new MouseEvent('click', {bubbles: true}))")
            page.wait_for_selector("#panel.open")
            panel_text = page.inner_text("#panel-body")
            # The panel's field-label CSS applies text-transform: uppercase,
            # which Playwright's rendered inner_text reflects -- compare
            # case-insensitively rather than against the literal source text.
            assert "neighbours" in panel_text.lower()

            assert console_errors == []
            browser.close()
    finally:
        out.unlink(missing_ok=True)
