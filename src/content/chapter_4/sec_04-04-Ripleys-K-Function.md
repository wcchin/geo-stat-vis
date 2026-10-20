---
label: ripleys-k-function
---

# Ripley's K-function

## From the nearest neighbour to several spatial scales

[NNA](sec_04-03-Nearest-Neighbor-Analysis.md) summarises the closest other point to every event. That is a specific spatial scale: the first neighbour. It can miss the organisation of points beyond those short distances. [Quadrat analysis](sec_04-02-Quadrat-Count-Analysis.md) instead counts points inside cells, but its answer depends on the partition.

Ripley's K-function examines how many other points occur within distance $r$ of a typical point, relative to overall intensity. Repeating the calculation over a range of radii creates a curve rather than one nearest-neighbour summary. The function is cumulative: each radius includes all pairs within it, not just those in a narrow distance band.

After reading, you should be able to distinguish $K(r)$, $L(r)$ and $L(r)-r$; calculate a small pair-count example; explain edge correction; and interpret simulation envelopes without confusing pointwise and whole-curve inference.

## A local motivation: paired bus stops

Bus stops on opposite sides of a Singapore street can be close together even when successive stopping locations are spaced along a route. A nearest-neighbour statistic can be dominated by those close pairs. That is a meaningful result about stop locations, but it is not a complete description of their organisation.

```{figure} ../resources/w05-img/Bus_Stop_nearest_neighbor.png
:label: k-singapore-bus-stop-motivation
:alt: Existing course illustration of nearby bus stops, motivating a distinction between opposite-side pairs and spacing along routes.
:align: center

The existing urban illustration motivates a question about scale. Closely paired stops and wider spacing between stopping locations can coexist. No new statistic is inferred from this image.
```

```{figure} ../resources/original/k-paired-sites.svg
:label: k-synthetic-paired-sites
:alt: Synthetic pairs at regularly spaced sites, with several search circles and a translation-corrected L minus r curve.
:align: center

An original, explicitly synthetic construction inspired by paired stops: 16 sites on a regular lattice, each containing a pair 30 m apart. The 32 coordinates lie in a fixed 2 km square. Circles show cumulative search radii from one point. These are not observed bus-stop coordinates, and the curve is descriptive rather than a significance test.
```

The plane-wide homogeneous model is only a starting reference for a road-related pattern. Stops are constrained by roads and service design. A network-based null may be more appropriate for substantive transport analysis. Rejection of planar CSR need not indicate stop-to-stop attraction.

## What K measures

For a stationary point process with intensity $\lambda$, the definition is

$$
\lambda K(r)=\mathbb{E}\!\left[\text{number of other points within }r
\text{ of a typical point}\right].
$$

The focal point is excluded. $K(r)$ is not itself a raw neighbour count: multiplication by intensity gives the expected count. Its units in a two-dimensional metric analysis are area, such as m². Under a homogeneous Poisson process,

$$
K_{\mathrm{CSR}}(r)=\pi r^2.
$$

