slide_title: Week 12 - Geovisualisation II: Geospatial Data Storytelling 
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

## Geovisualisation II: Geospatial Visualisation
------

<br />

.x-large.bold[Dr. CHIN Wei Chien Benny]  
[.underline.square[wcchin@nus.edu.sg]]  

.headnote.square.bold.x-large[GE5230 Geospatial Statistics and Visualization]
.footnote.square[12 @ 2025-11-06 Department of Geography, NUS]

---
layout: false
class: center, middle


<img src="resources/w11-img/recap-overall.drawio.png" width="100%" align="center">

---
class: left, middle
## Objectives of this lecture
- Spatial Database
- Geospatial Visualisation

---
class: center, middle, inverse

.xx-large.bold.wide[PART 1]
## Spatial Database
------
.square[Data Management .dot[] Spatial Database .dot[] Relational Database .dot[] Normalization]

.headnote.square.bold.x-large[Geovisualisation II]

---
class: left, middle
.split-20[.column[
### Why (do we need to talk about) Spatial Database
].column[
- .bold[Data Management and Organization]:  
Spatial databases play a crucial role in managing, storing, and querying .red[large volumes of geospatial data]. A solid understanding of spatial databases helps geovisualization professionals effectively organize and access data, ensuring efficient workflows and accurate analysis.

- .bold[Data Retrieval and Query Performance]:  
Geovisualization often involves working with complex spatial queries and data retrieval tasks. By discussing spatial databases, students can learn how to optimize these queries and improve performance, resulting in .red[faster and more efficient data retrieval] for visualization purposes.

- .bold[Data Quality and Consistency]:  
Spatial databases provide tools and techniques for maintaining data quality, consistency, and integrity. This knowledge is vital for geovisualization professionals, as .red[data quality directly impacts the accuracy and reliability of their visualizations].

- .bold[Data Analysis and Modeling]:  
Spatial databases support various geospatial analysis and modeling techniques, such as spatial statistics, spatial interpolation, and geostatistics. A strong foundation in spatial databases allows geovisualization professionals .red[to leverage these advanced methods and create more informative visualizations].

]]

---
class: left, middle
.split-50[.column[

### What is Data Management

#### How do you manage your photos?​​

- Most cellphones take nice photos​
    - Taking 3 photos a day will give you ~1,000 photos a year​
    - Taking a 5-day vacation would give you 200 photos​

- Ways to managing photos​
    - Leave them on the phone?​
    - Organize them into folders?​
    - Upload them to some cloud services?​

- Which method is the best?​
].column[
<img src="resources/w12-img/photographs.png" width="100%" align="center">

]]

---
class: center, middle

### What is Data Management

<img src="resources/w12-img/data_management.png" width="100%" align="center">

---
class: left, middle
.split-30[.column[
### Data Management
#### Definition (Oracle)​
].column[
- Data management is the practice of .red[collecting, keeping, and using] data securely, efficiently, and cost-effectively.​

- help people, organizations, and connected things​ 
    - optimize the use of data within the bounds of policy and regulation​ 
    - (use data to) enable data-driven decision-makings and take actions that maximize the benefit to the organisation​
]]

---
class: left, middle
.split-20[.column[
### Database Operations - CRUD​
].column[
- .bold[.red[C]reate]: The Create operation is used to add new records (or rows) to a database table. ​

- .bold[.red[R]ead]: The Read operation is used to retrieve or fetch existing records from a database table. ​

- .bold[.red[U]pdate]: The Update operation is used to modify existing records in a database table. ​

- .bold[.red[D]elete]: The Delete operation is used to remove existing records from a database table.​
]]

---
class: left, middle

### What is Spatial Database

.bold[Database]: an integrated set of data on a particular subject, which is often used to store, and organize data​

.bold[Spatial (Geographic) database]: database containing geographic data of a particular subject for a particular area​

<img src="resources/w12-img/spatial_database_simple.png" width="90%" align="center">

---
class: left, middle
### Characteristics of spatial database​

- Data is under .bold[centralized control​]
    - Can guarantee data sharing among different users and applications​
    - Different from file management in which files are dispersed​

