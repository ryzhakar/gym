"""The Concept graph: what it draws, and what a reader can do with it.

Run: `uv run pytest tests/map/test_graph_map.py`.

Every count here is re-derived straight from the YAML, never by calling the
builder's own graph code, so a change that moves both at once still fails.
The browser test writes the four screenshots in the report.
"""

from __future__ import annotations

import itertools
import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

from gym.map.site import main as build_site
from gym.map.site.load import canonical_map
from gym.map.site.page import build_data
from gym.paths import ROOT

MAP = ROOT / "maps" / "rust"
SHOTS = ROOT / "docs" / "orchestration_log" / "recon" / "2026-09-30" / "frontend"


def _yaml_kind(map_dir: Path, name: str) -> dict[str, dict]:
    return {
        f.stem: yaml.safe_load(f.read_text()) or {}
        for f in sorted((map_dir / name).glob("*.yaml"))
    }


def _independent_pass(map_dir: Path) -> tuple[dict[tuple[str, str], set[str]], dict[str, int]]:
    """Edges and weighted degrees, derived here and nowhere else.

    Reads the `merged_into` contract the same way the page must: follow it
    to a fixed point, treat a missing field as canonical, and deduplicate a
    Question's Concepts after resolving them, so two raw ids that fold into
    one Concept make no self-loop.
    """
    questions = _yaml_kind(map_dir, "questions")
    concepts = _yaml_kind(map_dir, "concepts")

    def resolve(cid: str) -> str:
        walked = [cid]
        cur = cid
        while True:
            nxt = (concepts.get(cur) or {}).get("merged_into")
            if not nxt or nxt not in concepts:
                return cur
            if nxt in walked:
                cycle = walked[walked.index(nxt):]
                return min(cycle)
            walked.append(nxt)
            cur = nxt

    edges: dict[tuple[str, str], set[str]] = defaultdict(set)
    for qid, q in questions.items():
        cids = sorted({resolve(c) for c in (q.get("concepts") or []) if c in concepts})
        for a, b in itertools.combinations(cids, 2):
            edges[(a, b)].add(qid)
    degree: dict[str, int] = defaultdict(int)
    for (a, b), qs in edges.items():
        degree[a] += len(qs)
        degree[b] += len(qs)
    return dict(edges), dict(degree)


def test_canonical_resolution_follows_merged_into(tmp_path: Path) -> None:
    """A chain resolves to its end, a cycle to its smallest member, a
    pointer at an id the map does not hold stops where it stands."""
    concepts = {
        "a": {"merged_into": "b"},
        "b": {"merged_into": "c"},
        "c": {},
        "plain": {},
        "x": {"merged_into": "y"},
        "y": {"merged_into": "x"},
        "into_cycle": {"merged_into": "y"},
        "dangling": {"merged_into": "not-a-concept"},
        "empty": {"merged_into": None},
    }
    canon = canonical_map(concepts)
    assert canon["a"] == "c"
    assert canon["b"] == "c"
    assert canon["c"] == "c"
    assert canon["plain"] == "plain"
    assert canon["x"] == canon["y"] == "x"
    # "into_cycle" sorts before "x" but is not on the cycle, so it does not win
    assert canon["into_cycle"] == "x"
    assert canon["dangling"] == "dangling"
    assert canon["empty"] == "empty"


def test_edges_equal_an_independent_pass_over_the_data() -> None:
    edges, degree = _independent_pass(MAP)
    data = build_data(MAP)
    g = data["graph"]

    assert g["stats"]["nodes"] == len(degree)
    assert g["stats"]["edges"] == len(edges)
    assert len(g["ids"]) == len(degree)
    assert g["ids"] == sorted(degree)
    assert g["deg"] == [degree[c] for c in g["ids"]]

    index = {cid: i for i, cid in enumerate(g["ids"])}
    built: dict[tuple[str, str], set[str]] = {}
    for k in range(len(g["e_a"])):
        a, b = g["ids"][g["e_a"][k]], g["ids"][g["e_b"][k]]
        assert a < b, "an edge is stored once, with its ends in id order"
        built[(a, b)] = {g["qids"][q] for q in g["e_q"][k]}
    assert built == edges

    # The weight a reader sees is the length of the Question list and nothing
    # else -- the one rule the whole view rests on.
    for pair, qs in built.items():
        assert len(qs) == len(edges[pair])
    assert sum(len(v) for v in built.values()) == g["stats"]["weight_total"]
    assert g["stats"]["max_weight"] == max(len(v) for v in built.values())
    assert index  # ids are indexable, which is how the page addresses them


