---
label: global-morans-i
---

# Moran’s I


When we see many fire detections close together on a map, what exactly have we learned? We have identified a visible concentration of observations. To ask whether areas with high fire activity tend to have similarly high-activity neighbours, we need a variable for each area, a definition of neighbours and a reference against which to assess the resulting pattern.

**Global Moran's I** summarises the association between values at locations and values at their specified neighbours. It turns the idea of spatial similarity from the preceding sections into a statistic. The word *global* matters: the result describes the study area as a whole, rather than identifying individual significant clusters.

## The regional question

Our running application asks: **During September 2026, do grid cells with high satellite-detected fire activity in Sumatra tend to be near cells with similarly high activity?** This is motivated by regional haze. An official 19 September update reported smoke from Kalimantan and southern Sumatra drifting towards Singapore. [^morans-source-1]

This question concerns the geography of fire activity. Explaining haze exposure in Malaysia or Singapore requires additional evidence about emissions, winds and atmospheric transport. A spatial autocorrelation statistic alone cannot establish the origin or destination of smoke.

## What you should be able to do

After reading, you should be able to define a spatial lag; calculate Moran's I in a small example; explain its scatterplot; distinguish a statistic from evidence under a null model; and qualify a result using the data, scale and neighbourhood choices.

```{note} About the running example
The four-cell diagrams remain explicitly hypothetical and explain the calculation. The observed South Sumatra application is now included in Section 8 below: a separate, attributed September 2026 snapshot is aggregated to 48 retained cells. Read the source and observation limitations with the empirical results; do not confuse them with the four-cell arithmetic.
```

Reading route: measurement → neighbours → arithmetic → scatterplot → inference → interpretation → sensitivity → self-check. Read alongside [Autocorrelation & Spatial Autocorrelation](sec_06-01-Spatial-Autocorrelation.md) and [Defining Distance and Neighbourhoods](sec_06-02-Statistical-Spatial-Testing.md).

## 1. Decide what each number represents

A satellite detection is an observation made by an instrument at a particular time. It is not automatically a distinct fire event. One persistent fire can be observed repeatedly, and a detection does not by itself establish that the land cover is forest. Our variable is therefore called **satellite-detected fire activity**, rather than the number of forest fires.

### From detections to an areal variable

For the Sumatra example, place a regular grid in a suitable projected coordinate system and count qualifying detections inside each retained cell during 1–30 September 2026. Define $x_i$ as that count for cell i. For a confirmatory analysis, fix the satellite product, confidence filter, period and study boundary before inspecting Moran's I. Our two teaching windows were selected after exploratory inspection, so their tests are illustrative rather than prespecified regional hypotheses. A point-location map explains the input; the count map shows the variable actually analysed.

A practical starting design uses 20 km cells, with 10 km cells as a planned sensitivity comparison. Grid origin matters too: moving the same grid changes allocation near its edges. Retain a documented land mask, and decide explicitly how to handle coastal cells and offshore islands. Partial land cells have less land available for detections, so cell counts are not perfectly comparable merely because the original grid squares have equal area.

| Record or cell | Meaning and treatment |
| --- | --- |
| Retained land cell, count 0 | No qualifying detection in the selected records. This does not establish that no fire occurred. Keep the cell. |
| Ocean outside the land mask | Outside the analytical population. Do not insert an artificial zero. |
| Missing or unusable observations | A data limitation, not a zero. Record the issue and decide how it affects the analysis. |
| Coastal or isolated land cell | Inspect land fraction and neighbours. Apply an explicit inclusion rule; report its consequences. |

### Counts, rates and transformations ask different questions

Raw counts describe detected activity per retained cell. Detections per square kilometre of land adjust for land area, but tiny land fractions can produce unstable rates. A log(1 + count) transformation reduces the influence of very large counts; it changes the variable and therefore the estimand. It is a sensitivity analysis, not a device for obtaining a preferred p-value.

NASA FIRMS provides archived detections in downloadable formats. Recent near-real-time records can later be replaced by standard science-quality data, so preserve the retrieval date and exact source snapshot. [^morans-source-2] If the intended variable is burned fraction rather than detections, use a burned-area product and define that different question.

