---
label: getis-ord-g
---

# Getis–Ord G Statistics

## A different question about local concentration

A high-value cell can be surrounded by low-valued neighbours, or lie within a broader high-value neighbourhood. Local Moran distinguishes the focal-versus-neighbour contrast. Getis–Ord statistics instead ask whether relatively large or small values concentrate within the selected neighbourhood.

This section separates **General G**, **local Gi** and **local Gi***. After reading, you should be able to explain self-inclusion, distinguish a raw ratio from a standardised score, interpret conditional permutation results, and choose among the chapter's summaries. The star is part of the statistic's definition, not a marker of significance.

## General G is a global statistic

For nonnegative values, zero self-weights and binary adjacency $a_{ij}$, use

$$
G=\frac{\displaystyle\sum_i\sum_{j\ne i}a_{ij}x_ix_j}
{\displaystyle\sum_i\sum_{j\ne i}x_ix_j}.
$$

The denominator is $(\sum_i x_i)^2-\sum_i x_i^2$. It must be positive. The numerator counts products for selected ordered relationships; the denominator includes every ordered pair of distinct observations. Under unrestricted permutation of the values,

$$
\mathbb{E}[G]=\frac{\sum_i\sum_{j\ne i}a_{ij}}{n(n-1)}.
$$

Large positive products arise when large values are connected. A larger-than-reference G supports concentration of high values; a low-tail departure concerns an unusually low selected-pair product sum. G is not a symmetric measure treating low–low and high–high similarity identically, as Moran's mean-centred products do. A global tail does not locate a particular hotspot or coldspot.

The binary union-4NN graph is the same graph used for Moran and Geary, but those two statistics use row-standardised weights in our main analysis. This numerical weighting difference is deliberate and documented; do not attribute every difference in output solely to the statistic's name.

Nonnegative income estimates are suitable for this raw-ratio example. Arbitrarily adding a constant changes the products and the statistic. Unlike Moran's I and Geary's C, G is not invariant to a shift of origin. Do not mean-centre values before inserting them into this raw-ratio formula.

## Local Gi excludes the focal unit

A local ratio is

$$
G_i=\frac{\sum_{j\ne i}a_{ij}x_j}{\sum_{j\ne i}x_j}.
$$

The numerator summarises selected neighbours, excluding the focal unit. The denominator contains all other observations, not just the neighbours. The focal value therefore does not enter either sum. A positive denominator is required.

For a synthetic five-unit dataset $[2,4,6,8,10]$, suppose the focal value is 6 and its neighbours have values 4 and 8. Binary local Gi is $(4+8)/(2+4+8+10)=12/24=0.5$. The fraction depends on the selected neighbourhood; a large raw ratio is not automatically significant.

## Local Gi* includes the focal unit

Let $a^*_{ij}=a_{ij}$ for other units and set $a^*_{ii}=1$. Then

$$
G_i^*=\frac{\sum_j a^*_{ij}x_j}{\sum_jx_j}.
$$

For the same example, Gi* is $(4+6+8)/30=0.6$. Here self-inclusion means adding both the focal observation to the selected sum and its value to the total denominator. Different diagonal or weight-transformation conventions must be stated explicitly.

Gi* can highlight a high-sum neighbourhood containing a locally low focal value, while Local Moran may describe that focal value as an LH contrast. A significant high Gi* score concerns the **neighbourhood concentration**, not necessarily an individually high focal observation. Gi and Gi* do not provide Moran's four focal/lag categories.

## Raw ratios, analytical scores and conditional scores

A raw Gi* ratio has no universal zero reference for hot versus cold. Compare it with the distribution implied by the chosen null. One widely used analytical standardisation, with fixed weights $a^*_{ij}$ and unrestricted random assignment, is

$$
Z_i^*=\frac{\sum_j a^*_{ij}x_j-\bar{x}\sum_j a^*_{ij}}
{s\sqrt{\dfrac{n\sum_j(a^*_{ij})^2-(\sum_j a^*_{ij})^2}{n-1}}},
\qquad s^2=\frac{1}{n}\sum_j(x_j-\bar{x})^2.
$$

A zero denominator is undefined. Normal-approximation inference adds assumptions beyond calculating this score. A z-score is not the raw ratio and is not automatically a calibrated small-sample probability.

Our maps instead use the **fixed-focal-value conditional permutation** design introduced in Section 6.4. Keep $x_i$ fixed, draw the other neighbour values without replacement and add the fixed self term. For binary weights with $k_i$ other neighbours,

$$
\mathbb{E}[G_i^*\mid x_i]
=\frac{x_i+k_i\bar{x}_{-i}}{\sum_jx_j},
\qquad \bar{x}_{-i}=\frac{\sum_{j\ne i}x_j}{n-1}.
$$

This differs from the unrestricted expectation implicit in the analytical score. The downloadable `Gstar_z_perm` is an observed departure divided by the conditional simulations' standard deviation, **not the analytical $Z_i^*$ above**. P-values are calculated from ranked simulation tails, not a normal approximation to that conditional score.

Our two-sided procedure uses inclusive lower and upper tail counts, the plus-one adjustment and twice the smaller tail, as in Section 6.4. A selected observation above its conditional mean is labelled **Hot** and one below it **Cold**. These are statistical labels for relative income concentration, not literal temperature or official income-group categories.

### When two methods give the same local p-values

With binary equal-weight neighbours and a fixed focal value, Gi and Gi* are affine functions of the same neighbour sum, so their conditional rank comparisons agree when denominators are positive. For nonzero focal deviation, Local Moran is also an affine function of that sum, possibly reversing its direction. Consequently, our doubled-tail Local Moran and Gi* p-values coincide when using the same random draws. This is a consequence of the stated design, not independent confirmation by two tests. Their descriptive labels and interpretation can still differ. Other inference or weighting conventions need not produce this equivalence.

