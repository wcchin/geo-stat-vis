# Third-party data, images and asset licensing

Geo-stat-vis has **separate licensing layers**:

- **Part 1 (Core Chapters) and Part 2 (Worked Examples):** Original prose, educational explanations and project-created diagrams are under [CC BY-NC-ND 4.0](LICENSE), except where third-party rights apply.
- **Part 3 (Data and Notebooks):** Original executable notebook code and reusable scripts are under [MIT](LICENSE-CODE). Notebook prose, learning prompts and original non-code artwork remain under CC BY-NC-ND 4.0. **Bundled datasets are governed separately** by their source licences.
- **Part 4 (Lecture Slides):** Original project-owned prose and graphics are under CC BY-NC-ND 4.0; externally sourced slide illustrations are not automatically included.
- **All parts:** External data, photographs, basemaps, boundaries, icons, figures, fonts and other third-party material retain their own providers' terms. Neither the book's CC licence nor the repository's MIT licence overrides them.

The following inventory describes *documented sources*, not blanket permission. **Unverified** means the use or redistribution conditions still need confirmation. The listed status is not legal advice or a guarantee that all contents of a teaching extract derive from the named provider.

## Source and permission inventory

| Resource or resource family | Source and licence information | Redistribution status | What remains to check |
| --- | --- | --- | --- |
| Synthetic point-pattern data and fictional demonstrations | Produced within this project; see [construction notes](../src/content/datasets/point_pattern_teaching/README.md) | Project-generated | Confirm any imported third-party visual assets separately |
| HDB 2013/2023 compressed teaching extracts | Intended public upstream: [HDB via data.gov.sg](https://data.gov.sg/); [Singapore Open Data Licence v1.0](https://data.gov.sg/open-data-licence) applies **only to eligible official source data** | **Unverified for these redistributed files** | Exact public dataset ID, date, transformations, geometry/geocoding provenance, personal/third-party fields, attribution |
| HDB location geocoding (possible enrichment in resale teaching extracts) | Singapore Land Authority (SLA), [OneMap Search API documentation](https://www.onemap.gov.sg/apidocs/); [Singapore Open Data Licence](https://www.onemap.gov.sg/legal/opendatalicence.html) and [OneMap API Terms of Service](https://www.onemap.gov.sg/legal/apitermsofservice.html) | **Upstream provider identified; exact derived fields and reuse circumstances unverified** | Confirm which extract coordinates were obtained from OneMap; endpoint, retrieval date, address matching and coordinate conversion; preserve SLA/OneMap attribution |\n| URA Master Plan 2019 planning areas and subzones | Intended public upstream: URA on [data.gov.sg](https://data.gov.sg/); see [subzone catalogue entry](https://data.gov.sg/datasets/d_8594ae9ff96d0c708bc2af633048edfb/view) and [Singapore Open Data Licence](https://data.gov.sg/open-data-licence) | **Unverified for these exact archives** | Identify precise download source/version for each ZIP, shapefile contents, date, additional third-party rights, attribution |
| DOSM household income (district) | [OpenDOSM household income catalogue](https://open.dosm.gov.my/data-catalogue/hh_income_district); **CC BY 4.0** expressly declared by the provider | Provider licence documented; attribution required | Ensure the specific bundled CSV/snapshots remain attributable to DOSM and preserve transformation information |
| PLANMalaysia administrative boundaries and derived coordinates | [PLANMalaysia boundary feature service](https://gisdev.planmalaysia.gov.my/server/rest/services/Hosted/Data_Sempadan_Daerah/FeatureServer/0) | **Redistribution terms unverified** | Obtain explicit reuse terms for the boundary response, generalised snapshots and derived geometry/coordinate distributions |
| FIRMS fire detection observations | Provider and snapshot details should be documented in the [Part 3 catalogue](../src/content/datasets/data_list.md) and the associated notebook | **Not yet fully audited** | Exact provider, acquisition date, attribution, data-specific reuse policy and any map imagery |
| Queenstown locations, Johor POIs and roads, Singapore transit OD records | Legacy teaching materials; see [catalogue](../src/content/datasets/data_list.md) | **Not approved for new redistribution** | Identify all upstream datasets, transformations, source terms and any personal/third-party content before bundling |
| Lecture slides, external figures, screenshots, icons, map tiles and fonts | Multiple potential providers | **Asset-by-asset audit outstanding** | Record origin, licence/permission, attribution, modifications and whether public redistribution is allowed |

## Required attribution pattern

For each external dataset or reused asset, keep a source-specific record with: **title; copyright holder/provider; direct source URL and dataset ID; licence and licence URL; retrieval date; modifications; attribution text; redistribution decision; reviewer/date**.

For official Singapore data, the [Singapore Open Data Licence](https://data.gov.sg/open-data-licence) requires conspicuous acknowledgement of the specific dataset and a link to the licence; it excludes personal data and third-party rights not licensed by the agency. Do not treat 'publicly accessible' as equivalent to 'cleared for republication'.

Suggested notice (fill in verified details only):

> Contains information from **[official dataset name]**, accessed **[retrieval date]** from **[government source URL]**, made available under the [Singapore Open Data Licence v1.0](https://data.gov.sg/open-data-licence). **[Describe changes, including derived/geocoded fields, separately.]**

For DOSM income data:

> Source: Department of Statistics Malaysia (DOSM), [Household Income by Administrative District](https://open.dosm.gov.my/data-catalogue/hh_income_district), used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Refer to each dataset's snapshot notes for selection, mapping and other processing.

Do not substitute a generic 'Government open data' label for the actual dataset title and provider.

## Release review procedure

1. Identify exact source(s) and upstream licence(s) for **every included dataset and third-party asset**.
2. Verify the **exact redistributed bytes and derived columns**, not only the original upstream dataset licence.
3. Verify that no protected personal information, proprietary enrichment or unlicensed third-party asset is present.
4. Add accurate source, licence, date, changes and attribution to its local README and visible notebook or figure caption as appropriate.
5. If permission cannot be established, **remove the copy from the public distribution** and replace it with authorised downloads or synthetic data. Deleting files from the current branch does not automatically purge past Git history.
6. Review public lecture-slide images and fonts separately.

**Current highest-priority unresolved item:** the four HDB/URA teaching-input files are already public although their dataset-specific provenance and licence clearance remain outstanding. Do not interpret this page as clearing them.
