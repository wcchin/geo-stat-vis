# GeoSpatial Thinking: Describing Space in Geography

## Objectives of this lecture
- How do we define '.bold[Space]' or '.bold[GeoSpatial]'?
- Identify ways of .bold[thinking] and .bold[describng] geospatial
- Understand what is '.bold[Complete Spatial Randomness]' and '.bold[Spatial Patterns]'

---
class: center, middle, inverse

.xx-large.bold.wide[PART 1]
## What is 'Space' / 'Spatial'? 
------
.square[Geospatial .dot[] The Splatial Framework]

.headnote.square.bold.x-large[GeoSpatial Thinking]

---
class: left, middle

.split-30[.column[
### General Definition
.xkcd[How People See 'Space' and 'Spatial']

].column[.justify[

> .bold.x-large[Space] .italic[noun]

1. ​.square[[uncountable]] the area outside the earth’s atmosphere where all the other planets and stars are  
2. .square[[countable]] an area or a place that is empty  
3. .square[[uncountable]] an amount of an area or of a place that is empty or that is available for use  
4. .square[[countable, uncountable]] a place, especially a room or a building, that can be used for a particular purpose

.square[[Oxford Learners Dictionaries: Space](https://www.oxfordlearnersdictionaries.com/definition/english/space_1)]

]]
]

---
class: left, middle

.split-30[.column[
### General Definition
.xkcd[How People See 'Space' and 'Spatial']

].column[.justify[

> .bold.x-large[Spatial] .italic[adjective]  
relating to space and the position, size, shape, etc. of things in it

> .bold.x-large[Geospatial] .italic[adjective, only before noun]  
relating to information that is associated with a particular location

.square[Oxford Learners Dictionaries: [Spatial](https://www.oxfordlearnersdictionaries.com/definition/english/spatial?q=spatial) & [Geospatial](https://www.oxfordlearnersdictionaries.com/definition/english/geospatial?q=geospatial)]

]]
]


---
class: left, middle

.split-30[.column[
### General Definition
.xkcd[How AI See 'Space' and 'Spatial']

.square[generated and modified based on [Pi.ai](https://pi.ai/talk)'s response]

].column[.justify[

.bold[Spatial] refers to anything related to space, including the location, size, shape, and orientation of objects or elements within a given area or environment. It's a broad term that's used in many different fields and contexts, such as .red[geography, architecture, interior design, and psychology]. 

Some examples of spatial concepts include:
- .bold[Spatial awareness/perception]: This refers to an individual's ability to understand and navigate their surroundings, including the ability to perceive and judge distances, directions, and relationships between objects.
- .bold[Spatial reasoning]: This involves understanding and reasoning about spatial relationships between objects, such as their relative positions, distances, and orientations.
- .bold[Spatial planning]: This involves the organization and layout of physical spaces, such as the design of buildings, cities, or public spaces, to maximize functionality, efficiency, and aesthetics.
- .bold[Spatial data]: This includes any information or datasets that relate to the location, shape, or other spatial characteristics of objects or features, such as maps, satellite images, or GPS coordinates.

In general, .red.bold[spatial refers to anything that involves the arrangement or characteristics of objects or elements within a physical space].

]]
]


---
class: left, middle

.split-30[.column[
### General Definition
.xkcd[So, what is .bold.red[Space], .bold.red[Spatial], and .bold.red[Geospatial]]
].column[
- Space is a two- or three-dimensional physical realm that encompasses and contextualizes the location of objects and beings within it.
- Spatial-[some object] is the information related to the positional or geographical aspects and relationships of a specific object. 
- Geospatial: space and spatial can refer to any 'space' and 'spatial'; to differentiate and specifying geographical space, we use the term geospatial. 

.xkcd[In this course, the two terms spatial and geospatial can be used interchangeably, both refer to the space in geographical context. ]
]]

---
class: left, middle

.split-30[.column[
### The 'Splatial' Framework
.xkcd[How Geographers See 'Space' and 'Spatial']

.square[The space–place ('splatial') Framework.]
.square.small[Adapted from [Understanding the New Human Dynamics in Smart Spaces and Places: Toward a Splatial Framework](https://doi.org/10.1080/24694452.2019.1631145)]

].column[.justify[

<img src="resources/w04-img/drawing-fourspaces.png" width="70%" align="center">

]]
]


---
class: left, top

.split-30[.column[
### The 'Splatial' Framework
.xkcd[How Geographers See 'Space' and 'Spatial']

- .red[Absolute Space]
- .grey[Relative Space]
- .grey[Relational Space]
- .grey[Mental Space]

Absolute space is about .underline[the location itself]---where are the studying object?

].column[
<img src="resources/w04-img/splatial_absolute_space.png" width="80%" align="center">  
.square[Absolute Space. The red-X marker shows where the current location is.]
]]


---
class: left, top

.split-30[.column[
### The 'Splatial' Framework
.xkcd[How Geographers See 'Space' and 'Spatial']

- .grey[Absolute Space]
- .red[Relative Space]
- .grey[Relational Space]
- .grey[Mental Space]

Relative space is about .underline[the nearby area]---relative to the current target/space. 

].column[
<img src="resources/w04-img/splatial_relative_space.png" width="80%" align="center">  
.square[Relative Space. The buffer zone shows the neighborhood of current location.]
]]


---
class: left, top

.split-30[.column[
### The 'Splatial' Framework
.xkcd[How Geographers See 'Space' and 'Spatial']

- .grey[Absolute Space]
- .grey[Relative Space]
- .red[Relational Space]
- .grey[Mental Space]

Relational space is about .underline[the connectivity and the structure of connections]---how connected are them?

].column[
<img src="resources/w04-img/splatial_relational_space.png" width="80%" align="center">  
.square[Relational Space. The links show the connections between spatial units. Those connected to the current location are highlighted in blue.]
]]



---
class: left, top

.split-30[.column[
### The 'Splatial' Framework
.xkcd[How Geographers See 'Space' and 'Spatial']

- .grey[Absolute Space]
- .grey[Relative Space]
- .grey[Relational Space]
- .red[Mental Space]

Mental space is about .underline[how people think about the location].

In modelling, we can go beyond 'mental', and makes it any type of attribute.

].column[
<img src="resources/w04-img/splatial_mental_space.png" width="80%" align="center">  
.square[Mental Space. The size of point shows the familiarity of a person who stay at the current location.]
]]

---
class: left, middle

.split-30[.column[
### Summary
].column[
In general, what does space means?
- outer space
- a physical location/place/area that is empty, i.e., a gap
- a physical location/venue serves a particular urban function/purpose.

How geographers see 'space'?  
The 4 types/levels of space:
- .bold[Absolute Space]: the locations (coordinates)
- .bold[Relative Space]: the nearby area (buffer, search radius)
- .bold[Relational Space]: the connections & topological structure
- .bold[Mental Space]: how people think about the space, a dimension beyond physical space
]]

---
class: left, middle

.split-30[.column[
### Summary
].column[
As a geographer / geospatial data analyst, what is 'spatial information'?
- data related to the 4 types of .bold.red[space]
    - where is it?
    - what is found next to it?
    - what is connected to it?
    - how people describe it?

- attributes data (statistical, non-spatial) that .bold.red[attached to the space], e.g.,
    - the size (capacity)
    - the type (urban functions)
    - the crowdedness
    - the ranking
    - the demographic structure
    - etc.


]]









---
class: center, middle, inverse

.xx-large.bold.wide[PART 2]
## Spatial Patterns and Complete Spatial Randomness
------
.square[Patterns .dot[] Stationarity .dot[] CSR ]

.headnote.square.bold.x-large[GeoSpatial Thinking]

---
class: left, middle
.split-30[.column[
### What is Spatial Point Pattern? 

A bunch of points that form some patterns within a specific region.

.headnote.small.title-font.bold[John Snow's Cholera Death Incident Map]

].column[
<img src="resources/w04-img/johnsnowmap_1.png" width="90%">
]]

---
class: left, middle
.split-30[.column[
.headnote.small.title-font.bold[John Snow's Cholera Death Incident Map]

### What is Spatial Point Pattern? 

.red.bold[Visually speaking, what is the patterns here in the map?]

- How points are distributed?
- Some points .red[concentrated] at the middle.
- Some .red[outliers] are far from the cluster(s).
- Some empty spaces.

].column[
<img src="resources/w04-img/johnsnowmap_2.png" width="90%">
]]

---
class: left, middle

.split-30[.column[
### Key Aspects of Spatial Point Pattern
].column[
Spatial Point Pattern Analysis encompasses various methods and techniques that aim to:
- .bold[Explore the point locations]: This involves exploring the absolute locations/spaces of each point---where they are located. 
- .bold[Describe the points distribution]: This includes analyzing whether the points are distributed randomly, in clusters, or in a regular pattern, and determining the intensity or density of points within the study area.
- .bold[Explore the relationship between points]: This involves examining the interactions between points, such as the distance or orientation of points in relation to one another, and identifying any spatial correlation or dependence between points.
- .bold[Identify the spatial compositions and structures]: This focuses on determining the underlying spatial processes or factors that generate the observed point pattern and understanding the composition of different sub-patterns or structures within the overall pattern.

]]

---
class: center, top
### Three Major types of Point Pattern

<img src="resources/w04-img/spatial_patterns_3_basic.png" width="100%">

.red.xkcd[How to differentiate clustered from random?]

---
class: left, middle

.split-50[.column[
.headnote.small.title-font.bold[Defining Random]

### Complete Spatial Randomness .smaller[(CSR)]

- The definition of "random" distribution
- The null hypothesis for identifying significant clustered pattern
- Not a regular distribution
- Can be spatially inhomogeneous, i.e., both clusters and dispersed areas exist
    - i.e., any observed clustering or disperse patterns could be attributed to chance alone
- .bold.red[Spatial Stationarity]
].column[
<img src="resources/w04-img/describe_CSR2.png" width="100%">

]]

---
class: left, middle

.split-30[.column[

### Spatial Stationarity

].column[

Stationarity is a key concept in spatial statistics and geostatistics, .red[referring to the property of a spatial process where the statistical properties remain constant across space (or time).] 

Stationarity is an important assumption in many spatial statistical methods, including Kriging, variogram analysis, and point process models. If a spatial process is not stationary, it may be necessary to apply transformations, detrending techniques, or local models to account for the spatial variability in the data before applying these methods.

Stationarity is a fundamental concept in spatial statistics that allows for the analysis and modeling of spatial processes .red[under the assumption of consistent statistical properties across space (or time)]. Understanding the stationarity of a spatial process is crucial for selecting appropriate analysis techniques and drawing valid conclusions from the data.

]]

---
class: left, middle
.split-50[.column[
### Stationarity on a street
<img src="resources/w04-img/drawing_street.png" width="100%">

].column[
Imagine we're analyzing the occurrence of accidents along a particular street. If an accident happens at a specific location on the street, and there are no accidents on the remaining parts of the street, it doesn't mean that those sections have zero probability of accidents. In the context of stationarity, we assume that the probability of accidents happening is constant across the entire street. Therefore, even if an accident occurred at one location, the probability of accidents happening on any other part of the street remains the same.

Stationarity implies that the underlying process generating the accidents is consistent across the street, and the observed distribution of accidents can be explained by random chance rather than any specific spatial factors or variations along the street.

]]

---
class: left, middle

.split-40[.column[
### Spatial Stationarity
#### Two main types of stationarity
- .red[Strict stationarity]
- Second-order stationarity
].column[
.bold[Strict stationarity (or strong stationarity)] 

A spatial process is considered strictly stationary .red[when its statistical properties], such as the mean, variance, and autocorrelation structure, .red[do not change with location (or time)]. In other words, the spatial process behaves the same regardless of where (or when) it is observed. For instance, if a spatial process is strictly stationary, .red[the probability of finding a specific value at a given location would be the same across the entire study area.]

]]

---
class: left, middle

.split-40[.column[
### Spatial Stationarity
#### Two main types of stationarity
- Strict stationarity
- .red[Second-order stationarity]
].column[
.bold[Second-order stationarity (or weak stationarity)]

A spatial process is considered second-order stationary when only its first and second-order moments (.red[mean, variance], and autocorrelation) are constant across space (or time), while higher-order moments may vary. This weaker form of stationarity is often sufficient for many spatial statistical analyses.
]]

---
class: center, middle

### Random Spatial Points

<img src="resources/w04-img/drawing_random_pts_3.png" width="100%">

---
class: left, middle

.split-40[.column[
### Testing Strategy -- CSR
CSR represents a theoretical spatial distribution, and since its population parameters can be estimated accordingly, it serves as a useful basis for statistical testing and comparison with observed spatial patterns.
].column[
1. .bold[CSR as a Baseline]  
Complete Spatial Randomness (CSR) represents a scenario where points are distributed randomly and independently in space.
It serves as a baseline or null hypothesis for analyzing spatial point patterns.
2. .bold[Identifying Deviations from CSR]  
By comparing an observed spatial pattern to CSR, we can identify deviations that indicate potential clustering or dispersion.
Significant deviations suggest that the pattern is not random and may result from underlying spatial processes or interactions.
3. .bold[Quantifying Clustering]  
Comparing to CSR allows us to quantify the degree of clustering or dispersion in the observed pattern.
Statistical tests and measures, such as the quadrat count, nearest neighbor analysis and Ripley's K-function, can be used to assess the significance of clustering.
]]

---
class: center, middle

### How different it is compared to CSR?

<img src="resources/w04-img/spatial_patterns_2_basic_b.png" width="70%">

---
class: left, middle

.split-40[.column[
### How different it is compared to CSR?

].column[
- In spatial statistics, CSR is the common null hypothesis. 
- Before we have enough proof to claim that a pattern is clustered, we have to assume .red[everything can happen by chance], i.e., random. 
- If the evidence suggests that the pattern is unlikely to have occurred by chance, only then we can .red[reject the null hypothesis] and conclude that the pattern is clustered (or dispersed).

]]



---
class: center, middle, inverse

## The Closing Remark
------
.square[GeoSpatial .dot[] Splatial Framework .dot[] Stationarity .dot[] Complete Spatial Randomness]

.headnote.square.bold.x-large[GeoSpatial Thinking]

---
class: left, middle

.split-30[.column[
### Summary and key points
].column[
- .red.bold[Geospatial] is the space and spatial information specific for geographical context. 
- .red.bold[Spatial/Geospatial] are used interchangeably in this course to refer to the same thing. 
- .red.bold[Splatial framework], or the space-place framework, is a framework for discussing the space and place elements of a location or a geographical phenomenon. 
- .red.bold[Spatial patterns] are the description of spatial arrangement of geographical phenomena. 
    - Here, spatial point pattern is used for demonstration purpose. 
    - Random, Clustered, Dispersed
- .red.bold[Spatial Stationarity] is whether the probability of a geographical phenomenon will occur equally within the space. 
- .red.bold[Complete Spatial Randomness] (CSR) represents a scenario where points are distributed randomly and independently in space. 
    - It serves as a baseline or null hypothesis for analyzing spatial point patterns. 
]]
