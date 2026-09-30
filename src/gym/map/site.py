"""Generate the reorderable-matrix site for a Rust-opinion-map-shaped map.

Moved from the disposable prototype at
docs/orchestration_log/recon/2026-09-30/frontend/proto/build.py (see NOTES.md
there for the full derivation writeup: cell/latest/changed/checked rules,
color index, seriation, defaults, data problems, open questions). Page
behaviour and derivation are unchanged from the prototype; only the map
directory and output path are now parameters instead of hardcoded.
"""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import date
from pathlib import Path

import yaml

PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#7B3F61"]


def load_kind(map_dir: Path, name: str) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for f in sorted((map_dir / name).glob("*.yaml")):
        out[f.stem] = yaml.safe_load(f.read_text()) or {}
    return out


def build_graph_data(
    questions: dict[str, dict],
    positions: dict[str, dict],
    arguments: dict[str, dict],
    concepts: dict[str, dict],
    domains: dict[str, dict],
    values: dict[str, dict],
) -> dict:
    """Graph view's node/edge set.

    Edges drawn only where the files hold them: Question-Concept
    (question.concepts), Question-Domain (question.domains),
    Question-Value (a Question appeals to a Value when any Argument on any
    of its Positions appeals to it; weight = count of such Arguments), and
    Concept-Concept (concept.related) -- 0 today, never inferred from
    co-occurrence. Node id is "{kind}:{raw_id}" to keep the four id spaces
    from colliding; "raw" is kept per node for jumping to a Matrix row.
    """

    def nid(kind: str, raw: str) -> str:
        return f"{kind}:{raw}"

    edges: list[dict] = []
    degree: dict[str, float] = defaultdict(float)

    def add_edge(kind: str, a: str, b: str, weight: float = 1.0) -> None:
        edges.append({"kind": kind, "source": a, "target": b, "weight": weight})
        degree[a] += weight
        degree[b] += weight

    for qid, q in questions.items():
        qn = nid("question", qid)
        for cid in q.get("concepts") or []:
            if cid in concepts:
                add_edge("question-concept", qn, nid("concept", cid))
        for did in q.get("domains") or []:
            if did in domains:
                add_edge("question-domain", qn, nid("domain", did))

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
        add_edge("question-value", nid("question", qid), nid("value", vid), float(w))

    concept_concept_edges = 0
    for cid, c in concepts.items():
        for rid in c.get("related") or []:
            if rid in concepts:
                add_edge("concept-concept", nid("concept", cid), nid("concept", rid))
                concept_concept_edges += 1

    nodes: dict[str, dict] = {}
    for kind, table, text_field in (
        ("question", questions, "text"),
        ("concept", concepts, "text"),
        ("domain", domains, "text"),
        ("value", values, "text"),
    ):
        for raw_id, item in table.items():
            n = nid(kind, raw_id)
            if degree.get(n, 0) <= 0:
                continue
            nodes[n] = {
                "id": n,
                "kind": kind,
                "raw": raw_id,
                "label": item.get(text_field) or raw_id,
                "degree": degree[n],
            }

    concept_ids_by_degree = sorted(
        (n["raw"] for n in nodes.values() if n["kind"] == "concept" and n["degree"] >= 3)
    )
    default_concepts = set(nid("concept", cid) for cid in concept_ids_by_degree)
    default_nodes = set(default_concepts)
    for e in edges:
        if e["source"] in default_concepts:
            default_nodes.add(e["target"])
        if e["target"] in default_concepts:
            default_nodes.add(e["source"])

    return {
        "nodes": list(nodes.values()),
        "edges": edges,
        "concept_concept_count": concept_concept_edges,
        "default_subset": sorted(default_nodes),
        "counts": {
            "nodes_full": len(nodes),
            "nodes_default": len(default_nodes),
            "edges_full": len(edges),
        },
    }


