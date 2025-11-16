slide_title: Geovisualisation I: Geospatial Data Storytelling 
custom_css: ../../remarkjs/Catppuccin.css
aspect_ratio: 16:9
remarkjs_path: ../../remarkjs/remark-0.15.0.js
use_mathjax: true
use_mermaid: false
add_sidebar: true
add_searchbar: true
use_click: false
use_scroll: false

name: inverse
layout: true
class: center, middle, inverse
---

## Geovisualisation I: Geospatial Data Storytelling
------

<br />

.x-large.bold[Dr. CHIN Wei Chien Benny]  
[.underline.square[wcchin@nus.edu.sg]]  

.headnote.square.bold.x-large[GE5230 Geospatial Statistics and Visualization]
.footnote.square[11 @ 2025-10-30 Department of Geography, NUS]

---
layout: false
class: center, middle


<img src="resources/w11-img/recap-overall.drawio.png" width="100%" align="center">

---
class: left, middle
## Objectives of this lecture
- Key aspects in Geospatial Data Storytelling
- Main considerations about designing a map
- An example

---
class: center, middle, inverse

.xx-large.bold.wide[PART 1]
## Geospatial Data Storytelling
------
.square[Definition .dot[] Designing .dot[] Considerations ]

.headnote.square.bold.x-large[Geovisualisation I]

---
class: left, middle
.split-40[.column[
### The Data-Driven World
].column[
In today's world, 
- data is everywhere and anytime
- everyone is using data
    - make informed decisions
    - drive innovation
    - improve outcomes
- .red[the true value of data lies not only in its collection and analysis but also in its effective communication]

.xkcd[This is where data storytelling plays a crucial role.]

]]

---
class: left, middle
.split-30[.column[
### What is Data Storytelling?
#### Definition
].column[
- Data storytelling is the process of .red[transforming complex data into engaging and easy-to-understand narratives], allowing audiences to quickly .red[grasp insights and take action]. 
- Data storytelling  combines .red[data, visuals, narrative and interactivity] to create compelling stories that resonate with people, regardless of their background or expertise. 

]]

---
class: left, middle
.split-30[.column[
### Data Storytelling 
#### Benefits
].column[
Data storytelling can help:
- .bold[Improved Decision-Making]: Data storytelling enables decision-makers to comprehend complex information quickly, leading to more informed choices and better outcomes.
- .bold[Wider Audience Reach]: By making data more accessible and engaging, data storytelling helps reach a broader audience, fostering collaboration and driving change.
- .bold[Greater Engagement]: Stories tap into human emotions and experiences, making data more relatable and memorable. This increased engagement leads to better retention and understanding of key insights.
- .bold[Increased Trust and Credibility]: Clear and transparent data storytelling builds trust and credibility, helping stakeholders feel confident in the validity of the insights presented.
- .bold[Problem-Solving and Innovation]: By revealing hidden patterns and relationships, data storytelling fosters problem-solving, innovation, and the development of new strategies.

]]

---
class: left, middle
.split-40[.column[
### Geospatial Data Storytelling 
#### Definition
].column[

Geospatial data storytelling is the art of combining .red[geographic data, visualizations, and compelling narratives] to communicate insights and patterns within a spatial context. It involves the use of .red[maps, spatial relationships, and location-based data] to create engaging and informative stories that help audiences understand .red[complex geographic phenomena] and make informed decisions.

]]

---
layout: false
class: center, middle


<img src="resources/w11-img/geospatial-data-storytelling.png" width="50%" align="center">

---
class: left, middle
.split-20[.column[
### Geospatial Data Storytelling
#### Key characteristics
].column[

- .bold[Geographic Data]: Geospatial data storytelling relies on geographic data, which includes any information associated with a specific location. This data can be either .red[vector] (e.g., points, lines, and polygons) or .red[raster] (e.g., aerial imagery and satellite data) and often includes attributes that describe the features' characteristics.

- .bold[Locations & Maps]: Maps are a central component of geospatial data storytelling, serving as the canvas on which data is visualized and stories are told. They provide a .red[spatial context for the narrative], helping audiences understand the relative location, distribution, and relationships between various geographic features.

- .bold[Spatial Relationships]: A key aspect of geospatial data storytelling is the focus on spatial relationships, such as .red[proximity, connectivity, and overlap between geographic features]. These relationships can reveal patterns and trends that would otherwise be difficult to identify, enabling more informed decision-making.
]]

