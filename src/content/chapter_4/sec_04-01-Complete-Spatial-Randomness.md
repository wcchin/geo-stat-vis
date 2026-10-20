# Spatial Patterns and Complete Spatial Randomness

## What is a spatial point pattern?

Geographical events and objects are often represented as points on a map. These may include the locations of traffic accidents, disease cases, bus stops, trees, or individual housing transactions.

A **spatial point pattern** consists of the locations of observed events within a defined geographical region, known as the **study window**.

Two elements are therefore essential:

- **Point events:** The observations represented by geographical coordinates.
- **Study window:** The geographical area within which these events are observed or could occur.

For example, when examining traffic accidents in Singapore, each recorded accident may be represented by a point. However, the appropriate study window may be the relevant road network rather than the entire geographical area, including parks, reservoirs and other locations where road accidents cannot occur.

The study window is not simply a boundary drawn around the points. It is part of the definition of the spatial process being studied.

### Reading a point pattern

Consider the historical cholera map produced by John Snow, which illustrates the geographical distribution of cholera deaths in London.

```{figure} ../resources/w04-img/johnsnowmap_1.png
:label: ch4-snow-original
:alt: Historical map showing the geographical distribution of cholera deaths.
:align: center

John Snow's cholera map, illustrating the use of point locations to investigate a geographical pattern.
```

The map invites several questions:

- Where are the events concentrated?
- Are some locations relatively isolated?
- Where are the areas with few or no observations?
- Could the apparent concentrations reflect the distribution of the population or other geographical conditions?

```{figure} ../resources/w04-img/johnsnowmap_2.png
:label: ch4-snow-pattern
:alt: Annotated version of the cholera map highlighting the geographical distribution of events.
:align: center

Exploring concentrations and gaps in a spatial point pattern.
```

Visual exploration helps us recognise potential patterns. However, it cannot establish whether the arrangement is statistically unusual or explain the processes that produced it.

## Recognising spatial patterns

Spatial point patterns are commonly described as **clustered, random, or regular**.

- **Clustered patterns:** Points tend to occur close together, producing concentrations or groups.
- **Random patterns:** Points occur according to a specified random spatial process. Some apparent concentrations and gaps may arise purely by chance.
- **Regular patterns:** Points tend to be more evenly spaced, suggesting inhibition or separation between events.

```{figure} ../resources/w04-img/spatial_patterns_3_basic.png
:label: ch4-three-patterns
:alt: Comparison of regular, random and clustered spatial point patterns.
:align: center

Three broad spatial point-pattern arrangements.
```

These categories describe different arrangements, but visual appearance alone does not determine which statistical process generated the points.

For example, a random point pattern may contain several closely spaced points and relatively large empty spaces. Such features do not necessarily contradict randomness.

This leads to an important distinction:

**A pattern that looks clustered is not necessarily more clustered than we would expect from a random spatial process.**

To evaluate this distinction, we need a reference model.

## Complete Spatial Randomness (CSR)

**Complete Spatial Randomness (CSR)** is a statistical reference model commonly used in spatial point-pattern analysis.

The standard CSR model is a **homogeneous Poisson point process**, characterised by two properties.

### 1. Constant intensity

The expected number of events per unit area is constant throughout the study region.

This property is described by the **intensity**, commonly represented by $\lambda$:

$$
\lambda=\frac{E[N(A)]}{|A|}
$$

where:

- $\lambda$ is the expected number of points per unit area;
- $E[N(A)]$ is the expected number of events in region $A$;
- $|A|$ is the area of that region.

For an observed point pattern, intensity is commonly estimated as:

$$
\hat{\lambda}=\frac{n}{|A|}
$$

where $n$ is the observed number of points.

Constant intensity does not mean that every small region contains exactly the same number of points. The actual counts vary randomly, even when their expected values are equal.

### 2. Independence

Under CSR, events occur independently of one another.

The occurrence of one event does not make another event more or less likely to occur nearby.

This distinguishes CSR from processes involving spatial attraction or inhibition:

- **Attraction:** Events tend to occur near other events, potentially producing clustering.
- **Inhibition:** Events tend to maintain separation, potentially producing regularity.

