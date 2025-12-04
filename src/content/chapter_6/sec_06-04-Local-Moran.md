# LISA and Local Moran's I

## What is LISA

LISA, which stands for Local Indicators of Spatial Association, is a set of statistical measures used in spatial data analysis to identify and assess local patterns of spatial autocorrelation. LISA helps detect areas with significant concentrations or disparities of a given variable, such as regions with high crime rates, low-income neighborhoods, or areas with a high prevalence of a particular disease.

LISA encompasses various types of measures, including **Local Moran's I, Local Geary's C, Gi, and Gi***. These measures build upon the concept of global spatial autocorrelation, measured by Moran's I (for Local Moran), Geary's C (for local Geary C), by providing location-specific insights into spatial structures, mainly on spatial clustering (hot-spots, cold-spots) and spatial outliers (neighboring with the opposite type).

By analyzing the spatial patterns and local clustering of a given variable through the different LISA measures, researchers can gain valuable insights for urban planning, public health, environmental studies, criminology, and other fields where spatial relationships and interactions play a crucial role.


## LISA form of global spatial autocorrelation

- Decomposable statistics

- $\text{global} = a . [\sum_i \text{component}(i)]$

- then $\text{local}(i) = \text{component}(i)$



## What is Local Moran's

Local Moran's I is a measure of spatial autocorrelation used in geography and geographic information science (GIS) to assess the degree of spatial clustering or dispersion of a given variable around a specific location. Developed by Anselin (1995), it is a local version of the global Moran's I statistic, which measures the overall spatial autocorrelation in a dataset.

Local Moran's I helps identify the extent of significant spatial clustering of similar values around a specific observation. It calculates the correlation between a value at a given location and the values at neighboring locations, highlighting areas with high or low concentrations of the variable under study. This information can be useful in various applications, such as identifying crime hotspots, determining areas with higher disease prevalence, or understanding income disparities across a region.

Essentially, Local Moran's I provides a way to evaluate spatial patterns and relationships between values at specific locations and their surroundings, offering insights into the spatial structure of the data.


## The target of Local Moran

The target of Local Moran is to identify two types of locations with statistical significance (through permutation):
- **Clusters**: locations with significantly similar values (hot-spots & cold-spots)
- **Outliers**: locations with significantly different values.
- Places with very similar but not far from the means are ignored (as non-significant).

**Clusters**: To identify locations with _positive_ correlation:
- High-High (HH) clusters: _high_ value locations surrounded by _high_ value neighbors
- Low-Low (LL) clusters: _low_ value locations surrounded by _low_ value neighbors

**Outliers**: To identify locations with _negative_ correlation:
- High-Low (HL) outliers: _high_ value locations surrounded by _low_ value neighbors
- Low-High (LH) outliers: _low_ value locations surrounded by _high_ value neighbors



## Global Moran's I: Formula

The lower part (denominator) is a kind of standardizig process to control the range of the resulting values.

$$
\text{I}=\frac{N}{W} \times \frac{\sum_i^N \sum_j^N w_{i,j}(x_i-\bar{x})(x_j-\bar{x})}{\sum_k (x_k-\bar{x})^2}
$$

Where:
- $N$ is the number of spatial units indexed by $i$ and $j$;
- $x$ is the variable of interest;
- $\bar{x}$ is the mean of $x$;
- $w_{i,j}$ is the spatial weight---kind of an indicator variable, equal to 1 or the row-standardized value if $i$ and $j$ are neighbors, 0 otherwise;
- W is the sum of all $w_{i,j}$.

Let's $z_i = x_i - \bar{x}$ (i.e., deviations from mean), then

$$
\text{I} = \frac{\sum_i \sum_j w_{i,j} \times z_i \times z_j}{\sum_k z_k^2}
$$


## Local Moran's I: Formula
The lower part (denominator, $\sum_k z_k^2$) is a kind of standardizig process to control the range of the resulting values.

$$
\text{I} = \frac{\sum_i \sum_j w_{i,j} \times z_i \times z_j}{\sum_k z_k^2}
$$

rearrange...

$$
\text{I} = \frac{1}{\sum_k z_k^2} \times [\sum_i z_i \sum_j w_{i,j} \times z_j]
$$

$\sum_k z_k^2$ will not change with $i$, thus constant and this could be captured by the form of:

- $\text{global} = a . [\sum_i \text{component}(i)]$

$$
\text{Local I}_i = \frac{1}{\sum_k z_k^2} \times z_i \sum_j w_{i,j} \times z_j
$$


## Technical aspects of Local Moran('s I)
The first part ($1 / \sum_k z_k^2$ or $N / \sum_k z_k^2$) is a kind of standardizig process to control the range of the resulting values.

