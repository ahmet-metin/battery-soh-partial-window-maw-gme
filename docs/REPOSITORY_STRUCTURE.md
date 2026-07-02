# Repository structure

- `notebooks/`: cleaned notebooks with outputs and execution metadata removed.
- `results/`: feature tables, summary CSVs, detailed per-fold outputs, BMS replay outputs, and generated figures.
- `environment/`: Colab environment report and package version table.
- `scripts/make_summary_tables.py`: creates compact manuscript summary tables from the committed results.
- `outputs/`: generated compact tables useful for README/manuscript checking.

The original notebooks were executed in Google Colab with Google Drive paths. For local or new Colab execution, update the path constants near the beginning of each notebook or clone the repository into the expected working directory and adjust `BASE_DIR`/`RESULT_DIR` values.
