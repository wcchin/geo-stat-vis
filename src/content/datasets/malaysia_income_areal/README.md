# Peninsular Malaysia: shared areal income analysis

This dataset connects Chapter 6's observed income map, global Moran's I, Local Moran, Geary and Getis–Ord examples. FIRMS remains the separate point-event application in Chapter 4.

## Observation and sources

Use DOSM's **2022 median gross monthly household income**, in nominal RM, by household residence. All 92 matched mapped areas are retained: most are administrative districts, with one observation each for Perlis, Kuala Lumpur and Putrajaya, and a Kecil Lojing unit. Each area receives one observation weight. This is not a population-weighted household analysis, and averaging the district medians does not recover the peninsula's household median.

Income source: [DOSM catalogue](https://open.dosm.gov.my/data-catalogue/hh_income_district), downloaded CSV in [peninsula_income_2022](../peninsula_income_2022/README.md), CC BY 4.0. Explicit aliases match state/district identifiers one-to-one. Missing values are not imputed and no area is dropped for its income value. Household survey uncertainty is not propagated through these illustrative tests.

Boundary source: [PLANMalaysia district service](https://gisdev.planmalaysia.gov.my/server/rest/services/Hosted/Data_Sempadan_Daerah/FeatureServer/0). Retrieve full detail in EPSG:3375 on 21 October 2026, omitting maxAllowableOffset and geometryPrecision. `geometry_audit.json` records the exact query, raw response SHA-256, topology diagnostics and representative-point method. The 23,278,127-byte source response is not bundled; all 92 derived representative coordinates and both graph edge lists are saved for compact offline reproduction. The optional preparation script re-fetches/cache-checks the full response and stops if its checksum differs from the recorded version.

The existing generalized boundaries remain **display-only**, with their own verified snapshot. Maps use equal x/y scale, preserve rings and do not sketch-distort geometry. The 2026 boundary retrieval is not a reconstruction of 2022 geography. The income licence does not automatically license boundary data; retain both source attributions.

## Geometry audit and weights

The full-detail query has 92 geometries. Polygon construction respects clockwise Esri shells and counterclockwise holes; source rings pass through make_valid before union. Six pair overlaps exceed 1 m², including a roughly 0.309 km² Kangar/Kubang Pasu overlap. The resulting rook graph has four components and isolates Kangar and Langkawi; queen has three components and isolates Langkawi. These diagnostics are not a claim that all nominal contacts are topologically correct.

To retain all 92 units without silently adding contiguity links or dropping islands, choose **symmetric union 4NN** before calculating association. Use an interior representative point from each full geometry, metric distance in EPSG:3375, and stable index ordering for ties. Connect a pair if either point selects the other, then row-standardise for I/C. The primary graph has 226 undirected links, one component, no isolates, and degrees 4–9. Median link length is 36.65 km; the maximum is 90.47 km. Interior points are geometric representatives, not population centres. Links may cross water or barriers and do not represent journeys or economic influence.

Sensitivity: symmetric union 6NN on the same observations, 333 edges, degrees 6–11, maximum link 110.53 km, one component. Its outputs are reported rather than used to select a favourable result. General G uses binary versions of these graphs; Gi* additionally includes self weight 1. Those conventions differ explicitly from row-standardised I/C.

## Inference and classification

Use 9,999 unrestricted permutations for global I/C/G with seed 5230; report upper tails for I/G and lower for C. The fixed graph and set of values are unchanged. Local tests hold the focal value fixed and sample k distinct other indices without replacement. Distinct indices may have equal values. The same draws per focal area are used for Local Moran, Local Geary and Gi*.

Inclusive plus-one lower/upper tails treat floating equality with relative/absolute tolerance 1e-12. Local two-sided p is min(1, 2 min(p_lower,p_upper)), minimum 0.0002. Apply BH separately within each 92-test method family; provide Bonferroni counts as a family-wise comparison. BH is exploratory under dependent spatial tests, not guaranteed under arbitrary dependence. Adjusted q-values are not posterior probabilities that particular findings are false.

Local Moran uses population-standardised z_i times its row-standardised spatial lag. Local Geary uses sum_j w_ij (z_i-z_j)^2 and classifies departures below/above its conditional mean as Similar/Dissimilar. Gi* uses binary neighbour-plus-self sums divided by the regional total, classified above/below its conditional mean as Hot/Cold. Gstar_z_perm is conditional simulation standardisation, not the usual analytical unconditional Gi* score.

Under equal neighbour weights and fixed focal value, Local Moran (nonzero deviation) and Gi* are affine functions of the same neighbour sum. Their doubled-tail p-values coincide here; agreement is not independent confirmation. Their interpretations differ, illustrated by Bentong's unadjusted LH versus high-sum configurations.

## Files and reproduction

- `observations.csv`: 92 named areas, income variable, alternative mean income, and full-detail-derived representative coordinates; preserve string IDs including leading zeros.
- `edges.csv`: undirected union-4NN and union-6NN edge lists and metric lengths.
- `geometry_audit.json`: source fingerprints, query and geometry/graph diagnostics.
- `cell_results.csv`: values, graph degrees, lags, local statistics, both tails, doubled-tail p-values and BH q-values.
- `analysis.json`: equations/conventions and primary/sensitivity results.

Run `python scripts/malaysia_income_analysis.py` from the repository, or add `--check` to compare the saved results. Dependencies: NumPy, pandas, SciPy and Matplotlib. `scripts/areal_statistics.py` implements the shared equations explicitly; esda defaults and version-specific category codes are not used. `scripts/prepare_malaysia_income_geometry.py` is the optional network preparation/audit step and additionally requires Shapely. It does not run in CI.

The [self-study notebook](../../notebooks/malaysia-income-areal-self-study.ipynb) embeds the same implementation, uses the compact snapshots and can download them from the public repository without Google Drive. Observed income uses sequential OrRd with the established fixed breaks. Local results use categorical orange/purple/gold/teal; grey means not selected, not zero or missing income.
