# 5.5 DBSCAN

DBSCAN groups observations through dense neighbourhoods. It does not require the number of groups in advance. Instead, the analyst supplies a neighbourhood distance $\varepsilon$ and a minimum neighbourhood count, commonly called `min_samples` or `minPts`.

The neighbourhood of observation $i$ is

$$N_{\varepsilon}(i)=\{j:d(\mathbf{s}_i,\mathbf{s}_j)\leq\varepsilon\}.$$

In the scikit-learn implementation used here, the observation itself counts towards `min_samples`. A point is a **core point** when its neighbourhood contains at least this many observations. A **border point** is within the neighbourhood of a core point but does not itself meet the core criterion. An observation assigned to neither is labelled **noise** for that parameter setting.

## Density connection, rather than one common centre

Core points connected through chains of neighbouring core points form a cluster. Border points can be attached to such a cluster, but a border point does not propagate a chain by itself. This lets DBSCAN describe shapes that need not be compact around a centroid.

A cluster's total diameter can greatly exceed $\varepsilon$. The parameter limits a neighbourhood step, not the distance between every pair of members. A chain of locally dense observations can connect concentrations that look separate at a broader scale.

Our demonstration keeps `min_samples = 20` and compares neighbourhood distances of 300 m, 600 m and 1,000 m. The count is **20 transactions**, including self, rather than 20 unique blocks. Coincident transactions therefore matter. The figures use Euclidean distance in SVY21 metres.

```{figure} ../datasets/hdb_resale_2026/figures/dbscan.png
:label: ch5-dbscan
:alt: DBSCAN parameter comparison
:align: center

The same upper-group transaction locations under three DBSCAN neighbourhood distances. Grey observations are labelled noise. Colours distinguish clusters within a panel and are not matched between runs; repeated hues may occur where many clusters are present.
```

In this demonstration, increasing ε from 300 m to 600 m reduces the noise count from 603 to 306, while the number of clusters rises from 16 to 18. Additional concentrations can qualify as clusters even as others merge. At 1,000 m there are 11 clusters and 102 noise transactions. The cluster count need not change monotonically as ε increases.

A smaller neighbourhood can leave many observations without sufficient nearby support. A larger neighbourhood can connect dense regions through intervening sales. Changing `min_samples` also changes which observations qualify as core points. There is no parameter-free answer hidden behind these maps.

## What a noise label does and does not mean

Noise is an algorithmic label. It does not mean an erroneous transaction, a low-quality geocode or an economically unimportant place. An isolated high-price sale can be a valid observation that does not belong to a dense group under the chosen settings.

Some border observations can be reachable from core points in more than one cluster. Their assignment can depend on processing order, even when the core structure is unchanged. This is another reason to avoid treating a coloured boundary as a uniquely determined geographical division.

A nearest-neighbour distance plot can help identify candidate distance scales. It does not establish a universally correct threshold, especially where the point density varies strongly across the city. Report a small, interpretable range of settings and examine which conclusions persist. Do not choose settings solely because the resulting map looks persuasive.

## Repeated blocks and the meaning of density

A block with many upper-group transactions can help create a dense neighbourhood even when there are few distinct block positions. That is appropriate for a transaction-volume question. For a question about geographical coverage across blocks, it may be preferable to deduplicate positions and reinterpret the minimum count as blocks. If repeated positions are aggregated for computational efficiency, positive sample weights can preserve transaction counts, provided the implementation's weighting rules are understood.

**Interpretation task:** Describe one change between two panels without calling either result “correct”. Specify the parameter change, the resulting membership change and the limitation of the interpretation.

**Self-check:** Why is DBSCAN noise not a data-quality label?

```{dropdown} Feedback
A valid sale can lack enough nearby observations for the chosen distance and count. Different parameters can change its classification.
```

## Further reading

Ester, M., Kriegel, H.-P., Sander, J., and Xu, X. (1996). [A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise](https://aaai.org/papers/kdd96-037-a-density-based-algorithm-for-discovering-clusters-in-large-spatial-databases-with-noise/). *Proceedings of KDD-96*, 226–231. Read for density reachability and connectivity, then compare the definitions with this page’s core, border and noise examples.
