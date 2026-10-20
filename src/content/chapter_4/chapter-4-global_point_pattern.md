# Chapter 4: Global Point Pattern Analysis

The locations of geographical events and objects often reveal distinctive spatial patterns. Disease cases may concentrate in particular neighbourhoods, bus stops may occur in pairs along roads, and trees may be distributed relatively evenly across a managed landscape.

These arrangements raise an important geographical question: **do the observed locations form a meaningful spatial pattern, or could the apparent pattern have arisen by chance?**

A map allows us to explore the distribution of geographical features visually. However, visual inspection alone cannot establish whether a pattern is statistically unusual. What appears to be a cluster may simply reflect the number of points, the size of the study area, or the geographical conditions under which events occur.

**Spatial point-pattern analysis** provides statistical methods for examining the spatial arrangement of points and comparing observed patterns with an appropriate reference model.

In this chapter, we explore three methods—**Quadrat Count Analysis, Nearest Neighbour Analysis, and Ripley's K-function**—to investigate whether points exhibit clustering or dispersion, and how these patterns may vary across spatial scales.

## Learning objectives

After completing this chapter, you should be able to:

1. **Describe** the characteristics of clustered, random, and regular spatial point patterns.
2. **Explain** Complete Spatial Randomness (CSR) as a reference model for spatial point-pattern analysis.
3. **Compare** grid-based and distance-based methods for measuring spatial patterns.
4. **Apply and interpret** Quadrat Count Analysis, Nearest Neighbour Analysis, and Ripley's K-function.
5. **Evaluate** statistical evidence of clustering or dispersion using appropriate reference models and Monte Carlo simulation.
6. **Recognise** how study boundaries, spatial scale, and analytical choices influence the interpretation of point patterns.

## Understanding spatial point patterns

A **spatial point pattern** describes the geographical arrangement of events or objects represented as points within a defined study area.

Depending on the underlying processes, points may appear concentrated in certain locations, spread relatively evenly across space, or distributed without an obvious spatial structure.

Three broad patterns are commonly distinguished:

- **Clustered:** Points tend to occur close together, forming concentrations or groups.
- **Random:** Points are distributed according to a random spatial process, without systematic attraction or inhibition between events.
- **Regular (dispersed):** Points tend to maintain greater separation from one another, producing a more evenly spaced arrangement.

```{figure} ../resources/w04-img/spatial_patterns_3_basic.png
:label: ch4-basic-point-patterns
:alt: Illustrations comparing regular, random, and clustered spatial point patterns.
:align: center

Three broad types of spatial point patterns: regular, random, and clustered.
```

These descriptions help us recognise different spatial arrangements. However, **a visually clustered pattern is not necessarily statistically significant**, and a pattern that appears random may still contain spatial relationships that are difficult to identify by eye.

We therefore need a statistical reference against which the observed pattern can be evaluated.

## What do we mean by spatial clustering?

The term *spatial clustering* can refer to different, but related, geographical questions.

One question concerns the **overall spatial arrangement** of points:

*Do events tend to occur closer together than would be expected under a specified random spatial process?*

For example, we may examine whether HDB resale transactions across a selected part of Singapore exhibit an overall tendency towards clustering.

A second question concerns the **locations of particular concentrations or groups**:

*Where are the clusters, and which points belong to them?*

For example, we may wish to identify specific neighbourhoods with high concentrations of transactions or distinguish separate groups of commercial activities.

These questions require different analytical approaches.

**Global point-pattern analysis**, the focus of this chapter, summarises spatial relationships across a study area. It helps determine whether the overall arrangement of points departs from a specified reference model.

**Local pattern analysis and spatial clustering methods**, introduced in Chapter 5, focus more directly on geographical variation, concentrations, and groups within the study area.

The distinction is not absolute. Some methods can provide information relevant to both objectives. What matters is identifying the geographical question before selecting the analytical method.

## How can we measure spatial patterns?

There are two broad strategies for examining the arrangement of spatial points: **grid-based** and **distance-based** approaches.

### Grid-based approach

A grid-based approach divides the study area into smaller spatial units and counts the number of points within each unit.

If points are distributed relatively evenly, the counts may be similar across the grid. If points are concentrated in particular locations, some cells may contain substantially more points than others.

