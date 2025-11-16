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

```{figure} ./resources/w03-img/analysis_differences.png
:label:
:alt:
:align: center

The differences in petal length between the three species.
```

## Define Differences

In statistics, __"difference"__ typically refers to the extent to which two or more groups, samples, or observations differ from one another. This can be quantified and assessed through various statistical measures and analyses, depending on the nature of the data and research questions.

- Groups: by genders, by years, by types
- Data point in groups: individual participant, transaction, bus stop, district

```{figure} ./resources/w03-img/drawing-differences_groups.png
:label:
:alt:
:align: center

How to determine if they are different or not so different?
```



### Spotting The Differences

```{figure} ./resources/w03-img/measures_spread_4vars.png
:label:
:alt:
:align: center

The differences in the 4 variables between species.
```

## Hypothesis Testing
Hypothesis testing is a statistical method used to __evaluate claims__ or __assertions__ about a population parameter by __analyzing sample data__.

The goal is to determine if __the observed differences between groups or samples are statistically significant__ or **merely due to chance**.

#### What does it means by '__due to chance__'?

In another chapter, we talked about Normal Distribution, and why 'Normal' is 'Normal'.

When we get a set of samples, the samples' distribution tend to form a bell-shape, i.e., high at the middle (__the central tendency__), and dropped from middle to both sides (__the spread__).
**But why?**

```{figure} ./resources/w02-img/frequency_distribution_normal.png
:label:
:alt:
:align: center

The Normal Distribution.
```


The __variance__, or __spread__, of a dataset can result from various factors, including **random processes, natural variation, or systematic differences**. Despite this variability, data points often cluster around a __central value__ due to underlying patterns or tendencies within the population.

In other words, values that fall at positive or negative distances __from the mean may__ be influenced by **random factors or chance**. This also applies when we draw a value and obtain __an extreme value__ far from the center---such values can occur due to randomness or chance.

> Everything can happen by chance---so when we see one value that is away from the sample mean, it does not promise to be 'different' from the distribution.

]]

---
class: left, middle

.split-40[.column[
### Hypothesis Testing
#### What does it means by 'due to chance'?

<img src="resources/w03-img/demo_datapoint.png" width="80%" align="center">
.square[A data point compared to the distribution.]

].column[

Let's say we have a class of students, and their height values are measured and which shows a normal distribution (figure on left), i.e., mean=170, std=10.

At this point, you can view these students as .blue[a set of sample], sampling from the .blue[population] (the university).
The university's students height should (or can be assumed to) form a .blue[normal distribution].

Now, you get a student from the next door, and his height is 135. .red[Deos it means this person is different from the currect class?]

**Strategy for measuring difference of an individual data point from a distribution**
- .red[Calculate how far this data point is from the average of the distribution.]
- How many standard deviation it is from the distribution's mean? .blue[(the z-score that use mean and std)]
- How many deviance (MAD) it is from the distribution's median? .blue[(use median and MAD)]
]]

---
class: left, middle

.split-40[.column[
### Hypothesis Testing
#### Comparison of two distributions

<img src="resources/w03-img/demo_datapoint_2dist.png" width="80%" align="center">
.square[The distributions of two groups of students.]

].column[

Next, get a series of students' height from next door, perhaps the same number of students as the first class and which generate a distribution (another normal distribution).

.red[Then, how to compare them?]

**Central values and spread**
Central values can be represented by measures of central tendency, such as the mean, median, or mode. In many situations, particularly when data follow a normal distribution, .red[the combination of central tendency and spread can provide a helpful summary of the overall distribution] and its characteristics.

**Shape** and other measurements
Assume to be normal distribution

**Strategy for comparison**
- Compare the mean between the two distributions
- Compare the spread of the two distributions

]]

---
class: left, middle

.split-20[.column[
### Hypothesis Testing
#### Key Concepts

Hypothesis testing is a crucial tool in statistical inference and helps researchers make .red[data-driven decisions] about the relationships or differences between variables.

].column[

.bold[Null Hypothesis (H₀)]:
- A statement that assumes .red[no significant difference] between the variables.
- The goal of hypothesis testing is to gather .red[evidence .bold[to reject] the null hypothesis].
- Essentially, the null hypothesis reflects the idea of .blue.bold["no effect" or "no difference."]

.bold[Alternative Hypothesis (H₁)]:
- A statement that .red[assumes a significant difference] between the variables.
- This is the hypothesis .red[we .bold[aim to support] when rejecting the null hypothesis].
- The alternative hypothesis is basically about .blue.bold["has effect" or "has difference."]

.bold[Test Statistic]:
- A value calculated from the sample data to assess the likelihood of obtaining the observed results .red[under the assumption that the null hypothesis is true].
- Depending on the assumptions that fit the situation, the tests for assessing the differences are T-test, ANOVA, and their non-parametric alternatives.

]]

---
class: left, middle

.split-20[.column[
### Hypothesis Testing
#### Key Concepts

].column[
.bold[Significance Level (α)]:
- The threshold probability for rejecting the null hypothesis, often set at 0.05 or 0.01.
- It represents the probability threshold of incorrectly rejecting the null hypothesis when it is true (.red[Type I error]). .red[(The risk that we are willing to take.)]

.bold[p-value]:
- The probability of obtaining the observed results (or more extreme results) under the assumption that .underline[the null hypothesis is true].
- A small p-value indicates that the observed results are unlikely to occur by chance alone, providing evidence to reject the null hypothesis.
- .red[The risk of being wrong to reject H₀]

.bold[Statistical Significance]:
- When the p-value is less than the chosen significance level (α), we .red[reject the null hypothesis] and conclude that the results are statistically significant, .red[supporting the alternative hypothesis].
- .red[Otherwise, we fail to reject it].

]]

---
class: left, middle

.split-20[.column[
### Hypothesis Testing
#### About Type 1 and Type 2 errors

].column[

<img src="resources/w03-img/typeI_and_typeII_error.png" width="80%" align="center">
.square[Type 1 and type 2 errors. [Table from Wikipedia](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors)]

]]

---
class: left, middle

.split-20[.column[
### Hypothesis Testing
#### Testing the differences

].column[

.red[The null hypothesis reflects the idea of "no effect" or "no difference."]


Hypothesis for testing differences .red[between two means]:
$$\begin{align}
\text{H}_0 &: \mu_0 = \mu_1 \\\\
\text{H}_1 &: \mu_0 \neq \mu_1
\end{align}$$


Hypothesis for testing differences .red[between more than two means]:
$$\begin{align}
H_0 &: \mu_0 = \mu_1 = \mu_2 = ... = \mu_i  \\\\
H_1 &: \text{at least 2 of the }\mu_i\text{ are different}
\end{align}$$

Null hypothesis is something that we DO NOT NEED to prove, because it cannot be proven anyway.
- The null hypothesis is assumed to be true until the data provide sufficient evidence against it.
- We can only gather evidence to reject the null hypothesis, not to confirm or prove it.
- Failing to reject the null hypothesis doesn't necessarily mean it's true; it simply indicates that there's insufficient evidence to support the alternative hypothesis.

]]

---
class: left, middle

.split-40[.column[
### Hypothesis Testings in Spatial Patterns Detection
].column[
- Is the spatial pattern different from a random pattern?
    - null hypothesis: no difference
- Is there any significant clusters?
    - null hypothesis: no clustering effect
]]
