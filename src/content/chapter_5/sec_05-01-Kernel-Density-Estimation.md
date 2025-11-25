# Kernel Density Estimation

## The conceptual definition

Kernel Density Estimation (KDE) is a _non-parametric technique_ for estimating the probability density function---_the kernel function_---of a continuous variable. KDE is widely used in various fields, such as statistical analysis, machine learning, and data visualization. The main idea behind KDE is _to represent the underlying probability distribution_ of a dataset by summing up the influence of individual data points.

## Key properties

- **Non-parametric approach**: KDE does not assume a specific underlying distribution for the data, making it suitable for various types of data distributions.
- **Smoothing technique**: KDE applies a kernel function (e.g., a Gaussian or Epanechnikov kernel) to smooth the input data, resulting in a continuous density estimate.
- **Bandwidth selection**: A crucial aspect of KDE is choosing an appropriate bandwidth or smoothing parameter, which controls the degree of smoothing applied to the data. Optimal bandwidth selection methods, such as cross-validation or plug-in methods, help to balance bias and variance in the density estimate.
- **Multivariate extension**: KDE can be extended to handle multivariate (multi-dimensions) data, providing a way to visualize and analyze the relationships between multiple variables in a dataset.


## Probability Density Function

- A probability density function (PDF) represents the distribution of a continuous random variable, depicting the likelihood of observing values in a given range.
- PDFs provide a comprehensive understanding of the underlying data distribution, including its central tendency, variability, and shape.
- They are essential for various data analysis tasks, such as data visualization, outlier detection, and statistical inference.


```{figure} ../resources/w02-img/frequency_distribution_pdf_cdf.png
:label:
:alt:
:align: center

Remember that we have talked about this in an earlier chapter?
```


### Limitations of Parametric Density Estimation Approaches

- Parametric density estimation methods assume that the data follows a specific probability distribution, such as the normal (Gaussian) or exponential distribution.
- These methods estimate the distribution parameters (e.g., mean, variance) to characterize the data and make further inferences.
- However, the performance of parametric methods _heavily relies on the correctness of the assumed distribution, which may not always hold true for real-world datasets_.
- Incorrect distribution assumptions can lead to biased results and misinterpretations of the data.



### The Need for a Flexible and Data-Driven Approach like KDE

- KDE is a non-parametric method for estimating probability density functions directly from the data.
- KDE does not require strong assumptions about the underlying distribution of the data, making it more flexible and adaptable to various data types and scenarios.
- KDE's data-driven approach allows it to capture complex and irregular features in the data distribution, which may be missed by parametric methods.
- By avoiding distribution assumptions, KDE helps mitigate the risk of obtaining misleading results due to incorrect assumptions.
- This flexibility and data-driven nature make KDE an attractive choice for a wide range of data analysis tasks, particularly when the underlying distribution is unknown or complex.

_In simple words, KDE is a data-driven way to approximate the PDF of data._



## Kernel Functions and their properties

A kernel function is a mathematical function used in KDE _to assign weights to data points based on their distances from a location of interest_.

Kernel functions are characterized by several properties:
- **Symmetry**: The kernel function should be symmetric around the origin, ensuring equal weighting for points equidistant from the location of interest.
- **Non-negativity**: The kernel function should yield non-negative weights, preventing the occurrence of negative density values.
- **Integration to 1**: The kernel function should integrate to 1 over its domain, ensuring that the total density estimated across the entire range of the data sums to 1.


## How KDE works
Approach one (from point to space):
1. For every data point, draw a kernel, i.e., the red dashed lines in left figure.
2. Stack the kernels if they overlapped, i.e., the blue solid line.

Approach two (from space to point):
1. For every space unit (x-axis), draw a kernel.
2. Identify data points that fall within the kernel range.
3. Measure the distance from data point to the space unit.
4. Convert the distance to weight using kernel function.
5. Sum the weight through all identified points in step 2.


```{figure} ../resources/w06-img/kde_in_1_dim_wiki.png
:label:
:alt:
:align: center

A histogram and KDE plot. Image source: [Wikipedia](https://en.wikipedia.org/wiki/Kernel_density_estimation)
```

```{figure} ../resources/w06-img/summing_kde_1D_b.png
:label:
:alt:
:align: center

How KDE work: by summing the density value.
```


