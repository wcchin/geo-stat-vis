# 5.2 Spatial kernel density estimation

**Reading route.** First distinguish density, intensity and smoothed price, then inspect bandwidth and the all-sales reference. Continue to dual KDE for a comparison of distributions. Its ratio-to-share derivation is an optional second reading; keep the denominator-support rules with any interpretation of the ratio maps.

A point map shows observed positions. When many observations overlap, it becomes difficult to see the broad geographical pattern. Spatial KDE places a two-dimensional kernel over each position and sums the contributions at a grid of evaluation locations. The resulting surface describes how the observed point mass is distributed under a chosen amount of smoothing.

For a common isotropic bandwidth $h$ in two dimensions,

$$\widehat{f}_h(\mathbf{s})=\frac{1}{nh^2}\sum_{i=1}^{n}K\left(\frac{\mathbf{s}-\mathbf{s}_i}{h}\right).$$

Here $\mathbf{s}_i$ is an observed position and $\mathbf{s}$ is an evaluation position. An isotropic kernel treats directions equally, so its contribution depends on distance rather than direction. With coordinates in metres, the probability density has units of inverse square metres. Multiplication by one million expresses it per square kilometre.

## Choose the quantity before choosing the colours

Three surfaces can look similar while answering different questions.

| Surface | Interpretation | Important denominator |
|---|---|---|
| Probability density | Where is a randomly selected transaction from this group likely to occur? | Number of transactions in that group |
| Event intensity | How many transactions are smoothed into a unit area during the observation period? | Area, with a fixed period |
| Smoothed price | What average price is associated with nearby observed sales? | Local weighted sales, rather than just area |

For an uncorrected fixed-bandwidth estimate, multiplying probability density by the group's count gives a smoothed event intensity:

$$\widehat{\lambda}_h(\mathbf{s})=n\widehat{f}_h(\mathbf{s}).$$

Our first spatial comparison uses this intensity form, with a common Gaussian bandwidth of 700 m and a shared colour scale. Every transaction has unit weight, including transactions sharing a block position. The values describe registrations over the six-month window, not annual rates.

```{figure} ../datasets/hdb_resale_2026/figures/spatial_kde.png
:label: ch5-spatial-kde
:alt: All-sales and quartile intensity surfaces
:align: center

Uncorrected Gaussian intensity estimates evaluated on a 300 m grid. The same bandwidth, units and colour range apply to all three panels. The surface is displayed within the planning-area union; this display mask is not an edge correction.
```

A high value in the upper-group panel means a concentration of upper-group sales. It does not mean that the average local sale price equals a high value: price is not being averaged in this calculation. Likewise, summing price-weighted kernels would represent a smoothed concentration of transaction value, not an average price.

If the aim were to estimate a local average price, one possible descriptive smoother would divide the kernel-weighted sum of prices by the kernel-weighted sum of sales. Such an estimate needs care wherever the denominator is small and would answer a different question from {numref}`ch5-spatial-kde`.

## Bandwidth sets the geographical scale

```{figure} ../datasets/hdb_resale_2026/figures/bandwidth.png
:label: ch5-bandwidth
:alt: Spatial bandwidth comparison
:align: center

Upper-group probability density with Gaussian bandwidths of 350 m, 700 m and 1,400 m. The panels share a colour scale. These values are standard deviations of Gaussian kernels, not finite search radii.
```

A smaller bandwidth reveals estate-scale concentrations and gaps. A larger bandwidth can connect several concentrations into one broad feature. A Gaussian kernel has no finite cutoff, so distant observations still contribute, although increasingly weakly. Software that uses a compact kernel or a search radius can therefore interpret a numerical bandwidth differently. State the implementation as well as the distance.

The grid spacing controls how finely the estimated surface is sampled for display. It is not the bandwidth. Reducing a 300 m grid to 100 m produces more pixels; it does not create more precise source locations or reduce the smoothing scale.

## Coastlines, opportunities and interpretation

The kernels in these figures extend over the whole plane before the display is masked. Some mass falls into the sea or into places with no HDB stock. Simply hiding those cells does not redistribute the lost mass. The surface visible over land therefore need not integrate to the full count or to one. A boundary-corrected or opportunity-adjusted estimate would require an explicitly defined window and a justified correction.

Planning-area outlines provide a detailed geographical reference, but they do not define where a sale could have occurred. Housing stock, eligible flats and the locations of observed sales offer different possible reference populations. A dark upper-group patch may reflect plentiful housing, high turnover, a larger upper-price share, or several of these together.


## Dual KDE: compare one distribution with another

Separate surfaces show where each group concentrates. **Dual KDE** relates two smoothed surfaces through an explicitly chosen operation, such as subtraction or division. It is a family of comparisons, rather than a synonym for one particular ratio. The comparison helps us move from “Where are there many expensive sales?” to “Where are expensive sales relatively more common, given the geography of selling locations?”

