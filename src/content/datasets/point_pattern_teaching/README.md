# Reproducible point-pattern teaching constructions

These files contain **synthetic data**, not measured lightning, actual bus-stop coordinates or an empirical Singapore point-event sample. They support the quadrat, NNA and K-function readings.

## Files and coordinate frame

- `synthetic_points.csv`: 96 points in each of three patterns, with `pattern`, `x_m` and `y_m` fields. Coordinates use a fictional planar metric frame, not a geographic CRS. Do not put them on a real basemap.
- `results.json`: original seed 5230, simulation seed 5231, 999 simulations, the fixed window, radius grid and computed results.
- `../../../../scripts/point_pattern_examples.py` in the repository root is the authoritative generator. Run `python scripts/point_pattern_examples.py --write` from the repository root. Its default invocation checks the calculations without regenerating images.

The observation window is the full square `[0, 2000] x [0, 2000]` metres. It is defined independently of each point pattern and remains fixed. The CSR sample contains independent uniform points. The clustered construction places 24 normally displaced points around each of four centres. The spaced construction jitters a 12 by 8 lattice. These constructions illustrate contrasting summaries; their labels do not imply that every statistic must reject a particular null.

Quadrat figures use a 4 by 4 partition with expected count six in each cell. The sensitivity figure also uses a 2 by 2 partition and a shifted grid clipped to the same window. Expected counts for clipped cells use their actual areas. All points, including those on the outer edge, enter exactly one cell.

NNA calculations use Euclidean distances to the closest other point. The expected distance and ratio use the unbounded planar Clark–Evans approximation; they are not boundary-corrected finite-window inference.

The K figures use the explicitly implemented rectangular translation correction and ordered-pair normalisation. The plotted summary is `sqrt(K/pi) - r`, with radii 25–500 m. The 2.5th and 97.5th simulated quantiles at each radius are **pointwise reference bands**, not a global envelope test or confidence intervals for a true process curve. The same 999 fixed-count uniform samples supply the quadrat reference and K bands.

The separate bus-stop-inspired construction uses 16 regularly spaced sites, each with two points 30 m apart. It is illustrative and does not appear in the empirical-record CSV. The existing bus-stop image on the page is retained only as motivation; no new empirical result is attributed to it.

## Planned Singapore lightning case

Source: NEA / Meteorological Service Singapore, [Lightning Observation](https://data.gov.sg/datasets/d_08238953fe0f6dd13f10714ebfbcb9f9/view), via data.gov.sg. The attempted public historical endpoint returned HTTP 403 in this environment on 21 October 2026. No event records were obtained, and no synthetic coordinates have been substituted under the label of lightning observations.

Before adding regional results:

1. Retrieve and preserve a complete fixed interval, including all pagination; record the source URL, retrieval date and response metadata.
2. Confirm whether records denote strokes or grouped flashes, retain one event type, and deduplicate repeated delivery of the same record using the documented identifiers or exact record key. Do not remove distinct real events merely because coordinates coincide.
3. Establish the time zone, observation coverage, gaps and detection uncertainty. The source reports cloud-to-ground location accuracy of about 200 m to 2 km; grid choices must reflect this.
4. Select the observation window independently of the realised events. Do not automatically exclude sea: lightning can occur there, but coverage quality beyond Singapore must be checked separately.
5. Project to a suitable metric CRS, document the CRS and window, retain zero-count cells, and adjust expectations for clipped area.
6. Report the selected null, alternative, period and scale. Any new event map, count map and reference distribution must be generated from the validated records.

## Verification and attribution

The generator checks boundary-point allocation, count conservation, a hand-worked chi-squared statistic, nearest-neighbour distance, the ordered-pair translation correction, monotonic K curves and agreement with the committed result record. It also rejects points outside the declared window.

Original code follows the repository's MIT code licence; original teaching prose and figures follow the repository's content licence. Data-source attribution and permissions must be recorded separately when the lightning case is added.
