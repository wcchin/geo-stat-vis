slide_title: Week 02 - Statistical Pattern I 
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

## Statistical Pattern I: Frequency Distribution, Data Transformation & Classification 
------

<br />

.x-large.bold[Dr. CHIN Wei Chien Benny]  
[.underline.square[wcchin@nus.edu.sg]]  

.headnote.square.bold.x-large[GE5230 Geospatial Statistics and Visualization]
.footnote.square[02 @ 2025-08-21 Department of Geography, NUS]

---
layout: false
class: left, middle
## Objectives of this lecture
- To know the basic steps of .bold[data preparation]
- To learn about .bold[frequency distribution] and how to visualize the data based on frequency distribution
- To learn about .bold[data transformation] techniques and when to use it
- To learn about .bold[data classification] and key things to consider when classifying data

---
class: center, middle, inverse

.xx-large.bold.wide[PART 1]
## Data Preparation 
------
.square[The Steps]

.headnote.square.bold.x-large[Statistical Pattern I]

---
class: center, middle

### What do you think is the .red[first step] of .red[data analysis]?

.xkcd[Yes, it is Data Preprocessing]

---
class: center, middle

### About Data Preprocessing

<img src="resources/w02-img/preprocessing_steps.drawio.png" width="70%" align="center">

.square[Data preprocessing process.]

---
class: left, middle

.split-40[.column[
### What to do after data collection

].column[
- Identifying structure
- Cleaning and Editing
- Coding
- Classification
- Transcription
- Alignment
- Tabulation
- Transformation
- Initial analysis

.xkcd[The steps are not sequential.
Sometimes, some steps are done repeatedly and iteratively.]
]]

---
class: left, middle

.split-40[.column[
### What to do after data collection
- .red[Identifying structure]
- Cleaning and Editing
- Coding
- Classification
- Transcription
- Alignment
- Tabulation
- Transformation
- Initial analysis

].column[
#### Identifying structure
.bold.blue[Look at the patterns]  
- What is/was the purpose for data collection?
- What is the design strategy of data collection?
- What is the structure/organization of the collected data? 

.bold.blue[Any expectations? Counter-intuitive patterns?]  
- Is there any (expected/unexpected) relationships between variables?
- Is there any (expected/unexpected) hierarchies?
- Is there any (expected/unexpected) groupings?

]]

---
class: left, middle

.split-40[.column[
### What to do after data collection
- Identifying structure
- .red[Cleaning and Editing]
- Coding
- Classification
- Transcription
- Alignment
- Tabulation
- Transformation
- Initial analysis

].column[
#### Data Cleaning & Editing
- Remove errors.
- Remove inconsistencies.
- Resolve duplicate entries.
- What to do with missing values (default values, inputation, interpolation, deletion)?
- What to do with outliers?
- Verify accuracy of individual data points. 
- Ensure data is complete and consistent.
- Use manual editing or automated data validation techniques.
- Correct typos or formatting issues.

.xkcd[.blue[Documenting]: write down the steps you took. ]
]]

---
class: left, middle

.split-40[.column[
### What to do after data collection
- Identifying structure
- Cleaning and Editing
- .red[Coding]
- Classification
- Transcription
- Alignment
- Tabulation
- Transformation
- Initial analysis

].column[
#### Coding
- Assign codes to qualitative data (e.g., survey responses), e.g.,
    - yes/no, true/false to 1 and 0 (or 1 and 2)
    - male/female to 1 and 0 (or 1 and 2)
    - ordered data, e.g., Very disagree, slightly disagree, neutral, slightly agree, very agree, to numbers (-2 to 2, or 0 to 4), etc.
    - categorical data, e.g., land use, land cover, urban functional zones, house types, to numbers (nominal).
- Create new variables based on existing ones, e.g., 
    - calculating age from year of birth,
    - 5 yo age groups from age,
    - income levels from gross income,
    - measuring differences (differences of magnitude vs. magnitude of differences).
- Use consistent coding schemes across various data sources.

.xkcd[.blue[Documenting]: write down the code definitions and rules. ]
]]

---

class: left, middle

.split-40[.column[
### What to do after data collection
- Identifying structure
- Cleaning and Editing
- Coding
- .red[Classification]
- Transcription
- Alignment
- Tabulation
- Transformation
- Initial analysis

].column[
#### Classification
- Organize data into predefined categories or classes.
- Define classification criteria or rules:
    - at what level of household income could be considered as 'high'/'medium'/'low' income
    - how many times a month can be considered high frequency
- Apply classification methods consistently:
    - natural break, head-tail break, quantiles, etc.
- Evaluate classification validity, accuracy and consistency.

.xkcd[.blue[Documenting]: write down the classification method and your reason. ]
]]

---

class: left, middle