```{figure} ../resources/w04-img/describe_CSR2.png
:label: ch4-csr-concept
:alt: Illustration explaining the properties of Complete Spatial Randomness.
:align: center

Complete Spatial Randomness provides a reference for comparing observed point patterns.
```

Under homogeneous CSR, the number of events in a region of area $|A|$ follows a Poisson distribution with mean $\lambda |A|$. Counts in disjoint regions are independent.

When simulations retain the observed number of points $n$, CSR can instead be represented by placing those $n$ points independently and uniformly within the fixed study window. This is the **conditional-on-$n$** form of the CSR model.

Both approaches are useful, but the simulation procedure should match the null hypothesis and the statistic being evaluated.

## Why can random patterns appear clustered?

Imagine observing 100 point events within a 2 km × 2 km study window in Woodlands, Singapore.

Suppose the points are generated independently and uniformly across the window.

Although the process is random, the resulting map is unlikely to show perfectly even spacing. Some points will occur close together, while other areas may contain few or no points.

If we repeat the simulation, each realisation will produce a different arrangement, even though the underlying statistical process remains unchanged.

**Randomness describes the process generating the points, not a requirement that the observed points appear evenly spaced.**

A regular arrangement, such as points positioned on an equally spaced grid, is therefore not the same as CSR.

### Demonstration: Three patterns in the same study window

Consider three synthetic point patterns generated within the same 2 km × 2 km window, each containing 100 points:

1. **CSR:** Points are placed independently and uniformly within the window.
2. **Clustered:** Points are generated around several local centres.
3. **Regular:** Points are arranged with a tendency to maintain separation.

The patterns have identical point counts and study-window areas, but their spatial arrangements differ.

*Planned teaching figure: a three-panel, Python-generated XKCD-style illustration comparing CSR, clustered and regular patterns. The figure will use synthetic projected coordinates and a fixed random seed.*

This demonstration illustrates why the number of points and the study area must be considered when evaluating clustering or dispersion.

It also introduces an important principle: **a statistical comparison requires a clearly specified reference model**.

## Spatial stationarity and CSR

The concept of **spatial stationarity** concerns whether the statistical properties of a spatial process remain unchanged when locations are shifted across space.

For point-pattern analysis, an important starting point is whether the expected intensity remains constant across the study region.

Under homogeneous CSR, intensity is constant and events are independent. The process is therefore spatially stationary.

However, **stationarity and CSR are not equivalent**.

A spatial point process may have constant intensity while exhibiting dependence between events. For example, a stationary clustered process may generate groups of points throughout the study region without systematically favouring one geographical location over another.

Conversely, an inhomogeneous Poisson process allows intensity to vary across space while retaining independence between events.

This distinction matters when interpreting geographical patterns.

Consider traffic accidents along a road network. Accident intensity may vary because some roads carry more traffic than others. A concentration of accidents near a busy intersection may therefore reflect greater exposure rather than interaction between accident events.

Comparing such observations with homogeneous CSR may reveal a departure from constant-intensity randomness, but it does not establish the cause of that departure.

```{figure} ../resources/w04-img/drawing_street.png
:label: ch4-stationarity-street
:alt: Illustration of accident events along a street, used to discuss spatial intensity and stationarity.
:align: center

A road-based example for considering whether the expected intensity of events remains constant across space.
```

### A note on broader stationarity concepts

In spatial statistics, *strict stationarity* refers to invariance of the full joint distribution under spatial translation. *Second-order stationarity* is a weaker condition commonly used for random fields, requiring a constant mean and a covariance structure that depends on spatial separation rather than absolute location.

These concepts are important in broader spatial statistics and geostatistics. For the point-pattern methods introduced in this chapter, our immediate concern is the relationship between **intensity, independence, and the chosen reference model**.

## Comparing observed patterns with CSR

CSR is commonly used as a **null hypothesis** in spatial point-pattern analysis.

The basic question is:

*How unusual is the observed spatial arrangement if the points were generated under CSR?*

The general testing strategy involves four steps.

### Step 1: Define the geographical problem

Identify the events, study window, observation unit and spatial relationships of interest.

For example, are we examining individual HDB transactions, unique residential buildings, or bus-stop locations?

