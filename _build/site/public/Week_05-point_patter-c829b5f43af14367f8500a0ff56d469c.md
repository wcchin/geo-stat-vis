slide_title: Week 05 - Point Pattern I: Spatial Clustering Phenomenon
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

## Point Pattern I: Spatial Clustering Phenomenon
------

<br />

.x-large.bold[Dr. CHIN Wei Chien Benny]  
[.underline.square[wcchin@nus.edu.sg]]  

.headnote.square.bold.x-large[GE5230 Geospatial Statistics and Visualization]
.footnote.square[05 @ 2025-09-11 Department of Geography, NUS]

---
layout: false
class: left, middle

.split-10[.column[].column[
### Two Types Clustering in Spatial Analysis

1. some parts of the study area that have very high concentration of point events, i.e., .red['clusters']
    - to check if this phenomenon exists in the spatial point data
    - to identify the location of these clusters
    - significant tests, CSR

2. groups of spatial points that are close to each other, i.e., .red['clusters']
    - identify grouping of points with/without overlap


In today's lecture, we focus on the first 'clustering' analysis.
]]

---
class: center, top
### Recap: Three Major types of Point Pattern

<img src="resources/w04-img/spatial_patterns_3_basic.png" width="100%">

.red.xkcd[How to differentiate clustered from random .bold[(CSR)]?]

.xkcd[CSR: Complete Spatial Randomness]

---
class: left, middle

.split-50[.column[
### Measurement strategies
].column[
- Grid-based
- Distance-based
]]

---
class: center, middle

### Measurement strategies
#### Grid-based

<img src="resources/w05-img/three_strategies_for_point_pattern_2c.png" width="70%">

---
class: center, middle

### Measurement strategies
#### Distance-based

<img src="resources/w05-img/three_strategies_for_point_pattern_2b.png" width="70%">

---
class: left, middle
## Objectives of this lecture
- To learn how to identify Clustering Pattern
    - Grid-based, counting: Quadrat Count Analysis
    - Distance-based, sorting: Nearest Neighbor Analysis
    - Distance-based, searching: Ripley's K-function(s)
- Monte-Carlo Simulation

---
class: center, middle, inverse

.xx-large.bold.wide[PART 1]
## Quadrat Count Analysis
------
.square[Definition .dot[] Steps .dot[] Example .dot[] Consideration]

.headnote.square.bold.x-large[Point Pattern I]

---
class: left, middle
.split-30[.column[
### What is Quadrat Count Analysis? 
].column[
Quadrat Count Analysis is a method used in spatial point pattern analysis to determine whether a pattern of points is randomly distributed, clustered, or evenly spaced. It involves .red[dividing the study area into smaller, equal-sized areas called "quadrats"] (typically square or rectangular in shape) and .red[counting the number of points fall in each quadrat].
]]

---
class: left, middle
.split-30[.column[
### Calculating Quadrat Count Analysis? 
].column[
The main steps in Quadrat Count Analysis are:
1. Divide the study area into a .red[grid of quadrats].
2. .red[Count] the number of points in each quadrat.
3. Calculate the .red[expected number of points] per quadrat under the assumption of Complete Spatial Randomness (CSR). 
4. .red[Compare] the observed frequency distribution (the counts) with the expected frequency distribution (under CSR) to assess the degree of similarity or difference between them.
5. Apply .red[statistical tests], such as the chi-squared goodness-of-fit test, to determine whether the observed frequency distribution significantly differs from the expected distribution under CSR---whether the spatial pattern exhibits randomness, clustering, or regularity.
]]

---
class: center, middle

### Count the number of points in each quadrat
<img src="resources/w05-img/plot_quadrat_counts.png" width="100%">

