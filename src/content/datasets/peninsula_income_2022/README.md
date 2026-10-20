# Peninsular Malaysia income display snapshot

This snapshot supports the autocorrelation self-study section and notebook, covering **92 matched mapped areas** across Peninsular Malaysia. Most are administrative districts; Kuala Lumpur and Putrajaya each contribute one unit, Perlis contributes one state-level observation, and the source includes Kecil Lojing. It is not a neighbourhood dataset.

## Sources and retrieval

- **Income:** Department of Statistics Malaysia, [Household Income by Administrative District](https://open.dosm.gov.my/data-catalogue/hh_income_district), downloaded from <https://storage.dosm.gov.my/hies/hh_income_district.csv>. The table is released under CC BY 4.0. Retain DOSM attribution.
- **Boundaries:** PLANMalaysia [Sempadan Daerah service](https://gisdev.planmalaysia.gov.my/server/rest/services/Hosted/Data_Sempadan_Daerah/FeatureServer/0), queried on 20 October 2026. The notebook and `snapshot.json` record the complete query, including the exclusion of state codes 12, 13 and 15 (Sabah, Sarawak and Labuan), `outSR=3375`, `maxAllowableOffset=100` and `geometryPrecision=1`. The income table's licence does not automatically apply to the boundary data; retain PLANMalaysia attribution.
- `snapshot.json` contains SHA-256 values for the exact income CSV and decompressed boundary JSON. Both are verified when the notebook uses this snapshot.

`hh_income_district.csv` is the complete small downloaded table; the notebook selects the peninsula and a single common year. `boundaries_rso_display.json.gz` losslessly compresses the **generalized API response**, not the full-detail source geometries. The compressed display layer is about 195 KiB, avoiding a 23 MiB full-detail response for a map-only demonstration.

## Display geometry and projection

Coordinates are **GDM2000 / Peninsula RSO (EPSG:3375)**, in metres. The map uses equal x/y scale. Outlines are generalized by the source service at 100 m and coordinates are returned to one decimal metre. The notebook preserves all rings returned in that display response and does not sketch-distort geographic polygons.

These generalized outlines are **for plotting, not for deriving exact shared-border weights or measuring fine-scale boundaries**. Obtain the full-detail geometry (omit `maxAllowableOffset` and `geometryPrecision`) and verify topology before an adjacency analysis. No spatial autocorrelation statistic or p-value for the Malaysian data is calculated by this notebook.

The income reference year is 2022; boundary retrieval in 2026 is not a reconstruction of 2022 administrative geography. Verify historical boundary changes and area definitions for substantive analysis.

## Values, joins and permutations

Published figures use `income_median`: **median gross monthly household income in 2022, in nominal RM**. `income_mean` is an alternative. These are within-area household summaries, not individual salaries, annual income, land values or a combined regional household median.

Join on state and district and validate one-to-one matches. Explicit aliases reconcile Ulu/Hulu spellings, federal-territory prefixes, Perlis/Kangar, Kecil Lojing/Lojing, Larut dan Matang/Larut & Matang, and Timur Laut/Timor Laut. All 92 income values must match. Missing records are not imputed, different years are not mixed, and areas are not silently dropped. The current snapshot has incomplete peninsula coverage in 2024, so that selection is rejected.

Use **OrRd**, a sequential cream–orange–dark-red palette, with fixed breaks `[0, 3000, 5000, 7000, 9000, 15000]`. Available 2022 values are all within this range; the upper displayed class begins at RM 9,000. Every panel shares the same classification. `YlOrBr` offers a more golden alternative, and `CLASS_BREAKS=None` enables exploratory quantile classes.

The seed is 5230. Each permutation independently reassigns the same 92 values to the fixed units. Neither household-level distributions nor geographical locations are resimulated. Synthetic binary grids and the four-area chain are separate teaching examples.

## Reproduction and layouts

Open `src/content/notebooks/lab-08-autocorrelation-self-study.ipynb`. In the repository it locates this snapshot; standalone use can download the official sources directly. Set `USE_BOOK_SNAPSHOT=False` to select live sources explicitly. The settings record identifies the source route, fingerprints, palette, breaks, projection and display generalization.

Run `python scripts/check_autocorrelation_pilot.py` for offline validation, or add `--write-figures` to regenerate the four chapter illustrations. Requirements: NumPy, pandas, Matplotlib, IPython and nbformat; the existing Comic Neue font supplies optional xkcd lettering.

The observed map has a portrait canvas, the observed/permuted comparison has two columns, and the three-permutation figure has three columns. Repeated headings are removed, a single legend is shared within each figure, and PNGs are exported at 200 dpi. The chapter limits the standalone portrait's display width while allowing the comparisons to fill the content column. Map proportions are never stretched.