## Results on the shared Malaysian income data

For the same **92 median household incomes**, binary union-4NN General G = **0.05930**, with unrestricted upper-tail permutation p = **0.0001**. Its null expectation is $452/(92\times91)\approx0.05399$, so the observed value is interpreted relative to that reference, not zero.

```{figure} ../resources/original/malaysia-income-local-gstar.png
:label: malaysia-income-local-gstar
:alt: Conditional Gi-star high and low income concentration classifications across Peninsular Malaysia before and after BH adjustment.
:align: center

Binary union-4NN neighbours plus self weight one. Compare unadjusted two-sided p ≤ 0.05 with BH q ≤ 0.05 across 92 tests. Orange denotes high-sum departures and purple low-sum departures; grey is not selected. The figure uses conditional permutations, not analytical normal scores. Income: DOSM; boundaries: PLANMalaysia.
```

Twenty-five unadjusted candidates comprise ten high-sum and fifteen low-sum neighbourhoods. **Fourteen survive BH adjustment: seven high and seven low**; nine meet Bonferroni correction. Their inferential overlap with Local Moran follows the conditional rank equivalence explained above, not independent confirmation.

Bentong makes the interpretive difference concrete. Its median is below the overall mean, but its selected neighbours have a high average. It is an unadjusted LH candidate under Local Moran and an unadjusted high-sum candidate under conditional Gi*. Neither finding survives BH adjustment. A low focal value can therefore appear in a high-concentration neighbourhood without contradiction.

The union-6NN graph gives General G = 0.08568 and upper-tail p = 0.0002. Its additional links increase the raw statistic and its expected reference value. The larger raw number is not evidence that six neighbours reveal stronger concentration.

## Choose a statistic from the question

| Question | Useful starting summary | Interpretation to avoid |
| --- | --- | --- |
| Do neighbouring deviations tend to agree overall? | Global Moran's I | Treating a global result as a map of significant hotspots |
| Are neighbouring values unusually similar in squared-difference terms? | Global/local Geary | Assuming small differences imply a particular HH/LL label |
| Where does a focal value agree or contrast with its neighbours? | Local Moran | Calling every scatterplot quadrant significant |
| Do high values concentrate among selected pairs overall? | General G | Inferring locations directly from one global coefficient |
| Where are unusually high or low neighbourhood sums? | Gi or Gi* | Assuming the focal observation itself must be high or low |

Methods complement geographical reasoning; they do not select a causal explanation. Keep the support, variable and graph explicit, distinguish transformations and self-weights, and report the inferential family. Comparing many methods and retaining only favourable results creates another selection problem beyond the within-map multiple testing shown here.

## Closing the chapter

The Malaysia income maps established why a histogram cannot reveal geographical arrangement. The weights section defined which relationships enter a calculation. The Moran, Geary and Getis–Ord sections then examined different attribute summaries and global/local questions.

The Malaysian income results show that a global coefficient, an unadjusted local candidate and a multiplicity-adjusted local finding are different claims. Global similarity persists under both proximity graphs, while the selected local footprint changes. Geary highlights some modest deviations with small neighbour differences; Moran and Gi* interpret the same conditional neighbour-sum comparisons differently.

Report the observation unit, variable, year, graph and evidence rule with each conclusion. The district-level patterns do not establish household-level relationships, identify causal neighbour effects or account automatically for survey uncertainty and historical boundary changes.

## Check your reasoning

```{dropdown} 1. Does the star mean statistically significant?
No. It denotes self-inclusion in the local definition. Significance requires a separate reference comparison.
```

```{dropdown} 2. Is a high raw Gi* ratio automatically a hotspot?
No. The neighbourhood size, weights, value distribution and reference determine its expected magnitude and unusualness.
```

```{dropdown} 3. Can a low focal value lie inside a high-sum neighbourhood?
Yes. Gi* concerns the sum including neighbours. Local Moran can identify the focal-versus-neighbour contrast separately.
```

```{dropdown} 4. Does Local Moran/Gi* agreement here provide independent confirmation?
No. Their two-sided conditional rankings coincide under this equal-neighbour-weight, fixed-focal-value design. The same data and draws drive both.
```

```{dropdown} 5. What changes when diagonal neighbours are included?
The graph, selected pair products, neighbourhood sums and corresponding null distributions. Raw coefficients from different graphs are not a common strength scale.
```

## Reproduce and read further

The [shared areal notebook](../notebooks/malaysia-income-areal-self-study.ipynb), [source record](../datasets/malaysia_income_areal/README.md) and explicit Python implementation reproduce all figures and comparisons. The workbook's existing [local areal lab](../notebooks/lab-09-LISA.ipynb) provides the package-based course workflow; check its definitions and software defaults before expecting identical p-values or category codes.

- **Foundation:** Getis, A. and Ord, J. K. (1992). [The Analysis of Spatial Association by Use of Distance Statistics](https://doi.org/10.1111/j.1538-4632.1992.tb00261.x). *Geographical Analysis*, 24, 189–206.
- **Standardisation and inference:** Ord, J. K. and Getis, A. (1995). [Local Spatial Autocorrelation Statistics: Distributional Issues and an Application](https://doi.org/10.1111/j.1538-4632.1995.tb00912.x). *Geographical Analysis*, 27, 286–306.
- **Implementation comparison:** [GeoDa: Getis–Ord statistics](https://geodacenter.github.io/workbook/6b_local_adv/lab6b.html#getis-ord-statistics) and [esda G_Local](https://pysal.org/esda/stable/generated/esda.G_Local.html). Check self-weight, transformation and alternative conventions.
