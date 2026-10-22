# Neighbourhood storytelling example: Singapore, 2026

This directory supports Chapter 7 (7.0–7.6) with original figures and reproducible analysis. Reading sections are in `src/content/chapter_7`.

## Reproduce

Use Python 3.11+ and install pandas, numpy, scipy, pyproj, shapely, matplotlib. Run, in order:

```
python analyse.py
python plots.py
```

The prepared inputs are bundled, so these commands do not download observations. The environment must already have the dependencies installed.

`data/transactions.csv` and `data/blocks.csv` are the corrected Chapter 5 HDB extract, not the earlier LTSG coordinates. `data/stops.csv` is the prepared Chapter 3 volume-linked bus table. This is not a complete independent stop inventory. Keep PT_CODE as a string.

`data/hawkers_raw.json` is the official NEA directory API response, retrieved 22 October 2026. `data/sg_schools.csv` and `data/sg_parks.csv` are from the pinned mirror identified in the chapter. The prepared `pois.csv` removes fields unrelated to mapping. Source snapshots are deliberately preserved to make the analysis repeatable.

`block_metrics.csv` contains all 3,236 selling blocks and both radii. `selected_blocks.csv` contains the three illustrative cases. `audit.json` records counts, exclusions and selection. No randomly generated observations are used. Distances are EPSG:3414 metres. All searches include the radius boundary (distance <= radius). Nearby boarding activity is the sum of monthly weekday boardings divided by 22, not unique people or residents. All selected-block nearby stops have known weekday volumes at both radii.

Input source licence and attribution: Singapore Open Data Licence for the named agency datasets; OneMap geocoding/map data © Singapore Land Authority, subject to its open-data terms. The mirror's MIT software licence is separate. The chapter's source list provides originating dataset links and the mirror commit. Preserve these attributions when reusing the data. `_static/css/fonts/ComicNeue-OFL.txt` covers Comic Neue.

Input snapshots use lossless xz compression. Scripts expand a snapshot locally if the plain file is absent; remove expanded inputs to restore the bundled version. Analysis outputs are written as ordinary CSVs. Run analyse.py before plots.py after changing analysis parameters. SHA256SUMS.txt covers the committed dataset files and scripts. The shared book font and its licence are in `_static/css/fonts` at the repository root.


## Sources


- HDB, [Resale flat prices based on registration date from January 2017 onwards](https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view). Prepared sample: four-room transactions registered January–June 2026. The supplied teaching extract contains 5,379 records.
- LTA DataMall, [data and API resources](https://datamall.lta.gov.sg/). September 2026 bus-stop locations and transport-node activity files supplied by the instructor. This draft reuses the prepared Chapter 3 stop table; it does not claim a fresh download of the monthly volumes.
- NEA, [Dates of Hawker Centres Closure](https://data.gov.sg/datasets/d_bda4baa634dd1cc7a6c7cad5f19e2d68/view). The 2026 directory was retrieved through the official data.gov.sg datastore API on 22 October 2026; all 123 returned records have usable coordinates and an existing/new-existing status. Points do not establish continuous availability during closure periods.
- MOE, [General information of schools](https://data.gov.sg/datasets/d_688b934f82c1059ed0a6993d2a829089/view); NParks, [Parks](https://data.gov.sg/datasets/d_0542d48f0991541706b58059381a6eca/view). Coordinates and prepared records come from [this pinned, third-party source mirror](https://github.com/seehiong/autonomous-hdb-deepagents/tree/2a0df19534be15102658cebdda9267a653e79642/db/init/data), not a new live download from MOE or NParks. The mirror README cites 16 September 2026 retrieval and OneMap school geocoding. The parks table's update field is 22 April 2026. We use its point geometry rather than infer park entrances or polygons.
- HDB block coordinates also reuse the corrected HDB/OneMap-derived coordinate table prepared for Chapter 5 from the same pinned mirror. OneMap map and geocoding data: © Singapore Land Authority; [OneMap open data licence](https://www.onemap.gov.sg/legal/opendatalicence.html).
- URA, [Master Plan planning-area dataset listing](https://data.gov.sg/datasets?query=URA+planning+area&resultId=d_4765db0e87b9c86336792efe8a1f7a66). Background is the existing MP2019 planning-area teaching copy, not a newly retrieved revision.
- Public agency data is attributed under the [Singapore Open Data Licence](https://data.gov.sg/open-data-licence). The source mirror identifies this licence separately from its software licence. Comic Neue is bundled with its font licence.


The coordinate-provenance audit is bundled in `data/coordinate_provenance.json`. These are cross-source teaching comparisons, with periods and geometry limitations described in Chapter 7.
