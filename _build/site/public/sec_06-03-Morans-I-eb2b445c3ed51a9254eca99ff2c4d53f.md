# Moran’s I
------
.square[Moran’s I .dot[] Calculation .dot[] Interpretation .dot[] Permutation ]

.headnote.square.bold.x-large[Areal Pattern I]

---
class: center, middle

### Moran’s I main goal
Moran's I is a widely-used measure of .red[global spatial autocorrelation], developed by Australian statistician Patrick Moran. It quantifies the degree to which the values of a variable are .red[spatially correlated with their neighboring values] across an entire study area.

<img src="resources/w08-img/morans_i_goals.png" width="80%">

.footnote[[Global Moran's I (ArcGIS)](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/spatial-autocorrelation.htm)]

---
class: left, middle
.split-30[.column[
### Moran’s I calculation

Moran's I ranges from:
- -1 (indicating .red[perfect dispersion] or negative spatial autocorrelation) to
- +1 (indicating .red[perfect clustering] or positive spatial autocorrelation), with
- 0 indicating a .red[random] spatial pattern (no spatial autocorrelation).

].column[
Moran's I is defined as:

<img src="resources/w08-img/morans_I_equation.png" width="80%">

Where:
- $N$ is the number of spatial units indexed by $i$ and $j$;
- $x$ is the variable of interest;
- $\bar{x}$ is the mean of $x$;
- $w_{i,j}$ is the spatial weight---kind of an indicator variable, equal to 1 or the row-standardized value if $i$ and $j$ are neighbors, 0 otherwise;
- W is the sum of all $w\_{i,j}$.

A significant Moran's I value suggests that the observed spatial distribution of the variable is not random, and further investigation is warranted to understand the underlying spatial relationships and processes.
]]

---
class: left, middle
### Moran’s I calculation

<img src="resources/w08-img/morans_I_equation.png" width="60%">

Each value is compared to the mean value ($\bar{x}$) before the multiplying. Given the value ($x_i$) of a location and one of its neighbor's value ($x_j$), the multiplying result:
- is a .red[positive value] because both are at the same direction (both higher or both lower);
- is a .red[negative value] if one of which is higher than the mean and the other is lower compared to mean value;
- will be a .red[large value] if both the self and neighbor values are very far from the mean value;
- will be a .red[small value] (near to zero) if the two values are near to mean.

Note that if they are both a lot lower than the mean value, the result would also be a .red[large positive high value], indicating .red[positive spatial autocorrelation].

---
class: left, middle
### Moran’s I: Interpretation
.split-50[.column[
.bold[Reading I]
- theoretical mean is 1/(N-1), essentially zero for large N

- positive and significant: clustering of similar value
    - NOT clustering of high or low
    - could be either or a combination

- negative and significant: alternating values
    - presence of spatial outliers
    - spatial heterogeneity (checkerboard pattern)
].column[
.bold[Comparing the I]
- Moran's I depends on spatial weights

- relative magnitude for .red[same weights settings] and different variables is .red[meaningful]

- .red[NOT for different spatial weights]
    - use standardized z-value to compare
]]

.footnote.small[[see here for more details on the calculation of z-value](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/h-how-spatial-autocorrelation-moran-s-i-spatial-st.htm)]

---
class: left, middle
.split-30[.column[
### Moran’s I: Interpretation
#### Reading I
].column[
<img src="resources/w08-img/moran-result-demo.png" width="100%">

]]

---
class: left, middle
.split-40[.column[
### Moran’s I Scatter Plot: Interpretation

- X-axis: the standardized crime rate of every location (town)

- Y-axis: the average of standardized neighborhood's crime rate (spatial-lag of the variable)

- Moran's $I = 0.5237$ (written on top)

].column[
<img src="resources/w08-img/morans_I_example-1.png" width="80%">
]]

---
class: left, middle
.split-40[.column[
### Moran’s I Scatter Plot: Interpretation
The 4 quadrants:
- .bold[upper right]: self-.red[High] - lag-.red[High] (HH), positively autocorrelated with high values, indicate potential hot-spots;
- .bold[lower left]: self-.red[Low] - lag-.red[Low] (LL), positively autocorrelated with low values, indicate potential cold-spots;
- .bold[upper left]: self-.red[Low] - lag-.red[High] (LH), negatively autocorrelated;
- .bold[lower right]: self-.red[High] - lag-.red[Low] (HL), negatively autocorrelated.
- Required statistical testing to identify significant hot-spots and cold-spots.

].column[
<img src="resources/w08-img/morans_I_example-1.png" width="80%">
]]

---
class: left, middle
.split-30[.column[
### Permutation Approach
].column[
- Random reshuffling the attributes data, without modifying the locational data

- recompute Moran's I each time

- reconstructing a .red[reference distribution]

- compare the (original data) .red[observed value of Moran's I] to the reference distribution

- .red[even a high Moran's I value does not necessarily indicate significance.]

- the 'p-value' is not the same as the statistical p-value, it should be called pseudo-p-value as it is calculated using a permutation approach from empirical data, rather than estimated with some solid statistical method.

- the number of permutation will 'improve' the p-value.
]]

---
class: left, middle
.split-30[.column[
### Permutation Approach
#### (demo)
].column[
<img src="resources/w08-img/permutation_distribution.png" width="80%">
]]

---
class: left, middle
.split-30[.column[
### A demonstration
#### Moran's Scatter plot
The bus ridership aggregated by incoming flow, during the morning peak (7am-9am) in June 2023. Spatial weights are 2 levels of Queen contiguity.

Moran's I = 0.03
].column[
<img src="resources/w08-img/demo_weekday.png" width="100%">
]]

---
class: left, middle
.split-30[.column[
### A demonstration
999 times permutation is generated.
].column[
<img src="resources/w08-img/moran-i-weekday_morningpeak.png" width="80%">
]]

---
class: center, middle, inverse

## Closing Remarks
------
.square[Spatial Autocorrelation .dot[] Spatial Testing .dot[] Spatial Weights .dot[] Moran's I ]

.headnote.square.bold.x-large[Areal Pattern I]

---
class: left, middle
.split-30[.column[
### Recap of this lecture
].column[
- spatial randomness for areal data

- spatial autocorrelation

- spatial dependency and spatial heterogeneity

- attributes similarity and locational similarity

- spatial weights and row standardization
    - contiguity (rook, queen) and higher order
    - distance-based
    - k-nearest neighbors

- Moran's I
    - goals to identify positive and negative spatial autocorrelation
    - calculation
    - how to read the result
    - permutation
]]
