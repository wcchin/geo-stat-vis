## Principles of Cartographic and Geospatial Visualization
------



## Objectives of this lecture

- **Think Spatially**---the key to geospatial data visualization.
- **Think Statistically**---why this is important in doing geospatial visualization?
- Get to know what the **components of Cartography**: scales, coordinate system, typography, colors, etc.

---




## Principles of Cartographic & Geospatial Visualization
---

### Visualization?
The comic [](#catprox) is a visualization of the relationship between human proximity to cat and the intelligence of the person.

Visualization is .mark[the process of representing data or information] in a graphical or pictorial form .mark[to communicate an idea, concept, or .red[pattern]] more effectively.

```latex
\begin{figure}[!htbp]
\centering
\includegraphics[width=0.7\linewidth]{resources/w01-img/xkcd_cat_proximity.png}
\caption[]{[Cat Proximity (xkcd.com/231)](https://xkcd.com/231/).}
\label{catporx}
\end{figure}
```

<img src="resources/w01-img/xkcd_cat_proximity.png" width="80%" align="center">

.footnote[.square[[Cat Proximity (xkcd.com/231)](https://xkcd.com/231/). ]]
]]

]
---
class: right, top
background-image: url(resources/w01-img/general_purpose_map.jpg)

.split-40[.column[
].column[
### Map & Spatial Pattern
.bold.square[A topographic map showing the land, street networks, and boundary between Singapore and Malaysia (Johor).]

]]

---
class: left, middle
.split-30[.column[
### Map & Spatial Pattern
.bold.square[SMRT Locality map Chinese Garden Exit C, by [SMRT](http://journey.smrt.com.sg/journey/station_info/chinese-garden/map/)]

.red.bold[General purpose map] is mainly for wayfinding and navigation, as it displays .mark[a wide range of geographical features] such as roads, cities, rivers, and political boundaries.

This type of map aims to provide .mark[a comprehensive representation] of an area, allowing users to orient themselves and plan routes efficiently.

].column[.center[
<img src="resources/w01-img/SMRT_localitymap_Chinese_Garden.jpg" width="80%" align="center">
]]]

---
class: left, top
background-image: url(resources/w01-img/Snow-cholera-map-1.jpg)

.split-50[.column[
.box[
<h3 class="box-text"> Map & Spatial Pattern </h3>
<h5 class="box-text"> John Snow's 1854 Cholera Map: the distribution of cases and water pumps</h4>
]
].column[.justify[
.footnote-left.box2[.small.bold[John Snow's 1854 Cholera Map, see: [Wikipedia](https://en.wikipedia.org/wiki/File:Snow-cholera-map-1.jpg) for description.]]
]]]

---
class: left, top
background-image: url(resources/w01-img/clinic_flow_radiation.png)

.split-30[.column[
.box[
<h3 class="box-text"> Map & Spatial Pattern </h3>
<h5 class="box-text"> A flow map of estimated urban movement for accessing clinics.</h4>
]
].column[
.footnote-left.box2[[Interactive map on FlowMap.gl](https://app.flowmap.city/public/67249d1d-4c21-40e3-8ddb-fd5124907c99)]
]]

---
class: left, middle

.split-20[.column[
### Spatial Patterns

].column[.justify[

A .red.bold[thematic map] (e.g., John Snow's map and urban movement map) is a visual representation of a specific theme, subject, or data attribute that emphasizes .red.bold[spatial patterns], relationships, or trends within a geographical area.

Through the use of various .red[symbols, colors, or shading], thematic maps visually illustrate the spatial arrangement and distribution of features, revealing the relationships, trends, or correlations that constitute spatial patterns.

Spatial pattern encompasses the way elements are organized, positioned, or clustered in a particular space. By analyzing spatial patterns, researchers can gain valuable insights into underlying processes, trends, or correlations in diverse fields, including geography, ecology, urban planning, and epidemiology.


.xkcd[A .red[map] is a tool for .red[storytelling] and a medium for .red[communication].
.red[Spatial patterns] are the .red[information and insight] we can observe from a (thematic) map.]
]]]

---
class: left, middle

.split-60[.column[
### Geospatial Visualization Patterns

].column[

- Point pattern
- Areal pattern
- Statistical pattern

]]

---
class: left, middle

.split-30[.column[
### Geospatial Visualization Patterns

- .red[Point pattern]
- .grey[Areal pattern]
- .grey[Statistical pattern]

].column[
<img src="resources/w01-img/point-hdb_resaleprice.png" width="100%" align="center">
.footnote-right.square[The highest and lowest price of 10 yo, 4-room HDB flat in 2023.]

]]

---
class: left, top

.split-30[.column[
### Geospatial Visualization Patterns
].column[
- .grey[Point pattern]
- .red[Areal pattern]
- .grey[Statistical pattern]
]]
<img src="resources/w01-img/areal-education_level-b.png" width="100%" align="center">
.footnote.square[Education level by Planning Area.]

---
class: left, middle

.split-30[.column[
### Geospatial Visualization Patterns

- .grey[Point pattern]
- .grey[Areal pattern]
- .red[Statistical pattern]

].column[
<img src="resources/w01-img/stat-subzone_bus_flow.png" width="80%" align="center">

.footnote.square[Subzone-to-subzone daily flow ridership.]
]]

---
class: center, middle

### Why visualization?
<img src="resources/w01-img/drawing_compare_data_info-b.png" width="100%" align="center">
.square[Data vs. Information]


---
class: center, top

### Why visualization?
<img src="resources/w01-img/drawing-data_info_insight.png" width="80%" align="center">

.square[Data, Information, Insights.]

---
class: left, middle

.split-30[.column[
### Why visualization?

Data, Information, Insights

].column[
- .bold.red[Data]:
.red[Raw facts, figures, or observations collected and recorded] in various forms, such as text, numbers, or images.
Data is the basic building block for understanding and analyzing phenomena or trends.
- .bold.red[Information]:
.red[Organized, structured, and processed data] that provides context and meaning, making it useful and relevant to specific users or situations.
Information helps answer questions and guide decision-making.
- .bold.red[Insights]:
.red[Deep, meaningful conclusions and understanding] derived from analyzing and interpreting information.
Insights uncover patterns, trends, or cause-and-effect relationships, enabling informed decisions and new perspectives.

]]

---
class: left, top

.split-30[.column[
### Why visualisation?
Geovisualisation is a series of explorations and analyses, that includes using various techniques and methods, e.g., thematic mapping, exploratory spatial data analysis, to uncover the underlying patterns, to get better understanding of geographical phenomena.
].column[
<img src="resources/w01-img/drawing-how_maps_are_used.png" width="100%" align="center">
.square[MacEachren's cartographic cube.]

.xkcd[What are the common steps for data visualisation?]
]]

---
class: center, middle

### The Key Steps of Data Visualisation: .red[OTAS]

<img src="resources/w01-img/otas_01.png" width="40%" align="center">

---
class: left, middle

.split-30[.column[
### OTAS
- .red[Observe]
- .grey[Think]
- .grey[Assess]
- .grey[Show]

].column[
### Observe 


- .red[What can be SEEN？]
- Ensure you understand the .blue.bold[metadata].
- Look into the data.
- Get your hand dirty: .blue.bold[Create relevant plots or maps] using the data.
	- whatever plots/maps that you can think of, sky is the limit
- Look at those plots and maps...
- .red[Divergent thinking, brainstorming]

]]

---
class: left, middle

.split-30[.column[
### OTAS
- .grey[Observe]
- .red[Think]
- .grey[Assess]
- .grey[Show]
].column[
### Think

- .red[What are the CAUSES？]
- How does it look?
- Are there any .blue.bold[familiar] or .blue.bold[expected] patterns? (that you may have seen somewhere before)
- Is there anything looks .blue.bold[unusual and strange]? (something that really stands out)
	- Is there anything wrong?
- Are there any .blue.bold[unexpected] patterns? (something beyond your expectation)
	- unexpected patterns are usually the interesting one, if they are real
	- counter-intuitive
- What could be the .blue.bold[possible reasons] behind these patterns?
- .red[Expanding and synthesizing from the brainstorming step]

]]

---
class: left, middle

.split-30[.column[
### OTAS
- .grey[Observe]
- .grey[Think]
- .red[Assess]
- .grey[Show]
].column[
### Assess

- .red[How to VERIFY them?]
- Review and (re)evaluate your .blue.bold[initial ideas or thoughts], even if they seem .blue.bold[immature, unconventional, or funny].
- .blue.bold[Test your hypotheses or thoughts] to ensure their validity.
- Double-check for any possible .blue.bold[(stupid) mistakes] made during 
	- data processing, 
	- calculation, 
	- unit transformation, 
	- map projection, or 
	- visualization.
- .blue.bold[Literature review] for confirmation/contrasting the findings.
- .red[Convergent thinking, rigourously evaluating every idea]

]]

---
class: left, middle

.split-30[.column[
### Show
- .grey[Observe]
- .grey[Think]
- .grey[Assess]
- .red[Show]
].column[
### Show
- .red[How to VISUALISE them?]
- .blue.bold[(Re)Drawing] the plots & maps
- Think about the .blue.bold[layouts]
	- potrait, landscape
	- combining multiple subplots
	- sequences
	- colours
	- text font family, size, and positions
- .blue.bold[Show] it to people
- .blue.bold[Communicate] based on it
- Getting .blue.bold[feedbacks]

]]

---
class: center, middle

### OTAS Flow
<img src="resources/w01-img/otas_flow.png" width="70%" align="center">

---
class: left, middle

.split-20[.column[
### Summary
].column[

- There is .bold[no strict rules] for doing data visualisation
- The four OTAS steps are just a quick guideline for the .red["visual thinking process"]
	- Observe: divergent thinking & brainstorming
	- Think: extending & synthesing
	- Assess: convergent thinking & double checking
	- Show: presentation
- .red[Some people skip the Think and Assess] steps and jump from drawing initial plots/maps step to the last showing/communicating step. 
	- Their results could be bias, not comprehensively capture the thoughts

]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 2]
## Statistical Thinking
------
.square[The What question .dot[] The Why question]

.headnote.square.bold.x-large[Principles of Cartographic & Geospatial Visualization]

---
class: left, middle

.split-30[.column[
### Statistics?
What is statistics?

.xkcd[From .red[data] to .red[information].] 
].column[.justify[

The two main types of statistics:

1. **Descriptive Statistics** is about __how we describe data__. This branch focuses on summarizing and describing the main features of data, such as mean, median, standard deviation, and correlation. Descriptive statistics helps **visualize** and **interpret** data through graphical methods like histograms, scatter plots, box plots, and maps.

2. **Inferential Statistics** is about __what we can learn from the data__. This branch involves drawing conclusions about a population based on a sample by using probability theory. Inferential statistics allows us to **make predictions**, **<u>test hypotheses</u>**, and **evaluate the reliability** of conclusions. Some common methods in inferential statistics include regression analysis, hypothesis testing, and confidence intervals.

]]
]

---
class: left, middle

.split-30[.column[
### Descriptive Statistics
The three types of measures in descriptive statistics
].column[

- **Measures of Central Tendency**: These measures provide an indication of the "center" or "middle" of a dataset. They include: mean, median, mode.
- **Measures of Spread** (Variability): These measures describe how spread out or dispersed the data is. They include: range, variance, standard deviation.
- **Measures of Shape**: These measures help characterize the shape or distribution of the data, including: skewness, kurtosis.

]]

---
class: left, middle

.split-30[.column[
### Descriptive Statistics
- **Measures of Central Tendency** .red[help us understand the central or 'average' values in a dataset.]
- .grey[Measures of Spread]
- .grey[Measures of Shape]
].column[.justify[

<img src="resources/w01-img/measures_central.png" width="100%" align="center">
.square[The means of the three IRIS species.]

]]
]

---
class: left, middle

.split-30[.column[
### Descriptive Statistics
- .grey[Measures of Central Tendency]
- **Measures of Spread** .red[(variability) describe how the data is spread or dispersed around the central values.]
- .grey[Measures of Shape]
].column[.justify[

<img src="resources/w01-img/measures_spread.png" width="100%" align="center">
.square[The spread of the three IRIS species.]

]]
]

---
class: left, middle

.split-30[.column[
### Descriptive Statistics
- .grey[Measures of Central Tendency]
- .grey[Measures of Spread]
- **Measures of Shape** .red[describe the shape of the distribution, which could be steep/flat, skewed, or non-normal.]
].column[.justify[

<img src="resources/w01-img/measures_shapes.png" width="100%" align="center">
.square[The skewness and kurtosis of the three IRIS species.]

]]
]

---
class: left, middle

.split-30[.column[
### Inferential Statistics

].column[
- **Analysis of Relationship**:
How one variable is related to another? How a series of independent variables could be related to one of the dependent variables?
- **Analysis of Differences**:
Are them significantly different?
- **Analysis of Confidence**:
How confident are we about the sampling result?
]]

---
class: left, middle

.split-40[.column[
### Inferential Statistics
- **Analysis of Relationship**:
Assessing .red[the strength and direction of associations between variables]. Examples include .red[correlation] (Pearson's r for parametric data and Spearman's rho for non-parametric data), and .red[regression analysis] (linear, multiple, and logistic regression). These output could further be used for further analysis and predictions.
- .grey[Analysis of Differences]
- .grey[Analysis of Confidence]
].column[.justify[

<img src="resources/w01-img/analysis_correlation.png" width="80%" align="center">  
.square[The relationships between petal length and petal weight for the three IRIS species.]

]]
]

---
class: left, middle

.split-40[.column[
### Inferential Statistics
- .grey[Analysis of Relationship]
- **Analysis of Differences**:
Evaluating whether observed .red[differences between groups or conditions are statistically significant]. Hypothesis testing forms the foundation for these measures. .red[Parametric tests], such as t-tests and ANOVA, are used when data meets certain assumptions (e.g., normality). .red[Non-parametric tests], such as Mann-Whitney U test, Wilcoxon signed-rank test, and Kruskal-Wallis test, are used when assumptions are violated or with non-normal data.
- .grey[Analysis of Confidence]
].column[.justify[

<img src="resources/w01-img/analysis_differences-b.png" width="90%" align="center">  
.square[The differences in petal length between the three species.]

]]
]

---
class: left, middle

.split-40[.column[
### Inferential Statistics
- .grey[Analysis of Relationship]
- .grey[Analysis of Differences]
- **Analysis of Confidence**:
Provide insights into the .red[reliability and generalizability] of statistical findings. Estimation involves calculating point estimates and confidence intervals to infer .red[population] parameters. .red[Sampling distributions] and standard errors help quantify the variability of sample statistics. Statistical power and effect size measures ensure that studies have adequate sample sizes and detect meaningful effects.
].column[.justify[

<img src="resources/w01-img/analysis_confidence.png" width="90%" align="center">  
.square[The confidence interval (CI) of the actual population mean could fall within the 95% CI.]

]]
]

---
class: left, middle

.split-20[.column[
### Summary
Thinking .red[Statistically] while doing .red[Geospatial Visualization]
].column[.justify[
- Measures of **Central Tendency & Spreads**: .red[Spatial Aggregation]---
What is the median resale price of HDB flats in each district?

- Measures of **Shape**: .red[Data Categorization]---
Which data breaking scheme is more appropriate for mapping the variable?
Is data transformation needed?

- Analysis of **Relationship**: .red[Spatial Interaction]---
Is mental wellness related to the distribution of greenery?
Can Socio-Economic Status be explained or predicted by the distribution of various types of POIs and property prices?

- Analysis of **Differences**: .red[Spatial Patterns]---
Are there significant clusters of crime cases in the study area?
Are the spatial patterns of university-level and secondary-school-level residences different from each other?

- Analysis of **Confidence**: .red[Samples vs. Population]---
Is the sample data representative of the population?

.footnote.xkcd[These are some of the key concerns when we are reading/mapping a spatial pattern.]
]]
]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 3]
## Key Components of Maps
------

.square[Sizes .dot[] Typography .dot[] Colors .dot[] Coordinate System .dot[] Arrangement]

.headnote.square.bold.x-large[Principles of Cartographic & Geospatial Visualization]

---
class: left, middle

.split-50[.column[
### Key Components of Maps

].column[.justify[
- Sizes
- Typography
- Colors
- Coordinate System
- Arrangement
]]
]

---
class: left, middle

.split-30[.column[
### Sizes
- .red[Sizes]
- .grey[Typography]
- .grey[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

].column[.justify[

#### The size of the map:
- a 'full' width figure in an A4 paper (e.g., thesis, reports)
- a 'half' width figure in an A4 paper
(i.e., to fit in one column of a two columns layout)
- as one of the element inside an A1 poster
- a full A0 poster-size map
- in a Powerpoint slide (full-page vs. as an element)

]]
]

---
class: left, middle

.split-30[.column[
### Sizes
- .red[Sizes]
- .grey[Typography]
- .grey[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

].column[.justify[
.bold[Map details].
How much detail can be shown in:
- a small A4-one-column map
- a full A0 poster-size map

Two thinking directions:
- What should be added --- the 'plus'
- What should be removed --- the 'minus'

]]
]

---
class: left, middle

.split-30[.column[
### Sizes
- .red[Sizes]
- .grey[Typography]
- .grey[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

].column[.justify[

.bold[DPI] (dots-per-inch): the number of dots that will be drawn or printed within a one-inch span (in a single dimension).

.xkcd.red[Think:]
- .xkcd[What happens when you put an A0-size map/image inside an A4 paper?]
- .xkcd[How does a 2cm line in the original A0 map look on the A4 paper?]


]]
]

---
class: left, middle

.split-30[.column[
### Sizes
- .red[Sizes]
- .grey[Typography]
- .grey[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

.red[Take home message:
Always plan ahead about what size of map to be drawn.]
].column[.justify[

<img src="resources/w01-img/drawing_sizes_1a.png" width="100%" align="center">  
.square[The same map export with different size, squeezed to the same display size. ]

]]
]

---
class: left, middle

.split-30[.column[
### Sizes
- .red[Sizes]
- .grey[Typography]
- .grey[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

.red[Take home message:
Always plan ahead about what size of map to be drawn.]
].column[.justify[

<img src="resources/w01-img/drawing_sizes_1b.png" width="100%" align="center">  
.square[The same 4 maps, zoomed-in. ]

]]
]

---
class: left, middle

.split-30[.column[
### Typography
- .grey[Sizes]
- .red[Typography]
- .grey[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

].column[.justify[
Typography most often serves to label cartographic elements.
It is a .red.bold[“functional symbol”] primarily, and secondarily an .underline[aesthetic element​] meaning that .underline[it carries cartographic meaning​] and .red.bold[is not simply “window dressing”].
.footnote-right[[.square[(Typography, from Making Effective Maps: Cartographic Visualization for GIS)]](https://colorado.pressbooks.pub/makingmaps/chapter/typography/)]

- Font Family (Serif, Sans-Serif, Decorative, Monospaced)
- Font Size (relative to map size)
- Font Weight (Bold (700) vs. Regular (400) vs. Light (300))
- Font style (italic vs. regular)
- Uppercase, lowercase, title case

]]
]

---
class: left, middle

.split-30[.column[
### Typography
- .grey[Sizes]
- .red[Typography]
- .grey[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

].column[.justify[

.xkcd[What is the differences between .red[Sans Serif] fonts and .red[Serif] fonts?]

<img src="resources/w01-img/drawing-fonts.png" width="90%" align="center">  
.square[Some example of Sans-Serif fonts (left) and Serif fonts (right). ]
]]
]

---
class: left, middle

.split-30[.column[
### Typography
- .grey[Sizes]
- .red[Typography]
- .grey[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

].column[.justify[

<img src="resources/w01-img/text_elements.png" width="70%" align="center">  
.square[Text elements. ]
]]
]



---
class: left, middle

.split-30[.column[
### Typography
- .grey[Sizes]
- .red[Typography]
- .grey[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

].column[.justify[
Things to be considered:
- .bold[Visibility]: make sure the labels can be viewed .red[without zoom-in].
- .bold[Hierarchy]: use different sizes, weights, or styles to show .red[hierarchy] of labels.
- .bold[Consistency]: use the same typeface to show labels in .red[the same level].
- .bold[License]: make sure the font can be used in your targeted publication or is there any restriction/subscription-needed
- .bold[Publication requirement]: some journal requested that some specific fonts should be used for some of the map elements.

.red[Take home message:
The top priority is to ensure that the text is .red[clear and readable]. Additionally, make sure the fonts are appropriate for your target venue. ]


]]
]

---
class: left, middle

.split-30[.column[
### Colors
- .grey[Sizes]
- .grey[Typography]
- .red[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

].column[.justify[
In the realm of cartography and geovisualization, color is an essential tool that serves to delineate different components and highlight their significance, thereby facilitating effective visual communication. In designing geovisualization, .red.bold[the application of color goes beyond aesthetics, as it enables the clear differentiation of features and allows for the accurate representation of data], making it a crucial aspect of geovisualization design.

]]
]

---
class: right, top
background-image: url(resources/w01-img/US_temperature_map.png)

<div class="box">
<h3 class="box-text"> Temperature of colors </h3>
</div>


.footnote.square[.bold[NASA Earth Observatory: [Arctic Chill Sweeps U.S.](https://earthobservatory.nasa.gov/images/152333/arctic-chill-sweeps-us)]]



---
class: left, middle

.split-30[.column[
### Colors
- .grey[Sizes]
- .grey[Typography]
- .red[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

].column[.justify[

Things to considered while selecting color(s):
- The targeted  audiences or venues: color or black and white (and grey)?, colorblind? etc....
- Types of values:
    - Qualitative/Categorical
    - Quantitative/Sequential:
        - discrete: Q1, Q2, Q3, Q4; levels after 'breaks'; age groups...
        - continuous: scaled data from 0 to 1, with a min-value and max-value, exact age...
    - Diverging: with a center value (e.g., 0)
    -  <img src="resources/w01-img/drawing_continuous_discrete.png" width="40%" align="center">  
    Discrete vs. Continuous.

]]
]


---
class: left, middle

.split-30[.column[
### Colors
- .grey[Sizes]
- .grey[Typography]
- .red[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

].column[.justify[

Things to considered while selecting color(s):
- Temperature of colors:
    - cold colors for low values,
    - hot colors for high values, etc.
    - <img src="resources/w01-img/temperature-of-greys.png" width="40%" align="center">  
    [Color temperature](https://en.wikipedia.org/wiki/Color_temperature) from Wikipedia.
- The meaning of data:
    - green-series colors for greeneries level, or safety level, etc.
    - red, orange colors for dangerous level, or warning level...

]]
]

---
class: left, middle

.split-30[.column[
### Colors
- .grey[Sizes]
- .grey[Typography]
- .red[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

].column[.justify[

<img src="resources/w01-img/matplotlib-colors.png" width="100%" align="center">  
.square[Some example of colormaps from [Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html).]
]]
]

---
class: left, middle

.split-30[.column[
### Colors
- .grey[Sizes]
- .grey[Typography]
- .red[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

].column[.justify[

<img src="resources/w01-img/seaborn-qualitative.png" width="80%" align="center">  
.square[Various qualitative colormap from [Seaborn](https://seaborn.pydata.org/tutorial/color_palettes.html). ]
]]
]
---
class: left, middle

.split-30[.column[
### Colors
- .grey[Sizes]
- .grey[Typography]
- .red[Colors]
- .grey[Coordinate System]
- .grey[Arrangement]

].column[.justify[
Two basic color models:
- .bold[CMYK]: allows for more precise control over how colors appear on printed materials.
    - four integer values ranging from 0 to 100, each value corresponding to the percentage of ink coverage for Cyan, Magenta, Yellow, and blacK components.
- .bold[RGB]: allows for precise control over how colors appear on digital devices.
    - three integer values ranging from 0 to 255, each value corresponding to the intensity of the Red, Green, and Blue lights.

How to use colors in Python (Matplotlib):
- named colors: `'red'`, `'blue'`, `'green'`, `'white'`, [full list here](https://matplotlib.org/stable/gallery/color/named_colors.html)
- xkcd colors: `'xkcd:off white'`, [full list here](https://xkcd.com/color/rgb/)
- specifying R, G, & B in the ranging from 0 to 1 (divided by 255): `(0.1, 0.2, 0.5)`
- specifying R, G, B, & alpha in the ranging from 0 to 1 (alpha as proportion): `(0.1, 0.2, 0.5, 0.7)`
- specifying RGB hex code: `'#0f0f0f'`
- specifying RGBA hex code: `'#0f0f0fff'`
]]
]

---
class: left, middle

.split-30[.column[
### Coordinate System
- .grey[Sizes]
- .grey[Typography]
- .grey[Colors]
- .red[Coordinate System]
- .grey[Arrangement]

].column[.justify[
All maps are drawn with a specific coordinate reference system (CRS), which defines how the geographic coordinates of features on the Earth's surface are represented in a flat, two-dimensional plane (i.e., map). There are two main types of CRS: unprojected and projected.

1. **Unprojected CRS**

   - Uses latitude (N-S) and longitude (E-W) coordinates in degrees.
   - Represents Earth's curved surface.

2. **Projected CRS**

   - Transforms Earth's curved surface into a flat map (in length, e.g. meters).
   - Different types:
     - **Mercator**: Preserves angles and directions, used in navigation.
     - **Equal Area**: Preserves area, useful for spatial analysis.
     - **Conic**: Preserves shape and angles, used for mid-latitude regions.

   Each map projection serves different purposes and has its own advantages and disadvantages in terms of preserving shape, area, distance, and direction. The choice of projection depends on the specific needs and applications of the map.
]]
]

---
class: left, middle

.split-30[.column[
### Coordinate System
- .grey[Sizes]
- .grey[Typography]
- .grey[Colors]
- .red[Coordinate System]
- .grey[Arrangement]

].column[.justify[

<img src="resources/w01-img/morphing_map_project.png" width="100%" align="center">  
.square[Try and view the differences of various projections in [The Morphing Map Project](https://wcchin.github.io/map_projection/). ]

]]
]


---
class: left, middle

.split-30[.column[
### Coordinate System
- .grey[Sizes]
- .grey[Typography]
- .grey[Colors]
- .red[Coordinate System]
- .grey[Arrangement]

].column[.justify[

<img src="resources/w01-img/varying_projections.png" width="60%" align="center">  
.square[The four countries in three different projections. ]


]]
]


---
class: left, middle

.split-30[.column[
### Coordinate System
- .grey[Sizes]
- .grey[Typography]
- .grey[Colors]
- .red[Coordinate System]
- .grey[Arrangement]

].column[.justify[
#### How to use CRS in Python

```python
import geopandas as gpd
# read the file
singapore = gpd.read_file('../path_to_file/singapore.shp')
print(singapore.crs)  # to show the projection info from the saved file

# use .to_crs() to convert between projections, usually from or to EPSG:4326

# check EPSG.io website, 3414 is the code for SVY21 / Singapore TM,
# TM means Transverse Mercator, see https://epsg.io/3414 for details
sg_prjd = singapore.to_crs('epsg:3414')
# OR
## find the targeted crs string, something look like this:
targeted_crs = '+proj=tmerc +lat_0=1.36666666666667 +lon_0=103.833333333333 +k=1 +x_0=28001.642 +y_0=38744.572 +ellps=WGS84 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs +type=crs'
sg_prjd = singapore.to_crs(targeted_crs)

```


]]
]


---
class: left, middle

.split-30[.column[
### Arrangement
- .grey[Sizes]
- .grey[Typography]
- .grey[Colors]
- .grey[Coordinate System]
- .red[Arrangement]

].column[.justify[

- .bold[Arrangement] is about the position of every element on map.
    - Where to put what
- .bold[Which area] of a map/paper will be seen first by the readers?
    - The hierarchy of information
- Should we draw .bold[North arrow and scale bar]?
    - If it is a series of maps, the second and later maps could ignore the N-arrow and scale bar, for the sake of simplicity and readability.
- Collective/shared .bold[legend], or separate legends for every map?
    - In a multi-subplots layout setting, the elements in the legend are usually same, so that the colors/sizes could be compared between subplots---in this case, one large shared legend is sufficient.
- Figure .bold[title]
    - Do we need one for a map that would be placed in a report/thesis?
    - It is a common practice that if the map comes with a figure caption (e.g., Fig X. figure title) then the title on top of the map should be removed.
- The .bold[external (out-of-studying-scope) area]
    - It is a better idea to draw these external area with light grey or something less attractive.
    ]]
    ]


---
class: left, middle

.split-30[.column[
### Summary
Basics of mapping

].column[.justify[
Things to be considered and planned while visualizing spatial patterns:
- .bold.red[Sizes]: The sizes of maps and each individual element (line width, point size, etc.) in a static image affect the visibility and aesthetics of the visualization.
- .bold.red[Typography]: The visibility of text is the top priority.
- .bold.red[Colors]: Consider the color temperature, relation to the subject, targeted venue, etc.
- .bold.red[Coordinate System]: Choose a commonly used and suitable projection for the targeted area.
- .bold.red[Arrangement]: Carefully consider the hierarchy of information and the placement of various elements in the map or visualization.
]]
]

---
class: center, middle, inverse

## Closing Remarks
------

.square[House rules .dot[] Spatial Thinking .dot[] Statistical Thinking .dot[] Mapping]

.headnote.square.bold.x-large[Principles of Cartographic & Geospatial Visualization]

---
class: left, middle

### What we have talked about
- Maps and Scientific Visualisation
	- Think Spatially
	- OTAS visual thinking and steps
- Statistics
	- Think Statistically
	- Descriptive
	- Inferential
- Cartography
	- Basic but important things to always keep in mind when producing the outputs


---
class: center, middle

.bold[How to observe and describe these .bold.red[spatial] patterns .bold.red[statistically]?]

<img src="resources/w01-img/three_point_data.png" width="100%" align="center">
.square[Three sets of point patterns. ]

---
class: left, middle

### Learning Reflection Questions
- What are the 1-3 most important things you have learned from today's lecture?

- Were there any parts of today's lecture that you were already familiar with from your previous studies or related to your previous works? Please provide a brief description. 

- What things of today's lecture were unclear or not fully understood?

.red[Submit by the next day.]

.blue[Just write some simple responses. There is no 'correct' answer. ]

.xkcd[I expect to receive at least 10 reflection sheets from each of you for the semester.]
