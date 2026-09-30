"""The Concept graph: the front door, and the map itself.

Owner ruling 2026-09-30 (docs/opinion-map.md, Form): Concepts are the
nodes; an edge between two Concepts holds every Question that touches both,
and the more Questions the stronger it draws. Read at a glance, walked
through Concepts, no prose on the canvas.

This module turns the derived edges into the page's payload -- communities,
colours, dominant Domains, the always-labelled set -- and carries the
canvas's CSS and JS. The layout itself runs in the page, at load, from a
fixed seed: a deterministic Barnes-Hut force simulation, so dragging a node
and the local view use the same engine the first draw used.
"""

from __future__ import annotations

from collections import defaultdict

from gym.map.site.community import (
    cap_communities,
    fold_islands,
    louvain,
    modularity,
)

# Communities are colour, and colour has to survive a dark canvas, small
# circles and a colour-blind reader. Eighteen hues, evenly spread and
# lifted in lightness; the first eight are the Okabe-Ito set, which is
# built for exactly that, and the rest continue around the wheel.
COMMUNITY_COLORS = [
    "#E69F00", "#56B4E9", "#2FBF71", "#F0E442",
    "#B07AFF", "#FF7A5C", "#E4739B", "#37C8C3",
    "#A8D84F", "#6E7DFF", "#C9884B", "#FF5FD2",
    "#8FE3B6", "#D9B441", "#9BE0FF", "#FFB27A",
    "#7DD6A0", "#CBA6FF",
]

DOMAIN_COLORS = [
    "#56B4E9", "#E69F00", "#009E73", "#CC79A7", "#F0E442", "#0072B2",
    "#D55E00", "#9A86FF", "#59C6C0", "#B4D88B", "#E4739B", "#A0A7B0",
]

ISLAND_COLOR = "#5b6472"

COMMUNITY_CAP = 14
ALWAYS_LABELLED = 45


def _component_count(subset: set[str], edges: dict[tuple[str, str], list[str]]) -> int:
    """Connected components inside `subset`, counting the edges between its members."""
    if not subset:
        return 0
    adj: dict[str, set[str]] = defaultdict(set)
    for (a, b) in edges:
        if a in subset and b in subset:
            adj[a].add(b)
            adj[b].add(a)
    seen: set[str] = set()
    n = 0
    for start in sorted(subset):
        if start in seen:
            continue
        n += 1
        stack = [start]
        seen.add(start)
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
    return n


def build_graph_data(
    edges: dict[tuple[str, str], list[str]],
    degree: dict[str, int],
    labels: dict[str, str],
    dominant: dict[str, str],
    domains: dict[str, dict],
    question_ids: list[str],
) -> dict:
    """Payload for the Concept graph.

    `edges` maps a canonical Concept pair to the Questions touching both;
    the edge's weight is the length of that list and nothing else. Nodes are
    the canonical Concepts of degree 1 or more -- every one of them, no
    hidden subset.
    """
    nodes = sorted(degree)
    node_index = {cid: i for i, cid in enumerate(nodes)}
    question_index = {q: i for i, q in enumerate(question_ids)}
    weights = {pair: float(len(qids)) for pair, qids in edges.items()}

    membership = louvain(nodes, weights)
    raw_community_count = len(set(membership.values()))
    modularity_louvain = round(modularity(membership, weights), 4)
    membership, island_id = fold_islands(membership, weights)
    island_nodes = (
        {n for n, c in membership.items() if c == island_id} if island_id is not None else set()
    )
    island_components = _component_count(island_nodes, edges)
    membership = cap_communities(membership, weights, COMMUNITY_CAP)
    island_comm = membership[min(island_nodes)] if island_nodes else None

    members: dict[int, list[str]] = defaultdict(list)
    for cid, c in membership.items():
        members[c].append(cid)
    community_rows = []
    for c in sorted(members):
        top = sorted(members[c], key=lambda n: (-degree[n], n))[:3]
        name = " · ".join(labels[n] for n in top)
        if c == island_comm:
            name = "islands: %d detached clusters" % island_components
        community_rows.append(
            {
                "name": name,
                "size": len(members[c]),
                # Islands are not a cluster of the subject, they are what has
                # no line to the rest of it, so they take a neutral grey and
                # leave the hues to the communities that mean something.
                "color": ISLAND_COLOR
                if c == island_comm
                else COMMUNITY_COLORS[c % len(COMMUNITY_COLORS)],
                "islands": c == island_comm,
            }
        )

    domain_ids = sorted(domains)
    domain_index = {d: i for i, d in enumerate(domain_ids)}
    domain_rows = [
        {
            "id": d,
            "text": domains[d].get("text") or d,
            "color": DOMAIN_COLORS[i % len(DOMAIN_COLORS)],
        }
        for i, d in enumerate(domain_ids)
    ]

    e_a: list[int] = []
    e_b: list[int] = []
    e_q: list[list[int]] = []
    for (a, b) in sorted(edges):
        e_a.append(node_index[a])
        e_b.append(node_index[b])
        e_q.append([question_index[q] for q in edges[(a, b)]])

    top_labelled = sorted(nodes, key=lambda n: (-degree[n], n))[:ALWAYS_LABELLED]

    return {
        "islands_comm": island_comm,
        "qids": question_ids,
        "ids": nodes,
        "labels": [labels[n] for n in nodes],
        "deg": [degree[n] for n in nodes],
        "comm": [membership[n] for n in nodes],
        "dom": [domain_index.get(dominant.get(n, ""), -1) for n in nodes],
        "e_a": e_a,
        "e_b": e_b,
        "e_q": e_q,
        "communities": community_rows,
        "domains": domain_rows,
        "always_labelled": [node_index[n] for n in top_labelled],
        "stats": {
            "nodes": len(nodes),
            "edges": len(edges),
            "weight_total": sum(len(q) for q in edges.values()),
            "communities": len(community_rows),
            "communities_before_cap": raw_community_count,
            "modularity": round(modularity(membership, weights), 4),
            "modularity_louvain": modularity_louvain,
            "max_weight": max((len(q) for q in edges.values()), default=0),
            "island_concepts": len(island_nodes),
            "island_clusters": island_components,
        },
    }


