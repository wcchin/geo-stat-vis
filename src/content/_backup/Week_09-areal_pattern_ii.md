slide_title: Areal Pattern II: Spatial Autocorrelation & Hotspot Detection 
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

## Areal Pattern II: Local Spatial Autocorrelation
------

<br />

.x-large.bold[Dr. CHIN Wei Chien Benny]  
[.underline.square[wcchin@nus.edu.sg]]  

.headnote.square.bold.x-large[GE5230 Geospatial Statistics and Visualization]
.footnote.square[09 @ 2025-10-16 Department of Geography, NUS]

---
layout: false
class: center, middle

### What we have learnt so far

<img src="resources/w09-img/recap-1c.drawio.png" width="60%"> 

---
class: center, middle

### What we have learnt so far
.split-40[.column[
.red.xkcd[Why does the spatial pattern of attributes/values matter? And how do we analyze it?] 

Relatie Space: How the neighboring area is related to one/each location.

].column[
<img src="resources/w04-img/drawing-fourspaces.png" width="70%"> 
]]

---
class: left, middle
.split-50[.column[

### Spatial Contiguity
- A regular grid, 
- Rook (share edge only) <img src="resources/w08-img/rook-svgrepo.svg" width="10%">
- bishop (share point only) <img src="resources/w08-img/bishop-svgrepo.svg" width="10%">
- queen (share edge and point) <img src="resources/w08-img/queen-svgrepo.svg" width="10%">

Higher levels contiguity can be done by adding second, third, etc. outer ring of neighborhoods.  

].column[
<img src="resources/w08-img/demo_contiguity.png" width="90%">
]]