def test_no_edge_the_data_does_not_hold() -> None:
    """Every Question on an edge really touches both of that edge's Concepts."""
    questions = _yaml_kind(MAP, "questions")
    concepts = _yaml_kind(MAP, "concepts")
    canon = canonical_map(concepts)
    q_sets = {
        qid: {canon[c] for c in (q.get("concepts") or []) if c in concepts}
        for qid, q in questions.items()
    }
    g = build_data(MAP)["graph"]
    for k in range(len(g["e_a"])):
        a, b = g["ids"][g["e_a"][k]], g["ids"][g["e_b"][k]]
        for qi in g["e_q"][k]:
            qs = q_sets[g["qids"][qi]]
            assert a in qs and b in qs


def test_every_node_carries_a_community() -> None:
    g = build_data(MAP)["graph"]
    n = len(g["ids"])
    assert len(g["comm"]) == n
    assert min(g["comm"]) >= 0
    assert max(g["comm"]) < len(g["communities"])
    sizes = defaultdict(int)
    for c in g["comm"]:
        sizes[c] += 1
    assert sum(sizes.values()) == n, "communities cover every node exactly once"
    for i, row in enumerate(g["communities"]):
        assert row["size"] == sizes[i]
        assert row["name"] and row["color"]
    assert g["stats"]["communities"] == len(g["communities"])
    # Nodes are every canonical Concept with an edge -- no hidden subset.
    _, degree = _independent_pass(MAP)
    assert set(g["ids"]) == {c for c, d in degree.items() if d >= 1}


def test_communities_are_deterministic() -> None:
    a = build_data(MAP)["graph"]
    b = build_data(MAP)["graph"]
    assert a["comm"] == b["comm"]
    assert [r["name"] for r in a["communities"]] == [r["name"] for r in b["communities"]]


