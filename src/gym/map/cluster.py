"""Two-way (row/column) co-clustering of the Matrix's Question x Voice cells.

Owner ruling 2026-09-30: Voices are similar by their stances on Questions,
Questions are similar by the Voices taking stances on them; rows and columns
are clustered on both, and the lumps that appear are the Schools.

Method (Dhillon 2001, "Co-clustering documents and words using bipartite
spectral graph partitioning"), adapted so the signal a Voice contributes is
which Position it holds, not merely that it answered:

1. Thin rule: iterate a 2-core filter over the (question, voice) cells --
   drop a question below `min_row_degree` surviving voices, drop a voice
   below `min_col_degree` surviving questions, repeat to a fixed point. What
   is dropped is the trailing "thin" group; it is never clustered.
2. Bipartite graph: left nodes are surviving Voices, right nodes are the
   distinct (question, position) pairs actually chosen among surviving
   cells. Edge Voice--(question, position) exists iff that Voice's resolved
   cell on that question is that position. This is the literal "Voice to
   (Question, Position) pairs" bipartite graph: two Voices are close only
   when they hold the *same stance*, not merely opine on the same Question.
3. Biadjacency A (voices x (question,position)) is normalised
   D1^-1/2 A D2^-1/2 (Dhillon's An) and SVD'd. The top singular
   vector/value is trivial (Dhillon Thm 1) and dropped.
4. k is chosen by the eigengap in the remaining singular values, capped at
   `max_k`.
5. l = ceil(log2 k) non-trivial singular vector pairs (Dhillon's rule) embed
   every Voice and every (question, position) node into R^l via
   Z = [D1^-1/2 U_l ; D2^-1/2 V_l]; seeded k-means partitions Z's rows into
   k joint clusters -- this is what makes it *co*-clustering: Voices and
   (question,position) pairs share one label space.
6. A (question,position) cluster label is pushed down to its question by
   plurality vote weighted by cell count (ties -> lowest label index); this
   turns the column-side clusters into a Question partition without ever
   letting one question's positions outvote each other silently.
7. Ordering (row_order/col_order) uses the first non-trivial singular
   vector as a 1-D Fiedler-style coordinate: groups are ordered by their
   members' mean coordinate, members within a group by their own
   coordinate, ties by id. Thin rows/cols are appended, sorted by id.
8. A block is a (row_group, col_group) pair sharing a cluster label. Its
   fill_ratio is realised-cells / (|rows| * |cols|). Position ids are
   question-scoped (`<question>--p<n>`), so no id is ever shared across two
   different questions -- comparing raw ids block-wide would always read
   near zero regardless of real agreement. dominant_position_agreement is
   instead computed per question inside the block (the share of the
   block's voices on that question holding that question's single most
   common position there), then averaged across the block's realised cells;
   this is the number that actually answers "do this block's Voices hold
   the same stance on these Questions".

Determinism: every RNG use (k-means init) is seeded from the `seed`
argument; every tie (position votes, ordering, k-means assignment via
np.argmin) resolves to the lowest sorted id or lowest index, so two runs on
the same cells and seed produce byte-identical output.
"""

from __future__ import annotations

import math
from collections import Counter, defaultdict
from dataclasses import dataclass, field

import numpy as np


@dataclass(frozen=True)
class Block:
    row_group: list[str]
    col_group: list[str]
    fill_ratio: float
    dominant_position_agreement: float
    cells_present: int


@dataclass(frozen=True)
class Clustering:
    row_order: list[str]
    col_order: list[str]
    row_groups: list[list[str]]
    col_groups: list[list[str]]
    blocks: list[Block]
    thin_rows: list[str] = field(default_factory=list)
    thin_cols: list[str] = field(default_factory=list)
    k: int = 0
    singular_values: list[float] = field(default_factory=list)


def _two_core(
    cells: dict[tuple[str, str], str], min_row_degree: int, min_col_degree: int
) -> tuple[set[str], set[str]]:
    row_neighbors: dict[str, set[str]] = defaultdict(set)
    col_neighbors: dict[str, set[str]] = defaultdict(set)
    for q, v in cells:
        row_neighbors[q].add(v)
        col_neighbors[v].add(q)

    cur_rows = set(row_neighbors)
    cur_cols = set(col_neighbors)
    while True:
        next_rows = {
            q
            for q in cur_rows
            if len(row_neighbors[q] & cur_cols) >= min_row_degree
        }
        next_cols = {
            v
            for v in cur_cols
            if len(col_neighbors[v] & next_rows) >= min_col_degree
        }
        if next_rows == cur_rows and next_cols == cur_cols:
            return cur_rows, cur_cols
        cur_rows, cur_cols = next_rows, next_cols


