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
BACKBONE_PER_NODE = 2
BRIDGES_LABELLED = 18
BRIDGES_PER_PAIR = 3
HUB_PERCENTILE = 0.99


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
            name = "islands: %d detached clusters (Fit all)" % island_components
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

    # --- the backbone: what the opening frame draws ------------------------
    # 4793 of 4837 edges carry one Question. Drawing all of them at once put
    # every Concept inside a hub's spray of spokes and the picture read as one
    # mass (cold review, docs/orchestration_log/recon/2026-09-30/frontend/
    # map-review.md). The opening frame draws a backbone instead: every edge
    # carrying two Questions or more, plus each Concept's two strongest, which
    # guarantees no Concept is left with nothing drawn. The rest are in the
    # page and appear on hover, on a pin, and in a local view.
    incident: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for pair in edges:
        incident[pair[0]].append(pair)
        incident[pair[1]].append(pair)
    backbone: set[tuple[str, str]] = {p for p, qs in edges.items() if len(qs) >= 2}
    for n in nodes:
        ranked = sorted(
            incident[n],
            key=lambda p: (
                -len(edges[p]),
                degree[p[1] if p[0] == n else p[0]],
                p[1] if p[0] == n else p[0],
            ),
        )
        backbone.update(ranked[:BACKBONE_PER_NODE])

    # The reader is asked to name what bridges two islands, so the strongest
    # few crossings of every community pair are drawn whatever their weight.
    # Without this only 56 of the map's 390 crossings survived the per-node
    # rule and most pairs showed no line at all.
    by_pair: dict[tuple[int, int], list[tuple[str, str]]] = defaultdict(list)
    for a, b in edges:
        ca, cb = membership[a], membership[b]
        if ca != cb:
            by_pair[(min(ca, cb), max(ca, cb))].append((a, b))
    for pair_edges in by_pair.values():
        ranked = sorted(
            pair_edges,
            key=lambda p: (-len(edges[p]), -(degree[p[0]] + degree[p[1]]), p),
        )
        backbone.update(ranked[:BRIDGES_PER_PAIR])

    # Degree is heavily skewed; the top percentile fuses the picture if it is
    # drawn and pulled like everything else. Those Concepts keep a capped
    # radius and a damped edge spring, both applied in the page.
    ranked_degrees = sorted(degree[n] for n in nodes)
    hub_cut = ranked_degrees[int(len(ranked_degrees) * HUB_PERCENTILE)]

    # A bridge is what the reader is asked to name, so its ends are always
    # labelled, alongside the highest-degree Concepts.
    bridges = sorted(
        (p for p in edges if membership[p[0]] != membership[p[1]]),
        key=lambda p: (-len(edges[p]), p),
    )
    labelled = [n for n in sorted(nodes, key=lambda n: (-degree[n], n))[:ALWAYS_LABELLED]]
    for p in bridges[:BRIDGES_LABELLED]:
        labelled.extend(p)

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
        "always_labelled": sorted({node_index[n] for n in labelled}),
        "backbone": [1 if (a, b) in backbone else 0 for (a, b) in sorted(edges)],
        "bridge": [
            1 if membership[a] != membership[b] else 0 for (a, b) in sorted(edges)
        ],
        "hub_cut": hub_cut,
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
            "backbone_edges": len(backbone),
            "bridge_edges": sum(
                1 for (a, b) in edges if membership[a] != membership[b]
            ),
            "backbone_bridges": sum(
                1 for p in backbone if membership[p[0]] != membership[p[1]]
            ),
            "hub_cut": hub_cut,
            "hubs": sum(1 for n in nodes if degree[n] > hub_cut),
        },
    }