def test_graph_page_is_readable_and_walkable(tmp_path: Path) -> None:
    """Drive the page: hover, click, search, local mode, zoom, and shoot it."""
    from playwright.sync_api import sync_playwright

    out = tmp_path / "index.html"
    build_site(MAP, out)
    SHOTS.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1600, "height": 1000})
        errors: list[str] = []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(out.resolve().as_uri())
        page.wait_for_selector("#gscene .gnode")

        layout_ms = page.evaluate("() => window.__gym.layoutMs")
        node_count = page.evaluate("() => window.__gym.nodes")
        print("settle time (ms):", layout_ms, "nodes:", node_count)
        assert layout_ms < 3000, "layout must settle inside 3 s or ship precomputed"
        page.screenshot(path=str(SHOTS / "map-default.png"))

        base_labels = page.evaluate("() => window.__gym.visibleLabels()")
        assert base_labels > 0

        # the detached clusters start off the frame; their legend row is the
        # switch, and it says which way it will go
        row = page.inner_text("#glegend .row")
        assert "detached in" in row and row.strip().endswith("show"), row
        body_only = page.inner_text("#stat")
        page.eval_on_selector("#glegend .row", "el => el.click()")
        page.wait_for_timeout(250)
        assert page.inner_text("#glegend .row").strip().endswith("hide")
        with_islands = page.inner_text("#stat")
        assert body_only != with_islands
        print("stat, body only:", body_only, "| with clusters:", with_islands)
        # the detached clusters sit in a band under the body, not a ring
        # around it: their rows start below the lowest connected Concept.
        spread = page.evaluate("""() => {
          const g = window.__gym;
          return g.islandBand();
        }""")
        assert spread["bandTop"] >= spread["bodyBottom"], spread
        assert spread["bandWidth"] <= spread["bodyWidth"] * 1.6, spread
        print("island band:", spread)
        page.eval_on_selector("#glegend .row", "el => el.click()")
        page.wait_for_timeout(250)
        assert page.inner_text("#stat") == body_only

        # a label is its Concept: clicking the name pins the dot
        shown = page.eval_on_selector_all(
            "#glabels .glabel",
            "els => els.filter(e => e.style.display === 'block')"
            ".map(e => e.textContent)",
        )
        assert shown, "the opening frame names some Concepts"
        page.eval_on_selector_all(
            "#glabels .glabel",
            "els => { const e = els.find(x => x.style.display === 'block');"
            " const r = e.getBoundingClientRect();"
            " e.dispatchEvent(new PointerEvent('pointerdown',"
            " {bubbles: true, clientX: r.x + r.width / 2, clientY: r.y + r.height / 2})); }",
        )
        page.mouse.up()
        page.wait_for_selector("#panel.open")
        assert page.inner_text("#panel-body h2") == shown[0]
        print("label click:", shown[0], "->", page.evaluate("() => window.__gym.pinned()"))
        page.keyboard.press("Escape")
        page.wait_for_timeout(150)

        # hover: the Concept and its neighbours are named, the rest dims
        assert page.evaluate("() => window.__gym.hover('unsafe')")
        page.wait_for_timeout(120)
        assert page.eval_on_selector("#gscene", "el => el.classList.contains('focus')")
        hover_labels = page.evaluate("() => window.__gym.visibleLabels()")
        named = page.eval_on_selector_all(
            "#glabels .glabel.near", "els => els.map(e => e.textContent)"
        )
        assert "unsafe" in named, named[:10]
        assert len(named) > 1, "a hover names the Concept and its neighbours"
        print("hover names:", len(named), "labels shown:", hover_labels, "was", base_labels)
        page.screenshot(path=str(SHOTS / "map-hover.png"))

        # A synthetic mouseenter has no pointer to leave, so the hover is
        # ended explicitly; otherwise the next screenshot still carries the
        # previous Concept's neighbours.
        page.evaluate("() => window.__gym.unhover()")
        page.wait_for_timeout(80)

        # click: pinned, panel open, its Questions and neighbours listed
        assert page.evaluate("() => window.__gym.click('async-runtimes')")
        page.wait_for_selector("#panel.open")
        assert page.evaluate("() => window.__gym.pinned()") == "async-runtimes"
        panel = page.inner_text("#panel-body")
        assert "async runtimes" in panel
        assert "QUESTIONS ON THIS CONCEPT" in panel.upper()
        assert "NEIGHBOURS, BY SHARED QUESTIONS" in panel.upper()
        q_lines = page.eval_on_selector_all("#panel-body .qline", "els => els.length")
        assert q_lines > 0

        # The side panel narrows the canvas. Nothing may be drawn under it:
        # a hub at the right edge used to have its name cut mid-word.
        # Every drawn name -- a Concept's and an island's -- must sit inside
        # the canvas, clear of the side panel and clear of the legend. The
        # hidden node the page measures text against is skipped by its
        # visibility, not by its position.
        overflow = """() => {
          const svg = document.getElementById('graph').getBoundingClientRect();
          const panel = document.getElementById('panel').getBoundingClientRect();
          const hud = document.getElementById('graph-hud').getBoundingClientRect();
          const bad = [];
          document.querySelectorAll('#glabels .glabel, #ghullnames .ghullname').forEach(e => {
            if (e.style.display !== 'block' || e.style.visibility === 'hidden') return;
            const r = e.getBoundingClientRect();
            if (r.right > svg.right + 1) bad.push(['svg-right', e.textContent]);
            else if (r.left < svg.left - 1) bad.push(['svg-left', e.textContent]);
            else if (panel.width && r.right > panel.left) bad.push(['panel', e.textContent]);
            else if (r.right > hud.left && r.left < hud.right &&
                     r.bottom > hud.top && r.top < hud.bottom)
              bad.push(['legend', e.textContent]);
          });
          return bad;
        }"""
        page.keyboard.press("Escape")
        page.evaluate("() => window.__gym.fit()")
        page.wait_for_timeout(200)
        assert page.evaluate(overflow) == []
        wide = page.evaluate("() => document.getElementById('graph').getBoundingClientRect().width")

        edge_concept = page.evaluate("() => window.__gym.rightmost()")
        assert edge_concept
        assert page.evaluate("(n) => window.__gym.click(n)", edge_concept)
        page.wait_for_selector("#panel.open")
        page.wait_for_timeout(400)
        narrow = page.evaluate("() => document.getElementById('graph').getBoundingClientRect().width")
        assert narrow < wide, (narrow, wide)
        assert page.evaluate(overflow) == [], page.evaluate(overflow)
        assert page.inner_text("#panel-body h2")
        print("right-edge pin:", edge_concept, "canvas", wide, "->", narrow)
        page.screenshot(path=str(SHOTS / "map-pinned.png"))

        page.keyboard.press("Escape")
        page.wait_for_timeout(400)
        assert page.evaluate(
            "() => document.getElementById('graph').getBoundingClientRect().width"
        ) == wide
        assert page.evaluate(overflow) == []

        # The reviewer's path is search, not a click, and it clipped where a
        # click did not: the search centres the view, so a Concept can end up
        # just past the canvas with its label overflowing whichever way it
        # faces. Walked here exactly as a reader walks it.
        page.fill("#gsearch", "unsafe")
        page.wait_for_selector("#gsuggest div")
        page.eval_on_selector("#gsuggest div", "el => el.click()")
        page.wait_for_selector("#panel.open")
        page.wait_for_timeout(500)
        assert page.evaluate("() => window.__gym.pinned()") == "unsafe"
        assert page.evaluate(overflow) == [], page.evaluate(overflow)
        page.eval_on_selector("#panel-body .qline", "el => el.click()")
        page.wait_for_selector("#panel-body .pos")
        page.wait_for_timeout(300)
        assert page.evaluate(overflow) == [], page.evaluate(overflow)
        named_here = page.eval_on_selector_all(
            "#ghullnames .ghullname",
            "els => els.filter(e => e.style.display === 'block').length",
        )
        assert named_here >= 1, "an island name is drawn on this path too"
        print("search path clean, island names drawn:", named_here)
        page.screenshot(path=str(SHOTS / "map-search-path.png"))
        page.keyboard.press("Escape")
        page.evaluate("() => window.__gym.fit()")
        page.wait_for_timeout(300)

        assert page.evaluate("() => window.__gym.click('async-runtimes')")
        page.wait_for_selector("#panel.open")
        page.wait_for_timeout(200)

        # a Question line opens the whole entry: Positions, Arguments, Claims.
        # Every line is opened, because Arguments and Claims exist only where
        # the data holds them and one Question is not the contract.
        page.eval_on_selector_all("#panel-body .qline", "els => els.forEach(e => e.click())")
        page.wait_for_selector("#panel-body .pos")
        opened = page.inner_text("#panel-body")
        assert page.eval_on_selector_all(
            "#panel-body .arg-for, #panel-body .arg-against", "els => els.length"
        ) > 0, "an opened Question shows its Arguments"
        # The Question's text is the entry's one title, never printed twice.
        titles = page.eval_on_selector_all("#panel-body .qtitle", "els => els.map(e => e.textContent)")
        lines = page.eval_on_selector_all(
            "#panel-body .qline",
            "els => els.filter(e => e.style.display !== 'none').map(e => e.textContent)",
        )
        for t in titles:
            assert t not in lines, t
        assert re.search(r"Voice \d+", opened), "Claims name Voices anonymously"
        assert re.search(r"\d{4}-\d{2}-\d{2}", opened), "Claims carry their date"
        assert page.eval_on_selector_all("#panel-body .pos", "els => els.length") >= q_lines

        # local mode at depth 2 redraws the neighbourhood only
        page.click("#panel button:has-text('Local 2')")
        page.wait_for_timeout(400)
        assert page.evaluate("() => window.__gym.localDepth()") == 2
        local_nodes = page.evaluate("() => window.__gym.activeNodes()")
        assert 1 < local_nodes < node_count
        print("local depth 2 nodes:", local_nodes, "of", node_count)
        page.screenshot(path=str(SHOTS / "map-local2.png"))

        # Escape steps back out of the local view
        page.keyboard.press("Escape")
        page.wait_for_timeout(500)
        assert page.evaluate("() => window.__gym.localDepth()") == 0
        assert page.evaluate("() => window.__gym.activeNodes()") == node_count

        # search finds a Concept by name and pins it
        page.fill("#gsearch", "borrow check")
        page.wait_for_selector("#gsuggest div")
        page.eval_on_selector("#gsuggest div", "el => el.click()")
        page.wait_for_timeout(200)
        assert page.evaluate("() => window.__gym.pinned()") is not None
        assert "borrow check" in page.inner_text("#panel-body h2").lower()

        # Zooming in earns labels. The measure is the share of the Concepts
        # on screen that carry one, not the raw count: zooming in also pushes
        # most of the map out of the frame, so a raw count can fall while
        # every Concept you can still see has gained a name.
        page.keyboard.press("Escape")
        page.evaluate("() => window.__gym.fit()")
        page.wait_for_timeout(200)
        before = page.evaluate("() => window.__gym.labelStats()")
        page.evaluate("() => window.__gym.zoom(3)")
        page.wait_for_timeout(150)
        after = page.evaluate("() => window.__gym.labelStats()")
        r_before = before["shown"] / before["onScreen"]
        r_after = after["shown"] / after["onScreen"]
        print(
            "labels named/on-screen: fit %d/%d = %.3f, zoomed 3x %d/%d = %.3f"
            % (before["shown"], before["onScreen"], r_before,
               after["shown"], after["onScreen"], r_after)
        )
        assert r_after > r_before

        # a click on a line opens the Questions that line stands for
        page.keyboard.press("Escape")
        page.wait_for_timeout(150)
        e = page.evaluate("() => window.__gym.longestEdge()")
        page.evaluate("(k) => window.__gym.centreOnEdge(k, 2)", e)
        page.wait_for_timeout(150)
        # A Concept's label can sit over the middle of a line and take the
        # click -- the price of a label being its Concept -- so the first
        # point along the line that is not under one is used.
        spot = None
        for t in (0.5, 0.4, 0.6, 0.3, 0.7, 0.25, 0.75):
            cand = page.evaluate("([k, t]) => window.__gym.edgeScreen(k, t)", [e, t])
            if not (0 < cand["x"] < 1600 and 0 < cand["y"] < 1000):
                continue
            on_top = page.evaluate(
                "(s) => { const el = document.elementFromPoint(s.x, s.y);"
                " return el ? el.tagName + '.' + (el.getAttribute('class') || '') : ''; }",
                cand,
            )
            if "glabel" not in on_top and "gnode" not in on_top and "circle" not in on_top:
                spot = cand
                break
        assert spot is not None, "no point on this line is free of a label"
        page.mouse.click(spot["x"], spot["y"])
        page.wait_for_selector("#panel.open")
        # Which line the pointer lands on is the picker's business; what has
        # to hold is that the panel shows that line's own Questions.
        picked = page.evaluate("() => window.__gym.lastEdge()")
        assert picked is not None
        edge_panel = page.inner_text("#panel-body")
        assert picked["a"] in edge_panel and picked["b"] in edge_panel
        edge_lines = page.eval_on_selector_all("#panel-body .qline", "els => els.length")
        assert edge_lines == picked["w"], (edge_lines, picked["w"])
        print("edge click:", picked["a"], "--", picked["b"], "->", edge_lines, "Questions")

        # the Domains toggle recolours; it never adds a Domain node
        before_colour = page.evaluate("() => window.__gym.nodeColour('unsafe')")
        page.click("#btn-colour")
        page.wait_for_timeout(120)
        after_colour = page.evaluate("() => window.__gym.nodeColour('unsafe')")
        assert after_colour != before_colour
        assert page.evaluate("() => window.__gym.nodes") == node_count

        # island hulls: one soft shape per community, each carrying its name.
        # Colour goes back to community first -- the Domain toggle above left
        # it on, and the hulls are the community's own colour.
        if "domain" in page.inner_text("#btn-colour").lower():
            page.click("#btn-colour")
            page.wait_for_timeout(120)
        assert "community" in page.inner_text("#btn-colour").lower()
        page.keyboard.press("Escape")
        page.evaluate("() => window.__gym.fit()")
        page.wait_for_timeout(250)
        hulls = page.eval_on_selector_all("#ghulls .ghull", "els => els.length")
        names = page.eval_on_selector_all(
            "#ghullnames .ghullname",
            "els => els.filter(e => e.style.display === 'block').map(e => e.textContent)",
        )
        assert hulls >= 10, hulls
        assert len(names) >= 8, names
        assert any("unsafe" in n for n in names), names
        print("hulls:", hulls, "named on screen:", len(names))
        page.evaluate("() => window.__gym.click('unsafe')")
        page.wait_for_timeout(200)
        page.evaluate("() => window.__gym.zoom(2.2)")
        page.wait_for_timeout(250)
        assert page.evaluate(overflow) == [], page.evaluate(overflow)
        page.screenshot(path=str(SHOTS / "map-island-hull.png"))

        # the legend folds to a strip and the fit takes the width back
        wide_hud = page.evaluate("() => document.getElementById('graph-hud').offsetWidth")
        page.eval_on_selector("#glegend .hd", "el => el.click()")
        page.wait_for_timeout(300)
        folded_hud = page.evaluate("() => document.getElementById('graph-hud').offsetWidth")
        assert folded_hud < wide_hud, (folded_hud, wide_hud)
        assert page.eval_on_selector_all("#glegend .row", "els => els.length") == 0
        # nothing is drawn under the legend, folded or not
        def under_legend() -> list:
            return page.evaluate("""() => {
              const hud = document.getElementById('graph-hud').getBoundingClientRect();
              const bad = [];
              document.querySelectorAll('#glabels .glabel, #ghullnames .ghullname').forEach(e => {
                if (e.style.display !== 'block') return;
                const r = e.getBoundingClientRect();
                if (r.right > hud.left && r.left < hud.right &&
                    r.bottom > hud.top && r.top < hud.bottom) bad.push(e.textContent);
              });
              return bad;
            }""")
        assert under_legend() == [], under_legend()
        page.eval_on_selector("#glegend .hd", "el => el.click()")
        page.wait_for_timeout(300)
        assert page.eval_on_selector_all("#glegend .row", "els => els.length") > 0
        assert under_legend() == [], under_legend()

        # keyboard: "/" reaches the search box, arrows walk the neighbours,
        # Enter opens the one under the cursor, Escape lets the box go
        page.keyboard.press("Escape")
        page.evaluate("() => window.__gym.fit()")
        page.keyboard.press("/")
        assert page.evaluate("() => document.activeElement.id") == "gsearch"
        page.keyboard.press("Escape")
        assert page.evaluate("() => document.activeElement.id") != "gsearch"
        page.evaluate("() => window.__gym.click('unsafe')")
        page.wait_for_selector("#panel.open")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("ArrowDown")
        cursor = page.eval_on_selector_all(
            "#panel-body .gchip.kbd", "els => els.map(e => e.textContent)"
        )
        assert len(cursor) == 1, cursor
        page.keyboard.press("Enter")
        page.wait_for_timeout(300)
        assert page.evaluate("() => window.__gym.pinned()") != "unsafe"
        print("keyboard walk:", cursor[0], "->", page.inner_text("#panel-body h2"))

        assert errors == [], errors
        browser.close()


