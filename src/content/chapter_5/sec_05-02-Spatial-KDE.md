# Spatial Kernel Density Estimation

## Spatial Kernel Density Estimation
Spatial Kernel Density Estimation (Spatial KDE) is an extension of KDE for analyzing geospatial data.

It works with the same approach as KDE, i.e., selecting a Kernel Function, choosing a bandwidth, and calculate the density for every spatial sampling unit (grid cells).

How every event points contribute to the density of each sample grid cell?

```{figure} ../resources/w06-img/density_based.png
:label:
:alt:
:align: center

Impacts from near by points to each cell.
```

```{figure} ../resources/w06-img/SpatialKDE_inanutshell.png
:label:
:alt:
:align: center

Spatial KDE in a nutshell. For more information, please see Bailey and Gatrell 1995. Interactive Spatial Data Analysis. [Anderson 2009](https://pdf.sciencedirectassets.com/271664/1-s2.0-S0001457509X00035/1-s2.0-S0001457508002340/dx.doi.org/10.1016/j.aap.2008.12.014)]

```



## Calculation of Spatial KDE

The sum of 2-D kernel functions.

```{figure} ../resources/w06-img/summing_KDE_surface2.png
:label:
:alt:
:align: center

The sum of bell shape kernels for every cell in the grid [Levine 2013. Crimestat 4](https://www.ojp.gov/pdffiles1/nij/grants/242960-242995.pdf).
```



## Spatial KDE vs. aggregated count by cell
When using a grid-based approach for spatial data analysis, counting points in each cell might only reveal random distribution if the grid cell size is too small (the lower figure). In such cases, the counting result is not useful in presenting the spatial pattern.

Density estimation techniques, such as spatial KDE (middle figure), can help identify the spatial structure and trends within the data. These methods can effectively highlight areas with high concentration versus low concentration, as well as capture the changing rates and other essential aspects of spatial patterns.

```{figure} ../resources/w06-img/demonstration_KDE-c.png
:label:
:alt:
:align: center

Demonstration of KDE.
```

## Example of Spatial KDE

```{figure} ../resources/w06-img/cat_health_care.png
:label:
:alt:
:align: center

Health care POI @ Queenstown
```


```{figure} ../resources/w06-img/cat_commercials.png
:label:
:alt:
:align: center

Commercial POI @ Queenstown
```


```{figure} ../resources/w06-img/cat_education.png
:label:
:alt:
:align: center

Education POI @ Queenstown
```


```{figure} ../resources/w06-img/cat_foods.png
:label:
:alt:
:align: center

Food POI @ Queenstown
```


```{figure} ../resources/w06-img/cat_beverages.png
:label:
:alt:
:align: center

Beverages POI @ Queenstown
```


```{figure} ../resources/w06-img/cat_outdoor_activity.png
:label:
:alt:
:align: center

Outdoor Activity POI @ Queenstown
```


## Bandwidth Selection in Spatial KDE
With smaller bandwidth values, the density estimates are more localized and highlight finer details of the data distribution, which could be similar to the distribution of aggregated count by cell---seems random. As the bandwidth increases, the KDE maps start to emphasize broader spatial patterns and general trends in the data. This smoother representation of density may help identify larger-scale features and regional differences while potentially **overlooking local variations** in the data.


```{figure} ../resources/w06-img/kde_queenstown_health.png
:label:
:alt:
:align: center

E.g., Health POI @ Queenstown
```


```{figure} ../resources/w06-img/kde_dif_bw.png
:label:
:alt:
:align: center

KDE with different bandwidths
```



## Kernel Functions for Spatial KDE
(a) Gaussian
(b) Epanechnikov
(c) Triangular
(d) Uniform

All kernel functions have a rounded base shape.


```{figure} ../resources/w06-img/kernel_functions_3D.png
:label:
:alt:
:align: center

Kernel functions (height-dimension) for 2D spatial data. See [Fouedjio et al. 2017](http://dx.doi.org/10.1080/03717453.2017.1415114).
```


```{figure} ../resources/w06-img/kde_dif_kernel.png
:label:
:alt:
:align: center

Examples and differences between threee Kernel Functions using the same dataset.
```


## Visualizing Spatial KDE
```{figure} ../resources/w06-img/kde_example_1.png
:label:
:alt:
:align: center

Example of Spatial KDE visualisation: [Chin 2023](https://dx.doi.org/10.1007/978-981-19-8765-6_8)
```


```{figure} ../resources/w06-img/kde_example_2.png
:label:
:alt:
:align: center

Example of Spatial KDE visualisation: [Xia et al. 2024](https://doi.org/10.1186/s40494-024-01499-5)
```


```{figure} ../resources/w06-img/kde_example_4.png
:label:
:alt:
:align: center

Example of Spatial KDE visualisation: [Wheeler 2014](https://andrewpwheeler.com/tag/kernel-density/)
```



