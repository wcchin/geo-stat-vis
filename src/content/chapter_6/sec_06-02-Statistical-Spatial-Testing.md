---
label: distance-and-neighbourhoods
---

# Defining Distance and Neighbourhoods

## Neighbours are part of the question

The income maps in [Section 6.1](sec_06-01-Spatial-Autocorrelation.md) invite us to compare nearby areas. But a shared border, a short straight-line distance and a short journey describe different relationships. A weights specification makes that choice explicit before we calculate spatial association.

After reading, you should be able to translate a neighbour rule into a matrix, distinguish contiguity, distance-band and k-nearest-neighbour weights, calculate a spatial lag, and explain row standardisation and graph diagnostics. We use nonnegative weights and exclude self-neighbours unless a later statistic explicitly states otherwise.

## From polygons to a neighbour graph

**Rook contiguity** connects polygons sharing a boundary segment of positive length. **Queen contiguity** also permits contact at a point. On a regular square grid these resemble chess moves: an interior cell has four first-order rook neighbours or eight first-order queen neighbours. Queen includes rook contacts; it does not require every neighbour to share both an edge and a corner.

```{figure} ../resources/original/rook-polygons.svg
:label: rook-six-polygons
:alt: Six labelled synthetic polygons illustrating shared-edge contiguity.
:align: center

Six synthetic units. Rook neighbours share an edge of non-zero length; point contact alone is insufficient. These are teaching geometries, not Malaysian administrative boundaries.
```

```{figure} ../resources/original/rook-neighbour-graph.svg
:label: rook-six-neighbour-graph
:alt: Six nodes joined by eight undirected shared-edge relationships.
:align: center

The same units as a graph. Links are 1–2, 1–4, 1–5, 2–4, 2–5, 3–5, 3–6 and 4–5. The graph preserves the selected relationships, not polygon shape or area.
```

Let $a_{ij}=1$ when $j$ is a selected neighbour of $i$, and zero otherwise. With row and column order 1–6,

$$
A=\begin{bmatrix}
0&1&0&1&1&0\\
1&0&0&1&1&0\\
0&0&0&0&1&1\\
1&1&0&0&1&0\\
1&1&1&1&0&0\\
0&0&1&0&0&0
\end{bmatrix}.
$$

The diagonal is zero. The matrix is symmetric because shared-edge contact is mutual. Unit 5 has four neighbours; unit 6 has only one. There are eight undirected links but sixteen nonzero matrix entries: each link appears in both directions. Preserve that convention in later sums over $i$ and $j$.

### Higher-order neighbours

Graph distance counts the minimum number of links needed to reach another unit. Exactly second-order neighbours are two links away, excluding first-order neighbours and the focal unit. A cumulative neighbourhood up to order two includes first- and second-order neighbours. State which version is used.

For unit 6, the first-order neighbour is 3 and the exactly second-order neighbour is 5. The cumulative set through order two is therefore {3, 5}. Matrix powers count walks and can include repeated routes and returns to the focal unit; they are not automatically the desired binary higher-order neighbourhood.

### Topology is not a display detail

Small gaps, overlaps or generalised coastlines can create missing or spurious contacts. Use geometries suitable for the analysis and inspect the graph. The Peninsular Malaysia income maps use generalised display outlines; those outlines should not be used to infer exact shared-border adjacency. Island units also require an explicit decision: lack of land contact need not imply lack of a meaningful geographical connection.

## Distance-based relationships

A **binary distance band** connects observations whose representative locations are within a threshold $d_0$:

$$
a_{ij}=\mathbf{1}(0<d_{ij}\leq d_0),\qquad i\ne j.
$$

This expression assumes distinct representative coordinates. Coincident locations require a separate rule, rather than silently excluding a pair because its distance is zero. For polygon data, specify whether distance is between centroids, interior points, population centres or another representation. A geometric centroid may fall outside an irregular polygon and does not necessarily represent where people live.

A fixed distance band has a consistent distance threshold but can produce very different neighbour counts in dense and sparse regions. It may leave some units without neighbours. Straight-line distance also need not represent travel or environmental connectivity across barriers.

Distance-based weights need not be binary. For distinct locations, one option is inverse-distance weighting within a stated cutoff:

$$
b_{ij}=d_{ij}^{-\alpha}\mathbf{1}(d_{ij}\leq d_0),
\qquad i\ne j,\quad \alpha>0.
$$