def main(map_dir: Path, out: Path) -> None:
    questions = load_kind(map_dir, "questions")
    positions = load_kind(map_dir, "positions")
    claims = load_kind(map_dir, "claims")
    voices = load_kind(map_dir, "voices")
    sources = load_kind(map_dir, "sources")
    arguments = load_kind(map_dir, "arguments")
    values = load_kind(map_dir, "values")
    concepts = load_kind(map_dir, "concepts")
    domains = load_kind(map_dir, "domains")

    problems: dict[str, int] = defaultdict(int)

    # --- group claims by (question, voice) ---
    groups: dict[tuple[str, str], list[str]] = defaultdict(list)
    for cid, c in claims.items():
        pid = c.get("position")
        if pid == "unresolved":
            problems["claims_unresolved_position"] += 1
            continue
        pos = positions.get(pid)
        if pos is None:
            problems["claims_position_not_found"] += 1
            continue
        vid = c.get("voice")
        if vid not in voices:
            problems["claims_voice_not_found"] += 1
            continue
        qid = pos.get("question")
        if qid not in questions:
            problems["claims_question_not_found"] += 1
            continue
        groups[(qid, vid)].append(cid)

    # --- resolve the winning (latest) claim per cell ---
    matrix_cells: list[dict] = []
    question_positions_used: dict[str, set[str]] = defaultdict(set)
    question_voices: dict[str, set[str]] = defaultdict(set)
    undated_picks = 0
    mixed_dated_undated = 0

    for (qid, vid), cids in groups.items():
        dated = [c for c in cids if claims[c].get("date")]
        undated = [c for c in cids if not claims[c].get("date")]
        if dated:
            dated_sorted = sorted(dated, key=lambda c: (claims[c]["date"], c))
            chosen = dated_sorted[-1]
            distinct_positions = {claims[c]["position"] for c in dated}
            changed = len(distinct_positions) > 1
            history = [
                {"claim": c, "position": claims[c]["position"], "date": claims[c]["date"]}
                for c in dated_sorted
            ]
            if undated:
                mixed_dated_undated += 1
                history.extend(
                    {"claim": c, "position": claims[c]["position"], "date": None}
                    for c in sorted(undated)
                )
        else:
            chosen = sorted(cids)[0]
            changed = False
            history = [
                {"claim": c, "position": claims[c]["position"], "date": None}
                for c in sorted(cids)
            ]
            undated_picks += 1

        pid = claims[chosen]["position"]
        question_positions_used[qid].add(pid)
        question_voices[qid].add(vid)
        matrix_cells.append(
            {
                "q": qid,
                "v": vid,
                "position": pid,
                "claim": chosen,
                "changed": changed,
                "dated": bool(claims[chosen].get("date")),
                "history": history if len(cids) > 1 else None,
            }
        )

    # --- color index: positions actually chosen for a question, ranked by position id.
    # N>6 no longer clamps to 6 (info loss: 2+ genuinely different Positions
    # shared a color). Position 7 keeps color 7 ("overflow", one shared bucket
    # for every position past the 6th); positions 8+ still land in that same
    # bucket, since the palette only carries one overflow color.
    overflow_questions = 0
    color_index: dict[tuple[str, str], int] = {}
    for qid, pids in question_positions_used.items():
        ordered = sorted(pids)
        if len(ordered) > 6:
            overflow_questions += 1
        for i, pid in enumerate(ordered):
            color_index[(qid, pid)] = min(i + 1, 7)

    for cell in matrix_cells:
        cell["color"] = color_index[(cell["q"], cell["position"])]
        cell["checked"] = "checked" in claims[cell["claim"]]

    # --- default subset: iterate the two filters to a fixed point (a bipartite
    # 2-core): a literal single pass (the prototype's reading) can leave a
    # question in the subset whose only qualifying voices get filtered out by
    # the voice-side rule, or a voice whose only qualifying questions get
    # dropped by the question-side rule. Repeat both filters, each time
    # restricted to the survivors of the other side, until neither set moves.
    all_questions = set(question_voices)
    all_voices = {vid for cells in question_voices.values() for vid in cells}
    cur_questions, cur_voices = all_questions, all_voices
    while True:
        q_voices_live: dict[str, set[str]] = defaultdict(set)
        q_positions_live: dict[str, set[str]] = defaultdict(set)
        for cell in matrix_cells:
            if cell["v"] in cur_voices:
                q_voices_live[cell["q"]].add(cell["v"])
                q_positions_live[cell["q"]].add(cell["position"])
        next_questions = {
            qid
            for qid in cur_questions
            if len(q_voices_live.get(qid, ())) >= 2 and len(q_positions_live.get(qid, ())) >= 2
        }
        v_questions_live: dict[str, set[str]] = defaultdict(set)
        for cell in matrix_cells:
            if cell["q"] in next_questions:
                v_questions_live[cell["v"]].add(cell["q"])
        next_voices = {
            vid for vid in cur_voices if len(v_questions_live.get(vid, ())) >= 2
        }
        if next_questions == cur_questions and next_voices == cur_voices:
            break
        cur_questions, cur_voices = next_questions, next_voices

    candidate_questions, candidate_voices = cur_questions, cur_voices
    default_cells = [
        cell
        for cell in matrix_cells
        if cell["q"] in candidate_questions and cell["v"] in candidate_voices
    ]

    # --- claims payload: only claims actually referenced (chosen + history) ---
    referenced_claims: set[str] = set()
    for cell in matrix_cells:
        referenced_claims.add(cell["claim"])
        if cell["history"]:
            referenced_claims.update(h["claim"] for h in cell["history"])

    claims_payload = {}
    for cid in referenced_claims:
        c = claims[cid]
        src = sources.get(c.get("source"))
        if src is None:
            problems["claims_source_not_found"] += 1
            src = {}
        claims_payload[cid] = {
            "paraphrase": c.get("paraphrase"),
            "quote": c.get("quote"),
            "date": c.get("date"),
            "checked": c.get("checked"),
            "source": {"title": src.get("title"), "url": src.get("url")},
        }

    # --- positions payload: ALL positions (row click shows the whole Question) ---
    args_by_position: dict[str, list[str]] = defaultdict(list)
    for aid, a in arguments.items():
        args_by_position[a.get("position")].append(aid)

    positions_payload = {}
    for pid, p in positions.items():
        arg_list = []
        for aid in sorted(args_by_position.get(pid, [])):
            a = arguments[aid]
            vals = [values[v]["text"] for v in a.get("values", []) if v in values]
            arg_list.append({"side": a.get("side"), "text": a.get("text"), "values": vals})
        positions_payload[pid] = {
            "question": p.get("question"),
            "summary": p.get("summary"),
            "tag": p.get("tag"),
            "arguments": arg_list,
        }

    questions_payload = {}
    for qid, q in questions.items():
        pids = sorted(pid for pid, p in positions.items() if p.get("question") == qid)
        questions_payload[qid] = {"text": q.get("text"), "positions": pids}

    voices_payload = {vid: {"name": v.get("name") or vid} for vid, v in voices.items()}

    checked_count = sum(1 for c in claims.values() if "checked" in c)

    graph = build_graph_data(questions, positions, arguments, concepts, domains, values)

    data = {
        "meta": {
            "subject": "rust",
            "generated": date.today().isoformat(),
            "counts": {
                "questions": len(questions),
                "positions": len(positions),
                "claims": len(claims),
                "voices": len(voices),
                "sources": len(sources),
                "arguments": len(arguments),
            },
            "cells_total": len(matrix_cells),
            "default": {
                "questions": len(candidate_questions),
                "voices": len(candidate_voices),
                "cells": len(default_cells),
            },
            "problems": dict(problems),
            "undated_picks": undated_picks,
            "mixed_dated_undated": mixed_dated_undated,
            "overflow_questions": overflow_questions,
            "seriation": (
                "greedy nearest-neighbour, single deterministic pass per axis; "
                "columns (Voices) rank by color-index agreement with the last-"
                "placed Voice; rows (Questions) rank by shared-Voice count with "
                "the last-placed Question first, ties broken by that same "
                "color-index agreement"
            ),
            "checked_rule": (
                f"claim.checked present ({checked_count}/{len(claims)}) = checked "
                "(panel shows its date and verdict, confirmed or corrected, "
                "against Source); absent = provisional"
            ),
            "latest_rule": (
                "per (question,voice): among dated claims, max date wins, ties by "
                "claim id; if a group has zero dated claims, the lexicographically "
                "first claim id is the deterministic pick, flagged undated"
            ),
            "color_rule": (
                "positions actually chosen for a question, sorted by position id, "
                "numbered 1..N; N>6 gets a 7th shared 'overflow' color instead of "
                "clamping into an existing one"
            ),
            "default_subset_rule": (
                "candidate questions: >=2 voices holding a claim on it and >=2 "
                "distinct positions held, both counted only over surviving "
                "voices; candidate voices: hold a claim on >=2 surviving "
                "candidate questions; iterated to a fixed point (2-core), not a "
                "single pass"
            ),
        },
        "palette": PALETTE,
        "questions": questions_payload,
        "voices": voices_payload,
        "positions": positions_payload,
        "claims": claims_payload,
        "matrix": matrix_cells,
        "default_subset": {
            "questions": sorted(candidate_questions),
            "voices": sorted(candidate_voices),
        },
        "graph": graph,
    }

    json_text = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = HTML_TEMPLATE.replace("__DATA_JSON__", json_text)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")

    print("counts:", data["meta"]["counts"])
    print("problems:", dict(problems))
    print("undated_picks:", undated_picks, "mixed_dated_undated:", mixed_dated_undated)
    print("overflow_questions (>6 positions held):", overflow_questions)
    print("total matrix cells (all):", len(matrix_cells))
    print(
        "default subset: questions=%d voices=%d cells=%d"
        % (len(candidate_questions), len(candidate_voices), len(default_cells))
    )
    print(
        "graph: nodes_full=%d nodes_default=%d edges_full=%d concept_concept_edges=%d"
        % (
            graph["counts"]["nodes_full"],
            graph["counts"]["nodes_default"],
            graph["counts"]["edges_full"],
            graph["concept_concept_count"],
        )
    )
    print("wrote", out)