.split-40[.column[
### What to do after data collection
- Identifying structure
- Cleaning and Editing
- Coding
- Classification
- .red[Transcription]
- Alignment
- Tabulation
- Transformation
- Initial analysis

].column[
#### Transcription
(mainly for qualitative data collection approach)
- Convert audio to text using speech-to-text software.
- Transcribe video content to text format.
- Extract text from images using OCR (Optical Character Recognition).
- Perform manual or automated transcription as needed.

]]

---

class: left, middle

.split-40[.column[
### What to do after data collection
- Identifying structure
- Cleaning and Editing
- Coding
- Classification
- Transcription
- .red[Alignment]
- Tabulation
- Transformation
- Initial analysis

].column[
#### Alignment
- Standardize formats, naming conventions, spatial scales, and units of measurement.
- Ensure compatibility between different data sources.
- Make sure the projections and anchor points are same. 
- Handle inconsistencies in data representation or encoding.

.xkcd[.blue[Documenting]: write down data alignment decisions and procedures. ]
]]

---

class: left, middle

.split-40[.column[
### What to do after data collection
- Identifying structure
- Cleaning and Editing
- Coding
- Classification
- Transcription
- Alignment
- .red[Tabulation]
- Transformation
- Initial analysis

].column[
#### Tabulation
- Summarize data into tables or cross-tabulations.
- Create join-able tables:
    - unique identifiers/keys for every person/location
    - split tables for participants' background, participants' perspective on XXX, participants' performance
- Facilitate exploratory data analysis (EDA) and reporting.
- Create pivot tables or aggregated data views.
- Present data in a clear and concise format.

]]

---
class: left, middle

.split-40[.column[
### What to do after data collection
- Identifying structure
- Data cleaning and Editing
- Coding
- Classification
- Transcription
- Alignment
- Tabulation
- .red[Transformation]
- Initial analysis

].column[

#### Transformation
- Apply appropriate transformations
- Address .red[skewness, non-linearity, or differing scales].
- Perform tests as needed (statistics assumptions for further analyses, etc.).
- .red[Normalize or standardize] data as needed.
- Monitor impact on data distribution and relationships.

.xkcd[.blue[Documenting]: write down the steps and reasons. ]
]]

---
class: left, middle

.split-40[.column[
### What to do after data collection
- Identifying structure
- Data cleaning and Editing
- Coding
- Classification
- Transcription
- Alignment
- Tabulation
- Transformation
- .red[Initial analysis]

].column[
#### Initial analysis
- Perform exploratory data analysis (EDA) to gain insights.
- Identify trends, patterns, or relationships in the data.
- Check assumptions for further analysis or modeling.
- Generate visualizations (e.g., histograms, scatter plots) to support EDA.

]]

---
class: left, middle

.split-30[.column[
### Summary
].column[
#### Data (Pre)Processing
- Identifying structure: .blue.bold[Looking for patterns]
- Cleaning and Editing: .blue.bold[Identifying and resolving issues]
- Coding: .blue.bold[Assigning values and meanings]
- Classification: .blue.bold[Grouping and categorizing data]
- Transcription: .blue.bold[Extracting relevant information]
- Alignment: .blue.bold[Standardizing data formats]
- Tabulation: .blue.bold[Creating a structured view of data]
- Transformation: .blue.bold[Manipulating data for analysis]
- Initial analysis: .blue.bold[Exploring patterns and trends]
]]

---
class: center, middle

<img src="resources/w01-img/drawing-how_maps_are_used.png" width="70%" align="center">

