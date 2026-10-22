# 3.1 Hypothesis testing

A hypothesis test evaluates how compatible an observed statistic is with a specified null model. The model includes both a statement about a population quantity and assumptions about how the observations arise. Choosing a null hypothesis without considering the observational design leaves the calculation disconnected from the question.

For a paired comparison, an illustrative null and two-sided alternative are

$$H_0:\mu_D=0,\qquad H_1:\mu_D\ne0.$$

Here $\mu_D$ denotes the mean difference in the process or population to which the model refers. It is not the observed mean $\overline{D}$. Our dataset can have a nonzero observed mean even under a model whose mean is zero, because the model allows variation. A test asks whether that observed departure is unusual under the specified model.

## Relationships, differences and uncertainty answer different questions

Before selecting a procedure, distinguish three tasks. A description reports the observations, an association summarises how variables vary together, and a model-based inference assesses a specified target under stated assumptions. A correlation between weekday and weekend activity across stops does not answer whether the average paired difference is zero: a close association can coexist with a systematic difference.

Pearson correlation describes linear association; Spearman correlation describes association between ranks and can represent monotonic relationships. Choosing between them is not simply a choice between “normal” and “non-normal” data. Regression describes a specified conditional relationship and can support prediction or inference under an appropriate design and model. A fitted association alone does not identify a causal mechanism.

Keep the quantity and its uncertainty separate. A mean difference needs its units and reference population or process; a confidence interval describes uncertainty from a particular construction. The interval and error discussion below develops these ideas, rather than treating “confidence” as a substitute for checking coverage or representativeness. These distinctions expand the introductory questions in Chapter 1; the later sections here focus on paired differences, group comparisons and their assumptions.

## What exactly does a p-value say?

A p-value is the probability, **under the null model and its assumptions**, of obtaining a test statistic at least as extreme as the one observed. For a two-sided test, departures in both directions contribute. It is not the probability that the null hypothesis is true, nor the probability that the observations were caused by chance alone.

“Chance” has no single universal meaning. In a randomised experiment it may come from treatment assignment. In a sampling model it may come from selecting observations. In a permutation procedure it comes from allowed rearrangements of labels. The analyst must explain why that source of randomness is appropriate.

Weekdays and weekends were not randomly assigned to these stops. The 5,161 stops are not 5,161 independent experiments that changed weekday status. A test that treats stop differences as independent is making a modelling assumption; it is not borrowing randomisation from the calendar.

## Connect the statistic to the question

Before testing, inspect the distributions. In the bus example, the weekday and weekend distributions are both skewed, and the same stop contributes to both. An independent-samples comparison would discard that pairing. A test of mean differences also answers a different question from whether a majority of stops have positive differences.

```{figure} ../datasets/bus_ridership_202609/bus/distribution_details.png
:label: ch3-distribution-details
:alt: Detailed distributions
:align: center

The histogram focuses on the 0–5,000 range and omits larger values from that panel. The empirical cumulative distribution includes every paired stop and shows the fraction with activity at or below each value. Its symlog horizontal scale accommodates zeros.
```

The empirical cumulative distribution is useful because it compares complete distributions without requiring histogram bins. However, a visible distributional difference does not automatically identify its cause. Stop function, service provision, surrounding land use and the day-type schedule can all contribute.

## Decisions and errors

A significance threshold $\alpha$ defines a rejection rule before the test is interpreted. Under a valid model, a Type I error means rejecting a true null hypothesis. A Type II error means failing to reject it when the specified alternative holds. Power is the probability of rejection under a particular alternative; it depends on the effect, variability, sample size and decision rule.

A small p-value does not establish a large or practically useful effect. With many observations, even modest departures can be detected under a model. Conversely, failing to reject a null does not establish equality. Report an effect estimate, its units and the uncertainty construction alongside a test result.

A confidence interval also depends on its model. A conventional 95% interval is constructed by a procedure with 95% coverage in repeated applications when its assumptions hold. It is not a guarantee for this dataset, and it is not an interval containing 95% of the individual stop differences.

## Independence is a geographical question

The map reveals that nearby stops are embedded in common corridors and neighbourhoods. Such dependence can change the sampling distribution of a statistic and make a conventional standard error misleading. A large sample does not automatically remove that problem. Transforming the variable or choosing a rank-based test does not remove it either.

The appropriate response depends on the target. Describing this snapshot may require no significance test. Studying changes over time needs repeated temporal observations. Studying an underlying spatial process may require a model or resampling design that represents its dependence. Later chapters develop tools for examining spatial structure explicitly.

**Self-check:** Explain why “the p-value is small, so weekday demand causes more boardings” contains more than one unsupported step.

```{dropdown} Feedback
A small p-value describes incompatibility with a specified null under its assumptions. It does not establish causation. Here stops were not assigned randomly to weekdays, and conventional independent-stop calculations do not represent shared routes or spatial dependence.
```

