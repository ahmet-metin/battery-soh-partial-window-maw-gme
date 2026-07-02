# Method overview

The workflow has four main stages:

1. **Partial-window feature extraction:** chemistry-specific voltage windows are used to extract IC, DVA, partial-charge time, partial-throughput, and temperature-related health indicators.
2. **Leakage-clean model training:** SoH, capacity, cell identifiers, and target-derived variables are removed from model inputs. Leave-one-cell-out validation is used for cross-cell evaluation.
3. **Controlled baselines:** single-HI polynomial/EKF-style baselines and an approximate Kadem-style GPR/EKF baseline are evaluated with the same folds and extracted features where possible.
4. **TopK-MAW-GME:** candidate window-model experts are ranked using inner-LOCO validation and a lightweight size-aware penalty. K3 and K5 deployment modes are evaluated for accuracy, runtime, memory, and missing-window robustness.

The BMS-oriented replay experiments are chronological simulation protocols in Python/Google Colab, not embedded hardware measurements.