- Data are .bold[independent​]
    - Database is independent of the application systems, and thus can be called by various application systems​

- .bold[Data redundancy] is small​
    - Avoid repetitive data storage​
    - Improve data usage efficiency

- Database has .bold[complex data model structure​]
    - The complex data model structure is used for data organization and data management​
    - Vital difference from file management​

- Database has the function of .bold[data protection​]
    - A password and permission for access must be set​

---
class: left, middle
### Database Management Systems (DBMS)​

- A system to .red[perform database operations] on tables​
    - CRUD (Create, Read, Update, Delete)​
    - providing a systematic way to store, organize, retrieve, and manipulate data.​

- It ensures data .red[consistency, integrity, and security] while enabling efficient access and data sharing among multiple users or applications.​

- A DBMS supports various database models and provides features like backup, recovery, and performance optimization for .red[effective data management].​

---
class: left, middle
.split-30[.column[
### Database Management Systems (DBMS) ​
].column[
- .bold[Persistence] across failures​ --- maintain a consistent system after failures – software, hardware, network failures, etc.​

- .bold[Concurrent] access to data​

- .bold[Scalability] to search on very large datasets (which do not fit inside main memories of computers)​

- .bold[Efficiency​]
]]

---
class: left, middle
.split-20[.column[
### DBMS clients​
].column[
- an .red[interface] between users and the DBMS ​

- allow users to .red[connect, access, and interact] with the database​

- a software package that .red[enables] people to build and manipulate a database​

- Examples:​
    - MySQL Workbench, 
    - pgAdmin
    - SQL Developer
    - Microsoft Access (dBase file)​
    - dBeaver
]]

---
class: left, middle
.split-30[.column[

### Relational Database​
].column[

- It is a collection of tables, also called .red[relations​]

- The tables are .red[connected to each other] by keys​

- A .red[primary key]: represents one or more attributes whose values can uniquely identify a record in a table​

- A .red[foreign key]: is one or more attributes that refer to a primary key in another table​
]]

---
class: left, middle
.split-50[.column[
### Primary key, Foreign key, Composite key​
- Typically, one column, the .red.bold[primary key,] contains the unique ID (identifier) of the described things, e.g., student IDs, social security numbers​

- This primary key column can exist in other tables to establish a relation, i.e., the .red.bold[foreign key​]

- A .red.bold[composite key] is typically generated by combining the values of two or more columns in a table,  
e.g., student ID + course ID​
].column[

<img src="resources/w12-img/keys.png" width="100%" align="center">

]]

---
class: left, middle
.split-50[.column[
### Logical relation types​
].column[
- One-to-one  
<img src="resources/w12-img/one-to-one-link.png" width="30%" align="center">

- One-to-many  
<img src="resources/w12-img/one-to-many-link.png" width="30%" align="center">

- Many-to-one  
<img src="resources/w12-img/many-to-one-link.png" width="30%" align="center">

- Many-to-many  
<img src="resources/w12-img/many-to-many-link.png" width="30%" align="center">
]]

---
class: center, middle

### Logical relation types​ - One-to-one <img src="resources/w12-img/one-to-one-link.png" width="20%" align="center">

Every entity on the left can connect to one and only one entity on the right​.

<img src="resources/w12-img/one-to-one-demo.png" width="80%" align="center">

---
class: center, middle

### Logical relation types​ - One-to-many <img src="resources/w12-img/one-to-many-link.png" width="20%" align="center">

Every entity on the left can connect to multiple entities on the right​.  
Every entity on the right can connect to one and only one entity on the left. 

<img src="resources/w12-img/one-to-many-demo.png" width="80%" align="center">

---
class: center, middle

### Logical relation types​ - Many-to-one <img src="resources/w12-img/many-to-one-link.png" width="20%" align="center">

Every entity on the left can connect to one and only one entity on the right​.  
Every entity on the right can connect to multiple entities on the left​. 

<img src="resources/w12-img/many-to-one-demo.png" width="80%" align="center">

---
class: center, middle

### Logical relation types​ - Many-to-many <img src="resources/w12-img/many-to-many-link.png" width="20%" align="center">

