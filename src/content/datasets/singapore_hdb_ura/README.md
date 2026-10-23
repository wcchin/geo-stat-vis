# Singapore HDB resale and URA Master Plan 2019 teaching inputs

These four compressed source snapshots were copied **byte-for-byte** from the private GE5230-2610 repository's `resources/` directory on 23 October 2026 to support migration of the statistical foundations and spatial-analysis notebooks. The filename years describe the source teaching extracts; they do not imply that the extracts are the complete official datasets.

| File | Intended notebook uses | Source repository |
| --- | --- | --- |
| [hdb_data_2013.csv.xz](hdb_data_2013.csv.xz) | Comparing groups across years | GE5230-2610/resources |
| [hdb_data_2023.csv.xz](hdb_data_2023.csv.xz) | Distributions, classification, statistical comparisons, global point patterns | GE5230-2610/resources |
| [master-plan-2019-planningarea.zip](master-plan-2019-planningarea.zip) | Planning-area comparisons and spatial joins | GE5230-2610/resources |
| [master-plan-2019-subzone_landuse_area.zip](master-plan-2019-subzone_landuse_area.zip) | Subzone aggregation and point-pattern study windows | GE5230-2610/resources |

## Source and licence notes

The intended upstream public authorities are Singapore's **Housing & Development Board (HDB)** for resale transactions and **Urban Redevelopment Authority (URA)** for Master Plan 2019 areas. The [Singapore Open Data Licence](https://data.gov.sg/open-data-licence) permits use and redistribution of government open datasets subject to source attribution and third-party-rights exclusions. Relevant upstream entry points include [data.gov.sg](https://data.gov.sg/) and [URA Master Plan 2019 Subzone Boundary (No Sea)](https://data.gov.sg/datasets/d_8594ae9ff96d0c708bc2af633048edfb/view).

**Provenance still to verify before merging:** the exact original dataset IDs and retrieval dates; whether any HDB extract contains externally supplied geocoding, private enrichment or coordinates not covered by the government open-data licence; the original processing transformations; and licence compatibility for the archived boundary layers. The open-data licence for the official public data does not automatically cover every derived column in these GE5230 snapshots.

**Do not assume the book's CC BY-NC-ND licence applies to source government datasets.** Original provider licences, attributions and limitations remain applicable.

## Next validation step

Before converting the notebooks: inspect the archive members and CSV columns; check coordinates, temporal coverage, row counts, duplicates and nulls; verify spatial CRS; confirm the datasets contain no restricted/personal or third-party data; and record SHA-256 digests and a schema summary. Update notebook loaders to prefer local copies and fall back to a pinned public GitHub commit/tag after this PR is merged.
