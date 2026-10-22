# 5.3 Clustering and spatial clustering

KDE assigns a continuous value to each evaluation location. Clustering instead assigns observations to groups, according to a specified definition of similarity or connection. This can help describe the data, organise a large collection of observations or identify candidate areas for further investigation.

A group is an output of a method and its settings. Calling it a cluster does not establish that it is statistically unusual under a null model. The distinction is especially important when an algorithm is designed to return groups even for data without an obvious cluster structure.

## Define the space in which similarity is measured

A dataset can support several legitimate clustering questions. Clustering geographical coordinates groups nearby positions. Clustering prices, floor areas and remaining leases groups transactions with similar attributes, even if they are far apart. Combining coordinates with attributes creates a third question and requires a deliberate choice of relative scales.

Suppose one feature is distance in metres and another is price in dollars. Adding their squared differences directly makes the numerical units part of the answer. Standardisation can change that balance, but it does not decide the appropriate geographical trade-off for us. A one-standard-deviation difference in price is not inherently equivalent to a one-standard-deviation difference in location.

For this chapter, the main clustering examples use **upper-group transaction locations only**, with Euclidean distance in projected metres. The price threshold defines the subset. It is not an additional numerical clustering feature.

## Decide what an observation represents

Repeated block positions are part of the transaction pattern. Retaining them asks where the transactions are grouped, and gives blocks with several selected sales more influence. Collapsing to one observation per block asks where selling blocks are grouped. Both can be useful, but they are not equivalent.

We retain transactions in the main examples and do not jitter coincident locations. For plotting, an overlapping marker may represent several transactions. For algorithmic neighbourhood counts or centroids, each retained transaction still contributes. A useful sensitivity analysis would repeat the method with one observation per block and state the changed unit of analysis.

## Match the method to the question

| Method | What the analyst chooses | What the method returns | A key limitation |
|---|---|---|---|
| KDE | Kernel and bandwidth | A continuous smoothed surface | No group membership or significance test |
| k-means | Number of groups and feature space | A partition of all observations | Groups appear even without strong cluster structure |
| DBSCAN | Neighbourhood distance and minimum count | Density-connected groups and noise labels | One parameter set may poorly represent varying densities |

K-means is useful for understanding partitioning around centres. DBSCAN is useful for exploring concentrations connected through sufficiently dense neighbourhoods. Neither method automatically adjusts for the geography of housing opportunities, nor does either compare upper-price labels with all observed sales.

For an inferential question about price labels, a possible later analysis would hold selling locations fixed and permute the marks. That random-labelling null requires a defensible exchangeability assumption. Differences in lease, size and housing characteristics may make unrestricted relabelling too simplistic. This chapter first establishes what the descriptive methods do, so that a later inferential question can be stated clearly.

**Before running an algorithm:** Write one sentence specifying the observation, the features, the distance and the purpose of the grouping.

```{dropdown} Self-check feedback: What changes when repeated block positions are collapsed?
The observation becomes a selling block rather than a transaction. Neighbourhood counts and the influence of heavily selling blocks change.
```