---
class: left, middle
.split-30[.column[
### What is Autocorrelation (recap)
].column[
- The 'auto-' in autocorrelation means .red['oneself']. It is a word 'autos' that comes from Greek. 
- Autocorrelation is a measure of the linear relationship .red[between values of a variable and its own nearby values]. The 'self'-correlation here refer to the correlation within one variable itself. 
- .red['Self'-correlation: similar values between a location and its neighbor.] 
- .red[Moran's I]: an indicator for measuring the 'global' spatial autocorrelation.
- Spatial-lag: The overall value of the neighboring area.

]]

---
class: left, middle
.split-30[.column[
### What is Spatial Autocorrelation
].column[
- to identify spatial structure of statistical distribution in space. 
- patterns:
    - high-high: high surrounded by high 
    - low-low: low surrounded by low
    - high-low: high surrounded by low
    - low-high: low surrounded by high
]]

---
class: left, middle
### Global vs. Local
Global and local analyses are two approaches used in spatial data analysis to explore patterns and relationships within geographical data. 
While .red[global] analysis provides .red[an overview of the entire dataset], .red[local] analysis offers a more detailed understanding of .red[spatial patterns] and relationships .red[at the location level]. 
Here's a comparison between the two:
.split-50[.column[
.bold.red[Global Analysis]:
- .bold[Focus]: Global analysis examines the .red[overall patterns] and trends in a dataset, considering the entire study area as a whole.
- .bold[Measures]: Moran's I, Geary's C, Genarl G.
- .bold[Application]: Global analysis is useful for understanding general trends and relationships within the data, such as .red[whether there is a tendency for high or low values] to cluster across the entire study area.

].column[

.bold.red[Local Analysis]:
- .bold[Focus]: Local analysis investigates patterns and relationships at spatial-unit levels to reveal .red[spatial structure].
- .bold[Measures]: Local Moran's I, Local Geary's C, Gi, and Gi*.
- .bold[Application]: Local analysis is helpful for .red[understanding the spatial distribution of variables] and .red[identifying areas with significant concentrations or disparities], which can inform targeted interventions or policies.
]]


---
class: center, middle

### Negative, Random, and Positive Spatial Autoccorrelation
<img src="resources/w09-img/grid_3_spatial_autocor.png" width="70%"> 

---
class: left, middle
## Objectives of this lecture
- Local Indicator of Spatial Association: Local Moran's I
- Geary's C & Local Geary
- Getis-Ord G statistics
<!--- *Bivariate LISA*-->

---
class: center, middle, inverse

.xx-large.bold.wide[PART 1]
## Local Moran's I
------
.square[Hot/Cold Spots .dot[] LISA ]

.headnote.square.bold.x-large[Areal Pattern II]

---
class: left, middle
.split-30[.column[
### What is LISA
].column[
LISA, which stands for Local Indicators of Spatial Association, is a set of statistical measures used in spatial data analysis to identify and assess local patterns of spatial autocorrelation. LISA helps detect areas with significant concentrations or disparities of a given variable, such as regions with high crime rates, low-income neighborhoods, or areas with a high prevalence of a particular disease.

LISA encompasses various types of measures, including .red[Local Moran's I, Local Geary's C, Gi, and Gi*]. These measures build upon the concept of global spatial autocorrelation, measured by Moran's I (for Local Moran), Geary's C (for local Geary C), by providing location-specific insights into spatial structures, mainly on spatial clustering (hot-spots, cold-spots) and spatial outliers (neighboring with the opposite type).

By analyzing the spatial patterns and local clustering of a given variable through the different LISA measures, researchers can gain valuable insights for urban planning, public health, environmental studies, criminology, and other fields where spatial relationships and interactions play a crucial role.

]]

---
class: left, middle
.split-30[.column[
### LISA form of global spatial autocorrelation
].column[
- Decomposable statistics 

- $\text{global} = a . [\sum_i \text{component}(i)]$

- then $\text{local}(i) = \text{component}(i)$
]]

---
class: left, middle
.split-30[.column[
### What is Local Moran's 
].column[
Local Moran's I is a measure of spatial autocorrelation used in geography and geographic information science (GIS) to assess the degree of spatial clustering or dispersion of a given variable around a specific location. Developed by Anselin (1995), it is a local version of the global Moran's I statistic, which measures the overall spatial autocorrelation in a dataset.

Local Moran's I helps identify the extent of significant spatial clustering of similar values around a specific observation. It calculates the correlation between a value at a given location and the values at neighboring locations, highlighting areas with high or low concentrations of the variable under study. This information can be useful in various applications, such as identifying crime hotspots, determining areas with higher disease prevalence, or understanding income disparities across a region.

Essentially, Local Moran's I provides a way to evaluate spatial patterns and relationships between values at specific locations and their surroundings, offering insights into the spatial structure of the data.

]]

---
class: left, middle
.split-30[.column[
### The target of Local Moran
].column[
The target of Local Moran is to identify two types of locations with statistical significance (through permutation): 
- .bold[Clusters]: locations with significantly similar values (hot-spots & cold-spots)
- .bold[Outliers]: locations with significantly different values.
- Places with very similar but not far from the means are ignored (as non-significant). 

.red[Clusters]: To identify locations with .red[positive] correlation: 
- High-High (HH) clusters: .red[high] value locations surrounded by .red[high] value neighbors
- Low-Low (LL) clusters: .red[low] value locations surrounded by .red[low] value neighbors

.red[Outliers]: To identify locations with .red[negative] correlation: 
- High-Low (HL) outliers: .red[high] value locations surrounded by .red[low] value neighbors
- Low-High (LH) outliers: .red[low] value locations surrounded by .red[high] value neighbors

]]

---
class: left, middle
.split-30[.column[

### Global Moran's I: Formula

The lower part (denominator) is a kind of standardizig process to control the range of the resulting values. 

].column[
$$
\text{I}=\frac{N}{W} \times \frac{\sum\_i^N \sum\_j^N w_{i,j}(x_i-\bar{x})(x_j-\bar{x})}{\sum_k (x_k-\bar{x})^2}
$$

<!--<img src="resources/w08-img/morans_I_equation.png" width="80%">-->

Where:
- $N$ is the number of spatial units indexed by $i$ and $j$;
- $x$ is the variable of interest;
- $\bar{x}$ is the mean of $x$;
- $w_{i,j}$ is the spatial weight---kind of an indicator variable, equal to 1 or the row-standardized value if $i$ and $j$ are neighbors, 0 otherwise;
- W is the sum of all $w\_{i,j}$.

Let's $z_i = x_i - \bar{x}$ (i.e., deviations from mean), then

$$
\text{I} = \frac{\sum\_i \sum\_j w_{i,j} \times z_i \times z_j}{\sum_k z_k^2}
$$

<!--<img src="resources/w09-img/morans_I_equation2.png" width="60%">-->


]]

---
class: left, middle
.split-30[.column[

### Local Moran's I: Formula
The lower part (denominator, $\sum_k z_k^2$) is a kind of standardizig process to control the range of the resulting values. 

].column[
$$
\text{I} = \frac{\sum\_i \sum\_j w_{i,j} \times z_i \times z_j}{\sum_k z_k^2}
$$
<!--<img src="resources/w09-img/morans_I_equation2.png" width="50%">-->

rearrange...

$$
\text{I} = \frac{1}{\sum\_k z\_k^2} \times [\sum\_i z\_i \sum\_j w\_{i,j} \times z\_j]
$$
<!--<img src="resources/w09-img/morans_I_equation3.png" width="60%">-->

$\sum_k z_k^2$ will not change with $i$, thus constant and this could be captured by the form of: 

- $\text{global} = a . [\sum_i \text{component}(i)]$

$$
\text{Local I}\_i = \frac{1}{\sum\_k z\_k^2} \times z\_i \sum\_j w\_{i,j} \times z\_j
$$
<!--<img src="resources/w09-img/morans_I_local_equation_2.png" width="60%">-->


]]

---
class: left, middle
.split-30[.column[
### Technical aspects of Local Moran('s I)
The first part ($1 / \sum_k z_k^2$ or $N / \sum_k z_k^2$) is a kind of standardizig process to control the range of the resulting values. 
].column[
- for row-standardized weights  
(such that $S_0$ and $N$ cancel out in Moran's I)

- variables as deviations from mean ($z_i = x_i - \bar{x}$, positive means greater than mean, and negative means less than mean). 

$$
\text{Local I}\_i = \frac{1}{\sum\_k z\_k^2} \times z\_i \sum\_j w\_{i,j} \times z\_j
$$
<!--<img src="resources/w09-img/morans_I_local_equation_2.png" width="60%">-->

- $z_i$ is the deviation from mean for the current location 
- <!--<img src="resources/w09-img/lag_term.png" width="15%">-->$\sum\_j w\_{i,j} \times z\_j$ is the 'lag' term, how high or low is the (location $i$'s) neighbors'  overall value compared to the mean

- for non-row-standardised  
$$
\text{Local I}\_i = \frac{N}{\sum\_k z\_k^2} \times z\_i \sum\_j w\_{i,j} \times z\_j
$$
take note on the $N$...
]]

---
class: left, middle
.split-30[.column[
### Link Local - Global: LISA
].column[
take note on the $N$: 
$$
\sum\_i \text{Local I}\_i = \sum\_i \frac{N}{\sum\_k z\_k^2} \times z\_i \sum\_j w\_{i,j} \times z\_j
$$
$$
\sum\_i \text{Local I}\_i = N \times \frac{1}{\sum\_k z\_k^2} \times \sum\_i z\_i \sum\_j w\_{i,j} \times z\_j
$$
$$
\sum\_i \text{Local I}\_i = N \times \text{Global I}
$$

- $\sum_i \text{local}_i = N . \text{global}$

- or $\text{global} = \frac{\sum_i \text{local}_i}{N}$

- the global statistics is the average of local statistics

]]

---
class: left, middle
.split-30[.column[

### Statistical Inference
].column[

- analytical and computational

- analytical approximation is poor (do not use)

- computational approach is based on .red[conditional permutation]

]]

---
class: left, middle
.split-30[.column[

### Conditional Permutation
].column[
- Conditional upon value observed at location i

- hold value at i fixed, random permute remaining n-1 values and recompute local Moran's I
    - since $w_{i,j}$ leave non-neighbors to be 0, this is same as randomly pick J number of value (without replacement), J is the number of neighbors, then locate these J values on each neighbor for the local Moran calculation. 

- repeat many times (e.g., 999) to obtain reference distribution for location i, compare and calculate pseudo p-value

- computationally intensive:
    - if there is N size of entity (row), and the permutation is set to 1000, then the calculation takes N * 1000. 

]]

---
class: left, middle
.split-30[.column[

### Interpretation
#### Local Significance Map
].column[
- shows locations with significant local statistic by level of significance.

- not very useful for substantive interpretation

- useful for observation of the confidence level

- diagnostic for sensitivity of results (for example, when only significant at 0.05 but not at 0.001). 
]]

---
class: left, middle
.split-30[.column[

### Interpretation
#### An example
Take an example: the donations data (Guerry data)
].column[
<img src="resources/w09-img/guerry_data.png" width="100%">

]]

---
class: left, middle
.split-30[.column[

### Interpretation
#### The Local Significance Map
].column[
<img src="resources/w09-img/guerry_significant_map.png" width="100%">
]]

---
class: left, middle
.split-30[.column[

### Interpretation
#### The Local Cluster Map
].column[
- shows locations with .red[significant] local spatial autocorrelation by .red[type of association]

- four types (four colours):
    - HH clusters
    - LL clusters
    - HL outliers
    - LH outliers

- shown only for a specified significance level (sensitivity analysis)

- .red[but the Local Moran can only be used to identify positive or negative correlation, i.e., clusters or outliers, how to differentiate the HH from LL and HL from LH?]
]]

---
class: center, middle

### Interpretation
#### The Local Cluster Map

<img src="resources/w09-img/guerry_significant_map_scatter.png" width="100%">

.xkcd[use the quadrants]

---
class: left, middle
.split-30[.column[

### Interpretation
#### The Local Cluster Map
].column[
<img src="resources/w09-img/guerry_I_cluster_map.png" width="100%">
]]

---
class: left, middle
.split-50[.column[

### Interpretation
#### The Local Cluster Map (sensitivity analysis)

On the right, 
- top: p-value < 0.05
- bottom: p-value < 0.01

Through the changes of significance level, we can observe the changes of clusters/outliers and identify those that is more significant. 

].column[
<img src="resources/w09-img/guerry_I_cluster_map_sensitivity.png" width="75%">
]]

---
class: center, middle

### Interpretation
#### The Local Outliers

<img src="resources/w09-img/guerry_local_outliers_HL.png" width="100%">

The locations of HL outliers and their neighbors. 

---
class: center, middle

### Interpretation
#### The Local Outliers

<img src="resources/w09-img/guerry_local_outliers_LH.png" width="100%">

The locations of LH outliers and their neighbors. 

---
class: center, middle

### Interpretation
#### The Local Hot-spots

<img src="resources/w09-img/guerry_local_cluster_HH.png" width="100%">

The locations of HH clusters and their neighbors. 

---
class: center, middle

### Interpretation
#### The Local Cold-spots

<img src="resources/w09-img/guerry_local_cluster_LL.png" width="100%">

The locations of LL clusters and their neighbors. 

---
class: left, middle
.split-30[.column[
### Overview
].column[
Local Moran's I is a local measure of spatial autocorrelation used in spatial data analysis. It assesses the degree of spatial clustering or dispersion around individual locations, providing location-specific information about the presence of spatial patterns. As a member of the Local Indicators of Spatial Association (LISA) family, Local Moran's I builds upon the global Moran's I statistic to offer a more fine-grained understanding of spatial relationships within a dataset.

Four types of spatial clusters and outliers can be identified: 
- High-High (HH) clusters (hot-spots), 
- Low-Low (LL) clusters (cold-spots), 
- High-Low (HL) outliers, and 
- Low-High (LH) outliers.

Local Moran's I results could be observed and discussed in two linked maps, i.e., the local significance map and local cluster map. These maps can be used to visualize the spatial distribution of clusters and outliers, aiding in the interpretation and understanding of spatial patterns.
]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 2]
## Geary's C and Local Geary
------
.square[Geary's C .dot[] Local Geary]

.headnote.square.bold.x-large[Areal Pattern II]

---
class: left, middle
.split-60[.column[
### Spatial Autocorrelation metrics and their Local versions
].column[
- Moran's I and Local Moran's I

- .red[Geary's C and Local Geary's C]

- General G statistics, Gi, and Gi*
]]

---
class: left, middle
.split-30[.column[
### Geary's C
The lower part (denominator) is a kind of standardizig process to control the range of the resulting values. 

].column[
Geary's C is a global measure of spatial autocorrelation used in spatial data analysis to determine the overall degree of spatial dependency in a dataset. It quantifies the degree to which values in a dataset are similar to or different from neighboring values, considering the entire study area. Unlike  Moran's I, Geary's C focuses on .red.bold[the distance between value of a location and its neighbors] rather than their distances to the mean value. 

$$
C = \frac{(N-1)\sum\_i\sum\_j w\_{ij}(x\_i-x\_j)^{2}}{2S\_0\sum\_i(x\_i-\bar{x})^{2}}
$$
<!--<img src="resources/w09-img/geary_c_equation.png" width="80%">-->

In this equation:
- $N$ is the number of observations.
- $w_{ij}$ is the spatial weight matrix, representing the spatial relationships between observations $i$ and $j$.
- $x_{k}$ are the observed values of the variable at location k.
- $S_{0}$ is the sum of all spatial weights.
- $\bar{x}$ is the mean of the observed values.

]]

---
class: left, middle
.split-30[.column[
### Local Geary's C
The lower part (denominator) is a kind of standardizig process to control the range of the resulting values. 

].column[
And the Local Geary
$$
c\_i = \frac{\sum\_j w\_{ij}(x\_i - x\_j)^2}{2S\_0}
$$
<!--<img src="resources/w09-img/geary_c_local_equation.png" width="80%">-->

Unlike the global Geary's C, the local version provides .red[location-specific information about spatial autocorrelation], allowing for the identification of spatial clusters and outliers. .bold.red[Low values] of the Local Geary's C indicate .red[positive] spatial autocorrelation (.red[similar values cluster together]), while .bold.red[high values] indicate .red[negative] spatial autocorrelation (.red[dissimilar values are close to each other]).

]]

---
class: center, middle
### Comparing Global vs. Local
$$\text{global} = a . [\sum_i \text{component}(i)]$$

.split-50[.column[
#### Global
$$
C = \frac{(N-1)\sum\_i\sum\_j w\_{ij}(x\_i-x\_j)^{2}}{2S\_0\sum\_i(x\_i-\bar{x})^{2}}
$$

$$
C = \frac{(N-1)}{2S\_0\sum\_i(x\_i-\bar{x})^{2}} \times \sum\_i\sum\_j w\_{ij}(x\_i-x\_j)^{2}
$$

$$
C = \frac{(N-1)}{\sum\_i(x\_i-\bar{x})^{2}} \times \sum\_i \frac{1}{2S\_0}\times \sum\_j w\_{ij}(x\_i-x\_j)^{2}
$$

$$
C = \frac{(N-1)}{\sum\_i(x\_i-\bar{x})^{2}} \times \sum\_i c\_i
$$


].column[
#### Local
$$
c\_i = \frac{\sum\_j w\_{ij}(x\_i - x\_j)^2}{2S\_0}
$$

$$
c\_i = \frac{1}{2S\_0} \times \sum\_j w\_{ij}(x\_i - x\_j)^2
$$
]]



---
class: left, middle
.split-30[.column[
### Interpretation
].column[
- $(x_i - x_j)^2$

- attribute dissimilarity

- distance in attribute space

- Geary's C: weighted average of distances in .red[attribute space] to neighbors in .red[geographic space]

- positive: similarity, can be high-high, low-low, .red[middle-middle]

- negative: dissimilarity: no distinction between high-low and low-high

- Geary's C is more sensitive to .red[local patterns of spatial autocorrelation] and can better capture smaller-scale variations in the data.  
.red.bold[spatial non-stationarity]: a sub-region of the study area has a different (e.g., lower) average value, for which the similar-values (could be middle-middle) may be overlooked by Moran's I (and its local variant). 
]]

---
class: left, middle
.split-30[.column[

### Interpretation
#### An example (for reference)
Take an example: the donations data (Guerry data)
].column[
<img src="resources/w09-img/guerry_data.png" width="100%">

]]

---
class: left, middle
.split-30[.column[
### Interpretation
#### Local Significance Map
].column[
<img src="resources/w09-img/guerry_LC_significant_map.png" width="100%">

]]

---
class: left, middle
.split-30[.column[
### Interpretation
#### Local Cluster Map
].column[
<img src="resources/w09-img/guerry_C_cluster_map.png" width="100%">

]]

---
class: center, middle

### Interpretation
#### Comparison between p-value

<img src="resources/w09-img/guerry_C_cluster_map_sensitivity.png" width="100%">

---
class: center, middle

### Local Moran's I vs. Local Geary's C

<img src="resources/w09-img/guerry_I_C_cluster_map_sensitivity.png" width="65%">

---
class: left, middle
.split-30[.column[
### Moran's I vs. Geary's C
].column[

- Different type of attribute similarity
    - cross-product (correlation) vs.
    - squared difference (dissimilarity)

- power against different alternatives
    - the same null hypothesis: spatial randomness
    - what should be the 'alternative'? 

- Moran's I and its local variant: Detect similar values based on their .red[deviation from the mean value]. 
    - Moran's I is more sensitive to global patterns of spatial autocorrelation and overall trends in the data.

- Geary's C and its local variant: Detect similar values based on the .red[absolute differences between pairs of values]. 
    - Geary's C is more sensitive to local patterns of spatial autocorrelation and smaller-scale variations in the data.


]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 3]
## Getis-Ord G statistics
------
.square[General G .dot[] Local Gi]

.headnote.square.bold.x-large[Areal Pattern II]

---
class: left, middle
.split-60[.column[
### Spatial Autocorrelation metrics and their Local versions
].column[

- Moran's I and Local Moran's I

- Geary's C and Local Geary's C

- .red[General G statistics and Gi; G and Gi*]
]]

---
class: left, middle

### Three things to notice in next slide

- the difference between 'stars': with star means $j$ can equal to $i$

- $x\_i \times x\_j$

- The lower part (denominator) is a kind of standardizig process to control the range of the resulting values. 


---
class: left, middle

### Getis-Ord General G
$$\text{global} = a . [\sum_i \text{component}(i)]$$

.split-50[.column[
#### Global version 
General G: 
$$
\text{G} = \frac{\sum\_i \sum\_{j\neq  i} w\_{ij} x\_i x\_j }{\sum\_i\sum\_{j\neq  i} x\_i x\_j}
$$

General G*:

$$
\text{G}^{\*} = \frac{\sum\_i \sum\_j w\_{ij} x\_i x\_j }{\sum\_i\sum\_j x\_i x\_j}
$$

].column[
#### Local version
Gi: 
$$
\text{G}\_i = \frac{\sum\_{j\neq i}w\_{ij}x\_j}{\sum\_{j\neq i}x\_j}
$$

Gi*: 

$$
\text{G}\_{i}^{\*} = \frac{\sum\_{j}w\_{ij} x\_j}{\sum\_{j} x\_j}
$$

]]

---
class: left, middle
.split-30[.column[
### The three measures

].column[
#### Moran's I
- focus on $(x\_i - \bar{x})(x\_j - \bar{x})$ (deviation from the mean value)
- .red[large positive] value (I>0): spatial clusters (HH or LL)
- .red[large negative] value (I<0): spatial outliers (HL or LH)
- near zero (I=0): random

#### Geary's C
- focus on $(x\_i - x\_j)^2$ (squared differences)
- .red[small] value (c<1): spatial clusters (HH or LL)
- .red[large] value (c>1): spatial outliers (HL or LH)
- near 1 (c=1): random

#### Getis-Ord G\*
- focus on $x\_i \times x\_j$ (the intensity of values in local neighborhoods to the global average)
- .red[large] value (G\* > mean(G\*)): hot-spot (HH)
- .red[small] value (G\* < mean(G\*)): cold-spot (LL)
- near mean(G\*): random
]]

---
class: center, middle

### Significance Maps

<img src="resources/w09-img/guerry_LG_significant_map.png" width="100%">


---
class: center, middle

### Cluster Maps

<img src="resources/w09-img/guerry_LG_cluster_map.png" width="100%">


---
class: center, middle, inverse

## Closing Remarks
------
.square[LISA .dot[] Local Moran's I .dot[] Geary's C and Local Geary .dot[] Getis-Ord G and Gi]

.headnote.square.bold.x-large[Areal Pattern II]

---
class: left, middle
.split-30[.column[
### Recap of this lecture
].column[
- LISA
- Local Moran's I
- Geary's C and Local Geary's C
- Getis-Ord G(\*) Statistics and Gi(\*)
]]

---
class: left, middle

.split-30[.column[
### Choosing the appropriate method(s)
There are so many different methods and equations for spatial autocorrelation, which one should I use?
].column[

.bold[Aim of Visualisation]
- If you only want to detect high and low clustering phenomena, the .red[Getis-Ord G statistics] could be sufficient.
- If your data are expected to have a common middle value (e.g., mean), and you aim to detect hot-spots and cold-spots in relation to this middle value, .red[Moran's I] is ideal.
- If you want to detect places with similar values (not necessarily compared to the middle value), .red[Geary's C] is the way to go.

.bold[Scale Sensitivity]
- .red[Moran's I] is more sensitive to larger-scale spatial patterns, as every value is compared to the global mean.
- .red[Geary's C] is better at detecting local, smaller-scale variations, since it calculates the differences rather than similarity between values.
- .red[Getis-Ord G] statistic is also more sensitive to large-scale spatial patterns. The range of the product obtained by multiplying a pair of values implies that it focuses on global high and global low value pairs.

.bold[Comparison with Previous Studies]
- If you want to compare your results with other research in your field, choose a method that is commonly used in those studies for consistency and ease of comparison.

]]

---
class: center, middle

### What we have learnt so far

<img src="resources/w09-img/recap-1c.drawio.png" width="60%"> 




