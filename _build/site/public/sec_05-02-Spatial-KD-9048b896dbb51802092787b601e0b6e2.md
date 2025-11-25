# Spatial Kernel Density Estimation
------
.square[Introduction .dot[] Example .dot[] Bandwidth .dot[] Kernel Function .dot[] Edge-effect .dot[] Advanced Techniques]

.headnote.square.bold.x-large[Point Pattern II]

---
class: left, middle
.split-40[.column[
### Spatial Kernel Density Estimation
Spatial Kernel Density Estimation (Spatial KDE) is an extension of KDE for analyzing geospatial data.

It works with the same approach as KDE, i.e., selecting a Kernel Function, choosing a bandwidth, and calculate the density for every spatial sampling unit (grid cells).

.xkcd[How every event points contribute to the density of each sample grid cell?]
].column[

<img src="resources/w06-img/density_based.png" width="70%">


]]

---
class: center, middle
### Spatial Kernel Density Estimation

<img src="resources/w06-img/SpatialKDE_inanutshell.png" width="80%">

.footnote.small[Bailey and Gatrell 1995. Interactive Spatial Data Analysis. [Anderson 2009](https://pdf.sciencedirectassets.com/271664/1-s2.0-S0001457509X00035/1-s2.0-S0001457508002340/dx.doi.org/10.1016/j.aap.2008.12.014)]


---
class: left, middle
.split-30[.column[
### Spatial Kernel Density Estimation
.square[The sum of 2-D kernel functions. ]
].column[
<img src="resources/w06-img/summing_KDE_surface2.png" width="90%">

.footnote-left.small[[Levine 2013. Crimestat 4](https://www.ojp.gov/pdffiles1/nij/grants/242960-242995.pdf)]
]]

---
class: left, middle

.split-50[.column[
### Spatial KDE vs. aggregated count by cell
When using a grid-based approach for spatial data analysis, counting points in each cell might only reveal random distribution if the grid cell size is too small (the lower figure). In such cases, the counting result is not useful in presenting the spatial pattern.

Density estimation techniques, such as spatial KDE (middle figure), can help identify the spatial structure and trends within the data. These methods can effectively highlight areas with high concentration versus low concentration, as well as capture the changing rates and other essential aspects of spatial patterns.
].column[
<img src="resources/w06-img/demonstration_KDE-c.png" width="90%">
]]

---
class: center, middle

### Example of Spatial KDE - Health care POI @ Queenstown

<img src="resources/w06-img/cat_health_care.png" width="90%">

---
class: center, middle

### Example of Spatial KDE - Commercial POI @ Queenstown

<img src="resources/w06-img/cat_commercials.png" width="90%">

---
class: center, middle

### Example of Spatial KDE - Education POI @ Queenstown

<img src="resources/w06-img/cat_education.png" width="90%">

---
class: center, middle

### Example of Spatial KDE - Food POI @ Queenstown

<img src="resources/w06-img/cat_foods.png" width="90%">

---
class: center, middle

### Example of Spatial KDE - Beverages POI @ Queenstown

<img src="resources/w06-img/cat_beverages.png" width="90%">

---
class: center, middle

### Example of Spatial KDE - Outdoor Activity POI @ Queenstown

<img src="resources/w06-img/cat_outdoor_activity.png" width="90%">

---
class: left, middle
.split-30[.column[
### Bandwidth Selection in Spatial KDE
With smaller bandwidth values, the density estimates are more localized and highlight finer details of the data distribution, which could be similar to the distribution of aggregated count by cell---seems random. As the bandwidth increases, the KDE maps start to emphasize broader spatial patterns and general trends in the data. This smoother representation of density may help identify larger-scale features and regional differences while potentially .red[overlooking local variations] in the data.


].column[
<img src="resources/w06-img/kde_queenstown_health.png" width="100%">
]]

---
class: left, middle
.split-30[.column[
### Bandwidth Selection in Spatial KDE
].column[
<img src="resources/w06-img/kde_dif_bw.png" width="80%">
]]

---
class: left, middle

.split-30[.column[
### Spatial Kernel Functions
(a) Gaussian
(b) Epanechnikov
(c) Triangular
(d) Uniform

All kernel functions have a rounded base shape.
].column[
<img src="resources/w06-img/kernel_functions_3D.png" width="80%">

.footnote-right.small[[Fouedjio et al. 2017](http://dx.doi.org/10.1080/03717453.2017.1415114)]
]]

---
class: center, middle
### Kernel Functions for Spatial KDE

<img src="resources/w06-img/kde_dif_kernel.png" width="100%">

Examples and differences between threee Kernel Functions using the same dataset.

---
class: center, middle

.headnote.large.bold[Visualizing KDE]
<img src="resources/w06-img/kde_example_1.png" width="80%">
.footnote.small.square[[Chin 2023](https://dx.doi.org/10.1007/978-981-19-8765-6_8)]

---
class: center, middle

.headnote.large.bold[Visualizing KDE]
<img src="resources/w06-img/kde_example_2.png" width="50%">
.footnote.small.square[[Xia et al. 2024](https://doi.org/10.1186/s40494-024-01499-5)]

---
class: center, middle

.headnote.large.bold[Visualizing KDE]
<img src="resources/w06-img/kde_example_4.png" width="100%">
.footnote.small.square[[Wheeler 2014](https://andrewpwheeler.com/tag/kernel-density/)]

---
class: center, middle

.headnote.large.bold[Visualizing KDE]
<img src="resources/w06-img/kde_example_3.png" width="70%">
.footnote-right.small.square[[Yang et al. 2019](https://doi.org/10.3390/ijgi8020093)]

---
class: center, middle

.headnote.large.bold[Visualizing KDE]
<img src="resources/w06-img/kde_example_5.png" width="100%">
.footnote.small.square[[Kuo et al. 2012](https://api.semanticscholar.org/CorpusID:5968823)]

---
class: center, middle

.headnote.large.bold[Visualizing KDE]
<img src="resources/w06-img/kde_example_6.png" width="80%">
.footnote.small.square[[Levine 2013](https://www.ojp.gov/pdffiles1/nij/grants/242960-242995.pdf)]

---
class: left, middle

.split-30[.column[
### Edge Effects
Edge effects in KDE refer to the bias and inaccuracy in density estimates near the boundary of the study area due to the lack of data beyond the edges.
].column[
<img src="resources/w06-img/cat_outdoor_activity.png" width="100%">
]]

---
class: left, middle

.split-20[.column[
### Edge Effects
.bold[Methods addressing edge effects]
].column[
- .bold[Reflection Method]: Mirror the data points across the boundary, creating a new set of points outside the study area. Apply KDE to this extended dataset, ensuring the density estimates near the boundary are influenced by the reflected points, reducing edge effects.
- .bold[Gaussian Truncation]: Truncate the Gaussian kernel function used in KDE at the boundary of the study area. This method eliminates the need to make assumptions about the data beyond the boundary, as the truncated kernel function only considers the points within the study area.
- .bold[Adaptive Kernel Methods]: Utilize adaptive kernel functions, where the kernel shape and bandwidth vary based on the local density of points. By adapting to the local density, these methods can help reduce edge effects and produce more accurate density estimates near the boundary.
- .bold[Boundary Correction Methods]: Apply boundary correction methods, such as the bias-correction method proposed by Chen and Firth (2000), which adjusts the density estimates near the boundary to compensate for edge effects.
- .bold[Expansion of the Study Area]: Expand the study area beyond the original boundary, ensuring that the kernel function extends beyond the actual area of interest. This approach eliminates edge effects but may introduce uncertainty in density estimates for areas without data.

]]

---
class: left, middle

.split-20[.column[
### Advanced Techniques and Applications
- .red[Dual KDE]
- Space-time KDE
- Network KDE
].column[
<img src="resources/w06-img/advanced_dualkde.png" width="90%">
.footnote-left.square[[Jansenberger & Staufer-Steinnocher 2004](https://www.researchgate.net/publication/252791884_Dual_Kernel_Density_Estimation_as_a_Method_for_Describing_Spatio-Temporal_Changes_in_the_Upper_Austrian_Food_Retailing_Market)]

]]

---
class: left, middle

.split-20[.column[
### Advanced Techniques and Applications
- Dual KDE
- .red[Space-time KDE]
- Network KDE
].column[
<img src="resources/w06-img/advanced_stkde.png" width="100%">
.footnote.square[[Hu et al. 2018](https://doi.org/10.1016/j.apgeog.2018.08.001)]

]]

---
class: left, middle

.split-20[.column[
### Advanced Techniques and Applications
- Dual KDE
- Space-time KDE
- .red[Network KDE]
].column[
<img src="resources/w06-img/advanced_nkde.png" width="100%">
.footnote.square[[Tang et al. 2016](https://doi.org/10.1080/13658816.2015.1119279)]
]]

---
class: left, middle

.split-20[.column[
### Summary
].column[
- .bold[Introduction]: Spatial KDE is an extension of KDE for analyzing spatial data, focusing on patterns, trends, and density variations within a geographic context.
- .bold[Applications]: Spatial KDE is widely used in fields like ecology, crime analysis, epidemiology, and urban planning to identify hot spots, clusters, and spatial relationships.
- .bold[Spatial Adaptations]: Spatial KDE adapts traditional KDE by incorporating techniques to handle edge effects and the specific characteristics of spatial data.
- .bold[Kernel Functions]: Different kernel functions can be used in spatial KDE to accommodate various data distributions and spatial patterns, ensuring accurate density estimation.
- .bold[Bandwidth Selection]: Choosing an appropriate bandwidth for spatial KDE is crucial for accurate density estimation and pattern identification. Methods include rule-of-thumb, cross-validation, and plug-in approaches.
- .bold[Visualization]: Spatial KDE results are typically visualized as heatmaps, contour plots, or 3D surfaces to facilitate interpretation and communication of spatial patterns and trends.
]]


### Capturing Local Point Patterns with Spatial KDE
].column[

- Spatial KDE is an effective method for capturing and visualizing local point patterns in spatial data.
- By estimating density using a moving kernel window, spatial KDE highlights areas of high and low concentration within the study area.
- Bandwidth selection plays a crucial role in capturing local point patterns, as it controls the level of smoothing and the size of the local neighborhood considered in the density estimate.
- Smaller bandwidths capture finer details and local variations, while larger bandwidths highlight broader spatial trends and regional differences.
- Visualizing spatial KDE results as heatmaps or contour plots allows for easy identification of hotspots, clusters, and spatial relationships within the data.
- Spatial KDE does not provide related statistical tests to assess the significance level of the identified patterns or differences between point patterns. Additional statistical methods may be required for a more comprehensive analysis.
]]