## 2. Give “nearby” a precise meaning

Before measuring similarity, decide which pairs of cells count as neighbours. For an initial grid example, use **first-order rook contiguity**: retained cells are neighbours when they share a grid edge. This makes the rule easy to inspect. Queen contiguity also includes corner contacts. Neither rule is automatically the physical pathway through which fire or smoke moves.

Write $a_{ij}=1$ for a selected neighbour pair and $0$ otherwise. Set $a_{ii}=0$: a cell is not its own neighbour. With $k_i=\sum_j a_{ij}>0$ neighbours, row standardisation gives

$$
w_{ij}=\frac{a_{ij}}{k_i},\qquad \sum_j w_{ij}=1.
$$

Each nonempty row then sums to one.

### A spatial lag is a neighbour summary

The spatial lag of x at cell i is the weighted sum of neighbour values:

$$
\left(W\mathbf{x}\right)_i = \sum_{j=1}^{n} w_{ij}x_j
$$

For equally weighted rook neighbours with row standardisation, this is their arithmetic mean. A cell containing 8 detections might have a lag of 2 if its neighbours each contain only 2. The lag belongs to the focal cell, but its value is calculated from other cells. It is not a prediction and does not imply an effect from neighbours. [^morans-source-3]

### Edges, masks and isolated cells

An interior grid cell can have four rook neighbours; a boundary cell may have fewer. Row standardisation gives the available neighbours a total weight of one, so each neighbour of a two-neighbour cell receives greater weight than each neighbour of a four-neighbour cell. The choice therefore affects how local relationships contribute to the global statistic.

Check the neighbour graph after applying the land mask. An island or a narrow coastal fragment can have no rook neighbours. The simplified formula and slope interpretation here assume every included cell has at least one neighbour. The regional implementation must document exclusions or choose a justified alternative rule. Do not silently assign a zero lag and continue as though the same assumptions still hold.

```{note} Pause and reason
A cell has values 2, 4 and 9 at its three neighbours. Its row-standardised lag is (2 + 4 + 9) / 3 = 5. The cell's own value is excluded. If an extra neighbour is added, both the neighbour set and the weights change.
```

For the fire application, compare rook and queen only after inspecting the graph. A distance-based rule would instead answer a question about a specified spatial reach. A graph chosen to yield the largest I would undermine the intended interpretation.

## 3. Build Moran's I from cross-products

Let $d_i=x_i-\bar{x}$, where $\bar{x}$ is the mean across the included cells. Two neighbouring cells both above the mean give a positive cross-product. Two below the mean also give a positive product. A pair on opposite sides of the mean gives a negative product.

$$
I = \frac{n}{S_0}
\frac{\displaystyle\sum_{i=1}^{n}\sum_{j=1}^{n}w_{ij}(x_i-\bar{x})(x_j-\bar{x})}
{\displaystyle\sum_{i=1}^{n}(x_i-\bar{x})^2},
\qquad S_0=\sum_{i=1}^{n}\sum_{j=1}^{n}w_{ij}.
$$

Here n is the number of included cells and $S_0$ is the sum of all weights. The numerator combines neighbour cross-products; the denominator scales by overall variation. A constant variable has a zero denominator and cannot be analysed with this statistic.

```{figure} ../resources/original/morans-chain.svg
:label: morans-four-cell-chain
:alt: Two hypothetical four-cell chains with counts 2, 2, 8, 8 and 2, 8, 2, 8; adjacent cells are linked.
:align: center

Hypothetical counts on the same four-cell chain. Only adjacent cells are neighbours. Both arrangements contain exactly two values of 2 and two of 8; all weights are row-standardised. These are not Indonesian observations.
```

| Cell | $x_i$ | $d_i=x_i-5$ | $(W\mathbf{d})_i$ | $d_i(W\mathbf{d})_i$ |
| --- | --- | --- | --- | --- |
| A | 2 | −3 | −3 | 9 |
| B | 2 | −3 | 0 | 0 |
| C | 8 | 3 | 0 | 0 |
| D | 8 | 3 | 3 | 9 |