.square[MacEachren's cartographic cube.]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 2]
## Frequency Distribution
------
.square[The What .dot[] The Types .dot[] The Visualization]

.headnote.square.bold.x-large[Statistical Pattern I]

---
class: left, middle

.split-20[.column[
### Frequency Distribution?

].column[
#### Analyses start by viewing data.
How to .red['view'] the data?

.square[A slice of HDB data table. ]

| Street            | Flat Type   | Floor Area (sqm) |   Resale Age |   Resale Price |
|:------------------|------------:|-----------------:|-------------:|---------------:|
| ANG MO KIO AVE 10 | 2 ROOM      |               44 |           44 |         267000 |
| ANG MO KIO AVE 3  | 2 ROOM      |               49 |           46 |         300000 |
| ANG MO KIO AVE 3  | 2 ROOM      |               44 |           45 |         280000 |
| ANG MO KIO AVE 3  | 2 ROOM      |               44 |           45 |         282000 |
| ANG MO KIO AVE 4  | 2 ROOM      |               45 |           37 |         289800 |
|               ... |         ... |             ...  |          ... |            ... |

]
]

---
class: left, middle

.split-20[.column[
### Frequency Distribution?

].column[

#### Understanding frequency distribution
A frequency distribution is a representation, usually in the form of a table or graph, that .red[illustrates the number of occurrences] (frequency) of .red[each unique value] or .red[range of values] within a given dataset. This visual or tabular summary of data distribution allows us to understand the .red[spread, shape, and central tendency] of the data, providing initial understanding of the underlying patterns and structures in the dataset.
]]


---
class: left, middle

.split-40[.column[
### Frequency Distribution?

#### Examples of frequency distribution

And the measures of central tendency and spread.

(a): Bar chart (for discrete variable)  
(b): Histogram (for continuous variable)

].column[

<img src="resources/w02-img/frequency_distribution_demo_0.png" width="90%" align="center">  
.square[The frequency distribution of resale transactions by: (a) flat type and (b) resale price.]

]]

---
class: left, middle

.split-20[.column[
### Frequency Distribution and Density Function
#### Understanding PDF and CDF
].column[

.bold[Probability Density Function (PDF)]:
- A mathematical function representing the relative likelihood of observing a continuous random variable in a specific range of values.
- .red[PDFs have non-negative values, and their total area under the curve equals 1.]
- Different PDF shapes correspond to various probability distributions (e.g., normal, exponential).

.bold[Cumulative Distribution Function (CDF)]:
- Calculates the cumulative probability of a random variable being less than or equal to a given value.
- .red[The CDF value at a point x corresponds to the area under the PDF curve to the left of x.]
- CDFs are useful for assessing probabilities of events within a specific range.

The PDF and CDF are complementary tools in probability and statistics, providing insights into the distribution and likely outcomes of continuous random variables. PDFs offer a detailed view of relative likelihoods, while CDFs show the accumulated probabilities over a range of values. Together, they enable a comprehensive understanding of data distributions and facilitate various statistical analyses.

]]

---
class: center, middle

#### Understanding PDF and CDF

<img src="resources/w02-img/frequency_distribution_pdf_cdf.png" width="100%" align="center">  
.square[The (a) histogram, (b) PDF, and (c) CDF. In CDF, the x-axis value (167) that correspond to the y (density) value of 0.4 means that all the smaller values ($x<167$) contains 40% of the data points.]

The PDF here is estimated from an empirical data series using Kernel Density Estimation (aka KDE). 

If Y-axis shows count, then it should be a histogram, and if it shows 'density', then is should be either PDF or CDF. 

---
class: left, middle

.split-20[.column[
### Frequency Distribution?

#### Interpreting Frequency Distributions

].column[
Measure of .bold[Central Tendency] 
- Gravitational center: .red[mean], aka arithmetic mean
- Middle value: .red[median]
- Most frequent value: .red[mode]

Measure of .bold[Spread]
- Range and inter-quartile range
- Standard deviation and variance

Measure of .bold[Shape]
- .red[Symmetry]: Mirrored between left and right of central line
- .red[Skewness]: Has a long tail on right (positive skew) or left (negative skew)
- .red[Modality]: Number of peaks
- .red[Kurtosis]: Steepness of peak compared to a normal distribution

.xkcd[what are the other 'mean' besides 'arithmetic mean'?]

]]

---
class: center, middle

#### Interpreting Frequency Distributions (Symmetry)

<img src="resources/w02-img/frequency_distribution_symmetrical.png" width="100%" align="center">  
.square[Symmetrical shapes.]


---
class: center, middle

#### Interpreting Frequency Distributions (Asymmetry)

<img src="resources/w02-img/frequency_distribution_asymmetrical.png" width="100%" align="center">  
.square[Asymmetrical shapes.]

---
class: center, middle

#### Interpreting Frequency Distributions (Modality)

<img src="resources/w02-img/frequency_distribution_modality.png" width="100%" align="center">  
.square[Various modality shapes.]

---
class: center, middle

#### Interpreting Frequency Distributions (Kurtosis)

<img src="resources/w02-img/frequency_distribution_kurtosis.png" width="100%" align="center">  
.square[Various Kurtosis shapes.]

---
class: center, middle

#### Common Types of Frequency Distributions

<img src="resources/w02-img/frequency_distribution_3types.png" width="100%" align="center">  
.square[Three common types of distribution.]

---
class: left, middle

.split-50[.column[
#### Normal Distribution

The normal distribution, also known as the Gaussian distribution or the ".red[bell curve]," is often used to model .red[continuous variables] in various fields. It is particularly useful in statistics because of the .red[Central Limit Theorem], which states that the distribution of sample means approaches a normal distribution as the sample size increases. The normal distribution has applications in many areas, such as finance, psychology, and engineering.

Many real-world phenomena, such as heights, IQ scores, and measurement errors, tend to follow a normal distribution. As a result, the normal distribution plays a central role in statistics and is used as a basis for many statistical tests and analyses.

The normal distribution is defined by two parameters---the mean ($\mu$) and standard deviation ($\sigma$).

].column[
<img src="resources/w02-img/frequency_distribution_normal.png" width="100%" align="center">  
.square[Normal Distribution with various paramters ($\mu$ and $\sigma$).]

]]

---
class: left, middle

.split-50[.column[
<img src="resources/w02-img/frequency_distribution_poisson.png" width="100%" align="center">  
.square[Poisson Distribution with various paramters ($\lambda$).]
].column[
#### Poisson Distribution

The Poisson distribution is used to model .red[discrete count data], such as the number of occurrences of a particular event within a specific time interval or spatial area. It is often applied to scenarios .red[where events happen at a certain average rate], and each event is independent of the others. It has applications in various fields, such as telecommunications, insurance, and biology.

The Poisson distribution is ideal for modeling count data involving rare events. In many real-world situations, count data often represent occurrences of rare events.

The Poisson distribution is characterized by a single parameter, .red[lambda (λ), which represents the average rate of events over a given time interval or a specific area]. 

]]

---
class: left, middle

.split-50[.column[
#### Binomial Distribution

The binomial distribution is also used for .red[discrete data], specifically for modeling .red[the number of successes in a fixed number of] independent .red[trials]. Each trial has only two possible outcomes (e.g., success or failure, true or false), and .red[the probability of success remains the same across all trials]. It is frequently applied in areas such as quality control, marketing research, and opinion polls.

 The binomial distribution provides a straightforward way to calculate the probability of observing a specific number of successful outcomes in a fixed number of trials. This makes it easy to understand and communicate the results of analyses using binomial distributions.

The binomial distribution involves two parameters:
number of trials and the probability of success (or being one of the two options).

].column[
<img src="resources/w02-img/frequency_distribution_binomial.png" width="100%" align="center">  
.square[Binomial Distribution with various paramters. Number of trials is fixed at 10.]
]]

---
class: left, middle

.split-40[.column[
### Visualizing Frequency Distributions
#### Histogram

- .red[Histogram]
- PDF plot
- CDF plot
- Box plot
- Boxen plot
- 2-variables

].column[
<img src="resources/w02-img/frequency_distribution_histplot.png" width="60%" align="center">  
.square[Histogram of resale prices, differentiated by flat types.]
]]

---
class: left, middle

.split-20[.column[
### Visualizing Frequency Distributions
#### PDF plot

- Histogram
- .red[PDF plot]
- CDF plot
- Box plot
- Boxen plot
- 2-variables

].column[
<img src="resources/w02-img/frequency_distribution_kdeplot.png" width="100%" align="center">  
.square[PDF of resale prices, differentiated by flat types.]
]]

---
class: left, middle

.split-20[.column[
### Visualizing Frequency Distributions
#### CDF plot

- Histogram
- PDF plot
- .red[CDF plot]
- Box plot
- Boxen plot
- 2-variables

].column[
<img src="resources/w02-img/frequency_distribution_ecdfplot.png" width="100%" align="center">  
.square[CDF of resale prices, differentiated by flat types.]
]]

---
class: left, middle

.split-20[.column[
### Visualizing Frequency Distributions
#### Box plot

- Histogram
- PDF plot
- CDF plot
- .red[Box plot]
- Boxen plot
- 2-variables

].column[
<img src="resources/w02-img/frequency_distribution_boxplot.png" width="100%" align="center">  
.square[Box plot of resale prices, differentiated by flat types.]
]]

---
class: left, middle

.split-20[.column[
### Visualizing Frequency Distributions
#### Boxen plot

- Histogram
- PDF plot
- CDF plot
- Box plot
- .red[Boxen plot]
- 2-variables

].column[
<img src="resources/w02-img/frequency_distribution_boxenplot.png" width="100%" align="center">  
.square[Boxen plot of resale prices, differentiated by flat types.]
]]

---
class: left, middle

.split-20[.column[
### Visualizing Frequency Distributions
#### Joint grid plot for 2-variables

- Histogram
- PDF plot
- CDF plot
- Box plot
- Boxen plot
- .red[2-variables]

].column[
<img src="resources/w02-img/frequency_distribution_jointgrid.png" width="70%" align="center">  
.square[Joint grid (scatter plot and PDF) of floor area vs. resale prices, differentiated by flat types.]
]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 3]
## Data Transformation
------
.square[What .dot[] Why .dot[] Ways]

.headnote.square.bold.x-large[Statistical Pattern I]

---
class: left, middle
.split-30[.column[
### What is Data Transformation

].column[
- .bold[Definition]:  
Data transformation is the process of converting data from one form or scale to another to improve analysis and interpretation.
- .bold[Purpose]:  
    - To meet the assumptions of statistical tests, 
    - handle the scale of data range differences, 
    - enhance the performance of machine learning models, 
    - etc.
- .bold[Importance]:  
Proper data transformation can significantly affect the quality of insights derived from data analysis and modeling.

]]

---
class: left, middle
.split-30[.column[
### Ways of Data Transformation

].column[

#### Common data transformation techniques
- Min-Max Scaling
- Standardization
- Log transformation
- Box-Cox transformation
- Ranking data transformation
]]

---
class: left, middle
.split-30[.column[
### Common techniques
- .red[Min-Max Scaling]
- Standardization
- Log transformation
- Box-Cox transformation
- Ranking data transformation

].column[
#### Min-Max Scaling

.bold[Definition and purpose]:
Min-max scaling is a popular data normalization technique that transforms features to fall within a specific range, typically between 0 and 1. 

.bold[Equation]:

$$X'=\frac{X-a}{b-a} \times (b' - a') + a'$$

Where:
- $X'$ is the scaled value of the feature $X$.
- $X$ is the original value of the feature.
- $a$ is the minimum value of the feature across all samples.
- $b$ is the maximum value of the feature across all samples.
- $a'$ & $b'$ is the new minimum and maximum values, respectively, for the target range.

.bold[When to use]: 
Normalizing data to .red[a specific range] and .red[preserving original shape].

]]

---
class: left, middle
.split-30[.column[
### Common techniques
- .red[Min-Max Scaling]
- Standardization
- Log transformation
- Box-Cox transformation
- Ranking data transformation

].column[
#### Min-Max Scaling

<img src="resources/w02-img/data_transform-minmax.png" width="80%" align="center">  
.square[The histogram (top) and PDF (bottom) of the average subzone resale price before (left) and after (right) min-max scaling.]

]]

---
class: left, middle
.split-30[.column[
### Common techniques
- .red[Min-Max Scaling]
- Standardization
- Log transformation
- Box-Cox transformation
- Ranking data transformation

].column[
#### Min-Max Scaling

- Advantages: 
    - Simple, 
    - easy to understand, 
    - preserves shape.
- Disadvantages: 
    - Sensitive to outliers, 
    - less robust.
]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- .red[Standardization]
- Log transformation
- Box-Cox transformation
- Ranking data transformation

].column[

#### Standardization
.bold[Definition and purpose]: 
Standardization (aka Z-score normalization) is a data transformation technique that scales features to have zero mean and unit variance. Its purpose is to make different features comparable by transforming them to a common scale.

.bold[Equation]: 
$$X' = \frac{X - \mu}{\sigma}$$
Where:
- $X$ is the original feature value.
- $\mu$ is the mean of the feature values.
- $\sigma$ is the standard deviation of the feature values.

.bold[When to use]: 
- When working with features measured on different scales (e.g., age, income, and temperature).
- When using machine learning algorithms that are sensitive to feature scales, such as linear discriminant analysis, logistic regression, or principal component analysis.


]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- .red[Standardization]
- Log transformation
- Box-Cox transformation
- Ranking data transformation

].column[
#### Standardization

<img src="resources/w02-img/data_transform-zscore.png" width="80%" align="center">  
.square[The histogram (top) and PDF (bottom) of the average subzone resale price before (left) and after (right) standardization.]

]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- .red[Standardization]
- Log transformation
- Box-Cox transformation
- Ranking data transformation

].column[
#### Standardization

<img src="resources/w02-img/data_transform-zscore2.png" width="80%" align="center">  
.square[The PDF (top) of the average subzone resale price of 3 rooms and 5 rooms HDB flat before (left) and after (right) standardization. The two scatter plots at the bottom show the relationship between 3 and 5 room HDB flat. ]

]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- .red[Standardization]
- Log transformation
- Box-Cox transformation
- Ranking data transformation

].column[

#### Standardization
- Advantages: 
    - Unit variance and zero mean
    - Dimensionless (unitless)
    - Robust to outliers
    - (potentially) Reduces multicollinearity.
- Disadvantages: 
    - Removed original scale and unit
    - Sensitive to new data
    - Not suitable for non-normal/non-linear data
    - (potentially) Not suitable for data crossing zero
]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- Standardization
- .red[Log transformation]
- Box-Cox transformation
- Ranking data transformation

].column[

#### Log Transformation
.bold[Definition and Purpose]: 
Log transformation is a data transformation technique that applies the natural logarithm to the original data.
It helps to reduce skewness in the data and stabilize variance for statistical analysis or modeling.

.bold[Equation]: 
$$X_{\text{log}} = \log(X)$$

Where:
- could use various base for the log, common options include 2, 10, or e (natural log)  

.bold[When to Use]: 
- When the data is positively skewed or has a wide range of values.
- When the relationship between two variables can be better modeled using a logarithmic scale.


]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- Standardization
- .red[Log transformation]
- Box-Cox transformation
- Ranking data transformation

].column[

#### Log Transformation
<img src="resources/w02-img/data_transform-log.png" width="80%" align="center">  
.square[The before (left) and after (right) log-transformed of resale prices. ]

]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- Standardization
- .red[Log transformation]
- Box-Cox transformation
- Ranking data transformation

].column[

#### Log Transformation
<img src="resources/w02-img/demo_log_transform.png" width="50%" align="center">  
.square[The before (top) and after (bottom) log-transformed of ridership (arrival passsenger). ]

]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- Standardization
- .red[Log transformation]
- Box-Cox transformation
- Ranking data transformation

].column[

#### Log Transformation
- Advantages
    - Reduces skewness in data.
    - Helps stabilize variance.
    - Can improve linearity in relationships between variables.
- Disadvantages
    - Distorts the original scale of data, making interpretation more challenging.
    - Cannot be applied to negative values or zero.
    - The choice of logarithm base (e, 2, 10) may affect results and interpretation.
]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- Standardization
- Log transformation
- .red[Box-Cox transformation]
- Ranking data transformation

].column[

#### Box-Cox Transformation

.bold[Definition and Purpose]: 
Box-Cox transformation is a power transformation technique that can stabilize variance and make data more normally distributed.
It is a family of transformations that includes the logarithmic ($\lambda=0$) and square root ($\lambda=0.5$) transformations as special cases.

.bold[Equation]: 

$$X_{\text{box-cox}}(\lambda) = \frac{X^\lambda - 1}{\lambda} \quad \text{if} \quad \lambda \neq 0$$

$$X_{\text{box-cox}}(\lambda) = \log(X) \quad \text{if} \quad \lambda = 0$$

.bold[When to Use]: 
- When the data is not normally distributed or has varying degrees of skewness or kurtosis.
- When trying to linearize relationships between variables or equalize variances across groups.

]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- Standardization
- Log transformation
- .red[Box-Cox transformation]
- Ranking data transformation

].column[

#### Box-Cox Transformation
<img src="resources/w02-img/data_transform-boxcox.png" width="60%" align="center">  
.square[Histogram of Box-Cox transformed values, with $\lambda$ set to: 0, 0.25, 0.5, 1, 2, 3. ]

]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- Standardization
- Log transformation
- .red[Box-Cox transformation]
- Ranking data transformation

].column[

#### Box-Cox Transformation
- Advantages
    - Can handle various degrees of skewness and kurtosis.
    - Provides flexibility to choose the best transformation based on data characteristics.
    - Includes logarithmic and square root transformations as special cases.
- Disadvantages
    - Requires estimating the optimal lambda parameter, which can be time-consuming.
    - Loses some interpretability due to data transformation.
    - May not always provide a significant improvement in data normality.

.xkcd[How to determine which $\lambda$ is the best?]

]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- Standardization
- Log transformation
- Box-Cox transformation
- .red[Ranking data transformation]

].column[

#### Ranking Data Transformation
.bold[Definition and Purpose]: 
Ranking data transformation replaces original values with their corresponding ranks, preserving the order or hierarchy of the data.
It can help in data visualization, feature engineering, or non-parametric statistical tests.

.bold[How it works]: 
There is no explicit equation for ranking data transformation. The process involves sorting the values and assigning ranks based on their positions in the sorted list. In case of ties, you can use methods like average, min, or max ranking.

.bold[When to Use]: 
When working with ordinal data or categorical data that can be ordered.
When performing non-parametric statistical tests that require ranked data.

]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- Standardization
- Log transformation
- Box-Cox transformation
- .red[Ranking data transformation]

].column[

#### Ranking Data Transformation
<img src="resources/w02-img/data_transform-ranking.png" width="80%" align="center">  
.square[The relationship between the ranks and the original data, and the frequency distribution of the ranks. ]

.xkcd[What is the expected frequency distribution?]  
.xkcd[Why is it not exactly the same as the expected distribution?]
]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- Standardization
- Log transformation
- Box-Cox transformation
- .red[Ranking data transformation]

].column[

#### Ranking Data Transformation
- Advantages
    - Simplifies data interpretation by focusing on relative positions.
    - Can mitigate the impact of outliers.
    - Suitable for non-parametric statistical tests.
- Disadvantages
    - Loses information about the original magnitude, scale, and internal variation of data.
    - Sensitive to ties in data, especially when using certain ranking methods.
    - May not be appropriate for all types of statistical analyses or machine learning algorithms.
]]

