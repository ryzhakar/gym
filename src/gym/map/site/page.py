"""Assembly: one self-contained HTML file, header, view switch, shared JS.

No server, no CDN, no stored state; the page opens from file://. Nothing is
vendored, because the layout, the communities and the rendering are all
written here -- there is no third-party library on the page at all.

Two surfaces on purpose. The canvas is dark, because a Concept graph is
read by the light its nodes and lines carry. The side panel is a light
reading card, because what opens there is prose -- Questions, Positions,
Arguments, quotes -- and prose is read on paper, not on a screen of ink.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from gym.map.site import graph as graph_view
from gym.map.site import load as load_mod
from gym.map.site import matrix as matrix_view

BASE_CSS = r"""
  :root {
    --bg: #12161d;
    --canvas: #0e1116;
    /* The panel is the same surface as the canvas now. Two surfaces, one
       dark and one light, read as two applications side by side. */
    --panel-bg: #141922;
    --ink: #dde3ec;
    --ink-dim: #8b96a6;
    --border: #2a3340;
    --panel-raise: #1b2230;
    --chrome: #161b23;
    --chrome-ink: #dfe5ee;
    --chrome-dim: #8b96a6;
    --chrome-line: #262f3b;
    --grey-none: #dedad3;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; background: var(--bg); color: var(--ink);
    font: 14px/1.4 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
  body { height: 100vh; display: flex; flex-direction: column; overflow: hidden; }
  header, #note { flex: 0 0 auto; }
  header { padding: 9px 16px; border-bottom: 1px solid var(--chrome-line);
    background: var(--chrome); color: var(--chrome-ink);
    display: flex; flex-wrap: wrap; align-items: center; gap: 12px; }
  header h1 { font-size: 15px; margin: 0; font-weight: 600; letter-spacing: .01em; }
  header .stat { font-size: 12px; color: var(--chrome-dim); }
  button { font: inherit; padding: 4px 10px; border: 1px solid var(--chrome-line);
    background: #1e2531; color: var(--chrome-ink); border-radius: 4px; cursor: pointer; }
  button:hover { background: #28313f; }
  button.active { background: var(--chrome-ink); color: #11151c; border-color: var(--chrome-ink); }
  #panel button { border-color: var(--border); background: var(--panel-raise);
    color: var(--ink); }
  #panel button:hover { background: #26303e; }
  #panel button.active { background: var(--ink); color: #11151c; border-color: var(--ink); }
  /* What the view means is read once and then in the way. It folds behind
     the "i" button and the canvas takes the height back. */
  #note { display: none; padding: 8px 16px 12px; font-size: 12px; line-height: 1.5;
    color: var(--chrome-dim); border-bottom: 1px solid var(--chrome-line);
    background: #11161e; max-width: 96ch; }
  #note.open { display: block; }
  #btn-info { width: 24px; padding: 4px 0; font-style: italic; font-weight: 600; }
  #legend { display: flex; align-items: center; gap: 6px; font-size: 12px; color: var(--chrome-dim); }
  #legend .sw { width: 11px; height: 11px; display: inline-block; border-radius: 2px;
    border: 1px solid rgba(255,255,255,.18); }
  #wrap { display: flex; flex: 1 1 auto; min-height: 0; }
  #panel { width: 380px; flex: 0 0 380px; border-left: 1px solid var(--chrome-line);
    background: var(--panel-bg); color: var(--ink); overflow-y: auto; padding: 16px;
    display: none; }
  #panel.open { display: block; }
  #panel h2 { font-size: 14px; margin: 0 0 6px; }
  #panel .close { float: right; cursor: pointer; color: var(--ink-dim); border: none;
    background: none; font-size: 16px; padding: 0 4px; }
  #panel .q-context { font-size: 12px; color: var(--ink-dim); margin-bottom: 10px; }
  #panel .badge { display: inline-block; font-size: 10.5px; padding: 1px 7px; border-radius: 10px;
    border: 1px solid var(--border); margin-right: 4px; color: var(--ink);
    background: var(--panel-raise); }
  #panel .badge.checked { background: #14301f; border-color: #2c5c3d; color: #a9dcbc; }
  #panel .badge.provisional { background: #2f2617; border-color: #5a4a2b; color: #dcc59a; }
  #panel .badge.undated { background: #232a34; border-color: #3a4552; color: #aab4c1; }
  #panel .badge.voice-chip { cursor: pointer; }
  #panel .badge.voice-chip:hover { background: #26303e; }
  #panel .badge.tag-fact { background: #16293a; color: #a8c8e4; }
  #panel .badge.tag-tradeoff { background: #271d38; color: #c4b0e4; }
  #panel .badge.tag-taste { background: #2f2717; color: #dfc98f; }
  #panel blockquote { margin: 8px 0; padding: 6px 10px; border-left: 3px solid var(--border);
    font-style: italic; color: var(--ink-dim); }
  #panel .field { margin: 9px 0; }
  #panel .field .k { font-size: 10.5px; text-transform: uppercase; letter-spacing: .04em;
    color: var(--ink-dim); }
  #panel a { color: #7fb2ff; }
  #panel a:hover { color: #a8ccff; }
  #panel .pos-block { border: 1px solid var(--border); border-radius: 6px; padding: 8px 10px;
    margin: 10px 0; background: var(--panel-raise); }
  #panel .arg { margin: 6px 0 6px 4px; padding-left: 8px; border-left: 2px solid var(--border);
    font-size: 12.5px; }
  #panel .arg .side-for { color: #6fcf8f; font-weight: 600; }
  #panel .arg .side-against { color: #ee8d7f; font-weight: 600; }
  #panel .hist-item { font-size: 12px; margin: 3px 0; color: var(--ink-dim); }
  #panel .nbr-chip { margin: 2px 3px 2px 0; display: inline-block; }
