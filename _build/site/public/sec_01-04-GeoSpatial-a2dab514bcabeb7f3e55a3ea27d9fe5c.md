# GeoSpatial Thinking: Describing Space in Geography

## How People See 'Space' and 'Spatial'

From Oxford Learners Dictionaries: about ['Space'](https://www.oxfordlearnersdictionaries.com/definition/english/space_1)

> **Space** *noun*

1. uncountable - the area outside the earth’s atmosphere where all the other planets and stars are
2. countable - an area or a place that is empty
3. uncountable - an amount of an area or of a place that is empty or that is available for use
4. countable, uncountable - a place, especially a room or a building, that can be used for a particular purpose


From Oxford Learners Dictionaries: about ['Spatial'](https://www.oxfordlearnersdictionaries.com/definition/english/spatial?q=spatial) and ['Geospatial'](https://www.oxfordlearnersdictionaries.com/definition/english/geospatial?q=geospatial)

> **Spatial** *adjective*
relating to space and the position, size, shape, etc. of things in it

> **Geospatial** *adjective, only before noun*
relating to information that is associated with a particular location


## How AI See 'Space' and 'Spatial'

generated and modified based on [Pi.ai](https://pi.ai/talk)'s response

**Spatial** refers to anything related to space, including the location, size, shape, and orientation of objects or elements within a given area or environment. It's a broad term that's used in many different fields and contexts, such as *geography, architecture, interior design, and psychology*.

Some examples of spatial concepts include:
- **Spatial awareness/perception**: This refers to an individual's ability to understand and navigate their surroundings, including the ability to perceive and judge distances, directions, and relationships between objects.
- **Spatial reasoning**: This involves understanding and reasoning about spatial relationships between objects, such as their relative positions, distances, and orientations.
- **Spatial planning**: This involves the organization and layout of physical spaces, such as the design of buildings, cities, or public spaces, to maximize functionality, efficiency, and aesthetics.
- **Spatial data**: This includes any information or datasets that relate to the location, shape, or other spatial characteristics of objects or features, such as maps, satellite images, or GPS coordinates.

In general, .red**spatial refers to anything that involves the arrangement or characteristics of objects or elements within a physical space**.

So, what is **Space**, **Spatial**, and **Geospatial**?

- Space is a two- or three-dimensional physical realm that encompasses and contextualizes the location of objects and beings within it.
- Spatial-[some object] is the information related to the positional or geographical aspects and relationships of a specific object.
- Geospatial: space and spatial can refer to any 'space' and 'spatial'; to differentiate and specifying geographical space, we use the term geospatial.

Here, the two terms spatial and geospatial can be used interchangeably, both refer to the space in geographical context.

## How Geographers See 'Space' and 'Spatial'

### The space–place ('splatial') Framework

Adapted from [Understanding the New Human Dynamics in Smart Spaces and Places: Toward a Splatial Framework](https://doi.org/10.1080/24694452.2019.1631145)

```{figure} ./resources/w04-img/drawing-fourspaces.png
:label:
:alt:
:align: center

The splatial framework.
```


### Absolute Space

Absolute space is about __the location itself__---where are the studying object?

```{figure} ./resources/w04-img/splatial_absolute_space.png
:label:
:alt:
:align: center

Absolute Space. The red-X marker shows where the current location is.
```



### Relative Space

Relative space is about __the nearby area__---relative to the current target/space.

```{figure} ./resources/w04-img/splatial_relative_space.png
:label:
:alt:
:align: center

Relative Space. The buffer zone shows the neighborhood of current location.
```



### Relational Space

Relational space is about __the connectivity and the structure of connections__---how connected are them?

```{figure} ./resources/w04-img/splatial_relational_space.png
:label:
:alt:
:align: center

Relational Space. The links show the connections between spatial units. Those connected to the current location are highlighted in blue.
```



### Mental Space

Mental space is about __how people think about the location__.

In modelling, we can go beyond 'mental', and makes it any type of attribute.

```{figure} ./resources/w04-img/splatial_mental_space.png
:label:
:alt:
:align: center

Mental Space. The size of point shows the familiarity of a person who stay at the current location.
```



## Summary

In general, what does space means?
- outer space
- a physical location/place/area that is empty, i.e., a gap
- a physical location/venue serves a particular urban function/purpose.

How geographers see 'space'?
The 4 types/levels of space:
- **Absolute Space**: the locations (coordinates)
- **Relative Space**: the nearby area (buffer, search radius)
- **Relational Space**: the connections & topological structure
- **Mental Space**: how people think about the space, a dimension beyond physical space


As a geographer / geospatial data analyst, what is 'spatial information'?
- data related to the 4 types of **space**
    - where is it?
    - what is found next to it?
    - what is connected to it?
    - how people describe it?

- attributes data (statistical, non-spatial) that **attached to the space**, e.g.,
    - the size (capacity)
    - the type (urban functions)
    - the crowdedness
    - the ranking
    - the demographic structure
    - etc.
