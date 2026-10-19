# Figure authorship and replacement register

Goal: replace borrowed illustrations with original course artwork, while retaining citations for ideas, methods and external data. Original artwork does not imply original ownership of the underlying method or data.

## Completed in this batch

- Autocorrelation: replace both Milwaukee lecture images and the three-permutation companion with three reproducible synthetic diagrams.
- Defining distance: replace the first two figures with an original six-unit polygon map and its matching graph. The eight undirected edges match every non-zero pair in the existing binary weight matrix.
- Remove the three borrowed SVGRepo chess icons; retain the written rook/bishop/queen definitions.
- Reproduction: `python scripts/draw_spatial_figures.py` (NumPy and Matplotlib). Fixed random seed; no external images or datasets. SVGs contain editable text.
- Checks: permutation multisets are unchanged; polygon shared-edge relationships and graph edges match the matrix. Figures were visually reviewed before publication.

## Remaining review

This is a source-text inventory of core-chapter and worked-example Markdown, not an assertion that every unattributed image belongs to the author. A linked source may cite a dataset, method, coauthored paper or the author's own work, rather than borrowed artwork. These cases require inspection before replacement. In particular, retain attribution for external data used in an original plot.

Start with explicitly borrowed artwork: Datatab t-test illustrations; Wikipedia KDE and R-tree diagrams; dog-breed and iOS gallery pictures; NASA and external map/design examples in Chapter 7. Then inspect linked research figures and all unattributed assets. Retain confirmed author-created figures.

Coverage does not yet include embedded notebook outputs, archived Markdown, archived weekly slide snapshots, or unused resource files. Replacing an active reference does not remove the old asset from Git history or other pages. Audit these surfaces separately before claiming the entire repository contains only original illustrations.

## Inventory

Figure/image occurrences: 334. Linked source / provenance review: 86; Authorship unverified: 243; Original (reproducible source): 5.