GRAPH_CSS = r"""
  #graphwrap { flex: 1 1 auto; overflow: hidden; padding: 0; position: relative;
    background: var(--canvas); }
  svg#graph { display: block; width: 100%; height: 100%; cursor: grab;
    background: var(--canvas); }
  svg#graph.panning { cursor: grabbing; }
  #gscene .gedge { stroke: #7f8b9c; fill: none; }
  #gscene .gnode circle { stroke: rgba(10,12,16,.85); stroke-width: 1; }
  #gscene .gnode { cursor: pointer; }
  #glabels { pointer-events: none; }
  #glabels .glabel { font-size: 11px; fill: #ccd4df; pointer-events: none;
    paint-order: stroke; stroke: #0e1116; stroke-width: 3px;
    stroke-linejoin: round; display: none; }
  #glabels .glabel.near { fill: #ffffff; font-size: 12px; font-weight: 600; }
  #gscene.focus .gnode { opacity: .16; }
  #gscene.focus .gedge { stroke-opacity: .04 !important; }
  #gscene.focus .gnode.hl { opacity: 1; }
  /* A neighbour can be a 3px dot on the far side of the map; without a ring
     its label reads as a word floating over nothing. */
  #gscene.focus .gnode.hl circle { stroke: #ffffff; stroke-width: 1.6;
    paint-order: stroke; }
  #gscene.focus .gedge.hl { stroke-opacity: .95 !important; stroke: #f2f5f8; }
  #gscene .gnode.pinned circle { stroke: #ffffff; stroke-width: 2.5; }
  #gscene .gnode.off { display: none; }
  #gscene .gedge.off { display: none; }
  #graph-hud { position: absolute; left: 12px; top: 12px; display: flex;
    flex-direction: column; gap: 8px; width: 244px; pointer-events: none; }
  #graph-hud > * { pointer-events: auto; }
  #gsearch { width: 100%; padding: 6px 9px; border-radius: 5px;
    border: 1px solid #2f3947; background: rgba(16,20,27,.92); color: #e6ebf2;
    font: inherit; }
  #gsearch::placeholder { color: #6f7b8c; }
  #gsuggest { background: rgba(16,20,27,.97); border: 1px solid #2f3947;
    border-radius: 5px; max-height: 210px; overflow-y: auto; display: none; }
  #gsuggest div { padding: 4px 9px; cursor: pointer; font-size: 12px; color: #cfd6e0; }
  #gsuggest div:hover { background: #26303c; color: #fff; }
  #glegend { background: rgba(16,20,27,.92); border: 1px solid #2f3947;
    border-radius: 5px; padding: 7px 9px; max-height: 46vh; overflow-y: auto; }
  #glegend .row { display: flex; align-items: flex-start; gap: 6px; font-size: 11px;
    color: #b9c2ce; cursor: pointer; padding: 2px 0; line-height: 1.25; }
  #glegend .row:hover { color: #fff; }
  #glegend .row.muted { opacity: .35; }
  #glegend .row .sw { width: 9px; height: 9px; border-radius: 50%; flex: 0 0 9px;
    margin-top: 3px; }
  #glegend .hd { font-size: 10px; text-transform: uppercase; letter-spacing: .05em;
    color: #6f7b8c; margin-bottom: 4px; }
  #gcrumbs { position: absolute; left: 12px; bottom: 10px; right: 400px;
    font-size: 11.5px; color: #93a0b0; }
  #gcrumbs b { color: #e6ebf2; font-weight: 600; }
  #gcrumbs .sep { color: #55606f; margin: 0 5px; }
  #ghint { position: absolute; right: 12px; bottom: 10px; font-size: 11px;
    color: #6f7b8c; }
  .gchip { display: inline-block; font-size: 11px; padding: 2px 8px; border-radius: 10px;
    border: 1px solid var(--border); margin: 2px 3px 2px 0; cursor: pointer; }
  .gchip:hover { background: #efece6; }
  .gchip .w { color: var(--ink-dim); margin-left: 5px; }
  .qline { font-size: 12.5px; margin: 5px 0; cursor: pointer; color: #1c1b1a;
    border-left: 2px solid var(--border); padding-left: 8px; }
  .qline:hover { border-left-color: #1c1b1a; }
  .claim { font-size: 12px; margin: 5px 0 5px 4px; padding-left: 8px;
    border-left: 2px solid #e3ded4; }
  .claim .vn { cursor: pointer; text-decoration: underline dotted; }
"""


