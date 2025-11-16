slide_title: Week 07 - Point Pattern III: Spatial Clustering
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

## Point Pattern III: Spatial Clustering
------

<br />

.x-large.bold[Dr. CHIN Wei Chien Benny]  
[.underline.square[wcchin@nus.edu.sg]]  

.headnote.square.bold.x-large[GE5230 Geospatial Statistics and Visualization]
.footnote.square[07 @ 2025-10-02 Department of Geography, NUS]

---
layout: false
class: left, middle

.split-10[.column[].column[
### Two Types Clustering in Spatial Analysis

1. some parts of the study area that have very .red.bold[high concentration of point events],  
i.e., .red['clusters']
    - to check if this phenomenon exists in the spatial point data
    - to identify the location of these clusters
    - significant tests, CSR

2. .red.bold[groups of spatial points] that are close to each other, i.e., .red['clusters']
    - identify grouping of points with/without overlap


In this week, we will focus on the .underline[second 'clustering' analysis].

]]

---
layout: false
class: left, middle
## Objectives of this lecture
- Clustering & spatial clustering
- About k-means clustering
- About DBSCAN
- How to visualize spatial clusters

---
class: center, middle, inverse

.xx-large.bold.wide[PART 1]
## Clustering & Spatial Clustering
------
.square[Clustering .dot[] 2D Space]

.headnote.square.bold.x-large[Point Pattern III]

---
class: left, middle
.split-30[.column[
### What is Clustering
].column[
- .underline[Unsupervised] learning
- Requires data, but .underline[no labels]
    - labelled data is the 'ground truth'
    - supervised learning aim to model the relationship in data (i.e., data-driven) and eventually help to predict, thus need the 'ground truth'. 
- Focus on .underline[detecting patterns] e.g. in
    - Group emails or search results
    - Customer shopping patterns
    - Regions of images
    - Geospatial Point Patterns
- Useful when don’t know what you’re looking for
    - Useful when you're not sure what patterns or groups exist in your data.
- However, you may remain don't know what you're looking at
    - You may still need to interpret and analyze the resulting clusters to understand their meaning and significance.
]]

---
class: center, middle

### Basic idea of clustering: Identifying breeds of dogs

<img src="resources/w07-img/dog_breeds_3.png" width="85%">

Identify dogs that look similar from the photos.

