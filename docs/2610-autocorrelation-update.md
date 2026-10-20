# Autocorrelation self-study section

Baseline: main commit `747a3c2dbd79d74dbfecbf5e253bbab67fde3e24`, after the original-figure PR #2 was merged.

## Content and scope

Replace the Chapter 6 opening slide outline with connected self-study prose at the existing URL and title. Add the actual 2022 Selangor–KL–Putrajaya income table and three reproducible maps; temporal versus spatial autocorrelation; a synthetic similarity/contrast figure; neighbour cross-products and a four-area worked example; spatial lags; random-label exchangeability versus point-process CSR; explicitly hypothetical Monte Carlo arithmetic; global/local distinctions; geographical limitations; and six self-checks with feedback.

The Malaysian maps replace the Milwaukee example in this section. Old resources and the Milwaukee generator are retained because other material or earlier records may still refer to them. The earlier figure-authorship register describes the preceding batch; this update's active figures and provenance are documented in `src/content/datasets/kl_income_2022/README.md`.

Add `lab-08-autocorrelation-self-study.ipynb` to the notebook collection, alongside the existing full spatial-autocorrelation lab. The companion supports median versus mean income, fixed classification across permutations, a changeable seed and style, source checksums and explicit area matching. A losslessly compressed boundary response and the small income table make the in-repository route reproducible offline. Standalone use can download live sources without Google Drive.

The region has only 11 units, and KL is one unit. No within-KL clustering, Moran coefficient or inferential result is asserted. Survey uncertainty, exchangeability and the mismatch between survey year and boundary retrieval date are explained. The synthetic chain sum is not presented as a normalised coefficient; the p-value arithmetic is labelled hypothetical.

## Validation

`python scripts/check_autocorrelation_pilot.py` runs all notebook code sequentially in one process using the snapshot and bundled font, verifies the table, CRS, permutation invariants and chain arithmetic, checks the mean-income option and rejects incomplete 2024 coverage. The notebook is validated against the nbformat schema. This does not require a socket-based Jupyter kernel. `--write-figures` regenerates the chapter plots.

The PR workflow adds these checks and a complete Jupyter Book HTML build without deployment. Figure inspection covers legibility, shared legends, unchanged geography and the synthetic-grid counts. Source Markdown is reviewed for equation conventions, hypothetical versus observed claims, citations and links.

The general Chapter 6 version/implementation audit (including Local Geary and Getis–Ord) remains a separate task. No weekly slide snapshot is rewritten by this change. The book still deploys only after a merge to main.