---
class: left, middle
.split-30[.column[
### Chi-squared test
Use Chi-squared test, which is suitable for comparing the frequencies. 
].column[
The quadrat method partitions the study region into $r$ rows and $c$ columns, which define $m=r\times c$ non-overlapping subregions or quadrats of equal area. This method relies on the fact that, .red[under CSR, the expected number of observations within any region of equal size is the same]. Let $n$ be the number of observed points, $m$ the number of quadrats of equal size, and $n_i$ the number of points in quadrat $i$. The expected number of points in each quadrat is $N/m$. The test statistic is calculated as

$$
\chi^2 = \sum_{i=1}^m\frac{\text{observed}_i - \text{expected}}{\text{expected}}
$$

$$
\text{expected} = \frac{N}{m}
$$

.xkcd.red.bold[Why?]

.xkcd[A CSR would have a mean at the average with a spread (non-zero deviation). ]

]]

---
class: left, middle
.split-30[.column[
### Chi-squared test
Use Chi-squared test, which is suitable for comparing the frequencies against an expected frequency or distribution. 
].column[
.bold[Clustered example]
- chi-squared statistic=354.332, p-value=.red[2.606e-66]
- .red[significantly different] from random

.bold[Random example]
- chi-squared statistic=19.332, p-value=0.199
- non-significant; the distribution is .red[not different from random]

.bold[Regular example]
- chi-squared statistic=8.332, pvalue=0.910
- non-significant; the distribution is .red[not different from random]

.xkcd[Since the expected number of points are the average number of points---the test do not consider the spread mathematically---thus the regular example 'is not different from random'. ]

]]

---
class: left, middle
.split-30[.column[
### Key considerations
].column[
Some key considerations in Quadrat Count Analysis include:
- .bold[Quadrat size]: The size of the quadrats should be carefully chosen to ensure that it is appropriate for the scale of the pattern being studied.
- .bold[Quadrat shape]: While square quadrats are common, other shapes (such as rectangular or circular) may be used depending on the specific study requirements.
- .bold[Edge effects]: Care should be taken to account for edge effects, which occur when quadrats at the edge of the study area contain fewer points due to the smaller overlapping area.

.xkcd.red.bold[Is the analysis result sensitive to the parameter settings?]

Quadrat Count Analysis provides a simple and intuitive approach to analyzing spatial point patterns, but it has some limitations compared to more advanced methods, such as **distance-based** or **density-based** approaches. Nonetheless, it is a useful tool for exploratory analysis and can be helpful in understanding the general characteristics of a spatial point pattern.
]]


---
class: center, middle, inverse

.xx-large.bold.wide[PART 2]
## Nearest Neighbor Analysis
------
.square[Steps .dot[] Monte Carlo Simulation .dot[] Testing]

.headnote.square.bold.x-large[Point Pattern I]

---
class: center, top
### The 2 Distance-based Approaches

<img src="resources/w05-img/three_strategies_for_point_pattern_2b.png" width="85%">

---
class: left, middle

.split-40[.column[
### Clustered or Random

- Woodlands Regional Centre, Woodlands West, and Woodgrove
- $2 \text{km} \times 2 \text{km}$ area

].column[
    <img src="resources/w05-img/four_demo_points.png" width="95%">
]]


---
class: left, middle

.split-40[.column[
### Nearest Neighbor Analysis

- Identifying nearest neighbors for every point
- Record the nearest neighbor distances
- Calculate the .red[mean value]
    - observed average nearest neighbor distance ($D_O$)
- The average nearest neighbor distance:
    - short: the points are close to each other
    - long: the points are far from each other

].column[
    <img src="resources/w05-img/simulate_nna.gif" width="95%">
]]

---
class: left, middle

.split-40[.column[
### Nearest Neighbor Analysis
How short is short enough to be considered as "clustered"?

Let's use the .red[Monte Carlo Simulation] approach to test the .red[difference] between the .red[observed] point pattern and a large number of random patterns generated under the .red[CSR assumption]. 
].column[
<img src="resources/w05-img/mean_nearest_negihbor_4cases_b.png" width="95%">
]]

---
class: left, middle

.split-40[.column[
### Monte Carlo Simulation

- .red[Area size has to match the study area]. 
    - Area size will affect the distance between points. 
- .red[The number of points has to match the dataset]. 
    - Within the same area, more points (higher density) will lead to lower nearest neighbor distances. 

].column[
<img src="resources/w05-img/monte_carlo_point_pattern.gif" width="95%">
]]

