# The Analysis of Variance

## What is Analysis of Variance

**Definition**:
Analysis of Variance, aka ANOVA, is a statistical method used to compare the means of __more than two groups__ to determine whether there is a significant difference between them.

The primary purpose of ANOVA is to test the hypothesis that the means of several populations are equal. It helps determine __whether any observed differences between group means are real or occurred by chance__.

**When to use ANOVA**:
ANOVA is used when comparing more than two group means. It is particularly useful in experimental settings where a single factor (independent variable, one-way ANOVA) is __manipulated at multiple levels__ (e.g., low, medium, high), and the researcher wants to investigate the effect of __this manipulation__ on the outcome (dependent variable).


## Assumptions of ANOVA

ANOVA is based on the following assumptions:
- **Numeric Response**: The __target (dependent) variable__ should be continuous, either ratio or interval.
- **Normality**: The data within each group should be approximately normally distributed.
- **Equal Variances (homoscedasticity)**: The variances of the populations being compared should be roughly equal.
- **Independence**: Observations should be independent of each other. This means that the data from one subject should not influence the data from another subject.
- **Categorical treatment or factor variables**: ANOVA evaluates mean differences between one or more categorical variables (such as treatment groups), which are referred to as factors or “ways.”

Note: It is essential to verify that these assumptions are met before conducting ANOVA. If assumptions are not satisfied, the validity of the F-test may be compromised. In such cases, alternative methods such as __repeated measure ANOVA, Welch's ANOVA, non-parametric tests__ or more robust techniques may be considered.


## Steps of ANOVA
```{figure} ./resources/w03-img/anova_ttest.drawio.png
:label:
:alt:
:align: center

The analysis process for t-test, ANOVA, and post-hoc test.
```


## Types of ANOVA
Here only some commonly used types are introduced. Other types, e.g,. two-ways, three-ways, nested, Welch's ANOVA... are not covered here since those data is less common, and the concept is similar (anyway).

- One-way ANOVA
    - between groups
    - the simplest and straighforward situation

- Repeated Measures ANOVA
    - within group
    - when the groups are not independent

- Mixed-Design ANOVA
    - when both between and within occurs

### One-way ANOVA
**Concept**
One-way ANOVA is a statistical technique used to compare the target variable's means of __three or more independent groups__ with __a single independent variable__ (or factor). It helps determine whether any observed differences between group means are real or occurred by chance.

**Example**
To compare the average test scores of students who received different teaching methods.

**Hypothesis Tested in One-way ANOVA**
- $H_0$: The population means of the groups being compared are equal.
Symbolically: $μ_1 = μ_2 = μ_3 = ... = μ_k$, where μ_i represents the mean of the ith group, and k is the total number of groups.
- $H_1$: At least one of the group means is different from the others.

```{figure} ./resources/w03-img/measures_spread_4vars.png
:label:
:alt:
:align: center

The One-way ANOVA comparing the four target variables between the three species.
```



:::{table} The ANOVA result for the four target variables. Each row display the result from a single ANOVA.  All were significant.
:label: anovatable
:align: center

| variety      |   ddof1 |   ddof2 |        F |   p-unc |   np2 |
|:-------------|--------:|--------:|---------:|--------:|------:|
| petal.length |       2 |     147 | 1180.16  |   0.000 | 0.941 |
| petal.width  |       2 |     147 |  960.007 |   0.000 | 0.929 |
| sepal.length |       2 |     147 |  119.265 |   0.000 | 0.619 |
| sepal.width  |       2 |     147 |   49.16  |   0.000 | 0.401 |

:::

### Repeated Measures ANOVA
**Concept**
Repeated measures ANOVA, also known as __within-subjects__ ANOVA, is a statistical technique used to compare means of __three or more dependent groups__ when the same subjects are __observed under various conditions or at different points in time.__

**Example**
To compare the reaction times of a group of participants before, during, and after receiving a treatment.

**Hypothesis Tested in Repeated Measures ANOVA**
- $H_0$: The population means of the different conditions or time points are equal.
Symbolically: $μ_1 = μ_2 = μ_3 = ... = μ_k$, where μi represents the mean of the ith condition or time point, and k is the total number of conditions or time points.
- $H_1$: At least one of the population means is different from the others.
Symbolically: There exists at least one i and j such that $μ_i ≠ μ_j$.

```{figure} ./resources/w03-img/physiology_data_lineplot-b.png
:label:
:alt:
:align: center

The physiological responses before, during and after two types of VR treatments.
```


```{figure} ./resources/w03-img/physiology_data_lineplot-b-tables.png
:label:
:alt:
:align: center

The tables about the repeated measures and post-hoc results: (left) low decibel, (right) high decibel.
```



