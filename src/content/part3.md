# Data and Notebooks

These notebooks complement the [core chapters](part1.md) with practical demonstrations, applications and self-study investigations. They are organised by **concept and geographical question**, not by teaching week. Each notebook should identify its required data, packages and assumptions; some older course labs remain in migration and may require external resources.

The **GE5230 week** column provides an approximate connection to the original 2026 course schedule. It is not part of the notebook title or URL and may change in future teaching.

## Notebook catalogue

| Demonstration | Related core sections | Dataset or context | Type | GE5230 week (tentative) |
| --- | --- | --- | --- | --- |
| [Getting started](notebooks/getting-started.ipynb) | Notebook preparation | Python environment | Guide | Preparation |
| [Reading tables and distributions](notebooks/lab-01-reading-table-and-histogram.ipynb) | [§2.2](chapter_2/sec_02-02-Frequency-Distribution.md) | Course data (migration pending) | Core | 2 |
| [Data classification](notebooks/lab-02-map-classification.ipynb) | [§2.3–2.4](chapter_2/sec_02-03-Data-Transformation.md) | HDB resale (migration pending) | Core | 2 |
| [Statistical group comparisons](notebooks/lab-03-t-test-anova.ipynb) | [§3.1–3.4](chapter_3/sec_03-01-Hypothesis-Testing.md) | HDB resale (migration pending) | Core | 3 |
| [Spatial aggregation](notebooks/lab-04-spatially-aggregated.ipynb) | [Chapter 2](chapter_2/chapter-2-spatial_data.md) | HDB; planning subzones | Core | 4 |
| [Global point patterns](notebooks/lab-05-point-pattern.ipynb) | [§4.1–4.4](chapter_4/chapter-4-global_point_pattern.md) | Tampines HDB | Core | 5 |
| [Sumatra fire detection quadrats](notebooks/firms-sumatra-quadrat.ipynb) | [§4.2](chapter_4/sec_04-02-Quadrat-Count-Analysis.md) | FIRMS teaching snapshot | Application | 5 |
| [Nearest-neighbour self-study](notebooks/lab-05-nna-self-study.ipynb) | [§4.3](chapter_4/sec_04-03-Nearest-Neighbor-Analysis.md) | Synthetic points | Self-study | 5 |
| [Spatial kernel density](notebooks/lab-06-spatial-kde.ipynb) | [§5.1–5.2](chapter_5/sec_05-01-Kernel-Density-Estimation.md) | Synthetic points; Johor POIs | Core | 6 |
| [K-means and DBSCAN](notebooks/lab-07_1-clustering-random-demo.ipynb) | [§5.3–5.5](chapter_5/sec_05-03-Spatial-Clustering.md) | Synthetic points | Core | 7 |
| [Clustering across time](notebooks/lab-07_2-clustering-real-data.ipynb) | [§5.3–5.6](chapter_5/sec_05-03-Spatial-Clustering.md) | Queenstown location records | Application | 7 |
| [Global spatial autocorrelation](notebooks/lab-08-spatial-autocorrelation.ipynb) | [§6.1–6.3](chapter_6/sec_06-01-Spatial-Autocorrelation.md) | Singapore transit | Core | 8 |
| [Malaysia spatial autocorrelation self-study](notebooks/lab-08-autocorrelation-self-study.ipynb) | [§6.1–6.3](chapter_6/sec_06-03-Morans-I.md) | Peninsular Malaysia income | Self-study | 8–9 |
| [Local spatial association](notebooks/lab-09-LISA.ipynb) | [§6.4–6.6](chapter_6/sec_06-04-Local-Moran.md) | Course areal data | Core | 9 |
| [Malaysia income and areal patterns](notebooks/malaysia-income-areal-self-study.ipynb) | [Chapter 6](chapter_6/chapter-6-areal_pattern.md) | Peninsular Malaysia income | Application | 8–9 |
| [Preparing movement flows](notebooks/lab-10-for-flowmapgl.ipynb) | [Chapter 7](chapter_7/chapter-7-geovisualisation.md) | Singapore bus OD data | Application | 11 |

**Migration note.** The catalogue uses descriptive labels now; some underlying filenames still contain course numbering while they are being adapted and checked. The [migration blueprint](../../docs/part3-migration-blueprint.md) records proposed names, data dependencies and migration status. The legacy preparation notebook is no longer in the table of contents but remains in the repository until compatibility checks are complete.

## Data and reproducibility

The [data catalogue](datasets/data_list.md) is the intended place for source descriptions, redistribution conditions, spatial coverage and notebook dependencies; its inventory is being expanded as course resources are reviewed. Some older notebooks still depend on separately obtained GE5230 data or course-specific paths. Do not assume that every input is shipped with this public repository.

For a starting point with no external course data, try the [nearest-neighbour self-study](notebooks/lab-05-nna-self-study.ipynb). For a real-data areal example, the [Malaysia autocorrelation self-study](notebooks/lab-08-autocorrelation-self-study.ipynb) uses a documented income snapshot. Follow the specific notebook's data and environment notes rather than guessing paths.