---
class: left, middle

.split-50[.column[
### Statistical Testing

- After simulating random for M times, we will get M measurement of mean nearest neighbor distances.
- The frequency distribution of the N values would form a normal distribution. 
- The range where the normal distribution is located represent the "random (CSR)" under the specific area and # point setting. 

].column[
<img src="resources/w05-img/drawing_normal_testing_0.png" width="100%">
]]

---
class: left, middle

.split-50[.column[
### Statistical Testing

(1) If the observed value is far from the random, we found a clear evidence that the observed pattern is different from random. 
- either .red[clustered or dispersed]

].column[
<img src="resources/w05-img/drawing_normal_testing_1.png" width="100%">
]]

---
class: left, middle

.split-50[.column[
### Statistical Testing

(2) If the observed value fall within the random range, then, we did not find any evidence to prove that the observed pattern is different from random. 
- cannot reject the null hypothesis
- .red[we have no choice but to believe it is random]

].column[
<img src="resources/w05-img/drawing_normal_testing_2.png" width="100%">
]]

---
class: left, middle

.split-50[.column[
### Statistical Testing

(3) If the observed fall at the edge of the normal distribution
- check .red[p-value] and your confidence level setting. 

.underline[p-value: the probability of being wrong to reject null hypothesis]  

.footnote-left[see [ESRI "What is a z-score? What is a p-value?"](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/what-is-a-z-score-what-is-a-p-value.htm) for more details]

].column[
<img src="resources/w05-img/drawing_normal_testing_3.png" width="100%">
]]

???
Let's say we set the confidence level to 99%, meaning we are willing to accept a 1% risk of being wrong (incorrectly rejecting the null hypothesis, H0).
If the obtained p-value is 3%, which is higher than our acceptable risk, we cannot reject H0.

---
class: center, top

.headnote.small.title-font.bold[How the observed mean compared with 10k CSR simulations mean results?]

<img src="resources/w05-img/nna_compare_hist.png" width="90%">

.footnote.small.title-font.bold[Monte Carlo Simulation] 

???
The grey area indicates the mean nearest neighbor distance of the 10k random pattern.

---
class: left, middle
.split-30[.column[
### Z-test approach

Z-test is another option for testing the significant levels of how observed nearest neighbor distance ($\bar{D}_O$) is different from the 'expected' average nearest neighbor distance ($\bar{D}_E$) under CSR. 
.smaller[See [ESRI](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/h-how-average-nearest-neighbor-distance-spatial-st.htm) for detail.]

].column[
The nearest neighbor distance ratio: 
$$
\text{ANN} = \frac{\bar{D}_O}{\bar{D}_E}
$$
If the index ($\text{ANN}$) is less than 1, the pattern exhibits clustering.  
If the index is greater than 1, the trend is toward dispersion.

The expected mean distance could be calculated using the number of point (n) and the study area (A):
$$
\bar{D}_E = \frac{0.5}{\sqrt{n/A}}
$$

The z-score can then be calculated using $\bar{D}_O$ and $\bar{D}_E$:
$$
z = \frac{\bar{D}_O - \bar{D}_E}{SE}
$$

The z-score and p-value for this statistic are sensitive to changes in the study area or changes to the Area parameter. For this reason, only compare z-score and p-value results from this statistic when the study area is fixed. 

]]

---
class: left, middle
.split-30[.column[
### Z-test approach

].column[

<img src="resources/w05-img/ztest.png" width="85%">
.footnote-left[see [ESRI "What is a z-score? What is a p-value?"](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/what-is-a-z-score-what-is-a-p-value.htm) for more details]
]]


---
class: left, middle

.split-30[.column[
### Summary
#### Nearest Neighbor Analysis (NNA)

].column[

- This approach calculates the average distance of the nearest neighbor for every point. 

<br>
- The observed average nearest neighbor distance can be tested using a Monte Carlo Simulation or z-test approaches against the null hypothesis of CSR.

<br>
- The NNA has an assumption that the points being measured are .red[free to locate anywhere within the study area] (for example, there are no barriers, and all cases or features are located independently of one another). 

]]


