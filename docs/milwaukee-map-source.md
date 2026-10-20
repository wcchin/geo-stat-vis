# Milwaukee income maps: data and rendering

The book's three opening autocorrelation illustrations are original course maps drawn from real Census data. They replace the synthetic grid illustrations proposed in the initial version of PR #2. The two six-unit rook-neighbour diagrams remain synthetic teaching examples.

## Source and geographic verification

- Catalogue: [GeoDa Milwaukee Employment 2000](https://geodacenter.github.io/data-and-lab/milwaukee1/).
- Archive: <https://geodacenter.github.io/data-and-lab/data/MilwaukeeMSA.zip>.
- Archive SHA-256: `bf3c9617c872db26ea56f20e82a449f18bb04d8fb76a653a2d3842d465bc122c`.
- File used: `MilwaukeeMSA/wi_final_census2_random4.geojson`.
- Underlying source: US Census 2000, Summary File 3, prepared for distribution by the Center for Spatial Data Science. Income refers to **1999**, not 2000 or the present.
- Variable: `HH_INC`, median household income in 1999, US dollars.
- Geography: 417 census tracts, all with `MSA = Milwaukee`, in Wisconsin counties with FIPS prefixes 55079 (Milwaukee), 55089 (Ozaukee), 55131 (Washington) and 55133 (Waukesha). This is the metropolitan area, not only the city.

The catalogue's introductory sentence mentions Lansing and a county shapefile. The archive also includes a separate three-county Michigan file, `mi_msa_counties`; that file is **not used**. The selected Wisconsin layer, its 417 records, MSA names and FIPS identifiers were checked directly.

## Missing values and permutations

Four `HH_INC` records are coded zero: FIPS 55079090500, 55079014500, 55079013100 and 55079000000. They are treated as unavailable rather than interpreted as measured zero median income. Grey represents these four fixed locations in every panel.

Only the remaining 413 positive finite incomes are permuted. Each permutation preserves the exact multiset of values, the four unavailable locations, boundaries, extent and colour classes. A NumPy generator with seed 5230 creates the displayed permutations. These are illustrative random reassignments, not additional Census observations or a completed significance test. They do not account for spatial variation in population composition or sampling uncertainty.

Fixed classes: below $25,000; $25,000 to below $40,000; $40,000 to below $55,000; $55,000 to below $75,000; and $75,000 or more.

## Reproduction and style

Run `python scripts/draw_spatial_figures.py`. The script downloads the 2.4 MiB source archive into a temporary cache, verifies its SHA-256 and reads the GeoJSON without a GIS dependency. For offline reproduction, pass `--data-archive /path/to/MilwaukeeMSA.zip`. CI runs the same checks. The source archive is not duplicated in this repository.

Matplotlib `plt.xkcd(scale=0.5, length=100, randomness=1)` supplies the requested sketch style. The bundled Comic Neue font is distributed under the SIL Open Font License (see `_static/css/fonts/ComicNeue-OFL.txt`). Font outlines are included in the SVGs so viewers do not need to install the font. Real map polygon vertices and holes are retained; sketch distortion is disabled for the geographic layer so adjacent boundaries remain aligned. The drawn map layer is rasterized inside the SVG, while annotations remain vector outlines.

Longitude/latitude vertices are displayed using a local equirectangular transformation centred at 43.1°N; no metric distance or area is inferred from this display. All panels share identical limits and aspect ratio. No external basemap or lecture screenshot is used. Captions retain the data attribution.
