# Closure — threshold 10%

| stratum | n1 | n2 | m | seen | Chapman N̂ | Chapman unseen % | 95% CI | Chao1 N̂ | Chao1 unseen % | 95% CI | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cloud-workers | 26 | 21 | 14 | 33 | 38.6 | 14.5% | [31.3, 45.9] | 51.3 | 35.7% | [27.3, 75.3] | FAIL |
| core | 100 | 87 | 41 | 146 | 210.6 | 30.7% | [175.7, 245.6] | 290.6 | 49.8% | [207.0, 374.3] | FAIL |
| decentralized-iroh | 27 | 29 | 17 | 39 | 45.7 | 14.6% | [37.7, 53.6] | 47.9 | 18.6% | [35.7, 60.1] | FAIL |
| desktop-cli-ui | 30 | 29 | 18 | 41 | 47.9 | 14.5% | [39.9, 56.0] | 68.6 | 40.2% | [36.5, 100.6] | FAIL |
| distributed | 29 | 32 | 18 | 43 | 51.1 | 15.9% | [42.1, 60.1] | 61.0 | 29.6% | [39.6, 82.5] | FAIL |
| embedded | 38 | 34 | 22 | 50 | 58.3 | 14.3% | [49.4, 67.3] | 94.6 | 47.2% | [44.7, 144.5] | FAIL |
| frontend | 14 | 15 | 9 | 20 | 23.0 | 13.0% | [18.0, 28.0] | 80.5 | 75.2% | [-58.8, 219.8] | FAIL |
| ml | 23 | 24 | 15 | 32 | 36.5 | 12.3% | [30.3, 42.7] | 51.6 | 38.0% | [23.5, 79.7] | FAIL |
| other | 14 | 17 | 12 | 19 | 19.8 | 3.9% | [17.7, 21.9] | 31.2 | 39.2% | [5.5, 57.0] | FAIL |
| swift-interop | 7 | 4 | 4 | 7 | 7.0 | 0.0% | [7.0, 7.0] | undefined (f2=0) | undefined | undefined | FAIL |
| wasm | 26 | 29 | 12 | 43 | 61.3 | 29.9% | [43.6, 79.0] | 103.8 | 58.6% | [35.2, 172.3] | FAIL |
| web | 30 | 28 | 16 | 42 | 51.9 | 19.0% | [41.3, 62.4] | 76.6 | 45.1% | [36.3, 116.9] | FAIL |

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