"""


SHARED_JS = r"""
  var DATA = JSON.parse(document.getElementById("data").textContent);

  function truncate(s, n) {
    if (!s) return "";
    return s.length > n ? s.slice(0, n - 1) + "…" : s;
  }

  function svgEl(tag, attrs) {
    var el = document.createElementNS("http://www.w3.org/2000/svg", tag);
    for (var k in attrs) if (attrs.hasOwnProperty(k)) el.setAttribute(k, attrs[k]);
    return el;
  }

  function badge(text, cls) {
    var s = document.createElement("span");
    s.className = "badge " + cls;
    s.textContent = text;
    return s;
  }

  function field(labelText, valueNode) {
    var d = document.createElement("div");
    d.className = "field";
    var k = document.createElement("div");
    k.className = "k";
    k.textContent = labelText;
    d.appendChild(k);
    if (typeof valueNode === "string") {
      var v = document.createElement("div");
      v.textContent = valueNode;
      d.appendChild(v);
    } else if (valueNode) {
      d.appendChild(valueNode);
    }
    return d;
  }

  function openPanel() { document.getElementById("panel").classList.add("open"); }
  function closePanel() { document.getElementById("panel").classList.remove("open"); }
"""


BOOT_JS = r"""
  var currentView = "graph";

  function updateNote() {
    document.getElementById("note").textContent =
      currentView === "graph" ? graphNote() : matrixNote();
  }

  function setView(view) {
    currentView = view;
    document.getElementById("btn-view-graph").classList.toggle("active", view === "graph");
    document.getElementById("btn-view-matrix").classList.toggle("active", view === "matrix");
    document.getElementById("graph-controls").style.display = view === "graph" ? "" : "none";
    document.getElementById("matrix-controls").style.display = view === "matrix" ? "" : "none";
    document.getElementById("graphwrap").style.display = view === "graph" ? "" : "none";
    document.getElementById("gridwrap").style.display = view === "matrix" ? "" : "none";
    document.getElementById("legend").style.display = view === "matrix" ? "" : "none";
    closePanel();
    if (view === "graph") {
      initGraph();
    } else {
      render();
      buildMatrixLegend();
    }
    updateNote();
  }

  document.getElementById("btn-view-graph").addEventListener("click", function () { setView("graph"); });
  document.getElementById("btn-view-matrix").addEventListener("click", function () { setView("matrix"); });

  document.getElementById("btn-info").addEventListener("click", function () {
    var open = document.getElementById("note").classList.toggle("open");
    this.classList.toggle("active", open);
    this.setAttribute("aria-expanded", open ? "true" : "false");
  });

  resetOrders();
  document.getElementById("btn-scope").textContent = "Show all";
  setView("graph");
