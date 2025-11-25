# Local Point Pattern

## What was covered in previous section

- Point Patterns
- Complete Spatial Randomness
- Methods for differentiating various types of point patterns:
    - clustered,
    - random,
    - dispersed

The main purpose and testing hypothesis is:
Does the entire/overall pattern of point data present some sort of __non-random__ pattern?

It does not answer __WHERE__ the pattern occurs.


## Global Analysis and Local Analysis

- .bold[Terminology]: The term '.red[GLOBAL]' refers to the .red[scale of analysis], which encompasses the .red[entire study area], rather than implying an .red[analysis at the Earth's scale].
- .bold[Holistic perspective]: Global analysis provides an .red[overall view] of the spatial patterns or trends across the entire study area, enabling a comprehensive understanding of the phenomena under investigation.
    - Is the crime incidences clustered within the study area?
- .bold[Spatial autocorrelation]: Global analysis can detect global spatial autocorrelation, a measure of .red[how similar or dissimilar the values] of a given attribute .red[are in nearby locations].
    - Do places with more crime incidences near to other places with more crime incidences?
- .bold[Spatial heterogeneity]: It helps identify global spatial heterogeneity, or .red[the variation of a given attribute across the study area], providing insights into the distribution patterns of the phenomena.
    - Is the crime rate similar across the study area?
    - Is the crime rate (non-)uniform within the study area?
- .bold[Modeling and prediction]: Global analysis aids .red[in developing statistical models and predictions for the entire study area] by incorporating spatial autocorrelation and heterogeneity into the analysis.
- .bold[Scale considerations]: The results of global analysis may depend on .red[the scale or resolution of the study area], highlighting the importance of selecting appropriate spatial scales for the analysis.
]]

---
class: left, middle

### Global Analysis

Think of a regression model---any model. .red.xkcd[Would you focus on a single data point or a subset of data points?]

In most cases, when working with regression models, we .red[do not focus on the characteristics of a single or a few individual data points]. Instead, we pay attention to the .red[overall 'pattern' that emerges when considering the entire dataset]. This pattern allows us to calculate crucial components such as regression coefficients ($\beta$), their significance, and relevant statistical tests like $r^2$, pseudo $r^2$, AIC, and others.

By examining the .red[collective behavior] of the data points, we can gain insights into the underlying relationships between variables, assess the model's performance, and make informed predictions or decisions based on the model's output. In other words, .red[a 'global' understanding] of the entire dataset.


---
class: center, middle

<img src="resources/w04-img/spatial_patterns_3_basic.png" width="100%">

.red.square[Is it clustered? not-clustered? random?]

---
class: left, middle

.split-40[.column[
### Local Analysis

As geographers, we are not satisfied with the global understanding, we also want to know .red['where'].

].column[
#### What is Local Analysis
- .bold[Local pattern]: Local analysis focuses on .red[identifying patterns or trends within specific local areas or neighborhoods] in the study region.

- .bold[Spatial Heterogeneity]: It explores spatial variations by examining how a given attribute behaves differently across various locations in the study area.

- .bold[Identification of location]: Local analysis is crucial for understanding the nuances of spatial data and identifying specific regions that require targeted interventions or further investigation.
]]

---
class: left, middle

.split-40[.column[
### Local Analysis
].column[
#### Key aspects of local analysis include:
- .bold[Detection of local clusters]: Identifying regions with high or low concentrations of a given attribute, also known as hot spots and cold spots, respectively.

- .bold[Local spatial autocorrelation]: Evaluating how similar or dissimilar the values of a given attribute are in nearby locations within specific local areas.

- .bold[Scale-dependent patterns]: Investigating how local patterns change with different spatial scales or resolutions.

- .bold[Finer details]: Local analysis complements global analysis by providing insights into the finer details of spatial patterns and helping to develop more targeted strategies and solutions for different parts of the study area.
]]

---
class: left, middle

### Local Analysis
The aim of local analysis in geospatial visualization and statistics is .red[to identify local patterns and spatial variations] by examining how a given attribute .red[behaves differently across various locations] in the study area. This includes understanding the interaction between nearby spatial units and .red[detecting clusters or hot spots] where the concentration of the attribute is .red[significantly] high or low compared to the surrounding areas.

.red[.bold[Local] Spatial Analysis is to answer the question of .bold[WHERE are the clusters]?]

.red[.bold[Global] Spatial Analysis is about the question of .bold[WHAT is the pattern]?]

---
class: left, middle

.split-30[.column[
### Local Analysis - HOW?
].column[
Common methods for Local Spatial Analysis include:
- Local Indicators of Spatial Association (LISA) for areal data
    - Local Moran's I
    - Local Geary's C
    - Local Getis-Ord Gi*

- Kernel Density Estimation
