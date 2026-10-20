---
label: complete-spatial-randomness
---

# Spatial Patterns and Complete Spatial Randomness

## Define what a point represents and where it could be observed

Before measuring a point pattern, specify its **observation unit** and **study window**. The observation unit determines what each point represents; the window defines the region within which the observations are analysed. Together with the time interval and recording process, these choices determine the question a statistical comparison can answer.

For the South Sumatra example in the next section, each point is a qualifying satellite fire detection during September 2026. One persistent fire can produce several records. Retaining them asks about detection locations over the month, rather than the locations of distinct ignitions. In the housing example, several transactions may share a building coordinate. Aggregating these records would change the observation unit from transactions to locations.

The window is equally consequential. An arbitrary boundary around the observed points does not establish where events could have been recorded. For a land-based fire question, ocean should not be treated as zero-fire land. For road accidents, a road network may define the relevant spatial support rather than the surrounding plane. A network reference must measure opportunity along that network; it is not obtained simply by placing uniform points in a bounding rectangle.

Define these choices from the geographical question and observation design where possible. If a window is selected after inspecting the pattern, report that exploratory choice. The Sumatra windows are used as illustrations of the method, rather than as a prespecified regional hypothesis test.

## A model for the comparison

A concentration of points can arise for several reasons. Events may influence one another, opportunities may vary across space, or the observation system may record some locations more often than others. Even independent points with equal opportunity across a window can form visible groups by chance.

**Complete spatial randomness (CSR)** provides a reference against which to examine the observed arrangement. The standard model is a **homogeneous Poisson point process**. Two properties define the baseline used here: constant intensity and independent counts in disjoint regions.

### Constant intensity

Intensity, denoted by $\lambda$, is the expected number of points per unit area. If $B$ is a subregion with area $|B|$, homogeneous intensity implies

$$
\mathbb{E}[N(B)]=\lambda |B|,
$$

where $N(B)$ is the number of events in that subregion. Equal-area regions therefore have equal expected counts. Their observed counts need not be equal.

Let $W$ denote the observation window and $n$ its observed point count. A simple estimate of intensity is

$$
\widehat\lambda=\frac{n}{|W|}.
$$

For example, 96 points in a 2 km by 2 km square give an estimated intensity of 24 points per km². That describes the overall rate; it does not describe whether the points form pairs, groups or an evenly spaced arrangement.

### Independence and Poisson counts

Under homogeneous Poisson CSR,

$$
N(B)\sim\operatorname{Poisson}(\lambda |B|),
$$

and counts in disjoint regions are independent. There is no attraction or inhibition between events under this model. Observing an event does not change the model's rate for additional events nearby.

Independence does not require points to remain far apart. Several independent events can fall close together, and large gaps can occur. Conversely, arranging points to maintain nearly equal separation introduces a spacing constraint rather than representing CSR.

## Two simulation designs: varying or fixing the count

The distinction between a Poisson process and its fixed-count reference matters throughout this chapter.

| Reference design | What varies between simulations? | How are locations generated? |
| --- | --- | --- |
| Homogeneous Poisson in $W$ | Total count and locations | Draw $N\sim\operatorname{Poisson}(\lambda |W|)$, then place $N$ independent uniform locations in $W$ |
| Conditional on the observed $n$ | Locations; the count stays fixed | Place exactly $n$ independent uniform locations in $W$ |

In the first design, specify the intensity used. In the second, condition on the observed count and ask about the allocation of those points within the window. The fixed-count design is the one used for the chapter's synthetic comparisons and FIRMS quadrat simulations.

Conditioning changes the relationship between cell counts. Suppose the window is partitioned into $m$ cells, with usable areas $A_1,\ldots,A_m$. Their counts satisfy

$$
(O_1,\ldots,O_m)\mid n\sim
\operatorname{Multinomial}(n;p_1,\ldots,p_m),
\qquad p_i=\frac{A_i}{|W|}.
$$

The counts sum to $n$ and are therefore **not independent**: allocating more of the fixed total to one cell leaves fewer for the others. This does not contradict the independence of disjoint-region counts in the unconditioned Poisson model. The locations in the fixed-count simulation are still independent uniform draws; the resulting cell counts have the sum constraint.

Both designs are useful. State which is used and match the observed and simulated calculation procedures.

## Why a random realisation can look uneven

```{figure} ../resources/original/quadrat-three-patterns.svg
:label: csr-shared-synthetic-patterns
:alt: Three synthetic patterns with 96 points in equal two-kilometre square windows: a CSR realisation, a clustered construction and a spaced construction, with quadrat counts.
:align: center

The chapter's shared synthetic examples each contain 96 points in the same 2 km square. Only their arrangement changes. The grid anticipates the next section; the constructions are not observed regional data.
```

The CSR panel is one realisation of independent uniform placement. Repeating the procedure would produce another arrangement, with different close pairs, gaps and cell counts. The process remains the same even though the map changes.

The clustered and spaced constructions provide contrasts. Holding the count and area constant isolates differences in arrangement, but the labels describe how those teaching examples were constructed. To assess an observed pattern, we still need to select a statistic and establish its reference distribution.

This figure reappears in the quadrat section, where we calculate the cell counts. NNA and K then examine the same synthetic coordinates using different summaries. A single map can therefore support several questions without requiring all methods to reach the same conclusion.

## Separate uneven intensity from interaction

