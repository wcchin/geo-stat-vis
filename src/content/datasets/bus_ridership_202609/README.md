# Singapore bus ridership, September 2026

The source files are the September 2026 LTA DataMall extracts supplied by the instructor: `transport_node_bus_202609.csv.xz` and `busstop_from_api_202609.csv.xz`. The prepared tables retain original stop identifiers as text, including leading zeros. Four volume-file codes do not match the supplied coordinate table: 07522, 44711, 67708 and 70372. None belongs to the complete paired sample, which has 100% coordinate coverage. Unknown stop/day-type combinations remain missing rather than being filled with zeros.

LTA definitions: [DataMall API User Guide](https://datamall.lta.gov.sg/content/dam/datamall/datasets/LTA_DataMall_API_User_Guide.pdf), “Passenger Volume by Bus Stops” and Annex A. The day-type field includes weekends and public holidays. Calendar reference: [Ministry of Manpower, Public Holidays for 2026](https://www.mom.gov.sg/newsroom/press-releases/2025/0616-public-holidays-for-2026). There are 22 Monday–Friday days and 8 Saturday–Sunday days in September, with no gazetted public holidays.

Basemap: URA [Master Plan 2019 Planning Area Boundary (No Sea)](https://data.gov.sg/datasets/d_4765db0e87b9c86336792efe8a1f7a66/view), using the existing 55-area teaching layer in geo-stat-vis. Maps use EPSG:3414 metres internally, hide coordinate axes and show north arrows and 5 km scale bars. The boundaries are geographical context, not sampling strata or a model for passenger travel.

Implementation references: SciPy [paired t-test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_rel.html), [one-way and Welch ANOVA](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html), [Wilcoxon signed-rank](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html), [Kruskal–Wallis](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html) and [binomial test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html). These document the calculations; all reported inference values are explicitly conditional demonstrations of assumptions that the snapshot does not establish.

For the label-group example, interchange labels match descriptions ending in “Int” and terminal labels match descriptions ending in “Ter”, case-insensitively. Other descriptions form the remaining category. This independent naming rule makes the teaching example reproducible; it is not a validated operational classification. A production study should verify it against an authoritative inventory.

This directory contains compressed prepared tables, numerical audits, figure scripts and the chapter figures. `bus_analysis.py` reproduces the analysis and uses exact count numerators for paired differences. Source p-values that underflow to floating-point zero are retained in the machine-readable audit; the prose explains this limit rather than reporting zero probability. Applied reading selections by Benny and collaborators remain part of the later book-wide reading plan.


## Reproduce the chapter figures

Install numpy pandas scipy>=1.16 matplotlib pyproj shapely. From this directory run `python bus_analysis.py`; inputs are bundled and no network access is needed. `python plots.py` regenerates only the map and overview plot. The book font is loaded from `_static/css/fonts` at the repository root. The planning-area geometry is stored as EPSG:4326 and projected to EPSG:3414 before display. No coordinate axes are shown.

Prepared tables use lossless xz compression; preserve stop codes as text. The paired file is regenerated from the stop table. Source raw extracts remain the instructor-supplied files, rather than a live API refresh. All inferential outputs use conventional independent-stop models for teaching; no spatial correction, causal inference or reconstruction of individual days is claimed. Some p-values underflow to numerical zero in the audit; the chapter explains that this is not a probability of exactly zero.

LTA DataMall: https://datamall.lta.gov.sg/ . Data users should follow the source terms and acknowledgement requirements. The chapter does not grant a new licence to third-party source records. These are public transport aggregates, with no passenger identifiers.
