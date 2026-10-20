# Point-pattern reading update

Scope: the existing quadrat, nearest-neighbour and Ripley K pages, preserving their paths and titles.

## What changed

- Quadrat: replace a short slide-like page with a self-study reading, three original figures, explicit multinomial/CSR reference, area-adjusted expectations, hand-worked statistic, degrees of freedom, one-sided alternatives, Monte Carlo inference, scale/origin sensitivity and self-checks.
- NNA: retain the established reading and local Woodlands illustrations, connect it to quadrat and K, add two reasoning checks and the original Clark–Evans paper. Remove the London worked-example link from this page to follow the regional-example preference.
- K: replace the incomplete pair-count expression with an indicator-based estimator; distinguish ordered/unordered pairs, K, L and L-r; explain and implement rectangular translation correction. Retain the local bus-stop motivation and add original synthetic paired-site and simulation-envelope figures. Distinguish pointwise bands from global inference and add published readings.

The same three synthetic patterns support the quadrat and K comparison. The source and result record make the construction auditable; it is never presented as empirical FIRMS fire or bus-stop data. Existing older assets are retained for references elsewhere in the book.

## Data access and remaining work

The agreed regional quadrat case is now **FIRMS fire detections in Sumatra, September 2026**, with VIIRS S-NPP selected consistently. This connects the point-pattern sequence with the later areal-autocorrelation case. Distinguish detection records from separate fires, preserve repeat observations unless the unit is deliberately changed, fix the land window and account for usable area and observation coverage.

Historical FIRMS downloads require Earthdata or email verification. No regional file has been obtained in this change, so the student page and data record explicitly keep empirical results pending. All existing new figures remain synthetic teaching constructions. The Moran page is not modified.

## Validation

Run `python scripts/point_pattern_examples.py` for hand-worked count, distance, pair-count, monotonicity and stored-result checks. Use `--write` to reproduce the five new SVG figures and synthetic data. The PR workflow runs the new checks and the full Jupyter Book build alongside existing notebook checks.
