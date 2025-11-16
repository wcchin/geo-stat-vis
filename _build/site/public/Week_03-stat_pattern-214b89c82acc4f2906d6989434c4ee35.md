slide_title: Week 03 - Statistical Pattern II
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

## Statistical Pattern II: Analyzing & Visualizing Differences 
------

<br />

.x-large.bold[Dr. CHIN Wei Chien Benny]  
[.underline.square[wcchin@nus.edu.sg]]  

.headnote.square.bold.x-large[GE5230 Geospatial Statistics and Visualization]
.footnote.square[03 @ 2025-08-28 Department of Geography, NUS]

---
layout: false
class: left, middle
## Objectives of this lecture
- To know how to measure and visualize differences
- To learn t-test and when to use it
- To learn ANOVA and when to use it
- To learn non-parametric tests and when to use them


---
class: center, middle, inverse

.xx-large.bold.wide[PART 1]
## The Hypothesis Testing
------
.square[Differences .dot[] Hypothesis Testing.dot[] 'By Chance' .dot[] Null Hypothesis]

.headnote.square.bold.x-large[Statistical Pattern II]

---
class: left, middle

.split-40[.column[
### What is the first step of getting your hands dirty?
].column[
    
Table 1. Iris dataset. 

| ID | Variety   |   Sepal Length |   Sepal Width |   Petal Length |   Petal Width |
|:---|:----------|---------------:|--------------:|---------------:|--------------:|
|  0 | Setosa    |            5.1 |           3.5 |            1.4 |           0.2 |
|  1 | Setosa    |            4.9 |           3   |            1.4 |           0.2 |
|  2 | Setosa    |            4.7 |           3.2 |            1.3 |           0.2 |
|  3 | Setosa    |            4.6 |           3.1 |            1.5 |           0.2 |
|  4 | Setosa    |            5   |           3.6 |            1.4 |           0.2 |
| .. |       ... |            ... |           ... |            ... |           ... |

]]

---
class: left, middle

.split-40[.column[
### What is the first step of getting your hands dirty?
First Step: Draw the frequency distribution. 

On the right is an example of Iris' petal length from week 1, when we talked about the analysis of differences. 

The frequency distributions were drawn separately for different species of Iris, which provided a visual comparison between the three species. 

.xkcd.red[Are them separated?]

].column[

<img src="resources/w03-img/analysis_differences.png" width="90%" align="center">  
.square[The differences in petal length between the three species.]

]]

---
class: left, middle
.split-30[.column[
### Define Differences
].column[
In statistics, "difference" typically refers to the extent to which two or more groups, samples, or observations differ from one another. This can be quantified and assessed through various statistical measures and analyses, depending on the nature of the data and research questions.

<img src="resources/w03-img/drawing-differences_groups.png" width="70%" align="center">  

- Groups: by genders, by years, by types
- Data point in groups: individual participant, transaction, bus stop, district

]]

---
class: center, middle

### Spotting The Differences

<img src="resources/w03-img/measures_spread_4vars.png" width="100%" align="center">  
.square[The differences in the 4 variables between species.]

---
class: left, middle

.split-40[.column[
### Hypothesis Testing
].column[
Hypothesis testing is a statistical method used to .red[evaluate claims] or .red[assertions about a population parameter by .underline[analyzing sample data]]. 

The goal is to determine if .red[the observed differences between groups or samples are statistically significant] or .bold.red[merely due to chance].

.xkcd.red[due to chance?]
]]

---
class: left, middle

.split-40[.column[
### Hypothesis Testing
#### What does it means by '.red[due to chance]'?

Last week, we talked about Normal Distribution, and why 'Normal' is 'Normal'. 

When we get a set of samples, the samples' distribution tend to form a bell-shape, i.e., high at the middle (.blue[the central tendency]), and dropped from middle to both sides (.blue[the spread]).  
.red.bold[But why?]

].column[

<img src="resources/w02-img/frequency_distribution_normal.png" width="80%" align="center">  
.square[The Normal Distribution.]

]]

---
class: left, middle

