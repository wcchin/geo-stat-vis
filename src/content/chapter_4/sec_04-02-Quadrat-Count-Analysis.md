---
label: quadrat-count-analysis
---

# Quadrat Count Analysis

## Three ways to ask about a point pattern

A map of events invites several different questions. Are events concentrated in some parts of the observation window? Is each event unusually close to its nearest other event? Does the pattern change when we examine larger distances? These questions motivate quadrat analysis, [Nearest Neighbour Analysis](sec_04-03-Nearest-Neighbor-Analysis.md) and [Ripley's K-function](sec_04-04-Ripleys-K-Function.md), respectively.

| Method | What is summarised? | What must we choose? |
| --- | --- | --- |
| Quadrat analysis | Counts inside a partition of the window | Quadrat size, shape and placement |
| NNA | One nearest-other-point distance per event | Observation window, metric and null model |
| K-function | Pairs within each of several radii | Window, radii, edge correction and null model |

The methods can disagree without any calculation being wrong. Each compresses the pattern in a different way. Different regional examples are useful, provided we keep the observation unit and reference model explicit.

**Quadrat analysis** partitions a study window into non-overlapping cells and compares the observed counts with counts expected under a stated model. In this section, we ask whether variation among counts is unusually large under homogeneous complete spatial randomness (CSR). After reading, you should be able to construct the counts, calculate expected values, interpret a Pearson statistic and distinguish uneven intensity from evidence of interaction among events.

## A regional question: where was fire activity detected?

Satellite-detected fire activity in Sumatra provides a regional application that can later connect to the book's areal autocorrelation example. Our question is: **during September 2026, were qualifying FIRMS fire detections distributed uniformly across a fixed land observation window in Sumatra, or concentrated in particular quadrats?** The [NASA FIRMS archive](https://firms.modaps.eosdis.nasa.gov/download/) provides historical active-fire records. The example uses one product, VIIRS S-NPP, throughout the selected month, rather than mixing satellite products with different observation opportunities.

```{note} Observed data and synthetic teaching examples
The South Sumatra maps below use observed September 2026 VIIRS S-NPP detections obtained through a public FIRMS mirror, filtered to nominal/high confidence. The source is near-real-time version 2.0NRT; September records were not independently downloaded from the authenticated NASA archive. The [data record](../datasets/firms_sumatra/README.md) documents provenance, filters and approximate coastal areas. The smaller constructed patterns remain explicitly synthetic and explain the method separately.
```

The observation unit is a **satellite fire detection**, not a distinct ignition or fire event. One persistent fire can generate detections on multiple overpasses. Remove duplicate delivery of the same source record, but do not silently merge repeated observations of an ongoing fire: that would define a different variable and require an explicit event-grouping rule. The example therefore concerns the pattern of recorded detection locations. A detection also does not establish forest land cover; calling the records “forest fires” would require additional evidence.

Fix the time interval, product and confidence filter before analysis. For a confirmatory study, define a land observation window independently of the realised detections, retain land cells with zero detections, and account for clipped cell areas. Ocean is outside this land-based question, not zero-fire land. Detection gaps, cloud cover and changing observation conditions must be investigated before interpreting spatial differences. A fine grid cannot overcome the measurement and sampling limitations of the source.

## Count every cell, including empty cells

Let the fixed window be divided into $m$ cells and let $O_i$ be the number of points in cell $i$. If every point falls inside the window and is allocated once,

$$
\sum_{i=1}^{m}O_i=n.
$$

Cells form a partition: they do not overlap and together cover the window. An event exactly on a shared boundary needs a consistent allocation rule. The synthetic example uses intervals closed on the left and open on the right, except that the final outer boundary is included. The FIRMS windows use half-open bounds throughout; no retained record lies on an excluded outer edge. Thus a boundary event is counted once, not twice.

```{figure} ../resources/original/quadrat-three-patterns.svg
:label: quadrat-three-synthetic-patterns
:alt: Three synthetic point patterns in equal 2000 metre square windows, each divided into sixteen cells with counts shown.
:align: center

Original synthetic examples: each has 96 points, the same 2 km square window and sixteen 500 m cells. Empty cells remain part of the calculation. The counts, rather than the appearance of the dots alone, enter the quadrat statistic.
```

## What does CSR predict?

Under a homogeneous Poisson process, intensity is constant and disjoint-region counts are independent Poisson variables. Conditional on the observed total $n$, locations are independent and uniform over the window. The resulting vector of cell counts is multinomial, not a vector of independent counts with freely varying total.

Let $A_i$ be the area of cell $i$ inside the observation window and $A$ the total window area. Under the conditional homogeneous reference,

$$
p_i=\frac{A_i}{A},\qquad E_i=np_i,
\qquad (O_1,\ldots,O_m)\sim\operatorname{Multinomial}(n;p_1,\ldots,p_m).
$$

With equal-area cells, $E_i=n/m$. In the figure, every cell has expected count $96/16=6$. A CSR realisation is not expected to put exactly six events in every cell. Random allocation produces variation around that expectation.

With clipped or unequal cells, use their actual usable areas. A cell with half the area should have half the expected count under uniform intensity. Remove zero-area cells from the partition; do not assign them a positive expectation or divide by zero. If event opportunities differ for reasons beyond area, a homogeneous reference may be unsuitable.

## From counts to a test statistic

The Pearson quadrat statistic is

$$
T=\sum_{i=1}^{m}\frac{(O_i-E_i)^2}{E_i}.
$$

Both unexpectedly high and unexpectedly low counts increase $T$: deviations are squared. The division by $E_i$ accounts for the expected scale of count variation. This compares cell counts with expected counts; it is not a comparison between the overall mean count and zero, nor a test of a histogram of count frequencies.

### A calculation you can check by hand

Consider four equal-area quadrats containing 40 synthetic events:

| Cell | $O_i$ | $E_i$ | $(O_i-E_i)^2/E_i$ |
| --- | --- | --- | --- |
| A | 4 | 10 | 3.6 |
| B | 8 | 10 | 0.4 |
| C | 12 | 10 | 0.4 |
| D | 16 | 10 | 3.6 |
| Total | 40 | 40 | 8.0 |

Every term is nonnegative and $T=8$. A large statistic describes strong count differences relative to this expectation, but we still need a reference distribution to judge whether it is unusual.

The statistic does **not** use adjacency. Rearranging the same four counts among equal-area cells leaves $T$ unchanged. A contiguous high-count region and an alternating arrangement can have identical quadrat statistics. This will matter later when [Moran's I](../chapter_6/sec_06-03-Morans-I.md) explicitly introduces relationships between neighbouring areas.

## How unusual is the variation?

### Analytical approximation

For the basic homogeneous model with total intensity estimated from the point count, the usual approximation is

$$
T\ \dot\sim\ \chi^2_{m-1}.
$$

The degrees of freedom are $m-1$, not $(r-1)(c-1)$ for an $r$ by $c$ grid. We are testing goodness of fit across cells, not independence in a row-by-column contingency table. Additional fitted parameters require a corresponding adjustment.

For the four-cell example, the upper-tail probability is $P(\chi^2_3\geq8)\approx0.046$. This supplies evidence against the specified homogeneous reference at a prespecified 5% threshold, conditional on the approximation being appropriate. It does not reveal why the counts differ. Small expected counts can make the approximation unreliable; “at least about five per cell” is a useful diagnostic, not a universal guarantee.

### Conditional Monte Carlo comparison

Instead of using the analytical approximation, repeatedly simulate $n$ independent uniform locations inside the same window, count them using the same partition, and recompute $T$. For a quadrat statistic alone, drawing multinomial counts with probabilities $p_i$ gives the same count-level null distribution and is more efficient. The [spatstat quadrat-test documentation](https://search.r-project.org/CRAN/refmans/spatstat.explore/html/quadrat.test.html) describes both conditional and unconditional simulation options.

With $B$ simulations and $b$ simulated statistics at least as large as the observed statistic, an upper-tail Monte Carlo p-value is

$$
p_{\mathrm{upper}}=\frac{b+1}{B+1}.
$$

Include ties. With 999 simulations, the smallest value is 0.001. Record the seed, simulation count and alternative. More simulations improve numerical resolution; they do not guarantee stronger evidence.

```{figure} ../resources/original/quadrat-csr-reference.svg
:label: quadrat-conditional-csr-reference
:alt: Histogram of quadrat statistics from 999 fixed-count CSR simulations, with the constructed clustered pattern's statistic marked.
:align: center

The clustered synthetic example is compared with 999 simulations in the same window and grid, each containing 96 points. Simulated locations change; the window, point count and partition stay fixed. This is a teaching construction, not evidence from FIRMS observations.
```

For these reproducible teaching constructions, the calculation gives:

| Synthetic pattern | $T$ | Upper-tail Monte Carlo p-value |
| --- | --- | --- |
| CSR realisation | 13.67 | 0.538 |
| Clustered construction | 265.00 | 0.001 |
| Spaced construction | 0.00 | 1.000 |

The first row is one random realisation, not a claim that all CSR samples give similar p-values. The second is unusual under this null. The last requires care:

The upper-tail test is sensitive to unusually **large** count variation. Very even counts require a separately specified lower-tail procedure to test unusually low variation. A large upper-tail p-value does not establish regular spacing or prove CSR. Our spaced construction puts six points in every cell and therefore has $T=0$; its regularity is not established by failing to reject an upper-tail test.

## Quadrat size and origin change what we see

```{figure} ../resources/original/quadrat-grid-sensitivity.svg
:label: quadrat-grid-sensitivity
:alt: The same synthetic clustered pattern aggregated to coarse, fine and shifted grids, with cell counts shown and area-adjusted expected counts.
:align: center

The same points can give very different summaries under a coarse grid, a finer grid or a shifted grid. The shifted grid is clipped to the fixed window; its smaller edge cells receive area-adjusted expectations. Colour indicates count, not significance.
```

A coarse grid can hide structure inside cells. A fine grid can produce many empty cells and unstable analytical approximations. Moving the grid can split a concentration across several cells. Compare a small number of defensible specifications and report their consequences; do not select the grid that produces the smallest p-value. Statistics from different partitions also have different null distributions, so their raw magnitudes are not directly comparable measures of clustering strength.

Changing the observation window is different from changing the grid. The window defines where events could have been observed; the grid partitions that opportunity. Keep the window fixed when investigating grid sensitivity.

## Worked regional example: two adjoining South Sumatra windows

We now apply the method to observed detections. Both squares cover 100 km by 100 km in **WGS84 / UTM zone 48S (EPSG:32748)**. B lies immediately east of A, with the same northing bounds. We use 1–30 September 2026 UTC, one satellite product, nominal/high confidence, and 20 km quadrats throughout. Distinct observations of ongoing burning remain in the data. These windows were selected after exploratory inspection, so this is an illustrative comparison rather than a prespecified regional hypothesis test.

```{figure} ../resources/original/firms-two-windows.svg
:label: firms-quadrat-two-windows
:alt: Observed September S-NPP fire detection locations in adjoining western and eastern South Sumatra squares, followed by their twenty-five quadrat counts using one sequential colour scale.
:align: center

A (west) and B (east), each 100 km square. The maps share dates, filtering, grid size and a sequential OrRd count scale. The thin coastline crosses the northern edge of B. Points are satellite detections, not separate fire incidents; colours show counts, not significance.
```

### Step 1: work through the western square

A contains **2,149 detections** and 25 full land quadrats, giving $E_i=2149/25=85.96$. Its counts range from 1 to 481. For the quadrat containing 481 detections, the contribution is $(481-85.96)^2/85.96\approx1815.46$. Adding all 25 contributions gives $T\approx4733.00$.

The contrast between the low-count cells and the concentration in the northeastern part is much larger than uniform allocation predicts. This is evidence against a constant detection intensity across this square; it does not establish a mechanism for that variation.

### Step 2: repeat the procedure in the eastern square

B contains **4,052 detections**, including 1,207 in one quadrat near its western side. Ask first: would a higher total alone produce higher expected counts? Yes. Its expected values must be calculated from its own total, rather than retaining A's expectation of 85.96.

B is approximately 99.56% land according to the generalized Natural Earth boundary. We exclude the ocean portion and use $E_i=nA_i/A$. Most cells have expected count 162.80, while the two coast-clipped cells have approximately 145.10 and 162.48. Thus the simple value $4052/25=162.08$ is not the appropriate expectation for every land cell. These coastal areas are approximate; finer boundary geometry would be needed for precise coastal inference.

| Window | Detections | Land quadrats | Expected count range | Pearson $T$ | Upper-tail Monte Carlo p-value |
| --- | ---: | ---: | ---: | ---: | ---: |
| A: west | 2,149 | 25 | 85.96 | 4,733.00 | 0.0001 |
| B: east | 4,052 | 25 | 145.10–162.80 | 9,247.98 | 0.0001 |
| A+B: combined | 6,201 | 50 | 110.78–124.30 | 15,978.66 | 0.0001 |

These are conditional multinomial comparisons with 9,999 simulations and seed 5230. In each case no simulated statistic reached the observed value; 0.0001 is the minimum attainable Monte Carlo value, not an estimate of the exact tail probability at that precision. The analytical reference would have 24 degrees of freedom for either square and 49 for the combined window.

Both squares have uneven counts under their respective homogeneous baselines. B has about 1.89 times as many detections over almost the same land area, but neither its higher total nor its larger raw $T$ alone establishes stronger spatial clustering. The reference distributions depend on the totals and cell probabilities.

### Step 3: combine the squares and reconsider the reference

```{figure} ../resources/original/firms-combined-window.svg
:label: firms-quadrat-combined-window
:alt: Fifty quadrat counts across the combined 200 km by 100 km South Sumatra rectangle, with a vertical divider marking the original two squares.
:align: center

The same 6,201 detections are pooled into a 200 km by 100 km window with fifty 20 km quadrats. The divider marks the original square boundary. Coastal land-area adjustment remains part of the calculation even though the grid cells are drawn as complete rectangles.
```

Pooling changes the null question. Separate analyses estimate one mean intensity for A and another for B. The combined analysis assumes **one constant intensity over all usable land in both squares**. Full land quadrats now have expected count approximately 124.30. That raises A's expectation from 85.96 and lowers B's from 162.80.

Consequently, the combined statistic includes both within-square unevenness and the broad west–east difference in intensity. Expanding the window has not created new fires or moved points; it has changed the reference against which their allocation is judged. The two squares may also cut across the same physical fire concentrations, so they should not be treated as independent replicated landscapes.

Try explaining the difference before calculating: if both squares were internally uniform but B still had a higher intensity, could the combined homogeneous test reject? Yes. This is why rejection does not by itself demonstrate interactions between fire events.

Use the [FIRMS quadrat notebook](../notebooks/firms-sumatra-quadrat.ipynb) to reproduce the counts, expected values, simulations and combined map. The compact [snapshot and provenance](../datasets/firms_sumatra/README.md) are included in the repository; Google Drive mounting is unnecessary. Observations on all 30 dates do not guarantee complete cloud-free coverage or equal detection opportunities.

## What can we conclude?

An unusually large $T$ indicates more variation among cell counts than expected under the stated reference. It does not distinguish interaction among events from a changing background intensity. For FIRMS, land cover, burning conditions, persistent fires and observation coverage can all affect counts. Time aggregation also matters: a month combines changing conditions and repeated observations. Rejection of homogeneous CSR does not establish fire-to-fire attraction, distinguish separate fire incidents or attribute haze in Singapore to particular sources.

NNA asks a different question about the closest other event. The K-function examines cumulative neighbour relationships across distances. Use those methods to extend the inquiry, rather than expecting quadrat counts to settle every aspect of the pattern.

## Check your reasoning

```{dropdown} 1. Should empty cells be omitted?
No. They are observations about the allocation of points within the defined window. Removing them changes the comparison and usually suppresses part of the count variation.
```

```{dropdown} 2. Two equal-area grids have the same multiset of counts but different arrangements. Must T differ?
No. The statistic uses each count and its expectation, not which cells touch. The spatial arrangement of those counts can differ while the statistic remains identical.
```

```{dropdown} 3. Why not compare means using a t-test?
With the point count and number of cells fixed, the mean count is already $n/m$. Counts $[3,3,3,3,3,3]$ and $[0,0,0,6,6,6]$ have the same mean but different variation. The question concerns allocation among cells.
```

```{dropdown} 4. Does rejection prove that individual fires attract one another?
No. These records represent detections rather than separate fires. Uneven land conditions, repeated observations of persistent fires, observation effects or dependence could all contribute. The test rejects a particular homogeneous reference; it does not identify a mechanism.
```

## Try it and read further

The [point-pattern lab](../notebooks/lab-05-point-pattern.ipynb) provides the existing course workflow. The new [reproducible teaching source](https://github.com/wcchin/geo-stat-vis/blob/main/scripts/point_pattern_examples.py) generates the original figures; its [data record](../datasets/point_pattern_teaching/README.md) explains the synthetic examples and links to the observed FIRMS snapshot. Later, aggregated FIRMS counts can support [Moran's I](../chapter_6/sec_06-03-Morans-I.md): quadrat analysis asks about allocation across cells, whereas Moran's I asks about relationships between neighbouring cell values.

- **Foundational reading:** Greig-Smith, P. (1952). [The Use of Random and Contiguous Quadrats in the Study of the Structure of Plant Communities](https://doi.org/10.1093/oxfordjournals.aob.a083317). *Annals of Botany*, 16, 293–316. Read for the historical connection between sampling scale and pattern, rather than treating vegetation quadrats as identical to our event-grid design.
- **Method reference:** [spatstat: quadrat.test](https://search.r-project.org/CRAN/refmans/spatstat.explore/html/quadrat.test.html). Check the distinction between alternatives, expected counts and simulation designs.
- **Regional data:** [NASA FIRMS archive](https://firms.modaps.eosdis.nasa.gov/download/). Record the product, confidence selection, period and download date. Recent near-real-time data can later be replaced by standard science-quality records, so preserve the version used.
