slide_title: Week 06 - Point Pattern II: Kernel Density Estimation for Spatial Data
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

## Point Pattern II: Kernel Density Estimation for Spatial Data
------

<br />

.x-large.bold[Dr. CHIN Wei Chien Benny]  
[.underline.square[wcchin@nus.edu.sg]]  

.headnote.square.bold.x-large[GE5230 Geospatial Statistics and Visualization]
.footnote.square[06 @ 2025-09-18 Department of Geography, NUS]

---
layout: false
class: left, middle

.split-10[.column[].column[
### Two Types Clustering in Spatial Analysis

1. some parts of the study area that have very .red.bold[high concentration of point events],  
i.e., .red['clusters']
    - to check if this phenomenon exists in the spatial point data
    - to identify the location of these clusters
    - significant tests, CSR

2. .red.bold[groups of spatial points] that are close to each other, i.e., .red['clusters']
    - identify grouping of points with/without overlap


Same as last week, today's lecture focus on the .underline[first 'clustering' analysis].

]]

---
class: left, middle
## Objectives of this lecture
- To be aware of the .red[Global] Pattern and .red[Local] Pattern
- To understand the .red[1D Kernel Density Estimation]
- To learn the 2D .red[Spatial] Kernel Density Estimation

---
class: center, middle, inverse

.xx-large.bold.wide[PART 1]
## Global Pattern and Local Pattern
------
.square[Global Pattern .dot[] Local Pattern]

.headnote.square.bold.x-large[Point Pattern II]

---
class: left, middle
.split-30[.column[
### What have we learnt previous weeks?

].column[
- Point Patterns
- Complete Spatial Randomness
- Methods for differentiating various types of point patterns:
    - clustered, 
    - random, 
    - dispersed

The main purpose and testing hypothesis is:  
.bold[Does the entire/overall pattern of point data present some sort of  
.red[non-random] pattern?]  
.xkcd.red[It does not answer .bold[WHERE] the pattern occurs.]
]]

---
class: left, middle

.split-20[.column[
### Global Analysis
].column[
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
- Local Indicators of Spatial Association (LISA)
    - Local Moran's I
    - Local Geary's C
    - Local Getis-Ord Gi*

- Kernel Density Estimation
]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 2]
## Kernel Density Estimation
------
.square[KDE .dot[] Properties .dot[] How .dot[]  Kernel Function .dot[] Bandwidth .dot[] Advanced]

.headnote.square.bold.x-large[Point Pattern II]

---
class: left, middle

### Kernel Density Estimation - the conceptual definition

Kernel Density Estimation (KDE) is a .red[non-parametric technique] for estimating the probability density function---.red[the kernel function]---of a continuous variable. KDE is widely used in various fields, such as statistical analysis, machine learning, and data visualization. The main idea behind KDE is .red[to represent the underlying probability distribution] of a dataset by summing up the influence of individual data points.

---
class: left, middle
.split-30[.column[
### Kernel Density Estimation - key properties
].column[
- .bold[Non-parametric approach]: KDE does not assume a specific underlying distribution for the data, making it suitable for various types of data distributions.
- .bold[Smoothing technique]: KDE applies a kernel function (e.g., a Gaussian or Epanechnikov kernel) to smooth the input data, resulting in a continuous density estimate.
- .bold[Bandwidth selection]: A crucial aspect of KDE is choosing an appropriate bandwidth or smoothing parameter, which controls the degree of smoothing applied to the data. Optimal bandwidth selection methods, such as cross-validation or plug-in methods, help to balance bias and variance in the density estimate.
- .bold[Multivariate extension]: KDE can be extended to handle multivariate (multi-dimensions) data, providing a way to visualize and analyze the relationships between multiple variables in a dataset.
]]

---
class: left, middle

### Probability Density Function
<img src="resources/w02-img/frequency_distribution_pdf_cdf.png" width="90%">

- A probability density function (PDF) represents the distribution of a continuous random variable, depicting the likelihood of observing values in a given range.
- PDFs provide a comprehensive understanding of the underlying data distribution, including its central tendency, variability, and shape.
- They are essential for various data analysis tasks, such as data visualization, outlier detection, and statistical inference.

---
class: left, middle
.split-30[.column[
### Limitations of Parametric Density Estimation Approaches
].column[
- Parametric density estimation methods assume that the data follows a specific probability distribution, such as the normal (Gaussian) or exponential distribution.
- These methods estimate the distribution parameters (e.g., mean, variance) to characterize the data and make further inferences.
- However, the performance of parametric methods .red[heavily relies on the correctness of the assumed distribution, which may not always hold true for real-world datasets].
- Incorrect distribution assumptions can lead to biased results and misinterpretations of the data.
]]