---
class: left, middle
.split-20[.column[
### Geospatial Data Storytelling
#### Key characteristics
].column[
- .bold[Temporal Trends]: In addition to spatial relationships, geospatial data storytelling often incorporates temporal analysis, exploring .red[how geographic patterns and relationships change over time]. This can provide valuable insights into past trends and help predict future outcomes.

- .bold[Audience Engagement]: Geospatial data storytelling can incorporate .red[multimedia] elements like images, videos, and .red[interactive] features to create a more engaging and immersive experience for the audience. Interactive maps and visualizations encourage exploration and enable users to discover insights tailored to their interests.

]]

---
class: left, middle
.split-30[.column[
### Key Elements of a Successful Data Story
A successful data story engages .red[the audience, effectively communicates insights, and drives action]. 

].column[

- .bold[Clear Objective]  
A well-defined objective ensures that the data story stays focused and addresses the intended goals. The objective should be aligned with the audience's interests and needs.

- .bold[Targeted Audience]  
Tailor the data story to the audience's level of expertise, interests, and expectations. Consider their needs and the actions you want them to take after engaging with the story.

- .bold[Strong Narrative]  
A strong narrative weaves together data, visuals, and text to create a cohesive and engaging story. Utilize storytelling techniques like conflict, resolution, and character development to make the narrative more compelling.

- .bold[Informative and Relevant Data]  
Select data that is accurate, relevant, and supportive of the narrative. Ensure that the data insights are clearly communicated through appropriate visualizations and context.

]]

---
class: left, middle
.split-30[.column[
### Key Elements of a Successful Data Story
.grey[A successful data story engages the audience, effectively communicates insights, and drives action.] 

A successful data story combines these elements to create a .red[compelling narrative] that informs, engages, and drives change. 
By focusing on .red[the audience], using strong visuals, and providing clear insights, data storytellers can maximize the impact of their work.

].column[
- .bold[Effective Visualizations]  
Choose the most suitable visualizations to represent the data, and ensure they are easy to understand, visually appealing, and consistent in design.

- .bold[Context and Perspective]  
Provide context for the data, explaining its relevance, source, and limitations. Incorporate diverse perspectives to create a balanced and comprehensive narrative.

- .bold[Interactivity and Exploration]  
Enable the audience to interact with the data and explore it on their terms, enhancing engagement and understanding.

- .bold[Clear and Actionable Insights]: Present insights that are easy to grasp and provide clear recommendations for action or further investigation.

- .bold[Concluding Remarks and Next Steps]  
Wrap up the data story with a summary of key points, implications, and suggested next steps. This helps reinforce the main message and encourages the audience to take action.


]]

---
class: left, middle
.split-30[.column[
### Knowing Your Audience

Understanding the audience and their needs is crucial in data storytelling, as it enables the creation of impactful and engaging narratives that resonate with the intended recipients. 

].column[

- .bold[Tailored Content]  
By understanding the audience's interests, background, and expectations, you can select and .red[prioritize data insights that are most relevant to them]. Tailoring the content to their needs increases engagement and ensures the message is more likely to be heard and acted upon.

- .bold[Appropriate Complexity]  
Knowing your audience's .red[level of expertise] allows you to present data and insights with the appropriate level of complexity. This ensures that .red[the audience can understand and engage with the content] without feeling overwhelmed or bored.

- .bold[Effective Communication]  
Adjusting the .red[tone, language, and structure] of your data story to suit the audience's preferences improves communication and comprehension. This helps establish a connection with the audience and makes the narrative more relatable and engaging.

]]

