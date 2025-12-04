# Getis-Ord G statistics

## Getis-Ord General G
Three things to notice next

- the difference between 'stars': with star means $j$ can equal to $i$

- $x_i \times x_j$

- The lower part (denominator) is a kind of standardizig process to control the range of the resulting values.

$$\text{global} = a . [\sum_i \text{component}(i)]$$


### Global version
General G:

$$
\text{G} = \frac{\sum_i \sum_{j\neq  i} w_{ij} x_i x_j }{\sum_i\sum_{j\neq  i} x_i x_j}
$$

General G*:

$$
\text{G}^{\ast} = \frac{\sum_i \sum_j w_{ij} x_i x_j }{\sum_i\sum_j x_i x_j}
$$


### Local version
Gi:

$$
\text{G}_i = \frac{\sum_{j\neq i}w_{ij}x_j}{\sum_{j\neq i}x_j}
$$

Gi*:

$$
\text{G}_{i}^{\ast} = \frac{\sum_{j}w_{ij} x_j}{\sum_{j} x_j}
$$


## The three measures

**Moran's I**
- focus on $(x_i - \bar{x})(x_j - \bar{x})$ (deviation from the mean value)
- **large positive** value (I>0): spatial clusters (HH or LL)
- **large negative** value (I<0): spatial outliers (HL or LH)
- near zero (I=0): random

**Geary's C**
- focus on $(x_i - x_j)^2$ (squared differences)
- **small** value (c<1): spatial clusters (HH or LL)
- **large** value (c>1): spatial outliers (HL or LH)
- near 1 (c=1): random

**Getis-Ord G\***
- focus on $x_i \times x_j$ (the intensity of values in local neighborhoods to the global average)
- **large** value (G\* > mean(G\*)): hot-spot (HH)
- **small** value (G\* < mean(G\*)): cold-spot (LL)
- near mean(G\*): random


## Interpretation
### Significance Maps

```{figure} ../resources/w09-img/guerry_LG_significant_map.png
:label:
:alt:
:align: center

Significance Maps
```



### Cluster Maps

```{figure} ../resources/w09-img/guerry_LG_cluster_map.png
:label:
:alt:
:align: center

Cluster Maps
```

## Closing Remarks

### Choosing the appropriate method(s)
There are so many different methods and equations for spatial autocorrelation, which one should I use?

**Aim of Visualisation**
- If you only want to detect high and low clustering phenomena, the **Getis-Ord G statistics** could be sufficient.
- If your data are expected to have a common middle value (e.g., mean), and you aim to detect hot-spots and cold-spots in relation to this middle value, **Moran's I** is ideal.
- If you want to detect places with similar values (not necessarily compared to the middle value), **Geary's C** is the way to go.

**Scale Sensitivity**
- **Moran's I** is more sensitive to larger-scale spatial patterns, as every value is compared to the global mean.
- **Geary's C** is better at detecting local, smaller-scale variations, since it calculates the differences rather than similarity between values.
- **Getis-Ord G** statistic is also more sensitive to large-scale spatial patterns. The range of the product obtained by multiplying a pair of values implies that it focuses on global high and global low value pairs.

**Comparison with Previous Studies**
- If you want to compare your results with other research in your field, choose a method that is commonly used in those studies for consistency and ease of comparison.


### What we have learnt so far

<img src="../resources/w09-img/recap-1c.drawio.png" width="60%">
