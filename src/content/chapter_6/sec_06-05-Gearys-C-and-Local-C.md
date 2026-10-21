---
label: gearys-c-and-local-geary
---

# Geary's C and Local Geary

## Compare differences rather than mean-centred products

Moran's I combines products of deviations from the overall mean. **Geary's C** instead compares the squared difference between each observation and its neighbours. Both use attribute values and a specified spatial graph, but compress those relationships differently.

This section develops the global statistic, a clearly scaled local version and a comparison on the same Malaysian income observations. After reading, you should be able to interpret C relative to its null expectation, calculate a local squared-difference summary, and explain why Local Geary does not automatically inherit Moran's HH/LL/HL/LH labels.

For an individual pair, consider these synthetic values with overall mean 10:

| Pair | Mean-centred product | Squared difference |
| --- | ---: | ---: |
| 2 and 2 | $(-8)(-8)=64$ | 0 |
| 9 and 11 | $(-1)(1)=-1$ | 4 |
| 2 and 18 | $(-8)(8)=-64$ | 256 |

The first pair is low–low similarity. The second straddles the mean but has a small difference. The third straddles the same mean with a much larger contrast. Geary's pair contribution depends on separation in **attribute space**, not which side of the overall mean each value occupies. Geographical space determines which pairs receive a weight.

## Global Geary's C

With $n$ observations, zero self-weights, $S_0=\sum_i\sum_jw_{ij}$ and $Q=\sum_i(x_i-\bar{x})^2$,

$$
C=\frac{n-1}{2S_0}
\frac{\displaystyle\sum_i\sum_jw_{ij}(x_i-x_j)^2}{Q}.
$$

The numerator accumulates squared neighbour differences; the denominator scales by the variation in the whole dataset. Nonnegative weights give nonnegative C. A constant variable has $Q=0$ and cannot be analysed with this formula. Both ordered directions enter the sum wherever the corresponding weights are nonzero.

Under unrestricted random reassignment of a nonconstant set of values with zero diagonal weights, $\mathbb{E}[C]=1$. Relative to that reference, smaller values indicate neighbour similarity and larger values indicate contrast. Merely being below or above one does not establish significance; a reference distribution is still needed. Avoid treating 0–2 as a universal attainable range for every weighting configuration.

For the synthetic chain $[2,2,8,8]$ with row-standardised neighbours, the ordered weighted sum of squared differences is 36. Here $n=4$, $S_0=4$ and $Q=36$, giving

$$
C=\frac{3}{8}\frac{36}{36}=0.375.
$$

The alternating assignment $[2,8,2,8]$ gives C = 1.5. As with Moran's example, these are transparent calculations, not evidence about a regional dataset.

C is invariant to adding a constant or multiplying every value by the same nonzero constant. Squared pair differences and overall squared deviations change together. The unnormalised numerator alone does not have that property.

## A local squared-difference statistic

Use population-standardised values $z_i=(x_i-\bar{x})/\sqrt{Q/n}$. Our local convention is

$$
c_i=\sum_jw_{ij}(z_i-z_j)^2.
$$

With row-standardised weights, this is the weighted mean squared standardised difference from neighbours. It is dimensionless and nonnegative. Other sources use different factors or unstandardised differences; comparing raw numbers requires matching definitions.

Under this convention,

$$
C=\frac{n-1}{2nS_0}\sum_i c_i.
$$

The source verifies this identity. The average local value is not simply global C, unlike the Local Moran convention under nonempty row-standardised weights.

For the grouped four-cell chain, $\mathbf{z}=[-1,-1,1,1]$ and $\mathbf{c}=[0,2,2,0]$. The end cells match their only neighbour. Each interior cell has one matching and one contrasting neighbour, so its local average is $(0+4)/2=2$. Substituting their sum of four into the identity recovers C = 0.375.

### A small local value needs a reference

A small $c_i$ means small observed differences, but its unusualness depends on the focal value, available values and neighbourhood. A central value in a narrow distribution can have small differences with many randomly selected neighbours. An extreme value may have a much higher expected difference under the conditional reference.

We therefore compare the observed $c_i$ with simulations holding the focal value fixed and drawing distinct neighbour values from the remaining observations. Use the same 9,999 draws, seed and doubled inclusive two-tail procedure defined in [Section 6.4](sec_06-04-Local-Moran.md). Low-tail departures indicate unusually small differences; high-tail departures indicate unusually large differences. The local null expectation is not universally one.

## Classification should match the statistic

The empirical maps use two explicit categories after significance filtering:

- **Similar:** observed $c_i$ is below its conditional simulation mean.
- **Dissimilar:** observed $c_i$ is above that mean.

The selected tail and p-value remain in the downloadable results. These labels describe a departure relative to a local reference; a “dissimilar” label does not mean the statistic itself is negative.

