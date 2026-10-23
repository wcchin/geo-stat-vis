"""Check the archived inputs needed by the distributions and group-comparison labs.

Run from repository root: python scripts/check_hdb_ura_inputs.py
This checks ingestion and common notebook operations, not full notebook execution,
upstream licensing or whether derived/geocoded fields can be redistributed.
"""
from pathlib import Path
import zipfile
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1] / "src/content/datasets/singapore_hdb_ura"
assert ROOT.is_dir(), f"Missing data directory: {ROOT}"

tables = {}
for year in (2013, 2023):
    file = ROOT / f"hdb_data_{year}.csv.xz"
    assert file.is_file() and file.stat().st_size > 0
    data = pd.read_csv(file, index_col=0)
    assert not data.empty and len(data.columns) > 1
    assert data.columns.is_unique
    assert data.index.notna().all()
    numeric = data.select_dtypes(include=np.number)
    assert not numeric.empty, f"No numeric columns in {file.name}"
    col = numeric.columns[0]
    assert numeric[col].notna().any()
    # Smoke-test operations used in Week 2's distribution workflow.
    assert not data[col].describe().empty
    assert int(data[col].notna().sum()) > 0
    tables[year] = data
    print(f"{file.name}: rows={len(data)}, cols={len(data.columns)}, "
          f"numeric={list(numeric.columns[:8])}, sample={list(data.columns[:12])}")

for name in ("master-plan-2019-planningarea.zip",
             "master-plan-2019-subzone_landuse_area.zip"):
    archive = ROOT / name
    assert archive.is_file() and zipfile.is_zipfile(archive)
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None, f"Corrupt member in {name}"
        members = [x for x in z.namelist() if not x.endswith("/")]
        lower = [x.lower() for x in members]
        assert any(x.endswith(".shp") for x in lower), f"No shapefile in {name}"
        assert any(x.endswith(".dbf") for x in lower), f"No DBF in {name}"
        assert any(x.endswith(".shx") for x in lower), f"No SHX in {name}"
        print(name, "verified ZIP members:", members[:12])

# Replicate the essential Week 3 ingest + CRS conversion path.
import geopandas as gpd

pa = gpd.read_file(ROOT / "master-plan-2019-planningarea.zip")
sz = gpd.read_file(ROOT / "master-plan-2019-subzone_landuse_area.zip")
for name, frame in (("planningarea", pa), ("subzone", sz)):
    assert not frame.empty
    assert frame.crs is not None, f"{name} has no declared CRS"
    assert frame.geometry.notna().any()
    projected = frame.to_crs("EPSG:3414")
    assert projected.crs.to_epsg() == 3414
    assert projected.geometry.notna().any()
    print(f"{name}: rows={len(frame)}, original_crs={frame.crs}, "
          f"fields={list(frame.columns[:12])}")

assert 2013 in tables and 2023 in tables
print("PASS: compressed HDB input loading, numeric summaries, boundary ZIP integrity, "
      "GeoPandas reads and EPSG:3414 conversions")
