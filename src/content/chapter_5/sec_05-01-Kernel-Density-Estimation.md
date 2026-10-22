# 5.1 Kernel density estimation

A histogram groups numerical observations into intervals. It gives a useful first view of a distribution, but its appearance depends on the width and starting positions of its bins. Kernel density estimation (KDE) offers a smooth description by placing a small curve around every observation and adding the contributions together.

For observations $x_1,\ldots,x_n$, a one-dimensional KDE is

$$\widehat{f}_h(x)=\frac{1}{nh}\sum_{i=1}^{n}K\left(\frac{x-x_i}{h}\right).$$

The **kernel** $K$ determines the shape of an observation's contribution, and the **bandwidth** $h$ determines its width. The probability density function being estimated is the combined result. It should not be confused with the kernel function used to build that result.

A common choice is the Gaussian kernel,

$$K(u)=\frac{1}{\sqrt{2\pi}}\exp(-u^2/2).$$

A transaction contributes most near its observed price and progressively less farther away. The factor $1/h$ adjusts the height as the contribution widens, while $1/n$ averages across observations. With a normalised kernel, the full estimated density integrates to one.

## Read density as an area

In this example, prices are plotted in thousands of Singapore dollars. Density therefore has units of inverse thousands of dollars. The height of the curve at S\$650,000 is not the probability that a transaction has exactly that price. An interval probability is represented by the area under the curve across that price interval.

```{figure} ../datasets/hdb_resale_2026/figures/price_kde.png
:label: ch5-price-kde
:alt: Price KDE bandwidth comparison
:align: center

Gaussian KDEs of the same 5,379 prices with bandwidths of S\$15,000, S\$40,000 and S\$100,000. The histogram is also scaled as probability density.
```

A narrow bandwidth preserves many local bumps, including features related to repeated and rounded prices. A wide bandwidth merges nearby features into a broad shape. Neither is automatically correct: the useful amount of smoothing depends on whether the aim is to inspect fine detail or communicate the broad distribution. An estimate can be too rough to reveal structure or too smooth to preserve meaningful variation.

The three bandwidths in {numref}`ch5-price-kde` are deliberately chosen for comparison. They are not an estimated optimum. A data-driven bandwidth can provide a starting point, but the analyst must still inspect what it does and consider the measurement process. A smooth curve cannot restore information that was never recorded.

## What non-parametric means here

KDE does not require the complete price distribution to belong to a prespecified family such as the normal distribution. That is why it is described as non-parametric. It still depends on assumptions and choices: the kernel, bandwidth, measurement scale and handling of boundaries all matter.

Gaussian kernels also assign some density outside the observed range, and in principle below zero. That mathematical tail does not imply that negative resale prices are possible. Boundary-aware methods or a justified transformation may be preferable when behaviour near a natural limit is important.

The next section keeps the idea of adding contributions, but replaces distance along a price axis with geographical distance across a plane.

**Self-check:** What happens when a normalised kernel is widened?

```{dropdown} Feedback
It becomes wider and shorter. Its area remains one, so bandwidth changes shape rather than the total probability mass.
```

## Further reading

Rosenblatt, M. (1956). [Remarks on Some Nonparametric Estimates of a Density Function](https://doi.org/10.1214/aoms/1177728190). *The Annals of Mathematical Statistics*, 27(3), 832–837. Read for density estimation as a statistical construction; return to this page’s bandwidth comparison to connect the estimator with a visible result.
