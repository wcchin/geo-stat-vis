# Data and Notebooks

These notebooks complement the [core chapters](part1.md) with practical demonstrations, applications and self-study investigations. They are organised by **concept and geographical question**, not by teaching week. Each notebook should identify its required data, packages and assumptions; some older course labs remain in migration and may require external resources.

The **GE5230 week** column provides an approximate connection to the original 2026 course schedule. It is not part of the notebook title or URL and may change in future teaching.

The guided notebooks have **learner** and **solution** versions. Only the learner appears in the book navigation, so each activity is listed once. Use the solution links in the table to open the complete notebooks on GitHub after attempting the exercises. Solutions remain openly accessible but are not separate sidebar chapters.

## Notebook catalogue

| Demonstration | Related core sections | Dataset or context | Type | GE5230 week (tentative) |
| --- | --- | --- | --- | --- |
| [Getting started](notebooks/getting-started.ipynb) | Notebook preparation | Python environment | Guide | Preparation |
| [Exploring distributions — learner](notebooks/exploring-distributions.ipynb) · [solution](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/notebooks/exploring-distributions-solution.ipynb) | [§2.2](chapter_2/sec_02-02-Frequency-Distribution.md) | 2023 HDB extract (PR #33) | Core | 2 |
| [Transforming and classifying values — learner](notebooks/data-transformation-classification.ipynb) · [solution](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/notebooks/data-transformation-classification-solution.ipynb) | [§2.3–2.4](chapter_2/sec_02-03-Data-Transformation.md) | 2023 HDB extract (PR #33) | Core | 2 |
| [Statistical group comparisons — learner](notebooks/statistical-group-comparisons.ipynb) · [solution](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/notebooks/statistical-group-comparisons-solution.ipynb) | [§3.1–3.4](chapter_3/sec_03-01-Hypothesis-Testing.md) | 2023 HDB extract (PR #33) | Core | 3 |
| [Spatial aggregation — learner](notebooks/spatial-aggregation.ipynb) · [solution](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/notebooks/spatial-aggregation-solution.ipynb) | [Chapter 2](chapter_2/chapter-2-spatial_data.md) | HDB; planning subzones | Core | 4 |
| [Global point-pattern methods — learner](notebooks/global-point-patterns.ipynb) · [solution](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/notebooks/global-point-patterns-solution.ipynb) | [§4.1–4.4](chapter_4/chapter-4-global_point_pattern.md) | Synthetic points | Core | 5 |
| [Sumatra fire detection quadrats](notebooks/firms-sumatra-quadrat.ipynb) | [§4.2](chapter_4/sec_04-02-Quadrat-Count-Analysis.md) | FIRMS teaching snapshot | Application | 5 |
| [Nearest-neighbour self-study](notebooks/lab-05-nna-self-study.ipynb) | [§4.3](chapter_4/sec_04-03-Nearest-Neighbor-Analysis.md) | Synthetic points | Self-study | 5 |
| [Spatial kernel density — learner](notebooks/spatial-kernel-density.ipynb) · [solution](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/notebooks/spatial-kernel-density-solution.ipynb) | [§5.1–5.2](chapter_5/sec_05-01-Kernel-Density-Estimation.md) | Synthetic points | Core | 6 |
| [Spatial clustering methods — learner](notebooks/spatial-clustering-methods.ipynb) · [solution](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/notebooks/spatial-clustering-methods-solution.ipynb) | [§5.3–5.5](chapter_5/sec_05-03-Spatial-Clustering.md) | Synthetic points | Core | 7 |
| [Clustering across time](notebooks/lab-07_2-clustering-real-data.ipynb) | [§5.3–5.6](chapter_5/sec_05-03-Spatial-Clustering.md) | Queenstown location records | Application | 7 |
| [Global spatial autocorrelation — learner](notebooks/global-spatial-autocorrelation.ipynb) · [solution](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/notebooks/global-spatial-autocorrelation-solution.ipynb) | [§6.1–6.3](chapter_6/sec_06-01-Spatial-Autocorrelation.md) | Synthetic areal grid; transit application retained for later migration | Core | 8 |
| [Malaysia spatial autocorrelation self-study](notebooks/lab-08-autocorrelation-self-study.ipynb) | [§6.1–6.3](chapter_6/sec_06-03-Morans-I.md) | Peninsular Malaysia income | Self-study | 8–9 |
| [Local spatial autocorrelation — learner](notebooks/local-spatial-autocorrelation.ipynb) · [solution](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/notebooks/local-spatial-autocorrelation-solution.ipynb) | [§6.4–6.6](chapter_6/sec_06-04-Local-Moran.md) | Synthetic areal grid; legacy LISA application retained | Core | 9 |
| [Malaysia income and areal patterns](notebooks/malaysia-income-areal-self-study.ipynb) | [Chapter 6](chapter_6/chapter-6-areal_pattern.md) | Peninsular Malaysia income | Application | 8–9 |
| [Visualising origin–destination flows](notebooks/visualising-origin-destination-flows.ipynb) | [Chapter 7](chapter_7/chapter-7-geovisualisation.md) | Synthetic OD flows (real-data source under review) | Worked demonstration | 11 |

**Migration note.** The catalogue uses descriptive labels now; some underlying filenames still contain course numbering while they are being adapted and checked. The [migration blueprint](../../docs/part3-migration-blueprint.md) records proposed names, data dependencies and migration status. Superseded numbered foundation, point-pattern, KDE and introductory clustering notebooks have been removed. Legacy application notebooks with unique material remain available pending their own migration.

## Data and reproducibility

The [data catalogue](datasets/data_list.md) is the intended place for source descriptions, redistribution conditions, spatial coverage and notebook dependencies; its inventory is being expanded as course resources are reviewed. Some older notebooks still depend on separately obtained GE5230 data or course-specific paths. Do not assume that every input is shipped with this public repository.

For a starting point with no external course data, try the [nearest-neighbour self-study](notebooks/lab-05-nna-self-study.ipynb). For a real-data areal example, the [Malaysia autocorrelation self-study](notebooks/lab-08-autocorrelation-self-study.ipynb) uses a documented income snapshot. Follow the specific notebook's data and environment notes rather than guessing paths.