---
class: left, middle
.split-30[.column[
### Common techniques
- Min-Max Scaling
- Standardization
- Log transformation
- Box-Cox transformation
- Ranking data transformation

].column[

#### Other Techniques
- Sigmoid function, 
- Yeo-Johnson transformation, 
- etc.
]]

---
class: left, middle
.split-20[.column[
### Choosing the Right Technique
#### A simple guide

].column[

**1. Assess data quality and characteristics**:  
Examine your dataset for issues like missing values, outliers, .red[non-linearity, and non-normal distributions]. Identifying these challenges will inform the choice of transformation technique.

**2. Understand variable types**:  
Determine whether your variables are .red[categorical or numerical]. This will help you choose appropriate transformation methods, as some techniques are designed specifically for certain variable types.

**3. Evaluate the goals of your analysis**:  
Consider the .red[objectives of your data analysis] and the specific requirements of your chosen modeling technique. Different transformations can address particular challenges or better align with specific analysis goals.

**4. Investigate common transformation techniques**:  
Explore various methods like .red[logarithmic], square root, .red[Box-Cox], or .red[Z-score (standardization)] transformations for numerical data, and one-hot encoding or ordinal encoding for categorical data.

]]

---
class: left, middle
.split-30[.column[
### Choosing the Right Technique
#### A simple guide

].column[
**5. Compare the pros and cons**: 
Weight the advantages and disadvantages of different techniques, considering factors like interpretability, ease of implementation, and .red[potential impact on model performance].

**6. Iterate and validate**:  
Test multiple transformation techniques and .red[evaluate their effects] on your data and model performance. This will help you identify the most effective approach for your specific situation.

**7. Consult resources and domain experts**:  
Leverage the knowledge of experienced professionals, peer-reviewed literature, and other credible sources to inform your decision-making process.
]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 4]
## Numerical Data Classification
------
.square[The What .dot[] The Ways]

