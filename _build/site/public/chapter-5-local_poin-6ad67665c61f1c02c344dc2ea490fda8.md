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

- **Terminology**: The term '__GLOBAL__' refers to the __scale of analysis__, which encompasses the __entire study area__, rather than implying an __analysis at the Earth's scale__.
- **Holistic perspective**: Global analysis provides an __overall view__ of the spatial patterns or trends across the entire study area, enabling a comprehensive understanding of the phenomena under investigation.
    - Is the crime incidences clustered within the study area?
- **Spatial autocorrelation**: Global analysis can detect global spatial autocorrelation, a measure of _how similar or dissimilar the values_ of a given attribute .red[are in nearby locations].
    - Do places with more crime incidences near to other places with more crime incidences?
- **Spatial heterogeneity**: It helps identify global spatial heterogeneity, or .red[the variation of a given attribute across the study area], providing insights into the distribution patterns of the phenomena.
    - Is the crime rate similar across the study area?
    - Is the crime rate (non-)uniform within the study area?
- **Modeling and prediction**: Global analysis aids .red[in developing statistical models and predictions for the entire study area] by incorporating spatial autocorrelation and heterogeneity into the analysis.
- **Scale considerations**: The results of global analysis may depend on .red[the scale or resolution of the study area], highlighting the importance of selecting appropriate spatial scales for the analysis.
]]

---
class: left, middle

### Global Analysis

Think of a regression model---any model. __Would you focus on a single data point or a subset of data points?__

In most cases, when working with regression models, we __do not focus on the characteristics of a single or a few individual data points__. Instead, we pay attention to the __overall 'pattern' that emerges when considering the entire dataset__. This pattern allows us to calculate crucial components such as regression coefficients ($\beta$), their significance, and relevant statistical tests like $r^2$, pseudo $r^2$, AIC, and others.

By examining the __collective behavior__ of the data points, we can gain insights into the underlying relationships between variables, assess the model's performance, and make informed predictions or decisions based on the model's output. In other words, __a 'global' understanding__ of the entire dataset.


<img src="../resources/w04-img/spatial_patterns_3_basic.png" width="100%">

Is it clustered? not-clustered? random?





## Local Analysis

As geographers, we are not satisfied with the global understanding, we also want to know __'where'__.

**What is Local Analysis**

- **Local pattern**: Local analysis focuses on .red[identifying patterns or trends within specific local areas or neighborhoods] in the study region.

- **Spatial Heterogeneity**: It explores spatial variations by examining how a given attribute behaves differently across various locations in the study area.

- **Identification of location**: Local analysis is crucial for understanding the nuances of spatial data and identifying specific regions that require targeted interventions or further investigation.


Key aspects of local analysis include:
- **Detection of local clusters**: Identifying regions with high or low concentrations of a given attribute, also known as hot spots and cold spots, respectively.

- **Local spatial autocorrelation**: Evaluating how similar or dissimilar the values of a given attribute are in nearby locations within specific local areas.

- **Scale-dependent patterns**: Investigating how local patterns change with different spatial scales or resolutions.

- **Finer details**: Local analysis complements global analysis by providing insights into the finer details of spatial patterns and helping to develop more targeted strategies and solutions for different parts of the study area.


The aim of local analysis in geospatial visualization and statistics is .red[to identify local patterns and spatial variations] by examining how a given attribute .red[behaves differently across various locations] in the study area. This includes understanding the interaction between nearby spatial units and .red[detecting clusters or hot spots] where the concentration of the attribute is .red[significantly] high or low compared to the surrounding areas.

In other words:
- **Local** Spatial Analysis is to answer the question of __WHERE are the clusters__?
- **Global** Spatial Analysis is about the question of __WHAT is the pattern__?


## Local Analysis - HOW?

Common methods for Local Spatial Analysis include:
- Local Indicators of Spatial Association (LISA) for areal data
    - Local Moran's I
    - Local Geary's C
    - Local Getis-Ord Gi*

- Kernel Density Estimation