"""


def _page_html(data_json: str) -> str:
    return (
        """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Rust opinion map</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>"""
        + BASE_CSS
        + matrix_view.MATRIX_CSS
        + graph_view.GRAPH_CSS
        + """</style>
</head>
<body>
<header>
  <h1>Rust opinion map</h1>
  <span id="view-switch">
    <button id="btn-view-graph" class="active">Concept graph</button>
    <button id="btn-view-matrix">Matrix</button>
  </span>
  <span id="graph-controls">
    <button id="btn-colour">Colour: community</button>
    <button id="btn-fit">Fit</button>
  </span>
  <span id="matrix-controls" style="display:none">
    <button id="btn-scope">Default subset</button>
    <button id="btn-reorder">Reorder (seriate)</button>
  </span>
  <button id="btn-info" aria-expanded="false" title="What this view shows">i</button>
  <span class="stat" id="stat"></span>
  <span id="legend" style="display:none"></span>
</header>
<div id="note"></div>
<div id="wrap">
  <div id="graphwrap">
    <svg id="graph" xmlns="http://www.w3.org/2000/svg"></svg>
    <div id="graph-hud">
      <input id="gsearch" type="text" placeholder="Find a Concept…" autocomplete="off">
      <div id="gsuggest"></div>
      <div id="glegend"></div>
    </div>
    <div id="gcrumbs"></div>
    <div id="ghint">wheel = zoom · drag = pan · hover = neighbours · click = open</div>
  </div>
  <div id="gridwrap" style="display:none"><svg id="matrix" xmlns="http://www.w3.org/2000/svg"></svg></div>
  <div id="panel"><button class="close" id="panel-close">&times;</button><div id="panel-body"></div></div>
</div>
<script id="data" type="application/json">"""
        + data_json
        + """</script>
<script>
(function () {
  "use strict";
"""
        + SHARED_JS
        + matrix_view.MATRIX_JS
        + graph_view.GRAPH_JS
        + BOOT_JS
        + """})();