Each row sums to one, so $S_0=n=4$. The sum of $d_i(W\mathbf{d})_i$ is $18$ and the sum of $d_i^2$ is $36$. Consequently,

$$
I=\frac{4}{4}\times\frac{18}{36}=0.50.
$$

For the alternating arrangement, every cell contrasts with its neighbours and $I=-1.00$.

Positive I indicates an overall tendency towards similar neighbour values; negative I indicates contrast. The attainable range depends on the weights. Moran's I is not an ordinary correlation coefficient with universal bounds of −1 and +1.

The sum over i and j uses ordered neighbour relationships. Do not count each undirected edge only once while retaining the full-matrix $S_0$. With binary rather than row-standardised weights, the first arrangement gives $I=1/3$: changing weights changes the calculation.

## 4. Read the Moran scatterplot

For a plot with comparable axes, standardise the variable using one positive standard deviation $s$ for every observation:

$$
z_i=\frac{x_i-\bar{x}}{s}.
$$

Plot each cell's z on the horizontal axis and its spatial lag Wz on the vertical axis. A cell appears once; its neighbours are summarised in its vertical coordinate.

```{figure} ../resources/original/morans-scatter.svg
:label: morans-four-cell-scatter
:alt: Moran scatterplot for the hypothetical four-cell chain, with standardised values on the horizontal axis and spatial lag on the vertical axis.
:align: center

The same hypothetical arrangement [2, 2, 8, 8], standardised using the population standard deviation s = 3. A and B have z = −1; C and D have z = 1. The line is fitted through the origin.
```

With nonempty row-standardised weights, $S_0=n$, and the through-origin slope is

$$
\hat{\beta}=\frac{\sum_i z_i(W\mathbf{z})_i}{\sum_i z_i^2}=I.
$$

Without that weighting condition, the slope needs the $n/S_0$ factor. The axes show $z_i$ and $(W\mathbf{z})_i$; independently standardising the vertical axis would change the slope.

| Quadrant | Reading relative to the overall mean |
| --- | --- |
| HH: upper right | Above-average focal value; above-average neighbour summary. |
| LL: lower left | Below-average focal value; below-average neighbour summary. |
| LH: upper left | Below-average focal value; above-average neighbour summary. |
| HL: lower right | Above-average focal value; below-average neighbour summary. |

A and D lie in LL and HH respectively. B and C lie on the horizontal axis because each has one low and one high neighbour; their neighbour deviations cancel. Do not force axis points into a strict high/low category.

For Sumatra, “high” would mean above the mean of the selected fire variable, cells and month. It would not mean an official fire-danger threshold. Quadrant membership is descriptive, not a local significance test. Several high-activity cells may also influence the global slope strongly; examine the point cloud rather than reading the coefficient alone.

## 5. Compare the statistic with a null model

A positive coefficient describes similarity under the chosen weights. Whether that coefficient is unusual requires a reference. Our randomisation null holds the included cells and weights fixed and treats the observed values as exchangeable across those cells. It asks what I would look like under random reassignment of this same set of values.

A permutation leaves the histogram of cell values unchanged. It changes which cell receives which value. Recalculate I after each shuffle; do not recompute a new neighbour graph. This is an attribute-randomisation test, not a simulation of random fire ignition points or smoke movement.

```{figure} ../resources/original/morans-exact-permutations.svg
:label: morans-four-cell-permutations
:alt: Exact randomisation distribution for six distinct arrangements of two values of 2 and two of 8; two arrangements have Moran I equal to 0.5.
:align: center

Exact randomisation distribution for the hypothetical chain. There are six distinct arrangements of two 2s and two 8s. Each is equally likely; two produce I = 0.50. The right-tail exact probability is therefore 2/6 = 0.333.
```

This small example has a visibly ordered arrangement and a positive I, yet weak right-tail evidence because similarly high values are not rare under its null. Exhaustive enumeration includes the observed arrangement and uses its exact proportion; it does not need the Monte Carlo adjustment below.

### For a larger grid: Monte Carlo permutations

