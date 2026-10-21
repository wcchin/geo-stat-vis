---
label: local-morans-i
---

# LISA and Local Moran's I

## From an overall association to individual neighbourhoods

[Global Moran's I](sec_06-03-Morans-I.md) combines relationships across the included units. A positive result can coexist with a high-value cell among lower-valued neighbours, or a low-value cell beside a concentration of high values. A global coefficient does not identify those locations.

**Local Moran's I** examines a focal unit's deviation from the overall mean together with the deviations of its neighbours. It distinguishes local similarity from contrast, then asks whether the observed relationship is unusual under a location-specific reference. After reading, you should be able to calculate a local value, interpret the four quadrants, explain conditional permutation, and distinguish unadjusted from multiplicity-adjusted findings.

Anselin's **local indicators of spatial association (LISA)** framework connects local association with contributions to an overall measure. Local Moran provides a particularly direct decomposition. Not every statistic used for hotspot mapping has the same decomposition, so “local statistic” and “LISA” should not be used as interchangeable mathematical definitions.

## Keep the local-to-global scaling explicit

Let $d_i=x_i-\bar{x}$, $Q=\sum_i d_i^2$, $m_2=Q/n$, and $S_0=\sum_i\sum_jw_{ij}$, with $w_{ii}=0$. We use the population second-moment convention:

$$
I_i=\frac{d_i}{m_2}\sum_jw_{ij}d_j.
$$

Equivalently, if $z_i=d_i/\sqrt{m_2}$, then $I_i=z_i(W\mathbf{z})_i$. The sign comes from the product of the focal deviation and its spatial lag. The scale factor does not disappear when weights are row-standardised.

Combining this definition with the global statistic gives

$$
\sum_i I_i=S_0 I.
$$

With every row nonempty and standardised to sum to one, $S_0=n$, so the **mean of these local statistics equals global I**. Software may use a sample-variance convention involving $n-1$. That changes numerical scaling and the exact decomposition; record the convention before comparing outputs. Our reproducible implementation uses the equations on this page directly rather than relying on package label codes.

### A calculation from the four-cell chain

Return to the synthetic chain A–B–C–D with values $[2,2,8,8]$. The mean is 5, $m_2=9$, and row-standardised deviation lags are $[-3,0,0,3]$.

| Cell | $d_i$ | $(W\mathbf{d})_i$ | $I_i$ |
| --- | ---: | ---: | ---: |
| A | −3 | −3 | 1 |
| B | −3 | 0 | 0 |
| C | 3 | 0 | 0 |
| D | 3 | 3 | 1 |

Their mean is 0.5, agreeing with global I. B and C have zero lag because their low and high neighbours cancel. They are not thereby established to be random or unimportant. This example explains arithmetic, not local significance.

## Four configurations, followed by a test

| Configuration | Focal deviation | Neighbour lag | Sign of $I_i$ | Descriptive reading |
| --- | --- | --- | --- | --- |
| HH | Positive | Positive | Positive | High value with a high neighbour summary |
| LL | Negative | Negative | Positive | Low value with a low neighbour summary |
| HL | Positive | Negative | Negative | High value with a low neighbour summary |
| LH | Negative | Positive | Negative | Low value with a high neighbour summary |

“High” and “low” refer here to the overall mean of the selected variable and units, not an external danger or policy threshold. Points exactly on an axis require separate handling. A positive local statistic alone cannot distinguish HH from LL; use both deviations. A negative local statistic indicates contrast, not a negative original value.

Every non-axis observation has a descriptive quadrant, but only some may be unusual under a chosen local null. A scatterplot quadrant is not a significance classification, and a dark count-map cell is not automatically a statistically supported hotspot.

## A shared South Sumatra analysis

The chapter now uses an observed teaching snapshot from **1–30 September 2026**, retaining nominal/high-confidence S-NPP VIIRS detections. Start with the two adjoining 100 km squares used in the quadrat section and partition them into fifty 20 km cells. For the areal comparison, retain only cells classified as full land by the saved generalized boundary. This removes two coastal cells containing 104 detections, leaving **48 cells and 6,097 detections**. No cell is removed because it has a low or zero count.

These choices differ from the area-adjusted quadrat example, which retained both coastal cells. Here all retained cell areas are equal, so the count comparison does not introduce different ocean exposure. Classification as full land remains approximate because the source coastline is generalized. The exploratory region and filtering are documented in the [analysis record](../datasets/firms_areal/README.md).

Use a fixed rook graph with row-standardised weights: it has 80 undirected edges, one connected component, no isolates, and two to four neighbours per cell. The observed variable is a detection count, not burned area, distinct ignitions or forest-fire incidents. Repeated overpasses and uneven observation conditions remain relevant.

## Conditional permutation: what stays fixed?

For each focal cell $i$, retain its observed value, its neighbour slots and weights. Randomly reassign the other $n-1$ values to the other locations, then recompute $I_i$. With equal row weights, sampling $k_i$ distinct values without replacement for the neighbour slots gives the same local reference. Distinct records may have equal numerical values; sample indices, rather than deduplicating values.

Repeat independently for each focal cell. The simulations are local conditional references, not a single simultaneous shuffled map. The neighbours' original values are not held fixed. Holding the focal value fixed is also different from the unrestricted global permutation in Section 6.3.

For these pages we use 9,999 simulations, seed 5230, inclusive tails and the explicit two-sided convention

$$
p_{i,+}=\frac{1+\#\{I_i^{(b)}\geq I_i\}}{B+1},\qquad
p_{i,-}=\frac{1+\#\{I_i^{(b)}\leq I_i\}}{B+1},
$$

$$
p_{i,2}=\min\{1,\ 2\min(p_{i,+},p_{i,-})\}.
$$

This doubled-tail convention is conservative for discrete references and has minimum value 0.0002 here. A different tail rule can give different results; a package field named `p_sim` is not sufficient documentation. Positive versus negative observed $I_i$ should not be used to choose a tail retrospectively.

## Reading the observed results

```{figure} ../resources/original/firms-local-moran.svg
:label: firms-local-moran
:alt: Local Moran classifications for the 48-cell South Sumatra grid, comparing unadjusted two-sided permutation p-values with Benjamini–Hochberg adjusted values. Excluded coastal cells are hatched.
:align: center

Original observed-data analysis. Left: quadrant labels shown only where unadjusted two-sided p is at most 0.05. Right: the same results after a separate 48-test BH adjustment. Grey means not selected by that procedure; hatching means outside the retained support. Neither means no fire.
```

Four cells meet the unadjusted threshold: two HH and two LL. For example, R3C06 has 1,207 detections and an HH configuration, with unadjusted two-sided p = 0.0182. **None of the 48 cells is selected at BH-adjusted q ≤ 0.05**, and none meets the Bonferroni threshold. Thus the data offer exploratory local candidates under the unadjusted procedure, not multiplicity-adjusted discoveries at this level.

Cell identifiers count rows south to north and columns west to east. A classified focal cell is not the same as a delineated fire perimeter or a cluster membership assignment for individual detections. Neighbourhoods overlap, and their local statistics are related.

## Why multiple testing changes the map

Testing 48 locations creates more opportunities for small p-values than a single test. Under a complete null with valid tests at level 0.05, the expected number of false rejections is at most $48\times0.05=2.4$. This expectation does not require independence, but the joint error behaviour does depend on the tests' relationships.

**Bonferroni** compares each p-value with $0.05/48\approx0.00104$ and controls family-wise error without requiring independence, assuming valid individual p-values. **Benjamini–Hochberg (BH)** sorts the p-values and compares ordered $p_{(r)}$ with $r\alpha/48$ using a step-up rule. It targets false discovery rate under suitable assumptions. Spatially overlapping tests are dependent; ordinary BH is not a universal guarantee under arbitrary dependence. We show it as an exploratory adjustment and provide the Bonferroni comparison as well.

An adjusted q-value is not the probability that its cell is a false discovery. Nor does changing a threshold identify a different physical pattern: it changes the evidence rule applied to the same estimates. Do not tune the number of permutations, seed or weights until coloured cells appear.

## Relate local results back to global association

On the same rook graph, global I = 0.2314 with upper-tail permutation p = 0.0085. This does not contradict the absence of BH-selected local findings. The global test pools contributions into one statistic; the local analysis uses 48 conditional comparisons with a different inferential family.

Queen weights give global I = 0.0889 and upper-tail p = 0.0552. This sensitivity matters: the evidence concerns the chosen neighbour relationships, not a universal property of the region. Both graphs and all sensitivity outputs are saved. Low counts, broad intensity differences, clouds and repeat observations may affect either result.

## Check your reasoning

```{dropdown} 1. Can a positive local statistic describe low values?
Yes. A below-mean focal value with a below-mean neighbour lag is LL and gives a positive product.
```

```{dropdown} 2. What is fixed in the local conditional reference?
The focal value, observation support and weights. The other values are reassigned. The observed neighbour values are not fixed.
```

```{dropdown} 3. Do four unadjusted findings establish four corrected hotspots?
No. Two are LL rather than HH, and none survives the reported BH or Bonferroni procedure. State the exact inference rule.
```

```{dropdown} 4. Does an all-grey adjusted map prove the absence of local structure?
No. It reports no selected findings under that procedure. It does not prove the null or erase the observed variation.
```

## Reproduce and read further

The [shared areal notebook](../notebooks/firms-areal-self-study.ipynb) reproduces the retained grid, statistics, maps and sensitivity comparison from the repository snapshot. The [source and result record](../datasets/firms_areal/README.md) defines every calculation. These new empirical maps replace the earlier Guerry illustrations.

- **Foundation:** Anselin, L. (1995). [Local Indicators of Spatial Association—LISA](https://doi.org/10.1111/j.1538-4632.1995.tb00338.x). *Geographical Analysis*, 27, 93–115. Read the local-to-global argument alongside the stated normalisation.
- **Multiplicity:** Benjamini, Y. and Hochberg, Y. (1995). [Controlling the False Discovery Rate](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x). *JRSS B*, 57, 289–300. Distinguish false discovery rate from family-wise error and note the assumptions.
- **Method walkthrough:** [GeoDa: Local Spatial Autocorrelation (1)](https://geodacenter.github.io/workbook/6a_local_auto/lab6a.html), including local inference and multiple comparisons.

**Next:** [Geary's C and Local Geary](sec_06-05-Gearys-C-and-Local-C.md): compare the same values through squared neighbour differences.
