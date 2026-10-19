---
label: nearest-neighbour-analysis
---

# Nearest Neighbour Analysis

## When is close unusually close?

A map may look crowded, but proximity alone does not establish clustering. One hundred events placed independently in a small park will usually be closer together than one hundred events placed independently across a town. We need a reference that accounts for both the number of events and the space in which they could occur.

**Nearest Neighbour Analysis (NNA)** asks whether the average distance from an event to its nearest other event is unusually short or long relative to a specified random point process. It summarises the pattern across the study area; it does not identify the location of each cluster.

After this section, you should be able to calculate and interpret the nearest-neighbour ratio, explain its CSR reference, and distinguish a descriptive result from evidence against a null model.

```{figure} ../resources/w05-img/four_demo_points.png
:label: nna-four-patterns
:alt: Four point patterns in the Woodlands area shown within equally sized study windows.
:align: center

Examples from Woodlands Regional Centre, Woodlands West and Woodgrove, each within a 2 km by 2 km window. Predict which has the shortest average nearest-neighbour distance. Would that alone tell you which is most unusual under randomness?
```

## From individual distances to one summary

For each point, find the closest **other** point and record its distance. A point is not its own neighbour. Two points can be each other's nearest neighbours, so one pair can contribute a distance for both observations.

With $n$ points and nearest-neighbour distance $d_i$ for point $i$, the observed mean is

$$
\bar{D}_O=\frac{1}{n}\sum_{i=1}^{n}d_i.
$$

If coordinates are in metres, the mean is in metres. Use a suitable projected coordinate system for local Euclidean analysis; longitude and latitude in degrees are not distances in metres.

```{figure} ../resources/w05-img/simulate_nna.gif
:label: nna-search-animation
:alt: Animation connecting each point to its nearest other point.
:align: center

Each event contributes its nearest-neighbour distance. We average these distances, rather than distances between every possible pair.
```

A short observed mean can result from clustering, high overall intensity, or repeated records at identical coordinates. We therefore need an appropriate comparison.

## The CSR reference and nearest-neighbour ratio

[Complete spatial randomness (CSR)](sec_04-01-Complete-Spatial-Randomness.md) is commonly represented by a homogeneous Poisson process: intensity is constant and events occur independently. Let $A$ be the study area and estimate intensity by $\lambda=n/A$. The theoretical expected nearest-neighbour distance for a homogeneous planar Poisson process is

$$
\bar{D}_E=\frac{1}{2\sqrt{\lambda}}=\frac{0.5}{\sqrt{n/A}}.
$$

The Clark–Evans nearest-neighbour ratio is

$$
R=\frac{\bar{D}_O}{\bar{D}_E}.
$$

| Ratio | Descriptive interpretation |
|---|---|
| $R<1$ | Neighbours are closer than the theoretical CSR expectation: a tendency towards clustering. |
| $R\approx1$ | The mean is close to that expectation. |
| $R>1$ | Neighbours are farther apart: a tendency towards regularity or dispersion. |

The ratio is dimensionless. Its direction does not by itself establish statistical significance. A ratio near one does not demonstrate that every aspect of a pattern follows CSR.

### A numerical example

Consider an **illustrative dataset**, separate from the Woodlands figures: 100 events in 1 km². Working in metres gives $A=1{,}000{,}000$ m² and

$$
\bar{D}_E=\frac{0.5}{\sqrt{100/1{,}000{,}000}}=50\text{ m}.
$$

If the observed mean is 35 m, $R=35/50=0.70$. The observed mean is 30% shorter than the theoretical expectation. This does **not** mean that 70% of points are clustered or that there is a 30% probability of clustering.

## How unusual is the observed distance?

We can use an analytical approximation or construct a reference distribution by simulation. Both require an explicit null model and a question specified before inspecting the result.

A question about **clustering** uses a lower-tail alternative: are distances unusually short? A question about **dispersion** uses the upper tail. A two-sided question permits either departure. Selecting whichever one-sided test looks significant after seeing the data changes the testing procedure.

### Analytical Clark–Evans comparison

The standard error commonly used for the planar CSR approximation is

$$
SE=\frac{0.26136}{\sqrt{n^2/A}}=0.26136\frac{\sqrt{A}}{n}.
$$

The z-score measures the difference in standard-error units:

$$
z=\frac{\bar{D}_O-\bar{D}_E}{SE}.
$$

For the illustrative example, $SE\approx2.61$ m and $z\approx-5.74$. Under the approximation, this is a very short mean distance relative to CSR. A lower-tail p-value comes from the standard normal distribution.

The simple formula does not correct for boundaries. Its theoretical expectation describes an unbounded planar process, whereas an observation window has edges beyond which possible neighbours are not observed. Do not assume its reference exactly matches a finite-window simulation.

