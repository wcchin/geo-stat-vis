---
label: global-morans-i
---

# Moran’s I


When districts with relatively high household incomes appear close together, does the pattern extend to their specified neighbours? We need an income measure for each area, a definition of neighbours and a reference against which to assess that arrangement.

**Global Moran's I** summarises the association between values at locations and values at their specified neighbours. It turns the idea of spatial similarity from the preceding sections into a statistic. The word *global* matters: the result describes the study area as a whole, rather than identifying individual significant clusters.

## The regional question

Our running application asks: **Do areas with relatively high median household incomes in Peninsular Malaysia tend to have neighbours with similarly high incomes in 2022?** Use the same 92 mapped areas and DOSM median gross monthly household income introduced in Section 6.1. [^morans-source-1]

The question concerns area-level income estimates by household residence. A spatial association does not establish neighbour influence, explain household mobility or describe inequality within each area. We treat all 92 area estimates as observations; this is not a household-population-weighted analysis.

## What you should be able to do

After reading, you should be able to define a spatial lag; calculate Moran's I in a small example; explain its scatterplot; distinguish a statistic from evidence under a null model; and qualify a result using the data, scale and neighbourhood choices.

```{note} About the running example
The four-cell diagrams remain hypothetical and explain the calculation. The empirical results in Section 8 use Malaysian household income, with a full-detail boundary audit and a documented proximity graph. All chapter methods use the same 92 observations. FIRMS detection locations remain the separate Chapter 4 application.
```

Reading route: measurement → neighbours → arithmetic → scatterplot → inference → interpretation → sensitivity → self-check. Read alongside [Autocorrelation & Spatial Autocorrelation](sec_06-01-Spatial-Autocorrelation.md) and [Defining Distance and Neighbourhoods](sec_06-02-Statistical-Spatial-Testing.md).

## 1. Decide what each number represents

Define $x_i$ as **median gross monthly household income in 2022**, in nominal Malaysian ringgit, for mapped area $i$. Most units are administrative districts; Perlis, Kuala Lumpur and Putrajaya each contribute one observation, and the source includes Kecil Lojing. Every income estimate is matched once using state and district aliases. No area is dropped for having a low value.

The regional mean used by Moran's I is the mean of these 92 area estimates, approximately RM 5,296.83. It is not the mean income or median income of all households in the peninsula. Areas differ in household population, survey uncertainty and size. A district median does not imply that each resident household has that income.

### Match the observations to the geometry

The 2022 income table is combined with a boundary service retrieved in October 2026. This is not a reconstruction of 2022 geography. The display maps use generalized outlines, while full-detail geometries are retrieved separately to audit topology and derive interior representative points. The [analysis record](../datasets/malaysia_income_areal/README.md) preserves query details, source hashes and the matched data. [^morans-source-2]

Missing or unmatched estimates are not replaced with zero. Water and neighbouring countries are outside the included observation set. A mean-income alternative or a log transformation changes the variable and question; it is not a way to tune significance.

## 2. Give “nearby” a precise meaning

Before measuring similarity, decide which pairs of areas are neighbours. The full-detail boundary audit found overlaps and disconnected contiguity graphs, including an isolated Langkawi. Rather than silently excluding areas or patching contacts, the main example uses a **symmetric union of four-nearest-neighbour selections** between interior representative points in EPSG:3375. Connect a pair when either area selects the other; then row-standardise.

This retains all 92 observations in one connected graph. Union symmetrisation gives four to nine neighbours per area, rather than exactly four. A six-nearest-neighbour union graph provides the stated sensitivity comparison. These are geographical proximity relations, not commuting or income-transmission pathways. The rules were specified before calculating association.

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

For binary neighbours with row standardisation, this is their arithmetic mean. An area with median income RM 8,000 could have a lag of RM 5,000 if its selected neighbours average RM 5,000. The lag belongs to the focal cell, but its value is calculated from other cells. It is not a prediction and does not imply an effect from neighbours. [^morans-source-3]

### Edges, masks and isolated cells

