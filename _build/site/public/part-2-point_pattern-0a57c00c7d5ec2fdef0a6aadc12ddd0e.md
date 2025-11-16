# Chapter 3: Point Pattern

**Objectives of this lecture**

- Understand what is '.bold[Complete Spatial Randomness]' and '.bold[Spatial Patterns]'
- To learn how to identify Clustering Pattern
    - Grid-based, counting: Quadrat Count Analysis
    - Distance-based, sorting: Nearest Neighbor Analysis
    - Distance-based, searching: Ripley's K-function(s)
- Monte-Carlo Simulation



### Two Types Clustering in Spatial Analysis

1. some parts of the study area that have very high concentration of point events, i.e., .red['clusters']
    - to check if this phenomenon exists in the spatial point data
    - to identify the location of these clusters
    - significant tests, CSR

2. groups of spatial points that are close to each other, i.e., .red['clusters']
    - identify grouping of points with/without overlap



### Three Major types of Point Pattern

<img src="resources/w04-img/spatial_patterns_3_basic.png" width="100%">

.red.xkcd[How to differentiate clustered from random .bold[(CSR)]?]

.xkcd[CSR: Complete Spatial Randomness]

---
class: left, middle

.split-50[.column[
### Measurement strategies
].column[
- Grid-based
- Distance-based
]]

---
class: center, middle

### Measurement strategies
#### Grid-based

<img src="resources/w05-img/three_strategies_for_point_pattern_2c.png" width="70%">

---
class: center, middle

### Measurement strategies
#### Distance-based

<img src="resources/w05-img/three_strategies_for_point_pattern_2b.png" width="70%">