GRAPH_JS = r"""
  // ---------------- Concept graph ----------------
  // Nodes are canonical Concepts of degree >= 1, all of them. An edge holds
  // the Questions touching both its Concepts; its weight is the length of
  // that list and nothing else, so a thick line means "many Questions cross
  // here", never an inferred affinity.
  //
  // The layout is a Barnes-Hut force simulation run here, at load, from a
  // fixed seed and a fixed tick count: no animation, no randomness after the
  // seed, so the same map always draws the same picture. The same engine
  // runs the local view and the drag, which is why it lives in the page
  // rather than in a precomputed position file.

  var G = DATA.graph;
  var W = DATA.walk;
  var GN = G.ids.length;
  var GE = G.e_a.length;

  var gAdj = [];            // node -> [edge index, ...]
  for (var ai = 0; ai < GN; ai++) gAdj.push([]);
  for (var ei = 0; ei < GE; ei++) { gAdj[G.e_a[ei]].push(ei); gAdj[G.e_b[ei]].push(ei); }

  var gx = new Float64Array(GN), gy = new Float64Array(GN);
  var gr = new Float64Array(GN);
  for (var ri = 0; ri < GN; ri++) gr[ri] = Math.min(2.2 + Math.sqrt(G.deg[ri]) * 1.5, 16);

  var gNodeEl = new Array(GN), gLabelEl = new Array(GN), gEdgeEl = new Array(GE);
  var activeNode = [], activeEdge = [];
  var inActive = new Uint8Array(GN);
  var commOff = {};
  var colorMode = "community";
  var pinned = -1, hovered = -1, crumbs = [], localDepth = 0;
  var vk = 1, vx = 0, vy = 0;
  var layoutMs = 0;

  function nodeColor(i) {
    if (colorMode === "domain") {
      var d = G.dom[i];
      return d < 0 ? "#5a6473" : G.domains[d].color;
    }
    return G.communities[G.comm[i]].color;
  }
  function other(e, i) { return G.e_a[e] === i ? G.e_b[e] : G.e_a[e]; }
  function edgeWeight(e) { return G.e_q[e].length; }

  function mulberry32(seed) {
    return function () {
      seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
      var t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  // --- Barnes-Hut quadtree over the live node set -------------------------
  function qtInsert(q, i, depth) {
    if (q.n === 0) { q.i = i; q.n = 1; q.cx = gx[i]; q.cy = gy[i]; q.m = 1; return; }
    if (q.kids === null) {
      if (depth > 22) { q.n++; q.m++; return; }
      q.kids = [null, null, null, null];
      var held = q.i; q.i = -1;
      qtPush(q, held, depth);
    }
    qtPush(q, i, depth);
    q.n++;
    q.m++;
    q.cx += (gx[i] - q.cx) / q.n;
    q.cy += (gy[i] - q.cy) / q.n;
  }
  function qtPush(q, i, depth) {
    var half = q.s / 2;
    var k = (gx[i] >= q.x0 + half ? 1 : 0) + (gy[i] >= q.y0 + half ? 2 : 0);
    var kid = q.kids[k];
    if (kid === null) {
      kid = {
        x0: q.x0 + (k & 1 ? half : 0), y0: q.y0 + (k & 2 ? half : 0),
        s: half, kids: null, i: -1, n: 0, m: 0, cx: 0, cy: 0
      };
      q.kids[k] = kid;
    }
    qtInsert(kid, i, depth + 1);
  }
  function qtBuild(ids) {
    var minx = Infinity, miny = Infinity, maxx = -Infinity, maxy = -Infinity;
    for (var a = 0; a < ids.length; a++) {
      var i = ids[a];
      if (gx[i] < minx) minx = gx[i];
      if (gy[i] < miny) miny = gy[i];
      if (gx[i] > maxx) maxx = gx[i];
      if (gy[i] > maxy) maxy = gy[i];
    }
    var s = Math.max(maxx - minx, maxy - miny, 1) * 1.02;
    var root = { x0: minx - 1, y0: miny - 1, s: s + 2, kids: null, i: -1, n: 0, m: 0, cx: 0, cy: 0 };
    for (var b = 0; b < ids.length; b++) qtInsert(root, ids[b], 0);
    return root;
  }
  var THETA2 = 0.81;
  function qtForce(q, i, k2, out) {
    var dx = q.cx - gx[i], dy = q.cy - gy[i];
    var d2 = dx * dx + dy * dy;
    if (d2 < 1e-6) { d2 = 1e-6; dx = 0.001; dy = 0.001; }
    if (q.kids === null || q.s * q.s < THETA2 * d2) {
      if (q.kids === null && q.i === i) return;
      var d = Math.sqrt(d2);
      var f = q.m * k2 / d;
      out.x -= dx / d * f;
      out.y -= dy / d * f;
      return;
    }
    for (var c = 0; c < 4; c++) if (q.kids[c] !== null) qtForce(q.kids[c], i, k2, out);
  }

  // --- the simulation -----------------------------------------------------
  function runLayout(ids, edges, ticks, seed) {
    var n = ids.length;
    if (n === 0) return;
    var side = Math.sqrt(n * 2600) + 120;
    var rand = mulberry32(seed);
    for (var s0 = 0; s0 < n; s0++) {
      var ang = rand() * Math.PI * 2, rad = Math.sqrt(rand()) * side / 2;
      gx[ids[s0]] = Math.cos(ang) * rad;
      gy[ids[s0]] = Math.sin(ang) * rad;
    }
    if (n === 1) { gx[ids[0]] = 0; gy[ids[0]] = 0; return; }
    var k = Math.sqrt(side * side / n);
    var k2 = k * k;
    var dx = new Float64Array(n), dy = new Float64Array(n);
    var slot = {};
    for (var m0 = 0; m0 < n; m0++) slot[ids[m0]] = m0;
    var acc = { x: 0, y: 0 };
    for (var t = 0; t < ticks; t++) {
      var temp = (1 - t / ticks) * k * 0.55 + 0.4;
      dx.fill(0); dy.fill(0);
      var root = qtBuild(ids);
      for (var a = 0; a < n; a++) {
        acc.x = 0; acc.y = 0;
        qtForce(root, ids[a], k2, acc);
        dx[a] += acc.x; dy[a] += acc.y;
      }
      for (var e = 0; e < edges.length; e++) {
        var ee = edges[e];
        var ia = G.e_a[ee], ib = G.e_b[ee];
        var sa = slot[ia], sb = slot[ib];
        if (sa === undefined || sb === undefined) continue;
        var ex = gx[ia] - gx[ib], ey = gy[ia] - gy[ib];
        var ed = Math.sqrt(ex * ex + ey * ey) || 0.01;
        var wf = 1 + Math.log(1 + edgeWeight(ee)) * 0.9;
        var f2 = ed * ed / k * wf;
        var fx = ex / ed * f2, fy = ey / ed * f2;
        dx[sa] -= fx; dy[sa] -= fy;
        dx[sb] += fx; dy[sb] += fy;
      }
      for (var c = 0; c < n; c++) {
        var id = ids[c];
        var len = Math.sqrt(dx[c] * dx[c] + dy[c] * dy[c]) || 1e-6;
        var cap = Math.min(len, temp);
        gx[id] += dx[c] / len * cap;
        gy[id] += dy[c] / len * cap;
        gx[id] -= gx[id] * 0.006;
        gy[id] -= gy[id] * 0.006;
      }
    }
    relaxCollisions(ids, 60);
  }

  // Circles that overlap hide each other's colour, so the last pass is pure
  // collision: a uniform grid, neighbours within one cell, pushed apart by
  // however much their radii overlap. It moves nothing that does not touch.
  function relaxCollisions(ids, rounds) {
    var pad = 2.5;
    var cell = 0;
    for (var m = 0; m < ids.length; m++) cell = Math.max(cell, gr[ids[m]]);
    cell = cell * 2 + pad * 2;
    for (var r = 0; r < rounds; r++) {
      var grid = {};
      for (var a = 0; a < ids.length; a++) {
        var i = ids[a];
        var key = Math.floor(gx[i] / cell) + "," + Math.floor(gy[i] / cell);
        (grid[key] || (grid[key] = [])).push(i);
      }
      var moved = false;
      for (var b = 0; b < ids.length; b++) {
        var p = ids[b];
        var cxi = Math.floor(gx[p] / cell), cyi = Math.floor(gy[p] / cell);
        for (var ox = -1; ox <= 1; ox++) for (var oy = -1; oy <= 1; oy++) {
          var bucket = grid[(cxi + ox) + "," + (cyi + oy)];
          if (!bucket) continue;
          for (var z = 0; z < bucket.length; z++) {
            var q = bucket[z];
            if (q <= p) continue;
            var ddx = gx[q] - gx[p], ddy = gy[q] - gy[p];
            var dd = Math.sqrt(ddx * ddx + ddy * ddy);
            var want = gr[p] + gr[q] + pad;
            if (dd >= want) continue;
            if (dd < 1e-6) { ddx = (p % 7) - 3 + 0.5; ddy = (q % 7) - 3 + 0.5; dd = Math.sqrt(ddx * ddx + ddy * ddy) || 1; }
            var push = (want - dd) / 2;
            gx[p] -= ddx / dd * push; gy[p] -= ddy / dd * push;
            gx[q] += ddx / dd * push; gy[q] += ddy / dd * push;
            moved = true;
          }
        }
      }
      if (!moved) break;
    }
  }

  // --- scene --------------------------------------------------------------
  var gsvg = document.getElementById("graph");
  var gscene = null, gEdgeLayer = null, gNodeLayer = null, gLabelLayer = null;

  function buildScene() {
    gsvg.innerHTML = "";
    gNodeEl = new Array(GN); gLabelEl = new Array(GN); gEdgeEl = new Array(GE);
    hlNodes = []; hlEdges = [];
    gscene = svgEl("g", { id: "gscene" });
    gEdgeLayer = svgEl("g", {});
    gNodeLayer = svgEl("g", {});
    gscene.appendChild(gEdgeLayer);
    gscene.appendChild(gNodeLayer);
    gsvg.appendChild(gscene);
    gLabelLayer = svgEl("g", { id: "glabels" });
    gsvg.appendChild(gLabelLayer);

    for (var a = 0; a < activeEdge.length; a++) {
      var e = activeEdge[a];
      var w = edgeWeight(e);
      var line = svgEl("line", {
        class: "gedge",
        "stroke-width": Math.min(0.32 + w * 0.62, 4).toFixed(2),
        "stroke-opacity": Math.min(0.13 + w * 0.13, 0.8).toFixed(3)
      });
      gEdgeEl[e] = line;
      gEdgeLayer.appendChild(line);
    }
    for (var b = 0; b < activeNode.length; b++) {
      var i = activeNode[b];
      var g = svgEl("g", { class: "gnode" });
      var circ = svgEl("circle", { r: gr[i].toFixed(2), fill: nodeColor(i) });
      g.appendChild(circ);
      gNodeEl[i] = g;
      gNodeLayer.appendChild(g);
      var lbl = svgEl("text", { class: "glabel" });
      lbl.textContent = G.labels[i];
      gLabelEl[i] = lbl;
      gLabelLayer.appendChild(lbl);
      bindNode(g, i);
    }
    placeAll();
  }

  function placeAll() {
    for (var a = 0; a < activeEdge.length; a++) {
      var e = activeEdge[a], el = gEdgeEl[e];
      el.setAttribute("x1", gx[G.e_a[e]].toFixed(1));
      el.setAttribute("y1", gy[G.e_a[e]].toFixed(1));
      el.setAttribute("x2", gx[G.e_b[e]].toFixed(1));
      el.setAttribute("y2", gy[G.e_b[e]].toFixed(1));
    }
    for (var b = 0; b < activeNode.length; b++) {
      var i = activeNode[b];
      gNodeEl[i].setAttribute("transform", "translate(" + gx[i].toFixed(1) + "," + gy[i].toFixed(1) + ")");
    }
    updateLabels();
  }

  function applyTransform() {
    gscene.setAttribute("transform", "translate(" + vx + "," + vy + ") scale(" + vk + ")");
    updateLabels();
  }

  // The 123 detached clusters ring the body and would squeeze it into a
  // third of the canvas, so the opening frame is the connected body. Every
  // Concept is still drawn and still reachable -- "Fit all" pulls back to
  // the whole picture, and a scroll out gets there too.
  function fitView(all) {
    var minx = Infinity, miny = Infinity, maxx = -Infinity, maxy = -Infinity;
    for (var a = 0; a < activeNode.length; a++) {
      var i = activeNode[a];
      if (!all && G.islands_comm !== null && G.comm[i] === G.islands_comm && activeNode.length > 400) continue;
      if (gx[i] < minx) minx = gx[i];
      if (gy[i] < miny) miny = gy[i];
      if (gx[i] > maxx) maxx = gx[i];
      if (gy[i] > maxy) maxy = gy[i];
    }
    if (minx === Infinity) { minx = miny = -100; maxx = maxy = 100; }
    var r = gsvg.getBoundingClientRect();
    var pad = 40;
    vk = Math.min((r.width - pad * 2) / Math.max(maxx - minx, 1), (r.height - pad * 2) / Math.max(maxy - miny, 1));
    vk = Math.max(Math.min(vk, 4), 0.05);
    vx = r.width / 2 - (minx + maxx) / 2 * vk;
    vy = r.height / 2 - (miny + maxy) / 2 * vk;
    applyTransform();
  }

  // Labels are drawn in screen space, outside the zoom transform, so text
  // stays the same size at every zoom and never smears. Only the ones on
  // screen are positioned, which is why 1400 nodes cost nothing to pan.
  // Labels are drawn in screen space, outside the zoom transform, so text
  // stays one size at every zoom and never smears. They are placed in
  // priority order -- what the pointer is on, then its neighbours, then the
  // highest-degree Concepts, then whatever the zoom has earned -- and a
  // label that would land on one already placed is dropped, not stacked.
  var LABEL_BUDGET = 220;
  var alwaysSet = {};
  for (var qq = 0; qq < G.always_labelled.length; qq++) alwaysSet[G.always_labelled[qq]] = true;

  var visibleLabelCount = 0, onScreenCount = 0;
  function updateLabels() {
    var r = gsvg.getBoundingClientRect();
    onScreenCount = 0;
    var neigh = null;
    if (hovered >= 0) {
      neigh = {};
      for (var h = 0; h < gAdj[hovered].length; h++) neigh[other(gAdj[hovered][h], hovered)] = true;
    }
    var cands = [];
    for (var a = 0; a < activeNode.length; a++) {
      var i = activeNode[a];
      var el = gLabelEl[i];
      if (!el) continue;
      el.style.display = "none";
      el.classList.remove("near");
      if (commOff[G.comm[i]]) continue;
      // Same frame the label candidates are judged against, so "named" and
      // "on screen" are counted over one and the same set.
      var px = gx[i] * vk + vx, py = gy[i] * vk + vy;
      if (px >= -60 && py >= -20 && px <= r.width + 60 && py <= r.height + 20) onScreenCount++;
      var pri;
      if (i === pinned || i === hovered) pri = 0;
      else if (neigh && neigh[i]) pri = 1;
      else if (alwaysSet[i]) pri = 2;
      else if (G.deg[i] * vk >= 26) pri = 3;
      else continue;
      var sx = gx[i] * vk + vx, sy = gy[i] * vk + vy;
      if (sx < -60 || sy < -20 || sx > r.width + 60 || sy > r.height + 20) continue;
      cands.push({ i: i, pri: pri, x: sx + gr[i] * vk + 3, y: sy + 3, el: el });
    }
    cands.sort(function (p, q) { return p.pri - q.pri || G.deg[q.i] - G.deg[p.i] || p.i - q.i; });
    var placed = [], shown = 0;
    for (var c = 0; c < cands.length && shown < LABEL_BUDGET; c++) {
      var k = cands[c];
      var fs = k.pri <= 1 ? 12 : 11;
      var box = { x: k.x, y: k.y - fs, w: G.labels[k.i].length * fs * 0.55, h: fs + 3 };
      var clash = false;
      for (var q2 = 0; q2 < placed.length; q2++) {
        var o = placed[q2];
        if (box.x < o.x + o.w && box.x + box.w > o.x && box.y < o.y + o.h && box.y + box.h > o.y) {
          clash = true; break;
        }
      }
      if (clash && k.pri > 0) continue;
      placed.push(box);
      k.el.setAttribute("x", k.x.toFixed(1));
      k.el.setAttribute("y", k.y.toFixed(1));
      if (k.pri <= 1) k.el.classList.add("near");
      k.el.style.display = "block";
      shown++;
    }
    visibleLabelCount = shown;
  }

  // --- highlight ----------------------------------------------------------
  var hlNodes = [], hlEdges = [];
  function clearHighlight() {
    for (var a = 0; a < hlNodes.length; a++) if (gNodeEl[hlNodes[a]]) gNodeEl[hlNodes[a]].classList.remove("hl");
    for (var b = 0; b < hlEdges.length; b++) if (gEdgeEl[hlEdges[b]]) gEdgeEl[hlEdges[b]].classList.remove("hl");
    hlNodes = []; hlEdges = [];
    gscene.classList.remove("focus");
  }
  function highlight(i) {
    clearHighlight();
    if (i < 0) return;
    gscene.classList.add("focus");
    hlNodes.push(i);
    if (gNodeEl[i]) gNodeEl[i].classList.add("hl");
    for (var a = 0; a < gAdj[i].length; a++) {
      var e = gAdj[i][a];
      if (!gEdgeEl[e] || !inActive[other(e, i)]) continue;
      gEdgeEl[e].classList.add("hl");
      hlEdges.push(e);
      var o = other(e, i);
      if (gNodeEl[o]) { gNodeEl[o].classList.add("hl"); hlNodes.push(o); }
    }
  }

  function bindNode(g, i) {
    g.addEventListener("mouseenter", function () {
      hovered = i;
      highlight(i);
      updateLabels();
    });
    g.addEventListener("mouseleave", function () {
      hovered = -1;
      if (pinned >= 0) highlight(pinned); else clearHighlight();
      updateLabels();
    });
    g.addEventListener("pointerdown", function (ev) { startNodeDrag(ev, i); });
  }

  // --- drag ---------------------------------------------------------------
  function startNodeDrag(ev, i) {
    ev.stopPropagation();
    var moved = false;
    var r = gsvg.getBoundingClientRect();
    function toWorld(cx, cy) { return { x: (cx - r.left - vx) / vk, y: (cy - r.top - vy) / vk }; }
    var grab = toWorld(ev.clientX, ev.clientY);
    var off = { x: gx[i] - grab.x, y: gy[i] - grab.y };
    function onMove(m) {
      if (Math.abs(m.clientX - ev.clientX) + Math.abs(m.clientY - ev.clientY) > 3) moved = true;
      if (!moved) return;
      var w = toWorld(m.clientX, m.clientY);
      gx[i] = w.x + off.x; gy[i] = w.y + off.y;
      relaxCollisions(activeNode, 3);
      placeAll();
    }
    function onUp() {
      window.removeEventListener("pointermove", onMove);
      window.removeEventListener("pointerup", onUp);
      if (!moved) pinNode(i, true);
    }
    window.addEventListener("pointermove", onMove);
    window.addEventListener("pointerup", onUp);
  }

  // --- pan / zoom ---------------------------------------------------------
  gsvg.addEventListener("wheel", function (ev) {
    ev.preventDefault();
    var r = gsvg.getBoundingClientRect();
    var mx = ev.clientX - r.left, my = ev.clientY - r.top;
    var f = Math.exp(-ev.deltaY * 0.0018);
    var nk = Math.max(0.05, Math.min(12, vk * f));
    vx = mx - (mx - vx) * (nk / vk);
    vy = my - (my - vy) * (nk / vk);
    vk = nk;
    applyTransform();
  }, { passive: false });

  gsvg.addEventListener("pointerdown", function (ev) {
    var sx = ev.clientX, sy = ev.clientY, ox = vx, oy = vy, moved = false;
    gsvg.classList.add("panning");
    function onMove(m) {
      if (Math.abs(m.clientX - sx) + Math.abs(m.clientY - sy) > 3) moved = true;
      vx = ox + (m.clientX - sx); vy = oy + (m.clientY - sy);
      applyTransform();
    }
    function onUp(u) {
      window.removeEventListener("pointermove", onMove);
      window.removeEventListener("pointerup", onUp);
      gsvg.classList.remove("panning");
      if (!moved) backgroundClick(u);
    }
    window.addEventListener("pointermove", onMove);
    window.addEventListener("pointerup", onUp);
  });

  // An edge is a hairline, so it is not picked by hit-testing but by
  // distance: the click point is put back into world coordinates and the
  // nearest drawn segment within a few pixels wins. Nothing else on the
  // background does anything, so a miss just clears the pin.
  function backgroundClick(ev) {
    var r = gsvg.getBoundingClientRect();
    var wx = (ev.clientX - r.left - vx) / vk, wy = (ev.clientY - r.top - vy) / vk;
    var tol = 5 / vk, best = -1, bestD = tol;
    for (var a = 0; a < activeEdge.length; a++) {
      var e = activeEdge[a];
      var x1 = gx[G.e_a[e]], y1 = gy[G.e_a[e]], x2 = gx[G.e_b[e]], y2 = gy[G.e_b[e]];
      var ddx = x2 - x1, ddy = y2 - y1;
      var L2 = ddx * ddx + ddy * ddy;
      var t = L2 === 0 ? 0 : Math.max(0, Math.min(1, ((wx - x1) * ddx + (wy - y1) * ddy) / L2));
      var px = x1 + t * ddx - wx, py = y1 + t * ddy - wy;
      var d = Math.sqrt(px * px + py * py);
      if (d < bestD) { bestD = d; best = e; }
    }
    if (best >= 0) { showEdgePanel(best); return; }
    pinned = -1;
    crumbs = [];
    renderCrumbs();
    clearHighlight();
    closePanel();
    updateLabels();
  }

  // --- selection / walking ------------------------------------------------
  function pinNode(i, pushCrumb) {
    if (pushCrumb && pinned !== i) {
      if (crumbs[crumbs.length - 1] !== i) crumbs.push(i);
      if (crumbs.length > 12) crumbs.shift();
    }
    pinned = i;
    for (var a = 0; a < activeNode.length; a++) {
      if (gNodeEl[activeNode[a]]) gNodeEl[activeNode[a]].classList.remove("pinned");
    }
    if (gNodeEl[i]) gNodeEl[i].classList.add("pinned");
    highlight(i);
    renderCrumbs();
    showConceptPanel(i);
    updateLabels();
  }

  function centreOn(i, minZoom) {
    var r = gsvg.getBoundingClientRect();
    vk = Math.max(vk, minZoom || 1.4);
    vx = r.width / 2 - gx[i] * vk;
    vy = r.height / 2 - gy[i] * vk;
    applyTransform();
  }

  function renderCrumbs() {
    var el = document.getElementById("gcrumbs");
    el.innerHTML = "";
    if (localDepth > 0 && pinned >= 0) {
      var m = document.createElement("span");
      m.innerHTML = "<b>local " + localDepth + "</b> around ";
      el.appendChild(m);
    }
    for (var a = 0; a < crumbs.length; a++) {
      if (a) { var s = document.createElement("span"); s.className = "sep"; s.textContent = "›"; el.appendChild(s); }
      var b = document.createElement(a === crumbs.length - 1 ? "b" : "span");
      b.textContent = G.labels[crumbs[a]];
      b.style.cursor = "pointer";
      (function (idx) { b.addEventListener("click", function () { crumbs = crumbs.slice(0, idx + 1); pinNode(crumbs[idx], false); centreOn(crumbs[idx]); }); })(a);
      el.appendChild(b);
    }
    if (crumbs.length) {
      var esc = document.createElement("span");
      esc.className = "sep";
      esc.textContent = "  (Esc steps back)";
      el.appendChild(esc);
    }
  }

  // --- active set / local view -------------------------------------------
  function setActive(ids) {
    activeNode = ids.slice();
    inActive = new Uint8Array(GN);
    for (var a = 0; a < activeNode.length; a++) inActive[activeNode[a]] = 1;
    activeEdge = [];
    for (var e = 0; e < GE; e++) if (inActive[G.e_a[e]] && inActive[G.e_b[e]]) activeEdge.push(e);
  }

  function neighbourhood(i, depth) {
    var seen = {}, frontier = [i];
    seen[i] = true;
    for (var d = 0; d < depth; d++) {
      var next = [];
      for (var a = 0; a < frontier.length; a++) {
        var n = frontier[a];
        for (var b = 0; b < gAdj[n].length; b++) {
          var o = other(gAdj[n][b], n);
          if (!seen[o]) { seen[o] = true; next.push(o); }
        }
      }
      frontier = next;
    }
    var out = [];
    for (var k in seen) if (seen.hasOwnProperty(k)) out.push(+k);
    out.sort(function (p, q) { return p - q; });
    return out;
  }

  function setLocal(depth) {
    if (depth > 0 && pinned < 0) return;
    var centre = pinned;
    localDepth = depth;
    if (depth === 0) {
      setActive(allNodeIds);
      runLayout(activeNode, activeEdge, 320, 1337);
    } else {
      setActive(neighbourhood(centre, depth));
      runLayout(activeNode, activeEdge, 420, 4242);
    }
    buildScene();
    fitView(depth > 0);
    if (centre >= 0 && inActive[centre]) {
      pinNode(centre, false);
      // In a local view the neighbourhood *is* the subject, so the dimming
      // that isolates one Concept on the whole map would hide the point of
      // it. The centre keeps its ring; nothing else is dimmed.
      if (depth > 0) { clearHighlight(); updateLabels(); }
    }
    updateStat();
  }

  // --- panels -------------------------------------------------------------
  function conceptQuestions(i) {
    var seen = {}, out = [];
    for (var a = 0; a < gAdj[i].length; a++) {
      var qs = G.e_q[gAdj[i][a]];
      for (var b = 0; b < qs.length; b++) if (!seen[qs[b]]) { seen[qs[b]] = true; out.push(qs[b]); }
    }
    out.sort(function (p, q) { return G.qids[p] < G.qids[q] ? -1 : 1; });
    return out;
  }

  var revealedVoice = {};
  function questionBlock(qIdx) {
    var qid = G.qids[qIdx];
    var q = W.questions[qid];
    var wrap = document.createElement("div");
    wrap.className = "pos-block";
    var head = document.createElement("div");
    head.textContent = q.text;
    head.style.fontWeight = "600";
    wrap.appendChild(head);
    if (q.domains && q.domains.length) {
      var dwrap = document.createElement("div");
      dwrap.style.marginTop = "4px";
      for (var d = 0; d < q.domains.length; d++) dwrap.appendChild(badge(W.domains[q.domains[d]] || q.domains[d], ""));
      wrap.appendChild(dwrap);
    }
    for (var p = 0; p < q.positions.length; p++) {
      var pid = q.positions[p], pos = W.positions[pid];
      var pb = document.createElement("div");
      pb.style.marginTop = "8px";
      pb.appendChild(badge(pos.tag ? pos.tag : "untagged", pos.tag ? "tag-" + pos.tag : ""));
      var sum = document.createElement("div");
      sum.style.marginTop = "4px";
      sum.textContent = pos.summary;
      pb.appendChild(sum);
      for (var ar = 0; ar < pos.arguments.length; ar++) {
        var arg = pos.arguments[ar];
        var ad = document.createElement("div");
        ad.className = "arg";
        var side = document.createElement("span");
        side.className = arg.side === "for" ? "side-for" : "side-against";
        side.textContent = arg.side === "for" ? "For: " : "Against: ";
        ad.appendChild(side);
        ad.appendChild(document.createTextNode(arg.text));
        if (arg.values && arg.values.length) {
          var vv = document.createElement("div");
          vv.style.marginTop = "3px";
          for (var vi = 0; vi < arg.values.length; vi++) vv.appendChild(badge(arg.values[vi], ""));
          ad.appendChild(vv);
        }
        pb.appendChild(ad);
      }
      for (var cl = 0; cl < pos.claims.length; cl++) {
        pb.appendChild(claimBlock(pos.claims[cl], qIdx));
      }
      wrap.appendChild(pb);
    }
    return wrap;
  }

  function claimBlock(c, qIdx) {
    var d = document.createElement("div");
    d.className = "claim";
    var vn = document.createElement("span");
    vn.className = "vn";
    vn.textContent = revealedVoice[c.voice] ? W.voice_names[c.voice] : "Voice " + c.n;
    vn.addEventListener("click", function () {
      revealedVoice[c.voice] = !revealedVoice[c.voice];
      vn.textContent = revealedVoice[c.voice] ? W.voice_names[c.voice] : "Voice " + c.n;
    });
    d.appendChild(vn);
    d.appendChild(document.createTextNode(" · " + (c.date || "undated") + (c.checked ? " · checked" : " · provisional")));
    if (c.paraphrase) {
      var pp = document.createElement("div");
      pp.textContent = c.paraphrase;
      d.appendChild(pp);
    }
    if (c.quote) {
      var bq = document.createElement("blockquote");
      bq.textContent = c.quote;
      d.appendChild(bq);
    }
    if (c.source && c.source.url) {
      var a = document.createElement("a");
      a.href = c.source.url; a.target = "_blank"; a.rel = "noopener";
      a.textContent = c.source.title || c.source.url;
      var sw = document.createElement("div");
      sw.appendChild(a);
      d.appendChild(sw);
    }
    return d;
  }

  function showConceptPanel(i) {
    var body = document.getElementById("panel-body");
    body.innerHTML = "";
    var h = document.createElement("h2");
    h.textContent = G.labels[i];
    body.appendChild(h);

    var meta = document.createElement("div");
    meta.className = "q-context";
    meta.textContent = "Concept · degree " + G.deg[i] + " · " +
      G.communities[G.comm[i]].name +
      (G.dom[i] >= 0 ? " · mostly " + G.domains[G.dom[i]].text : "");
    body.appendChild(meta);

    var tools = document.createElement("div");
    [["Local 1", 1], ["Local 2", 2], ["Whole map", 0]].forEach(function (pair) {
      var b = document.createElement("button");
      b.textContent = pair[0];
      b.className = localDepth === pair[1] ? "active" : "";
      b.style.marginRight = "5px";
      b.addEventListener("click", function () { setLocal(pair[1]); });
      tools.appendChild(b);
    });
    var cb = document.createElement("button");
    cb.textContent = "Centre";
    cb.addEventListener("click", function () { centreOn(i, 1.8); });
    tools.appendChild(cb);
    body.appendChild(tools);

    var qs = conceptQuestions(i);
    var qwrap = document.createElement("div");
    for (var a = 0; a < qs.length; a++) {
      (function (qIdx) {
        var line = document.createElement("div");
        line.className = "qline";
        line.textContent = truncate(W.questions[G.qids[qIdx]].text, 110);
        var open = false, block = null;
        line.addEventListener("click", function () {
          open = !open;
          if (open) { block = questionBlock(qIdx); line.parentNode.insertBefore(block, line.nextSibling); }
          else if (block) { block.parentNode.removeChild(block); block = null; }
        });
        qwrap.appendChild(line);
      })(qs[a]);
    }
    body.appendChild(field("Questions on this Concept (" + qs.length + ")", qwrap));

    var nb = [];
    for (var b2 = 0; b2 < gAdj[i].length; b2++) {
      var e = gAdj[i][b2];
      nb.push({ i: other(e, i), w: edgeWeight(e), e: e });
    }
    nb.sort(function (p, q) { return q.w - p.w || (G.labels[p.i] < G.labels[q.i] ? -1 : 1); });
    var nwrap = document.createElement("div");
    for (var c = 0; c < nb.length; c++) {
      (function (row) {
        var chip = document.createElement("span");
        chip.className = "gchip";
        chip.textContent = G.labels[row.i];
        var w = document.createElement("span");
        w.className = "w";
        w.textContent = row.w;
        chip.appendChild(w);
        chip.addEventListener("click", function () {
          if (!inActive[row.i]) setLocal(0);
          pinNode(row.i, true);
          centreOn(row.i);
        });
        nwrap.appendChild(chip);
      })(nb[c]);
    }
    body.appendChild(field("Neighbours by shared Questions (" + nb.length + ")", nwrap));
    openPanel();
  }

  var lastEdge = -1;
  function showEdgePanel(e) {
    lastEdge = e;
    var a = G.e_a[e], b = G.e_b[e];
    var body = document.getElementById("panel-body");
    body.innerHTML = "";
    var h = document.createElement("h2");
    h.textContent = G.labels[a] + "  —  " + G.labels[b];
    body.appendChild(h);
    var meta = document.createElement("div");
    meta.className = "q-context";
    meta.textContent = "Edge · " + edgeWeight(e) + " Question" + (edgeWeight(e) === 1 ? "" : "s") + " touch both Concepts.";
    body.appendChild(meta);
    var qs = G.e_q[e];
    var wrap = document.createElement("div");
    for (var i = 0; i < qs.length; i++) {
      (function (qIdx) {
        var line = document.createElement("div");
        line.className = "qline";
        line.textContent = truncate(W.questions[G.qids[qIdx]].text, 110);
        var open = false, block = null;
        line.addEventListener("click", function () {
          open = !open;
          if (open) { block = questionBlock(qIdx); line.parentNode.insertBefore(block, line.nextSibling); }
          else if (block) { block.parentNode.removeChild(block); block = null; }
        });
        wrap.appendChild(line);
      })(qs[i]);
    }
    body.appendChild(field("Questions on this edge", wrap));
    gEdgeEl[e].classList.add("hl");
    hlEdges.push(e);
    gscene.classList.add("focus");
    if (gNodeEl[a]) { gNodeEl[a].classList.add("hl"); hlNodes.push(a); }
    if (gNodeEl[b]) { gNodeEl[b].classList.add("hl"); hlNodes.push(b); }
    openPanel();
  }

  // --- legend, search, colour mode ---------------------------------------
  function renderLegend() {
    var el = document.getElementById("glegend");
    el.innerHTML = "";
    var hd = document.createElement("div");
    hd.className = "hd";
    hd.textContent = colorMode === "community"
      ? G.communities.length + " communities · click to hide"
      : G.domains.length + " domains · colour by dominant Domain";
    el.appendChild(hd);
    var rows = colorMode === "community" ? G.communities : G.domains;
    for (var i = 0; i < rows.length; i++) {
      (function (idx, row) {
        var d = document.createElement("div");
        d.className = "row" + (colorMode === "community" && commOff[idx] ? " muted" : "");
        var sw = document.createElement("span");
        sw.className = "sw";
        sw.style.background = row.color;
        d.appendChild(sw);
        var t = document.createElement("span");
        t.textContent = (colorMode === "community" ? row.name + " (" + row.size + ")" : row.text);
        d.appendChild(t);
        if (colorMode === "community") {
          d.addEventListener("click", function () {
            commOff[idx] = !commOff[idx];
            applyCommunityFilter();
            renderLegend();
          });
        }
        el.appendChild(d);
      })(i, rows[i]);
    }
  }

  function applyCommunityFilter() {
    for (var a = 0; a < activeNode.length; a++) {
      var i = activeNode[a];
      if (gNodeEl[i]) gNodeEl[i].classList.toggle("off", !!commOff[G.comm[i]]);
    }
    for (var b = 0; b < activeEdge.length; b++) {
      var e = activeEdge[b];
      var off = !!commOff[G.comm[G.e_a[e]]] || !!commOff[G.comm[G.e_b[e]]];
      if (gEdgeEl[e]) gEdgeEl[e].classList.toggle("off", off);
    }
    updateLabels();
    updateStat();
  }

  function recolour() {
    for (var a = 0; a < activeNode.length; a++) {
      var i = activeNode[a];
      if (gNodeEl[i]) gNodeEl[i].firstChild.setAttribute("fill", nodeColor(i));
    }
  }

  function setupSearch() {
    var input = document.getElementById("gsearch");
    var box = document.getElementById("gsuggest");
    function close() { box.style.display = "none"; box.innerHTML = ""; }
    input.addEventListener("input", function () {
      var q = input.value.trim().toLowerCase();
      box.innerHTML = "";
      if (q.length < 2) { close(); return; }
      var hits = [];
      for (var i = 0; i < GN; i++) {
        var l = G.labels[i].toLowerCase();
        var p = l.indexOf(q);
        if (p >= 0) hits.push({ i: i, p: p });
      }
      hits.sort(function (a, b) { return a.p - b.p || G.deg[b.i] - G.deg[a.i] || (G.labels[a.i] < G.labels[b.i] ? -1 : 1); });
      hits = hits.slice(0, 40);
      if (!hits.length) { close(); return; }
      for (var h = 0; h < hits.length; h++) {
        (function (i) {
          var d = document.createElement("div");
          d.textContent = G.labels[i] + "  (" + G.deg[i] + ")";
          d.addEventListener("click", function () { gotoConcept(i); close(); input.value = ""; });
          box.appendChild(d);
        })(hits[h].i);
      }
      box.style.display = "block";
    });
    input.addEventListener("keydown", function (ev) {
      if (ev.key === "Enter") {
        var first = box.querySelector("div");
        if (first) first.dispatchEvent(new MouseEvent("click", { bubbles: true }));
      } else if (ev.key === "Escape") { close(); }
    });
  }

  function gotoConcept(i) {
    if (!inActive[i]) setLocal(0);
    commOff[G.comm[i]] = false;
    applyCommunityFilter();
    renderLegend();
    pinNode(i, true);
    centreOn(i, 1.8);
  }

  function updateStat() {
    var hiddenNodes = 0;
    for (var a = 0; a < activeNode.length; a++) if (commOff[G.comm[activeNode[a]]]) hiddenNodes++;
    document.getElementById("stat").textContent =
      (activeNode.length - hiddenNodes) + " Concepts, " + activeEdge.length + " edges" +
      (localDepth ? " · local depth " + localDepth : "") +
      " · layout " + layoutMs + " ms";
  }

  function graphNote() {
    return "Concept graph — " + G.stats.nodes + " canonical Concepts, " +
      G.stats.edges + " edges. An edge holds every Question touching both its " +
      "Concepts; thickness and brightness are that count (heaviest here: " +
      G.stats.max_weight + "). Colour is community, found by Louvain on the " +
      "weighted graph; grey are the " + G.stats.island_clusters + " clusters " +
      "with no line to the rest. The Colour button recolours by the Domain " +
      "most of a Concept's Questions are live in. " +
      "Hover isolates a Concept and its neighbours, click pins it and opens " +
      "its Questions, a click on a line opens the Questions that line stands for.";
  }

  var allNodeIds = [];
  for (var z = 0; z < GN; z++) allNodeIds.push(z);

  var graphReady = false;
  function initGraph() {
    if (graphReady) return;
    graphReady = true;
    setActive(allNodeIds);
    var t0 = (window.performance && performance.now) ? performance.now() : Date.now();
    runLayout(activeNode, activeEdge, 320, 1337);
    var t1 = (window.performance && performance.now) ? performance.now() : Date.now();
    layoutMs = Math.round(t1 - t0);
    buildScene();
    fitView();
    renderLegend();
    setupSearch();
    updateStat();
    window.__gym = window.__gym || {};
    window.__gym.layoutMs = layoutMs;
    window.__gym.nodes = GN;
    window.__gym.edges = GE;
    window.__gym.visibleLabels = function () { return visibleLabelCount; };
    window.__gym.labelStats = function () {
      return { shown: visibleLabelCount, onScreen: onScreenCount };
    };
    window.__gym.activeNodes = function () { return activeNode.length; };
    window.__gym.pinned = function () { return pinned < 0 ? null : G.ids[pinned]; };
    window.__gym.localDepth = function () { return localDepth; };
    window.__gym.fit = function () { fitView(false); };
    window.__gym.zoom = function (f) { vk = Math.max(0.05, Math.min(12, vk * f)); applyTransform(); };
    window.__gym.hover = function (name) {
      for (var i = 0; i < GN; i++) if (G.ids[i] === name) { gNodeEl[i].dispatchEvent(new MouseEvent("mouseenter")); return true; }
      return false;
    };
    window.__gym.unhover = function () {
      if (hovered >= 0 && gNodeEl[hovered]) {
        gNodeEl[hovered].dispatchEvent(new MouseEvent("mouseleave"));
      }
    };
    window.__gym.click = function (name) {
      for (var i = 0; i < GN; i++) if (G.ids[i] === name) { pinNode(i, true); return true; }
      return false;
    };
    window.__gym.lastEdge = function () {
      if (lastEdge < 0) return null;
      return {
        w: edgeWeight(lastEdge),
        a: G.labels[G.e_a[lastEdge]],
        b: G.labels[G.e_b[lastEdge]]
      };
    };
    window.__gym.heaviestEdge = function () {
      var best = 0;
      for (var e = 0; e < GE; e++) if (edgeWeight(e) > edgeWeight(best)) best = e;
      return best;
    };
    window.__gym.centreOnEdge = function (e, zoom) {
      var r = gsvg.getBoundingClientRect();
      vk = zoom || 2;
      vx = r.width / 2 - ((gx[G.e_a[e]] + gx[G.e_b[e]]) / 2) * vk;
      vy = r.height / 2 - ((gy[G.e_a[e]] + gy[G.e_b[e]]) / 2) * vk;
      applyTransform();
    };
    window.__gym.edgeScreen = function (e) {
      var r = gsvg.getBoundingClientRect();
      return {
        x: r.left + ((gx[G.e_a[e]] + gx[G.e_b[e]]) / 2) * vk + vx,
        y: r.top + ((gy[G.e_a[e]] + gy[G.e_b[e]]) / 2) * vk + vy,
        w: edgeWeight(e),
        a: G.labels[G.e_a[e]],
        b: G.labels[G.e_b[e]]
      };
    };
    window.__gym.nodeColour = function (name) {
      for (var i = 0; i < GN; i++) {
        if (G.ids[i] === name) return gNodeEl[i].firstChild.getAttribute("fill");
      }
      return null;
    };
  }

  document.getElementById("btn-colour").addEventListener("click", function () {
    colorMode = colorMode === "community" ? "domain" : "community";
    this.textContent = colorMode === "community" ? "Colour: community" : "Colour: domain";
    recolour();
    renderLegend();
  });
  var fitAll = false;
  document.getElementById("btn-fit").addEventListener("click", function () {
    fitAll = !fitAll;
    this.textContent = fitAll ? "Fit body" : "Fit all";
    fitView(fitAll);
  });

  document.addEventListener("keydown", function (ev) {
    if (ev.key !== "Escape" || currentView !== "graph") return;
    if (localDepth > 0) { setLocal(0); if (pinned >= 0) centreOn(pinned); return; }
    if (crumbs.length > 1) {
      crumbs.pop();
      pinNode(crumbs[crumbs.length - 1], false);
      centreOn(crumbs[crumbs.length - 1]);
      return;
    }
    crumbs = [];
    pinned = -1;
    clearHighlight();
    closePanel();
    renderCrumbs();
  });
"""
