# Density-Based Spatial Clustering of Applications with Noise (DBSCAN)
------
.square[Key Concepts .dot[] Parameters .dot[] Applications]

.headnote.square.bold.x-large[Point Pattern III]

---
class: left, middle

.split-30[.column[
### Density-Based Spatial Clustering of Applications with Noise (DBSCAN)
].column[

- The algorithm finds dense areas and expands these recursively to find .red[dense arbitrarily shaped clusters].

- Two main parameters to DBSCAN are ‘Epsilon (ε)’ and ‘minPoints’.
    - ‘Epsilon (ε, or Eps)’ defines radius of the ‘neighborhood region’ and
    - ‘minPoints’ defines the minimum number of points that should be contained within that neighborhood to be considered as 'high density'.

- The '.red[density]' refers to the number of points within Eps, which should be larger than minPoints.

- Since it .red[has a concept of noise], it works well even with noisy datasets.
]]

---
class: center, middle

### Arbitrary shape clusters

<img src="resources/w07-img/arbitrary_shape.png" width="70%">

---
class: left, middle

### Key concepts

.split-40[.column[
<img src="resources/w07-img/dbscan_key_concept.png" width="100%">
minPoint = 4
].column[
- .bold[Epsilon neighborhood] (Nε): set of all points within a distance ‘ε’.
- .bold[Core point]: A point that has at least ‘minPoint’ (including itself) points within it’s Nε.
- .bold[Directly Density Reachable (DDR)]: A point q is .underline[directly density reachable] from a point p if .red[p is core point] and q ∈ Nε of p.
- .bold[Density Reachable (DR)]: Two points are .underline[DR] if there is .red[a chain of DDR points that link] these two points.
- .bold[Border Point]: Point that are DDR but not a core point.
- .bold[Noise] : Points that could not reach to any core point through a chain of DDR points.

]]

---
class: left, middle

### Key concepts

.split-40[.column[
<img src="resources/w07-img/about_reachable.png" width="100%">
].column[
- Let p be a core point, then every point in its Epsilon neighborhood is said to be .red[directly density-reachable] from p.
- A point p is .red[density-reachable] from a core point q if there is a chain of points p, p1, p2, ..., pn, q.
- A point p is .red[density-connected] to a point q if there is a point o such that both, p and q are density-reachable from o.

.bold[Clusters in DBSCAN] are groups of .red[points that are density-connected], meaning that every point within a cluster .red[must be reachable from any other point in the same cluster through a chain of directly density-reachable points], given a specified epsilon (neighborhood radius) and MinPoint (minimum number of points required to form a dense region).
]]


---
class: center, middle

### The cores, borders, and noises

<img src="resources/w07-img/dbscan_type_of_points.png" width="100%">


---
class: center, middle

### The clusters

<img src="resources/w07-img/dbscan_clusters.png" width="100%">

---
class: left, middle

.split-20[.column[
### Choosing MinPoint

How many nearby points to form a 'core'?

].column[
- .bold[Domain knowledge]: If you have an understanding of how dense the clusters should be, use it to set MinPoint accordingly.

- .bold[Sensitivity analysis]: Experiment with various MinPoint values and evaluate the clustering results based on metrics such as the silhouette score, Calinski-Harabasz index, or your own domain-specific criteria.

- .bold[Rule of thumb]: A common rule of thumb (for starting) is to set MinPoint as twice the number of dimensions in your dataset, especially if you don't have any domain knowledge about the expected density.

]]

---
class: left, middle

.split-20[.column[
### Choosing Epsilon
(search radius)

How close is close?

].column[

- .bold[Domain knowledge]: If you have prior knowledge about the scale or density of your data, you can use it to set an appropriate value for ε.

- .bold[k-distance or k-nearest neighbors]: Calculate the k-distance or k-nearest neighbors for various values of k to understand how the local density changes. Choose ε to capture the desired level of density based on these calculations. .underline[(see next page)]

- .bold[Experimentation]: Try different values for ε and observe how the clustering results change. Visualizing the clusters can help you assess their quality.
]]

---
class: left, middle

.split-40[.column[
### Choosing Epsilon
#### k-distance or k-nearest neighbors
].column[
- The idea is that for points in a cluster, their $k$th nearest neighbors are at roughly the same distance.

- Noise points have the kth nearest neighbor at farther distance.

- So, plot sorted distance of every point to its kth nearest neighbor (e.g., $k=4$).
]]

<img src="resources/w07-img/dbscan-demo_knn.png" width="80%">

---
class: center, middle

### A real-life application

<img src="resources/w07-img/clustering_analysis_sample2.jpg" width="80%">

A Modified DBSCAN Clustering Method to Estimate Retail Center Extent. [Pavlis et al. 2017](https://doi.org/10.1111/gean.12138)