### Common Kernel Functions
- Gaussian kernel
- Epanechnikov/Parabolic kernel
- Quartic (biweight) kernel
- Triangular kernel
- Uniform kernel


#### Gaussian (normal) kernel

The Gaussian kernel follows a bell-shaped curve and is widely used due to its smoothness and differentiability. Its formula is given by:

$$
K(x) = \frac{1}{h\times \sqrt{2\pi}} \times e^{-0.5(x/h)^2}
$$

```{figure} ../resources/w06-img/gauss_kernel.png
:label:
:alt:
:align: center

Gaussian Kernel, bandwidth (h) set as 1.
```



#### Epanechnikov (parabolic) kernel

The Epanechnikov kernel is optimal for some statistical properties and has a compact support, meaning it assigns zero weight to points outside a specific range. Its formula is:

$$
K(x) =
\begin{cases}
\frac{3}{4h} \times (1 - (x / h)^2) & \text{if -h ≤ x ≤ h} \\\\
0 & \text{otherwise} \\
\end{cases}
$$

```{figure} ../resources/w06-img/parabolic_kernel.png
:label:
:alt:
:align: center

Epanechnikov Kernel, bandwidth (h) set as 1.
```

#### Quartic (biweight) kernel

The Quartic kernel function is another commonly used kernel function in Kernel Density Estimation (KDE). It is defined as follows:

$$
K(x) =
\begin{cases}
\frac{15}{16h} \times (1 - (x / h)^2)^2  & \text{if -h ≤ x ≤ h} \\\\
0 & \text{otherwise} \\
\end{cases}
$$

```{figure} ../resources/w06-img/quartic_kernel.png
:label:
:alt:
:align: center

Quartic Kernel, bandwidth (h) set as 1.
```

#### Triangular kernel

The Triangular kernel function is a simple and computationally efficient kernel that assigns weights to points based on a triangular shape. It is defined as:

$$
K(x) =
\begin{cases}
\frac{1 - |x/h|}{h} & \text{if -h ≤ x ≤ h} \\\\
0 & \text{otherwise} \\
\end{cases}
$$

```{figure} ../resources/w06-img/triangular_kernel.png
:label:
:alt:
:align: center

Triangular Kernel, bandwidth (h) set as 1.
```


#### Uniform (Tophat) kernel

The uniform kernel assigns equal weights to points within a specific range and zero weight outside that range. Its formula is:

$$
K(x) =
\begin{cases}
\frac{1}{2h} & \text{if -h ≤ x ≤ h} \\\\
0 & \text{otherwise} \\
\end{cases}
$$

```{figure} ../resources/w06-img/uniform_kernel.png
:label:
:alt:
:align: center

Uniform Kernel, bandwidth (h) set as 1.
```



### The effect of Bandwidth


```{figure} ../resources/w06-img/demo_bandwidth.png
:label:
:alt:
:align: center

Effect of bandwidth (h) on Kernel Function (weighting).
```


```{figure} ../resources/w06-img/demo_bandwidth_dif.png
:label:
:alt:
:align: center

Effect of bandwidth (h) on 1-D KDE results.
```


### Bandwidth Selection

- Rule of Thumb
- Cross-Validation
- Plug-in Methods
- Visual Inspection

#### Rule of Thumb
- Silverman's rule: For a Gaussian kernel,

$h \approx 1.06 \times \sigma \times n^{-1/5}$,

where $\sigma$ is the _standard deviation of the data_, and $n$ is the _number of data points_.

- Other heuristics exist for different kernel functions and data dimensions. These rules provide quick estimates but may not be optimal for all datasets.


#### Cross-Validation
- Partition the data into several training sets.
- Apply KDE with different bandwidth values to the training set and full dataset.
- Calculate the error (MAE, MSE, etc.) between the estimated density and full data set density.
- Choose the bandwidth that minimizes the error.
- This method is more computationally intensive but provides a more data-driven bandwidth selection.


```{figure} ../resources/w06-img/k-fold-validation2.png
:label:
:alt:
:align: center

5-fold cross-validation approach.
```

#### Plug-in Methods
- These methods, such as Least Squares Cross-Validation (LSCV), directly estimate the optimal bandwidth by minimizing an approximation of the Mean Integrated Squared Error (MISE).
- Plug-in methods are more complex but can provide better bandwidth estimates in certain scenarios.