Specify the alternative before analysis. For our proposed question, use a **right-tailed test** for larger $I$. With $B$ simulated random permutations and $b$ statistics at least as large as the observed $I$, report

$$
p_{\mathrm{right}}=\frac{b+1}{B+1},\qquad b=\sum_{r=1}^{B}\mathbf{1}\!\left(I^{(r)}\geq I_{\mathrm{obs}}\right).
$$

With $B=999$, the smallest reportable value is $0.001$, not zero. This finite Monte Carlo estimate is often called a *pseudo-p-value*. [^morans-source-4]

Under unrestricted random reassignment, zero self-weights and a nonconstant variable,

$$
\mathbb{E}[I]=-\frac{1}{n-1}.
$$

For four cells it is $-1/3$, not zero. The exact example verifies this expectation. More permutations improve numerical resolution and Monte Carlo stability; they do not guarantee a smaller p-value.

Exchangeability is a substantive assumption. Major differences in land cover, land fraction or detectability can make unrestricted shuffling an unconvincing baseline. Rejection shows incompatibility with this null, not proof of one fire-generating mechanism.

## 6. Separate statistical outputs from conclusions

A complete result combines the variable, study population, weights, coefficient and inferential convention. A bare statement that “Moran's I is significant” leaves the reader unable to assess what was tested.

| Output | How to read it |
| --- | --- |
| Observed I | Magnitude and direction of the global cross-product association for the specified variable and weights. |
| E[I] | Reference expectation under the stated null; generally slightly negative with zero self-weights. |
| `p_norm` | Analytical p-value using a normality-based variance and normal reference approximation. |
| `p_rand` | Analytical p-value using a randomisation-based variance and normal reference approximation. It is not a Monte Carlo permutation count. |
| Permutation p-value | Probability estimate from simulated reassignments, with the alternative, tail rule and number of permutations explicitly recorded. |

Software output names are not enough. PySAL distinguishes analytical and simulated quantities, and versions differ in how a permutation alternative is configured. The notebook should record the installed version and calculate the intended right-tail exceedance count explicitly, rather than assuming a default `p_sim` always represents our substantive test. [^morans-source-5] [^morans-source-6]

### What would a positive result support?

If the fire application yields a positive I and a small prespecified right-tail permutation p-value, a defensible conclusion would be: “For the retained Sumatra grid cells in September 2026, neighbouring values of the selected detection-count variable were more similar than expected under unrestricted reassignment of those values, using the stated weights.” This is a conditional reporting template, not an observed result.

It would not establish that fire spreads from one cell to the next. Similar activity may reflect shared conditions, land management, observation processes or broad geographical differences. Nor would it identify which cells are significant hotspots or demonstrate which fires contributed smoke to Singapore.

### If the result is not significant

Do not conclude that fires are spatially random in every sense. The test concerns a particular variable, support, neighbour rule, period and null. Opposing local patterns can offset each other in a global measure. A small coefficient can also have strong statistical evidence with many cells, so report magnitude alongside inference.

```{note} Keep the terms distinct
Global autocorrelation describes an overall association. Local cluster detection asks where unusually similar or contrasting neighbourhoods occur. Smoke-source attribution asks about transport and contribution. These require different evidence.
```

## 7. Ask whether the finding survives reasonable choices

Spatial statistics depend on representation. A useful sensitivity analysis changes one defensible choice at a time and explains the question that changes with it. It should help readers understand the result, not search for a specification that crosses a significance threshold.

| Choice | Planned comparison | Interpretive question |
| --- | --- | --- |
| Grid support | 20 km versus 10 km; document grid origin | Does the conclusion depend on aggregation scale? |
| Neighbour rule | Rook versus queen on the same retained cells | Does including diagonal relationships change the association? |
| Variable | Counts versus log(1 + counts) | Is the pattern dominated by a few very large values? |
| Coastal cells | Record land fraction; test one stated inclusion threshold | Are partial cells driving low-count patterns? |
| Period | September versus a separately defined month | How does the pattern change through time? |
| Random seed | Repeat the same Monte Carlo design with another seed | Is simulation variability material to the conclusion? |