.split-40[.column[
### Hypothesis Testing
#### What does it means by 'due to chance'?


<img src="resources/w02-img/frequency_distribution_normal.png" width="80%" align="center">  

].column[

The .blue[variance], or .blue[spread], of a dataset can result from various factors, including .red[random processes, natural variation, or systematic differences]. Despite this variability, data points often cluster around a .blue[central value] due to underlying patterns or tendencies within the population. 

In other words, values that fall at positive or negative distances .blue[from the mean may] be influenced by .red.bold[random factors or chance]. This also applies when we draw a value and obtain .red[an extreme value] far from the center---such values can occur due to randomness or chance. 

.red[Everything can happen by chance---so when we see one value that is away from the sample mean, it does not promise to be 'different' from the distribution.]  

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


---
class: center, middle, inverse

.xx-large.bold.wide[PART 2]
## The T-test
------
.square[Assumptions .dot[] Types .dot[] Interpretation .dot[] Effect Size]

.headnote.square.bold.x-large[Statistical Pattern II]

---
class: left, middle

.split-30[.column[
### Assumptions of t-tests
<img src="resources/w03-img/demo_datapoint_2dist.png" width="80%" align="center">  
.square[The distributions of two groups of students.]
].column[
To ensure the validity of the results, the t-test relies on certain assumptions:
- .bold[Continuous]:  
The data (target variable) should be continuous (interval/ratio).
- .bold[Normality]:  
The data should be approximately normally distributed.
- .bold[Independence]:  
Observations .red[within and between groups] should be independent (not influence one another).
- .bold[Homogeneity of variances]:  
The variances (or standard deviations) of the groups should be approximately equal (this assumption can be relaxed for some t-tests).

]]

---
class: left, middle

### Two Types of 'Groups': Between vs. Within

.split-50[.column[
#### 'Between'-Group Analysis
- Number of subject groups: 2 or more
- Number of target variables: 1 (for every subject)
- Purpose: To compare differences among distinct groups of subjects.

].column[
#### 'Within'-Group Analysis
- Number subject groups: 1
- Number of target variables: 2 or more (for every subject)
- Purpose: To examine the differences or changes within a single group over time or under different conditions.  
]]

---
class: left, middle

.split-30[.column[
### Types of t-tests
].column[
There are three main types of t-tests:
- One sample t-test
- Independent samples t-test
- Paired samples t-test

<img src="resources/w03-img/Types_of_t-test.png" width="60%" align="center">  
.square[Source: [Datatab](https://datatab.net/tutorial/t-test)]
]]

---
class: left, middle

.split-30[.column[
### Types of t-tests
- .red[One sample t-test]
- Independent samples t-test
- Paired samples t-test
].column[
.bold[One sample t-test]:  
- .red.bold[Compares the mean of a single group to a known population mean.]
- E.g., the students' performances from one school compared to the national mean; the air polution level compared to the safety standards...
- Each individual or observation in the sample contributes to a single group being compared to the known population mean.

<img src="resources/w03-img/Example_one-sample_t-test.png" width="60%" align="center">  
.square[Source: [Datatab](https://datatab.net/tutorial/t-test)]
]]

---
class: left, middle

.split-30[.column[
### Types of t-tests
- .red[One sample t-test]
- Independent samples t-test
- Paired samples t-test
].column[
#### An example
A factory claims that their light bulbs have an average lifespan of $1,000$ hours. A consumer group selects a random sample of $25$ bulbs and finds that the sample has an average lifespan of $985$ hours with a standard deviation of $50$ hours. .red[The consumer group wants to determine whether the factory's claim is accurate.]

```
[ 935,  969,  917,  922,  906, 1022,  984, 1023, 1042,  944,
  982, 1054,  923, 1012,  963, 1011,  924, 1026, 1081,  932,
 1027,  947,  994, 1016, 1069 ]
```

<img src="resources/w03-img/ttest_one_sample.png" width="90%" align="center">  

]]

---
class: left, middle

.split-30[.column[
### Types of t-tests
#### An example
- .red[One sample t-test]
- Independent samples t-test
- Paired samples t-test

.bold[Conclusion]:  
The consumer group .red[cannot conclude] that the factory's claim is inaccurate based on this sample. There is .red[not enough evidence to reject the null hypothesis] that the average lifespan of the light bulbs is 1,000 hours.

].column[
Steps involved in the one-sample t-test:
- Formulate the .underline[null hypothesis] (H₀) and the .underline[alternative hypothesis] (H₁):
    - H₀: The average lifespan of the light bulbs is 1,000 hours (μ = 1,000).
    - H₁: The average lifespan of the light bulbs is not 1,000 hours (μ ≠ 1,000).
- Calculate the .underline[t-test statistic] (t) using the formula:
    - t = (sample mean - population mean) / (standard error of the mean)
    - standard error of the mean = std / sqrt(n) = 50/sqrt(25) = 50/5 = 10
    - Plugging in the values: t ≈ (985 - 1,000) / 10 = -1.5
- Determine the .underline[degrees of freedom] (df), which is equal to 
    - the sample size minus 1 (df = n - 1);
    - df = 25 - 1 = 24.
- Using the t-value (-1.5) and degrees of freedom (24), find the .underline[p-value] associated with the test statistic from the t-distribution table or by using statistical software:
- The .red.bold[p-value is approximately 0.16].
    - Since the p-value (0.16) is greater than the conventional significance level of 0.05, we fail to reject the null hypothesis.
]]

---
class: left, middle

.split-30[.column[
### Types of t-tests
- One sample t-test
- .red[Independent samples t-test]
- Paired samples t-test
].column[

.bold[Independent samples t-test]:  
- .red.bold[Compares the means of two independent groups.]
- E.g., the scores of students from two classes; the effect of treatment vs. placebo-control groups...
- .underline[Every individual will only appear in only one of the two groups.] 

<img src="resources/w03-img/Example_of_a_t-test_for_independent_samples.png" width="40%" align="center">  
.square[Source: [Datatab](https://datatab.net/tutorial/t-test)]
]]

---
class: left, middle

.split-50[.column[
### Types of t-tests
- One sample t-test
- .red[Independent samples t-test]
- Paired samples t-test

In each subplot, the mean of two Iris species were compared. 

].column[
<img src="resources/w03-img/analysis_differences--ttest.png" width="90%" align="center">  
.square[The differences in petal length between the three species, with t-test results.]
]]

---
class: left, middle

.split-30[.column[
### Types of t-tests
- One sample t-test
- Independent samples t-test
- .red[Paired samples t-test]
].column[
.bold[Paired samples t-test]:
- .red.bold[Compares the means of two related or paired groups.]
- E.g., pre-test and post-test scores from the same group of individuals; differences between spouses or siblings...
- Every individual in the pre-test group must also be present in the post-test group, or .underline[each individual in one group should have a specific counterpart in the other group.]

<img src="resources/w03-img/Example_of_the_t-test_for_paired_samples.png" width="40%" align="center">  
.square[Source: [Datatab](https://datatab.net/tutorial/t-test)]
]]

---
class: center, middle

<img src="resources/w03-img/psychology_data_lineplot-b.png" width="80%" align="center">  
.square[The changes of psychological indexes before and after a VR treatment. T-test and significant levels are shown at top right. [10.1016/j.jenvp.2023.102012](https://doi.org/10.1016/j.jenvp.2023.102012)]

---
class: left, middle

.split-30[.column[
### T-Test Statistic and Interpretation
].column[
.bold[T-value] (aka T-statistic)

The t-test calculates a t-value by dividing the difference between the group means by the standard error of the difference. .red[A higher t-value (positive or negative) suggests a larger inter-group difference] relative to the intra-group variability.

.bold[P-value]

The t-test also provides a p-value, which represents the probability of observing a t-value at least as extreme as the one calculated, assuming the null hypothesis is true. .red[A lower p-value indicates stronger evidence] against the null hypothesis, suggesting a significant difference between the groups.

.bold[Degrees of Freedom]

Degrees of freedom (df) are used to determine the appropriate t-distribution for calculating p-values. For independent samples t-test, df = n₁ + n₂ - 2, where n₁ and n₂ are the sample sizes of the two groups.
]]



---
class: left, middle

.split-30[.column[
### T-Test Statistic and Interpretation

To assess the .red[practical significance of the difference between group means], effect size measures like Cohen's d, Eta-squared, and Hedge's g can be calculated. Cohen's d indicates the magnitude of the difference between the groups in standard deviation units.
].column[

.bold[Effect Size]

- .bold[Cohen's d]:  
Cohen's d is a standardized measure of effect size, often used in comparing the means of two groups. It expresses the difference between group means in terms of standard deviations, making it a useful metric for comparing effects across different studies. The guidelines proposed by Jacob Cohen for interpreting d are:
    - Small effect: d = 0.2
    - Medium effect: d = 0.5
    - Large effect: d = 0.8
- .bold[Eta-squared (η²)]:  
Eta-squared is often reported in the context of ANOVA (Analysis of Variance) tests. It describes the proportion of variance in the dependent variable that can be explained by the independent variable. Eta-squared values range from 0 to 1, with higher values indicating larger effects. Here are some general guidelines for interpreting η²:
    - Small effect: η² = 0.01
    - Medium effect: η² = 0.06
    - Large effect: η² = 0.14
]]

---
class: left, middle

.split-30[.column[
### T-Test Statistic and Interpretation

.bold[Summary]

The t-test is widely used in various fields to compare group means and evaluate the effectiveness of treatments, interventions, or different conditions. It serves as an essential tool for hypothesis testing and data analysis.

].column[
- .bold[Hedge's g]:  
Hedge's g, like Cohen's d, is a standardized effect size measure for comparing two group means. However, it includes a correction for bias in small samples, making it more appropriate than Cohen's d when sample sizes are small. The interpretation guidelines for Hedge's g are similar to Cohen's d:
    - Small effect: g = 0.2
    - Medium effect: g = 0.5
    - Large effect: g = 0.8

- .bold[Common Language Effect Size]:  
The Common Language Effect Size (CLES) is a non-parametric effect size measure that communicates the likelihood that a randomly selected observation from one group will be greater than a randomly selected observation from another group. CLES offers a more intuitive understanding of statistical results, making it easier for researchers and non-experts to interpret the practical significance of findings.

]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 3]
## The Analysis of Variance
------
.square[Assumptions .dot[] Types .dot[] Interpretation .dot[] Posthoc Tests]

.headnote.square.bold.x-large[Statistical Pattern II]

---
class: left, middle

.split-30[.column[
### What is Analysis of Variance
].column[
.bold[Definition]:  
Analysis of Variance, aka ANOVA, is a statistical method used to compare the means of .red[more than two groups] to determine whether there is a significant difference between them.

The primary purpose of ANOVA is to test the hypothesis that the means of several populations are equal. It helps determine .red[whether any observed differences between group means are real or occurred by chance].

.bold[When to use ANOVA]:  
ANOVA is used when comparing more than two group means. It is particularly useful in experimental settings where a single factor (independent variable, one-way ANOVA) is .red[manipulated at multiple levels] (e.g., low, medium, high), and .red[the researcher wants to investigate the effect of .red[this manipulation] on the outcome] (dependent variable).
]]

---
class: left, middle
.split-30[.column[
### Assumptions of ANOVA
].column[
ANOVA is based on the following assumptions:
- .bold[Numeric Response]: The .red[target (dependent) variable] should be continuous, either ratio or interval. 
- .bold[Normality]: The data within each group should be approximately normally distributed.
- .bold[Equal Variances (homoscedasticity)]: The variances of the populations being compared should be roughly equal.
- .bold[Independence]: Observations should be independent of each other. This means that the data from one subject should not influence the data from another subject.
- .bold[Categorical treatment or factor variables]: ANOVA evaluates mean differences between one or more categorical variables (such as treatment groups), which are referred to as factors or “ways.”

Note: It is essential to verify that these assumptions are met before conducting ANOVA. If assumptions are not satisfied, the validity of the F-test may be compromised. In such cases, alternative methods such as .underline[repeated measure ANOVA, Welch's ANOVA, non-parametric tests] or more robust techniques may be considered.
]]

---
class: center, middle

### Analysis process for ANOVA
<img src="resources/w03-img/anova_ttest.drawio.png" width="90%" align="center">  
.square[The analysis process for t-test, ANOVA, and post-hoc test. ]


---
class: left, middle

.split-40[.column[
### Types of ANOVA 
Here only some commonly used types are introduced. Other types, e.g,. two-ways, three-ways, nested, Welch's ANOVA... are not covered here since those data is less common, and the concept is similar (anyway). 
].column[
- One-way ANOVA
    - between groups
    - the simplest and straighforward situation
- Repeated Measures ANOVA 
    - within group
    - when the groups are not independent
- Mixed-Design ANOVA 
    - when both between and within occurs
]]

---
class: left, middle

.split-40[.column[
### Types of ANOVA 
- .red[One-way ANOVA]
- Repeated Measures ANOVA
- Mixed-Design ANOVA
].column[
#### One-way ANOVA
.bold[Concept]  
One-way ANOVA is a statistical technique used to compare the target variable's means of .red[three or more independent groups] with .red[a single independent variable] (or factor). It helps determine whether any observed differences between group means are real or occurred by chance.

.bold[Example]  
To compare the average test scores of students who received different teaching methods.

.bold[Hypothesis Tested in One-way ANOVA]
- $H_0$: The population means of the groups being compared are equal.
Symbolically: $μ_1 = μ_2 = μ_3 = ... = μ_k$, where μ_i represents the mean of the ith group, and k is the total number of groups.
- $H_1$: At least one of the group means is different from the others.
]]

---
class: center, middle
#### One-way ANOVA
<img src="resources/w03-img/measures_spread_4vars.png" width="90%" align="center">  
.square[The One-way ANOVA comparing the four target variables between the three species. ]

---
class: left, middle
.split-30[.column[
#### One-way ANOVA
].column[
Table 1. The ANOVA result for the four target variables. Each row display the result from a single ANOVA.  All were significant. 

| variety      |   ddof1 |   ddof2 |        F |   p-unc |   np2 |
|:-------------|--------:|--------:|---------:|--------:|------:|
| petal.length |       2 |     147 | 1180.16  |   0.000 | 0.941 |
| petal.width  |       2 |     147 |  960.007 |   0.000 | 0.929 |
| sepal.length |       2 |     147 |  119.265 |   0.000 | 0.619 |
| sepal.width  |       2 |     147 |   49.16  |   0.000 | 0.401 |
]]

---
class: left, middle

.split-40[.column[
### Types of ANOVA 
- One-way ANOVA
- .red[Repeated Measures ANOVA]
- Mixed-Design ANOVA
].column[
#### Repeated Measures ANOVA
.bold[Concept]  
Repeated measures ANOVA, also known as .red[within-subjects] ANOVA, is a statistical technique used to compare means of .red[three or more dependent groups] when the same subjects are .red[observed under various conditions or at different points in time.]

.bold[Example]  
To compare the reaction times of a group of participants before, during, and after receiving a treatment.

.bold[Hypothesis Tested in Repeated Measures ANOVA]  
- $H_0$: The population means of the different conditions or time points are equal.
Symbolically: $μ_1 = μ_2 = μ_3 = ... = μ_k$, where μi represents the mean of the ith condition or time point, and k is the total number of conditions or time points.
- $H_1$: At least one of the population means is different from the others.
Symbolically: There exists at least one i and j such that $μ_i ≠ μ_j$.
]]

---
class: center, middle
#### Repeated Measures ANOVA
<img src="resources/w03-img/physiology_data_lineplot-b.png" width="90%" align="center">  
.square[The physiological responses before, during and after two types of VR treatments. ]

---
class: center, middle
#### Repeated Measures ANOVA
<img src="resources/w03-img/physiology_data_lineplot-b-tables.png" width="90%" align="center">  
.square[The tables about the repeated measures and post-hoc results: (left) low decibel, (right) high decibel. ]

---
class: left, middle

.split-40[.column[
### Types of ANOVA 
- One-way ANOVA
- Repeated Measures ANOVA
- .bold[Mixed-Design ANOVA]
].column[
#### Mixed-Design ANOVA

.bold[Concept]  
Mixed-design ANOVA, also known as split-plot ANOVA, is a statistical method used for analyzing data from studies with both between-subjects factors and within-subjects factors. It .red[combines features of one-way ANOVA and repeated measures ANOVA], allowing researchers to examine the effects of multiple independent variables on a dependent variable.

.bold[Key Points]  
- .red[Between-subjects factors] involve comparisons between different groups of participants, similar to one-way ANOVA.
- .red[Within-subjects factors] involve comparisons within the same group of participants at different time points or under various conditions, similar to repeated measures ANOVA.
- Mixed-design ANOVA enables researchers to assess the main effects of each factor and the potential interaction effects between factors.
]]

---
class: left, middle

.split-40[.column[
### Types of ANOVA 
- One-way ANOVA
- Repeated Measures ANOVA
- .bold[Mixed-Design ANOVA]
].column[
#### Mixed-Design ANOVA

.bold[Assumptions]  
The assumptions of mixed-design ANOVA are similar to those of one-way and repeated measures ANOVA, including normality, homogeneity of variances, and independence. Additionally, the assumption of .underline[sphericity] must be met for the .underline[within-subjects factor].

.bold[Use case]  
By using mixed-design ANOVA, researchers can gain a deeper understanding of the complex relationships between multiple factors and their effects on the dependent variable. It's a powerful tool for analyzing data from various experimental designs, particularly in fields such as psychology, medicine, and education.

]]

---
class: center, middle

#### Mixed-Design ANOVA
<img src="resources/w03-img/mixed-anova.png" width="70%" align="center">  
.square[The mixed ANOVA result between classes, time (pre-test vs. post-test), and the interaction between class and time. ]

---
class: center, middle

#### Mixed-Design ANOVA
<img src="resources/w03-img/mixed-anova_posthoc.png" width="60%" align="center">  
.square[The post-hoc test after mixed ANOVA, to observe the time effects in different condition. ]

---
class: left, middle

.split-40[.column[
### F-test and F-distribution
#### F-test and F-statistic
].column[

The F-test is a statistical test used in ANOVA to compare variances and determine whether there is a significant difference between group means. The F-statistic (or F-ratio) is calculated as .red[the ratio of the between-group variance to the within-group variance]:
$$
F = (\text{Between-group variance}) / (\text{Within-group variance})
$$

The F-statistic reflects the extent to which .red[the variation between groups exceeds the variation within groups].  
A higher F-value indicates a greater difference between group means relative to the variability within each group.
]]

---
class: left, middle

.split-40[.column[
### F-test and F-distribution
#### F-distribution and its relationship with the F-test
].column[
Under the null hypothesis that all group means are equal, the F-statistic follows an F-distribution, which is a family of continuous probability distributions characterized by two parameters: .red[degrees of freedom for the .bold[numerator] ($\text{ddof}_1$) and degrees of freedom for the .bold[denominator] ($\text{ddof}_2$)].  

The F-distribution is used to determine the .red[critical F-value] for a given significance level ($\alpha$) and degrees of freedom ($\text{ddof}_1$ and $\text{ddof}_2$). This critical value is compared with the calculated F-statistic .red[to make a decision] about the null hypothesis.
]]

---
class: left, middle

.split-40[.column[
### F-test and F-distribution
#### Making decisions in ANOVA using the F-value
].column[
- To make decisions in ANOVA, the calculated F-statistic is compared to the critical F-value obtained from the F-distribution.

- If the F-statistic is .red.bold[larger] than the critical F-value, we .red[.bold[reject]] the null hypothesis, concluding that .red[at least one group mean is significantly] different from the others.

- If the F-statistic is .red.bold[smaller] than the critical F-value, we .red[.bold[fail to reject]] the null hypothesis, concluding that there is .red[insufficient evidence to claim a significant] difference between group means.

- In practice, a p-value is often computed and compared to a predetermined significance level ($\alpha$) to make this decision. .red[If the p-value is smaller than $\alpha$, the null hypothesis is rejected.] 
]]

---
class: left, middle

.split-40[.column[
### Post-hoc Tests
].column[

#### Purpose of Post-hoc Tests
Post-hoc tests are follow-up analyses conducted .red[.bold[after] a significant overall F-test in ANOVA]. Their purpose is to determine .red[which specific group means] are significantly different from one another. Since ANOVA only tells us that at least two means are different, .red[post-hoc tests help pinpoint where those differences lie].
]]

---
class: left, middle

.split-30[.column[
### Post-hoc Tests
].column[
#### Common post-hoc tests

.bold[Tukey's HSD Test]:
- Simultaneously compares all possible pairs of means.
- Controls the family-wise error rate, ensuring the overall probability of making at least one Type I error across all comparisons remains at the desired significance level.
- Generally more appropriate when making multiple comparisons in an ANOVA context, as it has greater power to detect significant differences while controlling for multiple comparisons.

.bold[Pairwise t-tests]:
- Compares two means at a time.
- Performing multiple pairwise t-tests inflates the Type I error rate, as each test uses a fixed significance level (e.g., 0.05) without considering the number of comparisons made.
- While adjustments such as the Bonferroni correction can control for multiple comparisons, using individual t-tests becomes less powerful and more complex as the number of comparisons increases.
]]

---
class: center, middle

### Roadmap for choosing ANOVA and post-hoc tests

<img src="resources/w03-img/pingouin_anova_guide.png" width="80%" align="center">  
.square[The roadmap for choosing ANOVA and post-hoc tests approaches. by [Pingouin](https://pingouin-stats.org/build/html/guidelines.html) ]


---
class: center, middle, inverse

.xx-large.bold.wide[PART 4]
## The Non-parametric Tests
------
.square[Concept .dot[] As Alternatives]

.headnote.square.bold.x-large[Statistical Pattern II]

---
class: left, middle

.split-30[.column[
### Limitations of t-tests and ANOVA
].column[
- Both t-test and ANOVA have assumptions of:
    - numerical responses (ratio or interval target variable)
    - normality (target variable)
    - independence (within and between groups)
    - equal variances
- When these assumptions are violated, the validity of t-tests and ANOVA may be compromised, leading to inaccurate results.
- In this case, the relevant .red.bold[non-parametric tests] could be used. 
]]

---
class: center, middle

### Roadmap for choosing non-parametric tests

<img src="resources/w03-img/pingouin_nonparam_guide.png" width="80%" align="center">  
.square[The roadmap for choosing non-parametric tests approaches. by [Pingouin](https://pingouin-stats.org/build/html/guidelines.html) ]

---
class: left, middle

### The non-parametric alternatives

.split-50[.column[
.bold[T-test]
- Independent samples t-test
    - Mann-Whitney U Test
- Paired samples t-test
    - Wilcoxon Sign-Rank Test

].column[
.bold[ANOVA]
- One-way ANOVA
    - Kruskal-Wallis Test
- Repeated Measures ANOVA 
    - Friedman Test (non-binary data)
    - Cochran Test (binary data)
]]

---
class: center, middle

### An example (socio-economic status in Brunei)

The income levels are ordinal (ranks) data, which is not numerical, and not normally distributed. Two groups are observed in both example, i.e., gender (male: 1, female: 0) and rural (rural: 1, urban: 0). 

.split-50[.column[
<img src="resources/w03-img/nonparam_byGender_brunei.png" width="80%" align="center"> 
].column[
<img src="resources/w03-img/nonparam_byRural_brunei.png" width="80%" align="center"> 
]] 
.footnote.square[Comparing the income level vs. gender (left) and rural/urban (right). ]

.headnote.small[Data source: [A global dataset of 7 billion individuals with socio-economic characteristics](https://doi.org/10.1038/s41597-024-03864-2)]


---
class: center, middle

### An example (socio-economic status in Brunei)

The income levels are ordinal (ranks) data, which is not numerical, and not normally distributed. .red[Multiple] groups are observed in both example, i.e., age group (from low to large) and rural (from low education level to high education level), thus, ANOVA's alternatives could be used. 

.split-50[.column[
<img src="resources/w03-img/nonparam_byAge_brunei.png" width="80%" align="center"> 
].column[
<img src="resources/w03-img/nonparam_byEdu_brunei.png" width="80%" align="center"> 
]] 
.footnote.square[Comparing the income level vs. age groups (left) and education levels (right). ]

.headnote.small[Data source: [A global dataset of 7 billion individuals with socio-economic characteristics](https://doi.org/10.1038/s41597-024-03864-2)]

---
class: center, middle, inverse

## The Closing Remark
------
.square[Hypothesis .dot[] T-test .dot[] ANOVA .dot[] Non-parametric Tests]

.headnote.square.bold.x-large[Statistical Pattern II]

---
class: left, middle

.split-30[.column[
### Summary and key points
].column[
- Hypothesis testing is a key to quantify the differences in data.
- Null hypothesis are usually 'no effects' or 'no differences'.  
- T-test, ANOVA, and non-parametric tests could be used in various conditions. 
- T-test and ANOVA were designed with some assumptions and base distribution (t-distribution and F-distribution), which are prefered if the assumptions are met. 
- If the assumptions are violated, the statistical estimation is compromised and the accuracy is unknown. 
- Non-parametric tests can be used in that situation. 
]]

---
class: left, middle

.split-30[.column[
### How to think statistically?
].column[
Some key points:
- How to measure data quantitatively (or qualitatively)
    - nominal, ordinal, interval, ratio
    - binary, numerical, categorical 
- Are them different? Are them same?
    - designing the hypothesis
    - how to formulate a question
- Are them related? 
    - correlation, regression (not covered)
- How to test/assess the hypothesis?
    - parametric, non-parametric
    - the assumptions behind each method
- How to read the results (interpretation)?
    - significant at what level? 
    - effect size? 
    - how confidence are we?
- Relating to the big picture
    - what this means in your big-aim / Reseearch Questions (RQ)
    - how visualisation can help linking back to your study

]]

---
class: center, middle

### How to use these techniques and thinking in spatial data? 


.square[A slice of HDB data table. ]
.split-10[.column[].column[
| Street            | Flat Type   | Floor Area (sqm) |   Resale Age |   Resale Price |
|:------------------|------------:|-----------------:|-------------:|---------------:|
| ANG MO KIO AVE 10 | 2 ROOM      |               44 |           44 |         267000 |
| ANG MO KIO AVE 3  | 2 ROOM      |               49 |           46 |         300000 |
| ANG MO KIO AVE 3  | 2 ROOM      |               44 |           45 |         280000 |
| ANG MO KIO AVE 3  | 2 ROOM      |               44 |           45 |         282000 |
| ANG MO KIO AVE 4  | 2 ROOM      |               45 |           37 |         289800 |
|               ... |         ... |             ...  |          ... |            ... |
]]

---
class: center, middle

### How to use these techniques and thinking in spatial data? 

<img src="resources/w02-img/frequency_distribution_kdeplot.png" width="80%" align="center">  
.square[The differences between flat type?]

---
class: center, middle

### How to use these techniques and thinking in spatial data? 

<img src="resources/w03-img/HDB_price_points_13.png" width="80%" align="center">  
.square[The differences between regions?]

---
class: center, middle

### How to use these techniques and thinking in spatial data? 

<img src="resources/w03-img/HDB_price_points_13_23.png" width="100%" align="center">  
.square[The differences between the two years?]

---
class:

### Strategies to investigate spatial data differences

- .red[individual level] comparison
    - directly analyzing the data table
    - transactions between flat types, between regions, between time, ...  
    - each data point is considered independent from other data point
    - use statistical methods

- .red[spatially aggregated] comparison
    - aggregate the data by spatial units (subzone, planning area)
    - the average price for 4 rooms for every subzone, ...
    - each spatial unit is considered independent from other spatial unit
    - use statistical methods

- consider .red[spatial relationship] (nearby) effects
    - spatial relationship between data points or spatial units
    - the prices of the same type of house unit within the neighborhood (a search distance)... 
    - data points or spatial units are consider spatially dependent
    - use spatial statistic methods
    