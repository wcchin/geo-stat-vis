# Why visualisation? From seeing to investigating

Visualisation gives us something to inspect, compare and question. Its value is especially clear when an initial impression changes after we add context. That change can be the most useful result of an exploratory figure: we learn that our first question was incomplete.

## A concentration needs a comparison

Imagine two areas displayed in a housing study. Area A has 20 upper-price-group sales and Area B has 10. A display of these counts makes A more prominent. Now add all-sales totals: A has 100 sales overall, while B has 20. The upper-group shares are 20% and 50% respectively.

```{figure} ../resources/chapter_1_original/02_denominator.png
:label: ch1-denominator
:alt: Invented example comparing 20 versus 10 upper-group sales with their shares of all sales: 20 out of 100 in Area A and 10 out of 20 in Area B.

Invented teaching numbers, not findings about HDB neighbourhoods. Both views are arithmetically correct. Counts identify more selected transactions; shares describe their composition relative to the chosen denominator. Neither view establishes the cause of a difference.
```

A reader interested in the number of selected sales may need the first view. A reader interested in their prevalence among all observed sales needs the second. The useful question is “which comparison serves our purpose?” Chapter 5 returns to this issue with real HDB data and density comparisons.

An extra layer of context does not necessarily settle the inquiry. Different flat types, sizes, remaining leases and transaction periods could still matter. Visual exploration progresses by identifying consequential questions and finding ways to examine them.

## Exploration and communication

During exploration, a display helps the analyst discover possibilities. You might change a boundary, inspect a subset or compare another variable. During communication, a display helps another person follow an interpretation and assess its evidence. These purposes can overlap: a well-designed teaching figure may guide an initial reading and invite further exploration.

An exploratory display can be unfinished and still useful. A public-facing figure needs enough context to stand on its own, including units, period and source. A busy interactive dashboard does not automatically offer deeper exploration, and an elegant static figure does not automatically provide strong evidence. Its usefulness depends on the task it enables.

Research in geovisualisation treats visual thinking as part of inquiry, extending the role of maps beyond presenting final results. MacEachren and Kraak (2001) provide one foundation for that perspective. We keep the detailed design decisions for Chapter 7, where we can connect them to an audience and a complete example sequence.

## Data, information and an interpretation we can defend

Recorded values become informative when we know what they measure and how they relate to a question. An interpretation connects that information to a claim. It becomes more persuasive when a reader can follow the connection, inspect the comparison and identify what could change the conclusion.

This progression is iterative. A map may reveal an error in a table. A calculation may show that a visually striking contrast is small relative to the reference quantity. A local expert may explain that two apparently comparable facilities serve different functions. Meaning develops through those checks; it is not a guaranteed final product of drawing a figure.

## A short visual-thinking guideline

The course uses **Observe, Think, Assess, Show (OTAS)** as a practical reminder. Observe the records and representations. Think about possible interpretations and alternative explanations. Assess the data handling and the evidence needed to distinguish them. Show an interpretation that a reader can inspect, and use their feedback to return to earlier questions.

This is a flexible course guideline, not a mandatory sequence or a claim that every investigation begins with a finished dataset. A question may motivate new observation, and assessment may send us back to the source. The fuller planning activities, communication choices and feedback loop now sit in [Chapter 7's storytelling section](../chapter_7/sec_07-01-Geospatial-Data-Storytelling.md).

**Further reading:** MacEachren, A. M., & Kraak, M.-J. (2001). *Research Challenges in Geovisualization*. Cartography and Geographic Information Science, 28(1), 3–12. [Publisher record](https://doi.org/10.1559/152304001782173970).

```{dropdown} Self-check: Which area has more upper-price-group sales, and which has the larger share?
A has more selected sales: 20 rather than 10. B has the larger share of its observed sales: 50% rather than 20%. A statement about “more” needs to identify the quantity being compared.
```