#### Visual Inspection
- Plot KDE with different bandwidth values and visually inspect the resulting density estimates.
- Choose the bandwidth that produces a density estimate that best captures the underlying structure and trends in the data. This method is subjective and relies on human judgment.

#### Remarks
- In practice, you can start with a _rule-of-thumb_ estimate, then refine it using _cross-validation_ or _plug-in_ methods, and finally perform _visual inspection_ to confirm the selected bandwidth's appropriateness.
- Remember that the best bandwidth may vary depending on the specific data and application.


### Advantages of KDE

- **Non-parametric**: Does not assume a specific distribution for the data.
- **Versatile**: Works with various data types and dimensions.
- **Flexible**: Handles complex data structures and multimodal distributions.
- **Smoothness**: Produces smooth, continuous density estimates.
- **Adaptive**: Bandwidth selection allows for control over smoothing.
- **Intuitive interpretation**: Visualization of the density estimate is straightforward.
- **Wide availability**: Implemented in many statistical software packages and libraries.



### Disadvantages/ Limitations of KDE

- **Bandwidth selection**: Can be challenging and affect the quality of the density estimate.
- **Computational complexity**: High-dimensional data can make KDE computationally demanding.
- **Boundary bias**: Density estimates can be biased near the boundary of the data.
- **Curse of dimensionality**: Performance deteriorates as the dimension of the data increases.
- **Sensitivity to outliers**: KDE can be influenced by outliers or data sparsity.
- **Interpretation**: Understanding the shape of the density estimate can be subjective.
- **Lack of model**: KDE does not provide a parametric model that can be used for further analysis.


### KDE: Visualizing Data Distribution


```{figure} ../resources/w06-img/KDE_line_fill_plot.png
:label:
:alt:
:align: center

Line fill plot.
```


```{figure} ../resources/w06-img/kde_contour_3species.png
:label:
:alt:
:align: center

Contour lines.
```


```{figure} ../resources/w06-img/kde_contour_line.png
:label:
:alt:
:align: center

Contour lines on Facet Grid with single KDE line on the diagonal.
```


```{figure} ../resources/w06-img/kde_hist_contour.png
:label:
:alt:
:align: center

Contour lines on Facet Grid with the histograme of single vector on the diagonal.
```



## Advanced Topics
Kernel Density Estimation (KDE) has several advanced topics that can be explored for a deeper understanding and more effective application. Here are some of these topics:

1) Adaptive Bandwidth Selection: This involves using _different bandwidths for different regions_ of the data space, based on local density or other data characteristics. It can improve KDE performance for datasets with varying density and complex structures.

2) Multivariate KDE: Extending KDE to multivariate data _involves selecting appropriate kernel functions and bandwidths in multiple dimensions._ Handling the curse of dimensionality and the increased computational complexity are important considerations.

3) Kernel Choice: _Different kernel functions_ can yield different KDE results, and understanding their properties, such as order, continuity, and bias, can guide kernel selection for specific applications.

4) Density Derivatives: Estimating density derivatives (e.g., gradient, Hessian) using KDE can provide additional insights into the data, such as _local maxima and saddle points_. This is particularly useful in optimization and feature detection tasks.

5) Kernel Smoothing in Regression: KDE can be used for nonparametric regression by _locally smoothing_ the data using kernel functions. Nadaraya-Watson and Local Linear Regression are examples of such methods.

6) Advanced KDE Algorithms: Techniques like Fast Fourier Transform (FFT) or K-D Trees can _speed up] KDE computations for large datasets, while advanced KDE methods like Variable Kernel Density Estimation (VKDE) or Bayesian KDE can _handle complex data structures and uncertainty_ in the density estimates.


## Summary

- Kernel Density Estimation (KDE) is a non-parametric method to _estimate the probability density function_ of continuous random variables.

- KDE works by _summing kernel functions centered at each data point_, resulting in a smooth density estimate.

- Key components of KDE include selecting an _appropriate kernel function and bandwidth_.

- KDE has numerous _applications_, such as data visualization, outlier detection, and data comparison.

- Advanced topics in KDE include _adaptive bandwidth selection_, multivariate KDE, and handling the _curse of dimensionality_.
