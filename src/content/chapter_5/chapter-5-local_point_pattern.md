# Chapter 5: Local point patterns

Chapter 4 asked whether a point pattern, considered across a study window, departed from a specified model of randomness. A global summary can reveal aggregation without showing where the concentrations lie. It can also conceal differences within the window: a dense centre and a sparse fringe may contribute to the same overall statistic. This chapter turns from an overall summary to the geographical arrangement of concentrations and groups. Here, **local description** means identifying where density and algorithmic groups occur. It does not mean a location-specific significance test; Chapter 6 introduces that inferential use of local statistics.

We develop this question using Singapore HDB resale registrations: **where do transactions in the higher and lower parts of the price distribution occur, and how does our description change with the analytical method?** The example connects an attribute distribution to a spatial pattern. It also introduces a distinction that matters throughout spatial analysis: a concentration of events is not automatically a concentration of unusually high values.

## The example and its observations

The teaching snapshot contains 5,379 four-room resale registrations from January through June 2026, at 3,236 distinct block-and-street addresses. Registration month defines inclusion. It does not provide an exact sale date. Each record represents a transaction, while the available coordinate represents its HDB block. Several records can therefore occupy exactly the same mapped position.

Using all selected transactions, the lower price quartile is S\$558,000 and the upper quartile is S\$745,000. We include every record at either cutoff: the lower group contains 1,367 transactions and the upper group contains 1,353. The groups are slightly larger than 25% because prices are tied. Arbitrarily splitting tied prices would create a distinction that is absent from the data.

```{figure} ../datasets/hdb_resale_2026/figures/hdb-overview.png
:label: ch5-hdb-overview
:alt: All transactions and the two price groups
:align: center

The same map extent and colour scale show all transactions, lower-group transactions and upper-group transactions. Markers count sales at blocks, without jitter. URA MP2019 planning areas provide geographical context. They are not the units of this point analysis.
```

The lower-price group occupies more selling blocks than the upper-price group: 1,033 compared with 647. This is a descriptive difference in geographical spread. It does not by itself establish statistically significant clustering. A large volume of transactions in one housing estate can produce a concentration in several price categories simply because many sales occurred there.

We therefore retain the all-sales map as a reference throughout the chapter. When discussing expensive sales, ask both “Where are these sales concentrated?” and “Is their concentration distinctive relative to the locations of sales overall?” These are related but different questions.

## What you will learn

By the end of this chapter, you should be able to explain how bandwidth shapes a density estimate; distinguish probability density, event intensity and average attribute values; compare the purposes of k-means and DBSCAN; and describe how a map's symbols and envelopes affect the interpretation of a cluster. You should also be able to explain why a visually compelling concentration is not a statistical significance test.

The chapter follows one sequence. We first smooth the distribution of resale prices along a number line. We then smooth transaction locations over a map. Next we consider what it means to assign observations to groups, compare two clustering algorithms and examine ways of displaying the resulting groups.

## From a location pattern to a marked point pattern

A point can carry attributes, often called **marks** in point-process analysis. Here the location is the block position and the mark is the transaction price. Analysing locations alone asks where sales occur. Selecting the upper-price group asks where that subset occurs. Including price as a numerical feature in a clustering algorithm asks something else again: which observations are similar under a combined definition of spatial and price difference?

In the main spatial demonstrations, price selects the subset and projected coordinates determine distance. We do not silently add price to the distance calculation. Distances use SVY21 / Singapore TM (EPSG:3414), in metres. Planning-area lines are background context, not barriers or proof of housing-market divisions.

**Before continuing:** Why might a district with many expensive sales have an ordinary proportion of expensive sales? Think about the denominator before interpreting a dark patch on a map.

## Data and reproducibility

Contains HDB resale-price information and HDB/OneMap building coordinates, accessed 21–22 October 2026 and made available under the [Singapore Open Data Licence](https://www.onemap.gov.sg/legal/opendatalicence.html). The coordinate snapshot is distributed by [seehiong/autonomous-hdb-deepagents](https://github.com/seehiong/autonomous-hdb-deepagents), with source attribution to HDB and OneMap, © Singapore Land Authority. URA MP2019 planning areas provide the basemap. See the [dataset sources, matching audit and reproducible figure scripts](https://github.com/wcchin/geo-stat-vis/blob/main/src/content/datasets/hdb_resale_2026/README.md).

**Self-check:** Why does a concentration of expensive sales need a reference pattern?

```{dropdown} Feedback
Many sales of every type may occur where housing stock or turnover is large. Compare with all selling locations and make the denominator explicit.
```
