"""Bertin's reorderable matrix: derivation and view, moved as is.

Everything here came out of the single-file src/gym/map/site.py unchanged --
the cell/latest/changed/checked rules, the colour index, the fixed-point
default subset, the seriation, the drag, the panels. Only the surrounding
packaging moved. Another agent replaces this view with the two-way
clustered Matrix the owner ruled for on 2026-09-30; until then its
behaviour is the behaviour the site-v02 screenshot shows.
"""

from __future__ import annotations

from collections import defaultdict

from gym.map.cluster import cocluster

# Okabe-Ito base, re-lightened for a dark (#0e1116) canvas: the two entries
# that read fine on white but sank toward the background on dark --
# #009E73 (green) and #0072B2 (blue) -- are lifted in luminance; the rest
# were already bright enough to hold contrast unchanged.
PALETTE = ["#E69F00", "#56B4E9", "#00C896", "#F0E442", "#3391D6", "#E8703A", "#B368A0"]


def build_matrix(
    questions: dict[str, dict],
    positions: dict[str, dict],
    claims: dict[str, dict],
    voices: dict[str, dict],
    sources: dict[str, dict],
    arguments: dict[str, dict],
    values: dict[str, dict],
) -> dict:
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

    # --- two-way co-clustering (owner ruling 2026-09-30): Voices are similar
    # by their stances on Questions, Questions are similar by the Voices
    # taking stances on them. cocluster() runs its own 2-core thin filter
    # (min_row_degree=2, min_col_degree=2), which supersedes the matrix's
    # former standalone bipartite-fixed-point filter: the default view is
    # now exactly cocluster()'s non-thin core, and row_order/col_order
    # already carry the clustered order with thin rows/cols appended last.
    cluster_cells: dict[tuple[str, str], str] = {
        (cell["q"], cell["v"]): cell["position"] for cell in matrix_cells
    }
    clustering = cocluster(cluster_cells)

    thin_row_set = set(clustering.thin_rows)
    thin_col_set = set(clustering.thin_cols)
    candidate_questions = {q for q in clustering.row_order if q not in thin_row_set}
    candidate_voices = {v for v in clustering.col_order if v not in thin_col_set}
    default_cells = [
        cell
        for cell in matrix_cells
        if cell["q"] in candidate_questions and cell["v"] in candidate_voices
    ]

    clustering_payload = {
        "row_order": clustering.row_order,
        "col_order": clustering.col_order,
        "thin_rows": clustering.thin_rows,
        "thin_cols": clustering.thin_cols,
        "k": clustering.k,
        "blocks": [
            {
                "rows": b.row_group,
                "cols": b.col_group,
                "fill_ratio": b.fill_ratio,
                "agreement": b.dominant_position_agreement,
                "cells_present": b.cells_present,
            }
            for b in clustering.blocks
        ],
    }

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

    return {
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
        "clustering": clustering_payload,
        "problems": dict(problems),
        "stats": {
            "cells_total": len(matrix_cells),
            "default": {
                "questions": len(candidate_questions),
                "voices": len(candidate_voices),
                "cells": len(default_cells),
            },
            "undated_picks": undated_picks,
            "mixed_dated_undated": mixed_dated_undated,
            "overflow_questions": overflow_questions,
            "checked_count": checked_count,
        },
    }


