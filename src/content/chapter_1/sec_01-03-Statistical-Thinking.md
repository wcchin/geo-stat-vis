# Statistical thinking: what would count as convincing evidence?

Statistical thinking begins when we ask how observations vary, what comparison matters, and how much confidence a claim deserves. It is useful before we know a test's name. The first task is to connect a question with an observation unit and a meaningful reference.

Suppose a busy bus stop has higher weekday than weekend boardings. Before explaining that difference, we need to know whether the figures cover the same number of days, whether the same stop is compared, and whether a typical day or a monthly total is the quantity of interest. The calculation follows those decisions.

## Describe what was observed

Description summarises the observations we have. A centre describes a typical or average value; spread describes variation; a distribution shows how observations occupy the range. These summaries complement a map by helping us inspect what the colours and symbols represent.

One average can hide important differences. A few busy stops can pull a mean above the values seen at most stops. An area average can hide a mixture of smaller and larger values. [Chapter 2](../chapter_2/sec_02-02-Frequency-Distribution.md) explains means, medians, spread, distribution shape and cumulative distributions using the MRT example. Here, carry forward a simple habit: inspect variation alongside a headline summary.

## State the comparison

A difference becomes interpretable when its reference is clear. We might compare weekdays with weekends at the same stops, a selected price group with all observed sales, or an event arrangement with patterns generated under a specified model. Each comparison asks something different.

The word “random” also needs a definition. Uniformly placing points within a rectangle creates one expectation. Allowing event likelihood to vary with available habitat creates another. A departure from the first expectation might reflect that varying background rather than interaction between events. The point-pattern chapters introduce these choices through explicit study windows and reference models.

## Ask where uncertainty comes from

If we have the reported records for a particular month, we can calculate their descriptive average. Generalising to other months, unobserved places or an underlying process raises another question: what makes these observations informative about that target?

Sampling, measurement, incomplete coverage and model assumptions can each introduce uncertainty. More records may improve some estimates while leaving systematic coverage errors unresolved. Nearby stops can share routes and passengers; treating them as independent observations can therefore misrepresent how much independent evidence we have.

Inference uses a stated model or design to reason beyond a direct summary of the available records. A test or interval does not supply its own justification. [Chapter 3](../chapter_3/sec_03-01-Hypothesis-Testing.md) develops effect estimates, confidence intervals, hypothesis tests and comparison designs, including why an impressive number of records cannot replace an appropriate model.

## Separate a relationship from its explanation

If higher sale prices occur near busy transport locations, we have a possible association to investigate. Several processes could contribute: accessibility, centrality, housing characteristics, land use or selection into the observed sales. A visual association alone cannot identify which explanation is responsible.

An explanation becomes more credible when the study design and additional evidence help distinguish alternatives. A useful conclusion may be narrower than our initial story: the records show a descriptive contrast, and a proposed mechanism remains a question. That is a productive outcome because it tells us what to investigate next.

## Five questions to keep nearby

Before interpreting a pattern, ask: what constitutes one observation; compared with what; over which places and period; what could change the result; and what evidence would distinguish the proposed explanation from alternatives? You do not need to answer every question immediately. Recognising an unanswered question helps you choose the next observation or analysis.

For example, a satellite fire detection is not automatically one distinct fire. Repeated detections and the observation process matter. Similarly, a resale registration describes an observed transaction rather than every household's housing conditions. These distinctions connect statistical thinking directly to data preparation in Chapter 2.

```{dropdown} Self-check: We have more than 5,000 stops. Does that settle the uncertainty question?
No. First identify the target and source of uncertainty. Stops can share routes and geographical conditions, and one month's aggregates do not provide repeated observations of individual days. The number of rows alone does not establish independence, coverage or generalisability.
```
