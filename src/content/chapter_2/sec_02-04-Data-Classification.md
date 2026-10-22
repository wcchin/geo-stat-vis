# Data Classification

Numerical classification groups values into intervals so that readers can compare categories rather than inspect every number. A classified map, table or matrix is simpler to read, but it discards within-class differences and introduces boundaries chosen by the analyst. “High” is therefore incomplete without a definition: high relative to what range, distribution or external threshold?

Here we classify the same 12 selected OD-pair counts. A national map is unnecessary: aligned bars show how class membership changes while the observations remain fixed. These are descriptive value classes, not spatial clusters, hypothesis-test results or evidence that a transport service is adequate.

## Equal intervals

Equal-interval classification divides the numerical range into $k$ intervals of the same width:

$$
w=\frac{x_{\max}-x_{\min}}{k}.
$$

For three classes from 50 to 4,294, the width is approximately 1,414.67. The interior breaks are 1,464.67 and 2,879.33. We include the minimum in the first class and assign a value exactly on an interior break to the lower class. The resulting class sizes are **10, 0 and 2**.

An empty middle class is a property of these boundaries and observed gaps, not a software failure. Equal intervals make equal numerical spans comparable, but they can place many observations together when a distribution is skewed. For comparison across times or groups, fixing one shared set of breaks preserves category meaning more clearly than recomputing the range separately for every panel.

## Quantiles

Quantile classification aims to distribute observations approximately equally among classes. For three classes with these 12 distinct values, linear-interpolated one-third and two-thirds quantiles are approximately 404.33 and 729.67. Class sizes are **4, 4 and 4**, with very different numerical spans.

Equal class counts can help reveal relative ordering, but they can separate similar values or group very different values together. The highest class here spans 1,113 through 4,294 trips. Recomputing quantiles for another month would keep a relative ranking interpretation, not necessarily a fixed level of activity. Tied observations complicate equal-sized classes: identical values should normally retain the same class, even if the resulting class sizes differ.

## Natural breaks

A common one-dimensional natural-breaks approach partitions ordered values into a specified number of contiguous groups to minimise within-class squared deviations. It seeks relatively compact groups separated by larger gaps. For three non-empty classes, exhaustive evaluation of this small dataset gives:

- 50–538: eight records;
- 1,113–1,385: two records;
- 3,092–4,294: two records.

Our implementation reports class upper limits 538, 1,385 and 4,294. Different software may display equivalent separating thresholds differently when no observation lies in the intervening gaps. Record the algorithm, class count and boundary convention when reproducing a classification.

```{figure} ../datasets/mrt_data_foundations_202609/figures/08_classification.png
:label: ch2-classification
:alt: Three panels classify the same sorted OD counts into three classes using equal intervals, quantiles and exact one-dimensional natural breaks.

Same records, values and order in every panel; colours indicate lower, middle and upper numerical classes. Class sizes are 10/0/2, 4/4/4 and 8/2/2 respectively. The natural-breaks calculation exhaustively evaluates possible partitions of this small sample; it does not identify spatial clusters.
```

Natural breaks adapts to the selected data. That can be useful for a single display, but it complicates comparison when each panel uses a different optimisation. An apparently similar colour could then mean a different numerical range. It also does not prove that the underlying population contains three natural types.

## Standard-deviation classes

Standard-deviation classification groups values by distances from the mean, often using breaks at the mean and selected multiples of the standard deviation. The breaks and treatment of tails must be specified. There is no single mandatory standard-deviation legend.

This approach answers a relative question: how far above or below the reference mean is an observation? It is easiest to read when the mean and standard deviation are informative summaries. In a skewed sample, many observations may lie below the mean and a few may dominate the upper classes. A label such as “more than one standard deviation above the mean” is descriptive; it is not automatically a statistically significant hotspot or an error.

## Head/tail breaks

Head/tail breaks was developed to express hierarchy in distributions with many small values and relatively few large values. It splits values at their arithmetic mean and can repeat the operation within the smaller, high-valued head under a stated stopping rule. The resulting number of classes need not be fixed in advance.

For our selected counts, the first mean is 1,075.33: eight observations are at or below it, and four are above it. This demonstrates the first split. We do not infer a heavy-tailed law from 12 selected records or choose a recursion rule merely to produce an attractive legend. A complete implementation must state how it handles equality and when it stops; a skewed histogram alone is insufficient justification for an elaborate hierarchy.

**Reading:** Jiang, B. (2013). *Head/Tail Breaks: A New Classification Scheme for Data with a Heavy-Tailed Distribution*. The Professional Geographer, 65(3), 482–494. [Publisher record](https://doi.org/10.1080/00330124.2012.700499). Read for the rationale and recursive procedure, rather than assuming that any unequal dataset meets its intended conditions.

## Choose classes for the comparison

| Purpose | A useful option | What must remain visible |
|---|---|---|
| Compare fixed activity levels across periods | Shared numerical breaks, possibly based on an external decision rule | Same units, exposure and class meanings in every panel |
| Compare relative position within a distribution | Quantiles | Sample definition, ties and changing numerical thresholds |
| Highlight large gaps in one dataset | Natural breaks | Chosen class count and sample-specific optimisation |
| Show distance from a reference mean | Standard-deviation classes | Reference sample, standard deviation convention and skewness |
| Explore a hierarchy of many small/few large values | Head/tail breaks where justified | Recursive rule, stopping criterion and evidence of suitability |

For an actual planning decision, externally justified thresholds may be more useful than any automatic classifier. Conversely, a continuous sequential colour scale may preserve more detail than a few classes. The choice should follow the audience's question, not a desire to fill every colour in a palette.

Classification changes visual emphasis without changing the observations. Keep exact values or a retrievable source table available, disclose class boundaries, and use consistent units and legends. The [bundled numerical audit](../datasets/mrt_data_foundations_202609/README.md) records all three worked classifications, including the quantile convention and right-closed interior breaks.

```{dropdown} Self-check: Why can the upper class contain two records in one display and four in another?
The methods define “upper” differently. Equal intervals use the numerical range; quantiles use relative position. Neither label identifies a significant spatial cluster. Inspect the thresholds and sample before comparing colours.
```