### sec_01-01-Geovisualisation.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w01-img/xkcd_cat_proximity.png` | Linked source / provenance review | [Cat Proximity (xkcd.com/231)](https://xkcd.com/231/). |
| `../resources/w01-img/general_purpose_map.jpg` | Authorship unverified | A topographic map showing the land, street networks, and boundary between Singapore and Malaysia (Johor). |
| `../resources/w01-img/SMRT_localitymap_Chinese_Garden.jpg` | Linked source / provenance review | SMRT Locality map Chinese Garden Exit C, by [SMRT](http://journey.smrt.com.sg/journey/station_info/chinese-garden/map/) |
| `../resources/w01-img/Snow-cholera-map-1.jpg` | Linked source / provenance review | John Snow's 1854 Cholera Map: the distribution of cases and water pumps. See: [Wikipedia](https://en.wikipedia.org/wiki/File:Snow-cholera-map-1.jpg) for description. |
| `../resources/w01-img/clinic_flow_radiation.png` | Linked source / provenance review | A flow map of estimated urban movement for accessing clinics. See [Interactive map on FlowMap.gl](https://app.flowmap.city/public/67249d1d-4c21-40e3-8ddb-fd5124907c99) |
| `../resources/w01-img/point-hdb_resaleprice.png` | Authorship unverified | The highest and lowest price of 10 yo, 4-room HDB flat in 2023. |
| `../resources/w01-img/areal-education_level-b.png` | Authorship unverified | Education level by Planning Area. |
| `../resources/w01-img/stat-subzone_bus_flow.png` | Authorship unverified | Subzone-to-subzone daily flow ridership. |

### sec_01-02-Visualization.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w01-img/drawing_compare_data_info-b.png` | Authorship unverified | Data vs. Information |
| `../resources/w01-img/drawing-data_info_insight.png` | Authorship unverified | Data, Information, Insights. |
| `../resources/w01-img/drawing-how_maps_are_used.png` | Authorship unverified | MacEachren's cartographic cube. |
| `../resources/w01-img/otas_01.png` | Authorship unverified | **OTAS**. |
| `../resources/w01-img/otas_flow.png` | Authorship unverified | OTAS workflow. |

### sec_01-03-Statistical-Thinking.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w01-img/measures_central.png` | Authorship unverified | The means of the three IRIS species. |
| `../resources/w01-img/measures_spread.png` | Authorship unverified | The spread of the three IRIS species. |
| `../resources/w01-img/measures_shapes.png` | Authorship unverified | The skewness and kurtosis of the three IRIS species. |
| `../resources/w01-img/analysis_correlation.png` | Authorship unverified | The relationships between petal length and petal weight for the three IRIS species. |
| `../resources/w01-img/analysis_differences-b.png` | Authorship unverified | The differences in petal length between the three species. |
| `../resources/w01-img/analysis_confidence.png` | Authorship unverified | The confidence interval (CI) of the actual population mean could fall within the 95% CI. |

### sec_01-04-GeoSpatial-Thinking.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w04-img/drawing-fourspaces.png` | Authorship unverified | The splatial framework. |
| `../resources/w04-img/splatial_absolute_space.png` | Authorship unverified | Absolute Space. The red-X marker shows where the current location is. |
| `../resources/w04-img/splatial_relative_space.png` | Authorship unverified | Relative Space. The buffer zone shows the neighborhood of current location. |
| `../resources/w04-img/splatial_relational_space.png` | Authorship unverified | Relational Space. The links show the connections between spatial units. Those connected to the current location are highlighted in blue. |
| `../resources/w04-img/splatial_mental_space.png` | Authorship unverified | Mental Space. The size of point shows the familiarity of a person who stay at the current location. |

### sec_02-01-Data-Preparation.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w02-img/preprocessing_steps.drawio.png` | Authorship unverified | Key data preprocessing process. |
| `../resources/w01-img/drawing-how_maps_are_used.png` | Authorship unverified | MacEachren's cartographic cube. In the exploring steps (lower left corner). |

### sec_02-02-Frequency-Distribution.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w02-img/frequency_distribution_demo_0.png` | Authorship unverified | The frequency distribution of resale transactions by: (a) flat type and (b) resale price. |
| `../resources/w02-img/frequency_distribution_pdf_cdf.png` | Authorship unverified | The (a) histogram, (b) PDF, and (c) CDF. In CDF, the x-axis value (167) that correspond to the y (density) value of 0.4 means that all the smaller values ($x<167$) contains 40% of the data points. |
| `../resources/w02-img/frequency_distribution_symmetrical.png` | Authorship unverified | Symmetrical shapes. |
| `../resources/w02-img/frequency_distribution_asymmetrical.png` | Authorship unverified | Asymmetrical shapes. |
| `../resources/w02-img/frequency_distribution_modality.png` | Authorship unverified | Various modality shapes. |
| `../resources/w02-img/frequency_distribution_kurtosis.png` | Authorship unverified | Various Kurtosis shapes. |
| `../resources/w02-img/frequency_distribution_3types.png` | Authorship unverified | Three common types of distribution. |
| `../resources/w02-img/frequency_distribution_normal.png` | Authorship unverified | Normal Distribution with various paramters ($\mu$ and $\sigma$). |
| `../resources/w02-img/frequency_distribution_poisson.png` | Authorship unverified | Poisson Distribution with various paramters ($\lambda$). |
| `../resources/w02-img/frequency_distribution_binomial.png` | Authorship unverified | Binomial Distribution with various paramters. Number of trials is fixed at 10. |
| `../resources/w02-img/frequency_distribution_histplot.png` | Authorship unverified | Histogram of resale prices, differentiated by flat types. |
| `../resources/w02-img/frequency_distribution_kdeplot.png` | Authorship unverified | PDF of resale prices, differentiated by flat types. |
| `../resources/w02-img/frequency_distribution_ecdfplot.png` | Authorship unverified | CDF of resale prices, differentiated by flat types. |
| `../resources/w02-img/frequency_distribution_boxplot.png` | Authorship unverified | Box plot of resale prices, differentiated by flat types. |
| `../resources/w02-img/frequency_distribution_boxenplot.png` | Authorship unverified | Boxen plot of resale prices, differentiated by flat types. |
| `../resources/w02-img/frequency_distribution_jointgrid.png` | Authorship unverified | Joint grid (scatter plot and PDF) of floor area vs. resale prices, differentiated by flat types. |

### sec_02-03-Data-Transformation.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w02-img/data_transform-minmax.png` | Authorship unverified | The histogram (top) and PDF (bottom) of the average subzone resale price before (left) and after (right) min-max scaling. |
| `../resources/w02-img/data_transform-zscore.png` | Authorship unverified | The histogram (top) and PDF (bottom) of the average subzone resale price before (left) and after (right) standardization. |
| `../resources/w02-img/data_transform-zscore2.png` | Authorship unverified | The PDF (top) of the average subzone resale price of 3 rooms and 5 rooms HDB flat before (left) and after (right) standardization. The two scatter plots at the bottom show the relationship between 3 and 5 room HDB flat. |
| `../resources/w02-img/data_transform-log.png` | Authorship unverified | The before (left) and after (right) log-transformed of resale prices. |
| `../resources/w02-img/demo_log_transform.png` | Authorship unverified | The before (top) and after (bottom) log-transformed of ridership (arrival passsenger). |
| `../resources/w02-img/data_transform-boxcox.png` | Authorship unverified | Histogram of Box-Cox transformed values, with $\lambda$ set to: 0, 0.25, 0.5, 1, 2, 3. |
| `../resources/w02-img/data_transform-ranking.png` | Authorship unverified | The relationship between the ranks and the original data, and the frequency distribution of the ranks. |

### sec_02-04-Data-Classification.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w02-img/data_classify-equal_interval.png` | Authorship unverified | The breaks and the number of records in each class for Equal Interval. |
| `../resources/w02-img/data_classify-quantiles.png` | Authorship unverified | The breaks and the number of records in each class for Quantiles. |
| `../resources/w02-img/data_classify-StdMean.png` | Authorship unverified | The breaks and the number of records in each class for standard deviation. |
| `../resources/w02-img/data_classify-NaturalBreaks.png` | Authorship unverified | The breaks and the number of records in each class for Natural Breaks. |
| `../resources/w02-img/data_classify-HeadTailBreaks.png` | Authorship unverified | The breaks and the number of records in each class for Head/Tail Breaks. |

### sec_02-05-Spatial-Database.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w12-img/charles-postiaux-_Ulv6kWf5Gw-unsplash.jpg` | Linked source / provenance review | Sultan Mosque, Singapore. Photo by <a href="https://unsplash.com/@charlespostiaux?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Charles Postiaux</a> on <a href="https://unsplash.com/photos/selective-focus-photography-of-woman-taking-photo-_Ulv6kWf5Gw?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a> |
| `../resources/w12-img/data_management.png` | Authorship unverified | The photo management. |
| `../resources/w12-img/spatial_database_simple.png` | Authorship unverified | Spatial Database |
| `../resources/w12-img/keys.png` | Authorship unverified | The keys in Relational Database. |
| `../resources/w12-img/one-to-one-demo.png` | Authorship unverified | One-to-one demo. |
| `../resources/w12-img/one-to-many-demo.png` | Authorship unverified | One-to-many demo. |
| `../resources/w12-img/many-to-one-demo.png` | Authorship unverified | Many-to-one demo. |
| `../resources/w12-img/many-to-many-demo.png` | Authorship unverified | Many-to-many demo. |
| `../resources/w12-img/database_relational_demo.png` | Authorship unverified | A database for food order & delivery system. |
| `../resources/w12-img/normalization_before.png` | Authorship unverified | A demo table, before normalisation. |
| `../resources/w12-img/normalization_observe.png` | Authorship unverified | First step is to observe the composition and structure of the database: how many and what are the different 'entity' or 'object' in the table. |
| `../resources/w12-img/normalization_missing_value.png` | Authorship unverified | The original data may organised in an ordered way such that the repeated values are skipped if it is same as the one before. |
| `../resources/w12-img/normalization_decompose_1.png` | Authorship unverified | Decopmose the table. Still, there are one table with two types of 'object'. |
| `../resources/w12-img/normalization_decompose_2.png` | Authorship unverified | Keep decompose the table again, until every table only represent a single type of object. |
| `../resources/w12-img/normalization_after.png` | Authorship unverified | Finalise the table decomposition and the normalisation is complete. |
| `../resources/w12-img/table_join.png` | Authorship unverified |  |
| `../resources/w12-img/table_relate.png` | Authorship unverified |  |
| `../resources/w12-img/google_map_demo.png` | Authorship unverified | What about 'spatial' in spatial database? The location, proximity, and direction in Google Map. |
| `../resources/w12-img/spatial_join.png` | Authorship unverified | 'Merging' (join/relate) table by spatial relationships. |
| `../resources/w12-img/R-tree.svg.png` | Linked source / provenance review | Image source: [Wikipedia: R-tree](https://en.wikipedia.org/wiki/R-tree) |
| `../resources/w12-img/one-to-one-link.png` | Authorship unverified | Inline image |
| `../resources/w12-img/one-to-many-link.png` | Authorship unverified | Inline image |
| `../resources/w12-img/many-to-one-link.png` | Authorship unverified | Inline image |
| `../resources/w12-img/many-to-many-link.png` | Authorship unverified | Inline image |
| `../resources/w12-img/one-to-one-link.png` | Authorship unverified | Inline image |
| `../resources/w12-img/one-to-many-link.png` | Authorship unverified | Inline image |
| `../resources/w12-img/many-to-one-link.png` | Authorship unverified | Inline image |
| `../resources/w12-img/many-to-many-link.png` | Authorship unverified | Inline image |

### sec_03-01-Hypothesis-Testing.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w03-img/analysis_differences.png` | Authorship unverified | The differences in petal length between the three species. |
| `../resources/w03-img/drawing-differences_groups.png` | Authorship unverified | How to determine if they are different or not so different? |
| `../resources/w03-img/measures_spread_4vars.png` | Authorship unverified | The differences in the 4 variables between species. |
| `../resources/w02-img/frequency_distribution_normal.png` | Authorship unverified | The Normal Distribution. |
| `../resources/w03-img/demo_datapoint.png` | Authorship unverified | A data point compared to the distribution. |
| `../resources/w03-img/demo_datapoint_2dist.png` | Authorship unverified | The distributions of two groups of students. |
| `../resources/w03-img/typeI_and_typeII_error.png` | Linked source / provenance review | Type 1 and type 2 errors. [Table from Wikipedia](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors) |

### sec_03-02-T-test.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w03-img/demo_datapoint_2dist.png` | Authorship unverified | The distributions of two groups of students. |
| `../resources/w03-img/Types_of_t-test.png` | Linked source / provenance review | Source: [Datatab](https://datatab.net/tutorial/t-test) |
| `../resources/w03-img/Example_one-sample_t-test.png` | Linked source / provenance review | Source: [Datatab](https://datatab.net/tutorial/t-test) |
| `../resources/w03-img/ttest_one_sample.png` | Authorship unverified | The one sample t-test example. |
| `../resources/w03-img/Example_of_a_t-test_for_independent_samples.png` | Linked source / provenance review | Source: [Datatab](https://datatab.net/tutorial/t-test) |
| `../resources/w03-img/analysis_differences--ttest.png` | Authorship unverified | The differences in petal length between the three species, with t-test results. |
| `../resources/w03-img/Example_of_the_t-test_for_paired_samples.png` | Linked source / provenance review | Source: [Datatab](https://datatab.net/tutorial/t-test) |
| `../resources/w03-img/psychology_data_lineplot-b.png` | Linked source / provenance review | The changes of psychological indexes before and after a VR treatment. T-test and significant levels are shown at top right. [10.1016/j.jenvp.2023.102012](https://doi.org/10.1016/j.jenvp.2023.102012) |

### sec_03-03-ANOVA.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w03-img/anova_ttest.drawio.png` | Authorship unverified | The analysis process for t-test, ANOVA, and post-hoc test. |
| `../resources/w03-img/measures_spread_4vars.png` | Authorship unverified | The One-way ANOVA comparing the four target variables between the three species. |
| `../resources/w03-img/physiology_data_lineplot-b.png` | Authorship unverified | The physiological responses before, during and after two types of VR treatments. |
| `../resources/w03-img/physiology_data_lineplot-b-tables.png` | Authorship unverified | The tables about the repeated measures and post-hoc results: (left) low decibel, (right) high decibel. |
| `../resources/w03-img/mixed-anova.png` | Authorship unverified | The mixed ANOVA result between classes, time (pre-test vs. post-test), and the interaction between class and time. |
| `../resources/w03-img/mixed-anova_posthoc.png` | Authorship unverified | The post-hoc test after mixed ANOVA, to observe the time effects in different condition. |
| `../resources/w03-img/pingouin_anova_guide.png` | Linked source / provenance review | The roadmap for choosing ANOVA and post-hoc tests approaches. by [Pingouin](https://pingouin-stats.org/build/html/guidelines.html) |

### sec_03-04-Non-parametric.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w03-img/pingouin_nonparam_guide.png` | Linked source / provenance review | The roadmap for choosing non-parametric tests approaches. by [Pingouin](https://pingouin-stats.org/build/html/guidelines.html) |
| `../resources/w03-img/nonparam_byGender_brunei.png` | Authorship unverified | by age |
| `../resources/w03-img/nonparam_byEdu_brunei.png` | Authorship unverified | by rural |
| `../resources/w03-img/nonparam_byAge_brunei.png` | Authorship unverified | by age |
| `../resources/w03-img/nonparam_byEdu_brunei.png` | Authorship unverified | by Education |

### sec_03-05-Summary.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w02-img/frequency_distribution_kdeplot.png` | Authorship unverified | The differences between flat type? |
| `../resources/w03-img/HDB_price_points_13.png` | Authorship unverified | The differences between regions? |
| `../resources/w03-img/HDB_price_points_13_23.png` | Authorship unverified | The differences between the two years? |

### chapter-4-global_point_pattern.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w04-img/spatial_patterns_3_basic.png` | Authorship unverified | Regular, random, and clustered. |
| `../resources/w05-img/three_strategies_for_point_pattern_2c.png` | Authorship unverified | Grid-based: density estimation and quadrat count. |
| `../resources/w05-img/three_strategies_for_point_pattern_2b.png` | Authorship unverified | Distance-based: search for the k-nearest and find neighbors fall within a search-radius (buffer). |

### sec_04-01-Complete-Spatial-Randomness.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w04-img/johnsnowmap_1.png` | Authorship unverified | John Snow's Cholera Death Incident Map |
| `../resources/w04-img/johnsnowmap_2.png` | Authorship unverified | Visually speaking, what is the patterns here in the map? |
| `../resources/w04-img/spatial_patterns_3_basic.png` | Authorship unverified | How to differentiate clustered from random? |
| `../resources/w04-img/describe_CSR2.png` | Authorship unverified | About Complete Spatial Randomness |
| `../resources/w04-img/drawing_street.png` | Authorship unverified | Stationarity on a street |
| `../resources/w04-img/drawing_random_pts_3.png` | Authorship unverified | Random Spatial Points |
| `../resources/w04-img/spatial_patterns_2_basic_b.png` | Authorship unverified | How different it is compared to CSR? |

### sec_04-02-Quadrat-Count-Analysis.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w05-img/plot_quadrat_counts.png` | Authorship unverified | Counting points in cells |

### sec_04-03-Nearest-Neighbor-Analysis.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w05-img/four_demo_points.png` | Authorship unverified | Examples from Woodlands Regional Centre, Woodlands West and Woodgrove, each within a 2 km by 2 km window. Predict which has the shortest average nearest-neighbour distance. Would that alone tell you which is most unusual under randomness? |
| `../resources/w05-img/simulate_nna.gif` | Authorship unverified | Each event contributes its nearest-neighbour distance. We average these distances, rather than distances between every possible pair. |
| `../resources/w05-img/monte_carlo_point_pattern.gif` | Authorship unverified | The window and point count stay fixed while locations change. Each simulation contributes one mean nearest-neighbour distance to the reference distribution. |
| `../resources/w05-img/nna_compare_hist.png` | Authorship unverified | Read each observed statistic relative to its own reference distribution. How unusual is the distance under that reference, rather than how short does it look in isolation? |

### sec_04-04-Ripleys-K-Function.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w05-img/three_strategies_for_point_pattern_2b.png` | Authorship unverified | Everyone look for the nearest neighbor vs. everyone draw a series of search buffer (radius). |
| `../resources/w05-img/Bus_Stop_nearest_neighbor.png` | Authorship unverified | Bus Stops distribution. Is the nearest neighbor distance 'meaningful'? |
| `../resources/w05-img/simulate_kfunc.gif` | Authorship unverified | Simulation of the buffer area and counting. |
| `../resources/w05-img/kfunc_arcGIS_redraw.png` | Authorship unverified | The clustered and dispersed range of K-function curve. |
| `../resources/w05-img/k_function_4cases_rand.png` | Authorship unverified | K-function curve of the four examples and the k-function curves of the corresponding 10 random distributions. |
| `../resources/w05-img/k_function_4cases_rand.png` | Authorship unverified | The k-function curves and the confidence interval (Monte Carlo Simulation) for the 4 examples. |
| `../resources/w05-img/drawing_nna_res_2.png` | Authorship unverified | Nearest Neighbor Analysis |
| `../resources/w05-img/k_function_4cases_ci.png` | Authorship unverified | Ripley's K-function |

### chapter-5-local_point_pattern.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w04-img/spatial_patterns_3_basic.png` | Authorship unverified | Is it clustered? not-clustered? random? |

### sec_05-01-Kernel-Density-Estimation.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w02-img/frequency_distribution_pdf_cdf.png` | Authorship unverified | Remember that we have talked about this in an earlier chapter? |
| `../resources/w06-img/kde_in_1_dim_wiki.png` | Linked source / provenance review | A histogram and KDE plot. Image source: [Wikipedia](https://en.wikipedia.org/wiki/Kernel_density_estimation) |
| `../resources/w06-img/summing_kde_1D_b.png` | Authorship unverified | How KDE work: by summing the density value. |
| `../resources/w06-img/gauss_kernel.png` | Authorship unverified | Gaussian Kernel, bandwidth (h) set as 1. |
| `../resources/w06-img/parabolic_kernel.png` | Authorship unverified | Epanechnikov Kernel, bandwidth (h) set as 1. |
| `../resources/w06-img/quartic_kernel.png` | Authorship unverified | Quartic Kernel, bandwidth (h) set as 1. |
| `../resources/w06-img/triangular_kernel.png` | Authorship unverified | Triangular Kernel, bandwidth (h) set as 1. |
| `../resources/w06-img/uniform_kernel.png` | Authorship unverified | Uniform Kernel, bandwidth (h) set as 1. |
| `../resources/w06-img/demo_bandwidth.png` | Authorship unverified | Effect of bandwidth (h) on Kernel Function (weighting). |
| `../resources/w06-img/demo_bandwidth_dif.png` | Authorship unverified | Effect of bandwidth (h) on 1-D KDE results. |
| `../resources/w06-img/k-fold-validation2.png` | Authorship unverified | 5-fold cross-validation approach. |
| `../resources/w06-img/KDE_line_fill_plot.png` | Authorship unverified | Line fill plot. |
| `../resources/w06-img/kde_contour_3species.png` | Authorship unverified | Contour lines. |
| `../resources/w06-img/kde_contour_line.png` | Authorship unverified | Contour lines on Facet Grid with single KDE line on the diagonal. |
| `../resources/w06-img/kde_hist_contour.png` | Authorship unverified | Contour lines on Facet Grid with the histograme of single vector on the diagonal. |

### sec_05-02-Spatial-KDE.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w06-img/density_based.png` | Authorship unverified | Impacts from near by points to each cell. |
| `../resources/w06-img/SpatialKDE_inanutshell.png` | Linked source / provenance review | Spatial KDE in a nutshell. For more information, please see Bailey and Gatrell 1995. Interactive Spatial Data Analysis. [Anderson 2009](https://pdf.sciencedirectassets.com/271664/1-s2.0-S0001457509X00035/1-s2.0-S0001457508002340/dx.doi.org/10.1016/j.aap.2008.12.014)] |
| `../resources/w06-img/summing_KDE_surface2.png` | Linked source / provenance review | The sum of bell shape kernels for every cell in the grid [Levine 2013. Crimestat 4](https://www.ojp.gov/pdffiles1/nij/grants/242960-242995.pdf). |
| `../resources/w06-img/demonstration_KDE-c.png` | Authorship unverified | Demonstration of KDE. |
| `../resources/w06-img/cat_health_care.png` | Authorship unverified | Health care POI @ Queenstown |
| `../resources/w06-img/cat_commercials.png` | Authorship unverified | Commercial POI @ Queenstown |
| `../resources/w06-img/cat_education.png` | Authorship unverified | Education POI @ Queenstown |
| `../resources/w06-img/cat_foods.png` | Authorship unverified | Food POI @ Queenstown |
| `../resources/w06-img/cat_beverages.png` | Authorship unverified | Beverages POI @ Queenstown |
| `../resources/w06-img/cat_outdoor_activity.png` | Authorship unverified | Outdoor Activity POI @ Queenstown |
| `../resources/w06-img/kde_queenstown_health.png` | Authorship unverified | E.g., Health POI @ Queenstown |
| `../resources/w06-img/kde_dif_bw.png` | Authorship unverified | KDE with different bandwidths |
| `../resources/w06-img/kernel_functions_3D.png` | Linked source / provenance review | Kernel functions (height-dimension) for 2D spatial data. See [Fouedjio et al. 2017](http://dx.doi.org/10.1080/03717453.2017.1415114). |
| `../resources/w06-img/kde_dif_kernel.png` | Authorship unverified | Examples and differences between threee Kernel Functions using the same dataset. |
| `../resources/w06-img/kde_example_1.png` | Linked source / provenance review | Example of Spatial KDE visualisation: [Chin 2023](https://dx.doi.org/10.1007/978-981-19-8765-6_8) |
| `../resources/w06-img/kde_example_2.png` | Linked source / provenance review | Example of Spatial KDE visualisation: [Xia et al. 2024](https://doi.org/10.1186/s40494-024-01499-5) |
| `../resources/w06-img/kde_example_4.png` | Linked source / provenance review | Example of Spatial KDE visualisation: [Wheeler 2014](https://andrewpwheeler.com/tag/kernel-density/) |
| `../resources/w06-img/kde_example_3.png` | Linked source / provenance review | Example of Spatial KDE visualisation: [Yang et al. 2019](https://doi.org/10.3390/ijgi8020093) |
| `../resources/w06-img/kde_example_5.png` | Linked source / provenance review | Example of Spatial KDE visualisation: [Kuo et al. 2012](https://api.semanticscholar.org/CorpusID:5968823) |
| `../resources/w06-img/kde_example_6.png` | Linked source / provenance review | Example of Spatial KDE visualisation: [Levine 2013](https://www.ojp.gov/pdffiles1/nij/grants/242960-242995.pdf) |
| `../resources/w06-img/cat_outdoor_activity.png` | Authorship unverified | Effects of the edges where the external data is not included. |
| `../resources/w06-img/advanced_dualkde.png` | Linked source / provenance review | See [Jansenberger & Staufer-Steinnocher 2004](https://www.researchgate.net/publication/252791884_Dual_Kernel_Density_Estimation_as_a_Method_for_Describing_Spatio-Temporal_Changes_in_the_Upper_Austrian_Food_Retailing_Market) for more details |
| `../resources/w06-img/advanced_stkde.png` | Linked source / provenance review | See [Hu et al. 2018](https://doi.org/10.1016/j.apgeog.2018.08.001) for more details |
| `../resources/w06-img/advanced_nkde.png` | Linked source / provenance review | See [Tang et al. 2016](https://doi.org/10.1080/13658816.2015.1119279) for more details |

### sec_05-03-Spatial-Clustering.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w07-img/dog_breeds_3.png` | Linked source / provenance review | Identify dogs that look similar from the photos. Source: [Solving the mystery of my dog's breed with ML](https://gdmarmerola.github.io/discovering-breed-with-ml/) |
| `../resources/w07-img/ios-17-pets-photos.jpg` | Linked source / provenance review | Looking for the same person or pet in the photo gallery. Image Source: [iOS 17 Photos App Recognizes Your Pets](https://www.macrumors.com/2023/06/06/ios-17-photos-recognizes-pets/) |
| `../resources/w07-img/demo_clustering_0.png` | Authorship unverified | The data points. |
| `../resources/w07-img/demo_clustering_1.png` | Authorship unverified | 2 big groups. |
| `../resources/w07-img/demo_clustering_5.png` | Authorship unverified | Another 2 big groups. |
| `../resources/w07-img/demo_clustering_2.png` | Authorship unverified | Those on the left split into 2 small groups. |
| `../resources/w07-img/demo_clustering_3.png` | Authorship unverified | Those on the right split into 2 small groups. |
| `../resources/w07-img/demo_clustering_4.png` | Authorship unverified | 4 small groups. |
| `../resources/w07-img/gps_activity_spaces.png` | Linked source / provenance review | Using the GPS records of a person moving within a neighborhood to detect clusters (with noises) and identify the place where the participant had visited by follow-up interview and manual checking. [Feng et al. 2024.](https://doi.org/10.1111/tgis.13235) |
| `../resources/w07-img/demo_poi_clusters_1.png` | Linked source / provenance review | The study run clustering on the kernel density of various GPS types and identify clusters with similar density of the different POI types. [Chin et al. 2023](https://doi.org/10.1177/23998083231217376) |

### sec_05-04-K-Means-Clustering.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w07-img/kmeans-step_0.png` | Authorship unverified | The data point |
| `../resources/w07-img/kmeans-step_1.png` | Authorship unverified | The steps: 1 Initialize with random centroids. 2 Get the nearest neighbors, and calculate the new mean centers. 3 Move the centers to the mean centers |
| `../resources/w07-img/kmeans-step_2.png` | Authorship unverified | The steps: 1 Re-calculate distance and find nearest neighbors. 2 Re-Calculate new mean centers and move |
| `../resources/w07-img/kmeans-step_3.png` | Authorship unverified | The steps: 1 The location of new and previous centers overlapped. Hence, stops. |
| `../resources/w07-img/kmeans_demo_7/kmeans_7.gif` | Authorship unverified |  |
| `../resources/w07-img/kmeans_demo_7/kmeans_7-step_17.png` | Authorship unverified | The final clusters. |
| `../resources/w07-img/DataClustering_ElbowCriterion.JPG` | Linked source / provenance review | [Wikipedia](https://en.wikipedia.org/wiki/File:DataClustering_ElbowCriterion.JPG) |
| `../resources/w07-img/Silhouette-plot-orange.png` | Linked source / provenance review | [Wikipedia](https://commons.wikimedia.org/wiki/File:Silhouette-plot-orange.png) |

### sec_05-05-DBSCAN.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w07-img/arbitrary_shape.png` | Authorship unverified | Arbitrary shape clusters |
| `../resources/w07-img/dbscan_key_concept.png` | Authorship unverified | Key concepts of DBSCAN. (minPoint = 4) |
| `../resources/w07-img/about_reachable.png` | Authorship unverified | Abour reachable |
| `../resources/w07-img/dbscan_type_of_points.png` | Authorship unverified | Types of points: The cores, borders, and noises |
| `../resources/w07-img/dbscan_clusters.png` | Authorship unverified | The clusters |
| `../resources/w07-img/dbscan-demo_knn.png` | Authorship unverified | Demo using KNN |
| `../resources/w07-img/clustering_analysis_sample2.jpg` | Linked source / provenance review | A Modified DBSCAN Clustering Method to Estimate Retail Center Extent. [Pavlis et al. 2017](https://doi.org/10.1111/gean.12138) |

### sec_05-06-Visualising-Clusters.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w07-img/point_color.png` | Authorship unverified | Point colours |
| `../resources/w07-img/convex_hull.png` | Authorship unverified | Convex hull |
| `../resources/w07-img/standard_ellipse.png` | Authorship unverified | Standard ellipse |
| `../resources/w07-img/voronoi_polygon.png` | Authorship unverified | Voronoi polygon |

### chapter-6-areal_pattern.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w08-img/recap-1a.drawio.png` | Authorship unverified | What we have learnt: The patterns of statistical values and the patterns of locations. |
| `../resources/w08-img/recap-1b.drawio.png` | Authorship unverified | What we have learnt: The intersection---location of values, values of locations. |

### sec_06-01-Spatial-Autocorrelation.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/original/spatial-values-structured.svg` | Original (reproducible source) | A synthetic spatial pattern: nearby cells have similar values. Each category occurs 16 times. These are illustrative values, not observations from a real place. |
| `../resources/original/spatial-values-permutation.svg` | Original (reproducible source) | Random permutation keeps the spatial units and the set of values fixed, but reshuffles which value belongs to each unit. The histogram is unchanged; the spatial arrangement changes. |
| `../resources/original/spatial-values-three-permutations.svg` | Original (reproducible source) | Three independent permutations of the same values. Chance can produce small local groupings, so visual impressions alone are insufficient evidence of spatial dependence. |
| `../resources/w08-img/grid_positive_spatial_autocor.png` | Authorship unverified | Similar values (either high or low) are closer to each other on the right, compared to the random pattern (left). |
| `../resources/w08-img/grid_negative_spatial_autocor.png` | Authorship unverified | On the right, the dissimilar values are closer to each other, generating checkerboard-like pattern. |

### sec_06-02-Statistical-Spatial-Testing.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/original/rook-polygons.svg` | Original (reproducible source) | Six synthetic spatial units. Two units are rook neighbours when they share an edge of non-zero length; touching only at a point does not count. |
| `../resources/original/rook-neighbour-graph.svg` | Original (reproducible source) | The same units represented as a graph. Links connect 1–2, 1–4, 1–5, 2–4, 2–5, 3–5, 3–6 and 4–5. These are exactly the non-zero pairs in the symmetric matrix below. |
| `../resources/w08-img/demo_contiguity.png` | Authorship unverified | Using the chess concept to define who are the neighbors. |
| `../resources/w08-img/Rook_vs_Queen_Contiguity.png` | Authorship unverified | Top: Based on rook contiguity, the Chong Boon Subzone has 4 neighboring subzones. Bottom: Based on queen contiguity, the same Chong Boon Subzone has 8 neighboring subzones (4 additional). |
| `../resources/w08-img/higher_order_Contiguity.png` | Authorship unverified | Top: Second level (k=2) contiguity for rook and queen. Bottom: Second level contiguity with lower level ($k \leq 2$). |
| `../resources/w08-img/distance_based_1200m.png` | Authorship unverified | Set a distance band (e.g., 2000 m), draw a buffer as a neighborhood, those spatial units (with their centroid) fall within the buffer are considered neighbors, regardless of the spatial contiguity/adjacency. |
| `../resources/w08-img/distance_based_differ_size.png` | Authorship unverified | When the size of spatial units vary, the same distance band may generate different numbers of neighbors. E.g., for Fort Canning (left), 1200 m (top) and 1500 m (bottom) distance bands can identify 16 and 23 neighbors, respectively; whereas for Holland Road, the same distance bands can find 0 and 1 neighbor. |
| `../resources/w08-img/knn_example.png` | Authorship unverified | Regardless of variation in distance and spatial contiguity, the k-nearest neighbor approach will sort the neigbors by distance, then select the same number of neighbors (k=4 for top and k=12 bottom). The neighborhood area sizes will be different, depending on the area size of the spatial unit and its nearby units. |

### sec_06-03-Morans-I.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w08-img/morans_i_goals.png` | Linked source / provenance review | See [Global Moran's I (ArcGIS)](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/spatial-autocorrelation.htm). |
| `../resources/w08-img/moran-result-demo.png` | Linked source / provenance review | [see here for more details on the calculation of z-value](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/h-how-spatial-autocorrelation-moran-s-i-spatial-st.htm) |
| `../resources/w08-img/morans_I_example-1.png` | Authorship unverified | Example of Moran's scatter plot |
| `../resources/w08-img/permutation_distribution.png` | Authorship unverified | A demo of the permutation distribution. The observed value (orange vertical line) is far higher than the distribution derived from the random permutations. |
| `../resources/w08-img/demo_weekday.png` | Authorship unverified | Moran's I scatter plot of the bus ridership |
| `../resources/w08-img/moran-i-weekday_morningpeak.png` | Authorship unverified | 999 times permutation is generated. The observed value (vertical dash line) is somewhere at a higher value range of the distribution. |

### sec_06-04-Local-Moran.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w09-img/guerry_data.png` | Authorship unverified | The data distribution (based on Natural Breaks). |
| `../resources/w09-img/guerry_significant_map.png` | Authorship unverified | The Local Significance Map |
| `../resources/w09-img/guerry_significant_map_scatter.png` | Authorship unverified | Use the quadrants: For those significant (the map on the right), check the position of the spatial unit in the scatter plot: on top right indicates HH, bottom left LL. |
| `../resources/w09-img/guerry_I_cluster_map.png` | Authorship unverified | The Local Cluster Map |
| `../resources/w09-img/guerry_I_cluster_map_sensitivity.png` | Authorship unverified | Top: p-value < 0.05; bottom: p-value < 0.01 |
| `../resources/w09-img/guerry_local_outliers_HL.png` | Authorship unverified | The locations of HL outliers and their neighbors. |
| `../resources/w09-img/guerry_local_outliers_LH.png` | Authorship unverified | The locations of LH outliers and their neighbors. |
| `../resources/w09-img/guerry_local_cluster_HH.png` | Authorship unverified | The locations of HH clusters and their neighbors. |
| `../resources/w09-img/guerry_local_cluster_LL.png` | Authorship unverified | The locations of LL clusters and their neighbors. |

### sec_06-05-Gearys-C-and-Local-C.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w09-img/guerry_data.png` | Authorship unverified | The data distribution (based on Natural Breaks). |
| `../resources/w09-img/guerry_LC_significant_map.png` | Authorship unverified | Local Significance Map |
| `../resources/w09-img/guerry_C_cluster_map.png` | Authorship unverified | Local Cluster Map |
| `../resources/w09-img/guerry_C_cluster_map_sensitivity.png` | Authorship unverified | Sensitivity Analysis |
| `../resources/w09-img/guerry_I_C_cluster_map_sensitivity.png` | Authorship unverified | Comparison between local Moran's I and local Geary's C |

### sec_06-06-Getis-Ord-G.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w09-img/guerry_LG_significant_map.png` | Authorship unverified | Significance Maps |
| `../resources/w09-img/guerry_LG_cluster_map.png` | Authorship unverified | Cluster Maps |
| `../resources/w09-img/recap-1c.drawio.png` | Authorship unverified | Inline image |

### chapter-7-geovisualisation.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w11-img/recap-overall.drawio.png` | Authorship unverified | Inline image |

### sec_07-01-Geospatial-Data-Storytelling.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w11-img/geospatial-data-storytelling.png` | Authorship unverified | Geospatial Data Storytelling |
| `../resources/w11-img/compelling-data-story.png` | Authorship unverified |  |

### sec_07-02-Key-Components-of-Maps.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w01-img/drawing_sizes_1a.png` | Authorship unverified | The same map export with different size, squeezed to the same display size. |
| `../resources/w01-img/drawing_sizes_1b.png` | Authorship unverified | The same 4 maps, zoomed-in. |
| `../resources/w01-img/drawing-fonts.png` | Authorship unverified | Some example of Sans-Serif fonts (left) and Serif fonts (right). |
| `../resources/w01-img/text_elements.png` | Authorship unverified | Text elements. |
| `../resources/w01-img/US_temperature_map.png` | Linked source / provenance review | Temperature of colours. Source: NASA Earth Observatory: [Arctic Chill Sweeps U.S.](https://earthobservatory.nasa.gov/images/152333/arctic-chill-sweeps-us) |
| `../resources/w01-img/matplotlib-colors.png` | Linked source / provenance review | Some example of colormaps from [Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html). |
| `../resources/w01-img/seaborn-qualitative.png` | Linked source / provenance review | Various qualitative colormap from [Seaborn](https://seaborn.pydata.org/tutorial/color_palettes.html). |
| `../resources/w01-img/morphing_map_project.png` | Linked source / provenance review | [Try and view the differences of various projections in [The Morphing Map Project](https://wcchin.github.io/map_projection/). |
| `../resources/w01-img/varying_projections.png` | Authorship unverified | The four countries in three different projections. |
| `../resources/w01-img/drawing_continuous_discrete.png` | Authorship unverified | Inline image |
| `../resources/w01-img/temperature-of-greys.png` | Authorship unverified | Inline image |

### sec_07-03-Visual-Hierarchy.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w11-img/map_elements_example.png` | Linked source / provenance review | Example of map elements. [source: ESRI](https://mgimond.github.io/Spatial/good-map-making-tips.html) |
| `../resources/w11-img/example_bad_map.jpg` | Linked source / provenance review | [source: Chapter 7 Good Map Making Tips](https://mgimond.github.io/Spatial/good-map-making-tips.html) |
| `../resources/w11-img/example_bad_map_improved.jpg` | Linked source / provenance review | [source: Chapter 7 Good Map Making Tips](https://mgimond.github.io/Spatial/good-map-making-tips.html) |
| `../resources/w11-img/visual_hierarchy.png` | Linked source / provenance review | Designing visual (for web UI). [Source](https://clay.global/blog/web-design-guide/visual-hierarchy-web-design) |
| `../resources/w11-img/what-is-visual-hierarchy-in-web-design.jpg` | Linked source / provenance review | Visual design. [Source](https://wpdean.com/what-is-visual-hierarchy-in-web-design/) |
| `../resources/w11-img/size_hierarchy.jpg` | Linked source / provenance review | How size affect visual. [Source](https://admiral.digital/what-is-visual-hierarchy-and-why-is-it-important/) |
| `../resources/w11-img/Scale-organizes-content-by-size.png` | Linked source / provenance review | How size affect visual. [Source](https://visme.co/blog/visual-hierarchy/) |
| `../resources/w11-img/Fonts-organize-design-01.png` | Linked source / provenance review | How size of fonts affect visual. [Source](https://visme.co/blog/visual-hierarchy/) |
| `../resources/w11-img/colour_order.png` | Linked source / provenance review | The order of colours. [Source](https://clay.global/blog/web-design-guide/visual-hierarchy-web-design) |
| `../resources/w11-img/Color-and-contrast-draw-attention-and-create-harmony.png` | Linked source / provenance review | How colour and contrast draw attention and create harmony. [Source](https://visme.co/blog/visual-hierarchy/) |
| `../resources/w11-img/different_color_mapbox.png` | Linked source / provenance review | [Screenshot from Mapbox Gallery, Community Templates](https://www.mapbox.com/gallery) |
| `../resources/w11-img/uiux_read_pattern.png` | Linked source / provenance review | Reading pattern in UIUX. [Source](https://www.interaction-design.org/literature/topics/visual-hierarchy) |
| `../resources/w11-img/uiux_read_pattern2.png` | Linked source / provenance review | Reading pattern in UIUX. [Source](https://www.interaction-design.org/literature/topics/visual-hierarchy?srsltid=AfmBOopgpNcuvrThNqPlsGQEKeRgygYpwrRwQ2TpCL0EJ9K2v1OSIOl5) |
| `../resources/w11-img/rule_of_third.png` | Linked source / provenance review | What is the rule of third. [Source](https://www.interaction-design.org/literature/article/the-rule-of-thirds-know-your-layout-sweet-spots) |
| `../resources/w11-img/Greenland-Husky-Rule-of-Thirds.webp` | Linked source / provenance review | What is the rule of third. [Source](https://www.capturelandscapes.com/the-rule-of-thirds-explained/) |
| `../resources/w11-img/image-5-ruleofthrid-min.jpg` | Linked source / provenance review | What is the rule of third. [Source](https://admiral.digital/what-is-visual-hierarchy-and-why-is-it-important/) |
| `../resources/w11-img/poster_rule_of_thirds.png` | Linked source / provenance review | Rule of third in poster design. [Source](https://www.artworkflowhq.com/resources/the-rule-of-thirds-in-graphic-design) |
| `../resources/w11-img/rule_of_third_KevinsGinMapGRID.jpg` | Linked source / provenance review | What is the rule of third. [Source](https://community.esri.com/t5/esri-training-blog/using-artistic-inspiration-for-cartographic/ba-p/903968) |
| `../resources/w11-img/processed-image-5.png` | Linked source / provenance review | What is the rule of third. [Source](https://community.esri.com/t5/esri-training-blog/using-artistic-inspiration-for-cartographic/ba-p/903968) |
| `../resources/w11-img/processed-image-6.png` | Linked source / provenance review | Example of rule of third in map. [Using tool](https://onlinephototools.com/image-tools/image-rule-of-thirds-grid-overlay-tool/). Map screen short on [Zoom Earth](https://zoom.earth/) |
| `../resources/w11-img/processed-image-1.png` | Linked source / provenance review | Example of rule of third in map. [Using tool](https://onlinephototools.com/image-tools/image-rule-of-thirds-grid-overlay-tool/). |
| `../resources/w11-img/processed-image-3.png` | Linked source / provenance review | Example of rule of third in map. [Using tool](https://onlinephototools.com/image-tools/image-rule-of-thirds-grid-overlay-tool/). |
| `../resources/w11-img/processed-image-4.png` | Linked source / provenance review | Example of rule of third in map. [Using tool](https://onlinephototools.com/image-tools/image-rule-of-thirds-grid-overlay-tool/). |
| `../resources/w11-img/processed-image-2.png` | Linked source / provenance review | Example of rule of third in map. [Using tool](https://onlinephototools.com/image-tools/image-rule-of-thirds-grid-overlay-tool/). |
| `../resources/w11-img/processed-image-7.png` | Linked source / provenance review | Example of rule of third in map. [Using tool](https://onlinephototools.com/image-tools/image-rule-of-thirds-grid-overlay-tool/). |
| `../resources/w11-img/common_aspect_ratios.png` | Authorship unverified | Landscape. |
| `../resources/w11-img/common_aspect_ratios2.png` | Authorship unverified | Portrait. |
| `../resources/w11-img/Space-provides-balance-emphasis-and-movement.png` | Linked source / provenance review | Spacing in design. [Source](https://visme.co/blog/visual-hierarchy/] |
| `../resources/w11-img/whitespace.jpg` | Linked source / provenance review | Spacing Definition. [Source](https://clay.global/blog/web-design-guide/visual-hierarchy-web-design] |
| `../resources/w11-img/whitespace_google.png` | Linked source / provenance review | White spacing in [Google](https://www.google.com/) |
| `../resources/w11-img/design_balance.png` | Linked source / provenance review | Spacing for balance in a map. [Source](https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/design-principles-for-cartography) |
| `../resources/w11-img/whitespace_NASA_artic.png` | Linked source / provenance review | Example of spacing. [Source](https://earthobservatory.nasa.gov/images/152333/arctic-chill-sweeps-us) |
| `../resources/w11-img/whitespace_OSM.png` | Linked source / provenance review | Example of spacing. [A spatio-temporal analysis investigating completeness and inequalities of global urban building data in OpenStreetMap](https://www.nature.com/articles/s41467-023-39698-6)) |
| `../resources/w11-img/color_bad.png` | Authorship unverified | Bad |
| `../resources/w11-img/color_improved.png` | Authorship unverified | Improved |

### sec_07-04-Tools.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w11-img/carto_webpage.png` | Linked source / provenance review | [Carto](https://carto.com/) |
| `../resources/w11-img/mapbox_3D.png` | Linked source / provenance review | Mapbox 3D buildings. [Mapbox](https://www.mapbox.com/) |
| `../resources/w11-img/kepler-gl.png` | Linked source / provenance review | [Kepler.gl](https://kepler.gl/) demo. [Demo link](https://wcchin.github.io/sg_HDB_price_map/hdb_map_filter.html) |
| `../resources/w11-img/flowmap-gl.png` | Linked source / provenance review | [Flowmap.gl](https://flowmap.gl/) demo. [Demo link](https://app.flowmap.city/public/67249d1d-4c21-40e3-8ddb-fd5124907c99) |
| `../resources/w11-img/plotly_dash-2.png` | Linked source / provenance review | Plot.ly Dash [webpage](https://plotly.com/examples/) |
| `../resources/w11-img/bokeh_webpage.png` | Linked source / provenance review | [Bokeh webpage](https://docs.bokeh.org/en/latest/) |
| `../resources/w11-img/storymap-js_webpage.png` | Linked source / provenance review | Storymap.js (Knight-lab) [webpage](https://storymap.knightlab.com/#examples) |
| `../resources/w11-img/odyssey-js_webpage.png` | Linked source / provenance review | Odyssey.js (by Cartodb) [webpage](https://cartodb.github.io/odyssey.js/) |

### sec_07-05-Geospatial-Ethics.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w12-img/code_of_ethics.png` | Authorship unverified | Screenshot of the GIS Code-of-Ethics page. |
| `../resources/w12-img/rules_of_conduct.png` | Authorship unverified | Screenshot of the Rules of Conduct page. |
| `../resources/w12-img/ethical_legal.png` | Authorship unverified | Ethics and legality |

### sec_07-06-A-Final-Closing-Remark.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w01-img/xkcd_cat_proximity.png` | Linked source / provenance review | [Cat Proximity (xkcd.com/231)](https://xkcd.com/231/). |
| `../resources/w01-img/drawing-data_info_insight.png` | Authorship unverified | Data, Information, Insights. |
| `../resources/w01-img/drawing-how_maps_are_used.png` | Authorship unverified | MacEachren's cartographic cube. |
| `../resources/w12-img/information_is_beautiful.png` | Authorship unverified | Screenshot of Information is Beautiful |
| `../resources/w12-img/data_viz_project.png` | Authorship unverified | Screenshot of Data Viz Project |
| `../resources/w12-img/bad-3d_bar.png` | Authorship unverified | Unnecessary 3D view. |
| `../resources/w12-img/bad-piechart.png` | Authorship unverified | A bar chart could be clearer. |
| `../resources/w12-img/bad-line_discrete.png` | Authorship unverified | Line plot used to show discrete data (not continuous). |
| `../resources/w12-img/bad-confusing.png` | Authorship unverified | Confusing composition --- what is the main message? |
| `../resources/w12-img/bad_visual_time_spiral.jpg` | Authorship unverified | Unnecessary spiral effect --- what is the main message? |
| `../resources/w12-img/bad-negative-values.png` | Authorship unverified | Negative values going up and/or down? |
| `../resources/w12-img/bad-color-palette-types.png` | Authorship unverified | Color palette choice & type of chart (bar? or just table). |
| `../resources/w12-img/bad-change_size_range.png` | Authorship unverified | Generated based on the relative diameters of their circles, not relative areas. It’s subtle but still misleading. |
| `../resources/w12-img/bad-color_category.jpg` | Authorship unverified | Inconsistent categories and colors. |
| `../resources/w12-img/bad-maps-numbers.jpg` | Authorship unverified | Distracting labels (numbers). |
| `../resources/w12-img/bad-maps-area_effect.jpg` | Authorship unverified | Confusing area effect. |
| `../resources/w12-img/how-3D-population.png` | Authorship unverified | Population (3D) in New York City. |
| `../resources/w12-img/how-3D-SFO-tree.png` | Authorship unverified | Tree density in San Francisco. |

### sec_04-A-Demonstration-point-pattern.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w05-img/gordon_square2.png` | Linked source / provenance review | Let's do a mind travel to  Gordon Square, London, UK. Source: [Google Map](https://maps.app.goo.gl/Qdb1K4hzyG485Btm8) |
| `../resources/w05-img/GordonSquare_individual_and_groups_xkcd.png` | Authorship unverified | Distribution of individuals and groups. |
| `../resources/w05-img/nna_compare_hist_gordon.png` | Authorship unverified | NNA result. |
| `../resources/w05-img/k_function_ci_gordon.png` | Authorship unverified | K-function result. |
| `../resources/w05-img/area_size.png` | Authorship unverified | Effect of different area. |
| `../resources/w05-img/edge_effect.png` | Authorship unverified | Edge Effect. |
| `../resources/w05-img/pop_at_risk.png` | Authorship unverified | Population at risk. |
| `../resources/w05-img/about_point_pattern_analysis Diagram.drawio.png` | Authorship unverified | Point pattern analysis. |

### sec_07-An-Example-accessibility.md

| Asset | Status | Caption / evidence |
| --- | --- | --- |
| `../resources/w11-img/example-1-link.png` | Linked source / provenance review | The demonstration page: [the link](https://wcchin.github.io/sg_health_access/) |
| `../resources/w11-img/network_flow_isp_clinic.png` | Authorship unverified | Estimated flows demonstrated with a static map. |
| `../resources/w11-img/flowmap-gl.png` | Linked source / provenance review | [Interactive Map Link](https://app.flowmap.city/public/67249d1d-4c21-40e3-8ddb-fd5124907c99) |
| `../resources/w11-img/sankey_flowmap-bokeh.png` | Linked source / provenance review | [Interactive Map Link](https://wcchin.github.io/sg_health_access/interactive/holoviews_sankey_pln_flow.html) |
| `../resources/w11-img/mobility-by-region.png` | Linked source / provenance review | [Interactive Map Link](https://wcchin.github.io/sg_health_access/#histogram) |
| `../resources/w11-img/accessibility-keplergl.png` | Linked source / provenance review | [Interactive Map Link](https://wcchin.github.io/sg_health_access/interactive/keplergl_accessibility_clinic.html) |