Changing grid size changes n and the variable values. Changing weights changes which relationships receive attention. Their raw I values do not measure a universally comparable strength of clustering. A z-score or small p-value does not remove these differences in the spatial question.

### Do not build the answer into the data

Avoid smoothing a fire-count map before the main Moran calculation. Smoothing already combines nearby values and can manufacture or strengthen the similarity we are trying to describe. If a smoothed field is analysed, make that preprocessing and the changed question explicit.

Do not discard zero-count land cells merely because their removal gives a more dramatic map. Such a subset would describe spatial relationships among detected-active cells, rather than fire activity across the defined land grid. Likewise, filling the sea with zeros would introduce a large artificial low-activity region.

### Sampling and the observation process

Keep one satellite product and confidence convention throughout the main example. Record temporal coverage and known gaps. An absence of records can reflect both absence of detectable activity and limitations in observation. A visually coherent pattern is a reason to investigate these possibilities, not a substitute for checking them.

For current-year data, preserve the downloaded files and processing choices. A later science-quality refresh can change the counts; compare versions as a data revision rather than silently replacing the published result.

## 8. Observed South Sumatra results

The shared empirical analysis uses nominal/high-confidence **S-NPP VIIRS detections during 1–30 September 2026 UTC**, obtained through the public FIRMS mirror. It starts from the two adjoining 100 km windows introduced in Chapter 4 and their fifty 20 km cells. Retain only cells classified as full land by the saved generalized main-island boundary: two coastal cells containing 104 detections are excluded, leaving **48 cells and 6,097 detections**. This is a different support rule from the area-adjusted quadrat analysis, which retained the partial cells.

The [source record](../datasets/firms_areal/README.md) gives the input checksum, exclusions, conventions and complete results. The source is near-real-time version 2.0NRT; the September records have not been independently re-downloaded from the authenticated NASA archive. Full-land classification is approximate, and records on every date do not verify uniform or complete observation coverage.

```{figure} ../resources/original/firms-areal-support.svg
:label: firms-areal-support
:alt: Observed detection counts and rook neighbour counts on the retained South Sumatra grid, with two excluded coastal cells hatched.
:align: center

Observed values and the graph used for analysis. All retained cells have the same 400 km² grid area. There are 80 undirected rook links, one connected component and no isolates. Hatching marks exclusions rather than observed zero activity. The divider identifies the western and eastern teaching windows.
```

```{figure} ../resources/original/firms-moran-observed.svg
:label: firms-moran-observed
:alt: Moran scatterplot and global permutation reference for the 48 South Sumatra cell counts, with observed Moran I marked.
:align: center

The observed scatterplot uses population-standardised counts and row-standardised rook lags. Its through-origin slope is I = 0.2314. The reference is generated by 9,999 unrestricted permutations of the same 48 counts on the fixed graph, seed 5230.
```

For rook weights, **I = 0.2314**, with upper-tail Monte Carlo **p = 0.0085**. Under unrestricted reassignment, the expected I is $-1/47\approx-0.0213$. Thus the chosen summary shows greater neighbour similarity than the reference predicts for this exploratory region. This is not a statement that all high-count cells are significant local hotspots, that distinct fires attract one another, or that these detections caused haze in Singapore.

| Neighbour rule | Global I | Upper-tail permutation p |
| --- | ---: | ---: |
| Rook | 0.2314 | 0.0085 |
| Queen | 0.0889 | 0.0552 |

Queen adds diagonal relationships on the same retained cells and variable. Its graph has 148 undirected links and no isolates. The change in result should be reported: evidence under rook does not establish the same conclusion for every neighbour definition. These p-values use the same simulation count and seed, not a search for the most favourable graph. The 10 km, temporal and transformed-variable comparisons listed earlier remain possible extensions, not completed empirical checks.

Local analyses in the following pages use the same retained observations and neighbour relation, while stating each statistic's weighting and self-inclusion convention. The [shared notebook](../notebooks/firms-areal-self-study.ipynb) reproduces the figures and all recorded outputs.

## 9. Check your understanding

