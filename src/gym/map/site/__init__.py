"""The map site: a Concept graph (the front door) and Bertin's matrix.

`main(map_dir, out)` writes one self-contained HTML file -- no server, no
CDN, no stored state, opens from file://.

    load.py       YAML in; canonical Concepts, derived edges, panel payload
    community.py  Louvain on the weighted Concept graph
    graph.py      the Concept graph view: data, CSS, JS
    matrix.py     Bertin's reorderable matrix, moved unchanged from the
                  single-file site.py
    page.py       assembly: skeleton, header, view switch, shared JS
"""

from __future__ import annotations

from gym.map.site.page import main

__all__ = ["main"]