Set $b_{ii}=0$ and define how coincident points are handled before using this expression. A larger exponent gives nearer neighbours greater relative weight. A distance band selects who contributes; a decay function additionally determines how contribution varies with distance. They are separate choices.

Use projected metric coordinates suitable for the region, or a documented geodesic calculation. A threshold in metres cannot be applied directly to unprojected longitude and latitude as if degrees were metres. For a road-travel question, a network travel-time relationship may be more appropriate than Euclidean distance.

## k-nearest-neighbour weights

A **k-nearest-neighbour (kNN)** rule selects the $k$ closest other observations for each focal unit. With enough observations and an explicit tie rule, each row has $k$ outgoing neighbours, but the distance to the furthest selected neighbour varies.

Consider four synthetic points on a line at 0, 1, 3 and 10 km. With $k=1$, their directed selections are A→B, B→A, C→B and D→C. C selects B, but B does not select C. Thus kNN weights need not be symmetric even though the underlying distance is symmetric. The selected distance ranges from 1 km to 7 km in this example.

Choosing $k\geq1$ avoids empty outgoing neighbour sets, but does not guarantee that the entire graph is connected. Separate groups can select neighbours only within themselves. Equal-distance ties and coincident coordinates need documented handling; arbitrary coordinate jitter changes the geometry and should not be an unexplained default.

