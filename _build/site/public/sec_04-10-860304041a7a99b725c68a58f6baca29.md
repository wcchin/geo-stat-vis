# k-means clustering
------
.square[Steps .dot[] The k .dot[] Applications ]

.headnote.square.bold.x-large[Point Pattern III]

---
class: left, middle

.split-30[.column[
### What is k-means Clustering?
].column[

.bold[Definition]:
k-means is an unsupervised machine learning algorithm used for clustering data points into .red[k distinct, non-overlapping groups] based on their similarities and differences.

.bold[Objective]:
The main goal of k-means is to minimize the within-cluster sum of squares (WCSS), which represents the .red[total squared distance (euclidean distance) between data points and their nearest cluster centroid].
]]

---
class: left, middle

.split-30[.column[
### k-means Clustering Steps & Process
].column[
- .bold[Choose k]: Select the number of clusters (k) to generate.

- .bold[Initialize centroids]: Randomly select k initial centroids from the dataset or use other initialization methods like k-means++.

- .bold[Assign points to clusters]: Assign each data point to the cluster with the nearest centroid.

- .bold[Update centroids]: Recalculate the centroid positions by taking the mean of all data points belonging to each cluster.

- .bold[Repeat]: Repeat steps 3 and 4 until convergence, i.e., no further changes in cluster assignments or centroid positions occur.
]]

---
class: left, middle

.split-30[.column[
### k-means Clustering Steps & Process

.red.bold[The data point]

].column[
<img src="resources/w07-img/kmeans-step_0.png" width="100%">
]]

---
class: left, middle

.split-30[.column[
### k-means Clustering Steps & Process

.red.bold[The Steps]
- Initialize with random centroids
- Get the nearest neighbors, and calculate the new mean centers
- Move the centers to the mean centers

].column[
<img src="resources/w07-img/kmeans-step_1.png" width="100%">
]]

---
class: left, middle

.split-30[.column[
### k-means Clustering Steps & Process

.red.bold[The Steps]
- Re-calculate distance and find nearest neighbors
- Re-Calculate new mean centers and move

].column[
<img src="resources/w07-img/kmeans-step_2.png" width="100%">
]]

---
class: left, middle

.split-30[.column[
### k-means Clustering Steps & Process

.red.bold[The Steps]
- The location of new and previous centers overlapped. Hence, stops.

].column[
<img src="resources/w07-img/kmeans-step_3.png" width="100%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_0.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_1.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_2.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

.xkcd[Note how the blue mean center moved.]

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_3.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_4.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_5.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_6.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_7.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_8.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_9.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_10.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_11.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_12.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_13.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_14.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_15.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_16.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### k-means Clustering: Example with 7 clusters

.xkcd[There is a cluster divided into two clusters, and two (at the bottom right) clusters merged as one. ]

].column[
<img src="resources/w07-img/kmeans_demo_7/kmeans_7-step_17.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### Parameters and Initialization
].column[
- How do we know the number of clusters (i.e., the k in k-means)?
- How to initialize mean centers' locations?
]]

---
class: left, middle

.split-30[.column[
### How to select k

<img src="resources/w07-img/DataClustering_ElbowCriterion.JPG" width="90%">
.square[[Wikipedia](https://en.wikipedia.org/wiki/File:DataClustering_ElbowCriterion.JPG)]
].column[

.bold[Elbow Method]: Plot the explained variation (or distortion) as a function of the number of clusters, and choose the elbow point as the number of clusters to use. The elbow point is the point of diminishing returns, where the additional gain in reducing the distortion starts to decrease significantly as more clusters are added. For the final iteration (i), the explained variation (EV^i) can be calculated by the distance between each point (k) and the cluster they were assigned (C_j^i).

$$D_{j}^i = \sum (|x_k - \mu_j^i|^2)$$

where ${x_{k} \in C_j^i}$

$$D^i = ∑_{j=1}^k D_j^i$$

$$EV^i = D^0 - D^i$$

]]

---
class: left, middle

.split-30[.column[
### How to select k

.bold[Silhouette Analysis]: Calculate the average silhouette score ($Si$) for different values of k and choose the value that yields the highest score. The silhouette score measures the cohesiveness of datapoints within a cluster compared to their closeness to datapoints in other clusters, with values closer to 1 indicating well-defined clusters.

].column[


$$Si = (b_i - a_i) / \text{max}(a_i, b_i)$$

$a_i$ is the average distance between point i and all other points in its own cluster:

$$a_i = \sum \frac{(d(x_i, x_j))}{|C_i|}$$

where, $x_j ∈ C_i$

$b_i$ is the lowest average distance between point i and all points in any other cluster:

$$b_i = \text{min} ∑ \frac{(d(x_i, x_j))}{|C_j|}$$

where, $x_j ∈ C_j$ and $j\neq i$

Note that the Silhouette Coefficient ranges between -1 and 1, with higher values indicating better clustering.

]]

---
class: left, middle

.split-30[.column[
### How to select k

.bold[Silhouette Analysis]

].column[

<img src="resources/w07-img/Silhouette-plot-orange.png" width="70%">

[Wikipedia](https://commons.wikimedia.org/wiki/File:Silhouette-plot-orange.png)

]]

---
class: left, middle

.split-30[.column[
### How to select k
].column[

- [.bold[Gap Statistic]](https://en.wikipedia.org/wiki/Determining_the_number_of_clusters_in_a_data_set#The_gap_statistics): Compare the total within-cluster variation for different values of k and choose the value that maximizes the gap statistic, which is the difference between the observed and expected within-cluster variation.

- .bold[Domain Knowledge]: Rely on your knowledge of the dataset and the problem domain to choose a value for k that makes sense in the context of your analysis.
]]

---
class: left, middle

.split-30[.column[
### How set the initial position of the mean centers?
].column[
- .bold[Random Initialization]: Randomly select k points from the dataset to serve as the initial centers. This method is simple but may lead to suboptimal clusters due to its unpredictability.

- .bold[k-means++]: Choose the first center randomly from the dataset. Then, for each subsequent center, choose a point from the dataset with a probability proportional to its squared distance from the nearest existing center. This method tends to provide better clustering results than random initialization.

- .bold[Furthest Point]: Calculate the distances between all pairs of points in the dataset, then choose the two points with the largest distance as the first two centers. For each subsequent center, select the point that maximizes the minimum distance to the previously chosen centers.
]]

---
class: left, middle

.split-40[.column[
### Properties of k-means clustering
].column[
- Guaranteed to	converge in a finite number of iterations.

- Running time per iteration:
    - assign data points to closest cluster center: O(KN) time
    - change the cluster center to average of its assigned points: O(N)

- Sensitive to outliers since an object with an extremely large value may substantially move a center.
]]
