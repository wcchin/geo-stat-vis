# 7.2 Map components as parts of an argument

A title, legend, boundary and scale bar are not finishing touches. Together they tell readers what the map represents and which comparisons are possible. Begin with the question the panel must answer, then choose the components that make that answer inspectable.

## Establishing place and scale

A national overview locates patterns; a local map helps us inspect what lies around a particular block. These purposes require different extents. Our three local maps use identical extents and physical scale. A 500 m circle therefore appears the same size in each panel. Enlarging one neighbourhood until its facilities filled the frame would make it look richer in detail while quietly changing the comparison.

```{figure} ../datasets/neighbourhood_story_2026/figures/02_neighbourhoods.png
:label: ch7-02-neighbourhoods
:alt: Three equally scaled local maps showing selected blocks, bus stops and three amenity categories
:align: center

Three named blocks with 500 m solid circles and 800 m dashed circles. Symbols outside the circles provide context but do not enter the corresponding count. The maps show planning boundaries rather than a street network, so they cannot demonstrate routes across roads, canals or other barriers.
```

Distance calculations require a suitable coordinate reference system. Latitude and longitude are angular coordinates; their numerical differences are not metres. We transform the points to EPSG:3414 before measuring Euclidean distances. The circle is a straight-line search boundary, not a walking catchment. Projection makes the metric calculation consistent; it does not add information about pedestrian routes.

The 500 m and 800 m choices are teaching scenarios, not universal walking thresholds. A reader using a mobility aid, a parent accompanying a child and a commuter carrying groceries may experience the same distance differently. We keep the units explicit rather than converting the radii into unsupported walking times.

## Colour, symbols and legends

Use a sequential palette for a quantity that progresses from smaller to larger. Our price and boarding maps use OrRd, with separate colour scales because the units differ. A darker bus point does not mean the same thing as a darker HDB point. The bus colour scale is logarithmic to reveal variation in a skewed activity distribution; the label states that transformation. The price overview fixes its colour range at S\$300,000–S\$1,400,000 and indicates clipped extremes. Exact observations remain in the data.

Amenity categories have no natural order. We use distinct hues and shapes: squares for hawker centres, triangles for schools and diamonds for park reference points. Shape gives readers a second cue when colours are hard to distinguish. Stops recede in neutral grey; the selected block has a dark star. A legend should explain the visible encoding, including what a size or colour means, rather than merely name the data provider.

Do not imply that every point represents an equivalent facility. A park diamond might locate a small recreation site or a reference position for a much larger park. A school triangle does not encode enrolment, available places or school level. Those omitted attributes are reasons to refine the analysis if the audience's question requires them.

## Titles and captions divide the work

A title should orient attention. A caption should supply the unit, period, selection rule and the limitation most likely to change interpretation. “Neighbourhood accessibility” would overstate what {numref}`ch7-02-neighbourhoods` measures. “What is nearby?” is a better opening, provided the caption immediately defines “nearby” as a straight-line radius and identifies the selected records.

For a standalone map, include enough source information that it remains understandable outside the chapter. For a sequence, stable layouts and a shared source note can reduce repetition, but each panel still needs its own units and period. A figure copied into a slide should not lose those essentials.

## Typography, layout and export

Use a clear reading order: title, main evidence, legend or direct labels, then supporting notes. Keep map labels readable at the size students will actually view. Exporting at a high dots-per-inch value cannot rescue tiny text. For raster figures, choose pixel dimensions for the display or print size; retain vector output where practical for line work and text. Inspect the exported figure rather than relying on the plotting window.

Our original figures use Comic Neue, a hand-drawn-style font bundled with its licence. The geographic boundaries and measured circles remain undistorted. A playful typeface can establish a teaching tone; applying a sketch effect to precise geometry could make a boundary or distance harder to read. Font choice should support comprehension rather than signal scientific authority.

**Check your map.** Hide the surrounding paragraph and ask a classmate to describe the unit, period and meaning of each symbol. Any disagreement identifies information the figure still needs.