For the HDB example, let $\widehat f_H$, $\widehat f_L$ and $\widehat f_A$ denote separately normalised probability densities for the high-price group, low-price group and all transactions. Each density integrates to one over the full plane before display masking. We use the same Gaussian kernel, 700 m bandwidth and 300 m grid for all three.

| Comparison | Ratio | Meaning of a value above 1 |
|---|---|---|
| High versus all | High-group density divided by all-sales density | High-price sales are overrepresented relative to their overall share |
| Low versus all | Low-group density divided by all-sales density | Low-price sales are overrepresented relative to their overall share |
| High versus low | High-group density divided by low-group density | Greater concentration of the high-group distribution than the low-group distribution |

For example,

$$R_H(\mathbf{s})=\frac{\widehat f_H(\mathbf{s})}{\widehat f_A(\mathbf{s})}.$$

The neutral value is one. A ratio of two means that the high-group probability density is twice the all-sales probability density at that location. It does **not** mean that twice as many high-price transactions as total transactions occur there.

::::{dropdown} Go deeper: the ratio-to-share calculation

### A relative-representation ratio and a local share

The distinction follows from normalisation. Let $p_H=n_H/n_A$ be the high-group proportion across the complete sample. Using the same kernels, its smoothed local share is

$$\widehat p_H(\mathbf{s})=\frac{\widehat\lambda_H(\mathbf{s})}{\widehat\lambda_A(\mathbf{s})}=p_H R_H(\mathbf{s}).$$

Here $p_H$ is about 0.252. A relative-representation ratio of two therefore corresponds to a smoothed local share of about 0.503, or 50.3%. The ratio compares that local share with its overall baseline. Dividing the **count-intensity** surfaces directly gives the share; dividing the **separately normalised probability-density** surfaces gives the baseline-relative ratio. State which calculation the map shows.

High and low are not complementary categories: middle-price transactions remain in the all-sales denominator. For high versus low, a ratio of one means equal normalised densities. Equal local count intensities would instead require allowing for the groups' different total counts.

::::

```{figure} ../datasets/hdb_resale_2026/figures/dual_kde.png
:label: ch5-dual-kde
:alt: Dual KDE ratios for the price groups
:align: center

Ratios of separately normalised Gaussian KDEs, displayed on a log₂-spaced scale. Orange indicates a ratio above one and purple below one; the first named group determines the direction of the comparison. Ratios of one-half and two are equally far from the neutral value. Colours saturate outside one-quarter to four. This diverging palette represents departures around a reference value; the earlier observed-count and density maps retain sequential OrRd colours.
```

### Avoid ratios supported by almost no data

A Gaussian kernel has positive tails far from the observations. A ratio can therefore be calculated where both densities are extremely small, producing an apparently striking contrast with little local support. We retain high/all and low/all cells only where all-sales intensity is at least 5 transactions per km² over the six months. High/low additionally requires each group's intensity to be at least 1 transaction per km². Other land cells retain the muted basemap and are **not** neutral ratios or zeros.

These thresholds are transparent exploratory choices, not confidence limits. Their sensitivity should be checked before making a substantive claim. No pseudocount is added to the denominator. The comparisons inherit the location uncertainty and bandwidth dependence of the component estimates, and do not remove differences in housing stock, turnover, size or remaining lease. They are descriptive relative patterns, not tests of significant clustering or probabilities for all flats.

### Reading connection: the food-retailing study

[Jansenberger and Staufer-Steinnocher (2004)](https://research.wu.ac.at/en/publications/dual-kernel-density-estimation-as-a-method-for-describing-spatio--4/) examined Upper Austrian food retailing in 1998 and 2001. Their comparison grouped Rewe and Spar against other retailers and used differences between density surfaces to describe changing outlet concentration and dominance. Thus the comparison concerned retail groups, rather than two individual hypermarket stores. We retain it as a methodological reading while using Singapore HDB data for the worked maps.

Their subtraction and our normalised ratios answer different questions: a difference retains the component surfaces' units, while a ratio is dimensionless and emphasises relative representation. Reading task: explain why a large absolute density difference need not imply a large density ratio, and why either result depends on the underlying reference distribution.

**Interpretation task:** Compare a dark patch in the upper-group surface with the all-sales surface. What additional evidence would distinguish a concentration of sales from an unusually high local share of expensive sales?

**Self-check:** Does a ratio of two mean twice as many high-price as all sales?

```{dropdown} Feedback
No. With separately normalised densities it means the local high-price share is twice its overall share. At an overall share near 0.252, this corresponds to a local smoothed share near 0.503.
```
