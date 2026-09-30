"""Communities on the weighted Concept graph: Louvain, written out here.

No third-party graph library is a dependency of gym, and none is added for
this: the algorithm is Blondel et al. (2008) modularity optimisation, about
a hundred lines on a graph this size.

Determinism is structural, not seeded. Every loop walks a sorted list, every
tie breaks on the id, and nothing samples. The same input always yields the
same partition, so the page's colours do not move between builds.
"""

from __future__ import annotations

from collections import defaultdict


def _one_level(
    nodes: list[str],
    adj: dict[str, dict[str, float]],
    total_weight: float,
    resolution: float,
) -> dict[str, str]:
    """One Louvain level: move each node to its best neighbouring community."""
    community = {n: n for n in nodes}
    # strength = sum of incident edge weights (self-loops counted twice)
    strength = {n: sum(adj[n].values()) + adj[n].get(n, 0.0) for n in nodes}
    comm_strength = dict(strength)
    m2 = 2.0 * total_weight
    if m2 == 0:
        return community

    improved = True
    while improved:
        improved = False
        for n in nodes:
            own = community[n]
            comm_strength[own] -= strength[n]
            # weight from n into each neighbouring community
            into: dict[str, float] = defaultdict(float)
            into[own] += 0.0
            for nb, w in adj[n].items():
                if nb == n:
                    continue
                into[community[nb]] += w
            best, best_gain = own, into[own] - resolution * comm_strength[own] * strength[n] / m2
            for cand in sorted(into):
                gain = into[cand] - resolution * comm_strength[cand] * strength[n] / m2
                if gain > best_gain + 1e-12 or (
                    abs(gain - best_gain) <= 1e-12 and cand < best
                ):
                    best, best_gain = cand, gain
            comm_strength[best] += strength[n]
            if best != own:
                community[n] = best
                improved = True
    return community


def louvain(
    nodes: list[str],
    edges: dict[tuple[str, str], float],
    resolution: float = 1.0,
    max_levels: int = 12,
) -> dict[str, int]:
    """Concept id -> community index, indices assigned by community size."""
    nodes = sorted(nodes)
    total_weight = sum(edges.values())
    membership = {n: n for n in nodes}

    cur_nodes = nodes
    cur_edges = dict(edges)
    for _ in range(max_levels):
        adj: dict[str, dict[str, float]] = {n: defaultdict(float) for n in cur_nodes}
        for (a, b), w in cur_edges.items():
            if a == b:
                adj[a][a] += w
            else:
                adj[a][b] += w
                adj[b][a] += w
        part = _one_level(cur_nodes, adj, total_weight, resolution)
        # relabel: community id = smallest member id, for determinism
        groups: dict[str, list[str]] = defaultdict(list)
        for n in cur_nodes:
            groups[part[n]].append(n)
        rename = {old: min(members) for old, members in groups.items()}
        part = {n: rename[part[n]] for n in cur_nodes}
        if len(set(part.values())) == len(cur_nodes):
            break
        membership = {n: part[membership[n]] for n in nodes}
        next_nodes = sorted(set(part.values()))
        next_edges: dict[tuple[str, str], float] = defaultdict(float)
        for (a, b), w in cur_edges.items():
            ca, cb = part[a], part[b]
            key = (ca, cb) if ca <= cb else (cb, ca)
            next_edges[key] += w
        if len(next_nodes) == len(cur_nodes):
            break
        cur_nodes, cur_edges = next_nodes, dict(next_edges)

    sizes: dict[str, int] = defaultdict(int)
    for n in nodes:
        sizes[membership[n]] += 1
    order = sorted(sizes, key=lambda c: (-sizes[c], c))
    index = {c: i for i, c in enumerate(order)}
    return {n: index[membership[n]] for n in nodes}


def cap_communities(
    membership: dict[str, int],
    edges: dict[tuple[str, str], float],
    cap: int,
) -> dict[str, int]:
    """Fold the smallest communities into their strongest neighbour, until `cap`.

    A legend a reader can scan is the point; Louvain on this data returns
    far more communities than that. The smallest community is merged into
    whichever other community it shares the most edge weight with, ties on
    the smaller community index; a community with no outside edge at all is
    left alone, so the result can exceed `cap` and the caller reports the
    number it actually got.
    """
    membership = dict(membership)
    while True:
        members: dict[int, list[str]] = defaultdict(list)
        for n, c in membership.items():
            members[c].append(n)
        if len(members) <= cap:
            break
        between: dict[int, dict[int, float]] = defaultdict(lambda: defaultdict(float))
        for (a, b), w in edges.items():
            ca, cb = membership[a], membership[b]
            if ca != cb:
                between[ca][cb] += w
                between[cb][ca] += w
        candidates = sorted(members, key=lambda c: (len(members[c]), c))
        moved = False
        for c in candidates:
            if not between.get(c):
                continue
            target = min(sorted(between[c]), key=lambda t: (-between[c][t], t))
            for n in members[c]:
                membership[n] = target
            moved = True
            break
        if not moved:
            break

    sizes: dict[int, int] = defaultdict(int)
    for c in membership.values():
        sizes[c] += 1
    order = sorted(sizes, key=lambda c: (-sizes[c], c))
    index = {c: i for i, c in enumerate(order)}
    return {n: index[c] for n, c in membership.items()}


def modularity(
    membership: dict[str, int], edges: dict[tuple[str, str], float]
) -> float:
    m = sum(edges.values())
    if m == 0:
        return 0.0
    inside: dict[int, float] = defaultdict(float)
    strength: dict[str, float] = defaultdict(float)
    for (a, b), w in edges.items():
        strength[a] += w
        strength[b] += w
        if membership[a] == membership[b]:
            inside[membership[a]] += w
    comm_strength: dict[int, float] = defaultdict(float)
    for n, s in strength.items():
        comm_strength[membership[n]] += s
    return sum(
        inside[c] / m - (comm_strength[c] / (2 * m)) ** 2 for c in comm_strength
    )


def fold_islands(
    membership: dict[str, int], edges: dict[tuple[str, str], float]
) -> tuple[dict[str, int], int | None]:
    """Put every community with no edge leaving it into one shared bucket.

    This map is one body of 887 Concepts plus 123 small detached fragments.
    Louvain calls each fragment a community of its own, which is true and
    useless: a legend of 124 rows is not read at a glance, and no merge by
    edge weight can ever join a fragment to anything, because it has no
    outside edge. They are collected under one identity instead, and the
    legend says what they are rather than listing them.

    Returns the new membership and the bucket's community id, or None when
    no community was isolated.
    """
    external: dict[int, float] = defaultdict(float)
    for (a, b), w in edges.items():
        if membership[a] != membership[b]:
            external[membership[a]] += w
            external[membership[b]] += w
    isolated = sorted({c for c in set(membership.values()) if external.get(c, 0.0) == 0.0})
    if len(isolated) < 2:
        return dict(membership), (isolated[0] if isolated else None)
    target = isolated[0]
    keep = set(isolated)
    out = {n: (target if c in keep else c) for n, c in membership.items()}
    return out, target
