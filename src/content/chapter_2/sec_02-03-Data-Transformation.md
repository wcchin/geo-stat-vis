# 2.3 Data transformation

Transformations change how data are arranged, measured or represented. These operations are often discussed together, but their consequences differ. Before transforming a column, state the purpose: are we making a table easier to read, adjusting exposure, reducing differences in scale, or changing the relationship a model will describe?

Our MRT slice offers a useful distinction. Pivoting the 12 OD records into a matrix changes arrangement. Dividing a monthly count by the relevant number of days changes the measure. Applying a logarithm changes numerical scale. Changing only a plot's colour scale changes the visual encoding. None should be described simply as “normalising the data” without explaining the operation.

## Rearrangement preserves the observations

```{figure} ../datasets/mrt_data_foundations_202609/figures/04_od_matrix.svg
:label: ch2-od-matrix
:alt: Four-by-four directed OD matrix with origins as rows, destinations as columns, and missing diagonal cells retained as dashes.

The same selected records arranged as a matrix. Counts are September 2026 weekday hour-category 08 aggregates. The absent diagonal records remain missing; a dash is not an observed zero. The linear colour scale is sequential.
```

Rows are origins and columns are destinations. Bishan to Paya Lebar has 3,092 reported trips; the reverse direction has 342. A directed OD matrix need not be symmetric. Pivoting retains these differences and the total of 12,904. It does not reveal a route or distance.

A pivot requires a rule for repeated row/column combinations. Here, the temporal categories have already been fixed, so each reported ordered pair is unique. If we retained several hours, we would need another dimension or an explicitly chosen aggregation. A tool that silently averages repeated records could change the meaning of a trip count.

## Changing exposure changes the measure

Monthly counts for different day types do not have equal time exposure. If we want mean daily activity for a category, a suitable calculation is monthly category total divided by the number of relevant days. The denominator must correspond to the source's calendar and day-type definitions. “Weekends/holiday” needs particular care because public holidays can alter the category's exposure.

The figures here retain monthly counts. They are not daily estimates. Likewise, dividing station activity by residential population would create a different measure and require a defensible population denominator and catchment. A nearby population total is not automatically the population exposed to a station's service.

## Min–max scaling

For observed minimum $a$ and maximum $b$, scaling to the interval $[0,1]$ gives:

$$
x_i'=\frac{x_i-a}{b-a}.
$$

A general target interval $[a',b']$ uses $x_i'=a'+(x_i-a)(b'-a')/(b-a)$. The denominator is zero for a constant variable, so such a case needs an explicit rule. In our sample, $a=50$ and $b=4294$: the endpoints become 0 and 1, while 500 becomes about 0.106.

This positive linear rescaling preserves ordering and distributional shape apart from the horizontal scale. It does not remove skewness or make a variable normally distributed. It is sensitive to the chosen extrema: adding another large count would change the scaled positions of all existing observations. In a predictive workflow, estimate scaling parameters from training data and reuse them for validation data; new values may fall outside the original target range.

## Standardisation

Using the sample mean and sample standard deviation from the previous section:

$$
z_i=\frac{x_i-\bar{x}}{s}.
$$

The transformed sample has mean zero and sample standard deviation one, apart from numerical rounding. A count of 500 has a z-score of about -0.442: it lies 0.442 sample standard deviations below this selected sample's mean. It does not mean the count is negative.

Standardisation can help algorithms where differences in measurement scale influence a distance or penalty. However, it does not make unlike concepts substantively equivalent: a standardised housing price and a standardised boarding count still measure different things. Ordinary mean-and-standard-deviation scaling is sensitive to outliers, works with negative as well as positive inputs, and does not require a normal distribution. It does not itself remove skewness, dependence or correlations between variables.

## Logarithms and related power transformations

For positive values, a logarithmic transformation is $y_i=\log(x_i)$. In a logarithmic scale, equal ratios correspond to equal differences. For example, the natural-log difference between 500 and 50 is $\log(10)$, while their raw difference is 450. Large absolute gaps are compressed relative to a linear display.

For non-negative values, $\log(1+x_i)$ is sometimes used so that zero is defined. The added constant is a modelling choice tied to the units; it should be stated rather than used to conceal missing values or repair an unsuitable variable. An ordinary real-valued logarithm is undefined for zero and negative inputs. Changing the log base rescales the transformed values by a constant.

```{figure} ../datasets/mrt_data_foundations_202609/figures/07_transformations.png
:label: ch2-transformations
:alt: Ordered OD counts shown on their raw scale, min–max scale, sample z-score scale, and natural log of one plus count scale.

The same 12 records in a fixed order. Positive linear rescalings preserve the spacing pattern up to a scale change; the logarithmic transformation compresses large values. No normality claim follows from any panel.
```

A log transformation may help with strongly varying positive quantities or a multiplicative relationship. Whether it improves a model depends on the model and its diagnostics. For regression, requirements often concern conditional errors rather than a demand that every input variable look bell-shaped. Transforming a variable does not resolve spatial dependence, an inappropriate observation unit or an incorrect join.

::::{dropdown} Go deeper: the Box–Cox family

The Box–Cox family extends the idea for strictly positive data:

$$
y_i(\lambda)=
\begin{cases}
(x_i^\lambda-1)/\lambda,&\lambda\ne0,\\
\log(x_i),&\lambda=0.
\end{cases}
$$

At $\lambda=0.5$, it is proportional to a square-root transform with an offset; it is not exactly $\sqrt{x_i}$. Selecting $\lambda$ should follow an explicit criterion in the intended model. We do not estimate an optimal transformation from these 12 teaching records. Box and Cox's original paper explains the model-based rationale; a transformed histogram alone is not a complete selection criterion.

::::

## Ranks retain order and discard magnitude

Ranking assigns positions to sorted values. The smallest count receives rank 1 and the largest rank 12. The gap between ranks 11 and 12 is one even though their raw counts differ by 1,202. Ranks can support order-based comparisons, but they discard information about the size of differences. Ties require a convention such as average ranks.

A uniform sequence of ranks without ties is produced by the ranking operation itself. It does not establish that the original variable had a uniform distribution. Similarly, replacing counts with class labels is a deliberate loss of numerical detail, examined in the next section.

## Select a transformation for a reason

Keep original quantities alongside derived columns, document fitted parameters, and label plots with the correct units. When only a colour scale is transformed, retain a legend that explains the encoding; do not describe unchanged cell labels as transformed observations. Ask whether the operation preserves the comparison that matters. For example, a log-scaled view helps compare ratios, while a linear view makes absolute differences more direct.

**Reading:** Box, G. E. P., & Cox, D. R. (1964). *An Analysis of Transformations*. Journal of the Royal Statistical Society: Series B, 26(2), 211–243. [Publisher record](https://academic.oup.com/jrsssb/article/26/2/211/7028064). The article develops transformations within statistical models; this chapter introduces the basic ideas without fitting that full framework.

**Self-check:** Does standardisation make these counts normally distributed?

```{dropdown} Feedback
No. Subtracting the mean and dividing by a positive standard deviation changes location and scale. It preserves the distribution's shape and does not remove skewness or dependence.
```