---
class: left, middle
.split-30[.column[
### The Need for a Flexible and Data-Driven Approach like KDE
].column[
- KDE is a non-parametric method for estimating probability density functions directly from the data.
- KDE does not require strong assumptions about the underlying distribution of the data, making it more flexible and adaptable to various data types and scenarios.
- KDE's data-driven approach allows it to capture complex and irregular features in the data distribution, which may be missed by parametric methods.
- By avoiding distribution assumptions, KDE helps mitigate the risk of obtaining misleading results due to incorrect assumptions.
- This flexibility and data-driven nature make KDE an attractive choice for a wide range of data analysis tasks, particularly when the underlying distribution is unknown or complex.

.xkcd[In simple words, KDE is a data-driven way to approximate the PDF of data.] 
]]

---
class: left, middle
.split-30[.column[
### Definition of Kernel Functions and their properties
].column[
A kernel function is a mathematical function used in KDE .red[to assign weights to data points based on their distances from a location of interest].

Kernel functions are characterized by several properties:
- .bold[Symmetry]: The kernel function should be symmetric around the origin, ensuring equal weighting for points equidistant from the location of interest.
- .bold[Non-negativity]: The kernel function should yield non-negative weights, preventing the occurrence of negative density values.
- .bold[Integration to 1]: The kernel function should integrate to 1 over its domain, ensuring that the total density estimated across the entire range of the data sums to 1.
]]