GRAPH_CSS = r"""
  #graphwrap { flex: 1 1 auto; overflow: hidden; padding: 0; position: relative;
    background: var(--canvas); }
  svg#graph { display: block; width: 100%; height: 100%; cursor: grab;
    background: var(--canvas); }
  svg#graph.panning { cursor: grabbing; }
  #gscene .gedge { stroke: #6f7b8c; fill: none; }
  /* A crossing between two communities is the thing a reader is asked to
     name, so it is drawn brighter than a line inside one. */
  #gscene .gedge.br { stroke: #9fb6cf; fill: none; }
  /* The opening frame draws the backbone. Everything else is in the page and
     comes back on a hover, a pin, or in a local view. */
  #gscene .gedge.nb { display: none; }
  #gscene.showall .gedge.nb { display: block; }
  #gscene .gedge.nb.hl { display: block; }
  #ghulls .ghull { filter: url(#hullsoft); opacity: .1; pointer-events: none; }
  #ghullnames { pointer-events: none; }
  #ghullnames .ghullname { font-variant: small-caps;
    letter-spacing: .1em; opacity: .75; paint-order: stroke;
    stroke: #0e1116; stroke-width: 3px; stroke-linejoin: round; }
  #gscene .gnode circle { stroke: rgba(10,12,16,.85); stroke-width: 1; }
  #gscene .gnode { cursor: pointer; }
  #glabels { pointer-events: none; }
  /* A label sits over the canvas, so a click on the name used to land on
     nothing. The layer stays transparent to the pointer and each label takes
     it back, acting as its own Concept. */
  #glabels .glabel { font-size: 11px; fill: #ccd4df; pointer-events: auto;
    cursor: pointer;
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
  #graph-hud.folded { width: auto; }
  #graph-hud.folded #gsearch, #graph-hud.folded #gsuggest { display: none; }
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
    color: #6f7b8c; margin-bottom: 4px; cursor: pointer; white-space: nowrap; }
  #glegend .hd:hover { color: #cfd6e0; }
  #graph-hud.folded #glegend .hd { margin-bottom: 0; }
  #gcrumbs { position: absolute; left: 12px; bottom: 10px; right: 400px;
    font-size: 11.5px; color: #93a0b0; }
  #gcrumbs b { color: #e6ebf2; font-weight: 600; }
  #gcrumbs .sep { color: #55606f; margin: 0 5px; }
  #ghint { position: absolute; right: 12px; bottom: 10px; font-size: 11px;
    color: #6f7b8c; }
  /* Panel. One spacing grid, 4 / 8 / 12, and one type scale, 12 / 13 / 15 /
     18. Nothing else is allowed a size of its own. */
  #panel h2 { font-size: 18px; line-height: 1.25; margin: 0 24px 8px 0; font-weight: 600; }
  #panel .seclabel { font-size: 12px; letter-spacing: .04em; text-transform: uppercase;
    color: var(--ink-dim); margin: 20px 0 8px; }
  .chiprow { display: flex; flex-wrap: wrap; gap: 4px; margin: 8px 0; }
  .chip { display: inline-block; font-size: 12px; line-height: 1.5; padding: 0 8px;
    border-radius: 3px; background: #232b38; color: #b4c0cf; white-space: nowrap;
    max-width: 100%; overflow: hidden; text-overflow: ellipsis; }
  .chip-count { background: #1b2a3a; color: #9cc2e4; }
  .chip-island { background: #262039; color: #c0b0e2; }
  .chip-domain { background: #172c23; color: #8ecfa8; }
  .chip-value { background: #2d2617; color: #d9c08d; }
  .chip-fact { background: #16293a; color: #a8c8e4; }
  .chip-tradeoff { background: #271d38; color: #c4b0e4; }
  .chip-taste { background: #2f2717; color: #dfc98f; }
  .chip-untagged { background: #242a33; color: #9aa5b3; }
  #panel .tools { display: flex; flex-wrap: wrap; gap: 4px; margin: 12px 0 0; }
  #panel .tools button { font-size: 12px; padding: 4px 8px; border-radius: 3px; }
  .qlist { margin: 0; }
  .qline { font-size: 13px; line-height: 1.45; margin: 0 0 4px; padding: 4px 0 4px 12px;
    cursor: pointer; color: var(--ink); border-left: 2px solid var(--border); }
  .qline:hover, .qline:focus { border-left-color: var(--ink); background: var(--panel-raise);
    outline: none; }
  .qline.kbd { border-left-color: var(--ink); background: #26303e; }
  .qentry { border-left: 2px solid var(--ink); padding: 4px 0 8px 12px; margin: 0 0 12px; }
  .qtitle { font-size: 15px; line-height: 1.35; font-weight: 600; cursor: pointer; }
  .qtitle:hover { color: #ffffff; }
  .pos { margin: 12px 0 0; padding: 8px 12px; border: 1px solid var(--border);
    border-radius: 4px; background: var(--panel-raise); }
  .possum { font-size: 13px; line-height: 1.45; margin: 4px 0 0; }
  .arg { font-size: 12px; line-height: 1.45; margin: 8px 0 0; padding-left: 8px;
    border-left: 2px solid var(--border); }
  .argside { font-weight: 600; margin-right: 4px; }
  .arg-for .argside { color: #6fcf8f; }
  .arg-against .argside { color: #ee8d7f; }
  .claims { margin: 4px 0 0; }
  .claim { font-size: 12px; line-height: 1.5; margin: 8px 0 0; }
  .claimhead { display: flex; flex-wrap: wrap; align-items: baseline; gap: 8px; }
  .claim .voice { font: inherit; font-weight: 600; padding: 0; border: 0; background: none;
    color: var(--ink); cursor: pointer; text-decoration: underline dotted; }
  .claim .voice:hover { color: #ffffff; background: none; }
  .claimmeta { color: var(--ink-dim); }
  .claimpara { margin: 4px 0 0; }
  .quote { margin: 4px 0 0; padding: 4px 0 4px 8px; border-left: 2px solid var(--border);
    color: var(--ink-dim); font-style: italic; }
  .srcline { margin: 4px 0 0; }
  .nblist { display: flex; flex-wrap: wrap; gap: 4px; }
  .gchip { font: inherit; font-size: 12px; line-height: 1.5; padding: 0 8px;
    border-radius: 3px; border: 1px solid var(--border); background: var(--panel-raise);
    color: var(--ink); cursor: pointer; }
  .gchip:hover { background: #26303e; }
  .gchip.kbd { background: var(--ink); color: #11151c; border-color: var(--ink); }
  .gchip .w { color: var(--ink-dim); margin-left: 8px; }
  .gchip.kbd .w { color: #3b4655; }
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
  var HUB_R = 2.2 + Math.sqrt(G.hub_cut) * 1.5;
  for (var ri = 0; ri < GN; ri++) {
    gr[ri] = Math.min(2.2 + Math.sqrt(G.deg[ri]) * 1.5, HUB_R);
  }

  var gNodeEl = new Array(GN), gLabelEl = new Array(GN), gEdgeEl = new Array(GE);
  var commCentre = {};   // community index -> {x, y, r}, set by the two-level layout
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
  // Hubs are the top degree percentile, computed at build time. They draw at
  // a capped radius and pull on a damped spring: a Concept touching ninety
  // Questions otherwise drags every one of them onto itself, and that is what
  // fused the first opening frame into a single mass.
  var HUB_CUT = G.hub_cut;
  function isHub(i) { return G.deg[i] > HUB_CUT; }

  function seedNodes(ids, seed, side) {
    var rand = mulberry32(seed);
    for (var i = 0; i < ids.length; i++) {
      var ang = rand() * Math.PI * 2, rad = Math.sqrt(rand()) * side / 2;
      gx[ids[i]] = Math.cos(ang) * rad;
      gy[ids[i]] = Math.sin(ang) * rad;
    }
  }

  // opt: gravity (pull to the origin, flattens structure when strong),
  // containR (soft disc boundary: a node past it is eased back, never
  // snapped), hubPull (pull to the origin in proportion to a node's share of
  // the group's top degree, so the hubs sit in the middle and the graph's own
  // forces decide everything else).
  function simulate(ids, edgeList, ticks, side, opt) {
    var n = ids.length;
    if (n < 2) return;
    opt = opt || {};
    var grav = opt.gravity === undefined ? 0.006 : opt.gravity;
    var containR = opt.containR || 0;
    var hubPull = opt.hubPull || 0;
    var maxDeg = 1;
    for (var md = 0; md < n; md++) if (G.deg[ids[md]] > maxDeg) maxDeg = G.deg[ids[md]];
    var k = Math.sqrt(side * side / n), k2 = k * k;
    var dx = new Float64Array(n), dy = new Float64Array(n);
    var slot = {};
    for (var m = 0; m < n; m++) slot[ids[m]] = m;
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
      for (var e = 0; e < edgeList.length; e++) {
        var ee = edgeList[e], ia = G.e_a[ee], ib = G.e_b[ee];
        var sa = slot[ia], sb = slot[ib];
        if (sa === undefined || sb === undefined) continue;
        var ex = gx[ia] - gx[ib], ey = gy[ia] - gy[ib];
        var ed = Math.sqrt(ex * ex + ey * ey) || 0.01;
        var wf = 1 + Math.log(1 + edgeWeight(ee)) * 0.9;
        if (isHub(ia) || isHub(ib)) wf *= 0.28;
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
        if (grav) { gx[id] -= gx[id] * grav; gy[id] -= gy[id] * grav; }
        if (hubPull) {
          var hp = hubPull * (G.deg[id] / maxDeg);
          gx[id] -= gx[id] * hp;
          gy[id] -= gy[id] * hp;
        }
        if (containR) {
          var rd = Math.sqrt(gx[id] * gx[id] + gy[id] * gy[id]);
          if (rd > containR) {
            var back = (rd - containR) * 0.3 / rd;
            gx[id] -= gx[id] * back;
            gy[id] -= gy[id] * back;
          }
        }
      }
    }
  }

  function runLayout(ids, edgeList, ticks, seed, opt) {
    if (!ids.length) return;
    if (ids.length === 1) { gx[ids[0]] = 0; gy[ids[0]] = 0; return; }
    opt = opt || {};
    var side = opt.side || Math.sqrt(ids.length * 1500) + 90;
    seedNodes(ids, seed, side);
    simulate(ids, edgeList, ticks, side, opt);
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

  // --- the opening frame: communities as islands --------------------------
  // One force run over 1368 Concepts gives one mass. The communities are
  // real, but they interleave, and a cold reader could not separate three of
  // them by eye (map-review.md, 2026-09-30). The opening layout is built in
  // two levels instead. Each community is laid out on its own, from its own
  // edges alone, and becomes a disc; the discs are then packed -- pushed
  // apart wherever they overlap, pulled together by the Questions that cross
  // between them -- seeded on a ring that alternates large and small so two
  // big ones never start adjacent. The 125 detached clusters are not a
  // community, so they ring the outside instead of taking room in the middle.

  function edgesWithin(ids) {
    var inSet = {};
    for (var i = 0; i < ids.length; i++) inSet[ids[i]] = true;
    var seen = {}, out = [];
    for (var a = 0; a < ids.length; a++) {
      var n = ids[a];
      for (var b = 0; b < gAdj[n].length; b++) {
        var e = gAdj[n][b];
        if (!seen[e] && inSet[other(e, n)]) { seen[e] = true; out.push(e); }
      }
    }
    return out;
  }

  function componentsOf(ids) {
    var inSet = {};
    for (var i = 0; i < ids.length; i++) inSet[ids[i]] = true;
    var seen = {}, out = [];
    for (var s = 0; s < ids.length; s++) {
      var start = ids[s];
      if (seen[start]) continue;
      seen[start] = true;
      var stack = [start], comp = [];
      while (stack.length) {
        var x = stack.pop();
        comp.push(x);
        for (var a = 0; a < gAdj[x].length; a++) {
          var y = other(gAdj[x][a], x);
          if (inSet[y] && !seen[y]) { seen[y] = true; stack.push(y); }
        }
      }
      comp.sort(function (p, q) { return p - q; });
      out.push(comp);
    }
    return out;
  }

  function recentre(ids) {
    var cx = 0, cy = 0;
    for (var i = 0; i < ids.length; i++) { cx += gx[ids[i]]; cy += gy[ids[i]]; }
    cx /= ids.length; cy /= ids.length;
    var r = 0;
    for (var j = 0; j < ids.length; j++) {
      var id = ids[j];
      gx[id] -= cx; gy[id] -= cy;
      var d = Math.sqrt(gx[id] * gx[id] + gy[id] * gy[id]) + gr[id];
      if (d > r) r = d;
    }
    return r;
  }

  function shift(ids, dx, dy) {
    for (var i = 0; i < ids.length; i++) { gx[ids[i]] += dx; gy[ids[i]] += dy; }
  }

  // Two hulls must never touch. Each is its island's points plus 30, so
  // the gap between two packed discs has to clear both pads with room to
  // spare for the names that sit inside them.
  var DISC_GAP = 96;

  function packDiscs(units, interW) {
    var n = units.length;
    if (n === 0) return;
    var byComm = {};
    for (var i = 0; i < n; i++) byComm[units[i].comm] = units[i];
    var area = 0;
    for (var j = 0; j < n; j++) area += units[j].r * units[j].r;
    var R0 = Math.sqrt(area) * 1.15 + DISC_GAP;
    var order = units.slice().sort(function (a, b) { return b.r - a.r || a.comm - b.comm; });
    var ring = [], lo = 0, hi = n - 1;
    for (var s = 0; s < n; s++) ring.push(s % 2 === 0 ? order[lo++] : order[hi--]);
    for (var t = 0; t < n; t++) {
      var ang = (t / n) * Math.PI * 2;
      ring[t].cx = Math.cos(ang) * R0;
      ring[t].cy = Math.sin(ang) * R0;
    }
    for (var it = 0; it < 700; it++) {
      for (var a = 0; a < n; a++) { units[a].fx = 0; units[a].fy = 0; }
      for (var b = 0; b < n; b++) {
        for (var c = b + 1; c < n; c++) {
          var A = units[b], B = units[c];
          var dx = B.cx - A.cx, dy = B.cy - A.cy;
          var d = Math.sqrt(dx * dx + dy * dy) || 0.01;
          var want = A.r + B.r + DISC_GAP;
          if (d >= want) continue;
          var push = (want - d) * 0.5;
          A.fx -= dx / d * push; A.fy -= dy / d * push;
          B.fx += dx / d * push; B.fy += dy / d * push;
        }
      }
      for (var key in interW) {
        if (!interW.hasOwnProperty(key)) continue;
        var parts = key.split(",");
        var U = byComm[+parts[0]], V = byComm[+parts[1]];
        if (!U || !V) continue;
        var ex = V.cx - U.cx, ey = V.cy - U.cy;
        var ed = Math.sqrt(ex * ex + ey * ey) || 0.01;
        var slack = ed - (U.r + V.r + DISC_GAP);
        if (slack <= 0) continue;
        var pull = Math.min(slack * 0.5, slack * 0.006 * interW[key]);
        U.fx += ex / ed * pull; U.fy += ey / ed * pull;
        V.fx -= ex / ed * pull; V.fy -= ey / ed * pull;
      }
      for (var u = 0; u < n; u++) {
        // Without a real pull to the middle the discs stay on the seed ring
        // and leave a hole; separation alone never contracts.
        units[u].cx += units[u].fx - units[u].cx * 0.022;
        units[u].cy += units[u].fy - units[u].cy * 0.022;
      }
    }
  }

  // The detached clusters used to ring the body at three times its radius,
  // which read as decoration rather than data. They are packed into a band
  // below the body instead: rows of tight blobs, as wide as the body, so
  // switching them on adds a grey shelf under the map rather than a halo
  // around it.
  function bandDiscs(units, minx, maxx, maxy) {
    if (!units.length) return;
    var gap = 22;
    var width = Math.max(maxx - minx, 400);
    var x = minx, y = maxy + 60, rowH = 0;
    for (var i = 0; i < units.length; i++) {
      var u = units[i];
      var d = u.r * 2;
      if (x > minx && x + d > minx + width) {
        x = minx;
        y += rowH + gap;
        rowH = 0;
      }
      u.cx = x + u.r;
      u.cy = y + u.r;
      x += d + gap;
      if (d > rowH) rowH = d;
    }
  }

  function layoutTwoLevel(ids, edgeList) {
    var byComm = {};
    for (var i = 0; i < ids.length; i++) {
      var c = G.comm[ids[i]];
      (byComm[c] || (byComm[c] = [])).push(ids[i]);
    }
    var intra = {}, interW = {};
    for (var e = 0; e < edgeList.length; e++) {
      var ee = edgeList[e], ca = G.comm[G.e_a[ee]], cb = G.comm[G.e_b[ee]];
      if (ca === cb) (intra[ca] || (intra[ca] = [])).push(ee);
      else {
        var key = Math.min(ca, cb) + "," + Math.max(ca, cb);
        interW[key] = (interW[key] || 0) + edgeWeight(ee);
      }
    }
    var core = [], fringe = [];
    var keys = [];
    for (var k in byComm) if (byComm.hasOwnProperty(k)) keys.push(+k);
    keys.sort(function (a, b) { return a - b; });
    for (var q = 0; q < keys.length; q++) {
      var comm = keys[q], members = byComm[comm];
      if (comm === G.islands_comm) {
        var comps = componentsOf(members);
        comps.sort(function (a, b) { return b.length - a.length || a[0] - b[0]; });
        for (var z = 0; z < comps.length; z++) {
          // A detached cluster of two dots does not need the spacing a
          // community of 132 needs; at the default side, 125 of them
          // ringed the body at four times its own radius.
          runLayout(comps[z], edgesWithin(comps[z]), 110, 9001 + z, {
            gravity: 0.06,
            side: Math.sqrt(comps[z].length) * 15 + 14
          });
          fringe.push({ ids: comps[z], r: recentre(comps[z]), comm: comm });
        }
      } else {
        // Inside an island, structure rather than packing. Strong gravity
        // plus the collision pass produced concentric rings -- an
        // algorithm's signature, not the data's shape. Instead the island
        // keeps a soft disc boundary, its hubs are drawn to the middle in
        // proportion to their degree, and everything else is decided by the
        // Questions that join these Concepts.
        // The natural spread has to sit inside the boundary, or every
        // low-degree Concept presses on it and the island grows an arc --
        // the same signature the concentric rings were. side is set so the
        // force layout's own radius lands well within containR, which then
        // only catches outliers.
        var target = Math.sqrt(members.length) * 24 + 50;
        runLayout(members, intra[comm] || [], 340, 1337 + comm, {
          gravity: 0.003,
          hubPull: 0.05,
          containR: target,
          side: target * 1.15
        });
        core.push({ comm: comm, ids: members, r: recentre(members) });
      }
    }
    packDiscs(core, interW);
    var bminx = Infinity, bmaxx = -Infinity, bmaxy = -Infinity;
    for (var p = 0; p < core.length; p++) {
      bminx = Math.min(bminx, core[p].cx - core[p].r);
      bmaxx = Math.max(bmaxx, core[p].cx + core[p].r);
      bmaxy = Math.max(bmaxy, core[p].cy + core[p].r);
    }
    if (bminx === Infinity) { bminx = -400; bmaxx = 400; bmaxy = 400; }
    bandDiscs(fringe, bminx, bmaxx, bmaxy);
    commCentre = {};
    for (var u = 0; u < core.length; u++) {
      shift(core[u].ids, core[u].cx, core[u].cy);
      commCentre[core[u].comm] = { x: core[u].cx, y: core[u].cy, r: core[u].r };
    }
    for (var v = 0; v < fringe.length; v++) shift(fringe[v].ids, fringe[v].cx, fringe[v].cy);
    relaxCollisions(ids, 40);
  }

  // --- island hulls -------------------------------------------------------
  // A soft shape under each island in its own colour. It carries the island's
  // name, so the legend stops being the only place the colours are explained,
  // and it gives the eye a boundary the scattered low-degree Concepts do not.

  function convexHull(points) {
    if (points.length < 3) return points.slice();
    var pts = points.slice().sort(function (a, b) { return a[0] - b[0] || a[1] - b[1]; });
    function cross(o, a, b) {
      return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
    }
    var lower = [];
    for (var i = 0; i < pts.length; i++) {
      while (lower.length >= 2 && cross(lower[lower.length - 2], lower[lower.length - 1], pts[i]) <= 0) lower.pop();
      lower.push(pts[i]);
    }
    var upper = [];
    for (var j = pts.length - 1; j >= 0; j--) {
      while (upper.length >= 2 && cross(upper[upper.length - 2], upper[upper.length - 1], pts[j]) <= 0) upper.pop();
      upper.push(pts[j]);
    }
    lower.pop(); upper.pop();
    return lower.concat(upper);
  }

  // Catmull-Rom through the expanded hull vertices, closed: the blur alone
  // leaves polygon corners showing at high zoom.
  function smoothClosedPath(p) {
    if (p.length < 3) return "";
    var d = "M" + p[0][0].toFixed(1) + " " + p[0][1].toFixed(1);
    for (var i = 0; i < p.length; i++) {
      var p0 = p[(i - 1 + p.length) % p.length];
      var p1 = p[i];
      var p2 = p[(i + 1) % p.length];
      var p3 = p[(i + 2) % p.length];
      d += "C" + (p1[0] + (p2[0] - p0[0]) / 6).toFixed(1) + " " +
                 (p1[1] + (p2[1] - p0[1]) / 6).toFixed(1) + " " +
                 (p2[0] - (p3[0] - p1[0]) / 6).toFixed(1) + " " +
                 (p2[1] - (p3[1] - p1[1]) / 6).toFixed(1) + " " +
                 p2[0].toFixed(1) + " " + p2[1].toFixed(1);
    }
    return d + "Z";
  }

  var hullOf = {};   // community index -> {path, cx, topY, colour}

  function buildHulls() {
    hullOf = {};
    if (!gHullLayer) return;
    gHullLayer.innerHTML = "";
    if (!Object.keys(commCentre).length) return;   // local views carry no islands
    var byComm = {};
    for (var a = 0; a < activeNode.length; a++) {
      var i = activeNode[a];
      var c = G.comm[i];
      if (c === G.islands_comm) continue;
      (byComm[c] || (byComm[c] = [])).push(i);
    }
    var keys = [];
    for (var k in byComm) if (byComm.hasOwnProperty(k)) keys.push(+k);
    keys.sort(function (a, b) { return byComm[b].length - byComm[a].length || a - b; });
    for (var q = 0; q < keys.length; q++) {
      var comm = keys[q], members = byComm[comm];
      if (members.length < 3) continue;
      // The hull is drawn over the island's body, not its stragglers: a
      // convex hull over every member reaches out to the furthest satellite
      // and the thirteen shapes then overlap into mud. Members past the 80th
      // percentile of distance from the island's own centre are left out of
      // the shape; they are still drawn, still coloured, still theirs.
      var c0 = commCentre[comm] || { x: 0, y: 0 };
      var dists = [];
      for (var m0 = 0; m0 < members.length; m0++) {
        var ddx = gx[members[m0]] - c0.x, ddy = gy[members[m0]] - c0.y;
        dists.push(Math.sqrt(ddx * ddx + ddy * ddy));
      }
      var cut = dists.slice().sort(function (a, b) { return a - b; })[
        Math.max(2, Math.floor(dists.length * 0.8) - 1)
      ];
      var pts = [];
      for (var m = 0; m < members.length; m++) {
        if (dists[m] <= cut) pts.push([gx[members[m]], gy[members[m]]]);
      }
      if (pts.length < 3) continue;
      var hull = convexHull(pts);
      if (hull.length < 3) continue;
      var cx = 0, cy = 0;
      for (var h = 0; h < hull.length; h++) { cx += hull[h][0]; cy += hull[h][1]; }
      cx /= hull.length; cy /= hull.length;
      var pad = 30, expanded = [], topY = Infinity, hminx = Infinity, hmaxx = -Infinity;
      for (var e2 = 0; e2 < hull.length; e2++) {
        var vx2 = hull[e2][0] - cx, vy2 = hull[e2][1] - cy;
        var len = Math.sqrt(vx2 * vx2 + vy2 * vy2) || 1;
        var px = hull[e2][0] + vx2 / len * pad, py = hull[e2][1] + vy2 / len * pad;
        expanded.push([px, py]);
        if (py < topY) topY = py;
        if (px < hminx) hminx = px;
        if (px > hmaxx) hmaxx = px;
      }
      var path = svgEl("path", {
        class: "ghull",
        d: smoothClosedPath(expanded),
        fill: G.communities[comm].color,
        "data-comm": comm
      });
      gHullLayer.appendChild(path);
      hullOf[comm] = {
        cx: cx, topY: topY, minx: hminx, maxx: hmaxx,
        color: G.communities[comm].color
      };
    }
  }

  function buildHullNames() {
    if (!gHullNameLayer) return;
    gHullNameLayer.innerHTML = "";
    for (var c in hullOf) {
      if (!hullOf.hasOwnProperty(c)) continue;
      var t = svgEl("text", { class: "ghullname", "text-anchor": "middle", "data-comm": c });
      t.textContent = G.communities[+c].name;
      t.setAttribute("fill", hullOf[c].color);
      gHullNameLayer.appendChild(t);
      hullOf[c].el = t;
    }
  }

  // The name belongs to its island, so it is set inside the hull just under
  // its top edge -- never floating in the gap between two islands, which is
  // where a name placed above the shape ends up. An island's name is three
  // Concepts, which rarely fits a hull on one line, so it is allowed to break
  // between them; if even the narrowest arrangement will not fit at 8px the
  // name is dropped rather than hung outside its own shape.
  var NAME_CHAR = 0.62, NAME_MAX = 11, NAME_MIN = 8;

  function nameLayouts(name) {
    var parts = name.split(" \u00b7 ");
    if (parts.length < 2) return [[name]];
    if (parts.length === 2) return [[name], [parts[0], parts[1]]];
    return [
      [name],
      [parts[0], parts[1] + " \u00b7 " + parts[2]],
      [parts[0] + " \u00b7 " + parts[1], parts[2]],
      [parts[0], parts[1], parts[2]]
    ];
  }

  function longestLine(lines) {
    var n = 0;
    for (var i = 0; i < lines.length; i++) if (lines[i].length > n) n = lines[i].length;
    return n;
  }

  function updateHullNames() {
    var r = gsvg.getBoundingClientRect();
    var ins = canvasInsets();
    var boxes = [];
    for (var c in hullOf) {
      if (!hullOf.hasOwnProperty(c)) continue;
      var h = hullOf[c];
      if (!h.el) continue;
      if (commOff[+c]) { h.el.style.display = "none"; continue; }
      var name = G.communities[+c].name;
      var left = h.minx * vk + vx, right = h.maxx * vk + vx;
      var room = right - left - 16;
      var opts = nameLayouts(name), chosen = null, size = 0, widest = 0;
      for (var o = 0; o < opts.length; o++) {
        var at11 = 0;
        for (var li2 = 0; li2 < opts[o].length; li2++) {
          at11 = Math.max(at11, textWidth(opts[o][li2], NAME_MAX, false));
        }
        var sz = Math.min(NAME_MAX, NAME_MAX * room / at11);
        if (sz >= NAME_MIN) { chosen = opts[o]; size = sz; widest = at11 * sz / NAME_MAX; break; }
      }
      if (!chosen) { h.el.style.display = "none"; continue; }
      var half = widest / 2;
      var sx = h.cx * vk + vx;
      var top = h.topY * vk + vy + size + 5;
      if (sx - half < left + 8) sx = left + 8 + half;
      if (sx + half > right - 8) sx = right - 8 - half;
      var blockH = chosen.length * (size + 2);
      if (sx - half < ins.left || sx + half > r.width - ins.right ||
          top < ins.top || top + blockH > r.height - ins.bottom) {
        h.el.style.display = "none";
        continue;
      }
      h.el.innerHTML = "";
      for (var li = 0; li < chosen.length; li++) {
        var ts = svgEl("tspan", {
          x: sx.toFixed(1),
          y: (top + li * (size + 2)).toFixed(1)
        });
        ts.textContent = chosen[li];
        h.el.appendChild(ts);
      }
      h.el.setAttribute("font-size", size.toFixed(1));
      h.el.style.display = "block";
      boxes.push({ x: sx - half, y: top - size - 2, w: half * 2, h: blockH + 4 });
    }
    return boxes;
  }

  // --- scene --------------------------------------------------------------
  var gsvg = document.getElementById("graph");
  var gscene = null, gEdgeLayer = null, gNodeLayer = null, gLabelLayer = null;
  var gInterLayer = null, gHullLayer = null, gHullNameLayer = null;
  var gMeasure = null, widthCache = {};

  function textWidth(text, size, bold) {
    var key = size + "|" + (bold ? 1 : 0) + "|" + text;
    var hit = widthCache[key];
    if (hit !== undefined) return hit;
    var w;
    if (!gMeasure) {
      w = text.length * size * 0.58;
    } else {
      gMeasure.setAttribute("font-size", size);
      gMeasure.style.fontWeight = bold ? "600" : "400";
      gMeasure.textContent = text;
      try {
        w = gMeasure.getComputedTextLength();
      } catch (err) {
        w = text.length * size * 0.58;
      }
      if (!w) w = text.length * size * 0.58;
    }
    widthCache[key] = w;
    return w;
  }

  function buildScene() {
    gsvg.innerHTML = "";
    var defs = svgEl("defs", {});
    defs.innerHTML = '<filter id="hullsoft" x="-25%" y="-25%" width="150%" height="150%">' +
      '<feGaussianBlur stdDeviation="22"/></filter>';
    gsvg.appendChild(defs);
    gNodeEl = new Array(GN); gLabelEl = new Array(GN); gEdgeEl = new Array(GE);
    hlNodes = []; hlEdges = [];
    // A local view draws every line it holds; the opening frame draws the
    // backbone and keeps the rest one hover away.
    gscene = svgEl("g", { id: "gscene", class: localDepth > 0 ? "showall" : "" });
    gHullLayer = svgEl("g", { id: "ghulls" });
    gInterLayer = svgEl("g", { id: "ginter" });
    gEdgeLayer = svgEl("g", { id: "gintra" });
    gNodeLayer = svgEl("g", {});
    gscene.appendChild(gHullLayer);
    gscene.appendChild(gInterLayer);
    gscene.appendChild(gEdgeLayer);
    gscene.appendChild(gNodeLayer);
    gsvg.appendChild(gscene);
    gHullNameLayer = svgEl("g", { id: "ghullnames" });
    gsvg.appendChild(gHullNameLayer);
    gLabelLayer = svgEl("g", { id: "glabels" });
    gsvg.appendChild(gLabelLayer);
    // Label widths were guessed from the character count. A bold 12px
    // neighbour label runs about 12% wider than that guess, which is more
    // than the margin the edge test allows, so a label passed the test and
    // was then cut by the canvas edge where the panel begins. They are
    // measured now, once each, against this hidden text node.
    // In its own layer, not in #glabels: anything that selects the drawn
    // labels must not find the ruler among them.
    var measureLayer = svgEl("g", { id: "gmeasure" });
    measureLayer.style.visibility = "hidden";
    gMeasure = svgEl("text", { class: "glabel", x: "-9999", y: "-9999" });
    gMeasure.style.display = "block";
    measureLayer.appendChild(gMeasure);
    gsvg.appendChild(measureLayer);
    widthCache = {};

    // A line inside an island is drawn above, a crossing below and as a
    // curve: straight crossings cut the canvas into a star and read as noise,
    // a curve bowed toward the two island centres stays out of the way and
    // still says which islands it joins.
    for (var a = 0; a < activeEdge.length; a++) {
      var e = activeEdge[a];
      var w = edgeWeight(e);
      var crossing = G.bridge[e] === 1;
      var el = svgEl(crossing ? "path" : "line", {
        class: "gedge" + (G.backbone[e] ? "" : " nb") + (crossing ? " br" : ""),
        "stroke-width": (crossing
          ? Math.min(0.5 + w * 0.5, 3)
          : Math.min(0.32 + w * 0.62, 4)).toFixed(2),
        "stroke-opacity": Math.min((crossing ? 0.10 : 0.13) + w * 0.12, 0.8).toFixed(3)
      });
      gEdgeEl[e] = el;
      (crossing ? gInterLayer : gEdgeLayer).appendChild(el);
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
      bindNode(lbl, i);
    }
    buildHulls();
    buildHullNames();
    placeAll();
  }

  // A crossing is drawn as a quadratic bowed toward the midpoint of the two
  // island centres. One function returns that control point, so what is drawn
  // and what a click is tested against can never drift apart.
  function edgeControl(e) {
    var ia = G.e_a[e], ib = G.e_b[e];
    var mx = (gx[ia] + gx[ib]) / 2, my = (gy[ia] + gy[ib]) / 2;
    var ca = commCentre[G.comm[ia]], cb = commCentre[G.comm[ib]];
    if (!ca || !cb) return { x: mx, y: my };
    return {
      x: mx + (((ca.x + cb.x) / 2) - mx) * 0.55,
      y: my + (((ca.y + cb.y) / 2) - my) * 0.55
    };
  }
  function edgePointAt(e, t) {
    var ia = G.e_a[e], ib = G.e_b[e];
    if (G.bridge[e] !== 1) {
      return { x: gx[ia] + (gx[ib] - gx[ia]) * t, y: gy[ia] + (gy[ib] - gy[ia]) * t };
    }
    var q = edgeControl(e), u = 1 - t;
    return {
      x: u * u * gx[ia] + 2 * u * t * q.x + t * t * gx[ib],
      y: u * u * gy[ia] + 2 * u * t * q.y + t * t * gy[ib]
    };
  }

  function placeAll() {
    for (var a = 0; a < activeEdge.length; a++) {
      var e = activeEdge[a], el = gEdgeEl[e];
      var ia = G.e_a[e], ib = G.e_b[e];
      if (el.tagName === "path") {
        var q = edgeControl(e);
        el.setAttribute("d",
          "M" + gx[ia].toFixed(1) + " " + gy[ia].toFixed(1) +
          "Q" + q.x.toFixed(1) + " " + q.y.toFixed(1) +
          " " + gx[ib].toFixed(1) + " " + gy[ib].toFixed(1));
      } else {
        el.setAttribute("x1", gx[ia].toFixed(1));
        el.setAttribute("y1", gy[ia].toFixed(1));
        el.setAttribute("x2", gx[ib].toFixed(1));
        el.setAttribute("y2", gy[ib].toFixed(1));
      }
    }
    for (var b = 0; b < activeNode.length; b++) {
      var i = activeNode[b];
      gNodeEl[i].setAttribute("transform", "translate(" + gx[i].toFixed(1) + "," + gy[i].toFixed(1) + ")");
    }
    updateLabels();
  }

  // True while the view is exactly what fitView last produced. Any wheel,
  // drag or centring clears it, so a width change re-fits the opening frame
  // but never throws away a reader's own zoom.
  var viewIsFitted = false;
  var lastCanvasW = 0;

  function applyTransform() {
    gscene.setAttribute("transform", "translate(" + vx + "," + vy + ") scale(" + vk + ")");
    updateLabels();
  }

  // The frame is whatever is on: hiding a community and refitting gives the
  // rest of the map the whole canvas.
  // The legend floats over the left of the canvas and the side panel takes
  // the right. Neither is canvas, so the fit is computed inside what is
  // actually left, and a Concept at the edge is no longer half-covered.
  function canvasInsets() {
    var r = gsvg.getBoundingClientRect();
    var left = 12;
    var hud = document.getElementById("graph-hud");
    if (hud && hud.offsetWidth) {
      var hr = hud.getBoundingClientRect();
      left = Math.max(left, hr.right - r.left + 16);
    }
    // The panel sits beside the canvas, so normally it takes nothing off it.
    // The overlap is reserved anyway: between opening the panel and the
    // browser reflowing, the canvas still reports its old width, and a label
    // placed in that instant is placed against a box that no longer exists.
    var right = 12;
    var panel = document.getElementById("panel");
    if (panel && panel.classList.contains("open")) {
      var pr = panel.getBoundingClientRect();
      right = Math.max(right, r.right - pr.left + 12);
    }
    return { left: left, right: right, top: 12, bottom: 30 };
  }

  function fitView() {
    var minx = Infinity, miny = Infinity, maxx = -Infinity, maxy = -Infinity;
    for (var a = 0; a < activeNode.length; a++) {
      var i = activeNode[a];
      if (commOff[G.comm[i]]) continue;
      if (gx[i] < minx) minx = gx[i];
      if (gy[i] < miny) miny = gy[i];
      if (gx[i] > maxx) maxx = gx[i];
      if (gy[i] > maxy) maxy = gy[i];
    }
    if (minx === Infinity) { minx = miny = -100; maxx = maxy = 100; }
    var r = gsvg.getBoundingClientRect();
    var ins = canvasInsets();
    var availW = Math.max(r.width - ins.left - ins.right, 60);
    var availH = Math.max(r.height - ins.top - ins.bottom, 60);
    vk = Math.min(availW / Math.max(maxx - minx, 1), availH / Math.max(maxy - miny, 1));
    vk = Math.max(Math.min(vk, 4), 0.05);
    vx = ins.left + availW / 2 - (minx + maxx) / 2 * vk;
    vy = ins.top + availH / 2 - (miny + maxy) / 2 * vk;
    lastCanvasW = r.width;
    applyTransform();
    viewIsFitted = true;
  }

  // Opening the side panel narrows the canvas. Without this the transform
  // and the labels stayed sized to the wider box, and a label near the right
  // edge was cut in half by the panel.
  function onCanvasResize() {
    if (!gscene) return;
    var r = gsvg.getBoundingClientRect();
    if (!r.width || Math.abs(r.width - lastCanvasW) < 1) return;
    var delta = r.width - lastCanvasW;
    lastCanvasW = r.width;
    if (viewIsFitted) {
      fitView();
    } else {
      vx += delta / 2;
      applyTransform();
    }
  }
  if (window.ResizeObserver) {
    new ResizeObserver(onCanvasResize).observe(gsvg);
  } else {
    window.addEventListener("resize", onCanvasResize);
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
      cands.push({ i: i, pri: pri, sx: sx, sy: sy + 3, el: el });
    }
    cands.sort(function (p, q) { return p.pri - q.pri || G.deg[q.i] - G.deg[p.i] || p.i - q.i; });
    // A label sits to the right of its dot, unless that would put it past the
    // canvas -- where the side panel is -- in which case it flips to the left.
    // Nothing is ever drawn under the panel: a label that fits on neither side
    // is not drawn at all.
    // The island names go down first and a Concept label never lands on one.
    // The legend's own box goes in with them, so nothing is drawn under it.
    var ins = canvasInsets();
    var placed = updateHullNames(), shown = 0;
    var hudEl = document.getElementById("graph-hud");
    if (hudEl && hudEl.offsetWidth) {
      var hb = hudEl.getBoundingClientRect();
      placed.push({
        x: hb.left - r.left - 4, y: hb.top - r.top - 4,
        w: hb.width + 8, h: hb.height + 8
      });
    }
    for (var c = 0; c < cands.length && shown < LABEL_BUDGET; c++) {
      var k = cands[c];
      var fs = k.pri <= 1 ? 12 : 11;
      var w = textWidth(G.labels[k.i], fs, k.pri <= 1);
      var rad = gr[k.i] * vk;
      var rightEdge = r.width - ins.right;
      var anchor = "start", tx = k.sx + rad + 3, left = tx;
      if (tx + w > rightEdge) {
        anchor = "end";
        tx = k.sx - rad - 3;
        left = tx - w;
      }
      var box = { x: left, y: k.sy - fs, w: w, h: fs + 3 };
      // One boundary test on the box that will actually be drawn, both
      // sides. Checking only the side the flip moved to left a Concept whose
      // dot sits just past the canvas with a label that overflowed whichever
      // way it faced -- which is how "hot patching" and "JS interop" were
      // still being cut by the panel after the flip was added.
      if (box.x < ins.left || box.x + box.w > rightEdge) continue;
      var clash = false;
      for (var q2 = 0; q2 < placed.length; q2++) {
        var o = placed[q2];
        if (box.x < o.x + o.w && box.x + box.w > o.x && box.y < o.y + o.h && box.y + box.h > o.y) {
          clash = true; break;
        }
      }
      if (clash && k.pri > 0) continue;
      placed.push(box);
      k.el.setAttribute("x", tx.toFixed(1));
      k.el.setAttribute("y", k.sy.toFixed(1));
      k.el.setAttribute("text-anchor", anchor);
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
    viewIsFitted = false;
    applyTransform();
  }, { passive: false });

  gsvg.addEventListener("pointerdown", function (ev) {
    var sx = ev.clientX, sy = ev.clientY, ox = vx, oy = vy, moved = false;
    gsvg.classList.add("panning");
    function onMove(m) {
      if (Math.abs(m.clientX - sx) + Math.abs(m.clientY - sy) > 3) moved = true;
      vx = ox + (m.clientX - sx); vy = oy + (m.clientY - sy);
      viewIsFitted = false;
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
    var tol = 6 / vk, best = -1, bestD = tol;
    var drawnOnly = !localDepth;
    for (var a = 0; a < activeEdge.length; a++) {
      var e = activeEdge[a];
      if (drawnOnly && !G.backbone[e]) continue;      // it is not on screen
      if (commOff[G.comm[G.e_a[e]]] || commOff[G.comm[G.e_b[e]]]) continue;
      var d;
      if (G.bridge[e] === 1) {
        // Sampled along the curve, since the chord is not what is drawn.
        // Eight samples were too coarse once the islands moved apart and the
        // curves grew: a click sitting exactly on a long curve fell between
        // two samples and picked nothing. The bounding box rejects almost
        // every edge first, so the finer sampling costs nothing.
        var ax = gx[G.e_a[e]], ay = gy[G.e_a[e]];
        var bx2 = gx[G.e_b[e]], by2 = gy[G.e_b[e]];
        var qc = edgeControl(e);
        var loX = Math.min(ax, bx2, qc.x) - tol, hiX = Math.max(ax, bx2, qc.x) + tol;
        var loY = Math.min(ay, by2, qc.y) - tol, hiY = Math.max(ay, by2, qc.y) + tol;
        if (wx < loX || wx > hiX || wy < loY || wy > hiY) continue;
        // Sampling alone is not enough: a crossing can be 1700 units long,
        // so even fifty samples sit further apart than the click tolerance
        // and a click exactly on the curve falls between two of them. A
        // coarse scan finds the neighbourhood, then a ternary search closes
        // on the true nearest point.
        d = Infinity;
        var bestT = 0;
        for (var k2 = 0; k2 <= 24; k2++) {
          var tt = k2 / 24, pt = edgePointAt(e, tt);
          var sdx = pt.x - wx, sdy = pt.y - wy;
          var sd = sdx * sdx + sdy * sdy;
          if (sd < d) { d = sd; bestT = tt; }
        }
        var lo = Math.max(0, bestT - 1 / 24), hi = Math.min(1, bestT + 1 / 24);
        for (var it2 = 0; it2 < 40; it2++) {
          var m1 = lo + (hi - lo) / 3, m2 = hi - (hi - lo) / 3;
          var p1 = edgePointAt(e, m1), p2 = edgePointAt(e, m2);
          var d1 = (p1.x - wx) * (p1.x - wx) + (p1.y - wy) * (p1.y - wy);
          var d2 = (p2.x - wx) * (p2.x - wx) + (p2.y - wy) * (p2.y - wy);
          if (d1 < d2) hi = m2; else lo = m1;
        }
        var pf = edgePointAt(e, (lo + hi) / 2);
        d = Math.sqrt((pf.x - wx) * (pf.x - wx) + (pf.y - wy) * (pf.y - wy));
      } else {
        var x1 = gx[G.e_a[e]], y1 = gy[G.e_a[e]], x2 = gx[G.e_b[e]], y2 = gy[G.e_b[e]];
        var ddx = x2 - x1, ddy = y2 - y1;
        var L2 = ddx * ddx + ddy * ddy;
        var t = L2 === 0 ? 0 : Math.max(0, Math.min(1, ((wx - x1) * ddx + (wy - y1) * ddy) / L2));
        var px = x1 + t * ddx - wx, py = y1 + t * ddy - wy;
        d = Math.sqrt(px * px + py * py);
      }
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
    viewIsFitted = false;
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
      layoutTwoLevel(activeNode, activeEdge);
    } else {
      setActive(neighbourhood(centre, depth));
      commCentre = {};
      runLayout(activeNode, activeEdge, 420, 4242);
    }
    buildScene();
    fitView();
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

  // Domain texts are written as sentences, and one of them runs to eighty-five
  // characters ("Questions live in every Domain, e.g. language semantics,
  // ..."). A chip is a name, not a sentence: the text is used when it is short
  // enough to be a name, and otherwise the Domain's own id, which is already
  // short. The full text is the chip's tooltip either way.
  function domainName(did, text) {
    var t = (text || "").replace(/\.$/, "").trim();
    if (t && t.length <= 26) return t;
    // Acronyms stay acronyms; "core" is a word and must not become "CORE".
    if (/^(ml|wasm|wasi|api|abi|ffi|wit|cli|ui)$/.test(did)) return String(did).toUpperCase();
    var parts = String(did).split("-");
    return parts.map(function (w, i) {
      return i === 0 ? w.charAt(0).toUpperCase() + w.slice(1) : w;
    }).join(" ");
  }
  function domainChip(did, text) {
    var full = text !== undefined ? text : (W.domains[did] || did);
    var c = document.createElement("span");
    c.className = "chip chip-domain";
    c.textContent = domainName(did, full);
    c.title = full;
    return c;
  }
  function chip(text, cls) {
    var c = document.createElement("span");
    c.className = "chip" + (cls ? " " + cls : "");
    c.textContent = text;
    return c;
  }
  function chipRow() {
    var d = document.createElement("div");
    d.className = "chiprow";
    for (var i = 0; i < arguments.length; i++) if (arguments[i]) d.appendChild(arguments[i]);
    return d;
  }
  function sectionLabel(text) {
    var d = document.createElement("div");
    d.className = "seclabel";
    d.textContent = text;
    return d;
  }
  function questionBlock(qIdx) {
    var qid = G.qids[qIdx];
    var q = W.questions[qid];
    var wrap = document.createElement("div");
    wrap.className = "qentry";

    // The Question's text is the entry's one title. The list line above it is
    // hidden while the entry is open, so it is never printed twice.
    var head = document.createElement("div");
    head.className = "qtitle";
    head.textContent = q.text;
    wrap.appendChild(head);

    if (q.domains && q.domains.length) {
      var dwrap = chipRow();
      for (var d = 0; d < q.domains.length; d++) dwrap.appendChild(domainChip(q.domains[d]));
      wrap.appendChild(dwrap);
    }

    for (var p = 0; p < q.positions.length; p++) {
      var pid = q.positions[p], pos = W.positions[pid];
      var pb = document.createElement("div");
      pb.className = "pos";
      pb.appendChild(chipRow(chip(pos.tag || "untagged", "chip-" + (pos.tag || "untagged"))));
      var sum = document.createElement("div");
      sum.className = "possum";
      sum.textContent = pos.summary;
      pb.appendChild(sum);

      for (var ar = 0; ar < pos.arguments.length; ar++) {
        var arg = pos.arguments[ar];
        var ad = document.createElement("div");
        ad.className = "arg arg-" + (arg.side === "for" ? "for" : "against");
        var side = document.createElement("span");
        side.className = "argside";
        side.textContent = arg.side === "for" ? "For" : "Against";
        ad.appendChild(side);
        ad.appendChild(document.createTextNode(arg.text));
        if (arg.values && arg.values.length) {
          var vv = chipRow();
          for (var vi = 0; vi < arg.values.length; vi++) {
            vv.appendChild(chip(arg.values[vi], "chip-value"));
          }
          ad.appendChild(vv);
        }
        pb.appendChild(ad);
      }

      if (pos.claims.length) {
        pb.appendChild(sectionLabel(
          pos.claims.length + (pos.claims.length === 1 ? " Claim" : " Claims")));
        var cl = document.createElement("div");
        cl.className = "claims";
        for (var ci = 0; ci < pos.claims.length; ci++) cl.appendChild(claimBlock(pos.claims[ci]));
        pb.appendChild(cl);
      }
      wrap.appendChild(pb);
    }
    return wrap;
  }

  function claimBlock(c) {
    var d = document.createElement("div");
    d.className = "claim";

    var line = document.createElement("div");
    line.className = "claimhead";
    var vn = document.createElement("button");
    vn.className = "voice";
    vn.type = "button";
    vn.textContent = revealedVoice[c.voice] ? W.voice_names[c.voice] : "Voice " + c.n;
    vn.title = "Reveal this Voice";
    vn.addEventListener("click", function () {
      revealedVoice[c.voice] = !revealedVoice[c.voice];
      vn.textContent = revealedVoice[c.voice] ? W.voice_names[c.voice] : "Voice " + c.n;
    });
    line.appendChild(vn);
    var meta = document.createElement("span");
    meta.className = "claimmeta";
    meta.textContent = (c.date || "undated") + " · " + (c.checked ? "checked" : "provisional");
    line.appendChild(meta);
    d.appendChild(line);

    if (c.paraphrase) {
      var pp = document.createElement("div");
      pp.className = "claimpara";
      pp.textContent = c.paraphrase;
      d.appendChild(pp);
    }
    if (c.quote) {
      var bq = document.createElement("div");
      bq.className = "quote";
      bq.textContent = c.quote;
      d.appendChild(bq);
    }
    if (c.source && c.source.url) {
      var sl = document.createElement("div");
      sl.className = "srcline";
      var a = document.createElement("a");
      a.href = c.source.url; a.target = "_blank"; a.rel = "noopener";
      a.textContent = c.source.title || c.source.url;
      sl.appendChild(a);
      d.appendChild(sl);
    }
    return d;
  }

  function showConceptPanel(i) {
    var body = document.getElementById("panel-body");
    body.innerHTML = "";
    kbdIndex = -1;
    var h = document.createElement("h2");
    h.textContent = G.labels[i];
    body.appendChild(h);

    // Facts about the Concept are chips, not a sentence: three separate
    // things -- how many Questions touch it, which island it is in, which
    // Domain most of those Questions are live in -- were reading as one
    // run-on line ending in a stray full stop.
    // "degree", not "links": the number counts (Question, neighbour) pairs, so
    // it runs ahead of the neighbour count whenever two Concepts share more
    // than one Question. Calling it links would be a quiet lie.
    var degChip = chip("degree " + G.deg[i], "chip-count");
    degChip.title = "(Question, neighbouring Concept) pairs this Concept takes part in";
    body.appendChild(chipRow(
      degChip,
      chip(G.communities[G.comm[i]].name, "chip-island"),
      G.dom[i] >= 0 ? domainChip(G.domains[G.dom[i]].id, G.domains[G.dom[i]].text) : null
    ));

    var tools = document.createElement("div");
    tools.className = "tools";
    [["Local 1", 1], ["Local 2", 2], ["Whole map", 0]].forEach(function (pair) {
      var b = document.createElement("button");
      b.type = "button";
      b.textContent = pair[0];
      b.className = localDepth === pair[1] ? "active" : "";
      b.addEventListener("click", function () { setLocal(pair[1]); });
      tools.appendChild(b);
    });
    var cb = document.createElement("button");
    cb.type = "button";
    cb.textContent = "Centre";
    cb.addEventListener("click", function () { centreOn(i, 1.8); });
    tools.appendChild(cb);
    body.appendChild(tools);

    var qs = conceptQuestions(i);
    body.appendChild(sectionLabel(
      qs.length + (qs.length === 1 ? " Question" : " Questions") + " on this Concept"));
    var qwrap = document.createElement("div");
    qwrap.className = "qlist";
    for (var a = 0; a < qs.length; a++) {
      (function (qIdx) {
        var line = document.createElement("div");
        line.className = "qline";
        line.setAttribute("tabindex", "0");
        line.textContent = truncate(W.questions[G.qids[qIdx]].text, 110);
        var block = null;
        function toggle() {
          if (block) {
            block.parentNode.removeChild(block);
            block = null;
            line.style.display = "";
            line.classList.remove("open");
            return;
          }
          block = questionBlock(qIdx);
          block.querySelector(".qtitle").addEventListener("click", toggle);
          line.parentNode.insertBefore(block, line.nextSibling);
          line.style.display = "none";
          line.classList.add("open");
        }
        line.addEventListener("click", toggle);
        qwrap.appendChild(line);
      })(qs[a]);
    }
    body.appendChild(qwrap);

    var nb = [];
    for (var b2 = 0; b2 < gAdj[i].length; b2++) {
      var e = gAdj[i][b2];
      nb.push({ i: other(e, i), w: edgeWeight(e), e: e });
    }
    nb.sort(function (p, q) { return q.w - p.w || (G.labels[p.i] < G.labels[q.i] ? -1 : 1); });
    body.appendChild(sectionLabel(nb.length + " neighbours, by shared Questions"));
    var nwrap = document.createElement("div");
    nwrap.className = "nblist";
    for (var c = 0; c < nb.length; c++) {
      (function (row) {
        var ch = document.createElement("button");
        ch.type = "button";
        ch.className = "gchip";
        ch.textContent = G.labels[row.i];
        var w = document.createElement("span");
        w.className = "w";
        w.textContent = row.w;
        ch.appendChild(w);
        ch.addEventListener("click", function () {
          if (!inActive[row.i]) setLocal(0);
          pinNode(row.i, true);
          centreOn(row.i);
        });
        nwrap.appendChild(ch);
      })(nb[c]);
    }
    body.appendChild(nwrap);
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
        line.setAttribute("tabindex", "0");
        line.textContent = truncate(W.questions[G.qids[qIdx]].text, 110);
        var block = null;
        function toggle() {
          if (block) {
            block.parentNode.removeChild(block);
            block = null;
            line.style.display = "";
            return;
          }
          block = questionBlock(qIdx);
          block.querySelector(".qtitle").addEventListener("click", toggle);
          line.parentNode.insertBefore(block, line.nextSibling);
          line.style.display = "none";
        }
        line.addEventListener("click", toggle);
        wrap.appendChild(line);
      })(qs[i]);
    }
    body.appendChild(wrap);
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
    var hud = document.getElementById("graph-hud");
    var folded = hud.classList.contains("folded");
    var hd = document.createElement("div");
    hd.className = "hd";
    hd.textContent = folded
      ? "\u25b8 legend"
      : "\u25be " + (colorMode === "community"
          ? G.communities.length + " communities \u00b7 click a row to hide"
          : G.domains.length + " domains \u00b7 dominant Domain");
    hd.title = "Fold the legend away";
    hd.addEventListener("click", function () {
      hud.classList.toggle("folded");
      renderLegend();
      fitView();
    });
    el.appendChild(hd);
    if (folded) return;
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
        if (colorMode !== "community") {
          // The same short name the chips use; the legend is not the place
          // for a Domain's whole sentence either.
          t.textContent = domainName(row.id, row.text);
          d.title = row.text;
        } else if (row.islands) {
          t.textContent = row.size + " detached in " + G.stats.island_clusters +
            " clusters, " + (commOff[idx] ? "show" : "hide");
        } else {
          t.textContent = row.name + " (" + row.size + ")";
        }
        d.appendChild(t);
        if (colorMode === "community") {
          d.addEventListener("click", function () {
            commOff[idx] = !commOff[idx];
            applyCommunityFilter();
            renderLegend();
            // Switching the detached clusters on is a request to see them.
            if (row.islands) fitView();
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
    for (var h = 0; h < gHullLayer.childNodes.length; h++) {
      var node = gHullLayer.childNodes[h];
      node.style.display = commOff[+node.getAttribute("data-comm")] ? "none" : "block";
    }
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
    // Both halves count only what is on: hiding a community takes its lines
    // out of the total as well as out of the drawn count.
    var drawn = 0, held = 0;
    for (var b = 0; b < activeEdge.length; b++) {
      var e = activeEdge[b];
      if (commOff[G.comm[G.e_a[e]]] || commOff[G.comm[G.e_b[e]]]) continue;
      held++;
      if (localDepth || G.backbone[e]) drawn++;
    }
    document.getElementById("stat").textContent =
      (activeNode.length - hiddenNodes) + " Concepts, " + drawn + " of " +
      held + " edges drawn" +
      (localDepth ? " · local depth " + localDepth : "") +
      " · layout " + layoutMs + " ms";
  }

  function graphNote() {
    return "Concept graph — " + G.stats.nodes + " canonical Concepts, " +
      G.stats.edges + " edges. An edge holds every Question touching both its " +
      "Concepts; thickness and brightness are that count (heaviest here: " +
      G.stats.max_weight + "). The opening frame draws the backbone -- every " +
      "edge of two Questions or more, each Concept's two strongest, and the " +
      "strongest crossings of every community pair -- and the rest come back " +
      "on a hover, on a pin, and in full in a local view. Colour is community, " +
      "found by Louvain on the weighted graph; the " + G.stats.island_clusters +
      " clusters with no line to the rest start off the frame and their legend " +
      "row switches them on. The Colour button recolours by the Domain most of " +
      "a Concept's Questions are live in. " +
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
    // The 125 detached clusters ring the body and squeezed it into a third of
    // the canvas. They leave the opening frame; their legend row switches
    // them back on and refits (team-lead, 2026-09-30, from the cold review).
    if (G.islands_comm !== null) commOff[G.islands_comm] = true;
    var t0 = (window.performance && performance.now) ? performance.now() : Date.now();
    layoutTwoLevel(activeNode, activeEdge);
    var t1 = (window.performance && performance.now) ? performance.now() : Date.now();
    layoutMs = Math.round(t1 - t0);
    buildScene();
    applyCommunityFilter();
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
    window.__gym.fit = function () { fitView(); };
    window.__gym.zoom = function (f) {
      vk = Math.max(0.05, Math.min(12, vk * f));
      viewIsFitted = false;
      applyTransform();
    };
    // The visible Concept furthest to the right: the one whose label the side
    // panel used to cut in half.
    window.__gym.rightmost = function () {
      var best = -1, bestX = -Infinity;
      for (var a = 0; a < activeNode.length; a++) {
        var i = activeNode[a];
        if (commOff[G.comm[i]]) continue;
        var x = gx[i] * vk + vx;
        if (x > bestX) { bestX = x; best = i; }
      }
      return best < 0 ? null : G.ids[best];
    };
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
    // The longest drawn line, which is the one with room to be clicked
    // between its two labels.
    // Where the detached clusters sit relative to the connected body.
    window.__gym.islandBand = function () {
      var bb = { minx: Infinity, maxx: -Infinity, maxy: -Infinity };
      var band = { minx: Infinity, maxx: -Infinity, miny: Infinity };
      for (var i = 0; i < GN; i++) {
        if (G.comm[i] === G.islands_comm) {
          band.minx = Math.min(band.minx, gx[i]);
          band.maxx = Math.max(band.maxx, gx[i]);
          band.miny = Math.min(band.miny, gy[i]);
        } else {
          bb.minx = Math.min(bb.minx, gx[i]);
          bb.maxx = Math.max(bb.maxx, gx[i]);
          bb.maxy = Math.max(bb.maxy, gy[i]);
        }
      }
      return {
        bodyBottom: Math.round(bb.maxy),
        bodyWidth: Math.round(bb.maxx - bb.minx),
        bandTop: Math.round(band.miny),
        bandWidth: Math.round(band.maxx - band.minx)
      };
    };
    window.__gym.longestEdge = function () {
      var best = -1, bestL = -1;
      for (var e = 0; e < GE; e++) {
        if (!G.backbone[e]) continue;
        var a = G.e_a[e], b = G.e_b[e];
        var dx = gx[a] - gx[b], dy = gy[a] - gy[b];
        var L = dx * dx + dy * dy;
        if (L > bestL) { bestL = L; best = e; }
      }
      return best;
    };
    window.__gym.heaviestEdge = function () {
      var best = -1;
      for (var e = 0; e < GE; e++) {
        if (!G.backbone[e]) continue;
        if (best < 0 || edgeWeight(e) > edgeWeight(best)) best = e;
      }
      return best;
    };
    window.__gym.centreOnEdge = function (e, zoom) {
      var r = gsvg.getBoundingClientRect();
      vk = zoom || 2;
      vx = r.width / 2 - ((gx[G.e_a[e]] + gx[G.e_b[e]]) / 2) * vk;
      vy = r.height / 2 - ((gy[G.e_a[e]] + gy[G.e_b[e]]) / 2) * vk;
      applyTransform();
    };
    // t picks a point along the drawn line; a caller scans it because a
    // Concept's label can sit over the middle of a line and take the click,
    // which is the price of a label being its Concept.
    window.__gym.edgeScreen = function (e, t) {
      var r = gsvg.getBoundingClientRect();
      var mid = edgePointAt(e, t === undefined ? 0.5 : t);
      return {
        x: r.left + mid.x * vk + vx,
        y: r.top + mid.y * vk + vy,
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
  document.getElementById("btn-fit").addEventListener("click", function () { fitView(); });

  // --- keyboard -----------------------------------------------------------
  // "/" jumps to the search box, the arrows walk the neighbour list in the
  // panel and Enter opens the one under the cursor, so a Concept can be
  // walked without the mouse. Escape steps back, as it already did.
  var kbdIndex = -1;

  function kbdChips() {
    return Array.prototype.slice.call(
      document.querySelectorAll("#panel-body .nblist .gchip"));
  }

  function moveKbd(delta) {
    var chips = kbdChips();
    if (!chips.length) return false;
    for (var i = 0; i < chips.length; i++) chips[i].classList.remove("kbd");
    kbdIndex = kbdIndex < 0
      ? (delta > 0 ? 0 : chips.length - 1)
      : (kbdIndex + delta + chips.length) % chips.length;
    var el = chips[kbdIndex];
    el.classList.add("kbd");
    el.scrollIntoView({ block: "nearest" });
    return true;
  }

  function typingInField(ev) {
    var t = ev.target;
    return t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA" || t.isContentEditable);
  }

  document.addEventListener("keydown", function (ev) {
    if (currentView !== "graph") return;
    if (ev.key === "/" && !typingInField(ev)) {
      ev.preventDefault();
      // The search box folds away with the legend, so "/" brings both back.
      var hud = document.getElementById("graph-hud");
      if (hud.classList.contains("folded")) {
        hud.classList.remove("folded");
        renderLegend();
        fitView();
      }
      var box = document.getElementById("gsearch");
      box.focus();
      box.select();
      return;
    }
    if (typingInField(ev)) return;
    if (ev.key === "ArrowDown" || ev.key === "ArrowUp") {
      if (moveKbd(ev.key === "ArrowDown" ? 1 : -1)) ev.preventDefault();
      return;
    }
    if (ev.key === "Enter" && kbdIndex >= 0) {
      var chips = kbdChips();
      if (chips[kbdIndex]) { ev.preventDefault(); chips[kbdIndex].click(); }
    }
  });

  document.addEventListener("keydown", function (ev) {
    if (ev.key !== "Escape" || currentView !== "graph") return;
    var box = document.getElementById("gsearch");
    if (document.activeElement === box) { box.blur(); return; }
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