</script>
</body>
</html>
"""
    )


def build_data(map_dir: Path) -> dict:
    """Everything the page holds, derived from one map directory."""
    questions = load_mod.load_kind(map_dir, "questions")
    positions = load_mod.load_kind(map_dir, "positions")
    claims = load_mod.load_kind(map_dir, "claims")
    voices = load_mod.load_kind(map_dir, "voices")
    sources = load_mod.load_kind(map_dir, "sources")
    arguments = load_mod.load_kind(map_dir, "arguments")
    values = load_mod.load_kind(map_dir, "values")
    concepts = load_mod.load_kind(map_dir, "concepts")
    domains = load_mod.load_kind(map_dir, "domains")

    canon = load_mod.canonical_map(concepts)
    canonical_ids = sorted({canon[c] for c in concepts})
    q_concepts = load_mod.question_concept_sets(questions, concepts, canon)
    edges = load_mod.derive_edges(q_concepts)
    degree = load_mod.weighted_degree(edges)
    dominant = load_mod.dominant_domain(questions, domains, q_concepts)
    labels = {cid: load_mod.concept_label(concepts, cid) for cid in canonical_ids}

    graph = graph_view.build_graph_data(
        edges=edges,
        degree=degree,
        labels=labels,
        dominant=dominant,
        domains=domains,
        question_ids=sorted(questions),
    )
    graph["stats"]["concepts_on_file"] = len(concepts)
    graph["stats"]["concepts_canonical"] = len(canonical_ids)
    graph["stats"]["concepts_merged"] = len(concepts) - len(canonical_ids)
    graph["stats"]["concepts_isolated"] = len(canonical_ids) - len(degree)

    mat = matrix_view.build_matrix(
        questions, positions, claims, voices, sources, arguments, values
    )
    walk = load_mod.walk_payload(
        questions, positions, arguments, claims, voices, sources, values, domains
    )

    return {
        "meta": {
            "subject": map_dir.name,
            "generated": date.today().isoformat(),
            "counts": {
                "questions": len(questions),
                "positions": len(positions),
                "claims": len(claims),
                "voices": len(voices),
                "sources": len(sources),
                "arguments": len(arguments),
                "concepts": len(concepts),
                "domains": len(domains),
            },
            "cells_total": mat["stats"]["cells_total"],
            "default": mat["stats"]["default"],
            "problems": mat["problems"],
            "undated_picks": mat["stats"]["undated_picks"],
            "mixed_dated_undated": mat["stats"]["mixed_dated_undated"],
            "overflow_questions": mat["stats"]["overflow_questions"],
            "graph_rule": (
                "nodes are canonical Concepts of weighted degree >= 1, all of "
                "them; an edge between two Concepts holds every Question whose "
                "canonical Concept set contains both, and its weight is the "
                "length of that list; communities by Louvain on the weighted "
                "graph, smallest folded into their strongest neighbour until at "
                "most " + str(graph_view.COMMUNITY_CAP) + " remain"
            ),
            "canonical_rule": (
                "concept.merged_into is followed to a fixed point; a Concept "
                "with no merged_into is canonical; a cycle resolves to its "
                "smallest member; a merged_into naming an id the map does not "
                "hold stops the walk"
            ),
        },
        "palette": mat["palette"],
        "questions": mat["questions"],
        "voices": mat["voices"],
        "positions": mat["positions"],
        "claims": mat["claims"],
        "matrix": mat["matrix"],
        "default_subset": mat["default_subset"],
        "clustering": mat["clustering"],
        "graph": graph,
        "walk": walk,
        "voice_number": load_mod.voice_numbering(voices),
    }


def main(map_dir: Path, out: Path) -> None:
    data = build_data(map_dir)
    json_text = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(_page_html(json_text), encoding="utf-8")

    g = data["graph"]["stats"]
    print("counts:", data["meta"]["counts"])
    print("problems:", data["meta"]["problems"])
    print(
        "concepts: %d on file, %d canonical (%d merged away), %d canonical with no edge"
        % (
            g["concepts_on_file"],
            g["concepts_canonical"],
            g["concepts_merged"],
            g["concepts_isolated"],
        )
    )
    print(
        "graph: %d nodes, %d edges, total weight %d, heaviest edge %d"
        % (g["nodes"], g["edges"], g["weight_total"], g["max_weight"])
    )
    print(
        "communities: %d (Louvain gave %d; %d of those were islands, folded "
        "into one, then the smallest connected ones merged into their "
        "strongest neighbour until %d remained). Modularity: %.4f for "
        "Louvain's own partition, %.4f for the partition the page ships."
        % (
            g["communities"],
            g["communities_before_cap"],
            g["island_clusters"],
            g["communities"],
            g["modularity_louvain"],
            g["modularity"],
        )
    )
    print(
        "matrix default subset: questions=%d voices=%d cells=%d"
        % (
            data["meta"]["default"]["questions"],
            data["meta"]["default"]["voices"],
            data["meta"]["default"]["cells"],
        )
    )
    print("wrote", out, "(%.1f MB)" % (out.stat().st_size / 1e6))
