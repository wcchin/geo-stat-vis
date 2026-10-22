# 7.6 Putting the sequence together

Return to the opening question: “Is this neighbourhood convenient?” We can now give a more useful response: convenient for whom, for which activities, and measured how? The maps have not failed to answer a simple question. They have helped us recognise the decisions inside it.

The worked sequence begins with observed housing prices, introduces nearby stops and activity, then distinguishes amenity categories. The comparison shows why a familiar proxy can be incomplete: the Tampines and Woodlands illustrations have equal 500 m stop counts but very different boarding totals. The radius comparison then challenges the apparent firmness of a nearby-facility count. The ending asks the reader to specify a need before selecting a measure.

This is the chapter's central idea: **define convenience before comparing places**. Its human relevance comes from a recognisable decision. Its tension comes from a checked contrast. Its payoff is an improved way of evaluating evidence. The narrative has a purpose without manufacturing a winner or claiming that proximity determines price.

## A complete short-form version

A book chapter gives room for explanation. A six-panel slide sequence or short web story must carry the same logic more economically. The following storyboard is a draft of that version. It proposes a claim and an evidence check for every frame.

| Frame | Suggested headline | Evidence and guardrail |
|---|---|---|
| 1 | “What would make everyday life convenient for you?” | Open with an explicitly imagined reader scenario; invite a definition rather than state a universal preference. |
| 2 | “A resale-price map shows sales, not every home's value.” | Show 5,379 four-room registrations and block medians; retain period and sample definition. |
| 3 | “Equal stop counts can hide different activity.” | Show 18 stops for each selected Tampines and Woodlands block, beside about 70,173 and 11,701 weekday boardings. Label these illustrative blocks. |
| 4 | “Nearby facilities are not interchangeable.” | Show all three local maps at the same scale with separate POI categories; define park points and school records. |
| 5 | “Move the boundary, change the count.” | Show 500 m and 800 m results without changing cases or sources. Do not present either radius as a walking-time standard. |
| 6 | “Define convenience before comparing places.” | End with the measure, boundary, period and missing evidence. Invite a journey-time or facility-quality follow-up. |

A compelling final paragraph might read:

> These maps offer several views of the same city. Housing prices describe observed sales. Stop counts describe nearby records. Boarding totals describe transport activity. Amenity points describe selected facilities. To judge convenience, first decide which daily need matters, then choose evidence that measures it. A familiar map becomes more useful when we know which question it can answer.

## A self-study project

Develop an alternative sequence for a clearly named audience, using the bundled data as a starting point. Keep the analytical core inspectable. Your submission should contain a one-paragraph brief, four to six visual frames, a short methods note, a source list and a paragraph explaining what your story cannot establish.

Begin by selecting a specific need, such as reaching an everyday destination or finding a particular category of facility. Explain why the existing layers do or do not measure that need. If you change the case-selection rule, write it down before inspecting the new results. Retain one sensitivity comparison, such as a radius change or an alternative price measure. Conclude with the claim the evidence actually supports, even if it differs from the story you expected to tell.

Evaluate the work using four questions. Can the reader identify the central question? Does each visual contribute a new inference? Can another student reproduce the displayed numbers? Does the closing statement remain true when read without the surrounding explanations? Good visual communication requires all four.

## Reading resources

These papers support the narrative and framing concepts in this chapter. The audience brief and neighbourhood example are our teaching synthesis, rather than a framework attributed to either paper. Further empirical Singapore studies can be added to Part 2 after the core chapters are complete, following the book's agreed plan.

1. Segel, E., & Heer, J. (2010). **Narrative Visualization: Telling Stories with Data.** *IEEE Transactions on Visualization and Computer Graphics, 16*(6), 1139–1148. [DOI: 10.1109/TVCG.2010.179](https://doi.org/10.1109/TVCG.2010.179). [Author-hosted paper and summary](https://idl.uw.edu/papers/narrative). Read for the balance between author-directed narrative and reader exploration.
2. Hullman, J., & Diakopoulos, N. (2011). **Visualization Rhetoric: Framing Effects in Narrative Visualization.** *IEEE Transactions on Visualization and Computer Graphics, 17*(12), 2231–2240. [DOI: 10.1109/TVCG.2011.255](https://doi.org/10.1109/TVCG.2011.255). [Author-hosted paper and summary](https://www.hullmanlab.northwestern.edu/paper/2011/02/01/vis-rhetoric.html). Read for how representation, annotations and omissions guide interpretation.

## Data sources and reproducibility

- HDB, [Resale flat prices based on registration date from January 2017 onwards](https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view). Prepared sample: four-room transactions registered January–June 2026. The supplied teaching extract contains 5,379 records.
- LTA DataMall, [data and API resources](https://datamall.lta.gov.sg/). September 2026 bus-stop locations and transport-node activity files supplied by the instructor. This chapter reuses the prepared Chapter 3 stop table; it does not claim a fresh download of the monthly volumes.
- NEA, [Dates of Hawker Centres Closure](https://data.gov.sg/datasets/d_bda4baa634dd1cc7a6c7cad5f19e2d68/view). The 2026 directory was retrieved through the official data.gov.sg datastore API on 22 October 2026; all 123 returned records have usable coordinates and an existing/new-existing status. Points do not establish continuous availability during closure periods.
- MOE, [General information of schools](https://data.gov.sg/datasets/d_688b934f82c1059ed0a6993d2a829089/view); NParks, [Parks](https://data.gov.sg/datasets/d_0542d48f0991541706b58059381a6eca/view). Coordinates and prepared records come from [this pinned, third-party source mirror](https://github.com/seehiong/autonomous-hdb-deepagents/tree/2a0df19534be15102658cebdda9267a653e79642/db/init/data), not a new live download from MOE or NParks. The mirror README cites 16 September 2026 retrieval and OneMap school geocoding. The parks table's update field is 22 April 2026. We use its point geometry rather than infer park entrances or polygons.
- HDB block coordinates also reuse the corrected HDB/OneMap-derived coordinate table prepared for Chapter 5 from the same pinned mirror. OneMap map and geocoding data: © Singapore Land Authority; [OneMap open data licence](https://www.onemap.gov.sg/legal/opendatalicence.html).
- URA, [Master Plan planning-area dataset listing](https://data.gov.sg/datasets?query=URA+planning+area&resultId=d_4765db0e87b9c86336792efe8a1f7a66). Background is the existing MP2019 planning-area teaching copy, not a newly retrieved revision.
- Public agency data is attributed under the [Singapore Open Data Licence](https://data.gov.sg/open-data-licence). The source mirror identifies this licence separately from its software licence. Comic Neue is bundled with its font licence.

The [reproducibility directory](../datasets/neighbourhood_story_2026/README.md) contains prepared input tables, original plotting code, an audit and checksums. The seven reading sections are stored in the adjacent `chapter_7` directory. Analysis uses 500 m and 800 m straight-line radii in EPSG:3414. The local examples are illustrative blocks, not area-wide estimates, statistically tested price effects or neighbourhood rankings. 
