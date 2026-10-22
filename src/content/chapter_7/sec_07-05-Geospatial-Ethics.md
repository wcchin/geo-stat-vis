# 7.5 Framing, uncertainty and responsible persuasion

Every map selects. It selects observations, boundaries, symbols, labels and an order of presentation. Those choices direct attention even when no one intends to persuade. Research on visualisation rhetoric shows how additions and omissions in data, representation, annotation and interaction can privilege particular interpretations [2]. The practical response is to make consequential choices inspectable.

## Separate an observation from an explanation

Consider two possible headlines for the comparison:

> “The selected Tampines and Woodlands blocks have equal nearby stop counts but different recorded boarding activity.”

> “Tampines offers better transport and therefore commands higher home prices.”

The first states the checked comparison, including its limited scope. The second replaces activity with quality, generalises blocks to towns and introduces causation. It is an attractive narrative shortcut because it connects several layers with one explanation. The dataset does not justify that explanation.

Our advertising-inspired brief asks for relevance, tension and a memorable idea. In a teaching book, those devices serve understanding. A persuasive ending should make the evidence and its limits easier to remember. It should not make a weak claim feel certain.

## Show the effect of a boundary choice

```{figure} ../datasets/neighbourhood_story_2026/figures/04_radius.png
:label: ch7-04-radius
:alt: Nearby record counts for the same blocks using 500 metre and 800 metre radii
:align: center

A sensitivity comparison, keeping selected blocks and source records fixed. Counts refer to the specified categories and coordinate representations. Expanding the radius increases the area searched; it does not improve the underlying facilities or establish a travel-time catchment.
```

None of the three blocks has a hawker-centre directory point within 500 m. That statement is narrower than “there is nowhere nearby to eat.” Restaurants, coffee shops, food courts and other outlets are outside this directory. At 800 m, the counts can change without any underlying facility moving. A category boundary and a spatial boundary both shape the story.

The same issue affects park records. Counting reference points gives each point equal weight. Measuring actual park area, distance to an entrance or a route to a usable recreation facility would answer different questions. A precise distance to an unsuitable representation can still be an unsuitable measure.

## An evidence ledger

Before publication, write down what each part of the story supports. This is especially useful when an appealing caption begins to sound stronger than the analysis.

| Evidence | Supported statement | Additional evidence needed for a stronger statement |
|---|---|---|
| Observed block sale medians | The selected sales have these median prices | Comparable-property modelling for an adjusted price relationship; income and financing context for affordability |
| Straight-line stop proximity and counts | These supplied stop records lie near the reference point | Pedestrian network, operating services, frequency and journey times for accessibility |
| Nearby boarding totals | Qualifying stops record this aggregate boarding activity | Origins, destinations and population exposure for residents' travel demand |
| Selected POI locations | These category records lie within the radius | Facility type, capacity, opening hours, entrances, quality and user needs for practical convenience |
| Three illustrative cases | The measures can differ within these examples | A defined sample and broader analysis for generalisation to towns or the city |

The temporal mismatch matters too. September bus activity does not describe the exact transport conditions at every January–June sale. A 2026 directory does not establish whether a particular centre was available on a transaction date. We show the sources together to teach measurement and communication, while declining a historical causal interpretation.

## Privacy, attribution and consequences

Public data still deserves care. Block-level resale information should not be turned into a speculative story about an individual household. Bus aggregates should not be described as traces of identifiable passengers. Avoid labelling whole neighbourhoods as undesirable, poorly served or “cheap” on the strength of a few transactions and a narrow POI layer. Use observed-price language rather than social labels about residents.

Credit the originating agencies and distinguish them from a mirror that prepares coordinates. A code repository's software licence does not automatically license every dataset it contains. This chapter identifies the data licence and the OneMap attribution separately from software. If a future notebook adds another layer, its provenance and redistribution terms need their own check.

**Reader test.** Ask someone to read only the title, figures and final paragraph. What claim do they think you made? If it is stronger than the evidence ledger, revise the visual emphasis or wording before adding more caveats in small print.
