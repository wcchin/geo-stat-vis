# The Non-parametric Tests

## Limitations of t-tests and ANOVA

- Both t-test and ANOVA have assumptions of:
    - numerical responses (ratio or interval target variable)
    - normality (target variable)
    - independence (within and between groups)
    - equal variances
- When these assumptions are violated, the validity of t-tests and ANOVA may be compromised, leading to inaccurate results.
- In this case, the relevant __non-parametric tests__ could be used.



## Roadmap for choosing non-parametric tests
```{figure} ../resources/w03-img/pingouin_nonparam_guide.png
:label:
:alt:
:align: center

The roadmap for choosing non-parametric tests approaches. by [Pingouin](https://pingouin-stats.org/build/html/guidelines.html)
```

## The non-parametric alternatives

**T-test**
- Independent samples t-test
    - Mann-Whitney U Test
- Paired samples t-test
    - Wilcoxon Sign-Rank Test

**ANOVA**
- One-way ANOVA
    - Kruskal-Wallis Test
- Repeated Measures ANOVA
    - Friedman Test (non-binary data)
    - Cochran Test (binary data)


## An example (socio-economic status in Brunei)

The income levels are ordinal (ranks) data, which is not numerical, and not normally distributed. Two groups are observed in both example, i.e., gender (male: 1, female: 0) and rural (rural: 1, urban: 0).


:::{figure}
:label: bruneiexample1
:align: center

(byGender)=
![by age](../resources/w03-img/nonparam_byGender_brunei.png)

(byRural)=
![by rural](../resources/w03-img/nonparam_byEdu_brunei.png)

Comparing the income level vs. gender (a) and rural/urban (b). Data source: [A global dataset of 7 billion individuals with socio-economic characteristics](https://doi.org/10.1038/s41597-024-03864-2)
:::


The income levels are ordinal (ranks) data, which is not numerical, and not normally distributed. __Multiple__ groups are observed in both example, i.e., age group (from low to large) and rural (from low education level to high education level), thus, ANOVA's alternatives could be used.

:::{figure}
:label: bruneiexample2left
:align: center

(byAge)=
![by age](../resources/w03-img/nonparam_byAge_brunei.png)

(byEdu)=
![by Education](../resources/w03-img/nonparam_byEdu_brunei.png)

Comparing the income level vs. age groups (a) and education levels (b). Data source: [A global dataset of 7 billion individuals with socio-economic characteristics](https://doi.org/10.1038/s41597-024-03864-2)
:::
