# The Hypothesis Testing

**What is the first step of getting your hands dirty?**


:::{table} Iris dataset.
:label: iris
:align: center

| ID | Variety   |   Sepal Length |   Sepal Width |   Petal Length |   Petal Width |
|:---|:----------|---------------:|--------------:|---------------:|--------------:|
|  0 | Setosa    |            5.1 |           3.5 |            1.4 |           0.2 |
|  1 | Setosa    |            4.9 |           3   |            1.4 |           0.2 |
|  2 | Setosa    |            4.7 |           3.2 |            1.3 |           0.2 |
|  3 | Setosa    |            4.6 |           3.1 |            1.5 |           0.2 |
|  4 | Setosa    |            5   |           3.6 |            1.4 |           0.2 |
| .. |       ... |            ... |           ... |            ... |           ... |

:::

First Step: Draw the frequency distribution.

Below is an example of Iris' petal length from week 1, when we talked about the analysis of differences.

The frequency distributions were drawn separately for different species of Iris, which provided a visual comparison between the three species.

*Are them different?*

```{figure} ../resources/w03-img/analysis_differences.png
:label:
:alt:
:align: center

The differences in petal length between the three species.
```

## Define Differences

In statistics, _"difference"_ typically refers to the extent to which two or more groups, samples, or observations differ from one another. This can be quantified and assessed through various statistical measures and analyses, depending on the nature of the data and research questions.

- Groups: by genders, by years, by types
- Data point in groups: individual participant, transaction, bus stop, district

```{figure} ../resources/w03-img/drawing-differences_groups.png
:label:
:alt:
:align: center

How to determine if they are different or not so different?
```



### Spotting The Differences

```{figure} ../resources/w03-img/measures_spread_4vars.png
:label:
:alt:
:align: center

The differences in the 4 variables between species.
```

## Hypothesis Testing
Hypothesis testing is a statistical method used to _evaluate claims_ or _assertions_ about a population parameter by _analyzing sample data_.

The goal is to determine if _the observed differences between groups or samples are statistically significant_ or **merely due to chance**.

### What does it means by '_due to chance_'?

In another chapter, we talked about Normal Distribution, and why 'Normal' is 'Normal'.

When we get a set of samples, the samples' distribution tend to form a bell-shape, i.e., high at the middle (_the central tendency_), and dropped from middle to both sides (_the spread_).
**But why?**

```{figure} ../resources/w02-img/frequency_distribution_normal.png
:label:
:alt:
:align: center

The Normal Distribution.
```


The _variance_, or _spread_, of a dataset can result from various factors, including **random processes, natural variation, or systematic differences**. Despite this variability, data points often cluster around a _central value_ due to underlying patterns or tendencies within the population.

In other words, values that fall at positive or negative distances _from the mean may_ be influenced by **random factors or chance**. This also applies when we draw a value and obtain _an extreme value_ far from the center---such values can occur due to randomness or chance.

> Everything can happen by chance---so when we see one value that is away from the sample mean, it does not promise to be 'different' from the distribution.

```{figure} ../resources/w03-img/demo_datapoint.png
:label: demodata
:alt:
:align: center

A data point compared to the distribution.
```


Let's say we have a class of students, and their height values are measured and which shows a normal distribution ([](#demodata)), i.e., mean=170, std=10.

At this point, you can view these students as _a set of sample_, sampling from the _population_ (the university).
The university's students height should (or can be assumed to) form a _normal distribution_.

Now, you get a student from the next door, and his height is 135. **Deos it means this person is different from the currect class?**

**Strategy for measuring difference of an individual data point from a distribution**
- _Calculate how far this data point is from the average of the distribution._
- How many standard deviation it is from the distribution's mean? _(the z-score that use mean and std)_
- How many deviance (MAD) it is from the distribution's median? _(use median and MAD)_



## Comparison of two distributions

