# An Example - The Healthcare Resource Accessibility



```{figure} ../resources/w11-img/example-1-link.png
:label:
:alt:
:align: center

The demonstration page: [the link](https://wcchin.github.io/sg_health_access/)
```



## Motivation
### Background
As one of the most densely populated countries in the world, _Singapore faces challenges in ensuring equal access to healthcare for all_. The high population density has increased the demand for healthcare services, putting strain on the country's medical infrastructure.

Although clinics are located in every neighborhood, the quality and intensity of healthcare services vary in different parts of the city-state, leading to disparities in access.

Additionally, healthcare services in different geographic areas may experience varying levels of demand, subsequently affecting their ability to provide high-quality care to patients.

It is thus critical to assess the spatial distribution of the availability and accessibility of healthcare services.

### Problem
The spatial distribution of the availability and accessibility of healthcare services requires more exploration and analysis.

### Audience
- Urban planners
- General Public

### Data
- ISP Clinic locations
- Population distribution
- Road network
- Hexagons (800m size)

### Solution
This project presents a framework to measure the healthcare intensity by combining two popular models: radiation models and 2-step floating catchment area (2SFCA).


## Visualization
After the flows were estimated and healthcare intensity were calculated, we show the results below in 4 sections:
- Flow Estimation Map
- Movements between Planning Area
- Distribution of Travel Distances
- Service Intensity Map

### Flow Estimation Map
Estimated flow using [radiation models](https://www.nature.com/articles/s41598-021-02109-1).

Static, simple, map using arrows to show directions and colors to show above or below median.



```{figure} ../resources/w11-img/network_flow_isp_clinic.png
:label:
:alt:
:align: center

Estimated flows demonstrated with a static map.
```


Interactive map with the same data, using Flowmap.gl.

```{figure} ../resources/w11-img/flowmap-gl.png
:label:
:alt:
:align: center

[Interactive Map Link](https://app.flowmap.city/public/67249d1d-4c21-40e3-8ddb-fd5124907c99)
```


Aggregated flows by planning areas, visualize using Sankey graph (or Alluvial graph).

```{figure} ../resources/w11-img/sankey_flowmap-bokeh.png
:label:
:alt:
:align: center

[Interactive Map Link](https://wcchin.github.io/sg_health_access/interactive/holoviews_sankey_pln_flow.html)
```




### Mobility
The frequency distribution of travel distance, grouped by regions.



```{figure} ../resources/w11-img/mobility-by-region.png
:label:
:alt:
:align: center

[Interactive Map Link](https://wcchin.github.io/sg_health_access/#histogram)
```


### Accessibility Map

Accessibility to ISP Clinics estimated using [2SFCA](https://journals.sagepub.com/doi/10.1068/b29120).
Hexagon shows the service provider intensity. Circle shows the accessibility.


```{figure} ../resources/w11-img/accessibility-keplergl.png
:label:
:alt:
:align: center

[Interactive Map Link](https://wcchin.github.io/sg_health_access/interactive/keplergl_accessibility_clinic.html)
```




### Reflection

- **What was done**: The visualizations show some maps and graphs to display the population mobility for accessing healthcare service (ISP Clinic).

- **Resolution**: For visualization purpose, the spatial units were set to 800m hexagon size, which could be too large for analyzing walkable neighborhoods (400m).

- **Lack of spatial**: How spatial autocorelation, heterogeneity, or other spatial interactions effects may exists are not discussed.

- **Far from pratical**: The analysis remains conceptual, and thus, further development is required before it can effectively inform practical policy-making.

- **Other level of resource**: The visualization did not present the other level of healthcare resources, e.g., polyclinics and hospitals. Visualization for Comparison can be challenging.
