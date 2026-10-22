---
label: local-morans-i
---

# 6.4 LISA and Local Moran's I

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

## The shared Malaysian income analysis

Use the same **92 mapped areas and 2022 median gross monthly household incomes** as in Section 6.3. Every area estimate is retained and receives one observation weight. The symmetric union-4NN graph has 226 undirected links, one component, no isolates and four to nine neighbours. Interior representative points are derived from full-detail geometry in EPSG:3375; display outlines are not used to infer adjacency.

This proximity graph retains islands and avoids silently repairing the disconnected contiguity graph. It is not a claim that income travels along these links. The [source record](../datasets/malaysia_income_areal/README.md) documents geometry overlaps, joins, representative-point choices and link lengths. Published medians are treated as observations; the permutations do not propagate survey uncertainty or weight districts by household population.

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

```{figure} ../resources/original/malaysia-income-local-moran.png
:label: malaysia-income-local-moran
:alt: Local Moran income classifications across 92 Peninsular Malaysian areas before and after BH adjustment.
:align: center

Original income analysis: unadjusted two-sided p ≤ 0.05 (left) and separate 92-test BH q ≤ 0.05 (right). Orange is HH, purple LL, gold HL and teal LH where selected. Grey means not selected by the stated procedure. Income: DOSM; display boundaries: PLANMalaysia.
```

Twenty-five areas meet the unadjusted threshold: nine HH, fifteen LL and one LH. After BH adjustment, **fourteen remain: seven HH and seven LL**. Nine meet the stricter Bonferroni threshold. The adjusted HH group includes Kuala Lumpur, Putrajaya and several Selangor districts; the LL group includes seven Kelantan districts. These are relationships relative to this sample mean and graph, not official income-group categories.

Kuala Lumpur has median income RM 10,234, an HH configuration and two-sided permutation p = 0.0002 (BH q ≈ 0.0026). Bentong, with median RM 4,691, is an unadjusted LH candidate (p = 0.0240), but is not selected after BH adjustment (q ≈ 0.1162). This contrast helps separate a descriptive outlier configuration from adjusted evidence.

Neighbourhoods overlap. A selected focal area does not mean every household shares its median, nor does it assign every district to a mutually exclusive economic region.

## Why multiple testing changes the map

Testing 92 locations creates more opportunities for small p-values than a single test. Under a complete null with valid tests at level 0.05, the expected number of false rejections is at most $92\times0.05=4.6$. This expectation does not require independence, but the joint error behaviour does depend on the tests' relationships.

**Bonferroni** compares each p-value with $0.05/92\approx0.000543$ and controls family-wise error without requiring independence, assuming valid individual p-values. **Benjamini–Hochberg (BH)** sorts the p-values and compares ordered $p_{(r)}$ with $r\alpha/92$ using a step-up rule. It targets false discovery rate under suitable assumptions. Spatially overlapping tests are dependent; ordinary BH is not a universal guarantee under arbitrary dependence. We show it as an exploratory adjustment and provide the Bonferroni comparison as well.

An adjusted q-value is not the probability that its cell is a false discovery. Nor does changing a threshold identify a different physical pattern: it changes the evidence rule applied to the same estimates. Do not tune the number of permutations, seed or weights until coloured cells appear.

## Relate local results back to global association

Global I = 0.6646 with upper-tail p = 0.0001 describes pooled neighbour similarity. Fourteen BH-selected local findings provide a different, location-specific result. A global rejection does not imply significance for every district or determine the number of selected local observations.

Under the six-neighbour sensitivity graph, global I is 0.6593 and 23 local Moran observations meet the BH threshold. Thus global similarity persists while the local footprint changes. Both specifications are reported; neither is chosen because it produces more selected locations. Urbanisation, labour-market access, household composition and spatial trends remain possible explanations requiring additional evidence.

## Check your reasoning

**Self-check:** Can a positive local statistic describe low values?

```{dropdown} Feedback
Yes. A below-mean focal value with a below-mean neighbour lag is LL and gives a positive product.
```

**Self-check:** What is fixed in the local conditional reference?

```{dropdown} Feedback
The focal value, observation support and weights. The other values are reassigned. The observed neighbour values are not fixed.
```

**Self-check:** Is Bentong an adjusted spatial-outlier finding?

```{dropdown} Feedback
No. It is an unadjusted LH candidate but does not meet the reported BH threshold. State the configuration and inference rule separately.
```

**Self-check:** Do unselected districts have no spatial relationships?

```{dropdown} Feedback
No. Non-selection means insufficient evidence under that test and threshold. It does not erase observed variation or prove randomness.
```

## Reproduce and read further

The [shared areal notebook](../notebooks/malaysia-income-areal-self-study.ipynb) reproduces the observations, graph, statistics, maps and sensitivity comparison from the repository snapshot. The [source and result record](../datasets/malaysia_income_areal/README.md) defines every calculation.

- **Foundation:** Anselin, L. (1995). [Local Indicators of Spatial Association—LISA](https://doi.org/10.1111/j.1538-4632.1995.tb00338.x). *Geographical Analysis*, 27, 93–115. Read the local-to-global argument alongside the stated normalisation.
- **Multiplicity:** Benjamini, Y. and Hochberg, Y. (1995). [Controlling the False Discovery Rate](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x). *JRSS B*, 57, 289–300. Distinguish false discovery rate from family-wise error and note the assumptions.
- **Method walkthrough:** [GeoDa: Local Spatial Autocorrelation (1)](https://geodacenter.github.io/workbook/6a_local_auto/lab6a.html), including local inference and multiple comparisons.

**Next:** [Geary's C and Local Geary](sec_06-05-Gearys-C-and-Local-C.md): compare the same values through squared neighbour differences.
