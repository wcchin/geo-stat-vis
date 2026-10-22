# 2.1 Data preparation

Data preparation turns source records into a dataset that answers a defined question. It includes reading metadata, checking structure and quality, resolving identifiers, aligning observations, and recording decisions. The goal is not to make every field look complete. It is to preserve the meaning of the observations while making their limitations visible.

In the MRT example, the question determines the preparation. We want to demonstrate how four stations and their reported OD relationships can be linked to station information and planning areas. We therefore retain a small, explicit slice instead of treating every available record as necessary.

## Begin with the row, not the software command

The supplied OD table has these fields:

| Field | Meaning in this example | Preparation implication |
|---|---|---|
| YEAR_MONTH | Reporting month | Keep the month with every aggregate |
| DAY_TYPE | Source day-type category | Do not pool weekdays and weekends without considering exposure |
| TIME_PER_HOUR | Source hour category | Several hours are repeated observations of a pair, not duplicate pairs |
| PT_TYPE | Transport type | Retain in the observation key |
| ORIGIN_PT_CODE | Origin station-complex identifier | Read as text; check against the station lookup |
| DESTINATION_PT_CODE | Destination identifier | Match separately from the origin |
| TOTAL_TRIPS | Reported trip count | Check numeric type, non-negativity and scope |

A candidate composite key is month + day type + hour + transport type + origin + destination. In the supplied 887,478-row OD extract, no two rows repeat that full key. This check identifies a useful table structure; it does not prove that every possible pair or hour is present, or that every count is correct.

The station-activity table has a different unit: a station, temporal category and transport type, with tap-in and tap-out volumes. The exit table has one record per exit location. Document these meanings before combining anything.

## Preserve source records and make selection explicit

Keep the source extract unchanged, and make a prepared copy through a reproducible filter. Our teaching selection is:

```python
codes = ["NS17/CC15", "NE12/CC13", "EW8/CC9", "CC16"]
selected = od.loc[
    od["YEAR_MONTH"].eq("2026-09")
    & od["DAY_TYPE"].eq("WEEKDAY")
    & od["TIME_PER_HOUR"].eq(8)
    & od["ORIGIN_PT_CODE"].isin(codes)
    & od["DESTINATION_PT_CODE"].isin(codes)
].copy()
```

Both endpoint filters matter. Filtering only the origin would retain trips to destinations outside the four-station set and answer a different question. Changing the hour or station set is legitimate, but it creates another sample definition that must accompany the results.

The selected table has 12 rows. Its trip counts sum to 12,904. Record both row count and quantity total: later, a join might preserve one while changing the other. A checksum of the source file and a saved filtering script make it easier to identify exactly which version produced a figure.

## Clean identifiers without changing the entities

Store station codes as text, remove unintended whitespace, and inspect distinct values. A string such as `NS17/CC15` is the supplied identifier for a station complex in these records. Splitting it into two rows and copying the trip count into each would duplicate the observation. If we need line membership, we can maintain a separate station-to-line table without duplicating the OD facts.

Names are useful for people but can be unreliable keys: spelling, capitalisation, language and abbreviations can change. Our small lookup explicitly connects the four supplied codes to station names checked against LTA materials. This is a curated demonstration, not a claim that every station in the national data has been resolved.

Coding a category numerically does not make it quantitative. Replacing day-type labels with 0 and 1 can help storage or modelling, but an average code is not an average travel volume. Record the codebook so that values remain interpretable.

## Distinguish missing, zero and excluded

A recorded zero means the source reports a count of zero under its definitions. A missing value means a quantity is unavailable in the table we are using. An excluded record is one we deliberately removed by the selection rule. These states should not be collapsed automatically.

Our four-station matrix has 16 possible ordered cells, including self-pairs. Only 12 appear in the slice; the four self-pairs are absent. We retain those cells as missing. A display with a dash communicates this more accurately than silently filling every blank with zero. To interpret absence as zero, we would first need a source rule that justifies that treatment.

Likewise, an unusually large reported count is a reason to inspect the record, not an instruction to delete it. Check whether it reflects a busy relationship, an aggregation difference, an input error or duplication. Data cleaning should follow a reasoned rule rather than remove observations that make a graph inconvenient.

## Align scope, time and geography

Joining two tables requires compatible entity definitions. Comparing counts also requires compatible periods and exposure. A month contains more weekdays than weekend days; equal monthly totals would not imply equal daily averages. If a daily measure is wanted, its denominator must count the relevant days for that source category. The selected OD counts remain monthly aggregates throughout this chapter.

Geographical alignment requires compatible coordinate systems, valid geometry and a clear representation. We choose the alphabetically first exit code per station, breaking ties by source object ID, as a reference point. All four happen to use Exit A. This convention makes the demonstration reproducible; it does not establish that Exit A is the best representation for accessibility or service-area analysis.

For point-in-polygon matching, both inputs use EPSG:4326. No distances are calculated. For a future buffer, transform both inputs to a suitable metric CRS before measuring. A correctly declared CRS does not guarantee that coordinates are accurate or that the chosen reference location suits the question.

## Tabulate, inspect and keep an audit

A small inspection table should show original identifiers beside readable names, the temporal selection and the quantity. Compare a few prepared rows with the source before generating figures. Useful checks include key uniqueness, numeric ranges, missing attributes, join matches and totals before and after each operation.

The [bundled audit and reproduction scripts](../datasets/mrt_data_foundations_202609/README.md) record the slice, input versions, selected reference points and spatial matches. The next section uses this prepared slice to examine how reported counts vary. We interpret that distribution conditional on the selection, rather than generalising it to the whole MRT network.

**Self-check:** Why is a repeated origin code not necessarily a duplicate?

```{dropdown} Feedback
A station can have several destinations and repeated temporal categories. We check the full observation key. Two identical origin codes can belong to different, valid observations.
```

**Self-check:** A coordinate has ten decimal places. Is it accurate to that precision?

```{dropdown} Feedback
No. The stored precision does not establish positional accuracy. Source methods, geocoding choices and validation determine the uncertainty of the location.
```
