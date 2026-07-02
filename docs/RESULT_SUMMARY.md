# Result summary

This file provides a compact overview of the stored experiment outputs. Full per-fold and per-scenario CSV/XLSX files are available under `results/`.

## Main LOCO comparison

| Dataset | Best controlled single-HI RMSE | Controlled approx. GPR/EKF RMSE | Best fixed-window Multi-HI RMSE |
|---|---:|---:|---:|
| Dataset 1 NMC/UofM | 0.0175 | 0.0194 | 0.0104 |
| Dataset 2 Oxford | 0.0085 | 0.0127 | 0.0043 |
| Dataset 3 LFP/graphite | 0.0117 | 0.0156 | 0.0023 |

## Key BMS-1 online replay observations

- Dataset 1: TopK-MAW-GME-K5 gives the lowest BMS-1 RMSE among the reported deployment choices.
- Dataset 2: TopK-MAW-GME-K3 gives the best compact accuracy-latency-memory trade-off.
- Dataset 3: TopK-MAW-GME-K5 gives the lowest BMS-1 RMSE, while the best single estimator remains lower-latency.

## Stress-test interpretation

The BMS-3 stress tests are intended to separate missing-window robustness from feature-family sensitivity. When the best fixed voltage window is unavailable, the single fixed-window estimator loses measurement-update capability, whereas TopK-MAW-GME can continue updating through alternative retained experts. Feature-family removal is more severe and identifies chemistry-dependent critical HI groups.

Run the following command to regenerate compact CSV summaries from the stored result files:

```bash
python scripts/make_summary_tables.py
```
