# 7.4 Choosing tools after choosing the story

Tool choice should follow the analytical and communication tasks. Start with a storyboard, the operations it requires and the form the reader needs. A static sequence may communicate the main argument more clearly than a dashboard with many controls. Interactivity is valuable when it lets the reader ask a consequential additional question.

## A reproducible analytical core

For this example, a notebook or script can read the prepared HDB, bus and POI tables; transform coordinates; calculate distance-based selections; and produce maps and summaries. Python offers one route through pandas, pyproj, scipy and Matplotlib. QGIS offers another route for inspecting locations, checking projections and preparing spatial joins. The important requirement is that the operation and its parameters are recorded, rather than remembered from an editing session.

The bundled `analyse.py` records the selection rule and computes the same measures for all 3,236 selling blocks before extracting the three illustrations. The nearest-stop calculation uses geocoded bus records from the supplied volume-linked table. Radius counts include only those available records; they are not an independent census of every operating stop. Boarding sums use non-missing weekday averages and preserve a missing result when no activity is available. These definitions should travel with any notebook derived from this draft.

The `plots.py` script produces the original plates from the prepared tables and planning-area GeoJSON. Neither analytical reproduction nor figure reproduction needs a live geocoding service. The [reproducibility directory](../datasets/neighbourhood_story_2026/README.md) includes the inputs, scripts, selected-block metrics, source notes and checksums. Installation may require an internet connection, but rerunning the analysis on the bundled data does not require downloading the observations again.

## Choose an output for a reading task

| Output | A useful task | A responsibility that comes with it |
|---|---|---|
| Book figure sequence | Explain the central comparison in a stable order | Keep labels, captions and evidence visible in the static view |
| Notebook | Let students reproduce a measure and change its definition | Separate raw inputs from outputs; state dependencies and parameters |
| Interactive map | Let readers inspect local facilities or choose an address | Provide a usable default, keyboard-accessible controls and a static explanation |
| Dashboard | Compare a controlled set of measures or scenarios | Keep denominators and filter states explicit; avoid a decorative ranking score |

For this chapter, the first useful interaction would be a **500 m / 800 m radius switch**, because it tests a choice in the analysis. Selecting a POI category would be useful too, provided the reader sees what the category includes. A colour-picker or a rotating map would add less to the central question.

Do not let the availability of a tool determine the conclusion. A heatmap does not turn a set of locations into evidence of accessibility. A dashboard correlation does not control for confounding. A button labelled “best neighbourhood” would require defensible criteria and weights, not merely software that can calculate a score.

## Publish for inspection

A reader should be able to discover the source, reproduce the stated sample, inspect a selected block and understand any exclusions. Record source versions and retrieval dates. Keep bus-stop codes as strings so leading zeros survive. Keep source geometry and measured distances distinct from visual offsets; these figures do not jitter co-located records. Include readable alternative text and explain the key result in prose, so the argument is not locked inside the image.

For the eventual book, the static figures can carry the main reading path while a companion notebook supports exploration. An “Open in Colab” link can be added under the book's agreed notebook-sharing approach, with repository-hosted public input files where size and redistribution terms permit. The figure scripts run on the bundled inputs without a Google Drive mount.

**Try it.** Specify one control for an interactive version. State which reader question it answers, which calculation changes, and which warning must remain visible when the control changes.
