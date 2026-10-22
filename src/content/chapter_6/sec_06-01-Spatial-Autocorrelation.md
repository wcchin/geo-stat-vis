---
label: spatial-autocorrelation
---

# 6.1 Autocorrelation and spatial autocorrelation

**Reading route.** Begin with the observed income map, the four-area calculation and the reassignment maps. These establish the idea needed for neighbourhoods and Moran’s I. Return to the optional reference-model and geography notes when interpreting an empirical result.

## Does where a value occurs tell us something about its neighbours?

Imagine receiving a table of household incomes with the place names removed. You could describe its middle, its spread and the difference between its highest and lowest values. You could not tell whether higher-income places are next to one another or separated by lower-income places. That question requires both **values** and **spatial relationships**.

Spatial autocorrelation concerns the association between values of the **same variable** at locations connected by a specified spatial relationship. For example, do places with above-average incomes tend to have neighbours whose incomes are also above average? The question is about how values are arranged, rather than only how much they vary.

The chapter introduction distinguished event locations from attributes attached to areas. Here we use the Malaysian income maps to develop that second question before defining a neighbourhood matrix.

By the end of this section, you should be able to explain autocorrelation in time and space, distinguish positive from negative spatial association, describe a random-label permutation, and separate visual impressions from statistical evidence. You should also be able to explain why an answer depends on the variable, spatial units, definition of neighbours and reference model.

## A peninsula-wide income example

Our example covers **92 mapped areas across Peninsular Malaysia**. Most observations are administrative districts; Kuala Lumpur, Putrajaya and Perlis each contribute one unit, and the source includes Kecil Lojing. This broader extent lets us compare the arrangement of incomes around different parts of the peninsula. Kuala Lumpur is still one polygon, so its internal neighbourhood variation is not visible.