.headnote.square.bold.x-large[Statistical Pattern I]

---
class: left, middle
.split-30[.column[
### Definition of Numerical Data Classification
].column[
Numerical Data Classification is a method of .red[categorizing or grouping] numerical data into different classes or bins based on specific criteria or algorithms. This approach helps simplify data analysis, visualization, and interpretation by transforming .red[continuous numerical values into discrete categories or intervals]. 

The number of breaks: 
- for visualization purpose, the common preferred number of breaks is $\leq 7$, 
- common numbers of breaks in practice is: 4--5, 
- follow the requirement of the analysis method or domain knowledge.

Several common classification methods include:
- Equal Interval
- Quantile Breaks
- Standard Deviation
- Natural Breaks
- Head-tail Breaks
]]

---
class: left, middle
.split-30[.column[
### Data Classification Approaches
- .red[Equal Interval]
- Quantile Breaks
- Standard Deviation
- Natural Breaks
- Head-tail Breaks
].column[

.bold[Equal Interval]:  
This classification method involves dividing the range of the data into equal-sized intervals or classes. The class boundaries are determined by dividing the difference between the maximum and minimum values by the number of desired classes. This method is simple and easy to understand but may result in classes with significantly different numbers of observations or misrepresentation of the data distribution.
]]

---
class: left, middle
.split-30[.column[
### Data Classification Approaches
- .red[Equal Interval]
- Quantile Breaks
- Standard Deviation
- Natural Breaks
- Head-tail Breaks
].column[
<img src="resources/w02-img/data_classify-equal_interval.png" width="100%" align="center">  
.square[The breaks and the number of records in each class for Equal Interval. ]


]]

