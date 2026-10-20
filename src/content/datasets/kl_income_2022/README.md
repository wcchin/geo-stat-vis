# Selangor–KL–Putrajaya income illustration

This small snapshot supports the autocorrelation self-study section and notebook. It covers all nine Selangor administrative districts plus Kuala Lumpur and Putrajaya (11 units), a region broader than Greater KL. It is not a neighbourhood dataset.

## Sources and attribution

- **Income:** Department of Statistics Malaysia, [Household Income by Administrative District](https://open.dosm.gov.my/data-catalogue/hh_income_district), downloaded from <https://storage.dosm.gov.my/hies/hh_income_district.csv>. The catalogue makes this table available under CC BY 4.0. Preserve attribution to DOSM.
- **Boundaries:** PLANMalaysia, [Sempadan Daerah service](https://gisdev.planmalaysia.gov.my/server/rest/services/Hosted/Data_Sempadan_Daerah/FeatureServer/0). The notebook records the complete query: state codes 10, 14 and 16, district names and codes, full geometries, `outSR=32647`. Retain the service attribution; the income table's licence does not automatically apply to the boundaries.
- **Retrieval:** 20 October 2026. `snapshot.json` records SHA-256 values for both downloaded source files. The boundary hash applies to the decompressed JSON bytes.

`hh_income_district.csv` is the complete small downloaded table (approximately 20 KiB), not only the 2022 selection. `boundaries_utm47.json.gz` losslessly compresses the 11-area API response (approximately 946 KiB compressed). Every returned vertex and polygon ring is retained. Neither geometry simplification nor inferred subdivisions are used. The three maps are original plots, not copied screenshots.

## Variable and geography

Use `income_median` (median gross monthly household income in RM) in **2022** for the published figures. The notebook also permits `income_mean`. These nominal estimates are household-level summaries within each area, not individual salaries, annual incomes, land values or estimates of the combined region's household median.

The returned boundary coordinates are WGS 84 / UTM zone 47N, EPSG:32647, in metres. The notebook verifies the service's CRS and uses equal x/y scale. Boundary retrieval in 2026 is not proof of agreement with 2022 administrative geography. Verify boundary changes before substantive historical analysis.

The join uses both state and district names and validates one-to-one matching. Explicit aliases reconcile DOSM's `Ulu Langat` and `Ulu Selangor` with `HULU LANGAT` and `HULU SELANGOR`; federal-territory prefixes are also reconciled. All 11 values must match before plotting. No missing districts are silently removed and no income years are mixed.

The 2024 income snapshot does not include KL and Putrajaya at district level. The notebook therefore rejects that incomplete selection. It uses the common 2022 reference instead.

## Reproduction

Open `src/content/notebooks/lab-08-autocorrelation-self-study.ipynb`. In this repository it discovers the snapshot and verifies checksums. On its own it can download the official sources directly; `USE_BOOK_SNAPSHOT=False` explicitly selects that route. Both routes report fingerprints and export settings. Live source updates may change coverage or values.

Run `python scripts/check_autocorrelation_pilot.py` to execute the notebook offline, check the eleven source values against the chapter table, verify permutation invariants and chain arithmetic, and check that an incomplete year is rejected. Add `--write-figures` to regenerate the four chapter illustrations. Requirements: NumPy, pandas, Matplotlib, IPython and nbformat. The existing Comic Neue font in `_static/css/fonts` is used for optional xkcd-style annotations; its OFL attribution remains alongside it. Geographic boundaries are not sketch-distorted.

Colour breaks are computed once from observed medians and reused in all permutations. A fixed seed produces four independent draws. The maps reshuffle the **11 area medians**, not households or locations. No Moran statistic or significance test for the Malaysian data is claimed. The synthetic four-area chain and binary grids are separate teaching examples.