def _choose_k(singular_values: np.ndarray, max_k: int) -> int:
    """Eigengap on the non-trivial singular values, capped at max_k.

    singular_values[0] is Dhillon's trivial value/vector and is never
    considered. k = 1 + (index of the largest gap among the rest), so the
    largest drop after the (k-1)-th non-trivial value picks k clusters.
    Floors at 2 (a single cluster is not a co-clustering); floors at 1 when
    fewer than 2 non-trivial values exist at all (degenerate input).
    """
    non_trivial = singular_values[1:]
    limit = min(max_k, len(non_trivial))
    if limit < 2:
        return max(1, limit)
    candidates = non_trivial[:limit]
    gaps = candidates[:-1] - candidates[1:]
    best = int(np.argmax(gaps))  # first (largest) gap on ties
    return best + 2


def _seeded_kmeans(
    z: np.ndarray, k: int, seed: int, max_iter: int = 300
) -> np.ndarray:
    """Deterministic Lloyd's-algorithm k-means: k-means++ init from a seeded
    RandomState, then iterate to convergence. np.argmin always returns the
    first (lowest-index) minimiser, so every distance tie resolves the same
    way across runs given the same seed.
    """
    n = z.shape[0]
    if k >= n:
        return np.arange(n) % k
    rng = np.random.RandomState(seed)

    centers = np.empty((k, z.shape[1]))
    first = int(rng.randint(0, n))
    centers[0] = z[first]
    closest_sq = np.sum((z - centers[0]) ** 2, axis=1)
    for i in range(1, k):
        total = closest_sq.sum()
        if total <= 0:
            # every remaining point already sits exactly on a chosen center;
            # any further center choice is degenerate, pick deterministically
            pick = i % n
        else:
            probs = closest_sq / total
            pick = int(rng.choice(n, p=probs))
        centers[i] = z[pick]
        dist_sq = np.sum((z - centers[i]) ** 2, axis=1)
        closest_sq = np.minimum(closest_sq, dist_sq)

    labels = np.zeros(n, dtype=int)
    for _ in range(max_iter):
        dists = np.stack(
            [np.sum((z - centers[j]) ** 2, axis=1) for j in range(k)], axis=1
        )
        new_labels = np.argmin(dists, axis=1)
        if np.array_equal(new_labels, labels) and _ > 0:
            break
        labels = new_labels
        for j in range(k):
            members = z[labels == j]
            if len(members) > 0:
                centers[j] = members.mean(axis=0)
    return labels


