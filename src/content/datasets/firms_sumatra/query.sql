-- Public Portolan mirror of NASA FIRMS. Requires DuckDB httpfs and spatial extensions.
INSTALL httpfs; LOAD httpfs;
INSTALL spatial; LOAD spatial;
SELECT ST_Y(geometry) AS latitude, ST_X(geometry) AS longitude,
       acq_date, acq_datetime, sensor, satellite, instrument, quality, version,
       confidence, frp, daynight, type, scan, track
FROM read_parquet('https://data.source.coop/portolan-mirrors/firms-catalog/detections/year=2026/detections.parquet')
WHERE acq_date >= DATE '2026-09-01' AND acq_date < DATE '2026-10-01'
  AND sensor = 'VIIRS_SNPP'
  AND ST_Intersects(geometry, ST_MakeEnvelope(95,-6.5,106.5,6.5));
-- The saved CSV is the result of this query before confidence and main-island filtering.