.footnote-left.small[Source: [Solving the mystery of my dog's breed with ML](https://gdmarmerola.github.io/discovering-breed-with-ml/)]

---
class: center, middle

### Basic idea of clustering: Identifying individual pet

<img src="resources/w07-img/ios-17-pets-photos.jpg" width="65%">

Looking for the same person or pet in the photo gallery. 

.footnote-left.small[Image Source: [iOS 17 Photos App Recognizes Your Pets](https://www.macrumors.com/2023/06/06/ios-17-photos-recognizes-pets/)]

---
class: center, middle

### Basic idea of clustering: Group together similar/near instances

<img src="resources/w07-img/demo_clustering_0.png" width="60%">

The data points. 

---
class: center, middle

### Basic idea of clustering: Group together similar/near instances

<img src="resources/w07-img/demo_clustering_1.png" width="60%">

2 big groups. 

---
class: center, middle

### Basic idea of clustering: Group together similar/near instances

<img src="resources/w07-img/demo_clustering_5.png" width="60%">

Another 2 big groups. 

---
class: center, middle

### Basic idea of clustering: Group together similar/near instances

<img src="resources/w07-img/demo_clustering_2.png" width="60%">

Those on the left split into 2 small groups. 

---
class: center, middle

### Basic idea of clustering: Group together similar/near instances

<img src="resources/w07-img/demo_clustering_3.png" width="60%">

Those on the right split into 2 small groups. 


---
class: center, middle

### Basic idea of clustering: Group together similar/near instances

<img src="resources/w07-img/demo_clustering_4.png" width="60%">

4 small groups.

---
class: left, middle

.split-40[.column[
### What could 'similar' or 'near' mean?

The two distances assume the value ranges are equal (similar) among dimensions. (Equal aspect)  
].column[
How to measure similarity/dissimilarity?
- Euclidean distance  
$$d_{a,b} = \sqrt{|x_a-x_b|^2+|y_a-y_b|^2}$$
- Manhattan distance  
$$d_{a,b} = |x_a-x_b|+|y_a-y_b|$$
- Other ways to define 'distance' between data points (instances)
- More than 2 dimensions

.square[The clustering results are .bold[highly dependent] on the similarity metric (or distance measure) chosen to evaluate the proximity between data points within the cluster analysis.]
]]

---
class: left, middle

.split-40[.column[
### What is spatial clustering?
].column[
- .bold[On Spatial Point Patterns]:  
The 2 dimensions are X and Y

- .bold[On Attribute-based Spatial Clustering]:  
The clustering is run on some attributes fields rather than its X & Y locations
]]

---
class: left, middle

.split-20[.column[
### What is spatial clustering?
#### On Spatial Point Patterns

].column[
- .bold[Animal habitats]: Analyze GPS data from animal tracking devices to identify clusters of locations where animals spend most of their time. This can help researchers better understand .red[habitat preferences and territorial behaviors].

- .bold[Activity spaces]: Analyze GPS data from human participants or mobile devices to .red[cluster locations where individuals spend significant amounts of time], such as home, work, or recreational areas. This can help urban planners and researchers understand human movement patterns and inform the design of more efficient and livable urban spaces.

- .bold[Traffic accidents]: Cluster the locations of traffic accidents in a city based on their spatial coordinates to .red[identify accident hotspots]. This information can be used to improve road safety and inform infrastructure planning.

- .bold[Crime hotspots]: Cluster crime incidents based on their geographical locations to identify .red[areas with high concentrations of criminal activity]. This information can be used by law enforcement agencies to allocate resources more effectively, develop targeted crime prevention strategies, and improve public safety.

- .bold[Cell tower coverage]: Group cell towers based on their spatial distribution to determine .red[regions with optimal coverage] and identify areas where additional towers may be needed to improve network performance.
]]

---
class: left, middle

.split-40[.column[
### What is spatial clustering?
#### On Spatial Point Patterns

Using the GPS records of a person moving within a neighborhood to detect clusters (with noises) and identify the place where the participant had visited by follow-up interview and manual checking. 

.footnote-left[[Feng et al. 2024.](https://doi.org/10.1111/tgis.13235)]
].column[

<img src="resources/w07-img/gps_activity_spaces.png" width="100%">

]]

---
class: left, middle

.split-20[.column[
### What is spatial clustering?
#### On Attribute-based Spatial Clustering
].column[
- .bold[Real estate analysis]: Use attributes such as property value, lot size, and property age to cluster homes in a neighborhood. This can help real estate agents and potential buyers identify .red[areas with similar property characteristics].

- .bold[Environmental monitoring]: Cluster air quality monitoring stations based on attributes like pollutant concentrations, temperature, and humidity. This can help identify .red[areas with similar air quality profiles] and inform pollution control strategies.

- .bold[Demographic analysis]: Group census tracts or neighborhoods based on attributes such as population density, age distribution, and income levels to identify .red[areas with similar demographics]. This information can be valuable for urban planning, social services, and targeted marketing.

- .bold[Urban function analysis:] Cluster POIs within a city based on their types (e.g., retail, entertainment, healthcare, education) to identify .red[areas with distinct urban functions and land use patterns]. This can help urban planners and decision-makers better understand the distribution of various amenities and services within the city and inform urban development strategies.

]]

---
class: left, middle

.split-20[.column[
### What is spatial clustering?
#### On Attribute-based Spatial Clustering
The study run clustering on the kernel density of various GPS types and identify clusters with similar density of the different POI types.    
].column[
<img src="resources/w07-img/demo_poi_clusters_1.png" width="100%">
.footnote-right[[Chin et al. 2023](https://doi.org/10.1177/23998083231217376)]
]]

---
class: left, middle

.split-20[.column[
### Types of clustering methods
].column[
.bold[Partitioning]: 
- .red[Central Tendency]: focus on the 'center' of the clusters, e.g., k-means, k-medoids

- .red[Density-based]: focus on the 'density' of the data points, e.g., DBSCAN

.bold[Hierarchical Clustering]
- .red[Agglomerative] (bottom-up): Starts with each point as a separate cluster, then merges pairs of clusters until all points are in a single cluster.

- .red[Divisive] (top-down): Starts with all points in one cluster and recursively splits clusters until each point is in its own cluster.
]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 2]
## k-means clustering
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

---
class: center, middle, inverse

.xx-large.bold.wide[PART 3]
## Density-Based Spatial Clustering of Applications with Noise (DBSCAN)
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


---
class: center, middle, inverse

.xx-large.bold.wide[PART 4]
## Visualizing Spatial Clusters
------

.headnote.square.bold.x-large[Point Pattern III]

---
class: left, middle

.split-50[.column[
### Visualizing Spatial Clusters
].column[

1. point colors
2. convex hull
3. standard ellipse 
4. voronoi polygon
5. Other
    - bubble plot
    - heatmap
    - contour map
]]

---
class: left, middle

.split-50[.column[
### Visualizing Spatial Clusters
1. .red[point colors]
2. convex hull
3. standard ellipse 
4. voronoi polygon
].column[

<img src="resources/w07-img/point_color.png" width="80%">

]]

---
class: left, middle

.split-50[.column[
### Visualizing Spatial Clusters
1. point colors
2. .red[convex hull]
3. standard ellipse 
4. voronoi polygon
].column[

<img src="resources/w07-img/convex_hull.png" width="80%">

]]

---
class: left, middle

.split-50[.column[
### Visualizing Spatial Clusters
1. point colors
2. convex hull
3. .red[standard ellipse] 
4. voronoi polygon
].column[

<img src="resources/w07-img/standard_ellipse.png" width="80%">

]]

---
class: left, middle

.split-50[.column[
### Visualizing Spatial Clusters
1. point colors
2. convex hull
3. standard ellipse 
4. .red[voronoi polygon]
].column[

<img src="resources/w07-img/voronoi_polygon.png" width="80%">

]]

---
class: center, middle, inverse

## Summary
------
.square[Clustering .dot[] k-means .dot[] DBSCAN .dot[] Visualization]

.headnote.square.bold.x-large[Point Pattern III]

---
class: left, middle

.split-20[.column[
### Closing Remarks
].column[

.bold[Spatial Clustering]
- Groups data points based on their location and spatial characteristics.
- Two main types:
    - Spatial Point Patterns (X and Y dimensions)
    - Attribute-based Spatial Clustering

.bold[k-means Clustering]
- Partitions data points into k non-overlapping clusters based on their features.
- Minimizes within-cluster variance and maximizes between-cluster variance.
- Key steps:
    1. Choose k (number of clusters)
    2. Initialize centroids
    3. Assign points to clusters
    4. Update centroids
    5. Repeat until convergence
]]

---
class: left, middle

.split-20[.column[
### Closing Remarks
].column[

.bold[DBSCAN]
- Density-based clustering algorithm that groups points based on their local density.
- Key concepts:
    - Core points: Points with at least MinPts neighbors within ε distance.
    - Density-reachable: Points reachable from a core point through a chain of directly density-reachable points.
    - Density-connected: Points connected through a chain of directly density-reachable points.
- Parameters:
    - MinPts: Minimum number of points required to form a dense region.
    - ε (epsilon): Maximum distance to define the neighborhood.

.bold[Visualization]
- Crucial for understanding clustering results and evaluating cluster quality.
- Methods:
    - Scatter plots with colors
    - Standard ellipse
    - Convex hull
    - Voronoi polygon
    - Other mentioned
]]