Constant intensity and independence are different assumptions. A process may have a constant average rate while producing dependent groups. Alternatively, an **inhomogeneous Poisson process** can have a rate that varies across space while retaining independent counts in disjoint regions.

This distinction is central to geographical interpretation. Fire detections may be more frequent where vegetation, land management or burning conditions favour activity. Disease events may be more frequent where more people live. Bus stops follow road networks and service design. A departure from homogeneous planar CSR can reflect these differences in opportunity without demonstrating attraction among events.

**Spatial stationarity** concerns invariance of a process's statistical properties under translation. Homogeneous Poisson CSR is stationary, but stationarity does not imply CSR: a stationary process can exhibit clustering or inhibition. Constant intensity alone is also insufficient to establish full stationarity.

```{note} A broader use of stationarity
Strict stationarity concerns invariance of the full joint distribution under translation. For random fields, second-order stationarity concerns a constant mean and a covariance structure depending on separation rather than absolute location. These broader concepts return in other parts of spatial statistics. Here, focus on whether intensity is constant and whether events are independent under the chosen point-process reference. A finite or irregular observation window is a sampling restriction, not by itself evidence that the underlying process is nonstationary.
```

## From a model to statistical evidence

A reference model becomes useful when paired with a summary of the arrangement. Follow four steps.

1. **Define the question and observations.** Specify the observation unit, period, usable window, coordinate system and relevant recording conditions.
2. **Choose the statistic and alternative.** Quadrat variation, mean nearest-neighbour distance and cumulative pair relationships capture different properties. Decide which departures would address the question.
3. **Construct the reference.** Use an appropriate analytical result or simulate under the specified model. For a fixed-count comparison, retain $n$, the same usable window and the same calculation procedure.
4. **Interpret the observed statistic relative to that reference.** Explain both the evidence against the model and what the comparison leaves unresolved.

The direction of comparison depends on the statistic. Unusually large quadrat variation suggests uneven allocation. Unusually short nearest-neighbour distances suggest close first neighbours; unusually long distances address a different alternative. A K curve requires attention to the range of radii and whether inference concerns one radius or the whole curve.

Monte Carlo simulations generate a reference distribution of the chosen statistic. They do not need to resemble the observed map visually. What must match are the choices required by the null model and the statistic, including any boundary correction and grid specification.

A small p-value indicates that the observed statistic is unusual under the specified reference. It is not the probability that CSR is true, and it does not identify the process responsible for the departure. A non-significant result means that this comparison has not supplied sufficient evidence against the reference; it does not establish randomness in every aspect of the pattern.

## Geographical choices to carry into the methods

**Boundaries and usable area.** Including sea or inaccessible land changes the reference opportunity. Clipped quadrats require usable-area expectations, while distance summaries require attention to missing neighbours beyond the observation boundary.

**Observation and exposure.** A period with records on every date does not establish complete or spatially uniform coverage. Satellite overpasses, clouds, reporting practices and population at risk may affect the locations recorded.

**Coordinates and scale.** Use a suitable metric coordinate system for planar areas and distances. A pattern can contain close pairs within more widely spaced groups. State the grid size or distance range rather than assuming one scale describes the whole pattern.

These choices shape the question before any statistic is calculated. Simulation can reproduce a chosen window and procedure, but cannot make an unsuitable observation design or null model appropriate.

## Check your reasoning

```{dropdown} 1. Can independent uniform points contain visible groups?
Yes. Close pairs and gaps occur by chance. Compare a chosen summary with its reference distribution rather than deciding from appearance alone.
```

```{dropdown} 2. Does constant intensity require equal observed counts in equal-area cells?
No. It requires equal expected counts. Realised counts vary.
```

```{dropdown} 3. Are quadrat counts independent when the total is fixed?
No. They sum to the fixed total and follow a multinomial distribution under independent uniform placement. Disjoint-region counts are independent in the unconditioned Poisson model.
```

```{dropdown} 4. Does rejection of homogeneous CSR demonstrate attraction between individual fires?
No. Changing background opportunity, repeat detections, observation coverage and dependence can all contribute. Satellite detections are also not necessarily distinct fires.
```

```{dropdown} 5. Can a stationary process be clustered?
Yes. A process can generate groups throughout space without systematically favouring an absolute location. Stationarity and CSR are not equivalent.
```

## Read further and continue

- **Textbook:** Baddeley, A., Rubak, E. and Turner, R. (2015). [Spatial Point Patterns: Methodology and Applications with R](https://doi.org/10.1201/b19708). Read the introductory treatment of point patterns, observation windows and Poisson processes alongside the chapter examples.
- **Published introduction:** Wiegand, T. and Moloney, K. A. (2004). [Rings, circles, and null-models for point pattern analysis in ecology](https://doi.org/10.1111/j.0030-1299.2004.12497.x). *Oikos*, 104, 209–229. Consider how the null model determines the interpretation of a departure.
- **Implementation reference:** [spatstat: quadrat.test](https://search.r-project.org/CRAN/refmans/spatstat.explore/html/quadrat.test.html) distinguishes conditional and unconditional simulations and alternative hypotheses. The next section develops the count-level calculation.

**Next:** [Quadrat Count Analysis](sec_04-02-Quadrat-Count-Analysis.md). We partition the window, calculate expectations under the fixed-count reference, and work through the synthetic and South Sumatra examples.
