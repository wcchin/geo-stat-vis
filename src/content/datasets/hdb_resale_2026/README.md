# HDB resale registrations, January–June 2026

This teaching snapshot contains 5,379 four-room resale registrations at 3,236 block/street addresses. Source registration month defines the period. Quartiles are S$558,000 and S$745,000, including all ties (1,367 lower and 1,353 upper records). No unit-level identifier is available. Repeated positions and apparent duplicate source rows are retained.

## Sources and reuse

Contains information from HDB resale flat prices, accessed 21 October 2026 from [data.gov.sg](https://data.gov.sg/collections/189/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view), made available under the [Singapore Open Data Licence](https://data.gov.sg/open-data-licence).

HDB/OneMap coordinates are from the HDB property-information table distributed by [seehiong/autonomous-hdb-deepagents, commit 2a0df19534be15102658cebdda9267a653e79642](https://github.com/seehiong/autonomous-hdb-deepagents/blob/2a0df19534be15102658cebdda9267a653e79642/db/init/data/hdb_property_info.csv), accessed 22 October 2026. The upstream project expressly permits reuse, modification and redistribution of its HDB datasets under the Singapore Open Data Licence and attributes map/geocoding information to OneMap, © Singapore Land Authority. See [OneMap's Singapore Open Data Licence](https://www.onemap.gov.sg/legal/opendatalicence.html). The included MIT notice covers upstream software, not a replacement data licence.

All selected addresses match exact block/street keys; repeated source entries with identical address and coordinates are collapsed before the many-to-one join. Match coverage is 100% for all three price groups. Coordinates are block-level positions, not individual flat locations. Address coverage alone is not proof of geocoding accuracy. Five corrections over 100 m from the earlier research snapshot affect six transactions; the audit CSV records them. They include a Jalan Tiga/ Jalan Bintang Tiga mismatch and Boon Keng/Upper Boon Keng mismatches. The older coordinate source is not bundled.

Basemap: URA [Master Plan 2019 Planning Area Boundary (No Sea)](https://data.gov.sg/datasets/d_4765db0e87b9c86336792efe8a1f7a66/view), using the existing 55-area layer in this repository at main commit 92d2ab96957fdcb6ca8bf7c85d5d7b8a6841a7a2. This is the existing teaching boundary vintage, rather than a fresh download of the newest data.gov.sg revision. URA boundaries provide context and a display mask, not an HDB opportunity surface or KDE boundary correction.

## Reproduce

Install numpy pandas scipy matplotlib scikit-learn shapely pyproj. From this directory, run `python plots.py`, `python analysis.py`, and `python dual_kde.py`. To avoid unnecessary BLAS threading, `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1` is useful. The book font is loaded from the repository; scripts run without network access.

Coordinates for analysis are EPSG:3414 in metres; compressed boundary coordinates are EPSG:4326 and projected before plotting. Prepared CSVs and geometry use lossless xz compression. The observed all-sales and quartile counts remain unchanged by the coordinate-source update.

K-means uses upper-group transactions, seed 5230, 20 initialisations, and k=3/5. DBSCAN uses min_samples=20 including self and eps=300/600/1000 m; transaction multiplicity is retained. KDE uses isotropic fixed Gaussian kernels. Spatial grids are 300 m. All intensity surfaces are uncorrected and only masked for display. Dual comparisons divide separately normalised group densities; support masks use at least 5 all-sales transactions/km² and, for high/low, at least 1 transaction/km² in each group. These are exploratory thresholds, not confidence limits.

The scientific reading is Jansenberger, E. M. and Staufer-Steinnocher, P. (2004), *Dual Kernel Density Estimation as a Method for Describing Spatio-Temporal Changes in the Upper Austrian Food Retailing Market*, AGILE 2004, pp. 551–558. The original retail application uses density differences; this chapter explains the distinction from normalised ratios.