With constant intensity, twice the disk area means twice the expected number of neighbours. This reference follows from independence and uniform intensity, not from the observed pattern having equal distances between points. See [spatstat's K-function definition](https://search.r-project.org/CRAN/refmans/spatstat.explore/html/Kest.html).

## From point pairs to an estimator

Let $n$ be the number of observed points, $A$ the fixed window area and $d_{ij}$ the distance between different points $i$ and $j$. An elementary estimator without edge correction is

$$
\widehat K_0(r)=\frac{A}{n(n-1)}
\sum_{i=1}^{n}\sum_{\substack{j=1\\j\ne i}}^{n}
\mathbf{1}(d_{ij}\leq r).
$$

The indicator is essential: only pairs within the radius contribute. The denominator matches an **ordered-pair** sum: $i$ to $j$ and $j$ to $i$ each count. If software supplies unordered pairs, multiply their count by two before using this denominator. Self-pairs never enter the sum.

### A small counting example

Suppose four points lie in a 100 m by 100 m window. At radius 10 m, exactly two distinct unordered pairs are within range. There are four ordered contributions, so

$$
\widehat K_0(10)=\frac{10{,}000}{4(4-1)}\times4
=3333.33\ \mathrm{m}^2.
$$

This is an illustrative arithmetic example, not an edge-corrected estimate for real observations. As the radius increases, qualifying pairs are retained and additional pairs enter. A pair cannot disappear from the cumulative count at a larger radius.

## Boundaries affect neighbour counts

A disk around a point near the window boundary extends outside the observed region. Possible neighbours in that unobserved part cannot be counted. The elementary estimator therefore tends to underestimate the plane-wide K-function. The effect is generally more important as the radius becomes large relative to the window.

An edge correction adjusts the contributions of observable pairs. Different methods use different information: a border correction restricts eligible focal points, an isotropic correction uses visible circumferences, and a translation correction uses overlap between shifted windows. Report the method rather than simply stating “edge corrected”.

For the rectangular synthetic examples, the original code uses translation correction. If a displacement between two points is $h=(h_x,h_y)$ and the rectangle has width $a$ and height $b$, its overlap area is

$$
|W\cap(W+h)|=(a-|h_x|)(b-|h_y|).
$$

Writing $x_i$ for the coordinate vector of point $i$, for positive overlap the corresponding estimator is

$$
\widehat K_{\mathrm{trans}}(r)=
\frac{A^2}{n(n-1)}
\sum_{i=1}^{n}\sum_{\substack{j=1\\j\ne i}}^{n}
\frac{\mathbf{1}(d_{ij}\leq r)}{|W\cap(W+(x_j-x_i))|}.
$$

Pairs with a smaller overlap receive greater weight. Near-zero overlap can create unstable contributions, another reason to restrict the distance range. The formula above is for a rectangle; do not substitute a rectangular area for an irregular window with holes or a coastline. Correction reduces boundary bias under its assumptions; it does not reconstruct outside points or repair an unsuitable window.

## K, L and the centred L curve

A square-root transformation puts the curve back into distance units:

$$
\widehat L(r)=\sqrt{\frac{\widehat K(r)}{\pi}},
\qquad \widehat H(r)=\widehat L(r)-r.
$$

| Display | Theoretical CSR reference | Descriptive reading |
| --- | --- | --- |
| $\widehat K(r)$ | $\pi r^2$ | Compare with an area-valued curve |
| $\widehat L(r)$ | $r$ | Compare with a diagonal in distance units |
| $\widehat L(r)-r$ | $0$ | Compare with a horizontal reference |

Values above the reference suggest excess cumulative close pairs; values below suggest fewer. With a finite pattern, an estimated curve will vary around its reference. A small visual departure is not automatically significant. Always label the vertical axis: a curve labelled simply “K” should not actually show $L-r$.

The paired-site example can show excess close pairs at short radii and relatively sparse intermediate neighbourhoods between sites. Because K is cumulative, this does not identify a narrow interaction distance or establish that a curve crossing marks the exact size of a cluster. Annular summaries such as a pair-correlation function ask a different, noncumulative question.

## Compare like with like under simulation

Choose the null model, radius interval, radius grid, correction and inferential question before interpreting the curve. For the examples below, generate independent uniform points in the same fixed square and condition on the same count of 96. Calculate the same translation-corrected curve for each simulated pattern.

```{figure} ../resources/original/k-three-patterns-envelope.svg
:label: k-synthetic-pointwise-envelopes
:alt: Centred L curves for three synthetic patterns compared with pointwise quantiles from 999 CSR simulations in the same square window.
:align: center

Original comparison of the same synthetic patterns used on the quadrat page. The shaded bands are pointwise 2.5th–97.5th percentile bands from 999 conditional CSR simulations. All panels use translation correction, the same radius grid and the same vertical scale. These are simulation reference bands, not confidence intervals for the underlying process's true K-function.
```

### A pointwise envelope is not a global test

At one radius fixed in advance, a pointwise comparison asks whether the observed summary is unusually high or low at that radius. Looking across many radii creates many opportunities to cross a pointwise band. A crossing somewhere does not constitute a 5% test for the entire curve. The values at nearby radii are also strongly related because pairs accumulate.

For a whole-curve decision over a prespecified interval, use a calibrated global envelope or a single prespecified deviation statistic. For example, an upper-deviation statistic might summarise the maximum scaled departure over that interval. Its reference must be calibrated using the same simulation procedure; choosing a maximum after seeing the plot and reading a pointwise p-value does not do this. [Myllymäki et al. (2017)](https://doi.org/10.1111/rssb.12172) develop global envelope tests that address whole-curve inference.

Ten simulated curves can help visualise variation, but they are a weak basis for a precise envelope or small Monte Carlo p-value. State the number of simulations, seed and whether the comparison is pointwise or global. Do not call an arbitrary band a “95% confidence envelope”.

### Theory and a finite-window reference are related, not identical

The theoretical $\pi r^2$ reference describes the homogeneous Poisson process. A simulation envelope describes the chosen estimator applied to patterns in the specified observation window. If you use an uncorrected estimator on both observed and simulated points, the simulation can still compare those summaries consistently, but the curves retain boundary bias relative to the theoretical K-function. Name that estimator and do not interpret its raw departure from $\pi r^2$ as though it were corrected.

## What if NNA and K give different impressions?

NNA gives each point one closest-neighbour distance. K accumulates all pairs up to each radius. Close pairs embedded in a spaced layout can therefore produce a short nearest-neighbour mean and a more complicated K curve. The appropriate conclusion specifies the scale and reference, rather than assigning one permanent label to the entire pattern.

| Finding | What to investigate next |
| --- | --- |
| Short NNA distance; excess short-range pairs | Repeated coordinates, paired objects, observation units and genuine local grouping |
| Different departures across radii | Cumulative effects, background intensity, boundaries and the prespecified distance range |
| No strong departure in either summary | Whether the tests miss other aspects of the pattern; do not claim proven randomness |
| Rejection under homogeneous CSR | Whether uneven opportunity or a network constraint explains the contrast |

Under changing background intensity, the ordinary stationary K-function may reflect broad density differences as well as interaction. An inhomogeneous K analysis requires an explicit intensity model and its own assumptions. It is not achieved merely by drawing a different basemap or changing the colour scale.

## Check your reasoning

```{dropdown} 1. Why exclude the focal point?
A self-pair has distance zero and would add a contribution at every radius. The function concerns other points, so self-pairs are excluded.
```

```{dropdown} 2. Does K at 500 m count only pairs between 400 and 500 m?
No. It includes all qualifying pairs at distances up to 500 m. It is cumulative, so many short-distance pairs continue to influence the larger-radius summary.
```

```{dropdown} 3. A curve crosses a pointwise 95% band once. Has a global 5% test rejected CSR?
No. A whole-curve claim needs calibration for the entire prespecified radius interval, not an unadjusted pointwise band inspected at many distances.
```

```{dropdown} 4. Can the same planar CSR model be used uncritically for bus stops and lightning?
No. Bus stops are constrained by a road network and service design; lightning has a different observation process and potential window. The method can be shared while the defensible null models differ.
```

## Try it and read further

The [point-pattern lab](../notebooks/lab-05-point-pattern.ipynb) contains the existing K/L workflow. Check the estimator and edge-correction support in the installed package before comparing software output with a theoretical curve. The [original figure source](https://github.com/wcchin/geo-stat-vis/blob/main/scripts/point_pattern_examples.py) implements the stated rectangular translation correction explicitly and records the simulated reference.

- **Foundational reading:** Ripley, B. D. (1977). [Modelling Spatial Patterns](https://doi.org/10.1111/j.2517-6161.1977.tb01615.x). *Journal of the Royal Statistical Society: Series B*, 39, 172–192. Read for the connection between pattern summaries and models.
- **Inference:** Myllymäki, M., Mrkvička, T., Grabarnik, P., Seijo, H. and Hahn, U. (2017). [Global envelope tests for spatial processes](https://doi.org/10.1111/rssb.12172). *Journal of the Royal Statistical Society: Series B*, 79, 381–404. An [open manuscript](https://arxiv.org/abs/1307.0239) is available.
- **Implementation:** [spatstat: Kest](https://search.r-project.org/CRAN/refmans/spatstat.explore/html/Kest.html) explains the estimator, theoretical reference and edge corrections.
