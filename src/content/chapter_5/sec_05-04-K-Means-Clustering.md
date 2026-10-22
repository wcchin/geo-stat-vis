# 5.4 K-means clustering

K-means partitions observations into a chosen number $k$ of groups. Each group has a centre, or centroid, and observations are assigned to reduce the total squared distance from their group centres.

For groups $C_1,\ldots,C_k$ and their centroids $\boldsymbol{\mu}_j$, the objective is

$$J=\sum_{j=1}^{k}\sum_{i\in C_j}\left\|\mathbf{s}_i-\boldsymbol{\mu}_j\right\|^2.$$

For fixed memberships, a centroid is the arithmetic mean of the member coordinates. It need not coincide with a transaction or even an inhabited place. Repeated block coordinates count repeatedly, so a block with more selected transactions exerts greater influence.

## How the algorithm improves a partition

Starting from initial centres, the algorithm assigns each observation to its nearest centre. It then recomputes each centre as the mean of its assigned observations. These two steps repeat until the stopping rule is met. Each step does not increase the objective, but different starting centres can lead to different local solutions.

Our demonstration uses the 1,353 upper-group transactions, a fixed random seed of 5230 and 20 initialisations. It compares $k=3$ with $k=5$. These are teaching choices, not a claim that Singapore contains three or five distinct upper-price housing markets.

```{figure} ../datasets/hdb_resale_2026/figures/kmeans.png
:label: ch5-kmeans
:alt: K-means comparison
:align: center

Spatial k-means partitions of the same upper-group transactions. Crosses show centroids. Cluster colours identify membership and have no high-to-low ordering. All transactions are assigned in both runs.
```

The broad difference between the maps follows from the question imposed on the method. With three centres, a group can span several concentrations. With five centres, some of those concentrations receive separate centres. Every observation is assigned even if it is isolated or far from a centre. A partition is therefore not evidence that all the resulting groups are dense concentrations.

## What changes when k changes?

The best achievable sum of squared distances cannot increase as additional centres are allowed. A smaller objective at a larger $k$ is therefore expected and is insufficient evidence for that choice. An elbow plot or silhouette score can support exploration, but neither replaces an explanation of why the grouping is useful for the geographical question.

K-means favours compact groups under the chosen distance. It can split an elongated concentration or divide nearby features in ways that reflect the centroid objective rather than their connectivity. Euclidean distance also ignores coastlines, barriers and transport networks. A nearest-centre partition should not be interpreted as an accessibility catchment without an appropriate travel-distance model.

The numerical labels are arbitrary. “Cluster 0” in one run is not necessarily the same geographical group as “Cluster 0” in another. Compare memberships and positions rather than label numbers.

**Interpretation task:** Find a group that spans a visible gap between observed sales. Why can this happen under the k-means objective? Would drawing a filled polygon around that group make its apparent continuity more convincing than the observations warrant?

**Self-check:** Why can a k-means group span a gap?

```{dropdown} Feedback
K-means assigns every observation to a centre to reduce squared distance. It does not require a chain of densely occupied neighbourhoods.
```

## Further reading

MacQueen, J. (1967). [Some Methods for Classification and Analysis of Multivariate Observations](https://digicoll.lib.berkeley.edu/record/113015). In *Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability*, Vol. 1, 281–297. Read for the k-means grouping idea; distinguish the original procedure from the batch assignment/update algorithm demonstrated here.
