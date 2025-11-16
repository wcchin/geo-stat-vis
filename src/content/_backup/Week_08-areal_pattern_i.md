slide_title: Areal Pattern I: Spatial Autocorrelation & Hotspot Detection 
custom_css: ../../remarkjs/Catppuccin.css
aspect_ratio: 16:9
remarkjs_path: ../../remarkjs/remark-0.15.0.js
use_mathjax: true
use_mermaid: false
add_sidebar: true
add_searchbar: true
use_click: false
use_scroll: false

name: inverse
layout: true
class: center, middle, inverse
---

## Areal Pattern I: Spatial Autocorrelation & Hotspot Detection 
------

<br />

.x-large.bold[Dr. CHIN Wei Chien Benny]  
[.underline.square[wcchin@nus.edu.sg]]  

.headnote.square.bold.x-large[GE5230 Geospatial Statistics and Visualization]
.footnote.square[08 @ 2025-10-09 Department of Geography, NUS]

---
layout: false
class: center, middle

### What we have learnt so far

<img src="resources/w08-img/recap-1a.drawio.png" width="80%"> 

---
class: center, middle

### What we have learnt so far

<img src="resources/w08-img/recap-1b.drawio.png" width="70%"> 

---
class: center, middle

### What we have learnt so far
.split-40[.column[
.red.xkcd[Why does the spatial pattern of attributes/values matter? And how do we analyze it?] 

Relatie Space: How the neighboring area is related to one/each location.

].column[
<img src="resources/w04-img/drawing-fourspaces.png" width="70%"> 
]]


---
class: left, middle
## Objectives of this lecture
- Autocorrelation and Spatial Autocorrelation

- Related Statistical Testing and Spatial Weighting

- Moran’s I analysis


---
class: center, middle, inverse

.xx-large.bold.wide[PART 1]
## Autocorrelation & Spatial Autocorrelation
------
.square[Autocorrelation .dot[] Spatial Randomness .dot[] Spatial Autocorrelation]

.headnote.square.bold.x-large[Areal Pattern I]

---
class: left, middle
.split-30[.column[
### What is Autocorrelation
].column[
- The 'auto-' in autocorrelation means .red['oneself']. It is a word 'autos' that comes from Greek. 

- Autocorrelation is a measure of the linear relationship .red[between values of a variable and its own nearby values]. The 'self'-correlation here refer to the correlation within one variable itself. 

- Two common types of autocorrelation:
    - Temporal: Correlation between values of a variable and its own past or future. 
    - Spatial: Correlation between values of a variable and its own neighbors. 

- Other types of autocorrelation:
    - Network: between values of a variable and the connected neighbors. 
]]

---
class: left, middle
.split-30[.column[

### What is Spatial Randomness
].column[
#### The null hypothesis
- Spatial Randomness is the absence of any pattern

- Spatial Randomness is not interesting

- if rejected, then there is evidence of spatial structure---spatially structured
]]

---
class: left, middle
.split-30[.column[

### How to interpret Spatial Randomness
].column[
- the observed spatial pattern .red[is equally likely] as any other spatial pattern

- .red[no structure]

- values at one location .red[does not depend on] values at other (neighboring) locations

- value at one location .red[does not tell you anything about] what might be at the nearby locations
]]

---
class: left, middle
.split-30[.column[

### Operationalizing Spatial Randomness
].column[
- under spatial randomness, the location of values may be altered without affecting the information content of the data

- random permutation or reshuffling of values
]]

---
class: center, middle
### Operationalizing Spatial Randomness
.split-50[.column[
<img src="resources/w08-img/Milwaukee_map-1.png" width="90%">  
Actual Distribution
].column[
<img src="resources/w08-img/Milwaukee_map-2.png" width="90%">  
Random Permutation
]]