A more elaborate implementation may subdivide local similarity into high–high, low–low and other positive association, or use different label codes. Those classifications require additional information and rules. Our map does not claim to reproduce a package's categorical output. In particular, Local Geary alone cannot distinguish a high value among low neighbours from a low value among high neighbours using the sign of $c_i$: all its terms are squared.

## Results for the shared Malaysian income data

Use the same **92 income estimates and union-4NN graph** as in Sections 6.3–6.4. Global C = **0.3176**, with lower-tail permutation p = **0.0001** from 9,999 unrestricted shuffles. This supports neighbour similarity under the stated reference, not direct influence between household incomes. The p-value is the simulation resolution limit.

```{figure} ../resources/original/malaysia-income-local-geary.png
:label: malaysia-income-local-geary
:alt: Local Geary conditional similarity and dissimilarity classifications on the Peninsular Malaysian income map, before and after BH adjustment.
:align: center

Same income observations and primary graph. Gold denotes selected low-difference departures; purple denotes selected high-difference departures. Grey is not selected. Categories follow the stated equations rather than software-specific numeric labels. Income: DOSM; boundaries: PLANMalaysia.
```

Forty areas meet the unadjusted two-sided 0.05 threshold: 38 similar and two dissimilar. **Twenty-four remain under BH q ≤ 0.05**, all in the similarity category; seven meet Bonferroni correction. The adjusted map is therefore different from Local Moran's, even though the data and graph are unchanged.

Perlis illustrates the distinction: its median RM 4,713 is fairly close to the overall mean. Local Geary selects it as unusually similar to its selected neighbours (BH q ≈ 0.0288), while Local Moran does not (q ≈ 0.9211). Conversely, Kota Bharu is BH-selected LL under Moran (q ≈ 0.0226) but not selected by Local Geary (q ≈ 0.3137). A neighbour mean and the separate squared differences retain different information. These are not disagreements about which data are correct.

The six-neighbour sensitivity graph gives global C = 0.3365 and lower-tail p = 0.0001, with 38 BH-selected local Geary observations. Global similarity persists, but local classification remains dependent on the neighbourhood definition.

## Compare Geary and Moran carefully

| Aspect | Moran | Geary |
| --- | --- | --- |
| Pair contribution | Product of deviations from the global mean | Squared difference between values |
| Similarity reference | Global I has randomisation expectation $-1/(n-1)$ | Global C has randomisation expectation 1 |
| Local interpretation | Quadrants distinguish HH, LL, HL and LH | Small/large differences relative to a local reference; extra rules needed for finer labels |
| Scale | Determined by support and weights | Also determined by support and weights |

Geary is often described as sensitive to neighbour differences, but this is not a rule that Geary measures a local scale and Moran measures a global scale. Both global statistics use the chosen weights, and both have local counterparts. The data distribution, graph and alternative determine sensitivity. Squared differences do not automatically correct spatial trends, nonstationarity, unequal exposure or measurement error.

## Check your reasoning

```{dropdown} 1. Can two values on opposite sides of the mean still have a small Geary difference?
Yes. Values 9 and 11 around a mean of 10 differ by only two. The squared difference is four, regardless of their opposite deviation signs.
```

```{dropdown} 2. Does local c below one establish positive local association?
No. One is the expectation for the specified global C under unrestricted permutation, not a universal local threshold. Use the local conditional reference.
```

```{dropdown} 3. Can local Geary be negative with the weights used here?
No. It sums nonnegative weighted squares. A high-tail departure can suggest dissimilarity without the statistic being negative.
```

```{dropdown} 4. Does agreement between the global Moran and Geary tests prove a mechanism?
No. They are related summaries of the same observations and graph. Neither identifies direct neighbour influence or removes observation and survey limitations.
```

## Reproduce and read further

Use the [shared areal notebook](../notebooks/malaysia-income-areal-self-study.ipynb) and [analysis record](../datasets/malaysia_income_areal/README.md) to inspect every cell's statistic, tails and adjustment.

- **Foundation:** Geary, R. C. (1954). [The Contiguity Ratio and Statistical Mapping](https://doi.org/10.2307/2986645). *The Statistician*, 5, 115–141. Read the ratio of neighbour differences to overall variation.
- **Local framework:** Anselin, L. (1995). [Local Indicators of Spatial Association—LISA](https://doi.org/10.1111/j.1538-4632.1995.tb00338.x). *Geographical Analysis*, 27, 93–115.
- **Method walkthrough:** [GeoDa: Local Spatial Autocorrelation (2)](https://geodacenter.github.io/workbook/6b_local_adv/lab6b.html#local-geary) explains local difference-based interpretation and classification.

**Next:** [Getis–Ord G statistics](sec_06-06-Getis-Ord-G.md): examine local concentrations through neighbourhood sums rather than focal-versus-neighbour contrast.
