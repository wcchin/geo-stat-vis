# 2.2 Frequency distribution

A table preserves individual records, but it is difficult to see a distribution by reading down a column. A frequency distribution summarises how often values or ranges occur. It helps us examine a variable's centre, spread and shape before choosing a model or comparing groups.

In our example, the variable is `TOTAL_TRIPS` and the observations are the 12 reported OD pairs in the selected temporal slice. **The count recorded for a pair and the number of pairs in a histogram bin are different quantities.** A bin containing five OD pairs does not mean five passenger trips.

## Start with the observed values

The sorted trip counts are:

**50, 256, 342, 381, 416, 500, 537, 538, 1,113, 1,385, 3,092, 4,294.**

Every value belongs to a different directed pair. Sorting reveals that most selected pairs have smaller counts and a few have much larger counts. A dot display is often useful for such a small dataset because it shows every observation. A histogram groups observations and therefore introduces a choice of bin boundaries.

```{figure} ../datasets/mrt_data_foundations_202609/figures/05_empirical_distribution.png
:label: ch2-empirical-distribution
:alt: A histogram, empirical cumulative distribution and box plot of the twelve selected OD counts, with the individual values also indicated.

Three summaries of the same 12 OD-pair counts. Histogram bins have width 500 trips; the vertical axis counts OD-pair records. The empirical CDF accumulates records, not trips. The box plot uses the stated quartile convention and 1.5-IQR whiskers.
```

For bins 0–<500, 500–<1,000 and 1,000–<1,500, the frequencies are 5, 3 and 2. The 500-trip record belongs to the second bin because our intervals include their lower boundary and exclude their upper boundary. The final histogram bin includes its upper endpoint. State such rules when a value could lie exactly on a break.

Relative frequency divides a bin count by the number of observations. The first bin therefore contains 5/12, or about 41.7%, of the selected OD-pair records. This is not the share of trips carried by those pairs: a trip-weighted share would sum their trip counts and divide by 12,904. Choosing the denominator changes the question.

## Centre and spread

The arithmetic mean is the total divided by the number of observations:

$$
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i.
$$

Here, the mean is 1,075.33 reported trips per selected OD-pair record. The median is 518.5, halfway between the sixth and seventh sorted values, 500 and 537. A median need not be an observed count. The large difference between mean and median helps describe the uneven distribution. There is no unique mode because all 12 values occur once.

The range is maximum minus minimum, or 4,244. Quartiles describe positions in the ordered data. Using linear interpolation as in the bundled calculation, the first and third quartiles are 371.25 and 1,181; the interquartile range (IQR) is 809.75. Software can use different quantile conventions, particularly noticeable in a small sample. Record the convention rather than treating a different interpolated quartile as necessarily an error.

For a sample standard deviation, we use:

$$
s=\sqrt{\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}}.
$$

The result is about 1,300.73 trips. Variance is its square and therefore has squared units. Neither a mean nor a standard deviation alone describes the distribution fully; both are sensitive to large values. The median and IQR are often useful companions when the observations are strongly uneven.

Arithmetic means are not the only possible averages. A geometric mean summarises multiplicative variation in positive quantities; a harmonic mean can be appropriate for certain averages of rates with a fixed numerator. The choice follows the quantity and weighting scheme. We use the arithmetic mean here because each selected OD-pair record receives equal weight.

## Shape without overclaiming

A right-skewed distribution has a longer tail towards larger values. Our selected counts have that descriptive pattern. Modality refers to peaks; with only 12 observations, apparent peaks in a histogram can change considerably with binning. Kurtosis concerns the standardised fourth moment and tail behaviour relative to a reference convention. It should not be reduced to the visual height or sharpness of a histogram's central peak. Some software reports excess kurtosis, subtracting 3 from the ordinary kurtosis; always check the definition.

A box plot summarises quartiles and can flag values beyond a chosen whisker rule. It does not prove those observations are mistakes. Here, 3,092 and 4,294 exceed the upper 1.5-IQR fence and are drawn separately. They remain valid reported observations in the teaching slice. A flag invites investigation; it does not supply an explanation.

## Cumulative distribution, probability mass and density

The empirical cumulative distribution function (ECDF) is:

$$
\widehat{F}(t)=\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}(x_i\leq t).
$$

It gives the fraction of observed records whose values are at most a threshold. At 538 trips, 8 of the 12 selected pairs lie at or below the threshold, so the ECDF is 2/3. Its vertical axis is a cumulative proportion between 0 and 1, not a density. Ties would produce larger jumps.

A probability mass function assigns probabilities to discrete outcomes. A probability density function describes continuous outcomes through areas under a curve; its total area is one, but its height at a point is not a probability and may exceed one. With equal-width histogram bins, a density-normalised bar has height equal to its relative frequency divided by bin width. Unequal bin widths make the distinction between height and area especially important.

A smooth kernel-density curve can summarise a numerical sample, but it is an estimate affected by bandwidth and support. For a dozen integer counts, a smooth curve may suggest more information than we have and can assign density to impossible negative counts if used carelessly. We use the observed values and ECDF rather than fit a smooth density here. Chapter 5 develops KDE in greater detail.

## Observed distributions and theoretical models

A descriptive distribution and a probability model serve different purposes. The histogram reports what we observed; a model proposes a data-generating structure under assumptions. Three common families are useful foundations:

| Model | Outcome and parameters | Important conditions |
|---|---|---|
| Normal | Continuous values; mean and standard deviation | A symmetric continuous model. Approximate normality must be justified for the quantity or model errors being analysed. |
| Poisson | Non-negative integer count; expected count in a specified exposure | A Poisson-process interpretation requires suitable independence and rate assumptions. The mean equals the variance in the basic model. |
| Binomial | Successes in a fixed number of trials; trial count and success probability | Trials are independent with the same success probability in the basic model. |

```{figure} ../datasets/mrt_data_foundations_202609/figures/06_probability_models.png
:label: ch2-probability-models
:alt: Illustrative normal density, Poisson probability masses and binomial probability masses with explicitly chosen parameters.

Conceptual model illustrations, not fits to MRT observations. The continuous normal panel shows density; the discrete panels show probability mass. Their vertical-axis meanings differ.
```

Counts do not automatically follow a Poisson distribution, and a small right-skewed sample does not establish a heavy-tailed probability law. OD records share endpoints and may be dependent; different pairs also have different demand and exposure. The central limit theorem concerns sampling distributions of sums or means under appropriate conditions, not a rule that a large raw dataset becomes normally distributed. Chapter 3 returns to the assumptions needed for statistical inference.

The [NIST exploratory-data-analysis handbook](https://www.itl.nist.gov/div898/handbook/eda/eda.htm) provides further reading on distribution summaries and probability models. The calculations and figure parameters are recorded in the [reproducibility directory](../datasets/mrt_data_foundations_202609/README.md).

**Self-check:** Does an ECDF value of 2/3 at 538 mean that two-thirds of all trips have been counted?

```{dropdown} Feedback
No. It means that two-thirds of the 12 selected OD-pair records have counts at most 538. A trip-weighted cumulative share would use trip counts as weights and answer another question.
```
