# Dataset catalogue and downloads

This guide lists **published teaching datasets** and datasets still being prepared for the public Geo-stat-vis notebooks. Download links point to files in the repository; source notes document provenance and reuse conditions. The [Part 3 notebook catalogue](../part3.md) explains what each notebook teaches.

For a local repository clone, use the bundled file rather than downloading it again. For Colab or another remote environment, use a **version-pinned raw URL** when possible; `main` can change between releases.

## Available in Geo-stat-vis

| Dataset | Main use | Download | Source and usage notes |
| --- | --- | --- | --- |
| Synthetic point patterns | Quadrat, nearest-neighbour and K-function demonstrations | [CSV (GitHub)](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/datasets/point_pattern_teaching/synthetic_points.csv) | [Generation method](point_pattern_teaching/README.md); synthetic, not observed events |
| Malaysian income areal observations | Global/local spatial association | [CSV (GitHub)](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/datasets/malaysia_income_areal/observations.csv) | [Source, mapping and assumptions](malaysia_income_areal/README.md); 92 mapped areas |
| Malaysian income source snapshot metadata | Audit and reproducibility | [JSON (GitHub)](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/datasets/peninsula_income_2022/snapshot.json) | [Income and boundary provenance](peninsula_income_2022/README.md); metadata rather than the complete data package |

**How to download:** Open a GitHub file link above and use its **Download raw file** control. To load a CSV directly in Python, use the corresponding `raw.githubusercontent.com` URL, ideally with a release tag or commit SHA instead of `main`. The notebook migration will standardise a local-first loader with a remote fallback.

## Planned public teaching datasets

These sources are used in the GE5230-2610 labs but **do not yet have verified public download packages here**. The course repository's `resources` directory and older Google Drive references must be reconciled, and redistribution conditions checked before links are added.

| Dataset / source | Intended demonstrations | Status | Download |
| --- | --- | --- | --- |
| Singapore HDB resale teaching extract (2013/2023) | Distributions, classification, statistical comparisons, point patterns | Source, schema and redistribution audit pending | Not yet published |
| URA planning areas / subzones | Spatial aggregation and point-pattern windows | Check existing copies, version and public reuse conditions | Not yet published in this catalogue |
| Johor/Segamat POIs and roads | Spatial KDE | Provenance and redistribution review pending | Not yet published |
| Queenstown location observations | Clustering across time | Source and sampling/usage review pending | Not yet published |
| Singapore transit ODIO data and boundaries | Global spatial autocorrelation | Source, preprocessing and redistribution review pending | Not yet published |
| Singapore bus origin–destination / stop inputs | Flowmap visualisation | Existing notebook input paths require audit | Not yet published |

## Data publication checklist

Before adding a new download row, confirm: (1) original provider and licence/redistribution rights; (2) spatial and temporal coverage; (3) coordinate reference system and field definitions; (4) processing or sampling steps and known limitations; (5) file size and suitable storage; (6) a notebook that can load it from both a local checkout and a pinned remote URL.

Large or restricted datasets should use an official download source or clearly documented preparation procedure instead of an unapproved public copy. Never publish private course credentials, Google Drive paths or student information.