---
class: left, middle
.split-30[.column[
### Knowing Your Audience

.grey[Understanding the audience and their needs is crucial in data storytelling, as it enables the creation of impactful and engaging narratives that resonate with the intended recipients.]

Understanding your audience and their needs is a fundamental aspect of effective data storytelling. By tailoring content, addressing specific interests, and presenting insights in a relatable manner, you can create powerful narratives that resonate with the audience and inspire action.

].column[

- .bold[Addressing Pain Points and Objectives]  
By understanding .red[the challenges and goals] of your audience, you can frame the data story in a way that demonstrates how the insights can address .red[their specific needs or objectives]. This increases the likelihood that the audience will find the story valuable and act on the information provided.

- .bold[Building Trust and Credibility]  
Tailoring the data story to the audience's needs and preferences shows that you understand and care about their interests. This helps build trust and establishes your credibility .red[as a reliable source of information].

- .bold[Encouraging Action]  
Knowing your audience's motivations and barriers to action allows you to create a data story that .red[encourages them to take the desired next steps]. By addressing potential objections or concerns, you increase the chances of your story driving meaningful change.
]]


---
layout: false
class: center, middle
### Key Components of a Compelling Data Story

<img src="resources/w11-img/compelling-data-story.png" width="60%" align="center">

---
class: left, middle
.split-30[.column[
### Key Components of a Compelling Data Story
A successful data story engages the audience, communicates insights effectively, and inspires action. Here are the essential elements that contribute to a powerful data story:

].column[
- .bold[Clear Structure]  
A well-structured data story has a .red[logical flow], guiding the audience through the narrative. It typically includes an introduction, rising action, climax, and resolution, mirroring the elements of traditional storytelling.

- .bold[Compelling Characters]  
Characters in a data story can be .red[individuals, groups, or entities] that are central to the narrative. By showcasing their experiences, challenges, and transformations, you create a relatable and engaging story that humanizes the data.

- .bold[Conflict]  
A compelling data story presents a .red[problem or challenge] that needs to be addressed. This conflict generates .red[tension and curiosity], encouraging the audience to continue exploring the narrative to discover potential solutions or insights.
]]

---
class: left, middle
.split-30[.column[
### Key Components of a Compelling Data Story
A successful data story engages the audience, communicates insights effectively, and inspires action. Here are the essential elements that contribute to a powerful data story:

].column[
- .bold[Resolution] (as in for resolving the conflict) 
The resolution reveals .red[how the conflict is addressed or resolved], providing a sense of .red[closure and satisfaction] for the audience. This element should highlight the key insights and takeaways from the data story.

- .bold[Strong Theme]  
A strong theme ties together the various elements of the data story and communicates the overarching message or lesson. The theme should be relevant to the audience and provide .red[a clear takeaway] that encourages .red[reflection or action].

- .bold[Interactivity and Engagement]   
In the context of data storytelling, incorporating interactive elements and fostering engagement can elevate the overall impact of the story. 

]]

---
class: left, middle
.split-30[.column[
### Best Practices & Considerations

- .blue[Appropriate Visualization Methods]
- .blue[Clear and Consistent Symbolization]
- .blue[Avoid Clutter and Complexity]
- .blue[Provide Context]
- Visual Design Elements
- Interactivity
- Clear Labeling and Legends
- User Experience
- Accompany Visualizations with Narrative
- Be Transparent
].column[

- .bold[Choose Appropriate Visualization Methods]  
Select visualization methods that align with the nature of the data and the story you want to tell. Common geospatial visualizations include choropleth maps, heatmaps, dot density maps, and cartograms.

- .bold[Use Clear and Consistent Symbolization]  
Use colors, symbols, and patterns that effectively communicate the data without causing confusion. Stick to consistent symbolization throughout the visualization.

- .bold[Avoid Clutter and Complexity]  
Keep the visualization clean and uncluttered by avoiding unnecessary labels, icons, or details. Break down complex data into smaller, more manageable visualizations if needed.

- .bold[Provide Context]  
Include relevant contextual information such as scale, orientation, and neighboring geographic features to help the audience understand the spatial relationships and context.
]]

---
class: left, middle
.split-30[.column[
### Best Practices & Considerations

- Appropriate Visualization Methods
- Clear and Consistent Symbolization
- Avoid Clutter and Complexity
- Provide Context
- .blue[Visual Design Elements]
- .blue[Interactivity]
- .blue[Clear Labeling and Legends]
- User Experience
- Accompany Visualizations with Narrative
- Be Transparent
].column[

- .bold[Visual Design Elements]  
Choose color palettes that are visually appealing, accessible, and effectively communicate the data. Other design elements such as size, shapes, weights, styles should also be carefully considered. 

- .bold[Incorporate Interactivity]  
Utilize interactive elements (e.g., hover-over tooltips, zoom functions, or layer toggles) to enhance the audience's exploration and understanding of the visualization.

- .bold[Provide Clear Labeling and Legends]  
Ensure that all visualizations have clear titles, labels, and legends to help the audience interpret the data and understand the visualization's purpose.

]]