Every entity on the left can connect to multiple entities on the right.  
Every entity on the right can connect to multiple entities on the left​. 

<img src="resources/w12-img/many-to-many-demo.png" width="80%" align="center">

---
class: left, top
background-image: url(resources/w12-img/database_relational_demo.png)

### A database for food order 
### & delivery system​

---
class: left, middle
.split-30[.column[
### Advantages of Relational Database​
].column[
- Each table in the database can be prepared, maintained, and edited .red[separately from other tables]​
    - This is important as more (GIS) data are being recorded and added​

- The tables can remain separate until a query or an analysis requires that attribute data from different tables be .red[linked (joined) together], which is favorable to both data management and data processing.​
]]

---
class: left, middle
.split-30[.column[
### Normalization: Preparing a relational database​
].column[
- Normalization is the process of decomposition, taking a table with all the attribute data, and breaking it down into small tables while maintaining the necessary linkages between them​

- Objectives of normalization:​
    - To avoid redundant data​
    - To ensure that attribute data in separate tables can be maintained and updated separately and can be linked whenever necessary​
    - To facilitate a distributed database
]]

---
class: center, middle
### An original (unnormalized) table​

<img src="resources/w12-img/normalization_before.png" width="100%" align="center">

---
class: center, middle
### Normalization Step 0: Observation on the unnormalized table​

Database Normalization is mainly .red[to separate information from different types of entities to separated tables]. ​

<img src="resources/w12-img/normalization_observe.png" width="100%" align="center">

---
class: center, middle
### Normalization Step 1: Fill Missing Values

Step 1 fills the empty cells, and each cell has one value​  
But the problem of data redundancy has increased​​

<img src="resources/w12-img/normalization_missing_value.png" width="100%" align="center">

---
class: center, middle

### Normalization Step 2: Table Decomposition

<img src="resources/w12-img/normalization_decompose_1.png" width="100%" align="center">

---
class: center, middle

### Normalization Step 3: Table Decomposition again

<img src="resources/w12-img/normalization_decompose_2.png" width="100%" align="center">

---
class: center, middle

### Normalization: Done

<img src="resources/w12-img/normalization_after.png" width="100%" align="center">

---
class: center, middle

### Table join​
A join operation brings together two tables by using a common field or a primary key and a foreign key​.

<img src="resources/w12-img/table_join.png" width="70%" align="center">


---
class: left, middle

.split-40[.column[
### Table relate
- A relate operation temporarily connects two tables but keeps the tables physically separate​

- Does not append the data from one table to another​

- Three or more tables can be simultaneously connected​

- Support all relationships​

].column[
<img src="resources/w12-img/table_relate.png" width="90%" align="center">
]]

