# Gordon Square: Does the Pattern Change When We Count People or Groups?

Imagine visiting a London garden on a sunny afternoon. Some people sit alone; others sit with friends. Looking across the lawn, you might say that people are gathered in clusters. But what would happen if we treated each *social group*, rather than each *person*, as one event?

This case study follows a geographical decision with statistical consequences: **what does one point represent?** It uses an observed point pattern and previously prepared teaching figures to compare nearest-neighbour and multiple-distance perspectives. The aim is to evaluate the reasoning, not to claim a newly executed analysis.

**Read alongside:** [Complete spatial randomness](../chapter_4/sec_04-01-Complete-Spatial-Randomness.md), [nearest-neighbour analysis](../chapter_4/sec_04-03-Nearest-Neighbor-Analysis.md), and [Ripley's K-function](../chapter_4/sec_04-04-Ripleys-K-Function.md).

## 1. The geographical question

There are competing expectations about where people sit. Friends may choose adjacent spots, while separate groups might leave comfortable gaps between themselves. Both behaviours could appear in the same garden at the same time.

We therefore ask two related but distinct questions:

1. **Individuals:** Are people closer to one another than we would expect from an independent, uniform placement in the accessible garden?
2. **Groups:** Are the positions of distinct sitting groups more spread out than the same reference would predict?

Neither question alone establishes *why* people chose their seats. Other factors—shade, paths, occupied benches, personal preferences and earlier arrivals—may influence the locations.

```{figure} ../resources/w05-img/gordon_square2.png
:alt: Context illustration showing Gordon Square in London.
:align: center

Gordon Square, London. The original course illustration links to [Google Maps](https://maps.app.goo.gl/Qdb1K4hzyG485Btm8). This is context, not the measured point-pattern geometry.
```

## 2. What was observed—and what is represented?

The published **`gordon`** dataset in R's [`spatstat.data`](https://search.r-project.org/CRAN/refmans/spatstat.data/html/gordon.html) records locations of people sitting on a grass patch in Gordon Square at 3 pm on a sunny afternoon. Its coordinates are in **metres**, and the observation window is an **irregular polygon with two holes**. The dataset is attributed to Andrew Bevan, University College London; it is discussed in [Baddeley et al. (2013)](https://doi.org/10.18637/jss.v055.i11).

The `spatstat` teaching notes describe **99 individual points**. The original page's approximate 42 × 56 m rectangle should not be substituted for the actual polygon or treated as its area. The enclosing dimensions and the *usable observation area* are different quantities.

```{figure} ../resources/w05-img/GordonSquare_individual_and_groups_xkcd.png
:alt: Existing teaching illustration contrasting individual positions with sitting-group positions.
:align: center

The existing teaching illustration contrasts two observation units. The original grouping procedure and its derived coordinates have not yet been independently verified from the material in this repository; do not treat the group layer as an official field in `spatstat.data::gordon`.
```

A point for each **individual** asks about interpersonal proximity. One representative point for each **group** asks about spacing between social units. To reproduce the second analysis we would need a documented rule defining membership and group location (for example, a representative centre); it cannot be reconstructed uniquely from the individual coordinates alone.

### Check your reasoning

**Self-check:** If three friends sit together, how many events would each representation record?

```{dropdown} Feedback
The individual representation would record three events. The group representation would record one event *if* those three people were classified as a single group. The latter needs an explicit grouping rule; a group cannot be inferred reliably from distance alone.
```

## 3. Selecting analytical methods

A visual impression of a cluster is not a statistical test. We need to choose what kind of departure matters, define where sitting was possible, and compare the observed pattern with a relevant reference.

**Nearest-neighbour analysis (NNA)** summarises the distance from each event to its closest *other* event. Shorter-than-reference distances suggest local aggregation; longer distances suggest more regular spacing. It is one summary, not a complete description of the pattern.

**Ripley's K-function** considers the cumulative number of neighbours within a sequence of radii. It can reveal how the pattern's appearance changes with spatial scale. Its interpretation depends on an appropriate observation window, an edge correction and a clearly identified simulation or theoretical reference.

For both methods, homogeneous complete spatial randomness (CSR) is a **starting model**, not a realistic theory of how people must behave. In this setting, a finite-window simulation with a fixed event count and uniformly sampled locations would provide one conditional reference. The irregular accessible window—including the holes—matters.

## 4. What do the existing figures suggest?

### Nearest neighbours

```{figure} ../resources/w05-img/nna_compare_hist_gordon.png
:alt: Previously prepared nearest-neighbour comparison plots for the individual and group representations.
:align: center

Previously prepared course results comparing individual and group representations. The figure is retained as a teaching result; the precise input coordinates, grouping protocol, reference simulation and numerical significance calculations have not yet been independently reproduced here.
```

The original teaching interpretation reports *shorter* nearest-neighbour distances for individuals and *longer* distances for groups relative to their respective reference comparisons. That contrast is plausible: members of a party may sit together while separate parties leave more space between them.

But the interpretation should remain **conditional on the original analysis** until its data and test settings are reconstructed. A negative or positive z-score describes direction only in relation to the stated formula; a significance claim also requires a verified reference distribution, tail and p-value.

The key insight does not depend on declaring both tests significant: **changing the observation unit changes the question and can change the pattern we detect**.

### More than one distance

```{figure} ../resources/w05-img/k_function_ci_gordon.png
:alt: Previously prepared K-function comparison curves for individuals and groups across spatial distances.
:align: center

Previously prepared multi-distance comparison. Check whether the displayed function is K, L or centred L, the estimator and edge correction, and whether the bands are pointwise or globally calibrated before making inferential claims.
```

The existing course notes describe excess nearby individual pairs at short radii and relative separation among groups over short to intermediate distances. At larger distances the plotted group curve appears closer to its reference. This **does not prove randomness** beyond any particular radius.

Also, a curve crossing a *pointwise* simulation band at a selected radius is not automatically a globally calibrated test across the full interval. We should not report a whole-curve p-value unless that test has been performed.

### Compare the two summaries

| Question | NNA contributes | K-function contributes |
| --- | --- | --- |
| Are individual positions close together? | Closest other person's distance | Accumulated nearby pairs across chosen radii |
| Are social groups spaced apart? | Closest other group's distance | How spacing varies with radius |
| Does either statistic reveal why? | No | No |

## 5. Choices that could change the conclusion

**Observation unit.** A member of a group has nearby companions; the centre of that group might have no nearby *other group*. These are valid but different questions. A reproducible group analysis needs explicit membership and location rules.

**Window and inaccessible spaces.** Use the actual polygonal lawn and its holes, not the enclosing rectangle. An inflated reference area makes the same observed nearest-neighbour distances appear more clustered; mismatched simulation windows undermine inference.

**Edges and distance range.** Near-boundary neighbours beyond the lawn cannot be observed. A K-function analysis should report the correction used and a justified maximum radius relative to the window.

**Unequal opportunity.** Shade, paths and comfortable patches may make some locations more likely even without attraction or avoidance between people. Rejecting homogeneous CSR does not isolate a social mechanism.

**Uncertainty.** This is a single observed afternoon, not evidence of universal behaviour in London parks. Group definitions and any claimed p-values need an auditable calculation.

## 6. Synthesis: What have we learned?

The strongest lesson is not that people are simply clustered or dispersed. **People can appear clustered when we count individuals, while groups can appear more regularly spaced when each party is represented as one event.** The two statements answer different geographical questions.

An analytical account should therefore name the event, observation window, reference model, method and distance scale before assigning a label to the pattern. It should also make clear which results were reproduced and which came from earlier teaching materials.

**Final reflection:** If someone concludes that “people prefer to sit close together” from the individual pattern, how would you challenge that interpretation? Which alternative explanations would you investigate, and what extra observations would help distinguish them?

```{dropdown} Feedback
Ask whether the close neighbours are companions, whether people select shaded or accessible locations, and whether the usable lawn was modelled correctly. Group-membership observations, repeated time points and environmental covariates would help distinguish these explanations, though observational data alone would still not demonstrate causation.
```

## Continue exploring

The [NNA self-study notebook](../notebooks/lab-05-nna-self-study.ipynb) provides reproducible *synthetic* comparisons and an option to supply projected point coordinates. It does **not** reproduce the Gordon Square group analysis. For the method itself, revisit [NNA](../chapter_4/sec_04-03-Nearest-Neighbor-Analysis.md) and [Ripley's K-function](../chapter_4/sec_04-04-Ripleys-K-Function.md). The [point-pattern lab](../notebooks/lab-05-point-pattern.ipynb) offers further practical exercises.

**Source and further reading:** [`spatstat.data::gordon` documentation](https://search.r-project.org/CRAN/refmans/spatstat.data/html/gordon.html); [Baddeley, Turner, Mateu and Bevan (2013)](https://doi.org/10.18637/jss.v055.i11). The official dataset provides individual coordinates and its observation window; the group-level figures in this case study remain legacy teaching material pending a separate reproduction audit.
