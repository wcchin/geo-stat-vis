# 1.4 Geospatial thinking: why locations and relationships matter

Imagine two amenities equally distant from your home on a straight-line sketch. One has a direct path; the other requires crossing a major road and finding an entrance. Now imagine a friend farther away who is easy to reach by a direct train connection. Familiarity, mobility and purpose may change which journey you consider convenient.

These are ordinary experiences, but they expose an important analytical choice. Coordinates, proximity, connections and lived meanings describe different aspects of a place. Geospatial thinking asks which aspect matters to the question and how to represent it.

## Several perspectives on the same setting

**Absolute space** provides a positional reference: where is a station, home or event? Coordinates help us locate and compare features within a defined system. A reference point may be appropriate for one task while an entrance, building footprint or route is needed for another.

**Relative space** concerns relationships such as distance, travel time and accessibility. “Nearby” depends on the measure and circumstances. A radius gives one explicit definition, while a pedestrian route or public-transport journey gives another. Relative space is broader than a buffer around a point.

**Relational space** foregrounds connections and the relationships through which places acquire roles. Social ties, movements and exchanges can link distant places and give significance to an otherwise unremarkable location. A network diagram offers one representation of those relationships, rather than a complete account of relational space.

**Mental space** brings perceptions, familiarity, memories and meanings into view. The same route can feel straightforward to one person and unfamiliar to another. Understanding that experience may require interviews, diaries or other observations beyond coordinates and aggregate counts. A numerical attribute attached to a point does not, by itself, measure perception.

```{figure} ../resources/chapter_1_original/03_spatial_perspectives.png
:label: ch1-spatial-perspectives
:alt: Four schematic panels emphasise a reference location, a distance neighbourhood, selected connections and hypothetical familiarity in the same setting.

Original conceptual illustration. All positions, connections and perception cues are invented. The four panels are teaching lenses informed by space–place scholarship; they are not separate stages that a place passes through or an exhaustive classification of geographical theory.
```

The space–place, or “splatial,” framework discussed by Shaw and Sui (2020) motivates attention to multiple spatial perspectives. This chapter uses a simplified interpretation to help us ask questions. The distinction should expand the inquiry: it should not reduce absolute space to a coordinate, relative space to a circle, relational space to a graph, or mental space to an arbitrary score.

## Neighbourhoods, scale and boundaries

An area boundary can organise data, but its analytical meaning depends on the task. A planning area may be useful for reporting; a walking catchment may be more useful for reaching a facility. Changing the boundary or aggregation scale can change the visible pattern, even when the underlying records stay fixed. We therefore carry the definition of the study area and neighbourhood with the result.

This also affects statements about people. An area's average income does not tell us the income of every resident. A block's observed resale median does not describe every flat's value. Moving between individual, point, block and area representations requires careful interpretation. Chapter 2 develops observation units and aggregation; [Chapter 6](../chapter_6/sec_06-02-Statistical-Spatial-Testing.md) develops explicit neighbourhood structures.

## Similarity and difference both deserve attention

Nearby observations may resemble each other because of shared environments, interaction or common processes. Tobler's first law is a useful prompt to examine such relationships, rather than a guarantee that every neighbouring pair must be similar. Roads, coastlines, institutions and other boundaries can create sharp differences over short distances. Distant places can also be connected through transport, trade or social relationships.

**Spatial dependence** concerns relationships between observations across space. **Spatial heterogeneity** concerns geographical differences in distributions or processes. Both can matter: observations may be related within a region while the relationships or conditions vary between regions. We introduce those ideas here so that later methods have a geographical purpose, rather than becoming calculations detached from places.

## A short reflection on AI and representation

An AI system might describe a neighbourhood from text, classify an image or compare numerical location features. Those inputs make different aspects of a place available to the system. A plausible explanation still needs to be checked against the observations, task and representation. Ask which geographical relationships the inputs capture, and which experiences or processes would require other evidence. This is a question about analytical representation, not an assumption that all AI systems perceive space in one way.

## A local reading that brings the perspectives together

Feng, Chin, Gao, Chua and Ho (2024) examine older adults' activity spaces in Singapore through absolute, relative, relational and mental perspectives. Their study offers a local example of why locations, social connections and experiences can contribute complementary evidence about everyday life. Read it as an invitation to consider what a location-only dataset leaves open; a fuller worked case can be developed later in the book.

**Further reading**

- Shaw, S.-L., & Sui, D. (2020). *Understanding the New Human Dynamics in Smart Spaces and Places: Toward a Splatial Framework*. Annals of the American Association of Geographers, 110(2), 339–348. [Publisher record](https://doi.org/10.1080/24694452.2019.1631145).
- Feng, C.-C., Chin, W. C. B., Gao, S., Chua, V., & Ho, E. L.-E. (2024). *Illustrating a Splatial Framework to Aging: Absolute, Relative, Relational, and Mental Space in Singapore*. Transactions in GIS, 28(7), 2281–2294. [Open-access article](https://onlinelibrary.wiley.com/doi/full/10.1111/tgis.13235).
- Tobler, W. R. (1970). *A Computer Movie Simulating Urban Growth in the Detroit Region*. Economic Geography, 46(sup1), 234–240. [Publisher record](https://doi.org/10.2307/143141). This foundational reading motivates the discussion of geographical relationships; our teaching examples remain regional.

## Your question, ready for data

Return to the place or journey you chose at the start of the chapter. Identify one observation that would help investigate your question. Would it record a location, an event, a connection, an area summary or a person's experience? What period and geographical representation would it need?

That is the bridge to [Chapter 2](../chapter_2/chapter-2-spatial_data.md). Before choosing a method, we learn to ask **what our observations actually represent**—and how to prepare them so that the analysis remains connected to the question.

**Self-check:** Is the nearest facility necessarily the easiest one to use?

```{dropdown} Feedback
The answer depends on the definition of nearest and the person's purpose and circumstances. Straight-line distance, network distance, travel time, entrances and familiarity can point to different comparisons. State which meaning your data can support, and identify what else you would need.
```
