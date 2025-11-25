# Statistical Testing of Spatial Autocorrelation
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