---
class: left, middle
.split-50[.column[
### How KDE works
Approach one (from point to space):
1. For every data point, draw a kernel, i.e., the red dashed lines in left figure.
2. Stack the kernels if they overlapped, i.e., the blue solid line. 

Approach two (from space to point):
1. For every space unit (x-axis), draw a kernel.
2. Identify data points that fall within the kernel range.
3. Measure the distance from data point to the space unit.
4. Convert the distance to weight using kernel function.
5. Sum the weight through all identified points in step 2. 

].column[
<img src="resources/w06-img/kde_in_1_dim_wiki.png" width="100%">

A histogram and KDE plot. .small.square[Image source: [Wikipedia](https://en.wikipedia.org/wiki/Kernel_density_estimation)]

]]

---
class: center, middle

.headnote.bold[How KDE works]
<img src="resources/w06-img/summing_kde_1D_b.png" width="85%">

---
class: left, middle
.split-30[.column[
### Common Kernel Functions
- .red[Gaussian kernel]
- Epanechnikov/Parabolic kernel
- Quartic (biweight) kernel
- Triangular kernel
- Uniform kernel
].column[
.bold[Gaussian (normal) kernel]:  
The Gaussian kernel follows a bell-shaped curve and is widely used due to its smoothness and differentiability. Its formula is given by:

$$
K(x) = \frac{1}{h\times \sqrt{2\pi}} \times e^{-0.5(x/h)^2} 
$$

<img src="resources/w06-img/gauss_kernel.png" width="60%">

.xkcd[bandwidth (h) set as 1]
]]

---
class: left, middle
.split-30[.column[
### Common Kernel Functions
- Gaussian kernel
- .red[Epanechnikov/Parabolic kernel]
- Quartic (biweight) kernel
- Triangular kernel
- Uniform kernel
].column[
.bold[Epanechnikov (parabolic) kernel]:  
The Epanechnikov kernel is optimal for some statistical properties and has a compact support, meaning it assigns zero weight to points outside a specific range. Its formula is:
$$
K(x) =
\begin{cases}
\frac{3}{4h} \times (1 - (x / h)^2) & \text{if -h ≤ x ≤ h} \\\\
0 & \text{otherwise} \\
\end{cases}
$$
<img src="resources/w06-img/parabolic_kernel.png" width="60%">

.xkcd[bandwidth (h) set as 1]
]]

---
class: left, middle
.split-30[.column[
### Common Kernel Functions
- Gaussian kernel
- Epanechnikov/Parabolic kernel
- .red[Quartic (biweight) kernel]
- Triangular kernel
- Uniform kernel
].column[
.bold[Quartic (biweight) kernel]:  
The Quartic kernel function is another commonly used kernel function in Kernel Density Estimation (KDE). It is defined as follows:
$$
K(x) =
\begin{cases}
\frac{15}{16h} \times (1 - (x / h)^2)^2  & \text{if -h ≤ x ≤ h} \\\\
0 & \text{otherwise} \\
\end{cases}
$$
<img src="resources/w06-img/quartic_kernel.png" width="60%">

.xkcd[bandwidth (h) set as 1]
]]

---
class: left, middle
.split-30[.column[
### Common Kernel Functions
- Gaussian kernel
- Epanechnikov/Parabolic kernel
- Quartic (biweight) kernel
- .red[Triangular kernel]
- Uniform kernel
].column[
.bold[Triangular kernel]:  
The Triangular kernel function is a simple and computationally efficient kernel that assigns weights to points based on a triangular shape. It is defined as:
$$
K(x) =
\begin{cases}
\frac{1 - |x/h|}{h} & \text{if -h ≤ x ≤ h} \\\\
0 & \text{otherwise} \\
\end{cases}
$$
<img src="resources/w06-img/triangular_kernel.png" width="60%">

.xkcd[bandwidth (h) set as 1]
]]

---
class: left, middle
.split-30[.column[
### Common Kernel Functions
- Gaussian kernel
- Epanechnikov/Parabolic kernel
- Quartic (biweight) kernel
- Triangular kernel
- .red[Uniform kernel]
].column[
.bold[Uniform (Tophat) kernel]:  
The uniform kernel assigns equal weights to points within a specific range and zero weight outside that range. Its formula is:

$$
K(x) =
\begin{cases}
\frac{1}{2h} & \text{if -h ≤ x ≤ h} \\\\
0 & \text{otherwise} \\
\end{cases}
$$
<img src="resources/w06-img/uniform_kernel.png" width="60%">

.xkcd[bandwidth (h) set as 1]
]]

---
class: left, middle
.split-20[.column[

### The effect of Bandwidth
].column[
<img src="resources/w06-img/demo_bandwidth.png" width="100%">

.square[Effect of bandwidth (h) on Kernel Function (weighting).] 
]]

---
class: left, middle
.split-20[.column[
### The effect of Bandwidth
].column[
<img src="resources/w06-img/demo_bandwidth_dif.png" width="100%">

.square[Effect of bandwidth (h) on 1-D KDE results.] 
]]

---
class: left, middle

.split-30[.column[
### Bandwidth Selection
- .red[Rule of Thumb]
- Cross-Validation
- Plug-in Methods
- Visual Inspection
].column[
.bold[Rule of Thumb]:
- Silverman's rule: For a Gaussian kernel, 

$h \approx 1.06 \times \sigma \times n^{-1/5}$, 

where $\sigma$ is the .red[standard deviation of the data], and $n$ is the .red[number of data points].
- Other heuristics exist for different kernel functions and data dimensions. These rules provide quick estimates but may not be optimal for all datasets.

]]

---
class: left, middle

.split-30[.column[
### Bandwidth Selection
- Rule of Thumb
- .red[Cross-Validation]
- Plug-in Methods
- Visual Inspection
].column[
.bold[Cross-Validation]:
- Partition the data into several training sets.
- Apply KDE with different bandwidth values to the training set and full dataset. 
- Calculate the error (MAE, MSE, etc.) between the estimated density and full data set density.
- Choose the bandwidth that minimizes the error. 
- This method is more computationally intensive but provides a more data-driven bandwidth selection.

<img src="resources/w06-img/k-fold-validation2.png" width="70%">

]]

---
class: left, middle

.split-30[.column[
### Bandwidth Selection
- Rule of Thumb
- Cross-Validation
- .red[Plug-in Methods]
- .red[Visual Inspection]
].column[
.bold[Plug-in Methods]:
- These methods, such as Least Squares Cross-Validation (LSCV), directly estimate the optimal bandwidth by minimizing an approximation of the Mean Integrated Squared Error (MISE).
- Plug-in methods are more complex but can provide better bandwidth estimates in certain scenarios.

.bold[Visual Inspection]:
- Plot KDE with different bandwidth values and visually inspect the resulting density estimates.
- Choose the bandwidth that produces a density estimate that best captures the underlying structure and trends in the data. This method is subjective and relies on human judgment.

.bold[Remarks]:
- In practice, you can start with a .red[rule-of-thumb] estimate, then refine it using .red[cross-validation] or .red[plug-in] methods, and finally perform .red[visual inspection] to confirm the selected bandwidth's appropriateness. 
- Remember that the best bandwidth may vary depending on the specific data and application.
]]

---
class: left, middle

.split-30[.column[
### Advantages of KDE
].column[
- .bold[Non-parametric]: Does not assume a specific distribution for the data.
- .bold[Versatile]: Works with various data types and dimensions.
- .bold[Flexible]: Handles complex data structures and multimodal distributions.
- .bold[Smoothness]: Produces smooth, continuous density estimates.
- .bold[Adaptive]: Bandwidth selection allows for control over smoothing.
- .bold[Intuitive interpretation]: Visualization of the density estimate is straightforward.
- .bold[Wide availability]: Implemented in many statistical software packages and libraries.
]]

---
class: left, middle

.split-30[.column[
### Disadvantages/ Limitations of KDE
].column[
- .bold[Bandwidth selection]: Can be challenging and affect the quality of the density estimate.
- .bold[Computational complexity]: High-dimensional data can make KDE computationally demanding.
- .bold[Boundary bias]: Density estimates can be biased near the boundary of the data.
- .bold[Curse of dimensionality]: Performance deteriorates as the dimension of the data increases.
- .bold[Sensitivity to outliers]: KDE can be influenced by outliers or data sparsity.
- .bold[Interpretation]: Understanding the shape of the density estimate can be subjective.
- .bold[Lack of model]: KDE does not provide a parametric model that can be used for further analysis.
]]

---
class: center, middle

### KDE: Visualizing Data Distribution
.split-50[.column[
<img src="resources/w06-img/KDE_line_fill_plot.png" width="80%">
].column[
<img src="resources/w06-img/kde_contour_3species.png" width="80%">
]]

---
class: center, middle

### KDE: Visualizing Data Distribution
.split-50[.column[
<img src="resources/w06-img/kde_contour_line.png" width="100%">
].column[
<img src="resources/w06-img/kde_hist_contour.png" width="100%">
]]

---
class: left, middle

.split-30[.column[
### Advanced Topics
Kernel Density Estimation (KDE) has several advanced topics that can be explored for a deeper understanding and more effective application. Here are some of these topics:
].column[

1) Adaptive Bandwidth Selection: This involves using .red[different bandwidths for different regions] of the data space, based on local density or other data characteristics. It can improve KDE performance for datasets with varying density and complex structures.

2) Multivariate KDE: Extending KDE to multivariate data .red[involves selecting appropriate kernel functions and bandwidths in multiple dimensions.] Handling the curse of dimensionality and the increased computational complexity are important considerations.

3) Kernel Choice: .red[Different kernel functions] can yield different KDE results, and understanding their properties, such as order, continuity, and bias, can guide kernel selection for specific applications.

]]

