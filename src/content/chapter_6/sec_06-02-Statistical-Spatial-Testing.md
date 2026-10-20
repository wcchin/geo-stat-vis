# Defining Distance and neighborhoods

## Adjacency-based spatial weights
Spatial relationships can be defined using shared borders (rook contiguity). The two figures below show a polygon map and its corresponding neighbour graph.

```{figure} ../resources/original/rook-polygons.svg
:label: rook-six-polygons
:alt: Six labelled synthetic polygons, with unit four inside units one, two and five and units three and six extending to the left.
:align: center

Six synthetic spatial units. Two units are rook neighbours when they share an edge of non-zero length; touching only at a point does not count.
```


```{figure} ../resources/original/rook-neighbour-graph.svg
:label: rook-six-neighbour-graph
:alt: Six nodes labelled one to six joined by the eight shared-edge relationships in the polygon map.
:align: center

The same units represented as a graph. Links connect 1–2, 1–4, 1–5, 2–4, 2–5, 3–5, 3–6 and 4–5. These are exactly the non-zero pairs in the symmetric matrix below.
```

The binary adjacency matrix below represents the same graph. Row and column order is 1–6. A weight of 1 indicates a shared edge; the diagonal is 0 because a unit is not its own neighbour.

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


## Spatial Contiguity
- A regular grid,
- Rook (share edge only)
- bishop (share point only)
- queen (share edge and point)

Higher levels contiguity can be done by adding second, third, etc. outer ring of neighborhoods.


```{figure} ../resources/w08-img/demo_contiguity.png
:label:
:alt:
:align: center

Using the chess concept to define who are the neighbors.
```



### Rook and Queen Contiguity

```{figure} ../resources/w08-img/Rook_vs_Queen_Contiguity.png
:label:
:alt:
:align: center

Top: Based on rook contiguity, the Chong Boon Subzone has 4 neighboring subzones. Bottom: Based on queen contiguity, the same Chong Boon Subzone has 8 neighboring subzones (4 additional).
```

### Higher Order Contiguity

```{figure} ../resources/w08-img/higher_order_Contiguity.png
:label:
:alt:
:align: center

Top: Second level (k=2) contiguity for rook and queen. Bottom: Second level contiguity with lower level ($k \leq 2$).
```


## Distance-based Weights

- a.k.a. distance-band weights

- distance between points (polygon centroids, central points)

- can be any function of distnace that implies **distance decay**, e.g., inverse distance

- in practice, mostly based on a notion of contiguity defined by distance



```{figure} ../resources/w08-img/distance_based_1200m.png
:label:
:alt:
:align: center

Set a distance band (e.g., 2000 m), draw a buffer as a neighborhood, those spatial units (with their centroid) fall within the buffer are considered neighbors, regardless of the spatial contiguity/adjacency.
```


```{figure} ../resources/w08-img/distance_based_differ_size.png
:label:
:alt:
:align: center

When the size of spatial units vary, the same distance band may generate different numbers of neighbors. E.g., for Fort Canning (left), 1200 m (top) and 1500 m (bottom) distance bands can identify 16 and 23 neighbors, respectively; whereas for Holland Road, the same distance bands can find 0 and 1 neighbor.
```


## k-Nearest Neighbor Weights

- k-nearest observations, irrespective of distance
    - fixed isolates problem for distance bands
    - fixed adjacent but not neighbors issue

- have the same number of neighbors for all observations

- in practice, potential problem with
    - ties (observations at the same distance)
    - the area size of neighborhood can vary


```{figure} ../resources/w08-img/knn_example.png
:label:
:alt:
:align: center

Regardless of variation in distance and spatial contiguity, the k-nearest neighbor approach will sort the neigbors by distance, then select the same number of neighbors (k=4 for top and k=12 bottom). The neighborhood area sizes will be different, depending on the area size of the spatial unit and its nearby units.
```


### Row standardization of Spatial Weights

- the basic spatial weight uses 1 to indicate neighbors and 0 for non-neighbors

- locations with more neighbors with have more '1' in the row (more neighbors) will get more total 'influences' by all its neighbors.

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

**See the last two rows**

Row standardization:
- is to rescale weights so that for each row i: $\sum_j w^\prime_{ij}=1$ for each non-isolated row

- $w(i,j)' = \frac{w(i,j)}{\sum_k w(i,k)} $

- makes calculation results comparable
    - all locations will get same level of influence by all their neighbors

    - locations with more neighbors, each of its neighbbors will have less weights of influence to the location, such that the total weight of influence from neighbors is the same with any other location

- can become non-symmetric even when the original neighbour relation is symmetric; rows with no neighbours need explicit handling.

The original spatial weight matrix:

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

Row standardized spatial weight matrix:

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
