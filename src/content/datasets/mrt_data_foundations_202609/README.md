# MRT data foundations: September 2026

This directory supports all six Chapter 2 pages with a small recurring example: Bishan, Serangoon, Paya Lebar and Marymount. Both OD endpoints must belong to the four selected stations; month = September 2026, day type = WEEKDAY, hour category = 8. The 12 reported directed pairs sum to 12,904 trips. These are monthly category aggregates, not one morning, daily averages or unique travellers. The missing diagonal cells are retained as missing. The stations are illustrative selections, not a representative network sample.

## Reproduce

Use Python 3.11+ with numpy, pandas, scipy and matplotlib installed. From this directory run:

```sh
python reproduce.py
python draw_diagrams.py
python plots.py
```

No observation downloads or live geocoding are needed. `reproduce.py` checks the endpoint joins and independently verifies the four point-in-polygon matches using a ray-casting implementation and Matplotlib paths. It writes `data/od_joined_reproduced.csv` for comparison; that generated duplicate is not committed. `draw_diagrams.py` regenerates four SVGs. `plots.py` regenerates four statistical figure plates and `data/descriptive_audit.json`. The shared Comic Neue font is read from `_static/css/fonts` at the repository root, with a readable fallback if absent; its licence is in `ComicNeue-OFL.txt` beside the font. The conceptual normal/Poisson/binomial plots are explicitly not fitted to MRT data.

`data/audit.json` records the pilot source hashes, selection, row counts, safe/unsafe joins and reference-point rule. `data/descriptive_audit.json` records summaries, histogram bins, classification breaks, class counts, exact natural-breaks SSE and transformation examples. `SHA256SUMS.txt` identifies the committed inputs, scripts and figures. Reading Markdown is in the adjacent `chapter_2` directory.

## Data and provenance

- **OD trips:** instructor-supplied `origin_destination_train_202609.csv.xz`, accessed for this teaching pilot on 22 October 2026. The full extract has 887,478 rows and no repeated full observation key (month, day type, hour, transport type, origin, destination). Only the selected 12 rows are bundled as `od_selected.csv`. Original-file SHA256 is in the audit. This duplicate check is not proof of complete source coverage.
- **Station activity:** instructor-supplied `transport_node_train_202609.csv.xz`. Only the four station records matching the same temporal slice are bundled. Station tap-ins/tap-outs and restricted OD row/column sums have different scopes and definitions and are not assumed equal. LTA DataMall: https://datamall.lta.gov.sg/ . Follow source terms and acknowledgement requirements; this chapter does not grant a replacement licence to the observations.
- **Station lookup:** a curated four-station code/name crosswalk checked against supplied identifiers, LTA's system map (https://www.lta.gov.sg/content/dam/ltagov/getting_around/public_transport/rail_network/pdf/SM_20250704_BI.pdf) and exit names. Combined codes are retained as one source identifier. This does not establish a full-network matching result.
- **Exit coordinates:** 19 selected LTA-derived records from the pinned mirror https://github.com/seehiong/autonomous-hdb-deepagents/blob/2a0df19534be15102658cebdda9267a653e79642/db/init/data/mrt_exits.csv . Mirror source: LTA MRT Station Exit, https://data.gov.sg/datasets/d_b39d3a0871985372d7e1637193335da5/view . Source update field: 2 December 2025. The mirror README cites September 2026 retrieval and the Singapore Open Data Licence; the data was not freshly fetched from LTA for this chapter. Only selected exits are bundled. Alphabetically first exit code, then object ID, determines the station reference point: Exit A for all four. A selected exit is not an official station centre or evidence that passengers used that exit. Counts refer to records in the snapshot, not a verified inventory of currently open exits.
- **Planning areas:** existing URA Master Plan 2019 planning-area teaching copy, 55 features; compressed GeoJSON in EPSG:4326. Source https://data.gov.sg/datasets/d_4765db0e87b9c86336792efe8a1f7a66/view . This is an existing teaching vintage, not a new revision download. Point-in-polygon results refer to selected reference points. All 19 selected exits happen to share their respective reference-area labels in this snapshot.
- **Agency attribution:** LTA and URA; public datasets remain subject to the originating source terms, including the Singapore Open Data Licence where applicable: https://data.gov.sg/open-data-licence . The mirror's MIT software licence is separate from the source data licence. Preserve the original agency attribution when reusing the records. The chapter does not relicense third-party data.

All quantities are deliberately conditional on selection. The schematised area diagram uses calculated labels but illustrative boundaries and point positions. No national map, rail-route inference, passenger allocation model or statistical transport finding is claimed.

## Calculation conventions

Quantiles use linear interpolation. Standardisation uses sample standard deviation (ddof=1). Histogram bins are 500 trips wide, from 0 to 4,500; all except the final bin are left-closed/right-open. Classification uses three classes, with values on interior breaks assigned to the lower class. Equal intervals use the observed minimum and maximum; quantiles use one-third and two-thirds positions. Natural breaks exhaustively evaluates all contiguous, non-empty three-group partitions and minimises within-class squared deviations. This exact small-sample calculation requires no additional classification package. The head/tail paragraph shows only the first mean split, not a fitted heavy-tail model or completed recursive classifier.

Containment uses longitude/latitude EPSG:4326 with explicit boundary inclusion (covers semantics). There are four single matches. Boundary points in another sample may have multiple matches. No distance is calculated in this package. All records retain their original activity meanings after joins; duplicated exit joins are used only as a counterexample.

## Readings and technical references

- Box, G. E. P., & Cox, D. R. (1964). An Analysis of Transformations. *Journal of the Royal Statistical Society: Series B*, 26(2), 211–243. https://academic.oup.com/jrsssb/article/26/2/211/7028064
- Jiang, B. (2013). Head/Tail Breaks: A New Classification Scheme for Data with a Heavy-Tailed Distribution. *The Professional Geographer*, 65(3), 482–494. https://doi.org/10.1080/00330124.2012.700499
- NIST/SEMATECH e-Handbook of Statistical Methods, Exploratory Data Analysis: https://www.itl.nist.gov/div898/handbook/eda/eda.htm
- pandas merge documentation: https://pandas.pydata.org/docs/user_guide/merging.html
- PostGIS ST_Covers: https://postgis.net/docs/ST_Covers.html ; spatial queries: https://postgis.net/docs/using_postgis_query.html