Row standardisation gives each nonempty neighbour set total weight one. A neighbour of a four-neighbour area therefore receives weight 1/4, while a neighbour of a nine-neighbour area receives 1/9. The binary relation is symmetric, but the transformed numerical weights need not be.

The graph has 226 undirected links, no isolates and one component. Its median link length is approximately 36.65 km and the longest is 90.47 km. Representative points are geometric interior locations, not population centres; proximity can connect areas across water or barriers. Inspect those links when interpreting the result.

```{note} Pause and reason
A cell has values 2, 4 and 9 at its three neighbours. Its row-standardised lag is (2 + 4 + 9) / 3 = 5. The cell's own value is excluded. If an extra neighbour is added, both the neighbour set and the weights change.
```

Compare the primary four-neighbour union with the six-neighbour union on the same observations. A different graph answers a different proximity question. Choosing weights to maximise I would undermine interpretation.

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
:alt: Two hypothetical four-cell chains with attribute values 2, 2, 8, 8 and 2, 8, 2, 8; adjacent cells are linked.
:align: center

Hypothetical attribute values on the same four-cell chain. Only adjacent cells are neighbours. Both arrangements contain exactly two values of 2 and two of 8; all weights are row-standardised. These are synthetic values in arbitrary units, not measured district incomes.
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

For the income example, “high” means above the mean of the 92 area medians. It is not an official household income-group threshold. Quadrant membership is descriptive, not a local significance test. Several high-income areas may also influence the global slope strongly; examine the point cloud rather than reading the coefficient alone.

## 5. Compare the statistic with a null model

A positive coefficient describes similarity under the chosen weights. Whether that coefficient is unusual requires a reference. Our randomisation null holds the included cells and weights fixed and treats the observed values as exchangeable across those cells. It asks what I would look like under random reassignment of this same set of values.

A permutation leaves the histogram of cell values unchanged. It changes which cell receives which value. Recalculate I after each shuffle; do not recompute a new neighbour graph. This is attribute randomisation on fixed areas, not a simulation of households moving between districts.

```{figure} ../resources/original/morans-exact-permutations.svg
:label: morans-four-cell-permutations
:alt: Exact randomisation distribution for six distinct arrangements of two values of 2 and two of 8; two arrangements have Moran I equal to 0.5.
:align: center

Exact randomisation distribution for the hypothetical chain. There are six distinct arrangements of two 2s and two 8s. Each is equally likely; two produce I = 0.50. The right-tail exact probability is therefore 2/6 = 0.333.
```

This small example has a visibly ordered arrangement and a positive I, yet weak right-tail evidence because similarly high values are not rare under its null. Exhaustive enumeration includes the observed arrangement and uses its exact proportion; it does not need the Monte Carlo adjustment below.

### For a larger dataset: Monte Carlo permutations

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

Exchangeability is a substantive assumption. Major differences in urbanisation, household composition or income-generating conditions can make unrestricted shuffling an unconvincing baseline. Rejection shows incompatibility with this null, not proof of one income-generating mechanism.

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

For this application, report the variable, year, support, graph, coefficient and inference together: “Across the 92 mapped Peninsular Malaysian areas in 2022, median household incomes showed positive spatial association under the stated union-4NN weights and unrestricted reassignment reference.” Section 8 supplies the calculated coefficient and p-value.

This does not establish that one district's income causes its neighbours' incomes. Shared labour markets, accessibility, urbanisation and other regional conditions can contribute. Nor does a global result identify which individual areas have significant local relationships or describe household-level inequality.

### If the result is not significant

Do not conclude that incomes are spatially random in every sense. The test concerns a particular variable, support, neighbour rule, period and null. Opposing local patterns can offset each other in a global measure. A small coefficient can also have strong statistical evidence with many cells, so report magnitude alongside inference.

```{note} Keep the terms distinct
Global autocorrelation describes an overall association. Local cluster detection asks where unusually similar or contrasting neighbourhoods occur. Explaining income differences asks about underlying social and economic processes. These require different evidence.
```

