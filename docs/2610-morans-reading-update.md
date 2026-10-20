# Moran’s I reading update

Adapted from the approved review PDF v0.1 (20 October 2026). The existing page path and title remain unchanged. Replace six embedded teaching images with three original, reproducible figures. The complete reading covers measurement, weights, lag, arithmetic, scatterplots, randomisation, analytical output, interpretation, sensitivity and seven self-checks with feedback.

Equations use native MyST LaTeX. No September 2026 fire result is claimed or fabricated; the regional example remains explicitly proposed.

This page is for instructor review; the preceding pages are the proposed student reading. The final book version will place the regional evidence alongside the explanation, while keeping the four-cell example as a transparent arithmetic bridge.

| Original regional figure | Purpose and required checks |
| --- | --- |
| 1. Detections and grid counts | Two linked views of September 2026 Sumatra; show the time window, product, projected grid and zero-count land cells. OrRd counts, with a distinct outside-mask background. |
| 2. Values and spatial lag | Same extent, units, cell IDs and scale definition. Include a focal-cell inset showing exactly which neighbours enter the lag. |
| 3. Moran scatterplot | Use the actual standardised counts and their row-standardised lag; annotate n, weights and I. Mark quadrants without claiming local significance. |
| 4. Permutation reference | Use the same data and weights; show observed I, E[I], B, seed and explicitly right-tailed p-value. |
| 5. Sumatra / Kalimantan preview | Assess readability with separate map panels and shared count breaks where meaningful. Do not merge two disconnected regions into one test without justification. |

**Before inserting empirical results:** obtain and preserve the 2026 records; verify product coverage and confidence fields; document CRS, grid origin, coastal rule and isolated-cell handling; inspect all joins and counts; run the statistic and prespecified sensitivity checks; then write the result from the actual outputs. Regional observations and empirical figures remain a follow-up task; this change publishes the approved conceptual reading and original hypothetical examples.

Sources checked 20 October 2026. All figures in this review PDF are original calculations from the stated hypothetical dataset; no external teaching images are reproduced. The preparation notebook will pin software versions and retain source attribution.


## Validation

Run `python scripts/draw_morans_figures.py` to verify the row-standardised and binary statistics, slope identity, exact randomisation expectation and right-tail probability, affine invariance, and Monte Carlo arithmetic. Use `--write` to regenerate the SVG figures. GitHub checks run this script and the complete book build. All three figures have descriptive alternative text and unique labels. The six previous image files are retained for existing references elsewhere; this page no longer embeds them.
