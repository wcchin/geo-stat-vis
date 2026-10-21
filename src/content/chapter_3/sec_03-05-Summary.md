# 3.5 From a statistical result to a geographical interpretation

The bus example provides a clear descriptive finding: most paired stops have higher weekday daily-average boardings in September 2026, and the mean difference exceeds the median difference. The maps, distributions and summaries describe where and how activity differs in the supplied snapshot. Explaining those differences, or extending them to another period, requires additional evidence.

## Build an interpretation in a useful order

Begin with the observation and period. Here the unit is a stop, the measurements are monthly day-type totals converted to daily averages, and the paired comparison includes only stops reporting both day types. State what was excluded or left missing. Then report the size and direction of the observed difference in meaningful units.

Next explain the model, if an inferential calculation is used. A paired t-test targets a mean difference; a signed-rank test addresses a different distributional null; a sign summary describes the balance of directions. An ANOVA across categories requires categories that were not defined from the outcome being tested. The test name is not a substitute for identifying its target.

Finally, relate the result to geography. Shared routes and neighbourhoods connect stop observations. Interchanges and ordinary roadside stops have different functions and distributions. Group boundaries and naming rules affect comparisons. These issues belong in the reasoning that leads to an interpretation, not only in a final sentence about limitations.

## An example of a supported statement

> Among 5,161 bus stops with both day types reported in September 2026, 4,300 had higher weekday daily-average boardings. Across those stops, the mean weekday-minus-weekend difference was about 150 boardings per day and the median about 63. These summaries describe the supplied month. Conventional independent-stop tests do not account for shared routes and spatial dependence, and the aggregate data do not reveal day-to-day variability.

This statement distinguishes an observed comparison from a broader claim. It does not require us to pretend the data are uninformative merely because a simple inference model is imperfect.

## Questions to carry into spatial analysis

A difference between geographical groups may reflect their composition, their context or both. A stop category with higher boardings may contain more centrally located stops, larger facilities or more services. A comparison alone cannot establish that its label causes the difference.

Subsequent work could add daily observations, service frequency, independently verified stop functions and surrounding land use. A model could then distinguish specific relationships while accounting for repeated and spatial observations. The additional variables should follow a stated question rather than become a search for any statistically significant association.

Chapters 4 and 5 investigate the arrangement of point events and local concentrations. Chapter 6 examines similarity of attributes across neighbouring areas. Together these topics extend the current chapter's central lesson: a valid interpretation depends on how observations are represented, related and compared.

## Self-study feedback

**Why are the 22 weekdays not 22 observed replicates?** The source reports their combined volume. Individual daily values and their variation cannot be recovered from a total alone.

**Why retain pairing?** Weekday and weekend values refer to the same stop. The within-stop difference preserves that connection and answers a question about changes within those units.

**Why can a large sample still have a misleading standard error?** The conventional calculation depends on independence. Common routes and spatially related environments can connect many observations.

**Why do ranks not solve spatial dependence?** Ranking changes numerical information while leaving the relationships among stops intact.

**Why define groups before inspecting their volumes?** Groups derived from volumes would already be separated by the response, so a subsequent comparison would partly restate the construction rule.

**Why show means and medians together?** A mean describes total activity per stop on average, while a median describes the middle stop. In a skewed distribution they answer different questions.