## 7. Ask whether the finding survives reasonable choices

Spatial statistics depend on representation. A useful sensitivity analysis changes one defensible choice at a time and explains the question that changes with it. It should help readers understand the result, not search for a specification that crosses a significance threshold.

| Choice | Comparison or extension | Interpretive question |
| --- | --- | --- |
| Neighbour rule | Union 4NN versus union 6NN, completed below | Does broadening the proximity graph change the result? |
| Variable | Median versus mean household income, possible extension | Does the distributional summary matter? |
| Transformation | Raw income versus a documented log transformation, possible extension | How much do extreme estimates affect the summary? |
| Support and date | Alternative compatible units or a complete common year, possible extension | How do aggregation and period change the question? |
| Simulation seed | Repeat the same procedure, possible extension | Is Monte Carlo variability material near a threshold? |

A different support changes both the observations and the neighbour graph. Raw I values are not universally comparable measures of clustering strength across different spatial questions. A small p-value does not remove those differences.

### Do not build the answer into the data

Do not smooth the income estimates before the main calculation: smoothing already combines neighbouring values and can introduce the similarity being measured. If a smoothed variable is studied, state that different question explicitly. Do not exclude low-income areas or replace missing estimates with zeros to improve the appearance of a map.

The test treats published medians as the observed attributes. It does not propagate their household-survey estimation uncertainty. Boundary dates, unequal area populations and omitted geographic conditions remain substantive limits. A later official revision should be recorded as a data update, rather than silently replacing the saved snapshot.

## 8. Observed Peninsular Malaysia results

The [shared analysis record](../datasets/malaysia_income_areal/README.md) contains all 92 income estimates, full-detail geometry audit, representative coordinates, graph edges and results. All areal methods retain the same observations. The generalized boundaries are used only to draw maps; weights are reconstructed from the saved representative coordinates.

```{figure} ../resources/original/malaysia-income-support.png
:label: malaysia-income-support
:alt: Peninsular Malaysian median household income map beside the symmetric union four-nearest-neighbour graph on the same 92 mapped areas.
:align: center

Observed 2022 median gross monthly household income and the primary proximity graph. Income: DOSM; boundaries: PLANMalaysia. The sequential OrRd map uses the same fixed breaks as Section 6.1. Graph links show the selected proximity relation, not travel routes.
```

```{figure} ../resources/original/malaysia-income-moran.svg
:label: malaysia-income-moran
:alt: Moran scatterplot and permutation reference for median household incomes in 92 Peninsular Malaysian areas.
:align: center

Population-standardised income against its row-standardised lag. The through-origin slope is I = 0.6646. The reference uses 9,999 unrestricted permutations of the same 92 area estimates on the fixed graph, seed 5230.
```

Under union-4NN weights, **I = 0.6646**, with upper-tail Monte Carlo **p = 0.0001**. None of the 9,999 simulated statistics reached the observed value; 0.0001 is the Monte Carlo resolution limit, not a precisely estimated extreme tail. The unrestricted expectation is $-1/91\approx-0.0110$.

| Proximity graph | Global I | Upper-tail permutation p |
| --- | ---: | ---: |
| Symmetric union 4NN | 0.6646 | 0.0001 |
| Symmetric union 6NN | 0.6593 | 0.0001 |

Both specifications support positive association relative to the stated null, while the coefficients describe slightly different graphs. This consistency does not validate unrestricted exchangeability as a complete model of income generation or establish causation. The six-neighbour graph has 333 undirected links, six to eleven neighbours and no isolates. The remaining sensitivity ideas above are extensions, not completed results.

The [shared income notebook](../notebooks/malaysia-income-areal-self-study.ipynb) reproduces the graph, figures, global and local comparisons. The following sections keep the same income observations while stating each statistic's normalisation and self-inclusion convention.

## 9. Check your understanding

### Try these questions first

**1.** Two neighbouring cells both have below-average income. Does their cross-product contribute positively or negatively to Moran's I? Explain without using a map colour.