.footnote[[Luc Anselin's lecture on Spatial Autocorrelation](https://youtu.be/M9sMu73ogIE?si=asaiYfVbCIXlYKkv&t=490)]



---
class: center, middle

### Random Patterns 
<img src="resources/w08-img/random_3.png" width="100%">  
Permutated 3 times

.xkcd[Can you spot the difference?]

---
class: left, middle
.split-30[.column[

### Tobler's first law of geography

.xkcd[How do you define distance?]
].column[
- Everything is related to everything else, but .red.bold[near things] are more related than .red.bold[distant things].
    - Everything depends on everything else, but closer things more so.

- Structures spatial dependence
    - places closer to each other tend to have similar values
    - values of close locations tend to correlated

- the reversed: can we .red[define distance] by observing how things are correlated with each other?
    - if observations are correlated a lot, they are 'close'
    - if they are not correlated, they are 'far'

- Importance of distance decay
    - Distance measure
    - Spatial adjacency structure

- .red[Using some distance metrics to 'structure' the spatial dependence based on 'distance decay' characteristics.]
]]

---
class: left, middle
.split-30[.column[
### What is Spatial Autocorrelation
].column[
- .bold[Rejecting the Null Hypothesis]: rejecting spatial randomness: .red[the observed spatial pattern is not the result of a random process].
    - An evidence of Spatial Dependence: values are autocorrelated spatially
    - An evidence of Spatial Heterogeneity: the underlying probability is non-stationary

- .bold[Positive Spatial Autocorrelation]: .red[similar] values in neighboring locations are found to be more frequent compared to spatial randomness
    - High and High (HH)
    - Low and Low (LL)

- .bold[Negative Spatial Autocorrelation]: .red[dissimilar] values in neighboring locations are found to be more frequent compared to spatial randomness
    - High and Low (HL)
    - Low and High (LH)

]]

---
class: left, middle
### Spatial Autocorrelation: Global vs. Local
.split-50[.column[
.bold[Global Spatial Autocorrelation]:
- analyzing clustering, compared to spatial randomness

- measures the overall degree of spatial clustering or dispersion for the entire study area. 

- provides a single value (e.g., Moran's I) that summarizes the extent to which the variable exhibits a clustered, dispersed, or random pattern across the entire area.

- the spatial autocorrelation of the entire study area '.red[as a whole]'
].column[
.bold[Local Spatial Autocorrelation]:
- identifying clusters, compared to spatial randomness

- calculate the p-value for each location for exploring the probability of becoming a local hot-spot/cold-spot

- provides a map (or a series of maps) that shows where the significant hot-spots/cold-spots

- use the location-based spatial autocorrelation characteristics to detect posisble clusters at .red[specific locations]
]]

---
class: left, middle
.split-30[.column[
### Positive Spatial Autocorrelation
].column[
- Impression of clustering

- Clumps of similar values

- 'Similar' can be both high (hot-spots) or both low (cold-spots)
    - high values near to each other and 
    - low values near to each other, at the same time

- difficult to rely on human perception
]]

---
class: center, middle
### Positive Spatial Autocorrelation

<img src="resources/w08-img/grid_positive_spatial_autocor.png" width="90%">  

---
class: left, middle
.split-30[.column[
### Negative Spatial Autocorrelation
].column[
- checkerboard pattern
    - high value is surrounded by low values
    - low value is surrounded by high values

- alternating values

- more about variability

- hard to distinguish from spatial randomness
]]

---
class: center, middle
### Negative Spatial Autocorrelation

<img src="resources/w08-img/grid_negative_spatial_autocor.png" width="90%">  

---
class: left, middle
.split-30[.column[
### Methods for testing Spatial Autocorrelation
There are several statistical methods for testing global spatial autocorrelation, which helps determine whether the observed spatial pattern in a dataset deviates significantly from a random pattern. 
].column[
- .bold[Moran's I]: Perhaps the most widely used global spatial autocorrelation measure, Moran's I statistic evaluates whether the values of a variable are spatially clustered, dispersed, or randomly distributed. Moran's I ranges from -1 (perfect dispersion) to 1 (perfect clustering), with 0 indicating a random pattern.
- .bold[Geary's C]: Similar to Moran's I, Geary's C measures the degree of spatial autocorrelation in a dataset. While Moran's I focuses on the correlation between a value and its neighboring values, Geary's C emphasizes the differences between a value and its neighbors. Geary's C also ranges from 0 (perfect spatial autocorrelation) to 2 (perfect dispersion), with 1 indicating a random pattern.
- .bold[Getis-Ord Global G]: The Getis-Ord Global G statistic assesses whether the observed spatial pattern exhibits high-value clusters (hotspots) or low-value clusters (coldspots). It provides a single measure of clustering for the entire study area and can be used alongside Moran's I or Geary's C to gain additional insights into the data's spatial structure.
- .bold[Mantel Test]: Originally developed in biology, the Mantel Test is a correlation-based approach that evaluates the relationship between two spatial distance matrices (e.g., geographical and ecological distance matrices). While not strictly a measure of spatial autocorrelation, the Mantel Test can provide valuable insights into the relationship between spatial patterns in different variables.
]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 2]
## Statistical Testing of Spatial Autocorrelation
------
.square[Test statistics .dot[] Attribute-based Similarities .dot[] Locational-based Similarities]

.headnote.square.bold.x-large[Areal Pattern I]

---
class: left, middle
.split-30[.column[
### What is a Test Statistics (recap)
].column[
- a statistic is any value that summarizes characteristics of a distribution

- a test statistics calculated from the data and compared to a reference distribution

- how likely is the value if it had occurrred under the null hypothesis (spatial randomness)

- when unlikely (low p-value) the null hypothesis is rejected
]]

---
class: left, middle
.split-50[.column[
### Testing NNA (recap)
In week 4, we talked about nearest neighbor analysis and how to test the significant levels of the NNA (index). 

The main idea is same, generate a distribution of 'spatial randomness' by permutation (reshuffling values). Then, compare the observed value (calculated from data) to the distribution and calculate p-value (probability of being wrong to reject H0). 

A significant positive Moran's I value indicates a positive spatial autocorrelation. A significant negative Moran's I value indicates a negative spatial autocorrelation. 
].column[
<img src="resources/w05-img/drawing_normal_testing_3.png" width="90%">  

]]

---
class: left, middle
### Spatial Autocorrelation Statistics

Spatial Autocorrelation Statistics captures both .red[attribute similarity] and .red[locational similarity]

.split-50[.column[
.bold[Attribute similarity]: 
- .red[how close are the values]

- measurements of (dis)similarities between values

- squared differences: $(y_i-y_j)^2$

- absolute differences: $|y_i-y_j|$

].column[
.bold[Locational similarity]: 
- .red[how close are the locations]

- relationship of neighborhood between locations

- distance-based metrics (Euclidean, Manhattan)

- adjacency-based spatial weights (rook, queen)

- network-based spatial weights
]]

---
class: center, middle
### Adjacency-based spatial weights
Spatial relationships based on shared border (a.k.a. rook contiguity). Links on the right show the neighborhood relationship.
.split-50[.column[
<img src="resources/w08-img/spatial_weight_share_border.png" width="80%">  
].column[
<img src="resources/w08-img/spatial_weight_share_border_graph.png" width="60%">  
]]

---
class: center, middle
### Adjacency-based spatial weights
Spatial relationships based on shared border (a.k.a. rook contiguity). Links on the left show the neighborhood relationship and the matrix on the right shows the adjacency-matrix / neighborhood matrix. 
.split-50[.column[
<img src="resources/w08-img/spatial_weight_share_border_graph.png" width="60%">  
].column[
$$
\text{W} = 
\begin{bmatrix}
0 & 1 & 0 & 1 & 1 & 0 \\\\
1 & 0 & 0 & 1 & 1 & 0 \\\\
0 & 0 & 0 & 0 & 1 & 1 \\\\
1 & 1 & 0 & 0 & 1 & 0 \\\\
1 & 1 & 1 & 1 & 0 & 0 \\\\
0 & 0 & 1 & 0 & 0 & 0 
\end{bmatrix}
$$
]]

---
class: left, middle
.split-50[.column[

### Spatial Contiguity
- A regular grid, 
- Rook (share edge only) <img src="resources/w08-img/rook-svgrepo.svg" width="10%">
- bishop (share point only) <img src="resources/w08-img/bishop-svgrepo.svg" width="10%">
- queen (share edge and point) <img src="resources/w08-img/queen-svgrepo.svg" width="10%">

Higher levels contiguity can be done by adding second, third, etc. outer ring of neighborhoods.  

].column[
<img src="resources/w08-img/demo_contiguity.png" width="90%">
]]

---
class: left, middle
.split-50[.column[
### Rook and Queen Contiguity
Top: Based on rook contiguity, the Chong Boon Subzone has 4 neighboring subzones.

Bottom: Based on queen contiguity, the same Chong Boon Subzone has 8 neighboring subzones (4 additional).
].column[
<img src="resources/w08-img/Rook_vs_Queen_Contiguity.png" width="85%">

]]

---
class: left, middle
.split-30[.column[
### Higher Order Contiguity

Top: Second level (k=2) contiguity for rook and queen. 

Bottom: Second level contiguity with lower level ($k \leq 2$). 

Left: Rook contiguity

Right: Queen contiguity

].column[
<img src="resources/w08-img/higher_order_Contiguity.png" width="100%">

]]

---
class: left, middle
.split-30[.column[
### Distance-based Weights
].column[
- a.k.a. distance-band weights

- distance between points (polygon centroids, central points)

- can be any function of distnace that implies .red[distance decay], e.g., inverse distance

- in practice, mostly based on a notion of contiguity defined by distance
]]

---
class: left, middle
.split-30[.column[
### Distance-based Weights
].column[
<img src="resources/w08-img/distance_based_1200m.png" width="80%">
]]

---
class: center, middle

### Distance-based Weights

<img src="resources/w08-img/distance_based_differ_size.png" width="65%">

---
class: left, middle
.split-40[.column[
### k-Nearest Neighbor Weights
].column[
- k-nearest observations, irrespective of distance
    - fixed isolates problem for distance bands
    - fixed adjacent but not neighbors issue

- have the same number of neighbors for all observations

- in practice, potential problem with 
    - ties (observations at the same distance)
    - the area size of neighborhood can vary
]]

---
class: center, middle

### k-Nearest Neighbor Weights

<img src="resources/w08-img/knn_example.png" width="65%">

---

class: left, middle
.split-40[.column[
### Row standardization of Spatial Weights
].column[
- the basic spatial weight uses 1 to indicate neighbors and 0 for non-neighbors

- locations with more neighbors with have more '1' in the row, which will get more total 'influences' by all its neighbors

$$
\text{W} = 
\begin{bmatrix}
0 & 1 & 0 & 1 & 1 & 0 \\\\
1 & 0 & 0 & 1 & 1 & 0 \\\\
0 & 0 & 0 & 0 & 1 & 1 \\\\
1 & 1 & 0 & 0 & 1 & 0 \\\\
1 & 1 & 1 & 1 & 0 & 0 \\\\
0 & 0 & 1 & 0 & 0 & 0 
\end{bmatrix}
$$

.xkcd[See the last two rows.] 

]]


---
class: left, middle
.split-30[.column[
### Row standardization of Spatial Weights
].column[
- rescale weights so that for each row i: $\sum(j) w(i,j) = 1$

- $w(i,j)' = \frac{w(i,j)}{\sum_k w(i,k)} $

- makes calculation results comparable
    - all locations will get same level of influence by all their neighbors

    - locations with more neighbors, each of its neighbbors will have less weights of influence to the location, such that the total weight of influence from neighbors is the same with any other location 

- non-symmetrical
]]

---
class: center, middle
### Row standardization of Spatial Weights

.split-50[.column[
$$
\text{W} = 
\begin{bmatrix}
0 & 1 & 0 & 1 & 1 & 0 \\\\
1 & 0 & 0 & 1 & 1 & 0 \\\\
0 & 0 & 0 & 0 & 1 & 1 \\\\
1 & 1 & 0 & 0 & 1 & 0 \\\\
1 & 1 & 1 & 1 & 0 & 0 \\\\
0 & 0 & 1 & 0 & 0 & 0 
\end{bmatrix}
$$
].column[
$$
\text{W}' = 
\begin{bmatrix}
0 & 0.333 & 0 & 0.333 & 0.333 & 0 \\\\
0.333 & 0 & 0 & 0.333 & 0.333 & 0 \\\\
0 & 0 & 0 & 0 & 0.5 & 0.5 \\\\
0.333 & 0.333 & 0 & 0 & 0.333 & 0 \\\\
0.25 & 0.25 & 0.25 & 0.25 & 0 & 0 \\\\
0 & 0 & 1 & 0 & 0 & 0 
\end{bmatrix}
$$

]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 3]
## Moran’s I
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


