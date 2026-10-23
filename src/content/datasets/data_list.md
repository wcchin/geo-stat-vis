# Dataset catalogue and downloads

This catalogue links datasets to Geo-stat-vis demonstrations. Use the [Part 3 notebook guide](../part3.md) to choose an exercise. A downloaded repository contains local copies of these files; online notebooks can instead use pinned GitHub raw URLs.

## HDB resale and planning boundaries — staged, pending provenance review

The four following compressed files were confirmed in `wcchin/GE5230-2610/resources` and copied without modification into this PR. **Before merging, verify original data sources, derived/geocoded fields, and redistribution permissions.** Their presence in a private teaching repository alone does not establish permission for public release.

| Dataset | Used for | Download from this PR | Documentation |
| --- | --- | --- | --- |
| HDB resale teaching extract (2013) | Statistical comparisons | [CSV.xz](https://github.com/wcchin/geo-stat-vis/blob/data/hdb-2013-2023-planning-boundaries/src/content/datasets/singapore_hdb_ura/hdb_data_2013.csv.xz) | [Source notes](singapore_hdb_ura/README.md) |
| HDB resale teaching extract (2023) | Distributions, classification, comparisons, global point patterns | [CSV.xz](https://github.com/wcchin/geo-stat-vis/blob/data/hdb-2013-2023-planning-boundaries/src/content/datasets/singapore_hdb_ura/hdb_data_2023.csv.xz) | [Source notes](singapore_hdb_ura/README.md) |
| Master Plan 2019 planning areas | Spatial joins and regional comparisons | [ZIP](https://github.com/wcchin/geo-stat-vis/blob/data/hdb-2013-2023-planning-boundaries/src/content/datasets/singapore_hdb_ura/master-plan-2019-planningarea.zip) | [Source notes](singapore_hdb_ura/README.md) |
| Master Plan 2019 subzones | Spatial aggregation and point-pattern study areas | [ZIP](https://github.com/wcchin/geo-stat-vis/blob/data/hdb-2013-2023-planning-boundaries/src/content/datasets/singapore_hdb_ura/master-plan-2019-subzone_landuse_area.zip) | [Source notes](singapore_hdb_ura/README.md) |

## Other documented datasets

| Dataset | Use | Download | Source notes |
| --- | --- | --- | --- |
| Synthetic point-pattern observations | Quadrat, nearest-neighbour, K-functions | [CSV](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/datasets/point_pattern_teaching/synthetic_points.csv) | [Readme](point_pattern_teaching/README.md) |
| Malaysian income areal observations | Spatial autocorrelation and local association | [CSV](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/datasets/malaysia_income_areal/observations.csv) | [Readme](malaysia_income_areal/README.md) |
| Malaysian household income snapshot metadata | Reproduction audit | [JSON](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/datasets/peninsula_income_2022/snapshot.json) | [Readme](peninsula_income_2022/README.md) |

## Sources still to migrate

Johor/Segamat points of interest and roads, Queenstown location observations, and Singapore transit ODIO data need separate validation and documentation. Do not copy private-course source files into the public repository until reuse rights and preparation steps are established.

**Download guidance:** Open the GitHub file link and select **Download raw file**. In a notebook, prefer a local copy when present. For remote access, use a raw URL pinned to a release tag or commit SHA rather than relying indefinitely on `main`.
