# Kernel Density Estimation
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
