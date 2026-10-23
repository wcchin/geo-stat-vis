# Worked Examples

Knowing how a method works is different from deciding **when to use it, what to represent, and what its results allow us to say**. The worked examples in this part bring those decisions together around geographical questions. Rather than introduce another set of techniques to memorise, they show how data, analytical choices and visual communication shape an investigation.

You can read either example independently. Each gives a short introduction to any application-specific concepts not covered in the [core chapters](part1.md), points you to related explanations, and identifies the limits of the available evidence.

## Explore the case studies

### People and Groups: Analysing Point Patterns in Gordon Square

*Can individuals appear clustered while the groups they belong to appear more regularly spaced?*

People sitting in a London garden provide an accessible example of a fundamental analytical decision: **what counts as one point?** The case compares individual and group representations through nearest-neighbour and multiple-distance thinking, asking how the observation unit changes the geographical question.

**Read:** [Gordon Square case study](worked_examples/sec_04-A-Demonstration-point-pattern.md)  
**Related core topics:** [Nearest-neighbour analysis](chapter_4/sec_04-03-Nearest-Neighbor-Analysis.md) and [Ripley's K-function](chapter_4/sec_04-04-Ripleys-K-Function.md).

### Visualising Healthcare Accessibility in Singapore: From Mobility to Service Intensity

*Does living close to a clinic necessarily mean having better access to healthcare?*

This case follows a sequence of flow maps, an aggregated flow diagram, travel-distance distributions and accessibility maps. It explores how **different visualisations answer different questions** about modelled movement and potential service access. Short explanations introduce the radiation and two-step floating catchment area (2SFCA) models as application-specific background, without assuming you have studied them in Part 1.

**Read:** [Singapore healthcare accessibility case study](worked_examples/sec_07-An-Example-accessibility.md)  
**Related core topics:** [Spatial data](chapter_2/chapter-2-spatial_data.md) and [Geovisualisation and storytelling](chapter_7/chapter-7-geovisualisation.md).

## How to read a worked example

Follow the geographical argument rather than just the sequence of figures:

1. **Question:** What are we trying to understand, and for whom?
2. **Evidence:** What do the observations, locations and spatial units actually represent?
3. **Choices:** Why were particular comparisons, models or visualisations used?
4. **Interpretation:** What does each result reveal, and what does it leave unresolved?
5. **Reflection:** How could a different representation, assumption or scale change the conclusion?

These questions are prompts for critical reading, not a rigid recipe. Real investigations often revisit an earlier choice when evidence challenges an initial interpretation.

## From case studies to hands-on practice

Part 2 focuses on **reasoning through an investigation**; it is not a second methods textbook or a catalogue of finished solutions. The [Data and Notebooks](part3.md) section supports selected methods with Python exercises. In particular, the [NNA self-study notebook](notebooks/lab-05-nna-self-study.ipynb) offers a reproducible *synthetic* comparison relevant to Gordon Square; it does not reproduce that example's group-level analysis.

The case studies reuse earlier teaching figures and project outputs, with their provenance and uncertainties stated where relevant. Do not treat every displayed numerical or visual result as newly reproduced in this book. When using a case in your own work, ask what evidence would be needed to verify or extend its conclusions.