def test_page_is_self_contained(tmp_path: Path) -> None:
    """No server, no CDN, no stored state: one file that opens from file://.

    The data block is cut out first and the rules are applied to the markup
    and the script alone. A Question's text or a Voice's quote may contain
    any word at all -- "fetch(" appears in this map's own prose -- and that
    says nothing about what the page does.

    Nothing here ever puts the page's text inside an assert: pytest builds
    its failure explanation from the operands, and doing that over a 2.5 MB
    string takes longer than the rest of this suite put together.
    """
    out = tmp_path / "index.html"
    build_site(MAP, out)
    html = out.read_text(encoding="utf-8")

    block = re.search(
        r'<script id="data" type="application/json">(.*?)</script>', html, re.S
    )
    assert block is not None
    payload = json.loads(block.group(1))
    assert payload["graph"]["stats"]["nodes"] > 0
    assert payload["walk"]["questions"]

    code = html[: block.start()] + html[block.end() :]
    assert len(code) < len(html)

    remote = re.findall(r'(?:src|href)\s*=\s*"(https?:)?//[^"]*"', code)
    assert remote == [], remote[:5]
    for forbidden in (
        "localStorage",
        "sessionStorage",
        "indexedDB",
        "XMLHttpRequest",
        "fetch(",
        "import(",
        "cdn.",
    ):
        assert forbidden not in code, forbidden

    # One file: nothing beside it is loaded, and the page carries its own JS.
    assert "<script" in code and "</script>" in code
    assert out.stat().st_size > 1_000_000