---
class: left, middle
### Comparison
.split-50[.column[
#### Join
- Combines data from two tables .red[into a single table or layer].​

- Most often used for one-to-one or many-to-one relationships.​

- .blue[Requires a common field in both tables.​]

- Creates a .red[static connection] between tables (updates are not synchronized).​

- Appended columns are editable, but .red[changes won't reflect in the original table].​
].column[
#### Relate
- Establishes a .red[temporary, dynamic connection] between two tables or layers without physically combining them.​

- Allows for one-to-one, one-to-many, and many-to-many relationships.​

- .blue[Requires a common field in both tables.​]

- Provides .red[real-time access] to related data (updates are reflected when accessing related information).​

- Allows for editing related data, but .red[changes in the target table won't be synchronized back] to the original related table.​

]]

---
class: center, bottom
background-image: url(resources/w12-img/google_map_demo.png)

<h2 style="color: #00000090">What about 'spatial' in spatial database?​</h2>

---
class: left, middle
.split-30[.column[
### What about 'spatial' in spatial database?​
].column[
- .bold[Location]:  
Spatial databases store and manage data with a geographical component, allowing users to associate locations with other attributes for enhanced analysis and visualization.​

- .bold[Proximity]:  
Spatial databases enable proximity analysis, facilitating the identification of nearby features, calculation of distances, and exploration of spatial relationships between various data points.​

- .bold[Direction]:  
With spatial databases, direction-based queries and navigation-based queries, enabling route planning, shortest path calculations, and network analysis to optimize movement and travel within spatial data contexts.​

.xkcd.red[Spatial is indeed special!]
]]

---
class: left, middle

### Spatial join​
A spatial join uses a spatial relationship to join two sets of spatial features and their attribute data​.

<img src="resources/w12-img/spatial_join.png" width="70%" align="center">

- (left) Join a school to a county in which the school is located
- (center) Join a highway to a forest area by which the highway is intersected​
- (right) Join a villages to a fault line which the village is closest to

---
class: left, middle

.split-30[.column[
### Example of spatial database
].column[
- PostgreSQL + PostGIS 

- Mysql + Spatial Extension

- SQLite + SpatiaLite

- DuckDB + Spatial Extension

- MongoDB

- CrateDB

.xkcd.red[What is the addition of SPATIAL to the database?]

]]

---
class: left, middle

.split-40[.column[
### Spatial Indexing

- Spatial indexing is a crucial and arguably the main component of a spatial database because it's essential for efficiently querying large datasets of geographic or geometric data. 

- KD-Tree, QuadTree

- R-Tree

].column[
<img src="resources/w12-img/R-tree.svg.png" width="100%" align="center">

.footnote-right.small.square[Image source: [Wikipedia: R-tree](https://en.wikipedia.org/wiki/R-tree)]
]]

---
class: left, middle

.split-30[.column[
### Example of spatial query (PostGIS)
].column[
#### Create table
```sql
CREATE TABLE public.cities (
    id serial PRIMARY KEY,
    name VARCHAR(255),
    population INT,
    geom GEOMETRY(Point, 4326) -- Point geometry, SRID 4326 (WGS 84 geographic coordinate system)
);
```

#### Insert data rows (point)
```sql
INSERT INTO public.cities (name, population, geom) VALUES
('London', 8982000, ST_SetSRID(ST_MakePoint(-0.1278, 51.5074), 4326)),
('Paris', 2141000, ST_SetSRID(ST_MakePoint(2.3522, 48.8566), 4326)),
('New York', 8419000, ST_SetSRID(ST_MakePoint(-74.0060, 40.7128), 4326));
```
]]

---
class: left, middle

.split-30[.column[
### Example of spatial query (PostGIS)
].column[
#### Finding cities within a search distance from a point
```sql
    SELECT name
    FROM public.cities
    WHERE ST_DWithin(
        geom::geography,
        ST_SetSRID(ST_MakePoint(-0.1278, 51.5074), 4326)::geography,
        100000 -- distance in meters
    );
```

#### Spatial Joins
```sql
-- Assuming another table 'countries' with a 'geom' column (Polygon)
SELECT c.name AS city_name, co.name AS country_name
FROM public.cities AS c, public.countries AS co
WHERE ST_Contains(co.geom, c.geom);
```

#### Do calculation (area)
```sql
    SELECT ST_Area(ST_GeomFromText('POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))', 4326));
```
]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 2]
## Geospatial Ethics
------
.square[Ethics .dot[] Code and Rules of Conduct .dot[] Geospatial Privacy]

.headnote.square.bold.x-large[Geovisualisation II]

---
class: left, middle
### What is Ethics

> “Ethics, also known as moral philosophy, involves systematic intellectual reflection on morality in general ... or specific moral concerns in particular. The former can be called .red[theoretical ethics], and the latter .red[applied ethics], though the two are closely related. One realm of applied ethics that ahs garnered considerable attention outside philosophy focuses on professional conduct; thus, .red[the moral questions asked by scientists], as well as those in, for instance, the fields of law, medicine, and business, are legitimate components of ethical inquiry.”

In [Proctor, James D (1998). Ethics in geography: giving moral form tot he geographical imagination. Area 30.1, p. 9.](https://www.jstor.org/stable/20003845) 

.red.bold[Ethics is not what you do, but .underline[why] you do it.]

---
class: left, middle

.split-30[.column[
### Ethics in geospatial data analysis
#### Definition
].column[
Ethics in geospatial data analysis refers to the application of moral principles and guidelines to ensure that the collection, analysis, and use of geospatial data are .red[conducted responsibly and with respect for individuals, communities, and the environment].

- [A GIS Code-of-Ethics](https://www.gisci.org/Ethics/Code-of-Ethics)
- [Rules of Conduct for Certified GIS Professionals](https://www.gisci.org/Ethics/Rules-of-Conduct)

]]

---
class: center, middle

.split-30[.column[
### Code of Ethics

The link: [Code-of-Ethics](https://www.gisci.org/Ethics/Code-of-Ethics)
].column[

<img src="resources/w12-img/code_of_ethics.png" width="95%" align="center">
]]

---
class: center, middle

.split-30[.column[
### Rules of Conduct
The link: [Rules of Conduct](https://www.gisci.org/Ethics/Rules-of-Conduct)
].column[

<img src="resources/w12-img/rules_of_conduct.png" width="95%" align="center">
]]

---
class: center, middle

### Ethics is not legality

<img src="resources/w12-img/ethical_legal.png" width="65%" align="center">

Ethics is not a front-line of defense against wrong-doing.

Ethics is more like a touchstone for professionals to identify and resolve ethical dilemmas that they encounter in their research. 

---
class: left, middle

.split-30[.column[
### Geospatial Privacy
].column[

In geospatial research, particularly in people-related topics like health, crime, and disease-related studies, we often encounter privacy concerns. 

Sometimes, these concerns are the reason we cannot access certain data, such as the COVID-19 distribution data in the early days of the pandemic. 
- In the early days of a situation involving small case numbers, the data can be traced back to individual households or persons, potentially creating unnecessary problems for the people involved. As a result, government agencies may be unable to disclose such data.
- bias and inequality, privacy  

In other cases, privacy becomes a crucial aspect to consider while writing the results, ensuring that we do not reveal any private information in our reports or manuscripts. 
- Making sure the anonyminity or de-identification could not be re-identified.
]]

---
class: left, middle

.split-30[.column[
### Geospatial Privacy
Protecting geospatial information privacy involves employing various strategies to ensure that individuals' personal information remains .red[secure] and .red[anonymous]. 
].column[

.bold[Data anonymization]:  
Remove or alter personally .red[identifiable information] from geospatial datasets. This can be achieved through techniques such as generalization, perturbation, or differential privacy.

.bold[Geo-masking]:  
Geo-masking involves altering or obscuring the .red[precise location information] in geospatial data to protect individual privacy. This can be achieved by shifting, rotating, or perturbing the coordinates, or by introducing random noise to the location data. Geo-masking allows for the analysis of geospatial patterns and trends while maintaining a degree of anonymity for individuals or sensitive locations.

.bold[Data aggregation]:  
.red[Combine data from multiple individuals or locations] to make it more difficult to trace information back to a specific person or place.

.bold[Privacy-preserving data mining]:  
Utilize .red[data mining techniques] that protect privacy, such as k-anonymity, l-diversity, or t-closeness, to analyze geospatial data without revealing sensitive information.

]]

---
class: center, middle, inverse

.xx-large.bold.wide[PART 3]
## Geospatial Visualisation - a Final Closing Remark
------
.square[Visualisation .dot[] Good Elements .dot[] Some Bad Examples]

.headnote.square.bold.x-large[Geovisualisation II]

---
class: left, middle

.split-40[.column[
### Visualization?
The comic shows a .red[visualization] of the relationship between human proximity to cat and the intelligence of the person.

Visualization is .red[the process of representing data or information] in a graphical or pictorial form .red[to communicate an idea, concept, or pattern] more effectively.

].column[.justify[
<img src="resources/w01-img/xkcd_cat_proximity.png" width="90%" align="center">

.footnote[.square[[Cat Proximity (xkcd.com/231)](https://xkcd.com/231/). ]]
]]
]

---
class: center, middle

### Why visualization? 
<img src="resources/w01-img/drawing-data_info_insight.png" width="80%" align="center">

---
class: left, middle

.split-30[.column[
### Why visualization? 
Geovisualization is a series of explorations and analyses, that includes using various techniques and methods, e.g., thematic mapping, exploratory spatial data analysis, to uncover the underlying patterns, to get better understanding of geographical phenomena.
].column[
<img src="resources/w01-img/drawing-how_maps_are_used.png" width="100%" align="center">
.square[MacEachren's cartographic cube.]
]]

---
class: left, middle
.split-30[.column[
### What is a good visualisation

A good data visualization effectively communicates complex information in a clear, concise, and engaging manner, allowing the audience to quickly understand the data's key insights and messages. 

].column[
- .bold[Clear Purpose]:  
A well-defined purpose or goal helps guide the creation of the visualization, ensuring that it .red[addresses relevant questions and objectives].

- .bold[Appropriate Visual Encoding]:  
The choice of .red[visual elements (e.g., color, size, position)] should accurately represent the data and facilitate easy comparison, pattern identification, and understanding.

- .bold[Clarity and Simplicity]:  
A good visualization should be .red[easy to comprehend], avoiding unnecessary complexity and clutter. Clear labeling, appropriate use of scale, and logical organization contribute to overall clarity.

- .bold[Meaningful Context]:  
Providing context through .red[labels, titles, captions, and reference points] helps the audience interpret the data more accurately and effectively.

]]

---
class: left, middle
.split-30[.column[
### What is a good visualisation

A good data visualization effectively communicates complex information in a clear, concise, and engaging manner, allowing the audience to quickly understand the data's key insights and messages. 

].column[

- .bold[Attention to Detail]:  
A well-crafted visualization pays attention to details such as .red[color palettes, fonts, and visual hierarchy], creating an aesthetically pleasing and professional-looking end product.

- .bold[Accessibility]:  
Ensuring that visualizations are .red[accessible to all readers], including those with color vision deficiency or other visual impairments, is an essential aspect of good data visualization.

- .bold[Interactivity and Responsiveness]:  
Interactive visualizations allow users to explore and customize the data presentation, .red[enhancing engagement] and understanding.

- .bold[Accuracy]:  
A good visualization accurately represents the underlying data, .red[avoiding distortion or misrepresentation].

]]

---
class: left, middle
.split-40[.column[
### Some examples and ideas for good visualisation
#### Get some inspiration here:  
- [Information is Beautiful](https://informationisbeautiful.net/)
- [Data Viz Project](https://datavizproject.com/)
].column[
#### Information is Beautiful
<img src="resources/w12-img/information_is_beautiful.png" width="100%" align="center">
]]

---
class: left, middle
.split-40[.column[
### Some examples and ideas for good visualisation
#### Get some inspiration here:  
- [Information is Beautiful](https://informationisbeautiful.net/)
- [Data Viz Project](https://datavizproject.com/)
].column[
#### Data Viz Project
<img src="resources/w12-img/data_viz_project.png" width="90%" align="center">
]]

---
class: left, middle
### Statistics for better visualisation
Statistical tools play a crucial role in creating meaningful geospatial data visualizations and forming useful insights.

.split-50[.column[

- .bold[Descriptive Statistics]:  
Basic descriptive statistics like mean, median, standard deviation and frequency distribution can help .red[summarize and describe] geospatial data.

- .bold[Data Classification]:  
Methods for classifying geospatial data, such as equal interval, quantile, natural breaks, and geometrical intervals help .red[organize and group data] for effective visualization and analysis.

- .bold[Spatial Autocorrelation]:  
Spatial autocorrelation techniques could measure the similarity between values in a given spatial dataset. This can help .red[identify spatial clusters or outliers] in the data.
].column[

- .bold[Spatial Heterogeneity]:  
Heterogeneity refers to the variability of a variable across a study area. Spatial heterogeneity can be analyzed using techniques like geographically weighted regression (GWR) or spatial error models to better understand .red[regional variations and factors influencing local patterns].

- .bold[Spatial Dependence]:  
Spatial dependence occurs when the values of a variable at one location depend on the values of the variables at nearby locations. Analyzing spatial dependence can help model spatial relationships and predict outcomes more accurately.

]]

---
class: left, middle
### Elements for bad visualisation
.split-50[.column[
- .bold[Clutter and Complexity]:  
Excessive use of colors, fonts, labels, or visual elements can make a visualization .red[difficult to interpret and detract from its main message].

- .bold[Misleading Scales or Axes]:  
Manipulating or misrepresenting .red[scales or axes] can distort the data and lead to inaccurate conclusions.

- .bold[Poor Color Choices]:  
Using color palettes with .red[low contrast or inappropriate color associations] can make it difficult for viewers to distinguish between different data points or categories.

- .bold[Confusing Data Encoding]:  
Inconsistent encoding of data (e.g., .red[using different symbols or sizes for the same value]) can make it challenging for the audience to compare and understand the data.

].column[

- .bold[Unnecessary 3D Effects]:  
Adding 3D effects .red[without a specific purpose] can add unnecessary complexity and make it harder to interpret the visualization accurately.

- .bold[Lack of Context]:  
Omitting important contextual information, such as .red[units, labels, or reference points], can hinder the audience's ability to understand and interpret the data accurately.

- .bold[Unnecessary Visual Elements]:  
Including .red[irrelevant visual elements] or "chart junk" can distract from the main message and clutter the visualization.

- .bold[Inaccurate Representation of Data]:  
Using the .red[wrong visualization type] for the data type or purpose can lead to misinterpretation and misunderstanding.
]]

---
class: center, middle
### Example of bad visualisation
.split-50[.column[
<img src="resources/w12-img/bad-3d_bar.png" width="100%" align="center">  
Unnecessary 3D view.
].column[
<img src="resources/w12-img/bad-piechart.png" width="100%" align="center">  
A bar chart could be clearer.
]]

---
class: center, middle
### Example of bad visualisation
<img src="resources/w12-img/bad-line_discrete.png" width="70%" align="center">  
Line plot used to show discrete data (not continuous).

---
class: center, middle
### Example of bad visualisation
<img src="resources/w12-img/bad-confusing.png" width="70%" align="center">  
Confusing composition --- what is the main message?


---
class: center, middle
### Example of bad visualisation
<img src="resources/w12-img/bad_visual_time_spiral.jpg" width="40%" align="center">  
Unnecessary spiral effect --- what is the main message?

---
class: center, middle
### Example of bad visualisation
<img src="resources/w12-img/bad-negative-values.png" width="70%" align="center">  
Negative values going up and/or down?

---
class: left, middle
.split-50[.column[
### Example of bad visualisation
Color palette choice & type of chart (bar? or just table). 
].column[
<img src="resources/w12-img/bad-color-palette-types.png" width="70%" align="center">  
]]

---
class: center, middle
### Example of bad visualisation
<img src="resources/w12-img/bad-change_size_range.png" width="70%" align="center">  
Generated based on the relative diameters of their circles, not relative areas.  
It’s subtle but still misleading.   

---
class: center, middle
### Example of bad visualisation
<img src="resources/w12-img/bad-color_category.jpg" width="70%" align="center">  
Inconsistent categories and colors. 

---
class: center, middle
### Example of bad visualisation
<img src="resources/w12-img/bad-maps-numbers.jpg" width="40%" align="center">  
Distracting labels (numbers). 

---
class: center, middle
### Example of bad visualisation
<img src="resources/w12-img/bad-maps-area_effect.jpg" width="50%" align="center">  
Confusing area effect. 

---
class: center, middle
### How about this?
<img src="resources/w12-img/how-3D-population.png" width="80%" align="center">  
Population (3D) in New York City.

---
class: center, middle
### How about this?
<img src="resources/w12-img/how-3D-SFO-tree.png" width="80%" align="center">  
Tree density in San Francisco.


---
class: left, middle

.split-40[.column[
## The final summary
what we have covered in this semester
].column[
- Principles of Visualisation

- Statistical Pattern

- Point Pattern

- Areal Pattern

- Geovisualization
]]

---
class: center, middle

<img src="resources/w11-img/recap-overall.drawio.png" width="100%" align="center">

---
class: center, middle
background-image: url(resources/w12-img/NUS-map.png)

<h2 style="color: #00000090">Thank you, and all the best for your new journey.​</h2>
------
Questions?
