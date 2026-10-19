# Quadrat Count Analysis

## What is Quadrat Count Analysis?

Quadrat Count Analysis is a method used in spatial point pattern analysis to determine whether a pattern of points is randomly distributed, clustered, or evenly spaced. It involves _dividing the study area into smaller, equal-sized areas called "quadrats"_ (typically square or rectangular in shape) and _counting the number of points fall in each quadrat_.


## Calculating Quadrat Count

The main steps in Quadrat Count Analysis are:
1. Divide the study area into a _grid of quadrats_.
2. _Count_ the number of points in each quadrat.
3. Calculate the _expected number of points_ per quadrat under the assumption of Complete Spatial Randomness (CSR).
4. _Compare_ the observed frequency distribution (the counts) with the expected frequency distribution (under CSR) to assess the degree of similarity or difference between them.
5. Apply _statistical tests_, such as the chi-squared goodness-of-fit test, to determine whether the observed frequency distribution significantly differs from the expected distribution under CSR---whether the spatial pattern exhibits randomness, clustering, or regularity.


## Count the number of points in each quadrat

```{figure} ../resources/w05-img/plot_quadrat_counts.png
:label:
:alt:
:align: center

Counting points in cells
```

Then, how to compare?

## Chi-squared test
Use Chi-squared test, which is suitable for comparing frequencies.

The quadrat method partitions the study region into $r$ rows and $c$ columns, which define $m=r\times c$ non-overlapping subregions or quadrats of equal area. This method relies on the fact that, _under CSR, the expected number of observations within any region of equal size is the same_. Let $n$ be the number of observed points, $m$ the number of equal-area quadrats, $O_i$ the observed count in quadrat $i$, and $E_i=n/m$ its expected count under homogeneous CSR. The test statistic is calculated as

$$
\chi^2 = \sum_{i=1}^m\frac{(O_i-E_i)^2}{E_i}
$$

$$
\text{expected} = \frac{n}{m}
$$

**Why?**

> A CSR would have a mean at the average with a non-zero spread (non-zero deviation).


Use Chi-squared test, which is suitable for comparing the frequencies against an expected frequency or distribution.

**Clustered example**
- chi-squared statistic$= 354.332$, p-value$= 2.606\times10^{-66}$
- _significantly different_ from random

**Random example**
- chi-squared statistic$= 19.332$, p-value$= 0.199$
- non-significant; the distribution is _not significantly different from CSR under this test_

**Regular example**
- chi-squared statistic$= 8.332$, pvalue$= 0.910$
- non-significant; the distribution is _not significantly different from CSR under this test_

The usual upper-tail chi-squared test asks whether variation among counts is unusually large. A large p-value does not prove CSR or establish regularity. A test of unusually low variation requires a separately specified lower-tail or two-sided procedure and a suitable reference distribution.

### Why not compare means with a t-test?

Counts $[3,3,3,3,3,3]$ and $[0,0,0,6,6,6]$ both have mean 3, but differ greatly in their variation across cells. Given the point count and study window, the expected mean count is already determined. Here the question concerns the distribution of counts among quadrats, rather than a difference between means.

Very small expected counts can make the analytical chi-squared approximation unreliable. A Monte Carlo comparison should retain the same point count, fixed window and quadrat grid for every simulation. For unequal-area quadrats, expected counts must reflect their areas.



## Key considerations

Some key considerations in Quadrat Count Analysis include:
- **Quadrat size**: The size of the quadrats should be carefully chosen to ensure that it is appropriate for the scale of the pattern being studied.
- **Quadrat shape**: While square quadrats are common, other shapes (such as rectangular or circular) may be used depending on the specific study requirements.
- **Edge effects**: Care should be taken to account for edge effects, which occur when quadrats at the edge of the study area contain fewer points due to the smaller overlapping area.

> Is the analysis result sensitive to the parameter settings?

Quadrat Count Analysis provides a simple and intuitive approach to analyzing spatial point patterns, but it has some limitations compared to more advanced methods, such as **distance-based** or **density-based** approaches. Nonetheless, it is a useful tool for exploratory analysis and can be helpful in understanding the general characteristics of a spatial point pattern.
