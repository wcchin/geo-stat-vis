---
label: areal-pattern-analysis
---

# Chapter 6: Spatial Association in Areal Data

In Chapter 4, we examined where point events occur. Here, we begin with spatial units that already have values: median household income in each administrative area. The question changes from the arrangement of event locations to the **arrangement of attribute values across connected places**.

Two maps can contain the same values and have identical histograms, yet show very different geographical patterns. Higher values might occur beside other higher values, alternate with lower values, or form several distinct regional configurations. Spatial association concerns that relationship between values and their geographical arrangement.

## Learning objectives

After completing this chapter, you should be able to:

1. Distinguish point-location patterns from spatial patterns of attributes attached to areas.
2. Explain positive and negative spatial autocorrelation relative to specified neighbourhoods.
3. Construct and interpret spatial weights and spatial lags.
4. Interpret global Moran's I, Geary's C and Getis–Ord General G under their stated references.
5. Distinguish local similarity, spatial outliers and local concentrations using appropriate statistics and inference.
6. Evaluate how aggregation, neighbour definitions, observation conditions and multiple testing affect conclusions.

## Values and relationships must be considered together

A table describes the distribution of values. A map shows where those values occur. A spatial analysis also specifies which places are related and how those relationships enter the calculation.

There are two separate ingredients:

| Ingredient | Examples | Question it addresses |
| --- | --- | --- |
| Attribute relationship | Mean-centred cross-products, squared differences, neighbourhood sums | What aspect of similarity, contrast or concentration matters? |
| Spatial relationship | Shared boundaries, distance bands, nearest neighbours | Which locations are compared, and with what weights? |

A short geographical distance is not the same as a small difference in income. Likewise, two districts with similar incomes are not necessarily geographical neighbours. Spatial association combines an attribute comparison with a defined spatial relationship.

The chapter uses **Peninsular Malaysian household income** to introduce the arrangement of values on administrative areas. The same income observations continue through the global and local statistics, providing one coherent regional example. Small, explicitly synthetic examples make calculations transparent. A teaching construction is not an observed regional result; each page distinguishes the two.

## A connected reading sequence

| Section | Main question | What it establishes |
| --- | --- | --- |
| [6.1 Spatial autocorrelation](sec_06-01-Spatial-Autocorrelation.md) | What does the arrangement of values tell us? | Association, random reassignment and geographical interpretation |
| [6.2 Distance and neighbourhoods](sec_06-02-Statistical-Spatial-Testing.md) | Which places count as neighbours? | Weights, graph structure, standardisation and spatial lags |
| [6.3 Moran's I](sec_06-03-Morans-I.md) | Do neighbouring deviations tend to be similar overall? | Cross-products, the scatterplot and global randomisation inference |
| [6.4 Local Moran's I](sec_06-04-Local-Moran.md) | Where are local similarities and contrasts? | Local clusters, outliers and location-specific inference |
| [6.5 Geary's C and Local Geary](sec_06-05-Gearys-C-and-Local-C.md) | What do neighbour differences reveal? | A dissimilarity-based comparison with Moran's approach |
| [6.6 Getis–Ord G statistics](sec_06-06-Getis-Ord-G.md) | Where do relatively high or low values concentrate? | Global and local concentration statistics and their interpretation |

Read 6.1 and 6.2 before calculating a coefficient. Choosing the variable, spatial support and neighbours is part of defining the analysis, rather than a technical step to postpone until after the result.

## Global association and local patterns

A **global** statistic summarises a relationship across the included study units. A **local** statistic describes a relationship around a particular unit. Neither replaces the other. Overall positive association can coexist with a district that contrasts with its neighbours; opposing local patterns can also be obscured by a modest global result.

A high value surrounded by high values and a low value surrounded by low values both describe similarity. A high value among low neighbours, or the reverse, describes contrast. These descriptions do not establish statistical significance. Local inference requires a specified statistic and reference, and testing many units creates a multiple-comparison problem.

The methods also ask different attribute questions. Moran's mean-centred products, Geary's squared differences and Getis–Ord neighbourhood concentrations should not be treated as interchangeable ways to colour the same map. Their definitions and reference distributions matter more than choosing whichever produces the clearest-looking pattern.

## What stays fixed under randomisation?

For the initial areal-data reference, we hold the spatial units and weights fixed and randomly reassign the observed values. This preserves the multiset of values while changing their geographical arrangement. It differs from the point-process simulations in Chapter 4, where event locations were generated within a window.

The reassignment reference assumes exchangeability under the null. Unequal land exposure, survey uncertainty, spatial trends and differing observation conditions can make unrestricted permutation an incomplete substantive model. Rejection describes incompatibility with that reference; it does not establish direct influence between neighbours or identify a causal mechanism.

## Check your reasoning

**Self-check:** Why can identical histograms accompany different spatial association?

```{dropdown} Feedback
A histogram does not retain which spatial unit receives each value. Association also depends on the assignment and the neighbour relationships.
```

**Self-check:** Does a low-income district next to another low-income district imply negative association?

```{dropdown} Feedback
No. Similar low values contribute to positive association under a similarity-based summary. Positive and negative do not mean desirable and undesirable.
```

**Self-check:** Does a global coefficient identify every local hotspot?

```{dropdown} Feedback
No. It summarises the overall relationship. Local concentrations and spatial outliers require their own analysis and inference.
```

**Next:** [Autocorrelation and Spatial Autocorrelation](sec_06-01-Spatial-Autocorrelation.md).

## Try it yourself

Apply the concepts in the corresponding [Part 3 notebook catalogue](../part3.md). The linked learner notebooks include guided activities; companion solutions are available from their introductions or from the catalogue.

- [Global Moran's I](../notebooks/global-spatial-autocorrelation.ipynb)
- [Local Moran contributions](../notebooks/local-spatial-autocorrelation.ipynb)
- [Malaysian income maps and permutations](../notebooks/malaysia-income-mapping-permutations.ipynb)
- [Malaysian income spatial inference](../notebooks/malaysia-income-areal-inference.ipynb)

**Reflect:** Explain how neighbourhood weights define the comparison. Distinguish a descriptive quadrant or statistic from a statistically supported interpretation.