---
class: left, middle

.split-30[.column[
### Advanced Topics
Kernel Density Estimation (KDE) has several advanced topics that can be explored for a deeper understanding and more effective application. Here are some of these topics:
].column[
4) Density Derivatives: Estimating density derivatives (e.g., gradient, Hessian) using KDE can provide additional insights into the data, such as .red[local maxima and saddle points]. This is particularly useful in optimization and feature detection tasks.

5) Kernel Smoothing in Regression: KDE can be used for nonparametric regression by .red[locally smoothing] the data using kernel functions. Nadaraya-Watson and Local Linear Regression are examples of such methods.

6) Advanced KDE Algorithms: Techniques like Fast Fourier Transform (FFT) or K-D Trees can .red[speed up] KDE computations for large datasets, while advanced KDE methods like Variable Kernel Density Estimation (VKDE) or Bayesian KDE can .red[handle complex data structures and uncertainty] in the density estimates.
]]

---
class: left, middle

.split-20[.column[
### Summary
].column[

- Kernel Density Estimation (KDE) is a non-parametric method to .red[estimate the probability density function] of continuous random variables.

- KDE works by .red[summing kernel functions centered at each data point], resulting in a smooth density estimate.

- Key components of KDE include selecting an .red[appropriate kernel function and bandwidth].

- KDE has numerous .red[applications], such as data visualization, outlier detection, and data comparison.

- Advanced topics in KDE include .rd[adaptive bandwidth selection], multivariate KDE, and handling the .red[curse of dimensionality].
]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 3]
## Spatial Kernel Density Estimation
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

---
class: center, middle, inverse

## Closing Remarks
------
.square[Local Pattern .dot[] KDE .dot[] Spatial KDE]

.headnote.square.bold.x-large[Point Pattern II]

---
class: left, middle
.split-30[.column[
### Capturing Local Point Patterns with Spatial KDE  
].column[

- Spatial KDE is an effective method for capturing and visualizing local point patterns in spatial data.
- By estimating density using a moving kernel window, spatial KDE highlights areas of high and low concentration within the study area.
- Bandwidth selection plays a crucial role in capturing local point patterns, as it controls the level of smoothing and the size of the local neighborhood considered in the density estimate.
- Smaller bandwidths capture finer details and local variations, while larger bandwidths highlight broader spatial trends and regional differences.
- Visualizing spatial KDE results as heatmaps or contour plots allows for easy identification of hotspots, clusters, and spatial relationships within the data.
- Spatial KDE does not provide related statistical tests to assess the significance level of the identified patterns or differences between point patterns. Additional statistical methods may be required for a more comprehensive analysis.
]]