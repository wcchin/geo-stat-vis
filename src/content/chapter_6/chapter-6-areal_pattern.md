# Chapter 6: Areal Pattern

**Objectives of this lecture**




## Spatial Autocorrelation Statistics
It is about the values of spatial features

```{figure} ../resources/w08-img/recap-1a.drawio.png
:label:
:alt:
:align: center

What we have learnt: The patterns of statistical values and the patterns of locations.
```

```{figure} ../resources/w08-img/recap-1b.drawio.png
:label:
:alt:
:align: center

What we have learnt: The intersection---location of values, values of locations.
```


Spatial Autocorrelation Statistics captures both **attribute similarity** and **locational similarity**

**Attribute similarity**:
- _how close are the values_

- measurements of (dis)similarities between values

- squared differences: $(y_i-y_j)^2$

- absolute differences: $|y_i-y_j|$


**Locational similarity**:
- _how close are the locations_

- relationship of neighborhood between locations

- distance-based metrics (Euclidean, Manhattan)

- adjacency-based spatial weights (rook, queen)

- network-based spatial weights
