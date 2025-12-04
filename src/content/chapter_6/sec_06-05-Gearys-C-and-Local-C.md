# Geary's C and Local Geary

## Geary's C

Geary's C is a global measure of spatial autocorrelation used in spatial data analysis to determine the overall degree of spatial dependency in a dataset. It quantifies the degree to which values in a dataset are similar to or different from neighboring values, considering the entire study area. Unlike  Moran's I, Geary's C focuses on **the distance between value of a location and its neighbors** rather than their distances to the mean value.

$$
C = \frac{(N-1)\sum_i\sum_j w_{ij}(x_i-x_j)^{2}}{2S_0\sum_i(x_i-\bar{x})^{2}}
$$

In this equation:
- $N$ is the number of observations.
- $w_{ij}$ is the spatial weight matrix, representing the spatial relationships between observations $i$ and $j$.
- $x_{k}$ are the observed values of the variable at location k.
- $S_{0}$ is the sum of all spatial weights.
- $\bar{x}$ is the mean of the observed values.
- The lower part (denominator) is a kind of standardizig process to control the range of the resulting values.



## Local Geary's C
The Local Geary:

$$
c_i = \frac{\sum_j w_{ij}(x_i - x_j)^2}{2S_0}
$$

Unlike the global Geary's C, the local version provides **location-specific information about spatial autocorrelation**, allowing for the identification of spatial clusters and outliers. **Low values** of the Local Geary's C indicate **positive** spatial autocorrelation (**similar values cluster together**), while **high values** indicate **negative** spatial autocorrelation (**dissimilar values are close to each other**).


## Comparing Global vs. Local

$$\text{global} = a . [\sum_i \text{component}(i)]$$

### Global

$$
C = \frac{(N-1)\sum_i\sum_j w_{ij}(x_i-x_j)^{2}}{2S_0\sum_i(x_i-\bar{x})^{2}}
$$

$$
C = \frac{(N-1)}{2S_0\sum_i(x_i-\bar{x})^{2}} \times \sum_i\sum_j w_{ij}(x_i-x_j)^{2}
$$

$$
C = \frac{(N-1)}{\sum_i(x_i-\bar{x})^{2}} \times \sum_i \frac{1}{2S_0}\times \sum_j w_{ij}(x_i-x_j)^{2}
$$

$$
C = \frac{(N-1)}{\sum_i(x_i-\bar{x})^{2}} \times \sum_i c_i
$$


### Local
$$
c_i = \frac{\sum_j w_{ij}(x_i - x_j)^2}{2S_0}
$$

$$
c_i = \frac{1}{2S_0} \times \sum_j w_{ij}(x_i - x_j)^2
$$





## Interpretation

- $(x_i - x_j)^2$

- attribute **dissimilarity**

- distance in attribute space

- Geary's C: weighted average of distances in **attribute space** to neighbors in **geographic space**

- positive: similarity, can be high-high, low-low, **middle-middle**

- negative: dissimilarity: no distinction between high-low and low-high

- Geary's C is more sensitive to **local patterns of spatial autocorrelation** and can better capture smaller-scale variations in the data.
**spatial non-stationarity**: a sub-region of the study area has a different (e.g., lower) average value, for which the similar-values (could be middle-middle) may be overlooked by Moran's I (and its local variant).

### An example

Take an example: the donations data (Guerry data)

```{figure} ../resources/w09-img/guerry_data.png
:label:
:alt:
:align: center

The data distribution (based on Natural Breaks).
```



### Local Significance Map

```{figure} ../resources/w09-img/guerry_LC_significant_map.png
:label:
:alt:
:align: center

Local Significance Map
```


#### Local Cluster Map

```{figure} ../resources/w09-img/guerry_C_cluster_map.png
:label:
:alt:
:align: center

Local Cluster Map
```

### Sensitivity Analysis

```{figure} ../resources/w09-img/guerry_C_cluster_map_sensitivity.png
:label:
:alt:
:align: center

Sensitivity Analysis
```


## Local Moran's I vs. Local Geary's C

```{figure} ../resources/w09-img/guerry_I_C_cluster_map_sensitivity.png
:label:
:alt:
:align: center

Comparison between local Moran's I and local Geary's C
```

### Moran's I vs. Geary's C

- Different type of attribute similarity
    - cross-product (correlation) vs.
    - squared difference (dissimilarity)

- power against different alternatives
    - the same null hypothesis: spatial randomness
    - what should be the 'alternative'?

- Moran's I and its local variant: Detect similar values based on their **deviation from the mean value**.
    - Moran's I is more sensitive to global patterns of spatial autocorrelation and overall trends in the data.

- Geary's C and its local variant: Detect similar values based on the **absolute differences between pairs of values**.
    - Geary's C is more sensitive to local patterns of spatial autocorrelation and smaller-scale variations in the data.
