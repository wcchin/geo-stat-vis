# Geary's C and Local Geary
------
.square[Geary's C .dot[] Local Geary]

.headnote.square.bold.x-large[Areal Pattern II]

---
class: left, middle
.split-60[.column[
### Spatial Autocorrelation metrics and their Local versions
].column[
- Moran's I and Local Moran's I

- .red[Geary's C and Local Geary's C]

- General G statistics, Gi, and Gi*
]]

---
class: left, middle
.split-30[.column[
### Geary's C
The lower part (denominator) is a kind of standardizig process to control the range of the resulting values.

].column[
Geary's C is a global measure of spatial autocorrelation used in spatial data analysis to determine the overall degree of spatial dependency in a dataset. It quantifies the degree to which values in a dataset are similar to or different from neighboring values, considering the entire study area. Unlike  Moran's I, Geary's C focuses on .red.bold[the distance between value of a location and its neighbors] rather than their distances to the mean value.

$$
C = \frac{(N-1)\sum\_i\sum\_j w\_{ij}(x\_i-x\_j)^{2}}{2S\_0\sum\_i(x\_i-\bar{x})^{2}}
$$
<!--<img src="resources/w09-img/geary_c_equation.png" width="80%">-->

In this equation:
- $N$ is the number of observations.
- $w_{ij}$ is the spatial weight matrix, representing the spatial relationships between observations $i$ and $j$.
- $x_{k}$ are the observed values of the variable at location k.
- $S_{0}$ is the sum of all spatial weights.
- $\bar{x}$ is the mean of the observed values.

]]

---
class: left, middle
.split-30[.column[
### Local Geary's C
The lower part (denominator) is a kind of standardizig process to control the range of the resulting values.

].column[
And the Local Geary
$$
c\_i = \frac{\sum\_j w\_{ij}(x\_i - x\_j)^2}{2S\_0}
$$
<!--<img src="resources/w09-img/geary_c_local_equation.png" width="80%">-->

Unlike the global Geary's C, the local version provides .red[location-specific information about spatial autocorrelation], allowing for the identification of spatial clusters and outliers. .bold.red[Low values] of the Local Geary's C indicate .red[positive] spatial autocorrelation (.red[similar values cluster together]), while .bold.red[high values] indicate .red[negative] spatial autocorrelation (.red[dissimilar values are close to each other]).

]]

---
class: center, middle
### Comparing Global vs. Local
$$\text{global} = a . [\sum_i \text{component}(i)]$$

.split-50[.column[
#### Global
$$
C = \frac{(N-1)\sum\_i\sum\_j w\_{ij}(x\_i-x\_j)^{2}}{2S\_0\sum\_i(x\_i-\bar{x})^{2}}
$$

$$
C = \frac{(N-1)}{2S\_0\sum\_i(x\_i-\bar{x})^{2}} \times \sum\_i\sum\_j w\_{ij}(x\_i-x\_j)^{2}
$$

$$
C = \frac{(N-1)}{\sum\_i(x\_i-\bar{x})^{2}} \times \sum\_i \frac{1}{2S\_0}\times \sum\_j w\_{ij}(x\_i-x\_j)^{2}
$$

$$
C = \frac{(N-1)}{\sum\_i(x\_i-\bar{x})^{2}} \times \sum\_i c\_i
$$


].column[
#### Local
$$
c\_i = \frac{\sum\_j w\_{ij}(x\_i - x\_j)^2}{2S\_0}
$$

$$
c\_i = \frac{1}{2S\_0} \times \sum\_j w\_{ij}(x\_i - x\_j)^2
$$
]]



---
class: left, middle
.split-30[.column[
### Interpretation
].column[
- $(x_i - x_j)^2$

- attribute dissimilarity

- distance in attribute space

- Geary's C: weighted average of distances in .red[attribute space] to neighbors in .red[geographic space]

- positive: similarity, can be high-high, low-low, .red[middle-middle]

- negative: dissimilarity: no distinction between high-low and low-high

- Geary's C is more sensitive to .red[local patterns of spatial autocorrelation] and can better capture smaller-scale variations in the data.
.red.bold[spatial non-stationarity]: a sub-region of the study area has a different (e.g., lower) average value, for which the similar-values (could be middle-middle) may be overlooked by Moran's I (and its local variant).
]]

---
class: left, middle
.split-30[.column[

### Interpretation
#### An example (for reference)
Take an example: the donations data (Guerry data)
].column[
<img src="resources/w09-img/guerry_data.png" width="100%">

]]

---
class: left, middle
.split-30[.column[
### Interpretation
#### Local Significance Map
].column[
<img src="resources/w09-img/guerry_LC_significant_map.png" width="100%">

]]

---
class: left, middle
.split-30[.column[
### Interpretation
#### Local Cluster Map
].column[
<img src="resources/w09-img/guerry_C_cluster_map.png" width="100%">

]]

---
class: center, middle

### Interpretation
#### Comparison between p-value

<img src="resources/w09-img/guerry_C_cluster_map_sensitivity.png" width="100%">

---
class: center, middle

### Local Moran's I vs. Local Geary's C

<img src="resources/w09-img/guerry_I_C_cluster_map_sensitivity.png" width="65%">

---
class: left, middle
.split-30[.column[
### Moran's I vs. Geary's C
].column[

- Different type of attribute similarity
    - cross-product (correlation) vs.
    - squared difference (dissimilarity)

- power against different alternatives
    - the same null hypothesis: spatial randomness
    - what should be the 'alternative'?

- Moran's I and its local variant: Detect similar values based on their .red[deviation from the mean value].
    - Moran's I is more sensitive to global patterns of spatial autocorrelation and overall trends in the data.

- Geary's C and its local variant: Detect similar values based on the .red[absolute differences between pairs of values].
    - Geary's C is more sensitive to local patterns of spatial autocorrelation and smaller-scale variations in the data.


]]