### Mixed-Design ANOVA

**Concept**
Mixed-design ANOVA, also known as split-plot ANOVA, is a statistical method used for analyzing data from studies with both between-subjects factors and within-subjects factors. It __combines features of one-way ANOVA and repeated measures ANOVA__, allowing researchers to examine the effects of multiple independent variables on a dependent variable.

**Key Points**
- __Between-subjects factors__ involve comparisons between different groups of participants, similar to one-way ANOVA.
- __Within-subjects factors__ involve comparisons within the same group of participants at different time points or under various conditions, similar to repeated measures ANOVA.
- Mixed-design ANOVA enables researchers to assess the main effects of each factor and the potential interaction effects between factors.

**Assumptions**
The assumptions of mixed-design ANOVA are similar to those of one-way and repeated measures ANOVA, including normality, homogeneity of variances, and independence. Additionally, the assumption of __sphericity__ must be met for the __within-subjects factor__.

**Use case**
By using mixed-design ANOVA, researchers can gain a deeper understanding of the complex relationships between multiple factors and their effects on the dependent variable. It's a powerful tool for analyzing data from various experimental designs, particularly in fields such as psychology, medicine, and education.

```{figure} ./resources/w03-img/mixed-anova.png
:label:
:alt:
:align: center

The mixed ANOVA result between classes, time (pre-test vs. post-test), and the interaction between class and time.
```


```{figure} ./resources/w03-img/mixed-anova_posthoc.png
:label:
:alt:
:align: center

The post-hoc test after mixed ANOVA, to observe the time effects in different condition.
```


## F-test, F-distribution, and F-statistic

The F-test is a statistical test used in ANOVA to compare variances and determine whether there is a significant difference between group means. The F-statistic (or F-ratio) is calculated as __the ratio of the between-group variance to the within-group variance__:

$$
F = (\text{Between-group variance}) / (\text{Within-group variance})
$$

The F-statistic reflects the extent to which __the variation between groups exceeds the variation within groups__.
A higher F-value indicates a greater difference between group means relative to the variability within each group.


Under the null hypothesis that all group means are equal, the F-statistic follows an F-distribution, which is a family of continuous probability distributions characterized by two parameters: __degrees of freedom for the **numerator** ($\text{ddof}_1$) and degrees of freedom for the **denominator** ($\text{ddof}_2$)__.

The F-distribution is used to determine the __critical F-value__ for a given significance level ($\alpha$) and degrees of freedom ($\text{ddof}_1$ and $\text{ddof}_2$). This critical value is compared with the calculated F-statistic __to make a decision__ about the null hypothesis.


### Making decisions in ANOVA using the F-value

- To make decisions in ANOVA, the calculated F-statistic is compared to the critical F-value obtained from the F-distribution.

- If the F-statistic is **larger** than the critical F-value, we **reject** the null hypothesis, concluding that **at least one group mean is significantly** different from the others.

- If the F-statistic is __smaller__ than the critical F-value, we **fail to reject** the null hypothesis, concluding that there is __insufficient evidence to claim a significant__ difference between group means.

- In practice, a p-value is often computed and compared to a predetermined significance level ($\alpha$) to make this decision. __If the p-value is smaller than $\alpha$, the null hypothesis is rejected.__




## Post-hoc Tests

### Purpose of Post-hoc Tests

Post-hoc tests are follow-up analyses conducted **after** a significant overall F-test in ANOVA. Their purpose is to determine **which specific group means** are significantly different from one another. Since ANOVA only tells us that at least two means are different, **post-hoc tests help pinpoint where those differences lie**.

### Common post-hoc tests

**Tukey's HSD Test**:
- Simultaneously compares all possible pairs of means.
- Controls the family-wise error rate, ensuring the overall probability of making at least one Type I error across all comparisons remains at the desired significance level.
- Generally more appropriate when making multiple comparisons in an ANOVA context, as it has greater power to detect significant differences while controlling for multiple comparisons.

**Pairwise t-tests**:
- Compares two means at a time.
- Performing multiple pairwise t-tests inflates the Type I error rate, as each test uses a fixed significance level (e.g., 0.05) without considering the number of comparisons made.
- While adjustments such as the Bonferroni correction can control for multiple comparisons, using individual t-tests becomes less powerful and more complex as the number of comparisons increases.

### Roadmap for choosing ANOVA and post-hoc tests

```{figure} ./resources/w03-img/pingouin_anova_guide.png
:label:
:alt:
:align: center

The roadmap for choosing ANOVA and post-hoc tests approaches. by [Pingouin](https://pingouin-stats.org/build/html/guidelines.html)
```