MATRIX_CSS = r"""
  #gridwrap { flex: 1 1 auto; overflow: auto; padding: 18px; background: var(--canvas); }
  svg#matrix { display: block; }
  .hit { fill: transparent; cursor: pointer; }
  .hit:hover { fill: rgba(255,255,255,0.06); }
  .cell { stroke: var(--canvas); stroke-width: 1; cursor: pointer; }
  .cell.provisional { stroke-dasharray: 2,2; stroke: rgba(223,218,208,0.55); }
  /* Pre-existing bug found while wiring the dark theme, fixed here: these two
     rules used to read ".cell.changed-marker" / ".cell.undated-marker", but
     the circles below carry only the bare class -- the selector never
     matched, so "undated" rendered as a plain filled dot (default SVG
     fill: black) instead of the intended hollow ring. Selectors corrected;
     colours chosen for the dark canvas. */
  .changed-marker { fill: #12161d; stroke: rgba(255,255,255,.55); stroke-width: .6; }
  .undated-marker { fill: none; stroke: #ffffff; stroke-width: 1.1; }
  text.lbl { fill: var(--chrome-ink); font-size: 11px; cursor: pointer; user-select: none; }
  text.lbl:hover { fill: #ffffff; text-decoration: underline; }
  text.lbl.dragging { opacity: 0.4; }
  text.lbl.pulse-row { fill: #ff8f73; font-weight: 700; }
  .block-fill { pointer-events: none; }
  .block-outline { fill: none; stroke: var(--chrome-ink); stroke-width: 1.5; pointer-events: stroke; }
  .block-outline.block-discussion { stroke: #ff8f73; stroke-dasharray: 5,3; }
  /* A block can start at row/col 0, right over a Position-coloured cell --
     seen live as "discussion" landing on an orange cell and going half
     invisible when it was coral-on-orange. A dark halo (graph.py's own fix
     for glabel-over-varied-node-colour) keeps it legible over any cell
     colour regardless of the label's own ink. */
  text.block-label { fill: var(--chrome-dim); font-size: 10px; font-weight: 700; font-variant: small-caps;
    letter-spacing: .06em; pointer-events: none; paint-order: stroke;
    stroke: var(--canvas); stroke-width: 3px; stroke-linejoin: round; }
  .gap-hairline { stroke: var(--chrome-line); stroke-width: 1; }
  .gap-label { fill: var(--chrome-dim); font-size: 9px; letter-spacing: .08em; pointer-events: none; }
  .hover-band { fill: #ffffff; pointer-events: none; }
"""


