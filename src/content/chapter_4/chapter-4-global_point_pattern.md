# Chapter 4: Global Point Pattern Analysis

Fire detections form concentrations across South Sumatra. Housing transactions occur close together in Singapore neighbourhoods. Bus stops on opposite sides of a street form pairs, even where successive stopping locations are widely spaced. Each map contains point locations, but the geographical meaning of proximity differs.

This chapter asks: **which aspects of an observed arrangement are unusual under a specified spatial reference model?** A map helps us formulate the question. Statistical summaries let us compare the observed arrangement with patterns generated under that model.

## Learning objectives

After completing this chapter, you should be able to:

1. Define a point pattern's observation unit and study window.
2. Explain homogeneous complete spatial randomness (CSR), including the distinction between a Poisson model and a fixed-count simulation.
3. Calculate and interpret quadrat counts, nearest-neighbour summaries and K/L functions.
4. Compare an observed statistic with an appropriate analytical or simulated reference.
5. Explain how boundaries, scale, background intensity and observation conditions affect the conclusions.
6. Distinguish evidence against a reference model from an explanation of the process producing the pattern.

## Begin with the geographical question

A **spatial point pattern** records the locations of events or objects within a defined study window. Its interpretation depends on what each point represents. A FIRMS record is a satellite detection, which may be a repeated observation of ongoing burning. An HDB transaction is an event that may share a building coordinate with other transactions. A bus stop is a physical object constrained by a transport network.

We often describe arrangements as **clustered**, **random** or **regular**. These are useful starting descriptions: points may form groups, arise under a random process, or maintain relatively even separation. They are not conclusions that can be established from appearance alone. A random realisation can contain close pairs and large gaps, and an uneven map can reflect uneven opportunities for events rather than interaction among them.

The reference model makes the comparison precise. Under **homogeneous CSR**, intensity is constant and events are independent. [Section 4.1](sec_04-01-Complete-Spatial-Randomness.md) develops this model and explains when it is a useful baseline. A departure from it may reflect changing background intensity, dependence, geographical constraints or the observation process.

## Three complementary questions

The methods in this chapter summarise different parts of the arrangement.

| Method | What is summarised? | Question answered under the chosen reference |
| --- | --- | --- |
| [Quadrat count analysis](sec_04-02-Quadrat-Count-Analysis.md) | Counts in cells partitioning the window | Is variation among cell counts unusually large? |
| [Nearest Neighbour Analysis](sec_04-03-Nearest-Neighbor-Analysis.md) | Each point's distance to its nearest other point | Is the mean nearest-neighbour distance unusually short or long? |
| [Ripley's K-function](sec_04-04-Ripleys-K-Function.md) | Cumulative neighbour relationships up to each radius | Are there more or fewer nearby pairs than the reference predicts across a range of radii? |

Quadrat analysis converts locations into counts. It is easy to interpret, but discards positions within each cell and depends on the grid's size, shape and origin. NNA retains distances between points but uses only the closest other point for each observation. K examines pairs across a range of radii, producing a cumulative curve whose interpretation requires attention to boundaries and simulation envelopes.

The summaries can disagree without any calculation being wrong. Every quadrat could contain the same number of points, with those points tightly grouped inside each cell. Quadrat counts would then be perfectly even while nearest-neighbour distances would be short. Likewise, paired bus stops can have close first neighbours but wider spacing between stopping locations. A conclusion should identify the summary, scale and reference used rather than give the entire pattern one permanent label.

## How the examples connect

The chapter uses both observed regional data and explicitly synthetic constructions. The constructions hold the point count and window constant, making it easier to see what changes when the arrangement changes. They are teaching examples, not observations of fires, transactions or bus stops.

The observed examples give those comparisons geographical meaning:

- **South Sumatra fire detections:** work through quadrat counts in a western square, repeat the analysis in the adjoining eastern square, then combine them to examine how the study boundary changes the reference.
- **Woodlands point patterns:** compare nearest-neighbour distances while accounting for intensity and window area.
- **Singapore bus-stop motivation:** consider how close pairs can coexist with wider spacing, then use a synthetic paired-site construction to examine cumulative relationships across distances.

Different case studies need not share the same null model. A uniform planar reference may be a useful teaching baseline, while a substantive analysis of road-constrained objects or uneven fire opportunities may require a more specific model.

## Global summaries and local questions

**Global point-pattern analysis** summarises an aspect of the arrangement across the observation window. A global statistic can establish that a particular summary is unusual under a reference, but does not by itself identify every concentration or assign points to clusters. A K curve is also global in this sense, even though it is evaluated at several distances.

[Chapter 5](../chapter_5/chapter-5-local_point_pattern.md) turns towards geographical variation, density and groups within a study area. The distinction concerns the question being asked, rather than an absolute division between methods. Quadrat maps, for example, reveal where counts are high, while their overall goodness-of-fit statistic summarises variation across all cells.

## Reading the evidence

Throughout the chapter, follow the same sequence: define the observations and window, select a summary, specify the reference model, then interpret the comparison. Simulations must reproduce the relevant choices, including the point count when conditioning on it, usable area and calculation procedure.

A small p-value supplies evidence against the specified reference; it does not identify the cause of the pattern. A non-significant result does not prove randomness. Repeated observations, uneven population exposure, land conditions and incomplete coverage may all matter to the geographical interpretation.

### Check your reasoning

**Self-check:** Two maps have the same point count but different window areas. Does the smaller map establish stronger clustering because distances are shorter?

```{dropdown} Feedback
No. The smaller window has higher overall intensity, so its random reference also predicts shorter distances. Compare each observed summary with its appropriate reference.
```

**Self-check:** Would a single global statistic identify which commercial activities belong to each cluster?

```{dropdown} Feedback
No. It summarises the arrangement across the window. Identifying particular groups requires a method and definition suited to that question.
```

**Self-check:** Why might quadrat analysis and NNA give different impressions?

```{dropdown} Feedback
Quadrat counts discard positions within cells. NNA responds to the closest other point. Equal cell counts can coexist with tight groups inside the cells.
```

**Next:** [Spatial Patterns and Complete Spatial Randomness](sec_04-01-Complete-Spatial-Randomness.md).
