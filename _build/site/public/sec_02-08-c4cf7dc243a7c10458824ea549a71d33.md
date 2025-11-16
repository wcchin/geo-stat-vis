# The Non-parametric Tests
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