HTML_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Rust opinion map</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {
    --bg: #f7f6f3;
    --panel-bg: #ffffff;
    --ink: #1c1b1a;
    --ink-dim: #6b6560;
    --border: #d8d3cb;
    --accent: #1c1b1a;
    --grey-none: #dedad3;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; background: var(--bg); color: var(--ink);
    font: 14px/1.4 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
  header { padding: 10px 16px; border-bottom: 1px solid var(--border); background: var(--panel-bg);
    display: flex; flex-wrap: wrap; align-items: center; gap: 14px; }
  header h1 { font-size: 15px; margin: 0; font-weight: 600; }
  header .stat { font-size: 12px; color: var(--ink-dim); }
  button { font: inherit; padding: 5px 11px; border: 1px solid var(--border); background: var(--panel-bg);
    color: var(--ink); border-radius: 4px; cursor: pointer; }
  button:hover { background: #efece6; }
  button.active { background: var(--ink); color: #fff; border-color: var(--ink); }
  #legend { display: flex; align-items: center; gap: 6px; font-size: 12px; color: var(--ink-dim); }
  #legend .sw { width: 11px; height: 11px; display: inline-block; border-radius: 2px; border: 1px solid rgba(0,0,0,.15); }
  #note { padding: 6px 16px; font-size: 11.5px; color: var(--ink-dim); border-bottom: 1px solid var(--border); background: #f1efe9; }
  #wrap { display: flex; height: calc(100vh - 78px); }
  #gridwrap { flex: 1 1 auto; overflow: auto; padding: 18px; }
  svg#matrix { display: block; }
  .hit { fill: transparent; cursor: pointer; }
  .hit:hover { fill: rgba(0,0,0,0.045); }
  .cell { stroke: #ffffff; stroke-width: 1; cursor: pointer; }
  .cell.provisional { stroke-dasharray: 2,2; stroke: #8a8378; }
  .cell.changed-marker { fill: #1c1b1a; }
  .cell.undated-marker { fill: none; stroke: #ffffff; stroke-width: 1.1; }
  text.lbl { fill: var(--ink); font-size: 11px; cursor: pointer; user-select: none; }
  text.lbl:hover { fill: #000; text-decoration: underline; }
  text.lbl.dragging { opacity: 0.4; }
  #panel { width: 380px; flex: 0 0 380px; border-left: 1px solid var(--border); background: var(--panel-bg);
    overflow-y: auto; padding: 16px; display: none; }
  #panel.open { display: block; }
  #panel h2 { font-size: 14px; margin: 0 0 6px; }
  #panel .close { float: right; cursor: pointer; color: var(--ink-dim); border: none; background: none; font-size: 16px; }
  #panel .q-context { font-size: 12px; color: var(--ink-dim); margin-bottom: 10px; }
  #panel .badge { display: inline-block; font-size: 10.5px; padding: 1px 7px; border-radius: 10px;
    border: 1px solid var(--border); margin-right: 4px; }
  #panel .badge.checked { background: #e4f3e9; border-color: #9cc9ac; }
  #panel .badge.provisional { background: #f3ece4; border-color: #cbb290; }
  #panel .badge.undated { background: #eeeeee; border-color: #b9b9b9; }
  #panel .badge.voice-chip { cursor: pointer; }
  #panel .badge.voice-chip:hover { background: #efece6; }
  #panel .badge.tag-fact { background: #e4edf3; }
  #panel .badge.tag-tradeoff { background: #f3ecf9; }
  #panel .badge.tag-taste { background: #f9f3e4; }
  #panel blockquote { margin: 8px 0; padding: 6px 10px; border-left: 3px solid var(--border);
    font-style: italic; color: #4a453f; }
  #panel .field { margin: 9px 0; }
  #panel .field .k { font-size: 10.5px; text-transform: uppercase; letter-spacing: .04em; color: var(--ink-dim); }
  #panel a { color: #1a5fb4; }
  #panel .pos-block { border: 1px solid var(--border); border-radius: 6px; padding: 8px 10px; margin: 10px 0; }
  #panel .arg { margin: 6px 0 6px 4px; padding-left: 8px; border-left: 2px solid #e3ded4; font-size: 12.5px; }
  #panel .arg .side-for { color: #2a7a3f; font-weight: 600; }
  #panel .arg .side-against { color: #a13a2f; font-weight: 600; }
  #panel .hist-item { font-size: 12px; margin: 3px 0; color: var(--ink-dim); }
  #empty-hint { padding: 40px; color: var(--ink-dim); font-size: 13px; }
  #view-switch button.active { background: var(--ink); color: #fff; border-color: var(--ink); }
  #graphwrap { flex: 1 1 auto; overflow: hidden; padding: 0; position: relative; }
  svg#graph { display: block; width: 100%; height: 100%; }
  .gedge { stroke: #b9b2a6; stroke-opacity: .55; }
  .gedge.kind-concept-concept { stroke: #a13a2f; stroke-opacity: .8; }
  .gnode { cursor: pointer; }
  .gnode .shape { stroke: #ffffff; stroke-width: 1; }
  .gnode.kind-question .shape { fill: #56B4E9; }
  .gnode.kind-concept .shape { fill: #E69F00; }
  .gnode.kind-domain .shape { fill: #009E73; }
  .gnode.kind-value .shape { fill: #D55E00; }
  .gnode.pulse .shape { stroke: #1c1b1a; stroke-width: 3; }
  .gnode .glabel { font-size: 10px; fill: var(--ink); pointer-events: none; display: none; }
  .gnode.kind-domain .glabel, .gnode.kind-value .glabel { display: block; }
  .gnode.revealed .glabel, .gnode:hover .glabel { display: block; }
  #panel .nbr-chip { margin: 2px 3px 2px 0; display: inline-block; }
  text.lbl.pulse-row { fill: #a13a2f; font-weight: 700; }
</style>
</head>
<body>
<header>
  <h1>Rust opinion map</h1>
  <span id="view-switch">
    <button id="btn-view-matrix" class="active">Matrix</button>
    <button id="btn-view-graph">Graph</button>
  </span>
  <span id="matrix-controls">
    <button id="btn-scope">Default subset</button>
    <button id="btn-reorder">Reorder (seriate)</button>
  </span>
  <span id="graph-controls" style="display:none">
    <button id="btn-graph-scope">Show all</button>
  </span>
  <span class="stat" id="stat"></span>
  <span id="legend"></span>
</header>
<div id="note"></div>
<div id="wrap">
  <div id="gridwrap"><svg id="matrix" xmlns="http://www.w3.org/2000/svg"></svg></div>
  <div id="graphwrap" style="display:none"><svg id="graph" xmlns="http://www.w3.org/2000/svg"></svg></div>
  <div id="panel"><button class="close" id="panel-close">&times;</button><div id="panel-body"></div></div>
</div>
<script id="data" type="application/json">__DATA_JSON__</script>
<script>
(function () {
  "use strict";
  var DATA = JSON.parse(document.getElementById("data").textContent);
  var CELL = 18, LABEL_W = 320, HEAD_H = 170;
  var showAll = false;
  var rowOrder = [], colOrder = [];
  var revealed = {};
  var cellIndex = {};
  var voiceNumber = {};

  function key(q, v) { return q + "\u0001" + v; }

  function buildCellIndex() {
    cellIndex = {};
    for (var i = 0; i < DATA.matrix.length; i++) {
      var c = DATA.matrix[i];
      cellIndex[key(c.q, c.v)] = c;
    }
  }

  function currentQuestions() {
    return showAll ? Object.keys(DATA.questions).sort() : DATA.default_subset.questions.slice().sort();
  }
  function currentVoices() {
    return showAll ? Object.keys(DATA.voices).sort() : DATA.default_subset.voices.slice().sort();
  }

  function resetOrders() {
    rowOrder = currentQuestions();
    colOrder = currentVoices();
    // Anonymous Voice numbers are assigned once, here, from this initial
    // column order, and never recomputed by doReorder or a drag swap — so a
    // number stays with its Voice for the rest of this page load (or until
    // the subset itself changes, which is a fresh load of a different
    // column set).
    voiceNumber = {};
    for (var i = 0; i < colOrder.length; i++) voiceNumber[colOrder[i]] = i + 1;
  }

  function axisMaps(rows, cols) {
    var rowMap = {}, colMap = {};
    for (var i = 0; i < rows.length; i++) rowMap[rows[i]] = {};
    for (var j = 0; j < cols.length; j++) colMap[cols[j]] = {};
    for (var k = 0; k < DATA.matrix.length; k++) {
      var c = DATA.matrix[k];
      if (rowMap.hasOwnProperty(c.q) && colMap.hasOwnProperty(c.v)) {
        rowMap[c.q][c.v] = c.color;
        colMap[c.v][c.q] = c.color;
      }
    }
    return { rowMap: rowMap, colMap: colMap };
  }

  function mapSize(m) { var n = 0; for (var k in m) if (m.hasOwnProperty(k)) n++; return n; }

  // Color-index agreement: count of shared keys (opposite-axis items) where
  // both maps also hold the same color value. Used for column (Voice)
  // seriation, unchanged from the prototype, and as the row tie-break below.
  function similarity(mapA, mapB) {
    var small = mapA, large = mapB;
    if (mapSize(mapB) < mapSize(mapA)) { small = mapB; large = mapA; }
    var n = 0;
    for (var k in small) {
      if (small.hasOwnProperty(k) && large.hasOwnProperty(k) && large[k] === small[k]) n++;
    }
    return n;
  }

  // Shared-key count, ignoring color: number of Voices holding a Claim on
  // both Questions. Used as the primary row (Question) similarity, per the
  // owner's brief — color-index agreement is only a comparable ordinal
  // within one row's own arbitrary numbering, so it is a tie-break here, not
  // the primary signal.
  function overlap(mapA, mapB) {
    var small = mapA, large = mapB;
    if (mapSize(mapB) < mapSize(mapA)) { small = mapB; large = mapA; }
    var n = 0;
    for (var k in small) {
      if (small.hasOwnProperty(k) && large.hasOwnProperty(k)) n++;
    }
    return n;
  }

  function scoreOf(scoreFns, lastMap, candMap) {
    var out = [];
    for (var i = 0; i < scoreFns.length; i++) out.push(scoreFns[i](lastMap, candMap));
    return out;
  }

  // Lexicographic compare over a score tuple: true when `a` ranks strictly
  // ahead of `b` (first differing element wins).
  function scoreBetter(a, b) {
    for (var i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) return a[i] > b[i];
    }
    return false;
  }
  function scoreEqual(a, b) {
    for (var i = 0; i < a.length; i++) if (a[i] !== b[i]) return false;
    return true;
  }

  function greedySeriate(ids, dataMaps, scoreFns) {
    if (ids.length <= 1) return ids.slice();
    var sorted = ids.slice().sort(function (a, b) {
      var da = mapSize(dataMaps[a]), db = mapSize(dataMaps[b]);
      if (db !== da) return db - da;
      return a < b ? -1 : (a > b ? 1 : 0);
    });
    var seed = sorted[0];
    var remaining = {};
    for (var i = 0; i < ids.length; i++) remaining[ids[i]] = true;
    delete remaining[seed];
    var order = [seed];
    while (true) {
      var remKeys = Object.keys(remaining);
      if (remKeys.length === 0) break;
      var last = order[order.length - 1];
      var lastMap = dataMaps[last];
      var best = null, bestScore = null;
      for (var r = 0; r < remKeys.length; r++) {
        var cand = remKeys[r];
        var score = scoreOf(scoreFns, lastMap, dataMaps[cand]);
        if (bestScore === null || scoreBetter(score, bestScore) ||
            (scoreEqual(score, bestScore) && cand < best)) {
          bestScore = score; best = cand;
        }
      }
      order.push(best);
      delete remaining[best];
    }
    return order;
  }

  function doReorder() {
    var maps = axisMaps(rowOrder, colOrder);
    // Rows (Questions): primary = shared-Voice count; ties by color-index
    // agreement (Open question #2 in the prototype notes, now resolved).
    rowOrder = greedySeriate(rowOrder, maps.rowMap, [overlap, similarity]);
    // Columns (Voices): color-index agreement alone, as in the prototype.
    colOrder = greedySeriate(colOrder, maps.colMap, [similarity]);
    render();
  }

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

  function voiceLabel(vid) {
    if (revealed[vid]) return DATA.voices[vid].name;
    return "Voice " + (voiceNumber.hasOwnProperty(vid) ? voiceNumber[vid] : "?");
  }

  function showClaimPanel(qid, vid) {
    var c = cellIndex[key(qid, vid)];
    var body = document.getElementById("panel-body");
    body.innerHTML = "";
    var h = document.createElement("h2");
    h.textContent = "Claim";
    body.appendChild(h);
    var ctx = document.createElement("div");
    ctx.className = "q-context";
    ctx.textContent = DATA.questions[qid].text;
    body.appendChild(ctx);

    if (!c) {
      var empty = document.createElement("div");
      empty.className = "q-context";
      empty.textContent = voiceLabel(vid) + " holds no Claim on this Question.";
      body.appendChild(empty);
      openPanel();
      return;
    }
    var claim = DATA.claims[c.claim];
    var pos = DATA.positions[c.position];

    var isChecked = !!claim.checked;
    var badges = document.createElement("div");
    badges.appendChild(badge(voiceLabel(vid), ""));
    badges.appendChild(badge(isChecked ? "checked" : "provisional", isChecked ? "checked" : "provisional"));
    if (!c.dated) badges.appendChild(badge("undated pick", "undated"));
    if (pos.tag) badges.appendChild(badge(pos.tag, "tag-" + pos.tag));
    if (c.changed) badges.appendChild(badge("changed position", ""));
    body.appendChild(badges);

    body.appendChild(field("Position", pos.summary));
    body.appendChild(field("Paraphrase", claim.paraphrase || ""));
    if (claim.quote) {
      var bq = document.createElement("blockquote");
      bq.textContent = claim.quote;
      body.appendChild(field("Quote", bq));
    }
    var srcNode = document.createElement("div");
    if (claim.source && claim.source.url) {
      var a = document.createElement("a");
      a.href = claim.source.url; a.target = "_blank"; a.rel = "noopener";
      a.textContent = claim.source.title || claim.source.url;
      srcNode.appendChild(a);
    } else {
      srcNode.textContent = "(no source on file)";
    }
    body.appendChild(field("Source", srcNode));
    body.appendChild(field("Date", claim.date || "unknown (undated pick)"));
    if (isChecked) {
      body.appendChild(field(
        "Checked",
        claim.checked.date + " — " + claim.checked.verdict + " (" + claim.checked.method + ")"
      ));
    }

    var others = [];
    for (var oi = 0; oi < DATA.matrix.length; oi++) {
      var oc = DATA.matrix[oi];
      if (oc.q === qid && oc.v !== vid && oc.position === c.position) others.push(oc.v);
    }
    others.sort();
    if (others.length) {
      var othersWrap = document.createElement("div");
      others.forEach(function (ovid) {
        var chip = badge(voiceLabel(ovid), "voice-chip");
        chip.addEventListener("click", function () {
          revealed[ovid] = !revealed[ovid];
          showClaimPanel(qid, vid);
          render();
        });
        othersWrap.appendChild(chip);
      });
      body.appendChild(field(
        "Other Voices holding this Position on this Question (" + others.length + ")",
        othersWrap
      ));
    }

    if (c.history && c.history.length > 1) {
      var histWrap = document.createElement("div");
      for (var i = 0; i < c.history.length; i++) {
        var hcid = c.history[i].claim;
        var hpos = DATA.positions[c.history[i].position];
        var hline = document.createElement("div");
        hline.className = "hist-item";
        hline.textContent = (c.history[i].date || "undated") + " — " + hpos.summary.slice(0, 90);
        histWrap.appendChild(hline);
      }
      body.appendChild(field("Full history at this cell (" + c.history.length + " claims)", histWrap));
    }
    openPanel();
  }

  function showQuestionPanel(qid) {
    var q = DATA.questions[qid];
    var body = document.getElementById("panel-body");
    body.innerHTML = "";
    var h = document.createElement("h2");
    h.textContent = "Question";
    body.appendChild(h);
    var ctx = document.createElement("div");
    ctx.className = "q-context";
    ctx.textContent = q.text;
    body.appendChild(ctx);

    for (var i = 0; i < q.positions.length; i++) {
      var pid = q.positions[i];
      var p = DATA.positions[pid];
      var block = document.createElement("div");
      block.className = "pos-block";
      var tagB = badge(p.tag ? p.tag : "untagged", p.tag ? "tag-" + p.tag : "");
      block.appendChild(tagB);
      var sum = document.createElement("div");
      sum.style.marginTop = "5px";
      sum.textContent = p.summary;
      block.appendChild(sum);
      for (var j = 0; j < p.arguments.length; j++) {
        var arg = p.arguments[j];
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
          for (var vi = 0; vi < arg.values.length; vi++) {
            vv.appendChild(badge(arg.values[vi], ""));
          }
          ad.appendChild(vv);
        }
        block.appendChild(ad);
      }
      if (p.arguments.length === 0) {
        var none = document.createElement("div");
        none.className = "q-context";
        none.textContent = "No Arguments compiled yet for this Position.";
        block.appendChild(none);
      }
      body.appendChild(block);
    }
    openPanel();
  }

  function attachDrag(el, axis, id) {
    var startX, startY, dragging = false;
    el.addEventListener("pointerdown", function (ev) {
      startX = ev.clientX; startY = ev.clientY; dragging = false;
      try { el.setPointerCapture && el.setPointerCapture(ev.pointerId); } catch (e) { /* no active pointer to capture; window-level listeners still track the gesture */ }
      function onMove(mev) {
        if (!dragging && (Math.abs(mev.clientX - startX) > 6 || Math.abs(mev.clientY - startY) > 6)) {
          dragging = true;
          el.classList.add("dragging");
        }
      }
      function onUp(uev) {
        window.removeEventListener("pointermove", onMove);
        window.removeEventListener("pointerup", onUp);
        el.classList.remove("dragging");
        if (dragging) {
          var target = document.elementFromPoint(uev.clientX, uev.clientY);
          while (target && !target.getAttribute) target = target.parentNode;
          if (target && target.getAttribute("data-axis") === axis) {
            var otherId = target.getAttribute("data-id");
            if (otherId && otherId !== id) {
              var order = axis === "row" ? rowOrder : colOrder;
              var from = order.indexOf(id);
              var to = order.indexOf(otherId);
              if (from >= 0 && to >= 0) {
                order.splice(from, 1);
                order.splice(to, 0, id);
                render();
              }
            }
          }
        } else {
          if (axis === "row") showQuestionPanel(id);
          else {
            revealed[id] = !revealed[id];
            render();
          }
        }
      }
      window.addEventListener("pointermove", onMove);
      window.addEventListener("pointerup", onUp);
    });
  }

  function render() {
    buildCellIndex();
    var svg = document.getElementById("matrix");
    svg.innerHTML = "";
    var w = LABEL_W + colOrder.length * CELL + 20;
    var h = HEAD_H + rowOrder.length * CELL + 20;
    svg.setAttribute("width", w);
    svg.setAttribute("height", h);
    svg.setAttribute("viewBox", "0 0 " + w + " " + h);

    if (rowOrder.length === 0 || colOrder.length === 0) {
      var t = svgEl("text", { x: 20, y: 40, class: "lbl" });
      t.textContent = "Empty subset.";
      svg.appendChild(t);
      return;
    }

    // background = "no claim" colour for the whole grid
    svg.appendChild(svgEl("rect", {
      x: LABEL_W, y: HEAD_H, width: colOrder.length * CELL, height: rowOrder.length * CELL,
      fill: "#dedad3"
    }));

    // column headers (rotated) + drag/click hit area
    for (var ci = 0; ci < colOrder.length; ci++) {
      var vid = colOrder[ci];
      var x = LABEL_W + ci * CELL + CELL / 2;
      var hit = svgEl("rect", {
        x: LABEL_W + ci * CELL, y: 0, width: CELL, height: HEAD_H,
        class: "hit", "data-axis": "col", "data-id": vid
      });
      svg.appendChild(hit);
      var txt = svgEl("text", {
        x: x, y: HEAD_H - 6, class: "lbl", "data-axis": "col", "data-id": vid,
        transform: "rotate(-55 " + x + " " + (HEAD_H - 6) + ")"
      });
      txt.textContent = voiceLabel(vid);
      svg.appendChild(txt);
      attachDrag(txt, "col", vid);
      attachDrag(hit, "col", vid);
    }

    // row headers + hit area
    for (var ri = 0; ri < rowOrder.length; ri++) {
      var qid = rowOrder[ri];
      var y = HEAD_H + ri * CELL + CELL / 2 + 4;
      var hitR = svgEl("rect", {
        x: 0, y: HEAD_H + ri * CELL, width: LABEL_W, height: CELL,
        class: "hit", "data-axis": "row", "data-id": qid
      });
      svg.appendChild(hitR);
      var txtR = svgEl("text", {
        x: LABEL_W - 8, y: y, class: "lbl", "text-anchor": "end",
        "data-axis": "row", "data-id": qid
      });
      txtR.textContent = truncate(DATA.questions[qid].text, 56);
      svg.appendChild(txtR);
      attachDrag(txtR, "row", qid);
      attachDrag(hitR, "row", qid);
    }

    // data cells
    var shownCount = 0;
    for (var i = 0; i < rowOrder.length; i++) {
      for (var j = 0; j < colOrder.length; j++) {
        var c = cellIndex[key(rowOrder[i], colOrder[j])];
        if (!c) continue;
        shownCount++;
        var cx = LABEL_W + j * CELL, cy = HEAD_H + i * CELL;
        var rect = svgEl("rect", {
          x: cx + 1, y: cy + 1, width: CELL - 2, height: CELL - 2,
          fill: DATA.palette[c.color - 1] || "#999",
          class: "cell" + (c.checked ? "" : " provisional")
        });
        rect.addEventListener("click", (function (q, v) {
          return function () { showClaimPanel(q, v); };
        })(rowOrder[i], colOrder[j]));
        var tt = svgEl("title", {});
        tt.textContent = DATA.questions[rowOrder[i]].text.slice(0, 70) + " — " +
          voiceLabel(colOrder[j]) + " — " + DATA.positions[c.position].summary.slice(0, 90);
        rect.appendChild(tt);
        svg.appendChild(rect);
        if (c.changed) {
          svg.appendChild(svgEl("circle", {
            cx: cx + CELL - 3, cy: cy + 3, r: 2, class: "changed-marker"
          }));
        }
        if (!c.dated) {
          // Undated pick (no dated Claim in this cell's group): a visible
          // ring in the opposite corner from the "changed" dot, orthogonal
          // to and distinct from the checked/provisional border style.
          svg.appendChild(svgEl("circle", {
            cx: cx + 4, cy: cy + CELL - 5, r: 2.4, class: "undated-marker"
          }));
        }
      }
    }

    document.getElementById("stat").textContent =
      rowOrder.length + " Questions × " + colOrder.length + " Voices, " +
      shownCount + " cells shown" +
      (showAll ? "" : " (of " + DATA.meta.counts.questions + " / " + DATA.meta.counts.voices + " total)");
  }

  function buildMatrixLegend() {
    var l = document.getElementById("legend");
    l.innerHTML = "";
    var lab = document.createElement("span");
    lab.textContent =
      "position within its own row, not comparable across rows (1–6, 7 = overflow / 7+ held):";
    l.appendChild(lab);
    for (var i = 0; i < DATA.palette.length; i++) {
      var sw = document.createElement("span");
      sw.className = "sw";
      sw.style.background = DATA.palette[i];
      l.appendChild(sw);
      if (i === DATA.palette.length - 1) {
        var ofLab = document.createElement("span");
        ofLab.textContent = "7+";
        l.appendChild(ofLab);
      }
    }
    var none = document.createElement("span");
    none.className = "sw";
    none.style.background = "#dedad3";
    l.appendChild(none);
    var noneLab = document.createElement("span");
    noneLab.textContent = "none";
    l.appendChild(noneLab);
  }

  function buildGraphLegend() {
    var l = document.getElementById("legend");
    l.innerHTML = "";
    var shapes = [
      ["question", "circle"],
      ["concept", "square"],
      ["domain", "diamond"],
      ["value", "triangle"]
    ];
    for (var i = 0; i < shapes.length; i++) {
      var s = document.createElement("span");
      s.textContent = shapes[i][0] + " = " + shapes[i][1] + (i < shapes.length - 1 ? "; " : ". ");
      l.appendChild(s);
    }
    var sz = document.createElement("span");
    sz.textContent = "size = degree. ";
    l.appendChild(sz);
    var cc = document.createElement("span");
    cc.textContent = "Concept–Concept edges in this map: " + DATA.graph.concept_concept_count + ".";
    l.appendChild(cc);
  }

  function setMatrixScope(newShowAll) {
    showAll = newShowAll;
    var btn = document.getElementById("btn-scope");
    btn.classList.toggle("active", showAll);
    btn.textContent = showAll ? "Default subset" : "Show all";
    revealed = {};
    resetOrders();
    render();
  }

  document.getElementById("btn-scope").addEventListener("click", function () {
    setMatrixScope(!showAll);
  });
  document.getElementById("btn-reorder").addEventListener("click", doReorder);
  document.getElementById("panel-close").addEventListener("click", closePanel);

  function updateNote() {
    var note = document.getElementById("note");
    if (currentView === "matrix") {
      note.textContent =
        "Rust opinion map — " + DATA.meta.counts.questions + " Questions, " +
        DATA.meta.counts.positions + " Positions, " + DATA.meta.counts.claims + " Claims, " +
        DATA.meta.counts.voices + " Voices — generated " + DATA.meta.generated + ". " +
        "Solid border = checked (quote/date verified against Source, 2026-09-28); " +
        "dashed border = provisional (unverified Voice, never fidelity-checked). " +
        "A ring marks an undated pick (no dated Claim to sort by); a filled dot marks a cell " +
        "where the Voice changed Position over time — click for the history. " +
        "Column names stay anonymous until clicked.";
    } else {
      note.textContent =
        "Graph — Questions, Concepts, Domains and Values that carry at least one edge; " +
        "edges are Question–Concept, Question–Domain, Question–Value (weighted by " +
        "Argument count) and Concept–Concept (drawn only where the data holds them, " +
        DATA.graph.concept_concept_count + " today). Node size follows degree; Domain and " +
        "Value labels always show, Concept and Question labels show on hover and stay pinned " +
        "after a click. Click a node for its side panel; a Question chip there jumps to that " +
        "row in the Matrix.";
    }
  }

  // ---------------- Graph view ----------------
  // Deterministic force layout: seeded start positions (fixed PRNG seed), a
  // fixed iteration count set only by node count, no animation loop once
  // those iterations finish — the same input always settles at the same
  // positions.

  var GRAPH_W = 1400, GRAPH_H = 900;
  var graphNodeById = {};
  for (var gi = 0; gi < DATA.graph.nodes.length; gi++) {
    graphNodeById[DATA.graph.nodes[gi].id] = DATA.graph.nodes[gi];
  }
  var graphShowAll = false;
  var graphRevealed = {};
  var graphLayoutCache = {};

  function mulberry32(seed) {
    return function () {
      seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
      var t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function layoutGraph(nodeIds, edgeList) {
    var rand = mulberry32(1337);
    var n = nodeIds.length;
    var pos = {};
    for (var i = 0; i < n; i++) {
      var ang = rand() * Math.PI * 2;
      var rad = (0.15 + 0.75 * rand()) * Math.min(GRAPH_W, GRAPH_H) / 2;
      pos[nodeIds[i]] = {
        x: GRAPH_W / 2 + Math.cos(ang) * rad,
        y: GRAPH_H / 2 + Math.sin(ang) * rad
      };
    }
    if (n === 0) return pos;
    var iterations = n > 600 ? 60 : 150;
    var k = Math.sqrt((GRAPH_W * GRAPH_H) / n);
    for (var it = 0; it < iterations; it++) {
      var temp = (1 - it / iterations) * (k * 0.6);
      var disp = {};
      for (var di = 0; di < n; di++) disp[nodeIds[di]] = { x: 0, y: 0 };
      for (var a = 0; a < n; a++) {
        var pa = pos[nodeIds[a]];
        for (var b = a + 1; b < n; b++) {
          var pb = pos[nodeIds[b]];
          var dx = pa.x - pb.x, dy = pa.y - pb.y;
          var dist = Math.sqrt(dx * dx + dy * dy) || 0.01;
          var force = (k * k) / dist;
          var fx = (dx / dist) * force, fy = (dy / dist) * force;
          disp[nodeIds[a]].x += fx; disp[nodeIds[a]].y += fy;
          disp[nodeIds[b]].x -= fx; disp[nodeIds[b]].y -= fy;
        }
      }
      for (var e = 0; e < edgeList.length; e++) {
        var edge = edgeList[e];
        var pa2 = pos[edge.source], pb2 = pos[edge.target];
        if (!pa2 || !pb2) continue;
        var dx2 = pa2.x - pb2.x, dy2 = pa2.y - pb2.y;
        var dist2 = Math.sqrt(dx2 * dx2 + dy2 * dy2) || 0.01;
        var w = 0.4 + Math.min(edge.weight || 1, 5) * 0.15;
        var force2 = ((dist2 * dist2) / k) * w;
        var fx2 = (dx2 / dist2) * force2, fy2 = (dy2 / dist2) * force2;
        disp[edge.source].x -= fx2; disp[edge.source].y -= fy2;
        disp[edge.target].x += fx2; disp[edge.target].y += fy2;
      }
      for (var c = 0; c < n; c++) {
        var id = nodeIds[c];
        var p = pos[id], d = disp[id];
        var dlen = Math.sqrt(d.x * d.x + d.y * d.y) || 0.01;
        var capped = Math.min(dlen, temp);
        p.x += (d.x / dlen) * capped;
        p.y += (d.y / dlen) * capped;
        p.x += (GRAPH_W / 2 - p.x) * 0.002;
        p.y += (GRAPH_H / 2 - p.y) * 0.002;
        p.x = Math.max(20, Math.min(GRAPH_W - 20, p.x));
        p.y = Math.max(20, Math.min(GRAPH_H - 20, p.y));
      }
    }
    return pos;
  }

  function graphNeighbors(nodeId) {
    var out = [];
    for (var i = 0; i < DATA.graph.edges.length; i++) {
      var e = DATA.graph.edges[i];
      if (e.source === nodeId) out.push({ id: e.target, kind: e.kind, weight: e.weight });
      else if (e.target === nodeId) out.push({ id: e.source, kind: e.kind, weight: e.weight });
    }
    return out;
  }

  function currentGraphNodeIds() {
    return graphShowAll
      ? DATA.graph.nodes.map(function (n) { return n.id; })
      : DATA.graph.default_subset.slice();
  }

  function graphRadius(degree) {
    return Math.min(4 + Math.sqrt(degree) * 1.8, 22);
  }

  function graphShape(kind, cx, cy, r) {
    if (kind === "question") return svgEl("circle", { cx: cx, cy: cy, r: r, class: "shape" });
    if (kind === "concept") {
      return svgEl("rect", { x: cx - r, y: cy - r, width: r * 2, height: r * 2, class: "shape" });
    }
    if (kind === "domain") {
      var pts = [[cx, cy - r], [cx + r, cy], [cx, cy + r], [cx - r, cy]]
        .map(function (p) { return p.join(","); }).join(" ");
      return svgEl("polygon", { points: pts, class: "shape" });
    }
    var h = r * 1.6;
    var pts2 = [[cx, cy - h * 0.6], [cx + r, cy + h * 0.4], [cx - r, cy + h * 0.4]]
      .map(function (p) { return p.join(","); }).join(" ");
    return svgEl("polygon", { points: pts2, class: "shape" });
  }

  function renderGraph() {
    var nodeIds = currentGraphNodeIds();
    var idSet = {};
    for (var i0 = 0; i0 < nodeIds.length; i0++) idSet[nodeIds[i0]] = true;
    var edgeSubset = DATA.graph.edges.filter(function (e) {
      return idSet[e.source] && idSet[e.target];
    });

    var cacheKey = graphShowAll ? "all" : "default";
    if (!graphLayoutCache[cacheKey]) {
      graphLayoutCache[cacheKey] = layoutGraph(nodeIds, edgeSubset);
    }
    var pos = graphLayoutCache[cacheKey];

    var svg = document.getElementById("graph");
    svg.innerHTML = "";
    svg.setAttribute("viewBox", "0 0 " + GRAPH_W + " " + GRAPH_H);
    svg.setAttribute("preserveAspectRatio", "xMidYMid meet");

    for (var e2 = 0; e2 < edgeSubset.length; e2++) {
      var edge = edgeSubset[e2];
      var pa3 = pos[edge.source], pb3 = pos[edge.target];
      if (!pa3 || !pb3) continue;
      var line = svgEl("line", {
        x1: pa3.x, y1: pa3.y, x2: pb3.x, y2: pb3.y,
        class: "gedge kind-" + edge.kind,
        "stroke-width": Math.min(0.5 + (edge.weight || 1) * 0.35, 4)
      });
      svg.appendChild(line);
    }

    for (var n2 = 0; n2 < nodeIds.length; n2++) {
      var nid2 = nodeIds[n2];
      var node = graphNodeById[nid2];
      if (!node || !pos[nid2]) continue;
      var p2 = pos[nid2];
      var r2 = graphRadius(node.degree);
      var g = svgEl("g", {
        class: "gnode kind-" + node.kind + (graphRevealed[nid2] ? " revealed" : "")
      });
      g.appendChild(graphShape(node.kind, p2.x, p2.y, r2));
      var lbl = svgEl("text", { x: p2.x + r2 + 3, y: p2.y + 3, class: "glabel" });
      lbl.textContent = truncate(node.label, 40);
      g.appendChild(lbl);
      var tt2 = svgEl("title", {});
      tt2.textContent = node.kind + ": " + node.label + " (degree " + node.degree + ")";
      g.appendChild(tt2);
      g.addEventListener("click", (function (id) {
        return function () {
          graphRevealed[id] = !graphRevealed[id];
          showGraphNodePanel(id);
          renderGraph();
        };
      })(nid2));
      svg.appendChild(g);
    }

    document.getElementById("stat").textContent =
      nodeIds.length + " nodes, " + edgeSubset.length + " edges shown" +
      (graphShowAll ? "" : " (default subset; full graph: " +
        DATA.graph.counts.nodes_full + " nodes, " + DATA.graph.counts.edges_full + " edges)");
  }

  function showGraphNodePanel(nodeId) {
    var node = graphNodeById[nodeId];
    var body = document.getElementById("panel-body");
    body.innerHTML = "";
    if (!node) return;
    var h = document.createElement("h2");
    h.textContent = node.kind.charAt(0).toUpperCase() + node.kind.slice(1);
    body.appendChild(h);
    var ctx = document.createElement("div");
    ctx.className = "q-context";
    ctx.textContent = node.label;
    body.appendChild(ctx);
    body.appendChild(field("Degree", String(node.degree)));

    var neighbors = graphNeighbors(nodeId);
    neighbors.sort(function (x, y) {
      var nx = graphNodeById[x.id], ny = graphNodeById[y.id];
      if (!nx || !ny) return 0;
      if (nx.kind !== ny.kind) return nx.kind < ny.kind ? -1 : 1;
      return nx.label < ny.label ? -1 : (nx.label > ny.label ? 1 : 0);
    });
    var wrap = document.createElement("div");
    neighbors.forEach(function (nb) {
      var nnode = graphNodeById[nb.id];
      if (!nnode) return;
      var chip = badge(nnode.kind + ": " + truncate(nnode.label, 40), "voice-chip nbr-chip");
      chip.addEventListener("click", function () {
        if (nnode.kind === "question") {
          jumpToMatrixRow(nnode.raw);
        } else {
          showGraphNodePanel(nb.id);
        }
      });
      wrap.appendChild(chip);
    });
    body.appendChild(field("Neighbours (" + neighbors.length + ")", wrap));
    openPanel();
  }

  function jumpToMatrixRow(qid) {
    setView("matrix");
    if (!showAll && DATA.default_subset.questions.indexOf(qid) === -1) {
      setMatrixScope(true);
    } else {
      render();
    }
    var rowEl = document.querySelector(
      'svg#matrix text.lbl[data-axis="row"][data-id="' + qid + '"]'
    );
    if (rowEl) {
      rowEl.scrollIntoView({ block: "center", inline: "center" });
      rowEl.classList.add("pulse-row");
      setTimeout(function () { rowEl.classList.remove("pulse-row"); }, 1600);
    }
    showQuestionPanel(qid);
  }

  function setView(view) {
    currentView = view;
    document.getElementById("btn-view-matrix").classList.toggle("active", view === "matrix");
    document.getElementById("btn-view-graph").classList.toggle("active", view === "graph");
    document.getElementById("matrix-controls").style.display = view === "matrix" ? "" : "none";
    document.getElementById("graph-controls").style.display = view === "graph" ? "" : "none";
    document.getElementById("gridwrap").style.display = view === "matrix" ? "" : "none";
    document.getElementById("graphwrap").style.display = view === "graph" ? "" : "none";
    closePanel();
    if (view === "matrix") {
      render();
      buildMatrixLegend();
    } else {
      renderGraph();
      buildGraphLegend();
    }
    updateNote();
  }

  document.getElementById("btn-view-matrix").addEventListener("click", function () { setView("matrix"); });
  document.getElementById("btn-view-graph").addEventListener("click", function () { setView("graph"); });
  document.getElementById("btn-graph-scope").addEventListener("click", function () {
    graphShowAll = !graphShowAll;
    this.classList.toggle("active", graphShowAll);
    this.textContent = graphShowAll ? "Default subset" : "Show all";
    graphRevealed = {};
    renderGraph();
  });

  var currentView = "matrix";
  buildMatrixLegend();
  resetOrders();
  render();
  document.getElementById("btn-scope").textContent = "Show all";
  updateNote();
})();
</script>
</body>
</html>
"""
