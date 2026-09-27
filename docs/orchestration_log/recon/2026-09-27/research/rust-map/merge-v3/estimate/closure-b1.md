# Closure — threshold 10%

| stratum | n1 | n2 | m | seen | Chapman N̂ | Chapman unseen % | 95% CI | Chao1 N̂ | Chao1 unseen % | 95% CI | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cloud-workers | 30 | 17 | 9 | 38 | 54.8 | 30.7% | [36.7, 72.9] | 94.3 | 59.7% | [30.1, 158.6] | FAIL |
| core | 121 | 123 | 34 | 210 | 431.2 | 51.3% | [330.2, 532.2] | 575.7 | 63.5% | [405.6, 745.8] | FAIL |
| decentralized-iroh | 23 | 28 | 10 | 41 | 62.3 | 34.2% | [41.5, 83.0] | 63.0 | 34.9% | [38.7, 87.3] | FAIL |
| desktop-cli-ui | 29 | 25 | 10 | 44 | 69.9 | 37.1% | [45.7, 94.2] | 129.3 | 66.0% | [37.2, 221.5] | FAIL |
| distributed | 34 | 40 | 15 | 59 | 88.7 | 33.5% | [64.2, 113.2] | 128.1 | 54.0% | [66.3, 189.9] | FAIL |
| embedded | 49 | 37 | 16 | 70 | 110.8 | 36.8% | [79.6, 141.9] | 188.2 | 62.8% | [90.5, 285.9] | FAIL |
| frontend | 15 | 15 | 5 | 25 | 41.7 | 40.0% | [21.9, 61.4] | 225.0 | 88.9% | [-205.3, 655.3] | FAIL |
| ml | 21 | 29 | 8 | 42 | 72.3 | 41.9% | [43.1, 101.6] | 138.1 | 69.6% | [28.4, 247.8] | FAIL |
| other | 11 | 17 | 6 | 22 | 29.9 | 26.3% | [19.1, 40.6] | 59.5 | 63.0% | [1.3, 117.7] | FAIL |
| swift-interop | 6 | 4 | 2 | 8 | 10.7 | 25.0% | [5.2, 16.1] | 20.5 | 61.0% | [-13.1, 54.1] | FAIL |
| wasm | 43 | 44 | 16 | 71 | 115.5 | 38.5% | [82.2, 148.7] | 160.3 | 55.7% | [89.7, 230.9] | FAIL |
| web | 40 | 29 | 12 | 57 | 93.6 | 39.1% | [62.8, 124.4] | 145.9 | 60.9% | [63.7, 228.0] | FAIL |

## Five-part rule, per stratum
- cloud-workers: 1=FAIL 2=FAIL 3=FAIL 4=PASS 5=N/A (recomputed fresh every run) -> FAIL
- core: 1=FAIL 2=FAIL 3=FAIL 4=PASS 5=N/A (recomputed fresh every run) -> FAIL
- decentralized-iroh: 1=FAIL 2=FAIL 3=FAIL 4=PASS 5=N/A (recomputed fresh every run) -> FAIL
- desktop-cli-ui: 1=FAIL 2=FAIL 3=FAIL 4=PASS 5=N/A (recomputed fresh every run) -> FAIL
- distributed: 1=FAIL 2=FAIL 3=FAIL 4=PASS 5=N/A (recomputed fresh every run) -> FAIL
- embedded: 1=FAIL 2=FAIL 3=FAIL 4=PASS 5=N/A (recomputed fresh every run) -> FAIL
- frontend: 1=FAIL 2=FAIL 3=FAIL 4=PASS 5=N/A (recomputed fresh every run) -> FAIL
- ml: 1=FAIL 2=FAIL 3=FAIL 4=PASS 5=N/A (recomputed fresh every run) -> FAIL
- other: 1=FAIL 2=FAIL 3=FAIL 4=PASS 5=N/A (recomputed fresh every run) -> FAIL
- swift-interop: 1=FAIL 2=FAIL 3=FAIL 4=FAIL 5=N/A (recomputed fresh every run) -> FAIL
- wasm: 1=FAIL 2=FAIL 3=FAIL 4=PASS 5=N/A (recomputed fresh every run) -> FAIL
- web: 1=FAIL 2=FAIL 3=FAIL 4=PASS 5=N/A (recomputed fresh every run) -> FAIL