```{figure} ../resources/w05-img/three_strategies_for_point_pattern_2c.png
:label: ch4-grid-based-strategy
:alt: Illustration of grid-based approaches to point-pattern analysis, including point counting and density estimation.
:align: center

Grid-based approaches summarise the distribution of points within predefined spatial units.
```

The main advantage of this approach is its simplicity: it transforms point locations into counts that can be compared statistically.

However, the results may depend on the **size, shape, and placement of the grid cells**. The same point pattern can appear more or less concentrated when different grid configurations are used.

In Section 4.2, we introduce **Quadrat Count Analysis** as a grid-based method for examining spatial point patterns.

### Distance-based approach

Instead of dividing space into predefined units, a distance-based approach examines the spatial relationships between individual points.

Two related strategies are particularly useful:

- **Nearest-neighbour distance:** Measure the distance from each point to its closest neighbouring point.
- **Search-radius distance:** Examine how many neighbouring points fall within a specified distance, and repeat the calculation across different distances.

```{figure} ../resources/w05-img/three_strategies_for_point_pattern_2b.png
:label: ch4-distance-based-strategy
:alt: Illustration comparing nearest-neighbour distances with neighbours counted within a search radius.
:align: center

Distance-based approaches examine spatial relationships between points using nearest-neighbour distances or a series of search radii.
```

These approaches address related but distinct questions.

Nearest-neighbour distances describe the immediate proximity of points. Search-radius approaches examine spatial relationships over multiple distances, allowing us to investigate whether clustering or dispersion changes with spatial scale.

In Sections 4.3 and 4.4, we introduce **Nearest Neighbour Analysis** and **Ripley's K-function** to explore these relationships.

## From visual patterns to statistical evidence

Recognising a spatial pattern is only the first step. We also need to determine whether the observed arrangement is unusual relative to an appropriate statistical reference.

A commonly used reference in point-pattern analysis is **Complete Spatial Randomness (CSR)**.

Under the standard CSR model, points occur independently and with constant intensity across the study area. Even under these conditions, some points will appear close together while other parts of the study area remain relatively empty.

Consequently, the presence of visible concentrations does not automatically establish that a point pattern is clustered in a statistical sense.

To evaluate the evidence, we compare an observed statistic with the values expected under CSR or another suitable null model. **Monte Carlo simulation** is one way to generate such a reference distribution by repeatedly producing random point patterns under specified conditions.

This comparison helps us distinguish between a descriptive tendency towards clustering or dispersion and statistical evidence against the reference model.

Importantly, rejecting CSR does not necessarily explain *why* the observed pattern occurs. Geographical interpretation still requires consideration of the study area, observation process, population at risk, and other relevant spatial factors.

Section 4.1 develops the concept of CSR and its role in statistical testing.

## Three approaches to global point-pattern analysis

The three methods introduced in this chapter examine different aspects of spatial point distributions.

| Method | What it measures | Central question |
|---|---|---|
| **Quadrat Count Analysis** | Variation in point counts across spatial units | Are points distributed unevenly across the study area? |
| **Nearest Neighbour Analysis** | Average distance to the nearest other point | Are points unusually close together or far apart? |
| **Ripley's K-function** | Neighbour relationships across increasing distances | At which spatial distances does clustering or dispersion occur? |

No single method provides a complete description of every spatial pattern.

A point distribution may show clustering at short distances but a more regular arrangement at larger distances. Similarly, a pattern that appears clustered using one grid configuration may produce a different result when the analytical scale changes.

The choice of method should therefore reflect the **geographical question, characteristics of the data, and spatial scale of interest**.

### Check your reasoning

Before proceeding, consider the following questions:

1. Two maps contain the same number of points, but one covers a much larger geographical area. Can we conclude that the smaller-area pattern is more clustered simply because its points are closer together?
2. If our objective is to identify specific locations where commercial activities concentrate, would a single global point-pattern statistic be sufficient?
3. Why might Nearest Neighbour Analysis and Ripley's K-function lead to different interpretations of the same point distribution?

As you work through the following sections, revisit these questions and consider how each method helps answer them.

**Next:** [Spatial Patterns and Complete Spatial Randomness](sec_04-01-Complete-Spatial-Randomness.md).