### Monte Carlo comparison

For a rectangle, simulate independent uniform locations within the **same fixed window**, with the **same number of points**, and calculate the same statistic each time. This is the conditional-on-$n$ form of the homogeneous Poisson null model.

```{figure} ../resources/w05-img/monte_carlo_point_pattern.gif
:label: nna-csr-simulation
:alt: Repeated random point patterns generated within one fixed study window.
:align: center

The window and point count stay fixed while locations change. Each simulation contributes one mean nearest-neighbour distance to the reference distribution.
```

The empirical reference distribution need not be assumed normal. Compare the observed mean directly with the simulations. With $M$ simulated patterns, a lower-tail Monte Carlo p-value is

$$
p_{\mathrm{lower}}=\frac{k+1}{M+1},
$$

where $k$ is the number of simulated mean distances less than or equal to the observed mean $\bar{D}_O$. Include ties. The added one prevents a zero p-value; with 999 simulations, the minimum is 0.001. More simulations improve resolution and reduce Monte Carlo variability, but do not guarantee a smaller p-value.

A finite-window simulation reproduces the window's boundary geometry when observed and simulated statistics use the same procedure. It does not recover missing outside neighbours or make an unsuitable study window appropriate.

```{figure} ../resources/w05-img/nna_compare_hist.png
:label: nna-reference-histogram
:alt: Observed mean nearest-neighbour distances compared with reference distributions from CSR simulations.
:align: center

Read each observed statistic relative to its own reference distribution. How unusual is the distance under that reference, rather than how short does it look in isolation?
```

## What can we conclude?

A small lower-tail p-value provides evidence of clustering at the nearest-neighbour scale under the specified null model. It does not establish a cause, locate individual clusters, or show that every point belongs to a cluster.

A non-significant result means this test has not supplied sufficient evidence against the null model. It does not prove randomness: a pattern may differ from CSR in ways a nearest-neighbour summary misses.

A p-value concerns the behaviour of the statistic **assuming the null model**. It is not the probability that the null is true or that a particular rejection is wrong.

## Geographical choices that change the answer

**Study window.** Define where events could have occurred from the question and observation design. Enlarging the window while retaining the same points reduces intensity and increases the expected mean, making the same distances look more clustered. A convenient rectangle may include sea or inaccessible land. A polygonal null window requires sampling within that polygon.

**Observation unit and coincident points.** In the course's HDB example, records represent transactions, not necessarily unique buildings. Several transactions may share coordinates and have zero nearest-neighbour distances. Retaining them asks about transaction events; aggregating them asks a different question about locations. Explain the choice.

**Population at risk.** Accidents or disease events may concentrate where roads or people are concentrated. Rejection of homogeneous CSR may reflect uneven opportunity for events rather than interaction among events. Consider whether a network-constrained or inhomogeneous model fits the question better.

**Scale.** NNA uses one neighbour per event. [Ripley's K-function](sec_04-04-Ripleys-K-Function.md) examines neighbours within several distances. A pattern can be clustered at one scale and dispersed at another.

## Try it yourself

The [NNA self-study notebook](../notebooks/lab-05-nna-self-study.ipynb) uses synthetic data with NumPy, SciPy and Matplotlib, and accepts a projected-coordinate CSV. Compare clustered, CSR and regular patterns, then change one analytical choice at a time.

Follow the [Gordon Square worked example](../worked_examples/sec_04-A-Demonstration-point-pattern.md) to contrast individual people with groups. The [full point-pattern lab](../notebooks/lab-05-point-pattern.ipynb) connects quadrat counts, NNA and K/L functions. Revisit the [Semester 2610 Week 5 slides](../part4.md) for the visual lecture explanation.

### Check your reasoning

```{dropdown} 1. Keep the same points but double the window area. What happens to R?
The observed mean stays the same. The theoretical expected distance increases by $\sqrt{2}$, so $R$ decreases by that factor. This illustrates window sensitivity; it does not justify choosing a window to obtain a desired answer.
```

```{dropdown} 2. A lower-tail test gives p = 0.24. Have we shown randomness?
No. We have not found sufficient evidence of unusually short mean nearest-neighbour distances under this null model. This does not establish that the whole pattern is random.
```

```{dropdown} 3. Several transactions share a building coordinate. Should we remove them?
It depends on the observation unit. Retain records for a question about transaction events, or aggregate for a question about distinct locations. State the choice and its implications for the null model.
```

## Further reading

- [ArcGIS: How Average Nearest Neighbor works](https://doc.esri.com/en/arcgis-pro/latest/tool-reference/spatial-statistics/h-how-average-nearest-neighbor-distance-spatial-st.html): equations, assumptions and interpretation.
- [SciPy: Monte Carlo tests](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.monte_carlo_test.html): empirical reference distributions and alternatives.