---
class: left, middle
.split-30[.column[
### Data Classification Approaches
- Equal Interval
- .red[Quantile Breaks]
- Standard Deviation
- Natural Breaks
- Head-tail Breaks
].column[

.bold[Quantile Breaks]:  
Quantile classification is based on the statistical distribution of the data, dividing the data into classes with an equal number of observations. Each class represents a quantile, such as quartiles (4 classes), quintiles (5 classes), deciles (10 classes), or other user-specified quantiles. This method ensures that each class has an equal frequency of values.
]]

---
class: left, middle
.split-30[.column[
### Data Classification Approaches
- Equal Interval
- .red[Quantile Breaks]
- Standard Deviation
- Natural Breaks
- Head-tail Breaks
].column[
<img src="resources/w02-img/data_classify-quantiles.png" width="100%" align="center">  
.square[The breaks and the number of records in each class for Quantiles. ]

]]

---
class: left, middle
.split-30[.column[
### Data Classification Approaches
- Equal Interval
- Quantile Breaks
- .red[Standard Deviation]
- Natural Breaks
- Head-tail Breaks
].column[

.bold[Standard Deviation]:  
Standard Deviation classification divides the data into classes based on the number of standard deviations from the mean. This method is helpful for data that .red[follow a normal or near-normal distribution], as it takes into account the dispersion and variability of the data.
]]

