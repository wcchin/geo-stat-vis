# Chapter 2: Data and Spatial Data

Before asking whether a pattern is clustered, unusual or changing, we need to know what the observations represent. A table can look tidy while mixing different units. A join can run successfully while counting every trip several times. A map can look precise while locating the wrong geographical object. Preparing data is therefore part of geographical reasoning, rather than an administrative step before the real analysis begins.

This chapter follows a small Singapore MRT example from separate records to an interpretable spatial dataset. We use four stations—Bishan, Serangoon, Paya Lebar and Marymount—to learn how to inspect observations, summarise their distributions, transform quantities, classify values and connect tables. We need tables and explanatory diagrams rather than a map of the entire network.

## One transport system, several kinds of data

A station can be represented by a code and name, by a reference point, by several exit locations, or as one endpoint of a trip. These representations are related, but they are not interchangeable. A station-exit table records exits; a ridership table records aggregate activity. Attaching an exit to a trip does not turn that trip into an observed movement through the exit.

```{figure} ../datasets/mrt_data_foundations_202609/figures/01_row_meaning.svg
:label: ch2-row-meaning
:alt: Three tables have different row meanings: one row per station complex, one row per directed OD observation with temporal categories, and one row per exit location.

The row meaning determines which fields can identify an observation. Repeated station codes can be legitimate in an observation or exit table, while the station lookup requires unique keys.
```

Our working question is: **How do separate transport records become a reliable spatial dataset that we can explore?** We fix one month, day type and hour category: September 2026, `WEEKDAY`, and `TIME_PER_HOUR = 8`. Both endpoints must belong to the four selected stations. The resulting slice contains 12 reported directed origin–destination pairs and 12,904 trips. These are monthly aggregates for that weekday hour category, not trips observed on one morning, daily averages or unique travellers.

| Station complex | Code in the supplied ridership data | Exit records in the location snapshot |
|---|---|---:|
| Bishan | NS17/CC15 | 5 |
| Serangoon | NE12/CC13 | 8 |
| Paya Lebar | EW8/CC9 | 4 |
| Marymount | CC16 | 2 |

The cases were chosen for teaching before comparing their volumes. Three show combined interchange identifiers; one has a single code. The slice is deliberately small and conditional on selection. It does not describe the distribution of activity across Singapore's full network.

## Entities, observations and variables

An **entity** is something we distinguish, such as a station complex. An **observation** is a record about an entity or relationship under stated conditions, such as an OD pair for a particular month, day type and hour. A **variable** is an attribute recorded for observations, such as trip count. Identifying these separately helps prevent a common mistake: treating every row as if it represented a different place or person.

Station codes are nominal identifiers, even when they contain digits. They cannot sensibly be averaged. A reported trip count is a discrete numerical variable. An ordered category, such as a low/medium/high classification, is ordinal: its order is meaningful, but its labels do not preserve the original differences. The hour field provides temporal context; 23 followed by 0 also reminds us that time can be cyclic. A numerical storage type alone does not determine a variable's meaning.

For quantitative data, distinguish quantities with a meaningful zero, such as trip counts, from scales where zero is conventional, such as temperature in degrees Celsius. Ratios like “twice as many reported trips” require a suitable quantity and comparable coverage. A ratio of station codes has no interpretation.

## Adding geography

Spatial data connects attributes with a representation of location. In vector data, points can represent station reference locations, lines can represent railway segments, and polygons can represent planning areas. A straight connection between OD endpoints represents a relationship; it is not evidence of the route travelled. Raster data instead records values on a grid, as in a satellite image or gridded temperature surface. A station table can be combined with raster data, but the meaning and resolution of the grid must then be considered.

A coordinate reference system (CRS) specifies how coordinates relate to the Earth. Our exit points and planning-area polygons use EPSG:4326. The prepared table explicitly stores longitude and latitude. Check axis conventions when moving between software: coordinates labelled latitude/longitude in a document may be expected as x/y, or longitude/latitude, in an operation. For later metre-based distance calculations in Singapore, a suitable projected CRS such as EPSG:3414 is needed. Assigning a CRS label and transforming coordinates are different operations.

Representation also has a scale. We choose one source exit per station as a teaching reference point; we do not call it the station centre. A planning-area label attached to that point does not identify the residence of passengers, an entire station catchment, or every part of the station complex. More decimal places in a coordinate indicate stored precision, not independently demonstrated positional accuracy.

## The route through this chapter

[Data preparation](sec_02-01-Data-Preparation.md) establishes the unit, scope and quality checks. [Frequency distributions](sec_02-02-Frequency-Distribution.md) help us inspect variation. [Transformation](sec_02-03-Data-Transformation.md) separates changes of arrangement, measure and scale. [Classification](sec_02-04-Data-Classification.md) groups values for interpretation. [Spatial databases](sec_02-05-Spatial-Database.md) then bring the tables and geometries together through explicit relationships.

By the end, you should be able to explain what a row represents, select a meaningful summary or transformation, justify class boundaries, and check whether an attribute or spatial join preserves the intended observations. These foundations support the statistical comparisons in Chapter 3 and the spatial pattern methods that follow.

## Sources and reproducibility

The observations are instructor-supplied LTA September 2026 train OD and station-activity extracts. Selected exit records come from an LTA-derived, pinned third-party snapshot with an update field of 2 December 2025; planning polygons reuse the book's URA MP2019 teaching copy. The different vintages are explicit. This example demonstrates data operations rather than making a time-matched assessment of current transport service.

See the [selected data, source attribution, preparation rules, numerical audit and offline scripts](../datasets/mrt_data_foundations_202609/README.md). All new chapter illustrations are original. Conceptual model curves are labelled as illustrations; the trip observations are real records from the supplied extracts.

**Self-check:** Is a point always a station?

```{dropdown} Feedback
No. It could represent a station centre, a selected exit, an individual platform or another reference location. Geometry type tells us how a feature is represented; metadata tells us what the feature means.
```

## Try it yourself

Apply the concepts in the corresponding [Part 3 notebook catalogue](../part3.md). The linked learner notebooks include guided activities; companion solutions are available from their introductions or from the catalogue.

- [Explore distributions](../notebooks/exploring-distributions.ipynb)
- [Transform and classify values](../notebooks/data-transformation-classification.ipynb)
- [Investigate spatial aggregation](../notebooks/spatial-aggregation.ipynb)

**Reflect:** Compare a histogram or classification result under two reasonable parameter choices. Which features are stable, and which are choices made by the analyst?
