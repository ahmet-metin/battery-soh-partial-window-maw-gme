#!/usr/bin/env python3
"""Regenerate compact manuscript summary tables from committed CSV result files."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

DATASETS = {
    "Dataset 1 NMC/UofM": ROOT / "results" / "dataset1_nmc" / "results",
    "Dataset 2 Oxford": ROOT / "results" / "dataset2_oxford" / "results",
    "Dataset 3 LFP/graphite": ROOT / "results" / "dataset3_lfp" / "results",
}

def read_summary(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    # First row is a second-level header in several exported CSVs.
    if len(df) and str(df.iloc[0].get("RMSE", "")).lower() == "mean":
        df = df.iloc[1:].reset_index(drop=True)
    for col in ["RMSE", "RMSE.1", "MAE", "MAE.1", "R2", "R2.1"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    if "exclude_outliers" in df.columns:
        df["exclude_outliers"] = df["exclude_outliers"].astype(str).str.lower().map({"false": False, "true": True})
    return df

rows = []
for dataset, base in DATASETS.items():
    single = read_summary(base / "single_hi_polynomial_ekf_summary_mean_std.csv")
    approx = read_summary(base / "approx_paper_gpr_ekf_summary_mean_std.csv")
    multi = read_summary(base / "multi_hi_tabular_summary_mean_std.csv")
    for label, df in [("Best controlled single-HI", single), ("Controlled approx. GPR/EKF", approx), ("Best fixed-window Multi-HI", multi)]:
        dff = df[df["exclude_outliers"] == False].copy()
        best = dff.loc[dff["RMSE"].idxmin()]
        rows.append({
            "dataset": dataset,
            "method": label,
            "window": best.get("window"),
            "model": best.get("model"),
            "rmse_mean": best.get("RMSE"),
            "rmse_std": best.get("RMSE.1"),
            "mae_mean": best.get("MAE"),
            "mae_std": best.get("MAE.1"),
            "r2_mean": best.get("R2"),
            "r2_std": best.get("R2.1"),
        })

main = pd.DataFrame(rows)
main.to_csv(OUT / "main_loco_summary.csv", index=False)

# Window-level single-HI versus multi-HI comparison.
win_rows = []
for dataset, base in DATASETS.items():
    p = base / "single_hi_vs_best_multi_hi_summary.csv"
    if p.exists():
        df = pd.read_csv(p)
        df = df[df["exclude_outliers"] == False].copy()
        df.insert(0, "dataset", dataset)
        win_rows.append(df)
if win_rows:
    pd.concat(win_rows, ignore_index=True).to_csv(OUT / "window_level_single_vs_multi.csv", index=False)

# BMS runtime summaries.
bms_rows = []
for dataset, base in DATASETS.items():
    p = base / "bms_online_results" / "full_model_pool_runtime_review" / "bms1_full_model_pool_runtime_summary.csv"
    if p.exists():
        df = pd.read_csv(p)
        if "dataset" in df.columns:
            df["source_dataset"] = dataset
        else:
            df.insert(0, "dataset", dataset)
        bms_rows.append(df)
if bms_rows:
    pd.concat(bms_rows, ignore_index=True).to_csv(OUT / "bms1_runtime_summary.csv", index=False)

print("Wrote:")
for path in sorted(OUT.glob("*.csv")):
    print(f" - {path.relative_to(ROOT)}")