def cocluster(
    cells: dict[tuple[str, str], str],
    min_row_degree: int = 2,
    min_col_degree: int = 2,
    *,
    max_k: int = 12,
    seed: int = 0,
) -> Clustering:
    all_rows = sorted({q for q, _ in cells})
    all_cols = sorted({v for _, v in cells})

    surviving_rows, surviving_cols = _two_core(cells, min_row_degree, min_col_degree)
    thin_rows = sorted(set(all_rows) - surviving_rows)
    thin_cols = sorted(set(all_cols) - surviving_cols)

    survivor_cells = {
        (q, v): pos
        for (q, v), pos in cells.items()
        if q in surviving_rows and v in surviving_cols
    }

    rows = sorted(surviving_rows)
    cols = sorted(surviving_cols)

    if len(rows) < 2 or len(cols) < 2 or not survivor_cells:
        return Clustering(
            row_order=rows,
            col_order=cols,
            row_groups=[rows] if rows else [],
            col_groups=[cols] if cols else [],
            blocks=[],
            thin_rows=thin_rows,
            thin_cols=thin_cols,
            k=1 if rows and cols else 0,
            singular_values=[],
        )

    qp_pairs = sorted({(q, pos) for (q, v), pos in survivor_cells.items()})
    qp_index = {qp: i for i, qp in enumerate(qp_pairs)}
    voice_index = {v: i for i, v in enumerate(cols)}

    a = np.zeros((len(cols), len(qp_pairs)))
    for (q, v), pos in survivor_cells.items():
        a[voice_index[v], qp_index[(q, pos)]] = 1.0

    row_sums = a.sum(axis=1)
    col_sums = a.sum(axis=0)
    d1_inv_sqrt = 1.0 / np.sqrt(row_sums)
    d2_inv_sqrt = 1.0 / np.sqrt(col_sums)
    an = (a * d1_inv_sqrt[:, None]) * d2_inv_sqrt[None, :]

    u, s, vt = np.linalg.svd(an, full_matrices=False)
    v = vt.T

    k = _choose_k(s, max_k)

    if k < 2:
        return Clustering(
            row_order=rows,
            col_order=cols,
            row_groups=[rows],
            col_groups=[cols],
            blocks=[],
            thin_rows=thin_rows,
            thin_cols=thin_cols,
            k=1,
            singular_values=[float(x) for x in s],
        )

    l = max(1, math.ceil(math.log2(k)))
    l = min(l, u.shape[1] - 1, v.shape[1] - 1)
    l = max(l, 1)

    u_l = u[:, 1 : 1 + l]
    v_l = v[:, 1 : 1 + l]
    voice_embed = d1_inv_sqrt[:, None] * u_l
    qp_embed = d2_inv_sqrt[:, None] * v_l
    z = np.vstack([voice_embed, qp_embed])

    labels = _seeded_kmeans(z, k, seed)
    voice_labels = labels[: len(cols)]
    qp_labels = labels[len(cols) :]

    col_groups_by_label: dict[int, list[str]] = {j: [] for j in range(k)}
    for v_id, lbl in zip(cols, voice_labels):
        col_groups_by_label[int(lbl)].append(v_id)

    # push (question, position) column labels down to a per-question label
    # by plurality vote weighted by cell count, ties -> lowest label index
    question_votes: dict[str, Counter[int]] = defaultdict(Counter)
    for (q, pos), lbl in zip(qp_pairs, qp_labels):
        weight = col_sums[qp_index[(q, pos)]]
        question_votes[q][int(lbl)] += weight

    row_groups_by_label: dict[int, list[str]] = {j: [] for j in range(k)}
    for q in rows:
        votes = question_votes.get(q)
        if not votes:
            continue
        best = max(votes.values())
        winner = min(lbl for lbl, count in votes.items() if count == best)
        row_groups_by_label[winner].append(q)

    for lbl in row_groups_by_label:
        row_groups_by_label[lbl].sort()
    for lbl in col_groups_by_label:
        col_groups_by_label[lbl].sort()

    # Fiedler-style 1-D ordering: first non-trivial singular vector, mapped
    # back through the same normalisation used for clustering.
    fiedler_voice = (d1_inv_sqrt * u[:, 1]) if u.shape[1] > 1 else np.zeros(len(cols))
    fiedler_qp = (d2_inv_sqrt * v[:, 1]) if v.shape[1] > 1 else np.zeros(len(qp_pairs))
    voice_coord = {v_id: float(fiedler_voice[i]) for i, v_id in enumerate(cols)}
    question_coord: dict[str, float] = {}
    question_weight: dict[str, float] = defaultdict(float)
    question_coord_sum: dict[str, float] = defaultdict(float)
    for i, (q, pos) in enumerate(qp_pairs):
        w = col_sums[i]
        question_coord_sum[q] += fiedler_qp[i] * w
        question_weight[q] += w
    for q in rows:
        w = question_weight.get(q, 0.0)
        question_coord[q] = question_coord_sum[q] / w if w > 0 else 0.0

    def _group_order_key(label: int, coord: dict[str, float], members: list[str]) -> float:
        if not members:
            return 0.0
        return sum(coord[m] for m in members) / len(members)

    row_label_order = sorted(
        row_groups_by_label,
        key=lambda lbl: (_group_order_key(lbl, question_coord, row_groups_by_label[lbl]), lbl),
    )
    col_label_order = sorted(
        col_groups_by_label,
        key=lambda lbl: (_group_order_key(lbl, voice_coord, col_groups_by_label[lbl]), lbl),
    )

    row_groups = [
        sorted(row_groups_by_label[lbl], key=lambda q: (question_coord[q], q))
        for lbl in row_label_order
    ]
    col_groups = [
        sorted(col_groups_by_label[lbl], key=lambda v_id: (voice_coord[v_id], v_id))
        for lbl in col_label_order
    ]

    row_order = [q for group in row_groups for q in group] + thin_rows
    col_order = [v_id for group in col_groups for v_id in group] + thin_cols

    blocks: list[Block] = []
    for out_i, lbl in enumerate(row_label_order):
        row_group = row_groups[out_i]
        # same label index pairs row cluster lbl with col cluster lbl:
        # both sides came from one joint k-means labelling of z.
        col_out_i = col_label_order.index(lbl)
        col_group = col_groups[col_out_i]
        if not row_group or not col_group:
            blocks.append(
                Block(
                    row_group=row_group,
                    col_group=col_group,
                    fill_ratio=0.0,
                    dominant_position_agreement=0.0,
                    cells_present=0,
                )
            )
            continue
        row_set = set(row_group)
        col_set = set(col_group)
        per_question_positions: dict[str, Counter[str]] = defaultdict(Counter)
        present = 0
        for (q, v_id), pos in survivor_cells.items():
            if q in row_set and v_id in col_set:
                present += 1
                per_question_positions[q][pos] += 1
        total_possible = len(row_group) * len(col_group)
        fill_ratio = present / total_possible if total_possible else 0.0
        if present > 0:
            agreeing = sum(
                counts.most_common(1)[0][1] for counts in per_question_positions.values()
            )
            agreement = agreeing / present
        else:
            agreement = 0.0
        blocks.append(
            Block(
                row_group=row_group,
                col_group=col_group,
                fill_ratio=fill_ratio,
                dominant_position_agreement=agreement,
                cells_present=present,
            )
        )

    return Clustering(
        row_order=row_order,
        col_order=col_order,
        row_groups=row_groups,
        col_groups=col_groups,
        blocks=blocks,
        thin_rows=thin_rows,
        thin_cols=thin_cols,
        k=k,
        singular_values=[float(x) for x in s],
    )
