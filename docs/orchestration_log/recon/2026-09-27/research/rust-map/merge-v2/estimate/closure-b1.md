# Closure — threshold 10%

| stratum | n1 | n2 | m | seen | Chapman N̂ | Chapman unseen % | 95% CI | Chao1 N̂ | Chao1 unseen % | 95% CI | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cloud-workers | 27 | 21 | 14 | 34 | 40.1 | 15.1% | [32.3, 47.8] | 54.6 | 37.8% | [28.2, 81.1] | FAIL |
| core | 103 | 88 | 42 | 149 | 214.3 | 30.5% | [179.2, 249.3] | 305.7 | 51.3% | [215.2, 396.3] | FAIL |
| decentralized-iroh | 27 | 29 | 17 | 39 | 45.7 | 14.6% | [37.7, 53.6] | 47.9 | 18.6% | [35.7, 60.1] | FAIL |
| desktop-cli-ui | 31 | 30 | 18 | 43 | 51.2 | 16.0% | [42.1, 60.3] | 80.8 | 46.8% | [37.4, 124.2] | FAIL |
| distributed | 29 | 33 | 18 | 44 | 52.7 | 16.5% | [43.2, 62.1] | 60.4 | 27.2% | [41.0, 79.8] | FAIL |
| embedded | 38 | 35 | 22 | 51 | 60.0 | 15.1% | [50.6, 69.4] | 118.6 | 57.0% | [38.2, 199.0] | FAIL |
| frontend | 14 | 16 | 9 | 21 | 24.5 | 14.3% | [18.9, 30.1] | undefined (f2=0) | undefined | undefined | FAIL |
| ml | 25 | 24 | 16 | 33 | 37.2 | 11.4% | [31.4, 43.1] | 49.3 | 33.1% | [26.4, 72.3] | FAIL |
| other | 14 | 17 | 12 | 19 | 19.8 | 3.9% | [17.7, 21.9] | 43.5 | 56.3% | [-17.5, 104.5] | FAIL |
| swift-interop | 7 | 4 | 4 | 7 | 7.0 | 0.0% | [7.0, 7.0] | undefined (f2=0) | undefined | undefined | FAIL |
| wasm | 26 | 29 | 12 | 43 | 61.3 | 29.9% | [43.6, 79.0] | 115.9 | 62.9% | [29.9, 201.9] | FAIL |
| web | 31 | 30 | 17 | 44 | 54.1 | 18.7% | [43.5, 64.7] | 74.2 | 40.7% | [39.7, 108.8] | FAIL |

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