```{figure} ../resources/w06-img/kde_example_3.png
:label:
:alt:
:align: center

Example of Spatial KDE visualisation: [Yang et al. 2019](https://doi.org/10.3390/ijgi8020093)
```


```{figure} ../resources/w06-img/kde_example_5.png
:label:
:alt:
:align: center

Example of Spatial KDE visualisation: [Kuo et al. 2012](https://api.semanticscholar.org/CorpusID:5968823)
```
<img src="resources/w06-img/kde_example_5.png" width="100%">
.footnote.small.square[

```{figure} ../resources/w06-img/kde_example_6.png
:label:
:alt:
:align: center

Example of Spatial KDE visualisation: [Levine 2013](https://www.ojp.gov/pdffiles1/nij/grants/242960-242995.pdf)
```


## Edge Effects
Edge effects in KDE refer to the bias and inaccuracy in density estimates near the boundary of the study area due to the lack of data beyond the edges.

```{figure} ../resources/w06-img/cat_outdoor_activity.png
:label:
:alt:
:align: center

Effects of the edges where the external data is not included.
```

### Methods addressing edge effects
- **Reflection Method**: Mirror the data points across the boundary, creating a new set of points outside the study area. Apply KDE to this extended dataset, ensuring the density estimates near the boundary are influenced by the reflected points, reducing edge effects.
- **Gaussian Truncation**: Truncate the Gaussian kernel function used in KDE at the boundary of the study area. This method eliminates the need to make assumptions about the data beyond the boundary, as the truncated kernel function only considers the points within the study area.
- **Adaptive Kernel Methods**: Utilize adaptive kernel functions, where the kernel shape and bandwidth vary based on the local density of points. By adapting to the local density, these methods can help reduce edge effects and produce more accurate density estimates near the boundary.
- **Boundary Correction Methods**: Apply boundary correction methods, such as the bias-correction method proposed by Chen and Firth (2000), which adjusts the density estimates near the boundary to compensate for edge effects.
- **Expansion of the Study Area**: Expand the study area beyond the original boundary, ensuring that the kernel function extends beyond the actual area of interest. This approach eliminates edge effects but may introduce uncertainty in density estimates for areas without data.


## Advanced Techniques and Applications
- Dual KDE
- Space-time KDE
- Network KDE

### Dual KDE

```{figure} ../resources/w06-img/advanced_dualkde.png
:label:
:alt:
:align: center

See [Jansenberger & Staufer-Steinnocher 2004](https://www.researchgate.net/publication/252791884_Dual_Kernel_Density_Estimation_as_a_Method_for_Describing_Spatio-Temporal_Changes_in_the_Upper_Austrian_Food_Retailing_Market) for more details
```


### Space-time KDE

```{figure} ../resources/w06-img/advanced_stkde.png
:label:
:alt:
:align: center

See [Hu et al. 2018](https://doi.org/10.1016/j.apgeog.2018.08.001) for more details
```


### Network KDE

```{figure} ../resources/w06-img/advanced_nkde.png
:label:
:alt:
:align: center

See [Tang et al. 2016](https://doi.org/10.1080/13658816.2015.1119279) for more details
```


## Summary

- **Introduction**: Spatial KDE is an extension of KDE for analyzing spatial data, focusing on patterns, trends, and density variations within a geographic context.
- **Applications**: Spatial KDE is widely used in fields like ecology, crime analysis, epidemiology, and urban planning to identify hot spots, clusters, and spatial relationships.
- **Spatial Adaptations**: Spatial KDE adapts traditional KDE by incorporating techniques to handle edge effects and the specific characteristics of spatial data.
- **Kernel Functions**: Different kernel functions can be used in spatial KDE to accommodate various data distributions and spatial patterns, ensuring accurate density estimation.
- **Bandwidth Selection**: Choosing an appropriate bandwidth for spatial KDE is crucial for accurate density estimation and pattern identification. Methods include rule-of-thumb, cross-validation, and plug-in approaches.
- **Visualization**: Spatial KDE results are typically visualized as heatmaps, contour plots, or 3D surfaces to facilitate interpretation and communication of spatial patterns and trends.


### Capturing Local Point Patterns with Spatial KDE

- Spatial KDE is an effective method for capturing and visualizing local point patterns in spatial data.
- By estimating density using a moving kernel window, spatial KDE highlights areas of high and low concentration within the study area.
- Bandwidth selection plays a crucial role in capturing local point patterns, as it controls the level of smoothing and the size of the local neighborhood considered in the density estimate.
- Smaller bandwidths capture finer details and local variations, while larger bandwidths highlight broader spatial trends and regional differences.
- Visualizing spatial KDE results as heatmaps or contour plots allows for easy identification of hotspots, clusters, and spatial relationships within the data.
- Spatial KDE does not provide related statistical tests to assess the significance level of the identified patterns or differences between point patterns. Additional statistical methods may be required for a more comprehensive analysis.