---
class: left, middle
.split-30[.column[
### Data Classification Approaches
- Equal Interval
- Quantile Breaks
- .red[Standard Deviation]
- Natural Breaks
- Head-tail Breaks
].column[
<img src="resources/w02-img/data_classify-StdMean.png" width="100%" align="center">  
.square[The breaks and the number of records in each class for standard deviation. ]

]]

---
class: left, middle
.split-30[.column[
### Data Classification Approaches
- Equal Interval
- Quantile Breaks
- Standard Deviation
- .red[Natural Breaks]
- Head-tail Breaks
].column[

.bold[Natural Breaks]:  
Natural Breaks classification is a data-driven method that seeks to minimize the within-class variance and maximize the between-class variance. It identifies break points or class boundaries by grouping similar values together while keeping dissimilar values in different classes. This method is widely used in geographic information systems (GIS) and spatial data analysis.

]]

---
class: left, middle
.split-30[.column[
### Data Classification Approaches
- Equal Interval
- Quantile Breaks
- Standard Deviation
- .red[Natural Breaks]
- Head-tail Breaks
].column[
<img src="resources/w02-img/data_classify-NaturalBreaks.png" width="100%" align="center">  
.square[The breaks and the number of records in each class for Natural Breaks. ]


]]

---
class: left, middle
.split-30[.column[
### Data Classification Approaches
- Equal Interval
- Quantile Breaks
- Standard Deviation
- Natural Breaks
- .red[Head-tail Breaks]
].column[

.bold[Head-tail Breaks]:  
Head/Tail Breaks is a data classification method introduced to categorize data with heavy-tailed distributions. This method offers an alternative to traditional classification schemes by focusing on the inherent hierarchy within the data.
The Head/Tail Breaks method uses the mean or average to divide a dataset into small and large values recursively. It starts by calculating the first mean (m1) of the entire dataset and then calculates the second mean (m2) for values greater than m1. This process continues until the notion of ".red[far more small things than large ones]" no longer holds.

]]

