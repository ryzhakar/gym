# Closure — threshold 10%

| stratum | n1 | n2 | m | seen | Chapman N̂ | Chapman unseen % | 95% CI | Chao1 N̂ | Chao1 unseen % | 95% CI | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cloud-workers | 23 | 14 | 6 | 31 | 50.4 | 38.5% | [28.5, 72.3] | 88.6 | 65.0% | [18.6, 158.6] | FAIL |
| core | 112 | 92 | 21 | 183 | 476.7 | 61.6% | [323.6, 629.8] | 691.9 | 73.6% | [425.0, 958.8] | FAIL |
| decentralized-iroh | 15 | 22 | 4 | 33 | 72.6 | 54.5% | [29.4, 115.8] | 81.0 | 59.3% | [25.0, 137.0] | FAIL |
| desktop-cli-ui | 29 | 20 | 4 | 45 | 125.0 | 64.0% | [44.7, 205.3] | 197.1 | 77.2% | [31.3, 362.9] | FAIL |
| distributed | 25 | 23 | 6 | 42 | 88.1 | 52.4% | [43.7, 132.6] | 115.1 | 63.5% | [39.1, 191.2] | FAIL |
| embedded | 33 | 32 | 5 | 60 | 186.0 | 67.7% | [72.3, 299.7] | 816.2 | 92.6% | [-306.8, 1939.3] | FAIL |
| frontend | 15 | 15 | 2 | 28 | 84.3 | 66.8% | [16.4, 152.3] | 366.0 | 92.3% | [-346.5, 1078.5] | FAIL |
| ml | 20 | 24 | 5 | 39 | 86.5 | 54.9% | [38.7, 134.3] | 175.1 | 77.7% | [11.0, 339.3] | FAIL |
| other | 7 | 17 | 2 | 22 | 47.0 | 53.2% | [13.1, 80.9] | 50.9 | 56.8% | [12.1, 89.7] | FAIL |
| swift-interop | 4 | 4 | 0 | 8 | 24.0 | 66.7% | [-3.7, 51.7] | 32.5 | 75.4% | [-28.5, 93.5] | FAIL |
| wasm | 25 | 33 | 3 | 55 | 220.0 | 75.0% | [52.6, 387.4] | 455.2 | 87.9% | [-51.6, 961.9] | FAIL |
| web | 30 | 19 | 4 | 45 | 123.0 | 63.4% | [44.3, 201.7] | 325.2 | 86.2% | [-36.8, 687.1] | FAIL |

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
