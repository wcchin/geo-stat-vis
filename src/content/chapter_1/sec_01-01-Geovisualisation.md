# 1.1 Geovisualisation: different views reveal different things

A table, chart, map and flow diagram can show the same observations while helping us notice different relationships. Choosing a view is therefore part of forming a question. We ask what the representation makes easy to inspect and what information a reader still needs.

Geovisualisation uses visual representations of geographic information to support exploration, analysis and communication. Interactive maps and linked displays play an important role in its development, but the underlying habit is accessible with a small table and a few carefully chosen views. We use a display to think, then use what we learn to improve both the question and the display.

## One small example, four views

Consider two reported directions in the September 2026 train OD data: Bishan to Marymount has 256 trips, and Marymount to Bishan has 50, for the selected weekday hour category 08. These are aggregates across the reporting month. They do not describe one particular morning or count unique travellers.

```{figure} ../resources/chapter_1_original/01_several_views.png
:label: ch1-several-views
:alt: A table, bar chart, schematic endpoint layout and flow diagram display the same two reported MRT directions: 256 trips from Bishan to Marymount and 50 in the reverse direction.

The counts are real records from the supplied LTA extract used in Chapter 2. The location sketch and flow layout are schematic. Arrows show OD relationships, not observed railway routes; their widths distinguish magnitude but are not a calibrated proportional scale.
```

The table helps us retrieve exact values and inspect the field meanings. The chart makes the difference in counts easy to compare. A location view orients us to the endpoints. The flow diagram emphasises direction and connection. We can move between these views without changing the observations.

The difference raises questions rather than supplying a cause. Does it persist at other hours? What activities occur around the endpoints? Is the selected hour representative of a longer period? The two records alone cannot answer those questions, but they help us identify the additional evidence we would like.

## Maps have different purposes

A reference map provides orientation: roads, landmarks, stations and other features help us locate a place or plan a journey. A thematic map emphasises a selected variable or relationship, such as resale price, income or movement. The distinction concerns purpose. One map may provide reference context around a thematic layer.

Every display makes selections. A station symbol may locate a reference point while leaving out platforms and entrances. An area colour may summarise several observations while hiding variation within its boundary. A connection between endpoints does not establish the path between them. Reading a map involves understanding those representational choices as well as recognising locations.

## Points, areas and relationships

A point-pattern question asks about the arrangement of locations: for example, where fire detections occur within a study window. An areal question examines quantities attached to units such as districts: for example, whether neighbouring income values resemble one another. A flow question examines relationships between origins and destinations. A statistical view may compare the distributions behind any of these representations.

These are complementary views, rather than a rigid taxonomy in which every dataset has only one home. A fire record can have a location, detection time and measured attributes. An HDB sale can contribute to a point display or an area summary. Choosing a representation changes which differences become visible and which operations are meaningful.

## A first reading habit

When meeting an unfamiliar figure, identify the quantity, observation unit, period and visual encoding. Then describe one visible feature in ordinary language. “This selected direction has more reported trips” stays close to the evidence. An explanation of why requires additional reasoning and observations.

[Chapter 2](../chapter_2/chapter-2-spatial_data.md) develops the data definitions behind the MRT example. [Chapter 7](../chapter_7/sec_07-02-Key-Components-of-Maps.md) explains how scale, colour, typography, legends and layout support a visual argument. Here, the aim is to recognise that a change of view can open a new question.

**Further reading:** Çöltekin, A., Janetzko, H., & Fabrikant, S. I. (2018). *Geovisualization*. GIS&T Body of Knowledge. [Article](https://gistbok-ltb.ucgis.org/current/concept/CV-05-035). Read for how visual thinking and interaction support geographic inquiry.

**Self-check:** Which view would help you compare exact counts, and which would help you investigate direction?

```{dropdown} Feedback
A table preserves exact values clearly; an aligned chart supports magnitude comparison; a flow diagram foregrounds origins, destinations and direction. The best choice follows the question. More than one view can be useful, especially when the reader can trace the same observations between them.
```