If a symmetric relation is required, distinguish the **union rule** (connect a pair if either selects the other) from the **mutual rule** (connect only if both select each other). Symmetrising changes neighbour counts, and a mutual rule can create isolates. [libpysal's KNN documentation](https://pysal.org/libpysal/stable/generated/libpysal.weights.KNN.html) describes its implementation and tie handling.

## Row standardisation changes the summary

The neighbour relation and its numerical transformation are distinct. Starting with binary adjacency, define $k_i=\sum_j a_{ij}$. For a non-isolated row,

$$
w_{ij}=\frac{a_{ij}}{k_i},\qquad \sum_jw_{ij}=1.
$$

For general nonnegative weights, divide by the row's positive weight sum instead. The transformed weights specify relative contribution to the focal unit's neighbour summary. They do not demonstrate influence or causation.

In the six-unit example, row 5 assigns weight $1/4$ to each neighbour; row 6 assigns weight 1 to unit 3. Every nonempty row has total weight one, but each neighbour's contribution differs. Standardisation changes a neighbour sum into an average; it does not make all geographical specifications or statistical results universally comparable.

Even a symmetric binary graph can become numerically asymmetric. Units 3 and 5 are mutual neighbours, but $w_{35}=1/2$ while $w_{53}=1/4$. Distinguish asymmetry in whether a link exists from asymmetry in its transformed weight.

Let $S_0=\sum_i\sum_jw_{ij}$. For the binary matrix above, $S_0=16$. With all six rows standardised, $S_0=6$. The identity $S_0=n$ requires every included row to sum to one; do not apply it without checking isolates.

## A worked spatial lag

A **spatial lag** is the weighted neighbour summary

$$
(W\mathbf{x})_i=\sum_jw_{ij}x_j.
$$

For binary weights it is a sum; after row standardisation it is the mean of the selected neighbours. More generally, nonnegative weights summing to one give a weighted mean. The focal value is excluded when $w_{ii}=0$.

Assign the six synthetic units values $\mathbf{x}=(2,4,6,8,10,12)$:

| Unit | Neighbours | Binary lag: neighbour sum | Row-standardised lag: neighbour mean |
| --- | --- | ---: | ---: |
| 1 | 2, 4, 5 | 22 | $22/3$ |
| 2 | 1, 4, 5 | 20 | $20/3$ |
| 3 | 5, 6 | 22 | 11 |
| 4 | 1, 2, 5 | 16 | $16/3$ |
| 5 | 1, 2, 3, 4 | 20 | 5 |
| 6 | 3 | 6 | 6 |

Unit 5 has value 10 but neighbour mean 5. Unit 6 has value 12 but neighbour mean 6. A lag can differ substantially from the focal value and can hide disagreement among neighbours: a mean of 5 need not describe any individual neighbour.

For a mean-centred vector $\mathbf{d}=\mathbf{x}-\bar{x}\mathbf{1}$, the corresponding lag is $W\mathbf{d}$. With nonempty row-standardised weights, $W\mathbf{d}=W\mathbf{x}-\bar{x}\mathbf{1}$. In this example $\bar{x}=7$, so unit 5 has deviation 3 and neighbour deviation lag $5-7=-2$. Their product is negative, a contrast contributing to Moran's numerator. This is descriptive, not a local significance test.

A spatial lag is not a fitted prediction and does not establish that neighbouring values cause the focal value. [Section 6.3](sec_06-03-Morans-I.md) uses these products to construct the global statistic and its reference comparison.

## Diagnose the graph before calculating the statistic

An **isolate** has no selected neighbours. A **disconnected graph** contains components with no links between them, even if no unit is isolated. Record both. An empty row cannot be standardised by division; representing its lag as zero is a software convention, not an observed neighbour average of zero.

Possible responses include revisiting a justified threshold, using a substantively suitable alternative relation, or reporting an explicit exclusion and its effect on the study population. Do not add arbitrary links solely to obtain a preferred coefficient. A graph across islands, mountain barriers or disconnected land masks deserves geographical inspection.

Match matrix row/column identifiers to table and geometry identifiers. Reordering a table without reordering its matrix assigns values to the wrong units. After dropping missing observations, reconstruct or correctly subset and restandardise the weights as required; neighbour counts can change.

For the Sumatra grid, rook contiguity links shared cell edges and queen also links corners. Masks can remove a cell and sever a connection. For Malaysian districts, geometry quality and islands raise different issues. Neither specification automatically represents fire spread, commuting or income transmission.

## Choose and report a defensible specification

| Rule | Held consistent by construction | Main issue to inspect |
| --- | --- | --- |
| Rook/queen | A boundary-contact criterion | Topology, islands and unequal unit sizes |
| Distance band | A distance threshold | Isolates, variable neighbour counts and representative points |
| kNN | Outgoing neighbour count before symmetrisation | Long links, ties, asymmetry and separate components |
| Distance decay | A stated weighting function | Cutoff, exponent, distance units and coincident points |

Report the spatial support, geometry/coordinate system, neighbour rule and parameters, self-weight convention, transformation, isolates, components and data ordering. Compare a small set of justified alternatives while keeping other inputs fixed. A sensitivity result should explain how the question changes, rather than select the weights yielding the smallest p-value.

## Check your reasoning

```{dropdown} 1. Can queen neighbours share only an edge?
Yes. Queen includes shared-edge and point-contact relationships; rook requires an edge.
```

```{dropdown} 2. Does kNN guarantee one connected graph?
No. Each observation can have outgoing neighbours while separate groups remain disconnected. Directed selections can also be asymmetric.
```

```{dropdown} 3. Must row-standardised weights remain symmetric?
No. Mutual neighbours with different neighbour counts receive different reciprocal weights. The underlying relation can still be symmetric.
```

```{dropdown} 4. What is unit 5's lag, and does it include its own value of 10?
The binary lag is 20 and the row-standardised lag is 5. Its own value is excluded. The difference reflects the transformation, not a change in observations.
```

```{dropdown} 5. Is a zero lag for an isolate the same as having neighbours whose values average to zero?
No. The isolate has no neighbour information under that rule. A stored zero is a computational convention requiring explicit handling.
```

## Read further and continue

- **Published methods reading:** Anselin, L. (2002). [Under the hood: Issues in the specification and interpretation of spatial regression models](https://doi.org/10.1111/j.1574-0862.2002.tb00120.x). *Agricultural Economics*, 27, 247–267. Read the discussion of spatial weights as a model specification; regression details extend beyond this chapter.
- **Contiguity:** [GeoDa Workbook: Contiguity-Based Spatial Weights](https://geodacenter.github.io/workbook/4a_contig_weights/lab4a.html). Examine graph diagnostics and higher-order definitions.
- **Distance:** [GeoDa Workbook: Distance-Band Spatial Weights](https://geodacenter.github.io/workbook/4b_dist_weights/lab4b.html). Compare distance thresholds and nearest-neighbour rules.
- **Calculation:** [libpysal: lag_spatial](https://pysal.org/libpysal/stable/generated/libpysal.weights.lag_spatial.html) documents how the weights transformation affects the lag.

**Next:** [Moran's I](sec_06-03-Morans-I.md): combine focal deviations with their spatial lags, normalise the sum, and assess it against a fixed-weights permutation reference.