---
class: center, middle, inverse

.xx-large.bold.wide[PART 3]
## Ripley's K-function
------
.square[]

.headnote.square.bold.x-large[Point Pattern I]

---
class: center, top
### The 2 Approaches

<img src="resources/w05-img/three_strategies_for_point_pattern_2b.png" width="85%">

---
class: left, middle

.split-40[.column[
#### Bus Stops distribution

- Bus stops usually constructed in pairs, at both sides of a street. 
- The nearest neighbor is at a short distance (opposite of street), but the second nearest may not. 
- Is it a "real" clustered pattern?

].column[
<img src="resources/w05-img/Bus_Stop_nearest_neighbor.png" width="90%">
]]

---
class: left, middle

.split-40[.column[
### Search Radius approach

The Ripley's K-function

- Generate a series of search radius (SR), from low to high
- Search for pairs of points fall within every SR
- The implication:
    - if a lot of pairs are found within a short SR: the points are clustered at this distance.

].column[
    <img src="resources/w05-img/simulate_kfunc.gif" width="100%">
]]

---
class: left, middle

.split-30[.column[
### The Ripley's K-function
].column[
A common transformation of the K-function:
$$
L(d) = \sqrt{\frac{A \times \text{pairs}_d }{\pi n(n-1)}}
$$

$$
\text{pairs}\_d = \sum\_{i=1}^n \sum\_{j=1, j\neq i}^n w\_{ij}
$$

- $L(d)$: the k-function value at search radius $d$
- $\text{pairs}_d$: the number of pairs of points with distance less than $d$ 
- $w_{ij}$: equal to 1 if non-weighted; weighting for edge-correction
- $A$: Area of study
- $n$: total number of points
- $n(n-1)$: total number of all pairs

.smaller[More info: https://pro.arcgis.com/en/pro-app/3.1/tool-reference/spatial-statistics/h-how-multi-distance-spatial-cluster-analysis-ripl.htm]
]]

---
class: left, middle

.split-40[.column[
### Testing of K-functions

- How high is high enough to be considered as clustered?
- To compare them with CSR, Monte Carlo Simulation can be used


].column[
    <img src="resources/w05-img/kfunc_arcGIS_redraw.png" width="100%">
]]


---
class: left, middle

.split-40[.column[
### Testing of K-functions

- How high is high enough to be considered as clustered?
- To compare them with CSR, Monte Carlo Simulation can be used
- For demonstration: 10 random patterns are generated


].column[
    <img src="resources/w05-img/k_function_4cases_rand.png" width="100%">
]]

---
class: left, middle

.split-40[.column[
### Testing of K-functions

- How high is high enough to be considered as clustered?
- To compare them with CSR, Monte Carlo Simulation can be used
- For demonstration: 10 random patterns are generated
- Calculate 95% Confidence envelop

.small[see [ESRI](https://pro.arcgis.com/en/pro-app/3.1/tool-reference/spatial-statistics/h-how-multi-distance-spatial-cluster-analysis-ripl.htm) for more details]

].column[
    <img src="resources/w05-img/k_function_4cases_ci.png" width="100%">
]]

---
class: center, top

.split-50[.column[
.headnote.title-font.small.bold[Spatial Point Pattern]
<img src="resources/w05-img/drawing_nna_res_2.png" width="100%">

Nearest Neighbor Analysis
].column[
<img src="resources/w05-img/k_function_4cases_ci.png" width="100%">

Ripley's K-function
]]


---
class: left, middle

.split-30[.column[
### Summary
#### Repley's K-function
].column[
- Purpose:  
Ripley's K function is a tool used to analyze spatial point patterns, helping researchers understand the spatial relationships among events or objects in a given study area.

- Functionality:  
The K function estimates the expected number of points within a given distance from a randomly chosen point, providing insights into clustering, dispersion, or randomness in the spatial pattern.

- Key features:
    - The K function can be plotted as a function of distance to visualize changes in spatial interactions at different scales.
    - It can be compared with theoretical models, such as complete spatial randomness (CSR), to assess deviations from expected patterns.

]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 4]
## A Demonstration
---- 

.headnote.square.bold.x-large[Point Pattern I]

---
class: center, middle
background-image: url(resources/w05-img/gordon_square2b.png)

## Let's do a mind travel...

---
class: left, middle
background-image: url(resources/w05-img/gordon_square2.png)
<div class="box">
<h3 class="box-text"> Gordon Square </h3>
</div>

.footnote-right.red.title-font.bold[Source: [Google Map](https://maps.app.goo.gl/Qdb1K4hzyG485Btm8)]

---
class: left, middle

### The question

- Can we assume people randomly find a spot to sit?
- Can we assume people prefer not to sit too close to strangers?
- If they go with friends or colleagues, they will sit together.
<br/><br/>
- .underline[Will the process of .red[people finding comfortable spots for sitting in an open space] result in a random, clustered, or dispersed pattern?]
<br/><br/>
- Analyze with:
    1. individual level
    2. group level



---
class: left, middle

.split-40[.column[
### The dataset

This dataset records the location of people sitting on a grass patch in Gordon Square, London, at 3pm on a sunny afternoon.

Area: $42 \times 56 \text{m}^2$

Source: [R spatstat dataset](https://search.r-project.org/CRAN/refmans/spatstat.data/html/gordon.html)

.footnote-left.smaller[Baddeley et al. 2013: [DOI:10.18637/jss.v055.i11](https://www.jstatsoft.org/article/view/v055i11)]
].column[
<img src="resources/w05-img/Gordon_square_data_individuals_xkcd.png" width="75%">
]]

---
class: center, top

<img src="resources/w05-img/GordonSquare_individual_and_groups_xkcd.png" width="80%">


---
class: left, middle

.split-50[.column[
### Nearest Neighbor Analysis

- For individual, the p-value is significant with a negative z-score, indicating people tended to sit together. 
- For in-group, the p-value is significant, with a positive z-score, suggesting the locations of groups are dispersed. 

].column[
<img src="resources/w05-img/nna_compare_hist_gordon.png" width="70%">
]]

---
class: left, middle

.split-50[.column[
### Ripley's K-function
For individual,
- radius 4 m resulted in higher than random, indicating people tended to sit together at this scale. 
- betwen 4 m and 6 m , the observed line is near to the random, but still above the 95% CI. 
<br>

For in-group, 
- the search radius less than 7 m resulted in dispersed pattern. 
- the search radius beyond 8 m presented random pattern. 

].column[
<img src="resources/w05-img/k_function_ci_gordon.png" width="70%">
]]

---
class: center, middle, inverse

## Closing Remarks
---- 
.square[Considerations .dot[] Workflow .dot[] About Tests]

.headnote.square.bold.x-large[Point Pattern I]

---
class: left, middle

.split-30[.column[
### Summary
#### NNA & K-function: Key Considerations, Limitations, and Directions

- .red[Sensitive to study area size and settings]
- Edge effect (border effect)
- Population-at-risk
].column[

- .bold[Sensitive to study area size and settings]:  
CSR assume points to be scattered all around the study area. Thus, Ripley's K function can be influenced by the size and shape of the study area. .red[Larger study areas] may result in different K function estimates compared to smaller ones, and .red[irregular shapes] can introduce biases. Additionally, the settings used for the K function analysis, such as the bandwidth or edge correction method, can impact the results.

<img src="resources/w05-img/area_size.png" width="100%">
]]

---
class: left, middle

.split-30[.column[
### Summary
#### NNA & K-function: Key Considerations, Limitations, and Directions

- Sensitive to study area size and settings
- .red[Edge effect (border effect)]
- Population-at-risk
].column[
- .bold[Edge effect] (border effect):  
Points beyond the study area are 'ignored.' .red[Points close to the boundary of the study area may have fewer neighboring points] than those in the interior, which can bias the K function estimates. This is known as the edge effect, and it can introduce inaccuracies when studying spatial patterns. Edge correction methods are often employed to mitigate this issue.

<img src="resources/w05-img/edge_effect.png" width="50%">
]]

---
class: left, middle

.split-30[.column[
### Summary
#### NNA & K-function: Key Considerations, Limitations, and Directions

- Sensitive to study area size and settings
- Edge effect (border effect)
- .red[Population-at-risk]
].column[
- .bold[Population-at-risk]:  
Ripley's K function assumes that the underlying point process is .red[stationary and homogeneous]. If the population at risk (i.e., the underlying risk of events occurring) is not uniform across the study area, this can violate the assumptions and lead to misleading results. Incorporating information on the population at risk can help refine the analysis and improve the accuracy of the conclusions drawn from the K function.

<img src="resources/w05-img/pop_at_risk.png" width="50%">
]]

---
class: left, middle

.split-30[.column[
### What has been covered today

What is the workflow of analyzing spatial point pattern?

Global Pattern: the overall pattern of the point distribution

Local Pattern: where are the clusters

].column[
<img src="resources/w05-img/about_point_pattern_analysis Diagram.drawio.png" width="70%">
]]


---
class: left, middle

.split-20[.column[
### Some notes
].column[
The three methods explore the spatial pattern with different angle:
- Quadrat count: the number of points fall in equal size quadrats
- NNA: how near/far the nearest neighbor is
- K-function: how many other points could be found for a specific search radius

The latter two methods can be extended:
- NNA: to k-order nearest neighbor (see: .smaller[[CrimeStat III](https://www.ojp.gov/pdffiles1/nij/grants/209264.pdf)])
- K-function: weighted K-function (see: .smaller[[ArcGIS Pro](https://pro.arcgis.com/en/pro-app/3.1/tool-reference/spatial-statistics/h-how-multi-distance-spatial-cluster-analysis-ripl.htm)])

Things to considered:
- .red[Edge effect]: the near border areas could be underestimated due to the external points. (see: .smaller[[DOI:10.2307/3237072](https://doi.org/10.2307/3237072)])
- .red[Population at risk]: a place with more population could have more events (e.g., crime/disease cases) happens by chance. (see: .smaller[[SaTScan](https://www.satscan.org/cgi-bin/satscan/register.pl/SaTScan_Users_Guide.pdf?todo=process_userguide_download)])  
]]

---
class: left, middle

.split-20[.column[
### About Statistical Tests
].column[

#### About Tests
There are so many tests. It is more important to know:   
- The key considerations for choosing a test:  
Understand the .red[assumptions, requirements, and limitations of each test], as well as .red[the nature of your data] and .red[research questions], to select the most appropriate test.
    - Knowing these can help you to choose the appropriate test(s).

- What you're testing and why:  
Be clear to yourself about the null and alternative hypotheses, .red[the rationale behind them], and .red[the implications of your results].
    - Are you testing against CSR? Why?

- Explicitly communicate your approach:  
you have to explicitly tell your readers what, why, and how.
    - Don't let your readers guess. 

.xkcd[No single test is suitable for all situations, and it's impossible to memorize every test.] 
Instead, focus on developing a strong foundation in statistical concepts and .red[knowing where to find] relevant information when selecting the appropriate test for your specific needs.

]]

---
class: left, middle

.split-20[.column[
### About Statistical Tests
].column[


#### About p-value
- p-value can only tell you how much risk you need to take if you reject H0. 

- the common practice is to check if p-value $< \alpha$, and common alpha values are: 
    - 0.05 for 95% confidence, 
    - 0.01 for 99% confidence, and 
    - 0.001 for 99.9% confidence.  

- If p-value is less than the pre-determined $\alpha$, then it is significantly different. 

- That's how far you can get with p-value---.red[don't over-interpret the p-value]. 
    - Comparing p-values can be problematic, because they may be calculated from different settings, e.g., sample size. 

]]