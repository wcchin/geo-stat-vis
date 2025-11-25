# Chapter 4: Global Point Pattern

**Objectives of this lecture**

- Understand what is '**Complete Spatial Randomness**' and '**Spatial Patterns**'
- To learn how to identify Clustering Pattern
    - Grid-based, counting: Quadrat Count Analysis
    - Distance-based, sorting: Nearest Neighbor Analysis
    - Distance-based, searching: Ripley's K-function(s)
- Monte-Carlo Simulation



## Two Types Clustering in Spatial Analysis

1. some parts of the study area that have very high concentration of point events, i.e., _'clusters'_
    - to check if this phenomenon exists in the spatial point data
    - to identify the location of these clusters
    - significant tests, CSR

2. groups of spatial points that are close to each other, i.e., _'clusters'_
    - identify grouping of points with/without overlap



## Three Major types of Point Pattern

```{figure} ../resources/w04-img/spatial_patterns_3_basic.png
:label:
:alt:
:align: center

Regular, random, and clustered.
```


How to differentiate clustered from random **(CSR)**?


CSR: Complete Spatial Randomness


## Measurement strategies

- Grid-based
- Distance-based

#### Grid-based

```{figure} ../resources/w04-img/three_strategies_for_point_pattern_2c.png
:label:
:alt:
:align: center

Grid-based: density estimation and quadrat count.
```

#### Distance-based

```{figure} ../resources/w04-img/three_strategies_for_point_pattern_2b.png
:label:
:alt:
:align: center

Distance-based: search for the k-nearest and find neighbors fall within a search-radius (buffer).
```
