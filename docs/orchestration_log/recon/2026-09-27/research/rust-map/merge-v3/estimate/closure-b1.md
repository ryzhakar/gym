# Closure — threshold 10%

| stratum | n1 | n2 | m | seen | Chapman N̂ | Chapman unseen % | 95% CI | Chao1 N̂ | Chao1 unseen % | 95% CI | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cloud-workers | 30 | 17 | 9 | 38 | 54.8 | 30.7% | [36.7, 72.9] | 94.3 | 59.7% | [30.1, 158.6] | FAIL |
| core | 122 | 123 | 36 | 209 | 411.2 | 49.2% | [319.4, 503.0] | 537.9 | 61.1% | [385.7, 690.0] | FAIL |
| decentralized-iroh | 23 | 28 | 10 | 41 | 62.3 | 34.2% | [41.5, 83.0] | 59.4 | 30.9% | [38.7, 80.0] | FAIL |
| desktop-cli-ui | 29 | 25 | 10 | 44 | 69.9 | 37.1% | [45.7, 94.2] | 129.3 | 66.0% | [37.2, 221.5] | FAIL |
| distributed | 34 | 39 | 15 | 58 | 86.5 | 32.9% | [62.8, 110.2] | 115.0 | 49.6% | [63.9, 166.2] | FAIL |
| embedded | 49 | 37 | 16 | 70 | 110.8 | 36.8% | [79.6, 141.9] | 188.2 | 62.8% | [90.5, 285.9] | FAIL |
| frontend | 16 | 16 | 7 | 25 | 35.1 | 28.8% | [22.6, 47.6] | 106.0 | 76.4% | [-30.1, 242.1] | FAIL |
| ml | 21 | 29 | 8 | 42 | 72.3 | 41.9% | [43.1, 101.6] | 117.0 | 64.1% | [34.7, 199.3] | FAIL |
| other | 11 | 17 | 6 | 22 | 29.9 | 26.3% | [19.1, 40.6] | 59.5 | 63.0% | [1.3, 117.7] | FAIL |
| swift-interop | 6 | 4 | 2 | 8 | 10.7 | 25.0% | [5.2, 16.1] | 20.5 | 61.0% | [-13.1, 54.1] | FAIL |
| wasm | 43 | 45 | 17 | 71 | 111.4 | 36.3% | [81.1, 141.8] | 151.0 | 53.0% | [88.1, 213.9] | FAIL |
| web | 41 | 28 | 13 | 56 | 86.0 | 34.9% | [60.1, 111.9] | 136.2 | 58.9% | [61.0, 211.4] | FAIL |

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
