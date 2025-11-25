# A Demonstration


```{figure} ../resources/w05-img/gordon_square2.png
:label:
:alt:
:align: center

Let's do a mind travel to  Gordon Square, London, UK. Source: [Google Map](https://maps.app.goo.gl/Qdb1K4hzyG485Btm8)
```


## The question

- Can we assume people randomly find a spot to sit?
- Can we assume people prefer not to sit too close to strangers?
- If they go with friends or colleagues, they will sit together.

- _Will the process of **people finding comfortable spots for sitting in an open space** result in a random, clustered, or dispersed pattern?_

Analyze with:
1. individual level
2. group level


## The dataset

This dataset records the location of people sitting on a grass patch in Gordon Square, London, at 3pm on a sunny afternoon.

Area: $42 \times 56 \text{m}^2$

Source: [R spatstat dataset](https://search.r-project.org/CRAN/refmans/spatstat.data/html/gordon.html), Baddeley et al. 2013: [DOI:10.18637/jss.v055.i11](https://www.jstatsoft.org/article/view/v055i11)


```{figure} ../resources/w05-img/GordonSquare_individual_and_groups_xkcd.png
:label:
:alt:
:align: center

Distribution of individuals and groups.
```


## Nearest Neighbor Analysis

- For individual, the p-value is significant with a negative z-score, indicating people tended to sit together.
- For in-group, the p-value is significant, with a positive z-score, suggesting the locations of groups are dispersed.



```{figure} ../resources/w05-img/nna_compare_hist_gordon.png
:label:
:alt:
:align: center

NNA result.
```


## Ripley's K-function

For individual,
- radius 4 m resulted in higher than random, indicating people tended to sit together at this scale.
- betwen 4 m and 6 m , the observed line is near to the random, but still above the 95% CI.


For in-group,
- the search radius less than 7 m resulted in dispersed pattern.
- the search radius beyond 8 m presented random pattern.



```{figure} ../resources/w05-img/k_function_ci_gordon.png
:label:
:alt:
:align: center

K-function result.
```



## Closing Remarks

### NNA & K-function: Key Considerations, Limitations, and Directions

**Sensitive to study area size and settings**:

CSR assume points to be scattered all around the study area. Thus, Ripley's K function can be influenced by the size and shape of the study area. _Larger study areas_ may result in different K function estimates compared to smaller ones, and _irregular shapes_ can introduce biases. Additionally, the settings used for the K function analysis, such as the bandwidth or edge correction method, can impact the results.


```{figure} ../resources/w05-img/area_size.png
:label:
:alt:
:align: center

Effect of different area.
```


**Edge effect** (border effect):

Points beyond the study area are 'ignored.' _Points close to the boundary of the study area may have fewer neighboring points_ than those in the interior, which can bias the K function estimates. This is known as the edge effect, and it can introduce inaccuracies when studying spatial patterns. Edge correction methods are often employed to mitigate this issue.


```{figure} ../resources/w05-img/edge_effect.png
:label:
:alt:
:align: center

Edge Effect.
```


**Population-at-risk**:

Ripley's K function assumes that the underlying point process is _stationary and homogeneous_. If the population at risk (i.e., the underlying risk of events occurring) is not uniform across the study area, this can violate the assumptions and lead to misleading results. Incorporating information on the population at risk can help refine the analysis and improve the accuracy of the conclusions drawn from the K function.

```{figure} ../resources/w05-img/pop_at_risk.png
:label:
:alt:
:align: center

Population at risk.
```


## What has been covered in this chapter and section?

What is the workflow of analyzing spatial point pattern?

Global Pattern: the overall pattern of the point distribution

Local Pattern: where are the clusters


```{figure} ../resources/w05-img/about_point_pattern_analysis Diagram.drawio.png
:label:
:alt:
:align: center

Point pattern analysis.
```




## Some notes

The three methods explore the spatial pattern with different angle:
- Quadrat count: the number of points fall in equal size quadrats
- NNA: how near/far the nearest neighbor is
- K-function: how many other points could be found for a specific search radius

The latter two methods can be extended:
- NNA: to k-order nearest neighbor (see: [CrimeStat III](https://www.ojp.gov/pdffiles1/nij/grants/209264.pdf))
- K-function: weighted K-function (see: [ArcGIS Pro](https://pro.arcgis.com/en/pro-app/3.1/tool-reference/spatial-statistics/h-how-multi-distance-spatial-cluster-analysis-ripl.htm)])

Things to considered:
- Edge effect: the near border areas could be underestimated due to the external points. (see: .smaller[[DOI:10.2307/3237072](https://doi.org/10.2307/3237072)])
- Population at risk: a place with more population could have more events (e.g., crime/disease cases) happens by chance. (see: _SaTScan_(https://www.satscan.org/cgi-bin/satscan/register.pl/SaTScan_Users_Guide.pdf?todo=process_userguide_download)



## About Statistical Tests

There are so many tests. It is more important to know:
- The key considerations for choosing a test:
Understand the _assumptions, requirements, and limitations of each test_, as well as _the nature of your data_ and _research questions_, to select the most appropriate test.
    - Knowing these can help you to choose the appropriate test(s).

- What you're testing and why:
Be clear to yourself about the null and alternative hypotheses, _the rationale behind them_, and _the implications of your results_.
    - Are you testing against CSR? Why?

- Explicitly communicate your approach:
you have to explicitly tell your readers what, why, and how.
    - Don't let your readers guess.

_No single test is suitable for all situations, and it's impossible to memorize every test._
Instead, focus on developing a strong foundation in statistical concepts and _knowing where to find_ relevant information when selecting the appropriate test for your specific needs.

### About p-value
- p-value can only tell you how much risk you need to take if you reject H0.

- the common practice is to check if p-value $< \alpha$, and common alpha values are:
    - 0.05 for 95% confidence,
    - 0.01 for 99% confidence, and
    - 0.001 for 99.9% confidence.

- If p-value is less than the pre-determined $\alpha$, then it is significantly different.

- That's how far you can get with p-value---**don't over-interpret the p-value**.
    - Comparing p-values can be problematic, because they may be calculated from different settings, e.g., sample size.