---
class: left, middle
.split-30[.column[
### Data Classification Approaches
- Equal Interval
- Quantile Breaks
- Standard Deviation
- Natural Breaks
- .red[Head-tail Breaks]
].column[
<img src="resources/w02-img/data_classify-HeadTailBreaks.png" width="100%" align="center">  
.square[The breaks and the number of records in each class for Head/Tail Breaks. ]


]]

---
class: left, middle
.split-30[.column[
### Summary
].column[
Choosing an optimal data classification scheme is essential for effectively summarizing and analyzing numerical data. The selection depends on .red[the data's characteristics, the analysis objectives, and the desired level of detail]. See a list here from [mapclassify](https://github.com/pysal/mapclassify) for many other approaches.
Experiment with different methods and assess their effectiveness in achieving your analytical goals. The optimal scheme should provide .red[meaningful distinctions between classes, maintain simplicity, and facilitate accurate data interpretation].

.red[While Natural Breaks is the default option in many GIS software, it is not always the most suitable option for the data. Sometime, manually breaking the data is also recommended. ]

]]

---
class: left, middle
.split-30[.column[
### Summary
].column[
1. .bold[Equal Interval]: This simple method divides the data range into .red[equal-sized intervals]. It is straightforward and easy to understand but may result in classes with significantly different numbers of observations.
2. .bold[Quantile Breaks]: This method divides data into classes with an equal number of observations based on statistical distribution. It is useful when you require a specific number of classes or .red[a balanced representation] of the data.
3. .bold[Standard Deviation]: This method classifies data based on the number of standard deviations from the mean. It is helpful when data .red[follows a normal or near-normal distribution] and accounts for data dispersion and variability.
4. .bold[Natural Breaks]: This data-driven method minimizes within-class variance and maximizes between-class variance. It is widely used in geographic information systems (GIS) and spatial data analysis. Jenks' natural breaks are suitable for datasets with uneven distributions or .red[when you need to emphasize the differences between groups].
5. .bold[Head/Tail Breaks]: Introduced by Jiang (2013), this recursive method focuses on capturing .red[the inherent hierarchy within heavy-tailed data]. It provides an alternative to traditional schemes and is particularly suitable for data with a heavy-tailed distribution.
]]


---
class: center, middle, inverse

## Closing Remarks
------

.square[Data Preparation .dot[] Frequency Distribution .dot[] Data Transformation .dot[] Data Classification]

.headnote.square.bold.x-large[Statistical Pattern I]

---
class: left, middle

.split-30[.column[
### Today's topics
Dealing with Statistical Data
].column[
- The steps for Data Preparation
- The types of Frequency Distribution and how to visualize and read them
- Various types of data transformation that change the distribution of data
- Various types of numerical data classification that convert continuous data to discrete form. 

]]

---
class: center, middle

<img src="resources/w02-img/week2_concluding.drawio.png" width="90%" align="center">  
Dealing with Statistical Data

---
class: left, middle

.split-30[.column[
### Expanding from today's topics
].column[
Data analysis and visualization involve countless human-computer interactions, often requiring trial and error. Data (pre)processing is therefore an iterative (and possibly tedious) process.

- Keep versioning your code and back up periodically.
    - Try adding meaningful version codes for your notebooks/scripts.
- Maintain the readability of your code (ensure you can understand what you've written).
    - Try the most intuitive way of writing code.
    - Use comments to remind your future self of your thought process.
    - Use top block comments or text cells to explain what the code accomplishes and what's new in each version.
- Document your work periodically (write summaries of the output).
- Always reflect on what you've done and how it relates to your primary goal (BIG AIM).
- [Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python)

]]

---
class: left, middle
### Zen of Python
which also works in visualisation  

.red[Beautiful] is better than ugly.  
.red[Explicit] is better than implicit.  
.red[Simple] is better than complex.  
.red[Complex] is better than complicated.  
.red[Flat] is better than nested.  
.red[Sparse] is better than dense.  
.red[Readability] counts.  
Special cases aren't special enough to break the rules.  
......