**2.** A cell has value 8 and two neighbours with values 2 and 8. What is its row-standardised spatial lag? What information does the lag omit?

**3.** Can an HH point in a Moran scatterplot be called a statistically significant hotspot? What extra analysis would be needed?

**4.** Under our permutation null, which of the following changes: area geometry, the set of income estimates, the neighbour graph, or the assignment of estimates to areas?

**5.** In 999 random permutations, 19 statistics are at least as large as the observed I. What is the right-tail Monte Carlo p-value? Is it the probability that the null hypothesis is true?

**6.** Why might a map smoothed before analysis give a misleading first demonstration of spatial autocorrelation?

**7.** Suppose Peninsular Malaysia and another region have different Moran coefficients. What must you inspect before interpreting this as a difference in spatial organisation?

```{dropdown} Check your answers


**1.** Positive: both deviations from the mean are negative, and their product is positive. Similarity includes low-low relationships, not only high-high ones.

**2.** The lag is (2 + 8) / 2 = 5. It summarises the neighbour values but conceals their contrast: both neighbours need not have the mean value.

**3.** No. HH describes signs relative to the overall mean. Local inference requires a defined local statistic, a suitable null and attention to multiple testing. The next section develops that question.

**4.** Only the assignment changes. The locations, graph and multiset of values remain fixed.

**5.** (19 + 1) / (999 + 1) = 0.020. It estimates a tail probability for the statistic under the specified randomisation procedure; it is not a posterior probability for the null.

**6.** Smoothing introduces neighbour similarity through processing, so the analysis would partly measure that construction.

**7.** Check variable definitions, observation period and source definitions, spatial support, weights, n, exclusions, distribution and inferential conventions. The coefficients alone are insufficient.

```

**Transfer task.** Explain how using finer spatial units around Kuala Lumpur would change the support, variable estimates and graph. Why would the new coefficient not be a direct measurement of the same district-level question?

## Continue the inquiry

The [next section on LISA and Local Moran’s I](sec_06-04-Local-Moran.md) asks where local patterns occur. The income map, spatial lag, scatterplot and permutation reference above provide the shared regional input. Continue with the same areas and weights, keeping global and local inferential questions distinct.

## Sources and further reading

[^morans-source-1]: [DOSM. Household Income by Administrative District. Variable definitions, official table and survey context.](https://open.dosm.gov.my/data-catalogue/hh_income_district)

[^morans-source-2]: [PLANMalaysia. Administrative district boundary service. Full-detail query and topology audit are documented in the analysis record.](https://gisdev.planmalaysia.gov.my/server/rest/services/Hosted/Data_Sempadan_Daerah/FeatureServer/0)

[^morans-source-3]: [libpysal. lag_spatial documentation. Definition and row-standardised neighbour average.](https://pysal.org/libpysal/stable/generated/libpysal.weights.lag_spatial.html)

[^morans-source-4]: [Anselin, L. GeoDa Workbook: Global Spatial Autocorrelation (1). Further explanation of the statistic, plot and randomisation.](https://geodacenter.github.io/workbook/5a_global_auto/lab5a.html)

[^morans-source-5]: [PySAL esda. Moran, version 2.9 documentation. Analytical and permutation output fields.](https://pysal.org/esda/v2.9.0/source/generated/esda.Moran.html)

[^morans-source-6]: [PySAL esda. Development documentation for Moran. Version-dependent configuration of permutation alternatives.](https://pysal.org/esda/dev/generated/esda.Moran.html)

The four-cell figures are original calculations from the stated hypothetical dataset. Their reproducible source is [`scripts/draw_morans_figures.py`](https://github.com/wcchin/geo-stat-vis/blob/main/scripts/draw_morans_figures.py).

The empirical income figures use [`scripts/malaysia_income_analysis.py`](https://github.com/wcchin/geo-stat-vis/blob/main/scripts/malaysia_income_analysis.py) and the attributed source snapshot. They are distinct from the hypothetical four-cell diagrams.
