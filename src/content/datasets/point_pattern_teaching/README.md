# Reproducible point-pattern teaching constructions

These files contain **synthetic data**, not observed FIRMS fire detections, actual bus-stop coordinates or an empirical regional point-event sample. They support the quadrat, NNA and K-function readings.

## Files and coordinate frame

- `synthetic_points.csv`: 96 points in each of three patterns, with `pattern`, `x_m` and `y_m` fields. Coordinates use a fictional planar metric frame, not a geographic CRS. Do not put them on a real basemap.
- `results.json`: original seed 5230, simulation seed 5231, 999 simulations, the fixed window, radius grid and computed results.
- `../../../../scripts/point_pattern_examples.py` in the repository root is the authoritative generator. Run `python scripts/point_pattern_examples.py --write` from the repository root. Its default invocation checks the calculations without regenerating images.

The observation window is the full square `[0, 2000] x [0, 2000]` metres. It is defined independently of each point pattern and remains fixed. The CSR sample contains independent uniform points. The clustered construction places 24 normally displaced points around each of four centres. The spaced construction jitters a 12 by 8 lattice. These constructions illustrate contrasting summaries; their labels do not imply that every statistic must reject a particular null.

Quadrat figures use a 4 by 4 partition with expected count six in each cell. The sensitivity figure also uses a 2 by 2 partition and a shifted grid clipped to the same window. Expected counts for clipped cells use their actual areas. All points, including those on the outer edge, enter exactly one cell.

NNA calculations use Euclidean distances to the closest other point. The expected distance and ratio use the unbounded planar Clark–Evans approximation; they are not boundary-corrected finite-window inference.

The K figures use the explicitly implemented rectangular translation correction and ordered-pair normalisation. The plotted summary is `sqrt(K/pi) - r`, with radii 25–500 m. The 2.5th and 97.5th simulated quantiles at each radius are **pointwise reference bands**, not a global envelope test or confidence intervals for a true process curve. The same 999 fixed-count uniform samples supply the quadrat reference and K bands.

The separate bus-stop-inspired construction uses 16 regularly spaced sites, each with two points 30 m apart. It is illustrative and does not appear in the empirical-record CSV. The existing bus-stop image on the page is retained only as motivation; no new empirical result is attributed to it.

## Planned Sumatra FIRMS case

Source: NASA [Fire Information for Resource Management System (FIRMS) archive](https://firms.modaps.eosdis.nasa.gov/download/). The selected case is fire-detection locations in a fixed land window within Sumatra during **1–30 September 2026**, using **VIIRS S-NPP** consistently. This connects to the planned regional areal-autocorrelation application. It replaces the earlier lightning proposal.

Historical archive downloads require Earthdata authentication or an email verification code. No September 2026 detection file has been downloaded or processed for this change. All committed numerical data and figures remain explicitly synthetic, with no substitution of simulated points for observed fires.

Before adding regional results:

1. Obtain the selected archive CSV, preserve its source product, date range, download date, version and checksum. Recent near-real-time records may later be replaced by standard science-quality records.
2. Confirm the source record definition and confidence fields, select and document a confidence filter before analysis, and use one satellite product. The nominal detection-product pixel size is not a guarantee of exact point-location accuracy.
3. Distinguish duplicate delivery of the same source record from repeat observations of persistent fire activity. Remove delivery duplicates using the product's record key; retain distinct observations unless a separately documented fire-event grouping procedure is the actual question. Detections are not separate fire incidents or necessarily forest fires.
4. Select a land observation window independently of the realised detections. Exclude ocean from this land-based question, retain zero-detection land cells, and inspect coverage gaps and detectability. No detection is not proof of no fire.
5. Project to a suitable metric CRS and document the CRS, window and grid origin. Use actual land area for clipped cells and simulate within the same usable window. The existing K implementation is for rectangles; an irregular land mask needs a compatible correction or a clearly stated finite-window comparison.
6. Report the selected null, alternative, period and scale. Any observed-event map, count map and reference distribution must be generated from validated records. Heterogeneous land conditions, clouds, repeat observations and viewing opportunities qualify the homogeneous CSR reference. A result about detection locations does not attribute haze exposure in Singapore or Malaysia to particular fires.

## Verification and attribution

The generator checks boundary-point allocation, count conservation, a hand-worked chi-squared statistic, nearest-neighbour distance, the ordered-pair translation correction, monotonic K curves and agreement with the committed result record. It also rejects points outside the declared window.

Original code follows the repository's MIT code licence; original teaching prose and figures follow the repository's content licence. Data-source attribution and permissions must be recorded separately when the FIRMS case is added.