---
class: left, middle
.split-30[.column[
### Best Practices & Considerations

- Appropriate Visualization Methods
- Clear and Consistent Symbolization
- Avoid Clutter and Complexity
- Provide Context
- Visual Design Elements
- Interactivity
- Clear Labeling and Legends
- .blue[User/Reader Experience]
- .blue[Accompany Visualizations with Narrative]
- .blue[Be Transparent]
].column[

- .bold[Consider User/Reader Experience]:  
Design the visualization with the user/reader in mind, ensuring it is easy to navigate, understand, and interact with. Test the visualization with users to gather feedback and improve the design.

- .bold[Accompany Visualizations with Narrative]  
Use narrative elements to provide context, highlight key insights, and guide the audience through the data story.

- .bold[Be Transparent About Data Sources and Limitations]  
Clearly communicate the data source, accuracy, and any limitations to maintain transparency and credibility.


]]


---
class: center, middle, inverse

.xx-large.bold.wide[PART 2]
## The Map Layout and Visual Hierarchy
------
.square[Map elements .dot[] Visual Hierarchy]

.headnote.square.bold.x-large[Geovisualisation I]

---
class: center, middle

### Map Elements

<img src="resources/w11-img/map_elements_example.png" width="80%" align="center">

.footnote-right.small.square[[source: ESRI](https://mgimond.github.io/Spatial/good-map-making-tips.html)]

---
class: left, middle
.split-30[.column[
### Map Elements
].column[
- Title should be easily identifiable as the map’s title through its size and positioning. Sub-titles are best in a smaller type size.

- Legend is a graphic guide that should comprise symbols, including colours, styles and patterns, which are not necessarily familiar to or known by the reader. A well-designed map should involve minimal reference to the legend.

- Insets allow the cartographer to show areas at a more detailed scale or to reposition features that would have otherwise ‘fallen’ just off the sheet to make best use of the available page and keep the main mapping at the most appropriate scale. They may also include an overview of where the region is in a wider geographical context, known as a locator map.
]]
.footnote-right.small.square[[Layout, balance, and visual hierarchy in map design in "The Routledge Handbook of Mapping and Cartography"](https://www-taylorfrancis-com.libproxy1.nus.edu.sg/chapters/edit/10.4324/9781315736822-28/layout-balance-visual-hierarchy-map-design-christopher-wesson)]

---
class: left, middle

.split-30[.column[
### Map Elements
].column[
- Charts and figures are common to thematic maps showing geostatistical or geo-numerical data. They should be included only if they add weight to the message of the map. 

- North arrow or any other directional indicator is only required if the orientation is not obvious. Arrows with a clear and suitably long North-South line are easier to use than more decorative ones.

- Scalebar allows users to make measurements on the map and is a quick reference to size objects. It does not have to represent distance, for example it can represent travel time.

- Border is a line encasing the edges of the mapped area or a line framing the entire map layout. It is sometimes known as a neatline, a term also used for a finer border line that may form the outer part of a grid and may contain graticule intersections.
]]
.footnote-right.small.square[[Layout, balance, and visual hierarchy in map design in "The Routledge Handbook of Mapping and Cartography"](https://www-taylorfrancis-com.libproxy1.nus.edu.sg/chapters/edit/10.4324/9781315736822-28/layout-balance-visual-hierarchy-map-design-christopher-wesson)]

---
class: left, middle

.split-20[.column[
### Bad Map Example
.small[
- Legend color
- Legend range and numbers
- Location of source info
- North arrow (complicated)
- Scale bar (complicated and alignment)
- Inset map too large
- Info about the numbers
]
].column[
<img src="resources/w11-img/example_bad_map.jpg" width="90%" align="center">

.footnote-right.small.square[[source: Chapter 7 Good Map Making Tips](https://mgimond.github.io/Spatial/good-map-making-tips.html)]

]]

---
class: left, middle

.split-20[.column[
### Improved Map Example
.small[
- Replaced legend title with the description of the data column
- Simplified north arrow and scale bar
- Colours changed to divergent colormap, with the center value to be the median 
- Smaller inset map, better emphasized of main map
]
].column[
<img src="resources/w11-img/example_bad_map_improved.jpg" width="90%" align="center">

.footnote-right.small.square[[source: Chapter 7 Good Map Making Tips](https://mgimond.github.io/Spatial/good-map-making-tips.html)]

]]

---
class: center, middle

### Visual Hierarchy
------
About how people 'look' for information. 

---
class: center, middle

<img src="resources/w11-img/visual_hierarchy.png" width="90%" align="center">

.footnote.small.square[https://clay.global/blog/web-design-guide/visual-hierarchy-web-design]

---
class: center, middle

<img src="resources/w11-img/what-is-visual-hierarchy-in-web-design.jpg" width="90%" align="center">

.footnote.small.square[https://wpdean.com/what-is-visual-hierarchy-in-web-design/]

---
class: center, middle

### Size / Scale Hierarchy 
<img src="resources/w11-img/size_hierarchy.jpg" width="90%" align="center">

.footnote.small.square[https://admiral.digital/what-is-visual-hierarchy-and-why-is-it-important/]

---
class: center, middle

### Size / Scale Hierarchy 
<img src="resources/w11-img/Scale-organizes-content-by-size.png" width="90%" align="center">

.footnote.small.square[https://visme.co/blog/visual-hierarchy/]

---
class: center, middle

### Size / Scale Hierarchy 
<img src="resources/w11-img/Fonts-organize-design-01.png" width="90%" align="center">

.footnote.small.square[https://visme.co/blog/visual-hierarchy/]

---
class: left, middle
.split-30[.column[
### Colour
].column[
<img src="resources/w11-img/colour_order.png" width="90%" align="center">
]]

.footnote.small.square[https://clay.global/blog/web-design-guide/visual-hierarchy-web-design]

---
class: center, middle

### Colour
<img src="resources/w11-img/Color-and-contrast-draw-attention-and-create-harmony.png" width="90%" align="center">

.footnote.small.square[https://visme.co/blog/visual-hierarchy/]

---
class: center, middle

### Colour
.split-50[.column[
<img src="resources/w11-img/color_bad.png" width="100%" align="center">
].column[
<img src="resources/w11-img/color_improved.png" width="100%" align="center">
]]

.footnote.small.square[[Layout, balance, and visual hierarchy in map design in "The Routledge Handbook of Mapping and Cartography"](https://www.taylorfrancis.com/chapters/edit/10.4324/9781315736822-28/layout-balance-visual-hierarchy-map-design-christopher-wesson)]

---
class: center, middle

### Colour
<img src="resources/w11-img/different_color_mapbox.png" width="75%" align="center">

.footnote.small.square[[Screenshot from Mapbox Gallery, Community Templates](https://www.mapbox.com/gallery)]

---
class: center, middle
### Layout - How people read
<img src="resources/w11-img/uiux_read_pattern.png" width="90%" align="center">

.footnote.small.square[https://www.interaction-design.org/literature/topics/visual-hierarchy]

---
class: center, middle
### Layout - How people read
<img src="resources/w11-img/uiux_read_pattern2.png" width="70%" align="center">

.footnote-left.small.square[https://www.interaction-design.org/literature/topics/visual-hierarchy?srsltid=AfmBOopgpNcuvrThNqPlsGQEKeRgygYpwrRwQ2TpCL0EJ9K2v1OSIOl5]

---
class: center, middle
### Layout - Rule of Third
<img src="resources/w11-img/rule_of_third.png" width="70%" align="center">

.footnote.small.square[https://www.interaction-design.org/literature/article/the-rule-of-thirds-know-your-layout-sweet-spots]

---
class: center, middle
### Layout - Rule of Third
<img src="resources/w11-img/Greenland-Husky-Rule-of-Thirds.webp" width="70%" align="center">

.footnote.small.square[https://www.capturelandscapes.com/the-rule-of-thirds-explained/]

---
class: center, middle
### Layout - Rule of Third
<img src="resources/w11-img/image-5-ruleofthrid-min.jpg" width="70%" align="center">

.footnote-right.small.square[https://admiral.digital/what-is-visual-hierarchy-and-why-is-it-important/]

---
class: center, middle
.split-40[.column[
### Layout - Rule of Third

.footnote-left.small.square[https://www.artworkflowhq.com/resources/the-rule-of-thirds-in-graphic-design]

].column[
<img src="resources/w11-img/poster_rule_of_thirds.png" width="70%" align="center">

]]

---
class: center, middle
.split-40[.column[
### Layout - Rule of Third

.footnote-left.small.square[https://community.esri.com/t5/esri-training-blog/using-artistic-inspiration-for-cartographic/ba-p/903968]

].column[
<img src="resources/w11-img/rule_of_third_KevinsGinMapGRID.jpg" width="70%" align="center">

]]

---
class: center, middle
.split-40[.column[
### Layout - Rule of Third

.footnote-left.small.square[https://community.esri.com/t5/esri-training-blog/using-artistic-inspiration-for-cartographic/ba-p/903968]

].column[
<img src="resources/w11-img/processed-images/processed-image-5.png" width="70%" align="center">
]]

---
class: center, middle

<img src="resources/w11-img/processed-images/processed-image-6.png" width="90%" align="center">

[https://onlinephototools.com/image-tools/image-rule-of-thirds-grid-overlay-tool/]

---
class: center, middle

<img src="resources/w11-img/processed-images/processed-image-1.png" width="90%" align="center">

---
class: center, middle

<img src="resources/w11-img/processed-images/processed-image-3.png" width="90%" align="center">

---
class: center, middle

<img src="resources/w11-img/processed-images/processed-image-4.png" width="90%" align="center">

---
class: center, middle

<img src="resources/w11-img/processed-images/processed-image-2.png" width="70%" align="center">

---
class: center, middle

<img src="resources/w11-img/processed-images/processed-image-7.png" width="70%" align="center">

---
class: center, middle
### Layout - Common Ratio - Landscape

<img src="resources/w11-img/common_aspect_ratios.png" width="90%" align="center">

---
class: center, middle
### Layout - Common Ratio - Portrait

<img src="resources/w11-img/common_aspect_ratios2.png" width="55%" align="center">

---
class: center, middle

### Spacing - In Design
<img src="resources/w11-img/Space-provides-balance-emphasis-and-movement.png" width="90%" align="center">

.footnote.small.square[https://visme.co/blog/visual-hierarchy/]

---
class: center, middle

### Spacing - Definition
<img src="resources/w11-img/whitespace.jpg" width="90%" align="center">

.footnote.small.square[https://clay.global/blog/web-design-guide/visual-hierarchy-web-design]

---
class: center, middle

### Spacing - Definition
<img src="resources/w11-img/whitespace_google.png" width="90%" align="center">

.footnote.small.square[https://www.google.com/]

---
class: left, middle

.split-30[.column[
### Spacing - For Balance
].column[
<img src="resources/w11-img/design_balance.png" width="70%" align="center">
]]

.footnote-left.small.square[https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/design-principles-for-cartography]

---
class: center, middle

### Spacing - Example
<img src="resources/w11-img/whitespace_NASA_artic.png" width="65%" align="center">

.footnote.small.square[https://earthobservatory.nasa.gov/images/152333/arctic-chill-sweeps-us]

---
class: center, middle

### Spacing - Example
<img src="resources/w11-img/whitespace_OSM.png" width="80%" align="center">

.footnote-left.small.square[[A spatio-temporal analysis investigating completeness and inequalities of global urban building data in OpenStreetMap](https://www.nature.com/articles/s41467-023-39698-6)]


---
class: center, middle, inverse

.xx-large.bold.wide[PART 3]
## Tools and Resources
------
.square[]

.headnote.square.bold.x-large[Geovisualisation I]

---
class: left, middle
### Tools and Resources - Data Visualization Tools
.split-50[.column[
- .bold[Carto]: A location intelligence and data visualization platform for creating interactive maps and geospatial applications.

- .bold[Tableau]: A data visualization and storytelling tool that allows you to create interactive and engaging visualizations.

- .bold[Power BI]: A business analytics platform from Microsoft for creating data visualizations, reports, and interactive dashboards.

- .bold[QGIS]: A free and open-source GIS software that enables geospatial data visualization and analysis.

- .bold[ArcGIS Online]: A web-based GIS platform by Esri that enables users to create, share, and analyze geospatial data, maps, and apps.

].column[

- .bold[Mapbox]: A platform that offers customizable map designs tools to create interactive maps and location-based applications.

- .bold[Kepler.gl]: A geospatial data visualization tool that allows users to create large-scale visualizations for geospatial data exploration.

- .bold[Flowmap.gl]: A web-based tool designed for visualizing and exploring spatial interactions using animated flow maps.

- .bold[Plotly]: A versatile data library that can be used with various programming languages, offering a wide range of interactive charts, maps, and plots.

- .bold[Bokeh]: An interactive data visualization library for Python, providing elegant, concise construction of versatile graphics and interactive plots.

]]

---
class: left, middle
background-image: url(resources/w11-img/carto_webpage.png)

<h2 style="color: #ffffffff">Carto</h2>

.footnote-left[[Carto link](https://carto.com/)]

---
class: left, middle
background-image: url(resources/w11-img/mapbox_3D.png)

<h2 style="color: #00000090">Mapbox 3D buildings</h2>

.footnote[[Mapbox link](https://www.mapbox.com/)]

---
class: left, middle
background-image: url(resources/w11-img/kepler-gl.png)

<h2 style="color: #ffffff90">Kepler.gl demo</h2>

.footnote[[Kepler.gl link](https://kepler.gl/)]
.footnote-left[[Demo link](https://wcchin.github.io/sg_HDB_price_map/hdb_map_filter.html)]

---
class: left, top
background-image: url(resources/w11-img/flowmap-gl.png)

<h2 style="color: #ffffff90">Flowmap.gl demo</h2>

.footnote[[Flowmap.gl link](https://flowmap.gl/)]
.footnote-left[[Demo link](https://app.flowmap.city/public/67249d1d-4c21-40e3-8ddb-fd5124907c99)]

---
class: right, top
background-image: url(resources/w11-img/plotly_dash-2.png)

<h2 style="color: #ffffff90">Plot.ly Dash webpage</h2>

.footnote[[Plotly - Dash link](https://plotly.com/examples/)]

---
class: left, middle
background-image: url(resources/w11-img/bokeh_webpage.png)

<h2 style="color: #00000090">Bokeh webpage</h2>

.footnote[[Bokeh link](https://docs.bokeh.org/en/latest/)]

---
class: right, top
background-image: url(resources/w11-img/storymap-js_webpage.png)

<h2 style="color: #00000090">Storymap.js (Knight-lab) webpage</h2>

.footnote[[Storymap.js link](https://storymap.knightlab.com/#examples)]

---
class: left, bottom
background-image: url(resources/w11-img/odyssey-js_webpage.png)

<h2 style="color: #00000090">Odyssey.js (Cartodb) webpage</h2>

.footnote[[Odyssey.js link](https://cartodb.github.io/odyssey.js/)]

---

### Tools and Resources 
#### Programming Languages and Libraries
- Python: A popular programming language with libraries for data analysis, visualization, and mapping, such as Matplotlib, Seaborn, Bokeh, and Folium.

- R: A programming language designed for statistical computing and visualization, with packages like ggplot2 and leaflet for mapping and data visualization.

- JavaScript: A versatile programming language for building interactive web-based visualizations, with libraries such as D3.js and Leaflet.js.

#### Storytelling Resources
- "Storytelling with Data" by Cole Nussbaumer Knaflic: A book that provides practical tips and techniques for creating effective data stories.
- [The Pudding](https://pudding.cool/): A digital publication that uses data visualization and storytelling to explore a wide range of topics.
- [The Data Visualisation Catalogue](https://datavizcatalogue.com/): A comprehensive online resource showcasing various data visualization examples and use cases, offering guidance and inspiration for creating effective visualizations across diverse industries and applications.



---
class: center, middle, inverse

.xx-large.bold.wide[PART 4]
## An Example - The Healthcare Resource Accessibility
------
.square[Motivation .dot[] Flow Estimation .dot[] Mobility .dot[] Accessibility .dot[] Reflection ]

.headnote.square.bold.x-large[Geovisualisation I]

---
class: right, bottom
background-image: url(resources/w11-img/example-1-link.png)

<h2 style="color: #ffffff90">The Demonstration</h2>

.footnote[[the link](https://wcchin.github.io/sg_health_access/)]

---
class: left, middle
.split-20[.column[
### Motivation
#### Background
].column[
As one of the most densely populated countries in the world, .red[Singapore faces challenges in ensuring equal access to healthcare for all]. The high population density has increased the demand for healthcare services, putting strain on the country's medical infrastructure. 

Although clinics are located in every neighborhood, the quality and intensity of healthcare services vary in different parts of the city-state, leading to disparities in access. 

Additionally, healthcare services in different geographic areas may experience varying levels of demand, subsequently affecting their ability to provide high-quality care to patients. 

It is thus critical to assess the spatial distribution of the availability and accessibility of healthcare services. 
]]

---
class: left, middle
### Motivation
.split-50[.column[

#### Problem
The spatial distribution of the availability and accessibility of healthcare services requires more exploration and analysis. 

#### Audience
- Urban planners
- General Public

#### Data
- ISP Clinic locations
- Population distribution
- Road network
- Hexagons (800m size)

].column[

#### Solution
This project presents a framework to measure the healthcare intensity by combining two popular models: radiation models and 2-step floating catchment area (2SFCA).

#### Visualization
After the flows were estimated and healthcare intensity were calculated, we show the results below in 4 sections:
- Flow Estimation Map
- Movements between Planning Area
- Distribution of Travel Distances
- Service Intensity Map

]]

---
class: left, middle
.split-20[.column[
### Flow Estimation Map
Estimated flow using [radiation models](https://www.nature.com/articles/s41598-021-02109-1).

Static, simple, map using arrows to show directions and colors to show above or below median. 
].column[
<img src="resources/w11-img/network_flow_isp_clinic.png" width="90%" align="center">
]]

---
class: left, middle
.split-20[.column[
### Flow Estimation Map
Interactive map with the same data, using Flowmap.gl: [Link](https://app.flowmap.city/public/67249d1d-4c21-40e3-8ddb-fd5124907c99)
].column[
<img src="resources/w11-img/flowmap-gl.png" width="95%" align="center">
]]

---
class: left, middle
.split-20[.column[
### Flow Estimation Map
Aggregated flows by planning areas, visualize using Sankey graph (or Alluvial graph): [Interactive Link](https://wcchin.github.io/sg_health_access/interactive/holoviews_sankey_pln_flow.html)
].column[
<img src="resources/w11-img/sankey_flowmap-bokeh.png" width="85%" align="center">
]]

---
class: left, middle
.split-40[.column[
### Mobility
The frequency distribution of travel distance, grouped by regions: [Interactive Link](https://wcchin.github.io/sg_health_access/#histogram)
].column[
<img src="resources/w11-img/mobility-by-region.png" width="70%" align="center">
]]

---
class: left, middle
.split-20[.column[
### Accessibility Map

Accessibility to ISP Clinics estimated using [2SFCA](https://journals.sagepub.com/doi/10.1068/b29120). 
Hexagon shows the service provider intensity. Circle shows the accessibility. 

Interactive map: [Link](https://wcchin.github.io/sg_health_access/interactive/keplergl_accessibility_clinic.html)
].column[
<img src="resources/w11-img/accessibility-keplergl.png" width="90%" align="center">
]]

---
class: left, middle
.split-30[.column[
### Reflection
].column[
- .bold[What was done]: The visualizations show some maps and graphs to display the population mobility for accessing healthcare service (ISP Clinic). 

- .bold[Resolution]: For visualization purpose, the spatial units were set to 800m hexagon size, which could be too large for analyzing walkable neighborhoods (400m). 

- .bold[Lack of spatial]: How spatial autocorelation, heterogeneity, or other spatial interactions effects may exists are not discussed. 

- .bold[Far from pratical]: The analysis remains conceptual, and thus, further development is required before it can effectively inform practical policy-making.

- .bold[Other level of resource]: The visualization did not present the other level of healthcare resources, e.g., polyclinics and hospitals. Visualization for Comparison can be challenging. 
]]

---
class: center, middle, inverse

## Closing Remarks
------
.square[Storytelling .dot[] Visual Hierarchy .dot[] Tools and Resources.dot[] Healthcare Example]

.headnote.square.bold.x-large[Geovisualisation I]



