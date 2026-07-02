# GitHub release checklist

Before making the repository public:

1. Replace `https://github.com/REPLACE_WITH_USERNAME/...` in `CITATION.cff` with the final repository URL.
2. Confirm the license choice. The current package uses MIT for code.
3. Confirm that raw dataset files are not committed. Keep raw downloads under `raw_data/` or outside the repository.
4. Re-run `python scripts/make_summary_tables.py` and check `outputs/`.
5. Add a repository description, topics, and a release tag on GitHub after upload.
6. If the paper has a preprint or DOI, add it to `README.md` and `CITATION.cff`.

Suggested repository topics:

`battery-soh`, `lithium-ion-battery`, `incremental-capacity-analysis`, `partial-charging`, `machine-learning`, `battery-management-system`, `state-of-health`, `ensemble-learning`
