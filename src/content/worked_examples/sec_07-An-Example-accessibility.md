# Visualising Healthcare Accessibility in Singapore: From Mobility to Service Intensity

A clinic can be close on a map but difficult to reach, while a more distant clinic may be connected by a convenient route. Even when travel is feasible, many people may be competing for the same services. **Proximity, mobility and accessibility are related, but they are not interchangeable.**

This case study examines how several visualisations tell different parts of that story. It revisits an existing [Singapore healthcare accessibility demonstration](https://wcchin.github.io/sg_health_access/) and its legacy figures. The focus is on **choosing geographical representations, reading model-based evidence and communicating its limitations**, not learning to implement an accessibility model from scratch.

**Connections to the core chapters:** [Spatial data and representation](../chapter_2/chapter-2-spatial_data.md), [statistical patterns](../chapter_3/chapter-3-stat_pattern.md), [areal patterns](../chapter_6/chapter-6-areal_pattern.md) and [geovisualisation and storytelling](../chapter_7/chapter-7-geovisualisation.md). The radiation and floating-catchment models introduced below are additional application concepts, not prerequisites taught earlier in the book.

```{figure} ../resources/w11-img/example-1-link.png
:alt: Preview of the existing Singapore healthcare accessibility demonstration.
:align: center

Explore the [original interactive demonstration](https://wcchin.github.io/sg_health_access/). The following illustrations explain the communication choices in that project; they are not newly calculated or independently validated outputs in this revision.
```

## 1. The geographical problem: what does access mean?

Suppose a planner asks: **Which parts of Singapore have better access to primary healthcare?** A map of clinic locations is a start, but it cannot answer the question by itself. Relevant factors might include population demand, transport connections, service capacity, opening hours and the types of care available.

The original demonstration concentrates on a subset of clinic resources identified as **ISP clinics**, population distribution, network information and an illustrative **800 m hexagonal representation**. The clinic label is retained from the original project; the reader should not assume it means every primary-care provider in Singapore.

Two audiences might need different explanations. A general reader may want to understand why proximity can be misleading. A planner may need to know which spatial units, assumptions and capacity measures were used before evaluating any implication for service provision.

**Guiding question:** What can a series of maps and charts reveal about *modelled* access to clinics, and where do those displays stop short of describing real healthcare experiences?

## 2. From observations to estimated movements

The case combines several types of geographical information: locations of clinics, where population is distributed, a travel network and spatial units for summary and display. These sources are not equivalent observations. A clinic point marks a provider location; a population unit estimates potential demand; a network represents possible connections rather than a record of actual patient journeys.

### A short model primer: radiation

A **radiation model** is a spatial-interaction model used to estimate movements between origins and destinations using the distribution of opportunities. Conceptually, the attraction of a destination depends not only on its own opportunities but also on alternatives that may be encountered closer to the origin. The implementation and interpretation depend on how populations, opportunities and separation are defined.

The resulting lines are **estimated flows**, not tracked journeys made by individual patients. A visualisation must preserve that distinction.

```{figure} ../resources/w11-img/network_flow_isp_clinic.png
:alt: Existing static map of estimated connections to ISP clinic locations.
:align: center

A static flow map emphasises the geography and direction of estimated origin–destination relationships. Line symbols and colours need a stated quantity and classification; visible lines are model outputs, not observed patient tracks.
```

```{figure} ../resources/w11-img/flowmap-gl.png
:alt: Screenshot of the original interactive flow map.
:align: center

An interactive flow map allows a reader to inspect selected connections and reduce overlap. Explore the [original Flowmap.gl display](https://app.flowmap.city/public/67249d1d-4c21-40e3-8ddb-fd5124907c99). Interactive selection can improve readability but does not change the underlying model or its uncertainty.
```

**Visual choice:** A line map makes geography visible, but many overlapping lines can obscure the overall pattern. Would it be more useful to emphasise selected destinations, stronger connections or broader regional movement? Each choice hides something else.

## 3. From a map to a diagram of relationships

The next view aggregates estimated movements by planning area and uses a Sankey/alluvial-style diagram. Here the interest shifts from *where the movement lies on a map* to *which origin–destination connections dominate*.

```{figure} ../resources/w11-img/sankey_flowmap-bokeh.png
:alt: Existing flow diagram showing aggregated estimated movement relationships.
:align: center

A flow diagram makes relative volumes between area categories easier to compare, but it suppresses exact location, route geometry and travel distance. See the [interactive diagram](https://wcchin.github.io/sg_health_access/interactive/holoviews_sankey_pln_flow.html).
```

Neither representation is inherently better. The map preserves spatial context; the diagram prioritises relationships and relative magnitude. Both inherit any aggregation effects and model assumptions in the flow estimates.

**Self-check:** If a planning area has a wide outgoing band, can we conclude that its residents actually visited more clinics?

```{dropdown} Feedback
No. The bands represent modelled and aggregated connections in this demonstration. They should not be read as observed visits or evidence of individual behaviour without separate validation data.
```

## 4. How far do the estimated journeys extend?

A distribution of travel distances highlights something that neither a flow map nor a Sankey diagram communicates efficiently: the spread of estimated journey lengths, and how it differs between regional categories.

```{figure} ../resources/w11-img/mobility-by-region.png
:alt: Existing distribution plots of estimated travel distances grouped by region.
:align: center

The distribution view helps compare ranges, concentrations and differences between regional groups. Visit the [original distance display](https://wcchin.github.io/sg_health_access/#histogram).
```

A distance distribution can reveal whether estimated trips concentrate at shorter ranges or have long tails. But a distance is not necessarily **travel time, affordability, ease of transfer or accessibility for someone with reduced mobility**. Interpretation depends on how the distance was measured and how modelled flows were weighted in the plot; the original figure does not, by itself, verify patient travel distances.

## 5. From movements to accessibility

### A short model primer: two-step floating catchment area

The **two-step floating catchment area (2SFCA)** family of methods relates healthcare supply to potential demand within defined catchments. In simplified terms:

1. Around each provider, compare its available supply with population demand in a chosen catchment.
2. Around each population location, combine the supply-to-demand ratios of reachable providers.

Thus, the resulting score describes **modelled potential accessibility under specified catchments, provider capacities and population inputs**. It is not an observed measure of utilisation, healthcare quality or actual health outcomes. Travel thresholds, impedance and provider definitions can materially alter the result. Some 2SFCA variants include distance-decay weights or other refinements; the specific implementation should be documented before its values are compared with another study.

```{figure} ../resources/w11-img/accessibility-keplergl.png
:alt: Existing service-intensity and clinic accessibility visualisation.
:align: center

The original demonstration combines hexagonal service-intensity representation with a second circular accessibility display. See the [interactive accessibility map](https://wcchin.github.io/sg_health_access/interactive/keplergl_accessibility_clinic.html). Check the legend and the original data definitions before treating the two symbol systems as comparable measurements.
```

The original work used approximately 800 m hexagons for visual presentation. Aggregation can help reduce clutter, but **a hexagon is not a neighbourhood experienced by a resident**. Changing the grid size or its alignment can change what the map appears to emphasise. More importantly, a mapped ratio should not be read as a verified shortage or surplus without checking the capacity and demand assumptions behind it.

## 6. What does each view contribute?

| Representation | Makes clearer | Can obscure or overstate |
| --- | --- | --- |
| Flow map | Geographic direction and distribution of estimated movements | Overplotting; estimated flows mistaken for observed journeys |
| Sankey diagram | Magnitudes of aggregated origin–destination relationships | Where flows travel and how far apart areas are |
| Distance distribution | Variation and long tails in estimated journey distances | Routes, travel time and individual constraints |
| Accessibility map | Spatial variation in a modelled supply–demand summary | Sensitivity to catchments, capacity data and spatial aggregation |

Read the four views as **complementary evidence**, not four independent confirmations of a single claim. Because several of them may use the same estimated flows or input data, agreement in appearance is not equivalent to independent validation.

### Check your reasoning

**Self-check:** An area looks close to several clinics but has a low modelled accessibility score. Is the map necessarily wrong?

```{dropdown} Feedback
Not necessarily. Accessibility can depend on population demand, provider supply, catchment thresholds and travel impedance—not simple distance alone. First check which definitions the model uses; then inspect whether the input data and assumptions fit the question.
```

## 7. Reflection: a compelling visual story with honest limits

The sequence can be presented as a progression:

**Where are possible connections? → Which area relationships dominate? → How do estimated distances vary? → Where does the supply–demand model suggest relative differences?**

That narrative is useful precisely because it does not equate location, travel and service access. Yet it remains an exploratory, model-based demonstration rather than a validated policy assessment.

Important limits include the original project's selected provider category (not all healthcare services), spatial aggregation, unspecified or potentially simplified travel and capacity assumptions, and the absence of direct validation against actual clinic use. More detailed analysis would need up-to-date provider capacity, the relevant transport modes and travel times, population groups with different needs, and explicit sensitivity tests.

**Closing question:** If you had one slide for the public and one for a healthcare planner, which view would you choose for each, and what one sentence would you use to prevent overinterpretation?

```{dropdown} Feedback
For the public, a clearly labelled accessibility map alongside an explanation that the scores are modelled could introduce the problem. For planners, pairing the map with sensitivity to catchment and supply assumptions would be more defensible. Other choices can work if the audience, evidence and limitations are made explicit.
```

## Explore further

Revisit [Chapter 7](../chapter_7/chapter-7-geovisualisation.md) for visual hierarchy, narrative structure and communication ethics, and [Chapter 2](../chapter_2/chapter-2-spatial_data.md) for representation and spatial aggregation. The [original Singapore healthcare demonstration](https://wcchin.github.io/sg_health_access/) provides the existing interactive outputs.

For the underlying modelling ideas, see the [radiation-related research linked in the original project](https://www.nature.com/articles/s41598-021-02109-1) and the [original 2SFCA reference](https://journals.sagepub.com/doi/10.1068/b29120). These are extensions beyond the core book; this case study does not claim to reproduce either model numerically. A later reproducibility exercise could verify the original inputs, parameter choices, provider definitions and outputs before publishing quantitative findings.