```{figure} ../resources/w03-img/demo_datapoint_2dist.png
:label:
:alt:
:align: center

The distributions of two groups of students.
```


Next, get a series of students' height from next door, perhaps the same number of students as the first class and which generate a distribution (another normal distribution).

*Then, how to compare them?*

**Central values and spread**
Central values can be represented by measures of central tendency, such as the mean, median, or mode. In many situations, particularly when data follow a normal distribution, _the combination of central tendency and spread can provide a helpful summary of the overall distribution_ and its characteristics.

**Shape** and other measurements
Assume to be normal distribution

**Strategy for comparison**
- Compare the mean between the two distributions
- Compare the spread of the two distributions



### Key Concepts

Hypothesis testing is a crucial tool in statistical inference and helps researchers make _data-driven decisions_ about the relationships or differences between variables.

**Null Hypothesis ($\text{H}_0$)**:
- A statement that assumes _no significant difference_ between the variables.
- The goal of hypothesis testing is to gather _evidence **to reject** the null hypothesis_.
- Essentially, the null hypothesis reflects the idea of _"no effect" or "no difference."_

**Alternative Hypothesis ($\text{H}_1$ or $\text{H}_a$)**:
- A statement that _assumes a significant difference_ between the variables.
- This is the hypothesis _we **aim to support** when rejecting the null hypothesis_.
- The alternative hypothesis is basically about _"has effect" or "has difference."_

**Test Statistic**:
- A value calculated from the sample data to assess the likelihood of obtaining the observed results _under the assumption that the null hypothesis is true_.
- Depending on the assumptions that fit the situation, the tests for assessing the differences are T-test, ANOVA, and their non-parametric alternatives.

**Significance Level ($\alpha$)**:
- The threshold probability for rejecting the null hypothesis, often set at 0.05 or 0.01.
- It represents the probability threshold of incorrectly rejecting the null hypothesis when it is true (_Type I error_). _(The risk that we are willing to take.)_

**p-value**:
- The probability of obtaining the observed results (or more extreme results) under the assumption that _the null hypothesis is true_.
- A small p-value indicates that the observed results are unlikely to occur by chance alone, providing evidence to reject the null hypothesis.
- _The risk of being wrong to reject $\text{H}_0$_

**Statistical Significance**:
- When the p-value is less than the chosen significance level ($\alpha$), we _reject the null hypothesis_ and conclude that the results are statistically significant, _supporting the alternative hypothesis ($\text{H}_1$)_.
- _Otherwise, we fail to reject it_.


### About Type 1 and Type 2 errors

```{figure} ../resources/w03-img/typeI_and_typeII_error.png
:label:
:alt:
:align: center

Type 1 and type 2 errors. [Table from Wikipedia](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors)
```


## Hypothesis for Testing the Differences

**The null hypothesis reflects the idea of "no effect" or "no difference."**

Hypothesis for testing differences _between two means_:
$$\begin{align}
\text{H}_0 &: \mu_0 = \mu_1 \\\\
\text{H}_1 &: \mu_0 \neq \mu_1
\end{align}$$


Hypothesis for testing differences _between more than two means_:
$$\begin{align}
\text{H}_0 &: \mu_0 = \mu_1 = \mu_2 = ... = \mu_i  \\\\
\text{H}_1 &: \text{at least 2 of the }\mu_i\text{ are different}
\end{align}$$

Null hypothesis is something that we **DO NOT NEED** to prove, because it cannot be proven anyway.
- The null hypothesis is assumed to be true until the data provide sufficient evidence against it.
- We can only gather evidence to reject the null hypothesis, not to confirm or prove it.
- Failing to reject the null hypothesis doesn't necessarily mean it's true; it simply indicates that there's insufficient evidence to support the alternative hypothesis.


## For Spatial Patterns Detection

- Is the spatial pattern different from a random pattern?
    - null hypothesis: no difference

- Is there any significant clusters?
    - null hypothesis: no clustering effect
