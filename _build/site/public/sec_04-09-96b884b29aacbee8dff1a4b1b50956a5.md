# Clustering & Spatial Clustering
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
