# Semester 2610 notebook data inventory

Checked against the course and book main-branch file inventories on 20 October 2026. This is a content-hash inventory, not a completed dataset migration or a fresh notebook execution. Matching files elsewhere in the book are listed so they can be reused without uploading duplicate contents.

## Required publishing arrangement

- Keep a documented public data location for every notebook input and make its setup cell download only those files.
- Reuse `src/content/datasets/data_dirs/` for small datasets and a versioned dataset manifest. Keep illustrations in `src/content/resources/`. Distribute larger notebook data packages through GitHub Release assets rather than adding them all to Git history.
- Preserve existing public files and links while notebook paths are migrated. A file existing somewhere in the repository does not mean the notebook currently loads it correctly.
- Include helper modules (`utils.py`, the current course's `utils_week05.py` and `utils_week07.py`) where required, with explicit setup paths.
- Document dataset source, observation unit, period, CRS, field meanings and applicable reuse conditions. For source files that cannot be redistributed, document acquisition or provide a suitable teaching subset.
- Retain compressed tabular files and complete spatial datasets. Keep shapefile components together, preferably as one ZIP. Record which archive or extracted files a notebook uses rather than uploading both by default.
- For Colab, download data and helpers into the runtime and define one data directory; do not require an instructor-specific Google Drive path. Validate from a fresh runtime.

## File inventory

The course source paths below are under `GE5230-2610`. “Not found” means no identical blob was found outside generated `_build/` files in `geo-stat-vis`, including within differently named files. It does not inspect archive contents: an archive may contain an equivalent dataset that still needs unpacking and checking.

| Course source | Size (MiB) | Identical public book file | Next action |
|---|---:|---|---|
| `resources/MP14_SUBZONE_WEB_PL.zip` | 0.526 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/ODIO_all_202306.csv.xz` | 0.101 | `src/content/resources/lab_notebooks/ODIO_all_202306.csv.xz` | Reuse and fix notebook paths |
| `resources/West_Region/hex_800m.cpg` | 0.000 | `src/content/resources/data-week-01/master-plan-2019-planningarea.cpg` | Reuse and fix notebook paths |
| `resources/West_Region/hex_800m.dbf` | 0.062 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/West_Region/hex_800m.prj` | 0.000 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/West_Region/hex_800m.shp` | 0.058 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/West_Region/hex_800m.shx` | 0.003 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/bus_stop_loation.zip` | 0.381 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/citydata-Queenstown-20200915.csv.xz` | 1.144 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/citydata-date_2020-09-15.csv.xz` | 36.488 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/citydata-date_2020-09-15_simp.csv.zip` | 4.130 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/citydata-head_sample.csv` | 0.001 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/election.zip` | 10.105 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/election/election.dbf` | 6.099 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/election/election.prj` | 0.000 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/election/election.shp` | 13.683 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/election/election.shx` | 0.024 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/election/election_queen.gal` | 0.128 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/flowmap_flow_202005.csv` | 2.866 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/flowmap_location_202005.csv` | 0.297 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/hdb_data_2013.csv.xz` | 0.411 | `src/content/datasets/data_dirs/hdb_data_2013.csv.xz` | Reuse and fix notebook paths |
| `resources/hdb_data_2023.csv.xz` | 0.566 | `src/content/datasets/data_dirs/hdb_data_2023.csv.xz` | Reuse and fix notebook paths |
| `resources/master-plan-2019-planningarea.zip` | 0.483 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/master-plan-2019-subzone_landuse_area.zip` | 0.767 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/origin_destination_bus_202005.csv.xz` | 15.439 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/origin_destination_train_202005.csv.xz` | 1.765 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/segamat/gadm41_2.geojson` | 1.155 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/segamat/my_gempa_20250917.csv` | 0.788 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/segamat/penang.parquet` | 9.042 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/segamat/segamat.parquet` | 9.535 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/segamat/segamat_cats_regroup.json` | 0.001 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/segamat/segamat_earthquakes_data.zip` | 32.199 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/segamat/segamat_poi.parquet` | 4.522 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/segamat/segamat_road.parquet` | 43.599 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/segamat/segamat_roads2.parquet` | 44.383 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/segamat/segamat_roads3.parquet` | 35.630 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |
| `resources/train_station_location.zip` | 0.022 | Not found by content hash | Check notebook dependency and source metadata, then transfer required file |

The reflection-sheet document and QGIS `.qmd` metadata files were excluded from this dataset list. Some files listed above are alternate exports, generated outputs or optional inputs; their presence in the course resource folder does not make all of them required downloads.

## First data-backed pilot

1. Adapt the full point-pattern notebook to use the existing HDB 2023 file and the required planning/subzone boundaries, with its helper module supplied automatically.
2. Add a tested Colab setup and launch link. The synthetic NNA companion remains usable without external data.
3. For the Week 8 migration, reuse `ODIO_all_202306.csv.xz` and transfer the MP2014 boundary archive; retain the source notebook's caveat about transit-volume definitions.
4. Continue through KDE, clustering, LISA and flow mapping using an explicit per-notebook dependency list.

No missing dataset has been uploaded by this inventory change. Large archives, alternate exports and processed data still need to be matched to the actual notebook inputs before transfer.

## Large-file distribution recommendation

The 37 listed candidate files total approximately 276.4 MiB, including alternate exports and duplicate archive/extracted representations. The largest individual candidate is approximately 44.4 MiB. These sizes are an inventory, not the eventual per-student download requirement.

Use the same public `geo-stat-vis` project with two storage routes:

- Small inputs, helper scripts, documentation and a dataset manifest in Git.
- Larger, versioned data packages as Release assets, grouped by practical activity rather than one all-course download.

Suggested release tag: `teaching-data-v1` (not yet created). Notebook setup should use a fixed version, download only the relevant package, verify a published SHA-256 checksum, extract it into a local data directory, and reuse an existing verified download within a session. This avoids Google Drive mounting while keeping large changing binaries out of repository history. Do not use a moving latest-release URL for reproducible teaching examples.

GitHub documentation checked on 20 October 2026: regular Git files above 50 MiB generate a warning and files above 100 MiB are blocked. The Releases documentation states that each release asset must be under 2 GiB. See https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github and https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases .

This change records the inventory and proposed distribution design only. No release, release asset or missing dataset has been published.
