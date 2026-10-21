# Shared South Sumatra areal analysis

This record supports Sections 6.3–6.6. Input: the compact September 2026 NASA FIRMS mirror snapshot in [firms_sumatra](../firms_sumatra/README.md), nominal/high-confidence S-NPP VIIRS, version 2.0NRT. That source record includes query provenance and limitations; September observations were not independently checked against the authenticated NASA archive. The 6,201 input rows are satellite detections, not separate fires.

## Support and variable

Aggregate the two adjacent 100 km windows into 50 cells, 20 km per side, EPSG:32748. Count rows south-to-north (R1–R5) and columns west-to-east (C01–C10). Retain only cells whose saved Natural Earth main-island land area equals 400 km² within 1e-6 km². Exclude R5C07 (32 detections; 356.51 km² land) and R5C08 (72; 399.21 km²). This leaves 48 observations, 6,097 detections and 19,200 km² grid area. Full-land status is relative to generalized coastline geometry. Do not confuse these approximate land areas with survey geometry.

This deliberately differs from Chapter 4's area-adjusted quadrat comparison, which retained both coastal cells. All 48 cells are kept regardless of their detection count; no zero-count cell is removed by a count-based rule. Windows were selected after exploratory inspection and tests are illustrative. Counts do not adjust for clouds, overpass opportunities, repeated burning or land suitability.

## Graph, statistics and inference

Primary graph: first-order rook, 80 undirected edges, no isolates, one component; 2–4 neighbours. Queen sensitivity: same observations, 148 edges, 3–8 neighbours. Never recompute a graph after a permutation.

- Global I/C use row-standardised weights and the exact equations on the pages. Global General G uses binary weights on the same graph, no diagonal. Permute all values, 9,999 draws, seed 5230. Report upper tails for I/G and lower for C.
- Local Moran uses population-moment scaling: z_i times its row-standardised lag. Local Geary is sum_j w_ij (z_i-z_j)^2. Do not assume a software-specific numeric label scheme.
- Local Gi* uses binary neighbours with self weight 1. Hold the focal value fixed and sample k distinct other indices without replacement for the neighbour slots. Other distinct indices may carry identical numerical values. All three local summaries use the same draws per focal location.
- Floating equality of theoretically tied statistics uses relative/absolute tolerance 1e-12. Inclusive lower/upper tails use (exceedances+1)/(B+1). Two-sided p is min(1, 2 min(p_lower,p_upper)); minimum 0.0002. BH adjustments are calculated separately for each 48-test family. BH is exploratory under spatial dependence, not guaranteed under arbitrary dependence. Bonferroni results are included for a family-wise comparison. Comparing methods and specifications also raises selection issues not solved by within-map adjustment.
- Local Geary category refers to observed c below/above its simulated conditional mean (Similar/Dissimilar); Gi* similarly uses Hot/Cold. These are not signs of the raw statistics. Gstar_z_perm is conditional simulation standardisation, not the usual analytical unconditional Gi* z-score.
- With fixed focal value and equal neighbour weights, Local Moran (nonzero focal deviation) and Gi* are affine functions of the same neighbour sum. Their doubled-tail ranks coincide in this implementation; agreement is not independent corroboration.

## Files and reproduction

`grid_support.csv` records all 50 cells including exclusions. `cell_results.csv` contains the 48 retained counts, lags, local statistics, both tails, doubled-tail p-values and BH q-values. `analysis.json` records the source checksum, package versions, graph diagnostics, global outputs, local-selection counts and queen sensitivity. No missing, excluded and non-significant categories are conflated.

Run `python scripts/firms_areal_analysis.py` from the repository to regenerate results and five original SVG figures. Run with `--check` to reproduce and compare the saved outputs. Dependencies: Python, NumPy, pandas, SciPy and Matplotlib; esda/libpysal are not required by this explicit implementation. Equations are stated in the chapter. The self-study notebook embeds the same code and accepts a local repository or downloads the compact public inputs after merging. It does not mount Google Drive.

Observed counts use sequential OrRd; local results use categorical orange/purple/gold/teal with grey non-selection and hatching for exclusions. The geometry is not sketch-distorted. Original code follows the repository code licence; source data retain their original attribution.