MATRIX_JS = r"""
  var CELL = 18, LABEL_W = 280, HEAD_H = 170, GAP = 28;
  var LABEL_FONT = "11px -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif";
  var showAll = false;
  var rowOrder = [], colOrder = [];
  var revealed = {};
  var cellIndex = {};

  function key(q, v) { return q + "\u0001" + v; }

  function buildCellIndex() {
    cellIndex = {};
    for (var i = 0; i < DATA.matrix.length; i++) {
      var c = DATA.matrix[i];
      cellIndex[key(c.q, c.v)] = c;
    }
  }

  // --- pixel-accurate label fitting (SVG <text> has no CSS text-overflow) --
  var _measureCtx = null;
  function textWidth(s, font) {
    if (!_measureCtx) _measureCtx = document.createElement("canvas").getContext("2d");
    _measureCtx.font = font;
    return _measureCtx.measureText(s).width;
  }
  function ellipsisFit(s, maxWidth, font) {
    if (textWidth(s, font) <= maxWidth) return s;
    var lo = 0, hi = s.length;
    while (lo < hi) {
      var mid = (lo + hi + 1) >> 1;
      if (textWidth(s.slice(0, mid) + "…", font) <= maxWidth) lo = mid; else hi = mid - 1;
    }
    return lo > 0 ? s.slice(0, lo) + "…" : "…";
  }

  // The "default subset" cocluster() hands back, independent of showAll --
  // used only to size CELL/HEAD_H so that subset is what the width is sized
  // to; "show all" still renders past it, scrolled, as before.
  function coreColIds() {
    var c = DATA.clustering;
    return c.col_order.slice(0, c.col_order.length - c.thin_cols.length);
  }

  function computeLayout() {
    var coreCols = coreColIds();
    var maxColLabelW = 0;
    for (var i = 0; i < coreCols.length; i++) {
      var lw = textWidth(voiceLabel(coreCols[i]), LABEL_FONT);
      if (lw > maxColLabelW) maxColLabelW = lw;
    }
    // Column headers rotate -60deg; vertical space they need is the
    // label's pixel length projected onto the vertical axis (sin 60deg),
    // plus room for the rotation pivot and a little breathing space.
    HEAD_H = Math.max(60, Math.min(260, Math.round(maxColLabelW * Math.sin(Math.PI / 3)) + 34));
    // Measured off #wrap, not #gridwrap: #gridwrap is the overflow:auto box
    // whose own clientWidth shrinks the instant a scrollbar appears, which
    // would make this a closed loop chasing its own last frame. #wrap never
    // scrolls, so its box is stable input to size from.
    // -36 is #gridwrap's padding (18px both sides); -20 mirrors the same
    // fixed slack render() adds past the last column in its own w
    // (LABEL_W + cols*CELL + colGap + 20).
    // Sized to available WIDTH alone, up to 22px, so the default subset
    // fills the canvas horizontally rather than shrinking to also fit a
    // height budget -- rows beyond what the viewport shows scroll, same as
    // "show all" always has.
    var wrapEl = document.getElementById("wrap");
    var availW = (wrapEl.clientWidth || 1600) - 36 - 20 - LABEL_W;
    var byW = coreCols.length ? availW / coreCols.length : 18;
    CELL = Math.max(8, Math.min(22, Math.floor(byW)));
  }

  // Row/column order comes straight from cocluster()'s output: row_order /
  // col_order already carry the clustered groups first, thin rows/cols
  // appended last (src/gym/map/cluster.py). The default view is the
  // non-thin core (that ordering minus its trailing thin_rows/thin_cols);
  // "show all" is the full ordering, core then thin, rendered with a gap
  // between them (see rowY/colX in render()).
  function currentQuestions() {
    var c = DATA.clustering;
    if (showAll) return c.row_order.slice();
    return c.row_order.slice(0, c.row_order.length - c.thin_rows.length);
  }
  function currentVoices() {
    var c = DATA.clustering;
    if (showAll) return c.col_order.slice();
    return c.col_order.slice(0, c.col_order.length - c.thin_cols.length);
  }

  function resetOrders() {
    rowOrder = currentQuestions();
    colOrder = currentVoices();
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

  function voiceLabel(vid) {
    if (revealed[vid]) return DATA.voices[vid].name;
    // DATA.voice_number is the one numbering for the whole page (assigned
    // in load.py over all Voices, sorted by id) -- the same numbers the
    // Graph panel's Claim list shows, so a Voice reads the same number in
    // both views.
    return "Voice " + (DATA.voice_number.hasOwnProperty(vid) ? DATA.voice_number[vid] : "?");
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
    computeLayout();
    var svg = document.getElementById("matrix");
    svg.innerHTML = "";

    // Thin rows/cols only ever appear at the trailing end of rowOrder /
    // colOrder (cocluster()'s own convention, kept by currentQuestions /
    // currentVoices above): coreRowCount/coreColCount mark where the core
    // ends and the parked thin rows/cols begin. In the default (non-"show
    // all") view there are none, so the gap collapses to zero and rowY/colX
    // degrade to the old plain i*CELL/j*CELL.
    var thinRowN = showAll ? DATA.clustering.thin_rows.length : 0;
    var thinColN = showAll ? DATA.clustering.thin_cols.length : 0;
    var coreRowCount = rowOrder.length - thinRowN;
    var coreColCount = colOrder.length - thinColN;
    var rowGap = thinRowN > 0 ? GAP : 0;
    var colGap = thinColN > 0 ? GAP : 0;
    function rowY(i) { return HEAD_H + i * CELL + (i >= coreRowCount ? rowGap : 0); }
    function colX(j) { return LABEL_W + j * CELL + (j >= coreColCount ? colGap : 0); }

    var w = LABEL_W + colOrder.length * CELL + colGap + 20;
    var h = HEAD_H + rowOrder.length * CELL + rowGap + 20;
    svg.setAttribute("width", w);
    svg.setAttribute("height", h);
    svg.setAttribute("viewBox", "0 0 " + w + " " + h);

    if (rowOrder.length === 0 || colOrder.length === 0) {
      var t = svgEl("text", { x: 20, y: 40, class: "lbl" });
      t.textContent = "Empty subset.";
      svg.appendChild(t);
      return;
    }

    // background = "no claim" cells, one rect per (row band x col band) so
    // the gap between the core and the parked thin rows/cols stays visibly
    // empty rather than reading as more "no claim" cells. The field used to
    // be one solid light rect -- a light island on the dark page. It is now
    // a tiled pattern of individual faint dark squares (one per grid
    // position, canvas-coloured gutter between them, same idea as the data
    // cells' own stroke), anchored to each band's own top-left corner so the
    // tiling stays pixel-aligned with the real cell grid even across the
    // core/thin gap. O(1) DOM cost regardless of how many cells that is --
    // a <pattern>, not one rect per position.
    var bgDefs = svgEl("defs", {});
    svg.appendChild(bgDefs);
    var bgBandN = 0;
    function bgBand(rowStart, rowCount, colStart, colCount) {
      if (rowCount <= 0 || colCount <= 0) return;
      var patId = "bgpat" + (bgBandN++);
      var pattern = svgEl("pattern", {
        id: patId, patternUnits: "userSpaceOnUse",
        x: colX(colStart), y: rowY(rowStart), width: CELL, height: CELL
      });
      pattern.appendChild(svgEl("rect", { x: 1, y: 1, width: CELL - 2, height: CELL - 2, fill: "#161b23" }));
      bgDefs.appendChild(pattern);
      svg.appendChild(svgEl("rect", {
        x: colX(colStart), y: rowY(rowStart),
        width: colCount * CELL, height: rowCount * CELL,
        fill: "url(#" + patId + ")"
      }));
    }
    bgBand(0, coreRowCount, 0, coreColCount);
    bgBand(0, coreRowCount, coreColCount, thinColN);
    bgBand(coreRowCount, thinRowN, 0, coreColCount);
    bgBand(coreRowCount, thinRowN, coreColCount, thinColN);

    // the gap that separates the clustered core from parked thin rows/cols
    // reads as dead space otherwise; a hairline plus a small "thin" label
    // marks it as a deliberate break, not a rendering gap.
    if (thinColN > 0) {
      var gapX = LABEL_W + coreColCount * CELL + colGap / 2;
      svg.appendChild(svgEl("line", { x1: gapX, y1: 0, x2: gapX, y2: h, class: "gap-hairline" }));
      var gLblCol = svgEl("text", { x: gapX, y: 12, class: "gap-label", "text-anchor": "middle" });
      gLblCol.textContent = "thin";
      svg.appendChild(gLblCol);
    }
    if (thinRowN > 0) {
      var gapY = HEAD_H + coreRowCount * CELL + rowGap / 2;
      svg.appendChild(svgEl("line", { x1: 0, y1: gapY, x2: w, y2: gapY, class: "gap-hairline" }));
      var gLblRow = svgEl("text", { x: 4, y: gapY + 3, class: "gap-label" });
      gLblRow.textContent = "thin";
      svg.appendChild(gLblRow);
    }

    // a translucent row/col band, shown on hover (row and column hit areas
    // below toggle it); created now, appended once at the end of render()
    // so it paints on top of cells and blocks rather than under them.
    var rowBand = svgEl("rect", { x: 0, y: 0, width: w, height: CELL, class: "hover-band", "fill-opacity": "0" });
    var colBand = svgEl("rect", { x: 0, y: 0, width: CELL, height: h, class: "hover-band", "fill-opacity": "0" });

    // column headers (rotated) + drag/click hit area
    for (var ci = 0; ci < colOrder.length; ci++) {
      var vid = colOrder[ci];
      var x = colX(ci) + CELL / 2;
      var hit = svgEl("rect", {
        x: colX(ci), y: 0, width: CELL, height: HEAD_H,
        class: "hit", "data-axis": "col", "data-id": vid
      });
      svg.appendChild(hit);
      var txt = svgEl("text", {
        x: x, y: HEAD_H - 6, class: "lbl", "data-axis": "col", "data-id": vid,
        transform: "rotate(-60 " + x + " " + (HEAD_H - 6) + ")"
      });
      txt.textContent = voiceLabel(vid);
      svg.appendChild(txt);
      attachDrag(txt, "col", vid);
      attachDrag(hit, "col", vid);
      (function (bx) {
        function enter() { colBand.setAttribute("x", bx); colBand.setAttribute("fill-opacity", "0.07"); }
        function leave() { colBand.setAttribute("fill-opacity", "0"); }
        hit.addEventListener("mouseenter", enter);
        hit.addEventListener("mouseleave", leave);
        txt.addEventListener("mouseenter", enter);
        txt.addEventListener("mouseleave", leave);
      })(colX(ci));
    }

    // row headers + hit area
    for (var ri = 0; ri < rowOrder.length; ri++) {
      var qid = rowOrder[ri];
      var qText = DATA.questions[qid].text;
      var y = rowY(ri) + CELL / 2 + 4;
      var hitR = svgEl("rect", {
        x: 0, y: rowY(ri), width: LABEL_W, height: CELL,
        class: "hit", "data-axis": "row", "data-id": qid
      });
      var hitTitle = svgEl("title", {});
      hitTitle.textContent = qText;
      hitR.appendChild(hitTitle);
      svg.appendChild(hitR);
      var txtR = svgEl("text", {
        x: LABEL_W - 10, y: y, class: "lbl", "text-anchor": "end",
        "data-axis": "row", "data-id": qid
      });
      // Fit to the fixed label column by measured pixel width, not a
      // fixed character count: a 56-char cap at 11px can still run past a
      // 320px column on wide characters, which is exactly why row labels
      // used to clip mid-word against the panel edge. The full Question
      // text is always available on hover via the hit rect's <title>.
      txtR.textContent = ellipsisFit(qText, LABEL_W - 20, LABEL_FONT);
      svg.appendChild(txtR);
      attachDrag(txtR, "row", qid);
      attachDrag(hitR, "row", qid);
      (function (by) {
        function enter() { rowBand.setAttribute("y", by); rowBand.setAttribute("fill-opacity", "0.07"); }
        function leave() { rowBand.setAttribute("fill-opacity", "0"); }
        hitR.addEventListener("mouseenter", enter);
        hitR.addEventListener("mouseleave", leave);
        txtR.addEventListener("mouseenter", enter);
        txtR.addEventListener("mouseleave", leave);
      })(rowY(ri));
    }

    // block boxes: cocluster()'s diagonal blocks, one box per (row_group,
    // col_group) pair sharing a label. A block's bounding box is read off
    // the *current* rowOrder/colOrder positions of its members (min..max on
    // each axis), so it stays correct through a manual drag, not just the
    // default clustered order. Computed once, used for both the fill wash
    // (drawn under the cells) and the outline (drawn over them).
    var rowPos = {}, colPos = {};
    for (var pi = 0; pi < rowOrder.length; pi++) rowPos[rowOrder[pi]] = pi;
    for (var pj = 0; pj < colOrder.length; pj++) colPos[colOrder[pj]] = pj;
    var blocks = DATA.clustering.blocks;
    var blockBoxes = [];
    var blockCellKeys = {};
    for (var bi = 0; bi < blocks.length; bi++) {
      var blk = blocks[bi];
      if (!blk.rows.length || !blk.cols.length) continue;
      var rIdxs = [], cIdxs = [];
      for (var bri = 0; bri < blk.rows.length; bri++) {
        if (rowPos.hasOwnProperty(blk.rows[bri])) rIdxs.push(rowPos[blk.rows[bri]]);
      }
      for (var bci = 0; bci < blk.cols.length; bci++) {
        if (colPos.hasOwnProperty(blk.cols[bci])) cIdxs.push(colPos[blk.cols[bci]]);
      }
      if (!rIdxs.length || !cIdxs.length) continue;
      var rMin = Math.min.apply(null, rIdxs), rMax = Math.max.apply(null, rIdxs);
      var cMin = Math.min.apply(null, cIdxs), cMax = Math.max.apply(null, cIdxs);
      blockBoxes.push({
        blk: blk, rMin: rMin, rMax: rMax, cMin: cMin, cMax: cMax,
        discussion: blk.agreement < 0.75
      });
      for (var bq = 0; bq < blk.rows.length; bq++) {
        for (var bv = 0; bv < blk.cols.length; bv++) {
          var bk = key(blk.rows[bq], blk.cols[bv]);
          if (cellIndex.hasOwnProperty(bk)) blockCellKeys[bk] = true;
        }
      }
    }

    // block fill: a 6%-alpha wash over the block's full rows-by-columns
    // area, not a bounding rectangle around mostly-empty cells -- the wash
    // reads as "this region is one block" even where a Voice holds no
    // Claim on a Question in it, which the old outline-only look did not
    // convey (it enclosed dead space and looked like a box around nothing).
    for (var fi = 0; fi < blockBoxes.length; fi++) {
      var fb = blockBoxes[fi];
      svg.appendChild(svgEl("rect", {
        x: colX(fb.cMin), y: rowY(fb.rMin),
        width: (fb.cMax - fb.cMin + 1) * CELL, height: (fb.rMax - fb.rMin + 1) * CELL,
        // The field is the dark canvas now (the light-beige field this
        // used to sit on is gone), so the wash is a light neutral again --
        // at 12%, not the original 6%, since 6% over a dark canvas read
        // too close to invisible once the field stopped being light.
        fill: "#dfe5ee", "fill-opacity": "0.12", class: "block-fill"
      }));
    }

    // data cells -- a cell that actually falls inside a block's rows x cols
    // area is drawn 1px larger (thinner white gutter) so it reads as part
    // of the block's wash rather than floating a hairline above it.
    var shownCount = 0;
    for (var i = 0; i < rowOrder.length; i++) {
      for (var j = 0; j < colOrder.length; j++) {
        var ckey = key(rowOrder[i], colOrder[j]);
        var c = cellIndex[ckey];
        if (!c) continue;
        shownCount++;
        var cx = colX(j), cy = rowY(i);
        var inset = blockCellKeys.hasOwnProperty(ckey) ? 0.5 : 1;
        var size = CELL - inset * 2;
        var rect = svgEl("rect", {
          x: cx + inset, y: cy + inset, width: size, height: size,
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

    // block outlines on top of the cells: a 1px stroke plus, for a block
    // under the 75% agreement bar, a dashed "discussion" label. fill_ratio
    // and agreement go in the hover tooltip.
    for (var oi = 0; oi < blockBoxes.length; oi++) {
      var ob = blockBoxes[oi];
      var outline = svgEl("rect", {
        x: colX(ob.cMin), y: rowY(ob.rMin),
        width: (ob.cMax - ob.cMin + 1) * CELL, height: (ob.rMax - ob.rMin + 1) * CELL,
        class: "block-outline" + (ob.discussion ? " block-discussion" : "")
      });
      var bt = svgEl("title", {});
      bt.textContent = "Block: " + ob.blk.rows.length + " Questions × " + ob.blk.cols.length +
        " Voices — fill " + Math.round(ob.blk.fill_ratio * 100) + "%, agreement " +
        Math.round(ob.blk.agreement * 100) + "%" + (ob.discussion ? " (discussion)" : "");
      outline.appendChild(bt);
      svg.appendChild(outline);
      if (ob.discussion) {
        var lbl = svgEl("text", {
          x: colX(ob.cMin) + 3, y: rowY(ob.rMin) + 11, class: "block-label"
        });
        lbl.textContent = "discussion";
        svg.appendChild(lbl);
      }
    }

    svg.appendChild(rowBand);
    svg.appendChild(colBand);

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
    none.style.background = "#161b23";
    l.appendChild(none);
    var noneLab = document.createElement("span");
    noneLab.textContent = "none";
    l.appendChild(noneLab);
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


  function matrixNote() {
    return "Rust opinion map \u2014 " + DATA.meta.counts.questions + " Questions, " +
      DATA.meta.counts.positions + " Positions, " + DATA.meta.counts.claims + " Claims, " +
      DATA.meta.counts.voices + " Voices \u2014 generated " + DATA.meta.generated + ". " +
      "Solid border = checked (quote/date verified against Source, 2026-09-28); " +
      "dashed border = provisional (unverified Voice, never fidelity-checked). " +
      "A ring marks an undated pick (no dated Claim to sort by); a filled dot marks a cell " +
      "where the Voice changed Position over time \u2014 click for the history. " +
      "Column names stay anonymous until clicked; Voice numbers are the same here as in " +
      "the Graph panel. Rows and columns are co-clustered (Dhillon spectral co-clustering) " +
      "into blocks, outlined \u2014 dashed and labelled \"discussion\" where the block's Voices " +
      "agree on a stance under 75% of the time. Thin rows/columns (too few Claims to " +
      "cluster) are parked past the gap in \u201cShow all\u201d.";
  }

  function jumpToMatrixRow(qid) {
    setView("matrix");
    if (!showAll && DATA.clustering.thin_rows.indexOf(qid) !== -1) {
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
"""
