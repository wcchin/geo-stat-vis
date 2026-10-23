# Part 3 notebook migration blueprint

Status: **in progress**, 23 October 2026. This document records the mapping for migration from the private GE5230-2610 course labs into public-facing Geo-stat-vis. It is a plan, not evidence of notebook execution or dataset redistribution clearance.

## Conventions

- Public filenames, notebook titles, and URLs describe the **concept or application**, with lowercase hyphenated slugs and no week or chapter numbering.
- Keep the **GE5230 week (tentative)** only in the Part 3 catalogue's final column.
- Start each notebook with its question, learning objectives, links to core sections, data source and permission status, package requirements, and relative-path execution instructions.
- Keep existing public, reproducible self-study examples unless a replacement demonstrably improves them. Preserve course links until redirects or cross-reference updates are verified.
- Never assume that data in a private course repository can be redistributed publicly. Determine provenance, reuse rights, size, and any need for an anonymised or sampled teaching extract.
- For public notebooks, avoid mandatory `google.colab.drive.mount` and `/content/drive/MyDrive/GE5230/` paths. Google Colab may be optional.
- CI must build the MyST site and execute suitably scoped notebook validation before retiring old paths.

## Mapping matrix

| Current notebook in Geo-stat-vis | Target concept-based filename | Learning purpose / core alignment | GE5230-2610 reference | Inputs / dependencies | Action | GE5230 week (tentative) |
| --- | --- | --- | --- | --- | --- | --- |
| lab-00-installing-packages.ipynb | getting-started.ipynb | Environment, data and reproducibility | General lab preparation | Python/package environment | **Added**; old copy retained temporarily | Preparation |
| lab-01-reading-table-and-histogram.ipynb | exploring-distributions.ipynb | Distributions and plots; §2.1–2.2 | labs/week_02_demo.ipynb | HDB, currently older dataset paths | Combine/adapt | 2 |
| lab-02-map-classification.ipynb | data-transformation-classification.ipynb | Transformation/classification; §2.3–2.4 | labs/week_02_demo.ipynb | HDB; mapclassify | Adapt | 2 |
| lab-03-t-test-anova.ipynb | statistical-group-comparisons.ipynb | Inference, t-tests, ANOVA; §3.1–3.4 | labs/week_03_demo.ipynb | HDB 2013/2023; planning areas; pingouin | Replace/adapt after parse and data check | 3 |
| lab-04-spatially-aggregated.ipynb | spatial-aggregation.ipynb | Spatial joins, units and aggregation; Ch 2–3 | Original public lab | HDB; planning subzones | Review/retain | 4 |
| lab-05-point-pattern.ipynb | global-point-patterns.ipynb | CSR, quadrat, NNA, K; Ch 4 | labs/week_05_demo.ipynb | HDB; planning subzones; utils_week05.py | Adapt | 5 |
| firms-sumatra-quadrat.ipynb | sumatra-fire-point-patterns.ipynb | Real-data quadrats; §4.2 | Public reproducible example | FIRMS committed snapshot | Retain/rename | 5 |
| lab-05-nna-self-study.ipynb | nearest-neighbour-self-study.ipynb | Monte Carlo NNA; §4.3 | Public reproducible self-study | Synthetic coordinates | Retain/rename | 5 |
| lab-06-spatial-kde.ipynb | spatial-kernel-density.ipynb | KDE and bandwidth; §5.1–5.2 | labs/week_06_demo.ipynb | Johor POIs/roads; earthquake points; utils_week05.py | Adapt | 6 |
| lab-07_1-clustering-random-demo.ipynb | spatial-clustering-methods.ipynb | K-means/DBSCAN; §5.3–5.5 | labs/week_07_demo1.ipynb | Synthetic observations; sklearn | Adapt | 7 |
| lab-07_2-clustering-real-data.ipynb | queenstown-spatial-clustering.ipynb | Temporal grouping of cluster patterns; §5.3–5.6 | labs/week_07_demo2.ipynb | Citydata Queenstown; utils_week07.py | Adapt subject to provenance | 7 |
| lab-08-spatial-autocorrelation.ipynb | global-spatial-autocorrelation.ipynb | Spatial weights and Moran I; §6.1–6.3 | labs/week_08_demo.ipynb | ODIO_all_202306.csv.xz; MP14 subzones | Adapt subject to provenance | 8 |
| lab-08-autocorrelation-self-study.ipynb | malaysia-autocorrelation-self-study.ipynb | Guided global autocorrelation; §6.1–6.3 | Public reproducible self-study | 92 Malaysian income areas; public snapshot | Retain/rename | 8–9 |
| lab-09-LISA.ipynb | local-spatial-autocorrelation.ipynb | Local Moran and related statistics; §6.4–6.6 | Existing course lab / verify newest source | Areal dataset and packages to verify | Review/adapt | 9 |
| malaysia-income-areal-self-study.ipynb | malaysia-income-areal-patterns.ipynb | Global/local areal analysis; Ch 6 | Public reproducible example | Malaysian income; spatial weights | Retain/rename | 8–9 |
| lab-10-for-flowmapgl.ipynb | visualising-origin-destination-flows.ipynb | Preparing OD visualisation; Ch 7 | Existing public lab | Bus OD; bus stops | Adapt | 11 |

## Migration batches

1. **Foundations:** conventions; data and environment access; distributions, classification, comparisons. Current pilot publishes the getting-started notebook and a descriptive catalogue; the older labs remain the active pages until a verified adaptation is ready.
2. **Point patterns:** global methods, original self-study, KDE and clustering; identify duplicate investigations before replacing.
3. **Areal and geovisualisation:** global/local Moran, Malaysia data, flow visualisations; preserve reproducible public snapshots.

## Unresolved checks

- Verify actual availability and distribution rights for the course `resources` files used by GE5230 notebooks; the latest course code also references private Google Drive `data_base` files.
- Some large older Geo-stat-vis notebooks were not fully parsed through the GitHub connection; perform full JSON and execution checks before replacement.
- Audit cross-links in chapters, case studies, notebook markdown, MyST toc and any externally shared URLs when moving individual notebooks.
- Complete the currently empty data catalogue with source metadata and links to all notebooks that depend on each dataset.