The variable is **median gross monthly household income in 2022**, in Malaysian ringgit (RM), from the Department of Statistics Malaysia (DOSM). It is neither annual income nor an individual worker's salary. Households are assigned by place of residence: a household living in one district and working in another is counted where it lives. See the [official income catalogue](https://open.dosm.gov.my/data-catalogue/hh_income_district) and [DOSM's household-income dashboard](https://open.dosm.gov.my/dashboard/household-income-expenditure) for definitions and survey context.

```{figure} ../resources/original/peninsula-income-observed.png
:label: peninsula-income-observed
:alt: Median monthly household income across 92 areas of Peninsular Malaysia, with pale cream for lower and darker orange-red for higher values.
:align: center
:width: 70%

Observed area-level median incomes in 2022. The sequential OrRd palette runs from pale cream through orange to dark red: darker means higher income. Fixed breaks at RM 3,000, 5,000, 7,000 and 9,000 are used across all maps; no colour represents statistical significance. Income: DOSM; boundaries: PLANMalaysia. Original map drawn for this book in GDM2000 / Peninsula RSO (EPSG:3375). Outlines are generalized at 100 m for this display.
```

Before reading further, identify two areas that appear similar in colour and close together. Then identify a transition between different colours. What counts as “close”: a shared boundary, a short road journey, or a short straight-line distance?

A choropleth invites these questions but does not answer them statistically. Large polygons occupy more visual space, even though each is still one observation. Classification hides differences between values assigned to the same class. Inspect the table as well as the map.

The table lists selected observations for orientation; the notebook provides all 92 values.

| Selected area | Median monthly household income, 2022 (RM) |
|---|---:|
| Kota Bharu | 4,330 |
| Kuala Terengganu | 5,872 |
| Timur Laut | 6,714 |
| Johor Bahru | 8,232 |
| Sabak Bernam | 5,533 |
| Kuala Lumpur | 10,234 |
| Sepang | 12,608 |

Each income estimate is calculated **within an individual area**. Taking a simple average or median of all 92 area-level estimates would summarise those estimates; it would not recover the median income of all households in the combined region. The notebook explicitly reconciles spelling differences such as Ulu/Hulu, Timur/Timor Laut and Larut dan Matang/Larut & Matang, as well as federal-territory prefixes. Every income observation must match a single map unit.

There is no rule that the centre must have the highest household income. Sepang's median exceeds Kuala Lumpur's here. Central land values, the concentration of workplaces and resident households' incomes are different measurements. Interpret the observed values rather than imposing an expected centre–periphery pattern.

## From correlation to autocorrelation

Ordinary correlation can compare two different variables measured on the same observations, such as income and expenditure. **Autocorrelation** instead relates a variable to another occurrence of itself, with those occurrences linked by time, space or another structure.

For **temporal autocorrelation**, order supplies the relationship. We might compare each month's rainfall with the preceding month's rainfall. A one-month lag is different from a twelve-month lag; changing the lag changes the question. Seasonality can produce association without one month's rainfall directly causing the next month's rainfall.

For **spatial autocorrelation**, there is usually no single natural ordering. A district can have several neighbours in different directions. Shared boundaries, distance bands and nearest-neighbour rules specify different relationships. Rearranging spreadsheet rows should not change geographical neighbours. The [next section](sec_06-02-Statistical-Spatial-Testing.md) explains these choices.

The idea also extends to transport or social networks, where connected nodes supply the relationships. In every case, autocorrelation is defined relative to a structure, rather than only by a list of values.

## Positive and negative spatial association

**Positive spatial autocorrelation** means that similar values tend to occur at neighbouring locations relative to the chosen reference. Similarity includes relatively high values next to high values and relatively low values next to low values. A cluster of low incomes can therefore contribute positively to spatial autocorrelation.

**Negative spatial autocorrelation** means that neighbouring values tend to be dissimilar: relatively high values occur beside relatively low values. An alternating grid makes this visible when neighbours share an edge. If diagonal cells also count as neighbours, the same arrangement includes additional similar-value pairs.

```{figure} ../resources/original/autocorrelation-patterns.svg
:label: autocorrelation-patterns
:alt: Three synthetic grids containing identical counts of low and high values, arranged in blocks, a random reshuffle and a checkerboard.
:align: center

Synthetic teaching patterns, separate from the income data. Each panel contains 18 low and 18 high values. Under shared-edge neighbourhoods, blocks emphasise similar neighbours and the checkerboard emphasises dissimilar neighbours. The middle panel is one random assignment: chance groupings can occur, and its coefficient is not guaranteed to be zero.
```

Positive and negative describe association, not whether an outcome is good or bad. They do not refer to the sign of income or the colour on the map. “High” and “low” also need a reference: they might mean above and below the study-area mean, rather than categories defined by a government income threshold.

## A worked example: the same values, different neighbours

Four **synthetic** areas form a chain, A–B–C–D. Only consecutive areas are neighbours. Compare two assignments of the same values:

| Assignment | A | B | C | D |
|---|---:|---:|---:|---:|
| Grouped | 2 | 2 | 8 | 8 |
| Alternating | 2 | 8 | 2 | 8 |

Both have mean 5 and the same distribution. Define each mean-centred deviation as $d_i=x_i-\bar{x}$. The deviations are either $-3$ or $+3$.

For a neighbouring pair, $d_i d_j$ is positive when deviations have the same sign and negative when their signs differ. Two below-average values give $(-3)(-3)=+9$.

| Assignment | A–B | B–C | C–D | Sum over the three edges |
|---|---:|---:|---:|---:|
| Grouped | $+9$ | $-9$ | $+9$ | $+9$ |
| Alternating | $-9$ | $-9$ | $-9$ | $-27$ |

The distribution alone cannot distinguish the assignments; neighbour cross-products can. The grouped arrangement includes two similar-value edges and one contrasting edge. Every edge in the alternating arrangement connects dissimilar values.

This sum is a **teaching quantity, not a normalised autocorrelation coefficient**. It changes with measurement units, the number of edges and the definition of neighbours. Each undirected edge is counted once here. Matrix expressions may count both directions; numerator and denominator conventions must remain consistent.

## Neighbour relationships need a definition

The chain calculation used shared links, but the income map does not have just one obvious ordering. A district can have several neighbours, and alternative rules connect different sets of places. These choices determine which value pairs enter a statistic.

Tobler's first law of geography motivates attention to nearby relationships, but does not guarantee positive autocorrelation for every variable, scale or neighbourhood. Distance decay is a modelling choice to examine, not a substitute for checking the relationships. [Section 6.2](sec_06-02-Statistical-Spatial-Testing.md) translates those choices into a weights matrix and a spatial lag, then links them to Moran's I.

## What should a random comparison hold fixed?

Our initial reference for these areal data is **random assignment of observed values to fixed spatial units**. Conditional on the observed set of values, every assignment is equally likely under this reference. This is a random-label or permutation model.

Boundaries do not move, areas are not resized and no new income values are invented. We shuffle the 92 observed area medians, preserving their sorted values, mean, variance and histogram. Their association with particular areas changes.

```{figure} ../resources/original/peninsula-income-permutation.png
:label: peninsula-income-permutation
:alt: Observed income values beside a random reassignment of the same 92 estimates to the same polygons.
:align: center

Observed assignment (left) and one permutation (right), with identical values, boundaries, extent and classification. The right panel is simulated, not another survey or an income prediction. It preserves the distribution of the 92 area medians, not the underlying household-level distribution. Sources: DOSM and PLANMalaysia.
```

This differs from **complete spatial randomness for point events** in Chapter 4. There, we simulate event locations within a study window. Here, locations remain fixed and attributes move between them. The reference models answer different questions.

Random does not mean that no recognisable grouping can appear. A reshuffle can contain similar colours next to one another or an isolated contrasting area by chance. One striking feature is insufficient evidence against a random reference.

```{figure} ../resources/original/peninsula-income-three-permutations.png
:label: peninsula-income-three-permutations
:alt: Three further random assignments of the same income values, retaining identical boundaries and a shared legend.
:align: center

Three further permutations generated with a recorded seed. Some assignments can look more structured than others. These illustrate variability under reassignment; three pictures do not supply a sufficient statistical reference distribution. Sources: DOSM and PLANMalaysia.
```

## From maps to a statistical comparison

To ask whether an arrangement is unusual, define neighbours, choose a statistic and specify the departure of interest before interpreting the result. Calculate that statistic for the observed assignment and many random permutations, holding the weights fixed. The resulting reference distribution describes variation under the reassignment model.

For a statistic that increases with similar neighbour values, an unusually large observed value can provide evidence of positive association. The direction and calibration depend on the statistic: later sections explain why the same tail rule cannot simply be transferred to every measure. One visually striking permutation is not a substitute for this distribution.

A permutation p-value describes unusualness under the specified procedure. It is not the probability that the null is true, that the conclusion is wrong, or a measure of the importance of income differences. Failure to reject does not establish randomness in every aspect of the map. Section 6.3 develops the formal calculation and Monte Carlo reporting convention.

**Neither this section nor its notebook reports a spatial autocorrelation coefficient or p-value for the Malaysian data.** They establish the observations and permutation logic. First continue to [Defining Distance and Neighbourhoods](sec_06-02-Statistical-Spatial-Testing.md), then use [Moran's I](sec_06-03-Morans-I.md) to formalise the comparison.

::::{dropdown} Go deeper: exchangeability and survey estimates

## When is permutation a defensible reference?

Random reassignment treats areas as **exchangeable under the null**: values can be interchanged without violating that model. Independent observations are not automatically exchangeable if their distributions vary by location. Distinct urban and rural income-generating conditions, for example, could make unrestricted reassignment an unrealistic reference.

Observed association can reflect neighbour interaction, shared geographical influences, broad trends or several processes together. A common trend can make nearby values similar without direct influence between neighbouring households. Rejecting unrestricted reassignment therefore does not identify a cause or uniquely distinguish dependence from spatial heterogeneity. A research question may require modelling a trend, conditioning on relevant covariates or designing a more restricted randomisation.

Permuting district medians treats the estimates as the available observations. It does not propagate their survey uncertainty, recreate households or account for different household counts between areas. DOSM's survey methodology and uncertainty information matter for substantive comparisons.

::::

## Global patterns and local differences

A **global** statistic summarises association across the whole study area. A **local** statistic examines the relationship around individual locations. A modest global result can coexist with a strong local contrast; a strong global result need not describe every location.

| Configuration | Value at the location | Neighbour summary | Association tendency |
|---|---|---|---|
| High–high | Relatively high | Relatively high | Similarity |
| Low–low | Relatively low | Relatively low | Similarity |
| High–low | Relatively high | Relatively low | Contrast |
| Low–high | Relatively low | Relatively high | Contrast |

These configurations are descriptive until an appropriate local test has been performed. A dark high-income polygon is not automatically a significant hotspot, nor a pale low-income polygon a significant coldspot. [Local Moran's I](sec_06-04-Local-Moran.md) distinguishes local similarity from spatial outliers; testing many locations also raises a multiple-comparison question.

::::{dropdown} Go deeper: aggregation, boundaries, dates and map classes

## Read the geography before drawing a conclusion

**Aggregation changes what can be observed.** District-level observations cannot reveal neighbourhood-level inequalities, and patterns can change with the zoning scheme or spatial scale: part of the modifiable areal unit problem. An area's median does not describe every household. Inferring household relationships from an area-level relationship risks an ecological fallacy.

**Study boundaries limit neighbourhoods.** Edge areas can have important connections outside the selected region. A district can become isolated under a restrictive distance rule despite having real geographical connections. Island units such as Langkawi also require an explicit decision about whether and how to connect them to mainland neighbours. A suitable projected CRS supports metric distances, but does not decide which neighbours are meaningful.

**Maps and estimates have dates.** Income refers to 2022; the PLANMalaysia boundary snapshot was retrieved on 20 October 2026. It is not a reconstruction of 2022 administrative geography. The notebook matches names explicitly, and substantive historical analysis should verify boundary changes and area definitions. The small display snapshot uses the service's 100 m outline generalization. It must not be used to infer exact shared-border adjacency; obtain full-detail geometries and verify topology for that task.

**Representation affects perception.** The published maps use a sequential OrRd palette and fixed income breaks. Class widths are not all equal, and the upper class begins at RM 9,000. The notebook can instead calculate quantile breaks, which put similar numbers of observations into classes. Keep classification fixed across permutations so visible changes come from reassignment, and inspect numerical values before interpreting colours.

::::

## Reproduce, change and explain

Open the [self-study notebook](../notebooks/lab-08-autocorrelation-self-study.ipynb). In the book repository it loads an attributed source snapshot; used alone, it can download the official sources directly. Both routes report fingerprints. It reproduces the three maps with optional Matplotlib `xkcd` styling and Comic Neue lettering, using the same projected display layer in every panel. The portrait observed figure, two-column comparison and three-column permutation figure retain equal x/y scale and a shared legend; the peninsula is not stretched to fill a square.

Compare median with mean income, change the random seed and try different fixed breaks or set `CLASS_BREAKS=None` to explore quantile classes. Change one setting at a time and explain what stays fixed. A different year is accepted only when every area has an observation; the notebook stops rather than mixing years or silently dropping KL.

The [source record](../datasets/peninsula_income_2022/README.md) documents retrieval, projection and matching. The formal [shared income analysis](../datasets/malaysia_income_areal/README.md) now uses full-detail geometry for its audit and representative points, with separate proximity weights; the display notebook remains a map/permutation introduction. Continue to [Defining Distance and Neighbourhoods](sec_06-02-Statistical-Spatial-Testing.md) before calculating an autocorrelation statistic.

## Check your understanding

**Self-check:** Can identical histograms accompany different spatial autocorrelation?

```{dropdown} Feedback
Yes. Histograms record values and frequencies, not their assignment to locations. The chain example and map permutations illustrate this. Autocorrelation also requires specified neighbourhoods.
```

**Self-check:** Does a pair of low-income neighbours necessarily contribute negatively?

```{dropdown} Feedback
No. If both are below the chosen mean, both deviations are negative and their product is positive. Low–low similarity contributes towards positive association. A contribution is not a test of local significance.
```

**Self-check:** Must a random permutation look patternless?

```{dropdown} Feedback
No. Chance can produce groupings. Inference compares a defined statistic with a reference distribution instead of declaring randomness from appearance.
```

**Self-check:** Does this map establish whether income clusters within Kuala Lumpur?

```{dropdown} Feedback
No. KL is one observation. Its internal neighbourhood variation is not represented. Finer matched data and boundaries are needed for that question.
```

**Self-check:** Would a small permutation p-value prove neighbouring districts influence each other's incomes?

```{dropdown} Feedback
No. It provides evidence against a chosen randomisation reference. Shared influences and spatial trends can also produce association. Causal claims require an additional research design and evidence.
```

**Self-check:** What stays fixed when the notebook's seed changes?

```{dropdown} Feedback
The selected variable and year, boundaries, sorted values, colour classes and extent. Assignments change. In a formal test, the weights and statistic also stay fixed across permutations.
```

## Further reading

- **Foundational paper:** Tobler, W. R. (1970). [A Computer Movie Simulating Urban Growth in the Detroit Region](https://doi.org/10.2307/143141). *Economic Geography*, 46 (Supplement), 234–240. Read as geographical motivation for considering nearby relationships, not as evidence that every variable must have positive association.

- [GeoDa Workbook: Global Spatial Autocorrelation](https://geodacenter.github.io/workbook/5a_global_auto/lab5a.html): spatial lags, Moran scatter plots and randomisation inference.
- [DOSM income by administrative district](https://open.dosm.gov.my/data-catalogue/hh_income_district): definitions, survey coverage, nominal values and attribution.
- [PLANMalaysia boundary service](https://gisdev.planmalaysia.gov.my/server/rest/services/Hosted/Data_Sempadan_Daerah/FeatureServer/0): boundaries used in the regional illustration.

**Next:** [Defining Distance and Neighbourhoods](sec_06-02-Statistical-Spatial-Testing.md). Make the neighbour relationship explicit before calculating a statistic.