These represent different geographical questions and may require different assumptions.

### Step 2: Select a spatial statistic

Choose a statistic that captures the aspect of the point pattern relevant to the question.

Examples include:

- Variation in counts across quadrats.
- Average nearest-neighbour distance.
- Number of neighbouring points within increasing distances.

Different statistics describe different properties of the same point distribution.

### Step 3: Establish a CSR reference

We can use a theoretical distribution, an analytical approximation, or **Monte Carlo simulation** to determine what values of the statistic might be expected under CSR.

In a fixed-count simulation, we repeatedly generate $n$ independent uniform point locations within the same study window and calculate the chosen statistic for each simulated pattern.

```{figure} ../resources/w04-img/drawing_random_pts_3.png
:label: ch4-random-points
:alt: Illustration of randomly generated spatial points.
:align: center

Randomly generated point patterns provide a reference for evaluating observed spatial arrangements.
```

The simulated statistics form a **reference distribution** against which the observed statistic can be compared.

### Step 4: Evaluate the evidence

If the observed statistic lies in an unusually extreme part of the reference distribution, this may provide evidence against CSR.

The interpretation depends on the statistic and the alternative hypothesis.

For example:

- An unusually short mean nearest-neighbour distance may indicate clustering.
- An unusually long mean nearest-neighbour distance may indicate dispersion.
- Unusually large variation in quadrat counts may indicate an uneven distribution of events.

A statistically significant result indicates that the observed statistic is unusual under the specified null model.

It does **not** automatically establish the geographical process responsible for the pattern.

Similarly, a non-significant result does not prove that the point pattern is random. It indicates that the selected test has not provided sufficient evidence against the null model.

```{figure} ../resources/w04-img/spatial_patterns_2_basic_b.png
:label: ch4-csr-comparison
:alt: Comparison of spatial point patterns used to illustrate departures from Complete Spatial Randomness.
:align: center

Comparing observed patterns with a random spatial reference helps distinguish visual impressions from statistical evidence.
```

## Geographical considerations

Before applying CSR-based methods, several geographical decisions deserve attention.

**Study-window boundaries.** The reference model should represent the area in which events could reasonably occur. Including inaccessible land or water may distort the expected spatial distribution.

**Population at risk.** Events such as disease cases, accidents or commercial activities may be concentrated where people, roads or economic opportunities are concentrated. Homogeneous CSR may therefore be an unsuitable model for some geographical questions.

**Observation units.** Multiple records may share the same coordinates. For example, several housing transactions may occur within the same building. Whether these are treated as separate events or unique locations changes the analytical question.

**Spatial scale.** A point pattern may appear clustered at one distance but relatively dispersed at another. Different methods and analytical scales can reveal different aspects of the distribution.

**Coordinate systems.** Distance-based methods require appropriate spatial coordinates. For local analysis in Singapore, projected coordinates measured in metres are generally preferable to longitude and latitude expressed in degrees.

These considerations remind us that statistical evidence must be interpreted in the context of the geographical problem.

## Check your reasoning

### 1. Can a random point pattern contain visible clusters?

Yes. Under CSR, events occur independently, but some will happen to fall close together. Visible concentrations alone do not establish statistically significant clustering.

### 2. Does constant intensity mean equal numbers of points everywhere?

No. Constant intensity means equal expected counts for regions of equal area. The observed counts may differ because of random variation.

### 3. Is every stationary point process completely spatially random?

No. A stationary process can exhibit clustering or inhibition. CSR requires both constant intensity and independence.

### 4. If a point pattern significantly differs from CSR, have we identified the cause?

No. A departure from CSR may reflect interactions between events, variation in population exposure, geographical constraints or other processes. Additional analysis is needed to evaluate possible explanations.

## Moving to Quadrat Count Analysis

We now have a reference model for asking whether an observed spatial point pattern differs from randomness.

The next question is how to quantify that difference.

In **[Quadrat Count Analysis](sec_04-02-Quadrat-Count-Analysis.md)**, we begin with a grid-based approach: dividing the study area into smaller spatial units and comparing the variation in observed point counts with what would be expected under CSR.

This provides our first practical method for evaluating global spatial point patterns.
