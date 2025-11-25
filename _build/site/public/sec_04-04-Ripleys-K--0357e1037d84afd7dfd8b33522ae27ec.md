# Ripley's K-function

## The 2 Distance-based Approaches

```{figure} ./resources/w05-img/three_strategies_for_point_pattern_2b.png
:label:
:alt:
:align: center

Everyone look for the nearest neighbor vs. everyone draw a series of search buffer (radius).
```
In this section, we focus on the second approach.

## Bus Stops Distribution

Take bus stops distribution for example:
- Bus stops usually constructed in pairs, at both sides of a street.
- The nearest neighbor is at a short distance (opposite of street), but the second nearest may not.
- Is it a "real" clustered pattern?

```{figure} ./resources/w05-img/Bus_Stop_nearest_neighbor.png
:label:
:alt:
:align: center

Bus Stops distribution. Is the nearest neighbor distance 'meaningful'?
```


## The Search Radius Approach

The Ripley's K-function:

- Generate a series of search radius (SR), from low to high
- Search for pairs of points fall within every SR
- The implication:
    - if a lot of pairs are found within a short SR: the points are clustered at this distance.

```{figure} ./resources/w05-img/simulate_kfunc.gif
:label:
:alt:
:align: center

Simulation of the buffer area and counting.
```

A common transformation of the K-function:

$$
L(d) = \sqrt{\frac{A \times \text{pairs}_d }{\pi n(n-1)}}
$$

$$
\text{pairs}\_d = \sum\_{i=1}^n \sum\_{j=1, j\neq i}^n w\_{ij}
$$

- $L(d)$: the k-function value at search radius $d$
- $\text{pairs}_d$: the number of pairs of points with distance less than $d$
- $w_{ij}$: equal to 1 if non-weighted; weighting for edge-correction
- $A$: Area of study
- $n$: total number of points
- $n(n-1)$: total number of all pairs

More info: [ESRI ArcGIS: How multi-distance spatial cluster analysis works.](https://pro.arcgis.com/en/pro-app/3.1/tool-reference/spatial-statistics/h-how-multi-distance-spatial-cluster-analysis-ripl.htm)


## Testing for K-functions

- __How high is high enough__ to be considered as clustered?
- To compare them with CSR, __Monte Carlo Simulation__ can be used (again)


```{figure} ./resources/w05-img/kfunc_arcGIS_redraw.png
:label:
:alt:
:align: center

The clustered and dispersed range of K-function curve.
```

For demonstration: 10 random patterns are generated


```{figure} ./resources/w05-img/k_function_4cases_rand.png
:label:
:alt:
:align: center

K-function curve of the four examples and the k-function curves of the corresponding 10 random distributions.
```

Calculate 95% Confidence envelop. See [ESRI](https://pro.arcgis.com/en/pro-app/3.1/tool-reference/spatial-statistics/h-how-multi-distance-spatial-cluster-analysis-ripl.htm) for more details.


```{figure} ./resources/w05-img/k_function_4cases_rand.png
:label:
:alt:
:align: center

The k-function curves and the confidence interval (Monte Carlo Simulation) for the 4 examples.
```

## Comparison between NNA and K-function results


:::{figure}
:label: comparison-nna-kfunc
:align: center

(NNA)=
![Nearest Neighbor Analysis](./resources/w05-img/drawing_nna_res_2.png)

(kfunc)=
![Ripley's K-function](./resources/w05-img/k_function_4cases_ci.png)

The results for the 4 examples using two methods.
:::


## Summary: Repley's K-function

**Purpose**

Ripley's K function is a tool used to analyze spatial point patterns, helping researchers understand the spatial relationships among events or objects in a given study area.

**Functionality**

The K function estimates the expected number of points within a given distance from a randomly chosen point, providing insights into clustering, dispersion, or randomness in the spatial pattern.

**Key features**

- The K function can be plotted as a function of distance to visualize changes in spatial interactions at different scales.
- It can be compared with theoretical models, such as complete spatial randomness (CSR), to assess deviations from expected patterns.