### Try these questions first

**1.** Two neighbouring cells both have below-average fire activity. Does their cross-product contribute positively or negatively to Moran's I? Explain without using a map colour.

**2.** A cell has value 8 and two neighbours with values 2 and 8. What is its row-standardised spatial lag? What information does the lag omit?

**3.** Can an HH point in a Moran scatterplot be called a statistically significant hotspot? What extra analysis would be needed?

**4.** Under our permutation null, which of the following changes: cell geometry, the set of counts, the neighbour graph, or the assignment of counts to cells?

**5.** In 999 random permutations, 19 statistics are at least as large as the observed I. What is the right-tail Monte Carlo p-value? Is it the probability that the null hypothesis is true?

**6.** Why might a map smoothed before analysis give a misleading first demonstration of spatial autocorrelation?

**7.** Suppose Sumatra and Kalimantan have different Moran coefficients. What must you inspect before interpreting this as a difference in spatial organisation?

```{dropdown} Check your answers


**1.** Positive: both deviations from the mean are negative, and their product is positive. Similarity includes low-low relationships, not only high-high ones.

**2.** The lag is (2 + 8) / 2 = 5. It summarises the neighbour values but conceals their contrast: both neighbours need not have the mean value.

**3.** No. HH describes signs relative to the overall mean. Local inference requires a defined local statistic, a suitable null and attention to multiple testing. The next section develops that question.

**4.** Only the assignment changes. The locations, graph and multiset of values remain fixed.

**5.** (19 + 1) / (999 + 1) = 0.020. It estimates a tail probability for the statistic under the specified randomisation procedure; it is not a posterior probability for the null.

**6.** Smoothing introduces neighbour similarity through processing, so the analysis would partly measure that construction.

**7.** Check variable definitions, observation period and product, grid support, land mask, weights, n, exclusions, distribution and inferential conventions. The coefficients alone are insufficient.

```

**Transfer task.** Return to the Peninsular Malaysian income map. Identify what would replace the fire-count variable, grid support and rook graph. Explain why the same formula can answer a different geographical question.

## Continue the inquiry

The [next section on LISA and Local Moran’s I](sec_06-04-Local-Moran.md) asks where local patterns occur. The observed map, spatial lag, scatterplot and permutation reference above now provide the shared regional input. Continue with the same cells and weights, keeping global and local inferential questions distinct.

## Sources and further reading

[^morans-source-1]: [Meteorological Service Singapore. Haze Situation Update, 19 September 2026. Regional motivation.](https://www.nea.gov.sg/media/news/advisories/index/haze-situation-update-19-september-2026)

[^morans-source-2]: [NASA FIRMS. Archive Download. Product availability, historical access and replacement of near-real-time records.](https://firms.modaps.eosdis.nasa.gov/download/)

[^morans-source-3]: [libpysal. lag_spatial documentation. Definition and row-standardised neighbour average.](https://pysal.org/libpysal/stable/generated/libpysal.weights.lag_spatial.html)

[^morans-source-4]: [Anselin, L. GeoDa Workbook: Global Spatial Autocorrelation (1). Further explanation of the statistic, plot and randomisation.](https://geodacenter.github.io/workbook/5a_global_auto/lab5a.html)

[^morans-source-5]: [PySAL esda. Moran, version 2.9 documentation. Analytical and permutation output fields.](https://pysal.org/esda/v2.9.0/source/generated/esda.Moran.html)

[^morans-source-6]: [PySAL esda. Development documentation for Moran. Version-dependent configuration of permutation alternatives.](https://pysal.org/esda/dev/generated/esda.Moran.html)

The four-cell figures are original calculations from the stated hypothetical dataset. Their reproducible source is [`scripts/draw_morans_figures.py`](https://github.com/wcchin/geo-stat-vis/blob/main/scripts/draw_morans_figures.py).

The empirical South Sumatra figures use [`scripts/firms_areal_analysis.py`](https://github.com/wcchin/geo-stat-vis/blob/main/scripts/firms_areal_analysis.py) and the attributed source snapshot. They are distinct from the hypothetical four-cell diagrams.