- for row-standardized weights
(such that $S_0$ and $N$ cancel out in Moran's I)

- variables as deviations from mean ($z_i = x_i - \bar{x}$, positive means greater than mean, and negative means less than mean).

$$
\text{Local I}_i = \frac{1}{\sum_k z_k^2} \times z_i \sum_j w_{i,j} \times z_j
$$

- $z_i$ is the deviation from mean for the current location
- $\sum_j w_{i,j} \times z_j$ is the 'lag' term, how high or low is the (location $i$'s) neighbors'  overall value compared to the mean

- for non-row-standardised
$$
\text{Local I}_i = \frac{N}{\sum_k z_k^2} \times z_i \sum_j w_{i,j} \times z_j
$$
take note on the $N$...


## Link Local - Global: LISA

take note on the $N$:
$$
\sum_i \text{Local I}_i = \sum_i \frac{N}{\sum_k z_k^2} \times z_i \sum_j w_{i,j} \times z_j
$$

$$
\sum_i \text{Local I}_i = N \times \frac{1}{\sum_k z_k^2} \times \sum_i z_i \sum_j w_{i,j} \times z_j
$$

$$
\sum_i \text{Local I}_i = N \times \text{Global I}
$$

- $\sum_i \text{local}_i = N . \text{global}$

- or $\text{global} = \frac{\sum_i \text{local}_i}{N}$

- the global statistics is the average of local statistics


## Statistical Inference

- analytical and computational

- analytical approximation is poor (do not use)

- computational approach is based on **conditional permutation**

## Conditional Permutation

- Conditional upon value observed at location $i$

- hold value at i fixed, random permute remaining n-1 values and recompute local Moran's I
    - since $w_{i,j}$ leave non-neighbors to be 0, this is same as randomly pick J number of value (without replacement), J is the number of neighbors, then locate these J values on each neighbor for the local Moran calculation.

- repeat many times (e.g., 999) to obtain reference distribution for location i, compare and calculate pseudo p-value

- computationally intensive:
    - if there is N size of entity (row), and the permutation is set to 1000, then the calculation takes N * 1000.


## Interpretation
### Local Significance Map

- shows locations with significant local statistic by level of significance.

- not very useful for substantive interpretation

- useful for observation of the confidence level

- diagnostic for sensitivity of results (for example, when only significant at 0.05 but not at 0.001).


#### An example
Take an example: the donations data (Guerry data)


```{figure} ../resources/w09-img/guerry_data.png
:label:
:alt:
:align: center

The data distribution (based on Natural Breaks).
```


```{figure} ../resources/w09-img/guerry_significant_map.png
:label:
:alt:
:align: center

The Local Significance Map
```


### The Local Cluster Map

- shows locations with **significant** local spatial autocorrelation by **type of association**

- four types (four colours):
    - HH clusters
    - LL clusters
    - HL outliers
    - LH outliers

- shown only for a specified significance level (sensitivity analysis)

- **but the Local Moran can only be used to identify positive or negative correlation, i.e., clusters or outliers, how to differentiate the HH from LL and HL from LH?**


```{figure} ../resources/w09-img/guerry_significant_map_scatter.png
:label:
:alt:
:align: center

Use the quadrants: For those significant (the map on the right), check the position of the spatial unit in the scatter plot: on top right indicates HH, bottom left LL.
```


```{figure} ../resources/w09-img/guerry_I_cluster_map.png
:label:
:alt:
:align: center

The Local Cluster Map
```


### Sensitivity Analysis Using The Local Cluster Map

Through the changes of significance level, we can observe the changes of clusters/outliers and identify those that is more significant.

```{figure} ../resources/w09-img/guerry_I_cluster_map_sensitivity.png
:label:
:alt:
:align: center

Top: p-value < 0.05; bottom: p-value < 0.01
```


### The Local Outliers

```{figure} ../resources/w09-img/guerry_local_outliers_HL.png
:label:
:alt:
:align: center

The locations of HL outliers and their neighbors.
```



```{figure} ../resources/w09-img/guerry_local_outliers_LH.png
:label:
:alt:
:align: center

The locations of LH outliers and their neighbors.
```


### The Local Hot-spots

```{figure} ../resources/w09-img/guerry_local_cluster_HH.png
:label:
:alt:
:align: center

The locations of HH clusters and their neighbors.
```


### The Local Cold-spots

```{figure} ../resources/w09-img/guerry_local_cluster_LL.png
:label:
:alt:
:align: center

The locations of LL clusters and their neighbors.
```


## Overview

Local Moran's I is a local measure of spatial autocorrelation used in spatial data analysis. It assesses the degree of spatial clustering or dispersion around individual locations, providing location-specific information about the presence of spatial patterns. As a member of the Local Indicators of Spatial Association (LISA) family, Local Moran's I builds upon the global Moran's I statistic to offer a more fine-grained understanding of spatial relationships within a dataset.

Four types of spatial clusters and outliers can be identified:
- High-High (HH) clusters (hot-spots),
- Low-Low (LL) clusters (cold-spots),
- High-Low (HL) outliers, and
- Low-High (LH) outliers.

Local Moran's I results could be observed and discussed in two linked maps, i.e., the local significance map and local cluster map. These maps can be used to visualize the spatial distribution of clusters and outliers, aiding in the interpretation and understanding of spatial patterns.
